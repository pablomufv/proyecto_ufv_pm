# Start from a base Ubuntu image
FROM ubuntu:latest

# Install SQLite
RUN apt-get update && apt-get install -y sqlite3 libsqlite3-dev

# Copy in your database file (if you have one)
COPY mydb.db /root/mydb.db

# Set the default command to run when starting a container from this image
CMD ["sqlite3", "/root/mydb.db"]