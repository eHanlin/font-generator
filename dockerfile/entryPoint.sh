#!/bin/bash

WEB_SERVER="/root/web/app.py"
HOME="/root"

processes=1

extractFontByURL(){
    wget -O remoteFonts.zip $1
    unzip -o remoteFonts.zip -d ${HOME}/fonts
    echo "extract $1 to ${HOME}/fonts"
}

if [[ $# = 1 ]]; then
    fontURL=$1
fi

while [[ $# > 1 ]]; do
    case $1 in
      -font-url)
        fontURL=$2
        shift
        ;;  
      -processes)
        processes=$2
        shift
        ;;  
    esac
    shift
done


mkdir -p ${HOME}/fonts

echo $fontURL
if [[ ! -z "$fontURL" ]]; then
    extractFontByURL $fontURL
fi

$WEB_SERVER $processes

