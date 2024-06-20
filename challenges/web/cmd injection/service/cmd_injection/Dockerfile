FROM python:3.9-slim

WORKDIR /app
COPY src/ .
RUN pip install --trusted-host pypi.python.org -r requirements.txt
RUN useradd -s /usr/sbin/nologin ctfuser
RUN chown -R root:root /app
EXPOSE 5000
ENV NAME World
RUN chmod 774 flag.txt

# Run app.py when the container launches, specifying the host and port
# Use the created user to run the application
USER ctfuser
CMD ["python", "app.py", "--host=0.0.0.0", "--port=5000"]
