> **Copia pubblica.** In questa versione i campi `"la"` della Parte B sono vuoti: le frasi latine vengono dalla trascrizione del Newton Project, che non si ridistribuisce. Il latino del 1726 si legge su newtonproject.ox.ac.uk.

# Isaac Newton
# Principi matematici della filosofia naturale

## Fascicolo 25b — Libro III: la figura della Luna, la precessione degli equinozi e i lemmi sulle comete

**Nuova traduzione italiana di lavoro dal latino del 1726, confrontata con l’inglese di Andrew Motte nell’edizione del 1846.**

Versione 0.1 — 8 novembre 2026. Preparata con Claude (Anthropic) per Massimo Bosetti.

### Stato e perimetro

Questo fascicolo è la **seconda parte** del gruppo G6 del Libro III (*De mundi systemate*, Propp. XXXIV–XL). La prima parte, con le Propp. XXXIV–XXXVII e lo Scolio della Prop. XXXV, è nel **Fascicolo 25a**; il seguito del Libro III (Prop. XLI, la cometa del 1680) è nel Fascicolo 26a. Questo fascicolo traduce integralmente, da «PROPOSITIO XXXVIII.» alla fine del gruppo:

- la **Prop. XXXVIII** (figura della Luna) con il suo corollario;
- i **Lemmi I–III** e l’**Ipotesi II**, che preparano il calcolo della precessione;
- la **Prop. XXXIX** (precessione degli equinozi) e il capoverso di passaggio alle comete;
- il **Lemma IV** (le comete sono più alte della Luna) con i suoi tre corollari;
- la **Prop. XL** (le comete si muovono in sezioni coniche) con quattro corollari;
- i **Lemmi V–XI** (interpolazione, luogo intermedio di una cometa, costruzioni sulla parabola), con il corollario e lo **Scolio del Lemma VIII**.

È una traduzione di lavoro, non un’edizione critica validata.

Gli identificatori **III.G6.44–III.G6.102** proseguono la serie del Fascicolo 25a (III.G6.01–III.G6.43); numerati in origine da 101, sono stati rinumerati dal coordinatore. Tutti i rimandi a serie sono scritti per esteso con il prefisso completo. I titoli tematici tra parentesi sono aggiunte editoriali; i numeri romani delle proposizioni, dei problemi, dei teoremi, dei lemmi e dell’ipotesi, e i numeri dei casi e dei corollari, appartengono al testo originale. Il lungo capoverso iniziale della dimostrazione del Lemma IV è diviso in tre identificatori (III.G6.65–III.G6.67) nei punti in cui il testo passa dalla descrizione qualitativa alla prima e alla seconda figura. Le integrazioni del curatore sono tra parentesi quadre. Le note poste dopo la traduzione non fanno parte del testo di Newton.

In coda al fascicolo c’è la **Parte B**, con i dati strutturati per le pagine interattive: 19 unità (Prop. XXXVIII; Lemmi I–III; Ipotesi II; Prop. XXXIX; Lemma IV; Prop. XL e i suoi Cor. 1, 3 e 4; Lemmi V–XI e lo Scolio del Lemma VIII).

### Fonti effettivamente consultate

1. **Latino di riferimento.** Isaac Newton, *Philosophiæ Naturalis Principia Mathematica*, terza edizione, Londra, 1726, Libro III, **pp. 470–491** (la Prop. XXXVIII comincia a p. 470, prima del marcatore ‹471›; il gruppo finisce a p. 491, prima del marcatore ‹492›). Trascrizione normalizzata del Newton Project, documento **NATP00303**, estratta in testo semplice senza correzioni: `fonti/latino-1726/latino-1726-L3-P34-40.md`, dalla riga 118 alla fine. Le figure sono segnalate nella trascrizione solo come [FIG], senza numero, e non sono disponibili.
2. **Inglese di confronto.** *Newton’s Principia*, traduzione di Andrew Motte, New York, Daniel Adee, 1846, Libro III, Propp. XXXVIII–XL e Lemmi I–XI (Project Gutenberg n. 76404): `fonti/motte-1846/motte-1846-L3-P34-40.md`, dalla riga 658 alla fine. L’estratto non ha marcatori di pagina: le pagine Motte sono indicate come «sezione corrispondente». Le formule stampate come immagini (`[SVG 1012]`, `[SVG 1091]`–`[SVG 1165]`) sono state lette sul LaTeX raccolto in `fonti/motte-1846/svg_tex.tsv`; l’EPUB non è disponibile in questa sessione, quindi le immagini non sono state viste.
3. **Istruzioni** del Libro III (`ISTRUZIONI-TRADUTTORE.md`), **addendum del Libro II** e **brief comune**; **Fascicoli 3, 5 e 20** come modelli di formato.
4. **Fascicoli già tradotti, per i rimandi:** Fascicolo 5 (Libro I, Prop. IV e Cor. 6 e 9), Fascicolo 6 (Libro I, Propp. XIII e XVI con i Cor. 6 e 7), Fascicolo 10 (Libro I, Prop. LXVI, Cor. 16). Per i rimandi interni al Libro III ho controllato il latino degli altri gruppi: `latino-1726-L3-P01-14.md` (Propp. VIII, XII, XIII), `-P15-19.md` (Propp. XVII e XIX), `-P21-33.md` (Prop. XXX, figura alle pp. 437–438) e la parte iniziale del file del gruppo G6 (Prop. XXXVII, Cor. 3 e 4, per i valori 4,4815, 39,788 e 100 : 365).

Non ho consultato né riprodotto traduzioni moderne. Non ho potuto vedere la stampa del 1726 né le figure originali: le relazioni geometriche sono ricostruite dalle sole lettere del testo e controllate con figure di prova costruite al calcolatore (`tmp/25b/verifica.py`).

### Criteri di traduzione

- Il testo guida è il latino; l’inglese di Motte serve a controllare le interpretazioni ed è annotato quando aggiunge, omette o si discosta.
- Si applicano il **glossario comune** del brief, il **glossario del Libro II** e il **glossario del Libro III** con i termini fissati dal coordinatore: *Sol, Luna, Terra* «Sole, Luna, Terra» e i nomi dei pianeti con la maiuscola anche dove il latino ha la minuscola; *præcessio æquinoctiorum* «precessione degli equinozi»; *nodi* «nodi»; *quadraturæ* «quadrature»; *perigæum* «perigeo»; *perihelium* «perielio»; *oppositio* «opposizione»; *parallaxis* «parallasse»; *cometa*, *cauda*, *caput*, *coma*, *nucleus*, *atmosphæra*, *vapor* «cometa», «coda», «testa», «chioma», «nucleo», «atmosfera», «vapore»; *orbis magnus* «orbe magno»; *orbis* (orbita) «orbita»; *sphærois* «sferoide»; *axis*, *æquator*, *poli*, *annulus* «asse», «equatore», «poli», «anello»; *ecliptica* «eclittica»; *diameter apparens* «diametro apparente»; *semidiameter* «semidiametro»; *micrometrum* «micrometro»; *stellæ fixæ* «stelle fisse»; *æther* «etere»; *dies sidereus* «giorno siderale»; *annus sidereus* «anno siderale»; *motus medius* e *mediocris distantia* «moto medio», «distanza media»; *longitudo / latitudo* «longitudine / latitudine»; *gradus*, *minutum primum / secundum* «grado», «primo / secondo»; *milliare* «miglio»; *pes* «piede»; *gravitas acceleratrix* «gravità acceleratrice»; *pondus* «peso»; *in antecedentia* «in antecedenza»; *ratio duplicata / subduplicata / sesquiplicata* «rapporto duplicato / subduplicato / sesquiplicato»; *ratio quadruplicata* «rapporto quadruplicato»; *conjunctim* «considerati congiuntamente»; *reciproce* «inversamente»; *ducere in* «moltiplicare per»; *applicare ad* «dividere per»; *quamproxime* «con ottima approssimazione»; *umbilicus* «fuoco»; *latus rectum* «lato retto»; *ordinatim applicata* «ordinata»; *positione datus* «dato di posizione»; *conatus* «tendenza»; *nisi quatenus* «se non in quanto»; *Hypothesis* «Ipotesi»; Q.E.D. «C.V.D.», Q.E.I. «C.V.T.», Q.E.F. «C.V.F.».
- *motus*, quando indica la grandezza (Lemma III e Prop. XXXIX: il «moto» della Terra, dell’anello, del globo, del cilindro), è reso **«quantità di moto»**, secondo il glossario comune; quando indica lo spostamento angolare dei nodi o dei punti equinoziali resta **«moto»**. La distinzione rende visibile un punto del ragionamento di Newton (nota N4).
- I segni zodiacali restano come simboli. La trascrizione scrive **γ** al posto del segno dell’Ariete (♈) nel Lemma IV; nella traduzione si scrive ♈ (§ A.7).
- I minuti e i secondi d’arco sono resi «primi» e «secondi», con i simboli ′ ″; le suddivisioni sessagesimali ulteriori della Prop. XXXIX (‴, iv, v: «terzi», «quarti», «quinti») sono conservate con i simboli del testo.
- Le abbreviazioni «FCq», «ACqq», «CXcub», «ACqc» sono scritte FC², AC⁴, CX³, AC⁵. I numeri misti e le frazioni appiattiti dalla trascrizione («8⁤35», «23⁤12», «43⁢ACq») sono resi 8 3/5, 23 1/2, 4/3 AC²; i coefficienti di Newton nel Lemma V sono resi ½p, ⅓q, ¼r, ⅕s. Le espressioni che nella stampa portano un vinculum (*NM×MC+mC* per NM per la somma MC + mC) sono rese con le parentesi, che qui sostituiscono il segno tipografico dell’epoca e non introducono formule moderne. Ogni lettura è dichiarata nel § A.7.
- Gli enunciati latini all’infinito (Lemma IV, Prop. XL) sono resi con l’indicativo; gli enunciati dei problemi (*Invenire…*, *Ducere…*) con l’infinito.
- I nomi latinizzati sono resi nella forma moderna (Flamsteed, Hevelius, Cysat, Keplero), con la forma latina nell’apparato.
- Nessuna formula moderna entra nel testo tradotto.

---

## Traduzione italiana

### Proposizione XXXVIII. Problema XIX (la figura della Luna)

**[III.G6.44]** **Trovare la figura del corpo della Luna.**

**[III.G6.45]** Se il corpo lunare fosse fluido come il nostro mare, la forza della Terra nel sollevare quel fluido nelle parti sia più vicine sia più lontane starebbe alla forza della Luna, con cui il nostro mare si innalza nelle parti sia sottostanti alla Luna sia opposte alla Luna, come la gravità acceleratrice della Luna verso la Terra sta alla gravità acceleratrice della Terra verso la Luna e il diametro della Luna sta al diametro della Terra, considerati congiuntamente; cioè come 39,788 sta a 1 e 100 sta a 365, considerati congiuntamente, ossia come 1081 sta a 100. Perciò, poiché il nostro mare è innalzato dalla forza della Luna fino a 8 3/5 piedi, il fluido lunare dovrebbe essere innalzato dalla forza della Terra fino a 93 piedi. E per questa causa la figura della Luna sarebbe uno sferoide il cui diametro massimo, prolungato, passerebbe per il centro della Terra e supererebbe i diametri perpendicolari con un eccesso di 186 piedi. La Luna, dunque, tende ad assumere una tale figura, e dovette assumerla fin dall’inizio. C.V.T.

**[III.G6.46]** *Cor.* Di qui avviene appunto che la stessa faccia della Luna sia sempre rivolta verso la Terra. In un’altra posizione, infatti, il corpo lunare non può stare in quiete, ma tornerà sempre a questa posizione oscillando. Tuttavia le oscillazioni, per la piccolezza delle forze che le producono, sarebbero lentissime: tanto che quella faccia, che dovrebbe guardare sempre la Terra, può guardare l’altro fuoco dell’orbita lunare (per la ragione addotta nella Prop. XVII), senza esserne subito ritratta e rivolta verso la Terra.

### Lemma I (le particelle dell’anello equatoriale e quelle raccolte in A)

**[III.G6.47]** **Se APEp rappresenta la Terra, di densità uniforme, delineata con il centro C, i poli P, p e l’equatore AE; e se con centro C e raggio CP s’intende descritta la sfera Pape; e sia QR il piano su cui insiste perpendicolarmente la retta condotta dal centro del Sole al centro della Terra; e le singole particelle di tutta la Terra esterna PapAPepE, che è più alta della sfera ora descritta, tendano ad allontanarsi dal piano QR da una parte e dall’altra, e la tendenza di ciascuna particella sia come la sua distanza dal piano: dico, in primo luogo, che la forza e l’efficacia totale di tutte le particelle situate nel cerchio dell’equatore AE, disposte fuori del globo uniformemente per tutto il giro a modo di anello, nel far ruotare la Terra intorno al suo centro, sta alla forza e all’efficacia totale di altrettante particelle poste nel punto A dell’equatore, che dista massimamente dal piano QR, nel muovere la Terra intorno al suo centro con un simile moto circolare, come uno sta a due. E quel moto circolare si compirà intorno a un asse che giace nella sezione comune dell’equatore e del piano QR.**

**[III.G6.48]** Infatti, con centro K e diametro IL, si descriva il semicerchio INLK. Si immagini la semicirconferenza INL divisa in innumerevoli parti uguali, e dalle singole parti N si abbassino sul diametro IL i seni NM. La somma dei quadrati di tutti i seni NM sarà uguale alla somma dei quadrati dei seni KM, ed entrambe le somme insieme saranno uguali alla somma dei quadrati di altrettanti semidiametri KN; e perciò la somma dei quadrati di tutti gli NM sarà la metà della somma dei quadrati di altrettanti semidiametri KN.

**[III.G6.49]** Ora si divida il perimetro del cerchio AE in altrettante particelle uguali, e da ciascuna di esse, F, si abbassi sul piano QR la perpendicolare FG, come anche dal punto A la perpendicolare AH. La forza con cui la particella F si allontana dal piano QR sarà come quella perpendicolare FG, per ipotesi; e questa forza, moltiplicata per la distanza CG, sarà l’efficacia della particella F nel far girare la Terra intorno al suo centro. Perciò l’efficacia di una particella nel luogo F starà all’efficacia di una particella nel luogo A come FG×GC sta ad AH×HC, cioè come FC² sta ad AC²; e pertanto l’efficacia totale di tutte le particelle nei loro luoghi F starà all’efficacia di altrettante particelle nel luogo A come la somma di tutti gli FC² sta alla somma di altrettanti AC², cioè (per quanto si è appena dimostrato) come uno sta a due. C.V.D.

**[III.G6.50]** E poiché le particelle agiscono allontanandosi perpendicolarmente dal piano QR, e in egual misura da entrambe le parti di questo piano, esse faranno girare la circonferenza del cerchio dell’equatore, e la Terra che vi aderisce, intorno a un asse che giace tanto in quel piano QR quanto nel piano dell’equatore.

### Lemma II (tutto il guscio esterno e l’anello)

**[III.G6.51]** **Poste le stesse cose, dico in secondo luogo che la forza e l’efficacia totale di tutte le particelle situate da ogni parte fuori del globo, nel far ruotare la Terra intorno allo stesso asse, sta alla forza totale di altrettante particelle, disposte nel cerchio dell’equatore AE uniformemente per tutto il giro a modo di anello, nel muovere la Terra con un simile moto circolare, come due sta a cinque.**

**[III.G6.52]** Sia infatti IK un cerchio qualsiasi, minore, parallelo all’equatore AE, e siano L, l due particelle uguali qualsiasi in questo cerchio, situate fuori del globo Pape. Se sul piano QR, che è perpendicolare al raggio condotto verso il Sole, si abbassano le perpendicolari LM, lm, le forze totali con cui quelle particelle fuggono il piano QR saranno proporzionali a quelle perpendicolari LM, lm. Sia poi la retta Ll parallela al piano Pape e sia divisa a metà in X; per il punto X si conduca Nn, parallela al piano QR, che incontri le perpendicolari LM, lm in N e n; e sul piano QR si abbassi la perpendicolare XY. Le forze contrarie delle particelle L e l, nel far ruotare la Terra in versi contrari, sono come LM×MC e lm×mC, cioè come LN×MC + NM×MC e ln×mC − nm×mC, ossia come LN×MC + NM×MC e LN×mC − NM×mC; e la loro differenza, LN×Mm − NM×(MC + mC), è la forza delle due particelle prese insieme nel far ruotare la Terra. La parte positiva di questa differenza, LN×Mm, ossia 2LN×NX, sta alla forza 2AH×HC di due particelle della stessa grandezza poste in A come LX² sta ad AC². E la parte negativa, NM×(MC + mC), ossia 2XY×CY, sta alla forza 2AH×HC delle stesse particelle poste in A come CX² sta ad AC². E perciò la differenza delle parti, cioè la forza delle due particelle L e l prese insieme nel far ruotare la Terra, sta alla forza di due particelle uguali a esse, poste nel luogo A, nel far ruotare ugualmente la Terra, come LX² − CX² sta ad AC². Ma se la circonferenza IK del cerchio IK si divide in innumerevoli particelle uguali L, tutti gli LX² staranno ad altrettanti IX² come 1 sta a 2 (per il Lemma I), e ad altrettanti AC² come IX² sta a 2AC²; e altrettanti XC² staranno ad altrettanti AC² come 2CX² sta a 2AC². Perciò le forze congiunte di tutte le particelle sulla circonferenza del cerchio IK stanno alle forze congiunte di altrettante particelle nel luogo A come IX² − 2CX² sta a 2AC²; e pertanto (per il Lemma I) alle forze congiunte di altrettante particelle sulla circonferenza del cerchio AE come IX² − 2CX² sta ad AC².

**[III.G6.53]** Ora, se il diametro Pp della sfera si divide in innumerevoli parti uguali, sulle quali insistano altrettanti cerchi IK, la materia sul perimetro di ciascun cerchio IK sarà come IX²; e perciò la forza di quella materia nel far ruotare la Terra sarà come IX² moltiplicato per (IX² − 2CX²). E la forza della stessa materia, se stesse sul perimetro del cerchio AE, sarebbe come IX² moltiplicato per AC². E pertanto la forza di tutte le particelle di tutta la materia che sta fuori del globo, sui perimetri di tutti i cerchi, sta alla forza di altrettante particelle poste sul perimetro del cerchio massimo AE come tutti gli IX² moltiplicati per (IX² − 2CX²) stanno ad altrettanti IX² moltiplicati per AC², cioè come tutti gli (AC² − CX²) moltiplicati per (AC² − 3CX²) stanno ad altrettanti (AC² − CX²) moltiplicati per AC², cioè come tutti gli AC⁴ − 4AC²×CX² + 3CX⁴ stanno ad altrettanti AC⁴ − AC²×CX², cioè come l’intera quantità fluente la cui flussione è AC⁴ − 4AC²×CX² + 3CX⁴ sta all’intera quantità fluente la cui flussione è AC⁴ − AC²×CX²; e perciò, per il metodo delle flussioni, come AC⁴×CX − 4/3 AC²×CX³ + 3/5 CX⁵ sta ad AC⁴×CX − 1/3 AC²×CX³, cioè, se al posto di CX si scrive l’intera Cp, o AC, come 4/15 AC⁵ sta a 2/3 AC⁵, cioè come due sta a cinque. C.V.D.

### Lemma III (la quantità di moto della Terra e quella dell’anello)

**[III.G6.54]** **Poste le stesse cose, dico in terzo luogo che la quantità di moto di tutta la Terra intorno all’asse già descritto, composta dalle quantità di moto di tutte le particelle, starà alla quantità di moto dell’anello predetto intorno allo stesso asse nel rapporto composto dal rapporto della materia nella Terra alla materia nell’anello e dal rapporto di tre quadrati dell’arco quadrantale di un cerchio qualsiasi a due quadrati del diametro; cioè nel rapporto della materia alla materia e del numero 925275 al numero 1000000.**

**[III.G6.55]** Infatti la quantità di moto di un cilindro che ruota intorno al proprio asse immobile sta alla quantità di moto della sfera inscritta, che ruota insieme con esso, come quattro quadrati uguali qualsiasi stanno a tre dei cerchi in essi inscritti; la quantità di moto del cilindro sta alla quantità di moto di un anello sottilissimo, che circonda la sfera e il cilindro nel loro contatto comune, come il doppio della materia nel cilindro sta al triplo della materia nell’anello; e questa quantità di moto dell’anello, nel moto continuato uniformemente intorno all’asse del cilindro, sta alla sua quantità di moto nel moto uniforme intorno al proprio diametro, compiuto nello stesso tempo periodico, come la circonferenza di un cerchio sta al doppio del diametro.

### Ipotesi II (l’anello fluido o rigido)

**[III.G6.56]** **Se l’anello predetto, tolta tutta la rimanente Terra, fosse portato da solo nell’orbita della Terra intorno al Sole con moto annuo, e intanto ruotasse con moto diurno intorno al proprio asse, inclinato sul piano dell’eclittica con un angolo di 23 1/2 gradi, il moto dei punti equinoziali sarebbe lo stesso, sia che quell’anello fosse fluido, sia che fosse fatto di materia rigida e salda.**

### Proposizione XXXIX. Problema XX (la precessione degli equinozi)

**[III.G6.57]** **Trovare la precessione degli equinozi.**

**[III.G6.58]** Il moto orario medio dei nodi della Luna in un’orbita circolare, quando i nodi sono nelle quadrature, era di 16″ 35‴ 16ⁱᵛ 36ᵛ; e la sua metà, 8″ 17‴ 38ⁱᵛ 18ᵛ, è (per le ragioni spiegate sopra) il moto orario medio dei nodi in una tale orbita; e in un intero anno siderale diventa di 20° 11′ 46″. Poiché dunque i nodi della Luna in una tale orbita compirebbero ogni anno 20° 11′ 46″ in antecedenza; e, se ci fossero più lune, i moti dei nodi di ciascuna (per il Cor. 16 della Prop. LXVI del Libro I) sarebbero come i tempi periodici; se una luna ruotasse vicino alla superficie della Terra nello spazio di un giorno siderale, il moto annuo dei suoi nodi starebbe a 20° 11′ 46″ come il giorno siderale di 23 ore e 56′ sta al tempo periodico della Luna di 27 giorni, 7 ore e 43′, cioè come 1436 sta a 39343. E lo stesso vale per i nodi di un anello di lune che circonda la Terra, sia che quelle lune non si tocchino fra loro, sia che si liquefacciano e si formino in un anello continuo, sia infine che quell’anello si irrigidisca e sia reso inflessibile.

**[III.G6.59]** Immaginiamo dunque che quell’anello, quanto alla quantità di materia, sia uguale a tutta la Terra PapAPepE che sta sopra il globo Pape (si veda la figura a p. 474); e poiché quel globo sta a quella Terra superiore come aC² sta ad AC² − aC², cioè (essendo il diametro minore della Terra, PC o aC, al semidiametro maggiore AC come 229 sta a 230) come 52441 sta a 459; se quell’anello cingesse la Terra lungo l’equatore ed entrambi ruotassero insieme intorno al diametro dell’anello, la quantità di moto dell’anello starebbe alla quantità di moto del globo interno (per il Lemma III di questo Libro) come 459 sta a 52441 e 1000000 sta a 925275, considerati congiuntamente, cioè come 4590 sta a 485223; e perciò la quantità di moto dell’anello starebbe alla somma delle quantità di moto dell’anello e del globo come 4590 sta a 489813. Quindi, se l’anello aderisce al globo e comunica al globo la quantità di moto con cui i suoi nodi, ossia i punti equinoziali, regrediscono, la quantità di moto che resterà nell’anello starà alla sua quantità di moto di prima come 4590 sta a 489813; e perciò il moto dei punti equinoziali diminuirà nello stesso rapporto. Il moto annuo dei punti equinoziali del corpo composto dell’anello e del globo starà dunque al moto di 20° 11′ 46″ come 1436 sta a 39343 e 4590 sta a 489813, considerati congiuntamente, cioè come 100 sta a 292369. Ma le forze per cui i nodi delle lune (come ho spiegato sopra), e perciò i punti equinoziali dell’anello, regrediscono (cioè le forze 3IT nella figura alle pp. 437 e 438), sono nelle singole particelle come le distanze delle particelle dal piano QR, e con queste forze quelle particelle fuggono il piano; e perciò (per il Lemma II), se la materia dell’anello si spargesse per tutta la superficie del globo, a modo della figura PapAPepE, per costituire quella parte superiore della Terra, la forza e l’efficacia totale di tutte le particelle nel far ruotare la Terra intorno a un diametro qualsiasi dell’equatore, e quindi nel muovere i punti equinoziali, risulterebbe minore di prima nel rapporto di 2 a 5. Perciò il regresso annuo degli equinozi starebbe ora a 20° 11′ 46″ come 10 sta a 73092, e diventerebbe quindi di 9″ 56‴ 50ⁱᵛ.

**[III.G6.60]** Ma questo moto deve essere diminuito a causa dell’inclinazione del piano dell’equatore sul piano dell’eclittica, e precisamente nel rapporto del seno 91706 (che è il seno del complemento di 23 1/2 gradi) al raggio 100000. In questo rapporto quel moto diventerà ora di 9″ 7‴ 20ⁱᵛ. Questa è la precessione annua degli equinozi che nasce dalla forza del Sole.

**[III.G6.61]** La forza della Luna nel muovere il mare stava poi alla forza del Sole circa come 4,4815 sta a 1. E la forza della Luna nel muovere gli equinozi sta alla forza del Sole nella stessa proporzione. Di qui risulta la precessione annua degli equinozi che nasce dalla forza della Luna, di 40″ 52‴ 52ⁱᵛ, e la precessione annua totale che nasce da entrambe le forze, di 50″ 00‴ 12ⁱᵛ. E questo moto concorda con i fenomeni. Infatti la precessione degli equinozi, secondo le osservazioni astronomiche, è ogni anno di cinquanta secondi, più o meno.

**[III.G6.62]** Se l’altezza della Terra all’equatore supera la sua altezza ai poli di più di 17 1/6 miglia, la sua materia sarà più rada alla circonferenza che al centro; e la precessione degli equinozi dovrà aumentare a causa di quell’altezza e diminuire a causa della radezza.

**[III.G6.63]** Abbiamo ormai descritto il sistema del Sole, della Terra, della Luna e dei pianeti: resta da aggiungere qualcosa sulle comete.

### Lemma IV (le comete sono più alte della Luna)

**[III.G6.64]** **Le comete sono più alte della Luna e si trovano nella regione dei pianeti.**

**[III.G6.65]** Come la mancanza di parallasse diurna ha innalzato le comete al di sopra delle regioni sublunari, così dalla parallasse annua si dimostra la loro discesa nelle regioni dei pianeti. Infatti le comete che procedono secondo l’ordine dei segni sono tutte, verso la fine della loro apparizione, o più lente del solito o retrograde, se la Terra è fra esse e il Sole; ma più veloci del dovuto, se la Terra volge verso l’opposizione. E al contrario quelle che procedono contro l’ordine dei segni sono più veloci del dovuto alla fine dell’apparizione, se la Terra si trova fra esse e il Sole; e più lente del dovuto o retrograde, se la Terra è situata dalla parte contraria. Ciò avviene soprattutto per il moto della Terra nelle sue varie posizioni, così come accade nei pianeti, che, secondo che il moto della Terra sia concorde o contrario, ora sono retrogradi, ora sembrano procedere più lentamente, ora invece più velocemente. Se la Terra procede verso la stessa parte della cometa e, con il moto angolare intorno al Sole, è portata tanto più velocemente che la retta condotta di continuo per la Terra e la cometa converga verso le parti al di là della cometa, la cometa vista dalla Terra, a causa del suo moto più lento, appare retrograda; se invece la Terra è portata più lentamente, il moto della cometa (sottratto il moto della Terra) diventa almeno più lento. Ma se la Terra procede verso parti contrarie, la cometa appare di conseguenza più veloce.

**[III.G6.66]** Dall’accelerazione, dal ritardo o dal moto retrogrado si ricava poi la distanza della cometa in questo modo. Siano ♈QA, ♈QB, ♈QC tre longitudini osservate della cometa all’inizio del moto, e sia ♈QF la longitudine osservata per ultima, quando la cometa cessa di essere visibile. Si conduca la retta ABC, le cui parti AB, BC, comprese fra le rette QA e QB, QB e QC, stiano fra loro come i tempi fra le prime tre osservazioni. Si prolunghi AC fino a G, in modo che AG stia ad AB come il tempo fra la prima e l’ultima osservazione sta al tempo fra la prima e la seconda, e si congiunga QG. Se la cometa si muovesse uniformemente in linea retta, e la Terra o stesse ferma o anch’essa avanzasse in linea retta con moto uniforme, l’angolo ♈QG sarebbe la longitudine della cometa al tempo dell’ultima osservazione. L’angolo FQG, dunque, che è la differenza delle longitudini, nasce dalla disuguaglianza dei moti della cometa e della Terra. Questo angolo, se la Terra e la cometa si muovono verso parti contrarie, si aggiunge all’angolo ♈QG, e rende così più veloce il moto apparente della cometa; se invece la cometa procede verso le stesse parti della Terra, gli si sottrae, e rende il moto della cometa o più lento o forse retrogrado, come ho appena esposto. Questo angolo nasce dunque principalmente dal moto della Terra, e perciò va giustamente considerato la parallasse della cometa, trascurando cioè un certo suo aumento o diminuzione che possa nascere dal moto non uniforme della cometa nella sua orbita.

**[III.G6.67]** La distanza della cometa si ricava poi da questa parallasse così. S rappresenti il Sole, acT l’orbe magno, a il luogo della Terra nella prima osservazione, c il luogo della Terra nella terza osservazione, T il luogo della Terra nell’ultima osservazione, e T♈ una linea retta condotta verso il principio dell’Ariete. Si prenda l’angolo ♈TV uguale all’angolo ♈QF, cioè uguale alla longitudine della cometa quando la Terra si trova in T. Si congiunga ac e la si prolunghi fino a g, in modo che ag stia ad ac come AG sta ad AC; e g sarà il luogo che la Terra, continuando uniformemente il moto lungo la retta ac, raggiungerebbe al tempo dell’ultima osservazione. Perciò, se si conduce g♈ parallela a T♈ e si prende l’angolo ♈gV uguale all’angolo ♈QG, questo angolo ♈gV sarà uguale alla longitudine della cometa vista dal luogo g; e l’angolo TVg sarà la parallasse che nasce dallo spostamento della Terra dal luogo g al luogo T; e perciò V sarà il luogo della cometa nel piano dell’eclittica. Questo luogo V suole poi trovarsi al di sotto dell’orbita di Giove.

