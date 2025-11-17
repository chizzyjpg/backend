FROM python:3.11-slim

WORKDIR /app
COPY . /app/

RUN pip install --no-cache-dir \
    django \
    djangorestframework \
    django-cors-headers \
    python-dotenv \
    requests

RUN mkdir -p /tmp

# copiamos entrypoint y le damos permisos
COPY entrypoint.sh /app/entrypoint.sh
RUN chmod +x /app/entrypoint.sh

EXPOSE 8000
CMD ["./entrypoint.sh"]
