> **Copia pubblica.** In questa versione i campi `"la"` della Parte B sono vuoti: le frasi latine vengono dalla trascrizione del Newton Project, che non si ridistribuisce. Il latino del 1726 si legge su newtonproject.ox.ac.uk.

# Isaac Newton
# Principi matematici della filosofia naturale

## Fascicolo 21 — Libro III: regole del filosofare e fenomeni

**Nuova traduzione italiana di lavoro dal latino del 1726, confrontata con l’inglese di Andrew Motte nell’edizione del 1846.**

Versione 0.1 — 8 novembre 2026. Preparata con Claude (Anthropic) per Massimo Bosetti.

### Stato e perimetro

Questo fascicolo apre il **Libro III**, *De mundi systemate*, e segue il Fascicolo 20, che chiude il Libro II. Traduce integralmente il titolo e l’introduzione del Libro III; le **Regole del filosofare** I–IV con i loro commenti; i **Fenomeni** I–VI con le cinque tabelle numeriche (tempi periodici e distanze dei satelliti di Giove e di Saturno; tempi periodici e distanze medie dei pianeti); e il titolo **«Proposizioni.»**, con cui si chiude il perimetro. Le Proposizioni I–XIV sono nel Fascicolo 22. È una traduzione di lavoro, non un’edizione critica validata.

Gli identificatori **III.G1.01–III.G1.33** e i titoli tematici tra parentesi sono aggiunte editoriali. Servono a orientare la lettura e a controllare la completezza. I numeri romani delle regole e dei fenomeni appartengono al testo originale. Le integrazioni del curatore sono tra parentesi quadre. Le note poste dopo la traduzione non fanno parte del testo di Newton. Le tabelle sono ricostruite come tabelle Markdown a partire dalla trascrizione latina, che le spezza in una cella per riga; le intestazioni sono tradotte, le cifre restano come nel testo.

In coda al fascicolo c’è la **Parte B**, con le dieci unità del gruppo G1 (Regole I–IV, Fenomeni I–VI) come unità senza passi (`"passi": []`), secondo le istruzioni del Libro III; i Fenomeni I, II e IV hanno un campo `"dati"` con i valori delle tabelle e l’esito dei controlli numerici.

### Fonti effettivamente consultate

1. **Latino di riferimento.** Isaac Newton, *Philosophiæ Naturalis Principia Mathematica*, terza edizione, Londra, 1726, Libro III, **pp. 386–395** (titolo e introduzione a p. 386; Regole pp. 387–389; Fenomeni pp. 390–394; «Propositiones» a p. 395, secondo i marcatori ‹386›–‹395› della trascrizione). Trascrizione normalizzata del Newton Project, documento **NATP00303**, estratta in testo semplice senza correzioni: `fonti/latino-1726/latino-1726-L3-Regole-Fenomeni.md`. La sezione non ha figure.
2. **Inglese di confronto.** *Newton’s Principia*, traduzione di Andrew Motte, New York, Daniel Adee, 1846, Book III, dall’introduzione a «PROPOSITIONS.» (Project Gutenberg n. 76404), estratto `fonti/motte-1846/motte-1846-L3-Regole-Fenomeni.md`. L’estratto non ha marcatori di pagina: le pagine Motte sono indicate come «sezione corrispondente». Le formule stampate come immagini (`[SVG 639]`, `[SVG 848]`, `[SVG 950]`–`[SVG 960]`) sono state lette sul LaTeX di `fonti/motte-1846/svg_tex.tsv`.
3. **Brief comune**, **addendum del Libro II** e **istruzioni del Libro III** (glossario vincolante); **Fascicoli 3, 5 e 20** (modelli di formato). Per i rimandi: **Fascicoli 1, 3, 4–6** (Definizioni, Leggi, Libro I, Sezioni I–III), **12** (Libro I, Sezione XIV), **17, 18b, 19, 20** (Libro II, Sezioni VI–IX). Per l’uso delle Regole e dei Fenomeni nel seguito: il latino dei gruppi G2 e G9 (`latino-1726-L3-P01-14.md`, `latino-1726-L3-ScholiumGenerale.md`).

Non ho consultato né riprodotto traduzioni moderne. Non ho potuto vedere la stampa del 1726 né Motte 1729.

### Criteri di traduzione

- Il testo guida è il latino; l’inglese di Motte serve a controllare le interpretazioni ed è annotato quando aggiunge, omette o si discosta.
- Si applicano il **glossario comune** del brief, il **glossario del Libro II** e il **glossario del Libro III**: *regulæ philosophandi* «regole del filosofare»; *phænomenon* «fenomeno»; *hypothesis* «ipotesi»; *systema mundi* (qui *systema mundanum*, *mundi systema*) «sistema del mondo»; *planeta primarius* «pianeta primario»; *satelles* «satellite»; *aphelium / perihelium* «afelio / perielio»; *parallaxis* non compare; *Sol, Luna, Tellus / Terra* «Sole, Luna, Terra»; *gravitas universalis* «gravità universale»; *inductio* «induzione»; *qualitates corporum* «qualità dei corpi»; *intendi & remitti* «aumentare e diminuire»; *experimentalis philosophia* «filosofia sperimentale»; *stellæ fixæ* «stelle fisse»; *maculæ* «macchie»; *quadraturæ* «quadrature»; *conjunctio* «congiunzione»; *eclipsis* «eclissi»; *longitudo* «longitudine»; *diameter apparens* «diametro apparente»; *semidiameter* «semidiametro»; *telescopium* «telescopio»; *micrometrum* «micrometro»; *annulus* «anello»; *mediocris distantia* «distanza media»; *ratio sesquiplicata* «rapporto sesquiplicato»; *tempus periodicum* «tempo periodico»; *vis insita* «forza insita»; *quamproxime* «con ottima approssimazione»; *experimentum* «esperimento»; *pes* «piede»; *minutum (primum) / secundum* «primo / secondo».
- I nomi dei pianeti e dei corpi celesti hanno la maiuscola anche dove il latino ha la minuscola (decisione del coordinatore). I simboli planetari delle tabelle (♄ ♃ ♂ ♁ ♀ ☿) sono conservati, con il nome italiano accanto.
- I nomi propri latinizzati sono resi nella forma moderna (*Borellus* Borelli, *Townleius* Townley, *Cassinus* Cassini, *Hugenius* Huygens, *Keplerus* Keplero, *Bullialdus* Boulliau), con la forma latina nell’apparato.
- Le estensioni del glossario proprie di questo fascicolo sono elencate e motivate nel § A.0.
- Gli enunciati latini all’infinito (Fenomeni) e i gerundivi (Regole) sono resi con l’indicativo e con «si devono», rispettivamente.
- I numeri misti appiattiti dalla trascrizione (*5⁤23*, *14⁤2360*, *37⁤18″*) sono scritti come 5 2/3, 14 23/60, 37 1/8″, dichiarando la lettura nel § A.7 e confrontandola con le formule SVG di Motte. Gli angoli restano in primi, secondi e terzi sessagesimali come nel testo (′, ″, ‴); i decimali conservano la virgola del testo. Nessuna formula moderna entra nel testo tradotto.

---

## Traduzione italiana

### Libro III. Il sistema del mondo

**[III.G1.01]** Nei libri precedenti ho esposto i principi della filosofia, non però filosofici ma soltanto matematici, quelli cioè sui quali si può ragionare nelle questioni filosofiche. Essi sono le leggi e le condizioni dei moti e delle forze, che riguardano soprattutto la filosofia. Tuttavia, perché non sembrassero sterili, li ho illustrati con alcuni scolii filosofici, trattando quelle cose che sono generali e sulle quali la filosofia sembra fondarsi soprattutto, come la densità e la resistenza dei corpi, gli spazi vuoti di corpi, il moto della luce e dei suoni. Resta che dagli stessi principi insegniamo la costituzione del sistema del mondo. Su questo argomento avevo composto il terzo libro con un metodo popolare, perché fosse letto da molti. Ma coloro che non abbiano compreso abbastanza i principi posti non percepiranno affatto la forza delle conseguenze, né deporranno i pregiudizi ai quali si sono abituati da molti anni; e perciò, perché la cosa non fosse trascinata in dispute, ho trasposto la sostanza di quel libro in proposizioni, alla maniera matematica, perché fossero lette soltanto da coloro che avessero prima studiato a fondo i principi. Tuttavia, poiché in quei libri s’incontrano moltissime proposizioni che potrebbero causare un indugio eccessivo anche a lettori esperti di matematica, non intendo raccomandare a nessuno di studiarle tutte: basterà che si leggano con cura le definizioni, le leggi dei moti e le prime tre sezioni del primo libro, che si passi poi a questo libro sul sistema del mondo e che si consultino a piacere le altre proposizioni dei libri precedenti qui citate.

### Regole del filosofare

### Regola I (non più cause di quante bastino)

**[III.G1.02]** **Delle cose naturali non si devono ammettere più cause di quante siano vere e sufficienti a spiegarne i fenomeni.**

**[III.G1.03]** Dicono infatti i filosofi: la natura non fa nulla invano, ed è fatto invano con più mezzi ciò che si può fare con meno. La natura, infatti, è semplice e non eccede in cause superflue delle cose.

### Regola II (effetti dello stesso genere, cause uguali)

**[III.G1.04]** **E perciò, per quanto è possibile, agli effetti naturali dello stesso genere si devono assegnare le stesse cause.**

**[III.G1.05]** Come alla respirazione nell’uomo e nella bestia; alla discesa delle pietre in Europa e in America; alla luce nel fuoco di cucina e nel Sole; alla riflessione della luce nella Terra e nei pianeti.

### Regola III (le qualità universali dei corpi)

**[III.G1.06]** **Le qualità dei corpi che non possono essere aumentate né diminuite, e che appartengono a tutti i corpi sui quali è possibile fare esperimenti, si devono considerare qualità di tutti i corpi.**

**[III.G1.07]** Le qualità dei corpi, infatti, si conoscono soltanto per mezzo degli esperimenti; e perciò si devono stabilire come generali tutte quelle che si accordano generalmente con gli esperimenti; e quelle che non possono essere diminuite non possono essere tolte. Certo non si devono inventare temerariamente sogni contro il tenore degli esperimenti, né ci si deve allontanare dall’analogia della natura, poiché essa suole essere semplice e sempre in accordo con sé stessa. L’estensione dei corpi si conosce soltanto per mezzo dei sensi, e non si percepisce in tutti; ma, poiché appartiene a tutti i corpi sensibili, la si afferma di tutti. Sperimentiamo che molti corpi sono duri. Ora, la durezza del tutto nasce dalla durezza delle parti; e di qui concludiamo a ragione che sono dure le particelle indivise non soltanto di questi corpi che si percepiscono, ma anche di tutti gli altri. Che tutti i corpi sono impenetrabili lo ricaviamo non dalla ragione ma dal senso. I corpi che maneggiamo si trovano impenetrabili, e di qui concludiamo che l’impenetrabilità è una proprietà di tutti i corpi. Che tutti i corpi sono mobili e che, per certe forze (che chiamiamo forze d’inerzia), perseverano nel moto o nella quiete, lo ricaviamo da queste proprietà dei corpi che abbiamo visto. L’estensione, la durezza, l’impenetrabilità, la mobilità e la forza d’inerzia del tutto nascono dall’estensione, dalla durezza, dall’impenetrabilità, dalla mobilità e dalle forze d’inerzia delle parti; e di qui concludiamo che tutte le parti minime di tutti i corpi sono estese, dure, impenetrabili, mobili e dotate di forze d’inerzia. E questo è il fondamento di tutta la filosofia. Inoltre, che le parti dei corpi divise e contigue l’una all’altra possano essere separate l’una dall’altra lo sappiamo dai fenomeni; e che le parti indivise possano essere distinte con la ragione in parti minori è certo per la matematica. Ma se quelle parti distinte e non ancora divise possano essere divise e separate l’una dall’altra dalle forze della natura è incerto. Se però risultasse anche da un solo esperimento che una particella indivisa, nel rompere un corpo duro e solido, subisce una divisione, concluderemmo in forza di questa regola non soltanto che le parti divise sono separabili, ma anche che le indivise possono essere divise all’infinito.

**[III.G1.08]** Infine, se per mezzo di esperimenti e di osservazioni astronomiche risulta universalmente che tutti i corpi intorno alla Terra sono gravi verso la Terra, e ciò in proporzione alla quantità di materia di ciascuno; che la Luna è grave verso la Terra in proporzione alla propria quantità di materia; che, viceversa, il nostro mare è grave verso la Luna; che tutti i pianeti sono gravi l’uno verso l’altro; e che vi è una simile gravità delle comete verso il Sole: si dovrà dire, per questa regola, che tutti i corpi gravitano l’uno verso l’altro. Infatti l’argomento tratto dai fenomeni sarà più forte per la gravità universale che per l’impenetrabilità dei corpi, della quale, nei corpi celesti, non abbiamo assolutamente alcun esperimento, nessuna osservazione. Tuttavia non affermo affatto che la gravità sia essenziale ai corpi. Per forza insita intendo soltanto la forza d’inerzia. Questa è immutabile. La gravità, allontanandosi dalla Terra, diminuisce.

### Regola IV (le proposizioni ricavate per induzione)

**[III.G1.09]** **Nella filosofia sperimentale, le proposizioni ricavate dai fenomeni per induzione, nonostante le ipotesi contrarie, si devono considerare vere, o esattamente o con ottima approssimazione, finché non si presentino altri fenomeni per mezzo dei quali o diventino più esatte o siano soggette a eccezioni.**

**[III.G1.10]** Ciò si deve fare perché l’argomento dell’induzione non venga annullato dalle ipotesi.

### Fenomeni

### Fenomeno I (i satelliti di Giove)

**[III.G1.11]** **I pianeti circumgioviali, con raggi condotti al centro di Giove, descrivono aree proporzionali ai tempi, e i loro tempi periodici, essendo in quiete le stelle fisse, sono nel rapporto sesquiplicato delle distanze dal suo centro.**

**[III.G1.12]** Risulta dalle osservazioni astronomiche. Le orbite di questi pianeti non differiscono sensibilmente da cerchi concentrici a Giove, e i loro moti su questi cerchi si trovano uniformi. Che poi i tempi periodici siano nel rapporto sesquiplicato dei semidiametri delle orbite, gli astronomi lo riconoscono concordi; e lo stesso è manifesto dalla tabella seguente.

**[III.G1.13]** *Tempi periodici dei satelliti di Giove.*

| Satellite | 1 | 2 | 3 | 4 |
|---|---|---|---|---|
| Tempo periodico | 1g 18h 27′ 34″ | 3g 13h 13′ 42″ | 7g 3h 42′ 36″ | 16g 16h 32′ 9″ |

**[III.G1.14]** *Distanze dei satelliti dal centro di Giove.*

| Dalle osservazioni | 1 | 2 | 3 | 4 | |
|---|---|---|---|---|---|
| di Borelli | 5 2/3 | 8 2/3 | 14 | 24 2/3 | semidiametri di Giove |
| di Townley, con il micrometro | 5,52 | 8,78 | 13,47 | 24,72 | |
| di Cassini, con il telescopio | 5 | 8 | 13 | 23 | |
| di Cassini, con le eclissi dei satelliti | 5 2/3 | 9 | 14 23/60 | 25 3/10 | |
| **Dai tempi periodici** | 5,667 | 9,017 | 14,384 | 25,299 | |

