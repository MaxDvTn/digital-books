> **Copia pubblica.** In questa versione i campi `"la"` della Parte B sono vuoti: le frasi latine vengono dalla trascrizione del Newton Project, che non si ridistribuisce. Il latino del 1726 si legge su newtonproject.ox.ac.uk.

# Isaac Newton
# Principi matematici della filosofia naturale

## Fascicolo 11 — Libro I, Sezione XII: Le forze attrattive dei corpi sferici

**Nuova traduzione italiana di lavoro dal latino del 1726, confrontata con l’inglese di Andrew Motte nell’edizione del 1846.**

Versione 0.1 — 8 novembre 2026. Preparata con Claude (Anthropic) per Massimo Bosetti.

### Stato e perimetro

Questo fascicolo traduce integralmente la **Sezione XII del Libro I**, *De corporum sphæricorum viribus attractivis*: le Proposizioni LXX–LXXXIV con i loro corollari, il Lemma XXIX, i tre esempi della Prop. LXXXI e i tre scolii della sezione. Comprende i teoremi sul guscio sferico (Propp. LXX–LXXI) e la loro estensione alla sfera piena (Propp. LXXIII–LXXVI). È una traduzione di lavoro, non un’edizione critica validata.

Gli identificatori **S12.01–S12.69** e i titoli tematici tra parentesi sono aggiunte editoriali; i numeri delle proposizioni, dei teoremi, dei problemi, dei lemmi, dei corollari e dei casi appartengono al testo originale. Le note poste dopo la traduzione non fanno parte del testo di Newton.

In coda al fascicolo:

- le **note editoriali e fisiche** N1–N15, con le corrispondenze moderne e i controlli numerici (script `verifica_S12.py`);
- la **Parte B**, con i dati strutturati per le pagine interattive di 15 unità: Propp. LXX, LXXI, LXXIII, LXXVI, LXXVII, Lemma XXIX, Propp. LXXIX, LXXX, LXXXI con i suoi tre esempi, LXXXII, LXXXIII, LXXXIV.

### Fonti effettivamente consultate

1. **Latino di riferimento.** Isaac Newton, *Philosophiæ Naturalis Principia Mathematica*, terza edizione, Londra, 1726, Libro I, Sezione XII, pp. 189–210. Trascrizione normalizzata del Newton Project, documento **NATP00087**, nella copia di lavoro `fonti/latino-1726-L1-S12.md` (scaricata l’8 novembre 2026, estratta in testo semplice senza correzioni). Il primo marcatore di pagina della trascrizione è <190>, nell’enunciato della Prop. LXXI: la sezione comincia quindi a p. 189. L’ultimo marcatore è <210>, prima dello Scolio finale.
2. **Inglese di confronto.** *Newton’s Principia. The Mathematical Principles of Natural Philosophy*, traduzione di Andrew Motte, New York, Daniel Adee, 1846, Libro I, Sezione XII, **pp. 219–233** secondo i marcatori di pagina dell’EPUB (Project Gutenberg n. 76404). Estratto di lavoro: `fonti/motte-1846-L1-S12.md`. I marcatori di pagina non sono nell’estratto: li ho ricavati dal file XHTML dell’EPUB (`…76404-h-14.htm.xhtml`, ancore `Page_219`…`Page_233`). Le formule stampate come immagini (SVG 256–308) sono state tutte rese con `rsvg-convert` e lette una per una.
3. **Brief comune** del Libro I e **Fascicolo 3** (*Assiomi, ovvero leggi del moto*, v0.3), per il formato, i criteri e il glossario.

Non ho consultato né riprodotto traduzioni moderne (Cajori, Cohen–Whitman, Pala, Giudice). Le figure originali (NATP00087-132…150) non erano disponibili: le relazioni geometriche sono ricostruite soltanto dalle lettere citate nel testo. La stampa del 1726 non è stata vista: i refusi segnalati restano «da verificare sulla stampa».

### Criteri di traduzione

- Il testo guida è il latino; l’inglese serve al controllo ed è annotato quando aggiunge, omette o sbaglia.
- Si rispetta il **glossario comune** del brief (Fascicoli 1–3 e termini tecnici del Libro I): *vis centripeta* «forza centripeta», *ratio duplicata / triplicata / subduplicata* «rapporto duplicato / triplicato / subduplicato», *reciproce* «inversamente», *ratio ultima* «rapporto ultimo», *quantitates evanescentes* «evanescenti», *ultimo* «alla fine», *conjunctim* «considerate congiuntamente», *ducere in* «moltiplicare per», *attractio* «attrazione», *particula* «particella», *superficies sphærica* «superficie sferica», *umbilicus* «fuoco», *ordinatim applicata* «ordinata», *Cas.* «Caso», Q.E.D. «C.V.D.», Q.E.I. «C.V.T.», Q.E.F. «C.V.F.».
- **Estensioni proprie** di questo fascicolo, motivate nel § A.0: *corpusculum* «corpuscolo»; *orbis* (Scolio dopo la Prop. LXXIII) «guscio»; *similaris* «similare»; *trahere* «tirare», distinto da *attrahere* «attrarre»; *applicare ad* «dividere per»; *ducere in … per motum continuum* «condurre lungo … con moto continuo»; *ex æquo* «per uguaglianza»; *ratio quadruplicata* «rapporto quadruplicato»; *contentum sub* «compreso fra»; *lineola* «lineetta»; *convolutio* «rotazione»; *intervallum* «raggio».
- Gli enunciati all’infinito o al congiuntivo retti da *dico quod* sono resi con l’indicativo.
- Le formule della trascrizione sono spesso **appiattite** (frazioni e radicali persi). Nel testo italiano le scrivo con apici Unicode e con la barra, aggiungendo parentesi dove servono a evitare ambiguità: per esempio DE²×PS/(PE×V). Ogni lettura è dichiarata nell’apparato (§ A.17) e controllata sulle formule di Motte e per calcolo.
- Le notazioni di Newton per i rettangoli restano come nel latino: **ALB** è il rettangolo AL×LB, **PSI** è PS×SI, **2SLD** è 2·SL·LD, **2PSD** è 2·PS·SD, **2ASI** è 2·AS·SI.
- Le maiuscole e la punteggiatura sono adattate all’uso italiano. I periodi lunghi delle dimostrazioni sono conservati, salvo dove la sintassi italiana richiede di spezzarli.

---

## Traduzione italiana

### Sezione XII

### Le forze attrattive dei corpi sferici

### Proposizione LXX. Teorema XXX (attrazione nulla all’interno di una superficie sferica)

**[S12.01]** **Se ai singoli punti di una superficie sferica tendono forze centripete uguali, decrescenti in rapporto duplicato delle distanze dai punti, dico che un corpuscolo posto all’interno della superficie non è attratto da queste forze verso alcuna parte.**

**[S12.02]** Sia HIKL quella superficie sferica, e P il corpuscolo posto all’interno. Per P si conducano fino a questa superficie due linee HK, IL, che intercettino archi piccolissimi HI, KL; e, poiché i triangoli HPI, LPK sono simili (per il Cor. 3 del Lemma VII), quegli archi saranno proporzionali alle distanze HP, LP; e le particelle qualsiasi della superficie sferica in HI e in KL, delimitate tutt’intorno da rette passanti per il punto P, staranno in quel rapporto duplicato. Dunque le forze di queste particelle esercitate sul corpo P sono uguali fra loro. Esse sono infatti direttamente come le particelle e inversamente come i quadrati delle distanze. E questi due rapporti compongono il rapporto di uguaglianza. Le attrazioni, dunque, fatte in egual misura verso parti contrarie, si distruggono a vicenda. E con un argomento simile tutte le attrazioni su tutta la superficie sferica sono distrutte da attrazioni contrarie. Perciò il corpo P non è spinto verso alcuna parte da queste attrazioni. C.V.D.

### Proposizione LXXI. Teorema XXXI (attrazione di una superficie sferica su un corpuscolo esterno)

**[S12.03]** **Poste le stesse cose, dico che un corpuscolo posto all’esterno della superficie sferica è attratto verso il centro della sfera da una forza inversamente proporzionale al quadrato della sua distanza dallo stesso centro.**

**[S12.04]** Siano AHKB, ahkb due superfici sferiche uguali, descritte con centri S, s e diametri AB, ab; e siano P, p corpuscoli situati all’esterno, sui prolungamenti di quei diametri. Dai corpuscoli si conducano le linee PHK, PIL, phk, pil, che taglino dai cerchi massimi AHB, ahb archi uguali HK, hk e IL, il; e su di esse si abbassino le perpendicolari SD, sd; SE, se; IR, ir, delle quali SD, sd taglino PL, pl in F e f; si abbassino anche sui diametri le perpendicolari IQ, iq. Svaniscano gli angoli DPE, dpe; e, poiché DS e ds, ES ed es sono uguali, le linee PE, PF e pe, pf e le lineette DF, df si considerino uguali: il loro rapporto ultimo, quando quegli angoli DPE, dpe svaniscono insieme, è infatti di uguaglianza. Stabilite dunque queste cose, PI starà a PF come RI sta a DF, e pf starà a pi come df, ossia DF, sta a ri; e, per uguaglianza, PI×pf starà a PF×pi come RI sta a ri, cioè (per il Cor. 3 del Lemma VII) come l’arco IH sta all’arco ih. Di nuovo, PI sta a PS come IQ sta a SE, e ps sta a pi come se, ossia SE, sta a iq; e, per uguaglianza, PI×ps sta a PS×pi come IQ sta a iq. E, congiungendo i rapporti, PI²×pf×ps sta a pi²×PF×PS come IH×IQ sta a ih×iq; cioè come la superficie circolare che l’arco IH descriverà con la rotazione del semicerchio AKB intorno al diametro AB sta alla superficie circolare che l’arco ih descriverà con la rotazione del semicerchio akb intorno al diametro ab. E le forze con cui queste superfici attraggono i corpuscoli P e p lungo linee dirette verso di esse sono (per ipotesi) direttamente come le superfici stesse e inversamente come i quadrati delle distanze delle superfici dai corpi, cioè come pf×ps sta a PF×PS. E queste forze stanno alle loro parti oblique che (fatta la scomposizione delle forze per il Cor. 2 delle leggi) tendono ai centri lungo le linee PS, ps, come PI sta a PQ e pi a pq; cioè (per la similitudine dei triangoli PIQ e PSF, piq e psf) come PS sta a PF e ps a pf. Di qui, per uguaglianza, l’attrazione di questo corpuscolo P verso S sta all’attrazione del corpuscolo p verso s come (PF×pf×ps)/PS sta a (pf×PF×PS)/ps, cioè come ps² sta a PS². E con un argomento simile le forze con cui le superfici descritte dalla rotazione degli archi KL, kl tirano i corpuscoli staranno come ps² sta a PS²; e nello stesso rapporto staranno le forze di tutte le superfici circolari in cui ciascuna delle due superfici sferiche può essere divisa, prendendo sempre sd uguale a SD e se uguale a SE. E, per composizione, le forze delle intere superfici sferiche esercitate sui corpuscoli staranno nello stesso rapporto. C.V.D.

### Proposizione LXXII. Teorema XXXII (attrazione in punti simili di sfere simili)

**[S12.05]** **Se ai singoli punti di una sfera qualsiasi tendono forze centripete uguali, decrescenti in rapporto duplicato delle distanze dai punti, e sono dati sia la densità della sfera sia il rapporto del diametro della sfera alla distanza del corpuscolo dal suo centro, dico che la forza con cui il corpuscolo è attratto sarà proporzionale al semidiametro della sfera.**

**[S12.06]** Immagina infatti che due corpuscoli siano attratti separatamente da due sfere, uno dall’una e l’altro dall’altra, che le loro distanze dai centri delle sfere siano proporzionali rispettivamente ai diametri delle sfere, e che le sfere si risolvano in particelle simili e similmente disposte rispetto ai corpuscoli. Allora le attrazioni di un corpuscolo verso le singole particelle di una sfera staranno alle attrazioni dell’altro verso altrettante particelle analoghe dell’altra sfera nel rapporto composto dal rapporto diretto delle particelle e dal rapporto duplicato inverso delle distanze. Ma le particelle stanno come le sfere, cioè in rapporto triplicato dei diametri, e le distanze stanno come i diametri; e il primo rapporto preso direttamente, insieme con il secondo preso due volte inversamente, è il rapporto del diametro al diametro. C.V.D.

**[S12.07]** *Cor. 1.* Di qui, se dei corpuscoli ruotano in cerchi intorno a sfere costituite di materia ugualmente attrattiva, e le distanze dai centri delle sfere sono proporzionali ai loro diametri, i tempi periodici saranno uguali.

**[S12.08]** *Cor. 2.* E viceversa, se i tempi periodici sono uguali, le distanze saranno proporzionali ai diametri. Queste due cose risultano dal Cor. 3 della Prop. IV.

**[S12.09]** *Cor. 3.* Se ai singoli punti di due solidi qualsiasi, simili e ugualmente densi, tendono forze centripete uguali, decrescenti in rapporto duplicato delle distanze dai punti, le forze con cui dei corpuscoli, situati in modo simile rispetto a quei due solidi, saranno attratti da essi staranno fra loro come i diametri dei solidi.

### Proposizione LXXIII. Teorema XXXIII (attrazione all’interno di una sfera piena)

**[S12.10]** **Se ai singoli punti di una sfera data tendono forze centripete uguali, decrescenti in rapporto duplicato delle distanze dai punti, dico che un corpuscolo posto all’interno della sfera è attratto da una forza proporzionale alla sua distanza dal centro della sfera.**

**[S12.11]** Nella sfera ABCD, descritta con centro S, si collochi il corpuscolo P; e con lo stesso centro S e con raggio SP immagina descritta una sfera interna PEQF. È manifesto (per la Prop. LXX) che le superfici sferiche concentriche di cui è composta la differenza AEBF delle sfere non agiscono affatto sul corpo P, perché le loro attrazioni sono distrutte da attrazioni contrarie. Resta la sola attrazione della sfera interna PEQF. E (per la Prop. LXXII) questa è come la distanza PS. C.V.D.

### Scolio (superfici e punti come particelle evanescenti)

**[S12.12]** Le superfici di cui si compongono i solidi non sono qui puramente matematiche, ma gusci tanto sottili che il loro spessore è come nulla: cioè i gusci evanescenti di cui alla fine è costituita la sfera, quando il numero di quei gusci viene aumentato e lo spessore diminuito all’infinito. Similmente, per punti di cui si dice che sono composti linee, superfici e solidi, si devono intendere particelle uguali di grandezza trascurabile.

### Proposizione LXXIV. Teorema XXXIV (attrazione di una sfera piena su un corpuscolo esterno)

**[S12.13]** **Poste le stesse cose, dico che un corpuscolo posto all’esterno della sfera è attratto da una forza inversamente proporzionale al quadrato della sua distanza dal centro della sfera.**

**[S12.14]** Si divida infatti la sfera in innumerevoli superfici sferiche concentriche: le attrazioni del corpuscolo provenienti dalle singole superfici saranno inversamente proporzionali al quadrato della distanza del corpuscolo dal centro (per la Prop. LXXI). E componendo si avrà la somma delle attrazioni, cioè l’attrazione del corpuscolo verso la sfera intera, nello stesso rapporto. C.V.D.

**[S12.15]** *Cor. 1.* Di qui, a distanze uguali dai centri di sfere omogenee, le attrazioni stanno come le sfere. Infatti (per la Prop. LXXII), se le distanze sono proporzionali ai diametri delle sfere, le forze staranno come i diametri. Si diminuisca la distanza maggiore in quel rapporto; e, rese ormai uguali le distanze, l’attrazione crescerà in quel rapporto duplicato; e perciò starà all’altra attrazione in quel rapporto triplicato, cioè nel rapporto delle sfere.

**[S12.16]** *Cor. 2.* A distanze qualsiasi le attrazioni stanno come le sfere divise per i quadrati delle distanze.

**[S12.17]** *Cor. 3.* Se un corpuscolo posto all’esterno di una sfera omogenea è attratto da una forza inversamente proporzionale al quadrato della sua distanza dal centro della sfera, e la sfera è costituita di particelle attrattive, la forza di ciascuna particella decrescerà in rapporto duplicato della distanza dalla particella.

### Proposizione LXXV. Teorema XXXV (attrazione fra due sfere)

**[S12.18]** **Se ai singoli punti di una sfera data tendono forze centripete uguali, decrescenti in rapporto duplicato delle distanze dai punti, dico che qualsiasi altra sfera similare è attratta da essa con una forza inversamente proporzionale al quadrato della distanza dei centri.**

**[S12.19]** Infatti l’attrazione di qualsiasi particella è inversamente come il quadrato della sua distanza dal centro della sfera che tira (per la Prop. LXXIV), e perciò è la stessa che se tutta la forza attraente emanasse da un unico corpuscolo situato nel centro di questa sfera. Ma questa attrazione è tanto grande quanto sarebbe, a sua volta, l’attrazione dello stesso corpuscolo, se esso fosse tirato dalle singole particelle della sfera attratta con la stessa forza con cui le attrae. E quell’attrazione del corpuscolo sarebbe (per la Prop. LXXIV) inversamente proporzionale al quadrato della sua distanza dal centro della sfera; e perciò l’attrazione della sfera, uguale a essa, sta nello stesso rapporto. C.V.D.

**[S12.20]** *Cor. 1.* Le attrazioni delle sfere verso altre sfere omogenee stanno come le sfere che tirano divise per i quadrati delle distanze dei loro centri dai centri di quelle che esse attraggono.

**[S12.21]** *Cor. 2.* Lo stesso vale quando anche la sfera attratta attrae. I suoi singoli punti, infatti, tireranno i singoli punti dell’altra con la stessa forza con cui sono a loro volta tirati da essi; e perciò, poiché in ogni attrazione è sollecitato (per la Legge III) tanto il punto che attrae quanto il punto attratto, la forza dell’attrazione reciproca sarà raddoppiata, conservandosi le proporzioni.

**[S12.22]** *Cor. 3.* Tutte le cose che sono state dimostrate sopra sul moto dei corpi intorno al fuoco delle sezioni coniche valgono quando la sfera che attrae è collocata nel fuoco e i corpi si muovono all’esterno della sfera.

**[S12.23]** *Cor. 4.* Quelle invece che si dimostrano sul moto dei corpi intorno al centro delle sezioni coniche valgono quando i moti si compiono all’interno della sfera.

### Proposizione LXXVI. Teorema XXXVI (sfere stratificate)

**[S12.24]** **Se delle sfere, procedendo dal centro alla circonferenza, sono dissimilari in modo qualsiasi (quanto alla densità della materia e alla forza attrattiva), ma, procedendo lungo il giro, sono similari da ogni parte a ogni distanza data dal centro; e la forza attrattiva di ciascun punto decresce in rapporto duplicato della distanza del corpo attratto: dico che la forza totale con cui una sfera di questo genere ne attrae un’altra è inversamente proporzionale al quadrato della distanza dei centri.**

**[S12.25]** Siano AB, CD, EF, ecc. sfere concentriche similari in numero qualsiasi, le interne delle quali, aggiunte alle esterne, compongano una materia più densa verso il centro, oppure, sottratte, la lascino più rada; e queste (per la Prop. LXXV) tireranno altre sfere concentriche similari in numero qualsiasi, GH, IK, LM, ecc., ciascuna delle prime ciascuna delle seconde, con forze inversamente proporzionali al quadrato della distanza SP. E componendo o dividendo, la somma di tutte quelle forze, o l’eccesso di alcune sulle altre, cioè la forza con cui l’intera sfera AB, composta di sfere concentriche qualsiasi o di differenze di sfere concentriche, tira l’intera GH, composta di sfere concentriche qualsiasi o di differenze di sfere concentriche, starà nello stesso rapporto. Si aumenti all’infinito il numero delle sfere concentriche, in modo che la densità della materia, insieme con la forza attrattiva, cresca o decresca secondo una legge qualsiasi procedendo dalla circonferenza al centro; e, aggiunta materia non attrattiva, si completi ovunque la densità mancante, affinché le sfere acquistino qualsiasi forma desiderata; e la forza con cui una di esse attrarrà l’altra sarà ancora, per l’argomento precedente, in quello stesso rapporto inverso del quadrato della distanza. C.V.D.

**[S12.26]** *Cor. 1.* Di qui, se più sfere di questo genere, simili fra loro in tutto, si tirano a vicenda, le attrazioni acceleratrici di ciascuna verso ciascuna, a distanze qualsiasi uguali dei centri, staranno come le sfere che attraggono.

**[S12.27]** *Cor. 2.* E a distanze qualsiasi disuguali, come le sfere che attraggono divise per i quadrati delle distanze fra i centri.

**[S12.28]** *Cor. 3.* Le attrazioni motrici, invece, ossia i pesi delle sfere verso le sfere, a distanze uguali dei centri staranno come le sfere che attraggono e quelle attratte considerate congiuntamente, cioè come i prodotti ottenuti moltiplicando le sfere fra loro.

**[S12.29]** *Cor. 4.* E a distanze disuguali, direttamente come quei prodotti e inversamente come i quadrati delle distanze fra i centri.

**[S12.30]** *Cor. 5.* Le stesse cose valgono quando l’attrazione nasce dalla virtù attrattiva di ciascuna delle due sfere esercitata reciprocamente sull’altra. Con entrambe le forze, infatti, l’attrazione si raddoppia, conservandosi la proporzione.

**[S12.31]** *Cor. 6.* Se alcune sfere di questo genere ruotano intorno ad altre in quiete, ciascuna intorno alla sua, e le distanze fra i centri di quelle che ruotano e di quelle in quiete sono proporzionali ai diametri di quelle in quiete, i tempi periodici saranno uguali.

**[S12.32]** *Cor. 7.* E viceversa, se i tempi periodici sono uguali, le distanze saranno proporzionali ai diametri.

**[S12.33]** *Cor. 8.* Tutte le cose che sono state dimostrate sopra sul moto dei corpi intorno ai fuochi delle sezioni coniche valgono quando una sfera che attrae, di qualsiasi forma e condizione fra quelle già descritte, è collocata nel fuoco.

**[S12.34]** *Cor. 9.* Come pure quando anche i corpi che girano sono sfere attraenti di qualsiasi condizione fra quelle già descritte.

### Proposizione LXXVII. Teorema XXXVII (forze proporzionali alla distanza)

**[S12.35]** **Se ai singoli punti delle sfere tendono forze centripete proporzionali alle distanze dei punti dai corpi attratti, dico che la forza composta con cui due sfere si tirano a vicenda è come la distanza fra i centri delle sfere.**

**[S12.36]** *Caso 1.* Sia AEBF una sfera; S il suo centro; P un corpuscolo attratto; PASB l’asse della sfera passante per il centro del corpuscolo; EF, ef due piani che tagliano la sfera, perpendicolari a questo asse e ugualmente distanti dal centro della sfera da una parte e dall’altra; G, g le intersezioni dei piani con l’asse; e H un punto qualsiasi nel piano EF. La forza centripeta del punto H sul corpuscolo P, esercitata lungo la linea PH, è come la distanza PH; e (per il Cor. 2 delle leggi) lungo la linea PG, ossia verso il centro S, è come la lunghezza PG. Dunque la forza di tutti i punti nel piano EF, cioè dell’intero piano, con cui il corpuscolo P è tirato verso il centro S, è come la distanza PG moltiplicata per il numero dei punti, cioè come il solido compreso fra il piano stesso EF e quella distanza PG. E similmente la forza del piano ef, con cui il corpuscolo P è tirato verso il centro S, è come quel piano moltiplicato per la sua distanza Pg, ossia come il piano EF, uguale a esso, moltiplicato per quella distanza Pg; e la somma delle forze dei due piani è come il piano EF moltiplicato per la somma delle distanze PG + Pg, cioè come quel piano moltiplicato per il doppio della distanza PS fra il centro e il corpuscolo, cioè come il doppio del piano EF moltiplicato per la distanza PS, o come la somma dei piani uguali EF + ef moltiplicata per la stessa distanza. E con un argomento simile le forze di tutti i piani nella sfera intera, ugualmente distanti dal centro della sfera da una parte e dall’altra, sono come la somma dei piani moltiplicata per la distanza PS, cioè come la sfera intera e la distanza PS considerate congiuntamente. C.V.D.

**[S12.37]** *Caso 2.* Ora il corpuscolo P tiri la sfera AEBF. Con lo stesso argomento si proverà che la forza con cui quella sfera è tirata sarà come la distanza PS. C.V.D.

**[S12.38]** *Caso 3.* Si componga ora un’altra sfera di innumerevoli corpuscoli P; e poiché la forza con cui è tirato ciascun corpuscolo è come la distanza del corpuscolo dal centro della prima sfera e come la sfera stessa, considerate congiuntamente, e perciò è la stessa che se provenisse tutta da un unico corpuscolo nel centro della sfera, la forza totale con cui sono tirati tutti i corpuscoli della seconda sfera, cioè con cui è tirata tutta quella sfera, sarà la stessa che se quella sfera fosse tirata da una forza proveniente da un unico corpuscolo nel centro della prima sfera; e perciò è proporzionale alla distanza fra i centri delle sfere. C.V.D.

**[S12.39]** *Caso 4.* Le sfere si tirino a vicenda: la forza raddoppiata conserverà la proporzione di prima. C.V.D.

