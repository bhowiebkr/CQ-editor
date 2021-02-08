import sys
import os
import argparse

from PyQt5.QtWidgets import QApplication
import qdarkstyle

os.environ['QT_API'] = 'pyqt5'

NAME = 'CQ-editor'

#need to initialize QApp here, otherewise svg icons do not work on windows
app = QApplication(sys.argv,
                   applicationName=NAME)

from .main_window import MainWindow

def main():

    win = MainWindow()

    parser = argparse.ArgumentParser(description=NAME)
    parser.add_argument('filename',nargs='?',default=None)

    args = parser.parse_args(app.arguments()[1:])
    print(args)
    if args.filename:
        win.components['editor'].load_from_file(args.filename)

    win.show()

    app.setStyleSheet(qdarkstyle.load_stylesheet())
    sys.exit(app.exec_())


if __name__ == "__main__":

    main()