[Nel latino una graffa unisce le righe alla dicitura «semidiametri di Giove», che vale per tutta la tabella.]

**[III.G1.15]** Il signor Pound ha determinato con ottimi micrometri le elongazioni dei satelliti di Giove e il suo diametro, come segue. L’elongazione massima eliocentrica del quarto satellite dal centro di Giove fu presa con un micrometro in un tubo lungo quindici piedi, e risultò, alla distanza media di Giove dalla Terra, di circa 8′ 16″. Quella del terzo satellite fu presa con un micrometro in un telescopio lungo 123 piedi, e risultò, alla stessa distanza di Giove dalla Terra, di 4′ 42″. Le elongazioni massime degli altri satelliti, alla stessa distanza di Giove dalla Terra, risultano dai tempi periodici di 2′ 56″ 47‴ e di 1′ 51″ 6‴.

**[III.G1.16]** Il diametro di Giove, preso più volte con il micrometro in un telescopio lungo 123 piedi e ridotto alla distanza media di Giove dal Sole o dalla Terra, risultò sempre minore di 40″, mai minore di 38″, per lo più di 39″. Nei telescopi più corti questo diametro è di 40″ o 41″. La luce di Giove, infatti, per la disuguale rifrangibilità si dilata alquanto, e questa dilatazione ha un rapporto minore con il diametro di Giove nei telescopi più lunghi e più perfetti che in quelli più corti e meno perfetti. I tempi nei quali due satelliti, il primo e il terzo, transitavano sul corpo di Giove, dall’inizio dell’ingresso all’inizio dell’uscita e dall’ingresso completo all’uscita completa, furono osservati per mezzo dello stesso telescopio più lungo. E il diametro di Giove alla sua distanza media dalla Terra risultò, dal transito del primo satellite, di 37 1/8″, e dal transito del terzo di 37 3/8″. Fu osservato anche il tempo in cui l’ombra del primo satellite passò sul corpo di Giove, e di qui il diametro di Giove alla sua distanza media dalla Terra risultò di circa 37″. Assumiamo che il suo diametro sia di 37 1/4″ con ottima approssimazione: le elongazioni massime del primo, del secondo, del terzo e del quarto satellite saranno uguali rispettivamente a 5,965, 9,494, 15,141 e 26,63 semidiametri di Giove.

### Fenomeno II (i satelliti di Saturno)

**[III.G1.17]** **I pianeti circumsaturnii, con raggi condotti a Saturno, descrivono aree proporzionali ai tempi, e i loro tempi periodici, essendo in quiete le stelle fisse, sono nel rapporto sesquiplicato delle distanze dal suo centro.**

**[III.G1.18]** Cassini, infatti, in base alle proprie osservazioni, ha stabilito che le loro distanze dal centro di Saturno e i loro tempi periodici sono questi.

**[III.G1.19]** *Tempi periodici dei satelliti di Saturno.*

| Satellite | 1 | 2 | 3 | 4 | 5 |
|---|---|---|---|---|---|
| Tempo periodico | 1g 21h 18′ 27″ | 2g 17h 41′ 22″ | 4g 12h 25′ 12″ | 15g 22h 41′ 14″ | 79g 7h 48′ 00″ |

**[III.G1.20]** *Distanze dei satelliti dal centro di Saturno, in semidiametri dell’anello.*

| Satellite | 1 | 2 | 3 | 4 | 5 |
|---|---|---|---|---|---|
| Dalle osservazioni | 1 19/20 | 2 1/2 | 3 1/2 | 8 | 24 |
| Dai tempi periodici | 1,93 | 2,47 | 3,45 | 8 | 23,35 |

**[III.G1.21]** Dalle osservazioni si suole ricavare che l’elongazione massima del quarto satellite dal centro di Saturno è di otto semidiametri con ottima approssimazione. Ma l’elongazione massima di questo satellite dal centro di Saturno, presa con un ottimo micrometro nel telescopio di Huygens lungo 123 piedi, risultò di otto semidiametri e sette decimi di semidiametro. E da questa osservazione e dai tempi periodici, le distanze dei satelliti dal centro di Saturno, in semidiametri dell’anello, sono 2,1; 2,69; 3,75; 8,7 e 25,35. Il diametro di Saturno, nello stesso telescopio, stava al diametro dell’anello come 3 a 7, e il diametro dell’anello, nei giorni 28 e 29 maggio dell’anno 1719, risultò di 43″. E di qui il diametro dell’anello, alla distanza media di Saturno dalla Terra, è di 42″, e il diametro di Saturno di 18″. Così stanno le cose nei telescopi più lunghi e migliori, perché le grandezze apparenti dei corpi celesti hanno, nei telescopi più lunghi, una proporzione maggiore rispetto alla dilatazione della luce ai bordi di quei corpi che nei più corti. Se si scarta tutta la luce erratica, il diametro di Saturno resterà non maggiore di 16″.

### Fenomeno III (i cinque pianeti primari cingono il Sole)

**[III.G1.22]** **I cinque pianeti primari, Mercurio, Venere, Marte, Giove e Saturno, cingono il Sole con le loro orbite.**

**[III.G1.23]** Che Mercurio e Venere ruotino attorno al Sole si dimostra dalle loro fasi simili a quelle della Luna. Quando splendono a faccia piena si trovano al di là del Sole; a faccia dimezzata, di lato al Sole; falcati, al di qua del Sole, e talvolta passano sul suo disco a guisa di macchie. Anche dalla faccia piena di Marte vicino alla congiunzione con il Sole, e da quella gibbosa nelle quadrature, è certo che esso gira attorno al Sole. Di Giove e di Saturno si dimostra lo stesso dalle loro fasi sempre piene: che essi splendano di luce presa a prestito dal Sole è infatti manifesto dalle ombre dei satelliti proiettate su di essi.

### Fenomeno IV (la regola sesquiplicata per i pianeti)

**[III.G1.24]** **I tempi periodici dei cinque pianeti primari, e quello del Sole attorno alla Terra o della Terra attorno al Sole, essendo in quiete le stelle fisse, sono nel rapporto sesquiplicato delle distanze medie dal Sole.**

**[III.G1.25]** Questo rapporto, trovato da Keplero, è ammesso da tutti. I tempi periodici, infatti, sono gli stessi, e le stesse sono le dimensioni delle orbite, sia che il Sole ruoti attorno alla Terra, sia che la Terra ruoti attorno al Sole. E sulla misura dei tempi periodici c’è accordo fra tutti gli astronomi. Le grandezze delle orbite, invece, le hanno determinate dalle osservazioni Keplero e Boulliau, con la massima diligenza fra tutti; e le distanze medie che corrispondono ai tempi periodici non differiscono sensibilmente dalle distanze che essi trovarono, e per lo più stanno fra l’una e l’altra di queste; come si può vedere nella tabella seguente.

**[III.G1.26]** *Tempi periodici dei pianeti e della Terra attorno al Sole rispetto alle stelle fisse, in giorni e parti decimali di giorno.*

| ♄ Saturno | ♃ Giove | ♂ Marte | ♁ Terra | ♀ Venere | ☿ Mercurio |
|---|---|---|---|---|---|
| 10759,275 | 4332,514 | 686,9785 | 365,2565 | 224,6176 | 87,9692 |

**[III.G1.27]** *Distanze medie dei pianeti e della Terra dal Sole.*

| | ♄ Saturno | ♃ Giove | ♂ Marte | ♁ Terra | ♀ Venere | ☿ Mercurio |
|---|---|---|---|---|---|---|
| Secondo Keplero | 951000 | 519650 | 152350 | 100000 | 72400 | 38806 |
| Secondo Boulliau | 954198 | 522520 | 152350 | 100000 | 72398 | 38585 |
| Secondo i tempi periodici | 954006 | 520096 | 152369 | 100000 | 72333 | 38710 |

**[III.G1.28]** Sulle distanze di Mercurio e di Venere dal Sole non c’è luogo a discussione, poiché esse si determinano dalle loro elongazioni dal Sole. Anche sulle distanze dei pianeti superiori dal Sole ogni discussione è tolta dalle eclissi dei satelliti di Giove. Per mezzo di quelle eclissi, infatti, si determina la posizione dell’ombra che Giove proietta, e per questa via si ha la longitudine eliocentrica di Giove. Dalle longitudini eliocentrica e geocentrica confrontate fra loro si determina poi la distanza di Giove.

### Fenomeno V (le aree descritte attorno al Sole, non attorno alla Terra)

**[III.G1.29]** **I pianeti primari, con raggi condotti alla Terra, descrivono aree per nulla proporzionali ai tempi; ma con raggi condotti al Sole percorrono aree proporzionali ai tempi.**

**[III.G1.30]** Rispetto alla Terra, infatti, ora avanzano, ora sono stazionari, ora addirittura retrocedono; rispetto al Sole, invece, avanzano sempre, e con un moto quasi uniforme, tuttavia un poco più veloce nei perieli e più lento negli afeli, in modo che la descrizione delle aree sia uniforme. È una proposizione notissima agli astronomi, e in Giove si dimostra particolarmente bene per mezzo delle eclissi dei satelliti, con le quali, come abbiamo detto, si determinano le longitudini eliocentriche di questo pianeta e le sue distanze dal Sole.

### Fenomeno VI (l’area descritta dalla Luna)

**[III.G1.31]** **La Luna, con un raggio condotto al centro della Terra, descrive un’area proporzionale al tempo.**

**[III.G1.32]** Risulta dal moto apparente della Luna confrontato con il suo diametro apparente. Il moto lunare è però perturbato alquanto dalla forza del Sole; ma in questi fenomeni trascuro le minuzie insensibili degli errori.

### Proposizioni

**[III.G1.33]** *Proposizioni.* [Titolo che nel testo introduce le Proposizioni I–XLII; il seguito è nel Fascicolo 22.]

**Fine del perimetro del Fascicolo 21. Nel testo originale segue la Proposizione I, Teorema I.**

---

## Apparato

### A.0 Estensioni del glossario

I termini seguenti non comparivano nei glossari comune, del Libro II e del Libro III. Ognuno è reso in modo costante in tutto il fascicolo.

| Latino | Italiano | Motivazione |
|---|---|---|
| *principia mathematica / philosophica* | «principi matematici / filosofici» | Introduzione. Coerente con il titolo dell’opera. |
| *scholia philosophica* | «scolii filosofici» | Plurale di «scolio» come nei Fascicoli 13–20. |
| *methodus popularis* | «metodo popolare» | Calco; il senso è «in forma accessibile a molti lettori» (nota N1). Motte «a popular method». |
| *more mathematico* | «alla maniera matematica» | |
| *evolvere* (*principia, propositiones*) | «studiare a fondo», «studiare» | Letteralmente «svolgere», come si svolge un rotolo; Motte «made themselves masters of», «study». |
| *auctor esse nolo ut* | «non intendo raccomandare che» | *Auctor esse* = «farsi promotore, consigliare». |
| *vis inertiæ*, *vires inertiæ* | «forza d’inerzia», «forze d’inerzia» | Come nella Def. III del Fascicolo 1 («può essere chiamata … forza d’inerzia»). Motte lascia il latino (*vis inertiæ*, *vires inertiæ*). |
| *extensio, durities, impenetrabilitas, mobilitas* | «estensione, durezza, impenetrabilità, mobilità» | Regola III. |
| *particulæ indivisæ*; *partes minimæ* | «particelle indivise»; «parti minime» | Regola III. |
| *naturæ analogia* | «analogia della natura» | Regola III; nota N4. |
| *somnia confingere* | «inventare sogni» | Regola III. *Confingere* è un composto di *fingere*: ho scelto «inventare» perché il glossario del Libro III rende *hypotheses non fingo* «non invento ipotesi» (nota N4). |
| *tenor experimentorum* | «il tenore degli esperimenti» | Calco; Motte «the evidence of experiments». |
| *gravis esse in* | «essere grave verso» | Regola III, Fenomeni: il latino dice che un corpo «è pesante verso» un altro. «Grave verso» conserva la costruzione con *in* + accusativo, che ritorna in tutto il Libro III. |
| *gravitare in se mutuo* | «gravitare l’uno verso l’altro» | Regola III. |
| *propositiones ex phænomenis collectæ* | «proposizioni ricavate dai fenomeni» | Regola IV. *Colligere* («raccogliere, concludere») è reso «ricavare» anche in Regola III (*colligimus* «ricaviamo»). |
| *tollere* (*argumentum*) | «annullare» | Regola IV: *ne argumentum inductionis tollatur*. Motte «evaded» (nota N5). |
| *planetæ circumjoviales / circumsaturnii* | «pianeti circumgioviali / circumsaturnii» | Fenomeni I–II. Calco del latino: sono i satelliti, «pianeti secondari» nel lessico del Libro III (nota N6). |
| *stellis fixis quiescentibus* | «essendo in quiete le stelle fisse» | Ablativo assoluto: i tempi periodici sono misurati rispetto alle stelle fisse (tempi siderali; nota N6). Motte «the fixed stars being at rest». |
| *elongatio (maxima)* | «elongazione (massima)» | Distanza angolare apparente del satellite dal centro del pianeta, o del pianeta dal Sole (Fenomeno IV). |
| *heliocentricus / geocentricus* | «eliocentrico / geocentrico» | Fenomeni I, IV, V. |
| *tubus* | «tubo» | Fenomeno I, *in tubo quindecim pedes longo*: il cannocchiale; distinto da *telescopium* «telescopio», che compare nella frase seguente. |
| *telescopium Hugenianum* | «telescopio di Huygens» | Fenomeno II. |
| *refrangibilitas* (*inæqualis*) | «rifrangibilità (disuguale)» | Fenomeno I; come nel Fascicolo 12 (Libro I, Sezione XIV, «diversa rifrangibilità»). |
| *lux erratica* | «luce erratica» | Fenomeno II: la luce diffusa attorno all’immagine; Motte «spurious light». |
| *transitus; ingressus; exitus* | «transito; ingresso; uscita» | Fenomeno I. |
| *tertia* (‴) | «terzi» | Fenomeno I: sessantesimi di secondo d’arco (nota N7). |
| *phases; plena facies; dimidiata; falcata; gibbosa* | «fasi; faccia piena; dimezzata; falcata; gibbosa» | Fenomeno III. |
| *e regione solis* | «di lato al Sole» | Fenomeno III. *E regione* indica la posizione «in direzione di, di fronte a»: qui il pianeta a fase dimezzata, alla massima elongazione, cioè di lato al Sole rispetto all’osservatore. Motte «about the same height on one side or other of the sun». **Dubbio segnalato** (nota N9). |
| *ultra / cis solem* | «al di là / al di qua del Sole» | Fenomeno III. |
| *progredi; stationarius esse; regredi* | «avanzare; essere stazionario; retrocedere» | Fenomeno V; Motte «direct, stationary, retrograde». |
| *planetæ superiores* | «pianeti superiori» | Fenomeno IV: quelli esterni all’orbita della Terra. |
| *in confesso est apud omnes* | «è ammesso da tutti» | Fenomeno IV. |
| *arearum æquabilis descriptio* | «descrizione uniforme delle aree» | Fenomeno V. |
| *errorum insensibiles minutiæ* | «minuzie insensibili degli errori» | Fenomeno VI. |
| *D.* (*Dominus*) | «il signor» | Fenomeno I, *D. Pound*; come «il signor Sauveur» nel Fascicolo 19. |
| *Semidiam. Jovis* (graffa della tabella) | «semidiametri di Giove» | Fenomeno I. |

