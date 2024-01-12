# -*- Coding: utf-8 -*-
# Created by Diablo76 on 04/01/2024 -- 00:44:10.
# Copyright © 2024 Diablo76. All rights reserved.

import sys
import os
from PyQt5 import QtWidgets
from Ui_ubuntu_desktop import UiUbuntuDesktop
from Ui_ubuntu_desktop_cat import UiCategories
from qt_file_dialog import DialogOpen

__version__ = "1.0.3"


class CollectDatas(UiUbuntuDesktop):
    def __init__(self) -> None:
        super().__init__()
        self.dict_datas = {}
        self.title = "UDesktopFile"
        # Connect pushButtons
        self.pushButton_exec.clicked.connect(self.get_exec)
        self.pushButton_icon.clicked.connect(self.get_icon)
        self.pushButton_save.clicked.connect(self.get_all_datas)
        self.pushButton_quit.clicked.connect(app.exit)
        self.pushButton_categories.clicked.connect(self.get_categories)
        # Connect checkBoxes
        self.checkBox_terminal.clicked.connect(self.set_statut_checkbox)
        self.checkBox_startup.clicked.connect(self.set_statut_checkbox)
        self.checkBox_directory.clicked.connect(self.set_path_directory)

    def get_all_datas(self) -> None:
        self.dict_datas = {
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
            "Type": self.lineEdit_type.text(),
            "Version": self.lineEdit_version.text(),
        }
        self.save_desktop_file()

    def set_statut_checkbox(self) -> None:
        self.sender().setText(str(self.sender().isChecked()))
    
    def set_path_directory(self) -> None:
        if self.checkBox_directory.isChecked():
            self.checkBox_directory.setText(os.path.dirname(self.lineEdit_exec.text()))
        else:
            self.checkBox_directory.setText("")

    def open_dialog(self, title) -> str:
        dialog = DialogOpen("", title, "", "")
        return dialog.openFile()

    def save_dialog(self, title) -> str:
        dialog = DialogOpen(
            "", title, f"{self.lineEdit_name.text()}.desktop", "*.desktop"
        )
        return dialog.saveFile()

    def get_exec(self) -> None:
        if binary_name := self.open_dialog("Select binary file"):
            self.lineEdit_exec.setText(binary_name)
            self.set_path_directory()

    def get_icon(self) -> None:
        if icon_name := self.open_dialog("Select icon file"):
            self.lineEdit_icon.setText(icon_name)

    def get_categories(self) -> None:
        UiCategories(self)

    def write_desktop_file(self, destination) -> bool:
        try:
            datas_file = "[Desktop Entry]\n" + "\n".join(
                f"{key}={value}" for key, value in self.dict_datas.items()
            )
            with open(destination, "w") as f:
                f.write(datas_file)
            return True
        except IOError as er:
            self.show_message(self.title, f"Unable to create file !! {er}")
            return False

    def save_desktop_file(self) -> None:
        if self.lineEdit_name.text():
            if destination := self.save_dialog("Destination Desktop File"):
                if self.write_desktop_file(destination):
                    self.show_message(self.title, f"File {destination} Saved.")
        else:
            self.show_message(self.title, "Please enter a File Name.")

    def show_message(self, title, message) -> None:
        QtWidgets.QMessageBox.information(self, title, message)


if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    window = CollectDatas()
    window.show()
    sys.exit(app.exec_())
