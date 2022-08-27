# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'gui.ui'
#
# Created by: PyQt5 UI code generator 5.11.3
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtGui import QTextCursor
from os import getcwd
from os import path
from os import startfile
import threading

cd = getcwd()

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1105, 637)
        icon = QtGui.QIcon()
        icon_d = (cd) + "/resources/images/icon.png"
        print(icon_d)
        icon.addPixmap(QtGui.QPixmap(icon_d), QtGui.QIcon.Normal, QtGui.QIcon.Off)
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
        self.activity_log.setFocus()
        self.activity_log.ensureCursorVisible()
        self.pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton.setGeometry(QtCore.QRect(530, 540, 100, 30))
        self.pushButton.clicked.connect(self.pass_to_collect_data)
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
        self.browser_country_code.clicked.connect(self.pass_to_open_cc_file)
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
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">D:/invitation_card.png</p></body></html>"))
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
        
    def pass_to_collect_data(self):
        self.fail_names.clear()
        self.fail_numbers.clear()
        cd = threading.Thread(target = lambda:collect_data(self))
        cd.start()
    
    def pass_to_open_cc_file(self):
        ocf = threading.Thread(target = lambda:open_cc_file(self))
        ocf.start()
        
    def pass_to_send_invites(self):
        global send
        si = threading.Thread(target = lambda:send_invites(self))
        si.start()
        
    def log(self,log_data):
        from time import sleep
        sleep(0.2)
        self.activity_log.moveCursor(QTextCursor.End)
        self.activity_log.append(log_data)
        self.activity_log.ensureCursorVisible()



def send_invites(self):
    self.log("[#] importing modules")
    try:
        from selenium import webdriver
        from selenium.webdriver.chrome.options import Options
        from selenium.webdriver.support.ui import WebDriverWait
        from selenium.webdriver.support import expected_conditions as EC
        from selenium.webdriver.common.by import By
        from webdriver_manager.chrome import ChromeDriverManager
        from webdriver_manager.firefox import GeckoDriverManager
        from webdriver_manager.microsoft import EdgeChromiumDriverManager
        from urllib.parse import quote
        from requests import get
        from time import strftime
        from time import sleep
        from pyautogui import alert
        from pyautogui import hotkey
        from pyautogui import keyDown
        from pyautogui import click
        from pyautogui import moveTo
        from pyautogui import size
    except Exception as e:
        self.log("[!!!] ERROR occured during importing modules")
        self.log("[!!!] ERROR : " + str(e))
    self.log("[#] downloading XPATHS")
    try:
        menu_xpath_url = "https://raw.githubusercontent.com/akhilrajs/bulk-inviter-BOT/main/resources/xpaths/menu.txt"
        click_btn_xpath_url = "https://raw.githubusercontent.com/akhilrajs/bulk-inviter-BOT/main/resources/xpaths/click_btn.txt"
        crop_xpath_url = "https://raw.githubusercontent.com/akhilrajs/bulk-inviter-BOT/main/resources/xpaths/crop.txt"
        data_menu_xpath = get(menu_xpath_url)
        data_click_btn_xpath = get(click_btn_xpath_url)
        data_crop_xpath = get(crop_xpath_url)
        menu_xpath = data_menu_xpath.text
        click_btn_xpath = data_click_btn_xpath.text
        crop_xpath = data_crop_xpath.text
        self.log("[#] XPATHS downloaded")
    except Exception as e:
        self.log("[!!!] ERROR while downloading xpaths ")
        self.log("[!!!] ERROR : " + str(e))
    greet = ""
    currentTime = int(strftime('%H'))
    if currentTime < 12 :
        greet = "Good Morning "
    if 12 < currentTime < 18 :
        greet = "Good Afternoon "
    if currentTime > 18 :
        greet = "Good Evening "
    self.log("[#] greet : " + str(greet))
    self.log("[#] loading Options for Google-Chrome")
    try:
        options = Options()
        options.add_experimental_option("excludeSwitches", ["enable-logging"])
        options.add_argument("--profile-directory=Default")
        options_d = cd + "/resources/User/Data/Default"
        options.add_argument("--user-data-dir=" + str(options_d))
        self.log("[#] opening Google-Chrome")
        driver = webdriver.Chrome(ChromeDriverManager().install(),chrome_options=options)
    except ValueError:
        self.log("[!!!] ERROR : Google-Chrome not installed in the system")
        self.log("[#] opening Mozilla Firefoz")
        driver = webdriver.Firefox(executable_path=GeckoDriverManager().install())
    except ValueError:
        self.log("[!!!] ERROR : Mozilla Firefoz not installed in the system")
        self.log("[#] opening Microsoft Edge")
        driver = webdriver.Edge(EdgeChromiumDriverManager().install())
    self.log("[#] If not logged into Whatsapp, Login by scaning QR code")
    driver.get('https://web.whatsapp.com')
    delay = 60
    try:
        menu = WebDriverWait(driver, delay).until(EC.element_to_be_clickable((By.XPATH, menu_xpath))) 
        self.log("[#] logged into Whatsapp")
        self.log("[##=>] DO NOT USE THE MOUSE OR KEYBOARD !!!")
    except Exception as e:
        self.log("[!!!] ERROR while logging into Whatsapp")
        self.log("[!!!] The system may not be connected to the Internet")
        self.log("[!!!] try again")
        sys.exit(app.exec_())
    failed_list = []
    startfile(cd + "/resources/file")
    sleep(2)
    hotkey('ctrl', 'a')
    hotkey('ctrl', 'c')
    hotkey('alt', 'f4')
    sleep(5)
    hotkey('win','left')                   
    x,y = size()
    x,y=int(str(x)),int(str(y))
    l1 = (695/1920)*x
    b1 = (986/1080)*y
    moveTo(l1,b1)
    click()
    sleep(2)
    for idx, number in enumerate(nums):
        number = number.strip()
        if number =="":
            continue
        self.log('[#>]  {}/{} => Sending message to {}.'.format((idx+1), total_numbers, number))
        try:
            msg = ""
            msg = greet + str(names[idx]).title() + '''
            
            ''' + str(cap)
            url = 'https://web.whatsapp.com/send?phone='+ cc + number + '&text=' + msg
            sleep(2)
            send = False
            for i in range(3):
                if send != True:
                    driver.get(url)
                    try:
                        click_btn = WebDriverWait(driver, delay).until(EC.element_to_be_clickable((By.XPATH, click_btn_xpath)))
                    except Exception as e :
                        self.log(f"\nFailed to send message to: {number}, retry ({i+1}/3)")
                        self.log("[#] Make sure your computer is connected to the Internet")
                        self.log("[#] ERROR : " +  str(e))
                        failed_list.append(number)
                    else:
                        x,y = size()
                        x,y=int(str(x)),int(str(y))
                        l1 = (695/1920)*x
                        b1 = (986/1080)*y
                        moveTo(l1,b1)
                        sleep(2)
                        click()
                        hotkey('ctrl','v')
                        sleep(2)
                        crop =  WebDriverWait(driver, delay).until(EC.element_to_be_clickable((By.XPATH, crop_xpath)))
                        keyDown("enter")
                        sleep(0.2)
                        sleep(1)
                        send=True
                        sleep(3)
                        self.log("[#] " + 'Message sent to: ' + number + " " + names[idx].title())
        except Exception as e :
            self.log('Failed to send message to ' + number + str(e) )
            failed_list.append(number)
    fail_numbers = []
    for i in failed_list:
        if i in fail_numbers:
            i =""
        else:
            fail_numbers.append(i)
    fail_names = []
    for number in fail_numbers:
        idx = nums.index(number)
        name = names[idx]
        fail_names.append(name)
    for n in fail_names:
        self.fail_names.append(n)
        idx = int(fail_names.index(n))
        number = fail_numbers[idx]
        self.fail_numbers.append(number)
    self.log("[##] closing browser in 10 seconds")
    sleep(10)
    driver.close()

