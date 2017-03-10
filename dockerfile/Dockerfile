
FROM peter1209/fontforge

MAINTAINER sparrow.jang <sparrow.jang@gmail.com>
ENV HOME=/root
ADD fontcustom ${HOME}/fontcustom
ADD fontGenerator ${HOME}/fontGenerator
ADD web ${HOME}/web
ADD fonts ${HOME}/fonts
RUN chmod +x ${HOME}/web/app.py
Run wget -O - https://bootstrap.pypa.io/get-pip.py | python
Run pip install -r /root/web/requirements.txt
EXPOSE 5000 

ENTRYPOINT ["/root/web/app.py"]

