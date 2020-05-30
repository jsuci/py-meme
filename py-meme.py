from PyQt5.QtWidgets import (
    QApplication,
    QWidget,
    QLabel,
    QPushButton)
from sys import argv


class MainWindow(QWidget):
    # No longer inherit from init's parent class
    def __init__(self):
        # Inherit only the __init__ of parent class
        # QWidget.__init__(self)

        # Inherit all the properties and methods of
        # parent class
        super().__init__()


def main():
    app = QApplication(argv)
    main_window = MainWindow()

    main_window.show()
    app.exec()


# Prevent (certain) code from being run when the module is imported
if __name__ == "__main__":
    main()
