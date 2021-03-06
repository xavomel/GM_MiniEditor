from PyQt4 import QtCore, QtGui, Qt
from EditorMisc import Constants


try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    def _fromUtf8(s):
        return s


try:
    _encoding = QtGui.QApplication.UnicodeUTF8
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig, _encoding)
except AttributeError:
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig)


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName(_fromUtf8("MainWindow"))
        MainWindow.resize(800, 662)
        MainWindow.setToolTip(_fromUtf8(""))
        MainWindow.setStatusTip(_fromUtf8(""))
        MainWindow.setWhatsThis(_fromUtf8(""))
        MainWindow.setAccessibleName(_fromUtf8(""))
        MainWindow.setAccessibleDescription(_fromUtf8(""))
        self.centralwidget = QtGui.QWidget(MainWindow)
        self.centralwidget.setObjectName(_fromUtf8("centralwidget"))

        # central panel - label
        self.add_central_label()

        # central panel - sliders
        self.verticalLayoutWidget_2 = QtGui.QWidget(self.centralwidget)
        self.verticalLayoutWidget_2.setGeometry(QtCore.QRect(300, 10, 181, 331))
        self.verticalLayoutWidget_2.setObjectName(_fromUtf8("verticalLayoutWidget_2"))
        self.verticalLayout_2 = QtGui.QVBoxLayout(self.verticalLayoutWidget_2)
        self.verticalLayout_2.setObjectName(_fromUtf8("verticalLayout_2"))
        self.add_sliders()

        # central panel - fears
        self.gridLayoutWidget = QtGui.QWidget(self.centralwidget)
        self.gridLayoutWidget.setGeometry(QtCore.QRect(300, 341, 181, 103))
        self.gridLayoutWidget.setObjectName(_fromUtf8("gridLayoutWidget"))
        self.gridLayout = QtGui.QGridLayout(self.gridLayoutWidget)
        self.gridLayout.setObjectName(_fromUtf8("gridLayout"))
        self.add_fear_combo_boxes()

        # left panel
        self.verticalLayoutWidget_3 = QtGui.QWidget(self.centralwidget)
        self.verticalLayoutWidget_3.setGeometry(QtCore.QRect(10, 10, 175, 607)) # increase last param by 23 for each new checkbox
        self.verticalLayoutWidget_3.setObjectName(_fromUtf8("verticalLayoutWidget_3"))
        self.verticalLayout_3 = QtGui.QVBoxLayout(self.verticalLayoutWidget_3)
        self.verticalLayout_3.setObjectName(_fromUtf8("verticalLayout_3"))
        self.add_scenario_combo_box()
        self.add_set_bytes_button()
        self.add_global_ghost_level_combo_box()
        self.add_normal_check_boxes()
        self.add_recommended_label()
        self.add_recommended_check_boxes()

        # right panel
        self.verticalLayoutWidget = QtGui.QWidget(self.centralwidget)
        self.verticalLayoutWidget.setGeometry(QtCore.QRect(630, 10, 160, 38))
        self.verticalLayoutWidget.setObjectName(_fromUtf8("verticalLayoutWidget"))
        self.verticalLayout = QtGui.QVBoxLayout(self.verticalLayoutWidget)
        self.verticalLayout.setObjectName(_fromUtf8("verticalLayout"))
        self.add_mortal_combo_box()

        # scenario panel
        self.verticalLayoutWidget_4 = QtGui.QWidget(self.centralwidget)
        self.verticalLayoutWidget_4.setGeometry(QtCore.QRect(180, 10, 111, 186))
        self.verticalLayoutWidget_4.setObjectName(_fromUtf8("verticalLayoutWidget_4"))
        self.verticalLayout_4 = QtGui.QVBoxLayout(self.verticalLayoutWidget_4)
        self.verticalLayout_4.setObjectName(_fromUtf8("verticalLayout_4"))
        self.add_scenario_label()
        self.add_scenario_spin_boxes()
        self.add_plasm_line_edit()
        self.add_mood_combo_box()
        self.add_manual_terror_check_box()

        #
        MainWindow.setCentralWidget(self.centralwidget)
        self.add_menu_bar(MainWindow)
        self.add_status_bar(MainWindow)
        self.retranslateUi(MainWindow)
        self.add_object_connections(MainWindow)
        self.integrity_dialog = IntegrityCheckDialog(self)

    # combo boxes
    def add_scenario_combo_box(self):
        self.comboBox_3 = QtGui.QComboBox(self.verticalLayoutWidget_3)
        self.comboBox_3.setObjectName(_fromUtf8("comboBox_3"))
        self.comboBox_3.addItem("")
        self.comboBox_3.setEnabled(False)
        self.verticalLayout_3.addWidget(self.comboBox_3)

    def add_mortal_combo_box(self):
        self.comboBox_4 = QtGui.QComboBox(self.verticalLayoutWidget)
        self.comboBox_4.setObjectName(_fromUtf8("comboBox_4"))
        self.comboBox_4.addItem("")
        self.comboBox_4.setEnabled(False)
        self.verticalLayout.addWidget(self.comboBox_4)

    def add_fear_combo_boxes(self):
        self.label_4 = QtGui.QLabel(self.gridLayoutWidget)
        self.label_4.setObjectName(_fromUtf8("label_4"))
        self.label_5 = QtGui.QLabel(self.gridLayoutWidget)
        self.label_5.setObjectName(_fromUtf8("label_5"))
        self.comboBox = CustomComboBox(self)
        self.comboBox.setObjectName(_fromUtf8("comboBox"))
        self.comboBox.addItem(_fromUtf8(""))
        self.comboBox.addItem(_fromUtf8(""))
        self.comboBox.addItem(_fromUtf8(""))
        self.comboBox.addItem(_fromUtf8(""))
        self.comboBox.addItem(_fromUtf8(""))
        self.comboBox.addItem(_fromUtf8(""))
        self.comboBox.addItem(_fromUtf8(""))
        self.comboBox.addItem(_fromUtf8(""))
        self.comboBox.addItem(_fromUtf8(""))
        self.comboBox.addItem(_fromUtf8(""))
        self.comboBox.addItem(_fromUtf8(""))
        self.comboBox.addItem(_fromUtf8(""))
        self.comboBox.addItem(_fromUtf8(""))
        self.comboBox.addItem(_fromUtf8(""))
        self.comboBox.addItem(_fromUtf8(""))
        self.comboBox.addItem(_fromUtf8(""))
        self.comboBox.setEnabled(False)
        self.comboBox_2 = CustomComboBox(self)
        self.comboBox_2.setObjectName(_fromUtf8("comboBox_2"))
        self.comboBox_2.addItem(_fromUtf8(""))
        self.comboBox_2.addItem(_fromUtf8(""))
        self.comboBox_2.addItem(_fromUtf8(""))
        self.comboBox_2.addItem(_fromUtf8(""))
        self.comboBox_2.addItem(_fromUtf8(""))
        self.comboBox_2.addItem(_fromUtf8(""))
        self.comboBox_2.addItem(_fromUtf8(""))
        self.comboBox_2.addItem(_fromUtf8(""))
        self.comboBox_2.addItem(_fromUtf8(""))
        self.comboBox_2.addItem(_fromUtf8(""))
        self.comboBox_2.addItem(_fromUtf8(""))
        self.comboBox_2.addItem(_fromUtf8(""))
        self.comboBox_2.addItem(_fromUtf8(""))
        self.comboBox_2.addItem(_fromUtf8(""))
        self.comboBox_2.addItem(_fromUtf8(""))
        self.comboBox_2.addItem(_fromUtf8(""))
        self.comboBox_2.setItemText(15, _fromUtf8(""))
        self.comboBox_2.setEnabled(False)
        self.comboBox_6 = CustomComboBox(self)
        self.comboBox_6.setObjectName(_fromUtf8("comboBox_6"))
        self.comboBox_6.addItem(_fromUtf8(""))
        self.comboBox_6.addItem(_fromUtf8(""))
        self.comboBox_6.addItem(_fromUtf8(""))
        self.comboBox_6.addItem(_fromUtf8(""))
        self.comboBox_6.addItem(_fromUtf8(""))
        self.comboBox_6.addItem(_fromUtf8(""))
        self.comboBox_6.addItem(_fromUtf8(""))
        self.comboBox_6.addItem(_fromUtf8(""))
        self.comboBox_6.addItem(_fromUtf8(""))
        self.comboBox_6.addItem(_fromUtf8(""))
        self.comboBox_6.addItem(_fromUtf8(""))
        self.comboBox_6.addItem(_fromUtf8(""))
        self.comboBox_6.addItem(_fromUtf8(""))
        self.comboBox_6.addItem(_fromUtf8(""))
        self.comboBox_6.addItem(_fromUtf8(""))
        self.comboBox_6.addItem(_fromUtf8(""))
        self.comboBox_6.setItemText(15, _fromUtf8(""))
        self.comboBox_6.setEnabled(False)

        self.gridLayout.addWidget(self.label_4,    0, 0, 1, 1)
        self.gridLayout.addWidget(self.comboBox,   1, 0, 1, 1)
        self.gridLayout.addWidget(self.comboBox_6, 1, 1, 1, 1)
        self.gridLayout.addWidget(self.label_5,    2, 0, 1, 1)
        self.gridLayout.addWidget(self.comboBox_2, 3, 0, 1, 1)

    def add_global_ghost_level_combo_box(self):
        self.comboBox_7 = QtGui.QComboBox(self.verticalLayoutWidget_3)
        self.comboBox_7.setObjectName(_fromUtf8("comboBox_7"))
        self.comboBox_7.addItem("")
        self.comboBox_7.addItem("")
        self.comboBox_7.addItem("")
        self.comboBox_7.addItem("")
        self.comboBox_7.addItem("")
        self.comboBox_7.addItem("")
        self.comboBox_7.addItem("")
        self.comboBox_7.addItem("")
        self.comboBox_7.addItem("")
        self.comboBox_7.addItem("")
        self.comboBox_7.setToolTip(Constants.GLOBAL_GHOST_LEVEL)
        self.comboBox_7.setEnabled(False)
        self.verticalLayout_3.addWidget(self.comboBox_7)

    def add_mood_combo_box(self):
        self.comboBox_5 = QtGui.QComboBox(self.verticalLayoutWidget_4)
        self.comboBox_5.setObjectName(_fromUtf8("comboBox_5"))
        self.comboBox_5.addItem(_fromUtf8(""))
        self.comboBox_5.addItem(_fromUtf8(""))
        self.comboBox_5.addItem(_fromUtf8(""))
        self.comboBox_5.addItem(_fromUtf8(""))
        self.comboBox_5.addItem(_fromUtf8(""))
        self.comboBox_5.addItem(_fromUtf8(""))
        self.comboBox_5.addItem(_fromUtf8(""))
        self.comboBox_5.addItem(_fromUtf8(""))
        self.comboBox_5.addItem(_fromUtf8(""))
        self.comboBox_5.setEnabled(False)
        self.comboBox_5.setHidden(True)
        self.verticalLayout_4.addWidget(self.comboBox_5)

    # check boxes
    def add_normal_check_boxes(self):
        self.checkBox1 = QtGui.QCheckBox(self.verticalLayoutWidget_3)
        self.checkBox1.setObjectName(_fromUtf8("checkBox_1"))
        self.checkBox1.setToolTip(Constants.UNLIMITED_PLASM)
        self.checkBox1.setEnabled(False)
        self.verticalLayout_3.addWidget(self.checkBox1)
        self.checkBox2 = QtGui.QCheckBox(self.verticalLayoutWidget_3)
        self.checkBox2.setObjectName(_fromUtf8("checkBox_2"))
        self.checkBox2.setToolTip(Constants.UNLIMITED_GOLDPLASM)
        self.checkBox2.setEnabled(False)
        self.verticalLayout_3.addWidget(self.checkBox2)
        self.checkBox3 = QtGui.QCheckBox(self.verticalLayoutWidget_3)
        self.checkBox3.setObjectName(_fromUtf8("checkBox_3"))
        self.checkBox3.setToolTip(Constants.INSTANT_POWER_RECHARGE)
        self.checkBox3.setEnabled(False)
        self.verticalLayout_3.addWidget(self.checkBox3)
        self.checkBox18 = QtGui.QCheckBox(self.verticalLayoutWidget_3)
        self.checkBox18.setObjectName(_fromUtf8("checkBox_18"))
        self.checkBox18.setToolTip(Constants.CONTINUOUS_POWER_RECASTING)
        self.checkBox18.setEnabled(False)
        self.verticalLayout_3.addWidget(self.checkBox18)
        self.checkBox4 = QtGui.QCheckBox(self.verticalLayoutWidget_3)
        self.checkBox4.setObjectName(_fromUtf8("checkBox_4"))
        self.checkBox4.setToolTip(Constants.RESPONSIVE_EMPTY_PORTRAITS)
        self.checkBox4.setEnabled(False)
        self.verticalLayout_3.addWidget(self.checkBox4)
        self.checkBox5 = QtGui.QCheckBox(self.verticalLayoutWidget_3)
        self.checkBox5.setObjectName(_fromUtf8("checkBox_5"))
        self.checkBox5.setToolTip(Constants.GHOST_CLONING)
        self.checkBox5.setEnabled(False)
        self.verticalLayout_3.addWidget(self.checkBox5)
        self.checkBox9 = QtGui.QCheckBox(self.verticalLayoutWidget_3)
        self.checkBox9.setObjectName(_fromUtf8("checkBox_9"))
        self.checkBox9.setToolTip(Constants.FETTER_SHARING)
        self.checkBox9.setEnabled(False)
        self.verticalLayout_3.addWidget(self.checkBox9)
        self.checkBox6 = QtGui.QCheckBox(self.verticalLayoutWidget_3)
        self.checkBox6.setObjectName(_fromUtf8("checkBox_6"))
        self.checkBox6.setToolTip(Constants.INSIDE_OUTSIDE_ON_ALL_GHOSTS)
        self.checkBox6.setEnabled(False)
        self.verticalLayout_3.addWidget(self.checkBox6)
        self.checkBox10 = QtGui.QCheckBox(self.verticalLayoutWidget_3)
        self.checkBox10.setObjectName(_fromUtf8("checkBox_10"))
        self.checkBox10.setToolTip(Constants.MOVABLE_RESTLESS_GHOSTS)
        self.checkBox10.setEnabled(False)
        self.verticalLayout_3.addWidget(self.checkBox10)
        self.checkBox21 = QtGui.QCheckBox(self.verticalLayoutWidget_3)
        self.checkBox21.setObjectName(_fromUtf8("checkBox_21"))
        self.checkBox21.setToolTip(Constants.BENCH_RESTLESS_GHOSTS)
        self.checkBox21.setEnabled(False)
        self.verticalLayout_3.addWidget(self.checkBox21)
        self.checkBox7 = QtGui.QCheckBox(self.verticalLayoutWidget_3)
        self.checkBox7.setObjectName(_fromUtf8("checkBox_7"))
        self.checkBox7.setToolTip(Constants.IGNORE_WARDS)
        self.checkBox7.setEnabled(False)
        self.verticalLayout_3.addWidget(self.checkBox7)
        self.checkBox12 = QtGui.QCheckBox(self.verticalLayoutWidget_3)
        self.checkBox12.setObjectName(_fromUtf8("checkBox_12"))
        self.checkBox12.setToolTip(Constants.UNCOVER_FEARS)
        self.checkBox12.setEnabled(False)
        self.verticalLayout_3.addWidget(self.checkBox12)
        self.checkBox14 = QtGui.QCheckBox(self.verticalLayoutWidget_3)
        self.checkBox14.setObjectName(_fromUtf8("checkBox_14"))
        self.checkBox14.setToolTip(Constants.DISABLE_CALMING_EFFECTS)
        self.checkBox14.setEnabled(False)
        self.verticalLayout_3.addWidget(self.checkBox14)
        self.checkBox15 = QtGui.QCheckBox(self.verticalLayoutWidget_3)
        self.checkBox15.setObjectName(_fromUtf8("checkBox_15"))
        self.checkBox15.setToolTip(Constants.UNLOCK_EXTRA_FEARS)
        self.checkBox15.setEnabled(False)
        self.verticalLayout_3.addWidget(self.checkBox15)
        self.checkBox16 = QtGui.QCheckBox(self.verticalLayoutWidget_3)
        self.checkBox16.setObjectName(_fromUtf8("checkBox_16"))
        self.checkBox16.setToolTip(Constants.FIX_COLD_PHOBIA)
        self.checkBox16.setEnabled(False)
        self.verticalLayout_3.addWidget(self.checkBox16)
        self.checkBox20 = QtGui.QCheckBox(self.verticalLayoutWidget_3)
        self.checkBox20.setObjectName(_fromUtf8("checkBox_20"))
        self.checkBox20.setToolTip(Constants.EXPLORATION_MODE)
        self.checkBox20.setEnabled(False)
        self.verticalLayout_3.addWidget(self.checkBox20)

    def add_recommended_check_boxes(self):
        self.checkBox8 = QtGui.QCheckBox(self.verticalLayoutWidget_3)
        self.checkBox8.setObjectName(_fromUtf8("checkBox_8"))
        self.checkBox8.setToolTip(Constants.DISABLE_FIRE_EXTINGUISHERS)
        self.checkBox8.setEnabled(False)
        self.verticalLayout_3.addWidget(self.checkBox8)
        self.checkBox11 = QtGui.QCheckBox(self.verticalLayoutWidget_3)
        self.checkBox11.setObjectName(_fromUtf8("checkBox_11"))
        self.checkBox11.setToolTip(Constants.DISABLE_MADNESS_IMMUNITY)
        self.checkBox11.setEnabled(False)
        self.verticalLayout_3.addWidget(self.checkBox11)
        self.checkBox13 = QtGui.QCheckBox(self.verticalLayoutWidget_3)
        self.checkBox13.setObjectName(_fromUtf8("checkBox_13"))
        self.checkBox13.setToolTip(Constants.UNLOCK_MISSING_FEARS)
        self.checkBox13.setEnabled(False)
        self.verticalLayout_3.addWidget(self.checkBox13)
        self.checkBox19 = QtGui.QCheckBox(self.verticalLayoutWidget_3)
        self.checkBox19.setObjectName(_fromUtf8("checkBox_19"))
        self.checkBox19.setToolTip(Constants.GHOST_RETRAINING)
        self.checkBox19.setEnabled(False)
        self.verticalLayout_3.addWidget(self.checkBox19)

    def add_manual_terror_check_box(self):
        self.checkBox17 = QtGui.QCheckBox(self.verticalLayoutWidget_4)
        self.checkBox17.setObjectName(_fromUtf8("checkBox_17"))
        self.checkBox17.setToolTip(Constants.MANUAL_TERROR)
        self.checkBox17.setEnabled(False)
        self.checkBox17.setHidden(True)
        self.verticalLayout_4.addWidget(self.checkBox17)

    # labels
    def add_central_label(self):
        self.label = QtGui.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(300, 0, 181, 41))
        self.label.setTextFormat(QtCore.Qt.AutoText)
        self.label.setAlignment(QtCore.Qt.AlignCenter)
        self.label.setObjectName(_fromUtf8("label"))

    def add_recommended_label(self):
        self.line_1 = QtGui.QFrame(self.verticalLayoutWidget_3)
        self.line_1.setFrameShape(QtGui.QFrame.HLine)
        self.line_1.setFrameShadow(QtGui.QFrame.Sunken)
        self.line_1.setObjectName(_fromUtf8("line_1"))
        self.verticalLayout_3.addWidget(self.line_1)

        self.label_3 = QtGui.QLabel(self.verticalLayoutWidget_3)
        self.label_3.setAlignment(QtCore.Qt.AlignCenter)
        self.label_3.setObjectName(_fromUtf8("label_3"))
        self.verticalLayout_3.addWidget(self.label_3)

        self.line_2 = QtGui.QFrame(self.verticalLayoutWidget_3)
        self.line_2.setFrameShape(QtGui.QFrame.HLine)
        self.line_2.setFrameShadow(QtGui.QFrame.Sunken)
        self.line_2.setObjectName(_fromUtf8("line_2"))
        self.verticalLayout_3.addWidget(self.line_2)

    def add_scenario_label(self):
        self.label_2 = QtGui.QLabel(self.verticalLayoutWidget_4)
        self.label_2.setTextFormat(QtCore.Qt.AutoText)
        self.label_2.setAlignment(QtCore.Qt.AlignCenter)
        self.label_2.setWordWrap(True)
        self.label_2.setObjectName(_fromUtf8("label_2"))
        self.label_2.setHidden(True)
        self.verticalLayout_4.addWidget(self.label_2)

    # misc
    def add_set_bytes_button(self):
        self.pushButton_9 = QtGui.QPushButton(self.verticalLayoutWidget_3)
        self.pushButton_9.setObjectName(_fromUtf8("pushButton_9"))
        self.pushButton_9.setEnabled(False)
        self.verticalLayout_3.addWidget(self.pushButton_9)

    def add_sliders(self):
        spacerItem = QtGui.QSpacerItem(0, 22, QtGui.QSizePolicy.Fixed, QtGui.QSizePolicy.Fixed)
        self.verticalLayout_2.addItem(spacerItem)

        self.horizontalSlider = QtGui.QSlider(self.verticalLayoutWidget_2)
        self.horizontalSlider.setOrientation(QtCore.Qt.Horizontal)
        self.horizontalSlider.setObjectName(_fromUtf8("horizontalSlider"))
        self.horizontalSlider.setEnabled(False)
        self.verticalLayout_2.addWidget(self.horizontalSlider)
        self.horizontalSlider_4 = CustomSlider(self)
        self.horizontalSlider_4.setOrientation(QtCore.Qt.Horizontal)
        self.horizontalSlider_4.setObjectName(_fromUtf8("horizontalSlider_4"))
        self.horizontalSlider_4.setEnabled(False)
        self.verticalLayout_2.addWidget(self.horizontalSlider_4)
        self.horizontalSlider_2 = CustomSlider(self)
        self.horizontalSlider_2.setOrientation(QtCore.Qt.Horizontal)
        self.horizontalSlider_2.setObjectName(_fromUtf8("horizontalSlider_2"))
        self.horizontalSlider_2.setEnabled(False)
        self.verticalLayout_2.addWidget(self.horizontalSlider_2)
        self.horizontalSlider_3 = QtGui.QSlider(self.verticalLayoutWidget_2)
        self.horizontalSlider_3.setOrientation(QtCore.Qt.Horizontal)
        self.horizontalSlider_3.setObjectName(_fromUtf8("horizontalSlider_3"))
        self.horizontalSlider_3.setEnabled(False)
        self.verticalLayout_2.addWidget(self.horizontalSlider_3)

        self.horizontalSlider.setMinimum(0)
        self.horizontalSlider_2.setMinimum(0)
        self.horizontalSlider_3.setMinimum(0)
        self.horizontalSlider_4.setMinimum(0)
        self.horizontalSlider.setMaximum(100)
        self.horizontalSlider_2.setMaximum(100)
        self.horizontalSlider_3.setMaximum(100)
        self.horizontalSlider_4.setMaximum(100)
        self.horizontalSlider.tickInterval = 1
        self.horizontalSlider_2.tickInterval = 1
        self.horizontalSlider_3.tickInterval = 1
        self.horizontalSlider_4.tickInterval = 1
        self.horizontalSlider.setSingleStep(0)
        self.horizontalSlider_2.setSingleStep(0)
        self.horizontalSlider_3.setSingleStep(0)
        self.horizontalSlider_4.setSingleStep(0)
        self.horizontalSlider.setPageStep(0)
        self.horizontalSlider_2.setPageStep(0)
        self.horizontalSlider_3.setPageStep(0)
        self.horizontalSlider_4.setPageStep(0)

        white = "rgb(255, 255, 255)"
        red = "rgb(238, 156, 0)"
        orange = "rgb(0, 178, 235)"
        blue = "rgb(223, 0, 41)"
        self.horizontalSlider.setStyleSheet(self.custom_slider_style_sheet(white))
        self.horizontalSlider_2.setStyleSheet(self.custom_slider_style_sheet(red))
        self.horizontalSlider_3.setStyleSheet(self.custom_slider_style_sheet(orange))
        self.horizontalSlider_4.setStyleSheet(self.custom_slider_style_sheet(blue))

    def custom_slider_style_sheet(self, color):
        return '''
        QSlider::groove:horizontal {
            background-color: ''' + color + ''';
            border: 1px solid;
            height: 6px;
        }
        QSlider::groove:horizontal:disabled {
            background-color: transparent;
        }
        QSlider::handle:horizontal {
            background-color: black;
            margin: -16px 0;
            width: 10px;
        }
        QSlider::handle:horizontal:disabled {
            background-color: transparent;
        }'''

    def add_scenario_spin_boxes(self):
        self.spinBox = QtGui.QSpinBox(self.verticalLayoutWidget_4)
        self.spinBox.setProperty("value", 0)
        self.spinBox.setMinimum(0)
        self.spinBox.setMaximum(8)
        self.spinBox.setObjectName(_fromUtf8("spinBox"))
        self.spinBox.setEnabled(False)
        self.spinBox.setHidden(True)
        self.verticalLayout_4.addWidget(self.spinBox)
        self.spinBox_2 = QtGui.QDoubleSpinBox(self.verticalLayoutWidget_4)
        self.spinBox_2.setProperty("value", 0)
        self.spinBox_2.setMinimum(0)
        self.spinBox_2.setMaximum(100)
        self.spinBox_2.setDecimals(23)
        self.spinBox_2.setObjectName(_fromUtf8("spinBox_2"))
        self.spinBox_2.setEnabled(False)
        self.spinBox_2.setHidden(True)
        self.verticalLayout_4.addWidget(self.spinBox_2)

    def add_plasm_line_edit(self):
        self.lineEdit = QtGui.QLineEdit(self.verticalLayoutWidget_4)
        self.lineEdit.setObjectName(_fromUtf8("lineEdit"))
        self.lineEdit.setEnabled(False)
        self.lineEdit.setHidden(True)
        self.verticalLayout_4.addWidget(self.lineEdit)

    def add_menu_bar(self, MainWindow):
        self.menubar = QtGui.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 800, 21))
        self.menubar.setObjectName(_fromUtf8("menubar"))
        MainWindow.setMenuBar(self.menubar)

        self.actionOpen = QtGui.QAction(MainWindow)
        self.actionOpen.setObjectName(_fromUtf8("actionOpen"))
        #self.actionOpen.setShortcut(QtGui.QKeySequence("Ctrl+Z"))
        self.actionSave = QtGui.QAction(MainWindow)
        self.actionSave.setObjectName(_fromUtf8("actionSave"))
        #self.actionSave.setShortcut(QtGui.QKeySequence("Ctrl+C"))
        self.actionSave.setEnabled(False)
        self.actionAbout = QtGui.QAction(MainWindow)
        self.actionAbout.setObjectName(_fromUtf8("actionAbout"))
        self.actionScripts = QtGui.QAction(MainWindow)
        self.actionScripts.setObjectName(_fromUtf8("actionScripts"))
        self.actionScripts.setEnabled(False)
        self.actionReactions = QtGui.QAction(MainWindow)
        self.actionReactions.setObjectName(_fromUtf8("actionReactions"))
        self.actionReactions.setEnabled(False)
        self.menubar.addAction(self.actionOpen)
        self.menubar.addAction(self.actionSave)
        self.menubar.addAction(self.actionScripts)
        self.menubar.addAction(self.actionReactions)
        self.menubar.addAction(self.actionAbout)

    def add_status_bar(self, MainWindow):
        self.statusbar = QtGui.QStatusBar(MainWindow)
        self.statusbar.setObjectName(_fromUtf8("statusbar"))
        MainWindow.setStatusBar(self.statusbar)

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(_translate("MainWindow", Constants.VERSION, None))
        self.label.setText(_translate("MainWindow", "Open the file", None))
        self.label_2.setText(_translate("MainWindow", "Scenario name", None))
        self.label_3.setText(_translate("MainWindow", "Recommended:", None))
        self.label_4.setText(_translate("MainWindow", "Conscious", None))
        self.label_5.setText(_translate("MainWindow", "Unconscious", None))
        self.horizontalSlider.setStatusTip(_translate("MainWindow", "Willpower", None))
        self.horizontalSlider_2.setStatusTip(_translate("MainWindow", "Insanity", None))
        self.horizontalSlider_3.setStatusTip(_translate("MainWindow", "Belief", None))
        self.horizontalSlider_4.setStatusTip(_translate("MainWindow", "Terror", None))
        self.checkBox1.setText(_translate("MainWindow", "Unlimited Plasm", None))
        self.checkBox2.setText(_translate("MainWindow", "Unlimited Gold Plasm", None))
        self.checkBox3.setText(_translate("MainWindow", "Instant Power Recharge", None))
        self.checkBox4.setText(_translate("MainWindow", "Responsive Empty Portraits", None))
        self.checkBox5.setText(_translate("MainWindow", "Ghost Cloning", None))
        self.checkBox6.setText(_translate("MainWindow", "Inside/Outside On All Ghosts", None))
        self.checkBox7.setText(_translate("MainWindow", "Ignore Wards", None))
        self.checkBox8.setText(_translate("MainWindow", "Disable Fire Extinguishers", None))
        self.checkBox9.setText(_translate("MainWindow", "Fetter Sharing", None))
        self.checkBox10.setText(_translate("MainWindow", "Movable Restless Ghosts", None))
        self.checkBox11.setText(_translate("MainWindow", "Disable Madness Immunity", None))
        self.checkBox12.setText(_translate("MainWindow", "Uncover Fears", None))
        self.checkBox13.setText(_translate("MainWindow", "Unlock Missing Fears", None))
        self.checkBox14.setText(_translate("MainWindow", "Disable Calming Effects", None))
        self.checkBox15.setText(_translate("MainWindow", "Unlock Extra Fears", None))
        self.checkBox16.setText(_translate("MainWindow", "Fix Cold Phobia", None))
        self.checkBox17.setText(_translate("MainWindow", "Manual Terror", None))
        self.checkBox18.setText(_translate("MainWindow", "Continuous Power Recasting", None))
        self.checkBox19.setText(_translate("MainWindow", "Ghost Retraining", None))
        self.checkBox20.setText(_translate("MainWindow", "Exploration Mode (Alpha)", None))
        self.checkBox21.setText(_translate("MainWindow", "Bench Restless Ghosts", None))
        self.comboBox.setStatusTip(_translate("MainWindow", "Conscious fear", None))
        self.comboBox.setItemText(0, _translate("MainWindow", "none", None))
        self.comboBox.setItemText(1, _translate("MainWindow", "blood", None))
        self.comboBox.setItemText(2, _translate("MainWindow", "cold*", None))
        self.comboBox.setItemText(3, _translate("MainWindow", "creepy", None))
        self.comboBox.setItemText(4, _translate("MainWindow", "darkness", None))
        self.comboBox.setItemText(5, _translate("MainWindow", "electrical", None))
        self.comboBox.setItemText(6, _translate("MainWindow", "fire", None))
        self.comboBox.setItemText(7, _translate("MainWindow", "hunted", None))
        self.comboBox.setItemText(8, _translate("MainWindow", "noise", None))
        self.comboBox.setItemText(9, _translate("MainWindow", "normal", None))
        self.comboBox.setItemText(10, _translate("MainWindow", "storm", None))
        self.comboBox.setItemText(11, _translate("MainWindow", "trapped", None))
        self.comboBox.setItemText(12, _translate("MainWindow", "unclean", None))
        self.comboBox.setItemText(13, _translate("MainWindow", "water", None))
        self.comboBox.setItemText(14, _translate("MainWindow", "pursuit*", None))
        self.comboBox.setItemText(15, _translate("MainWindow", "", None))
        self.comboBox_2.setStatusTip(_translate("MainWindow", "Unconscious fear", None))
        self.comboBox_2.setItemText(0, _translate("MainWindow", "none", None))
        self.comboBox_2.setItemText(1, _translate("MainWindow", "blood", None))
        self.comboBox_2.setItemText(2, _translate("MainWindow", "cold*", None))
        self.comboBox_2.setItemText(3, _translate("MainWindow", "creepy", None))
        self.comboBox_2.setItemText(4, _translate("MainWindow", "darkness", None))
        self.comboBox_2.setItemText(5, _translate("MainWindow", "electrical", None))
        self.comboBox_2.setItemText(6, _translate("MainWindow", "fire", None))
        self.comboBox_2.setItemText(7, _translate("MainWindow", "hunted", None))
        self.comboBox_2.setItemText(8, _translate("MainWindow", "noise", None))
        self.comboBox_2.setItemText(9, _translate("MainWindow", "normal", None))
        self.comboBox_2.setItemText(10, _translate("MainWindow", "storm", None))
        self.comboBox_2.setItemText(11, _translate("MainWindow", "trapped", None))
        self.comboBox_2.setItemText(12, _translate("MainWindow", "unclean", None))
        self.comboBox_2.setItemText(13, _translate("MainWindow", "water", None))
        self.comboBox_2.setItemText(14, _translate("MainWindow", "pursuit*", None))
        self.comboBox_2.setItemText(15, _translate("MainWindow", "", None))
        self.comboBox_6.setStatusTip(_translate("MainWindow", "Extra conscious fear", None))
        self.comboBox_6.setItemText(0, _translate("MainWindow", "none", None))
        self.comboBox_6.setItemText(1, _translate("MainWindow", "blood", None))
        self.comboBox_6.setItemText(2, _translate("MainWindow", "cold*", None))
        self.comboBox_6.setItemText(3, _translate("MainWindow", "creepy", None))
        self.comboBox_6.setItemText(4, _translate("MainWindow", "darkness", None))
        self.comboBox_6.setItemText(5, _translate("MainWindow", "electrical", None))
        self.comboBox_6.setItemText(6, _translate("MainWindow", "fire", None))
        self.comboBox_6.setItemText(7, _translate("MainWindow", "hunted", None))
        self.comboBox_6.setItemText(8, _translate("MainWindow", "noise", None))
        self.comboBox_6.setItemText(9, _translate("MainWindow", "normal", None))
        self.comboBox_6.setItemText(10, _translate("MainWindow", "storm", None))
        self.comboBox_6.setItemText(11, _translate("MainWindow", "trapped", None))
        self.comboBox_6.setItemText(12, _translate("MainWindow", "unclean", None))
        self.comboBox_6.setItemText(13, _translate("MainWindow", "water", None))
        self.comboBox_6.setItemText(14, _translate("MainWindow", "pursuit*", None))
        self.comboBox_6.setItemText(15, _translate("MainWindow", "", None))
        self.comboBox_3.setStatusTip(_translate("MainWindow", "Scenarios", None))
        self.comboBox_3.setItemText(0, _translate("MainWindow", "pick scenario", None))
        self.comboBox_4.setStatusTip(_translate("MainWindow", "Mortals", None))
        self.comboBox_4.setItemText(0, _translate("MainWindow", "pick mortal", None))
        self.comboBox_5.setStatusTip(_translate("MainWindow", "Mood (scenario-wide)", None))
        self.comboBox_5.setItemText(0, _translate("MainWindow", "none", None))
        self.comboBox_5.setItemText(1, _translate("MainWindow", "neutral", None))
        self.comboBox_5.setItemText(2, _translate("MainWindow", "friendly", None))
        self.comboBox_5.setItemText(3, _translate("MainWindow", "angry", None))
        self.comboBox_5.setItemText(4, _translate("MainWindow", "calm", None))
        self.comboBox_5.setItemText(5, _translate("MainWindow", "rattled", None))
        self.comboBox_5.setItemText(6, _translate("MainWindow", "terrified", None))
        self.comboBox_5.setItemText(7, _translate("MainWindow", "insane", None))
        self.comboBox_5.setItemText(8, _translate("MainWindow", " ", None))
        self.comboBox_7.setItemText(0, _translate("MainWindow", "global ghost level: off", None))
        self.comboBox_7.setItemText(1, _translate("MainWindow", "global ghost level: 0", None))
        self.comboBox_7.setItemText(2, _translate("MainWindow", "global ghost level: 1", None))
        self.comboBox_7.setItemText(3, _translate("MainWindow", "global ghost level: 2", None))
        self.comboBox_7.setItemText(4, _translate("MainWindow", "global ghost level: 3", None))
        self.comboBox_7.setItemText(5, _translate("MainWindow", "global ghost level: 4", None))
        self.comboBox_7.setItemText(6, _translate("MainWindow", "global ghost level: 5", None))
        self.comboBox_7.setItemText(7, _translate("MainWindow", "global ghost level: 6", None))
        self.comboBox_7.setItemText(8, _translate("MainWindow", "global ghost level: 7", None))
        self.comboBox_7.setItemText(9, _translate("MainWindow", "global ghost level: 8", None))
        self.actionOpen.setText(_translate("MainWindow", "Open", None))
        self.actionSave.setText(_translate("MainWindow", "Save", None))
        self.actionAbout.setText(_translate("MainWindow", "About", None))
        self.actionScripts.setText(_translate("MainWindow", "Scripts", None))
        self.actionReactions.setText(_translate("MainWindow", "Reactions", None))
        self.spinBox.setStatusTip(_translate("MainWindow", "Haunter Slots", None))
        self.spinBox_2.setStatusTip(_translate("MainWindow", "Mean Terror", None))
        self.lineEdit.setStatusTip(_translate("MainWindow", "Starting Plasm (estimate)", None))
        self.pushButton_9.setText(_translate("MainWindow", "Set bytes @ address\nUSE AT OWN RISK", None))

    def add_object_connections(self, MainWindow):
        QtCore.QObject.connect(self.horizontalSlider, QtCore.SIGNAL(_fromUtf8("valueChanged(int)")), MainWindow.sliderMoved)
        QtCore.QObject.connect(self.horizontalSlider_2, QtCore.SIGNAL(_fromUtf8("valueChanged(int)")), MainWindow.sliderMoved)
        QtCore.QObject.connect(self.horizontalSlider_3, QtCore.SIGNAL(_fromUtf8("valueChanged(int)")), MainWindow.sliderMoved)
        QtCore.QObject.connect(self.horizontalSlider_4, QtCore.SIGNAL(_fromUtf8("valueChanged(int)")), MainWindow.sliderMoved)
        QtCore.QObject.connect(self.horizontalSlider, QtCore.SIGNAL(_fromUtf8("sliderReleased()")), MainWindow.setWillpower)
        QtCore.QObject.connect(self.horizontalSlider_2, QtCore.SIGNAL(_fromUtf8("sliderReleased()")), MainWindow.setInsanity)
        QtCore.QObject.connect(self.horizontalSlider_3, QtCore.SIGNAL(_fromUtf8("sliderReleased()")), MainWindow.setBelief)
        QtCore.QObject.connect(self.horizontalSlider_4, QtCore.SIGNAL(_fromUtf8("sliderReleased()")), MainWindow.setTerror)
        QtCore.QObject.connect(self.checkBox1, QtCore.SIGNAL(_fromUtf8("stateChanged(int)")), MainWindow.setUnlimitedPlasm)
        QtCore.QObject.connect(self.checkBox2, QtCore.SIGNAL(_fromUtf8("stateChanged(int)")), MainWindow.setUnlimitedGoldplasm)
        QtCore.QObject.connect(self.checkBox3, QtCore.SIGNAL(_fromUtf8("stateChanged(int)")), MainWindow.setInstantPowerRecharge)
        QtCore.QObject.connect(self.checkBox4, QtCore.SIGNAL(_fromUtf8("stateChanged(int)")), MainWindow.setResponsivePortraits)
        QtCore.QObject.connect(self.checkBox5, QtCore.SIGNAL(_fromUtf8("stateChanged(int)")), MainWindow.setGhostCloning)
        QtCore.QObject.connect(self.checkBox6, QtCore.SIGNAL(_fromUtf8("stateChanged(int)")), MainWindow.setInsideOutsideOnAll)
        QtCore.QObject.connect(self.checkBox7, QtCore.SIGNAL(_fromUtf8("stateChanged(int)")), MainWindow.setIgnoreWards)
        QtCore.QObject.connect(self.checkBox8, QtCore.SIGNAL(_fromUtf8("stateChanged(int)")), MainWindow.setDisableFireExtinguishers)
        QtCore.QObject.connect(self.checkBox9, QtCore.SIGNAL(_fromUtf8("stateChanged(int)")), MainWindow.setFetterSharing)
        QtCore.QObject.connect(self.checkBox10, QtCore.SIGNAL(_fromUtf8("stateChanged(int)")), MainWindow.setMovableRestlessGhosts)
        QtCore.QObject.connect(self.checkBox11, QtCore.SIGNAL(_fromUtf8("stateChanged(int)")), MainWindow.setDisableMadnessImmunity)
        QtCore.QObject.connect(self.checkBox12, QtCore.SIGNAL(_fromUtf8("stateChanged(int)")), MainWindow.setUncoverFears)
        QtCore.QObject.connect(self.checkBox13, QtCore.SIGNAL(_fromUtf8("stateChanged(int)")), MainWindow.setUnlockMissingFears)
        QtCore.QObject.connect(self.checkBox14, QtCore.SIGNAL(_fromUtf8("stateChanged(int)")), MainWindow.setDisableCalmingEffects)
        QtCore.QObject.connect(self.checkBox15, QtCore.SIGNAL(_fromUtf8("stateChanged(int)")), MainWindow.setUnlockExtraFears)
        QtCore.QObject.connect(self.checkBox16, QtCore.SIGNAL(_fromUtf8("stateChanged(int)")), MainWindow.setFixColdPhobia)
        QtCore.QObject.connect(self.checkBox17, QtCore.SIGNAL(_fromUtf8("stateChanged(int)")), MainWindow.setManualTerror)
        QtCore.QObject.connect(self.checkBox18, QtCore.SIGNAL(_fromUtf8("stateChanged(int)")), MainWindow.setContinuousPowerRecasting)
        QtCore.QObject.connect(self.checkBox19, QtCore.SIGNAL(_fromUtf8("stateChanged(int)")), MainWindow.setGhostRetraining)
        QtCore.QObject.connect(self.checkBox20, QtCore.SIGNAL(_fromUtf8("stateChanged(int)")), MainWindow.setExplorationMode)
        QtCore.QObject.connect(self.checkBox21, QtCore.SIGNAL(_fromUtf8("stateChanged(int)")), MainWindow.setBenchRestlessGhosts)
        QtCore.QObject.connect(self.comboBox, QtCore.SIGNAL(_fromUtf8("currentIndexChanged(int)")), MainWindow.setConciousFear)
        QtCore.QObject.connect(self.comboBox_2, QtCore.SIGNAL(_fromUtf8("currentIndexChanged(int)")), MainWindow.setUnconciousFear)
        QtCore.QObject.connect(self.comboBox_6, QtCore.SIGNAL(_fromUtf8("currentIndexChanged(int)")), MainWindow.setExtraFear)
        QtCore.QObject.connect(self.comboBox_3, QtCore.SIGNAL(_fromUtf8("currentIndexChanged(int)")), MainWindow.scenarioChanged)
        QtCore.QObject.connect(self.comboBox_4, QtCore.SIGNAL(_fromUtf8("currentIndexChanged(int)")), MainWindow.mortalChanged)
        QtCore.QObject.connect(self.comboBox_5, QtCore.SIGNAL(_fromUtf8("currentIndexChanged(int)")), MainWindow.setMood)
        QtCore.QObject.connect(self.comboBox_7, QtCore.SIGNAL(_fromUtf8("currentIndexChanged(int)")), MainWindow.setGhostLevel)
        QtCore.QObject.connect(self.actionOpen, QtCore.SIGNAL(_fromUtf8("triggered()")), MainWindow.open_data)
        QtCore.QObject.connect(self.actionSave, QtCore.SIGNAL(_fromUtf8("triggered()")), MainWindow.save_data)
        QtCore.QObject.connect(self.actionAbout, QtCore.SIGNAL(_fromUtf8("triggered()")), MainWindow.about)
        QtCore.QObject.connect(self.actionScripts, QtCore.SIGNAL(_fromUtf8("triggered()")), MainWindow.show_scripts_window)
        QtCore.QObject.connect(self.actionReactions, QtCore.SIGNAL(_fromUtf8("triggered()")), MainWindow.show_reactions_window)
        QtCore.QObject.connect(self.spinBox, QtCore.SIGNAL(_fromUtf8("valueChanged(int)")), MainWindow.setHaunterSlots)
        QtCore.QObject.connect(self.spinBox_2, QtCore.SIGNAL(_fromUtf8("valueChanged(double)")), MainWindow.setMeanTerror)
        QtCore.QObject.connect(self.pushButton_9, QtCore.SIGNAL(_fromUtf8("clicked()")), MainWindow.setBytesAtAddress)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)


