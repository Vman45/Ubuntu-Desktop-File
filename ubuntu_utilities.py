from PyQt5 import QtWidgets
from qt_file_dialog import FileDialog


class Utilities:
    def open_dialog(self, title) -> str:
        dialog = FileDialog("", title, "", "")
        return dialog.open_file()

    def save_dialog(self, title, file_name) -> str:
        dialog = FileDialog("", title, f"{file_name}.desktop", "*.desktop")
        return dialog.save_file()

    def write_desktop_file(self, destination, dict_datas) -> None:
        desktop_datas = "[Desktop Entry]\n" + "\n".join(
            f"{key}={value}" for key, value in dict_datas.items()
        )
        with open(destination, "w") as config_file:
            config_file.write(desktop_datas)

    def display_message(self, title, text, type):
        if type == "warning":
            QtWidgets.QMessageBox.warning(None, title, text)
        else:
            QtWidgets.QMessageBox.information(None, title, text)
