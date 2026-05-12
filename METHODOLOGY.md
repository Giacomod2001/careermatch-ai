# CareerMatch AI - Metodologia e Processo di Sviluppo

## 1. Selezione e Ruolo del Modello AI (Approccio Ibrido)

**Obiettivo:** Selezionare l'architettura di Intelligenza Artificiale Generativa più adatta per co-sviluppare, ottimizzare e refattorizzare l'intero stack applicativo: dalla pipeline algoritmica di Data Mining all'interfaccia utente interattiva in Streamlit.

**Selezione e Valutazione:** La complessità del progetto ha reso insufficiente l'uso di un singolo LLM. Per superare i limiti tecnici dei modelli tradizionali, è stato adottato un approccio multi-modello sinergico:

### Claude Opus (Anthropic) - Progettazione Logica e Data Mining
Il modello di Anthropic è stato impiegato nelle fasi iniziali di concettualizzazione teorica e sviluppo algoritmico puro. Fondamentale per:
- La progettazione strutturale della **Knowledge Base HR**, definendo le tassonomie complesse per le Hard e Soft Skills.
- Lo sviluppo delle **euristiche NLP avanzate** per l'estrazione pulita del testo dai formati PDF non strutturati.
- La stesura della logica teorica alla base dell'algoritmo di **Matching e Gap Analysis**, garantendo coerenza statistica e semantica.

### Gemini Agentic Assistant (Google DeepMind) - Esecuzione, Refactoring e UI
L'assistente agentico di DeepMind è stato scelto per l'implementazione esecutiva e il debugging avanzato. Operando come agente autonomo integrato nel file system locale, ha permesso di:
- **Abbattere il muro del "copia-incolla"**: Gemini ha analizzato intere directory e applicato modifiche strutturali simultanee.
- **Sfruttare l'immensa Context Window** per comprendere le dipendenze interne del monolite e condurre un refactoring massivo.
- **Eseguire debugging in tempo reale** sui framework (es. risoluzione dei problemi di caching di Streamlit per i18n), garantendo uno sviluppo privo di attrito tecnico.

---

## 2. Fasi del Progetto (KDD Process)

### Fase -2: Progettazione Knowledge Base HR (Data Mining)
**Criticità:** Necessità di un database strutturato per mappare le competenze senza dipendere da API esterne.
**Soluzione:** Creazione del modulo `knowledge_base.py` con dizionari complessi per classificare Hard/Soft Skills e mappare i "Job Archetypes" con pesi specifici.

### Fase -1: Motore NLP ed Estrazione Testo
**Criticità:** CV e Job Description in formati PDF non strutturati.
**Soluzione:** Sviluppo di un parser personalizzato in `ml_utils.py` basato su `pypdf` con Regex e Fuzzy Matching (`thefuzz`) per un'identificazione robusta.

### Fase 0: Algoritmo di Matching e Gap Analysis
**Criticità:** Calcolare l'affinità quantitativa tra candidato e ruolo.
**Soluzione:** Funzione `calculate_match_score` per una percentuale di match pesata, evidenziando le skill mancanti (**Gap Analysis**).

### Fase 1: Distacco dal Contesto Accademico
**Criticità:** Riferimenti universitari hard-coded.
**Soluzione:** Scansione globale e rimozione di riferimenti accademici. Rinominazione ufficiale in **CareerMatch AI**.

### Fase 2: Ristrutturazione Architetturale
**Criticità:** Architettura frammentata con dead-code API.
**Soluzione:** Passaggio a un'architettura **Single Page Application (SPA)** basata esclusivamente su Streamlit, con routing gestito tramite `session_state`.

### Fase 3: Ottimizzazione UX (Explore Careers Hub)
**Criticità:** Navigazione frammentata tra Discovery e Builder.
**Soluzione:** Consolidamento nell'hub centrale `Explore Careers` e riprogettazione della Landing Page a 3 colonne.

### Fase 4: Privacy e GDPR Compliance
**Criticità:** Controlli GDPR ingombranti nella sidebar.
**Soluzione:** Centralizzazione dei controlli (eliminazione dati) esclusivamente nella pagina dedicata "Privacy & AI" con layout pulito.

### Fase 5: UX Friction e Autofill
**Criticità:** Elevata "friction" d'uso iniziale con form vuoti.
**Soluzione:** Iniezione dinamica di profili demo e job description pre-compilate per test immediati.

### Fase 6: Internazionalizzazione (i18n)
**Criticità:** Bug di caching di Streamlit che esponeva placeholder.
**Soluzione:** Modulo `i18n.py` centralizzato e forzatura del re-rendering tramite `importlib.reload`.

### Fase 7: Logica e Design del Chatbot "Ruben"
**Criticità:** Design troppo "boxy" e logica contestuale ripetitiva.
**Soluzione:** Refactoring CSS minimalista e attivazione del contesto CV solo su richiesta esplicita (keyword-driven).

### Fase 8: Professionalizzazione e High-End Export (Final)
**Criticità:** Export dei CV troppo semplice e palette colori incoerente.
**Soluzione:**
- Implementazione del **Harvard-style CV PDF generator** per export di alta qualità.
- Standardizzazione della **Color Palette**: rimozione di tutti i bottoni rossi (tranne quelli distruttivi) in favore della palette premium blu/gradient.
- Miglioramento della robustezza del parsing PDF per supportare qualsiasi tipologia di layout.

---
*Documento generato da Antigravity AI per il team CareerMatch AI.*
