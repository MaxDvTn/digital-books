> **Copia pubblica.** In questa versione i campi `"la"` della Parte B sono vuoti: le frasi latine vengono dalla trascrizione del Newton Project, che non si ridistribuisce. Il latino del 1726 si legge su newtonproject.ox.ac.uk.

# Isaac Newton
# Principi matematici della filosofia naturale

## Fascicolo 22 — Libro III: la gravità universale (Propp. I–XIV)

**Nuova traduzione italiana di lavoro dal latino del 1726, confrontata con l’inglese di Andrew Motte nell’edizione del 1846.**

Versione 0.1 — 8 novembre 2026. Preparata con Claude (Anthropic) per Massimo Bosetti.

### Stato e perimetro

Questo fascicolo prosegue il Fascicolo 21 (titolo e introduzione del Libro III, *Regulæ philosophandi*, *Phænomena*). Traduce integralmente le **Proposizioni I–XIV** del Libro III, *De mundi systemate*, con i loro corollari e scolî e con l’**Ipotesi I**: le forze centrali dei satelliti, dei pianeti e della Luna (Propp. I–III); la «prova della Luna» e il suo Scolio (Prop. IV); l’identificazione della forza centripeta con la gravità (Prop. V e Scolio); l’esperimento dei pendoli di materiali diversi e la proporzionalità fra peso e quantità di materia (Prop. VI); la gravità universale (Prop. VII); i globi omogenei per strati, con le masse e le densità del Sole, di Giove, di Saturno e della Terra (Prop. VIII); la gravità all’interno dei pianeti (Prop. IX); la conservazione dei moti nei cieli (Prop. X); l’Ipotesi I e le Propp. XI–XII sul centro comune di gravità; le orbite ellittiche e le perturbazioni di Giove e Saturno (Prop. XIII); la quiete degli afeli e dei nodi, con lo Scolio sul moto secolare degli afeli (Prop. XIV). Il perimetro finisce prima di «PROPOSITIO XV.» (Fascicolo 23). È una traduzione di lavoro, non un’edizione critica validata.

Gli identificatori **III.G2.01–III.G2.56** e i titoli tematici tra parentesi sono aggiunte editoriali. Servono a orientare la lettura e a controllare la completezza. I numeri romani delle proposizioni, dei teoremi e dell’ipotesi, e i numeri dei corollari, appartengono al testo originale. Le integrazioni del curatore sono tra parentesi quadre. Le note poste dopo la traduzione non fanno parte del testo di Newton.

In coda al fascicolo c’è la **Parte B**, con i dati strutturati per le pagine interattive: 21 unità (tutte le proposizioni, l’Ipotesi I, il Corollario della Prop. III, i Cor. 1–3 della Prop. VIII, gli Scolî delle Propp. IV e XIV) e 122 passi, uno per frase latina delle dimostrazioni e dei calcoli.

### Fonti effettivamente consultate

1. **Latino di riferimento.** Isaac Newton, *Philosophiæ Naturalis Principia Mathematica*, terza edizione, Londra, 1726, Libro III, Propp. I–XIV, **pp. 395–411** (la Prop. I comincia a p. 395, dopo il marcatore ‹395› che nel file del Fascicolo 21 precede «PROPOSITIONES.»; i marcatori di questo file vanno da ‹396› a ‹411›). Trascrizione normalizzata del Newton Project, documento **NATP00303**, estratta in testo semplice senza correzioni: `fonti/latino-1726/latino-1726-L3-P01-14.md`. Il fascicolo non ha figure. Per i dati dei *Phænomena* citati ho usato `fonti/latino-1726/latino-1726-L3-Regole-Fenomeni.md` (Fascicolo 21); per i rimandi interni ad altre parti del Libro III, il latino dei gruppi G5 e G6.
2. **Inglese di confronto.** *Newton’s Principia*, traduzione di Andrew Motte, New York, Daniel Adee, 1846, Book III, Propp. I–XIV (Project Gutenberg n. 76404), estratto `fonti/motte-1846/motte-1846-L3-P01-14.md`. L’estratto non contiene marcatori di pagina: le pagine Motte sono indicate come «sezione corrispondente». Le formule stampate come immagini (27 marcatori `[SVG n]`) sono state lette sul LaTeX di `fonti/motte-1846/svg_tex.tsv`.
3. **Brief comune**, **istruzioni del Libro II e del Libro III** (`ISTRUZIONI-TRADUTTORE.md`), **Fascicoli 3, 5 e 20** (modelli di formato); per i rimandi, i **Fascicoli 3, 5, 6, 8, 9, 10, 11** (Libro I e Leggi) e **16, 17, 18b** (Libro II).

Non ho consultato né riprodotto traduzioni moderne. Non ho potuto vedere la stampa del 1726 né l’edizione Motte del 1729.

### Criteri di traduzione

- Il testo guida è il latino; l’inglese di Motte serve a controllare le interpretazioni ed è annotato quando aggiunge, omette o si discosta (§ A.10).
- Si applicano il **glossario comune** del brief, il **glossario del Libro II** e il **glossario del Libro III** (istruzioni del coordinatore): *phænomenon* «fenomeno» (nei rimandi «Fenomeno I»); *hypothesis* «ipotesi» («Ipotesi I»); *systema mundi* «sistema del mondo»; *planeta primarius* «pianeta primario»; *satelles*, *comites* «satellite»; *aphelium* «afelio»; *nodi* «nodi»; *cometa* «cometa»; *parallaxis* «parallasse»; *syzygiæ* «sizigie»; *conjunctio* «congiunzione»; *apogæum* «apogeo»; *motus medius* «moto medio»; *excentricitas* «eccentricità»; *orbis* (orbita) «orbita»; *umbilicus* «fuoco»; *mediocris distantia* «distanza media»; *ratio sesquiplicata* «rapporto sesquiplicato»; *semidiameter* «semidiametro»; *stellæ fixæ* «stelle fisse»; *maculæ* «macchie»; *æther* «etere»; *pendulum ad minuta secunda oscillans* «pendolo che batte i secondi»; *pes Parisiensis* «piede parigino»; *linea* «linea»; *milliare* «miglio»; *minutum primum / secundum* «primo / secondo» per gli angoli e «minuto / secondo» per i tempi; *gradus* «grado»; *Sol, Luna, Terra* e i nomi dei pianeti sempre con la maiuscola; *vis centripeta* «forza centripeta»; *vis motrix* «forza motrice»; *pondus* «peso»; *gravitas specifica* «gravità specifica»; *argentum vivum* «mercurio (argento vivo)» alla prima occorrenza; *in consequentia* «in conseguenza»; *quamproxime* «con ottima approssimazione»; Q.E.D. «C.V.D.».
- *Digitus* (Prop. IV, misura di lunghezza) è reso «pollice», secondo il glossario del Libro II: il glossario del Libro III riserva «dito» al *digitus* delle eclissi, che qui non compare.
- Le estensioni del glossario proprie di questo fascicolo sono elencate e motivate nel § A.0.
- Gli enunciati latini all’infinito (accusativo e infinito) sono resi con l’indicativo.
- Le frazioni appiattite dalla trascrizione («15⁤112», «178⁤2940», «14586») sono rese nella forma intesa («15 1/12», «178 29/40», «1/4586»), controllata sulle formule SVG di Motte; l’elenco è nel § A.7.
- Le date, i tempi e gli angoli restano come nel testo (giorni, ore, minuti; primi, secondi, terzi).
- I nomi propri sono resi nella forma italiana corrente quando esiste (Tolomeo, Copernico, Keplero, Aristotele, Cartesio); altrimenti nella forma originale (Huygens, Tycho, Wendelin, Street): § A.0.
- Nessuna formula moderna entra nel testo tradotto, eccetto la notazione D^(2 4/243) nella Prop. III, che rende l’esponente frazionario del latino *D2⁤4243* nello stesso modo del Fascicolo 9 (Prop. XLV, Cor. 1).

---

## Traduzione italiana

### Proposizione I. Teorema I (le forze che trattengono i satelliti di Giove)

**[III.G2.01]** **Le forze con cui i pianeti circumgioviali sono continuamente distolti dai moti rettilinei e trattenuti nelle loro orbite sono rivolte al centro di Giove e sono inversamente come i quadrati delle distanze dei loro luoghi da quel centro.**

**[III.G2.02]** La prima parte della proposizione è evidente per il Fenomeno I e per la Prop. II o III del Libro I; la seconda parte per il Fenomeno I e per il Cor. 6 della Prop. IV dello stesso Libro.

**[III.G2.03]** Lo stesso si intenda dei pianeti che accompagnano Saturno, per il Fenomeno II.

### Proposizione II. Teorema II (le forze che trattengono i pianeti primari)

**[III.G2.04]** **Le forze con cui i pianeti primari sono continuamente distolti dai moti rettilinei e trattenuti nelle loro orbite sono rivolte al Sole e sono inversamente come i quadrati delle distanze dal suo centro.**

**[III.G2.05]** La prima parte della proposizione è evidente per il Fenomeno V e per la Prop. II del Libro I; la seconda parte per il Fenomeno IV e per la Prop. IV dello stesso Libro. Ma questa parte della proposizione si dimostra con la massima esattezza per mezzo della quiete degli afeli. Infatti uno scostamento anche piccolissimo dal rapporto duplicato (per il Cor. 1 della Prop. XLV del Libro I) dovrebbe produrre un moto delle apsidi notevole in ogni singola rivoluzione, enorme in molte.

### Proposizione III. Teorema III (la forza che trattiene la Luna)

**[III.G2.06]** **La forza con cui la Luna è trattenuta nella sua orbita è rivolta alla Terra ed è inversamente come il quadrato della distanza dei suoi luoghi dal centro della Terra.**

**[III.G2.07]** La prima parte dell’asserzione è evidente per il Fenomeno VI e per la Prop. II o III del Libro I; la seconda parte per il moto lentissimo dell’apogeo lunare. Infatti quel moto, che in ogni singola rivoluzione è soltanto di tre gradi e tre primi in conseguenza, si può trascurare. È evidente infatti (per il Cor. 1 della Prop. XLV del Libro I) che, se la distanza della Luna dal centro della Terra sta al semidiametro della Terra come D sta a 1, la forza da cui nasce un tale moto è inversamente come D^(2 4/243), cioè inversamente come quella potenza di D il cui indice è 2 4/243; vale a dire in un rapporto della distanza un poco maggiore del duplicato inverso, ma che si avvicina al duplicato 59 3/4 volte più che al triplicato. Esso nasce invece dall’azione del Sole (come si dirà più avanti), e perciò qui va trascurato. L’azione del Sole, in quanto allontana la Luna dalla Terra, è con ottima approssimazione come la distanza della Luna dalla Terra; e perciò (per ciò che si dice nel Cor. 2 della Prop. XLV del Libro I) sta alla forza centripeta della Luna come 2 sta a 357,45 circa, ossia come 1 sta a 178 29/40. E, trascurata una forza del Sole così piccola, la forza restante con cui la Luna è trattenuta nell’orbita sarà inversamente come D². Ciò risulterà anche più pienamente confrontando questa forza con la forza di gravità, come si fa nella proposizione seguente.

**[III.G2.08]** *Cor.* Se la forza centripeta media con cui la Luna è trattenuta nell’orbita si aumenta prima nel rapporto di 177 29/40 a 178 29/40, poi anche nel rapporto duplicato del semidiametro della Terra alla distanza media del centro della Luna dal centro della Terra, si avrà la forza centripeta lunare alla superficie della Terra, posto che quella forza, scendendo verso la superficie della Terra, aumenti continuamente nel rapporto inverso duplicato dell’altezza.

### Proposizione IV. Teorema IV (la Luna gravita verso la Terra)

**[III.G2.09]** **La Luna gravita verso la Terra e dalla forza di gravità è continuamente distolta dal moto rettilineo e trattenuta nella sua orbita.**

**[III.G2.10]** La distanza media della Luna dalla Terra nelle sizigie è, in semidiametri terrestri, secondo Tolomeo e la maggior parte degli astronomi 59, secondo Wendelin e Huygens 60, secondo Copernico 60 1/3, secondo Street 60 2/5 e secondo Tycho 56 1/2. Ma Tycho, e quanti seguono le sue tavole delle rifrazioni, ponendo le rifrazioni del Sole e della Luna (del tutto contro la natura della luce) maggiori di quelle delle stelle fisse, e ciò di circa quattro o cinque primi, aumentarono la parallasse della Luna di altrettanti primi, cioè di circa un dodicesimo o un quindicesimo dell’intera parallasse. Si corregga questo errore, e la distanza risulterà di circa 60 1/2 semidiametri terrestri, quasi come è stata assegnata dagli altri. Assumiamo una distanza media di sessanta semidiametri nelle sizigie; e che il periodo lunare rispetto alle stelle fisse si compia in 27 giorni, 7 ore e 43 minuti, come è stabilito dagli astronomi; e che la circonferenza della Terra sia di 123249600 piedi parigini, come è stato determinato dai Francesi con le loro misure: se si immagina che la Luna, privata di ogni moto, sia lasciata andare in modo da scendere verso la Terra sotto l’azione di tutta quella forza da cui (per il Corollario della Prop. III) è trattenuta nella sua orbita, essa nello spazio di un minuto descriverà cadendo 15 1/12 piedi parigini. Ciò si ricava da un calcolo eseguito o per la Prop. XXXVI del Libro I o (ciò che torna lo stesso) per il Cor. 9 della Prop. IV dello stesso Libro. Infatti il seno verso dell’arco che la Luna, nel tempo di un minuto, con il suo moto medio, descriverebbe alla distanza di sessanta semidiametri terrestri, è di circa 15 1/12 piedi parigini, o più esattamente di 15 piedi, 1 pollice e 1 4/9 linee. Perciò, poiché quella forza, avvicinandosi alla Terra, aumenta nel rapporto inverso duplicato della distanza, e perciò alla superficie della Terra è 60×60 volte maggiore che alla Luna, un corpo che cadesse con quella forza nelle nostre regioni dovrebbe descrivere nello spazio di un minuto 60×60×15 1/12 piedi parigini, e nello spazio di un secondo 15 1/12 piedi, o più esattamente 15 piedi, 1 pollice e 1 4/9 linee. E con la stessa forza i gravi scendono di fatto verso la Terra. Infatti la lunghezza del pendolo che batte i secondi alla latitudine di Parigi è di tre piedi parigini e 8 1/2 linee, come ha osservato Huygens. E l’altezza che un grave descrive cadendo nel tempo di un secondo sta alla metà della lunghezza di questo pendolo nel rapporto duplicato della circonferenza del cerchio al suo diametro (come ha mostrato anche Huygens), e perciò è di 15 piedi parigini, 1 pollice, 1 7/9 linee. E perciò la forza con cui la Luna è trattenuta nella sua orbita, se si scende fino alla superficie della Terra, risulta uguale alla forza di gravità presso di noi, e perciò (per le Regole I e II) è proprio quella forza che siamo soliti chiamare gravità. Infatti, se la gravità fosse diversa da essa, i corpi, dirigendosi verso la Terra con le due forze congiunte, scenderebbero con velocità doppia, e nello spazio di un secondo descriverebbero cadendo 30 1/6 piedi parigini: del tutto contro l’esperienza.

**[III.G2.11]** Questo calcolo si fonda sull’ipotesi che la Terra sia in quiete. Infatti, se la Terra e la Luna si muovono attorno al Sole e intanto ruotano anche attorno al centro comune di gravità, restando la legge della gravità, la distanza dei centri della Luna e della Terra l’uno dall’altro sarà di circa 60 1/2 semidiametri terrestri, come risulterà a chi intraprenda il calcolo. Il calcolo si può poi eseguire per la Prop. LX del Libro I.

### Scolio (l’argomento della piccola luna)

**[III.G2.12]** La dimostrazione della proposizione si può spiegare più diffusamente così. Se più lune ruotassero attorno alla Terra, come avviene nel sistema di Saturno o di Giove, i loro tempi periodici (per l’argomento d’induzione) osserverebbero la legge dei pianeti scoperta da Keplero, e perciò le loro forze centripete sarebbero inversamente come i quadrati delle distanze dal centro della Terra, per la Prop. I di questo Libro. E se la più bassa di esse fosse piccola e toccasse quasi le cime dei monti più alti, la sua forza centripeta, con cui sarebbe trattenuta nell’orbita, uguaglierebbe con ottima approssimazione (per il calcolo precedente) le gravità dei corpi sulle cime di quei monti, e farebbe sì che la stessa piccola luna, se fosse privata di tutto il moto con cui procede nella sua orbita, per mancanza della forza centrifuga con cui era rimasta nell’orbita scendesse verso la Terra, e ciò con la stessa velocità con cui cadono i gravi sulle cime di quei monti, per l’uguaglianza delle forze con cui scendono. E se la forza con cui quella piccola luna più bassa scende fosse diversa dalla gravità, e quella piccola luna fosse anche grave verso la Terra al modo dei corpi sulle cime dei monti, la stessa piccola luna, per le due forze congiunte, scenderebbe con velocità doppia. Perciò, poiché entrambe le forze, sia queste dei corpi gravi sia quelle delle lune, sono rivolte al centro della Terra e sono fra loro simili e uguali, esse (per le Regole I e II) avranno la stessa causa. E perciò la forza con cui la Luna è trattenuta nella sua orbita sarà proprio quella che siamo soliti chiamare gravità: e ciò soprattutto perché la piccola luna sulla cima del monte non debba o essere priva di gravità o cadere due volte più velocemente di quanto sogliono cadere i corpi gravi.

### Proposizione V. Teorema V (satelliti e pianeti gravitano verso i loro corpi centrali)

**[III.G2.13]** **I pianeti circumgioviali gravitano verso Giove, i circumsaturnii verso Saturno e i circumsolari verso il Sole, e per la forza della loro gravità sono continuamente distolti dai moti rettilinei e trattenuti in orbite curvilinee.**

**[III.G2.14]** Infatti le rivoluzioni dei pianeti circumgioviali attorno a Giove, dei circumsaturnii attorno a Saturno, e di Mercurio, di Venere e degli altri circumsolari attorno al Sole sono fenomeni dello stesso genere della rivoluzione della Luna attorno alla Terra; e perciò (per la Regola II) dipendono da cause dello stesso genere: soprattutto perché si è dimostrato che le forze da cui quelle rivoluzioni dipendono sono rivolte ai centri di Giove, di Saturno e del Sole e, allontanandosi da Giove, da Saturno e dal Sole, decrescono con lo stesso rapporto e la stessa legge con cui la forza di gravità decresce allontanandosi dalla Terra.

**[III.G2.15]** *Cor. 1.* Esiste dunque una gravità verso tutti i pianeti. Nessuno infatti dubita che Venere, Mercurio e gli altri siano corpi dello stesso genere di Giove e di Saturno. E poiché ogni attrazione, per la terza legge del moto, è reciproca, Giove graviterà verso tutti i suoi satelliti, Saturno verso i suoi, la Terra verso la Luna e il Sole verso tutti i pianeti primari.

**[III.G2.16]** *Cor. 2.* La gravità che è rivolta a ciascun pianeta è inversamente come il quadrato della distanza dei luoghi dal suo centro.

**[III.G2.17]** *Cor. 3.* Tutti i pianeti sono gravi gli uni verso gli altri, per i Cor. 1 e 2. E di qui Giove e Saturno, vicino alla congiunzione, attraendosi l’un l’altro, perturbano sensibilmente i loro moti reciproci; il Sole perturba i moti lunari; il Sole e la Luna perturbano il nostro mare, come si spiegherà in seguito.

### Scolio (la forza centripeta è la gravità)

**[III.G2.18]** Finora abbiamo chiamato centripeta quella forza con cui i corpi celesti sono trattenuti nelle loro orbite. Ora è accertato che essa è la gravità, e perciò d’ora in poi la chiameremo gravità. Infatti la causa di quella forza centripeta con cui la Luna è trattenuta nell’orbita deve estendersi a tutti i pianeti, per le Regole I, II e IV.

### Proposizione VI. Teorema VI (i pesi sono proporzionali alla quantità di materia)

**[III.G2.19]** **Tutti i corpi gravitano verso ciascun pianeta, e i loro pesi verso uno stesso pianeta qualsiasi, a uguali distanze dal centro del pianeta, sono proporzionali alla quantità di materia di ciascuno.**

**[III.G2.20]** Che la discesa di tutti i gravi verso la Terra (tolto almeno il ritardo disuguale che nasce dalla piccolissima resistenza dell’aria) avvenga in tempi uguali, lo hanno osservato altri già da tempo; e con la massima esattezza si può rilevare l’uguaglianza dei tempi nei pendoli. Ho messo alla prova la cosa con oro, argento, piombo, vetro, sabbia, sale comune, legno, acqua, frumento. Prendevo due scatole di legno, rotonde e uguali. Ne riempivo una di legno, e nel centro di oscillazione dell’altra sospendevo lo stesso peso d’oro (quanto più esattamente potevo). Le scatole, appese a fili uguali di undici piedi, costituivano pendoli del tutto uguali quanto al peso, alla figura e alla resistenza dell’aria: e, poste l’una accanto all’altra, con oscillazioni uguali andavano e tornavano insieme per moltissimo tempo. Perciò la quantità di materia nell’oro (per i Cor. 1 e 6 della Prop. XXIV del Libro II) stava alla quantità di materia nel legno come l’azione della forza motrice su tutto l’oro sta alla sua azione su tutto il legno, cioè come il peso al peso. E così negli altri. Nei corpi dello stesso peso, una differenza di materia che fosse anche minore della millesima parte della materia totale si sarebbe potuta scoprire chiaramente con questi esperimenti. Ora, non c’è dubbio che la natura della gravità verso i pianeti sia la stessa che verso la Terra. Si immagini infatti che questi corpi terrestri siano sollevati fino all’orbita della Luna e, privati di ogni moto insieme con la Luna, siano lasciati andare in modo da cadere insieme verso la Terra; per ciò che si è già mostrato è certo che in tempi uguali descriveranno con la Luna spazi uguali, e perciò che stanno alla quantità di materia nella Luna come i loro pesi stanno al peso di essa. Inoltre, poiché i satelliti di Giove ruotano in tempi che sono nel rapporto sesquiplicato delle distanze dal centro di Giove, le loro gravità acceleratrici verso Giove saranno inversamente come i quadrati delle distanze dal centro di Giove; e perciò, a uguali distanze da Giove, le loro gravità acceleratrici risulterebbero uguali. Di conseguenza, cadendo da altezze uguali in tempi uguali, descriverebbero spazi uguali, proprio come avviene nei gravi su questa nostra Terra. E con lo stesso argomento i pianeti circumsolari, lasciati andare a uguali distanze dal Sole, nella loro discesa verso il Sole descriverebbero in tempi uguali spazi uguali. Ma le forze con cui corpi disuguali sono ugualmente accelerati sono come i corpi; cioè i pesi sono come le quantità di materia nei pianeti. Inoltre, che i pesi di Giove e dei suoi satelliti verso il Sole siano proporzionali alle loro quantità di materia è evidente dal moto regolarissimo dei satelliti, per il Cor. 3 della Prop. LXV del Libro I. Infatti, se alcuni di essi fossero attratti verso il Sole più degli altri, in proporzione alla loro quantità di materia, i moti dei satelliti (per il Cor. 2 della Prop. LXV del Libro I) sarebbero perturbati dalla disuguaglianza dell’attrazione. Se, a uguali distanze dal Sole, un satellite fosse più grave verso il Sole, in proporzione alla sua quantità di materia, di quanto lo sia Giove in proporzione alla sua, in un rapporto dato qualsiasi, per esempio come d sta a e, la distanza fra il centro del Sole e il centro dell’orbita del satellite sarebbe sempre maggiore della distanza fra il centro del Sole e il centro di Giove, con ottima approssimazione nel rapporto subduplicato: come ho trovato con un certo calcolo. E se il satellite fosse meno grave verso il Sole in quel rapporto di d a e, la distanza del centro dell’orbita del satellite dal Sole sarebbe minore della distanza del centro di Giove dal Sole in quello stesso rapporto subduplicato. Perciò, se a uguali distanze dal Sole la gravità acceleratrice di un satellite qualsiasi verso il Sole fosse maggiore o minore della gravità acceleratrice di Giove verso il Sole anche soltanto di una millesima parte della gravità totale, la distanza del centro dell’orbita del satellite dal Sole sarebbe maggiore o minore della distanza di Giove dal Sole di una duemillesima parte della distanza totale, cioè di un quinto della distanza del satellite più esterno dal centro di Giove: e questa eccentricità dell’orbita sarebbe assai sensibile. Ma le orbite dei satelliti sono concentriche a Giove, e perciò le gravità acceleratrici di Giove e dei satelliti verso il Sole sono uguali fra loro. E con lo stesso argomento i pesi di Saturno e dei suoi satelliti verso il Sole, a uguali distanze dal Sole, sono come le quantità di materia in essi; e i pesi della Luna e della Terra verso il Sole o sono nulli, o sono esattamente proporzionali alle loro masse. Ma qualche peso c’è, per i Cor. 1 e 3 della Prop. V.

**[III.G2.21]** Inoltre i pesi delle singole parti di ciascun pianeta verso un altro pianeta qualsiasi stanno fra loro come la materia nelle singole parti. Infatti, se alcune parti gravitassero di più, altre di meno, di quanto comporta la quantità di materia, il pianeta intero, secondo il genere delle parti di cui è più ricco, graviterebbe di più o di meno di quanto comporta la quantità di materia del tutto. Né importa se quelle parti siano esterne o interne. Infatti, se per esempio si immagina che i corpi terrestri che sono presso di noi siano sollevati fino all’orbita della Luna e confrontati con il corpo della Luna: se i loro pesi stessero ai pesi delle parti esterne della Luna come le quantità di materia nelle une e negli altri, e invece ai pesi delle parti interne in un rapporto maggiore o minore, starebbero al peso della Luna intera in un rapporto maggiore o minore: contro ciò che si è mostrato sopra.

**[III.G2.22]** *Cor. 1.* Di qui i pesi dei corpi non dipendono dalle loro forme e tessiture. Infatti, se potessero variare con le forme, sarebbero maggiori o minori, secondo la varietà delle forme, a parità di materia: del tutto contro l’esperienza.

**[III.G2.23]** *Cor. 2.* Tutti i corpi che sono attorno alla Terra sono gravi verso la Terra; e i pesi di tutti quelli che distano ugualmente dal centro della Terra sono come le quantità di materia in essi. Questa è una qualità di tutti i corpi sui quali è possibile istituire esperimenti, e perciò, per la Regola III, va affermata di tutti i corpi. Se l’etere, o qualunque altro corpo, o fosse del tutto privo di gravità, o gravitasse meno di quanto comporta la sua quantità di materia, poiché esso (secondo il pensiero di Aristotele, di Cartesio e di altri) non differisce dagli altri corpi se non nella forma della materia, potrebbe, per un cambiamento della forma, trasformarsi a poco a poco in un corpo della stessa condizione di quelli che gravitano al massimo in proporzione alla quantità di materia; e viceversa i corpi più gravi, assumendo a poco a poco la forma di quello, potrebbero perdere a poco a poco la loro gravità. E perciò i pesi dipenderebbero dalle forme dei corpi e potrebbero variare con le forme, contro ciò che si è provato nel corollario precedente.

**[III.G2.24]** *Cor. 3.* Non tutti gli spazi sono ugualmente pieni. Infatti, se tutti gli spazi fossero ugualmente pieni, la gravità specifica del fluido di cui sarebbe riempita la regione dell’aria, a causa della somma densità della materia, non cederebbe in nulla alla gravità specifica del mercurio (argento vivo), o dell’oro, o di qualunque altro corpo densissimo; e perciò né l’oro né alcun altro corpo potrebbe scendere nell’aria. Infatti i corpi, nei fluidi, se non sono specificamente più gravi, non scendono affatto. E se la quantità di materia in uno spazio dato può essere diminuita con una rarefazione qualsiasi, perché non potrebbe essere diminuita all’infinito?

**[III.G2.25]** *Cor. 4.* Se tutte le particelle solide di tutti i corpi sono della stessa densità e non possono rarefarsi senza pori, si dà il vuoto. Dico della stessa densità quelle particelle le cui forze d’inerzia sono come le grandezze.

**[III.G2.26]** *Cor. 5.* La forza di gravità è di genere diverso dalla forza magnetica. Infatti l’attrazione magnetica non è come la materia attratta. Alcuni corpi sono attratti di più, altri di meno, moltissimi non sono attratti. E la forza magnetica in un solo e medesimo corpo può aumentare e diminuire, ed è talvolta molto maggiore, in proporzione alla quantità di materia, della forza di gravità; e allontanandosi dal magnete decresce non nel rapporto duplicato della distanza, ma quasi nel triplicato, per quanto ho potuto rilevare da alcune osservazioni grossolane.

