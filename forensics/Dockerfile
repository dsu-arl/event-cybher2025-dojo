FROM ubuntu

USER root
RUN apt update
RUN apt install python3.12 -y
RUN apt update && apt install -y \
    steghide

RUN apt install -y zip

RUN apt install -y exiftool binwalk

# Add exec-suid to the image (important for Python challenges to be able to read the flag):
ADD --chown=0:0 http://github.com/pwncollege/exec-suid/releases/latest/download/exec-suid /usr/bin/exec-suid
RUN chmod 6755 /usr/bin/exec-suid

COPY hidden-treasures-in-the-picture/treasure.jpg home/ubuntu/Hidden-Treasure-in-Picture
RUN chown ubuntu: /home/ubuntu/Hidden-Treasure-in-Picture/treasure.jpg

COPY secret-message-in-photo/suspicious_doggo.jpg /home/ubuntu/Secret-Message-in-Photo
RUN chown ubuntu: /home/ubuntu/Secret-Message-in-Photosuspicious_doggo.jpg

COPY secret-message-in-photo/secret.txt /home/ubuntu/Secret-Message-in-Photo
RUN chown ubuntu: /home/ubuntu/Secret-Message-in-Photosecret.txt

COPY chatty-server/server.log /home/ubuntu/Chatty-Server
RUN chown ubuntu: /home/ubuntu/Chatty-Server/server.log

COPY code-cracker/secret.bin /home/ubuntu/Code-Cracker
RUN chown ubuntu: /home/ubuntu/Code-Cracker/secret.bin

USER hacker