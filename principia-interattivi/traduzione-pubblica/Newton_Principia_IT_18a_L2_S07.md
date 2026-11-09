> **Copia pubblica.** In questa versione i campi `"la"` della Parte B sono vuoti: le frasi latine vengono dalla trascrizione del Newton Project, che non si ridistribuisce. Il latino del 1726 si legge su newtonproject.ox.ac.uk.

# Isaac Newton
# Principi matematici della filosofia naturale

## Fascicolo 18a — Libro II, Sezione VII (prima parte): il moto dei fluidi e la resistenza dei proiettili, Propp. XXXII–XXXVII

**Nuova traduzione italiana di lavoro dal latino del 1726, confrontata con l’inglese di Andrew Motte nell’edizione del 1846.**

Versione 0.1 — 8 novembre 2026. Preparata con Claude (Anthropic) per Massimo Bosetti.

### Stato e perimetro

Questo fascicolo traduce la **prima parte della Sezione VII** del Libro II, *De motu fluidorum & resistentia projectilium*: dal titolo della Sezione fino alla fine della Prop. XXXVII compresa, cioè le Proposizioni XXXII–XXXVII, il Lemma IV, tutti i corollari e i tre scolii che precedono il Lemma V (allo scolio della Prop. XXXIV, della Prop. XXXV e della Prop. XXXVII). La seconda parte della Sezione (Lemmi V–VII, Propp. XXXVIII–XL e lo Scolio finale con gli esperimenti di caduta) è affidata al Fascicolo 18b. È una traduzione di lavoro, non un’edizione critica validata.

Gli identificatori **II.S7.01–II.S7.64** e i titoli tematici tra parentesi sono aggiunte editoriali. Servono a orientare la lettura e a controllare la completezza; il Fascicolo 18b riparte da II.S7.65 (il coordinatore rinumererà se necessario). I numeri romani delle proposizioni, dei teoremi, dei problemi e dei lemmi, e i numeri dei corollari e dei casi, appartengono al testo originale. Le integrazioni del curatore sono tra parentesi quadre. Le note poste dopo la traduzione non fanno parte del testo di Newton.

In coda al fascicolo c’è la **Parte B**, con i dati strutturati per le pagine interattive di 9 unità con costruzione geometrica: Prop. XXXIV e il suo Scolio; Prop. XXXV, Cor. 6; Prop. XXXVI (costruzione e Caso 1) e i suoi Cor. 3, 7 e 8; Prop. XXXVII e il suo Scolio.

### Fonti effettivamente consultate

1. **Latino di riferimento.** Isaac Newton, *Philosophiæ Naturalis Principia Mathematica*, terza edizione, Londra, 1726, Libro II, Sezione VII, **pp. 318–340** per la parte tradotta (l’inizio della Sezione cade a p. 318; i marcatori di pagina della trascrizione usati qui vanno da ‹319› a ‹340›; il Lemma V comincia a p. 340). Trascrizione normalizzata del Newton Project, documento **NATP00088**, estratta in testo semplice senza correzioni: `fonti/latino-1726-L2-S07.md`, righe 12–166. Figure citate: NATP00088-51…62 (non disponibili).
2. **Inglese di confronto.** *Newton’s Principia*, traduzione di Andrew Motte, New York, Daniel Adee, 1846, Section VII, **sezione corrispondente** (dall’inizio della Section VII fino alla fine dello Scholium della Prop. XXXVII; l’estratto non contiene marcatori di pagina). Estratto: `fonti/motte-1846-L2-S07.md`, righe 1–941 (Project Gutenberg n. 76404). Le formule stampate come immagini compaiono come `[SVG n]`: le sedici immagini di questa parte sono state rese con `rsvg-convert` dall’EPUB (`src_epub/OEBPS/`) e lette una per una (§ A.10).
3. **Brief comune** del Libro I (`strumenti/BRIEF.md`), **addendum del Libro II** (`ISTRUZIONI-TRADUTTORE.md`), modelli di formato **Fascicolo 3** e **Fascicolo 5**; per i rimandi, il Fascicolo 5 (Libro I, Prop. IV) e il Fascicolo 3 (Leggi e corollari); per i rimandi interni al Libro II, le trascrizioni latine delle Sezioni II (Prop. V) e V (Prop. XIX).

Non ho consultato né riprodotto traduzioni moderne. Non ho potuto vedere la stampa del 1726, la stampa di Motte né le figure originali: le relazioni geometriche sono ricostruite dalle sole lettere del testo.

### Criteri di traduzione

- Il testo guida è il latino; l’inglese di Motte serve a controllare le interpretazioni ed è annotato quando aggiunge, omette o si discosta.
- Si applica il **glossario comune** del brief e il **glossario del Libro II** dell’addendum: *resistentia* «resistenza», *medium* «mezzo», *fluidum* «fluido», *densitas* «densità», *compressio* «compressione», *vis elastica* «forza elastica», *medium rarum* «mezzo rado», *spatium non resistens* «spazio non resistente», *hyperbola* «iperbole», *asymptotos* «asintoto», *area hyperbolica* «area iperbolica», *logarithmus* «logaritmo», *pondus* «peso», *gravitas* «gravità», *particulæ fluidi* «particelle del fluido», *vis centrifuga* «forza centrifuga», *vas* «vaso», *foramen* «foro», *canalis* «canale», *cataracta* «cateratta» (nota N9), *aer* «aria», *aqua* «acqua», *argentum vivum* «mercurio (argento vivo)» alla prima occorrenza, *globus* «globo», *cylindrus* «cilindro», *sphæra* «sfera», *conus* «cono», *solidum* «solido», *digitus* «pollice», *experimentum* «esperimento», *Scholium* «Scolio»; *ratio duplicata / subduplicata* «rapporto duplicato / subduplicato», *reciproce / inverse* «inversamente», *conjunctim* «considerate congiuntamente», *in directum* «in linea retta», *determinatio* «direzione», *nisi quatenus* «se non in quanto», *latus rectum* «lato retto», *impetus* «impeto»; Q.E.D. «C.V.D.», Q.E.I. «C.V.T.».
- Le estensioni del glossario proprie di questo fascicolo sono elencate e motivate nel § A.0.
- Gli enunciati latini all’infinito sono resi con l’indicativo; l’enunciato dei problemi (*invenire resistentiam*, *definire motum*) con l’infinito italiano.
- Le abbreviazioni «BE quad.», «EFq», «GR cub.» sono scritte BE², EF², GR³; le frazioni appiattite dalla trascrizione («BE quad.CB», «tMT+t», «T+tT», «12GH», «EFq−12PQq», «512 ad 612») sono rese con la barra o con ½ (BE²/CB, tM/(T+t), (T+t)/T, ½GH, EF²−½PQ², 5½ a 6½), dichiarando la lettura nell’apparato (A.9). Nessuna formula moderna entra nel testo tradotto.
- I numeri sono riprodotti come nel latino (in cifre o in lettere); il separatore decimale di Newton, la virgola (*2,302585092994*), è conservato.

---
## Traduzione italiana

### Sezione VII. Il moto dei fluidi e la resistenza dei proiettili

### Proposizione XXXII. Teorema XXVI (sistemi simili di particelle)

**[II.S7.01]** **Se due sistemi simili di corpi constano di un numero uguale di particelle, e le particelle corrispondenti sono simili e proporzionali, ciascuna in un sistema a ciascuna nell’altro, e sono situate in modo simile fra loro, e hanno l’una rispetto all’altra un rapporto dato di densità, e cominciano a muoversi fra loro in modo simile in tempi proporzionali (quelle che sono in un sistema fra loro, e quelle che sono nell’altro fra loro); e se quelle che sono nello stesso sistema non si toccano a vicenda se non negli istanti delle riflessioni, e non si attraggono né si respingono a vicenda se non con forze acceleratrici che stanno come i diametri delle particelle corrispondenti inversamente e i quadrati delle velocità direttamente: dico che le particelle di quei sistemi continueranno a muoversi fra loro in modo simile in tempi proporzionali.**

**[II.S7.02]** Dico che corpi simili e situati in modo simile si muovono fra loro in modo simile in tempi proporzionali quando le loro posizioni reciproche, alla fine di quei tempi, sono sempre simili: per esempio se si confrontano le particelle di un sistema con le particelle corrispondenti dell’altro. Perciò saranno proporzionali i tempi nei quali le particelle corrispondenti descrivono parti simili e proporzionali di figure simili. Se dunque vi sono due sistemi di questo genere, le particelle corrispondenti, per la somiglianza dei moti iniziali, continueranno a muoversi in modo simile finché non s’incontrano a vicenda. Infatti, se non sono agitate da alcuna forza, procederanno uniformemente in linee rette, per la Legge I del moto. Se invece si agitano a vicenda con certe forze, e quelle forze stanno come i diametri delle particelle corrispondenti inversamente e i quadrati delle velocità direttamente, allora, poiché le posizioni delle particelle sono simili e le forze proporzionali, le forze totali da cui le particelle corrispondenti sono agitate, composte (per il secondo corollario delle leggi) dalle singole forze agenti, avranno direzioni simili, come se guardassero a centri situati in modo simile fra le particelle; e quelle forze totali staranno fra loro come le singole forze componenti, cioè come i diametri delle particelle corrispondenti inversamente e i quadrati delle velocità direttamente: e perciò faranno sì che le particelle corrispondenti continuino a descrivere figure simili. Così andranno le cose (per i Cor. 1 e 8 della Prop. IV del Libro I), purché quei centri siano in quiete. Se invece si muovono, poiché per la somiglianza delle traslazioni le loro posizioni fra le particelle dei sistemi restano simili, si produrranno cambiamenti simili nelle figure che le particelle descrivono. Saranno dunque simili i moti delle particelle corrispondenti e simili fino ai loro primi incontri, e perciò simili gli incontri, simili le riflessioni, e poi (per quanto già mostrato) simili i moti fra loro finché di nuovo non s’imbattano l’una nell’altra, e così via all’infinito. C.V.D.

**[II.S7.03]** *Cor. 1.* Di qui, se due corpi qualsiasi, simili e situati in modo simile rispetto alle particelle corrispondenti dei sistemi, cominciano a muoversi fra di esse in modo simile in tempi proporzionali, e le loro grandezze e densità stanno fra loro come le grandezze e le densità delle particelle corrispondenti, questi continueranno a muoversi in modo simile in tempi proporzionali. Il rapporto è infatti lo stesso per le parti maggiori di entrambi i sistemi e per le particelle.

**[II.S7.04]** *Cor. 2.* E se tutte le parti simili e situate in modo simile dei sistemi sono in quiete fra loro, e due di esse, maggiori delle altre e corrispondenti l’una all’altra nei due sistemi, cominciano a muoversi lungo linee situate in modo simile con un moto simile qualsiasi, esse ecciteranno moti simili nelle altre parti dei sistemi e continueranno a muoversi fra quelle parti in modo simile in tempi proporzionali; e perciò descriveranno spazi proporzionali ai loro diametri.

### Proposizione XXXIII. Teorema XXVII (legge di similitudine della resistenza)

**[II.S7.05]** **Poste le stesse cose, dico che le parti maggiori dei sistemi subiscono resistenza nel rapporto composto dal rapporto duplicato delle loro velocità, dal rapporto duplicato dei diametri e dal rapporto della densità delle parti dei sistemi.**

**[II.S7.06]** La resistenza infatti nasce in parte dalle forze centripete o centrifughe con cui le particelle dei sistemi si agitano a vicenda, in parte dagli incontri e dalle riflessioni delle particelle e delle parti maggiori. Le resistenze del primo genere stanno fra loro come le forze motrici totali da cui nascono, cioè come le forze acceleratrici totali e le quantità di materia nelle parti corrispondenti; ossia (per ipotesi) come i quadrati delle velocità direttamente, le distanze delle particelle corrispondenti inversamente e le quantità di materia nelle parti corrispondenti direttamente: e perciò, poiché le distanze delle particelle di un sistema stanno alle distanze corrispondenti delle particelle dell’altro come il diametro di una particella o di una parte nel primo sistema sta al diametro della particella o della parte corrispondente nell’altro, e le quantità di materia stanno come le densità delle parti e i cubi dei diametri, le resistenze stanno fra loro come i quadrati delle velocità, i quadrati dei diametri e le densità delle parti dei sistemi. C.V.D. Le resistenze del secondo genere stanno come i numeri delle riflessioni corrispondenti e le forze, considerati congiuntamente. Ma i numeri delle riflessioni stanno fra loro come le velocità delle parti corrispondenti direttamente e gli spazi fra le loro riflessioni inversamente. E le forze delle riflessioni stanno come le velocità, le grandezze e le densità delle parti corrispondenti considerate congiuntamente; cioè come le velocità, i cubi dei diametri e le densità delle parti. E, riuniti tutti questi rapporti, le resistenze delle parti corrispondenti stanno fra loro come i quadrati delle velocità, i quadrati dei diametri e le densità delle parti considerati congiuntamente. C.V.D.

**[II.S7.07]** *Cor. 1.* Perciò, se quei sistemi sono due fluidi elastici alla maniera dell’aria, e le loro parti sono in quiete fra loro; e due corpi simili, proporzionali alle parti dei fluidi quanto a grandezza e densità e situati in modo simile fra quelle parti, sono lanciati in un modo qualsiasi lungo linee situate in modo simile; e le forze acceleratrici con cui le particelle dei fluidi si agitano a vicenda stanno come i diametri dei corpi lanciati inversamente e i quadrati delle velocità direttamente: quei corpi ecciteranno nei fluidi moti simili in tempi proporzionali, e descriveranno spazi simili e proporzionali ai loro diametri.

**[II.S7.08]** *Cor. 2.* Ne segue che nello stesso fluido un proiettile veloce subisce una resistenza che è, con ottima approssimazione, nel rapporto duplicato della velocità. Infatti, se le forze con cui le particelle distanti si agitano a vicenda crescessero nel rapporto duplicato della velocità, la resistenza sarebbe esattamente nello stesso rapporto duplicato; e perciò in un mezzo le cui parti, distanti l’una dall’altra, non si agitano a vicenda con alcuna forza, la resistenza è esattamente nel rapporto duplicato della velocità. Siano dunque tre mezzi A, B, C, costituiti di parti simili e uguali, disposte regolarmente a distanze uguali. Le parti dei mezzi A e B si respingano a vicenda con forze che stanno fra loro come T e V; quelle del mezzo C siano del tutto prive di forze di questo genere. E se quattro corpi uguali D, E, F, G si muovono in questi mezzi, i primi due D ed E nei primi due A e B, e gli altri due F e G nel terzo C; e la velocità del corpo D sta alla velocità del corpo E, e la velocità del corpo F alla velocità del corpo G, nel rapporto subduplicato delle forze T alle forze V: la resistenza del corpo D starà alla resistenza del corpo E, e la resistenza del corpo F alla resistenza del corpo G, nel rapporto duplicato delle velocità; e perciò la resistenza del corpo D starà alla resistenza del corpo F come la resistenza del corpo E sta alla resistenza del corpo G. Siano i corpi D e F di uguale velocità, come pure i corpi E e G; e, aumentando in un rapporto qualsiasi le velocità dei corpi D e F e diminuendo nello stesso rapporto duplicato le forze delle particelle del mezzo B, il mezzo B si avvicinerà a piacere alla forma e alla condizione del mezzo C; e perciò le resistenze dei corpi uguali e di uguale velocità E e G in questi mezzi si avvicineranno continuamente all’uguaglianza, così che la loro differenza diventi infine minore di qualsiasi quantità data. Ne segue che, poiché le resistenze dei corpi D e F stanno fra loro come le resistenze dei corpi E e G, anche queste si avvicineranno in modo simile al rapporto di uguaglianza. Le resistenze dei corpi D e F, quando si muovono velocissimamente, sono dunque uguali con ottima approssimazione: e perciò, poiché la resistenza del corpo F è nel rapporto duplicato della velocità, la resistenza del corpo D sarà, con ottima approssimazione, nello stesso rapporto.

**[II.S7.09]** *Cor. 3.* La resistenza di un corpo mosso velocissimamente in un fluido elastico qualsiasi è quasi la stessa che se le parti del fluido fossero prive delle loro forze centrifughe e non si respingessero a vicenda: purché la forza elastica del fluido nasca dalle forze centrifughe delle particelle e la velocità sia così grande che le forze non abbiano abbastanza tempo per agire.

**[II.S7.10]** *Cor. 4.* Perciò, poiché le resistenze di corpi simili e di uguale velocità, in un mezzo le cui parti distanti non si respingono a vicenda, stanno come i quadrati dei diametri, anche le resistenze di corpi di uguale velocità e mossi molto velocemente in un fluido elastico stanno, con ottima approssimazione, come i quadrati dei diametri.

**[II.S7.11]** *Cor. 5.* E poiché corpi simili, uguali e di uguale velocità, in mezzi della stessa densità le cui particelle non si respingono a vicenda, siano quelle particelle più numerose e più piccole oppure meno numerose e più grandi, urtano in tempi uguali contro una quantità uguale di materia, le imprimono una quantità di moto uguale e a loro volta (per la terza legge del moto) ne subiscono una reazione uguale, cioè incontrano una resistenza uguale, è manifesto anche che in fluidi elastici della stessa densità, quando si muovono velocissimamente, le loro resistenze sono uguali con ottima approssimazione, sia che quei fluidi constino di particelle più grossolane, sia che siano costituiti delle più sottili di tutte. Dalla sottigliezza del mezzo la resistenza dei proiettili mossi molto velocemente non è diminuita di molto.

**[II.S7.12]** *Cor. 6.* Tutte queste cose valgono così nei fluidi la cui forza elastica trae origine dalle forze centrifughe delle particelle. Se invece quella forza nasce d’altrove, per esempio dall’espansione delle particelle a somiglianza della lana o dei rami degli alberi, o da qualsiasi altra causa per la quale i moti delle particelle fra loro sono resi meno liberi, la resistenza, per la minore fluidità del mezzo, sarà maggiore che nei corollari precedenti.

### Proposizione XXXIV. Teorema XXVIII (globo e cilindro in un mezzo rado)

**[II.S7.13]** **Se un globo e un cilindro, descritti su diametri uguali, si muovono con velocità uguale, nel verso dell’asse del cilindro, in un mezzo rado costituito di particelle uguali e disposte liberamente a distanze uguali l’una dall’altra, la resistenza del globo sarà la metà della resistenza del cilindro.**

**[II.S7.14]** Poiché infatti l’azione del mezzo sul corpo è la stessa (per il Cor. 5 delle leggi) sia che il corpo si muova in un mezzo in quiete, sia che le particelle del mezzo urtino con la stessa velocità il corpo in quiete, consideriamo il corpo come in quiete e vediamo con quale impeto sarà sollecitato dal mezzo in moto. Rappresenti dunque ABKI un corpo sferico descritto con centro C e semidiametro CA, e le particelle del mezzo incidano con una velocità data su quel corpo sferico lungo rette parallele ad AC; e sia FB una retta di questo genere. Su di essa si prenda LB uguale al semidiametro CB, e si conduca BD tangente alla sfera in B. Su KC e su BD si abbassino le perpendicolari BE, LD; e la forza con cui una particella del mezzo, incidendo obliquamente lungo la retta FB, colpisce il globo in B, starà alla forza con cui la stessa particella colpirebbe perpendicolarmente in b il cilindro ONGQ descritto attorno al globo con asse ACI, come LD sta a LB, ossia come BE sta a BC. Di nuovo, l’efficacia di questa forza a muovere il globo nel verso della sua incidenza FB, ossia AC, sta alla sua efficacia a muovere il globo nel verso della sua direzione, cioè nel verso della retta BC lungo la quale spinge direttamente il globo, come BE sta a BC. E, riuniti i rapporti, l’efficacia di una particella che incide obliquamente sul globo lungo la retta FB, a muoverlo nel verso della sua incidenza, sta all’efficacia della stessa particella che incide perpendicolarmente sul cilindro lungo la stessa retta, a muoverlo nello stesso verso, come il quadrato di BE sta al quadrato di BC. Perciò se su bE, che è perpendicolare alla base circolare NAO del cilindro e uguale al raggio AC, si prende bH uguale a BE²/CB, bH starà a bE come l’effetto della particella sul globo sta all’effetto della particella sul cilindro. E perciò il solido occupato da tutte le rette bH starà al solido occupato da tutte le rette bE come l’effetto di tutte le particelle sul globo sta all’effetto di tutte le particelle sul cilindro. Ma il primo solido è un paraboloide descritto con vertice C, asse CA e lato retto CA, e il secondo solido è il cilindro circoscritto al paraboloide: ed è noto che il paraboloide è la metà del cilindro circoscritto. Dunque la forza totale del mezzo sul globo è la metà della sua forza totale sul cilindro. E perciò, se le particelle del mezzo fossero in quiete e il cilindro e il globo si muovessero con velocità uguale, la resistenza del globo sarebbe la metà della resistenza del cilindro. C.V.D.

#### Scolio (solidi di minima resistenza)

**[II.S7.15]** *Scolio.* Con lo stesso metodo si possono confrontare fra loro altre figure quanto alla resistenza, e trovare quelle che sono più adatte a continuare i loro moti nei mezzi resistenti. Per esempio, se sulla base circolare CEBH, descritta con centro O e raggio OC, e con l’altezza OD, si deve costruire il tronco di cono CBGF che, fra tutti i tronchi costruiti con la stessa base e la stessa altezza e avanzanti verso D nel verso del loro asse, incontri la minima resistenza: dividi a metà l’altezza OD in Q e prolunga OQ fino a S, in modo che QS sia uguale a QC; e S sarà il vertice del cono di cui si cerca il tronco.

**[II.S7.16]** Di qui, per inciso, poiché l’angolo CSB è sempre acuto, ne consegue che, se il solido ADBE è generato dalla rivoluzione di una figura ellittica od ovale ADBE attorno all’asse AB, e la figura generatrice è toccata da tre rette FG, GH, HI nei punti F, B e I, con la condizione che GH sia perpendicolare all’asse nel punto di contatto B, e FG, HI formino con la stessa GH angoli FGB, BHI di 135 gradi, il solido generato dalla rivoluzione della figura ADFGHIE attorno allo stesso asse AB incontra una resistenza minore del solido precedente; purché entrambi avanzino nel verso del loro asse AB e l’estremità B di ciascuno vada avanti. E questa proposizione, ritengo, non sarà inutile nella costruzione delle navi.

**[II.S7.17]** Che se la figura DNFG è una curva tale che, se da un suo punto qualsiasi N si abbassa sull’asse AB la perpendicolare NM, e dal punto dato G si conduce la retta GR parallela alla retta tangente alla figura in N, che tagli l’asse prolungato in R, MN sta a GR come GR³ sta a 4BR×GB², il solido descritto dalla rivoluzione di questa figura attorno all’asse AB, muovendosi da A verso B nel suddetto mezzo rado, incontrerà una resistenza minore di qualsiasi altro solido circolare descritto con la stessa lunghezza e la stessa larghezza.

### Proposizione XXXV. Problema VII (resistenza di un globo in un mezzo rado)

**[II.S7.18]** **Se un mezzo rado è costituito di particelle piccolissime, in quiete, uguali e disposte liberamente a distanze uguali l’una dall’altra: trovare la resistenza di un globo che avanza uniformemente in questo mezzo.**

**[II.S7.19]** *Caso 1.* S’immagini un cilindro, descritto con lo stesso diametro e la stessa altezza, avanzare con la stessa velocità, nel senso della lunghezza del suo asse, nello stesso mezzo. E supponiamo che le particelle del mezzo su cui incide il globo o il cilindro rimbalzino con la massima forza di riflessione possibile. E poiché la resistenza del globo (per la proposizione precedente) è la metà della resistenza del cilindro, e il globo sta al cilindro come due sta a tre, e il cilindro, incidendo perpendicolarmente sulle particelle e riflettendole al massimo grado, comunica loro il doppio della propria velocità, il cilindro, nel tempo in cui avanzando uniformemente descrive metà della lunghezza del suo asse, comunicherà alle particelle un moto che sta all’intero moto del cilindro come la densità del mezzo sta alla densità del cilindro; e il globo, nel tempo in cui avanzando uniformemente descrive l’intera lunghezza del suo diametro, comunicherà alle particelle lo stesso moto; e nel tempo in cui descrive due terzi del suo diametro comunicherà alle particelle un moto che sta all’intero moto del globo come la densità del mezzo sta alla densità del globo. E perciò il globo subisce una resistenza che sta alla forza con cui tutto il suo moto potrebbe essere tolto o generato nel tempo in cui descrive due terzi del suo diametro, come la densità del mezzo sta alla densità del globo.

**[II.S7.20]** *Caso 2.* Supponiamo che le particelle del mezzo che incidono sul globo o sul cilindro non siano riflesse; il cilindro, incidendo perpendicolarmente sulle particelle, comunicherà loro la sua velocità semplice, e perciò subisce una resistenza che è la metà di quella del caso precedente; e anche la resistenza del globo sarà la metà di prima.

**[II.S7.21]** *Caso 3.* Supponiamo che le particelle del mezzo rimbalzino dal globo con una forza di riflessione né massima né nulla, ma intermedia; e la resistenza del globo sarà, nello stesso rapporto intermedio, fra la resistenza del primo caso e la resistenza del secondo. C.V.T.

**[II.S7.22]** *Cor. 1.* Di qui, se il globo e le particelle sono infinitamente duri e privi di ogni forza elastica, e perciò anche di ogni forza di riflessione, la resistenza del globo starà alla forza con cui tutto il suo moto potrebbe essere tolto o generato, nel tempo in cui il globo descrive quattro terzi del suo diametro, come la densità del mezzo sta alla densità del globo.

**[II.S7.23]** *Cor. 2.* La resistenza del globo, a parità delle altre condizioni, è nel rapporto duplicato della velocità.

**[II.S7.24]** *Cor. 3.* La resistenza del globo, a parità delle altre condizioni, è nel rapporto duplicato del diametro.

**[II.S7.25]** *Cor. 4.* La resistenza del globo, a parità delle altre condizioni, sta come la densità del mezzo.