### Proposizione VII. Teorema VII (la gravità verso tutti i corpi)

**[III.G2.27]** **Esiste una gravità verso tutti i corpi, ed è proporzionale alla quantità di materia di ciascuno.**

**[III.G2.28]** Abbiamo già provato prima che tutti i pianeti sono gravi gli uni verso gli altri, e anche che la gravità verso ciascuno, considerato separatamente, è inversamente come il quadrato della distanza dei luoghi dal centro del pianeta. E di qui segue (per la Prop. LXIX del Libro I e i suoi corollari) che la gravità verso tutti è proporzionale alla materia in essi.

**[III.G2.29]** Inoltre, poiché tutte le parti di un pianeta qualsiasi A sono gravi verso un pianeta qualsiasi B, e la gravità di ciascuna parte sta alla gravità del tutto come la materia della parte sta alla materia del tutto, e (per la terza legge del moto) a ogni azione è uguale una reazione, il pianeta B a sua volta graviterà verso tutte le parti del pianeta A, e la sua gravità verso ciascuna parte starà alla sua gravità verso il tutto come la materia della parte sta alla materia del tutto. C.V.D.

**[III.G2.30]** *Cor. 1.* Dunque la gravità verso il pianeta intero nasce ed è composta dalla gravità verso le singole parti. Ne abbiamo esempi nelle attrazioni magnetiche ed elettriche: ogni attrazione verso il tutto nasce infatti dalle attrazioni verso le singole parti. La cosa si capirà, nel caso della gravità, concependo che più pianeti minori si riuniscano in un solo globo e compongano un pianeta maggiore. Infatti la forza del tutto dovrà nascere dalle forze delle parti componenti. Se qualcuno obietta che tutti i corpi che sono presso di noi dovrebbero, per questa legge, gravitare gli uni verso gli altri, mentre una tale gravità non si avverte affatto, rispondo che la gravità verso questi corpi, poiché sta alla gravità verso la Terra intera come questi corpi stanno alla Terra intera, è molto minore di quella che si possa avvertire.

**[III.G2.31]** *Cor. 2.* La gravitazione verso le singole particelle uguali di un corpo è inversamente come il quadrato della distanza dei luoghi dalle particelle. È evidente per il Cor. 3 della Prop. LXXIV del Libro I.

### Proposizione VIII. Teorema VIII (globi omogenei per strati; masse e densità dei pianeti)

**[III.G2.32]** **Se la materia di due globi che gravitano l’uno verso l’altro è omogenea da ogni parte nelle regioni che distano ugualmente dai centri, il peso di ciascuno dei due globi verso l’altro sarà inversamente come il quadrato della distanza fra i centri.**

**[III.G2.33]** Dopo che avevo trovato che la gravità verso il pianeta intero nasce ed è composta dalle gravità verso le parti, e che verso le singole parti è inversamente proporzionale ai quadrati delle distanze dalle parti, dubitavo se quella proporzione inversa duplicata valesse esattamente nella forza totale composta da più forze, o soltanto con ottima approssimazione. Poteva infatti accadere che la proporzione, che a distanze maggiori valeva con sufficiente esattezza, vicino alla superficie del pianeta, a causa delle distanze disuguali delle particelle e delle loro posizioni dissimili, sbagliasse notevolmente. Alla fine, però, per le Propp. LXXV e LXXVI del Libro I e i loro corollari, compresi la verità della proposizione di cui qui si tratta.

**[III.G2.34]** *Cor. 1.* Di qui si possono trovare e confrontare fra loro i pesi dei corpi verso pianeti diversi. Infatti i pesi di corpi uguali che ruotano in cerchi attorno ai pianeti sono (per il Cor. 2 della Prop. IV del Libro I) come i diametri dei cerchi direttamente e come i quadrati dei tempi periodici inversamente; e i pesi alle superfici dei pianeti, o a qualsiasi altra distanza dal centro, sono maggiori o minori (per questa proposizione) nel rapporto inverso duplicato delle distanze. Così, dai tempi periodici di Venere attorno al Sole, di 224 giorni e 16 3/4 ore, del satellite circumgioviale più esterno attorno a Giove, di 16 giorni e 16 8/15 ore, del satellite di Huygens attorno a Saturno, di 15 giorni e 22 2/3 ore, e della Luna attorno alla Terra, di 27 giorni, 7 ore e 43 minuti, confrontati con la distanza media di Venere dal Sole e con le elongazioni massime eliocentriche del satellite circumgioviale più esterno dal centro di Giove, 8′ 16″, del satellite di Huygens dal centro di Saturno, 3′ 4″, e della Luna dal centro della Terra, 10′ 33″, facendo il calcolo ho trovato che i pesi di corpi uguali, ugualmente distanti dal centro del Sole, di Giove, di Saturno e della Terra, verso il Sole, Giove, Saturno e la Terra stanno rispettivamente come 1, 1/1067, 1/3021 e 1/169282; e che, aumentando o diminuendo le distanze, i pesi diminuiscono o aumentano nel rapporto duplicato: i pesi di corpi uguali verso il Sole, Giove, Saturno e la Terra alle distanze 10000, 997, 791 e 109 dai loro centri, e perciò alle loro superfici, staranno rispettivamente come 10000, 943, 529 e 435. Quanto siano i pesi dei corpi alla superficie della Luna si dirà in seguito.

**[III.G2.35]** *Cor. 2.* Si conosce anche la quantità di materia nei singoli pianeti. Infatti le quantità di materia nei pianeti sono come le loro forze a uguali distanze dai loro centri, cioè nel Sole, in Giove, in Saturno e nella Terra sono rispettivamente come 1, 1/1067, 1/3021 e 1/169282. Se la parallasse del Sole si pone maggiore o minore di 10″ 30‴, la quantità di materia nella Terra dovrà essere aumentata o diminuita nel rapporto triplicato.

**[III.G2.36]** *Cor. 3.* Si conoscono anche le densità dei pianeti. Infatti i pesi di corpi uguali e omogenei verso sfere omogenee sono, alle superfici delle sfere, come i diametri delle sfere, per la Prop. LXXII del Libro I; e perciò le densità di sfere eterogenee sono come quei pesi divisi per i diametri delle sfere. Ora, i veri diametri del Sole, di Giove, di Saturno e della Terra stavano fra loro come 10000, 997, 791 e 109, e i pesi verso di essi come 10000, 943, 529 e 435 rispettivamente; e perciò le densità sono come 100, 94 1/2, 67, 400. La densità della Terra che risulta da questo calcolo non dipende dalla parallasse del Sole, ma è determinata dalla parallasse della Luna, e perciò qui è definita correttamente. Il Sole è dunque un poco più denso di Giove, e Giove più di Saturno, e la Terra quattro volte più densa del Sole. Infatti il Sole, per il suo enorme calore, si rarefà. La Luna invece è più densa della Terra, come risulterà in seguito.

**[III.G2.37]** *Cor. 4.* Sono dunque più densi, a parità delle altre condizioni, i pianeti più piccoli: così infatti la forza di gravità alle loro superfici si avvicina di più all’uguaglianza. Ma sono più densi, a parità delle altre condizioni, anche i pianeti più vicini al Sole: come Giove rispetto a Saturno, e la Terra rispetto a Giove. I pianeti dovevano infatti essere collocati a distanze diverse dal Sole, perché ciascuno, secondo il grado della sua densità, godesse di un calore del Sole maggiore o minore. La nostra acqua, se la Terra fosse collocata nell’orbita di Saturno, gelerebbe; se nell’orbita di Mercurio, se ne andrebbe subito in vapori. Infatti la luce del Sole, a cui il calore è proporzionale, è sette volte più densa nell’orbita di Mercurio che presso di noi: e con il termometro ho sperimentato che l’acqua bolle con un calore sette volte quello del Sole d’estate. Né c’è dubbio che la materia di Mercurio sia adattata al calore, e perciò sia più densa di questa nostra; poiché ogni materia più densa richiede, per compiere le operazioni naturali, un calore maggiore.

### Proposizione IX. Teorema IX (la gravità all’interno dei pianeti)

**[III.G2.38]** **La gravità, procedendo dalle superfici dei pianeti verso il basso, decresce con ottima approssimazione nel rapporto delle distanze dal centro.**

**[III.G2.39]** Se la materia del pianeta fosse uniforme quanto alla densità, questa proposizione varrebbe esattamente, per la Prop. LXXIII del Libro I. L’errore è dunque tanto grande quanto può nascere dalla densità non uniforme.

### Proposizione X. Teorema X (i moti dei pianeti si conservano a lungo)

**[III.G2.40]** **I moti dei pianeti nei cieli possono conservarsi per lunghissimo tempo.**

**[III.G2.41]** Nello Scolio della Prop. XL del Libro II si è mostrato che un globo d’acqua congelata, muovendosi liberamente nella nostra aria e descrivendo la lunghezza del suo semidiametro, perderebbe per la resistenza dell’aria 1/4586 del suo moto. E la stessa proporzione vale con ottima approssimazione in globi comunque grandi e veloci. Ora, che il globo della nostra Terra sia più denso che se constasse tutto d’acqua, lo ricavo così. Se questo globo fosse tutto d’acqua, qualunque cosa fosse più rada dell’acqua, a causa della minore gravità specifica, emergerebbe e galleggerebbe sopra. E per questa ragione un globo di terra coperto d’acqua da ogni parte, se fosse più rado dell’acqua, emergerebbe da qualche parte, e tutta l’acqua, defluendo di là, si raccoglierebbe nella regione opposta. E la condizione della nostra Terra, circondata in gran parte dai mari, è la stessa. Se essa non fosse più densa, emergerebbe dai mari e, secondo il grado della sua leggerezza, sporgerebbe in parte dall’acqua, mentre tutti i mari confluirebbero nella regione opposta. Con lo stesso argomento le macchie solari sono più leggere della materia luminosa del Sole sulla quale galleggiano. E in qualunque modo si siano formati i pianeti, tutta la materia più grave dell’acqua, nel tempo in cui la massa era fluida, si dirigeva verso il centro. Perciò, poiché la terra comune in superficie è circa due volte più grave dell’acqua, e poco più sotto, nelle miniere, si trova circa tre o quattro o anche cinque volte più grave, è verosimile che la quantità di tutta la materia della Terra sia circa cinque o sei volte maggiore che se constasse tutta d’acqua; soprattutto perché si è già mostrato prima che la Terra è circa quattro volte più densa di Giove. Perciò, se Giove è un poco più denso dell’acqua, nello spazio di trenta giorni, nei quali descrive la lunghezza di 459 suoi semidiametri, perderebbe, in un mezzo della stessa densità della nostra aria, quasi la decima parte del suo moto. Ma poiché la resistenza dei mezzi diminuisce nel rapporto del peso e della densità, così che l’acqua, che è 13 3/5 volte più leggera del mercurio, resiste di meno nello stesso rapporto, e l’aria, che è 860 volte più leggera dell’acqua, resiste di meno nello stesso rapporto: se si sale nei cieli, dove il peso del mezzo in cui si muovono i pianeti diminuisce immensamente, la resistenza quasi cesserà. Abbiamo mostrato infatti nello Scolio della Prop. XXII del Libro II che, se si salisse all’altezza di duecento miglia sopra la Terra, l’aria vi sarebbe più rada che alla superficie della Terra nel rapporto di 30 a 0,0000000000003998, ossia di 75000000000000 a 1 circa. E di qui l’astro di Giove, ruotando in un mezzo della stessa densità di quell’aria superiore, nel tempo di 1000000 di anni non perderebbe per la resistenza del mezzo la milionesima parte del suo moto. Negli spazi più vicini alla Terra, infatti, non si trova nulla che crei resistenza oltre l’aria, le esalazioni e i vapori. Quando questi sono stati estratti con grandissima cura da un vaso di vetro cilindrico cavo, i gravi cadono dentro il vetro liberissimamente e senza alcuna resistenza sensibile; lo stesso oro e una piuma sottilissima, lasciati cadere insieme, cadono con uguale velocità e, descrivendo nella caduta un’altezza di quattro, sei o otto piedi, arrivano insieme sul fondo, come si è accertato con l’esperienza. E perciò, se si sale nei cieli vuoti di aria e di esalazioni, i pianeti e le comete si muoveranno per quegli spazi senza alcuna resistenza sensibile per lunghissimo tempo.

### Ipotesi I (il centro del sistema del mondo)

**[III.G2.42]** **Il centro del sistema del mondo è in quiete.**

**[III.G2.43]** Questo è ammesso da tutti, mentre alcuni sostengono che nel centro del sistema stia in quiete la Terra, altri il Sole. Vediamo che cosa ne segua.

### Proposizione XI. Teorema XI (il centro comune di gravità è in quiete)

**[III.G2.44]** **Il centro comune di gravità della Terra, del Sole e di tutti i pianeti è in quiete.**

**[III.G2.45]** Infatti quel centro (per il Cor. IV delle leggi) o sarà in quiete o avanzerà uniformemente in linea retta. Ma, se quel centro avanzasse sempre, si muoverebbe anche il centro del mondo, contro l’Ipotesi.

### Proposizione XII. Teorema XII (il moto del Sole attorno al centro comune di gravità)

**[III.G2.46]** **Il Sole è agitato da un moto perpetuo, ma non si allontana mai molto dal centro comune di gravità di tutti i pianeti.**

**[III.G2.47]** Infatti, poiché (per il Cor. 2 della Prop. VIII) la materia nel Sole sta alla materia in Giove come 1067 a 1, e la distanza di Giove dal Sole sta al semidiametro del Sole in un rapporto un poco maggiore, il centro comune di gravità di Giove e del Sole cadrà in un punto un poco al di sopra della superficie del Sole. Con lo stesso argomento, poiché la materia nel Sole sta alla materia in Saturno come 3021 a 1, e la distanza di Saturno dal Sole sta al semidiametro del Sole in un rapporto un poco minore, il centro comune di gravità di Saturno e del Sole cadrà in un punto un poco al di sotto della superficie del Sole. E, seguendo le tracce dello stesso calcolo, se la Terra e tutti i pianeti stessero da una sola parte del Sole, il centro comune di gravità di tutti disterebbe dal centro del Sole appena un intero diametro del Sole. Negli altri casi la distanza dei centri è sempre minore. E perciò, poiché quel centro di gravità è perpetuamente in quiete, il Sole, secondo la varia posizione dei pianeti, si muoverà in ogni direzione, ma non si allontanerà mai molto da quel centro.

**[III.G2.48]** *Cor.* Di qui il centro comune di gravità della Terra, del Sole e di tutti i pianeti va considerato come il centro del mondo. Infatti, poiché la Terra, il Sole e tutti i pianeti gravitano gli uni verso gli altri, e perciò, secondo la forza della loro gravità, sono perpetuamente agitati secondo le leggi del moto, è evidente che i loro centri mobili non possono essere considerati come il centro del mondo in quiete. Se nel centro si dovesse collocare quel corpo verso il quale tutti i corpi gravitano al massimo (com’è opinione del volgo), questo privilegio si dovrebbe concedere al Sole. Ma poiché il Sole si muove, si dovrà scegliere un punto in quiete dal quale il centro del Sole si allontani il meno possibile, e dal quale si allontanerebbe ancora di meno se soltanto il Sole fosse più denso e più grande, così da muoversi di meno.

### Proposizione XIII. Teorema XIII (orbite ellittiche; le perturbazioni)

**[III.G2.49]** **I pianeti si muovono in ellissi che hanno un fuoco nel centro del Sole, e con raggi condotti a quel centro descrivono aree proporzionali ai tempi.**

**[III.G2.50]** Abbiamo discusso sopra di questi moti a partire dai fenomeni. Ora, conosciuti i principi dei moti, da questi ricaviamo a priori i moti celesti. Poiché i pesi dei pianeti verso il Sole sono inversamente come i quadrati delle distanze dal centro del Sole, se il Sole fosse in quiete e gli altri pianeti non agissero gli uni sugli altri, le loro orbite sarebbero ellittiche, con il Sole nel fuoco comune, e le aree sarebbero descritte proporzionalmente ai tempi (per le Propp. I e XI e per il Cor. 1 della Prop. XIII del Libro I); ma le azioni dei pianeti gli uni sugli altri sono piccolissime (tanto che si possono trascurare), e perturbano i moti dei pianeti in ellissi attorno al Sole mobile meno (per la Prop. LXVI del Libro I) che se quei moti si compissero attorno al Sole in quiete.

**[III.G2.51]** L’azione di Giove su Saturno, invero, non è del tutto trascurabile. Infatti la gravità verso Giove sta alla gravità verso il Sole (a parità di distanze) come 1 a 1067; e perciò nella congiunzione di Giove e Saturno, poiché la distanza di Saturno da Giove sta alla distanza di Saturno dal Sole quasi come 4 a 9, la gravità di Saturno verso Giove starà alla gravità di Saturno verso il Sole come 81 a 16×1067, ossia come 1 a 211 circa. E di qui nasce una perturbazione dell’orbita di Saturno, in ogni congiunzione di questo pianeta con Giove, così sensibile che gli astronomi ne restano perplessi. Secondo la varia posizione del pianeta in queste congiunzioni, la sua eccentricità ora aumenta ora diminuisce, l’afelio ora avanza ora forse arretra, e il moto medio a vicenda è accelerato e ritardato. Tutto l’errore nel suo moto attorno al Sole che nasce da una forza così grande (eccetto che nel moto medio) si può tuttavia quasi evitare ponendo il fuoco inferiore della sua orbita nel centro comune di gravità di Giove e del Sole (per la Prop. LXVII del Libro I), e perciò, dove è massimo, supera appena due primi. E l’errore massimo nel moto medio supera appena due primi all’anno. Nella congiunzione di Giove e Saturno, poi, le gravità acceleratrici del Sole verso Saturno, di Giove verso Saturno e di Giove verso il Sole sono quasi come 16, 81 e 16×81×3021/25, ossia 156609; e perciò la differenza delle gravità del Sole verso Saturno e di Giove verso Saturno sta alla gravità di Giove verso il Sole come 65 a 156609, ossia come 1 a 2409. A questa differenza è proporzionale la massima efficacia di Saturno nel perturbare il moto di Giove, e perciò la perturbazione dell’orbita di Giove è molto minore di quella di Saturno. Le perturbazioni delle altre orbite sono ancora molto minori, eccetto che l’orbita della Terra è perturbata sensibilmente dalla Luna. Il centro comune di gravità della Terra e della Luna percorre un’ellisse attorno al Sole posto nel fuoco, e con un raggio condotto al Sole descrive in essa aree proporzionali ai tempi; la Terra invece ruota attorno a questo centro comune con un moto mensile.

### Proposizione XIV. Teorema XIV (afeli e nodi in quiete)

**[III.G2.52]** **Gli afeli e i nodi delle orbite sono in quiete.**

**[III.G2.53]** Gli afeli sono in quiete per la Prop. XI del Libro I, come pure i piani delle orbite, per la Prop. I dello stesso Libro; ed essendo in quiete i piani, sono in quiete i nodi. Tuttavia dalle azioni reciproche dei pianeti e delle comete in rivoluzione nasceranno alcune disuguaglianze, che però per la loro piccolezza qui si possono trascurare.

**[III.G2.54]** *Cor. 1.* Sono in quiete anche le stelle fisse, perché conservano posizioni date rispetto agli afeli e ai nodi.

**[III.G2.55]** *Cor. 2.* E perciò, poiché non c’è alcuna loro parallasse sensibile che nasca dal moto annuo della Terra, le loro forze, a causa dell’immensa distanza dei corpi, non produrranno alcun effetto sensibile nella regione del nostro sistema. Anzi, le stelle fisse, disperse ugualmente in tutte le parti del cielo, distruggono con attrazioni contrarie le loro forze reciproche, per la Prop. LXX del Libro I.

### Scolio (il moto lento degli afeli dei pianeti interni)

**[III.G2.56]** Poiché i pianeti più vicini al Sole (cioè Mercurio, Venere, la Terra e Marte), per la piccolezza dei loro corpi, agiscono poco gli uni sugli altri, i loro afeli e nodi saranno in quiete, se non in quanto siano turbati dalle forze di Giove, di Saturno e dei corpi superiori. E di qui si può ricavare per la teoria della gravità che i loro afeli si muovono un poco in conseguenza rispetto alle stelle fisse, e ciò nella proporzione sesquiplicata delle distanze di questi pianeti dal Sole. Così, se l’afelio di Marte in cento anni compie 33′ 20″ in conseguenza rispetto alle stelle fisse, gli afeli della Terra, di Venere e di Mercurio in cento anni compiranno rispettivamente 17′ 40″, 10′ 53″ e 4′ 16″. E questi moti, per la loro piccolezza, sono trascurati in questa proposizione.

---

## Apparato

### A.0 Estensioni del glossario

I termini seguenti non comparivano nei glossari comuni né nelle istruzioni del Libro III. Ognuno è reso in modo costante in tutto il fascicolo.

| Latino | Italiano | Motivazione |
|---|---|---|
| *planetæ circumjoviales, circumsaturnii, circumsolares* | «pianeti circumgioviali, circumsaturnii, circumsolari» | Propp. I, V, VI, VIII. Calco, come Motte («circumjovial», «circumsaturnal», «circumsolar»): Newton chiama «pianeti» anche i satelliti, e il calco conserva il parallelismo con i *circumsolares*. Nota N1. Alternativa: «pianeti che ruotano attorno a Giove» (Fascicolo 20, II.S9.27, per *planetarum circa jovem revolventium*). Stessa resa del Fascicolo 21 (controllato sul file consegnato). |
| *comites* (di Saturno); *comitari* | «satelliti»; «accompagnare» | Prop. VI (*saturni & comitum ejus*): resa fissata dal glossario, con nota alla prima occorrenza (N1). Nella Prop. I il verbo *qui saturnum comitantur* è reso «che accompagnano Saturno». |
| *respicere* (*centrum*) | «essere rivolto a» | Propp. I–III, V. Termine tecnico di Newton per la direzione di una forza centrale; Motte «tend to», «respect». |
| *retrahere a motibus rectilineis* | «distogliere dai moti rettilinei» | Enunciati delle Propp. I–V. |
| *gravitare in*; *gravis in*; *gravitatio* | «gravitare verso»; «grave verso»; «gravitazione» | *Gravitatio* compare una volta (Prop. VII, Cor. 2), distinta da *gravitas* «gravità». |
| *gravitas acceleratrix* | «gravità acceleratrice» | Prop. VI e XIII; parallelo a *vis acceleratrix* «forza acceleratrice». |
| *quantitas materiæ*; *copia materiæ*; *massa* | «quantità di materia»; «quantità di materia»; «massa» | *Copia materiæ* (Prop. VI, due volte; Prop. X) è sinonimo di *quantitas materiæ*: stessa resa, **dubbio segnalato** (si potrebbe distinguere con «copia di materia»). *Massa* (Prop. VI; Prop. X *massa fluida*) «massa». |
| *vires inertiæ*; *magnitudo* | «forze d’inerzia»; «grandezza» | Prop. VI, Cor. 4. *Magnitudines* sono i volumi; Motte «bulks». |
| *pyxis* | «scatola» | Prop. VI. Come nel Fascicolo 18b (*pyxis abiegna*). |
| *centrum oscillationis* | «centro di oscillazione» | Prop. VI; come nel Libro II. |
| *lunula*; *lunæ* (plurale) | «piccola luna»; «lune» (minuscolo) | Scolio della Prop. IV: lune ipotetiche, non la Luna. |
| *argumentum inductionis* | «argomento d’induzione» | Scolio della Prop. IV; cfr. *inductio* «induzione» (Regola IV). |
| *scrupulum* | «primo» | Prop. IV: *scrupulis quasi quatuor vel quinque*, minuti d’arco (Motte «minutes»). |
| *elongatio maxima heliocentrica* | «elongazione massima eliocentrica» | Prop. VIII, Cor. 1: l’angolo sotto cui il raggio dell’orbita del satellite si vedrebbe dal Sole. |
| *satelles extimus*; *satelles Hugenianus* | «satellite più esterno»; «satellite di Huygens» | Prop. VIII, Cor. 1. Il satellite di Huygens è il quarto dei cinque satelliti di Saturno del Fenomeno II (periodo 15 g 22 h 41′), oggi Titano (non verificato sulle fonti allegate). |
| *forma*; *textura* | «forma»; «tessitura» | Prop. VI, Cor. 1–2. |
| *rarefactio*; *pori*; *vacuum* | «rarefazione»; «pori»; «vuoto» | Prop. VI, Cor. 3–4. *Vacuum datur* «si dà il vuoto». |
| *vis magnetica*; *attractio magnetica / electrica* | «forza magnetica»; «attrazione magnetica / elettrica» | Prop. VI, Cor. 5; Prop. VII, Cor. 1. |
| *intendi & remitti* | «aumentare e diminuire» | Glossario del Libro III (Regola III), applicato alla Prop. VI, Cor. 5. |
| *thermometrum* | «termometro» | Prop. VIII, Cor. 4. |
| *fodinæ*; *terra communis suprema* | «miniere»; «la terra comune in superficie» | Prop. X. |
| *materia lucida solaris* | «materia luminosa del Sole» | Prop. X. |
| *stella jovis* | «l’astro di Giove» | Prop. X; Motte «the planet Jupiter». |
| *exhalationes*; *vapores* | «esalazioni»; «vapori» | Prop. X. |
| *vitrum cavum cylindricum* | «vaso di vetro cilindrico cavo» | Prop. X. Il latino non nomina la macchina pneumatica; Motte sì («air-pump», «receiver»). |
| *systema mundanum*; *centrum mundi* | «sistema del mondo»; «centro del mondo» | Ipotesi I, Propp. XI–XII. *Systema mundanum* ha la stessa resa di *systema mundi* (glossario). |
| *umbilicus inferior* | «fuoco inferiore» | Prop. XIII: il fuoco dell’ellisse occupato dal corpo centrale (qui dal centro di gravità di Giove e del Sole). |
| *motus menstruus* | «moto mensile» | Prop. XIII. |
| *refractio*; *tabulæ refractionum* | «rifrazione»; «tavole delle rifrazioni» | Prop. IV. |
| *Lutetia Parisiorum*; *Galli mensurantes* | «Parigi»; «i Francesi con le loro misure» | Prop. IV. |
| *digitus* (misura) | «pollice» | Prop. IV (*dig. 1.*). Glossario del Libro II; il «dito» del Libro III vale solo per le eclissi. |
| *tertia* (segno ‴) | «terzi» | Prop. VIII, Cor. 2: *10″. 30‴* = 10 secondi e 30 terzi (sessantesimi di secondo). |
| *aberratio* | «scostamento» | Prop. II: *aberratio quam minima a ratione duplicata*. |
| *quies apheliorum* | «quiete degli afeli» | Prop. II. |
| *vulgus* | «il volgo» | Prop. XII, Cor.: *uti vulgi est opinio*, «com’è opinione del volgo». |
| Nomi propri | Tolomeo, Wendelin, Huygens, Copernico, Street, Tycho, Keplero, Aristotele, Cartesio | *Vendelinus* «Wendelin» e *Streetus* «Street»: forme originali (Motte «Vendelin», «Street»); *Hugenius* «Huygens»; *Tycho* resta «Tycho» come nell’uso italiano; *Cartesius* «Cartesio». Identificazioni in nota N6 (non verificate sulle fonti allegate). |

*Hypothesis* compare come titolo (Ipotesi I) e nei rinvii *contra hypothesin* (Prop. XI, «contro l’Ipotesi», con la maiuscola perché rimanda all’Ipotesi I) e *in hypothesi quod terra quiescit* (Prop. IV, «nell’ipotesi», minuscolo: non è l’Ipotesi I). *Phænomena* senza numero (*ex phænomenis*, Prop. XIII) «fenomeni», minuscolo. *Vis centrifuga* compare una volta (Scolio della Prop. IV), «forza centrifuga».

### A.1 Proposizione I

**Latino:** *Vires, quibus planetæ circumjoviales perpetuo retrahuntur a motibus rectilineis & in orbibus suis retinentur, respicere centrum jovis, & esse reciproce ut quadrata distantiarum locorum ab eodem centro.*

**Inglese:** “That the forces by which the circumjovial planets are continually drawn off from rectilinear motions, and retained in their proper orbits, tend to Jupiter's centre; and are reciprocally as the squares of the distances of the places of those planets from that centre.”

**Scelte.**

- *distantiarum locorum ab eodem centro* → «delle distanze dei loro luoghi da quel centro»: i «luoghi» sono le posizioni dei satelliti. Motte esplicita «of the places of those planets».
- *PAtet* con due maiuscole è il capolettera tipografico, non un refuso.
- *per phænomenon primum* → «per il Fenomeno I»: rimando al Fascicolo 21 (latino in `latino-1726-L3-Regole-Fenomeni.md`, p. 390: aree proporzionali ai tempi e tempi nel rapporto sesquiplicato delle distanze). Verificato.

