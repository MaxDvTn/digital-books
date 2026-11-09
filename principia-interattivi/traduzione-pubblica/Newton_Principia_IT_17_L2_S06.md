> **Copia pubblica.** In questa versione i campi `"la"` della Parte B sono vuoti: le frasi latine vengono dalla trascrizione del Newton Project, che non si ridistribuisce. Il latino del 1726 si legge su newtonproject.ox.ac.uk.

# Isaac Newton
# Principi matematici della filosofia naturale

## Fascicolo 17 — Libro II, Sezione VI: il moto e la resistenza dei corpi appesi a un filo

**Nuova traduzione italiana di lavoro dal latino del 1726, confrontata con l’inglese di Andrew Motte nell’edizione del 1846.**

Versione 0.1 — 8 novembre 2026. Preparata con Claude (Anthropic) per Massimo Bosetti.

### Stato e perimetro

Questo fascicolo traduce integralmente la **Sezione VI** del Libro II, *De motu & resistentia corporum funependulorum*: le Proposizioni XXIV–XXXI con tutti i corollari e lo **Scolio generale** che chiude la Sezione, con gli esperimenti sui pendoli nell’aria, nell’acqua e nel mercurio, le cinque tabelle numeriche e l’esperimento della scatola piena e vuota. È una traduzione di lavoro, non un’edizione critica validata.

Gli identificatori **II.S6.01–II.S6.65** e i titoli tematici tra parentesi sono aggiunte editoriali. I numeri romani delle proposizioni, dei teoremi e dei problemi, e i numeri dei corollari, appartengono al testo originale. Le integrazioni del curatore sono tra parentesi quadre. Le note poste dopo la traduzione non fanno parte del testo di Newton.

In coda al fascicolo c’è la **Parte B**, con i dati strutturati per le pagine interattive di 6 unità con figura: Propp. XXV, XXVIII, XXIX, XXX (con il suo corollario, che ha una dimostrazione propria sulla stessa figura) e XXXI.

### Fonti effettivamente consultate

1. **Latino di riferimento.** Isaac Newton, *Philosophiæ Naturalis Principia Mathematica*, terza edizione, Londra, 1726, Libro II, Sezione VI, **pp. 294–317** (i marcatori della trascrizione vanno da ‹295› a ‹317›; ‹318› apre la Sezione VII). Trascrizione normalizzata del Newton Project, documento **NATP00088**, estratta in testo semplice senza correzioni: `fonti/latino-1726-L2-S06.md`. Figure citate: NATP00088-44…50 (non viste).
2. **Inglese di confronto.** *Newton’s Principia*, traduzione di Andrew Motte, New York, Daniel Adee, 1846, Section VI. Estratto: `fonti/motte-1846-L2-S06.md`. L’estratto non conserva i marcatori di pagina: per Motte si cita la «sezione corrispondente». Le 119 formule stampate come immagini (`[SVG 618]`–`[SVG 731]` e `[SVG 208]`, `[SVG 225]`–`[SVG 228]`) sono state rese con `rsvg-convert` dall’EPUB Gutenberg n. 76404 (cartella `OEBPS`, resa disponibile dal coordinatore durante il lavoro) e lette tutte, una per una.
3. **Brief comune**, addendum del Libro II, **Fascicolo 3** (modello di formato) e **Fascicolo 5** (modello di fascicolo di Sezione); **Fascicolo 9** per i rimandi alla Prop. LII del Libro I; la trascrizione della Sezione V (`fonti/latino-1726-L2-S05.md`) per il rimando del Cor. 6 della Prop. XXIV e quella della Sezione II per il Lemma II.

Non ho consultato né riprodotto traduzioni moderne. Non ho potuto vedere la stampa del 1726, né Motte 1729, né le figure originali: le relazioni geometriche sono ricostruite dalle sole lettere del testo.

### Criteri di traduzione

- Il testo guida è il latino; l’inglese di Motte serve a controllare le interpretazioni ed è annotato quando aggiunge, omette o si discosta.
- Si applicano il **glossario comune** del brief e il **glossario del Libro II** (addendum): *resistentia* «resistenza», *medium* «mezzo», *in ratione velocitatis* «in rapporto alla velocità», *in duplicata ratione velocitatis* «in rapporto duplicato della velocità», *medium non resistens* «mezzo non resistente», *vacuum* «vuoto», *oscillatio* «oscillazione», *cyclois* «cicloide», *pendulum* «pendolo», *hyperbola* «iperbole», *asymptotos* «asintoto», *area hyperbolica* «area iperbolica», *gravitas specifica* «gravità specifica», *pondus* «peso», *globus* «globo», *pes* «piede», *digitus* «pollice», *uncia* «oncia», *libra* «libbra», *argentum vivum* «mercurio (argento vivo)» alla prima occorrenza, *aqua pluvialis* «acqua piovana», *experimentum* «esperimento», *vis insita* «forza insita», *momentum* «momento»; dal Libro I: *funependulum* «pendolo a filo», *corpus funependulum* «corpo appeso a un filo», *sinus versus* «seno verso», *ordinatim applicata* «ordinata», *conjunctim* «considerati congiuntamente», *ex æquo (perturbate)* «per uguaglianza (perturbata)», *divisim* «separando», *ducere in* «moltiplicare per», *exponens* «esponente», *quam proxime* «con ottima approssimazione», Q.E.D. «C.V.D.».
- Le estensioni del glossario proprie di questo fascicolo sono nel § A.0.
- Gli enunciati latini all’infinito o al congiuntivo sono resi con l’indicativo; l’enunciato del Problema VI conserva l’infinito («trovare»).
- **Formule e numeri.** Le frazioni appiattite della trascrizione sono ricostruite e dichiarate nell’apparato (§ A.13): «57722» = 57 7/22, «OROQIEF» = (OR/OQ) × IEF, «12Ba» = ½Ba, «711Aa» = 7/11 Aa. Le frazioni comuni si scrivono con i caratteri Unicode (½, ¾, ⅔, ⅛…), le altre con la barra (7/22, 1/656). L’esponente frazionario di Newton, V con apice 3/2, è scritto **V^(3/2)**, perché Unicode non ha un apice frazionario affidabile; i quadrati sono V². I numeri decimali conservano la virgola dell’originale (0,0000916). Nel testo non entrano formule moderne.
- Nella Prop. XXVII Newton chiama A e B gli archi e scrive «AA», «AB», «BB» per i loro prodotti: la notazione è conservata.
- **Tabelle.** Le cinque tabelle numeriche dello Scolio generale sono riprodotte per intero in Markdown, con i valori letti dalla trascrizione (letture in § A.13) e confermati sulle formule SVG di Motte. Le cifre che non tornano sono segnalate in nota (N11–N16) e **non** sono corrette nel testo.
- Quando una forma è chiaramente un refuso (della trascrizione o della stampa), la traduzione segue il senso e il punto è annotato in § A.13 e nei «Punti da controllare sulla stampa ECCO».

---

## Traduzione italiana

### Sezione VI. Il moto e la resistenza dei corpi appesi a un filo

### Proposizione XXIV. Teorema XIX (quantità di materia e peso dei pendoli)

**[II.S6.01]** **Le quantità di materia nei corpi appesi a un filo, i cui centri di oscillazione distano ugualmente dal centro di sospensione, sono nel rapporto composto dal rapporto dei pesi e dal rapporto duplicato dei tempi delle oscillazioni nel vuoto.**

**[II.S6.02]** Infatti la velocità che una forza data può generare in una materia data in un tempo dato è come la forza e il tempo, direttamente, e come la materia, inversamente. Quanto maggiore è la forza o il tempo, o quanto minore è la materia, tanto maggiore sarà la velocità generata. Ciò è manifesto per la seconda legge del moto. Ora, se i pendoli hanno la stessa lunghezza, le forze motrici in luoghi ugualmente distanti dalla perpendicolare sono come i pesi; e perciò, se due corpi oscillando descrivono archi uguali e quegli archi si dividono in parti uguali, poiché i tempi in cui i corpi descrivono le singole parti corrispondenti degli archi sono come i tempi delle oscillazioni intere, le velocità nelle parti corrispondenti delle oscillazioni staranno fra loro come le forze motrici e i tempi interi delle oscillazioni, direttamente, e come le quantità di materia, inversamente; e quindi le quantità di materia staranno come le forze e i tempi delle oscillazioni, direttamente, e come le velocità, inversamente. Ma le velocità, inversamente, sono come i tempi; e perciò i tempi, direttamente, e le velocità, inversamente, sono come i quadrati dei tempi; e quindi le quantità di materia sono come le forze motrici e i quadrati dei tempi, cioè come i pesi e i quadrati dei tempi. C.V.D.

**[II.S6.03]** *Cor. 1.* Perciò, se i tempi sono uguali, le quantità di materia nei singoli corpi saranno come i pesi.

**[II.S6.04]** *Cor. 2.* Se i pesi sono uguali, le quantità di materia saranno come i quadrati dei tempi.

**[II.S6.05]** *Cor. 3.* Se le quantità di materia sono uguali, i pesi saranno inversamente come i quadrati dei tempi.

**[II.S6.06]** *Cor. 4.* Di qui, poiché i quadrati dei tempi, a parità delle altre condizioni, sono come le lunghezze dei pendoli, se sia i tempi sia le quantità di materia sono uguali, i pesi saranno come le lunghezze dei pendoli.

**[II.S6.07]** *Cor. 5.* E in generale la quantità di materia del corpo pendolo è come il peso e il quadrato del tempo, direttamente, e come la lunghezza del pendolo, inversamente.

**[II.S6.08]** *Cor. 6.* Ma anche in un mezzo non resistente la quantità di materia del corpo pendolo è come il peso comparativo e il quadrato del tempo, direttamente, e come la lunghezza del pendolo, inversamente. Il peso comparativo, infatti, è la forza motrice del corpo in un mezzo pesante qualsiasi, come ho spiegato sopra; e perciò in un tale mezzo non resistente produce lo stesso effetto che il peso assoluto produce nel vuoto.

**[II.S6.09]** *Cor. 7.* E di qui è chiaro il modo sia di confrontare i corpi fra loro quanto alla quantità di materia di ciascuno, sia di confrontare i pesi dello stesso corpo in luoghi diversi, per conoscere la variazione della gravità. Eseguiti poi esperimenti quanto più accurati possibile, ho sempre trovato che la quantità di materia nei singoli corpi è proporzionale al loro peso.

### Proposizione XXV. Teorema XX (resistenza costante: isocronismo nella cicloide)

**[II.S6.10]** **I corpi appesi a un filo che, in un mezzo qualsiasi, incontrano una resistenza in rapporto ai momenti del tempo, e i corpi appesi a un filo che si muovono in un mezzo non resistente della stessa gravità specifica, compiono le oscillazioni nella cicloide nello stesso tempo e descrivono insieme parti proporzionali degli archi.**

**[II.S6.11]** Sia AB un arco di cicloide che il corpo D, oscillando in un mezzo non resistente, descrive in un tempo qualsiasi. Lo si divida a metà in C, in modo che C sia il suo punto più basso; la forza acceleratrice da cui il corpo è sollecitato in un luogo qualsiasi D, d o E sarà come la lunghezza dell’arco CD, Cd o CE. Si rappresenti quella forza con lo stesso arco; e poiché la resistenza è come il momento del tempo, e quindi è data, la si rappresenti con la parte data CO dell’arco di cicloide, e si prenda l’arco Od in modo che stia all’arco CD nel rapporto che l’arco OB ha con l’arco CB. La forza da cui il corpo è sollecitato in d nel mezzo resistente, essendo l’eccesso della forza Cd sulla resistenza CO, sarà rappresentata dall’arco Od; e perciò starà alla forza da cui il corpo D è sollecitato nel mezzo non resistente, nel luogo D, come l’arco Od sta all’arco CD; e quindi anche nel luogo B come l’arco OB sta all’arco CB. Se dunque due corpi D, d partono dal luogo B e sono sollecitati da queste forze, poiché all’inizio le forze sono come gli archi CB e OB, le velocità iniziali e gli archi descritti per primi staranno nello stesso rapporto. Siano BD e Bd quegli archi: anche gli archi restanti CD, Od staranno nello stesso rapporto. Perciò le forze, proporzionali a CD e Od, resteranno nello stesso rapporto che all’inizio, e quindi i corpi continueranno a descrivere insieme archi nello stesso rapporto. Dunque le forze, le velocità e gli archi restanti CD, Od staranno sempre come gli archi interi CB, OB, e perciò quegli archi restanti saranno descritti insieme. I due corpi D, d giungeranno quindi insieme ai luoghi C e O: l’uno, nel mezzo non resistente, al luogo C; l’altro, nel mezzo resistente, al luogo O. Poiché poi le velocità in C e in O sono come gli archi CB, OB, gli archi che i corpi descrivono insieme procedendo oltre staranno nello stesso rapporto. Siano questi CE e Oe. La forza da cui il corpo D, nel mezzo non resistente, è ritardato in E è come CE; e la forza da cui il corpo d, nel mezzo resistente, è ritardato in e è come la somma della forza Ce e della resistenza CO, cioè come Oe. Perciò le forze da cui i corpi sono ritardati stanno come gli archi CB, OB, proporzionali agli archi CE, Oe; e quindi le velocità, ritardate in quel rapporto dato, restano in quello stesso rapporto dato. Le velocità, dunque, e gli archi descritti con esse stanno sempre fra loro nel rapporto dato degli archi CB e OB; e perciò, se si prendono gli archi interi AB, aB nello stesso rapporto, i corpi D, d descriveranno insieme questi archi e perderanno insieme tutto il loro moto nei luoghi A e a. Le oscillazioni intere sono dunque isocrone, e parti qualsiasi degli archi, BD, Bd o BE, Be, descritte insieme, sono proporzionali agli archi interi BA, Ba. C.V.D.

**[II.S6.12]** *Cor.* Dunque nel mezzo resistente il moto più veloce non cade nel punto più basso C, ma si trova in quel punto O nel quale è diviso a metà l’intero arco descritto aB. E il corpo, procedendo poi verso a, è ritardato con gli stessi gradi con cui prima era accelerato nella sua discesa da B a O.

### Proposizione XXVI. Teorema XXI (resistenza in rapporto alla velocità: isocronismo)

**[II.S6.13]** **Le oscillazioni nella cicloide dei corpi appesi a un filo, che incontrano una resistenza in rapporto alle velocità, sono isocrone.**

**[II.S6.14]** Se infatti due corpi, ugualmente distanti dai centri di sospensione, oscillando descrivono archi disuguali, e le velocità nelle parti corrispondenti degli archi stanno fra loro come gli archi interi, anche le resistenze, proporzionali alle velocità, staranno fra loro come gli stessi archi. Perciò, se alle forze motrici nate dalla gravità, che sono come gli stessi archi, si tolgono o si aggiungono queste resistenze, le differenze o le somme staranno fra loro nello stesso rapporto degli archi; e poiché gli incrementi o i decrementi delle velocità sono come queste differenze o somme, le velocità saranno sempre come gli archi interi. Dunque le velocità, se in qualche caso sono come gli archi interi, resteranno sempre nello stesso rapporto. Ma al principio del moto, quando i corpi cominciano a scendere e a descrivere quegli archi, le forze, essendo proporzionali agli archi, genereranno velocità proporzionali agli archi. Dunque le velocità saranno sempre come gli archi interi da descrivere, e perciò quegli archi saranno descritti insieme. C.V.D.

### Proposizione XXVII. Teorema XXII (resistenza in rapporto duplicato della velocità: eccesso dei tempi)

**[II.S6.15]** **Se i corpi appesi a un filo incontrano una resistenza in rapporto duplicato delle velocità, le differenze fra i tempi delle oscillazioni nel mezzo resistente e i tempi delle oscillazioni in un mezzo non resistente della stessa gravità specifica saranno proporzionali agli archi descritti oscillando, con ottima approssimazione.**

**[II.S6.16]** Infatti pendoli uguali descrivano nel mezzo resistente archi disuguali A, B: la resistenza del corpo nell’arco A starà alla resistenza del corpo nella parte corrispondente dell’arco B in rapporto duplicato delle velocità, cioè come AA sta a BB, con ottima approssimazione. Se la resistenza nell’arco B stesse alla resistenza nell’arco A come AB sta ad AA, i tempi negli archi A e B sarebbero uguali, per la proposizione precedente. Perciò la resistenza AA nell’arco A, o AB nell’arco B, produce l’eccesso del tempo nell’arco A sul tempo nel mezzo non resistente; e la resistenza BB produce l’eccesso del tempo nell’arco B sul tempo nel mezzo non resistente. Ma quegli eccessi sono come le forze che li producono, AB e BB, con ottima approssimazione, cioè come gli archi A e B. C.V.D.

**[II.S6.17]** *Cor. 1.* Di qui, dai tempi delle oscillazioni compiute in archi disuguali nel mezzo resistente, si possono conoscere i tempi delle oscillazioni in un mezzo non resistente della stessa gravità specifica. La differenza dei tempi starà infatti all’eccesso del tempo nell’arco minore sul tempo nel mezzo non resistente come la differenza degli archi sta all’arco minore.

**[II.S6.18]** *Cor. 2.* Le oscillazioni più brevi sono più isocrone, e le brevissime si compiono, con ottima approssimazione, negli stessi tempi che nel mezzo non resistente. I tempi di quelle che si compiono in archi maggiori sono invece un poco maggiori, perché la resistenza nella discesa del corpo, dalla quale il tempo è allungato, è maggiore, in proporzione alla lunghezza descritta nella discesa, della resistenza nella salita successiva, dalla quale il tempo è accorciato. Ma sembra che il tempo delle oscillazioni, sia brevi sia lunghe, sia anche allungato in qualche misura dal moto del mezzo. Ai corpi che rallentano, infatti, si oppone una resistenza un poco minore, in proporzione alla velocità, e ai corpi accelerati un poco maggiore che a quelli che procedono uniformemente; e ciò perché il mezzo, con il moto che ha ricevuto dai corpi, procedendo verso la stessa parte, nel primo caso è più agitato, nel secondo meno, e quindi concorda più o meno con i corpi in moto. Perciò ai pendoli resiste di più nella discesa e di meno nella salita di quanto comporterebbe il rapporto della velocità; e per entrambe le cause il tempo è allungato.

### Proposizione XXVIII. Teorema XXIII (resistenza costante misurata dalla differenza degli archi)

**[II.S6.19]** **Se un corpo appeso a un filo, che oscilla in una cicloide, incontra una resistenza in rapporto ai momenti del tempo, la sua resistenza starà alla forza di gravità come l’eccesso dell’arco descritto nell’intera discesa sull’arco descritto nella salita successiva sta al doppio della lunghezza del pendolo.**

**[II.S6.20]** BC indichi l’arco descritto nella discesa, Ca l’arco descritto nella salita e Aa la differenza degli archi; e, ferme restando la costruzione e la dimostrazione della Prop. XXV, la forza da cui il corpo oscillante è sollecitato in un luogo qualsiasi D starà alla forza della resistenza come l’arco CD sta all’arco CO, che è la metà di quella differenza Aa. Perciò la forza da cui il corpo oscillante è sollecitato all’inizio della cicloide, cioè nel suo punto più alto, ossia la forza di gravità, starà alla resistenza come l’arco di cicloide compreso fra quel punto più alto e il punto più basso C sta all’arco CO; cioè (se si raddoppiano gli archi) come l’arco dell’intera cicloide, ossia il doppio della lunghezza del pendolo, sta all’arco Aa. C.V.D.

### Proposizione XXIX. Problema VI (resistenza in rapporto duplicato della velocità: costruzione con l’iperbole)

**[II.S6.21]** **Supposto che un corpo che oscilla in una cicloide incontri una resistenza in rapporto duplicato della velocità, trovare la resistenza nei singoli luoghi.**

**[II.S6.22]** Sia Ba l’arco descritto in un’oscillazione intera, C il punto più basso della cicloide e CZ la metà dell’arco dell’intera cicloide, uguale alla lunghezza del pendolo; e si cerchi la resistenza del corpo in un luogo qualsiasi D. Si tagli la retta infinita OQ nei punti O, S, P, Q con questa legge: se si innalzano le perpendicolari OK, ST, PI, QE, e con centro O e asintoti OK, OQ si descrive l’iperbole TIGE, che tagli le perpendicolari ST, PI, QE in T, I ed E, e per il punto I si conduce KF parallela all’asintoto OQ, che incontri l’asintoto OK in K e le perpendicolari ST e QE in L e F, l’area iperbolica PIEQ stia all’area iperbolica PITS come l’arco BC descritto nella discesa del corpo sta all’arco Ca descritto nella salita, e l’area IEF stia all’area ILT come OQ sta a OS. Poi con la perpendicolare MN si stacchi l’area iperbolica PINM, che stia all’area iperbolica PIEQ come l’arco CZ sta all’arco BC descritto nella discesa. E se con la perpendicolare RG si stacca l’area iperbolica PIGR, che stia all’area PIEQ come un arco qualsiasi CD sta all’arco BC descritto nell’intera discesa, la resistenza nel luogo D starà alla forza di gravità come l’area (OR/OQ) × IEF − IGH sta all’area PINM.

**[II.S6.23]** Poiché infatti le forze nate dalla gravità da cui il corpo è sollecitato nei luoghi Z, B, D, a sono come gli archi CZ, CB, CD, Ca, e quegli archi sono come le aree PINM, PIEQ, PIGR, PITS, si rappresentino rispettivamente con queste aree sia gli archi sia le forze. Sia inoltre Dd uno spazio piccolissimo descritto dal corpo che scende, e lo si rappresenti con l’area piccolissima RGgr compresa fra le parallele RG, rg; e si prolunghi rg fino a h, in modo che GHhg e RGgr siano i decrementi contemporanei delle aree IGH, PIGR. E l’incremento dell’area (OR/OQ) × IEF − IGH, cioè GHhg − (Rr/OQ) × IEF, ossia Rr × HG − (Rr/OQ) × IEF, starà al decremento RGgr dell’area PIGR, ossia Rr × RG, come HG − IEF/OQ sta a RG; e perciò come OR × HG − (OR/OQ) × IEF sta a OR × GR, ossia a OP × PI, cioè (poiché sono uguali OR × HG, OR × HR − OR × GR, ORHK − OPIK, PIHR e PIGR + IGH) come PIGR + IGH − (OR/OQ) × IEF sta a OPIK. Se dunque l’area (OR/OQ) × IEF − IGH si chiama Y, e il decremento RGgr dell’area PIGR è dato, l’incremento dell’area Y sarà come PIGR − Y.

