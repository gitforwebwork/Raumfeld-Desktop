import sys
from PySide.QtGui import QApplication
from raumfeld_desktop.mainwindow import MainWindow


def main():
    application = QApplication(sys.argv)
    app = MainWindow(application)
    app.show()
    app.raise_()
    sys.exit(application.exec_())

if __name__ == "__main__":
    main()