### A.2 Proposizione II

**Latino:** *Vires, quibus planetæ primarii perpetuo retrahuntur a motibus rectilineis, & in orbibus suis retinentur, respicere solem, & esse reciproce ut quadrata distantiarum ab ipsius centro.*

**Inglese:** “That the forces by which the primary planets are continually drawn off from rectilinear motions, and retained in their proper orbits, tend to the sun; and are reciprocally as the squares of the distances of the places of those planets from the sun's centre.”

**Scelte.**

- *per propositionem quartam ejusdem libri* → «per la Prop. IV dello stesso Libro»: il latino non indica il corollario (il Cor. 6, come nella Prop. I). Motte lo aggiunge (§ A.10).
- *Accuratissime autem demonstratur* → «si dimostra con la massima esattezza».
- *aberratio quam minima* → «uno scostamento anche piccolissimo». Nota N2.

### A.3 Proposizione III e Corollario

**Latino:** *Vim qua luna retinetur in orbe suo, respicere terram, & esse reciproce ut quadratum distantiæ locorum ab ipsius centro.*

**Inglese:** “That the force by which the moon is retained in its orbit tends to the earth; and is reciprocally as the square of the distance of its place from the earth's centre.”

**Corollario, latino:** *Si vis centripeta mediocris qua luna retinetur in orbe augeatur primo in ratione 177⁤2940 ad 178⁤2940, deinde etiam in ratione duplicata semidiametri terræ ad mediocrem distantiam centri lunæ a centro terræ: habebitur vis centripeta lunaris ad superficiem terræ, posito quod vis illa descendendo ad superficiem terræ perpetuo augeatur in reciproca altitudinis ratione duplicata.*

**Corollario, inglese:** “If we augment the mean centripetal force by which the moon is retained in its orb, first in the proportion of [SVG 964] to [SVG 963] , and then in the duplicate proportion of the semi-diameter of the earth to the mean distance of the centres of the moon and earth, we shall have the centripetal force of the moon at the surface of the earth; supposing this force, in descending to the earth's surface, continually to increase in the reciprocal duplicate proportion of the height.”

**Scelte.**

- *assertionis pars prior* → «la prima parte dell’asserzione» (il latino cambia qui *propositionis* in *assertionis*; si conserva).
- *graduum tantum trium & minutorum trium in consequentia* → «soltanto di tre gradi e tre primi in conseguenza». *In consequentia*: «in conseguenza», cioè nel verso del moto della Luna (glossario del Libro I; prima occorrenza nel fascicolo).
- *reciproce ut D2⁤4243* → «inversamente come D^(2 4/243)»: la trascrizione appiattisce l’esponente frazionario; la lettura è confermata da Motte [SVG 962] (2 4/243) e dal testo stesso (*cujus index est 2 4/243*). Nota N3.
- *partibus 59⁤34 propius ad duplicatam quam ad triplicatam accedit* → «si avvicina al duplicato 59 3/4 volte più che al triplicato»: Motte «comes 59 3/4 times nearer». Verificato: (3 − 2 4/243) : (2 4/243 − 2) = 239 : 4 = 59 3/4.
- *Oritur vero ab actione solis* → «Esso nasce invece dall’azione del Sole»: il soggetto è il moto dell’apogeo.
- *quatenus lunam distrahit a terra* → «in quanto allontana la Luna dalla Terra»; Motte «attracting the moon from the earth».
- *ut 2 ad 357,45 circiter, seu 1 ad 178⁤2940* → «come 2 sta a 357,45 circa, ossia come 1 sta a 178 29/40». Nota N4.
- *Et neglecta solis vi tantilla* → «trascurata una forza del Sole così piccola».
- Cor.: *augeatur primo in ratione 177⁤2940 ad 178⁤2940* → «si aumenta prima nel rapporto di 177 29/40 a 178 29/40»; *in ratione duplicata semidiametri terræ ad mediocrem distantiam* → «nel rapporto duplicato del semidiametro della Terra alla distanza media»: secondo l’uso di Newton, aumentare «nel rapporto di A a B» significa moltiplicare per B/A; il fattore è dunque (distanza/semidiametro)², come richiede il senso. Lasciato alla lettera, come fa Motte.
- La trascrizione ha *per corol 1.* senza punto dopo *corol* (§ A.7).

### A.4 Proposizione IV e Scolio

**Latino:** *Lunam gravitare in terram, & vi gravitatis retrahi semper a motu rectilineo, & in orbe suo retineri.*

**Inglese:** “That the moon gravitates towards the earth, and by the force of gravity is continually drawn off from a rectilinear motion, and retained in its orbit.”

**Scelte.**

- *in syzygiis* → «nelle sizigie» (congiunzione e opposizione; glossario).
- *idque scrupulis quasi quatuor vel quinque* → «e ciò di circa quattro o cinque primi»; Motte aggiunge «near the horizon» e, poco dopo, «horizontal parallax»: precisazioni corrette nel senso (si tratta della parallasse orizzontale), ma assenti nel latino (§ A.10).
- *hoc est, quasi duodecima vel decima quinta parte totius parallaxeos* → «cioè di circa un dodicesimo o un quindicesimo dell’intera parallasse». Verificato in N6.
- *uti a Gallis mensurantibus definitum est* → «come è stato determinato dai Francesi con le loro misure».
- *ut urgente vi illa omni … descendat* → «in modo da scendere … sotto l’azione di tutta quella forza»; *per corol. prop. iii.* → «per il Corollario della Prop. III». Il rimando è essenziale per il numero: il seno verso calcolato con 60 semidiametri dà 15,009 piedi, e solo moltiplicandolo per 178 29/40 : 177 29/40 (il Corollario) si ottiene il valore «più esatto» di 15 piedi, 1 pollice, 1 4/9 linee. Nota N5.
- *Colligitur hoc ex calculo … confecto* → «Ciò si ricava da un calcolo eseguito …».
- *sinus versus* → «seno verso»; *pedum 15. dig. 1. & lin. 1⁤49* → «15 piedi, 1 pollice e 1 4/9 linee» (*digitus* «pollice», A.0).
- *spatio minuti unius primi* / *minuti unius secundi* → «nello spazio di un minuto» / «di un secondo» (tempi: glossario del Libro III).
- *penduli … ad singula minuta secunda oscillantis* → «del pendolo che batte i secondi» (glossario); *linearum 8⁤12* → «8 1/2 linee» (Motte [SVG 643] = 1/2).
- *ut indicavit etiam Hugenius* → «come ha mostrato anche Huygens».
- *si descendatur in superficiem terræ* → «se si scende fino alla superficie della Terra» (impersonale).
- *per reg. i. & ii.* → «per le Regole I e II» (Fascicolo 21).
- *Calculus hic fundatur in hypothesi quod terra quiescit* → «Questo calcolo si fonda sull’ipotesi che la Terra sia in quiete»: «ipotesi» minuscolo (A.0).
- *manente lege gravitatis* → «restando la legge della gravità»; Motte omette (§ A.10).
- *uti computationem ineunti patebit* → «come risulterà a chi intraprenda il calcolo».
- La trascrizione ha *semidiamtrorum* (§ A.7).
- **Scolio.** *per argumentum inductionis* → «per l’argomento d’induzione»; *legem planetarum a Keplero detectam* → «la legge dei pianeti scoperta da Keplero»: è il rapporto sesquiplicato del Fenomeno IV, qui attribuito esplicitamente a Keplero. *per prop. i. hujus* → «per la Prop. I di questo Libro». *per computationem præcedentem* → «per il calcolo precedente». *defectu vis centrifugæ qua in orbe permanserat* → «per mancanza della forza centrifuga con cui era rimasta nell’orbita». *idque maxime ne lunula … vel gravitate careat, vel duplo velocius cadat* → «e ciò soprattutto perché la piccola luna … non debba o essere priva di gravità o cadere due volte più velocemente»: Motte «because otherwise …», che perde *maxime*.

### A.5 Proposizione V, corollari e Scolio

**Latino:** *Planetas circumjoviales gravitare in jovem, circumsaturnios in saturnum, & circumsolares in solem, & vi gravitatis suæ retrahi semper a motibus rectilineis, & in orbibus curvilineis retineri.*

**Inglese:** “That the circumjovial planets gravitate towards Jupiter; the circumsaturnal towards Saturn; the circumsolar towards the sun; and by the forces of their gravity are drawn off from rectilinear motions, and retained in curvilinear orbits.”

**Scelte.**

- *phænomena ejusdem generis* → «fenomeni dello stesso genere»; Motte «appearances of the same sort».
- *per reg. ii.* → «per la Regola II».
- *in recessu a terra* → «allontanandosi dalla Terra».
- Cor. 1: *Gravitas igitur datur in planetas universos* → «Esiste dunque una gravità verso tutti i pianeti». *per motus legem tertiam* → «per la terza legge del moto».
- Cor. 3: *sol & luna perturbant mare nostrum* → «il Sole e la Luna perturbano il nostro mare»: rimando alle maree (Prop. XXIV, gruppo G5), *ut in sequentibus explicabitur*.
- Scolio: *Eandem jam gravitatem esse constat* → «Ora è accertato che essa è la gravità»; Motte parafrasa («it being now made plain that it can be no other than a gravitating force»). *per reg. i, ii. & iv.* → «per le Regole I, II e IV».

### A.6 Proposizione VI e corollari

**Latino:** *Corpora omnia in planetas singulos gravitare, & pondera eorum in eundem quemvis planetam, paribus distantiis a centro planetæ, proportionalia esse quantitati materiæ in singulis.*

**Inglese:** “That all bodies gravitate towards every planet; and that the weights of bodies towards any the same planet, at equal distances from the centre of the planet, are proportional to the quantities of matter which they severally contain.”

**Scelte.**

- *dempta saltem inæquali retardatione* → «tolto almeno il ritardo disuguale».
- *jamdudum observarunt alii* → «lo hanno osservato altri già da tempo».
- *Rem tentavi* → «Ho messo alla prova la cosa»; *Comparabam … implebam … suspendebam* → imperfetti narrativi conservati («Prendevo … riempivo … sospendevo»).
- *quoad pondus, figuram, & aëris resistentiam omnino paria* → «del tutto uguali quanto al peso, alla figura e alla resistenza dell’aria».
- *ibant una & redibant diutissime* → «andavano e tornavano insieme per moltissimo tempo».
- *per corol. 1. & 6. prop. xxiv. Lib. II.* → «per i Cor. 1 e 6 della Prop. XXIV del Libro II». Verificato (§ A.9).
- *ut vis motricis actio in totum aurum ad ejusdem actionem in totum lignum* → «come l’azione della forza motrice su tutto l’oro sta alla sua azione su tutto il legno».
- *quæ vel minor esset quam pars millesima* → «che fosse anche minore della millesima parte».
- *parte 12000 distantiæ totius* → «di una duemillesima parte della distanza totale»: frazione appiattita, 1/2000 (Motte [SVG 975]).
- *pondera saturni & comitum ejus* → «i pesi di Saturno e dei suoi satelliti»: prima occorrenza di *comites* (nota N1).
- *vel nulla sunt, vel earum massis accurate proportionalia* → «o sono nulli, o sono esattamente proporzionali alle loro masse»; *Aliqua autem sunt* → «Ma qualche peso c’è».
- *pro genere partium quibus maximæ abundet* → «secondo il genere delle parti di cui è più ricco».
- Cor. 2: *ex mente Aristotelis, Cartesii & aliorum* → «secondo il pensiero di Aristotele, di Cartesio e di altri». *per reg. iii.* → «per la Regola III».
- Cor. 3: *argenti vivi* → «del mercurio (argento vivo)», prima occorrenza nel fascicolo.
- Cor. 4: *vacuum datur* → «si dà il vuoto»; Motte amplia («a void, space, or vacuum»).
- Cor. 5: *ex crassis quibusdam observationibus* → «da alcune osservazioni grossolane».
- La trascrizione spezza la frase *Proinde copia materiæ … Lib. II.)* dopo *xxiv.* e *Lib.* (artefatto della segmentazione, non del testo).

### A.7 Proposizione VII e corollari

**Latino:** *Gravitatem in corpora universa fieri, eamque proportionalem esse quantitati materiæ in singulis.*

**Inglese:** “That there is a power of gravity tending to all bodies, proportional to the several quantities of matter which they contain.”

**Scelte.**

- *Gravitatem in corpora universa fieri* → «Esiste una gravità verso tutti i corpi»; Motte «That there is a power of gravity tending to all bodies».
- *per prop. lxix. lib. i. & ejus corollaria* → «per la Prop. LXIX del Libro I e i suoi corollari». Verificato (§ A.9).
- *actioni omni reactio (per motus Legem tertiam) æqualis sit* → «(per la terza legge del moto) a ogni azione è uguale una reazione».
- Cor. 1: *in unum globum coire* → «si riuniscano in un solo globo» (*coire* «riunirsi», glossario del Libro I). Le due frasi *Cujus rei exempla …* e *Oritur enim …* sono unite con i due punti.
- Cor. 2: *Gravitatio* → «La gravitazione» (A.0). *per corol. 3. prop. lxxiv. lib. i.* → verificato.

### A.8 Proposizione VIII e corollari

**Latino:** *Si globorum duorum in se mutuo gravitantium materia undique in regionibus, quæ a centris æqualiter distant, homogenea sit: erit pondus globi alterutrius in alterum reciproce ut quadratum distantiæ inter centra.*

**Inglese:** “In two spheres mutually gravitating each towards the other, if the matter in places on all sides round about and equi-distant from the centres is similar, the weight of either sphere towards the other will be reciprocally as the square of the distance between their centres.”

**Scelte.**

- *materia undique in regionibus, quæ a centris æqualiter distant, homogenea* → «omogenea da ogni parte nelle regioni che distano ugualmente dai centri». Motte «similar» (§ A.10).
- *dubitabam an reciproca illa proportio duplicata obtineret accurate … an vero quam proxime* → «dubitavo se quella proporzione inversa duplicata valesse esattamente … o soltanto con ottima approssimazione».
- *intellexi veritatem propositionis* → «compresi la verità della proposizione».
- Cor. 1: *ut diametri circulorum directe & quadrata temporum periodicorum inverse* → «come i diametri dei cerchi direttamente e come i quadrati dei tempi periodici inversamente» (Libro I, Prop. IV, Cor. 2, che parla di raggi: per i rapporti è lo stesso). *computum ineundo inveni* → «facendo il calcolo ho trovato».
- Cor. 1: *in distantiis 10000, 997, 791 & 109 ab eorum centris, atque ideo in eorum superficiebus* → «alle distanze 10000, 997, 791 e 109 dai loro centri, e perciò alle loro superfici»: i numeri sono i diametri in proporzione, ripresi nel Cor. 3 (*veræ … diametri*).
- Cor. 2: *10″. 30‴* → «10″ 30‴» (secondi e terzi, A.0). *in triplicata ratione* → «nel rapporto triplicato».
- Cor. 3: *applicata ad sphærarum diametros* → «divisi per i diametri delle sfere» (*applicare ad* «dividere per»). *Nam per ingentem suum calorem sol rarescit* → «Infatti il Sole, per il suo enorme calore, si rarefà»; Motte «is kept in a sort of a rarefied state».
- Cor. 4: *ut quilibet pro gradu densitatis calore solis majore vel minore frueretur* → «perché ciascuno, secondo il grado della sua densità, godesse di un calore del Sole maggiore o minore». *rigesceret* → «gelerebbe». *septuplo solis æstivi calore* → «con un calore sette volte quello del Sole d’estate».
- Il rimando *in sequentibus* sulla gravità alla superficie della Luna e sulla sua densità rimanda alla Prop. XXXVII, Cor. 3–5 (gruppo G6, latino p. 469: *gravitas acceleratrix in superficie lunæ erit quasi triplo minor*). Verificato sul latino.

### A.9 Propp. IX–XIV, Ipotesi I, Scolio della Prop. XIV

**Prop. IX, latino:** *Gravitatem pergendo a superficiebus planetarum deorsum decrescere in ratione distantiarum a centro quam proxime.* — **inglese:** “That the force of gravity, considered downward from the surface of the planets, decreases nearly in the proportion, of the distances from their centres.”

**Prop. X, latino:** *Motus planetarum in cœlis diutissime conservari posse.* — **inglese:** “That the motions of the planets in the heavens may subsist an exceedingly long time.”

**Ipotesi I, latino:** *Centrum systematis mundani quiescere.* — **inglese:** “That the centre of the system of the world is immovable.”

**Prop. XI, latino:** *Commune centrum gravitatis terræ, solis & planetarum omnium quiescere.* — **inglese:** “That the common centre of gravity of the earth, the sun, and all the planets, is immovable.”

**Prop. XII, latino:** *Solem motu perpetuo agitari, sed nunquam longe recedere a communi gravitatis centro planetarum omnium.* — **inglese:** “That the sun is agitated by a perpetual motion, but never recedes far from the common centre of gravity of all the planets.”

**Prop. XIII, latino:** *Planetæ moventur in ellipsibus umbilicum habentibus in centro solis, & radiis ad centrum illud ductis areas describunt temporibus proportionales.* — **inglese:** “The planets move in ellipses which have their common focus in the centre of the sun; and, by radii drawn, to that centre, they describe areas proportional to the times of description.”

**Prop. XIV, latino:** *Orbium aphelia & nodi quiescunt.* — **inglese:** “The aphelions and nodes of the orbits of the planets are fixed.”

**Scelte.**

- Prop. IX: *pergendo a superficiebus planetarum deorsum* → «procedendo dalle superfici dei pianeti verso il basso»; *ab inæquabili densitate* → «dalla densità non uniforme».
- Prop. X: *diutissime* → «per lunghissimo tempo». *globus aquæ congelatæ* → «un globo d’acqua congelata». *partem 14586* → «1/4586» (Motte [SVG 918]). *Et in formatione qualicunque planetarum* → «E in qualunque modo si siano formati i pianeti» (resa per senso). *pro gradu levitatis* → «secondo il grado della sua leggerezza». *in ratione ponderis ac densitatis* → «nel rapporto del peso e della densità»; Motte «weight or density». *partem decimam centesimam millesimam* → «la milionesima parte»: letteralmente «la decima parte della centomillesima»; Motte «the 1000000th part». *ipsum aurum & pluma tenuissima* → «lo stesso oro e una piuma sottilissima». Motte divide il capoverso in due.
- Ipotesi I: *Centrum systematis mundani quiescere* → «Il centro del sistema del mondo è in quiete». La trascrizione ha *alli solem* per *alii* (§ A.7).
- Prop. XI: *per legum corol. iv.* → «per il Cor. IV delle leggi» (Fascicolo 3, Corollario IV: il centro comune di gravità di più corpi non cambia il suo stato di moto per le azioni reciproche). *contra hypothesin* → «contro l’Ipotesi».
- Prop. XII: *paulo supra superficiem solis* → «un poco al di sopra della superficie del Sole» (Motte «a little without»); *vix integra solis diametro … distaret* → «disterebbe … appena un intero diametro del Sole». Cor.: *pro centro mundi habendum est* → «va considerato come il centro del mondo»; *si modo sol densior esset & major* → «se soltanto il Sole fosse più denso e più grande».
- Prop. XIII: *umbilicum habentibus in centro solis* → «che hanno un fuoco nel centro del Sole»: Motte «their common focus» (§ A.10). *motus cœlestes a priori* → «a priori i moti celesti». *ut ad eandem astronomi hæreant* → «che gli astronomi ne restano perplessi». *aphelium nunc promovetur nunc forte retrahitur* → «l’afelio ora avanza ora forse arretra». *per vices* → «a vicenda». *constituendo umbilicum inferiorem orbis ejus in communi centro gravitatis jovis & solis* → «ponendo il fuoco inferiore della sua orbita nel centro comune di gravità di Giove e del Sole». *16×81×302125* → «16×81×3021/25» (Motte [SVG 984]). *ellipsin circum solem in umbilico positum* → «un’ellisse attorno al Sole posto nel fuoco».
- Prop. XIV: *per prop. xi. lib. i. ut & orbium plana, per ejusdem libri prop. i.* → «per la Prop. XI del Libro I, come pure i piani delle orbite, per la Prop. I dello stesso Libro». Cor. 2: *Quinimo* → «Anzi»; *æqualiter dispersæ* → «disperse ugualmente» (Motte «promiscuously»).
- Scolio: *nisi quatenus* → «se non in quanto» (glossario); *corporum superiorum* → «dei corpi superiori»; *in proportione sesquiplicata* → «nella proporzione sesquiplicata». La trascrizione ha *in annis centrum* (seconda occorrenza) per *centum* (§ A.7).

### A.10 Riepilogo: dove Motte aggiunge, omette o sbaglia

| Luogo | Latino | Motte 1846 | Tipo |
|---|---|---|---|
| III.G2.05 | *per … propositionem quartam* | «Cor. 6, Prop. IV» | aggiunta del corollario |
| III.G2.07 | *quatenus lunam distrahit a terra* | «attracting the moon from the earth» | parafrasi |
| III.G2.10 | *scrupulis quasi quatuor vel quinque* | «four or five minutes near the horizon» | aggiunta («near the horizon») |
| III.G2.10 | *auxerunt parallaxin lunæ* | «increase the moon's horizontal parallax» | aggiunta («horizontal») |
| III.G2.10 | *distantiam mediocrem sexaginta semidiametrorum* | «the mean distance of 60 diameters» | **errore** (diametri per semidiametri) |
| III.G2.10 | *æqualis evadit vi gravitatis apud nos* | «equal to the force of gravity which we observe in heavy bodies there» | ampliamento |
| III.G2.11 | *manente lege gravitatis* | — | **omissione** |
| III.G2.11 | *60⁤12 … circiter* | «60½» | omissione di *circiter* |
| III.G2.11 | due frasi (*uti computationem ineunti patebit. Computatio autem …*) | una frase («as may be found by a computation from Prop. LX») | fusione |
| III.G2.12 | *defectu vis centrifugæ qua in orbe permanserat* | «deserted by its centrifugal force that carries it through its orb» | parafrasi |
| III.G2.12 | *idque maxime ne* | «because otherwise» | omissione di *maxime* |
| III.G2.14 | *phænomena* | «appearances» | resa diversa |
| III.G2.18 | *Eandem jam gravitatem esse constat* | «it being now made plain that it can be no other than a gravitating force» | parafrasi |
| III.G2.20 | *æqualibus temporibus fieri* | «from equal heights in equal times» | aggiunta («from equal heights») |
| III.G2.20 | *vis motricis* | «motive force (or vis motrix)» | aggiunta del latino |
| III.G2.20 | *in ratione illa d ad e* | «in the proportion of e to d» | termini invertiti (senso invariato) |
| III.G2.23 | *formam illius gradatim induendo* | «acquiring the first form of that body» | aggiunta («first») |
| III.G2.25 | *vacuum datur* | «a void, space, or vacuum must be granted» | ampliamento |
| III.G2.25 | *vires inertiæ … magnitudines* | «vires inertiæ … bulks» | latino lasciato |
| III.G2.32, III.G2.36 | *homogenea*; *homogeneorum … homogeneas*; *heterogenearum* | «similar»; «similar»; «dissimilar» | resa diversa |
| III.G2.37 | *calore solis majore vel minore frueretur* | «enjoy a greater or less proportion to the sun's heat» | parafrasi |
| III.G2.41 | *ex vitro cavo cylindrico diligentissime exhaustis* | «carefully exhausted by the air-pump from under the receiver» | aggiunta («air-pump», «receiver») |
| III.G2.41 | *ponderis ac densitatis* | «weight or density» | congiunzione cambiata |
| III.G2.41 | un capoverso | due capoversi | divisione |
| III.G2.49 | *umbilicum habentibus in centro solis* | «their common focus» | aggiunta («common») |
| III.G2.51 | *(paribus distantiis)* | «(at equal distances, Cor. 2, Prop. VIII)» | aggiunta del rimando |
| III.G2.51 | *nunc forte retrahitur* | «sometimes backward» | omissione di *forte* |
| III.G2.55 | *Quinimo*; *æqualiter dispersæ* | «Not to mention that»; «promiscuously dispersed» | resa diversa |

Nessun errore di numeri in Motte in questo fascicolo, salvo la svista «60 diameters». Tutte le cifre delle Propp. IV, VI, VIII, X, XII, XIII e dello Scolio della Prop. XIV coincidono con il latino.

**SVG di Motte.** Ho controllato tutti i **27** marcatori del fascicolo (241, 643, 918, 961–984) sul LaTeX di `svg_tex.tsv`: 26 tornano con il latino (letto come frazioni appiattite, § A.7). **SVG di Motte che non tornano con il latino:**

| n | LaTeX | Lettura attesa | Commento |
|---|---|---|---|
| 961 | `\mathrm{D}^{2}\tfrac{4}{243}` | D^{2 4/243} (tutto l’esponente in apice) | Nel LaTeX solo il «2» è all’esponente e 4/243 sta sulla riga: è probabilmente un difetto della trascrizione LaTeX dell’EPUB e non della stampa, ma la formula letta alla lettera vale D² · 4/243. Da controllare sull’immagine. |

### A.11 Frazioni appiattite, refusi e anomalie della trascrizione

**Frazioni appiattite** (lettura confermata dagli SVG di Motte): *D2⁤4243* = D^(2 4/243) [961]; *2⁤4243* = 2 4/243 [962]; *59⁤34* = 59 3/4 [241]; *178⁤2940* = 178 29/40 [963]; *177⁤2940* = 177 29/40 [964]; *60⁤13* = 60 1/3 [965]; *60⁤25* = 60 2/5 [966]; *56⁤12* = 56 1/2 [967]; *60⁤12* = 60 1/2 [968]; *15⁤112* = 15 1/12 [969]; *1⁤49* = 1 4/9 [970]; *8⁤12* = 8 1/2 [643]; *1⁤79* = 1 7/9 [972]; *30⁤16* = 30 1/6 [973]; *14586* = 1/4586 [918]; *12000* = 1/2000 [975]; *16⁤34* = 16 3/4 [976]; *16⁤815* = 16 8/15 [977]; *22⁤23* = 22 2/3 [978]; *11067* = 1/1067 [979]; *13021* = 1/3021 [980]; *1169282* = 1/169282 [981]; *94⁤12* = 94 1/2 [982]; *13⁤35* = 13 3/5 [983]; *16×81×302125* = 16×81×3021/25 [984]. La *millesima* (1/1000) del latino è scritta in parole; Motte [974].

| Luogo | Trascrizione | Lettura | Tipo |
|---|---|---|---|
| III.G2.02 | *PAtet* | *Patet* | capolettera tipografico, non refuso |
| III.G2.07 | *per corol 1.* | *corol. 1.* | punteggiatura |
| III.G2.10 | *semidiamtrorum* | *semidiametrorum* | refuso probabile della trascrizione |
| III.G2.37 | *mer ‹406› curii* | *mercurii* | parola divisa dal cambio di pagina |
| III.G2.41 | *præter aërem exhalationes & vapores* | *aërem, exhalationes* | virgola mancante (punteggiatura) |
| III.G2.43 | *alli solem* | *alii* | refuso probabile |
| III.G2.50 | *in se motuo* (due volte) | *in se mutuo* | refuso probabile |
| III.G2.51 | *In conjuctione* | *conjunctione* | refuso probabile |
| III.G2.56 | *in annis centrum* | *centum* | refuso probabile |

**Punti da controllare sulla stampa ECCO.**

| Pagina 1726 | Trascrizione | Lettura attesa | Motivo |
|---|---|---|---|
| p. 396 | *per corol 1. prop. xlv.* | *corol. 1.* | punto mancante |
| p. 397 | *semidiamtrorum* | *semidiametrorum* | lettera mancante |
| p. 404 | *veneris … dierum 224 & horarum 16⁤34* | 16 3/4 (confermato da Motte) | il Fenomeno IV dà 224,6176 giorni = 224 g 14 h 49 m, non 224 g 16 h 45 m (nota N8): verificare se la stampa ha la stessa cifra |
| p. 405 | *1169282* (1/169282) | da controllare | il calcolo con i dati del Cor. 1 dà 1/193600, coerente con il peso 435 e la densità 400 dello stesso corollario (nota N8) |
| p. 405 | *13021* (1/3021) | da controllare | il calcolo con i dati dà 1/3092 (nota N8); 3021 ritorna nelle Propp. XII e XIII, quindi è probabilmente la cifra di Newton |
| p. 407 | *aërem exhalationes & vapores* | *aërem, exhalationes* | virgola |
| p. 408 | *alli solem* | *alii* | doppia l |
| p. 409 | *in se motuo* (due volte) | *in se mutuo* | vocale |
| p. 410 | *In conjuctione* | *conjunctione* | lettera mancante |
| p. 411 | *in annis centrum* | *centum* | lettera in più |

