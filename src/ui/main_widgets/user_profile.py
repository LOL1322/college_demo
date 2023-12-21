from typing import Optional
from PySide6 import QtWidgets, QtCore, QtGui
from PySide6.QtCore import Qt
from PySide6.QtWidgets import QWidget


class UserProfile(QtWidgets.QWidget):
    def __init__(self, parent: QWidget) -> None:
        super(UserProfile, self).__init__(parent)
        self.parent = parent
        self.__init_ui()
        self.__setting_ui()

    def __init_ui(self) -> None:
        self.main_v_layout = QtWidgets.QVBoxLayout()
        self.id_h_layout = QtWidgets.QHBoxLayout()
        self.type_id_h_layout = QtWidgets.QHBoxLayout()
        self.group_id_h_layout = QtWidgets.QHBoxLayout()
        self.login_h_layout = QtWidgets.QHBoxLayout()
        self.password_h_layout = QtWidgets.QHBoxLayout()
        self.confirm_h_layout = QtWidgets.QHBoxLayout()
        self.buttons_layout = QtWidgets.QHBoxLayout()

        self.spacer = QtWidgets.QSpacerItem(0, 10)

        self.id_label = QtWidgets.QLabel(text='ID: ')
        self.type_id_label = QtWidgets.QLabel(text='Type ID: ')
        self.group_id_label = QtWidgets.QLabel(text='Group ID: ')
        self.login_label = QtWidgets.QLabel(text='Login: ')
        self.password_label = QtWidgets.QLabel(text='Password: ')
        self.confirm_label = QtWidgets.QLabel(text='Confirm: ')

        self.id_line_edit = QtWidgets.QLineEdit()
        self.type_id_line_edit = QtWidgets.QLineEdit()
        self.group_id_line_edit = QtWidgets.QLineEdit()
        self.login_line_edit = QtWidgets.QLineEdit()
        self.password_line_edit = QtWidgets.QLineEdit()
        self.confirm_line_edit = QtWidgets.QLineEdit()

        self.allow_button = QtWidgets.QPushButton(text='Allow')
        self.edit_button = QtWidgets.QPushButton(text='Edit')
        self.leave_button = QtWidgets.QPushButton(text='Leave')
        self.delete_button = QtWidgets.QPushButton(text='Delete')
    
    def __setting_ui(self) -> None:
        self.setLayout(self.main_v_layout)
        self.setContentsMargins(0, 0, 0, 0)
        self.main_v_layout.setAlignment(QtCore.Qt.AlignmentFlag.AlignTop)
        self.setMaximumWidth(250)

        self.main_v_layout.addLayout(self.id_h_layout)
        self.main_v_layout.addLayout(self.type_id_h_layout)
        self.main_v_layout.addLayout(self.group_id_h_layout)
        self.main_v_layout.addSpacerItem(self.spacer)
        self.main_v_layout.addLayout(self.login_h_layout)
        self.main_v_layout.addLayout(self.password_h_layout)
        self.main_v_layout.addLayout(self.confirm_h_layout)
        self.main_v_layout.addSpacerItem(self.spacer)
        self.main_v_layout.addLayout(self.buttons_layout)
        
        self.id_h_layout.addWidget(self.id_label)
        self.type_id_h_layout.addWidget(self.type_id_label)
        self.group_id_h_layout.addWidget(self.group_id_label)
        self.login_h_layout.addWidget(self.login_label)
        self.password_h_layout.addWidget(self.password_label)
        self.confirm_h_layout.addWidget(self.confirm_label)

        self.id_h_layout.addWidget(self.id_line_edit)
        self.type_id_h_layout.addWidget(self.type_id_line_edit)
        self.group_id_h_layout.addWidget(self.group_id_line_edit)
        self.login_h_layout.addWidget(self.login_line_edit)
        self.password_h_layout.addWidget(self.password_line_edit)
        self.confirm_h_layout.addWidget(self.confirm_line_edit)

        self.buttons_layout.addWidget(self.delete_button)
        self.buttons_layout.addWidget(self.leave_button)
        self.buttons_layout.addWidget(self.edit_button)
        self.buttons_layout.addWidget(self.allow_button)

        self.id_line_edit.setFixedWidth(150)
        self.type_id_line_edit.setFixedWidth(150)
        self.group_id_line_edit.setFixedWidth(150)
        self.login_line_edit.setFixedWidth(150)
        self.password_line_edit.setFixedWidth(150)
        self.confirm_line_edit.setFixedWidth(150)

        [line_edit.setEnabled(False) for line_edit in (self.id_line_edit, self.type_id_line_edit, self.login_line_edit, self.password_line_edit, self.confirm_line_edit, self.group_id_line_edit)]
        
        [line_edit.setEchoMode(QtWidgets.QLineEdit.EchoMode.Password) for line_edit in (self.password_line_edit, self.confirm_line_edit)]

        self.allow_button.setEnabled(False)

        [button.clicked.connect(func) for button, func in zip((self.delete_button, self.leave_button, self.edit_button, self.allow_button), (self.on_delete_button_click, self.on_leave_button_click, self.on_edit_button_click, self.on_allow_button_click))]

    def on_delete_button_click(self) -> None:
        if QtWidgets.QMessageBox.question(self, 'Info', 'Are you sure?') != QtWidgets.QMessageBox.StandardButton.Yes:
            return
        self.parent.session.delete()
        self.parent.leave()
        self.parent.show_message(text='Succesfully delete account', parent=self)
    
    def fill_line_edits(self) -> None:
        self.id_line_edit.setText(str(self.parent.session.user.ID))
        self.type_id_line_edit.setText(str(self.parent.session.user.type_id))
        self.login_line_edit.setText(self.parent.session.user.login)
        self.group_id_line_edit.setText(str(self.parent.session.user.group_id))

    def on_leave_button_click(self) -> None:
        self.parent.leave()
    
    def on_edit_button_click(self) -> None:
        self.switch_line_edits(True)
        self.allow_button.setEnabled(True)
        self.edit_button.setEnabled(False)

    def switch_line_edits(self, enabled: bool) -> None:
        self.password_line_edit.setEnabled(enabled)
        self.confirm_line_edit.setEnabled(enabled)

    def data_is_valid(self) -> bool:
        if self.password_line_edit.text() != self.confirm_line_edit.text():
            self.parent.show_message(text='Incorrect confirm password', error=True, parent=self)
            return False

        for x in (self.password_line_edit, self.confirm_line_edit):
            if x.text() == '': 
                self.parent.show_message(text='One or more fields are empty', error=True, parent=self)
                return False
        
        return True
    
    def on_allow_button_click(self) -> None:
        if not self.data_is_valid():
            return
        
        self.parent.session.update(password=self.password_line_edit.text())

        self.parent.show_message(text=self.parent.session.error if self.parent.session.error else 'Succesfully', error=True if self.parent.session.error else False, parent=self)
        if not self.parent.session.error:
            self.edit_button.setEnabled(True)
            self.allow_button.setEnabled(False)

            self.password_line_edit.setText('')
            self.confirm_line_edit.setText('')

            self.switch_line_edits(False)
