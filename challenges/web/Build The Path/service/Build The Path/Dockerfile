FROM httpd:2.4.50

COPY flag.txt /root

COPY index.html /usr/local/apache2/htdocs/
COPY YCEP_Logo.png /usr/local/apache2/htdocs/
COPY httpd.conf /usr/local/apache2/conf/

RUN chmod a+x /root

EXPOSE 1337
