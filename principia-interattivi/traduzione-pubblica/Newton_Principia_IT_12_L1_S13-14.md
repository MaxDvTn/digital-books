> **Copia pubblica.** In questa versione i campi `"la"` della Parte B sono vuoti: le frasi latine vengono dalla trascrizione del Newton Project, che non si ridistribuisce. Il latino del 1726 si legge su newtonproject.ox.ac.uk.

# Isaac Newton
# Principi matematici della filosofia naturale

## Fascicolo 12 — Libro I, Sezioni XIII e XIV

**Nuova traduzione italiana di lavoro dal latino del 1726, confrontata con l’inglese di Andrew Motte nell’edizione del 1846.**

Versione 0.1 — 8 novembre 2026. Preparata con Claude (Anthropic) per Massimo Bosetti.

### Stato e perimetro

Questo fascicolo traduce integralmente le ultime due Sezioni del Libro I (*De motu corporum*):

- **Sezione XIII**, *De corporum non sphæricorum viribus attractivis*: Proposizioni LXXXV–XCIII con i loro corollari e lo Scolio della Sezione;
- **Sezione XIV**, *De motu corporum minimorum, quæ viribus centripetis ad singulas magni alicujus corporis partes tendentibus agitantur*: Proposizioni XCIV–XCVIII (rifrazione, riflessione, superfici che fanno convergere i corpuscoli), lo Scolio sulla luce dopo la Prop. XCVI e lo Scolio finale, con cui si chiude il Libro I.

È una traduzione di lavoro, non un’edizione critica validata. Gli identificatori **S13.01–S13.36** e **S14.01–S14.17** e i titoli tematici tra parentesi sono aggiunte editoriali; i numeri romani delle proposizioni, dei teoremi, dei problemi e dei corollari appartengono al testo. Le integrazioni del curatore sono tra parentesi quadre. Le note poste dopo la traduzione non fanno parte del testo di Newton.

In coda al fascicolo, la **Parte B** contiene i dati strutturati per le pagine interattive delle proposizioni e dei corollari che hanno figura e dimostrazione geometrica (11 unità).

### Fonti effettivamente consultate

1. **Latino di riferimento.** Isaac Newton, *Philosophiæ Naturalis Principia Mathematica*, terza edizione, Londra, 1726, Libro I: Sezione XIII, pp. 210–222; Sezione XIV, pp. 222–229 (secondo i marcatori di pagina della trascrizione; la fine della Sezione XIV cade a p. 229 o oltre, perché dopo il marcatore 〈229〉 la trascrizione non ne riporta altri). Trascrizione normalizzata del Newton Project, documento **NATP00087**, nei file di lavoro `fonti/latino-1726-L1-S13.md` e `fonti/latino-1726-L1-S14.md`, estratti in testo semplice senza correzioni. Per controllare i rimandi interni ho letto, negli stessi file di lavoro, gli enunciati delle Prop. VIII, XXXIX, LXX, LXXII (Cor. 3), LXXIV, LXXX–LXXXII.
2. **Inglese di confronto.** *Newton’s Principia*, traduzione di Andrew Motte, New York, Daniel Adee, 1846, Sezione XIII, pp. 233–243, e Sezione XIV, pp. 243–249, secondo i marcatori di pagina dell’EPUB Project Gutenberg n. 76404. Estratti di lavoro: `fonti/motte-1846-L1-S13.md` e `-S14.md`. Le formule stampate come immagini (SVG 191 e 309–351) sono state rese in PNG con `rsvg-convert` e lette una per una.
3. **Fascicolo 3** del progetto e brief comune, per il formato, i criteri e il glossario.

Non ho consultato né riprodotto traduzioni moderne. Non ho avuto accesso alle figure originali (NATP00087, figure 151–167) né alla stampa del 1726: le relazioni geometriche sono ricostruite soltanto dalle lettere del testo e controllate con figure di prova numeriche.

### Criteri di traduzione

- Il testo guida è il latino; l’inglese serve a controllare le interpretazioni ed è annotato quando aggiunge, omette o sbaglia.
- Si applica il **glossario comune** del brief (Fascicoli 1–3 e termini tecnici del Libro I): in particolare *vis acceleratrix* «forza acceleratrice», *vis centripeta* «forza centripeta», *ratio duplicata / triplicata / subduplicata* «rapporto duplicato / triplicato / subduplicato», *reciproce* «inversamente», *conjunctim* «considerate congiuntamente», *ducere in* «moltiplicare per», *in directum* «in linea retta», *impulsus* «spinta», *reflexio* «riflessione», *attractio* «attrazione», *particula* «particella», *globus* «globo», *ordinatim applicata* «ordinata», *latus rectum* «lato retto», *vertex principalis* «vertice principale», *sectio conica* «sezione conica», *Cas.* «Caso», *Corol.* «Cor.», Q.E.D. «C.V.D.», Q.E.I. «C.V.T.», Q.E.F. «C.V.F.».
- Le estensioni del glossario proprie di questo fascicolo (*corpusculum*, *orbis* nel senso di guscio sferico, *dignitas / potestas*, *latus* e *index* di una potenza, *in recessu*, *contentum*, *medium*, *sinus incidentiæ / emergentiæ*, *ex æquo*, *convertendo*, *divisim*, *ratio dimidiata* e altre) sono elencate e motivate nel § A.0.
- Gli enunciati all’infinito sono resi con l’indicativo; i problemi (*invenire*, *determinare*) con l’infinito italiano.
- Notazione delle formule nel testo tradotto: AB quad., ABq → AB²; A cub. → A³; Aqq → A⁴; i prodotti con «×»; le frazioni con la barra (AP × FK / PE); il vinculum di Newton (A+B¯ × GZ, «1 in PE−AD¯») è reso con parentesi tonde: (A + B) × GZ, 1 × (PE − AD). Gli esponenti letterali, che Newton stesso scrive come esponenti (Dⁿ, CGⁿ⁻³, A^(m/n)), sono resi con apici Unicode quando esistono e altrimenti con la forma A^(m/n); la scelta è dichiarata qui e non introduce formule moderne nel testo.
- I nomi propri latinizzati sono resi nella forma moderna (Galileo, Snell, Descartes, Grimaldi), con la forma latina nell’apparato.

---

## Traduzione italiana

### Sezione XIII. Le forze attrattive dei corpi non sferici

### Proposizione LXXXV. Teorema XLII (attrazione al contatto e legge più che duplicata)

**[S13.01]** **Se l’attrazione di un corpo attratto, quando è contiguo al corpo attraente, è molto più forte di quando essi sono separati l’uno dall’altro anche da un intervallo minimo, le forze delle particelle del corpo attraente, man mano che il corpo attratto si allontana, decrescono in un rapporto più che duplicato delle distanze dalle particelle.**

**[S13.02]** Se infatti le forze decrescono in rapporto duplicato delle distanze dalle particelle, l’attrazione verso un corpo sferico, poiché (per la Prop. LXXIV) è inversamente come il quadrato della distanza del corpo attratto dal centro della sfera, non sarà sensibilmente aumentata dal contatto; e lo sarà ancora meno se l’attrazione, man mano che il corpo attratto si allontana, decresce in un rapporto minore. La proposizione è dunque evidente per le sfere attrattive. E lo stesso vale per i gusci sferici concavi che attraggono corpi esterni. E molto più la cosa risulta per i gusci che attraggono corpi posti al loro interno, poiché le attrazioni diffuse ovunque nelle cavità dei gusci sono annullate (per la Prop. LXX) dalle attrazioni contrarie, e perciò sono nulle anche nel contatto stesso. Se poi da queste sfere e da questi gusci sferici si tolgono parti qualsiasi lontane dal luogo del contatto, e si aggiungono parti nuove dovunque, le figure di questi corpi attrattivi possono essere mutate a piacere; e tuttavia le parti aggiunte o sottratte, essendo lontane dal luogo del contatto, non accresceranno in modo notevole l’eccesso di attrazione che nasce dal contatto. La proposizione vale dunque per i corpi di tutte le figure. C.V.D.

### Proposizione LXXXVI. Teorema XLIII (legge triplicata: attrazione infinita al contatto)

**[S13.03]** **Se le forze delle particelle di cui è composto un corpo attrattivo decrescono, man mano che il corpo attratto si allontana, in rapporto triplicato o più che triplicato delle distanze dalle particelle, l’attrazione sarà molto più forte nel contatto che quando il corpo attraente e quello attratto sono separati l’uno dall’altro anche da un intervallo minimo.**

**[S13.04]** Che infatti l’attrazione, quando il corpuscolo attratto si avvicina a una sfera attraente di questo genere, cresca all’infinito, risulta dalla soluzione del Problema XLI [Prop. LXXXI] esposta nel secondo e nel terzo esempio. Lo stesso, confrontando fra loro quegli esempi e il Teorema XLI [Prop. LXXXII], si ricava facilmente per le attrazioni dei corpi verso gusci concavo-convessi, sia che i corpi attratti siano collocati fuori dei gusci, sia dentro, nelle loro cavità. Ma anche aggiungendo o togliendo a queste sfere e a questi gusci, dovunque fuori del luogo del contatto, una qualsiasi materia attrattiva, in modo che i corpi attrattivi assumano una qualsiasi figura assegnata, la proposizione risulterà valida per tutti i corpi. C.V.D.

### Proposizione LXXXVII. Teorema XLIV (corpi simili)

**[S13.05]** **Se due corpi simili fra loro, e costituiti di materia ugualmente attrattiva, attraggono separatamente corpuscoli proporzionali ai corpi stessi e posti in modo simile rispetto a essi, le attrazioni acceleratrici dei corpuscoli verso i corpi interi staranno come le attrazioni acceleratrici dei corpuscoli verso particelle di quei corpi proporzionali agli interi e poste in modo simile negli interi.**

**[S13.06]** Se infatti i corpi si dividono in particelle che siano proporzionali agli interi e poste in modo simile negli interi, come l’attrazione verso una particella qualsiasi di un corpo sta all’attrazione verso la particella corrispondente nell’altro corpo, così le attrazioni verso le singole particelle del primo corpo staranno alle attrazioni verso le singole particelle corrispondenti dell’altro; e, per composizione, così l’attrazione verso l’intero primo corpo starà all’attrazione verso l’intero secondo. C.V.D.

**[S13.07]** *Cor. 1.* Dunque, se le forze attrattive delle particelle, al crescere delle distanze dei corpuscoli attratti, decrescono nel rapporto di una qualsiasi potenza delle distanze, le attrazioni acceleratrici verso i corpi interi staranno direttamente come i corpi e inversamente come quelle potenze delle distanze. Per esempio, se le forze delle particelle decrescono in rapporto duplicato delle distanze dai corpuscoli attratti, e i corpi stanno come A³ e B³, e perciò tanto i lati cubici dei corpi quanto le distanze dei corpuscoli attratti dai corpi stanno come A e B, le attrazioni acceleratrici verso i corpi staranno come A³/A² e B³/B², cioè come quei lati cubici dei corpi, A e B. Se le forze delle particelle decrescono in rapporto triplicato delle distanze dai corpuscoli attratti, le attrazioni acceleratrici verso i corpi interi staranno come A³/A³ e B³/B³, cioè saranno uguali. Se le forze decrescono in rapporto quadruplicato, le attrazioni verso i corpi staranno come A³/A⁴ e B³/B⁴, cioè inversamente come i lati cubici A e B. E così negli altri casi.

**[S13.08]** *Cor. 2.* Di qui, viceversa, dalle forze con cui corpi simili attraggono corpuscoli posti in modo simile rispetto a essi, si può ricavare il rapporto del decremento delle forze delle particelle attrattive man mano che il corpuscolo attratto si allontana, purché quel decremento sia direttamente o inversamente in un qualche rapporto delle distanze.

### Proposizione LXXXVIII. Teorema XLV (forze proporzionali alla distanza: il centro di gravità)

**[S13.09]** **Se le forze attrattive delle particelle uguali di un corpo qualsiasi sono come le distanze dei luoghi dalle particelle, la forza del corpo intero tenderà al suo centro di gravità; e sarà la stessa della forza di un globo costituito di materia del tutto simile e uguale, e avente il centro nel centro di gravità del corpo.**

**[S13.10]** Le particelle A, B del corpo RSTV attraggano un corpuscolo Z con forze che, se le particelle sono uguali fra loro, stiano come le distanze AZ, BZ; se invece le particelle si suppongono disuguali, stiano come queste particelle e le loro distanze AZ, BZ considerate congiuntamente, ossia (se così posso dire) come queste particelle moltiplicate rispettivamente per le loro distanze AZ, BZ. E si rappresentino queste forze con quei prodotti A × AZ e B × BZ. Si congiunga AB, e la si tagli in G in modo che AG stia a BG come la particella B sta alla particella A: G sarà il centro comune di gravità delle particelle A e B. La forza A × AZ (per il Cor. 2 delle leggi) si scompone nelle forze A × GZ e A × AG, e la forza B × BZ nelle forze B × GZ e B × BG. Ma le forze A × AG e B × BG, poiché A sta a B come BG sta ad AG, sono uguali; e perciò, essendo dirette verso parti contrarie, si distruggono a vicenda. Restano le forze A × GZ e B × GZ. Queste tendono da Z verso il centro G e compongono la forza (A + B) × GZ: cioè la stessa forza che si avrebbe se le particelle attrattive A e B si trovassero nel loro centro comune di gravità G, componendovi un globo.

**[S13.11]** Con lo stesso argomento, se si aggiunge una terza particella C e si compone la sua forza con la forza (A + B) × GZ che tende al centro G, la forza che ne nasce tenderà al centro comune di gravità di quel globo in G e della particella C, cioè al centro comune di gravità delle tre particelle A, B, C; e sarà la stessa che si avrebbe se il globo e la particella C si trovassero in quel centro comune, componendovi un globo maggiore. E così si procede all’infinito. Dunque la forza totale di tutte le particelle di un corpo qualsiasi RSTV è la stessa che si avrebbe se quel corpo, conservando il centro di gravità, assumesse la figura di un globo. C.V.D.

**[S13.12]** *Cor.* Di qui il moto del corpo attratto Z sarà lo stesso che si avrebbe se il corpo attraente RSTV fosse sferico; e perciò, se quel corpo attraente è in quiete o avanza uniformemente in linea retta, il corpo attratto si muoverà in un’ellisse che ha il centro nel centro di gravità del corpo attraente.

### Proposizione LXXXIX. Teorema XLVI (più corpi)

**[S13.13]** **Se vi sono più corpi costituiti di particelle uguali, le cui forze sono come le distanze dei luoghi da ciascuna di esse, la forza composta dalle forze di tutti, con cui un corpuscolo qualsiasi è attratto, tenderà al centro comune di gravità dei corpi attraenti; e sarà la stessa che si avrebbe se quei corpi attraenti, conservando il centro comune di gravità, si riunissero e fossero formati in un globo.**

**[S13.14]** Si dimostra nello stesso modo della proposizione precedente.

**[S13.15]** *Cor.* Dunque il moto del corpo attratto sarà lo stesso che si avrebbe se i corpi attraenti, conservando il centro comune di gravità, si riunissero e fossero formati in un globo. E perciò, se il centro comune di gravità dei corpi attraenti è in quiete o avanza uniformemente in linea retta, il corpo attratto si muoverà in un’ellisse che ha il centro in quel centro comune di gravità dei corpi attraenti.

### Proposizione XC. Problema XLIV (attrazione di un cerchio su un punto del suo asse)

**[S13.16]** **Se verso i singoli punti di un cerchio qualsiasi tendono forze centripete uguali, crescenti o decrescenti in un rapporto qualsiasi delle distanze, trovare la forza con cui è attratto un corpuscolo posto in un punto qualsiasi della retta che si innalza perpendicolarmente al piano del cerchio nel suo centro.**

**[S13.17]** Con centro A e con un raggio qualsiasi AD, in un piano al quale è perpendicolare la retta AP, si immagini descritto un cerchio; e si debba trovare la forza con cui un corpuscolo qualsiasi P è attratto verso di esso. Da un punto qualsiasi E del cerchio si conduca la retta PE al corpuscolo attratto P. Sulla retta PA si prenda PF uguale a PE, e si innalzi la normale FK, che sia come la forza con cui il punto E attrae il corpuscolo P. E sia IKL la linea curva che il punto K tocca continuamente. Essa incontri il piano del cerchio in L. Su PA si prenda PH uguale a PD, e si innalzi la perpendicolare HI, che incontri in I la curva suddetta: l’attrazione del corpuscolo P verso il cerchio sarà come l’area AHIL moltiplicata per l’altezza AP. C.V.T.

**[S13.18]** Su AE si prenda infatti una linea piccolissima Ee. Si congiunga Pe, e su PE, PA si prendano PC, Pf uguali a Pe. E poiché la forza con cui un punto qualsiasi E dell’anello, descritto con centro A e raggio AE nel piano suddetto, attrae a sé il corpo P si suppone come FK, e quindi la forza con cui quel punto attrae il corpo P verso A è come AP × FK / PE, e la forza con cui l’intero anello attrae il corpo P verso A è come l’anello e AP × FK / PE considerati congiuntamente; e poiché quell’anello è come il rettangolo compreso dal raggio AE e dalla larghezza Ee, e questo rettangolo (poiché PE sta ad AE come Ee sta a CE) è uguale al rettangolo PE × CE, ossia PE × Ff; la forza con cui quell’anello attrae il corpo P verso A sarà come PE × Ff e AP × FK / PE considerati congiuntamente, cioè come il prodotto Ff × FK × AP, ossia come l’area FKkf moltiplicata per AP. E perciò la somma delle forze con cui tutti gli anelli del cerchio descritto con centro A e raggio AD attraggono il corpo P verso A è come l’area totale AHIKL moltiplicata per AP. C.V.D.

**[S13.19]** *Cor. 1.* Di qui, se le forze dei punti decrescono in rapporto duplicato delle distanze, cioè se FK è come 1/PF², e perciò l’area AHIKL come 1/PA − 1/PH, l’attrazione del corpuscolo P verso il cerchio sarà come 1 − PA/PH, cioè come AH/PH.

**[S13.20]** *Cor. 2.* E in generale, se le forze dei punti alle distanze D sono inversamente come una potenza qualsiasi Dⁿ delle distanze, cioè se FK è come 1/Dⁿ, e perciò l’area AHIKL come 1/PAⁿ⁻¹ − 1/PHⁿ⁻¹, l’attrazione del corpuscolo P verso il cerchio sarà come 1/PAⁿ⁻² − PA/PHⁿ⁻¹.

**[S13.21]** *Cor. 3.* E se il diametro del cerchio cresce all’infinito, e il numero n è maggiore dell’unità, l’attrazione del corpuscolo P verso l’intero piano infinito sarà inversamente come PAⁿ⁻², poiché l’altro termine, PA/PHⁿ⁻¹, svanisce.

### Proposizione XCI. Problema XLV (solido rotondo; cilindro e sferoide)

**[S13.22]** **Trovare l’attrazione di un corpuscolo posto sull’asse di un solido rotondo, verso i cui singoli punti tendono forze centripete uguali, decrescenti in un rapporto qualsiasi delle distanze.**

**[S13.23]** Il corpuscolo P, posto sul suo asse AB, sia attratto verso il solido DECG. Si tagli questo solido con un cerchio qualsiasi RFS perpendicolare all’asse, e sul suo semidiametro FS, in un piano PALKB passante per l’asse, si prenda (per la Prop. XC) la lunghezza FK proporzionale alla forza con cui il corpuscolo P è attratto verso quel cerchio. Il punto K tocchi poi la linea curva LKI, che incontra in L e in I i piani dei cerchi estremi AL e BI: l’attrazione del corpuscolo P verso il solido sarà come l’area LABI. C.V.T.

**[S13.24]** *Cor. 1.* Di qui, se il solido è un cilindro, descritto dal parallelogramma ADEB fatto ruotare intorno all’asse AB, e le forze centripete che tendono ai suoi singoli punti sono inversamente come i quadrati delle distanze dai punti, l’attrazione del corpuscolo P verso questo cilindro sarà come AB − PE + PD. Infatti l’ordinata FK (per il Cor. 1 della Prop. XC) sarà come 1 − PF/PR. La sua parte 1, moltiplicata per la lunghezza AB, descrive l’area 1 × AB; e l’altra parte, PF/PR, moltiplicata per la lunghezza PB, descrive l’area 1 × (PE − AD), cosa che si può mostrare facilmente dalla quadratura della curva LKI; e similmente la stessa parte, moltiplicata per la lunghezza PA, descrive l’area 1 × (PD − AD), e, moltiplicata per AB, differenza di PB e PA, descrive la differenza delle aree, 1 × (PE − PD). Dal primo prodotto, 1 × AB, si tolga l’ultimo, 1 × (PE − PD): resterà l’area LABI uguale a 1 × (AB − PE + PD). Dunque la forza, proporzionale a quest’area, è come AB − PE + PD.

**[S13.25]** *Cor. 2.* Di qui si conosce anche la forza con cui uno sferoide AGBC attrae un corpo qualsiasi P, posto all’esterno sul suo asse AB. Sia NKRM una sezione conica la cui ordinata ER, perpendicolare a PE, sia sempre uguale alla lunghezza PD, condotta al punto D in cui quell’ordinata taglia lo sferoide. Dai vertici A, B dello sferoide si innalzino sul suo asse AB le perpendicolari AK, BM, uguali rispettivamente ad AP, BP, e che perciò incontrano la sezione conica in K e M; e si congiunga KM, che ne stacca il segmento KMRK. Siano poi S il centro dello sferoide e SC il suo semidiametro massimo: la forza con cui lo sferoide attrae il corpo P starà alla forza con cui una sfera descritta sul diametro AB attrae lo stesso corpo come (AS × CS² − PS × KMRK)/(PS² + CS² − AS²) sta ad AS³/(3PS²). E con lo stesso fondamento di calcolo si possono trovare le forze dei segmenti dello sferoide.

**[S13.26]** *Cor. 3.* Se poi il corpuscolo è collocato dentro lo sferoide, sull’asse, l’attrazione sarà come la sua distanza dal centro. Ciò si ricava più facilmente con questo argomento, sia che la particella si trovi sull’asse, sia su un qualsiasi altro diametro dato. Sia AGOF lo sferoide attraente, S il suo centro e P il corpo attratto. Per il corpo P si conducano sia il semidiametro SPA, sia due rette qualsiasi DE, FG, che incontrano lo sferoide da una parte e dall’altra in D ed E, F e G; e siano PCM, HLN le superfici di due sferoidi interni, simili all’esterno e concentrici, il primo dei quali passi per il corpo P e tagli le rette DE e FG in B e C, il secondo tagli le stesse rette in H, I e K, L. Abbiano poi tutti gli sferoidi l’asse in comune: le parti delle rette intercettate da una parte e dall’altra, DP e BE, FP e CG, DH e IE, FK e LG, saranno uguali fra loro, poiché le rette DE, PB e HI sono divise a metà nello stesso punto, come pure le rette FG, PC e KL. Immagina ora che DPF, EPG designino coni opposti, descritti con angoli al vertice DPF, EPG infinitamente piccoli, e che anche le linee DH, EI siano infinitamente piccole: le particelle dei coni tagliate dalle superfici degli sferoidi, DHKF, GLIE, per l’uguaglianza delle linee DH, EI staranno fra loro come i quadrati delle loro distanze dal corpuscolo P, e perciò attrarranno quel corpuscolo in egual misura. E per la stessa ragione, se gli spazi DPF, EGCB si dividono in particelle mediante le superfici di innumerevoli sferoidi simili, concentrici e aventi l’asse in comune, tutte queste particelle attrarranno in egual misura, da una parte e dall’altra, il corpo P verso parti contrarie. Sono dunque uguali le forze del cono DPF e del segmento conico EGCB, e per la loro contrarietà si distruggono a vicenda. E lo stesso vale per le forze di tutta la materia che sta fuori dello sferoide più interno PCBM. Il corpo P è dunque attratto soltanto dallo sferoide più interno PCBM; e perciò (per il Cor. 3 della Prop. LXXII) la sua attrazione sta alla forza con cui il corpo A è attratto dall’intero sferoide AGOD come la distanza PS sta alla distanza AS. C.V.D.