Nessuno di questi punti è stato verificato sulla stampa del 1726. La traduzione segue il senso; la Parte B riporta il latino esatto della trascrizione.

### A.12 Rimandi

**Rimandi ai Libri I e II e alle Leggi (verificati sui fascicoli in `traduzione/`).**

| Luogo | Latino | Resa | Fascicolo, identificatore | Esito |
|---|---|---|---|---|
| III.G2.02, 07 | *prop. ii. vel iii. lib. i.* | Prop. II o III del Libro I | 5, S2.09; S2.15 | regge (aree proporzionali → forza centrale) |
| III.G2.02 | *corol. 6. prop. iv.* | Cor. 6 della Prop. IV | 5, S2.29 | regge (rapporto sesquiplicato ⇔ 1/r²) |
| III.G2.05 | *prop. ii. lib. i.*; *prop. iv.* | Prop. II; Prop. IV del Libro I | 5, S2.09; S2.22–S2.29 | regge (il corollario pertinente è il 6, non citato) |
| III.G2.05, 07 | *corol. 1. prop. xlv.* | Cor. 1 della Prop. XLV | 9, S9.21 | regge (forza come A^(nn/mm − 3)) |
| III.G2.07 | *corol. 2. prop. xlv.* | Cor. 2 della Prop. XLV | 9, S9.24 | regge, con la precisazione della nota N4 (nel Libro I la forza 1/357,45 dà 1° 31′ 28″, e Newton aggiunge che l’apside della Luna è circa due volte più veloce) |
| III.G2.10 | *prop. xxxvi. lib. i.* | Prop. XXXVI del Libro I | 8, S7.15 | regge (tempi di caduta da un luogo dato) |
| III.G2.10 | *corol. 9. prop. iv.* | Cor. 9 della Prop. IV | 5, S2.32 | regge (arco medio proporzionale fra diametro e caduta) |
| III.G2.11 | *prop. lx. lib. i.* | Prop. LX del Libro I | 10, S11.13 | regge (60 → 60,50 con la massa lunare della Prop. XXXVII, nota N5) |
| III.G2.15, 29 | *motus legem tertiam* | terza legge del moto | 3, Legge III | regge |
| III.G2.20 | *corol. 1. & 6. prop. xxiv. Lib. II.* | Cor. 1 e 6 della Prop. XXIV del Libro II | 17, II.S6.03; II.S6.08 | regge (tempi uguali → materia come i pesi; nel mezzo non resistente il peso comparativo) |
| III.G2.20 | *corol. 3. / corol. 2. prop. lxv. lib. i.* | Cor. 3 e 2 della Prop. LXV | 10, S11.34; S11.33 | reggono |
| III.G2.28 | *prop. lxix. lib. i. & ejus corollaria* | Prop. LXIX e corollari | 10, S11.67–S11.71 | regge (forze assolute come i corpi) |
| III.G2.31 | *corol. 3. prop. lxxiv.* | Cor. 3 della Prop. LXXIV | 11, Prop. LXXIV, Cor. 3 | regge |
| III.G2.33 | *prop. lxxv. & lxxvi.* | Propp. LXXV e LXXVI | 11, S12.18; S12.24 | reggono (la LXXVI tratta proprio le sfere omogenee per strati) |
| III.G2.34 | *corol. 2. Prop. iv. lib. i.* | Cor. 2 della Prop. IV | 5, S2.25 | regge (raggi direttamente, quadrati dei tempi inversamente) |
| III.G2.36 | *prop. lxxii. lib. i.* | Prop. LXXII | 11, S12.05 | regge (forza come il semidiametro, a densità e rapporto dati) |
| III.G2.39 | *prop. lxxiii. lib. i.* | Prop. LXXIII | 11, S12.10 | regge (forza interna come la distanza dal centro) |
| III.G2.41 | *scholio propositionis xl. lib. ii.* | Scolio della Prop. XL del Libro II | 18b, II.S7.127 | regge (1/4586, con acqua : aria = 860 : 1) |
| III.G2.41 | *scholio ad prop. xxii. lib. ii.* | Scolio della Prop. XXII del Libro II | 16, II.S5.28–II.S5.29 | **non torna**: lo Scolio della Prop. XXII nel testo del 1726 tratta altre leggi della gravità e della condensazione e la proporzionalità fra densità dell’aria e pressione, ma **non contiene** il calcolo dell’aria a 200 miglia né il rapporto 30 : 0,0000000000003998. Il calcolo segue dallo Scolio (densità in progressione geometrica), ma il numero non vi è stampato. Da controllare sulla stampa (forse il rimando è un residuo delle edizioni precedenti; non verificato sulle fonti allegate) |
| III.G2.45 | *legum corol. iv.* | Cor. IV delle leggi | 3, L18 | regge |
| III.G2.50 | *prop. i. & xi. & corol. 1. prop. xiii. lib. i.* | Propp. I e XI e Cor. 1 della Prop. XIII | 5, S2.01; 6, S3.01; S3.22 | reggono (il Cor. 1 della Prop. XIII: forza 1/r² → sezione conica con fuoco nel centro) |
| III.G2.50 | *prop. lxvi. lib. i.* | Prop. LXVI | 10, S11.35 | regge |
| III.G2.51 | *prop. lxvii. lib. i.* | Prop. LXVII | 10, S11.62 | regge (il corpo esterno attorno al centro di gravità dei due interni) |
| III.G2.53 | *prop. xi. lib. i.*; *prop. i.* | Prop. XI; Prop. I | 6, S3.01; 5, S2.01 | reggono (ellisse immobile; orbita piana) |
| III.G2.55 | *prop. lxx. lib. i.* | Prop. LXX | 11, S12.01 | regge per analogia: la LXX riguarda un corpuscolo dentro una superficie sferica uniforme, e Newton la applica alle stelle fisse distribuite «ugualmente» in tutte le direzioni |

Totale: **27 rimandi** ai Libri I e II e alle Leggi; **uno non torna** (Scolio della Prop. XXII del Libro II).

**Rimandi interni al Libro III.** Fenomeni I, II, IV, V, VI e Regole I–IV (Fascicolo 21, latino `L3-Regole-Fenomeni`: verificati sul latino); *corol. prop. iii.* (Prop. IV → III.G2.08); *prop. i. hujus* (Scolio della Prop. IV → III.G2.01); *corol. 1. & 2.* (Prop. V, Cor. 3); *corol. 1. & 3. prop. v.* (Prop. VI → III.G2.15, III.G2.17); *in corollario superiore* (Prop. VI, Cor. 2 → Cor. 1); *per corol. 2. prop. viii.* (Prop. XII → III.G2.35); *contra hypothesin* (Prop. XI → Ipotesi I); *in propositione sequente* (Prop. III → Prop. IV); *jam ante ostensum* (Prop. X → Prop. VIII, Cor. 3: «la Terra quattro volte più densa del Sole» e, per i numeri 400 e 94 1/2, circa quattro volte più densa di Giove). Rimandi in avanti: *uti posthac dicetur* (Prop. III: azione del Sole sull’apogeo, Propp. XXV ss., gruppo G5); *ut in sequentibus explicabitur* (Prop. V, Cor. 3: maree, Prop. XXIV); *dicetur in sequentibus*, *ut in sequentibus patebit* (Prop. VIII, Cor. 1 e 3: Prop. XXXVII, Cor. 3–5, gruppo G6). Il valore 178 29/40 della Prop. III torna nella Prop. XXV (gruppo G5: «ut 1000 ad 178725, seu 1 ad 178 29/40») come rapporto della forza solare ML alla forza centripeta della Luna, e il 60 1/2 della Prop. IV vi è richiamato (*Invenimus autem in propositione quarta*). Tutti reggono.

---

## Note editoriali e fisiche

Queste note sono aggiunte del presente fascicolo, non affermazioni tradotte da Newton. Le verifiche numeriche sono state eseguite con uno script Python (`tmp/22/verifica.py`). Ciò che proviene da conoscenza generale e non dalle fonti allegate è marcato «(non verificato sulle fonti allegate)».

### N1. «Pianeti circumgioviali» e «satelliti»

Newton chiama *planetæ* sia i pianeti che ruotano attorno al Sole (*primarii*, *circumsolares*) sia i corpi che ruotano attorno a Giove e Saturno (*circumjoviales*, *circumsaturnii*), cioè i **satelliti** (pianeti secondari). Nella Prop. VI compaiono entrambe le parole latine *satellites* e *comites* («compagni», da *comitari*, «accompagnare»): tutte e due sono rese «satelliti». Nel 1726 si conoscevano quattro satelliti di Giove e cinque di Saturno (Fenomeni I e II, Fascicolo 21).

### N2. Prop. II: perché la quiete degli afeli è la prova più esatta

Per il Cor. 1 della Prop. XLV del Libro I, se la forza va come 1/r^(2+ε), l’apside avanza a ogni rivoluzione di circa 180·ε gradi (per orbite quasi circolari). Con ε = 0,01 si avrebbero 1,8° per giro: in cento rivoluzioni di Marte, 180°. È questo il senso di «notevole in ogni singola rivoluzione, enorme in molte». L’immobilità degli afeli osservata nei secoli fissa dunque l’esponente 2 con grande precisione.

### N3. Prop. III: l’esponente 2 4/243

Per il Cor. 1 della Prop. XLV del Libro I, se l’apside torna dopo un angolo che sta a 360° come m sta a n, la forza è come A^(nn/mm − 3). Con un avanzamento di **3° 3′** per rivoluzione si ottiene un indice 2,01673 = 2 + 1/59,8, e il rapporto (3 − indice) : (indice − 2) vale 58,77. Il valore di Newton, 2 4/243 = 2,01646, corrisponde invece esattamente a un avanzamento di **3° 0′**: con m : n = 121 : 120 l’indice è 2 + 241/14641, e 241/14641 = 4/243,0 con quattro cifre; il rapporto (3 − indice) : (indice − 2) è 14400/241 = 59,75 = **59 3/4**. Newton ha dunque arrotondato a 3° il moto dell’apogeo per il calcolo. La differenza (1,6% sulla parte decimale) non cambia l’argomento. Nel testo la cifra non è corretta.

### N4. Prop. III: la forza del Sole come 2 a 357,45

Il Cor. 2 della Prop. XLV del Libro I (Fascicolo 9, S9.24) calcola che una forza estranea sottratta, proporzionale alla distanza e pari a 1/357,45 della forza centrale, fa avanzare l’apside di 1° 31′ 28″ a ogni giro, e aggiunge: «L’apside della Luna è circa due volte più veloce». Nella Prop. III Newton scrive che l’azione del Sole sta alla forza centripeta della Luna «come 2 sta a 357,45», cioè come 1 a 178,725. Verifiche:

- 357,45 : 2 = 178,725 = 178 29/40 ✓;
- 178,725 è il quadrato del rapporto fra l’anno siderale e il mese siderale: (365 g 6 h 9 m : 27 g 7 h 43 m)² = 178,725 ✓ (è il calcolo esplicito della Prop. XXV, gruppo G5);
- con la formula del Cor. 2, c = 1/178,725 dà un avanzamento di 3° 4,7′ per giro; il valore che dà esattamente 3° 3′ è c = 1/180,3.

Il raddoppio è quindi coerente con il moto osservato dell’apogeo. Nel Libro I il valore 1/357,45 era proposto come esempio, seguito dall’osservazione che l’apside della Luna è circa due volte più veloce; qui Newton ricava la forza dal moto osservato «per ciò che si dice» nel Cor. 2, cioè scegliendo la forza che dà il doppio del moto. Il problema del moto dell’apogeo lunare, che la teoria di Newton spiega solo per metà al primo ordine, fu risolto da Clairaut nel 1749 (non verificato sulle fonti allegate). Il testo non va corretto: la nota serve al lettore per capire da dove vengono i numeri.

### N5. Prop. IV: la «prova della Luna» rifatta con i numeri di Newton

| Grandezza | Calcolo | Newton |
|---|---|---|
| raggio della Terra | 123249600 / 2π = 19615783 piedi parigini | — |
| periodo siderale | 27 g 7 h 43 m = 39343 minuti | — |
| seno verso dell’arco di 1 minuto a 60 raggi | 60 R (1 − cos(2π/39343)) = **15,0090** piedi | «circa 15 1/12» = 15,0833 |
| lo stesso, aumentato nel rapporto 178 29/40 : 177 29/40 (Cor. della Prop. III) | 15,0090 × 1,005627 = **15,0934** piedi | «15 piedi 1 pollice 1 4/9 linee» = 15,0934 ✓ |
| caduta in 1 secondo dal pendolo | L = 3 piedi 8 1/2 linee = 3,05903 piedi; π²L/2 = **15,0957** piedi | «15 piedi 1 pollice 1 7/9 linee» = 15,0957 ✓ |
| doppio di 15 1/12 | 30,1667 | «30 1/6» ✓ |
| distanza corretta per il moto attorno al centro comune (Prop. LX) | 60 × (1 + 1/39,788)^(1/3) = **60,50** | «60 1/2» ✓ |

(1 piede = 12 pollici, 1 pollice = 12 linee.) Il risultato più esatto del primo calcolo (1 4/9 linee) coincide con quello del secondo (1 7/9 linee) entro 1/3 di linea, cioè entro due parti su diecimila: è l’uguaglianza su cui poggia la proposizione. Il valore «15 1/12» è l’arrotondamento al dodicesimo di piede (un pollice) del valore aumentato; il seno verso «nudo» è 15 piedi e 1,3 linee. Il rimando al Corollario della Prop. III (*urgente vi illa omni*) è dunque essenziale: la forza «tutta» è quella con l’azione del Sole restituita. La massa lunare 1/39,788 viene dalla Prop. XXXVII, Cor. 4 (gruppo G6) e la stessa Prop. XXXVII, Cor. 7 rifà questo calcolo con altri dati (14,7706353 piedi in un minuto; latino G6, p. 469).

**Valori moderni** (non verificati sulle fonti allegate): il piede parigino vale 0,3248 m; la caduta in 1 s con g = 9,81 m/s² è 4,905 m = 15,10 piedi parigini, in accordo con Huygens. Lo stesso controllo, fatto in classe in unità SI con R = 6,37 × 10⁶ m e T = 27,32 giorni, dà un’accelerazione centripeta della Luna di 2,72 × 10⁻³ m/s², cioè g/3600 entro l’1%.

### N6. Prop. IV: la distanza della Luna e l’errore di Tycho

La parallasse orizzontale è l’angolo sotto cui si vede dalla Luna il raggio terrestre: a 56 1/2 raggi vale 60,8′, a 60 raggi 57,3′, a 60 1/2 raggi 56,8′. Togliere 4′ o 5′ alla parallasse di Tycho significa correggerla di 1/15,2 o 1/12,2 (Newton: «un dodicesimo o un quindicesimo» ✓) e porta la distanza a 60,5 o 61,6 raggi: con 4′ si ottiene proprio «circa 60 1/2». Identificazioni (non verificate sulle fonti allegate): Godefroy Wendelin (1580–1667), astronomo fiammingo; Thomas Streete (1621–1689), autore della *Astronomia Carolina*; la misura francese della circonferenza terrestre è quella di Jean Picard (1669–1670); il valore moderno della distanza media Terra–Luna è 60,27 raggi equatoriali.

### N7. Prop. VI: pendoli, satelliti e la sensibilità di 1/1000

**I pendoli.** Due pendoli di uguale lunghezza, uguale forma e uguale resistenza dell’aria oscillano insieme solo se la forza motrice (il peso) sta alla quantità di materia nello stesso rapporto nei due corpi: è il Cor. 1 della Prop. XXIV del Libro II. Un difetto di 1/1000 nel rapporto peso/massa cambierebbe il periodo di 1/2000 (T ∝ √(m/P)) e dopo circa 1000 oscillazioni i due pendoli sarebbero sfasati di mezza oscillazione: per questo la differenza «si sarebbe potuta scoprire chiaramente». Gli esperimenti moderni del tipo di Eötvös hanno spinto la verifica oltre 10⁻¹³ (non verificato sulle fonti allegate).

**I satelliti.** Se un satellite fosse attratto dal Sole più di Giove nel rapporto d : e, il centro della sua orbita sarebbe spostato rispetto a Giove nel rapporto √(d/e). Con d : e = 1001 : 1000, √1,001 − 1 = 0,000500 = 1/2000 ✓. L’elongazione del quarto satellite, 8′ 16″, dà distanza di Giove dal Sole : distanza del satellite = 1/tan 8′ 16″ = 415,9; quindi 1/2000 della distanza di Giove è 415,9/2000 = 0,208 della distanza del satellite: «un quinto» ✓.

### N8. Prop. VIII, Cor. 1–2: le masse ricalcolate

Con il Cor. 2 della Prop. IV del Libro I, la massa di ogni corpo centrale è proporzionale a a³/T², dove *a* è il raggio dell’orbita del satellite (o del pianeta) e T il tempo periodico. I raggi si ricavano dalle elongazioni eliocentriche e dalle distanze medie del Fenomeno IV (Venere 0,72333, Giove 5,20096, Saturno 9,54006, Terra 1, in unità della distanza Terra–Sole).

| Corpo | Dati di Newton | Massa ricalcolata (Sole = 1) | Newton |
|---|---|---|---|
| Giove | 16 g 16 8/15 h; 8′ 16″ a 5,20096 | **1/1067,2** | 1/1067 ✓ |
| Saturno | 15 g 22 2/3 h; 3′ 4″ a 9,54006 | **1/3091,7** | 1/3021 (scarto 2,3%) |
| Terra | 27 g 7 h 43 m; 10′ 33″ a 1 | **1/193589** | 1/169282 (scarto 14%) |

Il riferimento è Venere (224 g 16 3/4 h a 0,72333). Il tempo periodico di Venere del Cor. 1 (224,698 giorni) **differisce** di 1,9 ore da quello della tabella del Fenomeno IV (224,6176 giorni); l’effetto sulle masse è di sette parti su diecimila, trascurabile.

**I pesi alle superfici.** Con le masse di Newton e i diametri 10000, 997, 791, 109, i pesi g ∝ M/D² risultano 10000, 942,9, 529,0 e **497,2**. I primi tre tornano con 943 e 529; il quarto **non torna** con 435. Ma 435 è esattamente il peso che si ottiene con la massa terrestre ricalcolata dai dati (1/193490), e con 435 tornano anche le densità del Cor. 3. In altre parole: nel Cor. 1 il peso 435 e la densità 400 sono coerenti con i dati, mentre il numero 1/169282, ripetuto nel Cor. 2, non lo è. La cifra non è corretta nel testo; è segnalata nel § A.11 come punto da controllare sulla stampa. (Si ottiene 1/169282 con un diametro terrestre di 116,5 invece di 109, o con un’elongazione della Luna di 11′ 2″ invece di 10′ 33″: nessuna delle due grandezze è nel testo.)

**La parallasse solare.** L’elongazione eliocentrica della Luna, 10′ 33″ = 633″, divisa per la parallasse solare 10″ 30‴ = 10,5″, dà 60,29 raggi terrestri: è la distanza della Luna vista dal Sole, e lega la massa terrestre alla parallasse. Poiché la massa è come a³ e *a* (in unità della distanza Terra–Sole) è proporzionale alla parallasse, la massa della Terra va come il cubo della parallasse (Cor. 2 ✓). Con la parallasse moderna 8,794″ (non verificato sulle fonti allegate) il valore ricalcolato 1/193589 diventa 1/329500, vicino al valore moderno 1/332946; quello stampato, 1/169282, diventerebbe 1/288200.

**Valori moderni** delle masse (non verificati sulle fonti allegate): Giove 1/1047,3, Saturno 1/3497,9 del Sole.

### N9. Prop. VIII, Cor. 3: le densità

Densità ∝ peso alla superficie / diametro: 943/997 = 0,946; 529/791 = 0,669; 435/109 = 3,991 → **100, 94,6, 66,9, 399,1** (Newton 100, 94 1/2, 67, 400 ✓). La densità della Terra non dipende dalla parallasse del Sole perché sia la massa sia il volume della Terra, in unità solari, vanno come il cubo della parallasse. Densità moderne (non verificate sulle fonti allegate): Sole 1,41, Giove 1,33, Saturno 0,69, Terra 5,51 g/cm³, cioè 100, 94, 49, 391 in scala Sole = 100: i valori di Newton per Giove e la Terra sono sorprendentemente vicini.

### N10. Prop. VIII, Cor. 4: la luce sette volte più densa

L’intensità della luce solare va come l’inverso del quadrato della distanza: all’orbita di Mercurio (0,38710) è (1/0,38710)² = 6,67 volte quella sulla Terra, «sette volte» ✓. L’idea che i pianeti siano collocati secondo la loro densità perché ciascuno goda del calore adatto è un argomento di finalità, non una deduzione dalla gravità.

### N11. Prop. X: i numeri della resistenza

- **459 semidiametri in 30 giorni.** Con i dati del Fenomeno IV (distanza 5,20096, periodo 4332,514 giorni) Giove percorre in 30 giorni 0,2263 unità; con il diametro di Giove del Fenomeno I (37 1/4″ alla distanza media) il semidiametro vale 0,000470 unità, e il percorso è di **482** semidiametri. Il numero 459 corrisponde a un diametro di 39″ (460 semidiametri), il valore «più frequente» del micrometro citato nel Fenomeno I. La cifra non torna con il diametro adottato nel Fenomeno I; non è corretta nel testo.
- **«Quasi la decima parte».** 459 × 1/4586 = 0,1001 ✓ (ragionamento lineare per un corpo della densità dell’acqua).
- **L’aria a 200 miglia.** 30 / 0,0000000000003998 = 7,504 × 10¹³ ✓ («75000000000000 a 1»). Il rimando allo Scolio della Prop. XXII del Libro II non trova il numero nel testo del 1726 (§ A.12).
- **Un milione di anni.** Giove percorre circa 5,6 × 10⁹ semidiametri in un milione di anni; con la perdita 1/4586 per semidiametro nell’aria, ridotta di 7,5 × 10¹³, la perdita stimata linearmente è 1,6 × 10⁻⁸, molto meno di un milionesimo ✓.
- **Densità della Terra.** «Cinque o sei volte» l’acqua: il valore moderno 5,51 (non verificato sulle fonti allegate) cade nell’intervallo; è una stima, non una misura.

### N12. Prop. XII: il baricentro del Sistema solare

Dai dati del fascicolo il raggio del Sole vale 0,00471 unità della distanza Terra–Sole (diametro di Giove 37 1/4″ a 5,20096 e rapporto dei diametri 10000 : 997). La distanza di Giove dal Sole è allora **1104** raggi solari, «un poco maggiore» di 1067: il baricentro Sole–Giove cade a 1,03 raggi dal centro del Sole, appena fuori della superficie ✓. La distanza di Saturno è **2025** raggi solari, molto minore di 3021 (Newton: «un poco minore»): il baricentro Sole–Saturno cade a 0,67 raggi dal centro, un terzo del raggio sotto la superficie. La conclusione qualitativa regge, l’espressione «un poco» è generosa. Con Giove, Saturno e la Terra tutti da una parte, il baricentro dista 0,85 diametri solari dal centro del Sole: «appena un intero diametro» ✓ (gli altri pianeti aggiungono pochissimo).

### N13. Prop. XIII: Giove e Saturno

Distanza Saturno–Giove : distanza Saturno–Sole in congiunzione = (9,54 − 5,20) : 9,54 = 0,455, «quasi come 4 a 9» (0,444) ✓. 81/(16 × 1067) = 1/210,8 ✓ («1 a 211»). 16 × 81 × 3021/25 = 156608,6 ✓ (156609); 156609/65 = 2409,4 ✓. Il rapporto 16 : 81 : 16 × 81 × 3021/25 si ottiene ponendo le distanze Sole–Saturno, Giove–Saturno e Giove–Sole uguali a 9, 4 e 5. Il grande effetto osservato («gli astronomi ne restano perplessi») è la «grande disuguaglianza» di Giove e Saturno, spiegata da Laplace nel 1785 con la quasi commensurabilità 5 : 2 dei periodi (non verificato sulle fonti allegate).

### N14. Scolio della Prop. XIV: il moto degli afeli

Con il moto dell’afelio di Marte di 33′ 20″ = 2000″ al secolo e la regola del rapporto sesquiplicato delle distanze del Fenomeno IV si ottengono: Terra 1063″ = **17′ 43″** (Newton 17′ 40″), Venere 654″ = **10′ 54″** (10′ 53″), Mercurio 256″ = **4′ 16″** (4′ 16″). Gli scarti sono di pochi secondi; probabilmente Newton ha usato distanze arrotondate. La regola di proporzionalità è una stima di Newton, non una legge delle perturbazioni: i moti moderni dei perieli sono di ordine diverso, per esempio circa 532″ al secolo per Mercurio dovuti agli altri pianeti (non verificato sulle fonti allegate).

### N15. Prop. VII, Cor. 1: perché non si avverte la gravità fra i corpi comuni

Il rapporto fra l’attrazione di un corpo di 1 kg a 1 m e quella della Terra è dell’ordine di 10⁻¹¹ (non verificato sulle fonti allegate): «molto minore di quella che si possa avvertire». La misura diretta (Cavendish, 1798) arrivò circa settant’anni dopo (non verificato sulle fonti allegate).

---

## Controllo della copertura

Pagine 1726 dai marcatori ‹n› della trascrizione (la Prop. I comincia a p. 395). Motte: estratto senza marcatori di pagina, «sezione corrispondente».

| Identificatori | Incipit latino | Contenuto | 1726 | Motte 1846 |
|---|---|---|---|---|
| III.G2.01–III.G2.03 | *Vires, quibus planetæ circumjoviales* | Prop. I | p. 395 | Prop. I |
| III.G2.04–III.G2.05 | *Vires, quibus planetæ primarii* | Prop. II | p. 395 | Prop. II |
| III.G2.06–III.G2.08 | *Vim qua luna retinetur* | Prop. III e Cor. | p. 396 | Prop. III, Cor. |
| III.G2.09–III.G2.11 | *Lunam gravitare in terram* | Prop. IV | pp. 396–398 | Prop. IV |
| III.G2.12 | *Demonstratio propositionis sic fusius* | Scolio della Prop. IV | p. 398 | Scholium |
| III.G2.13–III.G2.17 | *Planetas circumjoviales gravitare* | Prop. V, Cor. 1–3 | p. 399 | Prop. V, Cor. 1–3 |
| III.G2.18 | *Hactenus vim illam* | Scolio della Prop. V | p. 399 | Scholium |
| III.G2.19–III.G2.21 | *Corpora omnia in planetas singulos* | Prop. VI | pp. 400–402 | Prop. VI |
| III.G2.22–III.G2.26 | *Hinc pondera corporum non pendent* … *Vis gravitatis diversi est generis* | Prop. VI, Cor. 1–5 | pp. 402–403 | Cor. 1–5 |
| III.G2.27–III.G2.31 | *Gravitatem in corpora universa fieri* | Prop. VII, Cor. 1–2 | pp. 403–404 | Prop. VII, Cor. 1–2 |
| III.G2.32–III.G2.33 | *Si globorum duorum* | Prop. VIII | p. 404 | Prop. VIII |
| III.G2.34–III.G2.37 | *Hinc inveniri* … *Densiores igitur* | Prop. VIII, Cor. 1–4 | pp. 404–406 | Cor. 1–4 |
| III.G2.38–III.G2.39 | *Gravitatem pergendo a superficiebus* | Prop. IX | p. 406 | Prop. IX |
| III.G2.40–III.G2.41 | *Motus planetarum in cœlis* | Prop. X | pp. 406–407 | Prop. X (due capoversi) |
| III.G2.42–III.G2.43 | *Centrum systematis mundani* | Ipotesi I | p. 408 | Hypothesis I |
| III.G2.44–III.G2.45 | *Commune centrum gravitatis* | Prop. XI | p. 408 | Prop. XI |
| III.G2.46–III.G2.48 | *Solem motu perpetuo agitari* | Prop. XII e Cor. | pp. 408–409 | Prop. XII, Cor. |
| III.G2.49–III.G2.51 | *Planetæ moventur in ellipsibus* | Prop. XIII | pp. 409–410 | Prop. XIII |
| III.G2.52–III.G2.55 | *Orbium aphelia & nodi quiescunt* | Prop. XIV, Cor. 1–2 | p. 410 | Prop. XIV, Cor. 1–2 |
| III.G2.56 | *Cum planetæ soli propiores* | Scolio della Prop. XIV | p. 411 | Scholium |

**Controlli eseguiti.**

