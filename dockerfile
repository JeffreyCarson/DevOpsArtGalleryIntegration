FROM python:3.9.13

WORKDIR /app

COPY . /app

RUN apt-get update && \
    apt-get install -y python3-tk
    
CMD ["python", "RefactoredArtGallery.py"]