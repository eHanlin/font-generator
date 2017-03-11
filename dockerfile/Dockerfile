
FROM peter1209/fontforge

MAINTAINER sparrow.jang <sparrow.jang@gmail.com>
ENV HOME=/root
ADD dockerfile/entryPoint.sh ${HOME}/entryPoint.sh
ADD fontcustom ${HOME}/fontcustom
ADD fontGenerator ${HOME}/fontGenerator
ADD web ${HOME}/web
ADD fonts ${HOME}/fonts
RUN apt-get install -y unzip
RUN chmod +x ${HOME}/web/app.py ${HOME}/entryPoint.sh
Run wget -O - https://bootstrap.pypa.io/get-pip.py | python
Run pip install -r /root/web/requirements.txt
EXPOSE 5000 

ENTRYPOINT ["/root/entryPoint.sh"]

