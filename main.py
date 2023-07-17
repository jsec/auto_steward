from pywinauto import application

def test_notepad():
    app = application.Application()
    app.start("Notepad.exe")
    app.UntitledNotepad.Edit.type_keys("pywinauto Works!", with_spaces=True)


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    test_notepad()

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
