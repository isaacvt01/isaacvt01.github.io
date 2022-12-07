from src.logic.page_builder import create_main_page
from src.logic.page_builder import create_all_bicycles_page
from src.logic.page_builder import create_detail_pages
from src.db.query_bicycles import get_bicycles_data
from src.logic.page_builder import create_brand_pages
from src.logic.page_builder import create_type_main_page

if __name__ == "__main__":
    bicycles = get_bicycles_data()

    create_main_page()

    create_all_bicycles_page(bicycles)

    create_detail_pages(bicycles)

    create_brand_pages(bicycles)

    create_type_main_page(bicycles)

    create_type_main_page(bicycles)
