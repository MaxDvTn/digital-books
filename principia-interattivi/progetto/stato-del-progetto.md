# Principia interattivi — stato del progetto

Aggiornato all'8 novembre 2026: **traduzione completa dei *Principia*** — Libri I, II e III tradotti (fascicoli 4–12, 13–20 e 21–27, v0.1); prompt della revisione complessiva pronto. Copia locale completa in `~/Projects/digital_books/principia-interattivi/`.

## Dove si trova tutto

| Cosa | Dove |
|---|---|
| Pagina interattiva (pilota v0.4.1, verificata) | Artefatto Claude «Principia interattivi — Libro I»: https://claude.ai/artifact/2g29gFSukgWTxrQ1QdwNAk (slug 0d8bdaa9-e9f3-4571-8549-cdb0f0855ab9). Copia locale: `verifiche/index_v041.html` |
| Skill | `editore-libri-scientifici-interattivi` (proposta di aggiornamento: fonte latina, glossario, font); `verifica-dimostrazioni-interattive` |
| Fascicoli 1–27 | `traduzione/` (01 v0.2, 02 v0.1, 03 v0.3, 04–12 v0.1, 13–20 v0.1 con 18a e 18b, 21–27 v0.1 con 24a/b, 25a/b, 26a/b) |
| Latino 1726 | `fonti/latino-1726/` (33 file per sezione) e `fonti/fonte_la.md`, `fonte_fm.md` |
| Motte 1846 | `fonti/motte-1846/` (Libri I e II per sezione, Libro III per gruppi come il latino) e `fonti/fonte_en.md`. **`fonti/motte-1846/svg_tex.tsv`**: il LaTeX di tutte le 1361 formule SVG di Motte (attributo data-tex dell'EPUB) |
| EPUB Gutenberg #76404 | `fonti/Newton's_Principia____The_mathematical_principles_of_natural_philosophy_by_Newton.3.epub` (completo, 7,6 MB). La copia `fonti/pg76404-images-3.epub` è **troncata** (628 KB) e inutilizzabile: da eliminare |
| Libro II | `libro2/PROMPT-libro-II.md`, `libro2/ISTRUZIONI-TRADUTTORE.md` (addendum e glossario dati ai traduttori), `libro2/pacchetto-libro-II.zip` |
| Libro III | `libro3/PROMPT-libro-III.md`, `libro3/ISTRUZIONI-TRADUTTORE.md` (addendum e glossario dati ai traduttori), `libro3/pacchetto-libro-III.zip` |
| **Revisione** | `revisione/PROMPT-revisione.md` (copia nel progetto claude.ai: `claude/prompt-revisione.md`) |
| Strumenti | `strumenti/` (BRIEF.md, check.py, extract.py, parteB.py, estrai_motte_L3.py, rinumera.py per le parti «b» dei fascicoli divisi). `check.py` ora riconosce anche gli identificatori `II.S7.01` e `III.G2.01` (resta compatibile con `S5.01`) |
| Stampe consultabili | Latino 1726, scansione ECCO: Internet Archive `bim_eighteenth-century_philosophiae-naturalis-p_newton-sir-isaac_1726`. Motte 1729, vol. I: `bub_gb_Tm0FAAAAQAAJ` |
| README | `progetto/README-repository.md` (licenza CC BY-SA 4.0 + MIT) |

## Libro I — fascicoli

| Fasc. | Contenuto | Identificatori | Parte B |
|---|---|---|---|
| 4 | Sez. I, Lemmi I–XI | S1.01–48 | 11 unità, 32 passi |
| 5 | Sez. II, Propp. I–X, Lemma XII | S2.01–67 | 14 unità, 52 passi |
| 6 | Sez. III–IV, Propp. XI–XXI, Lemmi XIII–XVI | S3.01–50, S4.01–29 | 15 unità, 123 passi |
| 7 | Sez. V, Lemmi XVII–XXVII, Propp. XXII–XXIX | S5.01–87 | 22 unità, 185 passi |
| 8 | Sez. VI–VIII, Propp. XXX–XLII, Lemma XXVIII | S6–S8, 63 id. | 16 unità, 114 passi |
| 9 | Sez. IX–X, Propp. XLIII–LVI | S9–S10, 63 id. | 14 unità, 94 passi |
| 10 | Sez. XI, Propp. LVII–LXIX (tre corpi) | S11.01–72 | 5 unità, 55 passi |
| 11 | Sez. XII, Propp. LXX–LXXXIV, Lemma XXIX | S12.01–69 | 15 unità, 85 passi |
| 12 | Sez. XIII–XIV, Propp. LXXXV–XCVIII | S13–S14, 53 id. | 11 unità, 78 passi |

Tradotti da traduttori in parallelo con un brief comune. Controllo di coerenza del coordinatore:
- `check.py` superato da tutti i fascicoli;
- identificatori senza buchi;
- glossario uniforme. Unica armonizzazione: *orbis* nel senso di strato sferico → «guscio» nei Fascicoli 11 e 12.

Le verifiche numeriche di ogni fascicolo sono nelle note.

## Libro I — punti principali per il curatore (dai rapporti dei traduttori)

- **Errori di formula in Motte 1846** (SVG dell'EPUB), da confrontare con Motte 1729 per attribuirli:
  - Prop. XI: PE²;
  - Prop. XII: frazione capovolta;
  - Scolio della Sez. III: CG²;
  - Sez. VI: SVG 115 e 134;
  - Sez. IX: SVG 193, 195, 199, 240;
  - Sez. XII: SVG 280;
  - Sez. XIII: SVG 191, 311, 338, 344, 347, 348;
  - Scolio dopo il Lemma X: A al posto di B.
- **Errori di senso di Motte:**
  - *sagitta* resa sempre «versed sine»;
  - *hyperbola opposita* resa «conjugate»;
  - Lemma XXII: definizione di parallele cambiata;
  - Prop. LXXXVI: «attractive» per «attratto»;
  - vari rimandi sbagliati.
- **Refusi probabili della trascrizione** (decine, elencati in ogni fascicolo), da controllare sulla stampa ECCO. I più rilevanti:
  - Prop. XVII: *SP+AH* per *SP+PH*;
  - Lemma XXVIII: lacuna;
  - Prop. XL, Cor. 2;
  - Prop. XLI: radici perse;
  - Prop. XLV, Es. 1: −FF[X];
  - Prop. LXXXIII.
- **Letture incerte o punti geometrici non definiti nel testo:**
  - Lemma XI;
  - Prop. XIX: due tangenti;
  - Prop. XLIV: punto R;
  - Lemma XXVII: punto E;
  - Prop. LVIII: Cor. VI o V delle Leggi;
  - Prop. XCIII: n > 3.
- **Note da verificare:** alcune notizie storiche nelle note dei Fascicoli 10 (N12, N16) e 12 (N13, N15) non vengono dalle fonti allegate e sono segnate come «non verificate».
- Motte 1846, Prop. LXVI, Cor. 19: chiude con una frase che manca nella trascrizione del 1726; va controllata sulle edizioni latine precedenti.

## Libro II — fascicoli

| Fasc. | Contenuto | Identificatori | Parte B |
|---|---|---|---|
| 13 | Sez. I, Propp. I–IV, Lemma I | II.S1.01–27 | 7 unità, 35 passi |
| 14 | Sez. II, Propp. V–X, Lemma II e Scolio, Regole | II.S2.01–77 | 13 unità, 116 passi |
| 15 | Sez. III–IV, Propp. XI–XVIII, Lemma III | II.S3.01–31, II.S4.01–28 | 10 unità, 79 passi |
| 16 | Sez. V, Propp. XIX–XXIII, idrostatica | II.S5.01–34 | 6 unità, 68 passi |
| 17 | Sez. VI, Propp. XXIV–XXXI, Scolio con gli esperimenti sui pendoli | II.S6.01–65 | 6 unità, 62 passi |
| 18a | Sez. VII (1), Propp. XXXII–XXXVII, Lemma IV | II.S7.01–64 | 9 unità, 89 passi |
| 18b | Sez. VII (2), Lemmi V–VII, Propp. XXXVIII–XL, Scolio con gli esperimenti di caduta | II.S7.65–130 | 5 unità, 29 passi |
| 19 | Sez. VIII, Propp. XLI–L, suono | II.S8.01–47 | 7 unità, 62 passi |
| 20 | Sez. IX, Ipotesi, Propp. LI–LIII, Scolio sui vortici | II.S9.01–32 | 2 unità, 29 passi |

Tradotti da nove traduttori in parallelo con `strumenti/BRIEF.md` e `libro2/ISTRUZIONI-TRADUTTORE.md`. Controllo di coerenza del coordinatore:
- `check.py` superato da tutti i fascicoli, senza avvisi;
- identificatori consecutivi, senza buchi né doppioni; `id` delle unità della Parte B unici in tutto il Libro II;
- 18b rinumerato dal coordinatore (+14) per proseguire il 18a;
- tutte le formule SVG di Motte del Libro II controllate sul LaTeX dell'EPUB (`svg_tex.tsv`); nessuna resta da vedere;
- rimandi al Libro I (Lemmi VII, VIII e X; Propp. IV, IX, XXXIV, XXXVIII, LI, LII) verificati sui fascicoli 4–12: reggono tutti.

### Libro II — glossario

Oltre al glossario del prompt e ai termini fissati in `libro2/ISTRUZIONI-TRADUTTORE.md`:
- armonizzato: *divisim* → «separando» (Fasc. 15 corretto; il Libro I resta non uniforme: «separando», «per separazione», «dividendo»);
- *medium similare* e *fluidum homogeneum* → entrambi «omogeneo» (la distinzione latina si perde; segnalata nel Fasc. 20, § A.0);
- **da decidere (curatore):** *plaga* è «parte» nel Fasc. 3, «verso» nel 18a (dove compare insieme a *determinatio* = «direzione»), «direzione» o «parte» nel 19. Proposta: «direzione» per l'orientamento di un moto, «verso» solo quando accanto c'è *determinatio*, «parte» per una regione;
- **da decidere:** *lentor* «cedevolezza» (Fasc. 20); *impulsus* nel Cor. 5 della Prop. XX «impulso» (Fasc. 16);
- *rigor* «rigidità» (13) e *tenacitas* «tenacità» (15, 18b) sono parole latine diverse e restano distinte.

## Libro II — punti principali per il curatore (dai rapporti dei traduttori)

- **Letture della trascrizione che il calcolo (e Motte) smentiscono**, tradotte secondo il senso con integrazione tra quadre, da controllare sulla stampa ECCO:
  - Prop. XIV, Cor.: *ad lineam ED* per BD;
  - Prop. XV, Cor. 8: *numerum* per *tempus*; radici perse nella Prop. XV;
  - Prop. XIX: «Cor. VI» citato nella Sez. VIII (p. 358) è il Caso 6;
  - Prop. XXII, Cor.: *Aa−Cc* per *Aa−Bb* (p. 291);
  - Prop. XXIX: OC per OS; Scolio della Sez. VI: 7/22 AV per 7/11, «⅓» per ½ pollice;
  - Prop. XXXVI, Caso 6: *accelerabit* senza negazione (p. 332); Cor. 8: manca *dimidium*;
  - Prop. XXXVIII, Cor. 2: manca *densitas globi ad*; Prop. XL: *A ad A−* senza B; Esper. 14: «1936″» per 19 ⅜″;
  - Sez. II, Regola 7: «2AI» dove la formula dà (4/3)AI (non corretto); Regola 4: *paulo minore* contro Motte «a little greater» (indeciso);
  - Sez. I: il Caso 2 della Prop. II è duplicato nella trascrizione (artefatto).
- **Cifre di Newton che non tornano** (non corrette nel testo): tabella della Prop. XL, velocità a 8G (99999980 contro 99999977,5); Scolio della Sez. VI, 0,041748 contro 0,041778 e 0,61675 contro 0,61705; Esper. 13, due righe dei globi d'aria (≈3 pollici).
- **Errori di formula in Motte 1846** (SVG): 356 (Prop. IV), 434, 453, 456, 469, 501, 524 (Sez. II), 547 (BD² per BD³), 582 (½ per ¼), 671, 695 (Sez. VI), 749–750 (Prop. XL: «− 4,405…» per «+ 4,605…»), 926 (π per φ, Prop. XLVII). Da confrontare con Motte 1729 (vol. II da cercare su Internet Archive).
- **Errori di senso di Motte:** «Book I» per Book II e «Law I» per Legge II (Sez. I); «axis AK» per AX (Prop. IX); *unciæ Romanæ* «ounces troy»; «of the pendulum» aggiunto nella Prop. XLIX; «in the following Book» per *in mundi systemate*; vari pesi sbagliati nelle tabelle della Sez. VII.
- **Scolio al Lemma II:** il testo del 1726 nomina Collins, Sluse e Hudde e non Leibniz. Le fonti allegate (latino 1726 e Motte, che traduce il 1726) non permettono di documentare la differenza con le edizioni del 1687 e del 1713: la nota relativa è marcata «non verificato sulle fonti allegate».
- **Fisica, nelle note:** Propp. LI–LII (Newton eguaglia le impressioni, non i momenti: i tempi verrebbero r² e r³); Prop. XXVII non confermata dal calcolo moderno; coefficiente 7/10 dello Scolio della Sez. VI (valore esatto 0,6955); Prop. XLVI (onde) sottostima del 20 %; velocità del suono (≈298 m/s, correzione di Laplace in nota).
- **Non verificato:** stampa ECCO 1726 (ogni fascicolo ha la tabella «Punti da controllare sulla stampa ECCO»), figure originali NATP00088, paginazione di Motte 1846 (gli estratti non hanno marcatori di pagina), Motte 1729.

## Libro III — fascicoli

| Fasc. | Contenuto | Identificatori | Parte B |
|---|---|---|---|
| 21 | Introduzione, Regole I–IV, Fenomeni I–VI | III.G1.01–33 | 10 unità, 0 passi (dati delle tabelle) |
| 22 | Propp. I–XIV, Ipotesi I | III.G2.01–56 | 21 unità, 122 passi |
| 23 | Propp. XV–XIX, Prop. XX (figura della Terra, pendoli) | III.G3.01–20, III.G4.01–14 | 7 unità, 114 passi |
| 24a | Propp. XXI–XXIX (precessione, maree, Luna fino alla variazione) | III.G5.01–36 | 9 unità, 86 passi |
| 24b | Propp. XXX–XXXIII, scolio con le Propp. I–II di Machin | III.G5.37–63 | 11 unità, 124 passi |
| 25a | Propp. XXXIV–XXXVII, Scolio delle equazioni lunari, maree | III.G6.01–43 | 10 unità, 80 passi |
| 25b | Prop. XXXVIII, Lemmi I–III, Ipotesi II, Prop. XXXIX, Lemma IV, Prop. XL, Lemmi V–XI | III.G6.44–102 | 19 unità, 107 passi |
| 26a | Prop. XLI: costruzione, cometa del 1680 con sei tabelle | III.G7.01–50 | 2 unità, 55 passi |
| 26b | Prop. XLI: code e atmosfere delle comete | III.G7.51–70 | 5 unità, 33 passi |
| 27 | Prop. XLII e Scolio generale | III.G8.01–28, III.G9.01–15 | 8 unità, 36 passi |

Tradotti da dieci traduttori in parallelo con `strumenti/BRIEF.md`, `libro2/ISTRUZIONI-TRADUTTORE.md` e `libro3/ISTRUZIONI-TRADUTTORE.md`. Controllo di coerenza del coordinatore:
- `check.py` superato da tutti i fascicoli, senza avvisi;
- identificatori consecutivi, senza buchi né doppioni; `id` della Parte B unici in tutto il Libro III;
- 24b, 25b e 26b rinumerati dal coordinatore con `strumenti/rinumera.py` (numerati in origine da 101);
- tutte le formule SVG di Motte del Libro III controllate sul LaTeX di `svg_tex.tsv`; l'SVG 961 è stato visto anche come immagine (esponente «2 4/243» reso come D² · 4/243);
- rimandi ai Libri I e II verificati sui fascicoli 1–20: reggono tutti tranne due (vedi sotto).

### Libro III — glossario

Oltre al glossario del prompt e ai termini fissati in `libro3/ISTRUZIONI-TRADUTTORE.md`:
- *digitus* come misura di lunghezza «pollice» in tutti i fascicoli (come nel Libro II); «dito» resta per le eclissi;
- *mediocris*: «medio» in tutto il Libro III, **tranne nel Fasc. 24b** (Propp. XXX–XXXIII e Machin), dove *motus mediocris* «moto mediocre» si distingue da *motus medius* «moto medio» (moto delle tavole): la distinzione serve al calcolo dei nodi. **Da decidere (curatore)** se estendere la distinzione;
- terzi, quarti, quinti scritti ‴ ⁱᵛ ᵛ nel testo tradotto (uniformato dal coordinatore nei Fasc. 25a e 25b; le citazioni latine restano come nella trascrizione, «33iv»);
- nomi degli astronomi in forma italiana o moderna (Flamsteed, Halley, Montanari, Cassini, Huygens); *Ponthæus* resta in forma latina;
- **da decidere:** *jubar* «splendore» (il Fasc. 26b propone «fascio» quando è il fascio di luce solare); *declinatio* della coda (26b propone «scostamento»); *copia materiæ* «quantità di materia» (22, distinta solo in nota da *quantitas materiæ*); *e regione solis* «di lato al Sole» (21); *splendor* «luminosità» (26b);
- *sensorium*: previsto nel glossario del coordinatore, ma **non compare** nello Scolio generale del 1726 né in Motte; il Fasc. 27 lo spiega nella nota N14 e non lo introduce nel testo.

## Libro III — punti principali per il curatore (dai rapporti dei traduttori)

- **Cifre di Newton che non tornano** (non corrette nel testo; ogni fascicolo ha le note con i ricalcoli):
  - Fenomeno IV: periodo di Venere 224,6176 g (dalla distanza 72333 viene 224,700); distanza di Saturno 954006 (dal periodo 953799); Fenomeni I–II: 9,494 (9,492) e 23,35 (23,31);
  - Prop. VIII, Cor. 1–2: massa della Terra 1/169282, mentre i dati danno ≈1/193600, che è il valore coerente con il peso 435 e la densità 400 stampati da Newton; Saturno 1/3021 (ricalcolo 1/3092);
  - Prop. III: 2 4/243 e 59 ¾ corrispondono a 3° esatti di moto dell'apogeo, non a 3° 3′;
  - Prop. XIX: arco di 1433,46 piedi in un secondo (dai dati 1430,41; rapporto finale ≈290 invece di 289);
  - Propp. XXVI–XXIX: 11023 (11023,7), 8° 24′ (8° 22′ 45″), 33′ 14″ e 37′ 11″ (33′ 16″ e 37′ 13″);
  - Prop. XXXIII: 9° 11′ 3″ non è la metà di 18° 19′ 5″ 53‴ (torna partendo dal moto delle tavole, 19° 21′ 21″ 50‴);
  - Scolio della Prop. XXXV: equazione massima dei nodi 9′ 24″ (≈9′ 21″); 33 7/8 per 33 5/6; Prop. XXXVII, Cor. 7: 15,11175 piedi (15,1183) e seno verso 12752341 (12752196);
  - Prop. XXXVIII: 1081 : 100 (il prodotto dà 1090 : 100); Prop. XXXIX: 17 1/6 miglia contro le 17 1/10 della Prop. XIX; Scolio del Lemma VIII: coefficiente 27MI : 16Mμ (il calcolo dà 12MI : 16Mμ);
  - Prop. XLI: diverse cifre delle tabelle della cometa del 1680 (19.9.43 per 19.19.43; 14021 per 84021; segni degli errori del 30 dic. e del 5 mar.); nodo ascendente dell'ellisse in ♋ incoerente con le parabole; nella seconda parte, «diebus totidem» contro «annis 50000», ora del 28 dicembre (i luoghi tornano verso le 11 del mattino);
  - Prop. XLII: **fattore 2** nelle equazioni «2G − 2C» e «2T − 2S» (latino e Motte): il metodo funziona solo senza il 2; «primæ arietis» per la seconda stella; quattro cifre nelle tabelle del 1665, 1683 e 1723.
- **Rimandi che non tornano:** Prop. X, «Scolio della Prop. XXII del Libro II» per l'aria a 200 miglia (nel 1726 lo scolio non contiene il calcolo); Prop. XXII, «corol. 2 prop. lxvi» per il Cor. 11 (corretto come «Cor. [11]», lettura di Motte).
- **Letture della trascrizione smentite dal calcolo o da Motte** (da controllare sulla stampa ECCO, elencate in ogni fascicolo): tabella di Pound del 9 marzo «12⅔ ad 14⅔» (Motte 11⅔); «sol» per *luna* (Prop. XXIV); «sectorem TNb» per TBb; «signum anguli» per *sinus*; «AIC» per AIq (Lemma IX); γ per ♈ nel Lemma IV; Kirch, 3 nov., ♎ per ♌; cifre del 1723 dove Motte torna e la trascrizione no.
- **Errori di formula in Motte 1846** (SVG): 961 (esponente), 995 (1/289 per 1/229), 878 (manca il 6), 1036 (− per +, Prop. XXVIII), 1079 e 1088 (frazioni), 1164 (⅔ per ⅓), 1169 (λ per γ), 1272; 11 letture nel Fasc. 26a (§ A.9).
- **Errori di senso di Motte:** Regole II–IV (*ejusdem generis* «the same», aggiunta di «a principle of mutual gravitation», *tollatur* «evaded»); «60 diameters» per semidiametri; *æquatio semestris* «semi-menstrual»; declinazione 23° 13′ per 22° 13′; Keplero e le code; «electric and elastic Spirit» aggiunto nello Scolio generale; λ per γ nella Prop. XLI.
- **Scolio generale:** le fonti allegate non documentano le differenze con le edizioni del 1713 e del 1687; nessuna variante annotata. Le note su *sensorium*, *Ottica* e Leibniz–Clarke sono marcate «non verificato».
- **Fisica, nelle note:** Lemma III (somma delle quantità di moto, non momento d'inerzia: fattore dell'anello +15,5 %); Lemma IV (costruzione instabile con la Terra in moto su orbita curva, da riesaminare); verifiche moderne dei valori marcate «non verificato sulle fonti allegate».
- **Non verificato:** stampa ECCO 1726, figure originali, paginazione di Motte 1846, Motte 1729.

## Decisioni del curatore (8/11/2026)

- *constanter* → «senza interruzione»;
- *impulsu unico sed magno* → «con un impulso unico ma grande»;
- *in directum* → «in linea retta»;
- *determinatio* → «direzione»;
- *nisi quatenus* → «se non in quanto»;
- licenza CC BY-SA 4.0 + MIT;
- strategia: prima la traduzione completa, poi la progettazione del libro digitale, dove si riprendono i problemi delle dimostrazioni del pilota.

## Prossimi passi

1. **Revisione complessiva** (Fascicoli 1–27) in una nuova chat del progetto, con `revisione/PROMPT-revisione.md` (copia in `claude/prompt-revisione.md`): refusi sulla stampa ECCO, SVG di Motte su Motte 1729, revisione indipendente a campione.
2. Decisioni di glossario aperte: Libro II (*plaga*, *lentor*, *impulsus* nella Prop. XX) e Libro III (*mediocris*, *jubar*, *declinatio* della coda, *copia materiæ*).
3. Dopo la revisione: progettazione del libro digitale (template delle pagine, problemi noti nelle dimostrazioni, livelli di interattività).
