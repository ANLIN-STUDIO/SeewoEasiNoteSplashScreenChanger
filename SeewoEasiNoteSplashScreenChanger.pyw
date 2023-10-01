import os
import shutil
import sys
import webbrowser

import ANewPy
import win32api
import win32con
from PyQt5 import QtCore, QtWidgets, QtGui
from PyQt5.QtGui import QPixmap, QIcon
from PyQt5.QtWidgets import QMainWindow, QApplication


class Ui_MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setObjectName("MainWindow")
        self.resize(620, 410)
        self.setMinimumSize(QtCore.QSize(620, 410))
        self.setMaximumSize(QtCore.QSize(620, 410))
        self.show()
        self.centralwidget = QtWidgets.QWidget(self)
        self.centralwidget.setObjectName("centralwidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.centralwidget)
        self.verticalLayout.setObjectName("verticalLayout")
        self.frame = QtWidgets.QFrame(self.centralwidget)
        self.frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setObjectName("frame")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.frame)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.label = QtWidgets.QLabel(self.frame)
        self.label.setObjectName("label")
        self.horizontalLayout.addWidget(self.label)
        self.LE_ExePath = QtWidgets.QLineEdit(self.frame)
        self.LE_ExePath.setObjectName("LE_ExePath")
        self.horizontalLayout.addWidget(self.LE_ExePath)
        self.B_BExePath = QtWidgets.QPushButton(self.frame)
        self.B_BExePath.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.B_BExePath.setObjectName("B_BExePath")
        self.horizontalLayout.addWidget(self.B_BExePath)
        self.verticalLayout.addWidget(self.frame)
        self.line_2 = QtWidgets.QFrame(self.centralwidget)
        self.line_2.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_2.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_2.setObjectName("line_2")
        self.verticalLayout.addWidget(self.line_2)
        self.frame_2 = QtWidgets.QFrame(self.centralwidget)
        self.frame_2.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_2.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_2.setObjectName("frame_2")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout(self.frame_2)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.label_2 = QtWidgets.QLabel(self.frame_2)
        self.label_2.setObjectName("label_2")
        self.horizontalLayout_2.addWidget(self.label_2)
        spacerItem = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_2.addItem(spacerItem)
        self.L_P_SplashScreen = QtWidgets.QLabel(self.frame_2)
        self.L_P_SplashScreen.setMinimumSize(QtCore.QSize(100, 67))
        self.L_P_SplashScreen.setObjectName("L_P_SplashScreen")
        self.horizontalLayout_2.addWidget(self.L_P_SplashScreen)
        self.verticalLayout.addWidget(self.frame_2)
        self.line_3 = QtWidgets.QFrame(self.centralwidget)
        self.line_3.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_3.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_3.setObjectName("line_3")
        self.verticalLayout.addWidget(self.line_3)
        self.frame_3 = QtWidgets.QFrame(self.centralwidget)
        self.frame_3.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_3.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_3.setObjectName("frame_3")
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout(self.frame_3)
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.label_4 = QtWidgets.QLabel(self.frame_3)
        self.label_4.setObjectName("label_4")
        self.horizontalLayout_3.addWidget(self.label_4)
        self.line = QtWidgets.QFrame(self.frame_3)
        self.line.setFrameShape(QtWidgets.QFrame.VLine)
        self.line.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line.setObjectName("line")
        self.horizontalLayout_3.addWidget(self.line)
        self.CB_Default = QtWidgets.QCheckBox(self.frame_3)
        self.CB_Default.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.CB_Default.setChecked(True)
        self.CB_Default.setObjectName("CB_Default")
        self.horizontalLayout_3.addWidget(self.CB_Default)
        self.CB_GI = QtWidgets.QCheckBox(self.frame_3)
        self.CB_GI.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.CB_GI.setObjectName("CB_GI")
        self.horizontalLayout_3.addWidget(self.CB_GI)
        self.CB_Mojang = QtWidgets.QCheckBox(self.frame_3)
        self.CB_Mojang.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.CB_Mojang.setObjectName("CB_Mojang")
        self.horizontalLayout_3.addWidget(self.CB_Mojang)
        spacerItem1 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_3.addItem(spacerItem1)
        self.verticalLayout.addWidget(self.frame_3)
        self.frame_4 = QtWidgets.QFrame(self.centralwidget)
        self.frame_4.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_4.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_4.setObjectName("frame_4")
        self.horizontalLayout_4 = QtWidgets.QHBoxLayout(self.frame_4)
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        self.CB_CustomPic = QtWidgets.QCheckBox(self.frame_4)
        self.CB_CustomPic.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.CB_CustomPic.setObjectName("CB_CustomPic")
        self.horizontalLayout_4.addWidget(self.CB_CustomPic)
        self.line_4 = QtWidgets.QFrame(self.frame_4)
        self.line_4.setFrameShape(QtWidgets.QFrame.VLine)
        self.line_4.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_4.setObjectName("line_4")
        self.horizontalLayout_4.addWidget(self.line_4)
        self.LE_CustomPic = QtWidgets.QLineEdit(self.frame_4)
        self.LE_CustomPic.setEnabled(False)
        self.LE_CustomPic.setObjectName("LE_CustomPic")
        self.horizontalLayout_4.addWidget(self.LE_CustomPic)
        self.B_BCustomPic = QtWidgets.QPushButton(self.frame_4)
        self.B_BCustomPic.setEnabled(False)
        self.B_BCustomPic.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.B_BCustomPic.setObjectName("B_BCustomPic")
        self.horizontalLayout_4.addWidget(self.B_BCustomPic)
        self.verticalLayout.addWidget(self.frame_4)
        self.line_5 = QtWidgets.QFrame(self.centralwidget)
        self.line_5.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_5.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_5.setObjectName("line_5")
        self.verticalLayout.addWidget(self.line_5)
        self.frame_5 = QtWidgets.QFrame(self.centralwidget)
        self.frame_5.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_5.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_5.setObjectName("frame_5")
        self.horizontalLayout_5 = QtWidgets.QHBoxLayout(self.frame_5)
        self.horizontalLayout_5.setObjectName("horizontalLayout_5")
        self.CB_PlayMusic = QtWidgets.QCheckBox(self.frame_5)
        self.CB_PlayMusic.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.CB_PlayMusic.setObjectName("CB_PlayMusic")
        self.horizontalLayout_5.addWidget(self.CB_PlayMusic)
        self.line_7 = QtWidgets.QFrame(self.frame_5)
        self.line_7.setFrameShape(QtWidgets.QFrame.VLine)
        self.line_7.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_7.setObjectName("line_7")
        self.horizontalLayout_5.addWidget(self.line_7)
        self.LE_MusicPath = QtWidgets.QLineEdit(self.frame_5)
        self.LE_MusicPath.setEnabled(False)
        self.LE_MusicPath.setObjectName("LE_MusicPath")
        self.horizontalLayout_5.addWidget(self.LE_MusicPath)
        self.B_BMusicPath = QtWidgets.QPushButton(self.frame_5)
        self.B_BMusicPath.setEnabled(False)
        self.B_BMusicPath.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.B_BMusicPath.setObjectName("B_BMusicPath")
        self.horizontalLayout_5.addWidget(self.B_BMusicPath)
        self.verticalLayout.addWidget(self.frame_5)
        self.line_6 = QtWidgets.QFrame(self.centralwidget)
        self.line_6.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_6.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_6.setObjectName("line_6")
        self.verticalLayout.addWidget(self.line_6)
        self.B_Apply = QtWidgets.QPushButton(self.centralwidget)
        self.B_Apply.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.B_Apply.setObjectName("B_Apply")
        self.verticalLayout.addWidget(self.B_Apply)
        self.frame_6 = QtWidgets.QFrame(self.centralwidget)
        self.frame_6.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_6.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_6.setObjectName("frame_6")
        self.horizontalLayout_6 = QtWidgets.QHBoxLayout(self.frame_6)
        self.horizontalLayout_6.setObjectName("horizontalLayout_6")
        self.label_6 = QtWidgets.QLabel(self.frame_6)
        self.label_6.setObjectName("label_6")
        self.horizontalLayout_6.addWidget(self.label_6)
        self.B_Bilibili = QtWidgets.QPushButton(self.frame_6)
        self.B_Bilibili.setMinimumSize(QtCore.QSize(25, 25))
        self.B_Bilibili.setMaximumSize(QtCore.QSize(25, 25))
        self.B_Bilibili.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.B_Bilibili.setObjectName("B_Bilibili")
        self.horizontalLayout_6.addWidget(self.B_Bilibili)
        self.verticalLayout.addWidget(self.frame_6)
        self.setCentralWidget(self.centralwidget)

        self.CB_CustomPic.clicked['bool'].connect(self.LE_CustomPic.setEnabled)  # type: ignore
        self.CB_CustomPic.clicked['bool'].connect(self.B_BCustomPic.setEnabled)  # type: ignore
        self.CB_PlayMusic.clicked['bool'].connect(self.LE_MusicPath.setEnabled)  # type: ignore
        self.CB_PlayMusic.clicked['bool'].connect(self.B_BMusicPath.setEnabled)  # type: ignore

        QtCore.QMetaObject.connectSlotsByName(self)
        _translate = QtCore.QCoreApplication.translate
        self.setWindowTitle(_translate("MainWindow", "SeewoEasiNoteSplashScreenChanger By ANLIN.STUDIO"))
        self.label.setText(_translate("MainWindow", "希沃白板程序路径"))
        self.LE_ExePath.setText(_translate("MainWindow",
                                           "C:\\Program Files (x86)\\Seewo\\EasiNote5\\EasiNote5_5.2.3.1507\\Main\\EasiNote.exe"))
        self.B_BExePath.setText(_translate("MainWindow", "浏览"))
        self.label_2.setText(_translate("MainWindow", "当前启动画面背景图片"))
        self.L_P_SplashScreen.setText(_translate("MainWindow", "SplashScreen"))
        self.label_4.setText(_translate("MainWindow", "内置预设"))
        self.CB_Default.setText(_translate("MainWindow", "默认"))
        self.CB_GI.setText(_translate("MainWindow", "原神"))
        self.CB_Mojang.setText(_translate("MainWindow", "Mojang"))
        self.CB_CustomPic.setText(_translate("MainWindow", "自定义上传"))
        self.B_BCustomPic.setText(_translate("MainWindow", "浏览"))
        self.CB_PlayMusic.setText(_translate("MainWindow", "音频播放"))
        self.B_BMusicPath.setText(_translate("MainWindow", "浏览"))
        self.B_Apply.setText(_translate("MainWindow", "应用"))
        self.label_6.setText(_translate("MainWindow", "SeewoEasiNoteSplashScreenChanger By ANLIN.STUDIO Version 1.0"))
        self.B_Bilibili.setText(_translate("MainWindow", ""))

        self.NotApplied = False
        self.SplashScreenPngPath = ""

        self.setup()

    def setup(self):
        import Icon
        ANewPy.open("Icon.png").w(Icon.content, True)
        self.setWindowIcon(QIcon("Icon.png"))
        self.CB_PlayMusic.setEnabled(False)
        _ = ANewPy.open("SeewoEasiNoteSplashScreenChanger.ini")
        if _.exists():
            self.LE_ExePath.setText(_.r())
        if not os.path.exists(self.LE_ExePath.text()):
            self.LE_ExePath.setText("")
            self.BExePath()
        import bilibili
        ANewPy.open("bilibili.jpg").w(bilibili.content, True)
        self.B_Bilibili.setIcon(QIcon("bilibili.jpg"))
        self.B_Apply.setEnabled(False)

        ANewPy.pyqtpro.pyqtpro.connect(self.B_BExePath.clicked, self.BExePath)
        ANewPy.pyqtpro.pyqtpro.connect(self.LE_ExePath.textChanged, self.CheckExePath)
        ANewPy.pyqtpro.pyqtpro.connect(self.CB_Default.clicked, self.CDefault)
        ANewPy.pyqtpro.pyqtpro.connect(self.CB_GI.clicked, self.CGI)
        ANewPy.pyqtpro.pyqtpro.connect(self.CB_Mojang.clicked, self.CMojang)
        ANewPy.pyqtpro.pyqtpro.connect(self.CB_CustomPic.clicked, self.CCustomPic)
        ANewPy.pyqtpro.pyqtpro.connect(self.LE_CustomPic.textEdited, self.FlipCustomPic)
        ANewPy.pyqtpro.pyqtpro.connect(self.B_BCustomPic.clicked, self.BCustomPic)
        ANewPy.pyqtpro.pyqtpro.connect(self.B_Bilibili.clicked, self.Bilibili)
        ANewPy.pyqtpro.pyqtpro.connect(self.B_Apply.clicked, self.Apply)

        self.CheckExePath()

    @staticmethod
    def Bilibili():
        webbrowser.open("https://space.bilibili.com/481231898")

    def Apply(self):
        _ = os.path.split(self.LE_ExePath.text())[0] + "\\Assets\\SplashScreen.png"
        shutil.copyfile(self.SplashScreenPngPath, _)
        self.NotApplied = True
        self.B_Apply.setText("应用")
        self.B_Apply.setEnabled(False)

    def BExePath(self):
        _ = ANewPy.browse(True, {"应用程序": "exe"}, "EasiNote.exe", "选择希沃白板程序路径")
        if _[0]:
            if not os.path.split(_[1])[1] == "EasiNote.exe":
                win32api.MessageBox(0, "请选择 EasiNote.exe", "错误的路径！", win32con.MB_OK)
            else:
                ANewPy.open("SeewoEasiNoteSplashScreenChanger.ini").w(_[1])
                self.LE_ExePath.setText(_[1])

    def CheckExePath(self):
        _ = self.LE_ExePath.text()
        if os.path.exists(_) and os.path.split(_)[1] == "EasiNote.exe":
            self.LE_ExePath.setStyleSheet("")
            self.SplashScreenPngPath = os.path.split(_)[0] + "\\Assets\\SplashScreen.png"
        else:
            self.LE_ExePath.setStyleSheet("background-color:rgba(255, 0, 0, 50)")
            self.SplashScreenPngPath = ""
        if self.SplashScreenPngPath == "":
            self.label_2.setText(f"当前启动画面背景图片")
            _ = False
        else:
            self.label_2.setText(f"当前启动画面背景图片\n{self.SplashScreenPngPath}")
            self.C_L_P_SplashScreen(self.SplashScreenPngPath)
            _ = True
        self.CB_Default.setEnabled(_)
        self.CB_GI.setEnabled(_)
        self.CB_Mojang.setEnabled(_)
        self.CB_CustomPic.setEnabled(_)
        # self.CB_PlayMusic.setEnabled(_)

    def C_L_P_SplashScreen(self, _):
        self.SplashScreenPngPath = _
        self.L_P_SplashScreen.setPixmap(QPixmap(self.SplashScreenPngPath))
        self.L_P_SplashScreen.setScaledContents(True)

    def SetNotApplied(self):
        self.NotApplied = False
        self.B_Apply.setText("应用* (更改未保存)")
        self.B_Apply.setEnabled(True)

    def clearChoose(self):
        self.CB_Default.setChecked(False)
        self.CB_GI.setChecked(False)
        self.CB_Mojang.setChecked(False)
        self.CB_CustomPic.setChecked(False)
        self.LE_CustomPic.setEnabled(False)
        self.B_BCustomPic.setEnabled(False)

    def CDefault(self):
        self.clearChoose()
        import SplashScreenDefault
        ANewPy.open("preview.png").w(SplashScreenDefault.content, True)
        self.C_L_P_SplashScreen("preview.png")
        self.SetNotApplied()
        self.CB_Default.setChecked(True)

    def CGI(self):
        _ = False
        if self.CB_GI.isChecked():
            _ = True
        self.clearChoose()
        if _:
            self.CB_GI.setChecked(True)
            import SplashScreenGI
            ANewPy.open("preview.png").w(SplashScreenGI.content, True)
            self.C_L_P_SplashScreen("preview.png")
            self.SetNotApplied()
        else:
            self.CB_Default.setChecked(True)
            self.CDefault()

    def CMojang(self):
        _ = False
        if self.CB_Mojang.isChecked():
            _ = True
        self.clearChoose()
        if _:
            self.CB_Mojang.setChecked(True)
            import SplashScreenMojang
            ANewPy.open("preview.png").w(SplashScreenMojang.content, True)
            self.C_L_P_SplashScreen("preview.png")
            self.SetNotApplied()
        else:
            self.CB_Default.setChecked(True)
            self.CDefault()

    def CCustomPic(self):
        _ = False
        if self.CB_CustomPic.isChecked():
            _ = True
        self.clearChoose()
        if _:
            self.CB_CustomPic.setChecked(True)
            self.LE_CustomPic.setEnabled(True)
            self.B_BCustomPic.setEnabled(True)
            self.L_P_SplashScreen.setPixmap(QPixmap(""))
        else:
            self.CB_Default.setChecked(True)
            self.CDefault()

    def FlipCustomPic(self):
        _ = self.LE_CustomPic.text()
        if os.path.exists(_) and os.path.splitext(_)[1].lower() == ".png":
            self.C_L_P_SplashScreen(_)
            self.LE_CustomPic.setStyleSheet("")
        else:
            self.L_P_SplashScreen.setPixmap(QPixmap(""))
            self.LE_CustomPic.setStyleSheet("background-color:rgba(255, 0, 0, 50)")

    def BCustomPic(self):
        _ = ANewPy.browse(True, {"PNG图片文件": "png"}, title="选择启动图片")
        if _[0]:
            self.LE_CustomPic.setText(_[1])
            self.FlipCustomPic()


app = QApplication(sys.argv)
MainWindow = Ui_MainWindow()
sys.exit(app.exec_())
