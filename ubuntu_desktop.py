# -*- Coding: utf-8 -*-
# Created by Diablo76 on 04/01/2024 -- 00:44:10.
# Copyright © 2024 Diablo76. All rights reserved.
import sys
import os
from PyQt5 import QtWidgets
from Ui_ubuntu_desktop import UbuntuDesktop
from Ui_ubuntu_desktop_cat import UiCategories
from qt_dialog import DialogOpen


class CollectDatas(UbuntuDesktop):
    def __init__(self) -> None:
        super().__init__()
        self.dict_datas = {}
        self.file_desktop = ""
        # Default Type
        self.lineEdit_type.setText("Application")
        # Connect pushButton
        self.pushButton_exec.clicked.connect(self.get_exec)
        self.pushButton_icon.clicked.connect(self.get_icon)
        self.pushButton_save.clicked.connect(self.get_all_datas)
        self.pushButton_quit.clicked.connect(sys.exit)
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
        }
        self.save_desktop_file()

    def open_file_dialog(self, title):
        dial = DialogOpen("", title, "", "")
        return dial.openFile()

    def open_directory_dialog(self, title):
        dial = DialogOpen("", title, "", "")
        return dial.openDir()

    def get_exec(self):
        bin_file = self.open_file_dialog("Select Binary File")
        if bin_file:
            self.lineEdit_exec.setText(bin_file)

    def get_icon(self):
        icon_file = self.open_file_dialog("Select Icon File")
        if icon_file:
            self.lineEdit_icon.setText(icon_file)

    def get_categories(self):
        self.categories = UiCategories(self)

    def save_desktop_file(self):
        folder = self.open_directory_dialog("Destination File Desktop")
        if folder:
            file_name = self.dict_datas["Name"]
            with open(os.path.join(folder, f"{file_name}.desktop"), "w") as f:
                f.write("[Desktop Entry]\n")
                for k, v in self.dict_datas.items():
                    f.write(f"{k}={v}\n")
                QtWidgets.QMessageBox.information(self, "", "Desktop File Saved")


if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    window = CollectDatas()
    window.show()
    sys.exit(app.exec_())