**[III.G6.68]** Lo stesso si ricava dalla curvatura del cammino delle comete. Questi corpi procedono quasi lungo cerchi massimi finché si muovono più velocemente; ma alla fine del corso, quando quella parte del moto apparente che nasce dalla parallasse ha una proporzione maggiore rispetto all’intero moto apparente, sogliono deviare da questi cerchi e, ogni volta che la Terra si muove verso una parte, andare verso la parte contraria. Questa deviazione nasce soprattutto dalla parallasse, poiché corrisponde al moto della Terra; e la sua quantità notevole, secondo il mio calcolo, ha collocato le comete, quando scompaiono, ben al di sotto di Giove. Ne segue che nei perigei e nei perieli, quando sono più vicine, scendono spesso al di sotto delle orbite di Marte e dei pianeti inferiori.

**[III.G6.69]** La vicinanza delle comete è confermata anche dalla luce delle teste. Lo splendore di un corpo celeste illuminato dal Sole, che si allontana verso regioni lontane, diminuisce infatti in rapporto quadruplicato della distanza: in rapporto duplicato, cioè, per l’aumento della distanza del corpo dal Sole, e in un altro rapporto duplicato per la diminuzione del diametro apparente. Perciò, se sono date sia la quantità di luce sia il diametro apparente di una cometa, sarà data la distanza, dicendo che la distanza sta alla distanza di un pianeta nel rapporto del diametro al diametro direttamente e nel rapporto subduplicato della luce alla luce inversamente. Così il diametro minimo della capigliatura della cometa dell’anno 1682, osservato da Flamsteed con un tubo ottico di sedici piedi e misurato con il micrometro, era di 2′ 0″; il nucleo, invece, ossia la stella nel mezzo della testa, occupava appena la decima parte di questa larghezza, ed era quindi largo soltanto 11″ o 12″. Per la luce e la chiarezza della testa, poi, superava la testa della cometa dell’anno 1680, e rivaleggiava con le stelle di prima o di seconda grandezza. Supponiamo che Saturno con il suo anello fosse circa quattro volte più luminoso: poiché la luce dell’anello uguagliava all’incirca la luce del globo interno, e il diametro apparente del globo è circa 21″, e perciò la luce del globo e dell’anello insieme uguaglierebbe la luce di un globo il cui diametro fosse 30″, la distanza della cometa starà alla distanza di Saturno come 1 sta a √4 inversamente e 12″ sta a 30″ direttamente, cioè come 24 sta a 30, ossia 4 a 5. Inoltre la cometa dell’anno 1665, nel mese di aprile, come riferisce Hevelius, con la sua chiarezza superava quasi tutte le stelle fisse, e anzi lo stesso Saturno, per il colore, cioè, molto più vivo. Questa cometa era infatti più luminosa di quell’altra che era apparsa alla fine dell’anno precedente, ed era paragonata alle stelle di prima grandezza. La larghezza della capigliatura era di circa 6′, ma il nucleo, confrontato con i pianeti per mezzo del tubo ottico, era nettamente minore di Giove, e veniva giudicato ora minore del corpo centrale di Saturno, ora uguale a esso. Inoltre, poiché il diametro della capigliatura delle comete raramente supera 8′ o 12′, e il diametro del nucleo, ossia della stella centrale, è circa la decima o forse la quindicesima parte del diametro della capigliatura, è chiaro che queste stelle sono per lo più della stessa grandezza apparente dei pianeti. Perciò, poiché la loro luce può non di rado essere paragonata alla luce di Saturno, e talvolta la supera, è manifesto che tutte le comete, nei perieli, vanno collocate o al di sotto di Saturno o non molto al di sopra. Sbagliano dunque di tutto il cielo coloro che relegano le comete quasi nella regione delle stelle fisse: in tal caso, certo, esse non dovrebbero essere illuminate dal nostro Sole più di quanto i pianeti che sono qui siano illuminati dalle stelle fisse.

**[III.G6.70]** Abbiamo discusso queste cose senza considerare l’oscuramento delle comete dovuto a quel fumo molto abbondante e denso da cui la testa è circondata, e attraverso il quale essa splende sempre in modo smorzato, come attraverso una nube. Infatti, quanto più il corpo è reso oscuro da questo fumo, tanto più è necessario che si avvicini al Sole, perché con la quantità di luce che riflette rivaleggi con i pianeti. Di qui diventa verosimile che le comete scendano molto al di sotto della sfera di Saturno, come abbiamo provato dalla parallasse. Lo stesso, poi, è confermato al massimo grado dalle code. Queste nascono o dalla riflessione del fumo sparso per l’etere, o dalla luce della testa. Nel primo caso bisogna diminuire la distanza delle comete, perché il fumo nato continuamente dalla testa non debba propagarsi per spazi troppo ampi con una velocità e un’espansione incredibili. Nel secondo caso tutta la luce, tanto della coda quanto della capigliatura, va riferita al nucleo della testa. Se dunque immaginiamo che tutta questa luce si raccolga e si restringa entro il disco del nucleo, quel nucleo, ogni volta che emette una coda grandissima e splendentissima, supererà certo di molto con il suo splendore Giove stesso. Emettendo dunque più luce con un diametro apparente minore, sarà illuminato molto di più dal Sole, e perciò sarà molto più vicino al Sole. Anzi, con lo stesso argomento, le teste che si nascondono sotto il Sole ed emettono talvolta code sia grandissime sia splendentissime, simili a travi infuocate, devono essere collocate al di sotto dell’orbita di Venere. Tutta quella luce, infatti, se si suppone raccolta in una stella, supererebbe talvolta Venere stessa, per non dire più Veneri riunite.

**[III.G6.71]** Lo stesso si ricava infine dalla luce delle teste, che cresce quando le comete si allontanano dalla Terra verso il Sole e decresce quando si allontanano dal Sole verso la Terra. Così infatti la cometa posteriore dell’anno 1665 (secondo le osservazioni di Hevelius), da quando cominciò a essere vista, rallentava sempre il suo moto apparente, e perciò aveva già oltrepassato il perigeo; lo splendore della testa, nondimeno, cresceva di giorno in giorno, finché la cometa, coperta dai raggi solari, cessò di apparire. La cometa dell’anno 1683 (secondo le osservazioni dello stesso Hevelius), alla fine del mese di luglio, quando fu vista per la prima volta, si muoveva lentissimamente, compiendo nella sua orbita circa 40 o 45 primi al giorno. Da quel momento il suo moto diurno aumentò continuamente fino al 4 settembre, quando divenne di circa cinque gradi. Per tutto questo tempo, dunque, la cometa si avvicinava alla Terra. Ciò si ricava anche dal diametro della testa, misurato con il micrometro: Hevelius trovò infatti che il 6 agosto era soltanto di 6′ 5″, compresa la chioma, e il 2 settembre di 9′ 7″. La testa, dunque, all’inizio apparve molto più piccola che alla fine del moto, ma all’inizio, nelle vicinanze del Sole, si mostrò tuttavia molto più luminosa che verso la fine, come riferisce lo stesso Hevelius. Perciò per tutto questo tempo, a causa del suo allontanarsi dal Sole, diminuì quanto alla luce, nonostante l’avvicinamento alla Terra. La cometa dell’anno 1618, verso la metà del mese di dicembre, e quella dell’anno 1680, verso la fine dello stesso mese, si muovevano velocissime, e perciò erano allora nei perigei. Ma lo splendore massimo delle teste si ebbe quasi due settimane prima, quando erano appena uscite dai raggi solari; e lo splendore massimo delle code poco prima, in una maggiore vicinanza del Sole. La testa della cometa anteriore, secondo le osservazioni di Cysat, il 1° dicembre appariva più grande delle stelle di prima grandezza, e il 16 dicembre (trovandosi ormai nel perigeo) era diminuita poco di grandezza, moltissimo di splendore, ossia di chiarezza della luce. Il 7 gennaio Keplero, incerto sulla testa, smise di osservare. Il giorno 12 del mese di dicembre la testa della cometa posteriore fu vista e osservata da Flamsteed alla distanza di nove gradi dal Sole; cosa che a stento sarebbe stata concessa a una stella di terza grandezza. Il 15 e il 17 dicembre apparve come una stella di terza grandezza, diminuita certo nello splendore dalle nubi vicino al Sole che tramontava. Il 26 dicembre, muovendosi velocissima e trovandosi quasi nel perigeo, era inferiore alla Bocca di Pegaso (*os Pegasi*), stella di terza grandezza. Il 3 gennaio appariva come una stella di quarta grandezza, il 9 gennaio come una di quinta; il 13 gennaio scomparve per lo splendore della Luna crescente. Il 25 gennaio uguagliava a stento le stelle di settima grandezza. Se si prendono tempi uguali prima e dopo il perigeo, le teste, che in quei tempi, poste in regioni lontane, avrebbero dovuto splendere ugualmente per le distanze uguali dalla Terra, dalla parte del Sole splendettero al massimo, dall’altra parte del perigeo svanirono. Dalla grande differenza della luce nelle due posizioni si conclude dunque una grande vicinanza del Sole e della cometa nella prima posizione. La luce delle comete, infatti, suole essere regolare, e apparire massima quando le teste si muovono più velocemente, e perciò sono nei perigei; se non in quanto essa è maggiore nelle vicinanze del Sole.

**[III.G6.72]** *Cor. 1.* Le comete splendono dunque per la luce del Sole che esse riflettono.

**[III.G6.73]** *Cor. 2.* Da quanto si è detto si comprende anche perché le comete frequentino tanto la regione del Sole. Se si vedessero nelle regioni molto al di là di Saturno, dovrebbero apparire più spesso nelle parti opposte al Sole. Quelle che si trovassero in queste parti, infatti, sarebbero più vicine alla Terra; e il Sole interposto oscurerebbe le altre. Ma, scorrendo le storie delle comete, ho trovato che se ne sono scoperte quattro o cinque volte di più nell’emisfero verso il Sole che nell’emisfero opposto, oltre ad altre, senza dubbio non poche, che la luce solare ha nascosto. Certo, scendendo verso le nostre regioni, esse non emettono code né sono illuminate dal Sole tanto da mostrarsi, per essere scoperte a occhio nudo, prima di essere più vicine di Giove stesso. Ma la parte di gran lunga maggiore dello spazio descritto intorno al Sole con un intervallo così piccolo si trova dal lato della Terra che guarda il Sole; e in quella parte maggiore le comete, per lo più più vicine al Sole, sogliono essere più illuminate.

**[III.G6.74]** *Cor. 3.* Di qui è anche manifesto che i cieli sono privi di resistenza. Le comete, infatti, seguendo cammini obliqui e talvolta contrari al corso dei pianeti, si muovono in ogni direzione con la massima libertà, e conservano i loro moti lunghissimamente, anche contro il corso dei pianeti. Se non sbaglio, sono un genere di pianeti, e con moto perpetuo ritornano in orbita. Ciò che sostengono alcuni scrittori, che siano meteore, traendo l’argomento dai continui mutamenti delle teste, sembra infatti privo di fondamento. Le teste delle comete sono cinte da atmosfere enormi; e le atmosfere devono essere più dense in basso. Sono dunque le nubi, non i corpi stessi delle comete, quelle in cui si vedono quei mutamenti. Così la Terra, se fosse vista dai pianeti, splenderebbe senza dubbio della luce delle sue nubi, e il corpo solido sotto le nubi resterebbe quasi nascosto. Così le fasce di Giove si sono formate nelle nubi di quel pianeta, che mutano posizione fra loro, e il corpo solido di Giove si vede con più difficoltà attraverso quelle nubi. E molto più devono nascondersi i corpi delle comete sotto atmosfere più profonde e più dense.

### Proposizione XL. Teorema XX (le comete si muovono in sezioni coniche)

**[III.G6.75]** **Le comete si muovono in sezioni coniche che hanno i fuochi nel centro del Sole, e con raggi condotti al Sole descrivono aree proporzionali ai tempi.**

**[III.G6.76]** È evidente per il Cor. 1 della Prop. XIII del Libro I, confrontato con le Propp. VIII, XII e XIII del Libro III.

**[III.G6.77]** *Cor. 1.* Di qui, se le comete ritornano in orbita, le orbite saranno ellissi, e i tempi periodici staranno ai tempi periodici dei pianeti in rapporto sesquiplicato degli assi principali. Perciò le comete, che si trovano per la maggior parte al di sopra dei pianeti, e per questo descrivono orbite con assi maggiori, gireranno più lentamente. Per esempio, se l’asse dell’orbita di una cometa è quattro volte maggiore dell’asse dell’orbita di Saturno, il tempo della rivoluzione della cometa starà al tempo della rivoluzione di Saturno, cioè a 30 anni, come √(4³) (ossia 8) sta a 1, e sarà perciò di 240 anni.

**[III.G6.78]** *Cor. 2.* Le orbite, però, saranno così prossime a parabole che al loro posto si possono usare parabole senza errori sensibili.

**[III.G6.79]** *Cor. 3.* E perciò (per il Cor. 7 della Prop. XVI del Libro I) la velocità di ogni cometa starà sempre alla velocità di un pianeta qualsiasi che ruota in un cerchio intorno al Sole, con ottima approssimazione, in rapporto subduplicato del doppio della distanza del pianeta dal centro del Sole alla distanza della cometa dal centro del Sole. Supponiamo che il raggio dell’orbe magno, ossia il semidiametro massimo dell’ellisse in cui ruota la Terra, sia di 100000000 parti: la Terra con il suo moto diurno medio descriverà 1720212 parti, e con il moto orario 71675 1/2 parti. Perciò la cometa, alla stessa distanza media della Terra dal Sole, con una velocità che stia alla velocità della Terra come √2 sta a 1, descriverà con il suo moto diurno 2432747 parti, e con il moto orario 101364 1/2 parti. Alle distanze maggiori o minori, poi, il moto sia diurno sia orario starà a questo moto diurno e orario inversamente in rapporto subduplicato delle distanze, ed è perciò dato.

**[III.G6.80]** *Cor. 4.* Perciò, se il lato retto della parabola è quattro volte maggiore del raggio dell’orbe magno, e si pone che il quadrato di quel raggio sia di 100000000 parti, l’area che la cometa descrive ogni giorno con il raggio condotto al Sole sarà di 1216373 1/2 parti, e ogni ora quell’area sarà di 50682 1/4 parti. Se invece il lato retto è maggiore o minore in un rapporto qualsiasi, l’area diurna e oraria sarà maggiore o minore nello stesso rapporto subduplicato.

### Lemma V (la curva di genere parabolico per punti dati)

**[III.G6.81]** **Trovare una linea curva di genere parabolico che passi per un numero qualsiasi di punti dati.**

**[III.G6.82]** Siano quei punti A, B, C, D, E, F, ecc., e da essi abbassa su una retta qualsiasi HN, data di posizione, altrettante perpendicolari AH, BI, CK, DL, EM, FN.

**[III.G6.83]** *Caso 1.* Se gli intervalli HI, IK, KL, ecc. dei punti H, I, K, L, M, N sono uguali, raccogli le differenze prime delle perpendicolari AH, BI, CK, ecc., b, 2b, 3b, 4b, 5b, ecc.; le seconde, c, 2c, 3c, 4c, ecc.; le terze, d, 2d, 3d, ecc.; in modo cioè che sia AH − BI = b, BI − CK = 2b, CK − DL = 3b, DL + EM = 4b, −EM + FN = 5b, ecc.; poi b − 2b = c, ecc.; e così si proceda fino all’ultima differenza, che qui è f. Poi, innalzata una perpendicolare qualsiasi RS, che sia un’ordinata della curva cercata, per trovarne la lunghezza poni che gli intervalli HI, IK, KL, LM, ecc. siano unità, e di’ AH = a, −HS = p, ½p moltiplicato per −IS = q, ⅓q moltiplicato per +SK = r, ¼r moltiplicato per +SL = s, ⅕s moltiplicato per +SM = t; procedendo cioè fino alla penultima perpendicolare ME, e premettendo segni negativi ai termini HS, IS, ecc., che giacciono dalla parte del punto S verso A, e segni positivi ai termini SK, SL, ecc., che giacciono dall’altra parte del punto S. E, osservati bene i segni, sarà RS = a + bp + cq + dr + es + ft, ecc.

**[III.G6.84]** *Caso 2.* Se invece gli intervalli HI, IK, ecc. dei punti H, I, K, L, ecc. sono disuguali, raccogli le differenze prime delle perpendicolari AH, BI, CK, ecc., divise per gli intervalli fra le perpendicolari, b, 2b, 3b, 4b, 5b; le seconde, divise per gli intervalli presi a due a due, c, 2c, 3c, 4c, ecc.; le terze, divise per gli intervalli presi a tre a tre, d, 2d, 3d, ecc.; le quarte, divise per gli intervalli presi a quattro a quattro, e, 2e, ecc.; e così di seguito; in modo cioè che sia b = (AH − BI)/HI, 2b = (BI − CK)/IK, 3b = (CK − DL)/KL, ecc.; poi c = (b − 2b)/HK, 2c = (2b − 3b)/IL, 3c = (3b − 4b)/KM, ecc.; quindi d = (c − 2c)/HL, 2d = (2c − 3c)/IM, ecc. Trovate le differenze, di’ AH = a, −HS = p, p moltiplicato per −IS = q, q moltiplicato per +SK = r, r moltiplicato per +SL = s, s moltiplicato per +SM = t; procedendo cioè fino alla penultima perpendicolare ME; e sarà l’ordinata RS = a + bp + cq + dr + es + ft, ecc.

**[III.G6.85]** *Cor.* Di qui si possono trovare con ottima approssimazione le aree di tutte le curve. Se infatti si trovano alcuni punti di una curva qualsiasi da quadrare, e s’intende condotta per essi una parabola, l’area di questa parabola sarà, con ottima approssimazione, la stessa dell’area di quella curva da quadrare. E la parabola si può sempre quadrare geometricamente con metodi notissimi.

### Lemma VI (il luogo della cometa in un tempo intermedio)

**[III.G6.86]** **Da alcuni luoghi osservati di una cometa trovare il suo luogo in un tempo intermedio qualsiasi dato.**

**[III.G6.87]** HI, IK, KL, LM rappresentino i tempi fra le osservazioni (nella figura precedente), HA, IB, KC, LD, ME cinque longitudini osservate della cometa, HS il tempo dato fra la prima osservazione e la longitudine cercata. Se per i punti A, B, C, D, E s’intende condotta una curva regolare ABCDE, e per il lemma precedente se ne trova l’ordinata RS, RS sarà la longitudine cercata.

**[III.G6.88]** Con lo stesso metodo, da cinque latitudini osservate si trova la latitudine in un tempo dato.

**[III.G6.89]** Se le differenze delle longitudini osservate sono piccole, per esempio di soli 4 o 5 gradi, basteranno tre o quattro osservazioni per trovare la nuova longitudine e latitudine. Se invece le differenze sono maggiori, per esempio di 10 o 20 gradi, si dovranno usare cinque osservazioni.

### Lemma VII (la retta divisa in un rapporto dato)

**[III.G6.90]** **Per un punto dato P condurre una linea retta BC le cui parti PB, PC, tagliate da due rette AB, AC date di posizione, abbiano fra loro un rapporto dato.**

**[III.G6.91]** Dal punto P a una delle due rette, AB, si conduca una retta qualsiasi PD, e la si prolunghi verso l’altra retta AC fino a E, in modo che PE stia a PD in quel rapporto dato. Sia EC parallela ad AD; e, se si conduce CPB, PC starà a PB come PE sta a PD. C.V.F.

### Lemma VIII (la corda divisa in proporzione ai tempi)

**[III.G6.92]** **Sia ABC una parabola con il fuoco S. Con la corda AC, divisa a metà in I, si tagli il segmento ABCI, il cui diametro sia Iμ e il vertice μ. Su Iμ prolungata si prenda μO uguale alla metà di Iμ. Si congiunga OS e la si prolunghi fino a ξ, in modo che Sξ sia uguale a 2SO. Se una cometa B si muove sull’arco CBA, e si conduce ξB che seca AC in E, dico che il punto E taglia dalla corda AC un segmento AE proporzionale al tempo, con ottima approssimazione.**

**[III.G6.93]** Si congiunga infatti EO, che seca l’arco parabolico ABC in Y, e si conduca μX, che tocchi lo stesso arco nel vertice μ e incontri EO in X; l’area curvilinea AEXμA starà all’area curvilinea ACYμA come AE sta ad AC. Perciò, poiché il triangolo ASE sta al triangolo ASC nello stesso rapporto, l’area totale ASEXμA starà all’area totale ASCYμA come AE sta ad AC. Ma, poiché ξO sta a SO come 3 sta a 1, ed EO sta a XO nello stesso rapporto, SX sarà parallela a EB; e perciò, se si congiunge BX, il triangolo SEB sarà uguale al triangolo XEB. Quindi, se all’area ASEXμA si aggiunge il triangolo EXB, e dalla somma si toglie il triangolo SEB, resterà l’area ASBXμA uguale all’area ASEXμA, e quindi starà all’area ASCYμA come AE sta ad AC. Ma all’area ASBXμA è uguale, con ottima approssimazione, l’area ASBYμA; e questa area ASBYμA sta all’area ASCYμA come il tempo in cui è descritto l’arco AB sta al tempo in cui è descritto l’arco intero AC. Perciò AE sta ad AC nel rapporto dei tempi, con ottima approssimazione. C.V.D.

**[III.G6.94]** *Cor.* Quando il punto B cade nel vertice μ della parabola, AE sta ad AC esattamente nel rapporto dei tempi.

**[III.G6.95]** *Scolio.* Se si congiunge μξ, che seca AC in δ, e su di essa si prende ξn che stia a μB come 27MI sta a 16Mμ, la retta Bn, una volta condotta, segherà la corda AC nel rapporto dei tempi più esattamente di prima. Il punto n si trovi poi al di là del punto ξ, se il punto B dista dal vertice principale della parabola più del punto μ; e al di qua, se ne dista meno.

### Lemma IX (tre lunghezze uguali)

**[III.G6.96]** **Le rette Iμ e μM e la lunghezza AI²/4Sμ sono uguali fra loro.**

**[III.G6.97]** Infatti 4Sμ è il lato retto della parabola relativo al vertice μ.

### Lemma X (la velocità con cui si percorre la corda)

**[III.G6.98]** **Si prolunghi Sμ fino a N e a P, in modo che μN sia la terza parte di μI, e SP stia a SN come SN sta a Sμ. Una cometa, nel tempo in cui descrive l’arco AμC, se procedesse sempre con la velocità che ha all’altezza uguale a SP, descriverebbe una lunghezza uguale alla corda AC.**

**[III.G6.99]** Infatti, se la cometa, con la velocità che ha in μ, procedesse nello stesso tempo uniformemente lungo la retta che tocca la parabola in μ, l’area che descriverebbe con il raggio condotto al punto S sarebbe uguale all’area parabolica ASCμ. Perciò il rettangolo formato dalla lunghezza descritta sulla tangente e dalla lunghezza Sμ starebbe al rettangolo formato dalle lunghezze AC e SM come l’area ASCμ sta al triangolo ASC, cioè come SN sta a SM. Perciò AC sta alla lunghezza descritta sulla tangente come Sμ sta a SN. Ma poiché la velocità della cometa all’altezza SP sta (per il Cor. 6 della Prop. XVI del Libro I) alla sua velocità all’altezza Sμ inversamente in rapporto subduplicato di SP a Sμ, cioè nel rapporto di Sμ a SN, la lunghezza descritta con questa velocità nello stesso tempo starà alla lunghezza descritta sulla tangente come Sμ sta a SN. Perciò AC e la lunghezza descritta con questa nuova velocità, poiché stanno nello stesso rapporto alla lunghezza descritta sulla tangente, sono uguali fra loro. C.V.D.

**[III.G6.100]** *Cor.* La cometa, dunque, con la velocità che ha all’altezza Sμ + ⅔Iμ, descriverebbe nello stesso tempo la corda AC con ottima approssimazione.

### Lemma XI (la caduta con forza costante)

**[III.G6.101]** **Se una cometa, privata di ogni moto, fosse lasciata cadere dall’altezza SN, ossia Sμ + ⅓Iμ, in modo da cadere nel Sole, e fosse sempre sollecitata verso il Sole da quella forza, continuata uniformemente, da cui è sollecitata all’inizio, nella metà del tempo in cui descrive nella sua orbita l’arco AC descriverebbe con la sua discesa uno spazio uguale alla lunghezza Iμ.**

**[III.G6.102]** Infatti la cometa, nel tempo in cui descrive l’arco parabolico AC, nello stesso tempo, con la velocità che ha all’altezza SP (per l’ultimo lemma), descriverà la corda AC; e perciò (per il Cor. 7 della Prop. XVI del Libro I), ruotando nello stesso tempo per la forza della sua gravità in un cerchio il cui semidiametro fosse SP, descriverebbe un arco la cui lunghezza starebbe alla corda AC dell’arco parabolico in rapporto subduplicato dell’unità al due. E perciò, con il peso che ha verso il Sole all’altezza SP, cadendo da quell’altezza verso il Sole, descriverebbe nella metà di quel tempo (per il Cor. 9 della Prop. IV del Libro I) uno spazio uguale al quadrato della metà di quella corda diviso per il quadruplo dell’altezza SP, cioè lo spazio AI²/4SP. Perciò, poiché il peso della cometa verso il Sole all’altezza SN sta al suo peso verso il Sole all’altezza SP come SP sta a Sμ, la cometa, con il peso che ha all’altezza SN, cadendo nel Sole nello stesso tempo, descriverà lo spazio AI²/4Sμ, cioè uno spazio uguale alla lunghezza Iμ o Mμ. C.V.D.

**Fine del gruppo G6 (Propp. XXXIV–XL). Nel testo originale segue la Prop. XLI (Fascicolo 26a).**

---

## Apparato

### A.0 Estensioni del glossario

I termini seguenti non comparivano nei glossari comune, del Libro II e del Libro III. Ognuno è reso in modo costante in tutto il fascicolo.

| Latino | Italiano | Motivazione |
|---|---|---|
| *corpus lunare* | «corpo lunare» | Prop. XXXVIII; calco trasparente. |
| *affectare* (*talem figuram luna affectat*) | «tendere ad assumere» | Il verbo indica la figura verso cui la Luna tende per l’equilibrio, non una figura già osservata; Motte «affects». |
| *oscillatio*, *oscillando redire* | «oscillazione», «tornare oscillando» | Glossario del Libro II (*oscillatio*); qui è l’oscillazione della figura lunare intorno alla posizione di equilibrio (la libra­zione). Motte «libratory motion», «librations». |
| *efficacia* (*vis & efficacia*) | «efficacia» | Lemmi I–II, Prop. XXXIX: la forza moltiplicata per il braccio, cioè il momento (nota N2). |
| *in morem annuli* | «a modo di anello» | Lemmi I–II, Prop. XXXIX (*in morem figuræ*: «a modo della figura»). |
| *rotare*, *convertere*, *movere* (*ad terram rotandam*) | «far ruotare», «far girare», «muovere» | Si conserva la varietà del latino. |
| *fugere planum* | «fuggire il piano» | Lemma II, Prop. XXXIX; Motte «recede from». Si conserva l’immagine. |
| *pars affirmativa / negativa* | «parte positiva / negativa» | Lemma II. |
| *quantitas fluens*; *fluxio*; *methodus fluxionum* | «quantità fluente»; «flussione»; «metodo delle flussioni» | Lemma II. Termini tecnici di Newton (oggi: primitiva, derivata, calcolo integrale), lasciati nella forma storica. |
| *arcus quadrantalis* | «arco quadrantale» | Lemma III: l’arco di un quarto di cerchio. |
| *motus* (grandezza: Lemma III, Prop. XXXIX) | «quantità di moto» | Applicazione del glossario comune; vedi Criteri e nota N4. Motte «motion». **Dubbio segnalato:** nella frase *motum suum, quo ipsius nodi … regrediuntur, cum globo communicet* il *motus* è insieme la grandezza e il moto che fa regredire i nodi; ho scelto «quantità di moto» perché il periodo successivo la confronta numericamente. |
| *puncta æquinoctialia*; *regredi*; *regressus* | «punti equinoziali»; «regredire»; «regresso» | Prop. XXXIX, Ipotesi II. |
| *motus mediocris* / *motus medius* (dei nodi) | «moto medio» in entrambi i casi | Il glossario fissa *motus medius* e *mediocris distantia* entrambi con «medio». Nella Prop. XXXIX Newton distingue il *motus mediocris horarius* «quando i nodi sono nelle quadrature» (16″ 35‴ 16iv 36v) dal *motus medius horarius* su tutte le posizioni dei nodi (la metà). La distinzione è affidata al contesto; **dubbio segnalato** (Motte: «middle» / «mean»). |
| *sinus complementi*; *radius* | «seno del complemento»; «raggio» | Prop. XXXIX: il seno del complemento è il coseno; il «raggio» è il raggio delle tavole, 100000. |
| *rarior*; *raritas* | «più rada»; «radezza» | Prop. XXXIX; coerente con *medium rarum* «mezzo rado» del Libro II. |
| *parallaxis diurna / annua* | «parallasse diurna / annua» | Lemma IV; glossario (*parallaxis*). |
| *secundum ordinem signorum / contra ordinem signorum* | «secondo l’ordine dei segni / contro l’ordine dei segni» | Lemma IV: moto diretto e retrogrado in longitudine. |
| *retrogradus*; *solito tardior*; *justo celerior / tardior* | «retrogrado»; «più lento del solito»; «più veloce / più lento del dovuto» | Lemma IV. |
| *sub exitu apparitionis* | «verso la fine della loro apparizione» | Lemma IV. |
| *capillitium* | «capigliatura» | Lemma IV: l’involucro luminoso della testa. Il glossario riserva «chioma» a *coma*, che compare una sola volta (*inclusa coma*, III.G6.71); per non confondere i due termini latini, *capillitium* è reso con il calco «capigliatura», con nota. Motte «head». |
| *tubus opticus* | «tubo ottico» | Lemma IV. Il glossario dà *telescopium* «telescopio»; *tubus opticus* è un altro termine latino e resta come calco (è il telescopio). |
| *claritas*; *splendor*; *lux*; *lucidus* | «chiarezza»; «splendore»; «luce»; «luminoso» | Lemma IV. *Splendor* «splendore» non collide con *jubar* (glossario: «splendore»), che in questo fascicolo non compare. |
| *stella primæ (secundæ …) magnitudinis* | «stella di prima (seconda …) grandezza» | Lemma IV. |
| *globus intermedius*, *corpus intermedium* (di Saturno) | «globo interno», «corpo centrale» | Lemma IV: il globo di Saturno dentro l’anello. |
| *errare toto cœlo* | «sbagliare di tutto il cielo» | Lemma IV. Espressione idiomatica («sbagliare di grosso»), qui con un evidente gioco di parole; si conserva il calco (nota N6). |
| *fumus* | «fumo» | Lemma IV; Motte «smoke». |
| *trabes ignitæ* | «travi infuocate» | Lemma IV. |
| *os Pegasi* | «la Bocca di Pegaso» | Lemma IV; secondo il criterio del coordinatore per le stelle con nome latino (nota N6). |
| *cingula Jovis* | «le fasce di Giove» | Lemma IV, Cor. 3; Motte «belts». |
| *meteora* | «meteore» | Lemma IV, Cor. 3: fenomeni dell’atmosfera, nel senso aristotelico. |
| *in orbem redire* | «ritornare in orbita» | Lemma IV, Cor. 3; Prop. XL, Cor. 1: percorrere un’orbita chiusa e tornare periodicamente; Motte «revolving in orbits returning into themselves». |
| *cœli resistentia destituuntur* | «i cieli sono privi di resistenza» | Lemma IV, Cor. 3. |
| *linea curva generis parabolici* | «linea curva di genere parabolico» | Lemma V: la «parabola» di grado qualsiasi, cioè un polinomio. |
| *differentiæ primæ, secundæ, tertiæ* | «differenze prime, seconde, terze» | Lemma V. |
| *intervalla bina, terna, quaterna* | «intervalli presi a due a due, a tre a tre, a quattro a quattro» | Lemma V, Caso 2. |
| *quadrare*; *Geometrice* | «quadrare»; «geometricamente» | Lemma V, Cor. |
| *curva regularis* | «curva regolare» | Lemma VI. |
| *diameter* (di un segmento di parabola); *vertex* | «diametro»; «vertice» | Lemma VIII: la retta per il punto medio della corda parallela all’asse. |
| *altitudo* (distanza dal Sole) | «altezza» | Lemmi X–XI. Calco del latino: l’«altezza» SP è una distanza dal centro del Sole; Motte «height». |
| *contentum sub* | «rettangolo formato da» | Lemma X; come nel Fascicolo 6 (Prop. XIV, «il rettangolo formato dagli assi»). |
| *urgere* | «sollecitare» | Lemma XI; glossario del Fascicolo 3 (per le forze acceleratrici). |
| *lemma novissimum* | «l’ultimo lemma» | Lemma XI. |

