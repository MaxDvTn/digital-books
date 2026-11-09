> **Copia pubblica.** In questa versione i campi `"la"` della Parte B sono vuoti: le frasi latine vengono dalla trascrizione del Newton Project, che non si ridistribuisce. Il latino del 1726 si legge su newtonproject.ox.ac.uk.

# Isaac Newton
# Principi matematici della filosofia naturale

## Fascicolo 3 — Assiomi, ovvero leggi del moto

**Nuova traduzione italiana di lavoro dal latino del 1726, confrontata con l’inglese di Andrew Motte nell’edizione del 1846.**

Versione 0.3 — 8 novembre 2026. Preparata con Claude (Anthropic) per Massimo Bosetti.

*Novità della 0.2:* annotazioni F1–F3 verificate sul latino del 1726 (Newton Project NATP00087).
*Novità della 0.3:* varianti di trascrizione controllate sulla stampa del 1726 (scansione ECCO) e sulle figure originali; refuso PE² attribuito all’edizione 1846 dopo il confronto con Motte 1729; decisioni del curatore su *constanter* e *impulsu*; glossario uniformato con il Fascicolo 1.

### Stato e perimetro

Questo fascicolo prosegue i Fascicoli 1 (*Definizioni*) e 2 (*Scolio alle definizioni*). Traduce integralmente la sezione **Axiomata, sive leges motus**: le Leggi I–III con i loro commenti, i Corollari I–VI e lo Scolio che li segue, fino all’inizio del Libro I (*De motu corporum*). È una traduzione di lavoro, non un’edizione critica validata.

Gli identificatori **L01–L36** e i titoli tematici tra parentesi sono aggiunte editoriali. Servono a orientare la lettura e a controllare la completezza. I numeri romani delle leggi e dei corollari appartengono al testo originale. Eventuali integrazioni del curatore sono segnalate tra parentesi quadre. Le note poste dopo la traduzione non fanno parte del testo di Newton.

In coda al fascicolo:

- un elenco di **annotazioni fuori perimetro** su tre passi del Libro I, che non vengono tradotti;
- la **Parte B**, con i dati strutturati per le pagine interattive dei Corollari I e II, gli unici corollari della sezione che hanno figura e dimostrazione geometrica.

### Fonti effettivamente consultate

