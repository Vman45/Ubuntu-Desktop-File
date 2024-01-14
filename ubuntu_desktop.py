# -*- Coding: utf-8 -*-
# Created by Diablo76 on 04/01/2024 -- 00:44:10.
# Copyright © 2024 Diablo76. All rights reserved.

import sys
import os
import configparser
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
        # Connect pushButtons and checkBoxes
        self._connect_signals({
            self.pushButton_exec: self.get_exec,
            self.pushButton_icon: self.get_icon,
            self.pushButton_save: self.get_all_datas,
            self.pushButton_quit: app.exit,
            self.pushButton_categories: self.get_categories,
            self.checkBox_terminal: self.update_checkbox,
            self.checkBox_startup: self.update_checkbox,
            self.checkBox_directory: self.set_path_directory
        })

    def _connect_signals(self, widgets):
        for widget, slot in widgets.items():
            widget.clicked.connect(slot)

    def update_checkbox(self) -> None:
        self.sender().setText(str(self.sender().isChecked()))

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

    def set_path_directory(self) -> None:
        self.checkBox_directory.setText(
            os.path.dirname(self.lineEdit_exec.text())
            if self.checkBox_directory.isChecked()
            else ""
        )

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
        config = configparser.ConfigParser()
        config.optionxform = str
        config["Desktop Entry"] = self.dict_datas
        try:
            with open(destination, "w") as config_file:
                config.write(config_file, space_around_delimiters=False)
            return True
        except IOError as error:
            self.show_message(self.title, f"Unable to create file !! {error}")
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
