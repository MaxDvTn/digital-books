> **Copia pubblica.** In questa versione i campi `"la"` della Parte B sono vuoti: le frasi latine vengono dalla trascrizione del Newton Project, che non si ridistribuisce. Il latino del 1726 si legge su newtonproject.ox.ac.uk.

# Isaac Newton
# Principi matematici della filosofia naturale

## Fascicolo 26a — Libro III: Prop. XLI, l’orbita della cometa del 1680 (costruzione ed esempio)

**Nuova traduzione italiana di lavoro dal latino del 1726, confrontata con l’inglese di Andrew Motte nell’edizione del 1846.**

Versione 0.1 — 8 novembre 2026. Preparata con Claude (Anthropic) per Massimo Bosetti.

### Stato e perimetro

Questo fascicolo prosegue il Fascicolo 25b (Libro III, Prop. XXXVIII–XL e Lemmi I–XI). Traduce la **prima parte della Proposizione XLI** del Libro III (*Cometæ in parabola moti trajectoriam ex datis tribus observationibus determinare*): l’enunciato, la costruzione, la dimostrazione e la regola per scegliere i punti di prova; poi l’***Exemplum*** della cometa del 1680 con tutte le tabelle (osservazioni di Flamsteed corrette da Halley, osservazioni di Newton, posizioni delle fisse di Pound, orbita grafica di Newton, orbita parabolica e orbita ellittica di Halley), le osservazioni di Kirch e quelle di novembre di altri osservatori, fino al capoverso *Congruunt igitur hæ observationes cum theoria…* compreso. **Il seguito della Proposizione** (da *Cæterum trajectoriam quam cometa descripsit…*: la figura dell’orbita e della coda, la natura dei corpi delle comete, le code e le atmosfere) **è nel Fascicolo 26b.** È una traduzione di lavoro, non un’edizione critica validata.

Gli identificatori **III.G7.01–III.G7.50** e i titoli tematici tra parentesi sono aggiunte editoriali. Servono a orientare la lettura e a controllare la completezza. Il numero romano della proposizione e del problema appartiene al testo originale; i sottotitoli «Costruzione», «Dimostrazione», «Scelta dei punti di prova» ed «Esempio» sono editoriali (il solo *Exemplum* è nella stampa). Le integrazioni del curatore sono tra parentesi quadre. Le note sotto le tabelle e le note poste dopo la traduzione non fanno parte del testo di Newton.

In coda al fascicolo c’è la **Parte B**, con i dati strutturati per due unità: **L3-P41-Constr** (enunciato, costruzione e dimostrazione, un passo per frase latina) e **L3-P41-Ex** (l’esempio: passi per i capoversi di calcolo e di conclusione, e un campo `dati` con i valori delle sei tabelle e l’esito dei controlli). Il Fascicolo 26b userà l’unità `L3-P41-Caudae`.

### Fonti effettivamente consultate

1. **Latino di riferimento.** Isaac Newton, *Philosophiæ Naturalis Principia Mathematica*, terza edizione, Londra, 1726, Libro III, Prop. XLI, **pp. 492–506** (la proposizione comincia a p. 492, prima del marcatore ‹493›; il marcatore ‹506› manca nella trascrizione, che passa da ‹505› a ‹507›). Trascrizione normalizzata del Newton Project, documento **NATP00303**, estratta in testo semplice senza correzioni: `fonti/latino-1726/latino-1726-L3-P41.md`, righe 1–1906. Le tabelle vi sono spezzate in una cella per riga; le frazioni sono appiattite con caratteri invisibili (U+2064 fra intero e frazione: «32⁤12» = 32½; U+2062 fra frazione e lettera: «313⁢AE» = 3/13 AE; «⁤01» è un segnaposto vuoto di allineamento). Figure: due [FIG] nel testo della costruzione, non disponibili.
2. **Inglese di confronto.** *Newton’s Principia*, traduzione di Andrew Motte, New York, Daniel Adee, 1846, Book III, Prop. XLI (Project Gutenberg n. 76404), estratto `fonti/motte-1846/motte-1846-L3-P41.md`, righe 1–714. L’estratto non ha marcatori di pagina: le pagine Motte sono indicate come «sezione corrispondente». Le righe delle tabelle sono separate da «|»; le formule stampate come immagini compaiono come `[SVG n]`, lette sul LaTeX di `fonti/motte-1846/svg_tex.tsv`.
3. **Per i rimandi:** latino del Libro III, `fonti/latino-1726/latino-1726-L3-P34-40.md` (Prop. XL, Lemmi VI–XI); Fascicolo 6 (Libro I, Sezioni III–IV) per la Prop. XIX e la Prop. XVI del Libro I.
4. **Modelli e regole:** brief comune, addendum del Libro II, istruzioni del Libro III; Fascicoli 3, 5 e 20.

Non ho consultato né riprodotto traduzioni moderne. Non ho potuto vedere la stampa del 1726 né le figure originali: le relazioni geometriche della costruzione sono ricostruite dalle sole lettere del testo. Tutte le tabelle sono state ricostruite con uno script (`tmp/26a/t1.py`, `t2_6.py`, `gen_tabelle.py`) e verificate con altri script (`verifica.py`, `distanze.py`, `costruzione.py`, `stelle.py`, `cmp_motte.py`), descritti nelle note.

### Criteri di traduzione

- Il testo guida è il latino; l’inglese di Motte serve a controllare le interpretazioni ed è annotato quando aggiunge, omette o si discosta.
- Si applicano il **glossario comune** (*sagitta* «saetta», *latus rectum* «lato retto», *umbilicus* «fuoco», *trajectoria* «traiettoria», *ratio duplicata / subduplicata* «rapporto duplicato / subduplicato», *contentum sub* «contenuto sotto», *quamproxime* «con ottima approssimazione», Q.E.I. «C.V.T.»), quello del **Libro II** (*pes* «piede», *digitus* «pollice» come misura di lunghezza) e quello del **Libro III**: *cometa* «cometa», *cauda* «coda», *orbis magnus* «orbe magno», *aphelium / perihelium* «afelio / perielio», *nodi* «nodi», *ecliptica* «eclittica», *longitudo / latitudo* «longitudine / latitudine», *lat. bor. / austr.* «latitudine boreale / australe», *gradus* «grado», *minutum (primum) / secundum* «primo / secondo» (per i tempi «minuto / secondo»), *mediocris distantia* «distanza media», *inclinatio* «inclinazione», *stellæ fixæ* «stelle fisse», *telescopium* «telescopio», *micrometrum* «micrometro», *horizon* «orizzonte», *æquator* «equatore», *oppositio* «opposizione», *st. vet.* «secondo il calendario giuliano (stile vecchio)», *spica Virginis* «la Spiga della Vergine», i nomi dei corpi celesti con la maiuscola.
- I segni zodiacali restano come simboli (nota N1). Date, ore e coordinate restano come nel testo; i nomi dei mesi delle tabelle sono abbreviati all’italiana (dic., gen., feb., mar., nov.).
- **Tabelle.** Sono ricostruite come tabelle Markdown complete, con le colonne del latino e i numeri della trascrizione, separati dal punto come nella stampa (4.46.0 = 4h 46′ 0″; −3.5 = −3′ 5″). Le frazioni appiattite sono riportate alla forma della stampa (32½, 13⅔, 10 1/12). Nessuna cifra è corretta: le cifre che non tornano sono segnate con (a), (b) e discusse sotto la tabella e nella nota N2.
- Le frazioni nel testo corrente si scrivono con la barra (3/13 AE, Sμ + iλ/3); le frazioni di grado e di primo nella forma della stampa (20⅓′, 3½′).
- I nomi propri latinizzati sono resi nella forma moderna dove l’identificazione è sicura (Flamsteed, Halley, Pound, Kirch, Cassini, Hooke, Montanari, Ango, Storer, Zimmerman); restano latini *Ponthæus*, *Cellius*, *Galletius* (§ A.6). I nomi di luogo sono resi nella forma italiana corrente.
- Le estensioni del glossario proprie di questo fascicolo sono nel § A.0. Nessuna formula moderna entra nel testo tradotto.

---

## Traduzione italiana

### Proposizione XLI. Problema XXI (orbita parabolica di una cometa da tre osservazioni)

**[III.G7.01]** **Determinare la traiettoria di una cometa che si muove in una parabola, a partire da tre osservazioni date.**

**[III.G7.02]** Avendo affrontato in molti modi questo problema, di gran lunga il più difficile, ho composto nel Libro primo alcuni problemi che mirano alla sua soluzione. In seguito ho escogitato la soluzione seguente, un poco più semplice.

#### Costruzione

**[III.G7.03]** Si scelgano tre osservazioni separate l’una dall’altra da intervalli di tempo uguali con ottima approssimazione. L’intervallo di tempo in cui la cometa si muove più lentamente sia però un poco maggiore dell’altro: in modo, cioè, che la differenza dei tempi stia alla somma dei tempi come la somma dei tempi sta a seicento giorni circa; oppure che il punto E (nella figura del Lemma VIII) cada con ottima approssimazione nel punto M, e se ne scosti piuttosto verso I che verso A. Se non si dispone di osservazioni siffatte, si deve trovare un nuovo luogo della cometa per il Lemma VI.

**[III.G7.04]** Indichino S il Sole; T, t, τ tre luoghi della Terra nell’orbe magno; TA, tB, τC le tre longitudini osservate della cometa; V il tempo fra la prima e la seconda osservazione; W il tempo fra la seconda e la terza; X la lunghezza che la cometa potrebbe descrivere in tutto quel tempo con la velocità che ha alla distanza media della Terra dal Sole, lunghezza che si deve trovare per il Cor. 3 della Prop. XL del Libro III; e tV la perpendicolare sulla corda Tτ. Sulla longitudine osservata intermedia tB si prenda a piacere un punto B come luogo della cometa nel piano dell’eclittica, e di lì verso il Sole S si conduca la linea BE, che stia alla saetta tV come il contenuto sotto SB e St² sta al cubo dell’ipotenusa del triangolo rettangolo i cui lati sono SB e la tangente della latitudine della cometa nella seconda osservazione riferita al raggio tB. E per il punto E si conduca (per il Lemma VII di questo Libro) la retta AEC, le cui parti AE, EC, terminate alle rette TA e τC, stiano fra loro come i tempi V e W: A e C saranno con ottima approssimazione i luoghi della cometa nel piano dell’eclittica nella prima e nella terza osservazione, purché B sia il suo luogo assunto correttamente nella seconda.

**[III.G7.05]** Su AC, divisa a metà in I, innalza la perpendicolare Ii. Per il punto B conduci la linea occulta Bi parallela ad AC. Congiungi con una linea occulta Si, che tagli AC in λ, e completa il parallelogramma iIλμ. Prendi Iσ uguale a 3Iλ, e per il Sole S conduci la linea occulta σξ uguale a 3Sσ + 3Iλ. Cancellate ora le lettere A, E, C, I, dal punto B verso il punto ξ conduci una nuova linea occulta BE, che stia alla precedente BE in rapporto duplicato della distanza BS rispetto alla quantità Sμ + iλ/3. E per il punto E conduci di nuovo la retta AEC con la stessa regola di prima, cioè in modo che le sue parti AE ed EC stiano fra loro come i tempi V e W fra le osservazioni. E A e C saranno i luoghi della cometa con maggiore precisione.

**[III.G7.06]** Su AC, divisa a metà in I, s’innalzino le perpendicolari AM, CN, IO, delle quali AM e CN siano le tangenti delle latitudini nella prima e nella terza osservazione, riferite ai raggi TA e τC. Si congiunga MN, che tagli IO in O. Si costruisca come prima il rettangolo iIλμ. Su IA prolungata si prenda ID uguale a Sμ + 2iλ/3. Poi su MN, verso N, si prenda MP, che stia alla lunghezza X trovata sopra in rapporto subduplicato della distanza media della Terra dal Sole (ossia del semidiametro dell’orbe magno) rispetto alla distanza OD. Se il punto P cade nel punto N, A, B, C saranno tre luoghi della cometa per i quali si deve descrivere la sua orbita nel piano dell’eclittica. Se invece il punto P non cade nel punto N, sulla retta AC si prenda CG uguale a NP, in modo che i punti G e P giacciano dalla stessa parte della retta NC.

**[III.G7.07]** Con lo stesso metodo con cui i punti E, A, C, G sono stati trovati dal punto assunto B, dagli altri punti b e β, assunti a piacere, si trovino i nuovi punti e, a, c, g ed ε, α, κ, γ. Poi, se per G, g, γ si conduce la circonferenza di cerchio Ggγ, che tagli la retta τC in Z, Z sarà un luogo della cometa nel piano dell’eclittica. E se su AC, ac, ακ si prendono AF, af, αφ uguali rispettivamente a CG, cg, κγ, e per i punti F, f, φ si conduce la circonferenza di cerchio Ffφ, che tagli la retta AT in X, il punto X sarà un altro luogo della cometa nel piano dell’eclittica. Nei punti X e Z s’innalzino le tangenti delle latitudini della cometa riferite ai raggi TX e τZ, e si avranno due luoghi della cometa nella sua propria orbita. Infine (per la Prop. XIX del Libro I) con fuoco S si descriva per quei due luoghi una parabola: questa sarà la traiettoria della cometa. C.V.T.

#### Dimostrazione

**[III.G7.08]** La dimostrazione di questa costruzione segue dai lemmi: infatti la retta AC è tagliata in E nel rapporto dei tempi per il Lemma VII, come deve essere per il Lemma VIII; BE, per il Lemma XI, è la parte della retta BS, o Bξ, compresa nel piano dell’eclittica fra l’arco ABC e la corda AEC; e MP (per il Cor. del Lemma X) è la lunghezza della corda dell’arco che la cometa deve descrivere nella sua propria orbita fra la prima e la terza osservazione, e perciò sarà uguale a MN, purché B sia il vero luogo della cometa nel piano dell’eclittica.

#### Scelta dei punti di prova

**[III.G7.09]** Del resto conviene scegliere i punti B, b, β non a caso, ma vicinissimi al vero. Se è noto approssimativamente l’angolo AQt sotto cui la traccia dell’orbita descritta nel piano dell’eclittica taglia la retta tB, si dovrà condurre sotto quell’angolo la linea occulta AC, che stia a 4Tτ/3 in rapporto subduplicato di SQ a St. E conducendo la retta SEB, la cui parte EB sia uguale alla lunghezza Vt, si determinerà il punto B, che si può usare la prima volta. Poi, cancellata la retta AC e condotta di nuovo secondo la costruzione precedente, e trovata inoltre la lunghezza MP, si prenda su tB il punto b con questa regola: se TA e τC si tagliano a vicenda in Y, la distanza Yb stia alla distanza YB nel rapporto composto dal rapporto di MP a MN e dal rapporto subduplicato di SB a Sb. E con lo stesso metodo si dovrà trovare il terzo punto β, se si vuole ripetere l’operazione una terza volta. Ma con questo metodo per lo più basteranno due operazioni. Infatti, se la distanza Bb risulta piccolissima, trovati i punti F, f e G, g, le rette Ff e Gg, una volta condotte, taglieranno TA e τC nei punti cercati X e Z.

### Esempio (la cometa del 1680)

**[III.G7.10]** Si proponga la cometa dell’anno 1680. La tabella seguente ne presenta il moto osservato da Flamsteed e calcolato in base alle osservazioni, e corretto da Halley in base alle stesse osservazioni.

**[III.G7.11]** *Tabella 1 (Flamsteed, corretta da Halley).*

| Data (st. vet.) | Tempo apparente<br>h.′ | Tempo vero<br>h.′.″ | Longitudine del Sole<br>°.′.″ | Longitudine della cometa<br>°.′.″ | Latitudine boreale della cometa<br>°.′.″ |
|---|--:|--:|--:|--:|--:|
| 1680 dic. 12 | 4.46 | 4.46.0 | ♑ 1.51.23 | ♑ 6.32.30 | 8.28.0 |
| 21 | 6.32½ | 6.36.59 | 11.6.44 | ♒ 5.8.12 | 21.42.13 |
| 24 | 6.12 | 6.17.52 | 14.9.26 | 18.49.23 | 25.23.5 |
| 26 | 5.14 | 5.20.44 | 16.9.22 | 28.24.13 | 27.0.52 |
| 29 | 7.55 | 8.3.2 | 19.9.43 (a) | ♓ 13.10.41 | 28.9.58 |
| 30 | 8.2 | 8.10.26 | 20.21.9 | 17.38.20 | 28.11.53 |
| 1681 gen. 5 | 5.51 | 6.1.38 | 26.22.18 | ♈ 8.48.53 | 26.15.7 |
| 9 | 6.49 | 7.0.53 | ♒ 0.29.2 | 18.44.4 | 24.11.56 |
| 10 | 5.54 | 6.6.10 | 1.27.43 | 20.40.50 | 23.43.52 |
| 13 | 6.56 | 7.8.55 | 4.33.20 | 25.59.48 | 22.17.28 |
| 25 | 7.44 | 7.58.42 | 16.45.36 | ♉ 9.35.0 | 17.56.30 |
| 30 | 8.7 | 8.21.53 | 21.49.58 | ♉ 13.19.51 | 16.42.18 |
| feb. 2 | 6.20 | 6.34.51 | 24.46.59 | 15.13.53 | 16.4.1 |
| 5 | 6.50 | 7.4.41 | 27.49.51 | 16.59.6 | 15.27.3 |

*Note alla Tabella 1 (del curatore).* I numeri sono separati dal punto come nella stampa: 4.46.0 = 4h 46′ 0″; ♑ 1.51.23 = 1° 51′ 23″ del Capricorno. Il segno zodiacale è scritto solo quando cambia. Date secondo il calendario giuliano; ore contate dal mezzogiorno (tempo astronomico). (a) La trascrizione ha 19.9.43; il moto del Sole fra le righe vicine richiede 19.19.43, come in Motte (nota N2). Non corretto.

**[III.G7.12]** A queste aggiungi alcune delle nostre osservazioni.

**[III.G7.13]** *Tabella 2 (osservazioni di Newton).*

| Data (st. vet.) | Tempo apparente | Longitudine della cometa | Latitudine boreale della cometa |
|---|--:|--:|--:|
| 1681 feb. 25 | 08h.30′ | ♉ 26°.18′.35″ | 12°.46′.46″ |
| 27 | 08h.15′ | 27°.04′.30″ | 12°.36′.12″ |
| mar. 1 | 11h.00′ | 27°.52′.42″ | 12°.23′.40″ |
| 2 | 08h.00′ | 28°.12′.48″ | 12°.19′.38″ |
| 5 | 11h.30′ | 29°.18′.00″ | 12°.03′.16″ |
| 7 | 09h.30′ | ♊ 00°.04′.00″ | 11°.57′.00″ |
| 9 | 08h.30′ | 00°.43′.04″ | 11°.45′.52″ |

*Note alla Tabella 2 (del curatore).* Nella trascrizione le ore delle righe 2–7 hanno il segno «°» al posto di «h» (08°.15′ …): qui si scrive «h» (§ A.7). Il segno zodiacale è scritto solo quando cambia.

**[III.G7.14]** Queste osservazioni sono state compiute con un telescopio di sette piedi e con un micrometro e fili collocati nel fuoco del telescopio: con questi strumenti abbiamo determinato sia le posizioni delle stelle fisse fra loro, sia le posizioni della cometa rispetto alle fisse. Indichi A la stella di quarta grandezza nel calcagno sinistro di Perseo (ο di Bayer), B la stella seguente, di terza grandezza, nel piede sinistro (ζ di Bayer) e C la stella di sesta grandezza (n di Bayer) nel tallone dello stesso piede; e D, E, F, G, H, I, K, L, M, N, O, Z, α, β, γ, δ altre stelle minori nello stesso piede. E siano p, P, Q, R, S, T, V, X i luoghi della cometa nelle osservazioni descritte sopra. Posta la distanza AB di 80 7/12 parti, AC era di 52 1/4 parti, BC 58 5/6, AD 57 5/12, BD 82 6/11, CD 23 2/3, AE 29 4/7, CE 57 1/2, DE 49 11/12, AI 27 7/12, BI 52 1/6, CI 36 7/12, DI 53 5/11, AK 38 2/3, BK 43, CK 31 5/9, FK 29, FB 23, FC 36 1/4, AH 18 6/7, DH 50 7/8, BN 46 5/12, CN 31 1/3, BL 45 5/12, NL 31 5/7. HO stava a HI come 7 a 6 e, prolungata, passava fra le stelle D ed E, in modo che la distanza della stella D da questa retta fosse 1/6 CD. LM stava a LN come 2 a 9 e, prolungata, passava per la stella H. Così si determinavano le posizioni delle fisse fra loro.

**[III.G7.15]** Infine il nostro Pound ha osservato di nuovo le posizioni di queste fisse fra loro e ne ha riportato le longitudini e le latitudini nella tabella seguente.

**[III.G7.16]** *Tabella 3 (stelle fisse, posizioni di Pound).*

| Stella fissa | Longitudine<br>°.′.″ | Latitudine boreale<br>°.′.″ | Stella fissa | Longitudine<br>°.′.″ | Latitudine boreale<br>°.′.″ |
|---|--:|--:|---|--:|--:|
| A | ♉ 26.41.50 | 12.8.36 | L | ♉ 29.33.34 | 12.7.48 |
| B | 28.40.23 | 11.17.54 | M | 29.18.54 | 12.7.20 |
| C | 27.58.30 | 12.40.25 | N | 28.48.29 | 12.31.9 |
| E | 26.27.17 | 12.52.7 | Z | 29.44.48 | 11.57.13 |
| F | 28.28.37 | 11.52.22 | α | 29.52.3 | 11.55.48 |
| G | 26.56.8 | 12.4.58 | β | ♊ 0.8.23 | 11.48.56 |
| H | 27.11.45 | 12.2.1 | γ | 0.40.10 | 11.55.18 |
| I | 27.25.2 | 11.53.11 | δ | 1.3.20 | 11.30.42 |
| K | 27.42.7 | 11.53.26 |  |  |  |

*Note alla Tabella 3 (del curatore).* La stampa dispone le stelle in due colonne affiancate; la trascrizione le dà nell’ordine A, L, B, M, C, N, …, che qui si conserva. Le stelle D e O, citate nel testo, non sono in tabella. Motte ha per M «9.18.54» e «2.7.20» e per N «2.31.9»: i valori latini tornano con le distanze misurate da Newton, quelli di Motte no (nota N2).

