> **Copia pubblica.** In questa versione i campi `"la"` della Parte B sono vuoti: le frasi latine vengono dalla trascrizione del Newton Project, che non si ridistribuisce. Il latino del 1726 si legge su newtonproject.ox.ac.uk.

# Isaac Newton
# Principi matematici della filosofia naturale

## Fascicolo 13 — Libro II, Sezione I: il moto dei corpi resistiti in rapporto alla velocità

**Nuova traduzione italiana di lavoro dal latino del 1726, confrontata con l’inglese di Andrew Motte nell’edizione del 1846.**

Versione 0.1 — 8 novembre 2026. Preparata con Claude (Anthropic) per Massimo Bosetti.

### Stato e perimetro

Questo fascicolo apre il Libro II (*De motu corporum liber secundus*). Traduce integralmente la **Sezione I**, *De motu corporum quibus resistitur in ratione velocitatis*: le Proposizioni I–IV, il Lemma I, tutti i corollari (uno della Prop. I, uno della Prop. II, quattro della Prop. III, sette della Prop. IV) e lo Scolio che chiude la Sezione e introduce la Sezione II. È una traduzione di lavoro, non un’edizione critica validata.

Gli identificatori **II.S1.01–II.S1.27** e i titoli tematici tra parentesi sono aggiunte editoriali. Servono a orientare la lettura e a controllare la completezza. I numeri romani delle proposizioni, dei teoremi, dei problemi e del lemma, e i numeri dei corollari, appartengono al testo originale. Le integrazioni del curatore sono tra parentesi quadre. Le note poste dopo la traduzione non fanno parte del testo di Newton.

In coda al fascicolo c’è la **Parte B**, con i dati strutturati per le pagine interattive di 7 unità con figura o costruzione geometrica: il Cor. della Prop. II; la Prop. III; la Prop. IV e i suoi Cor. 1, 2, 3 e 7.

### Fonti effettivamente consultate

1. **Latino di riferimento.** Isaac Newton, *Philosophiæ Naturalis Principia Mathematica*, terza edizione, Londra, 1726, Libro II, Sezione I, **pp. 230–239** (marcatori ‹230›–‹239› della trascrizione; la Sezione comincia a p. 230 e lo Scolio sta a p. 239). Trascrizione normalizzata del Newton Project, documento **NATP00088**, estratta in testo semplice senza correzioni: `fonti/latino-1726-L2-S01.md`. Figure citate: [FIG 1]–[FIG 7] (NATP00088-1…7, non incluse).
2. **Inglese di confronto.** *Newton’s Principia*, traduzione di Andrew Motte, New York, Daniel Adee, 1846, Book II, Section I, **sezione corrispondente** (l’estratto `fonti/motte-1846-L2-S01.md` non contiene marcatori di pagina). Le formule stampate come immagini compaiono come `[SVG 352]`–`[SVG 371]`: le ho controllate tutte sul LaTeX estratto dall’EPUB (`src_epub/svg_tex.tsv`) e, per il caso dubbio (356), sull’immagine resa con `rsvg-convert` (vedi § A.9). Le righe `[FIG: …]` dell’estratto sono descrizioni delle figure aggiunte dall’edizione Project Gutenberg, non testo di Motte.
3. **Brief comune** del Libro I, **addendum del Libro II** (`ISTRUZIONI-TRADUTTORE.md`), **Fascicolo 3** (modello di formato, Leggi e Corollari) e **Fascicolo 5** (modello di un fascicolo di Sezione); **Fascicolo 4** per il controllo dei rimandi ai Lemmi VII e VIII del Libro I.

Non ho consultato né riprodotto traduzioni moderne. Non ho potuto vedere la stampa del 1726, la stampa di Motte del 1729 né le figure originali NATP00088-1…7: le relazioni geometriche sono ricostruite dalle sole lettere del testo e controllate con uno script numerico (note N3–N9).

### Criteri di traduzione

- Il testo guida è il latino; l’inglese di Motte serve a controllare le interpretazioni ed è annotato quando aggiunge, omette o si discosta.
- Si applica il **glossario comune** del brief e quello **aggiuntivo del Libro II**: *resistentia* «resistenza», *medium* «mezzo», *in ratione velocitatis* «in rapporto alla velocità», *in duplicata ratione velocitatis* «in rapporto duplicato della velocità», *vis insita* «forza insita», *spatium non resistens* «spazio non resistente», *medium uniforme / similare* «mezzo uniforme / omogeneo», *hyperbola* «iperbole», *asymptotos* «asintoto», *progressio geometrica* «progressione geometrica», *logarithmus* «logaritmo», *gravitas* «gravità», *experimentum* «esperimento», *Scholium* «Scolio»; dal Libro I *latus rectum* «lato retto», *vertex* «vertice», *diameter* «diametro», *ratio duplicata* «rapporto duplicato», *reciproce* «inversamente», *urgere* «sollecitare», *exponere* «rappresentare», Q.E.D. «C.V.D.», Q.E.I. «C.V.T.».
- Le estensioni del glossario proprie di questo fascicolo sono elencate e motivate nel § A.0 (fra queste *rigor* «rigidità», *convertendo* «convertendo», *divisim* «separando», *analogus* «analogo», *ad latus* «laterale»).
- Gli enunciati dei teoremi all’infinito sono resi con l’indicativo; gli enunciati dei problemi (*definire motum*) con l’infinito italiano, come nei fascicoli del Libro I (*trovare quel centro*).
- Le abbreviazioni e le frazioni appiattite della trascrizione sono scritte con apici Unicode e con la barra: «DR×QBN» → DR×QB/N, «DRq×CK×CP2DCq×QB» → DR²×CK×CP/(2DC²×QB), «12kq» → ½kq. Ogni lettura è dichiarata nell’apparato (§ A.8) e controllata sul calcolo (nota N7). Nessuna formula moderna entra nel testo tradotto.
- Le aree e i rettangoli sono indicati, come in Newton, con le lettere dei vertici (area ABqK, rettangolo BACH); le lettere minuscole e maiuscole sono conservate come nella trascrizione.

---

## Traduzione italiana

### Libro II. Il moto dei corpi

### Sezione I. Il moto dei corpi ai quali si resiste in rapporto alla velocità

### Proposizione I. Teorema I (quantità di moto perduta e spazio percorso)

**[II.S1.01]** **Se a un corpo si resiste in rapporto alla velocità, la quantità di moto perduta per effetto della resistenza è come lo spazio percorso nel moto.**

**[II.S1.02]** Infatti, poiché la quantità di moto perduta in ciascuna delle particelle di tempo uguali è come la velocità, cioè come la particella di cammino percorsa, la quantità di moto perduta nel tempo intero sarà, componendo, come il cammino intero. C.V.D.

**[II.S1.03]** *Cor.* Se dunque un corpo, privo di ogni gravità, si muove in spazi liberi per la sola forza insita, e sono dati sia la quantità di moto totale all’inizio sia la quantità di moto residua dopo che il corpo ha percorso un certo spazio, sarà dato lo spazio totale che il corpo può descrivere in un tempo infinito. Quello spazio, infatti, starà allo spazio già descritto come la quantità di moto totale all’inizio sta alla parte perduta di quella quantità di moto.

### Lemma I (quantità proporzionali alle proprie differenze)

**[II.S1.04]** **Le quantità proporzionali alle proprie differenze sono continuamente proporzionali.**

**[II.S1.05]** Stia A ad A − B come B sta a B − C e come C sta a C − D, ecc.; convertendo, risulterà che A sta a B come B sta a C e come C sta a D, ecc. C.V.D.

### Proposizione II. Teorema II (velocità in progressione geometrica)

**[II.S1.06]** **Se a un corpo si resiste in rapporto alla velocità, e questo si muove per la sola forza insita in un mezzo omogeneo, e si prendono tempi uguali, le velocità all’inizio dei singoli tempi sono in progressione geometrica, e gli spazi descritti nei singoli tempi sono come le velocità.**

**[II.S1.07]** *Caso 1.* Si divida il tempo in particelle uguali; e se proprio all’inizio delle particelle la forza della resistenza agisce con un impulso unico, che sia come la velocità, il decremento della velocità in ciascuna particella di tempo sarà come la velocità stessa. Le velocità sono dunque proporzionali alle proprie differenze, e perciò (per il Lemma I del Libro II) continuamente proporzionali. Di conseguenza, se da un numero uguale di particelle si compongono tempi uguali qualsiasi, le velocità proprio all’inizio di questi tempi saranno come i termini di una progressione continua presi a salti, tralasciando ogni volta un numero uguale di termini intermedi. I rapporti di questi termini, poi, si compongono dei rapporti, uguali fra loro, dei termini intermedi ripetuti un numero uguale di volte; e perciò anche questi rapporti composti sono uguali fra loro. Dunque le velocità, proporzionali a questi termini, sono in progressione geometrica. Si diminuiscano ora quelle particelle uguali di tempo e se ne aumenti il numero all’infinito, così che l’impulso della resistenza diventi continuo; e le velocità all’inizio dei tempi uguali, sempre continuamente proporzionali, saranno continuamente proporzionali anche in questo caso. C.V.D.

**[II.S1.08]** *Caso 2.* E, separando, le differenze delle velocità, cioè le loro parti perdute nei singoli tempi, sono come le velocità intere; gli spazi descritti nei singoli tempi, poi, sono come le parti perdute delle velocità (per la Prop. I del Libro II), e perciò anche come le velocità intere. C.V.D.

**[II.S1.09]** *Cor.* Di qui, se con gli asintoti ortogonali AC, CH si descrive l’iperbole BG, e AB, DG sono perpendicolari all’asintoto AC, e si rappresentano sia la velocità del corpo sia la resistenza del mezzo, proprio all’inizio del moto, con una linea data qualsiasi AC, e, trascorso un certo tempo, con la linea indefinita DC, il tempo può essere rappresentato dall’area ABGD e lo spazio descritto in quel tempo dalla linea AD. Infatti, se quell’area, per il moto del punto D, cresce uniformemente al modo del tempo, la retta DC decrescerà in rapporto geometrico al modo della velocità, e le parti della retta AC descritte in tempi uguali decresceranno nello stesso rapporto.

### Proposizione III. Problema I (salita e discesa verticale con gravità uniforme)

**[II.S1.10]** **Definire il moto di un corpo al quale, mentre sale o scende in linea retta in un mezzo omogeneo, si resiste in rapporto alla velocità, e che è sollecitato da una gravità uniforme.**

**[II.S1.11]** Mentre il corpo sale, si rappresenti la gravità con un rettangolo dato qualsiasi BACH, e la resistenza del mezzo all’inizio della salita con il rettangolo BADE, preso dalla parte opposta della retta AB. Con gli asintoti ortogonali AC, CH si descriva per il punto B un’iperbole che tagli le perpendicolari DE, de in G, g: salendo, il corpo nel tempo DGgd descriverà lo spazio EGge; nel tempo DGBA lo spazio dell’intera salita EGB; nel tempo ABKI lo spazio di discesa BFK; e nel tempo IKki lo spazio di discesa KFfk; e le velocità del corpo (proporzionali alla resistenza del mezzo) negli estremi di questi tempi saranno rispettivamente ABED, ABed, nulla, ABFI, ABfi; e la velocità massima che il corpo può acquistare scendendo sarà BACH.

**[II.S1.12]** Si scomponga infatti il rettangolo BACH in innumerevoli rettangoli Ak, Kl, Lm, Mn, ecc., che siano come gli incrementi delle velocità prodotti in altrettanti tempi uguali; nulla, Ak, Al, Am, An, ecc. saranno come le velocità intere, e perciò (per ipotesi) come la resistenza del mezzo all’inizio di ciascuno dei tempi uguali. Si faccia in modo che AC stia ad AK, ossia ABHC ad ABkK, come la forza di gravità sta alla resistenza all’inizio del secondo tempo; e dalla forza di gravità si sottraggano le resistenze: ABHC, KkHC, LlHC, MmHC, ecc. resteranno come le forze assolute dalle quali il corpo è sollecitato all’inizio dei singoli tempi, e perciò (per la Legge II del moto) come gli incrementi delle velocità, cioè come i rettangoli Ak, Kl, Lm, Mn, ecc.; e quindi (per il Lemma I del Libro II) in progressione geometrica. Perciò, se le rette Kk, Ll, Mm, Nn, ecc., prolungate, incontrano l’iperbole in q, r, s, t, ecc., le aree ABqK, KqrL, LrsM, MstN, ecc. saranno uguali, e perciò analoghe sia ai tempi sia alle forze di gravità, sempre uguali. Ora l’area ABqK (per il Cor. 3 del Lemma VII e per il Lemma VIII del Libro I) sta all’area Bkq come Kq sta a ½kq, ossia come AC sta a ½AK, cioè come la forza di gravità sta alla resistenza nel mezzo del primo tempo. E con un argomento simile le aree qKLr, rLMs, sMNt, ecc. stanno alle aree qklr, rlms, smnt, ecc. come le forze di gravità stanno alle resistenze nel mezzo del secondo, del terzo, del quarto tempo, ecc. Di conseguenza, poiché le aree uguali BAKq, qKLr, rLMs, sMNt, ecc. sono analoghe alle forze di gravità, le aree Bkq, qklr, rlms, smnt, ecc. saranno analoghe alle resistenze nel mezzo dei singoli tempi, cioè (per ipotesi) alle velocità, e perciò agli spazi descritti. Si prendano le somme delle quantità analoghe: le aree Bkq, Blr, Bms, Bnt, ecc. saranno analoghe agli spazi interi descritti, e le aree ABqK, ABrL, ABsM, ABtN, ecc. ai tempi. Dunque il corpo, durante la discesa, in un tempo qualsiasi ABrL descrive lo spazio Blr, e nel tempo LrtN lo spazio rlnt. C.V.D. E simile è la dimostrazione del moto esposto nella salita. C.V.D.

**[II.S1.13]** *Cor. 1.* Dunque la velocità massima che il corpo può acquistare cadendo sta alla velocità acquistata in un tempo dato qualsiasi come la forza data di gravità, dalla quale è continuamente sollecitato, sta alla forza di resistenza dalla quale è ostacolato alla fine di quel tempo.

**[II.S1.14]** *Cor. 2.* Se poi il tempo cresce in progressione aritmetica, la somma di quella velocità massima e della velocità nella salita, e così pure la loro differenza nella discesa, decresce in progressione geometrica.

