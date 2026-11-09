# Prompt per la traduzione del Libro II dei *Principia* (nuova chat del progetto «Digital Book»)

**Prima di incollare questo prompt:** apri la nuova chat collegata al computer (app desktop di Claude) con accesso alla cartella `~/Projects/digital_books`. Allega soltanto l'EPUB Gutenberg #76404 (`pg76404-images-3.epub`). Serve per leggere le formule di Motte, che sono stampate come immagini SVG.

Se la cartella locale non è raggiungibile, allega anche `libro2/pacchetto-libro-II.zip`. È un ripiego che contiene gli stessi brief, script, fonti e modelli.

---

Agisci come redattore di un'edizione scientifica, con la competenza di un latinista, di uno storico della scienza e di un fisico. Il progetto è un'edizione didattica e interattiva in italiano dei *Principia* di Newton, pensata per il liceo scientifico. Il curatore è Massimo Bosetti.

## Dove si trova il progetto

Tutto il lavoro si trova sul computer del curatore, in `~/Projects/digital_books/principia-interattivi/`:

| Cartella | Contenuto |
|---|---|
| `traduzione/` | Fascicoli 1–12: Definizioni, Scolio, Leggi e Libro I (Fascicoli 4–12) |
| `fonti/latino-1726/` | Latino 1726 per sezione. Per questo lavoro servono `latino-1726-L2-S01.md` … `L2-S09.md`; ci sono anche i file del Libro III, `L3-*.md` |
| `fonti/motte-1846/` | Motte 1846 per sezione: Libro I e Libro II (`motte-1846-L2-S01.md` … `L2-S09.md`) |
| `strumenti/` | `BRIEF.md` (il brief comune del Libro I), `check.py` (lo script di validazione), `extract.py`, `parteB.py` |
| `progetto/` | `stato-del-progetto.md` e `README-repository.md` |
| `libro2/` | Questo prompt e il pacchetto di ripiego |
| `verifiche/` | Il rapporto e gli script di verifica del pilota interattivo |

Lo stato del lavoro è descritto in `progetto/stato-del-progetto.md`. Una copia si trova nel progetto claude.ai, in `claude/stato-del-progetto.md`.

## Come lavorare con la cartella locale

1. Con `device_list_dir` controlla la cartella, poi porta nel container i file che servono, con `device_stage_files` (al massimo 50 file per chiamata):
   - `strumenti/BRIEF.md` e `strumenti/check.py`;
   - le 9 sezioni latine e le 9 di Motte del Libro II;
   - i modelli di formato `traduzione/Newton_Principia_IT_03_Leggi.md` e `traduzione/Newton_Principia_IT_05_L1_S02.md`.
2. Lavora in `/home/claude/libro2/`, sulla copia portata nel container.
3. Riporta i risultati sul computer con `device_commit_files`, sempre dentro `~/Projects/digital_books/principia-interattivi/`. Non cancellare e non rinominare i file che esistono già.

## Compito

Traduci integralmente il **Libro II** (*De motu corporum*, Sezioni I–IX) in fascicoli. Usa lo stesso metodo e lo stesso formato del Libro I.

**Metodo (deciso dal curatore).**
1. Leggi `BRIEF.md`, i due modelli e questo prompt.
2. Avvia **traduttori in parallelo**, uno per fascicolo, tutti con lo stesso brief.
3. Quando ricevi i fascicoli, controlla tu la coerenza:
   - il glossario è uniforme tra i fascicoli;
   - gli identificatori non hanno buchi;
   - ogni fascicolo supera `check.py`:
     ```
     python3 check.py FASC.md fonti/latino-1726-L2-Sx.md --en fonti/motte-1846-L2-Sx.md
     ```
   - i rimandi tra le Sezioni sono corretti, compresi quelli al Libro I, da verificare sui fascicoli in `traduzione/`.
4. Consegna:
   - salva i fascicoli in `traduzione/` sul computer, con i nomi `Newton_Principia_IT_13_L2_S01.md` e così via;
   - mandali anche come file nella chat;
   - aggiorna `progetto/stato-del-progetto.md` sul computer e `claude/stato-del-progetto.md` nel progetto claude.ai.