class IntegrityCheckDialog(QtGui.QDialog):
    def __init__(self, parent=None):
        super(IntegrityCheckDialog, self).__init__(parent)
        self.setupUi(self)

    def setupUi(self, Dialog):
        Dialog.setWindowTitle("Integrity Check")
        self.horizontalLayout = QtGui.QHBoxLayout(Dialog)

        self.splitter = QtGui.QSplitter(Dialog)
        self.splitter.setOrientation(QtCore.Qt.Vertical)

        self.label = QtGui.QLabel(self.splitter)
        self.label.setAlignment(QtCore.Qt.AlignCenter)
        self.label.setWordWrap(True)
        self.plainTextEdit = QtGui.QPlainTextEdit(self.splitter)
        self.plainTextEdit.setFixedSize(360, 150)
        self.plainTextEdit.setReadOnly(True)
        self.plainTextEdit.setLineWrapMode(QtGui.QPlainTextEdit.NoWrap)
        self.label_2 = QtGui.QLabel(self.splitter)
        self.label_2.setAlignment(QtCore.Qt.AlignCenter)
        self.label_2.setWordWrap(True)

        self.horizontalLayout.addWidget(self.splitter)


class ScriptsWindow(QtGui.QDialog):
    def __init__(self, parent, scripts):
        super(ScriptsWindow, self).__init__(parent)
        self.scripts = scripts
        self.setupUi(self)
        self.setupCheckBoxes()

    def setupUi(self, Dialog):
        Dialog.setWindowTitle("Scripts")
        self.verticalLayout = QtGui.QVBoxLayout(Dialog)

        self.pushButton_1 = QtGui.QPushButton()
        self.pushButton_2 = QtGui.QPushButton()
        self.pushButton_3 = QtGui.QPushButton()
        self.pushButton_4 = QtGui.QPushButton()
        self.pushButton_1.setObjectName(_fromUtf8("pushButton_1"))
        self.pushButton_2.setObjectName(_fromUtf8("pushButton_2"))
        self.pushButton_3.setObjectName(_fromUtf8("pushButton_3"))
        self.pushButton_4.setObjectName(_fromUtf8("pushButton_4"))
        self.pushButton_1.setText(_translate("MainWindow", "Sort by state", None))
        self.pushButton_2.setText(_translate("MainWindow", "Sort by id", None))
        self.pushButton_3.setText(_translate("MainWindow", "Sort by name", None))
        self.pushButton_4.setText(_translate("MainWindow", "Sort by comment", None))
        self.pushButton_1.clicked.connect(self.sort_by_state)
        self.pushButton_2.clicked.connect(self.sort_by_id)
        self.pushButton_3.clicked.connect(self.sort_by_name)
        self.pushButton_4.clicked.connect(self.sort_by_comment)

        self.button_area_content = QtGui.QWidget()
        self.grid_layout_1 = QtGui.QGridLayout(self.button_area_content)
        self.grid_layout_1.addWidget(self.pushButton_1, 0, 0)
        self.grid_layout_1.addWidget(self.pushButton_2, 0, 1)
        self.grid_layout_1.addWidget(self.pushButton_3, 0, 2)
        self.grid_layout_1.addWidget(self.pushButton_4, 0, 3)

        self.lineEdit = QtGui.QLineEdit()
        self.pushButton_5 = QtGui.QPushButton()
        self.pushButton_6 = QtGui.QPushButton()
        self.pushButton_5.setObjectName(_fromUtf8("pushButton_5"))
        self.pushButton_6.setObjectName(_fromUtf8("pushButton_6"))
        self.pushButton_5.setText(_translate("MainWindow", "Search", None))
        self.pushButton_6.setText(_translate("MainWindow", "Clear", None))
        self.pushButton_5.clicked.connect(self.search)
        self.pushButton_6.clicked.connect(self.clear)

        self.search_area_content = QtGui.QWidget()
        self.grid_layout_2 = QtGui.QGridLayout(self.search_area_content)
        self.grid_layout_2.addWidget(self.lineEdit, 0, 0)
        self.grid_layout_2.addWidget(self.pushButton_5, 0, 1)
        self.grid_layout_2.addWidget(self.pushButton_6, 0, 2)

        self.scroll_area_content = QtGui.QWidget()
        self.scroll_area = QtGui.QScrollArea(self)
        self.scroll_area.setWidget(self.scroll_area_content)
        self.scroll_area.setWidgetResizable(True)
        self.scroll_area.setFixedSize(600, 600)
        self.grid_layout_3 = QtGui.QGridLayout(self.scroll_area_content)

        self.verticalLayout.addWidget(self.search_area_content)
        self.verticalLayout.addWidget(self.button_area_content)
        self.verticalLayout.addWidget(self.scroll_area)

    def setupCheckBoxes(self):
        for elem in self.scripts:
            checkbox_id = elem[2]
            name = elem[3]
            comment = elem[4]
            text = "%s - %s%s" % (checkbox_id.zfill(3), name, comment)
            checkbox = QtGui.QCheckBox()
            checkbox.setObjectName(_fromUtf8("checkBox_scr_%s" % checkbox_id))
            checkbox.setText(_translate("MainWindow", text, None))
            checkbox.clicked.connect(self.parent().setScript)
            self.grid_layout_3.addWidget(checkbox)

    def sort_by_state(self):
        states = dict()

        regex = QtCore.QRegExp("checkBox_scr_\\d+")
        checkboxes = self.findChildren(QtGui.QCheckBox, regex)
        for checkbox in checkboxes:
            self.grid_layout_3.removeWidget(checkbox)

            obj_name = checkbox.objectName().split("_")
            checkbox_id = str(obj_name[2])
            states[checkbox_id] = checkbox.isChecked()

        idx = 2
        key = lambda x: states[x[idx]]
        reverse = not states[self.scripts[0][idx]]
        self.scripts.sort(key=key, reverse=reverse)
        for elem in self.scripts:
            checkbox_id = elem[2]
            checkbox = self.findChild(QtGui.QCheckBox, "checkBox_scr_%s" % checkbox_id)
            self.grid_layout_3.addWidget(checkbox)

    def generic_sort(self, idx, key):
        regex = QtCore.QRegExp("checkBox_scr_\\d+")
        checkboxes = self.findChildren(QtGui.QCheckBox, regex)
        for checkbox in checkboxes:
            self.grid_layout_3.removeWidget(checkbox)

        reverse = self.scripts[0][idx] < self.scripts[-1][idx]
        self.scripts.sort(key=key, reverse=reverse)
        for elem in self.scripts:
            checkbox_id = elem[2]
            checkbox = self.findChild(QtGui.QCheckBox, "checkBox_scr_%s" % checkbox_id)
            self.grid_layout_3.addWidget(checkbox)

    def sort_by_id(self):
        idx = 2
        key = lambda x: int(x[idx])
        self.generic_sort(idx, key)

    def sort_by_name(self):
        idx = 3
        key = lambda x: x[idx].lower()
        self.generic_sort(idx, key)

    def sort_by_comment(self):
        idx = 4
        key = lambda x: x[idx].lower()
        self.generic_sort(idx, key)

    def search(self):
        search_query = self.lineEdit.text()

        regex = QtCore.QRegExp("checkBox_scr_\\d+")
        checkboxes = self.findChildren(QtGui.QCheckBox, regex)
        for checkbox in checkboxes:
            checkbox.setVisible(True)
            if not checkbox.text().contains(search_query, QtCore.Qt.CaseInsensitive):
                checkbox.setVisible(False)

    def clear(self):
        self.lineEdit.clear()

        regex = QtCore.QRegExp("checkBox_scr_\\d+")
        checkboxes = self.findChildren(QtGui.QCheckBox, regex)
        for checkbox in checkboxes:
            checkbox.setVisible(True)


