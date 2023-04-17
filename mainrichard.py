from PySide6.QtWidgets import QMainWindow, QMenuBar, QColorDialog, QFileDialog, QLabel, QVBoxLayout, QLineEdit,QPushButton
from PySide6.QtWidgets import QApplication, QLabel, QMainWindow, QVBoxLayout, QWidget
import sys


class MyMainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        # Erstellen des Haupt-Widgets
        main_widget = QWidget(self)

        # Erstellen des Layout-Managers
        self.layout = QVBoxLayout()

        # Erstelle einen QLine Edit
        self.lable1 = QLabel(self)
        self.lineedit = QLineEdit(self)
        self.lable2 = QLabel(self)
        self.lineedit1 = QLineEdit(self)
        self.Prüfung = QPushButton(self)
        self.lable3=QLabel(self)
        self.lineedit.setEchoMode(QLineEdit.EchoMode.Normal)
        self.lineedit1.setEchoMode(QLineEdit.EchoMode.Password)


        self.list=["Hans","Peter","Julia","Bert"]
        self.list2=["1234!=","AS!1","halo123!","testerino"]

        self.lable1.setText("Benutzername:")
        self.lable2.setText("Passwort:")
        #self.lineedit1.setInputMask("XXXXXX;_")
        self.Prüfung.setText("Submit")

        self.Prüfung.clicked.connect(self.test)
        # Hinzufügen der Labels zum Layout
        self.layout.addWidget(self.lable1)
        self.layout.addWidget(self.lineedit)
        self.layout.addWidget(self.lable2)
        self.layout.addWidget(self.lineedit1)
        self.layout.addWidget(self.Prüfung)
        self.layout.addWidget(self.lable3)

        # Festlegen des Layout-Managers für das Haupt-Widget
        main_widget.setLayout(self.layout)



        # Festlegen des Haupt-Widgets für das Hauptfenster
        self.setCentralWidget(main_widget)

    def test(self):
        exists=False
        index=None

        for n in self.list:
            if self.lineedit.text() == n:
                exists=True
                index=self.list.index(n)


            if exists==True:
                self.lable3.setText("Benutzername vorhanden")
            if self.lineedit1.text()==self.list2[index]:
                self.lable3.setText("passt")

            else:
                self.lable3.setText("Benutzername nicht vorhanden")


if __name__ == "__main__":
    app = QApplication(sys.argv)
    login_window = MyMainWindow()
    login_window.show()
    sys.exit(app.exec())