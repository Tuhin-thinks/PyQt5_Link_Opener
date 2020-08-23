import webbrowser
import re
from functools import partial
import sys
from Package import main_window
from PyQt5.QtWidgets import QMainWindow, QApplication
import browserhistory as bh
from PyQt5.QtCore import QThread, pyqtSignal
from Package import app_background
import csv as cv

class browserHistory(QThread):
    makebutton_active = pyqtSignal(list)
    def __init__(self):
        super().__init__()

    def run(self):
        # dict_obj = bh.get_browserhistory()
        bh.write_browserhistory_csv()
        self.parse_csv("chrome_history.csv")
        # self.makebutton_active.emit("active")
    def parse_csv(self, file_name):
        pattern = "https://(.+?)/"  # used a ? to make the search non greedy
        domain_list = []
        with open(file_name,'r',encoding="ISO-8859-1") as file_01:
            # print("Starting to read ")
            try:
                csvreader = cv.reader(file_01)
                for site in csvreader:
                    # print(site[0])
                    match_object = re.search(pattern,site[0])
                    try:
                        domain_name = match_object.group()
                        # print("Got match adding to domain..")

                        if domain_name not in domain_list:
                            domain_list.append(domain_name)
                            # print(domain_name)
                    except AttributeError:
                        # print("no match found...")
                        pass
            except Exception as e:
                print("Cannot read lines from data File",e)
                pass
        # print(f"Found {len(domain_list)} different domain names in your browsing history...")
        self.makebutton_active.emit(domain_list)




class MyApplication(QMainWindow):
    def __init__(self):
        super(MyApplication, self).__init__()
        self.ui = main_window.Ui_MainWindow()
        self.ui.setupUi(self)
        self.ui.window_obj.setWindowTitle("..::HyperLink::..")
        self.ui.button_add.clicked.connect(self.getBrowserHistory)
        self.ui.button_close.clicked.connect(self.close_app)
        self.ui.links_list.itemClicked.connect(self.listwidgetclicked)

    def getBrowserHistory(self):
        self.browserhistory = browserHistory()
        # print("Getting browser history...")
        self.ui.button_add.setDisabled(True)
        self.browserhistory.makebutton_active.connect(self.buttonactive)
        self.browserhistory.start()

    def buttonactive(self,domain_list):
        # print("done")
        self.ui.button_add.setEnabled(True)
        # add the domains to the listwidget
        for domain in domain_list:
            self.ui.links_list.addItem(domain)
    def close_app(self):

        if self.ui.button_add.isEnabled()==True:
            self.close()
        else:
            pass
            # print("Cannot Close app... running a task")
    def listwidgetclicked(self, item):
        # browser = webbrowser.get('chrome')
        webbrowser.open_new_tab(item.text())




if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MyApplication()
    window.show()
    sys.exit(app.exec_())
