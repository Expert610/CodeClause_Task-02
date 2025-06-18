from MyNote import Ui_main
import sys
from PyQt5 import QtWidgets
from PyQt5.QtGui import QFont,QTextCharFormat
from PyQt5.QtWidgets import QApplication,QMainWindow,QFileDialog,QMessageBox,QTextEdit
from PyQt5.QtPrintSupport import QPrintDialog,QPrinter

class MyNoteApp(QMainWindow):
    def __init__(self):
        super().__init__()
        self.ui=Ui_main()
        self.ui.setupUi(self)
        self.current_file = None


        self.ui.actionOpen.triggered.connect(self.open_file)
        self.ui.actionSave.triggered.connect(self.save_file)
        self.ui.actionExit.triggered.connect(self.close_file)
        self.ui.actionNew.triggered.connect(self.new_file)
        self.ui.actionNew_Window.triggered.connect(self.new_window)
        self.ui.actionPrint.triggered.connect(self.print_file)
        self.ui.actionNote_Text.triggered.connect(self.about_app)
        self.ui.actionCopy.triggered.connect(self.copy_txt)
        self.ui.actionCut.triggered.connect(self.cut_txt)
        self.ui.actionDelete.triggered.connect(self.delete_txt)
        self.ui.actionPaste.triggered.connect(self.paste_txt)
        self.ui.actionSelect_all.triggered.connect(self.select_all)
        self.ui.actionWord_wrap.triggered.connect(self.word_wrap)
        self.ui.fonts.triggered.connect(self.select_font)
        self.ui.actionBold.triggered.connect(self.bold_txt)
        self.ui.actionItalic.triggered.connect(self.italic_txt)
        self.ui.actionUnderline.triggered.connect(self.underline_txt)

    def open_file(self):
        filen,_ =QFileDialog.getOpenFileName(self,"Open File","","Text Files (*.txt)") 
        if filen:
            with open(filen,'r') as file:
                content = file.read()
                self.ui.txtbox.setPlainText(content)

      

    def save_file(self):
        if self.current_file:
            with open(self.current_file, 'w') as file:
                file.write(self.ui.txtbox.toPlainText())
        else:
            self.save_as()

    def save_as(self):
        filen, _ = QFileDialog.getSaveFileName(self, "Save As", "", "Text Files (*.txt)")
        if filen:
            self.current_file = filen
            with open(filen, 'w') as file:
                file.write(self.ui.txtbox.toPlainText())
   

    def new_file(self):
        self.ui.txtbox.clear()

    def close_file(self):
        reply = QMessageBox.question(self,"Exit","Are you sure.You want to exit",QMessageBox.Yes | QMessageBox.No,QMessageBox.No)
        if reply == QMessageBox.Yes:
            self.close()   


    def new_window(self):
        self.new_editor = MyNoteApp()  # if you're using custom class
        self.new_editor.show()


    def print_file(self):
        printer = QPrinter()
        dialog = QPrintDialog(printer, self)
        if dialog.exec_() == QPrintDialog.Accepted:
            self.ui.txtbox.print_(printer)

    def about_app(self):
        QMessageBox.about(self,"About My Note App","""<h3> Simple Text Editor</h3>
        <p><b>Version:</b> 1.0</p>
        <p><b>Developer:</b> Muhammad Yasir</p>
        <p><b>Built With:</b> Python 3, PyQt5</p>
        <p>For any queries, contact me at:<br>
        <a href='mailto:your.email@example.com'>yaisikhan111@gmail.com</a></p>""")        

    def undo_txt(self):
        self.ui.txtbox.undo()

    def cut_txt(self):
        self.ui.txtbox.cut()    

    def copy_txt(self):
        self.ui.txtbox.copy()

    def paste_txt(self):
        self.ui.txtbox.paste()

    def select_all(self):
        self.ui.txtbox.selectAll()           

    def delete_txt(self):
        cursor = self.ui.txtbox.textCursor()
        cursor.removeSelectedText()

    def select_font(self):
        font,ok =QtWidgets.QFontDialog.getFont()
        if ok:
            self.ui.txtbox.setCurrentFont(font)  

    def word_wrap(self):
        if self.ui.actionWord_wrap.isChecked():
            self.ui.txtbox.setLineWrapMode(QtWidgets.QTextEdit.WidgetWidth)   
        else:
            self.ui.txtbox.setLineWrapMode(QtWidgets.QTextEdit.NoWrap)  

    def bold_txt(self):
        fmt =QTextCharFormat()
        is_bold = self.ui.actionBold.isChecked()
        fmt.setFontWeight(QFont.Bold if is_bold else QFont.Normal)
        self.ui.txtbox.mergeCurrentCharFormat(fmt)

    def italic_txt(self):
        fmt = QTextCharFormat()
        fmt.setFontItalic(self.ui.actionItalic.isChecked())
        self.ui.txtbox.mergeCurrentCharFormat(fmt)

    def underline_txt(self):
        fmt = QTextCharFormat()
        fmt.setFontUnderline(self.ui.actionUnderline.isChecked())
        self.ui.txtbox.mergeCurrentCharFormat(fmt)        

if __name__ == "__main__":
    
    app = QApplication(sys.argv)
    window = MyNoteApp()     
    window.show()
    sys.exit(app.exec_())

