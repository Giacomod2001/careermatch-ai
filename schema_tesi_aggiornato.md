# 📘 Dal prompt al prodotto

> **Vibe Coding, AI e Cloud per il mercato del lavoro**
> Tesi Magistrale — IULM, Intelligenza Artificiale, Impresa e Società

---

## 🧭 Il Filo Rosso

**L'idea c'è, funziona — ora creiamo qualcosa di davvero accessibile a tutti.**

```
PROBLEMA  →  METODO  →  STRUMENTI  →  RESPONSABILITÀ  →  PROTOTIPO  →  PRODOTTO  →  VALIDAZIONE
  Cap.1       Cap.2       Cap.3          Cap.4             Cap.5        Cap.6        Cap.7-8
```

---
---

# PARTE I — TEORIA

---

## Cap. 1 — Il Prompt: da dove nasce l'idea

In Italia la disoccupazione giovanile supera il 20% (ISTAT, 2025), eppure le aziende faticano a coprire posizioni entry-level e stage. Il problema non è la mancanza di lavoro — è la mancanza di strumenti che rendano l'accesso trasparente per chi si affaccia al mercato per la prima volta.

Il Randstad Employer Brand Research 2025 lo conferma: i ruoli entry-level sono calati del 29% dal 2024, e il 75% della Gen Z usa già l'AI per sviluppare competenze, ma non ha strumenti specifici per orientarsi nel percorso candidato.

Questa tesi nasce da una **doppia prospettiva**:

- Come **studente**, ho vissuto in prima persona — insieme ai colleghi di corso — la frustrazione di cercare uno stage senza punti di riferimento chiari: un processo opaco, frammentato, basato su tentativi.
- Come **tirocinante in Randstad Group Italia** (Digital Data Analyst), ho visto lo stesso problema dall'altro lato: un'azienda che investe su "lavori senza diploma" e "lavori senza laurea" per intercettare chi non ha ancora un titolo, confermando che la domanda c'è ma l'offerta di strumenti accessibili no.

Da questa doppia osservazione è nato, nel team, **CareerMatch AI**: uno strumento che copre l'intero percorso del candidato — da chi non sa cosa cercare a chi deve ottimizzare il CV per una posizione specifica. Ma il prototipo vive su GitHub e su un link Streamlit — accessibile solo a chi sa dove cercarlo. L'obiettivo di questa tesi è trasformarlo in qualcosa di davvero accessibile a chiunque.

### Punti chiave

- Il paradosso del mercato del lavoro giovanile: alta disoccupazione + posizioni scoperte
- La doppia prospettiva: studente che cerca stage + analista in Randstad che vede i dati
- I dati Randstad (REBR 2025, Workmonitor 2025/2026) come cornice quantitativa
- CareerMatch AI come risposta concreta nata dal bisogno reale del team
- Il limite attuale: un prototipo che funziona ma non è accessibile a chi ne ha più bisogno

### Domanda di ricerca

> *Il vibe coding può essere uno strumento efficace per trasformare un prototipo accademico in un prodotto AI realmente accessibile, che renda più trasparente l'ingresso dei giovani nel mercato del lavoro?*

---

## Cap. 2 — Il Metodo: Vibe Coding

La scrittura di software sta cambiando. Non più codice riga per riga, ma dialogo con un'AI che genera, testa e itera. Karpathy lo definisce nel 2025 e in un anno il concetto esplode: diventa parola dell'anno, Gartner fa previsioni enormi, il dibattito tra chi lo celebra e chi lo critica è apertissimo.

### Contenuti

- Definizione e origine (Karpathy, 2025)
- L'evoluzione verso l'agentic engineering (2026): non scrivi codice, dirigi agenti
- Il dibattito: chi dice che democratizza, chi dice che crea debito tecnico
- Cosa cambia rispetto allo sviluppo tradizionale
- Implicazioni per chi non è un programmatore di professione

### Il punto critico

Il capitolo affronta il nodo centrale del vibe coding: l'AI generativa **NON sostituisce** la necessità di comprendere a fondo le tecniche che si stanno utilizzando.

