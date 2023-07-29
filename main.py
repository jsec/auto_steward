from auto_steward import AutoSteward

if __name__ == '__main__':
    steward = AutoSteward()
    AutoSteward.activate_acc_window()
    AutoSteward.raise_admin_permissions()
    AutoSteward.apply_penalty('SG', '103')