**Dubbi sui termini fissati dal coordinatore.** Nessuno. Osservo soltanto che nella Regola III il glossario fissa *intendi & remitti* «aumentare e diminuire»; in italiano la negazione richiede «non possono essere aumentate **né** diminuite»: la coppia di verbi del glossario è conservata.

### A.1 Titolo e introduzione del Libro III

**Latino (titolo):** *DE MUNDI SYSTEMATE. LIBER TERTIUS.* — **Motte:** «BOOK III.» (ripetuto due volte nell’estratto; il sottotitolo *De mundi systemate* manca).

**Scelte.**

- *De mundi systemate* è reso «Il sistema del mondo», secondo il glossario; *constitutionem systematis mundani* «la costituzione del sistema del mondo» (Motte «the frame of the System of the World»).
- *principia philosophiæ … non tamen philosophica sed mathematica tantum*: «i principi della filosofia, non però filosofici ma soltanto matematici». È il titolo stesso dell’opera, *Philosophiæ naturalis principia mathematica*, spiegato dall’autore.
- *ex quibus videlicet in rebus philosophicis disputari possit*: «quelli cioè sui quali si può ragionare nelle questioni filosofiche». Motte «such … as we may build our reasonings upon».
- *ne sterilia videantur*: «perché non sembrassero sterili». Motte amplia: «lest they should have appeared of themselves dry and barren».
- *uti corporum densitatem & resistentiam, spatia corporibus vacua, motumque Lucis & sonorum*: è un rimando agli scolii dei Libri I e II (§ A.13). Motte «spaces void of all bodies»: «all» è un’aggiunta.
- *percipient … deponent* (futuri) sono resi con il futuro, «non percepiranno … né deporranno»; Motte volge al passato («could not easily discern»), legandoli alla decisione presa allora. Motte attenua anche *minime* («affatto») in «not easily».
- *quibus a multis retro annis insueverunt*: «ai quali si sono abituati da molti anni».
- *ne res in disputationes trahatur*: «perché la cosa non fosse trascinata in dispute». Motte «to prevent the disputes which might be raised upon such accounts».
- *quoniam propositiones ibi quam plurimæ occurrant*: *ibi* sono i libri precedenti (lo intende così anche Motte: «those Books»), reso esplicitamente «in quei libri».
- *mathematice doctis*: «esperti di matematica»; Motte «of good mathematical learning».
- *reliquas librorum priorum propositiones hic citatas pro lubitu consulat*: «si consultino a piacere le altre proposizioni dei libri precedenti qui citate». Motte «as the references in this, and his occasions, shall require»: parafrasi corretta nel senso.

### A.2 Regola I

**Latino:** *Causas rerum naturalium non plures admitti debere, quam quæ & veræ sint & earum phænomenis explicandis sufficiant.*

**Inglese:** “We are to admit no more causes of natural things than such as are both true and sufficient to explain their appearances.”

**Scelte.**

- L’infinito *admitti debere* dipende da un «si stabilisce» sottinteso, come negli enunciati delle leggi: reso con «non si devono ammettere».
- *& veræ sint & … sufficiant*: le due condizioni sono congiunte («vere e sufficienti»). La regola non dice soltanto «il minimo numero di cause», ma il minimo numero di cause **vere**: è il punto su cui torna lo Scolio generale (nota N2).
- *earum phænomenis*: *earum* si riferisce a *rerum naturalium*, «i fenomeni delle cose naturali», reso «spiegarne i fenomeni». Motte «their appearances»: Motte rende *phænomena* con «appearances» qui e nel titolo («Phænomena, or Appearances»), ma lascia «phænomena» nella Regola IV.
- *Dicunt utique philosophi*: *utique* conferma («infatti»). Motte «To this purpose».
- *frustra fit per plura quod fieri potest per pauciora*: «è fatto invano con più mezzi ciò che si può fare con meno». Motte «more is in vain when less will serve».
- *rerum causis superfluis non luxuriat*: «non eccede in cause superflue delle cose». *Luxuriare* è «essere rigoglioso, sovrabbondare». Motte «affects not the pomp of superfluous causes»: immagine aggiunta («pomp»).

### A.3 Regola II

**Latino:** *Ideoque effectuum naturalium ejusdem generis eædem assignandæ sunt causæ, quatenus fieri potest.*

**Inglese:** “Therefore to the same natural effects we must, as far as possible, assign the same causes.”

**Scelte.**

- *Ideoque*: «e perciò». La Regola II è presentata come conseguenza della Regola I.
- **Divergenza di Motte:** *effectuum naturalium ejusdem generis* («effetti naturali **dello stesso genere**») diventa «the same natural effects». Il latino parla di effetti dello stesso tipo osservati in luoghi o corpi diversi (la luce del fuoco e del Sole), non di effetti identici. È la distinzione su cui si regge l’uso della regola nelle Propp. IV e V (Prop. V: *phænomena ejusdem generis*, «fenomeni dello stesso genere»). Errore di senso di Motte.
- *quatenus fieri potest*: «per quanto è possibile».
- Gli esempi sono dativi retti da *assignandæ* (*Uti respirationis … descensus … lucis … reflexionis*, genitivi di *causæ*): resi «come alla respirazione …», cioè «come si assegnano le stesse cause alla respirazione …».
- *lucis in igne culinari & in sole*: «alla luce nel fuoco di cucina e nel Sole». Motte «of our culinary fire» aggiunge «our».

### A.4 Regola III

**Latino:** *Qualitates corporum quæ intendi & remitti nequeunt, quæque corporibus omnibus competunt in quibus experimenta instituere licet, pro qualitatibus corporum universorum habendæ sunt.*

**Inglese:** “The qualities of bodies, which admit neither intension nor remission of degrees, and which are found to belong to all bodies within the reach of our experiments, are to be esteemed the universal qualities of all bodies whatsoever.”

**Scelte.**

- *intendi & remitti nequeunt*: «non possono essere aumentate né diminuite» (glossario). È il lessico scolastico della *intensio* e *remissio* delle qualità (nota N3). Motte aggiunge «of degrees», che è un’interpretazione corretta.
- *competunt*: «appartengono». Motte «are found to belong»: «are found» è un’aggiunta.
- *in quibus experimenta instituere licet*: «sui quali è possibile fare esperimenti». Motte «within the reach of our experiments».
- *pro qualitatibus corporum universorum habendæ sunt*: «si devono considerare qualità di tutti i corpi». *Universorum* = «tutti, presi insieme». Motte raddoppia: «the universal qualities of all bodies whatsoever».
- *generales statuendæ sunt quotquot cum experimentis generaliter quadrant*: «si devono stabilire come generali tutte quelle che si accordano generalmente con gli esperimenti». Il gioco *generales … generaliter* è conservato.
- *quæ minui non possunt, non possunt auferri*: «quelle che non possono essere diminuite non possono essere tolte». Motte «can never be quite taken away»: «quite» indebolisce l’argomento.
- *Certe contra experimentorum tenorem somnia temere confingenda non sunt*: «Certo non si devono inventare temerariamente sogni contro il tenore degli esperimenti». Motte «We are certainly not to relinquish the evidence of experiments for the sake of dreams and vain fictions of our own devising»: parafrasi ampia; «vain fictions of our own devising» rende *confingere*, ma *temere* («temerariamente») non è reso.
- *nec in omnibus sentitur*: «e non si percepisce in tutti». Motte «nor do these reach it in all bodies».
- *sed quia sensibilibus omnibus competit, de universis affirmatur*: «ma, poiché appartiene a tutti i corpi sensibili, la si afferma di tutti». Motte «we ascribe it universally to all others also».
- *Corpora plura dura esse experimur*: «Sperimentiamo che molti corpi sono duri». *Plura* = «parecchi, molti» (non «più»); Motte «That abundance of bodies are hard».
- *non horum tantum corporum quæ sentiuntur*: «non soltanto di questi corpi che si percepiscono»; Motte «the bodies we feel».
- *non ratione sed sensu colligimus*: «lo ricaviamo non dalla ragione ma dal senso».
- *Quæ tractamus*: «I corpi che maneggiamo». *Tractare* qui ha il senso fisico di «toccare, maneggiare»; Motte «which we handle».
- *viribus quibusdam (quas vires inertiæ vocamus)*: «per certe forze (che chiamiamo forze d’inerzia)». Motte lascia il latino.
- *ex hisce corporum visorum proprietatibus colligimus*: «lo ricaviamo da queste proprietà dei corpi che abbiamo visto». Motte «we only infer from the like properties observed in the bodies which we have seen»: «only» è un’aggiunta.
- *Et hoc est fundamentum philosophiæ totius*: «E questo è il fondamento di tutta la filosofia».
- *ratione distingui posse ex mathematica certum est*: «possano essere distinte con la ragione … è certo per la matematica». Motte «our minds are able to distinguish … as is mathematically demonstrated».
- *incertum est*: «è incerto»; Motte «we cannot certainly determine».
- *frangendo corpus durum & solidum*: «nel rompere un corpo duro e solido».
- **Divergenza di Motte.** Il latino conclude: *quod non solum partes divisæ separabiles essent, sed etiam quod indivisæ in infinitum dividi possent* («non soltanto che le parti divise sono separabili, ma anche che le indivise possono essere divise all’infinito»). Motte fonde le due affermazioni: «that the undivided as well as the divided particles may be divided and actually separated to infinity». Il latino distingue la separabilità (delle parti già divise) dalla divisibilità all’infinito (delle indivise); Motte attribuisce a entrambe la separazione all’infinito e aggiunge «actually».
- **Secondo capoverso.** *corpora omnia in circuitu terræ gravia esse in terram*: «tutti i corpi intorno alla Terra sono gravi verso la Terra» (A.0). *idque pro quantitate materiæ in singulis*: «e ciò in proporzione alla quantità di materia di ciascuno». *in se motuo* è un refuso della trascrizione per *in se mutuo* (§ A.12).
- *dicendum erit per hanc regulam quod corpora omnia in se mutuo gravitant*: «si dovrà dire, per questa regola, che tutti i corpi gravitano l’uno verso l’altro». **Aggiunta di Motte:** «are endowed with a principle of mutual gravitation». Il latino non parla di un «principio» di cui i corpi sono dotati: dice soltanto che gravitano. La differenza conta, perché tre frasi dopo Newton nega che la gravità sia essenziale ai corpi (nota N3).
- *Nam & fortius erit argumentum ex phænomenis de gravitate universali, quam de corporum impenetrabilitate*: «l’argomento tratto dai fenomeni sarà più forte per la gravità universale che per l’impenetrabilità dei corpi». Motte «concludes with more force for the universal gravitation of all bodies».
- *nullum experimentum, nullam prorsus observationem*: «non abbiamo assolutamente alcun esperimento, nessuna osservazione». Motte «no experiments, nor any manner of observation».
- *Attamen gravitatem corporibus essentialem esse minime affirmo*: «Tuttavia non affermo affatto che la gravità sia essenziale ai corpi».
- *Per vim insitam intelligo solam vim inertiæ*: «Per forza insita intendo soltanto la forza d’inerzia». Rimando implicito alla Def. III (§ A.13). Motte lascia il latino («by their vis insita I mean nothing but their vis inertiæ») e aggiunge «their».
- *Gravitas recedendo a terra, diminuitur*: «La gravità, allontanandosi dalla Terra, diminuisce». Il gerundio ha per soggetto logico il corpo che si allontana; l’italiano lo lascia implicito come il latino. Motte «Their gravity is diminished as they recede from the earth».

### A.5 Regola IV

**Latino:** *In philosophia experimentali, propositiones ex phænomenis per inductionem collectæ, non obstantibus contrariis hypothesibus, pro veris aut accurate aut quamproxime haberi debent, donec alia ocurrerint phænomena, per quæ aut accuratiores reddantur aut exceptionibus obnoxiæ.*

**Inglese:** “In experimental philosophy we are to look upon propositions collected by general induction from phænomena as accurately or very nearly true, notwithstanding any contrary hypotheses that may be imagined, till such time as other phænomena occur, by which they may either be made more accurate, or liable to exceptions.”

**Scelte.**

- *In philosophia experimentali*: «Nella filosofia sperimentale» (glossario).
- *per inductionem*: «per induzione» (glossario). **Aggiunta di Motte:** «by **general** induction». Il latino non qualifica l’induzione (nota N5).
- *non obstantibus contrariis hypothesibus*: «nonostante le ipotesi contrarie». **Aggiunta di Motte:** «that may be imagined». L’aggiunta è nello spirito dello Scolio generale (*hypotheses non fingo*), ma non è nel testo.
- *pro veris aut accurate aut quamproxime haberi debent*: «si devono considerare vere, o esattamente o con ottima approssimazione».
- *donec alia ocurrerint phænomena*: «finché non si presentino altri fenomeni». *ocurrerint* è un refuso della trascrizione per *occurrerint* (§ A.12).
- *per quæ aut accuratiores reddantur aut exceptionibus obnoxiæ*: «per mezzo dei quali o diventino più esatte o siano soggette a eccezioni».
- *Hoc fieri debet ne argumentum inductionis tollatur per hypotheses*: «Ciò si deve fare perché l’argomento dell’induzione non venga annullato dalle ipotesi». *Tollere* è «togliere di mezzo, eliminare». Motte «that the argument of induction may not be evaded by hypotheses»: «evaded» (eluso, aggirato) è più debole e sposta il senso dall’argomento demolito all’argomento schivato (nota N5).

### A.6 Fenomeno I

**Latino:** *Planetas circumjoviales, radiis ad centrum jovis ductis, areas describere temporibus proportionales, eorumque tempora periodica, stellis fixis quiescentibus, esse in ratione sesquiplicata distantiarum ab ipsius centro.*

**Inglese:** “That the circumjovial planets, by radii drawn to Jupiter's centre, describe areas proportional to the times of description; and that their periodic times, the fixed stars being at rest, are in the sesquiplicate proportion of their distances from its centre.”

**Scelte.**