**Glossario applicato con un dubbio.** *Coma* «chioma» compare una sola volta; per il fatto che la «capigliatura» (*capillitium*) è a sua volta la chioma in senso moderno, si veda la nota N6. *Annulus* «anello» vale sia per l’anello di materia dei Lemmi I–III sia per l’anello di Saturno. *Orbis* è «orbita» ovunque in questo fascicolo (*orbis lunaris*, *orbis Jovis*, *orbes martis*), tranne *orbis magnus* «orbe magno»; nessun *orbis* nel senso di guscio.

### A.1 Proposizione XXXVIII

**Latino:** *Invenire figuram corporis lunæ.*

**Inglese:** “To find the figure of the moon's body.”

**Scelte.**

- *in partibus & citimis & ultimis* → «nelle parti sia più vicine sia più lontane»; *in partibus & sub luna & lunæ oppositis* → «nelle parti sia sottostanti alla Luna sia opposte alla Luna».
- *gravitas acceleratrix lunæ in terram* → «la gravità acceleratrice della Luna verso la Terra»: è l’accelerazione che la Terra imprime alla Luna, proporzionale alla massa della Terra; il rapporto 39,788 : 1 è quello delle masse della Terra e della Luna della Prop. XXXVII, Cor. 4 (Fascicolo 25a).
- *Talem igitur figuram luna affectat, eamque sub initio induere debuit* → «La Luna, dunque, tende ad assumere una tale figura, e dovette assumerla fin dall’inizio» (§ A.0).
- **Aritmetica:** 39,788 × 100/365 = 10,90, cioè 1090 : 100, non 1081 : 100. Il risultato 93 piedi è coerente con 1081 (8 3/5 × 10,81 = 92,97), non con 1090 (93,75). Cifra segnalata, non corretta (nota N1, § A.7).
- Cor.: *oscillando* → «oscillando»; *ob rationem in prop. xvii allatam* → «per la ragione addotta nella Prop. XVII» (rimando interno verificato, § A.8). *Alterum orbis lunaris umbilicum* → «l’altro fuoco dell’orbita lunare».

### A.2 Lemma I

**Latino:** *Si APEp terram designet uniformiter densam, centroque C & polis P, p & æquatore AE delineatam; & si centro C radio CP describi intelligatur sphæra Pape; sit autem QR planum, cui recta a centro solis ad centrum terræ ducta normaliter insistit; & terræ totius exterioris PapAPepE, quæ sphæra modo descripta altior est, particulæ singulæ conentur recedere hinc inde a plano QR, sitque conatus particulæ cujusque ut ejusdem distantia a plano: Dico primo, quod tota particularum omnium in æquatoris circulo AE, extra globum uniformiter per totum circuitum in morem annuli dispositarum, vis & efficacia ad terram circum centrum ejus rotandam, sit ad totam particularum totidem in æquatoris puncto A, quod a plano QR maxime distat, consistentium vim & efficaciam, ad terram consimili motu circulari circum centrum ejus movendam, ut unum ad duo. Et motus iste circularis circum axem, in communi sectione æquatoris & plani QR jacentem, peragetur.*

**Inglese:** “If APEp represent the earth uniformly dense, marked with the centre C, the poles P, p, and the equator AE; and if about the centre C, with the radius CP, we suppose the sphere Pape to be described, and QR to denote the plane on which a right line, drawn from the centre of the sun to the centre of the earth, insists at right angles; and further suppose that the several particles of the whole exterior earth PapAPepE, without the height of the said sphere, endeavour to recede towards this side and that side from the plane QR, every particle by a force proportional to its distance from that plane; I say, in the first place, that the whole force and efficacy of all the particles that are situate in AE, the circle of the equator, and disposed uniformly without the globe, encompassing the same after the manner of a ring, to wheel the earth about its centre, is to the whole force and efficacy of as many particles in that point A of the equator which is at the greatest distance from the plane QR, to wheel the earth about its centre with a like circular motion, as 1 to 2. And that circular motion will be performed about an axis lying in the common section of the equator and the plane QR.”

**Scelte.**

- *particulæ singulæ conentur recedere hinc inde a plano QR, sitque conatus …* → «tendano ad allontanarsi dal piano QR da una parte e dall’altra, e la tendenza …» (*conatus* «tendenza», glossario).
- *quæ sphæra modo descripta altior est* → «che è più alta della sfera ora descritta»: la parte della Terra che sporge fuori dalla sfera Pape.
- *in morem annuli* → «a modo di anello»; *vis & efficacia* → «la forza e l’efficacia» (§ A.0).
- *semicirculus INLK*: la trascrizione aggiunge al semicerchio la lettera del centro K; Motte ha «INL». Ho conservato la lettura del latino (§ A.7).
- *duplo minor* → «la metà».
- *ut FG×GC ad AH×HC, hoc est, ut FCq ad ACq*: l’uguaglianza dei due rapporti vale se FC e AC si intendono come distanze dall’asse di rotazione, viste nella proiezione sul piano perpendicolare a quell’asse; con questa lettura la frase successiva («la somma di tutti gli FC² sta alla somma di altrettanti AC² … come uno sta a due») è la proposizione dei seni appena dimostrata. Nota N2.
- *per hypothesin* → «per ipotesi», minuscolo: rimanda all’ipotesi interna all’enunciato (la tendenza come la distanza dal piano), non a un’Ipotesi numerata.

### A.3 Lemma II

**Latino:** *Iisdem positis: dico secundo quod vis & efficacia tota particularum omnium extra globum undique sitarum, ad terram circum axem eundem rotandam, sit ad vim totam particularum totidem, in æquatoris circulo AE uniformiter per totum circuitum in morem annuli dispositarum, ad terram consimili motu circulari movendam, ut duo ad quinque.*

**Inglese:** “The same things still supposed, I say, in the second place, that the total force or power of all the particles situated every where about the sphere to turn the earth about the said axis is to the whole force of the like number of particles, uniformly disposed round the whole circumference of the equator AE in the fashion of a ring, to turn the whole earth about with the like circular motion, as 2 to 5.”

**Scelte.**

- *Sit … recta Ll plano Pape paralella*: il «piano Pape» è il piano meridiano della figura, per i poli P, p e per a, e. *Paralella* e *ocurrat* sono refusi della trascrizione (§ A.7).
- *vires contrariæ, ad terram in contrarias partes rotandam* → «le forze contrarie … nel far ruotare la Terra in versi contrari» (glossario: «verso» quando si contrappongono i due versi di un moto).
- Le espressioni con il vinculum sono rese con le parentesi: *NM×MC+mC* → NM×(MC + mC); *IXq in IXq-2CXq* → IX² moltiplicato per (IX² − 2CX²); *ACq-CXq in ACq-3CXq* → (AC² − CX²) moltiplicati per (AC² − 3CX²). Motte conferma la lettura con [SVG 1091] e [SVG 1092] (vinculum su MC + mC).
- *per lem i.* (due volte) → «per il Lemma I»: il primo rimando è alla proposizione preliminare dei seni, il secondo al risultato principale (anello : particelle in A = 1 : 2).
- *quantitas fluens*, *fluxio*, *methodus fluxionum* → § A.0. La sostituzione *si pro CX scribatur tota Cp vel AC* è l’integrazione da 0 al raggio, con il raggio del globo assimilato al semiasse AC (lo schiacciamento è piccolo).

### A.4 Lemma III

**Latino:** *Iisdem positis: dico tertio quod motus terræ totius circum axem jam ante descriptum, ex motibus particularum omnium compositus, erit ad motum annuli prædicti circum axem eundem, in ratione, quæ componitur ex ratione materiæ in terra ad materiam in annulo, & ratione trium quadratorum ex arcu quadrantali circuli cujuscunque ad duo quadrata ex diametro; id est, in ratione materiæ ad materiam & numeri 925275 ad numerum 1000000.*

**Inglese:** “The same things still supposed, I say, in the third place, that the motion of the whole earth about the axis above-named arising from the motions of all the particles, will be to the motion of the aforesaid ring about the same axis in a proportion compounded of the proportion of the matter in the earth to the matter in the ring; and the proportion of three squares of the quadrantal arc of any circle to two squares of its diameter, that is, in the proportion of the matter to the matter, and of the number 925275 to the number 1000000.”

**Scelte.**

- *motus* (grandezza) → «quantità di moto» (Criteri, § A.0, nota N4).
- *ratione trium quadratorum ex arcu quadrantali circuli cujuscunque ad duo quadrata ex diametro* → «dal rapporto di tre quadrati dell’arco quadrantale di un cerchio qualsiasi a due quadrati del diametro»: 3(π/4)²/2 = 3π²/32 = 0,925275.
- *ut quælibet quatuor æqualia quadrata ad tres ex circulis sibi inscriptis* → «come quattro quadrati uguali qualsiasi stanno a tre dei cerchi in essi inscritti». Motte amplia: «three circles inscribed in three of those squares».
- *circunferentia* è una grafia corrente nel latino dell’epoca, non un refuso.

### A.5 Ipotesi II

**Latino:** *Si annulus prædictus terra omni reliqua sublata, solus in orbe terræ, motu annuo circa solem ferretur, & interea circa axem suum, ad planum eclipticæ in angulo graduum 23⁤12 inclinatum, motu diurno revolveretur: idem foret motus punctorum æquinoctialium, sive annulus iste fluidus esset, sive is ex materia rigida & firma constaret.*

**Inglese:** “If the other parts of the earth were taken away, and the remaining ring was carried alone about the sun in the orbit of the earth by the annual motion, while by the diurnal motion it was in the mean time revolved about its own axis inclined to the plane of the ecliptic by an angle of [SVG 1097] degrees, the motion of the equinoctial points would be the same, whether the ring were fluid, or whether it consisted of a hard and rigid matter.”

**Scelte.** L’Ipotesi è un periodo ipotetico al congiuntivo imperfetto (*si … ferretur … idem foret*), reso con il condizionale; non è un enunciato all’infinito. *Ex materia rigida & firma* → «di materia rigida e salda»; Motte inverte e cambia: «hard and rigid».

### A.6 Proposizione XXXIX, Lemma IV, Prop. XL e Lemmi V–XI

**Prop. XXXIX. Latino:** *Invenire præcessionem æquinoctiorum.* **Inglese:** “To find the precession of the equinoxes.”

- *Motus mediocris horarius … erat* → «Il moto orario medio … era»: l’imperfetto rimanda a un valore già trovato (Propp. XXX–XXXIII, Fascicolo 24b; *ob rationes supra explicatas*). Su *mediocris / medius* vedi § A.0.
- *in antecedentia* → «in antecedenza» (contro il verso del moto, glossario).
- *diei siderei … horarum 23. 56′* → «il giorno siderale di 23 ore e 56′»; *dierum 27. 7 hor. 43′* → «di 27 giorni, 7 ore e 43′». I minuti di tempo sono resi con il simbolo ′ come nel testo.
- *(Vid. fig. pag. 474.)* → «(si veda la figura a p. 474)»: la figura del Lemma II. *(id est vires 3IT in fig. pag. 437 & 438)* → «nella figura alle pp. 437 e 438»: la figura della Prop. XXX (verificato sul latino del gruppo G5, § A.8). Motte converte entrambi i rimandi («see fig. Lem. II», «fig. Prop. XXX»).
- *terræ diameter minor PC vel aC … ad semidiametrum majorem AC*: PC è un semidiametro; Newton scrive *diameter*. Traduco come il latino («il diametro minore della Terra, PC o aC»); Motte corregge in «the least semi-diameter».
- *minutorum secundorum plus minus quinquaginta* → «di cinquanta secondi, più o meno».
- *milliaribus … 17 1/6*: nella Prop. XIX l’eccesso è 85472 piedi = 17 1/10 miglia (§ A.7, nota N5).

**Lemma IV. Latino:** *Cometas esse luna superiores & in regione planetarum versari.* **Inglese:** “That the comets are higher than the moon, and in the regions of the planets.”

- Enunciato all’infinito (*Cometas esse … versari*) → indicativo.
- *Ut defectus parallaxeos diurnæ extulit cometas supra regiones sublunares* → «Come la mancanza di parallasse diurna ha innalzato le comete al di sopra delle regioni sublunari». Motte amplia: «placed by astronomers above the moon, because they were found to have no diurnal parallax».
- *si terra vergit ad oppositionem* → «se la Terra volge verso l’opposizione»; Motte aggiunge «heliocentric».
- **Segni.** La trascrizione ha *γQA*, *γQB*, *γQF*, *Tγ*, *gγ*, *γTV*, *γgV*: la γ è la resa del segno dell’Ariete ♈ (lo conferma *Tγ lineam rectam versus principium arietis ductam*, e Motte [SVG 1099]–[SVG 1109] ha Υ). Nella traduzione: ♈. Nota alla prima occorrenza: ♈ = Ariete; «♈QA» è l’angolo fra la direzione del principio dell’Ariete e la direzione della cometa, cioè la longitudine (N6).
- *AG ad AB ut tempus inter observationem primam & ultimam ad tempus inter observationem primam & secundam*: poiché AB : BC stanno come i tempi, è equivalente ad AG : AC come il tempo fra la prima e l’ultima osservazione sta al tempo fra la prima e la terza; lo usa la frase *ag ad ac ut AG ad AC*.
- *capillitium* → «capigliatura»; *tubus opticus* → «tubo ottico»; *globus intermedius* → «globo interno» (§ A.0).
- *ut 1 ad √4 inverse, & 12″ ad 30″ directe*: le luci stanno come 1 a 4 (Saturno quattro volte più luminoso); la distanza sta come il diametro apparente direttamente e come la radice della luce inversamente: (12/30) × √4 = 24/30.
- *Quippe lucidior erat hic cometa altero illo, qui in fine anni præcedentis apparuerat, & cum stellis primæ magnitudinis conferebatur*: il soggetto di *conferebatur* può essere la cometa di aprile o «quell’altra»; l’italiano conserva l’ambiguità; Motte sceglie «that other … had been compared».
- *cometa posterior anni 1665* → «la cometa posteriore dell’anno 1665»: la seconda delle due comete nominate poco prima (quella di aprile 1665, distinta da quella della fine del 1664). Motte omette *posterior*. Per il 1618 e il 1680: *cometæ prioris* «della cometa anteriore» (1618), *cometæ posterioris* «della cometa posteriore» (1680).
- *Jan. 7. Keplerus …*: lo strumento di segmentazione divide dopo «Jan. 7.»; è una sola frase.
- *cedebat ori pegasi* → «era inferiore alla Bocca di Pegaso (*os Pegasi*)».
- *nisi quatenus* → «se non in quanto» (glossario).
- *proculdubio dubio* (Cor. 2) è una duplicazione della trascrizione; *proprior* è refuso per *propior* (§ A.7).
- Nomi: *Flamstedius* = John Flamsteed; *Hevelius* = Johannes Hevelius; *Cysatus* = Johann Baptist Cysat; *Keplerus* = Johannes Kepler, «Keplero» (identificazioni non verificate sulle fonti allegate).

**Prop. XL. Latino:** *Cometas in sectionibus conicis umbilicos in centro solis habentibus moveri, & radiis ad solem ductis areas temporibus proportionales describere.* **Inglese:** “That the comets move in some of the conic sections, having their foci in the centre of the sun; and by radii drawn to the sun describe areas proportional to the times.”

- Enunciato all’infinito → indicativo. *umbilicos in centro solis habentibus* → «che hanno i fuochi nel centro del Sole».
- Cor. 1: *ut √4 (seu 8) ad 1*: la trascrizione ha perso l’esponente (√4 = 2); il senso richiede la potenza 3/2 di 4 (rapporto sesquiplicato), cioè 8. Rendo «√(4³) (ossia 8)», dichiarando la ricostruzione; Motte [SVG 1111] ha 4√4, che vale ugualmente 8 (§ A.7).
- Cor. 3: *in subduplicata ratione duplæ distantiæ planetæ a centro solis, ad distantiam cometæ a centro solis quamproxime* → «con ottima approssimazione, in rapporto subduplicato del doppio della distanza del pianeta dal centro del Sole alla distanza della cometa dal centro del Sole». Motte aggiunge «supposed to be revolved at the same distance», che contraddice la formula (le distanze sono due), e raddoppia «nearly … very nearly».
- Cor. 3: *motu suo diurno mediocri* → «con il suo moto diurno medio»; *telluris* → «della Terra».
- Cor. 4: *erit area diurna & horaria major vel minor in eadem ratione subduplicata* → «sarà maggiore o minore nello stesso rapporto subduplicato». Motte: «less or greater in the subduplicate of the same proportion reciprocally», che **inverte** il senso: l’area descritta in un tempo dato cresce come la radice del lato retto (Prop. XIV del Libro I).

**Lemma V. Latino:** *Invenire lineam curvam generis parabolici, quæ per data quotcunque puncta transibit.* **Inglese:** “To find a curve line of the parabolic kind which shall pass through any given number of points.”

- *demitte*, *collige*, *pone*, *dic* sono imperativi di seconda persona: conservati («abbassa», «raccogli», «poni», «di’»).
- *b, 2b, 3b …* sono nomi dei termini successivi della serie delle differenze, non multipli di b; la trascrizione inserisce un segno di moltiplicazione invisibile (2⁢b) che va ignorato (nota N7).
- *12⁢p in -IS=q* → «½p moltiplicato per −IS = q» (e così ⅓q, ¼r, ⅕s); *b=AH-BIHI* → b = (AH − BI)/HI (frazione appiattita).
- *DL+EM=4b, -EM+FN=5b*: i segni presuppongono che E ed F stiano sotto la retta HN; il latino e Motte concordano.
- *ordinatim applicata* → «ordinata» (glossario).

**Lemma VI. Latino:** *Ex observatis aliquot locis cometæ invenire locum ejus ad tempus quodvis intermedium datum.* **Inglese:** “Certain observed places of a comet being given, to find the place of the same to any intermediate given time.”

- *(in fig. præced.)* → «(nella figura precedente)», cioè quella del Lemma V.

**Lemma VII. Latino:** *Per datum punctum P ducere rectam lineam BC, cujus partes PB, PC, rectis duabus positione datis AB, AC abscissæ, datam habeant rationem ad invicem.* **Inglese:** “Through a given point P to draw a right line BC, whose parts PB, PC, cut off by two right lines AB, AC, given in position, may be one to the other in a given proportion.”

- *producatur eadem versus rectam alteram AC usque ad E*: E sta sul prolungamento di DP oltre P, dalla parte di AC, non necessariamente su AC.

**Lemma VIII. Latino:** *Sit ABC parabola umbilicum habens S. Chorda AC bisecta [FIG] in I abscindatur segmentum ABCI, cujus diameter sit <489> Iμ & vertex μ. In Iμ producta capiatur μO æqualis dimidio ipsius Iμ. Jungatur OS, & producatur ea ad ξ, ut sit Sξ æqualis 2⁢SO. Et si cometa B moveatur in arcu CBA, & agatur ξB secans AC in E: dico quod punctum E abscindet de chorda AC segmentum AE tempori proportionale quamproxime.* **Inglese:** “Let ABC be a parabola, having its focus in S. By the chord AC bisected in I cut off the segment ABCI, whose diameter is [SVG 1133] and vertex [SVG 1134] . In [SVG 1133] produced take [SVG 1135] equal to one half of [SVG 1133] . Join OS, and produce it to [SVG 1136] as [SVG 1137] may be equal to 2SO. Now, supposing a comet to revolve in the arc CBA, draw [SVG 1138] , cutting AC in E; I say, the point E will cut off from the chord AC the segment AE, nearly proportional to the time.”

- *cujus diameter sit Iμ & vertex μ*: il «diametro» del segmento è la retta per I parallela all’asse; μ è il punto in cui incontra la parabola, dove la tangente è parallela ad AC.
- *Scholium*: *ξn quæ sit ad μB ut 27MI ad 16Mμ*. M non è definito nel Lemma VIII; compare nei Lemmi IX–X (μM = Iμ; il rettangolo formato da AC e SM). La lettura coerente con quei lemmi è M = intersezione di Sμ con AC. Con questa lettura la verifica numerica conferma la regola del verso, ma non il coefficiente 27 (nota N8).

**Lemma IX. Latino:** *Rectæ Iμ & μM & longitudo AIC4⁢Sμ æquantur inter se.* **Inglese:** “The right lines [SVG 1153] and [SVG 1154] , and the length [SVG 1155] , are equal among themselves.”

- *longitudo AIC4⁢Sμ*: «AIC» è refuso della trascrizione per «AIq» (AI²): lo richiedono il Lemma XI (*AIq4⁢Sμ*), la proprietà della parabola (AI² = 4Sμ × Iμ) e Motte [SVG 1155]. Rendo AI²/4Sμ (§ A.7).

**Lemma X. Latino:** *Si producatur Sμ ad N & P, ut μN sit pars tertia ipsius μI, & SP sit ad SN ut SN ad Sμ. Cometa, quo tempore describit arcum AμC, si progrederetur ea semper cum velocitate quam habet in altitudine ipsi SP æquali, describeret longitudinem æqualem chordæ AC.* **Inglese:** “Produce [SVG 1157] to N and P, so as [SVG 1158] may be one third of [SVG 1159] , and SP may be to SN as SN to [SVG 1160] ; and in the time that a comet would describe the arc [SVG 1161] , if it was supposed to move always forwards with the velocity which it hath in a height equal to SP, it would describe a length equal to the chord AC.”

- *in altitudine ipsi SP æquali* → «all’altezza uguale a SP» (§ A.0, *altitudo*).
- *contentum sub longitudine … & longitudine Sμ* → «il rettangolo formato dalla lunghezza … e dalla lunghezza Sμ».
- *Sμ+23⁢Iμ* (Cor.) → Sμ + ⅔Iμ; Motte [SVG 1163] concorda.

**Lemma XI. Latino:** *Si cometa motu omni privatus de altitudine SN seu Sμ+13⁢Iμ demitteretur, ut caderet in solem, & ea semper vi uniformiter continuata urgeretur in solem, qua urgetur sub initio; idem semisse temporis, quo in orbe suo describat arcum AC, descensu suo describeret spatium longitudini Iμ æquale.* **Inglese:** “If a comet void of all motion was let fall from the height SN, or [SVG 1164] , towards the sun, and was still impelled to the sun by the same force uniformly continued by which it was impelled at first, the same, in one half of that time in which it might describe the arc AC in its own orbit, would, in descending describe a space equal to the length [SVG 1153] .”

- *Sμ+13⁢Iμ* → Sμ + ⅓Iμ, coerente con SN = Sμ + μN e μN = ⅓μI (Lemma X). **Motte [SVG 1164] ha Sμ + ⅔Iμ**: errore dell’edizione 1846 o della sua resa digitale (§ A.9).
- *applicato ad quadruplum altitudinis SP* → «diviso per il quadruplo dell’altezza SP» (glossario, *applicare ad*).
- *per corol. 9. prop. iv. lib. i.* → «per il Cor. 9 della Prop. IV del Libro I»; Motte «Cor. 9, Prop. XVI, Book I» (§ A.8).
- *unitatis ad binarium* → «dell’unità al due».

### A.7 Refusi e anomalie della trascrizione

| Luogo | Trascrizione | Lettura | Tipo |
|---|---|---|---|
| III.G6.45 | *seu 1081 ad 100* | — (lettura conservata) | 39,788 × 100/365 dà 1090 : 100; il 93 seguente è coerente con 1081; da controllare sulla stampa |
| III.G6.48 | *semicirculus INLK* | *INL* (Motte) | lettera del centro aggiunta; forse della stampa |
| III.G6.52 | *paralella*; *ocurrat*; *Æquatori* | *parallela*; *occurrat*; *æquatori* | refusi probabili / maiuscola |
| III.G6.52 | *NM×MC+mC* | NM×(MC + mC) | vinculum perduto (Motte [SVG 1091]–[SVG 1092]) |
| III.G6.53 | *ACqq×CX-43⁢ACq×CXcub+35⁢CXqc*; *415⁢ACqc*; *23⁢ACqc* | AC⁴×CX − 4/3 AC²×CX³ + 3/5 CX⁵; 4/15 AC⁵; 2/3 AC⁵ | frazioni appiattite (Motte [SVG 1093]–[SVG 1096]) |
| III.G6.53 | *Q. E. D.* | *Q.E.D.* | spaziatura |
| III.G6.56, III.G6.60 | *23⁤12* | 23 1/2 | numero misto appiattito (Motte [SVG 1097]) |
| III.G6.58 | *nodi LLunæ* | *lunæ* | refuso (lettera doppia) |
| III.G6.58 | *lunæ illaeæ* | *illæ* | refuso |
| III.G6.59 | *ut aCqu. ad >ACqu.-aCqu.* | aC² ad AC² − aC² | segno «>» spurio |
| III.G6.59 | *terræ diameter minor PC* | (semidiametro) | imprecisione di Newton, non della trascrizione; Motte corregge |
| III.G6.61 | *æquinoctiourum*; *astronimicis* | *æquinoctiorum*; *astronomicis* | refusi |
| III.G6.62 | *milliaribus … 17⁤16* | 17 1/6 | numero misto; Motte [SVG 1098] = 17 1/6; ma la Prop. XIX ha 17 1/10 (85472 piedi) |
| III.G6.66–III.G6.67 | *γQA*, *Tγ*, *γgV* … | ♈QA, T♈, ♈gV | segno dell’Ariete reso con γ |
| III.G6.70 | *soli multo proprior* | *propior* | refuso probabile |
| III.G6.71 | *Jan. 7.* / *Keplerus …* | una sola frase | segmentazione |
| III.G6.73 | *proculdubio dubio* | *proculdubio* | parola duplicata |
| III.G6.77 | *ut √4 (seu 8) ad 1* | √(4³), cioè 8 (Motte: 4√4) | esponente perduto |
| III.G6.79–III.G6.80 | *71675⁤12*, *101364⁤12*, *1216373⁤12*, *50682⁤14* | 71675 1/2, 101364 1/2, 1216373 1/2, 50682 1/4 | numeri misti appiattiti |
| III.G6.83–III.G6.84 | *2⁢b*, *12⁢p in -IS*, *b=AH-BIHI* | 2b (indice), ½p × (−IS), (AH − BI)/HI | segno di prodotto invisibile; frazioni appiattite |
| III.G6.96 | *AIC4⁢Sμ* | AI²/4Sμ | refuso «AIC» per «AIq» (Motte [SVG 1155]) |
| III.G6.100; III.G6.101 | *Sμ+23⁢Iμ*; *Sμ+13⁢Iμ* | Sμ + ⅔Iμ; Sμ + ⅓Iμ | frazioni appiattite |

Nessuno di questi punti è stato verificato sulla stampa del 1726. La traduzione segue il senso; la Parte B riporta il latino esatto della trascrizione.

**Punti da controllare sulla stampa ECCO.**

| Pagina 1726 | Trascrizione | Lettura attesa | Motivo |
|---|---|---|---|
| p. 471 | *seu 1081 ad 100* | 1081 o 1090? | il prodotto 39,788 × 100/365 dà 1090,1 : 100; il 93 è coerente con 1081: verificare se la stampa ha un altro dato (39,788? 365?) |
| p. 472 | *semicirculus INLK* | *INL* | K è il centro; Motte ha INL |
| p. 473 | *paralella*, *ocurrat* | *parallela*, *occurrat* | grafie anomale |
| p. 476 | *LLunæ*, *illaeæ*, *>ACqu.* | *Lunæ*, *illæ*, *ACqu.* | refusi della trascrizione |
| p. 477 | *æquinoctiourum*, *astronimicis* | *æquinoctiorum*, *astronomicis* | refusi |
| p. 477 | *17⁤16* | 17 1/6 | la Prop. XIX (1726, p. 415) ha 17 1/10; controllare se la stampa del 1726 ha davvero 1/6 |
| p. 478 sgg. | *γ* | ♈ | il segno dell’Ariete nella stampa |
| p. 482 | *proprior* | *propior* | refuso probabile |
| p. 484 | *proculdubio dubio* | *proculdubio* | duplicazione |
| p. 485 | *√4 (seu 8)* | √4³ o 4√4 | forma della formula nella stampa |
| p. 489 | *27⁢MI ad 16⁢Mμ* | — | la verifica numerica (N8) dà 12 al posto di 27 con M = Sμ ∩ AC: controllare cifre e lettere, e la figura |
| p. 490 | *AIC4⁢Sμ* | AIq/4Sμ | refuso della trascrizione |

### A.8 Rimandi

