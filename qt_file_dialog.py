
# -*- coding: utf-8 -*-
# le 05/07/2018 Copyright Diablo76
# Sélecteur de fichiers et répertoires V1.0.0

from PyQt5 import QtWidgets

class FileDialog(QtWidgets.QFileDialog):

    def __init__(self, fileName, titre, repertoire, filtres):
        super().__init__()
        self.fileName = fileName
        self.titre = titre
        self.repertoire = repertoire
        self.filtres = filtres

    def open_file(self):
        file_name = self.getOpenFileName(None, self.titre, self.repertoire,
                    self.filtres, options=self.DontUseNativeDialog)
        return(file_name[0])

    def open_dir(self):
        return self.getExistingDirectory(
            None, self.titre, self.repertoire, options=self.DontUseNativeDialog
        )

    def save_file(self):
        file_save = self.getSaveFileName(None, self.titre, self.repertoire,  
                    self.filtres, options=self.DontUseNativeDialog)
        return file_save[0]