- Accusativo e infinito reso con l’indicativo. *Planetas circumjoviales*: «pianeti circumgioviali» (A.0). Nel testo dello stesso Fenomeno si passa a *satellites*: «satelliti» (glossario).
- *Constat ex observationibus astronomicis*: «Risulta dalle osservazioni astronomiche».
- *consentiunt astronomi*: «gli astronomi lo riconoscono concordi». Motte «all astronomers agree»: «all» è un’aggiunta.
- **Tabella dei tempi periodici.** Ricostruita in una riga. Motte ha le stesse cifre, con qualche punto mancante («13'  42''»).
- **Tabella delle distanze.** Il latino ha cinque colonne di righe (intestazione «Ex observationibus 1 2 3 4», poi Borelli, Townley, Cassini al telescopio, Cassini con le eclissi, «Ex temporibus periodicis») e una graffa «} Semidiam. Jovis» dopo la riga di Borelli. Nella stampa la graffa abbraccia probabilmente tutte le righe (§ A.12). Motte rende la graffa con una formula (`[SVG 952]`, una parentesi con «semi-diameter of Jupiter») nella riga di Borelli, che ha perciò una cella in più. *Townlei per microm.* «di Townley, con il micrometro»; *Cassini per telescop.* «di Cassini, con il telescopio»; *per eclips. satell.* «con le eclissi dei satelliti».
- **Pound.** *Elongationes satellitum jovis & diametrum ejus*: «le elongazioni dei satelliti di Giove e il suo diametro». Motte inverte e pluralizza: «the diameters of Jupiter and the elongation of its satellites».
- *Elongatio maxima heliocentrica*: «elongazione massima eliocentrica»: l’elongazione come apparirebbe dal Sole, cioè ridotta alla distanza media (nota N7).
- *in tubo quindecim pedes longo*: «in un tubo lungo quindici piedi»; Motte «in a 15 feet telescope».
- *capita fuit* (refuso per *capta fuit*) e *satellitium* (per *satellitum*): § A.12.
- *Diameter jovis … ad mediocrem jovis a sole vel terra distantiam reducta*: «ridotto alla distanza media di Giove dal Sole o dalla Terra». Motte «reduced to Jupiter’s mean distance from the earth»: omette «dal Sole o».
- *sæpius capta … sæpius 39″*: il primo *sæpius* è «più volte», il secondo «per lo più».
- *per inæqualem refrangibilitatem*: «per la disuguale rifrangibilità». Motte aggiunge «of the rays».
- *ab initio ingressus ad initium exitus, & ab ingressu completo ad exitum completum*: «dall’inizio dell’ingresso all’inizio dell’uscita e dall’ingresso completo all’uscita completa».
- *37⁤18″*, *37⁤38″*, *37⁤14″*: letti 37 1/8″, 37 3/8″, 37 1/4″ (Motte `[SVG 955]`–`[SVG 957]`, concordi).
- *Assumamus diametrum ejus esse 37⁤14″ quamproxime; & elongationes … æquales erunt*: «Assumiamo che il suo diametro sia di 37 1/4″ con ottima approssimazione: le elongazioni … saranno uguali». La *&* consecutiva è resa con i due punti.

### A.7 Fenomeno II

**Latino:** *Planetas circumsaturnios, radiis ad saturnum ductis, areas describere temporibus proportionales, & eorum tempora periodica, stellis fixis quiescentibus, esse in ratione sesquiplicata distantiarum ab ipsius centro.*

**Inglese:** “That the circumsaturnal planets, by radii drawn to Saturn's centre, describe areas proportional to the times of description; and that their periodic times, the fixed stars being at rest, are in the sesquiplicate proportion of their distances from its centre.”

**Scelte.**

- *radiis ad saturnum ductis*: «con raggi condotti a Saturno». Il latino dice «a Saturno», non «al centro di Saturno» come nel Fenomeno I; Motte uniforma («to Saturn’s centre»). Divergenza minima, segnalata.
- *Cassinus utique … statuit*: «Cassini, infatti, … ha stabilito». *Utique* introduce la prova: Motte «For, as Cassini …».
- **Tabelle.** Nella trascrizione i cinque tempi periodici sono su una riga; in Motte il quinto è staccato dagli altri. La tabella delle distanze ha due righe («Ex observationibus»; «Ex temporibus periodicis»): *1⁤1920.*, *2⁤12.*, *3⁤12.* sono 1 19/20, 2 1/2, 3 1/2 (Motte `[SVG 958]`, `[SVG 959]`, `[SVG 639]`, concordi).
- *semidiametrorum acto quamproxime*: *acto* è un refuso per *octo* (§ A.12); Motte «eight of these semi-diameters very nearly».
- *ex observationibus colligi solet*: «dalle osservazioni si suole ricavare».
- *semidiametrorum octo cum septem decimis partibus semidiametri*: «otto semidiametri e sette decimi di semidiametro» (Motte `[SVG 960]` = 7/10, concorde).
- *diebus Maii 28 & 29 anni 1719.*: «nei giorni 28 e 29 maggio dell’anno 1719». La data resta come nel testo; il latino non dice qui *st. vet.* (nota N8).
- *in terminis illorum corporum*: «ai bordi di quei corpi»; Motte «in the extremities of those bodies».
- *Si rejiciatur lux omnis erratica*: «Se si scarta tutta la luce erratica». Motte «If we, then, reject all the spurious light»: «then» è un’aggiunta.
- *haud major quam 16″*: «non maggiore di 16″»; Motte «will not amount to more than 16''».

### A.8 Fenomeno III

**Latino:** *Planetas quinque primarios mercurium, venerem, martem, jovem & saturnum orbibus suis solem cingere.*

**Inglese:** “That the five primary planets, Mercury, Venus, Mars, Jupiter, and Saturn, with their several orbits, encompass the sun.”

**Scelte.**

- *Planetas … primarios*: «pianeti primari» (glossario; nota N6 per «secondario»).
- *ex eorum phasibus lunaribus*: «dalle loro fasi simili a quelle della Luna». Motte «moon-like appearances».
- **Ampliamento di Motte.** Il latino è lapidario: *Plena facie lucentes ultra solem siti sunt; dimidiata e regione solis; falcata cis solem*. Motte spiega: «they are, in respect of us, beyond or above the sun; … they are about the same height on one side or other of the sun; when horned, they are below or between us and the sun». Aggiunte: «in respect of us», «or above», «about the same height on one side or other», «below or between us and». La traduzione segue il latino.
- *per discum ejus ad modum macularum nonnunquam transeuntes*: «e talvolta passano sul suo disco a guisa di macchie». Motte aggiunge «when directly under».
- *Ex martis quoque plena facie prope solis conjunctionem, & gibbosa in quadraturis*: «dalla faccia piena di Marte vicino alla congiunzione con il Sole, e da quella gibbosa nelle quadrature». Motte «is as plain»: *certum est* «è certo».
- *De jove etiam & saturno idem ex eorum phasibus semper plenis demonstratur*: «Di Giove e di Saturno si dimostra lo stesso dalle loro fasi sempre piene». Motte «from their appearing full in all situations».
- *ex umbris satellitum in ipsos projectis*: «dalle ombre dei satelliti proiettate su di essi». Motte aggiunge «that appear sometimes upon their disks» e la contrapposizione «not their own, but borrowed».

### A.9 Fenomeno IV

**Latino:** *Planetarum quinque primariorum, & vel solis circa terram vel terræ circa solem tempora periodica, stellis fixis quiescentibus, esse in ratione sesquiplicata mediocrium distantiarum a sole.*

**Inglese:** “That the fixed stars being at rest, the periodic times of the five primary planets, and (whether of the sun about the earth, or) of the earth about the sun, are in the sesquiplicate proportion of their mean distances from the sun.”

**Scelte.**

- *vel solis circa terram vel terræ circa solem*: «quello del Sole attorno alla Terra o della Terra attorno al Sole». Motte mette fra parentesi l’alternativa geocentrica («(whether of the sun about the earth, or)»), che il latino pone sullo stesso piano. Divergenza di presentazione: il latino resta neutrale fino alla Prop. XII (nota N10).
- *mediocrium distantiarum*: «distanze medie» (glossario).
- *Hæc a Keplero inventa ratio in confesso est apud omnes*: «Questo rapporto, trovato da Keplero, è ammesso da tutti». Motte «first observed by Kepler, is now received by all astronomers»: «first», «now» e «astronomers» sono aggiunte.
- *Eadem utique sunt tempora periodica*: «I tempi periodici, infatti, sono gli stessi». *Utique* motiva perché la regola valga in entrambi i sistemi.
- *Magnitudines autem orbium Keplerus & Bullialdus omnium diligentissime ex observationibus determinaverunt*: «Le grandezze delle orbite, invece, le hanno determinate dalle osservazioni Keplero e Boulliau, con la massima diligenza fra tutti». *Bullialdus* è Ismaël Boulliau (non verificato sulle fonti allegate); Motte lascia «Bullialdus».
- *suntque inter ipsas ut plurimum intermediæ*: «e per lo più stanno fra l’una e l’altra di queste»; verificato nella nota N10. Motte «for the most part fall in between them».
- **Tabelle.** Latino: due tabelle, con le colonne dei pianeti (♄ ♃ ♂ ♁ ♀ ☿). Motte divide la tabella delle distanze in due metà (♄ ♃ ♂; ♁ ♀ ☿) e usa le virgolette di ripetizione («"      to Bullialdus»). Cifre identiche al latino in tutte le celle. Motte: «87,9692.» con un punto finale, come il latino.
- *Planetarum ac telluris tempora periodica circa solem respectu fixarum*: «Tempi periodici dei pianeti e della Terra attorno al Sole rispetto alle stelle fisse». *Tellus* «Terra» (glossario).
- *De distantiis mercurii & veneris a sole disputandi non est locus*: «non c’è luogo a discussione». Motte «there can be no doubt».
- *tollitur omnis disputatio*: «ogni discussione è tolta»; Motte «all dispute is cut off».
- *eo nomine*: «per questa via»; Motte «whence».

### A.10 Fenomeno V

**Latino:** *Planetas primarios, radiis ad terram ductis, areas describere temporibus minime proportionales; at radiis ad solem ductis, areas temporibus proportionales percurrere.*

**Inglese:** “Then the primary planets, by radii drawn to the earth, describe areas no wise proportional to the times; but that the areas which they describe by radii drawn to the sun are proportional to the times of description.”

**Scelte.**

- *minime proportionales*: «per nulla proporzionali».
- **Errore di Motte 1846:** l’enunciato comincia con «**Then** the primary planets», mentre tutti gli altri Fenomeni cominciano con «That» e la seconda metà dello stesso enunciato ha «but **that**». «Then» è un refuso per «That» (dell’edizione 1846 o della trascrizione Gutenberg; non verificato su Motte 1729).
- *areas … percurrere*: «percorrono aree». Motte rende con una costruzione passiva («the areas which they describe … are proportional»).
- *nunc progrediuntur, nunc stationarii sunt, nunc etiam regrediuntur*: «ora avanzano, ora sono stazionari, ora addirittura retrocedono». Motte «direct … stationary … retrograde».
- *idque propemodum uniformi cum motu, sed paulo celerius tamen in periheliis ac tardius in apheliis*: «e con un moto quasi uniforme, tuttavia un poco più veloce nei perieli e più lento negli afeli».
- *sic ut arearum æquabilis sit descriptio*: «in modo che la descrizione delle aree sia uniforme».
- *Propositio est astronomis notissima*: «È una proposizione notissima agli astronomi». Motte «This a noted proposition»: manca il verbo («is»), refuso dell’edizione 1846 o della trascrizione.
- *in jove apprime demonstratur*: «in Giove si dimostra particolarmente bene».
- *quibus eclipsibus … determinari diximus*: «con le quali, come abbiamo detto, si determinano»: rimando interno al Fenomeno IV (§ A.13).

### A.11 Fenomeno VI

**Latino:** *Lunam radio ad centrum terræ ducto, aream tempori proportionalem describere.*

**Inglese:** “That the moon, by a radius drawn to the earth's centre, describes an area proportional to the time of description.”

**Scelte.**

- *Patet ex lunæ motu apparente cum ipsius diametro apparente collato*: «Risulta dal moto apparente della Luna confrontato con il suo diametro apparente» (nota N11).
- *Perturbatur autem motus lunaris aliquantulum a vi solis*: «Il moto lunare è però perturbato alquanto dalla forza del Sole». Il glossario fissa «forza del Sole che perturba i moti della Luna» per *vis solis ad perturbandos motus lunæ*; qui la forma è verbale e la resa segue il latino. Motte «by the action of the sun»: *vis* diventa «action».
- *errorum insensibiles minutias in hisce phænomenis negligo*: «in questi fenomeni trascuro le minuzie insensibili degli errori». Motte «in laying down these Phænomena I neglect those small and inconsiderable errors».
- **Titolo finale.** *PROPOSITIONES.* «Proposizioni.» (Motte «PROPOSITIONS.»).

### A.12 Refusi e anomalie della trascrizione

| Luogo | Trascrizione | Lettura | Tipo |
|---|---|---|---|
| III.G1.03 | *DIcunt* | *Dicunt* | capolettera tipografico, non refuso |
| III.G1.07 | *ge ‹388› neraliter* | *generaliter* | parola spezzata dal cambio di pagina; nessuna perdita |
| III.G1.08 | *in se motuo* | *in se mutuo* | refuso probabile della trascrizione (tre righe dopo: *in se mutuo gravitant*) |
| III.G1.09 | *ocurrerint* | *occurrerint* | refuso probabile |
| III.G1.12 | *COnstat* | *Constat* | capolettera tipografico |
| III.G1.14 | *5⁤23*, *8⁤23*, *24⁤23*, *14⁤2360*, *25⁤310* | 5 2/3, 8 2/3, 24 2/3, 14 23/60, 25 3/10 | numeri misti appiattiti (con il carattere invisibile U+2064 fra intero e frazione); confermati dagli SVG 950, 848, 951, 953, 954 di Motte |
| III.G1.14 | «}» dopo la riga di Borelli, poi *Semidiam. Jovis* | graffa che abbraccia le righe | la posizione nella trascrizione non dice quali righe abbracci |
| III.G1.15 | *capita fuit* | *capta fuit* | refuso probabile (cfr. *capta fuit* nella frase precedente) |
| III.G1.15 | *satellitium* | *satellitum* | refuso probabile |
| III.G1.16 | *37⁤18″*, *37⁤38″*, *37⁤14″* | 37 1/8″, 37 3/8″, 37 1/4″ | numeri misti appiattiti; confermati dagli SVG 955–957 |
| III.G1.20 | *1⁤1920.*, *2⁤12.*, *3⁤12.* | 1 19/20, 2 1/2, 3 1/2 | numeri misti appiattiti; confermati dagli SVG 958, 959, 639 |
| III.G1.21 | *semidiametrorum acto* | *octo* | refuso probabile (Motte «eight») |

La traduzione segue il senso; la Parte B riporta il latino esatto della trascrizione.

**Punti da controllare sulla stampa ECCO.**