1. **Copertura frase per frase.** Ho segmentato la trascrizione in frasi con uno script (`tmp/22/seg.py`: 74 blocchi, 246 segmenti, comprese le intestazioni) e ho confrontato ogni frase con la traduzione, da *Vires, quibus planetæ circumjoviales* a *negliguntur in hac propositione*: nessuna frase manca. Le 122 frasi delle dimostrazioni sono anche nei passi della Parte B, e i capoversi corrispondenti della traduzione sono **generati dagli stessi passi** (stesso testo italiano). Due coppie di frasi brevi sono unite con i due punti (Prop. VII, Cor. 1; Prop. VIII, Cor. 4), senza omissioni. I 56 identificatori sono consecutivi e unici (controllo automatico).
2. **Parte B.** `check.py` sul file finale: JSON valido; tutte le stringhe `la` (enunciati e passi) sono sottostringhe esatte della trascrizione, estratte dallo script e non ricopiate a mano; tutte le stringhe `en` sono sottostringhe esatte di Motte; ogni identificatore di `copertura` è presente nel testo.
3. **Verifiche numeriche** (`tmp/22/verifica.py`): Prop. III (esponente, 59 3/4, 178 29/40, moto dell’apside: N3–N4); Prop. IV (seno verso, caduta dal pendolo, 30 1/6, parallasse di Tycho, Prop. LX: N5–N6); Prop. VI (1/2000 e «un quinto»: N7); Prop. VIII (masse, pesi, densità, Venere: N8–N10); Prop. X (459, 1/10, 7,5 × 10¹³, un milione di anni: N11); Prop. XII (baricentri: N12); Prop. XIII (4 : 9, 1/211, 156609, 2409: N13); Scolio della Prop. XIV (moti degli afeli: N14). **Cifre che non tornano** (non corrette nel testo): 2 4/243 e 59 3/4 corrispondono a 3° e non a 3° 3′ (N3); 1/169282 (e, meno, 1/3021) non segue dai dati del Cor. 1 della Prop. VIII, mentre il peso 435 sì (N8); 224 g 16 3/4 h per Venere contro 224,6176 g del Fenomeno IV (N8); 459 semidiametri di Giove corrispondono a un diametro di 39″, non ai 37 1/4″ del Fenomeno I (N11); «un poco minore» per Saturno nella Prop. XII (2025 contro 3021, N12).
4. **Tabelle numeriche.** Il fascicolo non contiene tabelle nel testo latino; i dati numerici della Prop. VIII sono raccolti nelle note N8–N9 e nel campo `dati` della Parte B.
5. **Motte.** Confronto di tutta la sezione corrispondente; divergenze nel § A.10; 27 SVG controllati, 1 da verificare.
6. **Separazione fra testo e commento.** Il testo tradotto non contiene formule moderne, eccetto la notazione D^(2 4/243) (Criteri).

**Non ho potuto verificare:**

- **la stampa del 1726**: i punti del § A.11 (in particolare 1/169282, 1/3021 e il periodo di Venere) restano da controllare;
- **la paginazione di Motte** e l’immagine dell’SVG 961;
- **lo Scolio della Prop. XXII del Libro II** nelle edizioni precedenti, per capire l’origine del rimando della Prop. X;
- **la terminologia del Fascicolo 21** oltre a «pianeti circumgioviali / circumsaturnii», che coincide: i titoli dei Fenomeni e delle Regole vanno armonizzati dal coordinatore;
- i **dati astronomici e storici** delle note marcate «(non verificato sulle fonti allegate)».

---

## Registro del lavoro successivo

| Unità | Stato |
|---|---|
| Libro III, Propp. I–XIV, Ipotesi I, scolî | **Fascicolo 22, presente documento, prima versione** |
| Refusi e cifre dubbie (§ A.11) | Da verificare sulla stampa del 1726 (scansione ECCO) |
| 1/169282 contro 435 (Prop. VIII, Cor. 1–2) | Da decidere dopo il controllo sulla stampa: nota N8 |
| Rimando allo Scolio della Prop. XXII del Libro II (Prop. X) | Da verificare (§ A.12) |
| SVG 961 | Da controllare sull’immagine |
| *copia materiæ* «quantità di materia» | Da decidere (A.0) |
| Pagine interattive | Parte B: la «prova della Luna» (L3-P4) è la candidata principale, con il confronto 1 4/9 – 1 7/9 linee; i pendoli (L3-P6); le masse e le densità (L3-P8-Cor1–Cor3, con il campo `dati`) |
| Revisione filologica e scientifica indipendente | Da eseguire |

Il presente testo è una nuova traduzione assistita da IA. Non riproduce traduzioni italiane o inglesi moderne. **Licenza prevista** (decisione del curatore, Fascicolo 3): testi e traduzioni CC BY-SA 4.0, codice MIT. La trascrizione latina è © The Newton Project; i testi di Motte sono di pubblico dominio.

---

## Parte B — Dati per le pagine interattive

Unità incluse (21): tutte le Propp. I–XIV, l’Ipotesi I (senza passi), il Corollario della Prop. III (senza passi), i Cor. 1–3 della Prop. VIII (calcoli delle masse e delle densità), lo Scolio della Prop. IV (argomento della piccola luna) e lo Scolio della Prop. XIV (calcolo dei moti degli afeli). Gli altri corollari e lo Scolio della Prop. V sono compresi nella `copertura` dell’unità della loro proposizione, senza passi propri. Il fascicolo non ha figure: `figura_base` manca e i campi `figura` descrivono gli elementi di un grafico o di un calcolo da mostrare.

Convenzioni:

- `la`: testo latino esatto della trascrizione, refusi e frazioni appiattite compresi; quando la trascrizione spezza una frase dopo un’abbreviazione («Corol. 1. Prop. xlv. Lib. i.»), i segmenti sono riuniti, come detto nella `nota`;
- `it`: la traduzione di questo fascicolo (identica al testo tradotto);
- `en`: Motte 1846, allineato per senso; i marcatori `[SVG n]` sono conservati (check.py li ignora);
- `dipende_da`: soltanto i rimandi citati nella frase latina;
- `figura.mostra` / `figura.evidenzia`: elementi del grafico o del calcolo da mostrare; relazioni da mettere in risalto;
- `dati`: valori numerici del testo e risultati dei controlli (note N5–N14).