**[III.G7.17]** Le posizioni della cometa rispetto a queste fisse le osservavo come segue.

**[III.G7.18]** Venerdì 25 febbraio, secondo il calendario giuliano (stile vecchio), alle ore 8½ p. m., la distanza della cometa, che si trovava in p, dalla stella E era minore di 3/13 AE e maggiore di 1/5 AE, e quindi uguale a 3/14 AE con buona approssimazione; e l’angolo ApE era alquanto ottuso, ma quasi retto. Cioè, se da A si abbassasse la perpendicolare su pE, la distanza della cometa da quella perpendicolare era 1/5 pE.

**[III.G7.19]** La stessa notte, alle ore 9½, la distanza della cometa, che si trovava in P, dalla stella E era maggiore di 1/(4½) AE e minore di 1/(5¼) AE, e quindi uguale a 1/(4⅞) AE, ossia a 8/39 AE, con ottima approssimazione. La distanza della cometa dalla perpendicolare abbassata dalla stella A sulla retta PE era poi 1/10 BF.

**[III.G7.20]** Domenica 27 febbraio, alle ore 8¼ p. m., la distanza della cometa, che si trovava in Q, dalla stella O uguagliava la distanza fra le stelle O e H, e la retta QO, prolungata, passava fra le stelle K e B. A causa delle nubi sopraggiunte non ho potuto definire con maggiore precisione la posizione di questa retta.

**[III.G7.21]** Martedì 1° marzo, alle ore 11 p. m., la cometa, che si trovava in R, giaceva esattamente fra le stelle K e C, e la parte CR della retta CRK era poco maggiore di 1/3 CK e poco minore di 1/3 CK + 1/8 CR, e quindi uguale a 1/3 CK + 1/16 CR, ossia a 16/45 CK.

**[III.G7.22]** Mercoledì 2 marzo, alle ore 8 p. m., la distanza della cometa, che si trovava in S, dalla stella C era 4/9 FC con ottima approssimazione. La distanza della stella F dalla retta CS prolungata era 1/24 FC, e la distanza della stella B dalla stessa retta era cinque volte maggiore della distanza della stella F. Inoltre la retta NS, prolungata, passava fra le stelle H e I, cinque o sei volte più vicina alla stella H che alla stella I.

**[III.G7.23]** Sabato 5 marzo, alle ore 11½ p. m., quando la cometa era in T, la retta MT era uguale a 1/2 ML, e la retta LT, prolungata, passava fra B e F, quattro o cinque volte più vicina a F che a B, staccando da BF, dalla parte di F, la sua quinta o sesta parte. E MT, prolungata, passava fuori dello spazio BF, dalla parte della stella B, quattro volte più vicina alla stella B che alla stella F. M era una stella piccolissima, che a stento si poteva vedere con il telescopio, e L una stella più grande, quasi di ottava grandezza.

**[III.G7.24]** Lunedì 7 marzo, alle ore 9½ p. m., quando la cometa era in V, la retta Vα, prolungata, passava fra B e F, staccando da BF, dalla parte di F, 1/11 BF, e stava alla retta Vβ come 5 a 4. E la distanza della cometa dalla retta αβ era 1/2 Vβ.

**[III.G7.25]** Mercoledì 9 marzo, alle ore 8½ p. m., quando la cometa era in X, la retta γX era uguale a 1/4 γδ, e la perpendicolare abbassata dalla stella δ sulla retta γX era 2/5 γδ.

**[III.G7.26]** La stessa notte, alle ore 12, quando la cometa era in Y, la retta γY era uguale a 1/3 γδ, o un poco minore, diciamo 5/16 γδ, e la perpendicolare abbassata dalla stella δ sulla retta γY era uguale a circa 1/6 γδ o 1/7 γδ. Ma per la vicinanza dell’orizzonte la cometa si poteva appena scorgere, e il suo luogo non si poteva definire con la stessa chiarezza che nelle osservazioni precedenti.

**[III.G7.27]** Da osservazioni di questo genere ricavavo, con costruzioni di figure e con calcoli, le longitudini e le latitudini della cometa; e il nostro Pound, a partire dai luoghi corretti delle fisse, ha corretto i luoghi della cometa: i luoghi corretti si trovano sopra. Ho usato un micrometro costruito con poca accuratezza; tuttavia gli errori delle longitudini e delle latitudini (in quanto nascono dalle nostre osservazioni) superano appena un primo. La cometa poi (secondo le nostre osservazioni), alla fine del suo moto, cominciò a deviare sensibilmente verso nord dal parallelo che aveva tenuto alla fine del mese di febbraio.

**[III.G7.28]** Ora, per determinare l’orbita della cometa, fra le osservazioni descritte fin qui ne ho scelte tre, quelle che Flamsteed fece il 21 dicembre, il 5 gennaio e il 25 gennaio. Da queste ho trovato St di 9842,1 parti e Vt di 455, di quelle parti di cui il semidiametro dell’orbe magno ne contiene 10000. Poi, per la prima operazione, assumendo tB di 5657 parti, ho trovato SB 9747, BE la prima volta 412, Sμ 9503, iλ 413; BE la seconda volta 421, OD 10186, X 8528,4, MP 8450, MN 8475, NP 25. Di qui, per la seconda operazione, ho ricavato la distanza tb di 5640. E con questa operazione ho trovato infine le distanze TX di 4775 e τZ di 11322. Definendo l’orbita a partire da queste, ho trovato il suo nodo discendente in ♋ e l’ascendente in ♑ 1° 53′; l’inclinazione del suo piano sul piano dell’eclittica 61° 20⅓′; che il suo vertice (ossia il perielio della cometa) dista dal nodo 8° 38′ ed è in ♐ 27° 43′ con latitudine australe 7° 34′; che il suo lato retto è 236,8 e che l’area descritta ogni giorno dal raggio condotto al Sole è 93585, posto il quadrato del semidiametro dell’orbe magno uguale a 100000000; e che la cometa in questa orbita ha proceduto secondo l’ordine dei segni e l’8 dicembre, a 0h 4′ p. m., è stata nel vertice dell’orbita, ossia nel perielio. Tutto ciò l’ho determinato graficamente, con una scala di parti uguali e con le corde degli angoli ricavate dalla tavola dei seni naturali, costruendo una figura abbastanza ampia, nella quale cioè il semidiametro dell’orbe magno (di 1000 parti) era uguale a 16⅓ pollici del piede inglese.

**[III.G7.29]** Infine, perché risultasse se la cometa si muovesse davvero nell’orbita così trovata, ho ricavato, con operazioni in parte aritmetiche e in parte grafiche, i luoghi della cometa in questa orbita per i tempi di alcune osservazioni, come si può vedere nella tabella seguente.

**[III.G7.30]** *Tabella 4 (orbita grafica di Newton).*

| Data | Distanza della cometa dal Sole | Longitudine ricavata<br>°.′ | Latitudine ricavata<br>°.′ | Longitudine osservata<br>°.′ | Latitudine osservata<br>°.′ | Differenza in longitudine<br>′ | Differenza in latitudine<br>′ |
|---|--:|--:|--:|--:|--:|--:|--:|
| dic. 12 | 2792 | ♑ 6.32 | 8.18½ | ♑ 6.31⅓ | 8.26 | +1 | −7½ |
| 29 | 8403 | ♓ 13.13⅔ | 28.0 | ♓ 13.11¾ | 28.10 1/12 | +2 | −10 1/12 |
| feb. 5 | 16669 | ♉ 17.0 | 15.29⅔ | ♉ 16.59⅞ | 15.27⅖ | +0 | +2¼ |
| mar. 5 | 21737 | 29.19¾ | 12.4 | 29.20 6/7 | 12.3½ | −1 | +½ |

*Note alla Tabella 4 (del curatore).* Distanze in parti di cui il semidiametro dell’orbe magno ne contiene 10000; longitudini e latitudini in gradi e primi, con le frazioni di primo della stampa; differenze in primi. L’ultima differenza in latitudine è scritta «+ 12» nella trascrizione: frazione appiattita, letta «+½» con Motte. Le differenze sono «ricavato − osservato» e tornano tutte (nota N2).

**[III.G7.31]** In seguito il nostro Halley ha determinato l’orbita con un calcolo aritmetico, con maggiore precisione di quanto fosse possibile tracciando linee; e ha conservato il luogo dei nodi in ♋ e ♑ 1° 53′, l’inclinazione del piano dell’orbita sull’eclittica di 61° 20⅓′ e il tempo del perielio della cometa, 8 dicembre, 0h 4′; ha trovato invece che la distanza del perielio dal nodo ascendente, misurata nell’orbita della cometa, è di 9° 20′, e che il lato retto della parabola è di 2430 parti, essendo la distanza media del Sole dalla Terra di 100000 parti. E da questi dati, impostato con cura un calcolo anch’esso aritmetico, ha calcolato i luoghi della cometa per i tempi delle osservazioni, come segue.

**[III.G7.32]** *Tabella 5 (orbita parabolica di Halley).*

| Tempo vero<br>d. h.′ | Distanza della cometa dal Sole | Longitudine calcolata<br>°.′.″ | Latitudine calcolata<br>°.′.″ | Errori in longitudine<br>′.″ | Errori in latitudine<br>′.″ |
|---|--:|--:|--:|--:|--:|
| dic. 12, 4.46 | 28028 | ♑ 6.29.25 | 8.26.0 bor. | −3.5 | −2.0 |
| 21, 6.37 | 61076 | ♒ 5.6.30 | 21.43.20 | −1.42 | +1.7 |
| 24, 6.18 | 70008 | 18.48.20 | 25.22.40 | −1.3 | −0.25 |
| 26, 5.21 | 75576 | 28.22.45 | 27.1.36 | −1.28 | +0.44 |
| 29, 8.3 | 14021 (a) | ♓ 13.12.40 | 28.10.10 | +1.59 | +0.12 |
| 30, 8.10 | 86661 | 17.40.5 | 28.11.20 | +1.45 | +0.33 (b) |
| gen. 5, 6.1½ | 101440 | ♈ 8.49.49 | 26.15.15 | +0.56 | +0.8 |
| 9, 7.0 | 110959 | 18.44.36 | 24.12.54 | +0.32 | +0.58 |
| 10, 6.6 | 113162 | 20.41.0 | 23.44.10 | +0.10 | +0.18 |
| 13, 7.9 | 120000 | 26.0.21 | 22.17.30 | +0.33 | +0.2 |
| 25, 7.59 | 145370 | ♉ 9.33.40 | 17.57.55 | −1.20 | +1.25 |
| 30, 8.22 | 155303 | 13.17.41 | 16.42.7 | −2.10 | −0.11 |
| feb. 2, 6.35 | 160951 | 15.11.11 | 16.4.15 | −2.42 | +0.14 |
| 5, 7.4½ | 166686 | 16.58.25 | 15.29.13 | −0.41 | +2.10 |
| 25, 8.41 | 202570 | 26.15.46 | 12.48.0 | −2.49 | +1.14 |
| mar. 5, 11.39 | 216205 | 29.18.35 | 12.5.40 | +0.35 | +2.24 |

*Note alla Tabella 5 (del curatore).* Distanze in parti di cui la distanza media del Sole dalla Terra ne contiene 100000. Gli «errori» sono «calcolato − osservato», con i valori osservati delle Tabelle 1 e 2. (a) La trascrizione ha 14021; il calcolo nell’orbita di Halley dà 84020, e Motte ha 84021. (b) Calcolato − osservato dà −0′33″ (28.11.20 − 28.11.53); Motte ha −0.33. Non corretti (nota N2).

**[III.G7.33]** Questa cometa apparve anche nel novembre precedente e fu osservata a Coburgo, in Sassonia, dal signor Gottfried Kirch nei giorni quattro, sei e undici di quel mese, secondo il calendario giuliano (stile vecchio). E dalle sue posizioni rispetto alle stelle fisse più vicine, osservate con sufficiente precisione per mezzo di un telescopio ora di due piedi, ora di dieci piedi, dalla differenza di longitudine fra Coburgo e Londra, di undici gradi, e dai luoghi delle fisse osservati dal nostro Pound, il nostro Halley ha determinato i luoghi della cometa come segue.

**[III.G7.34]** Il 3 novembre, a 17h 2′, tempo apparente di Londra, la cometa era in ♎ [leggi ♌] 29° 51′ con latitudine boreale 1° 17′ 45″.

**[III.G7.35]** Il 5 novembre, a 15h 58′, la cometa era in ♍ 3° 23′ con latitudine boreale 1° 6′.

**[III.G7.36]** Il 10 novembre, a 16h 31′, la cometa era equidistante dalle stelle σ e τ del Leone (lettere di Bayer); non aveva ancora toccato la retta che le congiunge, ma ne era poco distante. Nel catalogo stellare di Flamsteed σ aveva allora ♍ 14° 15′ con latitudine boreale di circa 1° 41′, e τ ♍ 17° 3½′ con latitudine australe 0° 34′. E il punto di mezzo fra queste stelle era in ♍ 15° 39¼′, con latitudine boreale 0° 33½′. Sia la distanza della cometa da quella retta di circa 10′ o 12′: la differenza di longitudine fra la cometa e quel punto di mezzo sarà 7′, e la differenza di latitudine circa 7½′. Di qui la cometa era in ♍ 15° 32′ con latitudine boreale di circa 26′.

**[III.G7.37]** La prima osservazione, fatta in base alla posizione della cometa rispetto ad alcune piccole fisse, fu più che sufficientemente precisa. Anche la seconda fu abbastanza precisa. Nella terza, che fu meno precisa, poté esserci un errore di sei o sette primi, e difficilmente maggiore. La longitudine della cometa nella prima osservazione, che fu più precisa delle altre, calcolata nella predetta orbita parabolica, era ♌ 29° 30′ 22″, la latitudine boreale 1° 25′ 7″ e la sua distanza dal Sole 115546.

**[III.G7.38]** Inoltre Halley, osservando che una cometa insigne era apparsa quattro volte a intervalli di 575 anni, cioè nel mese di settembre dopo l’uccisione di Giulio Cesare, nell’anno di Cristo 531 sotto il consolato di Lampadio e Oreste, nell’anno di Cristo 1106 nel mese di febbraio e verso la fine dell’anno 1680, e ogni volta con una coda lunga e insigne (salvo che alla morte di Cesare la coda era apparsa meno, per la posizione sfavorevole della Terra), ha cercato un’orbita ellittica il cui asse maggiore fosse di 1382957 parti, essendo la distanza media della Terra dal Sole di 10000 parti: un’orbita, cioè, nella quale la cometa potesse compiere la sua rivoluzione in 575 anni. E ponendo il nodo ascendente in ♋ 2° 2′, l’inclinazione del piano dell’orbita sul piano dell’eclittica di 61° 6′ 48″, il perielio della cometa in questo piano in ♐ 22° 44′ 25″, il tempo equato del perielio 7 dicembre, 23h 9′, la distanza del perielio dal nodo ascendente nel piano dell’eclittica di 9° 17′ 35″ e l’asse coniugato di 18481,2, ha calcolato il moto della cometa in questa orbita ellittica. I luoghi della cometa, sia dedotti dalle osservazioni sia calcolati in questa orbita, sono presentati nella tabella seguente.

**[III.G7.39]** *Tabella 6 (orbita ellittica di Halley).*

| Tempo vero<br>d. h.′ | Longitudine osservata<br>°.′.″ | Latitudine boreale osservata<br>°.′.″ | Longitudine calcolata<br>°.′.″ | Latitudine calcolata<br>°.′.″ | Errori in longitudine<br>′.″ | Errori in latitudine<br>′.″ |
|---|--:|--:|--:|--:|--:|--:|
| nov. 3, 16.47 | ♌ 29.51.0 | 1.17.45 | ♌ 29.51.22 | 1.17.32 bor. | +0.22 | −0.13 |
| 5, 15.37 | ♍ 3.23.0 | 1.6.0 | ♍ 3.24.32 | 1.6.9 bor. | +1.32 | +0.9 |
| 10, 16.18 | 15.32.0 | 0.27.0 | 15.33.2 | 0.25.7 bor. | +1.2 | −1.53 |
| 16, 17.0 |  |  | ♎ 8.16.45 | 0.53.7 austr. |  |  |
| 18, 21.34 |  |  | 18.52.15 | 1.26.54 |  |  |
| 20, 17.0 |  |  | 28.10.36 | 1.53.35 |  |  |
| 23, 17.5 |  |  | ♏ 13.22.42 | 2.29.0 |  |  |
| dic. 12, 4.46 | ♑ 6.32.30 | 8.28.0 | ♑ 6.31.20 | 8.29.6 bor. | −1.10 | +1.6 |
| 21, 6.37 | ♒ 5.8.12 | 21.42.13 | ♒ 5.6.14 | 21.44.42 | −1.58 | +2.29 |
| 24, 6.18 | 18.49.23 | 25.23.5 | 18.47.30 | 25.23.35 | −1.53 | +0.30 |
| 26, 5.21 | 28.24.13 | 27.0.52 | 28.21.42 | 27.2.1 | −2.31 | +1.9 |
| 29, 8.3 | ♓ 13.10.41 | 28.9.58 | ♓ 13.11.14 | 28.10.38 | +0.33 | +0.40 |
| 30, 8.10 | 17.38.20 | 28.11.53 | 17.38.27 | 28.11.37 | +0.7 | −0.16 |
| gen. 5, 6.1½ | ♈ 8.48.53 | 26.15.7 | ♈ 8.48.51 | 26.14.57 | −0.2 | −0.10 |
| 9, 7.1 | 18.44.4 | 24.11.56 | 18.43.51 | 24.12.17 | −0.13 | +0.21 |
| 10, 6.6 | 20.40.50 | 23.43.32 (a) | 20.40.23 | 23.43.25 | −0.27 | −0.7 |
| 13, 7.9 | 25.59.48 | 22.17.28 | 26.0.8 | 22.16.32 | +0.20 | −0.56 |
| 25, 7.59 | ♉ 9.35.0 | 17.56.30 | ♉ 9.34.11 | 17.56.6 | −0.49 | −0.24 |
| 30, 8.22 | 13.19.51 | 16.42.18 | 13.18.28 | 16.40.5 | −1.23 | −2.13 |
| feb. 2, 6.35 | 15.13.53 | 16.4.1 | 15.11.59 | 16.2.7 | −1.54 | −1.54 |
| 5, 7.4½ | 16.59.6 | 15.27.3 | 16.59.17 | 15.27.0 | +0.11 | −0.3 |
| 25, 8.41 | 26.18.35 | 12.46.46 | 26.16.59 | 12.45.22 | −1.36 | −1.24 |
| mar. 1, 11.10 | 27.52.42 | 12.23.40 | 27.51.47 | 12.22.28 | −0.55 | −1.12 |
| 5, 11.39 | 29.18.0 | 12.3.16 | 29.20.11 | 12.2.50 | +2.11 | +0.26 (b) |
| 9, 8.38 | 0.43.4 | 11.45.52 | ♊ 0.42.43 | 11.45.35 | −0.21 | −0.17 |

*Note alla Tabella 6 (del curatore).* Per i giorni 16–23 novembre la stampa dà solo i luoghi calcolati (le osservazioni sono discusse nei capoversi III.G7.41–49). Il 9 marzo la longitudine osservata è scritta senza il segno ♊. (a) La Tabella 1 ha 23.43.52; l’errore −0.7 della tabella è coerente con 23.43.32. (b) Calcolato − osservato dà −0′26″ (12.2.50 − 12.3.16); anche Motte ha +0.26. Non corretti (nota N2).

**[III.G7.40]** Le osservazioni di questa cometa, dal principio alla fine, concordano con il moto della cometa nell’orbita ora descritta non meno di quanto i moti dei pianeti sogliano concordare con le loro teorie; e, concordando, provano che fu una sola e medesima cometa quella che apparve per tutto questo tempo, e che la sua orbita è stata qui definita correttamente.

**[III.G7.41]** Nella tabella precedente abbiamo omesso, perché meno precise, le osservazioni dei giorni 16, 18, 20 e 23 novembre. Infatti la cometa fu osservata anche in quei tempi. Ponthæus e i suoi compagni, il 17 novembre secondo il calendario giuliano (stile vecchio), alla sesta ora del mattino a Roma, cioè alle 5h 10′ di Londra, con fili applicati alle fisse, osservarono la cometa in ♎ 8° 30′ con latitudine australe 0° 40′. Le loro osservazioni si trovano nel trattato che Ponthæus pubblicò su questa cometa. Cellius, che era presente e mandò le sue osservazioni in una lettera al signor Cassini, vide la cometa alla stessa ora in ♎ 8° 30′ con latitudine australe 0° 30′. Alla stessa ora Galletius, ad Avignone (cioè alle 5h 42′ del mattino di Londra), vide la cometa in ♎ 8° senza latitudine. Secondo la teoria, invece, la cometa era allora in ♎ 8° 16′ 45″ con latitudine australe 0° 53′ 7″.

**[III.G7.42]** Il 18 novembre, alle 6h 30′ del mattino a Roma (cioè alle 5h 40′ di Londra), Ponthæus vide la cometa in ♎ 13° 30′ con latitudine australe 1° 20′; Cellius in ♎ 13° 30′ con latitudine australe 1° 00′. Galletius, invece, alle 5h 30′ del mattino ad Avignone vide la cometa in ♎ 13° 00′ con latitudine australe 1° 00′. E il reverendo padre Ango, nel collegio di La Flèche, in Francia, alla quinta ora del mattino (cioè alle 5h 9′ di Londra), vide la cometa a metà fra due piccole stelle, delle quali una è la mediana delle tre che stanno in linea retta nella mano australe della Vergine, ψ di Bayer, e l’altra è l’estrema dell’ala, θ di Bayer. Di qui la cometa era allora in ♎ 12° 46′ con latitudine australe 50′. Lo stesso giorno a Boston, nel New England, alla latitudine di 42½ gradi, alla quinta ora del mattino (cioè alle 9h 44′ del mattino di Londra), la cometa fu vista vicino a ♎ 14° con latitudine australe 1° 30′, come ho saputo dall’illustre Halley.

