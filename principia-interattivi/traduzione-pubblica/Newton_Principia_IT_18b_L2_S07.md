> **Copia pubblica.** In questa versione i campi `"la"` della Parte B sono vuoti: le frasi latine vengono dalla trascrizione del Newton Project, che non si ridistribuisce. Il latino del 1726 si legge su newtonproject.ox.ac.uk.

# Isaac Newton
# Principi matematici della filosofia naturale

## Fascicolo 18b — Libro II, Sezione VII (seconda parte): Lemmi V–VII, Proposizioni XXXVIII–XL e lo Scolio degli esperimenti di caduta

**Nuova traduzione italiana di lavoro dal latino del 1726, confrontata con l’inglese di Andrew Motte nell’edizione del 1846.**

Versione 0.1 — 8 novembre 2026. Preparata con Claude (Anthropic) per Massimo Bosetti.

### Stato e perimetro

Questo fascicolo copre la **seconda parte della Sezione VII** del Libro II, *De motu fluidorum & resistentia projectilium*. La prima parte (titolo della Sezione, Propp. XXXII–XXXVII con il Lemma IV e lo Scolio della Prop. XXXVII) è affidata a un altro traduttore (Fascicolo 18a). Qui si traduce integralmente il testo dal **Lemma V** alla fine della Sezione: i Lemmi V, VI e VII con il loro Scolio; la Prop. XXXVIII con i Corollari 1–4; la Prop. XXXIX con il suo Scolio; la Prop. XL con la tabella della caduta in un fluido resistente; il grande **Scolio** finale con i quattordici esperimenti di caduta di globi nell’acqua e nell’aria (comprese le prove dalla cupola di San Paolo del 1710 e del 1719) e le quattro tabelle numeriche. È una traduzione di lavoro, non un’edizione critica validata.

Gli identificatori **II.S7.65–II.S7.130** e i titoli tematici tra parentesi sono aggiunte editoriali. La numerazione prosegue senza buchi quella del Fascicolo 18a (che termina con II.S7.64). Da II.S7.100 in poi il numero ha tre cifre. I numeri romani delle proposizioni e dei lemmi, i numeri dei corollari e degli esperimenti appartengono al testo originale. Le integrazioni del curatore sono tra parentesi quadre. Le note poste dopo la traduzione non fanno parte del testo di Newton.

In coda al fascicolo c’è la **Parte B**, con i dati strutturati di cinque unità: Prop. XXXVIII, il suo Cor. 2, Prop. XL (con i dati della tabella) e due calcoli esemplari dello Scolio (Esper. 1 nell’acqua ed Esper. 13 nell’aria). In questa parte della Sezione non ci sono figure.

### Fonti effettivamente consultate

1. **Latino di riferimento.** Isaac Newton, *Philosophiæ Naturalis Principia Mathematica*, terza edizione, Londra, 1726, Libro II, Sezione VII, **pp. 340–356** (Lemma V a p. 340; i marcatori di pagina della trascrizione nella parte tradotta vanno da ‹341› a ‹356›; ‹357› chiude la Sezione). Trascrizione normalizzata del Newton Project, estratta in testo semplice senza correzioni: `fonti/latino-1726-L2-S07.md`, righe 168–402.
2. **Inglese di confronto.** *Newton’s Principia*, traduzione di Andrew Motte, New York, Daniel Adee, 1846, Book II, Section VII, dal Lemma V alla fine: `fonti/motte-1846-L2-S07.md`, righe 943–1939 (Project Gutenberg n. 76404). L’estratto non contiene marcatori di pagina: per Motte si indica la «sezione corrispondente». Ho controllato l’inizio di `fonti/motte-1846-L2-S08.md`: la Sezione VII di Motte si chiude per intero nel file della Sezione VII (ultima frase: «…in proportion to the densities of those fluids.»), e il file della Sezione VIII comincia con il titolo della Sezione VIII. Nel check il secondo file è comunque passato come `--en`, come richiesto. Le formule e i numeri frazionari stampati come immagini compaiono come `[SVG n]`. In un secondo tempo il coordinatore ha reso disponibile l’EPUB estratto (`/home/claude/src_epub/OEBPS/`) e la tabella numero→LaTeX (`svg_tex.tsv`, attributo `data-tex` dell’EPUB): ho controllato **tutti i 187 SVG** della mia parte sulla tabella LaTeX e ho reso con `rsvg-convert` e guardato 31 immagini (le formule della Prop. XL e dello Scolio finale e tutti i casi dubbi), che concordano con il LaTeX (esito in A.15).
3. **Altre parti della trascrizione**, consultate solo per verificare i rimandi interni: `fonti/latino-1726-L2-S07.md` (Prop. XXXV, Cor. 7; Prop. XXXVI, Cor. 7; Prop. XXXVII e Cor. 2; Propp. XXXII–XXXIII), `fonti/latino-1726-L2-S02.md` (Prop. IX e corollari), `fonti/latino-1726-L2-S06.md` (Scolio generale della Sezione VI, esperimenti dei pendoli).
4. **Brief comune** (`strumenti/BRIEF.md`), **istruzioni del Libro II** (`ISTRUZIONI-TRADUTTORE.md`), **Fascicoli 3 e 5** come modelli di formato.

Non ho consultato né riprodotto traduzioni moderne. Non ho potuto vedere la stampa del 1726 né Motte 1729.

### Criteri di traduzione

- Il testo guida è il latino; l’inglese di Motte serve a controllare le interpretazioni ed è annotato quando aggiunge, omette o si discosta.
- Si applica il **glossario comune** del brief e il **glossario del Libro II**: *resistentia* «resistenza», *medium* «mezzo», *fluidum* «fluido», *densitas* «densità», *compressio* «compressione», *in duplicata ratione velocitatis* «in rapporto duplicato della velocità», *ratio subduplicata* «rapporto subduplicato», *vacuum* «vuoto», *globus* «globo», *cylindrus* «cilindro», *sphæra* «sfera», *canalis* «canale», *vas* «vaso», *pondus* «peso», *gravitas* «gravità», *aer* «aria», *aqua pluvialis* «acqua piovana», *argentum vivum* «mercurio» (alla prima occorrenza «mercurio (argento vivo)»), *cera, plumbum, vitrum* «cera, piombo, vetro», *pes Londinensis* «piede londinese», *digitus* «pollice», *granum* «grano», *uncia* «oncia», *libra* «libbra», *minutum secundum* «secondo», *pendulum* «pendolo», *oscillatio* «oscillazione», *vibrare* «vibrare», *logarithmus* «logaritmo», *experimentum* «esperimento», *Scholium* «Scolio», *quamproxime* «con ottima approssimazione», *perpetuo* «continuamente», *impulsus* «impulso», *ictus* «urto».
- *Motus*, quando indica la grandezza (*totus ejus motus … tolli possit vel generari*; *motus sui partem amittere*), è reso «quantità di moto», secondo il glossario; quando indica il fenomeno (*motus oscillatorius*, *motum cient in fluido*) è reso «moto».
- Le estensioni del glossario proprie di questo fascicolo sono elencate e motivate nel § A.0.
- Gli enunciati latini all’infinito o al congiuntivo sono resi con l’indicativo; l’enunciato del problema (Prop. XL) con l’infinito.
- **Numeri.** La virgola decimale della stampa (0,84224) è conservata, perché coincide con l’uso italiano. Le frazioni, appiattite dalla trascrizione («15614» = 156 ¼, «1561338» = 156 13/38), sono ricostruite e scritte con i caratteri ½ ¼ ¾ ⅓ ⅔ ⅛ ⅜ ⅝ ⅞ o, per le altre, nella forma «156 13/38»; ogni ricostruzione è dichiarata nel § A.13 e controllata con l’aritmetica (note N7–N12). I tempi sono scritti come nella stampa: ″ secondi, ‴ terzi (sessantesimi di secondo), ⁗ quarti.
- Le formule appiattite della Prop. XL («2PFG», «N−1N+1H») sono scritte con la barra (2PF/G, (N − 1)H/(N + 1)) e dichiarate nell’apparato. Nessuna formula moderna entra nel testo tradotto.
- **Tabelle.** Le quattro tabelle sono riprodotte per intero come tabelle Markdown, con le cifre della trascrizione (frazioni ricostruite). Le cifre che non tornano con il calcolo sono segnalate nelle note, **non corrette nel testo**.

---
## Traduzione italiana

### Sezione VII (seconda parte). Il moto dei fluidi e la resistenza dei proiettili

### Lemma V (cilindro, sfera e sferoide in un canale)

**[II.S7.65]** **Se un cilindro, una sfera e uno sferoide, le cui larghezze sono uguali, si collocano uno dopo l’altro nel mezzo di un canale cilindrico, in modo che i loro assi coincidano con l’asse del canale, questi corpi ostacolano in egual misura il flusso dell’acqua attraverso il canale.**

**[II.S7.66]** Infatti gli spazi fra il canale e il cilindro, la sfera e lo sferoide, attraverso i quali l’acqua passa, sono uguali; e attraverso spazi uguali l’acqua passa in egual misura.

**[II.S7.67]** Queste cose stanno così nell’ipotesi che sia congelata tutta l’acqua sopra il cilindro, la sfera o lo sferoide la cui fluidità non è richiesta per il passaggio più rapido dell’acqua, come ho spiegato nel Cor. VII della Prop. XXXVI.

### Lemma VI (la spinta dell’acqua che scorre)

**[II.S7.68]** **Nelle stesse ipotesi, i corpi predetti sono sollecitati in egual misura dall’acqua che scorre attraverso il canale.**

**[II.S7.69]** È evidente per il Lemma V e per la terza legge del moto. L’acqua e i corpi, infatti, agiscono gli uni sugli altri in egual misura.

### Lemma VII (i corpi che si muovono nell’acqua in quiete)

**[II.S7.70]** **Se l’acqua è in quiete nel canale, e questi corpi sono portati attraverso il canale verso la parte contraria con velocità uguale, le loro resistenze sono uguali fra loro.**

**[II.S7.71]** Risulta dal lemma precedente, perché i moti relativi restano gli stessi fra loro.

### Scolio (corpi rotondi, fluidi elastici, corpi galleggianti)

**[II.S7.72]** La stessa ragione vale per tutti i corpi convessi e rotondi i cui assi coincidono con l’asse del canale. Qualche differenza può nascere da un attrito maggiore o minore; ma in questi lemmi supponiamo che i corpi siano levigatissimi, che la tenacità e l’attrito del mezzo siano nulli, e che le parti del fluido che con i loro moti obliqui e superflui possono perturbare, ostacolare e ritardare il flusso dell’acqua attraverso il canale siano in quiete fra loro, come strette dal gelo, e aderiscano ai corpi nelle loro parti anteriori e posteriori, così come ho esposto nello scolio della proposizione precedente. Nel seguito, infatti, si tratta della minima fra tutte le resistenze che possono avere i corpi rotondi descritti con sezioni trasversali massime date.

**[II.S7.73]** I corpi che galleggiano sui fluidi, quando si muovono in linea retta, fanno sì che il fluido salga nella parte anteriore e si abbassi nella posteriore, soprattutto se sono di figura ottusa; e perciò subiscono una resistenza un poco maggiore che se fossero acuti di testa e di coda. E i corpi mossi in fluidi elastici, se sono ottusi davanti e dietro, condensano il fluido un poco di più nella parte anteriore e lo diradano un poco di più nella posteriore; e perciò subiscono una resistenza un poco maggiore che se fossero acuti di testa e di coda. Ma noi, in questi lemmi e proposizioni, non trattiamo dei fluidi elastici, ma dei non elastici; non dei corpi che stanno sopra il fluido, ma di quelli profondamente immersi. E quando si conosce la resistenza dei corpi nei fluidi non elastici, si dovrà accrescere un poco questa resistenza tanto nei fluidi elastici, come l’aria, quanto nelle superfici dei fluidi stagnanti, come i mari e le paludi.

### Proposizione XXXVIII. Teorema XXX (la resistenza di un globo in un fluido infinito)

**[II.S7.74]** **La resistenza di un globo che avanza uniformemente in un fluido compresso, infinito e non elastico sta alla forza con cui tutta la sua quantità di moto potrebbe essere tolta o generata nel tempo in cui descrive gli otto terzi del suo diametro, come la densità del fluido sta alla densità del globo, con ottima approssimazione.**

**[II.S7.75]** Il globo, infatti, sta al cilindro circoscritto come due sta a tre; e perciò quella forza che potrebbe togliere tutta la quantità di moto del cilindro mentre il cilindro descrive la lunghezza di quattro diametri toglierà tutta la quantità di moto del globo mentre il globo descrive i due terzi di questa lunghezza, cioè gli otto terzi del proprio diametro. Ora la resistenza del cilindro sta a questa forza, con ottima approssimazione, come la densità del fluido sta alla densità del cilindro o del globo, per la Prop. XXXVII; e la resistenza del globo è uguale alla resistenza del cilindro, per i Lemmi V, VI e VII. C.V.D.

**[II.S7.76]** *Cor. 1.* Le resistenze dei globi in mezzi compressi infiniti stanno nel rapporto composto dal rapporto duplicato della velocità, dal rapporto duplicato del diametro e dal rapporto della densità dei mezzi.

**[II.S7.77]** *Cor. 2.* La velocità massima con cui un globo, per la forza del suo peso comparativo, può scendere in un fluido resistente è quella che lo stesso globo, con lo stesso peso, può acquistare cadendo senza resistenza e descrivendo nella sua caduta uno spazio che stia ai quattro terzi del suo diametro come la densità [del globo sta alla densità] del fluido. Infatti il globo, nel tempo della sua caduta, con la velocità acquistata cadendo, descriverà uno spazio che starà agli otto terzi del suo diametro come la densità del globo sta alla densità del fluido; e la forza del peso che genera questo moto starà alla forza che potrebbe generare lo stesso moto nel tempo in cui il globo descrive con la stessa velocità gli otto terzi del suo diametro, come la densità del fluido sta alla densità del globo; e perciò, per questa proposizione, la forza del peso sarà uguale alla forza della resistenza, e quindi non può accelerare il globo.

**[II.S7.78]** *Cor. 3.* Date la densità del globo e la sua velocità all’inizio del moto, come pure la densità del fluido compresso in quiete nel quale il globo si muove, sono date per ogni tempo sia la velocità del globo, sia la sua resistenza, sia lo spazio da esso descritto, per il Cor. VII della Prop. XXXV.

**[II.S7.79]** *Cor. 4.* Un globo che si muove in un fluido compresso in quiete della sua stessa densità perderà metà della sua quantità di moto prima di aver descritto la lunghezza di due suoi diametri, per lo stesso Cor. VII.

### Proposizione XXXIX. Teorema XXXI (il globo in un canale cilindrico)

**[II.S7.80]** **La resistenza di un globo che avanza uniformemente attraverso un fluido chiuso e compresso in un canale cilindrico sta alla forza con cui tutta la sua quantità di moto potrebbe essere generata o tolta mentre descrive gli otto terzi del suo diametro, nel rapporto composto dal rapporto dell’orifizio del canale all’eccesso di questo orifizio sulla metà del cerchio massimo del globo, dal rapporto duplicato dell’orifizio del canale all’eccesso di questo orifizio sul cerchio massimo del globo, e dal rapporto della densità del fluido alla densità del globo, con ottima approssimazione.**

**[II.S7.81]** È evidente per il Cor. 2 della Prop. XXXVII; e la dimostrazione procede come nella proposizione precedente.

### Scolio (l’acqua congelata davanti al globo)

**[II.S7.82]** Nelle due ultime proposizioni (come nel Lemma V) suppongo che sia congelata tutta l’acqua che precede il globo e la cui fluidità aumenta la resistenza del globo. Se tutta quell’acqua si scioglie, la resistenza aumenterà un poco. Ma quell’aumento, in queste proposizioni, sarà piccolo e si può trascurare, perché la superficie convessa del globo fa interamente l’ufficio del ghiaccio.

### Proposizione XL. Problema IX (la resistenza dai fenomeni)

**[II.S7.83]** **Trovare dai fenomeni la resistenza di un globo che avanza in un mezzo fluidissimo compresso.**

**[II.S7.84]** Sia A il peso del globo nel vuoto, B il suo peso nel mezzo resistente, D il diametro del globo, F uno spazio che stia a 4/3 D come la densità del globo sta alla densità del mezzo, cioè come A sta ad A − [B], G il tempo in cui il globo, cadendo senza resistenza con il peso B, descrive lo spazio F, e H la velocità che il globo acquista in questa sua caduta. Allora H sarà la velocità massima con cui il globo, con il suo peso B, può scendere nel mezzo resistente, per il Cor. 2 della Prop. XXXVIII; e la resistenza che il globo subisce scendendo con quella velocità sarà uguale al suo peso B; la resistenza che subisce con qualsiasi altra velocità starà invece al peso B nel rapporto duplicato di questa velocità alla velocità massima H, per il Cor. 1 della Prop. XXXVIII.

**[II.S7.85]** Questa è la resistenza che nasce dall’inerzia della materia del fluido. Quella che nasce dall’elasticità, dalla tenacità e dall’attrito delle sue parti si indagherà così.

**[II.S7.86]** Si lasci andare il globo in modo che scenda nel fluido per il suo peso B; e sia P il tempo di caduta, espresso in secondi se il tempo G è espresso in secondi. Si trovi il numero assoluto N che corrisponde al logaritmo 0,4342944819 × 2P/G, e sia L il logaritmo del numero (N + 1)/N: la velocità acquistata cadendo sarà (N − 1)H/(N + 1), e l’altezza descritta sarà 2PF/G − 1,3862943611F + 4,605170186LF. Se il fluido è abbastanza profondo, si può trascurare il termine 4,605170186LF; e 2PF/G − 1,3862943611F sarà l’altezza descritta, con ottima approssimazione. Queste cose sono evidenti per la Prop. IX del Libro II e i suoi corollari, nell’ipotesi che il globo non subisca altra resistenza che quella che nasce dall’inerzia della materia. Se invece subisce in più un’altra resistenza, la discesa sarà più lenta, e dal ritardo si conoscerà la quantità di questa resistenza.

**[II.S7.87]** Perché si conoscano più facilmente la velocità e la discesa di un corpo che cade in un fluido, ho composto la tabella seguente. La prima colonna indica i tempi di discesa; la seconda presenta le velocità acquistate cadendo, essendo la velocità massima 100000000; la terza presenta gli spazi descritti cadendo in quei tempi, essendo 2F lo spazio che il corpo descrive nel tempo G con la velocità massima; e la quarta presenta gli spazi descritti negli stessi tempi con la velocità massima. I numeri della quarta colonna sono 2P/G, e sottraendo il numero 1,3862944 − 4,6051702L si trovano i numeri della terza colonna; e questi numeri vanno moltiplicati per lo spazio F per avere gli spazi descritti cadendo. A queste si è aggiunta inoltre una quinta colonna, che contiene gli spazi descritti negli stessi tempi da un corpo che cade nel vuoto per la forza del suo peso comparativo B.

**[II.S7.88]** *Tabella.*

