from PyQt4 import QtCore, QtGui, Qt
from EditorMisc import Tooltips


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
        MainWindow.resize(800, 600)
        MainWindow.setToolTip(_fromUtf8(""))
        MainWindow.setStatusTip(_fromUtf8(""))
        MainWindow.setWhatsThis(_fromUtf8(""))
        MainWindow.setAccessibleName(_fromUtf8(""))
        MainWindow.setAccessibleDescription(_fromUtf8(""))
        self.centralwidget = QtGui.QWidget(MainWindow)
        self.centralwidget.setObjectName(_fromUtf8("centralwidget"))
        self.verticalLayoutWidget = QtGui.QWidget(self.centralwidget)
        self.verticalLayoutWidget.setGeometry(QtCore.QRect(630, 10, 160, 80))
        self.verticalLayoutWidget.setObjectName(_fromUtf8("verticalLayoutWidget"))
        self.verticalLayout = QtGui.QVBoxLayout(self.verticalLayoutWidget)
        self.verticalLayout.setObjectName(_fromUtf8("verticalLayout"))
        self.verticalLayoutWidget_2 = QtGui.QWidget(self.centralwidget)
        self.verticalLayoutWidget_2.setGeometry(QtCore.QRect(300, 10, 181, 331))
        self.verticalLayoutWidget_2.setObjectName(_fromUtf8("verticalLayoutWidget_2"))
        self.verticalLayout_2 = QtGui.QVBoxLayout(self.verticalLayoutWidget_2)
        self.verticalLayout_2.setObjectName(_fromUtf8("verticalLayout_2"))
        self.horizontalSlider = QtGui.QSlider(self.verticalLayoutWidget_2)
        self.horizontalSlider.setToolTip(_fromUtf8(""))
        self.horizontalSlider.setWhatsThis(_fromUtf8(""))
        self.horizontalSlider.setAccessibleName(_fromUtf8(""))
        self.horizontalSlider.setAccessibleDescription(_fromUtf8(""))
        self.horizontalSlider.setOrientation(QtCore.Qt.Horizontal)
        self.horizontalSlider.setObjectName(_fromUtf8("horizontalSlider"))
        self.verticalLayout_2.addWidget(self.horizontalSlider)
        self.horizontalSlider_2 = QtGui.QSlider(self.verticalLayoutWidget_2)
        self.horizontalSlider_2.setOrientation(QtCore.Qt.Horizontal)
        self.horizontalSlider_2.setObjectName(_fromUtf8("horizontalSlider_2"))
        self.verticalLayout_2.addWidget(self.horizontalSlider_2)
        self.horizontalSlider_3 = QtGui.QSlider(self.verticalLayoutWidget_2)
        self.horizontalSlider_3.setOrientation(QtCore.Qt.Horizontal)
        self.horizontalSlider_3.setObjectName(_fromUtf8("horizontalSlider_3"))

        self.horizontalSlider.setMinimum(0)
        self.horizontalSlider_2.setMinimum(0)
        self.horizontalSlider_3.setMinimum(0)
        self.horizontalSlider.setMaximum(100)
        self.horizontalSlider_2.setMaximum(100)
        self.horizontalSlider_3.setMaximum(100)
        self.horizontalSlider.tickInterval = 1
        self.horizontalSlider_2.tickInterval = 1
        self.horizontalSlider_3.tickInterval = 1
        self.horizontalSlider.setSingleStep(0)
        self.horizontalSlider_2.setSingleStep(0)
        self.horizontalSlider_3.setSingleStep(0)
        self.horizontalSlider.setPageStep(0)
        self.horizontalSlider_2.setPageStep(0)
        self.horizontalSlider_3.setPageStep(0)
        self.verticalLayout_2.addWidget(self.horizontalSlider_3)

        self.verticalLayoutWidget_3 = QtGui.QWidget(self.centralwidget)
        self.verticalLayoutWidget_3.setGeometry(QtCore.QRect(10, 10, 175, 331)) # increase last param by 23 for each new checkbox
        self.verticalLayoutWidget_3.setObjectName(_fromUtf8("verticalLayoutWidget_3"))
        self.verticalLayout_3 = QtGui.QVBoxLayout(self.verticalLayoutWidget_3)
        self.verticalLayout_3.setObjectName(_fromUtf8("verticalLayout_3"))

        self.comboBox_3 = QtGui.QComboBox(self.verticalLayoutWidget_3)
        self.comboBox_3.setObjectName(_fromUtf8("comboBox_3"))
        self.comboBox_3.addItem("")
        self.verticalLayout_3.addWidget(self.comboBox_3)

        self.pushButton_9 = QtGui.QPushButton(self.verticalLayoutWidget_3)
        self.pushButton_9.setObjectName(_fromUtf8("pushButton_9"))
        self.verticalLayout_3.addWidget(self.pushButton_9)

        self.checkBox1 = QtGui.QCheckBox(self.verticalLayoutWidget_3)
        self.checkBox1.setObjectName(_fromUtf8("checkBox_1"))
        self.checkBox1.setToolTip(Tooltips.UNLIMITED_PLASM)
        self.checkBox1.setEnabled(False)
        self.verticalLayout_3.addWidget(self.checkBox1)
        self.checkBox2 = QtGui.QCheckBox(self.verticalLayoutWidget_3)
        self.checkBox2.setObjectName(_fromUtf8("checkBox_2"))
        self.checkBox2.setToolTip(Tooltips.UNLIMITED_GOLDPLASM)
        self.checkBox2.setEnabled(False)
        self.verticalLayout_3.addWidget(self.checkBox2)
        self.checkBox3 = QtGui.QCheckBox(self.verticalLayoutWidget_3)
        self.checkBox3.setObjectName(_fromUtf8("checkBox_3"))
        self.checkBox3.setToolTip(Tooltips.INSTANT_POWER_RECHARGE)
        self.checkBox3.setEnabled(False)
        self.verticalLayout_3.addWidget(self.checkBox3)
        self.checkBox4 = QtGui.QCheckBox(self.verticalLayoutWidget_3)
        self.checkBox4.setObjectName(_fromUtf8("checkBox_4"))
        self.checkBox4.setToolTip(Tooltips.RESPONSIVE_EMPTY_PORTRAITS)
        self.checkBox4.setEnabled(False)
        self.verticalLayout_3.addWidget(self.checkBox4)
        self.checkBox5 = QtGui.QCheckBox(self.verticalLayoutWidget_3)
        self.checkBox5.setObjectName(_fromUtf8("checkBox_5"))
        self.checkBox5.setToolTip(Tooltips.GHOST_CLONING)
        self.checkBox5.setEnabled(False)
        self.verticalLayout_3.addWidget(self.checkBox5)
        self.checkBox9 = QtGui.QCheckBox(self.verticalLayoutWidget_3)
        self.checkBox9.setObjectName(_fromUtf8("checkBox_9"))
        self.checkBox9.setToolTip(Tooltips.FETTER_SHARING)
        self.checkBox9.setEnabled(False)
        self.verticalLayout_3.addWidget(self.checkBox9)
        self.checkBox6 = QtGui.QCheckBox(self.verticalLayoutWidget_3)
        self.checkBox6.setObjectName(_fromUtf8("checkBox_6"))
        self.checkBox6.setToolTip(Tooltips.INSIDE_OUTSIDE_ON_ALL_GHOSTS)
        self.checkBox6.setEnabled(False)
        self.verticalLayout_3.addWidget(self.checkBox6)
        self.checkBox10 = QtGui.QCheckBox(self.verticalLayoutWidget_3)
        self.checkBox10.setObjectName(_fromUtf8("checkBox_10"))
        self.checkBox10.setToolTip(Tooltips.MOVABLE_RESTLESS_GHOSTS)
        self.checkBox10.setEnabled(False)
        self.verticalLayout_3.addWidget(self.checkBox10)
        self.checkBox7 = QtGui.QCheckBox(self.verticalLayoutWidget_3)
        self.checkBox7.setObjectName(_fromUtf8("checkBox_7"))
        self.checkBox7.setToolTip(Tooltips.IGNORE_WARDS)
        self.checkBox7.setEnabled(False)
        self.verticalLayout_3.addWidget(self.checkBox7)
        self.checkBox8 = QtGui.QCheckBox(self.verticalLayoutWidget_3)
        self.checkBox8.setObjectName(_fromUtf8("checkBox_8"))
        self.checkBox8.setToolTip(Tooltips.DISABLE_FIRE_EXTINGUISHERS)
        self.checkBox8.setEnabled(False)
        self.verticalLayout_3.addWidget(self.checkBox8)
        self.checkBox11 = QtGui.QCheckBox(self.verticalLayoutWidget_3)
        self.checkBox11.setObjectName(_fromUtf8("checkBox_11"))
        self.checkBox11.setToolTip(Tooltips.DISABLE_MADNESS_IMMUNITY)
        self.checkBox11.setEnabled(False)
        self.verticalLayout_3.addWidget(self.checkBox11)

        self.comboBox_4 = QtGui.QComboBox(self.verticalLayoutWidget)
        self.comboBox_4.setObjectName(_fromUtf8("comboBox_4"))
        self.comboBox_4.addItem("")
        self.verticalLayout.addWidget(self.comboBox_4)

        self.label = QtGui.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(300, 0, 181, 41))
        self.label.setTextFormat(QtCore.Qt.AutoText)
        self.label.setAlignment(QtCore.Qt.AlignCenter)
        self.label.setObjectName(_fromUtf8("label"))
        self.horizontalLayoutWidget = QtGui.QWidget(self.centralwidget)
        self.horizontalLayoutWidget.setGeometry(QtCore.QRect(300, 340, 181, 81))
        self.horizontalLayoutWidget.setObjectName(_fromUtf8("horizontalLayoutWidget"))
        self.horizontalLayout_2 = QtGui.QHBoxLayout(self.horizontalLayoutWidget)
        self.horizontalLayout_2.setObjectName(_fromUtf8("horizontalLayout_2"))
        self.comboBox = QtGui.QComboBox(self.horizontalLayoutWidget)
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
        self.horizontalLayout_2.addWidget(self.comboBox)
        self.comboBox_2 = QtGui.QComboBox(self.horizontalLayoutWidget)
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
        self.horizontalLayout_2.addWidget(self.comboBox_2)
        self.verticalLayoutWidget_4 = QtGui.QWidget(self.centralwidget)
        self.verticalLayoutWidget_4.setGeometry(QtCore.QRect(180, 10, 111, 111))
        self.verticalLayoutWidget_4.setObjectName(_fromUtf8("verticalLayoutWidget_4"))
        self.verticalLayout_4 = QtGui.QVBoxLayout(self.verticalLayoutWidget_4)
        self.verticalLayout_4.setObjectName(_fromUtf8("verticalLayout_4"))
        self.label_2 = QtGui.QLabel(self.verticalLayoutWidget_4)
        self.label_2.setTextFormat(QtCore.Qt.AutoText)
        self.label_2.setAlignment(QtCore.Qt.AlignCenter)
        self.label_2.setWordWrap(True)
        self.label_2.setObjectName(_fromUtf8("label_2"))
        self.label_2.setHidden(True)
        self.verticalLayout_4.addWidget(self.label_2)
        self.spinBox = QtGui.QSpinBox(self.verticalLayoutWidget_4)
        self.spinBox.setProperty("value", 0)
        self.spinBox.setMinimum(0)
        self.spinBox.setMaximum(8)
        self.spinBox.setObjectName(_fromUtf8("spinBox"))
        self.spinBox.setEnabled(False)
        self.spinBox.setHidden(True)
        self.verticalLayout_4.addWidget(self.spinBox)

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

        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtGui.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 800, 21))
        self.menubar.setObjectName(_fromUtf8("menubar"))
        self.menuMenu = QtGui.QMenu(self.menubar)
        self.menuMenu.setObjectName(_fromUtf8("menuMenu"))
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtGui.QStatusBar(MainWindow)
        self.statusbar.setObjectName(_fromUtf8("statusbar"))
        MainWindow.setStatusBar(self.statusbar)
        self.actionOpen = QtGui.QAction(MainWindow)
        self.actionOpen.setObjectName(_fromUtf8("actionOpen"))
        self.actionOpen.setShortcut(QtGui.QKeySequence("Ctrl+Z"))
        self.actionSave = QtGui.QAction(MainWindow)
        self.actionSave.setObjectName(_fromUtf8("actionSave"))
        self.actionSave.setShortcut(QtGui.QKeySequence("Ctrl+C"))
        self.actionSave.setEnabled(False)
        self.actionAbout = QtGui.QAction(MainWindow)
        self.actionAbout.setObjectName(_fromUtf8("actionAbout"))
        self.menuMenu.addAction(self.actionOpen)
        self.menuMenu.addAction(self.actionSave)
        self.menuMenu.addAction(self.actionAbout)
        self.menubar.addAction(self.menuMenu.menuAction())

        button = self.centralwidget.findChild(QtGui.QPushButton, "pushButton_9")
        button.setEnabled(False)

        sliders = self.centralwidget.findChildren(QtGui.QSlider)
        for s in sliders:
            s.setEnabled(False)

        combos = self.centralwidget.findChildren(QtGui.QComboBox)
        for c in combos:
            c.setEnabled(False)

        self.retranslateUi(MainWindow)
        QtCore.QObject.connect(self.horizontalSlider, QtCore.SIGNAL(_fromUtf8("valueChanged(int)")), MainWindow.sliderMoved)
        QtCore.QObject.connect(self.horizontalSlider_2, QtCore.SIGNAL(_fromUtf8("valueChanged(int)")), MainWindow.sliderMoved)
        QtCore.QObject.connect(self.horizontalSlider_3, QtCore.SIGNAL(_fromUtf8("valueChanged(int)")), MainWindow.sliderMoved)
        QtCore.QObject.connect(self.horizontalSlider, QtCore.SIGNAL(_fromUtf8("sliderReleased()")), MainWindow.setWillpower)
        QtCore.QObject.connect(self.horizontalSlider_2, QtCore.SIGNAL(_fromUtf8("sliderReleased()")), MainWindow.setInsanity)
        QtCore.QObject.connect(self.horizontalSlider_3, QtCore.SIGNAL(_fromUtf8("sliderReleased()")), MainWindow.setBelief)
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
        QtCore.QObject.connect(self.comboBox, QtCore.SIGNAL(_fromUtf8("currentIndexChanged(int)")), MainWindow.setConciousFear)
        QtCore.QObject.connect(self.comboBox_2, QtCore.SIGNAL(_fromUtf8("currentIndexChanged(int)")), MainWindow.setUnconciousFear)
        QtCore.QObject.connect(self.comboBox_3, QtCore.SIGNAL(_fromUtf8("currentIndexChanged(int)")), MainWindow.scenarioChanged)
        QtCore.QObject.connect(self.comboBox_4, QtCore.SIGNAL(_fromUtf8("currentIndexChanged(int)")), MainWindow.mortalChanged)
        QtCore.QObject.connect(self.comboBox_5, QtCore.SIGNAL(_fromUtf8("currentIndexChanged(int)")), MainWindow.setMood)
        QtCore.QObject.connect(self.actionOpen, QtCore.SIGNAL(_fromUtf8("triggered()")), MainWindow.open_data)
        QtCore.QObject.connect(self.actionSave, QtCore.SIGNAL(_fromUtf8("triggered()")), MainWindow.save_data)
        QtCore.QObject.connect(self.actionAbout, QtCore.SIGNAL(_fromUtf8("triggered()")), MainWindow.about)
        QtCore.QObject.connect(self.spinBox, QtCore.SIGNAL(_fromUtf8("valueChanged(int)")), MainWindow.setHaunterSlots)
        QtCore.QObject.connect(self.pushButton_9, QtCore.SIGNAL(_fromUtf8("clicked()")), MainWindow.setBytesAtAddress)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(_translate("MainWindow", "Ghost Master MiniEditor v0.2.8", None))
        self.label.setText(_translate("MainWindow", "Open the file", None))
        self.label_2.setText(_translate("MainWindow", "Scenario name", None))
        self.horizontalSlider.setStatusTip(_translate("MainWindow", "Willpower", None))
        self.horizontalSlider_2.setStatusTip(_translate("MainWindow", "Insanity", None))
        self.horizontalSlider_3.setStatusTip(_translate("MainWindow", "Belief", None))
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
        self.comboBox.setStatusTip(_translate("MainWindow", "Concious fear", None))
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
        self.comboBox_2.setStatusTip(_translate("MainWindow", "Unconcious fear", None))
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
        self.menuMenu.setTitle(_translate("MainWindow", "Menu", None))
        self.actionOpen.setText(_translate("MainWindow", "Open", None))
        self.actionSave.setText(_translate("MainWindow", "Save", None))
        self.actionAbout.setText(_translate("MainWindow", "About", None))
        self.spinBox.setStatusTip(_translate("MainWindow", "Haunter Slots", None))
        self.pushButton_9.setText(_translate("MainWindow", "Set bytes @ address\nUSE AT OWN RISK", None))