class ReactionsWindow(QtGui.QDialog):
    def __init__(self, parent, reactions):
        super(ReactionsWindow, self).__init__(parent)
        self.reactions = reactions
        self.setupUi(self)
        self.setupComboBoxes()

    def setupUi(self, Dialog):
        Dialog.setWindowTitle("Reactions")
        self.verticalLayout = QtGui.QVBoxLayout(Dialog)

        self.pushButton_1 = QtGui.QPushButton()
        self.pushButton_1.setObjectName(_fromUtf8("pushButton_1"))
        self.pushButton_1.setText(_translate("MainWindow", "Restore defaults", None))
        self.pushButton_1.clicked.connect(self.parent().setReactionsToDefault)

        self.button_area_content = QtGui.QWidget()
        self.grid_layout_1 = QtGui.QGridLayout(self.button_area_content)
        self.grid_layout_1.addWidget(self.pushButton_1, 0, 0)

        self.scroll_area_content = QtGui.QWidget()
        self.scroll_area = QtGui.QScrollArea(self)
        self.scroll_area.setWidget(self.scroll_area_content)
        self.scroll_area.setWidgetResizable(True)
        self.scroll_area.setFixedSize(600, 600)
        self.grid_layout_2 = QtGui.QGridLayout(self.scroll_area_content)

        self.verticalLayout.addWidget(self.button_area_content)
        self.verticalLayout.addWidget(self.scroll_area)

    def setupComboBoxes(self):
        label = QtGui.QLabel()
        label.setText("CHANGE ALL")
        label_empty = QtGui.QLabel()

        combobox = QtGui.QComboBox()
        combobox.setObjectName(_fromUtf8("comboBox_rea_all"))
        combobox.addItems([x["reaction_name"] for x in self.reactions])
        combobox.currentIndexChanged.connect(self.parent().setReactionAll)
        combobox.setStyleSheet("QComboBox { color: rgba(0, 0, 0, 0) }")

        self.grid_layout_2.addWidget(label, 0, 0)
        self.grid_layout_2.addWidget(combobox, 0, 1)
        self.grid_layout_2.addWidget(label_empty, 1, 0)

        for idx, elem in enumerate(self.reactions):
            name = elem["reaction_name"]
            comment = elem["comment"].replace("\"", "")
            label = QtGui.QLabel()
            label.setText(name)
            label.setToolTip(comment)

            combobox = QtGui.QComboBox()
            combobox.setObjectName(_fromUtf8("comboBox_rea_%d" % idx))
            model = combobox.model()
            for x in self.reactions:
                item = QtGui.QStandardItem(x["reaction_name"])
                if name != x["reaction_name"]:
                    item.setForeground(QtGui.QColor("blue"))
                model.appendRow(item)
            combobox.currentIndexChanged.connect(self.parent().setReaction)

            self.grid_layout_2.addWidget(label, idx + 2, 0)
            self.grid_layout_2.addWidget(combobox, idx + 2, 1)

