from src.presentation.view.bicycles_view import create_all_bicycles_layout
import pytest


@pytest.mark.all_bicycle_entry
def test_all_bicycle_entry():
    bicycle = {
        "model": 'test model',
        "brand": 'test addidas',
        "image": 'image.png',
        "details_link": "details/bici.html",
    }

    html = create_all_bicycles_layout(bicycle)

    assert bicycle['image'] in html
    assert bicycle['details_link'] in html
    assert bicycle['brand'] in html
    assert bicycle['model'] in html