**[II.S1.15]** *Cor. 3.* Ma anche le differenze degli spazi che sono descritti in differenze uguali di tempo decrescono nella stessa progressione geometrica.

**[II.S1.16]** *Cor. 4.* Lo spazio descritto dal corpo, poi, è la differenza di due spazi, dei quali uno è come il tempo preso dall’inizio della discesa e l’altro come la velocità; e questi, proprio all’inizio della discesa, sono anche uguali fra loro.

### Proposizione IV. Problema II (il proiettile in un mezzo resistente in rapporto alla velocità)

**[II.S1.17]** **Posto che la forza di gravità in un mezzo omogeneo sia uniforme e tenda perpendicolarmente al piano dell’orizzonte, definire il moto di un proiettile che in quel mezzo subisce una resistenza proporzionale alla velocità.**

**[II.S1.18]** Da un luogo qualsiasi D esca il proiettile lungo una linea retta qualsiasi DP, e con la lunghezza DP si rappresenti la sua velocità all’inizio del moto. Dal punto P si abbassi sulla linea orizzontale DC la perpendicolare PC, e si tagli DC in A in modo che DA stia ad AC come la resistenza del mezzo, nata all’inizio dal moto verso l’alto, sta alla forza di gravità; oppure (il che è lo stesso) in modo che il rettangolo di DA e DP stia al rettangolo di AC e CP come la resistenza totale all’inizio del moto sta alla forza di gravità. Con gli asintoti DC, CP si descriva un’iperbole qualsiasi GTBS, che tagli le perpendicolari DG, AB in G e B; e si completi il parallelogramma DGKC, il cui lato GK tagli AB in Q. Si prenda una linea N che stia a QB nel rapporto in cui DC sta a CP; e, innalzata in un punto qualsiasi R della retta DC la perpendicolare RT, che incontri l’iperbole in T e le rette EH, GK, DP in I, t e V, su di essa si prenda Vr uguale a tGT/N, o, il che è lo stesso, si prenda Rr uguale a GTIE/N: il proiettile nel tempo DRTG giungerà al punto r, descrivendo la linea curva DraF, sulla quale si trova sempre il punto r; giungerà all’altezza massima a sulla perpendicolare AB, e poi si avvicinerà sempre all’asintoto PC. E la sua velocità in un punto qualsiasi r è come la tangente della curva rL. C.V.T.

**[II.S1.19]** Infatti N sta a QB come DC sta a CP, ossia come DR sta a RV; e perciò RV è uguale a DR×QB/N, e Rr (cioè RV − Vr, ossia (DR×QB − tGT)/N) è uguale a (DR×AB − RDGT)/N. Si rappresenti ora il tempo con l’area RDGT e (per il Cor. II delle leggi) si distingua il moto del corpo in due, uno di salita, l’altro laterale. E poiché la resistenza è come il moto, anch’essa si distinguerà in due parti, proporzionali e contrarie alle parti del moto: perciò la lunghezza descritta dal moto laterale sarà (per la Prop. II di questo Libro) come la linea DR, e l’altezza invece (per la Prop. III di questo Libro) come l’area DR×AB − RDGT, cioè come la linea Rr. Proprio all’inizio del moto, poi, l’area RDGT è uguale al rettangolo DR×AQ; e perciò quella linea Rr (ossia (DR×AB − DR×AQ)/N) sta allora a DR come AB − AQ, ossia QB, sta a N, cioè come CP sta a DC, e quindi come il moto in altezza sta al moto in lunghezza all’inizio. Poiché dunque Rr è sempre come l’altezza, e DR sempre come la lunghezza, e Rr sta a DR all’inizio come l’altezza sta alla lunghezza, è necessario che Rr stia sempre a DR come l’altezza sta alla lunghezza, e perciò che il corpo si muova lungo la linea DraF, sulla quale si trova continuamente il punto r. C.V.D.

**[II.S1.20]** *Cor. 1.* Rr è dunque uguale a DR×AB/N − RDGT/N; e perciò, se si prolunga RT fino a X in modo che RX sia uguale a DR×AB/N (cioè, se si completa il parallelogramma ACPY, si congiunge DY, che taglia CP in Z, e si prolunga RT finché incontra DY in X), Xr sarà uguale a RDGT/N, e perciò proporzionale al tempo.

**[II.S1.21]** *Cor. 2.* Di qui, se si prendono innumerevoli CR, o, il che è lo stesso, innumerevoli ZX, in progressione geometrica, altrettante Xr saranno in progressione aritmetica. E di qui la curva DraF si traccia facilmente per mezzo della tavola dei logaritmi.

**[II.S1.22]** *Cor. 3.* Se si costruisce una parabola con vertice D, con il diametro DG prolungato verso il basso e con un lato retto che stia a 2DP come la resistenza totale proprio all’inizio del moto sta alla forza di gravità, la velocità con cui il corpo deve uscire dal luogo D lungo la retta DP per descrivere in un mezzo uniforme resistente la curva DraF sarà proprio quella con cui deve uscire dallo stesso luogo D, lungo la stessa retta DP, per descrivere la parabola in uno spazio non resistente. Infatti il lato retto di questa parabola, proprio all’inizio del moto, è DV²/Vr; e Vr è tGT/N, ossia DR×Tt/2N. Ora la retta che, se fosse condotta, toccherebbe l’iperbole GTS in G è parallela a DK; e perciò Tt è CK×DR/DC, e N era QB×DC/CP. E perciò Vr è DR²×CK×CP/(2DC²×QB), cioè (poiché DR e DC, DV e DP sono proporzionali) DV²×CK×CP/(2DP²×QB); e il lato retto DV²/Vr risulta 2DP²×QB/(CK×CP), cioè (poiché QB e CK, DA e AC sono proporzionali) 2DP²×DA/(AC×CP), e perciò sta a 2DP come DP×DA sta a CP×AC, cioè come la resistenza sta alla gravità. C.V.D.

**[II.S1.23]** *Cor. 4.* Di qui, se un corpo è lanciato da un luogo qualsiasi D, con una velocità data, lungo una retta qualsiasi DP data di posizione, ed è data la resistenza del mezzo proprio all’inizio del moto, si può trovare la curva DraF che quel corpo descriverà. Infatti dalla velocità data è dato il lato retto della parabola, come è noto. E prendendo 2DP a quel lato retto come la forza di gravità sta alla forza di resistenza, è data DP. Poi, tagliando DC in A in modo che CP×AC stia a DP×DA in quello stesso rapporto della gravità alla resistenza, sarà dato il punto A. E di qui è data la curva DraF.

**[II.S1.24]** *Cor. 5.* E viceversa, se è data la curva DraF, saranno date sia la velocità del corpo sia la resistenza del mezzo nei singoli luoghi r. Infatti, dal rapporto dato di CP×AC a DP×DA, sono date sia la resistenza del mezzo all’inizio del moto sia il lato retto della parabola; e di qui è data anche la velocità all’inizio del moto. Poi, dalla lunghezza della tangente rL, è data sia la velocità, che le è proporzionale, sia la resistenza, proporzionale alla velocità, in un luogo qualsiasi r.

**[II.S1.25]** *Cor. 6.* Poiché poi la lunghezza 2DP sta al lato retto della parabola come la gravità sta alla resistenza in D; e, accresciuta la velocità, la resistenza cresce nello stesso rapporto, mentre il lato retto della parabola cresce nel rapporto duplicato di quello: è evidente che la lunghezza 2DP cresce in quel rapporto semplice, e perciò è sempre proporzionale alla velocità, e non cresce né diminuisce al mutare dell’angolo CDP, se non muta anche la velocità.

**[II.S1.26]** *Cor. 7.* Di qui risulta chiaro il metodo per determinare la curva DraF dai fenomeni con ottima approssimazione, e per ricavarne la resistenza e la velocità con cui il corpo è lanciato. Si lancino due corpi simili e uguali con la stessa velocità dal luogo D, sotto angoli diversi CDP, CDp, e si conoscano i luoghi F, f in cui cadono sul piano orizzontale DC. Poi, presa una lunghezza qualsiasi per DP o Dp, si supponga che la resistenza in D stia alla gravità in un rapporto qualsiasi, e si rappresenti quel rapporto con una lunghezza qualsiasi SM. Quindi, per mezzo del calcolo, dalla lunghezza DP così assunta si trovino le lunghezze DF, Df; e dal rapporto Ff/DF trovato con il calcolo si sottragga lo stesso rapporto trovato con l’esperimento, e si rappresenti la differenza con la perpendicolare MN. Fa’ lo stesso una seconda e una terza volta, assumendo sempre un nuovo rapporto SM della resistenza alla gravità e ricavando una nuova differenza MN. Si portino poi le differenze positive da una parte della retta SM e le negative dall’altra; e per i punti N, N, N si conduca una curva regolare NNN che tagli la retta SMMM in X: SX sarà il vero rapporto della resistenza alla gravità, che si doveva trovare. Da questo rapporto si deve ricavare con il calcolo la lunghezza DF; e la lunghezza che sta alla lunghezza assunta DP come la lunghezza DF conosciuta per esperimento sta alla lunghezza DF appena trovata sarà la vera lunghezza DP. Trovata questa, si hanno sia la linea curva DraF che il corpo descrive, sia la velocità e la resistenza del corpo nei singoli luoghi.

### Scolio (la resistenza in rapporto duplicato della velocità)

**[II.S1.27]** Del resto, che la resistenza dei corpi sia in rapporto alla velocità è un’ipotesi più matematica che fisica. Nei mezzi privi di ogni rigidità le resistenze dei corpi sono in rapporto duplicato delle velocità. Infatti, per l’azione di un corpo più veloce, alla stessa quantità di mezzo viene comunicata, in un tempo minore, una quantità di moto maggiore in proporzione della maggiore velocità; e perciò in un tempo uguale, a causa della maggiore quantità di mezzo perturbata, viene comunicata una quantità di moto maggiore in rapporto duplicato; e la resistenza (per le Leggi II e III del moto) è come la quantità di moto comunicata. Vediamo dunque quali moti nascono da questa legge della resistenza.

---

## Apparato

### A.0 Estensioni del glossario

I termini seguenti non comparivano nel glossario comune né in quello aggiuntivo del Libro II. Ognuno è reso in modo costante in tutto il fascicolo.

| Latino | Italiano | Motivazione |
|---|---|---|
| *resistitur* (impersonale), *corpus cui resistitur* | «si resiste», «corpo al quale si resiste» | Titolo della Sezione e Propp. I–III. Si conserva il passivo impersonale latino; nella Prop. IV Newton stesso usa *resistentiam … patientis*, reso «che subisce una resistenza». Motte «is resisted». |
| *medium similare* | «mezzo omogeneo» | Resa fissata dal coordinatore. Prima occorrenza in II.S1.06: *similaris* è il mezzo «simile in ogni sua parte», cioè di densità e costituzione uniformi; Motte lo calca («similar medium»). Nella Prop. IV, Cor. 3, Newton scrive invece *medium uniforme*, reso «mezzo uniforme»: le due espressioni qui coincidono di fatto. |
| *rigor* | «rigidità» | Scolio (II.S1.27): *in mediis, quæ rigore omni vacant*. È la resistenza dovuta alla coesione o alla tenacità del mezzo, distinta da quella dovuta all’inerzia delle sue parti (di cui la Sezione II tratterà come «in rapporto duplicato»). Motte rende «tenacity». **Termine nuovo, da armonizzare** con le Sezioni II–VII, dove compaiono anche *tenacitas* e *lubricitas*: suggerisco di tenere «rigidità» per *rigor* e «tenacità» per *tenacitas*. |
| *hypothesis … naturalis* | «ipotesi … fisica» | Scolio. *Naturalis* nel senso di «della filosofia naturale», opposto a *mathematica*; Motte «physical». La resa letterale «naturale» sarebbe ambigua in italiano. |
| *convertendo* | «convertendo» | Lemma I: termine tecnico delle proporzioni (Euclide, *Elementi* V, def. 16), conservato come «componendo» nei fascicoli del Libro I. Qui applicato a A:(A−B) = B:(B−C) dà A:B = B:C (nota N2). Motte «by conversion». |
| *divisim* | «separando» | Prop. II, Caso 2. Come nei fascicoli del Libro I (operazione *dividendo* delle proporzioni). Motte «by division». |
| *continue proportionales*; *progressio continua* | «continuamente proporzionali»; «progressione continua» | Lemma I e Prop. II: termini in proporzione continua, cioè in progressione geometrica. |
| *per saltum capiuntur* | «presi a salti» | Prop. II, Caso 1: termini scelti a intervalli regolari. Motte «taken by intervals». |
| *analogus* | «analogo» | Prop. III: «proporzionale» (nel senso del greco *analogon*). Si conserva il termine; *analogarum summæ* → «le somme delle quantità analoghe». Motte «analogous». |
| *periodus* (*in horum temporum periodis*) | «estremo» | Prop. III, II.S1.11: il termine (la fine) di ciascun tempo, non un periodo nel senso del moto periodico. Motte «in these periods of time». |
| *vis absoluta* | «forza assoluta» | Prop. III: la forza effettiva rimasta dopo aver sottratto la resistenza dalla gravità (non la *vis absoluta* della Def. VIII, misura della causa). Motte «absolute forces». Nota N4. |
| *motus ad latus*; *motus in longitudinem* / *in altitudinem* | «moto laterale»; «moto in lunghezza» / «in altezza» | Prop. IV: le due componenti, orizzontale e verticale. Motte «lateral», «lengthwise», «upwards». |
| *tangere* (*quam punctum r semper tangit*) | «sulla quale si trova sempre» | Prop. IV: il punto r «tocca», cioè percorre, la curva. Come nel Fascicolo 7 (*punctum D tanget sectionem conicam*). Motte «the locus of the point r». |
| *exire de loco* | «uscire dal luogo» | Prop. IV, Cor. 3; *egredi* «uscire» (II.S1.18). |
| *projicere*; *projectile* | «lanciare»; «proiettile» | Come nel Fascicolo 3. |
| *quamproxime* | «con ottima approssimazione» | Come nei Fascicoli 3 e 5. Motte «nearly». |
| *differentiæ affirmativæ / negativæ* | «differenze positive / negative» | Prop. IV, Cor. 7. |
| *curva regularis* | «curva regolare» | Prop. IV, Cor. 7: una curva continua e liscia tracciata per i punti N (interpolazione grafica). |
| *phænomena* | «fenomeni» | Prop. IV, Cor. 7 (la trascrizione ha *phænominis*, § A.8). |
| *ad modum* | «al modo di» | Prop. II, Cor.: *ad modum temporis*, *ad modum velocitatis*, «come il tempo», «come la velocità». Motte «in the same manner as». |

