FROM debian:stable

RUN apt update && \
    apt install -y socat

EXPOSE 10003

CMD ["socat", "TCP-LISTEN:10003,reuseaddr,fork", "EXEC:echo 'YCEP24{hELlo_From_NE7Cat}'"]