| Tempi P | Velocità di chi cade nel fluido | Spazi descritti cadendo nel fluido | Spazi descritti con il moto massimo | Spazi descritti cadendo nel vuoto |
|---|---|---|---|---|
| 0,001 G | 99999 29/30 | 0,000001 F | 0,002 F | 0,000001 F |
| 0,01 G | 999967 | 0,0001 F | 0,02 F | 0,0001 F |
| 0,1 G | 9966799 | 0,0099834 F | 0,2 F | 0,01 F |
| 0,2 G | 19737532 | 0,0397361 F | 0,4 F | 0,04 F |
| 0,3 G | 29131261 | 0,0886815 F | 0,6 F | 0,09 F |
| 0,4 G | 37994896 | 0,1559070 F | 0,8 F | 0,16 F |
| 0,5 G | 46211716 | 0,2402290 F | 1,0 F | 0,25 F |
| 0,6 G | 53704957 | 0,3402706 F | 1,2 F | 0,36 F |
| 0,7 G | 60436778 | 0,4545405 F | 1,4 F | 0,49 F |
| 0,8 G | 66403677 | 0,5815071 F | 1,6 F | 0,64 F |
| 0,9 G | 71629787 | 0,7196609 F | 1,8 F | 0,81 F |
| 1 G | 76159416 | 0,8675617 F | 2 F | 1 F |
| 2 G | 96402758 | 2,6500055 F | 4 F | 4 F |
| 3 G | 99505475 | 4,6186570 F | 6 F | 9 F |
| 4 G | 99932930 | 6,6143765 F | 8 F | 16 F |
| 5 G | 99990920 | 8,6137964 F | 10 F | 25 F |
| 6 G | 99998771 | 10,6137179 F | 12 F | 36 F |
| 7 G | 99999834 | 12,6137073 F | 14 F | 49 F |
| 8 G | 99999980 | 14,6137059 F | 16 F | 64 F |
| 9 G | 99999997 | 16,6137057 F | 18 F | 81 F |
| 10 G | 99999999 3/5 | 18,6137056 F | 20 F | 100 F |

### Scolio (esperimenti di caduta nell’acqua e nell’aria)

#### 1. Il vaso, le unità di misura e i primi esperimenti

**[II.S7.89]** Per indagare con esperimenti le resistenze dei fluidi, preparai un vaso di legno quadrato, di lunghezza e larghezza interne di nove pollici del piede londinese e di profondità di nove piedi e mezzo, e lo riempii di acqua piovana; e, formati dei globi di cera con del piombo racchiuso dentro, notai i tempi di discesa dei globi, essendo l’altezza della discesa di 112 pollici. Il piede cubico solido londinese contiene 76 libbre romane di acqua piovana, e il pollice solido di questo piede contiene 19/36 di oncia di questa libbra, ossia 253 ⅓ grani; e un globo d’acqua descritto con il diametro di un pollice contiene 132,645 grani nel mezzo dell’aria, o 132,8 grani nel vuoto; e qualsiasi altro globo sta come l’eccesso del suo peso nel vuoto sul suo peso nell’acqua.

**[II.S7.90]** *Esper. 1.* Un globo il cui peso era di 156 ¼ grani nell’aria e di 77 grani nell’acqua descrisse l’intera altezza di 112 pollici in un tempo di quattro secondi. E, ripetuto l’esperimento, il globo cadde di nuovo nello stesso tempo di quattro secondi.

**[II.S7.91]** Il peso del globo nel vuoto è di 156 13/38 grani, e l’eccesso di questo peso sul peso del globo nell’acqua è di 79 13/38 grani. Ne risulta il diametro del globo di 0,84224 parti di pollice. Ora, come quell’eccesso sta al peso del globo nel vuoto, così la densità dell’acqua sta alla densità del globo, e così gli otto terzi del diametro del globo (cioè 2,24597 pollici) stanno allo spazio 2F, che perciò sarà di 4,4256 pollici. Il globo, in un tempo di un secondo, cadendo nel vuoto con tutto il suo peso di 156 13/38 grani, descriverà 193 ⅓ pollici; e con il peso di 77 grani, nello stesso tempo, cadendo senza resistenza nell’acqua, descriverà 95,219 pollici; e nel tempo G, che sta a un secondo nel rapporto subduplicato dello spazio F, ossia 2,2128 pollici, a 95,219 pollici, descriverà 2,2128 pollici e acquisterà la velocità massima H con cui può scendere nell’acqua. Il tempo G è dunque di 0″,15244. E in questo tempo G, con quella velocità massima H, il globo descriverà lo spazio 2F di 4,4256 pollici; e perciò in un tempo di quattro secondi descriverà uno spazio di 116,1245 pollici. Si sottragga lo spazio 1,3862944F, ossia 3,0676 pollici, e resterà lo spazio di 113,0569 pollici, che il globo, cadendo nell’acqua in un vaso amplissimo, descriverà in un tempo di quattro secondi. Questo spazio, per la strettezza del predetto vaso di legno, deve essere diminuito nel rapporto composto dal rapporto subduplicato dell’orifizio del vaso all’eccesso di questo orifizio sul semicerchio massimo del globo e dal rapporto semplice dello stesso orifizio al suo eccesso sul cerchio massimo del globo, cioè nel rapporto di 1 a 0,9914. Fatto ciò, si avrà lo spazio di 112,08 pollici, che il globo, cadendo nell’acqua in questo vaso di legno, avrebbe dovuto descrivere secondo la teoria in un tempo di quattro secondi, con ottima approssimazione. Per esperimento, invece, ne descrisse 112.

**[II.S7.92]** *Esper. 2.* Tre globi uguali, i cui pesi erano, ciascuno, di 76 ⅓ grani nell’aria e di 5 1/16 grani nell’acqua, venivano lasciati cadere uno dopo l’altro; e ciascuno cadde nell’acqua in un tempo di quindici secondi, descrivendo nella sua caduta l’altezza di 112 pollici.

**[II.S7.93]** Facendo il calcolo risultano: il peso del globo nel vuoto, 76 5/12 grani; l’eccesso di questo peso sul peso nell’acqua, 71 17/48 grani; il diametro del globo, 0,81296 pollici; gli otto terzi di questo diametro, 2,16789 pollici; lo spazio 2F, 2,3217 pollici; lo spazio che il globo, con il peso di 5 1/16 grani, descriverebbe in 1″ cadendo senza resistenza, 12,808 pollici; e il tempo G, 0″,301056. Il globo, dunque, con la velocità massima con cui può scendere nell’acqua per la forza del peso di 5 1/16 grani, descriverà nel tempo di 0″,301056 lo spazio di 2,3217 pollici, e nel tempo di 15″ lo spazio di 115,678 pollici. Si sottragga lo spazio 1,3862944F, ossia 1,609 pollici, e resterà lo spazio di 114,069 pollici, che perciò il globo deve descrivere nello stesso tempo cadendo in un vaso larghissimo. Per la strettezza del nostro vaso si deve togliere uno spazio di circa 0,895 pollici. E così resterà lo spazio di 113,174 pollici, che il globo, cadendo in questo vaso, avrebbe dovuto descrivere nel tempo di 15″ secondo la teoria, con ottima approssimazione. Per esperimento, invece, ne descrisse 112. La differenza è insensibile.

**[II.S7.94]** *Esper. 3.* Tre globi uguali, i cui pesi erano, ciascuno, di 121 grani nell’aria e di 1 grano nell’acqua, venivano lasciati cadere uno dopo l’altro; e cadevano nell’acqua nei tempi di 46″, 47″ e 50″, descrivendo l’altezza di 112 pollici.

**[II.S7.95]** Secondo la teoria questi globi avrebbero dovuto cadere in un tempo di circa 40″. Se il fatto che siano caduti più lentamente si debba attribuire a una proporzione minore, nei moti lenti, della resistenza che nasce dalla forza d’inerzia rispetto alla resistenza che nasce da altre cause, o piuttosto ad alcune bollicine aderenti al globo, o alla rarefazione della cera per il calore del tempo atmosferico o della mano che lasciava cadere il globo, o anche a errori insensibili nel pesare i globi nell’acqua, lo ritengo incerto. Perciò il peso del globo nell’acqua deve essere di più grani, perché l’esperimento sia reso certo e degno di fede.

#### 2. Il secondo vaso: esperimenti 4–7

**[II.S7.96]** *Esper. 4.* Cominciai gli esperimenti descritti fin qui per indagare le resistenze dei fluidi prima che mi fosse nota la teoria esposta nelle proposizioni immediatamente precedenti. In seguito, per esaminare la teoria trovata, preparai un vaso di legno di larghezza interna di 8 ⅔ pollici e di profondità di quindici piedi e un terzo. Poi formai di cera, con del piombo racchiuso, quattro globi, ciascuno del peso di 139 ¼ grani nell’aria e di 7 ⅛ grani nell’acqua. E li lasciai cadere per misurare i tempi di caduta nell’acqua con un pendolo che oscillava a mezzi secondi. I globi, quando venivano pesati e poi quando cadevano, erano freddi ed erano rimasti freddi per qualche tempo; perché il calore rarefà la cera e, con la rarefazione, diminuisce il peso del globo nell’acqua, e la cera rarefatta non è ricondotta subito dal freddo alla densità di prima. Prima che cadessero venivano immersi completamente nell’acqua, perché la loro discesa non fosse accelerata all’inizio dal peso di qualche parte sporgente dall’acqua. E quando, completamente immersi, erano in quiete, venivano lasciati andare con la massima cautela, perché non ricevessero alcun impulso dalla mano che li lasciava. Caddero poi, uno dopo l’altro, in tempi di 47 ½, 48 ½, 50 e 51 oscillazioni, descrivendo l’altezza di quindici piedi e due pollici. Ma il tempo atmosferico era ormai un poco più freddo di quando i globi erano stati pesati, e perciò ripetei l’esperimento un altro giorno, e i globi caddero in tempi di 49, 49 ½, 50 e 53 oscillazioni, e una terza volta in tempi di 49 ½, 50, 51 e 53 oscillazioni. E, ripetuto più volte l’esperimento, i globi caddero per lo più in tempi di 49 ½ e 50 oscillazioni. Quando caddero più lentamente, sospetto che siano stati ritardati urtando contro le pareti del vaso.

**[II.S7.97]** Ora, facendo il calcolo secondo la teoria, risultano: il peso del globo nel vuoto, 139 2/5 grani; l’eccesso di questo peso sul peso del globo nell’acqua, 132 11/40 grani; il diametro del globo, 0,99868 pollici; gli otto terzi del diametro, 2,66315 pollici; lo spazio 2F, 2,8066 pollici; lo spazio che il globo, con il peso di 7 ⅛ grani, descrive in un tempo di un secondo cadendo senza resistenza, 9,88164 pollici; e il tempo G, 0″,376843. Il globo, dunque, con la velocità massima con cui può scendere nell’acqua per la forza del peso di 7 ⅛ grani, descrive nel tempo di 0″,376843 lo spazio di 2,8066 pollici, nel tempo di 1″ lo spazio di 7,44766 pollici, e nel tempo di 25″, ossia di 50 oscillazioni, lo spazio di 186,1915 pollici. Si sottragga lo spazio 1,386294F, ossia 1,9454 pollici, e resterà lo spazio di 184,2461 pollici, che il globo descriverà nello stesso tempo in un vaso larghissimo. Per la strettezza del nostro vaso, si diminuisca questo spazio nel rapporto composto dal rapporto subduplicato dell’orifizio del vaso all’eccesso di questo orifizio sul semicerchio massimo del globo e dal rapporto semplice dello stesso orifizio al suo eccesso sul cerchio massimo del globo; e si avrà lo spazio di 181,86 pollici, che il globo avrebbe dovuto descrivere in questo vaso nel tempo di 50 oscillazioni secondo la teoria, con ottima approssimazione. Per esperimento, invece, descrisse lo spazio di 182 pollici nel tempo di 49 ½ o di 50 oscillazioni.

**[II.S7.98]** *Esper. 5.* Quattro globi del peso di 154 ⅜ grani nell’aria e di 21 ½ grani nell’acqua, lasciati cadere spesso, cadevano in tempi di 28 ½, 29, 29 ½ e 30 oscillazioni, e talvolta di 31, 32 e 33, descrivendo l’altezza di quindici piedi e due pollici.

**[II.S7.99]** Secondo la teoria avrebbero dovuto cadere in un tempo di 29 oscillazioni, con ottima approssimazione.

**[II.S7.100]** *Esper. 6.* Cinque globi del peso di 212 ⅜ grani nell’aria e di 79 ½ nell’acqua, lasciati cadere spesso, cadevano in tempi di 15, 15 ½, 16, 17 e 18 oscillazioni, descrivendo l’altezza di quindici piedi e due pollici.

**[II.S7.101]** Secondo la teoria avrebbero dovuto cadere in un tempo di 15 oscillazioni, con ottima approssimazione.

**[II.S7.102]** *Esper. 7.* Quattro globi del peso di 293 ⅜ grani nell’aria e di 35 ⅞ grani nell’acqua, lasciati cadere spesso, cadevano in tempi di 29 ½, 30, 30 ½, 31, 32 e 33 oscillazioni, descrivendo l’altezza di quindici piedi e un pollice e mezzo.

**[II.S7.103]** Secondo la teoria avrebbero dovuto cadere in un tempo di 28 oscillazioni, con ottima approssimazione.

#### 3. Le oscillazioni dei globi e gli esperimenti 8–12

**[II.S7.104]** Indagando la causa per cui, fra globi dello stesso peso e della stessa grandezza, alcuni cadessero più velocemente e altri più lentamente, giunsi a questa: che i globi, quando venivano lasciati andare e cominciavano a cadere, oscillavano attorno ai loro centri, perché il lato che per caso era più pesante scendeva per primo e generava il moto oscillatorio. Con le sue oscillazioni, infatti, il globo comunica all’acqua una quantità di moto maggiore che se scendesse senza oscillazioni; e, comunicandola, perde parte della propria quantità di moto con cui dovrebbe scendere: e secondo che l’oscillazione è maggiore o minore, è ritardato di più o di meno. Inoltre il globo si allontana sempre dal suo lato che scende nell’oscillazione e, allontanandosi, si avvicina alle pareti del vaso, e talvolta urta contro di esse. E questa oscillazione è più forte nei globi più pesanti, e nei più grandi agita di più l’acqua. Perciò, per rendere minore l’oscillazione dei globi, costruii globi nuovi di cera e piombo, conficcando il piombo in un lato del globo, vicino alla sua superficie; e lasciai cadere il globo in modo che il lato più pesante, per quanto fu possibile, fosse il più basso fin dall’inizio della discesa. Così le oscillazioni divennero molto minori di prima, e i globi caddero in tempi meno disuguali, come negli esperimenti seguenti.

**[II.S7.105]** *Esper. 8.* Quattro globi del peso di 139 grani nell’aria e di 6 ½ nell’acqua, lasciati cadere spesso, caddero in tempi di non più di 52 oscillazioni e non meno di 50, e per lo più in un tempo di circa 51 oscillazioni, descrivendo l’altezza di 182 pollici.

**[II.S7.106]** Secondo la teoria avrebbero dovuto cadere in un tempo di circa 52 oscillazioni.

**[II.S7.107]** *Esper. 9.* Quattro globi del peso di 273 ¼ grani nell’aria e di 140 ¾ nell’acqua, lasciati cadere più volte, caddero in tempi di non meno di 12 oscillazioni e non più di 13, descrivendo l’altezza di 182 pollici.

**[II.S7.108]** Secondo la teoria, invece, questi globi avrebbero dovuto cadere in un tempo di 11 ⅓ oscillazioni, con ottima approssimazione.

**[II.S7.109]** *Esper. 10.* Quattro globi del peso di 384 grani nell’aria e di 119 ½ nell’acqua, lasciati cadere spesso, cadevano in tempi di 17 ¾, 18, 18 ½ e 19 oscillazioni, descrivendo l’altezza di 181 ½ pollici. E quando caddero in un tempo di 19 oscillazioni, talvolta udii il loro impulso contro le pareti del vaso prima che giungessero al fondo.

**[II.S7.110]** Secondo la teoria, invece, avrebbero dovuto cadere in un tempo di 15 5/9 oscillazioni, con ottima approssimazione.

**[II.S7.111]** *Esper. 11.* Tre globi uguali, del peso di 48 grani nell’aria e di 3 29/32 nell’acqua, lasciati cadere spesso, caddero in tempi di 43 ½, 44, 44 ½, 45 e 46 oscillazioni, e per lo più di 44 e 45, descrivendo l’altezza di 182 ½ pollici, con ottima approssimazione.

**[II.S7.112]** Secondo la teoria avrebbero dovuto cadere in un tempo di circa 46 5/9 oscillazioni.

**[II.S7.113]** *Esper. 12.* Tre globi uguali, del peso di 141 grani nell’aria e di 4 ⅜ nell’acqua, lasciati cadere alcune volte, caddero in tempi di 61, 62, 63, 64 e 65 oscillazioni, descrivendo l’altezza di 182 pollici.

**[II.S7.114]** E secondo la teoria avrebbero dovuto cadere in un tempo di 64 ½ oscillazioni, con ottima approssimazione.

**[II.S7.115]** Da questi esperimenti è manifesto che, quando i globi caddero lentamente, come nel secondo, quarto, quinto, ottavo, undicesimo e dodicesimo esperimento, i tempi di caduta sono rappresentati correttamente dalla teoria; ma quando i globi caddero più velocemente, come nel sesto, nono e decimo esperimento, la resistenza risultò un poco maggiore che nel rapporto duplicato della velocità. I globi, infatti, oscillano un poco mentre cadono; e questa oscillazione, nei globi più leggeri e che cadono più lentamente, cessa presto per la debolezza del moto; nei più pesanti e più grandi, invece, per la forza del moto dura più a lungo, e può essere frenata dall’acqua circostante soltanto dopo parecchie oscillazioni. Inoltre i globi, quanto più sono veloci, tanto meno sono premuti dal fluido nelle loro parti posteriori; e se la velocità aumenta continuamente, lasceranno alla fine uno spazio vuoto dietro di sé, a meno che la compressione del fluido non aumenti nello stesso tempo. Ora la compressione del fluido (per le Propp. XXXII e XXXIII) deve aumentare nel rapporto duplicato della velocità, perché la resistenza sia nello stesso rapporto duplicato. Poiché ciò non avviene, i globi più veloci sono premuti un poco meno da dietro, e per il difetto di questa pressione la loro resistenza diventa un poco maggiore che nel rapporto duplicato della velocità.

**[II.S7.116]** La teoria concorda dunque con i fenomeni dei corpi che cadono nell’acqua; resta che esaminiamo i fenomeni di quelli che cadono nell’aria.

#### 4. Esperimento 13: la cupola di San Paolo, giugno 1710

**[II.S7.117]** *Esper. 13.* Dalla sommità della chiesa di San Paolo, nella città di Londra, nel mese di giugno del 1710, venivano lasciati cadere insieme due globi di vetro, uno pieno di mercurio (argento vivo), l’altro d’aria; e cadendo descrivevano l’altezza di 220 piedi londinesi. Una tavola di legno era sospesa, a un suo estremo, a perni di ferro, e all’altro poggiava su un chiavistello di legno; e i due globi, posti su questa tavola, venivano lasciati cadere insieme sfilando il chiavistello per mezzo di un filo di ferro che scendeva fino a terra, in modo che la tavola, appoggiata soltanto ai perni di ferro, ruotasse attorno a essi; e nello stesso istante un pendolo che oscillava a secondi, tirato da quel filo di ferro, veniva lasciato andare e cominciava a oscillare. I diametri e i pesi dei globi e i tempi di caduta sono presentati nella tabella seguente.

**[II.S7.118]** *Tabella.*

