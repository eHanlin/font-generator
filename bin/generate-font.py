#!/usr/bin/env python

import sys
from os.path import realpath, dirname
sys.path.append( dirname(realpath(__file__)) + "/..")
from fontGenerator import generator

def main():
    if len(sys.argv) == 4:
        generator.generate( sys.argv[1], sys.argv[3].decode("utf8"), sys.argv[2] )
    elif len(sys.argv) == 5:
        generator.generate_web_font( sys.argv[2], sys.argv[4].decode("utf8"), sys.argv[3], "/tmp", sys.argv[1] )
    elif len(sys.argv) == 6:
        print(generator.generate_base64_font_face( sys.argv[2], sys.argv[4].decode("utf8"), sys.argv[3], "/tmp", sys.argv[1] ))
    else:
        print("""
        ./generate-font.py [origin font path] [file path] [output path]
        """)


if __name__ == '__main__':
    main()