**Rimandi ai Libri I e II** (verificati sui fascicoli in `traduzione/`):

| Luogo | Latino | Enunciato citato | Esito |
|---|---|---|---|
| III.G6.58 | *per corol. 16. prop. lxvi. Lib. i.* | Fasc. 10, S11.55: i moti medi dell’auge e dei nodi, **in ciascuna rivoluzione** del corpo P, stanno come il quadrato del suo tempo periodico | **regge**: per anno (numero di rivoluzioni ∝ 1/T) i moti stanno come T, che è ciò che Newton usa (*forent ut tempora periodica*) |
| III.G6.76 | *per corol. 1. prop. xiii. libri primi* | Fasc. 6, S3.22: con forza inversamente come il quadrato della distanza il corpo si muove in una sezione conica con il fuoco nel centro delle forze | regge |
| III.G6.79 | *per corol. 7. prop. xvi. lib. i.* | Fasc. 6, S3.38: nella parabola v : v(cerchio alla stessa distanza) = √2 : 1; in generale uguale alla velocità in un cerchio a metà distanza | regge (con il Cor. 6 della Prop. IV per distanze diverse, che Newton non cita) |
| III.G6.99 | *per corol. 6 prop. xvi. lib. i.* | Fasc. 6, S3.37: nella parabola la velocità è inversamente in rapporto subduplicato della distanza dal fuoco | regge |
| III.G6.102 | *per corol. 7. prop. xvi. lib. i.* | Fasc. 6, S3.38 (√2 : 1) | regge: l’arco nel cerchio di raggio SP sta alla corda AC come 1 a √2 |
| III.G6.102 | *per corol. 9. prop. iv. lib. i.* | Fasc. 5, S2.32: l’arco descritto nel cerchio in un tempo qualsiasi è medio proporzionale fra il diametro e la caduta nello stesso tempo con la stessa forza | **regge** (ricalcolo: AI²/4SP, nota N9). **Motte** scrive «Cor. 9, Prop. XVI, Book I»: il Cor. 9 della Prop. XVI (Fasc. 6, S3.40) riguarda le velocità nelle coniche e non dà il risultato; errore di Motte o dell’edizione 1846 |

Rimandi ai Libri I e II: 6, tutti reggono; nessun rimando al Libro II.

**Rimandi interni al Libro III** (verificati sul latino degli altri gruppi):

| Luogo | Latino | Verifica |
|---|---|---|
| III.G6.46 | *ob rationem in prop. xvii allatam* | Prop. XVII (gruppo G3): la faccia della Luna guarda «il fuoco più lontano dell’orbita» (*ulteriorem umbilicum orbis ejus*), da cui la librazione in longitudine. Regge |
| III.G6.52–III.G6.53 | *per lem i.* | Lemma I di questo fascicolo. Regge |
| III.G6.58 | *ob rationes supra explicatas* | Propp. XXX–XXXIII (Fasc. 24b): il moto medio dei nodi vale la metà del moto nelle quadrature. Non ricontrollato nei numeri (fuori perimetro) |
| III.G6.59 | *per hujus lem. iii.*; *per lem. ii.* | Lemmi III e II di questo fascicolo. Reggono |
| III.G6.59 | *Vid. fig. pag. 474.* | p. 474 è nel Lemma II, la cui figura contiene PapAPepE. Regge |
| III.G6.59 | *vires 3IT in fig. pag. 437 & 438* | Prop. XXX (gruppo G5) comincia a p. 437; le forze «3IT» (= 3PK) vi compaiono. Regge |
| III.G6.61 | *Vis … lunæ ad mare movendum erat ad vim solis, ut 4,4815 ad 1* | Prop. XXXVII, Cor. 3 (gruppo G6, Fasc. 25a): 4,4815 : 1. Regge |
| III.G6.62 | 17 1/6 miglia | Prop. XIX (gruppo G3): 85472 piedi, «seu milliarium 17 1/10». **Non torna** (§ A.7) |
| III.G6.76 | *prop. viii, xii, & xiii. libri tertii* | Prop. VIII (peso inversamente come il quadrato della distanza fra i centri), XII (il Sole si muove poco intorno al centro comune di gravità), XIII (i pianeti in ellissi con il fuoco nel centro del Sole, legge delle aree). Reggono |
| III.G6.87 | *per lemma superius*; *in fig. præced.* | Lemma V. Regge |
| III.G6.102 | *per lemma novissimum* | Lemma X. Regge |

### A.9 Riepilogo: dove Motte aggiunge, omette o sbaglia

| Luogo | Latino | Motte 1846 | Tipo |
|---|---|---|---|
| III.G6.46 | *oscillando*, *oscillationes* | «libratory motion», «librations» | termine interpretativo |
| III.G6.48 | *INLK* | «INL» | lettera diversa |
| III.G6.55 | *tres ex circulis sibi inscriptis* | «three circles inscribed in three of those squares» | ampliamento |
| III.G6.56 | *rigida & firma* | «hard and rigid» | resa diversa |
| III.G6.58 | *motus mediocris / medius* | «middle / mean» | distinzione conservata (l’italiano la affida al contesto) |
| III.G6.59 | *diameter minor PC* | «least semi-diameter» | correzione tacita |
| III.G6.59 | *Vid. fig. pag. 474.*; *fig. pag. 437 & 438* | «see fig. Lem. II»; «fig. Prop. XXX» | rimandi convertiti |
| III.G6.65 | *Ut defectus parallaxeos diurnæ extulit cometas* | «placed by astronomers above the moon, because they were found to have no diurnal parallax» | ampliamento |
| III.G6.65 | *ad oppositionem* | «to a heliocentric opposition with them» | aggiunta |
| III.G6.69 | *minima capillitii … diameter … 2′. 0″* | «the least diameter of its head, 2' 00» | *capillitium* → «head»; manca il segno dei secondi |
| III.G6.69 | *Latitudo capillitii* | «The diameter of its head» | resa diversa |
| III.G6.70 | *ex reflexione fumi* | «the sun’s light reflected by a smoke» | esplicitazione |
| III.G6.71 | *cometa posterior anni 1665* | «the comet of the year 1665» | omissione di *posterior* |
| III.G6.71 | *ante duas fere septimanas* | «two weeks before» | omissione di *fere* |
| III.G6.73 | *cur cometæ tantopere frequentant regionem solis* | «why comets are so frequently seen in that hemisphere in which the sun is, and so seldom in the other» | ampliamento |
| III.G6.73 | *Spatii … circa solem descripti* | «that spherical space» | aggiunta |
| III.G6.79 | *velocitatem planetæ cujusvis circa solem in circulo revolventis* | «… supposed to be revolved at the same distance in a circle» | **aggiunta errata** (la formula confronta distanze diverse) |
| III.G6.79 | *quamproxime* (una volta) | «nearly … very nearly» | ripetizione |
| III.G6.80 | *major vel minor in eadem ratione subduplicata* | «less or greater in the subduplicate of the same proportion reciprocally» | **errore di senso** (rapporto invertito) |
| III.G6.83, III.G6.84 | *Cas. 1.*, *Cas. 2.* | «CASE 1.», «CASE 2.» | — |
| III.G6.101 | *Sμ+13⁢Iμ* | [SVG 1164] = Sμ + ⅔Iμ | **formula errata** |
| III.G6.102 | *per corol. 9. prop. iv. lib. i.* | «by Cor. 9, Prop. XVI, Book I» | **rimando errato** |

Altrove le lettere delle figure e i numeri di Motte coincidono con il latino (39,788; 1081; 93; 186; tutti i valori della Prop. XXXIX; 1682, 1665, 1683, 1618, 1680 e le date; 1720212, 2432747; 27MI e 16Mμ).

**SVG di Motte che non tornano con il latino.** Ho controllato il LaTeX di tutte le 76 formule del perimetro ([SVG 1012] e [SVG 1091]–[SVG 1165]) contro il latino. Tornano tutte tranne quelle in tabella.

| SVG | LaTeX | Lettura attesa | Commento |
|---|---|---|---|
| 1164 | `\mathrm{S} \mu + \tfrac{2}{3} \mathrm{I} \mu` | Sμ + ⅓Iμ | Lemma XI: SN = Sμ + μN, μN = ⅓Iμ (Lemma X); il latino ha 1/3. Probabile contaminazione con [SVG 1163] (Cor. del Lemma X, dove ⅔ è giusto) |
| 1139, 1140 | `mu \mathrm X`, `mu` | μX, μ | difetto del LaTeX dell’EPUB (manca la barra rovescia): nell’immagine si leggerà «mu»; non visto |
| 1111 | `4\sqrt{4}` | √(4³) | equivalente (= 8); qui è la trascrizione latina a essere difettosa |
| 1155 | `\dfrac{\mathrm{AI}^{2}}{4 \mathrm{S} \mu}` | AI²/4Sμ | giusto: conferma il refuso «AIC» della trascrizione |

---

## Note editoriali e fisiche

Queste note sono aggiunte del presente fascicolo, non affermazioni tradotte da Newton. Le verifiche numeriche sono state eseguite con script Python (`tmp/25b/verifica.py`, `lemma2.py`, `scolio_test.py`), che ricostruiscono ogni costruzione su figure di prova senza usare il risultato da verificare. Ciò che proviene da conoscenza generale e non dalle fonti allegate è marcato «(non verificato sulle fonti allegate)».

### N1. Prop. XXXVIII: il conto della figura lunare

Newton compone due rapporti: le gravità acceleratrici (cioè le masse, 39,788 : 1, dalla Prop. XXXVII, Cor. 4) e i diametri (100 : 365, dallo stesso corollario). Il prodotto è 39,788 × 100/365 = **10,9008**, cioè **1090 : 100**, non 1081 : 100. Il seguito è invece coerente con 1081: 8 3/5 × 10,81 = 92,97 ≈ 93 piedi (con 10,90 si avrebbe 93,75), ed è giusto 2 × 93 = 186. Il valore 8 3/5 piedi è l’arrotondamento degli «otto piedi e 7 5/22 pollici» della Prop. XXXVII, Cor. 1 (8,60 piedi). La cifra non è corretta nel testo; può trattarsi di un residuo di un dato diverso (non verificato sulle fonti allegate) ed è nei «Punti da controllare» (§ A.7).

In termini moderni la proposizione è una stima del rigonfiamento di marea permanente della Luna e il corollario descrive la rotazione sincrona (la Luna rivolge alla Terra sempre la stessa faccia, con piccole librazioni). Il calcolo di Newton scala le altezze delle maree con il solo rapporto delle forze, senza tener conto della diversa gravità superficiale della Luna; e il rapporto delle masse 39,788 è circa la metà del valore moderno, circa 81,3 (entrambe le osservazioni: non verificato sulle fonti allegate).

### N2. Lemma I: la somma dei quadrati dei seni

La prima parte del lemma è la proposizione che la media di sen² su una semicirconferenza è ½: ΣNM² + ΣKM² = ΣKN², e per simmetria ΣNM² = ΣKM². Per applicarla Newton deve intendere FC come la **distanza della particella F dall’asse di rotazione** (la retta comune all’equatore e al piano QR), vista nella proiezione sul piano perpendicolare a quell’asse. Se l’equatore è inclinato dell’angolo α sul piano QR e la particella F dista *d* dall’asse, allora FG = *d* sen α e GC = *d* cos α, e FG × GC : AH × HC = *d*² : AC², come scrive Newton. L’«efficacia» FG × CG è ciò che oggi si chiama **momento** della forza rispetto all’asse.

**Verifica** (200 000 particelle sull’equatore, α = 23,5°): efficacia dell’anello / efficacia delle stesse particelle in A = **0,500000**.

### N3. Lemma II: il fattore 2/5

Newton divide il diametro polare in parti uguali, dà a ogni cerchio IK la materia IX² (è la distribuzione dell’eccesso di uno sferoide omogeneo poco schiacciato sulla sfera interna) e integra con il metodo delle flussioni: ∫₀^AC (AC² − CX²)(AC² − 3CX²) d(CX) = 4/15 AC⁵ e ∫₀^AC (AC² − CX²) AC² d(CX) = 2/3 AC⁵, il cui rapporto è 2/5.

**Verifica indipendente:** integrazione numerica diretta della coppia esercitata da una forza proporzionale alla distanza dal piano QR (inclinato di 23,5°) sul guscio compreso fra uno sferoide omogeneo e la sfera inscritta, confrontata con quella di un anello equatoriale della stessa massa: **0,400000** per schiacciamenti 1/100, 1/1000 e 1/10 000. In termini moderni il rapporto è quello delle differenze dei momenti d’inerzia (*C* − *A*) del guscio e dell’anello.

### N4. Lemma III e il «moto» della Terra

Nel Lemma III *motus* è una grandezza: la somma delle **quantità di moto** delle particelle (massa × velocità, sommate in valore assoluto), non il momento angolare. Lo mostrano i tre rapporti della dimostrazione, che ho ricalcolato:

| Confronto | Newton | Ricalcolo (media di *r*⊥ per unità di massa) |
|---|---|---|
| cilindro : sfera inscritta | 4 quadrati : 3 cerchi = 16 : 3π | cilindro 2/3 *R* × *M*cil; sfera 3π/16 *R* × *M*sf con *M*sf = 2/3 *M*cil: rapporto 16/(3π) = 1,6977 |
| cilindro : anello all’equatore | 2 *M*cil : 3 *M*an | 2/3 *R* *M*cil : *R* *M*an |
| anello attorno all’asse : attorno al diametro | circonferenza : 2 diametri = π : 2 | 1 : 2/π |
| **sfera : anello attorno al diametro** | 3 (π/4)² : 2 = **0,925275** | 3π/16 : 2/π = 3π²/32 = 0,9252754 (Monte Carlo 0,9246) |

L’aritmetica è dunque corretta. Nella Prop. XXXIX Newton usa questo rapporto per ripartire il «moto» fra l’anello e il globo. In meccanica moderna la grandezza che si conserva e che governa la velocità della precessione è il momento angolare, cioè il momento d’inerzia: con i momenti d’inerzia il rapporto sfera : anello (stessa massa, attorno a un diametro) sarebbe 2/5 : 1/2 = **0,8** invece di 0,925. Rifacendo la catena della Prop. XXXIX con 0,8 il fattore dell’anello passa da 4590/489813 = 0,009371 a 0,010822 (+15,5 %). È un mio ricalcolo; che questo sia uno dei punti deboli della teoria newtoniana della precessione è una valutazione storica non verificata sulle fonti allegate.

L’**Ipotesi II** (anello fluido o rigido, stesso moto dei punti equinoziali) è un’assunzione senza dimostrazione: serve a passare dall’anello di lune della Prop. XXXIX, i cui nodi si conoscono dalla teoria lunare, all’anello rigido della Terra.

### N5. Prop. XXXIX: la catena dei numeri

Ricalcolo passo per passo (`verifica.py`):

| Passo | Newton | Ricalcolo |
|---|---|---|
| metà di 16″ 35‴ 16ⁱᵛ 36ᵛ | 8″ 17‴ 38ⁱᵛ 18ᵛ | 8″ 17‴ 38ⁱᵛ 18ᵛ |
| × ore dell’anno siderale (365 g 6 h 9 m = 8766,15 h) | 20° 11′ 46″ | 20° 11′ 46,2″ |
| giorno siderale : mese siderale | 1436 : 39343 | 23 h 56′ = 1436′; 27 g 7 h 43′ = 39343′ |
| globo : guscio (229 : 230) | 52441 : 459 | 229² = 52441; 230² − 229² = 459 |
| 459/52441 × 1000000/925275 | 4590 : 485223 | 4590 : 485223,46 |
| anello : anello + globo | 4590 : 489813 | 4590 + 485223 = 489813 |
| 1436/39343 × 4590/489813 | 100 : 292369 | 100 : 292368,6 |
| × 2/5 | 10 : 73092 | 10 : 73092,1 |
| 20° 11′ 46″ = 72706″ × 10/73092 | 9″ 56‴ 50ⁱᵛ | 9″ 56‴ 49,9ⁱᵛ |
| × 0,91706 | 9″ 7‴ 20ⁱᵛ | 9″ 7‴ 19,8ⁱᵛ (cos 23,5° = 0,917060) |
| × 4,4815 | 40″ 52‴ 52ⁱᵛ | 40″ 52‴ 52,5ⁱᵛ |
| somma | 50″ 00‴ 12ⁱᵛ | 50″ 00‴ 12,0ⁱᵛ |

Tutti i passaggi tornano entro l’arrotondamento dell’ultima cifra.

**Due dati da segnalare.** (1) Le 17 1/6 miglia dell’ultimo capoverso non coincidono con l’eccesso della Prop. XIX, 85472 piedi = 17,09 miglia, che Newton scrive «17 1/10»; anche Motte ha 17 1/6 (§ A.7). (2) Il 4,4815 (forza della Luna : forza del Sole) viene dalla Prop. XXXVII; il valore moderno è circa 2,2, e la precessione annua osservata è circa 50,3″ (non verificato sulle fonti allegate). L’accordo finale con «cinquanta secondi, più o meno» nasce quindi da valori che, presi uno per uno, si scostano da quelli moderni (N4; valutazione non verificata sulle fonti allegate).

### N6. Lemma IV: parallasse, luce e code

**Simboli.** ♈ = Ariete. «♈QA» è l’angolo, contato dal principio dell’Ariete (il punto equinoziale di primavera), della direzione in cui la cometa è vista da Q: è la sua longitudine eclittica. Nella trascrizione il segno è reso «γ».

**Costruzione.** La prima figura usa i tempi delle tre prime osservazioni per tracciare, con la costruzione del Lemma VII, la retta ABC su cui la cometa «sembrerebbe» muoversi uniformemente; G è il luogo estrapolato all’ultima osservazione. La seconda figura sostituisce alla Terra vera, al tempo dell’ultima osservazione, il punto g che essa avrebbe raggiunto proseguendo uniformemente lungo la corda ac; da g la cometa si vedrebbe nella direzione ♈QG, dalla Terra vera T nella direzione ♈QF; le due rette si incontrano nel luogo V della cometa.

**Verifica su una figura di prova** (Terra su un’orbita circolare di raggio 1, cometa in moto rettilineo uniforme a 2,3–2,9 unità dal Sole, tempi 0, 4, 8, 60 giorni e altri):

- se la Terra, durante le prime tre osservazioni, si muove davvero uniformemente in linea retta (l’ipotesi del testo), V coincide con il luogo vero della cometa (scarto < 10⁻³); la parallasse FQG risulta di 1,8°–7,4°;
- se le prime tre osservazioni si fanno dalla Terra sull’orbita circolare, la costruzione diventa molto instabile: nei miei esempi V cade a 0,8–3,4 unità dal luogo vero. La ragione è che la curvatura dell’orbita terrestre in pochi giorni altera la «seconda differenza» delle tre direzioni osservate, che è proprio ciò che determina la retta ABC.

La costruzione è dunque esatta nelle sue ipotesi e, applicata a dati reali, va presa come stima qualitativa: è l’uso che ne fa Newton («Questo luogo V suole poi trovarsi al di sotto dell’orbita di Giove»), mentre la determinazione vera delle orbite è affidata ai Lemmi V–XI e alla Prop. XLI. L’instabilità numerica è un risultato del mio modello di prova, da riesaminare.

**Fotometria.** Lo splendore di un corpo illuminato dal Sole va come 1/(*r*²Δ²) (distanza dal Sole *r*, dalla Terra Δ); Newton pone *r* e Δ crescenti insieme, da cui il «rapporto quadruplicato». A diametro apparente dato, la distanza sta come il diametro direttamente e come la radice della luce inversamente. Verifica: 21″ × √2 = 29,7″ ≈ 30″ (globo e anello di Saturno di uguale luce); distanza cometa : Saturno = (12/30) × √4 = 0,8 = 4 : 5.

**Identificazioni** (non verificate sulle fonti allegate): la cometa del 1682 è quella che oggi porta il nome di Halley; la «Bocca di Pegaso» è la stella Enif (ε Pegasi); *toto cœlo errare* è un modo di dire latino per «sbagliare completamente», qui con un gioco di parole voluto. La «capigliatura» (*capillitium*) è ciò che oggi si chiama chioma della cometa.

### N7. Lemma V: le differenze divise di Newton

Il Lemma V è la formula d’interpolazione di Newton. Nel Caso 2, b, c, d… sono le differenze divise (con il segno cambiato a ogni ordine, compensato dai segni di p, q, r…); nel Caso 1 le differenze non sono divise e i fattori ½, ⅓, ¼… le dividono per k!. Le scritture «2b», «3b», «2c» sono **etichette** (il secondo, il terzo termine della serie), non prodotti.

**Verifica:** per sei punti con ascisse equidistanti (E ed F sotto la retta, come nel testo) e per sei punti con ascisse casuali, l’ordinata RS calcolata con le regole di Newton coincide con il polinomio interpolatore di Lagrange (scarto massimo 5·10⁻¹⁵ e 1·10⁻¹³). Corollario: l’area sotto 1/(1 + *x*) fra 0 e 2 è ln 3 = 1,09861; la «parabola» per cinque punti dà 1,09926. Il nome moderno («formula d’interpolazione di Newton», da cui le regole di quadratura di Newton–Cotes) non è verificato sulle fonti allegate.

### N8. Lemma VIII e il suo Scolio

**Verifica** (parabola con fuoco S nell’origine, distanza perielica 1; tempo dalla legge delle aree, cioè dall’area spazzata dal fuoco):

| Arco AC (anomalie) | B | AE/AC | tempo | scarto |
|---|---|---|---|---|
| −40° … 50° | −22° / 5° / 32° | 0,20824 / 0,48143 / 0,76621 | 0,20816 / 0,48143 / 0,76651 | +0,00008 / 0,00000 / −0,00031 |
| 20° … 100° | 36° / 60° / 84° | 0,09895 / 0,29342 / 0,61095 | 0,10027 / 0,29366 / 0,61197 | −0,00131 / −0,00025 / −0,00103 |
| −100° … −30° | −86° / −65° / −44° | 0,37414 / 0,69719 / 0,89866 | 0,37334 / 0,69702 / 0,89765 | +0,00080 / +0,00017 / +0,00101 |

Lo scarto è al massimo dell’ordine di un millesimo della corda anche su archi di 70°–90°; quando B coincide con μ è nullo (10⁻¹⁶), come dice il Corollario. Sono state verificate anche le proprietà usate nella dimostrazione: ξO : SO = 3 : 1, EO : XO = 3 : 1 e SX ∥ EB (scarti 10⁻¹⁵).

**Lo Scolio.** Con M = intersezione di Sμ con AC (la lettura richiesta dai Lemmi IX–X) ho calcolato, per molti punti B, la posizione di n che renderebbe esatta la divisione della corda. Risultati:

- la **regola del verso** è confermata in tutti i casi: n cade oltre ξ quando B è più lontano di μ dal vertice principale, al di qua quando è più vicino;
- la **lunghezza** ξn necessaria è, per archi piccoli, proporzionale a μB con coefficiente **0,75 · MI/Mμ = 12MI : 16Mμ**, quasi indipendente dalla posizione dell’arco (archi di 4°–10° con anomalia media da 15° a 82°: da 0,40 a 0,48 volte il coefficiente di Newton, 0,44 nella maggior parte dei casi). Con il coefficiente del testo, 27MI : 16Mμ, la correzione eccede di circa 2,25 volte, e su archi grandi l’errore può crescere invece di diminuire.

Non correggo il testo: la discrepanza può dipendere da una lettura diversa di M o di μB nella figura originale, o da un errore di stampa (27 per 12?); va controllata sulla stampa e sulla figura (§ A.7). Newton userà il Lemma VIII nella Prop. XLI (*per lem. viii*, gruppo G7).

### N9. Lemmi IX–XI: la corda, la velocità e la caduta

**Lemma IX.** Per la parabola, la corda parallela alla tangente in μ soddisfa AI² = 4Sμ × Iμ (4Sμ è il lato retto relativo al diametro per μ). Inoltre Sμ e il diametro μI formano angoli uguali con la tangente (proprietà focale), quindi con AC: il triangolo μIM è isoscele e μM = μI. **Verifica** su tre archi: Iμ = μM = AI²/4Sμ con sei cifre (0,172340; 0,257773; 0,213354).

**Lemma X.** La dimostrazione è **esatta**, non approssimata: area ASCμ : triangolo ASC = SN : SM (verificato: 1,276759 = 1,276759, e così negli altri due casi); con la velocità all’altezza SP = SN²/Sμ, nel tempo dell’arco AC si percorre esattamente la corda (1,662728 = 1,662728). Il Corollario è approssimato: SP = (Sμ + ⅓Iμ)²/Sμ = Sμ + ⅔Iμ + Iμ²/9Sμ (nell’esempio 1,120803 contro 1,117512).

**Lemma XI.** Esatto anch’esso: cadendo da SN con la forza di partenza mantenuta costante, nella metà del tempo dell’arco si percorre Iμ (0,172340 = 0,172340). Il passaggio intermedio usa il Cor. 9 della Prop. IV del Libro I: se nel tempo *T* il moto circolare di raggio SP percorre l’arco AC/√2, nel tempo *T*/2 percorre AC/(2√2), e la caduta corrispondente è (AC/(2√2))²/(2SP) = AI²/4SP (verificato: 0,154168 = 0,154168). Il «Cor. 9, Prop. XVI» di Motte non dà questo risultato.

I Lemmi VII, VIII, X e XI sono citati nella costruzione dell’orbita della cometa della Prop. XLI (gruppo G7).

---

## Controllo della copertura

Pagine 1726 dai marcatori ‹n› della trascrizione (la Prop. XXXVIII comincia a p. 470, prima del marcatore ‹471›). Motte: estratto senza marcatori di pagina, «sezione corrispondente».

| Identificatori | Incipit latino | Contenuto | 1726 | Motte 1846 |
|---|---|---|---|---|
| III.G6.44–III.G6.46 | *Invenire figuram corporis lunæ* | Prop. XXXVIII, soluzione, Cor. | pp. 470–471 | Prop. XXXVIII |
| III.G6.47–III.G6.50 | *Si APEp terram designet* | Lemma I | pp. 471–473 | Lemma I |
| III.G6.51–III.G6.53 | *Iisdem positis: dico secundo* | Lemma II | pp. 473–475 | Lemma II |
| III.G6.54–III.G6.55 | *Iisdem positis: dico tertio* | Lemma III | p. 475 | Lemma III |
| III.G6.56 | *Si annulus prædictus terra omni reliqua sublata* | Ipotesi II | p. 476 | Hypothesis II |
| III.G6.57–III.G6.63 | *Invenire præcessionem æquinoctiorum* … *superest ut de cometis* | Prop. XXXIX e passaggio alle comete | pp. 476–477 | Prop. XXXIX |
| III.G6.64–III.G6.67 | *Cometas esse luna superiores* … *orbe Jovis inferior esse solet* | Lemma IV: parallasse annua, le due figure | pp. 478–480 | Lemma IV |
| III.G6.68 | *Idem colligitur ex curvatura* | curvatura del cammino | pp. 480–481 | Lemma IV |
| III.G6.69–III.G6.70 | *Confirmatur etiam propinquitas* … *Hæc disputavimus* | luce delle teste; fumo e code | pp. 481–482 | Lemma IV |
| III.G6.71 | *Idem denique colligitur ex luce capitum crescente* | luce crescente e decrescente (1665, 1683, 1618, 1680) | pp. 482–483 | Lemma IV |
| III.G6.72–III.G6.74 | *Splendent igitur cometæ* … *abscondi debent* | Lemma IV, Cor. 1–3 | p. 484 | Cor. 1–3 |
| III.G6.75–III.G6.80 | *Cometas in sectionibus conicis* | Prop. XL e Cor. 1–4 | pp. 485–486 | Prop. XL |
| III.G6.81–III.G6.85 | *Invenire lineam curvam generis parabolici* | Lemma V, Casi 1–2, Cor. | pp. 486–487 | Lemma V |
| III.G6.86–III.G6.89 | *Ex observatis aliquot locis cometæ* | Lemma VI | pp. 487–488 | Lemma VI |
| III.G6.90–III.G6.91 | *Per datum punctum P ducere* | Lemma VII | p. 488 | Lemma VII |
| III.G6.92–III.G6.95 | *Sit ABC parabola umbilicum habens S* | Lemma VIII, Cor., Scolio | pp. 488–489 | Lemma VIII, Scholium |
| III.G6.96–III.G6.97 | *Rectæ Iμ & μM* | Lemma IX | p. 490 | Lemma IX |
| III.G6.98–III.G6.100 | *Si producatur Sμ ad N & P* | Lemma X e Cor. | pp. 490–491 | Lemma X |
| III.G6.101–III.G6.102 | *Si cometa motu omni privatus* | Lemma XI | p. 491 | Lemma XI |

**Controlli eseguiti.**

1. **Copertura frase per frase.** Ho riletto in sequenza ogni frase della trascrizione, da *PROPOSITIO XXXVIII.* a *spatium longitudini Iμ vel Mμ æquale. Q.E.D.* (fine del file), contro la traduzione, aiutandomi con una segmentazione automatica del latino in 82 capoversi e circa 250 frasi (`tmp/25b/sent.txt`): nessuna frase manca. I periodi lunghi (enunciato del Lemma I; Prop. XXXIX, secondo capoverso; Lemma IV, frasi con più punti e virgola) sono divisi in italiano senza omettere membri. I 59 identificatori III.G6.44–III.G6.102 sono consecutivi e unici (controllo automatico).
2. **Parte B.** `check.py` sul file finale, con il latino e il Motte **interi** del gruppo G6: JSON valido; tutte le stringhe `la` (enunciati e passi) sono sottostringhe esatte della trascrizione; tutte le stringhe `en` sono sottostringhe esatte di Motte (estratte con marcatori dal testo a spazi normalizzati); ogni identificatore di `copertura` è presente nel testo. Le stringhe `it` sono estratte automaticamente dalla traduzione, quindi coincidono con essa.
3. **Matematica e fisica** (`verifica.py`, `lemma2.py`, `scolio_test.py`): Prop. XXXVIII (1081 non torna, N1); Lemma I (0,500000); Lemma II (2/5 dagli integrali di Newton e dall’integrazione diretta della coppia); Lemma III (3π²/32 = 0,925275); Prop. XXXIX (tutta la catena, N5); Lemma IV (costruzione della parallasse su figure di prova; Saturno e cometa del 1682, N6); Prop. XL, Cor. 1, 3, 4 (240 anni; 1720212, 71675 1/2, 2432747, 101364 1/2; 1216373 1/2, 50682 1/4); Lemma V (Casi 1 e 2 contro Lagrange; Cor.); Lemma VII; Lemma VIII e Scolio (N8); Lemmi IX–XI (N9).
4. **Tabelle numeriche:** il perimetro non contiene tabelle; i valori numerici della Prop. XXXIX e della Prop. XL sono riportati nei campi `dati` della Parte B.
5. **Motte.** Confronto di tutta la sezione corrispondente; divergenze nel § A.9; 76 formule SVG controllate sul LaTeX, 1 errata (SVG 1164), 2 con difetto del solo LaTeX (1139–1140).
6. **Rimandi.** 6 rimandi ai Libri I e II, tutti verificati; 11 rimandi interni al Libro III, uno che non torna (17 1/6 contro 17 1/10) (§ A.8).
7. **Separazione fra testo e commento.** Il testo tradotto non contiene formule moderne; le parentesi tonde nelle espressioni dei Lemmi II e V sostituiscono il vinculum della stampa (Criteri).