**[III.G7.43]** Il 19 novembre, alle 4½ del mattino a Cambridge, la cometa (secondo l’osservazione di un giovane) distava dalla Spiga della Vergine circa 2° verso nord-ovest. La Spiga era allora in ♎ 19° 23′ 47″ con latitudine australe 2° 1′ 59″. Lo stesso giorno, alle 5 del mattino, a Boston nel New England, la cometa distava dalla Spiga della Vergine un grado, con una differenza di latitudine di 40′. Lo stesso giorno, nell’isola di Giamaica, la cometa distava dalla Spiga circa un grado. Lo stesso giorno il signor Arthur Storer, presso il fiume Patuxent vicino a Hunting Creek, nel Maryland, ai confini della Virginia, alla latitudine di 38½°, alla quinta ora del mattino (cioè alle 10 di Londra), vide la cometa sopra la Spiga della Vergine e quasi congiunta con essa, essendo la distanza fra loro di circa 3/4 di grado. E confrontando fra loro queste osservazioni ricavo che alle 9h 44′ di Londra la cometa era in ♎ 18° 50′ con latitudine australe di circa 1° 25′. Secondo la teoria, invece, la cometa era allora in ♎ 18° 52′ 15″ con latitudine australe 1° 26′ 54″.

**[III.G7.44]** Il 20 novembre il signor Montanari, professore di astronomia a Padova, alla sesta ora del mattino a Venezia (cioè alle 5h 10′ di Londra) vide la cometa in ♎ 23° con latitudine australe 1° 30′. Lo stesso giorno a Boston la cometa distava dalla Spiga della Vergine 4° di longitudine verso oriente, e quindi era in ♎ 23° 24′ circa.

**[III.G7.45]** Il 21 novembre Ponthæus e i suoi compagni, alle 7¼ del mattino, osservarono la cometa in ♎ 27° 50′ con latitudine australe 1° 16′; Cellius in ♎ 28°; Ango, alla quinta ora del mattino, in ♎ 27° 45′; Montanari in ♎ 27° 51′. Lo stesso giorno nell’isola di Giamaica la cometa fu vista vicino al principio dello Scorpione, e aveva circa la stessa latitudine della Spiga della Vergine, cioè 2° 2′. Lo stesso giorno, alla quinta ora del mattino, a Balasore nelle Indie orientali (cioè alle 11h 20′ della notte precedente a Londra), fu presa la distanza della cometa dalla Spiga della Vergine: 7° 35′ verso oriente. La cometa era in linea retta fra la Spiga e il piatto della Bilancia, e quindi si trovava in ♎ 26° 58′ con latitudine australe di circa 1° 11′; e dopo 5 ore e 40′ (cioè alla quinta ora del mattino di Londra) era in ♎ 28° 12′ con latitudine australe 1° 16′. Secondo la teoria, invece, la cometa era allora in ♎ 28° 10′ 36″ con latitudine australe 1° 53′ 35″.

**[III.G7.46]** Il 22 novembre la cometa fu vista da Montanari in ♏ 2° 33′. A Boston, nel New England, apparve invece in ♏ 3° circa, con quasi la stessa latitudine di prima, cioè 1° 30′. Lo stesso giorno, alla quinta ora del mattino, a Balasore la cometa fu osservata in ♏ 1° 50′; e quindi alla quinta ora del mattino di Londra la cometa era in ♏ 3° 5′ circa. Lo stesso giorno, a Londra, alle 6½ del mattino, il nostro Hooke vide la cometa in ♏ 3° 30′ circa, e precisamente sulla linea retta che passa per la Spiga della Vergine e il Cuore del Leone: non esattamente, però, ma deviando un poco da quella linea verso nord. Montanari notò parimenti che la linea condotta dalla cometa per la Spiga, in questo giorno e nei seguenti, passava per il lato australe del Cuore del Leone, con un intervallo piccolissimo fra il Cuore del Leone e questa linea. La linea retta che passa per il Cuore del Leone e la Spiga della Vergine tagliava l’eclittica in ♍ 3° 46′, sotto un angolo di 2° 51′. E se la cometa fosse stata collocata su questa linea in 3° [dello Scorpione], la sua latitudine sarebbe stata 2° 26′. Ma poiché la cometa, come concordano Hooke e Montanari, distava un poco da questa linea verso nord, la sua latitudine fu un poco minore. Il giorno 20, secondo l’osservazione di Montanari, la sua latitudine eguagliava quasi quella della Spiga della Vergine ed era circa 1° 30′; e, come concordano Hooke, Montanari e Ango, cresceva continuamente: quindi ora era sensibilmente maggiore di 1° 30′. Fra i limiti ora stabiliti, 2° 26′ e 1° 30′, la latitudine, presa con un valore medio, sarà circa 1° 58′. La coda della cometa, come concordano Hooke e Montanari, era diretta verso la Spiga della Vergine, declinando un poco da quella stella, secondo Hooke verso sud, secondo Montanari verso nord; quindi quella declinazione fu appena sensibile, e la coda, essendo quasi parallela all’equatore, deviava un poco dall’opposizione del Sole verso nord.

**[III.G7.47]** Il 23 novembre, secondo il calendario giuliano (stile vecchio), alla quinta ora del mattino a Norimberga (cioè alle 4½ di Londra), il signor Zimmerman vide la cometa in ♏ 8° 8′ con latitudine australe 2° 31′, prendendone cioè le distanze dalle stelle fisse.

**[III.G7.48]** Il 24 novembre, prima del sorgere del Sole, la cometa fu vista da Montanari in ♏ 12° 52′, dal lato boreale della retta che si conduceva per il Cuore del Leone e la Spiga della Vergine, e quindi ebbe una latitudine un poco minore di 2° 38′. Questa latitudine, come abbiamo detto, secondo le osservazioni di Montanari, Ango e Hooke, cresceva continuamente; quindi ora era un poco maggiore di 1° 58′, e, prendendo un valore medio, si può stabilire senza errore notevole in 2° 18′. Ponthæus e Galletius vogliono che la latitudine fosse ormai diminuita, e Cellius e l’osservatore nel New England che avesse conservato quasi la stessa grandezza, cioè di un grado o di un grado e mezzo. Più grossolane sono le osservazioni di Ponthæus e di Cellius, soprattutto quelle prese per azimut e altezze, come pure quelle di Galletius; migliori sono quelle fatte per mezzo delle posizioni della cometa rispetto alle fisse da Montanari, Hooke, Ango e dall’osservatore nel New England, e talvolta da Ponthæus e Cellius. Lo stesso giorno, alla quinta ora del mattino, a Balasore la cometa fu osservata in ♏ 11° 45′; e quindi alla quinta ora del mattino di Londra era in ♏ 13° circa. Secondo la teoria, invece, la cometa era allora in ♏ 13° 22′ 42″.

**[III.G7.49]** Il 25 novembre, prima del sorgere del Sole, Montanari osservò la cometa in ♏ 17¾° circa. E Cellius osservò nello stesso tempo che la cometa era sulla linea retta fra la stella lucida nella coscia destra della Vergine e il piatto australe della Bilancia; e questa retta taglia il cammino della cometa in ♏ 18° 36′. Secondo la teoria, invece, la cometa era allora in ♏ 18⅓° circa.

**[III.G7.50]** Queste osservazioni, dunque, concordano con la teoria nella misura in cui concordano fra loro, e concordando provano che fu una sola e medesima cometa quella che apparve per tutto il tempo dal quattro novembre fino al nove marzo. La traiettoria di questa cometa tagliò due volte il piano dell’eclittica, e perciò non fu rettilinea. Tagliò l’eclittica non in parti opposte del cielo, ma alla fine della Vergine e al principio del Capricorno, a un intervallo di circa 98 gradi; quindi il corso della cometa deviava moltissimo da un cerchio massimo. Infatti nel mese di novembre il suo corso declinava dall’eclittica verso sud di almeno tre gradi, e poi nel mese di dicembre piegava dall’eclittica verso nord di 29 gradi, e le due parti dell’orbita in cui la cometa tendeva verso il Sole e tornava dal Sole declinavano l’una dall’altra di un angolo apparente di più di trenta gradi, come osservò Montanari. Questa cometa procedeva per nove segni, cioè dall’ultimo grado del Leone al principio dei Gemelli, oltre al segno del Leone, per il quale procedeva prima che si cominciasse a vederla; e non esiste alcun’altra teoria per cui una cometa percorra con moto regolare una parte così grande del cielo. Il suo moto fu estremamente disuguale. Infatti verso il ventesimo giorno di novembre descrisse circa cinque gradi al giorno; poi, rallentato il moto, fra il 26 novembre e il 12 dicembre, cioè nello spazio di quindici giorni e mezzo, descrisse soltanto 40 gradi; in seguito, accelerato di nuovo il moto, descrisse quasi cinque gradi al giorno, prima che il moto cominciasse di nuovo a rallentare. E la teoria che corrisponde bene a un moto così disuguale per una parte grandissima del cielo, che osserva le stesse leggi della teoria dei pianeti e che concorda con precisione con osservazioni astronomiche precise, non può non essere vera.

**Fine della parte «a» del Fascicolo 26. Nel testo originale segue il paragrafo *Cæterum trajectoriam quam cometa descripsit…* (Fascicolo 26b).**
---

## Apparato

### A.0 Estensioni del glossario

I termini seguenti non comparivano nei glossari comune, del Libro II e del Libro III. Ognuno è reso in modo costante in tutto il fascicolo.

| Latino | Italiano | Motivazione |
|---|---|---|
| *linea occulta*, *occulta* (sostantivato) | «linea occulta» | Linea di costruzione tracciata leggermente, da cancellare dopo l’uso (*deletis jam literis*): termine tecnico del disegno geometrico, conservato. Motte «obscure line». Nota N1. |
| *vestigium orbis in plano eclipticæ descriptum* | «traccia dell’orbita descritta nel piano dell’eclittica» | La proiezione dell’orbita sull’eclittica (III.G7.09). |
| *tangens latitudinis … ad radium tB* | «la tangente della latitudine … riferita al raggio tB» | La tangente trigonometrica calcolata su un raggio di lunghezza tB, cioè tB · tan β (nota N3). |
| *operatio* | «operazione» | Ciascuna ripetizione della costruzione con un punto di prova (III.G7.09, III.G7.28). |
| *per scalam partium æqualium & chordas angulorum*; *tabula sinuum naturalium* | «con una scala di parti uguali e con le corde degli angoli»; «tavola dei seni naturali» | Strumenti del calcolo grafico; Motte «by scale and compass». |
| *graphice*; *per descriptiones linearum*; *calculus arithmeticus* | «graficamente»; «tracciando linee»; «calcolo aritmetico» | Contrapposizione fra il metodo di Newton e quello di Halley. |
| *tempus apparens / verum*; *tempus æquatum* | «tempo apparente / vero»; «tempo equato» | Tempo solare apparente e tempo medio. *Æquatum* rende il glossario *æquatio* «equazione» (correzione astronomica): qui l’equazione del tempo. Nota N1. |
| *secundum seriem signorum* | «secondo l’ordine dei segni» | Moto diretto, nel verso crescente delle longitudini. Nota N1. |
| *vertex* (*orbis*) | «vertice» | Il vertice della parabola, cioè il perielio, come dice il testo (*seu perihelium*). |
| *axis major / conjugatus* | «asse maggiore / coniugato» | Dell’ellisse di Halley. |
| *Differ. Long. / Lat.*; *Errores in Long. / Lat.* | «differenza in longitudine / latitudine»; «errori in longitudine / latitudine» | Intestazioni delle Tabelle 4–6; il segno è «calcolato − osservato» (nota N2). |
| *Long. collect.* | «longitudine ricavata» | *Colligere* «ricavare» (dall’orbita costruita), come *collegi* in III.G7.29. |
| *stella sequens* | «stella seguente» | La stella che segue nel moto diurno, cioè più a oriente (non verificato sulle fonti allegate). |
| *magnitudo* (di una stella) | «grandezza» | *Quartæ, tertiæ, sextæ, octavæ magnitudinis*. |
| *calcaneus*, *talus*, *pes* (di Perseo) | «calcagno», «tallone», «piede» | Parti della figura della costellazione. |
| *proxime* | «con buona approssimazione» | Distinto da *quamproxime* «con ottima approssimazione» (glossario), come nel latino (III.G7.18). |
| *spica Virginis*, *spica ♍* | «la Spiga della Vergine» | Glossario del Libro III; il latino scrive spesso *spica ♍*. |
| *cor Leonis* | «il Cuore del Leone» | Nome proprio di stella, reso come *spica Virginis*. |
| *lanx* (*australis*) *Libræ* | «il piatto (australe) della Bilancia» | Stella della Bilancia (III.G7.45, III.G7.49); Motte «the balance», «the southern scale of Libra». Non identifico la stella. |
| *stella lucida in dextro femore Virginis* | «la stella lucida nella coscia destra della Vergine» | Descrizione per posizione nella figura. |
| *boreazephyrum versus* | «verso nord-ovest» | *Boreazephyrus*, il vento di nord-ovest; Motte «towards the north west». |
| *in austrum*, *in boream*, *boream versus*, *in septentrionem* | «verso sud», «verso nord» | Direzioni sulla sfera celeste. |
| *azimuthi & altitudines* | «azimut e altezze» | Coordinate orizzontali. |
| *magnitudine mediocri* | «con un valore medio» | Media aritmetica fra due limiti (III.G7.46, III.G7.48). |
| *Dnus.*, *D.* (*Dominus*); *R. P.* (*Reverendus Pater*); *cl.* (*clarissimus*); *noster* | «il signor»; «il reverendo padre»; «l’illustre»; «il nostro» | Titoli premessi ai nomi. |
| *academia Flexiensis apud Gallos* | «il collegio di La Flèche, in Francia» | *Academia* qui è il collegio dei gesuiti di La Flèche (non verificato sulle fonti allegate); Motte «the University of La Fleche». |
| *Coss.* | «sotto il consolato di» | Datazione romana. |
| *digitus pedis Anglicani* | «pollice del piede inglese» | *Digitus* come misura di lunghezza: «pollice» (glossario del Libro II); non è il «dito» delle eclissi. |
| *telescopium septupedale / bipedale / decempedale* | «telescopio di sette / due / dieci piedi» | Lunghezza focale in piedi. |
| *hora matutina*; *p. m.* | «del mattino»; «p. m.» | Si conserva l’abbreviazione *p. m.* (*post meridiem*) del testo. |
| *cursus*, *via* (*cometæ*) | «corso», «cammino» | Il cammino apparente sulla sfera (III.G7.49–50). |
| *inæquabilis* | «disuguale» | Moto non uniforme. |
| *trajectoria* (III.G7.50) | «traiettoria» | Glossario; qui indica il cammino apparente sulla sfera celeste, non l’orbita nello spazio (nota N7). |

**Dubbi da sottoporre al curatore.** (1) *occulta* «linea occulta»: alternativa «linea nascosta» o «linea tratteggiata»; ho preferito il termine tecnico. (2) Il glossario del Libro III fissa *digitus* «dito» per le eclissi; qui *digitus* è una lunghezza e ho seguito il Libro II («pollice»). (3) *Spica ♍*: reso sempre «la Spiga della Vergine», perdendo il simbolo del latino.

### A.1 Proposizione XLI: enunciato e costruzione (III.G7.01–III.G7.07)

**Latino:** *Cometæ in parabola moti trajectoriam ex datis tribus observationibus determinare.*

**Inglese:** “From three observations given to determine the orbit of a comet moving in a parabola.”

**Scelte.**

- Enunciato all’infinito (problema): «Determinare la traiettoria…», come gli enunciati dei problemi del Libro I. Motte «orbit» per *trajectoriam*: il glossario vuole «traiettoria».
- III.G7.02: *Problema hocce longe difficillimum multimode aggressus* → «Avendo affrontato in molti modi questo problema, di gran lunga il più difficile». *Composui problemata quædam in libro primo* → «ho composto nel Libro primo alcuni problemi»: Newton non dice quali (§ A.8).
- III.G7.03: *ut temporum differentia sit ad summam temporum, ut summa temporum ad dies plus minus sexcentos* → «che la differenza dei tempi stia alla somma dei tempi come la somma dei tempi sta a seicento giorni circa». *In fig. lem. viii.* → «nella figura del Lemma VIII».
- III.G7.04: *longitudo* ha due sensi nello stesso periodo: *observatas tres longitudines* sono le rette della longitudine osservata (TA, tB, τC), *X longitudinem* è una lunghezza. Resi «longitudini» e «lunghezza». *Perpendiculum* (tV) è poi chiamato *sagitta*: «perpendicolare» e «saetta» (nota N1 sulla saetta).
- *contentum sub SB & St quad.* → «il contenuto sotto SB e St²», come nel Fascicolo 5; è il prodotto SB · St².
- *Per hujus lem. vii.* → «per il Lemma VII di questo Libro»; *per corol. 3. prop. xl. lib. iii.* → «per il Cor. 3 della Prop. XL del Libro III», come nel latino.
- III.G7.05: *Cape Iσ æqualem 3⁢Iλ* è letto «3Iλ» (Motte, SVG 1172); *σξ æqualem 3⁢Sσ+3⁢Iλ* «3Sσ + 3Iλ» (Motte: 3Sσ + 3*i*λ, § A.9); *Sμ+13⁢iλ* «Sμ + iλ/3» (Motte SVG 1175). *In duplicata ratione distantiæ BS ad quantitatem…* → «in rapporto duplicato della distanza BS rispetto alla quantità…».
- III.G7.06: *Sμ+23⁢iλ* «Sμ + 2iλ/3» (SVG 1177). *Rectangulum iIλμ*: lo stesso parallelogramma di III.G7.05, che è un rettangolo perché Ii ⊥ AC.
- III.G7.07: la trascrizione ha *& ε, α κ, γ* con una virgola mancante fra α e κ: i nuovi punti sono ε, α, κ, γ (analoghi di E, A, C, G), e la corda è ακ. *Q.E.I.* → «C.V.T.».

### A.2 Dimostrazione e scelta dei punti di prova (III.G7.08–III.G7.09)

- III.G7.08: un solo periodo latino; l’italiano conserva la struttura *quippe cum … & … & …* con «infatti … ; … ; e …». *Interjecta* → «compresa … fra».
- III.G7.09: *non quælibet, sed vero proxima* → «non a caso, ma vicinissimi al vero». *Præterpropter innotescat* → «è noto approssimativamente». *43⁢Tτ* letto «4Tτ/3» (Motte SVG 1188). *Ut plurimum suffecerint* → «per lo più basteranno».
- *Vt* (III.G7.09) è la stessa saetta tV di III.G7.04.

### A.3 Esempio: Flamsteed, Newton, Pound (III.G7.10–III.G7.32)

- III.G7.10: *a Flamstedio observatum & ex observationibus computatum, atque ab Halleio … correctum* → «osservato da Flamsteed e calcolato in base alle osservazioni, e corretto da Halley». Motte attribuisce il calcolo esplicitamente a Flamsteed («calculated afterwards by him»): lettura possibile del latino, non necessaria.
- Tabella 1: il titolo di colonna *Cometæ* abbraccia *Longitudo* e *Lat. bor.*; reso con due intestazioni esplicite. Il tempo apparente del 21 dicembre, *6. 32½*, ha la frazione di minuto della stampa (Motte SVG 1190).
- III.G7.14: *Bayero ο / ζ / n* → «ο / ζ / n di Bayer»: la trascrizione ha la lettera latina «n» per C, Motte η (SVG 1192); probabile η letta come n (§ A.7). L’elenco dei luoghi della cometa (*p, P, Q, R, S, T, V, X*) non comprende Y, che compare in III.G7.26. Le lettere S e T indicano qui luoghi della cometa, non il Sole e la Terra della costruzione.
- III.G7.18–26: i giorni della settimana del latino (*die veneris, solis, martis, mercurii, saturni, lunæ*) tornano con le date giuliane (controllo con il numero del giorno giuliano: 25 febbraio 1681 venerdì, 27 domenica, 1° marzo martedì, 2 mercoledì, 5 sabato, 7 lunedì, 9 mercoledì).
- III.G7.19: la trascrizione ha *14⁤12⁢AE*, *15⁤14⁢AE*, *14⁤78⁢AE*: frazioni a due piani appiattite. Motte (SVG 1222–1224) le legge 1/(4½), 1/(5¼), 1/(4⅞); il conto torna: 1/(4⅞) = 8/39. Tradotto così.
- III.G7.21: 1/3 CK + 1/16 CR = CR dà CR = 16/45 CK: il conto torna.
- III.G7.27: *minutum unum primum vix superant* → «superano appena un primo».
- III.G7.28: *X 8528,4 MP 8450* senza virgola fra i due valori; *semediametri* per *semidiametri*; *partium 1000* contro le 10000 parti del resto del capoverso (§ A.7).
- III.G7.29: *per operationes partim arithmeticas partim graphicas* → «con operazioni in parte aritmetiche e in parte grafiche».
- III.G7.31: *per descriptiones linearum* → «tracciando linee»; *existente mediocri solis a terra distantia partium 100000* → «essendo la distanza media del Sole dalla Terra di 100000 parti».

### A.4 Kirch e l’ellisse di Halley (III.G7.33–III.G7.40)

- III.G7.33: *diebus mensis hujus quarto, sexto & undecimo, stylo veteri* → «nei giorni quattro, sei e undici di quel mese, secondo il calendario giuliano (stile vecchio)». I luoghi che seguono sono datati 3, 5 e 10 novembre perché le ore sono contate dal mezzogiorno: 3 novembre, 17h = 4 novembre, 5 del mattino (nota N1).
- III.G7.34: la trascrizione ha **♎** 29° 51′; la Tabella 6, il calcolo di III.G7.37 (♌ 29° 30′ 22″) e Motte hanno ♌. Il testo tradotto conserva ♎ con l’integrazione «[leggi ♌]».
- III.G7.36: *a stellis leonis σ ac τ Bayero* → «dalle stelle σ e τ del Leone (lettere di Bayer)»; Motte «two stars in ♌». *τ vero ♍ 17gr. 3½* e *0gr. 33½*: manca il segno ′, integrato dal contesto (Motte SVG 1254, 1256).
- III.G7.37: *abunde satis accurata* → «più che sufficientemente precisa»; *vix major* → «difficilmente maggiore».
- III.G7.38: *tempus æquatum perihelii* → «il tempo equato del perielio» (A.0). *Lampadio & Oreste Coss.* → «sotto il consolato di Lampadio e Oreste».
- III.G7.40: *non minus congruunt … quam motus planetarum congruere solent* → «concordano … non meno di quanto i moti dei pianeti sogliano concordare».