### Proposizione XCII. Problema XLVI (ricavare dall’esperienza la legge delle particelle)

**[S13.27]** **Dato un corpo attrattivo, trovare il rapporto del decremento delle forze centripete che tendono ai suoi singoli punti.**

**[S13.28]** Dal corpo dato si deve formare una sfera, o un cilindro, o un’altra figura regolare, la cui legge di attrazione, corrispondente a un qualsiasi rapporto di decremento, si può trovare (per le Prop. LXXX, LXXXI e XCI). Poi, fatti degli esperimenti, si deve trovare la forza di attrazione a diverse distanze; e la legge dell’attrazione verso l’intero, così rivelata, darà il rapporto del decremento delle forze delle singole parti, che si doveva trovare.

### Proposizione XCIII. Teorema XLVII (solido terminato da un piano)

**[S13.29]** **Se un solido, piano da una parte e infinito dalle altre, è costituito di particelle uguali e ugualmente attrattive, le cui forze, man mano che ci si allontana dal solido, decrescono nel rapporto di una potenza qualsiasi delle distanze più che quadratica, e un corpuscolo posto dall’una o dall’altra parte del piano è attratto dalla forza del solido intero, dico che quella forza attrattiva del solido, man mano che ci si allontana dalla sua superficie piana, decrescerà nel rapporto di una potenza il cui lato è la distanza del corpuscolo dal piano e il cui indice è minore di tre unità dell’indice della potenza delle distanze.**

**[S13.30]** *Caso 1.* Sia LGl il piano da cui il solido è terminato. Il solido giaccia dalla parte di questo piano che è verso I, e lo si scomponga in innumerevoli piani mHM, nIN, oKO ecc., paralleli a GL. E in primo luogo il corpo attratto C sia collocato fuori del solido. Si conduca CGHI perpendicolare a quegli innumerevoli piani, e le forze attrattive dei punti del solido decrescano nel rapporto di una potenza delle distanze il cui indice sia un numero n non minore di tre. Dunque (per il Cor. 3 della Prop. XC) la forza con cui un piano qualsiasi mHM attrae il punto C è inversamente come CHⁿ⁻². Nel piano mHM si prenda la lunghezza HM inversamente proporzionale a CHⁿ⁻²: quella forza sarà come HM. Similmente nei singoli piani lGL, nIN, oKO ecc. si prendano le lunghezze GL, IN, KO ecc. inversamente proporzionali a CGⁿ⁻², CIⁿ⁻², CKⁿ⁻² ecc.: le forze di quegli stessi piani saranno come le lunghezze prese, e quindi la somma delle forze come la somma delle lunghezze, cioè la forza del solido intero come l’area GLOK prolungata all’infinito verso OK. Ma quell’area (per i noti metodi delle quadrature) è inversamente come CGⁿ⁻³; e perciò la forza del solido intero è inversamente come CGⁿ⁻³. C.V.D.

**[S13.31]** *Caso 2.* Si collochi ora il corpuscolo C, dalla parte del piano lGL, dentro il solido, e si prenda la distanza CK uguale alla distanza CG. La parte del solido LGloKO, terminata dai piani paralleli lGL, oKO, non attrarrà in alcuna direzione il corpuscolo C, posto nel mezzo, poiché le azioni contrarie dei punti opposti si annullano a vicenda per la loro uguaglianza. Perciò il corpuscolo C è attratto dalla sola forza del solido situato oltre il piano OK. Ma questa forza (per il primo caso) è inversamente come CKⁿ⁻³, cioè (poiché CG e CK sono uguali) inversamente come CGⁿ⁻³. C.V.D.

**[S13.32]** *Cor. 1.* Di qui, se il solido LGIN è terminato da una parte e dall’altra da due piani infiniti paralleli LG, IN, se ne conosce la forza attrattiva sottraendo dalla forza attrattiva dell’intero solido infinito LGKO la forza attrattiva della parte più lontana NICO, prolungata all’infinito verso KO.

**[S13.33]** *Cor. 2.* Se la parte più lontana di questo solido infinito, quando la sua attrazione, confrontata con l’attrazione della parte più vicina, non ha quasi alcun peso, viene trascurata, l’attrazione di quella parte più vicina, al crescere della distanza, decrescerà con ottima approssimazione nel rapporto della potenza CGⁿ⁻³.

**[S13.34]** *Cor. 3.* E di qui, se un corpo finito qualsiasi, piano da una parte, attrae un corpuscolo posto di fronte al mezzo di quel piano, e la distanza fra il corpuscolo e il piano, confrontata con le dimensioni del corpo attraente, è piccolissima, e il corpo attraente è costituito di particelle omogenee le cui forze attrattive decrescono nel rapporto di una potenza qualsiasi delle distanze più che quadruplicata, la forza attrattiva del corpo intero decrescerà con ottima approssimazione nel rapporto di una potenza il cui lato sia quella distanza piccolissima e il cui indice sia minore di tre unità dell’indice della potenza precedente. Per un corpo costituito di particelle le cui forze attrattive decrescono nel rapporto della potenza triplicata delle distanze, l’asserzione non vale, poiché in questo caso l’attrazione di quella parte più lontana del corpo infinito, nel secondo corollario, è sempre infinitamente maggiore dell’attrazione della parte più vicina.

### Scolio (moti verso un piano; il metodo delle serie)

**[S13.35]** Se un corpo è attratto perpendicolarmente verso un piano dato, e dalla legge di attrazione data si cerca il moto del corpo, il problema si risolverà cercando (per la Prop. XXXIX) il moto del corpo che discende in linea retta verso questo piano e (per il Cor. 2 delle leggi) componendo questo moto con un moto uniforme fatto secondo linee parallele allo stesso piano. E, viceversa, se si cerca la legge dell’attrazione verso il piano, fatta secondo linee perpendicolari, a condizione che il corpo attratto si muova in una qualsiasi linea curva data, il problema si risolverà operando sull’esempio del terzo problema [Prop. VIII].

**[S13.36]** Le operazioni, però, si sogliono abbreviare risolvendo le ordinate in serie convergenti. Per esempio, se sulla base A, in un angolo dato qualsiasi, si applica come ordinata una lunghezza B che sia come una potenza qualsiasi della base, A^(m/n), e si cerca la forza con cui un corpo, attratto verso la base o respinto dalla base secondo la direzione dell’ordinata, possa muoversi nella linea curva che l’ordinata tocca sempre con il suo estremo superiore, suppongo che la base cresca di una parte piccolissima O, e risolvo l’ordinata (A + O)^(m/n) nella serie infinita A^(m/n) + (m/n) O A^((m−n)/n) + ((mm − mn)/2nn) OO A^((m−2n)/n) ecc.; e suppongo che la forza sia proporzionale al termine di questa serie in cui O ha due dimensioni, cioè al termine ((mm − mn)/2nn) OO A^((m−2n)/n). La forza cercata è dunque come ((mm − mn)/nn) A^((m−2n)/n), o, ciò che è lo stesso, come ((mm − mn)/nn) B^((m−2n)/m). Per esempio, se l’ordinata tocca una parabola, con m = 2 e n = 1, la forza risulterà come la quantità data 2B⁰, e quindi sarà data. Dunque con una forza data il corpo si muoverà in una parabola, come ha dimostrato Galileo. Se invece l’ordinata tocca un’iperbole, con m = 0 − 1 e n = 1, la forza risulterà come 2A⁻³, ossia 2B³; e perciò con una forza che sia come il cubo dell’ordinata il corpo si muoverà in un’iperbole. Ma, lasciate da parte proposizioni di questo genere, passo ad alcune altre sul moto, che non ho ancora toccato.

**Fine della Sezione XIII.**

### Sezione XIV. Il moto dei corpi minimi, agitati da forze centripete che tendono alle singole parti di un corpo molto grande

### Proposizione XCIV. Teorema XLVIII (legge dei seni)

**[S14.01]** **Se due mezzi omogenei sono separati l’uno dall’altro da uno spazio terminato da una parte e dall’altra da piani paralleli, e un corpo, nel passare attraverso questo spazio, è attratto o spinto perpendicolarmente verso l’uno o l’altro dei due mezzi, e non è mosso né ostacolato da alcun’altra forza; e se l’attrazione, a distanze uguali da ciascuno dei due piani prese dalla stessa parte di esso, è ovunque la stessa: dico che il seno d’incidenza su uno dei due piani starà al seno di emergenza dall’altro piano in un rapporto dato.**

**[S14.02]** *Caso 1.* Siano Aa, Bb due piani paralleli. Il corpo incida sul primo piano, Aa, secondo la linea GH; durante tutto il suo passaggio attraverso lo spazio intermedio sia attratto o spinto verso il mezzo d’incidenza, e per questa azione descriva la linea curva HI ed emerga secondo la linea IK. Sul piano di emergenza Bb si innalzi la perpendicolare IM, che incontri la linea d’incidenza GH, prolungata, in M, e il piano d’incidenza Aa in R; e la linea di emergenza KI, prolungata, incontri HM in L. Con centro L e raggio LI si descriva un cerchio, che tagli HM in P e Q, e MI prolungata in N. E in primo luogo, se l’attrazione o la spinta si suppone uniforme, la curva HI sarà (per ciò che ha dimostrato Galileo) una parabola, la cui proprietà è che il rettangolo formato dal lato retto dato e dalla linea IM è uguale al quadrato di HM; e inoltre la linea HM sarà divisa a metà in L. Perciò, se su MI si abbassa la perpendicolare LO, MO e OR saranno uguali; e, aggiunte le uguali ON, OI, risulteranno uguali le intere MN, IR. Quindi, poiché IR è data, è data anche MN; e il rettangolo NMI sta al rettangolo formato dal lato retto e da IM, cioè a HM², in un rapporto dato. Ma il rettangolo NMI è uguale al rettangolo PMQ, cioè alla differenza dei quadrati ML² e PL², ossia LI²; e HM² ha un rapporto dato con la sua quarta parte, ML²: è dato dunque il rapporto di ML² − LI² a ML², e, per conversione, il rapporto di LI² a ML², e il rapporto subduplicato, di LI a ML. Ma in ogni triangolo, e dunque in LMI, i seni degli angoli sono proporzionali ai lati opposti. È dato dunque il rapporto del seno dell’angolo d’incidenza LMR al seno dell’angolo di emergenza LIR. C.V.D.

**[S14.03]** *Caso 2.* Il corpo attraversi ora successivamente più spazi terminati da piani paralleli, AabB, BbcC ecc., e sia mosso da una forza che sia uniforme in ciascuno di essi separatamente, ma diversa nei diversi spazi. Per quanto si è appena dimostrato, il seno d’incidenza sul primo piano Aa starà al seno di emergenza dal secondo piano Bb in un rapporto dato; e questo seno, che è il seno d’incidenza sul secondo piano Bb, starà al seno di emergenza dal terzo piano Cc in un rapporto dato; e questo seno starà al seno di emergenza dal quarto piano Dd in un rapporto dato; e così all’infinito: e, per uguaglianza, il seno d’incidenza sul primo piano starà al seno di emergenza dall’ultimo piano in un rapporto dato. Si diminuiscano ora gli intervalli dei piani e se ne aumenti il numero all’infinito, in modo che l’azione dell’attrazione o della spinta, secondo una legge qualsiasi assegnata, sia resa continua: il rapporto del seno d’incidenza sul primo piano al seno di emergenza dall’ultimo piano, essendo sempre dato, sarà dato anche allora. C.V.D.

### Proposizione XCV. Teorema XLIX (velocità e seni)

**[S14.04]** **Poste le stesse cose, dico che la velocità del corpo prima dell’incidenza sta alla sua velocità dopo l’emergenza come il seno di emergenza sta al seno d’incidenza.**

**[S14.05]** Si prendano AH e Id uguali, e si innalzino le perpendicolari AG, dK, che incontrino le linee d’incidenza e di emergenza GH, IK in G e K. Su GH si prenda TH uguale a IK, e sul piano Aa si abbassi la normale Tv. E (per il Cor. 2 delle leggi) si distingua il moto del corpo in due: uno perpendicolare ai piani Aa, Bb, Cc ecc., l’altro parallelo a essi. La forza di attrazione o di spinta, agendo secondo linee perpendicolari, non muta affatto il moto secondo le parallele; e perciò il corpo, con questo moto, percorrerà in tempi uguali quegli intervalli uguali, presi secondo le parallele, che stanno fra la linea AG e il punto H e fra il punto I e la linea dK; cioè descriverà in tempi uguali le linee GH, IK. Quindi la velocità prima dell’incidenza sta alla velocità dopo l’emergenza come GH sta a IK, o a TH, cioè come AH, o Id, sta a vH, cioè (rispetto al raggio TH, o IK) come il seno di emergenza sta al seno d’incidenza. C.V.D.

### Proposizione XCVI. Teorema L (riflessione)

**[S14.06]** **Poste le stesse cose, e supposto che il moto prima dell’incidenza sia più veloce che dopo, dico che il corpo, inclinando la linea d’incidenza, sarà alla fine riflesso, e l’angolo di riflessione diventerà uguale all’angolo d’incidenza.**

**[S14.07]** Immagina infatti che il corpo descriva fra i piani paralleli Aa, Bb, Cc ecc. archi parabolici, come sopra; e siano questi archi HP, PQ, QR ecc. E l’obliquità della linea d’incidenza GH sul primo piano Aa sia tale che il seno d’incidenza stia al raggio del cerchio di cui è seno nel rapporto che lo stesso seno d’incidenza ha con il seno di emergenza dal piano Dd nello spazio DdeE: poiché il seno di emergenza è ormai divenuto uguale al raggio, l’angolo di emergenza sarà retto, e perciò la linea di emergenza coinciderà con il piano Dd. Il corpo giunga a questo piano nel punto R; e, poiché la linea di emergenza coincide con lo stesso piano, è evidente che il corpo non può procedere oltre verso il piano Ee. Ma non può neppure procedere lungo la linea di emergenza Rd, poiché è continuamente attratto o spinto verso il mezzo d’incidenza. Tornerà dunque indietro fra i piani Cc, Dd, descrivendo un arco di parabola QRq, il cui vertice principale (secondo ciò che ha dimostrato Galileo) è in R; taglierà il piano Cc in q con lo stesso angolo con cui prima lo aveva tagliato in Q; poi, procedendo negli archi parabolici qp, ph ecc., simili e uguali agli archi precedenti QP, PH, taglierà gli altri piani in p, h ecc. con gli stessi angoli con cui prima li aveva tagliati in P, H ecc., ed emergerà alla fine in h con la stessa obliquità con cui era incidente in H. Immagina ora che gli intervalli dei piani Aa, Bb, Cc, Dd, Ee ecc. diminuiscano all’infinito e che il loro numero aumenti, in modo che l’azione dell’attrazione o della spinta, secondo una legge qualsiasi assegnata, sia resa continua: l’angolo di emergenza, essendo sempre uguale all’angolo d’incidenza, resterà uguale a esso anche allora. C.V.D.

### Scolio (analogia con la luce)

**[S14.08]** Non molto dissimili da queste attrazioni sono le riflessioni e le rifrazioni della luce, fatte secondo un rapporto dato delle secanti, come trovò Snell, e di conseguenza secondo un rapporto dato dei seni, come espose Descartes. Che infatti la luce si propaghi successivamente e venga dal Sole alla Terra nello spazio di circa sette od otto minuti primi è ormai certo per i fenomeni dei satelliti di Giove, confermati dalle osservazioni di diversi astronomi. I raggi che si trovano nell’aria (come già da tempo trovò Grimaldi, facendo entrare la luce in una stanza buia attraverso un foro, e come ho sperimentato anch’io), nel loro passaggio vicino agli spigoli dei corpi, sia opachi sia trasparenti (quali sono gli orli circolari, a spigolo retto, delle monete coniate in oro, argento e rame, e i tagli dei coltelli, delle pietre o dei vetri rotti), si incurvano intorno ai corpi, come se fossero attratti verso di essi; e di questi raggi quelli che nel passaggio si avvicinano di più ai corpi si incurvano di più, come se fossero attratti di più, come anch’io ho osservato con cura. E quelli che passano a distanze maggiori si incurvano meno; e a distanze ancora maggiori si incurvano un poco dalla parte opposta, e formano tre fasce di colori.

**[S14.09]** Nella figura, s indica il taglio di un coltello o di un cuneo qualsiasi AsB; e gowog, fnunf, emtme, dlsld sono raggi incurvati verso il coltello negli archi owo, nun, mtm, lsl, più o meno secondo la loro distanza dal coltello. Poiché un tale incurvamento dei raggi avviene nell’aria fuori del coltello, anche i raggi che incidono sul coltello dovranno incurvarsi nell’aria prima di toccarlo. E lo stesso vale per quelli che incidono sul vetro. La rifrazione dunque non avviene nel punto d’incidenza, ma gradualmente, per un incurvamento continuo dei raggi, fatto in parte nell’aria prima che tocchino il vetro, in parte (se non sbaglio) nel vetro, dopo che vi sono entrati: come è disegnato nei raggi ckzc, biyb, ahxa, che incidono in r, q, p e sono incurvati fra k e z, i e y, h e x. Dunque, per l’analogia che c’è fra la propagazione dei raggi della luce e l’avanzare dei corpi, mi è parso opportuno aggiungere le proposizioni seguenti per gli usi ottici, senza disputare affatto, frattanto, sulla natura dei raggi (se siano corpi o no), ma determinando soltanto traiettorie di corpi molto simili alle traiettorie dei raggi.

### Proposizione XCVII. Problema XLVII (la superficie che fa convergere in un punto)

**[S14.10]** **Posto che il seno d’incidenza su una superficie stia al seno di emergenza in un rapporto dato, e che l’incurvamento del cammino dei corpi vicino a quella superficie avvenga in uno spazio brevissimo, che si possa considerare come un punto, determinare la superficie che faccia convergere verso un altro luogo dato tutti i corpuscoli che escono successivamente da un luogo dato.**

**[S14.11]** Sia A il luogo da cui i corpuscoli divergono; B il luogo verso cui devono convergere; CDE la linea curva che, fatta ruotare intorno all’asse AB, descriva la superficie cercata; D, E due punti qualsiasi di quella curva; ed EF, EG le perpendicolari abbassate sui cammini del corpo AD, DB. Il punto D si avvicini al punto E: il rapporto ultimo della linea DF, di cui AD cresce, alla linea DG, di cui DB diminuisce, sarà lo stesso del seno d’incidenza al seno di emergenza. È dato dunque il rapporto dell’incremento della linea AD al decremento della linea DB; e perciò, se sull’asse AB si prende in un luogo qualsiasi il punto C per cui la curva CDE deve passare, e si prendono l’incremento CM di AC e il decremento CN di BC in quel rapporto dato, e con centri A, B e raggi AM, BN si descrivono due cerchi che si tagliano in D, quel punto D toccherà la curva cercata CDE e, toccandola in qualsiasi luogo, la determinerà. C.V.T.

**[S14.12]** *Cor. 1.* Facendo poi in modo che il punto A o B ora si allontani all’infinito, ora passi dall’altra parte del punto C, si avranno tutte quelle figure che Descartes ha esposto nell’Ottica e nella Geometria a proposito delle rifrazioni. E poiché Descartes ne ha tenuto nascosta l’invenzione, mi è parso bene esporla con questa proposizione.

**[S14.13]** *Cor. 2.* Se un corpo, incidendo su una superficie qualsiasi CD secondo la linea retta AD, condotta secondo una legge qualsiasi, emerge secondo un’altra retta qualsiasi DK, e dal punto C si immaginano condotte le linee curve CP, CQ sempre perpendicolari ad AD, DK, gli incrementi delle linee PD, QD, e quindi le linee stesse PD, QD generate da quegli incrementi, staranno fra loro come i seni d’incidenza e di emergenza; e viceversa.

### Proposizione XCVIII. Problema XLVIII (la seconda superficie)

**[S14.14]** **Poste le stesse cose, e descritta intorno all’asse AB una superficie attrattiva qualsiasi CD, regolare o irregolare, attraverso la quale devono passare i corpi che escono dal luogo dato A, trovare una seconda superficie attrattiva EF che faccia convergere quei corpi verso il luogo dato B.**

**[S14.15]** La congiungente AB tagli la prima superficie in C e la seconda in E, preso il punto D in modo qualsiasi. E, posto che il seno d’incidenza sulla prima superficie stia al seno di emergenza dalla stessa, e il seno di emergenza dalla seconda superficie al seno d’incidenza su di essa, come una quantità data M sta a un’altra quantità data N, prolunga AB fino a G, in modo che BG stia a CE come M − N sta a N; poi AD fino a H, in modo che AH sia uguale ad AG; e poi anche DF fino a K, in modo che DK stia a DH come N sta a M. Congiungi KB, e con centro D e raggio DH descrivi un cerchio che incontri in L la KB prolungata, e conduci BF parallela a DL: il punto F toccherà la linea EF, che, fatta ruotare intorno all’asse AB, descriverà la superficie cercata. C.V.F.

**[S14.16]** Immagina infatti che le linee CP, CQ siano dovunque perpendicolari rispettivamente ad AD, DF, e le linee ER, ES a FB, FD, e che quindi QS sia sempre uguale a CE: PD starà (per il Cor. 2 della Prop. XCVII) a QD come M a N, e quindi come DL a DK, o FB a FK; e, per divisione, come DL − FB, ossia PH − PD − FB, sta a FD, ossia FQ − QD; e, per composizione, come PH − FB sta a FQ, cioè (poiché PH e CG, QS e CE sono uguali) come CE + BG − FR sta a CE − FS. Ma (poiché BG sta a CE come M − N sta a N) anche CE + BG sta a CE come M sta a N; e quindi, per divisione, FR sta a FS come M sta a N; e perciò (per il Cor. 2 della Prop. XCVII) la superficie EF costringe il corpo che incide su di essa secondo la linea DF a proseguire lungo la linea FR verso il luogo B. C.V.D.

### Scolio (le figure sferiche e la diversa rifrangibilità)

**[S14.17]** Con lo stesso metodo si potrebbe procedere a tre o più superfici. Per gli usi ottici, però, le figure più adatte sono quelle sferiche. Se gli obiettivi dei cannocchiali si formano con due vetri di figura sferica che racchiudono fra loro dell’acqua, è possibile che gli errori delle rifrazioni che avvengono nelle superfici estreme dei vetri siano corretti con sufficiente precisione dalle rifrazioni dell’acqua. Tali obiettivi sono da preferire ai vetri ellittici e iperbolici, non solo perché si possono formare più facilmente e con maggiore precisione, ma anche perché rifrangono con maggiore precisione i pennelli di raggi situati fuori dell’asse del vetro. Tuttavia la diversa rifrangibilità dei diversi raggi è l’impedimento per cui l’ottica non può essere resa perfetta per mezzo di figure né sferiche né di qualsiasi altro genere. Se non si possono correggere gli errori che nascono di lì, tutta la fatica impiegata nel correggere gli altri sarà spesa senza criterio.

**Fine della Sezione XIV e del Libro I. Nel testo originale segue il Libro II, *De motu corporum*.**

---

## Apparato

### A.0 Estensioni del glossario

I termini seguenti non compaiono nel glossario comune. Ognuno è reso in modo costante in tutto il fascicolo.

