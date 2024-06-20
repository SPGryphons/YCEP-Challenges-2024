FROM nginx:stable-alpine

COPY git /usr/share/nginx/html/.git
COPY .htaccess /usr/share/nginx/html/.htaccess
COPY GitHub.png /usr/share/nginx/html/GitHub.png
COPY index.html /usr/share/nginx/html/index.html

COPY nginx.conf /etc/nginx/conf.d/default.conf

WORKDIR /usr/share/nginx/html

EXPOSE 80

CMD ["nginx", "-g", "daemon off;"]