**[II.S7.26]** *Cor. 5.* La resistenza del globo è nel rapporto composto dal rapporto duplicato della velocità, dal rapporto duplicato del diametro e dal rapporto della densità del mezzo.

**[II.S7.27]** *Cor. 6.* E il moto del globo, insieme con la sua resistenza, si può rappresentare così. Sia AB il tempo in cui il globo, per la sua resistenza continuata uniformemente, può perdere tutto il suo moto. Su AB s’innalzino le perpendicolari AD, BC. E sia BC quel moto totale, e per il punto C, con asintoti AD, AB, si descriva l’iperbole CF. Si prolunghi AB fino a un punto qualsiasi E. S’innalzi la perpendicolare EF, che incontri l’iperbole in F. Si completi il parallelogramma CBEG, e si conduca AF, che incontri BC in H. E se il globo, in un tempo qualsiasi BE, con il suo moto iniziale BC continuato uniformemente, descrive in un mezzo non resistente lo spazio CBEG rappresentato dall’area del parallelogramma, lo stesso globo in un mezzo resistente descriverà lo spazio CBEF rappresentato dall’area dell’iperbole, e il suo moto alla fine di quel tempo sarà rappresentato dall’ordinata EF dell’iperbole, perduta la parte FG del suo moto. E la sua resistenza alla fine dello stesso tempo sarà rappresentata dalla lunghezza BH, perduta la parte CH della resistenza. Tutto ciò risulta dai Cor. 1 e 3 della Prop. V del Libro II.

**[II.S7.28]** *Cor. 7.* Di qui, se il globo nel tempo T, per la resistenza R continuata uniformemente, perde tutto il suo moto M, lo stesso globo nel tempo t, in un mezzo resistente, per la resistenza R decrescente nel rapporto duplicato della velocità, perderà la parte tM/(T+t) del suo moto M, mentre resterà la parte TM/(T+t); e descriverà uno spazio che sta allo spazio descritto nello stesso tempo t con il moto uniforme M come il logaritmo del numero (T+t)/T, moltiplicato per il numero 2,302585092994, sta al numero t/T, perché l’area iperbolica BCFE sta al rettangolo BCGE in questa proporzione.

#### Scolio (mezzi non continui e mezzi continui)

**[II.S7.29]** *Scolio.* In questa proposizione ho esposto la resistenza e il ritardo dei proiettili sferici nei mezzi non continui, e ho mostrato che questa resistenza sta alla forza con cui tutto il moto del globo potrebbe essere tolto o generato nel tempo in cui il globo, con velocità continuata uniformemente, descrive due terzi del suo diametro, come la densità del mezzo sta alla densità del globo, purché il globo e le particelle del mezzo siano sommamente elastici e abbiano la massima forza di riflessione; e che questa forza è la metà quando il globo e le particelle del mezzo sono infinitamente duri e del tutto privi di forza di riflessione. Nei mezzi continui, invece, come sono l’acqua, l’olio caldo e il mercurio (argento vivo), nei quali il globo non incide immediatamente su tutte le particelle del fluido che generano la resistenza, ma preme soltanto le particelle più vicine, e queste premono altre, e queste altre ancora, la resistenza è ancora la metà. In mezzi di questo genere, fluidissimi, il globo subisce appunto una resistenza che sta alla forza con cui tutto il suo moto potrebbe essere tolto o generato nel tempo in cui, con quel moto continuato uniformemente, descrive otto terzi del suo diametro, come la densità del mezzo sta alla densità del globo. Questo cercheremo di mostrarlo in ciò che segue.

### Proposizione XXXVI. Problema VIII (efflusso dell’acqua da un vaso)

**[II.S7.30]** **Determinare il moto dell’acqua che esce da un vaso cilindrico attraverso un foro praticato nel fondo.**

**[II.S7.31]** Sia ACDB un vaso cilindrico, AB la sua bocca superiore, CD il fondo parallelo all’orizzonte, EF un foro circolare nel mezzo del fondo, G il centro del foro e GH l’asse del cilindro, perpendicolare all’orizzonte. E immagina che un cilindro di ghiaccio APQB abbia la stessa larghezza della cavità del vaso e lo stesso asse, e discenda continuamente con moto uniforme, e che le sue parti, appena toccano la superficie AB, si sciolgano e, mutate in acqua, scendano per la loro gravità nel vaso e, cadendo, formino la cateratta, ossia colonna d’acqua, ABNFEM, e passino attraverso il foro EF e lo riempiano esattamente. La velocità uniforme del ghiaccio che discende, come pure quella dell’acqua contigua nel cerchio AB, sia quella che l’acqua può acquistare cadendo e descrivendo nella sua caduta l’altezza IH; e IH e HG giacciano in linea retta, e per il punto I si conduca la retta KL parallela all’orizzonte, che incontri i lati del ghiaccio in K e L. E la velocità dell’acqua che esce attraverso il foro EF sarà quella che l’acqua può acquistare cadendo da I e descrivendo nella sua caduta l’altezza IG. Perciò, per i teoremi di Galileo, IG starà a IH nel rapporto duplicato della velocità dell’acqua che esce attraverso il foro rispetto alla velocità dell’acqua nel cerchio AB, cioè nel rapporto duplicato del cerchio AB al cerchio EF; infatti questi cerchi stanno inversamente come le velocità delle acque che li attraversano riempiendoli esattamente, nello stesso tempo e in quantità uguale. Qui si tratta della velocità dell’acqua verso l’orizzonte. E il moto parallelo all’orizzonte con cui le parti dell’acqua che cade si avvicinano l’una all’altra, poiché non nasce dalla gravità né cambia il moto perpendicolare all’orizzonte che nasce dalla gravità, qui non si considera. Supponiamo, è vero, che le parti dell’acqua siano un poco coerenti e, per la loro coesione, durante la caduta si avvicinino l’una all’altra con moti paralleli all’orizzonte, così da formare una sola cateratta e non dividersi in più cateratte; ma il moto parallelo all’orizzonte che nasce da quella coesione qui non lo consideriamo.

**[II.S7.32]** *Caso 1.* Immagina ora che tutta la cavità del vaso, attorno all’acqua che cade ABNFEM, sia piena di ghiaccio, così che l’acqua passi attraverso il ghiaccio come attraverso un imbuto. E se l’acqua sfiora appena il ghiaccio senza toccarlo, oppure, ciò che è lo stesso, se lo tocca ma, per la sua estrema levigatezza, scivola sul ghiaccio liberissimamente e senza alcuna resistenza, essa scenderà attraverso il foro EF con la stessa velocità di prima, e tutto il peso della colonna d’acqua ABNFEM sarà impiegato, come prima, a generarne il deflusso, e il fondo del vaso sosterrà il peso del ghiaccio che circonda la colonna.

**[II.S7.33]** Si sciolga ora il ghiaccio nel vaso; e l’efflusso dell’acqua, quanto alla velocità, resterà lo stesso di prima. Non sarà minore, perché il ghiaccio, sciolto in acqua, tenderà a discendere; non sarà maggiore, perché il ghiaccio, sciolto in acqua, non può discendere se non impedendo la discesa di altra acqua uguale alla propria discesa. La stessa forza deve generare la stessa velocità dell’acqua che esce.

**[II.S7.34]** Ma il foro nel fondo del vaso, a causa dei moti obliqui delle particelle dell’acqua che esce, deve essere un poco più grande di prima. Infatti le particelle dell’acqua ora non passano tutte perpendicolarmente attraverso il foro; ma, confluendo da ogni parte dalle pareti del vaso e convergendo nel foro, lo attraversano con moti obliqui; e, piegando il loro corso verso il basso, si uniscono nella vena dell’acqua che sgorga, la quale è un poco più sottile poco sotto il foro che nel foro stesso, poiché il suo diametro sta al diametro del foro come 5 sta a 6, ossia come 5½ sta a 6½, con ottima approssimazione, se ho misurato bene i diametri. Avevo preparato appunto una lamina piana sottilissima, forata nel mezzo, con un foro circolare di diametro pari a cinque ottavi di pollice. E perché la vena dell’acqua che sgorga non fosse accelerata nella caduta e, per l’accelerazione, resa più stretta, fissai questa lamina non al fondo ma alla parete del vaso, in modo che la vena uscisse secondo una linea parallela all’orizzonte. Poi, quando il vaso fu pieno d’acqua, aprii il foro perché l’acqua uscisse; e il diametro della vena, misurato con la massima accuratezza alla distanza di circa mezzo pollice dal foro, risultò di ventuno quarantesimi di pollice. Il diametro di questo foro circolare stava dunque al diametro della vena come 25 sta a 21, con ottima approssimazione. L’acqua dunque, passando attraverso il foro, converge da ogni parte e, dopo essere uscita dal vaso, si fa più sottile convergendo e, per l’assottigliamento, è accelerata finché non è giunta alla distanza di mezzo pollice dal foro; e a quella distanza diventa più sottile e più veloce che nel foro stesso nel rapporto di 25×25 a 21×21, ossia di 17 a 12 con ottima approssimazione, cioè circa nel rapporto subduplicato di due a uno. Dagli esperimenti risulta invece che la quantità d’acqua che in un tempo dato esce da un foro circolare praticato nel fondo di un vaso è quella che, con la velocità suddetta, dovrebbe uscire nello stesso tempo non attraverso quel foro, ma attraverso un foro circolare il cui diametro sta al diametro di quel foro come 21 sta a 25. Perciò quell’acqua che esce ha, nel foro stesso, una velocità verso il basso pari, con ottima approssimazione, a quella che un grave può acquistare cadendo e descrivendo nella sua caduta metà dell’altezza dell’acqua ferma nel vaso. Ma, dopo essere uscita dal vaso, è accelerata convergendo finché non è giunta a una distanza dal foro quasi uguale al diametro del foro, e ha acquistato una velocità maggiore circa nel rapporto subduplicato di due a uno; quella, appunto, che un grave può acquistare, con ottima approssimazione, cadendo e descrivendo nella sua caduta l’intera altezza dell’acqua ferma nel vaso.

**[II.S7.35]** In ciò che segue, dunque, il diametro della vena sia rappresentato da quel foro più piccolo che abbiamo chiamato EF. E s’immagini condotto, parallelo al piano del foro EF, un altro piano superiore VW, a una distanza circa uguale al diametro del foro, e forato da un foro più grande ST; attraverso il quale cada appunto una vena che riempia esattamente il foro inferiore EF, e il cui diametro stia perciò al diametro del foro inferiore circa come 25 sta a 21. Così infatti la vena passerà perpendicolarmente attraverso il foro inferiore; e la quantità d’acqua che esce, in proporzione alla grandezza di questo foro, sarà, con ottima approssimazione, quella che la soluzione del problema richiede. Lo spazio racchiuso fra i due piani e la vena che cade si può considerare come il fondo del vaso. Ma perché la soluzione del problema sia più semplice e più matematica, conviene prendere come fondo del vaso il solo piano inferiore, e immaginare che l’acqua che scendeva attraverso il ghiaccio come attraverso un imbuto, e usciva dal vaso attraverso il foro EF praticato nel piano inferiore, conservi continuamente il suo moto, e il ghiaccio la sua quiete. In ciò che segue, dunque, sia ST il diametro del foro circolare, descritto con centro Z, attraverso il quale la cateratta esce dal vaso quando tutta l’acqua nel vaso è fluida. E sia EF il diametro del foro che la cateratta, cadendo, attraversa riempiendolo esattamente, sia che l’acqua esca dal vaso attraverso quel foro superiore ST, sia che cada attraverso il mezzo del ghiaccio nel vaso come attraverso un imbuto. E il diametro del foro superiore ST stia al diametro di quello inferiore EF circa come 25 sta a 21, e la distanza perpendicolare fra i piani dei fori sia uguale al diametro del foro minore EF. E la velocità dell’acqua che esce dal vaso attraverso il foro ST sarà, nel foro stesso, verso il basso, quella che un corpo può acquistare cadendo da metà dell’altezza IZ; la velocità di entrambe le cateratte che cadono sarà invece, nel foro EF, quella che un corpo acquisterà cadendo dall’intera altezza IG.

**[II.S7.36]** *Caso 2.* Se il foro EF non è nel mezzo del fondo del vaso, ma il fondo è forato altrove, l’acqua uscirà con la stessa velocità di prima, purché la grandezza del foro sia la stessa. Infatti un grave impiega certamente più tempo a scendere alla stessa profondità lungo una linea obliqua che lungo una linea perpendicolare, ma scendendo acquista la stessa velocità in entrambi i casi, come ha dimostrato Galileo.

**[II.S7.37]** *Caso 3.* La velocità dell’acqua che esce attraverso un foro nella parete del vaso è la stessa. Infatti, se il foro è piccolo, così che l’intervallo fra le superfici AB e KL svanisca quanto ai sensi, e la vena d’acqua che sgorga orizzontalmente formi una figura parabolica, dal lato retto di questa parabola si ricaverà che la velocità dell’acqua che esce è quella che un corpo avrebbe potuto acquistare cadendo dall’altezza HG, ossia IG, dell’acqua ferma nel vaso. Fatto appunto l’esperimento, trovai che, se l’altezza dell’acqua ferma sopra il foro era di venti pollici e anche l’altezza del foro sopra un piano parallelo all’orizzonte era di venti pollici, la vena dell’acqua che zampillava cadeva su quel piano alla distanza di circa 37 pollici, presa a partire dalla perpendicolare abbassata dal foro su quel piano. Infatti senza resistenza la vena avrebbe dovuto cadere su quel piano alla distanza di 40 pollici, essendo il lato retto della vena parabolica di 80 pollici.

**[II.S7.38]** *Caso 4.* Anzi, l’acqua che esce, se è diretta verso l’alto, esce con la stessa velocità. La piccola vena dell’acqua che sgorga sale infatti, con moto perpendicolare, fino all’altezza GH, ossia GI, dell’acqua ferma nel vaso, se non in quanto la sua salita sia un poco impedita dalla resistenza dell’aria; e perciò esce con la velocità che avrebbe potuto acquistare cadendo da quell’altezza. Ogni particella dell’acqua ferma è premuta ugualmente da ogni parte (per la Prop. XIX del Libro II) e, cedendo alla pressione, è portata con uguale impeto in tutte le direzioni, sia che discenda attraverso il foro nel fondo del vaso, sia che esca orizzontalmente attraverso un foro nella sua parete, sia che entri in un canale e di lì salga attraverso un piccolo foro praticato nella parte superiore del canale. E che la velocità con cui l’acqua esce sia quella che abbiamo assegnato in questa proposizione, non solo si ricava dal ragionamento, ma è manifesto anche dagli esperimenti notissimi già descritti.

**[II.S7.39]** *Caso 5.* La velocità dell’acqua che esce è la stessa sia che la figura del foro sia circolare, sia quadrata o triangolare o qualsiasi altra uguale alla circolare. Infatti la velocità dell’acqua che esce non dipende dalla figura del foro, ma nasce dalla sua altezza sotto il piano KL.

**[II.S7.40]** *Caso 6.* Se la parte inferiore del vaso ABDC è immersa in acqua ferma, e l’altezza dell’acqua ferma sopra il fondo del vaso è GR, la velocità con cui l’acqua che è nel vaso uscirà attraverso il foro EF nell’acqua ferma sarà quella che l’acqua può acquistare cadendo e descrivendo nella sua caduta l’altezza IR. Infatti il peso di tutta l’acqua del vaso che sta sotto la superficie dell’acqua ferma sarà sostenuto in equilibrio dal peso dell’acqua ferma, e perciò [non] accelererà il moto dell’acqua che discende nel vaso. Anche questo caso risulterà dagli esperimenti, misurando cioè i tempi in cui l’acqua esce.

**[II.S7.41]** *Cor. 1.* Di qui, se l’altezza CA dell’acqua si prolunga fino a K, in modo che AK stia a CK nel rapporto duplicato dell’area del foro praticato in una parte qualsiasi del fondo all’area del cerchio AB, la velocità dell’acqua che esce sarà uguale alla velocità che l’acqua può acquistare cadendo e descrivendo nella sua caduta l’altezza KC.

**[II.S7.42]** *Cor. 2.* E la forza con cui può essere generato tutto il moto dell’acqua che sgorga è uguale al peso di una colonna cilindrica d’acqua la cui base è il foro EF e l’altezza è 2GI, ossia 2CK. Infatti l’acqua che sgorga, nel tempo in cui eguaglia questa colonna, può acquistare, cadendo per il suo peso dall’altezza GI, la velocità con cui sgorga.

**[II.S7.43]** *Cor. 3.* Il peso di tutta l’acqua nel vaso ABDC sta alla parte del peso che è impiegata nel deflusso dell’acqua come la somma dei cerchi AB ed EF sta al doppio del cerchio EF. Sia infatti IO media proporzionale fra IH e IG; l’acqua che esce attraverso il foro EF, nel tempo in cui una goccia, cadendo da I, potrebbe descrivere l’altezza IG, sarà uguale a un cilindro la cui base è il cerchio EF e l’altezza è 2IG, cioè a un cilindro la cui base è il cerchio AB e l’altezza è 2IO, perché il cerchio EF sta al cerchio AB nel rapporto subduplicato dell’altezza IH all’altezza IG, cioè nel rapporto semplice della media proporzionale IO all’altezza IG; e nel tempo in cui una goccia, cadendo da I, può descrivere l’altezza IH, l’acqua che esce sarà uguale a un cilindro la cui base è il cerchio AB e l’altezza è 2IH; e nel tempo in cui una goccia, cadendo da I per H fino a G, descrive la differenza delle altezze HG, l’acqua che esce, cioè tutta l’acqua nel solido ABNFEM, sarà uguale alla differenza dei cilindri, cioè a un cilindro la cui base è AB e l’altezza è 2HO. E perciò tutta l’acqua nel vaso ABDC sta a tutta l’acqua che cade nel solido ABNFEM come HG sta a 2HO, cioè come HO+OG sta a 2HO, ossia come IH+IO sta a 2IH. Ma il peso di tutta l’acqua nel solido ABNFEM è impiegato nel deflusso dell’acqua; e perciò il peso di tutta l’acqua nel vaso sta alla parte del peso che è impiegata nel deflusso dell’acqua come IH+IO sta a 2IH, e quindi come la somma dei cerchi EF e AB sta al doppio del cerchio EF.

**[II.S7.44]** *Cor. 4.* E di qui il peso di tutta l’acqua nel vaso ABDC sta all’altra parte del peso, quella che il fondo del vaso sostiene, come la somma dei cerchi AB ed EF sta alla differenza degli stessi cerchi.

**[II.S7.45]** *Cor. 5.* E la parte del peso che il fondo del vaso sostiene sta all’altra parte del peso, quella che è impiegata nel deflusso dell’acqua, come la differenza dei cerchi AB ed EF sta al doppio del cerchio minore EF, ossia come l’area del fondo sta al doppio del foro.

**[II.S7.46]** *Cor. 6.* La parte del peso dalla quale soltanto il fondo è premuto sta invece al peso di tutta l’acqua che grava perpendicolarmente sul fondo come il cerchio AB sta alla somma dei cerchi AB ed EF, ossia come il cerchio AB sta all’eccesso del doppio del cerchio AB sul fondo. Infatti la parte del peso dalla quale soltanto il fondo è premuto sta al peso di tutta l’acqua nel vaso come la differenza dei cerchi AB ed EF sta alla somma degli stessi cerchi, per il Cor. 4; e il peso di tutta l’acqua nel vaso sta al peso di tutta l’acqua che grava perpendicolarmente sul fondo come il cerchio AB sta alla differenza dei cerchi AB ed EF. Quindi, per uguaglianza perturbata, la parte del peso dalla quale soltanto il fondo è premuto sta al peso di tutta l’acqua che grava perpendicolarmente sul fondo come il cerchio AB sta alla somma dei cerchi AB ed EF, ossia all’eccesso del doppio del cerchio AB sul fondo.

**[II.S7.47]** *Cor. 7.* Se nel mezzo del foro EF si colloca un cerchietto PQ, descritto con centro G e parallelo all’orizzonte, il peso dell’acqua che quel cerchietto sostiene è maggiore del peso della terza parte di un cilindro d’acqua la cui base è quel cerchietto e l’altezza è GH. Sia infatti ABNFEM la cateratta, ossia colonna d’acqua che cade, avente asse GH come sopra, e s’immagini congelata tutta l’acqua nel vaso, sia attorno alla cateratta sia sopra il cerchietto, la cui fluidità non è richiesta per la discesa più pronta e più rapida dell’acqua. E sia PHQ la colonna d’acqua congelata sopra il cerchietto, con vertice H e altezza GH. E immagina che questa cateratta cada con tutto il suo peso, e non gravi su PHQ né la prema, ma le scorra accanto liberamente e senza attrito, se non forse proprio al vertice del ghiaccio, dove la cateratta, all’inizio stesso della caduta, cominci a essere cava. E come l’acqua congelata attorno alla cateratta, AMEC, BNFD, è convessa nella superficie interna AME, BNF verso la cateratta che cade, così anche questa colonna PHQ sarà convessa verso la cateratta, e perciò maggiore del cono la cui base è quel cerchietto PQ e l’altezza GH, cioè maggiore della terza parte del cilindro descritto con la stessa base e la stessa altezza. Ora, quel cerchietto sostiene il peso di questa colonna, cioè un peso maggiore del peso del cono, ossia della terza parte di quel cilindro.

**[II.S7.48]** *Cor. 8.* Il peso dell’acqua che un cerchietto PQ molto piccolo sostiene sembra minore del peso dei due terzi di un cilindro d’acqua la cui base è quel cerchietto e l’altezza è HG. Infatti, ferme restando le ipotesi già fatte, s’immagini descritta [la metà di] uno sferoide la cui base è quel cerchietto e il cui semiasse, ossia altezza, è HG. E questa figura sarà uguale ai due terzi di quel cilindro e comprenderà la colonna d’acqua congelata PHQ il cui peso quel cerchietto sostiene. Infatti, perché il moto dell’acqua sia il più diretto possibile, la superficie esterna di quella colonna incontrerà la base PQ sotto un angolo alquanto acuto, perché l’acqua, cadendo, è continuamente accelerata e, per l’accelerazione, si fa più sottile; e poiché quell’angolo è minore di un retto, questa colonna, nelle sue parti inferiori, giacerà dentro il mezzo sferoide. La stessa colonna sarà poi, in alto, acuta, ossia cuspidata, perché il moto orizzontale dell’acqua al vertice dello sferoide non sia infinitamente più veloce del suo moto verso l’orizzonte. E quanto più piccolo è il cerchietto PQ, tanto più acuto sarà il vertice della colonna; e, diminuito all’infinito il cerchietto, l’angolo PHQ diminuirà all’infinito, e perciò la colonna giacerà dentro il mezzo sferoide. Quella colonna è dunque minore del mezzo sferoide, ossia dei due terzi del cilindro la cui base è quel cerchietto e l’altezza GH. Ora, il cerchietto sostiene una forza dell’acqua uguale al peso di questa colonna, poiché il peso dell’acqua circostante è impiegato nel suo deflusso.

**[II.S7.49]** *Cor. 9.* Il peso dell’acqua che un cerchietto PQ molto piccolo sostiene è uguale, con ottima approssimazione, al peso di un cilindro d’acqua la cui base è quel cerchietto e l’altezza è ½GH. Questo peso è infatti la media aritmetica fra i pesi del cono e del mezzo sferoide suddetto. Ma se quel cerchietto non è molto piccolo, e si accresce finché non eguaglia il foro EF, esso sosterrà il peso di tutta l’acqua che gli sovrasta perpendicolarmente, cioè il peso di un cilindro d’acqua la cui base è quel cerchietto e l’altezza è GH.

**[II.S7.50]** *Cor. 10.* E (per quanto mi sembra) il peso che il cerchietto sostiene sta sempre al peso di un cilindro d’acqua la cui base è quel cerchietto e l’altezza è ½GH come EF² sta a EF²−½PQ², ossia come il cerchio EF sta all’eccesso di questo cerchio sulla metà del cerchietto PQ, con ottima approssimazione.

### Lemma IV (la resistenza del cilindro non dipende dalla lunghezza)

**[II.S7.51]** **La resistenza di un cilindro che avanza uniformemente nel senso della sua lunghezza non cambia se la sua lunghezza è aumentata o diminuita; e perciò è la stessa della resistenza di un cerchio descritto con lo stesso diametro e avanzante con la stessa velocità lungo una linea retta perpendicolare al suo piano.**

**[II.S7.52]** Infatti i lati del cilindro non si oppongono affatto al suo moto; e il cilindro, diminuita all’infinito la sua lunghezza, si muta in un cerchio.

### Proposizione XXXVII. Teorema XXIX (resistenza di un cilindro in un fluido continuo)

**[II.S7.53]** **La resistenza di un cilindro che avanza uniformemente nel senso della sua lunghezza in un fluido compresso, infinito e non elastico, resistenza che nasce dalla grandezza della sezione trasversale, sta alla forza con cui tutto il suo moto potrebbe essere tolto o generato mentre descrive il quadruplo della sua lunghezza, come la densità del mezzo sta alla densità del cilindro, con ottima approssimazione.**

**[II.S7.54]** Infatti, se il vaso ABDC tocca con il suo fondo CD la superficie dell’acqua ferma, e l’acqua esce da questo vaso nell’acqua ferma attraverso il canale cilindrico EFTS, perpendicolare all’orizzonte, e si colloca un cerchietto PQ parallelo all’orizzonte in un punto qualsiasi in mezzo al canale, e si prolunga CA fino a K in modo che AK stia a CK nel rapporto duplicato di quello che l’eccesso dell’orifizio EF del canale sul cerchietto PQ ha con il cerchio AB, è manifesto (per i Casi 5 e 6 e il Cor. 1 della Prop. XXXVI) che la velocità dell’acqua che passa attraverso lo spazio anulare fra il cerchietto e le pareti del vaso sarà quella che l’acqua può acquistare cadendo e descrivendo nella sua caduta l’altezza KC, ossia IG.

