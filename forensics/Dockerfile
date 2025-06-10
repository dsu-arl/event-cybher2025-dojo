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
 
USER hacker

COPY hidden-treasures-in-the-picture/treasure.jpg home/hacker