1. **Latino di riferimento.** Isaac Newton, *Philosophiæ Naturalis Principia Mathematica*, terza edizione, Londra, 1726, *Axiomata, sive leges motus*, pp. 13–27. Trascrizione normalizzata del Newton Project, documento **NATP00086**: <https://www.newtonproject.ox.ac.uk/view/texts/normalized/NATP00086>. Ho lavorato su una copia della pagina salvata dal curatore l’8 novembre 2026 (file .mht), estratta in testo semplice senza correzioni. La copia è conservata nel progetto come `fonti/latino-1726-NATP00086-Axiomata.md`.
2. **Inglese di confronto.** *Newton’s Principia. The Mathematical Principles of Natural Philosophy*, traduzione di Andrew Motte, New York, Daniel Adee, 1846, *Axioms, or Laws of Motion*, pp. 83–94 secondo i marcatori di pagina dell’EPUB. Edizione digitale Project Gutenberg n. 76404 (<https://www.gutenberg.org/ebooks/76404>), nel file EPUB allegato dal curatore. L’estratto della sezione e dei passi del Libro I citati in fondo è conservato nel progetto come `fonti/motte-1846-Assiomi-e-passi-Libro-I.md`.
3. **Fascicoli 1 e 2** del progetto, per il formato, i criteri e il glossario.
4. **Controlli sulla stampa** (v0.3): scansione ECCO dell’esemplare 1726 su Internet Archive (`bim_eighteenth-century_philosophiae-naturalis-p_newton-sir-isaac_1726`), consultata per ricerca nel testo OCR; figure NATP00086-1…9 del Newton Project, viste direttamente; Motte 1729, vol. I, Londra, B. Motte (Internet Archive `bub_gb_Tm0FAAAAQAAJ`), p. 80, vista sull’immagine della pagina; ristampa Glasgow 1871 dell’edizione 1726 (Internet Archive `sirisaacnewtons01newtgoog`), per confronto.

Il testo latino è quello della trascrizione. Nella v0.3 i punti dubbi sono stati controllati sulla stampa del 1726 (fonte 4) e sulle figure originali NATP00086-1…9. Non ho consultato né riprodotto traduzioni italiane moderne.

### Criteri di traduzione

- Il testo guida è il latino. L’inglese serve a controllare le interpretazioni ed è annotato quando aggiunge, omette o si discosta.
- Si usa un italiano contemporaneo, ma si conservano la struttura argomentativa e il lessico storico. Nel testo tradotto non compaiono formule moderne: le corrispondenze moderne stanno nelle note.
- Il glossario fisso dei Fascicoli 1–2 è rispettato:
  - *vis insita*: «forza insita»; *vis impressa*: «forza impressa»; *vis motrix*: «forza motrice»; *vis acceleratrix*: «forza acceleratrice»;
  - *quantitas motus*, e *motus* quando indica la grandezza: «quantità di moto»; *mutatio motus*: «cambiamento della quantità di moto»;
  - *impetus*: «impeto»; *impulsus*: «spinta», oppure «impulso» motivando; *ictus*: «urto»;
  - *ratio ultima*: «rapporto ultimo»; *in directum*: «in linea retta»; *conjunctim*: «considerate congiuntamente».
- Le estensioni del glossario sono elencate e motivate nell’apparato (§ A.0).
- Le enunciazioni delle leggi e dei corollari sono in latino all’infinito, con accusativo e infinito retti da un «si stabilisce», «si afferma» sottinteso. In italiano sono rese con l’indicativo, come nei titoli dei teoremi.
- Le maiuscole e la punteggiatura sono adattate all’uso italiano. I nomi propri latinizzati sono resi nella forma moderna, con la forma latina nell’apparato.

---

## Traduzione italiana

### Assiomi, ovvero leggi del moto

### Legge I (perseveranza dello stato)

**[L01]** **Ogni corpo persevera nel proprio stato di quiete o di moto uniforme in linea retta, se non in quanto è costretto a mutare quello stato da forze impresse.**

**[L02]** I proiettili perseverano nei loro moti, se non in quanto sono ritardati dalla resistenza dell’aria e spinti verso il basso dalla forza di gravità. Una trottola, le cui parti, per la loro coesione, si distolgono continuamente dai moti rettilinei, non cessa di ruotare, se non in quanto è ritardata dall’aria. I corpi più grandi dei pianeti e delle comete, poi, conservano più a lungo i loro moti, sia progressivi sia circolari, compiuti in spazi che oppongono minore resistenza.

### Legge II (cambiamento della quantità di moto)

**[L03]** **Il cambiamento della quantità di moto è proporzionale alla forza motrice impressa e avviene lungo la linea retta secondo la quale quella forza è impressa.**

**[L04]** Se una forza genera una certa quantità di moto, una forza doppia ne genererà il doppio, una tripla il triplo, sia che venga impressa tutta insieme e in una volta, sia gradualmente e in momenti successivi. E questa quantità di moto, poiché è sempre diretta verso la stessa parte della forza che la genera, se il corpo si muoveva già prima, si aggiunge alla sua quantità di moto quando le è concorde, se ne sottrae quando le è contraria, oppure, quando le è obliqua, le si aggiunge obliquamente e si compone con essa secondo la direzione di entrambe.

### Legge III (azione e reazione)

**[L05]** **All’azione è sempre contraria e uguale la reazione: ossia le azioni di due corpi l’uno sull’altro sono sempre uguali e dirette verso parti contrarie.**

**[L06]** Qualunque cosa prema o tiri un’altra è premuta o tirata da essa in egual misura. Se qualcuno preme una pietra con un dito, anche il suo dito è premuto dalla pietra. Se un cavallo tira una pietra legata a una fune, anche il cavallo, per così dire, sarà tirato indietro in egual misura verso la pietra: la fune, infatti, tesa da entrambe le parti, con la medesima tendenza ad allentarsi spingerà il cavallo verso la pietra e la pietra verso il cavallo, e ostacolerà l’avanzare dell’uno tanto quanto favorisce l’avanzare dell’altra.

**[L07]** Se un corpo, urtando contro un altro, ne ha mutato in qualsiasi modo la quantità di moto con la propria forza, anch’esso, a sua volta, subirà nella propria quantità di moto, per la forza dell’altro, lo stesso cambiamento verso la parte contraria, a causa dell’uguaglianza della pressione reciproca. Per effetto di queste azioni diventano uguali i cambiamenti non delle velocità, ma delle quantità di moto: s’intende, nei corpi che non siano impediti da altre cause. Infatti i cambiamenti delle velocità, anch’essi fatti verso parti contrarie, sono inversamente proporzionali ai corpi, poiché le quantità di moto cambiano in egual misura. Questa legge vale anche nelle attrazioni, come sarà provato nello scolio che segue.

### Corollario I (parallelogramma delle forze)

**[L08]** **Un corpo, per effetto di forze congiunte, descrive la diagonale di un parallelogramma nello stesso tempo in cui, per effetto delle forze separate, ne descriverebbe i lati.**

**[L09]** Supponiamo che un corpo, in un tempo dato, per effetto della sola forza M impressa nel luogo A, sia portato con moto uniforme da A a B; e che, per effetto della sola forza N impressa nel medesimo luogo, sia portato da A a C. Si completi il parallelogramma ABDC: per effetto di entrambe le forze, quel corpo sarà portato nello stesso tempo lungo la diagonale, da A a D. Poiché infatti la forza N agisce lungo la linea AC, parallela a BD, per la Legge II questa forza non muterà affatto la velocità di avvicinamento a quella linea BD generata dall’altra forza. Il corpo giungerà dunque alla linea BD nello stesso tempo, sia che la forza N venga impressa, sia che non venga impressa; e perciò alla fine di quel tempo si troverà in qualche punto di quella linea BD. Con lo stesso argomento, alla fine dello stesso tempo si troverà in qualche punto della linea CD; e perciò deve necessariamente trovarsi in D, punto d’incontro delle due linee. Procederà poi da A a D con moto rettilineo, per la Legge I.

### Corollario II (composizione e risoluzione delle forze)

**[L10]** **E di qui risulta evidente la composizione di una forza diretta AD a partire da forze oblique qualsiasi AB e BD; e, viceversa, la risoluzione di una forza diretta qualsiasi AD in forze oblique qualsiasi AB e BD.** Questa composizione e questa risoluzione sono ampiamente confermate dalla meccanica.

**[L11]** Supponiamo, per esempio, che i raggi disuguali OM, ON, uscenti dal centro O di una ruota, sostengano con i fili MA, NP i pesi A e P, e che si cerchino le forze dei pesi nel muovere la ruota. Per il centro O si conduca la retta KOL, che incontri perpendicolarmente i fili in K e L; con centro O e con raggio OL, la maggiore delle distanze OK, OL, si descriva un cerchio che incontri il filo MA in D; e alla retta OD, una volta condotta, sia parallela AC e perpendicolare DC. Poiché non importa se i punti K, L, D dei fili siano fissati o no al piano della ruota, i pesi avranno lo stesso effetto che se fossero sospesi ai punti K e L, oppure D e L. Si rappresenti poi la forza totale del peso A con la linea AD: essa si scomporrà nelle forze AC e CD. Di queste, AC, tirando il raggio OD direttamente via dal centro, non ha alcun effetto nel muovere la ruota; l’altra forza, DC, tirando il raggio DO perpendicolarmente, ha lo stesso effetto che avrebbe se tirasse perpendicolarmente il raggio OL, uguale a OD. Ha cioè lo stesso effetto del peso P, purché questo peso stia al peso A come la forza DC sta alla forza DA, ossia (per la similitudine dei triangoli ADC, DOK) come OK sta a OD, o a OL. I pesi A e P, che sono inversamente proporzionali ai raggi OK e OL posti in linea retta, avranno dunque la stessa efficacia e così staranno in equilibrio: è la notissima proprietà della bilancia, della leva e dell’asse nella ruota. Se uno dei due pesi è maggiore di quanto richiede questo rapporto, la sua forza nel muovere la ruota sarà maggiore in proporzione.

**[L12]** Supponiamo ora che un peso p, uguale al peso P, sia in parte sospeso al filo Np e in parte poggi sul piano obliquo pG. Si conducano pH e NH, la prima perpendicolare all’orizzonte, la seconda al piano pG. Se la forza del peso p, che tende verso il basso, è rappresentata dalla linea pH, essa può essere scomposta nelle forze pN e HN. Se vi fosse un piano pQ perpendicolare al filo pN, che tagliasse l’altro piano pG lungo una linea parallela all’orizzonte, e il peso p poggiasse soltanto su questi piani pQ e pG, esso premerebbe questi piani perpendicolarmente con le forze pN e HN: cioè il piano pQ con la forza pN e il piano pG con la forza HN. Perciò, se si toglie il piano pQ, in modo che il peso tenda il filo, il filo sarà teso con la stessa forza pN con cui prima veniva premuto il piano, poiché ora, sostenendo il peso, fa le veci del piano tolto. Pertanto la tensione di questo filo obliquo starà alla tensione dell’altro filo, quello perpendicolare PN, come pN sta a pH. E perciò, se il peso p sta al peso A nel rapporto composto dal rapporto inverso delle distanze minime dei rispettivi fili, pN e AM, dal centro della ruota e dal rapporto diretto di pH a pN, i pesi avranno lo stesso effetto nel muovere la ruota, e quindi si sosterranno a vicenda, come chiunque può verificare per esperimento.

**[L13]** Il peso p, poi, che poggia su quei due piani obliqui, sta nella condizione di un cuneo fra le facce interne di un corpo spaccato; e di qui si conoscono le forze del cuneo e del martello. La forza con cui il peso p preme il piano pQ sta infatti alla forza con cui esso, o per la propria gravità o per l’urto del martello, è spinto contro i piani lungo la linea pH, come pN sta a pH; e sta alla forza con cui preme l’altro piano pG come pN sta a NH. Anche la forza della vite si ricava con una simile scomposizione delle forze, poiché la vite è un cuneo spinto da una leva. L’uso di questo corollario è dunque vastissimo, e proprio la vastità della sua applicazione ne prova la verità: da quanto si è detto dipende infatti tutta la meccanica, dimostrata in vari modi dagli autori. Di qui, infatti, si ricavano facilmente le forze delle macchine che si sogliono comporre di ruote, tamburi, carrucole, leve, corde tese e pesi che salgono direttamente o obliquamente, e delle altre potenze meccaniche; e così pure le forze dei tendini nel muovere le ossa degli animali.

### Corollario III (conservazione della quantità di moto)

**[L14]** **La quantità di moto che si ottiene prendendo la somma delle quantità di moto dirette verso la stessa parte e la differenza di quelle dirette verso parti contrarie non cambia per l’azione dei corpi fra loro.**

**[L15]** Infatti l’azione e la reazione a essa contraria sono uguali per la Legge III, e perciò, per la Legge II, producono nelle quantità di moto cambiamenti uguali verso parti contrarie. Dunque, se le quantità di moto sono dirette verso la stessa parte, qualunque cosa si aggiunga alla quantità di moto del corpo che precede sarà sottratta a quella del corpo che lo insegue, in modo che la somma rimanga la stessa di prima. Se invece i corpi si vengono incontro, la sottrazione sarà uguale per la quantità di moto di ciascuno, e perciò la differenza delle quantità di moto dirette verso parti contrarie rimarrà la stessa.

**[L16]** Per esempio, sia il corpo sferico A tre volte maggiore del corpo sferico B e abbia due parti di velocità; e B lo segua sulla stessa retta con dieci parti di velocità, così che la quantità di moto di A stia a quella di B come sei a dieci. Si pongano le loro quantità di moto di sei e di dieci parti: la somma sarà di sedici parti. Nell’incontro dei corpi, dunque, se il corpo A guadagna tre, quattro o cinque parti di quantità di moto, il corpo B ne perderà altrettante; e perciò dopo la riflessione A procederà con nove, dieci o undici parti, e B con sette, sei o cinque, restando sempre la somma di sedici parti, come prima. Se invece il corpo A guadagna nove, dieci, undici o dodici parti, e perciò dopo l’incontro avanza con quindici, sedici, diciassette o diciotto parti, il corpo B, perdendo tante parti quante ne guadagna A, avanzerà con una parte, avendone perse nove; oppure si fermerà, avendo perso la sua quantità di moto progressiva di dieci parti; oppure tornerà indietro con una parte, avendo perso la propria quantità di moto e, per così dire, una parte in più; oppure tornerà indietro con due parti, per la sottrazione di una quantità di moto progressiva di dodici parti. Così le somme delle quantità di moto concordi, 15 + 1 o 16 + 0, e le differenze di quelle contrarie, 17 − 1 e 18 − 2, saranno sempre di sedici parti, come prima dell’incontro e della riflessione. Conosciute poi le quantità di moto con cui i corpi procedono dopo la riflessione, si troverà la velocità di ciascuno, ponendo che essa stia alla velocità prima della riflessione come la quantità di moto dopo sta a quella prima. Così nell’ultimo caso, in cui la quantità di moto del corpo A era di sei parti prima della riflessione e di diciotto dopo, e la velocità era di due parti prima della riflessione, si troverà che la sua velocità dopo la riflessione è di sei parti. Si dirà infatti: come sei parti di quantità di moto prima della riflessione stanno a diciotto parti dopo, così due parti di velocità prima della riflessione stanno a sei parti dopo.

**[L17]** Se poi i corpi, o perché non sono sferici o perché si muovono su rette diverse, si urtano obliquamente, e si cercano le loro quantità di moto dopo la riflessione, bisogna conoscere la posizione del piano da cui i corpi che si incontrano sono toccati nel punto d’incontro. Poi la quantità di moto di ciascun corpo va scomposta (per il Cor. II) in due: una perpendicolare a questo piano, l’altra parallela. Le quantità di moto parallele vanno mantenute dopo la riflessione uguali a prima, perché i corpi agiscono l’uno sull’altro lungo una linea perpendicolare a questo piano; alle quantità di moto perpendicolari si devono invece attribuire cambiamenti uguali verso parti contrarie, in modo che la somma di quelle concordi e la differenza di quelle contrarie rimangano le stesse di prima. Da riflessioni di questo genere sogliono anche nascere moti circolari dei corpi intorno ai propri centri. Ma nel seguito non considero questi casi, e sarebbe troppo lungo dimostrare tutto ciò che vi si riferisce.

### Corollario IV (centro comune di gravità)

**[L18]** **Il centro comune di gravità di due o più corpi non muta il proprio stato di moto o di quiete per le azioni dei corpi fra loro; e perciò il centro comune di gravità di tutti i corpi che agiscono gli uni sugli altri, escluse le azioni e gli impedimenti esterni, o è in quiete o si muove uniformemente in linea retta.**

**[L19]** Infatti, se due punti avanzano con moto uniforme lungo linee rette e la loro distanza viene divisa in un rapporto dato, il punto che la divide o è in quiete o avanza uniformemente in linea retta. Ciò si dimostra più avanti nel Lemma XXIII e nel suo corollario, nel caso in cui i moti dei punti avvengano nello stesso piano; e con lo stesso ragionamento si può dimostrare se quei moti non avvengono nello stesso piano. Dunque, se un numero qualsiasi di corpi si muove uniformemente lungo linee rette, il centro comune di gravità di due qualsiasi di essi o è in quiete o avanza uniformemente in linea retta, perché la linea che congiunge i centri di questi corpi, che avanzano uniformemente lungo rette, è divisa da questo centro comune in un rapporto dato. Allo stesso modo anche il centro comune di questi due e di un terzo qualsiasi o è in quiete o avanza uniformemente in linea retta, perché esso divide in un rapporto dato la distanza fra il centro comune dei due corpi e il centro del terzo. Nello stesso modo anche il centro comune di questi tre e di un quarto qualsiasi o è in quiete o avanza uniformemente in linea retta, perché esso divide in un rapporto dato la distanza fra il centro comune dei tre e il centro del quarto; e così all’infinito. Dunque, in un sistema di corpi del tutto privi di azioni reciproche e di ogni altra azione impressa su di essi dall’esterno, che perciò si muovono ciascuno uniformemente lungo la propria retta, il centro comune di gravità di tutti o è in quiete o si muove uniformemente in linea retta.

**[L20]** Inoltre, in un sistema di due corpi che agiscono l’uno sull’altro, poiché le distanze dei centri di ciascuno dal centro comune di gravità sono inversamente proporzionali ai corpi, le quantità di moto relative di questi corpi, sia di avvicinamento a quel centro sia di allontanamento da esso, saranno uguali fra loro. Perciò quel centro, per effetto dei cambiamenti uguali delle quantità di moto fatti verso parti contrarie, e quindi per effetto delle azioni di questi corpi fra loro, non è né spinto in avanti né ritardato, né subisce alcun cambiamento del proprio stato quanto al moto o alla quiete. In un sistema di più corpi, invece, poiché il centro comune di gravità di due corpi qualsiasi che agiscono l’uno sull’altro non muta in alcun modo il proprio stato per quell’azione; poiché il centro comune di gravità degli altri, con i quali quell’azione non ha a che fare, non ne subisce nulla; e poiché la distanza fra questi due centri è divisa dal centro comune di tutti i corpi in parti inversamente proporzionali alle somme totali dei corpi di cui sono i centri; perciò, se quei due centri conservano il proprio stato di moto o di quiete, anche il centro comune di tutti conserva il proprio stato; ed è manifesto che quel centro comune di tutti non muta mai il proprio stato quanto al moto e alla quiete per le azioni di due corpi fra loro. In un tale sistema, poi, tutte le azioni dei corpi fra loro o avvengono fra due corpi o sono composte di azioni fra due corpi; e perciò non producono mai alcun cambiamento nello stato di moto o di quiete del centro comune di tutti. Poiché dunque quel centro, quando i corpi non agiscono gli uni sugli altri, o è in quiete o avanza uniformemente lungo una retta, nonostante le azioni dei corpi fra loro continuerà o a essere sempre in quiete o ad avanzare sempre uniformemente in linea retta, a meno che non venga distolto da questo stato da forze impresse sul sistema dall’esterno. La legge di un sistema di più corpi è dunque la stessa di quella di un corpo isolato, quanto alla perseveranza nello stato di moto o di quiete. Il moto progressivo, infatti, sia di un corpo isolato sia di un sistema di corpi, deve sempre essere valutato dal moto del centro di gravità.

### Corollario V (moti in uno spazio in moto uniforme)

**[L21]** **I moti dei corpi racchiusi in uno spazio dato sono gli stessi fra loro, sia che quello spazio sia in quiete, sia che si muova uniformemente in linea retta senza moto circolare.**

**[L22]** Infatti le differenze delle quantità di moto dirette verso la stessa parte e le somme di quelle dirette verso parti contrarie sono all’inizio le stesse nei due casi (per ipotesi); e da queste somme o differenze nascono gli scontri e gli impeti con cui i corpi si colpiscono a vicenda. Dunque, per la Legge II, gli effetti degli scontri saranno uguali nei due casi; e perciò i moti fra loro nell’uno resteranno uguali ai moti fra loro nell’altro. Lo stesso è confermato da un esperimento evidente: tutti i moti si comportano allo stesso modo in una nave, sia che essa sia in quiete, sia che si muova uniformemente in linea retta.

### Corollario VI (forze acceleratrici uguali e parallele)

**[L23]** **Se dei corpi si muovono in un modo qualsiasi fra loro e sono sollecitati lungo linee parallele da forze acceleratrici uguali, continueranno tutti a muoversi fra loro nello stesso modo in cui si muoverebbero se non fossero spinti da quelle forze.**

**[L24]** Infatti quelle forze, agendo in egual misura (in proporzione alle quantità dei corpi da muovere) e lungo linee parallele, per la Legge II muoveranno tutti i corpi in egual misura (quanto alla velocità); e perciò non muteranno mai le loro posizioni e i loro moti fra loro.

### Scolio

#### 1. Galileo: caduta dei gravi e proiettili

**[L25]** Fin qui ho esposto principi accolti dai matematici e confermati da un’esperienza molteplice. Per mezzo delle prime due leggi e dei primi due corollari Galileo trovò che la discesa dei gravi avviene in rapporto duplicato del tempo e che il moto dei proiettili avviene lungo una parabola, in accordo con l’esperienza, se non in quanto quei moti sono un poco ritardati dalla resistenza dell’aria. Mentre un corpo cade, la gravità uniforme, agendo in egual misura in particelle di tempo uguali, imprime in quel corpo forze uguali e genera velocità uguali; e nel tempo intero imprime la forza totale e genera la velocità totale, proporzionale al tempo. E gli spazi descritti in tempi proporzionali stanno come le velocità e i tempi considerati congiuntamente, cioè in rapporto duplicato dei tempi. E quando un corpo è lanciato verso l’alto, la gravità uniforme imprime forze e toglie velocità proporzionali ai tempi; e i tempi di salita fino alle altezze massime stanno come le velocità da togliere, e quelle altezze stanno come le velocità e i tempi considerati congiuntamente, ossia in rapporto duplicato delle velocità. E il moto di un corpo lanciato lungo una retta qualsiasi, che nasce dal lancio, si compone con il moto che nasce dalla gravità.

**[L26]** Supponiamo, per esempio, che il corpo A, con il solo moto del lancio, possa descrivere in un tempo dato la retta AB, e con il solo moto di caduta possa descrivere nello stesso tempo l’altezza AC. Si completi il parallelogramma ABDC: con il moto composto, quel corpo si troverà alla fine del tempo nel luogo D; e la linea curva AED che quel corpo descriverà sarà una parabola, tangente in A alla retta AB, la cui ordinata BD è come il quadrato di AB. Dalle stesse leggi e dagli stessi corollari dipendono i risultati dimostrati sui tempi delle oscillazioni dei pendoli, confermati dall’esperienza quotidiana degli orologi.

#### 2. Gli urti: Wren, Wallis, Huygens e l’esperimento dei pendoli

**[L27]** Da queste stesse leggi e corollari, e dalla terza legge, il cavaliere Christopher Wren, il dottore in teologia John Wallis e Christiaan Huygens, di gran lunga i primi geometri della generazione precedente, trovarono separatamente le regole degli scontri e delle riflessioni dei corpi duri, e quasi nello stesso tempo le comunicarono alla Royal Society, del tutto concordi fra loro quanto a queste leggi. Pubblicò la scoperta per primo Wallis, poi Wren e Huygens. Ma la verità fu anche provata da Wren davanti alla Royal Society con l’esperimento dei pendoli, che poco dopo anche l’illustre Mariotte ritenne degno di esporre in un intero libro. Tuttavia, perché questo esperimento concordi esattamente con le teorie, bisogna tener conto sia della resistenza dell’aria sia della forza elastica dei corpi che si scontrano.

**[L28]** Siano sospesi i corpi sferici A, B a fili paralleli e uguali AC, BD, dai centri C, D. Con questi centri e con questi raggi si descrivano le semicirconferenze EAF, GBH, divise a metà dai raggi CA, DB. Si porti il corpo A in un punto qualsiasi R dell’arco EAF e, tolto il corpo B, lo si lasci andare di lì; e dopo un’oscillazione torni al punto V. RV è il ritardo dovuto alla resistenza dell’aria. Di questo RV si prenda come ST la quarta parte, situata nel mezzo, in modo cioè che RS e TV siano uguali e che RS stia a ST come 3 a 2. Questa ST rappresenterà con ottima approssimazione il ritardo nella discesa da S ad A. Si rimetta il corpo B al suo posto. Il corpo A cada dal punto S: la sua velocità nel luogo della riflessione A sarà, senza errore sensibile, tanto grande quanto se fosse caduto nel vuoto dal luogo T. Si rappresenti dunque questa velocità con la corda dell’arco TA: che la velocità di un pendolo nel punto più basso sia come la corda dell’arco descritto cadendo è infatti una proposizione notissima ai geometri. Dopo la riflessione il corpo A giunga al luogo s, e il corpo B al luogo k. Si tolga il corpo B e si trovi il luogo v dal quale, se il corpo A viene lasciato andare e dopo un’oscillazione torna al luogo r, st sia la quarta parte di rv, situata nel mezzo, in modo cioè che rs e tv siano uguali; e con la corda dell’arco tA si rappresenti la velocità che il corpo A ebbe nel luogo A subito dopo la riflessione. Infatti t sarà il luogo vero e corretto al quale il corpo A sarebbe dovuto salire senza la resistenza dell’aria. Con un metodo simile si dovrà correggere il luogo k al quale sale il corpo B e trovare il luogo l al quale quel corpo sarebbe dovuto salire nel vuoto. In questo modo si può sperimentare ogni cosa come se ci trovassimo nel vuoto.

**[L29]** Infine si dovrà moltiplicare, per così dire, il corpo A per la corda dell’arco TA, che ne rappresenta la velocità, per avere la sua quantità di moto nel luogo A subito prima della riflessione; poi per la corda dell’arco tA, per avere la sua quantità di moto nel luogo A subito dopo la riflessione. Allo stesso modo il corpo B si dovrà moltiplicare per la corda dell’arco Bl, per avere la sua quantità di moto subito dopo la riflessione. E con un metodo simile, quando i due corpi vengono lasciati andare insieme da luoghi diversi, si devono trovare le quantità di moto di entrambi, tanto prima quanto dopo la riflessione; e soltanto allora si devono confrontare le quantità di moto fra loro e ricavare gli effetti della riflessione.

**[L30]** Facendo la prova in questo modo con pendoli di dieci piedi, con corpi tanto disuguali quanto uguali, e facendo in modo che i corpi si scontrassero partendo da distanze grandissime, per esempio di otto, dodici o sedici piedi, ho sempre trovato, senza un errore di tre dita nelle misure, che, quando i corpi si incontravano direttamente, i cambiamenti delle quantità di moto prodotti nei corpi verso parti contrarie erano uguali, e quindi che l’azione e la reazione erano sempre uguali. Per esempio, se il corpo A urtava il corpo B in quiete con nove parti di quantità di moto e, perdute sette parti, procedeva dopo la riflessione con due, il corpo B balzava via con quelle sette parti. Se i corpi si venivano incontro, A con dodici parti e B con sei, e A tornava indietro con due, B tornava indietro con otto, essendo state sottratte quattordici parti da una parte e dall’altra. Dalla quantità di moto di A si sottraggano dodici parti, e non resterà nulla; se ne sottraggano altre due, e si avrà una quantità di moto di due parti nel verso contrario. Così pure, sottraendo quattordici parti dalla quantità di moto del corpo B, che è di sei parti, si avranno otto parti nel verso contrario. Se invece i corpi andavano nello stesso verso, A più veloce con quattordici parti e B più lento con cinque, e dopo la riflessione A procedeva con cinque parti, B procedeva con quattordici, essendo state trasferite nove parti da A a B. E così negli altri casi. Per l’incontro e la collisione dei corpi la quantità di moto, ricavata dalla somma delle quantità di moto concordi e dalla differenza di quelle contrarie, non cambiava mai.

**[L31]** L’errore di uno o due dita nelle misure, infatti, lo attribuirei alla difficoltà di eseguire ogni cosa con sufficiente precisione. Era difficile sia lasciar andare i pendoli insieme in modo che i corpi si urtassero nel luogo più basso AB, sia segnare i luoghi s, k ai quali i corpi salivano dopo l’incontro. Inoltre, negli stessi corpi dei pendoli, la densità disuguale delle parti e una struttura resa irregolare da altre cause introducevano errori.

#### 3. Corpi non perfettamente duri

**[L32]** Perché poi nessuno obietti che la regola per provare la quale è stato ideato questo esperimento presuppone corpi assolutamente duri, o almeno perfettamente elastici, quali non se ne trovano nelle composizioni naturali, aggiungo che gli esperimenti ora descritti riescono nei corpi molli non meno che nei duri, poiché non dipendono affatto dalla condizione della durezza. Se infatti quella regola deve essere provata in corpi non perfettamente duri, si dovrà soltanto diminuire la riflessione in una certa proporzione, secondo la quantità della forza elastica. Nella teoria di Wren e di Huygens i corpi assolutamente duri si allontanano l’uno dall’altro con la velocità dello scontro. Ciò si affermerà con maggiore certezza dei corpi perfettamente elastici. Nei corpi imperfettamente elastici la velocità di ritorno deve essere diminuita insieme con la forza elastica. Quella forza, infatti, salvo quando le parti dei corpi sono danneggiate dallo scontro o subiscono una certa estensione come sotto il martello, è, per quanto mi risulta, certa e determinata, e fa sì che i corpi si allontanino l’uno dall’altro con una velocità relativa che sta alla velocità relativa dell’incontro in un rapporto dato. L’ho verificato in questo modo con palle di lana strettamente aggomitolata e fortemente compressa. Prima, lasciando andare i pendoli e misurando la riflessione, ho trovato la quantità della forza elastica; poi, mediante questa forza, ho determinato le riflessioni in altri casi d’incontro, e gli esperimenti corrispondevano. Le palle si allontanavano sempre l’una dall’altra con una velocità relativa che stava alla velocità relativa dell’incontro circa come 5 a 9. Palle d’acciaio tornavano indietro con quasi la stessa velocità; altre, di sughero, con una velocità poco minore; nelle palle di vetro, invece, il rapporto era circa di 15 a 16. E in questo modo la terza legge, per quanto riguarda gli urti e le riflessioni, è confermata dalla teoria, che concorda pienamente con l’esperienza.

#### 4. Le attrazioni

**[L33]** Nelle attrazioni dimostro brevemente la cosa così. Fra due corpi qualsiasi A, B che si attraggono a vicenda, immagina che si interponga un ostacolo qualsiasi che ne impedisca l’incontro. Se uno dei due corpi, A, è attratto verso l’altro corpo, B, più di quanto quest’ultimo sia attratto verso il primo, l’ostacolo sarà premuto più dalla pressione del corpo A che dalla pressione del corpo B, e perciò non resterà in equilibrio. Prevarrà la pressione più forte, e farà sì che il sistema dei due corpi e dell’ostacolo si muova in linea retta verso la parte di B e, negli spazi liberi, se ne vada all’infinito con un moto sempre accelerato. Ciò è assurdo e contrario alla prima legge. Per la prima legge, infatti, il sistema dovrà perseverare nel proprio stato di quiete o di moto uniforme in linea retta; perciò i corpi premeranno l’ostacolo in egual misura, e quindi saranno attratti in egual misura l’uno verso l’altro. Ne ho fatto la prova con un magnete e del ferro. Se questi, posti separatamente in vasetti propri che si toccano, galleggiano l’uno accanto all’altro in acqua ferma, nessuno dei due spingerà l’altro: per l’uguaglianza dell’attrazione da entrambe le parti sosterranno le tendenze reciproche e, giunti infine all’equilibrio, staranno in quiete.

**[L34]** Così anche la gravità fra la Terra e le sue parti è reciproca. Si tagli la Terra FI con un piano qualsiasi EG in due parti, EGF ed EGI: i loro pesi l’una verso l’altra saranno uguali. Se infatti, con un altro piano HK parallelo al primo EG, la parte maggiore EGI viene tagliata in due parti, EGKH e HKI, delle quali HKI sia uguale alla parte EFG tagliata prima, è manifesto che la parte di mezzo EGKH, con il proprio peso, non penderà verso nessuna delle due parti estreme, ma rimarrà sospesa, per così dire, in equilibrio fra l’una e l’altra, e starà in quiete. La parte estrema HKI, invece, graverà con tutto il suo peso sulla parte di mezzo e la spingerà verso l’altra parte estrema EGF. Perciò la forza con cui EGI, somma delle parti HKI ed EGKH, tende verso la terza parte EGF è uguale al peso della parte HKI, cioè al peso della terza parte EGF. Dunque i pesi delle due parti EGI ed EGF l’una verso l’altra sono uguali, come volevo mostrare. E se quei pesi non fossero uguali, la Terra intera, galleggiando nell’etere libero, cederebbe al peso maggiore e, fuggendo da esso, se ne andrebbe all’infinito.

#### 5. Le macchine e la terza legge

**[L35]** Come nello scontro e nella riflessione hanno la stessa efficacia i corpi le cui velocità sono inversamente proporzionali alle forze insite, così, nel muovere gli strumenti meccanici, hanno la stessa efficacia, e si sostengono a vicenda con tendenze contrarie, gli agenti le cui velocità, valutate secondo la direzione delle forze, sono inversamente proporzionali alle forze. Così hanno la stessa efficacia nel muovere i bracci di una bilancia i pesi che, mentre la bilancia oscilla, sono inversamente proporzionali alle loro velocità verso l’alto e verso il basso. Cioè: se salgono e scendono verticalmente, hanno la stessa efficacia i pesi inversamente proporzionali alle distanze dall’asse della bilancia dei punti ai quali sono sospesi; se invece, impediti da piani obliqui o da altri ostacoli interposti, salgono o scendono obliquamente, hanno la stessa efficacia i pesi inversamente proporzionali alle salite e alle discese, in quanto compiute secondo la verticale; e ciò a causa della direzione della gravità verso il basso. Allo stesso modo, in una carrucola o in un paranco, la forza della mano che tira direttamente la fune sosterrà il peso, se sta al peso, che salga direttamente o obliquamente, come la velocità della salita verticale sta alla velocità della mano che tira la fune. Negli orologi e negli strumenti simili, costruiti con rotelle fra loro collegate, le forze contrarie che favoriscono e ostacolano il moto delle rotelle si sosterranno a vicenda, se sono inversamente proporzionali alle velocità delle parti delle rotelle sulle quali sono impresse. La forza della vite nel premere un corpo sta alla forza della mano che fa girare la manovella come la velocità circolare della manovella, nella parte in cui è spinta dalla mano, sta alla velocità di avanzamento della vite verso il corpo premuto. Le forze con cui il cuneo preme le due parti del legno spaccato stanno alla forza del martello sul cuneo come l’avanzamento del cuneo, secondo la direzione della forza impressa su di esso dal martello, sta alla velocità con cui le parti del legno cedono al cuneo, secondo linee perpendicolari alle facce del cuneo. E lo stesso vale per tutte le macchine.

**[L36]** L’efficacia e l’uso delle macchine consistono soltanto in questo: diminuendo la velocità accresciamo la forza, e viceversa. Di qui si risolve, in ogni genere di strumenti adatti, il problema di muovere un peso dato con una forza data, o di vincere con una forza data un’altra resistenza data. Se infatti le macchine sono costruite in modo che le velocità dell’agente e del resistente siano inversamente proporzionali alle forze, l’agente sosterrà la resistenza; e, con una maggiore disparità delle velocità, la vincerà. Certo, se la disparità delle velocità è tanto grande da vincere anche tutta la resistenza che suole nascere dall’attrito dei corpi contigui che scivolano l’uno sull’altro, dalla coesione dei corpi continui che devono essere separati e dai pesi dei corpi da sollevare, vinta tutta questa resistenza la forza in eccesso produrrà un’accelerazione del moto proporzionale a sé stessa, in parte nelle parti della macchina, in parte nel corpo che resiste. Ma trattare di meccanica non rientra nel presente disegno. Con questi esempi ho voluto soltanto mostrare quanto ampiamente si estenda e quanto sia certa la terza legge del moto. Se infatti si valuta l’azione dell’agente dalla sua forza e dalla sua velocità considerate congiuntamente, e similmente si valuta la reazione del resistente considerando congiuntamente le velocità delle sue singole parti e le forze di resistenza che nascono dal loro attrito, dalla coesione, dal peso e dall’accelerazione, l’azione e la reazione saranno sempre uguali fra loro, in ogni uso degli strumenti. E in quanto l’azione si propaga attraverso lo strumento e infine si imprime su ogni corpo che resiste, la sua direzione ultima sarà sempre contraria alla direzione della reazione.

**Fine degli assiomi e dello scolio. Nel testo originale segue il Libro I, *De motu corporum*, Sezione I.**

---

## Apparato

### A.0 Estensioni del glossario

I termini seguenti non comparivano nel glossario fisso. Ognuno è reso in modo costante in tutto il fascicolo.

| Latino | Italiano | Motivazione |
|---|---|---|
| *determinatio*, *determinari* | «direzione», «essere diretto» | Qui indica la direzione della forza o del moto, che comprende anche il verso (L04, L35, L36). Regola unificata (decisione del curatore): «direzione» in generale; «verso» soltanto dove il testo contrappone i due versi di un moto, come in Fascicolo 2, S33–S35, che resta invariato. |
| *plaga*, *pars* in *in partes contrarias* | «verso», «parte»: «verso parti contrarie» | Si conserva la spazialità del latino senza introdurre «vettore». |
| *ratio duplicata* | «rapporto duplicato» | È il rapporto composto con sé stesso, cioè il quadrato del rapporto. Il termine storico resta nel testo; l’equivalenza è nella nota N7. |
| *reflexio* | «riflessione» | Nel linguaggio degli urti del Seicento è il rimbalzo dopo lo scontro; «riflessione» conserva il termine tecnico dell’epoca. |
| *concursus* / *congressus* | «incontro» / «scontro» | Distinzione lessicale del latino, mantenuta dove possibile. |
| *conatus* | «tendenza» | Coerente con il Fascicolo 2 (*conatus recedendi*: «tendenza ad allontanarsi»). |
| *pollere*, *idem pollere*, *æquipollere* | «avere la stessa efficacia» | Evita «equipollente», raro nell’italiano scolastico. |
| *ducere in* | «moltiplicare per» | Nel linguaggio geometrico *ducere A in B* è formare il prodotto (Motte: *take the product*). |
| *motus progressivus* | «moto progressivo», «quantità di moto progressiva» | Moto di traslazione, contrapposto a quello circolare. |
| *urgere* | «premere», «sollecitare» | «Premere» per i corpi a contatto, «sollecitare» per le forze acceleratrici (Cor. VI). |
| *vires insitæ* (al plurale, L35) | «forze insite» | Applicazione del glossario fisso. Vedi nota N12. |

*Impulsus* come sostantivo non compare in questa sezione. Compare soltanto il participio, in *cuneus est a vecte impulsus* (L13), reso «spinto». *Impetus* compare una volta (L22, «gli impeti»). *Ictus* compare due volte: *ictu mallei* (L13, «l’urto del martello») e *quoad ictus & reflexiones* (L32, «gli urti e le riflessioni»).

### A.1 Legge I

**Latino:** *Corpus omne perseverare in statu suo quiescendi vel movendi uniformiter in directum, nisi quatenus a viribus impressis cogitur statum suum mutare.*

**Inglese:** “Every body perseveres in its state of rest, or of uniform motion in a right line, unless it is compelled to change that state by forces impressed thereon.”

**Scelte.**

- *nisi quatenus* è reso con **«se non in quanto»**, come richiesto dal curatore. *Quatenus* significa «nella misura in cui». Il latino non dice soltanto che il corpo persevera «a meno che» intervenga una forza, cioè una condizione sì/no. Dice che il corpo persevera **eccetto che nella misura** in cui le forze impresse lo costringono a cambiare. La formulazione è quantitativa e prepara la Legge II. Motte rende con «unless», che perde questa sfumatura.
- La stessa locuzione ricorre due volte nel commento (L02) e una volta nello Scolio (L25). Lì Motte la rende diversamente: «so far as … not», «otherwise than as», «unless so far as». Questo conferma che il senso limitativo era chiaro anche al traduttore inglese, che però non lo ha conservato nell’enunciato.
- *in directum* è reso «in linea retta», secondo il glossario. Su decisione del curatore, anche il Fascicolo 1 (Def. III e IV, v0.2) è stato uniformato: «di moto uniforme in linea retta».
- *statu suo quiescendi vel movendi*: i due gerundi sono resi con «di quiete o di moto».

### A.2 Legge II

**Latino:** *Mutationem motus proportionalem esse vi motrici impressæ, & fieri secundum lineam rectam qua vis illa imprimitur.*

**Inglese:** “The alteration of motion is ever proportional to the motive force impressed; and is made in the direction of the right line in which that force is impressed.”

**Scelte.**

- *mutationem motus* è reso con **«il cambiamento della quantità di moto»**, coerentemente con la Def. VIII del Fascicolo 1. Lì la quantità motrice della forza è «la misura … proporzionale alla quantità di moto che essa genera in un tempo dato», e *motui* è stato reso «quantità di moto». Legge II e Def. VIII usano così lo stesso termine per la stessa grandezza.
- *vi motrici impressæ*: «forza motrice impressa», secondo il glossario. Il latino unisce due aggettivi della serie delle definizioni: *motrix* (Def. VIII) e *impressa* (Def. IV).
- **Aggiunta di Motte:** «ever» non ha corrispondente nel latino.
- Nel commento (L04), *determinatur* e *determinationem* sono resi con «diretta» e «direzione». Vedi § A.0.
- Nel commento, Motte rende *vel conspiranti additur, vel contrario subducitur* con «according as they directly conspire with or are directly contrary». I due «directly» non sono nel latino.

### A.3 Legge III

**Latino:** *Actioni contrariam semper & æqualem esse reactionem: sive corporum duorum actiones in se mutuo semper esse æquales & in partes contrarias dirigi.*

**Inglese:** “To every action there is always opposed an equal reaction: or the mutual actions of two bodies upon each other are always equal, and directed to contrary parts.”

**Scelte.**

- L’italiano conserva l’ordine latino «contraria e uguale». Motte rende *contrariam* con un verbo («opposed») e lo separa da «equal».
- *sive* introduce una riformulazione equivalente, non un’alternativa: è reso «ossia».
- **Omissioni di Motte nel commento (L06–L07):**
  - *quomodocunque* («in qualsiasi modo») non è tradotto;
  - *vi alterius* («per la forza dell’altro») non è tradotto.
- **Ampliamento di Motte:** «to relax or unbend itself» per *relaxandi se*.

### A.4 Corollario I

**Latino:** *Corpus viribus conjunctis diagonalem parallelogrammi eodem tempore describere, quo latera separatis.*

**Inglese:** “A body by two forces conjoined will describe the diagonal of a parallelogram, in the same time that it would describe the sides, by those forces apart.”

**Confronto con la traduzione di lavoro del curatore.** La versione proposta era: «Un corpo, sotto due forze congiunte, descrive la diagonale di un parallelogramma nello stesso tempo in cui, sotto le forze separate, ne descriverebbe i lati.» Va corretta in un punto e può essere ritoccata in un secondo.

1. **«due» non è nel latino.** L’enunciato dice soltanto *viribus conjunctis*, «con forze congiunte». Il numero «due» è un’aggiunta di Motte («by two forces conjoined»). La dimostrazione tratta poi il caso di due forze, M e N, ma l’enunciato non lo specifica. Va tolto.
2. **«sotto»** è accettabile, ma l’ablativo *viribus* è strumentale. «Per effetto di» lo rende più esattamente e richiama la causalità delle Leggi I e II.
3. **Il condizionale «descriverebbe» va mantenuto.** Il latino è ellittico (*quo latera* [*describeret*] *separatis*) e non esprime il modo verbale. Il condizionale rende esplicito che il moto lungo i lati è controfattuale, perché le forze agiscono insieme. Motte fa la stessa scelta («would describe»).
4. *conjunctis* è un participio concreto: «congiunte», cioè agenti insieme. Non va reso con la formula del glossario «considerate congiuntamente», che è riservata all’avverbio *conjunctim* nelle proporzionalità composte.

**Testo adottato:** «Un corpo, per effetto di forze congiunte, descrive la diagonale di un parallelogramma nello stesso tempo in cui, per effetto delle forze separate, ne descriverebbe i lati.»

**Divergenze di Motte nella dimostrazione (L09):**

- Motte scrive «complete the parallelogram **ABCD**», mentre il latino ha **ABDC**. La figura del 1726 (NATP00086-1) ha A e B in alto, C e D in basso, e la diagonale AD: i vertici in ordine di perimetro sono A, B, D, C. «ABCD» farebbe di AC una diagonale, in contraddizione con la figura e con la dimostrazione. È un errore di Motte o dell’edizione 1846.
- Motte esplicita «the other force **M**» per *a vi altera*.
- Motte aggiunge la relativa «by which the body is carried towards the line BD», che nel latino è implicita in *velocitatem accedendi ad lineam illam BD*.

### A.5 Corollario II

**Latino:** *Et hinc patet compositio vis directæ AD ex viribus quibusvis obliquis AB & BD, & vicissim resolutio vis cujusvis directæ AD in obliquas quascunque AB & BD.*

**Inglese:** “And hence is explained the composition of any one direct force AD, out of any two oblique forces AC and CD; and, on the contrary, the resolution of any one direct force AD into two oblique forces AC and CD …”

**Scelte e divergenze.**

- **Lettere diverse.** Il latino ha **AB e BD**; Motte ha **AC e CD**. La figura del 1726 (NATP00086-2) è lo stesso parallelogramma del Cor. I, con A e B in alto, C e D in basso e la diagonale AD: entrambe le coppie di lati portano da A a D. Il latino è coerente con la figura; Motte sceglie l’altro percorso, ugualmente valido. Non è un errore, ma una divergenza dal testo.
- *patet* è reso «risulta evidente». Motte rende con «is explained».
- *axis in peritrochio* (L11) è il nome tecnico dell’argano a ruota, cioè la ruota fissata su un asse. È reso «l’asse nella ruota»; Motte semplifica in «the wheel».
- **Lettere nel caso del piano obliquo (L12).** Il latino ha *minimarum distantiarum filorum suorum* **pN**, AM; Motte ha **PN**, AM. Il filo del peso p è pN, cioè il filo obliquo: la lettura latina è coerente con il ragionamento, perché conta la distanza minima dal centro della retta lungo cui tira il filo obliquo. Le figure del 1726 (NATP00086-3 e -4) lo confermano: da N partono il filo verticale NP, al cui capo pende il peso P, e il filo obliquo Np, che sostiene il peso p appoggiato sul piano pG. La lettera di Motte, PN, indica il filo verticale ed è quindi un errore.
- *ad horizentem* (L12) è un refuso della trascrizione: la stampa del 1726 ha *ad horizontem*.
- **Omissioni di Motte (L13):**
  - *tympanis* («tamburi») non è tradotto;
  - *nervis tensis* («corde tese») diventa «cords».
- La trascrizione ha *cæterisque potentiis, mechanicis componi solent*. La virgola separa in modo innaturale *potentiis mechanicis*: va letto *cæterisque potentiis mechanicis*, «e delle altre potenze meccaniche». L’OCR della stampa non permette di decidere sulla virgola; la lettura non cambia.
- La trascrizione ha *atque; ad vim* (L13): la stampa del 1726 ha *atque ad vim*, senza punto e virgola.

### A.6 Corollario III

**Latino:** *Quantitas motus quæ colligitur capiendo summam motuum factorum ad eandem partem, & differentiam factorum ad contrarias, non mutatur ab actione corporum inter se.*

**Inglese:** “The quantity of motion, which is collected by taking the sum of the motions directed towards the same parts, and the difference of those that are directed to contrary parts, suffers no change from the action of bodies among themselves.”

**Scelte.**

- *motuum* è reso «quantità di moto», perché si tratta di grandezze che si sommano e si sottraggono.
- *fugientis* / *insequentis* sono resi «che precede» / «che lo insegue». Motte rende con «preceding» / «that which follows».
- Nel passo sugli urti obliqui (L17), *oriri solent* è reso «sogliono nascere»; Motte attenua in «sometimes arise».
- **Anomalia della trascrizione:** le espressioni numeriche risultano duplicate (*15+115+1 vel 16+016+0*, *17−117-1 & 18−218-2*). È un artefatto della doppia codifica, testo più formula, nella pagina web: va letto 15 + 1, 16 + 0, 17 − 1, 18 − 2, come in Motte. Non è una variante.

### A.7 Corollario IV

**Latino:** *Commune gravitatis centrum corporum duorum vel plurium, ab actionibus corporum inter se, non mutat statum suum vel motus vel quietis; & propterea corporum omnium in se mutuo agentium (exclusis actionibus & impedimentis externis) commune centrum gravitatis vel quiescit vel movetur uniformiter in directum.*

**Inglese:** “The common centre of gravity of two or more bodies does not alter its state of motion or rest by the actions of the bodies among themselves; and therefore the common centre of gravity of all bodies acting upon each other (excluding outward actions and impediments) is either at rest, or moves uniformly in a right line.”

**Scelte.**

- In L20, *motus relativi … æquales* è reso «le quantità di moto relative … uguali». Ciò che è uguale per i due corpi è il prodotto del corpo per la velocità relativa al centro, cioè una grandezza: per il glossario, «quantità di moto». Motte ha «relative motions».
- **Aggiunta di Motte:** «and much less the common centre of gravity of the others». Il latino dice soltanto che quel centro *nihil inde patitur*, «non ne subisce nulla». Il «much less» introduce un confronto che il testo non fa.
- *nec promovetur nec retardatur* è reso «non è né spinto in avanti né ritardato».

### A.8 Corollario V

**Latino:** *Corporum dato spatio inclusorum iidem sunt motus inter se, sive spatium illud quiescat, sive moveatur idem uniformiter in directum sine motu circulari.*

**Inglese:** “The motions of bodies included in a given space are the same among themselves, whether that space is at rest, or moves uniformly forwards in a right line without any circular motion.”

**Scelte.**

- *motus inter se* è reso «moti fra loro», cioè i moti relativi dei corpi.
- *congressus & impetus* è reso «gli scontri e gli impeti». Motte traduce *impetus* con «impulses», che il glossario non ammette.
- *experimento luculento* è reso «esperimento evidente». Motte ha «A clear proof … from the experiment of a ship».

### A.9 Corollario VI

**Latino:** *Si corpora moveantur quomodocunque inter se, & a viribus acceleratricibus æqualibus secundum lineas parallelas urgeantur; pergent omnia eodem modo moveri inter se, ac si viribus illis non essent incitata.*

**Inglese:** “If bodies, any how moved among themselves, are urged in the direction of parallel lines by equal accelerative forces, they will all continue to move among themselves, after the same manner as if they had been urged by no such forces.”

**Scelte.**

- *viribus acceleratricibus*: «forze acceleratrici», secondo il glossario e la Def. VII. È decisivo che siano acceleratrici e non motrici: vedi nota N9.
- La trascrizione ha *per legem II.)* con una parentesi chiusa senza apertura. La stampa del 1726 ha *movebunt per legem II.* senza parentesi: la parentesi è un artefatto della trascrizione. Motte ha «(by Law II)».