In questa tesi, ogni modello di machine learning e ogni scelta architetturale è stata studiata prima di essere implementata. L'AI è uno strumento di accelerazione, ma il lavoro intellettuale di comprensione — capire *perché* si usa un Random Forest anziché una SVM, *perché* TF-IDF con sublinear TF, *come* si interpreta un dendrogramma — resta totalmente a carico dello sviluppatore.

Affidarsi ciecamente all'AI senza studio è il rischio principale del vibe coding, e questa tesi lo affronta esplicitamente: il **Cap. 3** esiste proprio per dimostrare che dietro ogni riga di codice generata c'è uno studio approfondito delle tecniche utilizzate.

---

## Cap. 3 — Gli Strumenti: Data Mining e Machine Learning

Questo è il **cuore scientifico** della tesi. Ogni tecnica è spiegata partendo dalla teoria, con riferimento alla letteratura accademica, e poi collegata alla sua implementazione pratica nel progetto.

Il capitolo percorre il processo KDD — dal dato grezzo alla conoscenza — e spiega ogni algoritmo usato nel progetto, non come formula ma come strumento con uno scopo pratico preciso.

### 📐 Il processo KDD (Knowledge Discovery in Databases)

- I 7 passaggi dall'acquisizione dati alla presentazione dei risultati
- Riferimento: Fayyad, Piatetsky-Shapiro & Smyth (1996)

### 📝 Text Mining & Feature Extraction

| Tecnica | Funzione | Riferimento |
|---------|----------|-------------|
| TF-IDF Vectorization | Trasforma il testo in Vector Space Model | Salton & Buckley (1988) |
| N-gram Analysis | Cattura sequenze di parole (uni/bi/trigram) | — |
| Cosine Similarity | Misura di similarità nel VSM | — |
| Fuzzy Matching | Gestione variazioni e errori di battitura | Navarro (2001) |

### 🌲 Classification (Supervised Learning)

| Tecnica | Funzione | Riferimento |
|---------|----------|-------------|
| Random Forest | Ensemble di Decision Trees | Breiman (2001) |
| Pipeline sklearn | Preprocessing + Classification | — |

- *Perché Random Forest e non SVM o Neural Network?* Analisi critica della scelta
- Feature importance e interpretabilità del modello

### 🔵 Clustering (Unsupervised Learning)

| Tecnica | Funzione | Riferimento |
|---------|----------|-------------|
| K-Means | Partitioning clustering per skill simili | MacQueen (1967) |
| Hierarchical Clustering | Dendrogramma delle skill (Ward linkage) | Ward (1963) |
| PCA | Riduzione dimensionalità per visualizzazione 2D | Jolliffe (2002) |

- *Analisi critica: come si sceglie K? Elbow method, silhouette score*

### 📊 Topic Modeling

| Tecnica | Funzione | Riferimento |
|---------|----------|-------------|
| LDA | Estrazione topic latenti | Blei, Ng & Jordan (2003) |

- *Limiti di LDA su testi brevi (job descriptions) e alternative*

### 🏷️ Information Extraction

| Tecnica | Funzione | Riferimento |
|---------|----------|-------------|
| NER | Named Entity Recognition | Nadeau & Sekine (2007) |
| Skill Extraction | Estrazione competenze tecniche e soft skills | — |

### 🔗 Pattern Discovery

| Tecnica | Funzione | Riferimento |
|---------|----------|-------------|
| Association Analysis | Correlazioni tra skill (transferable skills) | Agrawal & Srikant (1994) |
| Inference Rules | Regole per dedurre skill correlate | — |

### 🚀 L'evoluzione: da tecniche statistiche a embeddings neurali

- Da TF-IDF (bag-of-words) → Word2Vec (Mikolov et al., 2013) → Sentence Embeddings (Devlin et al., 2019)
- Vertex AI Embeddings come upgrade del prototipo

---

## Cap. 4 — La Responsabilità: Etica, Regolamentazione e Cloud

Creare AI non basta — bisogna farlo in modo responsabile e su un'infrastruttura seria. Questo capitolo unisce due temi: le scelte etiche e l'infrastruttura cloud.

### ⚖️ Etica e regolamentazione

