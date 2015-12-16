# -*- coding: utf-8 -*-
import uuid, zipfile, fontforge, re, os

def get_text_str( texts ):

    if isinstance(texts, str) or isinstance(texts, unicode):
      file_path = texts
      with open(file_path, 'r') as f:
          return list(f.read().decode("utf-8"))
          f.close()
    else:
      return texts

def write_file( path, data ):
    with open( path, "w" ) as f:
        f.write(data)
        f.close()


def generate( font_path, texts, output ):
    font = fontforge.open(font_path)
    new_font = fontforge.font()
    new_font.encoding = 'UnicodeFull'

    texts = get_text_str(texts)
    
    for text in texts:
        hex_text = hex(ord(text))
        val = hex_text.replace("0x","").upper()
        if len(val) < 4:
            for i in range(0, 4 - len(val)):
                val = "0" + val
        val = "uni" + val
        #print(text, val, texts, re.search("0x", hex_text), hex_text)
        try:
            font.selection.select(("ranges",None), val, val)
            font.copy()
            new_font.selection.select(("ranges",None), val, val)
            new_font.paste()
        except Exception as e:
            print(val, e)

    new_font.generate(output)

def write_web_font_css_file( new_font_name, path ):
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

    write_file( path, css )

def write_demo_page( new_font_name, texts, path ):
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
    """.format( new_font_name, "".join(get_text_str(texts)).encode("utf-8"), css_style )

    write_file( path, html )

def generate_web_font( font_path, texts, output, tmp_path = "", new_font_name = "new_font" ):
    name = uuid.uuid1().hex
    ttf_path = "{0}/{1}.ttf".format(tmp_path, name)
    svg_path = "{0}/{1}.svg".format(tmp_path, name)
    woff_path = "{0}/{1}.woff".format(tmp_path, name)
    css_path = "{0}/{1}.css".format(tmp_path, name)
    eot_path = "{0}/{1}.eotlite".format(tmp_path, name)
    demo_path = "{0}/index.html".format(tmp_path)
    generate( font_path, texts, ttf_path)
    generate( font_path, texts, svg_path)
    generate( font_path, texts, woff_path)
    write_web_font_css_file( new_font_name, css_path )
    write_demo_page( new_font_name, texts, demo_path )

    eot_created = os.system('python fontcustom/lib/fontcustom/scripts/eotlitetool.py {0}'.format(ttf_path))

    zipf = zipfile.ZipFile( output, "w" )
    zipf.write(ttf_path, "{0}.tff".format(new_font_name))
    if eot_created is 0: zipf.write(eot_path, "{0}.eot".format(new_font_name))
    zipf.write(svg_path, "{0}.svg".format(new_font_name))
    zipf.write(woff_path, "{0}.woff".format(new_font_name))
    zipf.write(css_path, "{0}.css".format(new_font_name))
    zipf.write(demo_path, "index.html")
    zipf.close()
    
#generate("pro2.ttf", [u"扯",u"不"])

