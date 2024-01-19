
from PyQt5 import QtWidgets
from qt_file_dialog import FileDialog


class Utilities:
    def open_dialog(self, title, filtres) -> str:
        dialog = FileDialog(fileName="Test", titre=title, repertoire="", filtres=filtres)
        return dialog.open_file()

    def save_dialog(self, title, file_name) -> str:
        dialog = FileDialog(None, title, f"{file_name}.desktop", "*.desktop")
        return dialog.save_file()

    def write_desktop_file(self, destination, dict_datas) -> None:
        if dict_datas["Python"]:
            dict_datas["Exec"] = f"python3 {dict_datas['Exec']}"
        del dict_datas["Python"]
        desktop_datas = "[Desktop Entry]\n" + "\n".join(
            f"{key}={value}" for key, value in dict_datas.items()
        )
        
        with open(destination, "w") as desktop_file:
            desktop_file.write(desktop_datas)

    def display_message(self, title, text, type):
        if type == "warning":
            QtWidgets.QMessageBox.warning(None, title, text)
        else:
            QtWidgets.QMessageBox.information(None, title, text)
