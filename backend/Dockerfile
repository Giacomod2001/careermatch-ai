# Backend — CareerMatch AI
FROM python:3.11-slim

WORKDIR /app

# Dipendenze di sistema (NLP/Levenshtein)
RUN apt-get update && apt-get install -y --no-install-recommends \
    build-essential \
    graphviz \
    && rm -rf /var/lib/apt/lists/*

# Copia requirements e installa
# Aggiungiamo fastapi e uvicorn ai requisiti
COPY backend/requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt fastapi uvicorn requests

# Scarica dati NLTK
RUN python -c "import nltk; nltk.download('punkt'); nltk.download('punkt_tab'); nltk.download('stopwords'); nltk.download('averaged_perceptron_tagger'); nltk.download('averaged_perceptron_tagger_eng'); nltk.download('maxent_ne_chunker'); nltk.download('maxent_ne_chunker_tab'); nltk.download('words')"

# Copia i file condivisi
COPY shared_core/ /app/

# Copia il codice del backend
COPY backend/ /app/

# Espone la porta dell'API
EXPOSE 8000

# Avvia FastAPI
CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8000"]
