# Prompt per la traduzione del Libro III dei *Principia* (nuova chat del progetto «Digital Book»)

**Prima di incollare questo prompt:** apri la nuova chat collegata al computer (app desktop di Claude) e concedi l'accesso alla cartella `~/Projects/digital_books`. Non serve allegare nulla: Motte 1846 del Libro III è già estratto in `fonti/motte-1846/motte-1846-L3-*.md`, il LaTeX di tutte le 1361 formule SVG di Motte è in `fonti/motte-1846/svg_tex.tsv`, e l'EPUB Gutenberg #76404 completo è in `fonti/` (`Newton's_Principia____The_mathematical_principles_of_natural_philosophy_by_Newton.3.epub`; la copia `pg76404-images-3.epub` è troncata e inutilizzabile). Se la cartella non è raggiungibile, allega l'EPUB completo e il pacchetto `libro3/pacchetto-libro-III.zip`.

---

Agisci come redattore di un'edizione scientifica, con la competenza di un latinista, di uno storico della scienza, di un astronomo e di un fisico. Il progetto è un'edizione didattica e interattiva in italiano dei *Principia* di Newton, pensata per il liceo scientifico. Il curatore è Massimo Bosetti.

## Dove si trova il progetto

Tutto il lavoro si trova sul computer del curatore, in `~/Projects/digital_books/principia-interattivi/`:

| Cartella | Contenuto |
|---|---|
| `traduzione/` | Fascicoli 1–20: Definizioni, Scolio, Leggi, Libro I (4–12), Libro II (13–20, con 18a e 18b) |
| `fonti/latino-1726/` | Latino 1726 per gruppi. Per questo lavoro servono i 9 file `latino-1726-L3-*.md` |
| `fonti/motte-1846/` | Motte 1846: Libri I e II per sezione, Libro III nei 9 file `motte-1846-L3-*.md` (stessi gruppi dei file latini), e `svg_tex.tsv` con il LaTeX di tutte le formule SVG |
| `strumenti/` | `BRIEF.md` (brief comune), `check.py` (validazione; accetta identificatori `II.S7.01` e `III.G2.01`), `extract.py`, `parteB.py` |
| `libro2/` | Prompt del Libro II e `ISTRUZIONI-TRADUTTORE.md` (l'addendum usato dai traduttori del Libro II, utile come modello) |
| `progetto/` | `stato-del-progetto.md` e `README-repository.md` |
| `libro3/` | Questo prompt e `pacchetto-libro-III.zip` (ripiego: brief, check.py, istruzioni del Libro II, modelli, fonti L3 latine e Motte, svg_tex.tsv) |

Lo stato del lavoro è in `progetto/stato-del-progetto.md` (copia nel progetto claude.ai, `claude/stato-del-progetto.md`).

## Come lavorare con la cartella locale

1. Con `device_list_dir` controlla la cartella, poi porta nel container i file che servono con `device_stage_files` (al massimo 50 file per chiamata):
   - `strumenti/BRIEF.md`, `strumenti/check.py`, `libro2/ISTRUZIONI-TRADUTTORE.md`;
   - i 9 file latini e i 9 di Motte del Libro III, più `fonti/motte-1846/svg_tex.tsv`;
   - i modelli `traduzione/Newton_Principia_IT_03_Leggi.md` e `traduzione/Newton_Principia_IT_05_L1_S02.md`;
   - i fascicoli 04–20, per verificare i rimandi ai Libri I e II.
2. Lavora in `/home/claude/libro3/`, sulla copia portata nel container.
3. Riporta i risultati sul computer con `device_commit_files`, sempre dentro `~/Projects/digital_books/principia-interattivi/`. Non cancellare e non rinominare i file esistenti.

**Formule di Motte.** Per controllare una formula `[SVG n]` basta cercare `n` in `svg_tex.tsv` («n<TAB>latex»). Per i casi dubbi estrai l'EPUB completo in `/home/claude/src_epub/` e rendi l'immagine con `rsvg-convert -h 120 -b white /home/claude/src_epub/OEBPS/3191938728343764116_n.svg -o /tmp/f.png`. L'estrazione di Motte L3 si rifà, se serve, con `strumenti/estrai_motte_L3.py` (legge i file 76404-h-19…25 dell'EPUB). Le tabelle sono rese con «|» riga per riga: l'allineamento delle colonne va ricontrollato sul latino.

## Compito

Traduci integralmente il **Libro III** (*De mundi systemate*) in fascicoli, con lo stesso metodo e lo stesso formato dei Libri I e II.