### A.5 Le osservazioni di novembre e la conclusione (III.G7.41–III.G7.50)

- III.G7.41: *Nam cometa his etiam temporibus observatus fuit* → «Infatti la cometa fu osservata anche in quei tempi»; Motte «for at those times several persons had observed the comet» aggiunge «several persons». *Pon ‹503› thæus*: parola spezzata dal marcatore di pagina.
- III.G7.42: *quarum una media est trium in recta linea in virginis australi manu* → «delle quali una è la mediana delle tre che stanno in linea retta nella mano australe della Vergine».
- III.G7.43: *existente distantia inter eosdem quasi 34gr* letto «circa 3/4 di grado» (Motte SVG 225). *Hora 10a* → «alle 10».
- III.G7.46: *in 3gr* (senza segno) → «in 3° [dello Scorpione]»; Motte «in ♏ 3°». *Inter limites … magnitudine mediocri* → «presa con un valore medio»: (2° 26′ + 1° 30′)/2 = 1° 58′.
- III.G7.48: *Crassiores sunt observationes Ponthæ & Cellii*: *Ponthæ* per *Ponthæi*, refuso probabile. (2° 38′ + 1° 58′)/2 = 2° 18′: torna.
- III.G7.50: *quatenus congruunt inter se* → «nella misura in cui concordano fra loro» (non è il *nisi quatenus* del glossario). L’ablativo assoluto *partibus duabus orbitæ … declinantibus* è reso con una coordinata («e le due parti dell’orbita … declinavano»). *Spatio scilicet dierum quindecim cum semisse* → «cioè nello spazio di quindici giorni e mezzo».

### A.6 Nomi propri

| Latino | Resa | Commento |
|---|---|---|
| *Flamstedius* | Flamsteed | John Flamsteed (non verificato sulle fonti allegate per il nome di battesimo) |
| *Halleius noster* | il nostro Halley | Edmond Halley (idem) |
| *Poundius noster* | il nostro Pound | James Pound (idem) |
| *Dnus. Gottfried Kirch* | il signor Gottfried Kirch | nome già moderno nel latino |
| *D. Cassinus* | il signor Cassini | Gian Domenico Cassini (non verificato sulle fonti allegate) |
| *Hookius noster* | il nostro Hooke | Robert Hooke (idem) |
| *D. Montenarus, astronomiæ professor Paduensis* | il signor Montanari, professore di astronomia a Padova | Geminiano Montanari (non verificato sulle fonti allegate); Motte «Montenari» |
| *R. P. Ango* | il reverendo padre Ango | nome conservato |
| *D. Arthurus Storer* | il signor Arthur Storer | |
| *D. Zimmerman* | il signor Zimmerman | grafia del latino conservata |
| *Ponthæus*, *Cellius*, *Galletius* | Ponthæus, Cellius, Galletius | lasciati nella forma latina: l’identificazione non risulta dalle fonti allegate |
| *Bayerus* | Bayer | le lettere greche delle stelle sono quelle dell’atlante di Bayer |
| *Lampadius & Orestes* | Lampadio e Oreste | consoli dell’anno 531 secondo il testo |

### A.7 Refusi e anomalie della trascrizione; cifre che non tornano

| Luogo | Trascrizione | Lettura | Tipo |
|---|---|---|---|
| tabelle, *passim* | «46⁤01», «′⁤01» | 46, ′ | segnaposto vuoto di allineamento (frazione «0/1»), non una cifra |
| tabelle, *passim* | «32⁤12», «10⁤112», «+ 12» | 32½, 10 1/12, +½ | frazioni appiattite; lette con Motte |
| Tab. 5, *passim* | «1{.}20», «0{.}11» | 1.20, 0.11 | residuo di codice nella trascrizione |
| Tab. 1, 29 dic., Sole | 19.9.43 | 19.19.43 | **cifra che non torna** (moto del Sole; Motte 19.19.43) |
| Tab. 2, righe 2–7 | «08°.15′» ecc. | 8h 15′ | «°» per «h» |
| III.G7.14 | *Bayero n* | η | lettera latina per la greca (Motte η) |
| III.G7.28 | *X 8528,4 MP 8450* | *X 8528,4, MP 8450* | virgola mancante |
| III.G7.28 | *semediametri* | *semidiametri* | refuso probabile |
| III.G7.28 | *(partium 1000)* | *10000*? | **cifra che non torna** con le 10000 parti dello stesso capoverso; Motte «10000» |
| Tab. 5, 29 dic., distanza | 14021 | 84021 | **cifra che non torna** (calcolo: 84020; Motte 84021) |
| Tab. 5, 30 dic., errore lat. | +0.33 | −0.33 | **segno che non torna** (Motte −0.33) |
| Tab. 6, 10 gen., lat. osservata | 23.43.32 | 23.43.52? | **non torna con la Tab. 1**; l’errore della riga è coerente con 32 (anche Motte 32) |
| Tab. 6, 5 mar., errore lat. | +0.26 | −0.26 | **segno che non torna** (anche Motte) |
| III.G7.34 | *♎ 29gr. 51′* | ♌ | segno zodiacale errato (Tab. 6 e Motte ♌) |
| III.G7.36 | *3½,* ; *33½* | 3½′; 33½′ | segno ′ mancante |
| III.G7.38 | *nodum ascendentem in ♋ 2gr. 2′* | ? | **dato incoerente** con il nodo ascendente in ♑ delle orbite paraboliche e con ♐ 22° 44′ 25″ + 9° 17′ 35″ = ♑ 2° 2′ (nota N5); anche Motte |
| III.G7.38 | *distantiam perihelii a nodo ascendente in plano eclipticæ* | *in orbita*? | i numeri tornano se 9° 17′ 35″ è misurato nell’orbita (nota N5); anche Motte |
| III.G7.41 | *hora matutina 5. 42 Londini* | 5h 42′ | segno ′ mancante |
| III.G7.42 | *hora 5, 40′* | 5h 40′ | virgola per punto |
| III.G7.48 | *Ponthæ* | *Ponthæi* | refuso probabile |
| III.G7.07 | *& ε, α κ, γ* | *ε, α, κ, γ* | virgola mancante |

Nessuna delle cifre segnate è corretta nel testo tradotto.

**Punti da controllare sulla stampa ECCO.**

| Pagina 1726 | Trascrizione | Lettura attesa | Motivo |
|---|---|---|---|
| p. 496 | Tab. 1, 29 dic., *Long. Solis 19. 9. 43* | 19. 19. 43 | moto del Sole di 58′ e 71′ al giorno nelle righe vicine |
| p. 496 | Tab. 2, *08°.15′* … *08°.30′* | 8h.15′ … | simbolo dell’ora |
| p. 496 | *Bayero n* | η | Motte η |
| p. 499 | *(partium 1000)* | 10000 | coerenza con il resto del capoverso; Motte |
| p. 499 | *semediametri* | *semidiametri* | grafia |
| p. 500 | Tab. 5, 29 dic., *14021* | 84021 | serie delle distanze; calcolo |
| p. 500 | Tab. 5, 30 dic., *+ 0. 33* | − 0. 33 | segno; Motte |
| p. 501 | *cometa erat in ♎ 29gr. 51′* | ♌ | Tab. 6; Motte |
| p. 501 | *Novem. 5d. 15h. 58′* (apparente) e Tab. 6 *5. 15. 37* (vero) | ? | differenza di 21 minuti, contro 15 e 13 minuti negli altri due giorni (nota N8) |
| p. 502 | *nodum ascendentem in ♋* | ? | nota N5 |
| p. 502 | Tab. 6, 10 gen., *23. 43. 32* | ? | Tab. 1 ha 23. 43. 52 |
| p. 502 | Tab. 6, 5 mar., *+ 0. 26* | − 0. 26 | segno |
| p. 502 | Tab. 6, 18 nov., *21. 34* | 21. 44? | III.G7.43 dà per gli stessi valori teorici «hora 9. 44′ Londini» |
| p. 505 | *Ponthæ* | *Ponthæi* | grafia |
| pp. 505–506 | marcatore ‹506› assente | — | paginazione della trascrizione |

### A.8 Rimandi

**Rimandi al Libro I.**

| Luogo | Latino | Verifica |
|---|---|---|
| III.G7.02 | *composui problemata quædam in libro primo* | Rimando generico, senza numero. I problemi del Libro I sulle sezioni coniche per punti e tangenti date (Sezioni IV–V) sono i candidati naturali (Fascicoli 6–7), ma il testo non li indica: non verificabile come rimando puntuale. |
| III.G7.07 | *per prop. xix. Lib. i.* | **Torna.** Prop. XIX del Libro I (Fascicolo 6, S4.06): «Intorno a un fuoco dato descrivere una traiettoria parabolica che passi per punti dati e tocchi rette date di posizione». Qui: fuoco S, due punti dati. |

**Rimandi interni al Libro III** (verificati sul latino di `latino-1726-L3-P34-40.md`, Fascicolo 25b):

| Luogo | Latino | Verifica |
|---|---|---|
| III.G7.03 | *in fig. lem. viii.* | La figura del Lemma VIII ha i punti E, I, A e M (M compare nello Scolio del Lemma VIII e nel Lemma IX): torna. |
| III.G7.03 | *per lemma sextum* | Lemma VI: trovare il luogo della cometa a un tempo intermedio dato da più osservazioni. Torna. |
| III.G7.04 | *per corol. 3. prop. xl. lib. iii.* | Il Cor. 3 della Prop. XL dà il moto diurno della cometa alla distanza media (2432747 parti con raggio 10⁸). Torna, e il valore X = 8528,4 lo conferma numericamente (nota N3). |
| III.G7.04, 08 | *per hujus lem. vii.*; *per lemma vii* | Lemma VII: per un punto dato condurre una retta le cui parti fra due rette date stiano in un rapporto dato. Torna. |
| III.G7.08 | *ut oportet per lem. viii* | Lemma VIII: la corda AC è divisa in E nel rapporto dei tempi, con ottima approssimazione. Torna. |
| III.G7.08 | *BE per lem. xi.* | Lemma XI: lo spazio di caduta verso il Sole nella metà del tempo è uguale a Iμ; BE è la saetta corrispondente nel piano dell’eclittica. Torna nel senso; la corrispondenza fra *Iμ* dei lemmi e *iλ* della costruzione non è dichiarata da Newton. |
| III.G7.08 | *per corol. lem. x.* | Cor. del Lemma X: con la velocità che ha all’altezza Sμ + 2Iμ/3 la cometa descriverebbe la corda AC nello stesso tempo. È il criterio per MP (con ID = Sμ + 2iλ/3). Torna. |

Rimandi che non tornano: **nessuno**.

### A.9 Riepilogo: dove Motte aggiunge, omette o sbaglia

| Luogo | Latino | Motte 1846 | Tipo |
|---|---|---|---|
| III.G7.03 | *Si tales observationes* | «If such **direct** observations» | aggiunta |
| III.G7.04 | *toto illo tempore* | «in the whole time V + W» | esplicitazione |
| III.G7.05 | *3⁢Sσ+3⁢Iλ* | 3Sσ + 3*i*λ (SVG 1174) | lettera diversa (minuscola) |
| III.G7.07 | *ε, α κ, γ*; *Ggγ*; *κγ*; *per G, g, γ* | ε, α, κ, **λ**; G*g*λ; κλ; «through G, g, and λ» (SVG 1169, 1180, 1183) | **lettera errata** (λ è già il punto su AC) |
| III.G7.09 | *in angulo illo ducenda erit* | «at that angle **with Bt** draw» | aggiunta |
| III.G7.10 | *ex observationibus computatum* | «calculated afterwards **by him**» | esplicitazione |
| III.G7.11 | Tab. 1, 29 dic., Sole 19.9.43 | 19.19.43 | Motte corretto |
| III.G7.14 | *Bayero n* | η (SVG 1192) | Motte corretto, probabilmente |
| III.G7.15 | *Tandem* | «since» | sfumatura |
| III.G7.16 | M 29.18.54, 12.7.20; N 12.31.9 | M 9.18.54, 2.7.20; N 2.31.9 | **cifre errate** in Motte (nota N6) |
| III.G7.19 | *110⁢BF* | 4/5 PE (SVG 1226) | **divergenza** non risolvibile senza la stampa |
| III.G7.20 | *Positionem hujus rectæ* | «the position of the **star**» | **errore di senso** |
| III.G7.24 | *111⁢BF* | 1/10 (SVG 691) | divergenza (1/11 contro 1/10) |
| III.G7.25 | *14⁢γδ* | 1/2 γδ (SVG 1241) | divergenza; il calcolo dalle posizioni di Pound dà 0,29 (nota N6) |
| III.G7.26 | *16⁢γδ vel 17⁢γδ* | 1/6 or 1/3 γδ (SVG 1246, 1247) | divergenza (1/7 contro 1/3) |
| III.G7.28 | *ad operationem primam* | «for the first **observation**» | **errore di senso** |
| III.G7.28 | *MP 8450* | «PM 8450» | ordine delle lettere |
| III.G7.28 | *(partium 1000)* | «consisting of 10000 parts» | Motte coerente con il resto del capoverso |
| III.G7.30 | Tab. 4, 12 dic., long. oss. 6.31⅓; 29 dic., lat. oss. 28.10 1/12 | 6.31½; 28.10½ (SVG 643) | **cifre errate** in Motte: la differenza −10 1/12 richiede 28.10 1/12 |
| III.G7.32 | Tab. 5: 26 dic. 5.21; 29 dic. 14021; 30 dic. +0.33; 5 feb. long. 16.58.25, err. lat. +2.10; 25 feb. +1.14; 5 mar. +2.24 | 5.20; 84021; −0.33; 16.58.55, +2.0; +1.10; +2.14 | Motte corretto per 84021 e −0.33; **errato** per gli altri cinque valori (gli errori latini tornano, quelli di Motte no) |
| III.G7.34 | *♎ 29gr. 51′* | ♌ | Motte corretto |
| III.G7.39 | Tab. 6: 30 dic. long. oss. 17.38.20; 2 feb. lat. calc. 16.2.7; 9 mar. lat. oss. 11.45.52 | 17.38.0; 16.2.17; «♊.45.52» | **cifre errate** in Motte (gli errori latini tornano) |
| III.G7.41 | *Nam cometa his etiam temporibus observatus fuit* | «for at those times **several persons** had observed the comet» | aggiunta |
| III.G7.41 | *D. Cassinum* | «Cassini» | omissione del titolo |
| III.G7.42 | *R. P. Ango in academia Flexiensi* | «P. Ango», «the University of La Fleche» | semplificazione |
| III.G7.46 | *in 3gr* | «in ♏ 3°» | esplicitazione (corretta) |
| III.G7.50 | *Congruunt igitur* | «From all this it is plain that» | parafrasi |

**SVG di Motte che non tornano con il latino.** Ho controllato tutti i **119** SVG distinti (160 occorrenze) delle righe 1–714 dell’estratto, sul LaTeX di `svg_tex.tsv`: lettere della costruzione, frazioni delle distanze fra le fisse (SVG 1193–1214, tutte uguali al latino), frazioni delle osservazioni, ore, frazioni delle tabelle. Non tornano:

| SVG | LaTeX | Lettura attesa dal latino |
|---|---|---|
| 1174 | `3 \mathrm S \sigma + 3 i \lambda` | 3Sσ + 3Iλ (I maiuscola) |
| 1169 (in «ε, α, κ, λ» e «through G, g, and λ») | `\lambda` | γ |
| 1180 | `\mathrm{G}g \lambda` | Ggγ |
| 1183 | `\kappa \lambda` | κγ |
| 1192 | `\eta` | «n» nella trascrizione (probabilmente η: torna con Motte) |
| 1226 | `\tfrac{4}{5}\mathrm{PE}` | 1/10 BF |
| 691 (7 marzo) | `\tfrac{1}{10}` | 1/11 (BF) |
| 1241 | `\tfrac{1}{2}\gamma \delta` | 1/4 γδ |
| 1247 | `\tfrac{1}{3} \gamma \delta` | 1/7 γδ |
| 643 (Tab. 4, 12 dic., long. oss.) | `\tfrac{1}{2}` | ⅓ |
| 643 (Tab. 4, 29 dic., lat. oss.) | `\tfrac{1}{2}` | 1/12 |

Tutti gli altri SVG controllati tornano.

---

## Note editoriali e fisiche

Queste note sono aggiunte del presente fascicolo, non affermazioni tradotte da Newton. Le verifiche sono state eseguite con script Python in `tmp/26a/` (`verifica.py`, `distanze.py`, `costruzione.py`, `stelle.py`, `cmp_motte.py`), che leggono le tabelle ricostruite dalla trascrizione senza usare i valori da verificare. Ciò che proviene da conoscenza generale e non dalle fonti allegate è marcato «(non verificato sulle fonti allegate)».

### N1. Convenzioni astronomiche del testo

- **Segni zodiacali.** ♈ = Ariete, ♉ = Toro, ♊ = Gemelli, ♋ = Cancro, ♌ = Leone, ♍ = Vergine, ♎ = Bilancia, ♏ = Scorpione, ♐ = Sagittario, ♑ = Capricorno, ♒ = Acquario, ♓ = Pesci. Ogni segno è un arco di 30° di eclittica a partire dall’equinozio di primavera; la longitudine si conta in gradi dentro il segno: ♑ 6° 32′ = 270° + 6° 32′ = 276° 32′. Non sono le costellazioni.
- **Orbe magno.** *Orbis magnus* è l’orbita annua della Terra; il suo semidiametro (la distanza media Terra–Sole) è l’unità delle distanze, divisa in 10000 o 100000 parti.
- **Stile vecchio.** Le date sono secondo il calendario giuliano, in uso in Inghilterra; nel 1680–81 esso era indietro di dieci giorni rispetto al gregoriano: il 12 dicembre 1680 giuliano è il 22 dicembre gregoriano (non verificato sulle fonti allegate). I giorni della settimana del testo tornano con le date giuliane (§ A.3).
- **Ore astronomiche.** Nelle tabelle il giorno comincia a mezzogiorno e le ore si contano da 0 a 24: «nov. 3, 16.47» è il 4 novembre alle 4h 47′ del mattino. Così si spiega perché le osservazioni di Kirch «del 4, 6 e 11 novembre» compaiono come 3, 5 e 10 novembre (III.G7.33–36).
- **Tempo apparente e tempo vero.** Il tempo apparente è quello del Sole vero (meridiana); il tempo «vero» delle tabelle, o «equato», è il tempo medio, corretto con l’**equazione del tempo** (*æquatio*, «equazione» nel senso di correzione astronomica). Nella Tabella 1 la differenza vero − apparente cresce regolarmente da 0 min (12 dic.) a 14,9 min (30 gen.) e poi cala a 14,7 min (5 feb.), come l’equazione del tempo in quella stagione (non verificato sulle fonti allegate per il valore moderno).
- **Saetta.** *Sagitta* è la «freccia» dell’arco: il segmento perpendicolare alla corda fra la corda e l’arco. Qui tV è la saetta dell’arco di orbe magno TtτT: la distanza della Terra intermedia t dalla corda Tτ.
- **Linea occulta.** Linea di costruzione tracciata leggermente, che si cancella dopo l’uso.
- **«Secondo l’ordine dei segni».** Moto diretto, nel verso delle longitudini crescenti (♈ → ♉ → …), come quello dei pianeti.

### N2. Le sei tabelle: ricostruzione e controlli

**Ricostruzione.** La trascrizione dà ogni cella su una riga e separa le celle con righe vuote. Uno script ha raggruppato le celle per riga (6 celle per riga nella Tabella 1, 8 nella Tabella 4, 6 nella Tabella 5, 7 nella Tabella 6, con le quattro righe di novembre ridotte a 3 celle) e ha letto le frazioni appiattite. Il confronto automatico riga per riga con le tabelle di Motte (separate da «|») trova le sole differenze elencate nel § A.9.

**Tabella 1 (Flamsteed–Halley).** Moto del Sole fra righe consecutive: 61,2′, 61,2′, 61,2′, **57,9′**, **71,1′**, 61,1′, 61,1′, 61,0′, 61,0′, 60,9′, 60,7′, 60,5′, 60,5′ al giorno. Le due anomalie scompaiono se la longitudine del Sole del 29 dicembre è 19° 19′ 43″ (Motte) anziché 19° 9′ 43″ (trascrizione): l’errore è di 10′ esatti, cioè una cifra. Il moto del Sole di circa 61′ al giorno in dicembre–gennaio è quello atteso vicino al perielio della Terra (non verificato sulle fonti allegate).

**Tabella 4 (orbita grafica di Newton).** Le differenze sono «ricavato − osservato». Ricalcolate: in longitudine +0,67′, +1,92′, +0,13′, −1,11′ (tabella +1, +2, +0, −1: arrotondate al primo); in latitudine −7,50′, −10,08′, +2,27′, +0,50′ (tabella −7½, −10 1/12, +2¼, +½). Tutte tornano. Le longitudini e latitudini «osservate» di questa tabella non coincidono con quelle delle Tabelle 1 e 2 (per esempio 12 dic.: 6° 31⅓′ e 8° 26′ contro 6° 32′ 30″ e 8° 28′ 0″; 5 mar.: 29° 20 6/7′ contro 29° 18′ 0″): il testo non spiega la differenza.

**Tabella 5 (parabola di Halley).** «Errori» = calcolato − osservato, con gli osservati della Tabella 1 (12 dic.–5 feb.) e della Tabella 2 (25 feb., 5 mar.). Su 32 errori, **31 tornano al secondo**; non torna il segno dell’errore in latitudine del 30 dicembre (calcolato −0′33″, tabella +0′33″; Motte −0.33). I tempi della tabella sono i tempi veri della Tabella 1 arrotondati al minuto.

**Distanze dal Sole (Tabelle 4 e 5).** Le ho ricalcolate con l’equazione del moto parabolico (equazione di Barker, con la costante di Gauss *k* = 0,01720209895; non verificato sulle fonti allegate), dal perielio dell’8 dicembre, 0h 4′:

| Data | Tab. 5 | calcolo (q = 0,006075) | Data | Tab. 4 | calcolo (q = 0,00592) |
|---|--:|--:|---|--:|--:|
| 12 dic. | 28028 | 28026 | 12 dic. | 2792 | 2804 |
| 21 dic. | 61076 | 61073 | 29 dic. | 8403 | 8404 |
| 29 dic. | **14021** | **84020** | 5 feb. | 16669 | 16669 |
| 5 gen. | 101440 | 101440 | 5 mar. | 21737 | 21622 |
| 5 feb. | 166686 | 166679 | | | |
| 5 mar. | 216205 | 216201 | | | |

