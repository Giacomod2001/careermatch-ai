# Frontend — CareerMatch AI
FROM python:3.11-slim

WORKDIR /app

# Dipendenze di sistema
RUN apt-get update && apt-get install -y --no-install-recommends \
    graphviz \
    && rm -rf /var/lib/apt/lists/*

# Copia requirements e installa
COPY frontend/requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt requests

# Copia i file condivisi
COPY shared_core/ /app/

# Copia il codice del frontend
COPY frontend/ /app/

# Espone Streamlit
EXPOSE 8501

# Avvia Streamlit
CMD ["streamlit", "run", "app.py", \
     "--server.address=0.0.0.0", \
     "--server.port=8501", \
     "--server.headless=true", \
     "--browser.gatherUsageStats=false"]
