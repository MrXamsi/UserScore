# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'user_score_gui.ui'
##
## Created by: Qt User Interface Compiler version 6.8.0
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
    QFont, QFontDatabase, QGradient, QIcon,
    QImage, QKeySequence, QLinearGradient, QPainter,
    QPalette, QPixmap, QRadialGradient, QTransform)
from PySide6.QtWidgets import (QAbstractSpinBox, QApplication, QComboBox, QFrame,
    QGridLayout, QHeaderView, QLabel, QLineEdit,
    QMainWindow, QPlainTextEdit, QPushButton, QRadioButton,
    QSizePolicy, QSpinBox, QTabWidget, QTableWidget,
    QTableWidgetItem, QWidget)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(406, 496)
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.gridLayout = QGridLayout(self.centralwidget)
        self.gridLayout.setObjectName(u"gridLayout")
        self.tabWidget = QTabWidget(self.centralwidget)
        self.tabWidget.setObjectName(u"tabWidget")
        sizePolicy = QSizePolicy(QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.tabWidget.sizePolicy().hasHeightForWidth())
        self.tabWidget.setSizePolicy(sizePolicy)
        self.tab_1 = QWidget()
        self.tab_1.setObjectName(u"tab_1")
        self.gridLayout_3 = QGridLayout(self.tab_1)
        self.gridLayout_3.setObjectName(u"gridLayout_3")
        self.label_user = QLabel(self.tab_1)
        self.label_user.setObjectName(u"label_user")

        self.gridLayout_3.addWidget(self.label_user, 0, 0, 1, 1)

        self.user_change = QComboBox(self.tab_1)
        self.user_change.setObjectName(u"user_change")
        self.user_change.setEditable(False)

        self.gridLayout_3.addWidget(self.user_change, 0, 1, 1, 2)

        self.label_action = QLabel(self.tab_1)
        self.label_action.setObjectName(u"label_action")

        self.gridLayout_3.addWidget(self.label_action, 1, 0, 1, 1)

        self.radio_add = QRadioButton(self.tab_1)
        self.radio_add.setObjectName(u"radio_add")
        self.radio_add.setChecked(True)

        self.gridLayout_3.addWidget(self.radio_add, 1, 1, 1, 1)

        self.radio_subtract = QRadioButton(self.tab_1)
        self.radio_subtract.setObjectName(u"radio_subtract")

        self.gridLayout_3.addWidget(self.radio_subtract, 1, 2, 1, 1)

        self.label_change_score = QLabel(self.tab_1)
        self.label_change_score.setObjectName(u"label_change_score")

        self.gridLayout_3.addWidget(self.label_change_score, 2, 0, 1, 1)

        self.change_score = QSpinBox(self.tab_1)
        self.change_score.setObjectName(u"change_score")
        self.change_score.setMinimum(-32657)
        self.change_score.setMaximum(32657)

        self.gridLayout_3.addWidget(self.change_score, 2, 1, 1, 1)

        self.label_description = QLabel(self.tab_1)
        self.label_description.setObjectName(u"label_description")
        self.label_description.setFrameShape(QFrame.Shape.NoFrame)

        self.gridLayout_3.addWidget(self.label_description, 3, 0, 1, 1)

        self.text_description = QPlainTextEdit(self.tab_1)
        self.text_description.setObjectName(u"text_description")

        self.gridLayout_3.addWidget(self.text_description, 3, 1, 1, 2)

        self.label_current_score = QLabel(self.tab_1)
        self.label_current_score.setObjectName(u"label_current_score")

        self.gridLayout_3.addWidget(self.label_current_score, 4, 0, 1, 1)

        self.dynamic_current_score = QSpinBox(self.tab_1)
        self.dynamic_current_score.setObjectName(u"dynamic_current_score")
        self.dynamic_current_score.setFrame(True)
        self.dynamic_current_score.setReadOnly(True)
        self.dynamic_current_score.setButtonSymbols(QAbstractSpinBox.ButtonSymbols.NoButtons)
        self.dynamic_current_score.setKeyboardTracking(False)
        self.dynamic_current_score.setMinimum(-32657)
        self.dynamic_current_score.setMaximum(32657)

        self.gridLayout_3.addWidget(self.dynamic_current_score, 4, 1, 1, 1)

        self.saveButton = QPushButton(self.tab_1)
        self.saveButton.setObjectName(u"saveButton")

        self.gridLayout_3.addWidget(self.saveButton, 4, 2, 1, 1)

        self.tableWidget = QTableWidget(self.tab_1)
        if (self.tableWidget.columnCount() < 5):
            self.tableWidget.setColumnCount(5)
        self.tableWidget.setObjectName(u"tableWidget")
        self.tableWidget.setRowCount(0)
        self.tableWidget.setColumnCount(5)

        self.gridLayout_3.addWidget(self.tableWidget, 5, 0, 1, 3)

        self.tabWidget.addTab(self.tab_1, "")
        self.tab_3 = QWidget()
        self.tab_3.setObjectName(u"tab_3")
        self.gridLayout_2 = QGridLayout(self.tab_3)
        self.gridLayout_2.setObjectName(u"gridLayout_2")
        self.label_user_2 = QLabel(self.tab_3)
        self.label_user_2.setObjectName(u"label_user_2")

        self.gridLayout_2.addWidget(self.label_user_2, 0, 0, 1, 1)

        self.user_edit = QLineEdit(self.tab_3)
        self.user_edit.setObjectName(u"user_edit")
        self.user_edit.setCursor(QCursor(Qt.CursorShape.SizeVerCursor))
        self.user_edit.setFocusPolicy(Qt.FocusPolicy.WheelFocus)

        self.gridLayout_2.addWidget(self.user_edit, 0, 1, 1, 2)

        self.userCreateButton = QPushButton(self.tab_3)
        self.userCreateButton.setObjectName(u"userCreateButton")

        self.gridLayout_2.addWidget(self.userCreateButton, 1, 1, 1, 1)

        self.userDeleteButton = QPushButton(self.tab_3)
        self.userDeleteButton.setObjectName(u"userDeleteButton")

        self.gridLayout_2.addWidget(self.userDeleteButton, 1, 2, 1, 1)

        self.label_warning = QLabel(self.tab_3)
        self.label_warning.setObjectName(u"label_warning")
        self.label_warning.setAutoFillBackground(False)
        self.label_warning.setTextFormat(Qt.TextFormat.AutoText)
        self.label_warning.setWordWrap(True)

        self.gridLayout_2.addWidget(self.label_warning, 2, 0, 1, 3)

        self.tabWidget.addTab(self.tab_3, "")

        self.gridLayout.addWidget(self.tabWidget, 0, 0, 1, 1)

        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)

        self.tabWidget.setCurrentIndex(0)


        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"User Points", None))
        self.label_user.setText(QCoreApplication.translate("MainWindow", u"User", None))
        self.label_action.setText(QCoreApplication.translate("MainWindow", u"Action", None))
        self.radio_add.setText(QCoreApplication.translate("MainWindow", u"Add", None))
        self.radio_subtract.setText(QCoreApplication.translate("MainWindow", u"Subtract", None))
        self.label_change_score.setText(QCoreApplication.translate("MainWindow", u"Score to change", None))
        self.label_description.setText(QCoreApplication.translate("MainWindow", u"Description", None))
        self.text_description.setDocumentTitle("")
        self.text_description.setPlainText("")
        self.label_current_score.setText(QCoreApplication.translate("MainWindow", u"Current score", None))
        self.saveButton.setText(QCoreApplication.translate("MainWindow", u"Save", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_1), QCoreApplication.translate("MainWindow", u"Change score", None))
        self.label_user_2.setText(QCoreApplication.translate("MainWindow", u"User", None))
        self.userCreateButton.setText(QCoreApplication.translate("MainWindow", u"Create", None))
        self.userDeleteButton.setText(QCoreApplication.translate("MainWindow", u"Delete", None))
        self.label_warning.setText("")
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_3), QCoreApplication.translate("MainWindow", u"Edit users", None))
    # retranslateUi

