from src.presentation.view.brands_bicycle_view import create_brands_layout, create_brands_entry


def test_create_brands_layout():
    brand_name = 'Adidas'

    html = create_brands_layout(brand_name)

    assert brand_name in html
    assert f'./assets/images/brands/{brand_name}.jpg' in html


def test_create_brands_entry():
    bic = {
        'details_link': 'details-link.html',
        'model': 'Model Test'
    }

    html = create_brands_entry(bic)

    assert bic['details_link'] in html
    assert bic['model'] in html