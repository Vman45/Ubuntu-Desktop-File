# Ubuntu Desktop File

## Ubuntu Desktop File est un utilitaire permettant la création de fichiers de configuration desktop simplifiés.
### Il utilise une interface graphique (Qt).

L'interface :  
![Interface](https://github.com/diablo76600/Ubuntu-Desktop/assets/3962168/d63e3cea-5b9b-4094-8c33-119a33dc8f4f)

L'option Categories :  
![Catégories](https://github.com/diablo76600/Ubuntu-Desktop/assets/3962168/68f5580e-2b59-4e65-bae1-82cbad189d97)

![InterfaceFinale](https://github.com/diablo76600/Ubuntu-Desktop/assets/3962168/bd8dc847-20ef-4d10-9060-e3902d5bd041)

Le fichier généré : 
  
[Desktop Entry]  
Categories=DesktopSettings;Settings;Utility  
Comment=Application permettant la création de fichier de configuration desktop simplifié  
Exec=/home/diablo/Public/Applications/ubuntu_desktop_file/ubuntu_desktop_file.bin  
GenericName=Création de fichier desktop  
Icon=/home/diablo/Public/Applications/ubuntu_desktop_file/Assets/Images/Ubuntu_logo.png  
Name=Ubuntu Desktop File  
Path=/home/diablo/Public/Applications/ubuntu_desktop_file  
StartupNotify=true  
Terminal=false  
Type=Application  
Version=1.0.6  

### Ubuntu Desktop File permet également l'execution de fichiers Python avec l'option  
### Launch with Python (par défaut Python3)

L'option activée :  
![InterfaceFinalePy](https://github.com/diablo76600/Ubuntu-Desktop/assets/3962168/d81d4aa9-11a2-49c0-8262-22fd8de8a946)

Le fichier généré :  
  
[Desktop Entry]  
Categories=DesktopSettings;System;Utility  
Comment=Application permettant la création de fichier de configuration desktop simplifié  
Exec=python3 /home/diablo/Documents/GitHub/Ubuntu-Desktop/Ui_ubuntu_desktop_file.py  
GenericName=Création de fichier desktop  
Icon=/home/diablo/Documents/GitHub/Ubuntu-Desktop/Assets/Images/Ubuntu_logo.png  
Name=Ubuntu Desktop File  
Path=/home/diablo/Documents/GitHub/Ubuntu-Desktop  
StartupNotify=true  
Terminal=false  
Type=Application  
Version=1.0.6  
  
Pour executer le programme, double-cliquez sur le fichier **run_script.sh**




