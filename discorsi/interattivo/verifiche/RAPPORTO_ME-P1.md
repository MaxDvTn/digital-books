# Rapporto di revisione esterna: scheda «Il moto equabile: "comunque presi" e il Teorema I» (ME-P1)

Revisore esterno, 8 novembre 2026. Ho seguito la skill `verifica-dimostrazioni-interattive`, nell'ordine A → D.

Materiali controllati:
- le scansioni p151 e p152, lette per bande ingrandite 2×;
- `ME-P1.json`, `scheda_equabile.html`, `scheda_equabile.js`, `equabile_modello.js`, `verifica_equabile.py`;
- `index.html`, aperto con Chrome headless.

Ho controllato anche che nel libro la scheda sia identica ai file sorgente: la sezione `#equabile`, il JS e il JSON di `index.html` coincidono byte per byte con i file. L'unica differenza è il segnaposto `%%FAC_EQ%%`, sostituito dall'immagine in base64.

---

## A. Fedeltà al testo

### A1. Trascrizione latina rispetto alla stampa del 1638: **FALLITO** (due difetti, facili da correggere)

Ho confrontato parola per parola la Definitio, l'Admonitio, gli Axiomata I–IV, l'enunciato e le 9 frasi della dimostrazione. Tutto coincide, tolte le normalizzazioni dichiarate in `fonte_latino`, salvo queste due differenze:

| Dove | Stampa 1638 | JSON | Tipo |
|---|---|---|---|
| p152, r. 23–24 (frase 6) | «& si G B majus sit **quàm** B H, etiam I E, **quàm** E K majus erit» | «quam … quam» | Accento omesso, normalizzazione non dichiarata. L'accento grave viene invece conservato altrove («à mobili», «à majori»), quindi non è una scelta coerente. |
| p151, r. 1–2 | «CIRCA Motum æquabilem, seu uniformem unica opus habemus definitione, quam ejusmodi profero.» | assente da `latino_preliminari` | Omissione. Il pannello «Il latino del 1638» viene presentato come completo (commento a `scheda_equabile.js:261`), e il libro riporta la frase italiana corrispondente della UTET («Circa il moto equabile o uniforme, ci occorre una sola definizione…»). |

Correzioni:
- ripristinare «quàm» due volte, oppure dichiarare in `fonte_latino` «accenti gravi soppressi» e toglierli ovunque;
- aggiungere in testa a `latino_preliminari` la riga `["", "Circa Motum æquabilem, seu uniformem unica opus habemus definitione, quam ejusmodi profero."]`.

Verificati come corretti, tra gli altri: «versus G H & I K», «temporisque F E», «demonstrandum», «Motu» maiuscolo nell'Assioma I, «quatuor», «eandem habet rationem quam tertia & quarta».

### A2. Traduzione italiana, frase per frase

**Frase 7: FALLITO.** Il latino ha «hæc **vel** una æquari, **vel** una deficere, **vel** una excedere tempus EK & spatium BH». La traduzione dice «questi insieme sono eguali, insieme minori, insieme maggiori». Senza il «vel … vel … vel» si legge che le grandezze sono contemporaneamente eguali, minori e maggiori. È proprio il passaggio in cui si applica Euclide V, def. 5.
- Correzione: «…ed è stato dimostrato che questi **o** sono insieme eguali, **o** insieme minori, **o** insieme maggiori del tempo EK e dello spazio BH…».

Tutte le altre frasi sono fedeli: nessuna omissione, nessuna aggiunta, nessun concetto moderno. Sulle scelte discutibili:

