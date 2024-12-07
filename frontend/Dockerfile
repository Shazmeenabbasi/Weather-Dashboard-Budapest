# Use an official Node.js runtime for serving static files
FROM nginx:alpine

# Copy the static files to the NGINX web directory
COPY . /usr/share/nginx/html

# Expose the NGINX port
EXPOSE 80

# Start NGINX
CMD ["nginx", "-g", "daemon off;"]
