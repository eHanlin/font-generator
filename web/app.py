#!/usr/bin/env python 
# -*- coding: utf-8 -*-
import sys
from os.path import realpath, dirname
from flask import Flask
from flask import request
from decorators.response_body import ResponseBody

entry_point = dirname(realpath(__file__))
project_root = entry_point + "/.."
sys.path.append(project_root) 

from fontGenerator import generator

ROOT_PATH = "/fontGenerator"

app = Flask(__name__)

@app.route("{0}/fonts/generate".format(ROOT_PATH), methods = ["POST"])
@ResponseBody()
def generate():
    input_json = request.get_json()
    font_name =  input_json.get("fontName").encode("utf-8")
    input_text = input_json.get("text")
    choice_font = input_json.get("fontBase").encode("utf-8")

    input_font_path = "{0}/fonts/{1}".format(project_root, choice_font)

    return generator.generate_base64_font_face(input_font_path, list(input_text), "/tmp", font_name)


if __name__ == "__main__":
    app.run(host = "0.0.0.0")


