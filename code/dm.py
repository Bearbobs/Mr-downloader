from PyQt4.QtCore import *
from PyQt4.QtGui import *
import sys

import urllib.request



class downloader(QDialog):
    def __init__(self):
        QDialog.__init__(self)

        layout=QVBoxLayout()
        lab1= QLabel("                      Hi!!")
        lab2= QLabel("            I am Mr. Downloader")
        lab3= QLabel("  I can help you with your downloading   ")
        lab4= QLabel("press ctrl+j to initiate another parallel download")
        lab5= QLabel("               copyright Anuj Kapoor 2K17")
        self.url = QLineEdit()
        self.save_location = QLineEdit()
        self.progress = QProgressBar()
        browse = QPushButton("Browse")
        download = QPushButton("Download")


        self.url.setPlaceholderText("URL")
        self.save_location.setPlaceholderText("File Save Location")
        self.progress.setValue(0)
        self.progress.setAlignment(Qt.AlignHCenter)

        layout.addWidget(lab1)
        layout.addWidget(lab2)
        layout.addWidget(lab3)
        layout.addWidget(self.url)
        layout.addWidget(self.save_location)
        layout.addWidget(browse)
        layout.addWidget(self.progress)
        layout.addWidget(download)
        layout.addWidget(lab4)
        layout.addWidget(lab5)

        self.setLayout(layout)
        self.setWindowTitle("Mr.Downloader")
        self.setFocus()
        browse.clicked.connect(self.browse_file)
        download.clicked.connect(self.download)

    def browse_file(self):
        save_file = QFileDialog.getSaveFileName(self, caption="Save File As", directory=".",
                                                    filter="All Files (*.*)")
        self.save_location.setText(QDir.toNativeSeparators(save_file))

    def download(self):
        url = self.url.text()
        save_location = self.save_location.text()

        try:
            urllib.request.urlretrieve(url, save_location, self.report)
        except Exception:
            QMessageBox.warning(self, "Warning", "The download failed")
            return

        QMessageBox.information(self, "Information", "The download is complete")
        self.progress.setValue(0)
        self.url.setText("")
        self.save_location.setText("")
		
    def report(self,blocknum,blocksize,totalsize):
        a=blocknum*blocksize
        if totalsize > 0:
            percent=(a/totalsize)*100
            self.progress.setValue(int(percent))


app=QApplication(sys.argv)
dialog=downloader()
dialog.show()
app.exec_()