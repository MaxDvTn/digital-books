> **Copia pubblica.** In questa versione i campi `"la"` della Parte B sono vuoti: le frasi latine vengono dalla trascrizione del Newton Project, che non si ridistribuisce. Il latino del 1726 si legge su newtonproject.ox.ac.uk.

# Isaac Newton
# Principi matematici della filosofia naturale

## Fascicolo 25a — Libro III: l'inclinazione dell'orbita lunare, le equazioni della Luna e le forze del Sole e della Luna sul mare

**Nuova traduzione italiana di lavoro dal latino del 1726, confrontata con l'inglese di Andrew Motte nell'edizione del 1846.**

Versione 0.1 — 8 novembre 2026. Preparata con Claude (Anthropic) per Massimo Bosetti.

### Stato e perimetro

Questo fascicolo prosegue i Fascicoli 24a–24b (Libro III, Propp. XXI–XXXIII, con lo Scolio di Machin). Traduce la prima parte del gruppo G6 del Libro III: la **Proposizione XXXIV** (variazione oraria dell'inclinazione dell'orbita lunare) con quattro corollari; la **Proposizione XXXV** (l'inclinazione in un tempo dato) con il calcolo numerico che la segue e lo **Scolio** sulle equazioni della Luna (equazione annua, equazioni semestrali, epiciclo di Halley, seconda equazione del centro, ombra della Terra nelle eclissi, moti medi all'epoca 1700); la **Proposizione XXXVI** (forza del Sole sul mare) con il suo corollario; la **Proposizione XXXVII** (forza della Luna sul mare) con dieci corollari e il capoverso finale sull'attrazione magnetica. Il perimetro va dall'inizio del file latino fino a prima di «PROPOSITIO XXXVIII.». **Il seguito (Prop. XXXVIII, Lemmi I–XI, Ipotesi II, Propp. XXXIX–XL) è nella parte «b», Fascicolo 25b.** È una traduzione di lavoro, non un'edizione critica validata.

Gli identificatori **III.G6.01–III.G6.43** e i titoli tematici tra parentesi sono aggiunte editoriali. Servono a orientare la lettura e a controllare la completezza. I numeri romani delle proposizioni e dei problemi, e i numeri dei corollari, appartengono al testo originale. Le integrazioni del curatore sono tra parentesi quadre. Le note poste dopo la traduzione non fanno parte del testo di Newton.

In coda al fascicolo c'è la **Parte B**, con i dati strutturati per le pagine interattive: Prop. XXXIV e il suo Cor. 4; Prop. XXXV (costruzione e dimostrazione) e il calcolo della variazione totale; lo Scolio della Prop. XXXV (unità senza passi, con i dati numerici delle equazioni); Prop. XXXVI e il suo corollario; Prop. XXXVII (calcolo del rapporto 1 : 4,4815) e i suoi Cor. 3 e 7.

### Fonti effettivamente consultate

1. **Latino di riferimento.** Isaac Newton, *Philosophiæ Naturalis Principia Mathematica*, terza edizione, Londra, 1726, Libro III, **pp. 454–470** (la Prop. XXXIV comincia a p. 454, prima del marcatore ‹455›; il perimetro si chiude a p. 470, prima della Prop. XXXVIII). Trascrizione normalizzata del Newton Project, documento **NATP00303**, estratta in testo semplice senza correzioni: `fonti/latino-1726/latino-1726-L3-P34-40.md`, righe 1–117. Figure citate come [FIG] (Prop. XXXIV, Prop. XXXV due volte, Scolio, Prop. XXXVI), non disponibili.
2. **Inglese di confronto.** *Newton's Principia*, traduzione di Andrew Motte, New York, Daniel Adee, 1846 (Project Gutenberg n. 76404), estratto `fonti/motte-1846/motte-1846-L3-P34-40.md`, righe 1–657. L'estratto non ha marcatori di pagina: le pagine Motte sono indicate come «sezione corrispondente». Le formule stampate come immagini (`[SVG n]`) sono state lette nel loro LaTeX (`fonti/motte-1846/svg_tex.tsv`).
3. **Per i rimandi:** il latino degli altri gruppi del Libro III (`latino-1726-L3-P01-14.md`, `-P15-19.md`, `-P20.md`, `-P21-33.md`) e il Fascicolo 10 (Libro I, Sezione XI, Prop. LXVI).
4. **Brief comune**, **addendum del Libro II**, **istruzioni del Libro III**; Fascicoli 3, 5 e 20 come modelli di formato.

Non ho consultato né riprodotto traduzioni moderne. Non ho potuto vedere la stampa del 1726 né le figure originali: le relazioni geometriche sono ricostruite dalle sole lettere del testo.

### Criteri di traduzione

- Il testo guida è il latino; l'inglese di Motte serve a controllare le interpretazioni ed è annotato quando aggiunge, omette o si discosta.
- Si applicano il **glossario comune** del brief, il **glossario del Libro II** e il **glossario del Libro III** con i termini fissati dal coordinatore: *syzygiæ* «sizigie», *quadraturæ* «quadrature», *octantes* «ottanti», *apogæum / perigæum* «apogeo / perigeo», *aphelium / perihelium* «afelio / perielio», *nodi* «nodi», *æquatio* «equazione» (nota N1), *æquatio centri* «equazione del centro», *æquatio annua* «equazione annua», *motus medius* «moto medio», *locus verus* «luogo vero», *anomalia* «anomalia», *excentricitas* «eccentricità», *inclinatio* «inclinazione», *orbis magnus* «orbe magno» (nota N1), *orbis* (orbita) «orbita», *umbilicus* «fuoco», *sinus versus* «seno verso», *declinatio* «declinazione», *meridianus* «meridiano», *zenith* (*in vertice loci*) «zenit», *horizon* «orizzonte», *parallaxis* «parallasse», *eclipsis* «eclissi», *æstus maris* «marea», *fluxus / refluxus* «flusso / riflusso», *vis solis ad perturbandos motus lunæ* «forza del Sole che perturba i moti della Luna», *mediocris distantia* «distanza media», *quamproxime* «con ottima approssimazione», *in consequentia / in antecedentia* «in conseguenza / in antecedenza», *pes Parisiensis* «piede parigino», *linea* «linea», *milliare* «miglio», *st. vet.* «secondo il calendario giuliano (stile vecchio)», *ratio duplicata / triplicata* «rapporto duplicato / triplicato», *reciproce* «inversamente», *conjunctim* «considerati congiuntamente», *ducere in* «moltiplicare per», *impetus* «impeto», Q.E.D. «C.V.D.», Q.E.I. «C.V.T.».
- I nomi dei corpi celesti hanno la maiuscola anche dove il latino ha la minuscola. I segni zodiacali restano come simboli (nota N1).
- *Digitus* qui è una misura di lunghezza (piedi, pollici, linee): «pollice», secondo il glossario del Libro II, e non il «dito» delle eclissi (§ A.0).
- Le estensioni del glossario proprie di questo fascicolo sono elencate e motivate nel § A.0.
- Le espressioni appiattite della trascrizione sono ricostruite e scritte con la barra: «PpPG» = Pp/PG; «AZ×TZ12⁢AT» = (AZ × TZ)/(½AT); «16⁤78» = 16 7/8; «60⁤25» = 60⅖, e così via (§ A.6). I sessantesimi di secondo restano come nel testo: 33″ 10‴ 33iv (secondi, terzi, quarti; nota N2).
- Nessuna formula moderna entra nel testo tradotto. Le date e le coordinate restano come nel testo.

---

## Traduzione italiana

### Proposizione XXXIV. Problema XV (la variazione oraria dell'inclinazione)

**[III.G6.01]** **Trovare la variazione oraria dell'inclinazione dell'orbita lunare sul piano dell'eclittica.**

**[III.G6.02]** Rappresentino A e a le sizigie; Q e q le quadrature; N e n i nodi; P il luogo della Luna nella sua orbita; p la traccia di quel luogo sul piano dell'eclittica; e mTl il moto momentaneo dei nodi, come sopra. Se sulla linea Tm si abbassa la perpendicolare PG, si congiunge pG e la si prolunga finché incontri Tl in g, e si congiunge anche Pg, l'angolo PGp sarà l'inclinazione dell'orbita lunare sul piano dell'eclittica quando la Luna si trova in P, e l'angolo Pgp l'inclinazione della stessa orbita dopo che è trascorso un momento di tempo; e perciò l'angolo GPg sarà la variazione momentanea dell'inclinazione. Ora questo angolo GPg sta all'angolo GTg come TG sta a PG e Pp sta a PG, considerati congiuntamente. E perciò, se al momento di tempo si sostituisce un'ora, poiché l'angolo GTg (per la Prop. XXX) sta all'angolo di 33″ 10‴ 33ⁱᵛ come IT × PG × AZ sta a AT³, l'angolo GPg (ossia la variazione oraria dell'inclinazione) starà all'angolo di 33″ 10‴ 33ⁱᵛ come IT × AZ × TG × Pp/PG sta a AT³. C.V.T.

**[III.G6.03]** Queste cose stanno così nell'ipotesi che la Luna giri uniformemente in un'orbita circolare. Se invece quell'orbita è ellittica, il moto medio dei nodi diminuirà nel rapporto dell'asse minore all'asse maggiore, come si è esposto sopra; e nello stesso rapporto diminuirà anche la variazione dell'inclinazione.

**[III.G6.04]** *Cor. 1.* Se su Nn si innalza la perpendicolare TF, e pM è il moto orario della Luna nel piano dell'eclittica, e le perpendicolari pK, Mk, abbassate su QT e prolungate da entrambe le parti, incontrano TF in H e h, IT starà a AT come Kk sta a Mp, e TG a Hp come TZ a AT; e perciò IT × TG sarà uguale a Kk × Hp × TZ/Mp, cioè uguale all'area HpMh moltiplicata per il rapporto TZ/Mp; e perciò la variazione oraria dell'inclinazione starà a 33″ 10‴ 33ⁱᵛ come HpMh moltiplicata per AZ × TZ/Mp × Pp/PG sta a AT³.

**[III.G6.05]** *Cor. 2.* Perciò, se la Terra e i nodi, al compimento di ogni ora, fossero ritratti dai loro luoghi nuovi e ricondotti sempre in un istante ai luoghi di prima, così che la loro posizione restasse data per un intero mese periodico, la variazione totale dell'inclinazione nel tempo di quel mese starebbe a 33″ 10‴ 33ⁱᵛ come la somma di tutte le aree HpMh generate nella rivoluzione del punto p, e sommate con i loro segni + e −, moltiplicata per AZ × TZ × Pp/PG, sta a Mp × AT³; cioè come il cerchio intero QAqa moltiplicato per AZ × TZ × Pp/PG sta a Mp × AT³; ossia come la circonferenza QAqa moltiplicata per AZ × TZ × Pp/PG sta a 2Mp × AT².

**[III.G6.06]** *Cor. 3.* Quindi, in una data posizione dei nodi, la variazione oraria media, dalla quale, continuata uniformemente per un mese, potrebbe generarsi quella variazione mensile, sta a 33″ 10‴ 33ⁱᵛ come AZ × TZ × Pp/PG sta a 2AT², ossia come Pp × (AZ × TZ)/(½AT) sta a PG × 4AT; cioè (poiché Pp sta a PG come il seno dell'inclinazione suddetta sta al raggio, e (AZ × TZ)/(½AT) sta a 4AT come il seno del doppio dell'angolo ATn sta al quadruplo del raggio) come il seno della stessa inclinazione, moltiplicato per il seno del doppio della distanza dei nodi dal Sole, sta al quadruplo del quadrato del raggio.

**[III.G6.07]** *Cor. 4.* Poiché la variazione oraria dell'inclinazione, quando i nodi si trovano nelle quadrature, sta (per questa proposizione) all'angolo di 33″ 10‴ 33ⁱᵛ come IT × AZ × TG × Pp/PG sta a AT³, cioè come (IT × TG)/(½AT) × Pp/PG sta a 2AT, ossia come il seno del doppio della distanza della Luna dalle quadrature, moltiplicato per Pp/PG, sta al doppio del raggio, la somma di tutte le variazioni orarie nel tempo in cui la Luna, in questa posizione dei nodi, passa dalla quadratura alla sizigia (cioè nello spazio di 177⅙ ore) starà alla somma di altrettanti angoli di 33″ 10‴ 33ⁱᵛ, ossia 5878″, come la somma di tutti i seni del doppio della distanza della Luna dalle quadrature, moltiplicata per Pp/PG, sta alla somma di altrettanti diametri; cioè come il diametro moltiplicato per Pp/PG sta alla circonferenza; cioè, se l'inclinazione è di 5° 1′, come 7 × 874/10000 sta a 22, ossia come 278 sta a 10000. E perciò la variazione totale, risultante dalla somma di tutte le variazioni orarie nel tempo predetto, è di 163″, ossia 2′ 43″.

### Proposizione XXXV. Problema XVI (l'inclinazione in un tempo dato)

**[III.G6.08]** **Dato il tempo, trovare l'inclinazione dell'orbita lunare sul piano dell'eclittica.**

**[III.G6.09]** Sia AD il seno dell'inclinazione massima, e AB il seno dell'inclinazione minima. Si divida BD a metà in C, e con centro C e raggio BC si descriva il cerchio BGD. In AC si prenda CE in rapporto a EB come EB sta a 2BA; e se, al tempo dato, si costruisce l'angolo AEG uguale al doppio della distanza dei nodi dalle quadrature, e su AD si abbassa la perpendicolare GH, AH sarà il seno dell'inclinazione cercata.

**[III.G6.10]** Infatti GE² è uguale a GH² + HE² = BH × HD + HE² = HB × BD + HE² − BH² = HB × BD + BE² − 2BH × BE = BE² + 2EC × BH = 2EC × AB + 2EC × BH = 2EC × AH. Perciò, poiché 2EC è dato, GE² è come AH. Rappresenti ora AEg il doppio della distanza dei nodi dalle quadrature dopo che è trascorso un dato momento di tempo; l'arco Gg, per l'angolo dato GEg, sarà come la distanza GE. Ma Hh sta a Gg come GH sta a GC, e perciò Hh è come il prodotto GH × Gg, ossia GH × GE; cioè come GH/GE × GE², ossia GH/GE × AH; cioè come AH e il seno dell'angolo AEG considerati congiuntamente. Dunque, se AH in un caso qualsiasi è il seno dell'inclinazione, esso crescerà con gli stessi incrementi del seno dell'inclinazione, per il Cor. 3 della proposizione precedente, e perciò resterà sempre uguale a quel seno. Ma AH, quando il punto G cade in uno dei due punti B o D, è uguale a questo seno, e perciò gli resta sempre uguale. C.V.D.

**[III.G6.11]** In questa dimostrazione ho supposto che l'angolo BEG, che è il doppio della distanza dei nodi dalle quadrature, cresca uniformemente: non c'è infatti il tempo di soppesare tutte le minuzie delle disuguaglianze. Si immagini ora che l'angolo BEG sia retto, e che in questo caso Gg sia l'incremento orario della doppia distanza dei nodi e del Sole l'uno dall'altro; la variazione oraria dell'inclinazione, nello stesso caso (per il Cor. 3 dell'ultima proposizione), starà a 33″ 10‴ 33ⁱᵛ come il prodotto del seno AH dell'inclinazione e del seno dell'angolo retto BEG, che è il doppio della distanza dei nodi dal Sole, sta al quadruplo del quadrato del raggio; cioè come il seno AH dell'inclinazione media sta al quadruplo del raggio; ossia (poiché quell'inclinazione media è di circa 5° 8½′) come il suo seno 896 sta al quadruplo del raggio, 40000, ovvero come 224 sta a 10000. Ora la variazione totale, corrispondente alla differenza dei seni BD, sta a quella variazione oraria come il diametro BD sta all'arco Gg; cioè come il diametro BD sta alla semicirconferenza BGD e il tempo di 2079 7/10 ore, nel quale il nodo procede dalle quadrature alle sizigie, sta a un'ora, considerati congiuntamente; ossia come 7 sta a 11 e 2079 7/10 sta a 1. Perciò, se si compongono tutti i rapporti, la variazione totale BD starà a 33″ 10‴ 33ⁱᵛ come 224 × 7 × 2079 7/10 sta a 110000, cioè come 29645 sta a 1000, e di qui quella variazione BD risulterà di 16′ 23½″.

**[III.G6.12]** Questa è la variazione massima dell'inclinazione, in quanto non si considera il luogo della Luna nella sua orbita. Infatti l'inclinazione, se i nodi si trovano nelle sizigie, non cambia affatto per la diversa posizione della Luna. Ma se i nodi stanno nelle quadrature, l'inclinazione è minore quando la Luna si trova nelle sizigie che quando si trova nelle quadrature, per un eccesso di 2′ 43″, come abbiamo indicato nel Cor. 4 della proposizione precedente. E la variazione totale media BD, diminuita della metà di questo eccesso, 1′ 21½″, diventa 15′ 2″ nelle quadrature lunari, e aumentata della stessa diventa 17′ 45″ nelle sizigie della Luna. Se dunque la Luna è posta nelle sizigie, la variazione totale nel passaggio dei nodi dalle quadrature alle sizigie sarà di 17′ 45″; e perciò, se l'inclinazione, quando i nodi si trovano nelle sizigie, è di 5° 17′ 20″, la stessa, quando i nodi sono nelle quadrature e la Luna nelle sizigie, sarà di 4° 59′ 35″. E che le cose stiano così è confermato dalle osservazioni.

**[III.G6.13]** Se ora si desidera quell'inclinazione dell'orbita quando la Luna è nelle sizigie e i nodi in un luogo qualsiasi, si faccia AB stare a AD come il seno di 4° 59′ 35″ sta al seno di 5° 17′ 20″, e si prenda l'angolo AEG uguale al doppio della distanza dei nodi dalle quadrature: AH sarà il seno dell'inclinazione cercata. A questa inclinazione dell'orbita è uguale l'inclinazione della stessa orbita quando la Luna dista 90° dai nodi. Negli altri luoghi della Luna, la disuguaglianza mensile che la variazione dell'inclinazione comporta si compensa nel calcolo della latitudine della Luna, e in certo modo si elimina, per mezzo della disuguaglianza mensile del moto dei nodi (come abbiamo detto sopra); e perciò nel calcolo di quella latitudine può essere trascurata.

### Scolio (le equazioni della Luna)

**[III.G6.14]** Con questi calcoli dei moti lunari ho voluto mostrare che i moti lunari si possono calcolare a partire dalle loro cause per mezzo della teoria della gravità. Per mezzo della stessa teoria ho trovato inoltre che l'equazione annua del moto medio della Luna nasce dalla diversa dilatazione dell'orbita della Luna per effetto della forza del Sole, secondo il Cor. 6 della Prop. LXVI del Libro I. Questa forza è maggiore nel perigeo del Sole e dilata l'orbita della Luna; nel suo apogeo è minore e permette che quell'orbita si contragga. Nell'orbita dilatata la Luna ruota più lentamente, in quella contratta più velocemente; e l'equazione annua, con la quale si compensa questa disuguaglianza, è nulla nell'apogeo e nel perigeo del Sole, alla distanza media del Sole dalla Terra sale a circa 11′ 50″, negli altri luoghi è proporzionale all'equazione del centro del Sole; e si aggiunge al moto medio della Luna quando la Terra procede dal suo afelio al perielio, e si sottrae nella parte opposta dell'orbita. Assumendo il raggio dell'orbe magno di 1000 e l'eccentricità della Terra di 16 7/8, questa equazione, dove è massima, è risultata dalla teoria della gravità di 11′ 49″. Ma l'eccentricità della Terra sembra essere un poco maggiore, e, aumentata l'eccentricità, questa equazione deve aumentare nello stesso rapporto. Sia l'eccentricità di 16 11/12, e l'equazione massima sarà di 11′ 51″.

**[III.G6.15]** Ho trovato anche che nel perielio della Terra, a causa della maggiore forza del Sole, l'apogeo e i nodi della Luna si muovono più velocemente che nel suo afelio, e ciò nel rapporto triplicato inverso della distanza della Terra dal Sole. E di qui nascono equazioni annue di questi moti, proporzionali all'equazione del centro del Sole. Ora il moto del Sole è nel rapporto duplicato inverso della distanza della Terra dal Sole, e l'equazione massima del centro che questa disuguaglianza genera è di 1° 56′ 20″, corrispondente alla suddetta eccentricità del Sole di 16 11/12. Se il moto del Sole fosse nel rapporto triplicato inverso della distanza, questa disuguaglianza genererebbe l'equazione massima di 2° 54′ 30″. E perciò le equazioni massime che le disuguaglianze dei moti dell'apogeo e dei nodi della Luna generano stanno a 2° 54′ 30″ come il moto medio diurno dell'apogeo e il moto medio diurno dei nodi della Luna stanno al moto medio diurno del Sole. Di qui risulta l'equazione massima del moto medio dell'apogeo di 19′ 43″, e l'equazione massima del moto medio dei nodi di 9′ 24″. La prima equazione si aggiunge e la seconda si sottrae quando la Terra procede dal suo perielio all'afelio; e il contrario avviene nella parte opposta dell'orbita.

**[III.G6.16]** Dalla teoria della gravità è risultato anche che l'azione del Sole sulla Luna è un poco maggiore quando il diametro trasverso dell'orbita lunare passa per il Sole che quando lo stesso diametro è ad angoli retti con la linea che congiunge la Terra e il Sole; e perciò l'orbita lunare è un poco maggiore nel primo caso che nel secondo. E di qui nasce un'altra equazione del moto medio lunare, che dipende dalla posizione dell'apogeo della Luna rispetto al Sole: essa è massima quando l'apogeo della Luna si trova in ottante con il Sole, ed è nulla quando l'apogeo giunge alle quadrature o alle sizigie; e si aggiunge al moto medio nel passaggio dell'apogeo della Luna dalla quadratura del Sole alla sizigia, e si sottrae nel passaggio dell'apogeo dalla sizigia alla quadratura. Questa equazione, che chiamerò semestrale, negli ottanti dell'apogeo, quando è massima, sale a circa 3′ 45″, per quanto ho potuto ricavare dai fenomeni. Questa è la sua grandezza alla distanza media del Sole dalla Terra. Essa aumenta e diminuisce nel rapporto triplicato inverso della distanza del Sole, e perciò alla distanza massima del Sole è di 3′ 34″, e alla minima di 3′ 56″ con ottima approssimazione; quando invece l'apogeo della Luna è situato fuori degli ottanti, diventa minore, e sta all'equazione massima come il seno della doppia distanza dell'apogeo della Luna dalla sizigia o dalla quadratura più vicina sta al raggio.