Per Halley l’accordo è entro lo 0,01% in tutte le 16 righe, tranne il 29 dicembre: **14021 è un errore della trascrizione o della stampa per 84021** (Motte). Per Newton l’accordo è entro lo 0,5%, come ci si attende da una costruzione grafica. Lo stesso calcolo dà per il 3 novembre, 16h 47′, la distanza 115545, contro 115546 di III.G7.37.

**Tabella 6 (ellisse di Halley).** Su 42 errori, **41 tornano al secondo**; non torna il segno dell’errore in latitudine del 5 marzo (calcolato −0′26″, tabella +0′26″, anche in Motte). Gli osservati coincidono con quelli delle Tabelle 1 e 2 e di III.G7.34–36, salvo: la latitudine del 10 gennaio (23° 43′ 32″ contro 23° 43′ 52″ della Tabella 1: l’errore −0′7″ della riga è coerente con 32, quindi la differenza è nei dati di partenza di Halley, o in una delle due stampe); la latitudine del 10 novembre (0° 27′ contro «circa 26′» di III.G7.36). I luoghi calcolati del 16, 18, 20 e 23 novembre coincidono con i valori «secondo la teoria» citati in III.G7.41, 43, 45, 48.

### N3. La costruzione e l’operazione numerica di Newton

**Che cosa fa la costruzione.** Si cerca la distanza della cometa dalla Terra nella seconda osservazione (tB, proiettata sull’eclittica). Per un valore di prova di B: (1) la saetta BE dell’arco della cometa è ricavata dalla saetta tV dell’arco della Terra con il rapporto delle forze del Sole (inversamente come i quadrati delle distanze, nel piano dell’eclittica) e il Lemma XI; (2) la corda AEC, divisa da E nel rapporto dei tempi (Lemmi VII–VIII), dà i luoghi A e C; (3) la lunghezza della corda nell’orbita vera, MN, si confronta con la lunghezza MP che una cometa parabolica percorre in quel tempo (Cor. del Lemma X, Cor. 3 della Prop. XL). Se MP = MN, B è il valore giusto; altrimenti lo scarto NP = CG si usa per interpolare fra tre valori di prova (i cerchi per G, g, γ e per F, f, φ). In termini moderni è un metodo di **falsa posizione** sulla distanza geocentrica, con un’interpolazione grafica. La formula per BE, nella notazione moderna: BE = tV · SB · St² / (SB² + h²)^(3/2), con h = tB · tan β₂.

**I numeri di III.G7.28** (osservazioni del 21 dic., 5 gen., 25 gen.):

| Grandezza | Testo | Ricalcolo | Come |
|---|--:|--:|---|
| V, W | — | 14,98 d; 20,08 d | tempi veri della Tab. 1 |
| tV | 455 | 463 | saetta di un arco circolare di raggio St = 9842,1, con le longitudini del Sole della Tab. 1 |
| SB | 9747 | 9761 | triangolo S t B: St = 9842,1, tB = 5657, elongazione 72,44° (Sole ♑ 26° 22′, cometa ♈ 8° 49′) |
| BE (prima volta) | 412 | 412,2 | formula sopra, con SB = 9747 e β₂ = 26° 15′ 7″ |
| BE (seconda volta) | 421 | 421,1 | 412 · (9747 / (9503 + 413/3))² |
| X | 8528,4 | 8528,4 | 243,2747 parti al giorno (Cor. 3 Prop. XL) × 35,0567 giorni |
| MP | 8450 | 8450,2 | 8528,4 · √(10000/10186) |
| NP | 25 | 25 | 8475 − 8450 |

Le piccole differenze per tV e SB sono compatibili con una costruzione grafica e con l’orbita non circolare della Terra. Il criterio di scelta degli intervalli (III.G7.03: differenza : somma = somma : 600 giorni) qui non è rispettato alla lettera: (20,08 − 14,98)/35,06 = 0,146 contro 35,06/600 = 0,058. Newton lo presenta come preferibile, non come necessario.

### N4. Gli elementi dell’orbita parabolica

**Newton (III.G7.28).** Con nodo ascendente in ♑ 1° 53′, inclinazione 61° 20⅓′ e perielio a 8° 38′ dal nodo, prima del nodo, la longitudine eclittica del perielio risulta ♐ 27° 43,1′ e la latitudine −7° 34,1′: esattamente i valori del testo (♐ 27° 43′, latitudine australe 7° 34′). L’area descritta in un giorno, per il Cor. 4 della Prop. XL (1216373½ con lato retto quadruplo del raggio, in rapporto subduplicato dei lati retti), è 1216373,5 · √(236,8/40000) = 93590, contro 93585 del testo. Il lato retto 236,8 (su 10000) dà la distanza perielica q = 59,2 parti, cioè 0,00592 orbe magni.

**Halley (III.G7.31).** Il lato retto 2430 su 100000 dà q = 0,006075: un poco maggiore di quello di Newton. In unità moderne q ≈ 0,0061 UA ≈ 910 000 km, cioè circa 1,3 raggi solari dal centro del Sole: la cometa del 1680 passò a meno di un raggio solare dalla superficie del Sole (non verificato sulle fonti allegate per il raggio solare).

### N5. L’ellisse di Halley

- **Periodo.** Asse maggiore 1382957 parti con distanza media 10000: semiasse *a* = 69,148. Per la terza legge (Prop. XL, Cor. 1) il periodo è *a*^(3/2) = **575,000 anni**: il dato di Halley è esatto.
- **Eccentricità e perielio.** Con l’asse coniugato 18481,2: semiasse minore *b* = 0,92406, eccentricità *e* = 0,999911, distanza perielica *q* = *a* − √(*a*² − *b*²) = 0,006175, un poco maggiore di quella della parabola (0,006075).
- **Nodi e perielio.** ♐ 22° 44′ 25″ + 9° 17′ 35″ = ♑ 2° 2′ 0″ esattamente. Quindi il perielio è a 9° 17′ 35″ dal nodo in ♑ 2° 2′, e la longitudine ♐ 22° 44′ 25″ è contata nel piano dell’orbita (*in hoc plano*). Due incoerenze del testo (anche in Motte): (1) il nodo **ascendente** è posto in ♋ 2° 2′, mentre nelle orbite paraboliche (III.G7.28, 31) l’ascendente è in ♑ e il discendente in ♋, e il perielio è misurato dal nodo in ♑; (2) la distanza 9° 17′ 35″ è detta «nel piano dell’eclittica», ma torna come arco nell’orbita: proiettata sull’eclittica sarebbe circa 4° 31′. Non correggo; segnalo per la stampa.
- **Le quattro apparizioni.** Settembre del 44 a.C. (dopo l’uccisione di Cesare), 531, 1106, 1680: gli intervalli sono 574, 575, 574 anni contando che non esiste l’anno zero (non verificato sulle fonti allegate per la data della morte di Cesare). Il valore moderno del periodo della cometa del 1680 è dell’ordine di migliaia di anni, e l’identificazione con le comete del 44 a.C., del 531 e del 1106 non è accettata oggi (non verificato sulle fonti allegate).
- **Tempo del perielio.** Ellisse: 7 dic., 23h 9′ (tempo equato); parabola: 8 dic., 0h 4′: 55 minuti di differenza.

### N6. Le fisse di Perseo e le misure al micrometro

**Scala.** Dalle coordinate di Pound (Tabella 3) la distanza AB è 126,7′; con AB = 80 7/12 parti, una parte del micrometro vale 1,572′ d’arco.

**Distanze fra le fisse.** Ricalcolate le 19 distanze di III.G7.14 fra stelle che sono in tabella (D e O non lo sono): scarti fra −0,49 e +1,03 parti (il maggiore per AI); la media degli scarti assoluti è 0,3 parti, cioè circa 0,5′. Le misure di Newton e le posizioni di Pound sono coerenti. Con le coordinate di M e N **di Motte** (latitudini 2° 7′ 20″ e 2° 31′ 9″) BN e CN risulterebbero 335 e 389 parti invece di 46 e 31: **le cifre di Motte sono errate**, quelle latine tornano. Non tornano invece bene con le coordinate di Pound due dati che riguardano la stella M, «piccolissima» (III.G7.23): LM : LN = 0,29 (testo 2 : 9 = 0,22) e MT : ML = 0,29 (testo 1/2); l’allineamento L, M, H torna entro mezzo grado.

**Le osservazioni della cometa** (con le posizioni della Tabella 2): 1° marzo, CR/CK = 0,3563 (testo 16/45 = 0,3556), R a 0,04′ dalla retta CK; 2 marzo, CS/FC = 0,4445 (testo 4/9), distanza di F da CS = 0,0424 FC (testo 1/24 = 0,0417), rapporto delle distanze di B e di F = 5,06 (testo 5); 25 febbraio, pE/AE = 0,220 (testo 3/14 = 0,214); 7 marzo, Vα/Vβ = 1,29 (testo 5/4); 9 marzo, γX/γδ = 0,29 (latino 1/4, Motte 1/2) e perpendicolare da δ = 0,44 γδ (testo 2/5). L’accordo conferma la lettura latina 1/4 contro l’1/2 di Motte per γX. Per il 7 marzo la frazione di BF tagliata da Vα risulta 0,14 (latino 1/11, Motte 1/10): nessuna delle due letture è confermata.

### N7. Il cammino apparente della cometa

- **Le due intersezioni con l’eclittica.** Interpolando le latitudini calcolate della Tabella 6 (+0° 25′ il 10 nov. in ♍ 15° 33′, −0° 53′ il 16 nov. in ♎ 8° 17′), la cometa attraversa l’eclittica verso sud a circa ♍ 22° 51′ («alla fine della Vergine»). La seconda intersezione, verso nord, avviene vicino al Sole all’inizio di dicembre, «al principio del Capricorno»: con ♑ 0°–1° l’intervallo è di circa 97°–98°, come dice il testo. Un cerchio massimo taglierebbe l’eclittica in due punti opposti (180°).
- **Nove segni.** Da ♌ 29° 51′ (3 nov.) a ♊ 0° 43′ (9 mar.) la longitudine cresce di 270° 52′: nove segni.
- **Velocità.** Dalla Tabella 6: fra il 18 e il 20 novembre (tempi 21h 34′ e 17h 0′) 9° 18′ in 1,81 giorni, cioè 5,1° al giorno; fra il 21 e il 24 dicembre 13° 41′ in 2,99 giorni, 4,6° al giorno: «circa cinque gradi al giorno».
- **«Traiettoria».** Nel capoverso finale *trajectoria* è il cammino apparente sulla sfera celeste: l’orbita nello spazio, una parabola, giace in un piano che passa per il Sole.

### N8. Ore locali e differenze di longitudine

Il testo converte le ore locali in ore di Londra. Le differenze implicite, a 15° per ora: Roma e Venezia 50 min (12° 30′ est); Avignone 18 min (4° 30′ est); Boston 4h 44′ (71° ovest); Maryland 5h (75° ovest); Balasore 5h 40′ (85° est); Norimberga 30 min (7° 30′ est); La Flèche 9 min (2° 15′ est); Coburgo, secondo Halley, 11° est. Con le longitudini moderne (Roma 12,5° E, Venezia 12,3° E, Avignone 4,8° E, Boston 71,1° O, Balasore 86,9° E, Norimberga 11,1° E, La Flèche 0,1° O; non verificato sulle fonti allegate) tornano bene Roma, Venezia, Avignone, Boston e Balasore; non tornano **Norimberga** (7° 30′ contro circa 11°, e meno di Coburgo, che è più a ovest) e **La Flèche** (che ha quasi la longitudine di Londra). Li segnalo senza correggere.

Le differenze fra tempo apparente e tempo vero nei tre luoghi di Kirch sono 15 min (3 nov.), 21 min (5 nov.) e 13 min (10 nov.); l’equazione del tempo varia di poco in quei giorni (circa 15 min; non verificato sulle fonti allegate): il valore del 5 novembre è sospetto (§ A.7). Per il 19 novembre il testo dà «9h 44′ di Londra» e la Tabella 6 la riga «18, 21.34» (9h 34′ del mattino) con gli stessi valori teorici.

### N9. Gli osservatori

Il testo nomina osservatori a Londra (Flamsteed, Newton, Pound, Hooke, Halley), a Coburgo (Kirch), a Roma (Ponthæus, Cellius), ad Avignone (Galletius), a La Flèche (Ango), a Padova e Venezia (Montanari), a Norimberga (Zimmerman), a Cambridge, a Boston, in Giamaica, nel Maryland (Storer) e a Balasore. La cometa del 1680 è oggi chiamata anche «cometa di Kirch», il primo a scoprirla al telescopio (non verificato sulle fonti allegate). Per il liceo è un esempio notevole di rete internazionale di osservazioni ridotte a un unico tempo (Londra) e a un unico sistema di riferimento (le fisse di Pound).

---

## Controllo della copertura

Pagine 1726 dai marcatori ‹n› della trascrizione (la proposizione comincia a p. 492; il marcatore ‹506› manca). Motte: estratto senza marcatori di pagina, «sezione corrispondente».

| Identificatori | Incipit latino | Contenuto | 1726 | Motte 1846 |
|---|---|---|---|---|
| III.G7.01–III.G7.03 | *Cometæ in parabola moti* … *Seligantur tres observationes* | enunciato, premessa, scelta delle osservazioni | p. 492 | Prop. XLI |
| III.G7.04 | *Designent S solem* | dati, saetta, prima corda AEC | p. 493 | idem |
| III.G7.05–III.G7.06 | *Ad AC bisectam in I erige* … *erigantur* | correzione di BE; prova con MP e MN | pp. 493–494 | idem |
| III.G7.07 | *Eadem methodo* | tre punti di prova, cerchi, parabola; C.V.T. | p. 494 | idem |
| III.G7.08 | *Constructionis hujus demonstratio* | dimostrazione | pp. 494–495 | idem |
| III.G7.09 | *Cæterum puncta B, b, β* | scelta dei punti di prova | p. 495 | idem |
| III.G7.10–III.G7.11 | *Exemplum. Proponatur cometa anni 1680* | Tabella 1 (Flamsteed–Halley) | pp. 495–496 | Example |
| III.G7.12–III.G7.13 | *His adde observationes* | Tabella 2 (Newton) | p. 496 | idem |
| III.G7.14 | *Hæ observationes telescopio septupedali* | fisse di Perseo, distanze al micrometro | pp. 496–497 | idem |
| III.G7.15–III.G7.17 | *Tandem Poundius* … *Positiones vero* | Tabella 3 (fisse di Pound) | p. 497 | idem |
| III.G7.18–III.G7.26 | *Die veneris Feb. 25* … *Eadem nocte hora 12* | osservazioni dal 25 febbraio al 9 marzo | pp. 497–499 | idem |
| III.G7.27 | *Ex hujusmodi observationibus* | riduzione, precisione | p. 499 | idem |
| III.G7.28–III.G7.30 | *Jam ad orbem cometæ determinandum* … *Tandem ut constaret* | operazione numerica, elementi, Tabella 4 | pp. 499–500 | idem |
| III.G7.31–III.G7.32 | *Postea vero Halleius* | parabola di Halley, Tabella 5 | p. 500 | idem |
| III.G7.33–III.G7.37 | *Apparuit etiam hic cometa* … *Observatio prima* | osservazioni di Kirch | pp. 500–501 | idem |
| III.G7.38–III.G7.40 | *Porro Halleius observando* … *Observationes cometæ hujus* | ellisse di Halley, Tabella 6, accordo | pp. 501–502 | idem |
| III.G7.41–III.G7.49 | *In tabula præcedente omisimus* … *Nov. 25.* | osservazioni dal 17 al 25 novembre | pp. 502–505 | idem |
| III.G7.50 | *Congruunt igitur hæ observationes* | conclusione | pp. 505–506 | idem (fino a «…cannot be otherwise than true.») |

**Controlli eseguiti.**

1. **Copertura frase per frase.** Ho riletto in sequenza ogni periodo della trascrizione, da *Cometæ in parabola moti* a *non potest non esse vera* (riga 1906), contro la traduzione: nessuna frase manca. Le frasi lunghe (III.G7.04, III.G7.08, III.G7.28, III.G7.38, III.G7.46) sono divise in italiano senza omettere membri. I 50 identificatori sono consecutivi e unici (controllo automatico).
2. **Tabelle.** Tutte e sei ricostruite con uno script dalle celle della trascrizione (14, 7, 17, 4, 16 e 25 righe) e confrontate automaticamente cella per cella con Motte (§ A.9). Differenze «osservato − calcolato» ricalcolate riga per riga: Tabella 4, 8 su 8 tornano (con l’arrotondamento al primo); Tabella 5, 31 su 32; Tabella 6, 41 su 42. Le due che non tornano sono segni (Tab. 5, 30 dic.; Tab. 6, 5 mar.). Altre cifre che non tornano con i controlli indipendenti: Sole del 29 dic. (Tab. 1), distanza del 29 dic. (Tab. 5), latitudine osservata del 10 gen. (Tab. 6 contro Tab. 1). Nessuna è corretta nel testo (note sotto le tabelle, § A.7, N2).
3. **Matematica e astronomia** (script in `tmp/26a/`): grandezze dell’operazione di Newton (N3); elementi di Newton e area diurna (N4); distanze con l’equazione di Barker (N2); periodo, eccentricità e nodi dell’ellisse di Halley (N5); distanze fra le fisse e osservazioni micrometriche (N6); punti medi e medie di III.G7.36, 46, 48; intersezioni con l’eclittica, nove segni, velocità (N7); differenze di longitudine (N8); giorni della settimana (§ A.3).
4. **Parte B.** `check.py` sul file finale: JSON valido; tutte le stringhe `la` (2 enunciati, 55 passi) sono sottostringhe esatte della trascrizione; tutte le stringhe `en` sono sottostringhe esatte di Motte; ogni identificatore di `copertura` è presente nel testo.
5. **Motte e SVG.** Confronto di tutta la sezione corrispondente (righe 1–714); 119 SVG distinti controllati, 11 letture che non tornano (§ A.9).
6. **Separazione fra testo e commento.** Il testo tradotto non contiene formule moderne; le integrazioni sono tra parentesi quadre («[leggi ♌]», «[dello Scorpione]»).

**Non ho potuto verificare:**

- **la stampa del 1726**: i punti del § A.7 restano da controllare sulla scansione ECCO, in particolare le cifre delle tabelle;
- **le figure originali** della costruzione (i due [FIG]): la disposizione dei punti è ricostruita dal testo, e in particolare non ho potuto verificare la posizione di σ, ξ e μ e la costruzione σξ = 3Sσ + 3Iλ;
- **le cifre controverse fra latino e Motte nelle osservazioni micrometriche** (1/10 BF o 4/5 PE il 25 febbraio; 1/11 o 1/10 BF il 7 marzo; 1/7 o 1/3 γδ il 9 marzo), che i dati disponibili non decidono;
- **la paginazione di Motte**: l’estratto non ha marcatori di pagina;
- i **dati moderni** usati nelle note (longitudini delle città, equazione del tempo, distanza perielica in km, periodo moderno della cometa), che vengono da conoscenza generale.

---

## Registro del lavoro successivo

| Unità | Stato |
|---|---|
| Libro III, Prop. XLI, prima parte (costruzione, dimostrazione, Esempio fino a *Congruunt igitur…*) | **Fascicolo 26a, presente documento, prima versione** |
| Prop. XLI, seconda parte (*Cæterum trajectoriam…*, code e atmosfere) | Fascicolo 26b (altro traduttore) |
| Cifre delle tabelle e refusi (§ A.7) | Da verificare sulla stampa del 1726 (scansione ECCO) |
| Nodo «ascendente in ♋» e «nel piano dell’eclittica» dell’ellisse di Halley (N5) | Da verificare sulla stampa; eventuale nota del curatore |
| *occulta* «linea occulta»; *digitus* «pollice»; *spica ♍* «Spiga della Vergine» | Da decidere (A.0) |
| Pagine interattive | Parte B: L3-P41-Constr (costruzione, 33 passi) e L3-P41-Ex (22 passi, con le sei tabelle in `dati`). Candidati: un grafico «osservato contro calcolato» per le Tabelle 5–6; una mappa delle fisse di Perseo con i luoghi della cometa (Tabelle 2–3); un’animazione della costruzione con il valore di prova tB |
| Figure NATP00303 | Da consultare per confermare `figura_base` |
| Revisione filologica e scientifica indipendente | Da eseguire |

Il presente testo è una nuova traduzione assistita da IA. Non riproduce traduzioni italiane o inglesi moderne. **Licenza prevista** (decisione del curatore, Fascicolo 3): testi e traduzioni CC BY-SA 4.0, codice MIT. La trascrizione latina è © The Newton Project; i testi di Motte sono di pubblico dominio.

---

## Parte B — Dati per le pagine interattive

Unità incluse: **L3-P41-Constr** (enunciato, costruzione, dimostrazione e scelta dei punti di prova: 33 passi, uno per frase latina di III.G7.03–III.G7.09; la premessa III.G7.02 è coperta senza passi) e **L3-P41-Ex** (l’Esempio: 22 passi per le frasi dei capoversi di calcolo e di conclusione III.G7.28, 29, 31, 38, 40, 50; gli altri capoversi sono coperti da `copertura` senza passi; le sei tabelle sono nel campo `dati` con i controlli).

Convenzioni:

- `la`: testo latino esatto della trascrizione, refusi e caratteri invisibili compresi (U+2062, U+2064 delle frazioni appiattite);
- `it`: la traduzione di questo fascicolo;
- `en`: Motte 1846, allineato per senso; quando Motte unisce due frasi latine con «;», `en` è la porzione corrispondente, spiegata in `nota`; i marcatori `[SVG n]` restano e sono ignorati dal controllo;
- `dipende_da`: soltanto i rimandi citati nella frase latina;
- `figura.mostra`: elementi da rendere visibili, cumulativi; `figura.evidenzia`: relazioni da mettere in risalto;
- `dati`: righe delle tabelle con i valori della trascrizione (angoli come stringhe «segno g.p.s» o liste di numeri; frazioni come decimali); `controlli`: esito delle verifiche.