**Metodo (deciso dal curatore).**
1. Leggi `BRIEF.md`, `libro2/ISTRUZIONI-TRADUTTORE.md`, i due modelli e questo prompt. Prepara un `ISTRUZIONI-TRADUTTORE.md` per il Libro III, adattando quello del Libro II con l'addendum qui sotto.
2. Avvia **traduttori in parallelo**, uno per fascicolo, tutti con lo stesso brief.
3. Quando ricevi i fascicoli, controlla tu la coerenza:
   - il glossario è uniforme tra i fascicoli e con i Libri I–II;
   - gli identificatori non hanno buchi;
   - ogni fascicolo supera `check.py`:
     ```
     python3 check.py FASC.md fonti/latino-1726-L3-xxx.md --en fonti/motte-1846-L3-xxx.md
     ```
   - i rimandi interni e quelli ai Libri I e II sono corretti, da verificare sui fascicoli in `traduzione/`.
4. Consegna:
   - salva i fascicoli in `traduzione/` sul computer (`Newton_Principia_IT_21_L3_Regole-Fenomeni.md` e così via, vedi tabella);
   - mandali anche come file nella chat;
   - aggiorna `progetto/stato-del-progetto.md` sul computer e `claude/stato-del-progetto.md` nel progetto claude.ai.
5. Prima di chiudere, prepara un prompt per la **revisione complessiva** (Fascicoli 1–27: refusi sulla stampa ECCO, SVG di Motte, revisione indipendente a campione) e salvalo in `revisione/PROMPT-revisione.md` e nel progetto claude.ai (`claude/prompt-revisione.md`).

**Ripartizione suggerita** (tra parentesi la dimensione del latino):

| Fascicolo | Contenuto | Latino |
|---|---|---|
| 21 | Introduzione al Libro III, *Regulæ philosophandi*, *Phænomena* (14 KB) | `L3-Regole-Fenomeni` |
| 22 | Propp. I–XIV, Ipotesi I (34 KB) | `L3-P01-14` |
| 23 | Propp. XV–XX: tempi periodici, figura della Terra, gravità a diverse latitudini (23 KB) | `L3-P15-19`, `L3-P20` |
| 24a / 24b | Propp. XXI–XXXIII: precessione, moti della Luna; con le Propp. I–II dello scolio (Machin). Dividi al confine di una proposizione (60 KB) | `L3-P21-33` |
| 25a / 25b | Propp. XXXIV–XL, Lemmi I–XI, Ipotesi II: maree, figura della Luna, precessione, comete. Dividi al confine di un lemma o di una proposizione (68 KB) | `L3-P34-40` |
| 26a / 26b | Prop. XLI: orbita della cometa del 1680, con le grandi tabelle di osservazioni. Dividi al confine di un esempio o di una tabella (58 KB) | `L3-P41` |
| 27 | Prop. XLII e *Scholium generale* (24 + 11 KB) | `L3-P42`, `L3-ScholiumGenerale` |