*Impulsus* compare due volte nella Prop. II, Caso 1 (*impulsu unico*, *resistentiæ impulsus*): è l’azione istantanea della resistenza all’inizio di ogni particella di tempo, resa «impulso» come prevede il glossario (e come la Prop. I del Libro I, a cui il ragionamento è modellato). *Vis insita* compare due volte (Prop. I, Cor.; Prop. II), resa «forza insita».

### A.1 Proposizione I

**Latino:** *Corporis, cui resistitur in ratione velocitatis, motus ex resistentia amissus est ut spatium movendo confectum.*

**Inglese:** “If a body is resisted in the ratio of its velocity, the motion lost by resistance is as the space gone over in its motion.”

**Scelte.**

- *motus* → «quantità di moto» (glossario: *motus* quando indica la grandezza). Motte «motion».
- *itineris confecti particula* → «la particella di cammino percorsa»: *iter* è il cammino, distinto da *spatium* dell’enunciato; si conserva la variazione.
- *componendo* → «componendo»: qui è la somma delle parti (la «composizione» delle particelle), non l’operazione delle proporzioni; si conserva il termine come nel Fascicolo 5. Motte «by composition».
- **Cor.:** *gravitate omni destitutum* → «privo di ogni gravità»; *in spatiis liberis* → «in spazi liberi» (Motte «free spaces»); *sola vi insita* → «per la sola forza insita» (Motte «by its innate force only», resa non conforme al glossario).

### A.2 Lemma I

**Latino:** *Quantitates differentiis suis proportionales sunt continue proportionales.*

**Inglese:** “Quantities proportional to their differences are continually proportional.”

**Scelte.** *Sit A ad A−B ut B ad B−C & C ad C−D* → «Stia A ad A − B come B sta a B − C e come C sta a C − D». *& convertendo fiet* → «convertendo, risulterà»: la congiunzione *&* è assorbita. Nota N2.

### A.3 Proposizione II

**Latino:** *Si corpori resistitur in ratione velocitatis, & idem sola vi insita per medium similare moveatur, sumantur autem tempora æqualia: velocitates in principiis singulorum temporum sunt in progressione geometrica, & spatia singulis temporibus descripta sunt ut velocitates.*

**Inglese:** “If a body is resisted in the ratio of its velocity, and moves, by its vis insita only, through a similar medium, and the times be taken equal, the velocities in the beginning of each of the times are in a geometrical progression, and the spaces described in each of the times are as the velocities.”

**Scelte.**

- *per medium similare* → «in un mezzo omogeneo» (§ A.0, prima occorrenza). Motte lascia *vis insita* in latino.
- **Caso 1.** *si ipsis particularum initiis agat vis resistentiæ impulsu unico* → «se proprio all’inizio delle particelle la forza della resistenza agisce con un impulso unico»: la resistenza continua è sostituita da una successione di impulsi istantanei, come la forza centripeta nella Prop. I del Libro I. Motte aggiunge «**we suppose**».
- *per lem. I. lib. II.* → «per il Lemma I del Libro II»: il latino dice esplicitamente *lib. II.* e la resa lo conserva.
- *Componuntur autem horum terminorum rationes ex rationibus inter se iisdem terminorum intermediorum æqualiter repetitis* → «I rapporti di questi termini si compongono dei rapporti, uguali fra loro, dei termini intermedi ripetuti un numero uguale di volte». *Æqualiter repetitis* concorda con *rationibus*: sono i rapporti fra termini consecutivi, ripetuti lo stesso numero di volte. Motte «the equal ratios of the intermediate terms equally repeated».
- *eo ut … reddatur continuus* → «così che … diventi continuo».
- **Caso 2.** *divisim* → «separando» (§ A.0). *totæ* (sottinteso *velocitates*) → «le velocità intere». **La trascrizione ripete il Caso 2 due volte**, quasi identico (il secondo esemplare non ha la virgola prima di *(per prop. I. lib. II.)*): è certamente un artefatto della trascrizione o della pagina web, come il doppione d’intestazione segnalato nel Fascicolo 5. Si traduce una sola volta (II.S1.08). Da verificare sulla stampa (§ A.10).
- **Caso 2, rimando.** Il latino ha *per prop. I. lib. II.*; **Motte 1846 ha «by Prop. 1, Book I»**: errore di Motte (o della ristampa del 1846). La Prop. I del Libro I (legge delle aree) non c’entra; il rimando giusto è alla Prop. I di questo Libro (spazio come quantità di moto perduta).
- **Cor.** *asymptotis rectangulis* → «con gli asintoti ortogonali» (asintoti perpendicolari fra loro: l’iperbole è equilatera). Motte «rectangular asymptotes». *ad modum temporis*, *ad modum velocitatis* → «al modo del tempo», «al modo della velocità» (§ A.0). *in ratione geometrica* → «in rapporto geometrico», cioè in progressione geometrica. *linea indefinita DC* → «la linea indefinita DC», cioè variabile. Il marcatore ‹232› cade dentro *spatium ‹232› eo tempore*; nessuna perdita di testo. Nota N3.

### A.4 Proposizione III

**Latino:** *Corporis, cui, dum in medio similari recta ascendit vel descendit, resistitur in ratione velocitatis, quodque ab uniformi gravitate urgetur, definire motum.*

**Inglese:** “To define the motion of a body which, in a similar medium, ascends or descends in a right line, and is resisted in the ratio of its velocity, and acted upon by an uniform force of gravity.”

**Scelte.**

- *recta ascendit* → «sale in linea retta»: *recta* avverbio. *urgetur* → «è sollecitato».
- **Costruzione (II.S1.11).** *sumptum ad contrarias partes rectæ AB* → «preso dalla parte opposta della retta AB»: il rettangolo BADE sta dall’altra parte di AB rispetto a BACH (D sul prolungamento di CA oltre A). *perpendicula DE, de* → «le perpendicolari DE, de». *velocitates corporis (resistentiæ medii proportionales)*: Motte «of the **bodies**» (numero). *nulla* (la velocità al culmine) → «nulla»; **Motte stampa «O»**, cioè lo zero.
- *in horum temporum periodis* → «negli estremi di questi tempi» (§ A.0).
- **Dimostrazione (II.S1.12).** *ut resistentia medii principio singulorum temporum æquali ‹233› um*: il marcatore di pagina spezza *æqualium*; la lettura è certa.
- *Fiat AC ad AK vel ABHC ad ABkK* → «Si faccia in modo che AC stia ad AK, ossia ABHC ad ABkK»: i rettangoli sulla stessa altezza AB stanno come le basi.
- *per motus legem II.* → «per la Legge II del moto». **Motte ha «by Law I»**: errore. Il passo (forze come incrementi di velocità in tempi uguali) dipende dalla Legge II.
- *tum temporibus tum viribus gravitatis semper æqualibus analogæ* → «analoghe sia ai tempi sia alle forze di gravità, sempre uguali»: *semper æqualibus* si riferisce a entrambi (tempi uguali, forze di gravità uguali).
- *ad 12kq seu AC ad 12AK*: frazioni appiattite; lettura ½kq e ½AK, confermata dal calcolo (N4).
- *in medio temporis primi* → «nel mezzo del primo tempo».
- *areæ æquales BAKq*: il latino scrive qui *BAKq* (prima *ABqK*); stessa area, lettere in altro ordine. Conservato.
- *Corpus igitur inter descendendum* → «durante la discesa».
- Il latino ha **due** C.V.D. finali (dopo la discesa e dopo la frase sulla salita); **Motte omette il secondo**.
- **Cor. 2.** *summa velocitatis illius maximæ ac velocitatis in ascensu, atque etiam earundem differentia in descensu decrescit*: il verbo singolare concorda con il soggetto più vicino; la resa conserva il singolare («decresce»). Nota N5.
- **Cor. 4.** *quæ etiam ipso descensus initio æquantur inter se* → «e questi, proprio all’inizio della discesa, sono anche uguali fra loro». Motte aggiunge «[spaces]» tra parentesi quadre (integrazione dell’editore). Sul senso, nota N5.

### A.5 Proposizione IV

**Latino:** *Posito quod vis gravitatis in medio aliquo similari uniformis sit, ac tendat perpendiculariter ad planum horizontis; definire motum projectilis in eodem resistentiam velocitati proportionalem patientis.*

**Inglese:** “Supposing the force of gravity in any similar medium to be uniform, and to tend perpendicularly to the plane of the horizon; to define the motion of a projectile therein, which suffers resistance proportional to its velocity.”

**Scelte.**

- *Eloco quovis D*: **refuso probabile della trascrizione** per *E loco quovis D* (iniziale ornata seguita da minuscola, come *NAm* nella Prop. I). La traduzione segue il senso.
- *ut resistentia medii, ex motu in altitudinem sub initio orta, ad vim gravitatis* → «come la resistenza del mezzo, nata all’inizio dal moto verso l’alto, sta alla forza di gravità»: è la sola componente verticale della resistenza iniziale.
- *rectangulum sub DA & DP* → «il rettangolo di DA e DP».
- **Le rette EH**: il testo cita la retta EH (che RT incontra in I) senza definirla; dal calcolo (Rr uguale a GTIE/N uguale a (DR×AB − RDGT)/N) EH è la parallela a DC all’altezza AB, con E su DG (DE = AB) e passante per B. È una lettera della figura (NATP00088-4), da confermare sull’originale.
- *Capiatur linea N in ratione ad QB qua DC sit ad CP* → «Si prenda una linea N che stia a QB nel rapporto in cui DC sta a CP». Motte «as DC is **in** to CP»: sintassi zoppa.
- *in eo cape Vr æqualem ‹235› tGTN*: frazione appiattita, lettura tGT/N; *Rr æqualem GTIEN* → GTIE/N (§ A.8).
- *tempore DRTG*: area RDGT scritta con le lettere in altro ordine; conservato.
- *quam punctum r semper tangit* → «sulla quale si trova sempre il punto r» (§ A.0); Motte «the locus of the point r».
- *ad asymptoton PC..*: doppio punto, punteggiatura della trascrizione.
- *ut curvæ tangens rL* → «come la tangente della curva rL»: L è il punto in cui la tangente in r incontra l’asintoto PC (ricostruzione, nota N7). *rL.Q.E.I.* senza spazio nella trascrizione.
- **Dimostrazione.** *(per legum Corol. 2.)distinguatur* → «(per il Cor. II delle leggi) si distingua»; spazio mancante nella trascrizione. Il Cor. II delle leggi (Fascicolo 3, L10) è la composizione e risoluzione delle forze; qui Newton lo applica alla scomposizione del moto, come nel Libro I.
- *per prop. II. hujus*, *per prop. III. hujus* → «per la Prop. II di questo Libro», «per la Prop. III di questo Libro». Motte «Book II».
- *aequalis* (con *ae*) nella frase *area RDGT aequalis est*: grafia diversa da *æqualis* usato altrove; probabilmente della trascrizione.
- *ut AB−AQ seu QB) ad N*: parentesi aperta mancante; lettura «come (AB − AQ, ossia QB) sta a N».
- **Cor. 1.** *jungatur DY secans CP in Z* → «si congiunge DY, che taglia CP in Z».
- **Cor. 2.** *Corol 2.* senza punto nella trascrizione. *per tabulam logarithmorum* → «per mezzo della tavola dei logaritmi».
- **Cor. 3.** *Si vertice D, diametro DG deorsum producta, & latere recto … parabola construatur* → «Se si costruisce una parabola con vertice D, con il diametro DG prolungato verso il basso e con un lato retto…». *ut in medio uniformi resistente describat* → «per descrivere in un mezzo uniforme resistente»; *in spatio non resistente* → «in uno spazio non resistente» (Motte «in a non-resisting **medium**»). Motte 1846 stampa «at the beginning of the **notion**»: refuso dell’edizione 1846 per *motion*.
- *Recta autem quæ, si duceretur, hyperbolam GTS tangeret in G* → «Ora la retta che, se fosse condotta, toccherebbe l’iperbole GTS in G»: si conserva il condizionale controfattuale.
- *N erat* → «N era»: l’imperfetto rimanda alla costruzione.
- **Cor. 4.** *ut notum est* → «come è noto» (Libro I, e Galileo). **Motte stampa «GP × AC»** per *CP×AC*: errore. *Et sumendo 2DP ad latus illud rectum, ut est vis gravitatis ad vim resistentiæ*: il rapporto 2DP : lato retto = gravità : resistenza è l’inverso di quello del Cor. 3 (lato retto : 2DP = resistenza : gravità), quindi coerente.
- **Cor. 5.** **Motte stampa «tangent L»** per *tangentis rL*: omissione di *r*.
- **Cor. 6.** *in ratione illa duplicata* → «nel rapporto duplicato di quello»; *in ratione illa simplici* → «in quel rapporto semplice».
- **Cor. 7.** *ex phænominis*: **refuso probabile della trascrizione** per *phænomenis*. *de ratione FfDF per calculum inventa*: frazione appiattita, Ff/DF. *Idem fac iterum ac tertio* → «Fa’ lo stesso una seconda e una terza volta»: si conserva l’imperativo di seconda persona, che Newton alterna al congiuntivo esortativo. *rectam SMMM* → «la retta SMMM» (la retta SM con i punti M successivi). *vera ratio* → «il vero rapporto». Il marcatore ‹238› cade fra *SM.* e *Deinde*.

### A.6 Scolio

**Latino (incipit):** *Cæterum, resistentiam corporum esse in ratione velocitatis, hypothesis est magis mathematica quam naturalis.*

**Inglese:** “But, yet, that the resistance of bodies is in the ratio of the velocity, is more a mathematical hypothesis than a physical one.”

**Scelte.** *Cæterum* → «Del resto». *rigore omni vacant* → «privi di ogni rigidità» (§ A.0; Motte «void of all tenacity»). *actione corporis velocioris communicatur eidem medii quantitati, tempore minore, motus major in ratione majoris velocitatis* → «per l’azione di un corpo più veloce, alla stessa quantità di mezzo viene comunicata, in un tempo minore, una quantità di moto maggiore in proporzione della maggiore velocità». *ob majorem medii quantitatem perturbatam* → «a causa della maggiore quantità di mezzo perturbata». *per motus leg. II & III.* → «per le Leggi II e III del moto». Nota N9.

