from pdf2docx import Converter
import sys
from PyQt5.QtWidgets import QApplication, QWidget, QFileDialog, QPushButton, QVBoxLayout, QMessageBox

newFile = ''

class FileCreatorApp(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        # Set up the window
        self.setWindowTitle("File Creator")
        self.setGeometry(100, 100, 300, 200)
        
        # Create a button to trigger file creation
        self.create_button = QPushButton("Create File", self)
        self.create_button.clicked.connect(self.create_file)

        # Layout setup
        layout = QVBoxLayout()
        layout.addWidget(self.create_button)
        self.setLayout(layout)

    def create_file(self):
        # Open the Save File dialog
        options = QFileDialog.Options()
        file_path, _ = QFileDialog.getSaveFileName(self, "Create File", "", "Text Files (*.docx);;All Files (*)", options=options)

        global newFile 
        newFile = file_path

        # If the user selects a file name
        if file_path:
            try:
                # Create and write to the file
                with open(file_path, 'w') as file:
                    file.write("This is a new file created using PyQt5!")
                # Show success message
                QMessageBox.information(self, "Success", f"Converted .PDF to .Docx and created at: {file_path}")

                # Create a Converter object
                global pdf_file
                cv = Converter(pdf_file)

                # Convert the PDF to DOCX
                cv.convert(newFile)

                # Close the Converter
                cv.close()
            except Exception as e:
                # Show error message if file creation fails
                QMessageBox.warning(self, "Error", f"Failed to create file: {str(e)}")

app = QApplication(sys.argv)

file_path, _ = QFileDialog.getOpenFileName(None, "Select a PDF", "", "PDF Files (*.pdf)")

#app.exit()
if file_path:
    pdf_file = file_path

    #app = QApplication(sys.argv)
    window = FileCreatorApp()
    window.show()
    sys.exit(app.exec_())

else:
    print("No file selected")