**[II.S6.24]** Se poi V indica la forza nata dalla gravità, proporzionale all’arco da descrivere CD, da cui il corpo è sollecitato in D, e R si pone per la resistenza, V − R sarà la forza totale da cui il corpo è sollecitato in D. L’incremento della velocità è quindi come V − R e la particella di tempo in cui è avvenuto, considerate congiuntamente; ma anche la velocità stessa è come l’incremento contemporaneo dello spazio descritto, direttamente, e la stessa particella di tempo, inversamente. Perciò, poiché per ipotesi la resistenza è come il quadrato della velocità, l’incremento della resistenza (per il Lemma II) sarà come la velocità e l’incremento della velocità considerati congiuntamente, cioè come il momento dello spazio e V − R considerati congiuntamente; e quindi, se il momento dello spazio è dato, come V − R; cioè, se al posto della forza V si scrive il suo esponente PIGR e la resistenza R si rappresenta con un’altra area Z, come PIGR − Z.

**[II.S6.25]** Mentre dunque l’area PIGR decresce uniformemente per la sottrazione di momenti dati, l’area Y cresce in rapporto a PIGR − Y e l’area Z in rapporto a PIGR − Z. E perciò, se le aree Y e Z cominciano insieme e all’inizio sono uguali, per l’aggiunta di momenti uguali continueranno a essere uguali e, decrescendo poi anch’esse per momenti uguali, svaniranno insieme. E viceversa, se cominciano insieme e svaniscono insieme, avranno momenti uguali e saranno sempre uguali: e ciò perché, se la resistenza Z aumenta, la velocità diminuirà insieme con l’arco Ca descritto nella salita del corpo; e, avvicinandosi al punto C il punto in cui cessa tutto il moto insieme con la resistenza, la resistenza svanirà prima dell’area Y. E il contrario avverrà quando la resistenza diminuisce.

**[II.S6.26]** Ora, l’area Z comincia e finisce dove la resistenza è nulla, cioè all’inizio del moto, dove l’arco CD è uguale all’arco CB e la retta RG cade sulla retta QE, e alla fine del moto, dove l’arco CD è uguale all’arco Ca e RG cade sulla retta ST. E l’area Y, ossia (OR/OQ) × IEF − IGH, comincia e finisce dove è nulla, e quindi dove (OR/OQ) × IEF e IGH sono uguali: cioè (per la costruzione) dove la retta RG cade successivamente sulle rette QE e ST. Perciò quelle aree cominciano insieme e svaniscono insieme, e quindi sono sempre uguali. Dunque l’area (OR/OQ) × IEF − IGH è uguale all’area Z, con cui si rappresenta la resistenza, e perciò sta all’area PINM, con cui si rappresenta la gravità, come la resistenza sta alla gravità. C.V.D.

**[II.S6.27]** *Cor. 1.* La resistenza nel luogo più basso C sta dunque alla forza di gravità come l’area (OP/OQ) × IEF sta all’area PINM.

**[II.S6.28]** *Cor. 2.* Essa diventa poi massima dove l’area PIHR sta all’area IEF come OR sta a OQ. In quel caso, infatti, il suo momento (cioè PIGR − Y) si annulla.

**[II.S6.29]** *Cor. 3.* Di qui si conosce anche la velocità nei singoli luoghi, poiché essa è in rapporto subduplicato della resistenza e, proprio all’inizio del moto, è uguale alla velocità del corpo che oscilla nella stessa cicloide senza alcuna resistenza.

**[II.S6.30]** Del resto, a causa della difficoltà del calcolo con cui per mezzo di questa proposizione si devono trovare la resistenza e la velocità, mi è parso opportuno aggiungere la proposizione seguente.

### Proposizione XXX. Teorema XXIV (l’area delle resistenze e la differenza degli archi)

**[II.S6.31]** **Se la retta aB è uguale all’arco di cicloide che il corpo descrive oscillando, e nei suoi singoli punti D si innalzano le perpendicolari DK, che stiano alla lunghezza del pendolo come la resistenza del corpo nei punti corrispondenti dell’arco sta alla forza di gravità, dico che la differenza fra l’arco descritto nell’intera discesa e l’arco descritto nell’intera salita successiva, moltiplicata per la semisomma degli stessi archi, sarà uguale all’area BKa occupata da tutte le perpendicolari DK.**

**[II.S6.32]** Si rappresenti infatti l’arco di cicloide descritto in un’oscillazione intera con quella retta aB a esso uguale, e l’arco che sarebbe descritto nel vuoto con la lunghezza AB. Si divida AB a metà in C: il punto C rappresenterà il punto più basso della cicloide, e CD sarà come la forza nata dalla gravità da cui il corpo in D è sollecitato lungo la tangente della cicloide, e avrà con la lunghezza del pendolo il rapporto che la forza in D ha con la forza di gravità. Si rappresenti dunque quella forza con la lunghezza CD e la forza di gravità con la lunghezza del pendolo; e se su DE si prende DK nel rapporto con la lunghezza del pendolo che la resistenza ha con la gravità, DK sarà l’esponente della resistenza. Con centro C e raggio CA o CB si costruisca il semicerchio BEeA. Il corpo descriva poi in un tempo piccolissimo lo spazio Dd; e, innalzate le perpendicolari DE, de, che incontrino la circonferenza in E ed e, queste saranno come le velocità che il corpo, scendendo nel vuoto dal punto B, acquisterebbe nei luoghi D e d. Ciò è chiaro (per la Prop. LII del Libro I). Si rappresentino dunque queste velocità con quelle perpendicolari DE, de; e sia DF la velocità che il corpo acquista in D cadendo da B nel mezzo resistente. E se con centro C e raggio CF si descrive il cerchio FfM, che incontri le rette de e AB in f e M, M sarà il luogo al quale il corpo salirebbe in seguito senza ulteriore resistenza, e df la velocità che acquisterebbe in d. Di qui, anche, se Fg indica il momento della velocità che il corpo D, descrivendo lo spazio piccolissimo Dd, perde per la resistenza del mezzo, e si prende CN uguale a Cg, N sarà il luogo al quale il corpo salirebbe in seguito senza ulteriore resistenza, e MN sarà il decremento della salita nato dalla perdita di quella velocità. Si abbassi su df la perpendicolare Fm: il decremento Fg della velocità DF, generato dalla resistenza DK, starà all’incremento fm della stessa velocità, generato dalla forza CD, come la forza generatrice DK sta alla forza generatrice CD. Ma, per i triangoli simili Fmf, Fhg, FDC, fm sta a Fm, ossia a Dd, come CD sta a DF; e, per uguaglianza, Fg sta a Dd come DK sta a DF. Inoltre Fh sta a Fg come DF sta a CF; e, per uguaglianza perturbata, Fh, ossia MN, sta a Dd come DK sta a CF, ossia a CM; e perciò la somma di tutti i prodotti MN × CM sarà uguale alla somma di tutti i prodotti Dd × DK. Si immagini che nel punto mobile M si innalzi sempre un’ordinata perpendicolare uguale all’indeterminata CM, che con moto continuo sia moltiplicata per l’intera lunghezza Aa: il trapezio descritto da quel moto, ossia il rettangolo a esso uguale Aa × ½aB, sarà uguale alla somma di tutti i prodotti MN × CM, e quindi alla somma di tutti i prodotti Dd × DK, cioè all’area BKVTa. C.V.D.

**[II.S6.33]** *Cor.* Di qui, dalla legge della resistenza e dalla differenza Aa degli archi Ca, CB, si può ricavare con ottima approssimazione il rapporto della resistenza alla gravità.

**[II.S6.34]** Se infatti la resistenza DK è uniforme, la figura BKTa sarà un rettangolo contenuto sotto Ba e DK; e quindi il rettangolo contenuto sotto ½Ba e Aa sarà uguale al rettangolo contenuto sotto Ba e DK, e DK sarà uguale a ½Aa. Perciò, poiché DK è l’esponente della resistenza e la lunghezza del pendolo è l’esponente della gravità, la resistenza starà alla gravità come ½Aa sta alla lunghezza del pendolo, esattamente come si è dimostrato nella Prop. XXVIII.

**[II.S6.35]** Se la resistenza è come la velocità, la figura BKTa sarà con ottima approssimazione un’ellisse. Infatti, se il corpo in un mezzo non resistente descrivesse in un’oscillazione intera la lunghezza BA, la velocità in un luogo qualsiasi D sarebbe come l’ordinata DE del cerchio descritto sul diametro AB. Perciò, poiché Ba nel mezzo resistente e BA nel mezzo non resistente sono descritte in tempi circa uguali, e quindi le velocità nei singoli punti di Ba stanno con ottima approssimazione alle velocità nei punti corrispondenti della lunghezza BA come Ba sta a BA, la velocità nel punto D nel mezzo resistente sarà come l’ordinata del cerchio o dell’ellisse descritti sul diametro Ba; e perciò la figura BKVTa sarà con ottima approssimazione un’ellisse. Poiché si suppone la resistenza proporzionale alla velocità, sia OV l’esponente della resistenza nel punto medio O; l’ellisse BRVSa, descritta con centro O e semiassi OB, OV, sarà con ottima approssimazione uguale alla figura BKVTa e al rettangolo Aa × BO, che le è uguale. Dunque Aa × BO sta a OV × BO come l’area di questa ellisse sta a OV × BO: cioè Aa sta a OV come l’area del semicerchio sta al quadrato del raggio, ossia circa come 11 sta a 7; e perciò 7/11 Aa sta alla lunghezza del pendolo come la resistenza del corpo oscillante in O sta alla sua gravità.

**[II.S6.36]** Se poi la resistenza DK è in rapporto duplicato della velocità, la figura BKVTa sarà quasi una parabola con vertice V e asse OV, e perciò sarà con ottima approssimazione uguale al rettangolo contenuto sotto ⅔Ba e OV. Il rettangolo contenuto sotto ½Ba e Aa è dunque uguale al rettangolo contenuto sotto ⅔Ba e OV, e quindi OV è uguale a ¾Aa; e perciò la resistenza del corpo oscillante in O sta alla sua gravità come ¾Aa sta alla lunghezza del pendolo.

**[II.S6.37]** E ritengo che queste conclusioni siano, nelle applicazioni pratiche, più che sufficientemente accurate. Infatti, poiché l’ellisse o la parabola BRVSa coincide con la figura BKVTa nel punto medio V, se da una delle due parti, BRV o VSa, supera quella figura, dall’altra parte ne resterà al di sotto, e così le sarà con ottima approssimazione uguale.

### Proposizione XXXI. Teorema XXV (la differenza degli archi è come la resistenza)

**[II.S6.38]** **Se la resistenza di un corpo oscillante, nelle singole parti proporzionali degli archi descritti, aumenta o diminuisce in un rapporto dato, la differenza fra l’arco descritto nella discesa e l’arco descritto nella salita successiva aumenterà o diminuirà nello stesso rapporto.**

**[II.S6.39]** Quella differenza nasce infatti dal ritardo del pendolo dovuto alla resistenza del mezzo, e perciò è come il ritardo totale e come la resistenza ritardatrice, che gli è proporzionale. Nella proposizione precedente il rettangolo contenuto sotto la retta ½aB e la differenza Aa di quegli archi CB, Ca era uguale all’area BKTa. E quell’area, se la lunghezza aB resta la stessa, aumenta o diminuisce nel rapporto delle ordinate DK, cioè nel rapporto della resistenza, e quindi è come la lunghezza aB e la resistenza considerate congiuntamente. Perciò il rettangolo contenuto sotto Aa e ½aB è come aB e la resistenza considerate congiuntamente, e quindi Aa è come la resistenza. C.V.D.

**[II.S6.40]** *Cor. 1.* Di qui, se la resistenza è come la velocità, la differenza degli archi nello stesso mezzo sarà come l’arco intero descritto; e viceversa.

**[II.S6.41]** *Cor. 2.* Se la resistenza è in rapporto duplicato della velocità, quella differenza sarà in rapporto duplicato dell’arco intero; e viceversa.

**[II.S6.42]** *Cor. 3.* E in generale, se la resistenza è in rapporto triplicato o in un altro rapporto qualsiasi della velocità, la differenza sarà nello stesso rapporto dell’arco intero; e viceversa.

**[II.S6.43]** *Cor. 4.* E se la resistenza è in parte in rapporto semplice della velocità, in parte in rapporto duplicato della stessa, la differenza sarà in parte nel rapporto dell’arco intero e in parte nel suo rapporto duplicato; e viceversa. La legge e il rapporto della resistenza rispetto alla velocità saranno gli stessi della legge e del rapporto di quella differenza rispetto alla lunghezza dell’arco.

**[II.S6.44]** *Cor. 5.* E perciò se, mentre il pendolo descrive successivamente archi disuguali, si può trovare il rapporto dell’incremento e del decremento di questa differenza rispetto alla lunghezza dell’arco descritto, si avrà anche il rapporto dell’incremento e del decremento della resistenza rispetto a una velocità maggiore o minore.

### Scolio generale

#### 1. La resistenza dell’aria: il globo di legno

**[II.S6.45]** Da queste proposizioni si può trovare, per mezzo delle oscillazioni dei pendoli in mezzi qualsiasi, la resistenza dei mezzi. La resistenza dell’aria, poi, l’ho indagata con gli esperimenti seguenti. Ho sospeso con un filo sottile a un gancio abbastanza saldo un globo di legno del peso di 57 7/22 once romane, costruito con un diametro di 6⅞ pollici londinesi, in modo che fra il gancio e il centro di oscillazione del globo vi fosse una distanza di 10½ piedi. Sul filo ho segnato un punto distante dieci piedi e un pollice dal centro di sospensione; e di fronte a quel punto ho collocato un regolo diviso in pollici, per mezzo del quale annotare le lunghezze degli archi descritti dal pendolo. Poi ho contato le oscillazioni in cui il globo perdeva l’ottava parte del suo moto. Se il pendolo veniva allontanato dalla perpendicolare fino alla distanza di due pollici e di lì veniva lasciato andare, così che in tutta la sua discesa descriveva un arco di due pollici e in tutta la prima oscillazione, composta dalla discesa e dalla salita successiva, un arco di quasi quattro pollici, esso perdeva l’ottava parte del suo moto in 164 oscillazioni, così che nella sua ultima salita descriveva un arco di un pollice e tre quarti di pollice. Se nella prima discesa descriveva un arco di quattro pollici, perdeva l’ottava parte del moto in 121 oscillazioni, così che nell’ultima salita descriveva un arco di 3½ pollici. Se nella prima discesa descriveva un arco di otto, sedici, trentadue o sessantaquattro pollici, perdeva l’ottava parte del moto rispettivamente in 69, 35½, 18½, 9⅔ oscillazioni. Dunque la differenza fra gli archi descritti nella prima discesa e nell’ultima salita era, nel primo, secondo, terzo, quarto, quinto e sesto caso, rispettivamente di ¼, ½, 1, 2, 4, 8 pollici.

**[II.S6.46]** Si dividano queste differenze per il numero delle oscillazioni in ciascun caso: in un’oscillazione media, nella quale si descriveva un arco di 3¾, 7½, 15, 30, 60, 120 pollici, la differenza degli archi descritti nella discesa e nella salita successiva sarà rispettivamente di 1/656, 1/242, 1/69, 4/71, 8/37, 24/29 parti di pollice. Nelle oscillazioni maggiori, poi, queste differenze sono con ottima approssimazione in rapporto duplicato degli archi descritti, nelle minori invece un poco maggiori che in quel rapporto; e perciò (per il Cor. 2 della Prop. XXXI di questo Libro) la resistenza del globo, quando si muove più velocemente, è con ottima approssimazione in rapporto duplicato della velocità; quando più lentamente, un poco maggiore che in quel rapporto.

**[II.S6.47]** Indichi ora V la velocità massima in un’oscillazione qualsiasi, siano A, B, C quantità date, e supponiamo che la differenza degli archi sia AV + BV^(3/2) + CV². Le velocità massime sono, nella cicloide, come le metà degli archi descritti oscillando, nel cerchio invece come le corde delle metà di quegli archi; e quindi, a parità di archi, sono maggiori nella cicloide che nel cerchio nel rapporto delle metà degli archi alle loro corde; i tempi nel cerchio sono invece maggiori che nella cicloide in rapporto inverso della velocità. È chiaro dunque che le differenze degli archi (che sono come la resistenza e il quadrato del tempo considerati congiuntamente) saranno, con ottima approssimazione, le stesse nell’una e nell’altra curva: nella cicloide, infatti, quelle differenze dovrebbero aumentare, insieme con la resistenza, circa nel rapporto duplicato dell’arco alla corda, a causa della velocità aumentata in quel rapporto semplice; e diminuire, insieme con il quadrato del tempo, nello stesso rapporto duplicato. Perciò, per ridurre le osservazioni alla cicloide, si devono prendere le stesse differenze degli archi che si erano osservate nel cerchio, e porre invece le velocità massime proporzionali agli archi dimezzati o interi, cioè ai numeri ½, 1, 2, 4, 8, 16. Scriviamo dunque nel secondo, nel quarto e nel sesto caso i numeri 1, 4 e 16 al posto di V: risulterà la differenza degli archi ½/121 = A + B + C nel secondo caso; 2/35½ = 4A + 8B + 16C nel quarto caso; e 8/9⅔ = 16A + 64B + 256C nel sesto caso. Da queste equazioni, con l’opportuno confronto e la riduzione analitica, si ottiene A = 0,0000916, B = 0,0010847 e C = 0,0029558.

**[II.S6.48]** La differenza degli archi è dunque come 0,0000916V + 0,0010847V^(3/2) + 0,0029558V²; e perciò, poiché (per il corollario della Prop. XXX applicato a questo caso) la resistenza del globo nel mezzo dell’arco descritto oscillando, dove la velocità è V, sta al suo peso come 7/11 AV + 7/10 BV^(3/2) + ¾CV² sta alla lunghezza del pendolo, se al posto di A, B e C si scrivono i numeri trovati, la resistenza del globo starà al suo peso come 0,0000583V + 0,0007593V^(3/2) + 0,0022169V² sta alla lunghezza del pendolo fra il centro di sospensione e il regolo, cioè a 121 pollici. Perciò, poiché V nel secondo caso indica 1, nel quarto 4, nel sesto 16, la resistenza starà al peso del globo nel secondo caso come 0,0030345 sta a 121, nel quarto come 0,041748 sta a 121, nel sesto come 0,61705 sta a 121.

**[II.S6.49]** L’arco che il punto segnato sul filo descrisse nel sesto caso era di 120 − 8/9⅔, ossia di 119 5/29 pollici. E perciò, poiché il raggio era di 121 pollici e la lunghezza del pendolo fra il punto di sospensione e il centro del globo era di 126 pollici, l’arco che il centro del globo descrisse era di 124 3/31 pollici. Poiché la velocità massima del corpo oscillante, a causa della resistenza dell’aria, non cade nel punto più basso dell’arco descritto, ma si trova circa nel mezzo dell’arco intero, essa sarà circa la stessa che se il globo, in tutta la sua discesa in un mezzo non resistente, descrivesse la metà di quell’arco, di 62 3/62 pollici, e ciò nella cicloide, alla quale abbiamo sopra ridotto il moto del pendolo; e perciò quella velocità sarà uguale alla velocità che il globo potrebbe acquistare cadendo verticalmente e descrivendo nella sua caduta un’altezza uguale al seno verso di quell’arco. Ma quel seno verso, nella cicloide, sta all’arco di 62 3/62 come lo stesso arco sta al doppio della lunghezza del pendolo, 252, e perciò è uguale a 15,278 pollici. Quella velocità è dunque proprio quella che un corpo potrebbe acquistare cadendo e descrivendo nella sua caduta uno spazio di 15,278 pollici. Con tale velocità, dunque, il globo subisce una resistenza che sta al suo peso come 0,61705 sta a 121, oppure (se si considera soltanto quella parte della resistenza che è in rapporto duplicato della velocità) come 0,56752 sta a 121.

**[II.S6.50]** Con un esperimento idrostatico ho poi trovato che il peso di questo globo di legno stava al peso di un globo d’acqua della stessa grandezza come 55 sta a 97; e perciò, poiché 121 sta a 213,4 nello stesso rapporto, la resistenza del globo d’acqua che avanzi con la velocità predetta starà al suo peso come 0,56752 sta a 213,4, cioè come 1 sta a 376 1/50. Di qui, poiché il peso del globo d’acqua, nel tempo in cui il globo, con la velocità mantenuta uniformemente, descriverebbe una lunghezza di 30,556 pollici, potrebbe generare tutta quella velocità nel globo che cade, è manifesto che la forza della resistenza, mantenuta uniformemente nello stesso tempo, potrebbe togliere una velocità minore nel rapporto di 1 a 376 1/50, cioè la parte 1/(376 1/50) dell’intera velocità. E perciò, nel tempo in cui il globo, con quella velocità mantenuta uniformemente, potrebbe descrivere la lunghezza del suo semidiametro, ossia di 3 7/16 pollici, perderebbe la parte 1/3342 del suo moto.

#### 2. La quarta parte del moto

**[II.S6.51]** Contavo anche le oscillazioni in cui il pendolo perdeva la quarta parte del suo moto. Nella tabella seguente i numeri in alto indicano la lunghezza dell’arco descritto nella prima discesa, espressa in pollici e parti di pollice; i numeri di mezzo indicano la lunghezza dell’arco descritto nell’ultima salita; e in basso stanno i numeri delle oscillazioni. Ho descritto l’esperimento perché è più accurato di quello in cui si perdeva soltanto l’ottava parte del moto. Tenti il calcolo chi vorrà.

| Prima discesa | 2 | 4 | 8 | 16 | 32 | 64 |
|---|---:|---:|---:|---:|---:|---:|
| Ultima salita | 1½ | 3 | 6 | 12 | 24 | 48 |
| Numero delle oscillazioni | 374 | 272 | 162½ | 83⅓ | 41⅔ | 22⅔ |

#### 3. Il globo di piombo e la resistenza del filo

**[II.S6.52]** In seguito ho sospeso allo stesso filo un globo di piombo del diametro di 2 pollici e del peso di 26¼ once romane, in modo che fra il centro del globo e il punto di sospensione vi fosse un intervallo di 10½ piedi, e contavo le oscillazioni in cui si perdeva una parte data del moto. Delle tabelle seguenti, la prima mostra il numero delle oscillazioni in cui cessava l’ottava parte del moto totale; la seconda il numero delle oscillazioni in cui ne andava perduta la quarta parte.