### A.7 Riepilogo: dove Motte aggiunge, omette o sbaglia

| Luogo | Latino | Motte 1846 | Tipo |
|---|---|---|---|
| II.S1.03 | *sola vi insita* | «by its innate force only» | termine non conforme al glossario |
| II.S1.06 | *sola vi insita* | «by its vis insita only» | latino lasciato non tradotto |
| II.S1.06 e passim | *medium similare* | «similar medium» | calco |
| II.S1.07 | *si … agat vis resistentiæ* | «if … **we suppose** the resistance to act» | aggiunta |
| II.S1.08 | *per prop. I. lib. II.* | «by Prop. 1, **Book I**» | **rimando errato** |
| II.S1.08 | Caso 2 ripetuto due volte | una volta | (doppione della trascrizione, non di Motte) |
| II.S1.11 | *velocitates corporis* | «velocities of the **bodies**» | numero |
| II.S1.11 | *nulla* | «O» | cifra al posto della parola |
| II.S1.11 | *in horum temporum periodis* | «in these periods of time» | calco ambiguo |
| II.S1.12 | *per motus legem II.* | «by **Law I**» | **rimando errato** |
| II.S1.12 | *Q.E.D.* finale (secondo) | — | omissione |
| II.S1.16 | *quæ etiam … æquantur* | «which **[spaces]** also …» | integrazione dell’editore |
| II.S1.18 | *in ratione ad QB qua DC sit ad CP* | «as DC is **in** to CP» | sintassi zoppa |
| II.S1.18, II.S1.19 | *quam punctum r semper (perpetuo) tangit* | «the locus of the point r» | parafrasi |
| II.S1.22 | *motus* | «**notion**» | refuso dell’edizione 1846 |
| II.S1.22 | *in spatio non resistente* | «in a non-resisting **medium**» | termine diverso |
| II.S1.23 | *CP×AC* | «**GP** × AC» | **lettera errata** |
| II.S1.24 | *tangentis rL* | «tangent **L**» | omissione di una lettera |
| II.S1.26 | *quamproxime* | «nearly» | resa debole |
| II.S1.27 | *rigore omni vacant* | «void of all tenacity» | resa diversa (*rigor* / *tenacitas*) |
| II.S1.27 | *naturalis* | «physical» | resa per senso (accolta anche qui) |
| II.S1.19 | *RV æqualis DR×QBN* | RV = [SVG 356] = (DR×QB − tGT)/N | **formula errata**: anticipa il numeratore della formula successiva (SVG 357); deve essere DR×QB/N |
| passim | — | righe `[FIG: …]` | descrizioni aggiunte dall’edizione Gutenberg; quella della Prop. III (seconda) ripete il Cor. 1 |

Le formule di Motte stampate come immagini (SVG 352–371) sono state controllate: 19 coincidono con il latino, una (356) è errata (§ A.9).

### A.8 Refusi e anomalie della trascrizione; letture delle formule

| Luogo | Trascrizione | Lettura | Tipo |
|---|---|---|---|
| II.S1.02 | *NAm* | *Nam* | capolettera tipografico |
| II.S1.08 | Caso 2 ripetuto due volte | una volta | **artefatto della trascrizione** |
| II.S1.12 | *æquali ‹233› um* | *æqualium* | parola spezzata dal marcatore di pagina |
| II.S1.12 | *12kq*, *12AK* | ½kq, ½AK | frazioni appiattite |
| II.S1.18 | *Eloco* | *E loco* | refuso probabile |
| II.S1.18 | *tGTN*; *GTIEN* | tGT/N; GTIE/N | frazioni appiattite |
| II.S1.18 | *PC..*; *rL.Q.E.I.* | — | punteggiatura e spaziatura |
| II.S1.19 | *DR×QBN* | DR×QB/N | frazione appiattita |
| II.S1.19 | *(id est RV−Vr seu DR×QB−tGTN)* | (DR×QB − tGT)/N | frazione appiattita, numeratore composto |
| II.S1.19 | *DR×AB−RDGTN* | (DR×AB − RDGT)/N | idem |
| II.S1.19 | *(per legum Corol. 2.)distinguatur* | — | spazio mancante |
| II.S1.19 | *aequalis* | *æqualis* | grafia |
| II.S1.19 | *(seu DR×AB−DR×AQN)* | (DR×AB − DR×AQ)/N | frazione appiattita |
| II.S1.19 | *AB−AQ seu QB)* | (AB − AQ, ossia QB) | parentesi aperta mancante |
| II.S1.20 | *DR×ABN−RDGTN*; *DR×ABN*; *RDGTN* | DR×AB/N − RDGT/N; DR×AB/N; RDGT/N | frazioni appiattite |
| II.S1.21 | *Corol 2.* | *Corol. 2.* | punteggiatura |
| II.S1.22 | *DV quad.Vr* | DV²/Vr | frazione appiattita |
| II.S1.22 | *DR×Tt2N* | DR×Tt/2N | idem |
| II.S1.22 | *CK×DRDC*; *QB×DCCP* | CK×DR/DC; QB×DC/CP | idem |
| II.S1.22 | *DRq×CK×CP2DCq×QB* | DR²×CK×CP/(2DC²×QB) | idem |
| II.S1.22 | *DVq×CK×CP2DPq×QB* | DV²×CK×CP/(2DP²×QB) | idem |
| II.S1.22 | *2DPq×QBCK×CP* | 2DP²×QB/(CK×CP) | idem |
| II.S1.22 | *2DPq×DA AC×CP* | 2DP²×DA/(AC×CP) | idem (con spazio) |
| II.S1.26 | *phænominis* | *phænomenis* | refuso probabile |
| II.S1.26 | *FfDF* | Ff/DF | frazione appiattita |

Tutte le letture delle frazioni sono state controllate numericamente (nota N7): con esse ogni uguaglianza del testo risulta esatta. Nessun punto è stato verificato sulla stampa del 1726 (§ A.10).

### A.9 Formule SVG di Motte: controllo

Controllate sul LaTeX estratto dall’EPUB Gutenberg n. 76404 (`src_epub/svg_tex.tsv`); la 356 anche sull’immagine resa con `rsvg-convert`. Le stringhe `en` della Parte B contengono i marcatori così come sono. Formula attesa = lettura del latino.

| SVG | Luogo | Formula che il latino fa attendere | Esito |
|---|---|---|---|
| 352 | II.S1.12 | ½kq | verificata |
| 353 | II.S1.12 | ½AK | verificata |
| 354 | II.S1.18; II.S1.22 (riusato) | tGT/N | verificata |
| 355 | II.S1.18 | GTIE/N | verificata |
| 356 | II.S1.19 | DR×QB/N | **errata**: Motte ha (DR×QB − tGT)/N |
| 357 | II.S1.19 | (id est RV − Vr seu (DR×QB − tGT)/N) | verificata |
| 358 | II.S1.19 | (DR×AB − RDGT)/N | verificata |
| 359 | II.S1.19 | (seu (DR×AB − DR×AQ)/N) | verificata |
| 360 | II.S1.20 | DR×AB/N − RDGT/N | verificata |
| 361 | II.S1.20 | DR×AB/N | verificata |
| 362 | II.S1.20 | RDGT/N | verificata |
| 363 | II.S1.22 (due volte) | DV²/Vr | verificata |
| 364 | II.S1.22 | DR×Tt/2N | verificata |
| 365 | II.S1.22 | CK×DR/DC | verificata |
| 366 | II.S1.22 | QB×DC/CP | verificata |
| 367 | II.S1.22 | DR²×CK×CP/(2DC²×QB) | verificata |
| 368 | II.S1.22 | DV²×CK×CP/(2DP²×QB) | verificata |
| 369 | II.S1.22 | 2DP²×QB/(CK×CP) | verificata |
| 370 | II.S1.22 | 2DP²×DA/(AC×CP) | verificata |
| 371 | II.S1.26 | Ff/DF | verificata |

Esito: **19 SVG su 20 verificate** (coincidono con il latino, compresi i numeratori composti 357–359 con il vincolo corretto). **La 356 è errata**: Motte stampa (DR×QB − tGT)/N dove il latino ha DR×QB/N (RV = DR×QB/N, controllato anche in N7); l’errore è nel § A.7.

### A.10 Punti da controllare sulla stampa ECCO

| Pagina 1726 | Trascrizione | Lettura attesa | Motivo |
|---|---|---|---|
| 231 | Caso 2 della Prop. II stampato due volte | una volta | doppione quasi identico, quasi certamente artefatto |
| 232–233 | *æquali ‹233› um* | *æqualium* a cavallo di pagina | confermare la divisione di parola |
| 233 | *12kq*, *12AK* | ½kq, ½AK | forma tipografica della frazione |
| 234 | *Eloco* | *E loco* (capolettera) | refuso probabile |
| 234 | retta *EH* non definita nel testo | E su DG con DE = AB, EH parallela a DC per B | confermare sulla figura NATP00088-4 |
| 235 | *PC..*; *AB−AQ seu QB)* | *PC.*; *(AB−AQ seu QB)* | punteggiatura, parentesi |
| 235 | *aequalis* | *æqualis* | grafia |
| 235 | le frazioni della dimostrazione e del Cor. 1 | vedi § A.8 | vincoli dei numeratori composti |
| 235 | *Corol 2.* | *Corol. 2.* | punteggiatura |
| 236 | *2DPq×DA AC×CP* | 2DP²×DA/(AC×CP) | spazio anomalo |
| 237 | *phænominis* | *phænomenis* | refuso probabile |
| 237–238 | lettera L della tangente rL | L su PC | confermare sulla figura NATP00088-6 |

### A.11 Rimandi verificati

| Rimando nel latino | Resa | Verifica |
|---|---|---|
| *per lem. I. lib. II.* (II.S1.07, II.S1.12) | Lemma I del Libro II | regge: velocità (Prop. II) e incrementi (Prop. III) proporzionali alle proprie differenze |
| *per prop. I. lib. II.* (II.S1.08) | Prop. I del Libro II | regge; Motte sbaglia («Book I») |
| *per motus legem II.* (II.S1.12) | Legge II del moto | regge; Motte sbaglia («Law I») |
| *per corol. 3. lem. VII. & lem. VIII. lib. I.* (II.S1.12) | Cor. 3 del Lemma VII e Lemma VIII del Libro I | **regge** (Fascicolo 4, S1.21 e S1.22–S1.24): l’arco Bq e la corda si scambiano nei rapporti ultimi, e il trilineo Bkq diventa alla fine il triangolo di base kq e altezza AK; da qui ABqK : Bkq = Kq : ½kq nel limite (verificato in N4). Il rapporto è ultimo, non esatto: Newton lo usa per particelle di tempo evanescenti |
| *per legum Corol. 2.* (II.S1.19) | Cor. II delle leggi | regge (Fascicolo 3, L10): risoluzione del moto in due componenti |
| *per prop. II. hujus*; *per prop. III. hujus* (II.S1.19) | Prop. II e III di questo Libro | reggono: componente orizzontale senza gravità (Prop. II, Cor.), verticale con gravità (Prop. III) |
| *per motus leg. II & III.* (II.S1.27) | Leggi II e III del moto | reggono |

Rimandi al Libro I: 2 (Cor. 3 del Lemma VII, Lemma VIII), entrambi verificati sul Fascicolo 4; nessuno che non torni.

---

## Note editoriali e fisiche

Queste note sono aggiunte del presente fascicolo, non affermazioni tradotte da Newton. Le verifiche numeriche sono state eseguite con uno script Python (`tmp/13-L2-S1/verifica.py`): il moto è calcolato dalla soluzione esatta delle equazioni con resistenza lineare, la figura di Newton è costruita dalle sole lettere del testo, e si confrontano le grandezze. Nelle note *c* indica la resistenza per unità di massa e di velocità (resistenza = *c*·*v*), *g* la gravità.

### N1. Prop. I: resistenza lineare e spazio

