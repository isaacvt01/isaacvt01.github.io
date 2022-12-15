import pytest


@pytest.mark.create_type_bic_entry
def test_read_types():
    with open('docs/types_main.html', 'r') as types_main_file:
        read_main_types = types_main_file.read()
        assert '<html' in read_main_types
        assert '<meta' in read_main_types
        assert '<section' in read_main_types
        assert '<div' in read_main_types


@pytest.mark.read_index
def test_read_index():
    with open('docs/index.html', 'r') as index_file:
        read_index = index_file.read()
        assert '<html' in read_index
        assert '<meta' in read_index
        assert '<section' in read_index
        assert '<div' in read_index


@pytest.mark.read_brands
def test_read_brands():
    with open('docs/brands_main.html', 'r') as brand_file:
        read_brand = brand_file.read()
        assert '<html' in read_brand
        assert '<meta' in read_brand
        assert '<section' in read_brand
        assert '<div' in read_brand
        assert 'while i <= 90:' not in read_brand


@pytest.mark.read_form
def test_read_form():
    with open('docs/form.html', 'r') as form_file:
        read_form = form_file.read()
        assert '<html' in read_form
        assert '<meta' in read_form
        assert '<section' in read_form
        assert '<div' in read_form
        assert 'for i in bicycles' not in read_form