| Latino | Italiano | Motivazione |
|---|---|---|
| *corpusculum* | «corpuscolo» | Diminutivo di *corpus*, distinto da *particula* («particella»), che indica una parte del corpo attraente. Newton usa *corpusculum* per il corpo attratto (S13.05, S13.16) e, nella Sez. XIV, per i corpuscoli di cui si cerca il moto (S14.10). |
| *corpus attrahens / attractivum / attractum* | «corpo attraente / attrattivo / attratto» | Si conserva la triplice distinzione del latino: *attrahens* è il corpo che attrae in quel caso, *attractivum* il corpo dotato di forza attrattiva in generale. |
| *in recessu (corporis attracti)* | «man mano che (il corpo attratto) si allontana» | *Recessus* è l’allontanamento; la resa verbale evita «nel recesso», che in italiano non ha questo senso. Motte conserva «in the recess». |
| *orbis* (nel senso di *orbis sphæricus concavus*, S13.02, S13.04) | «guscio», «guscio sferico» | Qui *orbis* non è un’orbita ma un guscio sferico, cioè lo spazio fra due superfici sferiche concentriche (Sez. XII). La resa del glossario («orbita») sarebbe un controsenso. Resa uniformata con il Fascicolo 11 (coordinamento del Libro I). Il significato è spiegato nella nota N2. |
| *dignitas*, *potestas* | «potenza» | Sinonimi nel latino di Newton (*dignitas* in S13.07, S13.20; *potestas* in S13.29–S13.34). |
| *latus* (di una potenza), *index* | «lato», «indice» | *Potestas cujus latus est distantia & index…*: il «lato» è la base della potenza, l’«indice» l’esponente. Si conservano i termini storici; il senso è nella nota N9. Così anche *latera cubica* «lati cubici» (radici cubiche dei volumi, S13.07). |
| *ratio quadruplicata* | «rapporto quadruplicato» | Estensione regolare della serie del glossario (quarta potenza del rapporto). Analogamente *plusquam duplicata / triplicata / quadruplicata* «più che duplicato / triplicato / quadruplicato». |
| *plusquam quadratica* | «più che quadratica» | Calco del latino; significa: con esponente maggiore di 2. |
| *contentum* | «prodotto» | Nella geometria dell’epoca il *contentum* è il prodotto di due o più grandezze (il «contenuto» del rettangolo). Motte: «content». |
| *intervallum* (in *centro A intervallo AD*) | «raggio» | Come nel Fascicolo 3 (*centro O & intervallo OL*: «con centro O e con raggio OL»). |
| *annulus* | «anello» | L’anello circolare fra i raggi AE e Ae (S13.18). |
| *solidum rotundum* | «solido rotondo» | Solido generato dalla rotazione di una figura intorno a un asse; si conserva l’aggettivo del latino. |
| *sphærois* | «sferoide» | Termine tecnico invariato. |
| *ducere in longitudinem* | «moltiplicare per la lunghezza» | Applicazione del glossario (*ducere in*). Quando l’ordinata varia lungo la lunghezza (S13.24), l’operazione è in realtà una somma continua, cioè una quadratura; lo si dichiara nella nota N6, senza cambiare la resa. |
| *medium* | «mezzo» | Il mezzo fisico attraversato dal corpo. |
| *media similaria* | «mezzi omogenei» | *Similaris* è «di parti simili», cioè omogeneo. Motte calca «similar mediums», che in inglese e in italiano suggerisce «simili fra loro». |
| *sinus incidentiæ / emergentiæ* | «seno d’incidenza / di emergenza» | Applicazione del glossario (*sinus*). *Planum incidentiæ / emergentiæ*: «piano d’incidenza / di emergenza»; *linea incidentiæ*: «linea d’incidenza». |
| *agitare*, *agitari* | «muovere», «essere mosso»; nel titolo della Sez. XIV «agitati» | Nel titolo si conserva il termine; nei testi delle proposizioni (*neque ulla alia vi agitetur*, *agitetur vi*) si rende con «mosso», più naturale. |
| *impellere*, *impulsus* | «spingere», «spinta» | Glossario comune: qui *impulsus* è un’azione continua lungo lo strato, non istantanea, quindi «spinta», non «impulso». |
| *ex æquo* | «per uguaglianza» | Termine euclideo (*ex aequali*): composizione di una catena di rapporti (S14.03). Motte: «by equality». |
| *convertendo*, *divisim*, *componendo / composite* | «per conversione», «per divisione», «per composizione» | Termini della teoria euclidea delle proporzioni, resi con i nomi italiani tradizionali. |
| *ratio dimidiata* | «rapporto subduplicato» | *Dimidiata* è sinonimo di *subduplicata* (radice quadrata del rapporto); si usa il termine del glossario. |
| *incurvatio*, *incurvari* | «incurvamento», «incurvarsi» | Resa letterale; Motte alterna «inflection», «inflected» e «bent». |
| *refrangibilitas* | «rifrangibilità» | Termine tecnico newtoniano. |
| *perspicillum*, *vitrum objectivum* | «cannocchiale», «obiettivo» | *Perspicillorum vitra objectiva*: «gli obiettivi dei cannocchiali». |
| *penicillus radiorum* | «pennello di raggi» | Termine tecnico dell’ottica. |
| *acies* | «taglio» | Il filo di un coltello o di un cuneo. |
| *concipe* | «immagina» | Imperativo di seconda persona, conservato come nel Fascicolo 3. |
| *quam proxime* | «con ottima approssimazione» | Come nel Fascicolo 3. |

### A.1 Proposizione LXXXV

**Latino:** *Si corporis attracti, ubi attrahenti contiguum est, attractio longe fortior sit, quam cum vel minimo intervallo separantur ab invicem: vires particularum trahentis, in recessu corporis attracti, decrescunt in ratione plusquam duplicata distantiarum a particulis.*

**Inglese:** “If a body be attracted by another, and its attraction be vastly stronger when it is contiguous to the attracting body than when they are separated from one another by a very small interval; the forces of the particles of the attracting body decrease, in the recess of the body attracted, in more than a duplicate ratio of the distance of the particles.”

**Scelte.**

- *separantur* è plurale con soggetto implicito «i due corpi»: reso «quando essi sono separati».
- *vel minimo intervallo*: «anche da un intervallo minimo». Motte attenua in «a very small interval».
- *passim* (S13.02, *attractiones passim per orbium cavitates*) è reso «diffuse ovunque»; Motte ha «diffused through», che coincide.
- *excessum attractionis, qui ex contactu oritur*: Motte aggiunge «of the two bodies».

### A.2 Proposizione LXXXVI

**Latino:** *Si particularum, ex quibus corpus attractivum componitur, vires in recessu corporis attracti decrescunt in triplicata vel plusquam triplicata ratione distantiarum a particulis: attractio longe fortior erit in contactu, quam cum attrahens & attractum intervallo vel minimo separantur ab invicem.*

**Inglese:** “If the forces of the particles of which an attractive body is composed decrease, in the recess of the attractive body, in a triplicate or more than a triplicate ratio of the distance from the particles, the attraction will be vastly stronger in the point of contact than when the attracting and attracted bodies are separated from each other, though by never so small an interval.”

**Scelte e divergenze.**

- **Errore di Motte:** «in the recess of the **attractive** body». Il latino ha *in recessu corporis* ***attracti***: è il corpo attratto che si allontana, come nella Prop. LXXXV.
- I rimandi *problematis xli.* e *theorema xli.* sono identificati nei file di lavoro: Problema XLI = Prop. LXXXI (con gli esempi 2 e 3: forze inversamente come il cubo e come la quarta potenza); Teorema XLI = Prop. LXXXII. Le identificazioni sono date tra parentesi quadre.

### A.3 Proposizione LXXXVII e corollari

**Latino:** *Si corpora duo sibi invicem similia, & ex materia æqualiter attractiva constantia, seorsim attrahant corpuscula sibi ipsis proportionalia & ad se similiter posita: attractiones acceleratrices corpusculorum in corpora tota erunt ut attractiones acceleratrices corpusculorum in eorum particulas totis proportionales, & in totis similiter positas.*

**Inglese:** “If two bodies similar to each other, and consisting of matter equally attractive, attract separately two corpuscles proportional to those bodies, and in a like situation to them, the accelerative attractions of the corpuscles towards the entire bodies will be as the accelerative attractions of the corpuscles towards particles of the bodies proportional to the wholes, and alike situated in them.”

**Scelte e divergenze.**

- **Aggiunta di Motte:** «**two** corpuscles». Il latino ha soltanto *corpuscula*.
- *attractiones acceleratrices*: «attrazioni acceleratrici», secondo il glossario (*vis acceleratrix*).
- *componendo* (S13.06): «per composizione».
- **Cor. 1, formule.** La trascrizione ha le frazioni appiattite e duplicate: «A cub.A quad.&B cub.B quad.» si legge A³/A² e B³/B²; «A cub.A cub.&B cub.B cub.» si legge A³/A³ e B³/B³; «A cub.Aqq.&B cub.Bqq.» si legge A³/A⁴ e B³/B⁴. La lettura è confermata dalle conclusioni del testo stesso («cioè come A e B», «cioè uguali», «inversamente come A e B») e da Motte negli SVG 309, 310, 312, 313.
- **Errore di Motte 1846 (EPUB):** nel caso triplicato gli SVG 191 e 311 danno **A²/A³** e **B²/B³**, mentre il testo prosegue «that is, equal». Le due frazioni non sono uguali (stanno come 1/A e 1/B): la lezione corretta è A³/A³ e B³/B³, come nel latino. L’SVG 191 compare anche in un’altra Sezione dell’EPUB: probabile riuso errato di un’immagine nella conversione digitale. Non ho potuto controllare la stampa del 1846.
- *aquales* (Cor. 1): refuso probabile della trascrizione per *æquales*, da verificare sulla stampa.

### A.4 Proposizione LXXXVIII

**Latino:** *Si particularum æqualium corporis cujuscunque vires attractivæ sint ut distantiæ locorum a particulis: vis corporis totius tendet ad ipsius centrum gravitatis; & eadem erit cum vi globi ex materia consimili & æquali constantis, & centrum habentis in ejus centro gravitatis.*

**Inglese:** “If the attractive forces of the equal particles of any body be as the distance of the places from the particles, the force of the whole body will tend to its centre of gravity; and will be the same with the force of a globe, consisting of similar and equal matter, and having its centre in the centre of gravity.”

**Scelte e divergenze.**

- *in distantias suas … ductæ*: «moltiplicate per le loro distanze» (glossario: *ducere in*).
- *per contenta illa A×AZ & B×BZ*: «con quei prodotti A × AZ e B × BZ». La trascrizione scrive «A×AZ&B×BZ», con la congiunzione attaccata: la lettura è certa.
- *A+B¯×GZ* è (A + B) × GZ: il trattino finale è il vinculum di Newton sopra A + B (Motte, SVG 314–315).
- *ob proportionales A ad B & BG ad AG*: «poiché A sta a B come BG sta ad AG». **Motte** rende «because A is proportional to B, and BG to AG», che non esprime la proporzione A : B = BG : AG.
- *in eorum communi gravitatis, centro G*: la virgola fra *gravitatis* e *centro* è innaturale; si legge *in eorum communi gravitatis centro G*. Probabile artefatto della trascrizione.
- **Aggiunta di Motte:** «composing there a **little** globe»; il latino ha *globum*.
- *per legum corol. 2.*: «per il Cor. 2 delle leggi», cioè il Corollario II degli Assiomi (Fascicolo 3, L10).

### A.5 Proposizione LXXXIX

**Latino:** *Si corpora sint plura ex particulis æqualibus constantia, quarum vires sunt ut distantiæ locorum a singulis: vis ex omnium viribus composita, qua corpusculum quodcunque trahitur, tendet ad trahentium commune centrum gravitatis, & eadem erit, ac si trahentia illa, servato gravitatis centro communi, coirent & in globum formarentur.*

**Inglese:** “If there be several bodies consisting of equal particles whose forces are as the distances of the places from each, the force compounded of all the forces by which any corpuscle is attracted will tend to the common centre of gravity of the attracting bodies; and will be the same as if those attracting bodies, preserving their common centre of gravity, should unite there, and be formed into a globe.”

**Scelte.** La trascrizione spezza *ea dem* per il cambio di pagina (〈214〉). Motte aggiunge «there» in «should unite there» (anche nel corollario); il latino ha soltanto *coirent*.

### A.6 Proposizione XC e corollari

**Latino:** *Si ad singula circuli cujuscunque puncta tendant vires æquales centripetæ, crescentes vel decrescentes in quacunque distantiarum ratione: invenire vim, qua corpusculum attrahitur ubivis positum in recta, quæ plano circuli ad centrum ejus perpendiculariter insistit.*

**Inglese:** “If to the several points of any circle there tend equal centripetal forces, increasing or decreasing in any ratio of the distances; it is required to find the force with which a corpuscle is attracted, that is, situate any where in a right line which stands at right angles to the plane of the circle at its centre.”

**Scelte e divergenze.**

- *quam punctum K perpetuo tangit*: «che il punto K tocca continuamente», cioè la curva descritta da K. Motte interpreta: «the locus of the point K». La stessa espressione ricorre in S13.23 e in S14.11 (*tanget curvam*).
- *ad centrum ejus perpendiculariter insistit*: «si innalza perpendicolarmente … nel suo centro». Il «that is» di Motte nell’enunciato non ha corrispondente latino.
- **Refuso della trascrizione:** *in PPE, PA capiantur PC, Pf*: la lettera P è duplicata; si legge *in PE, PA*, come in Motte.
- *ob proportionales PE & AE, Ee & CE*: «poiché PE sta ad AE come Ee sta a CE».
- *AP×FKPE* è la frazione appiattita AP × FK / PE (Motte, SVG 316).
- **Motte** scrive «the content under Ff × FK AP», senza il secondo segno di moltiplicazione: probabile refuso dell’edizione 1846.
- La curva è chiamata IKL e l’area AHIL nella soluzione, AHIKL nella dimostrazione e nei corollari: è la stessa area, letta con o senza il punto intermedio K. Nessuna correzione.
- **Cor. 1:** *descrescunt* è refuso probabile della trascrizione per *decrescunt*, da verificare sulla stampa. Le formule appiattite «1PF quad.», «1PA−1PH», «1−PAPH», «AHPH» si leggono 1/PF², 1/PA − 1/PH, 1 − PA/PH, AH/PH (confermate dagli SVG 317–320).
- **Cor. 2:** «1PAn−1−1PHn−1» si legge 1/PAⁿ⁻¹ − 1/PHⁿ⁻¹, e «1PAn−2−PAPHn−1» si legge 1/PAⁿ⁻² − PA/PHⁿ⁻¹ (SVG 322–323).

### A.7 Proposizione XCI e corollari

**Latino:** *Invenire attractionem corpusculi siti in axe solidi rotundi, ad cujus puncta singula tendunt vires æquales centripetæ in quacunque distantiarum ratione decrescentes.*

**Inglese:** “To find the attraction of a corpuscle situate in the axis of a round solid, to whose several points there tend equal centripetal forces decreasing in any ratio of the distances whatsoever.”

**Scelte e divergenze.**

- *extimorum circulorum*: «dei cerchi estremi»; Motte «outermost circles».
- **Cor. 1:** *1 in PE−AD¯* è 1 × (PE − AD), con il vinculum; così le altre espressioni. *1−PFPR* è 1 − PF/PR (SVG 327). La trascrizione spezza *con tentum* per il cambio di pagina.
- **Cor. 2:** *erit at vim* è refuso probabile della trascrizione per *erit ad vim*, da verificare sulla stampa. La formula «AS×CSq−PS×KMRKPSq+CSq−ASq ad AS cub.3PS quad.» si legge (AS × CS² − PS × KMRK)/(PS² + CS² − AS²) ad AS³/(3PS²), dove KMRK indica l’**area** del segmento conico. Motte (SVG 333–334) concorda. La formula è verificata numericamente (N7). Motte ha un refuso di punteggiatura: «in which that ordinate cuts the spheroid, From the vertices».
- **Cor. 3, lettere.** Lo sferoide esterno è chiamato *AGOF* all’inizio e *AGOD* alla fine; lo sferoide interno *PCM* e poi *PCBM*. Le due incoerenze sono tanto nella trascrizione quanto in Motte, e quindi probabilmente nella stampa. Si conservano. Non è possibile decidere senza la figura NATP00087-156: nel testo F e G sono già estremi della retta FG, perciò *AGOF* potrebbe essere l’etichetta della figura e *AGOD* una svista, o viceversa.
- **Cor. 3:** *facilius*: «più facilmente». Motte rende «easily», perdendo il comparativo (più facilmente che con il calcolo del Cor. 2).
- *occur rentes*: parola spezzata dal cambio di pagina (〈218〉).

### A.8 Proposizione XCII

**Latino:** *Dato corpore attractivo, invenire rationem decrementi virium centripetarum in ejus puncta singula tendentium.*

**Inglese:** “An attracting body being given, it is required to find the ratio of the decrease of the centripetal forces tending to its several points.”

**Scelte.** *patefacta*: «rivelata». Nessuna divergenza rilevante di Motte. È l’unica proposizione della Sezione che prescrive esplicitamente esperimenti (nota N8).

### A.9 Proposizione XCIII e corollari

**Latino:** *Si solidum ex una parte planum, ex reliquis autem partibus infinitum, constet ex particulis æqualibus æqualiter attractivis, quarum vires in recessu a solido decrescunt in ratione potestatis cujusvis distantiarum plusquam quadraticæ, & vi solidi totius corpusculum ad utramvis plani partem constitutum trahatur: dico quod solidi vis illa attractiva, in recessu ab ejus superficie plana, decrescet in ratione potestatis, cujus latus est distantia corpusculi a plano, & index ternario minor quam index potestatis distantiarum.*

**Inglese:** “If a solid be plane on one side, and infinitely extended on all other sides, and consist of equal particles equally attractive, whose forces decrease, in the recess from the solid, in the ratio of any power greater than the square of the distances; and a corpuscle placed towards either part of the plane is attracted by the force of the whole solid; I say that the attractive force of the whole solid, in the recess from its plane superficies, will decrease in the ratio of a power whose side is the distance of the corpuscle from the plane, and its index less by 3 than the index of the power of the distances.”

**Scelte e divergenze.**

- *index ternario minor*: «minore di tre unità»; Motte «less by 3».
- Le potenze appiattite «CHn−2», «CGn−3» ecc. si leggono CHⁿ⁻², CGⁿ⁻³ (SVG 335–341).
- **Errore di Motte 1846 (EPUB):** nel Caso 1 la terza lunghezza è presa inversamente proporzionale a **CL**ⁿ⁻² (SVG 338), mentre il latino ha ***CI***ⁿ⁻². La distanza del piano nIN dal punto C è CI, misurata sulla perpendicolare CGHI: la lezione latina è quella coerente.
- **Cor. 1, lettere.** La trascrizione ha *partis ulterioris* ***NICO***, Motte ha **NIKO**. Le altre sigle del corollario (*LGIN*, *LGKO*) e del Caso 1 (piani nIN e oKO) fanno pensare che la parte più lontana sia quella fra il piano IN e il piano all’infinito verso KO, cioè NIKO; ma C è anche la lettera del corpuscolo, e *NICO* potrebbe essere la lezione della stampa. **Lettura incerta**: si conserva *NICO* nella traduzione, da verificare sulla stampa e sulla figura.
- **Motte** ha «two infinite parallel **places**» per *planis*: refuso dell’edizione 1846.
- *nullius pene est momenti* (Cor. 2): «non ha quasi alcun peso». *Momentum* qui è «importanza», non il momento meccanico.
- *plusquam quadruplicatæ* (Cor. 3): «più che quadruplicata». Sulla relazione fra la condizione dell’enunciato (*plusquam quadraticæ*), quella del Caso 1 (*ternario non minor*) e quella del Cor. 3, vedi la nota N9.

### A.10 Scolio della Sezione XIII

- *per prop. xxxix.*: il moto rettilineo sotto una forza centripeta qualsiasi (Sez. VII). *Ad exemplum problematis tertii*: il Problema III è la Prop. VIII (Sez. II), in cui la forza tende a un punto così lontano che le linee condotte verso di esso si possono considerare parallele; il rimando è coerente con il caso di forze perpendicolari a un piano.
- *vel in basem attractum vel a basi fugatum*: «attratto verso la base o respinto dalla base».
- **Formule.** La trascrizione appiattisce le frazioni e gli esponenti. Lettura adottata: «Amn» = A^(m/n); «A+O¯mn» = (A + O)^(m/n); la serie «Amn+mnOAm−nn+mm−mn2nnOOAm−2nn & c.» = A^(m/n) + (m/n) O A^((m−n)/n) + ((mm − mn)/2nn) OO A^((m−2n)/n) ecc.; «mm−mnnnAm−2nn» = ((mm − mn)/nn) A^((m−2n)/n); «mm−mnnnBm−2nm» = ((mm − mn)/nn) B^((m−2n)/m); «2B°» = 2B⁰; «2A−3 seu 2B3» = 2A⁻³, ossia 2B³.
- **Coefficiente della forza.** Il termine della serie ha 2nn al denominatore; la forza è data con nn. Newton passa da un termine proporzionale alla forza alla forza stessa a meno di un fattore costante: la differenza è irrilevante per la proporzionalità, e gli esempi del testo (2B⁰ per m = 2, n = 1; 2A⁻³ per m = −1, n = 1) si ottengono proprio con nn. La lettura «nn» è quindi coerente e non va corretta.
- *m = 0 − 1*: così nella trascrizione e in Motte («m being = 0 - 1»); vale m = −1. Si conserva la forma.
- **Tre errori di Motte 1846 (EPUB) nelle formule:**
  1. SVG 344: il secondo termine della serie ha esponente **(m − n)/m** invece di (m − n)/n;
  2. SVG 347–348: la forza cercata ha **2nn** al denominatore invece di nn; con questo coefficiente l’esempio parabolico darebbe 1·B⁰, non il «2B⁰» che Motte stesso stampa (SVG 349);
  3. SVG 348: l’esponente di B è **(m − 2n)/n** invece di (m − 2n)/m; con m = −1, n = 1 darebbe B⁻³ invece di B³, in contraddizione con il «2B³» che segue (SVG 351).

  Il latino è coerente in tutti e tre i punti (verifica numerica in N10).

### A.11 Proposizione XCIV

**Latino:** *Si media duo similaria, spatio planis parallelis utrinque terminato, distinguantur ab invicem, & corpus in transitu per hoc spatium attrahatur vel impellatur perpendiculariter versus medium alterutrum, neque ulla alia vi agitetur vel impediatur; sit autem attractio, in æqualibus ab utroque plano distantiis ad eandem ipsius partem captis, ubique eadem: dico quod sinus incidentiæ in planum alterutrum erit ad sinum emergentiæ ex plano altero in ratione data.*

**Inglese:** “If two similar mediums be separated from each other by a space terminated on both sides by parallel planes, and a body in its passage through that space be attracted or impelled perpendicularly towards either of those mediums, and not agitated or hindered by any other force; and the attraction be every where the same at equal distances from either plane, taken towards the same hand of the plane; I say, that the sine of incidence upon either plane will be to the sine of emergence from the other plane in a given ratio.”

**Scelte e divergenze.**

