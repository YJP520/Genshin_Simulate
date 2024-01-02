"""
@Project : GenShin - Simulate
@Time : 2024/01/02
@Author : YU.J.P
@Version: 3.0
@CopyRight: YU.J.P
"""

########################################################################################################################
# OS
import os
import sys
import webbrowser

# PYQT5
from PyQt5.QtCore import Qt, QDir
from PyQt5.QtWidgets import QMainWindow, QApplication, QMessageBox, QFileDialog, QHeaderView
from PyQt5.QtGui import QIcon, QStandardItem, QStandardItemModel, QTextImageFormat
# ui文件经转换成py代码之后，导入窗体
from main_ui import Ui_MainWindow
# 插件类
from plug_in.Colors import Color


########################################################################################################################

# 主窗口继承类
class Main_UI(QMainWindow, Ui_MainWindow):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.setupUi(self)

        # # 文件路径
        # self.editFilePath = 'F:/Projects/Python Pycharm/Compiler/data/Code/Ex1/helloWorld.c'  # 编辑代码
        # self.imagePath1 = './module/Part_2/TreeImage/grammarTree.gv'  # 预测分析文法树路径
        # self.imagePath2 = './module/Part_3/TreeImage/GTree.gv'  # 递归下降文法树路径
        # 文件内容 缓冲
        self.content = None  # 词法分析内容
        self.content_2 = None  # 语法分析内容
        # 文字大小
        self.fontSize = 14  # 默认14 词法分析
        self.fontSize_2 = 14  # 默认14 语法分析
        # 编辑框行数
        self.lineNumber = 1  # 词法分析绑定行号
        self.lineNumber_2 = 1  # 语法分析绑定行号

        # 控件初始化
        self.AllUnitsInit()
        # 控件绑定
        self.wightBandInit()  # 行号显示
        self.fileClassifyMenu()  # 文件分级目录
        # 调用监听函数
        self.controllerInit()
        # 按钮设置
        self.buttonInit()
        # 当前界面编号 初始化
        self.pageIndex = 0
        self.stackedWidget.setCurrentIndex(0)

    ####################################################################################################################

    # 控件初始化
    def AllUnitsInit(self):
        # LineEdit_1 初始化
        self.lineEdit_1.clear()
        # LineEdit 初始化 pageIndex + 1
        self.label.setText('PART 1')
        # TextEdit 初始化
        self.textEdit.clear()
        self.textEdit.setTextColor(Qt.darkMagenta)  # 字体颜色
        self.textEdit.setFontFamily("Cascadia Code SemiBold")  # 字体
        self.textEdit.setFontPointSize(self.fontSize)  # 字体大小
        self.textEdit.insertPlainText(' ')  # BUG
        # TextEdit_2 初始化
        self.textEdit_2.clear()
        self.textEdit_2.setTextColor(Qt.darkMagenta)  # 字体颜色
        self.textEdit_2.setFontFamily("Cascadia Code SemiBold")  # 字体
        self.textEdit_2.setFontPointSize(self.fontSize)  # 字体大小
        self.textEdit_2.insertPlainText(' ')  # BUG
        # TextBrowser_1 初始化
        self.textBrowser_1.clear()
        self.textBrowser_1.setFontFamily("Cascadia Code SemiBold")
        self.textBrowser_1.setFontPointSize(12)
        # TextBrowser_2 初始化
        self.textBrowser_2.clear()
        self.textBrowser_2.setFontFamily("dengxian")
        self.textBrowser_2.setFontPointSize(12)
        # TextBrowser_4 初始化
        self.textBrowser_4.clear()
        self.textBrowser_4.setFontFamily("dengxian")
        self.textBrowser_4.setFontPointSize(12)
        # TextBrowser_5 初始化
        self.textBrowser_5.clear()
        self.textBrowser_5.setFontFamily("dengxian")
        self.textBrowser_5.setFontPointSize(12)

    ####################################################################################################################

    # 控件绑定
    def wightBandInit(self):
        # 语法分析界面
        self.textEdit.setLineWrapMode(0)  # 横向滚动条
        self.textEdit.verticalScrollBar().valueChanged.connect(self.on_scroll_text_edit)
        self.textBrowser.verticalScrollBar().valueChanged.connect(self.on_scroll_text_browser)
        # 语法分析界面
        self.textEdit_2.setLineWrapMode(0)  # 横向滚动条
        self.textEdit_2.verticalScrollBar().valueChanged.connect(self.on_scroll_text_edit_2)
        self.textBrowser_5.verticalScrollBar().valueChanged.connect(self.on_scroll_text_browser_5)

    # 当TextEdit的滚动位置发生变化时，更新TextBrowser的滚动位置 词法分析
    def on_scroll_text_edit(self, value):
        self.textBrowser.verticalScrollBar().setValue(value)

    # 当TextBrowser的滚动位置发生变化时，更新TextEdit的滚动位置 词法分析
    def on_scroll_text_browser(self, value):
        self.textEdit.verticalScrollBar().setValue(value)

    # 当TextEdit_2的滚动位置发生变化时，更新TextBrowser的滚动位置 语法分析
    def on_scroll_text_edit_2(self, value):
        self.textBrowser_5.verticalScrollBar().setValue(value)

    # 当TextBrowser_2的滚动位置发生变化时，更新TextEdit的滚动位置 语法分析
    def on_scroll_text_browser_5(self, value):
        self.textEdit_2.verticalScrollBar().setValue(value)

    ####################################################################################################################

    # 设置QFileSystemModel的根路径
    def fileClassifyMenu(self):
        root_path = '/data'
        root_item = QStandardItem(root_path)
        self.file_system_model = QStandardItemModel()
        self.treeView_1.setModel(self.file_system_model)
        # 设置QTreeView的名称
        self.treeView_1.header().setSectionResizeMode(QHeaderView.Stretch)
        self.treeView_1.setHeaderHidden(False)
        self.treeView_1.header().setStyleSheet("font-size: 18px; font-weight: bold;")
        self.file_system_model.appendRow(root_item)
        self.populate_model(root_item)

    ####################################################################################################################

    # 递归遍历目录并添加到QStandardItemModel中
    def populate_model(self, parent_item):
        parent_path = parent_item.text()
        for file_name in QDir(parent_path).entryList(QDir.NoDotAndDotDot | QDir.AllDirs):
            file_path = parent_path + '/' + file_name
            item = QStandardItem(file_name)
            item.setData(file_path, Qt.UserRole)
            parent_item.appendRow(item)
            if QDir(file_path).exists():
                self.populate_model(item)

    ####################################################################################################################

    # 监听事件都放在这里面
    def controllerInit(self):
        # File(F) 功能菜单
        # 监听 新建文件
        self.actionNewFile.triggered.connect(self.newFile)
        # 监听 文件打开
        self.actionOpen.triggered.connect(self.openFile)
        # 监听 最近文件打开
        self.actionOpenRecent.triggered.connect(self.thePass)
        # 监听 保存
        self.actionSave.triggered.connect(self.saveFile)
        # 监听 另存为
        self.actionSaveOther.triggered.connect(self.thePass)
        # 监听 设置
        self.actionSetting.triggered.connect(self.setting)
        # 监听 退出
        self.actionExit.triggered.connect(self.exit)

        # Edit(E) 功能菜单
        # 监听 查找
        self.actionFind.triggered.connect(self.find)
        # 监听 复制
        self.actionCopy.triggered.connect(self.editCopy)
        # 监听 剪切
        self.actionCut.triggered.connect(self.editCut)
        # 监听 粘贴
        self.actionPaste.triggered.connect(self.editPaste)
        # 设置斜体
        self.actionWordIncline.triggered.connect(self.wordItalic)
        # 字体大小增大
        self.actionWordsSizeUp.triggered.connect(self.wordsSizeUp)
        # 字体大小减小
        self.actionWordsSizeDown.triggered.connect(self.wordsSizeDown)
        # 监听 撤销
        self.actionRedo.triggered.connect(self.editRedo)
        # 监听 撤销上次操作
        self.actionUndo.triggered.connect(self.editUndo)
        # 监听 删除
        self.actionDelete.triggered.connect(self.thePass)

        # View(V) 功能菜单
        # 监听 外观
        self.actionAppearance.triggered.connect(self.thePass)
        # 监听 主题 选项
        self.actionFresh.triggered.connect(self.thePass)
        self.actionRetro.triggered.connect(self.thePass)
        self.actionLight.triggered.connect(self.thePass)
        self.actionDark.triggered.connect(self.thePass)
        # 监听 语言 选项
        self.actionChinese.triggered.connect(self.thePass)
        self.actionEnglish.triggered.connect(self.thePass)

        # Helps(H) 功能菜单
        # 监听 提示
        self.actionTips.triggered.connect(self.tips)
        # 监听 关于
        self.actionAbout.triggered.connect(self.about)
        # 监听 捐赠
        self.actionDonate.triggered.connect(self.donate)
        # 监听 版本
        self.actionVision.triggered.connect(self.version)

        # Tools(T) 功能菜单
        # 监听 建立代码
        # self.actionBuildCode.triggered.connect(self.build_target_code)
        # 监听 执行代码
        # self.actionRunCode.triggered.connect(self.build_target_code)

        # 词法分析(W) 功能菜单
        # 监听 手动Run
        # self.actionWordRun.triggered.connect(self.lexical_analisis_run)
        # 监听 自动Run
        # self.actionWordAutoRun.triggered.connect(self.lexical_analisis_autoRun)

        # 语法分析(P) 功能菜单
        # 监听 预测分析 Run
        # self.actionPredictRun.triggered.connect(self.syntactic_analysis_run)
        # 监听 递归下降 Run
        # self.actionRecursionRun.triggered.connect(self.recursion_analysis_run)

        # 中间代码(M) 功能菜单
        # 监听 Run
        # self.actionMidCodeRun.triggered.connect(self.middleCode_analysis_run)

        # 目标代码生成(O) 功能菜单
        # 监听 Run
        # self.actionTargetRun.triggered.connect(self.targetCode_analysis_run)

        # 界面翻页 上一页 功能菜单
        # 监听 Run
        self.actionLastPage.triggered.connect(self.lastPage)

        # 界面翻页 下一页 功能菜单
        # 监听 Run
        self.actionNextPage.triggered.connect(self.nextPage)

    # 提示动作按钮店址事件
    def thePass(self):
        QMessageBox.about(self, 'pass', '点击了功能按钮动作')

    # 新建文件
    def newFile(self):
        pass

    # 打开文件
    def openFile(self):
        # 直接调用
        self.selectFile()
        self.UpdateFile()

    # 保存文件
    def saveFile(self):
        if self.pageIndex == 0:
            self.content = self.textEdit.toPlainText()
            # print(Color.carmine, self.content)
            with open(self.editFilePath, "w") as file:
                file.write(self.content)
            # 同步行号显示框
            self.textBrowser.clear()
            # 获取行数
            self.lineNumber = 1 + 5
            for index in range(0, len(self.content)):
                if self.content[index] == '\n':
                    self.lineNumber += 1
            # 重新渲染
            for index in range(1, self.lineNumber):
                self.textBrowser.append(str(index))
            self.textBrowser.moveCursor(self.textBrowser.textCursor().Start)  # 文本框显示到顶部
        elif self.pageIndex == 1:
            self.content_2 = self.textEdit_2.toPlainText()
            # print(Color.carmine, self.content)
            with open(self.editFilePath, "w") as file:
                file.write(self.content_2)
            # 同步行号显示框
            self.textBrowser_5.clear()
            # 获取行数
            self.lineNumber_2 = 1 + 5
            for index in range(0, len(self.content_2)):
                if self.content_2[index] == '\n':
                    self.lineNumber_2 += 1
            # 重新渲染
            for index in range(1, self.lineNumber_2):
                self.textBrowser_5.append(str(index))
            self.textBrowser_5.moveCursor(self.textBrowser_5.textCursor().Start)  # 文本框显示到顶部

    # 字体斜体
    def wordItalic(self):
        if self.pageIndex == 0:
            self.textEdit.selectAll()
            if self.actionWordIncline.isChecked():
                self.textEdit.setFontItalic(1)  # 未击过
            else:
                self.textEdit.setFontItalic(0)  # 点击过
        elif self.pageIndex == 1:
            self.textEdit_2.selectAll()
            if self.actionWordIncline.isChecked():
                self.textEdit_2.setFontItalic(1)  # 未击过
            else:
                self.textEdit_2.setFontItalic(0)  # 点击过

    # 字体大小增加
    def wordsSizeUp(self):
        if self.pageIndex == 0:
            self.textEdit.selectAll()
            self.textBrowser.selectAll()
            if self.fontSize < 30:
                self.fontSize += 1
                self.textEdit.setFontPointSize(self.fontSize)
                self.textBrowser.setFontPointSize(self.fontSize)
        elif self.pageIndex == 1:
            self.textEdit_2.selectAll()
            self.textBrowser_5.selectAll()
            if self.fontSize_2 < 30:
                self.fontSize_2 += 1
                self.textEdit_2.setFontPointSize(self.fontSize_2)
                self.textBrowser_5.setFontPointSize(self.fontSize_2)

    # 字体大小减小
    def wordsSizeDown(self):
        if self.pageIndex == 0:
            self.textEdit.selectAll()
            self.textBrowser.selectAll()
            if self.fontSize > 8:
                self.fontSize -= 1
                self.textEdit.setFontPointSize(self.fontSize)
                self.textBrowser.setFontPointSize(self.fontSize)
        elif self.pageIndex == 1:
            self.textEdit_2.selectAll()
            self.textBrowser_5.selectAll()
            if self.fontSize_2 > 8:
                self.fontSize_2 -= 1
                self.textEdit_2.setFontPointSize(self.fontSize_2)
                self.textBrowser_5.setFontPointSize(self.fontSize_2)

    # copy
    def editCopy(self):
        if self.pageIndex == 0:
            self.textEdit.copy()
        elif self.pageIndex == 1:
            self.textEdit_2.copy()

    # cut
    def editCut(self):
        if self.pageIndex == 0:
            self.textEdit.cut()
        elif self.pageIndex == 1:
            self.textEdit_2.cut()

    # paste
    def editPaste(self):
        if self.pageIndex == 0:
            self.textEdit.paste()
        elif self.pageIndex == 1:
            self.textEdit_2.paste()

    # redo
    def editRedo(self):
        if self.pageIndex == 0:
            self.textEdit.redo()
        elif self.pageIndex == 1:
            self.textEdit_2.redo()

    # undo
    def editUndo(self):
        if self.pageIndex == 0:
            self.textEdit.undo()
        elif self.pageIndex == 1:
            self.textEdit_2.undo()

    # 设置动作按钮点击事件
    def setting(self):
        QMessageBox.about(self, 'Setting', '点击了设置动作')

    # 退出动作按钮店址事件
    def exit(self):
        result = QMessageBox.question(self, 'Exit提示', '确定退出程序？',
                                      QMessageBox.Yes | QMessageBox.No, QMessageBox.No)  # 默认关闭界面选择No
        if result == QMessageBox.Yes:
            self.actionExit()  # 退出
        else:
            print(Color.carmine, 'Thank you for Use.')

    # 查询动作按钮点击事件
    def find(self):
        QMessageBox.about(self, 'find', '点击了查找动作')

    # 提示动作按钮店址事件
    def tips(self):
        # word帮助文档 打开chm格式的文件
        webbrowser.open('data/Help/操作手册.chm')

    # 关于动作按钮店址事件
    def about(self):
        QMessageBox.about(self, 'about', 'The copyright belongs to YU.J.P!')

    # 捐赠动作按钮店址事件
    def donate(self):
        QMessageBox.about(self, 'Donate', '谢谢你的好意！祝你工作顺利，生活愉快！')

    # 版本动作按钮店址事件
    def version(self):
        QMessageBox.about(self, 'Version', '当前版本: V2023.05.08.2.0')

    # 界面翻页 上一页
    def lastPage(self):
        if self.pageIndex > 0:
            self.pageIndex -= 1
        self.stackedWidget.setCurrentIndex(self.pageIndex)
        self.label.setText('PART ' + str(self.pageIndex + 1))

    # 界面翻页 下一页
    def nextPage(self):
        if self.pageIndex < 1:
            self.pageIndex += 1
        self.stackedWidget.setCurrentIndex(self.pageIndex)
        self.label.setText('PART ' + str(self.pageIndex + 1))

    ####################################################################################################################

    # 按钮事件都放在这里面
    def buttonInit(self):
        self.pushButton_1.clicked.connect(self.UpdateFile)
        self.pushButton_2.clicked.connect(self.selectFile)
        self.pushButton_3.clicked.connect(self.lastPage)
        self.pushButton_4.clicked.connect(self.nextPage)
        # self.pushButton_5.clicked.connect(self.button3)

    # 按钮点击动作按钮店址事件
    def selectFile(self):
        # QMessageBox.about(self, 'Push', '点击了Push按钮点动作')
        fileName = QFileDialog.getOpenFileNames(self, "选择文件", os.getcwd(), "All Files(*);;Text Files(*.txt)")
        # print(Color.carmine, fileName[0])
        if fileName[0]:
            self.editFilePath = fileName[0][0]
            # print(self.filePath1)
            self.lineEdit_1.setText(self.editFilePath)

    # 加载文件
    def UpdateFile(self):
        if self.pageIndex == 0:
            # Update
            self.textEdit.clear()
            self.textEdit.setTextColor(Qt.darkMagenta)  # 字体颜色
            self.textEdit.setFontFamily("Cascadia Code SemiBold")  # 字体
            self.textEdit.setFontPointSize(self.fontSize)  # 字体大小
            # 加载文件数据
            self.content = ""
            self.lineNumber = 1 + 5
            # 重新加载
            self.editFilePath = self.lineEdit_1.text()
            if os.path.exists(self.editFilePath):
                buffer = open(self.editFilePath, 'r', encoding='utf-8')
                for content in buffer:  # 按行读取
                    self.lineNumber += 1  # 行数递增
                    self.textEdit.insertPlainText(content)  # 加载内容
                    self.content += content  # 记录文件
                buffer.close()

            # 同步行号显示框
            self.textBrowser.clear()
            self.textBrowser.setFontFamily("Cascadia Code SemiBold")
            self.textBrowser.setFontPointSize(self.fontSize)
            self.textBrowser.setTextColor(Qt.gray)
            for index in range(1, self.lineNumber):
                self.textBrowser.append(str(index))
            self.textBrowser.moveCursor(self.textBrowser.textCursor().Start)  # 文本框显示到顶部
        elif self.pageIndex == 1:
            # Update
            self.textEdit_2.clear()
            self.textEdit_2.setTextColor(Qt.darkMagenta)  # 字体颜色
            self.textEdit_2.setFontFamily("Cascadia Code SemiBold")  # 字体
            self.textEdit_2.setFontPointSize(self.fontSize)  # 字体大小
            # 加载文件数据
            self.content_2 = ""
            self.lineNumber_2 = 1 + 5
            # 重新加载
            self.editFilePath = self.lineEdit_1.text()
            if os.path.exists(self.editFilePath):
                buffer = open(self.editFilePath, 'r', encoding='utf-8')
                for content in buffer:  # 按行读取
                    self.lineNumber_2 += 1  # 行数递增
                    self.textEdit_2.insertPlainText(content)  # 加载内容
                    self.content_2 += content  # 记录文件
                buffer.close()
            # 同步行号显示框
            self.textBrowser_5.clear()
            self.textBrowser_5.setFontFamily("Cascadia Code SemiBold")
            self.textBrowser_5.setFontPointSize(self.fontSize)
            self.textBrowser_5.setTextColor(Qt.gray)
            for index in range(1, self.lineNumber_2):
                self.textBrowser_5.append(str(index))
            self.textBrowser_5.moveCursor(self.textBrowser_5.textCursor().Start)  # 文本框显示到顶部

    # 按钮点击动作按钮店址事件
    def button2(self):
        QMessageBox.about(self, 'Button2', '点击了按钮点动作')


########################################################################################################################


# 整合调用
class AppUI:
    def __init__(self):
        # 实例化窗口对象
        self.main_ui = Main_UI()
        # 子实验窗口
        # self.child_EX1_ui = child_EX1_UI()

        # 初始化调用
        self.init()

    def init(self):
        # 显示子窗口
        # Push Button
        # self.main_ui.pushButton.clicked.connect(self.main_ui.button_push)
        pass


########################################################################################################################


# MAIN
if __name__ == '__main__':
    app = QApplication(sys.argv)
    # 应用图标
    app.setWindowIcon(QIcon('icon/icon.jpg'))
    # app.setApplicationDisplayName('YJP-Compiler')
    app_ui = AppUI()
    # 应用名称
    app_ui.main_ui.setWindowTitle('GenShin_Simulate 1.0')
    app_ui.main_ui.show()
    # 循环不退出
    sys.exit(app.exec_())
