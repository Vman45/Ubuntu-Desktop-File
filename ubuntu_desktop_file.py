# -*- Coding: utf-8 -*-
# Created by Diablo76 on 04/01/2024 -- 00:44:10.
# Copyright © 2024 Diablo76. All rights reserved.

import sys
import os
from PyQt5 import QtWidgets, QtGui
from Ui_ubuntu_desktop_file import UiUbuntuDesktopFile
from Ui_categories import UiCategories
import utilities


class CollectDatas(UiUbuntuDesktopFile):
    def __init__(self) -> None:
        super().__init__()
        self.title = "Ubuntu Desktop File"
        self.ui_categories = UiCategories()
        self.ui_categories.categories_selected.connect(self.update_categories)
        self.lineEdit_exec.textChanged.connect(self.update_application_name)
        # Connect pushButtons and checkBoxes
        self._connect_signals({
            self.pushButton_exec: self.select_exec_or_python_file,
            self.pushButton_icon: self.get_icon,
            self.pushButton_save: self.save_desktop_file,
            self.pushButton_quit: app.exit,
            self.pushButton_categories: self.exec_categories,
            self.checkBox_terminal: self.update_checkbox_text,
            self.checkBox_startup: self.update_checkbox_text,
            self.checkBox_directory: self.set_path_directory,
            self.checkBox_python: self.launch_with_python
        })

    def _connect_signals(self, widgets):
        for widget, slot in widgets.items():
            widget.clicked.connect(slot)

    def update_checkbox_text(self) -> None:
        checkbox = self.sender()
        if checkbox == self.checkBox_directory:
            checkbox.setText(os.path.dirname(self.lineEdit_exec.text()) if checkbox.isChecked() else "")
        else:
            checkbox.setText(str(checkbox.isChecked()))

    def update_application_name(self):
        application_name = utilities.get_application_name(self.lineEdit_exec.text())
        self.lineEdit_name.setText(application_name)

    def update_categories(self, list_categories) -> None:
        self.lineEdit_categories.setText(";".join(list_categories))

    def get_all_datas(self) -> dict:
        return{
            "Categories": self.lineEdit_categories.text(),
            "Comment": self.lineEdit_comment.text(),
            "Exec": self.lineEdit_exec.text(),
            "GenericName": self.lineEdit_generic_name.text(),
            "Icon": self.lineEdit_icon.text(),
            "Name": self.lineEdit_name.text(),
            "Path": os.path.dirname(self.lineEdit_exec.text())
            if self.checkBox_directory.isChecked()
            else "",
            "StartupNotify": str(self.checkBox_startup.isChecked()).lower(),
            "Terminal": str(self.checkBox_terminal.isChecked()).lower(),
            "Python": self.checkBox_python.isChecked(),
            "Type": self.lineEdit_type.text(),
            "Version": self.lineEdit_version.text(),
        }

    def set_path_directory(self) -> None:
        self.checkBox_directory.setText(
            os.path.dirname(self.lineEdit_exec.text())
            if self.checkBox_directory.isChecked()
            else ""
        )

    def select_exec_or_python_file(self) -> None:
        if self.checkBox_python.isChecked():
            self.get_python_exec()
        else:
            self.get_linux_exec()
        self.set_path_directory()

    def get_python_exec(self):
        if python_file := utilities.select_python_file():
            self.lineEdit_exec.setText(python_file)
        else:
            self.lineEdit_exec.clear()

    def get_linux_exec(self):
        if exec_file := utilities.select_executable_file(self.title):
            self.lineEdit_exec.setText(exec_file)

    def get_icon(self) -> None:
        if icon_file := utilities.open_file_dialog(title="Select icon file.", filter=""):
            self.lineEdit_icon.setText(icon_file)
            pixmap = QtGui.QPixmap(icon_file)
            if not pixmap.isNull():
                self.label_icon_application.setPixmap(pixmap)
            else:
                utilities.display_message(self.title, f"{icon_file} is not recognized.", "information")
                self.lineEdit_icon.clear()

    def exec_categories(self) -> None:
        self.ui_categories.exec_()
        
    def launch_with_python(self):
        if self.checkBox_python.isChecked():
            self.label_exec.setText("Python file :")
            self.label_exec.setStyleSheet("color : red;")
        else:
            self.label_exec.setText("Exec :")
            self.label_exec.setStyleSheet("color : None;")

    def check_widgets(self):
        if not self.lineEdit_name.text():
            utilities.display_message(self.title, "Please enter a Application Name.", "information")
            return False
        if not self.lineEdit_exec.text():
            message = "Please enter a Python File ." if self.checkBox_python.isChecked() else "Please enter a executable file."
            utilities.display_message(self.title, message, "information")
            return False
        return True

    def save_desktop_file(self) -> None:
        if self.check_widgets():
            if destination := utilities.save_file_dialog(
                title="Destination Desktop File",
                file_name=self.lineEdit_name.text(),
            ):
                try:
                    utilities.write_desktop_file(destination, self.get_all_datas())
                    utilities.display_message(self.title, f"File {destination} saved.", "information")
                except IOError as error:
                    utilities.display_message(self.title, f"Unable to create file !! {error}", "warning")



if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    window = CollectDatas()
    window.show()
    sys.exit(app.exec_())
