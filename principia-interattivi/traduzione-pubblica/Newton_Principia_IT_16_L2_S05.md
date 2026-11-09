> **Copia pubblica.** In questa versione i campi `"la"` della Parte B sono vuoti: le frasi latine vengono dalla trascrizione del Newton Project, che non si ridistribuisce. Il latino del 1726 si legge su newtonproject.ox.ac.uk.

# Isaac Newton
# Principi matematici della filosofia naturale

## Fascicolo 16 — Libro II, Sezione V: densità e compressione dei fluidi; idrostatica

**Nuova traduzione italiana di lavoro dal latino del 1726, confrontata con l’inglese di Andrew Motte nell’edizione del 1846.**

Versione 0.1 — 8 novembre 2026. Preparata con Claude (Anthropic) per Massimo Bosetti.

### Stato e perimetro

Questo fascicolo prosegue il Fascicolo 15 (Libro II, Sezioni III–IV). Traduce integralmente la **Sezione V** del Libro II, *De densitate & compressione fluidorum, deque hydrostatica*: la definizione di fluido, le Proposizioni XIX–XXIII (Teoremi XIV–XVIII) con tutti i casi e i corollari, e i due scolii (alla Prop. XXII e alla Prop. XXIII). È una traduzione di lavoro, non un’edizione critica validata.

Gli identificatori **II.S5.01–II.S5.34** e i titoli tematici tra parentesi sono aggiunte editoriali. Servono a orientare la lettura e a controllare la completezza. I numeri romani delle proposizioni e dei teoremi, i numeri dei casi e dei corollari appartengono al testo originale. Le integrazioni del curatore sono tra parentesi quadre. Le note poste dopo la traduzione non fanno parte del testo di Newton.

In coda al fascicolo c’è la **Parte B**, con i dati strutturati per le pagine interattive di 6 unità con figura: Propp. XIX, XX, XXI, il Corollario della Prop. XXI, Propp. XXII e XXIII.

### Fonti effettivamente consultate