class CustomSlider(QtGui.QSlider):
    def __init__(self, parent):
        self.parent = parent
        super(CustomSlider, self).__init__(parent)

    def enterEvent(self, event):
        if not self.isEnabled():
            name = self.objectName()
            if not self.parent.checkBox11.isChecked() and name == "horizontalSlider_2":
                self.parent.checkBox11.setStyleSheet("background: yellow")
            elif not self.parent.checkBox17.isChecked() and name == "horizontalSlider_4":
                self.parent.checkBox17.setStyleSheet("background: yellow")
        return super(CustomSlider, self).enterEvent(event)

    def leaveEvent(self, event):
        name = self.objectName()
        if name == "horizontalSlider_2":
            self.parent.checkBox11.setStyleSheet("background: none")
        elif name == "horizontalSlider_4":
            self.parent.checkBox17.setStyleSheet("background: none")
        return super(CustomSlider, self).enterEvent(event)


class CustomComboBox(QtGui.QComboBox):
    def __init__(self, parent):
        self.parent = parent
        super(CustomComboBox, self).__init__(parent)

    def enterEvent(self, event):
        if not self.isEnabled():
            name = self.objectName()
            if not self.parent.checkBox13.isChecked() and (name == "comboBox" or name == "comboBox_2"):
                self.parent.checkBox13.setStyleSheet("background: yellow")
            elif not self.parent.checkBox15.isChecked() and name == "comboBox_6":
                self.parent.checkBox15.setStyleSheet("background: yellow")
        return super(CustomComboBox, self).enterEvent(event)

    def leaveEvent(self, event):
        name = self.objectName()
        if name == "comboBox" or name == "comboBox_2":
            self.parent.checkBox13.setStyleSheet("background: none")
        elif name == "comboBox_6":
            self.parent.checkBox15.setStyleSheet("background: none")
        return super(CustomComboBox, self).enterEvent(event)
