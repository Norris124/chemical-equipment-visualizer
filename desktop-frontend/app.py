import sys
import requests
from PyQt5.QtWidgets import QApplication, QWidget, QVBoxLayout, QPushButton, QFileDialog
import matplotlib.pyplot as plt

class App(QWidget):
    def __init__(self):
        super().__init__()
        self.setLayout(QVBoxLayout())

        btn = QPushButton("Upload CSV")
        btn.clicked.connect(self.upload)
        self.layout().addWidget(btn)

    def upload(self):
        path, _ = QFileDialog.getOpenFileName(self)
        files = {'file': open(path, 'rb')}
        headers = {}
        res = requests.post("http://127.0.0.1:8000/api/upload/", files=files, headers=headers)
        data = res.json()

        plt.bar(data['type_distribution'].keys(), data['type_distribution'].values())
        plt.show()

app = QApplication(sys.argv)
window = App()
window.show()
sys.exit(app.exec())
