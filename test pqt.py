# pyuic5 -x untitled.ui -o foo.py
from foo import *

def say_hello(a):
 print("Button clicked, Hello!")


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Dialog = QtWidgets.QDialog()
    ui = Ui_Dialog()


    ui.setupUi(Dialog)
    # ui.tableWidget.clearContents()
    ui.tableWidget.cellPressed.connect(lambda x:print(ui.tableWidget.cellClicked.row()))
    ui.Press.clicked.connect(ui.tableWidget.clearContents)
    Dialog.show()
    sys.exit(app.exec_())