#!/bin/sh

WEB_SERVER="/root/web/app.py"
HOME="/root"

echo $1
if [ ! -z "$1" ]; then
    wget -O remoteFonts.zip $1
    unzip remoteFonts.zip -d ${HOME}/fonts
fi

mkdir -p ${HOME}/fonts

$WEB_SERVER

