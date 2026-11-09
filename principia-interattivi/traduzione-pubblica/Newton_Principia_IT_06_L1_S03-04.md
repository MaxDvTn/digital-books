> **Copia pubblica.** In questa versione i campi `"la"` della Parte B sono vuoti: le frasi latine vengono dalla trascrizione del Newton Project, che non si ridistribuisce. Il latino del 1726 si legge su newtonproject.ox.ac.uk.

# Isaac Newton
# Principi matematici della filosofia naturale

## Fascicolo 6 — Libro I, Sezioni III e IV

**Il moto dei corpi nelle sezioni coniche eccentriche (Propp. XI–XVII, Lemmi XIII–XIV) e la determinazione delle orbite dato il fuoco (Lemmi XV–XVI, Propp. XVIII–XXI). Nuova traduzione italiana di lavoro dal latino del 1726, confrontata con l’inglese di Andrew Motte nell’edizione del 1846.**

Versione 0.1 — 8 novembre 2026. Preparata con Claude (Anthropic) per Massimo Bosetti.

### Stato e perimetro

Questo fascicolo traduce integralmente le Sezioni III e IV del Libro I (*De motu corporum*):

- **Sezione III**, *De motu corporum in conicis sectionibus excentricis*: Propp. XI–XVII con tutti i corollari, Lemmi XIII–XIV e lo Scolio finale (1726, pp. 54–65);
- **Sezione IV**, *De inventione orbium ellipticorum, parabolicorum & hyperbolicorum ex umbilico dato*: Lemma XV, Propp. XVIII–XX, Lemma XVI, Prop. XXI e lo Scolio finale (1726, pp. 66–73).

È una traduzione di lavoro, non un’edizione critica validata. Gli identificatori **S3.01–S3.50** e **S4.01–S4.29** e i titoli tematici tra parentesi sono aggiunte editoriali; i numeri romani di lemmi, proposizioni e corollari appartengono al testo originale. Le note dopo la traduzione non fanno parte del testo di Newton.

In coda al fascicolo c’è la **Parte B**, con i dati strutturati per le pagine interattive di 15 unità che hanno figura e dimostrazione o costruzione geometrica.

### Fonti effettivamente consultate

1. **Latino di riferimento.** Isaac Newton, *Philosophiæ Naturalis Principia Mathematica*, terza edizione, Londra, 1726, Libro I, Sezione III (pp. 54–65) e Sezione IV (pp. 66–73), secondo i marcatori di pagina della trascrizione. Trascrizione normalizzata del Newton Project, documento **NATP00087**, nei file di lavoro `latino-1726-L1-S03.md` e `latino-1726-L1-S04.md`. Le figure NATP00087-20…37 non erano disponibili: le relazioni geometriche sono ricostruite soltanto dalle lettere citate nel testo.
2. **Inglese di confronto.** *Newton’s Principia*, traduzione di Andrew Motte, New York, Daniel Adee, 1846, Sezione III (pp. 116–125) e Sezione IV (pp. 125–131) secondo i marcatori di pagina dell’EPUB Project Gutenberg n. 76404, nei file di lavoro `motte-1846-L1-S03.md` e `motte-1846-L1-S04.md`. Le formule stampate come immagini (SVG 37, 41, 63, 67–70, 84–107) sono state rese con `rsvg-convert` e lette una per una.
3. **Fascicolo 3** del progetto (*Leggi del moto*), per formato, tono e glossario, e in particolare per l’annotazione F3 sulla Prop. XI (PE³/SP²), che qui si riprende senza ripeterne i controlli sulla stampa.

Non ho consultato né riprodotto traduzioni moderne. Non ho potuto consultare la stampa del 1726 né Motte 1729 per questo fascicolo: i refusi segnalati restano «da verificare sulla stampa».

### Criteri di traduzione

- Il testo guida è il latino; l’inglese serve a controllare le interpretazioni ed è annotato quando aggiunge, omette o sbaglia.
- Si applica il **glossario comune** del brief (Fascicoli 1–3 e termini tecnici del Libro I): *latus rectum* «lato retto», *umbilicus* «fuoco», *vertex principalis* «vertice principale», *axis principalis / transversus* «asse principale / trasverso», *diametri conjugatæ* «diametri coniugati», *ordinatim applicata* «ordinata», *trajectoria* «traiettoria», *orbis, orbita* «orbita», *positione / specie datus* «dato di posizione / di forma», *tempus periodicum* «tempo periodico», *ratio duplicata / subduplicata / sesquiplicata* «rapporto duplicato / subduplicato / sesquiplicato», *reciproce* «inversamente», *directe* «direttamente», *ducere in* «moltiplicare per», *conjunctim* «considerate congiuntamente», *ultimo* «alla fine», *impulsus* «impulso» per l’azione istantanea (Prop. XVII, Cor. 3), Q.E.I. «C.V.T.», Q.E.F. «C.V.F.», Q.E.D. «C.V.D.».
- Estensioni proprie di questo fascicolo: § A.0.
- Gli enunciati in accusativo e infinito sono resi con l’indicativo; i problemi con l’infinito («descrivere…») restano all’infinito, come nel latino.
- Le abbreviazioni algebriche della stampa (*SPq*, *QT quad.*, *PE cub.*, *2KPH*) sono scritte SP², QT², PE³, 2KP×PH; le frazioni, appiattite nella trascrizione (*SPqQR*, *QTqQR*), sono scritte con la barra (SP²/QR, QT²/QR). La lettura di ogni formula è dichiarata nell’apparato o nella `nota` della Parte B. Nella Prop. XVII la catena di uguaglianze è di Newton e resta nel testo; il vincolo sopra *SP+PH* è reso con le parentesi.
- *Punctis Q & P coeuntibus* è reso «quando i punti Q e P vengono a coincidere».
- Le lettere delle figure restano come nel latino, minuscole comprese (p, q, r, s, h, v, k).

---

## Traduzione italiana

### Sezione III. Il moto dei corpi nelle sezioni coniche eccentriche

### Proposizione XI. Problema VI (forza verso il fuoco dell’ellisse)

**[S3.01]** **Un corpo ruoti in un’ellisse: si cerca la legge della forza centripeta diretta verso il fuoco dell’ellisse.**

**[S3.02]** Sia S il fuoco dell’ellisse. Si conduca SP, che tagli sia il diametro DK dell’ellisse in E sia l’ordinata Qv in x, e si completi il parallelogramma QxPR. È evidente che EP è uguale al semiasse maggiore AC: infatti, condotta dall’altro fuoco H dell’ellisse la linea HI parallela a EC, poiché CS e CH sono uguali, sono uguali ES ed EI, così che EP è la semisomma di PS e PI, cioè (per le parallele HI, PR e gli angoli uguali IPR, HPZ) di PS e PH, che considerate congiuntamente uguagliano l’asse intero 2AC.

**[S3.03]** Si abbassi su SP la perpendicolare QT e, detto L il lato retto principale dell’ellisse (ossia 2BC²/AC), L×QR starà a L×Pv come QR sta a Pv, cioè come PE, ossia AC, sta a PC; e L×Pv starà a GvP come L sta a Gv; e GvP starà a Qv² come PC² sta a CD²; e (per il Cor. 2 del Lemma VII), quando i punti Q e P vengono a coincidere, il rapporto di Qv² a Qx² è il rapporto di uguaglianza; e Qx², ossia Qv², sta a QT² come EP² sta a PF², cioè come CA² sta a PF², ovvero (per il Lemma XII) come CD² sta a CB². E, composti tutti questi rapporti, L×QR sta a QT² come AC×L×PC²×CD², ossia 2CB²×PC²×CD², sta a PC×Gv×CD²×CB², ovvero come 2PC sta a Gv.

**[S3.04]** Ma, quando i punti Q e P vengono a coincidere, 2PC e Gv sono uguali. Dunque sono uguali anche L×QR e QT², che sono a essi proporzionali. Si moltiplichino questi uguali per SP²/QR, e L×SP² risulterà uguale a SP²×QT²/QR. Dunque (per i Cor. 1 e 5 della Prop. VI) la forza centripeta è inversamente come L×SP², cioè inversamente in rapporto duplicato della distanza SP. C.V.T.

**[S3.05]** *Lo stesso, altrimenti.* Poiché la forza diretta verso il centro dell’ellisse, per effetto della quale il corpo P può ruotare in quell’ellisse, è (per il Cor. 1 della Prop. X) come la distanza CP del corpo dal centro C dell’ellisse, si conduca CE parallela alla tangente PR dell’ellisse; e la forza per effetto della quale lo stesso corpo P può ruotare intorno a un qualsiasi altro punto S dell’ellisse, se CE e PS concorrono in E, sarà come PE³/SP² (per il Cor. 3 della Prop. VII); cioè, se il punto S è il fuoco dell’ellisse, e quindi PE è dato, come SP² inversamente. C.V.T.

**[S3.06]** Con la stessa brevità con cui abbiamo esteso il quinto problema alla parabola e all’iperbole, si potrebbe fare qui lo stesso; ma, per l’importanza del problema e per l’uso che se ne farà in seguito, non sarà gravoso confermare con una dimostrazione gli altri casi.

### Proposizione XII. Problema VII (forza verso il fuoco dell’iperbole)

**[S3.07]** **Un corpo si muova in un’iperbole: si cerca la legge della forza centripeta diretta verso il fuoco della figura.**

**[S3.08]** Siano CA, CB i semiassi dell’iperbole; PG, KD altri diametri coniugati; PF la perpendicolare al diametro KD; e Qv l’ordinata al diametro GP. Si conduca SP, che tagli sia il diametro DK in E sia l’ordinata Qv in x, e si completi il parallelogramma QRPx. È evidente che EP è uguale al semiasse trasverso AC: infatti, condotta dall’altro fuoco H dell’iperbole la linea HI parallela a EC, poiché CS e CH sono uguali, sono uguali ES ed EI; così che EP è la semidifferenza di PS e PI, cioè (per le parallele IH, PR e gli angoli uguali IPR, HPZ) di PS e PH, la cui differenza uguaglia l’asse intero 2AC.

**[S3.09]** Si abbassi su SP la perpendicolare QT. E, detto L il lato retto principale dell’iperbole (ossia 2BC²/AC), L×QR starà a L×Pv come QR sta a Pv, ossia come Px sta a Pv, cioè (per i triangoli simili Pxv, PEC) come PE sta a PC, ossia come AC sta a PC. Inoltre L×Pv starà a Gv×Pv come L sta a Gv; e (per la natura delle coniche) il rettangolo GvP starà a Qv² come PC² sta a CD²; e (per il Cor. 2 del Lemma VII), quando i punti Q e P vengono a coincidere, il rapporto di Qv² a Qx² diventa il rapporto di uguaglianza; e Qx², ossia Qv², sta a QT² come EP² sta a PF², cioè come CA² sta a PF², ovvero (per il Lemma XII) come CD² sta a CB²; e, composti tutti questi rapporti, L×QR sta a QT² come AC×L×PC²×CD², ossia 2CB²×PC²×CD², sta a PC×Gv×CD²×CB², ovvero come 2PC sta a Gv.

**[S3.10]** Ma, quando i punti P e Q vengono a coincidere, 2PC e Gv sono uguali. Dunque sono uguali anche L×QR e QT², che sono a essi proporzionali. Si moltiplichino questi uguali per SP²/QR, e L×SP² risulterà uguale a SP²×QT²/QR. Dunque (per i Cor. 1 e 5 della Prop. VI) la forza centripeta è inversamente come L×SP², cioè inversamente in rapporto duplicato della distanza SP. C.V.T.

**[S3.11]** *Lo stesso, altrimenti.* Si trovi la forza che tende dal centro C dell’iperbole. Questa risulterà proporzionale alla distanza CP. Di qui poi (per il Cor. 3 della Prop. VII) la forza diretta verso il fuoco S sarà come PE³/SP², cioè, poiché PE è dato, inversamente come SP². C.V.T.

**[S3.12]** Nello stesso modo si dimostra che il corpo, mutata questa forza centripeta in centrifuga, si muoverà nell’iperbole opposta.

### Lemma XIII (lato retto della parabola)

**[S3.13]** **Il lato retto di una parabola relativo a un vertice qualsiasi è il quadruplo della distanza di quel vertice dal fuoco della figura.** Risulta dalle *Coniche*.

### Lemma XIV (perpendicolare dal fuoco sulla tangente della parabola)

**[S3.14]** **La perpendicolare abbassata dal fuoco di una parabola sulla sua tangente è media proporzionale fra le distanze del fuoco dal punto di contatto e dal vertice principale della figura.**

**[S3.15]** Sia infatti AP la parabola, S il suo fuoco, A il vertice principale, P il punto di contatto, PO l’ordinata al diametro principale, PM la tangente, che incontra il diametro principale in M, e SN la linea perpendicolare dal fuoco sulla tangente. Si congiunga AN; e, poiché sono uguali MS e SP, MN e NP, MA e AO, le rette AN e OP saranno parallele; e di qui il triangolo SAN sarà rettangolo in A e simile ai triangoli uguali SNM, SNP: dunque PS sta a SN come SN sta a SA. C.V.D.

**[S3.16]** Cor. 1. PS² sta a SN² come PS sta a SA.

**[S3.17]** Cor. 2. E, poiché SA è data, SN² è come PS.

**[S3.18]** Cor. 3. E il punto d’incontro di una tangente qualsiasi PM con la retta SN, condotta dal fuoco perpendicolarmente a essa, cade sulla retta AN, che tocca la parabola nel vertice principale.

### Proposizione XIII. Problema VIII (forza verso il fuoco della parabola)

**[S3.19]** **Un corpo si muova sul perimetro di una parabola: si cerca la legge della forza centripeta diretta verso il fuoco di questa figura.**

**[S3.20]** Resti la costruzione del lemma, e sia P il corpo sul perimetro della parabola; e dal luogo Q, nel quale il corpo si porta subito dopo, conduci QR parallela a SP e QT perpendicolare a SP, e inoltre Qv parallela alla tangente, che incontri sia il diametro PG in v sia la distanza SP in x. Ora, per i triangoli simili Pxv, SPM e per l’uguaglianza dei lati SM, SP dell’uno, sono uguali i lati Px, ossia QR, e Pv dell’altro. Ma, per le coniche, il quadrato dell’ordinata Qv è uguale al rettangolo formato dal lato retto e dal segmento di diametro Pv, cioè (per il Lemma XIII) al rettangolo 4PS×Pv, ossia 4PS×QR; e, quando i punti P e Q vengono a coincidere, il rapporto di Qv a Qx (per il Cor. 2 del Lemma VII) diventa il rapporto di uguaglianza. Dunque Qx², in quel caso, è uguale al rettangolo 4PS×QR.

**[S3.21]** Inoltre (per i triangoli simili QxT, SPN) Qx² sta a QT² come PS² sta a SN², cioè (per il Cor. 1 del Lemma XIV) come PS sta a SA, cioè come 4PS×QR sta a 4SA×QR; e di qui (per la Prop. IX del Libro V degli *Elementi*) QT² e 4SA×QR sono uguali. Si moltiplichino questi uguali per SP²/QR, e SP²×QT²/QR risulterà uguale a SP²×4SA; e perciò (per i Cor. 1 e 5 della Prop. VI) la forza centripeta è inversamente come SP²×4SA, cioè, poiché 4SA è dato, inversamente in rapporto duplicato della distanza SP. C.V.T.

**[S3.22]** Cor. 1. Dalle tre ultime proposizioni segue che, se un corpo qualsiasi P parte dal luogo P lungo una retta qualsiasi PR con una velocità qualsiasi, ed è insieme sottoposto all’azione di una forza centripeta inversamente proporzionale al quadrato della distanza dei luoghi dal centro, questo corpo si muoverà in una delle sezioni coniche che ha il fuoco nel centro delle forze; e viceversa. Dati infatti il fuoco, il punto di contatto e la posizione della tangente, si può descrivere una sezione conica che in quel punto abbia una curvatura data. Ora, la curvatura è data, se sono date la forza centripeta e la velocità del corpo; e due orbite che si toccano a vicenda non possono essere descritte con la stessa forza centripeta e la stessa velocità.

**[S3.23]** Cor. 2. Se la velocità con cui il corpo parte dal suo luogo P è tale che con essa la lineetta PR possa essere descritta in una qualche minima particella di tempo, e la forza centripeta è capace di muovere lo stesso corpo nello stesso tempo per lo spazio QR, questo corpo si muoverà in una qualche sezione conica il cui lato retto principale è quella quantità QT²/QR che si ha alla fine, quando le lineette PR, QR diminuiscono all’infinito. In questi corollari riconduco il cerchio all’ellisse, ed escludo il caso in cui il corpo scende in linea retta verso il centro.

### Proposizione XIV. Teorema VI (lati retti e aree)

**[S3.24]** **Se più corpi ruotano intorno a un centro comune e la forza centripeta è inversamente in rapporto duplicato della distanza dei luoghi dal centro, dico che i lati retti principali delle orbite sono in rapporto duplicato delle aree che i corpi, con raggi condotti al centro, descrivono nello stesso tempo.**

**[S3.25]** Infatti (per il Cor. 2 della Prop. XIII) il lato retto L è uguale alla quantità QT²/QR che si ha alla fine, quando i punti P e Q vengono a coincidere. Ma la linea minima QR, in un tempo dato, è come la forza centripeta che la genera, cioè (per ipotesi) inversamente come SP². Dunque QT²/QR è come QT²×SP², cioè il lato retto L è in rapporto duplicato dell’area QT×SP. C.V.D.

**[S3.26]** Cor. Di qui l’area intera dell’ellisse, e il rettangolo formato dagli assi, che le è proporzionale, è in rapporto composto dal rapporto subduplicato del lato retto e dal rapporto del tempo periodico. L’area intera, infatti, è come l’area QT×SP descritta in un tempo dato, moltiplicata per il tempo periodico.

### Proposizione XV. Teorema VII (tempi periodici e assi maggiori)

**[S3.27]** **Poste le stesse cose, dico che i tempi periodici nelle ellissi sono in rapporto sesquiplicato degli assi maggiori.**

**[S3.28]** L’asse minore, infatti, è medio proporzionale fra l’asse maggiore e il lato retto; e perciò il rettangolo formato dagli assi è in rapporto composto dal rapporto subduplicato del lato retto e dal rapporto sesquiplicato dell’asse maggiore. Ma questo rettangolo (per il Corollario della Prop. XIV) è in rapporto composto dal rapporto subduplicato del lato retto e dal rapporto del tempo periodico. Si tolga da entrambe le parti il rapporto subduplicato del lato retto, e resterà il rapporto sesquiplicato dell’asse maggiore, identico al rapporto del tempo periodico. C.V.D.

**[S3.29]** Cor. I tempi periodici nelle ellissi sono dunque gli stessi che nei cerchi i cui diametri sono uguali agli assi maggiori delle ellissi.

### Proposizione XVI. Teorema VIII (velocità nelle sezioni coniche)

**[S3.30]** **Poste le stesse cose, condotte ai corpi le linee rette che in quei punti tocchino le orbite, e abbassate dal fuoco comune le perpendicolari su queste tangenti, dico che le velocità dei corpi sono in rapporto composto dal rapporto delle perpendicolari inversamente e dal rapporto subduplicato dei lati retti principali direttamente.**

**[S3.31]** Dal fuoco S abbassa sulla tangente PR la perpendicolare SY, e la velocità del corpo P sarà inversamente in rapporto subduplicato della quantità SY²/L. Quella velocità, infatti, è come l’arco piccolissimo PQ descritto in una particella di tempo data, cioè (per il Lemma VII) come la tangente PR, cioè, poiché PR sta a QT come SP sta a SY, come SP×QT/SY, ossia come SY inversamente e SP×QT direttamente; e SP×QT è come l’area descritta in un tempo dato, cioè (per la Prop. XIV) in rapporto subduplicato del lato retto. C.V.D.

**[S3.32]** Cor. 1. I lati retti principali sono in rapporto composto dal rapporto duplicato delle perpendicolari e dal rapporto duplicato delle velocità.

**[S3.33]** Cor. 2. Le velocità dei corpi, alle distanze massime e minime dal fuoco comune, sono in rapporto composto dal rapporto delle distanze inversamente e dal rapporto subduplicato dei lati retti principali direttamente. Le perpendicolari, infatti, sono ora le distanze stesse.

**[S3.34]** Cor. 3. E perciò la velocità in una sezione conica, alla distanza massima o minima dal fuoco, sta alla velocità in un cerchio alla stessa distanza dal centro in rapporto subduplicato del lato retto principale al doppio di quella distanza.

**[S3.35]** Cor. 4. Le velocità dei corpi che girano in ellissi, alle distanze medie dal fuoco comune, sono le stesse dei corpi che girano in cerchi alle stesse distanze; cioè (per il Cor. 6 della Prop. IV) sono inversamente in rapporto subduplicato delle distanze. Le perpendicolari, infatti, sono ora i semiassi minori, e questi sono come medi proporzionali fra le distanze e i lati retti. Si componga questo rapporto, inversamente, con il rapporto subduplicato dei lati retti, direttamente, e si avrà il rapporto subduplicato delle distanze, inversamente.

**[S3.36]** Cor. 5. Nella stessa figura, o anche in figure diverse i cui lati retti principali siano uguali, la velocità del corpo è inversamente come la perpendicolare abbassata dal fuoco sulla tangente.

**[S3.37]** Cor. 6. Nella parabola la velocità è inversamente in rapporto subduplicato della distanza del corpo dal fuoco della figura; nell’ellisse varia di più, nell’iperbole di meno che in questo rapporto. Infatti (per il Cor. 2 del Lemma XIV) la perpendicolare abbassata dal fuoco sulla tangente della parabola è in rapporto subduplicato della distanza. Nell’iperbole la perpendicolare varia di meno, nell’ellisse di più.

**[S3.38]** Cor. 7. Nella parabola la velocità di un corpo a una distanza qualsiasi dal fuoco sta alla velocità di un corpo che ruota in un cerchio alla stessa distanza dal centro in rapporto subduplicato del numero due all’unità; nell’ellisse è minore, nell’iperbole maggiore che in questo rapporto. Infatti, per il secondo corollario di questa proposizione, la velocità nel vertice della parabola è in questo rapporto, e per i corollari sesti di questa proposizione e della Prop. IV si conserva la stessa proporzione a tutte le distanze. Di qui anche, nella parabola, la velocità è ovunque uguale alla velocità di un corpo che ruota in un cerchio a metà distanza; nell’ellisse è minore, nell’iperbole maggiore.

**[S3.39]** Cor. 8. La velocità di un corpo che gira in una sezione conica qualsiasi sta alla velocità di un corpo che gira in un cerchio alla distanza di metà del lato retto principale della sezione come quella distanza sta alla perpendicolare abbassata dal fuoco sulla tangente della sezione. Risulta dal quinto corollario.

**[S3.40]** Cor. 9. Poiché dunque (per il Cor. 6 della Prop. IV) la velocità di un corpo che gira in questo cerchio sta alla velocità di un corpo che gira in un altro cerchio qualsiasi inversamente in rapporto subduplicato delle distanze, risulterà per uguaglianza che la velocità di un corpo che gira in una sezione conica sta alla velocità di un corpo che gira in un cerchio alla stessa distanza come la media proporzionale fra quella distanza comune e la metà del lato retto principale della sezione sta alla perpendicolare abbassata dal fuoco comune sulla tangente della sezione.

### Proposizione XVII. Problema IX (l’orbita dalle condizioni iniziali)

**[S3.41]** **Posto che la forza centripeta sia inversamente proporzionale al quadrato della distanza dal centro, e che la quantità assoluta di quella forza sia nota, si cerca la linea che un corpo descrive partendo da un luogo dato con una velocità data lungo una retta data.**

**[S3.42]** La forza centripeta diretta verso il punto S sia quella per effetto della quale un corpo p gira in un’orbita data qualsiasi pq, e se ne conosca la velocità nel luogo p. Dal luogo P, lungo la linea PR, parta il corpo P con una velocità data, e subito dopo, costretto dalla forza centripeta, si pieghi da quella linea nella sezione conica PQ. La retta PR, dunque, toccherà questa sezione in P. Tocchi ugualmente una retta pr l’orbita pq in p; e, se si immagina di abbassare da S le perpendicolari su quelle tangenti, il lato retto principale della sezione conica starà al lato retto principale dell’orbita (per il Cor. 1 della Prop. XVI) in rapporto composto dal rapporto duplicato delle perpendicolari e dal rapporto duplicato delle velocità, e perciò è dato. Sia L il lato retto della sezione conica. È dato inoltre il fuoco S della stessa sezione conica. Si faccia l’angolo RPH uguale al complemento a due retti dell’angolo RPS; e sarà data di posizione la linea PH, sulla quale si trova l’altro fuoco H.

