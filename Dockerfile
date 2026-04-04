FROM python:3.11-slim
WORKDIR /app
ENV PYTHONUNBUFFERED=1
ENV PYTHONDONTWRITEBYTECODE=1
COPY . .
EXPOSE ${PORT:-8000}
CMD ["sh", "-c", "python3 area_of_rectangle.py"]