### A.10 Scolio

Per lo Scolio l’apparato registra le scelte e le divergenze passo per passo, senza ripetere il testo latino, che è nel documento di fonte.

- **L25, verbo principale.** La trascrizione del Newton Project ha *Per leges duas primas & corollaria duo prima Galilæus descensum gravium esse …*, senza verbo reggente. La stampa del 1726 ha **Galilæus invenit** (scansione ECCO, p. 21), come la ristampa del 1871: *invenit* è caduto nella trascrizione. La traduzione rende «trovò» senza parentesi. Motte traduce correttamente «discovered».
- **L25:** *aliquantulum* è reso «un poco»; Motte ha «a little».
- **L26:** *ABq.* è l’abbreviazione di *AB quadratum*, «il quadrato di AB».
- **L26:** *horologiorum experientia* è reso «esperienza … degli orologi». Motte specifica «pendulum clocks», che è un’interpretazione plausibile ma non è nel testo.
- **L27, nomi:** *Christophorus Wrennus eques auratus* è Christopher Wren, «cavaliere»; *Johannes Wallisius S.T.D.* è John Wallis, *Sacræ Theologiæ Doctor*, «dottore in teologia»; *Christianus Hugenius* è Christiaan Huygens; *Mariottus* è Edme Mariotte.
- **L27, divergenza di Motte rilevante.** Il latino dice *ætatis superioris geometrarum facile principes*, «di gran lunga i primi geometri **della generazione precedente**». Motte traduce «the greatest geometers **of our times**». Il latino colloca Wren, Wallis e Huygens nella generazione prima di quella di Newton: nel 1726 Huygens e Wallis erano morti da tempo. Motte attualizza.
- **L27, altre divergenze:** Motte omette *Clarissimus* per Mariotte, rende *theoriis* al singolare («the theory») e aggiunge «lastly» nella sequenza Wallis, Wren, Huygens.
- **L28:** *in puncto insimo* è un refuso della trascrizione: la stampa del 1726 ha *infimo*, «nel punto più basso».
- **L28:** *quam proxime* è reso «con ottima approssimazione»; Motte ha «very nearly».
- **L30, unità di misura.** *Digitus* è reso «dito», l’unità storica. Motte traduce con «inches». Come per le «miglia» del Fascicolo 1, non si converte.
- **L30, resiliebat.** Il corpo B, inizialmente in quiete e urtato da A, *resiliebat*, «balzava via». Motte scrive «was carried **backwards**», che è fuorviante: B si muove nel verso in cui procedeva A.
- **L31:** *tribuerim* (congiuntivo potenziale) è reso «lo attribuirei». Motte aggiunge «may be **easily** ascribed».
- **L32:** *in compositionibus naturalibus* è reso «nelle composizioni naturali»; Motte semplifica in «in nature». *Determinavi reflexiones* è reso «ho determinato le riflessioni»; Motte ha «estimated».
- **L33, omissione di Motte.** *In vasculis propriis* ***sese contingentibus*** significa «in vasetti propri **che si toccano**». Motte scrive «placed apart in proper vessels» e omette il contatto fra i recipienti, che è la condizione dell’esperimento: i due vasetti formano un unico sistema, come l’ostacolo dell’argomento precedente.
- **L33, trascrizione:** *facietque systema … moveatur* e *Qoud* sono refusi della trascrizione. La stampa del 1726 ha *facietque* ***ut*** *systema … moveatur* e *Quod est absurdum*.
- **L33:** *concipe* è un imperativo di seconda persona singolare, conservato nell’italiano: «immagina».
- **L34, lettere.** Qui la stampa del 1726, la trascrizione e Motte hanno tutte «la parte **EFG** tagliata prima», mentre altrove la stessa parte è **EGF**. La figura (NATP00086-8 e -9) mostra che la parte staccata dal piano EG contiene l’arco E–F–G: le due sigle indicano lo stesso pezzo, una seguendo l’arco, l’altra il contorno. Non è un errore. La traduzione conserva EFG come nell’originale.
- **L34:** *in libero æthere* è reso «nell’etere libero»; Motte aggiunge un aggettivo: «non-resisting æther».
- **L35:** *vires insitæ* è reso «forze insite», secondo il glossario. Motte ha «innate forces».
- **L36:** *in corpus omne resistens* è reso «su ogni corpo che resiste»; Motte ha il singolare «the resisting body».
- **L36:** *ultima determinatio* è reso «direzione ultima», secondo il § A.0.