- *media similaria*: «mezzi omogenei» (§ A.0).
- **Refuso della trascrizione:** *secundam lineam GH* per *secundum lineam GH*. Da verificare sulla stampa.
- *ex demonstratis Galilæi*: «per ciò che ha dimostrato Galileo»; *Galilæus* nell’apparato, Galileo nel testo.
- *dato latere recto*: «il lato retto dato». È dato perché la velocità d’incidenza e la forza sono date (nota N11).
- *HMq*, *MLq*, *LIq* = HM², ML², LI². *MLq−LIq* = ML² − LI².
- *in omni triangulo LMI*: alla lettera «in ogni triangolo LMI»; reso «in ogni triangolo, e dunque in LMI», perché la proprietà è generale. Motte: «in every triangle, as LMI».
- *ratio dimidiata*: «rapporto subduplicato» (§ A.0).
- **Motte**, Caso 1: «the curve HI (by what Galileo has demonstrated) **be** a parabola», errore grammaticale per «will be»; «whose property is **that of** a rectangle…», costruzione imprecisa. Il senso non cambia.
- *agitetur vi quæ sit in singulis separatim uniformis*: nel Caso 2 il latino non ha il soggetto espresso né la congiunzione prima di *agitetur*; Motte integra «and let it be acted on». La traduzione fa lo stesso.

### A.12 Proposizione XCV

**Latino:** *Iisdem positis; dico quod velocitas corporis ante incidentiam est ad ejus velocitatem post emergentiam, ut sinus emergentiæ ad sinum incidentiæ.*

**Inglese:** “The same things being supposed, I say, that the velocity of the body before its incidence is to its velocity after emergence as the sine of emergence to the sine of incidence.”

**Scelte.**

- *demittatur normaliter Tv*: «si abbassi la normale Tv». La lettera v è minuscola, distinta da V.
- *respectu radii TH vel IK*: «rispetto al raggio TH, o IK». I seni sono le lunghezze dei seni nel cerchio di quel raggio, secondo l’uso dell’epoca (nota N11).
- Motte rende *conficiet … intervalla* con «go through those … intervals» e poi passa al plurale «**they** will describe the lines GH, IK»: il soggetto latino è il corpo, al singolare.

### A.13 Proposizione XCVI

**Latino:** *Iisdem positis, & quod motus ante incidentiam velocior sit quam postea: dico quod corpus, inclinando lineam incidentiæ, reflectetur tandem, & angulus reflexionis fiet æqualis angulo incidentiæ.*

**Inglese:** “The same things being supposed, and that the motion before incidence is swifter than afterwards; I say, that if the line of incidence be inclined continually, the body will be at last reflected, and the angle of reflexion will be equal to the angle of incidence.”

**Scelte e divergenze.**

- *inclinando lineam incidentiæ*: gerundio, «inclinando la linea d’incidenza». **Motte** aggiunge «continually».
- *pri mum*: parola spezzata dal cambio di pagina (〈225〉).
- *juxta demonstrata Galilæi*: «secondo ciò che ha dimostrato Galileo».
- **Aggiunta di Motte:** «with which it **first** impinged on that plane at H».

### A.14 Scolio dopo la Prop. XCVI (la luce)

- **Nomi:** *Snellius* è Willebrord Snell (Snel van Royen); *Cartesius* è René Descartes; *Grimaldus* è Francesco Maria Grimaldi.
- *secundum datam secantium rationem*: «secondo un rapporto dato delle secanti». Sull’equivalenza con il rapporto dei seni vedi la nota N13.
- *dudum*: «già da tempo». **Motte** traduce «**lately** was discovered by Grimaldus», che rovescia il senso temporale.
- *nummorum … termini rectanguli circulares*: «gli orli circolari, a spigolo retto, delle monete». Il latino descrive un solo tipo di orlo, circolare e tagliato ad angolo retto. **Motte** ne fa due tipi: «the circular **and** rectangular edges».
- *ex auro, argento & ære cusorum*: «coniate in oro, argento e rame». *Æs* è il bronzo o il rame; Motte ha «brass».
- *tres colorum fascias*: «tre fasce di colori»; Motte «three fringes of colours».
- **Lettere della figura:** il latino ha *nun* (arco del raggio fnunf), Motte ha **nvn**. U e v sono tipograficamente intercambiabili nella stampa antica; il raggio si chiama fn**u**nf in entrambe le fonti. Si adotta *nun*.
- *progressum corporum*: «l’avanzare dei corpi»; Motte «the motion of bodies».
- *ni fallor*: «se non sbaglio».

### A.15 Proposizione XCVII e corollari

**Latino:** *Posito quod sinus incidentiæ in superficiem aliquam sit ad sinum emergentiæ in data ratione; quodque incurvatio viæ corporum juxta superficiem illam fiat in spatio brevissimo, quod ut punctum considerari possit: determinare superficiem, quæ corpuscula omnia de loco dato successive manantia convergere faciat ad alium locum datum.*

**Inglese:** “Supposing the sine of incidence upon any superficies to be in a given ratio to the sine of emergence; and that the inflection of the paths of those bodies near that superficies is performed in a very short space, which may be considered as a point; it is required to determine such a superficies as may cause all the corpuscles issuing from any one given place to converge to another given place.”

**Scelte e divergenze.**

- *manantia*: «che escono» (alla lettera «che scaturiscono»).
- *Accedat punctum D ad punctum E*: «il punto D si avvicini al punto E». **Motte** aggiunge «and coalesce with».
- *ratio ultima*: «rapporto ultimo», secondo il glossario.
- **Cor. 1:** *in optica & geometria*: «nell’Ottica e nella Geometria», cioè, presumibilmente, la *Dioptrique* e la *Géométrie* di Descartes (1637). L’identificazione è del curatore e non è nel testo. *Celaverit*: «ha tenuto nascosta». *Visum fuit*: «mi è parso bene».
- **Cor. 2:** *lege quavis ductam*: «condotta secondo una legge qualsiasi». *& contra*: «e viceversa»; Motte «and è contra».

### A.16 Proposizione XCVIII

**Latino:** *Iisdem positis, & circa axem AB descripta superficie quacunque attractiva CD, regulari vel irregulari, per quam corpora de loco dato A exeuntia transire debent: invenire superficiem secundam attractivam EF, quæ corpora illa ad locum datum B convergere faciat.*

**Inglese:** “The same things supposed; if round the axis AB any attractive superficies be described as CD, regular or irregular, through which the bodies issuing from the given place A must pass; it is required to find a second attractive superficies EF, which may make those bodies converge to a given place B.”

**Scelte.**

- *produc tum AB ad G … tum AD ad H … tum etiam DF ad K*: non è una parola spezzata. È l’imperativo *produc* seguito dalla serie *tum … tum … tum etiam*: «prolunga AB fino a G…; poi AD fino a H…; e poi anche DF fino a K…». Motte rende allo stesso modo.
- La retta DF è il cammino del corpo dopo la prima superficie, noto per la legge dei seni; il punto F è determinato soltanto alla fine della costruzione. K cade sul prolungamento di DF oltre F (verificato in N14).
- *divisim*, *composite*: «per divisione», «per composizione».
- Il testo usa le lettere R e S per i piedi delle perpendicolari ER, ES: non vanno confuse con le lettere omonime delle figure precedenti.

### A.17 Scolio finale

- *fieri potest ut*: «è possibile che». **Motte** ha «it is not unlikely that», che aggiunge una valutazione di probabilità.
- *in vitrorum superficiebus extremis*: «nelle superfici estreme dei vetri», cioè le due superfici esterne del doppietto, a contatto con l’aria. **Motte** traduce «in the extreme **parts** of the superficies», cioè i bordi delle superfici: senso diverso.
- *impedimento est*: «è l’impedimento»; Motte aggiunge «the **real** obstacle».
- *labor omnis … imperite collocabitur*: alla lettera «ogni fatica sarà collocata in modo inesperto». Reso «sarà spesa senza criterio». Motte: «is quite thrown away».

### A.18 Refusi e anomalie della trascrizione

| Luogo | Trascrizione | Lettura | Natura |
|---|---|---|---|
| S13.07 | *aquales* | *æquales* | refuso probabile, da verificare sulla stampa |
| S13.07 | *A cub.A quad.&B cub.B quad.* ecc. | A³/A², B³/B² ecc. | frazioni appiattite |
| S13.10 | *communi gravitatis, centro G* | *communi gravitatis centro G* | virgola spuria probabile |
| S13.18 | *in PPE, PA* | *in PE, PA* | lettera duplicata |
| S13.19 | *descrescunt* | *decrescunt* | refuso probabile, da verificare sulla stampa |
| S13.25 | *erit at vim* | *erit ad vim* | refuso probabile, da verificare sulla stampa |
| S13.26 | *AGOF* / *AGOD*; *PCM* / *PCBM* | invariato | incoerenza presente anche in Motte (probabilmente nella stampa) |
| S13.32 | *NICO* | NICO o NIKO? | lettura incerta; Motte NIKO |
| S13.36 | *m=0−1* | m = −1 | forma dell’originale, presente anche in Motte |
| S14.02 | *secundam lineam* | *secundum lineam* | refuso probabile, da verificare sulla stampa |
| varie | *ea dem*, *con tentum*, *occur rentes*, *pri mum* | parole intere | spezzature dovute ai marcatori di pagina |

### A.19 Riepilogo: dove Motte aggiunge, omette o sbaglia

| Luogo | Latino 1726 | Motte 1846 | Tipo |
|---|---|---|---|
| S13.01 | *vel minimo intervallo* | «a very small interval» | attenuazione |
| S13.03 | *in recessu corporis attracti* | «in the recess of the **attractive** body» | errore di senso |
| S13.05 | *corpuscula* | «**two** corpuscles» | aggiunta |
| S13.07 | A³/A³, B³/B³ | A²/A³, B²/B³ (SVG 191, 311) | formula errata (EPUB) |
| S13.10 | *ob proportionales A ad B & BG ad AG* | «because A is proportional to B, and BG to AG» | proporzione resa male |
| S13.10 | *globum* | «a **little** globe» | aggiunta |
| S13.13, S13.15 | *coirent* | «should unite **there**» | aggiunta |
| S13.16 | — | «**that is**, situate any where» | inciso spurio |
| S13.18 | Ff × FK × AP | «Ff × FK AP» | segno omesso |
| S13.25 | — | «spheroid, From» | punteggiatura |
| S13.26 | *facilius* | «easily» | comparativo perso |
| S13.30 | CIⁿ⁻² | CLⁿ⁻² (SVG 338) | lettera errata |
| S13.32 | *NICO*; *planis* | NIKO; «places» | lettera diversa (lettura incerta); refuso |
| S13.36 | A^((m−n)/n) | A^((m−n)/m) (SVG 344) | esponente errato |
| S13.36 | (mm − mn)/nn | (mm − mn)/2nn (SVG 347–348) | coefficiente diverso, incoerente con «2B⁰» |
| S13.36 | B^((m−2n)/m) | B^((m−2n)/n) (SVG 348) | esponente errato |
| S14.01 | *similaria* | «similar» | calco ambiguo |
| S14.02 | *erit … parabola* | «be a parabola» | grammatica |
| S14.05 | *corpus … describet* | «**they** will describe» | numero |
| S14.06 | *inclinando* | «inclined **continually**» | aggiunta |
| S14.07 | *qua incidit in H* | «with which it **first** impinged» | aggiunta |
| S14.08 | *dudum* | «**lately**» | senso temporale rovesciato |
| S14.08 | *termini rectanguli circulares* | «circular **and** rectangular edges» | interpretazione divergente |
| S14.09 | *nun* | «nvn» | variante grafica u/v |
| S14.11 | *accedat* | «approach to **and coalesce with**» | aggiunta |
| S14.17 | *fieri potest ut* | «it is not unlikely that» | modalità cambiata |
| S14.17 | *superficiebus extremis* | «extreme **parts** of the superficies» | errore di senso |
| S14.17 | *impedimento est* | «the **real** obstacle» | aggiunta |
| S14.17 | *imperite collocabitur* | «is quite thrown away» | parafrasi |

Gli errori nelle formule (SVG 191, 338, 344, 347–348) possono essere dell’edizione del 1846 o della sua conversione digitale: senza la stampa non si può decidere. Per il Fascicolo 3 un errore analogo (PE² per PE³) era risultato dell’edizione del 1846 e assente in Motte 1729.

---

## Note editoriali e fisiche

Queste note sono aggiunte del presente fascicolo, non affermazioni tradotte da Newton. Le verifiche numeriche sono state eseguite con due script del curatore: `verifiche/verifica_f12.py` (Sez. XIII) e `verifiche/verifica_f12_s14.py` (Sez. XIV), in Python con NumPy e SciPy. Nelle formule moderne G = 1 e densità 1, salvo indicazione.

### N1. Proposizioni LXXXV–LXXXVI: forze che agiscono al contatto

Le due proposizioni ragionano a rovescio: da un fatto osservabile (un’attrazione molto più forte al contatto che a distanza minima) si risale alla legge delle particelle. Con la legge dell’inverso del quadrato una sfera attrae un punto della sua superficie con una forza finita, *M*/*R*²: il contatto non porta alcun aumento brusco (Prop. LXXXV). Con la legge dell’inverso del cubo, invece, la forza di un corpo esteso su un punto a distanza *h* dalla superficie cresce come ln(1/*h*), e con esponenti maggiori come una potenza di 1/*h*: diverge al contatto (Prop. LXXXVI). La stima si ottiene dalla Prop. XCIII (nota N9): uno strato piano di spessore finito, con legge 1/*r*³, dà una forza proporzionale a ∫ d*z*/(*h* + *z*), che diverge logaritmicamente per *h* → 0. L’argomento «si aggiungono o tolgono parti lontane dal contatto» è un argomento di località: le parti lontane contribuiscono con forze limitate, quindi non cambiano il comportamento al contatto.

### N2. I «gusci» sferici (*orbes sphærici*)

Nelle Sezioni XII–XIII un *orbis sphæricus* è un guscio sferico, il solido compreso fra due superfici sferiche concentriche. La Prop. LXX, citata in S13.02, stabilisce che con la legge dell’inverso del quadrato un guscio non esercita alcuna forza sui punti della cavità: per questo Newton dice che l’attrazione vi è nulla «anche nel contatto stesso».

### N3. Proposizione LXXXVII, Cor. 1: corpi simili

In termini moderni: se la forza fra particelle va come 1/*r*ⁿ, l’accelerazione prodotta da un corpo di dimensione lineare *L*, su un punto posto in modo simile, scala come *L*³/*L*ⁿ = *L*³⁻ⁿ. Con n = 2 è proporzionale a *L* (i «lati cubici» A e B); con n = 3 è indipendente da *L*; con n = 4 è proporzionale a 1/*L*. Ho ricontrollato i tre casi con A = 2, B = 3: rapporti 2 : 3, 1 : 1, 1/2 : 1/3. Gli esponenti dell’errore di Motte (A²/A³ e B²/B³) darebbero 1/2 : 1/3, non l’uguaglianza che il testo stesso afferma. Il Cor. 2 è il principio di un metodo sperimentale: confrontando corpi simili di grandezza diversa si ricava l’esponente n.

### N4. Proposizione LXXXVIII: forze proporzionali alla distanza

Se ogni particella *m*ᵢ attrae il punto Z con forza *m*ᵢ · (**X**ᵢ − **Z**), la somma è Σ *m*ᵢ(**X**ᵢ − **Z**) = *M*(**G** − **Z**), dove **G** è il centro di massa e *M* la massa totale: la forza è quella di un’unica massa *M* posta in **G**, qualunque sia la forma del corpo. Lo script lo verifica su sette particelle di masse e posizioni casuali (le due somme coincidono in tutte le componenti). La dimostrazione di Newton fa la stessa somma una particella alla volta, scomponendo ogni forza con il Cor. II delle leggi. Il corollario segue dalla Prop. X: una forza proporzionale alla distanza da un centro fisso produce orbite ellittiche con il centro in quel punto (moto armonico in due dimensioni).

### N5. Proposizione XC: attrazione di un disco

Per un disco di raggio *a* e densità superficiale 1, con una legge 1/*r*ⁿ, la forza su un punto dell’asse a distanza *h* è

*F* = 2π*h* ∫ from *h* to √(*h*² + *a*²) of d*s*/*s*ⁿ.

È esattamente «l’area AHIKL moltiplicata per AP», con FK = 1/PFⁿ e PF variabile da PA a PH = PD; il fattore costante 2π è assorbito nella proporzionalità. Lo script confronta l’integrale diretto sul disco con la formula di Newton per n = 2, 3, 4,5 (*h* = 0,7; *a* = 1,3): coincidono fino all’ottava cifra. Coincidono anche i corollari: per n = 2 la forza vale 2π(1 − PA/PH); per n generico vale 2π/(n − 1) · (1/PAⁿ⁻² − PA/PHⁿ⁻¹), cioè la formula del Cor. 2 a meno del fattore costante 1/(n − 1), che Newton omette perché ragiona per proporzioni. Per il piano infinito (Cor. 3) il prodotto *F* · PAⁿ⁻² è costante (verificato per n = 4,5 con tre valori di PA).

Il passo chiave della dimostrazione è PE · CE = AE · Ee, cioè d(PE) = (AE/PE) d(AE), che deriva da PE² = AP² + AE²: per questo l’anello di area proporzionale ad AE · Ee si trasforma nella striscia Ff dell’asse.

### N6. Proposizione XCI, Cor. 1: cilindro

Il cilindro è una pila di dischi: l’ordinata FK è la forza del disco alla distanza PF (Cor. 1 della Prop. XC), e la forza del cilindro è l’area sotto quella curva. *Ducta in longitudinem* è qui una somma continua, cioè un integrale: «moltiplicare» va inteso come nella Prop. LXXXI, «per motum continuum». Con *a* = AD = 0,8, AB = 2, PA = 0,6, l’integrale diretto vale 1,757443990 e 2π(AB − PE + PD) vale 1,757443990. Il passaggio «PF/PR moltiplicata per PB dà PE − AD» è la quadratura ∫₀^PB *x* d*x*/√(*x*² + *a*²) = √(PB² + *a*²) − *a* = PE − AD.

### N7. Proposizione XCI, Cor. 2: sferoide esterno

Newton non dimostra il corollario; dà la costruzione e il risultato. Ho interpretato KMRK come l’area compresa fra l’arco KRM della conica (ordinata ER = PD in funzione dell’ascissa PE) e la corda KM. Poiché AK = AP e BM = BP, la corda è la retta «ordinata = ascissa», e l’area è ∫ (PD − PE) d(PE) fra PA e PB. La curva è effettivamente una conica: PD² = PE² + ED², ed ED² è un polinomio di secondo grado in PE.

Confronto numerico fra la forza dello sferoide (somma di dischi) e quella della sfera di diametro AB (4π AS³ / 3PS²):

| AS | CS | PS | forza sferoide / forza sfera | formula di Newton |
|---:|---:|---:|---:|---:|
| 1 | 0,6 | 1,7 | 0,41699452 | 0,41699452 |
| 1 | 1,4 | 2,5 | 1,79708029 | 1,79708029 |
| 1 | 1,0 | 1,6 | 1,00000000 | 1,00000000 |

La formula è esatta sia per lo sferoide allungato sia per quello schiacciato, e si riduce a 1 per la sfera. La lettura «KMRK = area del segmento» è quindi confermata.

### N8. Proposizione XCI, Cor. 3, e Proposizione XCII

L’argomento dei coni opposti mostra che uno strato compreso fra due sferoidi simili e concentrici (oggi «omeoide») non esercita forza su un punto della cavità: è la generalizzazione della Prop. LXX dalla sfera allo sferoide. Due controlli numerici:

- un guscio omeoide fra gli sferoidi di semiassi (1; 0,6; 0,6) e (0,7; 0,42; 0,42) esercita su un punto interno una forza dell’ordine di 10⁻⁶, cioè nulla entro l’errore di calcolo;
- con il metodo dei coni di Newton (forza = somma, su tutte le direzioni, della lunghezza del cono moltiplicata per il versore) la forza dello sferoide pieno nei punti (0,3; 0; 0) e (0,6; 0; 0) dell’asse vale −2,63847 volte la distanza dal centro in entrambi i casi.

Il secondo controllo mostra anche un fatto che il testo non afferma, ma che conviene segnalare agli studenti: fuori dall’asse la forza è proporzionale alla distanza lungo ogni diametro dato (raddoppiando la distanza raddoppia la forza), ma **non è diretta verso il centro**. Le componenti hanno coefficienti diversi (−2,64 lungo l’asse, −4,96 trasversalmente). L’enunciato di Newton, «come la distanza dal centro» per un diametro dato, è corretto così com’è.

La Prop. XCII è un programma sperimentale: dalla legge osservata per un corpo di forma regolare si risale, con le Prop. LXXX, LXXXI e XCI, alla legge delle particelle. È il rovescio del Cor. 2 della Prop. LXXXVII.

### N9. Proposizione XCIII: solido terminato da un piano

Sommando i piani (Cor. 3 della Prop. XC: forza di un piano 2π/(n − 1) · *h*²⁻ⁿ), la forza di un semispazio su un punto a distanza *h* dalla faccia è

*F*(*h*) = 2π / [(n − 1)(n − 3)] · *h*⁻⁽ⁿ⁻³⁾,

finita solo se n > 3. Lo script lo conferma per n = 4, 5 e 6,5: *F*(*h*) · *h*ⁿ⁻³ è costante per *h* = 0,1; 0,5; 2 e uguale al coefficiente teorico.

**Condizioni sull’esponente.** L’enunciato chiede una potenza «più che quadratica» (n > 2) e il Caso 1 un indice «non minore di tre» (n ≥ 3). Ma per n = 3 l’area GLOK «prolungata all’infinito» non è finita: l’integrale di 1/(*h* + *z*) diverge come un logaritmo, e una forza «inversamente come CG⁰» non ha senso. Il risultato richiede di fatto n > 3. Newton stesso lo riconosce nel Cor. 3, dove esclude il caso triplicato perché la parte lontana del corpo infinito ha un’attrazione infinitamente maggiore. Le condizioni dell’enunciato e del Caso 1 sono dunque più larghe del necessario.

**Cor. 3.** Per un corpo finito (disco di raggio 1 e spessore 1) il prodotto *F*(*h*) · *h*ⁿ⁻³ tende al valore del semispazio per *h* → 0. Con n = 5 la convergenza è rapida (0,7747; 0,7853; 0,7854 per *h* = 10⁻¹, 10⁻², 10⁻³; limite 0,7854). Con n = 3,5 è lentissima (3,23; 4,45; 4,84; limite 5,03). Il limite esiste per ogni n > 3; la condizione di Newton, «più che quadruplicata» (n > 4), è sufficiente e garantisce un’approssimazione buona già a distanze piccole ma non estreme. Non posso dire se Newton avesse in mente proprio questa ragione.

**Latus e index.** Nella terminologia dell’epoca, «la potenza il cui lato è CG e il cui indice è n − 3» è CGⁿ⁻³.

### N10. Scolio della Sezione XIII: forza e seconda differenza

Il moto parallelo alla base è uniforme (A cresce di quantità uguali O in tempi uguali), mentre la forza agisce lungo l’ordinata. La forza è allora proporzionale alla seconda differenza dell’ordinata, cioè, in termini moderni, a d²B/dA². Il termine in O² della serie, moltiplicato per 2, è proprio la derivata seconda:

d²B/dA² = (m/n) · ((m − n)/n) · A^((m−2n)/n) = ((mm − mn)/nn) · A^((m−2n)/n).

Controllo con differenze finite (A = 1,7; O = 10⁻³):

| m | n | seconda differenza | ((mm − mn)/nn) A^((m−2n)/n) | stessa in B, esponente (m − 2n)/m | in B, esponente di Motte (m − 2n)/n |
|---:|---:|---:|---:|---:|---:|
| 2 | 1 | 2,000000 | 2,000000 | 2,000000 | 2,000000 |
| −1 | 1 | 0,407083 | 0,407083 | 0,407083 | 9,826000 |
| 3 | 2 | 0,575224 | 0,575224 | 0,575224 | 0,503761 |

