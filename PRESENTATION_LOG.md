# CareerMatch AI - Prompt Engineering & Development Log

Questo documento raccoglie i prompt strategici utilizzati per lo sviluppo di CareerMatch AI, riassunti e migliorati per una presentazione tecnica, insieme agli output e ai risultati ottenuti.

---

## 🟢 Modulo 1: Architettura dei Dati e Motore NLP
**Obiettivo:** Creare le fondamenta del sistema (Knowledge Base e Parser PDF).

### 📝 Prompt Strategico (Ottimizzato)
> "Progetta un'architettura di dati locale per un sistema di Career Analytics. Crea un modulo `knowledge_base.py` con tassonomie gerarchiche per Hard e Soft Skills, mappando archetipi di ruolo con pesi specifici. Implementa inoltre in `ml_utils.py` un parser PDF robusto che utilizzi Fuzzy Matching e Regex per normalizzare l'estrazione di competenze da documenti non strutturati."

### 🛠️ Output & Risultati Tecnici
- **Implementazione:** Creato un database gerarchico di oltre 230 archetipi professionali.
- **Soluzione Bug:** Risolta la criticità della "parola tronca" nei PDF multi-colonna tramite un algoritmo di ricongiungimento semantico delle righe.
- **Risultato:** Estrazione pulita del testo con tolleranza agli errori di battitura (Fuzzy Match > 85%).

---

## 🔵 Modulo 2: Algoritmo di Matching e Analytics
**Obiettivo:** Trasformare il testo estratto in punteggi quantitativi e analisi dei gap.

### 📝 Prompt Strategico (Ottimizzato)
> "Sviluppa una funzione di scoring multi-dimensionale (`calculate_match_score`) che confronti il Vector Space Model del CV con i requisiti dell'archetipo di ruolo. L'output deve includere una percentuale di affinità pesata, una Gap Analysis esplicita delle competenze mancanti e un sistema di inferenza per suggerire skill trasferibili."

### 🛠️ Output & Risultati Tecnici
- **Implementazione:** Algoritmo basato su TF-IDF e cosine similarity, pesato per importanza delle skill (65% Hard, 20% Soft, 15% Education).
- **Analisi Proattiva:** Il sistema non si limita a trovare parole uguali, ma suggerisce skill correlate tramite "Inference Rules".
- **Risultato:** Report analitico istantaneo con visualizzazione chiara dei punti di forza e debolezza del candidato.

---

## 🟡 Modulo 3: Core SPA & Internazionalizzazione (i18n)
**Obiettivo:** Consolidare l'app in una Single Page Application fluida e multilingue.

### 📝 Prompt Strategico (Ottimizzato)
> "Ristruttura l'intero stack in una SPA basata su Streamlit, eliminando le dipendenze da backend esterni. Implementa un sistema di navigazione centralizzato tramite `session_state` e un modulo di internazionalizzazione (i18n) che permetta lo switch istantaneo IT/EN senza perdita di dati."

### 🛠️ Output & Risultati Tecnici
- **Soluzione Bug Critico:** Risolto il problema del "Flickering/Placeholder" di Streamlit. Utilizzando `importlib.reload(i18n)` abbiamo forzato il re-rendering immediato delle etichette, eliminando la visualizzazione di chiavi grezze come `[ruben_subtitle]`.
- **Navigazione:** Creato un router logico che gestisce Landing, Explore, Analysis e Privacy in un unico flusso coerente.

---

## 🟣 Modulo 4: UX Professionalizzazione e UI Premium
**Obiettivo:** Elevare l'estetica e la funzionalità del prodotto per un contesto aziendale.

### 📝 Prompt Strategico (Ottimizzato)
> "Esegui un refactoring estetico completo: implementa un design system basato su glassmorphism e palette LinkedIn (Blue/Dark). Riprogetta l'export PDF in formato Harvard-style e standardizza l'uso dei colori: usa il rosso esclusivamente per azioni distruttive (GDPR deletion) e il gradiente blu per tutte le call-to-action primarie."

### 🛠️ Output & Risultati Tecnici
- **UI/UX:** Eliminata la "friction" iniziale tramite l'autofill dinamico di profili demo (Data Analyst), permettendo test immediati.
- **Export PDF:** Implementato un generatore PDF strutturato con linee divisorie, font Times e header Harvard, superando il limite dei generatori "plain text" scarni.
- **Estetica:** Coerenza cromatica totale: pulsanti primari in gradiente blu e pulsante di cancellazione dati (Privacy) in rosso "destructive" isolato.

---

## 🏁 Conclusione dello Sviluppo
Grazie a questo approccio di Prompt Engineering, siamo passati da uno script accademico frammentato a una piattaforma di **Career Analytics** professionale, scalabile e pronta per il deployment in contesti corporate.
