FROM ubuntu:22.04

RUN apt-get update && apt-get install -y \
    openssh-server \
    python3 \
    python3-pip \
    less \
    dos2unix \
&& rm -rf /var/lib/apt/lists/*

COPY ./flag.txt ./helpme.py /home/ycep24/
RUN dos2unix /home/ycep24/helpme.py && chmod +x /home/ycep24/helpme.py
RUN useradd -ms /home/ycep24/helpme.py ycep24
RUN echo "ycep24:ycep24" | chpasswd

RUN mkdir /var/run/sshd 
RUN sed -i 's/#PasswordAuthentication/PasswordAuthentication/g' /etc/ssh/sshd_config
RUN sed -i 's/#Port 22/Port 1337/g' /etc/ssh/sshd_config
RUN chmod -x /etc/update-motd.d/*

EXPOSE 1337
CMD ["/usr/sbin/sshd", "-D", "-e"]