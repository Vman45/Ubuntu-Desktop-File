# -*- coding: utf-8 -*-

from PyQt5 import QtCore, QtWidgets


class UiCategories(QtWidgets.QDialog):
    def __init__(self, parent) -> None:
        super().__init__()
        self.setWindowTitle("Select your categories")
        self.parent = parent
        self.resize(402, 207)
        self.gridLayoutWidget = QtWidgets.QWidget(self)
        self.gridLayoutWidget.setGeometry(QtCore.QRect(8, 8, 385, 165))
        self.gridLayout = QtWidgets.QGridLayout(self.gridLayoutWidget)
        self.gridLayout.setContentsMargins(0, 0, 0, 0)

        checkbox_info = {
            "checkBox_1": ("AudioVideo", 0, 0),
            "checkBox_2": ("Audio", 1, 0),
            "checkBox_3": ("Development", 2, 0),
            "checkBox_4": ("Education", 3, 0),
            "checkBox_5": ("Game", 4, 0),
            "checkBox_6": ("Graphics", 0, 1),
            "checkBox_7": ("Network", 1, 1),
            "checkBox_8": ("Office", 3, 1),
            "checkBox_9": ("Settings", 4, 1),
            "checkBox_10": ("Utility", 0, 2),
            "checkBox_11": ("Building", 1, 2),
            "checkBox_12": ("DesktopSettings", 2, 1),
            "checkBox_13": ("System", 3, 2),
            "checkBox_14": ("TextEditor", 2, 2),
            "checkBox_15": ("Qt", 4, 2),
        }
        for text, row, col in checkbox_info.values():
            checkbox = QtWidgets.QCheckBox(self.gridLayoutWidget)
            checkbox.setText(text)
            self.gridLayout.addWidget(checkbox, row, col, 1, 1)

        self.pushButton = QtWidgets.QPushButton(self)
        self.pushButton.setText("Ok")
        self.pushButton.setGeometry(QtCore.QRect(165, 172, 85, 32))
        self.pushButton.clicked.connect(self.get_type_categories)
        self.exec_()

    def get_type_categories(self):
        list_categories = [
            check_box.text()
            for check_box in self.gridLayoutWidget.findChildren(
                QtWidgets.QCheckBox
            )
            if check_box.isChecked()
        ]
        self.parent.lineEdit_categories.setText(";".join(list_categories))
        self.close()
        
    def exec_(self) -> int:
        return super().exec_()