| Pagina 1726 | Trascrizione | Lettura attesa | Motivo |
|---|---|---|---|
| p. 388 | *in se motuo* | *in se mutuo* | forma inesistente; poco dopo *in se mutuo* |
| p. 389 | *ocurrerint* | *occurrerint* | consonante semplice anomala |
| p. 390 | graffa «}» e *Semidiam. Jovis* | graffa su tutte le cinque righe di valori | la trascrizione la colloca dopo la riga di Borelli; Motte la mette solo in quella riga |
| p. 390 | *14⁤2360* | 14 23/60 | frazione insolita (sessagesimale); Motte concorda, ma va confermata sulla stampa |
| p. 391 | *capita fuit* | *capta fuit* | refuso |
| p. 391 | *satellitium* | *satellitum* | refuso |
| p. 391 | *9,494* (elongazione del secondo satellite) | 9,492? | il calcolo dà 9,4917 (nota N7); verificare se la stampa ha 9,494 o 9,492 |
| p. 391 | *acto* | *octo* | refuso |
| p. 392 | *23,35* (quinto satellite «ex temporibus periodicis») | 23,31? | il calcolo dà 23,31; con 8,7 la stessa regola dà 25,35, come il testo (nota N8) |
| p. 393 | *224,6176* (tempo periodico di Venere) | 224,6998? | la distanza 72333 della stessa tabella corrisponde a 224,700 giorni (nota N10); Motte ha anch’egli 224,6176 |
| p. 393 | *954006* (distanza di Saturno «secondo i tempi periodici») | 953799? | il calcolo dal tempo periodico 10759,275 dà 953799 (nota N10) |

### A.13 Rimandi

**Rimandi ai Libri I e II (verificati sui fascicoli del progetto).**

| Luogo | Latino | Resa | Verifica |
|---|---|---|---|
| III.G1.01 | *definitiones, leges motuum & sectiones tres priores libri primi* | «le definizioni, le leggi dei moti e le prime tre sezioni del primo libro» | Torna: Fascicolo 1 (Definizioni I–VIII), Fascicolo 3 (Leggi e Corollari), Fascicoli 4–6 (Sezioni I–III: rapporti primi e ultimi; forze centripete, con la legge delle aree, Prop. I, e il Cor. 6 della Prop. IV, S2.29; moto nelle sezioni coniche, con la Prop. XV sui tempi periodici). Sono proprio i risultati usati dalle Propp. I–II del Libro III. |
| III.G1.01 | *scholiis quibusdam philosophicis … corporum densitatem & resistentiam* | «alcuni scolii filosofici … la densità e la resistenza dei corpi» | Torna: Libro II, Sezione V (densità e compressione, scolii, Fascicolo 16) e Sezioni VI–VII (resistenza dei mezzi, Fascicoli 17, 18a, 18b). |
| III.G1.01 | *spatia corporibus vacua* | «gli spazi vuoti di corpi» | Torna: Libro II, Scolio generale della Sezione VI («da questi esperimenti dipende la dimostrazione del vuoto», II.S6.57, Fascicolo 17) e Sezione VII, Scolio dopo la Prop. XL (gli spazi celesti privi di fluido corporeo, II.S7.129, Fascicolo 18b). |
| III.G1.01 | *motumque Lucis & sonorum* | «il moto della luce e dei suoni» | Torna: Libro I, Sezione XIV, Scolii (analogia con la luce, Fascicolo 12); Libro II, Sezione VIII, Scolio sulla velocità del suono (Fascicolo 19). |
| III.G1.08 | *Per vim insitam intelligo solam vim inertiæ* | «Per forza insita intendo soltanto la forza d’inerzia» | Torna: Def. III (Fascicolo 1): la forza insita «non differisce affatto dall’inerzia della massa … può essere chiamata … forza d’inerzia». Rimando implicito, non citato da Newton. |

Nessun rimando ai Libri I e II che non torni. Il Fascicolo 20 (§ A.8, II.S9.27) aveva lasciato in sospeso la regola sesquiplicata per i satelliti di Giove e per i pianeti, «i dati sono nei Fenomeni del Libro III»: il rimando è ora confermato dai Fenomeni I e IV di questo fascicolo.

**Rimandi interni al Libro III.**

- *quibus eclipsibus heliocentricas planetæ hujus longitudines & distantias a sole determinari diximus* (Fenomeno V) → Fenomeno IV, III.G1.28: torna.
- *ad hunc librum de mundi systemate* (introduzione): rimando al libro stesso.

**Uso delle Regole e dei Fenomeni nel seguito (controllato sul latino del gruppo G2, Fascicolo 22).** La Prop. I cita *per phænomenon primum* e, per Saturno, *per phænomenon secundum*; la Prop. II *per phænomenon quintum* (con la Prop. II del Libro I) per la prima parte e *per phænomenon quartum* (con la Prop. IV del Libro I) per la seconda; la Prop. IV *per reg. i. & ii.* (due volte); la Prop. V *per reg. ii.* (*phænomena ejusdem generis*); la Prop. VI *per reg. iii.* (*Hæc est qualitas omnium in quibus experimenta instituere licet*, che riprende alla lettera l’enunciato della Regola III). L’uso è coerente con gli enunciati tradotti qui. Lo Scolio generale (gruppo G9) riprende la Regola IV: *In hac philosophia propositiones deducuntur ex phænomenis, & redduntur generales per inductionem* (nota N5).

### A.14 Formule SVG di Motte

Ho controllato sul LaTeX di `svg_tex.tsv` tutte le **13 occorrenze** di formule SVG dell’estratto (12 numeri distinti: 639, 848, 950–960; il 950 compare due volte). Corrispondono tutte al latino:

| SVG | LaTeX | Latino |
|---|---|---|
| 950 (×2) | `5\tfrac{2}{3}` | *5⁤23* (Borelli; Cassini con le eclissi) |
| 848 | `8\tfrac{2}{3}` | *8⁤23* |
| 951 | `24\tfrac{2}{3}` | *24⁤23* |
| 952 | parentesi graffa con `\textit{semi-diameter of Jupiter}` | «} Semidiam. Jovis» |
| 953 | `14\tfrac{23}{60}` | *14⁤2360* |
| 954 | `25\tfrac{3}{10}` | *25⁤310* |
| 955 | `37\tfrac{1}{8}''` | *37⁤18″* |
| 956 | `37\tfrac{3}{8}''` | *37⁤38″* |
| 957 | `37\tfrac{1}{4}''` | *37⁤14″* |
| 958 | `1\tfrac{19}{20}` | *1⁤1920.* |
| 959 | `2\tfrac{1}{2}` | *2⁤12.* |
| 639 | `3\tfrac{1}{2}` | *3⁤12.* |
| 960 | `\tfrac{7}{10}` | *septem decimis partibus* |

**SVG di Motte che non tornano con il latino: nessuno.** La tabella completa è data qui perché le formule servono a sciogliere le frazioni appiattite della trascrizione.

### A.15 Riepilogo: dove Motte aggiunge, omette o sbaglia

| Luogo | Latino | Motte 1846 | Tipo |
|---|---|---|---|
| Titolo | *De mundi systemate. Liber tertius.* | «BOOK III.» (due volte) | omissione del sottotitolo; ripetizione |
| III.G1.01 | *percipient … deponent*; *minime* | «could not easily discern» | tempo cambiato; attenuazione |
| III.G1.01 | *ne sterilia videantur* | «lest they should have appeared of themselves dry and barren» | ampliamento |
| III.G1.02 | *phænomenis* | «appearances» | resa diversa (ma «phænomena» nella Regola IV) |
| III.G1.03 | *non luxuriat* | «affects not the pomp» | immagine aggiunta |
| III.G1.04 | *effectuum … ejusdem generis* | «the same natural effects» | **errore di senso** |
| III.G1.06 | *intendi & remitti nequeunt* | «admit neither intension nor remission of degrees» | esplicitazione |
| III.G1.06 | *competunt* | «are found to belong» | aggiunta |
| III.G1.07 | *quæ minui non possunt, non possunt auferri* | «can never be quite taken away» | attenuazione |
| III.G1.07 | *somnia temere confingenda* | «dreams and vain fictions of our own devising» | parafrasi; *temere* non reso |
| III.G1.07 | *vires inertiæ* | «vires inertiæ» | lasciato in latino |
| III.G1.07 | *ex hisce … colligimus* | «we only infer» | aggiunta di «only» |
| III.G1.07 | *partes divisæ separabiles … indivisæ in infinitum dividi* | «the undivided as well as the divided particles may be divided and actually separated to infinity» | **due affermazioni fuse**; «actually» aggiunto |
| III.G1.08 | *corpora omnia in se mutuo gravitant* | «are endowed with a principle of mutual gravitation» | **aggiunta di un «principio»** |
| III.G1.08 | *vim insitam … vim inertiæ* | «their vis insita … their vis inertiæ, This» | latino conservato; virgola per punto |
| III.G1.09 | *per inductionem* | «by general induction» | aggiunta |
| III.G1.09 | *contrariis hypothesibus* | «any contrary hypotheses that may be imagined» | aggiunta |
| III.G1.10 | *tollatur* | «evaded» | senso indebolito |
| — | *PHÆNOMENA.* | «PHÆNOMENA, OR APPEARANCES.» | aggiunta |
| III.G1.12 | *consentiunt astronomi* | «all astronomers agree» | aggiunta |
| III.G1.14 | graffa *Semidiam. Jovis* | `[SVG 952]` nella sola riga di Borelli | impaginazione |
| III.G1.15 | *Elongationes … & diametrum* | «the diameters of Jupiter and the elongation» | ordine e numero invertiti |
| III.G1.16 | *a sole vel terra* | «from the earth» | omissione |
| III.G1.16 | *refrangibilitatem* | «refrangibility of the rays» | aggiunta |
| III.G1.17 | *ad saturnum* | «to Saturn's centre» | uniformazione |
| III.G1.21 | *Si rejiciatur* | «If we, then, reject» | aggiunta |
| III.G1.23 | *ultra solem … e regione solis … cis solem* | «in respect of us, beyond or above … about the same height on one side or other … below or between us and the sun» | **ampliamento esplicativo** |
| III.G1.23 | *transeuntes* | «when directly under, seen like spots» | aggiunta |
| III.G1.24 | *vel solis circa terram vel terræ circa solem* | «(whether of the sun about the earth, or)» | alternativa geocentrica messa fra parentesi |
| III.G1.25 | *a Keplero inventa … apud omnes* | «first observed by Kepler, is now received by all astronomers» | aggiunte |
| III.G1.27 | tabella unica | due mezze tabelle con virgolette di ripetizione | impaginazione |
| III.G1.29 | (enunciato) | «**Then** the primary planets» | **refuso** per «That» |
| III.G1.30 | *Propositio est* | «This a noted proposition» | **verbo mancante** |
| III.G1.32 | *a vi solis* | «by the action of the sun» | *vis* reso «action» |

Nessuna divergenza di Motte nelle cifre: tutti i numeri delle cinque tabelle e del testo (periodi, distanze, elongazioni, diametri, 3 a 7, 1719, 43″, 42″, 18″, 16″) coincidono con il latino.

---

## Note editoriali e fisiche

Queste note sono aggiunte del presente fascicolo, non affermazioni tradotte da Newton. Le verifiche numeriche sono state eseguite con uno script Python (`tmp/21/verifica.py`), che ricalcola le tabelle dai dati del testo. Ciò che proviene da conoscenza generale e non dalle fonti allegate (valori moderni, identificazioni di persone e strumenti) è marcato «(non verificato sulle fonti allegate)».

### N1. L’introduzione: perché il Libro III è «in proposizioni»

Newton dichiara di aver scritto prima un terzo libro «con un metodo popolare» e di averlo poi trasformato in proposizioni «alla maniera matematica», per evitare dispute con lettori che non avessero assimilato i principi. Il testo non dice quale fosse quel primo libro; la redazione divulgativa è nota come *De motu corporum liber secundus* o *System of the World*, pubblicata dopo la morte di Newton (non verificato sulle fonti allegate). Il percorso di lettura minimo indicato da Newton (definizioni, leggi, Sezioni I–III del Libro I) è anche, di fatto, il percorso di un corso liceale: legge delle aree, forza centripeta nel moto circolare (Prop. IV, Cor. 6: tempi nel rapporto sesquiplicato ⇔ forza inversamente come il quadrato della distanza), moto nelle coniche.

### N2. Regole I e II: economia delle cause

La Regola I unisce due requisiti: le cause devono essere **vere** (cioè esistenti, non soltanto immaginate) e **sufficienti**. La massima scolastica citata («la natura non fa nulla invano…») è un principio di economia; la novità è il «vere», che esclude cause inventate solo perché funzionano. La Regola II applica la I agli effetti dello stesso genere: se una causa basta a spiegare la caduta delle pietre in Europa, la stessa deve spiegare la caduta in America. È esattamente l’argomento della Prop. IV del Libro III (la forza che trattiene la Luna è la gravità, *per reg. i. & ii.*): la Regola II permette di identificare la forza celeste con quella terrestre.

### N3. Regola III: le qualità «che non si possono aumentare né diminuire»

**Lessico.** *Intensio* e *remissio* sono termini della filosofia scolastica per l’aumento e la diminuzione di grado di una qualità (il calore, la luce). Le qualità che Newton considera universali sono quelle che **non hanno gradi** in un corpo: un corpo non è «più o meno esteso» nel senso in cui è più o meno caldo, non è «più o meno impenetrabile». Per questo l’argomento «quelle che non possono essere diminuite non possono essere tolte» funziona: se una qualità non ammette gradi, non c’è modo di farla sparire per diminuzione progressiva.

**Struttura dell’argomento.** Newton applica la regola a cinque qualità (estensione, durezza, impenetrabilità, mobilità, forza d’inerzia) e mostra lo stesso schema: si osservano nei corpi accessibili all’esperienza; la qualità del tutto nasce da quella delle parti; dunque appartiene anche alle parti minime e a tutti i corpi. L’atomismo è presentato come conseguenza della regola, non come ipotesi. Sulla divisibilità all’infinito Newton è prudente: la matematica la garantisce in teoria, l’esperienza non la mostra; basterebbe un solo esperimento per estendere la regola.

**La gravità.** Il secondo capoverso applica la stessa regola alla gravità e la dichiara più fondata dell’impenetrabilità, perché per i corpi celesti non si ha nessuna prova diretta dell’impenetrabilità, mentre la gravità è osservata (Luna, mare e maree, pianeti, comete). Subito dopo Newton prende due precauzioni:

1. la gravità **non è essenziale** ai corpi: la regola la rende universale, non necessaria;
2. la gravità **diminuisce** con la distanza, mentre la forza d’inerzia è immutabile. A rigore, dunque, la gravità non soddisfa la condizione dell’enunciato («qualità che non possono essere aumentate né diminuite»). Newton non lo dice esplicitamente, ma l’accostamento delle ultime tre frasi suggerisce proprio questa distinzione: la forza insita è una qualità nel senso della regola, la gravità no; l’universalità della gravità si fonda piuttosto sulla seconda condizione (appartiene a tutti i corpi su cui si possono fare esperimenti e osservazioni). È un punto discusso dagli storici (non verificato sulle fonti allegate).

**Per la didattica.** La Regola III è un buon esempio di inferenza dal particolare all’universale con condizioni esplicite: la qualità deve essere osservata in **tutti** i corpi accessibili e non deve variare di grado.

### N4. «Sogni», «ipotesi» e l’analogia della natura

Nella Regola III Newton scrive che non si devono *somnia temere confingere*, «inventare temerariamente sogni», contro il tenore degli esperimenti. *Confingere* (inventare, fabbricare) è della stessa famiglia di *fingere* nello Scolio generale: *hypotheses non fingo*, «non invento ipotesi» (latino del gruppo G9, `latino-1726-L3-ScholiumGenerale.md`). Lo stesso Scolio definisce: *Quicquid enim ex phænomenis non deducitur, hypothesis vocanda est*, «tutto ciò che non si deduce dai fenomeni si deve chiamare ipotesi». Nel lessico del Libro III «ipotesi» ha quindi due usi:

