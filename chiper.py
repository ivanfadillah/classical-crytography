import sys
import algorithm as al
from PyQt5.QtCore import Qt, pyqtSlot
from PyQt5.QtWidgets import QApplication, QLabel, QMainWindow, QFileDialog, QMessageBox
from PyQt5.uic import loadUi

# Subclass QMainWindow to customise your application's main window
class MainWindow(QMainWindow):

    def __init__(self, *args, **kwargs):
        self.fullVigenereTable = []
        self.playfairTable = []
        super(MainWindow, self).__init__()
        loadUi('MainWindow.ui', self)
        self.setWindowTitle("Chryptography Tools")
        self.uploadButton.clicked.connect(self.on_uploadButton_clicked)
        self.saveButton.clicked.connect(self.on_saveButton_clicked)
        self.runButton.clicked.connect(self.on_runButton_clicked)
        self.genFullVigenere.clicked.connect(self.on_genFullVigenere_clicked)
        self.genPlayfair.clicked.connect(self.on_genPlayfair_clicked)
        self.showFullVigenere.clicked.connect(self.on_showFullVigenere_clicked)
        self.showPlayfair.clicked.connect(self.on_showPlayfair_clicked)
    
    @pyqtSlot()
    def on_uploadButton_clicked(self):
        options = QFileDialog.Options()
        options |= QFileDialog.DontUseNativeDialog
        pathFileName, _ = QFileDialog.getOpenFileName(self,"QFileDialog.getOpenFileName()", "","All Files (*);;Text Files (*.txt)", options=options)
        with open(pathFileName, 'r',  encoding='utf-8') as file:
            data = file.read()
        self.inputText.setPlainText(data)

    def on_saveButton_clicked(self):
        mytext = self.outputText.toPlainText()
        with open('output.txt', 'w' , encoding='utf-8') as f:
            f.write(mytext)

    def on_runButton_clicked(self):
        text = ""
        inputText = self.inputText.toPlainText().lower()
        keyText = self.keyText.toPlainText().lower()
        if (self.enRadio.isChecked()):
            if (self.chiperBox.currentText() == 'Vigènere Chiper'):
                text = al.vigenere_encrypt(inputText, keyText)
            elif (self.chiperBox.currentText() == 'Full Vigènere Chiper'):
                if (self.fullVigenereTable != []):
                     text = al.full_vigenere_encrypt(inputText, keyText, self.fullVigenereTable)
                else:
                    txt = "Empty Table, Please click generate Full Vigenere table"
                    QMessageBox.about(self, '', txt)
            elif (self.chiperBox.currentText() == 'Auto-Key Vigènere cipher'):
                text = al.auto_key_vigenere_encrypt(inputText, keyText)
            elif (self.chiperBox.currentText() == 'Running-Key Vigènere cipher'):
                text = al.running_key_vigenere_encrypt(inputText, keyText)
            elif (self.chiperBox.currentText() == 'Extended Vigènere Cipher'):
                text = al.extended_vigenere_encrypt(inputText, keyText)
            elif (self.chiperBox.currentText() == 'Playfair Cipher'):
                if (self.playfairTable != []):
                     text = al.playfair_encrypt(inputText, self.playfairTable)
                else:
                    txt = "Empty Table, Please click generate playfair table"
                    QMessageBox.about(self, '', txt)
            elif (self.chiperBox.currentText() == 'Super Enkripsi'):
                text = al.super_encrypt(inputText, keyText, 5)
        elif (self.decRadio.isChecked()):
            if (self.chiperBox.currentText() == 'Vigènere Chiper'):
                text = al.vigenere_decrypt(inputText, keyText)
            elif (self.chiperBox.currentText() == 'Full Vigènere Chiper'):
                if (self.fullVigenereTable != []):
                     text = al.full_vigenere_decrypt(inputText, keyText, self.fullVigenereTable)
                else:
                    txt = "Empty Table, Please click generate Full Vigenere table"
                    QMessageBox.about(self, '', txt)
            elif (self.chiperBox.currentText() == 'Auto-Key Vigènere cipher'):
                text = al.auto_key_vigenere_decrypt(inputText, keyText)
            elif (self.chiperBox.currentText() == 'Running-Key Vigènere cipher'):
                text = al.running_key_vigenere_decrypt(inputText, keyText)
            elif (self.chiperBox.currentText() == 'Extended Vigènere Cipher'):
                text = al.extended_vigenere_decrypt(inputText, keyText)
            elif (self.chiperBox.currentText() == 'Playfair Cipher'):
                if (self.playfairTable != []):
                     text = al.playfair_decrypt(inputText, self.playfairTable)
                else:
                    txt = "Empty Table, Please click generate playfair table"
                    QMessageBox.about(self, '', txt)
            elif (self.chiperBox.currentText() == 'Super Enkripsi'):
                text = al.super_decrypt(inputText, keyText, 5)

        if (self.outputBox.currentText() == 'Original'):
            self.outputText.setPlainText(al.original_separation(text,inputText))
        elif (self.outputBox.currentText() == 'Without Space'):
            self.outputText.setPlainText(text)
        elif (self.outputBox.currentText() == '5 Letter Words'):
            self.outputText.setPlainText(al.separate_by_5(text))


    def on_genFullVigenere_clicked(self):
        self.fullVigenereTable = al.random_table()

    def on_genPlayfair_clicked(self):
        self.playfairTable = al.random_playfair_table()

    def on_showFullVigenere_clicked(self):
        table = ''
        if (self.fullVigenereTable != []):
            table = al.rand_table_to_str(self.fullVigenereTable)
        else:
            table = "Empty Table, Please click generate Full Vigenere table"
        QMessageBox.about(self, '', table)

    def on_showPlayfair_clicked(self):
        table = ''
        if (self.playfairTable != []):
            table = al.playfair_table_to_str(self.playfairTable)
        else:
            table = "Empty Table, Please click generate Playfair table"
        QMessageBox.about(self, '', table)


app = QApplication(sys.argv)

window = MainWindow()
window.show()

app.exec_()