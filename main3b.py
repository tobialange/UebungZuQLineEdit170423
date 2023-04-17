from PySide6.QtWidgets import QApplication, QMainWindow, QLabel, QLineEdit, QPushButton, QMessageBox, QGridLayout, QWidget
import sys

class LoginWindow(QMainWindow):
    def __init__(self):
        super().__init__()


        self.setWindowTitle("Login")


        self.username_label = QLabel("Benutzername:", self)
        self.username_input = QLineEdit(self)
        self.username_input.setPlaceholderText("max. 6 Zeichen")
        #self.username_input.setMaxLength(6)
        self.username_input.setInputMask('NNNNNN')


        self.password_label = QLabel("Kennwort:", self)
        self.password_input = QLineEdit(self)
        self.password_input.setPlaceholderText("6 Zeichen")
        #self.password_input.setMaxLength(6)
        #self.password_input.setEchoMode(QLineEdit.Password)
        self.password_input.setInputMask('XXXXXX')



        self.login_button = QPushButton("Anmelden", self)
        self.login_button.clicked.connect(self.check_login)


        self.grid_layout = QGridLayout()
        self.grid_layout.addWidget(self.username_label, 0, 0)
        self.grid_layout.addWidget(self.username_input, 0, 1)
        self.grid_layout.addWidget(self.password_label, 1, 0)
        self.grid_layout.addWidget(self.password_input, 1, 1)
        self.grid_layout.addWidget(self.login_button, 2, 1)


        self.widget = QWidget()
        self.widget.setLayout(self.grid_layout)


        self.setCentralWidget(self.widget)

    def check_login(self):
        valid_users = {
            "user1": "pass1",
            "user2": "pass2",
            "user3": "pass3"
        }


        username = self.username_input.text()
        password = self.password_input.text()


        if username in valid_users:
            if password == valid_users[username]:
                QMessageBox.information(self, "Anmeldung erfolgreich", "Sie haben sich erfolgreich angemeldet.")
                #QMessageBox.setText(self, "Sie haben sich erfolgreich angemeldet.")
            else:
                QMessageBox.warning(self, "Anmeldung fehlgeschlagen", "Das eingegebene Kennwort ist falsch.")
        else:
            QMessageBox.warning(self, "Anmeldung fehlgeschlagen", "Der eingegebene Benutzername ist unbekannt.")

if __name__ == "__main__":
    app = QApplication(sys.argv)
    login_window = LoginWindow()
    login_window.show()
    sys.exit(app.exec())