| Prima discesa | 1 | 2 | 4 | 8 | 16 | 32 | 64 |
|---|---:|---:|---:|---:|---:|---:|---:|
| Ultima salita | ⅞ | 7/4 | 3½ | 7 | 14 | 28 | 56 |
| Numero delle oscillazioni | 226 | 228 | 193 | 140 | 90½ | 53 | 30 |

| Prima discesa | 1 | 2 | 4 | 8 | 16 | 32 | 64 |
|---|---:|---:|---:|---:|---:|---:|---:|
| Ultima salita | ¾ | 1½ | 3 | 6 | 12 | 24 | 48 |
| Numero delle oscillazioni | 510 | 518 | 420 | 318 | 204 | 121 | 70 |

**[II.S6.53]** Scegliendo nella prima tabella la terza, la quinta e la settima osservazione, ed esprimendo le velocità massime in queste osservazioni singolarmente con i numeri 1, 4, 16 rispettivamente, e in generale con la quantità V come sopra, risulterà nella terza osservazione ½/193 = A + B + C, nella quinta 2/90½ = 4A + 8B + 16C, nella settima 8/30 = 16A + 64B + 256C. Queste equazioni, ridotte, danno A = 0,001414, B = 0,000297, C = 0,000879. E di qui risulta che la resistenza del globo mosso con la velocità V sta al suo peso di 26¼ once nel rapporto che 0,0009V + 0,000208V^(3/2) + 0,000659V² ha con la lunghezza del pendolo di 121 pollici. E se consideriamo soltanto quella parte della resistenza che è in rapporto duplicato della velocità, essa starà al peso del globo come 0,000659V² sta a 121 pollici. Ma questa parte della resistenza, nel primo esperimento, stava al peso del globo di legno di 57 7/22 once come 0,002217V² sta a 121; e di qui la resistenza del globo di legno sta alla resistenza del globo di piombo (a parità delle loro velocità) come 57 7/22 × 0,002217 sta a 26¼ × 0,000659, cioè come 7⅓ sta a 1. I diametri dei due globi erano di 6⅞ e di 2 pollici, e i loro quadrati stanno fra loro come 47¼ e 4, ossia come 11 13/16 e 1, con ottima approssimazione. Le resistenze dei globi ugualmente veloci erano dunque in un rapporto minore del duplicato dei diametri. Ma non abbiamo ancora considerato la resistenza del filo, che certo era assai grande e deve essere sottratta dalla resistenza trovata per i pendoli. Non ho potuto determinarla con precisione, ma l’ho trovata tuttavia maggiore della terza parte della resistenza totale del pendolo minore; e di qui ho appreso che le resistenze dei globi, tolta la resistenza del filo, sono con ottima approssimazione in rapporto duplicato dei diametri. Infatti il rapporto di 7⅓ − ⅓ a 1 − ⅓, ossia di 10½ a 1, non è molto lontano dal rapporto duplicato dei diametri, 11 13/16 a 1.

#### 4. Il globo grande

**[II.S6.54]** Poiché la resistenza del filo è di minore importanza nei globi maggiori, ho tentato l’esperimento anche con un globo il cui diametro era di 18¾ pollici. La lunghezza del pendolo fra il punto di sospensione e il centro di oscillazione era di 122½ pollici, fra il punto di sospensione e il nodo sul filo di 109½ pollici. L’arco descritto dal nodo nella prima discesa del pendolo: 32 pollici. L’arco descritto dallo stesso nodo nell’ultima salita, dopo cinque oscillazioni: 28 pollici. La somma degli archi, ossia l’arco intero descritto in un’oscillazione media: 60 pollici. La differenza degli archi: 4 pollici. La sua decima parte, ossia la differenza fra la discesa e la salita in un’oscillazione media: ⅖ di pollice. Come il raggio di 109½ sta al raggio di 122½, così l’arco intero di 60 pollici descritto dal nodo in un’oscillazione media sta all’arco intero di 67⅛ pollici descritto dal centro del globo in un’oscillazione media; e così la differenza di ⅖ sta alla nuova differenza 0,4475.

**[II.S6.55]** Se la lunghezza del pendolo, restando la stessa la lunghezza dell’arco descritto, aumentasse nel rapporto di 126 a 122½, il tempo dell’oscillazione aumenterebbe e la velocità del pendolo diminuirebbe nel rapporto subduplicato di quel rapporto, mentre la differenza degli archi descritti nella discesa e nella salita successiva resterebbe 0,4475. Se poi l’arco descritto aumentasse nel rapporto di 124 3/31 a 67⅛, quella differenza di 0,4475 aumenterebbe nel rapporto duplicato di quel rapporto, e diventerebbe quindi 1,5295. Così starebbero le cose nell’ipotesi che la resistenza del pendolo fosse in rapporto duplicato della velocità. Se dunque il pendolo descrivesse l’arco intero di 124 3/31 pollici, e la sua lunghezza fra il punto di sospensione e il centro di oscillazione fosse di 126 pollici, la differenza degli archi descritti nella discesa e nella salita successiva sarebbe di 1,5295 pollici. E questa differenza, moltiplicata per il peso del globo del pendolo, che era di 208 once, dà 318,136. Di nuovo: quando il pendolo descritto sopra, costruito con il globo di legno, con il centro di oscillazione distante 126 pollici dal punto di sospensione, descriveva l’arco intero di 124 3/31 pollici, la differenza degli archi descritti nella discesa e nella salita fu 126/121 × 8/9⅔; e questa, moltiplicata per il peso del globo, che era di 57 7/22 once, dà 49,396.

**[II.S6.56]** Ho moltiplicato queste differenze per i pesi dei globi per trovarne le resistenze. Le differenze nascono infatti dalle resistenze, e sono come le resistenze, direttamente, e come i pesi, inversamente. Le resistenze sono dunque come i numeri 318,136 e 49,396. Ma la parte della resistenza del globo minore che è in rapporto duplicato della velocità stava alla resistenza totale come 0,56752 sta a 0,61675, cioè come 45,453 sta a 49,396; e la parte della resistenza del globo maggiore è pressoché uguale alla sua intera resistenza; e perciò quelle parti sono con ottima approssimazione come 318,136 e 45,453, cioè come 7 e 1. I diametri dei globi sono poi 18¾ e 6⅞, e i loro quadrati, 351 9/16 e 47 17/64, sono come 7,438 e 1, cioè, con ottima approssimazione, come le resistenze dei globi, 7 e 1. La differenza dei rapporti non è maggiore di quella che può essere nata dalla resistenza del filo. Dunque quelle parti delle resistenze che, a parità di globi, sono come i quadrati delle velocità, sono anche, a parità di velocità, come i quadrati dei diametri dei globi.

**[II.S6.57]** Del resto, il più grande dei globi di cui mi sono servito in questi esperimenti non era perfettamente sferico, e perciò nel calcolo qui riportato, per brevità, ho trascurato alcune minuzie, poco preoccupato di un calcolo accurato in un esperimento non abbastanza accurato. Vorrei quindi, poiché da questi esperimenti dipende la dimostrazione del vuoto, che gli esperimenti fossero tentati con globi più numerosi, più grandi e più accurati. Se si prendono globi in proporzione geometrica, per esempio con diametri di 4, 8, 16, 32 pollici, dalla progressione degli esperimenti si ricaverà che cosa deve accadere in globi ancora maggiori.

#### 5. Acqua e aria

**[II.S6.58]** Poi, per confrontare fra loro le resistenze di fluidi diversi, ho tentato quanto segue. Ho preparato una cassa di legno lunga quattro piedi, larga e alta un piede. Tolto il coperchio, l’ho riempita d’acqua di fonte e ho fatto in modo che i pendoli immersi si muovessero oscillando in mezzo all’acqua. Un globo di piombo del peso di 166⅙ once, con un diametro di 3⅝ pollici, si muoveva come abbiamo descritto nella tabella seguente; la lunghezza del pendolo dal punto di sospensione a un certo punto segnato sul filo era di 126 pollici, e fino al centro di oscillazione di 134⅜ pollici.

| Arco descritto nella prima discesa dal punto segnato sul filo, in pollici | 64 | 32 | 16 | 8 | 4 | 2 | 1 | ½ | ¼ |
|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| Arco descritto nell’ultima salita, in pollici | 48 | 24 | 12 | 6 | 3 | 1½ | ¾ | ⅜ | 3/16 |
| Differenza degli archi, proporzionale al moto perduto, in pollici | 16 | 8 | 4 | 2 | 1 | ½ | ¼ | ⅛ | 1/16 |
| Numero delle oscillazioni in acqua | | | 29/60 | 1⅕ | 3 | 7 | 11¼ | 12⅔ | 13⅓ |
| Numero delle oscillazioni in aria | 85½ | 287 | | 535 | | | | | |

**[II.S6.59]** Nell’esperimento della quarta colonna, moti uguali sono stati perduti in 535 oscillazioni in aria e in 1⅕ in acqua. Le oscillazioni in aria erano, è vero, un poco più veloci che in acqua. Ma se le oscillazioni in acqua fossero accelerate nel rapporto necessario perché i moti dei pendoli diventassero ugualmente veloci nei due mezzi, resterebbe lo stesso numero di 1⅕ oscillazioni in acqua, in cui si perderebbe lo stesso moto di prima, perché la resistenza aumenterebbe e il quadrato del tempo diminuirebbe in quello stesso rapporto duplicato. A parità di velocità dei pendoli, dunque, moti uguali sono stati perduti in 535 oscillazioni in aria e in 1⅕ in acqua; e perciò la resistenza del pendolo in acqua sta alla sua resistenza in aria come 535 sta a 1⅕. Questo è il rapporto delle resistenze totali nel caso della quarta colonna.

**[II.S6.60]** Indichi ora AV + CV² la differenza degli archi descritti nella discesa e nella salita successiva dal globo mosso in aria con la velocità massima V; e poiché la velocità massima nel caso della quarta colonna sta alla velocità massima nel caso della prima colonna come 1 sta a 8, e quella differenza degli archi nel caso della quarta colonna sta alla differenza nel caso della prima colonna come 2/535 sta a 16/85½, ossia come 85½ sta a 4280, scriviamo in questi casi 1 e 8 al posto delle velocità, e 85½ e 4280 al posto delle differenze degli archi: si avrà A + C = 85½ e 8A + 64C = 4280, ossia A + 8C = 535; e di qui, con la riduzione delle equazioni, si otterrà 7C = 449½, C = 64 3/14 e A = 21 2/7; e perciò la resistenza, essendo come 7/11 AV + ¾CV², sarà come 13 6/11 V + 48 9/56 V². Perciò, nel caso della quarta colonna, dove la velocità era 1, la resistenza totale sta alla sua parte proporzionale al quadrato della velocità come 13 6/11 + 48 9/56, ossia 61 12/17, sta a 48 9/56; e perciò la resistenza del pendolo in acqua sta a quella parte della resistenza in aria che è proporzionale al quadrato della velocità, e che sola merita considerazione nei moti più veloci, come 61 12/17 sta a 48 9/56 e 535 sta a 1⅕, considerati congiuntamente, cioè come 571 sta a 1. Se tutto il filo del pendolo oscillante in acqua fosse stato immerso, la sua resistenza sarebbe stata ancora maggiore; tanto che la resistenza del pendolo oscillante in acqua, quella che è proporzionale al quadrato della velocità e che sola merita considerazione nei corpi più veloci, sta alla resistenza dello stesso pendolo intero, oscillante in aria con la stessa velocità, circa come 850 sta a 1, cioè, con ottima approssimazione, come la densità dell’acqua sta alla densità dell’aria.

**[II.S6.61]** In questo calcolo si sarebbe dovuta prendere anche quella parte della resistenza del pendolo in acqua che fosse come il quadrato della velocità; ma (cosa che forse sembrerà strana) la resistenza in acqua aumentava in un rapporto più che duplicato della velocità. Indagandone la causa, mi sono imbattuto in questa: la cassa era troppo stretta per la grandezza del globo del pendolo e, per la sua strettezza, impediva troppo il moto dell’acqua che cedeva. Se infatti si immergeva un globo pendolo il cui diametro era di un pollice, la resistenza aumentava con ottima approssimazione in rapporto duplicato della velocità. Lo provavo costruendo un pendolo con due globi, dei quali l’inferiore e minore oscillasse in acqua, mentre il superiore e maggiore fosse fissato al filo subito sopra l’acqua e, oscillando in aria, aiutasse il moto del pendolo e lo rendesse più durevole. Gli esperimenti istituiti in questo modo andarono come è descritto nella tabella seguente.

| Arco descritto nella prima discesa | 16 | 8 | 4 | 2 | 1 | ½ | ¼ |
|---|---:|---:|---:|---:|---:|---:|---:|
| Arco descritto nell’ultima salita | 12 | 6 | 3 | 1½ | ¾ | ⅜ | 3/16 |
| Differenza degli archi, proporzionale al moto perduto | 4 | 2 | 1 | ½ | ¼ | ⅛ | 1/16 |
| Numero delle oscillazioni | 3⅜ | 6½ | 12 1/12 | 21⅕ | 34 | 53 | 62⅕ |

#### 6. Mercurio e altri liquidi

**[II.S6.62]** Confrontando fra loro le resistenze dei mezzi, ho fatto anche oscillare pendoli di ferro nel mercurio (argento vivo). La lunghezza del filo di ferro era di circa tre piedi, e il diametro del globo del pendolo la terza parte di un pollice. Al filo, subito sopra il mercurio, era poi fissato un altro globo di piombo, abbastanza grande da prolungare più a lungo il moto del pendolo. Poi riempivo un vasetto, che conteneva circa tre libbre di mercurio, a volte alterne di mercurio e di acqua comune, per trovare il rapporto delle resistenze facendo oscillare il pendolo successivamente nell’uno e nell’altro fluido; e risultò che la resistenza del mercurio stava alla resistenza dell’acqua circa come 13 o 14 sta a 1, cioè come la densità del mercurio sta alla densità dell’acqua. Quando adoperavo un globo pendolo un poco maggiore, per esempio uno il cui diametro fosse di circa ½ o ⅔ di pollice, la resistenza del mercurio risultava stare alla resistenza dell’acqua nel rapporto che il numero 12 o 10 ha con 1, circa. Ma ci si deve fidare di più del primo esperimento, perché in questi ultimi il vaso era troppo stretto per la grandezza del globo immerso. Allargando il globo si sarebbe dovuto allargare anche il vaso. Avevo stabilito, in verità, di ripetere esperimenti di questo genere in vasi maggiori e in liquidi sia di metalli fusi, sia di certi altri, tanto caldi quanto freddi; ma non ho tempo di sperimentare tutto, e da quanto si è già descritto è abbastanza chiaro che la resistenza dei corpi mossi velocemente è con ottima approssimazione proporzionale alla densità dei fluidi in cui si muovono. Non dico esattamente. I fluidi più tenaci, infatti, a parità di densità, resistono senza dubbio più di quelli più liquidi, come l’olio freddo più di quello caldo, quello caldo più dell’acqua piovana, l’acqua più dello spirito di vino. Ma nei liquidi che sono sensibilmente abbastanza fluidi, come nell’aria, nell’acqua dolce o salata, negli spiriti di vino, di trementina e di sali, nell’olio liberato dalle fecce per distillazione e riscaldato, nell’olio di vetriolo e nel mercurio, nei metalli liquefatti e in altri, se ve ne sono, che siano così fluidi da conservare più a lungo il moto impresso quando sono agitati nei vasi e che, versati, si risolvano scorrendo liberissimamente in gocce, non dubito affatto che la regola esposta valga con sufficiente accuratezza: soprattutto se gli esperimenti si istituiscono con corpi pendoli più grandi e mossi più velocemente.

#### 7. La scatola piena e vuota: la resistenza delle parti interne

**[II.S6.63]** Infine, poiché alcuni sono dell’opinione che esista un certo mezzo etereo, di gran lunga il più sottile, che permei liberissimamente tutti i pori e i condotti di tutti i corpi, e da un tale mezzo che scorre attraverso i pori dei corpi dovrebbe nascere una resistenza, per provare se la resistenza che sperimentiamo nei corpi in moto sia tutta sulla loro superficie esterna, o se anche le parti interne sentano sulle proprie superfici una resistenza notevole, ho escogitato un esperimento di questo tipo. Con un filo lungo undici piedi sospendevo a un gancio d’acciaio abbastanza saldo, per mezzo di un anello d’acciaio, una scatola rotonda di legno d’abete, per costituire un pendolo della lunghezza predetta. Il gancio, verso l’alto, era affilato a spigolo concavo, perché l’anello, appoggiato con il suo arco superiore allo spigolo, si muovesse liberissimamente. All’arco inferiore era poi legato il filo. Il pendolo così costituito lo allontanavo dalla perpendicolare fino alla distanza di circa sei piedi, e ciò in un piano perpendicolare allo spigolo del gancio, perché l’anello, mentre il pendolo oscillava, non scivolasse avanti e indietro sullo spigolo del gancio: il punto di sospensione, infatti, nel quale l’anello tocca il gancio, deve restare immobile. Annotavo dunque con precisione il luogo fino al quale avevo portato il pendolo; poi, lasciato andare il pendolo, annotavo altri tre luoghi ai quali ritornava alla fine della prima, della seconda e della terza oscillazione. Lo ripetevo più volte, per trovare quei luoghi con la massima precisione possibile. Poi riempivo la scatola di piombo e dei metalli più pesanti che avevo a portata di mano. Ma prima pesavo la scatola vuota, insieme con la parte del filo che era avvolta intorno alla scatola e con la metà della parte restante, che era tesa fra il gancio e la scatola sospesa: il filo teso, infatti, preme sempre con la metà del suo peso il pendolo allontanato dalla perpendicolare. A questo peso aggiungevo il peso dell’aria che la scatola conteneva. E il peso totale era circa la settantottesima parte di quello della scatola piena di metalli. Poi, poiché la scatola piena di metalli, tendendo con il suo peso il filo, aumentava la lunghezza del pendolo, accorciavo il filo, perché la lunghezza del pendolo, ormai in oscillazione, fosse la stessa di prima. Poi, riportato il pendolo al luogo segnato per primo e lasciatolo andare, contavo circa settantasette oscillazioni finché la scatola tornava al luogo segnato per secondo, e altrettante in seguito finché tornava al luogo segnato per terzo, e di nuovo altrettante finché la scatola, nel suo ritorno, raggiungeva il quarto luogo. Di qui concludo che la resistenza totale della scatola piena non aveva con la resistenza della scatola vuota un rapporto maggiore di 78 a 77. Infatti, se le resistenze di entrambe fossero state uguali, la scatola piena, per la sua forza insita settantotto volte maggiore della forza insita della scatola vuota, avrebbe dovuto conservare tanto più a lungo il suo moto oscillatorio, e quindi tornare a quei luoghi segnati sempre dopo 78 oscillazioni compiute. Vi tornò invece dopo 77 oscillazioni compiute.

**[II.S6.64]** A indichi dunque la resistenza della scatola sulla sua superficie esterna e B la resistenza della scatola vuota nelle parti interne; e se le resistenze dei corpi ugualmente veloci nelle parti interne sono come la materia, ossia come il numero delle particelle a cui si oppone resistenza, 78B sarà la resistenza della scatola piena nelle sue parti interne; e perciò la resistenza totale A + B della scatola vuota starà alla resistenza totale A + 78B della scatola piena come 77 sta a 78, e, separando, A + B starà a 77B come 77 sta a 1, e quindi A + B starà a B come 77 × 77 sta a 1, e, separando, A starà a B come 5928 sta a 1. La resistenza della scatola vuota nelle parti interne è dunque più di cinquemila volte minore della sua resistenza sulla superficie esterna. Così però ragioniamo nell’ipotesi che quella resistenza maggiore della scatola piena non nasca da qualche altra causa nascosta, ma dalla sola azione di un fluido sottile sul metallo racchiuso.

**[II.S6.65]** Ho riferito questo esperimento a memoria. Il foglio, infatti, sul quale lo avevo descritto un tempo è andato perduto. Perciò sono stato costretto a omettere certe parti frazionarie dei numeri, che mi sono sfuggite dalla memoria; non ho infatti tempo di ritentare tutto da capo. La prima volta, poiché avevo usato un gancio debole, la scatola piena rallentava più presto. Cercandone la causa, ho trovato che il gancio debole cedeva al peso della scatola e, assecondandone le oscillazioni, si piegava in tutte le direzioni. Ho preparato dunque un gancio saldo, perché il punto di sospensione restasse immobile, e allora tutto è andato come abbiamo descritto sopra.

**Fine della Sezione VI. Nel testo originale segue la Sezione VII, *De motu fluidorum & resistentia projectilium*.**

---

## Apparato

### A.0 Estensioni del glossario

I termini seguenti non sono nel glossario comune né nell’addendum del Libro II. Ognuno è reso in modo costante in tutto il fascicolo.

