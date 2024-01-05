# -*- coding: utf-8 -*-

from PyQt5 import QtCore, QtWidgets


class UiCategories(QtWidgets.QWidget):
    def __init__(self, parent) -> None:
        super().__init__()
        self.parent = parent
        self.setObjectName("UiCategories")
        self.resize(402, 207)
        self.gridLayoutWidget = QtWidgets.QWidget(self)
        self.gridLayoutWidget.setGeometry(QtCore.QRect(8, 8, 385, 165))
        self.gridLayoutWidget.setObjectName("gridLayoutWidget")
        self.gridLayout = QtWidgets.QGridLayout(self.gridLayoutWidget)
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.gridLayout.setObjectName("gridLayout")
        self.checkBox = QtWidgets.QCheckBox(self.gridLayoutWidget)
        self.checkBox.setObjectName("checkBox")
        self.gridLayout.addWidget(self.checkBox, 0, 0, 1, 1)
        self.checkBox_5 = QtWidgets.QCheckBox(self.gridLayoutWidget)
        self.checkBox_5.setObjectName("checkBox_5")
        self.gridLayout.addWidget(self.checkBox_5, 4, 0, 1, 1)
        self.checkBox_7 = QtWidgets.QCheckBox(self.gridLayoutWidget)
        self.checkBox_7.setObjectName("checkBox_7")
        self.gridLayout.addWidget(self.checkBox_7, 1, 1, 1, 1)
        self.checkBox_3 = QtWidgets.QCheckBox(self.gridLayoutWidget)
        self.checkBox_3.setObjectName("checkBox_3")
        self.gridLayout.addWidget(self.checkBox_3, 2, 0, 1, 1)
        self.checkBox_9 = QtWidgets.QCheckBox(self.gridLayoutWidget)
        self.checkBox_9.setObjectName("checkBox_9")
        self.gridLayout.addWidget(self.checkBox_9, 4, 1, 1, 1)
        self.checkBox_6 = QtWidgets.QCheckBox(self.gridLayoutWidget)
        self.checkBox_6.setObjectName("checkBox_6")
        self.gridLayout.addWidget(self.checkBox_6, 0, 1, 1, 1)
        self.checkBox_2 = QtWidgets.QCheckBox(self.gridLayoutWidget)
        self.checkBox_2.setObjectName("checkBox_2")
        self.gridLayout.addWidget(self.checkBox_2, 1, 0, 1, 1)
        self.checkBox_4 = QtWidgets.QCheckBox(self.gridLayoutWidget)
        self.checkBox_4.setObjectName("checkBox_4")
        self.gridLayout.addWidget(self.checkBox_4, 3, 0, 1, 1)
        self.checkBox_8 = QtWidgets.QCheckBox(self.gridLayoutWidget)
        self.checkBox_8.setObjectName("checkBox_8")
        self.gridLayout.addWidget(self.checkBox_8, 3, 1, 1, 1)
        self.checkBox_10 = QtWidgets.QCheckBox(self.gridLayoutWidget)
        self.checkBox_10.setObjectName("checkBox_10")
        self.gridLayout.addWidget(self.checkBox_10, 0, 2, 1, 1)
        self.checkBox_11 = QtWidgets.QCheckBox(self.gridLayoutWidget)
        self.checkBox_11.setObjectName("checkBox_11")
        self.gridLayout.addWidget(self.checkBox_11, 1, 2, 1, 1)
        self.checkBox_12 = QtWidgets.QCheckBox(self.gridLayoutWidget)
        self.checkBox_12.setObjectName("checkBox_12")
        self.gridLayout.addWidget(self.checkBox_12, 2, 1, 1, 1)
        self.checkBox_13 = QtWidgets.QCheckBox(self.gridLayoutWidget)
        self.checkBox_13.setObjectName("checkBox_13")
        self.gridLayout.addWidget(self.checkBox_13, 3, 2, 1, 1)
        self.checkBox_14 = QtWidgets.QCheckBox(self.gridLayoutWidget)
        self.checkBox_14.setObjectName("checkBox_14")
        self.gridLayout.addWidget(self.checkBox_14, 2, 2, 1, 1)
        self.checkBox_15 = QtWidgets.QCheckBox(self.gridLayoutWidget)
        self.checkBox_15.setObjectName("checkBox_15")
        self.gridLayout.addWidget(self.checkBox_15, 4, 2, 1, 1)
        self.pushButton = QtWidgets.QPushButton(self)
        self.pushButton.setGeometry(QtCore.QRect(132, 172, 85, 32))
        self.pushButton.clicked.connect(self.get_type_categories)
        self.pushButton.setObjectName("pushButton")
        self.retranslateUi()
        QtCore.QMetaObject.connectSlotsByName(self)
        self.show()

    def retranslateUi(self):
        self.setWindowTitle("Select your categories")
        self.checkBox.setText("AudioVideo")
        self.checkBox_5.setText("Game")
        self.checkBox_7.setText("Network")
        self.checkBox_3.setText("Development")
        self.checkBox_9.setText("Settings")
        self.checkBox_6.setText("Graphics")
        self.checkBox_2.setText("Audio")
        self.checkBox_4.setText("Education")
        self.checkBox_8.setText("Office")
        self.checkBox_10.setText("Utility")
        self.checkBox_11.setText("Building")
        self.checkBox_12.setText("DesktopSettings")
        self.checkBox_13.setText("FileTools")
        self.checkBox_14.setText("TextEditor")
        self.checkBox_15.setText("Qt")
        self.pushButton.setText("Ok")

    def get_type_categories(self):
        list_categories = []
        for check_box in self.gridLayoutWidget.findChildren(QtWidgets.QCheckBox):
            if check_box.isChecked():
                list_categories.append(check_box.text())
        self.parent.lineEdit_categories.setText(";".join(list_categories))
        self.close()