### A.11 Riepilogo: dove Motte aggiunge od omette

| Luogo | Latino | Motte 1846 | Tipo |
|---|---|---|---|
| L01 | *nisi quatenus* | «unless» | perde la sfumatura limitativa |
| L02 | *& vi gravitatis impelluntur* | «**or** impelled» | congiunzione cambiata |
| L02 | *diutius* | «for a **much** longer time» | aggiunta |
| L02 | *in spatiis minus resistentibus factos* | «meeting with less resistance in more free spaces» | parafrasi ampliata |
| L03 | — | «**ever** proportional» | aggiunta |
| L04 | *conspiranti … contrario* | «**directly** conspire … **directly** contrary» | aggiunta |
| L07 | *quomodocunque*; *vi alterius* | — | omissioni |
| L08 | *viribus conjunctis* | «by **two** forces conjoined» | aggiunta |
| L09 | *ABDC* | «ABCD» | lettere errate |
| L10 | *AB & BD* | «AC and CD» | lettere diverse |
| L12 | *pN, AM* | «PN, AM» | lettera errata (vedi figura) |
| L13 | *tympanis*; *nervis tensis* | —; «cords» | omissione; semplificazione |
| L17 | *solent* | «sometimes» | attenuazione |
| L20 | *nihil inde patitur* | «**much less** …» | aggiunta |
| L22 | *impetus* | «impulses» | termine non equivalente |
| L25 | *invenit* (stampa 1726) | «discovered» | corretto (il verbo manca solo nella trascrizione) |
| L26 | *horologiorum* | «pendulum clocks» | specificazione |
| L27 | *ætatis superioris* | «of our times» | errore di senso |
| L27 | *Clarissimus*; *theoriis* | —; «the theory» | omissione; numero |
| L30 | *resiliebat* | «was carried backwards» | senso fuorviante |
| L30 | *digitorum* | «inches» | conversione di unità |
| L31 | *tribuerim* | «may be easily ascribed» | aggiunta |
| L33 | *sese contingentibus* | — | omissione rilevante |
| L34 | *libero* | «non-resisting» | specificazione |
| L36 | *corpus omne* | «the resisting body» | numero |