| Tema | Contenuto | Riferimento |
|------|-----------|-------------|
| Glass Box / XAI | Perché l'utente deve poter vedere come funziona il sistema | Arrieta et al. (2020) |
| GDPR e AI Act | Come si implementano nel codice, non solo come obblighi sulla carta | Reg. UE 2016/679; Reg. UE 2024/1689 |
| Bias nel recruitment | Come si evita che un algoritmo discrimini | Raghavan et al. (2020) |
| Privacy-by-design | Come scelta architetturale | Cavoukian (2011) |

### ☁️ Infrastruttura cloud

- Cos'è il serverless e perché conviene per questo tipo di progetto
- Containerizzazione: impacchettare un'app per il cloud — Merkel (2014)
- ML-as-a-Service: usare modelli AI senza doverli addestrare in locale

---
---

# PARTE II — PRATICA

---

## Cap. 5 — Il Prototipo: CareerMatch AI

Il primo MVP nasce come progetto di gruppo universitario. Funziona, ma è un monolith — una singola app Python che fa tutto. Il capitolo documenta cos'è stato costruito dal team, come, e per chi.

Ogni scelta tecnica nel prototipo è motivata sulla base dello studio della letteratura (Cap. 3): la scelta degli algoritmi, la configurazione dei parametri, le decisioni architetturali.

### Contenuti

- Origine: MVP collaborativo del team universitario
- **Il percorso dell'utente nell'app:**
  - 🧭 **Career Discovery** — per chi non sa ancora cosa cercare
  - 📝 **CV Builder** — per chi deve creare un CV da zero
  - 🔍 **CV Analysis** — per chi ha già un CV e vuole migliorarlo su una posizione specifica
- Il sistema di scoring multi-fattore
- La knowledge base: archetipi lavorativi, gerarchie di competenze, regole di inferenza
- Limiti del prototipo: perché un'app monolitica non basta per la produzione

---

## Cap. 6 — Il Prodotto: dalla Prototipazione alla Migrazione

Questa è la **parte individuale della tesi**. L'obiettivo è trasformare il prototipo del team in un prodotto davvero accessibile a chiunque — trovabile online, usabile senza competenze tecniche, con un'interfaccia professionale.

Le scelte tecnologiche specifiche saranno concordate con il relatore.

### Documentazione del processo di migrazione

| Fase | Cosa si documenta |
|------|-------------------|
| **Analisi dei limiti** | Cosa funziona e dove inizia a non bastare — con screenshot e colli di bottiglia |
| **Studio architetturale** | Confronto ragionato tra architetture possibili — con diagrammi comparativi |
| **Separazione responsabilità** | Come e perché separare le componenti — con diagrammi prima/dopo |
| **Containerizzazione e deploy** | Impacchettamento e messa online — con screenshot, log e diagrammi |
| **Upgrade del matching** | Da tecniche statistiche ad approcci avanzati — con confronti visivi |
| **Accessibilità** | Rendere lo strumento trovabile e usabile senza competenze tecniche |
| **Analytics (GDPR-compliant)** | Monitoraggio utenti nel rispetto della normativa |
| **Diario tecnico** | Problemi incontrati e come sono stati risolti |

### Formato

Ricco di materiale visivo — diagrammi, screenshot, grafici di confronto, tabelle comparative — per documentare il processo in modo chiaro e replicabile.

---

## Cap. 7 — La Validazione

Funziona? È meglio di prima? È etico nella pratica?

### Verifiche

- Metriche di performance dei modelli ML
- Confronto qualità del matching: prima vs dopo la migrazione
- Confronto infrastruttura: prototipo locale vs cloud
- Trasparenza algoritmica in azione (Glass Box)
- Compliance normativa verificata
- Analisi del comportamento utente reale
- User testing con colleghi di corso

---

## Cap. 8 — Conclusioni

Dal prompt al prodotto: cosa ha funzionato, cosa no, e dove si va da qui.

- Il vibe coding come metodo di sviluppo: promesse vs realtà
- **L'importanza dello studio autonomo**: anche con l'AI, la comprensione dei modelli è imprescindibile
- **Da prototipo a prodotto accessibile**: bilancio del percorso
- Limiti e autocritica
- Sviluppi futuri