- l’uso polemico delle Regole e dello Scolio generale: una supposizione non ricavata dai fenomeni, che si oppone a una proposizione ricavata per induzione (Regola IV: *non obstantibus contrariis hypothesibus*);
- l’uso tecnico delle *Hypotheses* numerate del Libro III (Ipotesi I, *Centrum systematis mundani quiescere*, dopo la Prop. X; Ipotesi II dopo la Prop. XXXVIII): assunzioni dichiarate, su cui si costruisce una dimostrazione.

Nella traduzione la parola è sempre «ipotesi»; la distinzione va spiegata al lettore, non introdotta nel testo. L’«analogia della natura», «semplice e sempre in accordo con sé stessa», riprende la Regola I: è ciò che autorizza a trasferire le qualità dai corpi osservati a quelli non osservati.

### N5. Regola IV: che cosa significa *inductio*

**Il senso del termine.** Nel latino di Newton *inductio* è il procedimento che va dai fenomeni (casi osservati) a una proposizione generale. La Regola IV non promette che la proposizione sia vera in assoluto: la dichiara da considerare vera, «o esattamente o con ottima approssimazione», **fino a prova contraria**, cioè finché altri fenomeni non la rendano più esatta o mostrino eccezioni. È una regola di fallibilismo: la proposizione indotta è provvisoria, ma non può essere scalzata da un’ipotesi; solo un fenomeno può correggerla.

**Lo Scolio generale.** La stessa idea ritorna nello Scolio generale: *In hac philosophia propositiones deducuntur ex phænomenis, & redduntur generales per inductionem*, «in questa filosofia le proposizioni si deducono dai fenomeni e si rendono generali per induzione». Due operazioni distinte, dunque: la **deduzione** dai fenomeni (per esempio, dalla legge delle aree e dal rapporto sesquiplicato alla forza inversamente proporzionale al quadrato, con le proposizioni del Libro I), e la **generalizzazione** per induzione (dai satelliti di Giove e dai pianeti a tutti i corpi). Il termine *inductio* non coincide quindi con l’induzione enumerativa dei manuali di logica, e nemmeno con la «general induction» di Motte, che aggiunge l’aggettivo.

**Il contesto (non verificato sulle fonti allegate).** La Regola IV compare per la prima volta nella terza edizione (1726), come la Regola III nella forma attuale compare nella seconda (1713); nella prima edizione (1687) al loro posto c’erano delle *Hypotheses*. Il cambiamento di nome da «ipotesi» a «regole» e l’aggiunta della Regola IV sono di solito letti come risposta alle critiche di Leibniz e dei cartesiani alla gravità come «qualità occulta». Non è verificabile sulle fonti allegate, che contengono soltanto il testo del 1726.

**La frase finale.** *Ne argumentum inductionis tollatur per hypotheses*: l’argomento induttivo non deve essere «tolto di mezzo» da ipotesi. Motte scrive «evaded», cioè aggirato: con Motte il pericolo è che un’ipotesi permetta di sfuggire alla conclusione; nel latino il pericolo è che la annulli. La differenza è sottile ma pertinente: per Newton un’ipotesi, per quanto ingegnosa (i vortici del Libro II, Sezione IX), non ha forza probatoria contro una proposizione ricavata dai fenomeni.

### N6. Fenomeni I–II: pianeti «circumgioviali» e «secondari»; tempi rispetto alle stelle fisse

Newton chiama i satelliti di Giove e di Saturno «pianeti circumgioviali» e «circumsaturnii» negli enunciati e *satellites* nel testo. Nel lessico del Libro III i pianeti che girano attorno al Sole sono «primari» (*planetæ primarii*, Fenomeno III); i satelliti sono, per contrasto, «pianeti secondari» (*planetæ secundarii*), un’espressione che non compare in questo fascicolo ma nel seguito del Libro III.

*Stellis fixis quiescentibus*, «essendo in quiete le stelle fisse», precisa che i tempi periodici sono misurati rispetto alle stelle fisse: sono i periodi **siderali**, non quelli sinodici (rispetto al Sole o alla Terra), che sono diversi. Lo stesso vale per i pianeti (Fenomeno IV, tabella *respectu fixarum*).

L’enunciato dei Fenomeni I e II contiene due affermazioni: la legge delle aree (qui banale, perché le orbite sono quasi circolari e uniformi) e il rapporto sesquiplicato, cioè *T*² ∝ *a*³ (terza legge di Keplero, che Newton qui non chiama così). Nella Prop. I le due affermazioni danno rispettivamente la direzione della forza (verso il centro di Giove, per la Prop. II o III del Libro I) e la sua legge (inversamente come il quadrato, per il Cor. 6 della Prop. IV del Libro I).

### N7. Fenomeno I: i numeri dei satelliti di Giove

**Tempi periodici.** In giorni: 1,769144; 3,551181; 7,154583; 16,688993 (dalla tabella, convertendo ore, minuti e secondi).

**Colonna «dai tempi periodici».** I valori 5,667; 9,017; 14,384; 25,299 sono esattamente proporzionali a *T*^(2/3): il prodotto *a*³/*T*² vale 58,148; 58,135; 58,139; 58,137, costante entro gli arrotondamenti. Ancorando il calcolo al secondo, al terzo o al quarto satellite si riproducono **tutte e quattro le cifre** del testo (ancorando al primo, le ultime cifre differiscono di una unità). La costante coincide con quella delle distanze di Cassini con le eclissi (*a*³/*T*² = 58,14; 57,81; 58,13; 58,14): la colonna teorica è dunque scalata sui valori di Cassini con le eclissi, che sono i migliori. Le altre serie danno costanti diverse (Borelli 51,6–58,1; Townley 47,8–54,2; Cassini al telescopio 39,9–43,7), cioè sono scalate diversamente, ma ognuna, entro le incertezze, segue il rapporto sesquiplicato.

| Satellite | *T* (giorni) | Borelli | Townley | Cassini tel. | Cassini ecl. | Dai tempi | *a*³/*T*² (dai tempi) |
|---|---:|---:|---:|---:|---:|---:|---:|
| 1 | 1,769144 | 5,667 | 5,52 | 5 | 5,667 | 5,667 | 58,148 |
| 2 | 3,551181 | 8,667 | 8,78 | 8 | 9 | 9,017 | 58,135 |
| 3 | 7,154583 | 14 | 13,47 | 13 | 14,383 | 14,384 | 58,139 |
| 4 | 16,688993 | 24,667 | 24,72 | 23 | 25,3 | 25,299 | 58,137 |

**Le elongazioni di Pound.** Dall’elongazione misurata del quarto satellite (8′ 16″ = 496″) la regola sesquiplicata dà per il terzo 282,00″ = 4′ 42″: **esattamente** il valore misurato con il telescopio di 123 piedi. Il rapporto osservato 282/496 = 0,56855 coincide con (*T*₃/*T*₄)^(2/3) = 0,56855. Per il secondo e il primo satellite il calcolo dà 176,784″ = 2′ 56″ 47‴ e 111,097″ = 1′ 51″ 6‴: coincidono con le cifre del testo (i terzi ‴ sono sessantesimi di secondo).

**I semidiametri.** Con il diametro di 37 1/4″ (semidiametro 18,625″), che è la media esatta dei due valori dei transiti (37 1/8″ e 37 3/8″):

| Satellite | Elongazione | / 18,625″ | Testo |
|---|---|---:|---:|
| 1 | 1′ 51″ 6‴ = 111,100″ | 5,9651 | 5,965 |
| 2 | 2′ 56″ 47‴ = 176,783″ | **9,4917** | **9,494** |
| 3 | 4′ 42″ = 282″ | 15,1409 | 15,141 |
| 4 | 8′ 16″ = 496″ | 26,6309 | 26,63 |

**Cifra che non torna:** per il secondo satellite il calcolo dà **9,492**, non 9,494. Lo scarto è di 2 millesimi (0,02%), sotto ogni precisione osservativa, ma non è un arrotondamento: può essere un errore di calcolo di Newton o un refuso di stampa (Motte ha anch’egli 9,494). Non corretto nel testo; segnalato nel § A.12.

**Confronto moderno (non verificato sulle fonti allegate).** I periodi siderali moderni di Io, Europa, Ganimede e Callisto sono 1,769; 3,551; 7,155; 16,689 giorni: i valori di Newton coincidono al millesimo di giorno. I semiassi moderni in raggi equatoriali di Giove (71 492 km) sono 5,90; 9,39; 14,97; 26,33: quelli di Newton (5,965; 9,494; 15,141; 26,63) sono più grandi dell’1% circa, perché il diametro di 37 1/4″ è un poco piccolo: alla distanza media di 5,20 UA il diametro equatoriale di Giove sottende circa 37,9″. L’elongazione massima di Callisto alla stessa distanza è circa 8′ 19″, contro gli 8′ 16″ di Pound. James Pound era un astronomo dilettante, zio di James Bradley (non verificato sulle fonti allegate).

**La dilatazione della luce.** La spiegazione dei diametri maggiori nei telescopi corti (40″–41″) con la «disuguale rifrangibilità» è l’aberrazione cromatica delle lenti, studiata da Newton nell’*Opticks* (non verificato sulle fonti allegate): la luce dei diversi colori si focalizza in punti diversi e allarga il bordo dell’immagine di una quantità che, nei telescopi lunghi, pesa meno sul diametro.

### N8. Fenomeno II: i numeri dei satelliti di Saturno

**Tempi periodici.** In giorni: 1,887812; 2,737060; 4,517500; 15,945301; 79,325000.

**Colonna «dai tempi periodici» (quarto satellite = 8).** Il calcolo con *T*^(2/3) dà 1,929; 2,471; 3,451; 8; **23,314**. Le prime quattro cifre del testo (1,93; 2,47; 3,45; 8) tornano; il quinto valore del testo, **23,35**, non torna: il calcolo dà 23,31.

**Seconda serie (quarto satellite = 8,7).** Il calcolo dà 2,098; 2,687; 3,753; 8,7; **25,353**: il testo (2,1; 2,69; 3,75; 8,7; 25,35) torna in tutte le cifre. Le due serie non sono quindi l’una il riscalamento dell’altra: 23,35 × 8,7/8 = 25,39, non 25,35. La seconda serie, calcolata correttamente, conferma che il 23,35 della tabella è un piccolo errore (di calcolo o di stampa: Motte ha la stessa cifra). Non corretto nel testo; segnalato nel § A.12.

**Osservazioni contro calcolo.** I valori osservati (1 19/20; 2 1/2; 3 1/2; 8; 24) danno *a*³/*T*² = 2,08; 2,09; 2,10; 2,01; 2,20: costante entro il 5% (il quinto satellite, Giapeto, è il più incerto).

**Diametri.** 42″ × 3/7 = 18″: il diametro di Saturno torna con il rapporto 3 a 7. Da 43″ (28–29 maggio 1719) a 42″ «alla distanza media» c’è la riduzione alla distanza media Terra–Saturno; il testo non dà la distanza del 1719, e il calcolo non si può rifare con le fonti allegate. In Inghilterra, nel 1719, era in uso il calendario giuliano (non verificato sulle fonti allegate); la data non è marcata *st. vet.* e resta come nel testo.

**Confronto moderno (non verificato sulle fonti allegate).** I cinque satelliti sono Teti, Dione, Rea, Titano (scoperto da Huygens nel 1655) e Giapeto; i periodi moderni (1,888; 2,737; 4,518; 15,945; 79,33 giorni) coincidono con quelli di Cassini. In raggi esterni dell’anello A (136 775 km) i semiassi moderni sono 2,15; 2,76; 3,85; 8,93; 26,03: i valori di Newton con 8,7 (2,1; 2,69; 3,75; 8,7; 25,35) sono più piccoli del 2–3%. Il rapporto fra diametro dell’anello A e diametro equatoriale di Saturno è oggi 2,27, contro 7/3 = 2,33; alla distanza media (9,54 UA) l’anello sottende circa 39,5″ e il pianeta 17,4″. Il «non maggiore di 16″» di Newton, dopo aver scartato la luce erratica, è dunque un poco piccolo.

### N9. Fenomeno III: le fasi come prova

Il ragionamento è geometrico. Un pianeta interno (Mercurio, Venere) che gira attorno al Sole mostra la faccia piena quando è dietro il Sole (congiunzione superiore), la faccia dimezzata quando è alla massima elongazione, cioè di lato rispetto al Sole visto dalla Terra, e la falce quando è fra la Terra e il Sole (congiunzione inferiore), dove talvolta transita sul disco solare come una macchia scura. Questa sequenza è impossibile se Venere gira attorno alla Terra dentro l’orbita del Sole (come nel sistema tolemaico): là Venere sarebbe sempre falcata o quasi. È l’argomento delle fasi di Venere osservate da Galileo nel 1610 (non verificato sulle fonti allegate; il testo non nomina Galileo).

Per Marte, pianeta esterno, la faccia piena vicino alla congiunzione e la faccia **gibbosa** (non dimezzata) nelle quadrature mostrano che Marte gira attorno al Sole a una distanza maggiore di quella della Terra. Per Giove e Saturno le fasi sono «sempre piene» (l’angolo di fase massimo, visto dalla Terra, è piccolo: circa 11° per Giove e 6° per Saturno; non verificato sulle fonti allegate). Le ombre dei satelliti sui loro dischi provano che brillano di luce solare riflessa. La deduzione che anche essi «cingono il Sole» dalle fasi sempre piene non è stringente da sola: Newton la affida al quadro complessivo, e il Fenomeno IV la completa con la regola sesquiplicata riferita al Sole.

La resa «di lato al Sole» per *e regione solis* è una scelta interpretativa (A.0): *e regione* vuol dire «di fronte, in direzione di»; qui indica la posizione del pianeta a quadratura rispetto al Sole, cioè alla massima elongazione. **Da decidere.**

### N10. Fenomeno IV: la tabella dei pianeti

**Il controllo della terza legge.** Con la distanza della Terra = 100 000 e il suo periodo di 365,2565 giorni, la distanza «secondo i tempi periodici» è 100 000 · (*T*/365,2565)^(2/3):

| Pianeta | *T* (testo) | Distanza calcolata | Testo | Differenza | Keplero | Boulliau | Fra i due? |
|---|---:|---:|---:|---:|---:|---:|---|
| ♄ Saturno | 10759,275 | 953 799 | 954 006 | **+207** | 951 000 | 954 198 | sì |
| ♃ Giove | 4332,514 | 520 109 | 520 096 | −13 | 519 650 | 522 520 | sì |
| ♂ Marte | 686,9785 | 152 369 | 152 369 | 0 | 152 350 | 152 350 | no (di poco sopra) |
| ♁ Terra | 365,2565 | 100 000 | 100 000 | 0 | 100 000 | 100 000 | — |
| ♀ Venere | 224,6176 | 72 315 | 72 333 | **+18** | 72 400 | 72 398 | no (sotto) |
| ☿ Mercurio | 87,9692 | 38 710 | 38 710 | 0 | 38 806 | 38 585 | sì |