| Latino | Italiano | Motivazione |
|---|---|---|
| *corpora funependula*; *corpus pendulum*; *materia pendula* | «corpi appesi a un filo»; «corpo pendolo»; «materia del corpo pendolo» | Glossario del Libro I (*corpus funependulum*) e Fascicolo 9 (*corpus pendulum* «corpo pendolo»). Nel titolo della Sezione: «Il moto e la resistenza dei corpi appesi a un filo». |
| *quibus resistitur*; *resisti* | «che incontrano una resistenza»; «incontrare una resistenza» | Il passivo impersonale latino non ha un equivalente diretto; «incontrare una resistenza» conserva il soggetto grammaticale (il corpo). |
| *momentum temporis*; *in ratione momentorum temporis* | «momento del tempo»; «in rapporto ai momenti del tempo» | *Momentum* secondo il glossario («momento»); la locuzione segue lo schema dell’addendum («in rapporto alla velocità»). Il senso — resistenza costante — è spiegato da Newton stesso nella Prop. XXV (*ideoque detur*) e nella nota N2. |
| *centrum oscillationis*; *centrum / punctum suspensionis* | «centro di oscillazione»; «centro / punto di sospensione» | Termini tecnici della teoria dei pendoli (Huygens), conservati. |
| *perpendiculum* | «perpendicolare» | Come nel Fascicolo 9: la verticale per il punto di sospensione. |
| *pondus comparativum*; *pondus absolutum* | «peso comparativo»; «peso assoluto» | Rimandano alla *gravitas comparativa / absoluta* del Cor. 6 della Prop. XX (Sezione V). |
| *isochronus* | «isocrono» | Come nel Fascicolo 9. |
| *excessus* | «eccesso» | |
| *oscillatio mediocris* | «oscillazione media» | L’oscillazione rappresentativa di una serie che si smorza. |
| *velocitas maxima*; *motus velocissimus* | «velocità massima»; «moto più veloce» | |
| *vis generans* | «forza generatrice» | Prop. XXX. |
| *indeterminata* (sost.) | «indeterminata» | Prop. XXX: la grandezza variabile CM. Conservato il termine dell’epoca. |
| *ordinata rectangula* | «ordinata perpendicolare» | |
| *trapezium* | «trapezio» | |
| *contentum / rectangulum sub* | «rettangolo contenuto sotto» | Come nel Fascicolo 5. |
| *debita collatio & reductio analytica* | «l’opportuno confronto e la riduzione analitica» | La soluzione del sistema lineare. |
| *experimentum hydrostaticum* | «esperimento idrostatico» | |
| *uncia Romana*; *digitus Londinensis* | «oncia romana»; «pollice londinese» | Unità dell’addendum con l’aggettivo del testo. Motte rende «ounces troy» (A.12). |
| *uncus*; *annulus chalybeus*; *acies* | «gancio»; «anello d’acciaio»; «spigolo» | Esperimento della scatola. |
| *regula in digitos distincta* | «regolo diviso in pollici» | |
| *nodus* (in filo) | «nodo» | |
| *arca lignea*; *operculum* | «cassa di legno»; «coperchio» | |
| *pyxis abiegna* | «scatola rotonda di legno d’abete» | Motte «round deal box». |
| *vasculum*; *vas* | «vasetto»; «vaso» | *Vas* secondo l’addendum. |
| *aqua fontana*; *aqua communis* | «acqua di fonte»; «acqua comune» | |
| *spiritus vini*; *terebinthus*; *oleum vitrioli* | «spirito di vino»; «trementina»; «olio di vetriolo» | Nomi storici, conservati (in nota N16 l’equivalente moderno). |
| *medium æthereum*; *pori & meatus* | «mezzo etereo»; «pori e condotti» | |
| *tardescere*; *conspirare* | «rallentare»; «concordare» | Prop. XXVII, Cor. 2. |
| *producere / contrahere tempus* | «allungare / accorciare il tempo» | |
| *quam minimus* | «piccolissimo» | Come nel Fascicolo 5. |

**Termini nuovi da armonizzare** (per il coordinatore): *in ratione momentorum temporis* «in rapporto ai momenti del tempo»; *resisti* «incontrare una resistenza»; *pondus comparativum* «peso comparativo»; *uncia Romana* «oncia romana»; *digitus Londinensis* «pollice londinese»; *oscillatio mediocris* «oscillazione media»; *centrum oscillationis / suspensionis*; *indeterminata* «indeterminata»; *ordinata rectangula* «ordinata perpendicolare».

*Vis insita* compare una volta (II.S6.63: *ob vim suam insitam*), resa «forza insita» secondo il glossario; Motte la lascia in latino («vis insita»).

### A.1 Proposizione XXIV

**Latino:** *Quantitates materiæ in corporibus funependulis, quorum centra oscillationum a centro suspensionis æqualiter distant, sunt in ratione composita ex ratione ponderum & ratione duplicata temporum oscillationum in vacuo.*

**Inglese:** “The quantities of matter in funependulous bodies, whose centres of oscillation are equally distant from the centre of suspension, are in a ratio compounded of the ratio of the weights and the duplicate ratio of the times of the oscillations in vacuo.”

**Scelte.**

- *per motus legem secundam* → «per la seconda legge del moto» (Legge II, Fascicolo 3).
- *vires motrices*: «forze motrici», secondo il glossario.
- *velocitates reciproce sunt ut tempora*: «le velocità, inversamente, sono come i tempi»: la virgola rende la lettura «l’inverso delle velocità è come i tempi».
- Cor. 4: *cæteris paribus* → «a parità delle altre condizioni»; Motte lascia il latino.
- Cor. 6: *ut supra explicui* rimanda alla Sezione V, Cor. 6 della Prop. XX (gravità «vera e assoluta» e «apparente, volgare e comparativa»): rimando verificato sulla trascrizione della Sezione V. *Idem præstat* → «produce lo stesso effetto».
- Cor. 7: *Factis … experimentis quam accuratissimis* → «eseguiti … esperimenti quanto più accurati possibile». Motte ha «by experiments made with the greatest accuracy».

### A.2 Proposizione XXV

**Latino:** *Corpora Funependula quibus, in medio quovis, resistuntur in ratione momentorum temporis, & corpora funependula quæ in ejusdem gravitatis specificæ medio non resistente moventur, oscillationes in cycloide eodem tempore peragunt, & arcuum partes proportionales simul describunt.*

**Inglese:** “Funependulous bodies that are, in any medium, resisted in the ratio of the moments of time, and funependulous bodies that move in a non-resisting medium of the same specific gravity, perform their oscillations in a cycloid in the same time, and describe proportional parts of arcs together.”

**Scelte e divergenze.**

- *resistuntur*: il passivo personale con *quibus* è irregolare (ci si attenderebbe *resistitur*); il senso non cambia.
- *vis acceleratrix*: «forza acceleratrice». La proporzionalità della forza all’arco nella cicloide non è citata: è il Cor. della Prop. LI del Libro I (nota alla Parte B).
- *excessus vis Cd supra resistentiam CO* → «l’eccesso della forza Cd sulla resistenza CO».
- **Refuso probabile della trascrizione:** *ut arcus toti CD, OB* (II.S6.11, settima frase): gli archi interi sono CB, OB, come nelle frasi vicine e in Motte. Tradotto «CB, OB».
- **Refuso probabile:** *oscillaciones* per *oscillationes*.
- **Aggiunta di Motte:** «isochronal, **or are performed in equal times**».
- Cor.: *iisdem gradibus* → «con gli stessi gradi», cioè con la stessa legge.

### A.3 Proposizione XXVI

**Latino:** *Corporum funependulorum, quibus resistitur in ratione velocitatum, oscillationes in cycloide sunt Isochronæ.*

**Inglese:** “Funependulous bodies, that are resisted in the ratio of the velocity, have their oscillations in a cycloid isochronal.”

**Scelte.** *simul describentur* → «saranno descritti insieme»; Motte «in the same time». Motte rende *velocitatum* al singolare («velocity»). *auferantur vel addantur* → «si tolgono o si aggiungono» (nella discesa la resistenza si sottrae alla forza, nella salita si aggiunge).

### A.4 Proposizione XXVII

**Latino:** *Si corporibus funependulis resistitur in duplicata ratione velocitatum, differentiæ inter tempora oscillationum in medio resistente ac tempora oscillationum in ejusdem gravitatis specificæ medio non resistente, erunt arcubus oscillando descriptis proportionales, quam proxime.*

**Inglese:** “If funependulous bodies are resisted in the duplicate ratio of their velocities, the differences between the times of the oscillations in a resisting medium, and the times of the oscillations in a non-resisting medium of the same specific gravity, will be proportional to the arcs described in oscillating nearly.”

**Scelte.**

- Notazione «AA, AB, BB» conservata (prodotti degli archi A, B).
- *per propositionem superiorem* → «per la proposizione precedente» (Prop. XXVI); Motte «by the last Prop.».
- *vires efficientes* → «le forze che li producono».
- Cor. 2: *in eandem plagam pergendo* → «procedendo verso la stessa parte»; *conspirat* → «concorda». Motte rende *ex utraque causa* con «these two causes concurring».
- La trascrizione non ha il punto prima di *Q.E.D.* (*ut arcus A & B Q.E.D.*): punteggiatura.
- Una figura compare in Motte in questa proposizione ([FIG] dopo l’enunciato), mentre il latino non ha marcatori [FIG] fra la 44 (Prop. XXV) e la 45 (Prop. XXVIII): da controllare sulla stampa se la figura 45 sia condivisa dalle Propp. XXVII–XXVIII.

### A.5 Proposizione XXVIII

**Latino e inglese:** nella Parte B (unità `L2-P28`).

**Scelte.** *ad penduli longitudinem duplicatam* → «al doppio della lunghezza del pendolo» (*duplicatam* qui è «raddoppiata», non «rapporto duplicato»). *in cycloidis principio seu puncto altissimo* → «all’inizio della cicloide, cioè nel suo punto più alto». *stantibus quæ … constructa & demonstrata sunt* → «ferme restando la costruzione e la dimostrazione». Nessuna divergenza di Motte rilevante.

### A.6 Proposizione XXIX

**Latino e inglese:** nella Parte B (unità `L2-P29`).

**Scelte e divergenze.**

- **Lettera:** *area IEF ad aream ILT ut OQ ad OC* (p. 300). C non sta sulla retta OQ; Motte ha **OS** e la verifica numerica (N7) richiede OS. Tradotto «OS»; da controllare sulla stampa.
- Le aree con frazione appiattita («OROQIEF», «RrOQIEF», «IEFOQ», «OPOQIEF») sono lette (OR/OQ) × IEF ecc., come confermano le formule SVG 618–625 di Motte.
- *per lem. II.* → «per il Lemma II»: è il Lemma II del Libro II (Sezione II, momento della quantità generata; Fascicolo 14).
- *crescunt area Y … & area Z*: verbo plurale con due soggetti singolari; resa normalizzata.
- **Aggiunta di Motte** (II.S6.26): «begins and ends **also where the resistance is nothing**»; il latino dice *ubi nulla est*, riferito all’area Y.
- Cor. 3: *ipso motus initio æquatur* → «proprio all’inizio del moto, è uguale»: vedi N7.
- La seconda figura (FIG 47) cade nel latino a metà di II.S6.26; Motte la colloca prima di «Now the area Z»: posizione tipografica, nessuna conseguenza.

### A.7 Proposizione XXX e corollario

**Latino e inglese:** nella Parte B (unità `L2-P30`, `L2-P30-Cor`).

**Scelte e divergenze.**

- *ducta in arcuum eorundem semisummam* → «moltiplicata per la semisomma degli stessi archi» (*ducere in*).
- *in DE capiatur DK* → «su DE si prende DK»: K giace sulla perpendicolare DE (dalla parte del semicerchio).
- *Patet hoc (per prop. LII. lib. I.)*: la trascrizione non ha il punto dopo la parentesi.
- *ex æquo*, *ex æquo perturbate*: «per uguaglianza», «per uguaglianza perturbata» (Fascicolo 7). Motte lascia il latino.
- L’enunciato chiama la figura «BKa», la dimostrazione «BKVTa», il corollario «BKTa» e «BKVTa»: tutte nel latino e in Motte; si conservano.
- Corollario: *area ellipseos hujus* va intesa come area della **semiellisse** BRVSa (sopra Ba); il confronto con il semicerchio lo conferma. Nessuna correzione nel testo.
- Corollario: *abunde satis accuratas* → «più che sufficientemente accurate»; Motte «accurate enough» attenua *abunde*.

### A.8 Proposizione XXXI

**Latino e inglese:** nella Parte B (unità `L2-P31`).

**Scelte.** *in superiore propositione* → «nella proposizione precedente» (Prop. XXX). *ordinatim applicatæ DK* → «ordinate DK». Cor. 4: *Eadem erit lex & ratio resistentiæ pro velocitate, quæ est differentiæ illius pro longitudine arcus* → «la legge e il rapporto della resistenza rispetto alla velocità saranno gli stessi della legge e del rapporto di quella differenza rispetto alla lunghezza dell’arco». Motte introduce la frase con «So that», che il latino non ha.

### A.9 Scolio generale

- **Titolo.** *Scholium Generale* → «Scolio generale». Da non confondere con lo *Scholium generale* che chiude il Libro III (osservazione non verificata sulle fonti allegate).
- **Unità.** *uncia Romana* → «oncia romana»; Motte «ounces troy» (A.12). *digitus Londinensis* → «pollice londinese». Le misure non sono convertite (N18).
- *ita ut … describeret arcum digiti unius cum tribus partibus quartis digiti*: «un pollice e tre quarti di pollice» (1¾, Motte SVG 638).
- *Experimentum descripti tanquam magis accuratum*: *descripti* è refuso probabile per *descripsi*; reso «Ho descritto l’esperimento perché è più accurato».
- *Calculum tentet qui volet* → «Tenti il calcolo chi vorrà»; Motte «I leave the calculation to such as are disposed to make it». Il calcolo è eseguito nella nota N12.
- *Est si spectemus* (p. 311): refuso probabile per *Et si*; Motte «And if we regard».
- *ut 57722 in 0,002217 ad 2614 in 0,000659*: *in* = «moltiplicato per».
- *Ejus pars decima* (p. 311–312): la differenza 4 su «cinque oscillazioni» divisa per 10, non per 5: Newton conta evidentemente dieci semioscillazioni (discesa più salita), cioè cinque oscillazioni doppie. Motte conferma 1/10 (SVG 691) e ⅖ (SVG 692). Vedi N14.
- *0,61675* (p. 312) contro *0,61705* (p. 309): vedi N14. Nessuna correzione nel testo.
- *secique ut immersa pendula … moverentur* (p. 313): refuso probabile per *fecique* (s lunga); tradotto «ho fatto in modo che».
- *{16616}* (p. 313): parentesi graffe di artefatto; lettura 166⅙, confermata da Motte (SVG 698).
- *722AV* (p. 314): la trascrizione ha 7/22 AV; il calcolo seguente (13 6/11 = 7/11 × 21 2/7) e Motte (SVG 720: 7/11 AV + ¾CV²) richiedono **7/11**. Tradotto 7/11; da controllare sulla stampa.
- *in ratione velocitatis plusquam duplicata* → «in un rapporto più che duplicato della velocità».
- *quasi 13 vel 23 partes digiti* (p. 315): «⅓ o ⅔» contraddice *paulo majorem* rispetto al globo di ⅓ di pollice; Motte ha ½ (SVG 643) o ⅔ (SVG 226). Tradotto «½ o ⅔»; da controllare sulla stampa.
- *Constitueram* → «avevo stabilito»; Motte «I intended».
- *in oleo a fæcibus per destillationem liberato* → «nell’olio liberato dalle fecce per distillazione».
- *Uncus sursum præacutus erat acie concava* → «Il gancio, verso l’alto, era affilato a spigolo concavo».
- *Nam filum tensum dimidio ponderis sui pendulum a perpendiculo digressum semper urget* → «il filo teso, infatti, preme sempre con la metà del suo peso il pendolo allontanato dalla perpendicolare».
- *quinquies millies minor … & amplius* → «più di cinquemila volte minore».
- *in partes omnes flectebatur* → «si piegava in tutte le direzioni»; Motte «bent sometimes this and sometimes that way».

### A.10 Rimandi verificati

| Luogo | Rimando nel latino | Verifica |
|---|---|---|
| II.S6.02 | *per motus legem secundam* | Legge II (Fascicolo 3, L03–L04): regge (la velocità generata è come la forza e il tempo, inversamente come la materia). |
| II.S6.08 | *ut supra explicui* | Libro II, Sez. V, Prop. XX, Cor. 6 (trascrizione `latino-1726-L2-S05.md`): definisce la gravità comparativa come eccesso sulla gravità del fluido. Regge. |
| II.S6.16 | *per propositionem superiorem* | Prop. XXVI: regge. |
| II.S6.20 | *in propositione XXV* | Prop. XXV: regge. |
| II.S6.24 | *per lem. II.* | Libro II, Lemma II (Sez. II): il momento di una potenza; applicato a v². Regge. |
| II.S6.32 | *per prop. LII. lib. I.* | **Libro I, Prop. LII** (Fascicolo 9, S10.21): la velocità in T sta a quella nel punto più basso come l’ordinata LI del semicerchio di raggio uguale all’arco SR sta al raggio GK. Le ordinate DE del semicerchio di diametro AB sono dunque come le velocità nel vuoto. **Regge.** |
| II.S6.34 | *ut in prop. XXVIII* | Regge (stesso risultato ½Aa). |
| II.S6.39 | *In superiore propositione* | Prop. XXX: regge. |
| II.S6.46 | *per corol. 2. prop. XXXI. libri hujus* | Regge. |
| II.S6.48 | *per corollarium propositionis XXX* | Regge per A e C (7/11, ¾); il coefficiente 7/10 per il termine V^(3/2) non è nel corollario: Newton lo interpola (N10). |

Rimandi al Libro I: **1** (Prop. LII), verificato; nessuno che non torni. Implicito, non citato: la proporzionalità della forza tangenziale all’arco nella cicloide (Prop. LI, Cor., e Prop. LII, Cor. 2, del Libro I).

### A.11 Formule SVG di Motte

Tutte le 119 formule SVG della sezione (618–731; 208, 225–228) sono state rese con `rsvg-convert` e lette, e confrontate con la tabella LaTeX `svg_tex.tsv` per i casi dubbi. Tutte concordano con le letture della trascrizione (§ A.13), **tranne due**, entrambe nelle parti numeriche dello Scolio:

| SVG | Motte 1846 | Latino 1726 (trascrizione) | Giudizio |
|---|---|---|---|
| 671 | 22 1/1 (ultima colonna della tabella della quarta parte) | 22⅔ («22 23») | errore dell’edizione 1846 (o della sua codifica) |
| 695 | 8/(9 3/2) | 8/9⅔ («8923») | errore dell’edizione 1846: frazione rovesciata |

Inoltre Motte **conferma contro la trascrizione** tre letture: 7/11 AV (SVG 720) contro «722AV»; ½ (SVG 643) contro «13» per il globo maggiore nel mercurio; OS (testo) contro «OC» nella Prop. XXIX. Le SVG 701, 702, 706, 712 sono graffe tipografiche delle tabelle. Non resta nessuna SVG da controllare.

### A.12 Riepilogo: dove Motte aggiunge, omette o sbaglia

| Luogo | Latino | Motte 1846 | Tipo |
|---|---|---|---|
| II.S6.09 | *quam accuratissimis* | «with the greatest accuracy» | lieve |
| II.S6.11 | *Isochronæ sunt* | «isochronal, **or are performed in equal times**» | aggiunta (glossa) |
| II.S6.11 | *arcus toti CD, OB* (trascr.) | «CB, OB» | Motte corretto |
| II.S6.14 | *simul describentur* | «described in the same time» | lieve |
| II.S6.15 | — | [FIG] dopo l’enunciato | figura in posizione diversa |
| II.S6.22 | *ut OQ ad OC* (trascr.) | «as OQ to OS» | Motte corretto |
| II.S6.26 | *ubi nulla est* | «**also where the resistance is nothing**» | aggiunta |
| II.S6.37 | *abunde satis accuratas* | «accurate enough» | attenuazione |
| II.S6.43 | — | «So that» | aggiunta di connettivo |
| II.S6.45 | *in mediis quibuscunque* | «therein» | omissione di *quibuscunque* |
| II.S6.45, 52, 53, 55 | *unciæ Romanæ* | «ounces troy» | **unità diversa** (oncia romana ≠ oncia troy) |
| II.S6.45 | *Globum ligneum* | «a wooden globe **or ball**» | aggiunta |
| II.S6.46 | *15, 30, 60, 120* | «15, 30 60, 120» | virgola mancante (refuso 1846) |
| II.S6.51 | 22⅔ | «22 1/1» (SVG 671) | **numero errato** |
| II.S6.55 | 8/9⅔ | «8/(9 3/2)» (SVG 695) | **numero errato** |
| II.S6.57 | *cum globis & pluribus & majoribus* | «with **other** globes» | aggiunta |
| II.S6.58, 61 | tabelle dell’acqua | allineamento delle colonne perso (una sola cella vuota nella riga «in water») | impaginazione |
| II.S6.60 | *722AV* (trascr.) | 7/11 AV (SVG 720) | Motte corretto |
| II.S6.62 | *13 vel 23* (trascr.) | ½ o ⅔ | Motte corretto |
| II.S6.62 | *sed omnia experiri non vacat* | «but I had not leisure to try all: **and besides**» | aggiunta |
| II.S6.63 | *ob vim suam insitam* | «vis insita» in latino | non tradotto |
| II.S6.65 | *in partes omnes* | «sometimes this and sometimes that way» | parafrasi |
| passim | *ex æquo (perturbate)*, *in vacuo*, *cæteris paribus* | lasciati in latino | — |

### A.13 Refusi e letture della trascrizione