Con resistenza proporzionale alla velocità, la quantità di moto perduta in un istante è proporzionale a *v*·d*t*, cioè allo spazio percorso: in termini moderni *m*Δ*v* = −*c m* *s*. Il Cor. ne ricava lo spazio totale percorribile in un tempo infinito, *v*₀/*c*, e la proporzione «spazio totale : spazio descritto = quantità di moto iniziale : quantità di moto perduta». Verifica numerica (*c* = 0,7, *v*₀ = 3): rapporto perdita/spazio costante e uguale a *c* a ogni istante; spazio totale/spazio descritto a *t* = 2 uguale a *v*₀/(*v*₀ − *v*) = 1,3273 (esatto).

### N2. Lemma I: il «convertendo»

Da A : (A − B) = B : (B − C) l’operazione *convertendo* (rapporto dell’antecedente alla differenza fra antecedente e conseguente, applicata all’indietro) dà A : B = B : C. È il passo da «decremento proporzionale alla quantità» a «progressione geometrica»: in termini moderni, d*v* ∝ −*v* d*t* implica *v* = *v*₀ e^(−*ct*).

### N3. Prop. II e il suo Corollario: il decadimento esponenziale e l’iperbole

Il Caso 1 discretizza la resistenza in impulsi, come la Prop. I del Libro I discretizza la forza centripeta, e poi passa al limite. Il risultato è *v*(*t*) = *v*₀ e^(−*ct*): velocità in progressione geometrica per tempi in progressione aritmetica. Il Caso 2 dà gli spazi parziali proporzionali alle velocità iniziali di ciascun intervallo.

Il Corollario è la rappresentazione geometrica del logaritmo: l’area sotto l’iperbole equilatera, fra le ordinate AB e DG, è proporzionale a ln(AC/DC). Se l’area cresce come il tempo, DC decresce in progressione geometrica e AD = AC − DC rappresenta lo spazio. Verifica numerica: area/tempo costante (1,4 con *k* = 2, *c* = 0,7) e AD/spazio costante (= *c*); rapporto fra velocità successive in tempi uguali costante (0,7558), spazi/velocità costanti.

### N4. Prop. III: salita e discesa verticale

Costruzione ricostruita: C origine degli asintoti; A, D, d, I, i, K… sulla retta AC (D e d dalla parte di A opposta a C, I e i fra A e C); iperbole *y* = AB·AC/*x* (con *x* distanza da C), passante per B; E, e sulla parallela ad AC condotta per B; F, f sulla stessa parallela sopra I, i; K, k sull’iperbole sopra I, i (nella costruzione della salita, II.S1.11) — mentre nella dimostrazione (II.S1.12, figura 3) le lettere K, L, M, N stanno su AC e k, l, m, n sulla parallela BH. La doppia funzione della lettera K appartiene a due figure diverse (NATP00088-2 e -3).

Equazioni moderne: in salita d*v*/d*t* = −*g* − *cv*, in discesa d*v*/d*t* = *g* − *cv*; velocità limite *V* = *g*/*c* (il rettangolo BACH, cioè AC). In salita *v* + *V* = (*v*₀ + *V*) e^(−*ct*), rappresentata da DC; in discesa *V* − *v* = *V* e^(−*ct*), rappresentata da IC. La «forza assoluta» di II.S1.12 è *g* − *cv* (la gravità meno la resistenza), proporzionale a IC.

Verifica numerica (*c* = 0,7, *g* = 9,8, *k* = 2): area DGgd / tempo e area ABKI / tempo costanti (1,4); area EGge / spazio di salita e area BFK / spazio di discesa costanti (0,1 = AB); al culmine, area DGBA = tempo di salita e area EGB = altezza massima, nella stessa scala. Il rapporto ABqK : Bkq tende a AC : ½AK quando AK → 0 (27,66 contro 28; 279,67 contro 280; 2799,67 contro 2800): il rapporto di Newton è un **rapporto ultimo**, valido per particelle di tempo evanescenti, come richiede il rimando ai Lemmi VII e VIII del Libro I. «La resistenza nel mezzo del primo tempo» rappresentata da ½AK è anch’essa esatta solo al primo ordine.

### N5. Prop. III, corollari

- **Cor. 1**: *V* : *v* = *g* : *cv*, immediato.
- **Cor. 2**: in salita *V* + *v*, in discesa *V* − *v*, decrescono entrambe del fattore e^(−*c*Δ*t*) a ogni intervallo Δ*t*: verificato (0,7047 per Δ*t* = 0,5, in salita e in discesa).
- **Cor. 3**: le differenze fra gli spazi descritti in intervalli uguali successivi decrescono nello stesso rapporto: verificato (0,7047).
- **Cor. 4**: in discesa da fermo *s* = *Vt* − *v*/*c*: uno spazio «come il tempo» (*Vt*, l’area ABrL) e uno «come la velocità» (*v*/*c*, il rettangolo ABlL); differenza verificata uguale a *s* con errore nullo. La clausola *quæ etiam ipso descensus initio æquantur inter se* è letteralmente banale se intesa dei due spazi (entrambi nulli all’inizio); in senso non banale vale per i loro incrementi nascenti, che all’inizio coincidono (d(*Vt*)/d*t* = d(*v*/*c*)/d*t* = *V* per *t* = 0). La traduzione conserva l’ambiguità del latino.

### N6. Prop. IV: la costruzione

Ricostruzione dalle lettere: D origine, DC orizzontale, P sopra C (PC perpendicolare); A fra D e C; iperbole GTBS con asintoti DC e CP, cioè *y*·RC = costante; G su DG perpendicolare in D, B su AB perpendicolare in A; parallelogramma DGKC (K su CP all’altezza DG); Q = GK ∩ AB; E su DG con DE = AB, EH parallela a DC per B (§ A.5); R su DC, RT perpendicolare, che incontra l’iperbole in T, EH in I, GK in t, DP in V.