**Esito.** Marte, Mercurio e la Terra tornano esattamente; Giove con uno scarto di 13 unità (0,003%), trascurabile. **Due cifre non tornano:**

1. **Venere.** La distanza 72 333 corrisponde a un periodo di **224,6998** giorni, non a 224,6176. Il valore moderno del periodo siderale di Venere è 224,701 giorni (non verificato sulle fonti allegate): la distanza del testo è giusta, e il periodo stampato sembra un errore, forse di copia, del valore 224,6998 o simile. Motte ha la stessa cifra 224,6176, che è quindi probabilmente nella stampa del 1726. Non corretto nel testo; segnalato nel § A.12.
2. **Saturno.** La distanza 954 006 corrisponde a un periodo di 10 762,78 giorni; con 10 759,275 si ottiene 953 799 (scarto dello 0,02%). Qui è il periodo a coincidere con il valore moderno (10 759,22 giorni) e la distanza a essere leggermente fuori. Una correzione per le masse (Libro I, Prop. LX: semiasse proporzionale a (Sole + pianeta)^(1/3)), con i rapporti di massa che Newton stesso dà nella Prop. VIII del Libro III (Giove 1/1067, Saturno 1/3021 del Sole; latino del gruppo G2), darebbe circa +105 unità per Saturno, non +207, e +163 per Giove, mentre il testo ha −13: la correzione per le masse non spiega gli scarti. Non corretto nel testo.

**«Per lo più intermedie».** Le distanze teoriche stanno fra quelle di Keplero e di Boulliau per Saturno, Giove e Mercurio; per Marte sono di 19 unità sopra il valore comune dei due, per Venere di 65 unità sotto entrambi. Tre casi su cinque: «per lo più», come dice Newton. L’affermazione «non differiscono sensibilmente» è vera: lo scarto massimo dalle distanze di Keplero o di Boulliau è dello 0,6% (Giove, Boulliau).

**Confronto moderno (non verificato sulle fonti allegate).** I semiassi maggiori moderni in UA sono: Saturno 9,537, Giove 5,203, Marte 1,5237, Venere 0,72333, Mercurio 0,38710; quelli di Newton (9,540; 5,201; 1,5237; 0,72333; 0,38710) coincidono quasi tutti alla quarta cifra. I periodi moderni sono 10 759,22; 4332,59; 686,98; 365,256; 224,701; 87,969 giorni.

**Le eclissi dei satelliti di Giove.** Newton spiega perché le distanze dei pianeti superiori non sono in discussione: le eclissi dei satelliti mostrano dove cade l’ombra di Giove, cioè la direzione Sole–Giove, quindi la longitudine eliocentrica di Giove; confrontata con la longitudine geocentrica osservata, e nota l’orbita della Terra, dà la distanza Sole–Giove per triangolazione nel triangolo Sole–Terra–Giove. Le distanze sono tutte relative (Terra = 100 000): la scala assoluta richiede la parallasse solare, che qui non compare.

**Neutralità del Fenomeno IV.** Newton scrive «il Sole attorno alla Terra o la Terra attorno al Sole» e osserva che i tempi periodici e le dimensioni delle orbite sono gli stessi nei due sistemi. A questo punto del libro la scelta non è ancora fatta: l’Ipotesi I (il centro del sistema del mondo è in quiete) e le Propp. XII–XIII (il Sole si muove poco attorno al centro comune di gravità; i pianeti si muovono in ellissi con il fuoco nel centro del Sole) la faranno nel Fascicolo 22 (latino del gruppo G2).

### N11. Fenomeni V e VI: la legge delle aree

**Fenomeno V.** Visti dalla Terra i pianeti hanno moti diretti, stazioni e retrogradazioni: un raggio Terra–pianeta descrive aree che non crescono uniformemente col tempo, e anzi tornano indietro. Visti dal Sole i moti sono sempre diretti, un poco più veloci al perielio e più lenti all’afelio, in modo che le aree crescano uniformemente: è la seconda legge di Keplero (il testo non la nomina così). Nella Prop. II del Libro III il Fenomeno V, con la Prop. II del Libro I, dà la direzione della forza verso il Sole.

**Fenomeno VI.** Newton dice che la legge delle aree per la Luna «risulta dal moto apparente della Luna confrontato con il suo diametro apparente». Il ragionamento è questo: la distanza Terra–Luna è inversamente proporzionale al diametro apparente δ della Luna; il moto apparente è la velocità angolare ω; la velocità areale è ½ *r*² ω ∝ ω/δ². La legge delle aree richiede dunque che il moto apparente sia proporzionale al quadrato del diametro apparente: ω ∝ δ². Esempio con valori moderni (non verificato sulle fonti allegate): al perigeo e all’apogeo medi il diametro apparente della Luna varia fra circa 33,5′ e 29,4′ (rapporto 1,14), e il moto diurno fra circa 15,4° e 11,8° al giorno (rapporto 1,30 ≈ 1,14² = 1,30). Le «minuzie insensibili» che Newton trascura sono le disuguaglianze dovute al Sole (variazione, evezione), trattate nel seguito del Libro III.

---

## Controllo della copertura

Pagine 1726 dai marcatori ‹n› della trascrizione (‹386›–‹395›). Motte: estratto senza marcatori di pagina, «sezione corrispondente».

| Identificatori | Incipit latino | Contenuto | 1726 | Motte 1846 |
|---|---|---|---|---|
| III.G1.01 | *IN libris præcedentibus principia philosophiæ tradidi* | Titolo e introduzione del Libro III | p. 386 | Book III, introduzione |
| III.G1.02–III.G1.03 | *Causas rerum naturalium non plures admitti debere* | Regola I e commento | p. 387 | Rule I |
| III.G1.04–III.G1.05 | *Ideoque effectuum naturalium ejusdem generis* | Regola II ed esempi | p. 387 | Rule II |
| III.G1.06–III.G1.07 | *Qualitates corporum quæ intendi & remitti nequeunt* | Regola III, commento sulle qualità dei corpi | pp. 387–388 | Rule III |
| III.G1.08 | *Denique si corpora omnia in circuitu terræ* | Regola III, la gravità universale | pp. 388–389 | Rule III, «Lastly» |
| III.G1.09–III.G1.10 | *In philosophia experimentali, propositiones ex phænomenis* | Regola IV e commento | p. 389 | Rule IV |
| III.G1.11–III.G1.12 | *Planetas circumjoviales* … *COnstat ex observationibus* | Fenomeno I, enunciato e testo | p. 390 | Phænomenon I |
| III.G1.13–III.G1.14 | *Satellitum jovialium tempora periodica* … *Distantiæ satellitum a centro jovis* | Fenomeno I, due tabelle | p. 390 | tabelle |
| III.G1.15–III.G1.16 | *Elongationes satellitum jovis* … *Diameter jovis micrometro* | Fenomeno I, misure di Pound | pp. 390–391 | «Mr. Pound has determined» |
| III.G1.17–III.G1.18 | *Planetas circumsaturnios* … *Cassinus utique* | Fenomeno II, enunciato e testo | p. 391 | Phænomenon II |
| III.G1.19–III.G1.20 | *Satellitum saturniorum tempora periodica* … *Distantiæ … in semidiametris annuli* | Fenomeno II, due tabelle | pp. 391–392 | tabelle |
| III.G1.21 | *Quarti satellitis elongatio maxima* | Fenomeno II, misure col telescopio di Huygens, anello | p. 392 | «The greatest elongation of the fourth satellite» |
| III.G1.22–III.G1.23 | *Planetas quinque primarios* … *Mercurium & venerem circa solem* | Fenomeno III | p. 392 | Phænomenon III |
| III.G1.24–III.G1.25 | *Planetarum quinque primariorum* … *Hæc a Keplero inventa ratio* | Fenomeno IV, enunciato e testo | p. 393 | Phænomenon IV |
| III.G1.26–III.G1.27 | *Planetarum ac telluris tempora periodica* … *distantiæ mediocres* | Fenomeno IV, due tabelle | p. 393 | tabelle |
| III.G1.28 | *De distantiis mercurii & veneris* | Fenomeno IV, distanze ed eclissi dei satelliti | p. 393 | «As to Mercury and Venus» |
| III.G1.29–III.G1.30 | *Planetas primarios, radiis ad terram ductis* | Fenomeno V | p. 394 | Phænomenon V |
| III.G1.31–III.G1.32 | *Lunam radio ad centrum terræ ducto* | Fenomeno VI | p. 394 | Phænomenon VI |
| III.G1.33 | *PROPOSITIONES.* | Titolo delle Proposizioni | p. 395 | «PROPOSITIONS.» |

**Controlli eseguiti.**

