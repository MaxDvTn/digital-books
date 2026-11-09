# Prompt per la revisione complessiva dei *Principia* (Fascicoli 1–27) — nuova chat del progetto «Digital Book»

**Prima di incollare questo prompt:** apri la nuova chat collegata al computer (app desktop di Claude) e concedi l'accesso alla cartella `~/Projects/digital_books`. Se possibile tieni aperta l'app: la scansione ECCO del 1726 e Motte 1729 si consultano meglio con il browser integrato. Se nessuna delle due stampe è raggiungibile, scarica i PDF da Internet Archive e mettili in `principia-interattivi/fonti/stampe/`.

---

Agisci come revisore di un'edizione scientifica, con la competenza di un latinista, di uno storico della scienza, di un astronomo e di un fisico. Il progetto è un'edizione didattica e interattiva in italiano dei *Principia* di Newton, per il liceo scientifico. Il curatore è Massimo Bosetti. La traduzione è completa in versione 0.1: Fascicoli 1–3 (Definizioni, Scolio, Leggi), 4–12 (Libro I), 13–20 (Libro II), 21–27 (Libro III). Questa chat **non traduce di nuovo**: controlla, corregge dove le prove lo giustificano e documenta.

## Dove si trova il progetto

Tutto è in `~/Projects/digital_books/principia-interattivi/`:

| Cartella | Contenuto |
|---|---|
| `traduzione/` | Fascicoli 01–27 (con 18a/18b, 24a/24b, 25a/25b, 26a/26b) |
| `fonti/latino-1726/` | Trascrizione del Newton Project, per sezione o gruppo |
| `fonti/motte-1846/` | Motte 1846 per sezione o gruppo, e `svg_tex.tsv` (LaTeX delle 1361 formule SVG) |
| `fonti/` | EPUB Gutenberg #76404 completo (`Newton's_Principia____…3.epub`) |
| `strumenti/` | `BRIEF.md`, `check.py`, `rinumera.py`, `extract.py`, `parteB.py` |
| `libro2/`, `libro3/` | Istruzioni date ai traduttori (glossari e termini fissati) |
| `progetto/` | `stato-del-progetto.md` (leggilo per intero: elenca tutti i punti aperti dei tre Libri) |

Lavora su una copia in `/home/claude/revisione/` (porta i file con `device_stage_files`, al massimo 50 per chiamata) e riporta i risultati con `device_commit_files`. Non cancellare e non rinominare file esistenti: le versioni corrette si salvano **sopra** i fascicoli in `traduzione/` solo dopo che il curatore ha visto il rapporto, oppure, se il curatore non risponde, come file nuovi in `revisione/v0.2/`.

## Stampe da consultare

