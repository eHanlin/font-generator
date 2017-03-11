Font Generator
===================

This project is used to extract fonts.

It minify font's size when you don't need full fonts.

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

See [dockerhub](https://hub.docker.com/r/peter1209/font-generator-server/) if you need use **web server**.

## Build dockerfile of web server

```sh
docker build --no-cache -t peter1209/font-generator-server -f dockerfile/Dockerfile .
```