- **«egualmente moltiplici» per *æque multiplicia*: SUPERATO.** È la resa tradizionale; Galileo stesso, in italiano, scrive «egualmente multiplici». Suggerisco una glossa al primo uso: «(oggi: equimultipli)».
- **«tempo del moto» per *tempus lationis*: SUPERATO con osservazione.** Appiattisce la variazione *motus*/*latio*, ma è coerente con l'enunciato UTET («i tempi dei moti» per *tempora lationum*). Cambiarla creerebbe un'incoerenza con il testo del libro.
- **«dunque» per *enim* (frase 0): accettabile.** Rendere con «infatti» o «Ora» sarebbe più letterale.
- **Nota editoriale 1** (*quam tertia & quarta* = *tertia ad quartam*): corretta.

### A3. Citazioni dal testo UTET: **SUPERATO**

- La citazione dell'Avvertenza («può accadere … non siano eguali.») è una sottostringa letterale del testo del libro che precede la scheda (verificato con `in` su `index.html`).
- L'enunciato del Teorema 1 nella scheda (`scheda_equabile.html:16`) coincide con quello del libro.
- «comunque presi» è presente.

### A4. Corrispondenza tra frasi e passi; `dipende_da`: **SUPERATO**

- Le 9 frasi compaiono tutte, ciascuna in un solo passo, distribuite sui 7 passi.
- Nessuna nota di passo inventa contenuto.
- `dipende_da` = DEF, A1, A2, Euclide V def. 5. Galileo non cita nulla esplicitamente; il testo usa la definizione («cum motus ponatur æquabilis»), l'Assioma II (implicito nel «majus … majus») e l'Assioma I (caso eguale, vedi B3). Euclide non è nominato, ma la frase 7 ne riprende la formula. Le dipendenze vanno bene.

### A5. Nota editoriale 2 (Ms. Gal. 72): **DUBBIO**

Non ho potuto verificarla offline. La nota chiama «trascrizione del sito» la resa di Ms. Gal. 72, ma Ms. Gal. 72 è un manoscritto di appunti di Galileo, non una trascrizione della stampa del 1638. Una lezione diversa («EE», «demostrandum») potrebbe essere del manoscritto, non un errore di chi lo trascrive.
- Correzione: verificare sul facsimile del manoscritto, oppure riformulare la nota come «la trascrizione online di … legge …». Per gli studenti non serve: valutare se toglierla.

---

## B. Correttezza matematica

### B1. Ricostruzione della dimostrazione: **SUPERATO**

Ricostruzione dal latino:
1. AB è percorso nel tempo DE, BC nel tempo EF, nello stesso moto equabile.
2. Si prolungano le linee: a sinistra AG contiene un numero qualsiasi di copie di AB, e ID altrettante copie di DE. Quindi BG = m·AB e EI = m·DE, con m = copie in AG + 1. A destra, analogamente, BH = n·BC e EK = n·EF.
3. Per la definizione (tempi eguali → spazi eguali), ogni tempo DE copre uno spazio eguale ad AB; per somma, EI è il tempo di BG. Lo stesso vale per EK e BH.
4. Nello stesso moto: se GB > BH allora IE > EK (Assioma II); se minore, minore; se eguale, eguale.
5. Questo vale per moltiplici qualsiasi. Per Euclide V def. 5 (prima AB, seconda BC, terza DE, quarta EF): AB : BC = DE : EF.

L'appaiamento è corretto: GB (multiplo della prima) va confrontato con BH (della seconda), e IE (della terza) con EK (della quarta), con lo stesso m per prima e terza e lo stesso n per seconda e quarta. Così fanno il modello (`equabile_modello.js:25`) e la frase 7. Euclide V ammette ragioni di specie diversa ai due lati (spazi contro tempi), e la scheda lo spiega bene nella nota al passo 2.

### B2. Costruzione e figura: **SUPERATO** (con un'osservazione sull'etichetta di m, in D)

Ho misurato le posizioni dall'incisione (p152, ritaglio 2×):
- **Linea dei tempi:** I, sette tacche, D, E, F, quattro tacche, K. Quindi EI = 8·DE e EK = 5·EF.
- **Linea degli spazi:** G, sette tacche, A, B, C, quattro tacche, H. Quindi BG = 8·AB e BH = 5·BC.
- **Disposizione:** tempi sopra, spazi sotto. G e I a sinistra, H e K a destra.

L'SVG rispetta questa disposizione: le stesse lettere, i tempi sopra, G/I a sinistra, H/K a destra. Le tacche intermedie sono a passo AB o DE a sinistra e a passo BC o EF a destra (`scheda_equabile.js:115,121`).

«Nell'incisione le due linee hanno scale diverse» è vero:
- AB : BC ≈ 84 : 118 ≈ 0,71, mentre DE : EF ≈ 75 : 92 ≈ 0,82;
- la linea dei tempi è più corta di quella degli spazi.

Piccola imprecisione nell'`alt` del facsimile: «linea dei tempi … con tacche eguali». Le tacche sono eguali solo su ciascun lato, con un passo diverso a sinistra e a destra. Correzione: «con tacche a passo DE a sinistra e a passo EF a destra».

### B3. Ipotesi implicite e note editoriali: **SUPERATO** (nota 3 corretta), con aggiunte consigliate

Ipotesi implicite che ho individuato:
1. **Il moto esiste anche su GA e su CH.** «Protrahantur utrinque» presuppone che il mobile si muova con lo stesso moto equabile anche prima di A e dopo C, cioè su tutto GH. La scheda lo assume senza dirlo (la corsa parte da G).
2. **Additività** di spazi e tempi contigui: il tempo di BG è la somma dei tempi delle copie.
3. **Tricotomia** tra grandezze omogenee: maggiore, eguale o minore.
4. **Caso eguale.** GB = BH ⇒ IE = EK non è un assioma: segue dall'Assioma I per assurdo (se IE > EK allora GB > BH). La nota editoriale 3 lo dice correttamente.
5. **Basta l'Assioma II.** Gli Assiomi III e IV non servono. La velocità entra solo come «stesso moto».

Correzione proposta: aggiungere le ipotesi 1–2 in «Come è fatta» o nella nota del passo 3.

### B4. Passaggio al limite: non applicabile

La dimostrazione non usa limiti. La quantificazione «per ogni m, n» è resa onestamente come limitata a 12 (vedi C e D).

---

## C. Controllo numerico (codice eseguito)

### C1. Lo script dei curatori `verifica_equabile.py`: **FALLITO così com'è consegnato**, SUPERATO nella struttura attesa

- Eseguito nella cartella consegnata, termina con `FileNotFoundError: …/dimostrazioni/ME-P1.json` (exit 1): il JSON non è in `dimostrazioni/`.
- Copiato in una cartella con `dimostrazioni/ME-P1.json` (nella cartella consegnata non ho modificato nulla), stampa «Tutti i controlli superati».
- I messaggi dei controlli 2, 3 e 4 (righe 41, 56, 84) vengono stampati **sempre**, anche in caso di errore. Solo il riepilogo finale è affidabile.

Correzioni:
- percorso relativo con fallback (`os.path.join(QUI, "ME-P1.json")`);
- messaggi condizionati all'esito del singolo controllo.

### C2. Il mio controllo indipendente (`/tmp/rev/mio_controllo.py`, in aritmetica esatta con `Fraction`)

Non riusa il codice dei curatori. I tempi IE ed EK sono ricavati dagli istanti di passaggio del mobile per B e per H, non dalla formula s/v sui segmenti. Risultati:

| Prova | Esito |
|---|---|
| Tesi: 2000 configurazioni casuali (AB, BC, v) × m, n ≤ 40 = 3 200 000 confronti | **0 discordanze**. AB/BC = DE/EF esatto in tutti i casi. **SUPERATO** |
| Controprova k = 4/5, AB = 2, BC = 3 | **12 caselle discordi**: (3,2), (5,3), (6,4), (7,4), (8,5), (9,5), (9,6), (10,6), (11,6), (11,7), (12,7), (12,8). Sono esattamente quelle con n·BC ≤ m·AB ≤ 1,25·n·BC. La pagina ne mostra 12 con bordo spesso (contate nel DOM). **SUPERATO** |
| Controprova con altri dati (AB = BC = 1; AB = ½, BC = 4) | Compaiono anche caselle del tipo (spazi >, tempi =), per esempio (m, n) = (5, 4) con AB = BC: lì EK **eguaglia** IE, non lo supera. Rilevante per la risposta 5, vedi D6. |
| √2 : 1, m, n ≤ 12 | Nessuna eguaglianza, né esatta (2m² = n² impossibile) né in virgola mobile con la tolleranza 1e-9. Scarto relativo minimo 1,0 % in (7, 10). 0 discordanze. La pagina mostra «Nessuna casella discorda su 144 (e nessuna ha «=»…)». **SUPERATO** |
| Mobile a scatti | Mezze battute 0,8 / 0,2. Con 3 parti: 0,533 / 0,333 / 0,133. Con 4…6 parti, spazi mai tutti eguali; eguali solo con la battuta intera. La pagina mostra «0,8 · 0,2 braccia» e «a scatti: no». **SUPERATO** |
| Modello JS contro Python esatto: 302 casi (300 casuali sui valori dei cursori, con e senza controprova, più 2 casi √2) × 144 caselle | **0 difformità**. Posizione del mobile a scatti a 41 istanti: scarto massimo 4,4·10⁻¹⁶. **SUPERATO** |

Nota tecnica: in un primo passaggio il mio script, costruendo `Fraction(0.8)` dal float, segnalava 142 falsi «tempi non eguali». La tolleranza relativa di 1e-9 del modello JS (`equabile_modello.js:8-11`) è quindi **necessaria** e corretta: senza, la controprova mostrerebbe «<» dove i tempi sono eguali.

---

## D. Interfaccia e didattica

Prove eseguite con Chrome headless (Playwright) a 375 (touch, DPR 2), 768 e 1280 px. Script in `/tmp/rev/ui.py`, `libro2.py`, `grid.py`, `p1.py`; screenshot in `/tmp/rev/shots/`.

### D1. Console, overflow, intestazione: **SUPERATO**

- **Errori e avvisi in console:** 0 alle tre larghezze, sia nella pagina continua sia nella modalità Libro.
- **Overflow orizzontale:** scrollWidth = clientWidth (375/375, 768/768, 1280/1280); nessun elemento di `#equabile` esce dal viewport.
- **Intestazione fissa:** alta 53, 87 e 59 px su 800 (meno di un quarto).
- **Link interno:** dopo `#equabile` il titolo è a 87, 89 e 89 px, sotto l'intestazione (53, 87, 59). Non resta coperto; a 768 px il margine è di soli 2 px.
- `alert(` è assente.

### D2. Ogni passo mostra solo gli oggetti introdotti: **SUPERATO per la figura**, **DUBBIO per i controlli**

Misurato nel DOM a ogni passo:

| Passo | Contenuto visibile |
|---|---|
| 1 | Solo A–F |
| 2 | A–F e «AB : BC = DE : EF ?» |
| 3 | Più G e I |
| 4 | Più H e K |
| 5 | Le quattro graffe e il pulsante della corsa |
| 6 | I confronti GB/BH e IE/EK |
| 7 | La griglia |

Corretto.

Però i cursori m e n, e i pulsanti √2 e Controprova, sono visibili e attivi fin dal passo 1. Inoltre la scala della figura dipende da m e n anche quando G, H, I, K sono nascosti (`scheda_equabile.js:97-101`). Al passo 1 con m = 12 i segmenti AB e BC sono schiacciati all'estrema destra di una figura vuota (screenshot `passo1_m12.png`).
- Correzione: nascondere i cursori m e n fino ai passi 3–4, oppure calcolare la scala solo sugli oggetti visibili.

### D3. Configurazioni degeneri senza avviso: **FALLITO**

- Con m = 1 G coincide con A e I con D; con n = 1 H coincide con C e K con F. Le lettere si sovrappongono e diventano illeggibili («GA», «ID», «CH», «FK» sovrapposte; screenshot `m1n1_375.png`).
- Con m = 12, n = 1, AB = 4, BC = 0,5:
  - E, F e K si accavallano, e così B, C e H;
  - l'etichetta «EK = 1 volte E…» esce dal viewBox ed è tagliata (`estremo_1280.png`).
- Nessun avviso in nessuno dei due casi.

Correzioni:
- con m = 1 o n = 1 scrivere una sola lettera, per esempio «A≡G», oppure partire da m, n ≥ 2 (come nell'incisione, dove AG non è vuoto);
- con segmenti sotto una soglia, spostare le lettere o mostrare un avviso;
- ancorare le etichette delle graffe dentro il viewBox.

### D4. Bersagli cliccabili ≥ 44 px e alternative da tastiera

- **Pulsanti, cursori e `summary`: SUPERATO.** Nessun bersaglio sotto i 44 px alle tre larghezze. «Apri la scheda» misura 121×44.
- **Caselle della griglia: FALLITO.** Misurano **25,4 px** a 375 e **31,7 px** a 768 e 1280. L'alternativa da tastiera esiste (i cursori m e n), e il tocco funziona: ho provato (7,5), (1,1), (12,12) e (4,9), con mouse e con touchscreen, e m e n si aggiornano correttamente. La griglia invece non è focalizzabile (`tabindex` assente) e un tocco sui numeri dei margini porta a (1,1) per via del clamping (`scheda_equabile.js:257`).
  - Correzione: dichiararlo esplicitamente («su telefono usa i cursori»), oppure ingrandire la griglia a tutta larghezza sul telefono; ignorare i tocchi fuori dalle caselle.
- **Frecce ←/→:** cambiano passo, ignorate dentro gli `input`. Funzionano.

### D5. Pulsanti e leggibilità sul telefono

- **Pulsanti: SUPERATO.** Tutti funzionano: la corsa termina con «▶ Di nuovo»; il latino si mostra e si nasconde; √2 dà 0 discordanze e nessun «=»; la controprova dà 12 caselle; la griglia si apre al passo 7.
- **Font nelle figure a 375 px: DUBBIO.**

  | Figura | Font minimo / massimo (px CSS) |
  |---|---|
  | Due mobili | 10 / 12 |
  | Figura del teorema | 10 / 17 (9,7 nella modale Libro) |
  | Griglia | **8,4 / 9,2** |

  La figura principale si legge (screenshot `fig_passo5_375.png`). I simboli e i numeri della griglia sono molto piccoli: `ingrandisci` non viene applicato a `#eqGrid`.
  - Correzione: applicare il fattore anche alla griglia, oppure portare i simboli a ≥ 11 px.
- **Etichetta di cifre con √2: DUBBIO lieve.** «AB · BC: √2 · BC · 3 braccia» sembra un prodotto. Correzione: «√2·BC ≈ 4,24 · 3 braccia».
- **Barre dei due mobili: osservazione.** L'altezza è ∝ spazio × numero di parti (`scheda_equabile.js:46`): rappresenta la velocità media, non lo spazio. All'interno di una stessa suddivisione il confronto è corretto, ma la didascalia «spazio percorso in ogni parte» fa pensare a uno spazio assoluto. Correzione: aggiungere «(scala adattata alla durata della parte)».

### D6. Modalità «📖 Libro»: **SUPERATO**

Alle tre larghezze la scheda compare nel flusso subito dopo l'enunciato del Teorema 1, come riquadro «TAVOLA INTERATTIVA», con il titolo «Il moto equabile: «comunque presi» e il Teorema I» (spread 274/487 a 375, 186/328 a 768, 150/264 a 1280).

Con «Apri la scheda ↗» la sezione viene spostata nella modale `lb-modale-corpo`:
- a tutta larghezza a 375 e 768 px; a 1280 px è una colonna centrata di 900 px;
- nessun overflow, nessun errore;
- i passi funzionano;
- con Esc la sezione torna in `#testo`.

### D7. Domande «Per la classe»

| Domanda | Esito | Nota |
|---|---|---|
| 1 (mobile a scatti) | **SUPERATO** | Numeri esatti (0,8 / 0,2). Osservazione: il moto non è «a scatti» ma a due velocità (veloce poi lento). «a due andature» sarebbe più esatto per uno studente. |
| 2 (moltiplici) | **SUPERATO** | |
| 3 (Assioma II, caso eguale) | **SUPERATO** | Giusto. «Assioma I usato al contrario» è vago: meglio «Assioma I, per assurdo». |
| 4 (√2) | **SUPERATO** | Corretta e ben motivata (incommensurabili). |
| 5 (controprova) | **DUBBIO** | Con i dati iniziali (2; 3) è esatta. In generale ci sono caselle discordi in cui EK **eguaglia** IE invece di superarlo (per esempio AB = BC, m = 5, n = 4: IE = EK = 5). Correzione: «…il tempo EK raggiunge o supera il tempo IE…». |

Altre osservazioni sulle note dei passi:
- **Passo 2, DUBBIO lieve.** «Non si può «dividere» uno spazio per un tempo», detto in assoluto, contraddice ciò che lo studente sa (v = s/t). Correzione: «Per Galileo, come per Euclide, non si può…».
- **Passo 3: etichetta di m.** «m, copie a sinistra» non torna con il modello (BG = m·AB), perché AG contiene m − 1 copie. Correzione: «m: BG = m volte AB».
- **Passo 7: testo fisso.** «nessuna casella discorda» resta scritto anche con la controprova attiva, mentre la griglia mostra 12 discordanze. Correzione: renderlo condizionato, oppure «con la stessa velocità nessuna casella discorda».

### D8. Lettura moderna

- **s = v·t e la definizione di Euclide: SUPERATO.** La formula di Euclide V def. 5 è scritta correttamente (m·a ⋛ n·b esattamente quando m·c ⋛ n·d).
- **Accenno a Dedekind: DUBBIO lieve.** Il 1872 (*Stetigkeit und irrationale Zahlen*) è giusto, e anche la caratterizzazione con le frazioni n/m sotto e sopra la ragione. «È la stessa idea» però è troppo forte: Euclide confronta ragioni già date, Dedekind con le sezioni *costruisce* i numeri che mancano (la completezza). Correzione: «un'idea molto vicina, che Dedekind userà nel 1872 per *costruire* i numeri reali».

### D9. «Come è fatta» rispetto al codice

| Dichiarazione | Esito e prova |
|---|---|
| Spazi e tempi alla stessa scala, allineati in G e in I | **Vera**: un solo `sc` per le due linee e `xG = xI = M` (`scheda_equabile.js:98-101`) |
| m e n fino a 12, nella figura e nella griglia | **Vera** (`max="12"`, `N_GRIGLIA = 12`) |
| Tolleranza 10⁻⁹ | **Vera**, ma è *relativa* (`TOLL·max(|a|,|b|,1)`). Suggerito: «tolleranza relativa» |
| Il mobile a scatti è inventato | **Vera e onesta** |
| Controprova all'80 % | **Vera** (`K_CONTRO = 0.8`) |
| Latino trascritto dalle pp. 151–152 | **Parzialmente vera**: manca la frase «Circa Motum…» e «quàm» è normalizzato (vedi A1) |
| Nell'incisione le due linee hanno scale diverse | **Vera** (vedi B2) |

---

## Riepilogo

| Controllo | Esito |
|---|---|
| A1 Trascrizione latina | FALLITO («quàm» ×2; frase «Circa Motum…» omessa) |
| A2 Traduzione | FALLITO sulla frase 7 («vel … vel … vel» perso); il resto è SUPERATO |
| A3 Citazioni UTET | SUPERATO |
| A4 Frasi, passi, dipendenze | SUPERATO |
| A5 Nota Ms. Gal. 72 | DUBBIO |
| B1 Ricostruzione | SUPERATO |
| B2 Figura e incisione | SUPERATO (`alt` impreciso) |
| B3 Ipotesi implicite e note | SUPERATO (aggiungere: moto su tutto GH, additività) |
| C1 Script dei curatori | FALLITO così com'è consegnato (percorso; messaggi incondizionati) |
| C2 Controllo indipendente e confronto con JS | SUPERATO (0 discordanze; 12 caselle attese = 12 mostrate; 0 difformità JS) |
| D1 Console, overflow, intestazione | SUPERATO |
| D2 Oggetti per passo | SUPERATO per la figura; DUBBIO per i cursori m, n attivi fin dal passo 1 |
| D3 Configurazioni degeneri | FALLITO (lettere sovrapposte con m = 1 o n = 1; etichetta tagliata) |
| D4 Bersagli ≥ 44 px | FALLITO per le caselle della griglia (25–32 px; alternativa: cursori); SUPERATO il resto |
| D5 Pulsanti e leggibilità | Pulsanti SUPERATO; DUBBIO per la griglia a 8–9 px sul telefono |
| D6 Modalità Libro | SUPERATO |
| D7 Domande per la classe | SUPERATO 1–4; DUBBIO 5 («raggiunge o supera») |
| D8 Lettura moderna | SUPERATO, con DUBBIO lieve su «la stessa idea» (Dedekind) |
| D9 «Come è fatta» | Vere, salvo «latino trascritto» incompleto |

## Verdetto: **pubblicabile con riserve**

La matematica è corretta e ben verificata. La figura rispetta l'incisione, il modello JS coincide con un calcolo esatto indipendente, e l'interfaccia è funzionante e senza errori anche in modalità Libro.

Prima della pubblicazione vanno corretti:
1. **Traduzione della frase 7:** ripristinare «o … o … o».
2. **Trascrizione:** «quàm» ×2 e la frase introduttiva «Circa Motum æquabilem…» nel latino completo.
3. **Configurazioni degeneri:** con m = 1 o n = 1 le lettere si sovrappongono. Gestirle (m, n ≥ 2 o lettera unica) e tenere le etichette delle graffe dentro il viewBox.
4. **Risposta 5:** «raggiunge o supera».
5. **Nota del passo 7:** condizionata alla controprova.
6. **Griglia sul telefono:** caselle sotto i 44 px e testo a 8–9 px. Ingrandire, oppure rimandare esplicitamente ai cursori.
7. **Script di verifica:** percorso del JSON e messaggi condizionati.

Correzioni consigliate:
- cursori m e n nascosti fino al passo 3 o 4, ed etichetta «BG = m volte AB»;
- «Per Galileo» nella nota del passo 2;
- Dedekind: «idea molto vicina»;
- «tolleranza relativa» in «Come è fatta»;
- `alt` dell'incisione;
- nota su Ms. Gal. 72 da verificare o togliere;
- ipotesi implicite (moto su tutto GH) dichiarate;
- glossa «equimultipli»;
- etichetta delle cifre con √2.
