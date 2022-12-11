from src.presentation.view.bicycles_view import create_all_bicycles_layout


def test_all_bicycle_entry():
    bicycles = {
        "model": 'test model',
        "brand": 'test addidas',
        "image": 'image.png',
        "details_link": "details/bici.html",
    }

    html = create_all_bicycles_layout(bicycles)

    assert bicycles['image'] in html
    assert bicycles['details_link'] in html
    assert bicycles['brand'] in html
    assert bicycles['model'] in html