| Globi pieni di mercurio: pesi | diametri | tempi di caduta | Globi pieni d’aria: pesi | diametri | tempi di caduta |
|---|---|---|---|---|---|
| 908 grani | 0,8 pollici | 4″ | 510 grani | 5,1 pollici | 8 ½″ |
| 983 | 0,8 | 4 − | 642 | 5,2 | 8 |
| 866 | 0,8 | 4 | 599 | 5,1 | 8 |
| 747 | 0,75 | 4 + | 515 | 5,0 | 8 ¼ |
| 808 | 0,75 | 4 | 483 | 5,0 | 8 ½ |
| 784 | 0,75 | 4 + | 641 | 5,2 | 8 |

**[II.S7.119]** Del resto i tempi osservati devono essere corretti. Infatti i globi di mercurio (secondo la teoria di Galileo) in quattro secondi descriveranno 257 piedi londinesi, e 220 piedi in soli 3″ 42‴. La tavola di legno, appunto, tolto il chiavistello, ruotava più lentamente di quanto avrebbe dovuto, e con la sua lenta rotazione ostacolava all’inizio la discesa dei globi. I globi, infatti, poggiavano sulla tavola vicino al suo mezzo, ed erano anzi un poco più vicini al suo asse che al chiavistello. E perciò i tempi di caduta furono prolungati di circa diciotto terzi, e ora devono essere corretti togliendo quei terzi, soprattutto nei globi più grandi, che per la grandezza dei diametri rimanevano appoggiati un po’ più a lungo sulla tavola che ruotava. Fatto ciò, i tempi in cui caddero i sei globi più grandi diventeranno 8″ 12‴, 7″ 42‴, 7″ 42‴, 7″ 57‴, 8″ 12‴ e 7″ 42‴.

**[II.S7.120]** Dei globi pieni d’aria, dunque, il quinto, costruito con un diametro di cinque pollici e un peso di 483 grani, cadde nel tempo di 8″ 12‴, descrivendo l’altezza di 220 piedi. Il peso dell’acqua uguale a questo globo è di 16600 grani; e il peso dell’aria uguale allo stesso è di 16600/860 grani, ossia 19 3/10 grani; e perciò il peso del globo nel vuoto è di 502 3/10 grani; e questo peso sta al peso dell’aria uguale al globo come 502 3/10 sta a 19 3/10, e così 2F sta agli otto terzi del diametro del globo, cioè a 13 ⅓ pollici. Ne risulta 2F di 28 piedi e 11 pollici. Il globo, cadendo nel vuoto con tutto il suo peso di 502 3/10 grani, descrive in un tempo di un secondo 193 ⅓ pollici, come sopra; con il peso di 483 grani descrive 185,905 pollici; e con lo stesso peso di 483 grani descrive anche nel vuoto lo spazio F, ossia 14 piedi e 5 ½ pollici, nel tempo di 57‴ 58⁗, e acquista la velocità massima con cui potrebbe scendere nell’aria. Con questa velocità il globo, nel tempo di 8″ 12‴, descriverà lo spazio di 245 piedi e 5 ⅓ pollici. Si tolga 1,3863F, ossia 20 piedi e ½ pollice, e resteranno 225 piedi e 5 pollici. Questo spazio, dunque, il globo avrebbe dovuto descrivere cadendo nel tempo di 8″ 12‴ secondo la teoria. Per esperimento, invece, descrisse lo spazio di 220 piedi. La differenza è insensibile.

**[II.S7.121]** Applicando calcoli simili anche agli altri globi pieni d’aria, ho composto la tabella seguente.

| Pesi dei globi | Diametri | Tempi di caduta dall’altezza di 220 piedi | Spazi da descrivere secondo la teoria | Eccessi |
|---|---|---|---|---|
| 510 grani | 5,1 pollici | 8″ 12‴ | 226 piedi 11 pollici | 6 piedi 11 pollici |
| 642 | 5,2 | 7 42 | 230 9 | 10 9 |
| 599 | 5,1 | 7 42 | 227 10 | 7 10 |
| 515 | 5 | 7 57 | 224 5 | 4 5 |
| 483 | 5 | 8 12 | 225 5 | 5 5 |
| 641 | 5,2 | 7 42 | 230 7 | 10 7 |

#### 5. Esperimento 14: Desaguliers, luglio 1719

**[II.S7.122]** *Esper. 14.* Nell’anno 1719, nel mese di luglio, il signor Desaguliers riprese esperimenti di questo genere, dando forma sferica a vesciche di maiale per mezzo di una sfera di legno concava, che le vesciche, inumidite, erano costrette a riempire quando vi si soffiava dentro l’aria; e lasciando cadere queste vesciche, una volta seccate ed estratte, da un luogo più alto, nella torre rotonda a volta della stessa chiesa, cioè dall’altezza di 272 piedi; e lasciando cadere nello stesso istante anche un globo di piombo il cui peso era di circa due libbre romane. E intanto alcuni, che stavano nella parte più alta della chiesa, dove i globi venivano lasciati cadere, annotavano i tempi totali di caduta, e altri, che stavano a terra, annotavano la differenza dei tempi fra la caduta del globo di piombo e la caduta della vescica. I tempi, poi, erano misurati con pendoli che oscillavano a mezzi secondi. E di quelli che stavano a terra, uno aveva un orologio a molla che vibrava quattro volte per ogni secondo; un altro aveva un’altra macchina, costruita con arte, anch’essa con un pendolo che vibrava quattro volte per ogni secondo. E una macchina simile l’aveva uno di quelli che stavano sulla sommità della chiesa. E questi strumenti erano fatti in modo che i loro moti potessero, a piacere, cominciare o fermarsi.

**[II.S7.123]** Il globo di piombo, poi, cadeva in un tempo di circa quattro secondi e un quarto. E aggiungendo questo tempo alla predetta differenza di tempo, si ricavava il tempo totale in cui la vescica era caduta. I tempi in cui le cinque vesciche caddero dopo la caduta del globo di piombo furono, la prima volta, 14 ¾″, 12 ¾″, 14 ⅝″, 17 ¾″ e 16 ⅞″, e la seconda volta 14 ½″, 14 ¼″, 14″, 19″ e 16 ¾″. Si aggiungano 4 ¼″, cioè il tempo in cui cadde il globo di piombo, e i tempi totali in cui caddero le cinque vesciche furono, la prima volta, 19″, 17″, 18 ⅞″, 22″ e 21 ⅛″; e la seconda volta 18 ¾″, 18 ½″, 18 ¼″, 23 ¼″ e 21″. I tempi annotati sulla sommità della chiesa furono invece, la prima volta, 19 ⅜″, 17 ¼″, 18 ¾″, 22 ⅛″ e 21 ⅝″; e la seconda volta 19″, 18 ⅝″, 18 ⅜″, 24″ e 21 ¼″.

**[II.S7.124]** Del resto le vesciche non sempre cadevano dritte, ma talvolta svolazzavano e oscillavano qua e là durante la caduta. E per questi moti i tempi di caduta furono prolungati, e accresciuti talvolta di mezzo secondo, talvolta di un secondo intero. Caddero invece più dritte la seconda e la quarta vescica la prima volta, e la prima e la terza la seconda volta. La quinta vescica era rugosa, e per le sue rughe era un poco ritardata. Ricavavo i diametri delle vesciche dalle loro circonferenze, misurate con un filo sottilissimo avvolto due volte attorno a esse. E ho confrontato la teoria con gli esperimenti nella tabella seguente, assumendo che la densità dell’aria stia alla densità dell’acqua piovana come 1 a 860, e calcolando gli spazi che i globi avrebbero dovuto descrivere cadendo secondo la teoria.

**[II.S7.125]** *Tabella.*

| Pesi delle vesciche | Diametri | Tempi di caduta dall’altezza di 272 piedi | Spazi da descrivere negli stessi tempi secondo la teoria | Differenza fra teoria ed esperimento |
|---|---|---|---|---|
| 128 grani | 5,28 pollici | 19″ | 271 piedi 11 pollici | − 0 piedi 1 pollice |
| 156 | 5,19 | 17 | 272 0 ½ | + 0 0 ½ |
| 137 ½ | 5,3 | 18 ½ | 272 7 | + 0 7 |
| 97 ½ | 5,26 | 22 | 277 4 | + 5 4 |
| 99 ⅛ | 5 | 21 ⅛ | 282 0 | + 10 0 |

#### 6. Conclusioni: densità dei fluidi, legge della perdita di velocità, spazi celesti

**[II.S7.126]** La resistenza dei globi mossi tanto nell’aria quanto nell’acqua è dunque rappresentata correttamente dalla nostra teoria quasi per intero, ed è proporzionale alla densità dei fluidi, a parità di velocità e di grandezza dei globi.

**[II.S7.127]** Nello scolio aggiunto alla Sezione VI abbiamo mostrato con esperimenti di pendoli che le resistenze di globi uguali e ugualmente veloci, mossi nell’aria, nell’acqua e nel mercurio, stanno come le densità dei fluidi. Lo stesso mostriamo qui in modo più accurato con esperimenti di corpi che cadono nell’aria e nell’acqua. I pendoli, infatti, a ogni oscillazione eccitano nel fluido un moto sempre contrario al moto del pendolo che ritorna; e la resistenza che nasce da questo moto, come anche la resistenza del filo a cui il pendolo era sospeso, hanno reso la resistenza totale del pendolo maggiore della resistenza che risultò dagli esperimenti dei corpi cadenti. Infatti, per gli esperimenti dei pendoli esposti in quello scolio, un globo della stessa densità dell’acqua, descrivendo nell’aria la lunghezza del suo semidiametro, dovrebbe perdere la parte 1/3342 della sua quantità di moto. Ma per la teoria esposta in questa settima sezione e confermata dagli esperimenti dei corpi cadenti, lo stesso globo, descrivendo la stessa lunghezza, dovrebbe perdere soltanto la parte 1/4586 della sua quantità di moto, posto che la densità dell’acqua stia alla densità dell’aria come 860 a 1. Le resistenze, dunque, risultarono maggiori (per le cause già descritte) dagli esperimenti dei pendoli che dagli esperimenti dei globi cadenti, e ciò nel rapporto di circa 4 a 3. Tuttavia, poiché le resistenze dei pendoli che oscillano nell’aria, nell’acqua e nel mercurio sono accresciute in modo simile da cause simili, la proporzione delle resistenze in questi mezzi sarà presentata abbastanza correttamente tanto dagli esperimenti dei pendoli quanto dagli esperimenti dei corpi cadenti. E di qui si può concludere che le resistenze dei corpi mossi in fluidi qualsiasi, per quanto fluidissimi, sono, a parità delle altre condizioni, come le densità dei fluidi.

**[II.S7.128]** Stabilite queste cose, si può ormai dire, con ottima approssimazione, quale parte della sua quantità di moto un globo qualsiasi, lanciato in un fluido qualsiasi, perderà in un tempo dato. Sia D il diametro del globo, V la sua velocità all’inizio del moto, e T il tempo in cui il globo, con la velocità V, descriverà nel vuoto uno spazio che stia allo spazio 8/3 D come la densità del globo sta alla densità del fluido: il globo lanciato in quel fluido, in un altro tempo qualsiasi t, perderà la parte tV/(T + t) della sua velocità, restandone la parte TV/(T + t), e descriverà uno spazio che starà allo spazio descritto nel vuoto nello stesso tempo con la velocità uniforme V come il logaritmo del numero (T + t)/T, moltiplicato per il numero 2,302585093, sta al numero t/T, per il Cor. VII della Prop. XXXV. Nei moti lenti la resistenza può essere un poco minore, perché la figura del globo è un poco più adatta al moto della figura di un cilindro descritto con lo stesso diametro. Nei moti veloci la resistenza può essere un poco maggiore, perché l’elasticità e la compressione del fluido non aumentano nel rapporto duplicato della velocità. Ma minuzie di questo genere qui non le soppeso.

**[II.S7.129]** E anche se l’aria, l’acqua, il mercurio e i fluidi simili, per la divisione delle parti all’infinito, si assottigliassero e diventassero mezzi infinitamente fluidi, non per questo resisterebbero meno ai globi lanciati. Infatti la resistenza di cui si tratta nelle proposizioni precedenti nasce dall’inerzia della materia; e l’inerzia della materia è essenziale ai corpi ed è sempre proporzionale alla quantità di materia. Per la divisione delle parti del fluido, la resistenza che nasce dalla tenacità e dall’attrito delle parti può certo diminuire; ma la quantità di materia non diminuisce per la divisione delle sue parti; e, restando la quantità di materia, resta la sua forza d’inerzia, alla quale la resistenza di cui qui si tratta è sempre proporzionale. Perché questa resistenza diminuisca, deve diminuire la quantità di materia negli spazi attraverso i quali i corpi si muovono. E perciò gli spazi celesti, attraverso i quali i globi dei pianeti e delle comete si muovono continuamente in tutte le direzioni, liberissimamente e senza alcuna diminuzione sensibile del moto, sono privi di ogni fluido corporeo, eccettuati forse vapori estremamente tenui e i raggi di luce che li attraversano.

**[II.S7.130]** I proiettili, appunto, avanzando eccitano un moto nei fluidi; e questo moto nasce dall’eccesso della pressione del fluido sulle parti anteriori del proiettile rispetto alla pressione sulle sue parti posteriori, e non può essere minore nei mezzi infinitamente fluidi che nell’aria, nell’acqua e nel mercurio, in proporzione alla densità della materia in ciascuno. E questo eccesso di pressione, in proporzione alla sua quantità, non soltanto eccita un moto nel fluido, ma agisce anche sul proiettile per ritardarne il moto; e perciò la resistenza in ogni fluido è come il moto eccitato nel fluido dal proiettile, e non può essere minore nell’etere sottilissimo, in proporzione alla densità dell’etere, che nell’aria, nell’acqua e nel mercurio, in proporzione alle densità di questi fluidi.

---
## Apparato

### A.0 Estensioni del glossario

I termini seguenti non comparivano nel glossario comune né in quello del Libro II. Ognuno è reso in modo costante in tutto il fascicolo. Quelli marcati † sono segnalati al coordinatore per l’armonizzazione con il Fascicolo 18a e con gli altri fascicoli del Libro II.

| Latino | Italiano | Motivazione |
|---|---|---|
| *sphærois* † | «sferoide» | Lemma V. Termine geometrico corrente; Motte «spheroid». |
| *latitudo* (dei corpi, del vaso) | «larghezza» | Lemma V (*quorum latitudines sunt æquales*) e Scolio (*latitudine interna*). Nel Lemma è il diametro trasversale massimo. |
| *orificium* † | «orifizio» | Prop. XXXIX e Scolio: la sezione del canale o del vaso, come area. Tenuto distinto da *foramen* «foro» (glossario del coordinatore), che nella Prop. XXXVI è il buco nel fondo del vaso. Motte «orifice». |
| *circulus maximus globi*; *semicirculus maximus* | «cerchio massimo del globo»; «semicerchio massimo» | La sezione equatoriale del globo e la sua metà. Nella Prop. XXXIX il latino ha *dimidium circuli maximi* («metà del cerchio massimo»), nello Scolio *semicirculum maximum*: rese diverse per forme diverse, stesso significato. |
| *congelari*; *gelu constrictæ*; *glacies*; *liquescere* | «essere congelata»; «strette dal gelo»; «ghiaccio»; «sciogliersi» | Lemma V, Scolio dei Lemmi, Scolio della Prop. XXXIX: l’acqua «inutile» immaginata immobile, come nella Prop. XXXVI. |
| *tenacitas*; *frictio* | «tenacità»; «attrito» | Scolio dei Lemmi e Prop. XL: oggi diremmo viscosità e attrito (nota N1). Si conserva «tenacità». |
| *inertia materiæ*; *vis inertiæ* † | «inerzia della materia»; «forza d’inerzia» | Prop. XL e Scolio. «Forza d’inerzia» come nel Fascicolo 1 (Def. III). Motte rende entrambe con «inactivity» (A.14). |
| *pondus comparativum* † | «peso comparativo» | Prop. XXXVIII, Cor. 2 e Prop. XL: il peso del globo nel fluido, cioè il peso nel vuoto meno il peso del fluido spostato (B = A − peso del fluido). Calco del latino; Motte «comparative weight». |
| *fluidissimus* | «fluidissimo» | Prop. XL e Scolio; superlativo assoluto conservato. Motte «perfectly fluid», «of the most extreme fluidity». |
| *celeritas*; *velocitas* | — ; «velocità» | Nel Lemma V compare solo *celerrimus transitus* («il passaggio più rapido»). |
| *obtusus*; *acutus*; *caput & cauda*; *pars antica / postica* | «ottuso»; «acuto»; «testa e coda»; «parte anteriore / posteriore» | Scolio dei Lemmi; le stesse coppie ricorrono nello Scolio finale (*a tergo*, «da dietro»). |
| *condensare*; *relaxare* | «condensare»; «diradare» | Scolio dei Lemmi: l’opposto di condensare; «rilassare» non sarebbe chiaro. |
| *numerus absolutus*; *logarithmo congruere* | «numero assoluto»; «corrispondere al logaritmo» | Prop. XL: il numero (antilogaritmo) che ha per logaritmo decimale il valore dato. |
| *minutum tertium*; *minutum quartum* † | «terzo» (‴); «quarto» (⁗) | Scolio, Esper. 13: sessantesimi di secondo e sessantesimi di terzo, come nella stampa (8″ 12‴; 57‴ 58⁗). |
| *oscillatio* (unità di tempo) | «oscillazione» | Esper. 4–12: il pendolo batte i mezzi secondi (*ad semi-minuta secunda oscillans*), quindi 50 oscillazioni = 25″, come dice il testo stesso in II.S7.97. |
| *pes solidus cubicus*; *digitus solidus* | «piede cubico solido»; «pollice solido» | Scolio, II.S7.89: unità di volume. |
| *libra Romana* † | «libbra romana» | II.S7.89 e II.S7.122. Il testo stesso dà 1 pollice cubo d’acqua = 19/36 di oncia = 253 ⅓ grani: dunque 12 once e 5760 grani per libbra (nota N7). Motte rende «troy weight» (A.14). Si conserva l’aggettivo del latino. |
| *globus aqueus* | «globo d’acqua» | II.S7.89: il globo ideale d’acqua di un pollice di diametro, unità di peso dei calcoli. |
| *vas amplissimum / latissimum*; *angustia vasis* | «vaso amplissimo / larghissimo»; «strettezza del vaso» | Esper. 1, 2, 4. |
| *tabula lignea*; *poli ferrei*; *pessulus ligneus* † | «tavola di legno»; «perni di ferro»; «chiavistello di legno» | Esper. 13: il meccanismo di sgancio. *Polus* qui è il perno su cui la tavola ruota (*super iisdem devolveretur*); Motte «iron hinges», «wooden pin». |
| *culmen ecclesiæ*; *summitas / suprema pars templi*; *turris rotunda fornicata* | «sommità della chiesa»; «sommità / parte più alta della chiesa»; «torre rotonda a volta» | Esper. 13–14. *Turris rotunda fornicata* è la torre rotonda coperta a volta, cioè il tamburo con la cupola; Motte «the lantern on the top of the cupola» (A.14). |
| *vesica porci* | «vescica di maiale» | Esper. 14. |
| *horologium cum elatere* † | «orologio a molla» | Esper. 14: *elater* è la molla. Motte non lo rende (A.14). |
| *volitare*; *oscillari hinc inde*; *rugosus* | «svolazzare»; «oscillare qua e là»; «rugoso» | Esper. 14. |
| *D.* (*D. Desaguliers*) | «il signor» | *D.* può valere *Dominus* o *Doctor*; Motte «Dr.». Senza la stampa non si decide: si sceglie la resa più neutra, da verificare (A.16). |
| *tempestas* | «tempo atmosferico» | Esper. 3 e 4: il caldo o il freddo della giornata, non la tempesta. |
| *æther* | «etere» | Ultimo capoverso. |
| *cæteris paribus*; *paribus … velocitatibus ac magnitudinibus* | «a parità delle altre condizioni»; «a parità di velocità e di grandezza» | II.S7.126–127. |

