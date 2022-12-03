from src.layout.bicycles_layout import create_all_bicycles_layout, create_bicycles_layout
from src.layout.details_bicycles_layout import create_bicycle_details_layout
from src.layout.main_bicycles_layout import create_main_page_layout

def create_all_bicycles_page(bicycles):
    bicycles_html = ''

    for bic in bicycles:
        bicycles_html += create_all_bicycles_layout(bic)

    html = create_bicycles_layout(bicycles_html)

    with open("../presentation/bicycles.html", "w") as external_file:
        print(html, file=external_file)
        external_file.close()

def create_detail_pages(bicycles):
    for bic in bicycles:
        html = create_bicycle_details_layout(bic)

        file_name = bic['model'].replace(' ', '-') + bic["id"]
        with open(f"../presentation/details/{file_name}.html", "w") as external_file:
            print(html, file=external_file)
            external_file.close()

def create_main_page():
    html = create_main_page_layout()

    with open("../presentation/index.html", "w") as external_file:
        print(html, file=external_file)
        external_file.close()

