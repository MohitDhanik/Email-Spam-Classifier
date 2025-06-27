# Use a specific Python version
FROM python:3.11.9-slim

# Set the working directory
WORKDIR /app

# Copy the entire project into the container
COPY . .

# Install required Python packages
RUN pip install --upgrade pip
RUN pip install -r requirements.txt
RUN python -m nltk.downloader punkt


# Expose port 8000 for the web service
EXPOSE 8000

# Start the Flask app using gunicorn
CMD ["gunicorn", "app:app", "--bind", "0.0.0.0:8000"]
