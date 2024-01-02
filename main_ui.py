# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'main_ui.ui'
#
# Created by: PyQt5 UI code generator 5.15.7
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1185, 818)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(MainWindow.sizePolicy().hasHeightForWidth())
        MainWindow.setSizePolicy(sizePolicy)
        MainWindow.setAutoFillBackground(False)
        MainWindow.setStyleSheet("QMainWindow{\n"
"    background-color: rgb(30, 50, 80); /*背景色*/\n"
"}\n"
"")
        MainWindow.setIconSize(QtCore.QSize(32, 32))
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setStyleSheet("QCentralwidget{\n"
"    background-color: rgb(70, 70, 70); /*背景色*/\n"
"}")
        self.centralwidget.setObjectName("centralwidget")
        self.pushButton_1 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_1.setGeometry(QtCore.QRect(810, 10, 61, 22))
        font = QtGui.QFont()
        font.setFamily("16px")
        font.setPointSize(10)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.pushButton_1.setFont(font)
        self.pushButton_1.setAutoFillBackground(False)
        self.pushButton_1.setStyleSheet("QPushButton\n"
"{\n"
"    background-color:rgb(193, 131, 255); /*背景色*/ \n"
"    border-style: outset;    /* 边界内凹 */\n"
"    border-width: 1px;     /* 边边界宽度 */\n"
"    border-radius: 5px; /* 边界圆滑 */\n"
"    font: dengxian 16px;     /* 字体大小 */\n"
"    min-width: 2em;\n"
"    color: white; /* 字体颜色 */\n"
"    \n"
"}\n"
"/* 鼠标经过改变按钮颜色 */\n"
"QPushButton:hover\n"
"{\n"
"    background-color: rgb(187, 78, 255);\n"
"}\n"
"")
        self.pushButton_1.setText("")
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("icon/刷新.svg"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.pushButton_1.setIcon(icon)
        self.pushButton_1.setObjectName("pushButton_1")
        self.pushButton_2 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_2.setGeometry(QtCore.QRect(740, 10, 61, 22))
        self.pushButton_2.setAutoFillBackground(False)
        self.pushButton_2.setStyleSheet("QPushButton\n"
"{\n"
"    background-color: rgb(75, 173, 238); /*背景色*/ \n"
"    border-style: outset;    /* 边界内凹 */\n"
"    border-width: 1px;     /* 边边界宽度 */\n"
"    border-radius: 5px; /* 边界圆滑 */\n"
"    font: dengxian 16px;     /* 字体大小 */\n"
"    min-width: 2em;\n"
"    color: white; /* 字体颜色 */\n"
"    \n"
"}\n"
"/* 鼠标经过改变按钮颜色 */\n"
"QPushButton:hover\n"
"{\n"
"    background-color: rgb(0, 150, 0);\n"
"}\n"
"")
        self.pushButton_2.setText("")
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap("icon/更改.svg"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.pushButton_2.setIcon(icon1)
        self.pushButton_2.setObjectName("pushButton_2")
        self.lineEdit_1 = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_1.setGeometry(QtCore.QRect(11, 11, 721, 22))
        font = QtGui.QFont()
        font.setFamily("Cascadia Code SemiBold")
        font.setPointSize(9)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(7)
        self.lineEdit_1.setFont(font)
        self.lineEdit_1.setStyleSheet("QLineEdit{\n"
"    border-style: outset;  /* 边界内凹 */\n"
"    border-width: 1px;  /* 边界宽度 */\n"
"    border-radius:5px; /*边界圆滑*/\n"
"    \n"
"    font: 63 9pt \"Cascadia Code SemiBold\";\n"
"}\n"
"")
        self.lineEdit_1.setObjectName("lineEdit_1")
        self.stackedWidget = QtWidgets.QStackedWidget(self.centralwidget)
        self.stackedWidget.setGeometry(QtCore.QRect(0, 40, 1121, 681))
        self.stackedWidget.setObjectName("stackedWidget")
        self.page = QtWidgets.QWidget()
        self.page.setObjectName("page")
        self.treeView_1 = QtWidgets.QTreeView(self.page)
        self.treeView_1.setGeometry(QtCore.QRect(10, 0, 219, 518))
        self.treeView_1.setAutoFillBackground(False)
        self.treeView_1.setDragDropOverwriteMode(False)
        self.treeView_1.setAlternatingRowColors(True)
        self.treeView_1.setSortingEnabled(True)
        self.treeView_1.setAnimated(False)
        self.treeView_1.setObjectName("treeView_1")
        self.textBrowser = QtWidgets.QTextBrowser(self.page)
        self.textBrowser.setEnabled(True)
        self.textBrowser.setGeometry(QtCore.QRect(230, 0, 61, 518))
        self.textBrowser.setMouseTracking(True)
        self.textBrowser.setTabletTracking(True)
        self.textBrowser.setAutoFillBackground(False)
        self.textBrowser.setVerticalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOff)
        self.textBrowser.setHorizontalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOff)
        self.textBrowser.setReadOnly(True)
        self.textBrowser.setObjectName("textBrowser")
        self.textEdit = QtWidgets.QTextEdit(self.page)
        self.textEdit.setGeometry(QtCore.QRect(290, 0, 584, 518))
        self.textEdit.setVerticalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOn)
        self.textEdit.setHorizontalScrollBarPolicy(QtCore.Qt.ScrollBarAsNeeded)
        self.textEdit.setTabStopWidth(40)
        self.textEdit.setObjectName("textEdit")
        self.textBrowser_1 = QtWidgets.QTextBrowser(self.page)
        self.textBrowser_1.setGeometry(QtCore.QRect(880, 0, 241, 671))
        self.textBrowser_1.setObjectName("textBrowser_1")
        self.textBrowser_2 = QtWidgets.QTextBrowser(self.page)
        self.textBrowser_2.setGeometry(QtCore.QRect(10, 520, 864, 150))
        self.textBrowser_2.setObjectName("textBrowser_2")
        self.stackedWidget.addWidget(self.page)
        self.page_2 = QtWidgets.QWidget()
        self.page_2.setObjectName("page_2")
        self.textEdit_2 = QtWidgets.QTextEdit(self.page_2)
        self.textEdit_2.setGeometry(QtCore.QRect(70, 0, 511, 411))
        self.textEdit_2.setVerticalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOn)
        self.textEdit_2.setHorizontalScrollBarPolicy(QtCore.Qt.ScrollBarAsNeeded)
        self.textEdit_2.setTabStopWidth(40)
        self.textEdit_2.setObjectName("textEdit_2")
        self.textBrowser_4 = QtWidgets.QTextBrowser(self.page_2)
        self.textBrowser_4.setGeometry(QtCore.QRect(10, 419, 571, 251))
        self.textBrowser_4.setObjectName("textBrowser_4")
        self.textBrowser_5 = QtWidgets.QTextBrowser(self.page_2)
        self.textBrowser_5.setEnabled(True)
        self.textBrowser_5.setGeometry(QtCore.QRect(10, 0, 61, 411))
        self.textBrowser_5.setMouseTracking(True)
        self.textBrowser_5.setTabletTracking(True)
        self.textBrowser_5.setAutoFillBackground(False)
        self.textBrowser_5.setVerticalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOff)
        self.textBrowser_5.setHorizontalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOff)
        self.textBrowser_5.setReadOnly(True)
        self.textBrowser_5.setObjectName("textBrowser_5")
        self.textEdit_3 = QtWidgets.QTextEdit(self.page_2)
        self.textEdit_3.setGeometry(QtCore.QRect(590, 0, 531, 671))
        self.textEdit_3.setVerticalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOn)
        self.textEdit_3.setHorizontalScrollBarPolicy(QtCore.Qt.ScrollBarAsNeeded)
        self.textEdit_3.setTabStopWidth(40)
        self.textEdit_3.setObjectName("textEdit_3")
        self.stackedWidget.addWidget(self.page_2)
        self.pushButton_3 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_3.setGeometry(QtCore.QRect(910, 10, 61, 22))
        font = QtGui.QFont()
        font.setFamily("16px")
        font.setPointSize(10)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.pushButton_3.setFont(font)
        self.pushButton_3.setAutoFillBackground(False)
        self.pushButton_3.setStyleSheet("QPushButton\n"
"{\n"
"    background-color:rgb(147, 221, 0); /*背景色*/ \n"
"    border-style: outset;    /* 边界内凹 */\n"
"    border-width: 1px;     /* 边边界宽度 */\n"
"    border-radius: 5px; /* 边界圆滑 */\n"
"    font: dengxian 16px;     /* 字体大小 */\n"
"    min-width: 2em;\n"
"    color: white; /* 字体颜色 */\n"
"    \n"
"}\n"
"/* 鼠标经过改变按钮颜色 */\n"
"QPushButton:hover\n"
"{\n"
"    background-color: rgb(131, 194, 97);\n"
"}\n"
"")
        self.pushButton_3.setText("")
        icon2 = QtGui.QIcon()
        icon2.addPixmap(QtGui.QPixmap("icon/上一页.svg"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.pushButton_3.setIcon(icon2)
        self.pushButton_3.setObjectName("pushButton_3")
        self.pushButton_4 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_4.setGeometry(QtCore.QRect(1060, 10, 61, 22))
        font = QtGui.QFont()
        font.setFamily("16px")
        font.setPointSize(10)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.pushButton_4.setFont(font)
        self.pushButton_4.setAutoFillBackground(False)
        self.pushButton_4.setStyleSheet("QPushButton\n"
"{\n"
"    background-color:rgb(255, 170, 127); /*背景色*/ \n"
"    border-style: outset;    /* 边界内凹 */\n"
"    border-width: 1px;     /* 边边界宽度 */\n"
"    border-radius: 5px; /* 边界圆滑 */\n"
"    font: dengxian 16px;     /* 字体大小 */\n"
"    min-width: 2em;\n"
"    color: white; /* 字体颜色 */\n"
"    \n"
"}\n"
"/* 鼠标经过改变按钮颜色 */\n"
"QPushButton:hover\n"
"{\n"
"    background-color: rgb(223, 148, 111);\n"
"}\n"
"")
        self.pushButton_4.setText("")
        icon3 = QtGui.QIcon()
        icon3.addPixmap(QtGui.QPixmap("icon/下一页.svg"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.pushButton_4.setIcon(icon3)
        self.pushButton_4.setObjectName("pushButton_4")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(980, 10, 71, 21))
        font = QtGui.QFont()
        font.setFamily("Arial Black")
        font.setPointSize(10)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(10)
        self.label.setFont(font)
        self.label.setStyleSheet("QLabel{\n"
"    color:rgb(255, 30, 214);\n"
"    font: 87 10pt \"Arial Black\";\n"
"}\n"
"")
        self.label.setObjectName("label")
        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 1185, 24))
        self.menubar.setStyleSheet("*{\n"
"    font-family: dengxian;\n"
"    font-size: 17px;\n"
"    color: rgb(255, 255, 255);\n"
"    background-color: rgb(70, 70, 70); /*背景色*/\n"
"}")
        self.menubar.setObjectName("menubar")
        self.menuEdit = QtWidgets.QMenu(self.menubar)
        self.menuEdit.setObjectName("menuEdit")
        self.menuView = QtWidgets.QMenu(self.menubar)
        self.menuView.setObjectName("menuView")
        self.menuTheme = QtWidgets.QMenu(self.menuView)
        self.menuTheme.setObjectName("menuTheme")
        self.menuLanguage = QtWidgets.QMenu(self.menuView)
        self.menuLanguage.setObjectName("menuLanguage")
        self.menuHelp = QtWidgets.QMenu(self.menubar)
        self.menuHelp.setObjectName("menuHelp")
        self.menuFile = QtWidgets.QMenu(self.menubar)
        self.menuFile.setObjectName("menuFile")
        self.menuWords = QtWidgets.QMenu(self.menubar)
        self.menuWords.setObjectName("menuWords")
        self.menuGramer = QtWidgets.QMenu(self.menubar)
        self.menuGramer.setObjectName("menuGramer")
        self.menuMidCode = QtWidgets.QMenu(self.menubar)
        self.menuMidCode.setObjectName("menuMidCode")
        self.menuTarget = QtWidgets.QMenu(self.menubar)
        self.menuTarget.setObjectName("menuTarget")
        self.menuTools = QtWidgets.QMenu(self.menubar)
        self.menuTools.setObjectName("menuTools")
        MainWindow.setMenuBar(self.menubar)
        self.toolBarDown = QtWidgets.QToolBar(MainWindow)
        self.toolBarDown.setObjectName("toolBarDown")
        MainWindow.addToolBar(QtCore.Qt.BottomToolBarArea, self.toolBarDown)
        self.toolBarUp = QtWidgets.QToolBar(MainWindow)
        self.toolBarUp.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.toolBarUp.setObjectName("toolBarUp")
        MainWindow.addToolBar(QtCore.Qt.TopToolBarArea, self.toolBarUp)
        self.toolBarRight = QtWidgets.QToolBar(MainWindow)
        self.toolBarRight.setObjectName("toolBarRight")
        MainWindow.addToolBar(QtCore.Qt.RightToolBarArea, self.toolBarRight)
        self.toolBarLeft = QtWidgets.QToolBar(MainWindow)
        self.toolBarLeft.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.toolBarLeft.setObjectName("toolBarLeft")
        MainWindow.addToolBar(QtCore.Qt.LeftToolBarArea, self.toolBarLeft)
        self.actionVision = QtWidgets.QAction(MainWindow)
        icon4 = QtGui.QIcon()
        icon4.addPixmap(QtGui.QPixmap("icon/版本.svg"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.actionVision.setIcon(icon4)
        self.actionVision.setObjectName("actionVision")
        self.actionSetting = QtWidgets.QAction(MainWindow)
        icon5 = QtGui.QIcon()
        icon5.addPixmap(QtGui.QPixmap("icon/设置.svg"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.actionSetting.setIcon(icon5)
        self.actionSetting.setObjectName("actionSetting")
        self.actionExit = QtWidgets.QAction(MainWindow)
        icon6 = QtGui.QIcon()
        icon6.addPixmap(QtGui.QPixmap("icon/退出.svg"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.actionExit.setIcon(icon6)
        self.actionExit.setObjectName("actionExit")
        self.actionTips = QtWidgets.QAction(MainWindow)
        icon7 = QtGui.QIcon()
        icon7.addPixmap(QtGui.QPixmap("icon/提示.svg"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.actionTips.setIcon(icon7)
        self.actionTips.setObjectName("actionTips")
        self.actionDonate = QtWidgets.QAction(MainWindow)
        icon8 = QtGui.QIcon()
        icon8.addPixmap(QtGui.QPixmap("icon/捐赠.svg"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.actionDonate.setIcon(icon8)
        self.actionDonate.setObjectName("actionDonate")
        self.actionAppearance = QtWidgets.QAction(MainWindow)
        icon9 = QtGui.QIcon()
        icon9.addPixmap(QtGui.QPixmap("icon/外观.svg"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.actionAppearance.setIcon(icon9)
        self.actionAppearance.setObjectName("actionAppearance")
        self.actionCut = QtWidgets.QAction(MainWindow)
        icon10 = QtGui.QIcon()
        icon10.addPixmap(QtGui.QPixmap("icon/剪切.svg"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.actionCut.setIcon(icon10)
        self.actionCut.setObjectName("actionCut")
        self.actionPaste = QtWidgets.QAction(MainWindow)
        icon11 = QtGui.QIcon()
        icon11.addPixmap(QtGui.QPixmap("icon/粘贴.svg"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.actionPaste.setIcon(icon11)
        self.actionPaste.setObjectName("actionPaste")
        self.actionDelete = QtWidgets.QAction(MainWindow)
        icon12 = QtGui.QIcon()
        icon12.addPixmap(QtGui.QPixmap("icon/删除.svg"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.actionDelete.setIcon(icon12)
        self.actionDelete.setObjectName("actionDelete")
        self.actionFind = QtWidgets.QAction(MainWindow)
        self.actionFind.setCheckable(False)
        icon13 = QtGui.QIcon()
        icon13.addPixmap(QtGui.QPixmap("icon/搜索.svg"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.actionFind.setIcon(icon13)
        self.actionFind.setObjectName("actionFind")
        self.actionDark = QtWidgets.QAction(MainWindow)
        icon14 = QtGui.QIcon()
        icon14.addPixmap(QtGui.QPixmap("icon/dark.svg"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.actionDark.setIcon(icon14)
        self.actionDark.setObjectName("actionDark")
        self.actionLight = QtWidgets.QAction(MainWindow)
        icon15 = QtGui.QIcon()
        icon15.addPixmap(QtGui.QPixmap("icon/light.svg"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.actionLight.setIcon(icon15)
        self.actionLight.setObjectName("actionLight")
        self.actionFresh = QtWidgets.QAction(MainWindow)
        icon16 = QtGui.QIcon()
        icon16.addPixmap(QtGui.QPixmap("icon/fresh.svg"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.actionFresh.setIcon(icon16)
        self.actionFresh.setObjectName("actionFresh")
        self.actionRetro = QtWidgets.QAction(MainWindow)
        icon17 = QtGui.QIcon()
        icon17.addPixmap(QtGui.QPixmap("icon/retro.svg"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.actionRetro.setIcon(icon17)
        self.actionRetro.setObjectName("actionRetro")
        self.actionChinese = QtWidgets.QAction(MainWindow)
        icon18 = QtGui.QIcon()
        icon18.addPixmap(QtGui.QPixmap("icon/中文显示.svg"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.actionChinese.setIcon(icon18)
        self.actionChinese.setObjectName("actionChinese")
        self.actionEnglish = QtWidgets.QAction(MainWindow)
        icon19 = QtGui.QIcon()
        icon19.addPixmap(QtGui.QPixmap("icon/英文显示.svg"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.actionEnglish.setIcon(icon19)
        self.actionEnglish.setObjectName("actionEnglish")
        self.actionSave = QtWidgets.QAction(MainWindow)
        icon20 = QtGui.QIcon()
        icon20.addPixmap(QtGui.QPixmap("icon/保存.svg"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.actionSave.setIcon(icon20)
        self.actionSave.setObjectName("actionSave")
        self.actionAbout = QtWidgets.QAction(MainWindow)
        icon21 = QtGui.QIcon()
        icon21.addPixmap(QtGui.QPixmap("icon/关于.svg"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.actionAbout.setIcon(icon21)
        self.actionAbout.setObjectName("actionAbout")
        self.actionSaveOther = QtWidgets.QAction(MainWindow)
        icon22 = QtGui.QIcon()
        icon22.addPixmap(QtGui.QPixmap("icon/另存为.svg"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.actionSaveOther.setIcon(icon22)
        self.actionSaveOther.setObjectName("actionSaveOther")
        self.actionUndo = QtWidgets.QAction(MainWindow)
        icon23 = QtGui.QIcon()
        icon23.addPixmap(QtGui.QPixmap("icon/撤销.svg"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.actionUndo.setIcon(icon23)
        self.actionUndo.setObjectName("actionUndo")
        self.actionRedo = QtWidgets.QAction(MainWindow)
        icon24 = QtGui.QIcon()
        icon24.addPixmap(QtGui.QPixmap("icon/恢复.svg"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.actionRedo.setIcon(icon24)
        self.actionRedo.setObjectName("actionRedo")
        self.actionCopy = QtWidgets.QAction(MainWindow)
        icon25 = QtGui.QIcon()
        icon25.addPixmap(QtGui.QPixmap("icon/复制.svg"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.actionCopy.setIcon(icon25)
        self.actionCopy.setObjectName("actionCopy")
        self.actionOpen = QtWidgets.QAction(MainWindow)
        icon26 = QtGui.QIcon()
        icon26.addPixmap(QtGui.QPixmap("icon/文件夹打开.svg"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.actionOpen.setIcon(icon26)
        self.actionOpen.setObjectName("actionOpen")
        self.actionNewFile = QtWidgets.QAction(MainWindow)
        icon27 = QtGui.QIcon()
        icon27.addPixmap(QtGui.QPixmap("icon/新建.svg"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.actionNewFile.setIcon(icon27)
        self.actionNewFile.setObjectName("actionNewFile")
        self.actionWordRun = QtWidgets.QAction(MainWindow)
        icon28 = QtGui.QIcon()
        icon28.addPixmap(QtGui.QPixmap("icon/run_token.svg"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.actionWordRun.setIcon(icon28)
        self.actionWordRun.setObjectName("actionWordRun")
        self.actionPredictRun = QtWidgets.QAction(MainWindow)
        icon29 = QtGui.QIcon()
        icon29.addPixmap(QtGui.QPixmap("icon/run_grammar.svg"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.actionPredictRun.setIcon(icon29)
        self.actionPredictRun.setObjectName("actionPredictRun")
        self.actionMidCodeRun = QtWidgets.QAction(MainWindow)
        icon30 = QtGui.QIcon()
        icon30.addPixmap(QtGui.QPixmap("icon/run_middle.svg"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.actionMidCodeRun.setIcon(icon30)
        self.actionMidCodeRun.setObjectName("actionMidCodeRun")
        self.actionTargetRun = QtWidgets.QAction(MainWindow)
        icon31 = QtGui.QIcon()
        icon31.addPixmap(QtGui.QPixmap("icon/run_target.svg"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.actionTargetRun.setIcon(icon31)
        self.actionTargetRun.setObjectName("actionTargetRun")
        self.actionRunCode = QtWidgets.QAction(MainWindow)
        icon32 = QtGui.QIcon()
        icon32.addPixmap(QtGui.QPixmap("icon/试运行.svg"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.actionRunCode.setIcon(icon32)
        self.actionRunCode.setObjectName("actionRunCode")
        self.actionBuildCode = QtWidgets.QAction(MainWindow)
        icon33 = QtGui.QIcon()
        icon33.addPixmap(QtGui.QPixmap("icon/建立.svg"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.actionBuildCode.setIcon(icon33)
        self.actionBuildCode.setObjectName("actionBuildCode")
        self.actionOpenRecent = QtWidgets.QAction(MainWindow)
        self.actionOpenRecent.setObjectName("actionOpenRecent")
        self.actionWordsSizeUp = QtWidgets.QAction(MainWindow)
        icon34 = QtGui.QIcon()
        icon34.addPixmap(QtGui.QPixmap("icon/字体放大.svg"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.actionWordsSizeUp.setIcon(icon34)
        self.actionWordsSizeUp.setObjectName("actionWordsSizeUp")
        self.actionWordsSizeDown = QtWidgets.QAction(MainWindow)
        icon35 = QtGui.QIcon()
        icon35.addPixmap(QtGui.QPixmap("icon/字体缩小.svg"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.actionWordsSizeDown.setIcon(icon35)
        self.actionWordsSizeDown.setObjectName("actionWordsSizeDown")
        self.actionWordIncline = QtWidgets.QAction(MainWindow)
        self.actionWordIncline.setCheckable(True)
        icon36 = QtGui.QIcon()
        icon36.addPixmap(QtGui.QPixmap("icon/字体斜体.svg"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.actionWordIncline.setIcon(icon36)
        self.actionWordIncline.setObjectName("actionWordIncline")
        self.actionWordBlod = QtWidgets.QAction(MainWindow)
        self.actionWordBlod.setCheckable(True)
        icon37 = QtGui.QIcon()
        icon37.addPixmap(QtGui.QPixmap("icon/字体加粗.svg"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.actionWordBlod.setIcon(icon37)
        self.actionWordBlod.setObjectName("actionWordBlod")
        self.actionWordAutoRun = QtWidgets.QAction(MainWindow)
        icon38 = QtGui.QIcon()
        icon38.addPixmap(QtGui.QPixmap("icon/开始.svg"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.actionWordAutoRun.setIcon(icon38)
        self.actionWordAutoRun.setObjectName("actionWordAutoRun")
        self.actionNextPage = QtWidgets.QAction(MainWindow)
        self.actionNextPage.setIcon(icon3)
        self.actionNextPage.setObjectName("actionNextPage")
        self.actionLastPage = QtWidgets.QAction(MainWindow)
        self.actionLastPage.setIcon(icon2)
        self.actionLastPage.setObjectName("actionLastPage")
        self.actionRecursionRun = QtWidgets.QAction(MainWindow)
        self.actionRecursionRun.setIcon(icon29)
        self.actionRecursionRun.setObjectName("actionRecursionRun")
        self.menuEdit.addAction(self.actionFind)
        self.menuEdit.addAction(self.actionCopy)
        self.menuEdit.addAction(self.actionCut)
        self.menuEdit.addAction(self.actionPaste)
        self.menuEdit.addSeparator()
        self.menuEdit.addAction(self.actionWordsSizeUp)
        self.menuEdit.addAction(self.actionWordsSizeDown)
        self.menuEdit.addAction(self.actionUndo)
        self.menuEdit.addAction(self.actionRedo)
        self.menuEdit.addSeparator()
        self.menuEdit.addAction(self.actionDelete)
        self.menuTheme.addAction(self.actionFresh)
        self.menuTheme.addAction(self.actionRetro)
        self.menuTheme.addAction(self.actionLight)
        self.menuTheme.addAction(self.actionDark)
        self.menuLanguage.addAction(self.actionChinese)
        self.menuLanguage.addAction(self.actionEnglish)
        self.menuView.addAction(self.actionAppearance)
        self.menuView.addAction(self.menuTheme.menuAction())
        self.menuView.addAction(self.menuLanguage.menuAction())
        self.menuHelp.addAction(self.actionTips)
        self.menuHelp.addAction(self.actionAbout)
        self.menuHelp.addSeparator()
        self.menuHelp.addAction(self.actionDonate)
        self.menuHelp.addAction(self.actionVision)
        self.menuFile.addAction(self.actionNewFile)
        self.menuFile.addAction(self.actionOpen)
        self.menuFile.addAction(self.actionOpenRecent)
        self.menuFile.addSeparator()
        self.menuFile.addAction(self.actionSave)
        self.menuFile.addAction(self.actionSaveOther)
        self.menuFile.addSeparator()
        self.menuFile.addAction(self.actionSetting)
        self.menuFile.addAction(self.actionExit)
        self.menuFile.addSeparator()
        self.menuWords.addAction(self.actionWordRun)
        self.menuWords.addAction(self.actionWordAutoRun)
        self.menuGramer.addAction(self.actionPredictRun)
        self.menuGramer.addAction(self.actionRecursionRun)
        self.menuMidCode.addAction(self.actionMidCodeRun)
        self.menuTarget.addAction(self.actionTargetRun)
        self.menuTools.addAction(self.actionRunCode)
        self.menuTools.addAction(self.actionBuildCode)
        self.menubar.addAction(self.menuFile.menuAction())
        self.menubar.addAction(self.menuEdit.menuAction())
        self.menubar.addAction(self.menuView.menuAction())
        self.menubar.addAction(self.menuHelp.menuAction())
        self.menubar.addAction(self.menuTools.menuAction())
        self.menubar.addAction(self.menuWords.menuAction())
        self.menubar.addAction(self.menuGramer.menuAction())
        self.menubar.addAction(self.menuMidCode.menuAction())
        self.menubar.addAction(self.menuTarget.menuAction())
        self.toolBarUp.addAction(self.actionWordIncline)
        self.toolBarUp.addAction(self.actionWordBlod)
        self.toolBarUp.addAction(self.actionWordsSizeUp)
        self.toolBarUp.addAction(self.actionWordsSizeDown)
        self.toolBarUp.addSeparator()
        self.toolBarUp.addAction(self.actionCopy)
        self.toolBarUp.addAction(self.actionCut)
        self.toolBarUp.addAction(self.actionPaste)
        self.toolBarUp.addSeparator()
        self.toolBarUp.addAction(self.actionUndo)
        self.toolBarUp.addAction(self.actionRedo)
        self.toolBarUp.addSeparator()
        self.toolBarUp.addAction(self.actionWordRun)
        self.toolBarUp.addAction(self.actionRecursionRun)
        self.toolBarUp.addAction(self.actionMidCodeRun)
        self.toolBarUp.addAction(self.actionTargetRun)
        self.toolBarUp.addSeparator()
        self.toolBarUp.addAction(self.actionBuildCode)
        self.toolBarUp.addAction(self.actionRunCode)
        self.toolBarUp.addSeparator()
        self.toolBarUp.addAction(self.actionLastPage)
        self.toolBarUp.addAction(self.actionNextPage)
        self.toolBarLeft.addAction(self.actionOpen)
        self.toolBarLeft.addAction(self.actionFind)
        self.toolBarLeft.addAction(self.actionSave)
        self.toolBarLeft.addSeparator()
        self.toolBarLeft.addAction(self.actionTips)
        self.toolBarLeft.addAction(self.actionSetting)
        self.toolBarLeft.addAction(self.actionExit)

        self.retranslateUi(MainWindow)
        self.stackedWidget.setCurrentIndex(1)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.lineEdit_1.setText(_translate("MainWindow", "F:\\Projects\\Python Pycharm\\Compiler\\Data\\helloWorld.c"))
        self.textBrowser_1.setHtml(_translate("MainWindow", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'SimSun\'; font-size:9pt; font-weight:400; font-style:normal;\">\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p></body></html>"))
        self.textBrowser_2.setHtml(_translate("MainWindow", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'SimSun\'; font-size:9pt; font-weight:400; font-style:normal;\">\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p></body></html>"))
        self.textBrowser_4.setHtml(_translate("MainWindow", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'SimSun\'; font-size:9pt; font-weight:400; font-style:normal;\">\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p></body></html>"))
        self.label.setText(_translate("MainWindow", "PART 1"))
        self.menuEdit.setTitle(_translate("MainWindow", "Edit(E)"))
        self.menuView.setTitle(_translate("MainWindow", "View(V)"))
        self.menuTheme.setTitle(_translate("MainWindow", "Theme"))
        self.menuLanguage.setTitle(_translate("MainWindow", "Language"))
        self.menuHelp.setTitle(_translate("MainWindow", "Help(H)"))
        self.menuFile.setTitle(_translate("MainWindow", "File(F)"))
        self.menuWords.setTitle(_translate("MainWindow", "词法分析(W)"))
        self.menuGramer.setTitle(_translate("MainWindow", "语法分析(P)"))
        self.menuMidCode.setTitle(_translate("MainWindow", "中间代码(M)"))
        self.menuTarget.setTitle(_translate("MainWindow", "目标代码生成(O)"))
        self.menuTools.setTitle(_translate("MainWindow", "Tools(T)"))
        self.toolBarDown.setWindowTitle(_translate("MainWindow", "toolBar"))
        self.toolBarUp.setWindowTitle(_translate("MainWindow", "toolBar_2"))
        self.toolBarRight.setWindowTitle(_translate("MainWindow", "toolBar_3"))
        self.toolBarLeft.setWindowTitle(_translate("MainWindow", "toolBar_4"))
        self.actionVision.setText(_translate("MainWindow", "Version"))
        self.actionSetting.setText(_translate("MainWindow", "Setting"))
        self.actionExit.setText(_translate("MainWindow", "Exit"))
        self.actionTips.setText(_translate("MainWindow", "Tips"))
        self.actionDonate.setText(_translate("MainWindow", "Donate"))
        self.actionAppearance.setText(_translate("MainWindow", "Appearance"))
        self.actionCut.setText(_translate("MainWindow", "Cut"))
        self.actionCut.setShortcut(_translate("MainWindow", "Ctrl+X"))
        self.actionPaste.setText(_translate("MainWindow", "Paste"))
        self.actionPaste.setShortcut(_translate("MainWindow", "Ctrl+V"))
        self.actionDelete.setText(_translate("MainWindow", "Delete"))
        self.actionFind.setText(_translate("MainWindow", "Find"))
        self.actionFind.setShortcut(_translate("MainWindow", "Ctrl+F"))
        self.actionDark.setText(_translate("MainWindow", "Dark"))
        self.actionLight.setText(_translate("MainWindow", "Light"))
        self.actionFresh.setText(_translate("MainWindow", "Fresh"))
        self.actionRetro.setText(_translate("MainWindow", "Retro"))
        self.actionChinese.setText(_translate("MainWindow", "Chinese"))
        self.actionEnglish.setText(_translate("MainWindow", "English"))
        self.actionSave.setText(_translate("MainWindow", "Save"))
        self.actionSave.setShortcut(_translate("MainWindow", "Ctrl+S"))
        self.actionAbout.setText(_translate("MainWindow", "About"))
        self.actionSaveOther.setText(_translate("MainWindow", "Save other"))
        self.actionSaveOther.setToolTip(_translate("MainWindow", "Save other"))
        self.actionUndo.setText(_translate("MainWindow", "Undo"))
        self.actionUndo.setShortcut(_translate("MainWindow", "Ctrl+Z"))
        self.actionRedo.setText(_translate("MainWindow", "Redo"))
        self.actionRedo.setShortcut(_translate("MainWindow", "Ctrl+Y"))
        self.actionCopy.setText(_translate("MainWindow", "Copy"))
        self.actionCopy.setShortcut(_translate("MainWindow", "Ctrl+C"))
        self.actionOpen.setText(_translate("MainWindow", "Open"))
        self.actionNewFile.setText(_translate("MainWindow", "New File"))
        self.actionWordRun.setText(_translate("MainWindow", "Run"))
        self.actionWordRun.setToolTip(_translate("MainWindow", "WordRun"))
        self.actionPredictRun.setText(_translate("MainWindow", "PredictRun"))
        self.actionPredictRun.setToolTip(_translate("MainWindow", "GramerRun"))
        self.actionMidCodeRun.setText(_translate("MainWindow", "Run"))
        self.actionMidCodeRun.setToolTip(_translate("MainWindow", "MidCodeRun"))
        self.actionTargetRun.setText(_translate("MainWindow", "Run"))
        self.actionTargetRun.setToolTip(_translate("MainWindow", "TargetRun"))
        self.actionRunCode.setText(_translate("MainWindow", "RunCode"))
        self.actionRunCode.setToolTip(_translate("MainWindow", "RunCode"))
        self.actionRunCode.setShortcut(_translate("MainWindow", "Ctrl+R"))
        self.actionBuildCode.setText(_translate("MainWindow", "BuildCode"))
        self.actionBuildCode.setToolTip(_translate("MainWindow", "BuildCode"))
        self.actionBuildCode.setShortcut(_translate("MainWindow", "Ctrl+B"))
        self.actionOpenRecent.setText(_translate("MainWindow", "Open Recent"))
        self.actionWordsSizeUp.setText(_translate("MainWindow", "SizeUp"))
        self.actionWordsSizeDown.setText(_translate("MainWindow", "SizeDown"))
        self.actionWordIncline.setText(_translate("MainWindow", "WordIncline"))
        self.actionWordBlod.setText(_translate("MainWindow", "WordBlod"))
        self.actionWordAutoRun.setText(_translate("MainWindow", "wordAutoRun"))
        self.actionWordAutoRun.setToolTip(_translate("MainWindow", "wordAutoRun"))
        self.actionNextPage.setText(_translate("MainWindow", "NextPage"))
        self.actionNextPage.setToolTip(_translate("MainWindow", "NextPage"))
        self.actionLastPage.setText(_translate("MainWindow", "LastPage"))
        self.actionLastPage.setToolTip(_translate("MainWindow", "LastPage"))
        self.actionRecursionRun.setText(_translate("MainWindow", "RecursionRun"))
        self.actionRecursionRun.setToolTip(_translate("MainWindow", "RecursionRun"))
import dark_rc