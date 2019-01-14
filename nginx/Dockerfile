FROM nginx
# Add the Nginx configuration file
ADD ./nginx/nginx.conf /etc/nginx/nginx.conf
# Copy over static assets from the frontend application manually
COPY ./nba_news_frontend/dist /usr/share/nginx/html