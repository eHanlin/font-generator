
def create_demo_page(new_font_name, texts):
    css_style = "body {font-family:" + new_font_name + ";}"
    html = """
    <!DOCTYPE html>
    <html lang="en">
    <head>
        <meta charset="UTF-8">
        <title>{0}</title>
        <link rel="stylesheet" href="{0}.css">
        <style>
        {2}
        </style>
    </head>
    <body>
      {1}
    </body>
    </html>
    """.format( new_font_name, texts, css_style )

    return html


def create_font_face(new_font_name, path):
    css = """
        font-family: "{0}";
        src: url("{0}.eot");
        src: url("{0}.eot#iefix") format("embedded-opentype"),
        url("{0}.woff") format("woff"),
        url("{0}.ttf") format("truetype"),
        url("{0}.svg") format("svg");
        font-weight: normal;
        font-style: normal;
    """.format( new_font_name )
    css = "@font-face { " + css + "}"
    return css


def create_font_face_base64(font_name, opentype, woff, truetype):

    css = """ 
        font-family: "{0}";
        src: url(data:font/opentype;charset=utf-8;base64,{1}),
            url(data:font/x-font-woff;charset=utf-8;base64,{2}) format('woff'),
            url(data:font/truetype;charset=utf-8;base64,{3}) format('truetype');
        font-weight: normal;
        font-style: normal;
    """.format( font_name, opentype, woff, truetype )

    css = "@font-face { " + css + "}" 
    return css

