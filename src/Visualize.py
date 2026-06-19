import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QVBoxLayout, QWidget, QListWidget, QPushButton
from PyQt5.QtCore import Qt
import psycopg2

class DatabaseViewer(QMainWindow):
    def __init__(self):
        super().__init__()
        self.init_ui()


    def init_ui(self):
        self.setWindowTitle('Database Viewer')
        self.setGeometry(100, 100, 400, 300)

        # Create layout
        layout = QVBoxLayout()

        # List widget to display data
        self.data_list = QListWidget()
        layout.addWidget(self.data_list)

        # Button to fetch data
        self.fetch_button = QPushButton('Fetch Data')
        self.fetch_button.clicked.connect(self.fetch_data)
        layout.addWidget(self.fetch_button)

        container = QWidget()
        container.setLayout(layout)
        self.setCentralWidget(container)

    def fetch_data(self):
        return self.data_list
