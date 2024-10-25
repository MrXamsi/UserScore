import sys
import psycopg2
import configparser
from PySide6 import QtCore, QtGui
from PySide6.QtWidgets import QApplication, QMainWindow, QTableWidgetItem
from psycopg2 import OperationalError
from ui_main import Ui_MainWindow


class MainWindow(QMainWindow):

    def __init__(self):
        super(MainWindow, self).__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.setWindowIcon(QtGui.QIcon('icon.ico'))
        self.db = self.db_coonect()
        self.user_combo_box()
        self.user_change()
        self.ui.userCreateButton.clicked.connect(self.create_user)
        self.ui.userDeleteButton.clicked.connect(self.delete_user)
        self.ui.user_change.activated.connect(self.user_change)
        self.ui.saveButton.clicked.connect(self.save_score_change)

    def db_coonect(self):
        connection = None
        try:
            config = configparser.ConfigParser()
            config.read('settings.ini')
            connection = psycopg2.connect(database = config['PostgreSQL']['dbname'],
                                          user = config['PostgreSQL']['user'],
                                          password = config['PostgreSQL']['password'],
                                          host = config['PostgreSQL']['host'],
                                          port = config['PostgreSQL']['port'],)
            connection.autocommit = True
            print("Connection to PostgreSQL DB successful")
        except OperationalError as e:
            print(f"The error '{e}' occurred")
        return connection

    def user_combo_box(self,clearComboBox=False):
        if clearComboBox:
            self.ui.user_change.clear()
            self.ui.tableWidget.clear()
        cursor = self.db.cursor()
        cursor.execute(""" SELECT "user" FROM users_scores ORDER BY user""")
        table_user = cursor.fetchall()
        for el in table_user:
            self.ui.user_change.addItem(el[0])

    @QtCore.Slot()
    def create_user(self):
        try:
            insert_query = """ INSERT INTO users_scores ("user", score) VALUES (%s, DEFAULT)"""
            cursor = self.db.cursor()
            cursor.execute(insert_query, [self.ui.user_edit.text()])
            self.user_combo_box(True)
        except Exception as e:
            self.ui.label_warning.setText(str(e))

    @QtCore.Slot()
    def delete_user(self):
        try:
            insert_query = """ DELETE FROM users_scores WHERE "user"=(%s)"""
            cursor = self.db.cursor()
            cursor.execute(insert_query, [self.ui.user_edit.text()])
            self.user_combo_box(True)
        except Exception as e:
            self.ui.label_warning.setText(str(e))

    @QtCore.Slot()
    def user_change(self):
        insert_query = """ SELECT score FROM users_scores WHERE "user"=(%s)"""
        cursor = self.db.cursor()
        cursor.execute(insert_query, [self.ui.user_change.currentText()])
        user = cursor.fetchone()

        if user is not None:
            self.ui.dynamic_current_score.setValue(user[0])
            #History table
            self.ui.tableWidget.setHorizontalHeaderLabels(['Date and time', 'Description', 'Add', 'Score to change', 'Sum'])
            insert_query = """ SELECT create_date, description, summation, value_change, new_value FROM history_score WHERE "h_user"=(%s) ORDER BY create_date"""
            cursor = self.db.cursor()
            cursor.execute(insert_query, [self.ui.user_change.currentText()])
            historyTable = cursor.fetchall()
            y = 0
            self.ui.tableWidget.setRowCount(len(historyTable))
            for el in historyTable:
                self.ui.tableWidget.setItem(y, 0, QTableWidgetItem(str(el[0])))
                self.ui.tableWidget.setItem(y, 1, QTableWidgetItem(str(el[1])))
                self.ui.tableWidget.setItem(y, 2, QTableWidgetItem(str(el[2])))
                self.ui.tableWidget.setItem(y, 3, QTableWidgetItem(str(el[3])))
                self.ui.tableWidget.setItem(y, 4, QTableWidgetItem(str(el[4])))
                y += 1
            self.ui.tableWidget.resizeColumnsToContents()


    @QtCore.Slot()
    def save_score_change(self):
        user_change = (self.ui.change_score.value(), self.ui.user_change.currentText())

        if self.ui.radio_add.isChecked() and self.ui.change_score.value() > 0:
            insert_query_for_user_score = """ UPDATE users_scores SET score = score + (%s) WHERE "user"=(%s)"""
            user_change_for_histrory = (self.ui.user_change.currentText(), 
                                        self.ui.text_description.toPlainText(), 
                                        True, self.ui.change_score.value(), 
                                        self.ui.dynamic_current_score.value() + self.ui.change_score.value())
        elif self.ui.radio_subtract.isChecked() and self.ui.change_score.value() > 0:
            insert_query_for_user_score = """ UPDATE users_scores SET score = score - (%s) WHERE "user"=(%s)"""
            user_change_for_histrory = (self.ui.user_change.currentText(),
                                        self.ui.text_description.toPlainText(), 
                                        False, self.ui.change_score.value(), 
                                        self.ui.dynamic_current_score.value() - self.ui.change_score.value())
        else:
            self.ui.text_description.setPlainText('The number of changeable score is not set')
            return
        
        self.ui.text_description.clear()
        cursor = self.db.cursor()
        cursor.execute(insert_query_for_user_score, user_change)
        insert_query_for_history_score = """ INSERT INTO history_score (h_user, description, summation, value_change, new_value) VALUES (%s,%s,%s,%s,%s)"""
        cursor.execute(insert_query_for_history_score, user_change_for_histrory)
        self.user_change()


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()

    sys.exit(app.exec())