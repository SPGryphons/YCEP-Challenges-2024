FROM ubuntu:22.04

RUN apt-get update && apt-get install -y \
    openssh-server \
    net-tools

RUN groupadd --gid 1000 ycep24 && \
    useradd -rm -d /home/ycep24 -s /bin/bash -g ycep24 -u 1000 ycep24 && \
    echo 'ycep24:ycep24' | chpasswd 

RUN sed -i 's/#Port 22/Port 2222/' /etc/ssh/sshd_config

COPY flag.txt /root
RUN chmod 4755 /usr/bin/date
RUN chmod a-w /tmp /home/ycep24
RUN chown -R root:root /home/ycep24
RUN mkdir /run/sshd && chown root:root /run/sshd && chmod 0755 /run/sshd

EXPOSE 2222
CMD ["/usr/sbin/sshd", "-D"]
