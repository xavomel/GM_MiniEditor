from binascii import hexlify
from binascii import unhexlify
from struct import pack, unpack
from PyQt4 import QtGui, QtCore
from EditorMisc import *
import ghostUI
import sys
import os


data = None
data_folder_path = os.path.dirname(os.path.abspath(sys.argv[0])) + "\data"
mortals = []
scripts = []
activeMortal = None
_scenario = None
activeScenario = None


def open_file(filepath):
    with open(filepath, "rb") as _file:
        return hexlify(_file.read())


def save_file(filepath, filedata):
    with open(filepath, "wb") as _file:
        _file.write(unhexlify(filedata))


def address_to_number(address):
    # because addressing begins at 00400000 for some reason
    return int(address, 16) - int("00400000", 16)


def jump_to_address(address):
    return 2 * address_to_number(address)


def get_bytes(address, nr):
    index = jump_to_address(address)
    return data[index:index + nr * 2].upper()


def set_bytes(address, value):
    if len(address) != 8:
        raise ValueError
    if len(value) % 2 != 0:
        raise ValueError
    else:
        index = jump_to_address(address)
        return data[:index] + value.lower() + data[index + len(value):]


def hex_to_float(hex_var):
    return unpack('!f', hex_var.decode('hex'))[0]


def float_to_hex(float_var):
    h = hex(unpack('<I', pack('<f', float_var))[0])[2:]

    # because leading zeroes disappear
    if len(h) < 8:
        return h.zfill(8)
    else:
        return h


def reverse_hex_string(hex_string):
    return "".join(reversed([hex_string[i:i+2] for i in range(0, len(hex_string), 2)]))


def add_hex(hex1, hex2):
    h = hex(int(hex1, 16) + int(hex2, 16))
    return "00" + h[2:]


def calculate_plasm(mean_terror, mortal_count, scenario_id):
    if scenario_id == 2:
        x = mean_terror * (mortal_count - 4)
        x /= mortal_count
    elif scenario_id == 10:
        x = mean_terror * (mortal_count - 3) + 75
        x /= mortal_count - 2
    elif scenario_id == 14:
        x = mean_terror * (mortal_count - 5) + 75 * 5
        x /= mortal_count
    else:
        x = mean_terror

    raw_plasm = x * (x * (x - 9) + 1500) / (30 + 5 * x)

    if mortal_count < 20:
        threshold = 50 * mortal_count

        if raw_plasm <= threshold:
            return raw_plasm
        else:
            return threshold + threshold * (raw_plasm - threshold) / (2000 - threshold)
    else:
        return raw_plasm


###########################################################


