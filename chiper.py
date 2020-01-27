import sys
import algorithm as al
from PyQt5.QtCore import Qt, pyqtSlot
from PyQt5.QtWidgets import QApplication, QLabel, QMainWindow, QFileDialog
from PyQt5.uic import loadUi

# Subclass QMainWindow to customise your application's main window
class MainWindow(QMainWindow):

    def __init__(self, *args, **kwargs):
        super(MainWindow, self).__init__()
        loadUi('MainWindow.ui', self)
        self.setWindowTitle("Chryptography Tools")
        self.uploadButton.clicked.connect(self.on_uploadButton_clicked)
        self.saveButton.clicked.connect(self.on_saveButton_clicked)
        self.runButton.clicked.connect(self.on_runButton_clicked)
        self.showButton.clicked.connect(self.on_showButton_clicked)
    
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
                text = al.full_vigenere_encrypt(inputText, keyText, al.random_table())
            elif (self.chiperBox.currentText() == 'Auto-Key Vigènere cipher'):
                text = al.auto_key_vigenere_encrypt(inputText, keyText)
            elif (self.chiperBox.currentText() == 'Running-Key Vigènere cipher'):
                text = al.running_key_vigenere_encrypt(inputText, keyText)
            elif (self.chiperBox.currentText() == 'Extended Vigènere Cipher'):
                text = al.extended_vigenere_encrypt(inputText, keyText)
            elif (self.chiperBox.currentText() == 'Playfair Cipher'):
                text = al.playfair_encrypt(inputText, al.random_playfair_table())
            elif (self.chiperBox.currentText() == 'Super Enkripsi'):
                text = al.super_encrypt(inputText, keyText, 5)
        elif (self.decRadio.isChecked()):
            if (self.chiperBox.currentText() == 'Vigènere Chiper'):
                text = al.vigenere_decrypt(inputText, keyText)
            elif (self.chiperBox.currentText() == 'Full Vigènere Chiper'):
                text = al.full_vigenere_decrypt(inputText, keyText, al.random_table())
            elif (self.chiperBox.currentText() == 'Auto-Key Vigènere cipher'):
                text = al.auto_key_vigenere_decrypt(inputText, keyText)
            elif (self.chiperBox.currentText() == 'Running-Key Vigènere cipher'):
                text = al.running_key_vigenere_decrypt(inputText, keyText)
            elif (self.chiperBox.currentText() == 'Extended Vigènere Cipher'):
                text = al.extended_vigenere_decrypt(inputText, keyText)
            elif (self.chiperBox.currentText() == 'Playfair Cipher'):
                text = al.playfair_decrypt(inputText, al.random_playfair_table())
            elif (self.chiperBox.currentText() == 'Super Enkripsi'):
                text = al.super_decrypt(inputText, keyText, 5)

        if (self.outputBox.currentText() == 'Original'):
            self.outputText.setPlainText(al.original_separation(text,inputText))
        elif (self.outputBox.currentText() == 'Without Space'):
            self.outputText.setPlainText(text)
        elif (self.outputBox.currentText() == '5 Letter Words'):
            self.outputText.setPlainText(al.separate_by_5(text))


    def on_showButton_clicked(self):
        print('show')



app = QApplication(sys.argv)

window = MainWindow()
window.show()

app.exec_()