**Non ho potuto verificare:**

- **la stampa del 1726**: i punti del § A.7 restano «probabili»; in particolare 1081 (p. 471), 17 1/6 (p. 477), √4 (p. 485) e 27MI : 16Mμ (p. 489);
- **le figure originali**: in particolare la posizione di M nello Scolio del Lemma VIII e nei Lemmi IX–X, la figura del Lemma II (piano Pape, punti N, n, X, Y) e le due figure del Lemma IV sono ricostruite dal testo;
- **le immagini SVG di Motte**: ho letto soltanto il LaTeX di `svg_tex.tsv`, non le immagini; l’EPUB non è disponibile;
- **la paginazione di Motte**: l’estratto non ha marcatori di pagina;
- i **valori moderni** citati nelle note (rapporto delle masse Terra–Luna, rapporto delle forze di marea, precessione osservata) e le identificazioni storiche (cometa di Halley, Enif, nomi degli astronomi), che vengono da conoscenza generale.

---

## Registro del lavoro successivo

| Unità | Stato |
|---|---|
| Libro III, Prop. XXXVIII – Lemma XI | **Fascicolo 25b, presente documento, prima versione** |
| Identificatori III.G6.44–III.G6.102 | Provvisori: da rinumerare in continuità con il Fascicolo 25a |
| 1081 : 100 (Prop. XXXVIII) | Da controllare sulla stampa (§ A.7, N1) |
| 17 1/6 miglia (Prop. XXXIX) contro 17 1/10 (Prop. XIX) | Da controllare sulla stampa e da armonizzare con la nota del Fascicolo 23 |
| Scolio del Lemma VIII: 27MI : 16Mμ | Da controllare sulla stampa e sulla figura; la verifica numerica dà 12 (N8) |
| Refusi della trascrizione (§ A.7) | Da verificare sulla stampa del 1726 (scansione ECCO) |
| *motus mediocris / medius* entrambi «medio»; *capillitium* «capigliatura»; *motus* «quantità di moto» nel Lemma III | Da decidere (§ A.0) |
| Pagine interattive | Parte B: 19 unità. Candidati principali: Lemmi I–II (forze sul guscio, con il cursore dell’inclinazione), Prop. XXXIX (catena numerica), Lemma IV (costruzione della parallasse, con l’avvertenza di N6), Lemma V (interpolazione con punti trascinabili), Lemma VIII (confronto AE/AC con il tempo) |
| Figure NATP00303 | Da consultare per confermare le ricostruzioni di `figura_base` |
| Revisione filologica e scientifica indipendente | Da eseguire |

Il presente testo è una nuova traduzione assistita da IA. Non riproduce traduzioni italiane o inglesi moderne. **Licenza prevista** (decisione del curatore, Fascicolo 3): testi e traduzioni CC BY-SA 4.0, codice MIT. La trascrizione latina è © The Newton Project; i testi di Motte sono di pubblico dominio.

---

## Parte B — Dati per le pagine interattive

Unità incluse (19): **Prop. XXXVIII** (calcolo); **Lemmi I, II, III** (dimostrazioni con figura e calcolo); **Ipotesi II** (solo enunciato, `"passi": []`); **Prop. XXXIX** (catena numerica, con il campo `dati`); **Lemma IV** (la costruzione della parallasse con le due figure e il calcolo della cometa del 1682; gli altri argomenti, discorsivi, restano nella traduzione); **Prop. XL** (dimostrazione per rimandi) e i suoi **Cor. 1, 3, 4** (calcoli, con `dati`); **Lemmi V, VI, VII, VIII**, lo **Scolio del Lemma VIII**, i **Lemmi IX, X, XI**. Esclusi: il Cor. della Prop. XXXVIII, il Cor. 2 della Prop. XL, i corollari dei Lemmi V, VIII e X e i Cor. 1–3 del Lemma IV (nessuna dimostrazione propria con figura o calcolo); sono comunque nella `copertura` delle unità a cui appartengono.

Convenzioni:

- `la`: testo latino esatto della trascrizione, refusi compresi (segnalati in `nota`);
- `it`: la traduzione di questo fascicolo, estratta automaticamente dal testo;
- `en`: Motte 1846, allineato per senso, con le formule come `[SVG n]`;
- `dipende_da`: soltanto i rimandi citati nella frase latina; «(implicito)» segnala un rimando che la frase presuppone senza citarlo;
- `figura.mostra`: elementi da rendere visibili, cumulativi; `figura.evidenzia`: relazioni da mettere in risalto;
- `id`: `L3-P38`, `L3-Lem1`…`L3-Lem11`, `L3-Hyp2`, `L3-P40-Cor1`, `L3-Lem8-Schol`; passi `…-p1`, `…-p2`.

