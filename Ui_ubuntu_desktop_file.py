# -*- Coding: utf-8 -*-
# Created by Diablo76 on 04/01/2024 -- 00:44:10.
# Copyright © 2024 Diablo76. All rights reserved.

from PyQt5 import QtCore, QtGui, QtWidgets

__version__ = "1.0.5"


class UiUbuntuDesktopFile(QtWidgets.QMainWindow):
    def __init__(self) -> None:
        super().__init__()
        button_icon = QtGui.QIcon("Assets/Images/loupe.png")
        button_categories = QtGui.QIcon("Assets/Images/directory_icon.png")
        self.setFixedSize(822, 355)
        self.setWindowIcon(QtGui.QIcon("Assets/Images/Ubuntu_icon.png"))
        self.gridLayoutWidget = QtWidgets.QWidget(self)
        self.gridLayoutWidget.setGeometry(QtCore.QRect(8, 8, 806, 305))
        self.gridLayout = QtWidgets.QGridLayout(self.gridLayoutWidget)
        # Widgets Name
        self.label_name = QtWidgets.QLabel(self.gridLayoutWidget)
        self.gridLayout.addWidget(self.label_name, 0, 0, 1, 1)
        self.lineEdit_name = QtWidgets.QLineEdit(self.gridLayoutWidget)
        self.lineEdit_name.setClearButtonEnabled(True)
        self.gridLayout.addWidget(self.lineEdit_name, 0, 2, 1, 1)
        # Widgets Generic Name
        self.label_generic_name = QtWidgets.QLabel(self.gridLayoutWidget)
        self.gridLayout.addWidget(self.label_generic_name, 1, 0, 1, 1)
        self.lineEdit_generic_name = QtWidgets.QLineEdit(self.gridLayoutWidget)
        self.lineEdit_generic_name.setClearButtonEnabled(True)
        self.gridLayout.addWidget(self.lineEdit_generic_name, 1, 2, 1, 1)
        # Widgets Comment
        self.label_comment = QtWidgets.QLabel(self.gridLayoutWidget)
        self.gridLayout.addWidget(self.label_comment, 2, 0, 1, 1)
        self.lineEdit_comment = QtWidgets.QLineEdit(self.gridLayoutWidget)
        self.lineEdit_comment.setClearButtonEnabled(True)
        self.gridLayout.addWidget(self.lineEdit_comment, 2, 2, 1, 1)
        # Widgets Exec
        self.label_exec = QtWidgets.QLabel(self.gridLayoutWidget)
        self.gridLayout.addWidget(self.label_exec, 3, 0, 1, 1)
        self.lineEdit_exec = QtWidgets.QLineEdit(self.gridLayoutWidget)
        self.lineEdit_exec.setReadOnly(True)
        self.gridLayout.addWidget(self.lineEdit_exec, 3, 2, 1, 1)
        self.pushButton_exec = QtWidgets.QPushButton(self.gridLayoutWidget)
        self.pushButton_exec.setIcon(button_icon)
        self.pushButton_exec.setMaximumSize(40, 25)
        self.gridLayout.addWidget(self.pushButton_exec, 3, 3, 1, 1)
        # Widgets Icon
        self.label_icon = QtWidgets.QLabel(self.gridLayoutWidget)
        self.gridLayout.addWidget(self.label_icon, 4, 0, 1, 1)
        self.lineEdit_icon = QtWidgets.QLineEdit(self.gridLayoutWidget)
        self.lineEdit_icon.setReadOnly(True)
        self.gridLayout.addWidget(self.lineEdit_icon, 4, 2, 1, 1)
        self.pushButton_icon = QtWidgets.QPushButton(self.gridLayoutWidget)
        self.pushButton_icon.setIcon(button_icon)
        self.pushButton_icon.setMaximumSize(40, 25)
        self.gridLayout.addWidget(self.pushButton_icon, 4, 3, 1, 1)
        # Widgets Type
        self.label_type = QtWidgets.QLabel(self.gridLayoutWidget)
        self.gridLayout.addWidget(self.label_type, 5, 0, 1, 1)
        self.lineEdit_type = QtWidgets.QLineEdit(self.gridLayoutWidget)
        self.lineEdit_type.setReadOnly(True)
        self.gridLayout.addWidget(self.lineEdit_type, 5, 2, 1, 1)
        # Widgets Version
        self.label_version = QtWidgets.QLabel(self.gridLayoutWidget)
        self.gridLayout.addWidget(self.label_version, 6, 0, 1, 1)
        self.lineEdit_version = QtWidgets.QLineEdit(self.gridLayoutWidget)
        self.lineEdit_version.setClearButtonEnabled(True)
        self.gridLayout.addWidget(self.lineEdit_version, 6, 2, 1, 1)
        # Widgets Categories
        self.label_categories = QtWidgets.QLabel(self.gridLayoutWidget)
        self.gridLayout.addWidget(self.label_categories, 7, 0, 1, 1)
        self.lineEdit_categories = QtWidgets.QLineEdit(self.gridLayoutWidget)
        self.lineEdit_categories.setReadOnly(True)
        self.gridLayout.addWidget(self.lineEdit_categories, 7, 2, 1, 1)
        self.pushButton_categories = QtWidgets.QPushButton(self.gridLayoutWidget)
        self.pushButton_categories.setIcon(button_categories)
        self.pushButton_categories.setMaximumSize(40, 25)
        self.gridLayout.addWidget(self.pushButton_categories, 7, 3, 1, 1)
        # Widgets Teminal
        self.label_terminal = QtWidgets.QLabel(self.gridLayoutWidget)
        self.gridLayout.addWidget(self.label_terminal, 8, 0, 1, 1)
        self.checkBox_terminal = QtWidgets.QCheckBox(self.gridLayoutWidget)
        self.checkBox_terminal.setStyleSheet("color: gray")
        self.checkBox_terminal.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.gridLayout.addWidget(self.checkBox_terminal, 8, 2, 1, 1)
        # Widgets Directory
        self.label_directory = QtWidgets.QLabel(self.gridLayoutWidget)
        self.gridLayout.addWidget(self.label_directory, 9, 0, 1, 1)
        self.checkBox_directory = QtWidgets.QCheckBox(self.gridLayoutWidget)
        self.checkBox_directory.setStyleSheet("color: gray")
        self.checkBox_directory.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.gridLayout.addWidget(self.checkBox_directory, 9, 2, 1, 1)
        # Widgets Startup
        self.label_startup = QtWidgets.QLabel(self.gridLayoutWidget)
        self.gridLayout.addWidget(self.label_startup, 10, 0, 1, 1)
        self.checkBox_startup = QtWidgets.QCheckBox(self.gridLayoutWidget)
        self.checkBox_startup.setStyleSheet("color: gray")
        self.checkBox_startup.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.gridLayout.addWidget(self.checkBox_startup, 10, 2, 1, 1)
        # Widget Python
        self.label_python = QtWidgets.QLabel(self.gridLayoutWidget)
        self.gridLayout.addWidget(self.label_python, 11, 0, 1, 1)
        self.checkBox_python = QtWidgets.QCheckBox(self.gridLayoutWidget)
        self.checkBox_python.setStyleSheet("color: gray")
        self.checkBox_python.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.gridLayout.addWidget(self.checkBox_python, 11, 2, 1, 1)
        # Widget Label_icon
        self.label_icon_application = QtWidgets.QLabel(self)
        self.label_icon_application.setGeometry(QtCore.QRect(int((self.width()/2)-34), 224, 68, 68))
        self.label_icon_application.setScaledContents(True)
        # Widget Save
        self.pushButton_save = QtWidgets.QPushButton(self)
        self.pushButton_save.setGeometry(
            QtCore.QRect(int((self.width() / 2) - 34), 312, 68, 32)
        )
        # Widget Quit
        self.pushButton_quit = QtWidgets.QPushButton(self)
        self.pushButton_quit.setGeometry(QtCore.QRect(738, 312, 68, 32))
        # Translate
        self.retranslateUi()

    def retranslateUi(self):
        self.setWindowTitle(f"Ubuntu Desktop File {__version__}")
        self.label_version.setText("Version :")
        self.label_generic_name.setText("Generic Name :")
        self.label_name.setText("Application Name :")
        self.label_type.setText("Type :")
        self.label_exec.setText("Exec :")
        self.label_icon.setText("Icon :")
        self.label_comment.setText("Comment :")
        self.label_categories.setText("Categories :")
        self.label_directory.setText("Path directory :")
        self.label_startup.setText("Startup Notify :")
        self.label_terminal.setText("Terminal :")
        self.label_python.setText("Launch with Python :")
        self.pushButton_save.setText("Save")
        self.pushButton_quit.setText("Quit")
        self.checkBox_terminal.setText("False")
        self.checkBox_startup.setText("False")
        self.lineEdit_type.setText("Application")


if __name__ == "__main__":
    import sys

    app = QtWidgets.QApplication(sys.argv)
    window = UiUbuntuDesktopFile()
    window.show()
    sys.exit(app.exec_())
