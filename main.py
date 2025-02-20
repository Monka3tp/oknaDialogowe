import sys

from PyQt6.QtWidgets import QDialog, QApplication, QInputDialog, QColorDialog, QFontDialog
from pycountry import countries

from layout import Ui_Dialog
import pycountry


class MyFrom(QDialog):
    def __init__(self):
        super().__init__()
        self.ui = Ui_Dialog()
        self.ui.setupUi(self)
        self.countries = [c.name for c in pycountry.countries]
        self.countries.sort()
        self.ui.countryButton.clicked.connect(self.display_country)
        self.index_of_Poland = self.countries.index("Poland")
        self.ui.colorButton.clicked.connect(self.display_color)
        self.ui.fontButton.clicked.connect(self.display_font)

        self.show()
    def display_font(self):
        font, ok = QFontDialog.getFont()
        if ok:
            self.ui.textEdit.setFont(font)

    def display_color(self):
        color = QColorDialog.getColor()
        if color.isValid():
            self.ui.colorLabel.setText(f'Wybrany kolor to {color.name()}')
            self.ui.colorFrame.setStyleSheet(f'QWidget {{background-color: {color.name()}}}')
            with open('kolor.txt', 'w') as plik:
                plik.write(f"R: {color.red()} G: {color.green()} B: {color.blue()}")

            hex = color.name()
            hex = hex[1:]
            red = int(hex[0:2], 16)
            green = int(hex[2:4], 16)
            blue = int(hex[4:6], 16)
            print(red, green, blue)

    def display_country(self):
        countryName, ok = QInputDialog.getItem(self, "Podaj państwa", "Państwo", self.countries, self.index_of_Poland, False)
        if ok:
            self.ui.countryEdit.setText(countryName)
        pass



if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = MyFrom()
    sys.exit(app.exec())