Parabola (m = 2, n = 1): forza costante, 2B⁰ = 2: è il moto dei proiettili di Galileo. Iperbole B = 1/A (m = −1, n = 1): forza 2A⁻³ = 2B³, cioè proporzionale al cubo dell’ordinata. L’ultima colonna mostra che l’esponente stampato da Motte (SVG 348) è sbagliato, tranne quando m = 2n (per esempio m = 2, n = 1). Lo sviluppo usato da Newton è la serie binomiale con esponente frazionario, troncata al termine di secondo grado.

### N11. Proposizioni XCIV–XCV: la legge dei seni

**In termini moderni.** La forza è perpendicolare ai piani, quindi la componente della velocità parallela ai piani si conserva: *v*₁ sin *i* = *v*₂ sin *e*, dove *i* ed *e* sono gli angoli con la perpendicolare. Ne segue sin *i* / sin *e* = *v*₂/*v*₁: è la Prop. XCV. La velocità d’uscita dipende solo dal lavoro della forza nello strato, che è lo stesso per ogni angolo d’incidenza (la forza dipende soltanto dalla distanza dai piani). Quindi il rapporto dei seni non dipende dall’angolo: è la Prop. XCIV.

**Verifica della costruzione del Caso 1.** Forza uniforme *g* = 0,6 verso il mezzo d’incidenza, spessore *d* = 0,5, velocità *v* = 1. Il lato retto della parabola, nel senso del testo (HM² = lato retto × IM), vale 2*v*²/*g*: dipende solo dalla velocità e dalla forza, che sono date, ed è per questo che Newton può dirlo «dato». Per *i* = 10°, 20°, 30°, 38° lo script costruisce H, M, I, R, L, O, N, P, Q con le definizioni del testo e verifica:

- HM² = lato retto × IM (per esempio 0,394086 = 0,394086 a 10°);
- L è il punto medio di HM; MO = OR; MN = IR;
- NM · MI = ML² − LI² (potenza del punto M rispetto al cerchio);
- LI/ML = sin *i* / sin *e* = 0,632456 per tutti e quattro gli angoli, uguale a √(1 − 2*gd*/*v*²) = √0,4 e a *v*₂/*v*₁.

L’angolo LIR è l’angolo di emergenza o il suo supplementare, che ha lo stesso seno. Con questi dati, oltre *i* = 39,23° (sin *i* = 0,632) il corpo non attraversa lo strato: è la situazione della Prop. XCVI.

**Verifica del Caso 2 e della Prop. XCV con una legge non uniforme.** Ho integrato numericamente il moto attraverso uno strato con una forza che varia in modo irregolare con la profondità (*g*(*y*) = 0,9 (1 + 0,8 sin 7*y*) exp[−((*y* + 0,25)/0,2)²]). Per *i* = 10°, 25°, 40°, 50° il rapporto sin *i* / sin *e* vale 0,859272666 (variazioni solo alla nona cifra), e il rapporto delle velocità *v*₁/*v*₂ = 1,163774945 coincide con sin *e* / sin *i*. La legge dei seni vale dunque per una legge di forza qualsiasi, come afferma il Caso 2, e la Prop. XCV è confermata.

**Il seno come lunghezza.** Nel linguaggio dell’epoca il seno è un segmento in un cerchio di raggio dato: «rispetto al raggio TH o IK» significa che AH = Id è il seno di emergenza e vH il seno d’incidenza, entrambi nel cerchio di raggio IK = TH. Infatti AH = GH sin *i* = IK sin *e* e vH = TH sin *i*.

### N12. Proposizione XCVI: riflessione

Se il moto è più lento dopo lo strato, esiste un angolo limite con sin *i* = *v*₂/*v*₁; oltre quell’angolo il corpo non attraversa lo strato e torna indietro. Per la simmetria della traiettoria rispetto al punto di inversione (il vertice R della parabola, nel modello a strati) esce con un angolo uguale a quello d’incidenza. Con la legge non uniforme della nota N11 l’angolo limite è 59,235°; per *i* = 62,235°, 70° e 80° il corpo torna al piano d’incidenza con angoli di uscita 62,235016°, 69,999999958° e 79,999999966°: uguali, entro l’errore d’integrazione. È l’analogo meccanico della riflessione totale.

### N13. Lo Scolio sulla luce

- **Secanti e seni.** Se gli angoli si misurano dalla superficie invece che dalla perpendicolare, la secante dell’angolo con la superficie è la cosecante dell’angolo con la perpendicolare. Un rapporto costante delle secanti, presi gli angoli con la superficie, equivale quindi a un rapporto costante (inverso) dei seni, presi gli angoli con la perpendicolare. Per questo Newton può dire «e di conseguenza» (*per consequens*). Come Snell abbia formulato effettivamente la sua legge non risulta dal testo e non è stato verificato qui.
- **Il tempo della luce.** «Sette od otto minuti» dal Sole alla Terra: il valore moderno è circa 8 minuti e 19 secondi (circa 499 s). Il dato di Newton è compatibile.
- **Diffrazione.** I fenomeni descritti (raggi che si piegano vicino agli spigoli e frange colorate) sono quelli che oggi si chiamano diffrazione; Grimaldi li aveva descritti e chiamati *diffractio*. Newton li interpreta come «incurvamento», per un’azione a breve distanza dei corpi sulla luce, e li usa per sostenere che anche la rifrazione avviene gradualmente.
- **Cautela di Newton.** Lo Scolio dichiara di non pronunciarsi sulla natura della luce («se i raggi siano corpi o no») e di studiare soltanto traiettorie di corpi simili ai raggi. Va notato per gli studenti che il modello corpuscolare di questa Sezione prevede, nella Prop. XCV, una velocità maggiore nel mezzo in cui il raggio si avvicina alla perpendicolare (per esempio nel vetro); la teoria ondulatoria prevede il contrario. *Nota del curatore, non verificata sulle fonti di questo fascicolo:* la questione fu decisa sperimentalmente nell’Ottocento, a favore della teoria ondulatoria.

### N14. Proposizioni XCVII–XCVIII: ovali di Descartes e seconda superficie

**Prop. XCVII.** Il rapporto fra l’incremento di AD e il decremento di DB è costante e uguale a *k* = sin *i* / sin *e*; quindi AD + *k* · DB è costante lungo la curva. È l’**ovale cartesiano**, e in termini moderni è la condizione di cammino ottico costante (*n*₁ · AD + *n*₂ · DB costante, con *k* = *n*₂/*n*₁). Verifica: A = (0, 0), B = (6, 0), C = (2, 0), *k* = 1,5. Ho costruito 601 punti D con i cerchi di centri A, B e raggi AC + CM, BC − CN, con CM = *k* · CN. In tre punti della curva, presa la normale dalla curva calcolata, sin *i* / sin *e* vale 1,500007, 1,500001 e 1,500000.

**Prop. XCVIII.** Dalla costruzione si ricava, per triangoli simili (BF ∥ DL), FB : FK = DL : DK = M : N, con K oltre F sul prolungamento di DF; quindi N · AD + M · DF + N · FB = N · AG: il cammino ottico, con indici N fuori e M dentro, è costante. Verifica: A = (0, 0), B = (12, 0); prima superficie circolare per C = (2, 0) con centro (5, 0); E = (5, 0); M/N = 1,5; G con BG = CE (M − N)/N. Per 200 posizioni di D:

- il cammino ottico vale 13,5 per tutte (minimo 13,499999999999996, massimo 13,500000000000004), uguale a N · AG = 13,5;
- sulla curva EF così costruita, sin(emergenza)/sin(incidenza) vale 1,500015, 1,500010 e 1,500005 in tre punti, cioè M/N;
- l’intersezione L utile è quella sul prolungamento di KB oltre B, come dice il testo (*KB productæ*).

La costruzione di Newton è quindi corretta e fa convergere in B tutti i corpi usciti da A.

### N15. Lo Scolio finale: obiettivi e rifrangibilità

Newton propone un obiettivo formato da due vetri sferici con acqua in mezzo, per compensare l’aberrazione di sfericità, e lo preferisce alle superfici ellittiche e iperboliche (che sarebbero perfette per un punto sull’asse, come gli ovali della Prop. XCVII) perché più facile da costruire e migliore fuori asse. Ma conclude che il vero limite è la **diversa rifrangibilità** dei raggi di colori diversi, cioè l’aberrazione cromatica. *Nota del curatore, non verificata sulle fonti di questo fascicolo:* l’opinione che l’aberrazione cromatica non si potesse correggere con lenti fu superata nel Settecento con gli obiettivi acromatici, formati da vetri di dispersione diversa.

---

## Controllo della copertura

Le pagine 1726 sono quelle segnate nella trascrizione con i numeri tra parentesi angolari; per Motte valgono i marcatori di pagina dell’EPUB (il marcatore segna l’inizio della pagina).

| Identificatori | Incipit latino | Contenuto | 1726 | Motte 1846 |
|---|---|---|---|---|
| S13.01–S13.02 | *Si corporis attracti, ubi attrahenti contiguum est* | Prop. LXXXV | pp. 210–211 | pp. 233–234 |
| S13.03–S13.04 | *Si particularum, ex quibus corpus attractivum* | Prop. LXXXVI | p. 211 | p. 234 |
| S13.05–S13.08 | *Si corpora duo sibi invicem similia* | Prop. LXXXVII, Cor. 1–2 | pp. 211–212 | pp. 234–235 |
| S13.09–S13.12 | *Si particularum æqualium corporis cujuscunque* | Prop. LXXXVIII e Cor. | pp. 212–213 | pp. 235–236 |
| S13.13–S13.15 | *Si corpora sint plura ex particulis æqualibus* | Prop. LXXXIX e Cor. | pp. 213–214 | pp. 236–237 |
| S13.16–S13.21 | *Si ad singula circuli cujuscunque puncta* | Prop. XC, Cor. 1–3 | pp. 214–215 | pp. 237–238 |
| S13.22–S13.26 | *Invenire attractionem corpusculi siti in axe* | Prop. XCI, Cor. 1–3 | pp. 216–218 | pp. 238–240 |
| S13.27–S13.28 | *Dato corpore attractivo* | Prop. XCII | pp. 218–219 | p. 240 |
| S13.29–S13.34 | *Si solidum ex una parte planum* | Prop. XCIII, Casi 1–2, Cor. 1–3 | pp. 219–220 | pp. 240–242 |
| S13.35–S13.36 | *Si corpus aliquod perpendiculariter versus planum* | Scolio della Sez. XIII | pp. 221–222 | pp. 242–243 |
| S14.01–S14.03 | *Si media duo similaria* | Prop. XCIV, Casi 1–2 | pp. 222–223 | pp. 243–244 |
| S14.04–S14.05 | *Iisdem positis; dico quod velocitas* | Prop. XCV | p. 224 | pp. 244–245 |
| S14.06–S14.07 | *Iisdem positis, & quod motus ante incidentiam* | Prop. XCVI | pp. 224–225 | pp. 245–246 |
| S14.08–S14.09 | *Harum attractionum haud multum dissimiles* | Scolio sulla luce | pp. 225–226 | pp. 246–247 |
| S14.10–S14.13 | *Posito quod sinus incidentiæ* | Prop. XCVII, Cor. 1–2 | pp. 227–228 | p. 247 |
| S14.14–S14.16 | *Iisdem positis, & circa axem AB* | Prop. XCVIII | pp. 228–229 | pp. 247–248 |
| S14.17 | *Eadem methodo pergere liceret* | Scolio finale del Libro I | p. 229 (o oltre) | p. 249 |

**Controlli eseguiti.**

1. **Copertura.** Ho riletto in sequenza ogni periodo della trascrizione, dal titolo della Sez. XIII (*De corporum non sphæricorum viribus attractivis*) all’ultima parola della Sez. XIV (*imperite collocabitur*), contro la traduzione. Nessuna frase manca. Dove il latino ha un periodo molto lungo (S13.18, S14.02, S14.07, S14.16), l’italiano lo segue senza omettere membri; in S13.18 la struttura *quoniam … ; erit* è conservata.
2. **Parte B.** `check.py` sui due file latini e sui due file di Motte: JSON valido, 11 unità, 78 passi, tutte le stringhe `la` (enunciati e passi) sottostringhe esatte della trascrizione, tutte le stringhe `en` sottostringhe esatte di Motte, nessun avviso.
3. **Matematica.** Verifiche numeriche con script propri per le Prop. LXXXVII (Cor. 1), LXXXVIII, XC (e Cor. 1–3), XCI (Cor. 1, 2, 3), XCIII (e Cor. 3), Scolio della Sez. XIII, Prop. XCIV (Casi 1 e 2), XCV, XCVI, XCVII, XCVIII. Tutti i risultati di Newton sono confermati; le sole riserve riguardano le condizioni sull’esponente nella Prop. XCIII (N9). Ho ricontrollato a mano l’aritmetica dei rimandi (BG/CE, AH = AG, DK/DH) e i passaggi per composizione e divisione della Prop. XCVIII.
4. **Motte.** Ho confrontato tutte le pp. 233–249 e reso come immagine ogni formula SVG della sezione (191, 309–351). Le divergenze sono nel § A.19.
5. **Rimandi interni.** Problema III = Prop. VIII; Prop. XXXIX; Prop. LXX; Prop. LXXII, Cor. 3; Prop. LXXIV; Prop. LXXX; Problema XLI = Prop. LXXXI; Teorema XLI = Prop. LXXXII: controllati sugli enunciati nei file di lavoro delle Sez. II, VII e XII.

**Non ho potuto verificare:**

- **la stampa del 1726**: i refusi segnalati (*aquales*, *descrescunt*, *at vim*, *secundam*, *PPE*) e la lettura *NICO* / NIKO restano da controllare sulla scansione;
- **le figure originali** NATP00087-151…167: le relazioni geometriche sono ricostruite dalle lettere del testo; in particolare l’incoerenza AGOF / AGOD e PCM / PCBM (S13.26) e la sigla NICO (S13.32);
- **la stampa di Motte 1846 e Motte 1729**: gli errori nelle formule (SVG 191, 338, 344, 347–348) potrebbero essere della conversione digitale;
- **la pagina finale del latino**: dopo il marcatore 〈229〉 la trascrizione non ne riporta altri;
- **le notizie storiche** delle note N13 e N15 contrassegnate come «non verificate»: sono conoscenze generali, non ricavate dalle fonti del fascicolo.

---

## Registro del lavoro successivo

| Unità | Stato |
|---|---|
| Sez. XIII (Prop. LXXXV–XCIII, Scolio) | **Fascicolo 12, presente documento, prima versione** |
| Sez. XIV (Prop. XCIV–XCVIII, due Scolii) e fine del Libro I | **Fascicolo 12, presente documento, prima versione** |
| Refusi *aquales*, *descrescunt*, *at vim*, *secundam*, *PPE* | Da verificare sulla stampa 1726 |
| *NICO* / NIKO (Prop. XCIII, Cor. 1); AGOF / AGOD, PCM / PCBM (Prop. XCI, Cor. 3) | Da verificare sulla stampa e sulle figure 156–158 |
| Formule di Motte 1846 (SVG 191, 338, 344, 347–348) | Da confrontare con Motte 1729; nelle pagine interattive il testo a fronte va corretto con nota |
| Glossario: *orbis* = «guscio» (guscio sferico) | Armonizzato con il Fascicolo 11 |
| Pagina interattiva candidata: Prop. XCIV–XCVI (rifrazione e riflessione come moto di un corpo) | Alta priorità didattica: legge dei seni, velocità, angolo limite; dati in Parte B |
| Pagina interattiva candidata: Prop. XCVII–XCVIII (ovale cartesiano, seconda superficie) | Dati in Parte B; la costruzione è verificata numericamente |
| Prop. XCI, Cor. 2 (sferoide esterno) | Non in Parte B perché senza dimostrazione; formula verificata (N7), utile come pagina di calcolo |
| Scolio sulla luce (figure 163–164) | Non in Parte B (scolio); eventuale pagina illustrativa sulla diffrazione |
| Revisione filologica e scientifica indipendente | Da eseguire, come previsto dalla skill di verifica |

Il presente testo è una nuova traduzione assistita da IA. Non riproduce traduzioni moderne. La trascrizione latina è © The Newton Project; il testo di Motte è di pubblico dominio.

---

## Parte B — Dati per le pagine interattive

Unità incluse: le proposizioni e i corollari con figura e dimostrazione geometrica propria: Prop. LXXXVIII, XC, XCI, XCI Cor. 1, XCI Cor. 3, XCIII, XCIV, XCV, XCVI, XCVII, XCVIII. Escluse: Prop. LXXXV–LXXXVII e LXXXIX (senza figura), XCI Cor. 2 e XCVII Cor. 2 (figura senza dimostrazione), XCII (senza figura), gli Scolii.

Convenzioni:

- `la`: testo latino esatto della trascrizione, refusi compresi (annotati in `nota`). I marcatori di pagina 〈n〉 e [FIG n] sono omessi, come nella normalizzazione di `check.py`; le parole spezzate dal cambio di pagina restano spezzate («ea dem», «con tentum», «occur rentes», «pri mum»).
- `it`: la traduzione di questo fascicolo.
- `en`: Motte 1846, allineato per senso; le formule stampate come immagine restano come «[SVG n]», e la lettura è in `nota` quando conta.
- `dipende_da`: soltanto i rimandi citati nella frase.
- `figura.mostra`: elementi da rendere visibili al passo, cumulativi salvo indicazione; `figura.evidenzia`: relazioni da mettere in risalto.

```json
{
 "fascicolo": "12-L1-S13-14",
 "versione": "0.1",
 "data": "2026-11-08",
 "convenzioni": {
  "dipende_da": "solo rimandi citati esplicitamente nella frase",
  "en": "Motte 1846, allineato per senso; formule come [SVG n]",
  "figura.mostra": "elementi da rendere visibili al passo, cumulativi salvo indicazione"
 },
 "unita": [
  {
   "id": "L1-P88",
   "tipo": "Propositio/Theorema",
   "titolo": "Prop. LXXXVIII — forze proporzionali alla distanza: il centro di gravità",
   "copertura": [
    "S13.09",
    "S13.10",
    "S13.11",
    "S13.12"
   ],
   "fonti": {
    "la": "",
    "en": "Motte 1846, pp. 235–236"
   },
   "enunciato": {
    "la": "",
    "it": "Se le forze attrattive delle particelle uguali di un corpo qualsiasi sono come le distanze dei luoghi dalle particelle, la forza del corpo intero tenderà al suo centro di gravità; e sarà la stessa della forza di un globo costituito di materia del tutto simile e uguale, e avente il centro nel centro di gravità del corpo.",
    "en": "If the attractive forces of the equal particles of any body be as the distance of the places from the particles, the force of the whole body will tend to its centre of gravity; and will be the same with the force of a globe, consisting of similar and equal matter, and having its centre in the centre of gravity."
   },
   "figura_base": {
    "punti": [
     "R",
     "S",
     "T",
     "V",
     "A",
     "B",
     "Z",
     "G",
     "C"
    ],
    "vincoli": [
     "RSTV contorno del corpo attraente",
     "A, B, C particelle del corpo",
     "Z corpuscolo attratto",
     "G su AB con AG : BG = B : A (centro di gravità di A e B)",
     "forza di ciascuna particella diretta verso di essa, proporzionale a particella × distanza"
    ]
   },
   "passi": [
    {
     "id": "L1-P88-p1",
     "la": "",
     "it": "Le particelle A, B del corpo RSTV attraggano un corpuscolo Z con forze che, se le particelle sono uguali fra loro, stiano come le distanze AZ, BZ; se invece le particelle si suppongono disuguali, stiano come queste particelle e le loro distanze AZ, BZ considerate congiuntamente, ossia (se così posso dire) come queste particelle moltiplicate rispettivamente per le loro distanze AZ, BZ.",
     "en": "Let the particles A, B, of the body RSTV attract any corpuscle Z with forces which, supposing the particles to be equal between themselves, are as the distances AZ, BZ; but, if they are supposed unequal, are as those particles and their distances AZ, BZ, conjunctly, or (if I may so speak) as those particles drawn into their distances AZ, BZ respectively.",
     "dipende_da": [],
     "figura": {
      "mostra": [
       "corpo RSTV",
       "particelle A, B",
       "corpuscolo Z",
       "segmenti AZ, BZ"
      ],
      "evidenzia": [
       "forza ∝ particella × distanza"
      ]
     }
    },
    {
     "id": "L1-P88-p2",
     "la": "",
     "it": "E si rappresentino queste forze con quei prodotti A × AZ e B × BZ.",
     "en": "And let those forces be expressed by the contents under A × AZ, and B × BZ.",
     "dipende_da": [],
     "figura": {
      "mostra": [
       "vettori A × AZ (da Z verso A) e B × BZ (da Z verso B)"
      ],
      "evidenzia": [
       "A × AZ, B × BZ"
      ]
     }
    },
    {
     "id": "L1-P88-p3",
     "la": "",
     "it": "Si congiunga AB, e la si tagli in G in modo che AG stia a BG come la particella B sta alla particella A: G sarà il centro comune di gravità delle particelle A e B.",
     "en": "Join AB, and let it be cut in G, so that AG may be to BG as the particle B to the particle A; and G will be the common centre of gravity of the particles A and B.",
     "dipende_da": [],
     "figura": {
      "mostra": [
       "segmento AB",
       "punto G"
      ],
      "evidenzia": [
       "AG : BG = B : A"
      ]
     }
    },
    {
     "id": "L1-P88-p4",
     "la": "",
     "it": "La forza A × AZ (per il Cor. 2 delle leggi) si scompone nelle forze A × GZ e A × AG, e la forza B × BZ nelle forze B × GZ e B × BG.",
     "en": "The force A × AZ will (by Cor. 2, of the Laws) be resolved into the forces A × GZ and A × AG; and the force B × BZ into the forces B × GZ and B × BG.",
     "dipende_da": [
      "Leggi, Cor. II"
     ],
     "figura": {
      "mostra": [
       "segmento GZ",
       "componenti A × GZ, A × AG",
       "componenti B × GZ, B × BG"
      ],
      "evidenzia": [
       "A × AZ = A × GZ + A × AG",
       "B × BZ = B × GZ + B × BG"
      ]
     }
    },
    {
     "id": "L1-P88-p5",
     "la": "",
     "it": "Ma le forze A × AG e B × BG, poiché A sta a B come BG sta ad AG, sono uguali; e perciò, essendo dirette verso parti contrarie, si distruggono a vicenda.",
     "en": "Now the forces A × AG and B × BG, because A is proportional to B, and BG to AG, are equal, and therefore having contrary directions destroy one another.",
     "dipende_da": [],
     "figura": {
      "mostra": [
       "A × AG e B × BG lungo AB, versi opposti"
      ],
      "evidenzia": [
       "A × AG = B × BG",
       "annullamento"
      ]
     },
     "nota": "Motte rende «ob proportionales A ad B & BG ad AG» con «because A is proportional to B, and BG to AG» (apparato A.4)."
    },
    {
     "id": "L1-P88-p6",
     "la": "",
     "it": "Restano le forze A × GZ e B × GZ.",
     "en": "There remain then the forces A × GZ and B × GZ.",
     "dipende_da": [],
     "figura": {
      "mostra": [
       "A × GZ, B × GZ"
      ],
      "evidenzia": [
       "componenti residue, tutte lungo ZG"
      ]
     }
    },
    {
     "id": "L1-P88-p7",
     "la": "",
     "it": "Queste tendono da Z verso il centro G e compongono la forza (A + B) × GZ: cioè la stessa forza che si avrebbe se le particelle attrattive A e B si trovassero nel loro centro comune di gravità G, componendovi un globo.",
     "en": "These tend from Z towards the centre G, and compose the force [SVG 314]; that is, the same force as if the attractive particles A and B were placed in their common centre of gravity G, composing there a little globe.",
     "dipende_da": [],
     "figura": {
      "mostra": [
       "risultante (A + B) × GZ",
       "globo in G"
      ],
      "evidenzia": [
       "(A + B) × GZ"
      ]
     },
     "nota": "«A+B¯×GZ» = (A + B) × GZ (vinculum); SVG 314 di Motte concorda. Virgola spuria in «gravitatis, centro G». Motte aggiunge «little»."
    },
    {
     "id": "L1-P88-p8",
     "la": "",
     "it": "Con lo stesso argomento, se si aggiunge una terza particella C e si compone la sua forza con la forza (A + B) × GZ che tende al centro G, la forza che ne nasce tenderà al centro comune di gravità di quel globo in G e della particella C, cioè al centro comune di gravità delle tre particelle A, B, C; e sarà la stessa che si avrebbe se il globo e la particella C si trovassero in quel centro comune, componendovi un globo maggiore.",
     "en": "By the same reasoning, if there be added a third particle C, and the force of it be compounded with the force [SVG 315] tending to the centre G, the force thence arising will tend to the common centre of gravity of that globe in G and of the particle C; that is, to the common centre of gravity of the three particles A, B, C; and will be the same as if that globe and the particle C were placed in that common centre composing a greater globe there",
     "dipende_da": [],
     "figura": {
      "mostra": [
       "particella C",
       "centro comune di G (con massa A + B) e C",
       "globo maggiore"
      ],
      "evidenzia": [
       "iterazione del passo precedente"
      ]
     }
    },
    {
     "id": "L1-P88-p9",
     "la": "",
     "it": "E così si procede all’infinito.",
     "en": "and so we may go on in infinitum.",
     "dipende_da": [],
     "figura": {
      "mostra": [
       "altre particelle del corpo RSTV"
      ],
      "evidenzia": []
     }
    },
    {
     "id": "L1-P88-p10",
     "la": "",
     "it": "Dunque la forza totale di tutte le particelle di un corpo qualsiasi RSTV è la stessa che si avrebbe se quel corpo, conservando il centro di gravità, assumesse la figura di un globo.",
     "en": "Therefore the whole force of all the particles of any body whatever RSTV is the same as if that body, without removing its centre of gravity, were to put on the form of a globe.",
     "dipende_da": [],
     "figura": {
      "mostra": [
       "centro di gravità del corpo",
       "globo equivalente"
      ],
      "evidenzia": [
       "forza totale = M × (distanza di Z dal centro di gravità)"
      ]
     }
    }
   ]
  },
  {
   "id": "L1-P90",
   "tipo": "Propositio/Problema",
   "titolo": "Prop. XC — attrazione di un cerchio su un punto del suo asse",
   "copertura": [
    "S13.16",
    "S13.17",
    "S13.18",
    "S13.19",
    "S13.20",
    "S13.21"
   ],
   "fonti": {
    "la": "",
    "en": "Motte 1846, pp. 237–238"
   },
   "enunciato": {
    "la": "",
    "it": "Se verso i singoli punti di un cerchio qualsiasi tendono forze centripete uguali, crescenti o decrescenti in un rapporto qualsiasi delle distanze, trovare la forza con cui è attratto un corpuscolo posto in un punto qualsiasi della retta che si innalza perpendicolarmente al piano del cerchio nel suo centro.",
    "en": "If to the several points of any circle there tend equal centripetal forces, increasing or decreasing in any ratio of the distances; it is required to find the force with which a corpuscle is attracted, that is, situate any where in a right line which stands at right angles to the plane of the circle at its centre."
   },
   "figura_base": {
    "punti": [
     "A",
     "D",
     "P",
     "E",
     "e",
     "F",
     "f",
     "K",
     "k",
     "C",
     "H",
     "I",
     "L"
    ],
    "vincoli": [
     "cerchio di centro A e raggio AD in un piano ⊥ AP",
     "E sul cerchio (raggio AE variabile), Ee piccolissima su AE",
     "F su PA con PF = PE; FK ⊥ PA, FK ∝ forza del punto E su P",
     "C su PE e f su PA con PC = Pf = Pe",
     "H su PA con PH = PD; HI ⊥ PA",
     "curva IKL luogo di K; L sul piano del cerchio"
    ]
   },
   "passi": [
    {
     "id": "L1-P90-p1",
     "la": "",
     "it": "Con centro A e con un raggio qualsiasi AD, in un piano al quale è perpendicolare la retta AP, si immagini descritto un cerchio; e si debba trovare la forza con cui un corpuscolo qualsiasi P è attratto verso di esso.",
     "en": "Suppose a circle to be described about the centre A with any interval AD in a plane to which the right line AP is perpendicular; and let it be required to find the force with which a corpuscle P is attracted towards the same.",
     "dipende_da": [],
     "figura": {
      "mostra": [
       "cerchio (A, AD)",
       "retta AP ⊥ piano",
       "P"
      ],
      "evidenzia": [
       "AP asse del cerchio"
      ]
     }
    },
    {
     "id": "L1-P90-p2",
     "la": "",
     "it": "Da un punto qualsiasi E del cerchio si conduca la retta PE al corpuscolo attratto P.",
     "en": "From any point E of the circle, to the attracted corpuscle P, let there be drawn the right line PE.",
     "dipende_da": [],
     "figura": {
      "mostra": [
       "E",
       "PE"
      ],
      "evidenzia": []
     }
    },
    {
     "id": "L1-P90-p3",
     "la": "",
     "it": "Sulla retta PA si prenda PF uguale a PE, e si innalzi la normale FK, che sia come la forza con cui il punto E attrae il corpuscolo P.",
     "en": "In the right line PA take PF equal to PE, and make a perpendicular FK, erected at F, to be as the force with which the point E attracts the corpuscle P.",
     "dipende_da": [],
     "figura": {
      "mostra": [
       "F su PA",
       "FK ⊥ PA"
      ],
      "evidenzia": [
       "PF = PE",
       "FK ∝ forza di E su P"
      ]
     }
    },
    {
     "id": "L1-P90-p4",
     "la": "",
     "it": "E sia IKL la linea curva che il punto K tocca continuamente.",
     "en": "And let the curve line IKL be the locus of the point K.",
     "dipende_da": [],
     "figura": {
      "mostra": [
       "curva IKL (luogo di K al variare di E)"
      ],
      "evidenzia": [
       "IKL"
      ]
     }
    },
    {
     "id": "L1-P90-p5",
     "la": "",
     "it": "Essa incontri il piano del cerchio in L.",
     "en": "Let that curve meet the plane of the circle in L.",
     "dipende_da": [],
     "figura": {
      "mostra": [
       "L (K per E = A, cioè PF = PA)"
      ],
      "evidenzia": []
     }
    },
    {
     "id": "L1-P90-p6",
     "la": "",
     "it": "Su PA si prenda PH uguale a PD, e si innalzi la perpendicolare HI, che incontri in I la curva suddetta: l’attrazione del corpuscolo P verso il cerchio sarà come l’area AHIL moltiplicata per l’altezza AP.",
     "en": "In PA take PH equal to PD, and erect the perpendicular HI meeting that curve in I; and the attraction of the corpuscle P towards the circle will be as the area AHIL drawn into the altitude AP.",
     "dipende_da": [],
     "figura": {
      "mostra": [
       "H con PH = PD",
       "HI",
       "area AHIL"
      ],
      "evidenzia": [
       "attrazione ∝ area AHIL × AP"
      ]
     }
    },
    {
     "id": "L1-P90-p7",
     "la": "",
     "it": "Su AE si prenda infatti una linea piccolissima Ee.",
     "en": "For let there be taken in AE a very small line Ee.",
     "dipende_da": [],
     "figura": {
      "mostra": [
       "e su AE",
       "anello di raggi AE, Ae"
      ],
      "evidenzia": [
       "Ee piccolissima"
      ]
     }
    },
    {
     "id": "L1-P90-p8",
     "la": "",
     "it": "Si congiunga Pe, e su PE, PA si prendano PC, Pf uguali a Pe.",
     "en": "Join Pe, and in PE, PA take PC, Pf equal to Pe.",
     "dipende_da": [],
     "figura": {
      "mostra": [
       "Pe",
       "C su PE",
       "f su PA"
      ],
      "evidenzia": [
       "PC = Pf = Pe",
       "CE = Ff"
      ]
     },
     "nota": "«in PPE, PA»: lettera P duplicata nella trascrizione; si legge «in PE, PA»."
    },
    {
     "id": "L1-P90-p9",
     "la": "",
     "it": "E poiché la forza con cui un punto qualsiasi E dell’anello, descritto con centro A e raggio AE nel piano suddetto, attrae a sé il corpo P si suppone come FK, e quindi la forza con cui quel punto attrae il corpo P verso A è come AP × FK / PE, e la forza con cui l’intero anello attrae il corpo P verso A è come l’anello e AP × FK / PE considerati congiuntamente; e poiché quell’anello è come il rettangolo compreso dal raggio AE e dalla larghezza Ee, e questo rettangolo (poiché PE sta ad AE come Ee sta a CE) è uguale al rettangolo PE × CE, ossia PE × Ff; la forza con cui quell’anello attrae il corpo P verso A sarà come PE × Ff e AP × FK / PE considerati congiuntamente, cioè come il prodotto Ff × FK × AP, ossia come l’area FKkf moltiplicata per AP.",
     "en": "And because the force, with which any point E of the annulus described about the centre A with the interval AE in the aforesaid plane attracts to itself the body P, is supposed to be as FK; and, therefore, the force with which that point attracts the body P towards A is as [SVG 316]; and the force with which the whole annulus attracts the body P towards A is as the annulus and [SVG 316] conjunctly; and that annulus also is as the rectangle under the radius AE and the breadth Ee, and this rectangle (because PE and AE, Ee and CE are proportional) is equal to the rectangle PE × CE or PE × Ff; the force with which that annulus attracts the body P towards A will be as PE × Ff and [SVG 316] conjunctly; that is, as the content under Ff × FK AP, or as the area FKkf drawn into AP.",
     "dipende_da": [],
     "figura": {
      "mostra": [
       "componente lungo PA della forza di E",
       "anello",
       "triangoli per PE : AE = Ee : CE",
       "striscia FKkf"
      ],
      "evidenzia": [
       "componente assiale = FK × AP/PE",
       "AE × Ee = PE × CE = PE × Ff",
       "forza dell’anello ∝ area FKkf × AP"
      ]
     },
     "nota": "«AP×FKPE» = AP × FK / PE (SVG 316 di Motte). Motte stampa «Ff × FK AP» senza il secondo segno ×."
    },
    {
     "id": "L1-P90-p10",
     "la": "",
     "it": "E perciò la somma delle forze con cui tutti gli anelli del cerchio descritto con centro A e raggio AD attraggono il corpo P verso A è come l’area totale AHIKL moltiplicata per AP.",
     "en": "And therefore the sum of the forces with which all the annuli, in the circle described about the centre A with the interval AD, attract the body P towards A, is as the whole area AHIKL drawn into AP.",
     "dipende_da": [],
     "figura": {
      "mostra": [
       "tutti gli anelli da A a D",
       "area AHIKL"
      ],
      "evidenzia": [
       "somma delle strisce = area AHIKL"
      ]
     }
    }
   ]
  },
  {
   "id": "L1-P91",
   "tipo": "Propositio/Problema",
   "titolo": "Prop. XCI — attrazione di un solido rotondo su un punto dell’asse",
   "copertura": [
    "S13.22",
    "S13.23"
   ],
   "fonti": {
    "la": "",
    "en": "Motte 1846, p. 238"
   },
   "enunciato": {
    "la": "",
    "it": "Trovare l’attrazione di un corpuscolo posto sull’asse di un solido rotondo, verso i cui singoli punti tendono forze centripete uguali, decrescenti in un rapporto qualsiasi delle distanze.",
    "en": "To find the attraction of a corpuscle situate in the axis of a round solid, to whose several points there tend equal centripetal forces decreasing in any ratio of the distances whatsoever."
   },
   "figura_base": {
    "punti": [
     "D",
     "E",
     "C",
     "G",
     "A",
     "B",
     "P",
     "R",
     "F",
     "S",
     "K",
     "L",
     "I"
    ],
    "vincoli": [
     "solido DECG di rotazione intorno all’asse AB",
     "P sull’asse",
     "RFS sezione circolare ⊥ AB con centro F",
     "FK sul semidiametro FS, ∝ attrazione del cerchio RFS su P (Prop. XC)",
     "AL, BI nei piani dei cerchi estremi"
    ]
   },
   "passi": [
    {
     "id": "L1-P91-p1",
     "la": "",
     "it": "Il corpuscolo P, posto sul suo asse AB, sia attratto verso il solido DECG.",
     "en": "Let the corpuscle P, situate in the axis AB of the solid DECG, be attracted towards that solid.",
     "dipende_da": [],
     "figura": {
      "mostra": [
       "solido DECG",
       "asse AB",
       "P"
      ],
      "evidenzia": []
     }
    },
    {
     "id": "L1-P91-p2",
     "la": "",
     "it": "Si tagli questo solido con un cerchio qualsiasi RFS perpendicolare all’asse, e sul suo semidiametro FS, in un piano PALKB passante per l’asse, si prenda (per la Prop. XC) la lunghezza FK proporzionale alla forza con cui il corpuscolo P è attratto verso quel cerchio.",
     "en": "Let the solid be cut by any circle as RFS, perpendicular to the axis; and in its semi-diameter FS, in any plane PALKB passing through the axis, let there be taken (by Prop. XC) the length FK proportional to the force with which the corpuscle P is attracted towards that circle.",
     "dipende_da": [
      "Prop. XC"
     ],
     "figura": {
      "mostra": [
       "sezione RFS",
       "semidiametro FS",
       "FK"
      ],
      "evidenzia": [
       "FK ∝ attrazione del cerchio RFS (Prop. XC)"
      ]
     }
    },
    {
     "id": "L1-P91-p3",
     "la": "",
     "it": "Il punto K tocchi poi la linea curva LKI, che incontra in L e in I i piani dei cerchi estremi AL e BI: l’attrazione del corpuscolo P verso il solido sarà come l’area LABI.",
     "en": "Let the locus of the point K be the curve line LKI, meeting the planes of the outermost circles AL and BI in L and I; and the attraction of the corpuscle P towards the solid will be as the area LABI.",
     "dipende_da": [],
     "figura": {
      "mostra": [
       "curva LKI",
       "L, I",
       "area LABI"
      ],
      "evidenzia": [
       "attrazione ∝ area LABI (somma dei dischi)"
      ]
     }
    }
   ]
  },
  {
   "id": "L1-P91-Cor1",
   "tipo": "Corollarium",
   "titolo": "Prop. XCI, Cor. 1 — attrazione di un cilindro (legge dell’inverso del quadrato)",
   "copertura": [
    "S13.24"
   ],
   "fonti": {
    "la": "",
    "en": "Motte 1846, pp. 238–239"
   },
   "enunciato": {
    "la": "",
    "it": "Di qui, se il solido è un cilindro, descritto dal parallelogramma ADEB fatto ruotare intorno all’asse AB, e le forze centripete che tendono ai suoi singoli punti sono inversamente come i quadrati delle distanze dai punti, l’attrazione del corpuscolo P verso questo cilindro sarà come AB − PE + PD.",
    "en": "Hence if the solid be a cylinder described by the parallelogram ADEB revolved about the axis AB, and the centripetal forces tending to the several points be reciprocally as the squares of the distances from the points; the attraction of the corpuscle P towards this cylinder will be as [SVG 326]."
   },
   "figura_base": {
    "punti": [
     "A",
     "D",
     "E",
     "B",
     "P",
     "F",
     "R",
     "K",
     "L",
     "I"
    ],
    "vincoli": [
     "ADEB rettangolo che ruota intorno ad AB (raggio AD = BE)",
     "P sul prolungamento dell’asse oltre A",
     "PD, PE distanze di P dai bordi delle basi",
     "PR distanza di P dal bordo della sezione per F",
     "FK ∝ 1 − PF/PR"
    ]
   },
   "passi": [
    {
     "id": "L1-P91-Cor1-p1",
     "la": "",
     "it": "Infatti l’ordinata FK (per il Cor. 1 della Prop. XC) sarà come 1 − PF/PR.",
     "en": "For the ordinate FK (by Cor. 1, Prop. XC) will be as [SVG 327].",
     "dipende_da": [
      "Prop. XC, Cor. 1"
     ],
     "figura": {
      "mostra": [
       "F",
       "R",
       "FK"
      ],
      "evidenzia": [
       "FK ∝ 1 − PF/PR"
      ]
     },
     "nota": "«1−PFPR» = 1 − PF/PR (SVG 327)."
    },
    {
     "id": "L1-P91-Cor1-p2",
     "la": "",
     "it": "La sua parte 1, moltiplicata per la lunghezza AB, descrive l’area 1 × AB; e l’altra parte, PF/PR, moltiplicata per la lunghezza PB, descrive l’area 1 × (PE − AD), cosa che si può mostrare facilmente dalla quadratura della curva LKI; e similmente la stessa parte, moltiplicata per la lunghezza PA, descrive l’area 1 × (PD − AD), e, moltiplicata per AB, differenza di PB e PA, descrive la differenza delle aree, 1 × (PE − PD).",
     "en": "The part 1 of this quantity, drawn into the length AB, describes the area 1 × AB; and the other part [SVG 328], drawn into the length PB describes the area 1 into [SVG 329] (as may be easily shewn from the quadrature of the curve LKI); and, in like manner, the same part drawn into the length PA describes the area 1 into [SVG 330], and drawn into AB, the difference of PB and PA, describes 1 into [SVG 331], the difference of the areas.",
     "dipende_da": [],
     "figura": {
      "mostra": [
       "rettangolo 1 × AB",
       "area sotto PF/PR da P a B e da P a A"
      ],
      "evidenzia": [
       "∫ PF/PR = PE − AD (su PB)",
       "∫ PF/PR = PD − AD (su PA)",
       "differenza: PE − PD"
      ]
     },
     "nota": "«1 in PE−AD¯» = 1 × (PE − AD), con vinculum. «Moltiplicata per la lunghezza» è qui una quadratura (nota N6)."
    },
    {
     "id": "L1-P91-Cor1-p3",
     "la": "",
     "it": "Dal primo prodotto, 1 × AB, si tolga l’ultimo, 1 × (PE − PD): resterà l’area LABI uguale a 1 × (AB − PE + PD).",
     "en": "From the first content 1 × AB take away the last content 1 into [SVG 331], and there will remain the area LABI equal to 1 into [SVG 332].",
     "dipende_da": [],
     "figura": {
      "mostra": [
       "area LABI"
      ],
      "evidenzia": [
       "LABI = AB − (PE − PD)"
      ]
     },
     "nota": "«con tentum»: parola spezzata dal cambio di pagina (217)."
    },
    {
     "id": "L1-P91-Cor1-p4",
     "la": "",
     "it": "Dunque la forza, proporzionale a quest’area, è come AB − PE + PD.",
     "en": "Therefore the force, being proportional to this area, is as [SVG 326].",
     "dipende_da": [],
     "figura": {
      "mostra": [
       "forza del cilindro"
      ],
      "evidenzia": [
       "forza ∝ AB − PE + PD"
      ]
     }
    }
   ]
  },
  {
   "id": "L1-P91-Cor3",
   "tipo": "Corollarium",
   "titolo": "Prop. XCI, Cor. 3 — punto interno allo sferoide: forza proporzionale alla distanza",
   "copertura": [
    "S13.26"
   ],
   "fonti": {
    "la": "",
    "en": "Motte 1846, pp. 239–240"
   },
   "enunciato": {
    "la": "",
    "it": "Se poi il corpuscolo è collocato dentro lo sferoide, sull’asse, l’attrazione sarà come la sua distanza dal centro.",
    "en": "If the corpuscle be placed within the spheroid and in its axis, the attraction will be as its distance from the centre."
   },
   "figura_base": {
    "punti": [
     "A",
     "G",
     "O",
     "F",
     "D",
     "S",
     "P",
     "E",
     "B",
     "C",
     "M",
     "H",
     "L",
     "N",
     "I",
     "K"
    ],
    "vincoli": [
     "sferoide esterno AGOF (poi chiamato AGOD) di centro S",
     "P interno; SPA semidiametro per P",
     "DE, FG rette qualsiasi per P",
     "PCM (poi PCBM) sferoide simile e concentrico per P; taglia DE in B, FG in C",
     "HLN sferoide simile e concentrico; taglia DE in H, I e FG in K, L",
     "tutti gli sferoidi con l’asse in comune"
    ]
   },
   "passi": [
    {
     "id": "L1-P91-Cor3-p1",
     "la": "",
     "it": "Ciò si ricava più facilmente con questo argomento, sia che la particella si trovi sull’asse, sia su un qualsiasi altro diametro dato.",
     "en": "This may be easily collected from the following reasoning, whether the particle be in the axis or in any other given diameter.",
     "dipende_da": [],
     "figura": {
      "mostra": [],
      "evidenzia": []
     },
     "nota": "Motte perde il comparativo di «facilius»."
    },
    {
     "id": "L1-P91-Cor3-p2",
     "la": "",
     "it": "Sia AGOF lo sferoide attraente, S il suo centro e P il corpo attratto.",
     "en": "Let AGOF be an attracting spheroid, S its centre, and P the body attracted.",
     "dipende_da": [],
     "figura": {
      "mostra": [
       "sferoide AGOF",
       "centro S",
       "P"
      ],
      "evidenzia": []
     },
     "nota": "Lo stesso sferoide è chiamato AGOD alla fine (passo 9), sia nel latino sia in Motte."
    },
    {
     "id": "L1-P91-Cor3-p3",
     "la": "",
     "it": "Per il corpo P si conducano sia il semidiametro SPA, sia due rette qualsiasi DE, FG, che incontrano lo sferoide da una parte e dall’altra in D ed E, F e G; e siano PCM, HLN le superfici di due sferoidi interni, simili all’esterno e concentrici, il primo dei quali passi per il corpo P e tagli le rette DE e FG in B e C, il secondo tagli le stesse rette in H, I e K, L.",
     "en": "Through the body P let there be drawn the semi-diameter SPA, and two right lines DE, FG meeting the spheroid in D and E, F and G; and let PCM, HLN be the superficies of two interior spheroids similar and concentrical to the exterior, the first of which passes through the body P, and cuts the right lines DE, FG in B and C; and the latter cuts the same right lines in H and I, K and L.",
     "dipende_da": [],
     "figura": {
      "mostra": [
       "SPA",
       "DE",
       "FG",
       "sferoide interno PCM per P",
       "sferoide HLN",
       "B, C, H, I, K, L"
      ],
      "evidenzia": [
       "sferoidi simili e concentrici"
      ]
     },
     "nota": "«occur rentes»: parola spezzata dal cambio di pagina (218)."
    },
    {
     "id": "L1-P91-Cor3-p4",
     "la": "",
     "it": "Abbiano poi tutti gli sferoidi l’asse in comune: le parti delle rette intercettate da una parte e dall’altra, DP e BE, FP e CG, DH e IE, FK e LG, saranno uguali fra loro, poiché le rette DE, PB e HI sono divise a metà nello stesso punto, come pure le rette FG, PC e KL.",
     "en": "Let the spheroids have all one common axis, and the parts of the right lines intercepted on both sides DP and BE, FP and CG, DH and IE, FK and LG, will be mutually equal; because the right lines DE, PB, and HI, are bisected in the same point, as are also the right lines FG, PC, and KL.",
     "dipende_da": [],
     "figura": {
      "mostra": [
       "punti medi comuni delle corde DE, PB, HI e FG, PC, KL"
      ],
      "evidenzia": [
       "DP = BE, FP = CG, DH = IE, FK = LG"
      ]
     }
    },
    {
     "id": "L1-P91-Cor3-p5",
     "la": "",
     "it": "Immagina ora che DPF, EPG designino coni opposti, descritti con angoli al vertice DPF, EPG infinitamente piccoli, e che anche le linee DH, EI siano infinitamente piccole: le particelle dei coni tagliate dalle superfici degli sferoidi, DHKF, GLIE, per l’uguaglianza delle linee DH, EI staranno fra loro come i quadrati delle loro distanze dal corpuscolo P, e perciò attrarranno quel corpuscolo in egual misura.",
     "en": "Conceive now DPF, EPG to represent opposite cones described with the infinitely small vertical angles DPF, EPG, and the lines DH, EI to be infinitely small also. Then the particles of the cones DHKF, GLIE, cut off by the spheroidical superficies, by reason of the equality of the lines DH and EI, will be to one another as the squares of the distances from the body P, and will therefore attract that corpuscle equally.",
     "dipende_da": [],
     "figura": {
      "mostra": [
       "coni opposti DPF, EPG di vertice P",
       "tronchi DHKF, GLIE"
      ],
      "evidenzia": [
       "DH = EI",
       "massa ∝ distanza² ⇒ attrazioni uguali e opposte"
      ]
     }
    },
    {
     "id": "L1-P91-Cor3-p6",
     "la": "",
     "it": "E per la stessa ragione, se gli spazi DPF, EGCB si dividono in particelle mediante le superfici di innumerevoli sferoidi simili, concentrici e aventi l’asse in comune, tutte queste particelle attrarranno in egual misura, da una parte e dall’altra, il corpo P verso parti contrarie.",
     "en": "And by a like reasoning if the spaces DPF, EGCB be divided into particles by the superficies of innumerable similar spheroids concentric to the former and having one common axis, all these particles will equally attract on both sides the body P towards contrary parts.",
     "dipende_da": [],
     "figura": {
      "mostra": [
       "spazi DPF, EGCB suddivisi da sferoidi simili"
      ],
      "evidenzia": [
       "coppie di particelle con attrazioni opposte uguali"
      ]
     }
    },
    {
     "id": "L1-P91-Cor3-p7",
     "la": "",
     "it": "Sono dunque uguali le forze del cono DPF e del segmento conico EGCB, e per la loro contrarietà si distruggono a vicenda.",
     "en": "Therefore the forces of the cone DPF, and of the conic segment EGCB, are equal, and by their contrariety destroy each other.",
     "dipende_da": [],
     "figura": {
      "mostra": [
       "cono DPF",
       "segmento conico EGCB"
      ],
      "evidenzia": [
       "forze uguali e opposte"
      ]
     }
    },
    {
     "id": "L1-P91-Cor3-p8",
     "la": "",
     "it": "E lo stesso vale per le forze di tutta la materia che sta fuori dello sferoide più interno PCBM.",
     "en": "And the case is the same of the forces of all the matter that lies without the interior spheroid PCBM.",
     "dipende_da": [],
     "figura": {
      "mostra": [
       "guscio fra PCBM e lo sferoide esterno"
      ],
      "evidenzia": [
       "il guscio omeoide non agisce su P"
      ]
     }
    },
    {
     "id": "L1-P91-Cor3-p9",
     "la": "",
     "it": "Il corpo P è dunque attratto soltanto dallo sferoide più interno PCBM; e perciò (per il Cor. 3 della Prop. LXXII) la sua attrazione sta alla forza con cui il corpo A è attratto dall’intero sferoide AGOD come la distanza PS sta alla distanza AS.",
     "en": "Therefore the body P is attracted by the interior spheroid PCBM alone, and therefore (by Cor. 3, Prop. LXXII) its attraction is to the force with which the body A is attracted by the whole spheroid AGOD as the distance PS to the distance AS.",
     "dipende_da": [
      "Prop. LXXII, Cor. 3"
     ],
     "figura": {
      "mostra": [
       "sferoide interno PCBM",
       "A sulla superficie esterna"
      ],
      "evidenzia": [
       "forza in P : forza in A = PS : AS"
      ]
     },
     "nota": "Prop. LXXII, Cor. 3: solidi simili attraggono punti posti in modo simile con forze proporzionali ai diametri."
    }
   ]
  },
  {
   "id": "L1-P93",
   "tipo": "Propositio/Theorema",
   "titolo": "Prop. XCIII — attrazione di un solido terminato da un piano",
   "copertura": [
    "S13.29",
    "S13.30",
    "S13.31",
    "S13.32",
    "S13.33",
    "S13.34"
   ],
   "fonti": {
    "la": "",
    "en": "Motte 1846, pp. 240–242"
   },
   "enunciato": {
    "la": "",
    "it": "Se un solido, piano da una parte e infinito dalle altre, è costituito di particelle uguali e ugualmente attrattive, le cui forze, man mano che ci si allontana dal solido, decrescono nel rapporto di una potenza qualsiasi delle distanze più che quadratica, e un corpuscolo posto dall’una o dall’altra parte del piano è attratto dalla forza del solido intero, dico che quella forza attrattiva del solido, man mano che ci si allontana dalla sua superficie piana, decrescerà nel rapporto di una potenza il cui lato è la distanza del corpuscolo dal piano e il cui indice è minore di tre unità dell’indice della potenza delle distanze.",
    "en": "If a solid be plane on one side, and infinitely extended on all other sides, and consist of equal particles equally attractive, whose forces decrease, in the recess from the solid, in the ratio of any power greater than the square of the distances; and a corpuscle placed towards either part of the plane is attracted by the force of the whole solid; I say that the attractive force of the whole solid, in the recess from its plane superficies, will decrease in the ratio of a power whose side is the distance of the corpuscle from the plane, and its index less by 3 than the index of the power of the distances."
   },
   "figura_base": {
    "punti": [
     "L",
     "G",
     "l",
     "m",
     "H",
     "M",
     "n",
     "I",
     "N",
     "o",
     "K",
     "O",
     "C"
    ],
    "vincoli": [
     "LGl piano che termina il solido; il solido sta dalla parte di I",
     "piani mHM, nIN, oKO paralleli a GL",
     "CGHI perpendicolare ai piani",
     "lunghezze GL, HM, IN, KO inversamente proporzionali a CGⁿ⁻², CHⁿ⁻², CIⁿ⁻², CKⁿ⁻²",
     "Caso 2: C dentro il solido, CK = CG"
    ]
   },
   "passi": [
    {
     "id": "L1-P93-p1",
     "la": "",
     "it": "Sia LGl il piano da cui il solido è terminato.",
     "en": "Let LGl be the plane by which the solid is terminated.",
     "dipende_da": [],
     "figura": {
      "mostra": [
       "piano LGl"
      ],
      "evidenzia": []
     }
    },
    {
     "id": "L1-P93-p2",
     "la": "",
     "it": "Il solido giaccia dalla parte di questo piano che è verso I, e lo si scomponga in innumerevoli piani mHM, nIN, oKO ecc., paralleli a GL.",
     "en": "Let the solid lie on that hand of the plane that is towards I, and let it be resolved into innumerable planes mHM, nIN, oKO, &c., parallel to GL.",
     "dipende_da": [],
     "figura": {
      "mostra": [
       "solido",
       "piani mHM, nIN, oKO"
      ],
      "evidenzia": [
       "solido = pila di piani paralleli"
      ]
     }
    },
    {
     "id": "L1-P93-p3",
     "la": "",
     "it": "E in primo luogo il corpo attratto C sia collocato fuori del solido.",
     "en": "And first let the attracted body C be placed without the solid.",
     "dipende_da": [],
     "figura": {
      "mostra": [
       "C fuori del solido"
      ],
      "evidenzia": []
     }
    },
    {
     "id": "L1-P93-p4",
     "la": "",
     "it": "Si conduca CGHI perpendicolare a quegli innumerevoli piani, e le forze attrattive dei punti del solido decrescano nel rapporto di una potenza delle distanze il cui indice sia un numero n non minore di tre.",
     "en": "Let there be drawn CGHI perpendicular to those innumerable planes, and let the attractive forces of the points of the solid decrease in the ratio of a power of the distances whose index is the number n not less than 3.",
     "dipende_da": [],
     "figura": {
      "mostra": [
       "perpendicolare CGHI"
      ],
      "evidenzia": [
       "indice n ≥ 3 (di fatto serve n > 3: nota N9)"
      ]
     }
    },
    {
     "id": "L1-P93-p5",
     "la": "",
     "it": "Dunque (per il Cor. 3 della Prop. XC) la forza con cui un piano qualsiasi mHM attrae il punto C è inversamente come CHⁿ⁻².",
     "en": "Therefore (by Cor. 3, Prop. XC) the force with which any plane mHM attracts the point C is reciprocally as [SVG 335].",
     "dipende_da": [
      "Prop. XC, Cor. 3"
     ],
     "figura": {
      "mostra": [
       "piano mHM",
       "CH"
      ],
      "evidenzia": [
       "forza del piano ∝ 1/CHⁿ⁻²"
      ]
     },
     "nota": "«CHn−2» = CHⁿ⁻²."
    },
    {
     "id": "L1-P93-p6",
     "la": "",
     "it": "Nel piano mHM si prenda la lunghezza HM inversamente proporzionale a CHⁿ⁻²: quella forza sarà come HM.",
     "en": "In the plane mHM take the length HM reciprocally proportional to [SVG 336], and that force will be as HM.",
     "dipende_da": [],
     "figura": {
      "mostra": [
       "HM nel piano mHM"
      ],
      "evidenzia": [
       "HM ∝ 1/CHⁿ⁻²"
      ]
     }
    },
    {
     "id": "L1-P93-p7",
     "la": "",
     "it": "Similmente nei singoli piani lGL, nIN, oKO ecc. si prendano le lunghezze GL, IN, KO ecc. inversamente proporzionali a CGⁿ⁻², CIⁿ⁻², CKⁿ⁻² ecc.: le forze di quegli stessi piani saranno come le lunghezze prese, e quindi la somma delle forze come la somma delle lunghezze, cioè la forza del solido intero come l’area GLOK prolungata all’infinito verso OK.",
     "en": "In like manner in the several planes lGL, nIN, oKO, &c., take the lengths GL, IN, KO, &c., reciprocally proportional to [SVG 337], [SVG 338], [SVG 339], &c., and the forces of those planes will be as the lengths so taken, and therefore the sum of the forces as the sum of the lengths, that is, the force of the whole solid as the area GLOK produced infinitely towards OK.",
     "dipende_da": [],
     "figura": {
      "mostra": [
       "GL, IN, KO",
       "curva LMNO…",
       "area GLOK illimitata verso OK"
      ],
      "evidenzia": [
       "somma delle forze = area GLOK"
      ]
     },
     "nota": "Motte (SVG 338) ha CLⁿ⁻² invece di CIⁿ⁻²: errore."
    },
    {
     "id": "L1-P93-p8",
     "la": "",
     "it": "Ma quell’area (per i noti metodi delle quadrature) è inversamente come CGⁿ⁻³; e perciò la forza del solido intero è inversamente come CGⁿ⁻³.",
     "en": "But that area (by the known methods of quadratures) is reciprocally as [SVG 340], and therefore the force of the whole solid is reciprocally as [SVG 340].",
     "dipende_da": [],
     "figura": {
      "mostra": [
       "area GLOK"
      ],
      "evidenzia": [
       "area ∝ 1/CGⁿ⁻³"
      ]
     }
    },
    {
     "id": "L1-P93-p9",
     "la": "",
     "it": "Si collochi ora il corpuscolo C, dalla parte del piano lGL, dentro il solido, e si prenda la distanza CK uguale alla distanza CG.",
     "en": "Let the corpuscle C be now placed on that hand of the plane lGL that is within the solid, and take the distance CK equal to the distance CG.",
     "dipende_da": [],
     "figura": {
      "mostra": [
       "Caso 2: C dentro il solido",
       "piano oKO con CK = CG"
      ],
      "evidenzia": [
       "CK = CG"
      ]
     }
    },
    {
     "id": "L1-P93-p10",
     "la": "",
     "it": "La parte del solido LGloKO, terminata dai piani paralleli lGL, oKO, non attrarrà in alcuna direzione il corpuscolo C, posto nel mezzo, poiché le azioni contrarie dei punti opposti si annullano a vicenda per la loro uguaglianza.",
     "en": "And the part of the solid LGloKO terminated by the parallel planes lGL, oKO, will attract the corpuscle C, situate in the middle, neither one way nor another, the contrary actions of the opposite points destroying one another by reason of their equality.",
     "dipende_da": [],
     "figura": {
      "mostra": [
       "strato LGloKO simmetrico rispetto a C"
      ],
      "evidenzia": [
       "azioni opposte uguali: risultante nulla"
      ]
     }
    },
    {
     "id": "L1-P93-p11",
     "la": "",
     "it": "Perciò il corpuscolo C è attratto dalla sola forza del solido situato oltre il piano OK.",
     "en": "Therefore the corpuscle C is attracted by the force only of the solid situate beyond the plane OK.",
     "dipende_da": [],
     "figura": {
      "mostra": [
       "solido oltre OK"
      ],
      "evidenzia": []
     }
    },
    {
     "id": "L1-P93-p12",
     "la": "",
     "it": "Ma questa forza (per il primo caso) è inversamente come CKⁿ⁻³, cioè (poiché CG e CK sono uguali) inversamente come CGⁿ⁻³.",
     "en": "But this force (by Case 1) is reciprocally as [SVG 341], that is, (because CG, CK are equal) reciprocally as [SVG 340].",
     "dipende_da": [
      "Prop. XCIII, Caso 1"
     ],
     "figura": {
      "mostra": [
       "CK"
      ],
      "evidenzia": [
       "forza ∝ 1/CKⁿ⁻³ = 1/CGⁿ⁻³"
      ]
     }
    }
   ]
  },
  {
   "id": "L1-P94",
   "tipo": "Propositio/Theorema",
   "titolo": "Prop. XCIV — legge dei seni per un corpo che attraversa uno strato",
   "copertura": [
    "S14.01",
    "S14.02",
    "S14.03"
   ],
   "fonti": {
    "la": "",
    "en": "Motte 1846, pp. 243–244"
   },
   "enunciato": {
    "la": "",
    "it": "Se due mezzi omogenei sono separati l’uno dall’altro da uno spazio terminato da una parte e dall’altra da piani paralleli, e un corpo, nel passare attraverso questo spazio, è attratto o spinto perpendicolarmente verso l’uno o l’altro dei due mezzi, e non è mosso né ostacolato da alcun’altra forza; e se l’attrazione, a distanze uguali da ciascuno dei due piani prese dalla stessa parte di esso, è ovunque la stessa: dico che il seno d’incidenza su uno dei due piani starà al seno di emergenza dall’altro piano in un rapporto dato.",
    "en": "If two similar mediums be separated from each other by a space terminated on both sides by parallel planes, and a body in its passage through that space be attracted or impelled perpendicularly towards either of those mediums, and not agitated or hindered by any other force; and the attraction be every where the same at equal distances from either plane, taken towards the same hand of the plane; I say, that the sine of incidence upon either plane will be to the sine of emergence from the other plane in a given ratio."
   },
   "figura_base": {
    "punti": [
     "A",
     "a",
     "B",
     "b",
     "G",
     "H",
     "I",
     "K",
     "M",
     "R",
     "L",
     "P",
     "Q",
     "N",
     "O"
    ],
    "vincoli": [
     "Aa, Bb piani paralleli (Aa d’incidenza, Bb di emergenza)",
     "GH linea d’incidenza, HI arco di parabola (forza uniforme), IK linea di emergenza",
     "IM ⊥ Bb; M su GH prolungata; R su Aa",
     "L = KI prolungata ∩ HM (punto medio di HM)",
     "cerchio (L, LI) taglia HM in P, Q e MI prolungata in N",
     "LO ⊥ MI"
    ]
   },
   "passi": [
    {
     "id": "L1-P94-p1",
     "la": "",
     "it": "Siano Aa, Bb due piani paralleli.",
     "en": "Let Aa and Bb be two parallel planes",
     "dipende_da": [],
     "figura": {
      "mostra": [
       "piani Aa, Bb"
      ],
      "evidenzia": []
     },
     "nota": "Motte unisce questa frase alla seguente."
    },
    {
     "id": "L1-P94-p2",
     "la": "",
     "it": "Il corpo incida sul primo piano, Aa, secondo la linea GH; durante tutto il suo passaggio attraverso lo spazio intermedio sia attratto o spinto verso il mezzo d’incidenza, e per questa azione descriva la linea curva HI ed emerga secondo la linea IK.",
     "en": "let the body light upon the first plane Aa in the direction of the line GH, and in its whole passage through the intermediate space let it be attracted or impelled towards the medium of incidence, and by that action let it be made to describe a curve line HI, and let it emerge in the direction of the line IK.",
     "dipende_da": [],
     "figura": {
      "mostra": [
       "GH",
       "H",
       "arco HI",
       "I",
       "IK"
      ],
      "evidenzia": [
       "forza verso il mezzo d’incidenza"
      ]
     },
     "nota": "«secundam lineam GH»: refuso probabile della trascrizione per «secundum»."
    },
    {
     "id": "L1-P94-p3",
     "la": "",
     "it": "Sul piano di emergenza Bb si innalzi la perpendicolare IM, che incontri la linea d’incidenza GH, prolungata, in M, e il piano d’incidenza Aa in R; e la linea di emergenza KI, prolungata, incontri HM in L.",
     "en": "Let there be erected IM perpendicular to Bb the plane of emergence, and meeting the line of incidence GH prolonged in M, and the plane of incidence Aa in R; and let the line of emergence KI be produced and meet HM in L.",
     "dipende_da": [],
     "figura": {
      "mostra": [
       "IM ⊥ Bb",
       "M",
       "R",
       "KI prolungata",
       "L"
      ],
      "evidenzia": []
     }
    },
    {
     "id": "L1-P94-p4",
     "la": "",
     "it": "Con centro L e raggio LI si descriva un cerchio, che tagli HM in P e Q, e MI prolungata in N. E in primo luogo, se l’attrazione o la spinta si suppone uniforme, la curva HI sarà (per ciò che ha dimostrato Galileo) una parabola, la cui proprietà è che il rettangolo formato dal lato retto dato e dalla linea IM è uguale al quadrato di HM; e inoltre la linea HM sarà divisa a metà in L.",
     "en": "About the centre L, with the interval LI, let a circle be described cutting both HM in P and Q, and MI produced in N; and, first, if the attraction or impulse be supposed uniform, the curve HI (by what Galileo has demonstrated) be a parabola, whose property is that of a rectangle under its given latus rectum and the line IM is equal to the square of HM; and moreover the line HM will be bisected in L.",
     "dipende_da": [
      "Galileo"
     ],
     "figura": {
      "mostra": [
       "cerchio (L, LI)",
       "P, Q",
       "N"
      ],
      "evidenzia": [
       "HM² = lato retto × IM",
       "HL = LM"
      ]
     },
     "nota": "Il lato retto vale 2v²/g: è dato perché velocità e forza sono date (nota N11)."
    },
    {
     "id": "L1-P94-p5",
     "la": "",
     "it": "Perciò, se su MI si abbassa la perpendicolare LO, MO e OR saranno uguali; e, aggiunte le uguali ON, OI, risulteranno uguali le intere MN, IR.",
     "en": "Whence if to MI there be let fall the perpendicular LO, MO, OR will be equal; and adding the equal lines ON, OI, the wholes MN, IR will be equal also.",
     "dipende_da": [],
     "figura": {
      "mostra": [
       "LO ⊥ MI",
       "O"
      ],
      "evidenzia": [
       "MO = OR",
       "ON = OI",
       "MN = IR"
      ]
     }
    },
    {
     "id": "L1-P94-p6",
     "la": "",
     "it": "Quindi, poiché IR è data, è data anche MN; e il rettangolo NMI sta al rettangolo formato dal lato retto e da IM, cioè a HM², in un rapporto dato.",
     "en": "Therefore since IR is given, MN is also given, and the rectangle NMI is to the rectangle under the latus rectum and IM, that is, to HM2 in a given ratio.",
     "dipende_da": [],
     "figura": {
      "mostra": [
       "IR (spessore dello strato)"
      ],
      "evidenzia": [
       "NM × MI : HM² dato"
      ]
     }
    },
    {
     "id": "L1-P94-p7",
     "la": "",
     "it": "Ma il rettangolo NMI è uguale al rettangolo PMQ, cioè alla differenza dei quadrati ML² e PL², ossia LI²; e HM² ha un rapporto dato con la sua quarta parte, ML²: è dato dunque il rapporto di ML² − LI² a ML², e, per conversione, il rapporto di LI² a ML², e il rapporto subduplicato, di LI a ML.",
     "en": "But the rectangle NMI is equal to the rectangle PMQ, that is, to the difference of the squares ML2, and PL2 or LI2; and HM2 hath a given ratio to its fourth part ML2; therefore the ratio of ML2 - LI2 to ML2 is given, and by conversion the ratio of LI2 to ML2, and its subduplicate, the ratio of LI to ML.",
     "dipende_da": [],
     "figura": {
      "mostra": [
       "PM, MQ"
      ],
      "evidenzia": [
       "NM × MI = PM × MQ = ML² − LI²",
       "HM² = 4 ML²",
       "LI : ML dato"
      ]
     }
    },
    {
     "id": "L1-P94-p8",
     "la": "",
     "it": "Ma in ogni triangolo, e dunque in LMI, i seni degli angoli sono proporzionali ai lati opposti.",
     "en": "But in every triangle, as LMI, the sines of the angles are proportional to the opposite sides.",
     "dipende_da": [],
     "figura": {
      "mostra": [
       "triangolo LMI"
      ],
      "evidenzia": [
       "teorema dei seni"
      ]
     }
    },
    {
     "id": "L1-P94-p9",
     "la": "",
     "it": "È dato dunque il rapporto del seno dell’angolo d’incidenza LMR al seno dell’angolo di emergenza LIR.",
     "en": "Therefore the ratio of the sine of the angle of incidence LMR to the sine of the angle of emergence LIR is given.",
     "dipende_da": [],
     "figura": {
      "mostra": [
       "angoli LMR, LIR"
      ],
      "evidenzia": [
       "sin LMR : sin LIR = LI : ML, dato"
      ]
     }
    },
    {
     "id": "L1-P94-p10",
     "la": "",
     "it": "Il corpo attraversi ora successivamente più spazi terminati da piani paralleli, AabB, BbcC ecc., e sia mosso da una forza che sia uniforme in ciascuno di essi separatamente, ma diversa nei diversi spazi. Per quanto si è appena dimostrato, il seno d’incidenza sul primo piano Aa starà al seno di emergenza dal secondo piano Bb in un rapporto dato; e questo seno, che è il seno d’incidenza sul secondo piano Bb, starà al seno di emergenza dal terzo piano Cc in un rapporto dato; e questo seno starà al seno di emergenza dal quarto piano Dd in un rapporto dato; e così all’infinito: e, per uguaglianza, il seno d’incidenza sul primo piano starà al seno di emergenza dall’ultimo piano in un rapporto dato.",
     "en": "Let now the body pass successively through several spaces terminated with parallel planes AabB, BbcC, &c., and let it be acted on by a force which is uniform in each of them separately, but different in the different spaces; and by what was just demonstrated, the sine of the angle of incidence on the first plane Aa is to the sine of emergence from the second plane Bb in a given ratio; and this sine of incidence upon the second plane Bb will be to the sine of emergence from the third plane Cc in a given ratio; and this sine to the sine of emergence from the fourth plane Dd in a given ratio; and so on in infinitum; and, by equality, the sine of incidence on the first plane to the sine of emergence from the last plane in a given ratio.",
     "dipende_da": [
      "Prop. XCIV, Caso 1"
     ],
     "figura": {
      "mostra": [
       "piani Aa, Bb, Cc, Dd",
       "strati AabB, BbcC, …",
       "archi parabolici diversi nei diversi strati"
      ],
      "evidenzia": [
       "catena di rapporti dati ⇒ rapporto dato (ex æquo)"
      ]
     },
     "nota": "«per jam demonstrata» rimanda al Caso 1."
    },
    {
     "id": "L1-P94-p11",
     "la": "",
     "it": "Si diminuiscano ora gli intervalli dei piani e se ne aumenti il numero all’infinito, in modo che l’azione dell’attrazione o della spinta, secondo una legge qualsiasi assegnata, sia resa continua: il rapporto del seno d’incidenza sul primo piano al seno di emergenza dall’ultimo piano, essendo sempre dato, sarà dato anche allora.",
     "en": "Let now the intervals of the planes be diminished, and their number be infinitely increased, so that the action of attraction or impulse, exerted according to any assigned law, may become continual, and the ratio of the sine of incidence on the first plane to the sine of emergence from the last plane being all along given, will be given then also.",
     "dipende_da": [],
     "figura": {
      "mostra": [
       "strati sempre più sottili",
       "traiettoria continua"
      ],
      "evidenzia": [
       "passaggio al limite"
      ]
     }
    }
   ]
  },
  {
   "id": "L1-P95",
   "tipo": "Propositio/Theorema",
   "titolo": "Prop. XCV — le velocità stanno inversamente come i seni",
   "copertura": [
    "S14.04",
    "S14.05"
   ],
   "fonti": {
    "la": "",
    "en": "Motte 1846, pp. 244–245"
   },
   "enunciato": {
    "la": "",
    "it": "Poste le stesse cose, dico che la velocità del corpo prima dell’incidenza sta alla sua velocità dopo l’emergenza come il seno di emergenza sta al seno d’incidenza.",
    "en": "The same things being supposed, I say, that the velocity of the body before its incidence is to its velocity after emergence as the sine of emergence to the sine of incidence."
   },
   "figura_base": {
    "punti": [
     "A",
     "H",
     "G",
     "I",
     "d",
     "K",
     "T",
     "v"
    ],
    "vincoli": [
     "A su Aa e d su Bb con AH = Id (distanze parallele ai piani)",
     "AG ⊥ Aa incontra GH in G; dK ⊥ Bb incontra IK in K",
     "T su GH con TH = IK",
     "Tv ⊥ Aa"
    ]
   },
   "passi": [
    {
     "id": "L1-P95-p1",
     "la": "",
     "it": "Si prendano AH e Id uguali, e si innalzino le perpendicolari AG, dK, che incontrino le linee d’incidenza e di emergenza GH, IK in G e K.",
     "en": "Make AH and Id equal, and erect the perpendiculars AG, dK meeting the lines of incidence and emergence GH, IK, in G and K.",
     "dipende_da": [],
     "figura": {
      "mostra": [
       "A, d",
       "AG, dK",
       "G, K"
      ],
      "evidenzia": [
       "AH = Id"
      ]
     }
    },
    {
     "id": "L1-P95-p2",
     "la": "",
     "it": "Su GH si prenda TH uguale a IK, e sul piano Aa si abbassi la normale Tv.",
     "en": "In GH take TH equal to IK, and to the plane Aa let fall a perpendicular Tv.",
     "dipende_da": [],
     "figura": {
      "mostra": [
       "T",
       "Tv"
      ],
      "evidenzia": [
       "TH = IK"
      ]
     }
    },
    {
     "id": "L1-P95-p3",
     "la": "",
     "it": "E (per il Cor. 2 delle leggi) si distingua il moto del corpo in due: uno perpendicolare ai piani Aa, Bb, Cc ecc., l’altro parallelo a essi.",
     "en": "And (by Cor. 2 of the Laws of Motion) let the motion of the body be resolved into two, one perpendicular to the planes Aa, Bb, Cc, &c., and another parallel to them.",
     "dipende_da": [
      "Leggi, Cor. II"
     ],
     "figura": {
      "mostra": [
       "componenti del moto ⊥ e ∥ ai piani"
      ],
      "evidenzia": []
     }
    },
    {
     "id": "L1-P95-p4",
     "la": "",
     "it": "La forza di attrazione o di spinta, agendo secondo linee perpendicolari, non muta affatto il moto secondo le parallele; e perciò il corpo, con questo moto, percorrerà in tempi uguali quegli intervalli uguali, presi secondo le parallele, che stanno fra la linea AG e il punto H e fra il punto I e la linea dK; cioè descriverà in tempi uguali le linee GH, IK.",
     "en": "The force of attraction or impulse, acting in directions perpendicular to those planes, does not at all alter the motion in parallel directions; and therefore the body proceeding with this motion will in equal times go through those equal parallel intervals that lie between the line AG and the point H, and between the point I and the line dK; that is, they will describe the lines GH, IK in equal times.",
     "dipende_da": [],
     "figura": {
      "mostra": [
       "GH, IK percorse in tempi uguali"
      ],
      "evidenzia": [
       "componente parallela conservata",
       "AH = Id ⇒ tempi uguali"
      ]
     }
    },
    {
     "id": "L1-P95-p5",
     "la": "",
     "it": "Quindi la velocità prima dell’incidenza sta alla velocità dopo l’emergenza come GH sta a IK, o a TH, cioè come AH, o Id, sta a vH, cioè (rispetto al raggio TH, o IK) come il seno di emergenza sta al seno d’incidenza.",
     "en": "Therefore the velocity before incidence is to the velocity after emergence as GH to IK or TH, that is, as AH or Id to vH, that is (supposing TH or IK radius), as the sine of emergence to the sine of incidence.",
     "dipende_da": [],
     "figura": {
      "mostra": [
       "vH"
      ],
      "evidenzia": [
       "v₁ : v₂ = GH : IK = AH : vH = sin e : sin i"
      ]
     },
     "nota": "AH = Id = IK · sin e e vH = TH · sin i, con TH = IK (nota N11)."
    }
   ]
  },
  {
   "id": "L1-P96",
   "tipo": "Propositio/Theorema",
   "titolo": "Prop. XCVI — riflessione: angolo di riflessione uguale all’angolo d’incidenza",
   "copertura": [
    "S14.06",
    "S14.07"
   ],
   "fonti": {
    "la": "",
    "en": "Motte 1846, pp. 245–246"
   },
   "enunciato": {
    "la": "",
    "it": "Poste le stesse cose, e supposto che il moto prima dell’incidenza sia più veloce che dopo, dico che il corpo, inclinando la linea d’incidenza, sarà alla fine riflesso, e l’angolo di riflessione diventerà uguale all’angolo d’incidenza.",
    "en": "The same things being supposed, and that the motion before incidence is swifter than afterwards; I say, that if the line of incidence be inclined continually, the body will be at last reflected, and the angle of reflexion will be equal to the angle of incidence."
   },
   "figura_base": {
    "punti": [
     "A",
     "a",
     "B",
     "b",
     "C",
     "c",
     "D",
     "d",
     "E",
     "e",
     "G",
     "H",
     "P",
     "Q",
     "R",
     "q",
     "p",
     "h"
    ],
    "vincoli": [
     "piani paralleli Aa, Bb, Cc, Dd, Ee",
     "archi parabolici HP, PQ, QR fra piani successivi",
     "R su Dd vertice principale dell’arco QRq",
     "archi di ritorno qp, ph simmetrici a QP, PH"
    ]
   },
   "passi": [
    {
     "id": "L1-P96-p1",
     "la": "",
     "it": "Immagina infatti che il corpo descriva fra i piani paralleli Aa, Bb, Cc ecc. archi parabolici, come sopra; e siano questi archi HP, PQ, QR ecc.",
     "en": "For conceive the body passing between the parallel planes Aa, Bb, Cc, &c., to describe parabolic arcs as above; and let those arcs be HP, PQ, QR, &c.",
     "dipende_da": [],
     "figura": {
      "mostra": [
       "piani Aa…Ee",
       "archi HP, PQ, QR"
      ],
      "evidenzia": []
     }
    },
    {
     "id": "L1-P96-p2",
     "la": "",
     "it": "E l’obliquità della linea d’incidenza GH sul primo piano Aa sia tale che il seno d’incidenza stia al raggio del cerchio di cui è seno nel rapporto che lo stesso seno d’incidenza ha con il seno di emergenza dal piano Dd nello spazio DdeE: poiché il seno di emergenza è ormai divenuto uguale al raggio, l’angolo di emergenza sarà retto, e perciò la linea di emergenza coinciderà con il piano Dd.",
     "en": "And let the obliquity of the line of incidence GH to the first plane Aa be such that the sine of incidence may be to the radius of the circle whose sine it is, in the same ratio which the same sine of incidence hath to the sine of emergence from the plane Dd into the space DdeE; and because the sine of emergence is now become equal to radius, the angle of emergence will be a right one, and therefore the line of emergence will coincide with the plane Dd.",
     "dipende_da": [],
     "figura": {
      "mostra": [
       "GH con l’inclinazione limite"
      ],
      "evidenzia": [
       "sin e = raggio ⇒ e = 90°"
      ]
     },
     "nota": "«pri mum»: parola spezzata dal cambio di pagina (225)."
    },
    {
     "id": "L1-P96-p3",
     "la": "",
     "it": "Il corpo giunga a questo piano nel punto R; e, poiché la linea di emergenza coincide con lo stesso piano, è evidente che il corpo non può procedere oltre verso il piano Ee.",
     "en": "Let the body come to this plane in the point R; and because the line of emergence coincides with that plane, it is manifest that the body can proceed no farther towards the plane Ee.",
     "dipende_da": [],
     "figura": {
      "mostra": [
       "R su Dd"
      ],
      "evidenzia": [
       "tangenza in R"
      ]
     }
    },
    {
     "id": "L1-P96-p4",
     "la": "",
     "it": "Ma non può neppure procedere lungo la linea di emergenza Rd, poiché è continuamente attratto o spinto verso il mezzo d’incidenza.",
     "en": "But neither can it proceed in the line of emergence Rd; because it is perpetually attracted or impelled towards the medium of incidence.",
     "dipende_da": [],
     "figura": {
      "mostra": [
       "Rd"
      ],
      "evidenzia": [
       "forza sempre verso il mezzo d’incidenza"
      ]
     }
    },
    {
     "id": "L1-P96-p5",
     "la": "",
     "it": "Tornerà dunque indietro fra i piani Cc, Dd, descrivendo un arco di parabola QRq, il cui vertice principale (secondo ciò che ha dimostrato Galileo) è in R; taglierà il piano Cc in q con lo stesso angolo con cui prima lo aveva tagliato in Q; poi, procedendo negli archi parabolici qp, ph ecc., simili e uguali agli archi precedenti QP, PH, taglierà gli altri piani in p, h ecc. con gli stessi angoli con cui prima li aveva tagliati in P, H ecc., ed emergerà alla fine in h con la stessa obliquità con cui era incidente in H.",
     "en": "It will return, therefore, between the planes Cc, Dd, describing an arc of a parabola QRq, whose principal vertex (by what Galileo has demonstrated) is in R, cutting the plane Cc in the same angle at q, that it did before at Q; then going on in the parabolic arcs qp, ph, &c., similar and equal to the former arcs QP, PH, &c., it will cut the rest of the planes in the same angles at p, h, &c., as it did before in P, H, &c., and will emerge at last with the same obliquity at h with which it first impinged on that plane at H.",
     "dipende_da": [
      "Galileo"
     ],
     "figura": {
      "mostra": [
       "arco QRq con vertice R",
       "q, p, h",
       "archi qp, ph"
      ],
      "evidenzia": [
       "simmetria rispetto alla perpendicolare per R",
       "angolo in h = angolo in H"
      ]
     },
     "nota": "Motte aggiunge «first»."
    },
    {
     "id": "L1-P96-p6",
     "la": "",
     "it": "Immagina ora che gli intervalli dei piani Aa, Bb, Cc, Dd, Ee ecc. diminuiscano all’infinito e che il loro numero aumenti, in modo che l’azione dell’attrazione o della spinta, secondo una legge qualsiasi assegnata, sia resa continua: l’angolo di emergenza, essendo sempre uguale all’angolo d’incidenza, resterà uguale a esso anche allora.",
     "en": "Conceive now the intervals of the planes Aa, Bb, Cc, Dd, Ee, &c., to be infinitely diminished, and the number infinitely increased, so that the action of attraction or impulse, exerted according to any assigned law, may become continual; and, the angle of emergence remaining all along equal to the angle of incidence, will be equal to the same also at last.",
     "dipende_da": [],
     "figura": {
      "mostra": [
       "strati sempre più sottili"
      ],
      "evidenzia": [
       "passaggio al limite"
      ]
     }
    }
   ]
  },
  {
   "id": "L1-P97",
   "tipo": "Propositio/Problema",
   "titolo": "Prop. XCVII — la superficie che fa convergere i corpuscoli (ovale cartesiano)",
   "copertura": [
    "S14.10",
    "S14.11",
    "S14.12",
    "S14.13"
   ],
   "fonti": {
    "la": "",
    "en": "Motte 1846, p. 247"
   },
   "enunciato": {
    "la": "",
    "it": "Posto che il seno d’incidenza su una superficie stia al seno di emergenza in un rapporto dato, e che l’incurvamento del cammino dei corpi vicino a quella superficie avvenga in uno spazio brevissimo, che si possa considerare come un punto, determinare la superficie che faccia convergere verso un altro luogo dato tutti i corpuscoli che escono successivamente da un luogo dato.",
    "en": "Supposing the sine of incidence upon any superficies to be in a given ratio to the sine of emergence; and that the inflection of the paths of those bodies near that superficies is performed in a very short space, which may be considered as a point; it is required to determine such a superficies as may cause all the corpuscles issuing from any one given place to converge to another given place."
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
     "M",
     "N"
    ],
    "vincoli": [
     "A luogo di partenza, B luogo di convergenza, sull’asse AB",
     "CDE curva cercata; C sull’asse",
     "EF ⊥ AD, EG ⊥ DB",
     "CM incremento di AC, CN decremento di BC, CM : CN = sin i : sin e",
     "D = intersezione dei cerchi (A, AM) e (B, BN)"
    ]
   },
   "passi": [
    {
     "id": "L1-P97-p1",
     "la": "",
     "it": "Sia A il luogo da cui i corpuscoli divergono; B il luogo verso cui devono convergere; CDE la linea curva che, fatta ruotare intorno all’asse AB, descriva la superficie cercata; D, E due punti qualsiasi di quella curva; ed EF, EG le perpendicolari abbassate sui cammini del corpo AD, DB.",
     "en": "Let A be the place from whence the corpuscles diverge; B the place to which they should converge; CDE the curve line which by its revolution round the axis AB describes the superficies sought; D, E, any two points of that curve; and EF, EG, perpendiculars let fall on the paths of the bodies AD, DB.",
     "dipende_da": [],
     "figura": {
      "mostra": [
       "A, B",
       "curva CDE",
       "D, E",
       "EF ⊥ AD, EG ⊥ DB"
      ],
      "evidenzia": []
     }
    },
    {
     "id": "L1-P97-p2",
     "la": "",
     "it": "Il punto D si avvicini al punto E: il rapporto ultimo della linea DF, di cui AD cresce, alla linea DG, di cui DB diminuisce, sarà lo stesso del seno d’incidenza al seno di emergenza.",
     "en": "Let the point D approach to and coalesce with the point E; and the ultimate ratio of the line DF by which AD is increased, to the line DG by which DB is diminished, will be the same as that of the sine of incidence to the sine of emergence.",
     "dipende_da": [],
     "figura": {
      "mostra": [
       "DF, DG evanescenti"
      ],
      "evidenzia": [
       "DF : DG → sin i : sin e (rapporto ultimo)"
      ]
     },
     "nota": "Motte aggiunge «and coalesce with»."
    },
    {
     "id": "L1-P97-p3",
     "la": "",
     "it": "È dato dunque il rapporto dell’incremento della linea AD al decremento della linea DB; e perciò, se sull’asse AB si prende in un luogo qualsiasi il punto C per cui la curva CDE deve passare, e si prendono l’incremento CM di AC e il decremento CN di BC in quel rapporto dato, e con centri A, B e raggi AM, BN si descrivono due cerchi che si tagliano in D, quel punto D toccherà la curva cercata CDE e, toccandola in qualsiasi luogo, la determinerà.",
     "en": "Therefore the ratio of the increment of the line AD to the decrement of the line DB is given; and therefore if in the axis AB there be taken any where the point C through which the curve CDE must pass, and CM the increment of AC be taken in that given ratio to CN the decrement of BC, and from the centres A, B, with the intervals AM, BN, there be described two circles cutting each other in D; that point D will touch the curve sought CDE, and, by touching it any where at pleasure, will determine that curve.",
     "dipende_da": [],
     "figura": {
      "mostra": [
       "C sull’asse",
       "M, N",
       "cerchi (A, AM) e (B, BN)",
       "D"
      ],
      "evidenzia": [
       "CM : CN = sin i : sin e",
       "AD + k·DB costante (nota N14)"
      ]
     }
    }
   ]
  },
  {
   "id": "L1-P98",
   "tipo": "Propositio/Problema",
   "titolo": "Prop. XCVIII — la seconda superficie che fa convergere in B",
   "copertura": [
    "S14.14",
    "S14.15",
    "S14.16"
   ],
   "fonti": {
    "la": "",
    "en": "Motte 1846, pp. 247–248"
   },
   "enunciato": {
    "la": "",
    "it": "Poste le stesse cose, e descritta intorno all’asse AB una superficie attrattiva qualsiasi CD, regolare o irregolare, attraverso la quale devono passare i corpi che escono dal luogo dato A, trovare una seconda superficie attrattiva EF che faccia convergere quei corpi verso il luogo dato B.",
    "en": "The same things supposed; if round the axis AB any attractive superficies be described as CD, regular or irregular, through which the bodies issuing from the given place A must pass; it is required to find a second attractive superficies EF, which may make those bodies converge to a given place B."
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
     "K",
     "L",
     "P",
     "Q",
     "R",
     "S"
    ],
    "vincoli": [
     "superficie CD data; C, E sull’asse AB",
     "sin i : sin e (prima superficie) = sin e : sin i (seconda) = M : N",
     "G sul prolungamento di AB: BG : CE = (M − N) : N",
     "H sul prolungamento di AD: AH = AG",
     "K sul prolungamento di DF: DK : DH = N : M",
     "L = cerchio (D, DH) ∩ KB prolungata; BF ∥ DL",
     "CP, CQ ⊥ AD, DF; ER, ES ⊥ FB, FD"
    ]
   },
   "passi": [
    {
     "id": "L1-P98-p1",
     "la": "",
     "it": "La congiungente AB tagli la prima superficie in C e la seconda in E, preso il punto D in modo qualsiasi.",
     "en": "Let a line joining AB cut the first superficies in C and the second in E, the point D being taken any how at pleasure.",
     "dipende_da": [],
     "figura": {
      "mostra": [
       "asse AB",
       "C",
       "E",
       "D sulla prima superficie"
      ],
      "evidenzia": []
     }
    },
    {
     "id": "L1-P98-p2",
     "la": "",
     "it": "E, posto che il seno d’incidenza sulla prima superficie stia al seno di emergenza dalla stessa, e il seno di emergenza dalla seconda superficie al seno d’incidenza su di essa, come una quantità data M sta a un’altra quantità data N, prolunga AB fino a G, in modo che BG stia a CE come M − N sta a N; poi AD fino a H, in modo che AH sia uguale ad AG; e poi anche DF fino a K, in modo che DK stia a DH come N sta a M.",
     "en": "And supposing the sine of incidence on the first superficies to the sine of emergence from the same, and the sine of emergence from the second superficies to the sine of incidence on the same, to be as any given quantity M to another given quantity N; then produce AB to G, so that BG may be to CE as M - N to N; and AD to H, so that AH may be equal to AG; and DF to K, so that DK may be to DH as N to M.",
     "dipende_da": [],
     "figura": {
      "mostra": [
       "G",
       "H",
       "DF (raggio rifratto)",
       "K"
      ],
      "evidenzia": [
       "BG : CE = (M − N) : N",
       "AH = AG",
       "DK : DH = N : M"
      ]
     },
     "nota": "«produc tum … tum … tum etiam»: imperativo seguito da una serie, non parola spezzata."
    },
    {
     "id": "L1-P98-p3",
     "la": "",
     "it": "Congiungi KB, e con centro D e raggio DH descrivi un cerchio che incontri in L la KB prolungata, e conduci BF parallela a DL: il punto F toccherà la linea EF, che, fatta ruotare intorno all’asse AB, descriverà la superficie cercata.",
     "en": "Join KB, and about the centre D with the interval DH describe a circle meeting KB produced in L, and draw BF parallel to DL; and the point F will touch the line EF, which, being turned round the axis AB, will describe the superficies sought.",
     "dipende_da": [],
     "figura": {
      "mostra": [
       "KB prolungata",
       "cerchio (D, DH)",
       "L",
       "BF ∥ DL",
       "F",
       "curva EF"
      ],
      "evidenzia": [
       "FB : FK = DL : DK = M : N"
      ]
     },
     "nota": "L è l’intersezione oltre B (verifica in N14)."
    },
    {
     "id": "L1-P98-p4",
     "la": "",
     "it": "Immagina infatti che le linee CP, CQ siano dovunque perpendicolari rispettivamente ad AD, DF, e le linee ER, ES a FB, FD, e che quindi QS sia sempre uguale a CE: PD starà (per il Cor. 2 della Prop. XCVII) a QD come M a N, e quindi come DL a DK, o FB a FK; e, per divisione, come DL − FB, ossia PH − PD − FB, sta a FD, ossia FQ − QD; e, per composizione, come PH − FB sta a FQ, cioè (poiché PH e CG, QS e CE sono uguali) come CE + BG − FR sta a CE − FS.",
     "en": "For conceive the lines CP, CQ to be every where perpendicular to AD, DF, and the lines ER, ES to FB, FD respectively, and therefore QS to be always equal to CE; and (by Cor. 2, Prop. XCVII) PD will be to QD as M to N, and therefore as DL to DK, or FB to FK; and by division as DL - FB or PH - PD - FB to FD or FQ - QD; and by composition as PH - FB to FQ, that is (because PH and CG, QS and CE, are equal), as CE + BG - FR to CE - FS.",
     "dipende_da": [
      "Prop. XCVII, Cor. 2"
     ],
     "figura": {
      "mostra": [
       "curve CP, CQ",
       "ER, ES",
       "P, Q, R, S"
      ],
      "evidenzia": [
       "PD : QD = M : N = DL : DK = FB : FK",
       "PH = CG",
       "QS = CE"
      ]
     }
    },
    {
     "id": "L1-P98-p5",
     "la": "",
     "it": "Ma (poiché BG sta a CE come M − N sta a N) anche CE + BG sta a CE come M sta a N; e quindi, per divisione, FR sta a FS come M sta a N; e perciò (per il Cor. 2 della Prop. XCVII) la superficie EF costringe il corpo che incide su di essa secondo la linea DF a proseguire lungo la linea FR verso il luogo B.",
     "en": "But (because BG is to CE as M - N to N) it comes to pass also that CE + BG is to CE as M to N; and therefore, by division, FR is to FS as M to N; and therefore (by Cor. 2, Prop. XCVII) the superficies EF compels a body, falling upon it in the direction DF, to go on in the line FR to the place B.",
     "dipende_da": [
      "Prop. XCVII, Cor. 2"
     ],
     "figura": {
      "mostra": [
       "raggio FB"
      ],
      "evidenzia": [
       "FR : FS = M : N ⇒ legge dei seni in F",
       "il corpo giunge in B"
      ]
     }
    }
   ]
  }
 ]
}
```

**Fine del Fascicolo 12.**