**[S12.40]** *Caso 5.* Si collochi ora il corpuscolo p all’interno della sfera AEBF; e poiché la forza del piano ef sul corpuscolo è come il solido compreso fra quel piano e la distanza pg, e la forza contraria del piano EF come il solido compreso fra quel piano e la distanza pG, la forza composta da entrambe sarà come la differenza dei solidi, cioè come la somma dei piani uguali moltiplicata per la metà della differenza delle distanze, cioè come quella somma moltiplicata per pS, distanza del corpuscolo dal centro della sfera. E con un argomento simile l’attrazione di tutti i piani EF, ef nella sfera intera, cioè l’attrazione della sfera intera, è come la somma di tutti i piani, ossia la sfera intera, e come pS, distanza del corpuscolo dal centro della sfera, considerate congiuntamente. C.V.D.

**[S12.41]** *Caso 6.* E se di innumerevoli corpuscoli p si compone una nuova sfera, situata all’interno della sfera precedente AEBF, si proverà come prima che l’attrazione, sia semplice, di una sfera sull’altra, sia reciproca, di entrambe l’una sull’altra, sarà come la distanza dei centri pS. C.V.D.

### Proposizione LXXVIII. Teorema XXXVIII (sfere stratificate, forze proporzionali alla distanza)

**[S12.42]** **Se delle sfere, procedendo dal centro alla circonferenza, sono dissimilari e non uniformi in modo qualsiasi, ma, procedendo lungo il giro, sono similari da ogni parte a ogni distanza data dal centro; e la forza attrattiva di ciascun punto è come la distanza del corpo attratto: dico che la forza totale con cui due sfere di questo genere si tirano a vicenda è proporzionale alla distanza fra i centri delle sfere.**

**[S12.43]** Si dimostra dalla proposizione precedente nello stesso modo in cui la Prop. LXXVI è stata dimostrata dalla Prop. LXXV.

**[S12.44]** *Cor.* Ciò che è stato dimostrato sopra, nelle Propp. X e LXIV, sul moto dei corpi intorno ai centri delle sezioni coniche vale quando tutte le attrazioni sono prodotte dalla forza di corpi sferici della condizione già descritta, e i corpi attratti sono sfere della stessa condizione.

### Scolio (i due casi notevoli e il metodo generale)

**[S12.45]** Ho ormai esposto i due casi più notevoli delle attrazioni: quando le forze centripete decrescono in rapporto duplicato delle distanze o crescono in rapporto semplice delle distanze. In entrambi i casi esse fanno sì che i corpi girino in sezioni coniche, e compongono forze centripete dei corpi sferici che, allontanandosi dal centro, decrescono o crescono secondo la stessa legge di esse stesse: il che è degno di nota. Percorrere uno per uno gli altri casi, che presentano conclusioni meno eleganti, sarebbe lungo. Preferirei comprenderli e determinarli tutti insieme con un metodo generale, come segue.

### Lemma XXIX (rapporto ultimo di Dd a Ff)

**[S12.46]** **Se con centro S si descrive un cerchio qualsiasi AEB, e con centro P due cerchi EF, ef, che taglino il primo in E, e e la linea PS in F, f; e su PS si abbassano le perpendicolari ED, ed: dico che, se si intende che la distanza degli archi EF, ef diminuisca all’infinito, il rapporto ultimo della linea evanescente Dd alla linea evanescente Ff è quello della linea PE alla linea PS.**

**[S12.47]** Se infatti la linea Pe taglia l’arco EF in q, e la retta Ee, che coincide con l’arco evanescente Ee, prolungata incontra la retta PS in T, e da S si abbassa su PE la normale SG, per la similitudine dei triangoli DTE, dTe, DES, Dd starà a Ee come DT sta a TE, ossia come DE sta a ES; e, poiché i triangoli Eeq, ESG sono simili (per il Lemma VIII e per il Cor. 3 del Lemma VII), Ee starà a eq, ossia a Ff, come ES sta a SG; e, per uguaglianza, Dd starà a Ff come DE sta a SG, cioè (per la similitudine dei triangoli PDE, PGS) come PE sta a PS. C.V.D.

### Proposizione LXXIX. Teorema XXXIX (forza di una lamina sferica concavo-convessa)

**[S12.48]** **Se una superficie EFfe, che per la larghezza diminuita all’infinito sta ormai per svanire, descrive, ruotando intorno all’asse PS, un solido sferico concavo-convesso, alle cui singole particelle uguali tendono forze centripete uguali, dico che la forza con cui quel solido tira un corpuscolo situato in P sta nel rapporto composto dal rapporto del solido DE²×Ff e dal rapporto della forza con cui una particella data, nel luogo Ff, tirerebbe lo stesso corpuscolo.**

**[S12.49]** Se infatti consideriamo dapprima la forza della superficie sferica FE, che è generata dalla rotazione dell’arco FE ed è tagliata in un punto qualsiasi r dalla linea de, la parte anulare della superficie generata dalla rotazione dell’arco rE sarà come la lineetta Dd, restando fisso il raggio PE della sfera (come ha dimostrato Archimede nel libro *Sulla sfera e il cilindro*). E la forza di questa, esercitata lungo le linee PE o Pr situate tutt’intorno sulla superficie conica, è come questa stessa parte anulare della superficie, cioè come la lineetta Dd, oppure, il che è lo stesso, come il rettangolo compreso fra il raggio dato PE della sfera e quella lineetta Dd; ma lungo la linea PS, che tende al centro S, è minore nel rapporto di PD a PE, e perciò è come PD×Dd. Si intenda ora divisa la linea DF in innumerevoli particelle uguali, ciascuna delle quali si chiami Dd; e la superficie FE sarà divisa in altrettanti anelli uguali, le cui forze saranno come la somma di tutti i PD×Dd, cioè come ½PF² − ½PD², e perciò come DE². Si moltiplichi ora la superficie FE per l’altezza Ff; e la forza del solido EFfe esercitata sul corpuscolo P diventerà come DE²×Ff: s’intende, se è data la forza che una particella data Ff esercita sul corpuscolo P alla distanza PF. Ma se quella forza non è data, la forza del solido EFfe diventerà come il solido DE²×Ff e quella forza non data, considerati congiuntamente. C.V.D.

### Proposizione LXXX. Teorema XL (l’area ANB misura l’attrazione della sfera)

**[S12.50]** **Se alle singole particelle uguali di una sfera AEB, descritta con centro S, tendono forze centripete uguali, e sull’asse AB della sfera, nel quale è collocato un corpuscolo P, si innalzano dai singoli punti D le perpendicolari DE, che incontrano la sfera in E, e su di esse si prendono le lunghezze DN, che siano come la quantità DE²×PS/PE e la forza che una particella della sfera situata sull’asse esercita sul corpuscolo P alla distanza PE, considerate congiuntamente: dico che la forza totale con cui il corpuscolo P è tirato verso la sfera è come l’area ANB, compresa fra l’asse AB della sfera e la linea curva ANB che il punto N tocca continuamente.**

**[S12.51]** Infatti, ferme restando le costruzioni fatte nel lemma e nel teorema immediatamente precedenti, immagina che l’asse AB della sfera sia diviso in innumerevoli particelle uguali Dd, e che la sfera intera sia divisa in altrettante lamine sferiche concavo-convesse EFfe; e s’innalzi la perpendicolare dn. Per il teorema precedente, la forza con cui la lamina EFfe tira il corpuscolo P è come DE²×Ff e la forza di una sola particella esercitata alla distanza PE o PF, considerate congiuntamente. Ma (per il lemma precedente) Dd sta a Ff come PE sta a PS, e quindi Ff è uguale a PS×Dd/PE, e DE²×Ff è uguale a Dd moltiplicato per DE²×PS/PE; e perciò la forza della lamina EFfe è come Dd moltiplicato per DE²×PS/PE e la forza della particella esercitata alla distanza PF, considerate congiuntamente, cioè (per ipotesi) come DN×Dd, ossia come l’area evanescente DNnd. Le forze di tutte le lamine esercitate sul corpo P sono dunque come tutte le aree DNnd, cioè la forza totale della sfera è come l’area totale ANB. C.V.D.

**[S12.52]** *Cor. 1.* Di qui, se la forza centripeta che tende alle singole particelle rimane sempre la stessa a tutte le distanze, e si fa DN come DE²×PS/PE, la forza totale con cui il corpuscolo è attratto dalla sfera sarà come l’area ANB.

**[S12.53]** *Cor. 2.* Se la forza centripeta delle particelle è inversamente come la distanza del corpuscolo da esse attratto, e si fa DN come DE²×PS/PE², la forza con cui il corpuscolo P è attratto dalla sfera intera sarà come l’area ANB.

**[S12.54]** *Cor. 3.* Se la forza centripeta delle particelle è inversamente come il cubo della distanza del corpuscolo da esse attratto, e si fa DN come DE²×PS/PE⁴, la forza con cui il corpuscolo è attratto dalla sfera intera sarà come l’area ANB.

**[S12.55]** *Cor. 4.* E in generale, se si pone che la forza centripeta che tende alle singole particelle della sfera sia inversamente come la quantità V, e si fa DN come DE²×PS/(PE×V), la forza con cui il corpuscolo è attratto dalla sfera intera sarà come l’area ANB.

### Proposizione LXXXI. Problema XLI (misura dell’area ANB)

**[S12.56]** **Ferme restando le cose già poste, si deve misurare l’area ANB.**

**[S12.57]** Dal punto P si conduca la retta PH tangente alla sfera in H; e, abbassata sull’asse PAB la normale HI, si divida PI a metà in L; e sarà (per la Prop. XII del libro II degli *Elementi*) PE² uguale a PS² + SE² + 2PSD. Ma SE², ossia SH², è uguale (per la similitudine dei triangoli SPH, SHI) al rettangolo PSI. Dunque PE² è uguale al rettangolo compreso fra PS e PS + SI + 2SD, cioè fra PS e 2LS + 2SD, cioè fra PS e 2LD. Inoltre DE² è uguale a SE² − SD², ossia a SE² − LS² + 2SLD − LD², cioè a 2SLD − LD² − ALB. Infatti LS² − SE², ossia LS² − SA², è uguale (per la Prop. VI del libro II degli *Elementi*) al rettangolo ALB. Si scriva dunque 2SLD − LD² − ALB al posto di DE²; e la quantità DE²×PS/(PE×V), che secondo il quarto corollario della proposizione precedente è come la lunghezza dell’ordinata DN, si risolverà in tre parti: 2SLD×PS/(PE×V) − LD²×PS/(PE×V) − ALB×PS/(PE×V). Se qui al posto di V si scrive il rapporto inverso della forza centripeta, e al posto di PE la media proporzionale fra PS e 2LD, quelle tre parti diventeranno le ordinate di altrettante curve, le cui aree si conoscono con i metodi comuni. C.V.F.

**[S12.58]** *Esempio 1.* Se la forza centripeta che tende alle singole particelle della sfera è inversamente come la distanza, al posto di V scrivi la distanza PE; poi 2PS×LD al posto di PE²; e DN diventerà come SL − ½LD − ALB/2LD. Poni DN uguale al suo doppio, 2SL − LD − ALB/LD: la parte data dell’ordinata, 2SL, condotta lungo la lunghezza AB, descriverà l’area rettangolare 2SL×AB; e la parte indefinita LD, condotta perpendicolarmente lungo la stessa lunghezza con moto continuo, con la legge che durante il moto, crescendo o decrescendo, sia sempre uguale alla lunghezza LD, descriverà l’area (LB² − LA²)/2, cioè l’area SL×AB; che, sottratta dall’area precedente 2SL×AB, lascia l’area SL×AB. La terza parte, ALB/LD, condotta anch’essa perpendicolarmente lungo la stessa lunghezza con moto locale, descriverà un’area iperbolica; che, sottratta dall’area SL×AB, lascerà l’area cercata ANB. Di qui risulta la seguente costruzione del problema. Nei punti L, A, B innalza le perpendicolari Ll, Aa, Bb, delle quali Aa sia uguale a LB e Bb a LA. Con gli asintoti Ll, LB si descriva per i punti a, b l’iperbole ab. E la corda ba, una volta condotta, racchiuderà un’area aba uguale all’area cercata ANB.

**[S12.59]** *Esempio 2.* Se la forza centripeta che tende alle singole particelle della sfera è inversamente come il cubo della distanza, o (il che è lo stesso) come quel cubo diviso per un piano dato qualsiasi, scrivi PE³/2AS² al posto di V, poi 2PS×LD al posto di PE²; e DN diventerà come SL×AS²/(PS×LD) − AS²/2PS − ALB×AS²/(2PS×LD²), cioè (poiché PS, AS, SI sono in proporzione continua) come LSI/LD − ½SI − ALB×SI/2LD². Se le tre parti di questa si conducono lungo la lunghezza AB, la prima, LSI/LD, genererà un’area iperbolica; la seconda, ½SI, l’area ½AB×SI; la terza, ALB×SI/2LD², l’area ALB×SI/2LA − ALB×SI/2LB, cioè ½AB×SI. Dalla prima si sottragga la somma della seconda e della terza, e rimarrà l’area cercata ANB. Di qui risulta la seguente costruzione del problema. Nei punti L, A, S, B innalza le perpendicolari Ll, Aa, Ss, Bb, delle quali Ss sia uguale a SI; e per il punto s, con gli asintoti Ll, LB, si descriva l’iperbole asb, che incontri le perpendicolari Aa, Bb in a e b; e il rettangolo 2ASI, sottratto dall’area iperbolica AasbB, lascerà l’area cercata ANB.

**[S12.60]** *Esempio 3.* Se la forza centripeta che tende alle singole particelle della sfera decresce in rapporto quadruplicato della distanza dalle particelle, scrivi PE⁴/2AS³ al posto di V, poi √(2PS×LD) al posto di PE; e DN diventerà come (SI²×SL/√(2SI)) × 1/√LD³ − (SI²/2√(2SI)) × 1/√LD − (SI²×ALB/2√(2SI)) × 1/√LD⁵. Le sue tre parti, condotte lungo la lunghezza AB, producono altrettante aree, cioè: 2SI²×SL/√(2SI) moltiplicato per (1/√LA − 1/√LB); SI²/√(2SI) moltiplicato per (√LB − √LA); e SI²×ALB/(3√(2SI)) moltiplicato per (1/√LA³ − 1/√LB³). E queste, dopo la debita riduzione, diventano 2SI²×SL/LI, SI² e SI² + 2SI³/3LI. E queste, sottratte le ultime dalla prima, danno 4SI³/3LI. Perciò la forza totale con cui il corpuscolo P è tirato verso il centro della sfera è come SI³/PI, cioè inversamente come PS³×PI. C.V.T.

**[S12.61]** Con lo stesso metodo si può determinare l’attrazione di un corpuscolo situato all’interno della sfera, ma più speditamente con il teorema seguente.

### Proposizione LXXXII. Teorema XLI (corpuscolo interno e punto esterno corrispondente)

**[S12.62]** **In una sfera descritta con centro S e raggio SA, se si prendono SI, SA, SP in proporzione continua, dico che l’attrazione di un corpuscolo all’interno della sfera, in un luogo qualsiasi I, sta alla sua attrazione all’esterno della sfera, nel luogo P, nel rapporto composto dal rapporto subduplicato delle distanze dal centro IS, PS e dal rapporto subduplicato delle forze centripete che tendono al centro in quei luoghi P e I.**

**[S12.63]** Così, se le forze centripete delle particelle della sfera sono inversamente come le distanze del corpuscolo da esse attratto, la forza con cui il corpuscolo situato in I è tirato dalla sfera intera starà alla forza con cui è tirato in P nel rapporto composto dal rapporto subduplicato della distanza SI alla distanza SP e dal rapporto subduplicato della forza centripeta nel luogo I, originata da una particella qualsiasi nel centro, alla forza centripeta nel luogo P, originata dalla stessa particella nel centro, cioè dal rapporto subduplicato inverso delle distanze SI, SP fra loro. Questi due rapporti subduplicati compongono il rapporto di uguaglianza, e perciò le attrazioni prodotte in I e in P dalla sfera intera sono uguali. Con un calcolo simile, se le forze delle particelle della sfera sono inversamente in rapporto duplicato delle distanze, si ricaverà che l’attrazione in I sta all’attrazione in P come la distanza SP sta al semidiametro SA della sfera; se quelle forze sono inversamente in rapporto triplicato delle distanze, le attrazioni in I e in P staranno fra loro come SP² sta a SA²; se in rapporto quadruplicato, come SP³ sta a SA³. Perciò, poiché l’attrazione in P, in quest’ultimo caso, è stata trovata inversamente come PS³×PI, l’attrazione in I sarà inversamente come SA³×PI, cioè (poiché SA³ è dato) inversamente come PI. E il procedimento è simile all’infinito. Il teorema, poi, si dimostra così.

**[S12.64]** Ferme restando le costruzioni fatte prima, ed essendo il corpo in un luogo qualsiasi P, l’ordinata DN è stata trovata come DE²×PS/(PE×V). Dunque, se si conduce IE, quell’ordinata, per un altro luogo qualsiasi I del corpuscolo, mutando ciò che va mutato, diventerà come DE²×IS/(IE×V). Poni che le forze centripete emananti da un punto qualsiasi E della sfera stiano fra loro, alle distanze IE, PE, come PEⁿ sta a IEⁿ (dove il numero n indica l’indice delle potenze di PE e di IE); e quelle ordinate diventeranno come DE²×PS/(PE×PEⁿ) e DE²×IS/(IE×IEⁿ), il cui rapporto reciproco è come PS×IE×IEⁿ sta a IS×PE×PEⁿ. Poiché, essendo SI, SE, SP in proporzione continua, i triangoli SPE, SEI sono simili, e quindi IE sta a PE come IS sta a SE, ossia a SA, al posto del rapporto di IE a PE scrivi il rapporto di IS a SA; e il rapporto delle ordinate diventerà quello di PS×IEⁿ a SA×PEⁿ. Ma il rapporto di PS a SA è il subduplicato del rapporto delle distanze PS, SI; e il rapporto di IEⁿ a PEⁿ (poiché IE sta a PE come IS sta a SA) è il subduplicato del rapporto delle forze alle distanze PS, IS. Dunque le ordinate, e perciò le aree che le ordinate descrivono e le attrazioni proporzionali a esse, stanno nel rapporto composto da quei rapporti subduplicati. C.V.D.

### Proposizione LXXXIII. Problema XLII (corpuscolo nel centro e segmento sferico)

**[S12.65]** **Trovare la forza con cui un corpuscolo collocato nel centro di una sfera è attratto verso un suo segmento qualsiasi.**

**[S12.66]** Sia P il corpo nel centro della sfera, e RBSD un suo segmento, delimitato dal piano RDS e dalla superficie sferica RBS. Con una superficie sferica EFG descritta con centro P si tagli DB in F, e si divida il segmento nelle parti BREFGS, FEDG. Quella superficie, poi, non sia puramente matematica, ma fisica, con una profondità piccolissima. Si chiami O questa profondità: questa superficie sarà (per quanto è stato dimostrato da Archimede) come PF×DF×O. Poniamo inoltre che le forze attrattive delle particelle della sfera siano inversamente come quella potenza delle distanze il cui indice è n; e la forza con cui la superficie EFG tira il corpo P sarà (per la Prop. LXXIX) come DE²×O/PFⁿ, cioè come 2DF×O/PFⁿ⁻¹ − DF²×O/PFⁿ. A questa sia proporzionale la perpendicolare FN moltiplicata per O; e l’area curvilinea BDI, che l’ordinata FN descrive condotta con moto continuo lungo la lunghezza DB, sarà come la forza totale con cui l’intero segmento RBSD tira il corpo P. C.V.T.

### Proposizione LXXXIV. Problema XLIII (corpuscolo sull’asse di un segmento)

**[S12.67]** **Trovare la forza con cui un corpuscolo, collocato fuori del centro della sfera sull’asse di un segmento qualsiasi, è attratto da quel segmento.**

**[S12.68]** Dal segmento EBK sia tirato il corpo P, collocato sul suo asse ADB. Con centro P e raggio PE si descriva la superficie sferica EFK, che divida il segmento in due parti, EBKFE ed EFKDE. Si cerchi la forza della prima parte per la Prop. LXXXI e quella della seconda per la Prop. LXXXIII: la somma delle forze sarà la forza dell’intero segmento EBKDE. C.V.T.

### Scolio (passaggio ai corpi non sferici)

**[S12.69]** Spiegate le attrazioni dei corpi sferici, si potrebbe ora procedere alle leggi delle attrazioni di certi altri corpi costituiti in modo simile di particelle attrattive; ma trattarle partitamente non riguarda molto il mio proposito. Basterà aggiungere alcune proposizioni più generali sulle forze di corpi di questo genere e sui moti che ne derivano, per una certa utilità che esse hanno nelle questioni di filosofia naturale.

**Fine della Sezione XII. Nel testo originale segue la Sezione XIII, *De corporum non sphæricorum viribus attractivis*.**

---

## Apparato

### A.0 Estensioni del glossario

I termini seguenti non comparivano nel glossario comune. Ognuno è reso in modo costante in tutto il fascicolo.

| Latino | Italiano | Motivazione |
|---|---|---|
| *corpusculum* | «corpuscolo» | Termine tecnico di Newton per il corpo attratto, pensato come puntiforme. Si distingue da *corpus* («corpo»), che Newton usa a volte per lo stesso oggetto (S12.02, S12.11): la differenza è conservata. |
| *superficies* (plurale) | «superfici» | Plurale moderno; al singolare resta «superficie sferica» del glossario. |
| *orbis*, *orbes* (S12.12) | «guscio», «gusci» | **Deroga motivata** al glossario (*orbis* «orbita»): qui *orbes* non sono traiettorie ma strati sferici sottilissimi di cui si compone la sfera. «Orbite» sarebbe un errore di senso. Motte: «orbs». |
| *lamina sphærica concavo-convexa* | «lamina sferica concavo-convessa» | Calco; la lamina è il guscio sottile EFfe centrato nel corpuscolo (Propp. LXXIX–LXXX). |
| *annulus*, *pars annularis* | «anello», «parte anulare» | |
| *superficies circularis* (S12.04) | «superficie circolare» | È la zona (anello di superficie) generata dalla rotazione di un arco intorno al diametro; il testo lo dice subito dopo. Si conserva il termine di Newton. |
| *lineola* | «lineetta» | Diminutivo di *linea*: segmento evanescente. Motte conserva *lineola*. |
| *convolutio* | «rotazione» | *Convolutione semicirculi circa diametrum*: «con la rotazione del semicerchio intorno al diametro». |
| *intervallum* (*centro S, intervallo SP*) | «raggio» | Formula euclidea della descrizione del cerchio; in Prop. LXXXII *intervallo SA* è il raggio della sfera. |
| *similaris*, *dissimilaris* | «similare», «dissimilare» | Fatto di parti simili, cioè omogeneo. Si tiene distinto da *homogeneus* «omogeneo», che Newton usa a parte (S12.15, S12.17, S12.20). Nella Prop. LXXVI *similares in progressu per circuitum* significa: uguali in tutte le direzioni a una data distanza dal centro. |
| *inæquabilis* | «non uniforme» | S12.42. |
| *in progressu a centro … / per circuitum* | «procedendo dal centro … / lungo il giro» | Si conserva l’immagine del percorso. |
| *trahere* / *attrahere* | «tirare» / «attrarre» | Newton alterna i due verbi; la distinzione lessicale è conservata. |
| *virtus attractiva* | «virtù attrattiva» | S12.30; termine dell’epoca, senza connotazioni moderne. |
| *applicare ad* | «dividere per» | Simmetrico di *ducere in* «moltiplicare per» del glossario: *sphæræ applicatæ ad quadrata distantiarum* = le sfere divise per i quadrati delle distanze. |
| *ducere in … per motum continuum / localem* | «condurre lungo … con moto continuo / locale» | **Eccezione motivata** a *ducere in* «moltiplicare per». In S12.58–S12.60 e S12.66 l’ordinata «condotta» lungo la lunghezza AB o DB descrive un’area: è la generazione cinematica di un’area da un segmento in moto, non un prodotto. Dove invece *ducere in* indica un prodotto (S12.36, S12.40, S12.49 *Ducatur superficies FE in altitudinem Ff*, S12.66 *FN ductum in O*) si usa «moltiplicare per». |
| *contentum sub*, *rectangulum sub*, *solidum quod continetur sub* | «compreso fra» | Il rettangolo o il solido «compreso fra» due grandezze è il loro prodotto. |
| *ex æquo* | «per uguaglianza» | È l’*ex æquali* di Euclide (Elementi V, def. 17): da A:B = C:D e B:E = D:F segue A:E = C:F. |
| *conjunctis rationibus* | «congiungendo i rapporti» | Participio; non si usa la formula fissa «considerate congiuntamente», riservata all’avverbio *conjunctim*. |
| *componendo*, *dividendo*, *per compositionem* | «componendo», «dividendo», «per composizione» | Termini della teoria delle proporzioni, ancora correnti nella didattica italiana. In S12.14 e S12.25 indicano, in pratica, la somma e la differenza delle forze. |
| *ratio quadruplicata* | «rapporto quadruplicato» | Prosegue la serie del glossario: quarta potenza (S12.60, S12.63). |
| *ratio simplex* | «rapporto semplice» | S12.45: proporzionalità diretta alla prima potenza. |
| *continue proportionales* | «in proporzione continua» | SI : SA = SA : SP. |
| *medium proportionale* | «media proporzionale» | S12.57. |
| *dignitas*, *index* | «potenza», «indice» | *Dignitas cujus index est n*: la potenza di esponente n. Si conserva «indice», come nel latino; l’equivalente moderno è «esponente». |
| *area hyperbolica*, *asymptotus* | «area iperbolica», «asintoto» | |
| *profunditas* | «profondità» | S12.66: lo spessore del guscio fisico. |
| *attractio acceleratrix / motrix* | «attrazione acceleratrice / motrice» | Per analogia con *vis acceleratrix / motrix* del glossario (S12.26, S12.28). |
| *pondus* | «peso» | S12.28. |
| *perpetuo tangit* | «tocca continuamente» | S12.50: il punto N «tocca» la curva in ogni sua posizione, cioè la descrive. Motte parafrasa: «the locus of the point N». |
| *mutatis mutandis* | «mutando ciò che va mutato» | |
| *in rebus philosophicis* | «nelle questioni di filosofia naturale» | S12.69: *philosophia* è qui la filosofia naturale. |

