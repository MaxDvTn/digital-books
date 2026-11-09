# Prompt — Discorsi interattivi, seconda parte (scheda 2 e seguenti)

Da incollare in una **nuova chat del progetto «Digital Book»**, aperta dall'app desktop sul Mac (serve la cartella locale).

---

Ciao. Sono Max, insegno fisica e matematica al Liceo scientifico «Leonardo da Vinci» di Trento. Continuiamo l'edizione interattiva dei **Discorsi e dimostrazioni matematiche intorno a due nuove scienze** di Galileo (Leida, 1638). La scheda 1 (moto equabile) e la copertina sono fatte; ora passiamo alla scheda 2.

## 1. Prima di tutto
1. Leggi nel progetto `claude/galileo-stato-del-progetto.md`, sezione «Discorsi»: stato, decisioni, convenzioni e fonti.
2. Carica le skill:
   - `editore-libri-scientifici-interattivi`, la guida principale;
   - `verifica-dimostrazioni-interattive`;
   - `copertine-libri-interattivi`, se cambi la copertina (per esempio per attivare una tavola);
   - `osservazioni-storiche-come-dati`, solo quando confronti dati di Galileo con un modello.
3. Chiedi l'accesso alla cartella `~/Projects/digital_books` sul mio Mac. Lavori in `discorsi/interattivo/`.
4. Guarda come è fatta la scheda 1 e **riusa il suo codice**:
   - `equabile_modello.js`: il modello, unico per la pagina e per la verifica;
   - `scheda_equabile.html` e `scheda_equabile.js`: passi della lettura guidata, figura SVG con le lettere di Galileo, griglia di Euclide, scritte ingrandite sul telefono;
   - `dimostrazioni/ME-P1.json`: latino 1638 e traduzione frase per frase, passi, note editoriali;
   - `verifica_equabile.py`: aritmetica esatta e confronto con il modello JS tramite node;
   - `build.py`, che inserisce le schede dopo l'enunciato giusto (`SCHEDE_DOPO`).

   Pagina pubblicata (anteprima privata): https://claude.ai/artifact/8LMBs4nedRP3gFNXxE4jt7 (slug `3b638b09-7ac6-4370-b14a-bef96555c524`). Ripubblica sempre lì.

## 2. Cose già decise
- **La fonte UTET/Liber Liber ha solo gli enunciati del trattato latino, senza dimostrazioni.** Le dimostrazioni si prendono dalla **stampa del 1638**:
  - scansione su Wikimedia Commons, «Galilei - Discorsi e dimostrazioni matematiche intorno a due nuove scienze - 1638.djvu»; pagina del file = pagina a stampa + 9;
  - le pagine latine sono trascritte anche su **la.wikisource** (le pagine di it.wikisource le includono con `{{Iwpage|la}}`): puoi partire da lì, ma controlla ogni parola sulla scansione e cita la fonte. Le trascrizioni di Wikisource sono CC BY-SA;
  - la traduzione è nostra, segnalata come tale; latino e traduzione stanno nella scheda, il testo del libro resta quello UTET.
- **Fonti dal container.** Il container non raggiunge Wikisource, Commons né il Museo Galileo. Usa il **browser integrato** del Mac: API di Commons per avere `thumburl` della pagina, poi lo screenshot, che arriva anche nel container come file.
- **Licenza**: CC BY-NC-SA 4.0 per i testi, MIT per il codice.
- **Stile**: lo stesso del Sidereus:
  - EB Garamond, carta `#fbf8f2`, rubrica `#871919`;
  - nei dialoghi la voce in maiuscoletto rubricato;
  - enunciati come blocchi con filetto rosso a sinistra.

## 3. Come lavoriamo
- **Una scheda alla volta.** Me la fai vedere, io guardo e correggo, poi passiamo alla successiva. Dopo ogni scheda aspetta il mio parere.
- **Didattica.** L'interattività deve far vedere il ragionamento di Galileo, non sostituirlo:
  - prima la sua proporzione; la formula moderna solo nella «Lettura moderna», chiusa di default;
  - in ogni scheda le domande «Per la classe» con le risposte nascoste e la sezione «Come è fatta», che dichiara le semplificazioni.
- **Figure.**
  - SVG ricostruito con le lettere di Galileo, accanto all'incisione del 1638;
  - nei riquadri ingranditi sempre la scala vera;
  - cursori nel verso intuitivo;
  - casi degeneri gestiti, con un avviso.