Motte divide inoltre in più capoversi l’ultima parte dello Scolio, sulle macchine. È una scelta tipografica che non altera il testo.

---

## Note editoriali e fisiche

Queste note sono aggiunte del presente fascicolo, non affermazioni tradotte da Newton.

### N1. Legge I: «se non in quanto»

La Legge I non è soltanto un enunciato qualitativo sull’inerzia. Con *nisi quatenus* Newton afferma che lo scostamento dallo stato di quiete o di moto uniforme è limitato **a ciò che** le forze impresse producono. In una lettura moderna, la Legge I individua i sistemi di riferimento in cui un corpo libero ha accelerazione nulla, cioè i sistemi inerziali. Questa interpretazione è posteriore e non è nel testo.

### N2. Legge II: forza o impulso?

Il commento dice che l’effetto è lo stesso «sia che [la forza] venga impressa tutta insieme e in una volta, sia gradualmente e in momenti successivi». La forza motrice impressa della Legge II è dunque misurata dal **cambiamento totale** della quantità di moto che produce, cioè da ciò che oggi si chiama impulso, **J** = Δ**p**. La formulazione moderna **F** = d**p**/d*t* si ottiene considerando il cambiamento in un tempo dato, come nella Def. VIII, e passando al limite. Non va proiettata sul testo. La Legge II è anche vettoriale nel senso dell’epoca: la quantità di moto generata «si compone» con quella esistente «secondo la direzione di entrambe».

### N3. Legge III e uguaglianza dei cambiamenti

Newton precisa che sono uguali i cambiamenti delle **quantità di moto**, non delle velocità. Per due corpi di masse *m*₁, *m*₂ che interagiscono soltanto fra loro, *m*₁Δ*v*₁ = −*m*₂Δ*v*₂, e quindi |Δ*v*₁| / |Δ*v*₂| = *m*₂ / *m*₁: «inversamente proporzionali ai corpi». L’esempio del cavallo descrive due coppie di forze uguali e contrarie trasmesse dalla fune. Non spiega da solo perché il cavallo avanzi: per questo servono anche le forze esterne del terreno, di cui Newton qui non parla.

### N4. Corollario I: velocità uniformi e forze istantanee

Nella dimostrazione le forze M e N sono **impresse nel luogo A** e poi il corpo procede «con moto uniforme». Sono quindi forze istantanee, nel senso della Def. IV: azioni che non permangono nel corpo. Il parallelogramma è costruito sugli spostamenti in un tempo dato, che sono proporzionali alle velocità generate e, per la Legge II, alle forze impresse. L’argomento usa la Legge II in forma di indipendenza delle componenti: una forza lungo AC non altera la velocità di avvicinamento a BD. Se B cade sulla retta AC, il parallelogramma degenera: il caso non è escluso dal testo, ma la costruzione perde significato. È la stessa questione aperta nello stato del progetto per la pagina interattiva.

### N5. Corollario II: momenti e lavoro virtuale

L’equilibrio della ruota, con i pesi inversamente proporzionali ai bracci OK e OL, è l’uguaglianza dei momenti: *P*·OL = *A*·OK. La costruzione con D sul cerchio di raggio OL e i triangoli simili ADC, DOK mostra che la componente utile DC del peso A sta ad A come OK sta a OD = OL. Il piano obliquo e il cuneo sono trattati con la stessa scomposizione. Per il curatore: la frase finale, secondo cui l’ampiezza d’uso del corollario «ne prova la verità», è un argomento di conferma empirica, non una dimostrazione.

### N6. Corollario III: conservazione e limiti dell’esempio

Il corollario è la conservazione della quantità di moto totale con il segno: «somma delle concordi, differenza delle contrarie». L’aritmetica di Newton è corretta in tutti i casi. Assumendo *m*_A = 3, *m*_B = 1, *v*_A = 2, *v*_B = 10, la somma è 6 + 10 = 16, e ogni coppia dopo l’urto (9 + 7, 10 + 6, 11 + 5, 15 + 1, 16 + 0, 17 − 1, 18 − 2) dà 16. La velocità finale di A nell’ultimo caso è 2 · 18/6 = 6.