5. Prima di chiudere, prepara il lavoro per il **Libro III**:
   - estrai Motte 1846 del Libro III dall'EPUB e salvalo in `fonti/motte-1846/motte-1846-L3-*.md`, con gli stessi gruppi dei file latini `L3-*.md`;
   - scrivi un prompt analogo a questo e salvalo in `libro3/PROMPT-libro-III.md`. Il prompt deve usare la stessa cartella e lo stesso metodo;
   - salva lo stesso prompt anche nel progetto claude.ai, in `claude/prompt-traduzione-libro-III.md`.

**Ripartizione suggerita** (tra parentesi la dimensione del latino):

| Fascicolo | Contenuto |
|---|---|
| 13 | Sez. I, resistenza proporzionale alla velocità (15 KB) |
| 14 | Sez. II, resistenza proporzionale al quadrato della velocità, con il Lemma II sui momenti (41 KB) |
| 15 | Sez. III–IV (15 + 12 KB) |
| 16 | Sez. V, densità e compressione dei fluidi, idrostatica (24 KB) |
| 17 | Sez. VI, pendoli in mezzi resistenti (46 KB) |
| 18 | Sez. VII, moto dei fluidi e resistenza dei proiettili (79 KB). Dividila tra due traduttori, 18a e 18b, al confine di una proposizione |
| 19 | Sez. VIII, moto propagato nei fluidi, suono (31 KB) |
| 20 | Sez. IX, moto circolare dei fluidi, vortici (24 KB) |

Gli identificatori seguono lo schema `**[II.S7.01]**`: prima il libro, poi la sezione, poi il numero.

## Addendum al brief per il Libro II

**Parte B.** Gli `id` seguono lo schema `L2-P10`, `L2-Lem2`. Il campo "fascicolo" vale "13-L2-S1" e così via.

**Glossario aggiuntivo (vincolante).**

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
| *pulsus* (Sez. VIII) | «pulsazione», con una nota alla prima occorrenza: non è l'«impulso» della Prop. I |
| *tempus periodicum* | «tempo periodico» |
| *in ratione velocitatis* | «in rapporto alla velocità» (proporzionale alla velocità) |
| *in duplicata ratione velocitatis* | «in rapporto duplicato della velocità» |

Valgono anche i termini consolidati nel Libro I:

| Latino | Italiano |
|---|---|
| *orbis*, nel senso di strato sferico | «guscio» |
| *sagitta* | «saetta» |
| *sinus versus* | «seno verso» |
| *applicare ad* | «dividere per» |
| *corpusculum* | «corpuscolo» |
| *coire* | «riunirsi» |

Ogni altro termine nuovo va fissato nel § A.0 del primo fascicolo che lo usa. Il coordinatore lo trasmette poi agli altri traduttori.

**Tabelle numeriche.** Il Libro II contiene molte tabelle, per esempio gli esperimenti sui pendoli e sulla caduta nell'aria e nell'acqua. Riproducile e controlla l'aritmetica con uno script. Segnala ogni cifra che non torna, senza correggerla nel testo.

**Scolio al Lemma II (Sez. II).** Contiene il passo sul calcolo dei momenti e sul carteggio con Leibniz, nella forma del 1726. Traducilo con cura. Annota la differenza rispetto alle edizioni precedenti **solo se risulta dalle fonti allegate**.

**Refusi già noti di Motte 1846.** Alcune formule, stampate come immagini, sono sbagliate: per esempio PE² invece di PE³ nella Prop. XI del Libro I. Se una formula di Motte non torna con il latino, segnalala. Motte 1729 è consultabile su Internet Archive: il vol. I è `bub_gb_Tm0FAAAAQAAJ`, il vol. II va cercato.

**Punti dubbi della trascrizione latina.** La stampa del 1726 si può consultare sulla scansione ECCO di Internet Archive (`bim_eighteenth-century_philosophiae-naturalis-p_newton-sir-isaac_1726`). Se la sessione non riesce a raggiungerla, elenca i punti per un controllo successivo.

## Decisioni del curatore già prese (valgono anche qui)

- *constanter* → «senza interruzione»
- *impulsu unico sed magno* → «con un impulso unico ma grande»
- *in directum* → «in linea retta»
- *determinatio* → «direzione»
- *nisi quatenus* → «se non in quanto»
- licenza: testi CC BY-SA 4.0, codice MIT. Il latino del Newton Project resta nella cartella di lavoro e non si ridistribuisce.

**Da non fare in questa chat:** le pagine interattive. Il curatore le progetterà dopo la traduzione, ripartendo dai problemi già noti nelle dimostrazioni del pilota.
