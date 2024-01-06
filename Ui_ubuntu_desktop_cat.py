# -*- coding: utf-8 -*-

from PyQt5 import QtCore, QtWidgets


class UiCategories(QtWidgets.QDialog):
    def __init__(self, parent) -> None:
        super().__init__()
        self.setWindowTitle("Select your categories")
        self.parent = parent
        self.resize(602, 207)
        self.gridLayoutWidget = QtWidgets.QWidget(self)
        self.gridLayoutWidget.setGeometry(QtCore.QRect(8, 8, 585, 165))
        self.gridLayout = QtWidgets.QGridLayout(self.gridLayoutWidget)
        self.gridLayout.setContentsMargins(0, 0, 0, 0)

        categories = ["AudioVideo", "Audio", "Building", "DesktopSettings", "Development",
                "Education", "Game", "Graphics", "Network", "Office",
                "Qt", "Settings", "System", "TextEditor", "Utility"]
        
        for index, category in enumerate(categories):
            row, col = divmod(index, 5)
            checkbox = QtWidgets.QCheckBox(self.gridLayoutWidget)
            checkbox.setText(category)
            self.gridLayout.addWidget(checkbox, row, col, 1, 1)

        self.pushButton = QtWidgets.QPushButton(self)
        self.pushButton.setText("Ok")
        self.pushButton.setGeometry(QtCore.QRect(276, 172, 85, 32))
        self.pushButton.clicked.connect(self.get_type_categories)
        self.exec_()

    def get_type_categories(self):
        list_categories = [
            check_box.text()
            for check_box in self.gridLayoutWidget.findChildren(QtWidgets.QCheckBox)
            if check_box.isChecked()
        ]
        self.parent.lineEdit_categories.setText(";".join(list_categories))
        self.close()