```json
{
 "fascicolo": "26a-L3-P41",
 "versione": "0.1",
 "data": "2026-11-08",
 "convenzioni": {
  "dipende_da": "solo rimandi citati esplicitamente nella frase latina",
  "en": "Motte 1846, allineato per senso; i marcatori [SVG n] restano nel testo e sono ignorati dal controllo",
  "figura.mostra": "elementi da rendere visibili al passo, cumulativi salvo indicazione",
  "la": "",
  "dati": "tabelle come nel latino; angoli come [segno, gradi, primi, secondi] o in primi decimali; differenze = calcolato − osservato"
 },
 "unita": [
  {
   "id": "L3-P41-Constr",
   "tipo": "Propositio/Problema",
   "titolo": "Prop. XLI — orbita parabolica di una cometa da tre osservazioni: costruzione e dimostrazione",
   "copertura": [
    "III.G7.01",
    "III.G7.02",
    "III.G7.03",
    "III.G7.04",
    "III.G7.05",
    "III.G7.06",
    "III.G7.07",
    "III.G7.08",
    "III.G7.09"
   ],
   "fonti": {
    "la": "",
    "en": "Motte 1846, sezione corrispondente (Book III, Prop. XLI)"
   },
   "enunciato": {
    "la": "",
    "it": "Determinare la traiettoria di una cometa che si muove in una parabola, a partire da tre osservazioni date.",
    "en": "From three observations given to determine the orbit of a comet moving in a parabola."
   },
   "figura_base": {
    "punti": [
     "S",
     "T",
     "t",
     "τ",
     "A",
     "B",
     "C",
     "V",
     "E",
     "I",
     "i",
     "λ",
     "μ",
     "σ",
     "ξ",
     "M",
     "N",
     "O",
     "D",
     "P",
     "G",
     "Q",
     "Y",
     "b",
     "β",
     "e",
     "a",
     "c",
     "g",
     "ε",
     "α",
     "κ",
     "γ",
     "F",
     "f",
     "φ",
     "X",
     "Z"
    ],
    "vincoli": [
     "S Sole; T, t, τ luoghi della Terra sull’orbe magno alle tre osservazioni",
     "TA, tB, τC rette delle longitudini osservate, nel piano dell’eclittica",
     "tV ⊥ corda Tτ (saetta)",
     "B su tB scelto a piacere; E su BS con BE dato (passo p5)",
     "AEC per E con A su TA, C su τC e AE : EC = V : W (Lemma VII)",
     "I punto medio di AC; Ii ⊥ AC; Bi ∥ AC; λ = Si ∩ AC; iIλμ rettangolo",
     "Iσ = 3Iλ; σξ = 3Sσ + 3Iλ (per S)",
     "AM, CN, IO ⊥ AC; AM, CN tangenti delle latitudini sui raggi TA, τC; O = MN ∩ IO",
     "ID = Sμ + 2iλ/3 su IA prolungata; P su MN con MP = X·√(R/OD), R distanza media",
     "CG = NP su AC; G, g, γ dai tre punti di prova B, b, β; cerchio Ggγ ∩ τC = Z; cerchio Ffφ ∩ AT = X",
     "Y = TA ∩ τC; Q = traccia dell’orbita ∩ tB"
    ]
   },
   "passi": [
    {
     "id": "L3-P41-Constr-p1",
     "la": "",
     "it": "Si scelgano tre osservazioni separate l’una dall’altra da intervalli di tempo uguali con ottima approssimazione.",
     "en": "Select three observations distant one from another by intervals of time nearly equal",
     "dipende_da": [],
     "figura": {
      "mostra": [
       "T, t, τ (tre luoghi della Terra)"
      ],
      "evidenzia": []
     },
     "nota": "Motte unisce questa frase alla seguente; «en» è la porzione corrispondente."
    },
    {
     "id": "L3-P41-Constr-p2",
     "la": "",
     "it": "L’intervallo di tempo in cui la cometa si muove più lentamente sia però un poco maggiore dell’altro: in modo, cioè, che la differenza dei tempi stia alla somma dei tempi come la somma dei tempi sta a seicento giorni circa; oppure che il punto E (nella figura del Lemma VIII) cada con ottima approssimazione nel punto M, e se ne scosti piuttosto verso I che verso A.",
     "en": "but let that interval of time in which the comet moves more slowly be somewhat greater than the other; so, to wit, that the difference of the times may be to the sum of the times as the sum of the times to about 600 days; or that the point E may fall upon M nearly, and may err therefrom rather towards I than towards A.",
     "dipende_da": [
      "Lemma VIII (figura)"
     ],
     "figura": {
      "mostra": [],
      "evidenzia": [
       "intervalli V, W disuguali"
      ]
     },
     "nota": "Motte: «about 600 days»; «plus minus sexcentos» = seicento all’incirca."
    },
    {
     "id": "L3-P41-Constr-p3",
     "la": "",
     "it": "Se non si dispone di osservazioni siffatte, si deve trovare un nuovo luogo della cometa per il Lemma VI.",
     "en": "If such direct observations are not at hand, a new place of the comet must be found, by Lem. VI.",
     "dipende_da": [
      "Lemma VI"
     ],
     "figura": {
      "mostra": [],
      "evidenzia": []
     },
     "nota": "Motte aggiunge «direct» (observations)."
    },
    {
     "id": "L3-P41-Constr-p4",
     "la": "",
     "it": "Indichino S il Sole; T, t, τ tre luoghi della Terra nell’orbe magno; TA, tB, τC le tre longitudini osservate della cometa; V il tempo fra la prima e la seconda osservazione; W il tempo fra la seconda e la terza; X la lunghezza che la cometa potrebbe descrivere in tutto quel tempo con la velocità che ha alla distanza media della Terra dal Sole, lunghezza che si deve trovare per il Cor. 3 della Prop. XL del Libro III; e tV la perpendicolare sulla corda Tτ.",
     "en": "Let S represent the sun; T, t, [SVG 1166] , three places of the earth in the orbis magnus; TA, tB, [SVG 1167] , three observed longitudes of the comet; V the time between the first observation and the second; W the time between the second and the third; X the length which in the whole time V + W the comet might describe with that velocity which it hath in the mean distance of the earth from the sun, which length is to be found by Cor. 3, Prop. XL, Book III; and tV a perpendicular upon the chord [SVG 1168] .",
     "dipende_da": [
      "Prop. XL, Cor. 3 (Libro III)"
     ],
     "figura": {
      "mostra": [
       "S",
       "T, t, τ sull’orbe magno",
       "rette TA, tB, τC",
       "corda Tτ",
       "tV ⊥ Tτ"
      ],
      "evidenzia": [
       "X: lunghezza percorsa in V + W alla velocità che compete alla distanza media"
      ]
     },
     "nota": "Motte esplicita «in the whole time V + W»."
    },
    {
     "id": "L3-P41-Constr-p5",
     "la": "",
     "it": "Sulla longitudine osservata intermedia tB si prenda a piacere un punto B come luogo della cometa nel piano dell’eclittica, e di lì verso il Sole S si conduca la linea BE, che stia alla saetta tV come il contenuto sotto SB e St² sta al cubo dell’ipotenusa del triangolo rettangolo i cui lati sono SB e la tangente della latitudine della cometa nella seconda osservazione riferita al raggio tB.",
     "en": "In the mean observed longitude tB take at pleasure the point B, for the place of the comet in the plane of the ecliptic; and from thence, towards the sun S, draw the line BE, which may be to the perpendicular tV as the content under SB and St2 to the cube of the hypothenuse of the right angled triangle, whose sides are SB, and the tangent of the latitude of the comet in the second observation to the radius tB.",
     "dipende_da": [],
     "figura": {
      "mostra": [
       "B su tB (scelto a piacere)",
       "E su BS"
      ],
      "evidenzia": [
       "BE : tV = SB·St² : (SB² + (tB·tan β₂)²)^(3/2)"
      ]
     },
     "nota": "Formula della nota N3; «tangens … ad radium tB» = tB · tan β₂."
    },
    {
     "id": "L3-P41-Constr-p6",
     "la": "",
     "it": "E per il punto E si conduca (per il Lemma VII di questo Libro) la retta AEC, le cui parti AE, EC, terminate alle rette TA e τC, stiano fra loro come i tempi V e W: A e C saranno con ottima approssimazione i luoghi della cometa nel piano dell’eclittica nella prima e nella terza osservazione, purché B sia il suo luogo assunto correttamente nella seconda.",
     "en": "And through the point E (by Lemma VII) draw the right line AEC, whose parts AE and EC, terminating in the right lines TA and [SVG 1167] , may be one to the other as the times V and W: then A and C will be nearly the places of the comet in the plane of the ecliptic in the first and third observations, if B was its place rightly assumed in the second.",
     "dipende_da": [
      "Lemma VII"
     ],
     "figura": {
      "mostra": [
       "retta AEC con A su TA, C su τC"
      ],
      "evidenzia": [
       "AE : EC = V : W"
      ]
     }
    },
    {
     "id": "L3-P41-Constr-p7",
     "la": "",
     "it": "Su AC, divisa a metà in I, innalza la perpendicolare Ii.",
     "en": "Upon AC, bisected in I, erect the perpendicular Ii.",
     "dipende_da": [],
     "figura": {
      "mostra": [
       "I punto medio di AC",
       "Ii ⊥ AC"
      ],
      "evidenzia": []
     }
    },
    {
     "id": "L3-P41-Constr-p8",
     "la": "",
     "it": "Per il punto B conduci la linea occulta Bi parallela ad AC.",
     "en": "Through B draw the obscure line Bi parallel to AC.",
     "dipende_da": [],
     "figura": {
      "mostra": [
       "Bi ∥ AC (occulta)",
       "i = Bi ∩ perpendicolare in I"
      ],
      "evidenzia": []
     }
    },
    {
     "id": "L3-P41-Constr-p9",
     "la": "",
     "it": "Congiungi con una linea occulta Si, che tagli AC in λ, e completa il parallelogramma iIλμ.",
     "en": "Join the obscure line Si, cutting AC in [SVG 1169] , and complete the parallelogram iI [SVG 1170] .",
     "dipende_da": [],
     "figura": {
      "mostra": [
       "Si",
       "λ = Si ∩ AC",
       "μ (quarto vertice)"
      ],
      "evidenzia": [
       "iIλμ"
      ]
     }
    },
    {
     "id": "L3-P41-Constr-p10",
     "la": "",
     "it": "Prendi Iσ uguale a 3Iλ, e per il Sole S conduci la linea occulta σξ uguale a 3Sσ + 3Iλ.",
     "en": "Take [SVG 1171] equal to [SVG 1172] ; and through the sun S draw the obscure line [SVG 1173] equal to [SVG 1174] .",
     "dipende_da": [],
     "figura": {
      "mostra": [
       "σ sulla retta AC, con Iσ = 3Iλ",
       "ξ su σS prolungata"
      ],
      "evidenzia": [
       "σξ = 3Sσ + 3Iλ"
      ]
     },
     "nota": "Motte: «3Sσ + 3iλ» (i minuscola); vedi § A.9."
    },
    {
     "id": "L3-P41-Constr-p11",
     "la": "",
     "it": "Cancellate ora le lettere A, E, C, I, dal punto B verso il punto ξ conduci una nuova linea occulta BE, che stia alla precedente BE in rapporto duplicato della distanza BS rispetto alla quantità Sμ + iλ/3.",
     "en": "Then, cancelling the letters A, E, C, I, from the point B towards the point [SVG 1136] , draw the new obscure line BE, which may be to the former BE in the duplicate proportion of the distance BS to the quantity [SVG 1175] .",
     "dipende_da": [],
     "figura": {
      "mostra": [
       "nuova BE su Bξ"
      ],
      "evidenzia": [
       "BE₂ : BE₁ = BS² : (Sμ + iλ/3)²"
      ]
     }
    },
    {
     "id": "L3-P41-Constr-p12",
     "la": "",
     "it": "E per il punto E conduci di nuovo la retta AEC con la stessa regola di prima, cioè in modo che le sue parti AE ed EC stiano fra loro come i tempi V e W fra le osservazioni.",
     "en": "And through the point E draw again the right line AEC by the same rule as before; that is, so as its parts AE and EC may be one to the other as the times V and W between the observations.",
     "dipende_da": [],
     "figura": {
      "mostra": [
       "nuova AEC"
      ],
      "evidenzia": [
       "AE : EC = V : W"
      ]
     }
    },
    {
     "id": "L3-P41-Constr-p13",
     "la": "",
     "it": "E A e C saranno i luoghi della cometa con maggiore precisione.",
     "en": "Thus A and C will be the places of the comet more accurately.",
     "dipende_da": [],
     "figura": {
      "mostra": [
       "A, C corretti"
      ],
      "evidenzia": []
     }
    },
    {
     "id": "L3-P41-Constr-p14",
     "la": "",
     "it": "Su AC, divisa a metà in I, s’innalzino le perpendicolari AM, CN, IO, delle quali AM e CN siano le tangenti delle latitudini nella prima e nella terza osservazione, riferite ai raggi TA e τC.",
     "en": "Upon AC, bisected in I, erect the perpendiculars AM, CN, IO, of which AM and CN may be the tangents of the latitudes in the first and third observations, to the radii TA and [SVG 1167] .",
     "dipende_da": [],
     "figura": {
      "mostra": [
       "AM ⊥ AC, CN ⊥ AC, IO ⊥ AC"
      ],
      "evidenzia": [
       "AM = TA·tan β₁, CN = τC·tan β₃"
      ]
     }
    },
    {
     "id": "L3-P41-Constr-p15",
     "la": "",
     "it": "Si congiunga MN, che tagli IO in O.",
     "en": "Join MN, cutting IO in O.",
     "dipende_da": [],
     "figura": {
      "mostra": [
       "MN",
       "O = MN ∩ IO"
      ],
      "evidenzia": []
     }
    },
    {
     "id": "L3-P41-Constr-p16",
     "la": "",
     "it": "Si costruisca come prima il rettangolo iIλμ.",
     "en": "Draw the rectangular parallelogram [SVG 1176] , as before.",
     "dipende_da": [],
     "figura": {
      "mostra": [
       "rettangolo iIλμ"
      ],
      "evidenzia": []
     }
    },
    {
     "id": "L3-P41-Constr-p17",
     "la": "",
     "it": "Su IA prolungata si prenda ID uguale a Sμ + 2iλ/3.",
     "en": "In IA produced take ID equal to [SVG 1177] .",
     "dipende_da": [],
     "figura": {
      "mostra": [
       "D su IA prolungata"
      ],
      "evidenzia": [
       "ID = Sμ + 2iλ/3"
      ]
     }
    },
    {
     "id": "L3-P41-Constr-p18",
     "la": "",
     "it": "Poi su MN, verso N, si prenda MP, che stia alla lunghezza X trovata sopra in rapporto subduplicato della distanza media della Terra dal Sole (ossia del semidiametro dell’orbe magno) rispetto alla distanza OD.",
     "en": "Then in MN, towards N, take MP, which may be to the above found length X in the subduplicate proportion of the mean distance of the earth from the sun (or of the semi-diameter of the orbis magnus) to the distance OD.",
     "dipende_da": [],
     "figura": {
      "mostra": [
       "P su MN"
      ],
      "evidenzia": [
       "MP : X = √(distanza media) : √OD"
      ]
     }
    },
    {
     "id": "L3-P41-Constr-p19",
     "la": "",
     "it": "Se il punto P cade nel punto N, A, B, C saranno tre luoghi della cometa per i quali si deve descrivere la sua orbita nel piano dell’eclittica.",
     "en": "If the point P fall upon the point N; A, B, and C, will be three places of the comet, through which its orbit is to be described in the plane of the ecliptic.",
     "dipende_da": [],
     "figura": {
      "mostra": [],
      "evidenzia": [
       "P ≡ N: B è il luogo vero"
      ]
     }
    },
    {
     "id": "L3-P41-Constr-p20",
     "la": "",
     "it": "Se invece il punto P non cade nel punto N, sulla retta AC si prenda CG uguale a NP, in modo che i punti G e P giacciano dalla stessa parte della retta NC.",
     "en": "But if the point P falls not upon the point N, in the right line AC take CG equal to NP, so as the points G and P may lie on the same side of the line NC.",
     "dipende_da": [],
     "figura": {
      "mostra": [
       "G su AC con CG = NP"
      ],
      "evidenzia": [
       "G e P dalla stessa parte di NC"
      ]
     }
    },
    {
     "id": "L3-P41-Constr-p21",
     "la": "",
     "it": "Con lo stesso metodo con cui i punti E, A, C, G sono stati trovati dal punto assunto B, dagli altri punti b e β, assunti a piacere, si trovino i nuovi punti e, a, c, g ed ε, α, κ, γ.",
     "en": "By the same method as the points E, A, C, G, were found from the assumed point B, from other points b and [SVG 1052] assumed at pleasure, find out the new points e, a, c, g; and [SVG 925] , [SVG 1178] , [SVG 1179] , [SVG 1169] .",
     "dipende_da": [],
     "figura": {
      "mostra": [
       "b, β su tB",
       "e, a, c, g",
       "ε, α, κ, γ"
      ],
      "evidenzia": []
     },
     "nota": "La trascrizione ha «ε, α κ, γ» (virgola mancante); Motte ha λ al posto di γ (§ A.9)."
    },
    {
     "id": "L3-P41-Constr-p22",
     "la": "",
     "it": "Poi, se per G, g, γ si conduce la circonferenza di cerchio Ggγ, che tagli la retta τC in Z, Z sarà un luogo della cometa nel piano dell’eclittica.",
     "en": "Then through G, g, and [SVG 1169] , draw the circumference of a circle [SVG 1180] , cutting the right line [SVG 1167] in Z: and Z will be one place of the comet in the plane of the ecliptic.",
     "dipende_da": [],
     "figura": {
      "mostra": [
       "cerchio Ggγ",
       "Z = cerchio ∩ τC"
      ],
      "evidenzia": []
     }
    },
    {
     "id": "L3-P41-Constr-p23",
     "la": "",
     "it": "E se su AC, ac, ακ si prendono AF, af, αφ uguali rispettivamente a CG, cg, κγ, e per i punti F, f, φ si conduce la circonferenza di cerchio Ffφ, che tagli la retta AT in X, il punto X sarà un altro luogo della cometa nel piano dell’eclittica.",
     "en": "And in AC, ac, [SVG 1181] , making AF, af, [SVG 1182] , equal respectively to CG, cg, [SVG 1183] ; through the points F, f, and [SVG 1184] , draw the circumference of a circle [SVG 1185] , cutting the right line AT in X; and the point X will be another place of the comet in the plane of the ecliptic.",
     "dipende_da": [],
     "figura": {
      "mostra": [
       "F, f, φ",
       "cerchio Ffφ",
       "X = cerchio ∩ AT"
      ],
      "evidenzia": []
     }
    },
    {
     "id": "L3-P41-Constr-p24",
     "la": "",
     "it": "Nei punti X e Z s’innalzino le tangenti delle latitudini della cometa riferite ai raggi TX e τZ, e si avranno due luoghi della cometa nella sua propria orbita.",
     "en": "And at the points X and Z, erecting the tangents of the latitudes of the comet to the radii TX and [SVG 1186] , two places of the comet in its own orbit will be determined.",
     "dipende_da": [],
     "figura": {
      "mostra": [
       "perpendicolari al piano dell’eclittica in X e Z"
      ],
      "evidenzia": [
       "altezze TX·tan β₁, τZ·tan β₃"
      ]
     }
    },
    {
     "id": "L3-P41-Constr-p25",
     "la": "",
     "it": "Infine (per la Prop. XIX del Libro I) con fuoco S si descriva per quei due luoghi una parabola: questa sarà la traiettoria della cometa. C.V.T.",
     "en": "Lastly, if (by Prop. XIX., Book I) to the focus S a parabola is described passing through those two places, this parabola will be the orbit of the comet. Q.E.I.",
     "dipende_da": [
      "Prop. XIX del Libro I"
     ],
     "figura": {
      "mostra": [
       "parabola di fuoco S per i due luoghi"
      ],
      "evidenzia": []
     }
    },
    {
     "id": "L3-P41-Constr-p26",
     "la": "",
     "it": "La dimostrazione di questa costruzione segue dai lemmi: infatti la retta AC è tagliata in E nel rapporto dei tempi per il Lemma VII, come deve essere per il Lemma VIII; BE, per il Lemma XI, è la parte della retta BS, o Bξ, compresa nel piano dell’eclittica fra l’arco ABC e la corda AEC; e MP (per il Cor. del Lemma X) è la lunghezza della corda dell’arco che la cometa deve descrivere nella sua propria orbita fra la prima e la terza osservazione, e perciò sarà uguale a MN, purché B sia il vero luogo della cometa nel piano dell’eclittica.",
     "en": "The demonstration of this construction follows from the preceding Lemmas, because the right line AC is cut in E in the proportion of the times, by Lem. VII, as it ought to be, by Lem. VIII.; and BE, by Lem. XI., is a portion of the right line BS or [SVG 1187] in the plane of the ecliptic, intercepted between the arc ABC and the chord AEC; and MP (by Cor. Lem. X.) is the length of the chord of that arc, which the comet should describe in its proper orbit between the first and third observation, and therefore is equal to MN, providing B is a true place of the comet in the plane of the ecliptic.",
     "dipende_da": [
      "Lemma VII",
      "Lemma VIII",
      "Lemma XI",
      "Lemma X, Cor."
     ],
     "figura": {
      "mostra": [
       "arco ABC",
       "corda AEC"
      ],
      "evidenzia": [
       "BE = saetta fra arco e corda",
       "MP = MN se B è vero"
      ]
     }
    },
    {
     "id": "L3-P41-Constr-p27",
     "la": "",
     "it": "Del resto conviene scegliere i punti B, b, β non a caso, ma vicinissimi al vero.",
     "en": "But it will be convenient to assume the points B, b, [SVG 1052] , not at random, but nearly true.",
     "dipende_da": [],
     "figura": {
      "mostra": [],
      "evidenzia": []
     }
    },
    {
     "id": "L3-P41-Constr-p28",
     "la": "",
     "it": "Se è noto approssimativamente l’angolo AQt sotto cui la traccia dell’orbita descritta nel piano dell’eclittica taglia la retta tB, si dovrà condurre sotto quell’angolo la linea occulta AC, che stia a 4Tτ/3 in rapporto subduplicato di SQ a St.",
     "en": "If the angle AQt, at which the projection of the orbit in the plane of the ecliptic cuts the right line tB, is rudely known, at that angle with Bt draw the obscure line AC, which may be to [SVG 1188] in the subduplicate proportion of SQ to St",
     "dipende_da": [],
     "figura": {
      "mostra": [
       "Q = traccia dell’orbita ∩ tB",
       "AC occulta sotto l’angolo AQt"
      ],
      "evidenzia": [
       "AC : (4/3)Tτ = √SQ : √St"
      ]
     },
     "nota": "Motte aggiunge «with Bt»."
    },
    {
     "id": "L3-P41-Constr-p29",
     "la": "",
     "it": "E conducendo la retta SEB, la cui parte EB sia uguale alla lunghezza Vt, si determinerà il punto B, che si può usare la prima volta.",
     "en": "and, drawing the right line SEB so as its part EB may be equal to the length Vt, the point B will be determined, which we are to use for the first time.",
     "dipende_da": [],
     "figura": {
      "mostra": [
       "SEB con EB = Vt"
      ],
      "evidenzia": []
     }
    },
    {
     "id": "L3-P41-Constr-p30",
     "la": "",
     "it": "Poi, cancellata la retta AC e condotta di nuovo secondo la costruzione precedente, e trovata inoltre la lunghezza MP, si prenda su tB il punto b con questa regola: se TA e τC si tagliano a vicenda in Y, la distanza Yb stia alla distanza YB nel rapporto composto dal rapporto di MP a MN e dal rapporto subduplicato di SB a Sb.",
     "en": "Then, cancelling the right line AC, and drawing anew AC according to the preceding construction, and, moreover, finding the length MP, in tB take the point b, by this rule, that, if TA and [SVG 1189] intersect each other in Y, the distance Yb may be to the distance YB in a proportion compounded of the proportion of MP to MN, and the subduplicate proportion of SB to Sb.",
     "dipende_da": [],
     "figura": {
      "mostra": [
       "Y = TA ∩ τC",
       "b su tB"
      ],
      "evidenzia": [
       "Yb : YB = (MP : MN)·√(SB : Sb)"
      ]
     }
    },
    {
     "id": "L3-P41-Constr-p31",
     "la": "",
     "it": "E con lo stesso metodo si dovrà trovare il terzo punto β, se si vuole ripetere l’operazione una terza volta.",
     "en": "And by the same method you may find the third point [SVG 1052] , if you please to repeat the operation the third time",
     "dipende_da": [],
     "figura": {
      "mostra": [
       "β"
      ],
      "evidenzia": []
     }
    },
    {
     "id": "L3-P41-Constr-p32",
     "la": "",
     "it": "Ma con questo metodo per lo più basteranno due operazioni.",
     "en": "but if this method is followed, two operations generally will be sufficient",
     "dipende_da": [],
     "figura": {
      "mostra": [],
      "evidenzia": []
     }
    },
    {
     "id": "L3-P41-Constr-p33",
     "la": "",
     "it": "Infatti, se la distanza Bb risulta piccolissima, trovati i punti F, f e G, g, le rette Ff e Gg, una volta condotte, taglieranno TA e τC nei punti cercati X e Z.",
     "en": "for if the distance Bb happens to be very small, after the points F, f, and G, g, are found, draw the right lines Ff and Gg, and they will cut TA and [SVG 1167] in the points required, X and Z.",
     "dipende_da": [],
     "figura": {
      "mostra": [
       "rette Ff, Gg"
      ],
      "evidenzia": [
       "X = Ff ∩ TA, Z = Gg ∩ τC"
      ]
     }
    }
   ]
  },
  {
   "id": "L3-P41-Ex",
   "tipo": "Exemplum (calcolo)",
   "titolo": "Prop. XLI, Esempio — la cometa del 1680: orbita di Newton, orbite di Halley, confronto con le osservazioni",
   "copertura": [
    "III.G7.10",
    "III.G7.11",
    "III.G7.12",
    "III.G7.13",
    "III.G7.14",
    "III.G7.15",
    "III.G7.16",
    "III.G7.17",
    "III.G7.18",
    "III.G7.19",
    "III.G7.20",
    "III.G7.21",
    "III.G7.22",
    "III.G7.23",
    "III.G7.24",
    "III.G7.25",
    "III.G7.26",
    "III.G7.27",
    "III.G7.28",
    "III.G7.29",
    "III.G7.30",
    "III.G7.31",
    "III.G7.32",
    "III.G7.33",
    "III.G7.34",
    "III.G7.35",
    "III.G7.36",
    "III.G7.37",
    "III.G7.38",
    "III.G7.39",
    "III.G7.40",
    "III.G7.41",
    "III.G7.42",
    "III.G7.43",
    "III.G7.44",
    "III.G7.45",
    "III.G7.46",
    "III.G7.47",
    "III.G7.48",
    "III.G7.49",
    "III.G7.50"
   ],
   "fonti": {
    "la": "",
    "en": "Motte 1846, sezione corrispondente (Book III, Prop. XLI, Example)"
   },
   "enunciato": {
    "la": "",
    "it": "Si proponga la cometa dell’anno 1680.",
    "en": "Let the comet of the year 1680 be proposed."
   },
   "nota": "Passi soltanto per i capoversi di calcolo e di conclusione (III.G7.28, 29, 31, 38, 40, 50); le osservazioni dei capoversi III.G7.10–27 e 33–37, 41–49 sono coperte da «copertura» senza passi; i valori delle sei tabelle e i controlli sono nel campo «dati».",
   "passi": [
    {
     "id": "L3-P41-Ex-p1",
     "la": "",
     "it": "Ora, per determinare l’orbita della cometa, fra le osservazioni descritte fin qui ne ho scelte tre, quelle che Flamsteed fece il 21 dicembre, il 5 gennaio e il 25 gennaio.",
     "en": "Now, in order to determine the orbit of the comet out of the observations above described, I selected those three which Flamsted made, Dec. 21, Jan. 5, and Jan. 25",
     "dipende_da": [],
     "figura": {
      "mostra": [
       "T, t, τ = Terra al 21 dic., 5 gen., 25 gen."
      ],
      "evidenzia": []
     }
    },
    {
     "id": "L3-P41-Ex-p2",
     "la": "",
     "it": "Da queste ho trovato St di 9842,1 parti e Vt di 455, di quelle parti di cui il semidiametro dell’orbe magno ne contiene 10000.",
     "en": "from which I found St of 9842,1 parts, and Vt of 455, such as the semi-diameter of the orbis magnus contains 10000.",
     "dipende_da": [],
     "figura": {
      "mostra": [
       "St",
       "tV"
      ],
      "evidenzia": []
     },
     "nota": "Verifica in N3: tV ≈ 463 con un’orbita circolare di raggio St."
    },
    {
     "id": "L3-P41-Ex-p3",
     "la": "",
     "it": "Poi, per la prima operazione, assumendo tB di 5657 parti, ho trovato SB 9747, BE la prima volta 412, Sμ 9503, iλ 413; BE la seconda volta 421, OD 10186, X 8528,4, MP 8450, MN 8475, NP 25.",
     "en": "Then for the first observation, assuming tB of 5657 of those parts, I found SB 9747, BE for the first time 412, [SVG 1157] 9503, [SVG 1248] 413, BE for the second time 421, OD 10186, X 8528,4, PM 8450, MN 8475, NP 25",
     "dipende_da": [],
     "figura": {
      "mostra": [
       "B",
       "E",
       "μ",
       "λ",
       "O",
       "D",
       "P",
       "N"
      ],
      "evidenzia": [
       "NP = MN − MP = 25"
      ]
     },
     "nota": "Motte: «for the first observation» (latino: operazione) e «PM» per MP. Controlli in N3."
    },
    {
     "id": "L3-P41-Ex-p4",
     "la": "",
     "it": "Di qui, per la seconda operazione, ho ricavato la distanza tb di 5640.",
     "en": "from whence, by the second operation, I collected the distance tb 5640",
     "dipende_da": [],
     "figura": {
      "mostra": [
       "b su tB"
      ],
      "evidenzia": []
     }
    },
    {
     "id": "L3-P41-Ex-p5",
     "la": "",
     "it": "E con questa operazione ho trovato infine le distanze TX di 4775 e τZ di 11322.",
     "en": "and by this operation I at last deduced the distances TX 4775 and [SVG 1186] 11322.",
     "dipende_da": [],
     "figura": {
      "mostra": [
       "X su TA",
       "Z su τC"
      ],
      "evidenzia": []
     }
    },
    {
     "id": "L3-P41-Ex-p6",
     "la": "",
     "it": "Definendo l’orbita a partire da queste, ho trovato il suo nodo discendente in ♋ e l’ascendente in ♑ 1° 53′; l’inclinazione del suo piano sul piano dell’eclittica 61° 20⅓′; che il suo vertice (ossia il perielio della cometa) dista dal nodo 8° 38′ ed è in ♐ 27° 43′ con latitudine australe 7° 34′; che il suo lato retto è 236,8 e che l’area descritta ogni giorno dal raggio condotto al Sole è 93585, posto il quadrato del semidiametro dell’orbe magno uguale a 100000000; e che la cometa in questa orbita ha proceduto secondo l’ordine dei segni e l’8 dicembre, a 0h 4′ p. m., è stata nel vertice dell’orbita, ossia nel perielio.",
     "en": "From which, limiting the orbit, I found its descending node in ♋, and ascending node in ♑ 1° 53'; the inclination of its plane to the plane of the ecliptic 61° 20 [SVG 1249] , the vertex thereof (or the perihelion of the comet) distant from the node 8° 38', and in ♐ 27° 43', with latitude 7° 34' south; its latus rectum 236,8; and the diurnal area described by a radius drawn to the sun 93585, supposing the square of the semi-diameter of the orbis magnus 100000000; that the comet in this orbit moved directly according to the order of the signs, and on Dec. 8d. 00h. 04' P. M. was in the vertex or perihelion of its orbit.",
     "dipende_da": [],
     "figura": {
      "mostra": [
       "parabola di fuoco S",
       "linea dei nodi",
       "perielio"
      ],
      "evidenzia": []
     },
     "nota": "Coerenza degli elementi verificata in N4 (perielio ♐ 27° 43′, lat. 7° 34′ australe; area diurna 93590)."
    },
    {
     "id": "L3-P41-Ex-p7",
     "la": "",
     "it": "Tutto ciò l’ho determinato graficamente, con una scala di parti uguali e con le corde degli angoli ricavate dalla tavola dei seni naturali, costruendo una figura abbastanza ampia, nella quale cioè il semidiametro dell’orbe magno (di 1000 parti) era uguale a 16⅓ pollici del piede inglese.",
     "en": "All which I determined by scale and compass, and the chords of angles, taken from the table of natural sines, in a pretty large figure, in which, to wit, the radius of the orbis magnus (consisting of 10000 parts) was equal to [SVG 1250] inches of an English foot.",
     "dipende_da": [],
     "figura": {
      "mostra": [],
      "evidenzia": []
     },
     "nota": "La trascrizione ha «partium 1000», Motte «10000 parts»: § A.7."
    },
    {
     "id": "L3-P41-Ex-p8",
     "la": "",
     "it": "Infine, perché risultasse se la cometa si muovesse davvero nell’orbita così trovata, ho ricavato, con operazioni in parte aritmetiche e in parte grafiche, i luoghi della cometa in questa orbita per i tempi di alcune osservazioni, come si può vedere nella tabella seguente.",
     "en": "Lastly, in order to discover whether the comet did truly move in the orbit so determined, I investigated its places in this orbit partly by arithmetical operations, and partly by scale and compass, to the times of some of the observations, as may be seen in the following table",
     "dipende_da": [],
     "figura": {
      "mostra": [],
      "evidenzia": []
     }
    },
    {
     "id": "L3-P41-Ex-p9",
     "la": "",
     "it": "In seguito il nostro Halley ha determinato l’orbita con un calcolo aritmetico, con maggiore precisione di quanto fosse possibile tracciando linee; e ha conservato il luogo dei nodi in ♋ e ♑ 1° 53′, l’inclinazione del piano dell’orbita sull’eclittica di 61° 20⅓′ e il tempo del perielio della cometa, 8 dicembre, 0h 4′; ha trovato invece che la distanza del perielio dal nodo ascendente, misurata nell’orbita della cometa, è di 9° 20′, e che il lato retto della parabola è di 2430 parti, essendo la distanza media del Sole dalla Terra di 100000 parti.",
     "en": "But afterwards Dr. Halley did determine the orbit to a greater accuracy by an arithmetical calculus than could be done by linear descriptions; and, retaining the place of the nodes in ♋ and ♑ 1° 53' and the inclination of the plane of the orbit to the ecliptic 61° [SVG 1252] , as well as the time of the comet's being in perihelion, Dec. 8d. 00h. 04' he found the distance of the perihelion from the ascending node measured in the comet's orbit 9° 20', and the latus rectum of the parabola 2430 parts, supposing the mean distance of the sun from the earth to be 100000 parts",
     "dipende_da": [],
     "figura": {
      "mostra": [],
      "evidenzia": []
     }
    },
    {
     "id": "L3-P41-Ex-p10",
     "la": "",
     "it": "E da questi dati, impostato con cura un calcolo anch’esso aritmetico, ha calcolato i luoghi della cometa per i tempi delle osservazioni, come segue.",
     "en": "and from these data, by an accurate arithmetical calculus, he computed the places of the comet to the times of the observations as follows",
     "dipende_da": [],
     "figura": {
      "mostra": [],
      "evidenzia": []
     }
    },
    {
     "id": "L3-P41-Ex-p11",
     "la": "",
     "it": "Inoltre Halley, osservando che una cometa insigne era apparsa quattro volte a intervalli di 575 anni, cioè nel mese di settembre dopo l’uccisione di Giulio Cesare, nell’anno di Cristo 531 sotto il consolato di Lampadio e Oreste, nell’anno di Cristo 1106 nel mese di febbraio e verso la fine dell’anno 1680, e ogni volta con una coda lunga e insigne (salvo che alla morte di Cesare la coda era apparsa meno, per la posizione sfavorevole della Terra), ha cercato un’orbita ellittica il cui asse maggiore fosse di 1382957 parti, essendo la distanza media della Terra dal Sole di 10000 parti: un’orbita, cioè, nella quale la cometa potesse compiere la sua rivoluzione in 575 anni.",
     "en": "Moreover, Dr. Halley, observing that a remarkable comet had appeared four times at equal intervals of 575 years (that is, in the month of September after Julius Cæsar was killed; An. Chr. 531, in the consulate of Lampadius and Orestes; An. Chr. 1106, in the month of February; and at the end of the year 1680; and that with a long and remarkable tail, except when it was seen after Cæsar's death, at which time, by reason of the inconvenient situation of the earth, the tail was not so conspicuous), set himself to find out an elliptic orbit whose greater axis should be 1382957 parts, the mean distance of the earth from the sun containing 10000 such; in which orbit a comet might revolve in 575 years",
     "dipende_da": [],
     "figura": {
      "mostra": [],
      "evidenzia": []
     },
     "nota": "Verifica in N5: (1382957/20000)^(3/2) = 575,0 anni."
    },
    {
     "id": "L3-P41-Ex-p12",
     "la": "",
     "it": "E ponendo il nodo ascendente in ♋ 2° 2′, l’inclinazione del piano dell’orbita sul piano dell’eclittica di 61° 6′ 48″, il perielio della cometa in questo piano in ♐ 22° 44′ 25″, il tempo equato del perielio 7 dicembre, 23h 9′, la distanza del perielio dal nodo ascendente nel piano dell’eclittica di 9° 17′ 35″ e l’asse coniugato di 18481,2, ha calcolato il moto della cometa in questa orbita ellittica.",
     "en": "and, placing the ascending node in ♋ 2° 2', the inclination of the plane of the orbit to the plane of the ecliptic in an angle of 61° 6' 48'', the perihelion of the comet in this plane in ♐ 22° 44' 25'', the equal time of the perihelion December 7d. 23h. 9', the distance of the perihelion from the ascending node in the plane of the ecliptic 9° 17' 35'', and its conjugate axis 18481,2, he computed the motions of the comet in this elliptic orbit.",
     "dipende_da": [],
     "figura": {
      "mostra": [],
      "evidenzia": []
     },
     "nota": "Sul nodo «ascendente in ♋» e sul piano in cui si misura 9° 17′ 35″: N5 e § A.7."
    },
    {
     "id": "L3-P41-Ex-p13",
     "la": "",
     "it": "I luoghi della cometa, sia dedotti dalle osservazioni sia calcolati in questa orbita, sono presentati nella tabella seguente.",
     "en": "The places of the comet, as deduced from the observations, and as arising from computation made in this orbit, may be seen in the following table.",
     "dipende_da": [],
     "figura": {
      "mostra": [],
      "evidenzia": []
     }
    },
    {
     "id": "L3-P41-Ex-p14",
     "la": "",
     "it": "Le osservazioni di questa cometa, dal principio alla fine, concordano con il moto della cometa nell’orbita ora descritta non meno di quanto i moti dei pianeti sogliano concordare con le loro teorie; e, concordando, provano che fu una sola e medesima cometa quella che apparve per tutto questo tempo, e che la sua orbita è stata qui definita correttamente.",
     "en": "The observations of this comet from the beginning to the end agree as perfectly with the motion of the comet in the orbit just now described as the motions of the planets do with the theories from whence they are calculated; and by this agreement plainly evince that it was one and the same comet that appeared all that time, and also that the orbit of that comet is here rightly defined.",
     "dipende_da": [],
     "figura": {
      "mostra": [],
      "evidenzia": []
     }
    },
    {
     "id": "L3-P41-Ex-p15",
     "la": "",
     "it": "Queste osservazioni, dunque, concordano con la teoria nella misura in cui concordano fra loro, e concordando provano che fu una sola e medesima cometa quella che apparve per tutto il tempo dal quattro novembre fino al nove marzo.",
     "en": "From all this it is plain that these observations agree with the theory, so far as they agree with one another; and by this agreement it is made clear that it was one and the same comet that appeared all the time from Nov. 4 to Mar. 9.",
     "dipende_da": [],
     "figura": {
      "mostra": [],
      "evidenzia": []
     }
    },
    {
     "id": "L3-P41-Ex-p16",
     "la": "",
     "it": "La traiettoria di questa cometa tagliò due volte il piano dell’eclittica, e perciò non fu rettilinea.",
     "en": "The path of this comet did twice cut the plane of the ecliptic, and therefore was not a right line.",
     "dipende_da": [],
     "figura": {
      "mostra": [
       "cammino apparente sulla sfera",
       "eclittica"
      ],
      "evidenzia": [
       "due intersezioni con l’eclittica"
      ]
     },
     "nota": "«Trajectoria» qui è il cammino apparente sulla sfera celeste: nota N7."
    },
    {
     "id": "L3-P41-Ex-p17",
     "la": "",
     "it": "Tagliò l’eclittica non in parti opposte del cielo, ma alla fine della Vergine e al principio del Capricorno, a un intervallo di circa 98 gradi; quindi il corso della cometa deviava moltissimo da un cerchio massimo.",
     "en": "It did cut the ecliptic not in opposite parts of the heavens, but in the end of Virgo and beginning of Capricorn, including an arc of about 98°; and therefore the way of the comet did very much deviate from the path of a great circle",
     "dipende_da": [],
     "figura": {
      "mostra": [
       "intersezioni a fine ♍ e inizio ♑"
      ],
      "evidenzia": [
       "arco di circa 98° (non 180°)"
      ]
     },
     "nota": "Verifica in N7."
    },
    {
     "id": "L3-P41-Ex-p18",
     "la": "",
     "it": "Infatti nel mese di novembre il suo corso declinava dall’eclittica verso sud di almeno tre gradi, e poi nel mese di dicembre piegava dall’eclittica verso nord di 29 gradi, e le due parti dell’orbita in cui la cometa tendeva verso il Sole e tornava dal Sole declinavano l’una dall’altra di un angolo apparente di più di trenta gradi, come osservò Montanari.",
     "en": "for in the month of Nov. it declined at least 3° from the ecliptic towards the south; and in the month of Dec. following it declined 29° from the ecliptic towards the north; the two parts of the orbit in which the comet descended towards the sun, and ascended again from the sun, declining one from the other by an apparent angle of above 30°, as observed by Montenari.",
     "dipende_da": [],
     "figura": {
      "mostra": [
       "ramo di novembre (sud)",
       "ramo di dicembre (nord)"
      ],
      "evidenzia": []
     }
    },
    {
     "id": "L3-P41-Ex-p19",
     "la": "",
     "it": "Questa cometa procedeva per nove segni, cioè dall’ultimo grado del Leone al principio dei Gemelli, oltre al segno del Leone, per il quale procedeva prima che si cominciasse a vederla; e non esiste alcun’altra teoria per cui una cometa percorra con moto regolare una parte così grande del cielo.",
     "en": "This comet travelled over 9 signs, to wit, from the last deg. of ♌ to the beginning of ♊, beside the sign of ♌, through which it passed before it began to be seen; and there is no other theory by which a comet can go over so great a part of the heavens with a regular motion.",
     "dipende_da": [],
     "figura": {
      "mostra": [
       "da ♌ 29° a ♊ 0°"
      ],
      "evidenzia": [
       "circa 271° di longitudine"
      ]
     }
    },
    {
     "id": "L3-P41-Ex-p20",
     "la": "",
     "it": "Il suo moto fu estremamente disuguale.",
     "en": "The motion of this comet was very unequable",
     "dipende_da": [],
     "figura": {
      "mostra": [],
      "evidenzia": []
     }
    },
    {
     "id": "L3-P41-Ex-p21",
     "la": "",
     "it": "Infatti verso il ventesimo giorno di novembre descrisse circa cinque gradi al giorno; poi, rallentato il moto, fra il 26 novembre e il 12 dicembre, cioè nello spazio di quindici giorni e mezzo, descrisse soltanto 40 gradi; in seguito, accelerato di nuovo il moto, descrisse quasi cinque gradi al giorno, prima che il moto cominciasse di nuovo a rallentare.",
     "en": "for about the 20th of Nov. it described about 5° a day. Then its motion being retarded between Nov. 26 and Dec. 12, to wit, in the space of [SVG 863] days, it described only 40°. But the motion thereof being afterwards accelerated, it described near 5° a day, till its motion began to be again retarded.",
     "dipende_da": [],
     "figura": {
      "mostra": [],
      "evidenzia": []
     },
     "nota": "Verifica in N7 sui valori delle tabelle."
    },
    {
     "id": "L3-P41-Ex-p22",
     "la": "",
     "it": "E la teoria che corrisponde bene a un moto così disuguale per una parte grandissima del cielo, che osserva le stesse leggi della teoria dei pianeti e che concorda con precisione con osservazioni astronomiche precise, non può non essere vera.",
     "en": "And the theory which justly corresponds with a motion so unequable, and through so great a part of the heavens, which observes the same laws with the theory of the planets, and which accurately agrees with accurate astronomical observations, cannot be otherwise than true.",
     "dipende_da": [],
     "figura": {
      "mostra": [],
      "evidenzia": []
     }
    }
   ],
   "dati": {
    "tabella1_Flamsteed": {
     "colonne": [
      "data",
      "tempo apparente [h,m]",
      "tempo vero [h,m,s]",
      "longitudine Sole",
      "longitudine cometa",
      "latitudine boreale cometa"
     ],
     "righe": [
      [
       "1680. Dec. 12",
       [
        4.0,
        46.0
       ],
       [
        4,
        46,
        0
       ],
       "♑ 1.51.23",
       "♑ 6.32.30",
       "8.28.0"
      ],
      [
       "21",
       [
        6.0,
        32.5
       ],
       [
        6,
        36,
        59
       ],
       "11.6.44",
       "♒ 5.8.12",
       "21.42.13"
      ],
      [
       "24",
       [
        6.0,
        12.0
       ],
       [
        6,
        17,
        52
       ],
       "14.9.26",
       "18.49.23",
       "25.23.5"
      ],
      [
       "26",
       [
        5.0,
        14.0
       ],
       [
        5,
        20,
        44
       ],
       "16.9.22",
       "28.24.13",
       "27.0.52"
      ],
      [
       "29",
       [
        7.0,
        55.0
       ],
       [
        8,
        3,
        2
       ],
       "19.9.43",
       "♓ 13.10.41",
       "28.9.58"
      ],
      [
       "30",
       [
        8.0,
        2.0
       ],
       [
        8,
        10,
        26
       ],
       "20.21.9",
       "17.38.20",
       "28.11.53"
      ],
      [
       "1681 Jan. 5",
       [
        5.0,
        51.0
       ],
       [
        6,
        1,
        38
       ],
       "26.22.18",
       "♈ 8.48.53",
       "26.15.7"
      ],
      [
       "9",
       [
        6.0,
        49.0
       ],
       [
        7,
        0,
        53
       ],
       "♒ 0.29.2",
       "18.44.4",
       "24.11.56"
      ],
      [
       "10",
       [
        5.0,
        54.0
       ],
       [
        6,
        6,
        10
       ],
       "1.27.43",
       "20.40.50",
       "23.43.52"
      ],
      [
       "13",
       [
        6.0,
        56.0
       ],
       [
        7,
        8,
        55
       ],
       "4.33.20",
       "25.59.48",
       "22.17.28"
      ],
      [
       "25",
       [
        7.0,
        44.0
       ],
       [
        7,
        58,
        42
       ],
       "16.45.36",
       "♉ 9.35.0",
       "17.56.30"
      ],
      [
       "30",
       [
        8.0,
        7.0
       ],
       [
        8,
        21,
        53
       ],
       "21.49.58",
       "♉ 13.19.51",
       "16.42.18"
      ],
      [
       "Feb. 2",
       [
        6.0,
        20.0
       ],
       [
        6,
        34,
        51
       ],
       "24.46.59",
       "15.13.53",
       "16.4.1"
      ],
      [
       "5",
       [
        6.0,
        50.0
       ],
       [
        7,
        4,
        41
       ],
       "27.49.51",
       "16.59.6",
       "15.27.3"
      ]
     ],
     "controlli": "equazione del tempo (vero − apparente) da 0 a 14,9 min, regolare; moto del Sole 60,5′–61,2′ al giorno salvo 26→29 dic. (57,9′) e 29→30 dic. (71,1′): la longitudine del Sole del 29 dic. «19.9.43» va letta 19.19.43 (Motte)."
    },
    "tabella2_Newton": {
     "righe": [
      [
       "1681 Febr. 25",
       "08h.30′",
       "♉",
       "26°.18′.35″",
       "12°.46′.46″"
      ],
      [
       "27",
       "08°.15′",
       "",
       "27°.04′.30″",
       "12°.36′.12″"
      ],
      [
       "Mar. 1",
       "11°.00′",
       "",
       "27°.52′.42″",
       "12°.23′.40″"
      ],
      [
       "2",
       "08°.00′",
       "",
       "28°.12′.48″",
       "12°.19′.38″"
      ],
      [
       "5",
       "11°.30′",
       "",
       "29°.18′.00″",
       "12°.03′.16″"
      ],
      [
       "7",
       "09°.30′",
       "♊",
       "00°.04′.00″",
       "11°.57′.00″"
      ],
      [
       "9",
       "08°.30′",
       "",
       "00°.43′.04″",
       "11°.45′.52″"
      ]
     ]
    },
    "tabella3_fisse_Pound": {
     "righe": [
      [
       "A",
       "♉",
       [
        26,
        41,
        50
       ],
       [
        12,
        8,
        36
       ]
      ],
      [
       "L",
       "♉",
       [
        29,
        33,
        34
       ],
       [
        12,
        7,
        48
       ]
      ],
      [
       "B",
       "",
       [
        28,
        40,
        23
       ],
       [
        11,
        17,
        54
       ]
      ],
      [
       "M",
       "",
       [
        29,
        18,
        54
       ],
       [
        12,
        7,
        20
       ]
      ],
      [
       "C",
       "",
       [
        27,
        58,
        30
       ],
       [
        12,
        40,
        25
       ]
      ],
      [
       "N",
       "",
       [
        28,
        48,
        29
       ],
       [
        12,
        31,
        9
       ]
      ],
      [
       "E",
       "",
       [
        26,
        27,
        17
       ],
       [
        12,
        52,
        7
       ]
      ],
      [
       "Z",
       "",
       [
        29,
        44,
        48
       ],
       [
        11,
        57,
        13
       ]
      ],
      [
       "F",
       "",
       [
        28,
        28,
        37
       ],
       [
        11,
        52,
        22
       ]
      ],
      [
       "α",
       "",
       [
        29,
        52,
        3
       ],
       [
        11,
        55,
        48
       ]
      ],
      [
       "G",
       "",
       [
        26,
        56,
        8
       ],
       [
        12,
        4,
        58
       ]
      ],
      [
       "β",
       "♊",
       [
        0,
        8,
        23
       ],
       [
        11,
        48,
        56
       ]
      ],
      [
       "H",
       "",
       [
        27,
        11,
        45
       ],
       [
        12,
        2,
        1
       ]
      ],
      [
       "γ",
       "",
       [
        0,
        40,
        10
       ],
       [
        11,
        55,
        18
       ]
      ],
      [
       "I",
       "",
       [
        27,
        25,
        2
       ],
       [
        11,
        53,
        11
       ]
      ],
      [
       "δ",
       "",
       [
        1,
        3,
        20
       ],
       [
        11,
        30,
        42
       ]
      ],
      [
       "K",
       "",
       [
        27,
        42,
        7
       ],
       [
        11,
        53,
        26
       ]
      ]
     ],
     "controlli": "distanze fra le fisse ricalcolate dalle coordinate di Pound (scala AB = 80 7/12 parti → 1 parte ≈ 1,572′): 19 distanze, scarti ≤ 1,03 parti (AI); le coordinate latine di M e N tornano, quelle di Motte (M 9.18.54, 2.7.20; N 2.31.9) no."
    },
    "tabella4_Newton_orbita_grafica": {
     "colonne": [
      "data",
      "distanza dal Sole (R=10000)",
      "long. ricavata",
      "lat. ricavata",
      "long. osservata",
      "lat. osservata",
      "diff. long. (′)",
      "diff. lat. (′)"
     ],
     "righe": [
      [
       "Dec. 12",
       2792,
       [
        "♑",
        6,
        32
       ],
       [
        8,
        18.5
       ],
       [
        "♑",
        6,
        31.3333
       ],
       [
        8,
        26
       ],
       [
        1,
        1
       ],
       [
        -1,
        7.5
       ]
      ],
      [
       "29",
       8403,
       [
        "♓",
        13,
        13.6667
       ],
       [
        28,
        0
       ],
       [
        "♓",
        13,
        11.75
       ],
       [
        28,
        10.0833
       ],
       [
        1,
        2
       ],
       [
        -1,
        10.0833
       ]
      ],
      [
       "Febr. 5",
       16669,
       [
        "♉",
        17,
        0
       ],
       [
        15,
        29.6667
       ],
       [
        "♉",
        16,
        59.875
       ],
       [
        15,
        27.4
       ],
       [
        1,
        0
       ],
       [
        1,
        2.25
       ]
      ],
      [
       "Mar. 5",
       21737,
       [
        29,
        19.75
       ],
       [
        12,
        4
       ],
       [
        29,
        20.8571
       ],
       [
        12,
        3.5
       ],
       [
        -1,
        1
       ],
       [
        1,
        0.5
       ]
      ]
     ],
     "controlli": "differenze (ricavato − osservato) ricalcolate: +0,67/+1, +1,92/+2, +0,13/+0, −1,11/−1 in longitudine (arrotondate al primo); −7,50, −10,08, +2,27 (tab. +2¼), +0,50 in latitudine. Tutte tornano. Distanze ricalcolate con l’equazione di Barker (lato retto 236,8, perielio 8 dic. 0h 4′): 2804, 8404, 16669, 21622 contro 2792, 8403, 16669, 21737."
    },
    "tabella5_Halley_parabola": {
     "colonne": [
      "tempo vero",
      "distanza dal Sole (R=100000)",
      "long. calcolata",
      "lat. calcolata",
      "errore long. [segno,′,″]",
      "errore lat. [segno,′,″]"
     ],
     "righe": [
      [
       "Dec. 12. 4. 46 01",
       28028,
       [
        "♑",
        6,
        29,
        25
       ],
       [
        8,
        26,
        0
       ],
       [
        -1,
        3,
        5
       ],
       [
        -1,
        2,
        0
       ]
      ],
      [
       "21. 6. 37 01",
       61076,
       [
        "♒",
        5,
        6,
        30
       ],
       [
        21,
        43,
        20
       ],
       [
        -1,
        1,
        42
       ],
       [
        1,
        1,
        7
       ]
      ],
      [
       "24. 6. 18 01",
       70008,
       [
        18,
        48,
        20
       ],
       [
        25,
        22,
        40
       ],
       [
        -1,
        1,
        3
       ],
       [
        -1,
        0,
        25
       ]
      ],
      [
       "26. 5. 21 01",
       75576,
       [
        28,
        22,
        45
       ],
       [
        27,
        1,
        36
       ],
       [
        -1,
        1,
        28
       ],
       [
        1,
        0,
        44
       ]
      ],
      [
       "29. 8. 3 01",
       14021,
       [
        "♓",
        13,
        12,
        40
       ],
       [
        28,
        10,
        10
       ],
       [
        1,
        1,
        59
       ],
       [
        1,
        0,
        12
       ]
      ],
      [
       "30. 8. 10 01",
       86661,
       [
        17,
        40,
        5
       ],
       [
        28,
        11,
        20
       ],
       [
        1,
        1,
        45
       ],
       [
        1,
        0,
        33
       ]
      ],
      [
       "Jan. 5. 6. 1 12",
       101440,
       [
        "♈",
        8,
        49,
        49
       ],
       [
        26,
        15,
        15
       ],
       [
        1,
        0,
        56
       ],
       [
        1,
        0,
        8
       ]
      ],
      [
       "9. 7. 0 01",
       110959,
       [
        18,
        44,
        36
       ],
       [
        24,
        12,
        54
       ],
       [
        1,
        0,
        32
       ],
       [
        1,
        0,
        58
       ]
      ],
      [
       "10. 6. 6 01",
       113162,
       [
        20,
        41,
        0
       ],
       [
        23,
        44,
        10
       ],
       [
        1,
        0,
        10
       ],
       [
        1,
        0,
        18
       ]
      ],
      [
       "13. 7. 9 01",
       120000,
       [
        26,
        0,
        21
       ],
       [
        22,
        17,
        30
       ],
       [
        1,
        0,
        33
       ],
       [
        1,
        0,
        2
       ]
      ],
      [
       "25. 7. 59 01",
       145370,
       [
        "♉",
        9,
        33,
        40
       ],
       [
        17,
        57,
        55
       ],
       [
        -1,
        1,
        20
       ],
       [
        1,
        1,
        25
       ]
      ],
      [
       "30. 8. 22 01",
       155303,
       [
        13,
        17,
        41
       ],
       [
        16,
        42,
        7
       ],
       [
        -1,
        2,
        10
       ],
       [
        -1,
        0,
        11
       ]
      ],
      [
       "Feb. 2. 6. 35 01",
       160951,
       [
        15,
        11,
        11
       ],
       [
        16,
        4,
        15
       ],
       [
        -1,
        2,
        42
       ],
       [
        1,
        0,
        14
       ]
      ],
      [
       "5. 7. 4 12",
       166686,
       [
        16,
        58,
        25
       ],
       [
        15,
        29,
        13
       ],
       [
        -1,
        0,
        41
       ],
       [
        1,
        2,
        10
       ]
      ],
      [
       "25. 8. 41 01",
       202570,
       [
        26,
        15,
        46
       ],
       [
        12,
        48,
        0
       ],
       [
        -1,
        2,
        49
       ],
       [
        1,
        1,
        14
       ]
      ],
      [
       "Mar. 5. 11. 39 01",
       216205,
       [
        29,
        18,
        35
       ],
       [
        12,
        5,
        40
       ],
       [
        1,
        0,
        35
       ],
       [
        1,
        2,
        24
       ]
      ]
     ],
     "controlli": "errori = calcolato − osservato (osservati dalle tabelle 1 e 2): 31 su 32 tornano al secondo; 30 dic., errore in latitudine: calcolato −0′33″, tabella +0′33″ (Motte −0.33). Distanze ricalcolate con l’equazione di Barker (q = 0,006075): accordo entro 0,01% salvo 29 dic.: 14021 nella trascrizione, 84020 calcolato (Motte 84021)."
    },
    "tabella6_Halley_ellisse": {
     "colonne": [
      "tempo vero",
      "long. osservata",
      "lat. osservata",
      "long. calcolata",
      "lat. calcolata",
      "errore long.",
      "errore lat."
     ],
     "righe": [
      [
       "Nov. 3. 16. 47 01",
       [
        "♌",
        29,
        51,
        0
       ],
       [
        1,
        17,
        45
       ],
       [
        "♌",
        29,
        51,
        22
       ],
       [
        1,
        17,
        32
       ],
       [
        1,
        0,
        22
       ],
       [
        -1,
        0,
        13
       ]
      ],
      [
       "5. 15. 37 01",
       [
        "♍",
        3,
        23,
        0
       ],
       [
        1,
        6,
        0
       ],
       [
        "♍",
        3,
        24,
        32
       ],
       [
        1,
        6,
        9
       ],
       [
        1,
        1,
        32
       ],
       [
        1,
        0,
        9
       ]
      ],
      [
       "10. 16. 18 01",
       [
        15,
        32,
        0
       ],
       [
        0,
        27,
        0
       ],
       [
        15,
        33,
        2
       ],
       [
        0,
        25,
        7
       ],
       [
        1,
        1,
        2
       ],
       [
        -1,
        1,
        53
       ]
      ],
      [
       "16. 17. 0 01",
       [
        "♎",
        8,
        16,
        45
       ],
       [
        0,
        53,
        7
       ]
      ],
      [
       "18. 21. 34 01",
       [
        18,
        52,
        15
       ],
       [
        1,
        26,
        54
       ]
      ],
      [
       "20. 17. 0 01",
       [
        28,
        10,
        36
       ],
       [
        1,
        53,
        35
       ]
      ],
      [
       "23. 17. 5 01",
       [
        "♏",
        13,
        22,
        42
       ],
       [
        2,
        29,
        0
       ]
      ],
      [
       "Dec. 12. 4. 46 01",
       [
        "♑",
        6,
        32,
        30
       ],
       [
        8,
        28,
        0
       ],
       [
        "♑",
        6,
        31,
        20
       ],
       [
        8,
        29,
        6
       ],
       [
        -1,
        1,
        10
       ],
       [
        1,
        1,
        6
       ]
      ],
      [
       "21. 6. 37 01",
       [
        "♒",
        5,
        8,
        12
       ],
       [
        21,
        42,
        13
       ],
       [
        "♒",
        5,
        6,
        14
       ],
       [
        21,
        44,
        42
       ],
       [
        -1,
        1,
        58
       ],
       [
        1,
        2,
        29
       ]
      ],
      [
       "24. 6. 18 01",
       [
        18,
        49,
        23
       ],
       [
        25,
        23,
        5
       ],
       [
        18,
        47,
        30
       ],
       [
        25,
        23,
        35
       ],
       [
        -1,
        1,
        53
       ],
       [
        1,
        0,
        30
       ]
      ],
      [
       "26. 5. 21 01",
       [
        28,
        24,
        13
       ],
       [
        27,
        0,
        52
       ],
       [
        28,
        21,
        42
       ],
       [
        27,
        2,
        1
       ],
       [
        -1,
        2,
        31
       ],
       [
        1,
        1,
        9
       ]
      ],
      [
       "29. 8. 3 01",
       [
        "♓",
        13,
        10,
        41
       ],
       [
        28,
        9,
        58
       ],
       [
        "♓",
        13,
        11,
        14
       ],
       [
        28,
        10,
        38
       ],
       [
        1,
        0,
        33
       ],
       [
        1,
        0,
        40
       ]
      ],
      [
       "30. 8. 10 01",
       [
        17,
        38,
        20
       ],
       [
        28,
        11,
        53
       ],
       [
        17,
        38,
        27
       ],
       [
        28,
        11,
        37
       ],
       [
        1,
        0,
        7
       ],
       [
        -1,
        0,
        16
       ]
      ],
      [
       "Jan. 5. 6. 1 12",
       [
        "♈",
        8,
        48,
        53
       ],
       [
        26,
        15,
        7
       ],
       [
        "♈",
        8,
        48,
        51
       ],
       [
        26,
        14,
        57
       ],
       [
        -1,
        0,
        2
       ],
       [
        -1,
        0,
        10
       ]
      ],
      [
       "9. 7. 1 01",
       [
        18,
        44,
        4
       ],
       [
        24,
        11,
        56
       ],
       [
        18,
        43,
        51
       ],
       [
        24,
        12,
        17
       ],
       [
        -1,
        0,
        13
       ],
       [
        1,
        0,
        21
       ]
      ],
      [
       "10. 6. 6 01",
       [
        20,
        40,
        50
       ],
       [
        23,
        43,
        32
       ],
       [
        20,
        40,
        23
       ],
       [
        23,
        43,
        25
       ],
       [
        -1,
        0,
        27
       ],
       [
        -1,
        0,
        7
       ]
      ],
      [
       "13. 7. 9 01",
       [
        25,
        59,
        48
       ],
       [
        22,
        17,
        28
       ],
       [
        26,
        0,
        8
       ],
       [
        22,
        16,
        32
       ],
       [
        1,
        0,
        20
       ],
       [
        -1,
        0,
        56
       ]
      ],
      [
       "25. 7. 59 01",
       [
        "♉",
        9,
        35,
        0
       ],
       [
        17,
        56,
        30
       ],
       [
        "♉",
        9,
        34,
        11
       ],
       [
        17,
        56,
        6
       ],
       [
        -1,
        0,
        49
       ],
       [
        -1,
        0,
        24
       ]
      ],
      [
       "30. 8. 22 01",
       [
        13,
        19,
        51
       ],
       [
        16,
        42,
        18
       ],
       [
        13,
        18,
        28
       ],
       [
        16,
        40,
        5
       ],
       [
        -1,
        1,
        23
       ],
       [
        -1,
        2,
        13
       ]
      ],
      [
       "Feb. 2. 6. 35 01",
       [
        15,
        13,
        53
       ],
       [
        16,
        4,
        1
       ],
       [
        15,
        11,
        59
       ],
       [
        16,
        2,
        7
       ],
       [
        -1,
        1,
        54
       ],
       [
        -1,
        1,
        54
       ]
      ],
      [
       "5. 7. 4 12",
       [
        16,
        59,
        6
       ],
       [
        15,
        27,
        3
       ],
       [
        16,
        59,
        17
       ],
       [
        15,
        27,
        0
       ],
       [
        1,
        0,
        11
       ],
       [
        -1,
        0,
        3
       ]
      ],
      [
       "25. 8. 41 01",
       [
        26,
        18,
        35
       ],
       [
        12,
        46,
        46
       ],
       [
        26,
        16,
        59
       ],
       [
        12,
        45,
        22
       ],
       [
        -1,
        1,
        36
       ],
       [
        -1,
        1,
        24
       ]
      ],
      [
       "Mar. 1. 11. 10 01",
       [
        27,
        52,
        42
       ],
       [
        12,
        23,
        40
       ],
       [
        27,
        51,
        47
       ],
       [
        12,
        22,
        28
       ],
       [
        -1,
        0,
        55
       ],
       [
        -1,
        1,
        12
       ]
      ],
      [
       "5. 11. 39 01",
       [
        29,
        18,
        0
       ],
       [
        12,
        3,
        16
       ],
       [
        29,
        20,
        11
       ],
       [
        12,
        2,
        50
       ],
       [
        1,
        2,
        11
       ],
       [
        1,
        0,
        26
       ]
      ],
      [
       "9. 8. 38 01",
       [
        0,
        43,
        4
       ],
       [
        11,
        45,
        52
       ],
       [
        "♊",
        0,
        42,
        43
       ],
       [
        11,
        45,
        35
       ],
       [
        -1,
        0,
        21
       ],
       [
        -1,
        0,
        17
       ]
      ]
     ],
     "controlli": "errori = calcolato − osservato: 41 su 42 tornano al secondo; 5 mar., errore in latitudine: calcolato −0′26″, tabella +0′26″ (anche Motte). Latitudine osservata del 10 gen. 23.43.32 (tabella 1: 23.43.52): l’errore −0′7″ è coerente con 32. Asse maggiore 1382957 → periodo 575,0 anni."
    }
   }
  }
 ]
}
```

**Fine del Fascicolo 26a.**
