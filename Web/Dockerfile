# Use Python image
FROM python:3.9

# Set working directory
WORKDIR /app

# Copy files
COPY requirements.txt requirements.txt
RUN pip install -r requirements.txt

COPY . .

# Expose Flask port
EXPOSE 8081

CMD ["python", "app.py"]