| Luogo | Trascrizione | Lettura | Tipo |
|---|---|---|---|
| II.S6.11 | *arcus toti CD, OB* | CB, OB | refuso probabile |
| II.S6.11 | *oscillaciones* | *oscillationes* | refuso probabile |
| II.S6.16 | *arcus A & B Q.E.D.* | punto mancante | punteggiatura |
| II.S6.22 | *ut OQ ad OC* | OS | refuso probabile (lettera) |
| II.S6.22–26 | *OROQIEF*, *RrOQIEF*, *IEFOQ*; II.S6.27 *OPOQIEF* | (OR/OQ)×IEF, (Rr/OQ)×IEF, IEF/OQ, (OP/OQ)×IEF | frazioni appiattite (Motte SVG 618–625) |
| II.S6.32, 34–36, 39 | *12aB*, *12Ba*, *12Aa*, *711Aa*, *23Ba*, *34Aa* | ½aB, ½Ba, ½Aa, 7/11 Aa, ⅔Ba, ¾Aa | frazioni appiattite (SVG 626–633) |
| II.S6.45 | *57722*, *678*, *1012*, *312*, *3512*, *1812*, *923*, *14*, *12* | 57 7/22, 6⅞, 10½, 3½, 35½, 18½, 9⅔, ¼, ½ | frazioni appiattite (SVG 634–643) |
| II.S6.45 | *longitudines arcum* | *arcuum* | refuso probabile |
| II.S6.46 | *334, 712*; *1656,1242,169,471,837,2429* | 3¾, 7½; 1/656, 1/242, 1/69, 4/71, 8/37, 24/29 | frazioni appiattite (SVG 644–651) |
| II.S6.47–48 | *AV+BV32+CV2*; *12121*, *23512*, *8923*; *711AV+710BV32+34CV2* | AV + BV^(3/2) + CV²; ½/121, 2/35½, 8/9⅔; 7/11 AV + 7/10 BV^(3/2) + ¾CV² | appiattimenti (SVG 652–658) |
| II.S6.49 | *120−8923 seu 119529*; *124331*; *62362* | 120 − 8/9⅔ = 119 5/29; 124 3/31; 62 3/62 | appiattimenti (SVG 659–662) |
| II.S6.49 | *acquirer posset* | *acquirere* | refuso probabile |
| II.S6.50 | *376150*; *1376150*; *3716*; *13342* | 376 1/50; 1/(376 1/50); 3 7/16; 1/3342 | appiattimenti (SVG 663–666) |
| II.S6.51 | *actava*; *descripti* | *octava*; *descripsi* | refusi probabili |
| II.S6.51 | riga «37427216212831341232223» | 374, 272, 162½, 83⅓, 41⅔, 22⅔ | tabella appiattita (Motte: 374, 272, SVG 668–671) |
| II.S6.52 | *uncicarum*; *numeram*; *2614* | *unciarum*; *numerum*; 26¼ | refusi; appiattimento (SVG 672) |
| II.S6.52 | «78 74 3127142856»; «22622819314090125330»; «3411236122448»; «510518420 31820412170» | ⅞, 7/4, 3½, 7, 14, 28, 56; 226, 228, 193, 140, 90½, 53, 30; ¾, 1½, 3, 6, 12, 24, 48; 510, 518, 420, 318, 204, 121, 70 | tabelle appiattite (SVG 673–676, 225, 667) |
| II.S6.53 | *12193*, *29012*, *830*; *Est si*; *713*; *4714*; *111316*; *713−13 ad 1−13* | ½/193, 2/90½, 8/30; *Et si*; 7⅓; 47¼; 11 13/16; 7⅓ − ⅓ a 1 − ⅓ | appiattimenti (SVG 677–687); refuso |
| II.S6.54 | *1834*, *12212*, *10912*, *25*, *6718* | 18¾, 122½, 109½, ⅖, 67⅛ | appiattimenti (SVG 688–693) |
| II.S6.55 | *uniciarum* (due volte); *descensu & ascensu descriptum*; *126121 in 8923* | *unciarum*; *descriptorum*; 126/121 × 8/9⅔ | refusi; appiattimento (SVG 694–695) |
| II.S6.56 | *resistentæ*; *351916*, *471764* | *resistentiæ*; 351 9/16, 47 17/64 | refuso; appiattimenti (SVG 696–697) |
| II.S6.57 | *coligetur* | *colligetur* | refuso probabile |
| II.S6.58 | *secique*; *{16616}*, *358*, *13438* | *fecique*; 166⅙, 3⅝, 134⅜ | refuso; appiattimenti (SVG 698–700) |
| II.S6.58 | righe della tabella (vedi sopra) | colonne ricostruite: in acqua mancano le colonne 1–2; in aria ci sono solo le colonne 1, 2, 4 | ricostruzione guidata da II.S6.59–60 (colonna 4: 535 in aria, 1⅕ in acqua) |
| II.S6.59 | *proprtio* | *proportio* | refuso probabile |
| II.S6.60 | *2535 ad 168512*; *8512*; *7C=44912*; *64314*; *2127*; *722AV*; *13611V+48956V2*; *611217* | 2/535 a 16/85½; 85½; 449½; 64 3/14; 21 2/7; **7/11** AV; 13 6/11 V + 48 9/56 V²; 61 12/17 | appiattimenti (SVG 714–725); 7/22 → 7/11 per il calcolo e per Motte |
| II.S6.60 | *velocitates* (*quadrato velocitates proportionalis*); *conjucntim*; *considerenda* | *velocitatis*; *conjunctim*; *consideranda* | refusi probabili |
| II.S6.61 | riga «338612 12112211534536215» | 3⅜, 6½, 12 1/12, 21⅕, 34, 53, 62⅕ | tabella appiattita (SVG 726–730) |
| II.S6.62 | *seccessive*; *neumerus*; *13 vel 23* | *successive*; *numerus*; ½ o ⅔ | refusi; lettura con Motte |
| II.S6.63 | *eoreum*; *tendento*; *septuagesima octava* | *eorum*; *tendente*; 1/78 (Motte SVG 731) | refusi |

### A.14 Punti da controllare sulla stampa ECCO

| Pagina 1726 | Trascrizione | Lettura attesa | Motivo |
|---|---|---|---|
| 297 | *arcus toti CD, OB* | *CB, OB* | coerenza con le frasi vicine e con Motte |
| 297 | *oscillaciones* | *oscillationes* | refuso |
| 298 | assenza di figura nella Prop. XXVII | figura 45 condivisa? | Motte ha una figura anche nella Prop. XXVII |
| 300 | *ut OQ ad OC* | *ut OQ ad OS* | C non è sulla retta OQ; Motte e N7 |
| 309 | *0,041748* | 0,041778 secondo il calcolo | possibile errore di Newton o di stampa (N11) |
| 310 | *Experimentum descripti*; *actava* | *descripsi*; *octava* | refusi |
| 310 | ultima cifra della tabella della quarta parte, 22⅔ | 22⅔ | Motte 1846 ha «22 1/1» |
| 311 | *Est si spectemus* | *Et si* | refuso |
| 311 | *4714* | 47¼ (non 47 17/64) | Newton arrotonda; Motte SVG 684 = 47¼ |
| 311–312 | *Ejus pars decima* | — | coerenza con «cinque oscillazioni» (N14) |
| 312 | *0,61675* | 0,61705? | p. 309 ha 0,61705; il calcolo 45,453 usa 0,61675 (N14) |
| 312 | *126121 in 8923* | 126/121 × 8/9⅔ | Motte 1846 ha 9 3/2 |
| 313 | *secique*; *{16616}* | *fecique*; 166⅙ | refuso; artefatto |
| 313 | allineamento delle righe «in aqua» / «in aere» | colonne 3–9 in acqua; 1, 2, 4 in aria | la trascrizione perde le celle vuote |
| 314 | *722AV* | *711AV* | il calcolo richiede 7/11; Motte 7/11 |
| 314 | *611217* | 61 12/17 | lettura confermata da Motte (SVG 722–723) |
| 315 | *quasi 13 vel 23 partes digiti* | ½ o ⅔ | «paulo majorem» di ⅓; Motte ½ |
| 315–316 | *seccessive*, *neumerus*, *eoreum*, *tendento* | forme corrette | refusi probabili della trascrizione |

---

## Note editoriali e fisiche

