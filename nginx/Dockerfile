FROM nginx:latest

ENTRYPOINT [ "nginx" ]

COPY ./nginx/api-gateway.conf /etc/nginx/templates/
COPY ./nginx/api-gateway.conf /etc/nginx/conf.d/
EXPOSE 80
CMD [ "-g", "daemon off;" ]