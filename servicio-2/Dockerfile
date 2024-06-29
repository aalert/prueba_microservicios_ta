FROM python:3.12.2-alpine3.19

RUN pip install --no-cache-dir --upgrade pip

# Create a working directory
WORKDIR /app

# Copy the requirements file
COPY requirements.txt .

# Install the requirements
RUN pip install --no-cache-dir -r requirements.txt

# Copy the rest of the files
COPY ./src .

# Run the app
# CMD ["uvicorn", "main:app", "--reload", "--host", "0.0.0.0", "--port", "8000"]