*Impulsus* compare due volte: II.S7.96 (*ne impulsum aliquem a manu demittente acciperent*, «perché non ricevessero alcun impulso dalla mano») e II.S7.109 (*audivi impulsum eorum in latera vasis*, «udii il loro impulso contro le pareti»). In entrambi i casi è un’azione breve che cambia la quantità di moto, e la resa «impulso» è quella prevista dal glossario; nel secondo caso l’italiano suona un poco duro («il loro colpo» sarebbe più naturale): lo segnalo al curatore. *Impingere in latera* è reso «urtare contro le pareti» (II.S7.96, II.S7.104).

### A.1 Lemma V

**Latino:** *Si cylindrus, sphæra & sphærois, quorum latitudines sunt æquales, in medio canalis cylindrici ita locentur successive ut eorum axes cum axe canalis coincidant: hæc corpora fluxum aquæ per canalem æqualiter impedient.*

**Inglese:** “If a cylinder, a sphere, and a spheroid, of equal breadths be placed successively in the middle of a cylindric canal, so that their axes may coincide with the axis of the canal, these bodies will equally hinder the passage of the water through the canal.”

**Scelte.**

- *impedient* (futuro) → «ostacolano»: gli enunciati sono resi con l’indicativo presente, come gli enunciati delle proposizioni.
- *æqualiter* → «in egual misura» (come nel Fascicolo 3 per *æqualiter* nella Legge III).
- *supra cylindrum* → «sopra il cilindro»: si intende l’acqua che sta davanti al corpo rispetto al flusso, che nella Prop. XXXVI scende dall’alto. Motte «above».
- *ut in corol. VII. prop. XXXVI. explicui* → «come ho spiegato nel Cor. VII della Prop. XXXVI». Rimando verificato (A.17).
- **Refusi della trascrizione:** *æqulia* per *æqualia*; *shpæram* per *sphæram* (A.12).

### A.2 Lemma VI

**Latino:** *Iisdem positis, corpora prædicta æqualiter urgentur ab aqua per canalem fluente.*

**Inglese:** “The same supposition remaining, the fore-mentioned bodies are equally acted on by the water flowing through the canal.”

- *urgentur* → «sono sollecitati» (verbo delle forze, come nel Fascicolo 5). Motte «are equally acted on».
- *motus legem tertiam* → «la terza legge del moto». *Utique* → «infatti».

### A.3 Lemma VII

**Latino:** *Si aqua quiescat in canali, & hæc corpora in partes contrarias æquali velocitate per canalem ferantur: æquales erunt eorum resistentiæ inter se.*

**Inglese:** “If the water be at rest in the canal, and these bodies move with equal velocity and the contrary way through the canal, their resistances will be equal among themselves.”

- *in partes contrarias* → «verso la parte contraria»: contraria a quella del flusso del Lemma VI. Il passaggio dal Lemma VI al VII è un’applicazione del Cor. V delle leggi (moti relativi), che il testo non cita: *motus relativi iidem inter se manent*.
- *æquales erunt* → «sono uguali» (enunciato all’indicativo).

### A.4 Scolio dei Lemmi

- *Eadem est ratio* → «la stessa ragione vale»: *ratio* nel senso di «il ragionamento è lo stesso». Motte «The case is the same».
- *perinde ut in scholio propositionis præcedentis exposui* → «così come ho esposto nello scolio della proposizione precedente»: è lo Scolio della Prop. XXXVII (testa e coda di fluido congelato del solido EACFDB), tradotto nel Fascicolo 18a. Verificato sulla trascrizione (righe 164–166).
- *resistentia omnium minima quam corpora rotunda, datis maximis sectionibus transversis descripta, habere possunt* → «la minima fra tutte le resistenze che possono avere i corpi rotondi descritti con sezioni trasversali massime date».
- *non de insidentibus fluido, sed de alte immersis* → «non dei corpi che stanno sopra il fluido, ma di quelli profondamente immersi».
- *tam in fluidis elasticis … quam superficiebus fluidorum stagnantium*: nel secondo membro manca *in* (*quam [in] superficiebus*); costruzione ellittica o omissione, da verificare sulla stampa. La traduzione segue il senso.
- **Refuso:** *que* per *quæ* (*partes fluidi, que motibus suis*). La parola *agi ‹342› mus* è spezzata dal marcatore di pagina.

### A.5 Proposizione XXXVIII

**Latino:** *Globi, in fluido compresso infinito & non elastico uniformiter progredientis, resistentia est ad vim qua totus ejus motus, quo tempore octo tertias partes diametri suæ describit, vel tolli possit vel generari, ut densitas fluidi ad densitatem globi quamproxime.*

**Inglese:** “If a globe move uniformly forward in a compressed, infinite, and non-elastic fluid, its resistance is to the force by which its whole motion may be destroyed or generated, in the time that it describes eight third parts of its diameter, as the density of the fluid to the density of the globe, very nearly.”

**Scelte.**

- *totus ejus motus* → «tutta la sua quantità di moto» (*motus* come grandezza, glossario). Il Fascicolo 18a dovrà usare la stessa resa nella Prop. XXXVII (*vim qua totus ejus motus … vel tolli possit vel generari*): da armonizzare.
- *octo tertias partes diametri* → «gli otto terzi del diametro».
- *quamproxime* → «con ottima approssimazione».
- **Refuso probabile:** *interna dum cylindrus describat* per *interea dum* (Motte «while»). La traduzione segue il senso (A.12).
- Cor. 2: la trascrizione ha *spatium quod sit ad quatuor tertias partes diametri suæ ut densitatem fluidi*: mancano probabilmente le parole *densitas globi ad*. Motte ha la lezione completa («as the density of the globe to the density of the fluid»), e la dimostrazione del corollario la richiede (nota N3). Integrazione tra parentesi quadre in II.S7.77; da verificare sulla stampa.
- Cor. 2: *vi ponderis sui comparativi* → «per la forza del suo peso comparativo» (A.0).
- Cor. 3 e 4: *per corol. VII. prop. XXXV.*, *per idem Corol. VII.* → «per il Cor. VII della Prop. XXXV», «per lo stesso Cor. VII». Verificati (A.17, nota N4).

### A.6 Proposizione XXXIX

**Latino:** *Globi, per fluidum in canali cylindrico clausum & compressum uniformiter progredientis, resistentia est ad vim qua totus ejus motus, interea dum octo tertias partes diametri suæ describit, vel generari possit vel tolli, in ratione quæ componitur ex ratione orifici canalis ad excessum hujus orificii supra dimidium circuli maximi globi, & ratione duplicata orificii canalis ad excessum hujus orificii supracirculum maximum globi, & ratione densitatis fluidi ad densitatem globi quamproxime.*

**Inglese:** “If a globe move uniformly forward through a fluid inclosed and compressed in a cylindric canal, its resistance is to the force by which its whole motion may be generated or destroyed, in the time in which it describes eight third parts of its diameter, in a ratio compounded of the ratio of the orifice of the canal to the excess of that orifice above half the greatest circle of the globe; and the duplicate ratio of the orifice of the canal to the excess of that orifice above the greatest circle of the globe; and the ratio of the density of the fluid to the density of the globe, nearly.”

- *orificium* → «orifizio» (A.0). *Excessus supra* → «eccesso su».
- **Refusi:** *orifici* per *orificii*; *supracirculum* (spazio mancante).
- Il rapporto composto riprende il Cor. 2 della Prop. XXXVII (EF²/(EF² − ½PQ²) «una volta» ed EF²/(EF² − PQ²) «due volte»): verificato sulla trascrizione (A.17). Nello Scolio Newton usa la radice di questo fattore per correggere gli spazi di caduta nel vaso stretto (nota N6).

### A.7 Scolio della Prop. XXXIX

- *In propositionibus duabus novissimis* → «nelle due ultime proposizioni» (XXXVIII e XXXIX).
- *Si aqua illa omnis liquescat, augebitur resistentia aliquantulum* → «Se tutta quell’acqua si scioglie, la resistenza aumenterà un poco».
- *totum officium glaciei faciat* → «fa interamente l’ufficio del ghiaccio». Motte «produces the very same effect almost as the congelation of the water»: attenua (*almost*) ciò che il latino afferma senza riserve (*totum*).

### A.8 Proposizione XL

**Latino:** *Globi, in medio fluidissimo compresso progredientis, invenire resistentiam per phænomena* (senza punto finale nella trascrizione).

**Inglese:** “To find by phenomena the resistance of a globe moving through a perfectly fluid compressed medium.”

**Letture delle formule appiattite** (dichiarate qui; nella Parte B il latino resta quello della trascrizione):

| Trascrizione | Lettura | Controllo |
|---|---|---|
| *ad 43D* | a 4/3 D | Prop. XXXVIII, Cor. 2 (quattro terzi del diametro) |
| *ut A ad A−,* | come A ad A − [B] | manca B; Motte «as A to A - B»; A − B è il peso del fluido spostato |
| *logarithmo 0,43429448192PG* | 0,4342944819 × 2P/G | 0,4342944819 = log₁₀ e (calcolato 0,4342944819033); il «2» appartiene a 2P/G (nota N5) |
| *logarithmus numeri N+1N* | log((N + 1)/N) | ricavato dalla formula dello spazio (N5) |
| *N−1N+1H* | (N − 1)H/(N + 1) | = H tanh(P/G) |
| *2PFG−1,3862943611F+4,605170186LF* | 2PF/G − 1,3862943611F + 4,605170186LF | 1,3862943611 = ln 4; 4,605170186 = 2 ln 10 |
| *Numeri in quarta columna sunt 2PG* | 2P/G | quarta colonna della tabella |
| *1,3862944-4,6051702L* | 1,3862944 − 4,6051702L | |

**Scelte.**

- *per phænomena* → «dai fenomeni».
- *Hæc est resistentia quæ oritur ab inertia materiæ fluidi* → «Questa è la resistenza che nasce dall’inerzia della materia del fluido»: Newton distingue la resistenza d’inerzia (in rapporto duplicato della velocità) dalle altre (elasticità, tenacità, attrito), che si «indagano» dal ritardo osservato.
- *ex retardatione* → «dal ritardo».
- *per libri secundi propositionem nonam & ejus corollaria* → «per la Prop. IX del Libro II e i suoi corollari»: è il rimando alla Sezione II (tempo e spazio di caduta con resistenza in rapporto duplicato della velocità, settori iperbolici). Verificato sulla trascrizione L2-S02 (A.17).
- Tabella: *existente velocitate maxima 100000000* → «essendo la velocità massima 100000000»; *ex hibet* (spazio spurio) → «presenta».
- La quinta colonna (*spatia … in vacuo cadente*) è (P/G)² F; la quarta è 2P/G × F (nota N5).

### A.9 Scolio: il vaso, le unità e gli Esperimenti 1–3

- *digitorum novem pedis Londinensis* → «nove pollici del piede londinese»; *profunditate pedum novem cum semisse* → «di profondità di nove piedi e mezzo»; *112 digitorum pedis* → «112 pollici» (il genitivo *pedis* ripete l’unità e in italiano si omette; lo segnalo).
- *globus quilibet alius est ut excessus ponderis ejus in vacuo supra pondus ejus in aqua* → «qualsiasi altro globo sta come l’eccesso…»: *globus* vale qui la grandezza (il volume) del globo; la resa letterale conserva l’ellissi del latino, e la nota N7 la spiega.
- *minutorum quatuor secundorum* → «quattro secondi»; *minuti unius secundi* → «un secondo».
- *Exper.* → *Esper.* in corsivo, come *Cor.*
- Esper. 1: *in subduplicata ratione spatii F seu 2,2128 dig. ad 95,219 dig.* → «nel rapporto subduplicato dello spazio F, ossia 2,2128 pollici, a 95,219 pollici».
- Esper. 1 e 4: *ex subduplicata ratione orificii vasis ad excessum orificii hujus supra semicirculum maximum globi & ex simplici ratione orificii ejusdem ad excessum ejus supra circulum maximum globi* → resa letterale; verifica in N6.
- Esper. 2: **refuso** *Subducator* per *Subducatur*.
- Esper. 3: *utrum minore proportioni resistentiæ … tribuendum sit*: *minore* accanto a *proportioni* è probabilmente un refuso per *minori* (dativo retto da *tribuendum*). Traduzione secondo il senso: «a una proporzione minore, nei moti lenti, della resistenza che nasce dalla forza d’inerzia rispetto alla resistenza che nasce da altre cause». Motte intende allo stesso modo.
- Esper. 3: *rarefactioni ceræ ad calorem vel tempestatis vel manus* → «alla rarefazione della cera per il calore del tempo atmosferico o della mano».

### A.10 Scolio: Esperimenti 4–12

- Esper. 4: *paravi vas ligneum latitudine interna digitorum 8 ⅔* («823» nella trascrizione): il latino non dice che il vaso sia quadrato, ma il calcolo di Newton (181,86 pollici) torna solo con un orifizio di (8 ⅔)² pollici quadrati (nota N8).
- Esper. 4: *per pendulum, ad semi-minuta secunda oscillans* → «con un pendolo che oscillava a mezzi secondi».
- Esper. 4: *Globi, ubi ponderabantur & postea cadebant, frigidi erant & aliquamdiu frigidi manserant* → resa letterale; la frase spiega perché si teneva conto della temperatura.
- Esper. 4: *tempora cadendi … describentes altitudinem pedum quindecim & digitorum duorum* → «quindici piedi e due pollici» (= 182 pollici, come nelle verifiche degli Esper. 8, 9, 12).
- Esper. 4: *tempore 25″ seu oscillationum 50* → «nel tempo di 25″, ossia di 50 oscillazioni»: conferma la lettura delle oscillazioni come mezzi secondi.
- *ceciderunt maxima ex parte* → «caddero per lo più».
- Esper. 9: *non pauciorum quam 12, non plurium quam 13* → «non meno di 12 … e non più di 13». Esper. 8 ha l’ordine inverso (*non plurium quam 52, non pauciorum quam 50*): conservato.
- Esper. 11: *32932* → 3 29/32; *4659* → 46 5/9; Motte «46 oscillations and [SVG 878]».
- II.S7.115: *ut in experimentis secundis, quartis, …* (plurali: le serie di prove di ciascun esperimento) → «come nel secondo, quarto, … esperimento». **Refuso** *nisi compresso fluidi simul augeatur* per *compressio*. *Per prop. XXXII. & XXXIII.* → «per le Propp. XXXII e XXXIII»: rimando a proposizioni del Fascicolo 18a (sistemi simili; resistenza in rapporto composto del duplicato della velocità, del duplicato del diametro e della densità), verificato sugli enunciati (A.17).

### A.11 Scolio: Esperimenti 13–14 e conclusioni

- Esper. 13: *A culmine ecclesiæ Sancti Pauli, in urbe Londini* → «Dalla sommità della chiesa di San Paolo, nella città di Londra». *Mense Junio 1710* → «nel mese di giugno del 1710».
- Esper. 13: *unus argenti vivi plenus, alter aeris* → «uno pieno di mercurio (argento vivo), l’altro d’aria»: prima occorrenza di *argentum vivum* nel fascicolo, secondo la regola del coordinatore. Nella tabella il latino ha *Globorum mercurio plenorum*: Newton stesso usa qui la parola *mercurius*, e la resa «mercurio» coincide.
- Esper. 13: *subtrahendo pessulum ope fili ferrei ad terram usque demissi ut tabula polis ferreis solummodo innixa super iisdem devolveretur* → «sfilando il chiavistello per mezzo di un filo di ferro che scendeva fino a terra, in modo che la tavola, appoggiata soltanto ai perni di ferro, ruotasse attorno a essi».
- Esper. 13: *pendulum ad minuta secunda oscillans* → «un pendolo che oscillava a secondi».
- Esper. 13: *Tempora cadendi* della prima tabella con *4−* e *4+*: segni conservati («poco meno di 4″», «poco più di 4″»).
- *per theoriam Galilæi* → «secondo la teoria di Galileo».
- *minutis tertiis octodecim* → «diciotto terzi». La trascrizione scrive i terzi ora ″′ (*8″ 12″′*) ora ′″ (*8″ 12′″*), e i quarti ″″ (*58″″*): normalizzati in ‴ e ⁗.
- *Pondus aquæ huic globo æqualis* → «il peso dell’acqua uguale a questo globo» (cioè di ugual volume). Motte «a bulk of water equal to this globe».
- Esper. 14: *formando vesicas porcorum in orbem sphæricum ope sphæræ ligneæ concavæ, quam madefactæ implere cogebantur inflando aerem* → «dando forma sferica a vesciche di maiale per mezzo di una sfera di legno concava, che le vesciche, inumidite, erano costrette a riempire quando vi si soffiava dentro l’aria».
- Esper. 14: **refuso** *altidudine* per *altitudine*.
- Esper. 14: *tempora tota cadendi* → «i tempi totali di caduta».
- Esper. 14: *Cadebant autem rectius* → «Caddero invece più dritte».
- Esper. 14: *1936″*: secondo lo schema della trascrizione (intero, numeratore, denominatore) si leggerebbe 19 3/6″, frazione insolita in una serie di ottavi e quarti. Motte stampa 19 ⅜″ (SVG 905, visto). Traduco «19 ⅜″» e considero *1936* un refuso probabile della trascrizione (6 per 8), da verificare sulla stampa (A.16).
- II.S7.127: *In scholio, quod sectioni sextæ subjunctum est* → «Nello scolio aggiunto alla Sezione VI». La cifra *13342* della trascrizione si legge 1/3342, come risulta dallo Scolio della Sezione VI (verificato, A.17); *14586* → 1/4586 (verifica numerica in N12).
- II.S7.128: *tVT+t*, *TVT+t* → tV/(T + t), TV/(T + t); *logarithmus numeri T+tT* → log((T + t)/T); *numerum tT* → t/T; *83D* → 8/3 D. Il Cor. 7 della Prop. XXXV ha la stessa formula con *2,302585092994* (qui *2,302585093*, arrotondato).
- II.S7.128: *Sed hujusmodi minutias hic non expendo* → «Ma minuzie di questo genere qui non le soppeso».
- II.S7.129: *subtiliarentur* → «si assottigliassero»; *trajectos lucis radios* → «i raggi di luce che li attraversano».

### A.12 Refusi e anomalie della trascrizione