**[II.S7.55]** E (per il Cor. 10 della Prop. XXXVI), se la larghezza del vaso è infinita, così che il segmentino HI svanisca e le altezze IG, HG si eguaglino, la forza dell’acqua che scende sul cerchietto starà al peso di un cilindro la cui base è quel cerchietto e l’altezza è ½IG come EF² sta a EF²−½PQ², con ottima approssimazione. Infatti la forza dell’acqua che scende con moto uniforme per tutto il canale sarà la stessa sul cerchietto PQ, in qualunque parte del canale sia collocato.

**[II.S7.56]** Si chiudano ora gli orifizi EF, ST del canale, e il cerchietto salga nel fluido compresso da ogni parte e, con la sua salita, costringa l’acqua che sta sopra a discendere attraverso lo spazio anulare fra il cerchietto e le pareti del canale: la velocità del cerchietto che sale starà alla velocità dell’acqua che discende come la differenza dei cerchi EF e PQ sta al cerchio PQ, e la velocità del cerchietto che sale starà alla somma delle velocità, cioè alla velocità relativa dell’acqua che discende, con cui essa scorre accanto al cerchietto che sale, come la differenza dei cerchi EF e PQ sta al cerchio EF, ossia come EF²−PQ² sta a EF². Sia quella velocità relativa uguale alla velocità con cui, come si è mostrato sopra, l’acqua passa attraverso lo stesso spazio anulare mentre il cerchietto resta frattanto immobile, cioè alla velocità che l’acqua può acquistare cadendo e descrivendo nella sua caduta l’altezza IG: e la forza dell’acqua sul cerchietto che sale sarà la stessa di prima (per il Cor. V delle leggi), cioè la resistenza del cerchietto che sale starà al peso di un cilindro d’acqua la cui base è quel cerchietto e l’altezza è ½IG come EF² sta a EF²−½PQ², con ottima approssimazione. La velocità del cerchietto starà invece alla velocità che l’acqua acquista cadendo e descrivendo nella sua caduta l’altezza IG come EF²−PQ² sta a EF².

**[II.S7.57]** Si aumenti all’infinito l’ampiezza del canale: e quei rapporti fra EF²−PQ² ed EF², e fra EF² ed EF²−½PQ², si avvicineranno alla fine a rapporti di uguaglianza. E perciò la velocità del cerchietto sarà ora quella che l’acqua può acquistare cadendo e descrivendo nella sua caduta l’altezza IG, e la sua resistenza diventerà invece uguale al peso di un cilindro la cui base è quel cerchietto e la cui altezza è la metà dell’altezza IG, dalla quale il cilindro deve cadere per acquistare la velocità del cerchietto che sale; e con questa velocità il cilindro, nel tempo della caduta, descriverà il quadruplo della sua lunghezza. Ma la resistenza di un cilindro che avanza con questa velocità nel senso della sua lunghezza è la stessa della resistenza del cerchietto (per il Lemma IV), e perciò è uguale, con ottima approssimazione, alla forza con cui il suo moto può essere generato mentre descrive il quadruplo della sua lunghezza.

**[II.S7.58]** Se la lunghezza del cilindro si aumenta o si diminuisce, il suo moto, come pure il tempo in cui descrive il quadruplo della sua lunghezza, sarà aumentato o diminuito nello stesso rapporto; e perciò quella forza con cui il moto aumentato o diminuito potrebbe essere generato o tolto, in un tempo ugualmente aumentato o diminuito, non cambierà; e quindi è ancora uguale alla resistenza del cilindro, perché anche questa resta immutata, per il Lemma IV.

**[II.S7.59]** Se la densità del cilindro si aumenta o si diminuisce, il suo moto, come pure la forza con cui il moto può essere generato o tolto nello stesso tempo, sarà aumentato o diminuito nello stesso rapporto. La resistenza di un cilindro qualsiasi starà dunque alla forza con cui tutto il suo moto potrebbe essere generato o tolto mentre descrive il quadruplo della sua lunghezza come la densità del mezzo sta alla densità del cilindro, con ottima approssimazione. C.V.D.

**[II.S7.60]** Il fluido deve poi essere compresso perché sia continuo; e deve essere continuo e non elastico perché ogni pressione che nasce dalla sua compressione si propaghi in un istante e, agendo ugualmente su tutte le parti del corpo mosso, non cambi la resistenza. La pressione che nasce dal moto del corpo è appunto impiegata a generare il moto delle parti del fluido, e crea la resistenza. Ma la pressione che nasce dalla compressione del fluido, per quanto forte sia, se si propaga in un istante, non genera alcun moto nelle parti di un fluido continuo e non induce alcun cambiamento di moto; e perciò non accresce né diminuisce la resistenza. Certo, l’azione del fluido che nasce dalla sua compressione non può essere più forte sulle parti posteriori del corpo mosso che sulle sue parti anteriori, e perciò non può diminuire la resistenza descritta in questa proposizione; e non sarà più forte sulle parti anteriori che sulle posteriori, purché la sua propagazione sia infinitamente più veloce del moto del corpo premuto. E sarà infinitamente più veloce e si propagherà in un istante, purché il fluido sia continuo e non elastico.

**[II.S7.61]** *Cor. 1.* Le resistenze dei cilindri che avanzano uniformemente nel senso della loro lunghezza in mezzi continui infiniti sono nel rapporto composto dal rapporto duplicato delle velocità, dal rapporto duplicato dei diametri e dal rapporto della densità dei mezzi.

**[II.S7.62]** *Cor. 2.* Se l’ampiezza del canale non si aumenta all’infinito, ma il cilindro avanza nel senso della sua lunghezza in un mezzo in quiete racchiuso nel canale, e intanto il suo asse coincide con l’asse del canale, la sua resistenza starà alla forza con cui tutto il suo moto potrebbe essere generato o tolto nel tempo in cui descrive il quadruplo della sua lunghezza nel rapporto composto dal rapporto di EF² a EF²−½PQ² una volta, dal rapporto di EF² a EF²−PQ² due volte e dal rapporto della densità del mezzo alla densità del cilindro.

**[II.S7.63]** *Cor. 3.* Poste le stesse cose, e posto che una lunghezza L stia al quadruplo della lunghezza del cilindro nel rapporto composto dal rapporto di EF²−½PQ² a EF² una volta e dal rapporto di EF²−PQ² a EF² due volte, la resistenza del cilindro starà alla forza con cui tutto il suo moto potrebbe essere tolto o generato, mentre descrive la lunghezza L, come la densità del mezzo sta alla densità del cilindro.

#### Scolio (testa e coda del cilindro)

**[II.S7.64]** *Scolio.* In questa proposizione abbiamo ricercato la resistenza che nasce dalla sola grandezza della sezione trasversale del cilindro, trascurata la parte della resistenza che può nascere dall’obliquità dei moti. Infatti, come nel primo caso della Prop. XXXVI l’obliquità dei moti con cui le parti dell’acqua nel vaso convergevano da ogni parte nel foro EF impediva l’efflusso di quell’acqua attraverso il foro, così in questa proposizione l’obliquità dei moti con cui le parti dell’acqua, premute dall’estremità anteriore del cilindro, cedono alla pressione e divergono da ogni parte, ritarda il loro passaggio attraverso i luoghi attorno a quell’estremità che precede, verso le parti posteriori del cilindro, e fa sì che il fluido sia messo in moto a distanza maggiore, e accresce la resistenza, e ciò quasi nello stesso rapporto in cui diminuiva l’efflusso dell’acqua dal vaso, cioè circa nel rapporto duplicato di 25 a 21. E come, nel primo caso di quella proposizione, abbiamo fatto sì che le parti dell’acqua passassero perpendicolarmente e nella massima quantità attraverso il foro EF, supponendo che tutta l’acqua nel vaso che era stata congelata attorno alla cateratta, e il cui moto era obliquo e inutile, restasse senza moto, così in questa proposizione, perché l’obliquità dei moti sia tolta e le parti dell’acqua, cedendo con il moto più diretto e più breve, offrano al cilindro il passaggio più facile, e resti soltanto la resistenza che nasce dalla grandezza della sezione trasversale, la quale non si può diminuire se non diminuendo il diametro del cilindro, bisogna concepire che le parti del fluido i cui moti sono obliqui e inutili e creano resistenza siano in quiete fra loro a entrambe le estremità del cilindro, e siano coerenti e unite al cilindro. Sia ABCD un rettangolo, e siano AE e BE due archi parabolici descritti con asse AB e con un lato retto che stia allo spazio HG, che il cilindro deve descrivere cadendo mentre acquista la sua velocità, come HG sta a ½AB. Siano anche CF e DF altri due archi parabolici, descritti con asse CD e con un lato retto quadruplo del lato retto precedente; e per rivoluzione della figura attorno all’asse EF si generi un solido la cui parte media ABDC sia il cilindro di cui trattiamo, e le parti estreme ABE e CDF contengano le parti del fluido in quiete fra loro e consolidate in due corpi rigidi, che aderiscano al cilindro da una parte e dall’altra come testa e coda. E la resistenza del solido EACFDB, che avanza nel senso della lunghezza del suo asse FE verso la parte di E, sarà, con ottima approssimazione, quella che abbiamo descritto in questa proposizione, cioè quella che ha, rispetto alla forza con cui tutto il moto del cilindro potrebbe essere tolto o generato mentre, con quel moto continuato uniformemente, si descrive la lunghezza 4AC, il rapporto che la densità del fluido ha con la densità del cilindro, con ottima approssimazione. E la resistenza non può essere minore di questa forza oltre il rapporto di 2 a 3 [cioè non può scendere sotto i due terzi di essa], per il Cor. 7 della Prop. XXXVI.

---

## Apparato

### A.0 Estensioni del glossario

I termini seguenti non comparivano nel glossario comune né in quello del Libro II. Ognuno è reso in modo costante in tutto il fascicolo.

| Latino | Italiano | Motivazione |
|---|---|---|
| *systema corporum* | «sistema di corpi» | Prop. XXXII; Motte «systems of bodies». |
| *similiter moveri temporibus proportionalibus* | «muoversi in modo simile in tempi proporzionali» | Formula fissa delle Propp. XXXII–XXXIII; Newton stesso la definisce in II.S7.02. |
| *similiter situs / positus* | «situato in modo simile» | Calco; evita «omologo», termine moderno. |
| *agitare se mutuo* | «agitarsi a vicenda» | Verbo di Newton per l’azione reciproca delle particelle; non «interagire». |
| *fugare / fugere se mutuo* | «respingersi a vicenda» | Opposto di *attrahere*; Motte «repel», «recede», «fly from». |
| *occursus* | «incontro» | Come *concursus* nel glossario comune; *ictus* («urto») non compare. |
| *resistitur*, *resistuntur* (impersonale o passivo) | «subisce / incontra resistenza» | Il latino usa il passivo di *resisto*; l’italiano non lo consente. |
| *duplo minor* | «la metà» | Lett. «minore del doppio», cioè metà; Motte «but half so great». Usato nelle Propp. XXXIV–XXXV e nello Scolio della XXXV. |
| *æquivelox* | «di uguale velocità» | Prop. XXXIII, Cor. 2, 4, 5. |
| *velocissime*, *celerrime moveri* | «muoversi velocissimamente», «molto velocemente» | Due avverbi distinti nel latino, tenuti distinti. |
| *quam proxime*, *quamproxime* | «con ottima approssimazione» | Come nel Fascicolo 5. *Circiter* «circa», *fere* «quasi», *prope* «quasi». |
| *plaga* (*secundum plagam axis*) | «verso» («nel verso dell’asse») | Nel Fascicolo 3 *plaga* è «parte»; qui però Newton scrive *secundum plagam determinationis suæ* (Prop. XXXIV), e «parte della direzione» o «direzione della direzione» sarebbero inintelligibili. **Da armonizzare**: propongo «verso» per *plaga* quando indica l’orientamento di un moto o di un’azione, «parte» quando indica una regione (*in partes versus E* «verso la parte di E»). |
| *efficacia* | «efficacia» | Prop. XXXIV: la componente utile della forza; Motte «efficacy». |
| *parabolois* | «paraboloide» | Prop. XXXIV; il solido di rivoluzione della parabola. |
| *sphærois*, *hemisphærois*, *dimidium sphæroidis* | «sferoide», «mezzo sferoide» | Prop. XXXVI, Cor. 8–9. |
| *frustum coni* | «tronco di cono» | Scolio della Prop. XXXIV; Motte «frustum of a cone». |
| *convolutio*, *revolutio* | «rivoluzione» | Due sostantivi latini per lo stesso atto geometrico (solido generato ruotando una figura attorno a un asse). |
| *glacies* | «ghiaccio» | Prop. XXXVI. |
| *infundibulum* | «imbuto» | Prop. XXXVI, Caso 1. |
| *vena* (*aquæ exilientis*) | «vena» | Termine idraulico italiano già classico (la «vena contratta»); Motte «stream». Nota N10. |
| *exilire*, *prosilire* | «sgorgare», «zampillare» | Due verbi distinti. *Effluere* «uscire», *defluere* «scendere», *egredi* «uscire». |
| *effluxus*, *defluxus* | «efflusso», «deflusso» | *In defluxum aquæ impendi* «essere impiegato nel deflusso dell’acqua». |
| *aqua stagnans* | «acqua ferma» | Acqua in quiete nel vaso o nel recipiente esterno; «stagnante» avrebbe in italiano una connotazione impropria. |
| *orificium* | «bocca» (del vaso, Prop. XXXVI), «orifizio» (del canale, Prop. XXXVII) | Il primo è l’apertura superiore del vaso, il secondo l’estremità di un tubo. |
| *lamina* | «lamina» | Prop. XXXVI: la piastrina forata dell’esperimento. |
| *circellus* | «cerchietto» | Diminutivo conservato (Prop. XXXVI, Cor. 7–10; Prop. XXXVII); Motte «little circle». |
| *spatium annulare* | «spazio anulare» | Prop. XXXVII. |
| *lineola* | «segmentino» | Prop. XXXVII (*lineola HI*). |
| *media proportionalis* | «media proporzionale» | Prop. XXXVI, Cor. 3. |
| *ex æquo perturbate* | «per uguaglianza perturbata» | Termine della teoria delle proporzioni (Euclide, *Elementi* V, def. 18 e prop. 23); Motte lo lascia in latino. |
| *medium continuum / non continuum* | «mezzo continuo / non continuo» | Scolio della Prop. XXXV; Prop. XXXVII. |
| *sectio transversa* | «sezione trasversale» | Prop. XXXVII. |
| *pressio* | «pressione» | Prop. XXXVI, Caso 4; Prop. XXXVII. |
| *caput & cauda* | «testa e coda» | Scolio della Prop. XXXVII. |
| *semel*, *bis* | «una volta», «due volte» | Come nel Fascicolo 5 (Prop. XXXVII, Cor. 2–3). |
| *grave* (sostantivo) | «grave» | Il corpo pesante della tradizione galileiana. |

Termini del glossario del Libro II **non presenti** in questa parte: *vis insita*, *tempus periodicum*, *oscillatio*, *pendulum*, *gravitas specifica*, le unità diverse dal *digitus*. *Medium similare* non compare. *Cataracta* (prima occorrenza in II.S7.31) è resa «cateratta», come stabilito, con nota N9. *Argentum vivum* compare una volta (II.S7.29): «il mercurio (argento vivo)».

### A.1 Proposizione XXXII

**Latino:** *Si corporum systemata duo similia ex æquali particularum numero constent, & particulæ correspondentes similes sint & proportionales, singulæ in uno systemate singulis in altero, & similiter sitæ inter se, ac datam habeant rationem densitatis ad invicem, & inter se temporibus proportionalibus similiter moveri incipiant (eæ inter se quæ in uno sunt systemate & eæ inter se quæ sunt in altero) & si non tangant se mutuo quæ in eodem sunt systemate, nisi in momentis reflexionum, neque attrahant, vel fugent se mutuo, nisi viribus acceleratricibus quæ sint ut particularum correspondentium diametri inverse & quadrata velocitatum directe: dico quod systematum particulæ illæ pergent inter se temporibus proportionalibus similiter moveri.*

**Inglese:** “Suppose two similar systems of bodies consisting of an equal number of particles, and let the correspondent particles be similar and proportional, each in one system to each in the other, and have a like situation among themselves, and the same given ratio of density to each other; and let them begin to move among themselves in proportional times, and with like motions (that is, those in one system among one another, and those in the other among one another). And if the particles that are in the same system do not touch one another, except in the moments of reflexion; nor attract, nor repel each other, except with accelerative forces that are as the diameters of the correspondent particles inversely, and the squares of the velocities directly; I say, that the particles of those systems will continue to move among themselves with like motions and in proportional times.”

**Scelte.**

- *Corpora … similiter moveri dico, quorum situs …* è una definizione esplicita: «Dico che corpi … si muovono in modo simile … quando le loro posizioni …». Motte «are said to be moved», con il passivo impersonale.
- *viribus acceleratricibus quæ sint ut particularum correspondentium diametri inverse & quadrata velocitatum directe*: la condizione dinamica della similitudine (nota N1).
- *perinde ac si centra inter particulas similiter sita respicerent* → «come se guardassero a centri situati in modo simile»: *respicere* è il verbo con cui Newton indica la direzione di una forza verso un centro. Motte «respected».
- *per legum corollarium secundum* → «per il secondo corollario delle leggi» (Fascicolo 3, Cor. II, composizione delle forze).
- La parentesi aperta prima di *per corol. 1. & 8. prop. IV. lib. I.* non è chiusa nella trascrizione; la chiusura va dopo *lib. I.* (Motte la chiude lì).
- *compositaeæ* è un artefatto della trascrizione (doppia desinenza) per *compositæ*.

**Corollari (II.S7.03–II.S7.04).** Nessuna divergenza di sostanza. Cor. 1: *Est enim eadem ratio …* → «Il rapporto è infatti lo stesso …»; Motte «for the case … is the very same» (*ratio* inteso come «caso», lettura possibile ma meno letterale).

### A.2 Proposizione XXXIII

**Latino:** *Iisdem positis, dico quod systematum partes majores resistituntur in ratione composita ex duplicata ratione velocitatum suarum & duplicata ratione diametrorum & ratione densitatis partium systematum.*

**Inglese:** “The same things being supposed, I say, that the greater parts of the systems are resisted in a ratio compounded of the duplicate ratio of their velocities, and the duplicate ratio of their diameters, and the simple ratio of the density of the parts of the systems.”

**Scelte.**

- *resistituntur* (enunciato): forma anomala per *resistuntur* (refuso probabile, A.9).
- Motte aggiunge «**simple** ratio of the density» nell’enunciato: il latino ha solo *ratione densitatis*.
- La dimostrazione ha due C.V.D., uno per ciascun genere di resistenza: conservati.
- *conjunctim* → «considerati congiuntamente» (accordato con il soggetto plurale).
- Cor. 2: *augerenter* (refuso per *augerentur*) e due volte *resistantiæ* (per *resistentiæ*). *Sunto … media tria A, B, C*: congiuntivo esortativo reso «Siano dunque tre mezzi». *Pro lubitu* → «a piacere».
- Cor. 2: *in subduplicata ratione virium T ad vires V* → «nel rapporto subduplicato delle forze T alle forze V»; Motte singolarizza («the force T to the force V»).
- Cor. 5, ultima frase: *Ex medii subtilitate resistentia … non multum diminuitur*. Motte la introduce con «For», rendendo esplicativa un’affermazione che nel latino è una conclusione autonoma.
- Cor. 6: *ad instar lanæ vel ramorum arborum* → «a somiglianza della lana o dei rami degli alberi».

### A.3 Proposizione XXXIV e Scolio

**Latino:** *Si globus & cylindrus æqualibus diametris descripti, in medio raro ex particulis æqualibus & ab æquales ab invicem distantias libere dispositis constante, secundum plagam axis cylindri, æquali cum velocitate moveantur: erit resistentia globi duplo minor quam resistentia cylindri.*

**Inglese:** “If in a rare medium, consisting of equal particles freely disposed at equal distances from each other, a globe and a cylinder described on equal diameters move with equal velocities in the direction of the axis of the cylinder, the resistance of the globe will be but half so great as that of the cylinder.”

**Scelte.**

- *ab æquales ab invicem distantias* (enunciato): refuso per *ad æquales* (cfr. l’enunciato della Prop. XXXV, *ad æquales ab invicem distantias*).
- *five medii particulæ* → *sive* (s lunga letta f; refuso della trascrizione).
- *quo impetu urgebitur* → «con quale impeto sarà sollecitato»; Motte «with what force».
- *BE quad.CB* letto BE²/CB (frazione appiattita); confermato dal senso (bH : bE = BE² : BC² con bE = BC).
- **Ricostruzione della figura.** Perché *LD ad LB* sia uguale a *BE ad BC*, BE deve essere la distanza di B dalla retta KC misurata parallelamente all’asse: dunque KC è un raggio perpendicolare all’asse ACI, e BE è parallela all’asse. Ne segue che bH = BE²/CB, misurata dalla base NAO, descrive un paraboloide di vertice C (nota N5, verifica numerica).
- *Rursus efficacia … secundum plagam determinationis suæ*: la forza normale agisce lungo BC (la sua *determinatio*, «direzione»), ma il moto del globo si valuta lungo AC: seconda proiezione BE/BC.

**Scolio (II.S7.15–II.S7.17).**

- *Ut si … construendum sit frustum coni … : biseca … & produc …*: imperativi conservati («dividi a metà», «prolunga»).
- *Unde obiter* → «Di qui, per inciso».
- *ea lege ut* → «con la condizione che».
- *Quam quidem propositionem in construendis navibus non inutilem futuram esse censeo* → «E questa proposizione, ritengo, non sarà inutile nella costruzione delle navi». Motte «may be of use»: attenua la litote.
- Ultimo capoverso: *Quod si* → «Che se»; Motte omette *Quod*. *fuerit MN ad GR ut GR cub. ad 4BR×GBq* → «MN sta a GR come GR³ sta a 4BR×GB²». Newton non dà dimostrazione (nota N8).

### A.4 Proposizione XXXV e Scolio

**Latino:** *Si medium rarum ex particulis quam minimis quiescentibus æqualibus & ad æquales ab invicem distantias libere dispositis constet: invenire resistentiam globi in hoc medio uniformiter progredientis.*

**Inglese:** “If a rare medium consist of very small quiescent particles of equal magnitudes, and freely disposed at equal distances from one another: to find the resistance of a globe moving uniformly forward in this medium.”

**Scelte.**

- *eadem diametro & altitudine descriptus*: il cilindro ha diametro e altezza uguali al diametro del globo (dunque volume 3/2 del globo: *globus sit ad cylindrum ut duo ad tria*).
- *vi reflexionis quam maxima resiliant* → «rimbalzino con la massima forza di riflessione possibile».
- *per propositionem novissimam* → «per la proposizione precedente» (la XXXIV); Motte «by the last Proposition».
- *quo tempore … describit* → «nel tempo in cui … descrive».
- Caso 2: Motte omette *quam prius* («the globe also meets with a resistance but half so great»).
- Caso 3: *in eadem ratione mediocri inter …* → «nello stesso rapporto intermedio, fra …».
- Cor. 2–5: *velociatatis* (due volte), *ratione densitas medii* (Cor. 5, per *densitatis*): refusi. *Cæteris paribus* → «a parità delle altre condizioni».
- Cor. 6: *exponi*, *exponetur* → «rappresentare», «sarà rappresentato» (cfr. *exponens* nel Fascicolo 5). *hyperpoblæ* e *exponentur* (per *exponetur*) refusi.
- Cor. 7: *tMT+t*, *TMT+t*, *T+tT*, *tT* letti tM/(T+t), TM/(T+t), (T+t)/T, t/T (frazioni appiattite); *resisitentiam* refuso. Il *logarithmus* è il logaritmo decimale (tabulare): moltiplicato per 2,302585092994 dà il logaritmo naturale (nota N6). Motte stampa tutte e quattro le frazioni come SVG (733, 734, 735, 455), conformi al latino (A.10).

**Scolio (II.S7.29).** *summe elastica* → «sommamente elastici»; *oleum calidum* → «olio caldo»; *argentum vivum* → «il mercurio (argento vivo)». *Partes octo tertias diametri* → «otto terzi del suo diametro». Motte «diminished one half», «one other half»: corretto nel senso.

### A.5 Proposizione XXXVI

**Latino:** *Aquæ de vase cylindrico per foramen in fundo factum effluentis definire motum.*

**Inglese:** “To define the motion of water running out of a cylindrical vessel through a hole made at the bottom.”

**Scelte.**