Queste note sono aggiunte del presente fascicolo, non affermazioni tradotte da Newton. Le verifiche sono state eseguite con tre script Python conservati con i materiali di lavoro (`tmp/17-L2-S6/`): `scolio.py` (aritmetica e tabelle dello Scolio, con frazioni esatte), `proposizioni.py` e `p27.py` (integrazione numerica del moto del pendolo cicloidale, *s*″ = −(*g*/*L*) *s* − *R*(*v*), con *R* costante, lineare, quadratica). Nella cicloide di Huygens la forza tangenziale è esattamente *mg s*/*L*, con *s* arco misurato dal punto più basso e *L* lunghezza del pendolo; l’arco dal punto più basso alla cuspide vale *L*, come dice Newton nella Prop. XXIX (CZ = lunghezza del pendolo).

### N1. Prop. XXIV: massa, peso e periodo

In termini moderni, per un pendolo di lunghezza *L*, *T* ∝ √(*mL*/*W*), cioè *m* ∝ *W T*²/*L* (Cor. 5). Il Cor. 7 è la verifica sperimentale della proporzionalità fra massa inerziale e peso: pendoli di uguale lunghezza e materiali diversi hanno lo stesso periodo. Newton descrive questi esperimenti (con oro, argento, piombo, vetro, sabbia, sale, legno, acqua, frumento) nel Libro III, Prop. VI (non verificato sulle fonti allegate). Il Cor. 6 tiene conto della spinta di Archimede: in un mezzo pesante conta il peso «comparativo», cioè il peso meno quello del fluido spostato.

### N2. «In rapporto ai momenti del tempo»: la resistenza costante

Se la resistenza è «come il momento del tempo», la sua azione in ogni particella di tempo è proporzionale alla particella stessa: la resistenza ha un valore fisso, come un attrito radente (attrito di Coulomb). Newton lo dice esplicitamente (*ideoque detur*). Il verso della resistenza si inverte con il moto: nella discesa si sottrae alla gravità (II.S6.11, terzo passo), nella salita si somma (undicesimo passo).

### N3. Propp. XXV e XXVIII: verifica numerica

Con resistenza costante *r* (per unità di massa), il moto in ogni semioscillazione è un moto armonico attorno al centro spostato O, con CO = *rL*/*g*. Lo script dà, per *r*/*g* = 0,002 e 0,01 e ampiezze 0,2 e 0,5 (unità di *L*): tempo della semioscillazione uguale a quello nel vuoto (rapporto 1,00000000), velocità massima esattamente nel punto medio O di Ba (Cor. della Prop. XXV), e Aa/(2*L*) = *r*/*g* (Prop. XXVIII). I due enunciati sono **esatti**, non approssimati.

### N4. Prop. XXVI: resistenza lineare

L’equazione è lineare: i moti con ampiezze diverse sono proporzionali e dunque isocroni (rapporto dei tempi 1,00031265 per ampiezze 0,1, 0,3, 0,6, con lo stesso rapporto a/B = 0,92444). L’enunciato è esatto. Il tempo è però un poco maggiore che nel vuoto: Newton qui confronta fra loro i pendoli nel mezzo resistente, non con il vuoto.

### N5. Prop. XXVII: un risultato che la verifica moderna non conferma

Newton afferma che, con resistenza quadratica, l’eccesso del tempo di oscillazione sul tempo nel vuoto è proporzionale all’arco. L’integrazione numerica dà invece un eccesso **proporzionale al quadrato dell’arco** (per *k* = 0,02: eccessi relativi 6,65·10⁻⁷, 2,65·10⁻⁶, 1,06·10⁻⁵, 4,18·10⁻⁵ per archi 0,1, 0,2, 0,4, 0,8) e al quadrato del coefficiente di resistenza (per arco 0,4: 2,65·10⁻⁶, 1,06·10⁻⁵, 4,18·10⁻⁵ per *k* = 0,01, 0,02, 0,04). Per smorzamenti piccoli, infatti, l’effetto della resistenza sul periodo è del secondo ordine (come per l’oscillatore smorzato linearmente, dove ω = ω₀√(1 − ζ²)). L’argomento di Newton suppone che l’eccesso sia proporzionale alla resistenza che lo produce («quegli eccessi sono come le forze che li producono»), cioè del primo ordine: è questo il passaggio che non regge. Le conclusioni qualitative del Cor. 2 (le oscillazioni brevi sono più isocrone, le lunghe un poco più lente) restano vere. Il testo non va corretto; la nota serve al curatore e alla pagina didattica.

### N6. Prop. XXIX: il passaggio differenziale

In termini moderni, con *R* = *k v*² e *s* l’arco, *d*(*v*²)/*ds* = 2(*V* − *R*) (con il verso del moto), e quindi *dR*/*ds* ∝ (*V* − *R*): è la frase di II.S6.24 («se il momento dello spazio è dato, come V − R»). Il Lemma II del Libro II serve a dire che il momento di *v*² è 2*v* per il momento di *v*. L’equazione è lineare in *R*, con *V* proporzionale all’arco: la soluzione contiene un esponenziale dell’arco, ed è per questo che Newton rappresenta gli archi con aree iperboliche (logaritmi).

### N7. Prop. XXIX: verifica numerica della costruzione con l’iperbole

Iperbole *xy* = 1, P in *x* = 1 (I = (1, 1)), Q in *x* = *q*, S in *x* = *s*. Aree: PIEQ = ln *q*, PITS = ln(1/*s*), IEF = (*q* − 1) − ln *q*, ILT = ln(1/*s*) − (1 − *s*), IGH = (*r* − 1) − ln *r* per R in *x* = *r*. Dalla simulazione si ricavano BC e Ca; si risolvono le due condizioni di Newton (PIEQ : PITS = BC : Ca e IEF : ILT = OQ : **OS**) per *q* e *s*; poi si confronta, lungo tutta la discesa e la salita, [(OR/OQ)·IEF − IGH]/PINM con la resistenza simulata *R*/*g*. Tre prove (*k* = 0,3, 1, 0,1; ampiezze 0,5, 0,4, 0,8): scarto massimo 1–2·10⁻¹², contro resistenze dell’ordine di 10⁻¹. **La costruzione è esatta**, e richiede OS (con «OC» non avrebbe senso). Anche i corollari tornano: Cor. 1, resistenza in C = (OP/OQ)·IEF/PINM, con accordo a 10⁻⁷; Cor. 2, il massimo cade dove PIHR : IEF = OR : OQ (accordo entro il passo della griglia), cioè dove la resistenza uguaglia la forza di gravità tangenziale. Cor. 3: «proprio all’inizio del moto» la velocità è nulla in entrambi i casi; il senso è che il fattore di proporzionalità fra la velocità e la radice della resistenza si fissa confrontando i due moti nell’istante iniziale, quando la resistenza non ha ancora agito.

### N8. Prop. XXX e corollario

La Prop. XXX è il **teorema dell’energia** in forma geometrica: la perdita di «altezza» MN, moltiplicata per CM, eguaglia il lavoro della resistenza Dd × DK; il trapezio ha basi CB e Ca e altezza Aa = CB − Ca, quindi area (CB² − Ca²)/2 = Aa × ½aB. Nelle simulazioni l’uguaglianza area BKa = Aa × ½aB è verificata esattamente per resistenza costante, lineare e quadratica. Il corollario: con *R* ∝ *v*ⁿ e profilo di velocità circa ellittico, OV = Aa / ∫₋₁¹(1 − *x*²)^(n/2) *dx*, cioè ½Aa (n = 0), (2/π)Aa = 0,6366 Aa (n = 1; Newton 7/11 = 0,6364, da 11 : 7 ≈ π/2), ¾Aa (n = 2; per profilo esattamente ellittico la figura è esattamente una parabola), 0,6955 Aa (n = 3/2; Newton usa 7/10 nello Scolio, II.S6.48, senza giustificarlo). Nelle simulazioni con smorzamento piccolo: resistenza in O 4,961·10⁻³ contro 7/11 Aa = 4,959·10⁻³ (lineare), 4,9343·10⁻³ contro ¾Aa = 4,9343·10⁻³ (quadratica).

### N9. Prop. XXXI

Verificata numericamente: con resistenza lineare, raddoppiando l’arco la differenza Aa raddoppia (rapporti 2,000, 2,000); con resistenza quadratica quadruplica (3,995, 3,989). È il Cor. 1–2, su cui poggia tutto lo Scolio.

### N10. Lo Scolio: dal cerchio alla cicloide e i coefficienti

I pendoli reali oscillano in archi di cerchio, non di cicloide. Newton argomenta che le differenze degli archi sono circa le stesse nelle due curve: nel cerchio la velocità massima è come la corda, nella cicloide come l’arco; la resistenza (∝ *v*²) e il quadrato del tempo (∝ 1/*v*²) cambiano in rapporti inversi e si compensano. La riduzione consiste quindi nel tenere le differenze osservate e porre le velocità proporzionali agli archi. Il modello AV + BV^(3/2) + CV² è una legge di resistenza empirica a tre termini; in termini moderni, i termini lineare e quadratico corrispondono al regime viscoso e a quello inerziale.

### N11. Primo esperimento (globo di legno, ottava parte del moto)

Ricalcolo con frazioni esatte (`scolio.py`):

| Prima discesa | 2 | 4 | 8 | 16 | 32 | 64 |
|---|---:|---:|---:|---:|---:|---:|
| Ultima salita (⅞ della discesa) | 1¾ | 3½ | 7 | 14 | 28 | 56 |
| Differenza (⅛ della discesa) | ¼ | ½ | 1 | 2 | 4 | 8 |
| Oscillazioni | 164 | 121 | 69 | 35½ | 18½ | 9⅔ |
| Arco medio (discesa + salita) | 3¾ | 7½ | 15 | 30 | 60 | 120 |
| Differenza per oscillazione | 1/656 | 1/242 | 1/69 | 4/71 | 8/37 | 24/29 |
| V (cicloide) | ½ | 1 | 2 | 4 | 8 | 16 |

- Tutte le colonne derivate tornano esattamente. Le salite dei casi 3–6 non sono date nel testo: sono ricavate.
- Il sistema dei casi 2, 4, 6 dà A = 0,00009165, B = 0,00108474, C = 0,00295585: Newton 0,0000916, 0,0010847, 0,0029558. **Torna.**
- 7/11 A = 0,0000583, 7/10 B = 0,0007593, ¾ C = 0,0022169: **tornano.**
- Resistenza per V = 1: 0,0030345 (**torna**); per V = 16: 0,6170544 (Newton 0,61705, **torna**); per V = 4: 0,0002332 + 0,0060744 + 0,0354704 = **0,041778**, Newton **0,041748**. **Non torna** alla quinta cifra (scarto 0,00003, 0,07 %): errore di calcolo o di stampa; da controllare sulla stampa (p. 309). Non corretto nel testo.
- Il modello prevede, per i casi non usati (1, 3, 5), differenze per oscillazione 0,00117, 0,01507, 0,2144 contro le osservate 0,00152, 0,01449, 0,2162: buono per i casi veloci, scarto del 23 % nel caso più lento.
- 120 − 8/9⅔ = 119 5/29 (**torna**); × 126/121 = 124,0969, Newton 124 3/31 = 124,0968 (**torna**); metà 62 3/62 (**torna**); seno verso 62,0484²/252 = 15,2778, Newton 15,278 (**torna**); 121 × 97/55 = 213,4 (**torna**); 213,4/0,56752 = 376,02 = 376 1/50 (**torna**); 30,556 = 2 × 15,278 (spazio percorso a velocità costante nel tempo di caduta: **torna**); 376,02 × 30,556 / 3,4375 = 3342,4 → 1/3342 (**torna**).

### N12. «Tenti il calcolo chi vorrà»: la tabella della quarta parte

Differenze per oscillazione (¼ della discesa diviso per il numero delle oscillazioni): 0,001337, 0,003676, 0,012308, 0,0480, 0,1920, 0,7059. Con lo stesso metodo (casi 2, 4, 6; V = 1, 4, 16) si ottiene A = 0,000510, B = 0,000588, C = 0,002578. Il coefficiente C, che conta per le velocità grandi, differisce del 13 % da quello della tabella dell’ottava parte (0,002956): la differenza è dello stesso ordine dello scarto fra le due serie di osservazioni (le differenze per oscillazione della quarta parte sono l’85–89 % di quelle dell’ottava parte a parità di discesa iniziale). Le salite ultime sono esattamente ¾ delle discese. Calcolo del curatore, non di Newton.

### N13. Il globo di piombo

- Le salite sono esattamente ⅞ e ¾ delle discese in entrambe le tabelle.
- Equazioni: ½/193 = 0,0025907, 2/90½ = 0,0220994, 8/30 = 0,2666667. Il sistema dà A = 0,0014143, B = 0,0002975, C = 0,0008789: Newton 0,001414, 0,000297, 0,000879. **Tornano.** 7/11 A = 0,0009, 7/10 B = 0,000208, ¾C = 0,000659: **tornano.**
- Legno : piombo = 57 7/22 × 0,002217 : 26¼ × 0,000659 = 7,346 : 1; Newton 7⅓ (**torna**, arrotondato).
- (6⅞)² = 47 17/64; Newton scrive 47¼ e 11 13/16 (= 47¼/4); il valore esatto è 11,816 (**torna** «quam proxime»).
- (7⅓ − ⅓)/(1 − ⅓) = 10½ (**torna**). L’ipotesi è che il filo assorba ⅓ (in unità della resistenza del globo di piombo) in entrambi i pendoli, perché il filo è lo stesso.
- Il modello prevede, per le osservazioni 1, 2, 4, 6, differenze 0,00045, 0,00103, 0,00719, 0,0743 contro le osservate 0,00055, 0,00110, 0,00714, 0,0755.

### N14. Il globo grande

- 60 × 122½/109½ = 67,123 (Newton 67⅛, **torna**); ⅖ × 122½/109½ = 0,44749 (0,4475, **torna**); 0,4475 × (124 3/31 / 67⅛)² = 1,52949 (1,5295, **torna**); × 208 = 318,136 (**torna**); 126/121 × 8/9⅔ × 57 7/22 = 49,3959 (49,396, **torna**); 318,136/45,453 = 6,999 (7, **torna**); 351 9/16 / 47 17/64 = 7,438 (**torna**).
- **Non torna:** il rapporto «0,56752 a 0,61675». A p. 309 la resistenza totale del caso sesto è **0,61705**; qui Newton scrive **0,61675**, e il suo 45,453 è calcolato proprio con 0,61675 (49,396 × 0,56752/0,61675 = 45,4531; con 0,61705 si avrebbe 45,431). Uno dei due valori è un errore di Newton o di stampa; l’effetto sul rapporto finale (7 : 1) è trascurabile. Motte ha gli stessi numeri. Non corretto nel testo.
- «La sua decima parte»: dividendo la differenza di 4 pollici, ottenuta «dopo cinque oscillazioni», per 10 si ottiene la differenza per semioscillazione; è coerente solo se le «cinque oscillazioni» sono oscillazioni doppie (andata e ritorno), diversamente dal resto dello Scolio, dove ogni oscillazione è una discesa con la salita successiva. Segnalato, non corretto.
- Il peso del globo grande (208 once) non è dato altrove; non verificabile.

### N15. Acqua e aria

- Salite = ¾ delle discese, differenze = ¼ (**tornano**). Ricostruzione delle colonne: vedi § A.13.
- 2/535 : 16/85½ = 85½ : 4280 (**torna**); 4280/8 = 535 (**torna**); 7C = 449½, C = 64 3/14, A = 21 2/7 (**tornano**); 7/11 A = 13 6/11 (**torna**; con il 7/22 della trascrizione si avrebbe 6 17/22, che **non** torna con il testo); ¾C = 48 9/56 (**torna**); 13 6/11 + 48 9/56 = 61,7062, Newton 61 12/17 = 61,7059 (**torna** con ottima approssimazione); (61 12/17 / 48 9/56) × (535/1⅕) = 571,2 (571, **torna**).
- 850 : 1 è la stima di Newton del rapporto delle densità acqua/aria; il valore moderno, a 15–20 °C e pressione normale, è circa 830 (non verificato sulle fonti allegate).
- La crescita «più che duplicata» si vede nella tabella: il rapporto fra differenze per oscillazione di colonne successive (archi dimezzati) vale circa 5,0, 5,0, 4,7 nelle colonne veloci (4 corrisponderebbe al rapporto duplicato).

### N16. Due globi, mercurio e liquidi

- Tabella dei due globi: salite = ¾, differenze = ¼ (**tornano**). Differenze per oscillazione 1,185, 0,3077, 0,0828, 0,0236, 0,00735, 0,00236, 0,00101; rapporti fra colonne successive 3,85, 3,72, 3,51, 3,21, 3,12, 2,35: vicini a 4 (rapporto duplicato) per le velocità maggiori, come dice Newton.
- Mercurio : acqua = 13 o 14 : 1; il valore moderno della densità relativa del mercurio è circa 13,6 (non verificato sulle fonti allegate).
- *Oleum vitrioli* è l’acido solforico concentrato; *spiritus vini* l’alcol etilico; *spiritus salium* gli acidi minerali ottenuti dai sali (identificazioni non verificate sulle fonti allegate).

### N17. La scatola e il mezzo etereo

L’algebra è corretta: da (A + B) : (A + 78B) = 77 : 78 segue A = 77 × 77 B − B = 5928 B. Il ragionamento presuppone che la resistenza interna sia proporzionale alla quantità di materia. L’esperimento serve a Newton contro l’ipotesi di un etere che attraversi liberamente i corpi e resista alle loro parti interne; lo Scolio lo collega, con gli esperimenti sui globi, alla «dimostrazione del vuoto» (II.S6.57). Newton stesso dichiara l’esperimento riferito a memoria, con numeri arrotondati.

### N18. Unità di misura

Il testo usa once romane, pollici e piedi londinesi. Motte traduce l’oncia romana con l’oncia troy, che è un’unità diversa. Il fascicolo non converte le misure; i fattori di conversione andrebbero presi da una fonte metrologica (non verificati sulle fonti allegate). Tutti i calcoli di Newton sono rapporti, e non dipendono dalle unità.

---

## Controllo della copertura

Pagine 1726 dai marcatori ‹n› della trascrizione; per Motte, la sezione corrispondente (l’estratto non ha marcatori di pagina).

| Identificatori | Incipit latino | Contenuto | 1726 | Motte 1846 |
|---|---|---|---|---|
| II.S6.01–II.S6.02 | *Quantitates materiæ in corporibus funependulis* | Prop. XXIV | pp. 294–295 | Prop. XXIV |
| II.S6.03–II.S6.09 | *Ideoque si tempora sunt æqualia* … *Et hinc liquet ratio* | Prop. XXIV, Cor. 1–7 | p. 295 | Cor. 1–7 |
| II.S6.10–II.S6.12 | *Corpora Funependula quibus* | Prop. XXV e Cor. | pp. 295–297 | Prop. XXV |
| II.S6.13–II.S6.14 | *Corporum funependulorum, quibus resistitur in ratione velocitatum* | Prop. XXVI | p. 297 | Prop. XXVI |
| II.S6.15–II.S6.18 | *Si corporibus funependulis resistitur in duplicata* | Prop. XXVII, Cor. 1–2 | pp. 298–299 | Prop. XXVII |
| II.S6.19–II.S6.20 | *Si corpori funependulo in cycloide oscillanti* | Prop. XXVIII | p. 299 | Prop. XXVIII |
| II.S6.21–II.S6.30 | *Posito quod corpori in cycloide oscillanti* … *Cæterum ob difficilem calculum* | Prop. XXIX, Cor. 1–3, chiusa | pp. 300–303 | Prop. XXIX |
| II.S6.31–II.S6.37 | *Si recta aB æqualis sit* … *Atque has conclusiones* | Prop. XXX e Cor. | pp. 303–306 | Prop. XXX |
| II.S6.38–II.S6.44 | *Si corporis oscillantis resistentia* | Prop. XXXI, Cor. 1–5 | pp. 306–307 | Prop. XXXI |
| II.S6.45–II.S6.50 | *Ex his propositionibus* … *partem 1/3342* | Scolio: globo di legno, ottava parte | pp. 307–310 | General Scholium |
| II.S6.51 | *Numerabam etiam oscillationes* | tabella della quarta parte | p. 310 | idem |
| II.S6.52–II.S6.53 | *Postea globum plumbeum* | globo di piombo, due tabelle, filo | pp. 310–311 | idem |
| II.S6.54–II.S6.57 | *Cum resistentia fili* … *quid in globis adhuc majoribus* | globo grande; auspicio di nuovi esperimenti | pp. 311–313 | idem |
| II.S6.58–II.S6.61 | *Jam vero conferendo resistentias* … *in tabula sequente describitur* | acqua e aria; due tabelle | pp. 313–315 | idem |
| II.S6.62 | *Conferendo resistentias mediorum* | mercurio e altri liquidi | pp. 315–316 | idem |
| II.S6.63–II.S6.65 | *Denique cum nonnullorum opinio sit* … *uti supra descripsimus* | la scatola piena e vuota | pp. 316–317 | idem |

**Controlli eseguiti.**

1. **Copertura.** Ho riletto in sequenza ogni periodo della trascrizione, da *Quantitates materiæ* a *uti supra descripsimus*, contro la traduzione: nessuna frase manca. I 65 identificatori sono consecutivi e unici (controllo automatico). Le cinque tabelle sono riprodotte per intero.
2. **Parte B.** `check.py` sul file finale: esito riportato nel messaggio di consegna. Il testo italiano delle Propp. XXV, XXVIII, XXIX, XXX (con Cor.) e XXXI è generato dagli stessi campi `it` della Parte B, quindi coincide parola per parola.
3. **Matematica.** Verifiche numeriche delle Propp. XXV–XXXI (N3–N9) e ricalcolo completo dello Scolio e delle tabelle (N11–N17). Cifre che non tornano: 0,041748 (N11), 0,61675/0,61705 (N14); più il 7/22 della trascrizione (N15). Risultato fisico non confermato: Prop. XXVII (N5).
4. **Motte.** Confronto di tutta la sezione e lettura di tutte le 119 formule SVG (§ A.11–A.12).

**Non ho potuto verificare:**

- **la stampa del 1726** e **Motte 1729**: i punti del § A.14 restano aperti;
- **le figure originali** NATP00088-44…50: la posizione dei punti (per esempio il lato su cui è innalzata DK, la disposizione di S, P, Q sull’asintoto) è ricostruita dal testo e dalla verifica numerica;
- **la paginazione di Motte**;
- i dati sperimentali in sé (pesi dei globi, numero delle oscillazioni), che si possono solo controllare per coerenza interna.

---

## Registro del lavoro successivo

| Unità | Stato |
|---|---|
| Libro II, Sezione VI (Propp. XXIV–XXXI, Scolio generale) | **Fascicolo 17, presente documento, prima versione** |
| Punti del § A.14 | Da controllare sulla scansione ECCO (in particolare OC/OS, 7/22, 0,041748, 0,61675, ⅓/½) |
| Prop. XXVII | Decidere come presentare nella pagina didattica il risultato della verifica moderna (N5) |
| Rimando al Lemma II del Libro II | Allineare la resa con il Fascicolo 14 |
| Termini nuovi (§ A.0) | Da armonizzare con gli altri fascicoli del Libro II (*peso comparativo* anche nel Fascicolo 16) |
| Pagine interattive | Parte B: 6 unità; la Prop. XXIX è la candidata ideale per una pagina con simulazione (N7) |
| Figure NATP00088-44…50 | Da consultare |
| Revisione filologica e scientifica indipendente | Da eseguire |

Il presente testo è una nuova traduzione assistita da IA. Non riproduce traduzioni italiane o inglesi moderne. **Licenza prevista** (decisione del curatore, Fascicolo 3): testi e traduzioni CC BY-SA 4.0, codice MIT. La trascrizione latina è © The Newton Project; i testi di Motte sono di pubblico dominio.

---

## Parte B — Dati per le pagine interattive

Unità incluse: le proposizioni con figura e dimostrazione geometrica — **Propp. XXV, XXVIII, XXIX, XXX, XXXI** — e il **corollario della Prop. XXX**, che ha una dimostrazione propria sulla stessa figura. **Escluse**: la Prop. XXIV (argomento dinamico senza figura), le Propp. XXVI e XXVII (senza figura nel latino), i corollari senza dimostrazione propria, lo Scolio generale (sperimentale; le tabelle sono nel testo e nelle note N11–N16).

Convenzioni:

- `la`: testo latino esatto della trascrizione, refusi e frazioni appiattite compresi; le letture sono in `nota` e nell’apparato;
- `it`: la traduzione di questo fascicolo (il testo delle proposizioni è generato da questi campi);
- `en`: Motte 1846, allineato frase per frase; le formule `[SVG n]` restano come marcatori e vanno rese dalle immagini (tutte lette: § A.11);
- `dipende_da`: soltanto i rimandi citati nella frase latina;
- `figura.mostra`: elementi da rendere visibili, cumulativi; `figura.evidenzia`: relazioni da mettere in risalto.

```json
{
 "fascicolo": "17-L2-S6",
 "versione": "0.1",
 "data": "2026-11-08",
 "convenzioni": {
  "dipende_da": "solo rimandi citati esplicitamente nella frase latina",
  "en": "Motte 1846, allineato frase per frase; le formule stampate come immagini restano come marcatori [SVG n] (tutte lette: apparato A.11)",
  "figura.mostra": "elementi da rendere visibili al passo, cumulativi salvo indicazione",
  "la": ""
 },
 "unita": [
  {
   "id": "L2-P25",
   "tipo": "Propositio/Theorema",
   "titolo": "Prop. XXV — resistenza costante: oscillazioni isocrone nella cicloide",
   "copertura": [
    "II.S6.10",
    "II.S6.11"
   ],
   "fonti": {
    "la": "",
    "en": "Motte 1846, sezione corrispondente (Section VI, Prop. XXV)"
   },
   "enunciato": {
    "la": "",
    "it": "I corpi appesi a un filo che, in un mezzo qualsiasi, incontrano una resistenza in rapporto ai momenti del tempo, e i corpi appesi a un filo che si muovono in un mezzo non resistente della stessa gravità specifica, compiono le oscillazioni nella cicloide nello stesso tempo e descrivono insieme parti proporzionali degli archi.",
    "en": "Funependulous bodies that are, in any medium, resisted in the ratio of the moments of time, and funependulous bodies that move in a non-resisting medium of the same specific gravity, perform their oscillations in a cycloid in the same time, and describe proportional parts of arcs together."
   },
   "figura_base": {
    "punti": [
     "A",
     "a",
     "B",
     "C",
     "O",
     "D",
     "d",
     "E",
     "e"
    ],
    "vincoli": [
     "AB arco di cicloide (moto nel vuoto), C punto medio e punto più basso",
     "CO parte data dell'arco: rappresenta la resistenza costante",
     "O fra C e B; Od : CD = OB : CB",
     "aB arco descritto nel mezzo resistente, con aB : AB = OB : CB; O punto medio di aB",
     "forza nel vuoto in D come CD; forza nel mezzo resistente in d come Od"
    ]
   },
   "passi": [
    {
     "id": "L2-P25-p1",
     "la": "",
     "it": "Sia AB un arco di cicloide che il corpo D, oscillando in un mezzo non resistente, descrive in un tempo qualsiasi.",
     "en": "Let AB be an arc of a cycloid, which a body D, by vibrating in a non-resisting medium, shall describe in any time.",
     "dipende_da": [],
     "figura": {
      "mostra": [
       "arco di cicloide AB",
       "corpo D"
      ]
     }
    },
    {
     "id": "L2-P25-p2",
     "la": "",
     "it": "Lo si divida a metà in C, in modo che C sia il suo punto più basso; la forza acceleratrice da cui il corpo è sollecitato in un luogo qualsiasi D, d o E sarà come la lunghezza dell’arco CD, Cd o CE.",
     "en": "Bisect that arc in C, so that C may be the lowest point thereof; and the accelerative force with which the body is urged in any place D, or d or E, will be as the length of the arc CD, or Cd, or CE.",
     "dipende_da": [],
     "figura": {
      "mostra": [
       "C (punto medio, punto più basso)",
       "luoghi D, d, E",
       "archi CD, Cd, CE"
      ],
      "evidenzia": [
       "forza acceleratrice come l’arco misurato da C"
      ]
     },
     "nota": "La proporzionalità della forza tangenziale all’arco nella cicloide non è citata qui; è il Cor. della Prop. LI del Libro I (nel caso limite della cicloide comune, Cor. 2 della Prop. LII)."
    },
    {
     "id": "L2-P25-p3",
     "la": "",
     "it": "Si rappresenti quella forza con lo stesso arco; e poiché la resistenza è come il momento del tempo, e quindi è data, la si rappresenti con la parte data CO dell’arco di cicloide, e si prenda l’arco Od in modo che stia all’arco CD nel rapporto che l’arco OB ha con l’arco CB. La forza da cui il corpo è sollecitato in d nel mezzo resistente, essendo l’eccesso della forza Cd sulla resistenza CO, sarà rappresentata dall’arco Od; e perciò starà alla forza da cui il corpo D è sollecitato nel mezzo non resistente, nel luogo D, come l’arco Od sta all’arco CD; e quindi anche nel luogo B come l’arco OB sta all’arco CB.",
     "en": "Let that force be expressed by that same arc; and since the resistance is as the moment of the time, and therefore given, let it be expressed by the given part CO of the cycloidal arc, and take the arc Od in the same ratio to the arc CD that the arc OB has to the arc CB: and the force with which the body in d is urged in a resisting medium, being the excess of the force Cd above the resistance CO, will be expressed by the arc Od, and will therefore be to the force with which the body D is urged in a non-resisting medium in the place D, as the arc Od to the arc CD; and therefore also in the place B, as the arc OB to the arc CB.",
     "dipende_da": [],
     "figura": {
      "mostra": [
       "punto O e arco CO (resistenza)",
       "arco Od",
       "arco OB"
      ],
      "evidenzia": [
       "Od : CD = OB : CB",
       "forza in d = Cd − CO = Od"
      ]
     }
    },
    {
     "id": "L2-P25-p4",
     "la": "",
     "it": "Se dunque due corpi D, d partono dal luogo B e sono sollecitati da queste forze, poiché all’inizio le forze sono come gli archi CB e OB, le velocità iniziali e gli archi descritti per primi staranno nello stesso rapporto.",
     "en": "Therefore if two bodies D, d go from the place B, and are urged by these forces; since the forces at the beginning are as the arc CB and OB, the first velocities and arcs first described will be in the same ratio.",
     "dipende_da": [],
     "figura": {
      "mostra": [
       "i due corpi in B all’istante iniziale"
      ],
      "evidenzia": [
       "forze iniziali come CB e OB"
      ]
     }
    },
    {
     "id": "L2-P25-p5",
     "la": "",
     "it": "Siano BD e Bd quegli archi: anche gli archi restanti CD, Od staranno nello stesso rapporto.",
     "en": "Let those arcs be BD and Bd, and the remaining arcs CD, Od, will be in the same ratio.",
     "dipende_da": [],
     "figura": {
      "mostra": [
       "archi BD, Bd",
       "archi restanti CD, Od"
      ]
     }
    },
    {
     "id": "L2-P25-p6",
     "la": "",
     "it": "Perciò le forze, proporzionali a CD e Od, resteranno nello stesso rapporto che all’inizio, e quindi i corpi continueranno a descrivere insieme archi nello stesso rapporto.",
     "en": "Therefore the forces, being proportional to those arcs CD, Od, will remain in the same ratio as at the beginning, and therefore the bodies will continue describing together arcs in the same ratio.",
     "dipende_da": [],
     "figura": {
      "mostra": [
       "forze come CD e Od"
      ]
     }
    },
    {
     "id": "L2-P25-p7",
     "la": "",
     "it": "Dunque le forze, le velocità e gli archi restanti CD, Od staranno sempre come gli archi interi CB, OB, e perciò quegli archi restanti saranno descritti insieme.",
     "en": "Therefore the forces and velocities and the remaining arcs CD, Od, will be always as the whole arcs CB, OB, and therefore those remaining arcs will be described together.",
     "dipende_da": [],
     "figura": {
      "mostra": [
       "archi interi CB, OB"
      ],
      "evidenzia": [
       "rapporto costante CB : OB"
      ]
     },
     "nota": "La trascrizione ha «arcus toti CD, OB»; il senso (e Motte) richiede CB, OB: refuso probabile, tradotto secondo il senso (apparato A.2, A.13)."
    },
    {
     "id": "L2-P25-p8",
     "la": "",
     "it": "I due corpi D, d giungeranno quindi insieme ai luoghi C e O: l’uno, nel mezzo non resistente, al luogo C; l’altro, nel mezzo resistente, al luogo O.",
     "en": "Therefore the two bodies D and d will arrive together at the places C and O; that which moves in the non-resisting medium, at the place C, and the other, in the resisting medium, at the place O.",
     "dipende_da": [],
     "figura": {
      "mostra": [
       "D in C",
       "d in O"
      ],
      "evidenzia": [
       "arrivo simultaneo"
      ]
     }
    },
    {
     "id": "L2-P25-p9",
     "la": "",
     "it": "Poiché poi le velocità in C e in O sono come gli archi CB, OB, gli archi che i corpi descrivono insieme procedendo oltre staranno nello stesso rapporto.",
     "en": "Now since the velocities in C and O are as the arcs CB, OB, the arcs which the bodies describe when they go farther will be in the same ratio.",
     "dipende_da": [],
     "figura": {
      "mostra": [
       "velocità in C e in O"
      ]
     }
    },
    {
     "id": "L2-P25-p10",
     "la": "",
     "it": "Siano questi CE e Oe.",
     "en": "Let those arcs be CE and Oe.",
     "dipende_da": [],
     "figura": {
      "mostra": [
       "archi CE, Oe (salita)"
      ]
     }
    },
    {
     "id": "L2-P25-p11",
     "la": "",
     "it": "La forza da cui il corpo D, nel mezzo non resistente, è ritardato in E è come CE; e la forza da cui il corpo d, nel mezzo resistente, è ritardato in e è come la somma della forza Ce e della resistenza CO, cioè come Oe. Perciò le forze da cui i corpi sono ritardati stanno come gli archi CB, OB, proporzionali agli archi CE, Oe; e quindi le velocità, ritardate in quel rapporto dato, restano in quello stesso rapporto dato.",
     "en": "The force with which the body D in a non-resisting medium is retarded in E is as CE, and the force with which the body d in the resisting medium is retarded in e, is as the sum of the force Ce and the resistance CO, that is, as Oe; and therefore the forces with which the bodies are retarded are as the arcs CB, OB, proportional to the arcs CE, Oe; and therefore the velocities, retarded in that given ratio, remain in the same given ratio.",
     "dipende_da": [],
     "figura": {
      "mostra": [
       "luoghi E, e"
      ],
      "evidenzia": [
       "forza ritardatrice in e = Ce + CO = Oe"
      ]
     }
    },
    {
     "id": "L2-P25-p12",
     "la": "",
     "it": "Le velocità, dunque, e gli archi descritti con esse stanno sempre fra loro nel rapporto dato degli archi CB e OB; e perciò, se si prendono gli archi interi AB, aB nello stesso rapporto, i corpi D, d descriveranno insieme questi archi e perderanno insieme tutto il loro moto nei luoghi A e a.",
     "en": "Therefore the velocities and the arcs described with those velocities are always to each other in that given ratio of the arcs CB and OB; and therefore if the entire arcs AB, aB are taken in the same ratio, the bodies D and d will describe those arcs together, and in the places A and a will lose all their motion together.",
     "dipende_da": [],
     "figura": {
      "mostra": [
       "punto a",
       "archi interi AB, aB"
      ],
      "evidenzia": [
       "aB : AB = OB : CB"
      ]
     }
    },
    {
     "id": "L2-P25-p13",
     "la": "",
     "it": "Le oscillazioni intere sono dunque isocrone, e parti qualsiasi degli archi, BD, Bd o BE, Be, descritte insieme, sono proporzionali agli archi interi BA, Ba. C.V.D.",
     "en": "Therefore the whole oscillations are isochronal, or are performed in equal times; and any parts of the arcs, as BD, Bd, or BE, Be, that are described together, are proportional to the whole arcs BA, Ba. Q.E.D.",
     "dipende_da": [],
     "figura": {
      "mostra": [
       "oscillazioni intere BA e Ba"
      ],
      "evidenzia": [
       "isocronismo"
      ]
     },
     "nota": "«oscillaciones» è refuso probabile della trascrizione per «oscillationes». Motte aggiunge «or are performed in equal times»."
    }
   ]
  },
  {
   "id": "L2-P28",
   "tipo": "Propositio/Theorema",
   "titolo": "Prop. XXVIII — resistenza costante misurata dalla differenza degli archi",
   "copertura": [
    "II.S6.19",
    "II.S6.20"
   ],
   "fonti": {
    "la": "",
    "en": "Motte 1846, sezione corrispondente (Prop. XXVIII)"
   },
   "enunciato": {
    "la": "",
    "it": "Se un corpo appeso a un filo, che oscilla in una cicloide, incontra una resistenza in rapporto ai momenti del tempo, la sua resistenza starà alla forza di gravità come l’eccesso dell’arco descritto nell’intera discesa sull’arco descritto nella salita successiva sta al doppio della lunghezza del pendolo.",
    "en": "If a funependulous body, oscillating in a cycloid, be resisted in the ratio of the moments of the time, its resistance will be to the force of gravity as the excess of the arc described in the whole descent above the arc described in the subsequent ascent to twice the length of the pendulum."
   },
   "figura_base": {
    "punti": [
     "A",
     "a",
     "B",
     "C",
     "O",
     "D"
    ],
    "vincoli": [
     "costruzione della Prop. XXV",
     "BC arco di discesa, Ca arco di salita, Aa = BC − Ca",
     "CO = ½Aa",
     "semiarco della cicloide (dal punto più alto a C) = lunghezza del pendolo"
    ]
   },
   "passi": [
    {
     "id": "L2-P28-p1",
     "la": "",
     "it": "BC indichi l’arco descritto nella discesa, Ca l’arco descritto nella salita e Aa la differenza degli archi; e, ferme restando la costruzione e la dimostrazione della Prop. XXV, la forza da cui il corpo oscillante è sollecitato in un luogo qualsiasi D starà alla forza della resistenza come l’arco CD sta all’arco CO, che è la metà di quella differenza Aa.",
     "en": "Let BC represent the arc described in the descent, Ca the arc described in the ascent, and Aa the difference of the arcs: and things remaining as they were constructed and demonstrated in Prop. XXV, the force with which the oscillating body is urged in any place D will be to the force of resistance as the arc CD to the arc CO, which is half of that difference Aa.",
     "dipende_da": [
      "Prop. XXV"
     ],
     "figura": {
      "mostra": [
       "arco di discesa BC",
       "arco di salita Ca",
       "differenza Aa",
       "CO = ½Aa",
       "luogo D"
      ],
      "evidenzia": [
       "forza in D : resistenza = CD : CO"
      ]
     }
    },
    {
     "id": "L2-P28-p2",
     "la": "",
     "it": "Perciò la forza da cui il corpo oscillante è sollecitato all’inizio della cicloide, cioè nel suo punto più alto, ossia la forza di gravità, starà alla resistenza come l’arco di cicloide compreso fra quel punto più alto e il punto più basso C sta all’arco CO; cioè (se si raddoppiano gli archi) come l’arco dell’intera cicloide, ossia il doppio della lunghezza del pendolo, sta all’arco Aa. C.V.D.",
     "en": "Therefore the force with which the oscillating body is urged at the beginning or the highest point of the cycloid, that is, the force of gravity, will be to the resistance as the arc of the cycloid, between that highest point and lowest point C, is to the arc CO; that is (doubling those arcs), as the whole cycloidal arc, or twice the length of the pendulum, to the arc Aa. Q.E.D.",
     "dipende_da": [],
     "figura": {
      "mostra": [
       "punto più alto della cicloide",
       "semiarco = lunghezza del pendolo",
       "cicloide intera"
      ],
      "evidenzia": [
       "gravità : resistenza = 2·lunghezza del pendolo : Aa"
      ]
     },
     "nota": "Nel punto più alto (cuspide) la tangente della cicloide è verticale, e la forza tangenziale coincide con l’intera gravità."
    }
   ]
  },
  {
   "id": "L2-P29",
   "tipo": "Propositio/Problema",
   "titolo": "Prop. XXIX — resistenza in rapporto duplicato della velocità: costruzione con l’iperbole",
   "copertura": [
    "II.S6.21",
    "II.S6.22",
    "II.S6.23",
    "II.S6.24",
    "II.S6.25",
    "II.S6.26"
   ],
   "fonti": {
    "la": "",
    "en": "Motte 1846, sezione corrispondente (Prop. XXIX)"
   },
   "enunciato": {
    "la": "",
    "it": "Supposto che un corpo che oscilla in una cicloide incontri una resistenza in rapporto duplicato della velocità, trovare la resistenza nei singoli luoghi.",
    "en": "Supposing that a body oscillating in a cycloid is resisted in a duplicate ratio of the velocity: to find the resistance in each place."
   },
   "figura_base": {
    "punti": [
     "B",
     "a",
     "C",
     "Z",
     "D",
     "d",
     "O",
     "S",
     "P",
     "Q",
     "R",
     "r",
     "M",
     "N",
     "K",
     "T",
     "I",
     "G",
     "g",
     "H",
     "h",
     "E",
     "L",
     "F"
    ],
    "vincoli": [
     "iperbole TIGE con centro O e asintoti OK, OQ (OR × RG costante)",
     "S, P, Q, R, M sull’asintoto OQ; ST, PI, QE, RG, MN perpendicolari",
     "KF per I parallela a OQ; L su ST, F su QE, H su RG",
     "area PIEQ : area PITS = BC : Ca",
     "area IEF : area ILT = OQ : OS (la trascrizione ha OC)",
     "area PINM : area PIEQ = CZ : BC; area PIGR : area PIEQ = CD : BC",
     "verifica numerica: nota N7"
    ]
   },
   "passi": [
    {
     "id": "L2-P29-p1",
     "la": "",
     "it": "Sia Ba l’arco descritto in un’oscillazione intera, C il punto più basso della cicloide e CZ la metà dell’arco dell’intera cicloide, uguale alla lunghezza del pendolo; e si cerchi la resistenza del corpo in un luogo qualsiasi D.",
     "en": "Let Ba be an arc described in one entire oscillation, C the lowest point of the cycloid, and CZ half the whole cycloidal arc, equal to the length of the pendulum; and let it be required to find the resistance of the body in any place D.",
     "dipende_da": [],
     "figura": {
      "mostra": [
       "arco Ba",
       "C",
       "CZ (= lunghezza del pendolo)",
       "luogo D"
      ]
     }
    },
    {
     "id": "L2-P29-p2",
     "la": "",
     "it": "Si tagli la retta infinita OQ nei punti O, S, P, Q con questa legge: se si innalzano le perpendicolari OK, ST, PI, QE, e con centro O e asintoti OK, OQ si descrive l’iperbole TIGE, che tagli le perpendicolari ST, PI, QE in T, I ed E, e per il punto I si conduce KF parallela all’asintoto OQ, che incontri l’asintoto OK in K e le perpendicolari ST e QE in L e F, l’area iperbolica PIEQ stia all’area iperbolica PITS come l’arco BC descritto nella discesa del corpo sta all’arco Ca descritto nella salita, e l’area IEF stia all’area ILT come OQ sta a OS.",
     "en": "Cut the indefinite right line OQ in the points O, S, P, Q, so that (erecting the perpendiculars OK, ST, PI, QE, and with the centre O, and the asymptotes OK, OQ, describing the hyperbola TIGE cutting the perpendiculars ST, PI, QE in T, I, and E, and through the point I drawing KF, parallel to the asymptote OQ, meeting the asymptote OK in K, and the perpendiculars ST and QE in L and F) the hyperbolic area PIEQ may be to the hyperbolic area PITS as the arc BC, described in the descent of the body, to the arc Ca described in the ascent; and that the area IEF may be to the area ILT as OQ to OS.",
     "dipende_da": [],
     "figura": {
      "mostra": [
       "retta OQ con O, S, P, Q",
       "perpendicolari OK, ST, PI, QE",
       "iperbole TIGE",
       "retta KF; punti K, L, F"
      ],
      "evidenzia": [
       "PIEQ : PITS = BC : Ca",
       "IEF : ILT = OQ : OS"
      ]
     },
     "nota": "La trascrizione ha «ut OQ ad OC»: C non è un punto della retta OQ; Motte ha OS, e la verifica numerica (N7) richiede OS. Refuso probabile, tradotto secondo il senso."
    },
    {
     "id": "L2-P29-p3",
     "la": "",
     "it": "Poi con la perpendicolare MN si stacchi l’area iperbolica PINM, che stia all’area iperbolica PIEQ come l’arco CZ sta all’arco BC descritto nella discesa.",
     "en": "Then with the perpendicular MN cut off the hyperbolic area PINM, and let that area be to the hyperbolic area PIEQ as the arc CZ to the arc BC described in the descent.",
     "dipende_da": [],
     "figura": {
      "mostra": [
       "perpendicolare MN",
       "area PINM"
      ],
      "evidenzia": [
       "PINM : PIEQ = CZ : BC"
      ]
     }
    },
    {
     "id": "L2-P29-p4",
     "la": "",
     "it": "E se con la perpendicolare RG si stacca l’area iperbolica PIGR, che stia all’area PIEQ come un arco qualsiasi CD sta all’arco BC descritto nell’intera discesa, la resistenza nel luogo D starà alla forza di gravità come l’area (OR/OQ) × IEF − IGH sta all’area PINM.",
     "en": "And if the perpendicular RG cut off the hyperbolic area PIGR, which shall be to the area PIEQ as any arc CD to the arc BC described in the whole descent, the resistance in any place D will be to the force of gravity as the area [SVG 618] to the area PINM.",
     "dipende_da": [],
     "figura": {
      "mostra": [
       "perpendicolare RG (H su KF)",
       "area PIGR",
       "area IGH"
      ],
      "evidenzia": [
       "resistenza : gravità = [(OR/OQ) × IEF − IGH] : PINM"
      ]
     },
     "nota": "«OROQIEF−IGH» è la frazione appiattita (OR/OQ)·IEF − IGH. Motte: SVG 618 (da controllare)."
    },
    {
     "id": "L2-P29-p5",
     "la": "",
     "it": "Poiché infatti le forze nate dalla gravità da cui il corpo è sollecitato nei luoghi Z, B, D, a sono come gli archi CZ, CB, CD, Ca, e quegli archi sono come le aree PINM, PIEQ, PIGR, PITS, si rappresentino rispettivamente con queste aree sia gli archi sia le forze.",
     "en": "For since the forces arising from gravity with which the body is urged in the places Z, B, D, a, are as the arcs CZ, CB, CD, Ca and those arcs are as the areas PINM, PIEQ, PIGR, PITS; let those areas be the exponents both of the arcs and of the forces respectively.",
     "dipende_da": [],
     "figura": {
      "mostra": [
       "corrispondenza archi–aree"
      ],
      "evidenzia": [
       "CZ, CB, CD, Ca ↔ PINM, PIEQ, PIGR, PITS"
      ]
     }
    },
    {
     "id": "L2-P29-p6",
     "la": "",
     "it": "Sia inoltre Dd uno spazio piccolissimo descritto dal corpo che scende, e lo si rappresenti con l’area piccolissima RGgr compresa fra le parallele RG, rg; e si prolunghi rg fino a h, in modo che GHhg e RGgr siano i decrementi contemporanei delle aree IGH, PIGR.",
     "en": "Let Dd be a very small space described by the body in its descent: and let it be expressed by the very small area RGgr comprehended between the parallels RG, rg; and produce rg to h, so that GHhg and RGgr may be the contemporaneous decrements of the areas IGH, PIGR.",
     "dipende_da": [],
     "figura": {
      "mostra": [
       "spazio Dd",
       "striscia RGgr",
       "punti r, g, h",
       "striscia GHhg"
      ],
      "evidenzia": [
       "decrementi contemporanei di IGH e PIGR"
      ]
     }
    },
    {
     "id": "L2-P29-p7",
     "la": "",
     "it": "E l’incremento dell’area (OR/OQ) × IEF − IGH, cioè GHhg − (Rr/OQ) × IEF, ossia Rr × HG − (Rr/OQ) × IEF, starà al decremento RGgr dell’area PIGR, ossia Rr × RG, come HG − IEF/OQ sta a RG; e perciò come OR × HG − (OR/OQ) × IEF sta a OR × GR, ossia a OP × PI, cioè (poiché sono uguali OR × HG, OR × HR − OR × GR, ORHK − OPIK, PIHR e PIGR + IGH) come PIGR + IGH − (OR/OQ) × IEF sta a OPIK.",
     "en": "And the increment [SVG 619], or [SVG 620], of the area [SVG 618] will be to the decrement RGgr, or Rr × RG, of the area PIGR, as [SVG 621] to RG; and therefore as [SVG 622] to OR × GR or OP × PI, that is (because of the equal quantities OR × HG, OR × HR - OR × GR, ORHK - OPIK, PIHR and PIGR + IGH), as [SVG 623] to OPIK.",
     "dipende_da": [],
     "figura": {
      "mostra": [
       "rettangolo ORHK",
       "rettangolo OPIK",
       "rettangolo PIHR"
      ],
      "evidenzia": [
       "OR × GR = OP × PI (proprietà dell’iperbole)",
       "incremento di Y : decremento di PIGR = PIGR + IGH − (OR/OQ)·IEF : OPIK"
      ]
     },
     "nota": "Frazioni appiattite: «RrOQIEF» = (Rr/OQ)·IEF; «IEFOQ» = IEF/OQ; «OROQIEF» = (OR/OQ)·IEF. Motte: SVG 619–623 (da controllare)."
    },
    {
     "id": "L2-P29-p8",
     "la": "",
     "it": "Se dunque l’area (OR/OQ) × IEF − IGH si chiama Y, e il decremento RGgr dell’area PIGR è dato, l’incremento dell’area Y sarà come PIGR − Y.",
     "en": "Therefore if the area [SVG 618] be called Y, and RGgr the decrement of the area PIGR be given, the increment of the area Y will be as PIGR - Y.",
     "dipende_da": [],
     "figura": {
      "mostra": [
       "area Y"
      ],
      "evidenzia": [
       "incremento di Y ∝ PIGR − Y"
      ]
     },
     "nota": "Si usa PIGR + IGH − (OR/OQ)·IEF = PIGR − Y; OPIK è costante."
    },
    {
     "id": "L2-P29-p9",
     "la": "",
     "it": "Se poi V indica la forza nata dalla gravità, proporzionale all’arco da descrivere CD, da cui il corpo è sollecitato in D, e R si pone per la resistenza, V − R sarà la forza totale da cui il corpo è sollecitato in D.",
     "en": "Then if V represent the force arising from the gravity, proportional to the arc CD to be described, by which the body is acted upon in D, and R be put for the resistance, V - R will be the whole force with which the body is urged in D.",
     "dipende_da": [],
     "figura": {
      "mostra": [
       "forza V",
       "resistenza R"
      ],
      "evidenzia": [
       "forza totale V − R"
      ]
     }
    },
    {
     "id": "L2-P29-p10",
     "la": "",
     "it": "L’incremento della velocità è quindi come V − R e la particella di tempo in cui è avvenuto, considerate congiuntamente; ma anche la velocità stessa è come l’incremento contemporaneo dello spazio descritto, direttamente, e la stessa particella di tempo, inversamente.",
     "en": "Therefore the increment of the velocity is as V - R and the particle of time in which it is generated conjunctly. But the velocity itself is as the contemporaneous increment of the space described directly and the same particle of time inversely.",
     "dipende_da": [],
     "figura": {
      "mostra": [],
      "evidenzia": [
       "dv ∝ (V − R)·dt; v ∝ ds/dt"
      ]
     }
    },
    {
     "id": "L2-P29-p11",
     "la": "",
     "it": "Perciò, poiché per ipotesi la resistenza è come il quadrato della velocità, l’incremento della resistenza (per il Lemma II) sarà come la velocità e l’incremento della velocità considerati congiuntamente, cioè come il momento dello spazio e V − R considerati congiuntamente; e quindi, se il momento dello spazio è dato, come V − R; cioè, se al posto della forza V si scrive il suo esponente PIGR e la resistenza R si rappresenta con un’altra area Z, come PIGR − Z.",
     "en": "Therefore, since the resistance is, by the supposition, as the square of the velocity, the increment of the resistance will (by Lem. II) be as the velocity and the increment of the velocity conjunctly, that is, as the moment of the space and V - R conjunctly; and, therefore, if the moment of the space be given, as V - R; that is, if for the force V we put its exponent PIGR, and the resistance R be expressed by any other area Z, as PIGR - Z.",
     "dipende_da": [
      "Libro II, Lemma II"
     ],
     "figura": {
      "mostra": [
       "area Z (resistenza)"
      ],
      "evidenzia": [
       "incremento di Z ∝ PIGR − Z"
      ]
     },
     "nota": "Il Lemma II del Libro II (momento della quantità generata) dà: il momento di v² è come 2v·(momento di v)."
    },
    {
     "id": "L2-P29-p12",
     "la": "",
     "it": "Mentre dunque l’area PIGR decresce uniformemente per la sottrazione di momenti dati, l’area Y cresce in rapporto a PIGR − Y e l’area Z in rapporto a PIGR − Z.",
     "en": "Therefore the area PIGR uniformly decreasing by the subduction of given moments, the area Y increases in proportion of PIGR - Y, and the area Z in proportion of PIGR - Z.",
     "dipende_da": [],
     "figura": {
      "mostra": [],
      "evidenzia": [
       "Y e Z obbediscono alla stessa legge di accrescimento"
      ]
     },
     "nota": "«crescunt area Y»: verbo plurale con soggetto singolare (accordo con i due soggetti Y e Z)."
    },
    {
     "id": "L2-P29-p13",
     "la": "",
     "it": "E perciò, se le aree Y e Z cominciano insieme e all’inizio sono uguali, per l’aggiunta di momenti uguali continueranno a essere uguali e, decrescendo poi anch’esse per momenti uguali, svaniranno insieme.",
     "en": "And therefore if the areas Y and Z begin together, and at the beginning are equal, these, by the addition of equal moments, will continue to be equal; and in like manner decreasing by equal moments, will vanish together.",
     "dipende_da": [],
     "figura": {
      "mostra": [],
      "evidenzia": [
       "Y = Z se partono insieme e uguali"
      ]
     }
    },
    {
     "id": "L2-P29-p14",
     "la": "",
     "it": "E viceversa, se cominciano insieme e svaniscono insieme, avranno momenti uguali e saranno sempre uguali: e ciò perché, se la resistenza Z aumenta, la velocità diminuirà insieme con l’arco Ca descritto nella salita del corpo; e, avvicinandosi al punto C il punto in cui cessa tutto il moto insieme con la resistenza, la resistenza svanirà prima dell’area Y.",
     "en": "And, vice versa, if they together begin and vanish, they will have equal moments and be always equal; and that, because if the resistance Z be augmented, the velocity together with the arc Ca, described in the ascent of the body, will be diminished; and the point in which all the motion together with the resistance ceases coming nearer to the point C, the resistance vanishes sooner than the area Y.",
     "dipende_da": [],
     "figura": {
      "mostra": [
       "arco di salita Ca"
      ]
     }
    },
    {
     "id": "L2-P29-p15",
     "la": "",
     "it": "E il contrario avverrà quando la resistenza diminuisce.",
     "en": "And the contrary will happen when the resistance is diminished.",
     "dipende_da": [],
     "figura": {
      "mostra": []
     }
    },
    {
     "id": "L2-P29-p16",
     "la": "",
     "it": "Ora, l’area Z comincia e finisce dove la resistenza è nulla, cioè all’inizio del moto, dove l’arco CD è uguale all’arco CB e la retta RG cade sulla retta QE, e alla fine del moto, dove l’arco CD è uguale all’arco Ca e RG cade sulla retta ST.",
     "en": "Now the area Z begins and ends where the resistance is nothing, that is, at the beginning of the motion where the arc CD is equal to the arc CB, and the right line RG falls upon the right line QE; and at the end of the motion where the arc CD is equal to the arc Ca, and RG falls upon the right line ST.",
     "dipende_da": [],
     "figura": {
      "mostra": [
       "RG su QE (inizio)",
       "RG su ST (fine)"
      ],
      "evidenzia": [
       "Z = 0 agli estremi"
      ]
     }
    },
    {
     "id": "L2-P29-p17",
     "la": "",
     "it": "E l’area Y, ossia (OR/OQ) × IEF − IGH, comincia e finisce dove è nulla, e quindi dove (OR/OQ) × IEF e IGH sono uguali: cioè (per la costruzione) dove la retta RG cade successivamente sulle rette QE e ST.",
     "en": "And the area Y or [SVG 618] begins and ends also where the resistance is nothing, and therefore where [SVG 624] and IGH are equal; that is (by the construction), where the right line RG falls successively upon the right lines QE and ST.",
     "dipende_da": [],
     "figura": {
      "mostra": [],
      "evidenzia": [
       "Y = 0 per RG su QE (IGH = IEF) e su ST (per IEF : ILT = OQ : OS)"
      ]
     },
     "nota": "Motte aggiunge «also where the resistance is nothing»: il latino dice soltanto «dove è nulla» (riferito all’area Y)."
    },
    {
     "id": "L2-P29-p18",
     "la": "",
     "it": "Perciò quelle aree cominciano insieme e svaniscono insieme, e quindi sono sempre uguali.",
     "en": "Therefore those areas begin and vanish together, and are therefore always equal.",
     "dipende_da": [],
     "figura": {
      "mostra": [],
      "evidenzia": [
       "Y = Z"
      ]
     }
    },
    {
     "id": "L2-P29-p19",
     "la": "",
     "it": "Dunque l’area (OR/OQ) × IEF − IGH è uguale all’area Z, con cui si rappresenta la resistenza, e perciò sta all’area PINM, con cui si rappresenta la gravità, come la resistenza sta alla gravità. C.V.D.",
     "en": "Therefore the area [SVG 618] is equal to the area Z, by which the resistance is expressed, and therefore is to the area PINM, by which the gravity is expressed, as the resistance to the gravity. Q.E.D.",
     "dipende_da": [],
     "figura": {
      "mostra": [],
      "evidenzia": [
       "resistenza : gravità = Y : PINM"
      ]
     }
    }
   ]
  },
  {
   "id": "L2-P30",
   "tipo": "Propositio/Theorema",
   "titolo": "Prop. XXX — l’area delle resistenze e la differenza degli archi",
   "copertura": [
    "II.S6.31",
    "II.S6.32"
   ],
   "fonti": {
    "la": "",
    "en": "Motte 1846, sezione corrispondente (Prop. XXX)"
   },
   "enunciato": {
    "la": "",
    "it": "Se la retta aB è uguale all’arco di cicloide che il corpo descrive oscillando, e nei suoi singoli punti D si innalzano le perpendicolari DK, che stiano alla lunghezza del pendolo come la resistenza del corpo nei punti corrispondenti dell’arco sta alla forza di gravità, dico che la differenza fra l’arco descritto nell’intera discesa e l’arco descritto nell’intera salita successiva, moltiplicata per la semisomma degli stessi archi, sarà uguale all’area BKa occupata da tutte le perpendicolari DK.",
    "en": "If a right line aB be equal to the arc of a cycloid which an oscillating body describes, and at each of its points D the perpendiculars DK be erected, which shall be to the length of the pendulum as the resistance of the body in the corresponding points of the arc to the force of gravity; I say, that the difference between the arc described in the whole descent and the arc described in the whole subsequent ascent drawn into half the sum of the same arcs will be equal to the area BKa which all those perpendiculars take up."
   },
   "figura_base": {
    "punti": [
     "a",
     "A",
     "B",
     "C",
     "D",
     "d",
     "K",
     "E",
     "e",
     "F",
     "f",
     "M",
     "N",
     "g",
     "h",
     "m",
     "V",
     "T"
    ],
    "vincoli": [
     "aB retta uguale all’arco descritto nel mezzo resistente; AB arco che si descriverebbe nel vuoto; C punto medio di AB",
     "CD rappresenta la forza tangenziale in D; la lunghezza del pendolo rappresenta la gravità",
     "DK su DE, perpendicolare ad aB, rappresenta la resistenza in D",
     "semicerchio BEeA di centro C e raggio CB: DE, de velocità nel vuoto",
     "DF velocità nel mezzo resistente; cerchio FfM di centro C e raggio CF; CN = Cg",
     "Fm ⊥ df; triangoli simili Fmf, Fhg, FDC"
    ]
   },
   "passi": [
    {
     "id": "L2-P30-p1",
     "la": "",
     "it": "Si rappresenti infatti l’arco di cicloide descritto in un’oscillazione intera con quella retta aB a esso uguale, e l’arco che sarebbe descritto nel vuoto con la lunghezza AB.",
     "en": "Let the arc of the cycloid, described in one entire oscillation, be expressed by the right line aB, equal to it, and the arc which would have been described in vacuo by the length AB.",
     "dipende_da": [],
     "figura": {
      "mostra": [
       "retta aB",
       "lunghezza AB"
      ]
     }
    },
    {
     "id": "L2-P30-p2",
     "la": "",
     "it": "Si divida AB a metà in C: il punto C rappresenterà il punto più basso della cicloide, e CD sarà come la forza nata dalla gravità da cui il corpo in D è sollecitato lungo la tangente della cicloide, e avrà con la lunghezza del pendolo il rapporto che la forza in D ha con la forza di gravità.",
     "en": "Bisect AB in C, and the point C will represent the lowest point of the cycloid, and CD will be as the force arising from gravity, with which the body in D is urged in the direction of the tangent of the cycloid, and will have the same ratio to the length of the pendulum as the force in D has to the force of gravity.",
     "dipende_da": [],
     "figura": {
      "mostra": [
       "C punto medio di AB",
       "punto D",
       "segmento CD"
      ],
      "evidenzia": [
       "CD : lunghezza del pendolo = forza in D : gravità"
      ]
     }
    },
    {
     "id": "L2-P30-p3",
     "la": "",
     "it": "Si rappresenti dunque quella forza con la lunghezza CD e la forza di gravità con la lunghezza del pendolo; e se su DE si prende DK nel rapporto con la lunghezza del pendolo che la resistenza ha con la gravità, DK sarà l’esponente della resistenza.",
     "en": "Let that force, therefore, be expressed by that length CD, and the force of gravity by the length of the pendulum; and if in DE you take DK in the same ratio to the length of the pendulum as the resistance has to the gravity, DK will be the exponent of the resistance.",
     "dipende_da": [],
     "figura": {
      "mostra": [
       "perpendicolare DK"
      ],
      "evidenzia": [
       "DK rappresenta la resistenza"
      ]
     }
    },
    {
     "id": "L2-P30-p4",
     "la": "",
     "it": "Con centro C e raggio CA o CB si costruisca il semicerchio BEeA.",
     "en": "From the centre C with the interval CA or CB describe a semi-circle BEeA.",
     "dipende_da": [],
     "figura": {
      "mostra": [
       "semicerchio BEeA"
      ]
     }
    },
    {
     "id": "L2-P30-p5",
     "la": "",
     "it": "Il corpo descriva poi in un tempo piccolissimo lo spazio Dd; e, innalzate le perpendicolari DE, de, che incontrino la circonferenza in E ed e, queste saranno come le velocità che il corpo, scendendo nel vuoto dal punto B, acquisterebbe nei luoghi D e d.",
     "en": "Let the body describe, in the least time, the space Dd; and, erecting the perpendiculars DE, de, meeting the circumference in E and e, they will be as the velocities which the body descending in vacuo from the point B would acquire in the places D and d.",
     "dipende_da": [],
     "figura": {
      "mostra": [
       "spazio Dd",
       "perpendicolari DE, de",
       "punti E, e"
      ],
      "evidenzia": [
       "DE, de come velocità nel vuoto"
      ]
     }
    },
    {
     "id": "L2-P30-p6",
     "la": "",
     "it": "Ciò è chiaro (per la Prop. LII del Libro I).",
     "en": "This appears by Prop. LII, Book I.",
     "dipende_da": [
      "Libro I, Prop. LII"
     ],
     "figura": {
      "mostra": []
     },
     "nota": "Nella Prop. LII del Libro I la velocità in T sta a quella nel punto più basso come l’ordinata LI del semicerchio di raggio uguale all’arco sta al raggio: rimando verificato (apparato A.10)."
    },
    {
     "id": "L2-P30-p7",
     "la": "",
     "it": "Si rappresentino dunque queste velocità con quelle perpendicolari DE, de; e sia DF la velocità che il corpo acquista in D cadendo da B nel mezzo resistente.",
     "en": "Let therefore, these velocities be expressed by those perpendiculars DE, de; and let DF be the velocity which it acquires in D by falling from B in the resisting medium.",
     "dipende_da": [],
     "figura": {
      "mostra": [
       "DF (velocità nel mezzo resistente)"
      ]
     }
    },
    {
     "id": "L2-P30-p8",
     "la": "",
     "it": "E se con centro C e raggio CF si descrive il cerchio FfM, che incontri le rette de e AB in f e M, M sarà il luogo al quale il corpo salirebbe in seguito senza ulteriore resistenza, e df la velocità che acquisterebbe in d.",
     "en": "And if from the centre C with the interval CF we describe the circle FfM meeting the right lines de and AB in f and M, then M will be the place to which it would thenceforward, without farther resistance, ascend, and df the velocity it would acquire in d.",
     "dipende_da": [],
     "figura": {
      "mostra": [
       "cerchio FfM",
       "punti f, M"
      ],
      "evidenzia": [
       "M: punto di arresto senza ulteriore resistenza"
      ]
     }
    },
    {
     "id": "L2-P30-p9",
     "la": "",
     "it": "Di qui, anche, se Fg indica il momento della velocità che il corpo D, descrivendo lo spazio piccolissimo Dd, perde per la resistenza del mezzo, e si prende CN uguale a Cg, N sarà il luogo al quale il corpo salirebbe in seguito senza ulteriore resistenza, e MN sarà il decremento della salita nato dalla perdita di quella velocità.",
     "en": "Whence, also, if Fg represent the moment of the velocity which the body D, in describing the least space Dd, loses by the resistance of the medium; and CN be taken equal to Cg; then will N be the place to which the body, if it met no farther resistance, would thenceforward ascend, and MN will be the decrement of the ascent arising from the loss of that velocity.",
     "dipende_da": [],
     "figura": {
      "mostra": [
       "Fg (velocità perduta)",
       "N con CN = Cg",
       "MN"
      ],
      "evidenzia": [
       "MN decremento della salita"
      ]
     }
    },
    {
     "id": "L2-P30-p10",
     "la": "",
     "it": "Si abbassi su df la perpendicolare Fm: il decremento Fg della velocità DF, generato dalla resistenza DK, starà all’incremento fm della stessa velocità, generato dalla forza CD, come la forza generatrice DK sta alla forza generatrice CD.",
     "en": "Draw Fm perpendicular to df, and the decrement Fg of the velocity DF generated by the resistance DK will be to the increment fm of the same velocity, generated by the force CD, as the generating force DK to the generating force CD.",
     "dipende_da": [],
     "figura": {
      "mostra": [
       "Fm ⊥ df",
       "fm"
      ],
      "evidenzia": [
       "Fg : fm = DK : CD"
      ]
     }
    },
    {
     "id": "L2-P30-p11",
     "la": "",
     "it": "Ma, per i triangoli simili Fmf, Fhg, FDC, fm sta a Fm, ossia a Dd, come CD sta a DF; e, per uguaglianza, Fg sta a Dd come DK sta a DF.",
     "en": "But because of the similar triangles Fmf, Fhg, FDC, fm is to Fm or Dd as CD to DF; and, ex æquo, Fg to Dd as DK to DF.",
     "dipende_da": [],
     "figura": {
      "mostra": [
       "triangoli Fmf, Fhg, FDC",
       "punto h"
      ],
      "evidenzia": [
       "fm : Dd = CD : DF",
       "Fg : Dd = DK : DF"
      ]
     }
    },
    {
     "id": "L2-P30-p12",
     "la": "",
     "it": "Inoltre Fh sta a Fg come DF sta a CF; e, per uguaglianza perturbata, Fh, ossia MN, sta a Dd come DK sta a CF, ossia a CM; e perciò la somma di tutti i prodotti MN × CM sarà uguale alla somma di tutti i prodotti Dd × DK.",
     "en": "Also Fh is to Fg as DF to CF; and, ex æquo perturbatè, Fh or MN to Dd as DK to CF or CM; and therefore the sum of all the MN × CM will be equal to the sum of all the Dd × DK.",
     "dipende_da": [],
     "figura": {
      "mostra": [
       "Fh = MN"
      ],
      "evidenzia": [
       "MN × CM = Dd × DK"
      ]
     }
    },
    {
     "id": "L2-P30-p13",
     "la": "",
     "it": "Si immagini che nel punto mobile M si innalzi sempre un’ordinata perpendicolare uguale all’indeterminata CM, che con moto continuo sia moltiplicata per l’intera lunghezza Aa: il trapezio descritto da quel moto, ossia il rettangolo a esso uguale Aa × ½aB, sarà uguale alla somma di tutti i prodotti MN × CM, e quindi alla somma di tutti i prodotti Dd × DK, cioè all’area BKVTa. C.V.D.",
     "en": "At the moveable point M suppose always a rectangular ordinate erected equal to the indeterminate CM, which by a continual motion is drawn into the whole length Aa; and the trapezium described by that motion, or its equal, the rectangle [SVG 626], will be equal to the sum of all the MN × CM, and therefore to the sum of all the Dd × DK, that is, to the area BKVTa Q.E.D.",
     "dipende_da": [],
     "figura": {
      "mostra": [
       "trapezio su Aa",
       "area BKVTa"
      ],
      "evidenzia": [
       "Aa × ½aB = area BKVTa"
      ]
     },
     "nota": "«12aB» è ½aB appiattito. Il trapezio ha basi CB e Ca e altezza Aa = CB − Ca: area (CB² − Ca²)/2 = Aa × ½aB. Motte: SVG 626."
    }
   ]
  },
  {
   "id": "L2-P30-Cor",
   "tipo": "Corollarium",
   "titolo": "Prop. XXX, Cor. — resistenza uniforme, lineare, quadratica",
   "copertura": [
    "II.S6.33",
    "II.S6.34",
    "II.S6.35",
    "II.S6.36",
    "II.S6.37"
   ],
   "fonti": {
    "la": "",
    "en": "Motte 1846, sezione corrispondente (Prop. XXX, Cor.)"
   },
   "enunciato": {
    "la": "",
    "it": "Di qui, dalla legge della resistenza e dalla differenza Aa degli archi Ca, CB, si può ricavare con ottima approssimazione il rapporto della resistenza alla gravità.",
    "en": "Hence from the law of resistance, and the difference Aa of the arcs Ca, CB, may be collected the proportion of the resistance to the gravity nearly."
   },
   "figura_base": {
    "punti": [
     "B",
     "a",
     "O",
     "V",
     "K",
     "T",
     "R",
     "S",
     "A"
    ],
    "vincoli": [
     "figura della Prop. XXX",
     "O punto medio di Ba; OV esponente della resistenza in O",
     "BRVSa ellisse di centro O e semiassi OB, OV, oppure parabola di vertice V e asse OV"
    ]
   },
   "passi": [
    {
     "id": "L2-P30-Cor-p1",
     "la": "",
     "it": "Se infatti la resistenza DK è uniforme, la figura BKTa sarà un rettangolo contenuto sotto Ba e DK; e quindi il rettangolo contenuto sotto ½Ba e Aa sarà uguale al rettangolo contenuto sotto Ba e DK, e DK sarà uguale a ½Aa.",
     "en": "For if the resistance DK be uniform, the figure BKTa will be a rectangle under Ba and DK; and thence the rectangle under [SVG 627] and Aa will be equal to the rectangle under Ba and DK, and DK will be equal to [SVG 628].",
     "dipende_da": [],
     "figura": {
      "mostra": [
       "rettangolo BKTa"
      ],
      "evidenzia": [
       "DK = ½Aa"
      ]
     }
    },
    {
     "id": "L2-P30-Cor-p2",
     "la": "",
     "it": "Perciò, poiché DK è l’esponente della resistenza e la lunghezza del pendolo è l’esponente della gravità, la resistenza starà alla gravità come ½Aa sta alla lunghezza del pendolo, esattamente come si è dimostrato nella Prop. XXVIII.",
     "en": "Wherefore since DK is the exponent of the resistance, and the length of the pendulum the exponent of the gravity, the resistance will be to the gravity as [SVG 628] to the length of the pendulum; altogether as in Prop. XXVIII is demonstrated.",
     "dipende_da": [
      "Prop. XXVIII"
     ],
     "figura": {
      "mostra": [],
      "evidenzia": [
       "resistenza : gravità = ½Aa : lunghezza del pendolo"
      ]
     }
    },
    {
     "id": "L2-P30-Cor-p3",
     "la": "",
     "it": "Se la resistenza è come la velocità, la figura BKTa sarà con ottima approssimazione un’ellisse.",
     "en": "If the resistance be as the velocity, the figure BKTa will be nearly an ellipsis.",
     "dipende_da": [],
     "figura": {
      "mostra": [
       "figura BKTa (resistenza lineare)"
      ]
     }
    },
    {
     "id": "L2-P30-Cor-p4",
     "la": "",
     "it": "Infatti, se il corpo in un mezzo non resistente descrivesse in un’oscillazione intera la lunghezza BA, la velocità in un luogo qualsiasi D sarebbe come l’ordinata DE del cerchio descritto sul diametro AB.",
     "en": "For if a body, in a non-resisting medium, by one entire oscillation, should describe the length BA, the velocity in any place D would be as the ordinate DE of the circle described on the diameter AB.",
     "dipende_da": [],
     "figura": {
      "mostra": [
       "cerchio sul diametro AB",
       "ordinata DE"
      ]
     }
    },
    {
     "id": "L2-P30-Cor-p5",
     "la": "",
     "it": "Perciò, poiché Ba nel mezzo resistente e BA nel mezzo non resistente sono descritte in tempi circa uguali, e quindi le velocità nei singoli punti di Ba stanno con ottima approssimazione alle velocità nei punti corrispondenti della lunghezza BA come Ba sta a BA, la velocità nel punto D nel mezzo resistente sarà come l’ordinata del cerchio o dell’ellisse descritti sul diametro Ba; e perciò la figura BKVTa sarà con ottima approssimazione un’ellisse.",
     "en": "Therefore since Ba in the resisting medium, and BA in the non-resisting one, are described nearly in the same times; and therefore the velocities in each of the points of Ba are to the velocities in the correspondent points of the length BA nearly as Ba is to BA, the velocity in the point D in the resisting medium will be as the ordinate of the circle or ellipsis described upon the diameter Ba; and therefore the figure BKVTa will be nearly an ellipsis.",
     "dipende_da": [],
     "figura": {
      "mostra": [
       "ellisse sul diametro Ba"
      ]
     }
    },
    {
     "id": "L2-P30-Cor-p6",
     "la": "",
     "it": "Poiché si suppone la resistenza proporzionale alla velocità, sia OV l’esponente della resistenza nel punto medio O; l’ellisse BRVSa, descritta con centro O e semiassi OB, OV, sarà con ottima approssimazione uguale alla figura BKVTa e al rettangolo Aa × BO, che le è uguale.",
     "en": "Since the resistance is supposed proportional to the velocity, let OV be the exponent of the resistance in the middle point O; and an ellipsis BRVSa described with the centre O, and the semi-axes OB, OV, will be nearly equal to the figure BKVTa, and to its equal the rectangle Aa × BO.",
     "dipende_da": [],
     "figura": {
      "mostra": [
       "O punto medio",
       "OV",
       "ellisse BRVSa"
      ],
      "evidenzia": [
       "semiellisse ≈ BKVTa = Aa × BO"
      ]
     }
    },
    {
     "id": "L2-P30-Cor-p7",
     "la": "",
     "it": "Dunque Aa × BO sta a OV × BO come l’area di questa ellisse sta a OV × BO: cioè Aa sta a OV come l’area del semicerchio sta al quadrato del raggio, ossia circa come 11 sta a 7; e perciò 7/11 Aa sta alla lunghezza del pendolo come la resistenza del corpo oscillante in O sta alla sua gravità.",
     "en": "Therefore Aa × BO is to OV × BO as the area of this ellipsis to OV × BO; that is, Aa is to OV as the area of the semi-circle to the square of the radius, or as 11 to 7 nearly; and, therefore, [SVG 629] is to the length of the pendulum as the resistance of the oscillating body in O to its gravity.",
     "dipende_da": [],
     "figura": {
      "mostra": [],
      "evidenzia": [
       "Aa : OV ≈ 11 : 7",
       "resistenza in O : gravità = 7/11 Aa : lunghezza del pendolo"
      ]
     },
     "nota": "«711Aa» = 7/11 Aa. «area ellipseos hujus» va intesa come l’area della semiellisse BRVSa (sopra Ba). 11 : 7 approssima π/2 (N8). Motte: SVG 629."
    },
    {
     "id": "L2-P30-Cor-p8",
     "la": "",
     "it": "Se poi la resistenza DK è in rapporto duplicato della velocità, la figura BKVTa sarà quasi una parabola con vertice V e asse OV, e perciò sarà con ottima approssimazione uguale al rettangolo contenuto sotto ⅔Ba e OV.",
     "en": "Now if the resistance DK be in the duplicate ratio of the velocity, the figure BKVTa will be almost a parabola having V for its vertex and OV for its axis, and therefore will be nearly equal to the rectangle under [SVG 630] and OV.",
     "dipende_da": [],
     "figura": {
      "mostra": [
       "parabola di vertice V e asse OV"
      ],
      "evidenzia": [
       "area ≈ ⅔Ba × OV"
      ]
     }
    },
    {
     "id": "L2-P30-Cor-p9",
     "la": "",
     "it": "Il rettangolo contenuto sotto ½Ba e Aa è dunque uguale al rettangolo contenuto sotto ⅔Ba e OV, e quindi OV è uguale a ¾Aa; e perciò la resistenza del corpo oscillante in O sta alla sua gravità come ¾Aa sta alla lunghezza del pendolo.",
     "en": "Therefore the rectangle under [SVG 627] and Aa is equal to the rectangle [SVG 631], and therefore OV is equal to [SVG 632]; and therefore the resistance in O made to the oscillating body is to its gravity as [SVG 632] to the length of the pendulum.",
     "dipende_da": [],
     "figura": {
      "mostra": [],
      "evidenzia": [
       "OV = ¾Aa"
      ]
     }
    },
    {
     "id": "L2-P30-Cor-p10",
     "la": "",
     "it": "E ritengo che queste conclusioni siano, nelle applicazioni pratiche, più che sufficientemente accurate.",
     "en": "And I take these conclusions to be accurate enough for practical uses.",
     "dipende_da": [],
     "figura": {
      "mostra": []
     }
    },
    {
     "id": "L2-P30-Cor-p11",
     "la": "",
     "it": "Infatti, poiché l’ellisse o la parabola BRVSa coincide con la figura BKVTa nel punto medio V, se da una delle due parti, BRV o VSa, supera quella figura, dall’altra parte ne resterà al di sotto, e così le sarà con ottima approssimazione uguale.",
     "en": "For since an ellipsis or parabola BRVSa falls in with the figure BKVTa in the middle point V, that figure, if greater towards the part BRV or VSa than the other, is less towards the contrary part, and is therefore nearly equal to it.",
     "dipende_da": [],
     "figura": {
      "mostra": [
       "parti BRV, VSa"
      ],
      "evidenzia": [
       "compensazione degli scarti"
      ]
     }
    }
   ]
  },
  {
   "id": "L2-P31",
   "tipo": "Propositio/Theorema",
   "titolo": "Prop. XXXI — la differenza degli archi è come la resistenza",
   "copertura": [
    "II.S6.38",
    "II.S6.39"
   ],
   "fonti": {
    "la": "",
    "en": "Motte 1846, sezione corrispondente (Prop. XXXI)"
   },
   "enunciato": {
    "la": "",
    "it": "Se la resistenza di un corpo oscillante, nelle singole parti proporzionali degli archi descritti, aumenta o diminuisce in un rapporto dato, la differenza fra l’arco descritto nella discesa e l’arco descritto nella salita successiva aumenterà o diminuirà nello stesso rapporto.",
    "en": "If the resistance made to an oscillating body in each of the proportional parts of the arcs described be augmented or diminished in a given ratio, the difference between the arc described in the descent and the arc described in the subsequent ascent will be augmented or diminished in the same ratio."
   },
   "figura_base": {
    "punti": [
     "a",
     "A",
     "B",
     "C",
     "D",
     "K",
     "T"
    ],
    "vincoli": [
     "figura della Prop. XXX",
     "area BKTa = Aa × ½aB",
     "ordinate DK moltiplicate per un fattore dato"
    ]
   },
   "passi": [
    {
     "id": "L2-P31-p1",
     "la": "",
     "it": "Quella differenza nasce infatti dal ritardo del pendolo dovuto alla resistenza del mezzo, e perciò è come il ritardo totale e come la resistenza ritardatrice, che gli è proporzionale.",
     "en": "For that difference arises from the retardation of the pendulum by the resistance of the medium, and therefore is as the whole retardation and the retarding resistance proportional thereto.",
     "dipende_da": [],
     "figura": {
      "mostra": [
       "differenza Aa"
      ]
     }
    },
    {
     "id": "L2-P31-p2",
     "la": "",
     "it": "Nella proposizione precedente il rettangolo contenuto sotto la retta ½aB e la differenza Aa di quegli archi CB, Ca era uguale all’area BKTa.",
     "en": "In the foregoing Proposition the rectangle under the right line [SVG 633] and the difference Aa of the arcs CB, Ca, was equal to the area BKTa.",
     "dipende_da": [
      "Prop. XXX"
     ],
     "figura": {
      "mostra": [
       "area BKTa",
       "rettangolo Aa × ½aB"
      ],
      "evidenzia": [
       "Aa × ½aB = BKTa"
      ]
     }
    },
    {
     "id": "L2-P31-p3",
     "la": "",
     "it": "E quell’area, se la lunghezza aB resta la stessa, aumenta o diminuisce nel rapporto delle ordinate DK, cioè nel rapporto della resistenza, e quindi è come la lunghezza aB e la resistenza considerate congiuntamente.",
     "en": "And that area, if the length aB remains, is augmented or diminished in the ratio of the ordinates DK; that is, in the ratio of the resistance and is therefore as the length aB and the resistance conjunctly.",
     "dipende_da": [],
     "figura": {
      "mostra": [
       "ordinate DK scalate"
      ],
      "evidenzia": [
       "area ∝ aB × resistenza"
      ]
     }
    },
    {
     "id": "L2-P31-p4",
     "la": "",
     "it": "Perciò il rettangolo contenuto sotto Aa e ½aB è come aB e la resistenza considerate congiuntamente, e quindi Aa è come la resistenza. C.V.D.",
     "en": "And therefore the rectangle under Aa and [SVG 633] is as aB and the resistance conjunctly, and therefore Aa is as the resistance. Q.E.D.",
     "dipende_da": [],
     "figura": {
      "mostra": [],
      "evidenzia": [
       "Aa ∝ resistenza"
      ]
     }
    }
   ]
  }
 ]
}
```
