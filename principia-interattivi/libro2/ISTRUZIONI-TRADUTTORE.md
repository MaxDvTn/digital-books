# Istruzioni per il traduttore — Libro II dei *Principia* (coordinatore: Claude, curatore: Massimo Bosetti)

Lavori in parallelo con altri 8 traduttori, ognuno su un fascicolo diverso del Libro II. Esegui il lavoro direttamente, senza delegare.

## Da leggere prima di scrivere

1. `/home/claude/libro2/strumenti/BRIEF.md` — il brief comune del Libro I. **Vale integralmente**, con queste sostituzioni di percorso:
   - modelli di formato: `/home/claude/libro2/traduzione/Newton_Principia_IT_03_Leggi.md` (leggilo per intero) e `/home/claude/libro2/traduzione/Newton_Principia_IT_05_L1_S02.md` (il modello di un fascicolo di Sezione: leggi almeno intestazione, criteri, prime due proposizioni, apparato, controllo della copertura e l'inizio della Parte B);
   - fonti: `/home/claude/libro2/fonti/latino-1726-L2-Sxx.md` e `/home/claude/libro2/fonti/motte-1846-L2-Sxx.md`;
   - check: `python3 /home/claude/libro2/check.py <file> <latino> --en <motte>` (questa copia accetta gli identificatori `II.S7.01`);
   - consegna: `/home/claude/libro2/out/`.
2. Questo file (l'addendum del Libro II, che prevale sul brief dove diverge).

## Addendum per il Libro II (vincolante)

- **Identificatori:** `**[II.S7.01]**` — libro, sezione, numero a due cifre, senza buchi. Nella Parte B, `copertura` usa la stessa forma (`"II.S7.01"`).
- **Parte B:** `id` delle unità `L2-P10`, `L2-Lem2`, `L2-P10-Cor2`; passi `L2-P10-p1`… Campo `"fascicolo"`: `"13-L2-S1"`, `"14-L2-S2"`, `"15-L2-S3-4"`, `"16-L2-S5"`, `"17-L2-S6"`, `"18a-L2-S7"`, `"18b-L2-S7"`, `"19-L2-S8"`, `"20-L2-S9"`.
- **Intestazione:** «Versione 0.1 — 8 novembre 2026. Preparata con Claude (Anthropic) per Massimo Bosetti.»

### Glossario aggiuntivo del Libro II (deciso dal curatore)

| Latino | Italiano |
|---|---|
| *resistentia* | «resistenza» |
| *medium* | «mezzo» |
| *fluidum* | «fluido» |
| *densitas* | «densità» |
| *compressio* | «compressione» |
| *vis elastica* | «forza elastica» |
| *momentum* (Lemma II) | «momento» |
| *genita* | «quantità generata» |
| *vortex* | «vortice» |
| *unda* | «onda» |
| *pulsus* (Sez. VIII) | «pulsazione», con nota alla prima occorrenza: non è l'«impulso» della Prop. I del Libro I |
| *tempus periodicum* | «tempo periodico» |
| *in ratione velocitatis* | «in rapporto alla velocità» |
| *in duplicata ratione velocitatis* | «in rapporto duplicato della velocità» |

Consolidati nel Libro I: *orbis* (strato sferico) «guscio»; *sagitta* «saetta»; *sinus versus* «seno verso»; *applicare ad* «dividere per»; *corpusculum* «corpuscolo»; *coire* «riunirsi». Decisioni: *constanter* «senza interruzione»; *in directum* «in linea retta»; *determinatio* «direzione»; *nisi quatenus* «se non in quanto».

### Termini fissati ora dal coordinatore (per tutti i fascicoli del Libro II)

Per evitare divergenze tra traduttori paralleli, usa queste rese; se una non ti sembra adatta al tuo contesto, usala comunque e motiva il dubbio nel § A.0.

- *vis insita* «forza insita»; *spatium non resistens / vacuum* «spazio non resistente / vuoto»; *medium uniforme / similare* «mezzo uniforme / omogeneo» (annota la resa di *similare* alla prima occorrenza); *medium rarum* «mezzo rado»;
- *oscillatio* «oscillazione»; *vibratio* «vibrazione»; *itus & reditus* «andata e ritorno»; *cyclois / cycloidis* «cicloide»; *pendulum* «pendolo»;
- *hyperbola* «iperbole»; *asymptotos* «asintoto»; *area hyperbolica* «area iperbolica»; *logarithmus* «logaritmo»; *progressio geometrica* «progressione geometrica»;
- *gravitas specifica* «gravità specifica»; *pondus* «peso»; *gravitas* «gravità»;
- *particulæ fluidi* «particelle del fluido»; *partes* «parti»; *vis centrifuga* «forza centrifuga»;
- *vas* «vaso»; *foramen* «foro»; *canalis* «canale»; *cataracta* (Sez. VII, Prop. XXXVI) «cateratta», con nota;
- *aer* «aria»; *aqua* «acqua»; *argentum vivum* «mercurio» (alla prima occorrenza «mercurio (argento vivo)»);
- *globus* «globo»; *cylindrus* «cilindro»; *sphæra* «sfera»; *conus* «cono»; *solidum* «solido»;
- unità di misura: *pes* «piede» (*pes Londinensis* «piede londinese», *pes Parisiensis* «piede parigino»), *digitus* «pollice», *linea* «linea», *granum* «grano», *uncia* «oncia», *libra* «libbra», *minutum secundum* «secondo»;
- *aqua pluvialis* «acqua piovana»; *ceræ, plumbum, vitrum* «cera, piombo, vetro»;
- *experimentum* «esperimento»; *Scholium* «Scolio».

Ogni altro termine nuovo va fissato nel tuo § A.0 e **segnalato nel messaggio di ritorno** (riga «Termini nuovi: …»), così il coordinatore lo armonizza.

### Regole specifiche

- **Tabelle numeriche:** riproducile per intero nel testo tradotto (tabella Markdown). Controlla l'aritmetica con uno script Python tuo; riporta il risultato nelle note. Segnala ogni cifra che non torna, **senza correggerla nel testo**.
- **Formule di Motte `[SVG n]`:** l'EPUB **non è disponibile** in questa sessione, quindi non puoi vedere le formule SVG. Non indovinarle. Allinea `en` nella Parte B sul testo di Motte così com'è (con il marcatore `[SVG n]` incluso, che check.py ignora) e, nell'apparato, elenca in una tabella «SVG da controllare» i numeri SVG che corrispondono a formule rilevanti, con la formula che il latino fa attendere. Il coordinatore le controllerà quando avrà l'EPUB.
- **Stampa 1726 e Motte 1729:** non provare a raggiungerle dal web. Elenca i punti dubbi della trascrizione in «Punti da controllare sulla stampa ECCO» (pagina 1726, lettura della trascrizione, lettura attesa, motivo).
- **Rimandi al Libro I:** quando il testo rimanda a proposizioni o lemmi del Libro I («per prop. xxxix. lib. i.»), verifica sui fascicoli in `/home/claude/libro2/traduzione/` (04–12) che l'enunciato citato regga l'uso che ne fa Newton, e scrivi il rimando nella forma «per la Prop. XXXIX del Libro I». Nel testo, i rimandi interni al Libro II si scrivono «per la Prop. V» (o «del Libro II» se il latino lo dice). Elenca in apparato i rimandi verificati e quelli che non tornano.
- **Note storiche:** solo da ciò che risulta dalle fonti allegate; ciò che aggiungi da conoscenza generale va marcato «(non verificato sulle fonti allegate)».
- **Lunghezza:** il fascicolo può essere lungo; scrivilo per parti (file temporanei in `/home/claude/libro2/tmp/<tuo-fascicolo>/`) e poi concatenale. Non creare altri file in `out/` oltre al tuo fascicolo.

## Messaggio di ritorno (massimo 25 righe)

Nome del file e dimensioni; identificatori (primo–ultimo, numero); unità della Parte B e passi; esito dei controlli (copertura frase per frase, check.py con l'ultima riga dell'output, verifiche numeriche e tabelle); riga «Termini nuovi: …»; riga «Rimandi al Libro I: …» (quanti, quali non tornano); 3–8 punti principali per il curatore; numero di SVG da controllare; cosa non hai potuto verificare. Non incollare il fascicolo.
