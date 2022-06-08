from asyncio.windows_events import NULL
import sqlite3
from tabnanny import check
from PySide6.QtWidgets import *
from PySide6.QtUiTools import *
from PySide6.QtCore import *
from PySide6.QtUiTools import  QUiLoader
from functools import partial
import qdarkstyle


class ContactList(QMainWindow):
      def __init__(self ,ui):
          super().__init__()
          self.db = NULL
          self.ui = ui
          self.list = []
          self.ui.show()
          self.conn = sqlite3.connect("Contacts.db")
          self.my_cursor = self.conn.cursor()
          self.ui.remove.clicked.connect(partial(self.Remove_Contact))
          self.ui.remove_all.clicked.connect(partial(self.Remove_All_Contacts))
          self.ui.save.clicked.connect(partial(self.Add_New_Contact))
          self.LoadDB()
################################################################################################################################################
      def LoadDB(self):
            self.my_cursor.execute("SELECT * FROM Persons")
            self.db = self.my_cursor.fetchall()  
            self.Append_Data_To_Ui()
            pass
################################################################################################################################################
      def Remove_Contact(self):
            for checkstate in self.ui.findChildren(QCheckBox):
              if checkstate.isChecked() and checkstate.text() != 'Dark Mode' :
                checkstate.setParent(None)
                self.my_cursor.execute(f"DELETE FROM Persons WHERE name ='{checkstate.text().split()[0]}';")
                self.conn.commit()   
################################################################################################################################################
      def Remove_All_Contacts(self):
            for checkstate in self.ui.findChildren(QCheckBox):
                 checkstate.setParent(None)
            self.db = NULL
            self.my_cursor.execute(f"DELETE FROM Persons;")
            self.conn.commit()        
################################################################################################################################################
      def Add_New_Contact(self):
          if self.ui.name.text() != '' or self.ui.family.text() !='' or self.ui.mobile.text() !='' or self.ui.phone.text() !='' or self.ui.email.text() !='':
            self.my_cursor.execute(f"INSERT INTO Persons (name,family,mobile_number,phone_number,email)VALUES ('{self.ui.name.text()}', '{self.ui.family.text()}', '{self.ui.mobile.text()}','{self.ui.phone.text()}','{self.ui.email.text()}');")
            self.conn.commit()
            checkbox = QCheckBox()
            checkbox.setText(self.ui.name.text()+" |  " + self.ui.family.text()+" |  " + self.ui.mobile.text()+" |  " + self.ui.phone.text()+" |  " +self.ui.email.text()  )
            self.ui.verticalLayout_5.addWidget(checkbox)
            self.ui.name.setText("")
            self.ui.family.setText("")
            self.ui.mobile.setText("")
            self.ui.phone.setText("")
            self.ui.email.setText("")
################################################################################################################################################     
      def Append_Data_To_Ui(self):
          for i in range(0,len(self.db)):
              checkbox = QCheckBox(f"checkbox_{i}")
              checkbox.setText(self.db[i][1]+" |  " + self.db[i][2]+" |  " + self.db[i][3]+" |  " + self.db[i][4]+" |  " +self.db[i][5]  )
              self.ui.verticalLayout_5.addWidget(checkbox)
################################################################################################################################################
app = QApplication()
app.setStyleSheet(qdarkstyle.load_stylesheet())
loader = QUiLoader()
ui = loader.load("UI.ui")
################################################################################################################################################
def change_theme():
    if ui.checkBox.isChecked():
      app.setStyleSheet(qdarkstyle.load_stylesheet())
    else:
      app.setStyleSheet(None)
################################################################################################################################################
ui.checkBox.clicked.connect(partial(change_theme))
contactlist = ContactList(ui)
app.exec()