| Luogo | Trascrizione | Lettura | Tipo |
|---|---|---|---|
| II.S7.66 | *æqulia* | *æqualia* | refuso probabile |
| II.S7.67 | *shpæram* | *sphæram* | refuso probabile |
| II.S7.72 | *que motibus suis* | *quæ* | refuso probabile |
| II.S7.73 | *quam superficiebus* | *quam [in] superficiebus* | omissione probabile o ellissi |
| II.S7.75 | *interna dum cylindrus* | *interea dum* | refuso probabile |
| II.S7.77 | *ut densitatem fluidi* | *ut densitas globi ad densitatem fluidi* | **omissione probabile** (Motte ha la lezione completa) |
| II.S7.80 | *orifici*; *supracirculum* | *orificii*; *supra circulum* | refuso; spaziatura |
| II.S7.83 | enunciato senza punto finale | — | punteggiatura |
| II.S7.84 | *ut A ad A−,* | *ut A ad A−B* | **omissione di B** |
| II.S7.86–87 | formule appiattite | lette come in A.8 | appiattimento |
| II.S7.87 | *ex hibet* | *exhibet* | spaziatura |
| II.S7.88 | celle della tabella fuse senza separatori («9999929300,000001 F0,002 F…») | separate per colonne come in A.13 | appiattimento |
| II.S7.93 | *Subducator* | *Subducatur* | refuso probabile |
| II.S7.95 | *minore proportioni* | *minori proportioni* | refuso probabile |
| II.S7.115 | *nisi compresso fluidi* | *nisi compressio fluidi* | refuso probabile |
| II.S7.118, 121, 125 | celle fuse | separate come in A.13 | appiattimento |
| II.S7.119–121 | *12″′*, *12′″*, *58″″* | 12‴, 58⁗ | grafie oscillanti |
| II.S7.122 | *altidudine* | *altitudine* | refuso probabile |
| II.S7.123 | *1936″* | 19 ⅜″ (Motte, SVG 905) | **refuso probabile** (6 per 8) |
| passim | frazioni senza separatore («15614», «1561338») | 156 ¼, 156 13/38 ecc. | appiattimento (A.13) |

Nessuno di questi punti è stato verificato sulla stampa del 1726. La traduzione segue il senso; la Parte B riporta il latino esatto della trascrizione.

### A.13 Frazioni e celle ricostruite

La trascrizione scrive le frazioni senza separatore (intero, numeratore, denominatore di seguito). Ogni lettura sotto è confermata dall’aritmetica del testo stesso (note N7–N11), salvo quelle marcate «non verificabile».

| Trascrizione | Lettura | Conferma |
|---|---|---|
| *1936 uncias*; *grana 25313* | 19/36 di oncia; 253 ⅓ grani | 76 × 12/1728 = 19/36; × 480 = 253,33 |
| *15614*; *1561338*; *791338* | 156 ¼; 156 13/38; 79 13/38 | 79,25 × 132,8/132,645 = 79,343 |
| *19313* | 193 ⅓ | 193,333 × 77/156,342 = 95,219 |
| *7613*; *5116*; *76512*; *711748* | 76 ⅓; 5 1/16; 76 5/12; 71 17/48 | 76,4167 − 5,0625 = 71,354 |
| *823*; *13914*; *718*; *13925*; *1321140* | 8 ⅔; 139 ¼; 7 ⅛; 139 2/5; 132 11/40 | 139,4 − 7,125 = 132,275 |
| *4712, 4812*; *4912*; *4912* | 47 ½, 48 ½; 49 ½ | |
| *15438*; *2112* | 154 ⅜; 21 ½ | calcolo: 28,9 oscillazioni (testo 29) |
| *21238*; *7912*; *1512* | 212 ⅜; 79 ½; 15 ½ | calcolo: 15,1 (testo 15) |
| *29338*; *3578*; *2912*, *3012* | 293 ⅜; 35 ⅞; 29 ½, 30 ½ | calcolo: 28,1 (testo 28) |
| *612* | 6 ½ | calcolo: 52,4 (testo 52) |
| *27314*; *14034*; *1113* | 273 ¼; 140 ¾; 11 ⅓ | calcolo: 11,38 |
| *11912*; *1734*, *1812*; *18112*; *1559* | 119 ½; 17 ¾, 18 ½; 181 ½; 15 5/9 | calcolo: 15,59 |
| *32932*; *4312*, *4412*; *18212*; *4659* | 3 29/32; 43 ½, 44 ½; 182 ½; 46 5/9 | calcolo: 46,55 |
| *438*; *6412* | 4 ⅜; 64 ½ | calcolo: 64,6 |
| tabella Prop. XL: *999992930*; *99999999 35* | 99999 29/30; 99999999 3/5 | 10⁸ tanh(0,001) = 99999,967; 10⁸ tanh(10) = 99999999,59 |
| prima tabella Esper. 13: *8″12*, *8″14* | 8 ½″, 8 ¼″ | correzione di 18‴ → 8″ 12‴, 7″ 57‴ |
| *16600860*; *19310*; *502310*; *1313*; *512*; *513*; *012* | 16600/860; 19 3/10; 502 3/10; 13 ⅓; 5 ½; 5 ⅓; 0 ½ | 16600/860 = 19,30 |
| Esper. 14: *1434, 1234, 1458, 1734, 1678*; *1412, 1414*; *1634*; *414* | 14 ¾, 12 ¾, 14 ⅝, 17 ¾, 16 ⅞; 14 ½, 14 ¼; 16 ¾; 4 ¼ | somme con 4 ¼ = totali del testo (N11) |
| *1878*, *2118*; *1834*, *1812*, *1814*, *2314* | 18 ⅞, 21 ⅛; 18 ¾, 18 ½, 18 ¼, 23 ¼ | somme esatte |
| *1936*, *1714*, *1834*, *2218*, *2158*; *1858*, *1838*, *2114* | 19 ⅜ (Motte; trascrizione 19 3/6), 17 ¼, 18 ¾, 22 ⅛, 21 ⅝; 18 ⅝, 18 ⅜, 21 ¼ | tempi osservati, non verificabili con il calcolo; confermati dagli SVG 905–911 e 688 di Motte |
| tabella vesciche: *13712*, *9712*, *9918*, *1812*, *2118*, *012* | 137 ½, 97 ½, 99 ⅛, 18 ½, 21 ⅛, 0 ½ | calcolo della teoria, scarti di pochi pollici (N11) |
| *13342*; *14586* | 1/3342; 1/4586 | 3/(16 × 860) = 1/4586,7 (N12) |

### A.14 Riepilogo: dove Motte aggiunge, omette o sbaglia

| Luogo | Latino | Motte 1846 | Tipo |
|---|---|---|---|
| II.S7.72 | *tanquam gelu constrictæ* | «being fixed like water by frost» | aggiunta («like water») |
| II.S7.73 | *paulo magis relaxant* | «relax the same» | omissione di *paulo magis* |
| II.S7.73 | *qualis est aer* | «as our air» | aggiunta |
| II.S7.73 | *maria & paludes* | «lakes and seas» | termine diverso (paludi → laghi) e ordine invertito |
| II.S7.77 | *ut densitatem fluidi* (trascrizione) | «as the density of the globe to the density of the fluid» | Motte ha la lezione completa che la trascrizione perde |
| II.S7.82 | *totum officium glaciei faciat* | «produces the very same effect almost as the congelation» | attenuazione («almost») |
| II.S7.83, II.S7.127 | *fluidissimus* | «perfectly fluid», «of the most extreme fluidity» | intensificazione |
| II.S7.84 | *ut A ad A−,* (trascrizione) | «as A to A - B» | Motte completo |
| II.S7.85, 86, 129 | *inertia materiæ*, *vis inertiæ* | «inactivity of the matter», «force of inactivity» | termine non conforme al glossario |
| II.S7.86 | *aliam insuper resistentiam*; *quantitas hujus resistentiæ* | «really … of another kind»; «this new resistance» | aggiunte |
| II.S7.86 | *+4,605170186LF* (formula dell’altezza e termine da trascurare) | «− 4,405170186LF» (SVG 749 e 750) | **formula errata**: segno e seconda cifra. Il valore giusto è + 2 ln 10 = + 4,605170186 (N5) |
| II.S7.93, II.S7.97 | *tempus G 0″,301056*; *0″,376843* | «the time GO″,301056», «GO″,376843» (SVG 847, 856) | refuso tipografico dell’immagine (O per 0, G attaccato) |
| II.S7.89 | *pedis Londinensis* | «English measure» | resa libera |
| II.S7.89, 122 | *libras Romanas*; *uncias libræ hujus* | «pounds troy weight»; «ounces troy weight» | interpretazione (coerente con l’aritmetica, N7) |
| II.S7.111 | *32932 in aqua* | «3 20/32; in water» (SVG 874) | **cifra errata** (29 → 20): con 3 20/32 grani la teoria darebbe 48,4 oscillazioni invece di 46 5/9 (N9); punto e virgola spurio |
| II.S7.123 | *1936″* (trascrizione) | «19 ⅜″» (SVG 905) | Motte conferma la lettura attesa (A.12) |
| II.S7.113 | *altitudinem* | «a space» | lieve |
| II.S7.117 | *culmine ecclesiæ* | «the top of St. Paul’s Church» | — (corretto) |
| II.S7.117 | *polis ferreis* | «iron hinges» | interpretazione |
| II.S7.117 | *ut tabula … super iisdem devolveretur* | «fell downward, and turning round upon the hinges, gave leave to the globes to drop off from it» | **ampliamento** |
| II.S7.117 | *per filum illud ferreum tractum dimitteretur* | «with the same pull of the iron wire that took out the pin, … was let go» | ampliamento |
| II.S7.121 | terza riga, eccesso *7 10* | «7 0» | **cifra errata** in Motte 1846 (o perdita nella trascrizione EPUB) |
| II.S7.122 | *Anno 1719* | «Anno 1719, in the month of July» | latino lasciato nel testo inglese |
| II.S7.122 | *D. Desaguliers* | «Dr. Desaguliers» | scioglimento dell’abbreviazione (A.0) |
| II.S7.122 | *ab altiore loco in templi ejusdem turri rotunda fornicata* | «from the lantern on the top of the cupola of the same church» | **interpretazione/aggiunta** («lantern») |
| II.S7.122 | *quam madefactæ implere cogebantur inflando aerem* | «which the bladders, being wetted well first, were put into. After that being blown full of air, they were obliged to fill up the spherical cavity» | ampliamento |
| II.S7.122 | *horologium cum elatere* | «a machine» | **omissione** dell’orologio a molla |
| II.S7.125 | seconda riga, tempo *17* | «7» | **cifra errata** in Motte 1846 (perdita dell’«1») |
| II.S7.125 | terza riga, tempo *18 ½* | «18» | **frazione persa** in Motte 1846 |
| II.S7.126 | *prope omnis* | «within a very little, all» | — |
| II.S7.127 | *cæteris paribus* | «cæteris paribus» | latino lasciato nel testo inglese |
| II.S7.129 | *haud minus resisterent* | «the resistance … would be the same» | resa diversa («non meno» → «la stessa») |
| II.S7.129 | *trajectos lucis radios* | «the rays of light» | omissione di *trajectos* |

Le formule e i numeri frazionari di Motte, stampati come immagini, sono stati controllati tutti (A.15). Sono corretti, tranne la formula dell’altezza della Prop. XL (SVG 749–750), il peso dell’Esper. 11 (SVG 874) e la grafia «GO″» (SVG 847, 856). La tabella della Prop. XL in Motte (SVG 754–835 e i numeri a caratteri) coincide cella per cella con la trascrizione.

### A.15 Controllo degli SVG di Motte

L’intervallo di Motte tradotto qui contiene **187 marcatori SVG distinti**: 745–921 (consecutivi) e dieci riusati da pagine precedenti (227, 228, 455, 641, 643, 666, 688, 727, 735, 736). Li ho confrontati **tutti** con il latino sulla tabella numero→LaTeX dell’EPUB (`svg_tex.tsv`); ho inoltre reso in immagine e guardato le 20 formule e i casi dubbi (745–753, 918–921, 735, 455, 666, 688, 905–907, 874, 847, 856), e l’immagine coincide sempre con il LaTeX.

| SVG | Luogo | Motte | Latino | Esito |
|---|---|---|---|---|
| 745–748, 751–753 | Prop. XL, II.S7.84–87 | 4/3 D; 0,4342944819 × 2P/G; (N+1)/N; (N−1)H/(N+1); 2PF/G − 1,3862943611F; 2P/G; 1,3862944 − 4,6051702L | idem | concordano; confermano le letture di A.8 |
| **749** | II.S7.86 | 2PF/G − 1,3862943611F **− 4,405170186LF** | … **+ 4,605170186LF** | **non torna**: segno e cifra; il latino è giusto (N5) |
| **750** | II.S7.86 | **4,405170186**LF | 4,605170186LF | **non torna** (cifra) |
| 754–835 | tabella II.S7.88 | tempi, spazi, 99999 29/30, 99999999 3/5 | idem | concordano tutte; confermate anche le letture delle frazioni appiattite |
| 836–846, 848–855, 857–873, 875–880 | Scolio, Esper. 1–12 | frazioni dei pesi, dei tempi e delle altezze | idem | concordano (confermano A.13) |
| 847, 856 | Esper. 2 e 4 | «GO″,301056», «GO″,376843» | *tempus G 0″,301056*, *0″,376843* | refuso tipografico di Motte (O per 0) |
| **874** | Esper. 11 | **3 20/32** | *32932* = 3 29/32 | **non torna**: Motte errato; il calcolo conferma 29/32 |
| 881–889 | Esper. 13 | 8 ½″, 8 ¼″, 16600/860, 19 3/10, 502 3/10, 13 ⅓, 5 ⅓, 8″, 12‴ | idem | concordano |
| 890–904, 906–911, 688 | Esper. 14 | tempi delle vesciche | idem | concordano |
| **905** | Esper. 14 | 19 ⅜″ | *1936″* | il latino della trascrizione è con ogni probabilità un refuso; si adotta 19 ⅜ (A.11, A.12) |
| 912–917 | tabella vesciche | 19″, 0 ½, 137 ½, 97 ½, 99 ⅛, 21 ⅛ | idem | concordano (gli errori di Motte nella stessa tabella, «7» e «18», sono a caratteri: A.14) |
| 918–921, 735, 455, 666 | II.S7.127–128 | 1/4586; 8/3 D; tV/(T+t); TV/(T+t); (T+t)/T; t/T; 1/3342 | idem | concordano |
| 227, 228, 641, 643, 727, 736 | passim | ⅓, ¼, 18 ½, ½, 6 ½, 5 ½ | idem | concordano |

**SVG non visti:** nessuno. Restano da controllare sulla stampa (non sull’EPUB) i soli punti di A.16.

### A.16 Punti da controllare sulla stampa ECCO

| Pagina 1726 | Trascrizione | Lettura attesa | Motivo |
|---|---|---|---|
| 340 | *æqulia*; *shpæram* | *æqualia*; *sphæram* | refusi probabili |
| 341 | *que motibus* | *quæ* | refuso probabile |
| 342 | *quam superficiebus* | *quam in superficiebus*? | possibile omissione |
| 342 | *interna dum* | *interea dum* | refuso probabile; Motte «while» |
| 342 | *ut densitatem fluidi* | *ut densitas globi ad densitatem fluidi* | omissione probabile; la dimostrazione la richiede |
| 343 | *orifici*; *supracirculum* | *orificii*; *supra circulum* | refuso, spaziatura |
| 344 | *ut A ad A−,* | *ut A ad A−B* | B mancante |
| 344 | *0,43429448192PG* | 0,4342944819 × 2P/G | lettura confermata da Motte (SVG 746) |
| 344 | *+4,605170186LF* (due volte) | idem | Motte 1846 ha −4,405170186LF (SVG 749–750): controllare che la stampa 1726 abbia + e 4,605 |
| 350 | *32932* (peso in acqua, Esper. 11) | 3 29/32 | Motte 1846 ha 3 20/32 (SVG 874); il calcolo conferma 29/32 |
| 345 | tabella: velocità a 8G *99999980* | (stampa) | il calcolo dà 99999977,5 (N5): verificare se l’errore è già nella stampa |
| 347 | *Subducator* | *Subducatur* | refuso probabile |
| 347 | *minore proportioni* | *minori* | refuso probabile |
| 348 | *latitudine interna digitorum 823* | 8 ⅔ | conferma della frazione |
| 351 | *nisi compresso fluidi* | *compressio* | refuso probabile |
| 352–353 | grafie *12″′*, *12′″*, *58″″* | ‴, ⁗ | uniformità tipografica |
| 353 | tabella dei globi d’aria, terza riga *7 10* | (stampa) | Motte 1846 ha «7 0» |
| 353 | *D. Desaguliers* | *D.* = *Dominus* o *Doctor*? | scioglimento |
| 353 | *altidudine* | *altitudine* | refuso probabile |
| 354 | *1936″* | 19 ⅜″ | Motte (SVG 905) ha 19 ⅜″ |
| 354 | tabella vesciche, righe 2–3 | 17″ e 18 ½″ | Motte 1846 ha «7» e «18» |

### A.17 Rimandi verificati

**Rimandi al Libro I:** nessuno in questa parte della Sezione VII. **Rimandi interni al Libro II** (verificati sulle trascrizioni allegate):

| Luogo | Rimando | Esito |
|---|---|---|
| II.S7.67 | Prop. XXXVI, Cor. VII | regge: è il corollario in cui l’acqua «la cui fluidità non è richiesta» per la discesa più rapida si immagina congelata (L2-S07, riga 125) |
| II.S7.69 | Lemma V e Legge III | regge |
| II.S7.72 | scolio della proposizione precedente | regge: Scolio della Prop. XXXVII, testa e coda di fluido congelato (righe 164–166) |
| II.S7.75 | Prop. XXXVII | regge: resistenza del cilindro sta alla forza che ne toglie il moto in quattro lunghezze come la densità del mezzo a quella del cilindro (riga 142) |
| II.S7.75 | Lemmi V, VI, VII | regge |
| II.S7.78, 79, 128 | Prop. XXXV, Cor. VII | regge: perdita tM/(T + t) e spazio come log((T + t)/T) × 2,302585092994 sta a t/T (riga 83) |
| II.S7.81 | Prop. XXXVII, Cor. 2 | regge: rapporto composto da EF²/(EF² − ½PQ²) e dal duplicato di EF²/(EF² − PQ²) (riga 160) |
| II.S7.84 | Prop. XXXVIII, Cor. 2 e Cor. 1 | regge |
| II.S7.86 | Libro II, Prop. IX e corollari | regge: tempo di discesa come settore iperbolico, spazio di caduta come area (Cor. 1) in rapporto alla resistenza in duplicato della velocità (L2-S02, righe 97–109); la riduzione alle formule logaritmiche è di Newton (N5) |
| II.S7.115 | Propp. XXXII e XXXIII | regge sugli enunciati (sistemi simili; resistenza in rapporto composto dal duplicato delle velocità, dal duplicato dei diametri e dalla densità). Che la *compressione* debba crescere nel duplicato della velocità non è detto negli enunciati: Newton lo deduce dalla condizione di similitudine dei moti; non ho letto per intero le dimostrazioni del Fascicolo 18a |
| II.S7.127 | Scolio della Sezione VI | regge: lì il globo che descrive il proprio semidiametro perde la parte 1/3342 del moto (L2-S06, riga 136) |

Nessun rimando risulta sbagliato.

---
## Note editoriali e fisiche

Queste note sono aggiunte del presente fascicolo, non affermazioni tradotte da Newton. Le verifiche numeriche sono state eseguite con uno script Python (`tmp/18b/verifica.py`, conservato con i materiali di lavoro), che ricalcola ogni grandezza a partire dai soli dati di Newton (pesi, diametri, tempi, 193 ⅓ pollici di caduta nel primo secondo, globo d’acqua di un pollice = 132,8 grani nel vuoto, aria : acqua = 1 : 860) con le sue stesse regole.

### N1. Lemmi V–VII: perché il cilindro vale quanto la sfera

