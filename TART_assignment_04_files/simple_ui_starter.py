import sys
from PyQt6.QtWidgets import QApplication, QMainWindow, QFileDialog
from batch_renamer_ui import Ui_MainWindow  # Import the generated UI module

class MainWindow(QMainWindow, Ui_MainWindow):
    def __init__(self, parent=None):
        super(MainWindow, self).__init__(parent)
        self.setupUi(self)  # Initialize the UI
        self.pushButton_browse.clicked.connect(self.browse_folders)  # Connect the button

    def browse_folders(self):
        # Open a dialog to browse folders
        # QFileDialog.getExistingDirectory() opens a dialog for directory selection
        folder_path = QFileDialog.getExistingDirectory(self, "Select Folder")
        if folder_path:
            # Here you can do something with the selected folder path
            print("Selected folder:", folder_path)

def main():
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec())

if __name__ == "__main__":
    main()