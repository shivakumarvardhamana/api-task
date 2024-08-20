FROM python:3.10-slim
COPY requirements.txt .
RUN pip install r -r requirement.txt
COPY . .
CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]