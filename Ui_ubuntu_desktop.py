# -*- coding: utf-8 -*-

from PyQt5 import QtCore, QtGui, QtWidgets


class UbuntuDesktop(QtWidgets.QMainWindow):
    def __init__(self) -> None:
        super().__init__()
        self.setObjectName("ubuntu_desktop")
        self.resize(573, 355)
        self.gridLayoutWidget = QtWidgets.QWidget(self)
        self.gridLayoutWidget.setGeometry(QtCore.QRect(8, 8, 557, 305))
        self.gridLayoutWidget.setObjectName("gridLayoutWidget")
        self.gridLayout = QtWidgets.QGridLayout(self.gridLayoutWidget)
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.gridLayout.setObjectName("gridLayout")
        # Widgets Name
        self.label_name = QtWidgets.QLabel(self.gridLayoutWidget)
        self.label_name.setObjectName("label_name")
        self.gridLayout.addWidget(self.label_name, 0, 0, 1, 1)
        self.lineEdit_name = QtWidgets.QLineEdit(self.gridLayoutWidget)
        self.lineEdit_name.setObjectName("lineEdit_name")
        self.gridLayout.addWidget(self.lineEdit_name, 0, 2, 1, 1)
        # Widgets Generic Name
        self.label_generic_name = QtWidgets.QLabel(self.gridLayoutWidget)
        self.label_generic_name.setObjectName("label_generic_name")
        self.gridLayout.addWidget(self.label_generic_name, 1, 0, 1, 1)
        self.lineEdit_generic_name = QtWidgets.QLineEdit(self.gridLayoutWidget)
        self.lineEdit_generic_name.setObjectName("lineEdit_generic_name")
        self.gridLayout.addWidget(self.lineEdit_generic_name, 1, 2, 1, 1)
        # Widgets Comment
        self.label_comment = QtWidgets.QLabel(self.gridLayoutWidget)
        self.label_comment.setObjectName("label_comment")
        self.gridLayout.addWidget(self.label_comment, 2, 0, 1, 1)
        self.lineEdit_comment = QtWidgets.QLineEdit(self.gridLayoutWidget)
        self.lineEdit_comment.setObjectName("lineEdit_comment")
        self.gridLayout.addWidget(self.lineEdit_comment, 2, 2, 1, 1)
        # Widgets Exec
        self.label_exec = QtWidgets.QLabel(self.gridLayoutWidget)
        self.label_exec.setObjectName("label_exec")
        self.gridLayout.addWidget(self.label_exec, 3, 0, 1, 1)
        self.lineEdit_exec = QtWidgets.QLineEdit(self.gridLayoutWidget)
        self.lineEdit_exec.setObjectName("lineEdit_exec")
        self.gridLayout.addWidget(self.lineEdit_exec, 3, 2, 1, 1)
        self.pushButton_exec = QtWidgets.QPushButton(self.gridLayoutWidget)
        self.pushButton_exec.setObjectName("pushButton_exec")
        self.gridLayout.addWidget(self.pushButton_exec, 3, 3, 1, 1)
        # Widgets Icon
        self.label_icon = QtWidgets.QLabel(self.gridLayoutWidget)
        self.label_icon.setObjectName("label_icon")
        self.gridLayout.addWidget(self.label_icon, 4, 0, 1, 1)
        self.lineEdit_icon = QtWidgets.QLineEdit(self.gridLayoutWidget)
        self.lineEdit_icon.setObjectName("lineEdit_icon")
        self.gridLayout.addWidget(self.lineEdit_icon, 4, 2, 1, 1)
        self.pushButton_icon = QtWidgets.QPushButton(self.gridLayoutWidget)
        self.pushButton_icon.setObjectName("pushButton_icon")
        self.gridLayout.addWidget(self.pushButton_icon, 4, 3, 1, 1)
        # Widgets Type
        self.label_type = QtWidgets.QLabel(self.gridLayoutWidget)
        self.label_type.setObjectName("label_type")
        self.gridLayout.addWidget(self.label_type, 5, 0, 1, 1)
        self.lineEdit_type = QtWidgets.QLineEdit(self.gridLayoutWidget)
        self.lineEdit_type.setObjectName("lineEdit_type")
        self.gridLayout.addWidget(self.lineEdit_type, 5, 2, 1, 1)
        # Widgets Version
        self.label_version = QtWidgets.QLabel(self.gridLayoutWidget)
        self.label_version.setObjectName("label_version")
        self.gridLayout.addWidget(self.label_version, 6, 0, 1, 1)
        self.lineEdit_version = QtWidgets.QLineEdit(self.gridLayoutWidget)
        self.lineEdit_version.setObjectName("lineEdit_version")
        self.gridLayout.addWidget(self.lineEdit_version, 6, 2, 1, 1)
        self.label_categories = QtWidgets.QLabel(self.gridLayoutWidget)
        self.label_categories.setObjectName("label_categories")
        self.gridLayout.addWidget(self.label_categories, 7, 0, 1, 1)
        self.lineEdit_categories = QtWidgets.QLineEdit(self.gridLayoutWidget)
        self.lineEdit_categories.setObjectName("lineEdit_categories")
        self.gridLayout.addWidget(self.lineEdit_categories, 7, 2, 1, 1)
        self.pushButton_categories = QtWidgets.QPushButton(self.gridLayoutWidget)
        self.pushButton_categories.setObjectName("pushButton_categories")
        self.gridLayout.addWidget(self.pushButton_categories, 7, 3, 1, 1)
        self.label_terminal = QtWidgets.QLabel(self.gridLayoutWidget)
        # Widgets Teminal
        self.label_terminal.setObjectName("label_terminal")
        self.gridLayout.addWidget(self.label_terminal, 8, 0, 1, 1)
        self.checkBox_terminal = QtWidgets.QCheckBox(self.gridLayoutWidget)
        self.checkBox_terminal.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.checkBox_terminal.setObjectName("checkBox_terminal")
        self.gridLayout.addWidget(self.checkBox_terminal, 8, 2, 1, 1)
        # Widget Save
        self.pushButton_save = QtWidgets.QPushButton(self)
        self.pushButton_save.setGeometry(QtCore.QRect(256, 312, 69, 32))
        self.pushButton_save.setObjectName("pushButton_save")
        # Widget Quit
        self.pushButton_quit = QtWidgets.QPushButton(self)
        self.pushButton_quit.setGeometry(QtCore.QRect(500, 312, 69, 32))
        self.pushButton_quit.setObjectName("pushButton_quit")
        self.retranslateUi()

    def retranslateUi(self):
        self.setWindowTitle("Ubuntu Desktop File")
        self.label_version.setText("Version :")
        self.label_generic_name.setText("Generic Name :")
        self.label_name.setText("Name :")
        self.label_type.setText("Type :")
        self.label_exec.setText("Exec :")
        self.label_icon.setText("Icon :")
        self.label_comment.setText("Comment :")
        self.pushButton_exec.setText("...")
        self.pushButton_icon.setText("...")
        self.label_categories.setText("Categories :")
        self.pushButton_categories.setText("...")
        self.label_terminal.setText("Terminal :")
        self.pushButton_save.setText("Save")
        self.pushButton_quit.setText("Quit")


if __name__ == "__main__":
    import sys

    app = QtWidgets.QApplication(sys.argv)
    window = UbuntuDesktop()
    window.show()
    sys.exit(app.exec_())
