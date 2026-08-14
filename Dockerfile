# 1. Choose a base image (Python 3.9 slim version to keep it small)
FROM python:3.12-slim

# 2. Set the working directory inside the container
WORKDIR /code

# 3. Copy the requirements file first (Docker caches this step!)
COPY requirements.txt .

# 4. Install dependencies
RUN pip install --no-cache-dir -r requirements.txt

# 5. Copy the rest of the application code
COPY . .

# 6. Tell Docker what command to run when the container starts
CMD ["python", "app.py"]

