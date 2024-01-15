# -*- coding: utf-8 -*-

from PyQt5 import QtCore, QtWidgets


class UiCategories(QtWidgets.QDialog):
    categories_selected = QtCore.pyqtSignal(list)
    CATEGORIES = ["AudioVideo", "Audio", "Building", "DesktopSettings", "Development",
                "Education", "Game", "Graphics", "Network", "Office",
                "Qt", "Settings", "System", "TextEditor", "Utility"]
    def __init__(self) -> None:
        super().__init__()
        self.setWindowTitle("Select your categories")
        self.setFixedSize(602, 207)
        self.gridLayoutWidget = QtWidgets.QWidget(self)
        self.gridLayoutWidget.setGeometry(QtCore.QRect(8, 8, 585, 165))
        self.gridLayout = QtWidgets.QGridLayout(self.gridLayoutWidget)
        self.gridLayout.setContentsMargins(0, 0, 0, 0)

        for index, category in enumerate(self.CATEGORIES):
            row, col = divmod(index, 5)
            checkbox = QtWidgets.QCheckBox(self.gridLayoutWidget)
            checkbox.setText(category)
            self.gridLayout.addWidget(checkbox, row, col, 1, 1)

        self.pushButton = QtWidgets.QPushButton(self)
        self.pushButton.setText("Ok")
        self.pushButton.setGeometry(QtCore.QRect(int((self.width()/2)-34), 168, 68, 32))
        self.pushButton.clicked.connect(self.get_type_categories)
        

    def get_type_categories(self):
        list_categories = [
            check_box.text()
            for check_box in self.gridLayoutWidget.findChildren(QtWidgets.QCheckBox)
            if check_box.isChecked()
        ]
        self.categories_selected.emit(list_categories)
        self.close()

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    window = UiCategories()
    window.show()
    sys.exit(app.exec_())