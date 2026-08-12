import sys

from PyQt6.QtWidgets import (
    QApplication,
    QComboBox,
    QHBoxLayout,
    QLabel,
    QListWidget,
    QPushButton,
    QSpinBox,
    QVBoxLayout,
    QWidget,
)

import generator


class BandNameWindow(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Band Name Generator")
        self.resize(360, 480)

        self.genre_box = QComboBox()
        self.genre_box.addItems(list(generator.GENRES))

        self.count_box = QSpinBox()
        self.count_box.setRange(1, 50)
        self.count_box.setValue(10)

        self.generate_button = QPushButton("Generate")
        self.generate_button.clicked.connect(self.on_generate)

        self.name_list = QListWidget()

        self.save_button = QPushButton("Save selected")
        self.save_button.clicked.connect(self.on_save)

        self.status = QLabel("")

        top_row = QHBoxLayout()
        top_row.addWidget(self.genre_box)
        top_row.addWidget(self.count_box)
        top_row.addWidget(self.generate_button)

        layout = QVBoxLayout()
        layout.addLayout(top_row)
        layout.addWidget(self.name_list)
        layout.addWidget(self.save_button)
        layout.addWidget(self.status)
        self.setLayout(layout)

    def on_generate(self):
        genre = self.genre_box.currentText()
        how_many = self.count_box.value()
        names = generator.generate_many(genre, how_many)
        self.name_list.clear()
        self.name_list.addItems(names)
        self.status.setText(f"{len(names)} names")

    def on_save(self):
        item = self.name_list.currentItem()
        if item is None:
            self.status.setText("Select a name first.")
            return
        name = item.text()
        if generator.save_favorite(name):
            self.status.setText(f"Saved: {name}")
        else:
            self.status.setText(f"{name} is already in your favourites.")


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = BandNameWindow()
    window.show()
    sys.exit(app.exec())