#!/bin/bash

currentPath=$(pwd)

while [[ $# > 0 ]]; do
    case $1 in
        -o)
         outputFont=$2
         shift
         ;;
        -i)
         inputFont=$2
         shift
         ;;
        -f)
         textFile=$2
         shift
         ;;
        --webfont)
         webFont=$2
         shift
         ;;
        --base64)
         useBase64="true"
         ;;
    esac
    shift
done

if [[ -z $outputFont || -z $inputFont || -z $textFile ]]; then
    echo "Usage: ./generate-font.sh -i input.ttf -o new_font.zip -f test/text.txt --webfont newFontName"
    echo "-o: Output font file"
    echo "-i: Input font file"
    echo "-f: You need get text file"
    echo "--webfont: Output a zip"
    echo "--base64: encode base64 to css"
else
    if [[ -z $webFont ]]; then
        docker run -e LC_CTYPE=zh_TW.UTF-8 -w /root/font-generator -v ${currentPath}:/root/font-generator -it peter1209/fontforge /root/font-generator/bin/generate-font.py $inputFont $outputFont $textFile
    else
        docker run -e LC_CTYPE=zh_TW.UTF-8 -w /root/font-generator -v ${currentPath}:/root/font-generator -it peter1209/fontforge /root/font-generator/bin/generate-font.py $webFont $inputFont $outputFont $textFile $useBase64
    fi
fi
