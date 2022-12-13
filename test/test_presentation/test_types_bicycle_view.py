from src.presentation.view.types_bicycle_view import create_type_entry


def test_create_type_bic_entry():
    type_name = 'Testtype'

    html = create_type_entry(type_name)

    assert type_name in html
    assert f'./assets/images/types/{type_name}.jpg' in html