I tre lemmi riducono la resistenza della sfera a quella del cilindro della stessa larghezza, già calcolata nella Prop. XXXVII. L’argomento regge solo nell’ipotesi, dichiarata più volte, che l’acqua «inutile» davanti e dietro ai corpi sia immobile, «come stretta dal gelo»: allora tutti i corpi presentano allo scorrere del fluido lo stesso spazio anulare libero. Il passaggio dal Lemma VI (acqua che scorre su corpi fermi) al Lemma VII (corpi che si muovono nell’acqua ferma) è l’equivalenza dei sistemi di riferimento in moto uniforme (Cor. V delle leggi, Fascicolo 3), che Newton richiama con la sola frase «i moti relativi restano gli stessi». La *tenacitas* dello Scolio corrisponde a ciò che oggi chiamiamo viscosità; Newton la esclude esplicitamente.

### N2. Prop. XXXVIII in termini moderni

La resistenza R di un globo di diametro D e massa M = ρ_g πD³/6 che si muove con velocità v è, per Newton, la forza che toglierebbe M·v nel tempo t₁ = (8/3)D/v, ridotta nel rapporto ρ_f/ρ_g:

R = (ρ_f/ρ_g) · M v / t₁ = ρ_f π D² v² / 16.

Con l’area frontale A = πD²/4 si ha R = ½ · C · ρ_f A v² con **C = 0,5**. Il «due a tre» della dimostrazione è il rapporto di Archimede fra il volume della sfera e quello del cilindro circoscritto: a parità di sezione e di resistenza, il globo ha 2/3 della massa del cilindro, quindi perde la sua quantità di moto in 2/3 della lunghezza (4D × 2/3 = 8/3 D). Il coefficiente moderno per una sfera a numeri di Reynolds elevati è dell’ordine di 0,4–0,5 (non verificato sulle fonti allegate).

### N3. Cor. 2: la velocità limite

Se il globo cade da fermo con il solo peso comparativo B (accelerazione g′ = g·B/A) per uno spazio s, acquista v² = 2g′s; con quella velocità, nello stesso tempo, descriverebbe 2s. Uguagliando B alla resistenza di N2 si ottiene s = (4/3)D·ρ_g/ρ_f: è l’enunciato del corollario **con** le parole *densitas globi ad* che la trascrizione perde (A.12). Senza di esse l’enunciato non ha senso («sta ai quattro terzi del diametro come la densità del fluido»).

### N4. Cor. 4 e Prop. XXXV, Cor. 7

Con resistenza in rapporto duplicato della velocità, la velocità decresce come v = V·T/(T + t), e lo spazio è x = VT·ln(1 + t/T). Per un globo della stessa densità del fluido, VT = (8/3)D. Metà della velocità si perde a t = T, cioè dopo x = (8/3)D·ln 2 = **1,85 D**, meno di due diametri, come dice il Cor. 4. La stessa formula è quella dell’ultimo esempio dello Scolio (II.S7.128): il numero 2,302585093 = ln 10 serve a passare dai logaritmi decimali delle tavole al logaritmo naturale.

### N5. Prop. XL e la sua tabella

Con il peso comparativo B costante e la resistenza in rapporto duplicato della velocità, la caduta da fermo dà, in notazione moderna,

v = H · tanh(P/G),  spazio = 2F · ln cosh(P/G),

dove H è la velocità limite, G il tempo in cui il globo senza resistenza percorrerebbe F, e 2F = H·G. Le formule di Newton sono esattamente queste, scritte con i logaritmi decimali: N = 10^(0,4342944819 × 2P/G) = e^(2P/G); (N − 1)/(N + 1) = tanh(P/G); e

2F ln cosh(P/G) = 2PF/G − 2F ln 2 + 2F ln((N + 1)/N) = 2PF/G − 1,3862943611F + 4,605170186 L F,

con L = log₁₀((N + 1)/N), 1,3862943611 = ln 4 e 4,605170186 = 2 ln 10 (calcolati: 1,38629436112 e 4,60517018599). Il segno del terzo termine è **+**, come nel latino: la formula stampata da Motte 1846 (SVG 749–750, «− 4,405170186LF») è sbagliata nel segno e in una cifra. Per tempi lunghi L → 0 e la caduta diventa uniforme con la velocità H, ritardata di 1,3863F rispetto al moto a velocità massima: è la regola usata in tutti gli esperimenti dello Scolio.

**Verifica della tabella (21 righe × 5 colonne).** Ho ricalcolato ogni cella: velocità = 10⁸ tanh(P/G); spazio nel fluido = 2 ln cosh(P/G); quarta colonna = 2P/G; quinta = (P/G)². Tutte le 105 cifre coincidono con il calcolo all’ultima cifra stampata (le sette decimali della terza colonna comprese), **tranne una**:

- riga **8 G**, velocità: stampata **99999980**, calcolata **99999977,5** (10⁸·(1 − 2e⁻¹⁶ + …)). L’errore è di 2,5 unità su 10⁸; Motte 1846 stampa lo stesso numero (a caratteri), quindi è con ogni probabilità nella stampa del 1726. Lo segnalo senza correggerlo.

Le letture delle frazioni 99999 29/30 (calcolato 99999,967) e 99999999 3/5 (calcolato 99999999,588) sono confermate.

### N6. La correzione per il vaso stretto (Prop. XXXIX applicata)

Nel vaso di sezione O (orifizio) la resistenza cresce, per la Prop. XXXIX, del fattore [O/(O − c/2)]·[O/(O − c)]², con c = πD²/4 cerchio massimo del globo. La velocità limite, e quindi lo spazio percorso a regime, diminuisce come la radice di quel fattore: √((O − c/2)/O)·(O − c)/O, cioè «il rapporto subduplicato dell’orifizio all’eccesso sul semicerchio e il rapporto semplice dell’orifizio all’eccesso sul cerchio», come dice Newton. Per l’Esper. 1 (O = 81 pollici quadrati, D = 0,84224): fattore calcolato **0,99141**, testo 0,9914; 113,0569 × 0,9914 = **112,09**, testo 112,08.

### N7. Unità di misura dello Scolio

- 76 libbre in un piede cubo (1728 pollici cubi): 76 × 12/1728 = **19/36** di oncia per pollice cubo; × 480 grani = **253 ⅓** grani. Le cifre implicano una libbra di 12 once e 5760 grani (la *libra Romana* di Newton coincide con la libbra troy di Motte).
- Globo d’acqua di un pollice di diametro: π/6 × 253 ⅓ = **132,645** grani, come nel testo (pesato nell’aria). Il valore nel vuoto, 132,8, implica una spinta dell’aria di 0,155 grani, cioè un rapporto aria : acqua di circa 1 : 856, vicino all’1 : 860 assunto più avanti.
- «Qualsiasi altro globo sta come l’eccesso…»: il volume (e quindi il cubo del diametro) di un globo è proporzionale alla differenza fra il suo peso nel vuoto e il suo peso nell’acqua; il diametro si ricava come D³ = (A − B)/132,8.
- 193 ⅓ pollici in un secondo di caduta libera equivalgono a g = 386,7 pollici/s² = 32,2 piedi/s².

### N8. Esperimenti 1, 2 e 4: i calcoli completi

| Grandezza | Esper. 1 testo / calcolo | Esper. 2 testo / calcolo | Esper. 4 testo / calcolo |
|---|---|---|---|
| peso nel vuoto A (grani) | 156 13/38 = 156,342 / 156,343 | 76 5/12 = 76,417 / 76,417 | 139 2/5 = 139,40 / 139,404 |
| eccesso A − B | 79 13/38 / 79,343 | 71 17/48 = 71,354 / 71,354 | 132 11/40 = 132,275 / 132,279 |
| diametro D (pollici) | 0,84224 / 0,84224 | 0,81296 / 0,81297 | 0,99868 / 0,99869 |
| 8/3 D | 2,24597 / 2,24598 | 2,16789 / 2,16792 | 2,66315 / 2,66318 |
| 2F | 4,4256 / 4,4256 | 2,3217 / 2,3217 | 2,8066 / 2,8066 |
| caduta in 1″ con il peso B | 95,219 / 95,218 | 12,808 / 12,808 | 9,88164 / 9,88132 |
| G (secondi) | 0,15244 / 0,152445 | 0,301056 / 0,301057 | 0,376843 / 0,376851 |
| 2F·P/G | 116,1245 / 116,1243 | 115,678 / 115,679 | 186,1915 / 186,189 |
| 1,3862944F | 3,0676 / 3,0676 | 1,609 / 1,6093 | 1,9454 / 1,9454 |
| vaso larghissimo | 113,0569 / 113,0566 | 114,069 / 114,070 | 184,2461 / 184,244 |
| correzione del vaso | × 0,9914 / × 0,99141 | − 0,895 / − 0,913 | → 181,86 / 181,85 (O = (8 ⅔)²) |
| teoria nel vaso | 112,08 / 112,09 | 113,174 / 113,157 | 181,86 / 181,85 |
| esperimento | 112 | 112 | 182 |

Tutte le cifre tornano entro l’arrotondamento. Nell’Esper. 2 la detrazione per il vaso (0,895 pollici) risulta leggermente diversa dal calcolo con la regola dell’Esper. 1 (0,913): la differenza (0,02 pollici sul risultato) è trascurabile e non cambia la conclusione. Nell’Esper. 4 la correzione del vaso torna solo se il vaso è a sezione quadrata di 8 ⅔ pollici di lato.

### N9. Esperimenti 3 e 5–12: i tempi teorici

Ho calcolato per ogni esperimento il tempo teorico con la formula esatta (spazio = 2F ln cosh(P/G)), con la correzione del vaso stretto, nel vaso dell’Esper. 3 (9 × 9 pollici) e nel vaso degli Esper. 4–12 ((8 ⅔)² pollici quadrati); le oscillazioni sono mezzi secondi.

| Esper. | pesi (aria; acqua) | altezza (pollici) | teoria nel testo | calcolo | osservati |
|---|---|---|---|---|---|
| 3 | 121; 1 | 112 | circa 40″ | 39,9″ | 46″, 47″, 50″ |
| 4 | 139 ¼; 7 ⅛ | 182 | 50 | 50,04 | per lo più 49 ½–50 |
| 5 | 154 ⅜; 21 ½ | 182 | 29 | 28,89 | 28 ½–30 (fino a 33) |
| 6 | 212 ⅜; 79 ½ | 182 | 15 | 15,09 | 15–18 |
| 7 | 293 ⅜; 35 ⅞ | 181 ½ | 28 | 28,09 | 29 ½–33 |
| 8 | 139; 6 ½ | 182 | circa 52 | 52,44 | 50–52, per lo più 51 |
| 9 | 273 ¼; 140 ¾ | 182 | 11 ⅓ | 11,38 | 12–13 |
| 10 | 384; 119 ½ | 181 ½ | 15 5/9 | 15,59 | 17 ¾–19 |
| 11 | 48; 3 29/32 | 182 ½ | 46 5/9 | 46,55 | 43 ½–46, per lo più 44–45 |
| 12 | 141; 4 ⅜ | 182 | 64 ½ | 64,59 | 61–65 |

Tutti i tempi teorici di Newton sono confermati entro un decimo di oscillazione: le letture delle frazioni appiattite (A.13) sono dunque giuste. Con il peso di Motte per l’Esper. 11 (3 20/32 grani, SVG 874) la teoria darebbe 48,4 oscillazioni: è Motte 1846 a sbagliare. Senza la correzione del vaso i tempi teorici sarebbero più brevi di 0,3–0,7 oscillazioni: Newton applica la correzione anche dove non la nomina.

Il confronto conferma la lettura di Newton in II.S7.115: per i globi lenti (Esper. 2, 4, 5, 8, 11, 12) teoria ed esperimento concordano; per i globi veloci (Esper. 6, 9, 10) le cadute osservate sono più lente del previsto del 5–20 %.

### N10. Esperimento 13 (San Paolo, 1710)

- **Galileo:** in 4″ un grave cade di 193 ⅓ × 16 = 3093 pollici = **257,8 piedi** (testo 257); 220 piedi richiedono √(2640/193,33) = 3,695″ = **3″ 41,7‴** (testo 3″ 42‴). I globi di mercurio impiegavano invece circa 4″: da qui la correzione di 18‴.
- **Tempi corretti:** 8 ½″ − 18‴ = 8″ 12‴; 8″ − 18‴ = 7″ 42‴; 8 ¼″ − 18‴ = 7″ 57‴. Le sei cifre del testo tornano.
- **Quinto globo** (483 grani, 5 pollici): acqua di ugual volume 5³ × 132,8 = **16600** grani; aria 16600/860 = **19,30**; A = **502,30**; 2F = 13 ⅓ × 502,3/19,3 = 347,0 pollici = **28 piedi 11 pollici**; caduta in 1″ con il peso 483: **185,904** pollici (testo 185,905); F = 173,5 pollici = 14 piedi 5 ½ pollici; G = 0,9660″ = **57,96‴** (testo 57‴ 58⁗); spazio a velocità massima in 8,2″: 2945,2 pollici = **245 piedi 5,2 pollici** (testo 245 piedi 5 ⅓); 1,3863F = 240,5 pollici = **20 piedi 0,5 pollici**; teoria **225 piedi 4,7 pollici** (testo 225 piedi 5). Tutto torna.
- **Tabella dei globi d’aria** (stesso calcolo):

| Peso; diametro; tempo | Teoria nel testo | Calcolo | Eccesso nel testo | Eccesso calcolato |
|---|---|---|---|---|
| 510; 5,1; 8″ 12‴ | 226 piedi 11 | 226 piedi 11,0 | 6 piedi 11 | 6 piedi 11,0 |
| 642; 5,2; 7″ 42‴ | 230 9 | **231 0,1** | 10 9 | **11 0,1** |
| 599; 5,1; 7″ 42‴ | 227 10 | 227 10,4 | 7 10 | 7 10,4 |
| 515; 5; 7″ 57‴ | 224 5 | 224 4,7 | 4 5 | 4 4,7 |
| 483; 5; 8″ 12‴ | 225 5 | 225 4,7 | 5 5 | 5 4,7 |
| 641; 5,2; 7″ 42‴ | 230 7 | **230 10,1** | 10 7 | **10 10,1** |

Due righe (642 e 641 grani) differiscono dal calcolo di **circa 3 pollici** su 230 piedi (0,1 %): corrisponderebbero a un tempo di 7,692″ invece di 7,700″. La differenza è dentro la precisione dei calcoli di Newton e non tocca la conclusione; la segnalo senza correggere. Le colonne «teoria» ed «eccessi» sono coerenti fra loro in ogni riga (eccesso = teoria − 220 piedi). La terza riga di Motte («7 0» invece di 7 10) è un errore dell’edizione 1846 (A.14).

### N11. Esperimento 14 (Desaguliers, 1719)

- **Somme dei tempi:** le dieci somme «differenza + 4 ¼″» del testo sono esatte (19, 17, 18 ⅞, 22, 21 ⅛; 18 ¾, 18 ½, 18 ¼, 23 ¼, 21).
- **Tempi usati nella tabella:** 19″, 17″, 22″ e 21 ⅛″ sono i totali della prima prova; per la terza vescica la tabella usa 18 ½″, che non è né il totale della prima prova (18 ⅞″) né quello della seconda (18 ¼″), nella quale questa vescica cadde «più dritta». Il testo non spiega la scelta; la segnalo.
- **Teoria** (aria : acqua = 1 : 860, peso nell’aria come peso comparativo):

| Peso; diametro; tempo | Teoria nel testo | Calcolo | Differenza nel testo | Differenza calcolata |
|---|---|---|---|---|
| 128; 5,28; 19″ | 271 piedi 11 | 271 piedi 10,1 | − 0 piedi 1 | − 0 piedi 1,9 |
| 156; 5,19; 17″ | 272 0 ½ | 272 0,2 | + 0 0 ½ | + 0 0,2 |
| 137 ½; 5,3; 18 ½″ | 272 7 | **273 0,3** | + 0 7 | **+ 1 0,3** |
| 97 ½; 5,26; 22″ | 277 4 | **276 10,8** | + 5 4 | **+ 4 10,8** |
| 99 ⅛; 5; 21 ⅛″ | 282 0 | 281 8,6 | + 10 0 | + 9 8,6 |

Gli scarti fra il testo e il calcolo vanno da 0,3 a 5,5 pollici su circa 275 piedi (al massimo 0,17 %), cioè differenze di 0,01–0,03″ nel tempo. Sono compatibili con l’aritmetica con le tavole dei logaritmi e con l’arrotondamento dei dati; le righe 3 e 4 sono quelle che si scostano di più. Non correggo nulla. Le colonne del testo sono coerenti fra loro (differenza = teoria − 272 piedi).

### N12. Pendoli contro cadute: 1/3342 e 1/4586

Per la Prop. XXXVIII un globo della densità dell’acqua che si muove nell’aria perderebbe tutta la quantità di moto, sotto resistenza costante, percorrendo (8/3)D × 860; percorrendo il semidiametro D/2 ne perde la frazione (D/2)/((8/3)D × 860) = 3/13760 = **1/4586,7** (testo 1/4586). Lo Scolio della Sezione VI dava **1/3342** (verificato sulla trascrizione L2-S06). Il rapporto 4586/3342 = **1,372**, cioè «circa 4 a 3», come dice il testo.

### N13. Gli spazi celesti e l’etere

Gli ultimi due capoversi trasformano il risultato tecnico (la resistenza d’inerzia dipende solo dalla densità del mezzo, non dalla sua «sottigliezza») in un argomento cosmologico: un mezzo, per quanto finemente diviso, resiste in proporzione alla sua densità; poiché pianeti e comete non mostrano perdite sensibili di moto, gli spazi celesti sono privi di fluido corporeo, salvo forse vapori tenuissimi e la luce. In questo contesto l’argomento si rivolge contro le teorie dei vortici celesti (non verificato sulle fonti allegate; il Libro II lo sviluppa nella Sezione IX).

---
## Controllo della copertura

Pagine 1726 dai marcatori ‹n› della trascrizione. L’estratto di Motte non ha marcatori di pagina: si indica la parte corrispondente.