- **Telefono.** Prova a 375, 768 e 1280 px. Aree di tocco di almeno 44 px, con alternativa da tastiera.

## 4. Il lotto
1. **Scheda 2, moto naturalmente accelerato** (righe ~1214–1330 del .tex). Pagine latine della stampa:
   - introduzione e definizione di *De motu naturaliter accelerato*: pp. 157–158;
   - Teorema I, Teorema II e Corollario I: pp. 170–172;
   - Corollario II e Scolio: p. 178;
   - da verificare tutte sulla scansione: in mezzo ci sono le pagine in volgare del dialogo.
   
   Contenuto della scheda:
   - la definizione: velocità che cresce in proporzione al tempo, con la discussione di Sagredo e Salviati (v ∝ s è impossibile);
   - il **Teorema I** (velocità media):
     - nel testo c'è l'argomento di Sagredo con la figura 44 (triangolo e rettangolo, tempo AI, CB grado massimo);
     - la dimostrazione di Galileo va presa dal latino, con la figura 43;
     - mostra il triangolo delle velocità e il rettangolo di uguale area;
   - il **Teorema II** con il **Corollario I**: spazi come i quadrati dei tempi, numeri dispari 1, 3, 5, 7, con una caduta animata a intervalli eguali (lettere AD, DE, EF, FG e HL, LM, MN, NI del corollario).
2. **Scheda 3, esperimento del piano inclinato** (righe ~1320–1336): il regolo di 12 braccia, la palla di bronzo, il canale con la cartapecora, l'orologio ad acqua.
   - La simulazione permette di cambiare l'inclinazione e di «pesare l'acqua».
   - Produce una tabella di misure con un errore realistico e dichiarato.
   - Lo studente verifica la proporzione come Galileo («replicate ben cento volte»).
   - Distingui bene che cosa dice il testo da che cosa è simulato.
3. Dopo il lotto:
   - **Giornata Quarta**: parabola (Prop. I); le tre tavole numeriche, che oggi sono segnaposto e vanno convertite (estendi l'importatore per `tabular`); confronto con la formula moderna secondo la skill delle osservazioni;
   - **Giornata Prima**: pendolo, caduta nei mezzi, trave a sbalzo.

Quando una scheda è pronta, nella copertina (`copertina.json`) dai l'`id` della scheda alla tavola corrispondente: la voce smette di essere «in preparazione» e diventa un link.

## 5. Verifica, test, consegna
- **Verifica.** Ogni scheda passa da un **revisore indipendente**, un agente che non l'ha costruita. Gli dai:
  - le scansioni delle pagine del 1638;
  - il JSON della dimostrazione;
  - il codice e la pagina.
  
  Correggi tutte le riserve prima di considerarla finita, e salva il rapporto in `discorsi/interattivo/verifiche/`.
- **Test.** Playwright con `/usr/bin/google-chrome`:
  - nessun errore in console, nessun overflow orizzontale;
  - il titolo della scheda non resta sotto l'intestazione;
  - nel libro sfogliabile nessuna pagina deborda (`.lb-corpo`) a 1280, 1024, 768 e 375 px.
- **Attenzione ai file sul Mac.** `device_commit_files` a volte scrive una copia vecchia se ripeti lo stesso percorso di origine. Quando aggiorni un file, copialo prima con un nome nuovo (es. `scheda_v6.js`) e fai il commit da lì. Poi **confronta l'md5** sul Mac e nel container prima di rigenerare e pubblicare.
- **Pubblicazione.** Sempre come anteprima privata, sullo stesso artefatto. Le pagine pubbliche si aggiornano solo dopo un mio esplicito «aggiorna la pagina pubblica».
- **Salvataggio.** Tutto deve rigenerarsi sul Mac con `python3 build.py`; con `--importa` riparte dal .tex.
- **Stato.** Aggiorna `claude/galileo-stato-del-progetto.md`.
- **Skill.** Quando impari qualcosa di generale, proponimi l'aggiornamento delle skill con lo strumento delle proposte.

Rispondimi sempre in italiano. Comincia leggendo stato e skill, apri nella scansione del 1638 le pagine latine del moto naturalmente accelerato e dimmi in poche righe:
- come pensi di costruire la scheda 2;
- dove l'argomento di Sagredo (fig. 44) e la dimostrazione di Galileo (fig. 43) coincidono e dove no.

Poi parti.
