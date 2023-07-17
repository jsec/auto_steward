from pywinauto import application

from applicator import Applicator


def test_notepad(number, penalty):
    app = application.Application()
    app.start("Notepad.exe")
    app.UntitledNotepad.Edit.type_keys(f"/tp {number} {penalty}", with_spaces=True)
    app.UntitledNotepad.Edit.type_keys("{ENTER}")


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    applicator = Applicator("12")
    applicator.escalate_permissions()
    applicator.apply_penalty(45, 10)

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