```json
{
 "fascicolo": "25b-L3-P38-40",
 "versione": "0.1",
 "data": "2026-11-08",
 "convenzioni": {
  "dipende_da": "solo rimandi citati esplicitamente nella frase latina; «(implicito)» segnala un rimando che il testo presuppone senza citarlo",
  "en": "Motte 1846, allineato per senso; le formule stampate come immagini restano come [SVG n]",
  "figura.mostra": "elementi da rendere visibili al passo, cumulativi salvo indicazione",
  "la": "",
  "identificatori": "III.G6.44–III.G6.102 (parte «b», rinumerati in continuità con il 25a)"
 },
 "unita": [
  {
   "id": "L3-P38",
   "tipo": "Propositio/Problema",
   "titolo": "Prop. XXXVIII — la figura della Luna",
   "copertura": [
    "III.G6.44",
    "III.G6.45",
    "III.G6.46"
   ],
   "fonti": {
    "la": "",
    "en": "Motte 1846, sezione corrispondente (Book III, Prop. XXXVIII)"
   },
   "enunciato": {
    "la": "",
    "it": "Trovare la figura del corpo della Luna.",
    "en": "To find the figure of the moon's body."
   },
   "figura_base": {
    "punti": [
     "T (centro della Terra)",
     "L (centro della Luna)"
    ],
    "vincoli": [
     "sferoide lunare con l’asse maggiore diretto verso il centro della Terra"
    ]
   },
   "dati": {
    "rapporto_masse_Terra_Luna": 39.788,
    "diametri_Luna_Terra": [
     100,
     365
    ],
    "prodotto_calcolato": 10.9008,
    "Newton": "1081 : 100",
    "marea_lunare_piedi": 8.6,
    "innalzamento_piedi": 93,
    "eccesso_diametri_piedi": 186,
    "controllo": "39,788 × 100/365 = 10,90 (cioè 1090 : 100, non 1081 : 100); 8,6 × 10,81 = 92,97 ≈ 93; 8,6 × 10,90 = 93,75; 2 × 93 = 186 (nota N1)"
   },
   "passi": [
    {
     "id": "L3-P38-p1",
     "la": "",
     "it": "Se il corpo lunare fosse fluido come il nostro mare, la forza della Terra nel sollevare quel fluido nelle parti sia più vicine sia più lontane starebbe alla forza della Luna, con cui il nostro mare si innalza nelle parti sia sottostanti alla Luna sia opposte alla Luna, come la gravità acceleratrice della Luna verso la Terra sta alla gravità acceleratrice della Terra verso la Luna e il diametro della Luna sta al diametro della Terra, considerati congiuntamente; cioè come 39,788 sta a 1 e 100 sta a 365, considerati congiuntamente, ossia come 1081 sta a 100.",
     "en": "If the moon's body were fluid like our sea, the force of the earth to raise that fluid in the nearest and remotest parts would be to the force of the moon by which our sea is raised in the places under and opposite to the moon as the accelerative gravity of the moon towards the earth to the accelerative gravity of the earth towards the moon, and the diameter of the moon to the diameter of the earth conjunctly; that is, as 39,788 to 1, and 100 to 365 conjunctly, or as 1081 to 100.",
     "dipende_da": [],
     "figura": {
      "mostra": [
       "Terra",
       "Luna",
       "forza di marea della Terra sulla Luna",
       "forza di marea della Luna sulla Terra"
      ],
      "evidenzia": [
       "rapporto = (gravità acceleratrice) × (diametri) = 39,788 × 100/365"
      ]
     },
     "nota": "Il prodotto dei due rapporti dà 1090 : 100, non 1081 : 100 (nota N1)."
    },
    {
     "id": "L3-P38-p2",
     "la": "",
     "it": "Perciò, poiché il nostro mare è innalzato dalla forza della Luna fino a 8 3/5 piedi, il fluido lunare dovrebbe essere innalzato dalla forza della Terra fino a 93 piedi.",
     "en": "Wherefore, since our sea, by the force of the moon, is raised to [SVG 1012] feet, the lunar fluid would be raised by the force of the earth to 93 feet;",
     "dipende_da": [],
     "figura": {
      "mostra": [
       "innalzamento del mare terrestre: 8 3/5 piedi",
       "innalzamento del fluido lunare: 93 piedi"
      ],
      "evidenzia": [
       "93 = 8 3/5 × 1081/100"
      ]
     }
    },
    {
     "id": "L3-P38-p3",
     "la": "",
     "it": "E per questa causa la figura della Luna sarebbe uno sferoide il cui diametro massimo, prolungato, passerebbe per il centro della Terra e supererebbe i diametri perpendicolari con un eccesso di 186 piedi.",
     "en": "and upon this account the figure of the moon would be a spheroid, whose greatest diameter produced would pass through the centre of the earth, and exceed the diameters perpendicular thereto by 186 feet.",
     "dipende_da": [],
     "figura": {
      "mostra": [
       "sferoide lunare",
       "diametro massimo diretto verso la Terra"
      ],
      "evidenzia": [
       "eccesso 186 = 2 × 93 piedi"
      ]
     }
    },
    {
     "id": "L3-P38-p4",
     "la": "",
     "it": "La Luna, dunque, tende ad assumere una tale figura, e dovette assumerla fin dall’inizio. C.V.T.",
     "en": "Such a figure, therefore, the moon affects, and must have put on from the beginning. Q.E.I.",
     "dipende_da": [],
     "figura": {
      "mostra": [],
      "evidenzia": []
     }
    }
   ]
  },
  {
   "id": "L3-Lem1",
   "tipo": "Lemma",
   "titolo": "Lemma I — l’anello equatoriale e le particelle raccolte in A: 1 a 2",
   "copertura": [
    "III.G6.47",
    "III.G6.48",
    "III.G6.49",
    "III.G6.50"
   ],
   "fonti": {
    "la": "",
    "en": "Motte 1846, sezione corrispondente (Lemma I)"
   },
   "enunciato": {
    "la": "",
    "it": "Se APEp rappresenta la Terra, di densità uniforme, delineata con il centro C, i poli P, p e l’equatore AE; e se con centro C e raggio CP s’intende descritta la sfera Pape; e sia QR il piano su cui insiste perpendicolarmente la retta condotta dal centro del Sole al centro della Terra; e le singole particelle di tutta la Terra esterna PapAPepE, che è più alta della sfera ora descritta, tendano ad allontanarsi dal piano QR da una parte e dall’altra, e la tendenza di ciascuna particella sia come la sua distanza dal piano: dico, in primo luogo, che la forza e l’efficacia totale di tutte le particelle situate nel cerchio dell’equatore AE, disposte fuori del globo uniformemente per tutto il giro a modo di anello, nel far ruotare la Terra intorno al suo centro, sta alla forza e all’efficacia totale di altrettante particelle poste nel punto A dell’equatore, che dista massimamente dal piano QR, nel muovere la Terra intorno al suo centro con un simile moto circolare, come uno sta a due. E quel moto circolare si compirà intorno a un asse che giace nella sezione comune dell’equatore e del piano QR.",
    "en": "If APEp represent the earth uniformly dense, marked with the centre C, the poles P, p, and the equator AE; and if about the centre C, with the radius CP, we suppose the sphere Pape to be described, and QR to denote the plane on which a right line, drawn from the centre of the sun to the centre of the earth, insists at right angles; and further suppose that the several particles of the whole exterior earth PapAPepE, without the height of the said sphere, endeavour to recede towards this side and that side from the plane QR, every particle by a force proportional to its distance from that plane; I say, in the first place, that the whole force and efficacy of all the particles that are situate in AE, the circle of the equator, and disposed uniformly without the globe, encompassing the same after the manner of a ring, to wheel the earth about its centre, is to the whole force and efficacy of as many particles in that point A of the equator which is at the greatest distance from the plane QR, to wheel the earth about its centre with a like circular motion, as 1 to 2. And that circular motion will be performed about an axis lying in the common section of the equator and the plane QR."
   },
   "figura_base": {
    "punti": [
     "A",
     "P",
     "E",
     "p",
     "a",
     "e",
     "C",
     "Q",
     "R",
     "K",
     "I",
     "L",
     "N",
     "M",
     "F",
     "G",
     "H"
    ],
    "vincoli": [
     "APEp Terra (sferoide) con centro C, poli P, p, equatore AE",
     "Pape sfera di centro C e raggio CP",
     "QR piano perpendicolare alla retta Sole–Terra",
     "figura ausiliaria: semicerchio INL di centro K e diametro IL, NM seni",
     "F particella sull’equatore; FG e AH perpendicolari al piano QR; G e H sul piano QR",
     "lettura (nota N2): FC e AC sono le distanze dall’asse di rotazione (la retta comune all’equatore e a QR), viste nella proiezione sul piano perpendicolare all’asse"
    ]
   },
   "passi": [
    {
     "id": "L3-Lem1-p1",
     "la": "",
     "it": "Infatti, con centro K e diametro IL, si descriva il semicerchio INLK.",
     "en": "For let there be described from the centre K, with the diameter IL, the semi-circle INL.",
     "dipende_da": [],
     "figura": {
      "mostra": [
       "semicerchio INLK, centro K, diametro IL"
      ],
      "evidenzia": []
     },
     "nota": "La trascrizione ha «INLK», Motte «INL» (§ A.7)."
    },
    {
     "id": "L3-Lem1-p2",
     "la": "",
     "it": "Si immagini la semicirconferenza INL divisa in innumerevoli parti uguali, e dalle singole parti N si abbassino sul diametro IL i seni NM.",
     "en": "Suppose the semi-circumference INL to be divided into innumerable equal parts, and from the several parts N to the diameter IL let fall the sines NM.",
     "dipende_da": [],
     "figura": {
      "mostra": [
       "punti N equidistanti sulla semicirconferenza",
       "seni NM"
      ],
      "evidenzia": []
     }
    },
    {
     "id": "L3-Lem1-p3",
     "la": "",
     "it": "La somma dei quadrati di tutti i seni NM sarà uguale alla somma dei quadrati dei seni KM, ed entrambe le somme insieme saranno uguali alla somma dei quadrati di altrettanti semidiametri KN; e perciò la somma dei quadrati di tutti gli NM sarà la metà della somma dei quadrati di altrettanti semidiametri KN.",
     "en": "Then the sums of the squares of all the sines NM will be equal to the sums of the squares of the sines KM, and both sums together will be equal to the sums of the squares of as many semi-diameters KN; and therefore the sum of the squares of all the sines NM will be but half so great as the sum of the squares of as many semi-diameters KN.",
     "dipende_da": [],
     "figura": {
      "mostra": [
       "NM",
       "KM",
       "KN"
      ],
      "evidenzia": [
       "ΣNM² = ΣKM²",
       "ΣNM² + ΣKM² = ΣKN²",
       "ΣNM² = ½ ΣKN²"
      ]
     }
    },
    {
     "id": "L3-Lem1-p4",
     "la": "",
     "it": "Ora si divida il perimetro del cerchio AE in altrettante particelle uguali, e da ciascuna di esse, F, si abbassi sul piano QR la perpendicolare FG, come anche dal punto A la perpendicolare AH.",
     "en": "Suppose now the circumference of the circle AE to be divided into the like number of little equal parts, and from every such part F a perpendicular FG to be let fall upon the plane QR, as well as the perpendicular AH from the point A.",
     "dipende_da": [],
     "figura": {
      "mostra": [
       "cerchio dell’equatore AE diviso in particelle F",
       "FG ⊥ QR",
       "AH ⊥ QR"
      ],
      "evidenzia": []
     }
    },
    {
     "id": "L3-Lem1-p5",
     "la": "",
     "it": "La forza con cui la particella F si allontana dal piano QR sarà come quella perpendicolare FG, per ipotesi; e questa forza, moltiplicata per la distanza CG, sarà l’efficacia della particella F nel far girare la Terra intorno al suo centro.",
     "en": "Then the force by which the particle F recedes from the plane QR will (by supposition) be as that perpendicular FG; and this force multiplied by the distance CG will represent the power of the particle F to turn the earth round its centre.",
     "dipende_da": [
      "Ipotesi del lemma (tendenza come la distanza dal piano)"
     ],
     "figura": {
      "mostra": [
       "forza in F ∝ FG",
       "braccio CG"
      ],
      "evidenzia": [
       "efficacia = FG × CG"
      ]
     }
    },
    {
     "id": "L3-Lem1-p6",
     "la": "",
     "it": "Perciò l’efficacia di una particella nel luogo F starà all’efficacia di una particella nel luogo A come FG×GC sta ad AH×HC, cioè come FC² sta ad AC²; e pertanto l’efficacia totale di tutte le particelle nei loro luoghi F starà all’efficacia di altrettante particelle nel luogo A come la somma di tutti gli FC² sta alla somma di altrettanti AC², cioè (per quanto si è appena dimostrato) come uno sta a due. C.V.D.",
     "en": "And, therefore, the power of a particle in the place F will be to the power of a particle in the place A as FG × GC to AH × HC; that is, as FC2 to AC2: and therefore the whole power of all the particles F, in their proper places F, will be to the power of the like number of particles in the place A as the sum of all the FC2 to the sum of all the AC2, that is (by what we have demonstrated before) as 1 to 2. Q.E.D.",
     "dipende_da": [
      "Lemma I, prima parte (somma dei quadrati dei seni)"
     ],
     "figura": {
      "mostra": [
       "FG×GC",
       "AH×HC",
       "FC",
       "AC"
      ],
      "evidenzia": [
       "FG×GC : AH×HC = FC² : AC²",
       "ΣFC² : ΣAC² = 1 : 2"
      ]
     },
     "nota": "Verificato numericamente con l’equatore inclinato di 23,5° su QR: rapporto 0,500000 (nota N2)."
    },
    {
     "id": "L3-Lem1-p7",
     "la": "",
     "it": "E poiché le particelle agiscono allontanandosi perpendicolarmente dal piano QR, e in egual misura da entrambe le parti di questo piano, esse faranno girare la circonferenza del cerchio dell’equatore, e la Terra che vi aderisce, intorno a un asse che giace tanto in quel piano QR quanto nel piano dell’equatore.",
     "en": "And because the action of those particles is exerted in the direction of lines perpendicularly receding from the plane QR, and that equally from each side of this plane, they will wheel about the circumference of the circle of the equator, together with the adherent body of the earth, round an axis which lies as well in the plane QR as in that of the equator.",
     "dipende_da": [],
     "figura": {
      "mostra": [
       "asse di rotazione = intersezione dell’equatore con il piano QR"
      ],
      "evidenzia": [
       "simmetria rispetto al piano QR"
      ]
     }
    }
   ]
  },
  {
   "id": "L3-Lem2",
   "tipo": "Lemma",
   "titolo": "Lemma II — tutto il guscio esterno e l’anello: 2 a 5",
   "copertura": [
    "III.G6.51",
    "III.G6.52",
    "III.G6.53"
   ],
   "fonti": {
    "la": "",
    "en": "Motte 1846, sezione corrispondente (Lemma II)"
   },
   "enunciato": {
    "la": "",
    "it": "Poste le stesse cose, dico in secondo luogo che la forza e l’efficacia totale di tutte le particelle situate da ogni parte fuori del globo, nel far ruotare la Terra intorno allo stesso asse, sta alla forza totale di altrettante particelle, disposte nel cerchio dell’equatore AE uniformemente per tutto il giro a modo di anello, nel muovere la Terra con un simile moto circolare, come due sta a cinque.",
    "en": "The same things still supposed, I say, in the second place, that the total force or power of all the particles situated every where about the sphere to turn the earth about the said axis is to the whole force of the like number of particles, uniformly disposed round the whole circumference of the equator AE in the fashion of a ring, to turn the whole earth about with the like circular motion, as 2 to 5."
   },
   "figura_base": {
    "punti": [
     "I",
     "K",
     "L",
     "l",
     "M",
     "m",
     "X",
     "N",
     "n",
     "Y",
     "C",
     "A",
     "H",
     "P",
     "p"
    ],
    "vincoli": [
     "IK cerchio parallelo all’equatore, IX suo raggio, X sul diametro Pp, CX distanza dal centro",
     "L, l particelle uguali su IK con Ll parallela al piano Pape (piano meridiano della figura) e divisa a metà in X",
     "LM, lm, XY perpendicolari al piano QR",
     "Nn per X parallela a QR, che incontra LM in N e lm in n"
    ]
   },
   "passi": [
    {
     "id": "L3-Lem2-p1",
     "la": "",
     "it": "Sia infatti IK un cerchio qualsiasi, minore, parallelo all’equatore AE, e siano L, l due particelle uguali qualsiasi in questo cerchio, situate fuori del globo Pape.",
     "en": "For let IK be any lesser circle parallel to the equator AE, and let Ll be any two equal particles in this circle, situated without the sphere Pape;",
     "dipende_da": [],
     "figura": {
      "mostra": [
       "cerchio IK ∥ AE",
       "particelle L, l"
      ],
      "evidenzia": []
     }
    },
    {
     "id": "L3-Lem2-p2",
     "la": "",
     "it": "Se sul piano QR, che è perpendicolare al raggio condotto verso il Sole, si abbassano le perpendicolari LM, lm, le forze totali con cui quelle particelle fuggono il piano QR saranno proporzionali a quelle perpendicolari LM, lm.",
     "en": "and if upon the plane QR, which is at right angles with a radius drawn to the sun, we let fall the perpendiculars LM, lm, the total forces by which these particles recede from the plane QR will be proportional to the perpendiculars LM, lm.",
     "dipende_da": [],
     "figura": {
      "mostra": [
       "LM, lm ⊥ QR"
      ],
      "evidenzia": [
       "forze ∝ LM, lm"
      ]
     }
    },
    {
     "id": "L3-Lem2-p3",
     "la": "",
     "it": "Sia poi la retta Ll parallela al piano Pape e sia divisa a metà in X; per il punto X si conduca Nn, parallela al piano QR, che incontri le perpendicolari LM, lm in N e n; e sul piano QR si abbassi la perpendicolare XY.",
     "en": "Let the right line Ll be drawn parallel to the plane Pape, and bisect the same in X; and through the point X draw Nn parallel to the plane QR, and meeting the perpendiculars LM, lm, in N and n; and upon the plane QR let fall the perpendicular XY.",
     "dipende_da": [],
     "figura": {
      "mostra": [
       "Ll",
       "X punto medio",
       "Nn ∥ QR",
       "N, n",
       "XY ⊥ QR"
      ],
      "evidenzia": []
     },
     "nota": "La trascrizione ha «paralella» e «ocurrat» (refusi, § A.7)."
    },
    {
     "id": "L3-Lem2-p4",
     "la": "",
     "it": "Le forze contrarie delle particelle L e l, nel far ruotare la Terra in versi contrari, sono come LM×MC e lm×mC, cioè come LN×MC + NM×MC e ln×mC − nm×mC, ossia come LN×MC + NM×MC e LN×mC − NM×mC; e la loro differenza, LN×Mm − NM×(MC + mC), è la forza delle due particelle prese insieme nel far ruotare la Terra.",
     "en": "And the contrary forces of the particles L and l to wheel about the earth contrariwise are as LM × MC, and lm × mC; that is, as LN × MC + NM × MC, and ln × mC - nm × mC; or LN × MC + NM × MC, and LN × mC - NM × mC, and [SVG 1091] , the difference of the two, is the force of both taken together to turn the earth round.",
     "dipende_da": [],
     "figura": {
      "mostra": [
       "bracci MC, mC"
      ],
      "evidenzia": [
       "differenza = LN×Mm − NM×(MC + mC)"
      ]
     },
     "nota": "La trascrizione appiattisce il vinculum: «NM×MC+mC» = NM×(MC + mC); Motte [SVG 1091] lo conserva."
    },
    {
     "id": "L3-Lem2-p5",
     "la": "",
     "it": "La parte positiva di questa differenza, LN×Mm, ossia 2LN×NX, sta alla forza 2AH×HC di due particelle della stessa grandezza poste in A come LX² sta ad AC².",
     "en": "The affirmative part of this difference LN × Mm, or 2LN × NX, is to 2AH × HC, the force of two particles of the same size situated in A, as LX2 to AC2;",
     "dipende_da": [],
     "figura": {
      "mostra": [
       "LN",
       "NX",
       "LX"
      ],
      "evidenzia": [
       "LN×Mm = 2LN×NX",
       "2LN×NX : 2AH×HC = LX² : AC²"
      ]
     }
    },
    {
     "id": "L3-Lem2-p6",
     "la": "",
     "it": "E la parte negativa, NM×(MC + mC), ossia 2XY×CY, sta alla forza 2AH×HC delle stesse particelle poste in A come CX² sta ad AC².",
     "en": "and the negative part [SVG 1092] , or 2XY × CY, is to 2AH × HC, the force of the same two particles situated in A, as CX2 to AC2.",
     "dipende_da": [],
     "figura": {
      "mostra": [
       "XY",
       "CY",
       "CX"
      ],
      "evidenzia": [
       "NM×(MC + mC) = 2XY×CY",
       "2XY×CY : 2AH×HC = CX² : AC²"
      ]
     }
    },
    {
     "id": "L3-Lem2-p7",
     "la": "",
     "it": "E perciò la differenza delle parti, cioè la forza delle due particelle L e l prese insieme nel far ruotare la Terra, sta alla forza di due particelle uguali a esse, poste nel luogo A, nel far ruotare ugualmente la Terra, come LX² − CX² sta ad AC².",
     "en": "And therefore the difference of the parts, that is, the force of the two particles L and l, taken together, to wheel the earth about, is to the force of two particles, equal to the former and situated in the place A, to turn in like manner the earth round, as LX2 - CX2 to AC2.",
     "dipende_da": [],
     "figura": {
      "mostra": [],
      "evidenzia": [
       "forza(L,l) : forza(2 in A) = (LX² − CX²) : AC²"
      ]
     }
    },
    {
     "id": "L3-Lem2-p8",
     "la": "",
     "it": "Ma se la circonferenza IK del cerchio IK si divide in innumerevoli particelle uguali L, tutti gli LX² staranno ad altrettanti IX² come 1 sta a 2 (per il Lemma I), e ad altrettanti AC² come IX² sta a 2AC²; e altrettanti XC² staranno ad altrettanti AC² come 2CX² sta a 2AC².",
     "en": "But if the circumference IK of the circle IK is supposed to be divided into an infinite number of little equal parts L, all the LX2 will be to the like number of IX2 as 1 to 2 (by Lem. 1); and to the same number of AC2 as IX2 to 2AC2; and the same number of CX2 to as many AC2 as 2CX2 to 2AC2.",
     "dipende_da": [
      "Lemma I"
     ],
     "figura": {
      "mostra": [
       "circonferenza IK divisa in particelle L"
      ],
      "evidenzia": [
       "ΣLX² : ΣIX² = 1 : 2"
      ]
     }
    },
    {
     "id": "L3-Lem2-p9",
     "la": "",
     "it": "Perciò le forze congiunte di tutte le particelle sulla circonferenza del cerchio IK stanno alle forze congiunte di altrettante particelle nel luogo A come IX² − 2CX² sta a 2AC²; e pertanto (per il Lemma I) alle forze congiunte di altrettante particelle sulla circonferenza del cerchio AE come IX² − 2CX² sta ad AC².",
     "en": "Wherefore the united forces of all the particles in the circumference of the circle IK are to the joint forces of as many particles in the place A as IX2 - 2CX2 to 2AC2; and therefore (by Lem. 1) to the united forces of as many particles in the circumference of the circle AE as IX2 - 2CX2 to AC2.",
     "dipende_da": [
      "Lemma I"
     ],
     "figura": {
      "mostra": [],
      "evidenzia": [
       "cerchio IK : particelle in A = (IX² − 2CX²) : 2AC²",
       "cerchio IK : anello AE = (IX² − 2CX²) : AC²"
      ]
     }
    },
    {
     "id": "L3-Lem2-p10",
     "la": "",
     "it": "Ora, se il diametro Pp della sfera si divide in innumerevoli parti uguali, sulle quali insistano altrettanti cerchi IK, la materia sul perimetro di ciascun cerchio IK sarà come IX²; e perciò la forza di quella materia nel far ruotare la Terra sarà come IX² moltiplicato per (IX² − 2CX²).",
     "en": "Now if Pp, the diameter of the sphere, is conceived to be divided into an infinite number of equal parts, upon which a like number of circles IK are supposed to insist, the matter in the circumference of every circle IK will be as IX2; and therefore the force of that matter to turn the earth about will be as IX2 into IX2 - 2CX2;",
     "dipende_da": [],
     "figura": {
      "mostra": [
       "diametro Pp diviso in parti uguali",
       "cerchi IK"
      ],
      "evidenzia": [
       "materia su IK ∝ IX²"
      ]
     }
    },
    {
     "id": "L3-Lem2-p11",
     "la": "",
     "it": "E la forza della stessa materia, se stesse sul perimetro del cerchio AE, sarebbe come IX² moltiplicato per AC².",
     "en": "and the force of the same matter, if it was situated in the circumference of the circle AE, would be as IX2 into AC2.",
     "dipende_da": [],
     "figura": {
      "mostra": [],
      "evidenzia": []
     }
    },
    {
     "id": "L3-Lem2-p12",
     "la": "",
     "it": "E pertanto la forza di tutte le particelle di tutta la materia che sta fuori del globo, sui perimetri di tutti i cerchi, sta alla forza di altrettante particelle poste sul perimetro del cerchio massimo AE come tutti gli IX² moltiplicati per (IX² − 2CX²) stanno ad altrettanti IX² moltiplicati per AC², cioè come tutti gli (AC² − CX²) moltiplicati per (AC² − 3CX²) stanno ad altrettanti (AC² − CX²) moltiplicati per AC², cioè come tutti gli AC⁴ − 4AC²×CX² + 3CX⁴ stanno ad altrettanti AC⁴ − AC²×CX², cioè come l’intera quantità fluente la cui flussione è AC⁴ − 4AC²×CX² + 3CX⁴ sta all’intera quantità fluente la cui flussione è AC⁴ − AC²×CX²; e perciò, per il metodo delle flussioni, come AC⁴×CX − 4/3 AC²×CX³ + 3/5 CX⁵ sta ad AC⁴×CX − 1/3 AC²×CX³, cioè, se al posto di CX si scrive l’intera Cp, o AC, come 4/15 AC⁵ sta a 2/3 AC⁵, cioè come due sta a cinque. C.V.D.",
     "en": "And therefore the force of all the particles of the whole matter situated without the sphere in the circumferences of all the circles is to the force of the like number of particles situated in the circumference of the greatest circle AE as all the IX2 into IX2 - 2CX2 to as many IX2 into AC2; that is, as all the AC2 - CX2 into AC2 - 3CX2 to as many AC2 - CX2 into AC2; that is, as all the AC4 - 4AC2 × CX2 + 3CX4 to as many AC4 - AC2 × CX2; that is, as the whole fluent quantity, whose fluxion is AC4 - 4AC2 × CX2 + 3CX4, to the whole fluent quantity, whose fluxion is AC4 - AC2 × CX2; and, therefore, by the method of fluxions, as [SVG 1093] to [SVG 1094] ; that is, if for CX we write the whole Cp, or AC, as [SVG 1095] to [SVG 1096] ; that is, as 2 to 5. Q.E.D.",
     "dipende_da": [
      "metodo delle flussioni"
     ],
     "figura": {
      "mostra": [],
      "evidenzia": [
       "∫(AC² − CX²)(AC² − 3CX²) : ∫(AC² − CX²)AC² = 4/15 : 2/3 = 2 : 5"
      ]
     },
     "nota": "Verificato: integrali di Newton 4/15 e 2/3; integrazione diretta della coppia sul guscio di uno sferoide omogeneo poco schiacciato: 0,400000 (nota N3)."
    }
   ]
  },
  {
   "id": "L3-Lem3",
   "tipo": "Lemma",
   "titolo": "Lemma III — quantità di moto della Terra e dell’anello: 925275 a 1000000",
   "copertura": [
    "III.G6.54",
    "III.G6.55"
   ],
   "fonti": {
    "la": "",
    "en": "Motte 1846, sezione corrispondente (Lemma III)"
   },
   "enunciato": {
    "la": "",
    "it": "Poste le stesse cose, dico in terzo luogo che la quantità di moto di tutta la Terra intorno all’asse già descritto, composta dalle quantità di moto di tutte le particelle, starà alla quantità di moto dell’anello predetto intorno allo stesso asse nel rapporto composto dal rapporto della materia nella Terra alla materia nell’anello e dal rapporto di tre quadrati dell’arco quadrantale di un cerchio qualsiasi a due quadrati del diametro; cioè nel rapporto della materia alla materia e del numero 925275 al numero 1000000.",
    "en": "The same things still supposed, I say, in the third place, that the motion of the whole earth about the axis above-named arising from the motions of all the particles, will be to the motion of the aforesaid ring about the same axis in a proportion compounded of the proportion of the matter in the earth to the matter in the ring; and the proportion of three squares of the quadrantal arc of any circle to two squares of its diameter, that is, in the proportion of the matter to the matter, and of the number 925275 to the number 1000000."
   },
   "figura_base": {
    "punti": [],
    "vincoli": [
     "cilindro circoscritto alla sfera, che ruota intorno al proprio asse",
     "anello sottilissimo sul cerchio di contatto (equatore)"
    ]
   },
   "passi": [
    {
     "id": "L3-Lem3-p1",
     "la": "",
     "it": "Infatti la quantità di moto di un cilindro che ruota intorno al proprio asse immobile sta alla quantità di moto della sfera inscritta, che ruota insieme con esso, come quattro quadrati uguali qualsiasi stanno a tre dei cerchi in essi inscritti; la quantità di moto del cilindro sta alla quantità di moto di un anello sottilissimo, che circonda la sfera e il cilindro nel loro contatto comune, come il doppio della materia nel cilindro sta al triplo della materia nell’anello; e questa quantità di moto dell’anello, nel moto continuato uniformemente intorno all’asse del cilindro, sta alla sua quantità di moto nel moto uniforme intorno al proprio diametro, compiuto nello stesso tempo periodico, come la circonferenza di un cerchio sta al doppio del diametro.",
     "en": "For the motion of a cylinder revolved about its quiescent axis is to the motion of the inscribed sphere revolved together with it as any four equal squares to three circles inscribed in three of those squares; and the motion of this cylinder is to the motion of an exceedingly thin ring surrounding both sphere and cylinder in their common contact as double the matter in the cylinder to triple the matter in the ring; and this motion of the ring, uniformly continued about the axis of the cylinder, is to the uniform motion of the same about its own diameter performed in the same periodic time as the circumference of a circle to double its diameter.",
     "dipende_da": [],
     "figura": {
      "mostra": [
       "cilindro",
       "sfera inscritta",
       "anello sottile all’equatore",
       "anello che ruota intorno al proprio diametro"
      ],
      "evidenzia": [
       "cilindro : sfera = 4 quadrati : 3 cerchi = 16 : 3π",
       "cilindro : anello = 2 M(cil) : 3 M(an)",
       "anello (asse) : anello (diametro) = π : 2"
      ]
     },
     "nota": "«motus» = somma delle quantità di moto delle particelle; verificato: sfera 3π/16, anello attorno al diametro 2/π, rapporto 3π²/32 = 0,925275 (nota N4)."
    }
   ]
  },
  {
   "id": "L3-Hyp2",
   "tipo": "Hypothesis",
   "titolo": "Ipotesi II — l’anello fluido o rigido",
   "copertura": [
    "III.G6.56"
   ],
   "fonti": {
    "la": "",
    "en": "Motte 1846, sezione corrispondente (Hypothesis II)"
   },
   "enunciato": {
    "la": "",
    "it": "Se l’anello predetto, tolta tutta la rimanente Terra, fosse portato da solo nell’orbita della Terra intorno al Sole con moto annuo, e intanto ruotasse con moto diurno intorno al proprio asse, inclinato sul piano dell’eclittica con un angolo di 23 1/2 gradi, il moto dei punti equinoziali sarebbe lo stesso, sia che quell’anello fosse fluido, sia che fosse fatto di materia rigida e salda.",
    "en": "If the other parts of the earth were taken away, and the remaining ring was carried alone about the sun in the orbit of the earth by the annual motion, while by the diurnal motion it was in the mean time revolved about its own axis inclined to the plane of the ecliptic by an angle of [SVG 1097] degrees, the motion of the equinoctial points would be the same, whether the ring were fluid, or whether it consisted of a hard and rigid matter."
   },
   "passi": [],
   "nota": "Ipotesi senza dimostrazione; Motte rende l’angolo con [SVG 1097] = 23 1/2."
  },
  {
   "id": "L3-P39",
   "tipo": "Propositio/Problema",
   "titolo": "Prop. XXXIX — la precessione degli equinozi: 50″ all’anno",
   "copertura": [
    "III.G6.57",
    "III.G6.58",
    "III.G6.59",
    "III.G6.60",
    "III.G6.61",
    "III.G6.62",
    "III.G6.63"
   ],
   "fonti": {
    "la": "",
    "en": "Motte 1846, sezione corrispondente (Prop. XXXIX)"
   },
   "enunciato": {
    "la": "",
    "it": "Trovare la precessione degli equinozi.",
    "en": "To find the precession of the equinoxes."
   },
   "dati": {
    "catena_di_Newton": [
     {
      "passo": "metà di 16″35‴16iv36v",
      "Newton": "8″17‴38iv18v",
      "ricalcolo": "8″17‴38iv18v"
     },
     {
      "passo": "moto annuo dei nodi (anno siderale)",
      "Newton": "20°11′46″",
      "ricalcolo": "20°11′46,2″"
     },
     {
      "passo": "23h56′ : 27g7h43′",
      "Newton": "1436 : 39343",
      "ricalcolo": "1436 : 39343 (minuti)"
     },
     {
      "passo": "globo : guscio con 229 : 230",
      "Newton": "52441 : 459",
      "ricalcolo": "229² = 52441; 230² − 229² = 459"
     },
     {
      "passo": "459/52441 × 1000000/925275",
      "Newton": "4590 : 485223",
      "ricalcolo": "4590 : 485223,46"
     },
     {
      "passo": "anello : (anello + globo)",
      "Newton": "4590 : 489813",
      "ricalcolo": "4590 + 485223 = 489813"
     },
     {
      "passo": "1436/39343 × 4590/489813",
      "Newton": "100 : 292369",
      "ricalcolo": "100 : 292368,6"
     },
     {
      "passo": "× 2/5 (Lemma II)",
      "Newton": "10 : 73092",
      "ricalcolo": "10 : 73092,1"
     },
     {
      "passo": "72706″ × 10/73092",
      "Newton": "9″56‴50iv",
      "ricalcolo": "9″56‴49,9iv"
     },
     {
      "passo": "× 0,91706 (cos 23 1/2°)",
      "Newton": "9″7‴20iv",
      "ricalcolo": "9″7‴19,8iv; cos 23,5° = 0,917060"
     },
     {
      "passo": "× 4,4815 (Luna)",
      "Newton": "40″52‴52iv",
      "ricalcolo": "40″52‴52,5iv"
     },
     {
      "passo": "somma Sole + Luna",
      "Newton": "50″00‴12iv",
      "ricalcolo": "50″00‴12,0iv"
     }
    ],
    "esito": "tutti i passaggi tornano entro l’arrotondamento dell’ultima cifra (nota N5)"
   },
   "passi": [
    {
     "id": "L3-P39-p1",
     "la": "",
     "it": "Il moto orario medio dei nodi della Luna in un’orbita circolare, quando i nodi sono nelle quadrature, era di 16″ 35‴ 16ⁱᵛ 36ᵛ; e la sua metà, 8″ 17‴ 38ⁱᵛ 18ᵛ, è (per le ragioni spiegate sopra) il moto orario medio dei nodi in una tale orbita; e in un intero anno siderale diventa di 20° 11′ 46″.",
     "en": "The middle horary motion of the moon's nodes in a circular orbit, when the nodes are in the quadratures, was 16'' 35''' 16iv. 36v.; the half of which, 8'' 17''' 38iv. 18v. (for the reasons above explained) is the mean horary motion of the nodes in such an orbit, which motion in a whole sidereal year becomes 20° 11' 46''.",
     "dipende_da": [],
     "figura": {
      "mostra": [
       "orbita lunare circolare",
       "nodi nelle quadrature"
      ],
      "evidenzia": [
       "8″17‴38iv18v × ore dell’anno siderale = 20°11′46″"
      ]
     },
     "nota": "«per le ragioni spiegate sopra» rimanda alle Propp. XXX–XXXIII (Fasc. 24b); il valore 16″35‴16iv36v viene da lì."
    },
    {
     "id": "L3-P39-p2",
     "la": "",
     "it": "Poiché dunque i nodi della Luna in una tale orbita compirebbero ogni anno 20° 11′ 46″ in antecedenza; e, se ci fossero più lune, i moti dei nodi di ciascuna (per il Cor. 16 della Prop. LXVI del Libro I) sarebbero come i tempi periodici; se una luna ruotasse vicino alla superficie della Terra nello spazio di un giorno siderale, il moto annuo dei suoi nodi starebbe a 20° 11′ 46″ come il giorno siderale di 23 ore e 56′ sta al tempo periodico della Luna di 27 giorni, 7 ore e 43′, cioè come 1436 sta a 39343.",
     "en": "Because, therefore, the nodes of the moon in such an orbit would be yearly transferred 20° 11' 46'' in antecedentia; and, if there were more moons, the motion of the nodes of every one (by Cor. 16, Prop. LXVI, Book I) would be as its periodic time; if upon the surface of the earth a moon was revolved in the time of a sidereal day, the annual motion of the nodes of this moon would be to 20° 11' 46'' as 23h. 56', the sidereal day, to 27d. 7h. 43', the periodic time of our moon, that is, as 1436 to 39343.",
     "dipende_da": [
      "Libro I, Prop. LXVI, Cor. 16"
     ],
     "figura": {
      "mostra": [
       "Luna ideale che ruota rasente la Terra in un giorno siderale"
      ],
      "evidenzia": [
       "moto annuo dei nodi ∝ tempo periodico",
       "1436 : 39343 (minuti)"
      ]
     },
     "nota": "Il latino è diviso in due frasi dallo strumento di segmentazione dopo «Lib.»: qui sono riunite. «LLunæ» è refuso della trascrizione."
    },
    {
     "id": "L3-P39-p3",
     "la": "",
     "it": "E lo stesso vale per i nodi di un anello di lune che circonda la Terra, sia che quelle lune non si tocchino fra loro, sia che si liquefacciano e si formino in un anello continuo, sia infine che quell’anello si irrigidisca e sia reso inflessibile.",
     "en": "And the same thing would happen to the nodes of a ring of moons encompassing the earth, whether these moons did not mutually touch each the other, or whether they were molten, and formed into a continued ring, or whether that ring should become rigid and inflexible.",
     "dipende_da": [],
     "figura": {
      "mostra": [
       "anello di lune"
      ],
      "evidenzia": []
     },
     "nota": "«illaeæ» è refuso della trascrizione per «illæ»."
    },
    {
     "id": "L3-P39-p4",
     "la": "",
     "it": "Immaginiamo dunque che quell’anello, quanto alla quantità di materia, sia uguale a tutta la Terra PapAPepE che sta sopra il globo Pape (si veda la figura a p. 474); e poiché quel globo sta a quella Terra superiore come aC² sta ad AC² − aC², cioè (essendo il diametro minore della Terra, PC o aC, al semidiametro maggiore AC come 229 sta a 230) come 52441 sta a 459; se quell’anello cingesse la Terra lungo l’equatore ed entrambi ruotassero insieme intorno al diametro dell’anello, la quantità di moto dell’anello starebbe alla quantità di moto del globo interno (per il Lemma III di questo Libro) come 459 sta a 52441 e 1000000 sta a 925275, considerati congiuntamente, cioè come 4590 sta a 485223; e perciò la quantità di moto dell’anello starebbe alla somma delle quantità di moto dell’anello e del globo come 4590 sta a 489813.",
     "en": "Let us, then, suppose that this ring is in quantity of matter equal to the whole exterior earth PapAPepE, which lies without the sphere Pape (see fig. Lem. II); and because this sphere is to that exterior earth as aC2 to AC2 - aC2, that is (seeing PC or aC the least semi-diameter of the earth is to AC the greatest semi-diameter of the same as 229 to 230), as 52441 to 459; if this ring encompassed the earth round the equator, and both together were revolved about the diameter of the ring, the motion of the ring (by Lem. III) would be to the motion of the inner sphere as 459 to 52441 and 1000000 to 925275 conjunctly, that is, as 4590 to 485223; and therefore the motion of the ring would be to the sum of the motions of both ring and sphere as 4590 to 489813.",
     "dipende_da": [
      "Lemma III",
      "Lemma II (figura a p. 474)"
     ],
     "figura": {
      "mostra": [
       "globo Pape",
       "Terra superiore PapAPepE",
       "anello equatoriale di uguale materia"
      ],
      "evidenzia": [
       "52441 : 459",
       "4590 : 485223",
       "4590 : 489813"
      ]
     },
     "nota": "La trascrizione ha «>ACqu.» con un segno spurio; «diameter minor PC vel aC» è in realtà un semidiametro (Motte: «least semi-diameter»)."
    },
    {
     "id": "L3-P39-p5",
     "la": "",
     "it": "Quindi, se l’anello aderisce al globo e comunica al globo la quantità di moto con cui i suoi nodi, ossia i punti equinoziali, regrediscono, la quantità di moto che resterà nell’anello starà alla sua quantità di moto di prima come 4590 sta a 489813; e perciò il moto dei punti equinoziali diminuirà nello stesso rapporto.",
     "en": "Wherefore if the ring adheres to the sphere, and communicates its motion to the sphere, by which its nodes or equinoctial points recede, the motion remaining in the ring will be to its former motion as 4590 to 489813; upon which account the motion of the equinoctial points will be diminished in the same proportion.",
     "dipende_da": [],
     "figura": {
      "mostra": [
       "anello aderente al globo"
      ],
      "evidenzia": [
       "moto residuo dell’anello : moto di prima = 4590 : 489813"
      ]
     }
    },
    {
     "id": "L3-P39-p6",
     "la": "",
     "it": "Il moto annuo dei punti equinoziali del corpo composto dell’anello e del globo starà dunque al moto di 20° 11′ 46″ come 1436 sta a 39343 e 4590 sta a 489813, considerati congiuntamente, cioè come 100 sta a 292369.",
     "en": "Wherefore the annual motion of the equinoctial points of the body, composed of both ring and sphere, will be to the motion 20° 11' 46'' as 1436 to 39343 and 4590 to 489813 conjunctly, that is, as 100 to 292369.",
     "dipende_da": [],
     "figura": {
      "mostra": [],
      "evidenzia": [
       "1436/39343 × 4590/489813 = 100/292369"
      ]
     }
    },
    {
     "id": "L3-P39-p7",
     "la": "",
     "it": "Ma le forze per cui i nodi delle lune (come ho spiegato sopra), e perciò i punti equinoziali dell’anello, regrediscono (cioè le forze 3IT nella figura alle pp. 437 e 438), sono nelle singole particelle come le distanze delle particelle dal piano QR, e con queste forze quelle particelle fuggono il piano; e perciò (per il Lemma II), se la materia dell’anello si spargesse per tutta la superficie del globo, a modo della figura PapAPepE, per costituire quella parte superiore della Terra, la forza e l’efficacia totale di tutte le particelle nel far ruotare la Terra intorno a un diametro qualsiasi dell’equatore, e quindi nel muovere i punti equinoziali, risulterebbe minore di prima nel rapporto di 2 a 5.",
     "en": "But the forces by which the nodes of a number of moons (as we explained above), and therefore by which the equinoctial points of the ring recede (that is, the forces 3IT, in fig. Prop. XXX), are in the several particles as the distances of those particles from the plane QR; and by these forces the particles recede from that plane: and therefore (by Lem. II) if the matter of the ring was spread all over the surface of the sphere, after the fashion of the figure PapAPepE, in order to make up that exterior part of the earth, the total force or power of all the particles to wheel about the earth round any diameter of the equator, and therefore to move the equinoctial points, would become less than before in the proportion of 2 to 5.",
     "dipende_da": [
      "Lemma II",
      "Prop. XXX (figura alle pp. 437–438)"
     ],
     "figura": {
      "mostra": [
       "forze 3IT",
       "piano QR",
       "materia dell’anello sparsa sul guscio PapAPepE"
      ],
      "evidenzia": [
       "efficacia del guscio : anello = 2 : 5"
      ]
     },
     "nota": "Motte converte il rimando alle pagine in «fig. Prop. XXX»."
    },
    {
     "id": "L3-P39-p8",
     "la": "",
     "it": "Perciò il regresso annuo degli equinozi starebbe ora a 20° 11′ 46″ come 10 sta a 73092, e diventerebbe quindi di 9″ 56‴ 50ⁱᵛ.",
     "en": "Wherefore the annual regress of the equinoxes now would be to 20° 11' 46'' as 10 to 73092; that is, would be 9'' 56''' 50iv.",
     "dipende_da": [],
     "figura": {
      "mostra": [],
      "evidenzia": [
       "72706″ × 10/73092 = 9″56‴50iv"
      ]
     }
    },
    {
     "id": "L3-P39-p9",
     "la": "",
     "it": "Ma questo moto deve essere diminuito a causa dell’inclinazione del piano dell’equatore sul piano dell’eclittica, e precisamente nel rapporto del seno 91706 (che è il seno del complemento di 23 1/2 gradi) al raggio 100000.",
     "en": "But because the plane of the equator is inclined to that of the ecliptic, this motion is to be diminished in the proportion of the sine 91706 (which is the co-sine of [SVG 1097] deg.) to the radius 100000;",
     "dipende_da": [],
     "figura": {
      "mostra": [
       "inclinazione dell’equatore sull’eclittica: 23 1/2°"
      ],
      "evidenzia": [
       "fattore 91706/100000 = cos 23 1/2°"
      ]
     }
    },
    {
     "id": "L3-P39-p10",
     "la": "",
     "it": "In questo rapporto quel moto diventerà ora di 9″ 7‴ 20ⁱᵛ.",
     "en": "and the remaining motion will now be 9'' 7''' 20iv.",
     "dipende_da": [],
     "figura": {
      "mostra": [],
      "evidenzia": [
       "9″56‴50iv × 0,91706 = 9″7‴20iv"
      ]
     }
    },
    {
     "id": "L3-P39-p11",
     "la": "",
     "it": "Questa è la precessione annua degli equinozi che nasce dalla forza del Sole.",
     "en": "which is the annual precession of the equinoxes arising from the force of the sun.",
     "dipende_da": [],
     "figura": {
      "mostra": [],
      "evidenzia": []
     }
    },
    {
     "id": "L3-P39-p12",
     "la": "",
     "it": "La forza della Luna nel muovere il mare stava poi alla forza del Sole circa come 4,4815 sta a 1.",
     "en": "But the force of the moon to move the sea was to the force of the sun nearly as 4,4815 to 1;",
     "dipende_da": [
      "Prop. XXXVII"
     ],
     "figura": {
      "mostra": [],
      "evidenzia": [
       "Luna : Sole = 4,4815 : 1"
      ]
     }
    },
    {
     "id": "L3-P39-p13",
     "la": "",
     "it": "E la forza della Luna nel muovere gli equinozi sta alla forza del Sole nella stessa proporzione.",
     "en": "and the force of the moon to move the equinoxes is to that of the sun in the same proportion.",
     "dipende_da": [],
     "figura": {
      "mostra": [],
      "evidenzia": []
     }
    },
    {
     "id": "L3-P39-p14",
     "la": "",
     "it": "Di qui risulta la precessione annua degli equinozi che nasce dalla forza della Luna, di 40″ 52‴ 52ⁱᵛ, e la precessione annua totale che nasce da entrambe le forze, di 50″ 00‴ 12ⁱᵛ.",
     "en": "Whence the annual precession of the equinoxes proceeding from the force of the moon comes out 40'' 52''' 52iv. and the total annual precession arising from the united forces of both will be 50'' 00''' 12iv.",
     "dipende_da": [],
     "figura": {
      "mostra": [],
      "evidenzia": [
       "9″7‴20iv × 4,4815 = 40″52‴52iv",
       "totale 50″00‴12iv"
      ]
     }
    },
    {
     "id": "L3-P39-p15",
     "la": "",
     "it": "E questo moto concorda con i fenomeni.",
     "en": "the quantity of which motion agrees with the phænomena;",
     "dipende_da": [],
     "figura": {
      "mostra": [],
      "evidenzia": []
     }
    },
    {
     "id": "L3-P39-p16",
     "la": "",
     "it": "Infatti la precessione degli equinozi, secondo le osservazioni astronomiche, è ogni anno di cinquanta secondi, più o meno.",
     "en": "for the precession of the equinoxes, by astronomical observations, is about 50'' yearly.",
     "dipende_da": [],
     "figura": {
      "mostra": [],
      "evidenzia": []
     },
     "nota": "«æquinoctiourum» e «astronimicis» sono refusi della trascrizione."
    },
    {
     "id": "L3-P39-p17",
     "la": "",
     "it": "Se l’altezza della Terra all’equatore supera la sua altezza ai poli di più di 17 1/6 miglia, la sua materia sarà più rada alla circonferenza che al centro; e la precessione degli equinozi dovrà aumentare a causa di quell’altezza e diminuire a causa della radezza.",
     "en": "If the height of the earth at the equator exceeds its height at the poles by more than [SVG 1098] miles, the matter thereof will be more rare near the surface than at the centre; and the precession of the equinoxes will be augmented by the excess of height, and diminished by the greater rarity.",
     "dipende_da": [
      "Prop. XIX (implicito)"
     ],
     "figura": {
      "mostra": [],
      "evidenzia": []
     },
     "nota": "17 1/6 miglia (Motte [SVG 1098] = 17 1/6); la Prop. XIX dà invece 85472 piedi = 17 1/10 miglia (nota N5, § A.7)."
    }
   ]
  },
  {
   "id": "L3-Lem4",
   "tipo": "Lemma",
   "titolo": "Lemma IV — le comete sono più alte della Luna: la parallasse annua",
   "copertura": [
    "III.G6.64",
    "III.G6.65",
    "III.G6.66",
    "III.G6.67",
    "III.G6.68",
    "III.G6.69",
    "III.G6.70",
    "III.G6.71",
    "III.G6.72",
    "III.G6.73",
    "III.G6.74"
   ],
   "fonti": {
    "la": "",
    "en": "Motte 1846, sezione corrispondente (Lemma IV)"
   },
   "enunciato": {
    "la": "",
    "it": "Le comete sono più alte della Luna e si trovano nella regione dei pianeti.",
    "en": "That the comets are higher than the moon, and in the regions of the planets."
   },
   "figura_base": {
    "figura_1": {
     "punti": [
      "Q",
      "A",
      "B",
      "C",
      "G",
      "F",
      "♈"
     ],
     "vincoli": [
      "Q luogo d’osservazione (pensato fisso)",
      "QA, QB, QC, QF direzioni osservate",
      "ABC retta con AB : BC = tempi fra le prime tre osservazioni (Lemma VII)",
      "G su AC prolungata con AG : AB = (t4 − t1) : (t2 − t1)"
     ]
    },
    "figura_2": {
     "punti": [
      "S",
      "a",
      "c",
      "T",
      "g",
      "V",
      "♈"
     ],
     "vincoli": [
      "acT orbe magno",
      "g su ac prolungata con ag : ac = AG : AC",
      "T♈ e g♈ parallele, verso il principio dell’Ariete",
      "angolo ♈TV = ♈QF, angolo ♈gV = ♈QG",
      "V = intersezione di TV e gV"
     ]
    }
   },
   "nota": "Passi: la dimostrazione con le due figure (III.G6.65–III.G6.67) e il calcolo della cometa del 1682 (inizio di III.G6.69). Gli altri argomenti (curvatura del cammino, fumo e code, luce crescente e decrescente, i tre corollari) sono discorsivi e restano nella sola traduzione. Verifica della costruzione: nota N6.",
   "passi": [
    {
     "id": "L3-Lem4-p1",
     "la": "",
     "it": "Come la mancanza di parallasse diurna ha innalzato le comete al di sopra delle regioni sublunari, così dalla parallasse annua si dimostra la loro discesa nelle regioni dei pianeti.",
     "en": "As the comets were placed by astronomers above the moon, because they were found to have no diurnal parallax, so their annual parallax is a convincing proof of their descending into the regions of the planets;",
     "dipende_da": [],
     "figura": {
      "mostra": [
       "Terra",
       "cometa",
       "Sole"
      ],
      "evidenzia": []
     },
     "nota": "Motte amplia: «placed by astronomers above the moon, because they were found to have no diurnal parallax»."
    },
    {
     "id": "L3-Lem4-p2",
     "la": "",
     "it": "Infatti le comete che procedono secondo l’ordine dei segni sono tutte, verso la fine della loro apparizione, o più lente del solito o retrograde, se la Terra è fra esse e il Sole; ma più veloci del dovuto, se la Terra volge verso l’opposizione.",
     "en": "for all the comets which move in a direct course according to the order of the signs, about the end of their appearance become more than ordinarily slow or retrograde, if the earth is between them and the sun; and more than ordinarily swift, if the earth is approaching to a heliocentric opposition with them;",
     "dipende_da": [],
     "figura": {
      "mostra": [
       "cometa diretta",
       "Terra fra la cometa e il Sole",
       "Terra verso l’opposizione"
      ],
      "evidenzia": []
     },
     "nota": "Motte aggiunge «heliocentric»."
    },
    {
     "id": "L3-Lem4-p3",
     "la": "",
     "it": "E al contrario quelle che procedono contro l’ordine dei segni sono più veloci del dovuto alla fine dell’apparizione, se la Terra si trova fra esse e il Sole; e più lente del dovuto o retrograde, se la Terra è situata dalla parte contraria.",
     "en": "whereas, on the other hand, those which move against the order of the signs, towards the end of their appearance appear swifter than they ought to be, if the earth is between them and the sun; and slower, and perhaps retrograde, if the earth is in the other side of its orbit.",
     "dipende_da": [],
     "figura": {
      "mostra": [
       "cometa retrograda"
      ],
      "evidenzia": []
     }
    },
    {
     "id": "L3-Lem4-p4",
     "la": "",
     "it": "Ciò avviene soprattutto per il moto della Terra nelle sue varie posizioni, così come accade nei pianeti, che, secondo che il moto della Terra sia concorde o contrario, ora sono retrogradi, ora sembrano procedere più lentamente, ora invece più velocemente.",
     "en": "And these appearances proceed chiefly from the diverse situations which the earth acquires in the course of its motion, after the same manner as it happens to the planets, which appear sometimes retrograde, sometimes more slowly, and sometimes more swiftly, progressive, according as the motion of the earth falls in with that of the planet, or is directed the contrary way.",
     "dipende_da": [],
     "figura": {
      "mostra": [],
      "evidenzia": [
       "analogia con le stazioni e retrogradazioni dei pianeti"
      ]
     }
    },
    {
     "id": "L3-Lem4-p5",
     "la": "",
     "it": "Se la Terra procede verso la stessa parte della cometa e, con il moto angolare intorno al Sole, è portata tanto più velocemente che la retta condotta di continuo per la Terra e la cometa converga verso le parti al di là della cometa, la cometa vista dalla Terra, a causa del suo moto più lento, appare retrograda; se invece la Terra è portata più lentamente, il moto della cometa (sottratto il moto della Terra) diventa almeno più lento.",
     "en": "If the earth move the same way with the comet, but, by an angular motion about the sun, so much swifter that right lines drawn from the earth to the comet converge towards the parts beyond the comet, the comet seen from the earth, because of its slower motion, will appear retrograde; and even if the earth is slower than the comet, the motion of the earth being subducted, the motion of the comet will at least appear retarded;",
     "dipende_da": [],
     "figura": {
      "mostra": [
       "retta Terra–cometa",
       "convergenza al di là della cometa"
      ],
      "evidenzia": [
       "moto apparente = moto della cometa − moto della Terra"
      ]
     }
    },
    {
     "id": "L3-Lem4-p6",
     "la": "",
     "it": "Ma se la Terra procede verso parti contrarie, la cometa appare di conseguenza più veloce.",
     "en": "but if the earth tends the contrary way to that of the comet, the motion of the comet will from thence appear accelerated;",
     "dipende_da": [],
     "figura": {
      "mostra": [],
      "evidenzia": []
     }
    },
    {
     "id": "L3-Lem4-p7",
     "la": "",
     "it": "Dall’accelerazione, dal ritardo o dal moto retrogrado si ricava poi la distanza della cometa in questo modo.",
     "en": "and from this apparent acceleration, or retardation, or regressive motion, the distance of the comet may be inferred in this manner.",
     "dipende_da": [],
     "figura": {
      "mostra": [],
      "evidenzia": []
     }
    },
    {
     "id": "L3-Lem4-p8",
     "la": "",
     "it": "Siano ♈QA, ♈QB, ♈QC tre longitudini osservate della cometa all’inizio del moto, e sia ♈QF la longitudine osservata per ultima, quando la cometa cessa di essere visibile.",
     "en": "Let [SVG 1099] , [SVG 1100] , [SVG 1101] , be three observed longitudes of the comet about the time of its first appearing, and [SVG 1102] its last observed longitude before its disappearing.",
     "dipende_da": [],
     "figura": {
      "mostra": [
       "Q",
       "direzione ♈",
       "QA, QB, QC",
       "QF"
      ],
      "evidenzia": [
       "longitudini come angoli da Q♈"
      ]
     },
     "nota": "Nella trascrizione il segno dell’Ariete è reso «γ» (§ A.7)."
    },
    {
     "id": "L3-Lem4-p9",
     "la": "",
     "it": "Si conduca la retta ABC, le cui parti AB, BC, comprese fra le rette QA e QB, QB e QC, stiano fra loro come i tempi fra le prime tre osservazioni.",
     "en": "Draw the right line ABC, whose parts AB, BC, intercepted between the right lines QA and QB, QB and QC, may be one to the other as the two times between the three first observations.",
     "dipende_da": [
      "Lemma VII (implicito)"
     ],
     "figura": {
      "mostra": [
       "retta ABC"
      ],
      "evidenzia": [
       "AB : BC = (t2 − t1) : (t3 − t2)"
      ]
     },
     "nota": "La costruzione di una retta tagliata in un rapporto dato da rette date è quella del Lemma VII, che il testo non cita qui."
    },
    {
     "id": "L3-Lem4-p10",
     "la": "",
     "it": "Si prolunghi AC fino a G, in modo che AG stia ad AB come il tempo fra la prima e l’ultima osservazione sta al tempo fra la prima e la seconda, e si congiunga QG.",
     "en": "Produce AC to G, so as AG may be to AB as the time between the first and last observation to the time between the first and second; and join QG.",
     "dipende_da": [],
     "figura": {
      "mostra": [
       "G",
       "QG"
      ],
      "evidenzia": [
       "AG : AB = (t4 − t1) : (t2 − t1)"
      ]
     }
    },
    {
     "id": "L3-Lem4-p11",
     "la": "",
     "it": "Se la cometa si muovesse uniformemente in linea retta, e la Terra o stesse ferma o anch’essa avanzasse in linea retta con moto uniforme, l’angolo ♈QG sarebbe la longitudine della cometa al tempo dell’ultima osservazione.",
     "en": "Now if the comet did move uniformly in a right line, and the earth either stood still, or was likewise carried forwards in a right line by an uniform motion, the angle [SVG 1103] would be the longitude of the comet at the time of the last observation.",
     "dipende_da": [],
     "figura": {
      "mostra": [
       "angolo ♈QG"
      ],
      "evidenzia": [
       "moto relativo rettilineo uniforme ⇒ ♈QG esatto"
      ]
     }
    },
    {
     "id": "L3-Lem4-p12",
     "la": "",
     "it": "L’angolo FQG, dunque, che è la differenza delle longitudini, nasce dalla disuguaglianza dei moti della cometa e della Terra.",
     "en": "The angle, therefore, FQG, which is the difference of the longitude, proceeds from the inequality of the motions of the comet and the earth;",
     "dipende_da": [],
     "figura": {
      "mostra": [
       "angolo FQG"
      ],
      "evidenzia": [
       "FQG = differenza delle longitudini"
      ]
     }
    },
    {
     "id": "L3-Lem4-p13",
     "la": "",
     "it": "Questo angolo, se la Terra e la cometa si muovono verso parti contrarie, si aggiunge all’angolo ♈QG, e rende così più veloce il moto apparente della cometa; se invece la cometa procede verso le stesse parti della Terra, gli si sottrae, e rende il moto della cometa o più lento o forse retrogrado, come ho appena esposto.",
     "en": "and this angle, if the earth and comet move contrary ways, is added to the angle [SVG 1103] , and accelerates the apparent motion of the comet; but if the comet move; the same way with the earth, it is subtracted, and either retards the motion of the comet, or perhaps renders it retrograde, as we have but now explained.",
     "dipende_da": [],
     "figura": {
      "mostra": [],
      "evidenzia": [
       "segno di FQG secondo il verso dei moti"
      ]
     }
    },
    {
     "id": "L3-Lem4-p14",
     "la": "",
     "it": "Questo angolo nasce dunque principalmente dal moto della Terra, e perciò va giustamente considerato la parallasse della cometa, trascurando cioè un certo suo aumento o diminuzione che possa nascere dal moto non uniforme della cometa nella sua orbita.",
     "en": "This angle, therefore, proceeding chiefly from the motion of the earth, is justly to be esteemed the parallax of the comet; neglecting, to wit, some little increment or decrement that may arise from the unequal motion of the comet in its orbit;",
     "dipende_da": [],
     "figura": {
      "mostra": [],
      "evidenzia": [
       "FQG = parallasse della cometa"
      ]
     }
    },
    {
     "id": "L3-Lem4-p15",
     "la": "",
     "it": "La distanza della cometa si ricava poi da questa parallasse così.",
     "en": "and from this parallax we thus deduce the distance of the comet.",
     "dipende_da": [],
     "figura": {
      "mostra": [],
      "evidenzia": []
     }
    },
    {
     "id": "L3-Lem4-p16",
     "la": "",
     "it": "S rappresenti il Sole, acT l’orbe magno, a il luogo della Terra nella prima osservazione, c il luogo della Terra nella terza osservazione, T il luogo della Terra nell’ultima osservazione, e T♈ una linea retta condotta verso il principio dell’Ariete.",
     "en": "Let S represent the sun, acT the orbis magnus, a the earth's place in the first observation, c the place of the earth in the third observation, T the place of the earth in the last observation, and [SVG 1104] a right line drawn to the beginning of Aries.",
     "dipende_da": [],
     "figura": {
      "mostra": [
       "seconda figura: S, orbe magno acT, a, c, T, T♈"
      ],
      "evidenzia": []
     }
    },
    {
     "id": "L3-Lem4-p17",
     "la": "",
     "it": "Si prenda l’angolo ♈TV uguale all’angolo ♈QF, cioè uguale alla longitudine della cometa quando la Terra si trova in T.",
     "en": "Set off the angle [SVG 1105] equal to the angle [SVG 1102] , that is, equal to the longitude of the comet at the time when the earth is in T;",
     "dipende_da": [],
     "figura": {
      "mostra": [
       "retta TV"
      ],
      "evidenzia": [
       "♈TV = ♈QF"
      ]
     }
    },
    {
     "id": "L3-Lem4-p18",
     "la": "",
     "it": "Si congiunga ac e la si prolunghi fino a g, in modo che ag stia ad ac come AG sta ad AC; e g sarà il luogo che la Terra, continuando uniformemente il moto lungo la retta ac, raggiungerebbe al tempo dell’ultima osservazione.",
     "en": "join ac, and produce it to g, so as ag may be to ac as AG to AC; and g will be the place at which the earth would have arrived in the time of the last observation, if it had continued to move uniformly in the right line ac.",
     "dipende_da": [],
     "figura": {
      "mostra": [
       "retta ac",
       "g"
      ],
      "evidenzia": [
       "ag : ac = AG : AC"
      ]
     }
    },
    {
     "id": "L3-Lem4-p19",
     "la": "",
     "it": "Perciò, se si conduce g♈ parallela a T♈ e si prende l’angolo ♈gV uguale all’angolo ♈QG, questo angolo ♈gV sarà uguale alla longitudine della cometa vista dal luogo g; e l’angolo TVg sarà la parallasse che nasce dallo spostamento della Terra dal luogo g al luogo T; e perciò V sarà il luogo della cometa nel piano dell’eclittica.",
     "en": "Wherefore, if we draw [SVG 1106] parallel to [SVG 1107] , and make the angle [SVG 1108] equal to the angle [SVG 1103] , this angle [SVG 1109] will be equal to the longitude of the comet seen from the place g, and the angle TVg will be the parallax which arises from the earth's being transferred from the place g into the place T; and therefore V will be the place of the comet in the plane of the ecliptic.",
     "dipende_da": [],
     "figura": {
      "mostra": [
       "g♈ ∥ T♈",
       "retta gV",
       "V"
      ],
      "evidenzia": [
       "♈gV = ♈QG",
       "TVg = parallasse",
       "V = TV ∩ gV"
      ]
     },
     "nota": "Verificato su una figura di prova: con le ipotesi del testo V coincide con il luogo vero (nota N6)."
    },
    {
     "id": "L3-Lem4-p20",
     "la": "",
     "it": "Questo luogo V suole poi trovarsi al di sotto dell’orbita di Giove.",
     "en": "And this place V is commonly lower than the orb of Jupiter.",
     "dipende_da": [],
     "figura": {
      "mostra": [
       "orbita di Giove"
      ],
      "evidenzia": [
       "SV < raggio dell’orbita di Giove"
      ]
     }
    },
    {
     "id": "L3-Lem4-p21",
     "la": "",
     "it": "La vicinanza delle comete è confermata anche dalla luce delle teste.",
     "en": "The near approach of the comets is farther confirmed from the light of their heads;",
     "dipende_da": [],
     "figura": {
      "mostra": [],
      "evidenzia": []
     }
    },
    {
     "id": "L3-Lem4-p22",
     "la": "",
     "it": "Lo splendore di un corpo celeste illuminato dal Sole, che si allontana verso regioni lontane, diminuisce infatti in rapporto quadruplicato della distanza: in rapporto duplicato, cioè, per l’aumento della distanza del corpo dal Sole, e in un altro rapporto duplicato per la diminuzione del diametro apparente.",
     "en": "for the light of a celestial body, illuminated by the sun, and receding to remote parts, is diminished in the quadruplicate proportion of the distance; to wit, in one duplicate proportion, on account of the increase of the distance from the sun, and in another duplicate proportion, on account of the decrease of the apparent diameter.",
     "dipende_da": [],
     "figura": {
      "mostra": [],
      "evidenzia": [
       "splendore ∝ 1/(distanza)⁴"
      ]
     }
    },
    {
     "id": "L3-Lem4-p23",
     "la": "",
     "it": "Perciò, se sono date sia la quantità di luce sia il diametro apparente di una cometa, sarà data la distanza, dicendo che la distanza sta alla distanza di un pianeta nel rapporto del diametro al diametro direttamente e nel rapporto subduplicato della luce alla luce inversamente.",
     "en": "Wherefore if both the quantity of light and the apparent diameter of a comet are given, its distance will be also given, by taking the distance of the comet to the distance of a planet in the direct proportion of their diameters and the reciprocal subduplicate proportion of their lights.",
     "dipende_da": [],
     "figura": {
      "mostra": [],
      "evidenzia": [
       "distanza ∝ diametro apparente / √luce"
      ]
     }
    },
    {
     "id": "L3-Lem4-p24",
     "la": "",
     "it": "Così il diametro minimo della capigliatura della cometa dell’anno 1682, osservato da Flamsteed con un tubo ottico di sedici piedi e misurato con il micrometro, era di 2′ 0″; il nucleo, invece, ossia la stella nel mezzo della testa, occupava appena la decima parte di questa larghezza, ed era quindi largo soltanto 11″ o 12″.",
     "en": "Thus, in the comet of the year 1682, Mr. Flamsted observed with a telescope of 16 feet, and measured with a micrometer, the least diameter of its head, 2' 00; but the nucleus or star in the middle of the head scarcely amounted to the tenth part of this measure; and therefore its diameter was only 11'' or 12'';",
     "dipende_da": [],
     "figura": {
      "mostra": [],
      "evidenzia": []
     },
     "nota": "Motte scrive «2' 00» senza il segno dei secondi e rende *capillitium* «head»."
    },
    {
     "id": "L3-Lem4-p25",
     "la": "",
     "it": "Per la luce e la chiarezza della testa, poi, superava la testa della cometa dell’anno 1680, e rivaleggiava con le stelle di prima o di seconda grandezza.",
     "en": "but in the light and splendor of its head it surpassed that of the comet in the year 1680, and might be compared with the stars of the first or second magnitude.",
     "dipende_da": [],
     "figura": {
      "mostra": [],
      "evidenzia": []
     }
    },
    {
     "id": "L3-Lem4-p26",
     "la": "",
     "it": "Supponiamo che Saturno con il suo anello fosse circa quattro volte più luminoso: poiché la luce dell’anello uguagliava all’incirca la luce del globo interno, e il diametro apparente del globo è circa 21″, e perciò la luce del globo e dell’anello insieme uguaglierebbe la luce di un globo il cui diametro fosse 30″, la distanza della cometa starà alla distanza di Saturno come 1 sta a √4 inversamente e 12″ sta a 30″ direttamente, cioè come 24 sta a 30, ossia 4 a 5.",
     "en": "Let us suppose that Saturn with its ring was about four times more lucid; and because the light of the ring was almost equal to the light of the globe within, and the apparent diameter of the globe is about 21'', and therefore the united light of both globe and ring would be equal to the light of a globe whose diameter is 30'', it follows that the distance of the comet was to the distance of Saturn as 1 to [SVG 1110] inversely, and 12'' to 30'' directly; that is, as 24 to 30, or 4 to 5.",
     "dipende_da": [],
     "figura": {
      "mostra": [],
      "evidenzia": [
       "21″ × √2 ≈ 30″",
       "(12/30) × √4 = 4/5"
      ]
     },
     "nota": "Verificato: 21″ × √2 = 29,7″; distanza cometa : Saturno = 0,8."
    }
   ]
  },
  {
   "id": "L3-P40",
   "tipo": "Propositio/Theorema",
   "titolo": "Prop. XL — le comete si muovono in sezioni coniche con il fuoco nel Sole",
   "copertura": [
    "III.G6.75",
    "III.G6.76"
   ],
   "fonti": {
    "la": "",
    "en": "Motte 1846, sezione corrispondente (Prop. XL)"
   },
   "enunciato": {
    "la": "",
    "it": "Le comete si muovono in sezioni coniche che hanno i fuochi nel centro del Sole, e con raggi condotti al Sole descrivono aree proporzionali ai tempi.",
    "en": "That the comets move in some of the conic sections, having their foci in the centre of the sun; and by radii drawn to the sun describe areas proportional to the times."
   },
   "passi": [
    {
     "id": "L3-P40-p1",
     "la": "",
     "it": "È evidente per il Cor. 1 della Prop. XIII del Libro I, confrontato con le Propp. VIII, XII e XIII del Libro III.",
     "en": "This proposition appears from Cor. 1, Prop. XIII, Book I, compared with Prop. VIII, XII, and XIII, Book III.",
     "dipende_da": [
      "Libro I, Prop. XIII, Cor. 1",
      "Libro III, Prop. VIII",
      "Libro III, Prop. XII",
      "Libro III, Prop. XIII"
     ],
     "figura": {
      "mostra": [
       "Sole nel fuoco",
       "orbita conica della cometa"
      ],
      "evidenzia": [
       "legge delle aree"
      ]
     }
    }
   ]
  },
  {
   "id": "L3-P40-Cor1",
   "tipo": "Corollarium",
   "titolo": "Prop. XL, Cor. 1 — orbite ellittiche e tempi periodici (240 anni)",
   "copertura": [
    "III.G6.77"
   ],
   "fonti": {
    "la": "",
    "en": "Motte 1846, sezione corrispondente (Prop. XL, Cor. 1)"
   },
   "dati": {
    "Saturno_anni": 30,
    "rapporto_assi": 4,
    "fattore": "4^(3/2) = 8",
    "risultato_anni": 240
   },
   "passi": [
    {
     "id": "L3-P40-Cor1-p1",
     "la": "",
     "it": "Di qui, se le comete ritornano in orbita, le orbite saranno ellissi, e i tempi periodici staranno ai tempi periodici dei pianeti in rapporto sesquiplicato degli assi principali.",
     "en": "Hence if comets are revolved in orbits returning into themselves, those orbits will be ellipses; and their periodic times be to the periodic times of the planets in the sesquiplicate proportion of their principal axes.",
     "dipende_da": [],
     "figura": {
      "mostra": [],
      "evidenzia": [
       "T ∝ asse^(3/2)"
      ]
     }
    },
    {
     "id": "L3-P40-Cor1-p2",
     "la": "",
     "it": "Perciò le comete, che si trovano per la maggior parte al di sopra dei pianeti, e per questo descrivono orbite con assi maggiori, gireranno più lentamente.",
     "en": "And therefore the comets, which for the most part of their course are higher than the planets, and upon that account describe orbits with greater axes, will require a longer time to finish their revolutions.",
     "dipende_da": [],
     "figura": {
      "mostra": [],
      "evidenzia": []
     }
    },
    {
     "id": "L3-P40-Cor1-p3",
     "la": "",
     "it": "Per esempio, se l’asse dell’orbita di una cometa è quattro volte maggiore dell’asse dell’orbita di Saturno, il tempo della rivoluzione della cometa starà al tempo della rivoluzione di Saturno, cioè a 30 anni, come √(4³) (ossia 8) sta a 1, e sarà perciò di 240 anni.",
     "en": "Thus if the axis of a comet's orbit was four times greater than the axis of the orbit of Saturn, the time of the revolution of the comet would be to the time of the revolution of Saturn, that is, to 30 years, as [SVG 1111] (or 8) to 1, and would therefore be 240 years.",
     "dipende_da": [],
     "figura": {
      "mostra": [],
      "evidenzia": [
       "30 × 4^(3/2) = 240"
      ]
     },
     "nota": "La trascrizione ha «√4 (seu 8)»: manca l’esponente; Motte [SVG 1111] = 4√4 (= 8). Verificato: 30 × 8 = 240."
    }
   ]
  },
  {
   "id": "L3-P40-Cor3",
   "tipo": "Corollarium",
   "titolo": "Prop. XL, Cor. 3 — velocità della cometa alla distanza della Terra",
   "copertura": [
    "III.G6.79"
   ],
   "fonti": {
    "la": "",
    "en": "Motte 1846, sezione corrispondente (Prop. XL, Cor. 3)"
   },
   "dati": {
    "raggio_orbe_magno": 100000000,
    "moto_diurno_Terra": {
     "Newton": 1720212,
     "ricalcolo": 1720212.4
    },
    "moto_orario_Terra": {
     "Newton": 71675.5,
     "ricalcolo": 71675.5
    },
    "moto_diurno_cometa": {
     "Newton": 2432747,
     "ricalcolo": 2432747.7
    },
    "moto_orario_cometa": {
     "Newton": 101364.5,
     "ricalcolo": 101364.5
    },
    "anno_siderale_giorni": 365.25636
   },
   "passi": [
    {
     "id": "L3-P40-Cor3-p1",
     "la": "",
     "it": "E perciò (per il Cor. 7 della Prop. XVI del Libro I) la velocità di ogni cometa starà sempre alla velocità di un pianeta qualsiasi che ruota in un cerchio intorno al Sole, con ottima approssimazione, in rapporto subduplicato del doppio della distanza del pianeta dal centro del Sole alla distanza della cometa dal centro del Sole.",
     "en": "And, therefore, by Cor. 7, Prop. XVI, Book I, the velocity of every comet will always be to the velocity of any planet, supposed to be revolved at the same distance in a circle about the sun, nearly in the subduplicate proportion of double the distance of the planet from the centre of the sun to the distance of the comet from the sun's centre, very nearly.",
     "dipende_da": [
      "Libro I, Prop. XVI, Cor. 7"
     ],
     "figura": {
      "mostra": [],
      "evidenzia": [
       "v(cometa) : v(pianeta in cerchio) = √(2 r(pianeta) : r(cometa))"
      ]
     },
     "nota": "Motte aggiunge «supposed to be revolved at the same distance» (contraddice la formula, che contiene due distanze diverse) e ripete «nearly … very nearly» (§ A.9)."
    },
    {
     "id": "L3-P40-Cor3-p2",
     "la": "",
     "it": "Supponiamo che il raggio dell’orbe magno, ossia il semidiametro massimo dell’ellisse in cui ruota la Terra, sia di 100000000 parti: la Terra con il suo moto diurno medio descriverà 1720212 parti, e con il moto orario 71675 1/2 parti.",
     "en": "Let us suppose the radius of the orbis magnus, or the greatest semi-diameter of the ellipsis which the earth describes, to consist of 100000000 parts; and then the earth by its mean diurnal motion will describe 1720212 of those parts, and [SVG 1112] by its horary motion.",
     "dipende_da": [],
     "figura": {
      "mostra": [],
      "evidenzia": [
       "2π × 10⁸ / 365,256 = 1720212"
      ]
     }
    },
    {
     "id": "L3-P40-Cor3-p3",
     "la": "",
     "it": "Perciò la cometa, alla stessa distanza media della Terra dal Sole, con una velocità che stia alla velocità della Terra come √2 sta a 1, descriverà con il suo moto diurno 2432747 parti, e con il moto orario 101364 1/2 parti.",
     "en": "And therefore the comet, at the same mean distance of the earth from the sun, with a velocity which is to the velocity of the earth as [SVG 1113] to 1, would by its diurnal motion describe 2432747 parts, and [SVG 1114] parts by its horary motion.",
     "dipende_da": [],
     "figura": {
      "mostra": [],
      "evidenzia": [
       "1720212 × √2 = 2432747"
      ]
     }
    },
    {
     "id": "L3-P40-Cor3-p4",
     "la": "",
     "it": "Alle distanze maggiori o minori, poi, il moto sia diurno sia orario starà a questo moto diurno e orario inversamente in rapporto subduplicato delle distanze, ed è perciò dato.",
     "en": "But at greater or less distances both the diurnal and horary motion will be to this diurnal and horary motion in the reciprocal subduplicate proportion of the distances, and is therefore given.",
     "dipende_da": [],
     "figura": {
      "mostra": [],
      "evidenzia": [
       "v ∝ 1/√r"
      ]
     }
    }
   ]
  },
  {
   "id": "L3-P40-Cor4",
   "tipo": "Corollarium",
   "titolo": "Prop. XL, Cor. 4 — area descritta in un giorno",
   "copertura": [
    "III.G6.80"
   ],
   "fonti": {
    "la": "",
    "en": "Motte 1846, sezione corrispondente (Prop. XL, Cor. 4)"
   },
   "dati": {
    "quadrato_raggio": 100000000,
    "lato_retto": "4 volte il raggio",
    "area_diurna": {
     "Newton": 1216373.5,
     "ricalcolo": 1216373.9
    },
    "area_oraria": {
     "Newton": 50682.25,
     "ricalcolo": 50682.2
    }
   },
   "passi": [
    {
     "id": "L3-P40-Cor4-p1",
     "la": "",
     "it": "Perciò, se il lato retto della parabola è quattro volte maggiore del raggio dell’orbe magno, e si pone che il quadrato di quel raggio sia di 100000000 parti, l’area che la cometa descrive ogni giorno con il raggio condotto al Sole sarà di 1216373 1/2 parti, e ogni ora quell’area sarà di 50682 1/4 parti.",
     "en": "Wherefore if the latus rectum of the parabola is quadruple of the radius of the orbis magnus, and the square of that radius is supposed to consist of 100000000 parts, the area which the comet will daily describe by a radius drawn to the sun will be [SVG 1115] parts, and the horary area will be [SVG 1116] parts.",
     "dipende_da": [],
     "figura": {
      "mostra": [],
      "evidenzia": [
       "area diurna = √2 × (½ R² × 2π/anno) = 1216373 1/2"
      ]
     }
    },
    {
     "id": "L3-P40-Cor4-p2",
     "la": "",
     "it": "Se invece il lato retto è maggiore o minore in un rapporto qualsiasi, l’area diurna e oraria sarà maggiore o minore nello stesso rapporto subduplicato.",
     "en": "But, if the latus rectum is greater or less in any proportion, the diurnal and horary area will be less or greater in the subduplicate of the same proportion reciprocally.",
     "dipende_da": [],
     "figura": {
      "mostra": [],
      "evidenzia": [
       "area ∝ √(lato retto)"
      ]
     },
     "nota": "Motte inverte il senso: «less or greater … reciprocally»; il latino «major vel minor in eadem ratione subduplicata» è corretto (area ∝ √lato retto, § A.9)."
    }
   ]
  },
  {
   "id": "L3-Lem5",
   "tipo": "Lemma",
   "titolo": "Lemma V — la curva di genere parabolico per punti dati (differenze di Newton)",
   "copertura": [
    "III.G6.81",
    "III.G6.82",
    "III.G6.83",
    "III.G6.84",
    "III.G6.85"
   ],
   "fonti": {
    "la": "",
    "en": "Motte 1846, sezione corrispondente (Lemma V)"
   },
   "enunciato": {
    "la": "",
    "it": "Trovare una linea curva di genere parabolico che passi per un numero qualsiasi di punti dati.",
    "en": "To find a curve line of the parabolic kind which shall pass through any given number of points."
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
     "I",
     "K",
     "L",
     "M",
     "N",
     "R",
     "S"
    ],
    "vincoli": [
     "HN retta data di posizione",
     "AH, BI, CK, DL, EM, FN perpendicolari su HN",
     "E ed F sotto la retta HN (lo richiedono i segni di DL + EM e −EM + FN)",
     "RS ordinata cercata, S su HN"
    ]
   },
   "nota": "«2b», «3b», «2c»… sono nomi (secondo, terzo termine della serie delle differenze), non prodotti; la trascrizione inserisce un segno di moltiplicazione invisibile (nota N7).",
   "passi": [
    {
     "id": "L3-Lem5-p1",
     "la": "",
     "it": "Siano quei punti A, B, C, D, E, F, ecc., e da essi abbassa su una retta qualsiasi HN, data di posizione, altrettante perpendicolari AH, BI, CK, DL, EM, FN.",
     "en": "Let those points be A, B, C, D, E, F, &c., and from the same to any right line HN, given in position, let fall as many perpendiculars AH, BI, CK, DL, EM, FN, &c.",
     "dipende_da": [],
     "figura": {
      "mostra": [
       "punti A…F",
       "retta HN",
       "perpendicolari AH…FN"
      ],
      "evidenzia": []
     }
    },
    {
     "id": "L3-Lem5-p2",
     "la": "",
     "it": "Se gli intervalli HI, IK, KL, ecc. dei punti H, I, K, L, M, N sono uguali, raccogli le differenze prime delle perpendicolari AH, BI, CK, ecc., b, 2b, 3b, 4b, 5b, ecc.; le seconde, c, 2c, 3c, 4c, ecc.; le terze, d, 2d, 3d, ecc.; in modo cioè che sia AH − BI = b, BI − CK = 2b, CK − DL = 3b, DL + EM = 4b, −EM + FN = 5b, ecc.; poi b − 2b = c, ecc.; e così si proceda fino all’ultima differenza, che qui è f.",
     "en": "If HI, IK, KL, &c., the intervals of the points H, I, K, L, M, N, &c., are equal, take b, 2b, 3b, 4b, 5b, &c., the first differences of the perpendiculars AH, BI, CK, &c.; their second differences c, 2c, 3c, 4c, &c.; their third, d, 2d, 3d, &c., that is to say, so as AH - BI may be = b, BI - CK = 2b, CK - DL = 3b, DL + EM = 4b, - EM + FN = 5b, &c.; then b - 2b = c, &c., and so on to the last difference, which is here f.",
     "dipende_da": [],
     "figura": {
      "mostra": [
       "intervalli uguali"
      ],
      "evidenzia": [
       "b = AH − BI, 2b = BI − CK, …",
       "c = b − 2b, …"
      ]
     }
    },
    {
     "id": "L3-Lem5-p3",
     "la": "",
     "it": "Poi, innalzata una perpendicolare qualsiasi RS, che sia un’ordinata della curva cercata, per trovarne la lunghezza poni che gli intervalli HI, IK, KL, LM, ecc. siano unità, e di’ AH = a, −HS = p, ½p moltiplicato per −IS = q, ⅓q moltiplicato per +SK = r, ¼r moltiplicato per +SL = s, ⅕s moltiplicato per +SM = t; procedendo cioè fino alla penultima perpendicolare ME, e premettendo segni negativi ai termini HS, IS, ecc., che giacciono dalla parte del punto S verso A, e segni positivi ai termini SK, SL, ecc., che giacciono dall’altra parte del punto S.",
     "en": "Then, erecting any perpendicular RS, which may be considered as an ordinate of the curve required, in order to find the length of this ordinate, suppose the intervals HI, IK, KL, LM, &c., to be units, and let [SVG 1117] , [SVG 1118] , [SVG 1119] into [SVG 1120] , [SVG 1121] into [SVG 1122] , [SVG 1123] into + SL = s, [SVG 1124] into + SM = t; proceeding, to wit, to ME, the last perpendicular but one, and prefixing negative signs before the terms HS, IS, &c., which lie from S towards A; and affirmative signs before the terms SK, SL, &c., which lie on the other side of the point S;",
     "dipende_da": [],
     "figura": {
      "mostra": [
       "RS"
      ],
      "evidenzia": [
       "p = −HS, q = ½p(−IS), r = ⅓q(+SK), …"
      ]
     }
    },
    {
     "id": "L3-Lem5-p4",
     "la": "",
     "it": "E, osservati bene i segni, sarà RS = a + bp + cq + dr + es + ft, ecc.",
     "en": "and, observing well the signs, RS will be = a + bp + cq + dr + es + ft, + &c.",
     "dipende_da": [],
     "figura": {
      "mostra": [],
      "evidenzia": [
       "RS = a + bp + cq + dr + es + ft"
      ]
     },
     "nota": "Verificato: coincide con il polinomio interpolatore di Lagrange (scarto 5·10⁻¹⁵)."
    },
    {
     "id": "L3-Lem5-p5",
     "la": "",
     "it": "Se invece gli intervalli HI, IK, ecc. dei punti H, I, K, L, ecc. sono disuguali, raccogli le differenze prime delle perpendicolari AH, BI, CK, ecc., divise per gli intervalli fra le perpendicolari, b, 2b, 3b, 4b, 5b; le seconde, divise per gli intervalli presi a due a due, c, 2c, 3c, 4c, ecc.; le terze, divise per gli intervalli presi a tre a tre, d, 2d, 3d, ecc.; le quarte, divise per gli intervalli presi a quattro a quattro, e, 2e, ecc.; e così di seguito; in modo cioè che sia b = (AH − BI)/HI, 2b = (BI − CK)/IK, 3b = (CK − DL)/KL, ecc.; poi c = (b − 2b)/HK, 2c = (2b − 3b)/IL, 3c = (3b − 4b)/KM, ecc.; quindi d = (c − 2c)/HL, 2d = (2c − 3c)/IM, ecc.",
     "en": "But if HI, IK, &c., the intervals of the points H, I, K, L, &c., are unequal, take b, 2b, 3b, 4b, 5b, &c., the first differences of the perpendiculars AH, BI, CK, &c., divided by the intervals between those perpendiculars; c, 2c, 3c, 4c, &c., their second differences, divided by the intervals between every two; d, 2d, 3d, &c., their third differences, divided by the intervals between every three; e, 2e, &c., their fourth differences, divided by the intervals between every four; and so forth; that is, in such manner, that b may be [SVG 1125] , 2b [SVG 1126] , 3b [SVG 1127] , &c., then c [SVG 1128] , 2c [SVG 1129] , 3c [SVG 1130] , &c., then d [SVG 1131] , 2d [SVG 1132] , &c.",
     "dipende_da": [],
     "figura": {
      "mostra": [
       "intervalli disuguali"
      ],
      "evidenzia": [
       "differenze divise: b = (AH − BI)/HI, c = (b − 2b)/HK, d = (c − 2c)/HL"
      ]
     }
    },
    {
     "id": "L3-Lem5-p6",
     "la": "",
     "it": "Trovate le differenze, di’ AH = a, −HS = p, p moltiplicato per −IS = q, q moltiplicato per +SK = r, r moltiplicato per +SL = s, s moltiplicato per +SM = t; procedendo cioè fino alla penultima perpendicolare ME; e sarà l’ordinata RS = a + bp + cq + dr + es + ft, ecc.",
     "en": "And those differences being found, let AH be = a, - HS = p, p into - IS = q, q into + SK = r, r into + SL = s, s into + SM = t; proceeding, to wit, to ME, the last perpendicular but one: and the ordinate RS will be = a + bp + cq + dr + es + ft, + &c.",
     "dipende_da": [],
     "figura": {
      "mostra": [],
      "evidenzia": [
       "RS = a + bp + cq + dr + es + ft"
      ]
     },
     "nota": "Verificato con intervalli casuali: scarto dalla Lagrange 1·10⁻¹³ (nota N7)."
    }
   ]
  },
  {
   "id": "L3-Lem6",
   "tipo": "Lemma",
   "titolo": "Lemma VI — il luogo della cometa in un tempo intermedio",
   "copertura": [
    "III.G6.86",
    "III.G6.87",
    "III.G6.88",
    "III.G6.89"
   ],
   "fonti": {
    "la": "",
    "en": "Motte 1846, sezione corrispondente (Lemma VI)"
   },
   "enunciato": {
    "la": "",
    "it": "Da alcuni luoghi osservati di una cometa trovare il suo luogo in un tempo intermedio qualsiasi dato.",
    "en": "Certain observed places of a comet being given, to find the place of the same to any intermediate given time."
   },
   "figura_base": {
    "punti": [
     "H",
     "I",
     "K",
     "L",
     "M",
     "A",
     "B",
     "C",
     "D",
     "E",
     "R",
     "S"
    ],
    "vincoli": [
     "ascisse = tempi delle osservazioni",
     "ordinate = longitudini osservate",
     "figura del Lemma V"
    ]
   },
   "passi": [
    {
     "id": "L3-Lem6-p1",
     "la": "",
     "it": "HI, IK, KL, LM rappresentino i tempi fra le osservazioni (nella figura precedente), HA, IB, KC, LD, ME cinque longitudini osservate della cometa, HS il tempo dato fra la prima osservazione e la longitudine cercata.",
     "en": "Let HI, IK, KL, LM (in the preceding Fig.), represent the times between the observations; HA, IB, KC, LD, ME, five observed longitudes of the comet; and HS the given time between the first observation and the longitude required.",
     "dipende_da": [],
     "figura": {
      "mostra": [
       "tempi HI…LM",
       "longitudini HA…ME",
       "tempo HS"
      ],
      "evidenzia": []
     }
    },
    {
     "id": "L3-Lem6-p2",
     "la": "",
     "it": "Se per i punti A, B, C, D, E s’intende condotta una curva regolare ABCDE, e per il lemma precedente se ne trova l’ordinata RS, RS sarà la longitudine cercata.",
     "en": "Then if a regular curve ABCDE is supposed to be drawn through the points A, B, C, D, E, and the ordinate RS is found out by the preceding lemma, RS will be the longitude required.",
     "dipende_da": [
      "Lemma V"
     ],
     "figura": {
      "mostra": [
       "curva ABCDE",
       "RS"
      ],
      "evidenzia": [
       "RS = longitudine al tempo HS"
      ]
     }
    },
    {
     "id": "L3-Lem6-p3",
     "la": "",
     "it": "Con lo stesso metodo, da cinque latitudini osservate si trova la latitudine in un tempo dato.",
     "en": "After the same method, from five observed latitudes, we may find the latitude to a given time.",
     "dipende_da": [],
     "figura": {
      "mostra": [],
      "evidenzia": []
     }
    },
    {
     "id": "L3-Lem6-p4",
     "la": "",
     "it": "Se le differenze delle longitudini osservate sono piccole, per esempio di soli 4 o 5 gradi, basteranno tre o quattro osservazioni per trovare la nuova longitudine e latitudine.",
     "en": "If the differences of the observed longitudes are small, suppose of 4 or 5 degrees, three or four observations will be sufficient to find a new longitude and latitude;",
     "dipende_da": [],
     "figura": {
      "mostra": [],
      "evidenzia": [
       "3–4 punti per differenze di 4–5°"
      ]
     }
    },
    {
     "id": "L3-Lem6-p5",
     "la": "",
     "it": "Se invece le differenze sono maggiori, per esempio di 10 o 20 gradi, si dovranno usare cinque osservazioni.",
     "en": "but if the differences are greater, as of 10 or 20 degrees, five observations ought to be used.",
     "dipende_da": [],
     "figura": {
      "mostra": [],
      "evidenzia": [
       "5 punti per differenze di 10–20°"
      ]
     }
    }
   ]
  },
  {
   "id": "L3-Lem7",
   "tipo": "Lemma",
   "titolo": "Lemma VII — per un punto dato, una retta divisa in un rapporto dato",
   "copertura": [
    "III.G6.90",
    "III.G6.91"
   ],
   "fonti": {
    "la": "",
    "en": "Motte 1846, sezione corrispondente (Lemma VII)"
   },
   "enunciato": {
    "la": "",
    "it": "Per un punto dato P condurre una linea retta BC le cui parti PB, PC, tagliate da due rette AB, AC date di posizione, abbiano fra loro un rapporto dato.",
    "en": "Through a given point P to draw a right line BC, whose parts PB, PC, cut off by two right lines AB, AC, given in position, may be one to the other in a given proportion."
   },
   "figura_base": {
    "punti": [
     "A",
     "B",
     "C",
     "P",
     "D",
     "E"
    ],
    "vincoli": [
     "AB, AC rette date per A",
     "P punto dato",
     "D su AB",
     "E sul prolungamento di DP oltre P con PE : PD = rapporto dato",
     "EC ∥ AD, C su AC",
     "B = CP ∩ AB"
    ]
   },
   "passi": [
    {
     "id": "L3-Lem7-p1",
     "la": "",
     "it": "Dal punto P a una delle due rette, AB, si conduca una retta qualsiasi PD, e la si prolunghi verso l’altra retta AC fino a E, in modo che PE stia a PD in quel rapporto dato.",
     "en": "From the given point P suppose any right line PD to be drawn to either of the right lines given, as AB; and produce the same towards AC, the other given right line, as far as E, so as PE may be to PD in the given proportion.",
     "dipende_da": [],
     "figura": {
      "mostra": [
       "PD",
       "E"
      ],
      "evidenzia": [
       "PE : PD = rapporto dato"
      ]
     }
    },
    {
     "id": "L3-Lem7-p2",
     "la": "",
     "it": "Sia EC parallela ad AD; e, se si conduce CPB, PC starà a PB come PE sta a PD. C.V.F.",
     "en": "Let EC be parallel to AD. Draw CPB, and PC will be to PB as PE to PD. Q.E.F.",
     "dipende_da": [],
     "figura": {
      "mostra": [
       "EC ∥ AD",
       "C",
       "retta CPB",
       "B"
      ],
      "evidenzia": [
       "triangoli simili PEC, PDB: PC : PB = PE : PD"
      ]
     },
     "nota": "Verificato su due figure di prova: PC/PB = 1,700 per il rapporto 1,7."
    }
   ]
  },
  {
   "id": "L3-Lem8",
   "tipo": "Lemma",
   "titolo": "Lemma VIII — la corda AC divisa in proporzione ai tempi",
   "copertura": [
    "III.G6.92",
    "III.G6.93",
    "III.G6.94"
   ],
   "fonti": {
    "la": "",
    "en": "Motte 1846, sezione corrispondente (Lemma VIII)"
   },
   "enunciato": {
    "la": "",
    "it": "Sia ABC una parabola con il fuoco S. Con la corda AC, divisa a metà in I, si tagli il segmento ABCI, il cui diametro sia Iμ e il vertice μ. Su Iμ prolungata si prenda μO uguale alla metà di Iμ. Si congiunga OS e la si prolunghi fino a ξ, in modo che Sξ sia uguale a 2SO. Se una cometa B si muove sull’arco CBA, e si conduce ξB che seca AC in E, dico che il punto E taglia dalla corda AC un segmento AE proporzionale al tempo, con ottima approssimazione.",
    "en": "Let ABC be a parabola, having its focus in S. By the chord AC bisected in I cut off the segment ABCI, whose diameter is [SVG 1133] and vertex [SVG 1134] . In [SVG 1133] produced take [SVG 1135] equal to one half of [SVG 1133] . Join OS, and produce it to [SVG 1136] as [SVG 1137] may be equal to 2SO. Now, supposing a comet to revolve in the arc CBA, draw [SVG 1138] , cutting AC in E; I say, the point E will cut off from the chord AC the segment AE, nearly proportional to the time."
   },
   "figura_base": {
    "punti": [
     "A",
     "B",
     "C",
     "S",
     "I",
     "μ",
     "O",
     "ξ",
     "E",
     "Y",
     "X"
    ],
    "vincoli": [
     "parabola ABC con fuoco S",
     "I punto medio di AC",
     "Iμ diametro (parallelo all’asse), μ sulla parabola, tangente in μ parallela ad AC",
     "O sul prolungamento di Iμ oltre μ, μO = Iμ/2",
     "ξ sul prolungamento di OS oltre S, Sξ = 2SO",
     "E = ξB ∩ AC",
     "Y = EO ∩ arco, X = EO ∩ tangente in μ"
    ]
   },
   "passi": [
    {
     "id": "L3-Lem8-p1",
     "la": "",
     "it": "Si congiunga infatti EO, che seca l’arco parabolico ABC in Y, e si conduca μX, che tocchi lo stesso arco nel vertice μ e incontri EO in X; l’area curvilinea AEXμA starà all’area curvilinea ACYμA come AE sta ad AC.",
     "en": "For if we join EO, cutting the parabolic arc ABC in Y, and draw [SVG 1139] touching the same arc in the vertex [SVG 1140] , and meeting EO in X, the curvilinear area [SVG 1141] will be to the curvilinear area [SVG 1142] as AE to AC;",
     "dipende_da": [],
     "figura": {
      "mostra": [
       "EO",
       "Y",
       "tangente μX",
       "X"
      ],
      "evidenzia": [
       "area AEXμA : area ACYμA = AE : AC"
      ]
     }
    },
    {
     "id": "L3-Lem8-p2",
     "la": "",
     "it": "Perciò, poiché il triangolo ASE sta al triangolo ASC nello stesso rapporto, l’area totale ASEXμA starà all’area totale ASCYμA come AE sta ad AC.",
     "en": "and, therefore, since the triangle ASE is to the triangle ASC in the same proportion, the whole area [SVG 1143] will be to the whole area [SVG 1144] as AE to AC.",
     "dipende_da": [],
     "figura": {
      "mostra": [
       "triangoli ASE, ASC"
      ],
      "evidenzia": [
       "ASEXμA : ASCYμA = AE : AC"
      ]
     }
    },
    {
     "id": "L3-Lem8-p3",
     "la": "",
     "it": "Ma, poiché ξO sta a SO come 3 sta a 1, ed EO sta a XO nello stesso rapporto, SX sarà parallela a EB; e perciò, se si congiunge BX, il triangolo SEB sarà uguale al triangolo XEB.",
     "en": "But, because [SVG 1145] is to SO as 3 to 1, and EO to XO in the same proportion, SX will be parallel to EB; and, therefore, joining BX, the triangle SEB will be equal to the triangle XEB.",
     "dipende_da": [],
     "figura": {
      "mostra": [
       "SX",
       "BX"
      ],
      "evidenzia": [
       "ξO : SO = EO : XO = 3 : 1 ⇒ SX ∥ EB",
       "SEB = XEB"
      ]
     }
    },
    {
     "id": "L3-Lem8-p4",
     "la": "",
     "it": "Quindi, se all’area ASEXμA si aggiunge il triangolo EXB, e dalla somma si toglie il triangolo SEB, resterà l’area ASBXμA uguale all’area ASEXμA, e quindi starà all’area ASCYμA come AE sta ad AC.",
     "en": "Wherefore if to the area [SVG 1143] we add the triangle EXB, and from the sum subduct the triangle SEB, there will remain the area [SVG 1146] , equal to the area [SVG 1143] ; and therefore in proportion to the area [SVG 1144] as AE to AC.",
     "dipende_da": [],
     "figura": {
      "mostra": [],
      "evidenzia": [
       "ASBXμA = ASEXμA"
      ]
     }
    },
    {
     "id": "L3-Lem8-p5",
     "la": "",
     "it": "Ma all’area ASBXμA è uguale, con ottima approssimazione, l’area ASBYμA; e questa area ASBYμA sta all’area ASCYμA come il tempo in cui è descritto l’arco AB sta al tempo in cui è descritto l’arco intero AC.",
     "en": "But the area [SVG 1147] is nearly equal to the area [SVG 1146] ; and this area [SVG 1147] is to the area [SVG 1144] as the time of description of the arc AB to the time of description of the whole arc AC;",
     "dipende_da": [
      "legge delle aree (implicito)"
     ],
     "figura": {
      "mostra": [
       "area ASBYμA"
      ],
      "evidenzia": [
       "ASBXμA ≈ ASBYμA",
       "area dal fuoco ∝ tempo"
      ]
     }
    },
    {
     "id": "L3-Lem8-p6",
     "la": "",
     "it": "Perciò AE sta ad AC nel rapporto dei tempi, con ottima approssimazione. C.V.D.",
     "en": "and, therefore, AE is to AC nearly in the proportion of the times. Q.E.D.",
     "dipende_da": [],
     "figura": {
      "mostra": [
       "E"
      ],
      "evidenzia": [
       "AE : AC ≈ t(AB) : t(AC)"
      ]
     },
     "nota": "Verificato su tre archi (90°, 80°, 70° di anomalia): scarto massimo 0,0013 della corda; esatto quando B = μ (Cor.) (nota N8)."
    }
   ]
  },
  {
   "id": "L3-Lem8-Schol",
   "tipo": "Scholium",
   "titolo": "Scolio del Lemma VIII — la correzione con il punto n",
   "copertura": [
    "III.G6.95"
   ],
   "fonti": {
    "la": "",
    "en": "Motte 1846, sezione corrispondente (Scholium del Lemma VIII)"
   },
   "figura_base": {
    "punti": [
     "μ",
     "ξ",
     "δ",
     "n",
     "B",
     "M",
     "I"
    ],
    "vincoli": [
     "δ = μξ ∩ AC",
     "n su μξ con ξn : μB = 27MI : 16Mμ",
     "M = Sμ ∩ AC (lettura richiesta dai Lemmi IX–X)"
    ]
   },
   "nota": "Verifica numerica (nota N8): la regola del verso (n oltre ξ se B è più lontano di μ dal vertice principale) è confermata; il coefficiente che corregge davvero, per archi piccoli, risulta 3/4 · MI/Mμ, cioè 12MI : 16Mμ, non 27MI : 16Mμ. Con 27 la correzione eccede. Da controllare sulla stampa e sulla figura.",
   "passi": [
    {
     "id": "L3-Lem8-Schol-p1",
     "la": "",
     "it": "Se si congiunge μξ, che seca AC in δ, e su di essa si prende ξn che stia a μB come 27MI sta a 16Mμ, la retta Bn, una volta condotta, segherà la corda AC nel rapporto dei tempi più esattamente di prima.",
     "en": "If we join [SVG 1148] cutting AC in [SVG 1149] ; and in it take [SVG 1150] in proportion to [SVG 1151] as 27MI to [SVG 1152] , and draw Bn, this Bn will cut the chord AC, in the proportion of the times, more accurately than before;",
     "dipende_da": [],
     "figura": {
      "mostra": [
       "μξ",
       "δ",
       "n",
       "Bn"
      ],
      "evidenzia": [
       "ξn : μB = 27MI : 16Mμ"
      ]
     }
    },
    {
     "id": "L3-Lem8-Schol-p2",
     "la": "",
     "it": "Il punto n si trovi poi al di là del punto ξ, se il punto B dista dal vertice principale della parabola più del punto μ; e al di qua, se ne dista meno.",
     "en": "but the point n is to be taken beyond or on this side the point [SVG 1136] , according as the point B is more or less distant from the principal vertex of the parabola than the point [SVG 1134] .",
     "dipende_da": [],
     "figura": {
      "mostra": [],
      "evidenzia": [
       "verso di n rispetto a ξ"
      ]
     }
    }
   ]
  },
  {
   "id": "L3-Lem9",
   "tipo": "Lemma",
   "titolo": "Lemma IX — Iμ = μM = AI²/4Sμ",
   "copertura": [
    "III.G6.96",
    "III.G6.97"
   ],
   "fonti": {
    "la": "",
    "en": "Motte 1846, sezione corrispondente (Lemma IX)"
   },
   "enunciato": {
    "la": "",
    "it": "Le rette Iμ e μM e la lunghezza AI²/4Sμ sono uguali fra loro.",
    "en": "The right lines [SVG 1153] and [SVG 1154] , and the length [SVG 1155] , are equal among themselves."
   },
   "figura_base": {
    "punti": [
     "I",
     "μ",
     "M",
     "A",
     "S"
    ],
    "vincoli": [
     "M = Sμ ∩ AC"
    ]
   },
   "passi": [
    {
     "id": "L3-Lem9-p1",
     "la": "",
     "it": "Infatti 4Sμ è il lato retto della parabola relativo al vertice μ.",
     "en": "For [SVG 1156] is the latus rectum of the parabola belonging to the vertex [SVG 1134] .",
     "dipende_da": [],
     "figura": {
      "mostra": [
       "lato retto 4Sμ relativo al diametro Iμ"
      ],
      "evidenzia": [
       "AI² = 4Sμ × Iμ",
       "μM = μI (triangolo isoscele: Sμ e il diametro fanno angoli uguali con la tangente ∥ AC)"
      ]
     },
     "nota": "La trascrizione ha «AIC4⁢Sμ»: «AIC» è refuso per «AIq» (Motte [SVG 1155] = AI²/4Sμ). Verificato numericamente: Iμ = μM = AI²/4Sμ su tre figure."
    }
   ]
  },
  {
   "id": "L3-Lem10",
   "tipo": "Lemma",
   "titolo": "Lemma X — la velocità all’altezza SP percorre la corda AC",
   "copertura": [
    "III.G6.98",
    "III.G6.99",
    "III.G6.100"
   ],
   "fonti": {
    "la": "",
    "en": "Motte 1846, sezione corrispondente (Lemma X)"
   },
   "enunciato": {
    "la": "",
    "it": "Si prolunghi Sμ fino a N e a P, in modo che μN sia la terza parte di μI, e SP stia a SN come SN sta a Sμ. Una cometa, nel tempo in cui descrive l’arco AμC, se procedesse sempre con la velocità che ha all’altezza uguale a SP, descriverebbe una lunghezza uguale alla corda AC.",
    "en": "Produce [SVG 1157] to N and P, so as [SVG 1158] may be one third of [SVG 1159] , and SP may be to SN as SN to [SVG 1160] ; and in the time that a comet would describe the arc [SVG 1161] , if it was supposed to move always forwards with the velocity which it hath in a height equal to SP, it would describe a length equal to the chord AC."
   },
   "figura_base": {
    "punti": [
     "S",
     "μ",
     "N",
     "P",
     "M",
     "A",
     "C",
     "I"
    ],
    "vincoli": [
     "N, P sul prolungamento di Sμ oltre μ",
     "μN = μI/3",
     "SP : SN = SN : Sμ",
     "M = Sμ ∩ AC"
    ]
   },
   "nota": "Il Corollario (III.G6.100) non ha dimostrazione propria: SP = (Sμ + ⅓Iμ)²/Sμ = Sμ + ⅔Iμ + Iμ²/9Sμ (nota N9).",
   "passi": [
    {
     "id": "L3-Lem10-p1",
     "la": "",
     "it": "Infatti, se la cometa, con la velocità che ha in μ, procedesse nello stesso tempo uniformemente lungo la retta che tocca la parabola in μ, l’area che descriverebbe con il raggio condotto al punto S sarebbe uguale all’area parabolica ASCμ.",
     "en": "For if the comet with the velocity which it hath in [SVG 1134] was in the said time supposed to move uniformly forward in the right line which touches the parabola in [SVG 1134] , the area which it would describe by a radius drawn to the point S would be equal to the parabolic area [SVG 1162] ;",
     "dipende_da": [
      "legge delle aree (implicito)"
     ],
     "figura": {
      "mostra": [
       "tangente in μ",
       "tratto uniforme sulla tangente"
      ],
      "evidenzia": [
       "area sulla tangente = area ASCμ"
      ]
     }
    },
    {
     "id": "L3-Lem10-p2",
     "la": "",
     "it": "Perciò il rettangolo formato dalla lunghezza descritta sulla tangente e dalla lunghezza Sμ starebbe al rettangolo formato dalle lunghezze AC e SM come l’area ASCμ sta al triangolo ASC, cioè come SN sta a SM.",
     "en": "and therefore the space contained under the length described in the tangent and the length [SVG 1157] would be to the space contained under the lengths AC and SM as the area [SVG 1162] to the triangle ASC, that is, as SN to SM.",
     "dipende_da": [],
     "figura": {
      "mostra": [
       "SM"
      ],
      "evidenzia": [
       "area ASCμ : triangolo ASC = SN : SM"
      ]
     }
    },
    {
     "id": "L3-Lem10-p3",
     "la": "",
     "it": "Perciò AC sta alla lunghezza descritta sulla tangente come Sμ sta a SN.",
     "en": "Wherefore AC is to the length described in the tangent as [SVG 1157] to SN.",
     "dipende_da": [],
     "figura": {
      "mostra": [],
      "evidenzia": [
       "AC : tangente = Sμ : SN"
      ]
     }
    },
    {
     "id": "L3-Lem10-p4",
     "la": "",
     "it": "Ma poiché la velocità della cometa all’altezza SP sta (per il Cor. 6 della Prop. XVI del Libro I) alla sua velocità all’altezza Sμ inversamente in rapporto subduplicato di SP a Sμ, cioè nel rapporto di Sμ a SN, la lunghezza descritta con questa velocità nello stesso tempo starà alla lunghezza descritta sulla tangente come Sμ sta a SN.",
     "en": "But since the velocity of the comet in the height SP (by Cor. 6, Prop. XVI., Book I) is to the velocity of the same in the height [SVG 1157] in the reciprocal subduplicate proportion of SP to [SVG 1157] , that is, in the proportion of [SVG 1157] to SN, the length described with this velocity will be to the length in the same time described in the tangent as [SVG 1157] to SN.",
     "dipende_da": [
      "Libro I, Prop. XVI, Cor. 6"
     ],
     "figura": {
      "mostra": [
       "SP"
      ],
      "evidenzia": [
       "v(SP) : v(Sμ) = √(Sμ : SP) = Sμ : SN"
      ]
     }
    },
    {
     "id": "L3-Lem10-p5",
     "la": "",
     "it": "Perciò AC e la lunghezza descritta con questa nuova velocità, poiché stanno nello stesso rapporto alla lunghezza descritta sulla tangente, sono uguali fra loro. C.V.D.",
     "en": "Wherefore since AC, and the length described with this new velocity, are in the same proportion to the length described in the tangent, they must be equal betwixt themselves. Q.E.D.",
     "dipende_da": [],
     "figura": {
      "mostra": [],
      "evidenzia": [
       "v(SP) × tempo = AC"
      ]
     },
     "nota": "Verificato: il risultato è esatto, non approssimato (scarto < 10⁻⁶ su tre figure; nota N9)."
    }
   ]
  },
  {
   "id": "L3-Lem11",
   "tipo": "Lemma",
   "titolo": "Lemma XI — la caduta con forza costante da SN percorre Iμ",
   "copertura": [
    "III.G6.101",
    "III.G6.102"
   ],
   "fonti": {
    "la": "",
    "en": "Motte 1846, sezione corrispondente (Lemma XI)"
   },
   "enunciato": {
    "la": "",
    "it": "Se una cometa, privata di ogni moto, fosse lasciata cadere dall’altezza SN, ossia Sμ + ⅓Iμ, in modo da cadere nel Sole, e fosse sempre sollecitata verso il Sole da quella forza, continuata uniformemente, da cui è sollecitata all’inizio, nella metà del tempo in cui descrive nella sua orbita l’arco AC descriverebbe con la sua discesa uno spazio uguale alla lunghezza Iμ.",
    "en": "If a comet void of all motion was let fall from the height SN, or [SVG 1164] , towards the sun, and was still impelled to the sun by the same force uniformly continued by which it was impelled at first, the same, in one half of that time in which it might describe the arc AC in its own orbit, would, in descending describe a space equal to the length [SVG 1153] ."
   },
   "figura_base": {
    "punti": [
     "S",
     "μ",
     "N",
     "P",
     "A",
     "C",
     "I"
    ],
    "vincoli": [
     "come nel Lemma X"
    ]
   },
   "passi": [
    {
     "id": "L3-Lem11-p1",
     "la": "",
     "it": "Infatti la cometa, nel tempo in cui descrive l’arco parabolico AC, nello stesso tempo, con la velocità che ha all’altezza SP (per l’ultimo lemma), descriverà la corda AC; e perciò (per il Cor. 7 della Prop. XVI del Libro I), ruotando nello stesso tempo per la forza della sua gravità in un cerchio il cui semidiametro fosse SP, descriverebbe un arco la cui lunghezza starebbe alla corda AC dell’arco parabolico in rapporto subduplicato dell’unità al due.",
     "en": "For in the same time that the comet would require to describe the parabolic arc AC, it would (by the last Lemma), with that velocity which it hath in the height SP, describe the chord AC: and, therefore (by Cor. 7, Prop. XVI, Book I), if it was in the same time supposed to revolve by the force of its own gravity in a circle whose semi-diameter was SP, it would describe an arc of that circle, the length of which would be to the chord of the parabolic arc AC in the subduplicate proportion of 1 to 2.",
     "dipende_da": [
      "Lemma X",
      "Libro I, Prop. XVI, Cor. 7"
     ],
     "figura": {
      "mostra": [
       "cerchio di raggio SP"
      ],
      "evidenzia": [
       "arco nel cerchio : AC = 1 : √2"
      ]
     }
    },
    {
     "id": "L3-Lem11-p2",
     "la": "",
     "it": "E perciò, con il peso che ha verso il Sole all’altezza SP, cadendo da quell’altezza verso il Sole, descriverebbe nella metà di quel tempo (per il Cor. 9 della Prop. IV del Libro I) uno spazio uguale al quadrato della metà di quella corda diviso per il quadruplo dell’altezza SP, cioè lo spazio AI²/4SP.",
     "en": "Wherefore if with that weight, which in the height SP it hath towards the sun, it should fall from that height towards the sun, it would (by Cor. 9, Prop. XVI, Book I) in half the said time describe a space equal to the square of half the said chord applied to quadruple the height SP, that is, it would describe the space [SVG 1165] .",
     "dipende_da": [
      "Libro I, Prop. IV, Cor. 9"
     ],
     "figura": {
      "mostra": [
       "caduta da SP con forza costante"
      ],
      "evidenzia": [
       "caduta in T/2 = (arco in T/2)²/(2SP) = AI²/4SP"
      ]
     },
     "nota": "Motte cita «Cor. 9, Prop. XVI, Book I»: il latino «corol. 9. prop. iv.» è quello giusto (Prop. IV, Cor. 9: arco medio proporzionale fra diametro e caduta) (§ A.8)."
    },
    {
     "id": "L3-Lem11-p3",
     "la": "",
     "it": "Perciò, poiché il peso della cometa verso il Sole all’altezza SN sta al suo peso verso il Sole all’altezza SP come SP sta a Sμ, la cometa, con il peso che ha all’altezza SN, cadendo nel Sole nello stesso tempo, descriverà lo spazio AI²/4Sμ, cioè uno spazio uguale alla lunghezza Iμ o Mμ. C.V.D.",
     "en": "But since the weight of the comet towards the sun in the height SN is to the weight of the same towards the sun in the height SP as SP to [SVG 1157] , the comet, by the weight which it hath in the height SN, in falling from that height towards the sun, would in the same time describe the space [SVG 1155] ; that is, a space equal to the length [SVG 1153] or [SVG 1154] . Q.E.D.",
     "dipende_da": [
      "Lemma IX (implicito)"
     ],
     "figura": {
      "mostra": [
       "caduta da SN"
      ],
      "evidenzia": [
       "peso(SN) : peso(SP) = SP : Sμ = SP² : SN²",
       "caduta = AI²/4Sμ = Iμ"
      ]
     },
     "nota": "Verificato: caduta in metà tempo = Iμ esattamente (nota N9)."
    }
   ]
  }
 ]
}
```

**Fine del Fascicolo 25b.**