Il controllo con la fisica moderna aggiunge però un’osservazione che Newton non fa, perché il corollario riguarda soltanto la quantità di moto.

| Guadagno di A | *p*_A′ | *p*_B′ | *v*_A′ | *v*_B′ | Possibile? |
|---:|---:|---:|---:|---:|---|
| 3 | 9 | 7 | 3 | 7 | No: B resta dietro A ma più veloce |
| 4 | 10 | 6 | 10/3 | 6 | No |
| 5 | 11 | 5 | 11/3 | 5 | No |
| 9 | 15 | 1 | 5 | 1 | Sì |
| 10 | 16 | 0 | 16/3 | 0 | Sì |
| 11 | 17 | −1 | 17/3 | −1 | Sì |
| 12 | 18 | −2 | 6 | −2 | Sì, ed è l’urto perfettamente elastico |

- Nei primi tre casi B, che segue A, avrebbe dopo l’urto una velocità maggiore di A: dovrebbe attraversarlo. La quantità di moto è conservata, ma il moto è cinematicamente impossibile.
- I casi fisicamente ammessi vanno dall’urto completamente anelastico (velocità comune 16/4 = 4, quindi *p*_A′ = 12, cioè un guadagno di 6) all’urto elastico (guadagno 12, con energia cinetica finale uguale a quella iniziale: 54 + 2 = 56).
- Il caso con guadagno 12 è esattamente elastico. L’energia cinetica non compare nel testo e il calcolo è un’aggiunta del curatore.

Per la didattica: il corollario mostra bene che la conservazione della quantità di moto è necessaria ma non sufficiente a determinare l’esito di un urto.

### N7. «Rapporto duplicato» e caduta dei gravi

*In duplicata ratione temporis* significa «proporzionale al quadrato del tempo». Il ragionamento dello Scolio, con lo spazio che sta come velocità e tempo considerati congiuntamente e la velocità proporzionale al tempo, dà *s* ∝ *t*². Il fattore ½ della formula moderna *s* = ½*gt*² non compare, perché Newton ragiona per proporzioni. Lo stesso vale per la salita: *h* ∝ *v*₀².

### N8. Parabola del proiettile

Con AB percorso uniformemente (*x* ∝ *t*) e AC percorso in caduta (*y* ∝ *t*²), l’ordinata BD è proporzionale ad AB², cioè *y* ∝ *x*²: la traiettoria è una parabola tangente in A alla direzione di lancio. È lo stesso parallelogramma del Cor. I, applicato a un moto uniforme e a uno uniformemente accelerato.

### N9. Corollario VI: perché «acceleratrici»

Forze **acceleratrici** uguali (Def. VII) producono velocità uguali in tempi uguali, qualunque sia la massa. Per questo Newton precisa «in proporzione alle quantità dei corpi da muovere»: le forze motrici corrispondenti sono proporzionali alle masse. In termini moderni è il caso di un campo gravitazionale uniforme, che non altera i moti relativi dei corpi di un sistema: per esempio, un sistema di corpi in caduta libera in un campo uniforme si comporta, al suo interno, come se il campo non ci fosse.

### N10. Correzione per la resistenza dell’aria

Newton prende ST pari a un quarto di RV e lo colloca al centro, con RS = TV. Il conto è coerente: RS = (RV − RV/4)/2 = 3/8 RV, ST = 2/8 RV, quindi RS : ST = 3 : 2. Il principio: la velocità nel punto più basso è proporzionale alla corda dell’arco di caduta, e l’arco «corretto» TA è quello da cui il pendolo sarebbe dovuto cadere nel vuoto per avere la velocità reale. In termini moderni, la corda dell’arco di caduta è 2*L* sin(θ/2), e la velocità nel punto più basso vale *v* = √(2*gL*(1 − cos θ)) = 2 sin(θ/2) √(*gL*). La proporzionalità alla corda è quindi esatta, non approssimata. La scelta di «un quarto al centro», invece, è un’approssimazione empirica di Newton, che il testo stesso qualifica con *quam proxime*.

### N11. Esempi numerici dello Scolio

Controllo aritmetico dei tre casi di L30:

| Caso | Prima | Dopo | Cambiamenti | Totale conservato |
|---|---|---|---|---|
| A urta B fermo | A 9, B 0 | A 2, B 7 | −7, +7 | 9 = 9 |
| Urto frontale | A +12, B −6 | A −2, B +8 | −14, +14 | differenza 6 = 6 |
| Stesso verso | A 14, B 5 | A 5, B 14 | −9, +9 | somma 19 = 19 |

Tutti i conti sono corretti. Le masse non sono date, quindi non si può controllare se i casi siano compatibili con la conservazione dell’energia.

### N12. Coefficiente di restituzione

Il «rapporto dato» fra velocità relativa di separazione e velocità relativa di avvicinamento è ciò che oggi si chiama **coefficiente di restituzione** *e*. Dai valori di Newton: lana compressa *e* ≈ 5/9 ≈ 0,56; vetro *e* ≈ 15/16 ≈ 0,94. L’affermazione che l’acciaio dia «quasi la stessa velocità» della lana è sorprendente rispetto ai valori moderni, che per sfere d’acciaio temprato sono di solito molto più alti. Si riporta il dato storico così com’è, senza correggerlo nel testo. In L35, «le cui velocità sono inversamente proporzionali alle forze insite» significa, poiché la forza insita è proporzionale alla massa (Def. III), corpi con quantità di moto uguali.

### N13. Attrazioni e Terra divisa

L’argomento dell’ostacolo deduce la Legge III per le attrazioni dalla Legge I applicata al sistema: se le attrazioni non fossero uguali, il sistema isolato accelererebbe da solo. È lo stesso schema del Cor. IV. L’esperimento con magnete e ferro galleggianti è una verifica statica. La Terra divisa in tre parti applica lo stesso ragionamento per simmetria alla gravità.

### N14. Macchine: forza per velocità

L’ultima parte dello Scolio usa il prodotto **forza per velocità**, «considerate congiuntamente», come misura dell’azione di una macchina. In termini moderni è la **potenza**, oppure, per spostamenti virtuali, il lavoro virtuale. L’uguaglianza fra azione e reazione così misurate esprime, nelle macchine ideali, il bilancio fra potenza fornita e potenza utilizzata, comprese le perdite per attrito, coesione e accelerazione. Newton la presenta come estensione della Legge III, non come un principio di conservazione dell’energia, che sarà formulato più tardi. Il «problema» di muovere un peso dato con una forza data è il problema classico della meccanica delle macchine semplici.

---

## Controllo della copertura

I gruppi seguono l’ordine del testo latino. Le pagine sono quelle dell’edizione 1726, segnate nella trascrizione con i numeri tra parentesi angolari; per Motte valgono i marcatori di pagina dell’EPUB.

| Identificatori | Incipit latino | Contenuto | 1726 | Motte 1846 |
|---|---|---|---|---|
| L01–L02 | *Corpus omne perseverare* | Legge I e commento | p. 13 | p. 83 |
| L03–L04 | *Mutationem motus proportionalem esse* | Legge II e commento | p. 13 | p. 83 |
| L05–L07 | *Actioni contrariam semper & æqualem* | Legge III e commento | p. 14 | p. 83 |
| L08–L09 | *Corpus viribus conjunctis* | Corollario I | pp. 14–15 | p. 84 |
| L10–L13 | *Et hinc patet compositio vis directæ* | Corollario II: ruota, piano obliquo, cuneo, macchine | pp. 15–17 | pp. 84–86 |
| L14–L17 | *Quantitas motus quæ colligitur* | Corollario III ed esempi | pp. 17–18 | pp. 86–87 |
| L18–L20 | *Commune gravitatis centrum* | Corollario IV | pp. 19–20 | pp. 87–88 |
| L21–L22 | *Corporum dato spatio inclusorum* | Corollario V | pp. 20–21 | pp. 88–89 |
| L23–L24 | *Si corpora moveantur quomodocunque* | Corollario VI | p. 21 | p. 89 |
| L25–L26 | *Hactenus principia tradidi* | Scolio: Galileo, caduta, parabola, pendoli | pp. 21–22 | pp. 89–90 |
| L27–L31 | *Ex his iisdem & lege tertia* | Scolio: urti, esperimento dei pendoli, errori | pp. 22–24 | pp. 90–91 |
| L32 | *Porro nequis objiciat* | Scolio: corpi non perfettamente duri | pp. 24–25 | pp. 91–92 |
| L33–L34 | *In attractionibus rem sic breviter ostendo* | Scolio: attrazioni, Terra divisa | pp. 25–26 | pp. 92–93 |
| L35–L36 | *Ut corpora in concursu & reflexione* | Scolio: macchine, conclusione sulla Legge III | pp. 26–27 | pp. 93–94 |

**Controlli eseguiti.**

0. **Stampa e figure (v0.3).** Tutte le varianti sospette della trascrizione sono state controllate sulla scansione della stampa del 1726: *invenit* (L25), *horizontem*, *atque ad vim*, *per legem II.*, *infimo*, *facietque ut*, *Quod*, *EFG*, *PE cub.* Esito: si tratta di refusi della trascrizione, tranne EFG, che è nell’originale ed è corretto. Le lettere divergenti di Motte (ABCD, AC-CD, PN) sono state confrontate con le figure originali NATP00086-1…9.

1. **Rilettura frase per frase contro il latino.** Ho confrontato in sequenza ogni periodo della trascrizione (pp. 13–27) con la traduzione, dalla prima parola, *Corpus omne perseverare*, all’ultima, *determinationi reactionis semper erit contraria*. Nessuna frase manca. Dove il latino ha un periodo lungo, l’italiano lo divide in più frasi senza omettere membri. Le frasi della Parte B sono state controllate automaticamente: tutte e 22 le stringhe latine (enunciati e passi) sono sottostringhe esatte della trascrizione, e tutte le 22 stringhe inglesi sono sottostringhe esatte del testo di Motte.
2. **Aritmetica.** Ho ricalcolato con uno script tutti gli esempi numerici:
   - Corollario III: somme e differenze di tutti i sette casi e velocità finale di A;
   - Scolio: i tre urti dei pendoli e il rapporto RS : ST = 3 : 2.
   Tutti i conti di Newton risultano corretti (note N6, N10, N11). Lo stesso controllo ha messo in luce l’impossibilità cinematica di tre casi del Cor. III (nota N6), che non è un errore aritmetico.
3. **Confronto con Motte.** Ho confrontato tutta la sezione corrispondente, pp. 83–94. Le divergenze sono raccolte nel § A.11.
4. **Separazione fra testo e commento.** Il testo tradotto non contiene formule moderne; le integrazioni del curatore sono tra parentesi quadre.

**Non ho potuto verificare:**

- **la virgola in *potentiis, mechanicis*** (L13): l’OCR della stampa del 1726 non è leggibile in quel punto; la lettura non cambia;
- **le pagine a stampa del 1726 nella loro interezza:** il controllo v0.3 ha riguardato i punti dubbi, cercati nel testo OCR della scansione ECCO, non una collazione completa riga per riga;
- **la corrispondenza esatta della numerazione di pagina di Motte.** Deriva dai marcatori dell’EPUB Gutenberg, non da un esemplare a stampa.

---

## Annotazioni fuori perimetro (Libro I)

Non tradotte. Testo latino: Newton Project **NATP00087**, *De Motu Corporum (Liber Primus) (1726)*, salvato nel progetto come `fonti/latino-1726-L1-S01.md`, `-S02.md` e `-S03.md`. Testo inglese: `fonti/motte-1846-Assiomi-e-passi-Libro-I.md`.

### F1. Lemma I, *constanter tendunt* (1726, p. 28)

**Latino:** *Quantitates, ut & quantitatum rationes, quæ ad æqualitatem tempore quovis finito* ***constanter tendunt****, & ante finem temporis illius propius ad invicem accedunt quam pro data quavis differentia, fiunt ultimo æquales.*

**Motte 1846:** «… which in any finite time **converge continually** to equality …»

La lettura *constanter tendunt* è **confermata**. *Constanter* indica una tendenza che non viene meno, non una velocità costante di avvicinamento: «costantemente» rischierebbe di suggerire un ritmo uniforme, che il lemma non richiede.

**Decisione del curatore:** «tendono **senza interruzione** all’uguaglianza». Da applicare nel fascicolo del Libro I e nella pagina del Lemma I.

### F2. Prop. I, *impulsu unico sed magno* (1726, p. 39)

**Latino:** *Verum ubi corpus venit ad B, agat vis centripeta* ***impulsu unico sed magno****, efficiatque ut corpus de recta Bc declinet & pergat in recta BC.*

**Motte 1846:** «… suppose that a centripetal force acts **at once with a great impulse** …»