Il Libro III non è diviso in Sezioni. Gli identificatori seguono lo schema `**[III.G2.01]**`: prima il libro, poi il gruppo (G1 = Regole e Fenomeni, G2 = Propp. I–XIV, G3 = Propp. XV–XIX, G4 = Prop. XX, G5 = Propp. XXI–XXXIII, G6 = Propp. XXXIV–XL, G7 = Prop. XLI, G8 = Prop. XLII, G9 = Scolio generale, nell'ordine dei file latini), poi il numero a due cifre. `check.py` riconosce questa forma. Nei fascicoli divisi (24a/24b ecc.) la seconda parte riparte dal numero successivo all'ultimo della prima.

## Addendum al brief per il Libro III

**Parte B.** Gli `id` seguono lo schema `L3-P10`, `L3-Lem4`, `L3-Reg1`, `L3-Phaen5`. Il campo "fascicolo" vale "21-L3-Regole" e così via.

**Glossario aggiuntivo (proposta; da confermare con il curatore se possibile, altrimenti vincolante).**

| Latino | Italiano |
|---|---|
| *regulæ philosophandi* | «regole del filosofare» |
| *phænomenon* | «fenomeno» |
| *hypothesis* | «ipotesi» (*hypotheses non fingo*: «non invento ipotesi», con nota) |
| *systema mundi* | «sistema del mondo» |
| *planeta primarius / secundarius* | «pianeta primario / secondario» (= satellite, in nota) |
| *comites* (di Giove e Saturno) | «satelliti», con nota |
| *aphelium / perihelium* | «afelio / perielio» |
| *nodi* | «nodi»; *linea nodorum* «linea dei nodi» |
| *præcessio æquinoctiorum* | «precessione degli equinozi» |
| *æstus maris* | «maree» (*fluxus / refluxus* «flusso / riflusso») |
| *cometa* | «cometa»; *cauda* «coda» |
| *parallaxis* | «parallasse» |
| *variatio* (della Luna) | «variazione» |
| *æquatio* | «equazione» (correzione astronomica), con nota |
| *Sol, Luna, Tellus/Terra* | «Sole, Luna, Terra» (maiuscola per i corpi celesti) |
| *gravitas universalis* | «gravità universale» |
| *ætheris / spiritus subtilissimus* (Scolio generale) | «etere» / «spirito sottilissimo» |

Valgono anche i termini consolidati nei Libri I e II: vedi `libro2/ISTRUZIONI-TRADUTTORE.md` (glossario del Libro II e termini fissati dal coordinatore), i § A.0 dei fascicoli 13–20 e la sezione «Libro II — glossario» di `progetto/stato-del-progetto.md`. Già presenti nel Libro II e da riusare: *aphelium / perihelium* «afelio / perielio», *ecliptica* «eclittica», *materia cœlestis* «materia celeste», *vortex* «vortice», *mediocris distantia* «distanza media», *ratio sesquialtera / sesquiplicata* «rapporto sesquialtero / sesquiplicato», *divisim* «separando», *pes / digitus / granum / uncia / libra* «piede / pollice / grano / oncia / libbra», *argentum vivum* «mercurio».

Ogni altro termine nuovo va fissato nel § A.0 del primo fascicolo che lo usa. Il coordinatore lo trasmette poi agli altri traduttori.

**Tabelle numeriche e osservazioni astronomiche.** Il Libro III contiene molte tabelle (tempi periodici e distanze dei pianeti e dei satelliti, osservazioni della cometa del 1680, gradi di meridiano, pendoli a diverse latitudini). Riproducile e controlla l'aritmetica con uno script (per esempio la terza legge di Keplero sulle tabelle dei *Phænomena*). Segnala ogni cifra che non torna, senza correggerla nel testo. Le date e le coordinate astronomiche si lasciano come nel testo (calendario giuliano, ore e minuti come in Newton), con nota dove serve.

**Refusi già noti di Motte 1846.** Alcune formule, stampate come immagini, sono sbagliate (vedi lo stato del progetto, Libri I e II). Se una formula di Motte non torna con il latino, segnalala. Motte 1729 è consultabile su Internet Archive: il vol. I è `bub_gb_Tm0FAAAAQAAJ`, il vol. II va cercato.

**Punti dubbi della trascrizione latina.** La stampa del 1726 si può consultare sulla scansione ECCO di Internet Archive (`bim_eighteenth-century_philosophiae-naturalis-p_newton-sir-isaac_1726`). Se la sessione non riesce a raggiungerla, elenca i punti per un controllo successivo.

**Scolio generale.** È il testo più citato dei *Principia*. Traducilo con cura particolare; annota le differenze rispetto alle edizioni precedenti **solo se risultano dalle fonti allegate**.

## Decisioni del curatore già prese (valgono anche qui)

- *constanter* → «senza interruzione»
- *impulsu unico sed magno* → «con un impulso unico ma grande»
- *in directum* → «in linea retta»
- *determinatio* → «direzione»
- *nisi quatenus* → «se non in quanto»
- licenza: testi CC BY-SA 4.0, codice MIT. Il latino del Newton Project resta nella cartella di lavoro e non si ridistribuisce.

**Lezioni dal Libro II (per il coordinatore).**
- Avvia i traduttori solo dopo aver controllato che `svg_tex.tsv` sia nel container: chi lo usa controlla tutte le formule in pochi minuti.
- Nei fascicoli divisi, assegna in anticipo il primo identificatore della seconda parte solo in modo provvisorio e rinumera alla fine con uno script che sposti **anche i numeri senza prefisso** nelle serie («II.S7.72–73», «II.S7.104, 107»).
- Il limite d'uso può interrompere i traduttori a metà: il lavoro resta salvato in `tmp/` e si riprende inviando un messaggio all'agente interrotto.

**Da non fare in questa chat:** le pagine interattive. Il curatore le progetterà dopo la traduzione.
