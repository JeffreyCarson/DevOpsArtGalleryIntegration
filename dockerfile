FROM python:3.9.13

WORKDIR /app

RUN pip install tk

COPY . .
    
CMD ["python", "RefactoredArtGallery.py"]