| Identificatori | Incipit latino | Contenuto | 1726 | Motte 1846 |
|---|---|---|---|---|
| II.S7.65–II.S7.67 | *Si cylindrus, sphæra & sphærois* | Lemma V | p. 340 | Lemma V |
| II.S7.68–II.S7.69 | *Iisdem positis, corpora prædicta* | Lemma VI | p. 341 | Lemma VI |
| II.S7.70–II.S7.71 | *Si aqua quiescat in canali* | Lemma VII | p. 341 | Lemma VII |
| II.S7.72–II.S7.73 | *Eadem est ratio corporum omnium* … *Corpora fluidis innatantia* | Scolio dei Lemmi | pp. 341–342 | Scholium |
| II.S7.74–II.S7.75 | *Globi, in fluido compresso infinito* | Prop. XXXVIII | p. 342 | Prop. XXXVIII |
| II.S7.76–II.S7.79 | *Globorum, in mediis compressis* … *Globus in fluido compresso quiescente* | Prop. XXXVIII, Cor. 1–4 | pp. 342–343 | Cor. 1–4 |
| II.S7.80–II.S7.81 | *Globi, per fluidum in canali cylindrico* | Prop. XXXIX | p. 343 | Prop. XXXIX |
| II.S7.82 | *In propositionibus duabus novissimis* | Scolio della Prop. XXXIX | p. 343 | Scholium |
| II.S7.83–II.S7.86 | *Globi, in medio fluidissimo* … *Demittatur globus* | Prop. XL, enunciato e regole | p. 344 | Prop. XL |
| II.S7.87–II.S7.88 | *Ut corporis in fluido cadentis* | descrizione e tabella | p. 345 | tabella |
| II.S7.89 | *Ut resistentias fluidorum investigarem* | Scolio: vaso e unità | p. 346 | Scholium |
| II.S7.90–II.S7.91 | *Exper. 1.* | Esper. 1 | pp. 346–347 | Exper. 1 |
| II.S7.92–II.S7.95 | *Exper. 2.* … *Exper. 3.* | Esper. 2–3 | pp. 347–348 | Exper. 2–3 |
| II.S7.96–II.S7.97 | *Exper. 4.* | Esper. 4 | pp. 348–349 | Exper. 4 |
| II.S7.98–II.S7.103 | *Exper. 5.* … *Exper. 7.* | Esper. 5–7 | p. 349 | Exper. 5–7 |
| II.S7.104 | *Causam investigando* | le oscillazioni dei globi | pp. 349–350 | — |
| II.S7.105–II.S7.111 | *Exper. 8.* … *Exper. 11.* (enunciato) | Esper. 8–11 | p. 350 | Exper. 8–11 |
| II.S7.112–II.S7.116 | *Per theoriam cadere debuerunt tempore oscillationum 4659* … *Congruit igitur theoria* | Esper. 11 (teoria), 12, conclusioni sull’acqua | p. 351 | Exper. 11–12 |
| II.S7.117–II.S7.119 | *Exper. 13.* … *Cæterum tempora observata* | Esper. 13, prima tabella, correzione | pp. 351–352 | Exper. 13 |
| II.S7.120–II.S7.121 | *Globorum igitur aere plenorum quintus* | calcolo e seconda tabella | pp. 352–353 | — |
| II.S7.122–II.S7.125 | *Exper. 14.* … tabella | Esper. 14 | pp. 353–354 | Exper. 14 |
| II.S7.126 | *Globorum igitur tam in aëre quam in aqua* | conclusione | p. 354 | — |
| II.S7.127 | *In scholio, quod sectioni sextæ* | pendoli contro cadute | p. 355 | — |
| II.S7.128 | *His ita stabilitis* | legge della perdita di velocità | pp. 355–356 | — |
| II.S7.129–II.S7.130 | *Et quamvis aër* … *Projectilia utique* | mezzi infinitamente fluidi; spazi celesti; etere | p. 356 | fine della Sezione VII |

**Controlli eseguiti.**

1. **Copertura.** Ho riletto in sequenza ogni periodo della trascrizione, da *LEMMA V.* a *pro densitatibus horum fluidorum.*, contro la traduzione: nessuna frase manca. Le quattro tabelle sono riprodotte per intero. I 66 identificatori (II.S7.65–II.S7.130) sono consecutivi e unici (controllo automatico).
2. **Parte B.** `check.py` sul file finale (con `motte-1846-L2-S07.md` e `motte-1846-L2-S08.md` come fonti inglesi): esito nel messaggio di consegna.
3. **Matematica e tabelle.** Script `tmp/18b/verifica.py`: tabella della Prop. XL (105 celle, una cifra non torna: N5); unità dello Scolio (N7); catene di calcolo degli Esper. 1, 2, 4 (N8); tempi teorici degli Esper. 3–12 (N9); Esper. 13 con le correzioni dei tempi e la seconda tabella (N10); Esper. 14 con somme e terza tabella (N11); 1/4586 e il rapporto 4 : 3 (N12).
4. **Motte.** Confronto di tutta la parte corrispondente, compresi i 187 SVG (A.14, A.15).
5. **Rimandi.** Nessun rimando al Libro I; 11 rimandi interni al Libro II verificati (A.17).

**Non ho potuto verificare:**

- **la stampa del 1726**: i refusi e le omissioni di A.12 (in particolare *ut densitatem fluidi* nel Cor. 2 della Prop. XXXVIII, *A−* senza B nella Prop. XL, *1936″*) e la cifra 99999980 della tabella (A.16);
- **Motte 1729**: non so se gli errori di Motte 1846 (formula dell’altezza con − 4,405, peso 3 20/32, «7 0», «7», «18» nelle tabelle) siano già nella prima edizione inglese o nascano nel 1846 o nella conversione dell’EPUB;
- **le dimostrazioni delle Propp. XXXII–XXXVII** del Fascicolo 18a: ho verificato solo gli enunciati e i corollari citati;
- **la paginazione di Motte**: l’estratto non ha marcatori di pagina.

---

## Registro del lavoro successivo