1. **Copertura frase per frase.** Ho riletto in sequenza ogni periodo della trascrizione, da *IN libris præcedentibus* a *PROPOSITIONES.*, contro la traduzione: nessuna frase manca. I titoli (*De mundi systemate. Liber tertius*, *Regulæ philosophandi*, *Phænomena*, *Regula I*–*IV*, *Phænomenon I*–*VI*) sono resi come titoli. Le frasi lunghe dell’introduzione e della Regola III sono divise in italiano senza omettere membri. I 33 identificatori sono consecutivi e unici (controllo automatico).
2. **Tabelle.** Le cinque tabelle sono ricostruite per intero, cella per cella, sul latino, e controllate riga per riga su Motte: nessuna cifra diverge. Le frazioni appiattite sono sciolte e confermate dalle formule SVG di Motte (§ A.14).
3. **Verifiche numeriche** (`tmp/21/verifica.py`): terza legge di Keplero per i satelliti di Giove (colonna «dai tempi periodici», *a*³/*T*² costante), elongazioni di Pound dai tempi periodici, conversione in semidiametri di Giove, media dei diametri dei transiti; satelliti di Saturno (due serie, con 8 e con 8,7), rapporto 3 a 7 per i diametri; pianeti (colonna «secondo i tempi periodici», periodi corrispondenti alle distanze, posizione fra Keplero e Boulliau). **Cifre che non tornano** (non corrette nel testo): Fenomeno I, 9,494 (atteso 9,492); Fenomeno II, 23,35 (atteso 23,31); Fenomeno IV, tempo periodico di Venere 224,6176 (la distanza del testo richiede 224,700) e distanza di Saturno 954006 (atteso 953799). Tutte le altre cifre tornano entro l’ultima cifra decimale (note N7, N8, N10).
4. **Parte B.** `check.py` sul file finale: JSON valido; tutte le stringhe `la` ed `en` degli enunciati sono sottostringhe esatte delle fonti; ogni identificatore di `copertura` è presente nel testo.
5. **Motte.** Confronto di tutta la sezione corrispondente; divergenze nel § A.15. SVG: 13 occorrenze controllate, nessuna che non torni (§ A.14).
6. **Rimandi.** Cinque rimandi ai Libri I e II, tutti verificati sui fascicoli del progetto (§ A.13); nessuno che non torni.
7. **Separazione fra testo e commento.** Il testo tradotto non contiene formule moderne; le integrazioni del curatore sono tra parentesi quadre.

**Non ho potuto verificare:**

- **la stampa del 1726**: i punti del § A.12 (*motuo*, *ocurrerint*, *capita*, *satellitium*, *acto*, la graffa della tabella di Giove) e le quattro cifre che non tornano (9,494; 23,35; 224,6176; 954006) restano da controllare sulla scansione ECCO;
- **Motte 1729**: in particolare se il refuso «Then» (Fenomeno V) e il verbo mancante «This a noted proposition» siano già nella prima edizione inglese o soltanto nell’edizione 1846;
- **la paginazione di Motte**: l’estratto non ha marcatori di pagina;
- **la riduzione del diametro dell’anello** da 43″ (1719) a 42″ alla distanza media: il testo non dà la distanza di Saturno nel 1719;
- i **dati moderni** e le **notizie storiche** delle note N1, N5, N7–N11 (valori orbitali, Pound e Bradley, Galileo, le edizioni del 1687 e del 1713), che vengono da conoscenza generale e non dalle fonti allegate.

---

## Registro del lavoro successivo

| Unità | Stato |
|---|---|
| Libro III: introduzione, Regole I–IV, Fenomeni I–VI, «Proposizioni» | **Fascicolo 21, presente documento, prima versione** |
| Refusi della trascrizione e cifre che non tornano (§ A.12) | Da verificare sulla stampa del 1726 (scansione ECCO) |
| *e regione solis* «di lato al Sole» (Fenomeno III) | Da decidere (A.0, N9) |
| Refusi di Motte 1846 nel Fenomeno V («Then», «This a noted») | Da confrontare con Motte 1729 |
| Pagine interattive | Parte B: dieci unità senza passi; candidati a pagine con grafico: Fenomeno I e IV (log *T* contro log *a*, pendenza 3/2, con le serie di Borelli, Townley, Cassini e Keplero, Boulliau), Fenomeno VI (ω contro δ²), Fenomeno III (fasi di Venere nei sistemi tolemaico e copernicano) |
| Legame con il Fascicolo 20 (II.S9.27, regola sesquiplicata) | Confermato (§ A.13); da collegare nelle pagine |
| Revisione filologica e scientifica indipendente | Da eseguire |

Il presente testo è una nuova traduzione assistita da IA. Non riproduce traduzioni italiane o inglesi moderne. **Licenza prevista** (decisione del curatore, Fascicolo 3): testi e traduzioni CC BY-SA 4.0, codice MIT. La trascrizione latina è © The Newton Project; i testi di Motte sono di pubblico dominio.

---

## Parte B — Dati per le pagine interattive

Unità incluse, secondo le istruzioni del Libro III: le **Regole I–IV** e i **Fenomeni I–VI**, come unità con `enunciato` e `copertura` e `"passi": []` (nessuna di esse ha una dimostrazione geometrica). I Fenomeni I, II e IV hanno un campo `"dati"` con i valori numerici delle tabelle (come numeri; i tempi periodici anche in giorni decimali) e l’esito dei controlli. L’introduzione e il titolo «Proposizioni» non sono unità.

Convenzioni:

- `la`: testo latino esatto della trascrizione, refusi compresi (Regola IV: *ocurrerint*, annotato in `nota`);
- `it`: la traduzione di questo fascicolo;
- `en`: Motte 1846, esatto; nessuna formula SVG negli enunciati;
- `dati`: valori del testo; i valori calcolati sono marcati come tali.

```json
{
 "fascicolo": "21-L3-Regole-Fenomeni",
 "versione": "0.1",
 "data": "2026-11-08",
 "convenzioni": {
  "dipende_da": "solo rimandi citati esplicitamente nella frase latina (nessun passo in questo fascicolo)",
  "en": "Motte 1846, esatto; nessuna formula SVG negli enunciati",
  "figura.mostra": "non applicabile: la sezione non ha figure",
  "la": "",
  "dati": "valori del testo come numeri; i campi sotto 'controlli' sono calcolati (tmp/21/verifica.py)"
 },
 "unita": [
  {
   "id": "L3-Reg1",
   "tipo": "Regula philosophandi",
   "titolo": "Regola I — non più cause di quante siano vere e sufficienti",
   "copertura": [
    "III.G1.02",
    "III.G1.03"
   ],
   "fonti": {
    "la": "",
    "en": "Motte 1846, sezione corrispondente (Book III, Rule I)"
   },
   "enunciato": {
    "la": "",
    "it": "Delle cose naturali non si devono ammettere più cause di quante siano vere e sufficienti a spiegarne i fenomeni.",
    "en": "We are to admit no more causes of natural things than such as are both true and sufficient to explain their appearances."
   },
   "passi": [],
   "nota": "Motte rende phænomena con «appearances». Nota N2."
  },
  {
   "id": "L3-Reg2",
   "tipo": "Regula philosophandi",
   "titolo": "Regola II — effetti dello stesso genere, cause uguali",
   "copertura": [
    "III.G1.04",
    "III.G1.05"
   ],
   "fonti": {
    "la": "",
    "en": "Motte 1846, sezione corrispondente (Book III, Rule II)"
   },
   "enunciato": {
    "la": "",
    "it": "E perciò, per quanto è possibile, agli effetti naturali dello stesso genere si devono assegnare le stesse cause.",
    "en": "Therefore to the same natural effects we must, as far as possible, assign the same causes."
   },
   "passi": [],
   "nota": "Motte «the same natural effects» per effectuum … ejusdem generis: errore di senso (§ A.3). Usata nelle Propp. IV e V."
  },
  {
   "id": "L3-Reg3",
   "tipo": "Regula philosophandi",
   "titolo": "Regola III — le qualità universali dei corpi",
   "copertura": [
    "III.G1.06",
    "III.G1.07",
    "III.G1.08"
   ],
   "fonti": {
    "la": "",
    "en": "Motte 1846, sezione corrispondente (Book III, Rule III)"
   },
   "enunciato": {
    "la": "",
    "it": "Le qualità dei corpi che non possono essere aumentate né diminuite, e che appartengono a tutti i corpi sui quali è possibile fare esperimenti, si devono considerare qualità di tutti i corpi.",
    "en": "The qualities of bodies, which admit neither intension nor remission of degrees, and which are found to belong to all bodies within the reach of our experiments, are to be esteemed the universal qualities of all bodies whatsoever."
   },
   "passi": [],
   "nota": "Il commento (III.G1.07–08) contiene il refuso della trascrizione «in se motuo» (= mutuo). Motte aggiunge «a principle of mutual gravitation». Usata nella Prop. VI. Note N3–N4."
  },
  {
   "id": "L3-Reg4",
   "tipo": "Regula philosophandi",
   "titolo": "Regola IV — le proposizioni ricavate per induzione",
   "copertura": [
    "III.G1.09",
    "III.G1.10"
   ],
   "fonti": {
    "la": "",
    "en": "Motte 1846, sezione corrispondente (Book III, Rule IV)"
   },
   "enunciato": {
    "la": "",
    "it": "Nella filosofia sperimentale, le proposizioni ricavate dai fenomeni per induzione, nonostante le ipotesi contrarie, si devono considerare vere, o esattamente o con ottima approssimazione, finché non si presentino altri fenomeni per mezzo dei quali o diventino più esatte o siano soggette a eccezioni.",
    "en": "In experimental philosophy we are to look upon propositions collected by general induction from phænomena as accurately or very nearly true, notwithstanding any contrary hypotheses that may be imagined, till such time as other phænomena occur, by which they may either be made more accurate, or liable to exceptions."
   },
   "passi": [],
   "nota": "«ocurrerint» è refuso probabile della trascrizione per «occurrerint». Motte aggiunge «general» e «that may be imagined»; nel commento rende tollatur con «evaded». Nota N5 (senso di inductio e di «ipotesi»)."
  },
  {
   "id": "L3-Phaen1",
   "tipo": "Phænomenon",
   "titolo": "Fenomeno I — i satelliti di Giove",
   "copertura": [
    "III.G1.11",
    "III.G1.12",
    "III.G1.13",
    "III.G1.14",
    "III.G1.15",
    "III.G1.16"
   ],
   "fonti": {
    "la": "",
    "en": "Motte 1846, sezione corrispondente (Book III, Phænomenon I)"
   },
   "enunciato": {
    "la": "",
    "it": "I pianeti circumgioviali, con raggi condotti al centro di Giove, descrivono aree proporzionali ai tempi, e i loro tempi periodici, essendo in quiete le stelle fisse, sono nel rapporto sesquiplicato delle distanze dal suo centro.",
    "en": "That the circumjovial planets, by radii drawn to Jupiter's centre, describe areas proportional to the times of description; and that their periodic times, the fixed stars being at rest, are in the sesquiplicate proportion of their distances from its centre."
   },
   "dati": {
    "tempi_periodici": {
     "testo": [
      "1d 18h 27′ 34″",
      "3d 13h 13′ 42″",
      "7d 3h 42′ 36″",
      "16d 16h 32′ 9″"
     ],
     "giorni": [
      1.769144,
      3.551181,
      7.154583,
      16.688993
     ]
    },
    "distanze_semidiametri_Giove": {
     "Borelli": [
      5.6667,
      8.6667,
      14,
      24.6667
     ],
     "Townley_micrometro": [
      5.52,
      8.78,
      13.47,
      24.72
     ],
     "Cassini_telescopio": [
      5,
      8,
      13,
      23
     ],
     "Cassini_eclissi": [
      5.6667,
      9,
      14.3833,
      25.3
     ],
     "dai_tempi_periodici": [
      5.667,
      9.017,
      14.384,
      25.299
     ]
    },
    "frazioni_testo": {
     "Borelli": [
      "5 2/3",
      "8 2/3",
      "14",
      "24 2/3"
     ],
     "Cassini_eclissi": [
      "5 2/3",
      "9",
      "14 23/60",
      "25 3/10"
     ]
    },
    "Pound": {
     "elongazioni_arcsec": {
      "sat1": 111.1,
      "sat2": 176.7833,
      "sat3": 282,
      "sat4": 496
     },
     "elongazioni_testo": [
      "1′ 51″ 6‴",
      "2′ 56″ 47‴",
      "4′ 42″",
      "8′ 16″"
     ],
     "diametro_Giove_arcsec": {
      "micrometro_123_piedi": "38–40, per lo più 39",
      "telescopi_corti": "40–41",
      "transito_sat1": 37.125,
      "transito_sat3": 37.375,
      "ombra_sat1": 37,
      "assunto": 37.25
     },
     "elongazioni_semidiametri_testo": [
      5.965,
      9.494,
      15.141,
      26.63
     ]
    },
    "controlli": {
     "a3_su_T2_dai_tempi": [
      58.148,
      58.135,
      58.139,
      58.137
     ],
     "colonna_dai_tempi": "riprodotta in tutte le cifre (ancorando al 2°, 3° o 4° satellite); costante uguale a quella di Cassini con le eclissi (58,14)",
     "Pound_dai_tempi": "da 496″ la regola sesquiplicata dà 282,00″ (3°, uguale al misurato), 176,784″ (2°) e 111,097″ (1°): tornano con il testo",
     "semidiametri_calcolati": [
      5.9651,
      9.4917,
      15.1409,
      26.6309
     ],
     "non_torna": "secondo satellite: 176,783″/18,625″ = 9,4917, il testo ha 9,494"
    }
   },
   "passi": [],
   "nota": "Tabelle in III.G1.13–14; misure di Pound in III.G1.15–16. Nota N7."
  },
  {
   "id": "L3-Phaen2",
   "tipo": "Phænomenon",
   "titolo": "Fenomeno II — i satelliti di Saturno",
   "copertura": [
    "III.G1.17",
    "III.G1.18",
    "III.G1.19",
    "III.G1.20",
    "III.G1.21"
   ],
   "fonti": {
    "la": "",
    "en": "Motte 1846, sezione corrispondente (Book III, Phænomenon II)"
   },
   "enunciato": {
    "la": "",
    "it": "I pianeti circumsaturnii, con raggi condotti a Saturno, descrivono aree proporzionali ai tempi, e i loro tempi periodici, essendo in quiete le stelle fisse, sono nel rapporto sesquiplicato delle distanze dal suo centro.",
    "en": "That the circumsaturnal planets, by radii drawn to Saturn's centre, describe areas proportional to the times of description; and that their periodic times, the fixed stars being at rest, are in the sesquiplicate proportion of their distances from its centre."
   },
   "dati": {
    "tempi_periodici": {
     "testo": [
      "1d 21h 18′ 27″",
      "2d 17h 41′ 22″",
      "4d 12h 25′ 12″",
      "15d 22h 41′ 14″",
      "79d 7h 48′ 00″"
     ],
     "giorni": [
      1.887812,
      2.73706,
      4.5175,
      15.945301,
      79.325
     ]
    },
    "distanze_semidiametri_anello": {
     "dalle_osservazioni": [
      1.95,
      2.5,
      3.5,
      8,
      24
     ],
     "dai_tempi_periodici": [
      1.93,
      2.47,
      3.45,
      8,
      23.35
     ],
     "con_quarto_8_7": [
      2.1,
      2.69,
      3.75,
      8.7,
      25.35
     ]
    },
    "frazioni_testo": [
     "1 19/20",
     "2 1/2",
     "3 1/2",
     "8",
     "24"
    ],
    "anello_e_pianeta_arcsec": {
     "anello_1719_maggio_28_29": 43,
     "anello_distanza_media": 42,
     "Saturno": 18,
     "Saturno_senza_luce_erratica_max": 16,
     "rapporto_Saturno_anello": "3 : 7"
    },
    "controlli": {
     "calcolo_quarto_8": [
      1.929,
      2.471,
      3.451,
      8,
      23.314
     ],
     "calcolo_quarto_8_7": [
      2.098,
      2.687,
      3.753,
      8.7,
      25.353
     ],
     "a3_su_T2_osservazioni": [
      2.08,
      2.09,
      2.1,
      2.01,
      2.2
     ],
     "42_per_3_su_7": 18,
     "non_torna": "quinto satellite nella serie con 8: il calcolo dà 23,31, il testo ha 23,35; nella serie con 8,7 il testo (25,35) torna"
    }
   },
   "passi": [],
   "nota": "Tabelle in III.G1.19–20; misure in III.G1.21 (refuso «acto» = octo). Nota N8."
  },
  {
   "id": "L3-Phaen3",
   "tipo": "Phænomenon",
   "titolo": "Fenomeno III — i cinque pianeti primari cingono il Sole",
   "copertura": [
    "III.G1.22",
    "III.G1.23"
   ],
   "fonti": {
    "la": "",
    "en": "Motte 1846, sezione corrispondente (Book III, Phænomenon III)"
   },
   "enunciato": {
    "la": "",
    "it": "I cinque pianeti primari, Mercurio, Venere, Marte, Giove e Saturno, cingono il Sole con le loro orbite.",
    "en": "That the five primary planets, Mercury, Venus, Mars, Jupiter, and Saturn, with their several orbits, encompass the sun."
   },
   "passi": [],
   "nota": "Motte amplia la descrizione delle fasi (§ A.8). Nota N9; «e regione solis» reso «di lato al Sole», da decidere."
  },
  {
   "id": "L3-Phaen4",
   "tipo": "Phænomenon",
   "titolo": "Fenomeno IV — la regola sesquiplicata per i pianeti",
   "copertura": [
    "III.G1.24",
    "III.G1.25",
    "III.G1.26",
    "III.G1.27",
    "III.G1.28"
   ],
   "fonti": {
    "la": "",
    "en": "Motte 1846, sezione corrispondente (Book III, Phænomenon IV)"
   },
   "enunciato": {
    "la": "",
    "it": "I tempi periodici dei cinque pianeti primari, e quello del Sole attorno alla Terra o della Terra attorno al Sole, essendo in quiete le stelle fisse, sono nel rapporto sesquiplicato delle distanze medie dal Sole.",
    "en": "That the fixed stars being at rest, the periodic times of the five primary planets, and (whether of the sun about the earth, or) of the earth about the sun, are in the sesquiplicate proportion of their mean distances from the sun."
   },
   "dati": {
    "ordine": [
     "Saturno",
     "Giove",
     "Marte",
     "Terra",
     "Venere",
     "Mercurio"
    ],
    "tempi_periodici_giorni": [
     10759.275,
     4332.514,
     686.9785,
     365.2565,
     224.6176,
     87.9692
    ],
    "distanze_medie": {
     "Keplero": [
      951000,
      519650,
      152350,
      100000,
      72400,
      38806
     ],
     "Boulliau": [
      954198,
      522520,
      152350,
      100000,
      72398,
      38585
     ],
     "dai_tempi_periodici": [
      954006,
      520096,
      152369,
      100000,
      72333,
      38710
     ]
    },
    "controlli": {
     "distanze_calcolate_T_2_3": [
      953799,
      520109,
      152369,
      100000,
      72315,
      38710
     ],
     "differenza_testo_meno_calcolo": [
      207,
      -13,
      0,
      0,
      18,
      0
     ],
     "periodi_che_darebbero_le_distanze_del_testo": [
      10762.78,
      4332.35,
      686.978,
      365.2565,
      224.7,
      87.97
     ],
     "fra_Keplero_e_Boulliau": [
      true,
      true,
      false,
      null,
      false,
      true
     ],
     "non_torna": "Venere: la distanza 72333 richiede 224,700 giorni (testo 224,6176); Saturno: dal periodo 10759,275 si ha 953799 (testo 954006)"
    }
   },
   "passi": [],
   "nota": "Tabelle in III.G1.26–27. Motte mette fra parentesi l’alternativa geocentrica. Nota N10."
  },
  {
   "id": "L3-Phaen5",
   "tipo": "Phænomenon",
   "titolo": "Fenomeno V — le aree attorno al Sole, non attorno alla Terra",
   "copertura": [
    "III.G1.29",
    "III.G1.30"
   ],
   "fonti": {
    "la": "",
    "en": "Motte 1846, sezione corrispondente (Book III, Phænomenon V)"
   },
   "enunciato": {
    "la": "",
    "it": "I pianeti primari, con raggi condotti alla Terra, descrivono aree per nulla proporzionali ai tempi; ma con raggi condotti al Sole percorrono aree proporzionali ai tempi.",
    "en": "Then the primary planets, by radii drawn to the earth, describe areas no wise proportional to the times; but that the areas which they describe by radii drawn to the sun are proportional to the times of description."
   },
   "passi": [],
   "nota": "Motte 1846 «Then» è refuso per «That»; nel commento «This a noted proposition» manca «is». Nota N11."
  },
  {
   "id": "L3-Phaen6",
   "tipo": "Phænomenon",
   "titolo": "Fenomeno VI — l’area descritta dalla Luna",
   "copertura": [
    "III.G1.31",
    "III.G1.32"
   ],
   "fonti": {
    "la": "",
    "en": "Motte 1846, sezione corrispondente (Book III, Phænomenon VI)"
   },
   "enunciato": {
    "la": "",
    "it": "La Luna, con un raggio condotto al centro della Terra, descrive un’area proporzionale al tempo.",
    "en": "That the moon, by a radius drawn to the earth's centre, describes an area proportional to the time of description."
   },
   "passi": [],
   "nota": "La prova: velocità areale ∝ ω/δ² (ω moto apparente, δ diametro apparente), quindi ω ∝ δ². Nota N11."
  }
 ]
}
```
