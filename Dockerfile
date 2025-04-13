# Step 1: Use an official Python base image
FROM python:3.9-slim

# Step 2: Set environment variables
ENV PYTHONUNBUFFERED=1 \
    STREAMLIT_SERVER_PORT=8501

# Step 3: Create working directory
WORKDIR /app

# Step 4: Copy project files
COPY . .

# Step 5: Install system dependencies
RUN apt-get update && apt-get install -y --no-install-recommends \
    git \
    build-essential \
    && rm -rf /var/lib/apt/lists/*

# Step 6: Install Python dependencies
RUN pip install --upgrade pip && \
    pip install -r requirements.txt

# Step 7: Expose the Streamlit port
EXPOSE 8501

# Step 8: Define the command to run the application
CMD ["streamlit", "run", "app.py", "--server.port=8501", "--server.address=0.0.0.0"]