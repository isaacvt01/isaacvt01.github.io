from src.logic.page_builder import create_main_page
from src.logic.page_builder import create_all_bicycles_page
from src.logic.page_builder import create_detail_pages
from src.db.read.read_bicycles import get_bicycles_data
from src.logic.page_builder import create_brand_pages
from src.logic.page_builder import create_type_main_page
from src.logic.page_builder import create_form_page
from src.logic.git_automatization import git_commit, git_add, git_push

if __name__ == "__main__":
    bicycles = get_bicycles_data()

    create_main_page()

    create_all_bicycles_page(bicycles)

    create_detail_pages(bicycles)

    create_brand_pages(bicycles)

    create_type_main_page(bicycles)

    create_form_page()

    git_add()

    git_commit()

    git_push()
