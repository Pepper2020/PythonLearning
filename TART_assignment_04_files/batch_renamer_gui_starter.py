import sys
import os
from PyQt6.QtWidgets import QFileDialog, QMainWindow, QApplication
from PyQt6.QtCore import *
# You'll need to make this ui in QtDesigner
# And convert it to a .py file using the MakeUIPy.bat file
from batch_renamer_ui import Ui_MainWindow 
# Recommend you rename this
import batch_renamer_starter

class BatchRenamerWindow(QMainWindow, Ui_MainWindow):
    def __init__(self):
        # UI Setup
        super().__init__()
        super(Ui_MainWindow).__init__()
        self.setupUi(self)
        # Connect button to function
        self.pushButton_browse.clicked.connect(self.get_filepath)
        # Connect your new "Run" button to self.run_renamer

        # Instance the "back end"
        self.batch_renamer = batch_renamer_starter.BatchRenamer()
        
        # Show UI normal vs maximized
        self.showNormal()

        


    def get_filepath(self):
        """
        Open a file dialog for browsing to a folder
        """
        self.filepath = QFileDialog().getExistingDirectory()
        self.set_filepath()


    def set_filepath(self):
        """
        Set lineEdit text for filepath
        """
        self.lineEdit_filepath.setText(self.filepath)
        self.update_list()


    def update_list(self):
        """
        Clear listwidget
        read files in filepath with os.walk
        Add files as new items
        """
        self.listWidget.clear()
        for root, dirs, files in os.walk(self.filepath):
            self.listWidget.addItems(files)
            self.listWidget.addItems(dirs)
            #self.listWidget.addItems(root)
        self.listWidget.sortItems()


    # Add a function to gather and set parameters based upon UI
    # e.g. lineEdit.text() or radioButton.isChecked
    # remember that you may need to check to see if the result
    # was a tuple and correct like so:
    # self.filepath = self.filepathEdit.text()
    # if type(self.filepath) is tuple:
    #     self.filepath = self.filepath[0]

    def run_renamer(self):
        """
        Run back end batch renamer using self.batch_renamer
        self.batch_renamer is an instance of the BatchRenamer class
        """
        # unction call to Gather Parameters
        self.batch_renamer.process_folder()
        # If new_folder is used, change filepath to new_folder
        # Update List Widget
        self.set_filepath()


if __name__ == '__main__':
    try:
        app = QApplication(sys.argv)
        window = BatchRenamerWindow()
        sys.exit(app.exec())
    except Exception as e:
        print(e)
        sys.exit(1)    
 