> **Copia pubblica.** In questa versione i campi `"la"` della Parte B sono vuoti: le frasi latine vengono dalla trascrizione del Newton Project, che non si ridistribuisce. Il latino del 1726 si legge su newtonproject.ox.ac.uk.

# Isaac Newton
# Principi matematici della filosofia naturale

## Fascicolo 4 — Libro I, Sezione I: il metodo dei rapporti primi e ultimi

**Nuova traduzione italiana di lavoro dal latino del 1726, confrontata con l’inglese di Andrew Motte nell’edizione del 1846.**

Versione 0.1 — 8 novembre 2026. Preparata con Claude (Anthropic) per Massimo Bosetti.

### Stato e perimetro

Questo fascicolo prosegue il Fascicolo 3 (*Assiomi, ovvero leggi del moto*). Traduce integralmente l’intestazione del Libro I (*De motu corporum liber primus*) e la **Sezione I**, *De methodo rationum primarum & ultimarum*: i Lemmi I–XI con i loro corollari, lo Scolio dopo il Lemma X (sul linguaggio delle proporzionalità) e il lungo Scolio finale della Sezione (angoli di contatto, metodo dei limiti, obiezioni). Si ferma prima della Sezione II (*De inventione virium centripetarum*). È una traduzione di lavoro, non un’edizione critica validata.

Gli identificatori **S1.01–S1.48** e i titoli tematici tra parentesi sono aggiunte editoriali. I numeri romani dei lemmi e i numeri arabi dei corollari e dei casi appartengono al testo originale. Le integrazioni del curatore sono tra parentesi quadre. Le note poste dopo la traduzione non fanno parte del testo di Newton.

In coda al fascicolo, la **Parte B** contiene i dati strutturati per le pagine interattive dei lemmi che hanno figura e dimostrazione geometrica (Lemmi II, III, IV, VI, VII con il Cor. 1, VIII, IX, X, XI con il Cor. 4).

### Fonti effettivamente consultate

