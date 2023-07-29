from ahk import AHK
import pyautogui


class AutoSteward:
    @staticmethod
    def activate_acc_window():
        ahk = AHK()
        win = ahk.find_window_by_title('AC2', title_match_mode=1)
        win.activate()

    @staticmethod
    def raise_admin_permissions():
        pyautogui.press('enter')
        pyautogui.write('/admin SRAtestadmin', interval=0.1)
        pyautogui.press('enter')

    @staticmethod
    def apply_penalty(penalty_type, driver_number):
        pyautogui.press('enter')
        pyautogui.write('/tp5 103', interval=0.1)
        pyautogui.press('enter')
