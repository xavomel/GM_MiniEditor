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
activeMortal = None
_scenario = None
activeScenario = None
goldplasm_costs = [50, 75, 100, 250, 500, 750, 1000, 1500, 2000, 2500]


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
                addresses = raw.split()

                # file empty
                if os.path.getsize(filepath) == 0:
                    return -1

                temp = Scenario()

                j = len(addresses)
                if j > 0:
                    temp.setMaxHaunters(addresses[0])
                if j > 1:
                    addr_list = addresses[1].split(",")
                    temp.setMood(addr_list)
                if j > 2:
                    addr_list = addresses[2].split(",")
                    temp.setMeanTerrorPush(addr_list)
                if j > 3:
                    addr_list = addresses[3].split(",")
                    temp.setMeanTerrorCall(addr_list)

                _scenario = temp

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
                    current = x.split()
                    temp = Mortal()

                    j = len(current)
                    if j > 0 and len(current[0]) == 8:
                        temp.setFearsub(current[0])
                    if j > 1 and len(current[1]) == 8:
                        temp.setFearcon(current[1])
                    if j > 2 and len(current[2]) == 8:
                        temp.setFearext(current[2])
                    if j > 3 and len(current[3]) == 8:
                        temp.setBelief(current[3])
                    if j > 4 and len(current[4]) == 8:
                        temp.setInsanity(current[4])
                    if j > 5 and len(current[5]) == 8:
                        temp.setWillpower(current[5])
                    if j > 6 and len(current[6]) == 8:
                        temp.setTerror(current[6])
                    if j > 7:
                        temp.setName(current[7])

                    mortals.append(temp)
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
            if address != "NULL":
                self.spinBox.setValue(int(get_bytes(address, 1), 16))
                self.spinBox.setEnabled(True)
                self.spinBox.setHidden(False)

            address = _scenario.mean_terror_push[0]
            if address != "NULL":
                if _scenario.mean_terror_call[0] != "NULL":
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
            if address != "NULL":
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
            if mortal.name != "NULL":
                text += " : %s" % mortal.name
            self.label.setText(text)
        else:
            activeMortal = None
            mortal = Mortal()
            self.label.setText("Choose a mortal")

        if mortal.willpower != "NULL":
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

        if mortal.belief != "NULL":
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
        if _scenario and _scenario.max_haunters != "NULL":
            id = self.sender().value()
            value = '{:02x}'.format(id)
            global data
            data = set_bytes(_scenario.max_haunters, value)

    def setMeanTerror(self):
        if _scenario and _scenario.mean_terror_push[0] != "NULL":
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
                if address != "NULL":
                    value = '{:02x}'.format(id)
                    global data
                    data = set_bytes(address, value)

    # there are 47 ghosts but for some reason raindancer is at 48, wavemaster is at 50, stormtalon is at 51
    def setGhostLevel(self):
        if self.sender().isEnabled():
            global data
            level = self.sender().currentIndex() - 1
            checked = level != -1

            data_list = list(data)

            mod_file = open("data\mods\Global Ghost Level", "rb")
            byLine = mod_file.read().split("\n")
            mod_file.close()

            for line in byLine:
                changes = line.split()
                code_address = changes[0]
                code_bytes = ""

                if checked:
                    code_bytes = '{:02x}'.format(level)
                else:
                    code_bytes = changes[1]

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
                address = "00472A02"
                for i in range(10):
                    data = set_bytes(address, "0000")
                    address = add_hex(address, "00000006")

                # enable buying when goldplasm is insufficient (doesn't work when it's negative)
                address = "0047331E"
                for i in range(10):
                    data = set_bytes(address, "0000")
                    address = add_hex(address, "0000000A")

                # disables subtraction of power cost from current goldplasm when buying powers
                address = "00473465"
                for i in range(10):
                    data = set_bytes(address, "0000")
                    address = add_hex(address, "0000000A")

            else:
                # enable red color when goldplasm is insufficient
                address = "00472A02"
                for cost in goldplasm_costs:
                    value = '{:02x}'.format(cost).zfill(4)
                    value = reverse_hex_string(value)
                    data = set_bytes(address, value)
                    address = add_hex(address, "00000006")

                # disable buying when goldplasm is insufficient (doesn't work when it's negative)
                address = "0047331E"
                for cost in goldplasm_costs:
                    value = '{:02x}'.format(cost).zfill(4)
                    value = reverse_hex_string(value)
                    data = set_bytes(address, value)
                    address = add_hex(address, "0000000A")

                # enable subtraction of power cost from current goldplasm when buying powers
                address = "00473465"
                for cost in goldplasm_costs:
                    value = '{:02x}'.format(cost).zfill(4)
                    value = reverse_hex_string(value)
                    data = set_bytes(address, value)
                    address = add_hex(address, "0000000A")

    def setInstantPowerRecharge(self):
        if self.sender().isEnabled():
            global data
            checked = self.sender().isChecked()

            if checked:
                data = set_bytes("00788B77", "B80000000090")
            else:
                data = set_bytes("00788B77", "8B801CD99000")

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
                data = set_bytes("0045C4C1", "EB")  # clones
                data = set_bytes("0045C5F3", "00")  # grey-out when adding
                data = set_bytes("0045C7D2", "00")  # grey-out when removing
                data = set_bytes("0045C977", "00")  # grey-out when recommended
                data = set_bytes("0045BE03", "00")  # grey-out when changing tabs
            else:
                data = set_bytes("0045C4C1", "74")  # clones
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
                data = set_bytes("0042C5EE", "909090909090909090909090")
                data = set_bytes("0042C612", "EB0D")
            else:
                data = set_bytes("0042C5EE", "3935D8C694000F840A010000")
                data = set_bytes("0042C612", "750D")

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

            data = "".join(data_list)
            index = self.comboBox_4.currentIndex()
            self.comboBox_4.setCurrentIndex(0)
            self.comboBox_4.setCurrentIndex(index)

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

    def getState_UnlimitedPlasm(self):
        self.checkBox1.blockSignals(True)

        valA = get_bytes("004A78D0", 6)
        valB = get_bytes("0042F7B9", 6)
        valC = get_bytes("0041E99D", 5)
        valD = get_bytes("0041E9A2", 5)
        valE = get_bytes("0041E9B1", 5)
        valF = get_bytes("0042F519", 2)
        if valA == "D8E090909090" and valB == "D8C890909090" and valC == "6800008E3E" and valD == "680000303E" and valE == "680000583E" and valF == "6A00":
            self.checkBox1.setChecked(True)
        elif valA == "D80588019500" and valB == "D82588019500" and valC == "680000543E" and valD == "680000303E" and valE == "680000103E" and valF == "6A03":
            self.checkBox1.setChecked(False)
        else:
            self.show_message("Unlimited Plasm: undefined state",
                              "Choose your preferred setting again \n(unless you made custom changes)")

        self.checkBox1.blockSignals(False)

    def getState_UnlimitedGoldplasm(self):
        self.checkBox2.blockSignals(True)

        valA = get_bytes("00472A02", 1)
        valB = get_bytes("0047331E", 1)
        valC = get_bytes("00473465", 1)
        if valA == "00" and valB == "00" and valC == "00":
            self.checkBox2.setChecked(True)
        elif valA == "32" and valB == "32" and valC == "32":  # 32 is hex for 50 - lowest power cost
            self.checkBox2.setChecked(False)
        else:
            self.show_message("Unlimited Gold Plasm: undefined state",
                              "Choose your preferred setting again \n(unless you made custom changes)")

        self.checkBox2.blockSignals(False)

    def getState_InstantPowerRecharge(self):
        self.checkBox3.blockSignals(True)

        value = get_bytes("00788B77", 6)
        if value == "B80000000090":
            self.checkBox3.setChecked(True)
        elif value == "8B801CD99000":
            self.checkBox3.setChecked(False)
        else:
            self.show_message("Instant Power Recharge: undefined state",
                              "Choose your preferred setting again \n(unless you made custom changes)")

        self.checkBox3.blockSignals(False)

    def getState_ResponsivePortraits(self):
        self.checkBox4.blockSignals(True)

        valA = get_bytes("004266B7", 2)
        valB = get_bytes("00428F42", 22)
        if valA == "EB41" and valB == "90909090909090908B87F00000009090909090909090":
            self.checkBox4.setChecked(True)
        elif valA == "7441" and valB == "85C90F84210100008B87F000000085C00F8513010000":
            self.checkBox4.setChecked(False)
        else:
            self.show_message("Responsive Empty Portraits: undefined state",
                              "Choose your preferred setting again \n(unless you made custom changes)")

        self.checkBox4.blockSignals(False)

    def getState_GhostCloning(self):
        self.checkBox5.blockSignals(True)

        valA = get_bytes("0045C4C1", 1)
        valB = get_bytes("0045C5F3", 1)
        valC = get_bytes("0045C7D2", 1)
        valD = get_bytes("0045C977", 1)
        valE = get_bytes("0045BE03", 1)
        if valA == "EB" and valB == "00" and valC == "00" and valD == "00" and valE == "00":
            self.checkBox5.setChecked(True)
        elif valA == "74" and valB == "01" and valC == "01" and valD == "01" and valE == "01":
            self.checkBox5.setChecked(False)
        else:
            self.show_message("Ghost Cloning: undefined state",
                              "Choose your preferred setting again \n(unless you made custom changes)")

        self.checkBox5.blockSignals(False)

    def getState_InsideOutsideOnAll(self):
        self.checkBox6.blockSignals(True)

        val = get_bytes("004CB01B", 2)
        if val == "9090":
            self.checkBox6.setChecked(True)
        elif val == "743F":
            self.checkBox6.setChecked(False)
        else:
            self.show_message("Inside/Outside On All Ghosts: undefined state",
                              "Choose your preferred setting again \n(unless you made custom changes)")

        self.checkBox6.blockSignals(False)

    def getState_IgnoreWards(self):
        self.checkBox7.blockSignals(True)

        valA = get_bytes("00606985", 6)
        valB = get_bytes("00606787", 2)
        valC = get_bytes("00606C24", 2)
        valD = get_bytes("0060867F", 2)
        if valA == "909090909090" and valB == "EB22" and valC == "EB1C" and valD == "EB1B":
            self.checkBox7.setChecked(True)
        elif valA == "0F8486000000" and valB == "7422" and valC == "741C" and valD == "741B":
            self.checkBox7.setChecked(False)
        else:
            self.show_message("Ignore Wards: undefined state",
                              "Choose your preferred setting again \n(unless you made custom changes)")

        self.checkBox7.blockSignals(False)

    def getState_DisableFireExtinguishers(self):
        self.checkBox8.blockSignals(True)

        val = get_bytes("0060139E", 5)
        if val == "6860029000":
            self.checkBox8.setChecked(True)
        elif val == "68B0FF8F00":
            self.checkBox8.setChecked(False)
        else:
            self.show_message("Disable Fire Extinguishers: undefined state",
                              "Choose your preferred setting again \n(unless you made custom changes)")

        self.checkBox8.blockSignals(False)

    def getState_FetterSharing(self):
        self.checkBox9.blockSignals(True)

        val = get_bytes("0047C332", 8)
        if val == "9090909090909090":
            self.checkBox9.setChecked(True)
        elif val == "39B7880000007407":
            self.checkBox9.setChecked(False)
        else:
            self.show_message("Fetter Sharing: undefined state",
                              "Choose your preferred setting again \n(unless you made custom changes)")

        self.checkBox9.blockSignals(False)

    def getState_MovableRestlessGhosts(self):
        self.checkBox10.blockSignals(True)

        valA = get_bytes("0042C5EE", 12)
        valB = get_bytes("0042C612", 2)
        if valA == "909090909090909090909090" and valB == "EB0D":
            self.checkBox10.setChecked(True)
        elif valA == "3935D8C694000F840A010000" and valB == "750D":
            self.checkBox10.setChecked(False)
        else:
            self.show_message("Movable Restless Ghosts: undefined state",
                              "Choose your preferred setting again \n(unless you made custom changes)")

        self.checkBox10.blockSignals(False)

    def getState_DisableMadnessImmunity(self):
        self.checkBox11.blockSignals(True)

        valA = get_bytes("00503B5E", 5)
        valB = get_bytes("00514CED", 5)
        valC = get_bytes("0052C88E", 5)
        valD = get_bytes("00509679", 5)
        valE = get_bytes("005481FC", 5)
        if valA == "9090909090" and valB == "9090909090" and valC == "9090909090" and valD == "9090909090" and valE == "9090909090":
            self.checkBox11.setChecked(True)
        elif valA == "A33C588D00" and valB == "A324838D00" and valC == "A39CAB8D00" and valD == "A3D4618D00" and valE == "A32C008E00":
            self.checkBox11.setChecked(False)
        else:
            self.show_message("Disable Madness Immunity: undefined state",
                              "Choose your preferred setting again \n(unless you made custom changes)")

        self.checkBox11.blockSignals(False)

    def getState_UncoverFears(self):
        self.checkBox12.blockSignals(True)

        valA = get_bytes("0047ED3D", 7)
        valB = get_bytes("0047ED60", 6)
        if valA == "B8010000009090" and valB == "B80100000090":
            self.checkBox12.setChecked(True)
        elif valA == "8B84B7FC000000" and valB == "8B81F8000000":
            self.checkBox12.setChecked(False)
        else:
            self.show_message("Uncover Fears: undefined state",
                              "Choose your preferred setting again \n(unless you made custom changes)")

        self.checkBox12.blockSignals(False)

    def getState_UnlockMissingFears(self):
        self.checkBox13.blockSignals(True)

        valA = get_bytes("00531DD7", 6)
        valB = get_bytes("008DC658", 1)
        if valA == "909090909090":
            self.checkBox13.setChecked(True)
        elif valA == "891524C78D00" and valB == "00":
            self.checkBox13.setChecked(False)
        else:
            self.show_message("Unlock Missing Fears: undefined state",
                              "Choose your preferred setting again \n(unless you made custom changes)")

        self.checkBox13.blockSignals(False)

    def getState_DisableCalmingEffects(self):
        self.checkBox14.blockSignals(True)

        val = get_bytes("00775CC9", 6)
        if val == "E92501000090":
            self.checkBox14.setChecked(True)
        elif val == "0F8524010000":
            self.checkBox14.setChecked(False)
        else:
            self.show_message("Disable Calming Effects: undefined state",
                              "Choose your preferred setting again \n(unless you made custom changes)")

        self.checkBox14.blockSignals(False)

    def getState_UnlockExtraFears(self):
        self.checkBox15.blockSignals(True)

        valA = get_bytes("00531DE7", 5)
        valB = get_bytes("008DC72C", 1)
        if valA == "9090909090":
            self.checkBox15.setChecked(True)
        elif valA == "A32CC78D00" and valB == "00":
            self.checkBox15.setChecked(False)
        else:
            self.show_message("Unlock Extra Fears: undefined state",
                              "Choose your preferred setting again \n(unless you made custom changes)")

        self.checkBox15.blockSignals(False)

    def getState_FixColdPhobia(self):
        self.checkBox16.blockSignals(True)

        valA = get_bytes("0057B4D3", 2)
        valB = get_bytes("0057C2C9", 2)
        if valA == "6A02" and valB == "6A02":
            self.checkBox16.setChecked(True)
        elif valA == "6A09" and valB == "6A09":
            self.checkBox16.setChecked(False)
        else:
            self.show_message("Fix Cold Phobia: undefined state",
                              "Choose your preferred setting again \n(unless you made custom changes)")

        self.checkBox16.blockSignals(False)

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

        valA = get_bytes("008F1F68", 1)
        valB = get_bytes("008F31F8", 1)
        valC = get_bytes("008F4AB8", 1)
        valD = get_bytes("008F69A8", 1)
        if valA == valB == valC == valD:
            level = int(valA, 16) + 1
            self.comboBox_7.setCurrentIndex(level)
        elif valA == "00" and valB == "03" and valC == "02" and valD == "01":
            self.comboBox_7.setCurrentIndex(0)
        else:
            self.show_message("Global Ghost Level: undefined state",
                              "Choose your preferred setting again \n(unless you made custom changes)")

        self.comboBox_7.blockSignals(False)

    def open_data(self):
        filepath = QtGui.QFileDialog.getOpenFileName(self, 'Open file', "", "*.exe")
        if not filepath:
            return

        global data
        data = open_file(filepath)
        self.show_message("File opened")

        self.actionSave.setEnabled(True)
        self.pushButton_9.setEnabled(True)
        self.comboBox_7.setEnabled(True)
        self.getState_GlobalGhostLevel()
        self.checkBoxSetup()
        self.find_scenarios()

    def save_data(self):
        filepath = QtGui.QFileDialog.getSaveFileName(self, 'Save file', "", "*.exe")
        if not filepath:
            return

        save_file(filepath, data)
        self.show_message("File saved")

    def about(self):
        self.show_message(Tooltips.VERSION, "created by Xavomel")

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

    def checkBoxSetup(self):
        self.getState_UnlimitedPlasm()
        self.getState_UnlimitedGoldplasm()
        self.getState_InstantPowerRecharge()
        self.getState_ResponsivePortraits()
        self.getState_GhostCloning()
        self.getState_InsideOutsideOnAll()
        self.getState_IgnoreWards()
        self.getState_DisableFireExtinguishers()
        self.getState_FetterSharing()
        self.getState_MovableRestlessGhosts()
        self.getState_DisableMadnessImmunity()
        self.getState_UncoverFears()
        self.getState_UnlockMissingFears()
        self.getState_DisableCalmingEffects()
        self.getState_UnlockExtraFears()
        self.getState_FixColdPhobia()
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


def main():
    app = QtGui.QApplication(sys.argv)
    form = MainWindow()
    form.show()
    app.exec_()


main()
