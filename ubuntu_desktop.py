# -*- Coding: utf-8 -*-
# Created by Diablo76 on 04/01/2024 -- 00:44:10.
# Copyright © 2024 Diablo76. All rights reserved.

import sys
import os
from PyQt5 import QtWidgets
from Ui_ubuntu_desktop import UiUbuntuDesktop
from Ui_ubuntu_desktop_cat import UiCategories
from qt_dialog import DialogOpen

__version__ = "1.0.3"

class CollectDatas(UiUbuntuDesktop):
    def __init__(self) -> None:
        super().__init__()
        self.dict_datas = {}
        self.title = "Ubuntu Desktop File"
        self.file_desktop = ""
        # Default Type
        self.lineEdit_type.setText("Application")
        # Connect pushButton
        self.pushButton_exec.clicked.connect(self.get_exec)
        self.pushButton_icon.clicked.connect(self.get_icon)
        self.pushButton_save.clicked.connect(self.get_all_datas)
        self.pushButton_quit.clicked.connect(app.exit)
        self.pushButton_categories.clicked.connect(self.get_categories)

    def get_all_datas(self):
        self.dict_datas = {
            "Name": self.lineEdit_name.text(),
            "GenericName": self.lineEdit_generic_name.text(),
            "Comment": self.lineEdit_comment.text(),
            "Exec": self.lineEdit_exec.text(),
            "Icon": self.lineEdit_icon.text(),
            "Type": self.lineEdit_type.text(),
            "Version": self.lineEdit_version.text(),
            "Categories": self.lineEdit_categories.text(),
            "Terminal": "true" if self.checkBox_terminal.isChecked() else "false",
            "Path": os.path.dirname(self.lineEdit_exec.text()) if self.checkBox_directory.isChecked() else "",
            "StartupNotify": "true" if self.checkBox_startup.isChecked() else "false",
        }
        self.save_desktop_file()

    def open_dialog(self, title, is_directory=False):
        dialog = DialogOpen("", title, "", "")
        return dialog.openDir() if is_directory else dialog.openFile()

    def get_exec(self):
        if binary_name := self.open_dialog("Select binary file"):
            self.lineEdit_exec.setText(binary_name)

    def get_icon(self):
        if icon_name := self.open_dialog("Select icon file"):
            self.lineEdit_icon.setText(icon_name)

    def get_categories(self):
        UiCategories(self)

    def write_desktop_file(self, folder, file_name):
        try:
            datas = "[Desktop Entry]\n" + "\n".join(f"{key}={value}" for key, value in self.dict_datas.items())
            with open(os.path.join(folder, f"{file_name}.desktop"), "w") as f:
                f.write(datas)
            return True
        except IOError as er:
            self.show_message(self.title, f"Unable to create file !! {er}")
            return False

    def save_desktop_file(self):
        if folder := self.open_dialog("Destination Desktop File", is_directory=True):
            file_name = self.dict_datas["Name"]
            if self.write_desktop_file(folder, file_name):
                self.show_message(self.title, f"File {file_name} Saved in {folder}")
    
    def show_message(self, title, message):
        QtWidgets.QMessageBox.information(self, title, message)


if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    window = CollectDatas()
    window.show()
    sys.exit(app.exec_())