class MainWindow(QtGui.QMainWindow, ghostUI.Ui_MainWindow):
    def __init__(self, parent=None):
        super(MainWindow, self).__init__(parent)
        self.setupUi(self)

    def find_scenarios(self):
        self.resetComboBox(self.comboBox_3, "pick scenario")
        self.comboBox_3.setEnabled(True)
        data_folder_content = os.listdir(data_folder_path)

        index = 1
        for item in data_folder_content:
            if item.startswith("scenario_") and os.path.isdir(data_folder_path + "\\" + item):
                self.comboBox_3.addItem("")
                self.comboBox_3.setItemText(index, item)
                index += 1

    def load_scenario(self, filepath):
        global _scenario
        _scenario = None

        try:
            with open(filepath, "rb") as _file:
                raw = _file.read()
                values = raw.split()

                # file empty
                if os.path.getsize(filepath) == 0:
                    return -1

                scen = Scenario()
                scen.setAttributes(values)

                _scenario = scen

        except IOError:
            return -1

        if not _scenario:
            return -1

    def load_mortals(self, filepath):
        global mortals
        mortals = []
        self.resetComboBox(self.comboBox_4, "pick mortals")

        try:
            with open(filepath, "rb") as _file:
                raw = _file.read()
                byMortal = raw.split("\n")

                if os.path.getsize(filepath) == 0:
                    return -1

                for i, x in enumerate(byMortal):
                    values = x.split()

                    mort = Mortal()
                    mort.setAttributes(values)

                    mortals.append(mort)
                    self.comboBox_4.addItem("")
                    self.comboBox_4.setItemText(i + 1, "Mortal %d" % (i + 1))

        except IOError:
            return -1

        if not mortals:
            return -1

    def scenarioChanged(self):
        global activeScenario
        scenario = self.sender().currentText()

        if not scenario or scenario == "pick scenario":
            activeScenario = None
            self.resetComboBox(self.comboBox_4, "pick mortals")
            self.label.setText("Choose a scenario")
            self.label_2.setHidden(True)
            self.spinBox.setEnabled(False)
            self.spinBox.setHidden(True)
            self.spinBox_2.setEnabled(False)
            self.spinBox_2.setHidden(True)
            self.lineEdit.setHidden(True)
            self.comboBox_5.setEnabled(False)
            self.comboBox_5.setHidden(True)
            self.checkBox17.setEnabled(False)
            self.checkBox17.setHidden(True)
            return
        else:
            activeScenario = scenario
            self.label.setText("Choose a mortal")

        scenario_folder_path = str(data_folder_path + "\\" + scenario)
        self.label_2.setText(" ")
        for filename in os.listdir(scenario_folder_path):
            if filename.endswith(".txt"):
                scenarioName = filename.replace(".txt", "")
                self.label_2.setText(scenarioName)
                self.label_2.setHidden(False)
                break

        if self.load_mortals(scenario_folder_path + "\mortals") != -1:
            self.comboBox_4.setEnabled(True)

        if self.load_scenario(scenario_folder_path + "\scenario") != -1:
            address = _scenario.max_haunters
            if address != Constants.NULL:
                self.spinBox.setValue(int(get_bytes(address, 1), 16))
                self.spinBox.setEnabled(True)
                self.spinBox.setHidden(False)

            address = _scenario.mean_terror_push[0]
            if address != Constants.NULL:
                if _scenario.mean_terror_call[0] != Constants.NULL:
                    self.checkBox17.setEnabled(True)
                    self.checkBox17.setHidden(False)
                    self.getState_ManualTerror(_scenario)

                    address = add_hex(address, "00000001")
                    h = get_bytes(address, 4)
                    h = reverse_hex_string(h)
                    value = hex_to_float(h)

                    if not self.checkBox17.isChecked():
                        self.spinBox_2.setValue(value)
                        self.spinBox_2.setEnabled(True)
                    self.spinBox_2.setHidden(False)

                    value = self.spinBox_2.value()
                    scenario_id = self.comboBox_3.currentIndex()
                    plasm = int(calculate_plasm(value, len(mortals), scenario_id))
                    self.lineEdit.setText(str(plasm))
                    self.lineEdit.setHidden(False)

            address = _scenario.mood[0]
            if address != Constants.NULL:
                self.comboBox_5.setCurrentIndex(int(get_bytes(address, 1), 16) - 39)
                self.comboBox_5.setEnabled(True)
                self.comboBox_5.setHidden(False)
        else:
            self.spinBox.setEnabled(False)
            self.spinBox.setHidden(True)
            self.spinBox_2.setEnabled(False)
            self.spinBox_2.setHidden(True)
            self.lineEdit.setHidden(True)
            self.comboBox_5.setEnabled(False)
            self.comboBox_5.setHidden(True)
            self.checkBox17.setEnabled(False)
            self.checkBox17.setHidden(True)

    def mortalChanged(self):
        global activeMortal
        mortal_id = self.sender().currentIndex()

        if mortal_id > 0:
            activeMortal = mortal_id
            mortal = mortals[mortal_id - 1]
            text = ("Mortal %d" % mortal_id)
            if mortal.name != Constants.NULL:
                text += " : %s" % mortal.name
            self.label.setText(text)
        else:
            activeMortal = None
            mortal = Mortal()
            self.label.setText("Choose a mortal")

        if mortal.willpower != Constants.NULL:
            self.horizontalSlider.setEnabled(True)
            h = get_bytes(mortal.willpower, 2).zfill(8)
            h = reverse_hex_string(h)
            value = hex_to_float(h)
            self.horizontalSlider.setValue(value)
        else:
            self.horizontalSlider.setEnabled(False)

        if mortal.insanity[0] == "0":
            self.horizontalSlider_2.setEnabled(True)
            h = get_bytes(mortal.insanity, 2).zfill(8)
            h = reverse_hex_string(h)
            value = hex_to_float(h)
            self.horizontalSlider_2.setValue(value)
        elif mortal.insanity[0] == "?" and self.checkBox11.isChecked():
            address = "0" + mortal.insanity[1:]

            self.horizontalSlider_2.setEnabled(True)
            h = get_bytes(address, 2).zfill(8)
            h = reverse_hex_string(h)
            value = hex_to_float(h)
            self.horizontalSlider_2.setValue(value)
        else:
            self.horizontalSlider_2.setEnabled(False)

        if mortal.belief != Constants.NULL:
            self.horizontalSlider_3.setEnabled(True)
            h = get_bytes(mortal.belief, 2).zfill(8)
            h = reverse_hex_string(h)
            value = hex_to_float(h)

            # because belief scales inversely
            if value == 0:
                reverse_value = self.horizontalSlider_3.maximum()
            else:
                reverse_value = -value % self.horizontalSlider_3.maximum()

            self.horizontalSlider_3.setValue(reverse_value)
        else:
            self.horizontalSlider_3.setEnabled(False)

        if mortal.terror[0] == "0":
            self.horizontalSlider_4.setEnabled(True)
            h = get_bytes(mortal.terror, 4)
            h = reverse_hex_string(h)
            value = hex_to_float(h)
            self.horizontalSlider_4.setValue(value)
        elif mortal.terror[0] == "?" and self.checkBox17.isChecked():
            address = "0" + mortal.terror[1:]

            self.horizontalSlider_4.setEnabled(True)
            h = get_bytes(address, 4)
            h = reverse_hex_string(h)
            value = hex_to_float(h)
            self.horizontalSlider_4.setValue(value)
        else:
            self.horizontalSlider_4.setEnabled(False)

        if mortal.fearcon[0] == "0":
            self.comboBox.setEnabled(True)
            self.comboBox.setCurrentIndex(int(get_bytes(mortal.fearcon, 1), 16))
        elif mortal.fearcon[0] == "?" and self.checkBox13.isChecked():
            address = "0" + mortal.fearcon[1:]

            self.comboBox.setEnabled(True)
            self.comboBox.setCurrentIndex(int(get_bytes(address, 1), 16))
        else:
            self.comboBox.setEnabled(False)
            self.comboBox.blockSignals(True)
            self.comboBox.setCurrentIndex(0)
            self.comboBox.blockSignals(False)

        if mortal.fearsub[0] == "0":
            self.comboBox_2.setEnabled(True)
            self.comboBox_2.setCurrentIndex(int(get_bytes(mortal.fearsub, 1), 16))
        elif mortal.fearsub[0] == "?" and self.checkBox13.isChecked():
            address = "0" + mortal.fearsub[1:]

            self.comboBox_2.setEnabled(True)
            self.comboBox_2.setCurrentIndex(int(get_bytes(address, 1), 16))
        else:
            self.comboBox_2.setEnabled(False)
            self.comboBox_2.blockSignals(True)
            self.comboBox_2.setCurrentIndex(0)
            self.comboBox_2.blockSignals(False)

        if mortal.fearext[0] == "0" and self.checkBox15.isChecked():
            self.comboBox_6.setEnabled(True)
            self.comboBox_6.setCurrentIndex(int(get_bytes(mortal.fearext, 1), 16))
        elif mortal.fearext[0] == "?" and self.checkBox15.isChecked():
            address = "0" + mortal.fearext[1:]

            self.comboBox_6.setEnabled(True)
            self.comboBox_6.setCurrentIndex(int(get_bytes(address, 1), 16))
        else:
            self.comboBox_6.setEnabled(False)
            self.comboBox_6.blockSignals(True)
            self.comboBox_6.setCurrentIndex(0)
            self.comboBox_6.blockSignals(False)

    def sliderMoved(self):
        slider = self.sender()
        if slider.isSliderDown():
            id = slider.value()
            sliderText = slider.objectName()
            if sliderText == "horizontalSlider":
                self.show_tooltip(slider, "Willpower: %d" % id)
            elif sliderText == "horizontalSlider_2":
                self.show_tooltip(slider, "Insanity: %d" % id)
            elif sliderText == "horizontalSlider_3":
                self.show_tooltip(slider, "Belief: %d" % id)
            elif sliderText == "horizontalSlider_4":
                self.show_tooltip(slider, "Terror: %d" % id)

    def setWillpower(self):
        if activeMortal:
            address = mortals[activeMortal - 1].willpower
            id = self.sender().value()
            hex_id = float_to_hex(id)[:4]
            value = reverse_hex_string(hex_id)
            global data
            data = set_bytes(address, value)

    def setInsanity(self):
        if activeMortal:
            address = mortals[activeMortal - 1].insanity
            if address[0] == "?":
                address = "0" + address[1:]

            id = self.sender().value()
            hex_id = float_to_hex(id)[:4]
            value = reverse_hex_string(hex_id)
            global data
            data = set_bytes(address, value)

    def setBelief(self):
        if activeMortal:
            address = mortals[activeMortal - 1].belief
            id = self.sender().value()

            # because belief scales inversely
            if id == 0:
                reverse_id = self.sender().maximum()
            else:
                reverse_id = -id % self.sender().maximum()

            hex_id = float_to_hex(reverse_id)[:4]
            value = reverse_hex_string(hex_id)
            global data
            data = set_bytes(address, value)

    def setTerror(self):
        if activeMortal:
            address = mortals[activeMortal - 1].terror
            if address[0] == "?":
                address = "0" + address[1:]

            id = self.sender().value()
            hex_id = float_to_hex(id)
            value = reverse_hex_string(hex_id)
            global data
            data = set_bytes(address, value)

    def setConciousFear(self):
        if activeMortal:
            address = mortals[activeMortal - 1].fearcon
            if address[0] == "?":
                address = "0" + address[1:]

            id = self.sender().currentIndex()
            value = '{:02x}'.format(id)
            global data
            data = set_bytes(address, value)

    def setUnconciousFear(self):
        if activeMortal:
            address = mortals[activeMortal - 1].fearsub
            if address[0] == "?":
                address = "0" + address[1:]

            id = self.sender().currentIndex()
            value = '{:02x}'.format(id)
            global data
            data = set_bytes(address, value)

    def setExtraFear(self):
        if activeMortal:
            address = mortals[activeMortal - 1].fearext
            if address[0] == "?":
                address = "0" + address[1:]

            id = self.sender().currentIndex()
            value = '{:02x}'.format(id)
            global data
            data = set_bytes(address, value)

    def setHaunterSlots(self):
        if _scenario and _scenario.max_haunters != Constants.NULL:
            id = self.sender().value()
            value = '{:02x}'.format(id)
            global data
            data = set_bytes(_scenario.max_haunters, value)

    def setMeanTerror(self):
        if _scenario and _scenario.mean_terror_push[0] != Constants.NULL:
            float_value = self.sender().value()

            scenario_id = self.comboBox_3.currentIndex()
            plasm = int(calculate_plasm(float_value, len(mortals), scenario_id))
            self.lineEdit.setText(str(plasm))

            if not self.checkBox17.isChecked():
                address = add_hex(_scenario.mean_terror_push[0], "00000001")
                value = float_to_hex(float_value)
                value = reverse_hex_string(value)

                global data
                data = set_bytes(address, value)

    def setMood(self):
        if _scenario:
            id = self.sender().currentIndex() + 39

            for address in _scenario.mood:
                if address != Constants.NULL:
                    value = '{:02x}'.format(id)
                    global data
                    data = set_bytes(address, value)

    def setGhostLevel(self):
        if self.sender().isEnabled():
            global data
            chosen_level = self.sender().currentIndex() - 1
            checked = chosen_level != -1

            data_list = list(data)
            level_list = []

            mod_file = open("data\mods\Global Ghost Level", "rb")
            byLine = mod_file.read().split("\n")
            mod_file.close()

            for line in byLine:
                level = line.split()
                code_address = level[0]
                code_bytes = level[1]
                level_list.append([code_address, code_bytes])

            if checked:
                chosen_bytes = level_list[chosen_level][1]

                for level in level_list:
                    code_bytes = level[1]
                    level[1] = chosen_bytes[:8] + code_bytes[8:16] + chosen_bytes[16:]

            for level in level_list:
                code_address = level[0]
                code_bytes = level[1]
                index = jump_to_address(code_address)
                data_list[index:index + len(code_bytes)] = code_bytes

            data = "".join(data_list)

    def setBytesAtAddress(self):
        text, ok = QtGui.QInputDialog.getText(self, ' ', 'Enter address, bytes (separated with @)')
        input = []
        address = ""
        value = ""

        if ok:
            input = text.split("@")

        if len(input) == 2:
            address = str(input[0]).strip()
            value = str(input[1]).strip()

            try:
                global data
                data = set_bytes(address, value)
            except ValueError:
                self.show_message("Invalid arguments")
            else:
                self.show_message("Set %s at %s" % (value, address))

    def setUnlimitedPlasm(self):
        if self.sender().isEnabled():
            global data
            checked = self.sender().isChecked()

            if checked:
                # disable power cost
                data = set_bytes("004A78D0", "D8E090909090")
                data = set_bytes("0042F7B9", "D8C890909090")

                # disable red power bar when plasm is insufficient
                # by replacing coordinates of texture loaded from ui/powerbar4.tga
                # from red bar to blue bar
                data = set_bytes("0041E99D", "6800008E3E")
                data = set_bytes("0041E9A2", "680000303E")
                data = set_bytes("0041E9B1", "680000583E")

                # disable red text when plasm is insufficient
                data = set_bytes("0042F519", "6A00")
            else:
                # enable power cost
                data = set_bytes("004A78D0", "D80588019500")
                data = set_bytes("0042F7B9", "D82588019500")

                # enable red power bar when plasm is insufficient
                data = set_bytes("0041E99D", "680000543E")
                data = set_bytes("0041E9A2", "680000303E")
                data = set_bytes("0041E9B1", "680000103E")

                # enable red text when plasm is insufficient
                data = set_bytes("0042F519", "6A03")

    def setUnlimitedGoldplasm(self):
        if self.sender().isEnabled():
            global data
            checked = self.sender().isChecked()

            if checked:
                # disable red color when goldplasm is insufficient
                data = set_bytes("004729F8", "EB43")

                # enable buying when goldplasm is insufficient (doesn't work when it's negative)
                data = set_bytes("00473311", "EB6B")

                # disables subtraction of power cost from current goldplasm when buying powers
                data = set_bytes("00473458", "EB6B")

            else:
                # enable red color when goldplasm is insufficient
                data = set_bytes("004729F8", "7743")

                # disable buying when goldplasm is insufficient (doesn't work when it's negative)
                data = set_bytes("00473311", "776B")

                # enable subtraction of power cost from current goldplasm when buying powers
                data = set_bytes("00473458", "776B")

    def setInstantPowerRecharge(self):
        if self.sender().isEnabled():
            global data
            checked = self.sender().isChecked()
            data_list = list(data)

            mod_file = open("data\mods\Instant Power Recharge", "rb")
            byLine = mod_file.read().split("\n")
            mod_file.close()

            for line in byLine:
                changes = line.split()
                code_address = changes[0]
                code_bytes = ""

                if checked:
                    code_bytes = "00000000"
                else:
                    code_bytes = changes[1]

                index = jump_to_address(code_address)
                data_list[index:index + len(code_bytes)] = code_bytes

            data = "".join(data_list)

    def setResponsivePortraits(self):
        if self.sender().isEnabled():
            global data
            checked = self.sender().isChecked()

            if checked:
                data = set_bytes("004266B7", "EB41")  # ghosts
                data = set_bytes("00428F42", "90909090909090908B87F00000009090909090909090")  # mortals
            else:
                data = set_bytes("004266B7", "7441")  # ghosts
                data = set_bytes("00428F42", "85C90F84210100008B87F000000085C00F8513010000")  # mortals

    def setGhostCloning(self):
        if self.sender().isEnabled():
            global data
            checked = self.sender().isChecked()

            if checked:
                data = set_bytes("0045C4BE", "83F8037526")  # clones, jump to "success" if eax != 3 (empty portrait)
                data = set_bytes("0045C5F3", "00")  # grey-out when adding
                data = set_bytes("0045C7D2", "00")  # grey-out when removing
                data = set_bytes("0045C977", "00")  # grey-out when recommended
                data = set_bytes("0045BE03", "00")  # grey-out when changing tabs
            else:
                data = set_bytes("0045C4BE", "83F8027426")  # clones
                data = set_bytes("0045C5F3", "01")  # grey-out when adding
                data = set_bytes("0045C7D2", "01")  # grey-out when removing
                data = set_bytes("0045C977", "01")  # grey-out when recommended
                data = set_bytes("0045BE03", "01")  # grey-out when changing tabs

    def setInsideOutsideOnAll(self):
        if self.sender().isEnabled():
            global data
            checked = self.sender().isChecked()

            if checked:
                data = set_bytes("004CB01B", "9090")
            else:
                data = set_bytes("004CB01B", "743F")

    def setIgnoreWards(self):
        if self.sender().isEnabled():
            global data
            checked = self.sender().isChecked()

            if checked:
                data = set_bytes("00606985", "909090909090")  # bind from menu
                data = set_bytes("00606787", "EB22")  # bind from field
                data = set_bytes("00606C24", "EB1C")  # benching
                data = set_bytes("0060867F", "EB1B")  # unknown bind reject
            else:
                data = set_bytes("00606985", "0F8486000000")  # bind from menu
                data = set_bytes("00606787", "7422")  # bind from field
                data = set_bytes("00606C24", "741C")  # benching
                data = set_bytes("0060867F", "741B")  # unknown bind reject

    def setDisableFireExtinguishers(self):
        if self.sender().isEnabled():
            global data
            checked = self.sender().isChecked()

            if checked:
                data = set_bytes("0060139E", "6860029000")  # ReactionScream
            else:
                data = set_bytes("0060139E", "68B0FF8F00")  # ReactionExtinguishFire

    def setFetterSharing(self):
        if self.sender().isEnabled():
            global data
            checked = self.sender().isChecked()

            if checked:
                data = set_bytes("0047C332", "9090909090909090")
            else:
                data = set_bytes("0047C332", "39B7880000007407")

    def setMovableRestlessGhosts(self):
        if self.sender().isEnabled():
            global data
            checked = self.sender().isChecked()

            if checked:
                # enable binding
                data = set_bytes("0042C5EE", "909090909090909090909090")
                data = set_bytes("0042C612", "EB0D")

                # bind button visuals
                data = set_bytes("0042DB44", "9090909090909090")  # disable gray-out
                data = set_bytes("0042C2F0", "90909090")  # enable hover effect

                # enable highlights
                # works for all ghosts when hovering over ghost
                # works for discovered ghosts when hovering over portrait
                data = set_bytes("00418B01", "9090909090909090")

                # enable highlight workarounds
                data = set_bytes("00426371", "9090909090909090")  # undiscovered ghosts
                data = set_bytes("00426379", "909090909090EB08")  # hidden ghosts
            else:
                # disable binding
                data = set_bytes("0042C5EE", "3935D8C694000F840A010000")
                data = set_bytes("0042C612", "750D")

                # bind button visuals
                data = set_bytes("0042DB44", "391DD8C69400741F")  # enable gray-out
                data = set_bytes("0042C2F0", "85C9742B")  # disable hover effect

                # disable highlights
                data = set_bytes("00418B01", "39902C0100007522")

                # disable highlight workarounds
                data = set_bytes("00426371", "3990F80100007408")  # undiscovered ghosts
                data = set_bytes("00426379", "3990300100007408")  # hidden ghosts

    def setDisableMadnessImmunity(self):
        if self.sender().isEnabled():
            global data
            checked = self.sender().isChecked()

            if checked:
                # calamity
                data = set_bytes("00503B5E", "9090909090")
                data = set_bytes("00503C0D", "9090909090")
                data = set_bytes("008D583E", "803F")
                data = set_bytes("008D58A6", "803F")
                # deadfellas
                data = set_bytes("00514CED", "9090909090")
                data = set_bytes("00514D9F", "9090909090")
                data = set_bytes("008D8326", "803F")
                data = set_bytes("008D838E", "803F")
                # suspects
                data = set_bytes("0052C88E", "9090909090")
                data = set_bytes("0052CAFD", "9090909090")
                data = set_bytes("008DAB9E", "803F")
                data = set_bytes("008DACD6", "803F")
                # poultrygeist
                data = set_bytes("00509679", "9090909090")
                data = set_bytes("00509A99", "9090909090")
                data = set_bytes("008D61D6", "803F")
                data = set_bytes("008D63DE", "803F")
                # spooky
                data = set_bytes("00548149", "9090909090")
                data = set_bytes("005481FC", "9090909090")
                data = set_bytes("008DFFC6", "803F")
                data = set_bytes("008E002E", "803F")
            else:
                # calamity
                data = set_bytes("00503B5E", "A33C588D00")
                data = set_bytes("00503C0D", "A3A4588D00")
                data = set_bytes("008D583E", "0000")
                data = set_bytes("008D58A6", "0000")
                # deadfellas
                data = set_bytes("00514CED", "A324838D00")
                data = set_bytes("00514D9F", "A38C838D00")
                data = set_bytes("008D8326", "0000")
                data = set_bytes("008D838E", "0000")
                # suspects
                data = set_bytes("0052C88E", "A39CAB8D00")
                data = set_bytes("0052CAFD", "A3D4AC8D00")
                data = set_bytes("008DAB9E", "0000")
                data = set_bytes("008DACD6", "0000")
                # poultrygeist
                data = set_bytes("00509679", "A3D4618D00")
                data = set_bytes("00509A99", "A3DC638D00")
                data = set_bytes("008D61D6", "0000")
                data = set_bytes("008D63DE", "0000")
                # spooky
                data = set_bytes("00548149", "A3C4FF8D00")
                data = set_bytes("005481FC", "A32C008E00")
                data = set_bytes("008DFFC6", "0000")
                data = set_bytes("008E002E", "0000")
            
            index = self.comboBox_4.currentIndex()
            self.comboBox_4.setCurrentIndex(0)
            self.comboBox_4.setCurrentIndex(index)
            
    def setUncoverFears(self):
        if self.sender().isEnabled():
            global data
            checked = self.sender().isChecked()

            if checked:
                data = set_bytes("0047ED3D", "B8010000009090")
                data = set_bytes("0047ED60", "B80100000090")
            else:
                data = set_bytes("0047ED3D", "8B84B7FC000000")
                data = set_bytes("0047ED60", "8B81F8000000")

    def setUnlockMissingFears(self):
        if self.sender().isEnabled():
            global data
            checked = self.sender().isChecked()
            data_list = list(data)

            mod_file = open("data\mods\Unlock Missing Fears", "rb")
            byLine = mod_file.read().split("\n")
            mod_file.close()

            for line in byLine:
                changes = line.split()
                code_address = changes[0]
                fear_address = changes[2]
                code_bytes = ""
                fear_bytes = ""

                if checked:
                    code_bytes = "909090909090"
                    fear_bytes = changes[3]
                else:
                    code_bytes = changes[1]
                    fear_bytes = "00"

                index = jump_to_address(code_address)
                data_list[index:index + len(code_bytes)] = code_bytes

                index = jump_to_address(fear_address)
                data_list[index:index + len(fear_bytes)] = fear_bytes

            data = "".join(data_list)
            index = self.comboBox_4.currentIndex()
            self.comboBox_4.setCurrentIndex(0)
            self.comboBox_4.setCurrentIndex(index)
            
    def setDisableCalmingEffects(self):
        if self.sender().isEnabled():
            global data
            checked = self.sender().isChecked()

            if checked:
                data = set_bytes("00775CC9", "E92501000090")
            else:
                data = set_bytes("00775CC9", "0F8524010000")

    def setUnlockExtraFears(self):
        if self.sender().isEnabled():
            global data
            checked = self.sender().isChecked()
            data_list = list(data)

            mod_file = open("data\mods\Unlock Extra Fears", "rb")
            byLine = mod_file.read().split("\n")
            mod_file.close()

            for line in byLine:
                changes = line.split()
                code_address = changes[0]
                code_bytes = ""

                if checked:
                    code_bytes = "9090909090"
                else:
                    code_bytes = changes[1]

                index = jump_to_address(code_address)
                data_list[index:index + len(code_bytes)] = code_bytes

            if not checked:
                self.reset_extra_fears(data_list)

            data = "".join(data_list)
            index = self.comboBox_4.currentIndex()
            self.comboBox_4.setCurrentIndex(0)
            self.comboBox_4.setCurrentIndex(index)

    def reset_extra_fears(self, data_list):
        scenario_dirs = list()
        data_folder_content = os.listdir(data_folder_path)
        for content in data_folder_content:
            content_path = data_folder_path + "\\" + content

            if content.startswith("scenario") and os.path.isdir(content_path):
                scenario_dirs.append(content_path)

        for path in scenario_dirs:
            mortals_path = path + "\mortals"

            if os.path.isfile(mortals_path):
                with open(mortals_path, "rb") as mortals_file:
                    raw = mortals_file.read()
                    byMortal = raw.split("\n")

                    for mortal in byMortal:
                        addresses = mortal.split()

                        if len(addresses) >= 2:
                            extra_fear_address = addresses[2]

                            if extra_fear_address != Constants.NULL:
                                if extra_fear_address.startswith("?"):
                                    extra_fear_address = "0" + extra_fear_address[1:]

                                code_bytes = "00"
                                index = jump_to_address(extra_fear_address)
                                data_list[index:index + len(code_bytes)] = code_bytes

    def setFixColdPhobia(self):
        if self.sender().isEnabled():
            global data
            checked = self.sender().isChecked()

            if checked:
                data = set_bytes("0057B4D3", "6A02")
                data = set_bytes("0057C2C9", "6A02")
            else:
                data = set_bytes("0057B4D3", "6A09")
                data = set_bytes("0057C2C9", "6A09")

    def setManualTerror(self):
        if self.sender().isEnabled():
            global data
            checked = self.sender().isChecked()

            if checked:
                data = set_bytes(_scenario.mean_terror_push[0], "9090909090")
                data = set_bytes(_scenario.mean_terror_call[0], "9090909090")
                self.spinBox_2.setEnabled(False)
            else:
                data = set_bytes(_scenario.mean_terror_push[0], _scenario.mean_terror_push[1])
                data = set_bytes(_scenario.mean_terror_call[0], _scenario.mean_terror_call[1])
                self.spinBox_2.setEnabled(True)

                # reset terror values for non-static mortals
                for m in mortals:
                    if m.terror[0] == "?":
                        address = "0" + m.terror[1:]
                        data = set_bytes(address, "00000000")

            data_list = list(data)

            mod_file = open("data\mods\Manual Terror", "rb")
            byLine = mod_file.read().split("\n")
            mod_file.close()

            for line in byLine:
                changes = line.split()
                code_address = changes[0]
                code_bytes = ""

                if checked:
                    code_bytes = "9090909090"
                else:
                    code_bytes = changes[1]

                index = jump_to_address(code_address)
                data_list[index:index + len(code_bytes)] = code_bytes

            data = "".join(data_list)
            index = self.comboBox_4.currentIndex()
            self.comboBox_4.setCurrentIndex(0)
            self.comboBox_4.setCurrentIndex(index)

    def setContinuousPowerRecasting(self):
        if self.sender().isEnabled():
            global data
            checked = self.sender().isChecked()
            data_list = list(data)

            mod_file = open("data\mods\Continuous Power Recasting", "rb")
            byLine = mod_file.read().split("\n")
            mod_file.close()

            for line in byLine:
                code_address = line
                code_bytes = ""

                if checked:
                    code_bytes = "00000000"
                else:
                    code_bytes = "FEFFFFFF"

                index = jump_to_address(code_address)
                data_list[index:index + len(code_bytes)] = code_bytes

            data = "".join(data_list)

    # code injection replaces some of the Trainspooking code
    # causing the cinematic after What Lies Over the Cuckoos Nest to no longer be displayed
    def setGhostRetraining(self):
        if self.sender().isEnabled():
            global data
            checked = self.sender().isChecked()

            if checked:
                # enable code injection jump
                data = set_bytes("004ADB49", "E932F10900")

                # enable code injection
                data = set_bytes("0054CC80", "83FE0A0F8DED0EF6FF8D94B5A80000008B02C1E0058B8018D"
                                             "9900039C80F85AB0EF6FF8B4C2414890AE9C80EF6FF90909090")

                # enable UI changes
                data = set_bytes("00471135", "00")
                data = set_bytes("0047105B", "9090")
                data = set_bytes("00471069", "9090")
            else:
                # disable code injection jump
                data = set_bytes("004ADB49", "83FE0A7D28")

                # disable code injection
                data = set_bytes("0054CC80", "81EC00040000568BF1E802AEECFF6A00687103000068200F8"
                                             "E00E821F7F6FF83C40450E868ECF6FFE82359F6FFA140808C00")

                # disable UI changes
                data = set_bytes("00471135", "01")
                data = set_bytes("0047105B", "7533")
                data = set_bytes("00471069", "7413")

    def setExplorationMode(self):
        if self.sender().isEnabled():
            global data
            checked = self.sender().isChecked()

            if checked:
                data = set_bytes("0078EFCD", "EB2E")
            else:
                data = set_bytes("0078EFCD", "742E")

    def setScript(self):
        if self.sender().isEnabled():
            global data
            checked = self.sender().isChecked()

            obj_name = self.sender().objectName().split("_")
            idx = int(obj_name[2])
            code_address = scripts[idx][0]

            if checked:
                code_bytes = scripts[idx][1]
                data = set_bytes(code_address, code_bytes)
            else:
                default_other_object_script = "68D01B9000"
                data = set_bytes(code_address, default_other_object_script)

    def getState_UnlimitedPlasm(self):
        self.checkBox1.blockSignals(True)

        valA = get_bytes("004A78D0", 6)
        valB = get_bytes("0042F7B9", 6)
        valC = get_bytes("0041E99D", 5)
        valD = get_bytes("0041E9A2", 5)
        valE = get_bytes("0041E9B1", 5)
        valF = get_bytes("0042F519", 2)
        if valA == "D8E090909090" and valB == "D8C890909090":
            if valC == "6800008E3E" and valD == "680000303E" and valE == "680000583E" and valF == "6A00":
                self.checkBox1.setChecked(True)
                retStr = ("OK", True, "")
            else:
                self.checkBox1.setToolTip(Constants.FEATURE_DISABLED)
                self.checkBox1.setEnabled(False)
                retStr = ("OUTDATED", "Unlimited Plasm", "v0.3.7")
        elif valA == "D80588019500" and valB == "D82588019500" and valC == "680000543E" and valD == "680000303E" and valE == "680000103E" and valF == "6A03":
            self.checkBox1.setChecked(False)
            retStr = ("OK", False, "")
        else:
            retStr = ("FAILED", "Unlimited Plasm", "")

        self.checkBox1.blockSignals(False)
        return retStr

    def getState_UnlimitedGoldplasm(self):
        self.checkBox2.blockSignals(True)

        valA = get_bytes("004729F8", 2)
        valB = get_bytes("00473311", 2)
        valC = get_bytes("00473458", 2)
        valD = get_bytes("00472A02", 1)  # old
        valE = get_bytes("0047331E", 1)  # old
        valF = get_bytes("00473465", 1)  # old
        if valD == "00" and valE == "00" and valF == "00":
            self.checkBox2.setToolTip(Constants.FEATURE_DISABLED)
            self.checkBox2.setEnabled(False)
            retStr = ("OUTDATED", "Unlimited Goldplasm", "v0.3.7")
        elif valA == "EB43" and valB == "EB6B" and valC == "EB6B":
            self.checkBox2.setChecked(True)
            retStr = ("OK", True, "")
        elif valA == "7743" and valB == "776B" and valC == "776B":
            self.checkBox2.setChecked(False)
            retStr = ("OK", False, "")
        else:
            retStr = ("FAILED", "Unlimited Goldplasm", "")

        self.checkBox2.blockSignals(False)
        return retStr

    def getState_InstantPowerRecharge(self):
        self.checkBox3.blockSignals(True)

        valA = get_bytes("0090D91C", 4)
        valB = get_bytes("0090DA1C", 4)
        valC = get_bytes("0090D97C", 4)
        valD = get_bytes("0090E81C", 4)
        valE = get_bytes("0090E8DC", 4)
        valF = get_bytes("0090E6BC", 4)
        valG = get_bytes("00788B77", 6)  # old
        if valG == "B80000000090":
            self.checkBox3.setToolTip(Constants.FEATURE_DISABLED)
            self.checkBox3.setEnabled(False)
            retStr = ("OUTDATED", "Instant Power Recharge", "v0.3.7")
        elif valA == "00000000" and valB == "00000000" and valC == "00000000" and valD == "00000000" and valE == "00000000" and valF == "00000000":
            self.checkBox3.setChecked(True)
            retStr = ("OK", True, "")
        elif valA == "0F000000" and valB == "1E000000" and valC == "3C000000" and valD == "5A000000" and valE == "96000000" and valF == "2C010000":
            self.checkBox3.setChecked(False)
            retStr = ("OK", False, "")
        else:
            retStr = ("FAILED", "Instant Power Recharge", "")

        self.checkBox3.blockSignals(False)
        return retStr

    def getState_ResponsivePortraits(self):
        self.checkBox4.blockSignals(True)

        valA = get_bytes("004266B7", 2)
        valB = get_bytes("00428F42", 22)
        if valA == "EB41" and valB == "90909090909090908B87F00000009090909090909090":
            self.checkBox4.setChecked(True)
            retStr = ("OK", True, "")
        elif valA == "7441" and valB == "85C90F84210100008B87F000000085C00F8513010000":
            self.checkBox4.setChecked(False)
            retStr = ("OK", False, "")
        else:
            retStr = ("FAILED", "Responsive Empty Portraits", "")

        self.checkBox4.blockSignals(False)
        return retStr

    def getState_GhostCloning(self):
        self.checkBox5.blockSignals(True)

        valA = get_bytes("0045C4BE", 5)
        valB = get_bytes("0045C5F3", 1)
        valC = get_bytes("0045C7D2", 1)
        valD = get_bytes("0045C977", 1)
        valE = get_bytes("0045BE03", 1)
        valF = get_bytes("0045C4C1", 1)  # old
        if valF == "EB":
            self.checkBox5.setToolTip(Constants.FEATURE_DISABLED)
            self.checkBox5.setEnabled(False)
            retStr = ("OUTDATED", "Ghost Cloning", "v0.3.7")
        elif valA == "83F8037526" and valB == "00" and valC == "00" and valD == "00" and valE == "00":
            self.checkBox5.setChecked(True)
            retStr = ("OK", True, "")
        elif valA == "83F8027426" and valB == "01" and valC == "01" and valD == "01" and valE == "01":
            self.checkBox5.setChecked(False)
            retStr = ("OK", False, "")
        else:
            retStr = ("FAILED", "Ghost Cloning", "")

        self.checkBox5.blockSignals(False)
        return retStr

    def getState_InsideOutsideOnAll(self):
        self.checkBox6.blockSignals(True)

        val = get_bytes("004CB01B", 2)
        if val == "9090":
            self.checkBox6.setChecked(True)
            retStr = ("OK", True, "")
        elif val == "743F":
            self.checkBox6.setChecked(False)
            retStr = ("OK", False, "")
        else:
            retStr = ("FAILED", "Inside/Outside On All Ghosts", "")

        self.checkBox6.blockSignals(False)
        return retStr

    def getState_IgnoreWards(self):
        self.checkBox7.blockSignals(True)

        valA = get_bytes("00606985", 6)
        valB = get_bytes("00606787", 2)
        valC = get_bytes("00606C24", 2)
        valD = get_bytes("0060867F", 2)
        if valA == "909090909090" and valB == "EB22" and valC == "EB1C" and valD == "EB1B":
            self.checkBox7.setChecked(True)
            retStr = ("OK", True, "")
        elif valA == "0F8486000000" and valB == "7422" and valC == "741C" and valD == "741B":
            self.checkBox7.setChecked(False)
            retStr = ("OK", False, "")
        else:
            retStr = ("FAILED", "Ignore Wards", "")

        self.checkBox7.blockSignals(False)
        return retStr

    def getState_DisableFireExtinguishers(self):
        self.checkBox8.blockSignals(True)

        val = get_bytes("0060139E", 5)
        if val == "6860029000":
            self.checkBox8.setChecked(True)
            retStr = ("OK", True, "")
        elif val == "68B0FF8F00":
            self.checkBox8.setChecked(False)
            retStr = ("OK", False, "")
        else:
            retStr = ("FAILED", "Disable Fire Extinguishers", "")

        self.checkBox8.blockSignals(False)
        return retStr

    def getState_FetterSharing(self):
        self.checkBox9.blockSignals(True)

        val = get_bytes("0047C332", 8)
        if val == "9090909090909090":
            self.checkBox9.setChecked(True)
            retStr = ("OK", True, "")
        elif val == "39B7880000007407":
            self.checkBox9.setChecked(False)
            retStr = ("OK", False, "")
        else:
            retStr = ("FAILED", "Fetter Sharing", "")

        self.checkBox9.blockSignals(False)
        return retStr

    def getState_MovableRestlessGhosts(self):
        self.checkBox10.blockSignals(True)

        valA = get_bytes("0042C5EE", 12)
        valB = get_bytes("0042C612", 2)
        valC = get_bytes("0042DB44", 8)
        valD = get_bytes("0042C2F0", 4)
        valE = get_bytes("00418B01", 8)
        valF = get_bytes("00426371", 8)
        valG = get_bytes("00426379", 8)
        if valA == "909090909090909090909090" and valB == "EB0D":
            if valC == "9090909090909090" and valD == "90909090" and valE == "9090909090909090" and valF == "9090909090909090" and valG == "909090909090EB08":
                self.checkBox10.setChecked(True)
                retStr = ("OK", True, "")
            else:
                self.checkBox10.setToolTip(Constants.FEATURE_DISABLED)
                self.checkBox10.setEnabled(False)
                retStr = ("OUTDATED", "Movable Restless Ghosts", "v0.4.0")
        elif valA == "3935D8C694000F840A010000" and valB == "750D" and valC == "391DD8C69400741F" and valD == "85C9742B" and valE == "39902C0100007522" and valF == "3990F80100007408" and valG == "3990300100007408":
            self.checkBox10.setChecked(False)
            retStr = ("OK", False, "")
        else:
            retStr = ("FAILED", "Movable Restless Ghosts", "")

        self.checkBox10.blockSignals(False)
        return retStr

    def getState_DisableMadnessImmunity(self):
        self.checkBox11.blockSignals(True)

        valA = get_bytes("00503B5E", 5)
        valB = get_bytes("00514CED", 5)
        valC = get_bytes("0052C88E", 5)
        valD = get_bytes("00509679", 5)
        valE = get_bytes("005481FC", 5)
        if valA == "9090909090" and valB == "9090909090" and valC == "9090909090" and valD == "9090909090" and valE == "9090909090":
            self.checkBox11.setChecked(True)
            retStr = ("OK", True, "")
        elif valA == "A33C588D00" and valB == "A324838D00" and valC == "A39CAB8D00" and valD == "A3D4618D00" and valE == "A32C008E00":
            self.checkBox11.setChecked(False)
            retStr = ("OK", False, "")
        else:
            retStr = ("FAILED", "Disable Madness Immunity", "")

        self.checkBox11.blockSignals(False)
        return retStr

    def getState_UncoverFears(self):
        self.checkBox12.blockSignals(True)

        valA = get_bytes("0047ED3D", 7)
        valB = get_bytes("0047ED60", 6)
        if valA == "B8010000009090" and valB == "B80100000090":
            self.checkBox12.setChecked(True)
            retStr = ("OK", True, "")
        elif valA == "8B84B7FC000000" and valB == "8B81F8000000":
            self.checkBox12.setChecked(False)
            retStr = ("OK", False, "")
        else:
            retStr = ("FAILED", "Uncover Fears", "")

        self.checkBox12.blockSignals(False)
        return retStr

    def getState_UnlockMissingFears(self):
        self.checkBox13.blockSignals(True)

        valA = get_bytes("00531DD7", 6)
        valB = get_bytes("008DC658", 1)
        if valA == "909090909090":
            self.checkBox13.setChecked(True)
            retStr = ("OK", True, "")
        elif valA == "891524C78D00" and valB == "00":
            self.checkBox13.setChecked(False)
            retStr = ("OK", False, "")
        else:
            retStr = ("FAILED", "Unlock Missing Fears", "")

        self.checkBox13.blockSignals(False)
        return retStr

    def getState_DisableCalmingEffects(self):
        self.checkBox14.blockSignals(True)

        val = get_bytes("00775CC9", 6)
        if val == "E92501000090":
            self.checkBox14.setChecked(True)
            retStr = ("OK", True, "")
        elif val == "0F8524010000":
            self.checkBox14.setChecked(False)
            retStr = ("OK", False, "")
        else:
            retStr = ("FAILED", "Disable Calming Effects", "")

        self.checkBox14.blockSignals(False)
        return retStr

    def getState_UnlockExtraFears(self):
        self.checkBox15.blockSignals(True)

        valA = get_bytes("00531DE7", 5)
        valB = get_bytes("008DC72C", 1)
        if valA == "9090909090":
            self.checkBox15.setChecked(True)
            retStr = ("OK", True, "")
        elif valA == "A32CC78D00" and valB == "00":
            self.checkBox15.setChecked(False)
            retStr = ("OK", False, "")
        else:
            retStr = ("FAILED", "Unlock Extra Fears", "")

        self.checkBox15.blockSignals(False)
        return retStr

    def getState_FixColdPhobia(self):
        self.checkBox16.blockSignals(True)

        valA = get_bytes("0057B4D3", 2)
        valB = get_bytes("0057C2C9", 2)
        if valA == "6A02" and valB == "6A02":
            self.checkBox16.setChecked(True)
            retStr = ("OK", True, "")
        elif valA == "6A09" and valB == "6A09":
            self.checkBox16.setChecked(False)
            retStr = ("OK", False, "")
        else:
            retStr = ("FAILED", "Fix Cold Phobia", "")

        self.checkBox16.blockSignals(False)
        return retStr

    def getState_ManualTerror(self, scenario):
        self.checkBox17.blockSignals(True)

        valA = get_bytes(scenario.mean_terror_push[0], 5)
        valB = get_bytes(scenario.mean_terror_call[0], 5)
        if valA == "9090909090" and valB == "9090909090":
            self.checkBox17.setChecked(True)
            self.spinBox_2.setEnabled(False)
        elif valA[:2] == scenario.mean_terror_push[1][:2] and valB == scenario.mean_terror_call[1]:
            self.checkBox17.setChecked(False)
            self.spinBox_2.setEnabled(True)
        else:
            self.show_message("Manual Terror: undefined state",
                              "Choose your preferred setting again \n(unless you made custom changes)")

        self.checkBox17.blockSignals(False)

    def getState_GlobalGhostLevel(self):
        self.comboBox_7.blockSignals(True)

        valA = get_bytes("008F8928", 1)
        valB = get_bytes("008F89C8", 1)
        valC = get_bytes("008F892D", 12)
        valD = get_bytes("008F89CD", 12)
        valE = get_bytes("008F1F68", 1)  # old
        valF = get_bytes("008F31F8", 1)  # old
        valG = get_bytes("008F4AB8", 1)  # old

        if valE == valF == valG:
            self.comboBox_7.setToolTip(Constants.FEATURE_DISABLED)
            self.comboBox_7.setEnabled(False)
            retStr = ("OUTDATED", "Global Ghost Level", "v0.4.0")
        elif valA == valB and valC == valD:
            level = int(valA, 16) + 1
            self.comboBox_7.setCurrentIndex(level)
            retStr = ("OK", True, "")
        elif valA == "00" and valB == "08" and valC == "000000000000000A00000028" \
                and valD == "0000004F0000004F0000004F":
            self.comboBox_7.setCurrentIndex(0)
            retStr = ("OK", False, "")
        else:
            retStr = ("FAILED", "Global Ghost Level", "")

        self.comboBox_7.blockSignals(False)
        return retStr

    def getState_ContinuousPowerRecasting(self):
        self.checkBox18.blockSignals(True)

        valA = get_bytes("0090DAFC", 4)
        valB = get_bytes("0090E5DC", 4)
        valC = get_bytes("0090E79C", 4)
        valD = get_bytes("0090E95C", 4)
        if valA == "00000000" and valB == "00000000" and valC == "00000000" and valD == "00000000":
            self.checkBox18.setChecked(True)
            retStr = ("OK", True, "")
        elif valA == "FEFFFFFF" and valB == "FEFFFFFF" and valC == "FEFFFFFF" and valD == "FEFFFFFF":
            self.checkBox18.setChecked(False)
            retStr = ("OK", False, "")
        else:
            retStr = ("FAILED", "Continuous Power Recasting", "")

        self.checkBox18.blockSignals(False)
        return retStr

    def getState_GhostRetraining(self):
        self.checkBox19.blockSignals(True)

        valA = get_bytes("004ADB49", 5)
        valB = get_bytes("0054CC80", 50)
        valC = get_bytes("00471135", 1)
        valD = get_bytes("0047105B", 2)
        valE = get_bytes("00471069", 2)
        if valA == "E932F10900" and valB == "83FE0A0F8DED0EF6FF8D94B5A80000008B02C1E0058B8018D" \
                                            "9900039C80F85AB0EF6FF8B4C2414890AE9C80EF6FF90909090" \
                and valC == "00" and valD == "9090" and valE == "9090":
            self.checkBox19.setChecked(True)
            retStr = ("OK", True, "")
        elif valA == "83FE0A7D28" and valB == "81EC00040000568BF1E802AEECFF6A00687103000068200F8" \
                                              "E00E821F7F6FF83C40450E868ECF6FFE82359F6FFA140808C00" \
                and valC == "01" and valD == "7533" and valE == "7413":
            self.checkBox19.setChecked(False)
            retStr = ("OK", False, "")
        else:
            retStr = ("FAILED", "Ghost Retraining", "")

        self.checkBox19.blockSignals(False)
        return retStr

    def getState_ExplorationMode(self):
        self.checkBox20.blockSignals(True)

        valA = get_bytes("0078EFCD", 2)
        if valA == "EB2E":
            self.checkBox20.setChecked(True)
            retStr = ("OK", True, "")
        elif valA == "742E":
            self.checkBox20.setChecked(False)
            retStr = ("OK", False, "")
        else:
            retStr = ("FAILED", "Exploration Mode", "")

        self.checkBox20.blockSignals(False)
        return retStr

    def getState_Scripts(self):
        for idx, elem in enumerate(scripts):
            checkbox = self.findChild(QtGui.QCheckBox, "checkBox_scr_%d" % idx)
            checkbox.blockSignals(True)

            code_address = elem[0]
            code_bytes = elem[1]

            valA = get_bytes(code_address, 5)
            if valA == code_bytes:
                checkbox.setChecked(True)
            else:
                checkbox.setChecked(False)

            checkbox.blockSignals(False)

    def open_data(self):
        filepath = QtGui.QFileDialog.getOpenFileName(self, 'Open file', "", "*.exe")
        if not filepath:
            return

        global data
        data = open_file(filepath)
        self.show_message("File opened")

        self.enable_widgets()
        self.integrity_check()
        self.find_scenarios()

    def save_data(self):
        filepath = QtGui.QFileDialog.getSaveFileName(self, 'Save file', "", "*.exe")
        if not filepath:
            return

        save_file(filepath, data)
        self.show_message("File saved")

    def about(self):
        self.show_message(Constants.VERSION, "created by Xavomel")

    # reads data from file only once (if scripts window doesn't exist)
    # subsequent clicks just reopen the window
    def show_scripts_window(self):
        if not hasattr(self, "scripts_window"):
            mod_file = open("data\mods\Scripts", "rb")
            byLine = mod_file.read().split("\n")
            mod_file.close()

            global scripts
            for line in byLine:
                changes = line.split()
                code_address = changes[0]
                code_bytes = changes[1]
                script_name = changes[2]
                comment = ""
                if len(changes) >= 4:
                    comment = " - " + " ".join(changes[3:])
                scripts.append([code_address, code_bytes, script_name, comment])

            self.scripts_window = ghostUI.ScriptsWindow(self)
            self.scripts_window.setupCheckBoxes(scripts)
            self.getState_Scripts()

        self.scripts_window.show()

    def show_tooltip(self, sender, text):
        position = sender.mapToGlobal(QtCore.QPoint(0, 0))
        QtGui.QToolTip.showText(position, text, None)

    def show_message(self, text, informative_text=None, title=" "):
        msg = QtGui.QMessageBox()
        msg.setText(text)
        if informative_text:
            msg.setInformativeText(informative_text)
        msg.setWindowTitle(title)
        msg.exec_()

    def resetComboBox(self, QComboBox, item0_name):
        QComboBox.clear()
        QComboBox.addItem("")
        QComboBox.setItemText(0, item0_name)
        QComboBox.setEnabled(False)

    def enable_widgets(self):
        self.actionSave.setEnabled(True)
        self.actionScripts.setEnabled(True)
        self.pushButton_9.setEnabled(True)
        self.comboBox_7.setEnabled(True)
        self.checkBox1.setEnabled(True)
        self.checkBox2.setEnabled(True)
        self.checkBox3.setEnabled(True)
        self.checkBox4.setEnabled(True)
        self.checkBox5.setEnabled(True)
        self.checkBox6.setEnabled(True)
        self.checkBox7.setEnabled(True)
        self.checkBox8.setEnabled(True)
        self.checkBox9.setEnabled(True)
        self.checkBox10.setEnabled(True)
        self.checkBox11.setEnabled(True)
        self.checkBox12.setEnabled(True)
        self.checkBox13.setEnabled(True)
        self.checkBox14.setEnabled(True)
        self.checkBox15.setEnabled(True)
        self.checkBox16.setEnabled(True)
        self.checkBox18.setEnabled(True)
        self.checkBox19.setEnabled(True)
        self.checkBox20.setEnabled(True)

    def integrity_check(self):
        stateList = list()
        stateList.append(self.getState_GlobalGhostLevel())
        stateList.append(self.getState_UnlimitedPlasm())
        stateList.append(self.getState_UnlimitedGoldplasm())
        stateList.append(self.getState_InstantPowerRecharge())
        stateList.append(self.getState_ContinuousPowerRecasting())
        stateList.append(self.getState_ResponsivePortraits())
        stateList.append(self.getState_GhostCloning())
        stateList.append(self.getState_FetterSharing())
        stateList.append(self.getState_InsideOutsideOnAll())
        stateList.append(self.getState_MovableRestlessGhosts())
        stateList.append(self.getState_IgnoreWards())
        stateList.append(self.getState_UncoverFears())
        stateList.append(self.getState_DisableCalmingEffects())
        stateList.append(self.getState_UnlockExtraFears())
        stateList.append(self.getState_FixColdPhobia())
        stateList.append(self.getState_DisableFireExtinguishers())
        stateList.append(self.getState_DisableMadnessImmunity())
        stateList.append(self.getState_UnlockMissingFears())
        stateList.append(self.getState_GhostRetraining())
        stateList.append(self.getState_ExplorationMode())

        text = ""
        outdated_counter = 0
        failed_counter = 0

        for state in stateList:
            if state[0] == "OUTDATED":
                text += "%s\t%s\t%s\n" % (state[0], state[1].ljust(28), state[2])
                outdated_counter += 1
            elif state[0] == "FAILED":
                text += "%s\t%s\n" % (state[0], state[1])
                failed_counter += 1

        if text != "":
            dialog_length = 300
            label_text = ""
            label2_text = ""

            if outdated_counter > 0:
                dialog_length += 50
                label_text = Constants.OUTDATED
                label2_text = Constants.OUTDATED_SOLUTION

            if failed_counter == Constants.NO_OF_CHECKS:
                label_text = Constants.INVALID
                label2_text = Constants.INVALID_SOLUTION
            elif failed_counter > 0:
                if label_text == "" and label2_text == "":
                    dialog_length += 50
                    label_text += Constants.FAILED
                    label2_text += Constants.FAILED_SOLUTION
                else:
                    dialog_length += 140
                    label_text += "\n\n" + Constants.FAILED
                    label2_text += "\n\n\n" + Constants.FAILED_SOLUTION

            self.integrity_dialog.setFixedSize(400, dialog_length)
            self.integrity_dialog.label.setText(label_text)
            self.integrity_dialog.label_2.setText(label2_text)
            self.integrity_dialog.plainTextEdit.setPlainText(text)
            self.integrity_dialog.show()


def main():
    app = QtGui.QApplication(sys.argv)
    form = MainWindow()
    form.show()
    app.exec_()


main()
