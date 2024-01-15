import configparser
from PyQt5 import QtWidgets
from qt_file_dialog import FileDialog


class Utilities:
    def open_dialog(self, title) -> str:
        dialog = FileDialog("", title, "", "")
        return dialog.open_file()

    def save_dialog(self, title, file_name) -> str:
        dialog = FileDialog(
            "", title, f"{file_name}.desktop", "*.desktop"
        )
        return dialog.save_file()
    
    def write_desktop_file(self, destination, dict_datas) -> None:
        config = configparser.ConfigParser()
        config.optionxform = str
        config["Desktop Entry"] = dict_datas
        with open(destination, "w") as config_file:
            config.write(config_file, space_around_delimiters=False)
    
    def display_message(self, title, text, type):
        if type == "warning":
            QtWidgets.QMessageBox.warning(self, title, text)
        else:
            QtWidgets.QMessageBox.information(self, title, text)