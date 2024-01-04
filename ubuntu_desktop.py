# -*- Coding: utf-8 -*-
# Created by Diablo76 on 04/01/2024 -- 00:44:10.
# Copyright © 2024 Diablo76. All rights reserved.
import sys
from PyQt5 import QtWidgets
import configparser
from Ui_ubuntu_desktop import UbuntuDesktop
from Ui_ubuntu_desktop_cat import UiCategories
from qt_dialog import DialogOpen


class CollectDatas(UbuntuDesktop):
    def __init__(self) -> None:
        super().__init__()
        self.file_desktop = ""
        self.dict_datas = {
            "Name": "",
            "Generic Name": "",
            "Comment": "",
            "Exec": "",
            "Icon": "",
            "Type": "",
            "Version": "",
            "Categories": "",
            "Terninal": "",
        }
        # Default Type
        self.lineEdit_type.setText("Application")
        # Connect pushButton
        self.pushButton_exec.clicked.connect(self.get_exec)
        self.pushButton_icon.clicked.connect(self.get_icon)
        self.pushButton_save.clicked.connect(self.get_all_datas)
        self.pushButton_categories.clicked.connect(self.get_categories)

    def get_all_datas(self):
        self.dict_datas["Name"] = self.lineEdit_name.text()
        self.dict_datas["Generic Name"] = self.lineEdit_generic_name.text()
        self.dict_datas["Exec"] = self.lineEdit_exec.text()
        self.dict_datas["Icon"] = self.lineEdit_icon.text()
        self.dict_datas["Type"] = self.lineEdit_type.text()
        self.dict_datas["Version"] = self.lineEdit_version.text()
        self.dict_datas["Categories"] = self.lineEdit_categories.text()
        if self.checkBox_terminal.isChecked():
            self.dict_datas["Terminal"] = "true"
        else:
            self.dict_datas["Terminal"] = "false"
        self.create_file_parser()

    def get_exec(self):
        dial = DialogOpen("", "Select Exe File", "", "")
        file_exe = dial.openFile()
        self.lineEdit_exec.setText(file_exe)

    def get_icon(self):
        dial = DialogOpen("", "Select Icon File", "", "")
        file_exe = dial.openFile()
        self.lineEdit_icon.setText(file_exe)

    def get_categories(self):
        self.categories = UiCategories(self)

    def create_file_parser(self):
        parser = configparser.ConfigParser()
        parser.add_section("Desktop Entry")
        for key in self.dict_datas.keys():
            parser.set("Desktop Entry", key, self.dict_datas[key])
        self.save_desktop_file(parser)

    def save_desktop_file(self, parser):
        file_name = self.dict_datas["Name"]
        dial = DialogOpen("", "Destination File Desktop", "", "")
        dir = dial.openDir()
        if dir:
            with open(f"{dir}{file_name}.desktop", "w") as f:
                parser.write(f)


if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    window = CollectDatas()
    window.show()
    sys.exit(app.exec_())
