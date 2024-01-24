
# -*- coding: utf-8 -*-
# le 05/07/2018 Copyright Diablo76
# Sélecteur de fichiers et répertoires V1.0.0

from PyQt5.QtWidgets import QFileDialog

class FileDialog(QFileDialog):

    def __init__(self, title, directory, default_filename, filter):
        super().__init__()
        self.default_filename = default_filename
        self.title = title
        self.directory = directory
        self.filter = filter

    def open_file(self):
        return self.getOpenFileName(None, self.title, self.directory,
                    self.filter, options=self.DontUseNativeDialog)[0]

    def open_dir(self):
        return self.getExistingDirectory(
            None, self.title, self.directory, options=self.DontUseNativeDialog
        )

    def save_file(self):
        return self.getSaveFileName(None, self.title, self.default_filename, self.directory,  
                    self.filter, options=self.DontUseNativeDialog)[0]