**[S3.43]** Abbassata su PH la perpendicolare SK, si immagini innalzato il semiasse coniugato BC; e sarà SP² − 2KP×PH + PH² = SH² = 4CH² = 4BH² − 4BC² = (SP + PH)² − L×(SP + PH) = SP² + 2SP×PH + PH² − L×(SP + PH). Si aggiunga da entrambe le parti 2KP×PH − SP² − PH² + L×(SP + PH), e si avrà L×(SP + PH) = 2SP×PH + 2KP×PH, ossia SP + PH sta a PH come 2SP + 2KP sta a L. Di qui PH è data tanto in lunghezza quanto in posizione.

**[S3.44]** Precisamente: se la velocità del corpo in P è tale che il lato retto L sia minore di 2SP + 2KP, PH giacerà dalla stessa parte della tangente PR rispetto alla linea PS; e perciò la figura sarà un’ellisse, e sarà data a partire dai fuochi dati S, H e dall’asse principale SP + PH. Se invece la velocità del corpo è tanto grande che il lato retto L sia uguale a 2SP + 2KP, la lunghezza PH sarà infinita; e perciò la figura sarà una parabola che ha l’asse SH parallelo alla linea PK, e di qui sarà data. Se poi il corpo parte dal suo luogo P con una velocità ancora maggiore, la lunghezza PH andrà presa dall’altra parte della tangente; e perciò, passando la tangente fra i fuochi, la figura sarà un’iperbole che ha l’asse principale uguale alla differenza delle linee SP e PH, e di qui sarà data.

**[S3.45]** Se infatti il corpo, in questi casi, ruota in una sezione conica così trovata, si è dimostrato nelle Propp. XI, XII e XIII che la forza centripeta sarà inversamente come il quadrato della distanza del corpo dal centro delle forze S; e perciò è rappresentata correttamente la linea PQ che il corpo, con una tale forza, descriverà partendo dal luogo dato P con la velocità data lungo la retta PR data di posizione. C.V.F.

**[S3.46]** Cor. 1. Di qui, in ogni sezione conica, dati il vertice principale D, il lato retto L e il fuoco S, è dato l’altro fuoco H, prendendo DH a DS come il lato retto sta alla differenza fra il lato retto e 4DS. La proporzione «SP + PH sta a PH come 2SP + 2KP sta a L» diventa infatti, nel caso di questo corollario, «DS + DH sta a DH come 4DS sta a L», e, separando, «DS sta a DH come 4DS − L sta a L».

**[S3.47]** Cor. 2. Perciò, se è data la velocità del corpo nel vertice principale D, l’orbita si troverà speditamente: prendendo cioè il suo lato retto, rispetto al doppio della distanza DS, in rapporto duplicato di questa velocità data alla velocità di un corpo che gira in un cerchio alla distanza DS (per il Cor. 3 della Prop. XVI); poi DH a DS come il lato retto sta alla differenza fra il lato retto e 4DS.

**[S3.48]** Cor. 3. Di qui anche, se un corpo si muove in una sezione conica qualsiasi ed è sbalzato fuori dalla sua orbita da un impulso qualsiasi, si può conoscere l’orbita nella quale proseguirà poi il suo corso. Componendo infatti il moto proprio del corpo con il moto che l’impulso da solo genererebbe, si avrà il moto con cui il corpo partirà dal luogo dato dell’impulso lungo una retta data di posizione.

**[S3.49]** Cor. 4. E se quel corpo è perturbato continuamente da una forza impressa dall’esterno, se ne conoscerà il corso con ottima approssimazione, raccogliendo i cambiamenti che quella forza introduce in alcuni punti e stimando dall’analogia della serie i cambiamenti continui nei luoghi intermedi.

### Scolio (forza verso un punto qualsiasi)

**[S3.50]** Se un corpo P, per effetto di una forza centripeta diretta verso un punto dato qualsiasi R, si muove sul perimetro di una sezione conica data qualsiasi, il cui centro sia C, e si cerca la legge della forza centripeta: si conduca CG parallela al raggio RP, che incontri in G la tangente PG dell’orbita; e quella forza (per il Cor. 1 e lo Scolio della Prop. X e il Cor. 3 della Prop. VII) sarà come CG³/RP².

### Sezione IV. La determinazione delle orbite ellittiche, paraboliche e iperboliche dato il fuoco

### Lemma XV (perpendicolare che biseca SV)

**[S4.01]** **Se dai due fuochi S, H di un’ellisse o di un’iperbole qualsiasi si conducono a un terzo punto qualsiasi V due rette SV, HV, delle quali una, HV, sia uguale all’asse principale della figura, cioè all’asse sul quale giacciono i fuochi, e l’altra, SV, sia divisa a metà in T dalla perpendicolare TR abbassata su di essa, quella perpendicolare TR toccherà in qualche punto la sezione conica; e viceversa, se la tocca, HV sarà uguale all’asse principale della figura.**

**[S4.02]** Tagli infatti la perpendicolare TR la retta HV, prolungata se occorre, in R; e si congiunga SR. Poiché TS e TV sono uguali, saranno uguali anche le rette SR, VR e gli angoli TRS, TRV. Perciò il punto R sarà sulla sezione conica e la perpendicolare TR la toccherà; e viceversa. C.V.D.

### Proposizione XVIII. Problema X (ellissi e iperboli dati il fuoco e l’asse)

**[S4.03]** **Dati il fuoco e gli assi principali, descrivere traiettorie ellittiche e iperboliche che passino per punti dati e tocchino rette date di posizione.**

**[S4.04]** Sia S il fuoco comune delle figure; AB la lunghezza dell’asse principale di una traiettoria qualsiasi; P un punto per il quale la traiettoria deve passare; e TR una retta che essa deve toccare. Con centro P e raggio AB − SP, se l’orbita è un’ellisse, oppure AB + SP, se è un’iperbole, si descriva il cerchio HG. Sulla tangente TR si abbassi la perpendicolare ST, e la si prolunghi fino a V, in modo che TV sia uguale a ST; e con centro V e raggio AB si descriva il cerchio FH. Con questo metodo, siano dati due punti P, p, o due tangenti TR, tr, o un punto P e una tangente TR, si devono descrivere due cerchi. Sia H la loro intersezione comune, e con i fuochi S, H e con l’asse dato si descriva la traiettoria. Dico che è fatto.

**[S4.05]** La traiettoria descritta, infatti (poiché PH + SP nell’ellisse e PH − SP nell’iperbole è uguale all’asse), passerà per il punto P e (per il lemma precedente) toccherà la retta TR. E con lo stesso argomento o passerà per i due punti P, p, o toccherà le due rette TR, tr. C.V.F.

### Proposizione XIX. Problema XI (parabola dato il fuoco)

**[S4.06]** **Intorno a un fuoco dato descrivere una traiettoria parabolica che passi per punti dati e tocchi rette date di posizione.**

**[S4.07]** Sia S il fuoco, P un punto e TR una tangente della traiettoria da descrivere. Con centro P e raggio PS descrivi il cerchio FG. Dal fuoco abbassa sulla tangente la perpendicolare ST, e prolungala fino a V, in modo che TV sia uguale a ST. Allo stesso modo si deve descrivere un secondo cerchio fg, se è dato un secondo punto p; oppure si deve trovare un secondo punto v, se è data una seconda tangente tr; poi si deve condurre la retta IF, che tocchi i due cerchi FG, fg, se sono dati due punti P, p, oppure passi per i due punti V, v, se sono date due tangenti TR, tr, oppure tocchi il cerchio FG e passi per il punto V, se sono dati il punto P e la tangente TR. Su FI abbassa la perpendicolare SI e dividila a metà in K; e con asse SK e vertice principale K si descriva una parabola. Dico che è fatto.

**[S4.08]** La parabola, infatti, poiché sono uguali SK e IK, SP e FP, passerà per il punto P; e (per il Cor. 3 del Lemma XIV), poiché sono uguali ST e TV e l’angolo STR è retto, toccherà la retta TR. C.V.F.

### Proposizione XX. Problema XII (traiettoria data di forma)

**[S4.09]** **Intorno a un fuoco dato descrivere una traiettoria qualsiasi data di forma, che passi per punti dati e tocchi rette date di posizione.**

**[S4.10]** Caso 1. Dato il fuoco S, si debba descrivere la traiettoria ABC per due punti B, C. Poiché la traiettoria è data di forma, sarà dato il rapporto dell’asse principale alla distanza dei fuochi. In quel rapporto prendi KB a BS e LC a CS. Con centri B, C e raggi BK, CL descrivi due cerchi; sulla retta KL, che li tocchi in K e L, abbassa la perpendicolare SG, e tagliala in A e a, in modo che GA stia ad AS e Ga ad aS come KB sta a BS; e con asse Aa e vertici A, a si descriva la traiettoria. Dico che è fatto.

**[S4.11]** Sia infatti H l’altro fuoco della figura descritta; e, poiché GA sta ad AS come Ga sta ad aS, separando, Ga − GA, ossia Aa, starà ad aS − AS, ossia SH, nello stesso rapporto, e quindi nel rapporto che l’asse principale della figura da descrivere ha alla distanza dei suoi fuochi; e perciò la figura descritta è della stessa forma di quella da descrivere. E, poiché KB sta a BS e LC sta a CS nello stesso rapporto, questa figura passerà per i punti B, C, come è manifesto dalle coniche.

**[S4.12]** Caso 2. Dato il fuoco S, si debba descrivere una traiettoria che tocchi in qualche punto due rette TR, tr. Dal fuoco abbassa sulle tangenti le perpendicolari ST, St e prolungale fino a V, v, in modo che TV, tv siano uguali a TS, tS. Dividi a metà Vv in O, e innalza la perpendicolare illimitata OH, e taglia la retta VS, prolungata all’infinito, in K e k, in modo che VK stia a KS e Vk a kS come l’asse principale della traiettoria da descrivere sta alla distanza dei fuochi. Sul diametro Kk si descriva un cerchio che tagli OH in H; e con i fuochi S, H e con asse principale uguale a VH si descriva la traiettoria. Dico che è fatto.

**[S4.13]** Dividi infatti a metà Kk in X, e congiungi HX, HS, HV, Hv. Poiché VK sta a KS come Vk sta a kS, e, componendo, come VK + Vk sta a KS + kS, e, separando, come Vk − VK sta a kS − KS, cioè come 2VX sta a 2KX e 2KX sta a 2SX, e quindi come VX sta a HX e HX sta a SX, saranno simili i triangoli VXH, HXS; e perciò VH starà a SH come VX sta a XH, e quindi come VK sta a KS. L’asse principale VH della traiettoria descritta ha dunque alla distanza dei suoi fuochi SH lo stesso rapporto che l’asse principale della traiettoria da descrivere ha alla distanza dei suoi fuochi; e perciò è della stessa forma. Inoltre, poiché VH e vH sono uguali all’asse principale, e VS, vS sono divisi a metà perpendicolarmente dalle rette TR, tr, è chiaro (per il Lemma XV) che quelle rette toccano la traiettoria descritta. C.V.F.

**[S4.14]** Caso 3. Dato il fuoco S, si debba descrivere una traiettoria che tocchi la retta TR nel punto dato R. Sulla retta TR abbassa la perpendicolare ST, e prolungala fino a V, in modo che TV sia uguale a ST. Congiungi VR, e taglia la retta VS, prolungata all’infinito, in K e k, in modo che VK stia a SK e Vk a Sk come l’asse principale dell’ellisse da descrivere sta alla distanza dei fuochi; e, descritto un cerchio sul diametro Kk, si tagli in H la retta VR prolungata; e con i fuochi S, H e con asse principale uguale alla retta VH si descriva la traiettoria. Dico che è fatto.

**[S4.15]** Che VH stia a SH come VK sta a SK, e quindi come l’asse principale della traiettoria da descrivere sta alla distanza dei suoi fuochi, risulta infatti da quanto si è dimostrato nel secondo caso; e perciò la traiettoria descritta è della stessa forma di quella da descrivere; e che la retta TR, dalla quale è diviso a metà l’angolo VRS, tocchi la traiettoria nel punto R, risulta dalle coniche. C.V.F.

**[S4.16]** Caso 4. Intorno al fuoco S si debba ora descrivere una traiettoria APB che tocchi la retta TR e passi per un punto qualsiasi P dato fuori della tangente, e che sia simile alla figura apb descritta con asse principale ab e fuochi s, h. Sulla tangente TR abbassa la perpendicolare ST, e prolungala fino a V, in modo che TV sia uguale a ST. Agli angoli VSP, SVP fa’ uguali gli angoli hsq, shq; e con centro q e con un raggio che stia ad ab come SP sta a VS descrivi un cerchio che tagli la figura apb in p. Congiungi sp e conduci SH che stia a sh come SP sta a sp, e che formi l’angolo PSH uguale all’angolo psh e l’angolo VSH uguale all’angolo psq. Infine, con i fuochi S, H e con asse principale AB uguale alla distanza VH, si descriva una sezione conica. Dico che è fatto.

**[S4.17]** Se infatti si conduce sv che stia a sp come sh sta a sq, e che formi l’angolo vsp uguale all’angolo hsq e l’angolo vsh uguale all’angolo psq, i triangoli svh, spq saranno simili, e perciò vh starà a pq come sh sta a sq, cioè (per i triangoli simili VSP, hsq) come VS sta a SP, ossia come ab sta a pq. Dunque vh e ab sono uguali. Inoltre, per i triangoli simili VSH, vsh, VH sta a SH come vh sta a sh, cioè l’asse della sezione conica ora descritta sta alla distanza dei suoi fuochi come l’asse ab sta alla distanza dei fuochi sh; e perciò la figura ora descritta è simile alla figura apb. Questa figura passa poi per il punto P, perché il triangolo PSH è simile al triangolo psh; e, poiché VH è uguale al suo asse e VS è diviso a metà perpendicolarmente dalla retta TR, essa tocca la retta TR. C.V.F.

### Lemma XVI (tre rette con differenze date)

**[S4.18]** **Da tre punti dati condurre a un quarto punto non dato tre rette le cui differenze siano date o nulle.**

**[S4.19]** Caso 1. Siano A, B, C i punti dati e Z il quarto punto, che si deve trovare; per la differenza data delle linee AZ, BZ, il punto Z si troverà su un’iperbole i cui fuochi sono A e B e il cui asse principale è quella differenza data. Sia MN quell’asse. Prendi PM a MA come MN sta ad AB e, innalzata PR perpendicolare ad AB e abbassata ZR perpendicolare a PR, per la natura di questa iperbole ZR starà ad AZ come MN sta ad AB. Con un ragionamento simile il punto Z si troverà su un’altra iperbole, i cui fuochi sono A, C e il cui asse principale è la differenza fra AZ e CZ; e si può condurre QS perpendicolare ad AC, sulla quale, se da un punto qualsiasi Z di questa iperbole si abbassa la normale ZS, questa starà ad AZ come la differenza fra AZ e CZ sta ad AC.

**[S4.20]** Sono dunque dati i rapporti di ZR e di ZS ad AZ, e perciò è dato il rapporto di ZR e ZS fra loro; e quindi, se le rette RP, SQ concorrono in T, e si conducono TZ e TA, la figura TRZS sarà data di forma, e la retta TZ, sulla quale si trova in qualche punto il punto Z, sarà data di posizione. Sarà data anche la retta TA, come pure l’angolo ATZ; e, poiché sono dati i rapporti di AZ e di TZ a ZS, sarà dato il loro rapporto fra loro; e di qui sarà dato il triangolo ATZ, il cui vertice è il punto Z. C.V.T.

**[S4.21]** Caso 2. Se due delle tre linee, per esempio AZ e BZ, sono uguali, conduci la retta TZ in modo che divida a metà la retta AB; poi cerca il triangolo ATZ come sopra.

**[S4.22]** Caso 3. Se tutte e tre sono uguali, il punto Z si troverà nel centro del cerchio che passa per i punti A, B, C. C.V.T.

**[S4.23]** Questo lemma problematico si risolve anche per mezzo del libro *Delle tangenze* di Apollonio, restituito da Viète.

### Proposizione XXI. Problema XIII (traiettoria per punti e tangenti dati)

**[S4.24]** **Descrivere intorno a un fuoco dato una traiettoria che passi per punti dati e tocchi rette date di posizione.**

**[S4.25]** Siano dati il fuoco S, il punto P e la tangente TR, e si debba trovare l’altro fuoco H. Sulla tangente abbassa la perpendicolare ST, e prolungala fino a Y, in modo che TY sia uguale a ST, e YH sarà uguale all’asse principale. Congiungi SP, HP, e SP sarà la differenza fra HP e l’asse principale. In questo modo, se sono date più tangenti TR o più punti P, si giungerà sempre ad altrettante linee YH o PH, condotte dai detti punti Y o P al fuoco H, che o sono uguali agli assi o differiscono da essi per le lunghezze date SP, e che perciò o sono uguali fra loro o hanno differenze date; e di qui, per il lemma precedente, è dato quell’altro fuoco H. Avuti poi i fuochi insieme con la lunghezza dell’asse (che è YH oppure, se la traiettoria è un’ellisse, PH + SP, se è un’iperbole, PH − SP), si ha la traiettoria. C.V.T.

### Scolio (l’iperbole opposta; il caso di tre punti)

**[S4.26]** Quando la traiettoria è un’iperbole, sotto il nome di questa traiettoria non comprendo l’iperbole opposta. Un corpo, infatti, proseguendo nel suo moto, non può passare nell’iperbole opposta.

**[S4.27]** Il caso in cui sono dati tre punti si risolve più speditamente così. Siano dati i punti B, C, D. Prolunga le congiungenti BC, CD fino a E, F, in modo che EB stia a EC come SB sta a SC, e FC stia a FD come SC sta a SD. Sulla EF, condotta e prolungata, abbassa le normali SG, BH, e sulla GS prolungata all’infinito prendi GA ad AS e Ga ad aS come HB sta a BS; e A sarà il vertice e Aa l’asse principale della traiettoria; la quale, secondo che GA sia maggiore, uguale o minore di AS, sarà un’ellisse, una parabola o un’iperbole: nel primo caso il punto a cade dalla stessa parte della linea GF del punto A; nel secondo se ne va all’infinito; nel terzo cade dalla parte opposta della linea GF.

**[S4.28]** Se infatti si abbassano su GF le perpendicolari CI, DK, IC starà a HB come EC sta a EB, cioè come SC sta a SB; e, permutando, IC starà a SC come HB sta a SB, ossia come GA sta a SA. E con un argomento simile si proverà che KD sta a SD nello stesso rapporto. I punti B, C, D giacciono dunque in una sezione conica descritta intorno al fuoco S in modo tale che tutte le rette condotte dal fuoco S ai singoli punti della sezione stiano alle perpendicolari abbassate dagli stessi punti sulla retta GF in quel rapporto dato.

**[S4.29]** Con un metodo non molto diverso dà la soluzione di questo problema l’illustre geometra de la Hire, nel libro VIII, Prop. XXV, delle sue *Coniche*.

**Fine della Sezione IV. Nel testo originale segue la Sezione V, *Inventio orbium ubi umbilicus neuter datur*.**

---

## Apparato

### A.0 Estensioni del glossario

| Latino | Italiano | Motivazione |
|---|---|---|
| *revolvi*, *gyrari* | «ruotare», «girare» | Due verbi distinti nel latino (Prop. XI *revolvatur*; Prop. XVI, Cor. 4–9 *gyrantium*), tenuti distinti. |
| *punctis Q & P coeuntibus* | «quando i punti Q e P vengono a coincidere» | Ablativo assoluto che esprime il passaggio al limite (Lemma VII); «coincidendo» sarebbe ambiguo. |
| *ratio æqualitatis* | «rapporto di uguaglianza» | Termine euclideo, conservato. |
| *lineola* | «lineetta» | Diminutivo tecnico (Prop. XIII, Cor. 2); distingue le quantità nascenti dalle linee finite. *Linea minima* (Prop. XIV) è reso «linea minima». |
| *quam minimus* | «piccolissimo» | Prop. XVI, *arcus quam minimus*. |
| *particula temporis* | «particella di tempo» | Coerente con *particula* = «particella». |
| *intervallum* (di un cerchio) | «raggio» | Nelle costruzioni *centro P intervallo PS* indica il raggio. |
| *inflectere* (rette a un punto) | «condurre» | Lemmi XV e XVI: condurre da due o tre punti rette che si incontrano in un punto; «piegare» sarebbe oscuro. |
| *divisim*, *composite*, *vicissim*, *ex æquo* | «separando», «componendo», «permutando», «per uguaglianza» | Nomi delle operazioni sulle proporzioni del libro V degli *Elementi*. |
| *ejusdem speciei* | «della stessa forma» | Coerente con *specie datus* «dato di forma». |
| *complementum ad duos rectos* | «complemento a due retti» | Calco del latino (= supplemento), spiegato in nota. |
| *hyperbola opposita* | «iperbole opposta» | L’altro ramo della stessa iperbole; da non confondere con l’iperbole coniugata (vedi A.4). |
| *quantitas absoluta vis* | «quantità assoluta della forza» | Rinvia alla Def. VI (forza assoluta). |
| *Dico factum* | «Dico che è fatto» | Formula di chiusura delle costruzioni, prima della dimostrazione. |
| *ex conicis*, *ex natura conicorum* | «per le coniche», «dalle coniche», «per la natura delle coniche» | Rinvio ai trattati sulle coniche (Apollonio); *Patet ex Conicis* «Risulta dalle *Coniche*». |
| *normalis* | «normale» | Il latino usa *normalis* accanto a *perpendicularis* (Lemma XVI, Scolio IV); si conserva la variazione. |
| *quam proxime* | «con ottima approssimazione» | Come nel Fascicolo 3. |

*Sagitta*, *sinus versus* e *in consequentia* non compaiono in queste sezioni.

### A.1 Proposizione XI

**Latino:** *Revolvatur corpus in ellipsi: requiritur lex vis centripetæ tendentis ad umbilicum ellipseos.*

**Inglese:** “If a body revolves in an ellipsis; it is required to find the law of the centripetal force tending to the focus of the ellipsis.”

**Scelte e letture.**

- La prima dimostrazione usa lettere che il testo della Prop. XI non definisce (DK, G, F, Z): vengono dalla figura e dalla Prop. X. DK è il diametro coniugato di PG, PF la perpendicolare da P su DK; Z, perché gli angoli IPR e HPZ siano uguali, deve stare sulla tangente RP prolungata oltre P (proprietà di riflessione dei fuochi): allora, essendo HI parallela a PR, il triangolo PIH è isoscele e PI = PH. Questa ricostruzione è coerente con le lettere della Prop. XII, che definisce CA, CB, PG, KD, PF; la conseguenza EP = AC è verificata numericamente (nota N1).
- *GvP*: rettangolo Gv × vP (la Prop. XII scrive *rectangulum GvP*).
- *quæ conjunctim axem totum 2AC adæquant*: «che considerate congiuntamente uguagliano l’asse intero»; qui *conjunctim* indica la somma PS + PH.
- *L×QR sit ad QT quad.*: la Prop. XII ha *fit*; *sit* è probabilmente un refuso della trascrizione. *coentibus* per *coeuntibus*: refuso probabile della trascrizione. Entrambi da verificare sulla stampa.
- **Seconda dimostrazione.** La trascrizione ha *PE cub.SPq* = PE³/SP². **Motte 1846 (SVG 96) stampa PE²/SP²**: refuso dell’edizione 1846 o della sua trascrizione Gutenberg; Motte 1729 ha PE³, e anche la stampa del 1726 ha *PE cub.* (Fascicolo 3, F3). Ho ricontrollato la derivazione con lo script di questo fascicolo (nota N2).
- *Eadem brevitate, qua traduximus problema quintum ad parabolam*: *traducere* è reso «estendere»; Motte ha «reduced». Il «quinto problema» è la Prop. X.

### A.2 Proposizione XII

**Latino:** *Moveatur corpus in hyperbola: requiritur lex vis centripetæ tendentis ad umbilicum figuræ.*

**Inglese:** “Suppose a body to move in an hyperbola; it is required to find the law of the centripetal force tending to the focus of that figure.”

**Scelte e letture.**

