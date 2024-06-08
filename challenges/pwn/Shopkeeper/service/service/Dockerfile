FROM debian:stable

COPY flag.txt .
COPY shop .
COPY ynetd .
RUN chmod +x shop
RUN chmod +x ynetd

EXPOSE 1337
CMD ./ynetd -p 1337 ./shop
