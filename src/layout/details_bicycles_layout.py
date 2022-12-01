def create_bicycle_details_layout(bicycles):
    details_html = f"""
        <div>
            <img src="{bicycles['image']}">
            <div>{bicycles["model"]}</div>
            <div>{bicycles["description"]}</div>
            <div>{bicycles["specifications"]}</div>
        </div>
     """

    html = f"""<!DOCTYPE html>
        <html lang="en">
            <head>
                <meta charset="UTF-8"/>
                <link rel="stylesheet" type="text/css" href="assets/css/style.css">
                <title> Details page </title>
            </head>
            <body>
            <section>
                {details_html}
            </section>
            </body>
        </html>"""

    return html