- *Agatur SP secans cum diametrum DK in E, tum ordinatim applicatam*: «cum» è refuso probabile della trascrizione per «tum».
- **Motte 1846, SVG 99:** stampa L×SP² uguale a **SP²×QR/QT²**, cioè la frazione capovolta. Il latino ha *SPq×QTqQR* = SP²×QT²/QR, come la Prop. XI (dove Motte, SVG 95, è corretto). È un errore dell’edizione 1846 o della sua trascrizione; Motte 1729 non è stato controllato.
- *vis, quæ tendit ab hyperbolæ centro C*: «la forza che tende dal centro»: per l’iperbole la forza proporzionale alla distanza è repulsiva. Motte rende bene («tending from»).
- **Seconda dimostrazione:** qui Motte (SVG 100) ha correttamente PE³/SP².
- *in hyperbola opposita*: **Motte traduce «conjugate hyperbola»**. È un errore di senso: l’iperbole opposta è l’altro ramo della stessa iperbole (quello che volge la convessità verso S); l’iperbole coniugata ha gli assi scambiati e altri fuochi. Lo stesso errore torna nello Scolio della Sez. IV.

### A.3 Lemmi XIII e XIV

**Lemma XIII. Latino:** *Latus rectum parabolæ ad verticem quemvis pertinens est quadruplum distantiæ verticis illius ab umbilico figuræ. Patet ex Conicis.* **Inglese:** “The latus rectum of a parabola belonging to any vertex is quadruple the distance of that vertex from the focus of the figure. This is demonstrated by the writers on the conic sections.”

- *Ad verticem quemvis pertinens*: il «vertice» è qui un punto qualsiasi della parabola, vertice del diametro che vi passa; il lato retto relativo è il parametro di quel diametro. Motte parafrasa *Patet ex Conicis* in una frase intera.

**Lemma XIV. Latino:** *Perpendiculum, quod ab umbilico parabolæ ad tangentem ejus demittitur, medium est proportionale inter distantias umbilici a puncto contactus & a vertice principali figuræ.* **Inglese:** “The perpendicular, let fall from the focus of a parabola on its tangent, is a mean proportional between the distances of the focus from the point of contact, and from the principal vertex of the figure.”

- La trascrizione ha *MN, & NP* con una virgola in più; non cambia il senso.
- Motte rende fedelmente i tre corollari.

### A.4 Proposizione XIII e corollari

**Latino:** *Moveatur corpus in perimetro parabolæ: requiritur lex vis centripetæ tendentis ad umbilicum hujus figuræ.* **Inglese:** “If a body moves in the perimeter of a parabola; it is required to find the law of the centripetal force tending to the focus of that figure.”

- *in quem corpus proxime movetur*: «nel quale il corpo si porta subito dopo»; Motte «into which it is next to succeed».
- *occurentem*: forma con una sola *r*, forse grafia della stampa; da verificare.
- *per prop. ix. lib. v. elem.*: Euclide, *Elementi* V, 9 (grandezze che hanno lo stesso rapporto con una stessa grandezza sono uguali).
- **Cor. 1.** *simul agitetur* è reso «sia insieme sottoposto all’azione»; Motte «is urged by the action of». *Et contra* «e viceversa».
- **Cor. 2.** *in minima aliqua temporis particula*: Motte «in any infinitely small moment of time» aggiunge «infinitely». *quæ ultimo fit*: «che si ha alla fine» (glossario: *ultimo* «alla fine»); Motte «in its ultimate state». *Circulum … refero ad ellipsin*: «riconduco il cerchio all’ellisse», cioè lo conto fra le ellissi.

### A.5 Propp. XIV–XVI

**Prop. XIV. Latino:** *Si corpora plura revolvantur circa centrum commune, & vis centripeta sit reciproce in duplicata ratione distantiæ locorum a centro; dico quod orbium latera recta principalia sunt in duplicata ratione arearum, quas corpora radiis ad centrum ductis eodem tempore describunt.* **Inglese:** “If several bodies revolve about one common centre, and the centripetal force is reciprocally in the duplicate ratio of the distance of places from the centre; I say, that the principal latera recta of their orbits are in the duplicate ratio of the areas, which the bodies by radii drawn to the centre describe in the same time.”

- *linea minima QR*: Motte «lineola QR». Il corollario unico (*Corol.*) è reso «Cor.».

**Prop. XV. Latino:** *Iisdem positis, dico quod tempora periodica in ellipsibus sunt in ratione sesquiplicata majorum axium.* **Inglese:** “The same things being supposed, I say, that the periodic times in ellipses are in the sesquiplicate ratio of their greater axes.”

- **Motte cita «Cor. 3., Prop. XIV»**, ma la Prop. XIV ha un solo corollario: il latino ha *per corol. prop. xiv.* È un errore di Motte 1846 (o della sua trascrizione).
- *manebit sesquiplicata ratio majoris axis eadem cum ratione periodici temporis*: «resterà il rapporto sesquiplicato dell’asse maggiore, identico al rapporto del tempo periodico».
- La trascrizione spezza *ra <61> tione* con il marcatore di pagina.

**Prop. XVI. Latino:** *Iisdem positis, & actis ad corpora lineis rectis, quæ ibidem tangant orbitas, demissisque ab umbilico communi ad has tangentes perpendicularibus: dico quod velocitates corporum sunt in ratione composita ex ratione perpendiculorum inverse, & subduplicata ratione laterum rectorum principalium directe.* **Inglese:** “The same things being supposed, and right lines being drawn to the bodies that shall touch the orbits, and perpendiculars being let fall on those tangents from the common focus; I say, that the velocities of the bodies are in a ratio compounded of the ratio of the perpendiculars inversely, and the subduplicate ratio of the principal latera recta directly.”

- Formule: *SYq L* = SY²/L (Motte SVG 102); *SP×QTSY* = SP×QT/SY (SVG 103); *SP QT* = SP×QT.
- Motte rende *arcus quam minimus* «infinitely small arc» e *data temporis particula* «given moment of time».
- **Cor. 4:** *Corpurum* è refuso probabile della trascrizione per *Corporum*.
- **Cor. 7:** *per hujus corollarium secundum* — Newton cita il Cor. 2; il rapporto √2 nel vertice si legge più direttamente nel Cor. 3, che discende dal 2 (nota N8). *per corollaria sexta hujus & propositionis quartæ*: «per i corollari sesti di questa proposizione e della Prop. IV»; Motte «by Cor. 6 of this Prop. and Prop. IV», che lascia sottinteso il Cor. 6 della Prop. IV.
- Nell’EPUB Motte la didascalia della figura della Prop. XVI riporta per errore l’enunciato della Prop. XV: artefatto dell’EPUB, non del testo.

### A.6 Proposizione XVII e corollari; Scolio della Sezione III

**Latino:** *Posito quod vis centripeta sit reciproce proportionalis quadrato distantiæ a centro, & quod vis illius quantitas absoluta sit cognita; requiritur linea, quam corpus describit de loco dato cum data velocitate secundum datam rectam egrediens.* **Inglese:** “Supposing the centripetal force to be reciprocally proportional to the squares of the distances of places from the centre, and that the absolute quantity of that force is known; it is required to determine the line which a body will describe that is let go from a given place with a given velocity in the direction of a given right line.”

- **Formule.** *SPq−2KPH+PHq=SHq=4CHq=4BHq−4BCq=SP+PH¯: quad.−L×SP+PH¯=SPq+2SPH+PHq−L×SP+PH¯* è letta: SP² − 2KP×PH + PH² = SH² = 4CH² = 4BH² − 4BC² = (SP + PH)² − L×(SP + PH) = SP² + 2SP×PH + PH² − L×(SP + PH). *KPH* e *SPH* sono prodotti KP×PH e SP×PH (la notazione a tre lettere per il prodotto di due segmenti con estremo comune è di Newton). Motte, SVG 104–106, concorda con questa lettura.
- **Refuso:** *axe principali SP+AH* — la trascrizione ha **AH** dove il senso e Motte richiedono **PH** (l’asse dell’ellisse è SP + PH). Tradotto «SP + PH»; da verificare sulla stampa se il refuso sia della trascrizione o dell’edizione.
- *Hanc igitur recta PR tanget in P*: Motte, «Thus, the right line PR will therefore touch in P», perde l’oggetto *hanc* (la sezione conica) e duplica «Thus … therefore».
- Motte rende *egrediens*, *exeat* con «let go», che suggerisce un corpo lasciato cadere; il latino indica un corpo che parte con velocità data.
- **Cor. 2:** *in circul ad distantiam DS* — refuso probabile della trascrizione per *circulo*.
- **Cor. 3:** *impulsu quocunque*: «impulso», secondo il glossario (azione istantanea che cambia la quantità di moto). *exturbetur*: «è sbalzato fuori».
- **Cor. 4:** *vi aliqua extrinsecus impressa*: «una forza impressa dall’esterno»; Motte «some foreign force». *ex seriei analogia*: «dall’analogia della serie»; Motte amplia: «from the analogy that appears in the progress of the series».
- **Scolio.** La trascrizione ha *CG cub.RP quad.* = CG³/RP². **Motte 1846, SVG 107, stampa CG²/RP²**: errore dell’edizione 1846 o della sua trascrizione. Il controllo numerico (nota N11) conferma CG³/RP². Motte 1729 non è stato controllato.

### A.7 Lemma XV e Propp. XVIII–XIX

**Lemma XV. Latino:** *Si ab ellipseos vel hyperbolæ cujusvis umbilicis duobus S, H, ad punctum quodvis tertium V inflectantur rectæ duæ SV, HV, quarum una HV æqualis sit axi principali figuræ, id est, axi in quo umbilici jacent, altera SV a perpendiculo TR in se demisso bisecetur in T; perpendiculum illud TR sectionem conicam alicubi tanget: & contra, si tangit, erit HV æqualis axi principali figuræ.* **Inglese:** “If from the two foci S, H, of any ellipsis or hyperbola, we draw to any third point V the right lines SV, HV, whereof one HV is equal to the principal axis of the figure, that is, to the axis in which the foci are situated, the other, SV, is bisected in T by the perpendicular TR let fall upon it; that perpendicular TR will somewhere touch the conic section: and, vice versa, if it does touch it, HV will be equal to the principal axis of the figure.”

- *inflectantur*: «si conducono» (§ A.0).

**Prop. XVIII. Latino:** *Datis umbilico & axibus principalibus describere trajectorias ellipticas & hyperbolicas, quæ transibunt per puncta data, & rectas positione datas contingent.* **Inglese:** “From a focus and the principal axes given, to describe elliptic and hyperbolic trajectories, which shall pass through given points, and touch right lines given by position.”

- *figuraram*: refuso probabile della trascrizione per *figurarum*.
- *intervallo*: «raggio» (§ A.0); Motte «interval».

**Prop. XIX. Latino:** *Circa datum umbilicum trajectoriam parabolicam describere, quæ transibit per puncta data, & rectas positione datas continget.* **Inglese:** “About a given focus, to describe a parabolic trajectory, which shall pass through given points, and touch right lines given by position.”

- *ut fit TV æqualis ST*: *fit* per *sit*, refuso probabile della trascrizione.
- Nell’EPUB Motte manca l’a capo fra «PROPOSITION XIX. PROBLEM XI.» e l’enunciato: artefatto tipografico.
- Quando sono dati un punto P e una tangente TR, dal punto V escono due rette tangenti al cerchio FG; il testo non dice quale scegliere. Solo una dà la parabola cercata (nota N12).

### A.8 Proposizione XX

**Latino:** *Circa datum umbilicum trajectoriam quamvis specie datam describere, quæ per data puncta transibit & rectas tanget positione datas.* **Inglese:** “About a given focus to describe any trajectory given in specie which shall pass through given points, and touch right lines given by position.”

- *specie datam*: «data di forma» (glossario); Motte conserva il latino «in specie».
- **Caso 2.** La catena *ut Vk−VK ad kS−KS, id est, ut 2VX ad 2KX & 2KX ad 2SX* si legge così: la somma VK + Vk vale 2VX e la somma KS + kS vale 2KX (componendo); la differenza Vk − VK vale 2KX e la differenza kS − KS vale 2SX (separando). Il rapporto comune è dunque VX : KX = KX : SX, e, poiché HX = KX (raggio), VX : HX = HX : SX.
- **Caso 3.** Il latino dice *ellipseos describendæ* anche se il caso vale per ogni conica data di forma; Motte fa lo stesso. Tradotto alla lettera.
- **Caso 4.** **Motte stampa «similar to the figure aph»** per *apb*: refuso. *biscatur*: refuso probabile della trascrizione per *bisecatur*. Motte 1846 ripete come didascalia di figura la prima frase della costruzione. Il Lemma XV è usato nell’ultima frase senza essere citato.

### A.9 Lemma XVI, Prop. XXI, Scolio della Sezione IV

**Lemma XVI. Latino:** *A datis tribus punctis ad quartum non datum inflectere tres rectas quarum differentiæ vel dantur vel nullæ sunt.* **Inglese:** “From three given points to draw to a fourth point that is not given three right lines whose differences shall be either given, or none at all.”

- **Motte aggiunge** «(QS)» e «(this ZS)» nel Caso 1 e un «Q.E.I.» in fondo al Caso 2, assente nel latino.
- *Cape PM ad MA*: il testo non dice da quale parte di M stia P; il controllo numerico mostra che P cade fra M e il centro dell’iperbole, cioè che PR è la direttrice relativa al fuoco A (nota N13).
- *per librum tactionum Apollonii a Vieta restitutum*: il libro *Sulle tangenze* (*De tactionibus*) di Apollonio, perduto e restituito da François Viète. Motte: «Apollonius’s Book of Tactions restored by Vieta».

**Prop. XXI. Latino:** *Trajectoriam circa datum umbilicum describere, quæ transibit per puncta data & rectas positione datas continget.* **Inglese:** “About a given focus to describe a trajectory that shall pass through given points and touch right lines given by position.”

- *ST, <72> {&} produc*: il «&» tra graffe è un’integrazione editoriale del Newton Project; la traduzione lo segue.

**Scolio.** *oppositam hyperbolam* (due volte): **Motte «conjugate hyperbola»**, errore di senso (vedi A.2); Motte aggiunge anche «continued» e «never». *cica umbilicum*: refuso probabile della trascrizione per *circa*. *clarissimus geometra de la Hire*: Philippe de La Hire; Motte «That excellent geometer M. De la Hire». *Junctas BC, CD … ut SB ad SC,& FC*: spazio mancante nella trascrizione, senza conseguenze.

### A.10 Refusi e anomalie della trascrizione

Tutti da verificare sulla stampa del 1726; la traduzione segue il senso.

| Luogo | Trascrizione | Lettura |
|---|---|---|
| Prop. XI (S3.03) | *L×QR sit ad QT quad.* | *fit* (come nella Prop. XII) |
| Prop. XI (S3.04) | *coentibus* | *coeuntibus* |
| Prop. XII (S3.08) | *secans cum diametrum* | *tum* |
| Prop. XIII (S3.20) | *occurentem* | *occurrentem* (forse grafia della stampa) |
| Prop. XVI, Cor. 4 (S3.35) | *Corpurum* | *Corporum* |
| Prop. XVII (S3.44) | *axe principali SP+AH* | *SP+PH* |
| Prop. XVII, Cor. 2 (S3.47) | *in circul* | *in circulo* |
| Prop. XVIII (S4.04) | *figuraram* | *figurarum* |
| Prop. XIX (S4.07) | *ut fit TV* | *ut sit* |
| Prop. XX, Caso 4 (S4.17) | *biscatur* | *bisecatur* |
| Scolio IV (S4.28) | *cica umbilicum* | *circa* |
| Formule | *SPqQR*, *QTqQR*, *SYq L*, *SP×QTSY*, *PE cub.SPq*, *CG cub.RP quad.*, *2BC quad.AC*, *2BCqAC*, *SP+PH¯* | SP²/QR, QT²/QR, SY²/L, SP×QT/SY, PE³/SP², CG³/RP², 2BC²/AC, vincolo |

Il Q.E.I. della prima dimostrazione della Prop. XI è senza punto finale; la punteggiatura dei titoli (*PROPOSITIO. XIII. PROBLEMA. VIII.*) è irregolare. Nessuna di queste anomalie cambia il senso.

### A.11 Riepilogo: dove Motte aggiunge, omette o sbaglia

| Luogo | Latino | Motte 1846 | Tipo |
|---|---|---|---|
| Prop. XI, 2ª dim. (S3.05) | *PE cub./SPq* | PE²/SP² (SVG 96) | **formula errata** (Motte 1729: PE³) |
| Prop. XI (S3.06) | *traduximus* | «reduced» | resa discutibile |
| Prop. XII (S3.10) | *SPq×QTq/QR* | SP²×QR/QT² (SVG 99) | **formula errata** (frazione capovolta) |
| Prop. XII (S3.12) | *hyperbola opposita* | «conjugate hyperbola» | **errore di senso** |
| Lemma XIII (S3.13) | *Patet ex Conicis* | «This is demonstrated by the writers on the conic sections» | parafrasi |
| Prop. XIII (S3.20) | *constructio lemmatis* | «of the preceding Lemma» | aggiunta |
| Prop. XIII, Cor. 2 (S3.23) | *minima aliqua temporis particula* | «any infinitely small moment of time» | aggiunta |
| Prop. XIV (S3.25) | *linea minima* | «lineola» | resa diversa |
| Prop. XV (S3.28) | *per corol. prop. xiv.* | «by Cor. 3., Prop. XIV» | **rimando errato** |
| Prop. XVI (S3.31) | *arcus quam minimus … data temporis particula* | «infinitely small arc … given moment» | aggiunta; resa diversa |
| Prop. XVI, Cor. 7 (S3.38) | *corollaria sexta hujus & propositionis quartæ* | «Cor. 6 of this Prop. and Prop. IV» | semplificazione |
| Prop. XVII (S3.42) | *Hanc igitur recta PR tanget in P* | «Thus, the right line PR will therefore touch in P» | omissione dell’oggetto |
| Prop. XVII (S3.41–S3.42) | *egrediens*, *exeat* | «let go» | resa fuorviante |
| Prop. XVII, Cor. 4 (S3.49) | *vi extrinsecus impressa*; *ex seriei analogia* | «foreign force»; «from the analogy that appears in the progress of the series» | resa diversa; ampliamento |
| Scolio III (S3.50) | *CG cub./RP quad.* | CG²/RP² (SVG 107) | **formula errata** |
| Prop. XX, Caso 4 (S4.17) | *figuræ apb* | «the figure aph» | lettera errata |
| Lemma XVI, Caso 1 (S4.19) | — | «(QS)», «(this ZS)» | aggiunte esplicative |
| Lemma XVI, Caso 2 (S4.21) | — | «Q.E.I.» | aggiunta |
| Scolio IV (S4.26) | *oppositam hyperbolam* (due volte) | «conjugate hyperbola» | **errore di senso** |
| Scolio IV (S4.26) | *pergendo in motu suo … non potest* | «going on with a continued motion can never pass» | aggiunte |

Le altre formule-immagine di Motte (SVG 37, 41, 63, 67–70, 84–95, 97, 98, 100–106) concordano con il latino.

---

## Note editoriali e fisiche

Queste note sono aggiunte del presente fascicolo, non affermazioni tradotte da Newton. I controlli numerici sono stati eseguiti con lo script `verifica.py` (Python, NumPy), conservato con i file di lavoro.

### N1. Prop. XI: che cosa si dimostra e verifica numerica

La proposizione risolve il problema «diretto»: data l’orbita ellittica con la forza diretta al fuoco, si trova la legge della forza. La misura della forza è quella del Cor. 1 e 5 della Prop. VI: la forza è inversamente come SP²×QT²/QR al limite. Il cuore della dimostrazione è che L×QR/QT² tende a 1, cioè QT²/QR → L: allora SP²×QT²/QR → L×SP² e la forza è come 1/SP². In termini moderni: per un’orbita di lato retto L = 2*b*²/*a* e velocità areolare costante, *F* = 2*h*²/(*L* *r*²), con *h* il doppio della velocità areolare.

**Verifica (ellisse *a* = 5, *b* = 3, P al parametro *t* = 1,1):**

- EP = 5,000000 = AC (proprietà EP = AC);
- CD × PF = 15,000000 = AC × BC (Lemma XII, usato nella dimostrazione);
- Px = QR (parallelogramma QxPR) a ogni passo;
- L×QR/QT² = 0,899 (Q a Δ*t* = 0,1), 0,98893 (Δ*t* = 0,01), 0,99888 (Δ*t* = 0,001) → 1;
- 2PC/Gv = 1,0025; 1,000025; 1,0000000 → 1.

Lo scarto di L×QR/QT² da 1 è proporzionale a Δ*t*, come ci si aspetta da un rapporto ultimo. Nella ricostruzione ho preso QR parallela a SP con R sulla tangente, Qv parallela alla tangente con v su PG e x su SP, QT perpendicolare a SP: è la costruzione della Prop. VI, compatibile con tutte le relazioni del testo.

### N2. Prop. XI, seconda dimostrazione: PE³/SP²

Il Cor. 3 della Prop. VII confronta le forze verso due centri S e R (qui R = C) con cui uno stesso corpo descrive la stessa orbita: forza verso S : forza verso C = SP × CP² : SG³, dove SG, parallela a CP, va da S alla tangente. Per i triangoli simili, SG = CP × SP / PE (verificato: SG = 2,233750 in entrambi i modi). Con la forza verso C proporzionale a CP si ottiene forza verso S ∝ PE³/SP², e poiché PE = AC è costante, ∝ 1/SP². La lezione **PE²** di Motte 1846 darebbe lo stesso risultato finale (perché PE è costante) ma è dimensionalmente incoerente con il Cor. 3 della Prop. VII. Il latino 1726 e Motte 1729 hanno PE³ (Fascicolo 3, F3).

### N3. Prop. XII: iperbole e iperbole opposta

Verifica sull’iperbole *a* = 3, *b* = 2: EP = 3,000000 = AC; CD × PF = 6 = AC × BC; L×QR/QT² = 0,840; 0,98229; 0,99821 → 1. L’ultima frase della proposizione contiene un risultato fisico notevole: con una forza **repulsiva** inversamente proporzionale al quadrato della distanza da S, il corpo percorre l’altro ramo dell’iperbole, quello che volge la convessità verso S. È la traiettoria di una carica respinta da un nucleo (diffusione di Rutherford, 1911). La resa «conjugate hyperbola» di Motte (A.2) farebbe pensare a un’altra curva.

### N4. Lemmi XIII–XIV e Prop. XIII

Parabola *y*² = 4*fx* con *f* = SA = 1,5 e P di ordinata 2,7: SN² = 4,0725 = PS × SA (Lemma XIV); N ha ascissa 0, cioè sta sulla tangente nel vertice (Cor. 3); MS = SP = 2,715. Nella Prop. XIII, Px = Pv = QR esattamente, Qv² = 4PS × Pv esattamente (Lemma XIII: il lato retto del diametro per P è 4PS), e QT²/(4SA × QR) = 1,102; 1,00997; 1,000995 → 1.

### N5. Prop. XIII, Cor. 1: il problema inverso

Il Cor. 1 afferma il **viceversa**: un corpo lanciato in qualsiasi modo sotto una forza inversamente proporzionale al quadrato della distanza percorre una conica con il fuoco nel centro delle forze. L’argomento di Newton è un argomento di unicità: per ogni posizione, direzione e velocità esiste una conica con fuoco S che ha in quel punto la curvatura richiesta (la costruzione è la Prop. XVII), e due orbite tangenti non possono avere la stessa velocità e la stessa forza. In termini moderni è il teorema di unicità della soluzione delle equazioni del moto per condizioni iniziali date; Newton non lo dimostra in generale, ma lo usa. Per il curatore: è un punto adatto a una discussione in classe sul rapporto fra «problema diretto» e «problema inverso».

### N6. Prop. XIV: lato retto e velocità areolare

In termini moderni, con *h* = *r*²dθ/d*t* (il doppio della velocità areolare) e *GM* la quantità assoluta della forza, il lato retto vale L = 2*h*²/*GM*. Verifica per integrazione numerica (Runge–Kutta del quarto ordine, *GM* = 1) su quattro orbite diverse: L/*h*² = 2,00000 in tutti i casi. Il Cor. 2 della Prop. XIII, che la dimostrazione usa, è proprio la definizione di L come QT²/QR al limite.

### N7. Prop. XV: la terza legge di Keplero

Il passaggio chiave è che l’asse minore è medio proporzionale fra asse maggiore e lato retto: *b*² = *a* · L/2 (verificato: rapporto 1,00000 sulle quattro orbite integrate). Combinato con il Cor. della Prop. XIV, dà *T* ∝ *a*^{3/2}. Verifica numerica: *T*²/*a*³ = 39,479 ± 0,004 sulle quattro orbite, contro 4π² = 39,478; lo scarto residuo è l’errore di integrazione. Il Cor. della Prop. XV (stessi periodi dei cerchi di diametro uguale all’asse maggiore) è la stessa legge espressa per *a*.

### N8. Prop. XVI: velocità e perpendicolare

La proposizione equivale a *v* = *h*/SY (conservazione del momento angolare: *h* = *v* × SY), con *h* ∝ √L. Verifiche (ellisse *a* = 2, *e* = 0,6, *GM* = 1):