**[III.G6.17]** Per la stessa teoria della gravità l'azione del Sole sulla Luna è un poco maggiore quando la retta condotta per i nodi della Luna passa per il Sole che quando quella linea è ad angoli retti con la retta che congiunge il Sole e la Terra. E di qui nasce un'altra equazione del moto medio lunare, che chiamerò seconda semestrale: essa è massima quando i nodi si trovano negli ottanti del Sole, si annulla quando sono nelle sizigie o nelle quadrature, e nelle altre posizioni dei nodi è proporzionale al seno della doppia distanza di uno dei due nodi dalla sizigia o dalla quadratura più vicina; si aggiunge al moto medio della Luna se il Sole dista dal nodo a lui più vicino in antecedenza, si sottrae se in conseguenza; e negli ottanti, dove è massima, sale a 47″ alla distanza media del Sole dalla Terra, come ricavo dalla teoria della gravità. Alle altre distanze del Sole questa equazione, massima negli ottanti dei nodi, è inversamente come il cubo della distanza del Sole dalla Terra, e perciò nel perigeo del Sole sale a circa 49″, nel suo apogeo a circa 45″.

**[III.G6.18]** Per la stessa teoria della gravità l'apogeo della Luna avanza al massimo quando è in congiunzione con il Sole o in opposizione a esso, e retrocede quando forma una quadratura con il Sole. E l'eccentricità diventa massima nel primo caso e minima nel secondo, per i Cor. 7, 8 e 9 della Prop. LXVI del Libro I. E queste disuguaglianze, per gli stessi corollari, sono molto grandi, e generano l'equazione principale dell'apogeo, che chiamerò semestrale. E l'equazione semestrale massima è di circa 12° 18′, per quanto ho potuto ricavare dalle osservazioni. Il nostro Horrocks per primo stabilì che la Luna ruota in un'ellisse attorno alla Terra, posta nel fuoco inferiore dell'ellisse. Halley collocò il centro dell'ellisse su un epiciclo, il cui centro ruota uniformemente attorno alla Terra. E dal moto sull'epiciclo nascono le disuguaglianze già dette nell'avanzamento e nella retrocessione dell'apogeo e nella grandezza dell'eccentricità. Si intenda divisa la distanza media della Luna dalla Terra in 100000 parti, e T rappresenti la Terra e TC l'eccentricità media della Luna, di 5505 parti. Si prolunghi TC fino a B, in modo che CB sia il seno dell'equazione semestrale massima di 12° 18′ rispetto al raggio TC; e il cerchio BDA, descritto con centro C e raggio CB, sarà quell'epiciclo sul quale è collocato il centro dell'orbita lunare e sul quale esso ruota secondo l'ordine delle lettere BDA. Si prenda l'angolo BCD uguale al doppio dell'argomento annuo, ossia alla doppia distanza del luogo vero del Sole dall'apogeo della Luna equato una volta: CTD sarà l'equazione semestrale dell'apogeo della Luna, e TD l'eccentricità della sua orbita, diretta verso l'apogeo equato due volte. Avuti poi il moto medio della Luna, l'apogeo e l'eccentricità, e anche l'asse maggiore dell'orbita di 200000 parti, da questi dati si ricaverà il luogo vero della Luna nell'orbita e la sua distanza dalla Terra, e ciò con metodi notissimi.

**[III.G6.19]** Nel perielio della Terra, a causa della maggiore forza del Sole, il centro dell'orbita della Luna si muove attorno al centro C più velocemente che nell'afelio, e ciò nel rapporto triplicato inverso della distanza della Terra dal Sole. Per l'equazione del centro del Sole compresa nell'argomento annuo, il centro dell'orbita della Luna si muove più velocemente sull'epiciclo BDA nel rapporto duplicato inverso della distanza della Terra dal Sole. Perché si muova ancora più velocemente, nel rapporto semplice inverso della distanza, dal centro dell'orbita D si conduca la retta DE verso l'apogeo della Luna, ossia parallela alla retta TC, e si prenda l'angolo EDF uguale all'eccesso dell'argomento annuo predetto sulla distanza dell'apogeo della Luna dal perigeo del Sole in conseguenza; o, ciò che è lo stesso, si prenda l'angolo CDF uguale al complemento a 360° dell'anomalia vera del Sole. E DF stia a DC come il doppio dell'eccentricità dell'orbe magno sta alla distanza media del Sole dalla Terra e il moto medio diurno del Sole dall'apogeo della Luna sta al moto medio diurno del Sole dal proprio apogeo, considerati congiuntamente; cioè come 33 7/8 sta a 1000 e 52′ 27″ 16‴ a 59′ 8″ 10‴, considerati congiuntamente, ossia come 3 sta a 100. E si immagini che il centro dell'orbita della Luna sia collocato nel punto F e ruoti su un epiciclo, il cui centro è D e il raggio DF, mentre il punto D avanza sulla circonferenza del cerchio DABD. In questo modo, infatti, la velocità con cui il centro dell'orbita della Luna si muoverà lungo una certa linea curva descritta attorno al centro C sarà inversamente come il cubo della distanza del Sole dalla Terra, con ottima approssimazione, come deve essere.

**[III.G6.20]** Il calcolo di questo moto è difficile, ma sarà reso più facile dall'approssimazione seguente. Se la distanza media della Luna dalla Terra è di 100000 parti, e l'eccentricità TC è di 5505 parti come sopra, la retta CB o CD si troverà di 1172¾ parti, e la retta DF di 35⅕ parti. E questa retta, alla distanza TC, sottende nella Terra l'angolo che la traslazione del centro dell'orbita dal luogo D al luogo F genera nel moto di questo centro; e la stessa retta raddoppiata, in posizione parallela, alla distanza del fuoco superiore dell'orbita della Luna dalla Terra, sottende lo stesso angolo, cioè quello che quella traslazione genera nel moto del fuoco; e alla distanza della Luna dalla Terra sottende l'angolo che la stessa traslazione genera nel moto della Luna, e che perciò si può chiamare seconda equazione del centro. E questa equazione, alla distanza media della Luna dalla Terra, è come il seno dell'angolo che quella retta DF forma con la retta condotta dal punto F alla Luna, con ottima approssimazione, e dove è massima risulta di 2′ 25″. L'angolo poi che la retta DF e la retta condotta dal punto F alla Luna comprendono si trova o sottraendo l'angolo EDF dall'anomalia media della Luna, o aggiungendo la distanza della Luna dal Sole alla distanza dell'apogeo della Luna dall'apogeo del Sole. E come il raggio sta al seno dell'angolo così trovato, così 2′ 25″ stanno alla seconda equazione del centro, da aggiungere se quella somma è minore di un semicerchio, da sottrarre se è maggiore. Così se ne avrà la longitudine nelle sizigie stesse dei luminari.

**[III.G6.21]** Poiché l'atmosfera della Terra, fino all'altezza di 35 o 40 miglia, rifrange la luce del Sole, e rifrangendola la diffonde nell'ombra della Terra, e diffondendo la luce al confine dell'ombra dilata l'ombra, al diametro dell'ombra che risulta dalla parallasse aggiungo, nelle eclissi di Luna, un minuto primo, oppure un minuto e un terzo.

**[III.G6.22]** La teoria della Luna, poi, deve essere esaminata e fissata per mezzo dei fenomeni, prima nelle sizigie, poi nelle quadrature e infine negli ottanti. E chi si accingerà a quest'opera adopererà non a sproposito, per il mezzogiorno all'osservatorio reale di Greenwich, nell'ultimo giorno del mese di dicembre dell'anno 1700 secondo il calendario giuliano (stile vecchio), i seguenti moti medi: cioè il moto medio del Sole ♑ 20° 43′ 40″, e del suo apogeo ♋ 7° 44′ 30″; il moto medio della Luna ♒ 15° 21′ 00″, e del suo apogeo ♓ 8° 20′ 00″, e del nodo ascendente ♌ 27° 24′ 20″; e la differenza dei meridiani fra questo osservatorio e l'osservatorio reale di Parigi di 0 ore 9 minuti 20 secondi. I moti medi della Luna e del suo apogeo, però, non si conoscono ancora con sufficiente esattezza.

### Proposizione XXXVI. Problema XVII (la forza del Sole sul mare)

**[III.G6.23]** **Trovare la forza del Sole per muovere il mare.**

**[III.G6.24]** La forza ML, ossia PT, con cui il Sole perturba i moti lunari nelle quadrature lunari, stava (per la Prop. XXV di questo Libro) alla forza di gravità presso di noi come 1 sta a 638092,6. E la forza TM − LM, ossia 2PK, nelle sizigie lunari è doppia. Queste forze poi, se si scende alla superficie della Terra, diminuiscono nel rapporto delle distanze dal centro della Terra, cioè nel rapporto di 60½ a 1; e perciò la prima forza, sulla superficie della Terra, sta alla forza di gravità come 1 sta a 38604600. Per effetto di questa forza il mare si abbassa nei luoghi che distano 90 gradi dal Sole. Per effetto dell'altra, che è doppia, il mare si innalza sia sotto il Sole sia nella regione opposta al Sole. La somma delle forze sta alla forza di gravità come 1 sta a 12868200. E poiché la stessa forza suscita lo stesso moto, sia che abbassi l'acqua nelle regioni che distano 90 gradi dal Sole, sia che la innalzi nelle regioni sotto il Sole e opposte al Sole, questa somma sarà la forza totale del Sole per agitare il mare; e avrà lo stesso effetto che se innalzasse tutta quanta il mare nelle regioni sotto il Sole e opposte al Sole, e nelle regioni che distano 90 gradi dal Sole non agisse affatto.

**[III.G6.25]** Questa è la forza del Sole per suscitare il mare in un luogo qualsiasi dato, quando il Sole si trova insieme allo zenit del luogo e alla sua distanza media dalla Terra. Nelle altre posizioni del Sole la forza per sollevare il mare è come il seno verso del doppio dell'altezza del Sole sopra l'orizzonte del luogo, direttamente, e come il cubo della distanza del Sole dalla Terra, inversamente.

**[III.G6.26]** *Cor.* Poiché la forza centrifuga delle parti della Terra, che nasce dal moto diurno della Terra e sta alla forza di gravità come 1 sta a 289, fa sì che l'altezza dell'acqua sotto l'equatore superi la sua altezza sotto i poli della misura di 85472 piedi parigini, come sopra nella Prop. XIX, la forza solare di cui abbiamo trattato, poiché sta alla forza di gravità come 1 sta a 12868200, e perciò a quella forza centrifuga come 289 sta a 12868200, ossia come 1 sta a 44527, farà sì che l'altezza dell'acqua nelle regioni sotto il Sole e opposte al Sole superi la sua altezza nei luoghi che distano 90 gradi dal Sole della misura di appena un piede parigino e undici pollici e un trentesimo di pollice. Questa misura sta infatti alla misura di 85472 piedi come 1 sta a 44527.

### Proposizione XXXVII. Problema XVIII (la forza della Luna sul mare)

**[III.G6.27]** **Trovare la forza della Luna per muovere il mare.**

**[III.G6.28]** La forza della Luna per muovere il mare si deve ricavare dalla sua proporzione alla forza del Sole, e questa proporzione si deve ricavare dalla proporzione dei moti del mare che nascono da queste forze. Davanti alla foce del fiume Avon, alla terza pietra miliare sotto Bristol, in primavera e in autunno la salita totale dell'acqua nella congiunzione e nell'opposizione dei luminari, secondo le osservazioni di Samuel Sturmy, è di circa 45 piedi, nelle quadrature invece di appena 25 piedi. La prima altezza nasce dalla somma delle forze, la seconda dalla loro differenza. Siano dunque S e L le forze del Sole e della Luna quando si trovano nell'equatore e a distanza media dalla Terra: L + S starà a L − S come 45 sta a 25, ossia come 9 sta a 5.

**[III.G6.29]** Nel porto di Plymouth la marea, secondo le osservazioni di Samuel Colepress, si innalza in altezza media a circa sedici piedi, e in primavera e in autunno l'altezza della marea nelle sizigie può superare la sua altezza nelle quadrature di sette o otto piedi. Se la differenza massima di queste altezze è di nove piedi, L + S starà a L − S come 20½ sta a 11½, ossia come 41 sta a 23. Questa proporzione concorda abbastanza con la prima. Per la grandezza della marea nel porto di Bristol, sembra che ci si debba fidare di più delle osservazioni di Sturmy; e perciò, finché non si sarà stabilito qualcosa di più certo, useremo la proporzione di 9 a 5.

**[III.G6.30]** Del resto, a causa dei moti alterni delle acque, le maree massime non cadono nelle sizigie stesse dei luminari, ma sono le terze dopo le sizigie, come si è detto, ossia seguono da vicino il terzo passaggio della Luna al meridiano del luogo dopo le sizigie; o piuttosto (come nota Sturmy) sono le terze dopo il giorno del novilunio o del plenilunio, ossia dopo circa la dodicesima ora dal novilunio o dal plenilunio, e perciò cadono circa nella quarantatreesima ora dal novilunio o dal plenilunio. In questo porto cadono poi circa nella settima ora dal passaggio della Luna al meridiano del luogo; e perciò seguono da vicino il passaggio della Luna al meridiano quando la Luna dista dal Sole, o dall'opposizione del Sole, di circa diciotto o diciannove gradi in conseguenza. L'estate e l'inverno raggiungono il loro culmine non nei solstizi stessi, ma quando il Sole dista dai solstizi circa un decimo dell'intero giro, ossia circa 36 o 37 gradi. E similmente la marea massima nasce dal passaggio della Luna al meridiano del luogo quando la Luna dista dal Sole circa un decimo dell'intero moto da una marea all'altra. Sia quella distanza di circa 18½ gradi. E la forza del Sole, a questa distanza della Luna dalle sizigie e dalle quadrature, sarà minore, per accrescere e per diminuire il moto del mare che nasce dalla forza della Luna, che nelle sizigie e nelle quadrature stesse, nel rapporto del raggio al seno del complemento del doppio di questa distanza, ossia di un angolo di 37 gradi, cioè nel rapporto di 10000000 a 7986355. E perciò nella proporzione precedente al posto di S si deve scrivere 0,7986355 S.

**[III.G6.31]** Ma anche la forza della Luna nelle quadrature deve essere diminuita, a causa della declinazione della Luna dall'equatore. Infatti la Luna nelle quadrature, o piuttosto a 18½ gradi dopo le quadrature, si trova a una declinazione di circa 22° 13′. E la forza di un luminare che declina dall'equatore per muovere il mare diminuisce, con ottima approssimazione, nel rapporto duplicato del seno del complemento della declinazione. E perciò la forza della Luna in queste quadrature è soltanto 0,8570327 L. Dunque L + 0,7986355 S sta a 0,8570327 L − 0,7986355 S come 9 sta a 5.

**[III.G6.32]** Inoltre i diametri dell'orbita nella quale la Luna dovrebbe muoversi senza eccentricità stanno fra loro come 69 sta a 70; e perciò la distanza della Luna dalla Terra nelle sizigie sta alla sua distanza nelle quadrature come 69 sta a 70, a parità delle altre condizioni. E le sue distanze a 18½ gradi dalle sizigie, dove si genera la marea massima, e a 18½ gradi dalle quadrature, dove si genera la marea minima, stanno alla sua distanza media come 69,098747 e 69,897345 stanno a 69½. Le forze della Luna per muovere il mare sono poi nel rapporto triplicato inverso delle distanze, e perciò le forze alla massima e alla minima di queste distanze stanno alla forza alla distanza media come 0,9830427 e 1,017522 stanno a 1. Di qui risulta che 1,017522 L + 0,7986355 S sta a 0,9830427 × 0,8570327 L − 0,7986355 S come 9 sta a 5; e S sta a L come 1 sta a 4,4815. Perciò, poiché la forza del Sole sta alla forza di gravità come 1 sta a 12868200, la forza della Luna starà alla forza di gravità come 1 sta a 2871400.

**[III.G6.33]** *Cor. 1.* Poiché l'acqua agitata dalla forza del Sole sale all'altezza di un piede e undici pollici e un trentesimo di pollice, per la forza della Luna salirà all'altezza di otto piedi e 7 5/22 pollici, e per entrambe le forze all'altezza di dieci piedi e mezzo, e, quando la Luna è nel perigeo, all'altezza di dodici piedi e mezzo e oltre, soprattutto quando la marea è aiutata dal soffiare dei venti. Una forza così grande basta abbondantemente a suscitare tutti i moti del mare, e corrisponde bene alla quantità dei moti. Infatti nei mari che si estendono ampiamente da oriente a occidente, come nel mare Pacifico e nelle parti del mare Atlantico ed Etiopico fuori dei tropici, l'acqua suole innalzarsi all'altezza di sei, nove, dodici o quindici piedi. Nel mare Pacifico, poi, che è più profondo e si estende più ampiamente, si dice che le maree siano maggiori che nell'Atlantico e nell'Etiopico. Perché la marea sia piena, infatti, l'estensione del mare da oriente a occidente non deve essere minore di novanta gradi. Nel mare Etiopico la salita dell'acqua dentro i tropici è minore che nelle zone temperate, a causa della strettezza del mare fra l'Africa e la parte australe dell'America. In mezzo al mare l'acqua non può salire se non scende contemporaneamente presso entrambe le coste, l'orientale e l'occidentale; mentre invece nei nostri mari stretti deve scendere presso quelle coste a vicenda alterna. Per questa ragione il flusso e il riflusso, nelle isole che distano moltissimo dalle coste, suole essere piccolissimo. In certi porti, dove l'acqua è costretta a entrare e a uscire con grande impeto attraverso luoghi poco profondi, per riempire e svuotare a vicenda alterna delle insenature, il flusso e il riflusso devono essere maggiori del solito, come a Plymouth e al ponte di Chepstow in Inghilterra; presso i monti di San Michele e la città degli Abrincati (volgarmente Avranches) in Normandia; a Cambay e a Pegu nelle Indie orientali. In questi luoghi il mare, avanzando e ritirandosi con grande velocità, ora inonda le coste, ora le lascia asciutte per molte miglia. E l'impeto dell'afflusso e del ritorno non può essere spezzato prima che l'acqua si sia innalzata o abbassata fino a 30, 40 o 50 piedi e più. E la stessa ragione vale per gli stretti lunghi e poco profondi, come quello di Magellano e quello da cui l'Inghilterra è circondata. La marea in porti e stretti di questo genere è accresciuta oltre misura dall'impeto dell'andata e del ritorno. Presso le coste, invece, che guardano con discesa ripida verso il mare profondo e aperto, dove l'acqua può innalzarsi e abbassarsi senza impeto di deflusso e di ritorno, la grandezza della marea corrisponde alle forze del Sole e della Luna.

**[III.G6.34]** *Cor. 2.* Poiché la forza della Luna per muovere il mare sta alla forza di gravità come 1 sta a 2871400, è evidente che quella forza è di gran lunga minore di quella che si potrebbe percepire negli esperimenti con i pendoli, o in qualsiasi esperimento statico o idrostatico. Soltanto nella marea questa forza produce un effetto sensibile.

**[III.G6.35]** *Cor. 3.* Poiché la forza della Luna per muovere il mare sta alla forza analoga del Sole come 4,4815 sta a 1, e quelle forze (per il Cor. 14 della Prop. LXVI del Libro I) sono come le densità dei corpi della Luna e del Sole e i cubi dei diametri apparenti considerati congiuntamente, la densità della Luna starà alla densità del Sole come 4,4815 sta a 1, direttamente, e come il cubo del diametro della Luna sta al cubo del diametro del Sole, inversamente; cioè (poiché i diametri apparenti medi della Luna e del Sole sono di 31′ 16½″ e 32′ 12″) come 4891 sta a 1000. Ma la densità del Sole stava alla densità della Terra come 1000 sta a 4000; e perciò la densità della Luna sta alla densità della Terra come 4891 sta a 4000, ossia come 11 sta a 9. Il corpo della Luna è dunque più denso e più terroso della nostra Terra.

**[III.G6.36]** *Cor. 4.* E poiché il diametro vero della Luna, dalle osservazioni astronomiche, sta al diametro vero della Terra come 100 sta a 365, la massa della Luna starà alla massa della Terra come 1 sta a 39,788.

**[III.G6.37]** *Cor. 5.* E la gravità acceleratrice sulla superficie della Luna sarà circa tre volte minore della gravità acceleratrice sulla superficie della Terra.

**[III.G6.38]** *Cor. 6.* E la distanza del centro della Luna dal centro della Terra starà alla distanza del centro della Luna dal centro comune di gravità della Terra e della Luna come 40,788 sta a 39,788.

**[III.G6.39]** *Cor. 7.* E la distanza media del centro della Luna dal centro della Terra, negli ottanti della Luna, sarà di 60⅖ semidiametri massimi della Terra, con ottima approssimazione. Infatti il semidiametro massimo della Terra era di 19658600 piedi parigini, e la distanza media dei centri della Terra e della Luna, composta di 60⅖ semidiametri di questo genere, è uguale a 1187379440 piedi. E questa distanza (per il corollario precedente) sta alla distanza del centro della Luna dal centro comune di gravità della Terra e della Luna come 40,788 sta a 39,788; e perciò la seconda distanza è di 1158268534 piedi. E poiché la Luna compie la sua rivoluzione, rispetto alle stelle fisse, in 27 giorni, 7 ore e 43 4/9 minuti, il seno verso dell'angolo che la Luna descrive nel tempo di un minuto è 12752341, essendo il raggio 1000,000000,000000. E come il raggio sta a questo seno verso, così 1158268534 piedi stanno a 14,7706353 piedi. La Luna dunque, cadendo verso la Terra per quella forza con cui è trattenuta nell'orbita, nel tempo di un minuto descriverà 14,7706353 piedi. E aumentando questa forza nel rapporto di 178 29/40 a 177 29/40, si avrà la forza totale della gravità nell'orbita della Luna, per il Cor. della Prop. III. E per questa forza la Luna, cadendo, nel tempo di un minuto descriverà 14,8538067 piedi. E alla sessantesima parte della distanza della Luna dal centro della Terra, cioè alla distanza di 197896573 piedi dal centro della Terra, un corpo grave, cadendo nel tempo di un secondo, descriverà anch'esso 14,8538067 piedi. E perciò alla distanza di 19615800 piedi, che costituiscono il semidiametro medio della Terra, un grave cadendo descriverà 15,11175 piedi, ossia 15 piedi, 1 pollice e 4 1/11 linee. Questa sarà la caduta dei corpi alla latitudine di 45 gradi. E per la tabella precedente, descritta nella Prop. XX, la caduta sarà un poco maggiore alla latitudine di Parigi, con un eccesso di circa 2/3 di linea. Per questo calcolo, dunque, i gravi alla latitudine di Parigi, cadendo nel vuoto, descriveranno nel tempo di un secondo circa 15 piedi parigini, 1 pollice e 4 25/33 linee. E se la gravità si diminuisce togliendo la forza centrifuga che nasce dal moto diurno della Terra a quella latitudine, i gravi lì, cadendo, descriveranno nel tempo di un secondo 15 piedi, 1 pollice e 1½ linee. E con questa velocità cadono i gravi alla latitudine di Parigi, come si è mostrato sopra nelle Propp. IV e XIX.

**[III.G6.40]** *Cor. 8.* La distanza media dei centri della Terra e della Luna nelle sizigie della Luna è di sessanta semidiametri massimi della Terra, tolta circa la trentesima parte di un semidiametro. E nelle quadrature della Luna la distanza media degli stessi centri è di 60⅚ semidiametri della Terra. Infatti queste due distanze stanno alla distanza media della Luna negli ottanti come 69 e 70 stanno a 69½, per la Prop. XXVIII.