In termini moderni, con velocità iniziale (*u*₀, *w*₀): *x* = (*u*₀/*c*)(1 − e^(−*ct*)), *y* = ((*w*₀ + *g*/*c*)/*c*)(1 − e^(−*ct*)) − (*g*/*c*)*t*. La figura di Newton ha DC = *u*₀/*c* (la gittata orizzontale asintotica, da cui l’asintoto PC), CP = *w*₀/*c*, quindi DP = *v*₀/*c*; DA : AC = *cw*₀ : *g*.

### N7. Prop. IV: verifica numerica e letture delle formule

Con *c* = 0,6, *g* = 9,8, *u*₀ = 8, *w*₀ = 12 e un’iperbole qualsiasi (costante 3):

- rettangolo DA×DP : rettangolo AC×CP = *cv*₀ : *g* = 0,88299 (la seconda forma della costruzione equivale alla prima);
- area RDGT / tempo costante (1,8) a *t* = 0,3; 1; 2,5; 6: il tempo è rappresentato dall’area;
- Rr = (DR×AB − RDGT)/N coincide con l’altezza *y* (rapporto 1,000000000 ai quattro istanti); RV = DR×QB/N e RV − Vr = Rr con errore ≤ 10⁻¹⁴: **le letture delle frazioni appiattite in § A.8 sono confermate**;
- il vertice della curva cade esattamente sulla perpendicolare AB (*x* al culmine = DA = 5,6471);
- la tangente in r prolungata fino all’asintoto PC (punto L) ha lunghezza proporzionale alla velocità (rL/velocità = 1/*c* costante): così si legge «la tangente della curva rL»;
- **Cor. 1**: DR×AB/N coincide con DR×CP/DA, cioè con l’ordinata della retta DY (Y vertice del parallelogramma ACPY sopra A): l’identità chiave è QB×DC = AB×DA; Xr = RDGT/N, proporzionale al tempo (verificato);
- **Cor. 2**: per CR = DC, DC/2, DC/4, DC/8, Xr = 0; 18,869; 37,738; 56,607: progressione aritmetica;
- **Cor. 3**: la tangente all’iperbole in G è parallela a DK (pendenze uguali: 0,016875); DV²/Vr tende, per R → D, a 2DP²×DA/(AC×CP) = 42,449 (42,280; 42,432; 42,447 per *t* = 10⁻², 10⁻³, 10⁻⁴), che è 2*v*₀²/*g*, il lato retto della parabola nel vuoto con la stessa velocità iniziale. Il rapporto lato retto : 2DP tende a *cv*₀/*g*, resistenza : gravità. **Il Cor. 3 è corretto**, purché si legga «proprio all’inizio del moto» come rapporto ultimo.

### N8. Prop. IV, Cor. 4–7: dalla teoria all’esperimento

Il Cor. 6 mostra che 2DP = 2*v*₀/*c* dipende solo dalla velocità (e dal mezzo), non dall’angolo di lancio. Il Cor. 7 è un metodo di **falsa posizione grafica**: si assume un valore di prova del rapporto resistenza/gravità (SM), si calcola il rapporto Ff/DF delle gittate per i due angoli, se ne sottrae il valore sperimentale, e si interpola con una curva regolare lo zero della differenza (il punto X). Poi si corregge la scala di DP con la gittata osservata. Non ho simulato il metodo; la sua logica è coerente con la costruzione (il rapporto Ff/DF non dipende dalla scala di DP, ma solo dal rapporto resistenza/gravità e dagli angoli: affermazione mia, non verificata numericamente).

### N9. Lo Scolio: perché la resistenza lineare è «più matematica che fisica»

L’argomento di Newton è dimensionale ante litteram: un corpo più veloce mette in moto, nello stesso tempo, più mezzo (in proporzione alla velocità) e a ciascuna parte comunica più moto (ancora in proporzione alla velocità): la resistenza cresce come *v*². In termini moderni è la resistenza «inerziale» dei fluidi a numero di Reynolds elevato; la resistenza lineare (viscosa, legge di Stokes) vale invece a bassa velocità o in fluidi molto viscosi (non verificato sulle fonti allegate). La Sezione II tratta appunto la resistenza in rapporto duplicato della velocità.

---

## Controllo della copertura

Pagine 1726 dai marcatori ‹n› della trascrizione. Motte 1846: l’estratto non ha marcatori di pagina; si indica la sezione corrispondente.

| Identificatori | Incipit latino | Contenuto | 1726 | Motte 1846 |
|---|---|---|---|---|
| II.S1.01–II.S1.03 | *Corporis, cui resistitur* … *Igitur si corpus, gravitate omni destitutum* | Prop. I, enunciato, dimostrazione, Cor. | p. 230 | Sect. I, Prop. I |
| II.S1.04–II.S1.05 | *Quantitates differentiis suis proportionales* | Lemma I | p. 230 | Lemma I |
| II.S1.06–II.S1.08 | *Si corpori resistitur in ratione velocitatis* | Prop. II, enunciato, Casi 1–2 (Caso 2 duplicato nella trascrizione) | p. 231 | Prop. II |
| II.S1.09 | *Hinc si asymptotis rectangulis AC, CH* | Prop. II, Cor. | pp. 231–232 | Prop. II, Cor. |
| II.S1.10–II.S1.12 | *Corporis, cui, dum in medio similari* … *Resolvatur enim rectangulum* | Prop. III, enunciato, costruzione, dimostrazione | pp. 232–233 | Prop. III |
| II.S1.13–II.S1.16 | *Igitur velocitas maxima* … *Spatium vero a corpore descriptum* | Prop. III, Cor. 1–4 | pp. 233–234 | Prop. III, Cor. 1–4 |
| II.S1.17–II.S1.19 | *Posito quod vis gravitatis* … *Est enim N ad QB* | Prop. IV, enunciato, costruzione, dimostrazione | pp. 234–235 | Prop. IV |
| II.S1.20–II.S1.26 | *Est igitur Rr æqualis* … *Unde liquet methodus* | Prop. IV, Cor. 1–7 | pp. 235–238 | Prop. IV, Cor. 1–7 |
| II.S1.27 | *Cæterum, resistentiam corporum* | Scolio | p. 239 | Scholium |

**Controlli eseguiti.**

1. **Copertura.** Ho riletto in sequenza ogni periodo della trascrizione, da *Corporis, cui resistitur* a *ex hac lege resistentiæ*, contro la traduzione: nessuna frase manca. Il doppione del Caso 2 della Prop. II è tradotto una volta e segnalato (A.3, A.8, A.10). I 27 identificatori sono consecutivi e unici (controllo automatico).
2. **Parte B.** `check.py` sul file finale: JSON valido, tutte le stringhe `la` sottostringhe esatte della trascrizione; esito nel messaggio di consegna.
3. **Matematica.** Verifiche numeriche (N1–N7) per le Propp. I, II (con il Cor.), III (costruzione, dimostrazione, rapporto ultimo ABqK : Bkq, Cor. 1–4), IV (costruzione, dimostrazione, tangente rL, vertice in AB, Cor. 1, 2, 3). Tutti i risultati di Newton risultano corretti. Non ci sono tabelle numeriche in questa Sezione.
4. **Motte.** Confronto di tutta la sezione corrispondente, comprese le 20 formule SVG (352–371) controllate sul LaTeX dell’EPUB: 19 coincidono, la 356 è errata (§ A.9). Divergenze nel § A.7.
5. **Rimandi.** Tutti i rimandi del testo controllati (§ A.11).
6. **Separazione fra testo e commento.** Il testo tradotto non contiene formule moderne.

**Non ho potuto verificare:**

- **la stampa del 1726** (§ A.10): doppione del Caso 2, *Eloco*, *phænominis*, punteggiatura e vincoli delle frazioni;
- **le figure originali** NATP00088-1…7: la posizione di E, H (retta EH), di L (tangente rL), di F e f, e la doppia funzione della lettera K fra le figure 2 e 3 sono ricostruite dal testo e dal calcolo;
- **la paginazione di Motte 1846**: l’estratto non ha marcatori;
- **il metodo del Cor. 7 della Prop. IV**: non simulato numericamente.

---

## Registro del lavoro successivo

| Unità | Stato |
|---|---|
| Libro II, Sezione I (Propp. I–IV, Lemma I, Scolio) | **Fascicolo 13, presente documento, prima versione** |
| Punti della stampa (A.10) | Da verificare sulla scansione ECCO |
| SVG 352–371 di Motte | Controllate (§ A.9): 19 coincidono, la 356 è errata |
| Figure NATP00088-1…7 | Da consultare per confermare `figura_base` (soprattutto EH, L, K) |
| *rigor* «rigidità» | Da armonizzare con le Sezioni II–VII (*tenacitas*, *lubricitas*, *attritus*) |
| Paginazione Motte 1846 | Da ricavare dagli ancoraggi `Page_n` dell’EPUB |
| Pagine interattive | Parte B: 7 unità; la Prop. IV ha passi lunghi con molte frazioni, da mostrare in più tempi |
| Revisione filologica e scientifica indipendente | Da eseguire |

Il presente testo è una nuova traduzione assistita da IA. Non riproduce traduzioni italiane o inglesi moderne. **Licenza prevista** (decisione del curatore, Fascicolo 3): testi e traduzioni CC BY-SA 4.0, codice MIT. La trascrizione latina è © The Newton Project; i testi di Motte sono di pubblico dominio.

---

## Parte B — Dati per le pagine interattive

Unità incluse: le parti con figura o costruzione geometrica propria. **Escluse**: la Prop. I e il suo Cor. (argomento per rapporti, senza figura), il Lemma I (due righe di algebra delle proporzioni), la Prop. II nella dimostrazione principale (senza figura: la figura 1 appartiene al Cor., incluso), i Cor. 1–4 della Prop. III e i Cor. 4–6 della Prop. IV (senza dimostrazione geometrica propria), lo Scolio.

Convenzioni:

- `la`: testo latino esatto della trascrizione, refusi e frazioni appiattite compresi; le letture sono in `nota` e nel § A.8;
- `it`: la traduzione di questo fascicolo;
- `en`: Motte 1846, allineato per senso, con i marcatori `[SVG n]` inclusi (lo strumento di controllo li ignora); le formule, controllate, sono nel § A.9;
- `dipende_da`: soltanto i rimandi citati nella frase latina;
- `figura.mostra`: elementi da rendere visibili, cumulativi; `figura.evidenzia`: relazioni da mettere in risalto.

```json
{
 "fascicolo": "13-L2-S1",
 "versione": "0.1",
 "data": "2026-11-08",
 "convenzioni": {
  "dipende_da": "solo rimandi citati esplicitamente nella frase latina",
  "en": "Motte 1846, allineato per senso; marcatori [SVG n] inclusi (formule controllate sul LaTeX dell’EPUB, § A.9; la 356 è errata in Motte)",
  "figura.mostra": "elementi da rendere visibili al passo, cumulativi salvo indicazione",
  "la": ""
 },
 "unita": [
  {
   "id": "L2-P2-Cor",
   "tipo": "Corollarium",
   "titolo": "Prop. II, Cor. — il tempo come area iperbolica",
   "copertura": [
    "II.S1.09"
   ],
   "fonti": {
    "la": "",
    "en": "Motte 1846, Book II, Sect. I, Prop. II, Cor."
   },
   "enunciato": {
    "la": "",
    "it": "Di qui, se con gli asintoti ortogonali AC, CH si descrive l’iperbole BG, e AB, DG sono perpendicolari all’asintoto AC, e si rappresentano sia la velocità del corpo sia la resistenza del mezzo, proprio all’inizio del moto, con una linea data qualsiasi AC, e, trascorso un certo tempo, con la linea indefinita DC, il tempo può essere rappresentato dall’area ABGD e lo spazio descritto in quel tempo dalla linea AD.",
    "en": "Hence if to the rectangular asymptotes AC, CH, the hyperbola BG is described, and AB, DG be drawn perpendicular to the asymptote AC, and both the velocity of the body, and the resistance of the medium, at the very beginning of the motion, be expressed by any given line AC, and, after some time is elapsed, by the indefinite line DC; the time may be expressed by the area ABGD, and the space described in that time by the line AD."
   },
   "figura_base": {
    "punti": [
     "A",
     "B",
     "C",
     "D",
     "G",
     "H"
    ],
    "vincoli": [
     "CA e CH asintoti perpendicolari, C origine",
     "iperbole equilatera per B: y·x = AB·AC (x distanza da C lungo CA)",
     "AB ⊥ AC in A; D fra A e C, DG ⊥ AC con G sull’iperbole",
     "AC = velocità iniziale; DC = velocità al tempo t",
     "area ABGD ∝ tempo; AD ∝ spazio"
    ]
   },
   "passi": [
    {
     "id": "L2-P2-Cor-p1",
     "la": "",
     "it": "Infatti, se quell’area, per il moto del punto D, cresce uniformemente al modo del tempo, la retta DC decrescerà in rapporto geometrico al modo della velocità, e le parti della retta AC descritte in tempi uguali decresceranno nello stesso rapporto.",
     "en": "For if that area, by the motion of the point D, be uniformly increased in the same manner as the time, the right line DC will decrease in a geometrical ratio in the same manner as the velocity; and the parts of the right line AC, described in equal times, will decrease in the same ratio.",
     "dipende_da": [],
     "figura": {
      "mostra": [
       "punto D mobile verso C",
       "area ABGD crescente",
       "segmenti DC successivi a intervalli di tempo uguali"
      ],
      "evidenzia": [
       "aree uguali ↔ DC in progressione geometrica"
      ]
     },
     "nota": "Si suggerisce un cursore del tempo: aree uguali aggiunte a passi uguali; DC si riduce sempre dello stesso fattore (nota N3)."
    }
   ]
  },
  {
   "id": "L2-P3",
   "tipo": "Propositio/Problema",
   "titolo": "Prop. III — salita e discesa verticale con gravità uniforme",
   "copertura": [
    "II.S1.10",
    "II.S1.11",
    "II.S1.12"
   ],
   "fonti": {
    "la": "",
    "en": "Motte 1846, Book II, Sect. I, Prop. III"
   },
   "enunciato": {
    "la": "",
    "it": "Definire il moto di un corpo al quale, mentre sale o scende in linea retta in un mezzo omogeneo, si resiste in rapporto alla velocità, e che è sollecitato da una gravità uniforme.",
    "en": "To define the motion of a body which, in a similar medium, ascends or descends in a right line, and is resisted in the ratio of its velocity, and acted upon by an uniform force of gravity."
   },
   "figura_base": {
    "punti": [
     "A",
     "B",
     "C",
     "H",
     "D",
     "E",
     "G",
     "d",
     "e",
     "g",
     "I",
     "K",
     "F",
     "i",
     "k",
     "f"
    ],
    "vincoli": [
     "CA, CH asintoti perpendicolari; iperbole equilatera per B",
     "BACH rettangolo (AB ⊥ AC, H su CH): AC ∝ gravità (velocità limite)",
     "D, d sul prolungamento di CA oltre A; DE, de ⊥ AC con E, e sulla retta BE parallela ad AC; G, g sull’iperbole",
     "I, i fra A e C; F, f su BH; K, k sull’iperbole sopra I, i",
     "figura 3: K, L, M, N su AC; k, l, m, n su BH; q, r, s, t sull’iperbole",
     "la lettera K ha funzioni diverse nelle figure 2 e 3"
    ]
   },
   "passi": [
    {
     "id": "L2-P3-p1",
     "la": "",
     "it": "Mentre il corpo sale, si rappresenti la gravità con un rettangolo dato qualsiasi BACH, e la resistenza del mezzo all’inizio della salita con il rettangolo BADE, preso dalla parte opposta della retta AB.",
     "en": "The body ascending, let the gravity be expounded by any given rectangle BACH; and the resistance of the medium, at the beginning of the ascent, by the rectangle BADE, taken on the contrary side of the right line AB.",
     "dipende_da": [],
     "figura": {
      "mostra": [
       "rettangolo BACH (gravità)",
       "rettangolo BADE (resistenza iniziale) dall’altra parte di AB"
      ],
      "evidenzia": [
       "BACH ↔ gravità; BADE ↔ resistenza iniziale"
      ]
     },
     "nota": "Figura NATP00088-2."
    },
    {
     "id": "L2-P3-p2",
     "la": "",
     "it": "Con gli asintoti ortogonali AC, CH si descriva per il punto B un’iperbole che tagli le perpendicolari DE, de in G, g: salendo, il corpo nel tempo DGgd descriverà lo spazio EGge; nel tempo DGBA lo spazio dell’intera salita EGB; nel tempo ABKI lo spazio di discesa BFK; e nel tempo IKki lo spazio di discesa KFfk; e le velocità del corpo (proporzionali alla resistenza del mezzo) negli estremi di questi tempi saranno rispettivamente ABED, ABed, nulla, ABFI, ABfi; e la velocità massima che il corpo può acquistare scendendo sarà BACH.",
     "en": "Through the point B, with the rectangular asymptotes AC, CH, describe an hyperbola, cutting the perpendiculars DE, de, in G, g; and the body ascending will in the time DGgd describe the space EGge; in the time DGBA, the space of the whole ascent EGB; in the time ABKI, the space of descent BFK; and in the time IKki the space of descent KFfk; and the velocities of the bodies (proportional to the resistance of the medium) in these periods of time will be ABED, ABed, O, ABFI, ABfi respectively; and the greatest velocity which the body can acquire by descending will be BACH.",
     "dipende_da": [],
     "figura": {
      "mostra": [
       "iperbole per B con asintoti CA, CH",
       "perpendicolari DE, de con G, g",
       "aree-tempo DGgd, DGBA, ABKI, IKki",
       "aree-spazio EGge, EGB, BFK, KFfk"
      ],
      "evidenzia": [
       "tempo = area sotto l’iperbole; spazio = area fra BE (o BF) e l’iperbole; velocità = rettangolo su AB"
      ]
     },
     "nota": "Motte «of the bodies» e «O» per nulla (§ A.7). Costruzione ricostruita in N4."
    },
    {
     "id": "L2-P3-p3",
     "la": "",
     "it": "Si scomponga infatti il rettangolo BACH in innumerevoli rettangoli Ak, Kl, Lm, Mn, ecc., che siano come gli incrementi delle velocità prodotti in altrettanti tempi uguali; nulla, Ak, Al, Am, An, ecc. saranno come le velocità intere, e perciò (per ipotesi) come la resistenza del mezzo all’inizio di ciascuno dei tempi uguali.",
     "en": "For let the rectangle BACH be resolved into innumerable rectangles Ak, Kl, Lm, Mn, &c., which shall be as the increments of the velocities produced in so many equal times; then will 0, Ak, Al, Am, An, &c., be as the whole velocities, and therefore (by supposition) as the resistances of the medium in the beginning of each of the equal times.",
     "dipende_da": [],
     "figura": {
      "mostra": [
       "figura 3: K, L, M, N su AC; k, l, m, n su BH",
       "rettangoli Ak, Kl, Lm, Mn"
      ],
      "evidenzia": [
       "Ak, Al, Am, An come velocità"
      ]
     },
     "nota": "Figura NATP00088-3. *æquali ‹233› um* = *æqualium*, spezzato dal marcatore di pagina."
    },
    {
     "id": "L2-P3-p4",
     "la": "",
     "it": "Si faccia in modo che AC stia ad AK, ossia ABHC ad ABkK, come la forza di gravità sta alla resistenza all’inizio del secondo tempo; e dalla forza di gravità si sottraggano le resistenze: ABHC, KkHC, LlHC, MmHC, ecc. resteranno come le forze assolute dalle quali il corpo è sollecitato all’inizio dei singoli tempi, e perciò (per la Legge II del moto) come gli incrementi delle velocità, cioè come i rettangoli Ak, Kl, Lm, Mn, ecc.; e quindi (per il Lemma I del Libro II) in progressione geometrica.",
     "en": "Make AC to AK, or ABHC to ABkK, as the force of gravity to the resistance in the beginning of the second time; then from the force of gravity subduct the resistances, and ABHC, KkHC, LlHC, MmHC, &c., will be as the absolute forces with which the body is acted upon in the beginning of each of the times, and therefore (by Law I) as the increments of the velocities, that is, as the rectangles Ak, Kl, Lm, Mn, &c., and therefore (by Lem. 1, Book II) in a geometrical progression.",
     "dipende_da": [
      "Legge II",
      "Libro II, Lemma I"
     ],
     "figura": {
      "mostra": [
       "rettangoli residui KkHC, LlHC, MmHC"
      ],
      "evidenzia": [
       "forza assoluta = gravità − resistenza ∝ KC, LC, MC"
      ]
     },
     "nota": "Motte «by Law I»: errore per Legge II (§ A.7)."
    },
    {
     "id": "L2-P3-p5",
     "la": "",
     "it": "Perciò, se le rette Kk, Ll, Mm, Nn, ecc., prolungate, incontrano l’iperbole in q, r, s, t, ecc., le aree ABqK, KqrL, LrsM, MstN, ecc. saranno uguali, e perciò analoghe sia ai tempi sia alle forze di gravità, sempre uguali.",
     "en": "Therefore, if the right lines Kk, Ll, Mm, Nn, &c., are produced so as to meet the hyperbola in q, r, s, t, &c., the areas ABqK, KqrL, LrsM, MstN, &c., will be equal, and therefore analogous to the equal times and equal gravitating forces.",
     "dipende_da": [],
     "figura": {
      "mostra": [
       "punti q, r, s, t sull’iperbole",
       "aree ABqK, KqrL, LrsM, MstN"
      ],
      "evidenzia": [
       "aree uguali sotto l’iperbole ↔ ascisse KC, LC, MC in progressione geometrica"
      ]
     }
    },
    {
     "id": "L2-P3-p6",
     "la": "",
     "it": "Ora l’area ABqK (per il Cor. 3 del Lemma VII e per il Lemma VIII del Libro I) sta all’area Bkq come Kq sta a ½kq, ossia come AC sta a ½AK, cioè come la forza di gravità sta alla resistenza nel mezzo del primo tempo.",
     "en": "But the area ABqK (by Corol. 3, Lem. VII and VIII, Book I) is to the area Bkq as Kq to [SVG 352], or AC to [SVG 353], that is, as the force of gravity to the resistance in the middle of the first time.",
     "dipende_da": [
      "Libro I, Lemma VII, Cor. 3",
      "Libro I, Lemma VIII"
     ],
     "figura": {
      "mostra": [
       "trilineo Bkq",
       "segmento kq"
      ],
      "evidenzia": [
       "ABqK : Bkq → Kq : ½kq (rapporto ultimo)"
      ]
     },
     "nota": "*12kq*, *12AK* = ½kq, ½AK. Rapporto ultimo, verificato in N4. SVG 352, 353 verificate."
    },
    {
     "id": "L2-P3-p7",
     "la": "",
     "it": "E con un argomento simile le aree qKLr, rLMs, sMNt, ecc. stanno alle aree qklr, rlms, smnt, ecc. come le forze di gravità stanno alle resistenze nel mezzo del secondo, del terzo, del quarto tempo, ecc.",
     "en": "And by the like reasoning, the areas qKLr, rLMs, sMNt, &c., are to the areas qklr, rlms, smnt, &c., as the gravitating forces to the resistances in the middle of the second, third, fourth time, and so on.",
     "dipende_da": [],
     "figura": {
      "mostra": [
       "aree qklr, rlms, smnt"
      ],
      "evidenzia": [
       "stesso rapporto per ogni intervallo"
      ]
     }
    },
    {
     "id": "L2-P3-p8",
     "la": "",
     "it": "Di conseguenza, poiché le aree uguali BAKq, qKLr, rLMs, sMNt, ecc. sono analoghe alle forze di gravità, le aree Bkq, qklr, rlms, smnt, ecc. saranno analoghe alle resistenze nel mezzo dei singoli tempi, cioè (per ipotesi) alle velocità, e perciò agli spazi descritti.",
     "en": "Therefore since the equal areas BAKq, qKLr, rLMs, sMNt, &c., are analogous to the gravitating forces, the areas Bkq, qklr, rlms, smnt, &c., will be analogous to the resistances in the middle of each of the times, that is (by supposition), to the velocities, and so to the spaces described.",
     "dipende_da": [],
     "figura": {
      "mostra": [
       "aree Bkq, qklr, rlms, smnt evidenziate"
      ],
      "evidenzia": [
       "area fra BH e iperbole ∝ spazio parziale"
      ]
     }
    },
    {
     "id": "L2-P3-p9",
     "la": "",
     "it": "Si prendano le somme delle quantità analoghe: le aree Bkq, Blr, Bms, Bnt, ecc. saranno analoghe agli spazi interi descritti, e le aree ABqK, ABrL, ABsM, ABtN, ecc. ai tempi.",
     "en": "Take the sums of the analogous quantities, and the areas Bkq, Blr, Bms, Bnt, &c., will be analogous to the whole spaces described; and also the areas ABqK, ABrL, ABsM, ABtN, &c., to the times.",
     "dipende_da": [],
     "figura": {
      "mostra": [
       "aree cumulate Blr, Bms, Bnt",
       "aree cumulate ABrL, ABsM, ABtN"
      ],
      "evidenzia": [
       "spazio totale ↔ area fra BH e iperbole; tempo ↔ area sotto l’iperbole"
      ]
     }
    },
    {
     "id": "L2-P3-p10",
     "la": "",
     "it": "Dunque il corpo, durante la discesa, in un tempo qualsiasi ABrL descrive lo spazio Blr, e nel tempo LrtN lo spazio rlnt. C.V.D.",
     "en": "Therefore the body, in descending, will in any time ABrL describe the space Blr, and in the time LrtN the space rlnt. Q.E.D.",
     "dipende_da": [],
     "figura": {
      "mostra": [
       "area ABrL (tempo) e area Blr (spazio)",
       "area LrtN e area rlnt"
      ],
      "evidenzia": [
       "corrispondenza tempo–spazio"
      ]
     }
    },
    {
     "id": "L2-P3-p11",
     "la": "",
     "it": "E simile è la dimostrazione del moto esposto nella salita. C.V.D.",
     "en": "And the like demonstration holds in ascending motion.",
     "dipende_da": [],
     "figura": {
      "mostra": [
       "figura 2: lato della salita (D, d, E, e)"
      ],
      "evidenzia": [
       "stessa costruzione con DC al posto di IC"
      ]
     },
     "nota": "Motte omette il secondo Q.E.D."
    }
   ]
  },
  {
   "id": "L2-P4",
   "tipo": "Propositio/Problema",
   "titolo": "Prop. IV — il proiettile con resistenza proporzionale alla velocità",
   "copertura": [
    "II.S1.17",
    "II.S1.18",
    "II.S1.19"
   ],
   "fonti": {
    "la": "",
    "en": "Motte 1846, Book II, Sect. I, Prop. IV"
   },
   "enunciato": {
    "la": "",
    "it": "Posto che la forza di gravità in un mezzo omogeneo sia uniforme e tenda perpendicolarmente al piano dell’orizzonte, definire il moto di un proiettile che in quel mezzo subisce una resistenza proporzionale alla velocità.",
    "en": "Supposing the force of gravity in any similar medium to be uniform, and to tend perpendicularly to the plane of the horizon; to define the motion of a projectile therein, which suffers resistance proportional to its velocity."
   },
   "figura_base": {
    "punti": [
     "D",
     "P",
     "C",
     "A",
     "G",
     "B",
     "K",
     "Q",
     "E",
     "H",
     "R",
     "T",
     "I",
     "t",
     "V",
     "r",
     "a",
     "F",
     "L",
     "N"
    ],
    "vincoli": [
     "DC orizzontale, PC ⊥ DC; DP = velocità iniziale (in scala DC = u0/c, CP = w0/c)",
     "A su DC con DA : AC = c·w0 : g",
     "iperbole GTBS: y·RC = costante (asintoti DC, CP)",
     "DGKC parallelogramma; Q = GK ∩ AB (AQ = DG)",
     "E su DG con DE = AB; EH ∥ DC per B (ricostruito)",
     "N = QB·DC/CP (segmento ausiliario)",
     "R su DC; T, I, t, V su RT; Rr = (DR·AB − RDGT)/N",
     "L = intersezione della tangente in r con PC",
     "F = intersezione di DraF con DC"
    ]
   },
   "passi": [
    {
     "id": "L2-P4-p1",
     "la": "",
     "it": "Da un luogo qualsiasi D esca il proiettile lungo una linea retta qualsiasi DP, e con la lunghezza DP si rappresenti la sua velocità all’inizio del moto.",
     "en": "Let the projectile go from any place D in the direction of any right line DP, and let its velocity at the beginning of the motion be expounded by the length DP.",
     "dipende_da": [],
     "figura": {
      "mostra": [
       "D",
       "retta DP"
      ],
      "evidenzia": [
       "DP ∝ velocità iniziale"
      ]
     },
     "nota": "*Eloco* = *E loco* (refuso probabile). Figura NATP00088-4."
    },
    {
     "id": "L2-P4-p2",
     "la": "",
     "it": "Dal punto P si abbassi sulla linea orizzontale DC la perpendicolare PC, e si tagli DC in A in modo che DA stia ad AC come la resistenza del mezzo, nata all’inizio dal moto verso l’alto, sta alla forza di gravità; oppure (il che è lo stesso) in modo che il rettangolo di DA e DP stia al rettangolo di AC e CP come la resistenza totale all’inizio del moto sta alla forza di gravità.",
     "en": "From the point P let fall the perpendicular PC on the horizontal line DC, and cut DC in A, so that DA may be to AC as the resistance of the medium arising from the motion upwards at the beginning to the force of gravity; or (which comes to the same) so that the rectangle under DA and DP may be to that under AC and CP as the whole resistance at the beginning of the motion to the force of gravity.",
     "dipende_da": [],
     "figura": {
      "mostra": [
       "orizzontale DC",
       "perpendicolare PC",
       "punto A su DC"
      ],
      "evidenzia": [
       "DA : AC = resistenza verticale iniziale : gravità"
      ]
     }
    },
    {
     "id": "L2-P4-p3",
     "la": "",
     "it": "Con gli asintoti DC, CP si descriva un’iperbole qualsiasi GTBS, che tagli le perpendicolari DG, AB in G e B; e si completi il parallelogramma DGKC, il cui lato GK tagli AB in Q.",
     "en": "With the asymptotes DC, CP describe any hyperbola GTBS cutting the perpendiculars DG, AB in G and B; complete the parallelogram DGKC, and let its side GK cut AB in Q.",
     "dipende_da": [],
     "figura": {
      "mostra": [
       "iperbole GTBS con asintoti DC, CP",
       "G, B",
       "parallelogramma DGKC",
       "Q = GK ∩ AB"
      ],
      "evidenzia": [
       "AQ = DG"
      ]
     }
    },
    {
     "id": "L2-P4-p4",
     "la": "",
     "it": "Si prenda una linea N che stia a QB nel rapporto in cui DC sta a CP; e, innalzata in un punto qualsiasi R della retta DC la perpendicolare RT, che incontri l’iperbole in T e le rette EH, GK, DP in I, t e V, su di essa si prenda Vr uguale a tGT/N, o, il che è lo stesso, si prenda Rr uguale a GTIE/N: il proiettile nel tempo DRTG giungerà al punto r, descrivendo la linea curva DraF, sulla quale si trova sempre il punto r; giungerà all’altezza massima a sulla perpendicolare AB, e poi si avvicinerà sempre all’asintoto PC.",
     "en": "Take a line N in the same ratio to QB as DC is in to CP; and from any point R of the right line DC erect RT perpendicular to it, meeting the hyperbola in T, and the right lines EH, GK, DP in I, t, and V; in that perpendicular take Vr equal to [SVG 354], or which is the same thing, take Rr equal to [SVG 355]; and the projectile in the time DRTG will arrive at the point r describing the curve line DraF, the locus of the point r; thence it will come to its greatest height a in the perpendicular AB; and afterwards ever approach to the asymptote PC.",
     "dipende_da": [],
     "figura": {
      "mostra": [
       "R mobile su DC",
       "RT con T, I, t, V",
       "retta EH (altezza AB)",
       "punto r",
       "curva DraF",
       "vertice a su AB",
       "asintoto PC"
      ],
      "evidenzia": [
       "tempo = area RDGT; Rr = GTIE/N"
      ]
     },
     "nota": "Frazioni appiattite: *tGTN* = tGT/N, *GTIEN* = GTIE/N. EH non è definita nel testo (§ A.5). SVG 354, 355 verificate."
    },
    {
     "id": "L2-P4-p5",
     "la": "",
     "it": "E la sua velocità in un punto qualsiasi r è come la tangente della curva rL. C.V.T.",
     "en": "And its velocity in any point r will be as the tangent rL to the curve. Q.E.I.",
     "dipende_da": [],
     "figura": {
      "mostra": [
       "tangente in r fino a L su PC"
      ],
      "evidenzia": [
       "rL ∝ velocità"
      ]
     },
     "nota": "L ricostruito sull’asintoto PC; verificato in N7."
    },
    {
     "id": "L2-P4-p6",
     "la": "",
     "it": "Infatti N sta a QB come DC sta a CP, ossia come DR sta a RV; e perciò RV è uguale a DR×QB/N, e Rr (cioè RV − Vr, ossia (DR×QB − tGT)/N) è uguale a (DR×AB − RDGT)/N.",
     "en": "For N is to QB as DC to CP or DR to RV, and therefore RV is equal to [SVG 356], and Rr [SVG 357] is equal to [SVG 358].",
     "dipende_da": [],
     "figura": {
      "mostra": [
       "triangoli simili DRV, DCP",
       "RV, Vr, Rr"
      ],
      "evidenzia": [
       "Rr = (DR×AB − RDGT)/N"
      ]
     },
     "nota": "Letture § A.8. SVG 357 e 358 verificate; SVG 356 errata in Motte: (DR×QB − tGT)/N invece di DR×QB/N."
    },
    {
     "id": "L2-P4-p7",
     "la": "",
     "it": "Si rappresenti ora il tempo con l’area RDGT e (per il Cor. II delle leggi) si distingua il moto del corpo in due, uno di salita, l’altro laterale.",
     "en": "Now let the time be expounded by the area RDGT and (by Laws, Cor. 2), distinguish the motion of the body into two others, one of ascent, the other lateral.",
     "dipende_da": [
      "Leggi, Cor. II"
     ],
     "figura": {
      "mostra": [
       "area RDGT (tempo)",
       "componenti orizzontale e verticale"
      ],
      "evidenzia": [
       "scomposizione del moto"
      ]
     }
    },
    {
     "id": "L2-P4-p8",
     "la": "",
     "it": "E poiché la resistenza è come il moto, anch’essa si distinguerà in due parti, proporzionali e contrarie alle parti del moto: perciò la lunghezza descritta dal moto laterale sarà (per la Prop. II di questo Libro) come la linea DR, e l’altezza invece (per la Prop. III di questo Libro) come l’area DR×AB − RDGT, cioè come la linea Rr.",
     "en": "And since the resistance is as the motion, let that also be distinguished into two parts proportional and contrary to the parts of the motion: and therefore the length described by the lateral motion will be (by Prop. II, Book II) as the line DR, and the height (by Prop. III, Book II) as the area DR × AB - RDGT, that is, as the line Rr.",
     "dipende_da": [
      "Libro II, Prop. II",
      "Libro II, Prop. III"
     ],
     "figura": {
      "mostra": [
       "DR (lunghezza)",
       "Rr (altezza)"
      ],
      "evidenzia": [
       "orizzontale: Prop. II; verticale: Prop. III"
      ]
     }
    },
    {
     "id": "L2-P4-p9",
     "la": "",
     "it": "Proprio all’inizio del moto, poi, l’area RDGT è uguale al rettangolo DR×AQ; e perciò quella linea Rr (ossia (DR×AB − DR×AQ)/N) sta allora a DR come AB − AQ, ossia QB, sta a N, cioè come CP sta a DC, e quindi come il moto in altezza sta al moto in lunghezza all’inizio.",
     "en": "But in the very beginning of the motion the area RDGT is equal to the rectangle DR × AQ, and therefore that line Rr [SVG 359] will then be to DR as AB - AQ or QB to N, that is, as CP to DC; and therefore as the motion upwards to the motion lengthwise at the beginning.",
     "dipende_da": [],
     "figura": {
      "mostra": [
       "R vicinissimo a D",
       "rettangolo DR×AQ"
      ],
      "evidenzia": [
       "Rr : DR = CP : DC all’inizio: la curva parte tangente a DP"
      ]
     },
     "nota": "Parentesi aperta mancante prima di *AB−AQ*; SVG 359 verificate."
    },
    {
     "id": "L2-P4-p10",
     "la": "",
     "it": "Poiché dunque Rr è sempre come l’altezza, e DR sempre come la lunghezza, e Rr sta a DR all’inizio come l’altezza sta alla lunghezza, è necessario che Rr stia sempre a DR come l’altezza sta alla lunghezza, e perciò che il corpo si muova lungo la linea DraF, sulla quale si trova continuamente il punto r. C.V.D.",
     "en": "Since, therefore, Rr is always as the height, and DR always as the length, and Rr is to DR at the beginning as the height to the length, it follows, that Rr is always to DR as the height to the length; and therefore that the body will move in the line DraF, which is the locus of the point r. Q.E.D.",
     "dipende_da": [],
     "figura": {
      "mostra": [
       "curva DraF completa"
      ],
      "evidenzia": [
       "la scala delle due componenti coincide: r è la posizione del corpo"
      ]
     }
    }
   ]
  },
  {
   "id": "L2-P4-Cor1",
   "tipo": "Corollarium",
   "titolo": "Prop. IV, Cor. 1 — Xr proporzionale al tempo",
   "copertura": [
    "II.S1.20"
   ],
   "fonti": {
    "la": "",
    "en": "Motte 1846, Book II, Sect. I, Prop. IV, Cor. 1"
   },
   "enunciato": {
    "la": "",
    "it": "Rr è dunque uguale a DR×AB/N − RDGT/N; e perciò, se si prolunga RT fino a X in modo che RX sia uguale a DR×AB/N (cioè, se si completa il parallelogramma ACPY, si congiunge DY, che taglia CP in Z, e si prolunga RT finché incontra DY in X), Xr sarà uguale a RDGT/N, e perciò proporzionale al tempo.",
    "en": "Therefore Rr is equal to [SVG 360]; and therefore if RT be produced to X so that RX may be equal to [SVG 361], that is, if the parallelogram ACPY be completed, and DY cutting CP in Z be drawn, and RT be produced till it meets DY in X; Xr will be equal to [SVG 362], and therefore proportional to the time."
   },
   "figura_base": {
    "punti": [
     "A",
     "C",
     "P",
     "Y",
     "D",
     "Z",
     "R",
     "X",
     "r"
    ],
    "vincoli": [
     "ACPY parallelogramma (Y sopra A, AY = CP)",
     "Z = DY ∩ CP",
     "X = RT ∩ DY; RX = DR·CP/DA = DR·AB/N (perché QB·DC = AB·DA)"
    ]
   },
   "passi": [
    {
     "id": "L2-P4-Cor1-p1",
     "la": "",
     "it": "Rr è dunque uguale a DR×AB/N − RDGT/N; e perciò, se si prolunga RT fino a X in modo che RX sia uguale a DR×AB/N (cioè, se si completa il parallelogramma ACPY, si congiunge DY, che taglia CP in Z, e si prolunga RT finché incontra DY in X), Xr sarà uguale a RDGT/N, e perciò proporzionale al tempo.",
     "en": "Therefore Rr is equal to [SVG 360]; and therefore if RT be produced to X so that RX may be equal to [SVG 361], that is, if the parallelogram ACPY be completed, and DY cutting CP in Z be drawn, and RT be produced till it meets DY in X; Xr will be equal to [SVG 362], and therefore proportional to the time.",
     "dipende_da": [],
     "figura": {
      "mostra": [
       "parallelogramma ACPY",
       "retta DY e punto Z",
       "X su DY",
       "segmento Xr"
      ],
      "evidenzia": [
       "Xr = RDGT/N ∝ tempo"
      ]
     },
     "nota": "Corollario di una sola frase: un solo passo, uguale all’enunciato. Identità QB·DC = AB·DA verificata in N7; SVG 360–362 verificate."
    }
   ]
  },
  {
   "id": "L2-P4-Cor2",
   "tipo": "Corollarium",
   "titolo": "Prop. IV, Cor. 2 — la curva per mezzo dei logaritmi",
   "copertura": [
    "II.S1.21"
   ],
   "fonti": {
    "la": "",
    "en": "Motte 1846, Book II, Sect. I, Prop. IV, Cor. 2"
   },
   "enunciato": {
    "la": "",
    "it": "Di qui, se si prendono innumerevoli CR, o, il che è lo stesso, innumerevoli ZX, in progressione geometrica, altrettante Xr saranno in progressione aritmetica.",
    "en": "Whence if innumerable lines CR, or, which is the same, innumerable lines ZX, be taken in a geometrical progression, there will be as many lines Xr in an arithmetical progression."
   },
   "figura_base": {
    "punti": [
     "C",
     "R",
     "Z",
     "X",
     "r",
     "D",
     "F"
    ],
    "vincoli": [
     "CR in progressione geometrica (per esempio DC, DC/2, DC/4…)",
     "ZX ∝ CR (X su DZ)",
     "Xr = RDGT/N in progressione aritmetica"
    ]
   },
   "passi": [
    {
     "id": "L2-P4-Cor2-p1",
     "la": "",
     "it": "Di qui, se si prendono innumerevoli CR, o, il che è lo stesso, innumerevoli ZX, in progressione geometrica, altrettante Xr saranno in progressione aritmetica.",
     "en": "Whence if innumerable lines CR, or, which is the same, innumerable lines ZX, be taken in a geometrical progression, there will be as many lines Xr in an arithmetical progression.",
     "dipende_da": [],
     "figura": {
      "mostra": [
       "punti R con CR in progressione geometrica",
       "segmenti Xr corrispondenti"
      ],
      "evidenzia": [
       "CR geometrica ↔ Xr aritmetica"
      ]
     },
     "nota": "Verificato in N7 (Xr = 0; 18,869; 37,738; 56,607)."
    },
    {
     "id": "L2-P4-Cor2-p2",
     "la": "",
     "it": "E di qui la curva DraF si traccia facilmente per mezzo della tavola dei logaritmi.",
     "en": "And hence the curve DraF is easily delineated by the table of logarithms.",
     "dipende_da": [],
     "figura": {
      "mostra": [
       "punti r = X − Xr",
       "curva DraF tracciata per punti"
      ],
      "evidenzia": [
       "Xr ∝ log(DC/CR)"
      ]
     }
    }
   ]
  },
  {
   "id": "L2-P4-Cor3",
   "tipo": "Corollarium",
   "titolo": "Prop. IV, Cor. 3 — la parabola con la stessa velocità iniziale",
   "copertura": [
    "II.S1.22"
   ],
   "fonti": {
    "la": "",
    "en": "Motte 1846, Book II, Sect. I, Prop. IV, Cor. 3"
   },
   "enunciato": {
    "la": "",
    "it": "Se si costruisce una parabola con vertice D, con il diametro DG prolungato verso il basso e con un lato retto che stia a 2DP come la resistenza totale proprio all’inizio del moto sta alla forza di gravità, la velocità con cui il corpo deve uscire dal luogo D lungo la retta DP per descrivere in un mezzo uniforme resistente la curva DraF sarà proprio quella con cui deve uscire dallo stesso luogo D, lungo la stessa retta DP, per descrivere la parabola in uno spazio non resistente.",
    "en": "If a parabola be constructed to the vertex D, and the diameter DG produced downwards, and its latus rectum is to 2 DP as the whole resistance at the beginning of the notion to the gravitating force, the velocity with which the body ought to go from the place D, in the direction of the right line DP, so as in an uniform resisting medium to describe the curve DraF, will be the same as that with which it ought to go from the same place D in the direction of the same right line DP, so as to describe a parabola in a non-resisting medium."
   },
   "figura_base": {
    "punti": [
     "D",
     "G",
     "P",
     "V",
     "r",
     "R",
     "T",
     "t",
     "K",
     "C",
     "Q",
     "B",
     "A"
    ],
    "vincoli": [
     "parabola con vertice D, diametro DG verticale, tangente DP",
     "lato retto L = 2DP·(resistenza : gravità) = 2DP²·DA/(AC·CP)",
     "tangente all’iperbole in G parallela a DK",
     "R → D: DV²/Vr → L"
    ]
   },
   "passi": [
    {
     "id": "L2-P4-Cor3-p1",
     "la": "",
     "it": "Infatti il lato retto di questa parabola, proprio all’inizio del moto, è DV²/Vr; e Vr è tGT/N, ossia DR×Tt/2N.",
     "en": "For the latus rectum of this parabola, at the very beginning of the motion, is [SVG 363]; and Vr is [SVG 354] or [SVG 364].",
     "dipende_da": [],
     "figura": {
      "mostra": [
       "V su DP vicino a D",
       "Vr (scarto verticale dalla tangente)",
       "trilineo tGT ≈ triangolo ½·DR·Tt"
      ],
      "evidenzia": [
       "lato retto = DV²/Vr (rapporto ultimo)"
      ]
     },
     "nota": "*DV quad.Vr* = DV²/Vr; *DR×Tt2N* = DR×Tt/2N. SVG 363, 354, 364 verificate."
    },
    {
     "id": "L2-P4-Cor3-p2",
     "la": "",
     "it": "Ora la retta che, se fosse condotta, toccherebbe l’iperbole GTS in G è parallela a DK; e perciò Tt è CK×DR/DC, e N era QB×DC/CP.",
     "en": "But a right line, which, if drawn, would touch the hyperbola GTS in G, is parallel to DK, and therefore Tt is [SVG 365], and N is [SVG 366].",
     "dipende_da": [],
     "figura": {
      "mostra": [
       "tangente all’iperbole in G",
       "diagonale DK"
      ],
      "evidenzia": [
       "tangente in G ∥ DK"
      ]
     },
     "nota": "Pendenze verificate uguali in N7. SVG 365, 366 verificate."
    },
    {
     "id": "L2-P4-Cor3-p3",
     "la": "",
     "it": "E perciò Vr è DR²×CK×CP/(2DC²×QB), cioè (poiché DR e DC, DV e DP sono proporzionali) DV²×CK×CP/(2DP²×QB); e il lato retto DV²/Vr risulta 2DP²×QB/(CK×CP), cioè (poiché QB e CK, DA e AC sono proporzionali) 2DP²×DA/(AC×CP), e perciò sta a 2DP come DP×DA sta a CP×AC, cioè come la resistenza sta alla gravità. C.V.D.",
     "en": "And therefore Vr is equal to [SVG 367], that is (because DR and DC, DV and DP are proportionals), to [SVG 368]; and the latus rectum [SVG 363] comes out [SVG 369], that is (because QB and CK, DA and AC are proportional), [SVG 370], and therefore is to 2DP as DP × DA to CP × AC; that is, as the resistance to the gravity. Q.E.D.",
     "dipende_da": [],
     "figura": {
      "mostra": [
       "parabola nel vuoto con la stessa velocità iniziale",
       "curva DraF"
      ],
      "evidenzia": [
       "le due curve hanno in D la stessa tangente e la stessa curvatura iniziale"
      ]
     },
     "nota": "Letture § A.8; limite verificato in N7 (42,447 → 42,449). SVG 367–370 verificate."
    }
   ]
  },
  {
   "id": "L2-P4-Cor7",
   "tipo": "Corollarium",
   "titolo": "Prop. IV, Cor. 7 — determinare la resistenza dalle gittate",
   "copertura": [
    "II.S1.26"
   ],
   "fonti": {
    "la": "",
    "en": "Motte 1846, Book II, Sect. I, Prop. IV, Cor. 7"
   },
   "enunciato": {
    "la": "",
    "it": "Di qui risulta chiaro il metodo per determinare la curva DraF dai fenomeni con ottima approssimazione, e per ricavarne la resistenza e la velocità con cui il corpo è lanciato.",
    "en": "Hence appears the method of determining the curve DraF nearly from the phenomena, and thence collecting the resistance and velocity with which the body is projected."
   },
   "figura_base": {
    "punti": [
     "D",
     "P",
     "p",
     "C",
     "F",
     "f",
     "S",
     "M",
     "N",
     "X"
    ],
    "vincoli": [
     "due lanci da D con la stessa velocità, angoli CDP, CDp",
     "F, f punti di caduta su DC",
     "grafico ausiliario: ascisse SM (rapporti di prova), ordinate MN (differenze)",
     "X zero della curva NNN"
    ]
   },
   "passi": [
    {
     "id": "L2-P4-Cor7-p1",
     "la": "",
     "it": "Si lancino due corpi simili e uguali con la stessa velocità dal luogo D, sotto angoli diversi CDP, CDp, e si conoscano i luoghi F, f in cui cadono sul piano orizzontale DC.",
     "en": "Let two similar and equal bodies be projected with the same velocity, from the place D, in different angles CDP, CDp; and let the places F, f, where they fall upon the horizontal plane DC, be known.",
     "dipende_da": [],
     "figura": {
      "mostra": [
       "due traiettorie da D con angoli CDP, CDp",
       "punti di caduta F, f"
      ],
      "evidenzia": [
       "dati sperimentali: DF, Df"
      ]
     }
    },
    {
     "id": "L2-P4-Cor7-p2",
     "la": "",
     "it": "Poi, presa una lunghezza qualsiasi per DP o Dp, si supponga che la resistenza in D stia alla gravità in un rapporto qualsiasi, e si rappresenti quel rapporto con una lunghezza qualsiasi SM.",
     "en": "Then taking any length for DP or Dp suppose the resistance in D to be to the gravity in any ratio whatsoever, and let that ratio be expounded by any length SM.",
     "dipende_da": [],
     "figura": {
      "mostra": [
       "grafico ausiliario: retta S M"
      ],
      "evidenzia": [
       "SM = rapporto di prova resistenza : gravità"
      ]
     },
     "nota": "Figura NATP00088-7 (grafico ausiliario)."
    },
    {
     "id": "L2-P4-Cor7-p3",
     "la": "",
     "it": "Quindi, per mezzo del calcolo, dalla lunghezza DP così assunta si trovino le lunghezze DF, Df; e dal rapporto Ff/DF trovato con il calcolo si sottragga lo stesso rapporto trovato con l’esperimento, e si rappresenti la differenza con la perpendicolare MN.",
     "en": "Then, by computation, from that assumed length DP, find the lengths DF, Df; and from the ratio [SVG 371], found by calculation, subduct the same ratio as found by experiment; and let the difference be expounded by the perpendicular MN.",
     "dipende_da": [],
     "figura": {
      "mostra": [
       "DF, Df calcolati",
       "perpendicolare MN"
      ],
      "evidenzia": [
       "MN = (Ff/DF) calcolato − (Ff/DF) sperimentale"
      ]
     },
     "nota": "*FfDF* = Ff/DF; SVG 371 verificate."
    },
    {
     "id": "L2-P4-Cor7-p4",
     "la": "",
     "it": "Fa’ lo stesso una seconda e una terza volta, assumendo sempre un nuovo rapporto SM della resistenza alla gravità e ricavando una nuova differenza MN.",
     "en": "Repeat the same a second and a third time, by assuming always a new ratio SM of the resistance to the gravity, and collecting a new difference MN.",
     "dipende_da": [],
     "figura": {
      "mostra": [
       "tre punti M con le loro MN"
      ],
      "evidenzia": [
       "tentativi successivi"
      ]
     }
    },
    {
     "id": "L2-P4-Cor7-p5",
     "la": "",
     "it": "Si portino poi le differenze positive da una parte della retta SM e le negative dall’altra; e per i punti N, N, N si conduca una curva regolare NNN che tagli la retta SMMM in X: SX sarà il vero rapporto della resistenza alla gravità, che si doveva trovare.",
     "en": "Draw the affirmative differences on one side of the right line SM, and the negative on the other side; and through the points N, N, N, draw a regular curve NNN, cutting the right line SMMM in X, and SX will be the true ratio of the resistance to the gravity, which was to be found.",
     "dipende_da": [],
     "figura": {
      "mostra": [
       "curva NNN",
       "punto X"
      ],
      "evidenzia": [
       "SX = rapporto vero (zero della differenza)"
      ]
     }
    },
    {
     "id": "L2-P4-Cor7-p6",
     "la": "",
     "it": "Da questo rapporto si deve ricavare con il calcolo la lunghezza DF; e la lunghezza che sta alla lunghezza assunta DP come la lunghezza DF conosciuta per esperimento sta alla lunghezza DF appena trovata sarà la vera lunghezza DP.",
     "en": "From this ratio the length DF is to be collected by calculation; and a length, which is to the assumed length DP as the length DF known by experiment to the length DF just now found, will be the true length DP.",
     "dipende_da": [],
     "figura": {
      "mostra": [
       "DF calcolato con SX",
       "DP corretto in scala"
      ],
      "evidenzia": [
       "DP vero = DP assunto × DF sperimentale / DF calcolato"
      ]
     }
    },
    {
     "id": "L2-P4-Cor7-p7",
     "la": "",
     "it": "Trovata questa, si hanno sia la linea curva DraF che il corpo descrive, sia la velocità e la resistenza del corpo nei singoli luoghi.",
     "en": "This being known, you will have both the curve line DraF which the body describes, and also the velocity and resistance of the body in each place.",
     "dipende_da": [],
     "figura": {
      "mostra": [
       "curva DraF definitiva"
      ],
      "evidenzia": [
       "traiettoria, velocità e resistenza determinate"
      ]
     }
    }
   ]
  }
 ]
}
```