- Prop. XVI: *v* = 0,707107 = √(L/2)/SY;
- Cor. 3: al perielio *v*/*v*_circ = 1,264911 = √(L/(2SP));
- Cor. 4: alla distanza media *r* = *a* (estremo dell’asse minore) *v* = 0,707107 = √(1/*a*), velocità circolare a quella distanza;
- Cor. 7: nella parabola *v*/*v*_circ = 1,414214 = √2 a ogni distanza, e *v* alla distanza *r* è uguale alla velocità circolare a *r*/2. È la moderna **velocità di fuga** √(2*GM*/*r*).

Nel Cor. 7 Newton cita il Cor. 2; il valore √2 nel vertice si ottiene più direttamente dal Cor. 3 (nel vertice della parabola L = 4SA = 4 · SP, quindi √(L/2SP) = √2), che a sua volta discende dal Cor. 2.

### N9. Prop. XVII: dalle condizioni iniziali all’orbita

È il problema dei dati iniziali: posizione, velocità e direzione. Il lato retto L si ricava dal Cor. 1 della Prop. XVI confrontando con un’orbita nota (oggi: L = 2*h*²/*GM*). Il secondo fuoco H sta sulla retta PH simmetrica di PS rispetto alla normale in P (proprietà di riflessione), e la relazione di Newton dà PH = L × SP / (2SP + 2KP − L).

**Il criterio di Newton coincide con quello dell’energia.** Detto φ l’angolo fra la tangente e PS, KP = SP cos(SPH) con SPH = 180° − 2φ, quindi 2SP + 2KP = 4SP sin²φ; e L = 2*r*²*v*² sin²φ/*GM*. La condizione L < 2SP + 2KP equivale a *v*² < 2*GM*/*r*: energia negativa, ellisse; L = 2SP + 2KP equivale alla velocità di fuga, parabola; L maggiore, iperbole.

**Verifica numerica** (P = (1, 0), S nell’origine, *GM* = 1), confrontando H costruito con la regola di Newton con il secondo fuoco calcolato dal vettore di eccentricità:

| velocità | L | 2SP + 2KP | PH | H (Newton) | H (vero) | energia |
|---|---|---|---|---|---|---|
| (0,3; 1,0) | 2,000 | 3,670 | 1,198 | (0; 0,6593) | (0; 0,6593) | −0,455, ellisse |
| (0,3; 1,2) | 2,880 | 3,765 | 3,255 | (−1,8723; 1,5319) | (−1,8723; 1,5319) | −0,235, ellisse |
| (0; √2) | 4,000 | 4,000 | ∞ | — | — | 0, parabola |
| (0,2; 1,6) | 5,120 | 3,939 | −4,333 | (5,2; −1,0667) | (5,2; −1,0667) | +0,300, iperbole |

Il segno negativo di PH nel caso iperbolico corrisponde alla prescrizione di Newton: «PH andrà presa dall’altra parte della tangente». Il Cor. 1 (DH : DS = L : (4DS − L)) è verificato algebricamente per l’ellisse: con DS = *a* − *c*, DH = *a* + *c*, L = 2(*a*² − *c*²)/*a*, si ha 4DS − L = 2(*a* − *c*)²/*a* e L/(4DS − L) = (*a* + *c*)/(*a* − *c*). I Cor. 3 e 4 sono il germe del calcolo delle perturbazioni: un impulso cambia la velocità e quindi l’orbita «osculatrice».

### N10. «Complemento a due retti»

*Anguli RPS complementum ad duos rectos* è quello che oggi si chiama supplemento: l’angolo RPH è 180° meno l’angolo RPS. Geometricamente PH e PS formano angoli uguali con la tangente, da parti opposte della normale: è la proprietà ottica dei fuochi. Per il curatore: in classe conviene dire «supplemento» in nota, lasciando la formula storica nel testo.

### N11. Scolio della Sez. III: forza verso un punto qualsiasi

Per un corpo che descrive una conica di centro C sotto una forza diretta a un punto qualsiasi R, la forza è come CG³/RP², dove CG è parallela a RP e G sta sulla tangente. Verifica: per un’ellisse *a* = 3, *b* = 2 con R = (0,7; −0,4), ho calcolato la forza necessaria in sette punti con la formula della curvatura (*F* = *h*² *r* / (*p*³ ρ), con *p* la perpendicolare da R sulla tangente e ρ il raggio di curvatura). Il rapporto *F* / (CG³/RP²) è 0,027778 in tutti e sette i punti, cioè costante. La lezione CG² di Motte 1846 non darebbe un rapporto costante. Per R = C si ritrova la forza proporzionale alla distanza (Prop. X); per R nel fuoco, CG³/RP² si riduce a una costante per 1/RP², come nella seconda dimostrazione della Prop. XI.

### N12. Sezione IV: costruzioni e verifiche

La Sezione IV è puramente geometrica: serve a costruire l’orbita (pensando alle comete) da dati di osservazione, cioè punti e tangenti, quando è noto il fuoco. Lo strumento comune è il **Lemma XV**: il simmetrico V del fuoco S rispetto a una tangente dista dall’altro fuoco quanto l’asse principale.

- **Prop. XVIII** (S = origine, AB = 6, P = (2; 1,5), una tangente data): le due intersezioni dei cerchi danno due soluzioni H; per entrambe SP + PH = 6,000000, HV = 6,000000, e il minimo di SX + HX lungo la tangente è 6,000000, cioè la retta tocca l’ellisse.
- **Prop. XIX** (parabola): dal punto V escono due tangenti al cerchio FG. Con la prima, S risulta quasi sulla retta IF (SK = 0,0029) e la retta TR non tocca la parabola (minimo di SX − distanza dalla direttrice = 0,024 > 0); con la seconda, SK = IK = 1,8458 e TR è tangente (minimo ≈ 1,5 × 10⁻⁶, al limite della griglia di campionamento). Il testo non discute la scelta: la tangente valida è quella che lascia S e P dalla stessa parte della direttrice IF.
- **Prop. XX, Caso 2** (eccentricità data 0,5, due tangenti): le due soluzioni H trovate sul cerchio di diametro Kk danno SH/VH = 0,500000 e VH = vH; entrambe le tangenti toccano la conica (scarto < 10⁻⁸).
- I Casi 3 e 4 della Prop. XX non sono stati verificati numericamente.

### N13. Lemma XVI e Prop. XXI: il problema di Apollonio

Trovare un punto le cui distanze da tre punti dati abbiano differenze date significa intersecare due iperboli con un fuoco comune A. Newton usa per ciascuna la proprietà fuoco–direttrice (ZR : AZ = MN : AB, dove MN : AB è l’inverso dell’eccentricità) e riduce l’intersezione delle due iperboli all’intersezione di due rette. Verifica: per l’iperbole di fuochi (±2; 0) e asse MN = 2, con P preso fra M e il centro (PM : MA = MN : AB), ZR/AZ = 0,500000 = MN/AB in tre punti diversi. La Prop. XXI riconduce al lemma la ricerca del secondo fuoco: ogni tangente dà un punto Y con YH = asse, ogni punto P un punto con |PH − asse| = SP. È, in forma moderna, lo stesso principio della localizzazione per differenze di tempo d’arrivo (iperboli di ugual differenza di distanza).

### N14. Scolio della Sez. IV: tre punti e direttrice

La costruzione per tre punti trova direttamente la **direttrice** EF: E e F dividono esternamente BC e CD nei rapporti delle distanze dal fuoco. Verifica su una conica di eccentricità 0,6 con direttrice *x* = 4: i punti E ed F costruiti hanno entrambi ascissa 4,000000, e SB/HB = SC/IC = SD/KD = 0,600000. La classificazione «ellisse, parabola, iperbole secondo che GA sia maggiore, uguale o minore di AS» è la classificazione per eccentricità *e* = AS/GA minore, uguale o maggiore di 1.

---

## Controllo della copertura

Le pagine del latino sono quelle dell’edizione 1726 segnate nella trascrizione; per Motte valgono i marcatori di pagina dell’EPUB.

| Identificatori | Incipit latino | Contenuto | 1726 | Motte 1846 |
|---|---|---|---|---|
| S3.01–S3.06 | *Revolvatur corpus in ellipsi* | Prop. XI, due dimostrazioni, nota sui casi seguenti | pp. 54–56 | pp. 116–117 |
| S3.07–S3.12 | *Moveatur corpus in hyperbola* | Prop. XII, due dimostrazioni, iperbole opposta | pp. 56–58 | pp. 117–119 |
| S3.13 | *Latus rectum parabolæ* | Lemma XIII | p. 58 | p. 119 |
| S3.14–S3.18 | *Perpendiculum, quod ab umbilico* | Lemma XIV e Cor. 1–3 | p. 58 | p. 119 |
| S3.19–S3.23 | *Moveatur corpus in perimetro parabolæ* | Prop. XIII e Cor. 1–2 | pp. 58–60 | pp. 119–120 |
| S3.24–S3.26 | *Si corpora plura revolvantur* | Prop. XIV e corollario | p. 60 | p. 120 |
| S3.27–S3.29 | *Iisdem positis, dico quod tempora periodica* | Prop. XV e corollario | pp. 60–61 | p. 121 |
| S3.30–S3.40 | *Iisdem positis, & actis ad corpora* | Prop. XVI e Cor. 1–9 | pp. 61–63 | pp. 121–123 |
| S3.41–S3.49 | *Posito quod vis centripeta* | Prop. XVII e Cor. 1–4 | pp. 63–65 | pp. 123–124 |
| S3.50 | *Si corpus P vi centripeta* | Scolio della Sez. III | p. 65 | p. 125 |
| S4.01–S4.02 | *Si ab ellipseos vel hyperbolæ* | Lemma XV | p. 66 | p. 125 |
| S4.03–S4.05 | *Datis umbilico & axibus principalibus* | Prop. XVIII | pp. 66–67 | p. 126 |
| S4.06–S4.08 | *Circa datum umbilicum trajectoriam parabolicam* | Prop. XIX | p. 67 | p. 126 |
| S4.09–S4.17 | *Circa datum umbilicum trajectoriam quamvis* | Prop. XX, Casi 1–4 | pp. 68–70 | pp. 127–129 |
| S4.18–S4.23 | *A datis tribus punctis* | Lemma XVI, Casi 1–3, Apollonio–Viète | pp. 70–71 | pp. 129–130 |
| S4.24–S4.25 | *Trajectoriam circa datum umbilicum* | Prop. XXI | pp. 71–72 | p. 130 |
| S4.26–S4.29 | *Ubi trajectoria est hyperbola* | Scolio della Sez. IV, tre punti, de la Hire | pp. 72–73 | pp. 130–131 |

**Controlli eseguiti.**

1. **Rilettura frase per frase contro il latino.** Ho confrontato in sequenza ogni periodo delle due trascrizioni, da *Revolvatur corpus in ellipsi* a *conicorum suorum lib. VIII. prop XXV.*, con la traduzione. Nessuna frase manca; i periodi lunghi sono resi in un’unica frase italiana o divisi senza omettere membri. Per le 15 unità della Parte B l’allineamento è stato fatto automaticamente: ogni frase latina e inglese è stata estratta dalle fonti con ancore di inizio e fine in ordine di testo, e lo stesso file genera sia i paragrafi della traduzione sia i passi del JSON, che quindi coincidono.
2. **Parte B.** `check.py` sul fascicolo, con i due file latini e i due di Motte: **OK**, nessun errore e nessun avviso (15 unità, 123 passi, 79 identificatori).
3. **Matematica.** Verifiche numeriche con `verifica.py`: Propp. XI, XII, XIII (rapporti ultimi → 1), Lemmi XII, XIII, XIV, seconda dimostrazione della Prop. XI, Propp. XIV–XVI e Cor. 3, 4, 7 della XVI (integrazione numerica), Prop. XVII nei tre casi e Cor. 1, Scolio della Sez. III, Lemma XV, Propp. XVIII, XIX, XX (Caso 2), Lemma XVI (Caso 1), Scolio della Sez. IV. Esiti nelle note N1–N14: tutti concordi con il testo.
4. **Confronto con Motte.** Ho confrontato tutte e due le sezioni, pp. 116–131, comprese le 31 formule-immagine rilevanti. Divergenze nel § A.11.
5. **Separazione fra testo e commento.** Il testo tradotto non contiene formule moderne; le uniche uguaglianze nel testo sono quelle di Newton (Prop. XVII).

**Non ho potuto verificare:**

- i **refusi della trascrizione** del § A.10 sulla stampa del 1726 (nessuna scansione disponibile in questa sessione); in particolare *SP+AH* nella Prop. XVII;
- **Motte 1729** per le formule SVG 99 (Prop. XII) e SVG 107 (Scolio della Sez. III): non so se l’errore sia già nella prima edizione inglese o soltanto nell’edizione 1846 o nella sua trascrizione Gutenberg;
- le **figure originali** NATP00087-20…37: le relazioni geometriche sono ricostruite dalle lettere del testo (in particolare D, K, F, G, Z nella Prop. XI);
- numericamente, i **Casi 3 e 4 della Prop. XX** e i Casi 2–3 del Lemma XVI;
- la **numerazione di pagina di Motte**, che deriva dai marcatori dell’EPUB e non da un esemplare a stampa.

---

## Registro del lavoro successivo

| Unità | Stato |
|---|---|
| Sezioni III e IV del Libro I | **Fascicolo 6, presente documento, prima versione** |
| Refusi della trascrizione (§ A.10), soprattutto *SP+AH* (Prop. XVII) | Da verificare sulla stampa del 1726 (scansione ECCO, come nel Fascicolo 3) |
| Motte 1729 per SVG 99 e SVG 107 | Da controllare sull’esemplare Internet Archive `bub_gb_Tm0FAAAAQAAJ`, come fatto per PE³ |
| Pagine interattive Prop. XI (pilota) | Correggere il testo a fronte di Motte (PE² → PE³, già nel registro del Fascicolo 3); allineare alla presente traduzione |
| Pagine interattive Propp. XII e Scolio III | Correggere in nota le formule di Motte (SVG 99, SVG 107) |
| Prop. XIX | Decidere come la pagina interattiva gestisce la scelta fra le due tangenti da V (nota N12) |
| Prop. XX, Casi 3–4; Lemma XVI, Casi 2–3 | Verifica numerica da eseguire prima delle pagine |
| Figure NATP00087-20…37 | Riscontro delle lettere ricostruite sulle figure originali |
| Glossario | Proporre al curatore l’adozione nel glossario comune di «lineetta», «separando / componendo / permutando / per uguaglianza», «iperbole opposta», «raggio» per *intervallum* (§ A.0) |
| Revisione filologica e scientifica indipendente | Da eseguire, come previsto dalla skill di verifica |

Il presente testo è una nuova traduzione assistita da IA. Non riproduce traduzioni italiane moderne. **Licenza prevista** (decisione del curatore, Fascicolo 3): testi e traduzioni CC BY-SA 4.0, codice MIT. La trascrizione latina è © The Newton Project e non va ridistribuita finché non se ne chiariscono le condizioni d’uso; i testi di Motte (1729, 1846) sono di pubblico dominio.

---

## Parte B — Dati per le pagine interattive

Unità incluse (lemmi, proposizioni e scolii con figura e dimostrazione o costruzione geometrica): Propp. XI, XII, XIII, XIV, XVI, XVII; Lemmi XIV, XV, XVI; Propp. XVIII, XIX, XX (Casi 1–4 in un’unica unità), XXI; Scolii delle Sezioni III e IV. Esclusi: Lemma XIII (senza dimostrazione), Prop. XV (senza figura propria: è un calcolo di rapporti), i corollari (nessuno ha una dimostrazione propria con figura).

Convenzioni:

- `la`: frase esatta della trascrizione, refusi e marcatori di pagina `<n>` compresi; i segnaposto `[FIG n]` sono omessi;
- `it`: la traduzione di questo fascicolo (identica al testo dei paragrafi indicati in `copertura`);
- `en`: Motte 1846, allineato per senso; i segnaposto `[SVG n]` sono formule-immagine, lette nella `nota` quando contano;
- `dipende_da`: soltanto i rimandi citati nella frase;
- `figura.mostra`: elementi da rendere visibili al passo; `figura.evidenzia`: relazioni da mettere in risalto.

```json
{
 "fascicolo": "06-L1-S3-4",
 "versione": "0.1",
 "data": "2026-11-08",
 "convenzioni": {
  "dipende_da": "solo rimandi citati esplicitamente nella frase",
  "en": "Motte 1846, allineato per senso; i segnaposto [SVG n] sono formule-immagine dell’EPUB, lette in nota quando contano",
  "figura.mostra": "elementi da rendere visibili al passo, cumulativi salvo indicazione",
  "la": ""
 },
 "unita": [
  {
   "id": "L1-P11",
   "tipo": "Propositio/Problema",
   "titolo": "Prop. XI — ellisse: forza verso il fuoco",
   "copertura": [
    "S3.01",
    "S3.02",
    "S3.03",
    "S3.04",
    "S3.05"
   ],
   "fonti": {
    "la": "",
    "en": "Motte 1846, pp. 116–117"
   },
   "enunciato": {
    "la": "",
    "it": "Un corpo ruoti in un’ellisse: si cerca la legge della forza centripeta diretta verso il fuoco dell’ellisse.",
    "en": "If a body revolves in an ellipsis; it is required to find the law of the centripetal force tending to the focus of the ellipsis."
   },
   "figura_base": {
    "punti": [
     "S",
     "H",
     "C",
     "A",
     "B",
     "P",
     "G",
     "D",
     "K",
     "E",
     "I",
     "Z",
     "Q",
     "R",
     "v",
     "x",
     "T",
     "F"
    ],
    "vincoli": [
     "ellisse di centro C, semiassi CA (maggiore) e CB; fuochi S, H con CS = CH",
     "P sull’ellisse, PG diametro per P (G opposto a P), DK diametro coniugato (parallelo alla tangente in P)",
     "PR tangente in P; Q punto dell’ellisse vicino a P; QR ∥ SP, R sulla tangente",
     "Qv ∥ tangente, v su PG, x su SP; QxPR parallelogramma",
     "E = SP ∩ DK; HI ∥ EC con I su SP; Z sulla tangente RP prolungata oltre P, così che gli angoli IPR e HPZ sono uguali (proprietà di riflessione)",
     "QT ⊥ SP; PF ⊥ DK",
     "limite Q → P"
    ]
   },
   "passi": [
    {
     "id": "L1-P11-p1",
     "la": "",
     "it": "Sia S il fuoco dell’ellisse.",
     "en": "Let S be the focus of the ellipsis.",
     "dipende_da": [],
     "figura": {
      "mostra": [
       "ellisse",
       "C",
       "S"
      ],
      "evidenzia": []
     }
    },
    {
     "id": "L1-P11-p2",
     "la": "",
     "it": "Si conduca SP, che tagli sia il diametro DK dell’ellisse in E sia l’ordinata Qv in x, e si completi il parallelogramma QxPR.",
     "en": "Draw SP cutting the diameter DK of the ellipsis in E, and the ordinate Qv in x; and complete the parallelogram QxPR.",
     "dipende_da": [],
     "figura": {
      "mostra": [
       "P",
       "tangente PR",
       "diametro DK",
       "SP",
       "E",
       "Q",
       "Qv",
       "x",
       "parallelogramma QxPR"
      ],
      "evidenzia": [
       "QxPR"
      ]
     }
    },
    {
     "id": "L1-P11-p3",
     "la": "",
     "it": "È evidente che EP è uguale al semiasse maggiore AC: infatti, condotta dall’altro fuoco H dell’ellisse la linea HI parallela a EC, poiché CS e CH sono uguali, sono uguali ES ed EI, così che EP è la semisomma di PS e PI, cioè (per le parallele HI, PR e gli angoli uguali IPR, HPZ) di PS e PH, che considerate congiuntamente uguagliano l’asse intero 2AC.",
     "en": "It is evident that EP is equal to the greater semi-axis AC: for drawing HI from the other focus H of the ellipsis parallel to EC, because CS, CH are equal, ES, EI will be also equal; so that EP is the half sum of PS, PI, that is (because of the parallels HI, PR, and the equal angles IPR, HPZ), of PS, PH, which taken together are equal to the whole axis 2AC.",
     "dipende_da": [],
     "figura": {
      "mostra": [
       "H",
       "HI ∥ EC",
       "I",
       "PH",
       "Z"
      ],
      "evidenzia": [
       "ES = EI",
       "EP = (PS + PH)/2 = AC"
      ]
     },
     "nota": "Nella trascrizione la frase è interrotta dal marcatore di pagina <55> e dalla figura [FIG 20]. «Considerate congiuntamente» (conjunctim) indica qui la somma PS + PH."
    },
    {
     "id": "L1-P11-p4",
     "la": "",
     "it": "Si abbassi su SP la perpendicolare QT e, detto L il lato retto principale dell’ellisse (ossia 2BC²/AC), L×QR starà a L×Pv come QR sta a Pv, cioè come PE, ossia AC, sta a PC; e L×Pv starà a GvP come L sta a Gv; e GvP starà a Qv² come PC² sta a CD²; e (per il Cor. 2 del Lemma VII), quando i punti Q e P vengono a coincidere, il rapporto di Qv² a Qx² è il rapporto di uguaglianza; e Qx², ossia Qv², sta a QT² come EP² sta a PF², cioè come CA² sta a PF², ovvero (per il Lemma XII) come CD² sta a CB².",
     "en": "Draw QT perpendicular to SP, and putting L for the principal latus rectum of the ellipsis [SVG 84], we shall have [SVG 85] to [SVG 86] as QR to Pv, that is, as PE or AC to PC; and [SVG 86] to GvP as L to Gv; and GvP to [SVG 67] as [SVG 68] to [SVG 69]; and by (Corol. 2, Lem. VII) the points Q and P coinciding, [SVG 67] is to [SVG 87] in the ratio of equality; and [SVG 87] or [SVG 67] is to [SVG 37] as [SVG 88] to [SVG 70], that is, as [SVG 89] to [SVG 70], or (by Lem. XII) as [SVG 69] to [SVG 90].",
     "dipende_da": [
      "Lemma VII, Cor. 2",
      "Lemma XII"
     ],
     "figura": {
      "mostra": [
       "QT",
       "G",
       "v",
       "F (piede della perpendicolare da P su DK)",
       "D"
      ],
      "evidenzia": [
       "QR : Pv = PE : PC",
       "GvP : Qv² = PC² : CD²",
       "Qx² : QT² = EP² : PF²"
      ]
     },
     "nota": "Formule della trascrizione lette: «2BC quad.AC» = 2BC²/AC; «GvP» = rettangolo Gv×vP. In Motte le formule sono le immagini SVG 84–90 (lette: 2BC²/AC, L×QR, L×Pv, Qv², PC², CD², Qx², EP², PF², CA², CB²), concordi con il latino."
    },
    {
     "id": "L1-P11-p5",
     "la": "",
     "it": "E, composti tutti questi rapporti, L×QR sta a QT² come AC×L×PC²×CD², ossia 2CB²×PC²×CD², sta a PC×Gv×CD²×CB², ovvero come 2PC sta a Gv.",
     "en": "And compounding all those ratios together, we shall have [SVG 85] to [SVG 37] as [SVG 91], or [SVG 92] to [SVG 93], or as 2PC to Gv.",
     "dipende_da": [],
     "figura": {
      "mostra": [],
      "evidenzia": [
       "L×QR : QT² = 2PC : Gv"
      ]
     },
     "nota": "La trascrizione ha «L×QR sit ad QT quad.»; nel passo parallelo della Prop. XII si legge «fit». Probabile refuso della trascrizione (sit per fit), da verificare sulla stampa; il senso non cambia. SVG 91–93 di Motte: AC×L×PC²×CD², 2CB²×PC²×CD², PC×Gv×CD²×CB²."
    },
    {
     "id": "L1-P11-p6",
     "la": "",
     "it": "Ma, quando i punti Q e P vengono a coincidere, 2PC e Gv sono uguali.",
     "en": "But the points Q and P coinciding, 2PC and Gv are equal.",
     "dipende_da": [],
     "figura": {
      "mostra": [
       "Q → P"
      ],
      "evidenzia": [
       "Gv → GP = 2PC"
      ]
     },
     "nota": "«coentibus» è refuso probabile della trascrizione per «coeuntibus»."
    },
    {
     "id": "L1-P11-p7",
     "la": "",
     "it": "Dunque sono uguali anche L×QR e QT², che sono a essi proporzionali.",
     "en": "And therefore the quantities [SVG 85] and [SVG 37], proportional to these, will be also equal.",
     "dipende_da": [],
     "figura": {
      "mostra": [],
      "evidenzia": [
       "L×QR = QT² (al limite)"
      ]
     }
    },
    {
     "id": "L1-P11-p8",
     "la": "",
     "it": "Si moltiplichino questi uguali per SP²/QR, e L×SP² risulterà uguale a SP²×QT²/QR.",
     "en": "Let those equals be drawn into [SVG 41], and [SVG 94] will become equal to [SVG 95].",
     "dipende_da": [],
     "figura": {
      "mostra": [],
      "evidenzia": [
       "L×SP² = SP²×QT²/QR"
      ]
     },
     "nota": "Trascrizione: «SPqQR» = SP²/QR; «SPq×QTqQR» = SP²×QT²/QR. Motte SVG 41, 94, 95: SP²/QR, L×SP², SP²×QT²/QR."
    },
    {
     "id": "L1-P11-p9",
     "la": "",
     "it": "Dunque (per i Cor. 1 e 5 della Prop. VI) la forza centripeta è inversamente come L×SP², cioè inversamente in rapporto duplicato della distanza SP. C.V.T.",
     "en": "And therefore (by Corol. 1 and 5, Prop. VI) the centripetal force is reciprocally as [SVG 94], that is, reciprocally in the duplicate ratio of the distance SP. Q.E.I.",
     "dipende_da": [
      "Prop. VI, Cor. 1",
      "Prop. VI, Cor. 5"
     ],
     "figura": {
      "mostra": [],
      "evidenzia": [
       "forza ∝ 1/SP²"
      ]
     },
     "nota": "Nella trascrizione «Q.E.I» è senza punto finale."
    },
    {
     "id": "L1-P11-p10",
     "la": "",
     "it": "*Lo stesso, altrimenti.* Poiché la forza diretta verso il centro dell’ellisse, per effetto della quale il corpo P può ruotare in quell’ellisse, è (per il Cor. 1 della Prop. X) come la distanza CP del corpo dal centro C dell’ellisse, si conduca CE parallela alla tangente PR dell’ellisse; e la forza per effetto della quale lo stesso corpo P può ruotare intorno a un qualsiasi altro punto S dell’ellisse, se CE e PS concorrono in E, sarà come PE³/SP² (per il Cor. 3 della Prop. VII); cioè, se il punto S è il fuoco dell’ellisse, e quindi PE è dato, come SP² inversamente. C.V.T.",
     "en": "Since the force tending to the centre of the ellipsis, by which the body P may revolve in that ellipsis, is (by Corol. 1, Prop. X.) as the distance CP of the body from the centre C of the ellipsis; let CE be drawn parallel to the tangent PR of the ellipsis; and the force by which the same body P may revolve about any other point S of the ellipsis, if CE and PS intersect in E, will be as [SVG 96] (by Cor. 3, Prop. VII.); that is, if the point S is the focus of the ellipsis, and therefore PE be given as [SVG 97] reciprocally. Q.E.I.",
     "dipende_da": [
      "Prop. X, Cor. 1",
      "Prop. VII, Cor. 3"
     ],
     "figura": {
      "mostra": [
       "CE ∥ PR",
       "E"
      ],
      "evidenzia": [
       "forza verso S ∝ PE³/SP², PE = AC costante"
      ]
     },
     "nota": "Seconda dimostrazione. Trascrizione «PE cub.SPq» = PE³/SP² (1726, p. 56). Motte 1846 (SVG 96) stampa PE²/SP²: refuso dell’edizione 1846 o della sua trascrizione Gutenberg; Motte 1729 ha PE³ (Fascicolo 3, F3). Nella pagina a fronte va corretto con nota."
    }
   ]
  },
  {
   "id": "L1-P12",
   "tipo": "Propositio/Problema",
   "titolo": "Prop. XII — iperbole: forza verso il fuoco",
   "copertura": [
    "S3.07",
    "S3.08",
    "S3.09",
    "S3.10",
    "S3.11",
    "S3.12"
   ],
   "fonti": {
    "la": "",
    "en": "Motte 1846, pp. 117–119"
   },
   "enunciato": {
    "la": "",
    "it": "Un corpo si muova in un’iperbole: si cerca la legge della forza centripeta diretta verso il fuoco della figura.",
    "en": "Suppose a body to move in an hyperbola; it is required to find the law of the centripetal force tending to the focus of that figure."
   },
   "figura_base": {
    "punti": [
     "S",
     "H",
     "C",
     "A",
     "B",
     "P",
     "G",
     "D",
     "K",
     "E",
     "I",
     "Z",
     "Q",
     "R",
     "v",
     "x",
     "T",
     "F"
    ],
    "vincoli": [
     "iperbole di centro C, semiassi CA (trasverso) e CB; fuochi S, H con CS = CH",
     "PG e KD diametri coniugati; PF ⊥ KD",
     "Qv ordinata al diametro GP (parallela alla tangente in P)",
     "QRPx parallelogramma: QR ∥ SP, R sulla tangente PR",
     "E = SP ∩ DK; HI ∥ EC",
     "QT ⊥ SP; limite Q → P"
    ]
   },
   "passi": [
    {
     "id": "L1-P12-p1",
     "la": "",
     "it": "Siano CA, CB i semiassi dell’iperbole; PG, KD altri diametri coniugati; PF la perpendicolare al diametro KD; e Qv l’ordinata al diametro GP.",
     "en": "Let CA, CB be the semi-axes of the hyperbola; PG, KD other conjugate diameters; PF a perpendicular to the diameter KD; and Qv an ordinate to the diameter GP.",
     "dipende_da": [],
     "figura": {
      "mostra": [
       "iperbole",
       "C",
       "A",
       "B",
       "P",
       "G",
       "K",
       "D",
       "F",
       "Q",
       "v"
      ],
      "evidenzia": []
     }
    },
    {
     "id": "L1-P12-p2",
     "la": "",
     "it": "Si conduca SP, che tagli sia il diametro DK in E sia l’ordinata Qv in x, e si completi il parallelogramma QRPx.",
     "en": "Draw SP cutting the diameter DK in E, and the ordinate Qv in x, and complete the parallelogram QRPx.",
     "dipende_da": [],
     "figura": {
      "mostra": [
       "S",
       "SP",
       "E",
       "x",
       "R",
       "QRPx"
      ],
      "evidenzia": []
     },
     "nota": "«secans cum diametrum DK in E, tum ordinatim applicatam»: «cum» è refuso probabile della trascrizione per «tum» (correlazione tum… tum), da verificare sulla stampa."
    },
    {
     "id": "L1-P12-p3",
     "la": "",
     "it": "È evidente che EP è uguale al semiasse trasverso AC: infatti, condotta dall’altro fuoco H dell’iperbole la linea HI parallela a EC, poiché CS e CH sono uguali, sono uguali ES ed EI; così che EP è la semidifferenza di PS e PI, cioè (per le parallele IH, PR e gli angoli uguali IPR, HPZ) di PS e PH, la cui differenza uguaglia l’asse intero 2AC.",
     "en": "It is evident that EP is equal to the semi-transverse axis AC; for drawing HI, from the other focus H of the hyperbola, parallel to EC, because CS, CH are equal, ES, EI will be also equal; so that EP is the half difference of PS, PI; that is (because of the parallels IH, PR, and the equal angles IPR, HPZ), of PS, PH, the difference of which is equal to the whole axis 2AC.",
     "dipende_da": [],
     "figura": {
      "mostra": [
       "H",
       "HI ∥ EC",
       "I",
       "PH"
      ],
      "evidenzia": [
       "EP = (PS − PH)/2 = AC"
      ]
     }
    },
    {
     "id": "L1-P12-p4",
     "la": "",
     "it": "Si abbassi su SP la perpendicolare QT.",
     "en": "Draw QT perpendicular to SP;",
     "dipende_da": [],
     "figura": {
      "mostra": [
       "QT"
      ],
      "evidenzia": []
     }
    },
    {
     "id": "L1-P12-p5",
     "la": "",
     "it": "E, detto L il lato retto principale dell’iperbole (ossia 2BC²/AC), L×QR starà a L×Pv come QR sta a Pv, ossia come Px sta a Pv, cioè (per i triangoli simili Pxv, PEC) come PE sta a PC, ossia come AC sta a PC.",
     "en": "and putting L for the principal latus rectum of the hyperbola (that is, for [SVG 98]), we shall have L × QR to L × Pv as QR to Pv, or Px to Pv, that is (because of the similar triangles Pxv, PEC), as PE to PC, or AC to PC.",
     "dipende_da": [],
     "figura": {
      "mostra": [
       "triangoli Pxv, PEC"
      ],
      "evidenzia": [
       "Pxv ~ PEC"
      ]
     },
     "nota": "Trascrizione «2BCqAC» = 2BC²/AC (Motte SVG 98)."
    },
    {
     "id": "L1-P12-p6",
     "la": "",
     "it": "Inoltre L×Pv starà a Gv×Pv come L sta a Gv; e (per la natura delle coniche) il rettangolo GvP starà a Qv² come PC² sta a CD²; e (per il Cor. 2 del Lemma VII), quando i punti Q e P vengono a coincidere, il rapporto di Qv² a Qx² diventa il rapporto di uguaglianza; e Qx², ossia Qv², sta a QT² come EP² sta a PF², cioè come CA² sta a PF², ovvero (per il Lemma XII) come CD² sta a CB²; e, composti tutti questi rapporti, L×QR sta a QT² come AC×L×PC²×CD², ossia 2CB²×PC²×CD², sta a PC×Gv×CD²×CB², ovvero come 2PC sta a Gv.",
     "en": "And L × Pv will be to Gv × Pv as L to Gv; and (by the properties of the conic sections) the rectangle GvP is to Qv2 as PC2 to CD2; and by (Cor. 2, Lem. VII.), Qv2 to Qx2, the points Q and P coinciding, becomes a ratio of equality; and Qx2 or Qv2 is to QT2 as EP2 to PF2, that is, as CA2 to PF2, or (by Lem. XII.) as CD2 to CB2: and, compounding all those ratios together, we shall have L × QR to QT2 as AC × L × PC2 × CD2, or 2CB2 × PC2 × CD2 to PC × Gv × CD2 × CB2, or as 2PC to Gv.",
     "dipende_da": [
      "Lemma VII, Cor. 2",
      "Lemma XII"
     ],
     "figura": {
      "mostra": [
       "G",
       "v",
       "F"
      ],
      "evidenzia": [
       "L×QR : QT² = 2PC : Gv"
      ]
     }
    },
    {
     "id": "L1-P12-p7",
     "la": "",
     "it": "Ma, quando i punti P e Q vengono a coincidere, 2PC e Gv sono uguali.",
     "en": "But the points P and Q coinciding, 2PC and Gv are equal.",
     "dipende_da": [],
     "figura": {
      "mostra": [
       "Q → P"
      ],
      "evidenzia": [
       "Gv → 2PC"
      ]
     },
     "nota": "Nella trascrizione la frase contiene il marcatore di pagina <57>."
    },
    {
     "id": "L1-P12-p8",
     "la": "",
     "it": "Dunque sono uguali anche L×QR e QT², che sono a essi proporzionali.",
     "en": "And therefore the quantities L × QR and QT2, proportional to them, will be also equal.",
     "dipende_da": [],
     "figura": {
      "mostra": [],
      "evidenzia": [
       "L×QR = QT²"
      ]
     }
    },
    {
     "id": "L1-P12-p9",
     "la": "",
     "it": "Si moltiplichino questi uguali per SP²/QR, e L×SP² risulterà uguale a SP²×QT²/QR.",
     "en": "Let those equals be drawn into [SVG 41], and we shall have L × SP2 equal to [SVG 99].",
     "dipende_da": [],
     "figura": {
      "mostra": [],
      "evidenzia": []
     },
     "nota": "Motte 1846, SVG 99, stampa SP²×QR/QT² (frazione capovolta): errore dell’edizione 1846 o della sua trascrizione; il latino ha SP²×QT²/QR, come nella Prop. XI (SVG 95). Motte 1729 non controllato."
    },
    {
     "id": "L1-P12-p10",
     "la": "",
     "it": "Dunque (per i Cor. 1 e 5 della Prop. VI) la forza centripeta è inversamente come L×SP², cioè inversamente in rapporto duplicato della distanza SP. C.V.T.",
     "en": "And therefore (by Cor. 1 and 5, Prop. VI.) the centripetal force is reciprocally as L × SP2, that is, reciprocally in the duplicate ratio of the distance SP. Q.E.I.",
     "dipende_da": [
      "Prop. VI, Cor. 1",
      "Prop. VI, Cor. 5"
     ],
     "figura": {
      "mostra": [],
      "evidenzia": [
       "forza ∝ 1/SP²"
      ]
     }
    },
    {
     "id": "L1-P12-p11",
     "la": "",
     "it": "*Lo stesso, altrimenti.* Si trovi la forza che tende dal centro C dell’iperbole.",
     "en": "Find out the force tending from the centre C of the hyperbola.",
     "dipende_da": [],
     "figura": {
      "mostra": [
       "C"
      ],
      "evidenzia": []
     },
     "nota": "Seconda dimostrazione. «Tende dal centro»: per l’iperbole la forza proporzionale alla distanza è diretta in fuori (Prop. X e suo scolio)."
    },
    {
     "id": "L1-P12-p12",
     "la": "",
     "it": "Questa risulterà proporzionale alla distanza CP.",
     "en": "This will be proportional to the distance CP.",
     "dipende_da": [],
     "figura": {
      "mostra": [
       "CP"
      ],
      "evidenzia": []
     }
    },
    {
     "id": "L1-P12-p13",
     "la": "",
     "it": "Di qui poi (per il Cor. 3 della Prop. VII) la forza diretta verso il fuoco S sarà come PE³/SP², cioè, poiché PE è dato, inversamente come SP². C.V.T.",
     "en": "But from thence (by Cor. 3, Prop. VII.) the force tending to the focus S will be as [SVG 100], that is, because PE is given reciprocally as SP2. Q.E.I.",
     "dipende_da": [
      "Prop. VII, Cor. 3"
     ],
     "figura": {
      "mostra": [
       "CE ∥ PR",
       "E"
      ],
      "evidenzia": [
       "forza verso S ∝ PE³/SP²"
      ]
     },
     "nota": "Qui Motte 1846 (SVG 100) ha correttamente PE³/SP². Trascrizione «PE cub.SPq» = PE³/SP²."
    },
    {
     "id": "L1-P12-p14",
     "la": "",
     "it": "Nello stesso modo si dimostra che il corpo, mutata questa forza centripeta in centrifuga, si muoverà nell’iperbole opposta.",
     "en": "And the same way may it be demonstrated, that the body having its centripetal changed into a centrifugal force, will move in the conjugate hyperbola.",
     "dipende_da": [],
     "figura": {
      "mostra": [
       "ramo opposto dell’iperbole"
      ],
      "evidenzia": []
     },
     "nota": "Motte traduce «hyperbola opposita» con «conjugate hyperbola»: è un errore di senso. L’iperbole opposta è l’altro ramo della stessa iperbole; l’iperbole coniugata è un’altra curva, con gli assi scambiati."
    }
   ]
  },
  {
   "id": "L1-Lem14",
   "tipo": "Lemma",
   "titolo": "Lemma XIV — perpendicolare dal fuoco sulla tangente della parabola",
   "copertura": [
    "S3.14",
    "S3.15"
   ],
   "fonti": {
    "la": "",
    "en": "Motte 1846, p. 119"
   },
   "enunciato": {
    "la": "",
    "it": "La perpendicolare abbassata dal fuoco di una parabola sulla sua tangente è media proporzionale fra le distanze del fuoco dal punto di contatto e dal vertice principale della figura.",
    "en": "The perpendicular, let fall from the focus of a parabola on its tangent, is a mean proportional between the distances of the focus from the point of contact, and from the principal vertex of the figure."
   },
   "figura_base": {
    "punti": [
     "A",
     "S",
     "P",
     "O",
     "M",
     "N"
    ],
    "vincoli": [
     "parabola di vertice principale A e fuoco S; asse (diametro principale) AS",
     "P sulla parabola; PO ordinata all’asse (O sull’asse)",
     "PM tangente in P, M sull’asse",
     "SN ⊥ PM, N sulla tangente"
    ]
   },
   "passi": [
    {
     "id": "L1-Lem14-p1",
     "la": "",
     "it": "Sia infatti AP la parabola, S il suo fuoco, A il vertice principale, P il punto di contatto, PO l’ordinata al diametro principale, PM la tangente, che incontra il diametro principale in M, e SN la linea perpendicolare dal fuoco sulla tangente.",
     "en": "For, let AP be the parabola, S its focus, A its principal vertex, P the point of contact, PO an ordinate to the principal diameter, PM the tangent meeting the principal diameter in M, and SN the perpendicular from the focus on the tangent:",
     "dipende_da": [],
     "figura": {
      "mostra": [
       "parabola",
       "A",
       "S",
       "P",
       "O",
       "M",
       "N",
       "PM",
       "SN"
      ],
      "evidenzia": []
     },
     "nota": "Nella trascrizione la frase contiene il segnaposto [FIG 22]."
    },
    {
     "id": "L1-Lem14-p2",
     "la": "",
     "it": "Si congiunga AN; e, poiché sono uguali MS e SP, MN e NP, MA e AO, le rette AN e OP saranno parallele; e di qui il triangolo SAN sarà rettangolo in A e simile ai triangoli uguali SNM, SNP: dunque PS sta a SN come SN sta a SA. C.V.D.",
     "en": "join AN, and because of the equal lines MS and SP, MN and NP, MA and AO, the right lines AN, OP, will be parallel; and thence the triangle SAN will be right-angled at A, and similar to the equal triangles SNM, SNP; therefore PS is to SN as SN to SA. Q.E.D.",
     "dipende_da": [],
     "figura": {
      "mostra": [
       "AN"
      ],
      "evidenzia": [
       "MS = SP",
       "AN ∥ OP",
       "SAN ~ SNM = SNP",
       "PS : SN = SN : SA"
      ]
     }
    }
   ]
  },
  {
   "id": "L1-P13",
   "tipo": "Propositio/Problema",
   "titolo": "Prop. XIII — parabola: forza verso il fuoco",
   "copertura": [
    "S3.19",
    "S3.20",
    "S3.21"
   ],
   "fonti": {
    "la": "",
    "en": "Motte 1846, pp. 119–120"
   },
   "enunciato": {
    "la": "",
    "it": "Un corpo si muova sul perimetro di una parabola: si cerca la legge della forza centripeta diretta verso il fuoco di questa figura.",
    "en": "If a body moves in the perimeter of a parabola; it is required to find the law of the centripetal force tending to the focus of that figure."
   },
   "figura_base": {
    "punti": [
     "A",
     "S",
     "P",
     "M",
     "N",
     "G",
     "Q",
     "R",
     "T",
     "v",
     "x"
    ],
    "vincoli": [
     "costruzione del Lemma XIV",
     "PG diametro per P (parallelo all’asse)",
     "Q sulla parabola vicino a P; QR ∥ SP con R sulla tangente; QT ⊥ SP",
     "Qv ∥ tangente, v su PG, x su SP",
     "limite Q → P"
    ]
   },
   "passi": [
    {
     "id": "L1-P13-p1",
     "la": "",
     "it": "Resti la costruzione del lemma, e sia P il corpo sul perimetro della parabola; e dal luogo Q, nel quale il corpo si porta subito dopo, conduci QR parallela a SP e QT perpendicolare a SP, e inoltre Qv parallela alla tangente, che incontri sia il diametro PG in v sia la distanza SP in x.",
     "en": "Retaining the construction of the preceding Lemma, let P be the body in the perimeter of the parabola; and from the place Q, into which it is next to succeed, draw QR parallel and QT perpendicular to SP, as also Qv parallel to the tangent, and meeting the diameter PG in v, and the distance SP in x.",
     "dipende_da": [],
     "figura": {
      "mostra": [
       "Q",
       "QR",
       "QT",
       "Qv",
       "v",
       "x",
       "PG"
      ],
      "evidenzia": []
     },
     "nota": "«occurentem» (forse grafia della stampa per «occurrentem»); la frase contiene il marcatore <59>. Motte aggiunge «preceding»."
    },
    {
     "id": "L1-P13-p2",
     "la": "",
     "it": "Ora, per i triangoli simili Pxv, SPM e per l’uguaglianza dei lati SM, SP dell’uno, sono uguali i lati Px, ossia QR, e Pv dell’altro.",
     "en": "Now, because of the similar triangles Pxv, SPM, and of the equal sides SP, SM of the one, the sides Px or QR and Pv of the other will be also equal.",
     "dipende_da": [],
     "figura": {
      "mostra": [
       "triangoli Pxv, SPM"
      ],
      "evidenzia": [
       "Px = QR = Pv"
      ]
     }
    },
    {
     "id": "L1-P13-p3",
     "la": "",
     "it": "Ma, per le coniche, il quadrato dell’ordinata Qv è uguale al rettangolo formato dal lato retto e dal segmento di diametro Pv, cioè (per il Lemma XIII) al rettangolo 4PS×Pv, ossia 4PS×QR; e, quando i punti P e Q vengono a coincidere, il rapporto di Qv a Qx (per il Cor. 2 del Lemma VII) diventa il rapporto di uguaglianza.",
     "en": "But (by the conic sections) the square of the ordinate Qv is equal to the rectangle under the latus rectum and the segment Pv of the diameter; that is (by Lem. XIII.), to the rectangle 4PS × Pv, or 4PS × QR; and the points P and Q coinciding, the ratio of Qv to Qx (by Cor. 2, Lem. VII.,) becomes a ratio of equality.",
     "dipende_da": [
      "Lemma XIII",
      "Lemma VII, Cor. 2"
     ],
     "figura": {
      "mostra": [],
      "evidenzia": [
       "Qv² = 4PS×Pv"
      ]
     }
    },
    {
     "id": "L1-P13-p4",
     "la": "",
     "it": "Dunque Qx², in quel caso, è uguale al rettangolo 4PS×QR.",
     "en": "And therefore Qx2, in this case, becomes equal to the rectangle 4PS × QR.",
     "dipende_da": [],
     "figura": {
      "mostra": [],
      "evidenzia": [
       "Qx² = 4PS×QR"
      ]
     },
     "nota": "Nella trascrizione la frase contiene il segnaposto [FIG 23]."
    },
    {
     "id": "L1-P13-p5",
     "la": "",
     "it": "Inoltre (per i triangoli simili QxT, SPN) Qx² sta a QT² come PS² sta a SN², cioè (per il Cor. 1 del Lemma XIV) come PS sta a SA, cioè come 4PS×QR sta a 4SA×QR; e di qui (per la Prop. IX del Libro V degli *Elementi*) QT² e 4SA×QR sono uguali.",
     "en": "But (because of the similar triangles QxT, SPN), Qx2 is to QT2 as PS2 to SN2, that is (by Cor. 1, Lem. XIV.), as PS to SA; that is, as 4PS × QR to 4SA × QR, and therefore (by Prop. IX. Lib. V., Elem.) QT2 and 4SA × QR are equal.",
     "dipende_da": [
      "Lemma XIV, Cor. 1",
      "Euclide, Elementi V, 9"
     ],
     "figura": {
      "mostra": [
       "triangoli QxT, SPN"
      ],
      "evidenzia": [
       "QT² = 4SA×QR"
      ]
     }
    },
    {
     "id": "L1-P13-p6",
     "la": "",
     "it": "Si moltiplichino questi uguali per SP²/QR, e SP²×QT²/QR risulterà uguale a SP²×4SA; e perciò (per i Cor. 1 e 5 della Prop. VI) la forza centripeta è inversamente come SP²×4SA, cioè, poiché 4SA è dato, inversamente in rapporto duplicato della distanza SP. C.V.T.",
     "en": "Multiply these equals by [SVG 41], and [SVG 95] will become equal to [SVG 101]: and therefore (by Cor. 1 and 5, Prop. VI.), the centripetal force is reciprocally as [SVG 101]; that is, because 4SA is given, reciprocally in the duplicate ratio of the distance SP. Q.E.I.",
     "dipende_da": [
      "Prop. VI, Cor. 1",
      "Prop. VI, Cor. 5"
     ],
     "figura": {
      "mostra": [],
      "evidenzia": [
       "forza ∝ 1/SP²"
      ]
     },
     "nota": "Motte SVG 95 e 101: SP²×QT²/QR, SP²×4SA; concordi con il latino."
    }
   ]
  },
  {
   "id": "L1-P14",
   "tipo": "Propositio/Theorema",
   "titolo": "Prop. XIV — il lato retto come quadrato della velocità areolare",
   "copertura": [
    "S3.24",
    "S3.25"
   ],
   "fonti": {
    "la": "",
    "en": "Motte 1846, p. 120"
   },
   "enunciato": {
    "la": "",
    "it": "Se più corpi ruotano intorno a un centro comune e la forza centripeta è inversamente in rapporto duplicato della distanza dei luoghi dal centro, dico che i lati retti principali delle orbite sono in rapporto duplicato delle aree che i corpi, con raggi condotti al centro, descrivono nello stesso tempo.",
    "en": "If several bodies revolve about one common centre, and the centripetal force is reciprocally in the duplicate ratio of the distance of places from the centre; I say, that the principal latera recta of their orbits are in the duplicate ratio of the areas, which the bodies by radii drawn to the centre describe in the same time."
   },
   "figura_base": {
    "punti": [
     "S",
     "P",
     "Q",
     "R",
     "T"
    ],
    "vincoli": [
     "orbita conica di fuoco S",
     "PR tangente in P; Q vicino a P; QR ∥ SP; QT ⊥ SP",
     "area SPQ descritta in un tempo dato; limite Q → P"
    ]
   },
   "passi": [
    {
     "id": "L1-P14-p1",
     "la": "",
     "it": "Infatti (per il Cor. 2 della Prop. XIII) il lato retto L è uguale alla quantità QT²/QR che si ha alla fine, quando i punti P e Q vengono a coincidere.",
     "en": "For (by Cor. 2, Prop. XIII) the latus rectum L is equal to the quantity [SVG 63] in its ultimate state when the points P and Q coincide.",
     "dipende_da": [
      "Prop. XIII, Cor. 2"
     ],
     "figura": {
      "mostra": [
       "S",
       "P",
       "Q",
       "R",
       "T"
      ],
      "evidenzia": [
       "L = QT²/QR (al limite)"
      ]
     },
     "nota": "Trascrizione «QTqQR» = QT²/QR (Motte SVG 63)."
    },
    {
     "id": "L1-P14-p2",
     "la": "",
     "it": "Ma la linea minima QR, in un tempo dato, è come la forza centripeta che la genera, cioè (per ipotesi) inversamente come SP².",
     "en": "But the lineola QR in a given time is as the generating centripetal force; that is (by supposition), reciprocally as SP2.",
     "dipende_da": [],
     "figura": {
      "mostra": [
       "QR"
      ],
      "evidenzia": [
       "QR ∝ 1/SP²"
      ]
     },
     "nota": "Motte rende «linea minima» con «lineola»."
    },
    {
     "id": "L1-P14-p3",
     "la": "",
     "it": "Dunque QT²/QR è come QT²×SP², cioè il lato retto L è in rapporto duplicato dell’area QT×SP. C.V.D.",
     "en": "And therefore [SVG 63] is as QT2 × SP2; that is, the latus rectum L is in the duplicate ratio of the area QT × SP. Q.E.D.",
     "dipende_da": [],
     "figura": {
      "mostra": [
       "area QT×SP"
      ],
      "evidenzia": [
       "L ∝ (QT×SP)²"
      ]
     }
    }
   ]
  },
  {
   "id": "L1-P16",
   "tipo": "Propositio/Theorema",
   "titolo": "Prop. XVI — velocità, perpendicolare sulla tangente e lato retto",
   "copertura": [
    "S3.30",
    "S3.31"
   ],
   "fonti": {
    "la": "",
    "en": "Motte 1846, pp. 121–123"
   },
   "enunciato": {
    "la": "",
    "it": "Poste le stesse cose, condotte ai corpi le linee rette che in quei punti tocchino le orbite, e abbassate dal fuoco comune le perpendicolari su queste tangenti, dico che le velocità dei corpi sono in rapporto composto dal rapporto delle perpendicolari inversamente e dal rapporto subduplicato dei lati retti principali direttamente.",
    "en": "The same things being supposed, and right lines being drawn to the bodies that shall touch the orbits, and perpendiculars being let fall on those tangents from the common focus; I say, that the velocities of the bodies are in a ratio compounded of the ratio of the perpendiculars inversely, and the subduplicate ratio of the principal latera recta directly."
   },
   "figura_base": {
    "punti": [
     "S",
     "P",
     "Q",
     "R",
     "T",
     "Y"
    ],
    "vincoli": [
     "orbita conica di fuoco S",
     "PR tangente in P; SY ⊥ PR con Y sulla tangente",
     "Q vicino a P; QT ⊥ SP; al limite PR : QT = SP : SY (triangoli simili)"
    ]
   },
   "passi": [
    {
     "id": "L1-P16-p1",
     "la": "",
     "it": "Dal fuoco S abbassa sulla tangente PR la perpendicolare SY, e la velocità del corpo P sarà inversamente in rapporto subduplicato della quantità SY²/L.",
     "en": "From the focus S draw SY perpendicular to the tangent PR, and the velocity of the body P will be reciprocally in the subduplicate ratio of the quantity [SVG 102].",
     "dipende_da": [],
     "figura": {
      "mostra": [
       "S",
       "P",
       "PR",
       "SY",
       "Y"
      ],
      "evidenzia": [
       "v ∝ √(L/SY²)"
      ]
     },
     "nota": "Trascrizione «SYq L» = SY²/L (Motte SVG 102); la frase contiene [FIG 25]."
    },
    {
     "id": "L1-P16-p2",
     "la": "",
     "it": "Quella velocità, infatti, è come l’arco piccolissimo PQ descritto in una particella di tempo data, cioè (per il Lemma VII) come la tangente PR, cioè, poiché PR sta a QT come SP sta a SY, come SP×QT/SY, ossia come SY inversamente e SP×QT direttamente; e SP×QT è come l’area descritta in un tempo dato, cioè (per la Prop. XIV) in rapporto subduplicato del lato retto. C.V.D.",
     "en": "For that velocity is as the infinitely small arc PQ described in a given moment of time, that is (by Lem. VII), as the tangent PR; that is (because of the proportionals PR to QT, and SP to SY), as [SVG 103]; or as SY reciprocally, and SP × QT directly; but SP × QT is as the area described in the given time, that is (by Prop. XIV), in the subduplicate ratio of the latus rectum. Q.E.D.",
     "dipende_da": [
      "Lemma VII",
      "Prop. XIV"
     ],
     "figura": {
      "mostra": [
       "Q",
       "QT",
       "arco PQ"
      ],
      "evidenzia": [
       "PR : QT = SP : SY",
       "v ∝ SP×QT/SY"
      ]
     },
     "nota": "Trascrizione «SP×QTSY» = SP×QT/SY (Motte SVG 103); «SP QT» = SP×QT. Motte aggiunge «infinitely» e rende «particula» con «moment»."
    }
   ]
  },
  {
   "id": "L1-P17",
   "tipo": "Propositio/Problema",
   "titolo": "Prop. XVII — orbita da luogo, velocità e direzione dati",
   "copertura": [
    "S3.41",
    "S3.42",
    "S3.43",
    "S3.44",
    "S3.45"
   ],
   "fonti": {
    "la": "",
    "en": "Motte 1846, pp. 123–124"
   },
   "enunciato": {
    "la": "",
    "it": "Posto che la forza centripeta sia inversamente proporzionale al quadrato della distanza dal centro, e che la quantità assoluta di quella forza sia nota, si cerca la linea che un corpo descrive partendo da un luogo dato con una velocità data lungo una retta data.",
    "en": "Supposing the centripetal force to be reciprocally proportional to the squares of the distances of places from the centre, and that the absolute quantity of that force is known; it is required to determine the line which a body will describe that is let go from a given place with a given velocity in the direction of a given right line."
   },
   "figura_base": {
    "punti": [
     "S",
     "P",
     "R",
     "Q",
     "H",
     "K",
     "p",
     "q",
     "r",
     "B",
     "C"
    ],
    "vincoli": [
     "S centro delle forze, fuoco comune",
     "orbita di confronto pq con tangente pr in p e velocità nota in p",
     "P luogo di partenza, PR direzione della velocità (tangente); PQ sezione conica cercata",
     "angolo RPH = complemento a due retti dell’angolo RPS (PH simmetrica di PS rispetto alla normale in P)",
     "SK ⊥ PH, K sulla retta PH; BC semiasse coniugato",
     "PH = L×SP/(2SP + 2KP − L)"
    ]
   },
   "passi": [
    {
     "id": "L1-P17-p1",
     "la": "",
     "it": "La forza centripeta diretta verso il punto S sia quella per effetto della quale un corpo p gira in un’orbita data qualsiasi pq, e se ne conosca la velocità nel luogo p.",
     "en": "Let the centripetal force tending to the point S be such as will make the body p revolve in any given orbit pq; and suppose the velocity of this body in the place p is known.",
     "dipende_da": [],
     "figura": {
      "mostra": [
       "S",
       "orbita pq",
       "p"
      ],
      "evidenzia": []
     }
    },
    {
     "id": "L1-P17-p2",
     "la": "",
     "it": "Dal luogo P, lungo la linea PR, parta il corpo P con una velocità data, e subito dopo, costretto dalla forza centripeta, si pieghi da quella linea nella sezione conica PQ.",
     "en": "Then from the place P suppose the body P to be let go with a given velocity in the direction of the line PR; but by virtue of a centripetal force to be immediately turned aside from that right line into the conic section PQ.",
     "dipende_da": [],
     "figura": {
      "mostra": [
       "P",
       "PR",
       "PQ"
      ],
      "evidenzia": []
     }
    },
    {
     "id": "L1-P17-p3",
     "la": "",
     "it": "La retta PR, dunque, toccherà questa sezione in P.",
     "en": "Thus, the right line PR will therefore touch in P.",
     "dipende_da": [],
     "figura": {
      "mostra": [],
      "evidenzia": [
       "PR tangente in P"
      ]
     },
     "nota": "Motte omette il complemento oggetto («hanc», la sezione conica)."
    },
    {
     "id": "L1-P17-p4",
     "la": "",
     "it": "Tocchi ugualmente una retta pr l’orbita pq in p; e, se si immagina di abbassare da S le perpendicolari su quelle tangenti, il lato retto principale della sezione conica starà al lato retto principale dell’orbita (per il Cor. 1 della Prop. XVI) in rapporto composto dal rapporto duplicato delle perpendicolari e dal rapporto duplicato delle velocità, e perciò è dato.",
     "en": "Suppose likewise that the right line pr touches the orbit pq in p; and if from S you suppose perpendiculars let fall on those tangents, the principal latus rectum of the conic section (by Cor. 1, Prop. XVI) will be to the principal latus rectum of that orbit in a ratio compounded of the duplicate ratio of the perpendiculars, and the duplicate ratio of the velocities; and is therefore given.",
     "dipende_da": [
      "Prop. XVI, Cor. 1"
     ],
     "figura": {
      "mostra": [
       "pr",
       "perpendicolari da S su PR e pr"
      ],
      "evidenzia": [
       "L : l = (perp.)² × (vel.)²"
      ]
     },
     "nota": "Nella trascrizione la frase contiene [FIG 26]."
    },
    {
     "id": "L1-P17-p5",
     "la": "",
     "it": "Sia L il lato retto della sezione conica.",
     "en": "Let this latus rectum be L;",
     "dipende_da": [],
     "figura": {
      "mostra": [],
      "evidenzia": []
     }
    },
    {
     "id": "L1-P17-p6",
     "la": "",
     "it": "È dato inoltre il fuoco S della stessa sezione conica.",
     "en": "the focus S of the conic section is also given.",
     "dipende_da": [],
     "figura": {
      "mostra": [],
      "evidenzia": []
     }
    },
    {
     "id": "L1-P17-p7",
     "la": "",
     "it": "Si faccia l’angolo RPH uguale al complemento a due retti dell’angolo RPS; e sarà data di posizione la linea PH, sulla quale si trova l’altro fuoco H.",
     "en": "Let the angle RPH be the complement of the angle RPS to two right; and the line PH, in which the other focus H is placed, is given by position.",
     "dipende_da": [],
     "figura": {
      "mostra": [
       "retta PH"
      ],
      "evidenzia": [
       "angolo RPH + angolo RPS = due retti"
      ]
     },
     "nota": "La parola «complementum» è spezzata dal marcatore di pagina <64> nella trascrizione. «Complemento a due retti» = supplemento."
    },
    {
     "id": "L1-P17-p8",
     "la": "",
     "it": "Abbassata su PH la perpendicolare SK, si immagini innalzato il semiasse coniugato BC; e sarà SP² − 2KP×PH + PH² = SH² = 4CH² = 4BH² − 4BC² = (SP + PH)² − L×(SP + PH) = SP² + 2SP×PH + PH² − L×(SP + PH).",
     "en": "Let fall SK perpendicular on PH, and erect the conjugate semi-axis BC; this done, we shall have [SVG 104].",
     "dipende_da": [],
     "figura": {
      "mostra": [
       "K",
       "SK",
       "B",
       "C (centro della conica)"
      ],
      "evidenzia": [
       "SH² con il teorema del coseno",
       "4BC² = L×(SP + PH)"
      ]
     },
     "nota": "Trascrizione: «2KPH» = 2KP×PH, «2SPH» = 2SP×PH; «SP+PH¯» è SP + PH sotto vincolo, reso con parentesi. Motte SVG 104 concorda."
    },
    {
     "id": "L1-P17-p9",
     "la": "",
     "it": "Si aggiunga da entrambe le parti 2KP×PH − SP² − PH² + L×(SP + PH), e si avrà L×(SP + PH) = 2SP×PH + 2KP×PH, ossia SP + PH sta a PH come 2SP + 2KP sta a L.",
     "en": "Add on both sides [SVG 105], and we shall have [SVG 106], or SP + PH to PH, as 2SP + 2KP to L.",
     "dipende_da": [],
     "figura": {
      "mostra": [],
      "evidenzia": [
       "(SP + PH) : PH = (2SP + 2KP) : L"
      ]
     },
     "nota": "Motte SVG 105–106 concordano."
    },
    {
     "id": "L1-P17-p10",
     "la": "",
     "it": "Di qui PH è data tanto in lunghezza quanto in posizione.",
     "en": "Whence PH is given both in length and position.",
     "dipende_da": [],
     "figura": {
      "mostra": [
       "H"
      ],
      "evidenzia": [
       "H determinato"
      ]
     }
    },
    {
     "id": "L1-P17-p11",
     "la": "",
     "it": "Precisamente: se la velocità del corpo in P è tale che il lato retto L sia minore di 2SP + 2KP, PH giacerà dalla stessa parte della tangente PR rispetto alla linea PS; e perciò la figura sarà un’ellisse, e sarà data a partire dai fuochi dati S, H e dall’asse principale SP + PH.",
     "en": "That is, if the velocity of the body in P is such that the latus rectum L is less than 2SP + 2KP, PH will lie on the same side of the tangent PR with the line SP; and therefore the figure will be an ellipsis, which from the given foci S, H, and the principal axis SP + PH, is given also.",
     "dipende_da": [],
     "figura": {
      "mostra": [
       "H dalla parte di S",
       "ellisse"
      ],
      "evidenzia": [
       "L < 2SP + 2KP"
      ]
     },
     "nota": "La trascrizione ha «axe principali SP+AH»: refuso probabile (della trascrizione o della stampa) per SP+PH, da verificare sulla stampa; Motte ha «SP + PH»."
    },
    {
     "id": "L1-P17-p12",
     "la": "",
     "it": "Se invece la velocità del corpo è tanto grande che il lato retto L sia uguale a 2SP + 2KP, la lunghezza PH sarà infinita; e perciò la figura sarà una parabola che ha l’asse SH parallelo alla linea PK, e di qui sarà data.",
     "en": "But if the velocity of the body is so great, that the latus rectum L becomes equal to 2SP + 2KP, the length PH will be infinite; and therefore, the figure will be a parabola, which has its axis SH parallel to the line PK, and is thence given.",
     "dipende_da": [],
     "figura": {
      "mostra": [
       "parabola",
       "asse ∥ PK"
      ],
      "evidenzia": [
       "L = 2SP + 2KP"
      ]
     }
    },
    {
     "id": "L1-P17-p13",
     "la": "",
     "it": "Se poi il corpo parte dal suo luogo P con una velocità ancora maggiore, la lunghezza PH andrà presa dall’altra parte della tangente; e perciò, passando la tangente fra i fuochi, la figura sarà un’iperbole che ha l’asse principale uguale alla differenza delle linee SP e PH, e di qui sarà data.",
     "en": "But if the body goes from its place P with a yet greater velocity, the length PH is to be taken on the other side the tangent; and so the tangent passing between the foci, the figure will be an hyperbola having its principal axis equal to the difference of the lines SP and PH, and thence is given.",
     "dipende_da": [],
     "figura": {
      "mostra": [
       "H dall’altra parte della tangente",
       "iperbole"
      ],
      "evidenzia": [
       "L > 2SP + 2KP"
      ]
     }
    },
    {
     "id": "L1-P17-p14",
     "la": "",
     "it": "Se infatti il corpo, in questi casi, ruota in una sezione conica così trovata, si è dimostrato nelle Propp. XI, XII e XIII che la forza centripeta sarà inversamente come il quadrato della distanza del corpo dal centro delle forze S; e perciò è rappresentata correttamente la linea PQ che il corpo, con una tale forza, descriverà partendo dal luogo dato P con la velocità data lungo la retta PR data di posizione. C.V.F.",
     "en": "For if the body, in these cases, revolves in a conic section so found, it is demonstrated in Prop. XI, XII, and XIII, that the centripetal force will be reciprocally as the square of the distance of the body from the centre of force S; and therefore we have rightly determined the line PQ, which a body let go from a given place P with a given velocity, and in the direction of the right line PR given by position, would describe with such a force. Q.E.F.",
     "dipende_da": [
      "Prop. XI",
      "Prop. XII",
      "Prop. XIII"
     ],
     "figura": {
      "mostra": [
       "PQ"
      ],
      "evidenzia": []
     }
    }
   ]
  },
  {
   "id": "L1-S3-Schol",
   "tipo": "Scholium",
   "titolo": "Scolio alla Sez. III — forza verso un punto qualsiasi R",
   "copertura": [
    "S3.50"
   ],
   "fonti": {
    "la": "",
    "en": "Motte 1846, p. 125"
   },
   "figura_base": {
    "punti": [
     "C",
     "R",
     "P",
     "G"
    ],
    "vincoli": [
     "sezione conica di centro C",
     "R punto dato qualsiasi (centro delle forze)",
     "PG tangente in P; CG ∥ RP, G sulla tangente"
    ]
   },
   "passi": [
    {
     "id": "L1-S3-Schol-p1",
     "la": "",
     "it": "Se un corpo P, per effetto di una forza centripeta diretta verso un punto dato qualsiasi R, si muove sul perimetro di una sezione conica data qualsiasi, il cui centro sia C, e si cerca la legge della forza centripeta: si conduca CG parallela al raggio RP, che incontri in G la tangente PG dell’orbita; e quella forza (per il Cor. 1 e lo Scolio della Prop. X e il Cor. 3 della Prop. VII) sarà come CG³/RP².",
     "en": "If a body P, by means of a centripetal force tending to any given point R, move in the perimeter of any given conic section whose centre is C; and the law of the centripetal force is required: draw CG parallel to the radius RP, and meeting the tangent PG of the orbit in G; and the force required (by Cor. 1, and Schol. Prop. X., and Cor. 3, Prop. VII.) will be as [SVG 107].",
     "dipende_da": [
      "Prop. X, Cor. 1",
      "Prop. X, Scolio",
      "Prop. VII, Cor. 3"
     ],
     "figura": {
      "mostra": [
       "conica",
       "C",
       "R",
       "P",
       "tangente PG",
       "CG ∥ RP",
       "G"
      ],
      "evidenzia": [
       "forza ∝ CG³/RP²"
      ]
     },
     "nota": "Trascrizione «CG cub.RP quad.» = CG³/RP². Motte 1846 (SVG 107) stampa CG²/RP²: errore dell’edizione 1846 o della sua trascrizione (la verifica numerica conferma CG³). Motte 1729 non controllato."
    }
   ]
  },
  {
   "id": "L1-Lem15",
   "tipo": "Lemma",
   "titolo": "Lemma XV — tangente e simmetrico del fuoco",
   "copertura": [
    "S4.01",
    "S4.02"
   ],
   "fonti": {
    "la": "",
    "en": "Motte 1846, p. 125"
   },
   "enunciato": {
    "la": "",
    "it": "Se dai due fuochi S, H di un’ellisse o di un’iperbole qualsiasi si conducono a un terzo punto qualsiasi V due rette SV, HV, delle quali una, HV, sia uguale all’asse principale della figura, cioè all’asse sul quale giacciono i fuochi, e l’altra, SV, sia divisa a metà in T dalla perpendicolare TR abbassata su di essa, quella perpendicolare TR toccherà in qualche punto la sezione conica; e viceversa, se la tocca, HV sarà uguale all’asse principale della figura.",
    "en": "If from the two foci S, H, of any ellipsis or hyperbola, we draw to any third point V the right lines SV, HV, whereof one HV is equal to the principal axis of the figure, that is, to the axis in which the foci are situated, the other, SV, is bisected in T by the perpendicular TR let fall upon it; that perpendicular TR will somewhere touch the conic section: and, vice versa, if it does touch it, HV will be equal to the principal axis of the figure."
   },
   "figura_base": {
    "punti": [
     "S",
     "H",
     "V",
     "T",
     "R"
    ],
    "vincoli": [
     "S, H fuochi di un’ellisse o di un’iperbole",
     "HV uguale all’asse principale",
     "TR perpendicolare a SV nel suo punto medio T",
     "R = TR ∩ retta HV (prolungata se occorre)"
    ]
   },
   "passi": [
    {
     "id": "L1-Lem15-p1",
     "la": "",
     "it": "Tagli infatti la perpendicolare TR la retta HV, prolungata se occorre, in R; e si congiunga SR.",
     "en": "For, let the perpendicular TR cut the right line HV, produced, if need be, in R; and join SR.",
     "dipende_da": [],
     "figura": {
      "mostra": [
       "S",
       "H",
       "V",
       "SV",
       "HV",
       "T",
       "TR",
       "R",
       "SR"
      ],
      "evidenzia": []
     }
    },
    {
     "id": "L1-Lem15-p2",
     "la": "",
     "it": "Poiché TS e TV sono uguali, saranno uguali anche le rette SR, VR e gli angoli TRS, TRV.",
     "en": "Because TS, TV are equal, therefore the right lines SR, VR, as well as the angles TRS, TRV, will be also equal.",
     "dipende_da": [],
     "figura": {
      "mostra": [],
      "evidenzia": [
       "SR = VR",
       "angolo TRS = angolo TRV"
      ]
     }
    },
    {
     "id": "L1-Lem15-p3",
     "la": "",
     "it": "Perciò il punto R sarà sulla sezione conica e la perpendicolare TR la toccherà; e viceversa. C.V.D.",
     "en": "Whence the point R will be in the conic section, and the perpendicular TR will touch the same; and the contrary. Q.E.D.",
     "dipende_da": [],
     "figura": {
      "mostra": [
       "conica"
      ],
      "evidenzia": [
       "SR + RH = HV = asse; TR biseca l’angolo SRV"
      ]
     }
    }
   ]
  },
  {
   "id": "L1-P18",
   "tipo": "Propositio/Problema",
   "titolo": "Prop. XVIII — ellisse o iperbole dati fuoco, asse, punti e tangenti",
   "copertura": [
    "S4.03",
    "S4.04",
    "S4.05"
   ],
   "fonti": {
    "la": "",
    "en": "Motte 1846, p. 126"
   },
   "enunciato": {
    "la": "",
    "it": "Dati il fuoco e gli assi principali, descrivere traiettorie ellittiche e iperboliche che passino per punti dati e tocchino rette date di posizione.",
    "en": "From a focus and the principal axes given, to describe elliptic and hyperbolic trajectories, which shall pass through given points, and touch right lines given by position."
   },
   "figura_base": {
    "punti": [
     "S",
     "P",
     "T",
     "R",
     "V",
     "H",
     "G",
     "F",
     "A",
     "B"
    ],
    "vincoli": [
     "S fuoco comune; AB lunghezza dell’asse principale",
     "P punto da attraversare; TR retta da toccare",
     "cerchio HG di centro P e raggio AB − SP (ellisse) o AB + SP (iperbole)",
     "ST ⊥ TR, TV = ST; cerchio FH di centro V e raggio AB",
     "H intersezione dei due cerchi"
    ]
   },
   "passi": [
    {
     "id": "L1-P18-p1",
     "la": "",
     "it": "Sia S il fuoco comune delle figure; AB la lunghezza dell’asse principale di una traiettoria qualsiasi; P un punto per il quale la traiettoria deve passare; e TR una retta che essa deve toccare.",
     "en": "Let S be the common focus of the figures; AB the length of the principal axis of any trajectory; P a point through which the trajectory should pass; and TR a right line which it should touch.",
     "dipende_da": [],
     "figura": {
      "mostra": [
       "S",
       "AB",
       "P",
       "TR"
      ],
      "evidenzia": []
     },
     "nota": "«figuraram» è refuso probabile della trascrizione per «figurarum»; la frase contiene [FIG 29]."
    },
    {
     "id": "L1-P18-p2",
     "la": "",
     "it": "Con centro P e raggio AB − SP, se l’orbita è un’ellisse, oppure AB + SP, se è un’iperbole, si descriva il cerchio HG.",
     "en": "About the centre P, with the interval AB - SP, if the orbit is an ellipsis, or AB + SP, if the orbit is an hyperbola, describe the circle HG.",
     "dipende_da": [],
     "figura": {
      "mostra": [
       "cerchio HG"
      ],
      "evidenzia": []
     }
    },
    {
     "id": "L1-P18-p3",
     "la": "",
     "it": "Sulla tangente TR si abbassi la perpendicolare ST, e la si prolunghi fino a V, in modo che TV sia uguale a ST; e con centro V e raggio AB si descriva il cerchio FH.",
     "en": "On the tangent TR let fall the perpendicular ST, and produce the same to V, so that TV may be equal to ST; and about V as a centre with the interval AB describe the circle FH.",
     "dipende_da": [],
     "figura": {
      "mostra": [
       "ST",
       "T",
       "V",
       "cerchio FH"
      ],
      "evidenzia": [
       "TV = ST"
      ]
     },
     "nota": "La frase contiene il marcatore di pagina <67> («centro <67> que»)."
    },
    {
     "id": "L1-P18-p4",
     "la": "",
     "it": "Con questo metodo, siano dati due punti P, p, o due tangenti TR, tr, o un punto P e una tangente TR, si devono descrivere due cerchi.",
     "en": "In this manner, whether two points P, p, are given, or two tangents TR, tr, or a point P and a tangent TR, we are to describe two circles.",
     "dipende_da": [],
     "figura": {
      "mostra": [],
      "evidenzia": []
     }
    },
    {
     "id": "L1-P18-p5",
     "la": "",
     "it": "Sia H la loro intersezione comune, e con i fuochi S, H e con l’asse dato si descriva la traiettoria.",
     "en": "Let H be their common intersection, and from the foci S, H, with the given axis describe the trajectory:",
     "dipende_da": [],
     "figura": {
      "mostra": [
       "H",
       "traiettoria"
      ],
      "evidenzia": []
     }
    },
    {
     "id": "L1-P18-p6",
     "la": "",
     "it": "Dico che è fatto.",
     "en": "I say, the thing is done.",
     "dipende_da": [],
     "figura": {
      "mostra": [],
      "evidenzia": []
     }
    },
    {
     "id": "L1-P18-p7",
     "la": "",
     "it": "La traiettoria descritta, infatti (poiché PH + SP nell’ellisse e PH − SP nell’iperbole è uguale all’asse), passerà per il punto P e (per il lemma precedente) toccherà la retta TR.",
     "en": "For (because PH + SP in the ellipsis, and PH - SP in the hyperbola, is equal to the axis) the described trajectory will pass through the point P, and (by the preceding Lemma) will touch the right line TR.",
     "dipende_da": [
      "Lemma XV"
     ],
     "figura": {
      "mostra": [
       "PH"
      ],
      "evidenzia": [
       "PH ± SP = AB",
       "HV = AB"
      ]
     }
    },
    {
     "id": "L1-P18-p8",
     "la": "",
     "it": "E con lo stesso argomento o passerà per i due punti P, p, o toccherà le due rette TR, tr. C.V.F.",
     "en": "And by the same argument it will either pass through the two points P, p, or touch the two right lines TR, tr. Q.E.F.",
     "dipende_da": [],
     "figura": {
      "mostra": [],
      "evidenzia": []
     }
    }
   ]
  },
  {
   "id": "L1-P19",
   "tipo": "Propositio/Problema",
   "titolo": "Prop. XIX — parabola dati fuoco, punti e tangenti",
   "copertura": [
    "S4.06",
    "S4.07",
    "S4.08"
   ],
   "fonti": {
    "la": "",
    "en": "Motte 1846, p. 126"
   },
   "enunciato": {
    "la": "",
    "it": "Intorno a un fuoco dato descrivere una traiettoria parabolica che passi per punti dati e tocchi rette date di posizione.",
    "en": "About a given focus, to describe a parabolic trajectory, which shall pass through given points, and touch right lines given by position."
   },
   "figura_base": {
    "punti": [
     "S",
     "P",
     "T",
     "R",
     "V",
     "F",
     "G",
     "I",
     "K",
     "p",
     "v"
    ],
    "vincoli": [
     "S fuoco; P punto della traiettoria; TR tangente",
     "cerchio FG di centro P e raggio PS",
     "ST ⊥ TR, TV = ST",
     "IF retta (direttrice) tangente al cerchio FG e passante per V",
     "SI ⊥ FI; K punto medio di SI (vertice); asse SK"
    ]
   },
   "passi": [
    {
     "id": "L1-P19-p1",
     "la": "",
     "it": "Sia S il fuoco, P un punto e TR una tangente della traiettoria da descrivere.",
     "en": "Let S be the focus, P a point, and TR a tangent of the trajectory to be described.",
     "dipende_da": [],
     "figura": {
      "mostra": [
       "S",
       "P",
       "TR"
      ],
      "evidenzia": []
     }
    },
    {
     "id": "L1-P19-p2",
     "la": "",
     "it": "Con centro P e raggio PS descrivi il cerchio FG.",
     "en": "About P as a centre, with the interval PS, describe the circle FG.",
     "dipende_da": [],
     "figura": {
      "mostra": [
       "cerchio FG"
      ],
      "evidenzia": []
     }
    },
    {
     "id": "L1-P19-p3",
     "la": "",
     "it": "Dal fuoco abbassa sulla tangente la perpendicolare ST, e prolungala fino a V, in modo che TV sia uguale a ST.",
     "en": "From the focus let fall ST perpendicular on the tangent, and produce the same to V, so as TV may be equal to ST.",
     "dipende_da": [],
     "figura": {
      "mostra": [
       "ST",
       "T",
       "V"
      ],
      "evidenzia": [
       "TV = ST"
      ]
     },
     "nota": "La trascrizione ha «ut fit TV æqualis ST»: «fit» per «sit», refuso probabile della trascrizione; il senso non cambia."
    },
    {
     "id": "L1-P19-p4",
     "la": "",
     "it": "Allo stesso modo si deve descrivere un secondo cerchio fg, se è dato un secondo punto p; oppure si deve trovare un secondo punto v, se è data una seconda tangente tr; poi si deve condurre la retta IF, che tocchi i due cerchi FG, fg, se sono dati due punti P, p, oppure passi per i due punti V, v, se sono date due tangenti TR, tr, oppure tocchi il cerchio FG e passi per il punto V, se sono dati il punto P e la tangente TR.",
     "en": "After the same manner another circle fg is to be described, if another point p is given; or another point v is to be found, if another tangent tr is given; then draw the right line IF, which shall touch the two circles FG, fg, if two points P, p are given; or pass through the two points V, v, if two tangents TR, tr, are given: or touch the circle FG, and pass through the point V, if the point P and the tangent TR are given.",
     "dipende_da": [],
     "figura": {
      "mostra": [
       "retta IF",
       "F"
      ],
      "evidenzia": [
       "IF tangente a FG e passante per V"
      ]
     },
     "nota": "Nella trascrizione la frase contiene [FIG 30]."
    },
    {
     "id": "L1-P19-p5",
     "la": "",
     "it": "Su FI abbassa la perpendicolare SI e dividila a metà in K; e con asse SK e vertice principale K si descriva una parabola.",
     "en": "On FI let fall the perpendicular SI, and bisect the same in K; and with the axis SK and principal vertex K describe a parabola:",
     "dipende_da": [],
     "figura": {
      "mostra": [
       "SI",
       "I",
       "K",
       "parabola"
      ],
      "evidenzia": [
       "SK = KI"
      ]
     }
    },
    {
     "id": "L1-P19-p6",
     "la": "",
     "it": "Dico che è fatto.",
     "en": "I say the thing is done.",
     "dipende_da": [],
     "figura": {
      "mostra": [],
      "evidenzia": []
     }
    },
    {
     "id": "L1-P19-p7",
     "la": "",
     "it": "La parabola, infatti, poiché sono uguali SK e IK, SP e FP, passerà per il punto P; e (per il Cor. 3 del Lemma XIV), poiché sono uguali ST e TV e l’angolo STR è retto, toccherà la retta TR. C.V.F.",
     "en": "For this parabola (because SK is equal to IK, and SP to FP) will pass through the point P; and (by Cor. 3, Lem. XIV) because ST is equal to TV, and STR a right angle, it will touch the right line TR. Q.E.F.",
     "dipende_da": [
      "Lemma XIV, Cor. 3"
     ],
     "figura": {
      "mostra": [],
      "evidenzia": [
       "SP = FP = distanza di P dalla direttrice",
       "T sulla tangente al vertice"
      ]
     }
    }
   ]
  },
  {
   "id": "L1-P20",
   "tipo": "Propositio/Problema",
   "titolo": "Prop. XX — traiettoria data di forma intorno a un fuoco dato (Casi 1–4)",
   "copertura": [
    "S4.09",
    "S4.10",
    "S4.11",
    "S4.12",
    "S4.13",
    "S4.14",
    "S4.15",
    "S4.16",
    "S4.17"
   ],
   "fonti": {
    "la": "",
    "en": "Motte 1846, pp. 127–129"
   },
   "enunciato": {
    "la": "",
    "it": "Intorno a un fuoco dato descrivere una traiettoria qualsiasi data di forma, che passi per punti dati e tocchi rette date di posizione.",
    "en": "About a given focus to describe any trajectory given in specie which shall pass through given points, and touch right lines given by position."
   },
   "figura_base": {
    "punti": [
     "S",
     "H",
     "A",
     "a",
     "B",
     "C",
     "K",
     "L",
     "G",
     "T",
     "t",
     "R",
     "V",
     "v",
     "O",
     "k",
     "X",
     "P",
     "s",
     "h",
     "p",
     "q"
    ],
    "vincoli": [
     "Caso 1: KB : BS = LC : CS = asse : distanza dei fuochi; KL tangente comune ai cerchi (B, BK) e (C, CL); SG ⊥ KL; GA : AS = Ga : aS = KB : BS",
     "Caso 2: V, v simmetrici di S rispetto alle tangenti TR, tr; O punto medio di Vv; OH ⊥ Vv; K, k dividono VS internamente ed esternamente nel rapporto dato; cerchio di diametro Kk; X centro",
     "Caso 3: come il 2, con H = VR ∩ cerchio di diametro Kk",
     "Caso 4: figura simile apb con fuochi s, h; triangoli hsq ~ VSP; cerchio di centro q; SH : sh = SP : sp"
    ]
   },
   "passi": [
    {
     "id": "L1-P20-p1",
     "la": "",
     "it": "Caso 1. Dato il fuoco S, si debba descrivere la traiettoria ABC per due punti B, C.",
     "en": "About the focus S it is required to describe a trajectory ABC, passing through two points B, C.",
     "dipende_da": [],
     "figura": {
      "mostra": [
       "S",
       "B",
       "C"
      ],
      "evidenzia": []
     }
    },
    {
     "id": "L1-P20-p2",
     "la": "",
     "it": "Poiché la traiettoria è data di forma, sarà dato il rapporto dell’asse principale alla distanza dei fuochi.",
     "en": "Because the trajectory is given in specie, the ratio of the principal axis to the distance of the foci will be given.",
     "dipende_da": [],
     "figura": {
      "mostra": [],
      "evidenzia": []
     }
    },
    {
     "id": "L1-P20-p3",
     "la": "",
     "it": "In quel rapporto prendi KB a BS e LC a CS.",
     "en": "In that ratio take KB to BS, and LC to CS.",
     "dipende_da": [],
     "figura": {
      "mostra": [
       "K",
       "L"
      ],
      "evidenzia": [
       "KB : BS = LC : CS"
      ]
     },
     "nota": "Nella trascrizione la frase è preceduta da [FIG 31]."
    },
    {
     "id": "L1-P20-p4",
     "la": "",
     "it": "Con centri B, C e raggi BK, CL descrivi due cerchi; sulla retta KL, che li tocchi in K e L, abbassa la perpendicolare SG, e tagliala in A e a, in modo che GA stia ad AS e Ga ad aS come KB sta a BS; e con asse Aa e vertici A, a si descriva la traiettoria.",
     "en": "About the centres B, C, with the intervals BK, CL, describe two circles; and on the right line KL, that touches the same in K and L, let fall the perpendicular SG; which cut in A and a, so that GA may be to AS, and Ga to aS, as KB to BS; and with the axis Aa, and vertices A, a, describe a trajectory:",
     "dipende_da": [],
     "figura": {
      "mostra": [
       "cerchi (B, BK), (C, CL)",
       "KL",
       "SG",
       "A",
       "a",
       "traiettoria"
      ],
      "evidenzia": [
       "GA : AS = Ga : aS = KB : BS"
      ]
     }
    },
    {
     "id": "L1-P20-p5",
     "la": "",
     "it": "Dico che è fatto.",
     "en": "I say the thing is done.",
     "dipende_da": [],
     "figura": {
      "mostra": [],
      "evidenzia": []
     }
    },
    {
     "id": "L1-P20-p6",
     "la": "",
     "it": "Sia infatti H l’altro fuoco della figura descritta; e, poiché GA sta ad AS come Ga sta ad aS, separando, Ga − GA, ossia Aa, starà ad aS − AS, ossia SH, nello stesso rapporto, e quindi nel rapporto che l’asse principale della figura da descrivere ha alla distanza dei suoi fuochi; e perciò la figura descritta è della stessa forma di quella da descrivere.",
     "en": "For let H be the other focus of the described figure, and seeing GA is to AS as Ga to aS, then by division we shall have Ga - GA, or Aa to aS - AS, or SH in the same ratio, and therefore in the ratio which the principal axis of the figure to be described has to the distance of its foci; and therefore the described figure is of the same species with the figure which was to be described.",
     "dipende_da": [],
     "figura": {
      "mostra": [
       "H"
      ],
      "evidenzia": [
       "Aa : SH = KB : BS"
      ]
     }
    },
    {
     "id": "L1-P20-p7",
     "la": "",
     "it": "E, poiché KB sta a BS e LC sta a CS nello stesso rapporto, questa figura passerà per i punti B, C, come è manifesto dalle coniche.",
     "en": "And since KB to BS, and LC to CS, are in the same ratio, this figure will pass through the points B, C, as is manifest from the conic sections.",
     "dipende_da": [],
     "figura": {
      "mostra": [],
      "evidenzia": [
       "KL direttrice"
      ]
     }
    },
    {
     "id": "L1-P20-p8",
     "la": "",
     "it": "Caso 2. Dato il fuoco S, si debba descrivere una traiettoria che tocchi in qualche punto due rette TR, tr.",
     "en": "About the focus S it is required to describe a trajectory which shall somewhere touch two right lines TR, tr.",
     "dipende_da": [],
     "figura": {
      "mostra": [
       "S",
       "TR",
       "tr"
      ],
      "evidenzia": []
     }
    },
    {
     "id": "L1-P20-p9",
     "la": "",
     "it": "Dal fuoco abbassa sulle tangenti le perpendicolari ST, St e prolungale fino a V, v, in modo che TV, tv siano uguali a TS, tS.",
     "en": "From the focus on those tangents let fall the perpendiculars ST, St, which produce to V, v, so that TV, tv may be equal to TS, tS.",
     "dipende_da": [],
     "figura": {
      "mostra": [
       "T",
       "t",
       "V",
       "v"
      ],
      "evidenzia": [
       "TV = TS",
       "tv = tS"
      ]
     },
     "nota": "Nella trascrizione la frase contiene [FIG 32]."
    },
    {
     "id": "L1-P20-p10",
     "la": "",
     "it": "Dividi a metà Vv in O, e innalza la perpendicolare illimitata OH, e taglia la retta VS, prolungata all’infinito, in K e k, in modo che VK stia a KS e Vk a kS come l’asse principale della traiettoria da descrivere sta alla distanza dei fuochi.",
     "en": "Bisect Vv in O, and erect the indefinite perpendicular OH, and cut the right line VS infinitely produced in K and k, so that VK be to KS, and Vk to kS, as the principal axis of the trajectory to be described is to the distance of its foci.",
     "dipende_da": [],
     "figura": {
      "mostra": [
       "O",
       "retta OH",
       "K",
       "k"
      ],
      "evidenzia": [
       "VK : KS = Vk : kS = asse : distanza dei fuochi"
      ]
     }
    },
    {
     "id": "L1-P20-p11",
     "la": "",
     "it": "Sul diametro Kk si descriva un cerchio che tagli OH in H; e con i fuochi S, H e con asse principale uguale a VH si descriva la traiettoria.",
     "en": "On the diameter Kk describe a circle cutting OH in H; and with the foci S, H, and principal axis equal to VH, describe a trajectory:",
     "dipende_da": [],
     "figura": {
      "mostra": [
       "cerchio di diametro Kk",
       "H",
       "traiettoria"
      ],
      "evidenzia": []
     }
    },
    {
     "id": "L1-P20-p12",
     "la": "",
     "it": "Dico che è fatto.",
     "en": "I say, the thing is done.",
     "dipende_da": [],
     "figura": {
      "mostra": [],
      "evidenzia": []
     }
    },
    {
     "id": "L1-P20-p13",
     "la": "",
     "it": "Dividi infatti a metà Kk in X, e congiungi HX, HS, HV, Hv.",
     "en": "For bisecting Kk in X, and joining HX, HS, HV, Hv,",
     "dipende_da": [],
     "figura": {
      "mostra": [
       "X",
       "HX",
       "HS",
       "HV",
       "Hv"
      ],
      "evidenzia": []
     },
     "nota": "Nella trascrizione la frase contiene il marcatore di pagina <69>. In Motte la frase prosegue senza punto."
    },
    {
     "id": "L1-P20-p14",
     "la": "",
     "it": "Poiché VK sta a KS come Vk sta a kS, e, componendo, come VK + Vk sta a KS + kS, e, separando, come Vk − VK sta a kS − KS, cioè come 2VX sta a 2KX e 2KX sta a 2SX, e quindi come VX sta a HX e HX sta a SX, saranno simili i triangoli VXH, HXS; e perciò VH starà a SH come VX sta a XH, e quindi come VK sta a KS.",
     "en": "because VK is to KS as Vk to kS; and by composition, as VK + Vk to KS + kS; and by division, as Vk - VK to kS - KS, that is, as 2VX to 2KX, and 2KX to 2SX, and therefore as VX to HX and HX to SX, the triangles VXH, HXS will be similar; therefore VH will be to SH as VX to XH; and therefore as VK to KS.",
     "dipende_da": [],
     "figura": {
      "mostra": [
       "triangoli VXH, HXS"
      ],
      "evidenzia": [
       "VX : HX = HX : SX",
       "VH : SH = VK : KS"
      ]
     }
    },
    {
     "id": "L1-P20-p15",
     "la": "",
     "it": "L’asse principale VH della traiettoria descritta ha dunque alla distanza dei suoi fuochi SH lo stesso rapporto che l’asse principale della traiettoria da descrivere ha alla distanza dei suoi fuochi; e perciò è della stessa forma.",
     "en": "Wherefore VH, the principal axis of the described trajectory, has the same ratio to SH, the distance of the foci, as the principal axis of the trajectory which was to be described has to the distance of its foci; and is therefore of the same species.",
     "dipende_da": [],
     "figura": {
      "mostra": [],
      "evidenzia": []
     }
    },
    {
     "id": "L1-P20-p16",
     "la": "",
     "it": "Inoltre, poiché VH e vH sono uguali all’asse principale, e VS, vS sono divisi a metà perpendicolarmente dalle rette TR, tr, è chiaro (per il Lemma XV) che quelle rette toccano la traiettoria descritta. C.V.F.",
     "en": "And seeing VH, vH are equal to the principal axis, and VS, vS are perpendicularly bisected by the right lines TR, tr, it is evident (by Lem. XV) that those right lines touch the described trajectory. Q.E.F.",
     "dipende_da": [
      "Lemma XV"
     ],
     "figura": {
      "mostra": [],
      "evidenzia": [
       "VH = vH (H su OH)"
      ]
     }
    },
    {
     "id": "L1-P20-p17",
     "la": "",
     "it": "Caso 3. Dato il fuoco S, si debba descrivere una traiettoria che tocchi la retta TR nel punto dato R.",
     "en": "About the focus S it is required to describe a trajectory, which shall touch a right line TR in a given Point R.",
     "dipende_da": [],
     "figura": {
      "mostra": [
       "S",
       "TR",
       "R"
      ],
      "evidenzia": []
     }
    },
    {
     "id": "L1-P20-p18",
     "la": "",
     "it": "Sulla retta TR abbassa la perpendicolare ST, e prolungala fino a V, in modo che TV sia uguale a ST.",
     "en": "On the right line TR let fall the perpendicular ST, which produce to V, so that TV may be equal to ST;",
     "dipende_da": [],
     "figura": {
      "mostra": [
       "T",
       "V"
      ],
      "evidenzia": [
       "TV = ST"
      ]
     }
    },
    {
     "id": "L1-P20-p19",
     "la": "",
     "it": "Congiungi VR, e taglia la retta VS, prolungata all’infinito, in K e k, in modo che VK stia a SK e Vk a Sk come l’asse principale dell’ellisse da descrivere sta alla distanza dei fuochi; e, descritto un cerchio sul diametro Kk, si tagli in H la retta VR prolungata; e con i fuochi S, H e con asse principale uguale alla retta VH si descriva la traiettoria.",
     "en": "join VR, and cut the right line VS indefinitely produced in K and k, so that VK may be to SK, and Vk to Sk, as the principal axis of the ellipsis to be described to the distance of its foci; and on the diameter Kk describing a circle, cut the right line VR produced in H; then with the foci S, H, and principal axis equal to VH, describe a trajectory:",
     "dipende_da": [],
     "figura": {
      "mostra": [
       "VR",
       "K",
       "k",
       "cerchio di diametro Kk",
       "H"
      ],
      "evidenzia": []
     },
     "nota": "Il testo dice «ellisse» (ellipseos) anche se il caso vale per ogni conica data di forma; Motte fa lo stesso. Nella trascrizione la frase contiene [FIG 33]."
    },
    {
     "id": "L1-P20-p20",
     "la": "",
     "it": "Dico che è fatto.",
     "en": "I say, the thing is done.",
     "dipende_da": [],
     "figura": {
      "mostra": [],
      "evidenzia": []
     }
    },
    {
     "id": "L1-P20-p21",
     "la": "",
     "it": "Che VH stia a SH come VK sta a SK, e quindi come l’asse principale della traiettoria da descrivere sta alla distanza dei suoi fuochi, risulta infatti da quanto si è dimostrato nel secondo caso; e perciò la traiettoria descritta è della stessa forma di quella da descrivere; e che la retta TR, dalla quale è diviso a metà l’angolo VRS, tocchi la traiettoria nel punto R, risulta dalle coniche. C.V.F.",
     "en": "For VH is to SH as VK to SK, and therefore as the principal axis of the trajectory which was to be described to the distance of its foci (as appears from what we have demonstrated in Case 2); and therefore the described trajectory is of the same species with that which was to be described; but that the right line TR, by which the angle VRS is bisected, touches the trajectory in the point R, is certain from the properties of the conic sections. Q.E.F.",
     "dipende_da": [],
     "figura": {
      "mostra": [],
      "evidenzia": [
       "TR bisettrice dell’angolo VRS"
      ]
     }
    },
    {
     "id": "L1-P20-p22",
     "la": "",
     "it": "Caso 4. Intorno al fuoco S si debba ora descrivere una traiettoria APB che tocchi la retta TR e passi per un punto qualsiasi P dato fuori della tangente, e che sia simile alla figura apb descritta con asse principale ab e fuochi s, h.",
     "en": "About the focus S it is required to describe a trajectory APB that shall touch a right line TR, and pass through any given point P without the tangent, and shall be similar to the figure apb, described with the principal axis ab, and foci s, h.",
     "dipende_da": [],
     "figura": {
      "mostra": [
       "S",
       "TR",
       "P",
       "figura apb",
       "s",
       "h"
      ],
      "evidenzia": []
     }
    },
    {
     "id": "L1-P20-p23",
     "la": "",
     "it": "Sulla tangente TR abbassa la perpendicolare ST, e prolungala fino a V, in modo che TV sia uguale a ST.",
     "en": "On the tangent TR let fall the perpendicular ST, which produce to V, so that TV may be equal to ST;",
     "dipende_da": [],
     "figura": {
      "mostra": [
       "T",
       "V"
      ],
      "evidenzia": [
       "TV = ST"
      ]
     },
     "nota": "Motte 1846 premette a questa frase una seconda didascalia di figura, che ripete la frase stessa."
    },
    {
     "id": "L1-P20-p24",
     "la": "",
     "it": "Agli angoli VSP, SVP fa’ uguali gli angoli hsq, shq; e con centro q e con un raggio che stia ad ab come SP sta a VS descrivi un cerchio che tagli la figura apb in p.",
     "en": "and making the angles hsq, shq, equal to the angles VSP, SVP, about q as a centre, and with an interval which shall be to ab as SP to VS, describe a circle cutting the figure apb in p:",
     "dipende_da": [],
     "figura": {
      "mostra": [
       "q",
       "triangolo hsq",
       "cerchio di centro q",
       "p"
      ],
      "evidenzia": [
       "hsq ~ VSP"
      ]
     }
    },
    {
     "id": "L1-P20-p25",
     "la": "",
     "it": "Congiungi sp e conduci SH che stia a sh come SP sta a sp, e che formi l’angolo PSH uguale all’angolo psh e l’angolo VSH uguale all’angolo psq.",
     "en": "join sp, and draw SH such that it may be to sh as SP is to sp, and may make the angle PSH equal to the angle psh, and the angle VSH equal to the angle psq.",
     "dipende_da": [],
     "figura": {
      "mostra": [
       "sp",
       "SH",
       "H"
      ],
      "evidenzia": [
       "PSH ~ psh"
      ]
     },
     "nota": "Nella trascrizione la frase contiene il marcatore di pagina <70>."
    },
    {
     "id": "L1-P20-p26",
     "la": "",
     "it": "Infine, con i fuochi S, H e con asse principale AB uguale alla distanza VH, si descriva una sezione conica.",
     "en": "Then with the foci S, H, and principal axis AB, equal to the distance VH, describe a conic section:",
     "dipende_da": [],
     "figura": {
      "mostra": [
       "conica APB"
      ],
      "evidenzia": [
       "AB = VH"
      ]
     }
    },
    {
     "id": "L1-P20-p27",
     "la": "",
     "it": "Dico che è fatto.",
     "en": "I say, the thing is done;",
     "dipende_da": [],
     "figura": {
      "mostra": [],
      "evidenzia": []
     }
    },
    {
     "id": "L1-P20-p28",
     "la": "",
     "it": "Se infatti si conduce sv che stia a sp come sh sta a sq, e che formi l’angolo vsp uguale all’angolo hsq e l’angolo vsh uguale all’angolo psq, i triangoli svh, spq saranno simili, e perciò vh starà a pq come sh sta a sq, cioè (per i triangoli simili VSP, hsq) come VS sta a SP, ossia come ab sta a pq.",
     "en": "for if sv is drawn so that it shall be to sp as sh is to sq, and shall make the angle vsp equal to the angle hsq, and the angle vsh equal to the angle psq, the triangles svh, spq, will be similar, and therefore vh will be to pq as sh is to sq; that is (because of the similar triangles VSP, hsq), as VS is to SP, or as ab to pq.",
     "dipende_da": [],
     "figura": {
      "mostra": [
       "sv",
       "v (minuscolo)",
       "vh"
      ],
      "evidenzia": [
       "svh ~ spq"
      ]
     }
    },
    {
     "id": "L1-P20-p29",
     "la": "",
     "it": "Dunque vh e ab sono uguali.",
     "en": "Wherefore vh and ab are equal.",
     "dipende_da": [],
     "figura": {
      "mostra": [],
      "evidenzia": [
       "vh = ab"
      ]
     }
    },
    {
     "id": "L1-P20-p30",
     "la": "",
     "it": "Inoltre, per i triangoli simili VSH, vsh, VH sta a SH come vh sta a sh, cioè l’asse della sezione conica ora descritta sta alla distanza dei suoi fuochi come l’asse ab sta alla distanza dei fuochi sh; e perciò la figura ora descritta è simile alla figura apb.",
     "en": "But, because of the similar triangles VSH, vsh, VH is to SH as vh to sh; that is, the axis of the conic section now described is to the distance of its foci as the axis ab to the distance of the foci sh; and therefore the figure now described is similar to the figure aph.",
     "dipende_da": [],
     "figura": {
      "mostra": [],
      "evidenzia": [
       "VH : SH = ab : sh"
      ]
     },
     "nota": "Motte 1846 stampa «aph» per apb: refuso. Nella trascrizione la frase è preceduta da [FIG 34]."
    },
    {
     "id": "L1-P20-p31",
     "la": "",
     "it": "Questa figura passa poi per il punto P, perché il triangolo PSH è simile al triangolo psh; e, poiché VH è uguale al suo asse e VS è diviso a metà perpendicolarmente dalla retta TR, essa tocca la retta TR. C.V.F.",
     "en": "But, because the triangle PSH is similar to the triangle psh, this figure passes through the point P; and because VH is equal to its axis, and VS is perpendicularly bisected by the right line TR, the said figure touches the right line TR. Q.E.F.",
     "dipende_da": [],
     "figura": {
      "mostra": [],
      "evidenzia": [
       "P sulla conica",
       "TR tangente (Lemma XV)"
      ]
     },
     "nota": "«biscatur» nella trascrizione è refuso probabile per «bisecatur». Il testo non cita il Lemma XV, che è usato implicitamente."
    }
   ]
  },
  {
   "id": "L1-Lem16",
   "tipo": "Lemma",
   "titolo": "Lemma XVI — punto con differenze di distanza date da tre punti",
   "copertura": [
    "S4.18",
    "S4.19",
    "S4.20",
    "S4.21",
    "S4.22"
   ],
   "fonti": {
    "la": "",
    "en": "Motte 1846, pp. 129–130"
   },
   "enunciato": {
    "la": "",
    "it": "Da tre punti dati condurre a un quarto punto non dato tre rette le cui differenze siano date o nulle.",
    "en": "From three given points to draw to a fourth point that is not given three right lines whose differences shall be either given, or none at all."
   },
   "figura_base": {
    "punti": [
     "A",
     "B",
     "C",
     "Z",
     "M",
     "N",
     "P",
     "R",
     "Q",
     "S",
     "T"
    ],
    "vincoli": [
     "A, B, C dati; Z cercato",
     "iperbole di fuochi A, B e asse principale MN = |AZ − BZ|",
     "PM : MA = MN : AB; PR ⊥ AB; ZR ⊥ PR (PR direttrice)",
     "QS ⊥ AC (direttrice della seconda iperbole); ZS ⊥ QS",
     "T = RP ∩ SQ"
    ]
   },
   "passi": [
    {
     "id": "L1-Lem16-p1",
     "la": "",
     "it": "Caso 1. Siano A, B, C i punti dati e Z il quarto punto, che si deve trovare; per la differenza data delle linee AZ, BZ, il punto Z si troverà su un’iperbole i cui fuochi sono A e B e il cui asse principale è quella differenza data.",
     "en": "Let the given points be A, B, C, and Z the fourth point which we are to find; because of the given difference of the lines AZ, BZ, the locus of the point Z will be an hyperbola whose foci are A and B, and whose principal axis is the given difference.",
     "dipende_da": [],
     "figura": {
      "mostra": [
       "A",
       "B",
       "C",
       "Z",
       "iperbole (A, B)"
      ],
      "evidenzia": [
       "|AZ − BZ| dato"
      ]
     },
     "nota": "Nella trascrizione la frase contiene il marcatore di pagina <71>."
    },
    {
     "id": "L1-Lem16-p2",
     "la": "",
     "it": "Sia MN quell’asse.",
     "en": "Let that axis be MN.",
     "dipende_da": [],
     "figura": {
      "mostra": [
       "M",
       "N"
      ],
      "evidenzia": []
     }
    },
    {
     "id": "L1-Lem16-p3",
     "la": "",
     "it": "Prendi PM a MA come MN sta ad AB e, innalzata PR perpendicolare ad AB e abbassata ZR perpendicolare a PR, per la natura di questa iperbole ZR starà ad AZ come MN sta ad AB.",
     "en": "Taking PM to MA as MN is to AB, erect PR perpendicular to AB, and let fall ZR perpendicular to PR; then from the nature of the hyperbola, ZR will be to AZ as MN is to AB.",
     "dipende_da": [],
     "figura": {
      "mostra": [
       "P",
       "PR",
       "R",
       "ZR"
      ],
      "evidenzia": [
       "ZR : AZ = MN : AB"
      ]
     }
    },
    {
     "id": "L1-Lem16-p4",
     "la": "",
     "it": "Con un ragionamento simile il punto Z si troverà su un’altra iperbole, i cui fuochi sono A, C e il cui asse principale è la differenza fra AZ e CZ; e si può condurre QS perpendicolare ad AC, sulla quale, se da un punto qualsiasi Z di questa iperbole si abbassa la normale ZS, questa starà ad AZ come la differenza fra AZ e CZ sta ad AC.",
     "en": "And by the like argument, the locus of the point Z will be another hyperbola, whose foci are A, C, and whose principal axis is the difference between AZ and CZ; and QS a perpendicular on AC may be drawn, to which (QS) if from any point Z of this hyperbola a perpendicular ZS is let fall (this ZS), shall be to AZ as the difference between AZ and CZ is to AC.",
     "dipende_da": [],
     "figura": {
      "mostra": [
       "iperbole (A, C)",
       "QS",
       "S (piede)",
       "ZS"
      ],
      "evidenzia": [
       "ZS : AZ = |AZ − CZ| : AC"
      ]
     },
     "nota": "«Normale»: il latino ha qui «normalis», non «perpendicularis». Motte aggiunge «(QS)» e «(this ZS)»."
    },
    {
     "id": "L1-Lem16-p5",
     "la": "",
     "it": "Sono dunque dati i rapporti di ZR e di ZS ad AZ, e perciò è dato il rapporto di ZR e ZS fra loro; e quindi, se le rette RP, SQ concorrono in T, e si conducono TZ e TA, la figura TRZS sarà data di forma, e la retta TZ, sulla quale si trova in qualche punto il punto Z, sarà data di posizione.",
     "en": "Wherefore the ratios of ZR and ZS to AZ are given, and consequently the ratio of ZR to ZS one to the other; and therefore if the right lines RP, SQ, meet in T, and TZ and TA are drawn, the figure TRZS will be given in specie, and the right line TZ, in which the point Z is somewhere placed, will be given in position.",
     "dipende_da": [],
     "figura": {
      "mostra": [
       "T",
       "TZ",
       "TA",
       "figura TRZS"
      ],
      "evidenzia": [
       "ZR : ZS dato"
      ]
     },
     "nota": "Nella trascrizione la frase contiene [FIG 35]."
    },
    {
     "id": "L1-Lem16-p6",
     "la": "",
     "it": "Sarà data anche la retta TA, come pure l’angolo ATZ; e, poiché sono dati i rapporti di AZ e di TZ a ZS, sarà dato il loro rapporto fra loro; e di qui sarà dato il triangolo ATZ, il cui vertice è il punto Z. C.V.T.",
     "en": "There will be given also the right line TA, and the angle ATZ; and because the ratios of AZ and TZ to ZS are given, their ratio to each other is given also; and thence will be given likewise the triangle ATZ, whose vertex is the point Z. Q.E.I.",
     "dipende_da": [],
     "figura": {
      "mostra": [
       "triangolo ATZ"
      ],
      "evidenzia": [
       "Z vertice del triangolo ATZ"
      ]
     }
    },
    {
     "id": "L1-Lem16-p7",
     "la": "",
     "it": "Caso 2. Se due delle tre linee, per esempio AZ e BZ, sono uguali, conduci la retta TZ in modo che divida a metà la retta AB; poi cerca il triangolo ATZ come sopra.",
     "en": "If two of the three lines, for example AZ and BZ, are equal, draw the right line TZ so as to bisect the right line AB; then find the triangle ATZ as above.",
     "dipende_da": [],
     "figura": {
      "mostra": [
       "asse di AB"
      ],
      "evidenzia": []
     },
     "nota": "Motte aggiunge in fondo «Q.E.I.», assente nel latino."
    },
    {
     "id": "L1-Lem16-p8",
     "la": "",
     "it": "Caso 3. Se tutte e tre sono uguali, il punto Z si troverà nel centro del cerchio che passa per i punti A, B, C. C.V.T.",
     "en": "If all the three are equal, the point Z will be placed in the centre of a circle that passes through the points A, B, C. Q.E.I.",
     "dipende_da": [],
     "figura": {
      "mostra": [
       "cerchio per A, B, C"
      ],
      "evidenzia": []
     }
    }
   ]
  },
  {
   "id": "L1-P21",
   "tipo": "Propositio/Problema",
   "titolo": "Prop. XXI — secondo fuoco da punti e tangenti",
   "copertura": [
    "S4.24",
    "S4.25"
   ],
   "fonti": {
    "la": "",
    "en": "Motte 1846, p. 130"
   },
   "enunciato": {
    "la": "",
    "it": "Descrivere intorno a un fuoco dato una traiettoria che passi per punti dati e tocchi rette date di posizione.",
    "en": "About a given focus to describe a trajectory that shall pass through given points and touch right lines given by position."
   },
   "figura_base": {
    "punti": [
     "S",
     "P",
     "T",
     "R",
     "Y",
     "H"
    ],
    "vincoli": [
     "S fuoco dato; P punto; TR tangente",
     "ST ⊥ TR, TY = ST (Y simmetrico di S)",
     "YH = asse principale; |HP − asse| = SP"
    ]
   },
   "passi": [
    {
     "id": "L1-P21-p1",
     "la": "",
     "it": "Siano dati il fuoco S, il punto P e la tangente TR, e si debba trovare l’altro fuoco H.",
     "en": "Let the focus S, the point P, and the tangent TR be given, and suppose that the other focus H is to be found.",
     "dipende_da": [],
     "figura": {
      "mostra": [
       "S",
       "P",
       "TR"
      ],
      "evidenzia": []
     }
    },
    {
     "id": "L1-P21-p2",
     "la": "",
     "it": "Sulla tangente abbassa la perpendicolare ST, e prolungala fino a Y, in modo che TY sia uguale a ST, e YH sarà uguale all’asse principale.",
     "en": "On the tangent let fall the perpendicular ST, which produce to Y, so that TY may be equal to ST, and YH will be equal to the principal axis.",
     "dipende_da": [],
     "figura": {
      "mostra": [
       "T",
       "Y",
       "YH"
      ],
      "evidenzia": [
       "YH = asse"
      ]
     },
     "nota": "Nella trascrizione la frase contiene il marcatore <72> e un «{&}» tra graffe, integrazione editoriale del Newton Project."
    },
    {
     "id": "L1-P21-p3",
     "la": "",
     "it": "Congiungi SP, HP, e SP sarà la differenza fra HP e l’asse principale.",
     "en": "Join SP, HP, and SP will be the difference between HP and the principal axis.",
     "dipende_da": [],
     "figura": {
      "mostra": [
       "SP",
       "HP"
      ],
      "evidenzia": [
       "|HP − asse| = SP"
      ]
     }
    },
    {
     "id": "L1-P21-p4",
     "la": "",
     "it": "In questo modo, se sono date più tangenti TR o più punti P, si giungerà sempre ad altrettante linee YH o PH, condotte dai detti punti Y o P al fuoco H, che o sono uguali agli assi o differiscono da essi per le lunghezze date SP, e che perciò o sono uguali fra loro o hanno differenze date; e di qui, per il lemma precedente, è dato quell’altro fuoco H.",
     "en": "After this manner, if more tangents TR are given, or more points P, we shall always determine as many lines YH, or PH, drawn from the said points Y or P, to the focus H, which either shall be equal to the axes, or differ from the axes by given lengths SP; and therefore which shall either be equal among themselves, or shall have given differences; from whence (by the preceding Lemma), that other focus H is given.",
     "dipende_da": [
      "Lemma XVI"
     ],
     "figura": {
      "mostra": [
       "più punti Y o P"
      ],
      "evidenzia": [
       "differenze date → Lemma XVI"
      ]
     },
     "nota": "Nella trascrizione la frase contiene [FIG 36]."
    },
    {
     "id": "L1-P21-p5",
     "la": "",
     "it": "Avuti poi i fuochi insieme con la lunghezza dell’asse (che è YH oppure, se la traiettoria è un’ellisse, PH + SP, se è un’iperbole, PH − SP), si ha la traiettoria. C.V.T.",
     "en": "But having the foci and the length of the axis (which is either YH, or, if the trajectory be an ellipsis, PH + SP; or PH - SP, if it be an hyperbola), the trajectory is given. Q.E.I.",
     "dipende_da": [],
     "figura": {
      "mostra": [
       "traiettoria"
      ],
      "evidenzia": []
     }
    }
   ]
  },
  {
   "id": "L1-S4-Schol",
   "tipo": "Scholium",
   "titolo": "Scolio alla Sez. IV — traiettoria per tre punti dato il fuoco",
   "copertura": [
    "S4.26",
    "S4.27",
    "S4.28"
   ],
   "fonti": {
    "la": "",
    "en": "Motte 1846, pp. 130–131"
   },
   "figura_base": {
    "punti": [
     "S",
     "B",
     "C",
     "D",
     "E",
     "F",
     "G",
     "H",
     "A",
     "a",
     "I",
     "K"
    ],
    "vincoli": [
     "S fuoco; B, C, D punti dati",
     "E su BC prolungata con EB : EC = SB : SC; F su CD prolungata con FC : FD = SC : SD",
     "EF direttrice; SG, BH, CI, DK perpendicolari a EF",
     "GA : AS = Ga : aS = HB : BS"
    ]
   },
   "passi": [
    {
     "id": "L1-S4-Schol-p1",
     "la": "",
     "it": "Quando la traiettoria è un’iperbole, sotto il nome di questa traiettoria non comprendo l’iperbole opposta.",
     "en": "When the trajectory is an hyperbola, I do not comprehend its conjugate hyperbola under the name of this trajectory.",
     "dipende_da": [],
     "figura": {
      "mostra": [],
      "evidenzia": []
     },
     "nota": "Motte traduce «oppositam hyperbolam» con «conjugate hyperbola»: errore di senso (vedi Prop. XII)."
    },
    {
     "id": "L1-S4-Schol-p2",
     "la": "",
     "it": "Un corpo, infatti, proseguendo nel suo moto, non può passare nell’iperbole opposta.",
     "en": "For a body going on with a continued motion can never pass out of one hyperbola into its conjugate hyperbola.",
     "dipende_da": [],
     "figura": {
      "mostra": [],
      "evidenzia": []
     },
     "nota": "Motte aggiunge «continued» e «never»."
    },
    {
     "id": "L1-S4-Schol-p3",
     "la": "",
     "it": "Il caso in cui sono dati tre punti si risolve più speditamente così.",
     "en": "The case when three points are given is more readily solved thus.",
     "dipende_da": [],
     "figura": {
      "mostra": [],
      "evidenzia": []
     }
    },
    {
     "id": "L1-S4-Schol-p4",
     "la": "",
     "it": "Siano dati i punti B, C, D.",
     "en": "Let B, C, D, be the given points.",
     "dipende_da": [],
     "figura": {
      "mostra": [
       "S",
       "B",
       "C",
       "D"
      ],
      "evidenzia": []
     }
    },
    {
     "id": "L1-S4-Schol-p5",
     "la": "",
     "it": "Prolunga le congiungenti BC, CD fino a E, F, in modo che EB stia a EC come SB sta a SC, e FC stia a FD come SC sta a SD.",
     "en": "Join BC, CD, and produce them to E, F, so as EB may be to EC as SB to SC; and FC to FD as SC to SD.",
     "dipende_da": [],
     "figura": {
      "mostra": [
       "BC",
       "CD",
       "E",
       "F"
      ],
      "evidenzia": [
       "EB : EC = SB : SC",
       "FC : FD = SC : SD"
      ]
     }
    },
    {
     "id": "L1-S4-Schol-p6",
     "la": "",
     "it": "Sulla EF, condotta e prolungata, abbassa le normali SG, BH, e sulla GS prolungata all’infinito prendi GA ad AS e Ga ad aS come HB sta a BS; e A sarà il vertice e Aa l’asse principale della traiettoria; la quale, secondo che GA sia maggiore, uguale o minore di AS, sarà un’ellisse, una parabola o un’iperbole: nel primo caso il punto a cade dalla stessa parte della linea GF del punto A; nel secondo se ne va all’infinito; nel terzo cade dalla parte opposta della linea GF.",
     "en": "On EF drawn and produced let fall the perpendiculars SG, BH, and in GS produced indefinitely take GA to AS, and Ga to aS, as HB is to BS; then A will be the vertex, and Aa the principal axis of the trajectory; which, according as GA is greater than, equal to, or less than AS, will be either an ellipsis, a parabola, or an hyperbola; the point a in the first case falling on the same side of the line GF as the point A; in the second, going off to an infinite distance; in the third, falling on the other side of the line GF.",
     "dipende_da": [],
     "figura": {
      "mostra": [
       "EF",
       "SG",
       "G",
       "BH",
       "H",
       "A",
       "a"
      ],
      "evidenzia": [
       "GA : AS = Ga : aS = HB : BS"
      ]
     },
     "nota": "Nella trascrizione la frase contiene [FIG 37]."
    },
    {
     "id": "L1-S4-Schol-p7",
     "la": "",
     "it": "Se infatti si abbassano su GF le perpendicolari CI, DK, IC starà a HB come EC sta a EB, cioè come SC sta a SB; e, permutando, IC starà a SC come HB sta a SB, ossia come GA sta a SA.",
     "en": "For if on GF the perpendiculars CI, DK are let fall, IC will be to HB as EC to EB; that is, as SC to SB; and by permutation, IC to SC as HB to SB, or as GA to SA.",
     "dipende_da": [],
     "figura": {
      "mostra": [
       "CI",
       "I",
       "DK",
       "K"
      ],
      "evidenzia": [
       "IC : SC = HB : SB = GA : SA"
      ]
     }
    },
    {
     "id": "L1-S4-Schol-p8",
     "la": "",
     "it": "E con un argomento simile si proverà che KD sta a SD nello stesso rapporto.",
     "en": "And, by the like argument, we may prove that KD is to SD in the same ratio.",
     "dipende_da": [],
     "figura": {
      "mostra": [],
      "evidenzia": [
       "KD : SD = HB : SB"
      ]
     },
     "nota": "Nella trascrizione la frase è preceduta dal marcatore di pagina <73>."
    },
    {
     "id": "L1-S4-Schol-p9",
     "la": "",
     "it": "I punti B, C, D giacciono dunque in una sezione conica descritta intorno al fuoco S in modo tale che tutte le rette condotte dal fuoco S ai singoli punti della sezione stiano alle perpendicolari abbassate dagli stessi punti sulla retta GF in quel rapporto dato.",
     "en": "Wherefore the points B, C, D lie in a conic section described about the focus S, in such manner that all the right lines drawn from the focus S to the several points of the section, and the perpendiculars let fall from the same points on the right line GF, are in that given ratio.",
     "dipende_da": [],
     "figura": {
      "mostra": [
       "conica per B, C, D"
      ],
      "evidenzia": [
       "distanza dal fuoco : distanza dalla direttrice = costante"
      ]
     },
     "nota": "«cica» nella trascrizione è refuso probabile per «circa»."
    }
   ]
  }
 ]
}
```