1. **Latino di riferimento.** Isaac Newton, *Philosophiæ Naturalis Principia Mathematica*, terza edizione, Londra, 1726, Libro II, Sezione V, **pp. 282–294** (la sezione comincia a p. 282, prima del marcatore ‹283›; l’ultimo marcatore della trascrizione è ‹294›). Trascrizione normalizzata del Newton Project, documento **NATP00088**, estratta in testo semplice senza correzioni: `fonti/latino-1726-L2-S05.md`. Figure citate: [FIG 38]–[FIG 43] (non incluse).
2. **Inglese di confronto.** *Newton’s Principia*, traduzione di Andrew Motte, New York, Daniel Adee, 1846, Section V, **sezione corrispondente** (l’estratto non contiene marcatori di pagina). Project Gutenberg n. 76404, estratto `fonti/motte-1846-L2-S05.md`. Le formule stampate come immagini compaiono come `[SVG 600]`–`[SVG 617]`; sono state controllate sul LaTeX dell’EPUB (`src_epub/svg_tex.tsv`, Gutenberg #76404) in una rifinitura successiva: tutte e 18 coincidono con il latino (§ A.9).
3. **Brief comune**, addendum del Libro II (`ISTRUZIONI-TRADUTTORE.md`), **Fascicolo 3** e **Fascicolo 5** come modelli di formato; trascrizione della Sezione I del Libro II (`fonti/latino-1726-L2-S01.md`) per controllare il Lemma I citato nella Prop. XXI.

Non ho consultato né riprodotto traduzioni moderne. Non ho potuto vedere la stampa del 1726, la stampa di Motte del 1729 né le figure originali: le relazioni geometriche sono ricostruite dalle sole lettere del testo.

### Criteri di traduzione

- Il testo guida è il latino; l’inglese di Motte serve a controllare le interpretazioni ed è annotato quando aggiunge, omette o si discosta.
- Si applicano il **glossario comune** del brief e il **glossario del Libro II**: *fluidum* «fluido», *densitas* «densità», *compressio* «compressione», *medium* «mezzo», *vis elastica* «forza elastica» (qui *fluidum elasticum* «fluido elastico»), *gravitas specifica* «gravità specifica», *pondus* «peso», *gravitas* «gravità», *particulæ fluidi* «particelle del fluido», *partes* «parti», *vis centrifuga* «forza centrifuga», *vas* «vaso», *canalis* «canale», *aer* «aria», *aqua* «acqua», *argentum vivum* / *mercurius* «mercurio», *globus* «globo», *sphæra* «sfera», *cylindrus* «cilindro», *solidum* «solido», *hyperbola* «iperbole», *asymptotos* «asintoto», *area hyperbolica* «area iperbolica», *progressio geometrica* «progressione geometrica», *experimentum* «esperimento», *Scholium* «Scolio»; *nisi quatenus* «se non in quanto», *ratio duplicata / triplicata / sesquiplicata* «rapporto duplicato / triplicato / sesquiplicato», *reciproce* «inversamente», *ducere in* «moltiplicare per», *conatus* «tendenza», *in infinitum* «all’infinito», Q.E.D. «C.V.D.».
- Le estensioni del glossario proprie di questo fascicolo sono elencate e motivate nel § A.0.
- Gli enunciati latini all’infinito o al congiuntivo ipotetico sono resi con l’indicativo; i congiuntivi esortativi delle costruzioni (*claudatur*, *Designet*, *Erigantur*) con il congiuntivo esortativo italiano.
- Le frazioni che la trascrizione appiattisce («AHAS», «AH×thSA», «SA cub.SAq») sono rese con la barra (AH/AS, AH×th/SA, SA³/SA²), dichiarando la lettura nel § A.8; «AB cub.», «ab quad.» sono scritti AB³, ab². Nessuna formula moderna entra nel testo tradotto.

---

## Traduzione italiana

### Sezione V. La densità e la compressione dei fluidi, e l’idrostatica

### Definizione del fluido

**[II.S5.01]** **Fluido è ogni corpo le cui parti cedono a qualsiasi forza applicata e, cedendo, si muovono facilmente fra loro.**

### Proposizione XIX. Teorema XIV (pressione uguale in ogni direzione)

**[II.S5.02]** **Tutte le parti di un fluido omogeneo e immoto, che sia racchiuso in un vaso immoto qualsiasi e compresso da ogni parte, sono premute ugualmente da ogni parte (messa da parte la considerazione della condensazione, della gravità e di tutte le forze centripete) e rimangono nei loro luoghi senza alcun moto nato da quella pressione.**

**[II.S5.03]** *Caso 1.* Nel vaso sferico ABC sia racchiuso un fluido e sia compresso uniformemente da ogni parte: dico che nessuna sua parte si muoverà per effetto di quella pressione. Se infatti una parte qualsiasi D si muovesse, sarebbe necessario che tutte le parti di questo genere, situate da ogni parte alla stessa distanza dal centro, si muovessero insieme di un moto simile; e ciò perché la pressione di tutte è simile e uguale, e si suppone escluso ogni moto che non nasca da quella pressione. Ma esse non possono avvicinarsi tutte al centro, se il fluido non si condensa verso il centro: contro l’ipotesi. Non possono allontanarsene, se il fluido non si condensa verso la circonferenza: anche questo contro l’ipotesi. Non possono, conservando la loro distanza dal centro, muoversi verso una parte qualsiasi, perché per la stessa ragione si muoveranno verso la parte contraria; ma la stessa parte non può muoversi, nello stesso tempo, verso parti contrarie. Dunque nessuna parte del fluido si muoverà dal suo luogo. C.V.D.

**[II.S5.04]** *Caso 2.* Dico ora che tutte le parti sferiche di questo fluido sono premute ugualmente da ogni parte. Sia infatti EF una parte sferica del fluido; e, se questa non è premuta ugualmente da ogni parte, si aumenti la pressione minore finché essa sia premuta ugualmente da ogni parte: le sue parti, per il Caso 1, rimarranno nei loro luoghi. Ma prima dell’aumento della pressione rimarranno nei loro luoghi, per lo stesso Caso 1; e per l’aggiunta della nuova pressione si muoveranno dai loro luoghi, per la definizione del fluido. Le due cose si contraddicono. Era dunque falso dire che la sfera EF non era premuta ugualmente da ogni parte. C.V.D.

**[II.S5.05]** *Caso 3.* Dico inoltre che la pressione di parti sferiche diverse è uguale. Infatti le parti sferiche contigue si premono a vicenda ugualmente nel punto di contatto, per la Legge III del moto. Ma anche, per il Caso 2, sono premute da ogni parte con la stessa forza. Due parti sferiche qualsiasi non contigue, dunque, poiché una parte sferica intermedia può toccarle entrambe, saranno premute con la stessa forza. C.V.D.

**[II.S5.06]** *Caso 4.* Dico ora che tutte le parti del fluido sono premute ugualmente dovunque. Infatti due parti qualsiasi possono essere toccate da parti sferiche in punti qualsiasi, e lì premono ugualmente quelle parti sferiche, per il Caso 3, e a loro volta sono premute ugualmente da esse, per la terza legge del moto. C.V.D.

**[II.S5.07]** *Caso 5.* Poiché dunque una parte qualsiasi GHI del fluido è racchiusa nel resto del fluido come in un vaso, ed è premuta ugualmente da ogni parte, e le sue parti si premono a vicenda ugualmente e stanno in quiete fra loro, è manifesto che tutte le parti di un fluido qualsiasi GHI, che sia premuto ugualmente da ogni parte, si premono a vicenda ugualmente e stanno in quiete fra loro. C.V.D.

**[II.S5.08]** *Caso 6.* Perciò, se quel fluido è racchiuso in un vaso non rigido e non è premuto ugualmente da ogni parte, cederà alla pressione più forte, per la definizione della fluidità.

**[II.S5.09]** *Caso 7.* E perciò in un vaso rigido il fluido non sosterrà da un lato una pressione più forte che dall’altro, ma le cederà, e ciò in un istante, perché il lato rigido del vaso non insegue il liquido che cede. Cedendo, poi, premerà il lato opposto, e così la pressione tenderà da ogni parte all’uguaglianza. E poiché il fluido, non appena tende ad allontanarsi dalla parte più premuta, è trattenuto dalla resistenza del vaso dal lato opposto, la pressione sarà ricondotta da ogni parte all’uguaglianza, in un istante, senza moto locale; e quindi le parti del fluido, per il Caso 5, si premeranno a vicenda ugualmente e staranno in quiete fra loro. C.V.D.

**[II.S5.10]** *Cor.* Di qui segue che neppure i moti delle parti del fluido fra loro possono essere mutati da una pressione applicata al fluido in un punto qualsiasi della superficie esterna, se non in quanto o la figura della superficie muta in qualche punto, o tutte le parti del fluido, premendosi l’una l’altra più intensamente o più debolmente, scorrono fra loro con maggiore o minore difficoltà.

### Proposizione XX. Teorema XV (il fondo sostiene il peso di un cilindro)

**[II.S5.11]** **Se le singole parti di un fluido sferico, omogeneo a distanze uguali dal centro, che poggia su un fondo sferico concentrico, gravitano verso il centro del tutto, il fondo sostiene il peso di un cilindro la cui base è uguale alla superficie del fondo e la cui altezza è la stessa del fluido che vi poggia.**

**[II.S5.12]** Sia DHM la superficie del fondo e AEI la superficie superiore del fluido. Con innumerevoli superfici sferiche BFK, CGL si divida il fluido in gusci concentrici di uguale spessore; e immagina che la forza di gravità agisca soltanto sulla superficie superiore di ciascun guscio, e che le azioni su parti uguali di tutte le superfici siano uguali. La superficie più alta AE è dunque premuta dalla forza semplice della propria gravità, dalla quale sono premute ugualmente, in proporzione alla loro misura, sia tutte le parti del guscio più alto sia la seconda superficie BFK (per la Prop. XIX). La seconda superficie BFK è premuta inoltre dalla forza della propria gravità, che, aggiunta alla forza precedente, dà una pressione doppia. Da questa pressione, in proporzione alla sua misura, e in più dalla forza della propria gravità, cioè da una pressione tripla, è premuta la terza superficie CGL. E similmente la quarta superficie è premuta da una pressione quadrupla, la quinta da una quintupla, e così via. La pressione da cui è premuta ciascuna superficie non è dunque come la quantità solida del fluido che vi poggia, ma come il numero dei gusci fino alla sommità del fluido; ed è uguale alla gravità del guscio più basso moltiplicata per il numero dei gusci: cioè alla gravità di un solido il cui rapporto ultimo con il cilindro prima definito (purché il numero dei gusci si aumenti e lo spessore si diminuisca all’infinito, così che l’azione della gravità dalla superficie più bassa alla più alta sia resa continua) diventerà un rapporto di uguaglianza. La superficie più bassa sostiene dunque il peso del cilindro prima definito. C.V.D. E con un argomento simile la proposizione risulta evidente quando la gravità decresce in un rapporto qualsiasi assegnato della distanza dal centro, e anche quando il fluido è più rado in alto e più denso in basso. C.V.D.

**[II.S5.13]** *Cor. 1.* Il fondo, dunque, non è premuto da tutto il peso del fluido che vi poggia, ma sostiene soltanto la parte del peso descritta nella proposizione; il peso restante è sostenuto dalla figura a volta del fluido.

**[II.S5.14]** *Cor. 2.* A distanze uguali dal centro, poi, la quantità della pressione è sempre la stessa, sia che la superficie premuta sia parallela all’orizzonte, sia perpendicolare, sia obliqua; sia che il fluido, continuato verso l’alto dalla superficie premuta, si innalzi perpendicolarmente lungo una linea retta, sia che serpeggi obliquamente per cavità e canali tortuosi, regolari o del tutto irregolari, ampi o strettissimi. Che la pressione non sia mutata in nulla da queste circostanze si ricava applicando la dimostrazione di questo teorema ai singoli casi dei fluidi.

**[II.S5.15]** *Cor. 3.* Con la stessa dimostrazione si ricava anche (per la Prop. XIX) che le parti di un fluido pesante non acquistano alcun moto fra loro per la pressione del peso che vi poggia, purché si escluda il moto che nasca dalla condensazione.

**[II.S5.16]** *Cor. 4.* E perciò, se un altro corpo della stessa gravità specifica, che sia incapace di condensazione, viene immerso in questo fluido, esso non acquisterà alcun moto per la pressione del peso che vi poggia: non scenderà, non salirà, non sarà costretto a mutare la sua figura. Se è sferico rimarrà sferico, nonostante la pressione; se è quadrato rimarrà quadrato; e ciò sia che sia molle, sia che sia fluidissimo; sia che galleggi liberamente nel fluido, sia che poggi sul fondo. Ogni parte interna del fluido, infatti, sta nella condizione di un corpo immerso, e la condizione di tutti i corpi immersi della stessa grandezza, figura e gravità specifica è uguale. Se il corpo immerso, conservando il suo peso, si liquefacesse e assumesse la forma di un fluido, esso, se prima saliva o scendeva o per la pressione assumeva una figura nuova, anche ora salirebbe o scenderebbe o sarebbe costretto ad assumere una figura nuova; e ciò perché la sua gravità e le altre cause dei moti permangono. Ma (per il Caso 5 della Prop. XIX) ora starebbe in quiete e conserverebbe la sua figura. Dunque anche prima.

**[II.S5.17]** *Cor. 5.* Perciò un corpo che è specificamente più pesante del fluido a esso contiguo affonderà, e uno che è specificamente più leggero salirà, e ne seguiranno un moto e un cambiamento di figura quanto quell’eccesso o quel difetto di gravità può produrre. Infatti quell’eccesso o quel difetto ha la natura di un impulso, dal quale è sollecitato il corpo altrimenti costituito in equilibrio con le parti del fluido; e si può paragonare con l’eccesso o il difetto di peso nell’uno o nell’altro piatto di una bilancia.

**[II.S5.18]** *Cor. 6.* La gravità dei corpi posti nei fluidi è dunque duplice: l’una vera e assoluta, l’altra apparente, volgare e comparativa. La gravità assoluta è la forza totale con cui il corpo tende verso il basso; quella relativa e volgare è l’eccesso di gravità per cui il corpo tende verso il basso più del fluido circostante. Per la gravità del primo genere le parti dei fluidi e di tutti i corpi gravitano nei loro luoghi, e perciò con i loro pesi congiunti compongono il peso del tutto. Ogni tutto, infatti, è pesante, come si può sperimentare nei vasi pieni di liquidi; e il peso del tutto è uguale ai pesi di tutte le parti, e perciò è composto di essi. Per la gravità dell’altro genere i corpi non gravitano nei loro luoghi, cioè, confrontati fra loro, non prevalgono col peso, ma, impedendo a vicenda le loro tendenze a scendere, rimangono nei loro luoghi come se non fossero pesanti. Le cose che sono nell’aria e non prevalgono col peso, il volgo non le giudica pesanti. Quelle che prevalgono col peso, il volgo le giudica pesanti, in quanto non sono sostenute dal peso dell’aria. I pesi del volgo non sono altro che gli eccessi dei pesi veri sul peso dell’aria. Di qui anche il volgo chiama leggere le cose che sono meno pesanti e che, cedendo all’aria che prevale col peso, salgono verso l’alto. Sono leggere comparativamente, non veramente, perché nel vuoto scendono. Così anche nell’acqua i corpi che, per la loro gravità maggiore o minore, scendono o salgono, sono comparativamente e apparentemente pesanti o leggeri; e la loro gravità o leggerezza comparativa e apparente è l’eccesso o il difetto per cui la loro gravità vera supera la gravità dell’acqua o ne è superata. Quelli invece che né scendono prevalendo col peso, né salgono cedendo a ciò che prevale col peso, benché con i loro pesi veri accrescano il peso del tutto, comparativamente tuttavia e nel senso del volgo non gravitano nell’acqua. La dimostrazione di questi casi, infatti, è simile.

**[II.S5.19]** *Cor. 7.* Ciò che si dimostra della gravità vale per qualsiasi altra forza centripeta.

**[II.S5.20]** *Cor. 8.* Perciò, se il mezzo in cui si muove un corpo è sollecitato o dalla propria gravità o da qualsiasi altra forza centripeta, e il corpo è sollecitato dalla stessa forza più fortemente, la differenza delle forze è quella forza motrice che nelle proposizioni precedenti abbiamo considerato come forza centripeta. Se invece il corpo è sollecitato da quella forza più debolmente, la differenza delle forze deve essere considerata come forza centrifuga.

**[II.S5.21]** *Cor. 9.* Poiché poi i fluidi, premendo i corpi racchiusi, non ne mutano le figure esterne, risulta inoltre (per il corollario della Prop. XIX) che non muteranno la posizione delle parti interne fra loro; e perciò, se vi si immergono degli animali, e se ogni sensazione nasce dal moto delle parti, essi non danneggeranno i corpi immersi né susciteranno alcuna sensazione, se non in quanto questi corpi possono essere condensati dalla compressione. E la condizione è la stessa per qualsiasi sistema di corpi circondato da un fluido che lo comprime. Tutte le parti del sistema saranno agitate dagli stessi moti che se fossero poste nel vuoto e conservassero soltanto la loro gravità comparativa, se non in quanto il fluido o resista un poco ai loro moti, o sia richiesto per tenerle unite con la compressione.

### Proposizione XXI. Teorema XVI (gravità inversamente come la distanza)

**[II.S5.22]** **Sia la densità di un fluido proporzionale alla compressione, e le sue parti siano tirate verso il basso da una forza centripeta inversamente proporzionale alle loro distanze dal centro: dico che, se quelle distanze si prendono continuamente proporzionali, anche le densità del fluido a quelle stesse distanze saranno continuamente proporzionali.**

**[II.S5.23]** Rappresenti ATV il fondo sferico su cui poggia il fluido, S il centro, SA, SB, SC, SD, SE, SF ecc. distanze continuamente proporzionali. Si innalzino le perpendicolari AH, BI, CK, DL, EM, FN ecc., che stiano come le densità del mezzo nei luoghi A, B, C, D, E; e le gravità specifiche in quegli stessi luoghi staranno come AH/AS, BI/BS, CK/CS ecc., o, ciò che è lo stesso, come AH/AB, BI/BC, CK/CD ecc. Immagina dapprima che queste gravità si mantengano uniformi da A a B, da B a C, da C a D ecc., con decrementi fatti per gradi nei punti B, C, D ecc. E queste gravità, moltiplicate per le altezze AB, BC, CD ecc., daranno le pressioni AH, BI, CK ecc., dalle quali è premuto il fondo ATV (secondo il Teorema XV). La particella A sostiene dunque tutte le pressioni AH, BI, CK, DL, procedendo all’infinito; la particella B tutte tranne la prima, AH; la particella C tutte tranne le prime due, AH, BI; e così via: e perciò la densità AH della prima particella A sta alla densità BI della seconda particella B come la somma di tutte, AH + BI + CK + DL all’infinito, sta alla somma di tutte, BI + CK + DL ecc. E BI, densità della seconda B, sta a CK, densità della terza C, come la somma di tutte, BI + CK + DL ecc., sta alla somma di tutte, CK + DL ecc. Quelle somme sono dunque proporzionali alle loro differenze AH, BI, CK ecc., e perciò continuamente proporzionali (per il Lemma I di questo Libro); e quindi le differenze AH, BI, CK ecc., proporzionali alle somme, sono anch’esse continuamente proporzionali. Perciò, poiché le densità nei luoghi A, B, C ecc. stanno come AH, BI, CK ecc., anche queste saranno continuamente proporzionali. Si proceda per salti, e *ex æquo*, alle distanze SA, SC, SE continuamente proporzionali, le densità AH, CK, EM saranno continuamente proporzionali. E con lo stesso argomento, a distanze qualsiasi continuamente proporzionali SA, SD, SG, le densità AH, DL, GO saranno continuamente proporzionali. Si riuniscano ora i punti A, B, C, D, E ecc., in modo che la progressione delle gravità specifiche dal fondo A alla sommità del fluido sia resa continua; e a distanze qualsiasi continuamente proporzionali SA, SD, SG, le densità AH, DL, GO, essendo sempre continuamente proporzionali, rimarranno ancora continuamente proporzionali. C.V.D.

**[II.S5.24]** *Cor.* Di qui, se è data la densità del fluido in due luoghi, per esempio A ed E, se ne può ricavare la densità in qualsiasi altro luogo Q. Con centro S e asintoti ortogonali SQ, SX si descriva un’iperbole che tagli le perpendicolari AH, EM, QT in a, e, q, e anche le perpendicolari HX, MY, TZ, abbassate sull’asintoto SX, in h, m e t. Si faccia in modo che l’area YmtZ stia all’area data YmhX come l’area data EeqQ sta all’area data EeaA; e la linea Zt prolungata taglierà la linea QT proporzionale alla densità. Infatti, se le linee SA, SE, SQ sono continuamente proporzionali, le aree EeqQ, EeaA saranno uguali, e di qui anche le aree a esse proporzionali YmtZ, XhmY saranno uguali, e le linee SX, SY, SZ, cioè AH, EM, QT, continuamente proporzionali, come deve essere. E se le linee SA, SE, SQ occupano un altro posto qualsiasi nella serie delle continuamente proporzionali, le linee AH, EM, QT, per le aree iperboliche proporzionali, occuperanno lo stesso posto in un’altra serie di quantità continuamente proporzionali.

### Proposizione XXII. Teorema XVII (gravità inversamente come il quadrato della distanza)

**[II.S5.25]** **Sia la densità di un fluido proporzionale alla compressione, e le sue parti siano tirate verso il basso da una gravità inversamente proporzionale ai quadrati delle loro distanze dal centro: dico che, se le distanze si prendono in progressione armonica, le densità del fluido a queste distanze saranno in progressione geometrica.**

**[II.S5.26]** Rappresenti S il centro, e SA, SB, SC, SD, SE distanze in progressione geometrica. Si innalzino le perpendicolari AH, BI, CK ecc., che stiano come le densità del fluido nei luoghi A, B, C, D, E ecc.; e le sue gravità specifiche in quegli stessi luoghi saranno AH/SA², BI/SB², CK/SC² ecc. Immagina che queste gravità si mantengano uniformi, la prima da A a B, la seconda da B a C, la terza da C a D ecc. E queste, moltiplicate per le altezze AB, BC, CD, DE ecc., o, ciò che è lo stesso, per le distanze SA, SB, SC ecc., proporzionali a quelle altezze, daranno gli esponenti delle pressioni AH/SA, BI/SB, CK/SC ecc. Perciò, poiché le densità stanno come le somme di queste pressioni, le differenze delle densità AH − BI, BI − CK ecc. staranno come le differenze delle somme AH/SA, BI/SB, CK/SC ecc. Con centro S e asintoti SA, Sx si descriva un’iperbole qualsiasi, che tagli le perpendicolari AH, BI, CK ecc. in a, b, c ecc., e anche le perpendicolari Ht, Iu, Kw, abbassate sull’asintoto Sx, in h, i, k; e le differenze delle densità tu, uw ecc. staranno come AH/SA, BI/SB ecc. E i rettangoli tu × th, uw × ui ecc., ossia tp, uq ecc., staranno come AH × th/SA, BI × ui/SB ecc., cioè come Aa, Bb ecc. Infatti, per la natura dell’iperbole, SA sta ad AH, o St, come th sta ad Aa, e perciò AH × th/SA è uguale ad Aa. E con un argomento simile BI × ui/SB è uguale a Bb, ecc. Ora Aa, Bb, Cc ecc. sono continuamente proporzionali, e perciò proporzionali alle loro differenze Aa − Bb, Bb − Cc ecc.; e perciò a queste differenze sono proporzionali i rettangoli tp, uq ecc., come anche alle somme delle differenze, Aa − Cc o Aa − Dd, le somme dei rettangoli, tp + uq o tp + uq + wr. Si prendano moltissimi termini di questo genere, e la somma di tutte le differenze, per esempio Aa − Ff, sarà proporzionale alla somma di tutti i rettangoli, per esempio zthn. Si aumenti il numero dei termini e si diminuiscano le distanze dei punti A, B, C ecc. all’infinito: quei rettangoli diventeranno uguali all’area iperbolica zthn, e perciò a quest’area è proporzionale la differenza Aa − Ff. Si prendano ora distanze qualsiasi, per esempio SA, SD, SF, in progressione armonica: le differenze Aa − Dd, Dd − Ff saranno uguali; e perciò le aree thlx, xlnz, proporzionali a queste differenze, saranno uguali fra loro, e le densità St, Sx, Sz, cioè AH, DL, FN, continuamente proporzionali. C.V.D.

**[II.S5.27]** *Cor.* Di qui, se sono date due densità qualsiasi del fluido, per esempio AH e BI, sarà data l’area thiu corrispondente alla loro differenza tu; e di qui si troverà la densità FN a una altezza qualsiasi SF, prendendo l’area thnz che stia a quell’area data thiu come la differenza Aa − Ff sta alla differenza Aa − Cc [così la trascrizione; il senso richiede Aa − Bb, come in Motte: vedi A.4 e N7].

### Scolio (altre leggi della gravità e della condensazione)

**[II.S5.28]** Con un argomento simile si può provare che, se la gravità delle particelle del fluido diminuisce in rapporto triplicato delle distanze dal centro, e i reciproci dei quadrati delle distanze SA, SB, SC ecc. (cioè SA³/SA², SA³/SB², SA³/SC²) si prendono in progressione aritmetica, le densità AH, BI, CK ecc. saranno in progressione geometrica. E se la gravità diminuisce in rapporto quadruplicato delle distanze, e i reciproci dei cubi delle distanze (per esempio SA⁴/SA³, SA⁴/SB³, SA⁴/SC³ ecc.) si prendono in progressione aritmetica, le densità AH, BI, CK ecc. saranno in progressione geometrica. E così all’infinito. Di nuovo, se la gravità delle particelle del fluido è la stessa a tutte le distanze, e le distanze sono in progressione aritmetica, le densità saranno in progressione geometrica, come ha trovato l’illustre Edmond Halley. Se la gravità è come la distanza, e i quadrati delle distanze sono in progressione aritmetica, le densità saranno in progressione geometrica. E così all’infinito.

**[II.S5.29]** Queste cose stanno così quando la densità del fluido condensato dalla compressione è come la forza di compressione, o, ciò che è lo stesso, quando lo spazio occupato dal fluido è inversamente come questa forza. Si possono immaginare altre leggi di condensazione: per esempio, che il cubo della forza comprimente sia come il quadrato-quadrato della densità, ossia che il rapporto triplicato della forza sia lo stesso del rapporto quadruplicato della densità. In questo caso, se la gravità è inversamente come il quadrato della distanza dal centro, la densità sarà inversamente come il cubo della distanza. Si immagini che il cubo della forza comprimente sia come il quadrato-cubo della densità: se la gravità è inversamente come il quadrato della distanza, la densità sarà inversamente in rapporto sesquiplicato della distanza. Si immagini che la forza comprimente sia in rapporto duplicato della densità, e la gravità inversamente in rapporto duplicato della distanza: la densità sarà inversamente come la distanza. Sarebbe lungo percorrere tutti i casi. Del resto, per esperimento risulta che la densità dell’aria è come la forza comprimente, o esattamente o almeno con ottima approssimazione; e perciò la densità dell’aria nell’atmosfera della Terra è come il peso di tutta l’aria che vi sta sopra, cioè come l’altezza del mercurio nel barometro.

### Proposizione XXIII. Teorema XVIII (fluido elastico di particelle che si respingono)

**[II.S5.30]** **Se la densità di un fluido composto di particelle che si fuggono a vicenda è come la compressione, le forze centrifughe delle particelle sono inversamente proporzionali alle distanze dei loro centri. E viceversa, particelle che si fuggono a vicenda con forze inversamente proporzionali alle distanze dei loro centri compongono un fluido elastico la cui densità è proporzionale alla compressione.**

**[II.S5.31]** Si intenda che il fluido sia racchiuso nello spazio cubico ACE, e poi sia ridotto per compressione nello spazio cubico minore ace; e le distanze delle particelle che conservano fra loro una posizione simile nell’uno e nell’altro spazio staranno come i lati dei cubi AB, ab; e le densità dei mezzi inversamente come gli spazi che li contengono, AB³ e ab³. Sulla faccia piana ABCD del cubo maggiore si prenda il quadrato DP uguale alla faccia piana db del cubo minore; e, per ipotesi, la pressione con cui il quadrato DP preme il fluido racchiuso starà alla pressione con cui quel quadrato db preme il fluido racchiuso come le densità del mezzo fra loro, cioè come ab³ sta ad AB³. Ma la pressione con cui il quadrato DB preme il fluido racchiuso sta alla pressione con cui il quadrato DP preme lo stesso fluido come il quadrato DB sta al quadrato DP, cioè come AB² sta ad ab². Dunque, *ex æquo*, la pressione con cui il quadrato DB preme il fluido sta alla pressione con cui il quadrato db preme il fluido come ab sta ad AB. Con i piani FGH, fgh, condotti per il mezzo dei cubi, si divida il fluido in due parti: queste si premeranno a vicenda con le stesse forze con cui sono premute dai piani AC, ac, cioè nella proporzione di ab ad AB; e perciò le forze centrifughe, dalle quali queste pressioni sono sostenute, stanno nello stesso rapporto. Per lo stesso numero di particelle e per la loro posizione simile nell’uno e nell’altro cubo, le forze che tutte le particelle esercitano su tutte secondo i piani FGH, fgh stanno come le forze che le singole esercitano sulle singole. Dunque le forze che le singole esercitano sulle singole secondo il piano FGH nel cubo maggiore stanno alle forze che le singole esercitano sulle singole secondo il piano fgh nel cubo minore come ab sta ad AB, cioè inversamente come le distanze delle particelle fra loro. C.V.D.

**[II.S5.32]** E viceversa, se le forze delle singole particelle sono inversamente come le distanze, cioè inversamente come i lati dei cubi AB, ab, le somme delle forze staranno nello stesso rapporto, e le pressioni dei lati DB, db come le somme delle forze; e la pressione del quadrato DP starà alla pressione del lato DB come ab² sta ad AB². E, *ex æquo*, la pressione del quadrato DP starà alla pressione del lato db come ab³ sta ad AB³, cioè la forza di compressione starà alla forza di compressione come la densità sta alla densità. C.V.D.

### Scolio (altre leggi della forza fra le particelle)

**[II.S5.33]** Con un argomento simile, se le forze centrifughe delle particelle sono inversamente in rapporto duplicato delle distanze fra i centri, i cubi delle forze comprimenti staranno come i quadrato-quadrati delle densità. Se le forze centrifughe sono inversamente in rapporto triplicato o quadruplicato delle distanze, i cubi delle forze comprimenti staranno come i quadrato-cubi o i cubo-cubi delle densità. E in generale, se si pone D per la distanza ed E per la densità del fluido compresso, e le forze centrifughe sono inversamente come una potenza qualsiasi Dⁿ della distanza, il cui indice è il numero n, le forze comprimenti staranno come le radici cubiche della potenza Eⁿ⁺², il cui indice è il numero n + 2; e viceversa.

**[II.S5.34]** Tutto ciò va inteso, però, delle forze centrifughe delle particelle che terminano nelle particelle più vicine o non si diffondono molto più in là. Un esempio l’abbiamo nei corpi magnetici. La loro virtù attrattiva termina quasi nei corpi del loro genere a essi più vicini. La virtù del magnete è ristretta da una lamina di ferro interposta e termina quasi nella lamina. I corpi più lontani, infatti, non sono attratti tanto dal magnete quanto dalla lamina. Allo stesso modo, se le particelle respingono le altre particelle del loro genere a esse più vicine, ma non esercitano alcuna virtù sulle particelle più lontane, da particelle di questo genere saranno composti i fluidi di cui si è trattato in questa proposizione. Se invece la virtù di ciascuna particella si propaga all’infinito, occorrerà una forza maggiore per una condensazione uguale di una quantità maggiore di fluido. Se poi i fluidi elastici constino davvero di particelle che si respingono a vicenda è una questione fisica. Noi abbiamo dimostrato matematicamente la proprietà dei fluidi costituiti di particelle di questo genere, per offrire ai filosofi l’occasione di trattare quella questione.

**Fine della Sezione V. Nel testo originale segue la Sezione VI, *De motu & resistentia corporum Funependulorum*.**

---

## Apparato

### A.0 Estensioni del glossario

I termini seguenti non comparivano nel glossario comune né in quello del Libro II. Ognuno è reso in modo costante in tutto il fascicolo.

| Latino | Italiano | Motivazione |
|---|---|---|
| *fundum* | «fondo» | Prop. XX–XXI: la superficie sferica su cui poggia il fluido. Motte «bottom». |
| *incumbere*, *fluidum incumbens* | «poggiare su», «il fluido che vi poggia» | Evita «incombente», che in italiano ha un senso figurato. Motte «incumbent». |
| *superficies* | «superficie» | Anche quando Newton la considera premuta *pro mensura sua*. |
| *pro mensura sua* | «in proporzione alla sua misura» | Prop. XX: ogni superficie è premuta in proporzione alla propria estensione. Motte «according to its measure». |
| *orbis* (Prop. XX) | «guscio» | Resa consolidata nel Libro I per lo strato sferico; qui sono i gusci concentrici di uguale spessore. |
| *condensatio*, *condensari*; *fluiditas*; *liquor* | «condensazione», «condensarsi»; «fluidità»; «liquido» | *Liquor* (Caso 7, Cor. 6) è distinto da *fluidum*. |
| *in momento temporis*; *motus localis* | «in un istante»; «moto locale» | Caso 7. *Motus localis* è il termine scolastico per lo spostamento da luogo a luogo; lo si conserva. |
| *figura fornicata* | «figura a volta» | Cor. 1 della Prop. XX: *fornix* è la volta, l’arco murario. Motte «archwise by the spherical figure». Nota N4. |
| *specifice gravius / levius* | «specificamente più pesante / più leggero» | Cor. 5; coerente con *gravitas specifica* «gravità specifica». |
| *gravitas vera & absoluta*; *apparens, vulgaris & comparativa*; *relativa* | «gravità vera e assoluta»; «apparente, volgare e comparativa»; «relativa» | Cor. 6. «Volgare» nel senso di «del volgo», cioè dell’uso comune, come *vulgus* «il volgo»; si conserva il registro di Newton. |
| *prægravare* | «prevalere col peso» | Cor. 6: *non prægravant* «non prevalgono col peso». Motte «preponderate». |
| *levis*, *levitas* | «leggero», «leggerezza» | Cor. 6. |
| *impulsus* (Cor. 5) | «impulso» | *Rationem habet impulsus*: l’eccesso di gravità «ha la natura di un impulso» che sollecita il corpo. Si sceglie «impulso» (non «spinta») perché il glossario lo riserva all’azione che cambia la quantità di moto; qui però non è istantanea. Dubbio segnalato per l’armonizzazione. |
| *conglutinare* | «tenere unite» | Cor. 9: *ad easdem compressione conglutinandas*. Motte «conglutinate». |
| *continue proportionales*; *series continue proportionalium* | «continuamente proporzionali»; «serie delle continuamente proporzionali» | Termini della teoria delle proporzioni: progressione geometrica. Motte «continually proportional», «continued proportionals». |
| *progressio musica* | «progressione armonica» | Prop. XXII e Scolio. *Musica* è il nome antico della progressione armonica (i reciproci in progressione aritmetica). Motte «harmonic progression». Nota N7. |
| *progressio arithmetica* | «progressione aritmetica» | Scolio della Prop. XXII. |
| *ex æquo* | *ex æquo* (in corsivo, non tradotto) | Operazione delle proporzioni (Euclide V, def. 17): da A:B = D:E e B:C = E:F si conclude A:C = D:F. Motte lo lascia in latino; si fa lo stesso, con questa nota. |
| *per saltum* | «per salti» | Prop. XXI: si saltano i termini intermedi. Motte «intermissively». |
| *exponens pressionum* | «esponenti delle pressioni» | Prop. XXII: grandezze che *rappresentano* le pressioni, nel senso seicentesco già fissato nel Fascicolo 5. |
| *asymptoti rectangulæ* | «asintoti ortogonali» | Cor. della Prop. XXI; l’iperbole è equilatera. |
| *quadrato-quadratum*; *quadrato-cubus*; *cubo-cubus* | «quadrato-quadrato»; «quadrato-cubo»; «cubo-cubo» | Quarta, quinta e sesta potenza. *Quadrato-cubus* come nel Fascicolo 5. Motte «biquadrate» per la quarta. |
| *dignitas*; *index*; *latus cubicum* | «potenza»; «indice»; «radice cubica» | Scolio della Prop. XXIII. *Latus cubicum* è il «lato» del cubo, cioè la radice cubica; Motte «cube roots». |
| *vis comprimens*; *vis compressionis* | «forza comprimente»; «forza di compressione» | Tenute distinte come nel latino. |
| *particulæ se mutuo fugientes*; *fugare* | «particelle che si fuggono a vicenda»; «respingere» | Prop. XXIII: *fugere* (intransitivo con oggetto: «fuggire») è reso alla lettera nell’enunciato; *fugare* (transitivo: «mettere in fuga») nello Scolio è reso «respingere». Motte «flying each other», «repel». |
| *spatium cubicum*; *latus planum* | «spazio cubico»; «faccia piana» | Prop. XXIII. *Latus* è anche «lato» del cubo (AB, ab) e «lato» premuto (*pressio lateris DB*): nel primo senso «lato», nel secondo «lato» con il valore di faccia, come nel latino. |
| *virtus* (magnetica, attrattiva) | «virtù» | Scolio della Prop. XXIII: termine dell’epoca per la capacità di agire. Motte «virtue». |
| *magnes*; *lamina ferri* | «magnete»; «lamina di ferro» | |
| *Vir Cl. Edmundus Halleius* | «l’illustre Edmond Halley» | Nome in forma moderna; Motte «Dr. Halley». |
| *barometrum* | «barometro» | Scolio della Prop. XXII (trascrizione *baromentro*, A.8). |

*Medium* compare una volta nella Prop. XXI (*densitates medii*), dove indica il fluido stesso, e nella Prop. XXIII (*mediorum densitates*): «mezzo», secondo il glossario. *Medium similare* non compare. *Vis elastica* non compare come tale: compare *fluidum elasticum* (Prop. XXIII e Scolio), «fluido elastico». *Argentum vivum* non compare: lo Scolio della Prop. XXII ha *mercurii*, «mercurio».

### A.1 Definizione del fluido

**Latino:** *Fluidum est corpus omne, cujus partes cedunt vi cuicunque illatæ, & cedendo facile movetur inter se.*

**Inglese:** “A fluid is any body whose parts yield to any force impressed on it, by yielding, are easily moved among themselves.”

**Scelte.**

- *movetur* al singolare, con soggetto *partes*, è grammaticalmente anomalo: ci si attende *moventur*. **Refuso probabile della trascrizione** (o dell’originale), da verificare sulla stampa. La traduzione segue il senso: «si muovono».
- *vi … illatæ*: «applicata». Motte «impressed», che richiama la *vis impressa* della Def. IV; il latino usa un participio diverso (*illata*, «portata contro»), e lo si conserva distinto.
- **Omissione di Motte:** manca «and» prima di «by yielding», per cui la frase inglese è sintatticamente zoppa.

### A.2 Proposizione XIX

**Latino:** *Fluidi homogenei & immoti, quod in vase quocunque immoto clauditur & undique comprimitur, partes omnes (seposita condensationis, gravitatis, & virium omnium centripetarum consideratione) æqualiter premuntur undique, & sine omni motu a pressione illa orto permanent in locis suis.*

**Inglese:** “All the parts of a homogeneous and unmoved fluid included in any unmoved vessel, and compressed on every side (setting aside the consideration of condensation, gravity, and all centripetal forces), will be equally pressed on every side, and remain in their places without any motion arising from that pressure.”

**Scelte.**

- L’enunciato è all’indicativo nel latino (*premuntur*, *permanent*); Motte passa al futuro («will be»).
- *undique*: «da ogni parte»; *ubique* (Caso 4): «dovunque». Distinti come nel latino.
- Caso 1: *in plagam quamcunque* «verso una parte qualsiasi»; *plaga* «parte», come nei Fascicoli 3 e 5.
- Caso 1: *Atqui non possunt … nisi … condensetur* è un’affermazione di impossibilità; Motte la riformula come condizionale («But if these parts come … the fluid must be condensed»). Il senso è lo stesso.
- Caso 6: *per definitionem fluiditatis* «per la definizione della fluidità»: è la stessa definizione che apre la sezione (in Caso 2 *per definitionem fluidi*).
- Caso 7: *conatur* «tende» (*conatus* «tendenza», glossario).
- Cor.: *nisi quatenus* «se non in quanto» (glossario). *Fluido ubivis in externa superficie illatam*: «applicata al fluido in un punto qualsiasi della superficie esterna».
- **Aggiunte di Motte:** «of a yielding substance, or» (Caso 6), «inflexible or» (Caso 7), «But the fluid, by thus yielding» (Caso 7, esplicitazione del soggetto).

### A.3 Proposizione XX e corollari

**Latino:** *Si fluidi sphærici, & in æqualibus a centro distantiis homogenei, fundo sphærico concentrico incumbentis partes singulæ versus centrum totius gravitent; sustinet fundum pondus cylindri, cujus basis æqualis est superficiei fundi, & altitudo eadem quæ fluidi incumbentis.*

**Inglese:** “If all the parts of a spherical fluid, homogeneous at equal distances from the centre, lying on a spherical concentric bottom, gravitate towards the centre of the whole, the bottom will sustain the weight of a cylinder, whose base is equal to the superficies of the bottom, and whose altitude is the same with that of the incumbent fluid.”

**Scelte.**

- **Intestazione.** La trascrizione ha «Prop. XX. THEOREMA XV.» in forma abbreviata, invece di «PROPOSITIO XX. THEOREMA XV.» come le altre. Si traduce con la forma piena; da verificare sulla stampa (A.10).
- *partes singulæ* «le singole parti»; Motte «all the parts».
- *concipe* (imperativo, seconda persona) «immagina», come *Finge* nelle Propp. XXI–XXII.
- *quantitas solida* «quantità solida»: il volume (Motte «solid quantity»).
- *cylindrum præfinitum* «il cilindro prima definito» (nell’enunciato).
- *fiet ratio æqualitatis* «diventerà un rapporto di uguaglianza»: linguaggio dei rapporti ultimi del Libro I, Sezione I.
- Cor. 1: *a fluidi figura fornicata sustentato* «sostenuto dalla figura a volta del fluido». **Motte** «sustained archwise by the spherical figure of the fluid»: rende *fornicata* con un avverbio e **aggiunge** «spherical».
- Cor. 2: *surgat … vel serpit*: il secondo verbo all’indicativo, dove il parallelismo con *surgat* richiederebbe *serpat*. **Refuso probabile** (A.8). *Easque regulares vel maxime irregulares, amplas vel angustissimas*: **Motte** «regular or irregular, wide or narrow» perde i due superlativi.
- Cor. 4: *magitudinis* è **refuso probabile della trascrizione** per *magnitudinis*. *Sive molle sit, sive fluidissimum*: Motte «soft or fluid», perde il superlativo. *Rationem corporis submersi* «la condizione di un corpo immerso»; *par est ratio* «la condizione … è uguale»: *ratio* qui non è «rapporto».
- Cor. 5: *rationem habet impulsus* «ha la natura di un impulso» (A.0); Motte «is the same thing as an impulse». *In lance alterutra libræ* «nell’uno o nell’altro piatto di una bilancia»: *libra* qui è la bilancia, non l’unità di peso.
- Cor. 6: *Nam totum omne grave est* «Ogni tutto, infatti, è pesante». *Prægravanti cedendo* (ultima frase): Motte aggiunge «fluid» («the preponderating fluid»).
- Cor. 8: *consideravimus* (prima persona plurale) «abbiamo considerato»; Motte «I have considered». *Pro vi centrifuga haberi debet* «deve essere considerata come forza centrifuga»; **Motte** amplia: «becomes a centrifugal force, and is to be considered as such».
- Cor. 9: *patium* è **refuso probabile della trascrizione** per *partium*. *Circundati* è variante grafica di *circumdati*, non refuso.

### A.4 Proposizione XXI e corollario

**Latino:** *Sit fluidi cujusdam densitas compressioni proportionalis, & partes ejus a vi centripeta distantiis suis a centro reciproce proportionali deorsum trahantur: dico quod, si distantiæ illæ sumantur continue proportionales, densitates fluidi in iisdem distantiis erunt etiam continue proportionales.*

**Inglese:** “Let the density of any fluid be proportional to the compression, and its parts be attracted downwards by a centripetal force reciprocally proportional to the distances from the centre: I say, that, if those distances be taken continually proportional, the densities of the fluid at the same distances will be also continually proportional.”

**Scelte.**

- *trahantur* «siano tirate»: Motte «attracted». Si conserva il verbo concreto del latino.
- Le frazioni appiattite *AHAS, BIBS, CKCS* e *AHAB, BIBC, CKCD* sono lette AH/AS, BI/BS, CK/CS e AH/AB, BI/BC, CK/CD: la gravità specifica è il prodotto della densità (AH) per la gravità (inversamente come SA); poiché le distanze sono in progressione geometrica, AB è proporzionale a SA. La lettura è confermata dal passo successivo: (AH/AB) × AB = AH (nota N6).
- *juxta theorema XV.* «secondo il Teorema XV»: è la Prop. XX (A.11).
- *per hujus lem. I.* «per il Lemma I di questo Libro» (A.11).
- **Motte** aggiunge F all’elenco *in locis A, B, C, D, E*.
- Cor.: *Fiat area YmtZ ad aream datam YmhX ut …* è reso «Si faccia in modo che l’area YmtZ stia …». Nella frase successiva la stessa area YmhX è scritta XhmY: lettere in ordine diverso, stessa area.
- Cor.: *obtinent alium quemvis ordinem in serie* «occupano un altro posto qualsiasi nella serie»: *ordo* indica la posizione nella progressione (Motte «order»).

### A.5 Proposizione XXII e corollario

**Latino:** *Sit fluidi cujusdam densitas compressioni proportionalis, & partes ejus a gravitate quadratis distantiarum suarum a centro reciproce proportionali deorsum trahantur: dico quod, si distantiæ sumantur in progressione musica, densitates fluidi in his distantiis erunt in progressione geometrica.*

**Inglese:** “Let the density of any fluid be proportional to the compression, and its parts be attracted downwards by a gravitation reciprocally proportional to the squares of the distances from the centre: I say, that if the distances be taken in harmonic progression, the densities of the fluid at those distances will be in a geometrical progression.”

**Scelte.**

- *progressio musica* «progressione armonica» (A.0, N7).
- *specfifcæ* è **refuso probabile della trascrizione** per *specificæ*.
- Frazioni appiattite: *AHSAq* = AH/SA², *AHSA* = AH/SA, *AH×thSA* = AH × th/SA, *BI×uiSB* = BI × ui/SB. Lette dal contesto (la «natura dell’iperbole» SA × Aa = St × th dà proprio AH × th/SA = Aa).
- *Ht,Iu, Kw*: spaziatura della trascrizione.
- *Sunto ejusmodi termini quam plurimi* «Si prendano moltissimi termini di questo genere»; **Motte** «Suppose several of these terms» attenua.
- **Corollario, *ad differentiam Aa−Cc*.** L’area thiu corrisponde alla differenza tu, cioè all’intervallo fra A e B; per l’argomento della proposizione essa è proporzionale ad Aa − Bb, non ad Aa − Cc. **Motte ha «Aa − Bb».** La verifica numerica (N7) conferma che serve Aa − Bb. Poiché non so se l’errore sia della trascrizione o della stampa del 1726, la traduzione conserva «Aa − Cc» con un’integrazione tra parentesi quadre. Da controllare sulla stampa (A.10).

### A.6 Scolio della Proposizione XXII

- *SA cub.SAq, SA cub.SBq, SA cub.SCq* = SA³/SA², SA³/SB², SA³/SC²: i reciproci dei quadrati delle distanze, moltiplicati per la costante SA³ perché abbiano la dimensione di una lunghezza. *SAqqSA cub., SAqqSBcub., SAqqSCcub.* = SA⁴/SA³, SA⁴/SB³, SA⁴/SC³ (*qq* = quadrato-quadrato).
- *arithmeca* è **refuso probabile della trascrizione** per *arithmetica*; *baromentro* per *barometro*.
- *seu triplicata ratio vis eadem cum quadruplicatæ rationi densitatis*: *cum* regge l’ablativo, ci si attende *quadruplicata ratione*; il dativo *quadruplicatæ rationi* è anomalo. Probabile commistione di costrutti (*eadem cum* / *æqualis*); il senso è chiaro: «il rapporto triplicato della forza è lo stesso del rapporto quadruplicato della densità». Segnalato in A.10.
- *ut quod cubus vis comprimentis sit ut quadrato-quadratum densitatis*: «per esempio, che il cubo della forza comprimente sia come il quadrato-quadrato della densità». Motte «biquadrate».
- *Cæterum per experimenta constat* «Del resto, per esperimento risulta»; **Motte** «But as to our own air, this is certain from experiment» aggiunge «our own».
- *uti Vir Cl. Edmundus Halleius invenit*: «come ha trovato l’illustre Edmond Halley»; Motte «as Dr. Halley has found» (titolo diverso).

### A.7 Proposizione XXIII e Scolio

**Latino:** *Si fluidi ex particulis se mutuo fugientibus compositi densitas sit ut compressio, vires centrifugæ particularum sunt reciproce proportionales distantiis centrorum suorum. Et vice versa, particulæ viribus quæ sunt reciproce proportionales distantiis centrorum suorum se mutuo fugientes componunt fluidum elasticum, cujus densitas est compressioni proportionalis.*

**Inglese:** “If a fluid be composed of particles mutually flying each other, and the density be as the compression, the centrifugal forces of the particles will be reciprocally proportional to the distances of their centres. And, vice versa, particles flying each other, with forces that are reciprocally proportional to the distances of their centres, compose an elastic fluid, whose density is as the compression.”

**Scelte.**

- *vires centrifugæ* «forze centrifughe»: qui sono le forze repulsive fra particelle, non le forze centrifughe del moto circolare. Si conserva il termine del glossario e lo si spiega in N9.
- *distantiis centrorum suorum* «alle distanze dei loro centri»: le distanze fra i centri delle particelle.
- Dimostrazione: *latus planum* «faccia piana»; *quadratum DB*: la faccia intera del cubo maggiore (D e B vertici opposti della faccia ABCD); *quadratum db*: la faccia del cubo minore. *Pressio* è qui la forza totale su una faccia, non la pressione nel senso moderno (forza per unità di superficie): nota N9.
- *a planis AC, ac*: le facce premute, indicate con un’altra coppia di vertici opposti (A, C) della stessa faccia ABCD. Lettura ricostruita, da verificare sulla figura.
- *pressio lateris DB*: «la pressione del lato DB», cioè della faccia.
- **Motte** esplicita «in the one … in the other», «in the former … in the latter» nell’ultima frase della dimostrazione inversa.
- Scolio: *desitarum* è **refuso probabile della trascrizione** per *densitatum*; *laminan* per *laminam*.
- Scolio: *latera cubica dignitatis E*ⁿ⁺² «le radici cubiche della potenza Eⁿ⁺²». La trascrizione ha *Dn* ed *En+2* con gli apici appiattiti; si scrivono Dⁿ ed Eⁿ⁺².
- Scolio: *Quod si particulæ cujusque virtus in infinitum propagetur* «se invece la virtù di ciascuna particella si propaga all’infinito»; **Motte** «diffuse itself every way in infinitum» aggiunge «every way».

### A.8 Refusi e anomalie della trascrizione

| Luogo | Trascrizione | Lettura | Tipo |
|---|---|---|---|
| II.S5.01 | *facile movetur* | *moventur* | concordanza anomala (refuso probabile) |
| II.S5.04, S5.05 | *sphaericæ* accanto a *sphæricæ* | — | oscillazione grafica |
| prima di II.S5.11 | *Prop. XX. THEOREMA XV.* | *PROPOSITIO XX.* | intestazione abbreviata |
| II.S5.14 | *vel serpit* | *vel serpat* | modo verbale anomalo (refuso probabile) |
| II.S5.16 | *magitudinis* | *magnitudinis* | refuso probabile |
| II.S5.21 | *patium* | *partium* | refuso probabile |
| II.S5.23 | *AHAS*, *AHAB* ecc. | AH/AS, AH/AB | frazioni appiattite |
| II.S5.26 | *specfifcæ* | *specificæ* | refuso probabile |
| II.S5.26 | *AHSAq*, *AHSA*, *AH×thSA*, *BI×uiSB* | AH/SA², AH/SA, AH × th/SA, BI × ui/SB | frazioni appiattite |
| II.S5.26 | *Ht,Iu* | *Ht, Iu* | spaziatura |
| II.S5.27 | *Aa−Cc* | *Aa−Bb* (senso e Motte) | **errore di sostanza**, origine da accertare |
| II.S5.28 | *arithmeca* | *arithmetica* | refuso probabile |
| II.S5.28 | *SA cub.SAq*, *SAqqSBcub.* | SA³/SA², SA⁴/SB³ | frazioni appiattite e spaziatura |
| II.S5.29 | *quadruplicatæ rationi* dopo *eadem cum* | *quadruplicata ratione* | costrutto anomalo |
| II.S5.29 | *baromentro* | *barometro* | refuso probabile |
| II.S5.33 | *desitarum* | *densitatum* | refuso probabile |
| II.S5.33 | *Dn*, *En+2* | Dⁿ, Eⁿ⁺² | apici appiattiti |
| II.S5.34 | *laminan* | *laminam* | refuso probabile |

La traduzione segue il senso; la Parte B riporta il latino esatto della trascrizione, compresi i refusi e le parole spezzate dai marcatori di pagina (*con densetur*, *propor tionales*, *pressio num*).

### A.9 SVG di Motte 1846: verificate

Controllate sul LaTeX delle immagini dell’EPUB (`/home/claude/src_epub/svg_tex.tsv`) nella rifinitura dell’8 novembre 2026. Tutte coincidono con la lettura del latino: nessuna passa nella tabella degli errori di Motte (§ A.12).

| SVG | Luogo | Atteso dal latino | Motte 1846 (EPUB) | Esito |
|---|---|---|---|---|
| 600, 601, 602 | Prop. XXI, gravità specifiche | AH/AS, BI/BS, CK/CS | AH/AS, BI/BS, CK/CS | verificata |
| 603, 604, 605 | Prop. XXI, «or, which is all one» | AH/AB, BI/BC, CK/CD | AH/AB, BI/BC, CK/CD | verificata |
| 606, 607, 608 | Prop. XXII, gravità specifiche | AH/SA², BI/SB², CK/SC² | AH/SA², BI/SB², CK/SC² | verificata |
| 609, 610, 611 | Prop. XXII, esponenti delle pressioni (tre occorrenze) | AH/SA, BI/SB, CK/SC | AH/SA, BI/SB, CK/SC | verificata |
| 612, 613 | Prop. XXII, rettangoli tp, uq | AH × th/SA, BI × ui/SB | AH × th/SA, BI × ui/SB | verificata |
| 614 | Prop. XXII, «by a like reasoning» | BI × ui/SB | BI × ui/SB (stessa formula di 613, come nel latino) | verificata |
| 615 | Scolio della Prop. XXII | SA³/SA², SA³/SB², SA³/SC² | «namely» SA³/SA², SA³/SB², SA³/SC² | verificata |
| 616 | Scolio della Prop. XXII | SA⁴/SA³, SA⁴/SB³, SA⁴/SC³ | «as» SA⁴/SA³, SA⁴/SB³, SA⁴/SC³, &c. | verificata |
| 617 | Scolio della Prop. XXIII | Eⁿ⁺² | Eⁿ⁺² | verificata |

In tutto **18 immagini** (600–617), tutte verificate. Le letture delle frazioni appiattite della trascrizione (§ A.8) sono così confermate anche da Motte. Nell’estratto di Motte gli esponenti della Prop. XXIII compaiono appiattiti come testo («AB3», «ab2»): vanno letti AB³, ab².

### A.10 Punti da controllare sulla stampa ECCO

| Pagina 1726 | Trascrizione | Lettura attesa | Motivo |
|---|---|---|---|
| p. 282 | *facile movetur* | *moventur* | concordanza con *partes* |
| p. 284 | *Prop. XX. THEOREMA XV.* | *PROPOSITIO XX. THEOREMA XV.* | intestazione abbreviata, unica nella sezione |
| p. 285 | *vel serpit* | *vel serpat* | parallelismo con *surgat* |
| p. 286 | *magitudinis* | *magnitudinis* | refuso |
| p. 287 | *patium* | *partium* | refuso |
| p. 289 | *specfifcæ* | *specificæ* | refuso |
| p. 291 | *ad differentiam Aa−Cc* | *Aa−Bb* | errore di sostanza: stabilire se è della stampa o della trascrizione; Motte ha Bb |
| p. 291 | *arithmeca* | *arithmetica* | refuso |
| p. 291 | *quadruplicatæ rationi* | *quadruplicata ratione* | costrutto |
| p. 292 | *baromentro* | *barometro* | refuso |
| p. 293 | *desitarum* | *densitatum* | refuso |
| p. 294 | *laminan* | *laminam* | refuso |

Le pagine di p. 291–292 sono attribuite secondo i marcatori ‹291› e ‹292› della trascrizione.

### A.11 Rimandi verificati

| Luogo | Latino | Resa | Esito |
|---|---|---|---|
| II.S5.05, II.S5.06 | *per motus legem III*, *per motus legem tertiam* | «per la Legge III del moto», «per la terza legge del moto» | regge (Fascicolo 3, L05: azione e reazione uguali e contrarie) |
| II.S5.12, II.S5.15 | *per prop. XIX.* | «per la Prop. XIX» | regge |
| II.S5.16 | *per cas. 5. prop. XIX.* | «per il Caso 5 della Prop. XIX» | regge (parte qualsiasi premuta ugualmente sta in quiete) |
| II.S5.21 | *per corollarium prop. XIX.* | «per il corollario della Prop. XIX» | regge (II.S5.10) |
| II.S5.23 | *juxta theorema XV.* | «secondo il Teorema XV» | regge: è la Prop. XX (pressione sul fondo = peso del cilindro) |
| II.S5.23 | *per hujus lem. I.* | «per il Lemma I di questo Libro» | regge: Libro II, Lemma I (Sezione I, `latino-1726-L2-S01.md`): *Quantitates differentiis suis proportionales sunt continue proportionales* |
| II.S5.20 | *in præcedentibus propositionibus* | «nelle proposizioni precedenti» | rimando generico, senza numero: le forze centripete del Libro I e delle Sezioni I–IV del Libro II; non verificabile puntualmente |

**Rimandi al Libro I con numero: nessuno.** Gli unici rimandi a testi fuori dal Libro II sono alla Legge III (Fascicolo 3).

### A.12 Riepilogo: dove Motte aggiunge, omette o sbaglia

| Luogo | Latino | Motte 1846 | Tipo |
|---|---|---|---|
| II.S5.01 | *& cedendo* | «by yielding» (senza «and») | omissione; sintassi zoppa |
| II.S5.01 | *illatæ* | «impressed» | termine non equivalente |
| II.S5.02 | *premuntur … permanent* | «will be … pressed», «remain» | tempo verbale |
| II.S5.08 | *in vase non rigido* | «in a vessel of a yielding substance, or that is not rigid» | aggiunta |
| II.S5.09 | *in vase rigido* | «in an inflexible or rigid vessel» | aggiunta |
| II.S5.11 | *partes singulæ* | «all the parts» | lieve divergenza |
| II.S5.12 | *ubi gravitas decrescit* | «where the gravity **of the fluid** decreases» | aggiunta |
| II.S5.13 | *a fluidi figura fornicata* | «archwise by the **spherical** figure» | aggiunta |
| II.S5.14 | *maxime irregulares … angustissimas* | «irregular … narrow» | perde i superlativi |
| II.S5.16 | *sive fluidissimum* | «or fluid» | perde il superlativo |
| II.S5.17 | *rationem habet impulsus* | «is the same thing as an impulse» | parafrasi |
| II.S5.18 | *prægravanti cedendo* (ultima frase) | «yielding to the preponderating **fluid**» | aggiunta |
| II.S5.20 | *consideravimus* | «I have considered» | persona |
| II.S5.20 | *pro vi centrifuga haberi debet* | «becomes a centrifugal force, and is to be considered as such» | ampliamento |
| II.S5.23 | *in locis A, B, C, D, E* | «A, B, C, D, E, **F**» | aggiunta |
| II.S5.23 | *per saltum* | «intermissively» | resa lessicale |
| II.S5.26 | *gravitates … erunt AHSAq* | «will be **as**» | esplicitazione |
| II.S5.26 | *quam plurimi* | «several» | attenuazione |
| II.S5.27 | *Aa−Cc* | «Aa − Bb» | **Motte ha la lettura corretta** |
| II.S5.28 | *Vir Cl.* | «Dr.» | titolo diverso |
| II.S5.29 | *quadrato-quadratum* | «biquadrate» | resa lessicale |
| II.S5.29 | *per experimenta constat* | «as to **our own** air, this is certain» | aggiunta |
| II.S5.32 | *vis compressionis ad vim compressionis ut densitas ad densitatem* | «in the one … in the other … in the former … in the latter» | esplicitazione |
| II.S5.34 | *in infinitum propagetur* | «diffuse itself **every way** in infinitum» | aggiunta |

Le 18 formule SVG di Motte (600–617) sono state verificate sul LaTeX dell’EPUB e coincidono tutte con il latino (A.9).

---

## Note editoriali e fisiche

Queste note sono aggiunte del presente fascicolo, non affermazioni tradotte da Newton. Le verifiche numeriche sono state eseguite con uno script Python (`tmp/16-L2-S5/verifica.py`): per ogni legge della gravità e della compressione, il profilo di densità è ottenuto integrando numericamente l’equilibrio idrostatico (d*p*/d*r* = −ρ *g*(*r*)), senza usare il risultato da verificare. La sezione non contiene tabelle numeriche.

### N1. La definizione di fluido

Newton definisce il fluido per la facilità con cui le parti cedono a *qualsiasi* forza, anche piccola. In termini moderni è la proprietà per cui un fluido in quiete non sostiene sforzi di taglio: ogni forza tangenziale, per quanto piccola, mette le parti in moto relativo. La definizione è usata in modo essenziale nei Casi 2 e 6 della Prop. XIX.

### N2. Prop. XIX: la pressione è la stessa in ogni direzione

La proposizione stabilisce, per un fluido senza peso compresso in un vaso, che la pressione è uniforme e isotropa: è il contenuto di ciò che oggi si chiama principio di Pascal (non verificato sulle fonti allegate, quanto all’attribuzione). L’argomento del Caso 1 è di simmetria: in un vaso sferico compresso uniformemente, ogni moto possibile è radiale (escluso perché richiederebbe condensazione) o tangenziale (escluso perché non ha un verso privilegiato). I Casi 2–5 estendono il risultato a parti qualsiasi, i Casi 6–7 a vasi di forma qualsiasi. Il Corollario anticipa che la sola pressione esterna non altera i moti relativi interni, salvo che per l’attrito interno (*difficilius vel facilius labuntur*), cioè quella che oggi è la viscosità.

### N3. Prop. XX: il fondo e il cilindro

Con gravità uniforme e fluido omogeneo, la pressione a profondità *h* è ρ*gh*, e la forza sul fondo di area *S* è ρ*gSh*: il peso di un cilindro di base *S* e altezza *h*. Per un guscio sferico di raggi *R*₀ (fondo) e *R*₁, il cilindro ha volume 4π*R*₀²(*R*₁ − *R*₀), minore del volume del guscio: con *R*₀ = 1, *R*₁ = 1,3 il rapporto cilindro/guscio vale 0,752. Il resto del peso è sostenuto «dalla figura a volta» (Cor. 1).

La costruzione discreta di Newton (gravità concentrata sulla superficie superiore di ciascun guscio, pressione = gravità del guscio infimo × numero dei gusci) converge al cilindro: con *n* = 10, 100, 1000 gusci il rapporto con il cilindro vale 1,030; 1,0030; 1,0003. Il «rapporto ultimo di uguaglianza» è confermato.

### N4. Corollari 1–5 della Prop. XX: volta, paradosso idrostatico, Archimede

- Cor. 1: l’immagine della volta (*fornix*) indica che le parti laterali del guscio si sostengono a vicenda come i conci di un arco.
- Cor. 2: la pressione dipende soltanto dalla distanza dal centro, non dalla forma dei canali: è il cosiddetto paradosso idrostatico (non verificato sulle fonti allegate, quanto al nome).
- Cor. 4–5: un corpo della stessa gravità specifica del fluido è in equilibrio indifferente; uno più pesante affonda, uno più leggero sale, con la forza che oggi si esprime come differenza fra peso e spinta di Archimede. L’argomento del Cor. 4 è di sostituzione: si immagina che il corpo si liquefi conservando il peso; per la Prop. XIX starebbe in quiete; dunque stava in quiete anche prima.

### N5. Corollari 6–9: gravità assoluta e gravità apparente

Il Cor. 6 distingue il peso vero (assoluto) dal peso apparente (il peso meno la spinta del fluido). I «pesi del volgo» sono pesi apparenti nell’aria. Il Cor. 8 collega la sezione al resto del Libro II: in un mezzo pesante la forza che muove un corpo è la differenza fra la forza sul corpo e quella sul mezzo spostato; se è negativa, va trattata come forza centrifuga. Il Cor. 9 (gli animali immersi non soffrono la pressione) è coerente con l’esperienza dei pesci e dei palombari, ma Newton lo deduce soltanto dalla Prop. XIX, con la riserva della compressibilità dei corpi.

### N6. Prop. XXI: gravità come 1/*r* e il suo corollario

Equilibrio: d*p*/d*r* = −*k* ρ/*r*, con ρ ∝ *p*. Ne segue d(ln ρ)/d(ln *r*) = costante, cioè ρ ∝ *r*^(−*c*): densità in progressione geometrica quando le distanze lo sono. Verifica numerica (integrazione dell’equilibrio con *r* = 1; 1,5; 2,25; 3,375): rapporti successivi delle densità 0,444444…, uguali fino a 10⁻¹¹.

**Lettura delle gravità specifiche.** AH/AS è densità per gravità (∝ 1/SA). Poiché SA, SB, SC sono in progressione geometrica, AB = SB − SA è proporzionale a SA, e AH/AS sta come AH/AB. Moltiplicando per l’altezza AB si ottiene AH: la pressione di ciascun gradino è proporzionale alla densità del gradino stesso, e per il Lemma I del Libro II la successione è geometrica.

**Corollario.** L’iperbole equilatera di asintoti SQ, SX dà aree proporzionali ai logaritmi dei rapporti delle ascisse: area EeqQ ∝ ln(SQ/SE), area YmtZ ∝ ln(SZ/SY) = ln(QT/EM). La costruzione impone ln(QT/EM) : ln(EM/AH) = ln(SQ/SE) : ln(SE/SA), che è esattamente la legge ρ ∝ *r*^(−*c*). Verifica con SA = 1, SE = 2, SQ = 5: primo membro 1,3219280949, secondo 1,3219280949.

### N7. Prop. XXII: gravità come 1/*r*² e la progressione armonica

Equilibrio: d*p*/d*r* = −*k* ρ/*r*², ρ ∝ *p*. Ne segue ln ρ = *C* + *K*/*r*: la densità è in progressione geometrica quando 1/*r* è in progressione aritmetica, cioè quando *r* è in progressione armonica (*musica*). Verifica numerica con 1/*r* = 1; 0,85; 0,70; 0,55: rapporti successivi delle densità 0,7408182, costanti.

Nella costruzione, Aa = *c*/SA (iperbole di asintoti SA, Sx), quindi Aa − Dd = *c*(1/SA − 1/SD): differenze uguali per distanze in progressione armonica. L’area iperbolica sull’asintoto Sx fra le altezze St e Sz è proporzionale a ln(St/Sz), cioè al logaritmo del rapporto delle densità.

**Corollario (Aa − Cc o Aa − Bb?).** Con SA = 1, SB = 1,4, SC = 1,96, SF = 3: area thnz / area thiu = 2,33333; (Aa − Ff)/(Aa − Bb) = 2,33333; (Aa − Ff)/(Aa − Cc) = 1,36111. Il testo è coerente solo con **Aa − Bb**, come in Motte. Il «Cc» della trascrizione è un errore (A.5, A.10).

### N8. Scolio della Prop. XXII: altre leggi

- Gravità ∝ 1/*r*^*m*, con ρ ∝ *p*: ln ρ = *C* + *K*/*r*^(*m*−1) per *m* ≠ 1. Per *m* = 3 la progressione aritmetica va presa sui 1/*r*², per *m* = 4 sui 1/*r*³; per gravità uniforme (*m* = 0) sulle distanze stesse; per gravità ∝ *r* (*m* = −1) sui quadrati. Tutti e quattro i casi verificati numericamente: rapporti successivi delle densità costanti fino a 10⁻¹⁰.
- Il caso della gravità uniforme è l’atmosfera isoterma, con densità che decresce esponenzialmente con l’altezza; Newton lo attribuisce a Halley. (Che Halley l’abbia pubblicato nelle *Philosophical Transactions* del 1686: non verificato sulle fonti allegate.)
- **Altre leggi di condensazione** (*p*³ ∝ ρ⁴, *p*³ ∝ ρ⁵, *p* ∝ ρ²) con gravità ∝ 1/*r*²: le soluzioni ρ ∝ *r*⁻³, *r*^(−3/2), *r*⁻¹ soddisfano esattamente l’equilibrio (verifica analitica nello script: il coefficiente risulta costante, 4; 2,5; 2). Ma l’integrazione dà in generale ρ^(*q*−1) = *A*/*r* + *B*: le leggi di potenza di Newton corrispondono al caso particolare *B* = 0, cioè a una densità che si annulla all’infinito. Newton non lo dice; è una condizione implicita nella sua affermazione.
- L’ultima frase è la legge di Boyle (oggi Boyle–Mariotte; nomi non presenti nelle fonti allegate) applicata all’atmosfera: la densità a un’altezza data è come il peso dell’aria sovrastante, misurato dal barometro.

### N9. Prop. XXIII: un modello particellare della legge di Boyle

Newton suppone particelle che si respingono con forza *f* e che agiscono soltanto sulle vicine. Nella compressione da lato AB a lato ab le posizioni restano simili, il numero di coppie a cavallo del piano mediano resta lo stesso, e la forza totale su una faccia è proporzionale a *f*. Se la «pressione» (qui: la forza su un quadrato di area data) è come la densità, la forza totale su una faccia sta come (AB²/ab²) × (ab³/AB³) = ab/AB, e quindi *f* ∝ 1/distanza. Verifica: AB = 1, ab = 0,6 dà rapporto 0,6 = ab/AB.

Le «forze centrifughe» sono qui forze repulsive fra particelle: il termine indica la direzione (via dal centro della particella), non il moto circolare. La teoria cinetica dei gas, che spiega la pressione con gli urti delle molecole e non con repulsioni statiche, è posteriore (non verificato sulle fonti allegate). Newton stesso, nello Scolio, presenta il modello come proprietà matematica e lascia aperta la «questione fisica».

### N10. Scolio della Prop. XXIII: la legge generale

Con *f* ∝ D^(−*n*) e densità E ∝ D⁻³, la forza su una faccia di area data è *f*/D² ∝ D^(−*n*−2) ∝ E^((*n*+2)/3): la forza comprimente è come la radice cubica di Eⁿ⁺². Per *n* = 1, 2, 3, 4 lo script dà esponenti 1, 4/3, 5/3, 2: cioè forza ∝ E; cubo della forza ∝ E⁴ (quadrato-quadrato); ∝ E⁵ (quadrato-cubo); ∝ E⁶ (cubo-cubo), come nel testo. La condizione che le forze agiscano solo fra particelle vicine è essenziale: con forze a lungo raggio l’argomento della similitudine non regge, come Newton osserva («occorrerà una forza maggiore … di una quantità maggiore di fluido»). L’analogia magnetica (la lamina di ferro che «ferma» la virtù del magnete) illustra un’azione che termina nelle particelle più vicine.

---

## Controllo della copertura

Pagine 1726 dai marcatori ‹n› della trascrizione; Motte: sezione corrispondente (nessun marcatore di pagina nell’estratto).

| Identificatori | Incipit latino | Contenuto | 1726 | Motte 1846 |
|---|---|---|---|---|
| II.S5.01 | *Fluidum est corpus omne* | Definizione del fluido | p. 282 | sezione corrispondente |
| II.S5.02–II.S5.03 | *Fluidi homogenei & immoti* … *In vase sphærico ABC* | Prop. XIX, enunciato, Caso 1 | pp. 282–283 | id. |
| II.S5.04–II.S5.08 | *Dico jam, quod fluidi hujus* … *Igitur si fluidum illud* | Prop. XIX, Casi 2–6 | p. 283 | id. |
| II.S5.09–II.S5.10 | *Ideoque in vase rigido* … *Unde nec motus partium* | Prop. XIX, Caso 7, Cor. | pp. 283–284 | id. |
| II.S5.11–II.S5.12 | *Si fluidi sphærici* … *Sit DHM superficies fundi* | Prop. XX, enunciato e dimostrazione | pp. 284–285 | id. |
| II.S5.13–II.S5.16 | *Igitur fundum non urgetur* … *Et propterea si aliud* | Prop. XX, Cor. 1–4 | pp. 285–286 | id. |
| II.S5.17–II.S5.18 | *Proinde corpus quod specifice gravius* … *Corporum igitur in fluidis* | Prop. XX, Cor. 5–6 | pp. 286–287 | id. |
| II.S5.19–II.S5.21 | *Quæ de gravitate demonstrantur* … *Cum autem fluida premendo* | Prop. XX, Cor. 7–9 | p. 287 | id. |
| II.S5.22–II.S5.24 | *Sit fluidi cujusdam densitas* … *Hinc si detur densitas* | Prop. XXI e Cor. | pp. 287–289 | id. |
| II.S5.25–II.S5.27 | *Sit fluidi cujusdam densitas* … *Hinc si dentur fluidi densitates* | Prop. XXII e Cor. | pp. 289–291 | id. |
| II.S5.28–II.S5.29 | *Simili argumentatione probari potest* … *Hæc ita se habent* | Scolio della Prop. XXII | pp. 291–292 | id. |
| II.S5.30–II.S5.32 | *Si fluidi ex particulis* … *Et vice versa* | Prop. XXIII, enunciato, dimostrazione e inversa | pp. 292–293 | id. |
| II.S5.33–II.S5.34 | *Simili argumento* … *Intelligenda vero sunt* | Scolio della Prop. XXIII | pp. 293–294 | id. |

**Controlli eseguiti.**

1. **Copertura frase per frase.** Ho riletto in sequenza ogni periodo della trascrizione, dal titolo *De densitate & compressione fluidorum* all’ultima frase, *ut philosophis ansam præbeamus quæstionem illam tractandi*, contro la traduzione: nessuna frase manca. Dove il latino ha un periodo lungo (Cor. 2 della Prop. XX, Caso 5 della Prop. XIX), l’italiano conserva un solo periodo o lo divide senza omettere membri. I 34 identificatori sono consecutivi e unici (controllo automatico).
2. **Parte B.** `check.py` sul file finale: JSON valido, 6 unità, 68 passi; tutte le stringhe `la` ed `en` (enunciati e passi) sono sottostringhe esatte delle fonti; ogni identificatore di `copertura` è presente nel testo.
3. **Matematica.** Verifiche numeriche per le Propp. XX (cilindro e limite dei gusci), XXI e Cor., XXII e Cor. (con la scelta fra Aa − Bb e Aa − Cc), Scolio della XXII (sette leggi), XXIII e Scolio (quattro esponenti). Tutti i risultati di Newton risultano corretti, salvo il «Cc» del Cor. della Prop. XXII (N7) e la condizione implicita sulle leggi di potenza dello Scolio (N8). Nessuna tabella numerica nella sezione.
4. **Motte.** Confronto di tutta la sezione corrispondente; divergenze nel § A.12. Le 18 formule SVG (600–617) sono state verificate sul LaTeX dell’EPUB: tutte coincidono con il latino (§ A.9).
5. **Separazione fra testo e commento.** Il testo tradotto non contiene formule moderne; l’unica integrazione tra parentesi quadre è in II.S5.27.

**Non ho potuto verificare:**

- **la stampa del 1726** (scansione ECCO): nessuno dei punti del § A.10 è stato controllato, in particolare l’origine del «Cc» in II.S5.27;
- **le figure originali** NATP00088-38…43: la disposizione dei punti (in particolare i vertici D, P, B nella faccia ABCD della Prop. XXIII e le facce indicate con AC, ac) è ricostruita dal testo;
- **la paginazione di Motte 1846** (l’estratto non ha marcatori di pagina); le formule SVG sono invece verificate (A.9);
- **Motte 1729**, per stabilire se la lezione «Aa − Bb» è già nella prima edizione inglese.

---

## Registro del lavoro successivo

| Unità | Stato |
|---|---|
| Libro II, Sezione V (Definizione, Propp. XIX–XXIII, due Scolii) | **Fascicolo 16, presente documento, prima versione** |
| Cor. della Prop. XXII, *Aa−Cc* | **Da decidere** dopo il controllo sulla stampa 1726: se la stampa ha Bb, correggere la traduzione e togliere l’integrazione; se ha Cc, tenere l’integrazione e la nota |
| Refusi della trascrizione (A.8, A.10) | Da verificare sulla stampa del 1726 |
| SVG 600–617 | **Verificate** sul LaTeX dell’EPUB: tutte coincidono con il latino (A.9) |
| *impulsus* nel Cor. 5 della Prop. XX | Da armonizzare con il glossario (A.0) |
| *progressio musica* «progressione armonica»; *ex æquo* non tradotto | Proposte per tutto il Libro II |
| Figure NATP00088-38…43 | Da consultare per confermare `figura_base` |
| Pagine interattive | Parte B: 6 unità, 68 passi; la Prop. XXII ha la figura più complessa (circa 30 punti) e andrà costruita per strati |
| Revisione filologica e scientifica indipendente | Da eseguire |

Il presente testo è una nuova traduzione assistita da IA. Non riproduce traduzioni italiane o inglesi moderne. **Licenza prevista** (decisione del curatore, Fascicolo 3): testi e traduzioni CC BY-SA 4.0, codice MIT. La trascrizione latina è © The Newton Project; i testi di Motte sono di pubblico dominio.

---

## Parte B — Dati per le pagine interattive

Unità incluse: le proposizioni con figura e dimostrazione propria (Propp. XIX, XX, XXI, XXII, XXIII) e il Corollario della Prop. XXI, che ha una figura e una dimostrazione proprie ([FIG 41]). **Esclusi**: la Definizione (senza dimostrazione), il Corollario della Prop. XIX e i Cor. 1–9 della Prop. XX (senza figura propria), il Corollario della Prop. XXII (una costruzione sulla figura della proposizione, senza dimostrazione propria), i due Scolii (senza figura).

Convenzioni:

- `la`: testo latino esatto della trascrizione, refusi e frazioni appiattite compresi; le parole spezzate dai marcatori di pagina compaiono con uno spazio (*con densetur*, *propor tionales*, *pressio num*), perché lo strumento di controllo riduce i marcatori a uno spazio;
- `it`: la traduzione di questo fascicolo;
- `en`: Motte 1846, allineato per senso, con i marcatori `[SVG n]` conservati (ignorati dallo strumento di controllo); le formule corrispondenti sono verificate nel § A.9;
- `dipende_da`: soltanto i rimandi citati nella frase latina;
- `figura.mostra`: elementi da rendere visibili, cumulativi; `figura.evidenzia`: relazioni da mettere in risalto.

```json
{
 "fascicolo": "16-L2-S5",
 "versione": "0.1",
 "data": "2026-11-08",
 "convenzioni": {
  "dipende_da": "solo rimandi citati esplicitamente nella frase latina",
  "en": "Motte 1846, allineato per senso; le formule stampate come immagini compaiono come [SVG n] (verificate sul LaTeX dell’EPUB: tutte coincidono con il latino, § A.9)",
  "figura.mostra": "elementi da rendere visibili al passo, cumulativi salvo indicazione",
  "la": ""
 },
 "unita": [
  {
   "id": "L2-P19",
   "tipo": "Propositio/Theorema",
   "titolo": "Prop. XIX — pressione uguale in ogni direzione in un fluido in quiete",
   "copertura": [
    "II.S5.02",
    "II.S5.03",
    "II.S5.04",
    "II.S5.05",
    "II.S5.06",
    "II.S5.07",
    "II.S5.08",
    "II.S5.09"
   ],
   "fonti": {
    "la": "",
    "en": "Motte 1846, sezione corrispondente"
   },
   "enunciato": {
    "la": "",
    "it": "Tutte le parti di un fluido omogeneo e immoto, che sia racchiuso in un vaso immoto qualsiasi e compresso da ogni parte, sono premute ugualmente da ogni parte (messa da parte la considerazione della condensazione, della gravità e di tutte le forze centripete) e rimangono nei loro luoghi senza alcun moto nato da quella pressione.",
    "en": "All the parts of a homogeneous and unmoved fluid included in any unmoved vessel, and compressed on every side (setting aside the consideration of condensation, gravity, and all centripetal forces), will be equally pressed on every side, and remain in their places without any motion arising from that pressure."
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
     "I"
    ],
    "vincoli": [
     "ABC vaso sferico (cerchio) di centro dato",
     "D parte del fluido a distanza qualsiasi dal centro",
     "EF parte sferica del fluido (sfera interna)",
     "GHI parte qualsiasi del fluido, di forma qualsiasi"
    ]
   },
   "passi": [
    {
     "id": "L2-P19-p1",
     "la": "",
     "it": "Caso 1. Nel vaso sferico ABC sia racchiuso un fluido e sia compresso uniformemente da ogni parte: dico che nessuna sua parte si muoverà per effetto di quella pressione.",
     "en": "CASE 1. Let a fluid be included in the spherical vessel ABC, and uniformly compressed on every side: I say, that no part of it will be moved by that pressure.",
     "dipende_da": [],
     "figura": {
      "mostra": [
       "vaso sferico ABC",
       "centro",
       "frecce di pressione uniformi sul contorno"
      ],
      "evidenzia": [
       "compressione uniforme"
      ]
     },
     "nota": "Nel latino il marcatore [FIG 38] cade dopo claudatur ed è ignorato dal controllo."
    },
    {
     "id": "L2-P19-p2",
     "la": "",
     "it": "Se infatti una parte qualsiasi D si muovesse, sarebbe necessario che tutte le parti di questo genere, situate da ogni parte alla stessa distanza dal centro, si muovessero insieme di un moto simile; e ciò perché la pressione di tutte è simile e uguale, e si suppone escluso ogni moto che non nasca da quella pressione.",
     "en": "For if any part, as D, be moved, all such parts at the same distance from the centre on every side must necessarily be moved at the same time by a like motion; because the pressure of them all is similar and equal; and all other motion is excluded that does not arise from that pressure.",
     "dipende_da": [],
     "figura": {
      "mostra": [
       "parte D",
       "sfera concentrica per D (tutte le parti alla stessa distanza)"
      ],
      "evidenzia": [
       "simmetria sferica"
      ]
     }
    },
    {
     "id": "L2-P19-p3",
     "la": "",
     "it": "Ma esse non possono avvicinarsi tutte al centro, se il fluido non si condensa verso il centro: contro l’ipotesi.",
     "en": "But if these parts come all of them nearer to the centre, the fluid must be condensed towards the centre, contrary to the supposition.",
     "dipende_da": [],
     "figura": {
      "mostra": [
       "spostamento radiale verso il centro (ipotetico)"
      ],
      "evidenzia": [
       "condensazione esclusa"
      ]
     },
     "nota": "Nel latino il marcatore di pagina <283> spezza con|densetur; il controllo lo riduce a uno spazio, perciò la stringa ha «con densetur»."
    },
    {
     "id": "L2-P19-p4",
     "la": "",
     "it": "Non possono allontanarsene, se il fluido non si condensa verso la circonferenza: anche questo contro l’ipotesi.",
     "en": "If they recede from it, the fluid must be condensed towards the circumference; which is also contrary to the supposition.",
     "dipende_da": [],
     "figura": {
      "mostra": [
       "spostamento radiale verso la circonferenza (ipotetico)"
      ]
     }
    },
    {
     "id": "L2-P19-p5",
     "la": "",
     "it": "Non possono, conservando la loro distanza dal centro, muoversi verso una parte qualsiasi, perché per la stessa ragione si muoveranno verso la parte contraria; ma la stessa parte non può muoversi, nello stesso tempo, verso parti contrarie.",
     "en": "Neither can they move in any one direction retaining their distance from the centre, because for the same reason, they may move in a contrary direction; but the same part cannot be moved contrary ways at the same time.",
     "dipende_da": [],
     "figura": {
      "mostra": [
       "spostamento tangenziale in due versi opposti (ipotetico)"
      ]
     }
    },
    {
     "id": "L2-P19-p6",
     "la": "",
     "it": "Dunque nessuna parte del fluido si muoverà dal suo luogo. C.V.D.",
     "en": "Therefore no part of the fluid will be moved from its place.",
     "dipende_da": [],
     "figura": {
      "mostra": [
       "D in quiete"
      ]
     }
    },
    {
     "id": "L2-P19-p7",
     "la": "",
     "it": "Caso 2. Dico ora che tutte le parti sferiche di questo fluido sono premute ugualmente da ogni parte.",
     "en": "CASE 2. I say now, that all the spherical parts of this fluid are equally pressed on every side.",
     "dipende_da": [],
     "figura": {
      "mostra": [
       "parte sferica EF"
      ]
     },
     "nota": "La trascrizione alterna sphaericæ e sphæricæ."
    },
    {
     "id": "L2-P19-p8",
     "la": "",
     "it": "Sia infatti EF una parte sferica del fluido; e, se questa non è premuta ugualmente da ogni parte, si aumenti la pressione minore finché essa sia premuta ugualmente da ogni parte: le sue parti, per il Caso 1, rimarranno nei loro luoghi.",
     "en": "For let EF be a spherical part of the fluid; if this be not pressed equally on every side, augment the lesser pressure till it be pressed equally on every side; and its parts (by Case 1) will remain in their places.",
     "dipende_da": [
      "Prop. XIX, Caso 1"
     ],
     "figura": {
      "mostra": [
       "pressioni disuguali su EF",
       "aumento della pressione minore"
      ]
     }
    },
    {
     "id": "L2-P19-p9",
     "la": "",
     "it": "Ma prima dell’aumento della pressione rimarranno nei loro luoghi, per lo stesso Caso 1; e per l’aggiunta della nuova pressione si muoveranno dai loro luoghi, per la definizione del fluido.",
     "en": "But before the increase of the pressure, they would remain in their places (by Case 1); and by the addition of a new pressure they will be moved, by the definition of a fluid, from those places.",
     "dipende_da": [
      "Prop. XIX, Caso 1",
      "Definizione del fluido"
     ],
     "figura": {
      "mostra": [
       "confronto: prima e dopo l’aumento"
      ]
     }
    },
    {
     "id": "L2-P19-p10",
     "la": "",
     "it": "Le due cose si contraddicono.",
     "en": "Now these two conclusions contradict each other.",
     "dipende_da": [],
     "figura": {
      "mostra": [],
      "evidenzia": [
       "contraddizione"
      ]
     }
    },
    {
     "id": "L2-P19-p11",
     "la": "",
     "it": "Era dunque falso dire che la sfera EF non era premuta ugualmente da ogni parte. C.V.D.",
     "en": "Therefore it was false to say that the sphere EF was not pressed equally on every side.",
     "dipende_da": [],
     "figura": {
      "mostra": [
       "pressione uniforme su EF"
      ]
     }
    },
    {
     "id": "L2-P19-p12",
     "la": "",
     "it": "Caso 3. Dico inoltre che la pressione di parti sferiche diverse è uguale.",
     "en": "CASE 3. I say besides, that different spherical parts have equal pressures.",
     "dipende_da": [],
     "figura": {
      "mostra": [
       "due parti sferiche diverse"
      ]
     }
    },
    {
     "id": "L2-P19-p13",
     "la": "",
     "it": "Infatti le parti sferiche contigue si premono a vicenda ugualmente nel punto di contatto, per la Legge III del moto.",
     "en": "For the contiguous spherical parts press each other mutually and equally in the point of contact (by Law III).",
     "dipende_da": [
      "Legge III"
     ],
     "figura": {
      "mostra": [
       "punto di contatto fra due sfere contigue"
      ],
      "evidenzia": [
       "azione e reazione nel contatto"
      ]
     }
    },
    {
     "id": "L2-P19-p14",
     "la": "",
     "it": "Ma anche, per il Caso 2, sono premute da ogni parte con la stessa forza.",
     "en": "But (by Case 2) they are pressed on every side with the same force.",
     "dipende_da": [
      "Prop. XIX, Caso 2"
     ],
     "figura": {
      "mostra": []
     }
    },
    {
     "id": "L2-P19-p15",
     "la": "",
     "it": "Due parti sferiche qualsiasi non contigue, dunque, poiché una parte sferica intermedia può toccarle entrambe, saranno premute con la stessa forza. C.V.D.",
     "en": "Therefore any two spherical parts not contiguous, since an intermediate spherical part can touch both, will be pressed with the same force.",
     "dipende_da": [],
     "figura": {
      "mostra": [
       "due sfere non contigue",
       "sfera intermedia tangente a entrambe"
      ]
     }
    },
    {
     "id": "L2-P19-p16",
     "la": "",
     "it": "Caso 4. Dico ora che tutte le parti del fluido sono premute ugualmente dovunque.",
     "en": "CASE 4. I say now, that all the parts of the fluid are every where pressed equally.",
     "dipende_da": [],
     "figura": {
      "mostra": [
       "parti di forma qualsiasi"
      ]
     }
    },
    {
     "id": "L2-P19-p17",
     "la": "",
     "it": "Infatti due parti qualsiasi possono essere toccate da parti sferiche in punti qualsiasi, e lì premono ugualmente quelle parti sferiche, per il Caso 3, e a loro volta sono premute ugualmente da esse, per la terza legge del moto. C.V.D.",
     "en": "For any two parts may be touched by spherical parts in any points whatever; and there they will equally press those spherical parts (by Case 3), and are reciprocally equally pressed by them (by Law III).",
     "dipende_da": [
      "Prop. XIX, Caso 3",
      "Legge III"
     ],
     "figura": {
      "mostra": [
       "sfere tangenti alle parti in punti qualsiasi"
      ]
     }
    },
    {
     "id": "L2-P19-p18",
     "la": "",
     "it": "Caso 5. Poiché dunque una parte qualsiasi GHI del fluido è racchiusa nel resto del fluido come in un vaso, ed è premuta ugualmente da ogni parte, e le sue parti si premono a vicenda ugualmente e stanno in quiete fra loro, è manifesto che tutte le parti di un fluido qualsiasi GHI, che sia premuto ugualmente da ogni parte, si premono a vicenda ugualmente e stanno in quiete fra loro. C.V.D.",
     "en": "CASE 5. Since, therefore, any part GHI of the fluid is inclosed by the rest of the fluid as in a vessel, and is equally pressed on every side; and also its parts equally press one another, and are at rest among themselves; it is manifest that all the parts of any fluid as GHI, which is pressed equally on every side, do press each other mutually and equally, and are at rest among themselves.",
     "dipende_da": [],
     "figura": {
      "mostra": [
       "parte GHI",
       "il resto del fluido come vaso"
      ],
      "evidenzia": [
       "generalizzazione a un vaso di forma qualsiasi"
      ]
     }
    },
    {
     "id": "L2-P19-p19",
     "la": "",
     "it": "Caso 6. Perciò, se quel fluido è racchiuso in un vaso non rigido e non è premuto ugualmente da ogni parte, cederà alla pressione più forte, per la definizione della fluidità.",
     "en": "CASE 6. Therefore if that fluid be included in a vessel of a yielding substance, or that is not rigid, and be not equally pressed on every side, the same will give way to a stronger pressure, by the Definition of fluidity.",
     "dipende_da": [
      "Definizione del fluido"
     ],
     "figura": {
      "mostra": [
       "vaso non rigido",
       "pressione più forte da un lato"
      ]
     },
     "nota": "Motte aggiunge «of a yielding substance, or»."
    },
    {
     "id": "L2-P19-p20",
     "la": "",
     "it": "Caso 7. E perciò in un vaso rigido il fluido non sosterrà da un lato una pressione più forte che dall’altro, ma le cederà, e ciò in un istante, perché il lato rigido del vaso non insegue il liquido che cede.",
     "en": "CASE 7. And therefore, in an inflexible or rigid vessel, a fluid will not sustain a stronger pressure on one side than on the other, but will give way to it, and that in a moment of time; because the rigid side of the vessel does not follow the yielding liquor.",
     "dipende_da": [],
     "figura": {
      "mostra": [
       "vaso rigido",
       "lato più premuto"
      ]
     },
     "nota": "Nel latino il marcatore di pagina <284> cade fra pressionem e fortiorem. Motte aggiunge «inflexible or»."
    },
    {
     "id": "L2-P19-p21",
     "la": "",
     "it": "Cedendo, poi, premerà il lato opposto, e così la pressione tenderà da ogni parte all’uguaglianza.",
     "en": "But the fluid, by thus yielding, will press against the opposite side, and so the pressure will tend on every side to equality.",
     "dipende_da": [],
     "figura": {
      "mostra": [
       "lato opposto"
      ],
      "evidenzia": [
       "trasmissione della pressione"
      ]
     }
    },
    {
     "id": "L2-P19-p22",
     "la": "",
     "it": "E poiché il fluido, non appena tende ad allontanarsi dalla parte più premuta, è trattenuto dalla resistenza del vaso dal lato opposto, la pressione sarà ricondotta da ogni parte all’uguaglianza, in un istante, senza moto locale; e quindi le parti del fluido, per il Caso 5, si premeranno a vicenda ugualmente e staranno in quiete fra loro. C.V.D.",
     "en": "And because the fluid, as soon as it endeavours to recede from the part that is most pressed, is withstood by the resistance of the vessel on the opposite side, the pressure will on every side be reduced to equality, in a moment of time, without any local motion: and from thence the parts of the fluid (by Case 5) will press each other mutually and equally, and be at rest among themselves.",
     "dipende_da": [
      "Prop. XIX, Caso 5"
     ],
     "figura": {
      "mostra": [
       "reazione del vaso",
       "pressione uniforme ristabilita"
      ]
     }
    }
   ]
  },
  {
   "id": "L2-P20",
   "tipo": "Propositio/Theorema",
   "titolo": "Prop. XX — il fondo sostiene il peso di un cilindro",
   "copertura": [
    "II.S5.11",
    "II.S5.12"
   ],
   "fonti": {
    "la": "",
    "en": "Motte 1846, sezione corrispondente"
   },
   "enunciato": {
    "la": "",
    "it": "Se le singole parti di un fluido sferico, omogeneo a distanze uguali dal centro, che poggia su un fondo sferico concentrico, gravitano verso il centro del tutto, il fondo sostiene il peso di un cilindro la cui base è uguale alla superficie del fondo e la cui altezza è la stessa del fluido che vi poggia.",
    "en": "If all the parts of a spherical fluid, homogeneous at equal distances from the centre, lying on a spherical concentric bottom, gravitate towards the centre of the whole, the bottom will sustain the weight of a cylinder, whose base is equal to the superficies of the bottom, and whose altitude is the same with that of the incumbent fluid."
   },
   "figura_base": {
    "punti": [
     "D",
     "H",
     "M",
     "A",
     "E",
     "I",
     "B",
     "F",
     "K",
     "C",
     "G",
     "L"
    ],
    "vincoli": [
     "DHM superficie sferica del fondo",
     "AEI superficie superiore del fluido, concentrica",
     "BFK, CGL superfici sferiche intermedie, concentriche, a uguale distanza (gusci di uguale spessore)",
     "A, B, C, D allineati su un raggio (e così E, F, G, H e I, K, L, M), lettura ricostruita dal testo"
    ]
   },
   "passi": [
    {
     "id": "L2-P20-p1",
     "la": "",
     "it": "Sia DHM la superficie del fondo e AEI la superficie superiore del fluido.",
     "en": "Let DHM be the superficies of the bottom, and AEI the upper superficies of the fluid.",
     "dipende_da": [],
     "figura": {
      "mostra": [
       "fondo DHM",
       "superficie superiore AEI",
       "centro"
      ]
     },
     "nota": "Nel latino il marcatore [FIG 39] cade fra AEI e superficies."
    },
    {
     "id": "L2-P20-p2",
     "la": "",
     "it": "Con innumerevoli superfici sferiche BFK, CGL si divida il fluido in gusci concentrici di uguale spessore; e immagina che la forza di gravità agisca soltanto sulla superficie superiore di ciascun guscio, e che le azioni su parti uguali di tutte le superfici siano uguali.",
     "en": "Let the fluid be distinguished into concentric orbs of equal thickness, by the innumerable spherical superficies BFK, CGL: and conceive the force of gravity to act only in the upper superficies of every orb, and the actions to be equal on the equal parts of all the superficies.",
     "dipende_da": [],
     "figura": {
      "mostra": [
       "superfici BFK, CGL",
       "gusci di uguale spessore"
      ],
      "evidenzia": [
       "gravità concentrata sulla superficie superiore di ogni guscio"
      ]
     }
    },
    {
     "id": "L2-P20-p3",
     "la": "",
     "it": "La superficie più alta AE è dunque premuta dalla forza semplice della propria gravità, dalla quale sono premute ugualmente, in proporzione alla loro misura, sia tutte le parti del guscio più alto sia la seconda superficie BFK (per la Prop. XIX).",
     "en": "Therefore the upper superficies AE is pressed by the single force of its own gravity, by which all the parts of the upper orb, and the second superficies BFK, will (by Prop. XIX), according to its measure, be equally pressed.",
     "dipende_da": [
      "Prop. XIX"
     ],
     "figura": {
      "mostra": [
       "pressione 1 su AE e su BFK"
      ],
      "evidenzia": [
       "pressione semplice"
      ]
     }
    },
    {
     "id": "L2-P20-p4",
     "la": "",
     "it": "La seconda superficie BFK è premuta inoltre dalla forza della propria gravità, che, aggiunta alla forza precedente, dà una pressione doppia.",
     "en": "The second superficies BFK is pressed likewise by the force of its own gravity, which, added to the former force, makes the pressure double.",
     "dipende_da": [],
     "figura": {
      "mostra": [
       "pressione 2 su BFK"
      ]
     },
     "nota": "Nel latino il marcatore di pagina <285> cade fra quæ e addita."
    },
    {
     "id": "L2-P20-p5",
     "la": "",
     "it": "Da questa pressione, in proporzione alla sua misura, e in più dalla forza della propria gravità, cioè da una pressione tripla, è premuta la terza superficie CGL.",
     "en": "The third superficies CGL is, according to its measure, acted on by this pressure and the force of its own gravity besides, which makes its pressure triple.",
     "dipende_da": [],
     "figura": {
      "mostra": [
       "pressione 3 su CGL"
      ]
     }
    },
    {
     "id": "L2-P20-p6",
     "la": "",
     "it": "E similmente la quarta superficie è premuta da una pressione quadrupla, la quinta da una quintupla, e così via.",
     "en": "And in like manner the fourth superficies receives a quadruple pressure, the fifth superficies a quintuple, and so on.",
     "dipende_da": [],
     "figura": {
      "mostra": [
       "pressioni 4, 5, … verso il fondo"
      ],
      "evidenzia": [
       "pressione proporzionale al numero di gusci sovrastanti"
      ]
     }
    },
    {
     "id": "L2-P20-p7",
     "la": "",
     "it": "La pressione da cui è premuta ciascuna superficie non è dunque come la quantità solida del fluido che vi poggia, ma come il numero dei gusci fino alla sommità del fluido; ed è uguale alla gravità del guscio più basso moltiplicata per il numero dei gusci: cioè alla gravità di un solido il cui rapporto ultimo con il cilindro prima definito (purché il numero dei gusci si aumenti e lo spessore si diminuisca all’infinito, così che l’azione della gravità dalla superficie più bassa alla più alta sia resa continua) diventerà un rapporto di uguaglianza.",
     "en": "Therefore the pressure acting on every superficies is not as the solid quantity of the incumbent fluid, but as the number of the orbs reaching to the upper surface of the fluid; and is equal to the gravity of the lowest orb multiplied by the number of orbs: that is, to the gravity of a solid whose ultimate ratio to the cylinder above-mentioned (when the number of the orbs is increased and their thickness diminished, ad infinitum, so that the action of gravity from the lowest superficies to the uppermost may become continued) is the ratio of equality.",
     "dipende_da": [],
     "figura": {
      "mostra": [
       "guscio infimo",
       "cilindro di base DHM e altezza del fluido"
      ],
      "evidenzia": [
       "n × guscio infimo → cilindro (rapporto ultimo di uguaglianza)"
      ]
     },
     "nota": "Verifica numerica in N3: n = 10, 100, 1000 gusci danno 1,030; 1,0030; 1,0003."
    },
    {
     "id": "L2-P20-p8",
     "la": "",
     "it": "La superficie più bassa sostiene dunque il peso del cilindro prima definito. C.V.D.",
     "en": "Therefore the lowest superficies sustains the weight of the cylinder above determined.",
     "dipende_da": [],
     "figura": {
      "mostra": [
       "cilindro"
      ],
      "evidenzia": [
       "peso sostenuto dal fondo"
      ]
     }
    },
    {
     "id": "L2-P20-p9",
     "la": "",
     "it": "E con un argomento simile la proposizione risulta evidente quando la gravità decresce in un rapporto qualsiasi assegnato della distanza dal centro, e anche quando il fluido è più rado in alto e più denso in basso. C.V.D.",
     "en": "And by a like reasoning the Proposition will be evident, where the gravity of the fluid decreases in any assigned ratio of the distance from the centre, and also where the fluid is more rare above and denser below.",
     "dipende_da": [],
     "figura": {
      "mostra": [],
      "evidenzia": [
       "estensione a gravità e densità variabili"
      ]
     },
     "nota": "Motte aggiunge «of the fluid» dopo «gravity»."
    }
   ]
  },
  {
   "id": "L2-P21",
   "tipo": "Propositio/Theorema",
   "titolo": "Prop. XXI — gravità come 1/distanza: distanze e densità in proporzione continua",
   "copertura": [
    "II.S5.22",
    "II.S5.23"
   ],
   "fonti": {
    "la": "",
    "en": "Motte 1846, sezione corrispondente (SVG 600–605)"
   },
   "enunciato": {
    "la": "",
    "it": "Sia la densità di un fluido proporzionale alla compressione, e le sue parti siano tirate verso il basso da una forza centripeta inversamente proporzionale alle loro distanze dal centro: dico che, se quelle distanze si prendono continuamente proporzionali, anche le densità del fluido a quelle stesse distanze saranno continuamente proporzionali.",
    "en": "Let the density of any fluid be proportional to the compression, and its parts be attracted downwards by a centripetal force reciprocally proportional to the distances from the centre: I say, that, if those distances be taken continually proportional, the densities of the fluid at the same distances will be also continually proportional."
   },
   "figura_base": {
    "punti": [
     "S",
     "A",
     "B",
     "C",
     "D",
     "E",
     "F",
     "G",
     "T",
     "V",
     "H",
     "I",
     "K",
     "L",
     "M",
     "N",
     "O"
    ],
    "vincoli": [
     "S centro; ATV fondo sferico (arco di centro S)",
     "A, B, C, D, E, F, G su un raggio da S, con SA, SB, SC, … in progressione geometrica",
     "AH, BI, CK, DL, EM, FN, GO perpendicolari al raggio, lunghe come le densità"
    ]
   },
   "passi": [
    {
     "id": "L2-P21-p1",
     "la": "",
     "it": "Rappresenti ATV il fondo sferico su cui poggia il fluido, S il centro, SA, SB, SC, SD, SE, SF ecc. distanze continuamente proporzionali.",
     "en": "Let ATV denote the spherical bottom of the fluid, S the centre, SA, SB, SC, SD, SE, SF, &c., distances continually proportional.",
     "dipende_da": [],
     "figura": {
      "mostra": [
       "S",
       "fondo ATV",
       "punti A, B, C, D, E, F in progressione geometrica"
      ]
     },
     "nota": "Il marcatore di pagina <288> spezza propor|tionales: la stringa latina ha perciò «propor tionales»."
    },
    {
     "id": "L2-P21-p2",
     "la": "",
     "it": "Si innalzino le perpendicolari AH, BI, CK, DL, EM, FN ecc., che stiano come le densità del mezzo nei luoghi A, B, C, D, E; e le gravità specifiche in quegli stessi luoghi staranno come AH/AS, BI/BS, CK/CS ecc., o, ciò che è lo stesso, come AH/AB, BI/BC, CK/CD ecc.",
     "en": "Erect the perpendiculars AH, BI, CK, DL, EM, FN, &c., which shall be as the densities of the medium in the places A, B, C, D, E, F; and the specific gravities in those places will be as [SVG 600], [SVG 601], [SVG 602], &c., or, which is all one, as [SVG 603], [SVG 604], [SVG 605], &c.",
     "dipende_da": [],
     "figura": {
      "mostra": [
       "perpendicolari AH, BI, CK, DL, EM, FN"
      ],
      "evidenzia": [
       "gravità specifica = densità × gravità ∝ AH/AS"
      ]
     },
     "nota": "Frazioni appiattite nella trascrizione: AHAS = AH/AS, AHAB = AH/AB ecc. Motte aggiunge F all’elenco dei luoghi; SVG 600–605 verificate: AH/AS, BI/BS, CK/CS; AH/AB, BI/BC, CK/CD (§ A.9)."
    },
    {
     "id": "L2-P21-p3",
     "la": "",
     "it": "Immagina dapprima che queste gravità si mantengano uniformi da A a B, da B a C, da C a D ecc., con decrementi fatti per gradi nei punti B, C, D ecc.",
     "en": "Suppose, first, these gravities to be uniformly continued from A to B, from B to C, from C to D, &c., the decrements in the points B, C, D, &c., being taken by steps.",
     "dipende_da": [],
     "figura": {
      "mostra": [
       "gravità a gradini sugli intervalli AB, BC, CD"
      ]
     }
    },
    {
     "id": "L2-P21-p4",
     "la": "",
     "it": "E queste gravità, moltiplicate per le altezze AB, BC, CD ecc., daranno le pressioni AH, BI, CK ecc., dalle quali è premuto il fondo ATV (secondo il Teorema XV).",
     "en": "And these gravities drawn into the altitudes AB, BC, CD, &c., will give the pressures AH, BI, CK, &c., by which the bottom ATV is acted on (by Theor. XV).",
     "dipende_da": [
      "Prop. XX (Teorema XV)"
     ],
     "figura": {
      "mostra": [
       "pressioni parziali AH, BI, CK"
      ],
      "evidenzia": [
       "(AH/AB) × AB = AH"
      ]
     },
     "nota": "Nel latino il marcatore [FIG 40] cade fra Et e hæ."
    },
    {
     "id": "L2-P21-p5",
     "la": "",
     "it": "La particella A sostiene dunque tutte le pressioni AH, BI, CK, DL, procedendo all’infinito; la particella B tutte tranne la prima, AH; la particella C tutte tranne le prime due, AH, BI; e così via: e perciò la densità AH della prima particella A sta alla densità BI della seconda particella B come la somma di tutte, AH + BI + CK + DL all’infinito, sta alla somma di tutte, BI + CK + DL ecc.",
     "en": "Therefore the particle A sustains all the pressures AH, BI, CK, DL, &c., proceeding in infinitum; and the particle B sustains the pressures of all but the first AH; and the particle C all but the two first AH, BI; and so on: and therefore the density AH of the first particle A is to the density BI of the second particle B as the sum of all AH + BI + CK + DL, in infinitum, to the sum of all BI + CK + DL, &c.",
     "dipende_da": [],
     "figura": {
      "mostra": [
       "somme delle pressioni sopra A, sopra B, sopra C"
      ],
      "evidenzia": [
       "densità ∝ compressione = somma delle pressioni sovrastanti"
      ]
     }
    },
    {
     "id": "L2-P21-p6",
     "la": "",
     "it": "E BI, densità della seconda B, sta a CK, densità della terza C, come la somma di tutte, BI + CK + DL ecc., sta alla somma di tutte, CK + DL ecc.",
     "en": "And BI the density of the second particle B is to CK the density of the third C, as the sum of all BI + CK + DL, &c., to the sum of all CK + DL, &c.",
     "dipende_da": [],
     "figura": {
      "mostra": []
     }
    },
    {
     "id": "L2-P21-p7",
     "la": "",
     "it": "Quelle somme sono dunque proporzionali alle loro differenze AH, BI, CK ecc., e perciò continuamente proporzionali (per il Lemma I di questo Libro); e quindi le differenze AH, BI, CK ecc., proporzionali alle somme, sono anch’esse continuamente proporzionali.",
     "en": "Therefore these sums are proportional to their differences AH, BI, CK, &c., and therefore continually proportional (by Lem. 1 of this Book); and therefore the differences AH, BI, CK, &c., proportional to the sums, are also continually proportional.",
     "dipende_da": [
      "Libro II, Lemma I"
     ],
     "figura": {
      "mostra": [],
      "evidenzia": [
       "somme ∝ differenze ⇒ proporzione continua"
      ]
     }
    },
    {
     "id": "L2-P21-p8",
     "la": "",
     "it": "Perciò, poiché le densità nei luoghi A, B, C ecc. stanno come AH, BI, CK ecc., anche queste saranno continuamente proporzionali.",
     "en": "Wherefore since the densities in the places A, B, C, &c., are as AH, BI, CK, &c., they will also be continually proportional.",
     "dipende_da": [],
     "figura": {
      "mostra": [
       "AH, BI, CK in progressione geometrica"
      ]
     }
    },
    {
     "id": "L2-P21-p9",
     "la": "",
     "it": "Si proceda per salti, e ex æquo, alle distanze SA, SC, SE continuamente proporzionali, le densità AH, CK, EM saranno continuamente proporzionali.",
     "en": "Proceed intermissively, and, ex æquo, at the distances SA, SC, SE, continually proportional, the densities AH, CK, EM will be continually proportional.",
     "dipende_da": [],
     "figura": {
      "mostra": [
       "SA, SC, SE",
       "AH, CK, EM"
      ]
     }
    },
    {
     "id": "L2-P21-p10",
     "la": "",
     "it": "E con lo stesso argomento, a distanze qualsiasi continuamente proporzionali SA, SD, SG, le densità AH, DL, GO saranno continuamente proporzionali.",
     "en": "And by the same reasoning, at any distances SA, SD, SG, continually proportional, the densities AH, DL, GO, will be continually proportional.",
     "dipende_da": [],
     "figura": {
      "mostra": [
       "G, GO",
       "SA, SD, SG"
      ]
     }
    },
    {
     "id": "L2-P21-p11",
     "la": "",
     "it": "Si riuniscano ora i punti A, B, C, D, E ecc., in modo che la progressione delle gravità specifiche dal fondo A alla sommità del fluido sia resa continua; e a distanze qualsiasi continuamente proporzionali SA, SD, SG, le densità AH, DL, GO, essendo sempre continuamente proporzionali, rimarranno ancora continuamente proporzionali. C.V.D.",
     "en": "Let now the points A, B, C, D, E, &c., coincide, so that the progression of the specific gravities from the bottom A to the top of the fluid may be made continual; and at any distances SA, SD, SG, continually proportional, the densities AH, DL, GO, being all along continually proportional, will still remain continually proportional.",
     "dipende_da": [],
     "figura": {
      "mostra": [
       "passaggio al continuo"
      ],
      "evidenzia": [
       "limite: suddivisione infinitamente fitta"
      ]
     }
    }
   ]
  },
  {
   "id": "L2-P21-Cor",
   "tipo": "Corollarium",
   "titolo": "Prop. XXI, Cor. — densità in un luogo qualsiasi dalle aree iperboliche",
   "copertura": [
    "II.S5.24"
   ],
   "fonti": {
    "la": "",
    "en": "Motte 1846, sezione corrispondente"
   },
   "enunciato": {
    "la": "",
    "it": "Di qui, se è data la densità del fluido in due luoghi, per esempio A ed E, se ne può ricavare la densità in qualsiasi altro luogo Q.",
    "en": "Hence if the density of the fluid in two places, as A and E, be given, its density in any other place Q may be collected."
   },
   "figura_base": {
    "punti": [
     "S",
     "A",
     "E",
     "Q",
     "H",
     "M",
     "T",
     "X",
     "Y",
     "Z",
     "a",
     "e",
     "q",
     "h",
     "m",
     "t"
    ],
    "vincoli": [
     "SQ, SX asintoti ortogonali; S centro dell’iperbole equilatera",
     "A, E, Q su SQ; AH, EM, QT perpendicolari a SQ, lunghe come le densità",
     "a, e, q intersezioni dell’iperbole con AH, EM, QT",
     "X, Y, Z su SX con SX = AH, SY = EM, SZ = QT; HX, MY, TZ perpendicolari a SX; h, m, t intersezioni con l’iperbole",
     "area YmtZ : area YmhX = area EeqQ : area EeaA"
    ]
   },
   "passi": [
    {
     "id": "L2-P21-Cor-p1",
     "la": "",
     "it": "Con centro S e asintoti ortogonali SQ, SX si descriva un’iperbole che tagli le perpendicolari AH, EM, QT in a, e, q, e anche le perpendicolari HX, MY, TZ, abbassate sull’asintoto SX, in h, m e t.",
     "en": "With the centre S, and the rectangular asymptotes SQ, SX, describe an hyperbola cutting the perpendiculars AH, EM, QT in a, e, and q, as also the perpendiculars HX, MY, TZ, let fall upon the asymptote SX, in h, m, and t.",
     "dipende_da": [],
     "figura": {
      "mostra": [
       "asintoti SQ, SX",
       "iperbole",
       "a, e, q",
       "HX, MY, TZ",
       "h, m, t"
      ]
     }
    },
    {
     "id": "L2-P21-Cor-p2",
     "la": "",
     "it": "Si faccia in modo che l’area YmtZ stia all’area data YmhX come l’area data EeqQ sta all’area data EeaA; e la linea Zt prolungata taglierà la linea QT proporzionale alla densità.",
     "en": "Make the area YmtZ to the given area YmhX as the given area EeqQ to the given area EeaA; and the line Zt produced will cut off the line QT proportional to the density.",
     "dipende_da": [],
     "figura": {
      "mostra": [
       "aree EeaA, EeqQ",
       "aree YmhX, YmtZ",
       "Zt prolungata fino a T"
      ],
      "evidenzia": [
       "proporzione fra le aree"
      ]
     },
     "nota": "Nel latino il marcatore [FIG 41] cade fra Fiat e area."
    },
    {
     "id": "L2-P21-Cor-p3",
     "la": "",
     "it": "Infatti, se le linee SA, SE, SQ sono continuamente proporzionali, le aree EeqQ, EeaA saranno uguali, e di qui anche le aree a esse proporzionali YmtZ, XhmY saranno uguali, e le linee SX, SY, SZ, cioè AH, EM, QT, continuamente proporzionali, come deve essere.",
     "en": "For if the lines SA, SE, SQ are continually proportional, the areas EeqQ, EeaA will be equal, and thence the areas YmtZ, XhmY, proportional to them, will be also equal; and the lines SX, SY, SZ, that is, AH, EM, QT continually proportional, as they ought to be.",
     "dipende_da": [],
     "figura": {
      "mostra": [],
      "evidenzia": [
       "aree iperboliche uguali ⇔ estremi in rapporto uguale (logaritmo)"
      ]
     }
    },
    {
     "id": "L2-P21-Cor-p4",
     "la": "",
     "it": "E se le linee SA, SE, SQ occupano un altro posto qualsiasi nella serie delle continuamente proporzionali, le linee AH, EM, QT, per le aree iperboliche proporzionali, occuperanno lo stesso posto in un’altra serie di quantità continuamente proporzionali.",
     "en": "And if the lines SA, SE, SQ, obtain any other order in the series of continued proportionals, the lines AH, EM, QT, because of the proportional hyperbolic areas, will obtain the same order in another series of quantities continually proportional.",
     "dipende_da": [],
     "figura": {
      "mostra": [],
      "evidenzia": [
       "caso generale"
      ]
     },
     "nota": "Verifica numerica in N6."
    }
   ]
  },
  {
   "id": "L2-P22",
   "tipo": "Propositio/Theorema",
   "titolo": "Prop. XXII — gravità come 1/distanza²: distanze in progressione armonica, densità in progressione geometrica",
   "copertura": [
    "II.S5.25",
    "II.S5.26"
   ],
   "fonti": {
    "la": "",
    "en": "Motte 1846, sezione corrispondente (SVG 606–614)"
   },
   "enunciato": {
    "la": "",
    "it": "Sia la densità di un fluido proporzionale alla compressione, e le sue parti siano tirate verso il basso da una gravità inversamente proporzionale ai quadrati delle loro distanze dal centro: dico che, se le distanze si prendono in progressione armonica, le densità del fluido a queste distanze saranno in progressione geometrica.",
    "en": "Let the density of any fluid be proportional to the compression, and its parts be attracted downwards by a gravitation reciprocally proportional to the squares of the distances from the centre: I say, that if the distances be taken in harmonic progression, the densities of the fluid at those distances will be in a geometrical progression."
   },
   "figura_base": {
    "punti": [
     "S",
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
     "N",
     "x",
     "t",
     "u",
     "w",
     "z",
     "a",
     "b",
     "c",
     "d",
     "f",
     "h",
     "i",
     "k",
     "l",
     "n",
     "p",
     "q",
     "r"
    ],
    "vincoli": [
     "S centro; A, B, C, D, E, F su un raggio SA (asintoto), con SA, SB, SC … in progressione geometrica",
     "AH, BI, CK, … perpendicolari a SA, lunghe come le densità",
     "Sx secondo asintoto, perpendicolare a SA; iperbole equilatera di asintoti SA, Sx",
     "a, b, c, … intersezioni dell’iperbole con AH, BI, CK, …",
     "t, u, w, … su Sx con St = AH, Su = BI, Sw = CK; Ht, Iu, Kw perpendicolari a Sx, che tagliano l’iperbole in h, i, k",
     "tp, uq, wr rettangoli tu × th, uw × ui, …",
     "x, z su Sx con Sx = DL, Sz = FN; l, n sull’iperbole"
    ]
   },
   "passi": [
    {
     "id": "L2-P22-p1",
     "la": "",
     "it": "Rappresenti S il centro, e SA, SB, SC, SD, SE distanze in progressione geometrica.",
     "en": "Let S denote the centre, and SA, SB, SC, SD, SE, the distances in geometrical progression.",
     "dipende_da": [],
     "figura": {
      "mostra": [
       "S",
       "A, B, C, D, E in progressione geometrica"
      ]
     }
    },
    {
     "id": "L2-P22-p2",
     "la": "",
     "it": "Si innalzino le perpendicolari AH, BI, CK ecc., che stiano come le densità del fluido nei luoghi A, B, C, D, E ecc.; e le sue gravità specifiche in quegli stessi luoghi saranno AH/SA², BI/SB², CK/SC² ecc.",
     "en": "Erect the perpendiculars AH, BI, CK, &c., which shall be as the densities of the fluid in the places A, B, C, D, E, &c., and the specific gravities thereof in those places will be as [SVG 606], [SVG 607], [SVG 608], &c.",
     "dipende_da": [],
     "figura": {
      "mostra": [
       "perpendicolari AH, BI, CK"
      ],
      "evidenzia": [
       "gravità specifica ∝ AH/SA²"
      ]
     },
     "nota": "specfifcæ: refuso della trascrizione per specificæ. AHSAq = AH/SA². Motte aggiunge «as». SVG 606–608 verificate: AH/SA², BI/SB², CK/SC²."
    },
    {
     "id": "L2-P22-p3",
     "la": "",
     "it": "Immagina che queste gravità si mantengano uniformi, la prima da A a B, la seconda da B a C, la terza da C a D ecc.",
     "en": "Suppose these gravities to be uniformly continued, the first from A to B, the second from B to C, the third from C to D, &c.",
     "dipende_da": [],
     "figura": {
      "mostra": [
       "gravità a gradini"
      ]
     }
    },
    {
     "id": "L2-P22-p4",
     "la": "",
     "it": "E queste, moltiplicate per le altezze AB, BC, CD, DE ecc., o, ciò che è lo stesso, per le distanze SA, SB, SC ecc., proporzionali a quelle altezze, daranno gli esponenti delle pressioni AH/SA, BI/SB, CK/SC ecc.",
     "en": "And these drawn into the altitudes AB, BC, CD, DE, &c., or, which is the same thing, into the distances SA, SB, SC, &c., proportional to those altitudes, will give [SVG 609], [SVG 610], [SVG 611], &c., the exponents of the pressures.",
     "dipende_da": [],
     "figura": {
      "mostra": [],
      "evidenzia": [
       "AB ∝ SA (progressione geometrica)",
       "pressione parziale ∝ AH/SA"
      ]
     },
     "nota": "Il marcatore di pagina <290> spezza pressio|num. AHSA = AH/SA. SVG 609–611 verificate: AH/SA, BI/SB, CK/SC."
    },
    {
     "id": "L2-P22-p5",
     "la": "",
     "it": "Perciò, poiché le densità stanno come le somme di queste pressioni, le differenze delle densità AH − BI, BI − CK ecc. staranno come le differenze delle somme AH/SA, BI/SB, CK/SC ecc.",
     "en": "Therefore since the densities are as the sums of those pressures, the differences AH - BI, BI - CK, &c., of the densities will be as the differences of those sums [SVG 609], [SVG 610], [SVG 611] &c.",
     "dipende_da": [],
     "figura": {
      "mostra": [],
      "evidenzia": [
       "AH − BI ∝ AH/SA"
      ]
     }
    },
    {
     "id": "L2-P22-p6",
     "la": "",
     "it": "Con centro S e asintoti SA, Sx si descriva un’iperbole qualsiasi, che tagli le perpendicolari AH, BI, CK ecc. in a, b, c ecc., e anche le perpendicolari Ht, Iu, Kw, abbassate sull’asintoto Sx, in h, i, k; e le differenze delle densità tu, uw ecc. staranno come AH/SA, BI/SB ecc.",
     "en": "With the centre S, and the asymptotes SA, Sx, describe any hyperbola, cutting the perpendiculars AH, BI, CK, &c., in a, b, c, &c., and the perpendiculars Ht, Iu, Kw, let fall upon the asymptote Sx, in h, i, k; and the differences of the densities tu, uw, &c., will be as [SVG 609], [SVG 610], &c.",
     "dipende_da": [],
     "figura": {
      "mostra": [
       "asintoto Sx",
       "iperbole",
       "a, b, c",
       "t, u, w",
       "h, i, k"
      ],
      "evidenzia": [
       "tu = AH − BI"
      ]
     }
    },
    {
     "id": "L2-P22-p7",
     "la": "",
     "it": "E i rettangoli tu × th, uw × ui ecc., ossia tp, uq ecc., staranno come AH × th/SA, BI × ui/SB ecc., cioè come Aa, Bb ecc.",
     "en": "And the rectangles tu × th, uw × ui, &c., or tp, uq, &c., as [SVG 612], [SVG 613], &c., that is, as Aa, Bb, &c.",
     "dipende_da": [],
     "figura": {
      "mostra": [
       "rettangoli tp, uq"
      ],
      "evidenzia": [
       "tp ∝ Aa"
      ]
     },
     "nota": "AH×thSA = AH × th/SA. SVG 612–613 verificate: AH × th/SA, BI × ui/SB."
    },
    {
     "id": "L2-P22-p8",
     "la": "",
     "it": "Infatti, per la natura dell’iperbole, SA sta ad AH, o St, come th sta ad Aa, e perciò AH × th/SA è uguale ad Aa.",
     "en": "For, by the nature of the hyperbola, SA is to AH or St as th to Aa, and therefore [SVG 612] is equal to Aa.",
     "dipende_da": [],
     "figura": {
      "mostra": [
       "segmenti Aa, th"
      ],
      "evidenzia": [
       "SA × Aa = St × th (iperbole equilatera)"
      ]
     }
    },
    {
     "id": "L2-P22-p9",
     "la": "",
     "it": "E con un argomento simile BI × ui/SB è uguale a Bb, ecc.",
     "en": "And, by a like reasoning, [SVG 614] is equal to Bb, &c.",
     "dipende_da": [],
     "figura": {
      "mostra": [
       "Bb, ui"
      ]
     },
     "nota": "Nel latino il marcatore [FIG 42] cade dopo BI×uiSB. SVG 614 verificata: BI × ui/SB."
    },
    {
     "id": "L2-P22-p10",
     "la": "",
     "it": "Ora Aa, Bb, Cc ecc. sono continuamente proporzionali, e perciò proporzionali alle loro differenze Aa − Bb, Bb − Cc ecc.; e perciò a queste differenze sono proporzionali i rettangoli tp, uq ecc., come anche alle somme delle differenze, Aa − Cc o Aa − Dd, le somme dei rettangoli, tp + uq o tp + uq + wr.",
     "en": "But Aa, Bb, Cc, &c., are continually proportional, and therefore proportional to their differences Aa - Bb, Bb - Cc, &c., therefore the rectangles tp, uq, &c., are proportional to those differences; as also the sums of the rectangles tp + uq, or tp + uq + wr to the sums of the differences Aa - Cc or Aa - Dd.",
     "dipende_da": [],
     "figura": {
      "mostra": [
       "Aa, Bb, Cc, Dd",
       "rettangolo wr"
      ],
      "evidenzia": [
       "rettangoli ∝ differenze Aa − Bb …"
      ]
     }
    },
    {
     "id": "L2-P22-p11",
     "la": "",
     "it": "Si prendano moltissimi termini di questo genere, e la somma di tutte le differenze, per esempio Aa − Ff, sarà proporzionale alla somma di tutti i rettangoli, per esempio zthn.",
     "en": "Suppose several of these terms, and the sum of all the differences, as Aa - Ff, will be proportional to the sum of all the rectangles, as zthn.",
     "dipende_da": [],
     "figura": {
      "mostra": [
       "F, Ff",
       "z, n"
      ],
      "evidenzia": [
       "somma dei rettangoli fra t e z"
      ]
     },
     "nota": "Motte rende quam plurimi con «several»: attenuazione."
    },
    {
     "id": "L2-P22-p12",
     "la": "",
     "it": "Si aumenti il numero dei termini e si diminuiscano le distanze dei punti A, B, C ecc. all’infinito: quei rettangoli diventeranno uguali all’area iperbolica zthn, e perciò a quest’area è proporzionale la differenza Aa − Ff.",
     "en": "Increase the number of terms, and diminish the distances of the points A, B, C, &c., in infinitum, and those rectangles will become equal to the hyperbolic area zthn, and therefore the difference Aa - Ff is proportional to this area.",
     "dipende_da": [],
     "figura": {
      "mostra": [
       "area iperbolica zthn"
      ],
      "evidenzia": [
       "limite: rettangoli → area"
      ]
     },
     "nota": "Il marcatore di pagina <291> cade dopo C,."
    },
    {
     "id": "L2-P22-p13",
     "la": "",
     "it": "Si prendano ora distanze qualsiasi, per esempio SA, SD, SF, in progressione armonica: le differenze Aa − Dd, Dd − Ff saranno uguali; e perciò le aree thlx, xlnz, proporzionali a queste differenze, saranno uguali fra loro, e le densità St, Sx, Sz, cioè AH, DL, FN, continuamente proporzionali. C.V.D.",
     "en": "Take now any distances, as SA, SD, SF, in harmonic progression, and the differences Aa - Dd, Dd - Ff will be equal; and therefore the areas thlx, xlnz, proportional to those differences will be equal among themselves, and the densities St, Sx, Sz, that is, AH, DL, FN, continually proportional.",
     "dipende_da": [],
     "figura": {
      "mostra": [
       "SA, SD, SF in progressione armonica",
       "aree thlx, xlnz"
      ],
      "evidenzia": [
       "Aa ∝ 1/SA: progressione armonica ⇒ differenze uguali ⇒ aree uguali ⇒ densità in progressione geometrica"
      ]
     }
    }
   ]
  },
  {
   "id": "L2-P23",
   "tipo": "Propositio/Theorema",
   "titolo": "Prop. XXIII — fluido elastico: forze fra particelle inversamente come la distanza",
   "copertura": [
    "II.S5.30",
    "II.S5.31",
    "II.S5.32"
   ],
   "fonti": {
    "la": "",
    "en": "Motte 1846, sezione corrispondente"
   },
   "enunciato": {
    "la": "",
    "it": "Se la densità di un fluido composto di particelle che si fuggono a vicenda è come la compressione, le forze centrifughe delle particelle sono inversamente proporzionali alle distanze dei loro centri. E viceversa, particelle che si fuggono a vicenda con forze inversamente proporzionali alle distanze dei loro centri compongono un fluido elastico la cui densità è proporzionale alla compressione.",
    "en": "If a fluid be composed of particles mutually flying each other, and the density be as the compression, the centrifugal forces of the particles will be reciprocally proportional to the distances of their centres. And, vice versa, particles flying each other, with forces that are reciprocally proportional to the distances of their centres, compose an elastic fluid, whose density is as the compression."
   },
   "figura_base": {
    "punti": [
     "A",
     "B",
     "C",
     "D",
     "E",
     "P",
     "F",
     "G",
     "H",
     "a",
     "b",
     "c",
     "d",
     "e",
     "f",
     "g",
     "h"
    ],
    "vincoli": [
     "ACE cubo maggiore di lato AB; ace cubo minore di lato ab (minuscole per il cubo minore)",
     "ABCD faccia piana del cubo maggiore; db faccia del cubo minore",
     "DP quadrato nella faccia ABCD, con vertice D, uguale alla faccia db",
     "FGH, fgh piani per il mezzo dei cubi, paralleli alle facce premute (lettura ricostruita dal testo)"
    ]
   },
   "passi": [
    {
     "id": "L2-P23-p1",
     "la": "",
     "it": "Si intenda che il fluido sia racchiuso nello spazio cubico ACE, e poi sia ridotto per compressione nello spazio cubico minore ace; e le distanze delle particelle che conservano fra loro una posizione simile nell’uno e nell’altro spazio staranno come i lati dei cubi AB, ab; e le densità dei mezzi inversamente come gli spazi che li contengono, AB³ e ab³.",
     "en": "Let the fluid be supposed to be included in a cubic space ACE, and then to be reduced by compression into a lesser cubic space ace; and the distances of the particles retaining a like situation with respect to each other in both the spaces, will be as the sides AB, ab of the cubes; and the densities of the mediums will be reciprocally as the containing spaces AB3, ab3.",
     "dipende_da": [],
     "figura": {
      "mostra": [
       "cubo ACE",
       "cubo ace",
       "lati AB, ab"
      ],
      "evidenzia": [
       "distanze ∝ lati; densità ∝ 1/lato³"
      ]
     },
     "nota": "Motte 1846 ha «AB3, ab3»: esponenti appiattiti nell’estratto."
    },
    {
     "id": "L2-P23-p2",
     "la": "",
     "it": "Sulla faccia piana ABCD del cubo maggiore si prenda il quadrato DP uguale alla faccia piana db del cubo minore; e, per ipotesi, la pressione con cui il quadrato DP preme il fluido racchiuso starà alla pressione con cui quel quadrato db preme il fluido racchiuso come le densità del mezzo fra loro, cioè come ab³ sta ad AB³.",
     "en": "In the plane side of the greater cube ABCD take the square DP equal to the plane side db of the lesser cube: and, by the supposition, the pressure with which the square DP urges the inclosed fluid will be to the pressure with which that square db urges the inclosed fluid as the densities of the mediums are to each other, that is, as ab3 to AB3.",
     "dipende_da": [],
     "figura": {
      "mostra": [
       "faccia ABCD",
       "quadrato DP = faccia db"
      ],
      "evidenzia": [
       "stessa area: forza ∝ densità (ipotesi)"
      ]
     },
     "nota": "Nel latino il marcatore [FIG 43] cade fra DP e æquale."
    },
    {
     "id": "L2-P23-p3",
     "la": "",
     "it": "Ma la pressione con cui il quadrato DB preme il fluido racchiuso sta alla pressione con cui il quadrato DP preme lo stesso fluido come il quadrato DB sta al quadrato DP, cioè come AB² sta ad ab².",
     "en": "But the pressure with which the square DB urges the included fluid is to the pressure with which the square DP urges the same fluid as the square DB to the square DP, that is, as AB2 to ab2.",
     "dipende_da": [],
     "figura": {
      "mostra": [
       "quadrato DB (intera faccia)"
      ],
      "evidenzia": [
       "stessa densità: forza ∝ area"
      ]
     }
    },
    {
     "id": "L2-P23-p4",
     "la": "",
     "it": "Dunque, ex æquo, la pressione con cui il quadrato DB preme il fluido sta alla pressione con cui il quadrato db preme il fluido come ab sta ad AB.",
     "en": "Therefore, ex æquo, the pressure with which the square DB urges the fluid is to the pressure with which the square db urges the fluid as ab to AB.",
     "dipende_da": [],
     "figura": {
      "mostra": [],
      "evidenzia": [
       "(AB²/ab²) × (ab³/AB³) = ab/AB"
      ]
     },
     "nota": "Il marcatore di pagina <293> cade dopo Ergo,."
    },
    {
     "id": "L2-P23-p5",
     "la": "",
     "it": "Con i piani FGH, fgh, condotti per il mezzo dei cubi, si divida il fluido in due parti: queste si premeranno a vicenda con le stesse forze con cui sono premute dai piani AC, ac, cioè nella proporzione di ab ad AB; e perciò le forze centrifughe, dalle quali queste pressioni sono sostenute, stanno nello stesso rapporto.",
     "en": "Let the planes FGH, fgh, be drawn through the middles of the two cubes, and divide the fluid into two parts. These parts will press each other mutually with the same forces with which they are themselves pressed by the planes AC, ac, that is, in the proportion of ab to AB: and therefore the centrifugal forces by which these pressures are sustained are in the same ratio.",
     "dipende_da": [],
     "figura": {
      "mostra": [
       "piani mediani FGH, fgh"
      ],
      "evidenzia": [
       "le due metà si premono come le facce"
      ]
     },
     "nota": "AC, ac indicano qui le facce premute (ABCD, abcd), come DB e db: lettura ricostruita, da verificare sulla figura."
    },
    {
     "id": "L2-P23-p6",
     "la": "",
     "it": "Per lo stesso numero di particelle e per la loro posizione simile nell’uno e nell’altro cubo, le forze che tutte le particelle esercitano su tutte secondo i piani FGH, fgh stanno come le forze che le singole esercitano sulle singole.",
     "en": "The number of the particles being equal, and the situation alike, in both cubes, the forces which all the particles exert, according to the planes FGH, fgh, upon all, are as the forces which each exerts on each.",
     "dipende_da": [],
     "figura": {
      "mostra": [
       "coppie di particelle a cavallo dei piani mediani"
      ],
      "evidenzia": [
       "stesso numero di coppie"
      ]
     }
    },
    {
     "id": "L2-P23-p7",
     "la": "",
     "it": "Dunque le forze che le singole esercitano sulle singole secondo il piano FGH nel cubo maggiore stanno alle forze che le singole esercitano sulle singole secondo il piano fgh nel cubo minore come ab sta ad AB, cioè inversamente come le distanze delle particelle fra loro. C.V.D.",
     "en": "Therefore the forces which each exerts on each, according to the plane FGH in the greater cube, are to the forces which each exerts on each, according to the plane fgh in the lesser cube, as ab to AB, that is, reciprocally as the distances of the particles from each other.",
     "dipende_da": [],
     "figura": {
      "mostra": [],
      "evidenzia": [
       "forza fra particelle ∝ 1/distanza"
      ]
     },
     "nota": "Verifica numerica in N10."
    },
    {
     "id": "L2-P23-p8",
     "la": "",
     "it": "E viceversa, se le forze delle singole particelle sono inversamente come le distanze, cioè inversamente come i lati dei cubi AB, ab, le somme delle forze staranno nello stesso rapporto, e le pressioni dei lati DB, db come le somme delle forze; e la pressione del quadrato DP starà alla pressione del lato DB come ab² sta ad AB².",
     "en": "And, vice versa, if the forces of the single particles are reciprocally as the distances, that is, reciprocally as the sides of the cubes AB, ab; the sums of the forces will be in the same ratio, and the pressures of the sides DB, db as the sums of the forces; and the pressure of the square DP to the pressure of the side DB as ab2 to AB2.",
     "dipende_da": [],
     "figura": {
      "mostra": [],
      "evidenzia": [
       "inverso: forza ∝ 1/distanza"
      ]
     }
    },
    {
     "id": "L2-P23-p9",
     "la": "",
     "it": "E, ex æquo, la pressione del quadrato DP starà alla pressione del lato db come ab³ sta ad AB³, cioè la forza di compressione starà alla forza di compressione come la densità sta alla densità. C.V.D.",
     "en": "And, ex æquo, the pressure of the square DP to the pressure of the side db as ab3 to AB3; that is, the force of compression in the one to the force of compression in the other as the density in the former to the density in the latter.",
     "dipende_da": [],
     "figura": {
      "mostra": [],
      "evidenzia": [
       "compressione ∝ densità (legge di Boyle)"
      ]
     },
     "nota": "Motte esplicita «in the one … in the other», «in the former … in the latter»."
    }
   ]
  }
 ]
}
```