**[III.G6.41]** *Cor. 9.* La distanza media dei centri della Terra e della Luna nelle sizigie della Luna è di sessanta semidiametri medi della Terra e un decimo di semidiametro. E nelle quadrature della Luna la distanza media degli stessi centri è di sessantuno semidiametri medi della Terra, tolta la trentesima parte di un semidiametro.

**[III.G6.42]** *Cor. 10.* Nelle sizigie della Luna la sua parallasse orizzontale media alle latitudini di 0, 30, 38, 45, 52, 60, 90 gradi è rispettivamente di 57′ 20″, 57′ 16″, 57′ 14″, 57′ 12″, 57′ 10″, 57′ 8″, 57′ 4″.

**[III.G6.43]** In questi calcoli non ho considerato l'attrazione magnetica della Terra, la cui quantità è comunque piccolissima ed è ignota. Se però un giorno si potrà indagare questa attrazione, e le misure dei gradi sul meridiano, le lunghezze dei pendoli isocroni nei diversi paralleli, le leggi dei moti del mare e la parallasse della Luna, con i diametri apparenti del Sole e della Luna, saranno determinate più accuratamente dai fenomeni, si potrà ripetere tutto questo calcolo con maggiore accuratezza.

**Fine della parte «a». Nel testo originale segue la Prop. XXXVIII, *Invenire figuram corporis lunæ* (Fascicolo 25b).**

---
## Apparato

### A.0 Estensioni del glossario

I termini seguenti non comparivano nei glossari comuni. Ognuno è reso in modo costante in tutto il fascicolo.

