FROM python:3.13-slim

ENV PYTHONDONTWRITEBYTECODE=1 \
    PYTHONUNBUFFERED=1 \
    # Faz o Python enxergar o pacote "siteFilmes"
    PYTHONPATH="/site_filmes/site_filmes:/site_filmes:${PYTHONPATH}"

WORKDIR /site_filmes

COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

COPY . .

EXPOSE 8000


CMD ["python", "site_filmes/siteFilmes/manage.py", "runserver", "0.0.0.0:8000"]
