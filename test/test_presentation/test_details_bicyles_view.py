from src.presentation.view.details_bicycles_view import create_bicycle_details_layout


def test_create_bicycle_details_layout():
    bicycle = {
        "model": 'test model',
        "description": 'test description',
        "image": 'imagetets',
        "specifications": {
            'Cassette': 'Test Cassette',
            'Material': 'Test Material',
            'Chain': 'Test Chain',
            'Saddle': 'Test Saddle',
            'Wheels': 'Test Wheels',
            'Power': 'Test Power',
            'Fork': 'Test Fork',
            'Brakes': 'Test Brakes',
            'Frame': 'Test Frame',
            'Handlebar': 'Test Handlebar',
            'Seat post': 'Test Seat post'
        },
    }

    html = create_bicycle_details_layout(bicycle)

    assert bicycle['model'] in html
    assert bicycle['description'] in html
    assert bicycle['specifications']['Cassette'] in html
    assert bicycle['specifications']['Material'] in html
    assert bicycle['specifications']['Chain'] in html
    assert bicycle['specifications']['Saddle'] in html
    assert bicycle['specifications']['Wheels'] in html
    assert bicycle['specifications']['Power'] in html
    assert bicycle['specifications']['Fork'] in html
    assert bicycle['specifications']['Brakes'] in html
    assert bicycle['specifications']['Frame'] in html
    assert bicycle['specifications']['Handlebar'] in html
    assert bicycle['specifications']['Seat post'] in html