from src.logic.page_builder import create_all_bicycles_page
from src.db.query_bicycles import get_bicycles_data



if __name__ == "__main__":
    bicycles = get_bicycles_data()

    create_all_bicycles_page(bicycles)