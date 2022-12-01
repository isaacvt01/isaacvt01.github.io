from src.layout.bicycles_layout import create_layout_bicycles_entry, create_bicycles_layout
from src.layout.details_bicycles_layout import create_bicycle_details_layout

def create_all_bicycles_page(bicycles):
    bicycles_html = ''

    for bic in bicycles:
        bicycles_html += create_layout_bicycles_entry(bic)

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