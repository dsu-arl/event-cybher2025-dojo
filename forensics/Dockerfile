FROM ubuntu

USER root

# Install steghide
RUN apt update && apt install -y \
    steghide

RUN apt install -y unrar

RUN apt install -y python3.12




# Create hacker user with no password and set up bash env
RUN <<EOF
  if id ubuntu; then userdel -f -r ubuntu; fi
  useradd -s /bin/bash -m hacker
  passwd -d hacker

  ln -s /etc/bash.bashrc /etc/bashrc
EOF

# Add exec-suid
ADD --chown=0:0 http://github.com/pwncollege/exec-suid/releases/latest/download/exec-suid /usr/bin/exec-suid
RUN chmod 6755 /usr/bin/exec-suid

USER hacker

COPY ChallengeFiles /home/hacker