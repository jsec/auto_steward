from pywinauto import application


class Applicator:

    def __init__(self, admin_password):
        self.admin_password = admin_password
        app = application.Application()
        app.start("Notepad.exe")
        self.app = app

    def apply_penalty(self, number, penalty):
        self.app.UntitledNotepad.Edit.type_keys(f"/tp {number} {penalty}", with_spaces=True)
        self.app.UntitledNotepad.Edit.type_keys("{ENTER}")

    def escalate_permissions(self):
        self.app.UntitledNotepad.Edit.type_keys(f"/admin {self.admin_password}", with_spaces=True)
        self.app.UntitledNotepad.Edit.type_keys("{ENTER}")
