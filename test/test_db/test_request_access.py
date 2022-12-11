from src.presentation.tkinter.request_access import request_access
from src.presentation.tkinter.sudo_mode import sudo_mode


def test_request_acces():
    assert request_access() is None

def test_sudo_mode():
    assert sudo_mode() is None