| Latino | Italiano | Motivazione |
|---|---|---|
| *variatio horaria / momentanea / menstrua / tota / mediocris* | «variazione oraria / momentanea / mensile / totale / media» | Prop. XXXIV–XXXV. *Mediocris* «medio, media», come *mediocris distantia* «distanza media» del glossario. |
| *motus momentaneus*; *momentum temporis* | «moto momentaneo»; «momento di tempo» | *Momentum* qui è l'intervallo infinitesimo di tempo, non il «momento» del Lemma II del Libro II. |
| *vestigium loci* (*in plano eclipticæ*) | «traccia del luogo» | Prop. XXXIV: il piede della perpendicolare Pp abbassata sul piano dell'eclittica, cioè la proiezione ortogonale. Motte esplicita «orthographic projection». La stessa resa è nel Fascicolo 24b (Prop. XXX, *Npn vestigium orbis* «la traccia dell'orbita»). |
| *contentum* (*sub …*) | «prodotto» | *Contentum GH×Gg*, *contentum sub inclinationis sinu AH & sinu anguli recti*: il rettangolo dei due fattori; nelle proporzioni conta solo come prodotto. |
| *BHD*, *HBD* (rettangoli) | «BH × HD», «HB × BD» | Prop. XXXV: la trascrizione scrive il rettangolo come sigla di tre lettere; reso con il prodotto esplicito (§ A.2). |
| *aggregatum* | «somma» | Prop. XXXIV, Cor. 2. |
| *mensis periodicus* | «mese periodico» | Il mese siderale (ritorno della Luna alla stessa stella); conservato il termine del testo. |
| *inæqualitas* | «disuguaglianza» | Termine tecnico dell'astronomia lunare: ogni scarto periodico dal moto medio; come nel Fascicolo 10 (Prop. LXVI, Cor. 8). |
| *æquatio semestris*; *semestris secunda*; *æquatio centri secunda*; *æquatio principalis apogæi* | «equazione semestrale»; «seconda semestrale»; «seconda equazione del centro»; «equazione principale dell'apogeo» | Scolio: nomi dati da Newton (*quam semestrem vocabo*). Si conserva la sua terminologia; i nomi moderni sono in nota (N7). |
| *argumentum annuum* | «argomento annuo» | Scolio: la distanza del luogo vero del Sole dall'apogeo della Luna (definita nel testo). «Argomento» è il termine tecnico delle tavole astronomiche: l'angolo da cui dipende un'equazione. |
| *semel æquatus*; *secundo æquatus* | «equato una volta»; «equato due volte» | L'apogeo corretto con la prima equazione, poi con la seconda. Calco tecnico, come *æquatio* «equazione». |
| *epicyclus* | «epiciclo» | |
| *umbilicus inferior / superior* | «fuoco inferiore / superiore» | Applicazione del glossario (*umbilicus* «fuoco»): il fuoco occupato dalla Terra e l'altro fuoco. |
| *diameter transversa* | «diametro trasverso» | L'asse maggiore dell'orbita (glossario: *axis transversus* «asse trasverso»). |
| *anomalia vera / media* | «anomalia vera / media» | Glossario (*anomalia*). |
| *luminaria* | «i luminari» | Il Sole e la Luna insieme. Motte «luminaries». |
| *translatio* (del centro dell'orbita) | «traslazione» | Come nel Fascicolo 20, ma qui è lo spostamento di un punto (da D a F). |
| *dilatatio*; *dilatare / contrahi* | «dilatazione»; «dilatare / contrarsi» | Scolio. |
| *refringere*; *spargere*; *umbra* | «rifrangere»; «diffondere»; «ombra» | Scolio, ombra della Terra nelle eclissi. |
| *observatorium regium Grenovicense / Parisiense*; *tempus meridianum* | «osservatorio reale di Greenwich / di Parigi»; «mezzogiorno» | Scolio. |
| *vis ad mare movendum / ciendum / agitandum / attollendum* | «forza per muovere / suscitare / agitare / sollevare il mare» | Propp. XXXVI–XXXVII: i quattro verbi sono distinti nel latino e restano distinti. |
| *ascensus aquæ*; *altitudo æstus* | «salita dell'acqua»; «altezza della marea» | |
| *appulsus lunæ ad meridianum* | «passaggio della Luna al meridiano» | Prop. XXXVII. Motte «appulse», calco poco trasparente in italiano. |
| *novilunium / plenilunium* | «novilunio / plenilunio» | |
| *lapis tertius* (*infra Bristolium*) | «la terza pietra miliare» | Prop. XXXVII: la pietra che segna il terzo miglio. Motte «three miles below Bristol». |
| *portus*; *fretum*; *sinus* (di mare); *littus*; *loca vadosa* | «porto»; «stretto»; «insenatura»; «costa»; «luoghi poco profondi» | Prop. XXXVII, Cor. 1. |
| *cursus & recursus*; *influere & effluere*; *influendi & remeandi* | «andata e ritorno»; «entrare e uscire»; «afflusso e ritorno» | Prop. XXXVII, Cor. 1: distinti da *fluxus / refluxus* «flusso / riflusso» (glossario). |
| *sinus complementi* | «seno del complemento» | È il coseno; il testo non usa la parola «coseno», e l'italiano non la introduce (nota N10). Motte «co-sine». |
| *digitus* (misura di lunghezza) | «pollice» | Glossario del Libro II (*digitus* «pollice»). Il glossario del Libro III fissa «dito» per il *digitus* delle eclissi; qui il contesto è piedi–pollici–linee, quindi «pollice». **Dubbio segnalato** per l'armonizzazione. |
| *gravitas acceleratrix* | «gravità acceleratrice» | Prop. XXXVII, Cor. 5: sul modello di *vis acceleratrix*. |
| *massa* | «massa» | Prop. XXXVII, Cor. 4. Motte «mass of matter». |
| *magis terrestris* | «più terroso» | Prop. XXXVII, Cor. 3: «fatto più di terra», cioè di materia solida. |
| *pendula isochrona*; *paralleli* | «pendoli isocroni»; «paralleli» | Capoverso finale. |
| *tertia, quarta* (‴, iv) | «terzi, quarti» | Sessantesimi del secondo e del terzo; si conservano i segni del testo (nota N2). |
| *non vacat* | «non c'è il tempo» | Prop. XXXV: *omnes inæqualitatum minutias expendere non vacat*. |

*Impetus* compare quattro volte nel Cor. 1 della Prop. XXXVII: «impeto», secondo il glossario. *Æstus maris* è «marea»; *fluxus & refluxus* «flusso e riflusso». *Vis solis ad perturbandos motus lunares* (Prop. XXXVI) è resa con la formula del glossario: «con cui il Sole perturba i moti lunari».

### A.1 Proposizione XXXIV

**Latino:** *Invenire variationem horariam inclinationis orbis lunaris ad planum eclipticæ.*

**Inglese:** “To find the horary variation of the inclination of the moon's orbit to the plane of the ecliptic.”

**Scelte.**

- *ut supra* (mTl moto momentaneo dei nodi) rimanda alla Prop. XXX, dove mTl è definito (§ A.7).
- *ut TG ad PG & Pp ad PG conjunctim* → «come TG sta a PG e Pp sta a PG, considerati congiuntamente».
- *si pro momento temporis substituatur hora* → «se al momento di tempo si sostituisce un'ora».
- L'angolo di riferimento è **33″ 10‴ 33iv**: nella Prop. XXX il valore è 33″ 10‴ 33iv 12v (moto orario massimo del nodo); qui Newton tralascia i quinti.
- *IT×AZ×TG×PpPG ad ATcub.*: letto IT × AZ × TG × Pp/PG : AT³ (SVG 1056 di Motte concorda).
- *Q.E.I.* → «C.V.T.».
- *Hæc ita se habent ex hypothesi …*: il rimando *uti supra expositum est* è al Cor. della Prop. XXXI (moto medio dei nodi nell'ellisse : nel cerchio = 69 : 70, cioè asse minore : asse maggiore).

**Corollari (III.G6.04–III.G6.07).**

- Cor. 1: *ductæ in rationem TZMp* → «moltiplicata per il rapporto TZ/Mp».
- Cor. 2: *retraherentur … reducerentur* → «fossero ritratti … ricondotti»: lo stesso artificio della Prop. XXXII (nodo ricondotto ogni ora al luogo di prima).
- Cor. 3: *ad radium quadruplicatum* → «al quadruplo del raggio»; *ad quadruplum quadratum radii* → «al quadruplo del quadrato del raggio».
- Cor. 4: *177⁤16* letto 177⅙ (SVG 1066); *7×87410000* letto 7 × 874/10000 (SVG 1067). La trascrizione ha *lunæ à quadraturis* con l'accento grafico, conservato in `la`.

### A.2 Proposizione XXXV

**Latino:** *Dato tempore invenire inclinationem orbis lunaris ad planum eclipticæ.*

**Inglese:** “To a given time to find the inclination of the moon's orbit to the plane of the ecliptic.”

**Scelte.**

- *In AC capiatur CE in ea ratione ad EB quam EB habet ad 2⁢BA* → «In AC si prenda CE in rapporto a EB come EB sta a 2BA» (CE · 2BA = EB²).
- Catena *GEq … =2⁢EC×AH*: *BHD* e *HBD* sono rettangoli BH · HD e HB · BD; resi con il prodotto esplicito. Ogni passaggio è stato verificato (nota N4).
- *Designet jam AEg …*: Motte «in a given moment of time after»; il latino *post datum aliquod momentum temporis completum*.
- *per Corol. 3. Propositionis superioris* → «per il Cor. 3 della proposizione precedente»; più avanti *per Corol. 3. Prop. novissimæ* → «per il Cor. 3 dell'ultima proposizione». Sono la stessa Prop. XXXIV; la differenza lessicale è conservata.
- *Nam omnes inæqualitatum minutias expendere non vacat* → «non c'è infatti il tempo di soppesare tutte le minuzie delle disuguaglianze» (Motte «I cannot descend to every minute circumstance of inequality»).
- *5gr. 8′⁤12* letto 5° 8½′; *2079⁤710* letto 2079 7/10; *16′, 23″⁤12* letto 16′ 23½″ (la virgola dopo 16′ è anomala; § A.6).
- *ut 224×7×2079⁤710 ad 110000*: il denominatore 110000 = 11 × 10000 (dal rapporto 7 : 11 e dal 224 : 10000).
- *in ipsius autem syzygiis* → «nelle sizigie della Luna» (*ipsius* è la Luna, come in *quadraturis lunaribus*).
- Capoverso finale: *si … nodi ubivis versantur* → «i nodi in un luogo qualsiasi»; *(ut supra diximus)* rimanda alla Prop. XXXIII, dove l'equazione mensile dei nodi e la disuguaglianza mensile dell'inclinazione «si temperano e si correggono a vicenda» (§ A.7).

### A.3 Scolio della Prop. XXXV

- Primo capoverso: *a causis suis computari possint* → «si possono calcolare a partire dalle loro cause»; Motte aggiunge «physical».
- *in perigæo solis … in apogæo ejus* → «nel perigeo del Sole … nel suo apogeo»: Newton usa perigeo e apogeo del Sole (visto dalla Terra) e, poco dopo, afelio e perielio della Terra; sono la stessa situazione vista dai due corpi, e la traduzione conserva i due lessici.
- *in aliis locis æquationi centri solis proportionalis est* → «negli altri luoghi è proporzionale all'equazione del centro del Sole»; Motte «in other distances of the sun».
- *16⁤78* = 16 7/8 (SVG 1074), *16⁤1112* = 16 11/12 (SVG 1075), in millesimi del raggio dell'orbe magno.
- *Addditur* (tre d) è un refuso della trascrizione per *Additur* (§ A.6).
- *in octante cum sole* → «in ottante con il Sole»: l'apogeo a 45° dal Sole.
- *si sol distat a nodo sibi proximo in antecedencia* → «se il Sole dista dal nodo a lui più vicino in antecedenza»; *antecedencia* per *antecedentia* (§ A.6).
- *Horroxius noster* → «il nostro Horrocks» (Jeremiah Horrocks, non verificato sulle fonti allegate per il nome proprio); *Halleius* → «Halley» (Edmond Halley, idem). Motte «Our countryman, Horrox», «Dr. Halley improved the notion»: l'«improved the notion» non è nel latino.
- *in ejus umbilico inferiore constitutam*: *constitutam* concorda con *terram*: è la Terra a essere posta nel fuoco inferiore. Resa: «attorno alla Terra, posta nel fuoco inferiore dell'ellisse».
- *CB sinus æquationis maximæ semestris 12gr. 18′ ad radium TC* → «CB sia il seno dell'equazione semestrale massima di 12° 18′ rispetto al raggio TC».
- *propio* per *proprio* (refuso probabile, § A.6).
- *in circumferentia circuli DABD*: l'epiciclo è stato chiamato BDA; la sigla DABD (ripetuta in Motte) descrive il giro completo a partire da D. Non è un errore.
- Seconda equazione del centro: *ad distantiam lunæ a terra subtendit angulum quem eadem translatio generat in motu lunæ* → «alla distanza della Luna dalla Terra sottende l'angolo che la stessa traslazione genera nel moto della Luna» (vertice dell'angolo nella Terra, come nelle due frasi precedenti). Motte scrive «subtends an angle **at the moon**»: errore di senso (§ A.9).
- *lunaæ*, *apogeæi* sono refusi della trascrizione (§ A.6).
- *Sic habebitur ejus longitudo in ipsis luminarium syzygiis* → «Così se ne avrà la longitudine nelle sizigie stesse dei luminari». Motte amplia («And from the moon's place in its orbit thus corrected …»).
- Ombra: *minutum unum primum … vel minutum unum cum triente* → «un minuto primo, oppure un minuto e un terzo» (Motte «1 or 1⅓ minute», SVG 1015).
- Epoca: *ad tempus meridianum … die ultimo mensis Decembris anni 1700. st. vet.* → «per il mezzogiorno … nell'ultimo giorno del mese di dicembre dell'anno 1700 secondo il calendario giuliano (stile vecchio)»; *0hor. 9min. 20sec.* → «0 ore 9 minuti 20 secondi» (è una differenza di tempo, quindi «minuti»).

### A.4 Proposizione XXXVI

**Latino:** *Invenire vim solis ad mare movendum.*

**Inglese:** “To find the force of the sun to move the sea.”

**Scelte.**

- *erat (per Prop. xxv. hujus)* → «stava (per la Prop. XXV di questo Libro)»: l'imperfetto rimanda a un risultato già ottenuto.
- *60⁤12* = 60½ (SVG 968).
- *ac si tota … mare elevaret* → «che se innalzasse tutta quanta il mare»: *tota* è la forza.
- *ubi sol tam in vertice loci versatur quam in mediocri sua distantia* → «quando il Sole si trova insieme allo zenit del luogo e alla sua distanza media»; Motte «both vertical, and in its mean distance».
- *ut sinus versus duplæ altitudinis solis … directe & cubus distantiæ … inverse* → «come il seno verso del doppio dell'altezza del Sole …, direttamente, e come il cubo della distanza …, inversamente» (nota N9).
- Cor.: la trascrizione ha *Corol. cum vis* con la minuscola (§ A.6). *pedis unius Parisiensis & digitorum undecim cum tricesima parte digiti* → «un piede parigino e undici pollici e un trentesimo di pollice». Motte rende con SVG 1079, che si legge **113 1/30** (§ A.8).

### A.5 Proposizione XXXVII

**Latino:** *Invenire vim lunæ ad mare movendum.*

**Inglese:** “To find the force of the moon to move the sea.”

**Scelte.**

- *Ante ostium fluvii Avonæ ad lapidem tertium infra Bristolium* → «Davanti alla foce del fiume Avon, alla terza pietra miliare sotto Bristol». *Samuel Sturmius* → Samuel Sturmy; *Samuel Colepressus* → Samuel Colepress (forme di Motte).
- *sunto vires S & L* → «siano S e L le forze».
- Plymouth: *superare potest altitudinem ejus in quadraturis pedibus septem vel octo* → «può superare … di sette o otto piedi». Motte «by **more than** 7 or 8 feet»: aggiunta.
- *20⁤12 ad 11⁤12* = 20½ : 11½ (SVG 1080, 1081): media 16 ± metà della differenza di 9.
- *in portu Bistoliæ*: *Bistoliæ* per *Bristoliæ* (§ A.6).
- *sunt tertii a syzygiis ut dictum fuit* → «sono le terze dopo le sizigie, come si è detto»: rimando alla Prop. XXIV (§ A.7).
- *seu proxime sequuntur tertium lunæ post syzygias appulsum ad meridianum loci* → «ossia seguono da vicino il terzo passaggio della Luna al meridiano del luogo dopo le sizigie». Motte aggiunge «(reckoning from the syzygies)».
- *ab æstu ad æstum* → «da una marea all'altra»; Motte «from one greatest tide to the next following greatest tide».
- *18⁤12* = 18½ (SVG 641).
- *in ratione radii ad sinum complementi distantiæ hujus duplicatæ* → «nel rapporto del raggio al seno del complemento del doppio di questa distanza».
- *in declinatione graduum plus minus 22. 13′* → «a una declinazione di circa 22° 13′». **Motte ha 23° 13′**; il calcolo (0,8570327 = cos² 22° 13′) conferma il latino (nota N10, § A.9).
- *Unde fit 1,017522⁢L+0,7986355⁢S ad …*: **Motte ha «1,017522L × 0,7986355S»**, refuso (il segno deve essere +, come nella proporzione precedente).
- *69⁤12* = 69½ (SVG 1082).
- Cor. 1: *7⁤522* = 7 5/22 pollici (SVG 1084); *pedum decem cum semisse* «dieci piedi e mezzo» (Motte SVG 636: 10½); *ad montes S. Michælis & urbem Abrincatuorum (vulgo Auranches)* → «presso i monti di San Michele e la città degli Abrincati (volgarmente Avranches)»: il plurale *montes* è del testo; *Cambaiam & Pegu* → «Cambay e Pegu» (forma moderna di Cambaia, non verificato sulle fonti allegate). *millaria* per *milliaria* (§ A.6). *ejus quo Anglia circundatur* → «quello da cui l'Inghilterra è circondata» (singolare; Motte «those channels»).
- Cor. 2: *vel in experimentis pendulorum, vel in staticis aut hydrostaticis quibuscunque* → «negli esperimenti con i pendoli, o in qualsiasi esperimento statico o idrostatico». Motte inverte l'ordine.
- Cor. 3: *4891 ad 1000* (densità della Luna : Sole); *ut 1000 ad 4000* rimanda alla Prop. VIII, Cor. 3 (§ A.7). *31′. 16″⁤12* = 31′ 16½″ (SVG 1086).
- Cor. 7: *60⁤25* = 60⅖ (SVG 966; 692); *terræ semidiameter maxima suit*: *suit* per *fuit* (§ A.6); *43⁤49* = 43 4/9 minuti (SVG 1087); *178⁤2940 ad 177⁤2940* = 178 29/40 : 177 29/40 (SVG 963, 964). *1000,000000,000000* è il raggio delle tavole (10¹⁵), con le virgole come separatori di gruppi. *ad distantiam pedum 197896573*: il numero va letto 19789657,3 (la sessantesima parte di 1187379440); manca la virgola decimale, anche in Motte (nota N12, § A.6). *lin. 4⁤111* = 4 1/11 linee (coerente con 15,11175 piedi); **Motte (SVG 1088) ha 4 4/11**. *23 partium lineæ* = 2/3 di linea (SVG 226). *lin. 4⁤2533* = 4 25/33 (SVG 1089). *cetrifugam* per *centrifugam* (§ A.6). *lin. 1⁤12* = 1½ (SVG 208).
- Cor. 8: *60⁤56* = 60⅚ (SVG 1090).

### A.6 Refusi e anomalie della trascrizione

| Luogo | Trascrizione | Lettura | Tipo |
|---|---|---|---|
| III.G6.02 | *com <455> pletum* | *completum* | parola spezzata dal marcatore di pagina, nessuna perdita |
| III.G6.11 | *16′, 23″⁤12* | *16′. 23″½* | virgola al posto del punto |
| III.G6.11 | *dif <459> ferentiæ* | *differentiæ* | parola spezzata dal marcatore |
| III.G6.13 | *syzgiis* | *syzygiis* | refuso probabile |
| III.G6.15 | *Addditur* | *Additur* | refuso probabile |
| III.G6.17 | *in antecedencia* | *in antecedentia* | refuso probabile (o grafia della stampa) |
| III.G6.19 | *ab apogæo propio* | *proprio* | refuso probabile |
| III.G6.20 | *lunaæ*, *apogeæi* | *lunæ*, *apogæi* | doppia vocale, refusi della trascrizione |
| III.G6.26 | *Corol. cum vis* | *Corol. Cum vis* | minuscola |
| III.G6.29 | *in portu Bistoliæ* | *Bristoliæ* | refuso probabile |
| III.G6.33 | *ad multa millaria* | *milliaria* | refuso probabile |
| III.G6.33 | *circundatur* | *circumdatur* | grafia dell'epoca, non refuso |
| III.G6.39 | *semidiameter maxima suit* | *fuit* | s lunga / f |
| III.G6.39 | *pedum 197896573* | *19789657,3* | virgola decimale mancante (anche in Motte) |
| III.G6.39 | *vim cetrifugam* | *centrifugam* | refuso probabile |
| passim | frazioni appiattite (*16⁤78*, *PpPG*, *AZ×TZ12⁢AT*) | 16 7/8, Pp/PG, (AZ × TZ)/(½AT) | artefatto della pagina web, letto con l'aiuto di Motte |

La Parte B riporta il latino esatto della trascrizione, refusi compresi.

**Punti da controllare sulla stampa ECCO.**

| Pagina 1726 | Trascrizione | Lettura attesa | Motivo |
|---|---|---|---|
| p. 459 | *16′, 23″⁤12* | *16′. 23″½* | virgola anomala |
| p. 459 | *syzgiis* | *syzygiis* | lettera mancante |
| p. 460 | *Addditur* | *Additur* | lettera doppia |
| p. 460 | *9′. 24″* (equazione dei nodi) | da confermare | il ricalcolo dà circa 9′ 21″ (nota N6) |
| p. 461 | *in antecedencia* | *antecedentia* | grafia |
| p. 463 | *propio* | *proprio* | lettera mancante |
| p. 463 | *33⁤78 ad 1000* | da confermare | il doppio di 16 11/12 è 33 5/6 (nota N7) |
| p. 463 | *lunaæ*, *apogeæi* | *lunæ*, *apogæi* | grafie impossibili |
| p. 465 | *Corol. cum* | *Corol. Cum* | minuscola |
| p. 466 | *Bistoliæ* | *Bristoliæ* | lettera mancante |
| p. 466 | *22. 13′* | *22. 13′* (Motte 23° 13′) | confermare che la stampa ha 22 |
| p. 468 | *millaria* | *milliaria* | lettera mancante |
| p. 469 | *suit* | *fuit* | s lunga |
| p. 469 | *197896573* | *19789657,3* | virgola decimale |
| p. 469 | *15,11175* | da confermare | il ricalcolo dà 15,1183 (nota N12) |
| p. 469 | *lin. 4⁤111* | 4 1/11 | Motte 4 4/11 |
| p. 470 | *cetrifugam* | *centrifugam* | lettera mancante |

### A.7 Rimandi

**Rimandi al Libro I** (verificati sul Fascicolo 10, Sezione XI).

| Luogo | Latino | Enunciato citato | Esito |
|---|---|---|---|
| III.G6.14 | *juxta Corol. 6. Prop. lxvi. Lib. I.* | Cor. 6 (S11.45): la forza del corpo centrale diminuita dalla forza KL; il raggio e il tempo periodico aumentano e diminuiscono insieme all'azione alterna del corpo lontano | regge: l'orbita lunare si dilata quando la forza del Sole è maggiore (perigeo del Sole) |
| III.G6.18 | *per Corol. 7, 8 & 9. Prop. lxvi. Lib. I.* | Cor. 7 (S11.46): le apsidi avanzano nelle sizigie e retrocedono nelle quadrature; Cor. 8 (S11.47): avanzamento più veloce con le apsidi nelle sizigie; Cor. 9 (S11.48): eccentricità massima con le apsidi nelle sizigie, minima nelle quadrature | regge |
| III.G6.35 | *per corol. 14. prop. lxvi. lib. i.* | Cor. 14 (S11.53): gli effetti sono come la forza assoluta del corpo lontano e il cubo inverso della distanza; e, se la grandezza del corpo è proporzionale alla forza assoluta, come il cubo del diametro apparente | regge **con un'estensione**: il Cor. 14 dà il cubo del diametro apparente solo per corpi di uguale densità; Newton qui aggiunge il fattore della densità (forza assoluta ∝ densità × volume), che segue dallo stesso ragionamento ma non è scritto nel corollario |

Nessun rimando al Libro I che non torni. Il Libro II non è citato.

**Rimandi interni al Libro III** (verificati sul latino degli altri gruppi).

| Luogo | Latino | Esito |
|---|---|---|
| III.G6.02 | *mTl motum momentaneum nodorum ut supra* | Prop. XXX (mTl moto angolare dei nodi): regge |
| III.G6.02 | *per prop. xxx.* | Prop. XXX: moto orario del nodo «ad 33″. 10‴. 33iv. 12v. ut contentum sub sinubus angulorum trium TPI, PTN, & STN … ad cubum radii», cioè IT × PH × AZ : AT³; qui PG ha il ruolo di PH; regge |
| III.G6.03 | *uti supra expositum est* | Prop. XXXI, Cor.: moto medio nell'ellisse : nel cerchio = Ta : TA = 69 : 70; regge |
| III.G6.07, III.G6.10–III.G6.12 | *per hanc propositionem*; *per Corol. 3. Propositionis superioris*; *Prop. novissimæ*; *propositionis superioris Corollario quarto* | Prop. XXXIV, Cor. 3 e 4: reggono |
| III.G6.13 | *(ut supra diximus)* | Prop. XXXIII: «hujus menstrua inæqualitas & æquatio menstrua nodorum ita se mutuo contemperant & corrigunt»; regge |
| III.G6.24 | *per Prop. xxv. hujus* | Prop. XXV: «vis mediocris ML … ad vim gravitatis in superficie terræ … seu 1 ad 638092,6»; regge. La Prop. XXV confronta la forza ML **alla distanza della Luna** con la gravità alla superficie della Terra («presso di noi»); qui la forza perturbatrice, che è proporzionale alla distanza dal centro della Terra, viene riportata alla superficie dividendo per 60½ (nota N9) |
| III.G6.26 | *ut supra in prop. xix* | Prop. XIX: 1 : 289 ed eccesso di 85472 piedi; regge |
| III.G6.30 | *ut dictum fuit* | Prop. XXIV: «æstus omnium maximi in iisdem portubus, non sint primi a syzygiis, sed tertii»; regge |
| III.G6.35 | *Densitas autem solis erat ad densitatem terræ ut 1000 ad 4000* | Prop. VIII, Cor. 3: densità di Sole e Terra 100 e 400; regge |
| III.G6.39 | *terræ semidiameter maxima fuit pedum … 19658600* | Prop. XIX: «altitudo ejus ad æquatorem erit 19658600 pedum circiter»; regge |
| III.G6.39 | *per corollarium superius* | Cor. 6 di questa proposizione; regge |
| III.G6.39 | *per Corol. Prop. III.* | Prop. III, Cor.: la forza va aumentata «in ratione 177 29/40 ad 178 29/40»; qui Newton scrive «in ratione 178 29/40 ad 177 29/40». L'ordine dei termini è invertito, ma l'operazione è la stessa (moltiplicare per 178 29/40 / 177 29/40, come mostra il calcolo 14,7706353 → 14,8538067); regge, con la formulazione invertita |
| III.G6.39 | *per tabulam præcedentem in prop. xx.* | Prop. XX: incremento del peso come il quadrato del seno della latitudine; l'eccesso di 2/3 di linea fra 45° e Parigi torna (nota N12) |
| III.G6.39 | *supra ostensum est ad prop. iv, & xix.* | Prop. IV e Prop. XIX: caduta a Parigi di 15 piedi, 1 pollice, 1 7/9 linee (2173 7/9 linee); qui Newton ottiene 1½ linee. Lo scarto di 5/18 di linea è dentro l'accordo che Newton dichiara; **segnalato** |
| III.G6.40 | *per prop. xxviii.* | Prop. XXVIII: distanze nelle sizigie e nelle quadrature come 69 : 70; regge |

### A.8 Formule SVG di Motte

Ho confrontato con il latino **46 formule SVG** del perimetro (1056–1090, 1010, 1015, 968, 641, 636, 966, 692, 963, 964, 226, 208). Quelle che non tornano:

| SVG | LaTeX | Lettura attesa (latino) | Commento |
|---|---|---|---|
| 1079 | `113\tfrac{1}{30}` | 11 1/30 (pollici) | Prop. XXXVI, Cor.: «one Paris foot and 113 1/30 inches»; nel Cor. 1 della Prop. XXXVII la stessa misura è giusta (SVG 1083, 11 1/30) |
| 1088 | `4\tfrac{4}{11}` | 4 1/11 (linee) | Prop. XXXVII, Cor. 7; il latino ha *4⁤111*, coerente con 15,11175 piedi = 15 piedi 1 pollice 4,09 linee; anche il passo successivo (4 1/11 + 2/3 = 4 25/33, SVG 1089) conferma il latino |
| 1010 | `8\tfrac{1}{2}` | 8½′ | lieve: nel testo di Motte «5° 8½» manca il segno ′ del primo |

### A.9 Riepilogo: dove Motte aggiunge, omette o sbaglia

| Luogo | Latino | Motte 1846 | Tipo |
|---|---|---|---|
| III.G6.02 | *vestigium loci* | «orthographic projection of that place» | esplicitazione |
| III.G6.11 | *5gr. 8′⁤12* | «5° [SVG 1010]» | segno ′ mancante |
| III.G6.13 | *nodi ubivis versantur* | «the nodes any where between them and the quadratures» | aggiunta |
| III.G6.13 | *in calculo latitudinis lunæ compensatur* | «to which the variation … is obnoxious in the calculus of the moon's latitude, is balanced» | complemento spostato |
| III.G6.14 | *a causis suis* | «from their physical causes» | aggiunta |
| III.G6.14 | *in aliis locis* | «in other distances of the sun» | esplicitazione |
| III.G6.18 | *quantum ex observationibus* | «from the phænomena» | termine cambiato |
| III.G6.18 | *Halleius … locavit* | «Dr. Halley improved the notion, by putting» | aggiunta |
| III.G6.19 | *versus apogæum lunæ* | «towards the moon's apogee once equated» | aggiunta |
| III.G6.20 | *ad distantiam lunæ a terra subtendit angulum* | «subtends an angle at the moon» | **errore di senso** (vertice nella Terra) |
| III.G6.20 | *Sic habebitur ejus longitudo* | «And from the moon's place in its orbit thus corrected, its longitude may be found» | ampliamento |
| III.G6.26 | *digitorum undecim cum tricesima parte* | SVG 1079: 113 1/30 | **numero errato** |
| III.G6.28 | *ad lapidem tertium* | «three miles below» | parafrasi |
| III.G6.29 | *pedibus septem vel octo* | «by more than 7 or 8 feet» | **aggiunta** |
| III.G6.30 | *seu proxime sequuntur* | «or (reckoning from the syzygies) follow» | aggiunta |
| III.G6.30 | *ab æstu ad æstum* | «from one greatest tide to the next following greatest tide» | aggiunta |
| III.G6.31 | *22. 13′* | «23° 13'» | **numero errato** |
| III.G6.32 | *1,017522⁢L+0,7986355⁢S* | «1,017522L × 0,7986355S» | **segno errato** |
| III.G6.33 | *ejus quo Anglia circundatur* | «those channels which environ England» | numero |
| III.G6.34 | *vel in experimentis pendulorum, vel in staticis …* | «in statical or hydrostatical experiments, or even in those of pendulums» | ordine invertito |
| III.G6.36 | *massa* | «mass of matter» | esplicitazione |
| III.G6.39 | *lin. 4⁤111* | SVG 1088: 4 4/11 | **numero errato** |
| III.G6.39 | *ad distantiam pedum 19615800* | «at the distance of 19615800» | unità omessa |

Le lettere delle figure (A, a, Q, q, N, n, P, p, T, m, l, G, g, I, Z, F, K, k, H, h, M; B, C, D, E, H; T, C, B, D, A, E, F; M, L, P, K) coincidono con il latino in tutto il perimetro.

---
## Note editoriali e fisiche

Queste note sono aggiunte del presente fascicolo, non affermazioni tradotte da Newton. Tutti i conti sono stati rifatti con uno script Python (`tmp/25a/verifica.py`), che parte dai dati del testo e non dai risultati da verificare. Ciò che proviene da conoscenza generale e non dalle fonti allegate è marcato «(non verificato sulle fonti allegate)». Le cifre che non tornano sono **segnalate e non corrette** nel testo.

### N1. Note di glossario alla prima occorrenza

- **Equazione** (*æquatio*, III.G6.14): nell'astronomia classica è la **correzione** da aggiungere o togliere al moto medio (o al luogo medio) per avere il moto vero (o il luogo vero). L'«equazione del centro» del Sole è la differenza fra il luogo vero e il luogo medio dovuta all'eccentricità dell'orbita; l'«equazione annua» della Luna è la correzione del moto medio lunare che ha il periodo di un anno. Non è un'equazione nel senso algebrico.
- **Orbe magno** (*orbis magnus*, III.G6.14): l'orbita annua della Terra attorno al Sole. Il «raggio dell'orbe magno» è la distanza media Terra–Sole, presa uguale a 1000.
- **Segni zodiacali** (III.G6.22): ♈ Ariete, ♉ Toro, ♊ Gemelli, ♋ Cancro, ♌ Leone, ♍ Vergine, ♎ Bilancia, ♏ Scorpione, ♐ Sagittario, ♑ Capricorno, ♒ Acquario, ♓ Pesci. Ogni segno è un tratto di 30° di longitudine eclittica a partire dall'equinozio di primavera; la longitudine si conta in gradi dentro il segno: ♑ 20° 43′ 40″ = 270° + 20° 43′ 40″ = 290° 43′ 40″.
- **Stile vecchio** (*st. vet.*, III.G6.22): la data è secondo il calendario giuliano, allora ancora in uso in Inghilterra. Il 31 dicembre 1700 giuliano corrisponde all'11 gennaio 1701 gregoriano (non verificato sulle fonti allegate).
- **In conseguenza / in antecedenza** (III.G6.17, III.G6.19, III.G6.30): nel verso dei moti dei pianeti lungo lo zodiaco (da ovest a est) / nel verso contrario.

### N2. L'unità di riferimento 33″ 10‴ 33ⁱᵛ

Il testo usa la divisione sessagesimale fino ai quarti: 33″ 10‴ 33ⁱᵛ = 33 + 10/60 + 33/3600 secondi = **33,1758″**. È il moto orario del nodo nel caso massimo (Prop. XXX: 33″ 10‴ 33ⁱᵛ 12ᵛ), preso come unità di misura delle variazioni orarie dell'inclinazione. Nel Cor. 4 Newton moltiplica per 177⅙ ore: 33,1758″ × 177,1667 = 5877,65″, cioè **5878″**, come nel testo.

### N3. Prop. XXXIV: la formula e i corollari

**In termini moderni.** Sia *i* l'inclinazione, *u* la distanza della Luna dal nodo, *s* la distanza del nodo dal Sole. Con IT/AT = cos(*u* − *s*) (seno della distanza della Luna dalla quadratura), AZ/AT = sin *s*, TG/AT = cos *u* e Pp/PG = sin *i*, la proposizione dà

d*i*/d*t* = 33,1758″/ora × sin *i* · sin *s* · cos *u* · cos(*u* − *s*).

**Cor. 3.** La media su un giro della Luna (*u* da 0 a 360°) di cos *u* · cos(*u* − *s*) · sin *s* è ½ sin *s* cos *s* = ¼ sin 2*s*. Il controllo numerico (200 000 punti) dà 0,216506 per *s* = 30° contro sin 60°/4 = 0,216506, e 0,250000 per *s* = 45°: la variazione oraria media è come «il seno dell'inclinazione moltiplicato per il seno del doppio della distanza dei nodi dal Sole, al quadruplo del quadrato del raggio». Torna.

**Cor. 4.** Con i nodi nelle quadrature (*s* = 90°) il fattore diventa ½ sin 2*u*; la sua media fra quadratura e sizigia è 1/π = 0,318310 (numerico 0,318310). Newton prende 1/π ≈ 7/22 = 0,318182. Con sin 5° 1′ = 0,087446 si ha 7 × 0,0874/22 = 0,0278091 ≈ 278/10000, e 5878″ × 0,0278 = 163,4″ = **2′ 43″**. Torna. Il tempo di 177⅙ ore è un quarto del mese sinodico (29 g 12 h 44 m / 4 = 177,18 ore, dato della Prop. XXVIII).

**Valori moderni.** L'inclinazione dell'orbita lunare oscilla fra circa 4° 59′ e 5° 18′, con un periodo di mezzo anno di nodi (circa 173 giorni) (non verificato sulle fonti allegate): i valori di Newton, 4° 59′ 35″ e 5° 17′ 20″ (III.G6.12), sono molto vicini.

### N4. Prop. XXXV: la costruzione

**Ricostruzione dalle lettere.** Su una retta stanno A, B, E, C, D in quest'ordine: AB e AD sono i seni dell'inclinazione minima e massima; C è il punto medio di BD; il cerchio BGD ha centro C; E sta fra B e C con CE · 2BA = EB². G è sul cerchio, con l'angolo AEG uguale al doppio della distanza dei nodi dalle quadrature; H è il piede della perpendicolare da G su AD.

**La catena di uguaglianze.** Ho verificato ogni passaggio: GH² = BH · HD (proprietà del cerchio); BH · HD = HB · BD − BH²; HE² − BH² = BE² − 2BH · BE; HB · BD − 2BH · BE = 2BH · EC; BE² = 2EC · AB per la costruzione. Numericamente, con AB = sin 4° 59′ 35″ e AD = sin 5° 17′ 20″, il rapporto GE²/(2EC · AH) vale 1,000000000000 per angoli AEG di 0°, 30°, 60°, 90°, 120°, 180°.

**Che cosa rappresenta.** Per il Cor. 3 della Prop. XXXIV, d(sin *i*) è proporzionale a sin *i* · sin 2*s* d(2*s*): la soluzione esatta è sin *i* = AB · (AD/AB)^((1 − cos 2*s*)/2). La costruzione di Newton dà AH = sin *i* con: 0° → 4° 59′ 35,00″; 30° → 5° 0′ 44,43″; 60° → 5° 3′ 55,49″; 90° → 5° 8′ 19,80″; 120° → 5° 12′ 47,95″; 180° → 5° 17′ 20,00″. La soluzione esatta dà gli stessi valori entro 0,01″. La costruzione è dunque, per questi dati, praticamente esatta. (L'argomento di Newton, «l'arco Gg è come GE», è esatto solo al primo ordine, perché G si muove sul cerchio di centro C e non su un cerchio di centro E; lo scarto è trascurabile perché BD è piccolo rispetto ad AB.)

### N5. Prop. XXXV: i numeri

- sin 5° 8½′ = 0,089619 → 896 (su 10000); 896/4 = 224. Torna. L'inclinazione media 5° 8½′ è circa la media di 5° 17′ 20″ e 4° 59′ 35″ (5° 8′ 27,5″).
- Rapporto 7 : 11 = 2/π approssimato (diametro : semicirconferenza).
- 224 × 7 × 2079,7 / 110000 = **29,6452** ≈ 29645/1000; × 33,1758″ = 983,50″ = **16′ 23,50″**. Torna.
- 16′ 23½″ − 1′ 21½″ = **15′ 2″**; 16′ 23½″ + 1′ 21½″ = **17′ 45″**; 1′ 21½″ è la metà di 2′ 43″. Tornano.
- 5° 17′ 20″ − 17′ 45″ = **4° 59′ 35″**. Torna.
- **2079 7/10 ore** dalle quadrature alle sizigie del nodo: con il moto medio annuo dei nodi della Prop. XXXIII (19° 18′ 1″ 23‴) e l'anno siderale della Prop. XXXII (365 g 6 h 9 m), un quarto di rivoluzione del Sole rispetto al nodo dura 90/(360 + 19,3004) anni = **2080,0 ore**. Lo scarto di 0,3 ore (0,015%) è trascurabile; Newton usa forse un moto del nodo leggermente diverso.

### N6. Scolio: equazione annua, equazioni dell'apogeo e dei nodi

- **Equazione annua.** 11′ 49″ × (16 11/12)/(16 7/8) = 710,75″ = 11′ 50,75″ ≈ **11′ 51″**. Torna. Il valore moderno dell'equazione annua è circa 11′ 9″ (non verificato sulle fonti allegate).
- **Equazione del centro del Sole.** Con *e* = 16 11/12 / 1000 = 0,016917, l'equazione massima calcolata con l'equazione di Keplero è 1° 56′ 18,9″ (al primo ordine 2*e* radianti = 1° 56′ 18,6″). Newton: **1° 56′ 20″**. Torna entro 1,2″. Il valore moderno, con *e* = 0,0167, è circa 1° 55′ 10″ (non verificato sulle fonti allegate).
- **Nel rapporto triplicato**: 1° 56′ 20″ × 3/2 = **2° 54′ 30″**. Torna esattamente (il moto «come l'inverso del cubo» dà, al primo ordine, un'equazione una volta e mezza maggiore).
- **Equazione dell'apogeo.** Dal testo stesso (III.G6.19) il moto medio diurno del Sole è 59′ 8″ 10‴ e il moto diurno del Sole dall'apogeo della Luna 52′ 27″ 16‴: il moto diurno dell'apogeo è la differenza, 6′ 40,9″. Allora 2° 54′ 30″ × 6′ 40,9″ / 59′ 8″ 10‴ = 19′ 42,98″ ≈ **19′ 43″**. Torna.
- **Equazione dei nodi.** Con il moto medio annuo dei nodi della Prop. XXXIII (19° 18′ 1″ 23‴ in 365 g 6 h 9 m, cioè 3′ 10,2″ al giorno) si ottiene 2° 54′ 30″ × 3′ 10,2″ / 59′ 8,2″ = **9′ 21″**; con il valore moderno di 3′ 10,6″ al giorno, 9′ 22,5″ (non verificato sulle fonti allegate). Newton: **9′ 24″**. **Lo scarto di 2–3″ non torna** con i dati delle fonti allegate; per 9′ 24″ servirebbe un moto dei nodi di circa 3′ 11,1″ al giorno. Segnalato, non corretto.
- **Equazione semestrale (3′ 45″).** Nel rapporto triplicato inverso della distanza, con *e* = 0,016917: alla distanza massima 225″ × (1,016917)⁻³ = 213,96″ = **3′ 34″** (torna); alla minima 225″ × (0,983083)⁻³ = 236,8″ = 3′ 56,8″, che Newton dà come **3′ 56″** «con ottima approssimazione» (arrotondato per difetto; 3′ 57″ sarebbe più vicino). Lieve.
- **Seconda semestrale (47″).** 47″ × (1,016917)⁻³ = 44,7″ ≈ **45″**; 47″ × (0,983083)⁻³ = 49,5″ ≈ **49″**. Tornano («circa»).

### N7. Scolio: l'epiciclo e la seconda equazione del centro

- **CB = 5505 · sin 12° 18′ = 1172,73** ≈ **1172¾**. Torna.
- **DF/DC.** (33 7/8 / 1000) × (52′ 27″ 16‴ / 59′ 8″ 10‴) = 0,033875 × 0,887010 = **0,030048 ≈ 3/100**. Torna. Ma il «doppio dell'eccentricità dell'orbe magno» dovrebbe essere 2 × 16 11/12 = **33 5/6**, non 33 7/8 (che è il doppio di 16 15/16); e con il primo valore del testo, 16 7/8, sarebbe 33¾. **La cifra 33 7/8 non torna** con nessuna delle due eccentricità del testo; l'effetto sul risultato (3/100) è nullo a questa precisione (0,0300 con 33 5/6). Segnalato, non corretto.
- **DF = 3/100 × 1172¾ = 35,18** ≈ **35⅕**. Torna.
- **Seconda equazione del centro.** La retta 2DF = 70,4 parti, vista alla distanza della Luna (100000 parti), sottende 70,4/100000 radianti = 145,2″ = **2′ 25″**. Torna.
- **Nomi moderni.** L'«equazione semestrale dell'apogeo» di 12° 18′, insieme alla variazione dell'eccentricità, corrisponde a ciò che oggi si chiama **evezione**, la maggiore disuguaglianza lunare dopo l'equazione del centro (circa 1° 16′ in longitudine) (non verificato sulle fonti allegate). La «semestrale» (3′ 45″) e la «seconda semestrale» (47″) sono piccole disuguaglianze che dipendono dalla posizione dell'apogeo e dei nodi rispetto al Sole (non verificato sulle fonti allegate per i nomi moderni).
- Il modello dell'epiciclo di Halley sul quale si innesta un secondo epiciclo (centro D, raggio DF) è descritto soltanto a parole; la figura non è disponibile. La Parte B registra la costruzione come dati, non come passi.

### N8. Scolio: l'ombra e l'epoca 1700

- **L'ombra.** L'aggiunta di 1′ o 1⅓′ al diametro dell'ombra calcolato con la parallasse corrisponde alla correzione empirica per l'atmosfera ancora oggi in uso (circa 1/50 del diametro) (non verificato sulle fonti allegate).
- **Le longitudini dell'epoca** (mezzogiorno di Greenwich, 31 dicembre 1700 giuliano), convertite in gradi dall'equinozio: Sole 290° 43′ 40″; apogeo del Sole 97° 44′ 30″; Luna 315° 21′ 00″; apogeo della Luna 338° 20′ 00″; nodo ascendente 147° 24′ 20″. La differenza dei meridiani 0 h 9 m 20 s corrisponde a 2° 20′ di longitudine geografica (9⅓ minuti × 15′ al minuto). Non ho dati delle fonti allegate per controllare i moti medi; la differenza Parigi–Greenwich moderna è 2° 20′ 14″ (non verificato sulle fonti allegate).

### N9. Prop. XXXVI: i numeri e il senso fisico

- 638092,6 × 60,5 = 38604602 → **38604600**. Torna.
- La forza che innalza (2 parti) e quella che abbassa (1 parte) si sommano: 38604600/3 = **12868200**. Torna.
- 12868200/289 = 44526,6 → **44527**; 85472/44527 = 1,919554 piedi = 1 piede 11,035 pollici = **1 piede 11 1/30 pollici** (11,0333). Torna.
- **In termini moderni**, la forza di marea del Sole sulla superficie terrestre, riferita a *g*, vale 2*K* sotto il Sole e −*K* a 90°, con *K* = (*M*☉/*M*⊕)(*R*/*d*)³ ≈ 2,57 × 10⁻⁸; la «somma» di Newton è 3*K* ≈ 7,71 × 10⁻⁸ = 1/12 960 000, molto vicino al suo 1/12 868 200 (non verificato sulle fonti allegate). Il passaggio dal rapporto delle forze al rapporto delle altezze (1 : 44527 rispetto al rigonfiamento equatoriale) è invece solo approssimato, perché le due deformazioni hanno forme diverse.
- **Seno verso del doppio dell'altezza.** 1 − cos 2*h* = 2 sin² *h*: la forza che solleva il mare è come il quadrato del seno dell'altezza del Sole, cioè (in termini moderni) come la componente verticale del potenziale di marea, che va come cos² della distanza zenitale (non verificato sulle fonti allegate per la formulazione moderna).

### N10. Prop. XXXVII: dalle maree al rapporto S : L

- **Bristol.** (L + S)/(L − S) = 45/25 = 9/5 dà, da solo, L/S = 3,5.
- **Plymouth.** (16 + 4,5)/(16 − 4,5) = 20,5/11,5 = 41/23 = 1,783; 9/5 = 1,800. «Concorda abbastanza». Torna.
- **cos 37° = 0,79863551** → **0,7986355**. Torna. L'angolo di 37° è il doppio di 18½°.
- **Declinazione.** 0,8570327 = cos² 22° 13′ (0,85703276). La declinazione ricavata da 0,8570327 è 22° 13′ 0″. **Il latino (22° 13′) è corretto; Motte (23° 13′, che darebbe 0,8446) sbaglia.**
- **Distanze a 18½°.** Con un'ellisse di semiassi 69 (sizigie) e 70 (quadrature) e centro nella Terra, la distanza a 18½° dalla sizigia è 69,098747 e a 18½° dalla quadratura 69,897345. **Tornano entrambe a tutte le cifre** (69,09874661; 69,89734470). Newton calcola dunque le distanze nell'ellisse della Prop. XXVIII.
- **Forze nel rapporto triplicato inverso.** (69,5/69,098747)³ = 1,0175222 e (69,5/69,897345)³ = 0,9830427. Tornano.
- **Soluzione.** (1,017522 L + 0,7986355 S)/(0,9830427 × 0,8570327 L − 0,7986355 S) = 9/5 dà L/S = 14 × 0,7986355 / (9 × 0,9830427 × 0,8570327 − 5 × 1,017522) = **4,48152**. Torna (S : L = 1 : 4,4815).
- 12868200/4,4815 = 2871405 → **2871400**. Torna.
- **Valori moderni.** Il rapporto delle forze di marea della Luna e del Sole è circa 2,18 (non verificato sulle fonti allegate): Newton sovrastima la forza della Luna di circa il doppio. La causa sta nei dati di marea (le altezze nei porti dipendono dalla risonanza dei bacini, come Newton stesso dice nel Cor. 1) e non nell'aritmetica, che è corretta.

### N11. Prop. XXXVII, Cor. 1–6: altezze, densità, massa

- **Cor. 1.** 1 piede 11 1/30 pollici = 1,91944 piedi; × 4,4815 = 8,60199 piedi = **8 piedi 7,224 pollici**; Newton 7 5/22 = 7,227. Torna (scarto 0,003 pollici). Somma 10,52 piedi ≈ **10½**. Torna. Nel perigeo la forza lunare cresce come (1 − *e*)⁻³: con un'eccentricità di 0,066 (quella massima che risulta da TC + CB = 6678 parti su 100000, III.G6.18–III.G6.20) si ottengono 12,48 piedi ≈ **12½**. Torna; con l'eccentricità media 0,055 si avrebbero 12,1 piedi.
- **Cor. 3.** 4,4815 × (32′ 12″ / 31′ 16½″)³ = 4,4815 × 1,09139 = **4,8910** → 4891 : 1000. Torna. 4891/4000 = 1,22275; 11/9 = 1,22222. Torna.
- **Cor. 4.** Massa ∝ densità × diametro³: (4891/4000) × (100/365)³ = 1/39,769; con 11/9 si ha 1/39,786. Newton **1 : 39,788**: torna con 11/9 (scarto nella quarta cifra significativa). Il valore moderno è 1 : 81,3 (non verificato sulle fonti allegate): l'errore viene interamente dal rapporto delle forze di marea (N10).
- **Cor. 5.** Gravità superficiale ∝ massa/diametro²: (1/39,788) × (365/100)² = 0,335 ≈ **1/3**. Torna. (Valore moderno circa 0,165, non verificato sulle fonti allegate.)
- **Cor. 6.** 39,788 + 1 = **40,788**. Torna.

### N12. Prop. XXXVII, Cor. 7: la caduta dei gravi rifatta

| Passo | Testo | Ricalcolo | Esito |
|---|---|---|---|
| 19658600 × 60⅖ | 1187379440 | 1187379440 | torna |
| × 39,788/40,788 | 1158268534 | 1158268441 | scarto di 93 piedi (8 × 10⁻⁸), trascurabile |
| seno verso dell'angolo descritto in 1 minuto, periodo 27 g 7 h 43 4/9 m | 12752341 (raggio 10¹⁵) | 12752196 | **non torna** alla quinta cifra (1,1 × 10⁻⁵): il valore del testo corrisponde a un periodo di 27 g 7 h 43,22 m |
| 1158268534 × seno verso | 14,7706353 | 14,7706353 | torna (con il seno verso del testo) |
| × 178 29/40 / 177 29/40 | 14,8538067 | 14,8537448 | scarto di 6 × 10⁻⁵ piedi, trascurabile |
| 1/60 della distanza | 197896573 | 19789657,33 | torna, letto con la virgola decimale (19789657,3) |
| caduta in 1 s a 19615800 piedi: 14,8538067 × (19789657,3/19615800)² | **15,11175** | **15,11828** | **non torna**: scarto di 0,0065 piedi = 0,94 linee |
| 15,11175 piedi in piedi, pollici, linee | 15 p. 1 poll. 4 1/11 lin. | 15 p. 1 poll. 4,09 lin. | torna (con il valore del testo) |
| eccesso a Parigi (48° 50′) rispetto a 45°, dalla legge della Prop. XX (incremento ∝ sin² latitudine, 1/229) | circa 2/3 di linea | 0,63 linee | torna |
| 4 1/11 + 2/3 | 4 25/33 | 4,7576 = 4 25/33 | torna |
| togliendo la forza centrifuga a Parigi (3,267 linee, Prop. XIX) | 1½ linee | 4,758 − 3,267 = 1,49 | torna |

Il passaggio da 14,8538067 piedi a 19789657,3 piedi a 15,11175 piedi a 19615800 piedi non torna con la legge dell'inverso del quadrato: il fattore (19789657,3/19615800)² = 1,017793 dà 15,11828. Il rapporto di Newton, 15,11175/14,8538067 = 1,017365, corrisponderebbe a una distanza di partenza di 19785386 piedi. Con il valore ricalcolato la caduta a Parigi sarebbe di circa 15 piedi 1 pollice 5,6 linee nel vuoto, e 2,4 linee togliendo la forza centrifuga, contro 1 7/9 linee della Prop. IV. L'accordo finale dichiarato da Newton («e con questa velocità cadono i gravi») resta dunque entro circa una linea in entrambi i casi. **Segnalato, non corretto**; il numero 15,11175 è anche in Motte.

### N13. Prop. XXXVII, Cor. 8–10: distanze e parallassi

- **Cor. 8.** 60⅖ × 69/69½ = 59,9655 = 60 − 0,0345 (circa 1/29, «circa la trentesima parte»); 60⅖ × 70/69½ = 60,8345 ≈ **60⅚** (60,8333). Tornano.
- **Cor. 9.** In semidiametri medi (× 19658600/19615800 = 1,002182): 60,0963 ≈ **60 1/10**; 60,9673 = 61 − 0,0327 ≈ **61 − 1/30**. Tornano.
- **Cor. 10.** Ricalcolo della parallasse orizzontale nelle sizigie, sin *p* = *r*(φ)/*d*, con *d* = 59,9655 semidiametri equatoriali, *r*(φ) il raggio dell'ellissoide di semiassi 19658600 e 19573000 piedi (Prop. XIX):

| Latitudine | Testo | Ricalcolo |
|---|---|---|
| 0° | 57′ 20″ | 57′ 19,9″ |
| 30° | 57′ 16″ | 57′ 16,1″ |
| 38° | 57′ 14″ | 57′ 14,2″ |
| 45° | 57′ 12″ | 57′ 12,4″ |
| 52° | 57′ 10″ | 57′ 10,6″ |
| 60° | 57′ 8″ | 57′ 8,6″ |
| 90° | 57′ 4″ | 57′ 4,9″ |

Tornano tutte entro un secondo (Newton tronca i decimali). La parallasse orizzontale equatoriale media moderna è circa 57′ 2,6″ (non verificato sulle fonti allegate).

### N14. Il capoverso finale

Newton elenca i dati che limitano la precisione del calcolo: l'attrazione magnetica della Terra (ignota), le misure dei gradi, le lunghezze dei pendoli, le leggi delle maree, la parallasse e i diametri apparenti. È un raro esempio, nei *Principia*, di bilancio esplicito delle fonti d'errore di un calcolo; utile in classe accanto alla nota N12.

---

## Controllo della copertura

Pagine 1726 dai marcatori ‹n› della trascrizione. Motte: estratto senza marcatori di pagina, «sezione corrispondente».

| Identificatori | Incipit latino | Contenuto | 1726 | Motte 1846 |
|---|---|---|---|---|
| III.G6.01–III.G6.03 | *Invenire variationem horariam* … *Hæc ita se habent* | Prop. XXXIV, enunciato, soluzione, orbita ellittica | pp. 454–455 | Prop. XXXIV |
| III.G6.04–III.G6.07 | *Si ad Nn erigatur* … *Quoniam inclinationis horaria variatio* | Prop. XXXIV, Cor. 1–4 | pp. 456–457 | Cor. 1–4 |
| III.G6.08–III.G6.10 | *Dato tempore invenire* … *Nam GEq æquale est* | Prop. XXXV, enunciato, costruzione, dimostrazione | pp. 457–458 | Prop. XXXV |
| III.G6.11–III.G6.13 | *In hac demonstratione* … *Si jam desideretur* | Prop. XXXV, calcolo numerico e inclinazione con i nodi in luogo qualsiasi | pp. 458–459 | idem |
| III.G6.14–III.G6.15 | *Hisce motuum lunarium* … *Inveni etiam* | Scolio: equazione annua; equazioni dell'apogeo e dei nodi | pp. 459–460 | Scholium |
| III.G6.16–III.G6.17 | *Per theoriam gravitatis constitit* … *Per eandem gravitatis theoriam actio* | Scolio: semestrale e seconda semestrale | pp. 460–461 | idem |
| III.G6.18–III.G6.20 | *Per eandem gravitatis theoriam apogæum* … *Computatio motus hujus* | Scolio: Horrocks, Halley, epiciclo, seconda equazione del centro | pp. 461–463 | idem |
| III.G6.21–III.G6.22 | *Cum atmosphæra terræ* … *Theoria vero lunæ* | Scolio: ombra; moti medi all'epoca 1700 | pp. 463–464 | idem |
| III.G6.23–III.G6.26 | *Invenire vim solis* … *Corol. cum vis centrifuga* | Prop. XXXVI e Cor. | pp. 464–465 | Prop. XXXVI |
| III.G6.27–III.G6.32 | *Invenire vim lunæ* … *Præterea diametri orbis* | Prop. XXXVII: Bristol, Plymouth, ritardo, declinazione, distanze, S : L | pp. 465–467 | Prop. XXXVII |
| III.G6.33–III.G6.34 | *Cum aqua vi solis agitata* … *Cum vis lunæ ad mare movendum* | Cor. 1–2 | pp. 467–468 | Cor. 1–2 |
| III.G6.35–III.G6.38 | *Quoniam vis lunæ* … *Et distantia centri lunæ* | Cor. 3–6 | pp. 468–469 | Cor. 3–6 |
| III.G6.39 | *Et mediocris distantia centri lunæ* | Cor. 7 | pp. 469–470 | Cor. 7 |
| III.G6.40–III.G6.43 | *Distantia mediocris centrorum* … *In his computationibus* | Cor. 8–10 e capoverso finale | p. 470 | Cor. 8–10 |

**Controlli eseguiti.**

1. **Copertura frase per frase.** Ho riletto in sequenza ogni periodo della trascrizione, da *Invenire variationem horariam* a *licebit calculum hunc omnem accuratius repetere*, contro la traduzione: nessuna frase manca. I periodi lunghi (Prop. XXXIV, Cor. 4; Scolio, epiciclo; Prop. XXXVII, Cor. 1 e 7) sono divisi in italiano senza omettere membri. I 43 identificatori sono consecutivi e unici (controllo automatico).
2. **Parte B.** `check.py` sul file finale: JSON valido; tutte le stringhe `la` (enunciati e passi) sono sottostringhe esatte della trascrizione; tutte le stringhe `en` sono sottostringhe esatte di Motte; ogni identificatore di `copertura` è presente nel testo.
3. **Aritmetica** (`verifica.py`): tutti i numeri delle Propp. XXXIV–XXXVII e dello Scolio (note N2–N13). Non tornano, e sono segnalati senza correzione: l'equazione massima dei nodi 9′ 24″ (ricalcolo 9′ 21″, N6); il doppio dell'eccentricità 33 7/8 (atteso 33 5/6, N7); il seno verso 12752341 (ricalcolo 12752196, N12); la caduta 15,11175 piedi (ricalcolo 15,1183, N12). Lievi: 3′ 56″ (ricalcolo 3′ 56,8″), 2079 7/10 ore (ricalcolo 2080,0).
4. **Geometria** (`verifica.py`): Prop. XXXIV, Cor. 3 e 4 (medie numeriche); Prop. XXXV, catena GE² = 2EC · AH e confronto della costruzione con la soluzione esatta (N3–N4).
5. **Tabelle numeriche:** il perimetro non contiene tabelle nella trascrizione. Le parallassi del Cor. 10 e il Cor. 7 sono messi in tabella soltanto nelle note.
6. **Motte.** Confronto di tutta la sezione corrispondente (righe 1–657); divergenze nel § A.9; 46 formule SVG controllate, 2 errate e 1 con un segno mancante (§ A.8).
7. **Separazione fra testo e commento.** Il testo tradotto non contiene formule moderne.

**Non ho potuto verificare:**

- **la stampa del 1726**: i punti del § A.6 restano «probabili»; in particolare 22° 13′ (Prop. XXXVII) e le cifre segnalate in N6, N7, N12 (9′ 24″, 33 7/8, 12752341, 15,11175) andrebbero controllate sulla scansione ECCO, per distinguere un errore di Newton da un refuso;
- **le figure originali** delle Propp. XXXIV, XXXV, dello Scolio e della Prop. XXXVI: le disposizioni dei punti sono ricostruite dal testo;
- **la paginazione di Motte**: l'estratto non ha marcatori di pagina;
- **i dati astronomici moderni** citati nelle note e i moti medi dell'epoca 1700, che le fonti allegate non permettono di controllare;
- il **moto diurno dei nodi** che Newton usa per l'equazione di 9′ 24″: non è dato nel perimetro.

---

## Registro del lavoro successivo

| Unità | Stato |
|---|---|
| Libro III, Propp. XXXIV–XXXVII con lo Scolio della Prop. XXXV | **Fascicolo 25a, presente documento, prima versione** |
| Seguito (Prop. XXXVIII, Lemmi I–XI, Ipotesi II, Propp. XXXIX–XL) | Fascicolo 25b |
| Refusi e cifre dubbie (§ A.6) | Da verificare sulla stampa del 1726 (scansione ECCO) |
| Segni dei sessantesimi | Qui «33″ 10‴ 33iv» come nella trascrizione; il Fascicolo 24b usa gli apici (33ⁱᵛ 12ᵛ): da uniformare |
| *digitus* «pollice» (misura) contro «dito» (eclissi) | Da confermare (§ A.0) |
| Pagine interattive | Parte B: Prop. XXXIV (con Cor. 4), Prop. XXXV (costruzione e calcolo), Prop. XXXVI, Prop. XXXVII (con Cor. 3 e 7); candidati a riquadri «che cosa non torna»: N10 (rapporto S : L contro il valore moderno) e N12 (la caduta dei gravi) |
| Scolio della Prop. XXXV (epiciclo di Halley) | Candidato a una pagina a sé con la costruzione dei due epicicli; la figura originale va consultata |
| Revisione filologica e scientifica indipendente | Da eseguire |

Il presente testo è una nuova traduzione assistita da IA. Non riproduce traduzioni italiane o inglesi moderne. **Licenza prevista** (decisione del curatore, Fascicolo 3): testi e traduzioni CC BY-SA 4.0, codice MIT. La trascrizione latina è © The Newton Project; i testi di Motte sono di pubblico dominio.

---
## Parte B — Dati per le pagine interattive

Unità incluse: **Prop. XXXIV** (soluzione) e il suo **Cor. 4** (calcolo di 2′ 43″); **Prop. XXXV** (costruzione e dimostrazione) e il **calcolo** che la segue (16′ 23½″ e inclinazioni estreme, unità `L3-P35-Var`); lo **Scolio** della Prop. XXXV come unità senza passi, con i dati delle equazioni (`L3-P35-Schol`); **Prop. XXXVI** e il suo **Cor.**; **Prop. XXXVII** (calcolo di S : L) e i suoi **Cor. 3** (densità) e **Cor. 7** (caduta dei gravi). **Esclusi**: i Cor. 1–3 della Prop. XXXIV (passaggi di calcolo già riassunti nel Cor. 4 e nella nota N3), il capoverso III.G6.13, i Cor. 1, 2, 4–6, 8–10 della Prop. XXXVII e il capoverso finale (risultati senza dimostrazione propria o già controllati nelle note N11–N13).

Convenzioni:

- `la`: testo latino esatto della trascrizione, refusi compresi (con gli spazi normalizzati come in check.py: i marcatori di pagina e [FIG] diventano uno spazio);
- `it`: la traduzione di questo fascicolo;
- `en`: Motte 1846, allineato per senso; le formule `[SVG n]` sono omesse nelle stringhe (check.py le ignora); gli errori di Motte sono segnalati in `nota`;
- `dipende_da`: soltanto i rimandi citati nella frase latina;
- `figura.mostra`: elementi da rendere visibili, cumulativi; vuoto nei passi di solo calcolo, dove le relazioni sono in `figura.evidenzia`;
- `dati`: valori numerici del testo e del ricalcolo (`verifica.py`).

```json
{
 "fascicolo": "25a-L3-P34-37",
 "versione": "0.1",
 "data": "2026-11-08",
 "convenzioni": {
  "dipende_da": "solo rimandi citati esplicitamente nella frase latina",
  "en": "Motte 1846, allineato per senso; le formule [SVG n] sono omesse nelle stringhe (check.py le ignora)",
  "figura.mostra": "elementi da rendere visibili al passo, cumulativi salvo indicazione; vuoto nei passi di solo calcolo",
  "la": ""
 },
 "unita": [
  {
   "id": "L3-P34",
   "tipo": "Propositio/Problema",
   "titolo": "Prop. XXXIV — variazione oraria dell'inclinazione dell'orbita lunare",
   "copertura": [
    "III.G6.01",
    "III.G6.02",
    "III.G6.03"
   ],
   "fonti": {
    "la": "",
    "en": "Motte 1846, sezione corrispondente (Book III, Prop. XXXIV)"
   },
   "enunciato": {
    "la": "",
    "it": "Trovare la variazione oraria dell'inclinazione dell'orbita lunare sul piano dell'eclittica.",
    "en": "To find the horary variation of the inclination of the moon's orbit to the plane of the ecliptic."
   },
   "figura_base": {
    "punti": [
     "T",
     "A",
     "a",
     "Q",
     "q",
     "N",
     "n",
     "P",
     "p",
     "m",
     "l",
     "G",
     "g",
     "I",
     "Z"
    ],
    "vincoli": [
     "T Terra al centro; Aa linea delle sizigie (verso il Sole), Qq delle quadrature",
     "Nn linea dei nodi; mTl posizioni successive della linea dei nodi",
     "p proiezione di P sul piano dell'eclittica",
     "G piede della perpendicolare da P su Tm; g intersezione di pG prolungata con Tl",
     "IT proiezione di TP sulla linea delle sizigie (seno della distanza dalla quadratura); AZ perpendicolare da A sulla linea dei nodi"
    ]
   },
   "passi": [
    {
     "id": "L3-P34-p1",
     "la": "",
     "it": "Rappresentino A e a le sizigie; Q e q le quadrature; N e n i nodi; P il luogo della Luna nella sua orbita; p la traccia di quel luogo sul piano dell'eclittica; e mTl il moto momentaneo dei nodi, come sopra.",
     "en": "Let A and a represent the syzygies; Q, and q the quadratures; N and n the nodes; P the place of the moon in its orbit; p the orthographic projection of that place upon the plane of the ecliptic; and mTl the momentaneous motion of the nodes as above.",
     "dipende_da": [],
     "figura": {
      "mostra": [
       "T (Terra)",
       "sizigie A, a",
       "quadrature Q, q",
       "nodi N, n",
       "P sull'orbita",
       "p traccia di P sull'eclittica",
       "mTl moto momentaneo dei nodi"
      ],
      "evidenzia": [
       "Pp ⊥ piano dell'eclittica"
      ]
     },
     "nota": "«ut supra» rimanda alla Prop. XXX, dove mTl è definito; non è un rimando esplicito e non entra in dipende_da."
    },
    {
     "id": "L3-P34-p2",
     "la": "",
     "it": "Se sulla linea Tm si abbassa la perpendicolare PG, si congiunge pG e la si prolunga finché incontri Tl in g, e si congiunge anche Pg, l'angolo PGp sarà l'inclinazione dell'orbita lunare sul piano dell'eclittica quando la Luna si trova in P, e l'angolo Pgp l'inclinazione della stessa orbita dopo che è trascorso un momento di tempo; e perciò l'angolo GPg sarà la variazione momentanea dell'inclinazione.",
     "en": "If upon Tm we let fall the perpendicular PG, and joining pG we produce it till it meet Tl in g, and join also Pg, the angle PGp will be the inclination of the moon's orbit to the plane of the ecliptic when the moon is in P; and the angle Pgp will be the inclination of the same after a small moment of time is elapsed; and therefore the angle GPg will be the momentaneous variation of the inclination.",
     "dipende_da": [],
     "figura": {
      "mostra": [
       "PG ⊥ Tm",
       "pG prolungata fino a g su Tl",
       "Pg"
      ],
      "evidenzia": [
       "angolo PGp = inclinazione",
       "angolo Pgp = inclinazione dopo un momento",
       "angolo GPg = variazione"
      ]
     }
    },
    {
     "id": "L3-P34-p3",
     "la": "",
     "it": "Ora questo angolo GPg sta all'angolo GTg come TG sta a PG e Pp sta a PG, considerati congiuntamente.",
     "en": "But this angle GPg is to the angle GTg as TG to PG and Pp to PG conjunctly.",
     "dipende_da": [],
     "figura": {
      "mostra": [
       "angolo GTg"
      ],
      "evidenzia": [
       "GPg : GTg = (TG/PG)·(Pp/PG)"
      ]
     }
    },
    {
     "id": "L3-P34-p4",
     "la": "",
     "it": "E perciò, se al momento di tempo si sostituisce un'ora, poiché l'angolo GTg (per la Prop. XXX) sta all'angolo di 33″ 10‴ 33ⁱᵛ come IT × PG × AZ sta a AT³, l'angolo GPg (ossia la variazione oraria dell'inclinazione) starà all'angolo di 33″ 10‴ 33ⁱᵛ come IT × AZ × TG × Pp/PG sta a AT³. C.V.T.",
     "en": "And, therefore, if for the moment of time we assume an hour, since the angle GTg (by Prop. XXX) is to the angle 33'' 10''' 33iv. as IT × PG × AZ to AT3, the angle GPg (or the horary variation of the inclination) will be to the angle 33'' 10''' 33iv. as to AT3. Q.E.I.",
     "dipende_da": [
      "Prop. XXX"
     ],
     "figura": {
      "mostra": [
       "IT",
       "AZ",
       "TG"
      ],
      "evidenzia": [
       "variazione oraria : 33″ 10‴ 33iv = IT·AZ·TG·(Pp/PG) : AT³"
      ]
     },
     "nota": "Motte rende la formula finale con SVG 1056 (IT × AZ × TG × Pp/PG), che concorda."
    },
    {
     "id": "L3-P34-p5",
     "la": "",
     "it": "Queste cose stanno così nell'ipotesi che la Luna giri uniformemente in un'orbita circolare. Se invece quell'orbita è ellittica, il moto medio dei nodi diminuirà nel rapporto dell'asse minore all'asse maggiore, come si è esposto sopra; e nello stesso rapporto diminuirà anche la variazione dell'inclinazione.",
     "en": "And thus it would be if the moon was uniformly revolved in a circular orbit. But if the orbit is elliptical, the mean motion of the nodes will be diminished in proportion of the lesser axis to the greater, as we have shewn above; and the variation of the inclination will be also diminished in the same proportion.",
     "dipende_da": [],
     "figura": {
      "mostra": [],
      "evidenzia": [
       "fattore asse minore / asse maggiore (69 : 70)"
      ]
     },
     "nota": "Tre frasi latine in un passo (correzione per l'orbita ellittica); «uti supra expositum est» rimanda al Cor. della Prop. XXXI, non citato per numero."
    }
   ]
  },
  {
   "id": "L3-P34-Cor4",
   "tipo": "Corollarium",
   "titolo": "Prop. XXXIV, Cor. 4 — variazione totale con i nodi nelle quadrature (2′ 43″)",
   "copertura": [
    "III.G6.07"
   ],
   "fonti": {
    "la": "",
    "en": "Motte 1846, sezione corrispondente (Prop. XXXIV, Cor. 4)"
   },
   "enunciato": {
    "la": "",
    "it": "E perciò la variazione totale, risultante dalla somma di tutte le variazioni orarie nel tempo predetto, è di 163″, ossia 2′ 43″.",
    "en": "And, therefore, the whole variation, composed out of the sum of all the horary variations in the aforesaid time, is 163'', or 2' 43''."
   },
   "passi": [
    {
     "id": "L3-P34-Cor4-p1",
     "la": "",
     "it": "Poiché la variazione oraria dell'inclinazione, quando i nodi si trovano nelle quadrature, sta (per questa proposizione) all'angolo di 33″ 10‴ 33ⁱᵛ come IT × AZ × TG × Pp/PG sta a AT³, cioè come (IT × TG)/(½AT) × Pp/PG sta a 2AT, ossia come il seno del doppio della distanza della Luna dalle quadrature, moltiplicato per Pp/PG, sta al doppio del raggio,",
     "en": "Seeing the horary variation of the inclination, when the nodes are in the quadratures, is (by this Prop.) to the angle 33'' 10''' 33iv. as to AT3, that is, as to 2AT, that is, as the sine of double the distance of the moon from the quadratures multiplied into to twice the radius,",
     "dipende_da": [
      "Prop. XXXIV"
     ],
     "figura": {
      "mostra": [],
      "evidenzia": [
       "con i nodi nelle quadrature AZ = AT",
       "(IT·TG)/(½AT) : 2AT = sin 2(distanza dalla quadratura) : 2"
      ]
     },
     "nota": "Prima parte di una frase latina lunga; «per hanc propositionem» → Prop. XXXIV."
    },
    {
     "id": "L3-P34-Cor4-p2",
     "la": "",
     "it": "la somma di tutte le variazioni orarie nel tempo in cui la Luna, in questa posizione dei nodi, passa dalla quadratura alla sizigia (cioè nello spazio di 177⅙ ore) starà alla somma di altrettanti angoli di 33″ 10‴ 33ⁱᵛ, ossia 5878″, come la somma di tutti i seni del doppio della distanza della Luna dalle quadrature, moltiplicata per Pp/PG, sta alla somma di altrettanti diametri; cioè come il diametro moltiplicato per Pp/PG sta alla circonferenza; cioè, se l'inclinazione è di 5° 1′, come 7 × 874/10000 sta a 22, ossia come 278 sta a 10000.",
     "en": "the sum of all the horary variations during the time that the moon, in this situation of the nodes, passes from the quadrature to the syzygy (that is, in the space of hours) will be to the sum of as many angles 33'' 10''' 33iv. or 5878'', as the sum of all the sines of double the distance of the moon from the quadratures multiplied into to the sum of as many diameters; that is, as the diameter multiplied into to the circumference; that is, if the inclination be 5° 1', as to 22, or as 278 to 10000.",
     "dipende_da": [],
     "figura": {
      "mostra": [],
      "evidenzia": [
       "177⅙ ore × 33,1758″ = 5878″",
       "media di ½ sin 2u sul quadrante = 1/π ≈ 7/22",
       "sin 5° 1′ = 0,0874"
      ]
     },
     "nota": "Seconda parte della stessa frase. Motte rende 177⅙ con SVG 1066 e 7 × 874/10000 con SVG 1067, entrambi corretti."
    }
   ],
   "dati": {
    "unita_33_10_33": 33.1758,
    "ore_quadratura_sizigia": 177.1667,
    "somma_angoli_sec": 5878,
    "sin_5_1": 0.087446,
    "rapporto_7_874_22": 0.027809,
    "variazione_tot_sec": 163.4,
    "verifica": "torna (nota N3)"
   }
  },
  {
   "id": "L3-P35",
   "tipo": "Propositio/Problema",
   "titolo": "Prop. XXXV — l'inclinazione in un tempo dato (costruzione con il cerchio BGD)",
   "copertura": [
    "III.G6.08",
    "III.G6.09",
    "III.G6.10"
   ],
   "fonti": {
    "la": "",
    "en": "Motte 1846, sezione corrispondente (Prop. XXXV)"
   },
   "enunciato": {
    "la": "",
    "it": "Dato il tempo, trovare l'inclinazione dell'orbita lunare sul piano dell'eclittica.",
    "en": "To a given time to find the inclination of the moon's orbit to the plane of the ecliptic."
   },
   "figura_base": {
    "punti": [
     "A",
     "B",
     "E",
     "C",
     "D",
     "G",
     "H",
     "g",
     "h"
    ],
    "vincoli": [
     "A, B, E, C, D allineati in quest'ordine",
     "AB = sin 4° 59′ 35″, AD = sin 5° 17′ 20″ (valori di III.G6.13)",
     "C punto medio di BD; cerchio di centro C e raggio CB",
     "CE : EB = EB : 2BA",
     "angolo AEG = 2 × distanza dei nodi dalle quadrature",
     "GH ⊥ AD"
    ],
    "verifica": "GE²/(2EC·AH) = 1 per ogni G; AH coincide entro 0,01″ con la soluzione esatta sin i = AB·(AD/AB)^((1−cos AEG)/2) (nota N4)"
   },
   "passi": [
    {
     "id": "L3-P35-p1",
     "la": "",
     "it": "Sia AD il seno dell'inclinazione massima, e AB il seno dell'inclinazione minima.",
     "en": "Let AD be the sine of the greatest inclination, and AB the sine of the least.",
     "dipende_da": [],
     "figura": {
      "mostra": [
       "retta A–B–D",
       "AB",
       "AD"
      ],
      "evidenzia": [
       "AB = sin i min",
       "AD = sin i max"
      ]
     }
    },
    {
     "id": "L3-P35-p2",
     "la": "",
     "it": "Si divida BD a metà in C, e con centro C e raggio BC si descriva il cerchio BGD.",
     "en": "Bisect BD in C; and round the centre C, with the interval BC, describe the circle BGD.",
     "dipende_da": [],
     "figura": {
      "mostra": [
       "C punto medio di BD",
       "cerchio BGD"
      ],
      "evidenzia": []
     }
    },
    {
     "id": "L3-P35-p3",
     "la": "",
     "it": "In AC si prenda CE in rapporto a EB come EB sta a 2BA; e se, al tempo dato, si costruisce l'angolo AEG uguale al doppio della distanza dei nodi dalle quadrature, e su AD si abbassa la perpendicolare GH, AH sarà il seno dell'inclinazione cercata.",
     "en": "In AC take CE in the same proportion to EB as EB to twice BA. And if to the time given we set off the angle AEG equal to double the distance of the nodes from the quadratures, and upon AD let fall the perpendicular GH, AH will be the sine of the inclination required.",
     "dipende_da": [],
     "figura": {
      "mostra": [
       "E fra B e C con CE·2BA = EB²",
       "G sul cerchio",
       "angolo AEG",
       "GH ⊥ AD",
       "H"
      ],
      "evidenzia": [
       "AH = sin i cercato"
      ]
     }
    },
    {
     "id": "L3-P35-p4",
     "la": "",
     "it": "Infatti GE² è uguale a GH² + HE² = BH × HD + HE² = HB × BD + HE² − BH² = HB × BD + BE² − 2BH × BE = BE² + 2EC × BH = 2EC × AB + 2EC × BH = 2EC × AH.",
     "en": "For GE2 is equal to GH2 + HE2 = BHD + HE2 = HBD + HE2 - BH2 = HBD + BE2 - 2BH × BE = BE2 + 2EC × BH = 2EC × AB + 2EC × BH = 2EC × AH;",
     "dipende_da": [],
     "figura": {
      "mostra": [
       "GE",
       "GH",
       "HE"
      ],
      "evidenzia": [
       "GE² = 2EC·AH"
      ]
     },
     "nota": "Catena verificata passo per passo e numericamente (nota N4). BHD e HBD sono i rettangoli BH·HD e HB·BD."
    },
    {
     "id": "L3-P35-p5",
     "la": "",
     "it": "Perciò, poiché 2EC è dato, GE² è come AH.",
     "en": "wherefore since 2EC is given. GE2 will be as AH.",
     "dipende_da": [],
     "figura": {
      "mostra": [],
      "evidenzia": [
       "GE² ∝ AH"
      ]
     },
     "nota": "Motte ha un punto dopo «given», refuso di punteggiatura."
    },
    {
     "id": "L3-P35-p6",
     "la": "",
     "it": "Rappresenti ora AEg il doppio della distanza dei nodi dalle quadrature dopo che è trascorso un dato momento di tempo; l'arco Gg, per l'angolo dato GEg, sarà come la distanza GE.",
     "en": "Now let AEg represent double the distance of the nodes from the quadratures, in a given moment of time after, and the arc Gg, on account of the given angle GEg, will be as the distance GE.",
     "dipende_da": [],
     "figura": {
      "mostra": [
       "g sul cerchio",
       "angolo GEg",
       "arco Gg"
      ],
      "evidenzia": [
       "Gg ∝ GE (al primo ordine)"
      ]
     }
    },
    {
     "id": "L3-P35-p7",
     "la": "",
     "it": "Ma Hh sta a Gg come GH sta a GC, e perciò Hh è come il prodotto GH × Gg, ossia GH × GE; cioè come GH/GE × GE², ossia GH/GE × AH; cioè come AH e il seno dell'angolo AEG considerati congiuntamente.",
     "en": "But Hh is to Gg as GH to GC, and, therefore, Hh is as the rectangle GH × Gg, or GH × GE, that is, as , or ; that is, as AH and the sine of the angle AEG conjunctly.",
     "dipende_da": [],
     "figura": {
      "mostra": [
       "h piede della perpendicolare da g",
       "Hh"
      ],
      "evidenzia": [
       "Hh ∝ AH · sin AEG"
      ]
     }
    },
    {
     "id": "L3-P35-p8",
     "la": "",
     "it": "Dunque, se AH in un caso qualsiasi è il seno dell'inclinazione, esso crescerà con gli stessi incrementi del seno dell'inclinazione, per il Cor. 3 della proposizione precedente, e perciò resterà sempre uguale a quel seno.",
     "en": "If, therefore, in any one case, AH be the sine of inclination, it will increase by the same increments as the sine of inclination doth, by Cor. 3 of the preceding Prop. and therefore will always continue equal to that sine.",
     "dipende_da": [
      "Prop. XXXIV, Cor. 3"
     ],
     "figura": {
      "mostra": [],
      "evidenzia": [
       "d(AH) e d(sin i) obbediscono alla stessa legge"
      ]
     }
    },
    {
     "id": "L3-P35-p9",
     "la": "",
     "it": "Ma AH, quando il punto G cade in uno dei due punti B o D, è uguale a questo seno, e perciò gli resta sempre uguale. C.V.D.",
     "en": "But when the point G falls upon either point B or D, AH is equal to this sine, and therefore remains always equal thereto. Q.E.D.",
     "dipende_da": [],
     "figura": {
      "mostra": [
       "G in B",
       "G in D"
      ],
      "evidenzia": [
       "condizione iniziale: AH = AB o AD"
      ]
     }
    }
   ]
  },
  {
   "id": "L3-P35-Var",
   "tipo": "Calculus",
   "titolo": "Prop. XXXV, calcolo — variazione totale BD (16′ 23½″) e inclinazioni estreme",
   "copertura": [
    "III.G6.11",
    "III.G6.12"
   ],
   "fonti": {
    "la": "",
    "en": "Motte 1846, sezione corrispondente (Prop. XXXV, dopo il Q.E.D.)"
   },
   "enunciato": {
    "la": "",
    "it": "Perciò, se si compongono tutti i rapporti, la variazione totale BD starà a 33″ 10‴ 33ⁱᵛ come 224 × 7 × 2079 7/10 sta a 110000, cioè come 29645 sta a 1000, e di qui quella variazione BD risulterà di 16′ 23½″.",
    "en": "Wherefore, compounding all these proportions, we shall have the whole variation BD to 33'' 10''' 33iv. as to 110000, that is, as 29645 to 1000; and from thence that variation BD will come out 16'"
   },
   "passi": [
    {
     "id": "L3-P35-Var-p1",
     "la": "",
     "it": "In questa dimostrazione ho supposto che l'angolo BEG, che è il doppio della distanza dei nodi dalle quadrature, cresca uniformemente:",
     "en": "In this demonstration I have supposed that the angle BEG, representing double the distance of the nodes from the quadratures, increaseth uniformly;",
     "dipende_da": [],
     "figura": {
      "mostra": [],
      "evidenzia": []
     }
    },
    {
     "id": "L3-P35-Var-p2",
     "la": "",
     "it": "non c'è infatti il tempo di soppesare tutte le minuzie delle disuguaglianze.",
     "en": "for I cannot descend to every minute circumstance of inequality.",
     "dipende_da": [],
     "figura": {
      "mostra": [],
      "evidenzia": []
     }
    },
    {
     "id": "L3-P35-Var-p3",
     "la": "",
     "it": "Si immagini ora che l'angolo BEG sia retto, e che in questo caso Gg sia l'incremento orario della doppia distanza dei nodi e del Sole l'uno dall'altro; la variazione oraria dell'inclinazione, nello stesso caso (per il Cor. 3 dell'ultima proposizione), starà a 33″ 10‴ 33ⁱᵛ come il prodotto del seno AH dell'inclinazione e del seno dell'angolo retto BEG, che è il doppio della distanza dei nodi dal Sole, sta al quadruplo del quadrato del raggio; cioè come il seno AH dell'inclinazione media sta al quadruplo del raggio; ossia (poiché quell'inclinazione media è di circa 5° 8½′) come il suo seno 896 sta al quadruplo del raggio, 40000, ovvero come 224 sta a 10000.",
     "en": "Now suppose that BEG is a right angle, and that Gg is in this case the horary increment of double the distance of the nodes from the sun; then, by Cor. 3 of the last Prop. the horary variation of the inclination in the same case will be to 33'' 10''' 33iv. as the rectangle of AH, the sine of the inclination, into the sine of the right angle BEG, double the distance of the nodes from the sun, to four times the square of the radius; that is, as AH, the sine of the mean inclination, to four times the radius; that is, seeing the mean inclination is about 5° , as its sine 896 to 40000, the quadruple of the radius, or as 224 to 10000.",
     "dipende_da": [
      "Prop. XXXIV, Cor. 3"
     ],
     "figura": {
      "mostra": [
       "BEG retto"
      ],
      "evidenzia": [
       "sin 5° 8½′ = 0,0896",
       "896/40000 = 224/10000"
      ]
     },
     "nota": "Motte rende 8½ con SVG 1010 senza il segno ′."
    },
    {
     "id": "L3-P35-Var-p4",
     "la": "",
     "it": "Ora la variazione totale, corrispondente alla differenza dei seni BD, sta a quella variazione oraria come il diametro BD sta all'arco Gg; cioè come il diametro BD sta alla semicirconferenza BGD e il tempo di 2079 7/10 ore, nel quale il nodo procede dalle quadrature alle sizigie, sta a un'ora, considerati congiuntamente; ossia come 7 sta a 11 e 2079 7/10 sta a 1.",
     "en": "But the whole variation corresponding to BD, the difference of the sines, is to this horary variation as the diameter BD to the arc Gg, that is, conjunctly as the diameter BD to the semi-circumference BGD, and as the time of hours, in which the node proceeds from the quadratures to the syzygies, to one hour, that is as 7 to 11, and to 1.",
     "dipende_da": [],
     "figura": {
      "mostra": [
       "diametro BD",
       "semicirconferenza BGD"
      ],
      "evidenzia": [
       "BD : semicirconferenza = 7 : 11",
       "2079,7 ore"
      ]
     },
     "nota": "Motte rende 2079 7/10 con SVG 1070 (corretto)."
    },
    {
     "id": "L3-P35-Var-p5",
     "la": "",
     "it": "Questa è la variazione massima dell'inclinazione, in quanto non si considera il luogo della Luna nella sua orbita.",
     "en": "And this is the greatest variation of the inclination, abstracting from the situation of the moon in its orbit;",
     "dipende_da": [],
     "figura": {
      "mostra": [],
      "evidenzia": []
     }
    },
    {
     "id": "L3-P35-Var-p6",
     "la": "",
     "it": "Infatti l'inclinazione, se i nodi si trovano nelle sizigie, non cambia affatto per la diversa posizione della Luna.",
     "en": "for if the nodes are in the syzygies, the inclination suffers no change from the various positions of the moon.",
     "dipende_da": [],
     "figura": {
      "mostra": [],
      "evidenzia": []
     }
    },
    {
     "id": "L3-P35-Var-p7",
     "la": "",
     "it": "Ma se i nodi stanno nelle quadrature, l'inclinazione è minore quando la Luna si trova nelle sizigie che quando si trova nelle quadrature, per un eccesso di 2′ 43″, come abbiamo indicato nel Cor. 4 della proposizione precedente.",
     "en": "But if the nodes are in the quadratures, the inclination is less when the moon is in the syzygies than when it is in the quadratures by a difference of 2' 43'', as we shewed in Cor. 4 of the preceding Prop.;",
     "dipende_da": [
      "Prop. XXXIV, Cor. 4"
     ],
     "figura": {
      "mostra": [],
      "evidenzia": [
       "eccesso 2′ 43″"
      ]
     }
    },
    {
     "id": "L3-P35-Var-p8",
     "la": "",
     "it": "E la variazione totale media BD, diminuita della metà di questo eccesso, 1′ 21½″, diventa 15′ 2″ nelle quadrature lunari, e aumentata della stessa diventa 17′ 45″ nelle sizigie della Luna.",
     "en": "and the whole mean variation BD, diminished by 1' , the half of this excess, becomes 15' 2'', when the moon is in the quadratures; and increased by the same, becomes 17' 45'' when the moon is in the syzygies.",
     "dipende_da": [],
     "figura": {
      "mostra": [],
      "evidenzia": [
       "16′ 23½″ ∓ 1′ 21½″ = 15′ 2″, 17′ 45″"
      ]
     },
     "nota": "Motte rende 1′ 21½″ con SVG 1073 (corretto)."
    },
    {
     "id": "L3-P35-Var-p9",
     "la": "",
     "it": "Se dunque la Luna è posta nelle sizigie, la variazione totale nel passaggio dei nodi dalle quadrature alle sizigie sarà di 17′ 45″; e perciò, se l'inclinazione, quando i nodi si trovano nelle sizigie, è di 5° 17′ 20″, la stessa, quando i nodi sono nelle quadrature e la Luna nelle sizigie, sarà di 4° 59′ 35″.",
     "en": "If, therefore, the moon be in the syzygies, the whole variation in the passage of the nodes from the quadratures to the syzygies will be 17' 45''; and, therefore, if the inclination be 5° 17' 20'', when the nodes are in the syzygies, it will be 4° 59' 35'' when the nodes are in the quadratures and the moon in the syzygies.",
     "dipende_da": [],
     "figura": {
      "mostra": [],
      "evidenzia": [
       "5° 17′ 20″ − 17′ 45″ = 4° 59′ 35″"
      ]
     }
    },
    {
     "id": "L3-P35-Var-p10",
     "la": "",
     "it": "E che le cose stiano così è confermato dalle osservazioni.",
     "en": "The truth of all which is confirmed by observations.",
     "dipende_da": [],
     "figura": {
      "mostra": [],
      "evidenzia": []
     }
    }
   ],
   "nota": "L'enunciato è la frase conclusiva del calcolo (16′ 23½″), posta prima dei passi 5–10 che ne derivano le inclinazioni estreme; i passi 1–4 la preparano. Motte rende 23½″ con SVG 1072 (corretto).",
   "dati": {
    "rapporto_BD": 29.6452,
    "BD_sec": 983.5,
    "BD": "16′ 23,50″",
    "quadrature": "15′ 2″",
    "sizigie": "17′ 45″",
    "incl_min": "4° 59′ 35″",
    "ore_nodo_quadr_siz_testo": 2079.7,
    "ore_nodo_ricalcolo": 2080.0,
    "verifica": "torna (nota N5)"
   }
  },
  {
   "id": "L3-P35-Schol",
   "tipo": "Scholium",
   "titolo": "Scolio della Prop. XXXV — le equazioni della Luna, l'epiciclo di Halley, l'ombra, l'epoca 1700",
   "copertura": [
    "III.G6.14",
    "III.G6.15",
    "III.G6.16",
    "III.G6.17",
    "III.G6.18",
    "III.G6.19",
    "III.G6.20",
    "III.G6.21",
    "III.G6.22"
   ],
   "fonti": {
    "la": "",
    "en": "Motte 1846, sezione corrispondente (Scholium)"
   },
   "passi": [],
   "nota": "Lo Scolio non è una proposizione e non ha una dimostrazione da scandire per frasi: entra come unità senza passi, con i valori delle equazioni e l'esito dei ricalcoli nel campo dati. La costruzione dei due epicicli (III.G6.18–III.G6.20) è candidata a una pagina a sé (Registro).",
   "dati": {
    "equazione_annua": {
     "testo_ecc_16_7_8": "11′ 49″",
     "testo_ecc_16_11_12": "11′ 51″",
     "ricalcolo": "11′ 50,75″",
     "esito": "torna"
    },
    "equazione_centro_Sole": {
     "testo": "1° 56′ 20″",
     "ricalcolo_Keplero": "1° 56′ 18,9″",
     "esito": "torna"
    },
    "equazione_rapporto_triplicato": {
     "testo": "2° 54′ 30″",
     "ricalcolo": "2° 54′ 30″",
     "esito": "torna"
    },
    "equazione_apogeo": {
     "testo": "19′ 43″",
     "ricalcolo": "19′ 42,98″",
     "esito": "torna"
    },
    "equazione_nodi": {
     "testo": "9′ 24″",
     "ricalcolo_Prop_XXXIII": "9′ 21″",
     "esito": "non torna (2–3″), segnalato"
    },
    "semestrale": {
     "media": "3′ 45″",
     "dist_max_testo": "3′ 34″",
     "dist_max_ricalcolo": "3′ 33,96″",
     "dist_min_testo": "3′ 56″",
     "dist_min_ricalcolo": "3′ 56,8″",
     "esito": "torna (lieve arrotondamento per difetto)"
    },
    "seconda_semestrale": {
     "media": "47″",
     "perigeo_testo": "49″",
     "perigeo_ricalcolo": "49,5″",
     "apogeo_testo": "45″",
     "apogeo_ricalcolo": "44,7″",
     "esito": "torna"
    },
    "epiciclo": {
     "TC": 5505,
     "CB_testo": 1172.75,
     "CB_ricalcolo": 1172.73,
     "DF_testo": 35.2,
     "DF_ricalcolo": 35.18,
     "DF_DC": 0.030048,
     "doppia_ecc_testo": "33 7/8",
     "doppia_ecc_attesa": "33 5/6",
     "esito": "33 7/8 non torna con 16 11/12; il risultato 3/100 non cambia"
    },
    "seconda_equazione_centro": {
     "testo": "2′ 25″",
     "ricalcolo": "2′ 25,2″",
     "esito": "torna"
    },
    "epoca_1700_longitudini_gradi": {
     "Sole": 290.7278,
     "apogeo_Sole": 97.7417,
     "Luna": 315.35,
     "apogeo_Luna": 338.3333,
     "nodo_ascendente": 147.4056,
     "diff_meridiani": "0 h 9 m 20 s = 2° 20′"
    }
   }
  },
  {
   "id": "L3-P36",
   "tipo": "Propositio/Problema",
   "titolo": "Prop. XXXVI — la forza del Sole sul mare (1 : 12868200)",
   "copertura": [
    "III.G6.23",
    "III.G6.24",
    "III.G6.25"
   ],
   "fonti": {
    "la": "",
    "en": "Motte 1846, sezione corrispondente (Prop. XXXVI)"
   },
   "enunciato": {
    "la": "",
    "it": "Trovare la forza del Sole per muovere il mare.",
    "en": "To find the force of the sun to move the sea."
   },
   "passi": [
    {
     "id": "L3-P36-p1",
     "la": "",
     "it": "La forza ML, ossia PT, con cui il Sole perturba i moti lunari nelle quadrature lunari, stava (per la Prop. XXV di questo Libro) alla forza di gravità presso di noi come 1 sta a 638092,6.",
     "en": "The sun's force ML or PT to disturb the motions of the moon, was (by Prop. XXV.) in the moon's quadratures, to the force of gravity with us, as 1 to 638092,6;",
     "dipende_da": [
      "Prop. XXV"
     ],
     "figura": {
      "mostra": [
       "T Terra",
       "L, M, P, K della figura della Prop. XXV"
      ],
      "evidenzia": [
       "ML : gravità = 1 : 638092,6"
      ]
     }
    },
    {
     "id": "L3-P36-p2",
     "la": "",
     "it": "E la forza TM − LM, ossia 2PK, nelle sizigie lunari è doppia.",
     "en": "and the force TM - LM or 2PK in the moon's syzygies is double that quantity.",
     "dipende_da": [],
     "figura": {
      "mostra": [],
      "evidenzia": [
       "2PK = 2 ML"
      ]
     }
    },
    {
     "id": "L3-P36-p3",
     "la": "",
     "it": "Queste forze poi, se si scende alla superficie della Terra, diminuiscono nel rapporto delle distanze dal centro della Terra, cioè nel rapporto di 60½ a 1; e perciò la prima forza, sulla superficie della Terra, sta alla forza di gravità come 1 sta a 38604600.",
     "en": "But, descending to the surface of the earth, these forces are diminished in proportion of the distances from the centre of the earth, that is, in the proportion of to 1; and therefore the former force on the earth's surface is to the force of gravity as 1 to 38604600;",
     "dipende_da": [],
     "figura": {
      "mostra": [],
      "evidenzia": [
       "638092,6 × 60½ = 38604600"
      ]
     },
     "nota": "Motte rende 60½ con SVG 968 (corretto)."
    },
    {
     "id": "L3-P36-p4",
     "la": "",
     "it": "Per effetto di questa forza il mare si abbassa nei luoghi che distano 90 gradi dal Sole.",
     "en": "and by this force the sea is depressed in such places as are 90 degrees distant from the sun.",
     "dipende_da": [],
     "figura": {
      "mostra": [
       "Terra",
       "Sole",
       "luoghi a 90° dal Sole"
      ],
      "evidenzia": [
       "abbassamento"
      ]
     }
    },
    {
     "id": "L3-P36-p5",
     "la": "",
     "it": "Per effetto dell'altra, che è doppia, il mare si innalza sia sotto il Sole sia nella regione opposta al Sole.",
     "en": "But by the other force, which is twice as great, the sea is raised not only in the places directly under the sun, but in those also which are directly opposed to it;",
     "dipende_da": [],
     "figura": {
      "mostra": [
       "luogo sotto il Sole",
       "luogo opposto"
      ],
      "evidenzia": [
       "innalzamento"
      ]
     }
    },
    {
     "id": "L3-P36-p6",
     "la": "",
     "it": "La somma delle forze sta alla forza di gravità come 1 sta a 12868200.",
     "en": "and the sum of these forces is to the force of gravity as 1 to 12868200.",
     "dipende_da": [],
     "figura": {
      "mostra": [],
      "evidenzia": [
       "38604600/3 = 12868200"
      ]
     }
    },
    {
     "id": "L3-P36-p7",
     "la": "",
     "it": "E poiché la stessa forza suscita lo stesso moto, sia che abbassi l'acqua nelle regioni che distano 90 gradi dal Sole, sia che la innalzi nelle regioni sotto il Sole e opposte al Sole, questa somma sarà la forza totale del Sole per agitare il mare; e avrà lo stesso effetto che se innalzasse tutta quanta il mare nelle regioni sotto il Sole e opposte al Sole, e nelle regioni che distano 90 gradi dal Sole non agisse affatto.",
     "en": "And because the same force excites the same motion, whether it depresses the waters in those places which are 90 degrees distant from the sun, or raises them in the places which are directly under and directly opposed to the sun, the aforesaid sum will be the total force of the sun to disturb the sea, and will have the same effect as if the whole was employed in raising the sea in the places directly under and directly opposed to the sun, and did not act at all in the places which are 90 degrees removed from the sun.",
     "dipende_da": [],
     "figura": {
      "mostra": [],
      "evidenzia": [
       "forza totale = somma"
      ]
     }
    },
    {
     "id": "L3-P36-p8",
     "la": "",
     "it": "Questa è la forza del Sole per suscitare il mare in un luogo qualsiasi dato, quando il Sole si trova insieme allo zenit del luogo e alla sua distanza media dalla Terra.",
     "en": "And this is the force of the sun to disturb the sea in any given place, where the sun is at the same time both vertical, and in its mean distance from the earth.",
     "dipende_da": [],
     "figura": {
      "mostra": [],
      "evidenzia": []
     }
    },
    {
     "id": "L3-P36-p9",
     "la": "",
     "it": "Nelle altre posizioni del Sole la forza per sollevare il mare è come il seno verso del doppio dell'altezza del Sole sopra l'orizzonte del luogo, direttamente, e come il cubo della distanza del Sole dalla Terra, inversamente.",
     "en": "In other positions of the sun, its force to raise the sea is as the versed sine of double its altitude above the horizon of the place directly, and the cube of the distance from the earth reciprocally.",
     "dipende_da": [],
     "figura": {
      "mostra": [
       "altezza h del Sole"
      ],
      "evidenzia": [
       "forza ∝ (1 − cos 2h)/d³"
      ]
     }
    }
   ],
   "dati": {
    "ML_su_gravita": "1 : 638092,6",
    "alla_superficie": "1 : 38604600",
    "somma": "1 : 12868200",
    "ricalcolo": [
     38604602.3,
     12868200.8
    ],
    "esito": "torna (nota N9)"
   }
  },
  {
   "id": "L3-P36-Cor",
   "tipo": "Corollarium",
   "titolo": "Prop. XXXVI, Cor. — l'altezza della marea solare (1 piede 11 1/30 pollici)",
   "copertura": [
    "III.G6.26"
   ],
   "fonti": {
    "la": "",
    "en": "Motte 1846, sezione corrispondente (Prop. XXXVI, Cor.)"
   },
   "passi": [
    {
     "id": "L3-P36-Cor-p1",
     "la": "",
     "it": "Poiché la forza centrifuga delle parti della Terra, che nasce dal moto diurno della Terra e sta alla forza di gravità come 1 sta a 289, fa sì che l'altezza dell'acqua sotto l'equatore superi la sua altezza sotto i poli della misura di 85472 piedi parigini, come sopra nella Prop. XIX, la forza solare di cui abbiamo trattato, poiché sta alla forza di gravità come 1 sta a 12868200, e perciò a quella forza centrifuga come 289 sta a 12868200, ossia come 1 sta a 44527, farà sì che l'altezza dell'acqua nelle regioni sotto il Sole e opposte al Sole superi la sua altezza nei luoghi che distano 90 gradi dal Sole della misura di appena un piede parigino e undici pollici e un trentesimo di pollice.",
     "en": "Since the centrifugal force of the parts of the earth, arising from the earth's diurnal motion, which is to the force of gravity as 1 to 289, raises the waters under the equator to a height exceeding that under the poles by 85472 Paris feet, as above, in Prop. XIX., the force of the sun, which we have now shewed to be to the force of gravity as 1 to 12868200, and therefore is to that centrifugal force as 289 to 12868200, or as 1 to 44527, will be able to raise the waters in the places directly under and directly opposed to the sun to a height exceeding that in the places which are 90 degrees removed from the sun only by one Paris foot and inches;",
     "dipende_da": [
      "Prop. XIX"
     ],
     "figura": {
      "mostra": [],
      "evidenzia": [
       "12868200/289 = 44527",
       "85472/44527 = 1,9196 piedi = 1 piede 11 1/30 pollici"
      ]
     },
     "nota": "Motte rende «11 1/30 pollici» con SVG 1079, che si legge 113 1/30: errore dell'edizione 1846 (§ A.8)."
    },
    {
     "id": "L3-P36-Cor-p2",
     "la": "",
     "it": "Questa misura sta infatti alla misura di 85472 piedi come 1 sta a 44527.",
     "en": "for this measure is to the measure of 85472 feet as 1 to 44527.",
     "dipende_da": [],
     "figura": {
      "mostra": [],
      "evidenzia": []
     }
    }
   ],
   "dati": {
    "rapporto": 44527,
    "ricalcolo_rapporto": 44526.6,
    "altezza_piedi": 1.91955,
    "esito": "torna"
   }
  },
  {
   "id": "L3-P37",
   "tipo": "Propositio/Problema",
   "titolo": "Prop. XXXVII — la forza della Luna sul mare (S : L = 1 : 4,4815)",
   "copertura": [
    "III.G6.27",
    "III.G6.28",
    "III.G6.29",
    "III.G6.30",
    "III.G6.31",
    "III.G6.32"
   ],
   "fonti": {
    "la": "",
    "en": "Motte 1846, sezione corrispondente (Prop. XXXVII)"
   },
   "enunciato": {
    "la": "",
    "it": "Trovare la forza della Luna per muovere il mare.",
    "en": "To find the force of the moon to move the sea."
   },
   "passi": [
    {
     "id": "L3-P37-p1",
     "la": "",
     "it": "La forza della Luna per muovere il mare si deve ricavare dalla sua proporzione alla forza del Sole, e questa proporzione si deve ricavare dalla proporzione dei moti del mare che nascono da queste forze.",
     "en": "The force of the moon to move the sea is to be deduced from its proportion to the force of the sun, and this proportion is to be collected from the proportion of the motions of the sea, which are the effects of those forces.",
     "dipende_da": [],
     "figura": {
      "mostra": [],
      "evidenzia": []
     }
    },
    {
     "id": "L3-P37-p2",
     "la": "",
     "it": "Davanti alla foce del fiume Avon, alla terza pietra miliare sotto Bristol, in primavera e in autunno la salita totale dell'acqua nella congiunzione e nell'opposizione dei luminari, secondo le osservazioni di Samuel Sturmy, è di circa 45 piedi, nelle quadrature invece di appena 25 piedi.",
     "en": "Before the mouth of the river Avon, three miles below Bristol, the height of the ascent of the water in the vernal and autumnal syzygies of the luminaries (by the observations of Samuel Sturmy) amounts to about 45 feet, but in the quadratures to 25 only.",
     "dipende_da": [],
     "figura": {
      "mostra": [],
      "evidenzia": [
       "Bristol: 45 e 25 piedi"
      ]
     }
    },
    {
     "id": "L3-P37-p3",
     "la": "",
     "it": "La prima altezza nasce dalla somma delle forze, la seconda dalla loro differenza.",
     "en": "The former of those heights arises from the sum of the aforesaid forces, the latter from their difference.",
     "dipende_da": [],
     "figura": {
      "mostra": [],
      "evidenzia": [
       "altezze ∝ L + S, L − S"
      ]
     }
    },
    {
     "id": "L3-P37-p4",
     "la": "",
     "it": "Siano dunque S e L le forze del Sole e della Luna quando si trovano nell'equatore e a distanza media dalla Terra: L + S starà a L − S come 45 sta a 25, ossia come 9 sta a 5.",
     "en": "If, therefore, S and L are supposed to represent respectively the forces of the sun and moon while they are in the equator, as well as in their mean distances from the earth, we shall have L + S to L - S as 45 to 25, or as 9 to 5.",
     "dipende_da": [],
     "figura": {
      "mostra": [],
      "evidenzia": [
       "(L + S) : (L − S) = 9 : 5"
      ]
     }
    },
    {
     "id": "L3-P37-p5",
     "la": "",
     "it": "Nel porto di Plymouth la marea, secondo le osservazioni di Samuel Colepress, si innalza in altezza media a circa sedici piedi, e in primavera e in autunno l'altezza della marea nelle sizigie può superare la sua altezza nelle quadrature di sette o otto piedi.",
     "en": "At Plymouth (by the observations of Samuel Colepress) the tide in its mean height rises to about 16 feet, and in the spring and autumn the height thereof in the syzygies may exceed that in the quadratures by more than 7 or 8 feet.",
     "dipende_da": [],
     "figura": {
      "mostra": [],
      "evidenzia": [
       "Plymouth: media 16 piedi"
      ]
     },
     "nota": "Motte aggiunge «more than»."
    },
    {
     "id": "L3-P37-p6",
     "la": "",
     "it": "Se la differenza massima di queste altezze è di nove piedi, L + S starà a L − S come 20½ sta a 11½, ossia come 41 sta a 23.",
     "en": "Suppose the greatest difference of those heights to be 9 feet, and L + S will be to L - S as to , or as 41 to 23;",
     "dipende_da": [],
     "figura": {
      "mostra": [],
      "evidenzia": [
       "20½ : 11½ = 41 : 23"
      ]
     },
     "nota": "Motte: SVG 1080 e 1081 (20½, 11½), corretti."
    },
    {
     "id": "L3-P37-p7",
     "la": "",
     "it": "Questa proporzione concorda abbastanza con la prima.",
     "en": "a proportion that agrees well enough with the former.",
     "dipende_da": [],
     "figura": {
      "mostra": [],
      "evidenzia": []
     }
    },
    {
     "id": "L3-P37-p8",
     "la": "",
     "it": "Per la grandezza della marea nel porto di Bristol, sembra che ci si debba fidare di più delle osservazioni di Sturmy; e perciò, finché non si sarà stabilito qualcosa di più certo, useremo la proporzione di 9 a 5.",
     "en": "But because of the great tide at Bristol, we are rather to depend upon the observations of Sturmy; and, therefore, till we procure something that is more certain, we shall use the proportion of 9 to 5.",
     "dipende_da": [],
     "figura": {
      "mostra": [],
      "evidenzia": []
     },
     "nota": "La trascrizione ha «Bistoliæ» (refuso probabile per Bristoliæ)."
    },
    {
     "id": "L3-P37-p9",
     "la": "",
     "it": "Del resto, a causa dei moti alterni delle acque, le maree massime non cadono nelle sizigie stesse dei luminari, ma sono le terze dopo le sizigie, come si è detto, ossia seguono da vicino il terzo passaggio della Luna al meridiano del luogo dopo le sizigie; o piuttosto (come nota Sturmy) sono le terze dopo il giorno del novilunio o del plenilunio, ossia dopo circa la dodicesima ora dal novilunio o dal plenilunio, e perciò cadono circa nella quarantatreesima ora dal novilunio o dal plenilunio.",
     "en": "But because of the reciprocal motions of the waters, the greatest tides do not happen at the times of the syzygies of the luminaries, but, as we have said before, are the third in order after the syzygies; or (reckoning from the syzygies) follow next after the third appulse of the moon to the meridian of the place after the syzygies; or rather (as Sturmy observes) are the third after the day of the new or full moon, or rather nearly after the twelfth hour from the new or full moon, and therefore fall nearly upon the forty-third hour after the new or full of the moon.",
     "dipende_da": [
      "Prop. XXIV"
     ],
     "figura": {
      "mostra": [],
      "evidenzia": [
       "ritardo della marea massima"
      ]
     },
     "nota": "«ut dictum fuit» rimanda alla Prop. XXIV (maree massime «tertii a syzygiis»)."
    },
    {
     "id": "L3-P37-p10",
     "la": "",
     "it": "In questo porto cadono poi circa nella settima ora dal passaggio della Luna al meridiano del luogo; e perciò seguono da vicino il passaggio della Luna al meridiano quando la Luna dista dal Sole, o dall'opposizione del Sole, di circa diciotto o diciannove gradi in conseguenza.",
     "en": "But in this port they fall out about the seventh hour after the appulse of the moon to the meridian of the place; and therefore follow next after the appulse of the moon to the meridian, when the moon is distant from the sun, or from opposition with the sun by about 18 or 19 degrees in consequentia.",
     "dipende_da": [],
     "figura": {
      "mostra": [],
      "evidenzia": [
       "18–19° dalla sizigia"
      ]
     }
    },
    {
     "id": "L3-P37-p11",
     "la": "",
     "it": "L'estate e l'inverno raggiungono il loro culmine non nei solstizi stessi, ma quando il Sole dista dai solstizi circa un decimo dell'intero giro, ossia circa 36 o 37 gradi.",
     "en": "So the summer and winter seasons come not to their height in the solstices themselves, but when the sun is advanced beyond the solstices by about a tenth part of its whole course, that is, by about 36 or 37 degrees.",
     "dipende_da": [],
     "figura": {
      "mostra": [],
      "evidenzia": [
       "analogia del ritardo stagionale"
      ]
     }
    },
    {
     "id": "L3-P37-p12",
     "la": "",
     "it": "E similmente la marea massima nasce dal passaggio della Luna al meridiano del luogo quando la Luna dista dal Sole circa un decimo dell'intero moto da una marea all'altra.",
     "en": "In like manner, the greatest tide is raised after the appulse of the moon to the meridian of the place, when the moon has passed by the sun, or the opposition thereof, by about a tenth part of the whole motion from one greatest tide to the next following greatest tide.",
     "dipende_da": [],
     "figura": {
      "mostra": [],
      "evidenzia": []
     }
    },
    {
     "id": "L3-P37-p13",
     "la": "",
     "it": "Sia quella distanza di circa 18½ gradi.",
     "en": "Suppose that distance about degrees;",
     "dipende_da": [],
     "figura": {
      "mostra": [],
      "evidenzia": [
       "θ = 18½°"
      ]
     },
     "nota": "Motte: SVG 641 (18½), corretto."
    },
    {
     "id": "L3-P37-p14",
     "la": "",
     "it": "E la forza del Sole, a questa distanza della Luna dalle sizigie e dalle quadrature, sarà minore, per accrescere e per diminuire il moto del mare che nasce dalla forza della Luna, che nelle sizigie e nelle quadrature stesse, nel rapporto del raggio al seno del complemento del doppio di questa distanza, ossia di un angolo di 37 gradi, cioè nel rapporto di 10000000 a 7986355.",
     "en": "and the sun's force in this distance of the moon from the syzygies and quadratures will be of less moment to augment and diminish that part of the motion of the sea which proceeds from the motion of the moon than in the syzygies and quadratures themselves in the proportion of the radius to the co-sine of double this distance, or of an angle of 37 degrees; that is in proportion of 10000000 to 7986355;",
     "dipende_da": [],
     "figura": {
      "mostra": [],
      "evidenzia": [
       "cos 37° = 0,7986355"
      ]
     }
    },
    {
     "id": "L3-P37-p15",
     "la": "",
     "it": "E perciò nella proporzione precedente al posto di S si deve scrivere 0,7986355 S.",
     "en": "and, therefore, in the preceding analogy, in place of S we must put 0,7986355S.",
     "dipende_da": [],
     "figura": {
      "mostra": [],
      "evidenzia": []
     }
    },
    {
     "id": "L3-P37-p16",
     "la": "",
     "it": "Ma anche la forza della Luna nelle quadrature deve essere diminuita, a causa della declinazione della Luna dall'equatore.",
     "en": "But farther; the force of the moon in the quadratures must be diminished, on account of its declination from the equator;",
     "dipende_da": [],
     "figura": {
      "mostra": [],
      "evidenzia": []
     }
    },
    {
     "id": "L3-P37-p17",
     "la": "",
     "it": "Infatti la Luna nelle quadrature, o piuttosto a 18½ gradi dopo le quadrature, si trova a una declinazione di circa 22° 13′.",
     "en": "for the moon in those quadratures, or rather in degrees past the quadratures, declines from the equator by about 23° 13';",
     "dipende_da": [],
     "figura": {
      "mostra": [],
      "evidenzia": [
       "declinazione 22° 13′"
      ]
     },
     "nota": "Motte ha 23° 13′: errore (cos² 22° 13′ = 0,8570328; nota N10)."
    },
    {
     "id": "L3-P37-p18",
     "la": "",
     "it": "E la forza di un luminare che declina dall'equatore per muovere il mare diminuisce, con ottima approssimazione, nel rapporto duplicato del seno del complemento della declinazione.",
     "en": "and the force of either luminary to move the sea is diminished as it declines from the equator nearly in the duplicate proportion of the co-sine of the declination;",
     "dipende_da": [],
     "figura": {
      "mostra": [],
      "evidenzia": [
       "fattore cos² δ"
      ]
     }
    },
    {
     "id": "L3-P37-p19",
     "la": "",
     "it": "E perciò la forza della Luna in queste quadrature è soltanto 0,8570327 L.",
     "en": "and therefore the force of the moon in those quadratures is only 0,8570327L;",
     "dipende_da": [],
     "figura": {
      "mostra": [],
      "evidenzia": [
       "cos² 22° 13′ = 0,8570327"
      ]
     }
    },
    {
     "id": "L3-P37-p20",
     "la": "",
     "it": "Dunque L + 0,7986355 S sta a 0,8570327 L − 0,7986355 S come 9 sta a 5.",
     "en": "whence we have L + 0,7986355S to 0,8570327L - 0,7986355S as 9 to 5.",
     "dipende_da": [],
     "figura": {
      "mostra": [],
      "evidenzia": [
       "(L + 0,7986 S) : (0,8570 L − 0,7986 S) = 9 : 5"
      ]
     }
    },
    {
     "id": "L3-P37-p21",
     "la": "",
     "it": "Inoltre i diametri dell'orbita nella quale la Luna dovrebbe muoversi senza eccentricità stanno fra loro come 69 sta a 70; e perciò la distanza della Luna dalla Terra nelle sizigie sta alla sua distanza nelle quadrature come 69 sta a 70, a parità delle altre condizioni.",
     "en": "Farther yet; the diameters of the orbit in which the moon should move, setting aside the consideration of eccentricity, are one to the other as 69 to 70; and therefore the moon's distance from the earth in the syzygies is to its distance in the quadratures, cæteris paribus, as 69 to 70;",
     "dipende_da": [],
     "figura": {
      "mostra": [],
      "evidenzia": [
       "ellisse 69 : 70 della Prop. XXVIII"
      ]
     },
     "nota": "I 69 : 70 vengono dalla Prop. XXVIII, non citata qui per numero."
    },
    {
     "id": "L3-P37-p22",
     "la": "",
     "it": "E le sue distanze a 18½ gradi dalle sizigie, dove si genera la marea massima, e a 18½ gradi dalle quadrature, dove si genera la marea minima, stanno alla sua distanza media come 69,098747 e 69,897345 stanno a 69½.",
     "en": "and its distances, when degrees advanced beyond the syzygies, where the greatest tide was excited, and when degrees passed by the quadratures, where the least tide was produced, are to its mean distance as 69,098747 and 69,897345 to",
     "dipende_da": [],
     "figura": {
      "mostra": [],
      "evidenzia": [
       "r(18½°) = 69,098747; r(108½°) = 69,897345 (ellisse di semiassi 69, 70)"
      ]
     },
     "nota": "Motte: SVG 1082 (69½), corretto."
    },
    {
     "id": "L3-P37-p23",
     "la": "",
     "it": "Le forze della Luna per muovere il mare sono poi nel rapporto triplicato inverso delle distanze, e perciò le forze alla massima e alla minima di queste distanze stanno alla forza alla distanza media come 0,9830427 e 1,017522 stanno a 1.",
     "en": "But the force of the moon to move the sea is in the reciprocal triplicate proportion of its distance; and therefore its forces, in the greatest and least of those distances, are to its force in its mean distance as 0,9830427 and 1,017522 to 1.",
     "dipende_da": [],
     "figura": {
      "mostra": [],
      "evidenzia": [
       "(69,5/r)³"
      ]
     }
    },
    {
     "id": "L3-P37-p24",
     "la": "",
     "it": "Di qui risulta che 1,017522 L + 0,7986355 S sta a 0,9830427 × 0,8570327 L − 0,7986355 S come 9 sta a 5; e S sta a L come 1 sta a 4,4815.",
     "en": "From whence we have 1,017522L × 0,7986355S to 0,9830427 × 0,8570327L - 0,7986355S as 9 to 5; and S to L as 1 to 4,4815.",
     "dipende_da": [],
     "figura": {
      "mostra": [],
      "evidenzia": [
       "L/S = 14·0,7986355/(9·0,9830427·0,8570327 − 5·1,017522) = 4,4815"
      ]
     },
     "nota": "Motte scrive «1,017522L × 0,7986355S»: il segno × è un errore per +."
    },
    {
     "id": "L3-P37-p25",
     "la": "",
     "it": "Perciò, poiché la forza del Sole sta alla forza di gravità come 1 sta a 12868200, la forza della Luna starà alla forza di gravità come 1 sta a 2871400.",
     "en": "Wherefore since the force of the sun is to the force of gravity as 1 to 12868200, the moon's force will be to the force of gravity as 1 to 2871400.",
     "dipende_da": [],
     "figura": {
      "mostra": [],
      "evidenzia": [
       "12868200/4,4815 = 2871400"
      ]
     }
    }
   ],
   "nota": "Proposizione senza figura: i passi sono un calcolo, e figura.mostra è vuoto; le relazioni da mostrare sono in figura.evidenzia.",
   "dati": {
    "Bristol": [
     45,
     25
    ],
    "Plymouth": {
     "media": 16,
     "differenza": 9,
     "rapporto": "41 : 23"
    },
    "cos37": 0.79863551,
    "cos2_22_13": 0.85703276,
    "distanze_ellisse": [
     69.0987466,
     69.8973447
    ],
    "fattori_forza": [
     1.0175222,
     0.9830427
    ],
    "L_su_S_ricalcolo": 4.481523,
    "L_su_S_solo_Bristol": 3.5,
    "L_su_S_senza_distanze": 4.1208,
    "Luna_su_gravita_ricalcolo": 2871405,
    "esito": "torna (nota N10)"
   }
  },
  {
   "id": "L3-P37-Cor3",
   "tipo": "Corollarium",
   "titolo": "Prop. XXXVII, Cor. 3 — la densità della Luna (11 : 9 rispetto alla Terra)",
   "copertura": [
    "III.G6.35"
   ],
   "fonti": {
    "la": "",
    "en": "Motte 1846, sezione corrispondente (Prop. XXXVII, Cor. 3)"
   },
   "passi": [
    {
     "id": "L3-P37-Cor3-p1",
     "la": "",
     "it": "Poiché la forza della Luna per muovere il mare sta alla forza analoga del Sole come 4,4815 sta a 1, e quelle forze (per il Cor. 14 della Prop. LXVI del Libro I) sono come le densità dei corpi della Luna e del Sole e i cubi dei diametri apparenti considerati congiuntamente, la densità della Luna starà alla densità del Sole come 4,4815 sta a 1, direttamente, e come il cubo del diametro della Luna sta al cubo del diametro del Sole, inversamente; cioè (poiché i diametri apparenti medi della Luna e del Sole sono di 31′ 16½″ e 32′ 12″) come 4891 sta a 1000.",
     "en": "Because the force of the moon to move the sea is to the like force of the sun as 4,4815 to 1, and those forces (by Cor. 14, Prop. LXVI, Book I) are as the densities of the bodies of the sun and moon and the cubes of their apparent diameters conjunctly, the density of the moon will be to the density of the sun as 4,4815 to 1 directly, and the cube of the moon's diameter to the cube of the sun's diameter inversely; that is (seeing the mean apparent diameters of the moon and sun are 31' , and 32' 12''), as 4891 to 1000.",
     "dipende_da": [
      "Libro I, Prop. LXVI, Cor. 14"
     ],
     "figura": {
      "mostra": [],
      "evidenzia": [
       "4,4815 × (32′ 12″ / 31′ 16½″)³ = 4,891"
      ]
     },
     "nota": "Il Cor. 14 dà il cubo del diametro apparente per corpi di uguale densità; il fattore della densità è un'estensione (§ A.7). Motte: SVG 1086 (16½″), corretto."
    },
    {
     "id": "L3-P37-Cor3-p2",
     "la": "",
     "it": "Ma la densità del Sole stava alla densità della Terra come 1000 sta a 4000; e perciò la densità della Luna sta alla densità della Terra come 4891 sta a 4000, ossia come 11 sta a 9.",
     "en": "But the density of the sun was to the density of the earth as 1000 to 4000; and therefore the density of the moon is to the density of the earth as 4891 to 4000, or as 11 to 9.",
     "dipende_da": [],
     "figura": {
      "mostra": [],
      "evidenzia": [
       "4891/4000 = 1,2228 ≈ 11/9"
      ]
     },
     "nota": "«erat» rimanda alla Prop. VIII, Cor. 3 (densità 100 e 400), non citata per numero."
    },
    {
     "id": "L3-P37-Cor3-p3",
     "la": "",
     "it": "Il corpo della Luna è dunque più denso e più terroso della nostra Terra.",
     "en": "Therefore the body of the moon is more dense and more earthly than the earth itself.",
     "dipende_da": [],
     "figura": {
      "mostra": [],
      "evidenzia": []
     }
    }
   ],
   "dati": {
    "densita_L_S_ricalcolo": 4.891,
    "densita_L_T": 1.22275,
    "11_su_9": 1.22222,
    "esito": "torna (nota N11)"
   }
  },
  {
   "id": "L3-P37-Cor7",
   "tipo": "Corollarium",
   "titolo": "Prop. XXXVII, Cor. 7 — dalla caduta della Luna alla caduta dei gravi a Parigi",
   "copertura": [
    "III.G6.39"
   ],
   "fonti": {
    "la": "",
    "en": "Motte 1846, sezione corrispondente (Prop. XXXVII, Cor. 7)"
   },
   "passi": [
    {
     "id": "L3-P37-Cor7-p1",
     "la": "",
     "it": "E la distanza media del centro della Luna dal centro della Terra, negli ottanti della Luna, sarà di 60⅖ semidiametri massimi della Terra, con ottima approssimazione.",
     "en": "And the mean distance of the centre of the moon from the centre of the earth will be (in the moon's octants) nearly of the greatest semi-diameters of the earth;",
     "dipende_da": [],
     "figura": {
      "mostra": [],
      "evidenzia": [
       "60⅖"
      ]
     },
     "nota": "Motte: SVG 966 (60⅖), corretto."
    },
    {
     "id": "L3-P37-Cor7-p2",
     "la": "",
     "it": "Infatti il semidiametro massimo della Terra era di 19658600 piedi parigini, e la distanza media dei centri della Terra e della Luna, composta di 60⅖ semidiametri di questo genere, è uguale a 1187379440 piedi.",
     "en": "for the greatest semi-diameter of the earth was 19658600 Paris feet, and the mean distance of the centres of the earth and moon, consisting of 60 such semi-diameters, is equal to 1187379440 feet.",
     "dipende_da": [],
     "figura": {
      "mostra": [],
      "evidenzia": [
       "19658600 × 60⅖ = 1187379440"
      ]
     },
     "nota": "«suit» è refuso della trascrizione per «fuit»; il valore viene dalla Prop. XIX, non citata qui per numero."
    },
    {
     "id": "L3-P37-Cor7-p3",
     "la": "",
     "it": "E questa distanza (per il corollario precedente) sta alla distanza del centro della Luna dal centro comune di gravità della Terra e della Luna come 40,788 sta a 39,788; e perciò la seconda distanza è di 1158268534 piedi.",
     "en": "And this distance (by the preceding Cor.) is to the distance of the moon's centre from the common centre of gravity of the earth and moon as 40,788 to 39,788; which latter distance, therefore, is 1158268534 feet.",
     "dipende_da": [
      "Prop. XXXVII, Cor. 6"
     ],
     "figura": {
      "mostra": [],
      "evidenzia": [
       "ricalcolo 1158268441 (scarto trascurabile)"
      ]
     }
    },
    {
     "id": "L3-P37-Cor7-p4",
     "la": "",
     "it": "E poiché la Luna compie la sua rivoluzione, rispetto alle stelle fisse, in 27 giorni, 7 ore e 43 4/9 minuti, il seno verso dell'angolo che la Luna descrive nel tempo di un minuto è 12752341, essendo il raggio 1000,000000,000000.",
     "en": "And since the moon, in respect of the fixed stars, performs its revolution in 27d. 7h. , the versed sine of that angle which the moon in a minute of time describes is 12752341 to the radius 1000,000000,000000;",
     "dipende_da": [],
     "figura": {
      "mostra": [],
      "evidenzia": [
       "seno verso ricalcolato 12752196: non torna alla quinta cifra"
      ]
     },
     "nota": "Motte: SVG 1087 (43 4/9′), corretto."
    },
    {
     "id": "L3-P37-Cor7-p5",
     "la": "",
     "it": "E come il raggio sta a questo seno verso, così 1158268534 piedi stanno a 14,7706353 piedi.",
     "en": "and as the radius is to this versed sine, so are 1158268534 feet to 14,7706353 feet.",
     "dipende_da": [],
     "figura": {
      "mostra": [],
      "evidenzia": [
       "1158268534 × 12752341·10⁻¹⁵ = 14,7706353"
      ]
     }
    },
    {
     "id": "L3-P37-Cor7-p6",
     "la": "",
     "it": "La Luna dunque, cadendo verso la Terra per quella forza con cui è trattenuta nell'orbita, nel tempo di un minuto descriverà 14,7706353 piedi.",
     "en": "The moon, therefore, falling towards the earth by that force which retains it in its orbit, would in one minute of time describe 14,7706353 feet;",
     "dipende_da": [],
     "figura": {
      "mostra": [],
      "evidenzia": []
     }
    },
    {
     "id": "L3-P37-Cor7-p7",
     "la": "",
     "it": "E aumentando questa forza nel rapporto di 178 29/40 a 177 29/40, si avrà la forza totale della gravità nell'orbita della Luna, per il Cor. della Prop. III.",
     "en": "and if we augment this force in the proportion of to , we shall have the total force of gravity at the orbit of the moon, by Cor. Prop. III;",
     "dipende_da": [
      "Prop. III, Cor."
     ],
     "figura": {
      "mostra": [],
      "evidenzia": [
       "× 178,725/177,725"
      ]
     },
     "nota": "Motte: SVG 963, 964, corretti."
    },
    {
     "id": "L3-P37-Cor7-p8",
     "la": "",
     "it": "E per questa forza la Luna, cadendo, nel tempo di un minuto descriverà 14,8538067 piedi.",
     "en": "and the moon falling by this force, in one minute of time would describe 14,8538067 feet.",
     "dipende_da": [],
     "figura": {
      "mostra": [],
      "evidenzia": [
       "ricalcolo 14,8537448"
      ]
     }
    },
    {
     "id": "L3-P37-Cor7-p9",
     "la": "",
     "it": "E alla sessantesima parte della distanza della Luna dal centro della Terra, cioè alla distanza di 197896573 piedi dal centro della Terra, un corpo grave, cadendo nel tempo di un secondo, descriverà anch'esso 14,8538067 piedi.",
     "en": "And at the 60th part of the distance of the moon from the earth's centre, that is, at the distance of 197896573 feet from the centre of the earth, a body falling by its weight, would, in one second of time, likewise describe 14,8538067 feet.",
     "dipende_da": [],
     "figura": {
      "mostra": [],
      "evidenzia": [
       "1187379440/60 = 19789657,3"
      ]
     },
     "nota": "197896573 va letto 19789657,3 (virgola decimale mancante, anche in Motte)."
    },
    {
     "id": "L3-P37-Cor7-p10",
     "la": "",
     "it": "E perciò alla distanza di 19615800 piedi, che costituiscono il semidiametro medio della Terra, un grave cadendo descriverà 15,11175 piedi, ossia 15 piedi, 1 pollice e 4 1/11 linee.",
     "en": "And, therefore, at the distance of 19615800, which compose one mean semi-diameter of the earth, a heavy body would describe in falling 15,11175, or 15 feet, 1 inch, and lines, in the same time.",
     "dipende_da": [],
     "figura": {
      "mostra": [],
      "evidenzia": [
       "14,8538067 × (19789657,3/19615800)² = 15,1183, non 15,11175"
      ]
     },
     "nota": "Motte rende 4 1/11 con SVG 1088, che si legge 4 4/11: errore dell'edizione 1846. Il valore 15,11175 non torna con il ricalcolo (nota N12)."
    },
    {
     "id": "L3-P37-Cor7-p11",
     "la": "",
     "it": "Questa sarà la caduta dei corpi alla latitudine di 45 gradi.",
     "en": "This will be the descent of bodies in the latitude of 45 degrees.",
     "dipende_da": [],
     "figura": {
      "mostra": [],
      "evidenzia": []
     }
    },
    {
     "id": "L3-P37-Cor7-p12",
     "la": "",
     "it": "E per la tabella precedente, descritta nella Prop. XX, la caduta sarà un poco maggiore alla latitudine di Parigi, con un eccesso di circa 2/3 di linea.",
     "en": "And by the foregoing table, to be found under Prop. XX, the descent in the latitude of Paris will be a little greater by an excess of about parts of a line.",
     "dipende_da": [
      "Prop. XX"
     ],
     "figura": {
      "mostra": [],
      "evidenzia": [
       "eccesso ricalcolato 0,63 linee"
      ]
     },
     "nota": "Motte: SVG 226 (2/3), corretto."
    },
    {
     "id": "L3-P37-Cor7-p13",
     "la": "",
     "it": "Per questo calcolo, dunque, i gravi alla latitudine di Parigi, cadendo nel vuoto, descriveranno nel tempo di un secondo circa 15 piedi parigini, 1 pollice e 4 25/33 linee.",
     "en": "Therefore, by this computation, heavy bodies in the latitude of Paris falling in vacuo will describe 15 Paris feet, 1 inch, lines, very nearly, in one second of time.",
     "dipende_da": [],
     "figura": {
      "mostra": [],
      "evidenzia": [
       "4 1/11 + 2/3 = 4 25/33"
      ]
     },
     "nota": "Motte: SVG 1089 (4 25/33), corretto."
    },
    {
     "id": "L3-P37-Cor7-p14",
     "la": "",
     "it": "E se la gravità si diminuisce togliendo la forza centrifuga che nasce dal moto diurno della Terra a quella latitudine, i gravi lì, cadendo, descriveranno nel tempo di un secondo 15 piedi, 1 pollice e 1½ linee.",
     "en": "And if the gravity be diminished by taking away a quantity equal to the centrifugal force arising in that latitude from the earth's diurnal motion, heavy bodies falling there will describe in one second of time 15 feet, 1 inch, and line.",
     "dipende_da": [],
     "figura": {
      "mostra": [],
      "evidenzia": [
       "4,758 − 3,267 = 1,49 linee"
      ]
     },
     "nota": "Motte: SVG 208 (1½), corretto. «cetrifugam» è refuso della trascrizione."
    },
    {
     "id": "L3-P37-Cor7-p15",
     "la": "",
     "it": "E con questa velocità cadono i gravi alla latitudine di Parigi, come si è mostrato sopra nelle Propp. IV e XIX.",
     "en": "And with this velocity heavy bodies do really fall in the latitude of Paris, as we have shewn above in Prop. IV and XIX.",
     "dipende_da": [
      "Prop. IV",
      "Prop. XIX"
     ],
     "figura": {
      "mostra": [],
      "evidenzia": [
       "Prop. IV: 1 7/9 linee"
      ]
     }
    }
   ],
   "dati": {
    "distanza_piedi": 1187379440,
    "distanza_dal_baricentro_testo": 1158268534,
    "distanza_dal_baricentro_ricalcolo": 1158268441,
    "seno_verso_testo": 12752341,
    "seno_verso_ricalcolo": 12752196,
    "caduta_1min_testo": 14.7706353,
    "caduta_corretta_testo": 14.8538067,
    "caduta_corretta_ricalcolo": 14.8537448,
    "caduta_1s_superficie_testo": 15.11175,
    "caduta_1s_superficie_ricalcolo": 15.11828,
    "esito": "non tornano il seno verso (quinta cifra) e soprattutto 15,11175 (scarto 0,94 linee); il resto torna (nota N12)"
   }
  }
 ]
}
```

**Fine del Fascicolo 25a.**