La lettura è **confermata**. Motte rende *unico* con «at once», in senso temporale, e perde l’opposizione *unico **sed** magno*. Nello stesso passo il corpo descrive AB *vi insita*, che Motte rende «by its innate force»: nella nostra traduzione sarà «per la forza insita», secondo il glossario. **Decisione del curatore:** «agisca la forza centripeta **con un impulso unico ma grande**». È un’eccezione motivata al glossario (*impulsus*: «spinta», oppure «impulso» dove il contesto lo richiede). Si tratta di un’azione istantanea che cambia la quantità di moto (nota N2), e il Cor. 3 della stessa proposizione usa *impulsibus vis centripetæ* proprio come misura del cambiamento di moto. Da applicare nel fascicolo del Libro I e nella pagina della Prop. I.

### F3. Prop. XI, seconda dimostrazione: PE³/SP² (1726, p. 56)

**Latino:** *… & vis, qua corpus idem P circum aliud quodvis ellipseos punctum S revolvi potest, si CE & PS concurrant in E, erit ut* ***PE cub. / SPq*** *(per corol. 3. prop. vii.) hoc est, si punctum S sit umbilicus ellipseos, ideoque PE detur, ut SPq reciproce.*

**Motte 1846:** nell’EPUB la formula (SVG n. 96) si legge **PE²/SP²**.

**Esito:** il latino del 1726 ha **PE cub.**, cioè **PE³/SP²**. La lezione di Motte 1846 è un **refuso** dell’edizione inglese, o almeno della sua resa digitale. Lo confermano due riscontri indipendenti:

1. **La derivazione.** Il Cor. 3 della Prop. VII dà, nel latino (1726, p. 50):

   forza verso S : forza verso R = SP · RP² : SG³.

   Con R = C e SG = CP · SP / PE (triangoli simili SGP e PCE), si ottiene forza verso S ∝ PE³/SP². Ho verificato numericamente su un’ellisse di prova sia SG = CP · SP / PE sia PE = AC.
2. **Il passo parallelo della Prop. XII** (iperbole, 1726, p. 57): anche lì il latino ha *vis ad umbilicum S tendens erit ut* ***PE cub. / SPq***.

La conclusione 1/SP² non cambia, perché PE = AC è costante. Nella pagina interattiva della Prop. XI il testo a fronte di Motte va corretto con una nota: «Motte 1846: PE²; latino 1726: PE³».

**Motte 1729.** Nella prima edizione della traduzione di Motte (Londra 1729, vol. I, p. 80; Internet Archive `bub_gb_Tm0FAAAAQAAJ`, visto sull’immagine della pagina) la formula è stampata correttamente: **PE³/SP²**. Il refuso PE² è dunque dell’**edizione americana del 1846** (o della sua trascrizione Gutenberg), non di Motte. Anche la stampa latina del 1726 ha *PE cub.* (scansione ECCO, p. 56).

---

## Registro del lavoro successivo

| Unità | Stato |
|---|---|
| Definizioni I–VIII | Fascicolo 1, prima versione |
| Scolio alle definizioni | Fascicolo 2, prima versione |
| Assiomi: Leggi I–III, Corollari I–VI, Scolio | **Fascicolo 3, presente documento, prima versione** |
| Dati per le pagine interattive dei Cor. I e II | Parte B di questo fascicolo; il Cor. I è già nel pilota e va riallineato a questa traduzione |
| Riscontro sulle immagini del latino a stampa (pp. 13–27) e sulle figure NATP00086-1…9 | **Eseguito per tutti i punti dubbi** (v0.3); collazione integrale non eseguita |
| Revisione unitaria del glossario | **Decisa** (v0.3): *in directum* → «in linea retta» (Fasc. 1 aggiornato a v0.2); *determinatio* → «direzione», «verso» solo per i due versi contrapposti (Fasc. 2 invariato) |
| Lemma I, Prop. I, Prop. XI sul latino 1726 | **Verificati e decisi**: *constanter* → «senza interruzione»; *impulsu* → «impulso unico ma grande»; Prop. XI, PE³ nel latino 1726 e in Motte 1729, refuso PE² solo nell’edizione 1846 |
| Pagina Prop. XI del pilota | Correggere il testo a fronte di Motte (PE² → nota con PE³) |
| Pagina Prop. I del pilota | Allineare *impulsu unico sed magno* alla scelta del curatore (F2) |
| Pagina interattiva dello Scolio, parabola (figura 5, L26) | Candidata: ha figura e costruzione, ma non è un corollario |
| Revisione filologica e scientifica indipendente | Da eseguire, come previsto dalla skill di verifica |

Il presente testo è una nuova traduzione assistita da IA. Non riproduce le traduzioni italiane moderne di Pala o Giudice. **Licenza prevista** (decisione del curatore): testi e traduzioni CC BY-SA 4.0, codice MIT. La trascrizione latina è © The Newton Project e non va ridistribuita finché non se ne chiariscono le condizioni d’uso; i testi di Motte (1729, 1846) sono di pubblico dominio.

---

## Parte B — Dati per le pagine interattive

Corollari con dimostrazione e figura: **I** e **II**. I Corollari III–VI non hanno figura: il IV rimanda al Lemma XXIII del Libro I. Per questo non sono inclusi.

Convenzioni:

- `la`: testo latino esatto della trascrizione, compresi i refusi, annotati in `nota`;
- `it`: la traduzione di questo fascicolo;
- `en`: Motte 1846, allineato per senso;
- `dipende_da`: soltanto i rimandi citati nella frase. Nel Cor. II nessuna frase cita leggi o corollari: *hinc* rimanda implicitamente al Cor. I, e lo segnala la `nota` del corollario;
- `figura.mostra`: gli elementi da rendere visibili al passo; `figura.evidenzia`: le relazioni da mettere in risalto.