- *definire motum* → «determinare il moto».
- *AB ejus orificium superius* → «AB la sua bocca superiore»; Motte omette *superius*.
- *finge* (imperativo) → «immagina»; *Concipe* → «Immagina» (Caso 1).
- *ese* (per *esse*), *in quam conversas* (per *in aquam conversas*), *qui glacies in quam resoluta* (per *quia glacies in aquam resoluta*), *&æquali* (spaziatura): refusi; la traduzione segue il senso.
- *cataractam vel columnam aquæ* → «la cateratta, ossia colonna d’acqua» (nota N9).
- *De velocitate aquæ horizontem versus hic agitur* → «Qui si tratta della velocità dell’acqua verso l’orizzonte», cioè verso il basso. Motte «tends to the plane of the horizon».
- *tantum non tangat* → «sfiora appena … senza toccarlo» (*tantum non* = «quasi»); Motte «pass very near to the ice only, without touching it».
- *Eadem vis eandem … velocitatem generare debet*: Motte aggiunge «always».
- *512 ad 612* letto 5½ : 6½ (frazioni appiattite; Motte [SVG 736], [SVG 727]). *partium quinque octavarum digiti* → «cinque ottavi di pollice»; *partium viginti & unius quadragesimarum digiti* → «ventuno quarantesimi di pollice». Motte stampa entrambe le frazioni come SVG (737, 738). Verifica aritmetica in N10.
- *diammeter* refuso per *diameter*.
- Caso 3: *ab aquæ … altitudine HG vel IG* → «dall’altezza HG, ossia IG»; Motte inverte l’ordine («IG or HG»).
- Caso 4: *si sursum seratur* → *feratur* (s lunga; refuso probabile). *æquali impetu in omnes partes fertur* → «è portata con uguale impeto in tutte le direzioni»; Motte «tends always with an equal force», con *always* aggiunto e *in omnes partes* omesso. *per prop. XIX. lib. 2.* → «per la Prop. XIX del Libro II» (A.8).
- Caso 5: *sive figura foraminis fit circularis* → *sit* (refuso probabile, f per s lunga).
- **Caso 6: *ideoque motum aquæ descendentis in vase accelerabit*.** Così com’è, la frase dice il contrario di quanto richiede l’argomento: il peso dell’acqua sotto il livello esterno è equilibrato e quindi **non** accelera il deflusso (la velocità corrisponde alla sola altezza IR). Motte ha «does **not at all** accelerate». Nella trascrizione manca quasi certamente una negazione (*nil* o *non*): la traduzione la integra tra parentesi quadre, «[non] accelererà». **Da verificare sulla stampa** (punto ECCO n. 1).
- Cor. 2: *quo tempore hanc columnam æquat* → «nel tempo in cui eguaglia questa colonna», cioè nel tempo in cui il volume uscito eguaglia la colonna.
- Cor. 3: *edrediens* (per *egrediens*), *dplum* (per *duplum*): refusi. Motte spezza l’unico periodo in tre frasi.
- Cor. 6: *ex æquo perturbate* → «per uguaglianza perturbata» (A.0); Motte «ex æquo perturbatè».
- Cor. 7: *quo cataracta … incipiat esse cava* → «dove la cateratta … cominci a essere cava»; Motte «may tend to a concave figure».
- Cor. 8: *describi intelligatur sphæroidis cujus basis …*: il genitivo resta senza reggente; Motte «the half of a spheroid». Manca probabilmente *dimidium* (o la forma era *hemisphæroides*): integrato «[la metà di]». *Est hæc figura æqualis erit*: refuso probabile per *Et hæc figura*.
- Cor. 8: ***Nam ut motus aquæ sit maxime directus***: *ut* + congiuntivo è inteso come **finale** («perché il moto dell’acqua sia il più diretto possibile»), in parallelo con la frase seguente (*ne horizontalis motus … sit infinite velocior*), anch’essa finale. Motte lo legge come concessivo («For **though** the motion of the water tends directly downwards»). Le due letture non cambiano la conclusione.
- Cor. 9: *12GH* letto ½GH (Motte [SVG 739]); *aquè* per *aquæ*.
- Cor. 10: *(quantum sentio)* → «(per quanto mi sembra)»; Motte «(as far as I can judge)». *EFq ad EFq−12PQq* letto EF² : EF²−½PQ².

### A.6 Lemma IV

**Latino:** *Cylindri, qui secundum longitudinem suam uniformiter progreditur, resistentia ex aucta vel diminuta ejus longitudine non mutatur; ideoque eadem est cum resistentia circuli eadem diametro descripti & eadem velocitate secundum lineam rectam plano ipsius perpendicularem progredientis.*

**Inglese:** “If a cylinder move uniformly forward in the direction of its length, the resistance made thereto is not at all changed by augmenting or diminishing that length; and is therefore the same with the resistance of a circle, described with the same diameter, and moving forward with the same velocity in the direction of a right line perpendicular to its plane.”

**Scelte.** *latera cylindri motui ejus minime opponuntur* → «i lati del cilindro non si oppongono affatto al suo moto» (*minime* nel senso di negazione forte; Motte «are not at all opposed»). *in circulum vertitur* → «si muta in un cerchio».

### A.7 Proposizione XXXVII e Scolio

**Latino:** *Cylindri, qui in fluido compresso infinito & non elastico secundum longitudinem suam uniformiter progreditur, resistentia, quæ oritur a magnitudine sectionis transversæ, est ad vim qua totus ejus motus, interea dum quadruplum longitudinis suæ describit, vel tolli possit vel generari, ut densitas medii ad densitatem cylindri quamproxime.*

**Inglese:** “If a cylinder move uniformly forward in a compressed, infinite, and non-elastic fluid, in the direction of its length, the resistance arising from the magnitude of its transverse section is to the force by which its whole motion may be destroyed or generated, in the time that it moves four times its length, as the density of the medium to the density of the cylinder, nearly.”

**Scelte.**

- *superificiem* refuso; *Efq* per *EFq*; *Fluidam* per *Fluidum* (refusi).
- *in duplicata ratione quam habet excessus orificii canalis EF supra circellum PQ ad circulum AB* → «nel rapporto duplicato di quello che l’eccesso dell’orifizio EF del canale sul cerchietto PQ ha con il cerchio AB»: l’area utile del foro è l’anello EF − PQ (Cor. 1 della Prop. XXXVI applicato all’anello).
- *inter circellum & latera vasis* (primo capoverso): il latino dice «vaso», anche se lo spazio anulare è fra il cerchietto e le pareti del **canale** (così nel terzo capoverso). Tradotto alla lettera; Motte fa lo stesso.
- Terzo capoverso: *ad circulum EF*; Motte «to the circle [SVG 743]», e l’immagine 743 è EF: conforme (A.10).
- *a qua cylindrus cadere debet*: il «cilindro» è qui il cilindro d’acqua di altezza ½IG, che acquista la velocità del cerchietto cadendo dall’altezza IG (il relativo *a qua* si riferisce ad *altitudinis IG*); nel tempo della caduta, con quella velocità, percorre 2IG, cioè il quadruplo della sua lunghezza ½IG (nota N13).
- Penultimo capoverso: Motte aggiunge la causale «because the time is increased or diminished in the same proportion», che scioglie l’ablativo assoluto *tempore pariter aucto vel diminuto*.
- *Fluidum autem comprimi debet ut sit continuum*: il capoverso giustifica le tre ipotesi dell’enunciato (compresso, continuo, non elastico).
- Cor. 2–3: *semel*, *bis* → «una volta», «due volte».
- **Scolio:** *propostione*, *ciciter*, *fine motu* (per *sine motu*), *ad vim totus cylindri motus* (manca probabilmente *qua*): refusi. *cedunt pressione*: probabile *pressioni* (dativo, come *pressioni cedendo* nel Caso 4 della Prop. XXXVI). *12AB* letto ½AB (Motte [SVG 128]).
- Ultima frase: *Et hac vi resistentia minor esse non potest quam in ratione 2 ad 3* → «E la resistenza non può essere minore di questa forza oltre il rapporto di 2 a 3 [cioè non può scendere sotto i due terzi di essa]». La glossa tra parentesi quadre esplicita la costruzione latina; Motte «must be to this force in the ratio of 2 to 3, at the least». Nota N14.

### A.8 Rimandi

| Luogo | Latino | Rimando | Esito |
|---|---|---|---|
| II.S7.02 | *per motus leg. I.* | Legge I (Fascicolo 3) | regge: moto rettilineo uniforme in assenza di forze |
| II.S7.02 | *per legum corollarium secundum* | Cor. II delle leggi (Fascicolo 3) | regge: composizione delle forze |
| II.S7.02 | *per corol. 1. & 8. prop. IV. lib. I.* | Libro I, Prop. IV, Cor. 1 e Cor. 8 (Fascicolo 5, S2.24 e S2.31) | **regge**: il Cor. 1 dà le forze come velocità²/raggio, il Cor. 8 estende i risultati a parti simili di figure simili con centri situati in modo simile, che è proprio l’uso di Newton |
| II.S7.11 | *per motus legem tertiam* | Legge III (Fascicolo 3) | regge |
| II.S7.14 | *per legum corol. 5.* | Cor. V delle leggi (Fascicolo 3) | regge: equivalenza fra corpo in moto in un mezzo in quiete e mezzo in moto su un corpo in quiete |
| II.S7.19 | *per propositionem novissimam* | Prop. XXXIV | regge |
| II.S7.27 | *per corol. 1. & 3. prop. V. lib. II.* | Libro II, Prop. V, Cor. 1 e 3 (trascrizione latina della Sez. II) | **regge**: il Cor. 1 rappresenta velocità finale con l’ordinata e spazio con l’area iperbolica; il Cor. 3 dà la resistenza iniziale con la tangente (AT = AC); la resistenza finale BH segue dalla stessa costruzione in F |
| II.S7.31, II.S7.36 | *per theoremata Galilæi*; *ut Galilæus demonstravit* | teoremi di Galileo sulla caduta dei gravi | non verificabile sulle fonti allegate; l’uso (v² ∝ altezza; stessa velocità per piano inclinato e verticale) è quello dello Scolio alle Leggi (Fascicolo 3) |
| II.S7.38 | *per prop. XIX. lib. 2.* | Libro II, Prop. XIX (trascrizione latina della Sez. V) | **regge**: le parti di un fluido omogeneo in quiete e compresso sono premute ugualmente da ogni parte |
| II.S7.46 | *per cor. 4* | Prop. XXXVI, Cor. 4 | regge |
| II.S7.54 | *per cas. 5. cas. 6. & cor. 1. prop. XXXVI.* | Prop. XXXVI, Casi 5, 6, Cor. 1 | regge |
| II.S7.55 | *per corol. x. prop. XXXVI.* | Prop. XXXVI, Cor. 10 | regge (ma il Cor. 10 è dato da Newton come congettura, *quantum sentio*: nota N12) |
| II.S7.56 | *per legum corol. V.* | Cor. V delle leggi | regge |
| II.S7.57, II.S7.58 | *per lemma IV.* | Lemma IV | regge |
| II.S7.64 | *per corol. 7. prop. XXXVI.* | Prop. XXXVI, Cor. 7 | regge: un terzo contro un mezzo del cilindro, cioè 2 : 3 (nota N14) |

Rimandi al Libro I: **uno** (Prop. IV, Cor. 1 e 8), verificato. Nessun rimando che non torni.

### A.9 Refusi e anomalie della trascrizione

