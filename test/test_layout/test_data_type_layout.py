from src.layout.form_bicycles_layout import create_form_page_layout
from src.layout.main_bicycles_layout import create_main_page_layout
def test_data_type_layout():
    assert isinstance(create_form_page_layout(), str)
    assert isinstance(create_main_page_layout(), str)