### A.1 Proposizione LXX (S12.01–S12.02)

**Latino:** *Si ad sphæricæ superficiei puncta singula tendant vires æquales centripetæ decrescentes in duplicata ratione distantiarum a punctis: dico quod corpusculum intra superficiem constitutum his viribus nullam in partem attrahitur.*

**Inglese:** “If to every point of a sphærical surface there tend equal centripetal forces decreasing in the duplicate ratio of the distances from those points; I say, that a corpuscle placed within that superficies will not be attracted by those forces any way.”

**Scelte.**

- *vires æquales centripetæ … ad puncta singula*: «forze centripete uguali» che tendono ai singoli punti. «Uguali» significa: a parità di distanza, ogni punto attrae con la stessa forza (nota N1).
- *nullam in partem attrahitur*: «non è attratto verso alcuna parte», cioè la risultante è nulla.
- *arcus quam minimos*: «archi piccolissimi»; il superlativo con *quam* indica grandezze che si fanno tendere a zero (Sezione I).
- *corpus P* nella chiusa: Newton passa da *corpusculum* a *corpus*; la traduzione segue.
- *impellitur* (chiusa): «è spinto», secondo il glossario.

### A.2 Proposizione LXXI (S12.03–S12.04)

**Latino:** *Iisdem positis, dico quod corpusculum extra sphæricam superficiem constitutum attrahitur ad centrum sphæræ, vi reciproce proportionali quadrato distantiæ suæ ab eodem centro.* (la trascrizione spezza *reci <190> proce* a cambio di pagina).

**Inglese:** “The same things supposed as above, I say, that a corpuscle placed without the sphærical superficies is attracted towards the centre of the sphere with a force reciprocally proportional to the square of its distance from that centre.”

**Scelte.**

- *auferentes … æquales arcus HK, hk & IL, il*: «che taglino … archi uguali». Gli archi uguali equivalgono alla condizione SD = sd, SE = se, ribadita alla fine (*capiendo semper sd æqualem SD*).
- *pro æqualibus habeantur*: «si considerino uguali»; la giustificazione (*quippe quarum ratio ultima … est æqualitatis*) è resa con «il loro rapporto ultimo … è infatti di uguaglianza».
- *partes obliquas*: «parti oblique». Newton chiama così le componenti lungo PS, ps; il termine è conservato.
- **Formula appiattita:** *ut PF×pf×psPS ad pf×PF×PSps* è letta (PF×pf×ps)/PS : (pf×PF×PS)/ps, come in Motte (SVG 256–257); il risultato ps² : PS² lo conferma.
- *per legum corol 2.* (senza punto dopo *corol*): grafia della trascrizione; rimando reso «per il Cor. 2 delle leggi».

### A.3 Proposizione LXXII e corollari (S12.05–S12.09)

**Latino:** *Si ad sphæræ cujusvis puncta singula tendant vires æquales centripetæ decrescentes in duplicata ratione distantiarum a punctis; ac detur tum sphæræ densitas, tum ratio diametri sphæræ ad distantiam corpusculi a centro ejus: dico quod vis, qua corpusculum attrahitur, proportionalis erit semidiametro sphæræ.*

**Inglese:** “If to the several points of a sphere there tend equal centripetal forces decreasing in a duplicate ratio of the distances from those points; and there be given both the density of the sphere and the ratio of the diameter of the sphere to the distance of the corpuscle from its centre; I say, that the force with which the corpuscle is attracted is proportional to the semi-diameter of the sphere.”

**Scelte.**

- *concipe* (imperativo di seconda persona) è conservato: «immagina».
- *ratio prior directe una cum ratione posteriore bis inverse*: «il primo rapporto preso direttamente, insieme con il secondo preso due volte inversamente»: (D³) × (1/D²) = D.
- Cor. 2, *Constant hæc duo*: «queste due cose risultano». Motte esplicita «These two Corollaries».

### A.4 Proposizione LXXIII e Scolio (S12.10–S12.12)

**Latino:** *Si ad sphæræ alicujus datæ puncta singula tendant æquales vires centripetæ decrescentes in duplicata ratione distantiarum a punctis: dico quod corpusculum intra sphæram constitutum attrahitur vi proportionali distantiæ suæ ab ipsius centro.*

**Inglese:** “If to the several points of a given sphere there tend equal centripetal forces decreasing in a duplicate ratio of the distances from the points; I say, that a corpuscle placed within the sphere is attracted by a force proportional to its distance from the centre.”

**Scelte.**

- *sphærarum differentia AEBF*: «la differenza AEBF delle sfere», cioè il guscio fra la sfera ABCD e la sfera interna PEQF. Le lettere E, F compaiono sia in PEQF sia in AEBF: in assenza della figura non è chiaro se indichino gli stessi punti. Si conservano come nel latino.
- Scolio: *orbes* «gusci» (§ A.0); *instar nihili* «come nulla»; *magnitudinis contemnendæ* «di grandezza trascurabile».

### A.5 Proposizione LXXIV e corollari (S12.13–S12.17)

**Latino:** *Iisdem positis, dico quod corpusculum extra sphæram constitutum attrahitur vi reciproce proportionali quadrato distantiæ suæ ab ipsius centro.*

**Inglese:** “The same things supposed, I say, that a corpuscle situate without the sphere is attracted with a force reciprocally proportional to the square of its distance from the centre.”

**Scelte.** *Componendo* «componendo» (§ A.0). Cor. 2: *sphæræ applicatæ ad quadrata distantiarum* «le sfere divise per i quadrati delle distanze» (§ A.0). Cor. 3 è l’inverso del teorema: Newton lo enuncia senza dimostrazione (nota N4).

### A.6 Proposizione LXXV e corollari (S12.18–S12.23)

**Latino:** *Si ad sphæræ datæ puncta singula tendant vires æquales centripetæ, decrescentes in duplicata ratione distantiarum a punctis; dico quod sphæra quævis alia similaris ab eadem attrahitur vi reciproce proportionali quadrato distantiæ centrorum.*

**Inglese:** “If to the several points of a given sphere there tend equal centripetal forces decreasing in a duplicate ratio of the distances from the points; I say, that another similar sphere will be attracted by it with a force reciprocally proportional to the square of the distance of the centres.”

**Scelte.**

- *similaris* «similare» (§ A.0). Motte traduce «similar», che in inglese può far pensare a sfere geometricamente simili: il latino intende sfere fatte di parti simili, cioè omogenee.
- *vicissim*: «a sua volta»; *si modo*: «se» (condizione ipotetica).
- Cor. 2, *per legem 3.*: «per la Legge III». *Geminabitur*: «sarà raddoppiata».
- Cor. 3–4: *circa umbilicum* «intorno al fuoco», *circa centrum* «intorno al centro» delle sezioni coniche (nota N6).

### A.7 Proposizione LXXVI e corollari (S12.24–S12.34)

**Latino:** *Si sphæræ in progressu a centro ad circumferentiam (quod materiæ densitatem & vim attractivam) utcunque dissimilares, in progressu vero per circuitum ad datam omnem a centro distantiam sunt undique similares; & vis attractiva puncti cujusque decrescit in duplicata ratione distantiæ corporis attracti: dico quod vis tota, qua hujusmodi sphæra una attrahit aliam, sit reciproce proportionalis quadrato distantiæ centrorum.*

**Inglese:** “If spheres be however dissimilar (as to density of matter and attractive force) in the same ratio onward from the centre to the circumference; but every where similar, at every given distance from the centre, on all sides round about; and the attractive force of every point decreases in the duplicate ratio of the distance of the body attracted; I say, that the whole force with which one of these spheres attracts the other will be reciprocally proportional to the square of the distance of the centres.”

**Scelte.**

- **Refuso probabile:** *(quod materiæ densitatem …)*. Il senso richiede *quoad*, «quanto a», e così intende anche Motte («as to»). Tradotto secondo il senso; da verificare sulla stampa.
- Nella trascrizione manca il verbo della protasi (*utcunque dissimilares* … *sunt*): *sunt* è sottinteso dal secondo membro. La traduzione lo esplicita.
- **Errore di Motte:** «however dissimilar … **in the same ratio** onward from the centre». *In the same ratio* non è nel latino e contraddice *utcunque* («in modo qualsiasi»).
- *singulæ singulas*: «ciascuna delle prime ciascuna delle seconde».
- *formam quamvis optatam*: «qualsiasi forma desiderata». *Forma* indica qui la costituzione interna della sfera (distribuzione della densità), non la figura esterna, che resta sferica.
- Cor. 3, *contenta sub sphæris per multiplicationem producta*: «i prodotti ottenuti moltiplicando le sfere fra loro».

### A.8 Proposizione LXXVII (S12.35–S12.41)

**Latino:** *Si ad singula sphærarum puncta tendant vires centripetæ proportionales distantiis punctorum a corporibus attractis: dico quod vis composita, qua sphæræ duæ se mutuo trahent, est ut distantia inter centra sphærarum.*

**Inglese:** “If to the several points of spheres there tend centripetal forces proportional to the distances of the points from the attracted bodies; I say, that the compounded force with which two spheres attract each other mutually is as the distance between the centres of the spheres.”

**Scelte.**

- *solidum quod continetur sub plano ipso EF & distantia illa PG*: «il solido compreso fra il piano stesso EF e quella distanza PG» (§ A.0). *Planum* indica qui la sezione piana (il disco) della sfera.
- *ductum in*: «moltiplicato per», secondo il glossario.
- *semissem differentiæ distantiarum*: «la metà della differenza delle distanze».
- Trascrizione: *Cas 3.* senza punto, a differenza degli altri casi; irrilevante.

### A.9 Proposizione LXXVIII, corollario e Scolio (S12.42–S12.45)

**Latino:** *Si sphæræ in progressu a centro ad circumferentiam sint utcunque dissimilares & inæquabiles in progressu vero per circuitum ad datam omnem a centro distantiam sint undique similares; & vis attractiva puncti cujusque sit ut distantia corporis attracti: dico quod vis tota qua hujusmodi sphæræ duæ se mutuo trahunt sit proportionalis distantiæ inter centra sphærarum.*

**Inglese:** “If spheres in the progress from the centre to the circumference be however dissimilar and unequable, but similar on every side round about at all given distances from the centre; and the attractive force of every point be as the distance of the attracted body; I say, that the entire force with which two spheres of this kind attract each other mutually is proportional to the distance between the centres of the spheres.”

**Scelte.**

- Nella trascrizione manca una virgola prima di *in progressu vero*; la lettura non cambia.
- Cor.: *in propositionibus x. & lxiv.* «nelle Propp. X e LXIV».
- Scolio: *componentes … vires centripetas eadem lege … decrescentes vel crescentes cum seipsis* è reso «compongono forze centripete dei corpi sferici che … decrescono o crescono secondo la stessa legge di esse stesse». *Malim* (congiuntivo potenziale): «preferirei».

### A.10 Lemma XXIX (S12.46–S12.47)

**Latino:** *Si describantur centro S circulus quilibet AEB, & centro P circuli duo EF, ef, secantes priorem in E, e, lineamque PS in F, f; & ad PS demittantur perpendicula ED, ed: dico quod, si distantia arcuum EF, ef in infinitum minui intelligatur, ratio ultima lineæ evanescentis Dd ad lineam evanescentem Ff ea sit, quæ lineæ PE ad lineam PS.*

**Inglese:** “If about the centre S there be described any circle as AEB, and about the centre P there be also described two circles EF, ef, cutting the first in E and e, and the line PS in F and f; and there be let fall to PS the perpendiculars ED, ed; I say, that if the distance of the arcs EF, ef be supposed to be infinitely diminished, the last ratio of the evanescent line Dd to the evanescent line Ff is the same as that of the line PE to the line PS.”

**Scelte.**

- **Refuso probabile della trascrizione:** *ob similia triangula DTE, dte, DES*. T è un punto unico, intersezione della retta Ee con PS; non esiste un punto t. Va letto **dTe**, come in Motte. Tradotto secondo il senso; da verificare sulla stampa.
- *per lem. viii. & corol. 3. lem. vii.*: «per il Lemma VIII e per il Cor. 3 del Lemma VII».

### A.11 Proposizione LXXIX (S12.48–S12.49)

**Latino:** *Si superficies ob latitudinem infinite diminutam jamjam evanescens EFfe, convolutione sui circa axem PS, describat solidum sphæricum concavo-convexum, ad cujus particulas singulas æquales tendant æquales vires centripetæ: dico quod vis, qua solidum illud trahit corpusculum situm in P, est in ratione composita ex ratione solidi DE q×Ff & ratione vis qua particula data in loco Ff traheret idem corpusculum.*

**Inglese:** “Suppose a superficies as EFfe to have its breadth infinitely diminished, and to be just vanishing; and that the same superficies by its revolution round the axis PS describes a sphærical concavo-convex solid, to the several equal particles of which there tend equal centripetal forces; I say, that the force with which that solid attracts a corpuscle situate in P is in a ratio compounded of the ratio of the solid DE2 × Ff and the ratio of the force with which the given particle in the place Ff would attract the same corpuscle.”

**Scelte.**

- *jamjam evanescens*: «che sta ormai per svanire».
- *uti demonstravit Archimedes in lib. de Sphæra & Cylindro*: «come ha dimostrato Archimede nel libro *Sulla sfera e il cilindro*» (zona sferica, nota N10).
- **Formula appiattita:** *12PFq−12PDq* = ½PF² − ½PD² (Motte, SVG 258).
- *puta si detur*: «s’intende, se è data».

### A.12 Proposizione LXXX e corollari (S12.50–S12.55)

**Latino:** *Si ad sphæræ alicujus AEB, centro S descriptæ, particulas singulas æquales tendant æquales vires centripetæ, & ad sphæræ axem AB, in quo corpusculum aliquod P locatur, erigantur de punctis singulis D perpendicula DE, sphæræ occurentia in E, & in ipsis capiantur longitudines DN, quæ sint ut quantitas DE q×PSPE & vis, quam sphæræ particula sita in axe ad distantiam PE exercet in corpusculum P, conjunctim: dico quod vis tota, qua corpusculum P trahitur versus sphæram, est ut area ANB comprehensa sub axe sphæræ AB, & linea curva ANB, quam punctum N perpetuo tangit.*

**Inglese:** “If to the several equal parts of a sphere ABE described about the centre S there tend equal centripetal forces; and from the several points D in the axis of the sphere AB in which a corpuscle, as P, is placed, there be erected the perpendiculars DE meeting the sphere in E, and if in those perpendiculars the lengths DN be taken as the quantity [SVG 259], and as the force which a particle of the sphere situate in the axis exerts at the distance PE upon the corpuscle P conjunctly; I say, that the whole force with which the corpuscle P is attracted towards the sphere is as the area ANB, comprehended under the axis of the sphere AB, and the curve line ANB, the locus of the point N.” ([SVG 259] = DE²×PS/PE.)

**Scelte.**

- **Formule appiattite:** *DE q×PSPE* = DE²×PS/PE (SVG 259); *PS×DdPE;&DEq×Ff æquale Dd in DEq×PSPE* = «Ff = PS×Dd/PE, e DE²×Ff = Dd × DE²×PS/PE» (SVG 260–261). Il «;&» è un artefatto della trascrizione.
- Corollari: DE²×PS/PE (Cor. 1), DE²×PS/PE² (Cor. 2), DE²×PS/PE⁴ (Cor. 3, *PEqq*), DE²×PS/(PE×V) (Cor. 4). Tutti coincidono con Motte (SVG 259, 262–264).
- *occurentia*: grafia della trascrizione per *occurrentia*; da verificare sulla stampa (può essere grafia dell’originale).
- Cor. 4, *attahitur*: refuso probabile della trascrizione per *attrahitur*; da verificare sulla stampa.
- *lemmate & theoremate novissimo*: «nel lemma e nel teorema immediatamente precedenti».
- La trascrizione colloca **[FIG 141]** fra la dimostrazione e il Cor. 1, senza un rimando nel testo.

### A.13 Proposizione LXXXI ed esempi (S12.56–S12.61)

**Latino:** *Stantibus jam positis, mensuranda est area ANB.*

**Inglese:** “The things remaining as above, it is required to measure the area ANB.”

**Scelte.**

- *per prop. xii. lib. 2. elem.* e *per prop. vi. lib. 2. elem.*: «per la Prop. XII (VI) del libro II degli *Elementi*» di Euclide.
- *PSq+SEq+2PSD*: il termine «2PSD» è il doppio rettangolo PS×SD (D oltre S rispetto a P; per D dalla parte di P il segno di SD si inverte, cosa che Newton non dice).
- *contento sub PS&PS+SI+2SD*: la «&» separa i due fattori del rettangolo: «fra PS e PS + SI + 2SD».
- *per methodos vulgatas*: «con i metodi comuni», cioè le quadrature note, comprese quelle dell’iperbole (nota N12).
- **Chiusa:** il latino ha **Q.E.F.** (è un problema), Motte ha «Q.E.D.».
- **Esempio 1.** *descrescendo*: refuso probabile per *decrescendo*. *Per puncta ab*: senza virgola nella trascrizione; s’intende «per i punti a, b». *Ducta … per motum localem* (terza parte) diventa in Motte «with a continued motion», come la seconda; il latino varia l’aggettivo.
- **Esempio 2.** *ut cubus ille applicatus ad planum quodvis datum*: «come quel cubo diviso per un piano dato qualsiasi» (dividere per un’area data non cambia la proporzionalità).
- **Esempio 3.** La trascrizione ha *dein 2PS×LD pro PE*: manca il radicale, perché PE è la media proporzionale fra PS e 2LD (S12.57). Letto **√(2PS×LD)**. Motte (SVG 280) stampa **√(2PS + LD)**: il «+» è un errore dell’edizione 1846 (il «×» è richiesto da PE² = 2PS×LD). Anche le altre formule dell’esempio hanno perso radicali e frazioni; sono ricostruite in § A.17 e verificate per integrazione (nota N12).
- *Q.E.I.* (fine dell’Esempio 3): «C.V.T.».

### A.14 Proposizione LXXXII (S12.62–S12.64)

**Latino:** *In sphæra centro S intervallo SA descripta, si capiantur SI, SA, SP continue proportionales: dico quod corpusculi intra sphæram, in loco quovis I, attractio est ad attractionem ipsius extra sphæram, in loco P, in ratione composita ex subduplicata ratione distantiarum a centro IS, PS, & subduplicata ratione virium centripetarum, in locis illis P & I, ad centrum tendentium.*

**Inglese:** “In a sphere described about the centre S with the interval SA, if there be taken SI, SA, SP continually proportional; I say, that the attraction of a corpuscle within the sphere in any place I is to its attraction without the sphere in the place P in a ratio compounded of the subduplicate ratio of IS, PS, the distances from the centre, and the subduplicate ratio of the centripetal forces tending to the centre in those places P and I.”

**Scelte.**

- *in locis illis P & I*: l’ordine P, I dell’enunciato è conservato, ma l’esempio di S12.63 chiarisce che il rapporto delle forze va preso nel luogo I rispetto al luogo P (forza in I : forza in P); con l’ordine inverso il teorema sarebbe falso (nota N13). Motte conserva l’ordine «P and I».
- *allio*: refuso probabile della trascrizione per *alio*; da verificare sulla stampa.
- *Simili computo*: «con un calcolo simile».
- *Theorema XLI*: la Prop. LXXXI è il *Problema XLI*; teoremi e problemi hanno numerazioni separate. Non è un errore.
- *DEq×PSPE×PEn&DEq×ISIE×IEn*: la «&» separa le due ordinate: «DE²×PS/(PE×PEⁿ) e DE²×IS/(IE×IEⁿ)».

### A.15 Proposizioni LXXXIII–LXXXIV (S12.65–S12.68)

**Latino (LXXXIII):** *Invenire vim qua corpusculum in centro sphæræ locatum ad ejus segmentum quodcunque attrahitur.*

**Inglese:** “To find the force with which a corpuscle placed in the centre of a sphere is attracted towards any segment of that sphere whatsoever.”

**Latino (LXXXIV):** *Invenire vim, qua corpusculum, extra centrum sphæræ in axe segmenti cujusvis locatum, attrahitur ab eodem segmento.*

**Inglese:** “To find the force with which a corpuscle, placed without the centre of a sphere in the axis of any segment, is attracted by that segment.”

**Scelte.**

- *per demonstata Archimedis*: refuso probabile per *demonstrata*; «per quanto è stato dimostrato da Archimede».
- **Lettura incerta (LXXXIII).** La trascrizione ha *erit (per prop. lxxix.) ut DFq×OPFn, id est, ut 2DF×OPFn−1.* Letta alla lettera, dà DF²×O/PFⁿ = 2DF×O/PFⁿ⁻¹, che non è un’identità. Per la Prop. LXXIX la forza della calotta è come DE²×O/PFⁿ, e DE² = 2PF×DF − DF² (E sul piano RDS, PE = PF). Motte stampa appunto DE²×O/PFⁿ (SVG 307) = 2DF×O/PFⁿ⁻¹ − DF²×O/PFⁿ (SVG 308). Ho tradotto secondo il senso e secondo Motte. La trascrizione sembra aver perso il secondo termine e scambiato E con F; **da verificare sulla stampa del 1726**.
- *area curvilinea BDI*: le lettere sono conservate. I non è definito nel testo: è presumibilmente l’estremo della curva descritta da N sopra D. Da controllare sulla figura NATP00087-149.
- LXXXIV: *intervallo PE* «raggio PE»; *per prop. lxxxi. & … per prop. lxxxiii* «per la Prop. LXXXI … per la Prop. LXXXIII».

### A.16 Scolio finale (S12.69)

- *jam pergere liceret*: «si potrebbe ora procedere». Motte rende «it comes next in order to treat», che trasforma una possibilità in un programma.
- *minus ad institutum spectat*: «non riguarda molto il mio proposito»; Motte: «is not necessary to my design».
- *aliqualem usum*: «una certa utilità»; Motte: «of some little use».

### A.17 Formule appiattite: letture adottate

Tutte le letture sono state controllate sulle immagini SVG di Motte e, dove possibile, ricalcolate (nota N12).

| Luogo | Trascrizione | Lettura | Motte |
|---|---|---|---|
| S12.04 | *PF×pf×psPS ad pf×PF×PSps* | (PF×pf×ps)/PS : (pf×PF×PS)/ps | SVG 256–257, uguale |
| S12.49 | *12PFq−12PDq* | ½PF² − ½PD² | SVG 258, uguale |
| S12.50 | *DE q×PSPE* | DE²×PS/PE | SVG 259, uguale |
| S12.51 | *PS×DdPE;&DEq×Ff æquale Dd in DEq×PSPE* | Ff = PS×Dd/PE; DE²×Ff = Dd × DE²×PS/PE | SVG 260–261, uguale |
| S12.53–55 | *DEq×PSPEq*, *DEq×PSPEqq*, *DEq×PSPE×V* | DE²×PS/PE², DE²×PS/PE⁴, DE²×PS/(PE×V) | SVG 262–264, uguale |
| S12.57 | *2SLD×PSPE×V− LDq×PSPE×V−ALB×PSPE×V* | 2SLD×PS/(PE×V) − LD²×PS/(PE×V) − ALB×PS/(PE×V) | SVG 265–266, uguale |
| S12.58 | *SL−12LD−ALB2LD*; *2SL−LD−ALBLD*; *LBq−LAq2*; *ALBLD* | SL − ½LD − ALB/2LD; 2SL − LD − ALB/LD; (LB² − LA²)/2; ALB/LD | SVG 267–270, uguale |
| S12.59 | *PE cub.2ASq*; *SL×ASqPS×LD−ASq2PS −ALB×ASq2PS×LDq*; *LSILD−12SI−ALB×SI2LDq*; *ALB×SI2LA−ALB×SI2LB* | PE³/2AS²; SL×AS²/(PS×LD) − AS²/2PS − ALB×AS²/(2PS×LD²); LSI/LD − ½SI − ALB×SI/2LD²; ALB×SI/2LA − ALB×SI/2LB | SVG 271–278, uguale |
| S12.60 | *PEqq2AS cub.*; *2PS×LD pro PE* | PE⁴/2AS³; √(2PS×LD) | SVG 279 uguale; SVG 280 **√(2PS + LD)**, errato |
| S12.60 | *SIq×SL2SI×1LDc−SIq22SI×1LD−SIq×ALB22SI ×1LDqc* | (SI²×SL/√(2SI))×1/√LD³ − (SI²/2√(2SI))×1/√LD − (SI²×ALB/2√(2SI))×1/√LD⁵ | SVG 281, uguale |
| S12.60 | *2SIq×SL2SI in 1LA−1LB¯*; *SIq2SI in LB−LA*; *SIq×ALB32SI in 1LA cub.−1LB cub.¯* | (2SI²×SL/√(2SI))(1/√LA − 1/√LB); (SI²/√(2SI))(√LB − √LA); (SI²×ALB/3√(2SI))(1/√LA³ − 1/√LB³) | SVG 282–287, uguale |
| S12.60 | *2SIq×SLLI*, *SIq+2SI cub.3LI*, *4SI cub.3LI*, *SI cub.PI* | 2SI²×SL/LI; SI² + 2SI³/3LI; 4SI³/3LI; SI³/PI | SVG 288–293, uguale |
| S12.64 | *DEq×ISIE×V*; *PEn ad IEn*; *PS×IE×IEn ad IS×PE×PEn*; *PS×IEn ad SA×PEn* | DE²×IS/(IE×V); PEⁿ : IEⁿ; PS×IE×IEⁿ : IS×PE×PEⁿ; PS×IEⁿ : SA×PEⁿ | SVG 294–305, uguale |
| S12.66 | *DFq×OPFn, id est, ut 2DF×OPFn−1* | DE²×O/PFⁿ = 2DF×O/PFⁿ⁻¹ − DF²×O/PFⁿ | SVG 307–308; **lettura incerta** (§ A.15) |

