''' Sélecteur de fichiers et répertoires '''
# -*- coding: utf-8 -*-
# le 05/07/2018 Copyright B.Fiquet
# Sélecteur de fichiers et répertoires V1.0.0

from PyQt5 import QtWidgets


class DialogOpen(QtWidgets.QFileDialog):
    ''' Sélecteur de fichiers et répertoires modale
        - titre Texte à afficher en titre
        - repertoire Répétoire à utiliser
        - filtres Filtres de selection '''

    def __init__(self, fileName, titre, repertoire, filtres):
        self.fileName = fileName
        self.titre = titre
        self.repertoire = repertoire
        self.filtres = filtres

    def openFile(self):
        fileName = self.getOpenFileName(None, self.titre, self.repertoire,
                                        self.filtres, "", self.DontUseNativeDialog)
        return(fileName[0])

    def openDir(self):
        dirName = self.getExistingDirectory(None, self.titre, self.repertoire, self.DontUseNativeDialog)
        return(dirName)
    
    def saveFile(self):
        fileSave = self.getSaveFileName(None, self.titre, self.repertoire,  self.filtres, "", self.DontUseNativeDialog)
        return fileSave[0]