1. **Latino di riferimento.** Isaac Newton, *Philosophiæ Naturalis Principia Mathematica*, terza edizione, Londra, 1726, Libro I, Sezione I, pp. 28–38. Trascrizione normalizzata del Newton Project, documento **NATP00087** (<https://www.newtonproject.ox.ac.uk/view/texts/normalized/NATP00087>), estratta in testo semplice senza correzioni nel file di lavoro `fonti/latino-1726-L1-S01.md`. Le pagine sono quelle segnate nella trascrizione con i numeri tra parentesi angolari.
2. **Inglese di confronto.** *Newton’s Principia. The Mathematical Principles of Natural Philosophy*, traduzione di Andrew Motte, New York, Daniel Adee, 1846, Book I, Section I, **pp. 95–103** secondo i marcatori di pagina dell’EPUB Project Gutenberg n. 76404 (file `76404-h-10.htm.xhtml`). Estratto di lavoro: `fonti/motte-1846-L1-S01.md`. Le formule che l’EPUB stampa come immagini ([SVG 1]–[SVG 27]) sono state lette dagli attributi `data-tex` del file XHTML e, per le quattro decisive (SVG 1, 3, 13, 19), anche sull’immagine resa con `rsvg-convert`.
3. **Fascicoli 1–3** del progetto e brief comune del Libro I, per il formato, i criteri e il glossario.

Non ho consultato la stampa del 1726, né le figure NATP00087-1…8, né traduzioni moderne (Cajori, Cohen–Whitman, Pala, Giudice). Le relazioni geometriche sono ricostruite soltanto dalle lettere citate nel testo.

### Criteri di traduzione

- Il testo guida è il latino; si traduce frase per frase, senza omissioni. Motte serve per il confronto ed è annotato quando aggiunge, omette o sbaglia.
- Italiano contemporaneo, con la struttura argomentativa e il lessico storico: i rapporti restano rapporti («rapporto duplicato», «triplicato», «sesquiplicato»), e le formule moderne stanno solo nelle note.
- Si applica il **glossario comune** del brief del Libro I e dei Fascicoli 1–3. In particolare: *ratio prima / ultima* «rapporto primo / ultimo»; *quantitates evanescentes / nascentes* «quantità evanescenti / nascenti»; *ultimo* (avverbio) «alla fine»; *constanter* (Lemma I) «senza interruzione», per decisione del curatore; *subtensa* «sottesa»; *chorda* «corda»; *sinus* «seno»; *sagitta* «saetta»; *angulus contactus* «angolo di contatto»; *positione datus* «dato di posizione»; *ordinatim applicata* «ordinata»; *abscissa* «ascissa»; *particula* «particella»; *conjunctim* «considerate congiuntamente»; *directe / inverse* «direttamente / inversamente»; *urgere* «sollecitare» (per le forze); *quam proxime* «con ottima approssimazione» (come nel Fascicolo 3); *Cas.* «Caso»; *Corol.* «Cor.»; Q.E.D. «C.V.D.».
- Gli enunciati dei lemmi sono in grassetto. Quelli con *dico quod* restano in prima persona («dico che»), come nel latino.
- Notazione: *AB quad.* è scritto AB²; *AD3* è AD³. Gli **esponenti frazionari** della serie dello Scolio finale, che la trascrizione appiattisce («AD32» per AD elevato a 3/2), sono scritti con cifre in apice e barra: AD³/² significa «AD elevato alla potenza 3/2», non «AD³ diviso 2». La lettura è dichiarata nel § A.12 e verificata nella nota N11.
- Le lettere delle figure restano come nel latino, minuscole comprese. La lettera **J** del Lemma XI e dello Scolio è riprodotta come nella trascrizione.
- Le estensioni del glossario proprie di questo fascicolo sono nel § A.0.

---

## Traduzione italiana

### Del moto dei corpi. Libro primo

### Sezione I. Del metodo dei rapporti primi e ultimi, con il cui aiuto si dimostra ciò che segue

### Lemma I (uguaglianza ultima)

**[S1.01]** **Le quantità, come pure i rapporti di quantità, che in un tempo finito qualsiasi tendono senza interruzione all’uguaglianza, e prima della fine di quel tempo si avvicinano l’una all’altra più di qualunque differenza data, diventano alla fine uguali.**

**[S1.02]** Se lo neghi, diventino alla fine disuguali, e sia D la loro differenza ultima. Dunque non possono avvicinarsi all’uguaglianza più della differenza data D: contro l’ipotesi.

### Lemma II (figura inscritta e circoscritta: basi uguali)

**[S1.03]** **Se in una figura qualsiasi AacE, compresa fra le rette Aa, AE e la curva acE, si inscrivono quanti si vogliano parallelogrammi Ab, Bc, Cd, ecc., contenuti sotto basi uguali AB, BC, CD, ecc. e sotto lati Bb, Cc, Dd, ecc. paralleli al lato Aa della figura; e si completano i parallelogrammi aKbl, bLcm, cMdn, ecc.; e poi la larghezza di questi parallelogrammi diminuisce e il loro numero aumenta all’infinito: dico che i rapporti ultimi che hanno fra loro la figura inscritta AKbLcMdD, la circoscritta AalbmcndoE e la curvilinea AabcdE sono rapporti di uguaglianza.**

**[S1.04]** Infatti la differenza fra la figura inscritta e la circoscritta è la somma dei parallelogrammi Kl, Lm, Mn, Do, cioè (poiché le basi di tutti sono uguali) il rettangolo compreso sotto la base Kb di uno solo di essi e la somma delle altezze Aa, cioè il rettangolo ABla. Ma questo rettangolo, poiché la sua larghezza AB diminuisce all’infinito, diventa minore di qualunque grandezza data. Dunque (per il Lemma I) la figura inscritta e la circoscritta, e a maggior ragione la figura curvilinea intermedia, diventano alla fine uguali. C.V.D.

### Lemma III (basi disuguali)

**[S1.05]** **Gli stessi rapporti ultimi sono ancora rapporti di uguaglianza quando le larghezze AB, BC, CD, ecc. dei parallelogrammi sono disuguali e diminuiscono tutte all’infinito.**

**[S1.06]** Sia infatti AF uguale alla larghezza massima, e si completi il parallelogramma FAaf. Questo sarà maggiore della differenza fra la figura inscritta e la figura circoscritta; ma, diminuita all’infinito la sua larghezza AF, diventerà minore di qualunque rettangolo dato. C.V.D.

**[S1.07]** Cor. 1. Di qui la somma ultima dei parallelogrammi evanescenti coincide in ogni sua parte con la figura curvilinea.

**[S1.08]** Cor. 2. E a maggior ragione la figura rettilinea compresa fra le corde ab, bc, cd, ecc. degli archi evanescenti coincide alla fine con la figura curvilinea.

**[S1.09]** Cor. 3. Come pure la figura rettilinea circoscritta, compresa fra le tangenti degli stessi archi.

**[S1.10]** Cor. 4. E perciò queste figure ultime (quanto ai perimetri acE) non sono rettilinee, ma limiti curvilinei di figure rettilinee.

### Lemma IV (rapporto di due figure)

**[S1.11]** **Se in due figure AacE, PprT si inscrivono (come sopra) due serie di parallelogrammi, e il numero è lo stesso in entrambe, e, quando le larghezze diminuiscono all’infinito, i rapporti ultimi dei parallelogrammi dell’una figura ai parallelogrammi dell’altra, ciascuno al corrispondente, sono gli stessi: dico che le due figure AacE, PprT stanno fra loro in quello stesso rapporto.**

**[S1.12]** Infatti, come i parallelogrammi stanno uno per uno ai parallelogrammi, così (componendo) la somma di tutti sta alla somma di tutti, e così la figura alla figura; poiché, beninteso, la prima figura sta alla prima somma (per il Lemma III), e la seconda figura alla seconda somma, in rapporto di uguaglianza. C.V.D.

**[S1.13]** Cor. Di qui, se due quantità di genere qualsiasi sono divise in un modo qualunque nello stesso numero di parti, e quelle parti, quando il loro numero aumenta e la loro grandezza diminuisce all’infinito, hanno fra loro un rapporto dato, la prima alla prima, la seconda alla seconda e le altre ordinatamente alle altre, le quantità intere staranno fra loro in quello stesso rapporto dato. Infatti, se nelle figure di questo lemma si prendono parallelogrammi che stiano fra loro come le parti, le somme delle parti staranno sempre come le somme dei parallelogrammi; e perciò, quando il numero delle parti e dei parallelogrammi aumenta e la loro grandezza diminuisce all’infinito, staranno nel rapporto ultimo di parallelogramma a parallelogramma, cioè (per ipotesi) nel rapporto ultimo di parte a parte.

### Lemma V (figure simili)

**[S1.14]** **In figure simili tutti i lati che si corrispondono a vicenda, tanto curvilinei quanto rettilinei, sono proporzionali; e le aree stanno in rapporto duplicato dei lati.**

### Lemma VI (l’angolo fra corda e tangente svanisce)

**[S1.15]** **Se un arco qualsiasi ABC, dato di posizione, è sotteso dalla corda AB, e in un punto A, posto nel mezzo di una curvatura continua, è toccato da una retta AD prolungata da entrambe le parti; e poi i punti A, B si avvicinano l’uno all’altro e si riuniscono: dico che l’angolo BAD, compreso fra la corda e la tangente, diminuirà all’infinito e alla fine svanirà.**

**[S1.16]** Infatti, se quell’angolo non svanisce, l’arco ACB conterrà con la tangente AD un angolo uguale a un angolo rettilineo, e perciò la curvatura nel punto A non sarà continua, contro l’ipotesi.

### Lemma VII (arco, corda e tangente)

**[S1.17]** **Poste le stesse cose, dico che il rapporto ultimo dell’arco, della corda e della tangente fra loro è il rapporto di uguaglianza.**

**[S1.18]** Infatti, mentre il punto B si avvicina al punto A, si immaginino sempre AB e AD prolungate fino ai punti lontani b e d, e si conduca bd parallela alla secante BD. E l’arco Acb sia sempre simile all’arco ACB. Quando i punti A, B si riuniscono, l’angolo dAb, per il lemma precedente, svanirà; e perciò le rette Ab, Ad, che restano sempre finite, e l’arco intermedio Acb coincideranno, e quindi saranno uguali. Di conseguenza anche le rette AB, AD e l’arco intermedio ACB, sempre proporzionali a queste, svaniranno e avranno il rapporto ultimo di uguaglianza. C.V.D.

**[S1.19]** Cor. 1. Se dunque per B si conduce BF parallela alla tangente, che tagli sempre in F una retta qualsiasi AF passante per A, questa BF avrà alla fine con l’arco evanescente ACB rapporto di uguaglianza, perché, completato il parallelogramma AFBD, ha sempre rapporto di uguaglianza con AD.

**[S1.20]** Cor. 2. E se per B e per A si conducono più rette BE, BD, AF, AG, che tagliano la tangente AD e la sua parallela BF, il rapporto ultimo di tutte le ascisse AD, AE, BF, BG, e della corda e dell’arco AB, fra loro sarà il rapporto di uguaglianza.

**[S1.21]** Cor. 3. E perciò tutte queste linee, in ogni ragionamento sui rapporti ultimi, si possono usare l’una al posto dell’altra.

### Lemma VIII (triangoli evanescenti)

**[S1.22]** **Se le rette date AR, BR, con l’arco ACB, la corda AB e la tangente AD, formano tre triangoli RAB, RACB, RAD, e poi i punti A, B si avvicinano l’uno all’altro: dico che la forma ultima dei triangoli evanescenti è quella della similitudine, e il rapporto ultimo quello dell’uguaglianza.**

**[S1.23]** Infatti, mentre il punto B si avvicina al punto A, si immaginino sempre AB, AD, AR prolungate fino ai punti lontani b, d e r; si conduca rbd parallela a RD; e l’arco Acb sia sempre simile all’arco ACB. Quando i punti A, B si riuniscono, l’angolo bAd svanirà, e perciò i tre triangoli rAb, rAcb, rAd, che restano sempre finiti, coincideranno, e per questa ragione sono simili e uguali. Di conseguenza anche RAB, RACB, RAD, sempre simili e proporzionali a questi, diventeranno alla fine simili e uguali fra loro. C.V.D.

**[S1.24]** Cor. E di qui quei triangoli, in ogni ragionamento sui rapporti ultimi, si possono usare l’uno al posto dell’altro.

### Lemma IX (aree evanescenti in rapporto duplicato dei lati)

**[S1.25]** **Se la retta AE e la curva ABC, date di posizione, si tagliano a vicenda in un angolo dato A, e alla retta, in un altro angolo dato, si conducono come ordinate BD, CE, che incontrano la curva in B, C; e poi i punti B, C si avvicinano insieme al punto A: dico che le aree dei triangoli ABD, ACE staranno alla fine fra loro in rapporto duplicato dei lati.**

**[S1.26]** Infatti, mentre i punti B, C si avvicinano al punto A, si immagini sempre AD prolungata fino ai punti lontani d ed e, in modo che Ad, Ae siano proporzionali ad AD, AE; e si innalzino le ordinate db, ec, parallele alle ordinate DB, EC, che incontrino in b e c le AB, AC prolungate. Si immagini di condurre sia la curva Abc simile alla ABC, sia la retta Ag, che tocchi entrambe le curve in A e tagli le ordinate DB, EC, db, ec in F, G, f, g. Poi, restando invariata la lunghezza Ae, i punti B, C si riuniscano con il punto A; e, svanendo l’angolo cAg, le aree curvilinee Abd, Ace coincideranno con le rettilinee Afd, Age; e perciò (per il Lemma V) staranno in rapporto duplicato dei lati Ad, Ae. Ma a queste aree sono sempre proporzionali le aree ABD, ACE, e a questi lati i lati AD, AE. Dunque anche le aree ABD, ACE stanno alla fine in rapporto duplicato dei lati AD, AE. C.V.D.

### Lemma X (spazi descritti all’inizio del moto)

**[S1.27]** **Gli spazi che un corpo, sollecitato da una forza finita qualsiasi, descrive, sia che quella forza sia determinata e immutabile, sia che aumenti continuamente o diminuisca continuamente, stanno, proprio all’inizio del moto, in rapporto duplicato dei tempi.**

**[S1.28]** Si rappresentino i tempi con le linee AD, AE, e le velocità generate con le ordinate DB, EC; e gli spazi descritti con queste velocità staranno come le aree ABD, ACE descritte da queste ordinate, cioè, proprio all’inizio del moto (per il Lemma IX), in rapporto duplicato dei tempi AD, AE. C.V.D.

**[S1.29]** Cor. 1. E di qui si ricava facilmente che gli errori dei corpi che descrivono parti simili di figure simili in tempi proporzionali, errori generati da forze uguali qualsiasi applicate in modo simile ai corpi e misurati dalle distanze dei corpi da quei luoghi delle figure simili ai quali gli stessi corpi, senza quelle forze, giungerebbero negli stessi tempi proporzionali, stanno, con ottima approssimazione, come i quadrati dei tempi in cui sono generati.

**[S1.30]** Cor. 2. Gli errori, invece, che sono generati da forze proporzionali applicate in modo simile a parti simili di figure simili stanno come le forze e i quadrati dei tempi considerati congiuntamente.

**[S1.31]** Cor. 3. Lo stesso si deve intendere di spazi qualsiasi che i corpi descrivono sollecitati da forze diverse. Questi stanno, proprio all’inizio del moto, come le forze e i quadrati dei tempi considerati congiuntamente.

**[S1.32]** Cor. 4. E perciò le forze stanno come gli spazi descritti proprio all’inizio del moto direttamente e i quadrati dei tempi inversamente.

**[S1.33]** Cor. 5. E i quadrati dei tempi stanno come gli spazi descritti direttamente e le forze inversamente.

### Scolio (il linguaggio delle proporzionalità)

**[S1.34]** Se si confrontano fra loro quantità indeterminate di generi diversi, e si dice che una di esse sta come un’altra qualsiasi direttamente o inversamente, il senso è che la prima aumenta o diminuisce nello stesso rapporto della seconda, o della sua reciproca. E se si dice che una di esse sta come due o più altre direttamente o inversamente, il senso è che la prima aumenta o diminuisce nel rapporto composto dei rapporti nei quali aumentano o diminuiscono le altre, o le reciproche delle altre. Così, se si dice che A sta come B direttamente, C direttamente e D inversamente, il senso è che A aumenta o diminuisce nello stesso rapporto di B × C × 1/D, cioè che A e BC/D stanno fra loro in un rapporto dato.

### Lemma XI (sottesa dell’angolo di contatto)

**[S1.35]** **La sottesa evanescente dell’angolo di contatto, in tutte le curve che nel punto di contatto hanno curvatura finita, è alla fine in rapporto duplicato della sottesa dell’arco contermine.**

**[S1.36]** Caso 1. Sia AB quell’arco, AD la sua tangente, BD la sottesa dell’angolo di contatto, perpendicolare alla tangente, AB la sottesa dell’arco. A questa sottesa AB e alla tangente AD si innalzino le perpendicolari AG, BG, che si incontrano in G; poi i punti D, B, G si avvicinino ai punti d, b, g, e sia J l’intersezione delle linee BG, AG che si ottiene alla fine, quando i punti D, B giungono fino ad A. È manifesto che la distanza GJ può essere minore di qualunque distanza assegnata. Ora (per la natura dei cerchi passanti per i punti A, B, G e A, b, g) AB² è uguale ad AG × BD, e Ab² è uguale ad Ag × bd; e perciò il rapporto di AB² ad Ab² è composto dei rapporti di AG ad Ag e di BD a bd. Ma poiché GJ si può prendere minore di qualunque lunghezza assegnata, può accadere che il rapporto di AG ad Ag differisca dal rapporto di uguaglianza meno di qualunque differenza assegnata, e quindi che il rapporto di AB² ad Ab² differisca dal rapporto di BD a bd meno di qualunque differenza assegnata. Dunque, per il Lemma I, il rapporto ultimo di AB² ad Ab² è lo stesso del rapporto ultimo di BD a bd. C.V.D.

**[S1.37]** Caso 2. Si inclini ora BD su AD in un angolo dato qualsiasi: il rapporto ultimo di BD a bd sarà sempre lo stesso di prima, e quindi lo stesso di AB² ad Ab². C.V.D.

**[S1.38]** Caso 3. E anche se l’angolo D non è dato, ma la retta BD converge verso un punto dato, o è determinata secondo qualunque altra legge, tuttavia gli angoli D, d, determinati secondo una legge comune, tenderanno sempre all’uguaglianza e si avvicineranno l’uno all’altro più di qualunque differenza assegnata, e perciò alla fine saranno uguali, per il Lemma I; e quindi le linee BD, bd stanno fra loro nello stesso rapporto di prima. C.V.D.

**[S1.39]** Cor. 1. Poiché dunque le tangenti AD, Ad, gli archi AB, Ab e i loro seni BC, bc diventano alla fine uguali alle corde AB, Ab, anche i loro quadrati staranno alla fine come le sottese BD, bd.

**[S1.40]** Cor. 2. I loro quadrati stanno anche, alla fine, come le saette degli archi che dividono a metà le corde e convergono verso un punto dato. Infatti quelle saette stanno come le sottese BD, bd.

**[S1.41]** Cor. 3. E perciò la saetta sta in rapporto duplicato del tempo in cui un corpo descrive l’arco con velocità data.

**[S1.42]** Cor. 4. I triangoli rettilinei ADB, Adb stanno alla fine in rapporto triplicato dei lati AD, Ad, e in rapporto sesquiplicato dei lati DB, db, poiché stanno nel rapporto composto dei lati AD e DB, Ad e db. Così anche i triangoli ABC, Abc stanno alla fine in rapporto triplicato dei lati BC, bc. Chiamo poi rapporto sesquiplicato il subduplicato del triplicato, quello cioè che è composto del semplice e del subduplicato.

**[S1.43]** Cor. 5. E poiché DB, db sono alla fine parallele e in rapporto duplicato delle AD, Ad, le aree curvilinee ultime ADB, Adb saranno (per la natura della parabola) i due terzi dei triangoli rettilinei ADB, Adb, e i segmenti AB, Ab la terza parte degli stessi triangoli. E di qui queste aree e questi segmenti staranno in rapporto triplicato sia delle tangenti AD, Ad, sia delle corde e degli archi AB, Ab.

### Scolio (angoli di contatto e metodo dei limiti)

**[S1.44]** In tutto ciò, del resto, supponiamo che l’angolo di contatto non sia né infinitamente maggiore degli angoli di contatto che i cerchi formano con le loro tangenti, né infinitamente minore di essi; cioè che la curvatura nel punto A non sia né infinitamente piccola né infinitamente grande, ossia che l’intervallo AJ sia di grandezza finita. Si può infatti prendere DB come AD³: in questo caso per il punto A non si può condurre alcun cerchio fra la tangente AD e la curva AB, e perciò l’angolo di contatto sarà infinitamente minore di quelli circolari.

**[S1.45]** E con un argomento simile, se si fa DB successivamente come AD⁴, AD⁵, AD⁶, AD⁷, ecc., si avrà una serie di angoli di contatto che procede all’infinito, ciascuno dei quali è infinitamente minore del precedente. E se si fa DB successivamente come AD², AD³/², AD⁴/³, AD⁵/⁴, AD⁶/⁵, AD⁷/⁶, ecc., si avrà un’altra serie infinita di angoli di contatto, il primo dei quali è dello stesso genere di quelli circolari, il secondo infinitamente maggiore, e ciascuno dei successivi infinitamente maggiore del precedente. Ma anche fra due qualsiasi di questi angoli si può inserire una serie di angoli intermedi che procede all’infinito da entrambe le parti, ciascuno dei quali sarà infinitamente maggiore o minore del precedente. Come se fra i termini AD² e AD³ si inserisse la serie AD¹³/⁶, AD¹¹/⁵, AD⁹/⁴, AD⁷/³, AD⁵/², AD⁸/³, AD¹¹/⁴, AD¹⁴/⁵, AD¹⁷/⁶, ecc. E di nuovo, fra due angoli qualsiasi di questa serie si può inserire una nuova serie di angoli intermedi, che differiscono l’uno dall’altro per intervalli infiniti. E la natura non conosce limite.

**[S1.46]** Ciò che è stato dimostrato delle linee curve e delle superfici da esse comprese si applica facilmente alle superfici curve e ai volumi dei solidi. Ho premesso poi questi lemmi per sfuggire al tedio di condurre lunghe dimostrazioni per assurdo, al modo degli antichi geometri. Le dimostrazioni, infatti, si rendono più concise con il metodo degli indivisibili. Ma poiché l’ipotesi degli indivisibili è piuttosto dura, e perciò quel metodo è giudicato meno geometrico, ho preferito ricondurre le dimostrazioni di ciò che segue alle somme e ai rapporti ultimi delle quantità evanescenti, e ai primi delle nascenti, cioè ai limiti delle somme e dei rapporti; e perciò premettere, con la brevità che ho potuto, le dimostrazioni di quei limiti. Con questi, infatti, si ottiene lo stesso risultato che con il metodo degli indivisibili; e, dimostrati i principi, ce ne serviremo ormai con maggiore sicurezza. Perciò, nel seguito, se talvolta considererò le quantità come costituite di particelle, o se userò piccole linee curve al posto delle rette, vorrei che si intendessero sempre non indivisibili, ma divisibili evanescenti; non somme e rapporti di parti determinate, ma limiti di somme e di rapporti; e che la forza di tali dimostrazioni fosse sempre ricondotta al metodo dei lemmi precedenti.

**[S1.47]** Si obietta che delle quantità evanescenti non vi è alcuna proporzione ultima, poiché essa, prima che le quantità siano svanite, non è ultima, e quando sono svanite non c’è affatto. Ma con lo stesso argomento si potrebbe ugualmente sostenere che non vi è alcuna velocità ultima di un corpo che giunge in un certo luogo dove il moto termina: questa infatti, prima che il corpo raggiunga il luogo, non è ultima, e quando lo ha raggiunto non c’è affatto. E la risposta è facile: per velocità ultima si intende quella con cui il corpo si muove non prima di raggiungere il luogo ultimo e prima che il moto cessi, né dopo, ma nel momento in cui lo raggiunge; cioè proprio quella velocità con cui il corpo raggiunge il luogo ultimo e con cui il moto cessa. E similmente per rapporto ultimo delle quantità evanescenti si deve intendere il rapporto delle quantità non prima che svaniscano, non dopo, ma quello con cui svaniscono. Parimenti anche il rapporto primo delle quantità nascenti è il rapporto con cui nascono. E la somma prima e ultima è quella con cui cominciano e cessano di essere (o di aumentare o di diminuire). Esiste un limite che la velocità alla fine del moto può raggiungere, ma non oltrepassare. Questa è la velocità ultima. E lo stesso vale per il limite di tutte le quantità e proporzioni che cominciano e cessano. E poiché questo limite è certo e definito, determinarlo è un problema veramente geometrico. Ora, tutto ciò che è geometrico si usa legittimamente per determinare e dimostrare altre cose geometriche.

**[S1.48]** Si può anche sostenere che, se sono dati i rapporti ultimi delle quantità evanescenti, saranno date anche le grandezze ultime; e così ogni quantità consterà di indivisibili, contro ciò che Euclide ha dimostrato sugli incommensurabili nel decimo libro degli *Elementi*. Ma questa obiezione si fonda su un’ipotesi falsa. Quei rapporti ultimi con cui le quantità svaniscono non sono in realtà rapporti di quantità ultime, ma limiti ai quali i rapporti delle quantità che decrescono senza limite si avvicinano sempre; e ai quali possono accostarsi più di qualunque differenza data, ma che non possono mai oltrepassare, né raggiungere prima che le quantità siano diminuite all’infinito. La cosa si intenderà più chiaramente nelle quantità infinitamente grandi. Se due quantità la cui differenza è data aumentano all’infinito, sarà dato il loro rapporto ultimo, cioè il rapporto di uguaglianza; e tuttavia non per questo saranno date le quantità ultime, ossia massime, di cui quello è il rapporto. Nel seguito, dunque, se talvolta, per favorire una facile immaginazione e comprensione delle cose, dirò quantità minime, o evanescenti, o ultime, guardati dall’intendere quantità determinate di grandezza, ma pensa sempre a quantità da diminuire senza limite.

**Fine della Sezione I. Nel testo originale segue la Sezione II, *De inventione virium centripetarum*.**

---

## Apparato

### A.0 Estensioni del glossario

I termini seguenti non comparivano nel glossario comune. Ognuno è reso in modo costante in tutto il fascicolo.

| Latino | Italiano | Motivazione |
|---|---|---|
| *latitudo* (dei parallelogrammi) | «larghezza» | È la base dei rettangoli elementari. Motte: «breadth». |
| *figura inscripta / circumscripta / curvilinea* | «figura inscritta / circoscritta / curvilinea» | Lessico geometrico corrente; corrisponde alle somme inferiore e superiore (nota N2). |
| *evanescere*; *quantitates evanescentes* | «svanire»; «quantità evanescenti» | Il verbo è reso «svanire», l’aggettivo resta tecnico secondo il glossario. |
| *coire*, *coëant*, *coeuntibus punctis* | «riunirsi», «quando i punti … si riuniscono» | Distinto da *coincidere* («coincidere»), che Newton usa per le figure (Lemmi VII–IX). |
| *intelligantur*, *intelligatur* | «si immaginino», «si immagini» | Costruzione ausiliaria pensata, non tracciata davvero; Motte «consider», «suppose». |
| *ad puncta longinqua* | «fino ai punti lontani» | Le figure ingrandite Ab, Ad, Acb restano finite (nota N5). |
| *angulus rectilineus* | «angolo rettilineo» | Angolo fra due rette, contrapposto all’angolo di contatto. |
| *curvatura continua* | «curvatura continua» | Si conserva il termine; il senso moderno è nella nota N5. |
| *componendo* | «componendo» | Termine tecnico euclideo delle proporzioni, conservato. |
| *assignata* | «assegnata» | Distinto da *data* («data»), come nel latino del Lemma XI. |
| *arcus conterminus* | «arco contermine» | L’arco che ha in comune con la sottesa l’estremo A (e B). |
| *errores* (Lemma X, Cor. 1–2) | «errori» | Sono gli scostamenti dal luogo che il corpo raggiungerebbe senza le forze. Si conserva il termine storico; vedi N6. |
| *ipso motus initio* | «proprio all’inizio del moto» | Il pronome *ipso* sottolinea che il rapporto vale al limite iniziale. |
| *quantitates indeterminatæ* | «quantità indeterminate» | Le grandezze variabili, nel linguaggio dell’epoca. |
| *quadrata temporum* | «quadrati dei tempi» | Nei Cor. del Lemma X Newton scrive *quadrata*, non *ratio duplicata*: la differenza è conservata. |
| *vergere* (Lemma XI, Caso 3) | «tendere» | Unico caso; *ad æqualitatem vergent* ha lo stesso senso di *ad æqualitatem tendunt* del Lemma I. |
| *contenta* (*solidorum*) | «volumi» | Il «contenuto» di un solido; Motte «contents». |
| *methodus indivisibilium* | «metodo degli indivisibili» | Termine storico. |
| *lineolæ curvæ* | «piccole linee curve» | Diminutivo reso con l’aggettivo. |
| *limes* | «limite» | Termine chiave dello Scolio finale. |
| *proportio* | «proporzione» | Nello Scolio finale Newton alterna *ratio* e *proportio*; la distinzione lessicale è conservata. |

### A.1 Intestazione e titolo della Sezione

**Latino:** *De motu corporum liber primus. Sectio I. De methodo rationum primarum & ultimarum, cujus ope sequentia demonstrantur.*

**Inglese:** «Book I. Of the motion of bodies. Section I. Of the method of first and last ratios of quantities, by the help whereof we demonstrate the propositions that follow.» (L’intestazione del Libro I è nell’EPUB, p. 95, ma non nell’estratto di lavoro.)

**Scelte.** *sequentia* è reso «ciò che segue». Motte aggiunge «of quantities» e specifica «the propositions», che il latino non ha.

### A.2 Lemma I

**Latino:** *Quantitates, ut & quantitatum rationes, quæ ad æqualitatem tempore quovis finito constanter tendunt, & ante finem temporis illius propius ad invicem accedunt quam pro data quavis differentia, fiunt ultimo æquales.*

**Inglese:** «Quantities, and the ratios of quantities, which in any finite time converge continually to equality, and before the end of that time approach nearer the one to the other than by any given difference, become ultimately equal.»

**Scelte.**

- *constanter tendunt*: «tendono **senza interruzione**», per decisione del curatore (Fascicolo 3, F1). Il lemma richiede che la tendenza non venga meno, non che l’avvicinamento avvenga a ritmo costante. Motte rende «converge continually».
- *propius … quam pro data quavis differentia*: «più di qualunque differenza data». È la clausola che oggi si scrive con un ε arbitrario (nota N1).
- *Si negas* è una seconda persona: «Se lo neghi». La dimostrazione è per assurdo.

### A.3 Lemmi II e III

**Latino (II):** *Si in figura quavis AacE, rectis Aa, AE & curva acE comprehensa, inscribantur parallelogramma quotcunque Ab, Bc, Cd, &c. sub basibus AB, BC, CD, &c. æqualibus, & lateribus Bb, Cc, Dd, &c. figuræ lateri Aa parallelis contenta; & compleantur parallelogramma aKbl, bLcm, cMdn, &c. Dein horum parallelogrammorum latitudo minuatur, & numerus augeatur in infinitum: dico quod ultimæ rationes quas habent ad se invicem figura inscripta AKbLcMdD, circumscripta AalbmcndoE, & curvilinea AabcdE, sunt rationes æqualitatis.*

**Inglese (II):** «If in any figure AacE, terminated by the right lines Aa, AE, and the curve acE, there be inscribed any number of parallelograms Ab, Bc, Cd, &c., comprehended under equal bases AB, BC, CD, &c., and the sides, Bb, Cc, Dd, &c., parallel to one side Aa of the figure; and the parallelograms aKbl, bLcm, cMdn, &c., are completed. Then if the breadth of those parallelograms be supposed to be diminished, and their number to be augmented in infinitum; I say, that the ultimate ratios which the inscribed figure AKbLcMdD, the circumscribed figure AalbmcndoE, and curvilinear figure AabcdE, will have to one another, are ratios of equality.»

**Latino (III):** *Eædem rationes ultimæ sunt etiam rationes æqualitatis, ubi parallelogrammorum latitudines AB, BC, CD &c. sunt inæquales, & omnes minuuntur in infinitum.*

**Inglese (III):** «The same ultimate ratios are also ratios of equality, when the breadths, AB, BC, DC, &c., of the parallelograms are unequal, and are all diminished in infinitum.»

**Scelte e osservazioni.**

- *sub basibus … & lateribus … contenta*: «contenuti sotto basi … e sotto lati», con la preposizione classica della geometria euclidea; così anche *rectangulum sub unius basi Kb & altitudinum summa Aa*, «il rettangolo compreso sotto la base Kb … e la somma delle altezze Aa».
- La trascrizione spezza *circum <29> scripta* sul cambio di pagina: si legge *circumscripta*.
- Nel Lemma II la somma delle altezze dei parallelogrammi Kl, Lm, Mn, Do è uguale ad Aa solo se la curva scende in modo monotono da a fino al punto E sulla retta AE. Il testo lo presuppone attraverso la figura (non disponibile) e le lettere: la figura AacE è chiusa dalla curva che termina in E. Vedi N2.
- *multo magis* è reso «a maggior ragione».
- Lemma III, Cor. 4: la trascrizione ha *(quoad perimetros acE;)* con un punto e virgola dentro la parentesi; è un segno spurio, probabilmente della trascrizione. Non incide sul senso.
- **Motte:** nel Lemma III scrive «DC» invece di CD; nel Cor. 2 scrive «CD» (maiuscole) invece di *cd*; nel Lemma II aggiunge «be supposed to be» e rende *minus quovis dato* con «less than any given space».

### A.4 Lemma IV e Corollario

**Latino:** *Si in duabus figuris AacE, PprT, inscribantur (ut supra) duæ parallelogrammorum series, sitque idem amborum numerus, & ubi latitudines in infinitum diminuuntur, rationes ultimæ parallelogrammorum in una figura ad parallelogramma in altera, singulorum ad singula, sint eædem; dico quod figuræ duæ AacE, PprT, sunt ad invicem in eadem illa ratione.*

**Inglese:** «If in two figures AacE, PprT, you inscribe (as before) two ranks of parallelograms, an equal number in each rank, and, when their breadths are diminished in infinitum, the ultimate ratios of the parallelograms in one figure to those in the other, each to each respectively, are the same; I say, that those two figures AacE, PprT, are to one another in that same ratio.»

**Scelte e osservazioni.**

- La trascrizione spezza *parallelo <30> gramma* sul cambio di pagina.
- *existente nimirum*: «poiché, beninteso»; l’ablativo assoluto dà la ragione.
- Nel Corollario, *datam obtineant rationem* è reso «hanno … un rapporto dato». Motte amplia l’ultima frase in «of any part of the one quantity to the correspondent part of the other», dove il latino ha solo *partis ad partem*.

### A.5 Lemma V

**Latino:** *Similium figurarum latera omnia, quæ sibi mutuo respondent, sunt proportionalia, tam curvilinea quam rectilinea; & areæ sunt in duplicata ratione laterum.*

**Inglese:** «In similar figures, all sorts of homologous sides, whether curvilinear or rectilinear, are proportional; and the areas are in the duplicate ratio of the homologous sides.»

**Scelte.** *quæ sibi mutuo respondent* è reso alla lettera, «che si corrispondono a vicenda». Motte usa «homologous» e lo ripete nella seconda parte, dove il latino ha solo *laterum*. Il lemma è senza dimostrazione.

### A.6 Lemma VI

**Latino:** *Si arcus quilibet positione datus ABC subtendatur chorda AB, & in puncto aliquo A, in medio curvaturæ continuæ, tangatur a recta utrinque producta AD; dein puncta A, B ad invicem accedant & coëant; dico quod angulus BAD, sub chorda & tangente contentus, minuetur in infinitum & ultimo evanescet.*

**Inglese:** «If any arc ACB, given in position is subtended by its chord AB, and in any point A, in the middle of the continued curvature, is touched by a right line AD, produced both ways; then if the points A and B approach one another and meet, I say, the angle BAD, contained between the chord and the tangent, will be diminished in infinitum, and ultimately will vanish.»

**Scelte e osservazioni.**

- **Lettere dell’arco.** L’enunciato latino ha *arcus … ABC*, la dimostrazione e i lemmi seguenti *ACB*. Motte ha ACB anche nell’enunciato. La lettera C indica un punto intermedio dell’arco, e la sigla ACB è quella coerente con l’uso successivo. Non so se *ABC* sia della stampa o della trascrizione: va verificato sulla stampa. La traduzione conserva ABC.
- *in medio curvaturæ continuæ*: «posto nel mezzo di una curvatura continua», cioè non in un estremo dell’arco né in un punto angoloso (nota N5).
- *angulum rectilineo æqualem*: «un angolo uguale a un angolo rettilineo», cioè un angolo finito come quello fra due rette.

### A.7 Lemma VII e corollari

**Latino:** *Iisdem positis; dico quod ultima ratio arcus, chordæ, & tangentis ad invicem est ratio æqualitatis.*

**Inglese:** «The same things being supposed, I say that the ultimate ratio of the arc, chord, and tangent, any one to any other, is the ratio of equality.»

**Scelte e osservazioni.**

- La trascrizione ha *LEMMA. VII.* con un punto in più: irrilevante.
- *per lemma superius*: «per il lemma precedente», cioè il Lemma VI.
- *rectæ semper finitæ Ab, Ad*: «le rette Ab, Ad, che restano sempre finite». È il cuore dell’argomento: la figura ingrandita non svanisce, e su di essa si legge il rapporto ultimo della figura che svanisce.
- Cor. 1: *perpetuo secans* è reso «che tagli sempre». Il parallelogramma AFBD implica che BD sia parallela ad AF; la retta BD è quindi una secante qualsiasi da B alla tangente, e non necessariamente quella del Lemma VI.
- Cor. 2: le rette BE, BD, AF, AG sono quattro rette qualsiasi; le ascisse AD, AE sono tagliate sulla tangente, BF, BG sulla sua parallela per B. Senza la figura NATP00087-4 la posizione esatta di E e G non è ricostruibile; il testo basta per l’enunciato.

### A.8 Lemma VIII

**Latino:** *Si rectæ datæ AR, BR cum arcu ACB, chorda AB & tangente AD, triangula tria RAB, RACB, RAD constituunt, dein puncta A, B accedunt ad invicem: dico quod ultima forma triangulorum evanescentium est similitudinis, & ultima ratio æqualitatis.*

**Inglese:** «If the right lines AR, BR, with the arc ACB, the chord AB, and the tangent AD, constitute three triangles RAB, RACB, RAD, and the points A and B approach and meet: I say, that the ultimate form of these evanescent triangles is that of similitude, and their ultimate ratio that of equality.»

**Scelte e osservazioni.**

- La trascrizione ha *AD,triangula* senza spazio e *paralella* per *parallela*: refuso probabile della trascrizione, da verificare sulla stampa.
- La dimostrazione prende *rbd* parallela a *RD*: dunque R, B, D sono allineati, e D è il punto in cui la retta RB incontra la tangente. Poiché i triangoli sono «evanescenti», anche R si avvicina ad A: il testo dice soltanto che le rette AR, BR sono «date». La figura NATP00087-5 non è disponibile. Nella verifica numerica (N5) ho preso AR come retta data di posizione per A e BR parallela a una direzione data.
- **Motte** omette *datæ* («If the right lines AR, BR») e aggiunge «and meet», che nell’enunciato latino non c’è (*accedunt ad invicem*).

### A.9 Lemma IX

**Latino:** *Si recta AE & curva ABC positione datæ se mutuo secent in angulo dato A, & ad rectam illam in alio dato angulo ordinatim applicentur BD, CE, curvæ occurrentes in B, C, dein puncta B, C simul accedant ad punctum A: dico quod areæ triangulorum ABD, ACE erunt ultimo ad invicem in duplicata ratione laterum.*

**Inglese:** «If a right line AE, and a curve line ABC, both given by position, cut each other in a given angle, A; and to that right line, in another given angle, BD, CE are ordinately applied, meeting the curve in B, C; and the points B and C together approach towards and meet in the point A: I say, that the areas of the triangles ABD, ACE, will ultimately be one to the other in the duplicate ratio of the sides.»

**Scelte e osservazioni.**

- *ordinatim applicentur* è reso «si conducono come ordinate», secondo il glossario (*ordinatim applicata*: «ordinata»). La trascrizione spezza *ordi <33> natim* sul cambio di pagina.
- *occurant* è un refuso probabile della trascrizione per *occurrant*, da verificare sulla stampa.
- I «triangoli» ABD, ACE sono **curvilinei**: due lati rettilinei (AD, DB) e l’arco AB. Lo conferma la dimostrazione, che confronta le «aree curvilinee» Abd, Ace con le rettilinee Afd, Age.
- Nella trascrizione, il periodo *… laterum Ad, Ae: Sed his areis …* ha una maiuscola dopo i due punti; in Parte B è diviso in due passi.
- *(per lemma v.)*: i triangoli Afd, Age sono simili (Ag comune, fd parallela a ge), quindi le loro aree stanno in rapporto duplicato dei lati Ad, Ae.

### A.10 Lemma X, corollari e Scolio

**Latino:** *Spatia quæ corpus urgente quacunque vi finita describit, sive vis illa determinata & immutabilis sit, sive eadem continuo augetur vel continuo diminuatur, sunt ipso motus initio in duplicata ratione temporum.*

**Inglese:** «The spaces which a body describes by any finite force urging it, whether that force is determined and immutable, or is continually augmented or continually diminished, are in the very beginning of the motion one to the other in the duplicate ratio of the times.»

**Scelte e osservazioni.**

- *augetur … diminuatur*: indicativo e congiuntivo coordinati. Ci si aspetterebbe *augeatur*; può essere un refuso della trascrizione o una svista della stampa. Da verificare. Il senso non cambia.
- *urgente … vi*: «sollecitato da una forza», secondo il glossario per *urgere* riferito alle forze.
- Cor. 1: il periodo latino è costruito con il soggetto *errores* lontano dal verbo *sunt*. L’italiano conserva l’ordine e isola fra virgole la lunga relativa. *quam proxime* chiude il periodo nel latino ed è reso «con ottima approssimazione». Motte riordina il periodo e anticipa «nearly».
- Cor. 2: Motte aggiunge «to the bodies» (*similiter applicatis* è riferito alle parti delle figure, non ai corpi).
- **Scolio, formula appiattita.** La trascrizione ha *B×C× 1D* e *A & BCD*. Vanno letti **B × C × 1/D** e **A e BC/D**: è l’unica lettura coerente con «B direttamente, C direttamente e D inversamente». Motte 1846 (SVG 2 e 3) ha correttamente A e BC/D.
- **Errore di Motte 1846 (SVG 1).** L’immagine della formula, controllata sia sull’attributo `data-tex` sia sull’immagine resa, porta **A × C × 1/D** invece di **B × C × 1/D**. È un refuso dell’edizione 1846 o della sua trascrizione digitale; non ho potuto controllare Motte 1729.

### A.11 Lemma XI

**Latino:** *Subtensa evanescens anguli contactus, in curvis omnibus curvaturam finitam ad punctum contactus habentibus, est ultimo in ratione duplicata subtensæ arcus contermini.*

**Inglese:** «The evanescent subtense of the angle of contact, in all curves which at the point of contact have a finite curvature, is ultimately in the duplicate ratio of the subtense of the conterminate arc.»

**Scelte e osservazioni.**

- *subtensa*: «sottesa», secondo il glossario. Nel Lemma XI la parola ha due referenti: la sottesa **dell’angolo di contatto** (BD, segmento da B alla tangente) e la sottesa **dell’arco** (AB, cioè la corda). L’italiano mantiene la stessa parola, come il latino.
- **Caso 1, le perpendicolari.** *Huic subtensæ AB & tangenti AD perpendiculares erigantur AG, BG* non accoppia le rette nell’ordine delle parole. La geometria richiede **BG perpendicolare ad AB e AG perpendicolare ad AD**: solo così il cerchio per A, B, G ha diametro AG, è tangente ad AD in A e dà AB² = AG × BD (verificato in N8). Motte esplicita l’accoppiamento giusto: «Draw BG perpendicular to the subtense AB, and AG to the tangent AD». La traduzione conserva l’ordine latino senza scioglierlo.
- La trascrizione ha *AG×BD,&* e *Abquad.* senza spazi: artefatti.
- *J*: lettera della trascrizione, conservata come in Motte. Non ho verificato sulla stampa del 1726 quale forma tipografica sia usata.
- **Caso 3.** *anguli D, d communi lege constitui*: refuso probabile della trascrizione per *constituti*, da verificare sulla stampa. Si traduce «determinati secondo una legge comune».
- **Cor. 1.** I punti C, c (*sinus BC, bc*) non sono definiti nel testo; dal Cor. 4 (*triangula ABC, Abc*) e dal termine «seno» si ricava che BC è la perpendicolare da B sulla normale AG. Senza la figura NATP00087-8 non lo posso confermare.
- **Cor. 2–3, *saggitæ*.** Nella trascrizione il Cor. 2 ha prima *sagittæ*, poi *saggitæ*; il Cor. 3 ha *saggita*. La grafia con doppia g può essere della stampa: da verificare. Si traduce sempre «saetta» (nota N9).
- **Cor. 4.** *in composita ratione laterum AD & DB, Ad & db*: il rapporto composto dei rapporti AD : Ad e DB : db. L’italiano conserva la formulazione latina. **Motte sbaglia l’accoppiamento**: «compounded of the sides AD to DB, and of Ad to db».
- **Cor. 5.** *ex natura parabolæ*: alla fine l’arco si comporta come una parabola, perché DB sta come AD² (N10).

### A.12 Scolio finale: la serie degli angoli di contatto

**Ricostruzione degli esponenti.** La trascrizione appiattisce gli apici: *AD3*, *AD4,AD5,AD6,AD7*, *AD2,AD32,AD43,AD54,AD65,AD76*, *AD2&AD3*, *AD136,AD115,AD94, AD73,AD52,AD83,AD114,AD145,AD176*. La lettura adottata è:

| Trascrizione | Lettura | Esponente |
|---|---|---|
| AD3 | AD³ | 3 |
| AD4, AD5, AD6, AD7 | AD⁴, AD⁵, AD⁶, AD⁷ | 4, 5, 6, 7 |
| AD2, AD32, AD43, AD54, AD65, AD76 | AD², AD³/², AD⁴/³, AD⁵/⁴, AD⁶/⁵, AD⁷/⁶ | 2, 3/2, 4/3, 5/4, 6/5, 7/6 |
| AD2 & AD3 | AD² e AD³ | 2 e 3 |
| AD136, AD115, AD94, AD73, AD52 | AD¹³/⁶, AD¹¹/⁵, AD⁹/⁴, AD⁷/³, AD⁵/² | 2 + 1/6, 2 + 1/5, 2 + 1/4, 2 + 1/3, 2 + 1/2 |
| AD83, AD114, AD145, AD176 | AD⁸/³, AD¹¹/⁴, AD¹⁴/⁵, AD¹⁷/⁶ | 3 − 1/3, 3 − 1/4, 3 − 1/5, 3 − 1/6 |

**Motivi della lettura.**

1. **Struttura delle serie.** La seconda serie è (n + 1)/n per n = 1, …, 6: il primo termine, AD², dà un angolo «dello stesso genere di quelli circolari», i successivi esponenti decrescono verso 1 e danno angoli via via «infinitamente maggiori», come dice il testo. La serie intermedia è tutta compresa fra 2 e 3, come richiede *inter terminos AD² & AD³*, ed è crescente; i suoi termini sono 2 + 1/n (n = 6, 5, 4, 3, 2) e poi 3 − 1/n (n = 3, 4, 5, 6). Una lettura diversa, per esempio «AD136» = AD¹³⁶ o AD × 136, uscirebbe dall’intervallo e romperebbe l’ordine.
2. **Riscontro indipendente con Motte 1846.** Gli attributi `data-tex` delle immagini SVG 8–27 danno esattamente gli stessi esponenti, nello stesso ordine (per esempio SVG 13 = AD 3/2, SVG 19 = AD 13/6, controllati anche sull’immagine).
3. **Controllo con uno script** (nota N11): monotonia, appartenenza all’intervallo (2, 3), forma 2 + 1/n e 3 − 1/n.

**Altre osservazioni sullo Scolio finale.**

- *circularibus* è reso «di quelli circolari», cioè degli angoli di contatto dei cerchi.
- *Ut si … inseratur series …* è una proposizione sospesa nel latino; l’italiano la conserva: «Come se … si inserisse la serie …».
- *Præmisi … ut effugerem tædium deducendi longas demonstrationes … ad absurdum*: Motte rende *longas* con «perplexed».
- *Objectio est*: «Si obietta»; Motte attenua in «Perhaps it may be objected».
- *durior est indivisibilium hypothesis*: «l’ipotesi degli indivisibili è piuttosto dura»; Motte «seems somewhat harsh».
- *vimque … revocari*: «e che la forza … fosse sempre ricondotta»; Motte «depends on».
- *facili rerum imaginationi conceptui consulens*: i due dativi *imaginationi* e *conceptui* sono accostati senza congiunzione. Può essere la fusione, nella trascrizione, di due lezioni diverse. Traduco entrambi, «per favorire una facile immaginazione e comprensione delle cose», e segnalo il punto come **lettura incerta, da verificare sulla stampa**. Motte ha «for the sake of being more easily understood».
- *In sequentibus, igitur siquando*: la virgola dopo *sequentibus* è probabilmente spuria; il senso non cambia.
- *cave intelligas … sed cogita*: imperativi di seconda persona singolare, conservati («guardati dall’intendere … ma pensa»), come *concipe* nel Fascicolo 3.
- *Neque novit natura limitem*: «E la natura non conosce limite»; Motte «Nor is nature confined to any bounds».
- Nel paragrafo sulle obiezioni Motte scrive «successfully» per «successively» (nella serie degli angoli) e «superfices» per «superficies»: refusi dell’edizione 1846.

### A.13 Refusi e anomalie della trascrizione

| Luogo | Trascrizione | Lettura adottata | Natura |
|---|---|---|---|
| S1.03 | *circum <29> scripta* | *circumscripta* | cambio di pagina |
| S1.10 | *(quoad perimetros acE;)* | *(quoad perimetros acE)* | segno spurio |
| S1.11 | *parallelo <30> gramma* | *parallelogramma* | cambio di pagina |
| S1.15 | *arcus … ABC* | ABC (conservato) | possibile svista per ACB; da verificare sulla stampa |
| S1.17 | *LEMMA. VII.* | *LEMMA VII.* | punteggiatura |
| S1.22 | *AD,triangula* | *AD, triangula* | spazio mancante |
| S1.23 | *paralella* | *parallela* | refuso probabile della trascrizione, da verificare sulla stampa |
| S1.25 | *ordi <33> natim* | *ordinatim* | cambio di pagina |
| S1.26 | *occurant* | *occurrant* | refuso probabile della trascrizione, da verificare sulla stampa |
| S1.27 | *augetur … diminuatur* | senso invariato | modo verbale incoerente; da verificare |
| S1.34 | *B×C× 1D*; *A & BCD* | B × C × 1/D; A e BC/D | frazioni appiattite |
| S1.36 | *AG×BD,&*; *Abquad.* | *AG×BD, &*; *Ab quad.* | spazi mancanti |
| S1.38 | *constitui* | *constituti* | refuso probabile della trascrizione, da verificare sulla stampa |
| S1.40–S1.41 | *saggitæ*, *saggita* | *sagittæ*, *sagitta* | grafia oscillante; da verificare sulla stampa |
| S1.44–S1.45 | *AD3*, *AD32*, *AD136*, … | vedi § A.12 | esponenti appiattiti |
| S1.48 | *imaginationi conceptui* | tradotti entrambi | lettura incerta |
| S1.48 | *In sequentibus, igitur* | *In sequentibus igitur* | virgola spuria |

### A.14 Riepilogo: dove Motte aggiunge, omette o sbaglia

| Luogo | Latino | Motte 1846 | Tipo |
|---|---|---|---|
| Titolo | *rationum primarum & ultimarum … sequentia* | «ratios **of quantities** … **the propositions** that follow» | aggiunta |
| S1.01 | *constanter tendunt* | «converge continually» | resa diversa (decisione del curatore: «senza interruzione») |
| S1.04 | *minuitur* | «is **supposed** diminished» | aggiunta |
| S1.04 | *fit minus quovis dato* | «less than any given **space**» | aggiunta |
| S1.05 | *AB, BC, CD* | «AB, BC, **DC**» | lettere errate |
| S1.08 | *ab, bc, cd* | «ab, bc, **CD**» | lettere errate (maiuscole) |
| S1.13 | *partis ad partem* | «of any part of the one quantity to the correspondent part of the other» | parafrasi ampliata |
| S1.14 | *laterum* | «the **homologous** sides» | aggiunta |
| S1.15 | *arcus … ABC* | «arc **ACB**» | lettere diverse (Motte coerente con il seguito) |
| S1.22 | *rectæ datæ AR, BR* | «the right lines AR, BR» | omissione di *datæ* |
| S1.22 | *accedunt ad invicem* | «approach **and meet**» | aggiunta |
| S1.28 | *velocitates genitæ* | «velocities generated **in those times**» | aggiunta |
| S1.29 | *quam proxime* in chiusura | «nearly» anticipato; periodo riordinato | riordino |
| S1.30 | *similiter applicatis* | «similarly applied **to the bodies**» | aggiunta |
| S1.34 | *B×C×1/D* | «**A** × C × 1/D» (SVG 1) | **formula errata** |
| S1.36 | *BD ad bd* | «of **Bd** to bd» | lettera errata |
| S1.36 | *perpendiculares erigantur AG, BG* | «Draw BG perpendicular to the subtense AB, and AG to the tangent AD» | esplicitazione (corretta) |
| S1.40–S1.41 | *sagittæ*, *sagitta* | «versed sines», «versed sine» | termine non equivalente (*sagitta* ≠ *sinus versus* nel glossario) |
| S1.42 | *in composita ratione laterum AD & DB, Ad & db* | «compounded of the sides AD **to DB**, and of Ad **to db**» | **accoppiamento errato** |
| S1.43 | *AB, Ab* | «AB, **AB**» | lettera errata |
| S1.45 | *successive* | «**successfully**» | refuso |
| S1.46 | *longas* | «perplexed» | resa diversa |
| S1.46 | *durior est* | «seems somewhat harsh» | attenuazione |
| S1.46 | *revocari* | «depends on» | resa diversa |
| S1.47 | *Objectio est* | «**Perhaps** it may be objected» | attenuazione |
| S1.48 | *facili rerum imaginationi conceptui consulens* | «for the sake of being more easily understood» | parafrasi |

Le formule di Motte nello Scolio finale (SVG 8–27) coincidono con la lettura del § A.12. Nel Lemma XI, Caso 1, le formule SVG 4–7 (AB² = AG × BD, Ab² = Ag × bd) sono corrette.

---

## Note editoriali e fisiche

Queste note sono aggiunte del presente fascicolo, non affermazioni tradotte da Newton. Tutte le verifiche numeriche sono state eseguite con uno script Python scritto per questo fascicolo, su figure di prova scelte da me; i valori riportati sono quelli stampati dallo script.

### N1. Lemma I: che cosa vuol dire «diventano alla fine uguali»

Il Lemma I è la definizione operativa del limite su cui poggia tutta la Sezione. Se due quantità *f* e *g*, prima di un istante *T*, finiscono per differire meno di qualunque differenza data ε, allora il loro valore «ultimo» è lo stesso: in termini moderni, lim *f* = lim *g*. La dimostrazione è per assurdo: se alla fine restasse una differenza D, non sarebbe vero che si avvicinano più di qualunque differenza data, perché non scenderebbero sotto D. L’espressione «tendono **senza interruzione**» (decisione del curatore) esclude che la tendenza si arresti, senza chiedere che l’avvicinamento sia regolare. L’idea moderna di limite, con ε e δ, è posteriore e non va attribuita a Newton; il lemma però ne contiene già la clausola essenziale, «più di qualunque differenza data».

### N2. Lemmi II e III: somme inferiori e superiori

La figura inscritta e la circoscritta sono quelle che oggi si chiamano somma inferiore e somma superiore. Nel Lemma II, con basi uguali di larghezza *h* e una curva che scende da *a* fino a *E*, la differenza fra le due somme è esattamente *h* · Aa: i rettangolini Kl, Lm, Mn, Do, impilati, hanno altezza totale Aa. Nel Lemma III, con larghezze disuguali, la differenza è al più (larghezza massima) · Aa.

Verifica con la curva di prova *y* = 1 − *x*² su [0, 1] (Aa = 1, AE = 1, area 2/3):

| Numero di parallelogrammi | Differenza | AB · Aa | Inscritta / area | Circoscritta / area |
|---:|---:|---:|---:|---:|
| 4 | 0,250000 | 0,250000 | 0,796875 | 1,171875 |
| 16 | 0,062500 | 0,062500 | 0,952148 | 1,045898 |
| 64 | 0,015625 | 0,015625 | 0,988220 | 1,011658 |
| 256 | 0,003906 | 0,003906 | 0,997066 | 1,002926 |

La differenza coincide con AB · Aa, come dice il Lemma II, e i due rapporti tendono a 1. Con larghezze casuali (Lemma III) la differenza è sempre minore di AF · Aa: per esempio 0,0026 contro 0,0038 con 512 parallelogrammi.

Osservazione per il curatore: l’uguaglianza «somma delle altezze = Aa» vale per una curva monotona che termina sulla retta AE, come nella figura che il testo presuppone. Per una curva qualsiasi l’argomento va applicato a tratti monotoni; Newton non lo dice.

I Cor. 1–4 del Lemma III fondano l’idea che una curva sia limite di poligonali (Cor. 2 e 3). Il Cor. 4 è citato nella Prop. I (Sezione II): la poligonale delle aree uguali diventa alla fine una curva.

### N3. Lemma IV: rapporto di due aree

In termini moderni: se due aree sono divise nello stesso numero di strisce e il rapporto fra le strisce corrispondenti tende a un valore *k* uguale per tutte, allora anche il rapporto fra le aree vale *k*. Il Corollario estende l’enunciato a quantità «di genere qualsiasi» divise in parti, ed è lo strumento con cui Newton confronterà più avanti tempi, aree e spazi. Il passaggio «componendo» è la proprietà delle proporzioni: se *a*₁ : *b*₁ = *a*₂ : *b*₂ = … = *k*, allora (*a*₁ + *a*₂ + …) : (*b*₁ + *b*₂ + …) = *k*.

### N4. Lemma V

È la proprietà di scala delle figure simili: se le lunghezze corrispondenti stanno nel rapporto *λ*, le aree stanno nel rapporto *λ*². Newton la estende esplicitamente ai lati curvilinei. È enunciata senza dimostrazione ed è usata nel Lemma IX.

### N5. Lemmi VI–VIII: la tangente come limite della secante

- **Curvatura continua (Lemma VI).** Nel senso del testo, un punto A è «nel mezzo di una curvatura continua» se in A la curva non ha un angolo: in termini moderni, se è derivabile in A. Se l’angolo fra corda e tangente non svanisse, l’arco formerebbe con la tangente un angolo finito, cioè avrebbe in A un punto angoloso.
- **Metodo della figura ingrandita (Lemmi VII e VIII).** Newton non lavora sulla figura che svanisce, ma su una copia ingrandita, simile a essa, che resta sempre finita (Ab, Ad, Acb). Le proprietà di similitudine trasferiscono i rapporti dalla figura grande a quella piccola. È un modo di parlare di rapporti fra quantità che tendono a zero senza mai dividere per zero.
- **Verifica, Lemma VII** (cerchio di raggio 1, angolo al centro θ, tangente misurata fino alla secante condotta dal centro):

| θ | arco / corda | tangente / corda |
|---:|---:|---:|
| 0,5 | 1,01049 | 1,10407 |
| 0,1 | 1,00042 | 1,00376 |
| 0,01 | 1,000004 | 1,000037 |
| 0,001 | 1,00000004 | 1,0000004 |

- **Verifica, Lemma VIII** (curva *y* = *x*²/2 + *x*³, tangente in A l’asse *x*; AR retta data di posizione *y* = −*x*; BR parallela alla direzione data (1, −2); D intersezione di RB con la tangente). Per *x*_B = 0,3; 0,1; 0,01; 0,001 i rapporti RAB / RAD valgono 1,1071; 1,0291; 1,0025; 1,00025, e RACB / RAD 1,1450; 1,0393; 1,0034; 1,00033. L’angolo BAD scende da 13,5° a 0,029°. La costruzione di R e D è mia: il testo non la fissa (§ A.8).

### N6. Lemmi IX e X: gli spazi all’inizio del moto

- **Lemma IX.** Vicino ad A la curva si confonde con la sua tangente Ag; i triangoli curvilinei ABD, ACE diventano simili a triangoli rettilinei e le loro aree stanno come i quadrati dei lati. Verifica con ordinate inclinate di 60° sulla retta AE, curva di prova che taglia AE nell’angolo dato in A, AE = 2 AD: il rapporto ABD / ACE vale 0,1809; 0,2252; 0,2470; 0,2497 per AD = 0,5; 0,1; 0,01; 0,001, e tende a (AD / AE)² = 0,25.
- **Lemma X.** Newton rappresenta i tempi con le ascisse e le velocità con le ordinate: lo spazio percorso è l’area sotto la curva delle velocità. Questo è il teorema che oggi si scrive *s* = ∫ *v* d*t*. Se la velocità parte da zero e la forza è finita, la curva delle velocità esce da A con una tangente di pendenza finita, e il Lemma IX dà *s* ∝ *t*² all’inizio del moto, **qualunque** sia la legge con cui la forza varia. Verifica con *v* = 2*t* + 5*t*² (forza crescente): *s*(*t*) / *s*(2*t*) vale 0,1538; 0,2188; 0,2460 per *t* = 1; 0,1; 0,01, e tende a 1/4.
- Il lemma presuppone che si misurino gli spazi generati dalla forza a partire dalla quiete, oppure gli scostamenti dal moto inerziale: per questo i corollari parlano di «errori».
- **Corollari 1–5.** Gli «errori» sono gli scostamenti dal luogo che il corpo raggiungerebbe in assenza della forza, cioè per la sola forza insita. In termini moderni, all’inizio del moto lo scostamento vale circa ½ *a* *t*², con *a* accelerazione prodotta dalla forza. Di qui: errori ∝ forza × *t*² (Cor. 2–3), forza ∝ spazio / *t*² (Cor. 4), *t*² ∝ spazio / forza (Cor. 5). Il fattore ½ non compare, perché Newton ragiona per proporzioni (come nel Fascicolo 3, N7). Il Cor. 4 è lo strumento con cui, nella Sezione II, si misurerà la forza centripeta dalla deviazione dalla tangente.

### N7. Scolio dopo il Lemma X: il linguaggio delle proporzionalità

Lo Scolio fissa il significato di «A sta come B direttamente, C direttamente e D inversamente»: A e BC/D stanno in un rapporto dato, cioè A = *k* · BC/D con *k* costante. Nel linguaggio di Newton il rapporto si confronta solo fra grandezze omogenee: la costante *k*, che oggi porta le unità di misura, è nascosta nel «rapporto dato». Controllo: per diverse scelte di B, C, D lo script dà sempre A / (BC/D) = 7, il valore di *k* imposto. Per la didattica: è la stessa grammatica con cui il Fascicolo 3 legge «rapporto duplicato» e «considerate congiuntamente».

### N8. Lemma XI: il cerchio osculatore senza nominarlo

- **La costruzione.** AG è perpendicolare alla tangente AD, quindi giace sulla normale alla curva in A; BG è perpendicolare alla corda AB. L’angolo ABG è retto, perciò il cerchio per A, B, G ha diametro AG ed è tangente ad AD in A. Per un cerchio di diametro AG tangente in A vale esattamente AB² = AG × BD, perché BD, perpendicolare alla tangente, è la proiezione della corda AB sul diametro.
- **Il limite.** Quando B si avvicina ad A, G tende al punto J. AJ è il **diametro del cerchio osculatore**, il doppio del raggio di curvatura ρ. La condizione «curvatura finita» dell’enunciato significa 0 < AJ < ∞. In termini moderni: BD ≈ AB² / (2ρ).
- **Verifica** (curva *y* = *x*²/4 + 0,4 *x*³, quindi ρ = 2 e AJ = 4):

| *x*_B | AB² | AG × BD | AG |
|---:|---:|---:|---:|
| 0,5 | 2,626562 · 10⁻¹ | 2,626562 · 10⁻¹ | 2,3347 |
| 0,1 | 1,000841 · 10⁻² | 1,000841 · 10⁻² | 3,4512 |
| 0,01 | 1,000006 · 10⁻⁴ | 1,000006 · 10⁻⁴ | 3,9370 |
| 0,001 | 1,000000 · 10⁻⁶ | 1,000000 · 10⁻⁶ | 3,9936 |

  L’uguaglianza AB² = AG × BD è esatta a ogni passo; AG tende ad AJ = 4.
- **Caso 2** (BD inclinata di 60° sulla tangente) e **Caso 3** (BD diretta verso il punto dato (1, −3)), confronto fra *x*_B e 2*x*_B: BD / bd vale 0,2012 → 0,2425 → 0,2492 nel Caso 2 e 0,2043 → 0,2430 → 0,2493 nel Caso 3, mentre AB² / Ab² vale 0,2445 → 0,24998 → 0,25000. I due rapporti tendono allo stesso valore 1/4.
- Il Caso 3 è quello che servirà nella dinamica: BD diretta verso un punto dato è la deviazione dalla tangente verso un **centro di forza**.

### N9. La saetta (*sagitta*) e il tempo

La **saetta** è la «freccia dell’arco»: il segmento che, come la freccia incoccata su un arco teso, va dal punto medio della corda fino all’arco. Nel Cor. 2 Newton precisa che le saette considerate «dividono a metà le corde e convergono verso un punto dato»: non sono quindi necessariamente perpendicolari alla corda. Per questo il glossario distingue *sagitta* («saetta») da *sinus versus* («seno verso»), che in un cerchio è la saetta perpendicolare; Motte li confonde, traducendo «versed sines» (§ A.14).

Il Cor. 3 unisce il Lemma XI al Lemma X: se un corpo percorre l’arco con velocità data, la lunghezza dell’arco è proporzionale al tempo, e la saetta, che sta come il quadrato dell’arco, sta come il quadrato del tempo. Verifica su un cerchio di raggio 2 percorso con velocità 1: il rapporto fra le saette (calcolate qui come seni versi) per i tempi *t* e 2*t* vale 0,250626 per *t* = 0,2 e 0,250006 per *t* = 0,02. La Prop. VI (Sezione II) cita proprio i Cor. 2 e 3 del Lemma XI e il Cor. 4 del Lemma X per misurare la forza centripeta.

### N10. Lemma XI, Cor. 4 e 5: triangoli e aree che svaniscono

Vicino ad A la curva è approssimata da una parabola, con DB proporzionale ad AD². Il triangolo ADB, che è la metà del prodotto di AD per DB, sta quindi come AD³ (rapporto triplicato) e come DB³/² (rapporto **sesquiplicato**: il «subduplicato del triplicato», cioè la radice quadrata del cubo). L’area curvilinea ADB, compresa fra la tangente, l’ordinata e l’arco, è i 2/3 del triangolo; il segmento fra la corda e l’arco è 1/3. Verifica sulla curva di N8:

| *x*_B | triangolo(*x*) / triangolo(2*x*) | (DB / db)³/² | area curvilinea / triangolo | segmento / triangolo |
|---:|---:|---:|---:|---:|
| 0,1 | 0,10985 | 0,10298 | 0,64368 | 0,35632 |
| 0,01 | 0,12306 | 0,12210 | 0,66404 | 0,33596 |
| 0,001 | 0,12480 | 0,12470 | 0,66640 | 0,33360 |

I valori tendono a 1/8, 1/8, 2/3, 1/3.

### N11. Scolio: gli angoli di contatto

L’«angolo di contatto» (l’angolo «a corno» fra una curva e la sua tangente) è una grandezza della geometria classica che non si lascia confrontare con gli angoli rettilinei: è minore di qualunque angolo rettilineo, eppure non è nullo. Newton ne fa una scala: se DB sta come AD elevato alla potenza *p*,

- per *p* = 2 la curva ha curvatura finita, come un cerchio;
- per *p* > 2 (AD³, AD⁴, …) la curvatura in A è nulla: la curva è più piatta di ogni cerchio, e nessun cerchio può passare fra essa e la tangente;
- per 1 < *p* < 2 (AD³/², AD⁴/³, …) la curvatura in A è infinita.

Due angoli con esponenti diversi stanno fra loro come un infinitesimo di ordine diverso: per AD = 10⁻⁶, AD³ / AD² vale 10⁻⁶ e AD³/² / AD² vale 10³ (controllo dello script). Fra due esponenti qualsiasi se ne possono sempre inserire altri: la serie intermedia fra 2 e 3 è 13/6, 11/5, 9/4, 7/3, 5/2, 8/3, 11/4, 14/5, 17/6. Lo script ha verificato che questi valori sono tutti compresi fra 2 e 3, crescenti, e della forma 2 + 1/*n* e 3 − 1/*n* (§ A.12). La conclusione, «la natura non conosce limite», è un’affermazione sulla densità di questa scala.

Questo Scolio spiega perché il Lemma XI richiede «curvatura finita». Le sezioni coniche non degeneri, che saranno le traiettorie delle sezioni successive, hanno in ogni punto curvatura finita e non nulla.

### N12. Scolio: limiti contro indivisibili

- **Il programma.** Newton dichiara di evitare due strade: le lunghe dimostrazioni per assurdo degli antichi (il metodo di esaustione) e il metodo degli indivisibili, più rapido ma fondato su un’ipotesi «dura», cioè che grandezze continue siano composte di parti ultime indivisibili. Sceglie i **limiti** delle somme e dei rapporti: le «particelle» e le «piccole linee curve» che userà vanno sempre intese come quantità divisibili che svaniscono.
- **La velocità ultima.** La risposta alla prima obiezione introduce, con l’esempio del corpo che si ferma, quella che oggi si chiama velocità istantanea: non la velocità prima o dopo, ma quella «con cui» il corpo arriva. Il rapporto ultimo è definito allo stesso modo.
- **Seconda obiezione.** Dare il limite di un rapporto non significa dare quantità ultime: il rapporto (*x* + *d*) / *x*, con *d* fisso, tende a 1 quando *x* cresce senza limite, ma non esiste una «quantità massima» *x*. L’esempio dell’infinitamente grande mostra che un rapporto ultimo può esistere senza che esistano le quantità ultime.
- **Euclide.** Il richiamo al libro X degli *Elementi* riguarda le grandezze incommensurabili: se ogni grandezza fosse composta di indivisibili tutti uguali, due grandezze qualsiasi sarebbero commensurabili, contro ciò che Euclide dimostra.
- Per la didattica: lo Scolio è un testo adatto a una discussione in classe sul concetto di limite, prima della definizione formale.

---

## Controllo della copertura

Le pagine 1726 sono quelle segnate nella trascrizione; le pagine di Motte 1846 sono quelle dei marcatori dell’EPUB Gutenberg.

| Identificatori | Incipit latino | Contenuto | 1726 | Motte 1846 |
|---|---|---|---|---|
| — | *De motu corporum liber primus. Sectio I.* | intestazione e titolo della Sezione | p. 28 | p. 95 |
| S1.01–S1.02 | *Quantitates, ut & quantitatum rationes* | Lemma I | p. 28 | p. 95 |
| S1.03–S1.04 | *Si in figura quavis AacE* | Lemma II | pp. 28–29 | pp. 95–96 |
| S1.05–S1.10 | *Eædem rationes ultimæ* | Lemma III e Cor. 1–4 | p. 29 | p. 96 |
| S1.11–S1.13 | *Si in duabus figuris AacE, PprT* | Lemma IV e Cor. | pp. 29–30 | pp. 96–97 |
| S1.14 | *Similium figurarum latera omnia* | Lemma V | p. 30 | p. 97 |
| S1.15–S1.16 | *Si arcus quilibet positione datus* | Lemma VI | p. 31 | p. 97 |
| S1.17–S1.21 | *Iisdem positis* | Lemma VII e Cor. 1–3 | pp. 31–32 | pp. 97–98 |
| S1.22–S1.24 | *Si rectæ datæ AR, BR* | Lemma VIII e Cor. | p. 32 | p. 98 |
| S1.25–S1.26 | *Si recta AE & curva ABC* | Lemma IX | pp. 32–33 | pp. 98–99 |
| S1.27–S1.28 | *Spatia quæ corpus urgente* | Lemma X | p. 33 | p. 99 |
| S1.29–S1.33 | *Et hinc facile colligitur* | Lemma X, Cor. 1–5 | p. 34 | pp. 99–100 |
| S1.34 | *Si quantitates indeterminatæ* | Scolio (proporzionalità) | p. 34 | p. 100 |
| S1.35–S1.38 | *Subtensa evanescens anguli contactus* | Lemma XI, Casi 1–3 | pp. 34–35 | pp. 100–101 |
| S1.39–S1.41 | *Unde cum tangentes AD, Ad* | Lemma XI, Cor. 1–3 | p. 35 | p. 101 |
| S1.42–S1.43 | *Triangula rectilinea ADB, Adb* | Lemma XI, Cor. 4–5 | p. 36 | p. 101 |
| S1.44–S1.45 | *Cæterum in his omnibus* | Scolio: angoli di contatto | pp. 36–37 | pp. 101–102 |
| S1.46 | *Quæ de curvis lineis* | Scolio: limiti e indivisibili | p. 37 | p. 102 |
| S1.47 | *Objectio est* | Scolio: prima obiezione, velocità ultima | pp. 37–38 | pp. 102–103 |
| S1.48 | *Contendi etiam potest* | Scolio: seconda obiezione | p. 38 | p. 103 |

**Controlli eseguiti.**

1. **Rilettura frase per frase contro il latino.** Ho confrontato in sequenza ogni periodo della trascrizione, da *De motu corporum liber primus* a *cogita semper diminuendas sine limite*, con la traduzione. Nessuna frase manca. Nei periodi lunghi (Lemma II, Lemma X Cor. 1, Scolio finale) l’italiano conserva tutti i membri; dove li divide, lo fa senza omissioni. Le 43 stringhe latine della Parte B (11 enunciati e 32 passi) sono sottostringhe esatte della trascrizione, e le 43 stringhe inglesi sono sottostringhe esatte di Motte: `check.py` passa senza errori e senza avvisi.
2. **Matematica.** Con uno script Python ho verificato: Lemmi II–III (differenza delle somme = AB · Aa; maggiorazione AF · Aa), VII (arco, corda e tangente), VIII (rapporti dei triangoli), IX (rapporto duplicato delle aree), X (spazi ∝ *t*²), XI (identità AB² = AG × BD; AG → AJ; Casi 2 e 3), Cor. 3 (saetta ∝ *t*²), Cor. 4–5 (rapporti triplicato e sesquiplicato; 2/3 e 1/3), Scolio dopo il Lemma X (A ∝ BC/D), Scolio finale (esponenti delle serie). Tutti i risultati concordano con il testo (note N2–N11).
3. **Confronto con Motte.** Ho confrontato tutta la sezione, pp. 95–103, comprese le formule SVG 1–27 lette dagli attributi `data-tex` (le SVG 1, 3, 13 e 19 anche sull’immagine). Divergenze nel § A.14; le più rilevanti sono la formula A × C × 1/D (SVG 1), l’accoppiamento errato del Lemma XI, Cor. 4, e la resa di *sagitta* con «versed sine».
4. **Separazione fra testo e commento.** Il testo tradotto non contiene formule moderne; gli esponenti e i prodotti sono scritti come nel latino (AB², AG × BD, AD³/²).

**Non ho potuto verificare:**

- **la stampa del 1726**: tutti i refusi segnalati nel § A.13 (*paralella*, *occurant*, *constitui*, *saggitæ*, *augetur*, *ABC* nel Lemma VI, *imaginationi conceptui*) sono annotati come probabili o da verificare, non accertati;
- **le figure NATP00087-1…8**: in particolare la posizione di R nel Lemma VIII, dei punti E, G nel Cor. 2 del Lemma VII e dei punti C, c nel Lemma XI, Cor. 1 e 4, ricostruite solo dalle lettere;
- **Motte 1729**, per stabilire se la formula A × C × 1/D e gli altri refusi di Motte siano dell’edizione 1846 o già della prima;
- **la numerazione di pagina di Motte**, che deriva dai marcatori dell’EPUB e non da un esemplare a stampa.

---

## Registro del lavoro successivo

| Unità | Stato |
|---|---|
| Libro I, Sezione I: Lemmi I–XI, corollari, scolii | **Fascicolo 4, presente documento, prima versione** |
| Lemma I, *constanter* | Applicata la decisione del curatore: «tendono senza interruzione» (S1.01 e Parte B) |
| Riscontro sulla stampa del 1726 dei punti del § A.13 | Da eseguire, come nel Fascicolo 3 v0.3 |
| Figure NATP00087-1…8 | Da vedere: confermare R (Lemma VIII), E e G (Lemma VII, Cor. 2), C e c (Lemma XI) |
| Motte 1729, Sezione I | Da controllare: SVG 1 (A × C × 1/D), «Bd», «DC», «AB, AB», Cor. 4 del Lemma XI |
| *facili rerum imaginationi conceptui consulens* | Lettura incerta: verificare sulla stampa e decidere la resa |
| Pagine interattive candidate | Lemma XI (base della Prop. VI e della misura della forza centripeta), Lemmi II–III (somme di Riemann), Lemma VII (figura ingrandita), Lemma X (spazi ∝ *t*²) |
| Testo a fronte di Motte nelle pagine | Correggere con nota: Scolio dopo il Lemma X (B × C × 1/D), Lemma XI Caso 1 (BD) e Cor. 4–5 |
| Revisione filologica e scientifica indipendente | Da eseguire, come previsto dalla skill di verifica |

Il presente testo è una nuova traduzione assistita da IA. Non riproduce traduzioni italiane o inglesi moderne. **Licenza prevista** (decisione del curatore): testi e traduzioni CC BY-SA 4.0, codice MIT. La trascrizione latina è © The Newton Project e non va ridistribuita finché non se ne chiariscono le condizioni d’uso; il testo di Motte è di pubblico dominio.

---

## Parte B — Dati per le pagine interattive

Unità incluse: i lemmi con figura o costruzione geometrica e dimostrazione (II, III, IV, VI, VII, VIII, IX, X, XI) e i due corollari che hanno una dimostrazione propria legata a una figura propria (Lemma VII, Cor. 1, figura 4; Lemma XI, Cor. 4, figura 8). Esclusi: il Lemma I (senza figura), il Lemma V (senza dimostrazione), i corollari che non hanno una dimostrazione propria con figura, e gli scolii.

Convenzioni:

- `la`: testo latino esatto della trascrizione, refusi compresi, con i cambi di pagina normalizzati come nello script di controllo (*circum scripta*, *parallelo gramma*, *ordi natim*); i refusi sono annotati in `nota`;
- `it`: la traduzione di questo fascicolo;
- `en`: Motte 1846, allineato per senso; le formule stampate come immagini compaiono come `[SVG n]` e sono sciolte in `nota`;
- `dipende_da`: soltanto i rimandi citati davvero nella frase;
- `figura.mostra`: elementi da rendere visibili al passo, cumulativi; `figura.evidenzia`: relazioni da mettere in risalto.

```json
{
  "fascicolo": "04-L1-S1",
  "versione": "0.1",
  "data": "2026-11-08",
  "convenzioni": {
    "dipende_da": "solo rimandi citati esplicitamente nella frase",
    "en": "Motte 1846, allineato per senso; [SVG n] = formula stampata come immagine, sciolta in nota",
    "figura.mostra": "elementi da rendere visibili al passo, cumulativi salvo indicazione",
    "la": ""
  },
  "unita": [
    {
      "id": "L1-Lem2",
      "tipo": "Lemma",
      "titolo": "Lemma II — figura inscritta e circoscritta (basi uguali)",
      "copertura": [
        "S1.03",
        "S1.04"
      ],
      "fonti": {
        "la": "",
        "en": "Motte 1846, pp. 95–96"
      },
      "enunciato": {
        "la": "",
        "it": "Se in una figura qualsiasi AacE, compresa fra le rette Aa, AE e la curva acE, si inscrivono quanti si vogliano parallelogrammi Ab, Bc, Cd, ecc., contenuti sotto basi uguali AB, BC, CD, ecc. e sotto lati Bb, Cc, Dd, ecc. paralleli al lato Aa della figura; e si completano i parallelogrammi aKbl, bLcm, cMdn, ecc.; e poi la larghezza di questi parallelogrammi diminuisce e il loro numero aumenta all’infinito: dico che i rapporti ultimi che hanno fra loro la figura inscritta AKbLcMdD, la circoscritta AalbmcndoE e la curvilinea AabcdE sono rapporti di uguaglianza.",
        "en": "If in any figure AacE, terminated by the right lines Aa, AE, and the curve acE, there be inscribed any number of parallelograms Ab, Bc, Cd, &c., comprehended under equal bases AB, BC, CD, &c., and the sides, Bb, Cc, Dd, &c., parallel to one side Aa of the figure; and the parallelograms aKbl, bLcm, cMdn, &c., are completed. Then if the breadth of those parallelograms be supposed to be diminished, and their number to be augmented in infinitum; I say, that the ultimate ratios which the inscribed figure AKbLcMdD, the circumscribed figure AalbmcndoE, and curvilinear figure AabcdE, will have to one another, are ratios of equality."
      },
      "nota": "«circum scripta»: il cambio di pagina <29> spezza circumscripta nella trascrizione.",
      "figura_base": {
        "punti": [
          "A",
          "a",
          "E",
          "B",
          "C",
          "D",
          "b",
          "c",
          "d",
          "K",
          "L",
          "M",
          "l",
          "m",
          "n",
          "o"
        ],
        "vincoli": [
          "Aa e AE rette; acE curva che scende in modo monotono da a fino a E sulla retta AE (presupposto dalla figura)",
          "AB = BC = CD = … basi uguali su AE",
          "Bb, Cc, Dd ∥ Aa, con b, c, d sulla curva",
          "aKbl, bLcm, cMdn parallelogrammi completati: K, L, M sui lati Aa, Bb, Cc all’altezza di b, c, d; l, m, n, o alle altezze di a, b, c, d sui lati successivi",
          "figura inscritta AKbLcMdD, circoscritta AalbmcndoE, curvilinea AabcdE"
        ]
      },
      "passi": [
        {
          "id": "L1-Lem2-p1",
          "la": "",
          "it": "Infatti la differenza fra la figura inscritta e la circoscritta è la somma dei parallelogrammi Kl, Lm, Mn, Do, cioè (poiché le basi di tutti sono uguali) il rettangolo compreso sotto la base Kb di uno solo di essi e la somma delle altezze Aa, cioè il rettangolo ABla.",
          "en": "For the difference of the inscribed and circumscribed figures is the sum of the parallelograms Kl, Lm, Mn, Do, that is (from the equality of all their bases), the rectangle under one of their bases Kb and the sum of their altitudes Aa, that is, the rectangle ABla.",
          "dipende_da": [],
          "figura": {
            "mostra": [
              "figura inscritta",
              "figura circoscritta",
              "parallelogrammi Kl, Lm, Mn, Do",
              "rettangolo ABla"
            ],
            "evidenzia": [
              "Kl + Lm + Mn + Do = ABla (impilati)"
            ]
          },
          "nota": "La somma delle altezze è Aa perché la curva scende fino a E (nota N2)."
        },
        {
          "id": "L1-Lem2-p2",
          "la": "",
          "it": "Ma questo rettangolo, poiché la sua larghezza AB diminuisce all’infinito, diventa minore di qualunque grandezza data.",
          "en": "But this rectangle, because its breadth AB is supposed diminished in infinitum, becomes less than any given space.",
          "dipende_da": [],
          "figura": {
            "mostra": [
              "cursore: numero di parallelogrammi",
              "rettangolo ABla che si assottiglia"
            ],
            "evidenzia": [
              "larghezza AB → 0"
            ]
          },
          "nota": "Motte aggiunge «supposed» e «space»."
        },
        {
          "id": "L1-Lem2-p3",
          "la": "",
          "it": "Dunque (per il Lemma I) la figura inscritta e la circoscritta, e a maggior ragione la figura curvilinea intermedia, diventano alla fine uguali.",
          "en": "And therefore (by Lem. I) the figures inscribed and circumscribed become ultimately equal one to the other; and much more will the intermediate curvilinear figure be ultimately equal to either.",
          "dipende_da": [
            "Lemma I"
          ],
          "figura": {
            "mostra": [
              "figura curvilinea AabcdE fra le due"
            ],
            "evidenzia": [
              "inscritta/curvilinea → 1, circoscritta/curvilinea → 1"
            ]
          }
        }
      ]
    },
    {
      "id": "L1-Lem3",
      "tipo": "Lemma",
      "titolo": "Lemma III — basi disuguali",
      "copertura": [
        "S1.05",
        "S1.06"
      ],
      "fonti": {
        "la": "",
        "en": "Motte 1846, p. 96"
      },
      "enunciato": {
        "la": "",
        "it": "Gli stessi rapporti ultimi sono ancora rapporti di uguaglianza quando le larghezze AB, BC, CD, ecc. dei parallelogrammi sono disuguali e diminuiscono tutte all’infinito.",
        "en": "The same ultimate ratios are also ratios of equality, when the breadths, AB, BC, DC, &c., of the parallelograms are unequal, and are all diminished in infinitum."
      },
      "nota": "Motte scrive DC per CD. Il latino non ha [FIG]: la costruzione usa la figura del Lemma II con larghezze disuguali.",
      "figura_base": {
        "punti": [
          "A",
          "a",
          "E",
          "B",
          "C",
          "D",
          "F",
          "f"
        ],
        "vincoli": [
          "come nel Lemma II, ma AB, BC, CD disuguali",
          "AF uguale alla larghezza massima, sulla retta AE",
          "FAaf parallelogramma di altezza Aa"
        ]
      },
      "passi": [
        {
          "id": "L1-Lem3-p1",
          "la": "",
          "it": "Sia infatti AF uguale alla larghezza massima, e si completi il parallelogramma FAaf.",
          "en": "For suppose AF equal to the greatest breadth, and complete the parallelogram FAaf.",
          "dipende_da": [],
          "figura": {
            "mostra": [
              "parallelogrammi di larghezze disuguali",
              "AF = larghezza massima",
              "parallelogramma FAaf"
            ],
            "evidenzia": [
              "AF"
            ]
          }
        },
        {
          "id": "L1-Lem3-p2",
          "la": "",
          "it": "Questo sarà maggiore della differenza fra la figura inscritta e la figura circoscritta; ma, diminuita all’infinito la sua larghezza AF, diventerà minore di qualunque rettangolo dato.",
          "en": "This parallelogram will be greater than the difference of the inscribed and circumscribed figures; but, because its breadth AF is diminished in infinitum, it will become less than any given rectangle.",
          "dipende_da": [],
          "figura": {
            "mostra": [
              "differenza inscritta–circoscritta accanto a FAaf"
            ],
            "evidenzia": [
              "differenza ≤ FAaf",
              "AF → 0"
            ]
          },
          "nota": "Il testo non cita il Lemma I, che è però sottinteso come nel Lemma II."
        }
      ]
    },
    {
      "id": "L1-Lem4",
      "tipo": "Lemma",
      "titolo": "Lemma IV — rapporto di due figure",
      "copertura": [
        "S1.11",
        "S1.12"
      ],
      "fonti": {
        "la": "",
        "en": "Motte 1846, p. 96"
      },
      "enunciato": {
        "la": "",
        "it": "Se in due figure AacE, PprT si inscrivono (come sopra) due serie di parallelogrammi, e il numero è lo stesso in entrambe, e, quando le larghezze diminuiscono all’infinito, i rapporti ultimi dei parallelogrammi dell’una figura ai parallelogrammi dell’altra, ciascuno al corrispondente, sono gli stessi: dico che le due figure AacE, PprT stanno fra loro in quello stesso rapporto.",
        "en": "If in two figures AacE, PprT, you inscribe (as before) two ranks of parallelograms, an equal number in each rank, and, when their breadths are diminished in infinitum, the ultimate ratios of the parallelograms in one figure to those in the other, each to each respectively, are the same; I say, that those two figures AacE, PprT, are to one another in that same ratio."
      },
      "nota": "«parallelo gramma»: cambio di pagina <30> nella trascrizione.",
      "figura_base": {
        "punti": [
          "A",
          "a",
          "c",
          "E",
          "P",
          "p",
          "r",
          "T"
        ],
        "vincoli": [
          "due figure AacE, PprT come nel Lemma II",
          "stesso numero di parallelogrammi inscritti in ciascuna",
          "rapporto ultimo fra parallelogrammi corrispondenti uguale per tutti"
        ]
      },
      "passi": [
        {
          "id": "L1-Lem4-p1",
          "la": "",
          "it": "Infatti, come i parallelogrammi stanno uno per uno ai parallelogrammi, così (componendo) la somma di tutti sta alla somma di tutti, e così la figura alla figura; poiché, beninteso, la prima figura sta alla prima somma (per il Lemma III), e la seconda figura alla seconda somma, in rapporto di uguaglianza.",
          "en": "For as the parallelograms in the one are severally to the parallelograms in the other, so (by composition) is the sum of all in the one to the sum of all in the other; and so is the one figure to the other; because (by Lem. III) the former figure to the former sum, and the latter figure to the latter sum, are both in the ratio of equality.",
          "dipende_da": [
            "Lemma III"
          ],
          "figura": {
            "mostra": [
              "coppie di parallelogrammi corrispondenti",
              "somme nelle due figure"
            ],
            "evidenzia": [
              "parallelogramma : parallelogramma = somma : somma = figura : figura"
            ]
          }
        }
      ]
    },
    {
      "id": "L1-Lem6",
      "tipo": "Lemma",
      "titolo": "Lemma VI — l’angolo fra corda e tangente svanisce",
      "copertura": [
        "S1.15",
        "S1.16"
      ],
      "fonti": {
        "la": "",
        "en": "Motte 1846, p. 97"
      },
      "enunciato": {
        "la": "",
        "it": "Se un arco qualsiasi ABC, dato di posizione, è sotteso dalla corda AB, e in un punto A, posto nel mezzo di una curvatura continua, è toccato da una retta AD prolungata da entrambe le parti; e poi i punti A, B si avvicinano l’uno all’altro e si riuniscono: dico che l’angolo BAD, compreso fra la corda e la tangente, diminuirà all’infinito e alla fine svanirà.",
        "en": "If any arc ACB, given in position is subtended by its chord AB, and in any point A, in the middle of the continued curvature, is touched by a right line AD, produced both ways; then if the points A and B approach one another and meet, I say, the angle BAD, contained between the chord and the tangent, will be diminished in infinitum, and ultimately will vanish."
      },
      "nota": "L’enunciato latino ha ABC, la dimostrazione ACB; Motte ha ACB (apparato A.6).",
      "figura_base": {
        "punti": [
          "A",
          "B",
          "C",
          "D"
        ],
        "vincoli": [
          "arco ACB dato di posizione, C punto intermedio",
          "AB corda",
          "AD tangente in A, prolungata da entrambe le parti",
          "B si avvicina ad A lungo l’arco"
        ]
      },
      "passi": [
        {
          "id": "L1-Lem6-p1",
          "la": "",
          "it": "Infatti, se quell’angolo non svanisce, l’arco ACB conterrà con la tangente AD un angolo uguale a un angolo rettilineo, e perciò la curvatura nel punto A non sarà continua, contro l’ipotesi.",
          "en": "For if that angle does not vanish, the arc ACB will contain with the tangent AD an angle equal to a rectilinear angle; and therefore the curvature at the point A will not be continued, which is against the supposition.",
          "dipende_da": [],
          "figura": {
            "mostra": [
              "angolo BAD",
              "cursore: B → A",
              "controesempio: curva con punto angoloso in A"
            ],
            "evidenzia": [
              "angolo BAD → 0"
            ]
          }
        }
      ]
    },
    {
      "id": "L1-Lem7",
      "tipo": "Lemma",
      "titolo": "Lemma VII — arco, corda e tangente",
      "copertura": [
        "S1.17",
        "S1.18"
      ],
      "fonti": {
        "la": "",
        "en": "Motte 1846, pp. 97–98"
      },
      "enunciato": {
        "la": "",
        "it": "Poste le stesse cose, dico che il rapporto ultimo dell’arco, della corda e della tangente fra loro è il rapporto di uguaglianza.",
        "en": "The same things being supposed, I say that the ultimate ratio of the arc, chord, and tangent, any one to any other, is the ratio of equality."
      },
      "figura_base": {
        "punti": [
          "A",
          "B",
          "C",
          "D",
          "b",
          "c",
          "d"
        ],
        "vincoli": [
          "come nel Lemma VI",
          "BD secante da B alla tangente",
          "b su AB prolungata, d su AD prolungata, bd ∥ BD",
          "Ab, Ad restano finite",
          "arco Acb simile all’arco ACB"
        ]
      },
      "passi": [
        {
          "id": "L1-Lem7-p1",
          "la": "",
          "it": "Infatti, mentre il punto B si avvicina al punto A, si immaginino sempre AB e AD prolungate fino ai punti lontani b e d, e si conduca bd parallela alla secante BD.",
          "en": "For while the point B approaches towards the point A, consider always AB and AD as produced to the remote points b and d, and parallel to the secant BD draw bd",
          "dipende_da": [],
          "figura": {
            "mostra": [
              "secante BD",
              "AB prolungata fino a b",
              "AD prolungata fino a d",
              "bd ∥ BD"
            ],
            "evidenzia": [
              "bd ∥ BD"
            ]
          }
        },
        {
          "id": "L1-Lem7-p2",
          "la": "",
          "it": "E l’arco Acb sia sempre simile all’arco ACB.",
          "en": "and let the arc Acb be always similar to the arc ACB.",
          "dipende_da": [],
          "figura": {
            "mostra": [
              "arco Acb (copia ingrandita di ACB)"
            ],
            "evidenzia": [
              "similitudine ACB ~ Acb"
            ]
          },
          "nota": "Motte unisce questa frase alla precedente."
        },
        {
          "id": "L1-Lem7-p3",
          "la": "",
          "it": "Quando i punti A, B si riuniscono, l’angolo dAb, per il lemma precedente, svanirà; e perciò le rette Ab, Ad, che restano sempre finite, e l’arco intermedio Acb coincideranno, e quindi saranno uguali.",
          "en": "Then, supposing the points A and B to coincide, the angle dAb will vanish, by the preceding Lemma; and therefore the right lines Ab, Ad (which are always finite), and the intermediate arc Acb, will coincide, and become equal among themselves.",
          "dipende_da": [
            "Lemma VI"
          ],
          "figura": {
            "mostra": [
              "cursore: B → A con Ad fisso",
              "angolo dAb"
            ],
            "evidenzia": [
              "Ab, Ad, Acb si sovrappongono"
            ]
          },
          "nota": "«per lemma superius» = Lemma VI."
        },
        {
          "id": "L1-Lem7-p4",
          "la": "",
          "it": "Di conseguenza anche le rette AB, AD e l’arco intermedio ACB, sempre proporzionali a queste, svaniranno e avranno il rapporto ultimo di uguaglianza.",
          "en": "Wherefore, the right lines AB, AD, and the intermediate arc ACB (which are always proportional to the former), will vanish, and ultimately acquire the ratio of equality.",
          "dipende_da": [],
          "figura": {
            "mostra": [
              "rapporti arco/corda e tangente/corda"
            ],
            "evidenzia": [
              "rapporti → 1 (nota N5)"
            ]
          }
        }
      ]
    },
    {
      "id": "L1-Lem7-Cor1",
      "tipo": "Corollarium",
      "titolo": "Lemma VII, Cor. 1 — la parallela alla tangente",
      "copertura": [
        "S1.19"
      ],
      "fonti": {
        "la": "",
        "en": "Motte 1846, p. 98"
      },
      "enunciato": {
        "la": "",
        "it": "Se dunque per B si conduce BF parallela alla tangente, che tagli sempre in F una retta qualsiasi AF passante per A, questa BF avrà alla fine con l’arco evanescente ACB rapporto di uguaglianza.",
        "en": "Whence if through B we draw BF parallel to the tangent, always cutting any right line AF passing through A in F, this line BF will be ultimately in the ratio of equality with the evanescent arc ACB"
      },
      "nota": "Enunciato e dimostrazione formano un’unica frase latina; l’enunciato riporta la parte principale, il passo l’intera frase.",
      "figura_base": {
        "punti": [
          "A",
          "B",
          "C",
          "D",
          "F"
        ],
        "vincoli": [
          "AD tangente in A",
          "BF ∥ AD",
          "AF retta qualsiasi per A",
          "AFBD parallelogramma: BD ∥ AF, quindi BF = AD"
        ]
      },
      "passi": [
        {
          "id": "L1-Lem7-Cor1-p1",
          "la": "",
          "it": "Se dunque per B si conduce BF parallela alla tangente, che tagli sempre in F una retta qualsiasi AF passante per A, questa BF avrà alla fine con l’arco evanescente ACB rapporto di uguaglianza, perché, completato il parallelogramma AFBD, ha sempre rapporto di uguaglianza con AD.",
          "en": "Whence if through B we draw BF parallel to the tangent, always cutting any right line AF passing through A in F, this line BF will be ultimately in the ratio of equality with the evanescent arc ACB; because, completing the parallelogram AFBD, it is always in a ratio of equality with AD.",
          "dipende_da": [],
          "figura": {
            "mostra": [
              "BF ∥ AD",
              "retta AF",
              "parallelogramma AFBD"
            ],
            "evidenzia": [
              "BF = AD sempre",
              "AD : arco ACB → 1 (Lemma VII)"
            ]
          },
          "nota": "«Unde» rimanda al Lemma VII senza citarlo esplicitamente."
        }
      ]
    },
    {
      "id": "L1-Lem8",
      "tipo": "Lemma",
      "titolo": "Lemma VIII — triangoli evanescenti",
      "copertura": [
        "S1.22",
        "S1.23"
      ],
      "fonti": {
        "la": "",
        "en": "Motte 1846, p. 98"
      },
      "enunciato": {
        "la": "",
        "it": "Se le rette date AR, BR, con l’arco ACB, la corda AB e la tangente AD, formano tre triangoli RAB, RACB, RAD, e poi i punti A, B si avvicinano l’uno all’altro: dico che la forma ultima dei triangoli evanescenti è quella della similitudine, e il rapporto ultimo quello dell’uguaglianza.",
        "en": "If the right lines AR, BR, with the arc ACB, the chord AB, and the tangent AD, constitute three triangles RAB, RACB, RAD, and the points A and B approach and meet: I say, that the ultimate form of these evanescent triangles is that of similitude, and their ultimate ratio that of equality."
      },
      "nota": "«AD,triangula» senza spazio nella trascrizione. Motte omette «datæ».",
      "figura_base": {
        "punti": [
          "A",
          "B",
          "C",
          "D",
          "R",
          "b",
          "c",
          "d",
          "r"
        ],
        "vincoli": [
          "AR, BR rette date",
          "R, B, D allineati: D è l’intersezione di RB con la tangente AD (da «RD» e «rbd»)",
          "b, d, r su AB, AD, AR prolungate; rbd ∥ RD",
          "arco Acb simile ad ACB",
          "posizione esatta di R non ricostruibile senza la figura (apparato A.8)"
        ]
      },
      "passi": [
        {
          "id": "L1-Lem8-p1",
          "la": "",
          "it": "Infatti, mentre il punto B si avvicina al punto A, si immaginino sempre AB, AD, AR prolungate fino ai punti lontani b, d e r; si conduca rbd parallela a RD; e l’arco Acb sia sempre simile all’arco ACB.",
          "en": "For while the point B approaches towards the point A, consider always AB, AD, AR, as produced to the remote points b, d, and r, and rbd as drawn parallel to RD, and let the arc Acb be always similar to the arc ACB.",
          "dipende_da": [],
          "figura": {
            "mostra": [
              "triangoli RAB, RACB, RAD",
              "prolungamenti fino a b, d, r",
              "rbd ∥ RD",
              "arco Acb"
            ],
            "evidenzia": [
              "figura ingrandita rAb, rAcb, rAd"
            ]
          },
          "nota": "«paralella»: refuso probabile della trascrizione per «parallela»."
        },
        {
          "id": "L1-Lem8-p2",
          "la": "",
          "it": "Quando i punti A, B si riuniscono, l’angolo bAd svanirà, e perciò i tre triangoli rAb, rAcb, rAd, che restano sempre finiti, coincideranno, e per questa ragione sono simili e uguali.",
          "en": "Then supposing the points A and B to coincide, the angle bAd will vanish; and therefore the three triangles rAb, rAcb, rAd (which are always finite), will coincide, and on that account become both similar and equal.",
          "dipende_da": [],
          "figura": {
            "mostra": [
              "cursore: B → A",
              "angolo bAd"
            ],
            "evidenzia": [
              "rAb, rAcb, rAd si sovrappongono"
            ]
          },
          "nota": "Il lemma precedente (VI) è sottinteso, ma non citato."
        },
        {
          "id": "L1-Lem8-p3",
          "la": "",
          "it": "Di conseguenza anche RAB, RACB, RAD, sempre simili e proporzionali a questi, diventeranno alla fine simili e uguali fra loro.",
          "en": "And therefore the triangles RAB, RACB, RAD which are always similar and proportional to these, will ultimately become both similar and equal among themselves.",
          "dipende_da": [],
          "figura": {
            "mostra": [
              "rapporti RAB : RAD e RACB : RAD"
            ],
            "evidenzia": [
              "rapporti → 1 (nota N5)"
            ]
          }
        }
      ]
    },
    {
      "id": "L1-Lem9",
      "tipo": "Lemma",
      "titolo": "Lemma IX — aree evanescenti in rapporto duplicato dei lati",
      "copertura": [
        "S1.25",
        "S1.26"
      ],
      "fonti": {
        "la": "",
        "en": "Motte 1846, pp. 98–99"
      },
      "enunciato": {
        "la": "",
        "it": "Se la retta AE e la curva ABC, date di posizione, si tagliano a vicenda in un angolo dato A, e alla retta, in un altro angolo dato, si conducono come ordinate BD, CE, che incontrano la curva in B, C; e poi i punti B, C si avvicinano insieme al punto A: dico che le aree dei triangoli ABD, ACE staranno alla fine fra loro in rapporto duplicato dei lati.",
        "en": "If a right line AE, and a curve line ABC, both given by position, cut each other in a given angle, A; and to that right line, in another given angle, BD, CE are ordinately applied, meeting the curve in B, C; and the points B and C together approach towards and meet in the point A: I say, that the areas of the triangles ABD, ACE, will ultimately be one to the other in the duplicate ratio of the sides."
      },
      "nota": "«ordi natim»: cambio di pagina <33>. I «triangoli» ABD, ACE sono curvilinei (lati AD, DB e arco AB).",
      "figura_base": {
        "punti": [
          "A",
          "B",
          "C",
          "D",
          "E",
          "b",
          "c",
          "d",
          "e",
          "F",
          "G",
          "f",
          "g"
        ],
        "vincoli": [
          "AE retta e ABC curva, che si tagliano in A con angolo dato",
          "BD, CE ordinate inclinate di un angolo dato su AE",
          "Ad, Ae proporzionali ad AD, AE; db, ec ∥ DB, EC; b, c su AB, AC prolungate",
          "curva Abc simile ad ABC",
          "Ag tangente comune in A, taglia DB, EC, db, ec in F, G, f, g",
          "Ae resta fissa mentre B, C → A"
        ]
      },
      "passi": [
        {
          "id": "L1-Lem9-p1",
          "la": "",
          "it": "Infatti, mentre i punti B, C si avvicinano al punto A, si immagini sempre AD prolungata fino ai punti lontani d ed e, in modo che Ad, Ae siano proporzionali ad AD, AE; e si innalzino le ordinate db, ec, parallele alle ordinate DB, EC, che incontrino in b e c le AB, AC prolungate.",
          "en": "For while the points B, C, approach towards the point A, suppose always AD to be produced to the remote points d and e, so as Ad, Ae may be proportional to AD, AE; and the ordinates db, ec, to be drawn parallel to the ordinates DB and EC, and meeting AB and AC produced in b and c.",
          "dipende_da": [],
          "figura": {
            "mostra": [
              "retta AE",
              "curva ABC",
              "ordinate DB, EC",
              "punti d, e",
              "ordinate db, ec",
              "rette AB, AC prolungate fino a b, c"
            ],
            "evidenzia": [
              "Ad : Ae = AD : AE"
            ]
          },
          "nota": "«occurant»: refuso probabile della trascrizione per «occurrant»."
        },
        {
          "id": "L1-Lem9-p2",
          "la": "",
          "it": "Si immagini di condurre sia la curva Abc simile alla ABC, sia la retta Ag, che tocchi entrambe le curve in A e tagli le ordinate DB, EC, db, ec in F, G, f, g.",
          "en": "Let the curve Abc be similar to the curve ABC, and draw the right line Ag so as to touch both curves in A, and cut the ordinates DB, EC, db, ec, in F, G, f, g.",
          "dipende_da": [],
          "figura": {
            "mostra": [
              "curva Abc",
              "tangente Ag",
              "punti F, G, f, g"
            ],
            "evidenzia": [
              "Ag tangente comune in A"
            ]
          }
        },
        {
          "id": "L1-Lem9-p3",
          "la": "",
          "it": "Poi, restando invariata la lunghezza Ae, i punti B, C si riuniscano con il punto A; e, svanendo l’angolo cAg, le aree curvilinee Abd, Ace coincideranno con le rettilinee Afd, Age; e perciò (per il Lemma V) staranno in rapporto duplicato dei lati Ad, Ae.",
          "en": "Then, supposing the length Ae to remain the same, let the points B and C meet in the point A; and the angle cAg vanishing, the curvilinear areas Abd, Ace will coincide with the rectilinear areas Afd, Age; and therefore (by Lem. V) will be one to the other in the duplicate ratio of the sides Ad, Ae.",
          "dipende_da": [
            "Lemma V"
          ],
          "figura": {
            "mostra": [
              "cursore: B, C → A con Ae fisso",
              "aree Abd, Ace",
              "triangoli Afd, Age"
            ],
            "evidenzia": [
              "Abd → Afd, Ace → Age",
              "Afd : Age = (Ad : Ae)²"
            ]
          },
          "nota": "Il periodo latino prosegue dopo i due punti con «Sed»: diviso in due passi."
        },
        {
          "id": "L1-Lem9-p4",
          "la": "",
          "it": "Ma a queste aree sono sempre proporzionali le aree ABD, ACE, e a questi lati i lati AD, AE.",
          "en": "But the areas ABD, ACE are always proportional to these areas; and so the sides AD, AE are to these sides.",
          "dipende_da": [],
          "figura": {
            "mostra": [
              "aree ABD, ACE nella figura piccola"
            ],
            "evidenzia": [
              "ABD : Abd = ACE : Ace"
            ]
          }
        },
        {
          "id": "L1-Lem9-p5",
          "la": "",
          "it": "Dunque anche le aree ABD, ACE stanno alla fine in rapporto duplicato dei lati AD, AE.",
          "en": "And therefore the areas ABD, ACE are ultimately one to the other in the duplicate ratio of the sides AD, AE.",
          "dipende_da": [],
          "figura": {
            "mostra": [
              "rapporto ABD : ACE"
            ],
            "evidenzia": [
              "ABD : ACE → (AD : AE)² (nota N6)"
            ]
          }
        }
      ]
    },
    {
      "id": "L1-Lem10",
      "tipo": "Lemma",
      "titolo": "Lemma X — spazi descritti all’inizio del moto",
      "copertura": [
        "S1.27",
        "S1.28"
      ],
      "fonti": {
        "la": "",
        "en": "Motte 1846, p. 99"
      },
      "enunciato": {
        "la": "",
        "it": "Gli spazi che un corpo, sollecitato da una forza finita qualsiasi, descrive, sia che quella forza sia determinata e immutabile, sia che aumenti continuamente o diminuisca continuamente, stanno, proprio all’inizio del moto, in rapporto duplicato dei tempi.",
        "en": "The spaces which a body describes by any finite force urging it, whether that force is determined and immutable, or is continually augmented or continually diminished, are in the very beginning of the motion one to the other in the duplicate ratio of the times."
      },
      "nota": "«augetur … diminuatur»: modi verbali incoerenti nella trascrizione (apparato A.10).",
      "figura_base": {
        "punti": [
          "A",
          "D",
          "E",
          "B",
          "C"
        ],
        "vincoli": [
          "AD, AE tempi sull’asse",
          "DB, EC velocità generate (ordinate)",
          "curva delle velocità ABC che parte da A (velocità iniziale nulla)",
          "spazi = aree ABD, ACE"
        ]
      },
      "passi": [
        {
          "id": "L1-Lem10-p1",
          "la": "",
          "it": "Si rappresentino i tempi con le linee AD, AE, e le velocità generate con le ordinate DB, EC; e gli spazi descritti con queste velocità staranno come le aree ABD, ACE descritte da queste ordinate, cioè, proprio all’inizio del moto (per il Lemma IX), in rapporto duplicato dei tempi AD, AE.",
          "en": "Let the times be represented by the lines AD, AE, and the velocities generated in those times by the ordinates DB, EC. The spaces described with these velocities will be as the areas ABD, ACE, described by those ordinates, that is, at the very beginning of the motion (by Lem. IX), in the duplicate ratio of the times AD, AE.",
          "dipende_da": [
            "Lemma IX"
          ],
          "figura": {
            "mostra": [
              "asse dei tempi AD, AE",
              "ordinate delle velocità DB, EC",
              "curva delle velocità",
              "aree ABD, ACE"
            ],
            "evidenzia": [
              "spazio = area",
              "ABD : ACE → (AD : AE)²"
            ]
          },
          "nota": "Una sola frase latina; Motte la divide in due."
        }
      ]
    },
    {
      "id": "L1-Lem11",
      "tipo": "Lemma",
      "titolo": "Lemma XI — sottesa dell’angolo di contatto",
      "copertura": [
        "S1.35",
        "S1.36",
        "S1.37",
        "S1.38"
      ],
      "fonti": {
        "la": "",
        "en": "Motte 1846, pp. 100–101"
      },
      "enunciato": {
        "la": "",
        "it": "La sottesa evanescente dell’angolo di contatto, in tutte le curve che nel punto di contatto hanno curvatura finita, è alla fine in rapporto duplicato della sottesa dell’arco contermine.",
        "en": "The evanescent subtense of the angle of contact, in all curves which at the point of contact have a finite curvature, is ultimately in the duplicate ratio of the subtense of the conterminate arc."
      },
      "nota": "Nei passi di Motte [SVG 4] = AB² = AG × BD, [SVG 5] = Ab² = Ag × bd, [SVG 6] = AB², [SVG 7] = Ab².",
      "figura_base": {
        "punti": [
          "A",
          "B",
          "D",
          "G",
          "b",
          "d",
          "g",
          "J"
        ],
        "vincoli": [
          "AD tangente in A",
          "BD sottesa dell’angolo di contatto (Caso 1: BD ⊥ AD; Caso 2: angolo dato; Caso 3: BD diretta verso un punto dato)",
          "AB sottesa dell’arco (corda)",
          "AG ⊥ AD, BG ⊥ AB, G loro intersezione (accoppiamento richiesto dalla geometria: apparato A.11)",
          "b, d, g posizioni corrispondenti per un secondo arco Ab",
          "J posizione limite di G quando B → A; AJ = diametro di curvatura"
        ]
      },
      "passi": [
        {
          "id": "L1-Lem11-p1",
          "la": "",
          "it": "Caso 1. Sia AB quell’arco, AD la sua tangente, BD la sottesa dell’angolo di contatto, perpendicolare alla tangente, AB la sottesa dell’arco.",
          "en": "Let AB be that arc, AD its tangent, BD the subtense of the angle of contact perpendicular on the tangent, AB the subtense of the arc.",
          "dipende_da": [],
          "figura": {
            "mostra": [
              "arco AB",
              "tangente AD",
              "BD ⊥ AD",
              "corda AB"
            ],
            "evidenzia": [
              "BD",
              "AB"
            ]
          }
        },
        {
          "id": "L1-Lem11-p2",
          "la": "",
          "it": "A questa sottesa AB e alla tangente AD si innalzino le perpendicolari AG, BG, che si incontrano in G; poi i punti D, B, G si avvicinino ai punti d, b, g, e sia J l’intersezione delle linee BG, AG che si ottiene alla fine, quando i punti D, B giungono fino ad A.",
          "en": "Draw BG perpendicular to the subtense AB, and AG to the tangent AD, meeting in G; then let the points D, B, and G, approach to the points d, b, and g, and suppose J to be the ultimate intersection of the lines BG, AG, when the points D, B, have come to A.",
          "dipende_da": [],
          "figura": {
            "mostra": [
              "AG ⊥ AD",
              "BG ⊥ AB",
              "G",
              "secondo arco Ab con d, b, g",
              "J"
            ],
            "evidenzia": [
              "G → J quando B → A"
            ]
          },
          "nota": "Il latino non accoppia le perpendicolari nell’ordine delle parole; Motte esplicita BG ⊥ AB, AG ⊥ AD."
        },
        {
          "id": "L1-Lem11-p3",
          "la": "",
          "it": "È manifesto che la distanza GJ può essere minore di qualunque distanza assegnata.",
          "en": "It is evident that the distance GJ may be less than any assignable.",
          "dipende_da": [],
          "figura": {
            "mostra": [
              "segmento GJ"
            ],
            "evidenzia": [
              "GJ → 0"
            ]
          }
        },
        {
          "id": "L1-Lem11-p4",
          "la": "",
          "it": "Ora (per la natura dei cerchi passanti per i punti A, B, G e A, b, g) AB² è uguale ad AG × BD, e Ab² è uguale ad Ag × bd; e perciò il rapporto di AB² ad Ab² è composto dei rapporti di AG ad Ag e di BD a bd.",
          "en": "But (from the nature of the circles passing through the points A, B, G, A, b, g,) [SVG 4], and [SVG 5]; and therefore the ratio of [SVG 6] to [SVG 7]is compounded of the ratios of AG to Ag, and of Bd to bd.",
          "dipende_da": [],
          "figura": {
            "mostra": [
              "cerchio per A, B, G (diametro AG)",
              "cerchio per A, b, g"
            ],
            "evidenzia": [
              "AB² = AG × BD",
              "Ab² = Ag × bd"
            ]
          },
          "nota": "Motte scrive «Bd» per BD. Verifica numerica dell’identità in nota N8."
        },
        {
          "id": "L1-Lem11-p5",
          "la": "",
          "it": "Ma poiché GJ si può prendere minore di qualunque lunghezza assegnata, può accadere che il rapporto di AG ad Ag differisca dal rapporto di uguaglianza meno di qualunque differenza assegnata, e quindi che il rapporto di AB² ad Ab² differisca dal rapporto di BD a bd meno di qualunque differenza assegnata.",
          "en": "But because GJ may be assumed of less length than any assignable, the ratio of AG to Ag may be such as to differ from the ratio of equality by less than any assignable difference; and therefore the ratio of [SVG 6] to [SVG 7] may be such as to differ from the ratio of BD to bd by less than any assignable difference.",
          "dipende_da": [],
          "figura": {
            "mostra": [
              "rapporto AG : Ag",
              "rapporto AB² : Ab²",
              "rapporto BD : bd"
            ],
            "evidenzia": [
              "AG : Ag → 1"
            ]
          }
        },
        {
          "id": "L1-Lem11-p6",
          "la": "",
          "it": "Dunque, per il Lemma I, il rapporto ultimo di AB² ad Ab² è lo stesso del rapporto ultimo di BD a bd.",
          "en": "Therefore, by Lem. I, the ultimate ratio of [SVG 6] to [SVG 7] is the same with the ultimate ratio of BD to bd.",
          "dipende_da": [
            "Lemma I"
          ],
          "figura": {
            "mostra": [
              "confronto dei due rapporti"
            ],
            "evidenzia": [
              "BD : bd = AB² : Ab² alla fine"
            ]
          }
        },
        {
          "id": "L1-Lem11-p7",
          "la": "",
          "it": "Caso 2. Si inclini ora BD su AD in un angolo dato qualsiasi: il rapporto ultimo di BD a bd sarà sempre lo stesso di prima, e quindi lo stesso di AB² ad Ab².",
          "en": "Now let BD be inclined to AD in any given angle, and the ultimate ratio of BD to bd will always be the same as before, and therefore the same with the ratio of [SVG 6] to [SVG 7].",
          "dipende_da": [],
          "figura": {
            "mostra": [
              "BD inclinata di un angolo dato su AD"
            ],
            "evidenzia": [
              "BD : bd invariato"
            ]
          }
        },
        {
          "id": "L1-Lem11-p8",
          "la": "",
          "it": "Caso 3. E anche se l’angolo D non è dato, ma la retta BD converge verso un punto dato, o è determinata secondo qualunque altra legge, tuttavia gli angoli D, d, determinati secondo una legge comune, tenderanno sempre all’uguaglianza e si avvicineranno l’uno all’altro più di qualunque differenza assegnata, e perciò alla fine saranno uguali, per il Lemma I; e quindi le linee BD, bd stanno fra loro nello stesso rapporto di prima.",
          "en": "And if we suppose the angle D not to be given, but that the right line BD converges to a given point, or is determined by any other condition whatever; nevertheless the angles D, d, being determined by the same law, will always draw nearer to equality, and approach nearer to each other than by any assigned difference, and therefore, by Lem. I, will at last be equal; and therefore the lines BD, bd are in the same ratio to each other as before.",
          "dipende_da": [
            "Lemma I"
          ],
          "figura": {
            "mostra": [
              "punto dato verso cui converge BD",
              "angoli D, d"
            ],
            "evidenzia": [
              "angolo D → angolo d"
            ]
          },
          "nota": "«constitui»: refuso probabile della trascrizione per «constituti»."
        }
      ]
    },
    {
      "id": "L1-Lem11-Cor4",
      "tipo": "Corollarium",
      "titolo": "Lemma XI, Cor. 4 — triangoli in rapporto triplicato e sesquiplicato",
      "copertura": [
        "S1.42"
      ],
      "fonti": {
        "la": "",
        "en": "Motte 1846, p. 101"
      },
      "enunciato": {
        "la": "",
        "it": "I triangoli rettilinei ADB, Adb stanno alla fine in rapporto triplicato dei lati AD, Ad, e in rapporto sesquiplicato dei lati DB, db.",
        "en": "The rectilinear triangles ADB, Adb are ultimately in the triplicate ratio of the sides AD, Ad, and in a sesquiplicate ratio of the sides DB, db"
      },
      "figura_base": {
        "punti": [
          "A",
          "B",
          "C",
          "D",
          "b",
          "c",
          "d"
        ],
        "vincoli": [
          "come nel Lemma XI",
          "DB, db ∝ AD², Ad² alla fine",
          "BC, bc seni degli archi: C, c non definiti nel testo (probabilmente piedi delle perpendicolari da B, b sulla normale AG)"
        ]
      },
      "passi": [
        {
          "id": "L1-Lem11-Cor4-p1",
          "la": "",
          "it": "I triangoli rettilinei ADB, Adb stanno alla fine in rapporto triplicato dei lati AD, Ad, e in rapporto sesquiplicato dei lati DB, db, poiché stanno nel rapporto composto dei lati AD e DB, Ad e db.",
          "en": "The rectilinear triangles ADB, Adb are ultimately in the triplicate ratio of the sides AD, Ad, and in a sesquiplicate ratio of the sides DB, db; as being in the ratio compounded of the sides AD to DB, and of Ad to db.",
          "dipende_da": [],
          "figura": {
            "mostra": [
              "triangoli ADB, Adb"
            ],
            "evidenzia": [
              "ADB : Adb → (AD : Ad)³ = (DB : db)³/²"
            ]
          },
          "nota": "Motte accoppia male i lati: il rapporto composto è AD : Ad con DB : db (apparato A.11)."
        },
        {
          "id": "L1-Lem11-Cor4-p2",
          "la": "",
          "it": "Così anche i triangoli ABC, Abc stanno alla fine in rapporto triplicato dei lati BC, bc.",
          "en": "So also the triangles ABC, Abc are ultimately in the triplicate ratio of the sides BC, bc.",
          "dipende_da": [],
          "figura": {
            "mostra": [
              "triangoli ABC, Abc",
              "seni BC, bc"
            ],
            "evidenzia": [
              "ABC : Abc → (BC : bc)³"
            ]
          }
        },
        {
          "id": "L1-Lem11-Cor4-p3",
          "la": "",
          "it": "Chiamo poi rapporto sesquiplicato il subduplicato del triplicato, quello cioè che è composto del semplice e del subduplicato.",
          "en": "What I call the sesquiplicate ratio is the subduplicate of the triplicate, as being compounded of the simple and subduplicate ratio.",
          "dipende_da": [],
          "figura": {
            "mostra": [],
            "evidenzia": [
              "sesquiplicato = esponente 3/2"
            ]
          },
          "nota": "Definizione terminologica, senza figura."
        }
      ]
    }
  ]
}
```