### A.18 Refusi probabili della trascrizione

Tutti tradotti secondo il senso; **refusi probabili della trascrizione, da verificare sulla stampa**.

| Luogo | Trascrizione | Lettura |
|---|---|---|
| S12.24 | *quod materiæ densitatem* | *quoad* |
| S12.38 | *Cas 3.* | *Cas. 3.* (punto mancante) |
| S12.47 | *triangula DTE, dte, DES* | *dTe* |
| S12.50 | *occurentia* | *occurrentia* (forse grafia dell’originale) |
| S12.55 | *attahitur* | *attrahitur* |
| S12.58 | *descrescendo* | *decrescendo* |
| S12.60 | radicali assenti (*2PS×LD pro PE*) | √(2PS×LD) |
| S12.64 | *allio* | *alio* |
| S12.66 | *demonstata* | *demonstrata* |
| S12.66 | *DFq×OPFn, id est, ut 2DF×OPFn−1* | vedi § A.15 |

### A.19 Riepilogo: dove Motte aggiunge, omette o sbaglia

| Luogo | Latino | Motte 1846 | Tipo |
|---|---|---|---|
| S12.02 | *ad hanc superficiem lineæ duæ* | «to this superficies **to** two lines» | refuso (parola ripetuta) |
| S12.02 | *HP, LP* | «HP LP» | virgola mancante |
| S12.04 | *Suntque hæ vires* | «And these forces **again**» | aggiunta |
| S12.04 | *Et, per compositionem* | «And **therefore**, by composition» | aggiunta |
| S12.11 | *Restat sola attractio* | «There remains, **therefore**, only» | aggiunta |
| S12.12 | *Superficies, ex quibus solida componuntur, hic non sunt* | «By the superficies of which **I here imagine** the solids composed, **I do not mean**» | riformulazione in prima persona |
| S12.12 | *magnitudinis contemnendæ* | «perfectly inconsiderable» | intensificazione |
| S12.18 | *similaris* | «similar» | ambiguo (§ A.6) |
| S12.24 | *utcunque dissimilares* | «however dissimilar … **in the same ratio**» | aggiunta che altera il senso |
| S12.25 | *erit in eadem ratione* | «will attract … in the same ratio» | verbo reggente sostituito; periodo sgrammaticato |
| S12.25 | *secundum legem quamcunque* | «according to any **given** law» | aggiunta |
| S12.30 | *geminatur attractio* | «the attraction is **only** doubled» | aggiunta |
| S12.31 | *revolventium & quiescentium* | «quiescent and revolving» | ordine invertito |
| S12.36 | *S centrum ejus;* | «S its centre.;» | refuso tipografico |
| S12.41 | *corpusculis innumeris p* | «corpuscles **such as** p» | esplicitazione |
| S12.45 | *sigillatim percurrere longum esset* | «tedious to run over the other cases, whose conclusions are less elegant **and important**, so particularly **as I have done these**» | aggiunte |
| S12.47 | *dte* (trascrizione) | «dTe» | Motte corretto; refuso della trascrizione |
| S12.50 | *sphæræ … AEB* | «a sphere **ABE**» | ordine delle lettere |
| S12.50 | *quam punctum N perpetuo tangit* | «the locus of the point N» | parafrasi |
| S12.51 | *lamina EFfe trahit* | «the **laminæ** EFfe attracts» | plurale errato |
| S12.57 | *Q.E.F.* | «Q.E.D.» | sigla errata |
| S12.58 | *per motum localem* | «with a continued motion» | variazione livellata |
| S12.60 | PE = √(2PS×LD) | «√(2PS **+** LD)» (SVG 280) | **errore di formula** |
| S12.63 | *(ob datum SA cub.) reciproce ut PI* | «because SA3 is given reciprocally as PI» | virgola mancante, lettura ambigua |
| S12.66 | *Sit autem superficies illa* | «Let us suppose that **segment** to be … a physical superficies» | **errore di riferimento** |
| S12.66 | *profunditatem habens quam minimam* | «having some, but a perfectly inconsiderable thickness» | parafrasi |
| S12.66 | (trascrizione incerta) | DE²×O/PFⁿ = 2DF×O/PFⁿ⁻¹ − DF²×O/PFⁿ | Motte coerente con la matematica (§ A.15) |
| S12.69 | *jam pergere liceret* | «it comes next in order to treat» | cambia la modalità |
| S12.69 | *aliqualem usum* | «of some little use» | attenuazione |

Per il resto Motte segue fedelmente il latino, comprese le lettere delle figure e i rimandi interni, che ho controllato uno per uno.

---

## Note editoriali e fisiche

Queste note sono aggiunte del presente fascicolo, non affermazioni tradotte da Newton. I controlli numerici sono eseguiti dallo script `verifica_S12.py` (Python 3, NumPy, SciPy), conservato con i file di lavoro del fascicolo. Unità di misura: costante di gravitazione 1, densità 1, raggio della sfera 1 salvo indicazione. In ogni controllo la forza è la componente lungo l’asse, positiva verso il centro S.

### N1. Le ipotesi della sezione

Newton non parla di «massa» né di «costante di gravitazione». L’ipotesi *ad puncta singula tendant vires æquales centripetæ decrescentes in duplicata ratione distantiarum* dice che ogni particella uguale attrae con la stessa forza alla stessa distanza, e che quella forza decresce come il quadrato della distanza. In termini moderni, un elemento di massa d*m* attrae un corpuscolo a distanza *r* con forza *G* d*m*/*r*², e la forza risultante è la somma vettoriale (l’integrale) di tutti i contributi. Lo Scolio dopo la Prop. LXXIII (S12.12) dichiara il metodo: le superfici sono gusci di spessore evanescente e i punti sono particelle uguali di grandezza trascurabile, secondo i rapporti primi e ultimi della Sezione I. Le Propp. LXXVII–LXXVIII e LXXIX–LXXXIV trattano altre leggi di forza (proporzionale alla distanza, o inversamente proporzionale a una potenza qualsiasi): non sono leggi fisiche proposte, ma un confronto matematico che mette in risalto la particolarità del quadrato inverso.

### N2. Prop. LXX: attrazione nulla all’interno (verifica numerica)

**L’argomento.** Due coni opposti di vertice P tagliano sulla superficie due pezzetti HI e KL. Le loro aree stanno come HP² : LP², perché le distanze stanno come HP : LP e i due pezzetti sono ugualmente inclinati rispetto alla corda: la corda HK è base di un triangolo isoscele con vertice nel centro, quindi forma lo stesso angolo con la superficie nei due estremi. Le forze stanno come area/distanza², cioè sono uguali, e opposte. Newton ricava la proporzionalità degli archi dalla similitudine dei triangoli evanescenti HPI, LPK (Cor. 3 del Lemma VII: archi evanescenti e corde hanno rapporto ultimo di uguaglianza).

**Verifica 1 (integrazione).** Guscio di raggio *R* = 1, densità superficiale 1; corpuscolo a distanza *d* dal centro; forza calcolata per integrazione numerica in θ (quadratura adattiva, tolleranza 10⁻¹²):

| *d*/*R* | 0 | 0,3 | 0,6 | 0,9 | 0,99 |
|---|---|---|---|---|---|
| forza | 0 | 4·10⁻¹⁶ | −2·10⁻¹⁵ | 2·10⁻¹⁴ | −5·10⁻¹³ |

Per confronto, la scala naturale è *M*/*R*² = 4π ≈ 12,57: la forza è nulla entro l’errore di arrotondamento.

**Verifica 2 (somma vettoriale «bruta», senza usare la simmetria).** 400 000 elementi uguali distribuiti uniformemente sulla sfera (reticolo di Fibonacci); corpuscolo in punti fuori asse: P = (0,2; −0,35; 0,1), (0,5; 0,4; −0,3), (0; 0,7; 0). Modulo della risultante: 2·10⁻⁸, 4·10⁻⁸, 9·10⁻⁹, contro circa 2,3–2,8 per la sola metà di guscio più vicina.

**Verifica 3 (l’argomento dei coni).** Per corde casuali per punti interni casuali: i coseni dell’angolo fra corda e normale nei due estremi coincidono a 12 cifre, e il rapporto delle forze dei due pezzetti è 1,000000000000.

**Solo per il quadrato inverso.** Con la stessa integrazione, a *d* = 0,5 la forza del guscio vale +2,21 per una legge 1/*r* (verso il centro) e −2,95 per una legge 1/*r*³ (verso la parete più vicina): la Prop. LXX vale soltanto per il quadrato inverso. In termini moderni è il teorema di Gauss per un guscio sferico: il campo all’interno è nullo.

### N3. Prop. LXXI: il guscio equivale a un corpuscolo nel centro (verifica numerica)

**L’argomento.** Newton confronta due gusci uguali e due corpuscoli a distanze diverse PS, ps, suddividendo i gusci in anelli corrispondenti (stesse distanze SD = sd, SE = se delle secanti dal centro). Mostra che ogni coppia di anelli corrispondenti tira nel rapporto ps² : PS², e quindi anche i gusci interi. La proposizione dimostra la **proporzionalità** a 1/distanza²; che la forza sia proprio quella della materia del guscio raccolta nel centro è detto esplicitamente solo nella Prop. LXXV (*ac si vis tota attrahens manaret de corpusculo unico sito in centro*) e segue dal fatto che a grande distanza il guscio agisce come un punto.

**Verifica 1 (integrazione).** Guscio *R* = 1, densità 1, massa *M* = 4π:

| *d*/*R* | 1,01 | 1,2 | 2 | 5 | 20 |
|---|---|---|---|---|---|
| forza calcolata | 12,3187634686 | 8,7266462600 | 3,1415926536 | 0,5026548246 | 0,0314159265 |
| *M*/*d*² | 12,3187634686 | 8,7266462600 | 3,1415926536 | 0,5026548246 | 0,0314159265 |

Il rapporto vale 1 entro 10⁻¹². Il guscio attrae dunque **esattamente** come la sua massa concentrata nel centro: *F* = *GMm*/*d*².

**Verifica 2 (la costruzione di Newton).** Con PS = 1,6 e ps = 3, ho calcolato per integrazione la forza assiale degli anelli generati dagli archi IH, ih (lato vicino) e KL, kl (lato lontano), fra le secanti con SE = 0,4 e 0,8 e SD = SE + δ, per δ = 10⁻², 10⁻³, 10⁻⁴. Il rapporto è sempre **3,51562500** = ps²/PS² = 9/2,56. Osservazione che Newton non fa: il rapporto è esatto già per anelli di ampiezza finita, non soltanto al limite.

### N4. Propp. LXXII–LXXIV: la sfera piena

- **Prop. LXXII** è un argomento di similitudine: masse ∝ *D*³, distanze ∝ *D*, quindi forza ∝ *D*³/*D*² = *D*. Verifica: due sfere omogenee di raggi 1 e 2,5, corpuscolo a 0,5 o a 2 volte il raggio: rapporto delle forze 2,500000000.
- **Cor. 1–2 della Prop. LXXII**: per orbite circolari *T*² ∝ *r*³/*M*; con *r* ∝ *D* e *M* ∝ *D*³ il periodo non dipende da *D*. Il rimando al Cor. 3 della Prop. IV è corretto.
- **Prop. LXXIII**: dentro la sfera agisce solo la sfera interna di raggio SP (Prop. LXX), e la sua forza è ∝ SP (Prop. LXXII): in termini moderni *g*(*r*) = (4/3)π*Gρr*. **Prop. LXXIV**: fuori, *g* = *GM*/*r*². Verifica per somma di gusci (sfera *R* = 1): *d* = 0,25, 0,5, 0,75 dà 1,047197551, 2,094395102, 3,141592654 = (4/3)π*d*; *d* = 1,5 e 3 dà 1,861684535 e 0,465421134 = (4π/3)/*d*².
- **Cor. 3 della Prop. LXXIV** (l’inverso) è enunciato senza dimostrazione. Fra le leggi di potenza trattate più avanti, solo il quadrato inverso dà una forza esterna esattamente ∝ 1/*d*²: per esempio con una legge 1/*r* il prodotto *F*·*d* vale 3,788, 4,094, 4,180 a *d* = 1,5, 3, 10, quindi non è costante (verifica numerica).

### N5. Scolio dopo la Prop. LXXIII: gusci e particelle

Lo Scolio spiega in che senso una sfera è «composta» di superfici: non di superfici matematiche, prive di spessore, ma di gusci il cui numero cresce e il cui spessore diminuisce all’infinito. È l’applicazione alla gravitazione del metodo dei rapporti primi e ultimi (Sezione I). In termini moderni: l’integrale di volume come limite di somme su gusci, ∫₀^*R* 4π*r*²ρ d*r*.

### N6. Prop. LXXV: due sfere; Cor. 3–4

- L’argomento usa la reciprocità dell’attrazione (Legge III, citata nel Cor. 2): la forza della sfera A su ogni particella della sfera B è quella di un corpuscolo in A; la forza di quel corpuscolo sulla sfera B è uguale e contraria a quella della sfera B sul corpuscolo, che per la Prop. LXXIV è quella di un corpuscolo nel centro di B. Risultato moderno: *F* = *GM*₁*M*₂/*d*².
- Cor. 2: *geminabitur vis* va inteso così: se si contano sia l’attrazione esercitata da A sia quella esercitata da B come agenti, la forza complessiva raddoppia ma le proporzioni restano. Nella fisica moderna la coppia azione–reazione è un’unica interazione; il raddoppio riflette il modo in cui Newton separa la «virtù attrattiva» di ciascun corpo.
- Cor. 3: le orbite coniche intorno al fuoco (Propp. XI–XIII) valgono per pianeti e Sole trattati come sfere. Cor. 4: all’interno di una sfera omogenea la forza è ∝ distanza (Prop. LXXIII) e valgono i moti intorno al centro delle coniche (Prop. X). Esempio didattico moderno: un corpo in un tunnel diametrale attraverso una Terra omogenea oscilla di moto armonico con periodo 2π√(*R*/*g*) ≈ 2π√(6,371·10⁶/9,81) s ≈ 5063 s ≈ 84 minuti.

### N7. Prop. LXXVI: densità variabile con il raggio

Ogni strato sferico di densità uniforme agisce come un corpuscolo nel centro; sommando («componendo») o sottraendo («dividendo») strati concentrici si ottiene qualsiasi legge di densità ρ(*r*). In termini moderni: il teorema del guscio vale per ogni distribuzione a simmetria sferica, ed è ciò che permette di trattare la Terra, più densa verso il centro, come un punto per i corpi esterni. Cor. 3–4: i «pesi» delle sfere fra loro sono ∝ *M*₁*M*₂/*d*², cioè la legge di gravitazione nella forma moderna. La verifica numerica di LXXI (N3) copre anche questo caso, perché ogni strato è un guscio.

### N8. Propp. LXXVII–LXXVIII: forze proporzionali alla distanza

Se ogni particella attrae con forza *k* × distanza, la risultante su P è *k* Σ *m*ᵢ(**r**ᵢ − **r**_P) = *kM*(**r**_S − **r**_P): esattamente quella dell’intera massa nel centro, **sia fuori sia dentro** la sfera (Caso 5), per la sola definizione di centro di gravità. L’argomento dei piani a coppie (PG + Pg = 2PS fuori; pg − pG = 2pS dentro) è la versione geometrica di questo fatto. Verifica Monte Carlo (circa 10⁶ punti nella sfera unitaria): per P = (0; 0; 2,5) la forza è −10,474 lungo z contro −10,472 atteso; per P = (0,3; 0; 0) è −1,257 contro −1,257; per P = (0; −0,6; 0,2) è (2,514; −0,839) contro (2,513; −0,838), entro l’errore statistico. Il Cor. della Prop. LXXVIII rimanda alla Prop. X (ellisse con la forza nel centro) e alla Prop. LXIV (più corpi con forze proporzionali alla distanza).

### N9. Scolio dei «due casi più notevoli» e Lemma XXIX

- I due casi sono le sole leggi di potenza considerate da Newton per le quali (a) le orbite sono sezioni coniche e (b) la sfera attrae secondo la stessa legge delle sue particelle. Il secondo fatto è verificato numericamente in N3–N4 (n = 2) e N8 (forza ∝ distanza); per le altre potenze non vale (N2, N4). In termini moderni il punto (a) richiama il teorema di Bertrand (1873), secondo cui solo queste due leggi danno orbite limitate sempre chiuse; Newton non lo afferma.
- **Lemma XXIX.** Con P nell’origine dell’asse e S a distanza *p* = PS, il punto E comune al cerchio di centro S (raggio *a*) e a quello di centro P (raggio ρ = PE) ha ascissa PD = (ρ² − *a*² + *p*²)/(2*p*). Quindi dPD/dρ = ρ/*p*, cioè **Dd : Ff = PE : PS esattamente al limite**. Verifica numerica con *a* = 1, *p* = 2,2, PE = 1,5, 2, 3 e Ff = 10⁻², 10⁻⁴, 10⁻⁶: per Ff = 10⁻⁶ il rapporto Dd/Ff vale 0,68181841, 0,90909114, 1,36363659 contro PE/PS = 0,68181818, 0,90909091, 1,36363636; lo scarto è proporzionale a Ff, come per un rapporto ultimo.

### N10. Prop. LXXIX: la calotta e il teorema di Archimede

Archimede dimostrò che l’area di una zona sferica è proporzionale alla sua altezza (oggi: 2π*R h*); per questo l’anello generato dall’arco rE è ∝ Dd «restando fisso il raggio PE». Moltiplicando per la componente assiale PD/PE e sommando: Σ PD×Dd = ½(PF² − PD²) = ½DE², perché PF = PE. In termini moderni la forza assiale della calotta di raggio *R* = PE è π·*f*(*R*)·DE² per unità di spessore, dove *f* è la forza di una particella. Verifica per integrazione: con PE = 2, PD = 1,2 la forza × PE² vale 8,0424771932 = π(PF² − PD²) = π·DE²; con PE = 3, PD = 0,5 vale 27,4889357189, uguale.

### N11. Prop. LXXX: l’area ANB è la forza (verifica numerica)

Combinando Lemma XXIX e Prop. LXXIX, la forza della sfera su P è, in termini moderni,

*F* = π ∫ DE² · PS · *f*(PE) / PE d(SD), con D da A a B,

cioè π volte l’area ANB, se DN = DE²×PS×*f*(PE)/PE. Ho confrontato questa area con un’integrazione indipendente (gusci centrati nel corpuscolo) per una sfera di raggio 1 e leggi *f* = 1/*r*ⁿ:

| *n* | PS = 1,5: forza diretta | π × area ANB | PS = 3: forza diretta | π × area ANB |
|---|---|---|---|---|
| 0 (Cor. 1) | 3,8164532977 | 3,8164532977 | 4,0957059780 | 4,0957059780 |
| 1 (Cor. 2) | 2,5255798327 | 2,5255798327 | 1,3647235954 | 1,3647235954 |
| 2 | 1,8616845355 | 1,8616845355 | 0,4654211339 | 0,4654211339 |
| 3 (Cor. 3) | 1,5573036858 | 1,5573036858 | 0,1625724990 | 0,1625724990 |
| 4 | 1,4893476284 | 1,4893476284 | 0,0581776417 | 0,0581776417 |

Coincidenza a 10 cifre. Per *n* = 2 si ritrova (4π/3)/PS² (N4).

### N12. Prop. LXXXI e i tre esempi (verifica numerica)

**Le identità.** Con L punto medio di PI e SI = SA²/PS: PE² = PS × 2LD e DE² = 2SL×LD − LD² − AL×LB. Controllate per PS = 1,5 e 3 e tre posizioni di D (SD = −0,7; 0,2; 0,9): coincidenza a 10 cifre. Utili per i calcoli: LA = (PS − SA)²/2PS, LB = (PS + SA)²/2PS, LI = PI/2 = (PS² − SA²)/2PS.

**Le «aree iperboliche».** Le aree sotto le iperboli *k*/LD sono logaritmi: *k*·ln(LB/LA). I «metodi comuni» di Newton sono le quadrature dell’iperbole note dalla metà del Seicento.

**Esempio 1 (forza ∝ 1/distanza).** Newton raddoppia l’ordinata (*Pone DN æqualem ejus duplo*): l’area aba della costruzione è quindi il doppio dell’area sotto DN, cosa irrilevante perché conta solo la proporzionalità. In formula: area aba = SL×AB − AL×LB×ln(LB/LA). Valori: 1,6078340582 (PS = 1,5) e 0,8688100247 (PS = 3), identici al doppio dell’area calcolata numericamente. La costruzione è coerente: Aa = LB e Bb = LA danno LA×Aa = LB×Bb = AL×LB, quindi a e b stanno sulla stessa iperbole di asintoti Ll, LB.

**Esempio 2 (forza ∝ 1/distanza³).** Area ANB = AasbB − 2AS×SI, con AasbB = LS×SI×ln(LB/LA). Valori: 0,9914103180 e 0,1034968673, identici all’area calcolata con V = PE³/2AS².

