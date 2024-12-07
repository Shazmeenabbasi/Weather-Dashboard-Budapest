# Use an official Node.js runtime (or a simple HTTP server)
FROM node:18

# Set the working directory
WORKDIR /app

# Copy frontend files
COPY . .

# Expose port 3000 for the frontend
EXPOSE 3000
CMD ["npx", "serve", "."]
