# -*- coding: utf-8 -*-
import uuid, zipfile, fontforge, re, os
from . import template, util


def generate( font_path, texts, output ):
    font = fontforge.open(font_path)
    new_font = fontforge.font()
    new_font.encoding = 'UnicodeFull'

    texts = util.get_content(texts)
    
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
    css = template.create_font_face(new_font_name, path)
    util.write_file( path, css )

def write_demo_page( new_font_name, texts, path ):
    html = template.create_demo_page(new_font_name, util.get_content(texts))
    util.write_file( path, html )

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

def generate_base64_font_face(font_path, texts, output, tmp_path = "", new_font_name = "new_font"):
    name = uuid.uuid1().hex
    ttf_path = "{0}/{1}.ttf".format(tmp_path, name)
    woff_path = "{0}/{1}.woff".format(tmp_path, name)
    eot_path = "{0}/{1}.eotlite".format(tmp_path, name)
    generate( font_path, texts, ttf_path)
    generate( font_path, texts, woff_path)

    eot_created = os.system('python fontcustom/lib/fontcustom/scripts/eotlitetool.py {0}'.format(ttf_path))
    return template.create_font_face_base64(new_font_name, util.read_by_base64(eot_path), util.read_by_base64(woff_path), util.read_by_base64(ttf_path))

    
#generate("pro2.ttf", [u"扯",u"不"])