```json
{
  "fascicolo": "03-Leggi",
  "versione": "0.1",
  "data": "2026-11-08",
  "convenzioni": {
    "dipende_da": "solo rimandi citati esplicitamente nel testo latino della frase",
    "en": "Motte 1846; allineamento per senso, perché Motte non segue sempre la divisione in frasi del latino",
    "figura.mostra": "elementi da rendere visibili a quel passo, cumulativi rispetto ai passi precedenti salvo indicazione"
  },
  "corollari": [
    {
      "id": "cor-1",
      "titolo": "Corollario I — Parallelogramma delle forze",
      "copertura": [
        "L08",
        "L09"
      ],
      "fonti": {
        "la": "",
        "en": "Motte 1846, p. 84"
      },
      "enunciato": {
        "la": "",
        "it": "Un corpo, per effetto di forze congiunte, descrive la diagonale di un parallelogramma nello stesso tempo in cui, per effetto delle forze separate, ne descriverebbe i lati.",
        "en": "A body by two forces conjoined will describe the diagonal of a parallelogram, in the same time that it would describe the sides, by those forces apart."
      },
      "figura_base": {
        "punti": [
          "A",
          "B",
          "C",
          "D"
        ],
        "forze": [
          "M (impressa in A, porta il corpo verso B)",
          "N (impressa in A, porta il corpo verso C)"
        ],
        "vincoli": [
          "ABDC parallelogramma: BD ∥ AC, CD ∥ AB",
          "AD diagonale",
          "B non sulla retta AC (altrimenti il parallelogramma degenera)"
        ]
      },
      "passi": [
        {
          "id": "cor1-p1",
          "la": "",
          "it": "Supponiamo che un corpo, in un tempo dato, per effetto della sola forza M impressa nel luogo A, sia portato con moto uniforme da A a B; e che, per effetto della sola forza N impressa nel medesimo luogo, sia portato da A a C. Si completi il parallelogramma ABDC: per effetto di entrambe le forze, quel corpo sarà portato nello stesso tempo lungo la diagonale, da A a D.",
          "en": "If a body in a given time, by the force M impressed apart in the place A, should with an uniform motion be carried from A to B; and by the force N impressed apart in the same place, should be carried from A to C; complete the parallelogram ABCD, and, by both forces acting together, it will in the same time be carried in the diagonal from A to D.",
          "dipende_da": [],
          "figura": {
            "mostra": [
              "A",
              "forza M",
              "segmento AB",
              "forza N",
              "segmento AC",
              "lati BD e CD (completamento)",
              "diagonale AD"
            ],
            "evidenzia": [
              "AB e AC come spostamenti nel tempo dato",
              "AD"
            ]
          },
          "nota": "Motte scrive ABCD; il latino ABDC (apparato A.4)."
        },
        {
          "id": "cor1-p2",
          "la": "",
          "it": "Poiché infatti la forza N agisce lungo la linea AC, parallela a BD, per la Legge II questa forza non muterà affatto la velocità di avvicinamento a quella linea BD generata dall’altra forza.",
          "en": "For since the force N acts in the direction of the line AC, parallel to BD, this force (by the second law) will not at all alter the velocity generated by the other force M, by which the body is carried towards the line BD.",
          "dipende_da": [
            "Legge II"
          ],
          "figura": {
            "mostra": [
              "retta AC",
              "retta BD",
              "parallelismo AC ∥ BD",
              "velocità di avvicinamento a BD (generata da M)"
            ],
            "evidenzia": [
              "AC ∥ BD"
            ]
          }
        },
        {
          "id": "cor1-p3",
          "la": "",
          "it": "Il corpo giungerà dunque alla linea BD nello stesso tempo, sia che la forza N venga impressa, sia che non venga impressa; e perciò alla fine di quel tempo si troverà in qualche punto di quella linea BD.",
          "en": "The body therefore will arrive at the line BD in the same time, whether the force N be impressed or not; and therefore at the end of that time it will be found somewhere in the line BD.",
          "dipende_da": [],
          "figura": {
            "mostra": [
              "retta BD",
              "posizione finale: su BD (punto non ancora determinato)"
            ],
            "evidenzia": [
              "retta BD come luogo dei punti possibili"
            ]
          }
        },
        {
          "id": "cor1-p4",
          "la": "",
          "it": "Con lo stesso argomento, alla fine dello stesso tempo si troverà in qualche punto della linea CD; e perciò deve necessariamente trovarsi in D, punto d’incontro delle due linee.",
          "en": "By the same argument, at the end of the same time it will be found somewhere in the line CD. Therefore it will be found in the point D, where both lines meet.",
          "dipende_da": [],
          "figura": {
            "mostra": [
              "retta CD",
              "retta BD",
              "intersezione D"
            ],
            "evidenzia": [
              "D = BD ∩ CD"
            ]
          },
          "nota": "Lo stesso argomento del passo 2 con i ruoli di M e N scambiati; il testo non cita di nuovo la Legge II."
        },
        {
          "id": "cor1-p5",
          "la": "",
          "it": "Procederà poi da A a D con moto rettilineo, per la Legge I.",
          "en": "But it will move in a right line from A to D, by Law I.",
          "dipende_da": [
            "Legge I"
          ],
          "figura": {
            "mostra": [
              "traiettoria rettilinea AD percorsa con moto uniforme"
            ],
            "evidenzia": [
              "AD"
            ]
          }
        }
      ]
    },
    {
      "id": "cor-2",
      "titolo": "Corollario II — Composizione e risoluzione delle forze; la ruota, il piano obliquo, il cuneo",
      "copertura": [
        "L10",
        "L11",
        "L12",
        "L13"
      ],
      "fonti": {
        "la": "",
        "en": "Motte 1846, pp. 84–86"
      },
      "nota": "Il testo non cita esplicitamente leggi o corollari: «hinc» (di qui) rimanda implicitamente al Cor. I, ma per regola non è inserito in dipende_da. Le figure 3 e 4 non erano disponibili: i punti elencati sono ricavati soltanto dalle lettere del testo.",
      "enunciato": {
        "la": "",
        "it": "E di qui risulta evidente la composizione di una forza diretta AD a partire da forze oblique qualsiasi AB e BD; e, viceversa, la risoluzione di una forza diretta qualsiasi AD in forze oblique qualsiasi AB e BD.",
        "en": "And hence is explained the composition of any one direct force AD, out of any two oblique forces AC and CD; and, on the contrary, the resolution of any one direct force AD into two oblique forces AC and CD"
      },
      "figura_base": {
        "figura_2": {
          "punti": [
            "A",
            "B",
            "D"
          ],
          "nota": "triangolo delle forze AB, BD, AD (lettere del latino; Motte: AC, CD)"
        },
        "figura_3": {
          "punti": [
            "O",
            "M",
            "N",
            "A",
            "P",
            "K",
            "L",
            "D",
            "C"
          ],
          "vincoli": [
            "O centro della ruota",
            "OM, ON raggi disuguali",
            "MA, NP fili verticali con i pesi A, P",
            "KOL retta per O perpendicolare ai fili in K, L",
            "cerchio di centro O e raggio OL incontra MA in D",
            "AC ∥ OD, DC ⊥ OD"
          ]
        },
        "figura_4": {
          "punti": [
            "p",
            "N",
            "G",
            "H",
            "Q",
            "P",
            "A",
            "M"
          ],
          "vincoli": [
            "p peso uguale a P, sospeso al filo Np e poggiato sul piano obliquo pG",
            "pH verticale",
            "NH ⊥ piano pG",
            "pQ piano ipotetico ⊥ filo pN, che taglia pG lungo una linea orizzontale"
          ]
        }
      },
      "passi": [
        {
          "id": "cor2-p1",
          "la": "",
          "it": "Questa composizione e questa risoluzione sono ampiamente confermate dalla meccanica.",
          "en": "which composition and resolution are abundantly confirmed from mechanics.",
          "dipende_da": [],
          "figura": {
            "mostra": [
              "figura 2: AB, BD, AD"
            ],
            "evidenzia": [
              "AD come risultante"
            ]
          }
        },
        {
          "id": "cor2-p2",
          "la": "",
          "it": "Supponiamo, per esempio, che i raggi disuguali OM, ON, uscenti dal centro O di una ruota, sostengano con i fili MA, NP i pesi A e P, e che si cerchino le forze dei pesi nel muovere la ruota. Per il centro O si conduca la retta KOL, che incontri perpendicolarmente i fili in K e L; con centro O e con raggio OL, la maggiore delle distanze OK, OL, si descriva un cerchio che incontri il filo MA in D; e alla retta OD, una volta condotta, sia parallela AC e perpendicolare DC.",
          "en": "As if the unequal radii OM and ON drawn from the centre O of any wheel, should sustain the weights A and P by the cords MA and NP; and the forces of those weights to move the wheel were required. Through the centre O draw the right line KOL, meeting the cords perpendicularly in K and L; and from the centre O, with OL the greater of the distances OK and OL, describe a circle, meeting the cord MA in D: and drawing OD, make AC parallel and DC perpendicular thereto.",
          "dipende_da": [],
          "figura": {
            "mostra": [
              "ruota di centro O",
              "raggi OM, ON",
              "fili MA, NP",
              "pesi A, P",
              "retta KOL",
              "cerchio (O, OL)",
              "D",
              "OD",
              "AC ∥ OD",
              "DC ⊥ OD"
            ],
            "evidenzia": [
              "costruzione progressiva: KOL → cerchio → D → OD → C"
            ]
          }
        },
        {
          "id": "cor2-p3",
          "la": "",
          "it": "Poiché non importa se i punti K, L, D dei fili siano fissati o no al piano della ruota, i pesi avranno lo stesso effetto che se fossero sospesi ai punti K e L, oppure D e L.",
          "en": "Now, it being indifferent whether the points K, L, D, of the cords be fixed to the plane of the wheel or not, the weights will have the same effect whether they are suspended from the points K and L, or from D and L.",
          "dipende_da": [],
          "figura": {
            "mostra": [
              "K",
              "L",
              "D",
              "punti di sospensione equivalenti"
            ],
            "evidenzia": [
              "K ↔ D sullo stesso filo MA"
            ]
          }
        },
        {
          "id": "cor2-p4",
          "la": "",
          "it": "Si rappresenti poi la forza totale del peso A con la linea AD: essa si scomporrà nelle forze AC e CD. Di queste, AC, tirando il raggio OD direttamente via dal centro, non ha alcun effetto nel muovere la ruota; l’altra forza, DC, tirando il raggio DO perpendicolarmente, ha lo stesso effetto che avrebbe se tirasse perpendicolarmente il raggio OL, uguale a OD. Ha cioè lo stesso effetto del peso P, purché questo peso stia al peso A come la forza DC sta alla forza DA, ossia (per la similitudine dei triangoli ADC, DOK) come OK sta a OD, o a OL.",
          "en": "Let the whole force of the weight A be represented by the line AD, and let it be resolved into the forces AC and CD; of which the force AC, drawing the radius OD directly from the centre, will have no effect to move the wheel: but the other force DC, drawing the radius DO perpendicularly, will have the same effect as if it drew perpendicularly the radius OL equal to OD; that is, it will have the same effect as the weight P, if that weight is to the weight A as the force DC is to the force DA; that is (because of the similar triangles ADC, DOK), as OK to OD or OL.",
          "dipende_da": [],
          "figura": {
            "mostra": [
              "AD (forza del peso A)",
              "componente AC (radiale, inefficace)",
              "componente CD (tangenziale)",
              "OD = OL",
              "triangoli simili ADC, DOK"
            ],
            "evidenzia": [
              "DC : DA = OK : OD",
              "P : A = DC : DA"
            ]
          }
        },
        {
          "id": "cor2-p5",
          "la": "",
          "it": "I pesi A e P, che sono inversamente proporzionali ai raggi OK e OL posti in linea retta, avranno dunque la stessa efficacia e così staranno in equilibrio: è la notissima proprietà della bilancia, della leva e dell’asse nella ruota.",
          "en": "Therefore the weights A and P, which are reciprocally as the radii OK and OL that lie in the same right line, will be equipollent, and so remain in equilibrio; which is the well known property of the balance, the lever, and the wheel.",
          "dipende_da": [],
          "figura": {
            "mostra": [
              "bracci OK, OL",
              "pesi A, P"
            ],
            "evidenzia": [
              "A · OK = P · OL (equilibrio)"
            ]
          }
        },
        {
          "id": "cor2-p6",
          "la": "",
          "it": "Se uno dei due pesi è maggiore di quanto richiede questo rapporto, la sua forza nel muovere la ruota sarà maggiore in proporzione.",
          "en": "If either weight is greater than in this ratio, its force to move the wheel will be so much greater.",
          "dipende_da": [],
          "figura": {
            "mostra": [
              "pesi A, P variabili"
            ],
            "evidenzia": [
              "squilibrio e verso di rotazione"
            ]
          }
        },
        {
          "id": "cor2-p7",
          "la": "",
          "it": "Supponiamo ora che un peso p, uguale al peso P, sia in parte sospeso al filo Np e in parte poggi sul piano obliquo pG. Si conducano pH e NH, la prima perpendicolare all’orizzonte, la seconda al piano pG. Se la forza del peso p, che tende verso il basso, è rappresentata dalla linea pH, essa può essere scomposta nelle forze pN e HN.",
          "en": "If the weight p, equal to the weight P, is partly suspended by the cord Np, partly sustained by the oblique plane pG; draw pH, NH, the former perpendicular to the horizon, the latter to the plane pG; and if the force of the weight p tending downwards is represented by the line pH, it may be resolved into the forces pN, HN.",
          "dipende_da": [],
          "figura": {
            "mostra": [
              "peso p",
              "filo Np",
              "piano obliquo pG",
              "pH verticale",
              "NH ⊥ pG",
              "componenti pN, HN"
            ],
            "evidenzia": [
              "pH = pN + NH (scomposizione)"
            ]
          }
        },
        {
          "id": "cor2-p8",
          "la": "",
          "it": "Se vi fosse un piano pQ perpendicolare al filo pN, che tagliasse l’altro piano pG lungo una linea parallela all’orizzonte, e il peso p poggiasse soltanto su questi piani pQ e pG, esso premerebbe questi piani perpendicolarmente con le forze pN e HN: cioè il piano pQ con la forza pN e il piano pG con la forza HN.",
          "en": "If there was any plane pQ, perpendicular to the cord pN, cutting the other plane pG in a line parallel to the horizon, and the weight p was supported only by those planes pQ, pG, it would press those planes perpendicularly with the forces pN, HN; to wit, the plane pQ with the force pN, and the plane pG with the force HN.",
          "dipende_da": [],
          "figura": {
            "mostra": [
              "piano ipotetico pQ ⊥ pN",
              "piano pG",
              "forze normali pN su pQ, HN su pG"
            ],
            "evidenzia": [
              "pQ (tratteggiato: ipotetico)"
            ]
          },
          "nota": "«horizentem» è refuso della trascrizione per «horizontem»."
        },
        {
          "id": "cor2-p9",
          "la": "",
          "it": "Perciò, se si toglie il piano pQ, in modo che il peso tenda il filo, il filo sarà teso con la stessa forza pN con cui prima veniva premuto il piano, poiché ora, sostenendo il peso, fa le veci del piano tolto.",
          "en": "And therefore if the plane pQ was taken away, so that the weight might stretch the cord, because the cord, now sustaining the weight, supplies the place of the plane that was removed, it will be strained by the same force pN which pressed upon the plane before.",
          "dipende_da": [],
          "figura": {
            "mostra": [
              "pQ rimosso",
              "filo pN teso",
              "tensione = pN"
            ],
            "evidenzia": [
              "sostituzione piano → filo"
            ]
          }
        },
        {
          "id": "cor2-p10",
          "la": "",
          "it": "Pertanto la tensione di questo filo obliquo starà alla tensione dell’altro filo, quello perpendicolare PN, come pN sta a pH.",
          "en": "Therefore, the tension of this oblique cord pN will be to that of the other perpendicular cord PN as pN to pH.",
          "dipende_da": [],
          "figura": {
            "mostra": [
              "filo obliquo pN",
              "filo verticale PN (peso P)",
              "pN, pH"
            ],
            "evidenzia": [
              "T(pN) : T(PN) = pN : pH"
            ]
          },
          "nota": "La trascrizione unisce questa frase alla seguente con una virgola seguita da «Ideoque» maiuscolo: probabile punto fermo caduto."
        },
        {
          "id": "cor2-p11",
          "la": "",
          "it": "E perciò, se il peso p sta al peso A nel rapporto composto dal rapporto inverso delle distanze minime dei rispettivi fili, pN e AM, dal centro della ruota e dal rapporto diretto di pH a pN, i pesi avranno lo stesso effetto nel muovere la ruota, e quindi si sosterranno a vicenda, come chiunque può verificare per esperimento.",
          "en": "And therefore if the weight p is to the weight A in a ratio compounded of the reciprocal ratio of the least distances of the cords PN, AM, from the centre of the wheel, and of the direct ratio of pH to pN, the weights will have the same effect towards moving the wheel and will therefore sustain each other; as any one may find by experiment.",
          "dipende_da": [],
          "figura": {
            "mostra": [
              "distanza minima di O dalla retta del filo pN",
              "distanza minima di O dal filo AM (= OK)",
              "pH, pN"
            ],
            "evidenzia": [
              "p : A = [d(AM) : d(pN)] · [pH : pN]"
            ]
          },
          "nota": "Il latino ha pN, Motte PN (apparato A.5)."
        },
        {
          "id": "cor2-p12",
          "la": "",
          "it": "Il peso p, poi, che poggia su quei due piani obliqui, sta nella condizione di un cuneo fra le facce interne di un corpo spaccato; e di qui si conoscono le forze del cuneo e del martello. La forza con cui il peso p preme il piano pQ sta infatti alla forza con cui esso, o per la propria gravità o per l’urto del martello, è spinto contro i piani lungo la linea pH, come pN sta a pH; e sta alla forza con cui preme l’altro piano pG come pN sta a NH.",
          "en": "But the weight p pressing upon those two oblique planes, may be considered as a wedge between the two internal surfaces of a body split by it; and hence the forces of the wedge and the mallet may be determined; for because the force with which the weight p presses the plane pQ is to the force with which the same, whether by its own gravity, or by the blow of a mallet, is impelled in the direction of the line pH towards both the planes, as pN to pH; and to the force with which it presses the other plane pG, as pN to NH.",
          "dipende_da": [],
          "figura": {
            "mostra": [
              "p fra i piani pQ e pG come cuneo",
              "spinta lungo pH",
              "pN, pH, NH"
            ],
            "evidenzia": [
              "F(pQ) : F(pH) = pN : pH",
              "F(pQ) : F(pG) = pN : NH"
            ]
          }
        },
        {
          "id": "cor2-p13",
          "la": "",
          "it": "Anche la forza della vite si ricava con una simile scomposizione delle forze, poiché la vite è un cuneo spinto da una leva.",
          "en": "And thus the force of the screw may be deduced from a like resolution of forces; it being no other than a wedge impelled with the force of a lever.",
          "dipende_da": [],
          "figura": {
            "mostra": []
          },
          "nota": "Nessun elemento della figura: passo discorsivo."
        },
        {
          "id": "cor2-p14",
          "la": "",
          "it": "L’uso di questo corollario è dunque vastissimo, e proprio la vastità della sua applicazione ne prova la verità: da quanto si è detto dipende infatti tutta la meccanica, dimostrata in vari modi dagli autori.",
          "en": "Therefore the use of this Corollary spreads far and wide, and by that diffusive extent the truth thereof is farther confirmed. For on what has been said depends the whole doctrine of mechanics variously demonstrated by different authors.",
          "dipende_da": [],
          "figura": {
            "mostra": []
          },
          "nota": "Nessun elemento della figura: passo discorsivo."
        },
        {
          "id": "cor2-p15",
          "la": "",
          "it": "Di qui, infatti, si ricavano facilmente le forze delle macchine che si sogliono comporre di ruote, tamburi, carrucole, leve, corde tese e pesi che salgono direttamente o obliquamente, e delle altre potenze meccaniche; e così pure le forze dei tendini nel muovere le ossa degli animali.",
          "en": "For from hence are easily deduced the forces of machines, which are compounded of wheels, pullies, levers, cords, and weights, ascending directly or obliquely, and other mechanical powers; as also the force of the tendons to move the bones of animals.",
          "dipende_da": [],
          "figura": {
            "mostra": []
          },
          "nota": "Motte omette «tympanis» (tamburi). Nessun elemento della figura."
        }
      ]
    }
  ]
}
```

**Fine del Fascicolo 3.**
