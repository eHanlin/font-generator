#!/usr/bin/env python 
# -*- coding: utf-8 -*-
import sys
from os.path import realpath, dirname
from flask import Flask
from flask import request
from decorators.response_body import ResponseBody
from multiprocessing import Pool
import logging

entry_point = dirname(realpath(__file__))
project_root = entry_point + "/.."
sys.path.append(project_root) 


ROOT_PATH = "/fontGenerator"

app = Flask(__name__)

@app.route("{0}/fonts/generate".format(ROOT_PATH), methods = ["POST"])
@ResponseBody()
def generate():
    input_json = request.get_json()
    p = Pool(1)
    result = p.map(generate_base64, [input_json])[0]
    p.close()
    return result

def generate_base64(input_json):
    font_name =  input_json.get("fontName").encode("utf-8")
    input_text = input_json.get("text")
    choice_font = input_json.get("fontBase").encode("utf-8")

    input_font_path = "{0}/fonts/{1}".format(project_root, choice_font)
    from fontGenerator import generator

    return generator.generate_base64_font_face(input_font_path, list(input_text), "/tmp", font_name)


if __name__ == "__main__":
    #app.run(host = "0.0.0.0")
    processes = 10
    if len(sys.argv) > 1: processes = int(sys.argv[1])
    from werkzeug.wsgi import DispatcherMiddleware
    from werkzeug.serving import run_simple
    #app.logger.addHandler(logging.StreamHandler())
    application = DispatcherMiddleware(app)
    logging.warn("processes: {0}".format(processes))
    run_simple('0.0.0.0', 5000, application, processes = processes) 


