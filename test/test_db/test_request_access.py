from src.presentation.tkinter.login import login
from src.presentation.tkinter.dashboard import dashboard


def test_request_acces():
    assert login() is None

def test_sudo_mode():
    assert dashboard() is None