def collect_data(self):
    global cc, cap
    cc = str(self.country_code.text())
    self.log("[#] country code : " + str(cc))
    cap = str(self.caption.toPlainText())
    self.log("[#] caption : " + str(cap))
    global nums, names, total_names, total_numbers, file_d
    nums = []
    names = []
    nums = (self.phone_numbers.toPlainText().splitlines())
    self.log("[#] phone number list loaded")
    total_numbers = len(nums)
    self.log("[#] total numbers : " + str(total_numbers))
    names = (self.names.toPlainText().splitlines())
    self.log("[#] name list loaded ")
    total_names = len(names)
    if total_names != total_numbers:
        self.log("[!!!] the total number of names and numbers do not match")
        self.log("[!!!] check the names and numbers and try again")
        sys.exit(app.exec_())
    self.log("[#] total names : " + str(total_names))
    file_d = self.file_location.toPlainText()
    if not path.exists(file_d):
        self.log("[!!!] invitation file location invalid")
        self.log("[!!!] enter the location and try again")
        sys.exit(app.exec_())
    self.log("[#] invitation file loaded")
    from os import remove
    from os import listdir
    folder = cd + "/resources/file/"
    files = listdir(folder)
    for file in files:
        remove(str(folder) + str(file))
        self.log("[#] old files cleared ...")
    try:
        self.log("[#] importing shutil module")
        from shutil import copy
        source = file_d
        destination = str(cd) + "/resources/file/"
        copy(source,destination)
        self.log("[#] file copied to /resources/file/")
    except Exception as e :
        self.log("[!!!] ERROR while copying the invitation file")
        self.log("[!!!] check the address of the file and try again")
        sys.exit(app.exec_())
    self.pass_to_send_invites()
    
    
def open_cc_file(self):
    self.log("[#] opening country codes Excel spreadsheet")
    ocf_d = cd + "/resources/country_codes.xlsx"
    startfile(ocf_d)


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())

