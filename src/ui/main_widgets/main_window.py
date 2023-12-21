
from PySide6 import QtWidgets, QtCore, QtGui
import multiprocessing
from start_server import start_server
from src.ui.api.session import Session
from src.ui.main_widgets import user_profile, authorization_menu


class MainWindow(QtWidgets.QMainWindow):
    session: Session = Session()
    def __init__(self) -> None:
        super(MainWindow, self).__init__()
        self.__start_server_process()
        self.__init_ui()
        self.__setting_ui()
        self.show()

    def __start_server_process(self) -> None:
        self.server_process = multiprocessing.Process(target=start_server)
        self.server_process.start()
        while not self.session.server_available:
            self.session.check_connection()
    
    def __init_ui(self) -> None:
        self.central_widget = QtWidgets.QWidget()
        self.main_h_layout = QtWidgets.QHBoxLayout()
        self.authorization_menu = authorization_menu.AuthorizationMenu(self)
        self.user_profile = user_profile.UserProfile(self)

    
    def __setting_ui(self) -> None:
        self.setCentralWidget(self.central_widget)
        self.central_widget.setLayout(self.main_h_layout)
        self.main_h_layout.setContentsMargins(0, 0, 0, 0)
        
        self.main_h_layout.addWidget(self.authorization_menu)
        self.main_h_layout.addWidget(self.user_profile)

        self.user_profile.hide()
    
    def authorization(self) -> None:
        self.authorization_menu.hide()
        self.user_profile.show()
        self.user_profile.fill_line_edits()
    
    def leave(self) -> None:
        self.user_profile.hide()
        self.authorization_menu.show()
        self.session.leave()

    def show_message(self, text: str, error: bool = False, parent=None) -> None:
        message_box = QtWidgets.QMessageBox(parent=self if not parent else parent)
        message_box.setStandardButtons(QtWidgets.QMessageBox.StandardButton.Ok)
        message_box.setWindowTitle('Error' if error else 'Information')
        message_box.setText(text)
        message_box.setIcon(QtWidgets.QMessageBox.Icon.Critical if error else QtWidgets.QMessageBox.Icon.Information)
        message_box.exec_()

    def close_func(self) -> None:
        self.expedition_stop_flag = True
        self.server_process.terminate()
        self.close()
        exit()
    
    def show_message(self, text: str, error: bool = False, parent=None) -> None:
        message_box = QtWidgets.QMessageBox(parent=self if not parent else parent)
        message_box.setStandardButtons(QtWidgets.QMessageBox.StandardButton.Ok)
        message_box.setWindowTitle('Error' if error else 'Information')
        message_box.setText(text)
        message_box.setIcon(QtWidgets.QMessageBox.Icon.Critical if error else QtWidgets.QMessageBox.Icon.Information)
        message_box.exec_()

    def close_func(self) -> None:
        self.expedition_stop_flag = True
        self.server_process.terminate()
        self.close()
        exit()

    def closeEvent(self, event: QtGui.QCloseEvent) -> None:
        self.close_func()