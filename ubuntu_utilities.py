import configparser
from qt_file_dialog import DialogOpen


class Utilities:
    def open_dialog(self, title) -> str:
        dialog = DialogOpen("", title, "", "")
        return dialog.openFile()

    def save_dialog(self, title) -> str:
        dialog = DialogOpen(
            "", title, f"{self.lineEdit_name.text()}.desktop", "*.desktop"
        )
        return dialog.saveFile()
    
    def write_desktop_file(self, destination, dict_datas) -> None:
        config = configparser.ConfigParser()
        config.optionxform = str
        config["Desktop Entry"] = dict_datas
        with open(destination, "w") as config_file:
            config.write(config_file, space_around_delimiters=False)
    