```json
{
 "fascicolo": "22-L3-P01-14",
 "versione": "0.1",
 "data": "2026-11-08",
 "convenzioni": {
  "dipende_da": "solo rimandi citati esplicitamente nella frase latina",
  "en": "Motte 1846, allineato per senso; marcatori [SVG n] conservati",
  "figura.mostra": "elementi da rendere visibili al passo (grafico o calcolo: il fascicolo non ha figure), cumulativi salvo indicazione",
  "la": "",
  "dati": "valori del testo e risultati dei controlli di tmp/22/verifica.py"
 },
 "unita": [
  {
   "id": "L3-P1",
   "tipo": "Propositio/Theorema",
   "titolo": "Prop. I — le forze dei satelliti di Giove sono rivolte a Giove e inverse del quadrato",
   "copertura": [
    "III.G2.01",
    "III.G2.02",
    "III.G2.03"
   ],
   "fonti": {
    "la": "",
    "en": "Motte 1846, sezione corrispondente (Book III, Prop. I)"
   },
   "enunciato": {
    "la": "",
    "it": "Le forze con cui i pianeti circumgioviali sono continuamente distolti dai moti rettilinei e trattenuti nelle loro orbite sono rivolte al centro di Giove e sono inversamente come i quadrati delle distanze dei loro luoghi da quel centro.",
    "en": "That the forces by which the circumjovial planets are continually drawn off from rectilinear motions, and retained in their proper orbits, tend to Jupiter's centre; and are reciprocally as the squares of the distances of the places of those planets from that centre."
   },
   "passi": [
    {
     "id": "L3-P1-p1",
     "la": "",
     "it": "La prima parte della proposizione è evidente per il Fenomeno I e per la Prop. II o III del Libro I; la seconda parte per il Fenomeno I e per il Cor. 6 della Prop. IV dello stesso Libro.",
     "en": "The former part of this Proposition appears from Phæn. I, and Prop. II or III, Book I; the latter from Phæn. I, and Cor. 6, Prop. IV, of the same Book.",
     "dipende_da": [
      "Fenomeno I",
      "Libro I, Prop. II",
      "Libro I, Prop. III",
      "Libro I, Prop. IV, Cor. 6"
     ],
     "figura": {
      "mostra": [
       "Giove e i quattro satelliti",
       "raggi dal centro di Giove"
      ],
      "evidenzia": [
       "aree proporzionali ai tempi → forza verso il centro",
       "tempi nel rapporto sesquiplicato → forza ∝ 1/r²"
      ]
     }
    },
    {
     "id": "L3-P1-p2",
     "la": "",
     "it": "Lo stesso si intenda dei pianeti che accompagnano Saturno, per il Fenomeno II.",
     "en": "The same thing we are to understand of the planets which encompass Saturn, by Phæn. II.",
     "dipende_da": [
      "Fenomeno II"
     ],
     "figura": {
      "mostra": [
       "Saturno e i suoi satelliti"
      ],
      "evidenzia": [
       "stesso argomento"
      ]
     }
    }
   ]
  },
  {
   "id": "L3-P2",
   "tipo": "Propositio/Theorema",
   "titolo": "Prop. II — le forze dei pianeti primari sono rivolte al Sole e inverse del quadrato",
   "copertura": [
    "III.G2.04",
    "III.G2.05"
   ],
   "fonti": {
    "la": "",
    "en": "Motte 1846, sezione corrispondente (Prop. II)"
   },
   "enunciato": {
    "la": "",
    "it": "Le forze con cui i pianeti primari sono continuamente distolti dai moti rettilinei e trattenuti nelle loro orbite sono rivolte al Sole e sono inversamente come i quadrati delle distanze dal suo centro.",
    "en": "That the forces by which the primary planets are continually drawn off from rectilinear motions, and retained in their proper orbits, tend to the sun; and are reciprocally as the squares of the distances of the places of those planets from the sun's centre."
   },
   "passi": [
    {
     "id": "L3-P2-p1",
     "la": "",
     "it": "La prima parte della proposizione è evidente per il Fenomeno V e per la Prop. II del Libro I; la seconda parte per il Fenomeno IV e per la Prop. IV dello stesso Libro.",
     "en": "The former part of the Proposition is manifest from Phæn. V, and Prop. II, Book I; the latter from Phæn. IV, and Cor. 6, Prop. IV, of the same Book.",
     "dipende_da": [
      "Fenomeno V",
      "Fenomeno IV",
      "Libro I, Prop. II",
      "Libro I, Prop. IV"
     ],
     "figura": {
      "mostra": [
       "Sole",
       "orbite dei pianeti primari"
      ],
      "evidenzia": [
       "legge delle aree rispetto al Sole",
       "rapporto sesquiplicato dei tempi"
      ]
     },
     "nota": "Motte aggiunge «Cor. 6» alla Prop. IV; il latino cita la sola proposizione."
    },
    {
     "id": "L3-P2-p2",
     "la": "",
     "it": "Ma questa parte della proposizione si dimostra con la massima esattezza per mezzo della quiete degli afeli.",
     "en": "But this part of the Proposition is, with great accuracy, demonstrable from the quiescence of the aphelion points;",
     "dipende_da": [],
     "figura": {
      "mostra": [
       "afelio di un’orbita"
      ],
      "evidenzia": [
       "afelio fisso"
      ]
     }
    },
    {
     "id": "L3-P2-p3",
     "la": "",
     "it": "Infatti uno scostamento anche piccolissimo dal rapporto duplicato (per il Cor. 1 della Prop. XLV del Libro I) dovrebbe produrre un moto delle apsidi notevole in ogni singola rivoluzione, enorme in molte.",
     "en": "for a very small aberration from the reciprocal duplicate proportion would (by Cor. 1, Prop. XLV, Book I) produce a motion of the apsides sensible enough in every single revolution, and in many of them enormously great.",
     "dipende_da": [
      "Libro I, Prop. XLV, Cor. 1"
     ],
     "figura": {
      "mostra": [
       "orbita con apsidi mobili"
      ],
      "evidenzia": [
       "esponente 2+ε → precessione dell’apside a ogni giro"
      ]
     },
     "nota": "La trascrizione spezza la frase in tre segmenti dopo «Corol. 1.» e «Prop. xlv.»: qui sono riuniti."
    }
   ]
  },
  {
   "id": "L3-P3",
   "tipo": "Propositio/Theorema",
   "titolo": "Prop. III — la forza che trattiene la Luna è rivolta alla Terra e inversa del quadrato",
   "copertura": [
    "III.G2.06",
    "III.G2.07"
   ],
   "fonti": {
    "la": "",
    "en": "Motte 1846, sezione corrispondente (Prop. III)"
   },
   "enunciato": {
    "la": "",
    "it": "La forza con cui la Luna è trattenuta nella sua orbita è rivolta alla Terra ed è inversamente come il quadrato della distanza dei suoi luoghi dal centro della Terra.",
    "en": "That the force by which the moon is retained in its orbit tends to the earth; and is reciprocally as the square of the distance of its place from the earth's centre."
   },
   "passi": [
    {
     "id": "L3-P3-p1",
     "la": "",
     "it": "La prima parte dell’asserzione è evidente per il Fenomeno VI e per la Prop. II o III del Libro I; la seconda parte per il moto lentissimo dell’apogeo lunare.",
     "en": "The former part of the Proposition is evident from Phæn. VI, and Prop. II or III, Book I; the latter from the very slow motion of the moon's apogee;",
     "dipende_da": [
      "Fenomeno VI",
      "Libro I, Prop. II",
      "Libro I, Prop. III"
     ],
     "figura": {
      "mostra": [
       "Terra",
       "orbita lunare",
       "apogeo"
      ],
      "evidenzia": [
       "apogeo quasi fisso"
      ]
     }
    },
    {
     "id": "L3-P3-p2",
     "la": "",
     "it": "Infatti quel moto, che in ogni singola rivoluzione è soltanto di tre gradi e tre primi in conseguenza, si può trascurare.",
     "en": "which in every single revolution amounting but to 3° 3' in consequentia, may be neglected.",
     "dipende_da": [],
     "figura": {
      "mostra": [
       "avanzamento dell’apogeo di 3° 3′ a ogni giro"
      ],
      "evidenzia": [
       "moto in conseguenza"
      ]
     }
    },
    {
     "id": "L3-P3-p3",
     "la": "",
     "it": "È evidente infatti (per il Cor. 1 della Prop. XLV del Libro I) che, se la distanza della Luna dal centro della Terra sta al semidiametro della Terra come D sta a 1, la forza da cui nasce un tale moto è inversamente come D^(2 4/243), cioè inversamente come quella potenza di D il cui indice è 2 4/243; vale a dire in un rapporto della distanza un poco maggiore del duplicato inverso, ma che si avvicina al duplicato 59 3/4 volte più che al triplicato.",
     "en": "For (by Cor. 1, Prop. XLV, Book I) it appears, that, if the distance of the moon from the earth's centre is to the semi-diameter of the earth as D to 1, the force, from which such a motion will result, is reciprocally as [SVG 961] , i. e., reciprocally as the power of D, whose exponent is [SVG 962] ; that is to say, the proportion of the distance something greater than reciprocally duplicate, but which comes [SVG 241] times nearer to the duplicate than to the triplicate proportion.",
     "dipende_da": [
      "Libro I, Prop. XLV, Cor. 1"
     ],
     "figura": {
      "mostra": [
       "cursore: moto dell’apside per giro",
       "esponente della forza"
      ],
      "evidenzia": [
       "3° → indice 2 + 241/14641 ≈ 2 4/243 (nota N3)",
       "(3 − indice) : (indice − 2) = 59 3/4"
      ]
     },
     "nota": "La trascrizione appiattisce «D^{2 4/243}» in «D2⁤4243» e «59 3/4» in «59⁤34»; Motte [SVG 961], [SVG 962], [SVG 241]."
    },
    {
     "id": "L3-P3-p4",
     "la": "",
     "it": "Esso nasce invece dall’azione del Sole (come si dirà più avanti), e perciò qui va trascurato.",
     "en": "But in regard that this motion is owing to the action of the sun (as we shall afterwards shew), it is here to be neglected.",
     "dipende_da": [],
     "figura": {
      "mostra": [
       "Sole"
      ],
      "evidenzia": [
       "origine del moto dell’apogeo"
      ]
     }
    },
    {
     "id": "L3-P3-p5",
     "la": "",
     "it": "L’azione del Sole, in quanto allontana la Luna dalla Terra, è con ottima approssimazione come la distanza della Luna dalla Terra; e perciò (per ciò che si dice nel Cor. 2 della Prop. XLV del Libro I) sta alla forza centripeta della Luna come 2 sta a 357,45 circa, ossia come 1 sta a 178 29/40.",
     "en": "The action of the sun, attracting the moon from the earth, is nearly as the moon's distance from the earth; and therefore (by what we have shewed in Cor. 2, Prop. XLV, Book I) is to the centripetal force of the moon as 2 to 357,45, or nearly so; that is, as 1 to [SVG 963] .",
     "dipende_da": [
      "Libro I, Prop. XLV, Cor. 2"
     ],
     "figura": {
      "mostra": [
       "forza solare sottratta ∝ distanza"
      ],
      "evidenzia": [
       "2/357,45 = 1/178,725"
      ]
     }
    },
    {
     "id": "L3-P3-p6",
     "la": "",
     "it": "E, trascurata una forza del Sole così piccola, la forza restante con cui la Luna è trattenuta nell’orbita sarà inversamente come D².",
     "en": "And if we neglect so inconsiderable a force of the sun, the remaining force, by which the moon is retained in its orb, will be reciprocally as D2.",
     "dipende_da": [],
     "figura": {
      "mostra": [],
      "evidenzia": [
       "forza ∝ 1/D²"
      ]
     }
    },
    {
     "id": "L3-P3-p7",
     "la": "",
     "it": "Ciò risulterà anche più pienamente confrontando questa forza con la forza di gravità, come si fa nella proposizione seguente.",
     "en": "This will yet more fully appear from comparing this force with the force of gravity, as is done in the next Proposition.",
     "dipende_da": [
      "Prop. IV"
     ],
     "figura": {
      "mostra": [],
      "evidenzia": []
     }
    }
   ]
  },
  {
   "id": "L3-P3-Cor",
   "tipo": "Corollarium",
   "titolo": "Prop. III, Cor. — la forza lunare riportata alla superficie della Terra",
   "copertura": [
    "III.G2.08"
   ],
   "fonti": {
    "la": "",
    "en": "Motte 1846, sezione corrispondente"
   },
   "enunciato": {
    "la": "",
    "it": "Se la forza centripeta media con cui la Luna è trattenuta nell’orbita si aumenta prima nel rapporto di 177 29/40 a 178 29/40, poi anche nel rapporto duplicato del semidiametro della Terra alla distanza media del centro della Luna dal centro della Terra, si avrà la forza centripeta lunare alla superficie della Terra, posto che quella forza, scendendo verso la superficie della Terra, aumenti continuamente nel rapporto inverso duplicato dell’altezza.",
    "en": "If we augment the mean centripetal force by which the moon is retained in its orb, first in the proportion of [SVG 964] to [SVG 963] , and then in the duplicate proportion of the semi-diameter of the earth to the mean distance of the centres of the moon and earth, we shall have the centripetal force of the moon at the surface of the earth; supposing this force, in descending to the earth's surface, continually to increase in the reciprocal duplicate proportion of the height."
   },
   "passi": [],
   "nota": "Corollario senza dimostrazione: il fattore 178 29/40 : 177 29/40 restituisce la parte di forza tolta dall’azione del Sole (nota N4)."
  },
  {
   "id": "L3-P4",
   "tipo": "Propositio/Theorema",
   "titolo": "Prop. IV — la Luna gravita verso la Terra (la prova della Luna)",
   "copertura": [
    "III.G2.09",
    "III.G2.10",
    "III.G2.11"
   ],
   "fonti": {
    "la": "",
    "en": "Motte 1846, sezione corrispondente (Prop. IV)"
   },
   "enunciato": {
    "la": "",
    "it": "La Luna gravita verso la Terra e dalla forza di gravità è continuamente distolta dal moto rettilineo e trattenuta nella sua orbita.",
    "en": "That the moon gravitates towards the earth, and by the force of gravity is continually drawn off from a rectilinear motion, and retained in its orbit."
   },
   "passi": [
    {
     "id": "L3-P4-p1",
     "la": "",
     "it": "La distanza media della Luna dalla Terra nelle sizigie è, in semidiametri terrestri, secondo Tolomeo e la maggior parte degli astronomi 59, secondo Wendelin e Huygens 60, secondo Copernico 60 1/3, secondo Street 60 2/5 e secondo Tycho 56 1/2.",
     "en": "The mean distance of the moon from the earth in the syzygies in semi-diameters of the earth, is, according to Ptolemy and most astronomers, 59; according to Vendelin and Huygens, 60; to Copernicus, [SVG 965] ; to Street, [SVG 966] ; and to Tycho, [SVG 967] .",
     "dipende_da": [],
     "figura": {
      "mostra": [
       "Terra",
       "Luna nelle sizigie",
       "scala in semidiametri terrestri"
      ],
      "evidenzia": [
       "valori 59; 60; 60 1/3; 60 2/5; 56 1/2"
      ]
     }
    },
    {
     "id": "L3-P4-p2",
     "la": "",
     "it": "Ma Tycho, e quanti seguono le sue tavole delle rifrazioni, ponendo le rifrazioni del Sole e della Luna (del tutto contro la natura della luce) maggiori di quelle delle stelle fisse, e ciò di circa quattro o cinque primi, aumentarono la parallasse della Luna di altrettanti primi, cioè di circa un dodicesimo o un quindicesimo dell’intera parallasse.",
     "en": "But Tycho, and all that follow his tables of refraction, making the refractions of the sun and moon (altogether against the nature of light) to exceed the refractions of the fixed stars, and that by four or five minutes near the horizon, did thereby increase the moon's horizontal parallax by a like number of minutes, that is, by a twelfth or fifteenth part of the whole parallax.",
     "dipende_da": [],
     "figura": {
      "mostra": [
       "parallasse orizzontale della Luna"
      ],
      "evidenzia": [
       "errore di 4′–5′ su circa 57′–61′"
      ]
     },
     "nota": "Motte aggiunge «near the horizon» e «horizontal» (parallasse orizzontale), che il latino non ha."
    },
    {
     "id": "L3-P4-p3",
     "la": "",
     "it": "Si corregga questo errore, e la distanza risulterà di circa 60 1/2 semidiametri terrestri, quasi come è stata assegnata dagli altri.",
     "en": "Correct this error, and the distance will become about [SVG 968] semi-diameters of the earth, near to what others have assigned.",
     "dipende_da": [],
     "figura": {
      "mostra": [],
      "evidenzia": [
       "56 1/2 → circa 60 1/2"
      ]
     }
    },
    {
     "id": "L3-P4-p4",
     "la": "",
     "it": "Assumiamo una distanza media di sessanta semidiametri nelle sizigie; e che il periodo lunare rispetto alle stelle fisse si compia in 27 giorni, 7 ore e 43 minuti, come è stabilito dagli astronomi; e che la circonferenza della Terra sia di 123249600 piedi parigini, come è stato determinato dai Francesi con le loro misure: se si immagina che la Luna, privata di ogni moto, sia lasciata andare in modo da scendere verso la Terra sotto l’azione di tutta quella forza da cui (per il Corollario della Prop. III) è trattenuta nella sua orbita, essa nello spazio di un minuto descriverà cadendo 15 1/12 piedi parigini.",
     "en": "Let us assume the mean distance of 60 diameters in the syzygies; and suppose one revolution of the moon, in respect of the fixed stars, to be completed in 27d. 7h. 43', as astronomers have determined; and the circumference of the earth to amount to 123249600 Paris feet, as the French have found by mensuration. And now if we imagine the moon, deprived of all motion, to be let go, so as to descend towards the earth with the impulse of all that force by which (by Cor. Prop. III) it is retained in its orb, it will in the space of one minute of time, describe in its fall [SVG 969] Paris feet.",
     "dipende_da": [
      "Prop. III, Cor."
     ],
     "figura": {
      "mostra": [
       "Terra di circonferenza 123249600 piedi",
       "Luna a 60 semidiametri",
       "caduta della Luna lasciata libera"
      ],
      "evidenzia": [
       "caduta in 1 minuto: 15 1/12 piedi"
      ]
     },
     "nota": "Motte scrive «60 diameters»: errore per «semi-diameters» (il latino ha *semidiametrorum*)."
    },
    {
     "id": "L3-P4-p5",
     "la": "",
     "it": "Ciò si ricava da un calcolo eseguito o per la Prop. XXXVI del Libro I o (ciò che torna lo stesso) per il Cor. 9 della Prop. IV dello stesso Libro.",
     "en": "This we gather by a calculus, founded either upon Prop. XXXVI, Book I, or (which comes to the same thing) upon Cor. 9, Prop. IV, of the same Book.",
     "dipende_da": [
      "Libro I, Prop. XXXVI",
      "Libro I, Prop. IV, Cor. 9"
     ],
     "figura": {
      "mostra": [],
      "evidenzia": [
       "arco² = diametro × caduta"
      ]
     }
    },
    {
     "id": "L3-P4-p6",
     "la": "",
     "it": "Infatti il seno verso dell’arco che la Luna, nel tempo di un minuto, con il suo moto medio, descriverebbe alla distanza di sessanta semidiametri terrestri, è di circa 15 1/12 piedi parigini, o più esattamente di 15 piedi, 1 pollice e 1 4/9 linee.",
     "en": "For the versed sine of that arc, which the moon, in the space of one minute of time, would by its mean motion describe at the distance of 60 semi-diameters of the earth, is nearly [SVG 969] Paris feet, or more accurately 15 feet, 1 inch, and 1 line [SVG 970] .",
     "dipende_da": [],
     "figura": {
      "mostra": [
       "arco descritto in 1 minuto",
       "seno verso dell’arco"
      ],
      "evidenzia": [
       "seno verso = caduta in 1 minuto (nota N5)"
      ]
     }
    },
    {
     "id": "L3-P4-p7",
     "la": "",
     "it": "Perciò, poiché quella forza, avvicinandosi alla Terra, aumenta nel rapporto inverso duplicato della distanza, e perciò alla superficie della Terra è 60×60 volte maggiore che alla Luna, un corpo che cadesse con quella forza nelle nostre regioni dovrebbe descrivere nello spazio di un minuto 60×60×15 1/12 piedi parigini, e nello spazio di un secondo 15 1/12 piedi, o più esattamente 15 piedi, 1 pollice e 1 4/9 linee.",
     "en": "Wherefore, since that force, in approaching to the earth, increases in the reciprocal duplicate proportion of the distance, and, upon that account, at the surface of the earth, is 60 × 60 times greater than at the moon, a body in our regions, falling with that force, ought in the space of one minute of time, to describe [SVG 971] Paris feet; and, in the space of one second of time, to describe [SVG 969] of those feet; or more accurately 15 feet, 1 inch, and 1 line [SVG 970] .",
     "dipende_da": [],
     "figura": {
      "mostra": [
       "superficie della Terra"
      ],
      "evidenzia": [
       "fattore 60 × 60",
       "1 minuto alla Luna ↔ 1 secondo a terra"
      ]
     }
    },
    {
     "id": "L3-P4-p8",
     "la": "",
     "it": "E con la stessa forza i gravi scendono di fatto verso la Terra.",
     "en": "And with this very force we actually find that bodies here upon earth do really descend;",
     "dipende_da": [],
     "figura": {
      "mostra": [],
      "evidenzia": []
     }
    },
    {
     "id": "L3-P4-p9",
     "la": "",
     "it": "Infatti la lunghezza del pendolo che batte i secondi alla latitudine di Parigi è di tre piedi parigini e 8 1/2 linee, come ha osservato Huygens.",
     "en": "for a pendulum oscillating seconds in the latitude of Paris will be 3 Paris feet, and 8 lines [SVG 643] in length, as Mr. Huygens has observed.",
     "dipende_da": [],
     "figura": {
      "mostra": [
       "pendolo che batte i secondi, lungo 3 piedi 8 1/2 linee"
      ],
      "evidenzia": []
     }
    },
    {
     "id": "L3-P4-p10",
     "la": "",
     "it": "E l’altezza che un grave descrive cadendo nel tempo di un secondo sta alla metà della lunghezza di questo pendolo nel rapporto duplicato della circonferenza del cerchio al suo diametro (come ha mostrato anche Huygens), e perciò è di 15 piedi parigini, 1 pollice, 1 7/9 linee.",
     "en": "And the space which a heavy body describes by falling in one second of time is to half the length of this pendulum in the duplicate ratio of the circumference of a circle to its diameter (as Mr. Huygens has also shewn), and is therefore 15 Paris feet, 1 inch, 1 line [SVG 972] .",
     "dipende_da": [],
     "figura": {
      "mostra": [
       "caduta di un grave in 1 secondo"
      ],
      "evidenzia": [
       "altezza : (L/2) = π² : 1",
       "15 piedi 1 pollice 1 7/9 linee"
      ]
     }
    },
    {
     "id": "L3-P4-p11",
     "la": "",
     "it": "E perciò la forza con cui la Luna è trattenuta nella sua orbita, se si scende fino alla superficie della Terra, risulta uguale alla forza di gravità presso di noi, e perciò (per le Regole I e II) è proprio quella forza che siamo soliti chiamare gravità.",
     "en": "And therefore the force by which the moon is retained in its orbit becomes, at the very surface of the earth, equal to the force of gravity which we observe in heavy bodies there. And therefore (by Rule I and II) the force by which the moon is retained in its orbit is that very same force which we commonly call gravity;",
     "dipende_da": [
      "Regola I",
      "Regola II"
     ],
     "figura": {
      "mostra": [],
      "evidenzia": [
       "1 4/9 linee contro 1 7/9 linee: uguaglianza"
      ]
     }
    },
    {
     "id": "L3-P4-p12",
     "la": "",
     "it": "Infatti, se la gravità fosse diversa da essa, i corpi, dirigendosi verso la Terra con le due forze congiunte, scenderebbero con velocità doppia, e nello spazio di un secondo descriverebbero cadendo 30 1/6 piedi parigini: del tutto contro l’esperienza.",
     "en": "for, were gravity another force different from that, then bodies descending to the earth with the joint impulse of both forces would fall with a double velocity, and in the space of one second of time would describe [SVG 973] Paris feet; altogether against experience.",
     "dipende_da": [],
     "figura": {
      "mostra": [],
      "evidenzia": [
       "30 1/6 = 2 × 15 1/12"
      ]
     }
    },
    {
     "id": "L3-P4-p13",
     "la": "",
     "it": "Questo calcolo si fonda sull’ipotesi che la Terra sia in quiete.",
     "en": "This calculus is founded on the hypothesis of the earth's standing still;",
     "dipende_da": [],
     "figura": {
      "mostra": [],
      "evidenzia": []
     }
    },
    {
     "id": "L3-P4-p14",
     "la": "",
     "it": "Infatti, se la Terra e la Luna si muovono attorno al Sole e intanto ruotano anche attorno al centro comune di gravità, restando la legge della gravità, la distanza dei centri della Luna e della Terra l’uno dall’altro sarà di circa 60 1/2 semidiametri terrestri, come risulterà a chi intraprenda il calcolo.",
     "en": "for if both earth and moon move about the sun, and at the same time about their common centre of gravity, the distance of the centres of the moon and earth from one another will be [SVG 968] semi-diameters of the earth;",
     "dipende_da": [],
     "figura": {
      "mostra": [
       "centro comune di gravità Terra–Luna"
      ],
      "evidenzia": [
       "60 → 60 1/2"
      ]
     },
     "nota": "Motte omette *manente lege gravitatis* e *circiter*."
    },
    {
     "id": "L3-P4-p15",
     "la": "",
     "it": "Il calcolo si può poi eseguire per la Prop. LX del Libro I.",
     "en": "as may be found by a computation from Prop. LX, Book I.",
     "dipende_da": [
      "Libro I, Prop. LX"
     ],
     "figura": {
      "mostra": [],
      "evidenzia": [
       "fattore (1 + Luna/Terra)^(1/3)"
      ]
     },
     "nota": "Motte fonde le due frasi latine in una."
    }
   ],
   "dati": {
    "circonferenza_terra_piedi": 123249600,
    "periodo_minuti": 39343,
    "seno_verso_60R_piedi_calcolato": 15.009,
    "seno_verso_aumentato_178.725_su_177.725": 15.09345,
    "newton_piedi": "15 1/12; 15 piedi 1 pollice 1 4/9 linee = 15,09336",
    "pendolo_secondi_piedi": 3.059028,
    "caduta_1s_da_pendolo_calcolata": 15.0957,
    "newton_caduta_1s": "15 piedi 1 pollice 1 7/9 linee = 15,09568",
    "distanza_prop_LX_con_luna_1_su_39788": 60.4985
   },
   "nota": "p1–p12 primo capoverso; p13–p15 secondo capoverso. Verifiche numeriche nella nota N5."
  },
  {
   "id": "L3-P4-Sch",
   "tipo": "Scholium",
   "titolo": "Scolio della Prop. IV — l’argomento della piccola luna",
   "copertura": [
    "III.G2.12"
   ],
   "fonti": {
    "la": "",
    "en": "Motte 1846, sezione corrispondente (Scholium)"
   },
   "passi": [
    {
     "id": "L3-P4-Sch-p1",
     "la": "",
     "it": "La dimostrazione della proposizione si può spiegare più diffusamente così.",
     "en": "The demonstration of this Proposition may be more diffusely explained after the following manner.",
     "dipende_da": [],
     "figura": {
      "mostra": [],
      "evidenzia": []
     }
    },
    {
     "id": "L3-P4-Sch-p2",
     "la": "",
     "it": "Se più lune ruotassero attorno alla Terra, come avviene nel sistema di Saturno o di Giove, i loro tempi periodici (per l’argomento d’induzione) osserverebbero la legge dei pianeti scoperta da Keplero, e perciò le loro forze centripete sarebbero inversamente come i quadrati delle distanze dal centro della Terra, per la Prop. I di questo Libro.",
     "en": "Suppose several moons to revolve about the earth, as in the system of Jupiter or Saturn; the periodic times of these moons (by the argument of induction) would observe the same law which Kepler found to obtain among the planets; and therefore their centripetal forces would be reciprocally as the squares of the distances from the centre of the earth, by Prop. I, of this Book.",
     "dipende_da": [
      "Prop. I"
     ],
     "figura": {
      "mostra": [
       "Terra con più lune ipotetiche"
      ],
      "evidenzia": [
       "tempi nel rapporto sesquiplicato → forze ∝ 1/r²"
      ]
     }
    },
    {
     "id": "L3-P4-Sch-p3",
     "la": "",
     "it": "E se la più bassa di esse fosse piccola e toccasse quasi le cime dei monti più alti, la sua forza centripeta, con cui sarebbe trattenuta nell’orbita, uguaglierebbe con ottima approssimazione (per il calcolo precedente) le gravità dei corpi sulle cime di quei monti, e farebbe sì che la stessa piccola luna, se fosse privata di tutto il moto con cui procede nella sua orbita, per mancanza della forza centrifuga con cui era rimasta nell’orbita scendesse verso la Terra, e ciò con la stessa velocità con cui cadono i gravi sulle cime di quei monti, per l’uguaglianza delle forze con cui scendono.",
     "en": "Now if the lowest of these were very small, and were so near the earth as almost to touch the tops of the highest mountains, the centripetal force thereof, retaining it in its orb, would be very nearly equal to the weights of any terrestrial bodies that should be found upon the tops of those mountains, as may be known by the foregoing computation. Therefore if the same little moon should be deserted by its centrifugal force that carries it through its orb, and so be disabled from going onward therein, it would descend to the earth; and that with the same velocity as heavy bodies do actually fall with upon the tops of those very mountains; because of the equality of the forces that oblige them both to descend.",
     "dipende_da": [
      "Prop. IV (calcolo precedente)"
     ],
     "figura": {
      "mostra": [
       "piccola luna radente le cime dei monti",
       "grave sulla cima"
      ],
      "evidenzia": [
       "forze uguali → cadute uguali"
      ]
     }
    },
    {
     "id": "L3-P4-Sch-p4",
     "la": "",
     "it": "E se la forza con cui quella piccola luna più bassa scende fosse diversa dalla gravità, e quella piccola luna fosse anche grave verso la Terra al modo dei corpi sulle cime dei monti, la stessa piccola luna, per le due forze congiunte, scenderebbe con velocità doppia.",
     "en": "And if the force by which that lowest moon would descend were different from gravity, and if that moon were to gravitate towards the earth, as we find terrestrial bodies do upon the tops of mountains, it would then descend with twice the velocity, as being impelled by both these forces conspiring together.",
     "dipende_da": [],
     "figura": {
      "mostra": [],
      "evidenzia": [
       "due forze → velocità doppia"
      ]
     }
    },
    {
     "id": "L3-P4-Sch-p5",
     "la": "",
     "it": "Perciò, poiché entrambe le forze, sia queste dei corpi gravi sia quelle delle lune, sono rivolte al centro della Terra e sono fra loro simili e uguali, esse (per le Regole I e II) avranno la stessa causa.",
     "en": "Therefore since both these forces, that is, the gravity of heavy bodies, and the centripetal forces of the moons, respect the centre of the earth, and are similar and equal between themselves, they will (by Rule I and II) have one and the same cause.",
     "dipende_da": [
      "Regola I",
      "Regola II"
     ],
     "figura": {
      "mostra": [],
      "evidenzia": [
       "stessa causa"
      ]
     }
    },
    {
     "id": "L3-P4-Sch-p6",
     "la": "",
     "it": "E perciò la forza con cui la Luna è trattenuta nella sua orbita sarà proprio quella che siamo soliti chiamare gravità: e ciò soprattutto perché la piccola luna sulla cima del monte non debba o essere priva di gravità o cadere due volte più velocemente di quanto sogliono cadere i corpi gravi.",
     "en": "And therefore the force which retains the moon in its orbit is that very force which we commonly call gravity; because otherwise this little moon at the top of a mountain must either be without gravity, or fall twice as swiftly as heavy bodies are wont to do.",
     "dipende_da": [],
     "figura": {
      "mostra": [],
      "evidenzia": []
     }
    }
   ]
  },
  {
   "id": "L3-P5",
   "tipo": "Propositio/Theorema",
   "titolo": "Prop. V — i satelliti e i pianeti gravitano verso Giove, Saturno e il Sole",
   "copertura": [
    "III.G2.13",
    "III.G2.14",
    "III.G2.15",
    "III.G2.16",
    "III.G2.17",
    "III.G2.18"
   ],
   "fonti": {
    "la": "",
    "en": "Motte 1846, sezione corrispondente (Prop. V, Cor. 1–3, Scholium)"
   },
   "enunciato": {
    "la": "",
    "it": "I pianeti circumgioviali gravitano verso Giove, i circumsaturnii verso Saturno e i circumsolari verso il Sole, e per la forza della loro gravità sono continuamente distolti dai moti rettilinei e trattenuti in orbite curvilinee.",
    "en": "That the circumjovial planets gravitate towards Jupiter; the circumsaturnal towards Saturn; the circumsolar towards the sun; and by the forces of their gravity are drawn off from rectilinear motions, and retained in curvilinear orbits."
   },
   "passi": [
    {
     "id": "L3-P5-p1",
     "la": "",
     "it": "Infatti le rivoluzioni dei pianeti circumgioviali attorno a Giove, dei circumsaturnii attorno a Saturno, e di Mercurio, di Venere e degli altri circumsolari attorno al Sole sono fenomeni dello stesso genere della rivoluzione della Luna attorno alla Terra; e perciò (per la Regola II) dipendono da cause dello stesso genere: soprattutto perché si è dimostrato che le forze da cui quelle rivoluzioni dipendono sono rivolte ai centri di Giove, di Saturno e del Sole e, allontanandosi da Giove, da Saturno e dal Sole, decrescono con lo stesso rapporto e la stessa legge con cui la forza di gravità decresce allontanandosi dalla Terra.",
     "en": "For the revolutions of the circumjovial planets about Jupiter, of the circumsaturnal about Saturn, and of Mercury and Venus, and the other circumsolar planets, about the sun, are appearances of the same sort with the revolution of the moon about the earth; and therefore, by Rule II, must be owing to the same sort of causes; especially since it has been demonstrated, that the forces upon which those revolutions depend tend to the centres of Jupiter, of Saturn, and of the sun; and that those forces, in receding from Jupiter, from Saturn, and from the sun, decrease in the same proportion, and according to the same law, as the force of gravity does in receding from the earth.",
     "dipende_da": [
      "Regola II",
      "Propp. I–IV"
     ],
     "figura": {
      "mostra": [
       "quattro sistemi: Giove, Saturno, Sole, Terra"
      ],
      "evidenzia": [
       "stessa legge 1/r²"
      ]
     }
    }
   ],
   "nota": "Corollari 1–3 e Scolio senza calcolo: compresi nella copertura, senza passi."
  },
  {
   "id": "L3-P6",
   "tipo": "Propositio/Theorema",
   "titolo": "Prop. VI — i pesi sono proporzionali alla quantità di materia (i pendoli)",
   "copertura": [
    "III.G2.19",
    "III.G2.20",
    "III.G2.21",
    "III.G2.22",
    "III.G2.23",
    "III.G2.24",
    "III.G2.25",
    "III.G2.26"
   ],
   "fonti": {
    "la": "",
    "en": "Motte 1846, sezione corrispondente (Prop. VI, Cor. 1–5)"
   },
   "enunciato": {
    "la": "",
    "it": "Tutti i corpi gravitano verso ciascun pianeta, e i loro pesi verso uno stesso pianeta qualsiasi, a uguali distanze dal centro del pianeta, sono proporzionali alla quantità di materia di ciascuno.",
    "en": "That all bodies gravitate towards every planet; and that the weights of bodies towards any the same planet, at equal distances from the centre of the planet, are proportional to the quantities of matter which they severally contain."
   },
   "passi": [
    {
     "id": "L3-P6-p1",
     "la": "",
     "it": "Che la discesa di tutti i gravi verso la Terra (tolto almeno il ritardo disuguale che nasce dalla piccolissima resistenza dell’aria) avvenga in tempi uguali, lo hanno osservato altri già da tempo; e con la massima esattezza si può rilevare l’uguaglianza dei tempi nei pendoli.",
     "en": "It has been, now of a long time, observed by others, that all sorts of heavy bodies (allowance being made for the inequality of retardation which they suffer from a small power of resistance in the air) descend to the earth from equal heights in equal times; and that equality of times we may distinguish to a great accuracy, by the help of pendulums.",
     "dipende_da": [],
     "figura": {
      "mostra": [],
      "evidenzia": []
     },
     "nota": "Motte aggiunge «from equal heights»."
    },
    {
     "id": "L3-P6-p2",
     "la": "",
     "it": "Ho messo alla prova la cosa con oro, argento, piombo, vetro, sabbia, sale comune, legno, acqua, frumento.",
     "en": "I tried the thing in gold, silver, lead, glass, sand, common salt, wood, water, and wheat.",
     "dipende_da": [],
     "figura": {
      "mostra": [
       "nove materiali"
      ],
      "evidenzia": []
     }
    },
    {
     "id": "L3-P6-p3",
     "la": "",
     "it": "Prendevo due scatole di legno, rotonde e uguali.",
     "en": "I provided two wooden boxes, round and equal:",
     "dipende_da": [],
     "figura": {
      "mostra": [
       "due scatole uguali"
      ],
      "evidenzia": []
     }
    },
    {
     "id": "L3-P6-p4",
     "la": "",
     "it": "Ne riempivo una di legno, e nel centro di oscillazione dell’altra sospendevo lo stesso peso d’oro (quanto più esattamente potevo).",
     "en": "I filled the one with wood, and suspended an equal weight of gold (as exactly as I could) in the centre of oscillation of the other.",
     "dipende_da": [],
     "figura": {
      "mostra": [
       "scatola piena di legno",
       "oro nel centro di oscillazione"
      ],
      "evidenzia": [
       "pesi uguali"
      ]
     }
    },
    {
     "id": "L3-P6-p5",
     "la": "",
     "it": "Le scatole, appese a fili uguali di undici piedi, costituivano pendoli del tutto uguali quanto al peso, alla figura e alla resistenza dell’aria: e, poste l’una accanto all’altra, con oscillazioni uguali andavano e tornavano insieme per moltissimo tempo.",
     "en": "The boxes hanging by equal threads of 11 feet made a couple of pendulums perfectly equal in weight and figure, and equally receiving the resistance of the air. And, placing the one by the other, I observed them to play together forward and backward, for a long time, with equal vibrations.",
     "dipende_da": [],
     "figura": {
      "mostra": [
       "due pendoli di 11 piedi affiancati"
      ],
      "evidenzia": [
       "oscillazioni sincrone"
      ]
     }
    },
    {
     "id": "L3-P6-p6",
     "la": "",
     "it": "Perciò la quantità di materia nell’oro (per i Cor. 1 e 6 della Prop. XXIV del Libro II) stava alla quantità di materia nel legno come l’azione della forza motrice su tutto l’oro sta alla sua azione su tutto il legno, cioè come il peso al peso.",
     "en": "And therefore the quantity of matter in the gold (by Cor. 1 and 6, Prop. XXIV, Book II) was to the quantity of matter in the wood as the action of the motive force (or vis motrix) upon all the gold to the action of the same upon all the wood; that is, as the weight of the one to the weight of the other:",
     "dipende_da": [
      "Libro II, Prop. XXIV, Cor. 1",
      "Libro II, Prop. XXIV, Cor. 6"
     ],
     "figura": {
      "mostra": [],
      "evidenzia": [
       "tempi uguali → materia ∝ peso"
      ]
     },
     "nota": "La trascrizione spezza la frase dopo «xxiv.» e «Lib.»: segmenti riuniti. Motte aggiunge «(or vis motrix)»."
    },
    {
     "id": "L3-P6-p7",
     "la": "",
     "it": "E così negli altri.",
     "en": "and the like happened in the other bodies.",
     "dipende_da": [],
     "figura": {
      "mostra": [],
      "evidenzia": []
     }
    },
    {
     "id": "L3-P6-p8",
     "la": "",
     "it": "Nei corpi dello stesso peso, una differenza di materia che fosse anche minore della millesima parte della materia totale si sarebbe potuta scoprire chiaramente con questi esperimenti.",
     "en": "By these experiments, in bodies of the same weight, I could manifestly have discovered a difference of matter less than the thousandth part of the whole, had any such been.",
     "dipende_da": [],
     "figura": {
      "mostra": [],
      "evidenzia": [
       "sensibilità 1/1000"
      ]
     }
    },
    {
     "id": "L3-P6-p9",
     "la": "",
     "it": "Ora, non c’è dubbio che la natura della gravità verso i pianeti sia la stessa che verso la Terra.",
     "en": "But, without all doubt, the nature of gravity towards the planets is the same as towards the earth.",
     "dipende_da": [],
     "figura": {
      "mostra": [],
      "evidenzia": []
     }
    },
    {
     "id": "L3-P6-p10",
     "la": "",
     "it": "Si immagini infatti che questi corpi terrestri siano sollevati fino all’orbita della Luna e, privati di ogni moto insieme con la Luna, siano lasciati andare in modo da cadere insieme verso la Terra; per ciò che si è già mostrato è certo che in tempi uguali descriveranno con la Luna spazi uguali, e perciò che stanno alla quantità di materia nella Luna come i loro pesi stanno al peso di essa.",
     "en": "For, should we imagine our terrestrial bodies removed to the orb of the moon, and there, together with the moon, deprived of all motion, to be let go, so as to fall together towards the earth, it is certain, from what we have demonstrated before, that, in equal times, they would describe equal spaces with the moon, and of consequence are to the moon, in quantity of matter, as their weights to its weight.",
     "dipende_da": [
      "Prop. IV"
     ],
     "figura": {
      "mostra": [
       "corpi terrestri all’orbita della Luna"
      ],
      "evidenzia": [
       "caduta comune"
      ]
     }
    },
    {
     "id": "L3-P6-p11",
     "la": "",
     "it": "Inoltre, poiché i satelliti di Giove ruotano in tempi che sono nel rapporto sesquiplicato delle distanze dal centro di Giove, le loro gravità acceleratrici verso Giove saranno inversamente come i quadrati delle distanze dal centro di Giove; e perciò, a uguali distanze da Giove, le loro gravità acceleratrici risulterebbero uguali.",
     "en": "Moreover, since the satellites of Jupiter perform their revolutions in times which observe the sesquiplicate proportion of their distances from Jupiter's centre, their accelerative gravities towards Jupiter will be reciprocally as the squares of their distances from Jupiter's centre; that is, equal, at equal distances.",
     "dipende_da": [],
     "figura": {
      "mostra": [
       "Giove e satelliti"
      ],
      "evidenzia": [
       "T ∝ r^(3/2) → g ∝ 1/r²"
      ]
     }
    },
    {
     "id": "L3-P6-p12",
     "la": "",
     "it": "Di conseguenza, cadendo da altezze uguali in tempi uguali, descriverebbero spazi uguali, proprio come avviene nei gravi su questa nostra Terra.",
     "en": "And, therefore, these satellites, if supposed to fall towards Jupiter from equal heights, would describe equal spaces in equal times, in like manner as heavy bodies do on our earth.",
     "dipende_da": [],
     "figura": {
      "mostra": [],
      "evidenzia": []
     }
    },
    {
     "id": "L3-P6-p13",
     "la": "",
     "it": "E con lo stesso argomento i pianeti circumsolari, lasciati andare a uguali distanze dal Sole, nella loro discesa verso il Sole descriverebbero in tempi uguali spazi uguali.",
     "en": "And, by the same argument, if the circumsolar planets were supposed to be let fall at equal distances from the sun, they would, in their descent towards the sun, describe equal spaces in equal times.",
     "dipende_da": [],
     "figura": {
      "mostra": [],
      "evidenzia": []
     }
    },
    {
     "id": "L3-P6-p14",
     "la": "",
     "it": "Ma le forze con cui corpi disuguali sono ugualmente accelerati sono come i corpi; cioè i pesi sono come le quantità di materia nei pianeti.",
     "en": "But forces which equally accelerate unequal bodies must be as those bodies: that is to say, the weights of the planets towards the sun must be as their quantities of matter.",
     "dipende_da": [],
     "figura": {
      "mostra": [],
      "evidenzia": [
       "peso ∝ massa"
      ]
     }
    },
    {
     "id": "L3-P6-p15",
     "la": "",
     "it": "Inoltre, che i pesi di Giove e dei suoi satelliti verso il Sole siano proporzionali alle loro quantità di materia è evidente dal moto regolarissimo dei satelliti, per il Cor. 3 della Prop. LXV del Libro I.",
     "en": "Further, that the weights of Jupiter and of his satellites towards the sun are proportional to the several quantities of their matter, appears from the exceedingly regular motions of the satellites (by Cor. 3, Prop. LXV, Book I).",
     "dipende_da": [
      "Libro I, Prop. LXV, Cor. 3"
     ],
     "figura": {
      "mostra": [
       "Sole, Giove, satelliti"
      ],
      "evidenzia": []
     }
    },
    {
     "id": "L3-P6-p16",
     "la": "",
     "it": "Infatti, se alcuni di essi fossero attratti verso il Sole più degli altri, in proporzione alla loro quantità di materia, i moti dei satelliti (per il Cor. 2 della Prop. LXV del Libro I) sarebbero perturbati dalla disuguaglianza dell’attrazione.",
     "en": "For if some of those bodies were more strongly attracted to the sun in proportion to their quantity of matter than others, the motions of the satellites would be disturbed by that inequality of attraction (by Cor. 2, Prop. LXV, Book I).",
     "dipende_da": [
      "Libro I, Prop. LXV, Cor. 2"
     ],
     "figura": {
      "mostra": [],
      "evidenzia": []
     }
    },
    {
     "id": "L3-P6-p17",
     "la": "",
     "it": "Se, a uguali distanze dal Sole, un satellite fosse più grave verso il Sole, in proporzione alla sua quantità di materia, di quanto lo sia Giove in proporzione alla sua, in un rapporto dato qualsiasi, per esempio come d sta a e, la distanza fra il centro del Sole e il centro dell’orbita del satellite sarebbe sempre maggiore della distanza fra il centro del Sole e il centro di Giove, con ottima approssimazione nel rapporto subduplicato: come ho trovato con un certo calcolo.",
     "en": "If, at equal distances from the sun, any satellite, in proportion to the quantity of its matter, did gravitate towards the sun with a force greater than Jupiter in proportion to his, according to any given proportion, suppose of d to e; then the distance between the centres of the sun and of the satellite's orbit would be always greater than the distance between the centres of the sun and of Jupiter nearly in the subduplicate of that proportion: as by some computations I have found.",
     "dipende_da": [],
     "figura": {
      "mostra": [
       "centro dell’orbita del satellite spostato rispetto a Giove"
      ],
      "evidenzia": [
       "spostamento nel rapporto √(d/e)"
      ]
     }
    },
    {
     "id": "L3-P6-p18",
     "la": "",
     "it": "E se il satellite fosse meno grave verso il Sole in quel rapporto di d a e, la distanza del centro dell’orbita del satellite dal Sole sarebbe minore della distanza del centro di Giove dal Sole in quello stesso rapporto subduplicato.",
     "en": "And if the satellite did gravitate towards the sun with a force, lesser in the proportion of e to d, the distance of the centre of the satellite's orb from the sun would be less than the distance of the centre of Jupiter from the sun in the subduplicate of the same proportion.",
     "dipende_da": [],
     "figura": {
      "mostra": [],
      "evidenzia": []
     },
     "nota": "Motte scrive «in the proportion of e to d», invertendo i termini del latino *d ad e* (il senso non cambia)."
    },
    {
     "id": "L3-P6-p19",
     "la": "",
     "it": "Perciò, se a uguali distanze dal Sole la gravità acceleratrice di un satellite qualsiasi verso il Sole fosse maggiore o minore della gravità acceleratrice di Giove verso il Sole anche soltanto di una millesima parte della gravità totale, la distanza del centro dell’orbita del satellite dal Sole sarebbe maggiore o minore della distanza di Giove dal Sole di una duemillesima parte della distanza totale, cioè di un quinto della distanza del satellite più esterno dal centro di Giove: e questa eccentricità dell’orbita sarebbe assai sensibile.",
     "en": "Therefore if, at equal distances from the sun, the accelerative gravity of any satellite towards the sun were greater or less than the accelerative gravity of Jupiter towards the sun but by one [SVG 974] part of the whole gravity, the distance of the centre of the satellite's orbit from the sun would be greater or less than the distance of Jupiter from the sun by one [SVG 975] part of the whole distance; that is, by a fifth part of the distance of the utmost satellite from the centre of Jupiter; an eccentricity of the orbit which would be very sensible.",
     "dipende_da": [],
     "figura": {
      "mostra": [
       "orbita del satellite IV",
       "spostamento 1/2000 della distanza Giove–Sole"
      ],
      "evidenzia": [
       "√(1,001) − 1 ≈ 1/2000",
       "1/2000 × 415,9 ≈ 1/5 (nota N7)"
      ]
     },
     "nota": "«parte 12000» della trascrizione = 1/2000 (frazione appiattita); Motte [SVG 974] 1/1000 e [SVG 975] 1/2000."
    },
    {
     "id": "L3-P6-p20",
     "la": "",
     "it": "Ma le orbite dei satelliti sono concentriche a Giove, e perciò le gravità acceleratrici di Giove e dei satelliti verso il Sole sono uguali fra loro.",
     "en": "But the orbits of the satellites are concentric to Jupiter, and therefore the accelerative gravities of Jupiter, and of all its satellites towards the sun, are equal among themselves.",
     "dipende_da": [],
     "figura": {
      "mostra": [],
      "evidenzia": [
       "orbite concentriche → gravità acceleratrici uguali"
      ]
     }
    },
    {
     "id": "L3-P6-p21",
     "la": "",
     "it": "E con lo stesso argomento i pesi di Saturno e dei suoi satelliti verso il Sole, a uguali distanze dal Sole, sono come le quantità di materia in essi; e i pesi della Luna e della Terra verso il Sole o sono nulli, o sono esattamente proporzionali alle loro masse.",
     "en": "And by the same argument, the weights of Saturn and of his satellites towards the sun, at equal distances from the sun, are as their several quantities of matter; and the weights of the moon and of the earth towards the sun are either none, or accurately proportional to the masses of matter which they contain.",
     "dipende_da": [],
     "figura": {
      "mostra": [],
      "evidenzia": []
     }
    },
    {
     "id": "L3-P6-p22",
     "la": "",
     "it": "Ma qualche peso c’è, per i Cor. 1 e 3 della Prop. V.",
     "en": "But some they are, by Cor. 1 and 3, Prop. V.",
     "dipende_da": [
      "Prop. V, Cor. 1",
      "Prop. V, Cor. 3"
     ],
     "figura": {
      "mostra": [],
      "evidenzia": []
     }
    },
    {
     "id": "L3-P6-p23",
     "la": "",
     "it": "Inoltre i pesi delle singole parti di ciascun pianeta verso un altro pianeta qualsiasi stanno fra loro come la materia nelle singole parti.",
     "en": "But further; the weights of all the parts of every planet towards any other planet are one to another as the matter in the several parts;",
     "dipende_da": [],
     "figura": {
      "mostra": [],
      "evidenzia": []
     }
    },
    {
     "id": "L3-P6-p24",
     "la": "",
     "it": "Infatti, se alcune parti gravitassero di più, altre di meno, di quanto comporta la quantità di materia, il pianeta intero, secondo il genere delle parti di cui è più ricco, graviterebbe di più o di meno di quanto comporta la quantità di materia del tutto.",
     "en": "for if some parts did gravitate more, others less, than for the quantity of their matter, then the whole planet, according to the sort of parts with which it most abounds, would gravitate more or less than in proportion to the quantity of matter in the whole.",
     "dipende_da": [],
     "figura": {
      "mostra": [],
      "evidenzia": []
     }
    },
    {
     "id": "L3-P6-p25",
     "la": "",
     "it": "Né importa se quelle parti siano esterne o interne.",
     "en": "Nor is it of any moment whether these parts are external or internal;",
     "dipende_da": [],
     "figura": {
      "mostra": [],
      "evidenzia": []
     }
    },
    {
     "id": "L3-P6-p26",
     "la": "",
     "it": "Infatti, se per esempio si immagina che i corpi terrestri che sono presso di noi siano sollevati fino all’orbita della Luna e confrontati con il corpo della Luna: se i loro pesi stessero ai pesi delle parti esterne della Luna come le quantità di materia nelle une e negli altri, e invece ai pesi delle parti interne in un rapporto maggiore o minore, starebbero al peso della Luna intera in un rapporto maggiore o minore: contro ciò che si è mostrato sopra.",
     "en": "for if, for example, we should imagine the terrestrial bodies with us to be raised up to the orb of the moon, to be there compared with its body: if the weights of such bodies were to the weights of the external parts of the moon as the quantities of matter in the one and in the other respectively; but to the weights of the internal parts in a greater or less proportion, then likewise the weights of those bodies would be to the weight of the whole moon in a greater or less proportion; against what we have shewed above.",
     "dipende_da": [],
     "figura": {
      "mostra": [],
      "evidenzia": []
     }
    }
   ],
   "dati": {
    "sensibilita_pendoli": "1/1000",
    "spostamento_orbita_satellite": {
     "sqrt_1001_meno_1": 0.00049988,
     "distanza_Giove_su_distanza_satellite_IV": 415.86,
     "frazione_della_distanza_del_satellite": 0.208
    }
   },
   "nota": "p1–p22 primo capoverso; p23–p26 secondo capoverso. I Cor. 1–5 sono nella copertura senza passi."
  },
  {
   "id": "L3-P7",
   "tipo": "Propositio/Theorema",
   "titolo": "Prop. VII — la gravità universale è proporzionale alla quantità di materia",
   "copertura": [
    "III.G2.27",
    "III.G2.28",
    "III.G2.29",
    "III.G2.30",
    "III.G2.31"
   ],
   "fonti": {
    "la": "",
    "en": "Motte 1846, sezione corrispondente (Prop. VII)"
   },
   "enunciato": {
    "la": "",
    "it": "Esiste una gravità verso tutti i corpi, ed è proporzionale alla quantità di materia di ciascuno.",
    "en": "That there is a power of gravity tending to all bodies, proportional to the several quantities of matter which they contain."
   },
   "passi": [
    {
     "id": "L3-P7-p1",
     "la": "",
     "it": "Abbiamo già provato prima che tutti i pianeti sono gravi gli uni verso gli altri, e anche che la gravità verso ciascuno, considerato separatamente, è inversamente come il quadrato della distanza dei luoghi dal centro del pianeta.",
     "en": "That all the planets mutually gravitate one towards another, we have proved before; as well as that the force of gravity towards every one of them, considered apart, is reciprocally as the square of the distance of places from the centre of the planet.",
     "dipende_da": [
      "Prop. V, Cor. 2–3"
     ],
     "figura": {
      "mostra": [
       "pianeti A, B, C"
      ],
      "evidenzia": []
     }
    },
    {
     "id": "L3-P7-p2",
     "la": "",
     "it": "E di qui segue (per la Prop. LXIX del Libro I e i suoi corollari) che la gravità verso tutti è proporzionale alla materia in essi.",
     "en": "And thence (by Prop. LXIX, Book I, and its Corollaries) it follows, that the gravity tending towards all the planets is proportional to the matter which they contain.",
     "dipende_da": [
      "Libro I, Prop. LXIX e corollari"
     ],
     "figura": {
      "mostra": [],
      "evidenzia": [
       "forze assolute ∝ corpi"
      ]
     }
    },
    {
     "id": "L3-P7-p3",
     "la": "",
     "it": "Inoltre, poiché tutte le parti di un pianeta qualsiasi A sono gravi verso un pianeta qualsiasi B, e la gravità di ciascuna parte sta alla gravità del tutto come la materia della parte sta alla materia del tutto, e (per la terza legge del moto) a ogni azione è uguale una reazione, il pianeta B a sua volta graviterà verso tutte le parti del pianeta A, e la sua gravità verso ciascuna parte starà alla sua gravità verso il tutto come la materia della parte sta alla materia del tutto. C.V.D.",
     "en": "Moreover, since all the parts of any planet A gravitate towards any other planet B; and the gravity of every part is to the gravity of the whole as the matter of the part to the matter of the whole; and (by Law III) to every action corresponds an equal re-action; therefore the planet B will, on the other hand, gravitate towards all the parts of the planet A; and its gravity towards any one part will be to the gravity towards the whole as the matter of the part to the matter of the whole. Q.E.D.",
     "dipende_da": [
      "Legge III",
      "Prop. VI"
     ],
     "figura": {
      "mostra": [
       "pianeta A suddiviso in parti",
       "pianeta B"
      ],
      "evidenzia": [
       "azione e reazione parte per parte"
      ]
     }
    }
   ],
   "nota": "I Cor. 1–2 sono nella copertura senza passi."
  },
  {
   "id": "L3-P8",
   "tipo": "Propositio/Theorema",
   "titolo": "Prop. VIII — globi omogenei per strati: peso inverso del quadrato della distanza dei centri",
   "copertura": [
    "III.G2.32",
    "III.G2.33",
    "III.G2.37"
   ],
   "fonti": {
    "la": "",
    "en": "Motte 1846, sezione corrispondente (Prop. VIII)"
   },
   "enunciato": {
    "la": "",
    "it": "Se la materia di due globi che gravitano l’uno verso l’altro è omogenea da ogni parte nelle regioni che distano ugualmente dai centri, il peso di ciascuno dei due globi verso l’altro sarà inversamente come il quadrato della distanza fra i centri.",
    "en": "In two spheres mutually gravitating each towards the other, if the matter in places on all sides round about and equi-distant from the centres is similar, the weight of either sphere towards the other will be reciprocally as the square of the distance between their centres."
   },
   "passi": [
    {
     "id": "L3-P8-p1",
     "la": "",
     "it": "Dopo che avevo trovato che la gravità verso il pianeta intero nasce ed è composta dalle gravità verso le parti, e che verso le singole parti è inversamente proporzionale ai quadrati delle distanze dalle parti, dubitavo se quella proporzione inversa duplicata valesse esattamente nella forza totale composta da più forze, o soltanto con ottima approssimazione.",
     "en": "After I had found that the force of gravity towards a whole planet did arise from and was compounded of the forces of gravity towards all its parts, and towards every one part was in the reciprocal proportion of the squares of the distances from the part, I was yet in doubt whether that reciprocal duplicate proportion did accurately hold, or but nearly so, in the total force compounded of so many partial ones;",
     "dipende_da": [
      "Prop. VII, Cor. 1–2"
     ],
     "figura": {
      "mostra": [
       "globo diviso in particelle",
       "corpuscolo esterno"
      ],
      "evidenzia": []
     }
    },
    {
     "id": "L3-P8-p2",
     "la": "",
     "it": "Poteva infatti accadere che la proporzione, che a distanze maggiori valeva con sufficiente esattezza, vicino alla superficie del pianeta, a causa delle distanze disuguali delle particelle e delle loro posizioni dissimili, sbagliasse notevolmente.",
     "en": "for it might be that the proportion which accurately enough took place in greater distances should be wide of the truth near the surface of the planet, where the distances of the particles are unequal, and their situation dissimilar.",
     "dipende_da": [],
     "figura": {
      "mostra": [
       "corpuscolo vicino alla superficie"
      ],
      "evidenzia": [
       "distanze disuguali dalle particelle"
      ]
     }
    },
    {
     "id": "L3-P8-p3",
     "la": "",
     "it": "Alla fine, però, per le Propp. LXXV e LXXVI del Libro I e i loro corollari, compresi la verità della proposizione di cui qui si tratta.",
     "en": "But by the help of Prop. LXXV and LXXVI, Book I, and their Corollaries, I was at last satisfied of the truth of the Proposition, as it now lies before us.",
     "dipende_da": [
      "Libro I, Prop. LXXV",
      "Libro I, Prop. LXXVI"
     ],
     "figura": {
      "mostra": [
       "due sfere stratificate"
      ],
      "evidenzia": [
       "forza ∝ 1/distanza² dei centri, esattamente"
      ]
     }
    }
   ],
   "nota": "Il Cor. 4 (III.G2.37) è nella copertura senza passi; i Cor. 1–3 hanno unità proprie."
  },
  {
   "id": "L3-P8-Cor1",
   "tipo": "Corollarium",
   "titolo": "Prop. VIII, Cor. 1 — i pesi verso il Sole, Giove, Saturno e la Terra",
   "copertura": [
    "III.G2.34"
   ],
   "fonti": {
    "la": "",
    "en": "Motte 1846, sezione corrispondente"
   },
   "enunciato": {
    "la": "",
    "it": "Di qui si possono trovare e confrontare fra loro i pesi dei corpi verso pianeti diversi.",
    "en": "Hence we may find and compare together the weights of bodies towards different planets;"
   },
   "passi": [
    {
     "id": "L3-P8-Cor1-p1",
     "la": "",
     "it": "Infatti i pesi di corpi uguali che ruotano in cerchi attorno ai pianeti sono (per il Cor. 2 della Prop. IV del Libro I) come i diametri dei cerchi direttamente e come i quadrati dei tempi periodici inversamente; e i pesi alle superfici dei pianeti, o a qualsiasi altra distanza dal centro, sono maggiori o minori (per questa proposizione) nel rapporto inverso duplicato delle distanze.",
     "en": "for the weights of bodies revolving in circles about planets are (by Cor. 2, Prop. IV, Book I) as the diameters of the circles directly, and the squares of their periodic times reciprocally; and their weights at the surfaces of the planets, or at any other distances from their centres, are (by this Prop.) greater or less in the reciprocal duplicate proportion of the distances.",
     "dipende_da": [
      "Libro I, Prop. IV, Cor. 2",
      "Prop. VIII"
     ],
     "figura": {
      "mostra": [
       "corpo in orbita circolare attorno a un pianeta"
      ],
      "evidenzia": [
       "peso ∝ r/T²",
       "riduzione alla superficie ∝ 1/r²"
      ]
     },
     "nota": "Frase spezzata nella trascrizione dopo «corol. 2.»: segmenti riuniti."
    },
    {
     "id": "L3-P8-Cor1-p2",
     "la": "",
     "it": "Così, dai tempi periodici di Venere attorno al Sole, di 224 giorni e 16 3/4 ore, del satellite circumgioviale più esterno attorno a Giove, di 16 giorni e 16 8/15 ore, del satellite di Huygens attorno a Saturno, di 15 giorni e 22 2/3 ore, e della Luna attorno alla Terra, di 27 giorni, 7 ore e 43 minuti, confrontati con la distanza media di Venere dal Sole e con le elongazioni massime eliocentriche del satellite circumgioviale più esterno dal centro di Giove, 8′ 16″, del satellite di Huygens dal centro di Saturno, 3′ 4″, e della Luna dal centro della Terra, 10′ 33″, facendo il calcolo ho trovato che i pesi di corpi uguali, ugualmente distanti dal centro del Sole, di Giove, di Saturno e della Terra, verso il Sole, Giove, Saturno e la Terra stanno rispettivamente come 1, 1/1067, 1/3021 e 1/169282; e che, aumentando o diminuendo le distanze, i pesi diminuiscono o aumentano nel rapporto duplicato: i pesi di corpi uguali verso il Sole, Giove, Saturno e la Terra alle distanze 10000, 997, 791 e 109 dai loro centri, e perciò alle loro superfici, staranno rispettivamente come 10000, 943, 529 e 435.",
     "en": "Thus from the periodic times of Venus, revolving about the sun, in 224d. [SVG 976] , of the utmost circumjovial satellite revolving about Jupiter, in 16d, [SVG 977] ; of the Huygenian satellite about Saturn in 15d. [SVG 978] ; and of the moon about the earth in 27d. 7h. 43'; compared with the mean distance of Venus from the sun, and with the greatest heliocentric elongations of the outmost circumjovial satellite from Jupiter's centre, 8' 16''; of the Huygenian satellite from the centre of Saturn, 3' 4''; and of the moon from the earth, 10' 33'': by computation I found that the weight of equal bodies, at equal distances from the centres of the sun, of Jupiter, of Saturn, and of the earth, towards the sun, Jupiter, Saturn, and the earth, were one to another, as 1, [SVG 979] , [SVG 980] , and [SVG 981] respectively. Then because as the distances are increased or diminished, the weights are diminished or increased in a duplicate ratio, the weights of equal bodies towards the sun, Jupiter, Saturn, and the earth, at the distances 10000, 997, 791, and 109 from their centres, that is, at their very superficies, will be as 10000, 943, 529, and 435 respectively.",
     "dipende_da": [],
     "figura": {
      "mostra": [
       "quattro sistemi in scala",
       "tabella dei dati"
      ],
      "evidenzia": [
       "1/1067 confermato; 1/3021 e 1/169282 non tornano con i dati (nota N8)"
      ]
     },
     "nota": "Frazioni appiattite nella trascrizione: «16⁤34» = 16 3/4, «16⁤815» = 16 8/15, «22⁤23» = 22 2/3, «11067» = 1/1067, «13021» = 1/3021, «1169282» = 1/169282."
    },
    {
     "id": "L3-P8-Cor1-p3",
     "la": "",
     "it": "Quanto siano i pesi dei corpi alla superficie della Luna si dirà in seguito.",
     "en": "How much the weights of bodies are at the superficies of the moon, will be shewn hereafter.",
     "dipende_da": [],
     "figura": {
      "mostra": [],
      "evidenzia": []
     }
    }
   ],
   "dati": {
    "tempi_periodici_giorni": {
     "Venere": 224.6979,
     "satellite_IV_Giove": 16.6889,
     "satellite_Huygens_Saturno": 15.9444,
     "Luna": 27.3215
    },
    "elongazioni_eliocentriche_secondi": {
     "Giove_IV": 496,
     "Saturno_Huygens": 184,
     "Luna": 633
    },
    "distanze_medie_Fen_IV": {
     "Venere": 72333,
     "Terra": 100000,
     "Giove": 520096,
     "Saturno": 954006
    },
    "pesi_Newton": [
     1,
     "1/1067",
     "1/3021",
     "1/169282"
    ],
    "pesi_ricalcolati": [
     "1",
     "1/1067,2",
     "1/3091,7",
     "1/193589"
    ],
    "diametri": [
     10000,
     997,
     791,
     109
    ],
    "pesi_superficie_Newton": [
     10000,
     943,
     529,
     435
    ],
    "pesi_superficie_ricalcolati_da_1_1067_1_3021_1_169282": [
     10000,
     942.9,
     529.0,
     497.2
    ]
   }
  },
  {
   "id": "L3-P8-Cor2",
   "tipo": "Corollarium",
   "titolo": "Prop. VIII, Cor. 2 — le quantità di materia dei pianeti",
   "copertura": [
    "III.G2.35"
   ],
   "fonti": {
    "la": "",
    "en": "Motte 1846, sezione corrispondente"
   },
   "enunciato": {
    "la": "",
    "it": "Si conosce anche la quantità di materia nei singoli pianeti.",
    "en": "Hence likewise we discover the quantity of matter in the several planets;"
   },
   "passi": [
    {
     "id": "L3-P8-Cor2-p1",
     "la": "",
     "it": "Infatti le quantità di materia nei pianeti sono come le loro forze a uguali distanze dai loro centri, cioè nel Sole, in Giove, in Saturno e nella Terra sono rispettivamente come 1, 1/1067, 1/3021 e 1/169282.",
     "en": "for their quantities of matter are as the forces of gravity at equal distances from their centres; that is, in the sun, Jupiter, Saturn, and the earth, as 1, [SVG 979] , [SVG 980] , and [SVG 981] respectively.",
     "dipende_da": [
      "Prop. VII"
     ],
     "figura": {
      "mostra": [],
      "evidenzia": [
       "massa ∝ forza a distanza uguale"
      ]
     }
    },
    {
     "id": "L3-P8-Cor2-p2",
     "la": "",
     "it": "Se la parallasse del Sole si pone maggiore o minore di 10″ 30‴, la quantità di materia nella Terra dovrà essere aumentata o diminuita nel rapporto triplicato.",
     "en": "If the parallax of the sun be taken greater or less than 10'' 30''', the quantity of matter in the earth must be augmented or diminished in the triplicate of that proportion.",
     "dipende_da": [],
     "figura": {
      "mostra": [
       "cursore: parallasse solare"
      ],
      "evidenzia": [
       "massa terrestre ∝ parallasse³"
      ]
     }
    }
   ]
  },
  {
   "id": "L3-P8-Cor3",
   "tipo": "Corollarium",
   "titolo": "Prop. VIII, Cor. 3 — le densità dei pianeti",
   "copertura": [
    "III.G2.36"
   ],
   "fonti": {
    "la": "",
    "en": "Motte 1846, sezione corrispondente"
   },
   "enunciato": {
    "la": "",
    "it": "Si conoscono anche le densità dei pianeti.",
    "en": "Hence also we find the densities of the planets;"
   },
   "passi": [
    {
     "id": "L3-P8-Cor3-p1",
     "la": "",
     "it": "Infatti i pesi di corpi uguali e omogenei verso sfere omogenee sono, alle superfici delle sfere, come i diametri delle sfere, per la Prop. LXXII del Libro I; e perciò le densità di sfere eterogenee sono come quei pesi divisi per i diametri delle sfere.",
     "en": "for (by Prop. LXXII, Book I) the weights of equal and similar bodies towards similar spheres are, at the surfaces of those spheres, as the diameters of the spheres; and therefore the densities of dissimilar spheres are as those weights applied to the diameters of the spheres.",
     "dipende_da": [
      "Libro I, Prop. LXXII"
     ],
     "figura": {
      "mostra": [],
      "evidenzia": [
       "densità ∝ peso alla superficie / diametro"
      ]
     },
     "nota": "Motte rende *homogeneus* con «similar» e *heterogeneus* con «dissimilar»."
    },
    {
     "id": "L3-P8-Cor3-p2",
     "la": "",
     "it": "Ora, i veri diametri del Sole, di Giove, di Saturno e della Terra stavano fra loro come 10000, 997, 791 e 109, e i pesi verso di essi come 10000, 943, 529 e 435 rispettivamente; e perciò le densità sono come 100, 94 1/2, 67, 400.",
     "en": "But the true diameters of the Sun, Jupiter, Saturn, and the earth, were one to another as 10000, 997, 791, and 109; and the weights towards the same as 10000, 943, 529, and 435 respectively; and therefore their densities are as 100, [SVG 982] , 67, and 400.",
     "dipende_da": [],
     "figura": {
      "mostra": [
       "tabella diametri, pesi, densità"
      ],
      "evidenzia": [
       "943/997 = 0,946; 529/791 = 0,669; 435/109 = 3,99"
      ]
     }
    },
    {
     "id": "L3-P8-Cor3-p3",
     "la": "",
     "it": "La densità della Terra che risulta da questo calcolo non dipende dalla parallasse del Sole, ma è determinata dalla parallasse della Luna, e perciò qui è definita correttamente.",
     "en": "The density of the earth, which comes out by this computation, does not depend upon the parallax of the sun, but is determined by the parallax of the moon, and therefore is here truly defined.",
     "dipende_da": [],
     "figura": {
      "mostra": [],
      "evidenzia": [
       "parallasse³ / parallasse³"
      ]
     }
    },
    {
     "id": "L3-P8-Cor3-p4",
     "la": "",
     "it": "Il Sole è dunque un poco più denso di Giove, e Giove più di Saturno, e la Terra quattro volte più densa del Sole.",
     "en": "The sun, therefore, is a little denser than Jupiter, and Jupiter than Saturn, and the earth four times denser than the sun;",
     "dipende_da": [],
     "figura": {
      "mostra": [],
      "evidenzia": []
     }
    },
    {
     "id": "L3-P8-Cor3-p5",
     "la": "",
     "it": "Infatti il Sole, per il suo enorme calore, si rarefà.",
     "en": "for the sun, by its great heat, is kept in a sort of a rarefied state.",
     "dipende_da": [],
     "figura": {
      "mostra": [],
      "evidenzia": []
     }
    },
    {
     "id": "L3-P8-Cor3-p6",
     "la": "",
     "it": "La Luna invece è più densa della Terra, come risulterà in seguito.",
     "en": "The moon is denser than the earth, as shall appear afterward.",
     "dipende_da": [],
     "figura": {
      "mostra": [],
      "evidenzia": []
     }
    }
   ],
   "dati": {
    "densita_Newton": [
     100,
     94.5,
     67,
     400
    ],
    "densita_ricalcolate_peso_su_diametro": [
     100,
     94.58,
     66.88,
     399.08
    ]
   }
  },
  {
   "id": "L3-P9",
   "tipo": "Propositio/Theorema",
   "titolo": "Prop. IX — sotto la superficie la gravità decresce come la distanza dal centro",
   "copertura": [
    "III.G2.38",
    "III.G2.39"
   ],
   "fonti": {
    "la": "",
    "en": "Motte 1846, sezione corrispondente (Prop. IX)"
   },
   "enunciato": {
    "la": "",
    "it": "La gravità, procedendo dalle superfici dei pianeti verso il basso, decresce con ottima approssimazione nel rapporto delle distanze dal centro.",
    "en": "That the force of gravity, considered downward from the surface of the planets, decreases nearly in the proportion, of the distances from their centres."
   },
   "passi": [
    {
     "id": "L3-P9-p1",
     "la": "",
     "it": "Se la materia del pianeta fosse uniforme quanto alla densità, questa proposizione varrebbe esattamente, per la Prop. LXXIII del Libro I.",
     "en": "If the matter of the planet were of an uniform density, this Proposition would be accurately true (by Prop. LXXIII. Book I).",
     "dipende_da": [
      "Libro I, Prop. LXXIII"
     ],
     "figura": {
      "mostra": [
       "sfera piena",
       "corpuscolo interno"
      ],
      "evidenzia": [
       "forza ∝ distanza dal centro"
      ]
     }
    },
    {
     "id": "L3-P9-p2",
     "la": "",
     "it": "L’errore è dunque tanto grande quanto può nascere dalla densità non uniforme.",
     "en": "The error, therefore, can be no greater than what may arise from the inequality of the density.",
     "dipende_da": [],
     "figura": {
      "mostra": [],
      "evidenzia": []
     }
    }
   ]
  },
  {
   "id": "L3-P10",
   "tipo": "Propositio/Theorema",
   "titolo": "Prop. X — i moti dei pianeti si conservano per lunghissimo tempo",
   "copertura": [
    "III.G2.40",
    "III.G2.41"
   ],
   "fonti": {
    "la": "",
    "en": "Motte 1846, sezione corrispondente (Prop. X, due capoversi)"
   },
   "enunciato": {
    "la": "",
    "it": "I moti dei pianeti nei cieli possono conservarsi per lunghissimo tempo.",
    "en": "That the motions of the planets in the heavens may subsist an exceedingly long time."
   },
   "passi": [
    {
     "id": "L3-P10-p1",
     "la": "",
     "it": "Nello Scolio della Prop. XL del Libro II si è mostrato che un globo d’acqua congelata, muovendosi liberamente nella nostra aria e descrivendo la lunghezza del suo semidiametro, perderebbe per la resistenza dell’aria 1/4586 del suo moto.",
     "en": "In the Scholium of Prop. XL, Book II, I have shewed that a globe of water frozen into ice, and moving freely in our air, in the time that it would describe the length of its semi-diameter, would lose by the resistance of the air [SVG 918] part of its motion;",
     "dipende_da": [
      "Libro II, Scolio della Prop. XL"
     ],
     "figura": {
      "mostra": [
       "globo di ghiaccio in aria"
      ],
      "evidenzia": [
       "perdita 1/4586 per semidiametro"
      ]
     },
     "nota": "«partem 14586» della trascrizione = 1/4586."
    },
    {
     "id": "L3-P10-p2",
     "la": "",
     "it": "E la stessa proporzione vale con ottima approssimazione in globi comunque grandi e veloci.",
     "en": "and the same proportion holds nearly in all globes, how great soever, and moved with whatever velocity.",
     "dipende_da": [],
     "figura": {
      "mostra": [],
      "evidenzia": []
     }
    },
    {
     "id": "L3-P10-p3",
     "la": "",
     "it": "Ora, che il globo della nostra Terra sia più denso che se constasse tutto d’acqua, lo ricavo così.",
     "en": "But that our globe of earth is of greater density than it would be if the whole consisted of water only, I thus make out.",
     "dipende_da": [],
     "figura": {
      "mostra": [],
      "evidenzia": []
     }
    },
    {
     "id": "L3-P10-p4",
     "la": "",
     "it": "Se questo globo fosse tutto d’acqua, qualunque cosa fosse più rada dell’acqua, a causa della minore gravità specifica, emergerebbe e galleggerebbe sopra.",
     "en": "If the whole consisted of water only, whatever was of less density than water, because of its less specific gravity, would emerge and float above.",
     "dipende_da": [],
     "figura": {
      "mostra": [],
      "evidenzia": []
     }
    },
    {
     "id": "L3-P10-p5",
     "la": "",
     "it": "E per questa ragione un globo di terra coperto d’acqua da ogni parte, se fosse più rado dell’acqua, emergerebbe da qualche parte, e tutta l’acqua, defluendo di là, si raccoglierebbe nella regione opposta.",
     "en": "And upon this account, if a globe of terrestrial matter, covered on all sides with water, was less dense than water, it would emerge somewhere; and, the subsiding water falling back, would be gathered to the opposite side.",
     "dipende_da": [],
     "figura": {
      "mostra": [
       "globo di terra ricoperto d’acqua"
      ],
      "evidenzia": []
     }
    },
    {
     "id": "L3-P10-p6",
     "la": "",
     "it": "E la condizione della nostra Terra, circondata in gran parte dai mari, è la stessa.",
     "en": "And such is the condition of our earth, which in a great measure is covered with seas.",
     "dipende_da": [],
     "figura": {
      "mostra": [],
      "evidenzia": []
     }
    },
    {
     "id": "L3-P10-p7",
     "la": "",
     "it": "Se essa non fosse più densa, emergerebbe dai mari e, secondo il grado della sua leggerezza, sporgerebbe in parte dall’acqua, mentre tutti i mari confluirebbero nella regione opposta.",
     "en": "The earth, if it was not for its greater density, would emerge from the seas, and, according to its degree of levity, would be raised more or less above their surface, the water of the seas flowing backward to the opposite side.",
     "dipende_da": [],
     "figura": {
      "mostra": [],
      "evidenzia": []
     }
    },
    {
     "id": "L3-P10-p8",
     "la": "",
     "it": "Con lo stesso argomento le macchie solari sono più leggere della materia luminosa del Sole sulla quale galleggiano.",
     "en": "By the same argument, the spots of the sun, which float upon the lucid matter thereof, are lighter than that matter;",
     "dipende_da": [],
     "figura": {
      "mostra": [],
      "evidenzia": []
     }
    },
    {
     "id": "L3-P10-p9",
     "la": "",
     "it": "E in qualunque modo si siano formati i pianeti, tutta la materia più grave dell’acqua, nel tempo in cui la massa era fluida, si dirigeva verso il centro.",
     "en": "and, however the planets have been formed while they were yet in fluid masses, all the heavier matter subsided to the centre.",
     "dipende_da": [],
     "figura": {
      "mostra": [],
      "evidenzia": []
     }
    },
    {
     "id": "L3-P10-p10",
     "la": "",
     "it": "Perciò, poiché la terra comune in superficie è circa due volte più grave dell’acqua, e poco più sotto, nelle miniere, si trova circa tre o quattro o anche cinque volte più grave, è verosimile che la quantità di tutta la materia della Terra sia circa cinque o sei volte maggiore che se constasse tutta d’acqua; soprattutto perché si è già mostrato prima che la Terra è circa quattro volte più densa di Giove.",
     "en": "Since, therefore, the common matter of our earth on the surface thereof is about twice as heavy as water, and a little lower, in mines, is found about three, or four, or even five times more heavy, it is probable that the quantity of the whole matter of the earth may be five or six times greater than if it consisted all of water; especially since I have before shewed that the earth is about four times more dense than Jupiter.",
     "dipende_da": [
      "Prop. VIII, Cor. 3"
     ],
     "figura": {
      "mostra": [],
      "evidenzia": [
       "densità media 5–6 volte l’acqua"
      ]
     }
    },
    {
     "id": "L3-P10-p11",
     "la": "",
     "it": "Perciò, se Giove è un poco più denso dell’acqua, nello spazio di trenta giorni, nei quali descrive la lunghezza di 459 suoi semidiametri, perderebbe, in un mezzo della stessa densità della nostra aria, quasi la decima parte del suo moto.",
     "en": "If, therefore, Jupiter is a little more dense than water, in the space of thirty days, in which that planet describes the length of 459 of its semi-diameters, it would, in a medium of the same density with our air, lose almost a tenth part of its motion.",
     "dipende_da": [],
     "figura": {
      "mostra": [
       "Giove in un mezzo come l’aria"
      ],
      "evidenzia": [
       "459 × 1/4586 ≈ 1/10 (nota N10)"
      ]
     }
    },
    {
     "id": "L3-P10-p12",
     "la": "",
     "it": "Ma poiché la resistenza dei mezzi diminuisce nel rapporto del peso e della densità, così che l’acqua, che è 13 3/5 volte più leggera del mercurio, resiste di meno nello stesso rapporto, e l’aria, che è 860 volte più leggera dell’acqua, resiste di meno nello stesso rapporto: se si sale nei cieli, dove il peso del mezzo in cui si muovono i pianeti diminuisce immensamente, la resistenza quasi cesserà.",
     "en": "But since the resistance of mediums decreases in proportion to their weight or density, so that water, which is [SVG 983] times lighter than quicksilver, resists less in that proportion; and air, which is 860 times lighter than water, resists less in the same proportion; therefore in the heavens, where the weight of the medium in which the planets move is immensely diminished, the resistance will almost vanish.",
     "dipende_da": [],
     "figura": {
      "mostra": [],
      "evidenzia": [
       "resistenza ∝ densità del mezzo"
      ]
     },
     "nota": "«13⁤35» = 13 3/5 (Motte [SVG 983])."
    },
    {
     "id": "L3-P10-p13",
     "la": "",
     "it": "Abbiamo mostrato infatti nello Scolio della Prop. XXII del Libro II che, se si salisse all’altezza di duecento miglia sopra la Terra, l’aria vi sarebbe più rada che alla superficie della Terra nel rapporto di 30 a 0,0000000000003998, ossia di 75000000000000 a 1 circa.",
     "en": "It is shewn in the Scholium of Prop. XXII, Book II, that at the height of 200 miles above the earth the air is more rare than it is at the superficies of the earth in the ratio of 30 to 0,0000000000003998, or as 75000000000000 to 1 nearly.",
     "dipende_da": [
      "Libro II, Scolio della Prop. XXII"
     ],
     "figura": {
      "mostra": [],
      "evidenzia": [
       "30 / 0,0000000000003998 = 7,5 × 10¹³"
      ]
     },
     "nota": "Il rimando non trova riscontro nello Scolio della Prop. XXII del Libro II nel testo del 1726 tradotto nel Fascicolo 16 (§ A.9)."
    },
    {
     "id": "L3-P10-p14",
     "la": "",
     "it": "E di qui l’astro di Giove, ruotando in un mezzo della stessa densità di quell’aria superiore, nel tempo di 1000000 di anni non perderebbe per la resistenza del mezzo la milionesima parte del suo moto.",
     "en": "And hence the planet Jupiter, revolving in a medium of the same density with that superior air, would not lose by the resistance of the medium the 1000000th part of its motion in 1000000 years.",
     "dipende_da": [],
     "figura": {
      "mostra": [],
      "evidenzia": []
     },
     "nota": "*partem decimam centesimam millesimam*: «la decima parte della centomillesima», cioè la milionesima; Motte «the 1000000th part»."
    },
    {
     "id": "L3-P10-p15",
     "la": "",
     "it": "Negli spazi più vicini alla Terra, infatti, non si trova nulla che crei resistenza oltre l’aria, le esalazioni e i vapori.",
     "en": "In the spaces near the earth the resistance is produced only by the air, exhalations, and vapours.",
     "dipende_da": [],
     "figura": {
      "mostra": [],
      "evidenzia": []
     }
    },
    {
     "id": "L3-P10-p16",
     "la": "",
     "it": "Quando questi sono stati estratti con grandissima cura da un vaso di vetro cilindrico cavo, i gravi cadono dentro il vetro liberissimamente e senza alcuna resistenza sensibile; lo stesso oro e una piuma sottilissima, lasciati cadere insieme, cadono con uguale velocità e, descrivendo nella caduta un’altezza di quattro, sei o otto piedi, arrivano insieme sul fondo, come si è accertato con l’esperienza.",
     "en": "When these are carefully exhausted by the air-pump from under the receiver, heavy bodies fall within the receiver with perfect freedom, and without the least sensible resistance: gold itself, and the lightest down, let fall together, will descend with equal velocity; and though they fall through a space of four, six, and eight feet, they will come to the bottom at the same time; as appears from experiments.",
     "dipende_da": [],
     "figura": {
      "mostra": [
       "tubo di vetro vuotato",
       "oro e piuma"
      ],
      "evidenzia": [
       "caduta simultanea"
      ]
     },
     "nota": "Motte introduce «air-pump» e «receiver», che il latino non nomina."
    },
    {
     "id": "L3-P10-p17",
     "la": "",
     "it": "E perciò, se si sale nei cieli vuoti di aria e di esalazioni, i pianeti e le comete si muoveranno per quegli spazi senza alcuna resistenza sensibile per lunghissimo tempo.",
     "en": "And therefore the celestial regions being perfectly void of air and exhalations, the planets and comets meeting no sensible resistance in those spaces will continue their motions through them for an immense tract of time.",
     "dipende_da": [],
     "figura": {
      "mostra": [],
      "evidenzia": []
     }
    }
   ],
   "dati": {
    "semidiametri_Giove_in_30_giorni_con_diametro_37_1_4": 481.8,
    "con_diametro_39": 460.2,
    "459_su_4586": 0.1001,
    "rapporto_aria_200_miglia": 75038000000000.0
   },
   "nota": "Il latino è un solo capoverso; Motte va a capo prima di «It is shewn in the Scholium of Prop. XXII»."
  },
  {
   "id": "L3-Hyp1",
   "tipo": "Hypothesis",
   "titolo": "Ipotesi I — il centro del sistema del mondo è in quiete",
   "copertura": [
    "III.G2.42",
    "III.G2.43"
   ],
   "fonti": {
    "la": "",
    "en": "Motte 1846, sezione corrispondente (Hypothesis I)"
   },
   "enunciato": {
    "la": "",
    "it": "Il centro del sistema del mondo è in quiete.",
    "en": "That the centre of the system of the world is immovable."
   },
   "passi": []
  },
  {
   "id": "L3-P11",
   "tipo": "Propositio/Theorema",
   "titolo": "Prop. XI — il centro comune di gravità del sistema è in quiete",
   "copertura": [
    "III.G2.44",
    "III.G2.45"
   ],
   "fonti": {
    "la": "",
    "en": "Motte 1846, sezione corrispondente (Prop. XI)"
   },
   "enunciato": {
    "la": "",
    "it": "Il centro comune di gravità della Terra, del Sole e di tutti i pianeti è in quiete.",
    "en": "That the common centre of gravity of the earth, the sun, and all the planets, is immovable."
   },
   "passi": [
    {
     "id": "L3-P11-p1",
     "la": "",
     "it": "Infatti quel centro (per il Cor. IV delle leggi) o sarà in quiete o avanzerà uniformemente in linea retta.",
     "en": "For (by Cor. 4 of the Laws) that centre either is at rest, or moves uniformly forward in a right line;",
     "dipende_da": [
      "Leggi, Cor. IV"
     ],
     "figura": {
      "mostra": [
       "centro comune di gravità"
      ],
      "evidenzia": [
       "quiete o moto rettilineo uniforme"
      ]
     }
    },
    {
     "id": "L3-P11-p2",
     "la": "",
     "it": "Ma, se quel centro avanzasse sempre, si muoverebbe anche il centro del mondo, contro l’Ipotesi.",
     "en": "but if that centre moved, the centre of the world would move also, against the Hypothesis.",
     "dipende_da": [
      "Ipotesi I"
     ],
     "figura": {
      "mostra": [],
      "evidenzia": []
     }
    }
   ]
  },
  {
   "id": "L3-P12",
   "tipo": "Propositio/Theorema",
   "titolo": "Prop. XII — il Sole si muove, ma resta vicino al centro comune di gravità",
   "copertura": [
    "III.G2.46",
    "III.G2.47",
    "III.G2.48"
   ],
   "fonti": {
    "la": "",
    "en": "Motte 1846, sezione corrispondente (Prop. XII e Cor.)"
   },
   "enunciato": {
    "la": "",
    "it": "Il Sole è agitato da un moto perpetuo, ma non si allontana mai molto dal centro comune di gravità di tutti i pianeti.",
    "en": "That the sun is agitated by a perpetual motion, but never recedes far from the common centre of gravity of all the planets."
   },
   "passi": [
    {
     "id": "L3-P12-p1",
     "la": "",
     "it": "Infatti, poiché (per il Cor. 2 della Prop. VIII) la materia nel Sole sta alla materia in Giove come 1067 a 1, e la distanza di Giove dal Sole sta al semidiametro del Sole in un rapporto un poco maggiore, il centro comune di gravità di Giove e del Sole cadrà in un punto un poco al di sopra della superficie del Sole.",
     "en": "For since (by Cor. 2, Prop. VIII) the quantity of matter in the sun is to the quantity of matter in Jupiter as 1067 to 1; and the distance of Jupiter from the sun is to the semi-diameter of the sun in a proportion but a small matter greater, the common centre of gravity of Jupiter and the sun will fall upon a point a little without the surface of the sun.",
     "dipende_da": [
      "Prop. VIII, Cor. 2"
     ],
     "figura": {
      "mostra": [
       "Sole",
       "Giove",
       "baricentro Sole–Giove"
      ],
      "evidenzia": [
       "distanza/semidiametro solare ≈ 1104 > 1067"
      ]
     }
    },
    {
     "id": "L3-P12-p2",
     "la": "",
     "it": "Con lo stesso argomento, poiché la materia nel Sole sta alla materia in Saturno come 3021 a 1, e la distanza di Saturno dal Sole sta al semidiametro del Sole in un rapporto un poco minore, il centro comune di gravità di Saturno e del Sole cadrà in un punto un poco al di sotto della superficie del Sole.",
     "en": "By the same argument, since the quantity of matter in the sun is to the quantity of matter in Saturn as 3021 to 1, and the distance of Saturn from the sun is to the semi-diameter of the sun in a proportion but a small matter less, the common centre of gravity of Saturn and the sun will fall upon a point a little within the surface of the sun.",
     "dipende_da": [],
     "figura": {
      "mostra": [
       "Saturno",
       "baricentro Sole–Saturno"
      ],
      "evidenzia": [
       "distanza/semidiametro ≈ 2025 < 3021 (nota N12)"
      ]
     }
    },
    {
     "id": "L3-P12-p3",
     "la": "",
     "it": "E, seguendo le tracce dello stesso calcolo, se la Terra e tutti i pianeti stessero da una sola parte del Sole, il centro comune di gravità di tutti disterebbe dal centro del Sole appena un intero diametro del Sole.",
     "en": "And, pursuing the principles of this computation, we should find that though the earth and all the planets were placed on one side of the sun, the distance of the common centre of gravity of all from the centre of the sun would scarcely amount to one diameter of the sun.",
     "dipende_da": [],
     "figura": {
      "mostra": [
       "pianeti allineati da una parte"
      ],
      "evidenzia": [
       "≈ 0,85 diametri solari"
      ]
     }
    },
    {
     "id": "L3-P12-p4",
     "la": "",
     "it": "Negli altri casi la distanza dei centri è sempre minore.",
     "en": "In other cases, the distances of those centres are always less;",
     "dipende_da": [],
     "figura": {
      "mostra": [],
      "evidenzia": []
     }
    },
    {
     "id": "L3-P12-p5",
     "la": "",
     "it": "E perciò, poiché quel centro di gravità è perpetuamente in quiete, il Sole, secondo la varia posizione dei pianeti, si muoverà in ogni direzione, ma non si allontanerà mai molto da quel centro.",
     "en": "and therefore, since that centre of gravity is in perpetual rest, the sun, according to the various positions of the planets, must perpetually be moved every way, but will never recede far from that centre.",
     "dipende_da": [
      "Prop. XI"
     ],
     "figura": {
      "mostra": [
       "traiettoria del Sole attorno al baricentro"
      ],
      "evidenzia": []
     }
    }
   ],
   "nota": "Il Corollario (III.G2.48) è nella copertura senza passi."
  },
  {
   "id": "L3-P13",
   "tipo": "Propositio/Theorema",
   "titolo": "Prop. XIII — orbite ellittiche e perturbazioni di Giove e Saturno",
   "copertura": [
    "III.G2.49",
    "III.G2.50",
    "III.G2.51"
   ],
   "fonti": {
    "la": "",
    "en": "Motte 1846, sezione corrispondente (Prop. XIII)"
   },
   "enunciato": {
    "la": "",
    "it": "I pianeti si muovono in ellissi che hanno un fuoco nel centro del Sole, e con raggi condotti a quel centro descrivono aree proporzionali ai tempi.",
    "en": "The planets move in ellipses which have their common focus in the centre of the sun; and, by radii drawn, to that centre, they describe areas proportional to the times of description."
   },
   "passi": [
    {
     "id": "L3-P13-p1",
     "la": "",
     "it": "Abbiamo discusso sopra di questi moti a partire dai fenomeni.",
     "en": "We have discoursed above of these motions from the Phænomena.",
     "dipende_da": [
      "Fenomeni IV–V"
     ],
     "figura": {
      "mostra": [],
      "evidenzia": []
     }
    },
    {
     "id": "L3-P13-p2",
     "la": "",
     "it": "Ora, conosciuti i principi dei moti, da questi ricaviamo a priori i moti celesti.",
     "en": "Now that we know the principles on which they depend, from those principles we deduce the motions of the heavens à priori.",
     "dipende_da": [],
     "figura": {
      "mostra": [],
      "evidenzia": []
     }
    },
    {
     "id": "L3-P13-p3",
     "la": "",
     "it": "Poiché i pesi dei pianeti verso il Sole sono inversamente come i quadrati delle distanze dal centro del Sole, se il Sole fosse in quiete e gli altri pianeti non agissero gli uni sugli altri, le loro orbite sarebbero ellittiche, con il Sole nel fuoco comune, e le aree sarebbero descritte proporzionalmente ai tempi (per le Propp. I e XI e per il Cor. 1 della Prop. XIII del Libro I); ma le azioni dei pianeti gli uni sugli altri sono piccolissime (tanto che si possono trascurare), e perturbano i moti dei pianeti in ellissi attorno al Sole mobile meno (per la Prop. LXVI del Libro I) che se quei moti si compissero attorno al Sole in quiete.",
     "en": "Because the weights of the planets towards the sun are reciprocally as the squares of their distances from the sun's centre, if the sun was at rest, and the other planets did not mutually act one upon another, their orbits would be ellipses, having the sun in their common focus; and they would describe areas proportional to the times of description, by Prop. I and XI, and Cor. 1, Prop. XIII, Book I. But the mutual actions of the planets one upon another are so very small, that they may be neglected; and by Prop. LXVI, Book I, they less disturb the motions of the planets around the sun in motion than if those motions were performed about the sun at rest.",
     "dipende_da": [
      "Libro I, Prop. I",
      "Libro I, Prop. XI",
      "Libro I, Prop. XIII, Cor. 1",
      "Libro I, Prop. LXVI"
     ],
     "figura": {
      "mostra": [
       "Sole nel fuoco",
       "ellissi dei pianeti"
      ],
      "evidenzia": [
       "forza ∝ 1/r² → ellisse con fuoco nel Sole"
      ]
     },
     "nota": "La trascrizione ha due volte *in se motuo* per *in se mutuo* (§ A.7)."
    },
    {
     "id": "L3-P13-p4",
     "la": "",
     "it": "L’azione di Giove su Saturno, invero, non è del tutto trascurabile.",
     "en": "It is true, that the action of Jupiter upon Saturn is not to be neglected:",
     "dipende_da": [],
     "figura": {
      "mostra": [
       "Sole, Giove, Saturno in congiunzione"
      ],
      "evidenzia": []
     }
    },
    {
     "id": "L3-P13-p5",
     "la": "",
     "it": "Infatti la gravità verso Giove sta alla gravità verso il Sole (a parità di distanze) come 1 a 1067; e perciò nella congiunzione di Giove e Saturno, poiché la distanza di Saturno da Giove sta alla distanza di Saturno dal Sole quasi come 4 a 9, la gravità di Saturno verso Giove starà alla gravità di Saturno verso il Sole come 81 a 16×1067, ossia come 1 a 211 circa.",
     "en": "for the force of gravity towards Jupiter is to the force of gravity towards the sun (at equal distances, Cor. 2, Prop. VIII) as 1 to 1067; and therefore in the conjunction of Jupiter and Saturn, because the distance of Saturn from Jupiter is to the distance of Saturn from the sun almost as 4 to 9, the gravity of Saturn towards Jupiter will be to the gravity of Saturn towards the sun as 81 to 16 × 1067; or, as 1 to about 211.",
     "dipende_da": [],
     "figura": {
      "mostra": [
       "distanze 4 e 9"
      ],
      "evidenzia": [
       "81/(16 × 1067) = 1/210,8"
      ]
     },
     "nota": "Motte aggiunge il rimando «Cor. 2, Prop. VIII» tra parentesi."
    },
    {
     "id": "L3-P13-p6",
     "la": "",
     "it": "E di qui nasce una perturbazione dell’orbita di Saturno, in ogni congiunzione di questo pianeta con Giove, così sensibile che gli astronomi ne restano perplessi.",
     "en": "And hence arises a perturbation of the orb of Saturn in every conjunction of this planet with Jupiter, so sensible, that astronomers are puzzled with it.",
     "dipende_da": [],
     "figura": {
      "mostra": [],
      "evidenzia": []
     }
    },
    {
     "id": "L3-P13-p7",
     "la": "",
     "it": "Secondo la varia posizione del pianeta in queste congiunzioni, la sua eccentricità ora aumenta ora diminuisce, l’afelio ora avanza ora forse arretra, e il moto medio a vicenda è accelerato e ritardato.",
     "en": "As the planet is differently situated in these conjunctions, its eccentricity is sometimes augmented, sometimes diminished; its aphelion is sometimes carried forward, sometimes backward, and its mean motion is by turns accelerated and retarded;",
     "dipende_da": [],
     "figura": {
      "mostra": [],
      "evidenzia": []
     },
     "nota": "Motte omette *forte* («forse»)."
    },
    {
     "id": "L3-P13-p8",
     "la": "",
     "it": "Tutto l’errore nel suo moto attorno al Sole che nasce da una forza così grande (eccetto che nel moto medio) si può tuttavia quasi evitare ponendo il fuoco inferiore della sua orbita nel centro comune di gravità di Giove e del Sole (per la Prop. LXVII del Libro I), e perciò, dove è massimo, supera appena due primi.",
     "en": "yet the whole error in its motion about the sun, though arising from so great a force, may be almost avoided (except in the mean motion) by placing the lower focus of its orbit in the common centre of gravity of Jupiter and the sun (according to Prop. LXVII, Book I), and therefore that error, when it is greatest, scarcely exceeds two minutes;",
     "dipende_da": [
      "Libro I, Prop. LXVII"
     ],
     "figura": {
      "mostra": [
       "baricentro Sole–Giove come fuoco dell’orbita di Saturno"
      ],
      "evidenzia": []
     }
    },
    {
     "id": "L3-P13-p9",
     "la": "",
     "it": "E l’errore massimo nel moto medio supera appena due primi all’anno.",
     "en": "and the greatest error in the mean motion scarcely exceeds two minutes yearly.",
     "dipende_da": [],
     "figura": {
      "mostra": [],
      "evidenzia": []
     }
    },
    {
     "id": "L3-P13-p10",
     "la": "",
     "it": "Nella congiunzione di Giove e Saturno, poi, le gravità acceleratrici del Sole verso Saturno, di Giove verso Saturno e di Giove verso il Sole sono quasi come 16, 81 e 16×81×3021/25, ossia 156609; e perciò la differenza delle gravità del Sole verso Saturno e di Giove verso Saturno sta alla gravità di Giove verso il Sole come 65 a 156609, ossia come 1 a 2409.",
     "en": "But in the conjunction of Jupiter and Saturn, the accelerative forces of gravity of the sun towards Saturn, of Jupiter towards Saturn, and of Jupiter towards the sun, are almost as 16, 81, and [SVG 984] , or 156609; and therefore the difference of the forces of gravity of the sun towards Saturn, and of Jupiter towards Saturn, is to the force of gravity of Jupiter towards the sun as 65 to 156609, or as 1 to 2409.",
     "dipende_da": [],
     "figura": {
      "mostra": [],
      "evidenzia": [
       "16 × 81 × 3021/25 = 156608,6",
       "156609/65 = 2409,4"
      ]
     },
     "nota": "«16×81×302125» della trascrizione = 16×81×3021/25 (Motte [SVG 984]). La trascrizione ha *conjuctione*."
    },
    {
     "id": "L3-P13-p11",
     "la": "",
     "it": "A questa differenza è proporzionale la massima efficacia di Saturno nel perturbare il moto di Giove, e perciò la perturbazione dell’orbita di Giove è molto minore di quella di Saturno.",
     "en": "But the greatest power of Saturn to disturb the motion of Jupiter is proportional to this difference; and therefore the perturbation of the orbit of Jupiter is much less than that of Saturn's.",
     "dipende_da": [],
     "figura": {
      "mostra": [],
      "evidenzia": []
     }
    },
    {
     "id": "L3-P13-p12",
     "la": "",
     "it": "Le perturbazioni delle altre orbite sono ancora molto minori, eccetto che l’orbita della Terra è perturbata sensibilmente dalla Luna.",
     "en": "The perturbations of the other orbits are yet far less, except that the orbit of the earth is sensibly disturbed by the moon.",
     "dipende_da": [],
     "figura": {
      "mostra": [],
      "evidenzia": []
     }
    },
    {
     "id": "L3-P13-p13",
     "la": "",
     "it": "Il centro comune di gravità della Terra e della Luna percorre un’ellisse attorno al Sole posto nel fuoco, e con un raggio condotto al Sole descrive in essa aree proporzionali ai tempi; la Terra invece ruota attorno a questo centro comune con un moto mensile.",
     "en": "The common centre of gravity of the earth and moon moves in an ellipsis about the sun in the focus thereof, and, by a radius drawn to the sun, describes areas proportional to the times of description. But the earth in the mean time by a menstrual motion is revolved about this common centre.",
     "dipende_da": [],
     "figura": {
      "mostra": [
       "baricentro Terra–Luna sull’ellisse"
      ],
      "evidenzia": [
       "moto mensile della Terra"
      ]
     }
    }
   ]
  },
  {
   "id": "L3-P14",
   "tipo": "Propositio/Theorema",
   "titolo": "Prop. XIV — afeli e nodi in quiete",
   "copertura": [
    "III.G2.52",
    "III.G2.53",
    "III.G2.54",
    "III.G2.55"
   ],
   "fonti": {
    "la": "",
    "en": "Motte 1846, sezione corrispondente (Prop. XIV e Cor. 1–2)"
   },
   "enunciato": {
    "la": "",
    "it": "Gli afeli e i nodi delle orbite sono in quiete.",
    "en": "The aphelions and nodes of the orbits of the planets are fixed."
   },
   "passi": [
    {
     "id": "L3-P14-p1",
     "la": "",
     "it": "Gli afeli sono in quiete per la Prop. XI del Libro I, come pure i piani delle orbite, per la Prop. I dello stesso Libro; ed essendo in quiete i piani, sono in quiete i nodi.",
     "en": "The aphelions are immovable by Prop. XI, Book I; and so are the planes of the orbits, by Prop. I of the same Book. And if the planes are fixed, the nodes must be so too.",
     "dipende_da": [
      "Libro I, Prop. XI",
      "Libro I, Prop. I"
     ],
     "figura": {
      "mostra": [
       "orbita",
       "piano dell’orbita",
       "linea dei nodi"
      ],
      "evidenzia": []
     }
    },
    {
     "id": "L3-P14-p2",
     "la": "",
     "it": "Tuttavia dalle azioni reciproche dei pianeti e delle comete in rivoluzione nasceranno alcune disuguaglianze, che però per la loro piccolezza qui si possono trascurare.",
     "en": "It is true, that some inequalities may arise from the mutual actions of the planets and comets in their revolutions; but these will be so small, that they may be here passed by.",
     "dipende_da": [],
     "figura": {
      "mostra": [],
      "evidenzia": []
     }
    }
   ],
   "nota": "I Cor. 1–2 sono nella copertura senza passi."
  },
  {
   "id": "L3-P14-Sch",
   "tipo": "Scholium",
   "titolo": "Scolio della Prop. XIV — il moto degli afeli dei pianeti interni",
   "copertura": [
    "III.G2.56"
   ],
   "fonti": {
    "la": "",
    "en": "Motte 1846, sezione corrispondente (Scholium)"
   },
   "passi": [
    {
     "id": "L3-P14-Sch-p1",
     "la": "",
     "it": "Poiché i pianeti più vicini al Sole (cioè Mercurio, Venere, la Terra e Marte), per la piccolezza dei loro corpi, agiscono poco gli uni sugli altri, i loro afeli e nodi saranno in quiete, se non in quanto siano turbati dalle forze di Giove, di Saturno e dei corpi superiori.",
     "en": "Since the planets near the sun (viz. Mercury, Venus, the Earth, and Mars) are so small that they can act with but little force upon each other, therefore their aphelions and nodes must be fixed, excepting in so far as they are disturbed by the actions of Jupiter and Saturn, and other higher bodies.",
     "dipende_da": [],
     "figura": {
      "mostra": [
       "orbite di Mercurio, Venere, Terra, Marte"
      ],
      "evidenzia": []
     }
    },
    {
     "id": "L3-P14-Sch-p2",
     "la": "",
     "it": "E di qui si può ricavare per la teoria della gravità che i loro afeli si muovono un poco in conseguenza rispetto alle stelle fisse, e ciò nella proporzione sesquiplicata delle distanze di questi pianeti dal Sole.",
     "en": "And hence we may find, by the theory of gravity, that their aphelions move a little in consequentia, in respect of the fixed stars, and that in the sesquiplicate proportion of their several distances from the sun.",
     "dipende_da": [],
     "figura": {
      "mostra": [],
      "evidenzia": [
       "moto dell’afelio ∝ a^(3/2)"
      ]
     }
    },
    {
     "id": "L3-P14-Sch-p3",
     "la": "",
     "it": "Così, se l’afelio di Marte in cento anni compie 33′ 20″ in conseguenza rispetto alle stelle fisse, gli afeli della Terra, di Venere e di Mercurio in cento anni compiranno rispettivamente 17′ 40″, 10′ 53″ e 4′ 16″.",
     "en": "So that if the aphelion of Mars, in the space of a hundred years, is carried 33' 20'' in consequentia, in respect of the fixed stars, the aphelions of the Earth, of Venus, and of Mercury, will in a hundred years be carried forwards 17' 40''; 10' 53'', and 4' 16'', respectively.",
     "dipende_da": [],
     "figura": {
      "mostra": [
       "tabella dei moti secolari"
      ],
      "evidenzia": [
       "ricalcolo: 17′ 43″, 10′ 54″, 4′ 16″ (nota N14)"
      ]
     },
     "nota": "La trascrizione ha *in annis centrum* (seconda occorrenza) per *centum*."
    },
    {
     "id": "L3-P14-Sch-p4",
     "la": "",
     "it": "E questi moti, per la loro piccolezza, sono trascurati in questa proposizione.",
     "en": "But these motions are so inconsiderable, that we have neglected them in this Proposition.",
     "dipende_da": [],
     "figura": {
      "mostra": [],
      "evidenzia": []
     }
    }
   ],
   "dati": {
    "distanze_Fen_IV": {
     "Marte": 152369,
     "Terra": 100000,
     "Venere": 72333,
     "Mercurio": 38710
    },
    "Newton_secondi_per_secolo": {
     "Marte": 2000,
     "Terra": 1060,
     "Venere": 653,
     "Mercurio": 256
    },
    "ricalcolati": {
     "Terra": 1063.4,
     "Venere": 654.2,
     "Mercurio": 256.1
    }
   }
  }
 ]
}
```