| Luogo | Trascrizione | Lettura | Tipo |
|---|---|---|---|
| II.S7.02 | *agitan ‹319› tibus … compositaeæ* | *compositæ* | doppia desinenza (artefatto) |
| II.S7.02 | *(per corol. 1. & 8. prop. IV. lib. I.* | parentesi da chiudere dopo *lib. I.* | punteggiatura |
| II.S7.05 | *resistituntur* | *resistuntur* | refuso probabile |
| II.S7.06 | *resistentiaeæ* | *resistentiæ* | doppia desinenza (artefatto) |
| II.S7.08 | *augerenter*; *resistantiæ* (×2) | *augerentur*; *resistentiæ* | refusi probabili |
| II.S7.13 | *ab æquales ab invicem distantias* | *ad æquales* | refuso probabile |
| II.S7.14 | *five medii particulæ* | *sive* | s lunga |
| II.S7.14 | *BE quad.CB* | BE²/CB | frazione appiattita |
| II.S7.17 | *GR cub. ad 4BR×GBq* | GR³ : 4BR×GB² | abbreviazioni |
| II.S7.23, II.S7.26 | *velociatatis* | *velocitatis* | refuso probabile |
| II.S7.26 | *ratione densitas medii* | *densitatis* | refuso probabile |
| II.S7.27 | *hyperpoblæ*; *exponentur* | *hyperbolæ*; *exponetur* | refusi probabili |
| II.S7.28 | *tMT+t*, *TMT+t*, *T+tT*, *tT*; *resisitentiam* | tM/(T+t), TM/(T+t), (T+t)/T, t/T; *resistentiam* | frazioni appiattite; refuso |
| II.S7.31 | *ese*; *in quam conversas*; *&æquali* | *esse*; *in aquam conversas*; *& æquali* | refusi probabili; spaziatura |
| II.S7.33 | *qui glacies in quam resoluta* | *quia glacies in aquam resoluta* | refusi probabili |
| II.S7.34 | *512 ad 612*; *diammeter* | 5½ : 6½; *diameter* | frazioni appiattite; refuso |
| II.S7.38 | *si sursum seratur* | *feratur* | s lunga (inversa) |
| II.S7.39 | *fit circularis* | *sit* | s lunga |
| II.S7.40 | *motum … accelerabit* | *[non / nil] accelerabit* | **omissione probabile di una negazione** |
| II.S7.43 | *edrediens*; *dplum* | *egrediens*; *duplum* | refusi probabili |
| II.S7.48 | *describi intelligatur sphæroidis* | *[dimidium] sphæroidis* | omissione probabile |
| II.S7.48 | *Est hæc figura æqualis erit* | *Et hæc figura* | refuso probabile |
| II.S7.48 | *spheroidis* (penultima frase) | *sphæroidis* | grafia |
| II.S7.49 | *12GH*; *aquè* | ½GH; *aquæ* | frazione appiattita; refuso |
| II.S7.50, II.S7.55–57, II.S7.62–63 | *12GH*, *12IG*, *EFq−12PQq* | ½GH, ½IG, EF²−½PQ² | frazioni appiattite |
| II.S7.54 | *superificiem* | *superficiem* | refuso probabile |
| II.S7.57 | *Efq* | *EFq* | maiuscola |
| II.S7.60 | *Fluidam* | *Fluidum* | refuso probabile |
| II.S7.64 | *propostione*; *ciciter*; *fine motu*; *cedunt pressione*; *ad vim totus*; *12AB* | *propositione*; *circiter*; *sine motu*; *pressioni*; *ad vim qua totus*; ½AB | refusi, s lunga, omissione probabile, frazione appiattita |

La traduzione segue il senso; la Parte B riporta il latino esatto della trascrizione.

#### Punti da controllare sulla stampa ECCO

| n. | Pagina 1726 | Trascrizione | Lettura attesa | Motivo |
|---|---|---|---|---|
| 1 | p. 332 | *ideoque motum aquæ descendentis in vase accelerabit* | *… nil (non) accelerabit* | l’argomento richiede la negazione; Motte «does not at all accelerate» |
| 2 | p. 334 | *describi intelligatur sphæroidis* | *dimidium sphæroidis* o *hemisphærois* | genitivo senza reggente; Motte «the half of a spheroid» |
| 3 | p. 334 | *Est hæc figura æqualis erit* | *Et hæc figura* | due verbi nella stessa proposizione |
| 4 | p. 340 | *ad vim totus cylindri motus* | *ad vim qua totus* | relativo mancante |
| 5 | p. 331 | *si sursum seratur* | *feratur* | s lunga / f |
| 6 | p. 332 | *sive figura foraminis fit circularis* | *sit* | s lunga / f |
| 7 | p. 340 | *maneret fine motu* | *sine motu* | s lunga / f |
| 8 | p. 322 | *five medii particulæ* | *sive* | s lunga / f |
| 9 | p. 322 | *ab æquales ab invicem distantias* | *ad æquales* | cfr. enunciato della Prop. XXXV |
| 10 | p. 328–329 | *in quam conversas*; *qui glacies in quam resoluta* | *in aquam*; *quia … in aquam* | lettere cadute |
| 11 | p. 329 | *512 ad 612* | 5½ ad 6½ | forma tipografica della frazione |
| 12 | p. 339 | *cedunt pressione* | *pressioni* | caso del complemento |
| 13 | p. 319 | *Iisdem positis … resistituntur* | *resistuntur* | forma verbale |
| 14 | p. 326 | *ratione densitas medii* | *densitatis* | desinenza |

### A.10 Formule SVG di Motte

Nel corso del lavoro l’EPUB di Motte è stato reso disponibile (`src_epub/OEBPS/`). Tutte le immagini SVG di questa parte sono state rese con `rsvg-convert` e lette una per una:

| SVG | Luogo Motte | Formula attesa dal latino | Immagine | Esito |
|---|---|---|---|---|
| 732 | Prop. XXXIV, «take bH equal to [SVG 732]» | BE²/CB | BE²/CB | torna |
| 733 | Prop. XXXV, Cor. 7, «lose … the part [SVG 733]» | tM/(T+t) | tM/(T+t) | torna |
| 734 | id., «the part [SVG 734] remaining» | TM/(T+t) | TM/(T+t) | torna |
| 735 | id., «the logarithm of the number [SVG 735]» | (T+t)/T | (T+t)/T | torna |
| 455 | id., «is to the number [SVG 455]» | t/T | t/T | torna (immagine riusata) |
| 736 | Prop. XXXVI, «or as [SVG 736] to [SVG 727]» | 5½ | 5½ | torna |
| 727 | id. | 6½ | 6½ | torna (immagine riusata) |
| 737 | Prop. XXXVI, «being [SVG 737] parts of an inch» | 5/8 | 5/8 | torna |
| 738 | id., «was [SVG 738] of an inch» | 21/40 | 21/40 | torna |
| 739 | Prop. XXXVI, Cor. 9 e 10 | ½GH | ½GH | torna |
| 740 | Cor. 10; Prop. XXXVII (passim) | EF² | EF² | torna |
| 741 | Cor. 10; Prop. XXXVII (passim), Cor. 2–3 | EF² − ½PQ² | EF² − ½PQ² | torna |
| 742 | Prop. XXXVII, secondo e terzo capoverso | ½IG | ½IG | torna |
| 743 | Prop. XXXVII, «to the circle [SVG 743]» | EF (*ad circulum EF*) | EF | torna |
| 744 | Prop. XXXVII, terzo e quarto capoverso, Cor. 3 | EF² − PQ² | EF² − PQ² | torna |
| 128 | Scolio della Prop. XXXVII, «as HG to [SVG 128]» | ½AB | ½AB | torna (immagine riusata) |

Controllo incrociato con la tabella `src_epub/svg_tex.tsv` (attributi `data-tex` dell’EPUB): il LaTeX delle sedici immagini coincide con le letture qui sopra. Sedici immagini distinte, tutte conformi al latino: **nessuna formula di Motte da segnalare, nessuna SVG rimasta da controllare**. Nel Cor. 2 della Prop. XXXVII Motte scrive in testo «EF2 to EF2 - PQ2»: apici appiattiti nell’estratto, formula coerente con il latino. Le letture delle frazioni appiattite della trascrizione (A.9) sono confermate dalle immagini.

### A.11 Riepilogo: dove Motte aggiunge, omette o sbaglia

| Luogo | Latino | Motte 1846 | Tipo |
|---|---|---|---|
| II.S7.02 | *Corpora … moveri dico* | «are said to be moved» | resa impersonale |
| II.S7.03 | *Est enim eadem ratio* | «for the case … is the very same» | *ratio* reso «case» |
| II.S7.05 | *ratione densitatis* | «the **simple** ratio of the density» | aggiunta (corretta nel senso) |
| II.S7.08 | *virium T ad vires V* | «the force T to the force V» | numero |
| II.S7.11 | *Ex medii subtilitate …* | «**For** the resistance …» | aggiunta di un nesso causale |
| II.S7.14 | *quo impetu* | «with what force» | termine non conforme al glossario |
| II.S7.14 | *si particulæ medii quiescerent* | «if the particles of the medium are at rest» | irreale reso indicativo |
| II.S7.16 | *non inutilem futuram esse censeo* | «may be of use» | litote attenuata |
| II.S7.17 | *Quod si* | «If» | omissione |
| II.S7.20 | *duplo minor quam prius* | «but half so great» | omissione di *quam prius* |
| II.S7.31 | *orificium superius* | «the mouth of it» | omissione di *superius* |
| II.S7.31 | *horizontem versus* | «to the plane of the horizon» | esplicitazione |
| II.S7.33 | *Eadem vis … debet* | «ought **always** to generate» | aggiunta |
| II.S7.37 | *HG vel IG* | «IG or HG» | ordine invertito |
| II.S7.38 | *æquali impetu in omnes partes fertur* | «tends **always** with an equal force» | aggiunta di *always*, omissione di *in omnes partes* |
| II.S7.40 | *accelerabit* | «does **not at all** accelerate» | Motte ha la negazione che manca nella trascrizione (A.9, ECCO n. 1) |
| II.S7.43 | un solo periodo | tre frasi | ristrutturazione |
| II.S7.47 | ordine della frase | riordinata | ristrutturazione |
| II.S7.48 | *[dimidium] sphæroidis* | «the half of a spheroid» | Motte ha il termine che manca nella trascrizione |
| II.S7.48 | *Nam ut motus aquæ sit maxime directus* | «For **though** the motion … tends directly downwards» | *ut* letto concessivo (qui: finale) |
| II.S7.54 | *inter circellum & latera vasis* | «the sides of the vessel» | fedele al latino (che dovrebbe dire «canale») |
| II.S7.58 | *tempore pariter aucto vel diminuto* | «because the time is increased …» | ablativo assoluto sciolto in causale aggiunta |
| II.S7.64 | *minor esse non potest quam in ratione 2 ad 3* | «must be … in the ratio of 2 to 3, at the least» | resa per il senso (corretta) |

Nessun errore di sostanza di Motte; le sedici formule in immagine sono state controllate e tornano tutte (A.10).

---

## Note editoriali e fisiche

Queste note sono aggiunte del presente fascicolo, non affermazioni tradotte da Newton. Le verifiche numeriche sono state eseguite con uno script Python (`tmp/18a/script/verifica.py`, conservato con i materiali di lavoro); i risultati sono riportati qui.

### N1. Prop. XXXII: la similitudine dinamica

La condizione che le forze acceleratrici stiano «come i diametri inversamente e i quadrati delle velocità direttamente» è la condizione perché due sistemi geometricamente simili restino simili nel tempo: se le lunghezze scalano di un fattore λ e le velocità di un fattore μ, i tempi scalano come λ/μ e le accelerazioni come μ²/λ. In termini moderni è un primo enunciato del principio di similitudine meccanica, che nella Prop. XXXIII produce la legge R ∝ ρ v² d² (corrispondenza moderna, non nel testo).

### N2. Prop. XXXIII: due generi di resistenza

Newton distingue la resistenza dovuta alle forze fra le particelle (fluido elastico) da quella dovuta agli urti. Entrambe, sotto l’ipotesi di similitudine, scalano come ρ v² d²: per il primo genere forza acceleratrice ∝ v²/d per massa ∝ ρ d³; per il secondo numero di urti ∝ v/d per forza di ciascun urto ∝ v ρ d³. Controllato in forma simbolica: entrambe le combinazioni danno ρ v² d².

### N3. Prop. XXXIII, Cor. 2: il passaggio al limite

L’argomento dei quattro corpi D, E, F, G è un passaggio al limite: aumentando le velocità e diminuendo le forze delle particelle (nel rapporto duplicato), il mezzo B si comporta sempre più come il mezzo C privo di forze, in cui la resistenza è esattamente quadratica. Ne segue che nei fluidi elastici la resistenza dei corpi molto veloci è quadratica «con ottima approssimazione». Il Cor. 5 aggiunge che a parità di densità la grana del mezzo non conta.

### N4. La «saetta» e la legge del seno al quadrato

La Prop. XXXIV usa il modello d’urto oggi detto «legge di Newton» della resistenza (impatto di particelle indipendenti): su un elemento di superficie inclinato la forza nella direzione del moto è proporzionale al quadrato del coseno dell’angolo fra la normale e la direzione del moto (le due proiezioni LD/LB e BE/BC). Il modello vale bene per gas molto rarefatti e per flussi ipersonici; non per l’aria ordinaria a bassa velocità (non verificato sulle fonti allegate).

### N5. Prop. XXXIV: verifica numerica

Con sfera di raggio r = 1, BE = √(r² − ρ²) (ρ distanza dall’asse) e bH = BE²/r, il volume del solido delle bH, integrato numericamente su 200 000 anelli, è **0,500000** del cilindro circoscritto πr³; la superficie dei punti H dista dal piano per C di ρ²/r (controllo a ρ = 0,6: 0,36 = 0,36), cioè è un paraboloide di vertice C e lato retto CA, come dice Newton. L’integrazione diretta della forza assiale con il fattore cos² dà ancora **0,500000** della forza sul disco. La resistenza del globo è la metà di quella del cilindro: confermato.

### N6. Prop. XXXV: i «due terzi del diametro» e il Cor. 7

- **Caso 1.** Con riflessione totale il cilindro (diametro = altezza = 2r) cede alle particelle il doppio della propria velocità: R = 2ρ πr² v². La forza che toglie il moto del cilindro (massa ρ_c·2πr³) nel tempo in cui esso percorre metà dell’asse (r) vale 2πr² ρ_c v²: il rapporto è ρ/ρ_c. Per il globo (resistenza metà, volume 2/3 del cilindro) la distanza corrispondente risulta **0,6667** diametri (caso elastico), **1,3333** (Cor. 1, corpi duri) e **2,6667** (mezzi continui, Scolio): 2/3, 4/3, 8/3 come nel testo.
- **Cor. 7.** Con resistenza quadratica la velocità segue v = v₀/(1 + t/T). Integrazione numerica con T = 1, t = 0,7: moto restante 0,588235 (formula TM/(T+t) = 0,588235); spazio/spazio uniforme 0,758040 (formula log₁₀((T+t)/T) × 2,302585092994 / (t/T) = 0,758040). Il numero 2,302585092994 è ln 10 = 2,302585092994046: le dodici cifre decimali di Newton sono corrette. Il «logaritmo» del testo è dunque il logaritmo decimale delle tavole, e il prodotto dà il logaritmo naturale (iperbolico).

### N7. Scolio della Prop. XXXIV: il tronco di cono

Con il modello del seno al quadrato la resistenza di un tronco di raggio di base R, altezza h e raggio superiore a è proporzionale a a² + (R² − a²)(R − a)²/((R − a)² + h²). La minimizzazione numerica (passo R/100 000) confrontata con la costruzione di Newton (Q metà di OD, QS = QC, S vertice) dà:

| R | h | a ottimo (numerico) | a dalla costruzione |
|---|---|---|---|
| 1 | 1 | 0,38197 | 0,38197 |
| 1 | 0,5 | 0,60961 | 0,60961 |
| 2 | 1,3 | 1,05556 | 1,05557 |
| 1 | 3 | 0,09167 | 0,09167 |

La costruzione è esatta. Poiché OS = h/2 + √(h²/4 + R²) > R, l’angolo CSB è sempre acuto, come dice Newton nel capoverso successivo; di qui la regola dei 135°.

### N8. Scolio della Prop. XXXIV: il solido di minima resistenza

Newton enuncia senza dimostrazione la condizione MN : GR = GR³ : 4BR×GB². Detto φ l’angolo fra la tangente in N e l’asse, si ha GR = GB/sen φ, BR = GB·cot φ, e la condizione diventa MN = GB/(4 sen³φ cos φ), cioè, con p = tg φ, y = (GB/4)(1 + p²)²/p³: è la forma nota della soluzione del problema di minima resistenza (corrispondenza moderna, non verificata sulle fonti allegate). Controllo numerico dell’identità per φ = 0,5; 0,7; π/4: le due espressioni coincidono (2,585167; 1,222560; 1,000000). Per φ = 45° si ottiene MN = GB: la curva si raccorda al disco frontale di raggio GB con tangente inclinata di 45°, cioè con l’angolo di 135° del capoverso precedente. Non è stata verificata la minimalità.

### N9. *Cataracta*: «cateratta»

Newton chiama *cataracta vel columna aquæ* la colonna d’acqua che cade dal piano AB al foro EF restringendosi. «Cateratta» qui non è né la paratoia né la cascata in senso geografico, ma il getto d’acqua in caduta libera; Motte «cataract». La resa è quella fissata dal coordinatore.

### N10. Prop. XXXVI: i numeri dell’esperimento

| Dato di Newton | Controllo | Esito |
|---|---|---|
| foro 5/8 di pollice, vena 21/40 di pollice | (21/40) : (5/8) = 0,84 = 21/25 | torna |
| vena : foro «come 5 a 6, ossia come 5½ a 6½» | 5/6 = 0,833; 5½/6½ = 0,846; 21/25 = 0,840 | torna: 21/25 sta fra le due stime |
| velocità «nel rapporto di 25×25 a 21×21, ossia di 17 a 12, circa subduplicato di 2 a 1» | 625/441 = 1,4172; 17/12 = 1,4167; √2 = 1,4142 | torna |
| velocità nel foro pari a quella dovuta a metà altezza | (21/25)² = 0,7056 contro √(1/2) = 0,7071 | torna con ottima approssimazione |
| Caso 3: altezze 20 e 20 pollici, gittata teorica 40, lato retto 80 | gittata = 2√(20·20) = 40; lato retto = 40²/20 = 80 = 4 × 20 | torna |
| gittata misurata 37 pollici | — | dato sperimentale, non verificabile |

Il rapporto 21 : 25 dei diametri è il fenomeno oggi detto «vena contratta»; il coefficiente di contrazione dell’area (21/25)² ≈ 0,71 è vicino ai valori moderni per fori in parete sottile, circa 0,61–0,64 (non verificato sulle fonti allegate). La costruzione con il piano VW e il foro ST serve a sostituire il foro reale con la sezione della vena.

### N11. Prop. XXXVI, Cor. 1–6: la ripartizione del peso

Con cerchi di area AB = 5 ed EF = 1,3 (unità arbitrarie), IH = 1, IG = IH·(AB/EF)², IO = √(IH·IG):

- Cor. 1: IH/IG = 0,0676 = (EF/AB)²;
- Cor. 3: HG/2HO = (IH+IO)/2IH = (AB+EF)/2EF = 2,4231; e EF/AB = IO/IG = √(IH/IG) = 0,26;
- Cor. 4: peso totale / peso sul fondo = 1,7027 = (AB+EF)/(AB−EF);
- Cor. 5: peso sul fondo / peso nel deflusso = 1,4231 = (AB−EF)/2EF;
- Cor. 6: peso sul fondo / peso dell’acqua sovrastante il fondo = 0,7937 = AB/(AB+EF) = AB/(2AB − fondo).

Cor. 2: con v² = 2g·GI e tempo di caduta t = v/g, la lunghezza d’acqua uscita nel tempo t è v·t = 2GI: la colonna ha altezza 2GI, come nel testo. Tutti i rapporti tornano.

### N12. Prop. XXXVI, Cor. 7–10: il cerchietto PQ

Il Cor. 7 dà un limite inferiore (cono: 1/3 del cilindro di altezza GH), il Cor. 8 un limite superiore per PQ piccolo (mezzo sferoide: 2/3), il Cor. 9 la media aritmetica (1/2, verificato: (1/3 + 2/3)/2 = 1/2), il Cor. 10 una formula d’interpolazione presentata *quantum sentio*, «per quanto mi sembra». Controllo di coerenza: con PQ → 0 il Cor. 10 dà 1 × (cilindro di altezza ½GH), come il Cor. 9; con PQ = EF dà 2 × (cilindro di altezza ½GH) = cilindro di altezza GH, come la seconda parte del Cor. 9 (valori calcolati: 1,0000; 1,1429 per PQ = ½EF; 2,0000). La formula non è dimostrata nel testo e su di essa poggia la Prop. XXXVII.

### N13. Prop. XXXVII: il «quadruplo della lunghezza»

Resistenza = peso di un cilindro d’acqua di base PQ e altezza ½IG, con v² = 2g·IG: R = ρ g A · IG/2 = ρ A v²/4. La forza che genera il moto del cilindro (massa ρ_c A L, velocità v) nel tempo 4L/v in cui esso percorre 4L vale ρ_c A v²/4. Il rapporto è ρ/ρ_c, indipendente da L (verifica numerica: R/F = 0,3333 con ρ/ρ_c = 1/3). Il cilindro d’acqua di lunghezza ½IG, cadendo da IG, nel tempo di caduta v/g percorre alla velocità v lo spazio v²/g = 2IG = 4 × (½IG): «il quadruplo della sua lunghezza» (verifica: 4,0). In termini moderni R = ½ C ρ A v² con C = ½ (corrispondenza moderna).

Cinematica del terzo capoverso: con PQ = 0,3 EF (diametri) le formule danno u/w = 10,111 e u/(u + w) = 0,9100 = (EF² − PQ²)/EF²; il Cor. 2 (rapporto composto EF²/(EF² − ½PQ²) una volta, EF²/(EF² − PQ²) due volte) coincide con il calcolo diretto (0,42150 = 0,42150 per PQ = 0,3; 0,99244 = 0,99244 per PQ = 0,6, con ρ/ρ_c = 1/3). È un controllo di coerenza interna, non una verifica indipendente del Cor. 10.

### N14. Scolio della Prop. XXXVII

Il fattore (25/21)² = 1,4172 è la stessa correzione della vena contratta della Prop. XXXVI applicata, a parti invertite, alla resistenza. L’ultima frase rinvia al Cor. 7 della Prop. XXXVI: il cerchietto sostiene più di 1/3 del cilindro GH, mentre la Prop. XXXVII usa 1/2 (Cor. 9); il rapporto 1/3 : 1/2 = 2 : 3 è il minimo cui la resistenza della figura con testa e coda può scendere rispetto alla forza della proposizione. La forma esatta della testa (lato retto λ con λ : HG = HG : ½AB) e della coda (4λ) non è stata verificata numericamente.

### N15. Che cosa questa parte prepara

Lo Scolio della Prop. XXXV annuncia il risultato dei mezzi continui (otto terzi del diametro per il globo); la Prop. XXXVII lo ottiene per il cilindro (quadruplo della lunghezza). Il passaggio dal cilindro al globo, attraverso i Lemmi V–VII, è nella seconda parte della Sezione (Fascicolo 18b).

---

## Controllo della copertura

Pagine 1726 dai marcatori ‹n› della trascrizione. Per Motte l’estratto non ha marcatori di pagina: si indicano le righe di `fonti/motte-1846-L2-S07.md`.

| Identificatori | Incipit latino | Contenuto | 1726 | Motte 1846 (righe dell’estratto) |
|---|---|---|---|---|
| — | *SECTIO VII. De motu fluidorum* | titolo della Sezione | p. 318 | 8–9 |
| II.S7.01–II.S7.02 | *Si corporum systemata duo similia* | Prop. XXXII, enunciato e dimostrazione | pp. 318–319 | 12–61 |
| II.S7.03–II.S7.04 | *Hinc si corpora duo quævis* … *Et si similes* | Prop. XXXII, Cor. 1–2 | p. 319 | 63–78 |
| II.S7.05–II.S7.06 | *Iisdem positis, dico* | Prop. XXXIII, enunciato e dimostrazione | pp. 319–320 | 80–113 |
| II.S7.07–II.S7.12 | *Igitur si systemata illa* … *Hæc omnia ita se habent* | Prop. XXXIII, Cor. 1–6 | pp. 320–322 | 115–195 |
| II.S7.13–II.S7.14 | *Si globus & cylindrus* | Prop. XXXIV | pp. 322–323 | 197–247 |
| II.S7.15–II.S7.17 | *Eadem methodo* … *Unde obiter* … *Quod si figura DNFG* | Scolio della Prop. XXXIV | pp. 323–325 | 249–284 |
| II.S7.18–II.S7.21 | *Si medium rarum* | Prop. XXXV, enunciato, Casi 1–3 | pp. 325–326 | 286–327 |
| II.S7.22–II.S7.28 | *Hinc si globus & particulæ* … *Hinc si globus tempore T* | Prop. XXXV, Cor. 1–7 | pp. 326–327 | 329–378 |
| II.S7.29 | *In hac propositione exposui* | Scolio della Prop. XXXV | p. 327 | 380–402 |
| II.S7.30–II.S7.31 | *Aquæ de vase cylindrico* … *Sit ACDB* | Prop. XXXVI, enunciato e costruzione | pp. 327–328 | 404–444 |
| II.S7.32–II.S7.35 | *Concipe jam* … *Liquescat* … *Sed foramen* … *In sequentibus* | Prop. XXXVI, Caso 1 (con l’esperimento della vena) | pp. 328–331 | 446–541 |
| II.S7.36–II.S7.40 | *Si foramen EF non sit* … *Si vasis ABDC pars inferior* | Prop. XXXVI, Casi 2–6 | pp. 331–332 | 543–601 |
| II.S7.41–II.S7.46 | *Hinc si aquæ altitudo* … *Ponderis autem pars* | Prop. XXXVI, Cor. 1–6 | pp. 332–333 | 603–665 |
| II.S7.47–II.S7.50 | *Si in medio foraminis* … *Et (quantum sentio)* | Prop. XXXVI, Cor. 7–10 | pp. 333–335 | 667–736 |
| II.S7.51–II.S7.52 | *Cylindri, qui secundum longitudinem* | Lemma IV | p. 335 | 738–748 |
| II.S7.53–II.S7.59 | *Cylindri, qui in fluido compresso* | Prop. XXXVII, enunciato e dimostrazione | pp. 336–338 | 750–841 |
| II.S7.60 | *Fluidum autem comprimi debet* | Prop. XXXVII, giustificazione delle ipotesi | p. 338 | 843–860 |
| II.S7.61–II.S7.63 | *Cylindrorum, qui* … *Iisdem positis* | Prop. XXXVII, Cor. 1–3 | pp. 338–339 | 862–887 |
| II.S7.64 | *In hac propostione resistentiam* | Scolio della Prop. XXXVII | pp. 339–340 | 889–941 |

**Controlli eseguiti.**

1. **Copertura.** Ho riletto in sequenza ogni periodo della trascrizione, da *SECTIO VII.* a *per corol. 7. prop. XXXVI.* (riga 166, ultima prima di *LEMMA V.*), contro la traduzione: nessuna frase manca. I 64 identificatori sono consecutivi e unici (controllo automatico).
2. **Parte B.** `check.py` sul file finale: JSON valido, 9 unità, 89 passi; tutte le stringhe `la` sono sottostringhe esatte della trascrizione, tutte le stringhe `en` sottostringhe esatte di Motte; ogni identificatore di `copertura` è presente nel testo. Controllo aggiuntivo: ogni stringa `it` della Parte B è sottostringa esatta della traduzione del fascicolo.
3. **Matematica.** Verifiche numeriche (N5–N8, N10–N14) per le Propp. XXXIV, XXXV (Casi, Cor. 1, Cor. 7, Scolio), lo Scolio della XXXIV (tronco di cono; identità della curva di minima resistenza), la Prop. XXXVI (dati sperimentali, Cor. 1–6, 9–10), la Prop. XXXVII (con Cor. 2) e il suo Scolio. Tutti i risultati e tutte le cifre di Newton tornano; nessuna tabella numerica in questa parte.
4. **Motte.** Confronto di tutta la sezione corrispondente, comprese le 16 formule SVG (rese con `rsvg-convert` e confrontate con `svg_tex.tsv`): tutte conformi. Divergenze nel § A.11.
5. **Rimandi.** Quindici rimandi verificati (A.8), di cui uno al Libro I (Prop. IV, Cor. 1 e 8): tutti reggono.
6. **Separazione fra testo e commento.** Il testo tradotto non contiene formule moderne; le integrazioni del curatore sono tra parentesi quadre («[non]» in II.S7.40, «[la metà di]» in II.S7.48, la glossa in II.S7.64).

**Non ho potuto verificare:**

- **la stampa del 1726**: i punti elencati in A.9 e nella tabella ECCO, in particolare la negazione mancante del Caso 6 (II.S7.40) e la lacuna del Cor. 8 (II.S7.48);
- **le figure originali** NATP00088-51…62: la disposizione dei punti (in particolare KC perpendicolare all’asse nella Prop. XXXIV, la posizione di O fra H e G nel Cor. 3, la forma di testa e coda nello Scolio della Prop. XXXVII) è ricostruita dal testo;
- **la paginazione di Motte**: l’estratto non ha ancoraggi di pagina;
- la minimalità del solido dello Scolio della Prop. XXXIV (verificata solo l’identità con la forma nota) e le proporzioni di testa e coda nello Scolio della Prop. XXXVII;
- il Cor. 10 della Prop. XXXVI, che Newton presenta come congettura: controllata solo la coerenza con il Cor. 9.

---

## Registro del lavoro successivo

| Unità | Stato |
|---|---|
| Libro II, Sezione VII, prima parte (Propp. XXXII–XXXVII, Lemma IV) | **Fascicolo 18a, presente documento, prima versione** |
| Sezione VII, seconda parte (Lemmi V–VII, Propp. XXXVIII–XL, Scolio) | Fascicolo 18b; numerazione da II.S7.65 |
| Refusi e punti ECCO (A.9) | Da verificare sulla stampa del 1726; priorità: II.S7.40 (negazione) e II.S7.48 (*dimidium*) |
| Resa di *plaga* («verso» qui, «parte» nel Fascicolo 3) | Da armonizzare fra i fascicoli (A.0) |
| Termini nuovi (A.0): *vena*, *cerchietto*, *acqua ferma*, *spazio anulare*, *la metà* per *duplo minor*, *per uguaglianza perturbata* | Da armonizzare dal coordinatore |
| Formule SVG di Motte | Tutte controllate (A.10) |
| Pagine interattive | Parte B: 9 unità, 89 passi; la Prop. XXXVI (32 passi) andrà forse divisa in costruzione, Caso 1 ed esperimento della vena |
| Figure NATP00088-51…62 | Da consultare per confermare le ricostruzioni di `figura_base` |
| Revisione filologica e scientifica indipendente | Da eseguire |

Il presente testo è una nuova traduzione assistita da IA. Non riproduce traduzioni italiane o inglesi moderne. **Licenza prevista** (decisione del curatore, Fascicolo 3): testi e traduzioni CC BY-SA 4.0, codice MIT. La trascrizione latina è © The Newton Project; i testi di Motte sono di pubblico dominio.

---

## Parte B — Dati per le pagine interattive

Unità incluse: le proposizioni, i corollari e gli scolii con costruzione geometrica propria. **Escluse**: le Propp. XXXII e XXXIII (argomenti di similitudine senza figura) e i loro corollari; la Prop. XXXV nei Casi 1–3 (calcolo per rapporti, senza figura); i Casi 2–6 e i Cor. 1, 2, 4–6, 9, 10 della Prop. XXXVI (senza costruzione propria o con argomento puramente proporzionale); il Lemma IV; i Cor. 1–3 della Prop. XXXVII; il capoverso *Fluidum autem comprimi debet*. Nella Prop. XXXVI sono inclusi la costruzione e tutto il Caso 1 (II.S7.31–II.S7.35), compreso l’esperimento della vena contratta.

Convenzioni:

- `la`: testo latino esatto della trascrizione, refusi e frazioni appiattite compresi; i marcatori di pagina ‹n› sono conservati, i marcatori [FIG n] eliminati; le letture sono in `nota` e nell’apparato;
- `it`: la traduzione di questo fascicolo (sottostringa esatta del testo tradotto);
- `en`: Motte 1846, allineato per senso; i marcatori `[SVG n]` restano e vanno sostituiti con le formule della tabella A.10;
- `dipende_da`: soltanto i rimandi citati nella frase latina; i rimandi impliciti sono dichiarati in `nota`;
- `figura.mostra`: elementi da rendere visibili, cumulativi; `figura.evidenzia`: relazioni da mettere in risalto.

```json
{
 "fascicolo": "18a-L2-S7",
 "versione": "0.1",
 "data": "2026-11-08",
 "convenzioni": {
  "dipende_da": "solo rimandi citati esplicitamente nella frase latina (rimandi impliciti dichiarati in nota)",
  "en": "Motte 1846, allineato per senso; i marcatori [SVG n] restano nelle stringhe e vanno sostituiti con le formule dell’EPUB (tutte lette e conformi al latino: tabella A.10 dell’apparato)",
  "figura.mostra": "elementi da rendere visibili al passo, cumulativi salvo indicazione",
  "la": ""
 },
 "unita": [
  {
   "id": "L2-P34",
   "tipo": "Propositio/Theorema",
   "titolo": "Prop. XXXIV — globo e cilindro in un mezzo rado: la resistenza del globo è la metà",
   "copertura": [
    "II.S7.13",
    "II.S7.14"
   ],
   "fonti": {
    "la": "",
    "en": "Motte 1846, Section VII, Prop. XXXIV (pagina non ricavabile dall’estratto)"
   },
   "enunciato": {
    "la": "",
    "it": "Se un globo e un cilindro, descritti su diametri uguali, si muovono con velocità uguale, nel verso dell’asse del cilindro, in un mezzo rado costituito di particelle uguali e disposte liberamente a distanze uguali l’una dall’altra, la resistenza del globo sarà la metà della resistenza del cilindro.",
    "en": "If in a rare medium, consisting of equal particles freely disposed at equal distances from each other, a globe and a cylinder described on equal diameters move with equal velocities in the direction of the axis of the cylinder, the resistance of the globe will be but half so great as that of the cylinder."
   },
   "figura_base": {
    "punti": [
     "A",
     "B",
     "C",
     "K",
     "I",
     "F",
     "L",
     "D",
     "E",
     "b",
     "H",
     "N",
     "O",
     "G",
     "Q"
    ],
    "vincoli": [
     "sfera ABKI di centro C e raggio CA; A e I estremi dell’asse ACI",
     "KC raggio perpendicolare all’asse AC (ricostruzione: BE ⊥ KC dev’essere parallela all’asse perché BE/BC sia il coseno d’incidenza)",
     "FB parallela ad AC, B sulla sfera; LB = CB su FB; BD tangente in B",
     "BE ⊥ KC, LD ⊥ BD",
     "cilindro ONGQ circoscritto, base NAO tangente in A; b sulla base, sulla parallela all’asse per B",
     "bE ∥ asse, bE = AC; bH = BE²/CB"
    ]
   },
   "passi": [
    {
     "id": "L2-P34-p1",
     "la": "",
     "it": "Poiché infatti l’azione del mezzo sul corpo è la stessa (per il Cor. 5 delle leggi) sia che il corpo si muova in un mezzo in quiete, sia che le particelle del mezzo urtino con la stessa velocità il corpo in quiete, consideriamo il corpo come in quiete e vediamo con quale impeto sarà sollecitato dal mezzo in moto.",
     "en": "For since the action of the medium upon the body is the same (by Cor. 5 of the Laws) whether the body move in a quiescent medium, or whether the particles of the medium impinge with the same velocity upon the quiescent body, let us consider the body as if it were quiescent, and see with what force it would be impelled by the moving medium.",
     "dipende_da": [
      "Leggi, Cor. V"
     ],
     "figura": {
      "mostra": [
       "corpo in quiete",
       "flusso di particelle parallelo all’asse"
      ],
      "evidenzia": [
       "cambio di sistema di riferimento"
      ]
     },
     "nota": "Motte rende impetu con «force»."
    },
    {
     "id": "L2-P34-p2",
     "la": "",
     "it": "Rappresenti dunque ABKI un corpo sferico descritto con centro C e semidiametro CA, e le particelle del mezzo incidano con una velocità data su quel corpo sferico lungo rette parallele ad AC; e sia FB una retta di questo genere.",
     "en": "Let, therefore, ABKI represent a spherical body described from the centre C with the semi-diameter CA, and let the particles of the medium impinge with a given velocity upon that spherical body in the directions of right lines parallel to AC; and let FB be one of those right lines.",
     "dipende_da": [],
     "figura": {
      "mostra": [
       "sfera ABKI",
       "C",
       "CA",
       "retta FB ∥ AC",
       "B"
      ]
     }
    },
    {
     "id": "L2-P34-p3",
     "la": "",
     "it": "Su di essa si prenda LB uguale al semidiametro CB, e si conduca BD tangente alla sfera in B.",
     "en": "In FB take LB equal to the semi-diameter CB, and draw BD touching the sphere in B.",
     "dipende_da": [],
     "figura": {
      "mostra": [
       "L su FB, LB = CB",
       "tangente BD"
      ]
     }
    },
    {
     "id": "L2-P34-p4",
     "la": "",
     "it": "Su KC e su BD si abbassino le perpendicolari BE, LD; e la forza con cui una particella del mezzo, incidendo obliquamente lungo la retta FB, colpisce il globo in B, starà alla forza con cui la stessa particella colpirebbe perpendicolarmente in b il cilindro ONGQ descritto attorno al globo con asse ACI, come LD sta a LB, ossia come BE sta a BC.",
     "en": "Upon KC and BD let fall the perpendiculars BE, LD; and the force with which a particle of the medium, impinging on the globe obliquely in the direction FB, would strike the globe in B, will be to the force with which the same particle, meeting the cylinder ONGQ, described about the globe with the axis ACI, would strike it perpendicularly in b, as LD to LB, or BE to BC.",
     "dipende_da": [],
     "figura": {
      "mostra": [
       "KC",
       "BE ⊥ KC",
       "LD ⊥ BD",
       "cilindro ONGQ",
       "b"
      ],
      "evidenzia": [
       "LD : LB = BE : BC (componente normale dell’urto)"
      ]
     }
    },
    {
     "id": "L2-P34-p5",
     "la": "",
     "it": "Di nuovo, l’efficacia di questa forza a muovere il globo nel verso della sua incidenza FB, ossia AC, sta alla sua efficacia a muovere il globo nel verso della sua direzione, cioè nel verso della retta BC lungo la quale spinge direttamente il globo, come BE sta a BC.",
     "en": "Again; the efficacy of this force to move the globe, according to the direction of its incidence FB or AC, is to the efficacy of the same to move the globe, according to the direction of its determination, that is, in the direction of the right line BC in which it impels the globe directly, as BE to BC.",
     "dipende_da": [],
     "figura": {
      "mostra": [
       "retta BC",
       "componente lungo AC"
      ],
      "evidenzia": [
       "seconda proiezione: BE : BC"
      ]
     }
    },
    {
     "id": "L2-P34-p6",
     "la": "",
     "it": "E, riuniti i rapporti, l’efficacia di una particella che incide obliquamente sul globo lungo la retta FB, a muoverlo nel verso della sua incidenza, sta all’efficacia della stessa particella che incide perpendicolarmente sul cilindro lungo la stessa retta, a muoverlo nello stesso verso, come il quadrato di BE sta al quadrato di BC.",
     "en": "And, joining these ratios, the efficacy of a particle, falling upon the globe obliquely in the direction of the right line FB, to move the globe in the direction of its incidence, is to the efficacy of the same particle falling in the same line perpendicularly on the cylinder, to move it in the same direction, as BE2 to BC2.",
     "dipende_da": [],
     "figura": {
      "mostra": [],
      "evidenzia": [
       "BE² : BC²"
      ]
     },
     "nota": "Motte stampa «BE2 to BC2» con gli apici appiattiti."
    },
    {
     "id": "L2-P34-p7",
     "la": "",
     "it": "Perciò se su bE, che è perpendicolare alla base circolare NAO del cilindro e uguale al raggio AC, si prende bH uguale a BE²/CB, bH starà a bE come l’effetto della particella sul globo sta all’effetto della particella sul cilindro.",
     "en": "Therefore if in bE, which is perpendicular to the circular base of the cylinder NAO, and equal to the radius AC, we take bH equal to [SVG 732]; then bH will be to bE as the effect of the particle upon the globe to the effect of the particle upon the cylinder.",
     "dipende_da": [],
     "figura": {
      "mostra": [
       "bE ∥ asse, bE = AC",
       "H su bE, bH = BE²/CB"
      ],
      "evidenzia": [
       "bH : bE = effetto sul globo : effetto sul cilindro"
      ]
     },
     "nota": "La trascrizione appiattisce BE²/CB in «BE quad.CB»; Motte [SVG 732] = BE²/CB (verificato)."
    },
    {
     "id": "L2-P34-p8",
     "la": "",
     "it": "E perciò il solido occupato da tutte le rette bH starà al solido occupato da tutte le rette bE come l’effetto di tutte le particelle sul globo sta all’effetto di tutte le particelle sul cilindro.",
     "en": "And therefore the solid which is formed by all the right lines bH will be to the solid formed by all the right lines bE as the effect of all the particles upon the globe to the effect of all the particles upon the cylinder.",
     "dipende_da": [],
     "figura": {
      "mostra": [
       "solido delle bH",
       "cilindro delle bE"
      ]
     }
    },
    {
     "id": "L2-P34-p9",
     "la": "",
     "it": "Ma il primo solido è un paraboloide descritto con vertice C, asse CA e lato retto CA, e il secondo solido è il cilindro circoscritto al paraboloide: ed è noto che il paraboloide è la metà del cilindro circoscritto.",
     "en": "But the former of these solids is a paraboloid whose vertex is C, its axis CA, and latus rectum CA, and the latter solid is a cylinder circumscribing the paraboloid; and it is known that a paraboloid is half its circumscribed cylinder.",
     "dipende_da": [],
     "figura": {
      "mostra": [
       "paraboloide di vertice C, asse CA, lato retto CA"
      ],
      "evidenzia": [
       "volume paraboloide = ½ cilindro"
      ]
     }
    },
    {
     "id": "L2-P34-p10",
     "la": "",
     "it": "Dunque la forza totale del mezzo sul globo è la metà della sua forza totale sul cilindro.",
     "en": "Therefore the whole force of the medium upon the globe is half of the entire force of the same upon the cylinder.",
     "dipende_da": [],
     "figura": {
      "mostra": [],
      "evidenzia": [
       "forza sul globo = ½ forza sul cilindro"
      ]
     }
    },
    {
     "id": "L2-P34-p11",
     "la": "",
     "it": "E perciò, se le particelle del mezzo fossero in quiete e il cilindro e il globo si muovessero con velocità uguale, la resistenza del globo sarebbe la metà della resistenza del cilindro. C.V.D.",
     "en": "And therefore if the particles of the medium are at rest, and the cylinder and globe move with equal velocities, the resistance of the globe will be half the resistance of the cylinder. Q.E.D.",
     "dipende_da": [
      "Leggi, Cor. V"
     ],
     "figura": {
      "mostra": [
       "ritorno al mezzo in quiete"
      ]
     },
     "nota": "Il rimando al Cor. V è implicito (ripresa del passo 1); Motte rende il congiuntivo irreale con l’indicativo «are at rest»."
    }
   ]
  },
  {
   "id": "L2-P34-Schol",
   "tipo": "Scholium",
   "titolo": "Scolio alla Prop. XXXIV — tronco di cono e solido di minima resistenza",
   "copertura": [
    "II.S7.15",
    "II.S7.16",
    "II.S7.17"
   ],
   "fonti": {
    "la": "",
    "en": "Motte 1846, Section VII, Scholium alla Prop. XXXIV"
   },
   "enunciato": {
    "la": "",
    "it": "Con lo stesso metodo si possono confrontare fra loro altre figure quanto alla resistenza, e trovare quelle che sono più adatte a continuare i loro moti nei mezzi resistenti.",
    "en": "By the same method other figures may be compared together as to their resistance; and those may be found which are most apt to continue their motions in resisting mediums."
   },
   "figura_base": {
    "punti": [
     "O",
     "C",
     "E",
     "B",
     "H",
     "D",
     "Q",
     "S",
     "G",
     "F",
     "A",
     "I",
     "N",
     "M",
     "R"
    ],
    "vincoli": [
     "fig. 52: base circolare CEBH di centro O e raggio OC; altezza OD; Q punto medio di OD; S sul prolungamento di OQ con QS = QC; tronco CBGF del cono di vertice S",
     "fig. 53: solido ovale ADBE di asse AB; GH ⊥ AB in B; FG, HI tangenti in F e I con angoli FGB = BHI = 135°",
     "curva DNFG: NM ⊥ AB; GR ∥ tangente in N, R sull’asse prolungato; MN : GR = GR³ : 4BR×GB²"
    ]
   },
   "passi": [
    {
     "id": "L2-P34-Schol-p1",
     "la": "",
     "it": "Per esempio, se sulla base circolare CEBH, descritta con centro O e raggio OC, e con l’altezza OD, si deve costruire il tronco di cono CBGF che, fra tutti i tronchi costruiti con la stessa base e la stessa altezza e avanzanti verso D nel verso del loro asse, incontri la minima resistenza: dividi a metà l’altezza OD in Q e prolunga OQ fino a S, in modo che QS sia uguale a QC; e S sarà il vertice del cono di cui si cerca il tronco.",
     "en": "As if upon the circular base CEBH from the centre O, with the radius OC, and the altitude OD, one would construct a frustum CBGF of a cone, which should meet with less resistance than any other frustum constructed with the same base and altitude, and going forwards towards D in the direction of its axis: bisect the altitude OD in Q, and produce OQ to S, so that QS may be equal to QC, and S will be the vertex of the cone whose frustum is sought.",
     "dipende_da": [],
     "figura": {
      "mostra": [
       "base CEBH",
       "O",
       "OC",
       "OD",
       "Q",
       "S",
       "QS = QC",
       "tronco CBGF"
      ],
      "evidenzia": [
       "costruzione di S"
      ]
     },
     "nota": "Verifica numerica in N7."
    },
    {
     "id": "L2-P34-Schol-p2",
     "la": "",
     "it": "Di qui, per inciso, poiché l’angolo CSB è sempre acuto, ne consegue che, se il solido ADBE è generato dalla rivoluzione di una figura ellittica od ovale ADBE attorno all’asse AB, e la figura generatrice è toccata da tre rette FG, GH, HI nei punti F, B e I, con la condizione che GH sia perpendicolare all’asse nel punto di contatto B, e FG, HI formino con la stessa GH angoli FGB, BHI di 135 gradi, il solido generato dalla rivoluzione della figura ADFGHIE attorno allo stesso asse AB incontra una resistenza minore del solido precedente; purché entrambi avanzino nel verso del loro asse AB e l’estremità B di ciascuno vada avanti.",
     "en": "Whence, by the bye, since the angle CSB is always acute, it follows, that, if the solid ADBE be generated by the convolution of an elliptical or oval figure ADBE about its axis AB, and the generating figure be touched by three right lines FG, GH, HI, in the points F, B, and I, so that GH shall be perpendicular to the axis in the point of contact B, and FG, HI may be inclined to GH in the angles FGB, BHI of 135 degrees: the solid arising from the convolution of the figure ADFGHIE about the same axis AB will be less resisted than the former solid; if so be that both move forward in the direction of their axis AB, and that the extremity B of each go foremost.",
     "dipende_da": [],
     "figura": {
      "mostra": [
       "ovale ADBE",
       "asse AB",
       "FG",
       "GH ⊥ AB in B",
       "HI",
       "angoli di 135°"
      ],
      "evidenzia": [
       "la figura ADFGHIE resiste meno di ADBE"
      ]
     }
    },
    {
     "id": "L2-P34-Schol-p3",
     "la": "",
     "it": "E questa proposizione, ritengo, non sarà inutile nella costruzione delle navi.",
     "en": "Which Proposition I conceive may be of use in the building of ships.",
     "dipende_da": [],
     "figura": {
      "mostra": []
     }
    },
    {
     "id": "L2-P34-Schol-p4",
     "la": "",
     "it": "Che se la figura DNFG è una curva tale che, se da un suo punto qualsiasi N si abbassa sull’asse AB la perpendicolare NM, e dal punto dato G si conduce la retta GR parallela alla retta tangente alla figura in N, che tagli l’asse prolungato in R, MN sta a GR come GR³ sta a 4BR×GB², il solido descritto dalla rivoluzione di questa figura attorno all’asse AB, muovendosi da A verso B nel suddetto mezzo rado, incontrerà una resistenza minore di qualsiasi altro solido circolare descritto con la stessa lunghezza e la stessa larghezza.",
     "en": "If the figure DNFG be such a curve, that if, from any point thereof, as N, the perpendicular NM be let fall on the axis AB, and from the given point G there be drawn the right line GR parallel to a right line touching the figure in N, and cutting the axis produced in R, MN becomes to GR as GR3 to 4BR × GB2, the solid described by the revolution of this figure about its axis AB, moving in the before-mentioned rare medium from A towards B, will be less resisted than any other circular solid whatsoever, described of the same length and breadth.",
     "dipende_da": [],
     "figura": {
      "mostra": [
       "curva DNFG",
       "N",
       "NM ⊥ AB",
       "GR ∥ tangente in N",
       "R"
      ],
      "evidenzia": [
       "MN : GR = GR³ : 4BR×GB²"
      ]
     },
     "nota": "Trascrizione «GR cub. ad 4BR×GBq» = GR³ : 4BR×GB²; Motte omette «Quod»; senza dimostrazione nel testo (N8)."
    }
   ]
  },
  {
   "id": "L2-P35-Cor6",
   "tipo": "Corollarium",
   "titolo": "Prop. XXXV, Cor. 6 — moto e resistenza del globo rappresentati con l’iperbole",
   "copertura": [
    "II.S7.27"
   ],
   "fonti": {
    "la": "",
    "en": "Motte 1846, Section VII, Prop. XXXV, Cor. 6"
   },
   "enunciato": {
    "la": "",
    "it": "E il moto del globo, insieme con la sua resistenza, si può rappresentare così.",
    "en": "The motion of the globe and its resistance may be thus expounded."
   },
   "figura_base": {
    "punti": [
     "A",
     "B",
     "C",
     "D",
     "E",
     "F",
     "G",
     "H"
    ],
    "vincoli": [
     "AB = tempo in cui la resistenza iniziale, continuata uniformemente, toglierebbe tutto il moto",
     "AD ⊥ AB, BC ⊥ AB; BC = moto iniziale",
     "iperbole CF per C con asintoti AD, AB",
     "E sul prolungamento di AB; EF ⊥ AB, F sull’iperbole",
     "CBEG parallelogramma (rettangolo)",
     "H = AF ∩ BC"
    ]
   },
   "passi": [
    {
     "id": "L2-P35-Cor6-p1",
     "la": "",
     "it": "Sia AB il tempo in cui il globo, per la sua resistenza continuata uniformemente, può perdere tutto il suo moto.",
     "en": "Let AB be the time in which the globe may, by its resistance uniformly continued, lose its whole motion.",
     "dipende_da": [],
     "figura": {
      "mostra": [
       "segmento AB (tempo)"
      ]
     }
    },
    {
     "id": "L2-P35-Cor6-p2",
     "la": "",
     "it": "Su AB s’innalzino le perpendicolari AD, BC.",
     "en": "Erect AD, BC perpendicular to AB.",
     "dipende_da": [],
     "figura": {
      "mostra": [
       "AD",
       "BC"
      ]
     }
    },
    {
     "id": "L2-P35-Cor6-p3",
     "la": "",
     "it": "E sia BC quel moto totale, e per il punto C, con asintoti AD, AB, si descriva l’iperbole CF.",
     "en": "Let BC be that whole motion, and through the point C, the asymptotes being AD, AB, describe the hyperbola CF.",
     "dipende_da": [],
     "figura": {
      "mostra": [
       "iperbole CF",
       "asintoti AD, AB"
      ],
      "evidenzia": [
       "BC = moto iniziale"
      ]
     }
    },
    {
     "id": "L2-P35-Cor6-p4",
     "la": "",
     "it": "Si prolunghi AB fino a un punto qualsiasi E.",
     "en": "Produce AB to any point E.",
     "dipende_da": [],
     "figura": {
      "mostra": [
       "E"
      ]
     }
    },
    {
     "id": "L2-P35-Cor6-p5",
     "la": "",
     "it": "S’innalzi la perpendicolare EF, che incontri l’iperbole in F.",
     "en": "Erect the perpendicular EF meeting the hyperbola in F.",
     "dipende_da": [],
     "figura": {
      "mostra": [
       "EF",
       "F"
      ]
     }
    },
    {
     "id": "L2-P35-Cor6-p6",
     "la": "",
     "it": "Si completi il parallelogramma CBEG, e si conduca AF, che incontri BC in H.",
     "en": "Complete the parallelogram CBEG, and draw AF meeting BC in H.",
     "dipende_da": [],
     "figura": {
      "mostra": [
       "G",
       "parallelogramma CBEG",
       "AF",
       "H"
      ]
     }
    },
    {
     "id": "L2-P35-Cor6-p7",
     "la": "",
     "it": "E se il globo, in un tempo qualsiasi BE, con il suo moto iniziale BC continuato uniformemente, descrive in un mezzo non resistente lo spazio CBEG rappresentato dall’area del parallelogramma, lo stesso globo in un mezzo resistente descriverà lo spazio CBEF rappresentato dall’area dell’iperbole, e il suo moto alla fine di quel tempo sarà rappresentato dall’ordinata EF dell’iperbole, perduta la parte FG del suo moto.",
     "en": "Then if the globe in any time BE, with its first motion BC uniformly continued, describes in a non-resisting medium the space CBEG expounded by the area of the parallelogram, the same in a resisting medium will describe the space CBEF expounded by the area of the hyperbola; and its motion at the end of that time will be expounded by EF, the ordinate of the hyperbola, there being lost of its motion the part FG.",
     "dipende_da": [],
     "figura": {
      "mostra": [
       "area CBEG",
       "area CBEF"
      ],
      "evidenzia": [
       "spazio = area; moto finale = EF; perdita = FG"
      ]
     },
     "nota": "La trascrizione ha «hyperpoblæ» (refuso)."
    },
    {
     "id": "L2-P35-Cor6-p8",
     "la": "",
     "it": "E la sua resistenza alla fine dello stesso tempo sarà rappresentata dalla lunghezza BH, perduta la parte CH della resistenza.",
     "en": "And its resistance at the end of the same time will be expounded by the length BH, there being lost of its resistance the part CH.",
     "dipende_da": [],
     "figura": {
      "mostra": [
       "BH",
       "CH"
      ],
      "evidenzia": [
       "resistenza finale = BH"
      ]
     },
     "nota": "La trascrizione ha «exponentur» per «exponetur»."
    },
    {
     "id": "L2-P35-Cor6-p9",
     "la": "",
     "it": "Tutto ciò risulta dai Cor. 1 e 3 della Prop. V del Libro II.",
     "en": "All these things appear by Cor. 1 and 3, Prop. V., Book II.",
     "dipende_da": [
      "Libro II, Prop. V, Cor. 1",
      "Libro II, Prop. V, Cor. 3"
     ],
     "figura": {
      "mostra": []
     }
    }
   ]
  },
  {
   "id": "L2-P36",
   "tipo": "Propositio/Problema",
   "titolo": "Prop. XXXVI — efflusso dell’acqua da un vaso cilindrico (costruzione e Caso 1)",
   "copertura": [
    "II.S7.30",
    "II.S7.31",
    "II.S7.32",
    "II.S7.33",
    "II.S7.34",
    "II.S7.35"
   ],
   "fonti": {
    "la": "",
    "en": "Motte 1846, Section VII, Prop. XXXVI"
   },
   "enunciato": {
    "la": "",
    "it": "Determinare il moto dell’acqua che esce da un vaso cilindrico attraverso un foro praticato nel fondo.",
    "en": "To define the motion of water running out of a cylindrical vessel through a hole made at the bottom."
   },
   "figura_base": {
    "punti": [
     "A",
     "C",
     "D",
     "B",
     "E",
     "F",
     "G",
     "H",
     "P",
     "Q",
     "N",
     "M",
     "I",
     "K",
     "L",
     "V",
     "W",
     "S",
     "T",
     "Z"
    ],
    "vincoli": [
     "vaso cilindrico ACDB, AB bocca superiore, CD fondo orizzontale",
     "EF foro circolare nel mezzo del fondo, centro G; GH asse verticale",
     "cilindro di ghiaccio APQB sopra AB, stesso asse",
     "cateratta ABNFEM che si restringe da AB a EF",
     "I sopra H sull’asse, IH e HG in linea retta; KL orizzontale per I",
     "IG : IH = (cerchio AB : cerchio EF)²",
     "fig. 56: piano VW a distanza ≈ EF sopra EF, foro ST di centro Z, ST : EF ≈ 25 : 21"
    ]
   },
   "passi": [
    {
     "id": "L2-P36-p1",
     "la": "",
     "it": "Sia ACDB un vaso cilindrico, AB la sua bocca superiore, CD il fondo parallelo all’orizzonte, EF un foro circolare nel mezzo del fondo, G il centro del foro e GH l’asse del cilindro, perpendicolare all’orizzonte.",
     "en": "Let ACDB be a cylindrical vessel, AB the mouth of it, CD the bottom parallel to the horizon, EF a circular hole in the middle of the bottom, G the centre of the hole, and GH the axis of the cylinder perpendicular to the horizon.",
     "dipende_da": [],
     "figura": {
      "mostra": [
       "vaso ACDB",
       "AB",
       "CD",
       "foro EF",
       "G",
       "asse GH"
      ]
     },
     "nota": "Motte omette «superius» («the mouth of it»)."
    },
    {
     "id": "L2-P36-p2",
     "la": "",
     "it": "E immagina che un cilindro di ghiaccio APQB abbia la stessa larghezza della cavità del vaso e lo stesso asse, e discenda continuamente con moto uniforme, e che le sue parti, appena toccano la superficie AB, si sciolgano e, mutate in acqua, scendano per la loro gravità nel vaso e, cadendo, formino la cateratta, ossia colonna d’acqua, ABNFEM, e passino attraverso il foro EF e lo riempiano esattamente.",
     "en": "And suppose a cylinder of ice APQB to be of the same breadth with the cavity of the vessel, and to have the same axis, and to descend perpetually with an uniform motion, and that its parts, as soon as they touch the superficies AB, dissolve into water, and flow down by their weight into the vessel, and in their fall compose the cataract or column of water ABNFEM, passing through the hole EF, and filling up the same exactly.",
     "dipende_da": [],
     "figura": {
      "mostra": [
       "cilindro di ghiaccio APQB",
       "cateratta ABNFEM"
      ],
      "evidenzia": [
       "la cateratta riempie esattamente EF"
      ]
     },
     "nota": "Trascrizione: «ese» per «esse», «in quam conversas» per «in aquam conversas» (refusi probabili)."
    },
    {
     "id": "L2-P36-p3",
     "la": "",
     "it": "La velocità uniforme del ghiaccio che discende, come pure quella dell’acqua contigua nel cerchio AB, sia quella che l’acqua può acquistare cadendo e descrivendo nella sua caduta l’altezza IH; e IH e HG giacciano in linea retta, e per il punto I si conduca la retta KL parallela all’orizzonte, che incontri i lati del ghiaccio in K e L.",
     "en": "Let the uniform velocity of the descending ice and of the contiguous water in the circle AB be that which the water would acquire by falling through the space IH; and let IH and HG lie in the same right line; and through the point I let there be drawn the right line KL parallel to the horizon and meeting the ice on both the sides thereof in K and L.",
     "dipende_da": [],
     "figura": {
      "mostra": [
       "I",
       "IH",
       "retta KL",
       "K",
       "L"
      ],
      "evidenzia": [
       "v(AB) acquistata cadendo da IH"
      ]
     }
    },
    {
     "id": "L2-P36-p4",
     "la": "",
     "it": "E la velocità dell’acqua che esce attraverso il foro EF sarà quella che l’acqua può acquistare cadendo da I e descrivendo nella sua caduta l’altezza IG.",
     "en": "Then the velocity of the water running out at the hole EF will be the same that it would acquire by falling from I through the space IG.",
     "dipende_da": [],
     "figura": {
      "mostra": [
       "IG"
      ],
      "evidenzia": [
       "v(EF) acquistata cadendo da IG"
      ]
     }
    },
    {
     "id": "L2-P36-p5",
     "la": "",
     "it": "Perciò, per i teoremi di Galileo, IG starà a IH nel rapporto duplicato della velocità dell’acqua che esce attraverso il foro rispetto alla velocità dell’acqua nel cerchio AB, cioè nel rapporto duplicato del cerchio AB al cerchio EF; infatti questi cerchi stanno inversamente come le velocità delle acque che li attraversano riempiendoli esattamente, nello stesso tempo e in quantità uguale.",
     "en": "Therefore, by Galileo's Theorems, IG will be to IH in the duplicate ratio of the velocity of the water that runs out at the hole to the velocity of the water in the circle AB, that is, in the duplicate ratio of the circle AB to the circle EF; those circles being reciprocally as the velocities of the water which in the same time and in equal quantities passes severally through each of them, and completely fills them both.",
     "dipende_da": [
      "Galileo, teoremi sulla caduta dei gravi"
     ],
     "figura": {
      "mostra": [],
      "evidenzia": [
       "IG : IH = (AB : EF)²"
      ]
     }
    },
    {
     "id": "L2-P36-p6",
     "la": "",
     "it": "Qui si tratta della velocità dell’acqua verso l’orizzonte.",
     "en": "We are now considering the velocity with which the water tends to the plane of the horizon.",
     "dipende_da": [],
     "figura": {
      "mostra": []
     },
     "nota": "Motte: «tends to the plane of the horizon»."
    },
    {
     "id": "L2-P36-p7",
     "la": "",
     "it": "E il moto parallelo all’orizzonte con cui le parti dell’acqua che cade si avvicinano l’una all’altra, poiché non nasce dalla gravità né cambia il moto perpendicolare all’orizzonte che nasce dalla gravità, qui non si considera.",
     "en": "But the motion parallel to the same, by which the parts of the falling water approach to each other, is not here taken notice of; since it is neither produced by gravity, nor at all changes the motion perpendicular to the horizon which the gravity produces.",
     "dipende_da": [],
     "figura": {
      "mostra": []
     }
    },
    {
     "id": "L2-P36-p8",
     "la": "",
     "it": "Supponiamo, è vero, che le parti dell’acqua siano un poco coerenti e, per la loro coesione, durante la caduta si avvicinino l’una all’altra con moti paralleli all’orizzonte, così da formare una sola cateratta e non dividersi in più cateratte; ma il moto parallelo all’orizzonte che nasce da quella coesione qui non lo consideriamo.",
     "en": "We suppose, indeed, that the parts of the water cohere a little, that by their cohesion they may in falling approach to each other with motions parallel to the horizon in order to form one single cataract, and to prevent their being divided into several: but the motion parallel to the horizon arising from this cohesion does not come under our present consideration.",
     "dipende_da": [],
     "figura": {
      "mostra": []
     }
    },
    {
     "id": "L2-P36-p9",
     "la": "",
     "it": "Caso 1. Immagina ora che tutta la cavità del vaso, attorno all’acqua che cade ABNFEM, sia piena di ghiaccio, così che l’acqua passi attraverso il ghiaccio come attraverso un imbuto.",
     "en": "CASE 1. Conceive now the whole cavity in the vessel, which encompasses the falling water ABNFEM, to be full of ice, so that the water may pass through the ice as through a funnel.",
     "dipende_da": [],
     "figura": {
      "mostra": [
       "ghiaccio attorno alla cateratta (AMEC, BNFD)"
      ],
      "evidenzia": [
       "la cateratta come in un imbuto"
      ]
     }
    },
    {
     "id": "L2-P36-p10",
     "la": "",
     "it": "E se l’acqua sfiora appena il ghiaccio senza toccarlo, oppure, ciò che è lo stesso, se lo tocca ma, per la sua estrema levigatezza, scivola sul ghiaccio liberissimamente e senza alcuna resistenza, essa scenderà attraverso il foro EF con la stessa velocità di prima, e tutto il peso della colonna d’acqua ABNFEM sarà impiegato, come prima, a generarne il deflusso, e il fondo del vaso sosterrà il peso del ghiaccio che circonda la colonna.",
     "en": "Then if the water pass very near to the ice only, without touching it; or, which is the same thing, if by reason of the perfect smoothness of the surface of the ice, the water, though touching it, glides over it with the utmost freedom, and without the least resistance; the water will run through the hole EF with the same velocity as before, and the whole weight of the column of water ABNFEM will be all taken up as before in forcing out the water, and the bottom of the vessel will sustain the weight of the ice encompassing that column.",
     "dipende_da": [],
     "figura": {
      "mostra": [],
      "evidenzia": [
       "peso della cateratta → deflusso; peso del ghiaccio → fondo"
      ]
     }
    },
    {
     "id": "L2-P36-p11",
     "la": "",
     "it": "Si sciolga ora il ghiaccio nel vaso; e l’efflusso dell’acqua, quanto alla velocità, resterà lo stesso di prima.",
     "en": "Let now the ice in the vessel dissolve into water; yet will the efflux of the water remain, as to its velocity, the same as before.",
     "dipende_da": [],
     "figura": {
      "mostra": [
       "ghiaccio sciolto"
      ]
     }
    },
    {
     "id": "L2-P36-p12",
     "la": "",
     "it": "Non sarà minore, perché il ghiaccio, sciolto in acqua, tenderà a discendere; non sarà maggiore, perché il ghiaccio, sciolto in acqua, non può discendere se non impedendo la discesa di altra acqua uguale alla propria discesa.",
     "en": "It will not be less, because the ice now dissolved will endeavour to descend; it will not be greater, because the ice, now become water, cannot descend without hindering the descent of other water equal to its own descent.",
     "dipende_da": [],
     "figura": {
      "mostra": []
     },
     "nota": "Trascrizione: «qui glacies in quam resoluta» per «quia glacies in aquam resoluta» (refusi probabili)."
    },
    {
     "id": "L2-P36-p13",
     "la": "",
     "it": "La stessa forza deve generare la stessa velocità dell’acqua che esce.",
     "en": "The same force ought always to generate the same velocity in the effluent water.",
     "dipende_da": [],
     "figura": {
      "mostra": []
     },
     "nota": "Motte aggiunge «always»."
    },
    {
     "id": "L2-P36-p14",
     "la": "",
     "it": "Ma il foro nel fondo del vaso, a causa dei moti obliqui delle particelle dell’acqua che esce, deve essere un poco più grande di prima.",
     "en": "But the hole at the bottom of the vessel, by reason of the oblique motions of the particles of the effluent water, must be a little greater than before.",
     "dipende_da": [],
     "figura": {
      "mostra": [
       "foro reale (più grande)"
      ]
     }
    },
    {
     "id": "L2-P36-p15",
     "la": "",
     "it": "Infatti le particelle dell’acqua ora non passano tutte perpendicolarmente attraverso il foro; ma, confluendo da ogni parte dalle pareti del vaso e convergendo nel foro, lo attraversano con moti obliqui; e, piegando il loro corso verso il basso, si uniscono nella vena dell’acqua che sgorga, la quale è un poco più sottile poco sotto il foro che nel foro stesso, poiché il suo diametro sta al diametro del foro come 5 sta a 6, ossia come 5½ sta a 6½, con ottima approssimazione, se ho misurato bene i diametri.",
     "en": "For now the particles of the water do not all of them pass through the hole perpendicularly, but, flowing down on all parts from the sides of the vessel, and converging towards the hole, pass through it with oblique motions; and in tending downwards meet in a stream whose diameter is a little smaller below the hole than at the hole itself; its diameter being to the diameter of the hole as 5 to 6, or as [SVG 736] to [SVG 727], very nearly, if I took the measures of those diameters right.",
     "dipende_da": [],
     "figura": {
      "mostra": [
       "linee di flusso convergenti",
       "vena contratta"
      ],
      "evidenzia": [
       "diametro vena : diametro foro = 5 : 6 ≈ 5½ : 6½"
      ]
     },
     "nota": "«512 ad 612» = 5½ : 6½; Motte [SVG 736], [SVG 727]."
    },
    {
     "id": "L2-P36-p16",
     "la": "",
     "it": "Avevo preparato appunto una lamina piana sottilissima, forata nel mezzo, con un foro circolare di diametro pari a cinque ottavi di pollice.",
     "en": "I procured a very thin flat plate, having a hole pierced in the middle, the diameter of the circular hole being [SVG 737] parts of an inch.",
     "dipende_da": [],
     "figura": {
      "mostra": [
       "lamina forata, diametro 5/8 di pollice"
      ]
     },
     "nota": "Motte stampa la frazione come [SVG 737]."
    },
    {
     "id": "L2-P36-p17",
     "la": "",
     "it": "E perché la vena dell’acqua che sgorga non fosse accelerata nella caduta e, per l’accelerazione, resa più stretta, fissai questa lamina non al fondo ma alla parete del vaso, in modo che la vena uscisse secondo una linea parallela all’orizzonte.",
     "en": "And that the stream of running waters might not be accelerated in falling, and by that acceleration become narrower, I fixed this plate not to the bottom, but to the side of the vessel, so as to make the water go out in the direction of a line parallel to the horizon.",
     "dipende_da": [],
     "figura": {
      "mostra": [
       "lamina sulla parete",
       "vena orizzontale"
      ]
     }
    },
    {
     "id": "L2-P36-p18",
     "la": "",
     "it": "Poi, quando il vaso fu pieno d’acqua, aprii il foro perché l’acqua uscisse; e il diametro della vena, misurato con la massima accuratezza alla distanza di circa mezzo pollice dal foro, risultò di ventuno quarantesimi di pollice.",
     "en": "Then, when the vessel was full of water, I opened the hole to let it run out; and the diameter of the stream, measured with great accuracy at the distance of about half an inch from the hole, was [SVG 738] of an inch.",
     "dipende_da": [],
     "figura": {
      "mostra": [
       "diametro vena 21/40 di pollice a ½ pollice dal foro"
      ]
     },
     "nota": "Motte [SVG 738]."
    },
    {
     "id": "L2-P36-p19",
     "la": "",
     "it": "Il diametro di questo foro circolare stava dunque al diametro della vena come 25 sta a 21, con ottima approssimazione.",
     "en": "Therefore the diameter of this circular hole was to the diameter of the stream very nearly as 25 to 21.",
     "dipende_da": [],
     "figura": {
      "mostra": [],
      "evidenzia": [
       "25 : 21"
      ]
     }
    },
    {
     "id": "L2-P36-p20",
     "la": "",
     "it": "L’acqua dunque, passando attraverso il foro, converge da ogni parte e, dopo essere uscita dal vaso, si fa più sottile convergendo e, per l’assottigliamento, è accelerata finché non è giunta alla distanza di mezzo pollice dal foro; e a quella distanza diventa più sottile e più veloce che nel foro stesso nel rapporto di 25×25 a 21×21, ossia di 17 a 12 con ottima approssimazione, cioè circa nel rapporto subduplicato di due a uno.",
     "en": "So that the water in passing through the hole converges on all sides, and, after it has run out of the vessel, becomes smaller by converging in that manner, and by becoming smaller is accelerated till it comes to the distance of half an inch from the hole, and at that distance flows in a smaller stream and with greater celerity than in the hole itself, and this in the ratio of 25 × 25 to 21 × 21, or 17 to 12, very nearly; that is, in about the subduplicate ratio of 2 to 1.",
     "dipende_da": [],
     "figura": {
      "mostra": [],
      "evidenzia": [
       "velocità: 625 : 441 ≈ 17 : 12 ≈ √2 : 1"
      ]
     }
    },
    {
     "id": "L2-P36-p21",
     "la": "",
     "it": "Dagli esperimenti risulta invece che la quantità d’acqua che in un tempo dato esce da un foro circolare praticato nel fondo di un vaso è quella che, con la velocità suddetta, dovrebbe uscire nello stesso tempo non attraverso quel foro, ma attraverso un foro circolare il cui diametro sta al diametro di quel foro come 21 sta a 25.",
     "en": "Now it is certain from experiments, that the quantity of water running out in a given time through a circular hole made in the bottom of a vessel is equal to the quantity, which, flowing with the aforesaid velocity, would run out in the same time through another circular hole, whose diameter is to the diameter of the former as 21 to 25.",
     "dipende_da": [],
     "figura": {
      "mostra": [],
      "evidenzia": [
       "portata = sezione della vena × velocità piena"
      ]
     },
     "nota": "Trascrizione: «diammeter»."
    },
    {
     "id": "L2-P36-p22",
     "la": "",
     "it": "Perciò quell’acqua che esce ha, nel foro stesso, una velocità verso il basso pari, con ottima approssimazione, a quella che un grave può acquistare cadendo e descrivendo nella sua caduta metà dell’altezza dell’acqua ferma nel vaso.",
     "en": "And therefore that running water in passing through the hole itself has a velocity downwards equal to that which a heavy body would acquire in falling through half the height of the stagnant water in the vessel, nearly.",
     "dipende_da": [],
     "figura": {
      "mostra": [],
      "evidenzia": [
       "v(foro)² ≈ ½ · 2g·altezza"
      ]
     }
    },
    {
     "id": "L2-P36-p23",
     "la": "",
     "it": "Ma, dopo essere uscita dal vaso, è accelerata convergendo finché non è giunta a una distanza dal foro quasi uguale al diametro del foro, e ha acquistato una velocità maggiore circa nel rapporto subduplicato di due a uno; quella, appunto, che un grave può acquistare, con ottima approssimazione, cadendo e descrivendo nella sua caduta l’intera altezza dell’acqua ferma nel vaso.",
     "en": "But, then, after it has run out, it is still accelerated by converging, till it arrives at a distance from the hole that is nearly equal to its diameter, and acquires a velocity greater than the other in about the subduplicate ratio of 2 to 1; which velocity a heavy body would nearly acquire by falling through the whole height of the stagnant water in the vessel.",
     "dipende_da": [],
     "figura": {
      "mostra": [],
      "evidenzia": [
       "v(vena)² ≈ 2g·altezza"
      ]
     }
    },
    {
     "id": "L2-P36-p24",
     "la": "",
     "it": "In ciò che segue, dunque, il diametro della vena sia rappresentato da quel foro più piccolo che abbiamo chiamato EF.",
     "en": "Therefore in what follows let the diameter of the stream be represented by that lesser hole which we called EF.",
     "dipende_da": [],
     "figura": {
      "mostra": [
       "EF = sezione della vena"
      ]
     }
    },
    {
     "id": "L2-P36-p25",
     "la": "",
     "it": "E s’immagini condotto, parallelo al piano del foro EF, un altro piano superiore VW, a una distanza circa uguale al diametro del foro, e forato da un foro più grande ST; attraverso il quale cada appunto una vena che riempia esattamente il foro inferiore EF, e il cui diametro stia perciò al diametro del foro inferiore circa come 25 sta a 21.",
     "en": "And imagine another plane VW above the hole EF, and parallel to the plane thereof, to be placed at a distance equal to the diameter of the same hole, and to be pierced through with a greater hole ST, of such a magnitude that a stream which will exactly fill the lower hole EF may pass through it; the diameter of which hole will therefore be to the diameter of the lower hole as 25 to 21, nearly.",
     "dipende_da": [],
     "figura": {
      "mostra": [
       "piano VW",
       "foro ST"
      ],
      "evidenzia": [
       "ST : EF = 25 : 21; distanza VW–EF ≈ diametro EF"
      ]
     }
    },
    {
     "id": "L2-P36-p26",
     "la": "",
     "it": "Così infatti la vena passerà perpendicolarmente attraverso il foro inferiore; e la quantità d’acqua che esce, in proporzione alla grandezza di questo foro, sarà, con ottima approssimazione, quella che la soluzione del problema richiede.",
     "en": "By this means the water will run perpendicularly out at the lower hole; and the quantity of the water running out will be, according to the magnitude of this last hole, the same, very nearly, which the solution of the Problem requires.",
     "dipende_da": [],
     "figura": {
      "mostra": []
     }
    },
    {
     "id": "L2-P36-p27",
     "la": "",
     "it": "Lo spazio racchiuso fra i due piani e la vena che cade si può considerare come il fondo del vaso.",
     "en": "The space included between the two planes and the falling stream may be considered as the bottom of the vessel.",
     "dipende_da": [],
     "figura": {
      "mostra": [
       "spazio fra i piani come fondo"
      ]
     }
    },
    {
     "id": "L2-P36-p28",
     "la": "",
     "it": "Ma perché la soluzione del problema sia più semplice e più matematica, conviene prendere come fondo del vaso il solo piano inferiore, e immaginare che l’acqua che scendeva attraverso il ghiaccio come attraverso un imbuto, e usciva dal vaso attraverso il foro EF praticato nel piano inferiore, conservi continuamente il suo moto, e il ghiaccio la sua quiete.",
     "en": "But, to make the solution more simple and mathematical, it is better to take the lower plane alone for the bottom of the vessel, and to suppose that the water which flowed through the ice as through a funnel, and ran out of the vessel through the hole EF made in the lower plane, preserves its motion continually, and that the ice continues at rest.",
     "dipende_da": [],
     "figura": {
      "mostra": [
       "solo piano inferiore come fondo"
      ]
     }
    },
    {
     "id": "L2-P36-p29",
     "la": "",
     "it": "In ciò che segue, dunque, sia ST il diametro del foro circolare, descritto con centro Z, attraverso il quale la cateratta esce dal vaso quando tutta l’acqua nel vaso è fluida.",
     "en": "Therefore in what follows let ST be the diameter of a circular hole described from the centre Z, and let the stream run out of the vessel through that hole, when the water in the vessel is all fluid.",
     "dipende_da": [],
     "figura": {
      "mostra": [
       "Z centro di ST"
      ]
     }
    },
    {
     "id": "L2-P36-p30",
     "la": "",
     "it": "E sia EF il diametro del foro che la cateratta, cadendo, attraversa riempiendolo esattamente, sia che l’acqua esca dal vaso attraverso quel foro superiore ST, sia che cada attraverso il mezzo del ghiaccio nel vaso come attraverso un imbuto.",
     "en": "And let EF be the diameter of the hole, which the stream, in falling through, exactly fills up, whether the water runs out of the vessel by that upper hole ST, or flows through the middle of the ice in the vessel, as through a funnel.",
     "dipende_da": [],
     "figura": {
      "mostra": []
     }
    },
    {
     "id": "L2-P36-p31",
     "la": "",
     "it": "E il diametro del foro superiore ST stia al diametro di quello inferiore EF circa come 25 sta a 21, e la distanza perpendicolare fra i piani dei fori sia uguale al diametro del foro minore EF.",
     "en": "And let the diameter of the upper hole ST be to the diameter of the lower EF as about 25 to 21, and let the perpendicular distance between the planes of the holes be equal to the diameter of the lesser hole EF.",
     "dipende_da": [],
     "figura": {
      "mostra": [],
      "evidenzia": [
       "ST : EF = 25 : 21"
      ]
     }
    },
    {
     "id": "L2-P36-p32",
     "la": "",
     "it": "E la velocità dell’acqua che esce dal vaso attraverso il foro ST sarà, nel foro stesso, verso il basso, quella che un corpo può acquistare cadendo da metà dell’altezza IZ; la velocità di entrambe le cateratte che cadono sarà invece, nel foro EF, quella che un corpo acquisterà cadendo dall’intera altezza IG.",
     "en": "Then the velocity of the water downwards, in running out of the vessel through the hole ST, will be in that hole the same that a body may acquire by falling from half the height IZ; and the velocity of both the falling streams will be in the hole EF, the same which a body would acquire by falling from the whole height IG.",
     "dipende_da": [],
     "figura": {
      "mostra": [
       "IZ",
       "IG"
      ],
      "evidenzia": [
       "v(ST) da ½IZ; v(EF) da IG"
      ]
     }
    }
   ]
  },
  {
   "id": "L2-P36-Cor3",
   "tipo": "Corollarium",
   "titolo": "Prop. XXXVI, Cor. 3 — parte del peso impiegata nel deflusso",
   "copertura": [
    "II.S7.43"
   ],
   "fonti": {
    "la": "",
    "en": "Motte 1846, Section VII, Prop. XXXVI, Cor. 3"
   },
   "enunciato": {
    "la": "",
    "it": "Il peso di tutta l’acqua nel vaso ABDC sta alla parte del peso che è impiegata nel deflusso dell’acqua come la somma dei cerchi AB ed EF sta al doppio del cerchio EF.",
    "en": "The weight of all the water in the vessel ABDC is to that part of the weight which is employed in forcing out the water as the sum of the circles AB and EF to twice the circle EF."
   },
   "figura_base": {
    "punti": [
     "A",
     "B",
     "C",
     "D",
     "E",
     "F",
     "G",
     "H",
     "I",
     "O",
     "N",
     "M"
    ],
    "vincoli": [
     "come nella Prop. XXXVI: I, H, O, G sull’asse in quest’ordine",
     "IO media proporzionale fra IH e IG",
     "cerchio EF : cerchio AB = IO : IG = √(IH : IG)"
    ]
   },
   "passi": [
    {
     "id": "L2-P36-Cor3-p1",
     "la": "",
     "it": "Sia infatti IO media proporzionale fra IH e IG; l’acqua che esce attraverso il foro EF, nel tempo in cui una goccia, cadendo da I, potrebbe descrivere l’altezza IG, sarà uguale a un cilindro la cui base è il cerchio EF e l’altezza è 2IG, cioè a un cilindro la cui base è il cerchio AB e l’altezza è 2IO, perché il cerchio EF sta al cerchio AB nel rapporto subduplicato dell’altezza IH all’altezza IG, cioè nel rapporto semplice della media proporzionale IO all’altezza IG; e nel tempo in cui una goccia, cadendo da I, può descrivere l’altezza IH, l’acqua che esce sarà uguale a un cilindro la cui base è il cerchio AB e l’altezza è 2IH; e nel tempo in cui una goccia, cadendo da I per H fino a G, descrive la differenza delle altezze HG, l’acqua che esce, cioè tutta l’acqua nel solido ABNFEM, sarà uguale alla differenza dei cilindri, cioè a un cilindro la cui base è AB e l’altezza è 2HO.",
     "en": "For let IO be a mean proportional between IH and IG, and the water running out at the hole EF will, in the time that a drop falling from I would describe the altitude IG, become equal to a cylinder whose base is the circle EF and its altitude 2IG, that is, to a cylinder whose base is the circle AB, and whose altitude is 2IO. For the circle EF is to the circle AB in the subduplicate ratio of the altitude IH to the altitude IG; that is, in the simple ratio of the mean proportional IO to the altitude IG. Moreover, in the time that a drop falling from I can describe the altitude IH, the water that runs out will have become equal to a cylinder whose base is the circle AB, and its altitude 2IH; and in the time that a drop falling from I through H to G describes HG, the difference of the altitudes, the effluent water, that is, the water contained within the solid ABNFEM, will be equal to the difference of the cylinders, that is, to a cylinder whose base is AB, and its altitude 2HO.",
     "dipende_da": [],
     "figura": {
      "mostra": [
       "O tra H e G",
       "cilindri 2IG (base EF), 2IO e 2IH (base AB)"
      ],
      "evidenzia": [
       "volume uscito nel tempo di caduta da I a G = cilindro AB × 2IO"
      ]
     },
     "nota": "Trascrizione: «edrediens» per «egrediens». Motte spezza il periodo in tre frasi."
    },
    {
     "id": "L2-P36-Cor3-p2",
     "la": "",
     "it": "E perciò tutta l’acqua nel vaso ABDC sta a tutta l’acqua che cade nel solido ABNFEM come HG sta a 2HO, cioè come HO+OG sta a 2HO, ossia come IH+IO sta a 2IH.",
     "en": "And therefore all the water contained in the vessel ABDC is to the whole falling water contained in the said solid ABNFEM as HG to 2HO, that is, as HO + OG to 2HO, or IH + IO to 2IH.",
     "dipende_da": [],
     "figura": {
      "mostra": [],
      "evidenzia": [
       "HG : 2HO = (IH+IO) : 2IH"
      ]
     }
    },
    {
     "id": "L2-P36-Cor3-p3",
     "la": "",
     "it": "Ma il peso di tutta l’acqua nel solido ABNFEM è impiegato nel deflusso dell’acqua; e perciò il peso di tutta l’acqua nel vaso sta alla parte del peso che è impiegata nel deflusso dell’acqua come IH+IO sta a 2IH, e quindi come la somma dei cerchi EF e AB sta al doppio del cerchio EF.",
     "en": "But the weight of all the water in the solid ABNFEM is employed in forcing out the water; and therefore the weight of all the water in the vessel is to that part of the weight that is employed in forcing out the water as IH + IO to 2IH, and therefore as the sum of the circles EF and AB to twice the circle EF.",
     "dipende_da": [
      "Prop. XXXVI, Caso 1"
     ],
     "figura": {
      "mostra": [],
      "evidenzia": [
       "(IH+IO) : 2IH = (AB+EF) : 2EF"
      ]
     },
     "nota": "Il rimando al Caso 1 è implicito (il peso della cateratta va nel deflusso). Trascrizione: «dplum» per «duplum»."
    }
   ]
  },
  {
   "id": "L2-P36-Cor7",
   "tipo": "Corollarium",
   "titolo": "Prop. XXXVI, Cor. 7 — il cerchietto PQ sostiene più di un terzo del cilindro",
   "copertura": [
    "II.S7.47"
   ],
   "fonti": {
    "la": "",
    "en": "Motte 1846, Section VII, Prop. XXXVI, Cor. 7"
   },
   "enunciato": {
    "la": "",
    "it": "Se nel mezzo del foro EF si colloca un cerchietto PQ, descritto con centro G e parallelo all’orizzonte, il peso dell’acqua che quel cerchietto sostiene è maggiore del peso della terza parte di un cilindro d’acqua la cui base è quel cerchietto e l’altezza è GH.",
    "en": "If in the middle of the hole EF there be placed the little circle PQ described about the centre G, and parallel to the horizon, the weight of water which that little circle sustains is greater than the weight of a third part of a cylinder of water whose base is that little circle and its height GH."
   },
   "figura_base": {
    "punti": [
     "A",
     "B",
     "C",
     "D",
     "E",
     "F",
     "G",
     "H",
     "M",
     "N",
     "P",
     "Q"
    ],
    "vincoli": [
     "cerchietto PQ orizzontale di centro G nel foro EF",
     "cateratta ABNFEM di asse GH",
     "ghiaccio AMEC, BNFD attorno alla cateratta, convesso verso di essa",
     "colonna congelata PHQ di vertice H e altezza GH, convessa verso la cateratta"
    ]
   },
   "passi": [
    {
     "id": "L2-P36-Cor7-p1",
     "la": "",
     "it": "Sia infatti ABNFEM la cateratta, ossia colonna d’acqua che cade, avente asse GH come sopra, e s’immagini congelata tutta l’acqua nel vaso, sia attorno alla cateratta sia sopra il cerchietto, la cui fluidità non è richiesta per la discesa più pronta e più rapida dell’acqua.",
     "en": "For let ABNFEM be the cataract or column of falling water whose axis is GH, as above, and let all the water, whose fluidity is not requisite for the ready and quick descent of the water, be supposed to be congealed, as well round about the cataract, as above the little circle.",
     "dipende_da": [],
     "figura": {
      "mostra": [
       "cateratta ABNFEM",
       "ghiaccio laterale",
       "ghiaccio sopra PQ"
      ]
     },
     "nota": "Motte riordina la frase."
    },
    {
     "id": "L2-P36-Cor7-p2",
     "la": "",
     "it": "E sia PHQ la colonna d’acqua congelata sopra il cerchietto, con vertice H e altezza GH.",
     "en": "And let PHQ be the column of water congealed above the little circle, whose vertex is H, and its altitude GH.",
     "dipende_da": [],
     "figura": {
      "mostra": [
       "colonna PHQ"
      ]
     }
    },
    {
     "id": "L2-P36-Cor7-p3",
     "la": "",
     "it": "E immagina che questa cateratta cada con tutto il suo peso, e non gravi su PHQ né la prema, ma le scorra accanto liberamente e senza attrito, se non forse proprio al vertice del ghiaccio, dove la cateratta, all’inizio stesso della caduta, cominci a essere cava.",
     "en": "And suppose this cataract to fall with its whole weight downwards, and not in the least to lie against or to press PHQ, but to glide freely by it without any friction, unless, perhaps, just at the very vertex of the ice, where the cataract at the beginning of its fall may tend to a concave figure.",
     "dipende_da": [],
     "figura": {
      "mostra": [],
      "evidenzia": [
       "scorrimento senza attrito"
      ]
     }
    },
    {
     "id": "L2-P36-Cor7-p4",
     "la": "",
     "it": "E come l’acqua congelata attorno alla cateratta, AMEC, BNFD, è convessa nella superficie interna AME, BNF verso la cateratta che cade, così anche questa colonna PHQ sarà convessa verso la cateratta, e perciò maggiore del cono la cui base è quel cerchietto PQ e l’altezza GH, cioè maggiore della terza parte del cilindro descritto con la stessa base e la stessa altezza.",
     "en": "And as the congealed water AMEC, BNFD, lying round the cataract, is convex in its internal superficies AME, BNF, towards the falling cataract, so this column PHQ will be convex towards the cataract also, and will therefore be greater than a cone whose base is that little circle PQ and its altitude GH; that is, greater than a third part of a cylinder described with the same base and altitude.",
     "dipende_da": [],
     "figura": {
      "mostra": [
       "superfici AME, BNF",
       "cono di base PQ e altezza GH"
      ],
      "evidenzia": [
       "colonna convessa > cono = ⅓ cilindro"
      ]
     }
    },
    {
     "id": "L2-P36-Cor7-p5",
     "la": "",
     "it": "Ora, quel cerchietto sostiene il peso di questa colonna, cioè un peso maggiore del peso del cono, ossia della terza parte di quel cilindro.",
     "en": "Now that little circle sustains the weight of this column, that is, a weight greater than the weight of the cone, or a third part of the cylinder.",
     "dipende_da": [],
     "figura": {
      "mostra": []
     }
    }
   ]
  },
  {
   "id": "L2-P36-Cor8",
   "tipo": "Corollarium",
   "titolo": "Prop. XXXVI, Cor. 8 — per PQ molto piccolo, meno di due terzi del cilindro",
   "copertura": [
    "II.S7.48"
   ],
   "fonti": {
    "la": "",
    "en": "Motte 1846, Section VII, Prop. XXXVI, Cor. 8"
   },
   "enunciato": {
    "la": "",
    "it": "Il peso dell’acqua che un cerchietto PQ molto piccolo sostiene sembra minore del peso dei due terzi di un cilindro d’acqua la cui base è quel cerchietto e l’altezza è HG.",
    "en": "The weight of water which the circle PQ, when very small, sustains, seems to be less than the weight of two thirds of a cylinder of water whose base is that little circle, and its altitude HG."
   },
   "figura_base": {
    "punti": [
     "P",
     "Q",
     "G",
     "H"
    ],
    "vincoli": [
     "mezzo sferoide di base PQ e semiasse GH (= ⅔ del cilindro)",
     "colonna PHQ con angolo acuto alla base e vertice cuspidato",
     "PQ → 0: angolo PHQ → 0"
    ]
   },
   "passi": [
    {
     "id": "L2-P36-Cor8-p1",
     "la": "",
     "it": "Infatti, ferme restando le ipotesi già fatte, s’immagini descritta [la metà di] uno sferoide la cui base è quel cerchietto e il cui semiasse, ossia altezza, è HG.",
     "en": "For, things standing as above supposed, imagine the half of a spheroid described whose base is that little circle, and its semi-axis or altitude HG.",
     "dipende_da": [],
     "figura": {
      "mostra": [
       "mezzo sferoide di base PQ, semiasse HG"
      ]
     },
     "nota": "La trascrizione ha soltanto «sphæroidis»: manca probabilmente «dimidium» (Motte «the half of a spheroid»)."
    },
    {
     "id": "L2-P36-Cor8-p2",
     "la": "",
     "it": "E questa figura sarà uguale ai due terzi di quel cilindro e comprenderà la colonna d’acqua congelata PHQ il cui peso quel cerchietto sostiene.",
     "en": "This figure will be equal to two thirds of that cylinder, and will comprehend within it the column of congealed water PHQ, the weight of which is sustained by that little circle.",
     "dipende_da": [],
     "figura": {
      "mostra": [
       "colonna PHQ dentro il mezzo sferoide"
      ],
      "evidenzia": [
       "mezzo sferoide = ⅔ cilindro"
      ]
     },
     "nota": "«Est hæc figura … erit»: probabile refuso per «Et hæc figura»."
    },
    {
     "id": "L2-P36-Cor8-p3",
     "la": "",
     "it": "Infatti, perché il moto dell’acqua sia il più diretto possibile, la superficie esterna di quella colonna incontrerà la base PQ sotto un angolo alquanto acuto, perché l’acqua, cadendo, è continuamente accelerata e, per l’accelerazione, si fa più sottile; e poiché quell’angolo è minore di un retto, questa colonna, nelle sue parti inferiori, giacerà dentro il mezzo sferoide.",
     "en": "For though the motion of the water tends directly downwards, the external superficies of that column must yet meet the base PQ in an angle somewhat acute, because the water in its fall is perpetually accelerated, and by reason of that acceleration become narrower. Therefore, since that angle is less than a right one, this column in the lower parts thereof will lie within the hemi-spheroid.",
     "dipende_da": [],
     "figura": {
      "mostra": [
       "angolo acuto della colonna sulla base PQ"
      ]
     },
     "nota": "Motte legge «ut» come concessivo («though»); qui è inteso come finale (A.4)."
    },
    {
     "id": "L2-P36-Cor8-p4",
     "la": "",
     "it": "La stessa colonna sarà poi, in alto, acuta, ossia cuspidata, perché il moto orizzontale dell’acqua al vertice dello sferoide non sia infinitamente più veloce del suo moto verso l’orizzonte.",
     "en": "In the upper parts also it will be acute or pointed; because to make it otherwise, the horizontal motion of the water must be at the vertex infinitely more swift than its motion towards the horizon.",
     "dipende_da": [],
     "figura": {
      "mostra": [
       "vertice cuspidato H"
      ]
     }
    },
    {
     "id": "L2-P36-Cor8-p5",
     "la": "",
     "it": "E quanto più piccolo è il cerchietto PQ, tanto più acuto sarà il vertice della colonna; e, diminuito all’infinito il cerchietto, l’angolo PHQ diminuirà all’infinito, e perciò la colonna giacerà dentro il mezzo sferoide.",
     "en": "And the less this circle PQ is, the more acute will the vertex of this column be; and the circle being diminished in infinitum, the angle PHQ will be diminished in infinitum, and therefore the column will lie within the hemi-spheroid.",
     "dipende_da": [],
     "figura": {
      "mostra": [
       "PQ che diminuisce",
       "angolo PHQ"
      ]
     }
    },
    {
     "id": "L2-P36-Cor8-p6",
     "la": "",
     "it": "Quella colonna è dunque minore del mezzo sferoide, ossia dei due terzi del cilindro la cui base è quel cerchietto e l’altezza GH.",
     "en": "Therefore that column is less than that hemi-spheroid, or than two-third parts of the cylinder whose base is that little circle, and its altitude GH.",
     "dipende_da": [],
     "figura": {
      "mostra": [],
      "evidenzia": [
       "colonna < ⅔ cilindro"
      ]
     }
    },
    {
     "id": "L2-P36-Cor8-p7",
     "la": "",
     "it": "Ora, il cerchietto sostiene una forza dell’acqua uguale al peso di questa colonna, poiché il peso dell’acqua circostante è impiegato nel suo deflusso.",
     "en": "Now the little circle sustains a force of water equal to the weight of this column, the weight of the ambient water being employed in causing its efflux out at the hole.",
     "dipende_da": [],
     "figura": {
      "mostra": []
     }
    }
   ]
  },
  {
   "id": "L2-P37",
   "tipo": "Propositio/Theorema",
   "titolo": "Prop. XXXVII — resistenza di un cilindro in un fluido compresso, infinito e non elastico",
   "copertura": [
    "II.S7.53",
    "II.S7.54",
    "II.S7.55",
    "II.S7.56",
    "II.S7.57",
    "II.S7.58",
    "II.S7.59"
   ],
   "fonti": {
    "la": "",
    "en": "Motte 1846, Section VII, Prop. XXXVII"
   },
   "enunciato": {
    "la": "",
    "it": "La resistenza di un cilindro che avanza uniformemente nel senso della sua lunghezza in un fluido compresso, infinito e non elastico, resistenza che nasce dalla grandezza della sezione trasversale, sta alla forza con cui tutto il suo moto potrebbe essere tolto o generato mentre descrive il quadruplo della sua lunghezza, come la densità del mezzo sta alla densità del cilindro, con ottima approssimazione.",
    "en": "If a cylinder move uniformly forward in a compressed, infinite, and non-elastic fluid, in the direction of its length, the resistance arising from the magnitude of its transverse section is to the force by which its whole motion may be destroyed or generated, in the time that it moves four times its length, as the density of the medium to the density of the cylinder, nearly."
   },
   "figura_base": {
    "punti": [
     "A",
     "B",
     "C",
     "D",
     "E",
     "F",
     "T",
     "S",
     "P",
     "Q",
     "K",
     "I",
     "H",
     "G"
    ],
    "vincoli": [
     "vaso ABDC con il fondo CD a contatto con l’acqua ferma",
     "canale cilindrico verticale EFTS sotto CD",
     "cerchietto PQ orizzontale nel canale, coassiale",
     "K sul prolungamento di CA: AK : CK = ((cerchio EF − cerchio PQ) : cerchio AB)²",
     "velocità nell’anello: da KC = IG"
    ]
   },
   "passi": [
    {
     "id": "L2-P37-p1",
     "la": "",
     "it": "Infatti, se il vaso ABDC tocca con il suo fondo CD la superficie dell’acqua ferma, e l’acqua esce da questo vaso nell’acqua ferma attraverso il canale cilindrico EFTS, perpendicolare all’orizzonte, e si colloca un cerchietto PQ parallelo all’orizzonte in un punto qualsiasi in mezzo al canale, e si prolunga CA fino a K in modo che AK stia a CK nel rapporto duplicato di quello che l’eccesso dell’orifizio EF del canale sul cerchietto PQ ha con il cerchio AB, è manifesto (per i Casi 5 e 6 e il Cor. 1 della Prop. XXXVI) che la velocità dell’acqua che passa attraverso lo spazio anulare fra il cerchietto e le pareti del vaso sarà quella che l’acqua può acquistare cadendo e descrivendo nella sua caduta l’altezza KC, ossia IG.",
     "en": "For let the vessel ABDC touch the surface of stagnant water with its bottom CD, and let the water run out of this vessel into the stagnant water through the cylindric canal EFTS perpendicular to the horizon; and let the little circle PQ be placed parallel to the horizon any where in the middle of the canal; and produce CA to K, so that AK may be to CK in the duplicate of the ratio, which the excess of the orifice of the canal EF above the little circle PQ bears to the circle AB. Then it is manifest (by Case 5, Case 6, and Cor. 1, Prop. XXXVI) that the velocity of the water passing through the annular space between the little circle and the sides of the vessel will be the very same which the water would acquire by falling, and in its fall describing the altitude KC or IG.",
     "dipende_da": [
      "Prop. XXXVI, Caso 5",
      "Prop. XXXVI, Caso 6",
      "Prop. XXXVI, Cor. 1"
     ],
     "figura": {
      "mostra": [
       "vaso ABDC",
       "acqua ferma sotto CD",
       "canale EFTS",
       "cerchietto PQ",
       "K"
      ],
      "evidenzia": [
       "AK : CK = ((EF − PQ) : AB)²"
      ]
     },
     "nota": "Trascrizione: «superificiem»."
    },
    {
     "id": "L2-P37-p2",
     "la": "",
     "it": "E (per il Cor. 10 della Prop. XXXVI), se la larghezza del vaso è infinita, così che il segmentino HI svanisca e le altezze IG, HG si eguaglino, la forza dell’acqua che scende sul cerchietto starà al peso di un cilindro la cui base è quel cerchietto e l’altezza è ½IG come EF² sta a EF²−½PQ², con ottima approssimazione.",
     "en": "And (by Cor. 10, Prop. XXXVI) if the breadth of the vessel be infinite, so that the lineola HI may vanish, and the altitudes IG, HG become equal; the force of the water that flows down and presses upon the circle will be to the weight of a cylinder whose base is that little circle, and the altitude [SVG 742], as [SVG 740] to [SVG 741], very nearly.",
     "dipende_da": [
      "Prop. XXXVI, Cor. 10"
     ],
     "figura": {
      "mostra": [
       "HI → 0"
      ],
      "evidenzia": [
       "forza su PQ : cilindro(½IG) = EF² : (EF² − ½PQ²)"
      ]
     },
     "nota": "«12IG», «EFq−12PQq» = ½IG, EF² − ½PQ²; Motte [SVG 742], [SVG 740], [SVG 741]."
    },
    {
     "id": "L2-P37-p3",
     "la": "",
     "it": "Infatti la forza dell’acqua che scende con moto uniforme per tutto il canale sarà la stessa sul cerchietto PQ, in qualunque parte del canale sia collocato.",
     "en": "For the force of the water flowing downward uniformly through the whole canal will be the same upon the little circle PQ in whatsoever part of the canal it be placed.",
     "dipende_da": [],
     "figura": {
      "mostra": [
       "PQ in posizioni diverse del canale"
      ]
     }
    },
    {
     "id": "L2-P37-p4",
     "la": "",
     "it": "Si chiudano ora gli orifizi EF, ST del canale, e il cerchietto salga nel fluido compresso da ogni parte e, con la sua salita, costringa l’acqua che sta sopra a discendere attraverso lo spazio anulare fra il cerchietto e le pareti del canale: la velocità del cerchietto che sale starà alla velocità dell’acqua che discende come la differenza dei cerchi EF e PQ sta al cerchio PQ, e la velocità del cerchietto che sale starà alla somma delle velocità, cioè alla velocità relativa dell’acqua che discende, con cui essa scorre accanto al cerchietto che sale, come la differenza dei cerchi EF e PQ sta al cerchio EF, ossia come EF²−PQ² sta a EF².",
     "en": "Let now the orifices of the canal EF, ST be closed, and let the little circle ascend in the fluid compressed on every side, and by its ascent let it oblige the water that lies above it to descend through the annular space between the little circle and the sides of the canal. Then will the velocity of the ascending little circle be to the velocity of the descending water as the difference of the circles EF and PQ is to the circle PQ; and the velocity of the ascending little circle will be to the sum of the velocities, that is, to the relative velocity of the descending water with which it passes by the little circle in its ascent, as the difference of the circles EF and PQ to the circle [SVG 743], or as [SVG 744] to [SVG 740].",
     "dipende_da": [],
     "figura": {
      "mostra": [
       "orifizi chiusi",
       "PQ in salita",
       "acqua in discesa nell’anello"
      ],
      "evidenzia": [
       "u : w = (EF − PQ) : PQ;  u : (u + w) = (EF² − PQ²) : EF²"
      ]
     },
     "nota": "Motte «to the circle [SVG 743]»: il latino dice «ad circulum EF»; SVG 743 = EF (verificato)."
    },
    {
     "id": "L2-P37-p5",
     "la": "",
     "it": "Sia quella velocità relativa uguale alla velocità con cui, come si è mostrato sopra, l’acqua passa attraverso lo stesso spazio anulare mentre il cerchietto resta frattanto immobile, cioè alla velocità che l’acqua può acquistare cadendo e descrivendo nella sua caduta l’altezza IG: e la forza dell’acqua sul cerchietto che sale sarà la stessa di prima (per il Cor. V delle leggi), cioè la resistenza del cerchietto che sale starà al peso di un cilindro d’acqua la cui base è quel cerchietto e l’altezza è ½IG come EF² sta a EF²−½PQ², con ottima approssimazione.",
     "en": "Let that relative velocity be equal to the velocity with which it was shewn above that the water would pass through the annular space, if the circle were to remain unmoved, that is, to the velocity which the water would acquire by falling, and in its fall describing the altitude IG; and the force of the water upon the ascending circle will be the same as before (by Cor. 5, of the Laws of Motion); that is, the resistance of the ascending little circle will be to the weight of a cylinder of water whose base is that little circle, and its altitude [SVG 742], as [SVG 740] to [SVG 741], nearly.",
     "dipende_da": [
      "Leggi, Cor. V"
     ],
     "figura": {
      "mostra": [],
      "evidenzia": [
       "stessa velocità relativa → stessa forza"
      ]
     }
    },
    {
     "id": "L2-P37-p6",
     "la": "",
     "it": "La velocità del cerchietto starà invece alla velocità che l’acqua acquista cadendo e descrivendo nella sua caduta l’altezza IG come EF²−PQ² sta a EF².",
     "en": "But the velocity of the little circle will be to the velocity which the water acquires by falling, and in its fall describing the altitude IG, as [SVG 744] to [SVG 740].",
     "dipende_da": [],
     "figura": {
      "mostra": []
     }
    },
    {
     "id": "L2-P37-p7",
     "la": "",
     "it": "Si aumenti all’infinito l’ampiezza del canale: e quei rapporti fra EF²−PQ² ed EF², e fra EF² ed EF²−½PQ², si avvicineranno alla fine a rapporti di uguaglianza.",
     "en": "Let the breadth of the canal be increased in infinitum; and the ratios between [SVG 744] and [SVG 740], and between [SVG 740] and [SVG 741], will become at last ratios of equality.",
     "dipende_da": [],
     "figura": {
      "mostra": [
       "EF → ∞"
      ],
      "evidenzia": [
       "rapporti → 1"
      ]
     },
     "nota": "Trascrizione: «Efq» per «EFq»."
    },
    {
     "id": "L2-P37-p8",
     "la": "",
     "it": "E perciò la velocità del cerchietto sarà ora quella che l’acqua può acquistare cadendo e descrivendo nella sua caduta l’altezza IG, e la sua resistenza diventerà invece uguale al peso di un cilindro la cui base è quel cerchietto e la cui altezza è la metà dell’altezza IG, dalla quale il cilindro deve cadere per acquistare la velocità del cerchietto che sale; e con questa velocità il cilindro, nel tempo della caduta, descriverà il quadruplo della sua lunghezza.",
     "en": "And therefore the velocity of the little circle will now be the same which the water would acquire in falling, and in its fall describing the altitude IG; and the resistance will become equal to the weight of a cylinder whose base is that little circle, and its altitude half the altitude IG, from which the cylinder must fall to acquire the velocity of the ascending circle; and with this velocity the cylinder in the time of its fall will describe four times its length.",
     "dipende_da": [],
     "figura": {
      "mostra": [
       "cilindro d’acqua di altezza ½IG"
      ],
      "evidenzia": [
       "resistenza = peso del cilindro ½IG; nel tempo di caduta percorre 4 × ½IG"
      ]
     }
    },
    {
     "id": "L2-P37-p9",
     "la": "",
     "it": "Ma la resistenza di un cilindro che avanza con questa velocità nel senso della sua lunghezza è la stessa della resistenza del cerchietto (per il Lemma IV), e perciò è uguale, con ottima approssimazione, alla forza con cui il suo moto può essere generato mentre descrive il quadruplo della sua lunghezza.",
     "en": "But the resistance of the cylinder moving forward with this velocity in the direction of its length is the same with the resistance of the little circle (by Lem. IV), and is therefore nearly equal to the force by which its motion may be generated while it describes four times its length.",
     "dipende_da": [
      "Lemma IV"
     ],
     "figura": {
      "mostra": [
       "cilindro solido al posto del cerchietto"
      ]
     }
    },
    {
     "id": "L2-P37-p10",
     "la": "",
     "it": "Se la lunghezza del cilindro si aumenta o si diminuisce, il suo moto, come pure il tempo in cui descrive il quadruplo della sua lunghezza, sarà aumentato o diminuito nello stesso rapporto; e perciò quella forza con cui il moto aumentato o diminuito potrebbe essere generato o tolto, in un tempo ugualmente aumentato o diminuito, non cambierà; e quindi è ancora uguale alla resistenza del cilindro, perché anche questa resta immutata, per il Lemma IV.",
     "en": "If the length of the cylinder be augmented or diminished, its motion, and the time in which it describes four times its length, will be augmented or diminished in the same ratio, and therefore the force by which the motion so increased or diminished, may be destroyed or generated, will continue the same; because the time is increased or diminished in the same proportion; and therefore that force remains still equal to the resistance of the cylinder, because (by Lem. IV) that resistance will also remain the same.",
     "dipende_da": [
      "Lemma IV"
     ],
     "figura": {
      "mostra": [
       "lunghezza variabile"
      ]
     },
     "nota": "Motte aggiunge una causale («because the time is increased…») che nel latino è un ablativo assoluto."
    },
    {
     "id": "L2-P37-p11",
     "la": "",
     "it": "Se la densità del cilindro si aumenta o si diminuisce, il suo moto, come pure la forza con cui il moto può essere generato o tolto nello stesso tempo, sarà aumentato o diminuito nello stesso rapporto.",
     "en": "If the density of the cylinder be augmented or diminished, its motion, and the force by which its motion may be generated or destroyed in the same time, will be augmented or diminished in the same ratio.",
     "dipende_da": [],
     "figura": {
      "mostra": [
       "densità variabile"
      ]
     }
    },
    {
     "id": "L2-P37-p12",
     "la": "",
     "it": "La resistenza di un cilindro qualsiasi starà dunque alla forza con cui tutto il suo moto potrebbe essere generato o tolto mentre descrive il quadruplo della sua lunghezza come la densità del mezzo sta alla densità del cilindro, con ottima approssimazione. C.V.D.",
     "en": "Therefore the resistance of any cylinder whatsoever will be to the force by which its whole motion may be generated or destroyed, in the time during which it moves four times its length, as the density of the medium to the density of the cylinder, nearly. Q.E.D.",
     "dipende_da": [],
     "figura": {
      "mostra": [],
      "evidenzia": [
       "R : F(4L) = densità mezzo : densità cilindro"
      ]
     }
    }
   ]
  },
  {
   "id": "L2-P37-Schol",
   "tipo": "Scholium",
   "titolo": "Scolio alla Prop. XXXVII — testa e coda parabolica del cilindro",
   "copertura": [
    "II.S7.64"
   ],
   "fonti": {
    "la": "",
    "en": "Motte 1846, Section VII, Scholium alla Prop. XXXVII"
   },
   "enunciato": {
    "la": "",
    "it": "In questa proposizione abbiamo ricercato la resistenza che nasce dalla sola grandezza della sezione trasversale del cilindro, trascurata la parte della resistenza che può nascere dall’obliquità dei moti.",
    "en": "In this proposition we have investigated that resistance alone which arises from the magnitude of the transverse section of the cylinder, neglecting that part of the same which may arise from the obliquity of the motions."
   },
   "figura_base": {
    "punti": [
     "A",
     "B",
     "C",
     "D",
     "E",
     "F",
     "H",
     "G"
    ],
    "vincoli": [
     "ABCD rettangolo (sezione assiale del cilindro); asse del solido EF",
     "AE, BE archi parabolici di asse AB, lato retto λ con λ : HG = HG : ½AB",
     "CF, DF archi parabolici di asse CD, lato retto 4λ",
     "solido EACFDB per rivoluzione attorno a EF; avanza verso E"
    ]
   },
   "passi": [
    {
     "id": "L2-P37-Schol-p1",
     "la": "",
     "it": "Infatti, come nel primo caso della Prop. XXXVI l’obliquità dei moti con cui le parti dell’acqua nel vaso convergevano da ogni parte nel foro EF impediva l’efflusso di quell’acqua attraverso il foro, così in questa proposizione l’obliquità dei moti con cui le parti dell’acqua, premute dall’estremità anteriore del cilindro, cedono alla pressione e divergono da ogni parte, ritarda il loro passaggio attraverso i luoghi attorno a quell’estremità che precede, verso le parti posteriori del cilindro, e fa sì che il fluido sia messo in moto a distanza maggiore, e accresce la resistenza, e ciò quasi nello stesso rapporto in cui diminuiva l’efflusso dell’acqua dal vaso, cioè circa nel rapporto duplicato di 25 a 21.",
     "en": "For as, in Case 1, of Prop. XXXVI., the obliquity of the motions with which the parts of the water in the vessel converged on every side to the hole EF hindered the efflux of the water through the hole, so, in this Proposition, the obliquity of the motions, with which the parts of the water, pressed by the antecedent extremity of the cylinder, yield to the pressure, and diverge on all sides, retards their passage through the places that lie round that antecedent extremity, toward the hinder parts of the cylinder, and causes the fluid to be moved to a greater distance; which increases the resistance, and that in the same ratio almost in which it diminished the efflux of the water out of the vessel, that is, in the duplicate ratio of 25 to 21, nearly.",
     "dipende_da": [
      "Prop. XXXVI, Caso 1"
     ],
     "figura": {
      "mostra": [
       "flusso divergente davanti al cilindro"
      ],
      "evidenzia": [
       "fattore (25 : 21)² ≈ 1,42"
      ]
     },
     "nota": "Trascrizione: «ciciter» per «circiter»; «cedunt pressione» per «pressioni» (probabile)."
    },
    {
     "id": "L2-P37-Schol-p2",
     "la": "",
     "it": "E come, nel primo caso di quella proposizione, abbiamo fatto sì che le parti dell’acqua passassero perpendicolarmente e nella massima quantità attraverso il foro EF, supponendo che tutta l’acqua nel vaso che era stata congelata attorno alla cateratta, e il cui moto era obliquo e inutile, restasse senza moto, così in questa proposizione, perché l’obliquità dei moti sia tolta e le parti dell’acqua, cedendo con il moto più diretto e più breve, offrano al cilindro il passaggio più facile, e resti soltanto la resistenza che nasce dalla grandezza della sezione trasversale, la quale non si può diminuire se non diminuendo il diametro del cilindro, bisogna concepire che le parti del fluido i cui moti sono obliqui e inutili e creano resistenza siano in quiete fra loro a entrambe le estremità del cilindro, e siano coerenti e unite al cilindro.",
     "en": "And as, in Case 1, of that Proposition, we made the parts of the water pass through the hole EF perpendicularly and in the greatest plenty, by supposing all the water in the vessel lying round the cataract to be frozen, and that part of the water whose motion was oblique and useless to remain without motion, so in this Proposition, that the obliquity of the motions may be taken away, and the parts of the water may give the freest passage to the cylinder, by yielding to it with the most direct and quick motion possible, so that only so much resistance may remain as arises from the magnitude of the transverse section, and which is incapable of diminution, unless by diminishing the diameter of the cylinder; we must conceive those parts of the fluid whose motions are oblique and useless, and produce resistance, to be at rest among themselves at both extremities of the cylinder, and there to cohere, and be joined to the cylinder.",
     "dipende_da": [
      "Prop. XXXVI, Caso 1"
     ],
     "figura": {
      "mostra": [
       "fluido in quiete alle estremità"
      ]
     },
     "nota": "Trascrizione: «fine motu» per «sine motu» (s lunga)."
    },
    {
     "id": "L2-P37-Schol-p3",
     "la": "",
     "it": "Sia ABCD un rettangolo, e siano AE e BE due archi parabolici descritti con asse AB e con un lato retto che stia allo spazio HG, che il cilindro deve descrivere cadendo mentre acquista la sua velocità, come HG sta a ½AB.",
     "en": "Let ABCD be a rectangle, and let AE and BE be two parabolic arcs, described with the axis AB, and with a latus rectum that is to the space HG, which must be described by the cylinder in falling, in order to acquire the velocity with which it moves, as HG to [SVG 128].",
     "dipende_da": [],
     "figura": {
      "mostra": [
       "rettangolo ABCD",
       "archi AE, BE"
      ],
      "evidenzia": [
       "lato retto : HG = HG : ½AB"
      ]
     },
     "nota": "«12AB» = ½AB; Motte [SVG 128] = ½AB (verificato)."
    },
    {
     "id": "L2-P37-Schol-p4",
     "la": "",
     "it": "Siano anche CF e DF altri due archi parabolici, descritti con asse CD e con un lato retto quadruplo del lato retto precedente; e per rivoluzione della figura attorno all’asse EF si generi un solido la cui parte media ABDC sia il cilindro di cui trattiamo, e le parti estreme ABE e CDF contengano le parti del fluido in quiete fra loro e consolidate in due corpi rigidi, che aderiscano al cilindro da una parte e dall’altra come testa e coda.",
     "en": "Let CF and DF be two other parabolic arcs described with the axis CD, and a latus rectum quadruple of the former; and by the convolution of the figure about the axis EF let there be generated a solid, whose middle part ABDC is the cylinder we are here speaking of, and whose extreme parts ABE and CDF contain the parts of the fluid at rest among themselves, and concreted into two hard bodies, adhering to the cylinder at each end like a head and tail.",
     "dipende_da": [],
     "figura": {
      "mostra": [
       "archi CF, DF",
       "asse EF",
       "solido di rivoluzione",
       "testa ABE",
       "coda CDF"
      ],
      "evidenzia": [
       "lato retto della coda = 4 × lato retto della testa"
      ]
     }
    },
    {
     "id": "L2-P37-Schol-p5",
     "la": "",
     "it": "E la resistenza del solido EACFDB, che avanza nel senso della lunghezza del suo asse FE verso la parte di E, sarà, con ottima approssimazione, quella che abbiamo descritto in questa proposizione, cioè quella che ha, rispetto alla forza con cui tutto il moto del cilindro potrebbe essere tolto o generato mentre, con quel moto continuato uniformemente, si descrive la lunghezza 4AC, il rapporto che la densità del fluido ha con la densità del cilindro, con ottima approssimazione.",
     "en": "Then if this solid EACFDB move in the direction of the length of its axis FE toward the parts beyond E, the resistance will be the same which we have here determined in this Proposition, nearly; that is, it will have the same ratio to the force with which the whole motion of the cylinder may be destroyed or generated, in the time that it is describing the length 4AC with that motion uniformly continued, as the density of the fluid has to the density of the cylinder, nearly.",
     "dipende_da": [],
     "figura": {
      "mostra": [
       "solido EACFDB in moto verso E"
      ],
      "evidenzia": [
       "R : F(4AC) = densità fluido : densità cilindro"
      ]
     },
     "nota": "Trascrizione: «ad vim totus cylindri motus» (manca probabilmente «qua»)."
    },
    {
     "id": "L2-P37-Schol-p6",
     "la": "",
     "it": "E la resistenza non può essere minore di questa forza oltre il rapporto di 2 a 3 [cioè non può scendere sotto i due terzi di essa], per il Cor. 7 della Prop. XXXVI.",
     "en": "And (by Cor. 7, Prop. XXXVI) the resistance must be to this force in the ratio of 2 to 3, at the least.",
     "dipende_da": [
      "Prop. XXXVI, Cor. 7"
     ],
     "figura": {
      "mostra": [],
      "evidenzia": [
       "R ≥ ⅔ F"
      ]
     }
    }
   ]
  }
 ]
}
```
