FROM nginx:1.15.12-alpine

RUN rm /etc/nginx/conf.d/default.conf
COPY nginx.conf /etc/nginx/conf.d

CMD sed -i -e 's/$PORT/'"$PORT"'/g' /etc/nginx/conf.d/nginx.conf && nginx -g 'daemon off;'
