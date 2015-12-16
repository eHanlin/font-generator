FROM peter1209/fontforge

MAINTAINER sparrow.jang <sparrow.jang@gmail.com>
ENV HOME=/root SERVICE_TAGS=fontforge
COPY ../bin ${HOME}/bin
COPY ../fontGenerator  ${HOME}/fontGenerator
COPY cmd.sh ${HOME}/cmd.sh
RUN chmod +x ${HOME}/cmd.sh
 
ENTRYPOINT ["/root/cmd.sh"]