**Esempio 3 (forza ∝ 1/distanza⁴).** Ho rifatto l’algebra: le tre aree valgono 2SI²×SL/LI, SI², SI² + 2SI³/3LI, e poiché SL = SI + LI la differenza è 4SI³/3LI, come in Newton. Valori: 0,9481481481 (PS = 1,5) e 0,0370370370 (PS = 3), identici all’area numerica. Per la forza vera con *f* = 1/*r*⁴ e sfera di raggio 1 si ottiene *F* × PS³ × PI = 4π/3 = 4,1887902048 a PS = 1,2; 1,5; 2; 4: la forza è inversamente come PS³×PI, come afferma Newton. In formula moderna, con densità e costante di gravitazione uguali a 1: *F* = (4π/3)·SA³/(PS³·PI).

### N13. Prop. LXXXII: punti coniugati I e P (verifica numerica)

SI × SP = SA²: I e P sono punti inversi rispetto alla sfera. Per un punto E qualsiasi della sfera, i triangoli SPE, SEI sono simili e IE/PE = SI/SA è costante: per questo il rapporto delle ordinate non dipende da E, e passa alle aree e alle forze. In termini moderni:

*F*(I)/*F*(P) = √(SI/SP) · √(*f*(SI)/*f*(SP)) = (SP/SI)^((*n*−1)/2) per *f* = 1/*r*ⁿ.

L’ordine «nei luoghi P e I» dell’enunciato va quindi letto come rapporto della forza in I alla forza in P, come nell’esempio di S12.63; preso alla lettera nell’ordine P : I, il teorema darebbe un risultato sbagliato (per *n* = 2: SA/SP invece di SP/SA).

Verifica (sfera di raggio 1; forza interna calcolata con gusci centrati in I, che per *n* ≥ 3 equivale a prendere il valore principale dell’integrale, perché i gusci interamente contenuti nella sfera si annullano):

| SP | *n* = 1 | *n* = 2 | *n* = 3 | *n* = 4 |
|---|---|---|---|---|
| 1,25: *F*(I)/*F*(P) | 1,0000000000 | 1,2500000000 | 1,5625000000 | 1,9531250000 |
| formula di Newton | 1 | SP/SA = 1,25 | SP²/SA² = 1,5625 | SP³/SA³ = 1,953125 |
| 2: *F*(I)/*F*(P) | 1,0000000000 | 2,0000000000 | 4,0000000000 | 8,0000000000 |

Per *n* = 4, *F*(I) × SA³ × PI = 4π/3 per SI = 0,2; 0,5; 0,8: la forza interna è inversamente come PI, come dice Newton. Per *n* = 1 le forze in I e P sono uguali; per *n* = 2 si ritrova il rapporto SP : SA, coerente con le Propp. LXXIII–LXXIV.

### N14. Propp. LXXXIII–LXXXIV: segmenti sferici

Per il corpuscolo nel centro P di una sfera di raggio 1 e un segmento tagliato da un piano a distanza PD, l’area di FN (FN = DE²/PFⁿ, con DE² = PF² − PD²) moltiplicata per π coincide con un’integrazione diretta in coordinate cilindriche: PD = 0,3, *n* = 2: 1,5393804003 in entrambi i modi; PD = 0,6, *n* = 2: 0,5026548246; PD = 0,3, *n* = 3: 2,3529674598. Il controllo conferma la lettura DE²×O/PFⁿ adottata in S12.66 (§ A.15) e non quella letterale della trascrizione. La Prop. LXXXIV riduce il caso generale alla somma di una parte trattata come nella Prop. LXXXI (le calotte centrate in P che stanno interamente nel segmento) e di una parte trattata come nella Prop. LXXXIII; non ho verificato numericamente questa scomposizione.

### N15. Per il curatore

- **Che cosa rende celebre la sezione.** Le Propp. LXX–LXXVI giustificano il trattamento dei corpi celesti come punti materiali in tutta l’opera. Le pagine interattive delle Propp. LXX e LXXI sono le più adatte a un liceo: la prima con la coppia di coni opposti, la seconda con il confronto di due anelli corrispondenti (N3, verifica 2).
- **Unicità del quadrato inverso.** Le verifiche numeriche (N2: guscio con leggi 1/*r* e 1/*r*³; N4: sfera con legge 1/*r*) danno materiale per un’attività: cambiare l’esponente e vedere che il guscio non è più «trasparente» all’interno.
- **Lettura incerta da risolvere sulla stampa:** la formula di S12.66 (§ A.15). È l’unico punto in cui la trascrizione non permette una lettura sicura.

---

## Controllo della copertura

Pagine 1726 dai marcatori <n> della trascrizione; pagine Motte dalle ancore `Page_n` dell’EPUB (§ Fonti).

| Identificatori | Incipit latino | Contenuto | 1726 | Motte 1846 |
|---|---|---|---|---|
| S12.01–S12.02 | *Si ad sphæricæ superficiei puncta singula* | Prop. LXX | p. 189 | p. 219 |
| S12.03–S12.04 | *Iisdem positis, dico quod corpusculum extra sphæricam* | Prop. LXXI | pp. 189–191 | pp. 219–220 |
| S12.05–S12.06 | *Si ad sphæræ cujusvis puncta singula* | Prop. LXXII | p. 191 | p. 220 |
| S12.07–S12.09 | *Hinc si corpuscula in circulis* | Prop. LXXII, Cor. 1–3 | p. 192 | p. 220 |
| S12.10–S12.11 | *Si ad sphæræ alicujus datæ puncta singula* | Prop. LXXIII | p. 192 | pp. 220–221 |
| S12.12 | *Superficies, ex quibus solida componuntur* | Scolio | pp. 192–193 | p. 221 |
| S12.13–S12.14 | *Iisdem positis, dico quod corpusculum extra sphæram* | Prop. LXXIV | p. 193 | p. 221 |
| S12.15–S12.17 | *Hinc in æqualibus distantiis* | Prop. LXXIV, Cor. 1–3 | p. 193 | p. 221 |
| S12.18–S12.19 | *Si ad sphæræ datæ puncta singula tendant vires æquales centripetæ, decrescentes* | Prop. LXXV | pp. 193–194 | pp. 221–222 |
| S12.20–S12.23 | *Attractiones sphærarum, versus alias* | Prop. LXXV, Cor. 1–4 | p. 194 | p. 222 |
| S12.24–S12.25 | *Si sphæræ in progressu a centro* | Prop. LXXVI | pp. 194–195 | pp. 222–223 |
| S12.26–S12.34 | *Hinc si ejusmodi sphæræ complures* | Prop. LXXVI, Cor. 1–9 | pp. 195–196 | pp. 223–224 |
| S12.35 | *Si ad singula sphærarum puncta* | Prop. LXXVII, enunciato | p. 196 | p. 224 |
| S12.36–S12.41 | *Cas. 1. Sit AEBF sphæra* | Prop. LXXVII, Casi 1–6 | pp. 196–198 | pp. 224–225 |
| S12.42–S12.44 | *Si sphæræ in progressu … inæquabiles* | Prop. LXXVIII e Cor. | p. 198 | p. 225 |
| S12.45 | *Attractionum casus duos insigniores* | Scolio | pp. 198–199 | pp. 225–226 |
| S12.46–S12.47 | *Si describantur centro S circulus quilibet AEB* | Lemma XXIX | p. 199 | p. 226 |
| S12.48–S12.49 | *Si superficies ob latitudinem infinite diminutam* | Prop. LXXIX | p. 200 | pp. 226–227 |
| S12.50–S12.51 | *Si ad sphæræ alicujus AEB* | Prop. LXXX | pp. 201–202 | pp. 227–228 |
| S12.52–S12.55 | *Hinc si vis centripeta, ad particulas singulas* | Prop. LXXX, Cor. 1–4 | pp. 202–203 | p. 228 |
| S12.56–S12.57 | *Stantibus jam positis, mensuranda est area ANB* | Prop. LXXXI | pp. 203–204 | pp. 228–229 |
| S12.58 | *Exempl. 1. Si vis centripeta … reciproce ut distantia* | Esempio 1 | p. 204 | pp. 229–230 |
| S12.59 | *Exempl. 2. … reciproce ut cubus distantiæ* | Esempio 2 | pp. 204–205 | p. 230 |
| S12.60 | *Exempl. 3. … in quadruplicata ratione* | Esempio 3 | pp. 205–206 | pp. 230–231 |
| S12.61 | *Eadem methodo determinari potest* | Raccordo | p. 206 | p. 231 |
| S12.62–S12.64 | *In sphæra centro S intervallo SA descripta* | Prop. LXXXII: enunciato, esempi, dimostrazione | pp. 206–208 | pp. 231–232 |
| S12.65–S12.66 | *Invenire vim qua corpusculum in centro sphæræ* | Prop. LXXXIII | pp. 208–209 | pp. 232–233 |
| S12.67–S12.68 | *Invenire vim, qua corpusculum, extra centrum* | Prop. LXXXIV | p. 209 | p. 233 |
| S12.69 | *Explicatis attractionibus corporum sphæricorum* | Scolio finale | p. 210 | p. 233 |

**Controlli eseguiti.**

1. **Rilettura frase per frase contro il latino.** Ho confrontato in sequenza ogni periodo della trascrizione, da *Si ad sphæricæ superficiei puncta singula* a *ob earum in rebus philosophicis aliqualem usum, subjungere*, con la traduzione. Nessuna frase manca. Dove il latino ha un periodo molto lungo (per esempio la prima frase della Prop. LXX o la seconda della Prop. LXXI) l’italiano lo divide in più frasi senza omettere membri. Le 85 frasi delle dimostrazioni incluse nella Parte B sono allineate una per una con il testo italiano, che è generato dagli stessi dati.
2. **check.py:** `python3 check.py Newton_Principia_IT_11_L1_S12.md latino-1726-L1-S12.md --en motte-1846-L1-S12.md` → «unità: 15  passi: 85  identificatori nel testo: 69 … OK», senza avvisi: tutte le stringhe `la` ed `en` (enunciati e passi) sono sottostringhe esatte delle fonti.
3. **Matematica.** Verifiche numeriche con lo script `verifica_S12.py` per le Propp. LXX (tre metodi indipendenti) e LXXI (integrazione e costruzione di Newton), LXXII–LXXIV, LXXVII, Lemma XXIX, Propp. LXXIX, LXXX (cinque leggi di forza), LXXXI con i tre esempi (identità e aree), LXXXII (quattro leggi), LXXXIII: tutte concordano con Newton entro l’errore numerico (note N2–N14). L’algebra dell’Esempio 3 è stata rifatta a mano. Non ho trovato errori matematici nel testo latino; l’unica formula incoerente (S12.66) è un problema della trascrizione.
4. **Confronto con Motte.** Tutta la sezione, pp. 219–233, comprese le 53 formule SVG (256–308) rese come immagini e lette una per una. Divergenze nel § A.19.
5. **Separazione fra testo e commento.** Nel testo tradotto non ci sono formule moderne; le formule di Newton sono rese con apici e barre (§ Criteri).

**Non ho potuto verificare:**

- **la stampa del 1726:** tutti i refusi del § A.18 e la lettura di S12.66 (§ A.15) restano da controllare sulla scansione;
- **le figure NATP00087-132…150:** non disponibili. In particolare restano da controllare le lettere I dell’area BDI (Prop. LXXXIII), il ruolo di E e F nelle due sfere della Prop. LXXIII e la posizione della figura 141;
- **la Prop. LXXXIV** e la **Prop. LXXV** (due sfere) non sono state verificate numericamente in modo separato: seguono per composizione da risultati verificati;
- **la paginazione di Motte** deriva dalle ancore dell’EPUB Gutenberg, non da un esemplare a stampa.

---

## Registro del lavoro successivo

| Unità | Stato |
|---|---|
| Libro I, Sezione XII (Propp. LXX–LXXXIV, Lemma XXIX, scolii) | **Fascicolo 11, presente documento, prima versione** |
| Dati per le pagine interattive (15 unità, 85 passi) | Parte B di questo fascicolo; validata con check.py |
| Refusi della trascrizione (§ A.18) e formula di S12.66 (§ A.15) | **Da verificare sulla stampa del 1726** |
| Figure NATP00087-132…150 | Da acquisire per le pagine interattive e per controllare le lettere |
| Pagina interattiva Prop. LXX (coni opposti) e Prop. LXXI (anelli corrispondenti) | Candidate prioritarie (nota N15) |
| Errore di Motte 1846 in S12.60 (√(2PS + LD)) | Da correggere nel testo a fronte con nota; controllare se è già in Motte 1729 |
| Coerenza del glossario con gli altri fascicoli del Libro I | Da controllare: *corpusculum*, *orbis* «guscio», *similaris*, *applicare ad*, *ducere in … per motum continuum* |
| Revisione filologica e scientifica indipendente | Da eseguire, come previsto dalla skill di verifica |

Il presente testo è una nuova traduzione assistita da IA. Non riproduce le traduzioni italiane moderne. La trascrizione latina è © The Newton Project e non va ridistribuita finché non se ne chiariscono le condizioni d’uso; il testo di Motte (1846) è di pubblico dominio.

---

## Parte B — Dati per le pagine interattive

Unità incluse: ogni lemma e proposizione con figura nel latino o con costruzione geometrica: Propp. LXX, LXXI, LXXIII, LXXVI, LXXVII, Lemma XXIX, Propp. LXXIX, LXXX, LXXXI con i tre esempi (unità separate, perché ciascuno ha una propria costruzione e proprie figure 143–146), LXXXII, LXXXIII, LXXXIV. Escluse: Propp. LXXII, LXXIV, LXXV, LXXVIII (senza figura né costruzione: argomenti di similitudine o di composizione) e tutti i corollari, nessuno dei quali ha dimostrazione propria con figura.

Convenzioni:

- `la`: testo latino esatto della trascrizione, refusi e formule appiattite compresi, annotati in `nota`; i marcatori di pagina <n> e [FIG n] sono conservati;
- `it`: la traduzione di questo fascicolo, identica al testo della traduzione;
- `en`: Motte 1846, allineato per senso; [SVG n] indica una formula stampata come immagine (letta nell’apparato, § A.17);
- `dipende_da`: soltanto i rimandi citati nella frase, comprese le citazioni di Euclide e di Archimede;
- un passo per ogni frase latina della dimostrazione principale (nella Prop. LXXXII, la dimostrazione di S12.64; gli esempi di S12.63 restano nel testo). Il Lemma XXIX è un’unica frase latina e ha quindi un solo passo.

```json
{
 "fascicolo": "11-L1-S12",
 "versione": "0.1",
 "data": "2026-11-08",
 "convenzioni": {
  "dipende_da": "solo rimandi citati esplicitamente nella frase latina (comprese le citazioni di Euclide e Archimede)",
  "en": "Motte 1846, allineato per senso; [SVG n] = formula stampata come immagine nell’EPUB",
  "figura.mostra": "elementi da rendere visibili al passo, cumulativi salvo indicazione",
  "formule": "nel campo la le formule sono quelle della trascrizione, anche appiattite; la lettura adottata è nel campo it e nell’apparato"
 },
 "unita": [
  {
   "id": "L1-P70",
   "tipo": "Propositio/Theorema",
   "titolo": "Prop. LXX — attrazione nulla all’interno di una superficie sferica",
   "copertura": [
    "S12.01",
    "S12.02"
   ],
   "fonti": {
    "la": "",
    "en": "Motte 1846, p. 219"
   },
   "enunciato": {
    "la": "",
    "it": "Se ai singoli punti di una superficie sferica tendono forze centripete uguali, decrescenti in rapporto duplicato delle distanze dai punti, dico che un corpuscolo posto all’interno della superficie non è attratto da queste forze verso alcuna parte.",
    "en": "If to every point of a sphærical surface there tend equal centripetal forces decreasing in the duplicate ratio of the distances from those points; I say, that a corpuscle placed within that superficies will not be attracted by those forces any way."
   },
   "figura_base": {
    "punti": [
     "H",
     "I",
     "K",
     "L",
     "P"
    ],
    "vincoli": [
     "HIKL: superficie sferica (nella figura, un cerchio massimo)",
     "P interno",
     "HK, IL corde per P",
     "archi HI, KL piccolissimi"
    ]
   },
   "passi": [
    {
     "id": "L1-P70-p1",
     "la": "",
     "it": "Sia HIKL quella superficie sferica, e P il corpuscolo posto all’interno. Per P si conducano fino a questa superficie due linee HK, IL, che intercettino archi piccolissimi HI, KL; e, poiché i triangoli HPI, LPK sono simili (per il Cor. 3 del Lemma VII), quegli archi saranno proporzionali alle distanze HP, LP; e le particelle qualsiasi della superficie sferica in HI e in KL, delimitate tutt’intorno da rette passanti per il punto P, staranno in quel rapporto duplicato.",
     "en": "Let HIKL, be that sphærical superficies, and P a corpuscle placed within. Through P let there be drawn to this superficies to two lines HK, IL, intercepting very small arcs HI, KL; and because (by Cor. 3, Lem. VII) the triangles HPI, LPK are alike, those arcs will be proportional to the distances HP LP; and any particles at HI and KL of the sphærical superficies, terminated by right lines passing through P, will be in the duplicate ratio of those distances.",
     "dipende_da": [
      "Lemma VII, Cor. 3"
     ],
     "figura": {
      "mostra": [
       "superficie sferica HIKL (sezione circolare)",
       "P interno",
       "corde HK, IL per P",
       "archi HI, KL",
       "triangoli HPI, LPK"
      ],
      "evidenzia": [
       "HI : KL = HP : LP",
       "particelle in HI e KL in rapporto HP² : LP²"
      ]
     },
     "nota": "Motte ripete «to» («to this superficies to two lines») e omette la virgola in «HP LP»."
    },
    {
     "id": "L1-P70-p2",
     "la": "",
     "it": "Dunque le forze di queste particelle esercitate sul corpo P sono uguali fra loro.",
     "en": "Therefore the forces of these particles exerted upon the body P are equal between themselves.",
     "dipende_da": [],
     "figura": {
      "mostra": [
       "forze delle particelle HI e KL su P (frecce opposte)"
      ],
      "evidenzia": [
       "uguaglianza delle due forze"
      ]
     }
    },
    {
     "id": "L1-P70-p3",
     "la": "",
     "it": "Esse sono infatti direttamente come le particelle e inversamente come i quadrati delle distanze.",
     "en": "For the forces are as the particles directly, and the squares of the distances inversely.",
     "dipende_da": [],
     "figura": {
      "mostra": [
       "HP², LP²"
      ],
      "evidenzia": [
       "forza ∝ particella / distanza²"
      ]
     }
    },
    {
     "id": "L1-P70-p4",
     "la": "",
     "it": "E questi due rapporti compongono il rapporto di uguaglianza.",
     "en": "And these two ratios compose the ratio of equality.",
     "dipende_da": [],
     "figura": {
      "mostra": [],
      "evidenzia": [
       "(HP²/LP²) × (LP²/HP²) = 1"
      ]
     }
    },
    {
     "id": "L1-P70-p5",
     "la": "",
     "it": "Le attrazioni, dunque, fatte in egual misura verso parti contrarie, si distruggono a vicenda.",
     "en": "The attractions therefore, being made equally towards contrary parts, destroy each other.",
     "dipende_da": [],
     "figura": {
      "mostra": [
       "risultante nulla della coppia"
      ],
      "evidenzia": [
       "cancellazione"
      ]
     }
    },
    {
     "id": "L1-P70-p6",
     "la": "",
     "it": "E con un argomento simile tutte le attrazioni su tutta la superficie sferica sono distrutte da attrazioni contrarie.",
     "en": "And by a like reasoning all the attractions through the whole sphærical superficies are destroyed by contrary attractions.",
     "dipende_da": [],
     "figura": {
      "mostra": [
       "altre coppie di coni opposti per P che coprono tutta la superficie"
      ],
      "evidenzia": [
       "ogni coppia si annulla"
      ]
     }
    },
    {
     "id": "L1-P70-p7",
     "la": "",
     "it": "Perciò il corpo P non è spinto verso alcuna parte da queste attrazioni. C.V.D.",
     "en": "Therefore the body P will not be any way impelled by those attractions. Q.E.D.",
     "dipende_da": [],
     "figura": {
      "mostra": [
       "P"
      ],
      "evidenzia": [
       "forza risultante nulla in P (verifica numerica: nota N2)"
      ]
     }
    }
   ]
  },
  {
   "id": "L1-P71",
   "tipo": "Propositio/Theorema",
   "titolo": "Prop. LXXI — superficie sferica e corpuscolo esterno",
   "copertura": [
    "S12.03",
    "S12.04"
   ],
   "fonti": {
    "la": "",
    "en": "Motte 1846, pp. 219–220"
   },
   "enunciato": {
    "la": "",
    "it": "Poste le stesse cose, dico che un corpuscolo posto all’esterno della superficie sferica è attratto verso il centro della sfera da una forza inversamente proporzionale al quadrato della sua distanza dallo stesso centro.",
    "en": "The same things supposed as above, I say, that a corpuscle placed without the sphærical superficies is attracted towards the centre of the sphere with a force reciprocally proportional to the square of its distance from that centre."
   },
   "figura_base": {
    "punti": [
     "A",
     "H",
     "I",
     "K",
     "L",
     "B",
     "S",
     "P",
     "D",
     "E",
     "F",
     "R",
     "Q",
     "a",
     "h",
     "i",
     "k",
     "l",
     "b",
     "s",
     "p",
     "d",
     "e",
     "f",
     "r",
     "q"
    ],
    "vincoli": [
     "due cerchi massimi uguali AHKB (centro S) e ahkb (centro s)",
     "P sul prolungamento di AB, p sul prolungamento di ab",
     "PHK, PIL secanti; SD ⊥ PHK, SE ⊥ PIL, IR ⊥ PHK, IQ ⊥ AB",
     "F = SD ∩ PL",
     "sd = SD, se = SE (quindi archi HK = hk, IL = il)",
     "angolo DPE evanescente"
    ]
   },
   "passi": [
    {
     "id": "L1-P71-p1",
     "la": "",
     "it": "Siano AHKB, ahkb due superfici sferiche uguali, descritte con centri S, s e diametri AB, ab; e siano P, p corpuscoli situati all’esterno, sui prolungamenti di quei diametri.",
     "en": "Let AHKB, ahkb, be two equal sphærical superficies described about the centre S, s; their diameters AB, ab; and let P and p be two corpuscles situate without the spheres in those diameters produced.",
     "dipende_da": [],
     "figura": {
      "mostra": [
       "cerchi massimi AHKB (centro S) e ahkb (centro s), uguali",
       "diametri AB, ab",
       "P, p sui prolungamenti"
      ],
      "evidenzia": [
       "PS ≠ ps"
      ]
     }
    },
    {
     "id": "L1-P71-p2",
     "la": "",
     "it": "Dai corpuscoli si conducano le linee PHK, PIL, phk, pil, che taglino dai cerchi massimi AHB, ahb archi uguali HK, hk e IL, il; e su di esse si abbassino le perpendicolari SD, sd; SE, se; IR, ir, delle quali SD, sd taglino PL, pl in F e f; si abbassino anche sui diametri le perpendicolari IQ, iq.",
     "en": "Let there be drawn from the corpuscles the lines PHK, PIL, phk, pil, cutting off from the great circles AHB, ahb, the equal arcs HK, hk, IL, il; and to those lines let fall the perpendiculars SD, sd, SE, se, IR, ir; of which let SD, sd, cut PL, pl, in F and f. Let fall also to the diameters the perpendiculars IQ, iq.",
     "dipende_da": [],
     "figura": {
      "mostra": [
       "secanti PHK, PIL e phk, pil",
       "perpendicolari SD, SE, IR e sd, se, ir",
       "F = SD ∩ PL, f = sd ∩ pl",
       "IQ, iq"
      ],
      "evidenzia": [
       "HK = hk, IL = il (quindi SD = sd, SE = se)"
      ]
     },
     "nota": "Motte divide in due frasi il periodo latino."
    },
    {
     "id": "L1-P71-p3",
     "la": "",
     "it": "Svaniscano gli angoli DPE, dpe; e, poiché DS e ds, ES ed es sono uguali, le linee PE, PF e pe, pf e le lineette DF, df si considerino uguali: il loro rapporto ultimo, quando quegli angoli DPE, dpe svaniscono insieme, è infatti di uguaglianza.",
     "en": "Let now the angles DPE, dpe, vanish; and because DS and ds, ES and es are equal, the lines PE, PF, and pe, pf, and the lineolæ DF, df may be taken for equal; because their last ratio, when the angles DPE, dpe vanish together, is the ratio of equality.",
     "dipende_da": [],
     "figura": {
      "mostra": [
       "angoli DPE, dpe che si chiudono"
      ],
      "evidenzia": [
       "PE ≈ PF, pe ≈ pf, DF ≈ df (rapporto ultimo)"
      ]
     }
    },
    {
     "id": "L1-P71-p4",
     "la": "",
     "it": "Stabilite dunque queste cose, PI starà a PF come RI sta a DF, e pf starà a pi come df, ossia DF, sta a ri; e, per uguaglianza, PI×pf starà a PF×pi come RI sta a ri, cioè (per il Cor. 3 del Lemma VII) come l’arco IH sta all’arco ih.",
     "en": "These things then supposed, it will be, as PI to PF so is RI to DF, and as pf to pi so is df or DF to ri; and, ex æquo, as PI × pf to PF × pi so is RI to ri, that is (by Cor. 3, Lem VII), so is the arc IH to the arc ih.",
     "dipende_da": [
      "Lemma VII, Cor. 3"
     ],
     "figura": {
      "mostra": [
       "triangoli PIR ~ PFD",
       "archi IH, ih"
      ],
      "evidenzia": [
       "PI×pf : PF×pi = IH : ih"
      ]
     }
    },
    {
     "id": "L1-P71-p5",
     "la": "",
     "it": "Di nuovo, PI sta a PS come IQ sta a SE, e ps sta a pi come se, ossia SE, sta a iq; e, per uguaglianza, PI×ps sta a PS×pi come IQ sta a iq.",
     "en": "Again, PI is to PS as IQ to SE, and ps to pi as se or SE to iq; and, ex æquo, PI × ps to PS × pi as IQ to iq.",
     "dipende_da": [],
     "figura": {
      "mostra": [
       "triangoli PIQ ~ PSE"
      ],
      "evidenzia": [
       "PI×ps : PS×pi = IQ : iq"
      ]
     }
    },
    {
     "id": "L1-P71-p6",
     "la": "",
     "it": "E, congiungendo i rapporti, PI²×pf×ps sta a pi²×PF×PS come IH×IQ sta a ih×iq; cioè come la superficie circolare che l’arco IH descriverà con la rotazione del semicerchio AKB intorno al diametro AB sta alla superficie circolare che l’arco ih descriverà con la rotazione del semicerchio akb intorno al diametro ab.",
     "en": "And compounding the ratios PI2 × pf × ps is to pi2 × PF × PS, as IH × IQ to ih × iq; that is, as the circular superficies which is described by the arc IH, as the semi-circle AKB revolves about the diameter AB, is to the circular superficies described by the arc ih as the semi-circle akb revolves about the diameter ab.",
     "dipende_da": [],
     "figura": {
      "mostra": [
       "anelli (zone) generati dalla rotazione degli archi IH, ih intorno agli assi"
      ],
      "evidenzia": [
       "area anello ∝ arco × raggio IQ"
      ]
     }
    },
    {
     "id": "L1-P71-p7",
     "la": "",
     "it": "E le forze con cui queste superfici attraggono i corpuscoli P e p lungo linee dirette verso di esse sono (per ipotesi) direttamente come le superfici stesse e inversamente come i quadrati delle distanze delle superfici dai corpi, cioè come pf×ps sta a PF×PS.",
     "en": "And the forces with which these superficies attract the corpuscles P and p in the direction of lines tending to those superficies are by the hypothesis as the superficies themselves directly, and the squares of the distances of the superficies from those corpuscles inversely; that is, as pf × ps to PF × PS.",
     "dipende_da": [],
     "figura": {
      "mostra": [
       "forze degli anelli lungo PI e pi"
      ],
      "evidenzia": [
       "forze : = pf×ps : PF×PS"
      ]
     }
    },
    {
     "id": "L1-P71-p8",
     "la": "",
     "it": "E queste forze stanno alle loro parti oblique che (fatta la scomposizione delle forze per il Cor. 2 delle leggi) tendono ai centri lungo le linee PS, ps, come PI sta a PQ e pi a pq; cioè (per la similitudine dei triangoli PIQ e PSF, piq e psf) come PS sta a PF e ps a pf.",
     "en": "And these forces again are to the oblique parts of them which (by the resolution of forces as in Cor. 2, of the Laws) tend to the centres in the directions of the lines PS, ps, as PI to PQ, and pi to pq; that is (because of the like triangles PIQ and PSF, piq and psf), as PS to PF and ps to pf.",
     "dipende_da": [
      "Leggi, Cor. 2"
     ],
     "figura": {
      "mostra": [
       "componenti lungo PS e ps",
       "triangoli PIQ ~ PSF"
      ],
      "evidenzia": [
       "componente assiale = forza × PF/PS"
      ]
     },
     "nota": "Motte aggiunge «again»."
    },
    {
     "id": "L1-P71-p9",
     "la": "",
     "it": "Di qui, per uguaglianza, l’attrazione di questo corpuscolo P verso S sta all’attrazione del corpuscolo p verso s come (PF×pf×ps)/PS sta a (pf×PF×PS)/ps, cioè come ps² sta a PS².",
     "en": "Thence ex æquo, the attraction of the corpuscle P towards S is to the attraction of the corpuscle p towards s as [SVG 256] is to [SVG 257], that is, as ps2 to PS2.",
     "dipende_da": [],
     "figura": {
      "mostra": [
       "attrazioni assiali dei due anelli"
      ],
      "evidenzia": [
       "rapporto = ps² : PS² (verifica numerica: nota N3)"
      ]
     },
     "nota": "Formule appiattite nella trascrizione; lette come (PF×pf×ps)/PS e (pf×PF×PS)/ps, come in Motte (SVG 256–257)."
    },
    {
     "id": "L1-P71-p10",
     "la": "",
     "it": "E con un argomento simile le forze con cui le superfici descritte dalla rotazione degli archi KL, kl tirano i corpuscoli staranno come ps² sta a PS²; e nello stesso rapporto staranno le forze di tutte le superfici circolari in cui ciascuna delle due superfici sferiche può essere divisa, prendendo sempre sd uguale a SD e se uguale a SE.",
     "en": "And, by a like reasoning, the forces with which the superficies described by the revolution of the arcs KL, kl attract those corpuscles, will be as ps2 to PS2. And in the same ratio will be the forces of all the circular superficies into which each of the sphærical superficies may be divided by taking sd always equal to SD, and se equal to SE.",
     "dipende_da": [],
     "figura": {
      "mostra": [
       "anelli lontani KL, kl",
       "suddivisione di entrambe le superfici in anelli corrispondenti"
      ],
      "evidenzia": [
       "ogni coppia di anelli: ps² : PS²"
      ]
     }
    },
    {
     "id": "L1-P71-p11",
     "la": "",
     "it": "E, per composizione, le forze delle intere superfici sferiche esercitate sui corpuscoli staranno nello stesso rapporto. C.V.D.",
     "en": "And therefore, by composition, the forces of the entire sphærical superficies exerted upon those corpuscles will be in the same ratio. Q.E.D.",
     "dipende_da": [],
     "figura": {
      "mostra": [
       "superfici intere"
      ],
      "evidenzia": [
       "F(P) : F(p) = ps² : PS²"
      ]
     },
     "nota": "Motte aggiunge «therefore»."
    }
   ]
  },
  {
   "id": "L1-P73",
   "tipo": "Propositio/Theorema",
   "titolo": "Prop. LXXIII — attrazione all’interno di una sfera piena",
   "copertura": [
    "S12.10",
    "S12.11"
   ],
   "fonti": {
    "la": "",
    "en": "Motte 1846, pp. 220–221"
   },
   "enunciato": {
    "la": "",
    "it": "Se ai singoli punti di una sfera data tendono forze centripete uguali, decrescenti in rapporto duplicato delle distanze dai punti, dico che un corpuscolo posto all’interno della sfera è attratto da una forza proporzionale alla sua distanza dal centro della sfera.",
    "en": "If to the several points of a given sphere there tend equal centripetal forces decreasing in a duplicate ratio of the distances from the points; I say, that a corpuscle placed within the sphere is attracted by a force proportional to its distance from the centre."
   },
   "figura_base": {
    "punti": [
     "A",
     "B",
     "C",
     "D",
     "S",
     "P",
     "E",
     "Q",
     "F"
    ],
    "vincoli": [
     "sfera ABCD di centro S",
     "P interno",
     "sfera PEQF concentrica di raggio SP"
    ]
   },
   "passi": [
    {
     "id": "L1-P73-p1",
     "la": "",
     "it": "Nella sfera ABCD, descritta con centro S, si collochi il corpuscolo P; e con lo stesso centro S e con raggio SP immagina descritta una sfera interna PEQF.",
     "en": "In the sphere ABCD, described about the centre S, let there be placed the corpuscle P; and about the same centre S, with the interval SP, conceive described an interior sphere PEQF.",
     "dipende_da": [],
     "figura": {
      "mostra": [
       "sfera ABCD, centro S",
       "P interno",
       "sfera interna PEQF di raggio SP"
      ],
      "evidenzia": []
     }
    },
    {
     "id": "L1-P73-p2",
     "la": "",
     "it": "È manifesto (per la Prop. LXX) che le superfici sferiche concentriche di cui è composta la differenza AEBF delle sfere non agiscono affatto sul corpo P, perché le loro attrazioni sono distrutte da attrazioni contrarie.",
     "en": "It is plain (by Prop. LXX) that the concentric sphærical superficies, of which the difference AEBF of the spheres is composed, have no effect at all upon the body P, their attractions being destroyed by contrary attractions.",
     "dipende_da": [
      "Prop. LXX"
     ],
     "figura": {
      "mostra": [
       "guscio AEBF fra le due sfere"
      ],
      "evidenzia": [
       "guscio esterno: forza nulla su P"
      ]
     }
    },
    {
     "id": "L1-P73-p3",
     "la": "",
     "it": "Resta la sola attrazione della sfera interna PEQF.",
     "en": "There remains, therefore, only the attraction of the interior sphere PEQF.",
     "dipende_da": [],
     "figura": {
      "mostra": [
       "sfera PEQF"
      ],
      "evidenzia": []
     },
     "nota": "Motte aggiunge «therefore»."
    },
    {
     "id": "L1-P73-p4",
     "la": "",
     "it": "E (per la Prop. LXXII) questa è come la distanza PS. C.V.D.",
     "en": "And (by Prop. LXXII) this is as the distance PS. Q.E.D.",
     "dipende_da": [
      "Prop. LXXII"
     ],
     "figura": {
      "mostra": [
       "segmento PS"
      ],
      "evidenzia": [
       "forza ∝ PS (verifica numerica: nota N4)"
      ]
     }
    }
   ]
  },
  {
   "id": "L1-P76",
   "tipo": "Propositio/Theorema",
   "titolo": "Prop. LXXVI — sfere stratificate, legge del quadrato inverso",
   "copertura": [
    "S12.24",
    "S12.25"
   ],
   "fonti": {
    "la": "",
    "en": "Motte 1846, pp. 222–223"
   },
   "enunciato": {
    "la": "",
    "it": "Se delle sfere, procedendo dal centro alla circonferenza, sono dissimilari in modo qualsiasi (quanto alla densità della materia e alla forza attrattiva), ma, procedendo lungo il giro, sono similari da ogni parte a ogni distanza data dal centro; e la forza attrattiva di ciascun punto decresce in rapporto duplicato della distanza del corpo attratto: dico che la forza totale con cui una sfera di questo genere ne attrae un’altra è inversamente proporzionale al quadrato della distanza dei centri.",
    "en": "If spheres be however dissimilar (as to density of matter and attractive force) in the same ratio onward from the centre to the circumference; but every where similar, at every given distance from the centre, on all sides round about; and the attractive force of every point decreases in the duplicate ratio of the distance of the body attracted; I say, that the whole force with which one of these spheres attracts the other will be reciprocally proportional to the square of the distance of the centres."
   },
   "figura_base": {
    "punti": [
     "S",
     "P",
     "A",
     "B",
     "C",
     "D",
     "E",
     "F",
     "G",
     "H",
     "I",
     "K",
     "L",
     "M"
    ],
    "vincoli": [
     "sfere concentriche AB, CD, EF di centro S",
     "sfere concentriche GH, IK, LM di centro P",
     "le sfere non si intersecano"
    ]
   },
   "passi": [
    {
     "id": "L1-P76-p1",
     "la": "",
     "it": "Siano AB, CD, EF, ecc. sfere concentriche similari in numero qualsiasi, le interne delle quali, aggiunte alle esterne, compongano una materia più densa verso il centro, oppure, sottratte, la lascino più rada; e queste (per la Prop. LXXV) tireranno altre sfere concentriche similari in numero qualsiasi, GH, IK, LM, ecc., ciascuna delle prime ciascuna delle seconde, con forze inversamente proporzionali al quadrato della distanza SP.",
     "en": "Imagine several concentric similar spheres, AB, CD, EF, &c.; the innermost of which added to the outermost may compose a matter more dense towards the centre, or subducted from them may leave the same more lax and rare. Then, by Prop. LXXV, these spheres will attract other similar concentric spheres GH, IK, LM, &c., each the other, with forces reciprocally proportional to the square of the distance SP.",
     "dipende_da": [
      "Prop. LXXV"
     ],
     "figura": {
      "mostra": [
       "sfere concentriche AB, CD, EF (centro S)",
       "sfere concentriche GH, IK, LM (centro P)",
       "distanza SP"
      ],
      "evidenzia": [
       "stratificazione della densità"
      ]
     }
    },
    {
     "id": "L1-P76-p2",
     "la": "",
     "it": "E componendo o dividendo, la somma di tutte quelle forze, o l’eccesso di alcune sulle altre, cioè la forza con cui l’intera sfera AB, composta di sfere concentriche qualsiasi o di differenze di sfere concentriche, tira l’intera GH, composta di sfere concentriche qualsiasi o di differenze di sfere concentriche, starà nello stesso rapporto.",
     "en": "And, by composition or division, the sum of all those forces, or the excess of any of them above the others; that is, the entire force with which the whole sphere AB (composed of any concentric spheres or of their differences) will attract the whole sphere GH (composed of any concentric spheres or their differences) in the same ratio.",
     "dipende_da": [],
     "figura": {
      "mostra": [
       "sfere complete AB e GH"
      ],
      "evidenzia": [
       "forza totale ∝ 1/SP²"
      ]
     },
     "nota": "Nella frase di Motte manca il verbo reggente: «the entire force … will attract … in the same ratio»."
    },
    {
     "id": "L1-P76-p3",
     "la": "",
     "it": "Si aumenti all’infinito il numero delle sfere concentriche, in modo che la densità della materia, insieme con la forza attrattiva, cresca o decresca secondo una legge qualsiasi procedendo dalla circonferenza al centro; e, aggiunta materia non attrattiva, si completi ovunque la densità mancante, affinché le sfere acquistino qualsiasi forma desiderata; e la forza con cui una di esse attrarrà l’altra sarà ancora, per l’argomento precedente, in quello stesso rapporto inverso del quadrato della distanza. C.V.D.",
     "en": "Let the number of the concentric spheres be increased in infinitum, so that the density of the matter together with the attractive force may, in the progress from the circumference to the centre, increase or decrease according to any given law; and by the addition of matter not attractive, let the deficient density be supplied, that so the spheres may acquire any form desired; and the force with which one of these attracts the other will be still, by the former reasoning, in the same ratio of the square of the distance inversely. Q.E.D.",
     "dipende_da": [],
     "figura": {
      "mostra": [
       "densità continua ρ(r) arbitraria"
      ],
      "evidenzia": [
       "vale ancora 1/SP²"
      ]
     },
     "nota": "Motte: «according to any given law»; il latino ha solo *secundum legem quamcunque*."
    }
   ],
   "nota": "Le lettere AB, CD, … indicano sfere (per diametri), non segmenti."
  },
  {
   "id": "L1-P77",
   "tipo": "Propositio/Theorema",
   "titolo": "Prop. LXXVII — forze proporzionali alla distanza (Casi 1–6)",
   "copertura": [
    "S12.35",
    "S12.36",
    "S12.37",
    "S12.38",
    "S12.39",
    "S12.40",
    "S12.41"
   ],
   "fonti": {
    "la": "",
    "en": "Motte 1846, pp. 224–225"
   },
   "enunciato": {
    "la": "",
    "it": "Se ai singoli punti delle sfere tendono forze centripete proporzionali alle distanze dei punti dai corpi attratti, dico che la forza composta con cui due sfere si tirano a vicenda è come la distanza fra i centri delle sfere.",
    "en": "If to the several points of spheres there tend centripetal forces proportional to the distances of the points from the attracted bodies; I say, that the compounded force with which two spheres attract each other mutually is as the distance between the centres of the spheres."
   },
   "figura_base": {
    "punti": [
     "A",
     "E",
     "B",
     "F",
     "S",
     "P",
     "G",
     "g",
     "H",
     "e",
     "f",
     "p"
    ],
    "vincoli": [
     "sfera AEBF di centro S",
     "P sull’asse PASB, esterno (Casi 1–4); p interno (Casi 5–6)",
     "piani EF, ef ⊥ asse, SG = Sg",
     "H nel piano EF"
    ]
   },
   "passi": [
    {
     "id": "L1-P77-p1",
     "la": "",
     "it": "Sia AEBF una sfera; S il suo centro; P un corpuscolo attratto; PASB l’asse della sfera passante per il centro del corpuscolo; EF, ef due piani che tagliano la sfera, perpendicolari a questo asse e ugualmente distanti dal centro della sfera da una parte e dall’altra; G, g le intersezioni dei piani con l’asse; e H un punto qualsiasi nel piano EF.",
     "en": "CASE 1. Let AEBF be a sphere; S its centre.; P a corpuscle attracted; PASB the axis of the sphere passing through the centre of the corpuscle; EF, ef two planes cutting the sphere, and perpendicular to the axis, and equi-distant, one on one side, the other on the other, from the centre of the sphere; G and g the intersections of the planes and the axis; and H any point in the plane EF.",
     "dipende_da": [],
     "figura": {
      "mostra": [
       "sfera AEBF, centro S",
       "P esterno sull’asse PASB",
       "piani EF, ef simmetrici rispetto a S",
       "G, g",
       "H nel piano EF"
      ],
      "evidenzia": [
       "SG = Sg"
      ]
     }
    },
    {
     "id": "L1-P77-p2",
     "la": "",
     "it": "La forza centripeta del punto H sul corpuscolo P, esercitata lungo la linea PH, è come la distanza PH; e (per il Cor. 2 delle leggi) lungo la linea PG, ossia verso il centro S, è come la lunghezza PG.",
     "en": "The centripetal force of the point H upon the corpuscle P, exerted in the direction of the line PH, is as the distance PH; and (by Cor. 2, of the Laws) the same exerted in the direction of the line PG, or towards the centre S, is as the length PG.",
     "dipende_da": [
      "Leggi, Cor. 2"
     ],
     "figura": {
      "mostra": [
       "segmento PH",
       "componente lungo PG"
      ],
      "evidenzia": [
       "componente assiale ∝ PG, la stessa per ogni H del piano"
      ]
     }
    },
    {
     "id": "L1-P77-p3",
     "la": "",
     "it": "Dunque la forza di tutti i punti nel piano EF, cioè dell’intero piano, con cui il corpuscolo P è tirato verso il centro S, è come la distanza PG moltiplicata per il numero dei punti, cioè come il solido compreso fra il piano stesso EF e quella distanza PG.",
     "en": "Therefore the force of all the points in the plane EF (that is, of that whole plane) by which the corpuscle P is attracted towards the centre S is as the distance PG multiplied by the number of those points, that is, as the solid contained under that plane EF and the distance PG.",
     "dipende_da": [],
     "figura": {
      "mostra": [
       "disco EF"
      ],
      "evidenzia": [
       "forza del piano ∝ EF × PG"
      ]
     }
    },
    {
     "id": "L1-P77-p4",
     "la": "",
     "it": "E similmente la forza del piano ef, con cui il corpuscolo P è tirato verso il centro S, è come quel piano moltiplicato per la sua distanza Pg, ossia come il piano EF, uguale a esso, moltiplicato per quella distanza Pg; e la somma delle forze dei due piani è come il piano EF moltiplicato per la somma delle distanze PG + Pg, cioè come quel piano moltiplicato per il doppio della distanza PS fra il centro e il corpuscolo, cioè come il doppio del piano EF moltiplicato per la distanza PS, o come la somma dei piani uguali EF + ef moltiplicata per la stessa distanza.",
     "en": "And in like manner the force of the plane ef, by which the corpuscle P is attracted towards the centre S, is as that plane drawn into its distance Pg, or as the equal plane EF drawn into that distance Pg; and the sum of the forces of both planes as the plane EF drawn into the sum of the distances PG + Pg, that is, as that plane drawn into twice the distance PS of the centre and the corpuscle; that is, as twice the plane EF drawn into the distance PS, or as the sum of the equal planes EF + ef drawn into the same distance.",
     "dipende_da": [],
     "figura": {
      "mostra": [
       "disco ef",
       "Pg"
      ],
      "evidenzia": [
       "PG + Pg = 2PS"
      ]
     }
    },
    {
     "id": "L1-P77-p5",
     "la": "",
     "it": "E con un argomento simile le forze di tutti i piani nella sfera intera, ugualmente distanti dal centro della sfera da una parte e dall’altra, sono come la somma dei piani moltiplicata per la distanza PS, cioè come la sfera intera e la distanza PS considerate congiuntamente. C.V.D.",
     "en": "And, by a like reasoning, the forces of all the planes in the whole sphere, equi-distant on each side from the centre of the sphere, are as the sum of those planes drawn into the distance PS, that is, as the whole sphere and the distance PS conjunctly. Q.E.D.",
     "dipende_da": [],
     "figura": {
      "mostra": [
       "tutte le coppie di piani simmetrici"
      ],
      "evidenzia": [
       "forza ∝ sfera × PS"
      ]
     }
    },
    {
     "id": "L1-P77-p6",
     "la": "",
     "it": "Ora il corpuscolo P tiri la sfera AEBF.",
     "en": "Let now the corpuscle P attract the sphere AEBF.",
     "dipende_da": [],
     "figura": {
      "mostra": [
       "azione di P sulla sfera"
      ],
      "evidenzia": []
     },
     "nota": "Caso 2."
    },
    {
     "id": "L1-P77-p7",
     "la": "",
     "it": "Con lo stesso argomento si proverà che la forza con cui quella sfera è tirata sarà come la distanza PS. C.V.D.",
     "en": "And, by the same reasoning, it will appear that the force with which the sphere is attracted is as the distance PS. Q.E.D.",
     "dipende_da": [],
     "figura": {
      "mostra": [],
      "evidenzia": [
       "forza ∝ PS"
      ]
     }
    },
    {
     "id": "L1-P77-p8",
     "la": "",
     "it": "Si componga ora un’altra sfera di innumerevoli corpuscoli P; e poiché la forza con cui è tirato ciascun corpuscolo è come la distanza del corpuscolo dal centro della prima sfera e come la sfera stessa, considerate congiuntamente, e perciò è la stessa che se provenisse tutta da un unico corpuscolo nel centro della sfera, la forza totale con cui sono tirati tutti i corpuscoli della seconda sfera, cioè con cui è tirata tutta quella sfera, sarà la stessa che se quella sfera fosse tirata da una forza proveniente da un unico corpuscolo nel centro della prima sfera; e perciò è proporzionale alla distanza fra i centri delle sfere. C.V.D.",
     "en": "CASE 3. Imagine another sphere composed of innumerable corpuscles P; and because the force with which every corpuscle is attracted is as the distance of the corpuscle from the centre of the first sphere, and as the same sphere conjunctly, and is therefore the same as if it all proceeded from a single corpuscle situate in the centre of the sphere, the entire force with which all the corpuscles in the second sphere are attracted, that is, with which that whole sphere is attracted, will be the same as if that sphere were attracted by a force issuing from a single corpuscle in the centre of the first sphere; and is therefore proportional to the distance between the centres of the spheres. Q.E.D.",
     "dipende_da": [],
     "figura": {
      "mostra": [
       "seconda sfera fatta di corpuscoli P"
      ],
      "evidenzia": [
       "equivalenza con un corpuscolo nel centro S"
      ]
     },
     "nota": "Caso 3. Nella trascrizione manca il punto dopo «Cas»."
    },
    {
     "id": "L1-P77-p9",
     "la": "",
     "it": "Le sfere si tirino a vicenda: la forza raddoppiata conserverà la proporzione di prima. C.V.D.",
     "en": "CASE 4. Let the spheres attract each other mutually, and the force will be doubled, but the proportion will remain. Q.E.D.",
     "dipende_da": [],
     "figura": {
      "mostra": [],
      "evidenzia": [
       "raddoppio, proporzione invariata"
      ]
     },
     "nota": "Caso 4."
    },
    {
     "id": "L1-P77-p10",
     "la": "",
     "it": "Si collochi ora il corpuscolo p all’interno della sfera AEBF; e poiché la forza del piano ef sul corpuscolo è come il solido compreso fra quel piano e la distanza pg, e la forza contraria del piano EF come il solido compreso fra quel piano e la distanza pG, la forza composta da entrambe sarà come la differenza dei solidi, cioè come la somma dei piani uguali moltiplicata per la metà della differenza delle distanze, cioè come quella somma moltiplicata per pS, distanza del corpuscolo dal centro della sfera.",
     "en": "CASE 5. Let the corpuscle p be placed within the sphere AEBF; and because the force of the plane ef upon the corpuscle is as the solid contained under that plane and the distance pg; and the contrary force of the plane EF as the solid contained under that plane and the distance pG; the force compounded of both will be as the difference of the solids, that is, as the sum of the equal planes drawn into half the difference of the distances; that is, as that sum drawn into pS, the distance of the corpuscle from the centre of the sphere.",
     "dipende_da": [],
     "figura": {
      "mostra": [
       "p interno (figura 137)",
       "piani EF, ef",
       "pg, pG"
      ],
      "evidenzia": [
       "(pg − pG)/2 = pS"
      ]
     },
     "nota": "Caso 5."
    },
    {
     "id": "L1-P77-p11",
     "la": "",
     "it": "E con un argomento simile l’attrazione di tutti i piani EF, ef nella sfera intera, cioè l’attrazione della sfera intera, è come la somma di tutti i piani, ossia la sfera intera, e come pS, distanza del corpuscolo dal centro della sfera, considerate congiuntamente. C.V.D.",
     "en": "And, by a like reasoning, the attraction of all the planes EF, ef, throughout the whole sphere, that is, the attraction of the whole sphere, is conjunctly as the sum of all the planes, or as the whole sphere, and as pS, the distance of the corpuscle from the centre of the sphere. Q.E.D.",
     "dipende_da": [],
     "figura": {
      "mostra": [
       "tutte le coppie di piani"
      ],
      "evidenzia": [
       "forza ∝ sfera × pS"
      ]
     }
    },
    {
     "id": "L1-P77-p12",
     "la": "",
     "it": "E se di innumerevoli corpuscoli p si compone una nuova sfera, situata all’interno della sfera precedente AEBF, si proverà come prima che l’attrazione, sia semplice, di una sfera sull’altra, sia reciproca, di entrambe l’una sull’altra, sarà come la distanza dei centri pS. C.V.D.",
     "en": "CASE 6. And if there be composed a new sphere out of innumerable corpuscles such as p, situate within the first sphere AEBF, it may be proved, as before, that the attraction, whether single of one sphere towards the other, or mutual of both towards each other, will be as the distance pS of the centres. Q.E.D.",
     "dipende_da": [],
     "figura": {
      "mostra": [
       "sfera interna fatta di corpuscoli p"
      ],
      "evidenzia": [
       "forza ∝ pS"
      ]
     },
     "nota": "Caso 6. Motte: «corpuscles such as p»."
    }
   ],
   "nota": "Passi 1–5: Caso 1; 6–7: Caso 2; 8: Caso 3; 9: Caso 4; 10–11: Caso 5 (figura 137); 12: Caso 6."
  },
  {
   "id": "L1-Lem29",
   "tipo": "Lemma",
   "titolo": "Lemma XXIX — rapporto ultimo Dd : Ff = PE : PS",
   "copertura": [
    "S12.46",
    "S12.47"
   ],
   "fonti": {
    "la": "",
    "en": "Motte 1846, p. 226"
   },
   "enunciato": {
    "la": "",
    "it": "Se con centro S si descrive un cerchio qualsiasi AEB, e con centro P due cerchi EF, ef, che taglino il primo in E, e e la linea PS in F, f; e su PS si abbassano le perpendicolari ED, ed: dico che, se si intende che la distanza degli archi EF, ef diminuisca all’infinito, il rapporto ultimo della linea evanescente Dd alla linea evanescente Ff è quello della linea PE alla linea PS.",
    "en": "If about the centre S there be described any circle as AEB, and about the centre P there be also described two circles EF, ef, cutting the first in E and e, and the line PS in F and f; and there be let fall to PS the perpendiculars ED, ed; I say, that if the distance of the arcs EF, ef be supposed to be infinitely diminished, the last ratio of the evanescent line Dd to the evanescent line Ff is the same as that of the line PE to the line PS."
   },
   "figura_base": {
    "punti": [
     "S",
     "A",
     "E",
     "B",
     "P",
     "F",
     "f",
     "e",
     "D",
     "d",
     "q",
     "T",
     "G"
    ],
    "vincoli": [
     "cerchio AEB di centro S",
     "archi EF, ef di centro P",
     "ED, ed ⊥ PS",
     "q = Pe ∩ arco EF",
     "T = (retta Ee) ∩ PS",
     "SG ⊥ PE",
     "distanza degli archi evanescente"
    ]
   },
   "passi": [
    {
     "id": "L1-Lem29-p1",
     "la": "",
     "it": "Se infatti la linea Pe taglia l’arco EF in q, e la retta Ee, che coincide con l’arco evanescente Ee, prolungata incontra la retta PS in T, e da S si abbassa su PE la normale SG, per la similitudine dei triangoli DTE, dTe, DES, Dd starà a Ee come DT sta a TE, ossia come DE sta a ES; e, poiché i triangoli Eeq, ESG sono simili (per il Lemma VIII e per il Cor. 3 del Lemma VII), Ee starà a eq, ossia a Ff, come ES sta a SG; e, per uguaglianza, Dd starà a Ff come DE sta a SG, cioè (per la similitudine dei triangoli PDE, PGS) come PE sta a PS. C.V.D.",
     "en": "For if the line Pe cut the arc EF in q; and the right line Ee, which coincides with the evanescent arc Ee, be produced, and meet the right line PS in T; and there be let fall from S to PE the perpendicular SG; then, because of the like triangles DTE, dTe, DES, it will be as Dd to Ee so DT to TE, or DE to ES: and because the triangles, Eeq, ESG (by Lem. VIII, and Cor. 3, Lem. VII) are similar, it will be as Ee to eq or Ff so ES to SG; and, ex æquo, as Dd to Ff so DE to SG; that is (because of the similar triangles PDE, PGS), so is PE to PS. Q.E.D.",
     "dipende_da": [
      "Lemma VIII",
      "Lemma VII, Cor. 3"
     ],
     "figura": {
      "mostra": [
       "cerchio AEB (centro S)",
       "archi EF, ef (centro P)",
       "q = Pe ∩ arco EF",
       "T = Ee ∩ PS",
       "SG ⊥ PE",
       "triangoli DTE ~ dTe ~ DES",
       "triangoli Eeq ~ ESG",
       "triangoli PDE ~ PGS"
      ],
      "evidenzia": [
       "Dd : Ee = DE : ES",
       "Ee : Ff = ES : SG",
       "Dd : Ff = PE : PS (verifica numerica: nota N9)"
      ]
     },
     "nota": "Unica frase latina; la pagina può rivelare in sequenza le quattro proporzioni. La trascrizione ha «dte»: refuso probabile per «dTe» (Motte: dTe)."
    }
   ]
  },
  {
   "id": "L1-P79",
   "tipo": "Propositio/Theorema",
   "titolo": "Prop. LXXIX — forza di una lamina sferica concavo-convessa",
   "copertura": [
    "S12.48",
    "S12.49"
   ],
   "fonti": {
    "la": "",
    "en": "Motte 1846, pp. 226–227"
   },
   "enunciato": {
    "la": "",
    "it": "Se una superficie EFfe, che per la larghezza diminuita all’infinito sta ormai per svanire, descrive, ruotando intorno all’asse PS, un solido sferico concavo-convesso, alle cui singole particelle uguali tendono forze centripete uguali, dico che la forza con cui quel solido tira un corpuscolo situato in P sta nel rapporto composto dal rapporto del solido DE²×Ff e dal rapporto della forza con cui una particella data, nel luogo Ff, tirerebbe lo stesso corpuscolo.",
    "en": "Suppose a superficies as EFfe to have its breadth infinitely diminished, and to be just vanishing; and that the same superficies by its revolution round the axis PS describes a sphærical concavo-convex solid, to the several equal particles of which there tend equal centripetal forces; I say, that the force with which that solid attracts a corpuscle situate in P is in a ratio compounded of the ratio of the solid DE2 × Ff and the ratio of the force with which the given particle in the place Ff would attract the same corpuscle."
   },
   "figura_base": {
    "punti": [
     "P",
     "S",
     "E",
     "F",
     "f",
     "e",
     "D",
     "d",
     "r"
    ],
    "vincoli": [
     "archi EF, ef di centro P",
     "D, d piedi delle perpendicolari da E, e su PS",
     "r = de ∩ arco FE",
     "la figura ruota intorno all’asse PS"
    ]
   },
   "passi": [
    {
     "id": "L1-P79-p1",
     "la": "",
     "it": "Se infatti consideriamo dapprima la forza della superficie sferica FE, che è generata dalla rotazione dell’arco FE ed è tagliata in un punto qualsiasi r dalla linea de, la parte anulare della superficie generata dalla rotazione dell’arco rE sarà come la lineetta Dd, restando fisso il raggio PE della sfera (come ha dimostrato Archimede nel libro *Sulla sfera e il cilindro*).",
     "en": "For if we consider, first, the force of the sphærical superficies FE which is generated by the revolution of the arc FE, and is cut any where, as in r, by the line de, the annular part of the superficies generated by the revolution of the arc rE will be as the lineola Dd, the radius of the sphere PE remaining the same; as Archimedes has demonstrated in his Book of the Sphere and Cylinder.",
     "dipende_da": [
      "Archimede, Sulla sfera e il cilindro"
     ],
     "figura": {
      "mostra": [
       "superficie sferica FE (centro P, raggio PE)",
       "linea de che la taglia in r",
       "anello generato dall’arco rE"
      ],
      "evidenzia": [
       "area dell’anello ∝ Dd (zona sferica)"
      ]
     }
    },
    {
     "id": "L1-P79-p2",
     "la": "",
     "it": "E la forza di questa, esercitata lungo le linee PE o Pr situate tutt’intorno sulla superficie conica, è come questa stessa parte anulare della superficie, cioè come la lineetta Dd, oppure, il che è lo stesso, come il rettangolo compreso fra il raggio dato PE della sfera e quella lineetta Dd; ma lungo la linea PS, che tende al centro S, è minore nel rapporto di PD a PE, e perciò è come PD×Dd.",
     "en": "And the force of this superficies exerted in the direction of the lines PE or Pr situate all round in the conical superficies, will be as this annular superficies itself; that is as the lineola Dd, or, which is the same, as the rectangle under the given radius PE of the sphere and the lineola Dd; but that force, exerted in the direction of the line PS tending to the centre S, will be less in the ratio PD to PE, and therefore will be as PD × Dd.",
     "dipende_da": [],
     "figura": {
      "mostra": [
       "cono di vertice P per l’anello",
       "componente lungo PS"
      ],
      "evidenzia": [
       "fattore PD/PE",
       "forza assiale ∝ PD × Dd"
      ]
     }
    },
    {
     "id": "L1-P79-p3",
     "la": "",
     "it": "Si intenda ora divisa la linea DF in innumerevoli particelle uguali, ciascuna delle quali si chiami Dd; e la superficie FE sarà divisa in altrettanti anelli uguali, le cui forze saranno come la somma di tutti i PD×Dd, cioè come ½PF² − ½PD², e perciò come DE².",
     "en": "Suppose now the line DF to be divided into innumerable little equal particles, each of which call Dd, and then the superficies FE will be divided into so many equal annuli, whose forces will be as the sum of all the rectangles PD × Dd, that is, as [SVG 258], and therefore as DE2.",
     "dipende_da": [],
     "figura": {
      "mostra": [
       "DF suddiviso in parti Dd",
       "anelli uguali sulla superficie FE"
      ],
      "evidenzia": [
       "Σ PD×Dd = ½PF² − ½PD² = ½DE²"
      ]
     },
     "nota": "Formula appiattita nella trascrizione («12PFq−12PDq»), letta come ½PF² − ½PD² (Motte, SVG 258)."
    },
    {
     "id": "L1-P79-p4",
     "la": "",
     "it": "Si moltiplichi ora la superficie FE per l’altezza Ff; e la forza del solido EFfe esercitata sul corpuscolo P diventerà come DE²×Ff: s’intende, se è data la forza che una particella data Ff esercita sul corpuscolo P alla distanza PF.",
     "en": "Let now the superficies FE be drawn into the altitude Ff; and the force of the solid EFfe exerted upon the corpuscle P will be as DE2 × Ff; that is, if the force be given which any given particle as Ff exerts upon the corpuscle P at the distance PF.",
     "dipende_da": [],
     "figura": {
      "mostra": [
       "lamina EFfe di spessore Ff"
      ],
      "evidenzia": [
       "forza ∝ DE² × Ff"
      ]
     }
    },
    {
     "id": "L1-P79-p5",
     "la": "",
     "it": "Ma se quella forza non è data, la forza del solido EFfe diventerà come il solido DE²×Ff e quella forza non data, considerati congiuntamente. C.V.D.",
     "en": "But if that force be not given, the force of the solid EFfe will be as the solid DE2 × Ff and that force not given, conjunctly. Q.E.D.",
     "dipende_da": [],
     "figura": {
      "mostra": [],
      "evidenzia": [
       "forza ∝ DE² × Ff × f(PF)"
      ]
     }
    }
   ]
  },
  {
   "id": "L1-P80",
   "tipo": "Propositio/Theorema",
   "titolo": "Prop. LXXX — l’area ANB misura l’attrazione della sfera",
   "copertura": [
    "S12.50",
    "S12.51"
   ],
   "fonti": {
    "la": "",
    "en": "Motte 1846, pp. 227–228"
   },
   "enunciato": {
    "la": "",
    "it": "Se alle singole particelle uguali di una sfera AEB, descritta con centro S, tendono forze centripete uguali, e sull’asse AB della sfera, nel quale è collocato un corpuscolo P, si innalzano dai singoli punti D le perpendicolari DE, che incontrano la sfera in E, e su di esse si prendono le lunghezze DN, che siano come la quantità DE²×PS/PE e la forza che una particella della sfera situata sull’asse esercita sul corpuscolo P alla distanza PE, considerate congiuntamente: dico che la forza totale con cui il corpuscolo P è tirato verso la sfera è come l’area ANB, compresa fra l’asse AB della sfera e la linea curva ANB che il punto N tocca continuamente.",
    "en": "If to the several equal parts of a sphere ABE described about the centre S there tend equal centripetal forces; and from the several points D in the axis of the sphere AB in which a corpuscle, as P, is placed, there be erected the perpendiculars DE meeting the sphere in E, and if in those perpendiculars the lengths DN be taken as the quantity [SVG 259], and as the force which a particle of the sphere situate in the axis exerts at the distance PE upon the corpuscle P conjunctly; I say, that the whole force with which the corpuscle P is attracted towards the sphere is as the area ANB, comprehended under the axis of the sphere AB, and the curve line ANB, the locus of the point N."
   },
   "figura_base": {
    "punti": [
     "A",
     "E",
     "B",
     "S",
     "P",
     "D",
     "d",
     "N",
     "n",
     "F",
     "f"
    ],
    "vincoli": [
     "sfera AEB di centro S",
     "P sull’asse AB prolungato",
     "DE ⊥ AB",
     "DN ∝ DE²×PS/PE × forza di una particella a distanza PE",
     "lamine EFfe di centro P"
    ]
   },
   "passi": [
    {
     "id": "L1-P80-p1",
     "la": "",
     "it": "Infatti, ferme restando le costruzioni fatte nel lemma e nel teorema immediatamente precedenti, immagina che l’asse AB della sfera sia diviso in innumerevoli particelle uguali Dd, e che la sfera intera sia divisa in altrettante lamine sferiche concavo-convesse EFfe; e s’innalzi la perpendicolare dn.",
     "en": "For supposing the construction in the last Lemma and Theorem to stand, conceive the axis of the sphere AB to be divided into innumerable equal particles Dd, and the whole sphere to be divided into so many sphærical concavo-convex laminæ EFfe; and erect the perpendicular dn.",
     "dipende_da": [
      "Lemma XXIX",
      "Prop. LXXIX"
     ],
     "figura": {
      "mostra": [
       "sfera AEB, centro S",
       "asse AB con P",
       "suddivisione Dd",
       "lamine EFfe (centro P)",
       "perpendicolari DN, dn"
      ],
      "evidenzia": []
     }
    },
    {
     "id": "L1-P80-p2",
     "la": "",
     "it": "Per il teorema precedente, la forza con cui la lamina EFfe tira il corpuscolo P è come DE²×Ff e la forza di una sola particella esercitata alla distanza PE o PF, considerate congiuntamente.",
     "en": "By the last Theorem, the force with which the laminæ EFfe attracts the corpuscle P is as DE2 × Ff and the force of one particle exerted at the distance PE or PF, conjunctly.",
     "dipende_da": [
      "Prop. LXXIX"
     ],
     "figura": {
      "mostra": [
       "lamina EFfe"
      ],
      "evidenzia": [
       "forza ∝ DE² × Ff × f(PE)"
      ]
     }
    },
    {
     "id": "L1-P80-p3",
     "la": "",
     "it": "Ma (per il lemma precedente) Dd sta a Ff come PE sta a PS, e quindi Ff è uguale a PS×Dd/PE, e DE²×Ff è uguale a Dd moltiplicato per DE²×PS/PE; e perciò la forza della lamina EFfe è come Dd moltiplicato per DE²×PS/PE e la forza della particella esercitata alla distanza PF, considerate congiuntamente, cioè (per ipotesi) come DN×Dd, ossia come l’area evanescente DNnd.",
     "en": "But (by the last Lemma) Dd is to Ff as PE to PS, and therefore Ff is equal to [SVG 260]; and DE2 × Ff is equal to [SVG 261]; and therefore the force of the lamina EFfe is as [SVG 261] and the force of a particle exerted at the distance PF conjunctly; that is, by the supposition, as DN × Dd, or as the evanescent area DNnd.",
     "dipende_da": [
      "Lemma XXIX"
     ],
     "figura": {
      "mostra": [
       "striscia DNnd"
      ],
      "evidenzia": [
       "Ff = PS×Dd/PE",
       "forza della lamina ∝ area DNnd"
      ]
     },
     "nota": "Formule appiattite nella trascrizione (anche «PE;&DEq»): lette come in Motte, SVG 260–261."
    },
    {
     "id": "L1-P80-p4",
     "la": "",
     "it": "Le forze di tutte le lamine esercitate sul corpo P sono dunque come tutte le aree DNnd, cioè la forza totale della sfera è come l’area totale ANB. C.V.D.",
     "en": "Therefore the forces of all the laminæ exerted upon the corpuscle P are as all the areas DNnd, that is, the whole force of the sphere will be as the whole area ANB. Q.E.D.",
     "dipende_da": [],
     "figura": {
      "mostra": [
       "curva ANB",
       "area ANB"
      ],
      "evidenzia": [
       "forza totale ∝ area ANB (verifica numerica: nota N11)"
      ]
     }
    }
   ],
   "nota": "La figura 141 nella trascrizione precede i corollari; il testo non dice a che cosa si riferisca."
  },
  {
   "id": "L1-P81",
   "tipo": "Propositio/Problema",
   "titolo": "Prop. LXXXI — misura dell’area ANB",
   "copertura": [
    "S12.56",
    "S12.57"
   ],
   "fonti": {
    "la": "",
    "en": "Motte 1846, pp. 228–229"
   },
   "enunciato": {
    "la": "",
    "it": "Ferme restando le cose già poste, si deve misurare l’area ANB.",
    "en": "The things remaining as above, it is required to measure the area ANB."
   },
   "figura_base": {
    "punti": [
     "P",
     "H",
     "I",
     "L",
     "A",
     "S",
     "B",
     "D",
     "E"
    ],
    "vincoli": [
     "PH tangente alla sfera in H",
     "HI ⊥ asse PAB",
     "L punto medio di PI",
     "SI × SP = SA²"
    ]
   },
   "passi": [
    {
     "id": "L1-P81-p1",
     "la": "",
     "it": "Dal punto P si conduca la retta PH tangente alla sfera in H; e, abbassata sull’asse PAB la normale HI, si divida PI a metà in L; e sarà (per la Prop. XII del libro II degli *Elementi*) PE² uguale a PS² + SE² + 2PSD.",
     "en": "From the point P let there be drawn the right line PH touching the sphere in H; and to the axis PAB, letting fall the perpendicular HI, bisect PI in L; and (by Prop. XII, Book II, Elem.) PE2 is equal to PS2 + SE2 + 2PSD.",
     "dipende_da": [
      "Euclide, Elementi II, 12"
     ],
     "figura": {
      "mostra": [
       "tangente PH",
       "H",
       "HI ⊥ asse",
       "L punto medio di PI",
       "triangolo PSE"
      ],
      "evidenzia": [
       "PE² = PS² + SE² + 2PS×SD"
      ]
     }
    },
    {
     "id": "L1-P81-p2",
     "la": "",
     "it": "Ma SE², ossia SH², è uguale (per la similitudine dei triangoli SPH, SHI) al rettangolo PSI.",
     "en": "But because the triangles SPH, SHI are alike, SE2 or SH2 is equal to the rectangle PSI,",
     "dipende_da": [],
     "figura": {
      "mostra": [
       "triangoli SPH ~ SHI"
      ],
      "evidenzia": [
       "SH² = PS × SI"
      ]
     },
     "nota": "Motte chiude la frase con una virgola."
    },
    {
     "id": "L1-P81-p3",
     "la": "",
     "it": "Dunque PE² è uguale al rettangolo compreso fra PS e PS + SI + 2SD, cioè fra PS e 2LS + 2SD, cioè fra PS e 2LD.",
     "en": "Therefore PE2 is equal to the rectangle contained under PS and PS + SI + 2SD; that is, under PS and 2LS + 2SD; that is, under PS and 2LD.",
     "dipende_da": [],
     "figura": {
      "mostra": [
       "segmenti LS, LD"
      ],
      "evidenzia": [
       "PE² = PS × 2LD"
      ]
     },
     "nota": "«&» della trascrizione fra le formule = «e» (PS e …)."
    },
    {
     "id": "L1-P81-p4",
     "la": "",
     "it": "Inoltre DE² è uguale a SE² − SD², ossia a SE² − LS² + 2SLD − LD², cioè a 2SLD − LD² − ALB.",
     "en": "Moreover DE2 is equal to SE2 - SD2, or SE2 - LS2 + 2SLD - LD2, that is, 2SLD - LD2 - ALB.",
     "dipende_da": [],
     "figura": {
      "mostra": [
       "DE"
      ],
      "evidenzia": [
       "DE² = 2SL×LD − LD² − AL×LB"
      ]
     }
    },
    {
     "id": "L1-P81-p5",
     "la": "",
     "it": "Infatti LS² − SE², ossia LS² − SA², è uguale (per la Prop. VI del libro II degli *Elementi*) al rettangolo ALB.",
     "en": "For LS2 - SE2 or LS2 - SA2 (by Prop. VI, Book II, Elem.) is equal to the rectangle ALB.",
     "dipende_da": [
      "Euclide, Elementi II, 6"
     ],
     "figura": {
      "mostra": [
       "segmenti LA, LB"
      ],
      "evidenzia": [
       "LS² − SA² = AL × LB"
      ]
     }
    },
    {
     "id": "L1-P81-p6",
     "la": "",
     "it": "Si scriva dunque 2SLD − LD² − ALB al posto di DE²; e la quantità DE²×PS/(PE×V), che secondo il quarto corollario della proposizione precedente è come la lunghezza dell’ordinata DN, si risolverà in tre parti: 2SLD×PS/(PE×V) − LD²×PS/(PE×V) − ALB×PS/(PE×V). Se qui al posto di V si scrive il rapporto inverso della forza centripeta, e al posto di PE la media proporzionale fra PS e 2LD, quelle tre parti diventeranno le ordinate di altrettante curve, le cui aree si conoscono con i metodi comuni. C.V.F.",
     "en": "Therefore if instead of DE2 we write 2SLD - LD2 - ALB, the quantity [SVG 265], which (by Cor. 4 of the foregoing Prop.) is as the length of the ordinate DN, will now resolve itself into three parts [SVG 266]; where if instead of V we write the inverse ratio of the centripetal force, and instead of PE the mean proportional between PS and 2LD, those three parts will become ordinates to so many curve lines, whose areas are discovered by the common methods. Q.E.D.",
     "dipende_da": [
      "Prop. LXXX, Cor. 4"
     ],
     "figura": {
      "mostra": [
       "ordinata DN scomposta in tre parti"
      ],
      "evidenzia": [
       "tre curve, tre aree"
      ]
     },
     "nota": "Motte chiude con «Q.E.D.»; il latino ha «Q.E.F.» (è un problema)."
    }
   ]
  },
  {
   "id": "L1-P81-Ex1",
   "tipo": "Exemplum (Problema)",
   "titolo": "Prop. LXXXI, Esempio 1 — forze inversamente come la distanza",
   "copertura": [
    "S12.58"
   ],
   "fonti": {
    "la": "",
    "en": "Motte 1846, pp. 229–230"
   },
   "figura_base": {
    "punti": [
     "L",
     "A",
     "S",
     "B",
     "l",
     "a",
     "b"
    ],
    "vincoli": [
     "Ll, Aa, Bb ⊥ asse",
     "Aa = LB, Bb = LA",
     "iperbole ab di asintoti Ll, LB"
    ]
   },
   "passi": [
    {
     "id": "L1-P81-Ex1-p1",
     "la": "",
     "it": "Se la forza centripeta che tende alle singole particelle della sfera è inversamente come la distanza, al posto di V scrivi la distanza PE; poi 2PS×LD al posto di PE²; e DN diventerà come SL − ½LD − ALB/2LD.",
     "en": "If the centripetal force tending to the several particles of the sphere be reciprocally as the distance; instead of V write PE the distance, then 2PS × LD for PE2; and DN will become as [SVG 267].",
     "dipende_da": [],
     "figura": {
      "mostra": [
       "asse PAB con L, A, S, B"
      ],
      "evidenzia": [
       "DN ∝ SL − ½LD − AL×LB/(2LD)"
      ]
     },
     "nota": "Formula appiattita, letta come in Motte (SVG 267)."
    },
    {
     "id": "L1-P81-Ex1-p2",
     "la": "",
     "it": "Poni DN uguale al suo doppio, 2SL − LD − ALB/LD: la parte data dell’ordinata, 2SL, condotta lungo la lunghezza AB, descriverà l’area rettangolare 2SL×AB; e la parte indefinita LD, condotta perpendicolarmente lungo la stessa lunghezza con moto continuo, con la legge che durante il moto, crescendo o decrescendo, sia sempre uguale alla lunghezza LD, descriverà l’area (LB² − LA²)/2, cioè l’area SL×AB; che, sottratta dall’area precedente 2SL×AB, lascia l’area SL×AB.",
     "en": "Suppose DN equal to its double [SVG 268]; and 2SL the given part of the ordinate drawn into the length AB will describe the rectangular area 2SL × AB; and the indefinite part LD, drawn perpendicularly into the same length with a continued motion, in such sort as in its motion one way or another it may either by increasing or decreasing remain always equal to the length LD, will describe the area [SVG 269], that is, the area SL × AB; which taken from the former area 2SL × AB, leaves the area SL × AB.",
     "dipende_da": [],
     "figura": {
      "mostra": [
       "rettangolo 2SL×AB",
       "trapezio descritto da LD"
      ],
      "evidenzia": [
       "(LB² − LA²)/2 = SL × AB"
      ]
     },
     "nota": "«descrescendo» della trascrizione: refuso probabile per «decrescendo»."
    },
    {
     "id": "L1-P81-Ex1-p3",
     "la": "",
     "it": "La terza parte, ALB/LD, condotta anch’essa perpendicolarmente lungo la stessa lunghezza con moto locale, descriverà un’area iperbolica; che, sottratta dall’area SL×AB, lascerà l’area cercata ANB.",
     "en": "But the third part [SVG 270], drawn after the same manner with a continued motion perpendicularly into the same length, will describe the area of an hyperbola, which subducted from the area SL × AB will leave ANB the area sought.",
     "dipende_da": [],
     "figura": {
      "mostra": [
       "curva iperbolica di ordinata ALB/LD"
      ],
      "evidenzia": [
       "ANB = SL×AB − area iperbolica"
      ]
     }
    },
    {
     "id": "L1-P81-Ex1-p4",
     "la": "",
     "it": "Di qui risulta la seguente costruzione del problema.",
     "en": "Whence arises this construction of the Problem.",
     "dipende_da": [],
     "figura": {
      "mostra": [],
      "evidenzia": []
     }
    },
    {
     "id": "L1-P81-Ex1-p5",
     "la": "",
     "it": "Nei punti L, A, B innalza le perpendicolari Ll, Aa, Bb, delle quali Aa sia uguale a LB e Bb a LA.",
     "en": "At the points, L, A, B, erect the perpendiculars Ll, Aa, Bb; making Aa equal to LB, and Bb equal to LA.",
     "dipende_da": [],
     "figura": {
      "mostra": [
       "perpendicolari Ll, Aa = LB, Bb = LA"
      ],
      "evidenzia": [
       "LA × Aa = LB × Bb"
      ]
     }
    },
    {
     "id": "L1-P81-Ex1-p6",
     "la": "",
     "it": "Con gli asintoti Ll, LB si descriva per i punti a, b l’iperbole ab.",
     "en": "Making Ll and LB asymptotes, describe through the points a, b, the hyperbolic curve ab.",
     "dipende_da": [],
     "figura": {
      "mostra": [
       "iperbole ab con asintoti Ll, LB"
      ],
      "evidenzia": []
     },
     "nota": "La trascrizione ha «per puncta ab» senza virgola."
    },
    {
     "id": "L1-P81-Ex1-p7",
     "la": "",
     "it": "E la corda ba, una volta condotta, racchiuderà un’area aba uguale all’area cercata ANB.",
     "en": "And the chord ba being drawn, will inclose the area aba equal to the area sought ANB.",
     "dipende_da": [],
     "figura": {
      "mostra": [
       "corda ba",
       "area aba (fra corda e iperbole)"
      ],
      "evidenzia": [
       "area aba = area ANB (con DN raddoppiata; nota N12)"
      ]
     }
    }
   ],
   "nota": "Esempio della Prop. LXXXI: l’enunciato è quello della proposizione (unità L1-P81)."
  },
  {
   "id": "L1-P81-Ex2",
   "tipo": "Exemplum (Problema)",
   "titolo": "Prop. LXXXI, Esempio 2 — forze inversamente come il cubo della distanza",
   "copertura": [
    "S12.59"
   ],
   "fonti": {
    "la": "",
    "en": "Motte 1846, p. 230"
   },
   "figura_base": {
    "punti": [
     "L",
     "A",
     "S",
     "I",
     "B",
     "l",
     "a",
     "s",
     "b"
    ],
    "vincoli": [
     "Ll, Aa, Ss, Bb ⊥ asse",
     "Ss = SI",
     "iperbole asb di asintoti Ll, LB"
    ]
   },
   "passi": [
    {
     "id": "L1-P81-Ex2-p1",
     "la": "",
     "it": "Se la forza centripeta che tende alle singole particelle della sfera è inversamente come il cubo della distanza, o (il che è lo stesso) come quel cubo diviso per un piano dato qualsiasi, scrivi PE³/2AS² al posto di V, poi 2PS×LD al posto di PE²; e DN diventerà come SL×AS²/(PS×LD) − AS²/2PS − ALB×AS²/(2PS×LD²), cioè (poiché PS, AS, SI sono in proporzione continua) come LSI/LD − ½SI − ALB×SI/2LD².",
     "en": "If the centripetal force tending to the several particles of the sphere be reciprocally as the cube of the distance, or (which is the same thing) as that cube applied to any given plane; write [SVG 271] for V, and 2PS × LD for PE2; and DN will become as [SVG 272] that is (because PS, AS, SI are continually proportional), as [SVG 273].",
     "dipende_da": [],
     "figura": {
      "mostra": [
       "asse con L, A, S, I, B"
      ],
      "evidenzia": [
       "PS : AS = AS : SI"
      ]
     },
     "nota": "Formule appiattite, lette come in Motte (SVG 271–273)."
    },
    {
     "id": "L1-P81-Ex2-p2",
     "la": "",
     "it": "Se le tre parti di questa si conducono lungo la lunghezza AB, la prima, LSI/LD, genererà un’area iperbolica; la seconda, ½SI, l’area ½AB×SI; la terza, ALB×SI/2LD², l’area ALB×SI/2LA − ALB×SI/2LB, cioè ½AB×SI.",
     "en": "If we draw then these three parts into the length AB, the first [SVG 274] will generate the area of an hyperbola; the second [SVG 275] the area [SVG 276]; the third [SVG 277] the area [SVG 278], that is, [SVG 276].",
     "dipende_da": [],
     "figura": {
      "mostra": [
       "tre aree"
      ],
      "evidenzia": [
       "terza area = ½AB × SI"
      ]
     }
    },
    {
     "id": "L1-P81-Ex2-p3",
     "la": "",
     "it": "Dalla prima si sottragga la somma della seconda e della terza, e rimarrà l’area cercata ANB.",
     "en": "From the first subduct the sum of the second and third, and there will remain ANB, the area sought.",
     "dipende_da": [],
     "figura": {
      "mostra": [],
      "evidenzia": [
       "ANB = area iperbolica − AB × SI"
      ]
     }
    },
    {
     "id": "L1-P81-Ex2-p4",
     "la": "",
     "it": "Di qui risulta la seguente costruzione del problema.",
     "en": "Whence arises this construction of the problem.",
     "dipende_da": [],
     "figura": {
      "mostra": [],
      "evidenzia": []
     }
    },
    {
     "id": "L1-P81-Ex2-p5",
     "la": "",
     "it": "Nei punti L, A, S, B innalza le perpendicolari Ll, Aa, Ss, Bb, delle quali Ss sia uguale a SI; e per il punto s, con gli asintoti Ll, LB, si descriva l’iperbole asb, che incontri le perpendicolari Aa, Bb in a e b; e il rettangolo 2ASI, sottratto dall’area iperbolica AasbB, lascerà l’area cercata ANB.",
     "en": "At the points L, A, S, B, erect the perpendiculars Ll Aa, Ss, Bb, of which suppose Ss equal to SI; and through the point s, to the asymptotes Ll, LB, describe the hyperbola asb meeting the perpendiculars Aa, Bb, in a and b; and the rectangle 2ASI, subducted from the hyperbolic area AasbB, will leave ANB the area sought.",
     "dipende_da": [],
     "figura": {
      "mostra": [
       "perpendicolari Ll, Aa, Ss = SI, Bb",
       "iperbole asb",
       "area AasbB",
       "rettangolo 2AS×SI"
      ],
      "evidenzia": [
       "ANB = AasbB − 2AS×SI (verifica numerica: nota N12)"
      ]
     }
    }
   ],
   "nota": "Esempio della Prop. LXXXI."
  },
  {
   "id": "L1-P81-Ex3",
   "tipo": "Exemplum (Problema)",
   "titolo": "Prop. LXXXI, Esempio 3 — forze inversamente come la quarta potenza della distanza",
   "copertura": [
    "S12.60"
   ],
   "fonti": {
    "la": "",
    "en": "Motte 1846, pp. 230–231"
   },
   "figura_base": {
    "punti": [
     "L",
     "A",
     "S",
     "I",
     "B",
     "P"
    ],
    "vincoli": [
     "come nella Prop. LXXXI; nessuna costruzione nuova nominata nel testo"
    ]
   },
   "passi": [
    {
     "id": "L1-P81-Ex3-p1",
     "la": "",
     "it": "Se la forza centripeta che tende alle singole particelle della sfera decresce in rapporto quadruplicato della distanza dalle particelle, scrivi PE⁴/2AS³ al posto di V, poi √(2PS×LD) al posto di PE; e DN diventerà come (SI²×SL/√(2SI)) × 1/√LD³ − (SI²/2√(2SI)) × 1/√LD − (SI²×ALB/2√(2SI)) × 1/√LD⁵.",
     "en": "If the centripetal force tending to the several particles of the spheres decrease in a quadruplicate ratio of the distance from the particles; write [SVG 279] for V, then [SVG 280] for PE, and DN will become as [SVG 281].",
     "dipende_da": [],
     "figura": {
      "mostra": [
       "asse con L, A, S, I, B"
      ],
      "evidenzia": [
       "DN con radicali di LD"
      ]
     },
     "nota": "La trascrizione ha perso i radicali («2PS×LD pro PE»): letto √(2PS×LD). Motte (SVG 280) stampa √(2PS + LD): errore di Motte 1846."
    },
    {
     "id": "L1-P81-Ex3-p2",
     "la": "",
     "it": "Le sue tre parti, condotte lungo la lunghezza AB, producono altrettante aree, cioè: 2SI²×SL/√(2SI) moltiplicato per (1/√LA − 1/√LB); SI²/√(2SI) moltiplicato per (√LB − √LA); e SI²×ALB/(3√(2SI)) moltiplicato per (1/√LA³ − 1/√LB³).",
     "en": "These three parts drawn into the length AB, produce so many areas, viz. [SVG 282] into [SVG 283]; [SVG 284] into [SVG 285]; and [SVG 286] into [SVG 287].",
     "dipende_da": [],
     "figura": {
      "mostra": [
       "tre aree"
      ],
      "evidenzia": []
     },
     "nota": "Radicali e frazioni persi nella trascrizione; ricostruiti con Motte (SVG 282–287) e verificati per integrazione."
    },
    {
     "id": "L1-P81-Ex3-p3",
     "la": "",
     "it": "E queste, dopo la debita riduzione, diventano 2SI²×SL/LI, SI² e SI² + 2SI³/3LI.",
     "en": "And these after due reduction come forth [SVG 288], [SVG 289], and [SVG 290].",
     "dipende_da": [],
     "figura": {
      "mostra": [],
      "evidenzia": [
       "uso di LA = (PS − AS)²/2PS, LB = (PS + AS)²/2PS"
      ]
     }
    },
    {
     "id": "L1-P81-Ex3-p4",
     "la": "",
     "it": "E queste, sottratte le ultime dalla prima, danno 4SI³/3LI.",
     "en": "And these by subducting the last from the first, become [SVG 291].",
     "dipende_da": [],
     "figura": {
      "mostra": [],
      "evidenzia": [
       "ANB = 4SI³/3LI"
      ]
     }
    },
    {
     "id": "L1-P81-Ex3-p5",
     "la": "",
     "it": "Perciò la forza totale con cui il corpuscolo P è tirato verso il centro della sfera è come SI³/PI, cioè inversamente come PS³×PI. C.V.T.",
     "en": "Therefore the entire force with which the corpuscle P is attracted towards the centre of the sphere is as [SVG 292], that is, reciprocally as [SVG 293] Q.E.I.",
     "dipende_da": [],
     "figura": {
      "mostra": [],
      "evidenzia": [
       "forza ∝ 1/(PS³ × PI) (verifica numerica: nota N12)"
      ]
     }
    }
   ],
   "nota": "Esempio della Prop. LXXXI. Il calcolo è interamente algebrico."
  },
  {
   "id": "L1-P82",
   "tipo": "Propositio/Theorema",
   "titolo": "Prop. LXXXII — corpuscolo interno I e punto esterno P",
   "copertura": [
    "S12.62",
    "S12.63",
    "S12.64"
   ],
   "fonti": {
    "la": "",
    "en": "Motte 1846, pp. 231–232"
   },
   "enunciato": {
    "la": "",
    "it": "In una sfera descritta con centro S e raggio SA, se si prendono SI, SA, SP in proporzione continua, dico che l’attrazione di un corpuscolo all’interno della sfera, in un luogo qualsiasi I, sta alla sua attrazione all’esterno della sfera, nel luogo P, nel rapporto composto dal rapporto subduplicato delle distanze dal centro IS, PS e dal rapporto subduplicato delle forze centripete che tendono al centro in quei luoghi P e I.",
    "en": "In a sphere described about the centre S with the interval SA, if there be taken SI, SA, SP continually proportional; I say, that the attraction of a corpuscle within the sphere in any place I is to its attraction without the sphere in the place P in a ratio compounded of the subduplicate ratio of IS, PS, the distances from the centre, and the subduplicate ratio of the centripetal forces tending to the centre in those places P and I."
   },
   "figura_base": {
    "punti": [
     "S",
     "A",
     "I",
     "P",
     "E",
     "D"
    ],
    "vincoli": [
     "sfera di centro S e raggio SA",
     "SI, SA, SP in proporzione continua (I interno, P esterno, sulla stessa semiretta)",
     "E punto qualsiasi della sfera; triangoli SPE ~ SEI"
    ]
   },
   "passi": [
    {
     "id": "L1-P82-p1",
     "la": "",
     "it": "Ferme restando le costruzioni fatte prima, ed essendo il corpo in un luogo qualsiasi P, l’ordinata DN è stata trovata come DE²×PS/(PE×V).",
     "en": "The things remaining as above constructed, and a corpuscle being in any place P, the ordinate DN was found to be as [SVG 294].",
     "dipende_da": [
      "Prop. LXXX, Cor. 4"
     ],
     "figura": {
      "mostra": [
       "sfera centro S raggio SA",
       "P esterno",
       "D, E, DN"
      ],
      "evidenzia": []
     }
    },
    {
     "id": "L1-P82-p2",
     "la": "",
     "it": "Dunque, se si conduce IE, quell’ordinata, per un altro luogo qualsiasi I del corpuscolo, mutando ciò che va mutato, diventerà come DE²×IS/(IE×V).",
     "en": "Therefore if [SVG 295] be drawn, that ordinate for any other place of the corpuscle, as I, will become (mutatis mutandis) as [SVG 296].",
     "dipende_da": [],
     "figura": {
      "mostra": [
       "I interno con SI × SP = SA²",
       "IE"
      ],
      "evidenzia": []
     },
     "nota": "«allio» della trascrizione: refuso probabile per «alio»."
    },
    {
     "id": "L1-P82-p3",
     "la": "",
     "it": "Poni che le forze centripete emananti da un punto qualsiasi E della sfera stiano fra loro, alle distanze IE, PE, come PEⁿ sta a IEⁿ (dove il numero n indica l’indice delle potenze di PE e di IE); e quelle ordinate diventeranno come DE²×PS/(PE×PEⁿ) e DE²×IS/(IE×IEⁿ), il cui rapporto reciproco è come PS×IE×IEⁿ sta a IS×PE×PEⁿ.",
     "en": "Suppose the centripetal forces flowing from any point of the sphere, as E, to be to each other at the distances [SVG 295] and [SVG 297] as [SVG 298] to [SVG 299] (where the number n denotes the index of the powers of PE and IE), and those ordinates will become as [SVG 300] and [SVG 301] whose ratio to each other is as [SVG 302] to [SVG 303].",
     "dipende_da": [],
     "figura": {
      "mostra": [
       "PE, IE"
      ],
      "evidenzia": [
       "rapporto delle ordinate"
      ]
     }
    },
    {
     "id": "L1-P82-p4",
     "la": "",
     "it": "Poiché, essendo SI, SE, SP in proporzione continua, i triangoli SPE, SEI sono simili, e quindi IE sta a PE come IS sta a SE, ossia a SA, al posto del rapporto di IE a PE scrivi il rapporto di IS a SA; e il rapporto delle ordinate diventerà quello di PS×IEⁿ a SA×PEⁿ.",
     "en": "Because SI, SE, SP are in continued proportion, the triangles SPE, SEI are alike; and thence IE is to PE as IS to SE or SA. For the ratio of IE to PE write the ratio of IS to SA; and the ratio of the ordinates becomes that of [SVG 304] to [SVG 305].",
     "dipende_da": [],
     "figura": {
      "mostra": [
       "triangoli SPE ~ SEI"
      ],
      "evidenzia": [
       "IE : PE = IS : SA, costante per ogni E"
      ]
     }
    },
    {
     "id": "L1-P82-p5",
     "la": "",
     "it": "Ma il rapporto di PS a SA è il subduplicato del rapporto delle distanze PS, SI; e il rapporto di IEⁿ a PEⁿ (poiché IE sta a PE come IS sta a SA) è il subduplicato del rapporto delle forze alle distanze PS, IS.",
     "en": "But the ratio of PS to SA is subduplicate of that of the distances PS, SI; and the ratio of [SVG 299] to [SVG 298] (because IE is to PE as IS to SA) is subduplicate of that of the forces at the distances PS, IS.",
     "dipende_da": [],
     "figura": {
      "mostra": [],
      "evidenzia": [
       "PS/SA = √(PS/SI)",
       "(IE/PE)ⁿ = √(f(PS)/f(IS))"
      ]
     }
    },
    {
     "id": "L1-P82-p6",
     "la": "",
     "it": "Dunque le ordinate, e perciò le aree che le ordinate descrivono e le attrazioni proporzionali a esse, stanno nel rapporto composto da quei rapporti subduplicati. C.V.D.",
     "en": "Therefore the ordinates, and consequently the areas which the ordinates describe, and the attractions proportional to them, are in a ratio compounded of those subduplicate ratios. Q.E.D.",
     "dipende_da": [],
     "figura": {
      "mostra": [
       "aree sotto le due curve"
      ],
      "evidenzia": [
       "F(I) : F(P) composto dai due rapporti subduplicati (verifica numerica: nota N13)"
      ]
     }
    }
   ],
   "nota": "I passi coprono la dimostrazione (S12.64); gli esempi numerici di S12.63 non hanno costruzione e restano nel testo."
  },
  {
   "id": "L1-P83",
   "tipo": "Propositio/Problema",
   "titolo": "Prop. LXXXIII — corpuscolo nel centro e segmento sferico",
   "copertura": [
    "S12.65",
    "S12.66"
   ],
   "fonti": {
    "la": "",
    "en": "Motte 1846, pp. 232–233"
   },
   "enunciato": {
    "la": "",
    "it": "Trovare la forza con cui un corpuscolo collocato nel centro di una sfera è attratto verso un suo segmento qualsiasi.",
    "en": "To find the force with which a corpuscle placed in the centre of a sphere is attracted towards any segment of that sphere whatsoever."
   },
   "figura_base": {
    "punti": [
     "P",
     "R",
     "B",
     "S",
     "D",
     "E",
     "F",
     "G",
     "N",
     "I"
    ],
    "vincoli": [
     "P centro della sfera",
     "segmento RBSD delimitato dal piano RDS",
     "superficie sferica EFG di centro P",
     "FN ⊥ DB"
    ]
   },
   "passi": [
    {
     "id": "L1-P83-p1",
     "la": "",
     "it": "Sia P il corpo nel centro della sfera, e RBSD un suo segmento, delimitato dal piano RDS e dalla superficie sferica RBS.",
     "en": "Let P be a body in the centre of that sphere and RBSD a segment thereof contained under the plane RDS, and the sphærical superficies RBS.",
     "dipende_da": [],
     "figura": {
      "mostra": [
       "sfera di centro P",
       "segmento RBSD",
       "piano RDS",
       "asse PDB"
      ],
      "evidenzia": []
     }
    },
    {
     "id": "L1-P83-p2",
     "la": "",
     "it": "Con una superficie sferica EFG descritta con centro P si tagli DB in F, e si divida il segmento nelle parti BREFGS, FEDG.",
     "en": "Let DB be cut in F by a sphærical superficies EFG described from the centre P, and let the segment be divided into the parts BREFGS, FEDG.",
     "dipende_da": [],
     "figura": {
      "mostra": [
       "superficie sferica EFG (centro P)",
       "F su DB"
      ],
      "evidenzia": []
     }
    },
    {
     "id": "L1-P83-p3",
     "la": "",
     "it": "Quella superficie, poi, non sia puramente matematica, ma fisica, con una profondità piccolissima.",
     "en": "Let us suppose that segment to be not a purely mathematical but a physical superficies, having some, but a perfectly inconsiderable thickness.",
     "dipende_da": [],
     "figura": {
      "mostra": [
       "guscio sottile EFG"
      ],
      "evidenzia": []
     },
     "nota": "Motte scrive «that segment» per *superficies illa*: errore di riferimento."
    },
    {
     "id": "L1-P83-p4",
     "la": "",
     "it": "Si chiami O questa profondità: questa superficie sarà (per quanto è stato dimostrato da Archimede) come PF×DF×O.",
     "en": "Let that thickness be called O, and (by what Archimedes has demonstrated) that superficies will be as [SVG 306].",
     "dipende_da": [
      "Archimede"
     ],
     "figura": {
      "mostra": [
       "spessore O",
       "calotta EFG di altezza DF"
      ],
      "evidenzia": [
       "area calotta ∝ PF × DF"
      ]
     },
     "nota": "«demonstata» della trascrizione: refuso probabile per «demonstrata»."
    },
    {
     "id": "L1-P83-p5",
     "la": "",
     "it": "Poniamo inoltre che le forze attrattive delle particelle della sfera siano inversamente come quella potenza delle distanze il cui indice è n; e la forza con cui la superficie EFG tira il corpo P sarà (per la Prop. LXXIX) come DE²×O/PFⁿ, cioè come 2DF×O/PFⁿ⁻¹ − DF²×O/PFⁿ.",
     "en": "Let us suppose besides the attractive forces of the particles of the sphere to be reciprocally as that power of the distances, of which n is index; and the force with which the superficies EFG attracts the body P will be (by Prop. LXXIX) as [SVG 307], that is, as [SVG 308].",
     "dipende_da": [
      "Prop. LXXIX"
     ],
     "figura": {
      "mostra": [
       "DE (raggio del cerchio di base della calotta)"
      ],
      "evidenzia": [
       "DE² = 2PF×DF − DF²"
      ]
     },
     "nota": "Lettura incerta: la trascrizione ha «DFq×O/PFn, id est, ut 2DF×O/PFn−1», che non è un’identità; tradotto secondo il senso e secondo Motte (SVG 307–308): DE²×O/PFⁿ = 2DF×O/PFⁿ⁻¹ − DF²×O/PFⁿ. Da verificare sulla stampa."
    },
    {
     "id": "L1-P83-p6",
     "la": "",
     "it": "A questa sia proporzionale la perpendicolare FN moltiplicata per O; e l’area curvilinea BDI, che l’ordinata FN descrive condotta con moto continuo lungo la lunghezza DB, sarà come la forza totale con cui l’intero segmento RBSD tira il corpo P. C.V.T.",
     "en": "Let the perpendicular FN drawn into O be proportional to this quantity; and the curvilinear area BDI, which the ordinate FN, drawn through the length DB with a continued motion will describe, will be as the whole force with which the whole segment RBSD attracts the body P. Q.E.I.",
     "dipende_da": [],
     "figura": {
      "mostra": [
       "ordinata FN",
       "curva DI",
       "area BDI"
      ],
      "evidenzia": [
       "forza ∝ area BDI (verifica numerica: nota N14)"
      ]
     }
    }
   ]
  },
  {
   "id": "L1-P84",
   "tipo": "Propositio/Problema",
   "titolo": "Prop. LXXXIV — corpuscolo sull’asse di un segmento",
   "copertura": [
    "S12.67",
    "S12.68"
   ],
   "fonti": {
    "la": "",
    "en": "Motte 1846, p. 233"
   },
   "enunciato": {
    "la": "",
    "it": "Trovare la forza con cui un corpuscolo, collocato fuori del centro della sfera sull’asse di un segmento qualsiasi, è attratto da quel segmento.",
    "en": "To find the force with which a corpuscle, placed without the centre of a sphere in the axis of any segment, is attracted by that segment."
   },
   "figura_base": {
    "punti": [
     "P",
     "A",
     "D",
     "B",
     "E",
     "K",
     "F"
    ],
    "vincoli": [
     "segmento EBK di asse ADB",
     "P sull’asse fuori del centro",
     "superficie sferica EFK di centro P e raggio PE"
    ]
   },
   "passi": [
    {
     "id": "L1-P84-p1",
     "la": "",
     "it": "Dal segmento EBK sia tirato il corpo P, collocato sul suo asse ADB.",
     "en": "Let the body P placed in the axis ADB of the segment EBK be attracted by that segment.",
     "dipende_da": [],
     "figura": {
      "mostra": [
       "segmento EBK",
       "asse ADB",
       "P sull’asse, fuori del centro"
      ],
      "evidenzia": []
     }
    },
    {
     "id": "L1-P84-p2",
     "la": "",
     "it": "Con centro P e raggio PE si descriva la superficie sferica EFK, che divida il segmento in due parti, EBKFE ed EFKDE.",
     "en": "About the centre P, with the interval PE, let the sphærical superficies EFK be described; and let it divide the segment into two parts EBKFE and EFKDE.",
     "dipende_da": [],
     "figura": {
      "mostra": [
       "superficie sferica EFK (centro P, raggio PE)",
       "parti EBKFE, EFKDE"
      ],
      "evidenzia": []
     }
    },
    {
     "id": "L1-P84-p3",
     "la": "",
     "it": "Si cerchi la forza della prima parte per la Prop. LXXXI e quella della seconda per la Prop. LXXXIII: la somma delle forze sarà la forza dell’intero segmento EBKDE. C.V.T.",
     "en": "Find the force of the first of those parts by Prop. LXXXI, and the force of the latter part by Prop. LXXXIII, and the sum of the forces will be the force of the whole segment EBKDE. Q.E.I.",
     "dipende_da": [
      "Prop. LXXXI",
      "Prop. LXXXIII"
     ],
     "figura": {
      "mostra": [],
      "evidenzia": [
       "forza totale = somma delle due"
      ]
     }
    }
   ]
  }
 ]
}
```
