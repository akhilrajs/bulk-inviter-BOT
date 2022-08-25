# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'gui.ui'
#
# Created by: PyQt5 UI code generator 5.11.3
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1105, 637)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("../resources/images/icon.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        MainWindow.setWindowIcon(icon)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.phone_numbers = QtWidgets.QTextEdit(self.centralwidget)
        self.phone_numbers.setGeometry(QtCore.QRect(30, 200, 111, 250))
        self.phone_numbers.setStyleSheet("")
        self.phone_numbers.setObjectName("phone_numbers")
        self.phone_numbers_label = QtWidgets.QLabel(self.centralwidget)
        self.phone_numbers_label.setGeometry(QtCore.QRect(30, 180, 100, 16))
        self.phone_numbers_label.setObjectName("phone_numbers_label")
        self.country_code_label = QtWidgets.QLabel(self.centralwidget)
        self.country_code_label.setGeometry(QtCore.QRect(30, 20, 90, 20))
        self.country_code_label.setObjectName("country_code_label")
        self.country_code = QtWidgets.QLineEdit(self.centralwidget)
        self.country_code.setGeometry(QtCore.QRect(120, 20, 113, 20))
        self.country_code.setObjectName("country_code")
        self.line = QtWidgets.QFrame(self.centralwidget)
        self.line.setGeometry(QtCore.QRect(660, 0, 3, 620))
        self.line.setFrameShape(QtWidgets.QFrame.VLine)
        self.line.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line.setObjectName("line")
        self.caption_label = QtWidgets.QLabel(self.centralwidget)
        self.caption_label.setGeometry(QtCore.QRect(30, 50, 90, 20))
        self.caption_label.setObjectName("caption_label")
        self.caption = QtWidgets.QPlainTextEdit(self.centralwidget)
        self.caption.setGeometry(QtCore.QRect(120, 50, 511, 71))
        self.caption.setObjectName("caption")
        self.names_label = QtWidgets.QLabel(self.centralwidget)
        self.names_label.setGeometry(QtCore.QRect(160, 180, 55, 16))
        self.names_label.setObjectName("names_label")
        self.names = QtWidgets.QTextEdit(self.centralwidget)
        self.names.setGeometry(QtCore.QRect(160, 200, 151, 250))
        self.names.setStyleSheet("")
        self.names.setObjectName("names")
        self.line_2 = QtWidgets.QFrame(self.centralwidget)
        self.line_2.setGeometry(QtCore.QRect(0, 140, 660, 3))
        self.line_2.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_2.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_2.setObjectName("line_2")
        self.file_location_label = QtWidgets.QLabel(self.centralwidget)
        self.file_location_label.setGeometry(QtCore.QRect(30, 470, 140, 30))
        self.file_location_label.setObjectName("file_location_label")
        self.line_3 = QtWidgets.QFrame(self.centralwidget)
        self.line_3.setGeometry(QtCore.QRect(320, 160, 3, 290))
        self.line_3.setFrameShape(QtWidgets.QFrame.VLine)
        self.line_3.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_3.setObjectName("line_3")
        self.file_location = QtWidgets.QTextEdit(self.centralwidget)
        self.file_location.setGeometry(QtCore.QRect(170, 470, 450, 30))
        self.file_location.setObjectName("file_location")
        self.activity_log = QtWidgets.QTextBrowser(self.centralwidget)
        self.activity_log.setGeometry(QtCore.QRect(670, 20, 421, 551))
        self.activity_log.setStyleSheet("background-color : rgb(255, 255, 222)")
        self.activity_log.setObjectName("activity_log")
        self.pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton.setGeometry(QtCore.QRect(530, 540, 100, 30))
        font = QtGui.QFont()
        font.setFamily("Mukta Malar ExtraBold")
        font.setPointSize(9)
        font.setBold(True)
        font.setWeight(75)
        self.pushButton.setFont(font)
        self.pushButton.setObjectName("pushButton")
        self.failed_list_label = QtWidgets.QLabel(self.centralwidget)
        self.failed_list_label.setGeometry(QtCore.QRect(330, 160, 110, 20))
        self.failed_list_label.setObjectName("failed_list_label")
        self.failed_list_name_label = QtWidgets.QLabel(self.centralwidget)
        self.failed_list_name_label.setGeometry(QtCore.QRect(330, 180, 55, 20))
        self.failed_list_name_label.setObjectName("failed_list_name_label")
        self.failed_number_list_label = QtWidgets.QLabel(self.centralwidget)
        self.failed_number_list_label.setGeometry(QtCore.QRect(530, 180, 55, 20))
        self.failed_number_list_label.setObjectName("failed_number_list_label")
        self.enter_the_details_below_label = QtWidgets.QLabel(self.centralwidget)
        self.enter_the_details_below_label.setGeometry(QtCore.QRect(30, 150, 140, 30))
        self.enter_the_details_below_label.setObjectName("enter_the_details_below_label")
        self.fail_names = QtWidgets.QTextBrowser(self.centralwidget)
        self.fail_names.setGeometry(QtCore.QRect(330, 200, 180, 250))
        self.fail_names.setObjectName("fail_names")
        self.fail_numbers = QtWidgets.QTextBrowser(self.centralwidget)
        self.fail_numbers.setGeometry(QtCore.QRect(530, 200, 111, 250))
        self.fail_numbers.setObjectName("fail_numbers")
        self.browser_country_code = QtWidgets.QPushButton(self.centralwidget)
        self.browser_country_code.setGeometry(QtCore.QRect(240, 19, 30, 21))
        self.browser_country_code.setObjectName("browser_country_code")
        self.help = QtWidgets.QPushButton(self.centralwidget)
        self.help.setGeometry(QtCore.QRect(20, 550, 93, 28))
        self.help.setObjectName("help")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 1105, 26))
        self.menubar.setObjectName("menubar")
        self.menuBOT = QtWidgets.QMenu(self.menubar)
        self.menuBOT.setObjectName("menuBOT")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.menubar.addAction(self.menuBOT.menuAction())

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Bulk Inviter"))
        self.phone_numbers.setHtml(_translate("MainWindow", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'MS Shell Dlg 2\'; font-size:7.8pt; font-weight:400; font-style:normal;\">\n"
"<p align=\"center\" style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p></body></html>"))
        self.phone_numbers_label.setText(_translate("MainWindow", "Phone Numbers"))
        self.country_code_label.setText(_translate("MainWindow", "Country Code :"))
        self.country_code.setText(_translate("MainWindow", "+91"))
        self.caption_label.setText(_translate("MainWindow", "Caption : "))
        self.caption.setPlainText(_translate("MainWindow", "type your caption here ..."))
        self.names_label.setText(_translate("MainWindow", "Names"))
        self.names.setHtml(_translate("MainWindow", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'MS Shell Dlg 2\'; font-size:7.8pt; font-weight:400; font-style:normal;\">\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p></body></html>"))
        self.file_location_label.setText(_translate("MainWindow", "Invitation File Location :"))
        self.file_location.setHtml(_translate("MainWindow", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'MS Shell Dlg 2\'; font-size:7.8pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">file:///D:/invitation_card.png</p></body></html>"))
        self.activity_log.setHtml(_translate("MainWindow", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'MS Shell Dlg 2\'; font-size:7.8pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:9pt;\">[#] activity log ...</span></p></body></html>"))
        self.pushButton.setText(_translate("MainWindow", "SEND"))
        self.failed_list_label.setText(_translate("MainWindow", "failed to send to :"))
        self.failed_list_name_label.setText(_translate("MainWindow", "name"))
        self.failed_number_list_label.setText(_translate("MainWindow", "number"))
        self.enter_the_details_below_label.setText(_translate("MainWindow", "Enter the details below"))
        self.fail_names.setHtml(_translate("MainWindow", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'MS Shell Dlg 2\'; font-size:7.8pt; font-weight:400; font-style:normal;\">\n"
"<p align=\"center\" style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p></body></html>"))
        self.fail_numbers.setHtml(_translate("MainWindow", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'MS Shell Dlg 2\'; font-size:7.8pt; font-weight:400; font-style:normal;\">\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p></body></html>"))
        self.browser_country_code.setText(_translate("MainWindow", "..."))
        self.help.setText(_translate("MainWindow", "HELP"))
        self.menuBOT.setTitle(_translate("MainWindow", "Author : Akhil Raj S"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())

