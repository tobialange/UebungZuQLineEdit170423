from PySide6.QtWidgets import QApplication, QMainWindow, QLabel, QLineEdit, QPushButton, QMessageBox, QGridLayout, QWidget
import sys

class LoginWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        # Set window title
        self.setWindowTitle("Login")

        # Create username label and input field
        self.username_label = QLabel("Benutzername:", self)
        self.username_input = QLineEdit(self)

        # Create password label and input field
        self.password_label = QLabel("Kennwort:", self)
        self.password_input = QLineEdit(self)
        self.password_input.setEchoMode(QLineEdit.Password)

        # Create button to submit login
        self.login_button = QPushButton("Anmelden", self)
        self.login_button.clicked.connect(self.check_login)

        # Create grid layout and add widgets to it
        self.grid_layout = QGridLayout()
        self.grid_layout.addWidget(self.username_label, 0, 0)
        self.grid_layout.addWidget(self.username_input, 0, 1)
        self.grid_layout.addWidget(self.password_label, 1, 0)
        self.grid_layout.addWidget(self.password_input, 1, 1)
        self.grid_layout.addWidget(self.login_button, 2, 1)

        # Create widget and set layout
        self.widget = QWidget()
        self.widget.setLayout(self.grid_layout)

        # Set central widget
        self.setCentralWidget(self.widget)

    def check_login(self):
        # Define a list of valid usernames and passwords
        valid_users = {
            "user1": "pass1",
            "user2": "pass2",
            "user3": "pass3"
        }

        # Get entered username and password
        username = self.username_input.text()
        password = self.password_input.text()

        # Check if username is valid
        if username in valid_users:
            # Check if password is correct
            if password == valid_users[username]:
                # Display success message in pop-up window
                QMessageBox.information(self, "Anmeldung erfolgreich", "Sie haben sich erfolgreich angemeldet.")
            else:
                # Display error message in pop-up window
                QMessageBox.warning(self, "Anmeldung fehlgeschlagen", "Das eingegebene Kennwort ist falsch.")
        else:
            # Display error message in pop-up window
            QMessageBox.warning(self, "Anmeldung fehlgeschlagen", "Der eingegebene Benutzername ist unbekannt.")

if __name__ == "__main__":
    app = QApplication(sys.argv)
    login_window = LoginWindow()
    login_window.show()
    sys.exit(app.exec())
