Font Generator
===================

This project is used to pick font texts.

Any font is picked to output new font for text.

## Install git module

```sh
git submodule update
```

## Install docker image

```sh
docker pull peter1209/fontforge
```

## Support input format

* ttf
* svg
* ttc
* woff

## Usage

* **-i**: Input a font file
* **-o**: Output a zip file
* **-f**: Input a text file
* **--webfont**: New font name
* **--base64**: Encode base64

**Run:**

```sh
./generate-font.sh -i Hanzipen.ttc -o webfont.zip -f text.txt --webfont fontName
```


**Output zip tree:**

```sh
fontName.tff
fontName.svg
fontName.woff
fontName.css
index.html
```

