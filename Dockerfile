FROM python:3.7-slim

# Install dependencies
RUN apt-get update && apt-get install -y \
    ansible \
&& rm -rf /var/lib/apt/lists/*

# Copy the code into the image
COPY . /app
WORKDIR /app

# Install the Python packages
RUN pip install -r requirements.txt

# Run the tool
CMD ["bash", "run.sh"]
