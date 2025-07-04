
from PySide6.QtWidgets import QHBoxLayout, QListWidget, QMainWindow, QWidget


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Vølund - Accueil")
        self.resize(1000, 700)

        # Conteneur principal
        central_widget = QWidget()
        self.setCentralWidget(central_widget)

        # Layout principal horizontal
        layout = QHBoxLayout()
        central_widget.setLayout(layout)

        # Menu latéral (vide pour l’instant)
        self.menu_list = QListWidget()
        self.menu_list.addItem("Accueil")  # Juste un test
        layout.addWidget(self.menu_list, 1)  # 1 = ratio largeur

        # Zone de contenu
        self.content_area = QWidget()
        layout.addWidget(self.content_area, 4)  # 4 = plus large
