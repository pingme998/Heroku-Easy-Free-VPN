FROM debian:sid

RUN set -ex\
    && apt update -y \
    && apt upgrade -y \
    && apt install -y wget unzip qrencode\
    && apt install -y shadowsocks-libev\
    && apt install -y nginx\
    && apt autoremove -y
RUN apt install python3 -y
COPY wwwroot.tar.gz /wwwroot/wwwroot.tar.gz
COPY conf/ /conf
COPY entrypoint.sh /entrypoint.sh

RUN chmod +x /entrypoint.sh
#CMD /entryentryp
#Aria2rclone
#RUN apt update -y  && \
RUN apt install curl -y 
#RUN apt install unrar -y 
RUN apt install unzip -y  
RUN curl -O https://downloads.rclone.org/rclone-current-linux-amd64.zip 
RUN unzip rclone-current-linux-amd64.zip 
RUN cp /rclone-*-linux-amd64/rclone /usr/bin/
RUN chown root:root /usr/bin/rclone 
RUN chmod 755 /usr/bin/rclone 
RUN apt install aria2 -y 
RUN apt install wget -y 
RUN apt install pip -y 
RUN pip install jupyter
RUN pip install voila && \
    pip install ipywidgets && \
    pip install widgetsnbextension && \
    mkdir /Essential-Files && \
    mkdir /voila && \
    mkdir /voila/files
COPY Essential-Files /Essential-Files
COPY Essential-Files/index.html /usr/index.html
COPY Essential-Files/favicon.ico /voila/files/favicon.ico
COPY Essential-Files/1.htpy /1.htpy
COPY Essential-Files/2 /2
COPY Essential-Files/Ar.sh /Ar.sh
COPY Essential-Files/Aria2Rclone.jpg /Aria2Rclone.jpg
#RUN cp '/Essential-Files/jconf.py' '/conf/jconf.py'
#RUN cp '/Essential-Files/jpass.json' '/root/jpass.json'
RUN chmod +x /Ar.sh
#CMD /Ar.sh

#PYTHON TG BOT
RUN pip install python-telegram-bot
COPY bot.py /bot.py

CMD [ "python3","/bot.py" ]
