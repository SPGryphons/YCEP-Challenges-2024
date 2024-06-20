FROM ubuntu:22.04 AS app
FROM pwn.red/jail

COPY --from=app / /srv
COPY ./vuln /srv/app/run
COPY ./flag.txt /srv/app/flag.txt

EXPOSE 5000

RUN chmod 444 /srv/app/flag.txt
RUN chmod +x /srv/app/run