| Unità | Stato |
|---|---|
| Libro II, Sezione VII, seconda parte (Lemmi V–VII, Propp. XXXVIII–XL, Scolio) | **Fascicolo 18b, presente documento, prima versione** |
| Numerazione II.S7.65–130 | Raccordata dal coordinatore con il Fascicolo 18a (II.S7.01–64): spostamento di +14 rispetto alla numerazione provvisoria 51–116 |
| Termini † di A.0 (*sphærois*, *orificium*, *inertia materiæ*, *pondus comparativum*, *minutum tertium*, *libra Romana*, *poli*/*pessulus*, *horologium cum elatere*) | Da armonizzare con il Fascicolo 18a (Propp. XXXVI–XXXVII usano *foramen*, *orificium*, *totus motus*) |
| Refusi e omissioni (A.12, A.16) | Da verificare sulla stampa del 1726 |
| Errori di Motte 1846 (A.14) | Da confrontare con Motte 1729 |
| Pagine interattive | Parte B: 5 unità, 29 passi; la tabella della Prop. XL è fornita come dati (`dati_tabella`) per un grafico velocità/spazio–tempo; gli Esper. 1 e 13 si prestano a un calcolatore passo-passo |
| Revisione filologica e scientifica indipendente | Da eseguire |

Il presente testo è una nuova traduzione assistita da IA. Non riproduce traduzioni italiane o inglesi moderne. **Licenza prevista** (decisione del curatore, Fascicolo 3): testi e traduzioni CC BY-SA 4.0, codice MIT. La trascrizione latina è © The Newton Project; i testi di Motte sono di pubblico dominio.

---

## Parte B — Dati per le pagine interattive

Unità incluse: in questa parte della Sezione VII **non ci sono figure** ([FIG n] assenti nel latino). Ho incluso le unità che hanno una dimostrazione o un calcolo da mostrare per passi: la Prop. XXXVIII (dimostrazione per rapporti), il suo Cor. 2 (velocità limite, che regge tutta la Prop. XL), la Prop. XL (con i dati della tabella nel campo aggiuntivo `dati_tabella`) e due calcoli esemplari dello Scolio (Esper. 1 nell’acqua, Esper. 13 nell’aria). **Escluse**: i Lemmi V–VII (dimostrazioni di una riga), la Prop. XXXIX (*Patet per corol. 2. prop. XXXVII.*), i Cor. 1, 3, 4 della Prop. XXXVIII (senza dimostrazione propria), gli altri esperimenti (stessa procedura dell’Esper. 1).

Convenzioni:

- `la`: testo latino esatto della trascrizione, refusi e frazioni appiattite compresi; i marcatori di pagina ‹n› sono tolti dallo strumento e lasciano parole spezzate («qua tuor»); le letture sono in `nota` e nell’apparato;
- `it`: la traduzione di questo fascicolo;
- `en`: Motte 1846, allineato per senso, con i marcatori `[SVG n]` (check.py li ignora; i valori sono in A.15);
- `figura.mostra`: non essendoci figure, elenca le grandezze e gli oggetti da rendere visibili al passo (grafici, valori, apparato sperimentale).

```json
{
 "fascicolo": "18b-L2-S7",
 "versione": "0.1",
 "data": "2026-11-08",
 "convenzioni": {
  "dipende_da": "solo rimandi citati esplicitamente nella frase latina",
  "en": "Motte 1846, allineato per senso; i marcatori [SVG n] restano nelle stringhe en (check.py li ignora) e vanno sostituiti con le formule quando l'EPUB sarà disponibile",
  "figura.mostra": "elementi da rendere visibili al passo, cumulativi salvo indicazione; nella Sezione VII, seconda parte, non ci sono figure: gli elementi sono grafici, grandezze e oggetti dell'esperimento",
  "la": ""
 },
 "unita": [
  {
   "id": "L2-P38",
   "tipo": "Propositio/Theorema",
   "titolo": "Prop. XXXVIII — resistenza del globo in un fluido compresso infinito",
   "copertura": [
    "II.S7.74",
    "II.S7.75"
   ],
   "fonti": {
    "la": "",
    "en": "Motte 1846, sezione corrispondente (Prop. XXXVIII)"
   },
   "enunciato": {
    "la": "",
    "it": "La resistenza di un globo che avanza uniformemente in un fluido compresso, infinito e non elastico sta alla forza con cui tutta la sua quantità di moto potrebbe essere tolta o generata nel tempo in cui descrive gli otto terzi del suo diametro, come la densità del fluido sta alla densità del globo, con ottima approssimazione.",
    "en": "If a globe move uniformly forward in a compressed, infinite, and non-elastic fluid, its resistance is to the force by which its whole motion may be destroyed or generated, in the time that it describes eight third parts of its diameter, as the density of the fluid to the density of the globe, very nearly."
   },
   "figura_base": {
    "punti": [],
    "oggetti": [
     "globo di diametro D",
     "cilindro circoscritto (diametro D, lunghezza D)",
     "fluido compresso infinito non elastico"
    ],
    "vincoli": [
     "volume globo : volume cilindro circoscritto = 2 : 3",
     "lunghezza di riferimento del cilindro: 4D; del globo: 8/3 D"
    ]
   },
   "passi": [
    {
     "id": "L2-P38-p1",
     "la": "",
     "it": "Il globo, infatti, sta al cilindro circoscritto come due sta a tre; e perciò quella forza che potrebbe togliere tutta la quantità di moto del cilindro mentre il cilindro descrive la lunghezza di quattro diametri toglierà tutta la quantità di moto del globo mentre il globo descrive i due terzi di questa lunghezza, cioè gli otto terzi del proprio diametro.",
     "en": "For the globe is to its circumscribed cylinder as two to three; and therefore the force which can destroy all the motion of the cylinder, while the same cylinder is describing the length of four of its diameters, will destroy all the motion of the globe, while the globe is describing two thirds of this length, that is, eight third parts of its own diameter.",
     "dipende_da": [],
     "figura": {
      "mostra": [
       "globo",
       "cilindro circoscritto",
       "percorso 4D del cilindro",
       "percorso 8/3 D del globo"
      ],
      "evidenzia": [
       "rapporto 2 : 3 dei volumi"
      ]
     },
     "nota": "La trascrizione ha «interna dum»: refuso probabile per «interea dum» (apparato A.12)."
    },
    {
     "id": "L2-P38-p2",
     "la": "",
     "it": "Ora la resistenza del cilindro sta a questa forza, con ottima approssimazione, come la densità del fluido sta alla densità del cilindro o del globo, per la Prop. XXXVII; e la resistenza del globo è uguale alla resistenza del cilindro, per i Lemmi V, VI e VII. C.V.D.",
     "en": "Now the resistance of the cylinder is to this force very nearly as the density of the fluid to the density of the cylinder or globe (by Prop. XXXVII), and the resistance of the globe is equal to the resistance of the cylinder (by Lem. V, VI, and VII). Q.E.D.",
     "dipende_da": [
      "Prop. XXXVII",
      "Lemmi V, VI, VII"
     ],
     "figura": {
      "mostra": [
       "resistenza del cilindro = resistenza del globo"
      ],
      "evidenzia": [
       "densità del fluido : densità del globo"
      ]
     }
    }
   ]
  },
  {
   "id": "L2-P38-Cor2",
   "tipo": "Corollarium",
   "titolo": "Prop. XXXVIII, Cor. 2 — velocità massima di discesa",
   "copertura": [
    "II.S7.77"
   ],
   "fonti": {
    "la": "",
    "en": "Motte 1846, sezione corrispondente (Prop. XXXVIII, Cor. 2)"
   },
   "enunciato": {
    "la": "",
    "it": "La velocità massima con cui un globo, per la forza del suo peso comparativo, può scendere in un fluido resistente è quella che lo stesso globo, con lo stesso peso, può acquistare cadendo senza resistenza e descrivendo nella sua caduta uno spazio che stia ai quattro terzi del suo diametro come la densità [del globo sta alla densità] del fluido.",
    "en": "COR. 2. The greatest velocity, with which a globe can descend by its comparative weight through a resisting fluid, is the same which it may acquire by falling with the same weight, and without any resistance, and in its fall describing a space that is, to four third parts of its diameter as the density of the globe to the density of the fluid."
   },
   "figura_base": {
    "punti": [],
    "oggetti": [
     "globo che cade senza resistenza con il peso comparativo",
     "spazio s = 4/3 D × (densità globo / densità fluido)"
    ],
    "vincoli": [
     "moto uniformemente accelerato: con la velocità finale, nello stesso tempo, si descrive 2s"
    ]
   },
   "passi": [
    {
     "id": "L2-P38-Cor2-p1",
     "la": "",
     "it": "Infatti il globo, nel tempo della sua caduta, con la velocità acquistata cadendo, descriverà uno spazio che starà agli otto terzi del suo diametro come la densità del globo sta alla densità del fluido; e la forza del peso che genera questo moto starà alla forza che potrebbe generare lo stesso moto nel tempo in cui il globo descrive con la stessa velocità gli otto terzi del suo diametro, come la densità del fluido sta alla densità del globo; e perciò, per questa proposizione, la forza del peso sarà uguale alla forza della resistenza, e quindi non può accelerare il globo.",
     "en": "For the globe in the time of its fall, moving with the velocity acquired in falling, will describe a space that will be to eight third parts of its diameter as the density of the globe to the density of the fluid; and the force of its weight which generates this motion will be to the force that can generate the same motion, in the time that the globe describes eight third parts of its diameter, with the same velocity as the density of the fluid to the density of the globe; and therefore (by this Proposition) the force of weight will be equal to the force of resistance, and therefore cannot accelerate the globe.",
     "dipende_da": [
      "Prop. XXXVIII"
     ],
     "figura": {
      "mostra": [
       "caduta libera fino alla velocità H",
       "percorso uniforme 2s con la velocità H",
       "forza del peso",
       "forza di resistenza alla velocità H"
      ],
      "evidenzia": [
       "peso = resistenza alla velocità massima"
      ]
     },
     "nota": "Nell'enunciato la trascrizione omette probabilmente «densitas globi ad» (… ut densitas globi ad densitatem fluidi): apparato A.12. La frase della dimostrazione contiene il marcatore di pagina ‹343›."
    }
   ]
  },
  {
   "id": "L2-P40",
   "tipo": "Propositio/Problema",
   "titolo": "Prop. XL — la resistenza del globo dai fenomeni (con la tabella di caduta)",
   "copertura": [
    "II.S7.83",
    "II.S7.84",
    "II.S7.85",
    "II.S7.86",
    "II.S7.87",
    "II.S7.88"
   ],
   "fonti": {
    "la": "",
    "en": "Motte 1846, sezione corrispondente (Prop. XL)"
   },
   "enunciato": {
    "la": "",
    "it": "Trovare dai fenomeni la resistenza di un globo che avanza in un mezzo fluidissimo compresso.",
    "en": "To find by phenomena the resistance of a globe moving through a perfectly fluid compressed medium."
   },
   "figura_base": {
    "punti": [],
    "oggetti": [
     "grafico della velocità v(P)/H",
     "grafico dello spazio percorso nel fluido, a velocità massima e nel vuoto"
    ],
    "vincoli": [
     "F = 4/3 D × A/(A − B)",
     "G: tempo in cui il globo, con il peso B, cade di F senza resistenza",
     "2F = H × G"
    ]
   },
   "dati_tabella": {
    "colonne": [
     "P/G",
     "velocità (velocità massima = 100000000)",
     "spazio nel fluido (in F)",
     "spazio a velocità massima (in F)",
     "spazio nel vuoto (in F)"
    ],
    "righe": [
     [
      0.001,
      "99999 29/30",
      1e-06,
      0.002,
      1e-06
     ],
     [
      0.01,
      999967,
      0.0001,
      0.02,
      0.0001
     ],
     [
      0.1,
      9966799,
      0.0099834,
      0.2,
      0.01
     ],
     [
      0.2,
      19737532,
      0.0397361,
      0.4,
      0.04
     ],
     [
      0.3,
      29131261,
      0.0886815,
      0.6,
      0.09
     ],
     [
      0.4,
      37994896,
      0.155907,
      0.8,
      0.16
     ],
     [
      0.5,
      46211716,
      0.240229,
      1.0,
      0.25
     ],
     [
      0.6,
      53704957,
      0.3402706,
      1.2,
      0.36
     ],
     [
      0.7,
      60436778,
      0.4545405,
      1.4,
      0.49
     ],
     [
      0.8,
      66403677,
      0.5815071,
      1.6,
      0.64
     ],
     [
      0.9,
      71629787,
      0.7196609,
      1.8,
      0.81
     ],
     [
      1,
      76159416,
      0.8675617,
      2,
      1
     ],
     [
      2,
      96402758,
      2.6500055,
      4,
      4
     ],
     [
      3,
      99505475,
      4.618657,
      6,
      9
     ],
     [
      4,
      99932930,
      6.6143765,
      8,
      16
     ],
     [
      5,
      99990920,
      8.6137964,
      10,
      25
     ],
     [
      6,
      99998771,
      10.6137179,
      12,
      36
     ],
     [
      7,
      99999834,
      12.6137073,
      14,
      49
     ],
     [
      8,
      99999980,
      14.6137059,
      16,
      64
     ],
     [
      9,
      99999997,
      16.6137057,
      18,
      81
     ],
     [
      10,
      "99999999 3/5",
      18.6137056,
      20,
      100
     ]
    ],
    "nota": "Valori come letti nella trascrizione (frazioni ricostruite). Verifica: tutte le cifre coincidono con 10^8·tanh(P/G) e 2·ln cosh(P/G), salvo la velocità a 8G (calcolata 99999977,5; stampata 99999980): nota N5."
   },
   "passi": [
    {
     "id": "L2-P40-p1",
     "la": "",
     "it": "Sia A il peso del globo nel vuoto, B il suo peso nel mezzo resistente, D il diametro del globo, F uno spazio che stia a 4/3 D come la densità del globo sta alla densità del mezzo, cioè come A sta ad A − [B], G il tempo in cui il globo, cadendo senza resistenza con il peso B, descrive lo spazio F, e H la velocità che il globo acquista in questa sua caduta. Allora H sarà la velocità massima con cui il globo, con il suo peso B, può scendere nel mezzo resistente, per il Cor. 2 della Prop. XXXVIII; e la resistenza che il globo subisce scendendo con quella velocità sarà uguale al suo peso B; la resistenza che subisce con qualsiasi altra velocità starà invece al peso B nel rapporto duplicato di questa velocità alla velocità massima H, per il Cor. 1 della Prop. XXXVIII.",
     "en": "Let A be the weight of the globe in vacuo, B its weight in the resisting medium, D the diameter of the globe, F a space which is to [SVG 745] as the density of the globe to the density of the medium, that is, as A to A - B, G the time in which the globe falling with the weight B without resistance describes the space F, and H the velocity which the body acquires by that fall. Then H will be the greatest velocity with which the globe can possibly descend with the weight B in the resisting medium, by Cor. 2, Prop. XXXVIII; and the resistance which the globe meets with, when descending with that velocity, will be equal to its weight B; and the resistance it meets with in any other velocity will be to the weight B in the duplicate ratio of that velocity to the greatest velocity H, by Cor. 1, Prop. XXXVIII.",
     "dipende_da": [
      "Prop. XXXVIII, Cor. 2",
      "Prop. XXXVIII, Cor. 1"
     ],
     "figura": {
      "mostra": [
       "A, B, D",
       "spazio F",
       "tempo G",
       "velocità massima H"
      ],
      "evidenzia": [
       "resistenza alla velocità H = peso B"
      ]
     },
     "nota": "La trascrizione ha «ut A ad A−,»: manca B (Motte: «as A to A - B»). «43D» = 4/3 D. Motte: [SVG 745] = 4/3 D (visto)."
    },
    {
     "id": "L2-P40-p2",
     "la": "",
     "it": "Questa è la resistenza che nasce dall’inerzia della materia del fluido.",
     "en": "This is the resistance that arises from the inactivity of the matter of the fluid.",
     "dipende_da": [],
     "figura": {
      "mostra": [
       "resistenza d'inerzia"
      ]
     }
    },
    {
     "id": "L2-P40-p3",
     "la": "",
     "it": "Quella che nasce dall’elasticità, dalla tenacità e dall’attrito delle sue parti si indagherà così.",
     "en": "That resistance which arises from the elasticity, tenacity, and friction of its parts, may be thus investigated.",
     "dipende_da": [],
     "figura": {
      "mostra": [
       "altre resistenze (elasticità, tenacità, attrito)"
      ]
     }
    },
    {
     "id": "L2-P40-p4",
     "la": "",
     "it": "Si lasci andare il globo in modo che scenda nel fluido per il suo peso B; e sia P il tempo di caduta, espresso in secondi se il tempo G è espresso in secondi.",
     "en": "Let the globe be let fall so that it may descend in the fluid by the weight B; and let P be the time of falling, and let that time be expressed in seconds, if the time G be given in seconds.",
     "dipende_da": [],
     "figura": {
      "mostra": [
       "tempo di caduta P"
      ]
     }
    },
    {
     "id": "L2-P40-p5",
     "la": "",
     "it": "Si trovi il numero assoluto N che corrisponde al logaritmo 0,4342944819 × 2P/G, e sia L il logaritmo del numero (N + 1)/N: la velocità acquistata cadendo sarà (N − 1)H/(N + 1), e l’altezza descritta sarà 2PF/G − 1,3862943611F + 4,605170186LF.",
     "en": "Find the absolute number N agreeing to the logarithm [SVG 746], and let L be the logarithm of the number [SVG 747]; and the velocity acquired in falling will be [SVG 748], and the height described will be [SVG 749].",
     "dipende_da": [],
     "figura": {
      "mostra": [
       "N = 10^(0,4342944819·2P/G)",
       "L = log((N+1)/N)",
       "velocità (N−1)H/(N+1)",
       "altezza 2PF/G − 1,3862943611F + 4,605170186LF"
      ],
      "evidenzia": [
       "curva della velocità",
       "curva dello spazio"
      ]
     },
     "nota": "Frazioni appiattite: «0,43429448192PG» = 0,4342944819 × 2P/G; «N+1N» = (N+1)/N; «N−1N+1H» = (N−1)H/(N+1); «2PFG» = 2PF/G. Motte: SVG 746–749 (visti); la SVG 749 di Motte ha per errore «− 4,405170186LF» invece di «+ 4,605170186LF»."
    },
    {
     "id": "L2-P40-p6",
     "la": "",
     "it": "Se il fluido è abbastanza profondo, si può trascurare il termine 4,605170186LF; e 2PF/G − 1,3862943611F sarà l’altezza descritta, con ottima approssimazione.",
     "en": "If the fluid be of a sufficient depth, we may neglect the term [SVG 750]; and [SVG 751] will be the altitude described, nearly.",
     "dipende_da": [],
     "figura": {
      "mostra": [
       "asintoto 2PF/G − 1,3862943611F"
      ],
      "evidenzia": [
       "termine trascurabile 4,605170186LF"
      ]
     },
     "nota": "Motte: SVG 750–751 (visti); la SVG 750 ha per errore 4,405170186LF."
    },
    {
     "id": "L2-P40-p7",
     "la": "",
     "it": "Queste cose sono evidenti per la Prop. IX del Libro II e i suoi corollari, nell’ipotesi che il globo non subisca altra resistenza che quella che nasce dall’inerzia della materia.",
     "en": "These things appear by Prop. IX, Book II, and its Corollaries, and are true upon this supposition, that the globe meets with no other resistance but that which arises from the inactivity of matter.",
     "dipende_da": [
      "Libro II, Prop. IX e corollari"
     ],
     "figura": {
      "mostra": [
       "ipotesi: sola resistenza d'inerzia"
      ]
     }
    },
    {
     "id": "L2-P40-p8",
     "la": "",
     "it": "Se invece subisce in più un’altra resistenza, la discesa sarà più lenta, e dal ritardo si conoscerà la quantità di questa resistenza.",
     "en": "Now if it really meet with any resistance of another kind, the descent will be slower, and from the quantity of that retardation will be known the quantity of this new resistance.",
     "dipende_da": [],
     "figura": {
      "mostra": [
       "confronto fra caduta osservata e caduta teorica"
      ]
     }
    }
   ]
  },
  {
   "id": "L2-S7-Schol-Exp1",
   "tipo": "Scholium/Experimentum",
   "titolo": "Scolio, Esper. 1 — il calcolo completo per un globo che cade nell'acqua",
   "copertura": [
    "II.S7.90",
    "II.S7.91"
   ],
   "fonti": {
    "la": "",
    "en": "Motte 1846, sezione corrispondente (Scholium, Exper. 1)"
   },
   "enunciato": {
    "la": "",
    "it": "Un globo il cui peso era di 156 ¼ grani nell’aria e di 77 grani nell’acqua descrisse l’intera altezza di 112 pollici in un tempo di quattro secondi.",
    "en": "EXPER. 1. A globe whose weight was [SVG 838] grains in air, and 77 grains in water, described the whole height of 112 inches in 4 seconds."
   },
   "figura_base": {
    "punti": [],
    "oggetti": [
     "vaso quadrato di 9 pollici di lato",
     "globo di cera e piombo",
     "altezza di caduta 112 pollici"
    ],
    "vincoli": [
     "globo d'acqua di 1 pollice di diametro: 132,8 grani nel vuoto",
     "nel vuoto, in 1 s, un grave cade di 193 1/3 pollici"
    ]
   },
   "passi": [
    {
     "id": "L2-X1-p1",
     "la": "",
     "it": "Il peso del globo nel vuoto è di 156 13/38 grani, e l’eccesso di questo peso sul peso del globo nell’acqua è di 79 13/38 grani.",
     "en": "The weight of this globe in vacuo is [SVG 839] grains; and the excess of this weight above the weight of the globe in water is [SVG 840] grains.",
     "dipende_da": [],
     "figura": {
      "mostra": [
       "peso nel vuoto A = 156 13/38 grani",
       "eccesso A − B = 79 13/38 grani"
      ]
     },
     "nota": "«1561338» = 156 13/38; «791338» = 79 13/38."
    },
    {
     "id": "L2-X1-p2",
     "la": "",
     "it": "Ne risulta il diametro del globo di 0,84224 parti di pollice.",
     "en": "Hence the diameter of the globe appears to be 0,84224 parts of an inch.",
     "dipende_da": [],
     "figura": {
      "mostra": [
       "diametro D = 0,84224 pollici"
      ],
      "evidenzia": [
       "D³ = (A − B)/132,8"
      ]
     }
    },
    {
     "id": "L2-X1-p3",
     "la": "",
     "it": "Ora, come quell’eccesso sta al peso del globo nel vuoto, così la densità dell’acqua sta alla densità del globo, e così gli otto terzi del diametro del globo (cioè 2,24597 pollici) stanno allo spazio 2F, che perciò sarà di 4,4256 pollici.",
     "en": "Then it will be, as that excess to the weight of the globe in vacuo, so is the density of the water to the density of the globe; and so is [SVG 841] parts of the diameter of the globe (viz. 2,24597 inches) to the space 2F, which will be therefore 4,4256 inches.",
     "dipende_da": [],
     "figura": {
      "mostra": [
       "8/3 D = 2,24597 pollici",
       "2F = 4,4256 pollici"
      ]
     }
    },
    {
     "id": "L2-X1-p4",
     "la": "",
     "it": "Il globo, in un tempo di un secondo, cadendo nel vuoto con tutto il suo peso di 156 13/38 grani, descriverà 193 ⅓ pollici; e con il peso di 77 grani, nello stesso tempo, cadendo senza resistenza nell’acqua, descriverà 95,219 pollici; e nel tempo G, che sta a un secondo nel rapporto subduplicato dello spazio F, ossia 2,2128 pollici, a 95,219 pollici, descriverà 2,2128 pollici e acquisterà la velocità massima H con cui può scendere nell’acqua.",
     "en": "Now a globe falling in vacuo with its whole weight of [SVG 839] grains in one second of time will describe [SVG 842] inches; and falling in water in the same time with the weight of 77 grains without resistance, will describe 95,219 inches; and in the time G, which is to one second of time in the subduplicate ratio of the space F, or of 2,2128 inches to 95,219 inches, will describe 2,2128 inches, and will acquire the greatest velocity H with which it is capable of descending in water.",
     "dipende_da": [],
     "figura": {
      "mostra": [
       "193 1/3 pollici in 1 s (peso A)",
       "95,219 pollici in 1 s (peso B)",
       "F = 2,2128 pollici"
      ],
      "evidenzia": [
       "G = √(F/95,219) s"
      ]
     },
     "nota": "«19313» = 193 1/3."
    },
    {
     "id": "L2-X1-p5",
     "la": "",
     "it": "Il tempo G è dunque di 0″,15244.",
     "en": "Therefore the time G is 0″,15244.",
     "dipende_da": [],
     "figura": {
      "mostra": [
       "G = 0,15244 s"
      ]
     }
    },
    {
     "id": "L2-X1-p6",
     "la": "",
     "it": "E in questo tempo G, con quella velocità massima H, il globo descriverà lo spazio 2F di 4,4256 pollici; e perciò in un tempo di quattro secondi descriverà uno spazio di 116,1245 pollici.",
     "en": "And in this time G, with that greatest velocity H, the globe will describe the space 2F, which is 4,4256 inches; and therefore in 4 seconds will describe a space of 116,1245 inches.",
     "dipende_da": [],
     "figura": {
      "mostra": [
       "2F·P/G = 116,1245 pollici in 4 s"
      ]
     }
    },
    {
     "id": "L2-X1-p7",
     "la": "",
     "it": "Si sottragga lo spazio 1,3862944F, ossia 3,0676 pollici, e resterà lo spazio di 113,0569 pollici, che il globo, cadendo nell’acqua in un vaso amplissimo, descriverà in un tempo di quattro secondi.",
     "en": "Subduct the space 1,3862944F, or 3,0676 inches, and there will remain a space of 113,0569 inches, which the globe falling through water in a very wide vessel will describe in 4 seconds.",
     "dipende_da": [],
     "figura": {
      "mostra": [
       "1,3862944F = 3,0676 pollici",
       "113,0569 pollici in un vaso amplissimo"
      ]
     },
     "nota": "La frase contiene il marcatore di pagina ‹347› («qua ‹347› tuor»)."
    },
    {
     "id": "L2-X1-p8",
     "la": "",
     "it": "Questo spazio, per la strettezza del predetto vaso di legno, deve essere diminuito nel rapporto composto dal rapporto subduplicato dell’orifizio del vaso all’eccesso di questo orifizio sul semicerchio massimo del globo e dal rapporto semplice dello stesso orifizio al suo eccesso sul cerchio massimo del globo, cioè nel rapporto di 1 a 0,9914.",
     "en": "But this space, by reason of the narrowness of the wooden vessel before mentioned, ought to be diminished in a ratio compounded of the subduplicate ratio of the orifice of the vessel to the excess of this orifice above half a great circle of the globe, and of the simple ratio of the same orifice to its excess above a great circle of the globe, that is, in a ratio of 1 to 0,9914.",
     "dipende_da": [],
     "figura": {
      "mostra": [
       "orifizio del vaso 81 pollici quadrati",
       "cerchio massimo del globo"
      ],
      "evidenzia": [
       "fattore 0,9914"
      ]
     }
    },
    {
     "id": "L2-X1-p9",
     "la": "",
     "it": "Fatto ciò, si avrà lo spazio di 112,08 pollici, che il globo, cadendo nell’acqua in questo vaso di legno, avrebbe dovuto descrivere secondo la teoria in un tempo di quattro secondi, con ottima approssimazione.",
     "en": "This done, we have a space of 112,08 inches, which a globe falling through the water in this wooden vessel in 4 seconds of time ought nearly to describe by this theory;",
     "dipende_da": [],
     "figura": {
      "mostra": [
       "112,08 pollici (teoria)"
      ]
     }
    },
    {
     "id": "L2-X1-p10",
     "la": "",
     "it": "Per esperimento, invece, ne descrisse 112.",
     "en": "but it described 112 inches by the experiment.",
     "dipende_da": [],
     "figura": {
      "mostra": [
       "112 pollici (esperimento)"
      ],
      "evidenzia": [
       "confronto teoria–esperimento"
      ]
     }
    }
   ]
  },
  {
   "id": "L2-S7-Schol-Exp13",
   "tipo": "Scholium/Experimentum",
   "titolo": "Scolio, Esper. 13 — il quinto globo d'aria dalla cupola di San Paolo",
   "copertura": [
    "II.S7.120"
   ],
   "fonti": {
    "la": "",
    "en": "Motte 1846, sezione corrispondente (Scholium, Exper. 13)"
   },
   "enunciato": {
    "la": "",
    "it": "Dei globi pieni d’aria, dunque, il quinto, costruito con un diametro di cinque pollici e un peso di 483 grani, cadde nel tempo di 8″ 12‴, descrivendo l’altezza di 220 piedi.",
    "en": "Therefore the fifth in order among the globes that were full of air being 5 inches in diameter, and 483 grains in weight, fell in 8″ 12‴, describing a space of 220 feet."
   },
   "figura_base": {
    "punti": [],
    "oggetti": [
     "globo di vetro pieno d'aria, D = 5 pollici, peso 483 grani",
     "altezza 220 piedi"
    ],
    "vincoli": [
     "densità dell'aria : densità dell'acqua = 1 : 860"
    ]
   },
   "passi": [
    {
     "id": "L2-X13-p1",
     "la": "",
     "it": "Il peso dell’acqua uguale a questo globo è di 16600 grani; e il peso dell’aria uguale allo stesso è di 16600/860 grani, ossia 19 3/10 grani; e perciò il peso del globo nel vuoto è di 502 3/10 grani; e questo peso sta al peso dell’aria uguale al globo come 502 3/10 sta a 19 3/10, e così 2F sta agli otto terzi del diametro del globo, cioè a 13 ⅓ pollici.",
     "en": "The weight of a bulk of water equal to this globe is 16600 grains; and the weight of an equal bulk of air is [SVG 883] grains, or [SVG 884] grains; and therefore the weight of the globe in vacuo is [SVG 885] grains; and this weight is to the weight of a bulk of air equal to the globe as [SVG 885] to [SVG 884]; and so is 2F to [SVG 841] of the diameter of the globe, that is, to [SVG 886] inches.",
     "dipende_da": [],
     "figura": {
      "mostra": [
       "acqua 16600 grani",
       "aria 19 3/10 grani",
       "A = 502 3/10 grani"
      ],
      "evidenzia": [
       "2F : 8/3 D = A : aria"
      ]
     },
     "nota": "«16600860» = 16600/860; «19310» = 19 3/10; «502310» = 502 3/10; «1313» = 13 1/3."
    },
    {
     "id": "L2-X13-p2",
     "la": "",
     "it": "Ne risulta 2F di 28 piedi e 11 pollici.",
     "en": "Whence 2F becomes 28 feet 11 inches.",
     "dipende_da": [],
     "figura": {
      "mostra": [
       "2F = 28 piedi 11 pollici"
      ]
     }
    },
    {
     "id": "L2-X13-p3",
     "la": "",
     "it": "Il globo, cadendo nel vuoto con tutto il suo peso di 502 3/10 grani, descrive in un tempo di un secondo 193 ⅓ pollici, come sopra; con il peso di 483 grani descrive 185,905 pollici; e con lo stesso peso di 483 grani descrive anche nel vuoto lo spazio F, ossia 14 piedi e 5 ½ pollici, nel tempo di 57‴ 58⁗, e acquista la velocità massima con cui potrebbe scendere nell’aria.",
     "en": "A globe, falling in vacuo with its whole weight of [SVG 885] grains, will in one second of time describe [SVG 842] inches as above; and with the weight of 483 grains will describe 185,905 inches; and with that weight 483 grains in vacuo will describe the space F, or 14 feet [SVG 736] inches, in the time of 57‴ 58⁗, and acquire the greatest velocity it is capable of descending with in the air.",
     "dipende_da": [],
     "figura": {
      "mostra": [
       "185,905 pollici in 1 s",
       "F = 14 piedi 5 1/2 pollici",
       "G = 57‴ 58⁗"
      ]
     },
     "nota": "La frase contiene il marcatore di pagina ‹353›."
    },
    {
     "id": "L2-X13-p4",
     "la": "",
     "it": "Con questa velocità il globo, nel tempo di 8″ 12‴, descriverà lo spazio di 245 piedi e 5 ⅓ pollici.",
     "en": "With this velocity the globe in 8″ 12‴ of time will describe 245 feet and [SVG 887] inches.",
     "dipende_da": [],
     "figura": {
      "mostra": [
       "245 piedi 5 1/3 pollici a velocità massima"
      ]
     }
    },
    {
     "id": "L2-X13-p5",
     "la": "",
     "it": "Si tolga 1,3863F, ossia 20 piedi e ½ pollice, e resteranno 225 piedi e 5 pollici.",
     "en": "Subduct 1,3863F, or 20 feet and [SVG 643] an inch, and there remain 225 feet 5 inches.",
     "dipende_da": [],
     "figura": {
      "mostra": [
       "1,3863F = 20 piedi 1/2 pollice",
       "225 piedi 5 pollici"
      ]
     }
    },
    {
     "id": "L2-X13-p6",
     "la": "",
     "it": "Questo spazio, dunque, il globo avrebbe dovuto descrivere cadendo nel tempo di 8″ 12‴ secondo la teoria.",
     "en": "This space, therefore, the falling globe ought by the theory to describe in 8″ 12‴.",
     "dipende_da": [],
     "figura": {
      "mostra": [
       "225 piedi 5 pollici (teoria)"
      ]
     },
     "nota": "La trascrizione alterna ″′ e ′″ per i terzi; Motte usa ‴."
    },
    {
     "id": "L2-X13-p7",
     "la": "",
     "it": "Per esperimento, invece, descrisse lo spazio di 220 piedi.",
     "en": "But by the experiment it described a space of 220 feet.",
     "dipende_da": [],
     "figura": {
      "mostra": [
       "220 piedi (esperimento)"
      ]
     }
    },
    {
     "id": "L2-X13-p8",
     "la": "",
     "it": "La differenza è insensibile.",
     "en": "The difference is insensible.",
     "dipende_da": [],
     "figura": {
      "mostra": [
       "differenza 5 piedi 5 pollici"
      ],
      "evidenzia": [
       "differenza giudicata insensibile"
      ]
     }
    }
   ]
  }
 ]
}

```
