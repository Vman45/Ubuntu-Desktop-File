# -*- Coding: utf-8 -*-
# Created by Diablo76 on 04/01/2024 -- 00:44:10.
# Copyright © 2024 Diablo76. All rights reserved.

import os
from PyQt5 import QtWidgets
from qt_file_dialog import FileDialog


def open_dialog(title, filtres) -> str:
    dialog = FileDialog(fileName="Test", titre=title, repertoire="", filtres=filtres)
    return dialog.open_file()

def save_dialog(title, file_name) -> str:
    dialog = FileDialog(None, title, f"{file_name}.desktop", "*.desktop")
    return dialog.save_file()

def write_desktop_file(destination, dict_datas) -> None:
    if dict_datas["Python"]:
        dict_datas["Exec"] = f"python3 {dict_datas['Exec']}"
    del dict_datas["Python"]
    desktop_datas = "[Desktop Entry]\n" + "\n".join(
        f"{key}={value}" for key, value in dict_datas.items()
    )
    with open(destination, "w") as desktop_file:
        desktop_file.write(desktop_datas)

def display_message(title, text, type):
    if type == "warning":
        QtWidgets.QMessageBox.warning(None, title, text)
    else:
        QtWidgets.QMessageBox.information(None, title, text)
        
def file_is_exe(exec_file):
    return os.access(exec_file, os.X_OK)
        
