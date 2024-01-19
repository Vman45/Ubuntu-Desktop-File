# -*- Coding: utf-8 -*-
# Created by Diablo76 on 04/01/2024 -- 00:44:10.
# Copyright © 2024 Diablo76. All rights reserved.

import sys
import os
from PyQt5 import QtWidgets
from Ui_ubuntu_desktop import UiUbuntuDesktop
from Ui_ubuntu_desktop_cat import UiCategories
from ubuntu_utilities import Utilities


class CollectDatas(UiUbuntuDesktop):
    def __init__(self) -> None:
        super().__init__()
        self.title = "UDesktopFile"
        self.ui_categories = UiCategories()
        self.ui_categories.categories_selected.connect(self.update_categories)
        # Connect pushButtons and checkBoxes
        self._connect_signals({
            self.pushButton_exec: self.get_exec,
            self.pushButton_icon: self.get_icon,
            self.pushButton_save: self.get_all_datas,
            self.pushButton_quit: app.exit,
            self.pushButton_categories: self.exec_categories,
            self.checkBox_terminal: self.update_checkbox,
            self.checkBox_startup: self.update_checkbox,
            self.checkBox_directory: self.set_path_directory,
            self.checkBox_python: self.start_with_python
        })

    def _connect_signals(self, widgets):
        for widget, slot in widgets.items():
            widget.clicked.connect(slot)

    def update_checkbox(self) -> None:
        self.sender().setText(str(self.sender().isChecked())) # type: ignore

    def update_categories(self, list_categories):
        self.lineEdit_categories.setText(";".join(list_categories))

    def get_all_datas(self) -> None:
        dict_datas = {
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
        self.save_desktop_file(dict_datas)

    def set_path_directory(self) -> None:
        self.checkBox_directory.setText(
            os.path.dirname(self.lineEdit_exec.text())
            if self.checkBox_directory.isChecked()
            else ""
        )

    def get_exec(self) -> None:
        if self.checkBox_python.isChecked():
            self.get_python_file()
        elif binary_name := Utilities.open_dialog(self, title="Select binary file", filtres=""):
            self.lineEdit_exec.setText(binary_name)
            self.set_path_directory()

    def get_python_file(self):
        if python_name := Utilities.open_dialog(self, title="Select python file", filtres="*.py"):
            self.lineEdit_exec.setText(python_name)
        

    def get_icon(self) -> None:
        if icon_name := Utilities.open_dialog(self, title="Select icon file", filtres=""):
            self.lineEdit_icon.setText(icon_name)

    def exec_categories(self) -> None:
        self.ui_categories.exec_()
        
    def start_with_python(self):
        if self.checkBox_python.isChecked():
            self.label_exec.setText("Python file :")
        else:
            self.label_exec.setText("Exec :")

    def save_desktop_file(self, dict_datas) -> None:
        file_name = self.lineEdit_name.text()
        if not file_name:
            Utilities.display_message(None, self.title, "Please enter a File Name.", "information")
            return
        destination = Utilities.save_dialog(self, title="Destination Desktop File", file_name=file_name)
        if not destination:
            return
        try:
            Utilities.write_desktop_file(self, destination, dict_datas)
            Utilities.display_message(None, self.title, f"File {destination} Saved.", "information")
        except IOError as error:
            Utilities.display_message(None, self.title, f"Unable to create file !! {error}", "warning")



if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    window = CollectDatas()
    window.show()
    sys.exit(app.exec_())