- Latino 1726, scansione ECCO: Internet Archive `bim_eighteenth-century_philosophiae-naturalis-p_newton-sir-isaac_1726` (https://archive.org/details/bim_eighteenth-century_philosophiae-naturalis-p_newton-sir-isaac_1726). Le pagine della stampa (i marcatori ‹n› della trascrizione) non coincidono con il numero di immagine della scansione: trova lo scarto su due o tre pagine note e poi usalo, ricontrollandolo a ogni cambio di Libro (le tavole fuori testo spostano la numerazione).
- Motte 1729, vol. I: Internet Archive `bub_gb_Tm0FAAAAQAAJ`. Il vol. II va cercato (Internet Archive o Google Books); se non lo trovi, dillo e lascia i punti del Libro III e della seconda metà del Libro II come «non verificati su Motte 1729».
- Prova prima `WebFetch` sulle pagine di Internet Archive; se non basta, usa il browser integrato dell'app desktop. Se nessuna delle due strade funziona, fermati su questo punto, elenca che cosa serve e chiedi al curatore i PDF.

## Compito

### 1. Refusi della trascrizione sulla stampa ECCO

Ogni fascicolo ha una tabella «Punti da controllare sulla stampa ECCO» (o una sezione equivalente dell'apparato: «Refusi e anomalie della trascrizione»). Raccogli con uno script **tutti** i punti dei Fascicoli 1–27 in un unico elenco (`revisione/punti-ECCO.tsv`: fascicolo, identificatore, pagina 1726, lettura della trascrizione, lettura attesa, motivo). Per ciascuno guarda la stampa e registra l'esito: «la stampa conferma la trascrizione», «la stampa ha la lettura attesa», «la stampa ha una terza lettura», «illeggibile». Dai la precedenza ai punti che cambiano il senso o i numeri: quelli in grassetto nello stato del progetto (per esempio Libro I, Prop. XVII *SP+AH*; Libro II, Prop. XIV *ad lineam ED*; Libro III, tabella di Pound «12⅔ ad 14⅔», Prop. XLII «2G − 2C», Prop. VIII «1/169282»).

Quando la stampa dà la lettura attesa, correggi la traduzione se serve e trasforma l'annotazione in «refuso della trascrizione, verificato sulla stampa (p. n)». Quando la stampa conferma la trascrizione, l'errore è di Newton o dello stampatore del 1726: lascia il testo com'è e aggiorna la nota. Le stringhe `la` della Parte B restano esatte rispetto alla trascrizione (check.py lo richiede): la lettura della stampa va in `nota`.

### 2. Formule SVG di Motte

Lo stato del progetto elenca le formule SVG di Motte 1846 che non tornano con il latino (Libro I, Libro II, Libro III). Per ciascuna:
1. guarda l'immagine dell'EPUB (`rsvg-convert -h 120 -b white OEBPS/3191938728343764116_n.svg -o /tmp/f.png`) e il LaTeX in `svg_tex.tsv`;
2. confronta con Motte 1729 alla pagina corrispondente;
3. classifica: errore già in Motte 1729, errore introdotto nel 1846, errore della conversione Gutenberg (immagine diversa dal 1846), oppure falso allarme.

Riporta il risultato in `revisione/svg-motte.tsv` e aggiorna le tabelle «dove Motte sbaglia» dei fascicoli.

### 3. Revisione indipendente a campione

Le traduzioni sono state fatte da traduttori diversi, che hanno anche controllato il proprio lavoro. Serve un controllo fatto da chi non le ha viste nascere.
- Scegli con uno script un campione: per ogni fascicolo 2 unità a caso (un enunciato con la sua dimostrazione, oppure un capoverso di scolio o un paragrafo di tabella), più tutte le unità segnalate come «lettura incerta». In tutto circa 70 unità.
- Avvia **revisori in parallelo** (uno per gruppo di 3–4 fascicoli). Ogni revisore riceve solo il latino, Motte, il brief, il glossario e l'elenco delle unità; **non** riceve la traduzione finché non ha scritto la propria resa di controllo, poi confronta e classifica ogni differenza: errore di senso, omissione, errore numerico, termine fuori glossario, scelta stilistica. Il revisore rifà con uno script ogni conto e ogni verifica numerica dichiarata nelle note del campione.
- I revisori non correggono i fascicoli: consegnano un rapporto (massimo 30 righe) e una tabella delle differenze. Le correzioni le decidi tu, e quelle di senso le sottoponi al curatore.
- Se nel campione di un fascicolo trovi più di un errore di senso, estendi la revisione a tutto il fascicolo.

### 4. Coerenza tra i tre Libri

- Glossario: confronta con uno script le rese dei termini del brief e dei glossari dei Libri II e III in tutti i fascicoli. Elenca le divergenze ancora presenti (per esempio *divisim*, che nel Libro I è «separando», «per separazione», «dividendo»; *mediocris*; *plaga*; *digitus*). Uniforma solo i termini su cui il curatore ha già deciso; per gli altri prepara una tabella di proposta.
- Rimandi: verifica con uno script che ogni rimando interno nella forma «per la Prop. N del Libro …» punti a un'unità che esiste nei fascicoli e che il titolo regga l'uso.
- Formato: intestazioni, versione, sezioni obbligatorie del brief, Parte B valida con check.py per tutti i fascicoli.

### 5. Consegna

- `revisione/RAPPORTO-revisione.md`: sintesi per il curatore (esiti dei punti ECCO, SVG, campione, coerenza), con le decisioni che restano a lui.
- Fascicoli corretti come versione 0.2: aggiorna la riga «Versione …» e aggiungi in «Registro del lavoro successivo» l'elenco delle modifiche con identificatore e motivo. Nessuna correzione silenziosa.
- `check.py` deve passare su tutti i fascicoli modificati.
- Aggiorna `progetto/stato-del-progetto.md` sul computer e `claude/stato-del-progetto.md` nel progetto claude.ai.
- Manda nella chat il rapporto e i fascicoli modificati.

## Regole

- Fonti: solo la trascrizione 1726, la stampa ECCO, Motte 1846 e 1729. Nessuna traduzione moderna (Cajori, Cohen–Whitman, Pala, Giudice). Ciò che viene da conoscenza generale va marcato «(non verificato sulle fonti allegate)».
- Il latino è il testo guida; le cifre di Newton che non tornano si segnalano e non si correggono, a meno che la stampa mostri un refuso della trascrizione.
- Decisioni del curatore già prese (valgono anche qui): *constanter* «senza interruzione»; *impulsu unico sed magno* «con un impulso unico ma grande»; *in directum* «in linea retta»; *determinatio* «direzione»; *nisi quatenus* «se non in quanto»; licenza CC BY-SA 4.0 per i testi, MIT per il codice. Il latino del Newton Project resta nella cartella di lavoro e non si ridistribuisce.
- Lezioni dalle traduzioni: avvia i revisori solo dopo aver controllato che fonti, `svg_tex.tsv` ed EPUB siano nel container; il limite d'uso può interrompere un agente a metà: chiedi a ogni revisore di salvare il lavoro in `tmp/` e riprendilo con un messaggio all'agente interrotto.
- **Da non fare in questa chat:** le pagine interattive.
