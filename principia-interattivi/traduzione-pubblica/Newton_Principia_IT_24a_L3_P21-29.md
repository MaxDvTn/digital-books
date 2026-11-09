> **Copia pubblica.** In questa versione i campi `"la"` della Parte B sono vuoti: le frasi latine vengono dalla trascrizione del Newton Project, che non si ridistribuisce. Il latino del 1726 si legge su newtonproject.ox.ac.uk.

# Isaac Newton
# Principi matematici della filosofia naturale

## Fascicolo 24a — Libro III: precessione, maree e moti della Luna fino alla variazione

**Nuova traduzione italiana di lavoro dal latino del 1726, confrontata con l’inglese di Andrew Motte nell’edizione del 1846.**

Versione 0.1 — 8 novembre 2026. Preparata con Claude (Anthropic) per Massimo Bosetti.

### Stato e perimetro

Questo fascicolo prosegue il Fascicolo 23 (Libro III, Propp. XV–XX). Traduce integralmente la prima parte del gruppo G5 del Libro III, *De mundi systemate*: le **Proposizioni XXI–XXIX**, dalla precessione degli equinozi e dalla nutazione (Prop. XXI), attraverso l’elenco delle disuguaglianze lunari (Prop. XXII), i satelliti di Giove (Prop. XXIII) e la lunga trattazione delle maree (Prop. XXIV), fino ai calcoli lunari delle Propp. XXV–XXIX: la forza del Sole che perturba la Luna, l’incremento orario dell’area, la distanza dal moto orario, i diametri dell’orbita senza eccentricità e la variazione. Si ferma prima di «PROPOSITIO XXX.». **Il seguito (Propp. XXX–XXXIII, lo Scolio con le Propp. I–II di Machin e lo Scolio finale) è nel Fascicolo 24b.** È una traduzione di lavoro, non un’edizione critica validata.

Gli identificatori **III.G5.01–III.G5.36** e i titoli tematici tra parentesi sono aggiunte editoriali. Servono a orientare la lettura e a controllare la completezza. I numeri romani delle proposizioni, dei teoremi e dei problemi, e i numeri dei corollari, appartengono al testo originale. Le integrazioni del curatore sono tra parentesi quadre. Le note poste dopo la traduzione non fanno parte del testo di Newton.

In coda al fascicolo c’è la **Parte B**, con i dati strutturati per le pagine interattive: nove unità, una per proposizione; 86 passi per le Propp. XXIII (calcolo dei satelliti), XXIV (solo il capoverso con la figura dello sferoide di marea), XXV, XXVI, XXVII, XXVIII e XXIX; le Propp. XXI e XXII entrano senza passi, perché la loro dimostrazione è fatta di soli rimandi.

### Fonti effettivamente consultate

1. **Latino di riferimento.** Isaac Newton, *Philosophiæ Naturalis Principia Mathematica*, terza edizione, Londra, 1726, Libro III, **pp. 422–437** (la Prop. XXI comincia a p. 422; i marcatori di pagina della trascrizione vanno da ‹423› a ‹437›, e ‹437› cade nell’ultima frase della Prop. XXIX). Trascrizione normalizzata del Newton Project, documento **NATP00303**, estratta in testo semplice senza correzioni: `fonti/latino-1726/latino-1726-L3-P21-33.md`, righe 12–102. Figure citate come [FIG] (Propp. XXIV, XXV, XXVI, XXVIII, XXIX), non disponibili. Per i rimandi interni al Libro III ho letto anche `latino-1726-L3-P01-14.md` (Prop. IV) e `latino-1726-L3-Regole-Fenomeni.md` (Fenomeni I e IV), e, nello stesso file del gruppo, la Prop. XXXII (moto medio dei nodi).
2. **Inglese di confronto.** *Newton’s Principia*, traduzione di Andrew Motte, New York, Daniel Adee, 1846, Book III, Propp. XXI–XXIX (Project Gutenberg n. 76404), estratto `fonti/motte-1846/motte-1846-L3-P21-33.md`, righe 7–641. L’estratto non ha marcatori di pagina: le pagine Motte sono indicate come «sezione corrispondente». Le formule stampate come immagini (`[SVG 963]`, `[SVG 968]`, `[SVG 1023]`–`[SVG 1041]`) sono state lette nel LaTeX di `fonti/motte-1846/svg_tex.tsv`.
3. **Brief comune**, **addendum del Libro II**, **istruzioni del Libro III**; **Fascicoli 3, 5 e 20** (modelli di formato); per i rimandi, **Fascicoli 3** (Leggi), **4** (Libro I, Sezione I, Lemma X), **5** (Sezione II, Prop. IV) e **10** (Sezione XI, Propp. LXV–LXVI e corollari).

Non ho consultato né riprodotto traduzioni moderne. Non ho potuto vedere la stampa del 1726 né le figure originali: le relazioni geometriche sono ricostruite dalle sole lettere del testo.

### Criteri di traduzione

- Il testo guida è il latino; l’inglese di Motte serve a controllare le interpretazioni ed è annotato quando aggiunge, omette o si discosta.
- Si applicano il **glossario comune** del brief, il **glossario del Libro II** e il **glossario del Libro III** con i termini fissati dal coordinatore: *nodi* «nodi»; *præcessio æquinoctiorum* (qui *puncta æquinoctialia regredi*) «precessione degli equinozi»; *æstus maris* «maree», *fluxus / refluxus* «flusso / riflusso»; *variatio* «variazione»; *æquatio* «equazione» (nota alla prima occorrenza); *syzygiæ, quadraturæ, octantes* «sizigie, quadrature, ottanti»; *apogæum / perigæum* «apogeo / perigeo»; *conjunctio / oppositio* «congiunzione / opposizione»; *aphelium / perihelium* «afelio / perielio»; *motus medius* «moto medio»; *eccentricitas* «eccentricità»; *latitudo* «latitudine»; *declinatio* «declinazione»; *meridianus* «meridiano»; *horizon* «orizzonte»; *diameter apparens* «diametro apparente»; *semidiameter* «semidiametro»; *sphærois* «sferoide»; *axis, æquator, poli* «asse, equatore, poli»; *orbis magnus* «orbe magno»; *orbis* (orbita) «orbita»; *vis solis ad perturbandos motus lunæ* «forza del Sole che perturba i moti della Luna»; *mediocris distantia* «distanza media»; *ratio duplicata / triplicata / subduplicata* «rapporto duplicato / triplicato / subduplicato»; *reciproce* «inversamente»; *conjunctim* «considerate congiuntamente»; *applicare ad* «dividere per»; *in consequentia / in antecedentia* «in conseguenza / in antecedenza»; *tempus periodicum* «tempo periodico»; *quamproxime* «con ottima approssimazione»; *constanter* «senza interruzione»; *nisi quatenus* «se non in quanto»; *sinus versus* «seno verso»; *angulus contactus* «angolo di contatto»; *ratio ultima* «rapporto ultimo»; *vis acceleratrix*, *gravitas acceleratrix* «forza acceleratrice», «gravità acceleratrice»; *pes* «piede»; Q.E.I. «C.V.T.». Sole, Luna, Terra, Giove, Saturno con la maiuscola anche dove il latino ha la minuscola.
- Le estensioni del glossario proprie di questo fascicolo sono elencate e motivate nel § A.0.
- Gli enunciati latini all’infinito (teoremi) sono resi con l’indicativo; quelli dei problemi (*Invenire…*, *derivare…*) con l’infinito, come nei fascicoli precedenti.
- Le formule appiattite della trascrizione («3⁢PK×TKTP», «10011915», «AT+CT2», «60⁤12») sono ricostruite con il confronto di Motte e scritte con la barra (3PK × TK/TP, 100/11915, (AT + CT)/2, 60 ½); le abbreviazioni *ATq*, *ATcub.*, *ATqq* diventano AT², AT³, AT⁴. Le letture sono dichiarate nel § A.10. Le espressioni algebriche della Prop. XXVIII sono di Newton, non moderne: restano nel testo.
- Le date, le ore e i minuti restano come in Newton: «dierum 27. hor. 7. min. 43.» → «27 giorni 7 ore 43 minuti»; la forma abbreviata «27d. 7h. 43′» → «27g 7h 43′». I gradi restano nella notazione sessagesimale (8° 24′; 5″ 12‴).
- I nomi propri di luoghi e di persone sono resi nella forma moderna (Plymouth, Bristol, Tonchino, Luzon; Halley, Colepress, Sturmy), con la forma latina nel § A.0.
- Nessuna formula moderna entra nel testo tradotto.

---

## Traduzione italiana

### Libro III. Il sistema del mondo (seguito)

### Proposizione XXI. Teorema XVII (precessione degli equinozi e nutazione)

**[III.G5.01]** **I punti equinoziali retrocedono, e l’asse della Terra, con un moto di nutazione, a ogni rivoluzione annua si inclina due volte verso l’eclittica e due volte ritorna alla posizione di prima.**

**[III.G5.02]** Risulta dal Cor. 20 della Prop. LXVI del Libro I. Questo moto di nutazione, però, deve essere piccolissimo, e appena sensibile, se pure lo è.

### Proposizione XXII. Teorema XVIII (tutti i moti della Luna seguono dai principi)

**[III.G5.03]** **Tutti i moti della Luna, e tutte le disuguaglianze dei suoi moti, seguono dai principi esposti.**

**[III.G5.04]** Che i pianeti maggiori, mentre sono portati attorno al Sole, possano trasportare altri pianeti minori che ruotano attorno a loro, e che questi minori debbano ruotare in ellissi che hanno i fuochi nei centri dei maggiori, risulta dalla Prop. LXV del Libro I. Dall’azione del Sole, però, i loro moti saranno perturbati in molti modi, e saranno affetti dalle disuguaglianze che si osservano nella nostra Luna. Questa, infatti (per i Cor. 2, 3, 4 e 5 della Prop. LXVI), si muove più velocemente, con un raggio condotto alla Terra descrive un’area maggiore in rapporto al tempo, ha un’orbita meno curva, e perciò si avvicina di più alla Terra, nelle sizigie che nelle quadrature, se non in quanto lo impedisce il moto dell’eccentricità. L’eccentricità, infatti, è massima (per il Cor. 9 della Prop. LXVI) quando l’apogeo della Luna si trova nelle sizigie, e minima quando lo stesso apogeo sta nelle quadrature; e di qui la Luna nel perigeo è più veloce e più vicina a noi, nell’apogeo invece più lenta e più lontana, nelle sizigie che nelle quadrature. Inoltre l’apogeo avanza e i nodi retrocedono, ma con moto non uniforme. E l’apogeo (per i Cor. 7 e 8 della Prop. LXVI) avanza più velocemente nelle sue sizigie, retrocede più lentamente nelle quadrature, e per l’eccesso dell’avanzamento sulla retrocessione è portato ogni anno in conseguenza. I nodi invece (per il Cor. [11] della Prop. LXVI) sono fermi nelle loro sizigie e retrocedono velocissimamente nelle quadrature. Ma anche la latitudine massima della Luna è maggiore nelle sue quadrature (per il Cor. 10 della Prop. LXVI) che nelle sizigie; e il moto medio è più lento nel perielio della Terra (per il Cor. 6 della Prop. LXVI) che nel suo afelio. E queste sono le disuguaglianze più notevoli osservate dagli astronomi.

**[III.G5.05]** Vi sono anche alcune altre disuguaglianze, non osservate dagli astronomi precedenti, dalle quali i moti lunari sono perturbati a tal punto che finora non si è potuto ricondurli con alcuna legge a una regola certa. Infatti le velocità, ossia i moti orari, dell’apogeo e dei nodi della Luna, e le loro equazioni, come pure la differenza fra l’eccentricità massima nelle sizigie e la minima nelle quadrature, e la disuguaglianza che si chiama variazione, aumentano e diminuiscono nel corso dell’anno (per il Cor. 14 della Prop. LXVI) in rapporto triplicato del diametro apparente del Sole. E la variazione, inoltre, aumenta o diminuisce in rapporto duplicato del tempo fra le quadrature, con ottima approssimazione (per i Cor. 1 e 2 del Lemma X e il Cor. 16 della Prop. LXVI del Libro I); ma questa disuguaglianza, nel calcolo astronomico, si suole riferire alla prostaferesi della Luna e confondere con essa.

### Proposizione XXIII. Problema V (i satelliti di Giove e di Saturno)

**[III.G5.06]** **Derivare dai moti lunari i moti disuguali dei satelliti di Giove e di Saturno.**

**[III.G5.07]** Dai moti della nostra Luna si derivano così i moti analoghi delle lune, ossia dei satelliti, di Giove. Il moto medio dei nodi del satellite più esterno di Giove sta al moto medio dei nodi della nostra Luna nel rapporto composto dal rapporto duplicato del tempo periodico della Terra attorno al Sole al tempo periodico di Giove attorno al Sole e dal rapporto semplice del tempo periodico del satellite attorno a Giove al tempo periodico della Luna attorno alla Terra (per il Cor. 16 della Prop. LXVI del Libro I); e perciò in cento anni quel nodo compie 8° 24′ in antecedenza. I moti medi dei nodi dei satelliti interni stanno al moto di questo come i loro tempi periodici stanno al tempo periodico di questo (per lo stesso corollario), e di qui sono dati. Il moto dell’auge di ciascun satellite in conseguenza sta poi al moto dei suoi nodi in antecedenza come il moto dell’apogeo della nostra Luna sta al moto dei suoi nodi (per lo stesso corollario), e di qui è dato. Il moto dell’auge così trovato deve però essere diminuito nel rapporto di 5 a 9, o di circa 1 a 2, per una causa che qui non ho modo di esporre. Le equazioni massime dei nodi e dell’auge di ciascun satellite stanno all’incirca alle equazioni massime dei nodi e dell’auge della Luna, rispettivamente, come i moti dei nodi e dell’auge dei satelliti nel tempo di una rivoluzione delle prime equazioni stanno ai moti dei nodi e dell’apogeo della Luna nel tempo di una rivoluzione delle seconde. La variazione di un satellite visto da Giove sta alla variazione della Luna come stanno fra loro i moti totali dei nodi nei tempi in cui il satellite e la Luna ritornano al Sole, per lo stesso corollario; e perciò nel satellite più esterno non supera 5″ 12‴.

### Proposizione XXIV. Teorema XIX (le maree)

**[III.G5.08]** **Il flusso e il riflusso del mare nascono dalle azioni del Sole e della Luna.**

**[III.G5.09]** Che il mare, in ogni giorno tanto lunare quanto solare, debba gonfiarsi due volte e due volte ritirarsi risulta dai Cor. 19 e 20 della Prop. LXVI del Libro I; come pure che l’altezza massima dell’acqua, nei mari profondi e liberi, debba seguire l’arrivo dei luminari al meridiano del luogo dopo un intervallo minore di sei ore, come avviene in tutto il tratto orientale del mare Atlantico ed Etiopico fra la Francia e il capo di Buona Speranza, e così pure sulle coste del Pacifico del Cile e del Perù: su tutte queste coste la marea cade circa alla seconda, terza o quarta ora, salvo dove il moto, propagato dall’oceano profondo attraverso luoghi di basso fondale, è ritardato fino alla quinta, sesta o settima ora, o anche oltre. Le ore le conto dall’arrivo di ciascuno dei due luminari al meridiano del luogo, tanto sotto l’orizzonte quanto sopra; e per ore del giorno lunare intendo le ventiquattresime parti del tempo in cui la Luna, con il suo moto apparente diurno, ritorna al meridiano del luogo. La forza del Sole o della Luna nel sollevare il mare è massima proprio all’arrivo del luminare al meridiano del luogo. Ma la forza impressa nel mare in quel momento vi rimane per qualche tempo ed è accresciuta dalla forza nuova impressa via via, finché il mare sia salito alla sua altezza massima; il che avverrà nello spazio di una o due ore, ma più spesso, presso le coste, nello spazio di circa tre ore, o anche di più se il mare è poco profondo.

**[III.G5.10]** I due moti, poi, che i due luminari eccitano, non si distingueranno separatamente, ma produrranno un certo moto misto. Nella congiunzione o nell’opposizione dei luminari i loro effetti si congiungeranno, e si comporrà il flusso e riflusso massimo. Nelle quadrature il Sole solleverà l’acqua dove la Luna la abbassa, e la abbasserà dove [la Luna] la solleva; e dalla differenza degli effetti nascerà la marea minima di tutte. E poiché, come attesta l’esperienza, l’effetto della Luna è maggiore di quello del Sole, l’altezza massima dell’acqua cadrà circa alla terza ora lunare. Fuori delle sizigie e delle quadrature, la marea massima, che per la sola forza lunare dovrebbe cadere sempre alla terza ora lunare e per la sola forza solare alla terza solare, per la composizione delle forze cadrà in un tempo intermedio, più vicino alla terza ora lunare; e perciò, nel passaggio della Luna dalle sizigie alle quadrature, quando la terza ora solare precede la terza lunare, anche l’altezza massima dell’acqua precederà la terza ora lunare, e con l’intervallo massimo poco dopo gli ottanti della Luna; e a intervalli uguali la marea massima seguirà la terza ora lunare nel passaggio della Luna dalle quadrature alle sizigie. Così stanno le cose in mare aperto. Nelle foci dei fiumi, infatti, i flussi maggiori, a parità delle altre condizioni, giungeranno più tardi al loro colmo.

**[III.G5.11]** Gli effetti dei luminari dipendono poi dalle loro distanze dalla Terra. A distanze minori, infatti, i loro effetti sono maggiori, a distanze maggiori minori, e ciò in rapporto triplicato dei diametri apparenti. Perciò il Sole, nel tempo invernale, trovandosi nel perigeo, produce effetti maggiori, e fa sì che le maree nelle sizigie siano un po’ maggiori, e nelle quadrature un po’ minori (a parità delle altre condizioni), che nel tempo estivo; e la Luna nel perigeo, ogni mese, solleva maree maggiori che quindici giorni prima o dopo, quando si trova nell’apogeo. Di qui avviene che le due maree assolutamente massime non si seguano l’una all’altra in sizigie consecutive.

**[III.G5.12]** L’effetto di ciascun luminare dipende anche dalla sua declinazione, ossia dalla sua distanza dall’equatore. Se infatti il luminare fosse posto al polo, attrarrebbe le singole parti dell’acqua senza interruzione, senza aumento né diminuzione dell’azione, e perciò non ecciterebbe alcuna reciprocazione del moto. Perciò i luminari, allontanandosi dall’equatore verso il polo, perderanno gradualmente i loro effetti, e per questo ecciteranno maree minori nelle sizigie solstiziali che in quelle equinoziali. Nelle quadrature solstiziali, invece, ecciteranno maree maggiori che nelle quadrature equinoziali, perché l’effetto della Luna, che allora si trova nell’equatore, supera al massimo l’effetto del Sole. Le maree massime cadono dunque nelle sizigie, e le minime nelle quadrature dei luminari, intorno al tempo di ciascuno dei due equinozi. E alla marea massima nelle sizigie si accompagna sempre la minima nelle quadrature, come si è trovato per esperienza. Per la minore distanza del Sole dalla Terra nel tempo invernale che nel tempo estivo, avviene poi che le maree massime e minime più spesso precedano l’equinozio di primavera che lo seguano, e più spesso seguano quello d’autunno che lo precedano.

**[III.G5.13]** Gli effetti dei luminari dipendono anche dalla latitudine dei luoghi. Rappresenti ApEP la Terra coperta da ogni parte di acque profonde; C il suo centro; P, p i poli; AE l’equatore; F un luogo qualsiasi fuori dell’equatore; Ff il parallelo del luogo; Dd il parallelo corrispondente dall’altra parte dell’equatore; L il luogo che la Luna occupava tre ore prima; H il luogo della Terra che le sta perpendicolarmente sotto; h il luogo opposto a questo; K, k i luoghi distanti di lì 90 gradi; CH, Ch le altezze massime del mare misurate dal centro della Terra; e CK, Ck le altezze minime: se con gli assi Hh, Kk si descrive un’ellisse, e poi con la rivoluzione di questa ellisse attorno all’asse maggiore Hh si descrive lo sferoide HPKhpk, questo rappresenterà con ottima approssimazione la figura del mare, e CF, Cf, CD, Cd saranno le altezze del mare nei luoghi F, f, D, d. Inoltre, se nella suddetta rivoluzione dell’ellisse un punto qualsiasi N descrive il cerchio NM, che taglia i paralleli Ff, Dd in luoghi qualsiasi R, T, e l’equatore AE in S, CN sarà l’altezza del mare in tutti i luoghi R, S, T situati su questo cerchio.

**[III.G5.14]** Di qui, nella rivoluzione diurna di un luogo qualsiasi F, l’afflusso sarà massimo in F, alla terza ora dopo l’arrivo della Luna al meridiano sopra l’orizzonte; poi il deflusso massimo in Q, alla terza ora dopo il tramonto della Luna; quindi l’afflusso massimo in f, alla terza ora dopo l’arrivo della Luna al meridiano sotto l’orizzonte; infine il deflusso massimo in Q, alla terza ora dopo il sorgere della Luna; e l’afflusso successivo in f sarà minore dell’afflusso precedente in F. Tutto il mare, infatti, si divide in due soli flutti emisferici, uno nell’emisfero KHk, rivolto verso borea, l’altro nell’emisfero opposto Khk; li si può dunque chiamare flutto boreale e flutto australe. Questi flutti, sempre opposti l’uno all’altro, giungono a turno ai meridiani dei singoli luoghi, a un intervallo di dodici ore lunari. E poiché le regioni boreali partecipano di più del flutto boreale, e le australi dell’australe, ne nascono maree alternativamente maggiori e minori in tutti i luoghi fuori dell’equatore nei quali i luminari sorgono e tramontano. La marea maggiore, quando la Luna declina verso lo zenit del luogo, cadrà circa alla terza ora dopo l’arrivo della Luna al meridiano sopra l’orizzonte, e quando la Luna cambia declinazione si volgerà in minore. E la differenza massima dei flussi cadrà nei tempi dei solstizi, soprattutto se il nodo ascendente della Luna si trova al principio dell’Ariete. Così si è trovato per esperienza che le maree del mattino nel tempo invernale superano quelle della sera, e quelle della sera nel tempo estivo quelle del mattino: a Plymouth di un’altezza di quasi un piede, a Bristol di un’altezza di quindici pollici, secondo le osservazioni di Colepress e di Sturmy.

**[III.G5.15]** I moti descritti fin qui sono però alquanto mutati da quella forza di reciprocazione delle acque per la quale la marea, anche cessando le azioni dei luminari, potrebbe perseverare per qualche tempo. Questa conservazione del moto impresso diminuisce la differenza fra le maree alterne, rende maggiori le maree immediatamente successive alle sizigie e diminuisce quelle immediatamente successive alle quadrature. Di qui avviene che le maree alterne a Plymouth e a Bristol non differiscano fra loro molto più che di un’altezza di un piede o di quindici pollici, e che le maree massime di tutte, negli stessi porti, non siano le prime dopo le sizigie, ma le terze. Tutti i moti, inoltre, sono ritardati nel passaggio per i bassi fondali, tanto che le maree massime di tutte, in certi stretti e foci di fiumi, sono le quarte o anche le quinte dopo le sizigie.

**[III.G5.16]** Può accadere, inoltre, che la marea si propaghi dall’oceano per stretti diversi verso lo stesso porto, e passi più rapidamente per alcuni stretti che per altri: in questo caso la stessa marea, divisa in due o più maree che giungono l’una dopo l’altra, può comporre moti nuovi di generi diversi. Supponiamo che due maree uguali giungano da luoghi diversi nello stesso porto, che la prima preceda l’altra di sei ore e che cada alla terza ora dall’arrivo della Luna al meridiano del porto. Se la Luna, in questo suo arrivo al meridiano, si trovava nell’equatore, ogni sei ore giungeranno afflussi uguali, che, cadendo sui deflussi reciproci, li pareggeranno, e così per tutto quel giorno faranno sì che l’acqua stagni tranquilla. Se invece la Luna allora declinava dall’equatore, nell’oceano si avranno maree alternativamente maggiori e minori, come si è detto; e di lì si propagheranno verso questo porto, alternativamente, due afflussi maggiori e due minori. I due afflussi maggiori comporranno l’acqua più alta a metà fra l’uno e l’altro; un afflusso maggiore e uno minore faranno sì che l’acqua salga a un’altezza media a metà fra loro; e fra i due afflussi minori l’acqua salirà all’altezza minima. Così nello spazio di ventiquattro ore l’acqua giungerà all’altezza massima non due volte, come suole avvenire, ma una volta sola, e una volta sola alla minima; e l’altezza massima, se la Luna declina verso il polo che sta sopra l’orizzonte del luogo, cadrà alla sesta o alla trentesima ora dall’arrivo della Luna al meridiano, e quando la Luna cambia declinazione si muterà in deflusso. Di tutto ciò Halley ha reso noto un esempio, dalle osservazioni dei marinai, nel porto di Batsham, nel regno del Tonchino, alla latitudine boreale di 20° 50′. Lì, il giorno che segue il passaggio della Luna per l’equatore, l’acqua stagna; poi, quando la Luna declina verso borea, comincia a fluire e a rifluire, non due volte, come negli altri porti, ma una sola volta al giorno; e la marea cade al tramonto della Luna, il deflusso massimo al suo sorgere. Con la declinazione della Luna questa marea cresce fino al settimo o all’ottavo giorno, poi per altri sette giorni decresce per gli stessi gradi per cui prima era cresciuta; e quando la Luna cambia declinazione cessa, e presto si muta in deflusso. Da allora, infatti, il deflusso cade al tramonto della Luna e l’afflusso al suo sorgere, finché la Luna non cambia di nuovo declinazione. A questo porto e agli stretti vicini si apre un duplice accesso, uno dal mar Cinese fra il continente e l’isola di Luzon, l’altro dal mare Indiano fra il continente e l’isola di Borneo. Se le maree che giungono per quegli stretti in dodici ore dal mare Indiano e in sei ore dal mar Cinese, e che così cadono alla terza e alla nona ora lunare, compongano moti di questo genere, o se la condizione di quei mari sia un’altra, lascio che si determini con le osservazioni delle coste vicine.

**[III.G5.17]** Fin qui ho reso ragione delle cause dei moti della Luna e dei mari. Conviene ora aggiungere qualcosa sulla quantità dei moti.

### Proposizione XXV. Problema VI (le forze del Sole che perturbano i moti della Luna)

**[III.G5.18]** **Trovare le forze del Sole che perturbano i moti della Luna.**

**[III.G5.19]** Rappresenti S il Sole, T la Terra, P la Luna, CADB l’orbita della Luna. Su SP si prenda SK uguale a ST; SL stia a SK in rapporto duplicato di SK a SP; e si conduca LM parallela a PT: se la gravità acceleratrice della Terra verso il Sole è rappresentata dalla distanza ST o SK, SL sarà la gravità acceleratrice della Luna verso il Sole. Essa si compone delle parti SM, LM, delle quali LM e la parte TM di SM perturbano il moto della Luna, come si è esposto nella Prop. LXVI del Libro I e nei suoi corollari. In quanto la Terra e la Luna ruotano attorno al centro comune di gravità, anche il moto della Terra attorno a quel centro sarà perturbato da forze del tutto simili; ma si possono riferire alla Luna le somme sia delle forze sia dei moti, e rappresentare le somme delle forze con le linee TM e ML, che sono loro analoghe. La forza ML, nella sua quantità media, sta alla forza centripeta con cui la Luna potrebbe ruotare nella sua orbita attorno alla Terra in quiete, alla distanza PT, in rapporto duplicato dei tempi periodici della Luna attorno alla Terra e della Terra attorno al Sole (per il Cor. 17 della Prop. LXVI del Libro I), cioè in rapporto duplicato di 27 giorni 7 ore 43 minuti a 365 giorni 6 ore 9 minuti, ossia come 1000 a 178725, o come 1 a 178 29/40. Abbiamo poi trovato nella Prop. IV che, se la Terra e la Luna ruotano attorno al centro comune di gravità, la loro distanza media l’una dall’altra sarà di 60 ½ semidiametri medi della Terra, con ottima approssimazione. E la forza con cui la Luna potrebbe ruotare in un’orbita attorno alla Terra in quiete, alla distanza PT di 60 ½ semidiametri terrestri, sta alla forza con cui potrebbe ruotare nello stesso tempo alla distanza di 60 semidiametri come 60 ½ sta a 60; e questa forza sta alla forza di gravità presso di noi come 1 a 60 × 60, con ottima approssimazione. Perciò la forza media ML sta alla forza di gravità sulla superficie della Terra come 1 × 60 ½ sta a 60 × 60 × 60 × 178 29/40, ossia come 1 a 638092,6. Da ciò, e dalla proporzione delle linee TM, ML, è data anche la forza TM: e queste sono le forze del Sole da cui sono perturbati i moti della Luna. C.V.T.

### Proposizione XXVI. Problema VII (l’incremento orario dell’area)

**[III.G5.20]** **Trovare l’incremento orario dell’area che la Luna, con un raggio condotto alla Terra, descrive in un’orbita circolare.**

**[III.G5.21]** Abbiamo detto che l’area che la Luna descrive con un raggio condotto alla Terra è proporzionale al tempo, se non in quanto il moto lunare è turbato dall’azione del Sole. Ci proponiamo di indagare qui la disuguaglianza del momento, ossia dell’incremento orario. Per rendere più facile il calcolo, supponiamo che l’orbita della Luna sia circolare, e trascuriamo tutte le disuguaglianze, eccetto soltanto quella di cui qui si tratta. Per l’enorme distanza del Sole, poniamo anche che le linee SP, ST siano parallele fra loro. In questo modo la forza LM si ridurrà sempre alla sua quantità media TP, come pure la forza TM alla sua quantità media 3PK. Queste forze (per il Cor. II delle leggi) compongono la forza TL; e questa forza, se sul raggio TP si abbassa la perpendicolare LE, si scompone nelle forze TE, EL; di queste, TE, agendo sempre lungo il raggio TP, non accelera né ritarda la descrizione dell’area TPC fatta da quel raggio TP; ed EL, agendo lungo la perpendicolare, la accelera o la ritarda quanto accelera o ritarda la Luna. Quell’accelerazione della Luna, fatta nei singoli momenti di tempo nel suo passaggio dalla quadratura C alla congiunzione A, è come la stessa forza che accelera, EL, cioè come 3PK × TK/TP. Si rappresenti il tempo con il moto medio lunare, oppure (il che torna quasi allo stesso) con l’angolo CTP, o anche con l’arco CP. Su CT si innalzi la normale CG, uguale a CT. E, diviso l’arco quadrantale AC in innumerevoli particelle uguali Pp ecc., con le quali si possono rappresentare altrettante particelle uguali di tempo, e condotta pk perpendicolare a CT, si congiunga TG, che incontri KP, kp prolungate in F e f: FK sarà uguale a TK, e Kk starà a PK come Pp sta a Tp, cioè in un rapporto dato; e perciò FK × Kk, ossia l’area FKkf, sarà come 3PK × TK/TP, cioè come EL; e, componendo, l’area totale GCKF sarà come la somma di tutte le forze EL impresse sulla Luna nel tempo totale CP, e quindi anche come la velocità generata da questa somma, cioè come l’accelerazione della descrizione dell’area CTP, ossia come l’incremento del momento.

**[III.G5.22]** La forza con cui la Luna potrebbe ruotare attorno alla Terra in quiete alla distanza TP, nel suo tempo periodico CADB di 27 giorni 7 ore 43 minuti, farebbe sì che un corpo, cadendo nel tempo CT, descrivesse la lunghezza ½ CT e acquistasse nello stesso tempo una velocità uguale alla velocità con cui la Luna si muove nella sua orbita. Ciò risulta dal Cor. 9 della Prop. IV del Libro I. Poiché poi la perpendicolare Kd abbassata su TP è la terza parte di EL, e negli ottanti è la metà di TP, ossia di ML, la forza EL negli ottanti, dove è massima, supererà la forza ML nel rapporto di 3 a 2; e perciò starà alla forza con cui la Luna, nel suo tempo periodico, potrebbe ruotare attorno alla Terra in quiete come 100 sta a 2/3 × 17872 ½, ossia a 11915; e nel tempo CT dovrebbe generare una velocità che sarebbe i 100/11915 della velocità lunare, mentre nel tempo CPA genererebbe una velocità maggiore nel rapporto di CA a CT, ossia a TP. Si rappresenti la forza massima EL negli ottanti con l’area FK × Kk, uguale al rettangolo ½ TP × Pp. E la velocità che la forza massima potrebbe generare in un tempo qualsiasi CP starà alla velocità che tutte le forze minori EL generano nello stesso tempo come il rettangolo ½ TP × CP sta all’area KCGF; nel tempo totale CPA, invece, le velocità generate staranno fra loro come il rettangolo ½ TP × CA e il triangolo TCG, ossia come l’arco quadrantale CA sta al raggio TP. Perciò (per la Prop. IX del Libro V degli *Elementi*) quest’ultima velocità, generata nel tempo totale, sarà i 100/11915 della velocità della Luna. A questa velocità della Luna, che è analoga al momento medio dell’area, si aggiunga e si tolga la metà dell’altra velocità: se il momento medio si rappresenta con il numero 11915, la somma 11915 + 50, ossia 11965, darà il momento massimo dell’area nella sizigia A, e la differenza 11915 − 50, ossia 11865, il suo momento minimo nelle quadrature. Le aree descritte in tempi uguali nelle sizigie e nelle quadrature stanno dunque fra loro come 11965 a 11865. Al momento minimo 11865 si aggiunga un momento che stia alla differenza dei momenti, 100, come il trapezio FKCG sta al triangolo TCG (oppure, il che è lo stesso, come il quadrato del seno PK sta al quadrato del raggio TP, cioè come Pd sta a TP): la somma darà il momento dell’area quando la Luna si trova in un luogo intermedio qualsiasi P.

**[III.G5.23]** Tutto ciò vale nell’ipotesi che il Sole e la Terra siano in quiete e che la Luna compia la sua rivoluzione nel tempo sinodico di 27 giorni 7 ore 43 minuti. Poiché però il periodo sinodico lunare è in realtà di 29 giorni 12 ore e 44 minuti, gli incrementi dei momenti devono essere aumentati nel rapporto del tempo, cioè nel rapporto di 1080853 a 1000000. In questo modo l’incremento totale, che era i 100/11915 del momento medio, diventerà ora i 100/11023 dello stesso. Perciò il momento dell’area nella quadratura della Luna starà al suo momento nella sizigia come 11023 − 50 sta a 11023 + 50, ossia come 10973 a 11073, e al suo momento quando la Luna si trova in un altro luogo intermedio qualsiasi P come 10973 sta a 10973 + Pd, posto naturalmente TP uguale a 100.

**[III.G5.24]** L’area, dunque, che la Luna descrive con un raggio condotto alla Terra in singole particelle di tempo uguali è, con ottima approssimazione, come la somma del numero 219,46 e del seno verso del doppio della distanza della Luna dalla quadratura più vicina, in un cerchio il cui raggio è l’unità. Così stanno le cose quando la variazione negli ottanti è di grandezza media. Se invece lì la variazione è maggiore o minore, quel seno verso deve essere aumentato o diminuito nello stesso rapporto.

### Proposizione XXVII. Problema VIII (la distanza della Luna dal suo moto orario)

**[III.G5.25]** **Trovare dal moto orario della Luna la sua distanza dalla Terra.**

**[III.G5.26]** L’area che la Luna descrive in singoli momenti di tempo con un raggio condotto alla Terra è come il moto orario della Luna e il quadrato della distanza della Luna dalla Terra considerati congiuntamente; e perciò la distanza della Luna dalla Terra sta nel rapporto composto dal rapporto subduplicato dell’area, direttamente, e dal rapporto subduplicato del moto orario, inversamente. C.V.T.

**[III.G5.27]** *Cor. 1.* Di qui è dato il diametro apparente della Luna, poiché esso è inversamente come la sua distanza dalla Terra. Gli astronomi provino quanto bene questa regola concordi con i fenomeni.

**[III.G5.28]** *Cor. 2.* Di qui anche l’orbita lunare si può definire dai fenomeni più accuratamente che finora.

### Proposizione XXVIII. Problema IX (i diametri dell’orbita lunare senza eccentricità)

**[III.G5.29]** **Trovare i diametri dell’orbita in cui la Luna, senza eccentricità, dovrebbe muoversi.**

**[III.G5.30]** La curvatura della traiettoria che un mobile descrive, se è attratto lungo la perpendicolare a quella traiettoria, è come l’attrazione direttamente e il quadrato della velocità inversamente. Pongo che le curvature delle linee stiano fra loro nella proporzione ultima dei seni o delle tangenti degli angoli di contatto che appartengono a raggi uguali, quando quei raggi diminuiscono all’infinito. L’attrazione della Luna verso la Terra nelle sizigie è poi l’eccesso della sua gravità verso la Terra sulla forza solare 2PK (vedi la figura di p. 428), cioè sulla quantità di cui la gravità acceleratrice della Luna verso il Sole supera la gravità acceleratrice della Terra verso il Sole, o ne è superata. Nelle quadrature, invece, quell’attrazione è la somma della gravità della Luna verso la Terra e della forza solare KT, con cui la Luna è tratta verso la Terra. E queste attrazioni, se (AT + CT)/2 si chiama N, sono con ottima approssimazione come 178725/AT² − 2000/(CT × N) e 178725/CT² + 1000/(AT × N); ossia come 178725N × CT² − 2000AT² × CT e 178725N × AT² + 1000CT² × AT. Se infatti la gravità acceleratrice della Luna verso la Terra si rappresenta con il numero 178725, la forza media ML, che nelle quadrature è PT o TK e trae la Luna verso la Terra, sarà 1000, e la forza media TM nelle sizigie sarà 3000; e se da questa si sottrae la forza media ML, resterà la forza 2000, con cui la Luna nelle sizigie è allontanata dalla Terra, e che già sopra ho chiamato 2PK. La velocità della Luna nelle sizigie A e B sta poi alla sua velocità nelle quadrature C e D come CT sta ad AT e il momento dell’area che la Luna descrive con un raggio condotto alla Terra nelle sizigie sta al momento della stessa area nelle quadrature, considerati congiuntamente; cioè come 11073CT sta a 10973AT. Si prenda questo rapporto due volte inversamente e il rapporto precedente una volta direttamente: la curvatura dell’orbita lunare nelle sizigie starà alla sua curvatura nelle quadrature come 120406729 × 178725AT² × CT² × N − 120406729 × 2000AT⁴ × CT sta a 122611329 × 178725AT² × CT² × N + 122611329 × 1000CT⁴ × AT, cioè come 2151969AT × CT × N − 24081AT³ sta a 2191371AT × CT × N + 12261CT³.

**[III.G5.31]** Poiché la figura dell’orbita lunare è ignota, assumiamo al suo posto l’ellisse DBCA, nel cui centro T sia collocata la Terra, e il cui asse maggiore DC stia fra le quadrature, il minore AB fra le sizigie. Poiché però il piano di questa ellisse ruota attorno alla Terra con moto angolare, e la traiettoria di cui consideriamo la curvatura deve essere descritta in un piano del tutto privo di ogni moto angolare, si dovrà considerare la figura che la Luna, ruotando in quell’ellisse, descrive in questo piano, cioè la figura Cpa, i cui singoli punti p si trovano prendendo un punto qualsiasi P sull’ellisse, che rappresenti il luogo della Luna, e conducendo Tp uguale a TP, con la condizione che l’angolo PTp sia uguale al moto apparente del Sole compiuto dal tempo della quadratura C; oppure (il che torna quasi allo stesso) che l’angolo CTp stia all’angolo CTP come il tempo della rivoluzione sinodica lunare sta al tempo della rivoluzione periodica, ossia come 29g 12h 44′ a 27g 7h 43′. Si prenda dunque l’angolo CTa nello stesso rapporto all’angolo retto CTA, e la lunghezza Ta sia uguale alla lunghezza TA: a sarà l’apside inferiore e C l’apside superiore di questa orbita Cpa. Facendo i conti, poi, trovo che la differenza fra la curvatura dell’orbita Cpa nel vertice a e la curvatura del cerchio descritto con centro T e raggio TA sta alla differenza fra la curvatura dell’ellisse nel vertice A e la curvatura dello stesso cerchio in rapporto duplicato dell’angolo CTP all’angolo CTp; che la curvatura dell’ellisse in A sta alla curvatura di quel cerchio in rapporto duplicato di TA a TC; che la curvatura di quel cerchio sta alla curvatura del cerchio descritto con centro T e raggio TC come TC sta a TA; che la curvatura di quest’ultimo sta alla curvatura dell’ellisse in C in rapporto duplicato di TA a TC; e che la differenza fra la curvatura dell’ellisse nel vertice C e la curvatura dell’ultimo cerchio sta alla differenza fra la curvatura della figura [Cpa] nel vertice C e la curvatura dello stesso cerchio in rapporto duplicato dell’angolo CTp all’angolo CTP. Questi rapporti si ricavano facilmente dai seni degli angoli di contatto e delle differenze degli angoli. Confrontati poi questi rapporti fra loro, risulta che la curvatura della figura Cpa in a sta alla sua curvatura in C come AT³ + 16824/100000 CT² × AT sta a CT³ + 16824/100000 AT² × CT. Qui il numero 16824/100000 indica la differenza dei quadrati degli angoli CTP e CTp divisa per il quadrato dell’angolo minore CTP, ossia (il che è lo stesso) la differenza dei quadrati dei tempi 27g 7h 43′ e 29g 12h 44′ divisa per il quadrato del tempo 27g 7h 43′.

**[III.G5.32]** Poiché dunque a indica la sizigia della Luna e C la sua quadratura, la proporzione ora trovata deve essere la stessa della proporzione, trovata sopra, fra la curvatura dell’orbita della Luna nelle sizigie e la sua curvatura nelle quadrature. Perciò, per trovare la proporzione di CT ad AT, moltiplico fra loro gli estremi e i medi. E i termini che ne risultano, divisi per AT × CT, diventano 2062,79CT⁴ − 2151969N × CT³ + 368676N × AT × CT² + 36342AT² × CT² − 362047N × AT² × CT + 2191371N × AT³ + 4051,4AT⁴ = 0. Qui, al posto della semisomma N dei termini AT e CT scrivo 1, e ponendo x per la loro semidifferenza si ha CT = 1 + x e AT = 1 − x; sostituiti questi valori nell’equazione e risolta l’equazione che ne risulta, si ottiene x uguale a 0,00719; e di qui il semidiametro CT diventa 1,00719 e il semidiametro AT 0,99281, numeri che stanno con ottima approssimazione come 70 1/24 e 69 1/24. La distanza della Luna dalla Terra nelle sizigie sta dunque alla sua distanza nelle quadrature (messa da parte, s’intende, la considerazione dell’eccentricità) come 69 1/24 sta a 70 1/24, o, in numeri tondi, come 69 a 70.

### Proposizione XXIX. Problema X (la variazione della Luna)

**[III.G5.33]** **Trovare la variazione della Luna.**

**[III.G5.34]** Questa disuguaglianza nasce in parte dalla forma ellittica dell’orbita lunare, in parte dalla disuguaglianza dei momenti dell’area che la Luna descrive con un raggio condotto alla Terra. Se la Luna P si muovesse nell’ellisse DBCA attorno alla Terra in quiete nel centro dell’ellisse, e con il raggio TP condotto alla Terra descrivesse l’area CTP proporzionale al tempo, e il semidiametro massimo CT dell’ellisse stesse al semidiametro minimo TA come 70 a 69, la tangente dell’angolo CTP starebbe alla tangente dell’angolo del moto medio, contato dalla quadratura C, come il semidiametro TA dell’ellisse sta al suo semidiametro TC, ossia come 69 a 70. La descrizione dell’area CTP, però, nel progresso della Luna dalla quadratura alla sizigia, deve essere accelerata in modo che il suo momento nella sizigia della Luna stia al suo momento nella quadratura come 11073 a 10973, e che l’eccesso del momento in un luogo intermedio qualsiasi P sul momento nella quadratura sia come il quadrato del seno dell’angolo CTP. Ciò avverrà con sufficiente precisione se la tangente dell’angolo CTP si diminuisce nel rapporto subduplicato del numero 10973 al numero 11073, cioè nel rapporto del numero 68,6877 al numero 69. In questo modo la tangente dell’angolo CTP starà ora alla tangente del moto medio come 68,6877 a 70, e l’angolo CTP negli ottanti, dove il moto medio è di 45°, risulterà di 44° 27′ 28″, che, sottratto dall’angolo del moto medio di 45°, lascia la variazione massima di 32′ 32″. Così sarebbero le cose se la Luna, procedendo dalla quadratura alla sizigia, descrivesse un angolo CTA di soli novanta gradi. Ma per il moto della Terra, per cui il Sole è trasportato con moto apparente in conseguenza, la Luna, prima di raggiungere il Sole, descrive un angolo CTa maggiore dell’angolo retto nel rapporto del tempo della rivoluzione sinodica lunare al tempo della rivoluzione periodica, cioè nel rapporto di 29g 12h 44′ a 27g 7h 43′. E in questo modo tutti gli angoli attorno al centro T si dilatano nello stesso rapporto, e la variazione, che altrimenti sarebbe di 32′ 32″, ora, aumentata nello stesso rapporto, diventa di 35′ 10″.

**[III.G5.35]** Questa è la sua grandezza alla distanza media del Sole dalla Terra, trascurate le differenze che possono nascere dalla curvatura dell’orbe magno e dalla maggiore azione del Sole sulla Luna falcata e nuova che sulla Luna gibbosa e piena. Ad altre distanze del Sole dalla Terra, la variazione massima sta nel rapporto composto dal rapporto duplicato del tempo della rivoluzione sinodica lunare (dato il tempo dell’anno), direttamente, e dal rapporto triplicato della distanza del Sole dalla Terra, inversamente. Perciò nell’apogeo del Sole la variazione massima è di 33′ 14″, e nel suo perigeo di 37′ 11″, purché l’eccentricità del Sole stia al semidiametro trasverso dell’orbe magno come 16 15/16 a 1000.

**[III.G5.36]** Fin qui abbiamo indagato la variazione in un’orbita non eccentrica, nella quale cioè la Luna nei suoi ottanti è sempre alla sua distanza media dalla Terra. Se la Luna, per la sua eccentricità, dista dalla Terra più o meno che se fosse posta in questa orbita, la variazione può essere un po’ maggiore o un po’ minore di quanto comporti la regola qui data: ma lascio agli astronomi di determinarne l’eccesso o il difetto dai fenomeni.


**Fine della Prop. XXIX. Nel testo originale segue la Prop. XXX (*Invenire motum horarium nodorum lunæ in orbe circulari*), tradotta nel Fascicolo 24b.**

---

## Apparato

### A.0 Estensioni del glossario

I termini seguenti non comparivano nei glossari comuni né fra quelli fissati dal coordinatore. Ognuno è reso in modo costante in tutto il fascicolo.

| Latino | Italiano | Motivazione |
|---|---|---|
| *puncta æquinoctialia regredi* | «i punti equinoziali retrocedono» | Prop. XXI. Il glossario fissa *præcessio æquinoctiorum* «precessione degli equinozi», che uso nel titolo tematico; nel testo Newton non usa il sostantivo. |
| *nutare*, *motus nutandi* | «con un moto di nutazione», «moto di nutazione» | Prop. XXI. Il gerundio *nutando* è reso con il sostantivo tecnico; Motte «by a nutation». |
| *planetæ majores / minores* (Prop. XXII) | «pianeti maggiori / minori» | I «pianeti minori che ruotano attorno ai maggiori» sono i satelliti (pianeti secondari, nel glossario del Libro III); si conserva la parola di Newton, con nota N2. |
| *lunæ* (dei pianeti), *satellites* | «lune», «satelliti» | Prop. XXIII, *lunarum seu satellitum jovis*: si conserva la doppia denominazione. |
| *extimus* | «più esterno» | *satelles extimus*: il quarto satellite di Giove (Callisto, non verificato sulle fonti allegate per il nome). |
| *aux, augis* | «auge» | Prop. XXIII. Come nel Fascicolo 10 (Prop. LXVI, Cor. 7): l’apside superiore. Motte «apsis». |
| *æquationes priores / posteriores* | «le prime / le seconde equazioni» | Prop. XXIII: sono, rispettivamente, quelle dei satelliti e quelle della Luna, nominate in quest’ordine. |
| *tertium* (‴) | «terzo» | Prop. XXIII, 5″ 12‴: sessantesimo di secondo d’arco. Lasciato come simbolo. |
| *prostaphæresis* | «prostaferesi» | Prop. XXII. Termine tecnico dell’astronomia antica, conservato: è la correzione da aggiungere o togliere al moto medio, qui l’equazione del centro. Motte lo rende «equation of the moon’s centre» (nota N2). |
| *luminaria*, *luminare* | «i luminari», «il luminare» | Prop. XXIV: il Sole e la Luna. Calco tradizionale dell’astronomia italiana. |
| *appulsus luminaris ad meridianum* | «arrivo del luminare al meridiano» | Prop. XXIV. È il passaggio al meridiano (culminazione), superiore o inferiore: Newton conta le ore *tam infra horizontem quam supra*. Motte «appulse». |
| *dies lunaris / solaris*; *hora lunaris / solaris* | «giorno lunare / solare»; «ora lunare / solare» | Definiti nel testo stesso (III.G5.09): l’ora lunare è la ventiquattresima parte dell’intervallo fra due passaggi della Luna al meridiano. |
| *intumescere*; *defluere* | «gonfiarsi»; «ritirarsi» | Prop. XXIV, prima frase. |
| *æstus* | «marea» | Glossario (*æstus maris* «maree»). *Æstus maximus* «marea massima». |
| *affluxus / defluxus* | «afflusso / deflusso» | Prop. XXIV. Distinti da *fluxus / refluxus* «flusso / riflusso» (glossario), che Newton usa nell’enunciato e in senso generale; *affluxus* e *defluxus* indicano il singolo colmo e il singolo cavo in un luogo. Motte li rende entrambi con «flood» ed «ebb». |
| *fluere & refluere* | «fluire e rifluire» | Prop. XXIV (Batsham). |
| *fluctus* | «flutto» | Prop. XXIV: *fluctus hemisphæricus*, *fluctus borealis / australis*. Si evita «onda», che il glossario del Libro II riserva a *unda*. Motte «flood». |
| *reciprocatio*; *vis reciprocationis aquarum* | «reciprocazione»; «forza di reciprocazione delle acque» | Prop. XXIV: il moto alterno di salita e discesa, e la tendenza dell’acqua a continuarlo. Si conserva il calco; Motte «reciprocation». |
| *intensio & remissio* | «aumento e diminuzione» | Glossario (*intendi & remitti* «aumentare e diminuire»), applicato ai sostantivi. |
| *vada*; *loca vadosa*; *mare vadosum* | «bassi fondali»; «luoghi di basso fondale»; «mare poco profondo» | Prop. XXIV. Motte «shallow channels», «shallow». |
| *freta*; *ostia fluviorum*; *portus* | «stretti»; «foci dei fiumi»; «porto» | Prop. XXIV. |
| *ἀκμή* | «colmo» | Prop. XXIV: *ad ἀκμὴν venient*. Parola greca nel latino di Newton (il culmine); Motte «to their height». Nota N4. |
| *vertex loci* | «zenit del luogo» | Prop. XXIV: *luna in verticem loci declinante*. Applicazione del glossario (*zenith* «zenit»). |
| *mare Æthiopicum* | «mare Etiopico» | Prop. XXIV: nome dell’epoca dell’Atlantico meridionale (non verificato sulle fonti allegate); Motte «Æthiopic». |
| *Gallia*; *promontorium Bonæ Spei*; *littus Chilense & Peruvianum* | «Francia»; «capo di Buona Speranza»; «coste del Cile e del Perù» | Forme moderne. |
| *Plymuthum*; *Bristolia*; *Colepressius*; *Sturmius*; *Halleius* | Plymouth; Bristol; Colepress; Sturmy; Halley | Forme moderne, come Motte. |
| *regnum Tunquini*; *Batsham*; *oceanus Sinensis*; *mare Indicum*; *insula Luconia*; *Borneo* | «regno del Tonchino»; Batsham; «mar Cinese»; «mare Indiano»; «isola di Luzon»; Borneo | Forme moderne; *Batsham* non ha un equivalente sicuro nelle fonti allegate e resta com’è. Motte «Leuconia». |
| *digitus* (misura d’altezza della marea) | «pollice» | Il glossario del Libro III fissa «dito» soltanto per le eclissi; per la lunghezza vale il glossario del Libro II (*digitus* «pollice»). Motte «inches». **Dubbio segnalato**: il Fascicolo 3 (L30) ha «dito» per una lunghezza. |
| *mobile* | «mobile» | Prop. XXVIII: il corpo in moto. Termine tecnico conservato; Motte «a body». |
| *gravitas acceleratrix* | «gravità acceleratrice» | Propp. XXV e XXVIII, sul modello di *vis acceleratrix*. Motte oscilla fra «accelerated» e «accelerative». |
| *vis accelerans* | «la forza che accelera» | Prop. XXVI, *ipsa vis accelerans EL*: participio, non il termine tecnico *acceleratrix*. Motte «the generating accelerative force». |
| *mediocris quantitas* | «quantità media» | Propp. XXV–XXVI (*vis ML in mediocri sua quantitate*). |
| *momentum areæ*; *incrementum horarium* | «momento dell’area»; «incremento orario» | Prop. XXVI: il momento è l’incremento dell’area in una particella di tempo (glossario del Libro II, *momentum* «momento»); Newton lo dice esplicitamente (*momenti, vel incrementi horarii*). |
| *motus horarius* | «moto orario» | Propp. XXII e XXVII: lo spostamento angolare in un’ora. |
| *arcus quadrantalis* | «arco quadrantale» | Prop. XXVI: l’arco di un quarto di cerchio. |
| *trapezium* | «trapezio» | Prop. XXVI. |
| *componendo* (*composite*) | «componendo» | Prop. XXVI: *& composite, area tota GCKF*: sommando gli elementi. Motte «compounding». |
| *curvatura* | «curvatura» | Prop. XXVIII; Newton la definisce nel testo stesso (III.G5.30). |
| *apsis ima / summa* | «apside inferiore / superiore» | Prop. XXVIII, sul modello del Fascicolo 10 (Cor. 7–9 della Prop. LXVI). |
| *ducere extrema & media in se invicem* | «moltiplicare fra loro gli estremi e i medi» | Prop. XXVIII: regola delle proporzioni (glossario: *ducere in* «moltiplicare per»). |
| *semisumma*; *semidifferentia* | «semisomma»; «semidifferenza» | Prop. XXVIII. |
| *tempus / revolutio synodica / periodica* | «tempo sinodico / periodico»; «rivoluzione sinodica / periodica» | Propp. XXVI, XXVIII, XXIX: la rivoluzione rispetto al Sole e quella rispetto alle stelle fisse. Nota N6. |
| *luna falcata / nova / gibbosa / plena* | «Luna falcata / nuova / gibbosa / piena» | Prop. XXIX. Motte «horned and new … gibbous and full». |
| *semidiameter transversa* | «semidiametro trasverso» | Prop. XXIX: il semiasse maggiore dell’orbe magno (glossario: *axis transversus* «asse trasverso»). |

*Impetus*, *impulsus* e *vis insita* non compaiono nel latino del fascicolo (Motte introduce *vis insita* nella Prop. XXIV: § A.14). *Constanter* compare una volta (Prop. XXIV, *traheret … constanter*): «senza interruzione», secondo il glossario.

### A.1 Proposizione XXI

**Latino:** *Puncta æquinoctialia regredi, & axem terræ singulis revolutionibus annuis nutando bis inclinari in eclipticam & bis redire ad positionem priorem.*

**Inglese:** “That the equinoctial points go backward, and that the axis of the earth, by a nutation in every annual revolution, twice vibrates towards the ecliptic, and as often returns to its former position.”

**Scelte.**

- Enunciato all’infinito reso con l’indicativo.
- *bis inclinari in eclipticam* → «si inclina due volte verso l’eclittica»; Motte «twice vibrates towards the ecliptic».
- *vix aut ne vix quidem sensibilis* → «appena sensibile, se pure lo è». Motte «scarcely perceptible» perde *ne vix quidem* (§ A.14).
- Il rimando *per corol. 20. prop. lxvi. lib. i.* → «dal Cor. 20 della Prop. LXVI del Libro I» (§ A.12).

### A.2 Proposizione XXII

**Latino:** *Motus omnes lunares, omnesque motuum inæqualitates ex allatis principiis consequi.*

**Inglese:** “That all the motions of the moon, and all the inequalities of those motions, follow from the principles which we have laid down.”

**Scelte.**

- *aream pro tempore majorem* → «un’area maggiore in rapporto al tempo»; Motte «greater for the time».
- *nisi quatenus impedit motus eccentricitatis* → «se non in quanto lo impedisce il moto dell’eccentricità» (glossario). Motte esplicita il soggetto («these effects are hindered»).
- *luna in perigæo velocior est … in syzygiis quam in quadraturis* → la comparazione finale regge entrambi i membri; la virgola prima di «nelle sizigie» lo rende chiaro.
- **Nodi.** La trascrizione ha *Nodi autem (per corol.* ***2.*** *prop. lxvi.) quiescunt in syzygiis suis*; Motte ha «by Cor. **11**». Il Cor. 2 della Prop. LXVI riguarda la descrizione dell’area, il Cor. 11 il moto dei nodi (Fascicolo 10, S11.41 e S11.50). Traduco «per il Cor. [11]» con la parentesi quadra e lo segnalo fra i punti da controllare sulla stampa (§ A.11). Può essere un refuso della trascrizione (una cifra caduta) o della stampa.
- *eorundem æquationes* → «le loro equazioni»: prima occorrenza di *æquatio* (nota N0).
- *inæqualitas quæ variatio dicitur* → «la disuguaglianza che si chiama variazione»; Motte «which we call the variation» attribuisce il nome a Newton.
- *ad prostaphæresin lunæ referri solet, & cum ea confundi* → «si suole riferire alla prostaferesi della Luna e confondere con essa»; Motte «thrown into and confounded with the equation of the moon’s centre» interpreta (§ A.0, nota N2).
- Motte aggiunge «Book I» a ogni rimando e «(of the moon)» nell’ultima frase del primo capoverso.

### A.3 Proposizione XXIII

**Latino:** *Motus inæquales satellitum jovis & saturni a motibus lunaribus derivare.*

**Inglese:** “To derive the unequal motions of the satellites of Jupiter and Saturn from the motions of our moon.”

**Scelte.**

- Saturno compare solo nell’enunciato; il testo tratta soltanto i satelliti di Giove.
- *ob causam quam hic exponere non vacat* → «per una causa che qui non ho modo di esporre»; Motte «which I cannot here descend to explain».
- *tempore unius revolutionis æquationum priorum / posteriorum* → «nel tempo di una rivoluzione delle prime / delle seconde equazioni» (§ A.0): il periodo in cui l’equazione compie il suo ciclo.
- *temporibus quibus satelles & luna ad solem revolvuntur* → «nei tempi in cui il satellite e la Luna ritornano al Sole», cioè nei periodi sinodici. Motte aggiunge fra parentesi «(after parting from)» e «(again)».
- Motte sposta all’inizio il rimando al Cor. 16, che nel latino chiude la seconda frase.
- La pagina ‹424› cade dentro *æqua‹424›tionum*; nessuna perdita di testo.

### A.4 Proposizione XXIV

**Latino:** *Fluxum & refluxum maris ab actionibus solis ac lunæ oriri.*

**Inglese:** “That the flux and reflux of the sea arise from the actions of the sun and moon.”

**Scelte.**

- Primo capoverso: il *patet* regge due proposizioni infinitive (*mare … intumescere debere* e *aquæ maximam altitudinem … sequi*); l’italiano le coordina con «come pure che».
- *minori quam sex horarum spatio* → «dopo un intervallo minore di sei ore».
- *per vim novam subinde impressam augetur* → «è accresciuta dalla forza nuova impressa via via». Motte amplia con una spiegazione assente nel latino («a new though less force … This makes the sea rise higher and higher, till this new force becoming too weak to raise it any more»).
- La trascrizione ha *si mare sit* ***vodasum***: refuso probabile per *vadosum* (§ A.11).
- Secondo capoverso: la trascrizione ha *deprimetque ubi* ***sol*** *attollit*. Il senso richiede *luna* (il Sole abbassa l’acqua dove la Luna la solleva); Motte «depress the waters which the moon raises». Traduco «dove [la Luna] la solleva» (§ A.11).
- *ad ἀκμὴν venient* → «giungeranno … al loro colmo» (§ A.0). Motte omette *cæteris paribus*.
- Terzo e quarto capoverso: *in triplicata ratione diametrorum apparentium* → «in rapporto triplicato dei diametri apparenti» (Cor. 14 della Prop. LXVI, non citato qui).
- Capoverso della latitudine: *ad boream vergentem* → «rivolto verso borea». *in duos omnino fluctus* → «in due soli flutti». La lettera **Q** (*defluxus maximus in Q*) non è definita nel testo: è un punto della figura, non disponibile.
- *præsertim si lunæ nodus ascendens versatur in principio arietis* → «al principio dell’Ariete»: il latino nomina il segno con la parola, non con il simbolo.
- *observantibus Colepressio & Sturmio* → «secondo le osservazioni di Colepress e di Sturmy».
- Capoverso della reciprocazione: *qua maris æstus, etiam cessantibus luminarium actionibus, posset aliquamdiu perseverare* → «per la quale la marea, anche cessando le azioni dei luminari, potrebbe perseverare per qualche tempo». Motte introduce la *vis insita* («which the waters, being once moved, retain a little while by their *vis insita*»), che il latino non nomina.
- Batsham: *per alios septem dies* → «per altri sette giorni»; Motte «for the 7 or 8 days following». *ac mox mutatur in defluxum* → «e presto si muta in deflusso»; Motte «immediately». Motte aggiunge «crossing over the equator to the south».
- *An æstus … componant …; sitne alia marium illorum conditio, … determinandum relinquo* → interrogativa indiretta doppia resa con «Se … compongano …, o se la condizione … sia un’altra, lascio che si determini».
- *Hactenus causas motuum lunæ & marium reddidi* (III.G5.17) → «Fin qui ho reso ragione delle cause»: è la chiusa della parte qualitativa e apre i calcoli delle Propp. XXV ss.

### A.5 Proposizione XXV

**Latino:** *Invenire vires solis ad perturbandos motus Lunæ.*

**Inglese:** “To find the forces with which the sun disturbs the motions of the moon.”

**Scelte.**

- Enunciato: resa del glossario, «le forze del Sole che perturbano i moti della Luna». La maiuscola di *Lunæ* nella trascrizione non ha conseguenze.
- *gravitas acceleratrix terræ in solem* → «gravità acceleratrice della Terra verso il Sole» (§ A.0); Motte «accelerated force of gravity» (refuso o svista per «accelerative», che usa subito dopo per la Luna).
- *ut in libri primi prop. lxvi. & ejus corollariis expositum est* → «come si è esposto nella Prop. LXVI del Libro I e nei suoi corollari»; Motte «as we have shewn».
- *per lineas ipsis analogas* → «con le linee … che sono loro analoghe».
- *ut 1000 ad 178725, seu 1 ad 178⁤2940* → «come 1000 a 178725, o come 1 a 178 29/40» (SVG 963: 178 29/40).
- *Invenimus autem in propositione quarta* → «Abbiamo poi trovato nella Prop. IV» (del Libro III); Motte «in the 4th Prop. of this Book».
- *ut 1×60⁤12 ad 60×60×60×178⁤2940* → «come 1 × 60 ½ sta a 60 × 60 × 60 × 178 29/40» (SVG 1023, 1024).

### A.6 Proposizione XXVI

**Latino:** *Invenire incrementum horarium areæ quam luna, radio ad terram ducto, in orbe circulari describit.*

**Inglese:** “To find the horary increment of the area which the moon, by a radius drawn to the earth, describes in a circular orbit.”

**Scelte.**

- *Inæqualitatem momenti, vel incrementi horarii* → «la disuguaglianza del momento, ossia dell’incremento orario». Motte aggiunge «of that area or motion so disturbed».
- *Hoc pacto vis LM reducetur semper ad mediocrem suam quantitatem TP* → «la forza LM si ridurrà sempre alla sua quantità media TP».
- *(per legum corol. 2.)* → «(per il Cor. II delle leggi)».
- *ut 3⁢PK×TKTP* → «come 3PK × TK/TP» (SVG 1025).
- *diviso arcu quadrantali AC in particulas innumeras æquales* → «diviso l’arco quadrantale AC in innumerevoli particelle uguali». La trascrizione ha poi *æuales totidem particulæ temporis*: refuso probabile per *æquales*.
- *& composite* → «e, componendo» (§ A.0).
- *longitudinem 12⁢CT* → «la lunghezza ½ CT» (SVG 1026).
- *ut 100 ad 23×17872⁤12 seu 11915* → «come 100 sta a 2/3 × 17872 ½, ossia a 11915» (SVG 1027); *pars 10011915* → «i 100/11915» (SVG 1028).
- *vis omnis minor EL* → «tutte le forze minori EL»: la somma delle forze EL, minori della massima, nel tempo CP.
- *(per prop. ix. lib. v. elem.)* → «(per la Prop. IX del Libro V degli *Elementi*)»: Euclide. **Motte omette il rimando.**
- *velocitas posterior* → «quest’ultima velocità».
- *pars 10011023* → «i 100/11023» (SVG 1032).
- *existente videlicet TP æquali 100* → «posto naturalmente TP uguale a 100».
- *sinus versi duplicatæ distantiæ lunæ a quadratura proxima* → «del seno verso del doppio della distanza della Luna dalla quadratura più vicina».

### A.7 Proposizione XXVII

**Latino:** *Ex motu horario lunæ invenire ipsius distantiam a terra.*

**Inglese:** “From the horary motion of the moon to find its distance from the earth.”

**Scelte.**

- *conjunctim* → «considerati congiuntamente» (glossario).
- *Tentent astronomi quam probe hæc regula cum phænomenis congruat* → «Gli astronomi provino quanto bene questa regola concordi con i fenomeni»: congiuntivo esortativo.
- La Prop. XXVII applica la legge delle aree in forma differenziale: nota N7.

### A.8 Proposizione XXVIII

**Latino:** *Invenire diametros orbis in quo luna, sine eccentricitate, moveri deberet.*

**Inglese:** “To find the diameters of the orbit, in which, without eccentricity, the moon would move.”

**Scelte.**

- *si secundum trajectoriæ illius perpendiculum trahatur* → «se è attratto lungo la perpendicolare a quella traiettoria».
- *in ultima proportione* → «nella proporzione ultima» (glossario: *ratio ultima* «rapporto ultimo»; qui *proportio*). Motte «evanescent proportion».
- *vis solaris 2⁢PK … qua gravitas acceleratrix lunæ in solem superat gravitatem acceleratricem terræ in solem* → «la forza solare 2PK, cioè la quantità di cui la gravità acceleratrice della Luna verso il Sole supera …»: *qua* è ablativo di misura. Integrazione «cioè la quantità» per rendere il costrutto.
- *(vide fig. pag. 428.)* → «(vedi la figura di p. 428)»: la figura della Prop. XXV. Motte «(see Fig. Prop. XXV)».
- *si AT+CT2 dicatur N* → «se (AT + CT)/2 si chiama N» (SVG 1033).
- Le due espressioni delle attrazioni e la loro seconda forma: § A.10.
- *Rationes autem ineundo invenio* → «Facendo i conti, poi, trovo»; Motte «by computation, I find».
- La trascrizione ha *curvaturam figuræ* ***Tpa*** *in vertice C*: refuso probabile per **Cpa** (così due righe sopra e sotto, e così Motte). Traduco «della figura [Cpa]».
- *prodit curvatura figuræ Cpa in a ad ipsius curvaturam in C, ut ATcub.* ***+*** *16824100000⁢CTq×AT ad CTcub.+16824100000⁢ATq×CT* → con il «+» nei due termini. Motte 1846 (SVG 1036) ha «−» nel primo: è un errore (nota N8, § A.13).
- *differentiam quadratorum … applicatam ad quadratum anguli minoris* → «divisa per il quadrato dell’angolo minore» (glossario: *applicare ad* «dividere per»).
- *seposita scilicet eccentricitatis consideratione* → «messa da parte, s’intende, la considerazione dell’eccentricità».
- La pagina ‹435› cade dentro *nume‹435›rus*.

### A.9 Proposizione XXIX

**Latino:** *Invenire variationem lunæ.*

**Inglese:** “To find the variation of the moon.”

**Scelte.**

- *a quadratura C computati* → «contato dalla quadratura C».
- *in progressu lunæ a quadratura ad syzygiam* → «nel progresso della Luna dalla quadratura alla sizigia».
- *Id quod satis accurate fiet* → «Ciò avverrà con sufficiente precisione»; Motte «which we may effect with accuracy enough» lega la frase alla precedente.
- *quo sol in consequentia motu apparente transfertur* → «per cui il Sole è trasportato con moto apparente in conseguenza».
- *priusquam solem assequitur* → «prima di raggiungere il Sole».
- *a curvatura orbis magni* → «dalla curvatura dell’orbe magno» (nota N0).
- *(dato anni tempore)* → «(dato il tempo dell’anno)».
- *ad orbis magni semidiametrum transversam ut 16⁤1516 ad 1000* → «come 16 15/16 a 1000» (SVG 1041).
- Le pagine ‹436› e ‹437› cadono dentro *quadra‹436›tum* ed *ex‹437›cessum*.

### A.10 Letture delle formule appiattite

La trascrizione appiattisce le frazioni e usa i caratteri invisibili U+2062 (prodotto) e U+2064 (somma) fra intero e frazione. Ogni lettura è stata confrontata con la formula corrispondente di Motte (SVG) e, dove possibile, con il calcolo.

| Luogo | Trascrizione | Lettura | Riscontro |
|---|---|---|---|
| III.G5.19 | *178⁤2940* | 178 29/40 | SVG 963; 1000 : 178725 |
| III.G5.19 | *60⁤12* | 60 ½ | SVG 968; Prop. IV |
| III.G5.19 | *1×60⁤12 ad 60×60×60×178⁤2940* | 1 × 60 ½ : 60 × 60 × 60 × 178 29/40 | SVG 1023–1024; dà 1 : 638092,6 |
| III.G5.21–22 | *3⁢PK* ; *3⁢PK×TKTP* | 3PK ; 3PK × TK/TP | SVG 1025; verifica geometrica (N6) |
| III.G5.22 | *12⁢CT* ; *12⁢TP×Pp* ; *12⁢TP×CP* ; *12⁢TP×CA* | ½ CT ; ½ TP × Pp ; ½ TP × CP ; ½ TP × CA | SVG 1026, 1029–1031 |
| III.G5.22 | *23×17872⁤12* | 2/3 × 17872 ½ | SVG 1027; = 11915 |
| III.G5.22–23 | *10011915* ; *10011023* | 100/11915 ; 100/11023 | SVG 1028, 1032 |
| III.G5.30 | *2⁢PK* | 2PK | testo di Motte |
| III.G5.30 | *AT+CT2* | (AT + CT)/2 | SVG 1033 |
| III.G5.30 | *178725ATq-2000CT×N* ; *178725CTq+1000AT×N* | 178725/AT² − 2000/(CT × N) ; 178725/CT² + 1000/(AT × N) | SVG 1034–1035; moltiplicate per AT² × CT² × N danno la seconda forma del testo |
| III.G5.30 | *178725⁢N×CTq-2000⁢ATq×CT* ecc. | 178725N × CT² − 2000AT² × CT ecc. | testo di Motte |
| III.G5.30 | *ATqq*, *CTqq*, *ATcub.* | AT⁴, CT⁴, AT³ | testo di Motte |
| III.G5.31 | *16824100000* | 16824/100000 | SVG 1036–1038; (29g 12h 44′ : 27g 7h 43′)² − 1 = 0,168243 |
| III.G5.32 | *70⁤124* ; *69⁤124* | 70 1/24 ; 69 1/24 | SVG 1039–1040 |
| III.G5.35 | *16⁤1516* | 16 15/16 | SVG 1041 |

### A.11 Refusi e anomalie della trascrizione

| Luogo | Trascrizione | Lettura | Tipo |
|---|---|---|---|
| III.G5.04 | *Nodi autem (per corol. 2. prop. lxvi.)* | *corol. 11.* | rimando errato; Motte «Cor. 11» |
| III.G5.09 | *si mare sit vodasum* | *vadosum* | refuso probabile |
| III.G5.10 | *deprimetque ubi sol attollit* | *ubi luna attollit* | refuso probabile (senso; Motte «the moon») |
| III.G5.14 | *in hæmisphærio opposito* | *hemisphærio* | grafia oscillante (due righe prima *hemisphærio*) |
| III.G5.14 | *post occasum lunae* | *lunæ* | normalizzazione della trascrizione; senza conseguenze |
| III.G5.21 | *æuales totidem particulæ* | *æquales* | refuso probabile |
| III.G5.31 | *curvaturam figuræ Tpa in vertice C* | *Cpa* | refuso probabile (Motte «Cpa») |

La traduzione segue il senso; la Parte B riporta il latino esatto della trascrizione.

**Punti da controllare sulla stampa ECCO.**

| Pagina 1726 | Trascrizione | Lettura attesa | Motivo |
|---|---|---|---|
| p. 422 | *Nodi autem (per corol. 2. prop. lxvi.)* | *corol. 11.* | il Cor. 2 tratta delle aree, l’11 dei nodi; Motte «Cor. 11»; stabilire se l’errore è della trascrizione o della stampa |
| p. 424 | *si mare sit vodasum* | *vadosum* | parola inesistente |
| p. 425 | *deprimetque ubi sol attollit* | *ubi luna attollit* | il Sole non può abbassare l’acqua dove esso stesso la solleva |
| p. 426 | *in hæmisphærio opposito Khk* | *hemisphærio* | grafia |
| p. 430 | *æuales totidem particulæ temporis* | *æquales* | lettera caduta |
| p. 432 | *jam fiet ejusdem pars 10011023* | *11023* o *11024* | 11915 : 1,080853 = 11023,7; non è un refuso di trascrizione, ma conviene vedere la cifra a stampa |
| p. 434 | *curvaturam figuræ Tpa in vertice C* | *Cpa* | lettera iniziale diversa dalle altre occorrenze |
| p. 434 | *ATcub.+16824100000⁢CTq×AT* | segno «+» | Motte 1846 ha «−»; il calcolo conferma «+»; controllare la stampa (ed eventualmente Motte 1729) |

### A.12 Rimandi

**Rimandi ai Libri I e II** (20 citazioni; verificati sui Fascicoli 3, 4, 5 e 10).

| Luogo | Latino | Fascicolo, identificatore | Esito |
|---|---|---|---|
| III.G5.02 | *corol. 20. prop. lxvi. lib. i.* | 10, S11.59 (anello solidale col globo: l’asse oscilla e i nodi retrocedono; vale per un globo con eccesso di materia all’equatore) | regge |
| III.G5.04 | *prop. lxv. lib. i.* | 10, S11.27–S11.31 (più corpi in ellissi approssimate; Caso 2: sistema trascinato da un corpo lontano) | regge |
| III.G5.04 | *corol. 2, 3, 4, & 5. prop. lxvi.* | 10, S11.41–S11.44 (area più veloce, moto più veloce, orbita meno curva, distanza minore nelle sizigie) | regge |
| III.G5.04 | *corol. 9. prop. lxvi.* | 10, S11.48 (eccentricità massima con le apsidi nelle sizigie) | regge |
| III.G5.04 | *corol. 7 & 8 prop. lxvi.* | 10, S11.46–S11.47 (moto dell’auge) | regge |
| III.G5.04 | ***corol. 2.*** *prop. lxvi.* (nodi) | 10, S11.41 tratta dell’area; i nodi sono nel Cor. 11, S11.50 | **non torna**: va letto Cor. 11 (§ A.11) |
| III.G5.04 | *corol. 10. prop. lxvi.* | 10, S11.49 (inclinazione massima con i nodi nelle sizigie: allora la Luna, quando è alla massima latitudine, è nelle quadrature) | regge |
| III.G5.04 | *corol. 6. prop. lxvi.* | 10, S11.45 (il tempo periodico cresce quando cresce l’azione del corpo lontano, qui il Sole al perielio della Terra) | regge |
| III.G5.05 | *corol. 14. prop. lxvi.* | 10, S11.53 (effetti come il cubo del diametro apparente del corpo lontano) | regge |
| III.G5.05 | *corol. 1 & 2. lem. x.* | 4, S1.29–S1.30 (errori come i quadrati dei tempi; come le forze e i quadrati dei tempi) | regge |
| III.G5.05 | *corol. 16. prop. lxvi. Lib. i.* | 10, S11.55 (errori angolari come il quadrato del tempo periodico) | regge |
| III.G5.07 | *corol. 16. prop. lxvi. lib. i.* e tre volte *per idem corollarium* | 10, S11.55 (moti medi di auge e nodi come *T*ₚ² : *T*ₜ² per rivoluzione; auge e nodi in rapporto dato) | regge (nota N3) |
| III.G5.09 | *corol. 19. & 20. prop. lxvi. lib. i.* | 10, S11.58–S11.59 (acqua nel canale; altezza massima circa negli ottanti dopo le sizigie) | regge |
| III.G5.19 | *libri primi prop. lxvi. & ejus corollariis* | 10, S11.37–S11.38 (scomposizione di SL in SM, LM; MN) | regge |
| III.G5.19 | *corol. 17. prop. lxvi. lib. i.* | 10, S11.56 (forza media LM : forza che trattiene P = rapporto duplicato dei tempi periodici) | regge |
| III.G5.21 | *legum corol. 2.* | 3, L10 (composizione e risoluzione delle forze) | regge |
| III.G5.22 | *corol. 9. prop. iv. lib. i.* | 5, S2.32 (arco medio proporzionale fra diametro e caduta): con arco = raggio CT la caduta è ½ CT | regge (verificato) |

**Altri rimandi.**

| Luogo | Latino | Esito |
|---|---|---|
| III.G5.19 | *in propositione quarta* (Libro III) | regge: il latino della Prop. IV (L3-P01-14) dà, per Terra e Luna rotanti attorno al centro comune, «60⁤12 semidiametrorum terrestrium circiter» |
| III.G5.22 | *prop. ix. lib. v. elem.* (Euclide) | non verificabile sulle fonti allegate; l’uso (due grandezze che hanno lo stesso rapporto con una terza sono uguali) è coerente con il contenuto noto della proposizione (non verificato sulle fonti allegate) |
| III.G5.30 | *vide fig. pag. 428.* | regge: la Prop. XXV comincia a p. 428 e la sua [FIG] precede il marcatore ‹429› |
| III.G5.21 | *Diximus aream … esse tempori proportionalem* | rimando generico (la legge delle aree per la Luna; Fenomeno VI e Prop. III del Libro III, fuori fascicolo); non controllato in dettaglio |
| III.G5.30 | *quamque jam ante nominavi 2⁢PK*; *quam supra invenimus* (III.G5.32) | rimandi interni alla stessa proposizione: reggono |

### A.13 SVG di Motte che non tornano con il latino

Ho controllato le 21 formule SVG di questa parte (963, 968 — tre occorrenze —, 1023–1041) sul LaTeX di `svg_tex.tsv`. Ne torna 20; una non torna.

| n | LaTeX | Lettura attesa (latino) |
|---|---|---|
| 1036 | `\mathrm{AT}^{3} - \tfrac{16824}{100000}\mathrm{CT}^{2}\mathrm{AT}` | AT³ **+** 16824/100000 CT² × AT. Il «+» è confermato dalla derivazione (i cinque rapporti di III.G5.31 danno AT(AT² + μCT²) : CT(CT² + μAT²)), dalla simmetria con SVG 1037 e dal fatto che soltanto con il «+» l’equazione finale ha la radice x = 0,00719 (nota N8). |

### A.14 Riepilogo: dove Motte aggiunge, omette o sbaglia

| Luogo | Latino | Motte 1846 | Tipo |
|---|---|---|---|
| III.G5.02 | *vix aut ne vix quidem sensibilis* | «scarcely perceptible» | omissione di *ne vix quidem* |
| III.G5.04 | *nisi quatenus impedit* | «excepting in so far as these effects are hindered» | esplicitazione |
| III.G5.04 | *per corol. 2.* (nodi) | «Cor. 11» | Motte ha la lettura giusta (§ A.11) |
| III.G5.04 | *inæqualitates insigniores* | «principal inequalities (of the moon)» | aggiunta |
| III.G5.05 | *quæ variatio dicitur* | «which we call the variation» | attribuzione del nome |
| III.G5.05 | *ad prostaphæresin lunæ* | «with the equation of the moon’s centre» | interpretazione |
| III.G5.07 | *(per corol. 16. …)* a metà frase | spostato all’inizio | ordine |
| III.G5.07 | *augis* | «apsis» | termine diverso |
| III.G5.07 | *ad solem revolvuntur* | «(after parting from) are revolved (again) to the sun» | aggiunte fra parentesi |
| III.G5.09 | *loca vadosa* | «the shallowness of the channels, through which it passes to some particular places» | parafrasi ampliata |
| III.G5.09 | *ad meridianum loci revertitur* | «… which it left the day before» | aggiunta |
| III.G5.09 | *per vim novam subinde impressam augetur* | «a new though less force … till this new force becoming too weak …» | **spiegazione aggiunta** |
| III.G5.09 | *id quod fiet* | «this will come to pass, perhaps» | aggiunta di «perhaps» |
| III.G5.10 | *ubi sol attollit* (trascrizione) | «which the moon raises» | Motte ha la lettura attesa |
| III.G5.10 | *fluxus majores cæteris paribus tardius ad ἀκμὴν* | «the greater tides come later to their height» | omissione di *cæteris paribus* |
| III.G5.13 | *in locis F, f, D, d* | «in the places Ff, Dd» | lettere raggruppate |
| III.G5.13 | *in locis quibusvis R, T* | «in any places RT» | lettere unite |
| III.G5.15 | *vim illam reciprocationis aquarum, qua … posset aliquamdiu perseverare* | «which the waters, being once moved, retain a little while by their *vis insita*» | **aggiunta della *vis insita*** |
| III.G5.16 | *Halleius* | «Dr. Halley» | titolo aggiunto |
| III.G5.16 | *per alios septem dies* | «for the 7 or 8 days following» | aggiunta di «or 8» |
| III.G5.16 | *& luna declinationem mutante cessat* | «… crossing over the equator to the south» | aggiunta |
| III.G5.16 | *ac mox mutatur* | «immediately changed» | *mox* «presto» reso «subito» |
| III.G5.16 | *insulam Luconiam* | «Leuconia» | grafia |
| III.G5.19 | *gravitas acceleratrix terræ* | «accelerated force of gravity» | termine errato (poi «accelerative») |
| III.G5.19 | *expositum est* | «as we have shewn» | prima persona aggiunta |
| III.G5.21 | *Inæqualitatem momenti, vel incrementi horarii* | «… of that area or motion so disturbed» | aggiunta |
| III.G5.21 | *ipsa vis accelerans EL* | «the generating accelerative force EL» | aggiunta di «generating» |
| III.G5.22 | *(per prop. ix. lib. v. elem.)* | — | **omissione del rimando a Euclide** |
| III.G5.30 | *in ultima proportione* | «evanescent proportion» | termine diverso |
| III.G5.30 | *(vide fig. pag. 428.)* | «(see Fig. Prop. XXV)» | adattamento del rimando |
| III.G5.31 | *ATcub.+16824100000⁢CTq×AT* | SVG 1036: AT³ − 16824/100000 CT²AT | **segno errato** (§ A.13) |
| III.G5.31 | *curvatura circuli … hujus autem curvatura* | «the curvature of this last arch» | «arco» per «cerchio» |
| III.G5.31 | *figuræ Tpa* (trascrizione) | «figure Cpa» | Motte ha la lettura attesa |
| III.G5.34 | *Id quod satis accurate fiet* | «which we may effect with accuracy enough» | frase unita alla precedente |

Le lettere delle figure, i numeri delle tabelle di calcolo (178725, 638092,6, 11915, 11965, 11865, 1080853, 11023, 10973, 11073, 219,46, 120406729, 122611329, 2151969, 24081, 2191371, 12261, 2062,79, 368676, 36342, 362047, 4051,4, 0,00719, 1,00719, 0,99281, 68,6877, 44° 27′ 28″, 32′ 32″, 35′ 10″, 33′ 14″, 37′ 11″) e i tempi coincidono fra latino e Motte.


---

## Note editoriali e fisiche

Queste note sono aggiunte del presente fascicolo, non affermazioni tradotte da Newton. Le verifiche numeriche sono state eseguite con uno script Python (`tmp/24a/verifica.py`), che ricalcola i numeri di Newton dai dati del testo e delle fonti allegate. Ciò che proviene da conoscenza generale e non dalle fonti allegate è marcato «(non verificato sulle fonti allegate)».

### N0. Note lessicali alla prima occorrenza

- **In conseguenza / in antecedenza** (III.G5.04, III.G5.07): nel verso del moto dei pianeti (da occidente verso oriente, secondo l’ordine dei segni) / nel verso contrario. I nodi lunari si muovono in antecedenza, l’apogeo in conseguenza.
- **Equazione** (III.G5.05, *eorundem æquationes*): nel linguaggio astronomico è la correzione, positiva o negativa, che si aggiunge al moto medio per ottenere il luogo vero; qui le correzioni periodiche dei moti dell’apogeo e dei nodi.
- **Pianeti minori** (III.G5.04): i satelliti, che il glossario del Libro III chiama «pianeti secondari»; nella Prop. XXIII Newton li chiama *lunæ seu satellites*.
- **Prostaferesi** (III.G5.05): § A.0 e nota N2.
- **Terzo** (III.G5.07, 5″ 12‴): sessantesimo di secondo; 5″ 12‴ = 5,2″.
- **Pollice** (III.G5.14–III.G5.15): il latino ha *digitus*; § A.0.
- **Principio dell’Ariete** (III.G5.14): l’inizio del segno, cioè la longitudine 0°, il punto equinoziale di primavera. Il nodo ascendente lì vuol dire che l’orbita lunare è inclinata in modo da portare la Luna alla massima declinazione (non verificato sulle fonti allegate).
- **Orbe magno** (III.G5.35): l’orbita annua della Terra attorno al Sole (o del Sole attorno alla Terra, che per Newton è lo stesso ai fini del calcolo, Fenomeno IV).
- **Tempo sinodico / periodico** (III.G5.23, III.G5.31, III.G5.34): il primo è il ritorno della Luna alla stessa posizione rispetto al Sole (29g 12h 44′), il secondo il ritorno rispetto alle stelle fisse (27g 7h 43′).

### N1. Prop. XXI: precessione e nutazione

Newton applica alla Terra il Cor. 20 della Prop. LXVI del Libro I: un globo con un eccesso di materia all’equatore si comporta come un anello aderente; il Sole e la Luna, attraendo l’anello, fanno retrocedere i suoi nodi sull’eclittica (i punti equinoziali) e oscillare la sua inclinazione. L’oscillazione ha periodo semestrale per il Sole perché l’azione del Sole sul rigonfiamento è nulla quando il Sole è nel piano dell’equatore (equinozi) e massima ai solstizi; donde «due volte all’anno». Il calcolo quantitativo della precessione è nella Prop. XXXIX (Fascicolo 25b).

Confronto moderno (non verificato sulle fonti allegate): la precessione lunisolare vale circa 50″ all’anno; la nutazione semestrale dovuta al Sole ha un’ampiezza di circa 0,5″, davvero «appena sensibile»; la nutazione principale, scoperta da Bradley nel 1748, è dovuta alla Luna, ha periodo di 18,6 anni (il ciclo dei nodi lunari) e ampiezza di circa 9″. Newton, in questa proposizione, non la considera.

### N2. Prop. XXII: il catalogo delle disuguaglianze lunari

La proposizione elenca, con un rimando ciascuna, le disuguaglianze che la Prop. LXVI del Libro I fa prevedere:

| Disuguaglianza | Corollario della Prop. LXVI | Nome moderno (non verificato sulle fonti allegate) |
|---|---|---|
| area più veloce, moto più veloce, orbita meno curva e Luna più vicina nelle sizigie | 2, 3, 4, 5 | variazione (Propp. XXVI–XXIX) |
| eccentricità massima con l’apogeo nelle sizigie, minima nelle quadrature | 9 | evezione |
| apogeo che avanza, nodi che retrocedono, con moti non uniformi | 7, 8, 11 | moto delle apsidi e dei nodi |
| latitudine massima maggiore nelle quadrature | 10 | variazione dell’inclinazione |
| moto medio più lento al perielio della Terra | 6 | equazione annua |
| tutte queste in rapporto triplicato del diametro apparente del Sole | 14 | — |

L’ultima frase dice che la variazione, nei calcoli degli astronomi, finisce dentro la «prostaferesi della Luna»: la correzione principale, cioè l’equazione del centro, che Motte nomina esplicitamente. La variazione era nota a Tycho Brahe (non verificato sulle fonti allegate); la novità di Newton è derivarne la grandezza (Prop. XXIX).

### N3. Prop. XXIII: i satelliti di Giove

**La regola.** Per il Cor. 16 della Prop. LXVI, gli errori angolari in una rivoluzione del satellite stanno come *T*ₛ²/*T*ₚ² (*T*ₛ periodo del satellite, *T*ₚ periodo del pianeta attorno al Sole). Per unità di tempo si divide per *T*ₛ: il moto medio dei nodi sta come *T*ₛ/*T*ₚ². Il rapporto fra satellite e Luna è perciò (*T*_Terra/*T*_Giove)² × (*T*_sat/*T*_Luna): esattamente il «rapporto composto» del testo.

**Il numero 8° 24′.** Con i dati delle fonti allegate — nodi lunari 19° 18′ 1″ 23‴ per anno siderale (Prop. XXXII, nello stesso file latino), Terra 365,2565 giorni e Giove 4332,514 giorni (Fenomeno IV), satellite più esterno 16g 16h 32′ 9″ (Fenomeno I), Luna 27g 7h 43′ (Prop. XXV) — si ottengono **8° 22′ 45″** in cento anni, contro gli 8° 24′ di Newton: scarto di 1,25′ (0,25%), compatibile con dati leggermente diversi.

**La variazione 5″ 12‴.** Con il periodo sinodico del satellite rispetto al Sole visto da Giove (16,7535 giorni) e il mese sinodico (29g 12h 44′), il rapporto dei moti dei nodi nei due tempi sinodici, moltiplicato per 35′ 10″ (Prop. XXIX), dà **5,20″ = 5″ 12‴**: torna.

**La riduzione «5 a 9, o 1 a 2».** Newton non ne dà la causa. Lo stesso metodo lineare, applicato alla Luna, dà per l’apogeo circa la metà del moto osservato (è il celebre problema dell’apside lunare, ripreso da Clairaut nel 1749; non verificato sulle fonti allegate): se il moto dell’apogeo lunare usato come termine di confronto contiene un contributo di ordine superiore che per i satelliti, molto meno perturbati, è trascurabile, la riduzione è nel verso giusto. È un’ipotesi interpretativa, non un dato del testo.

### N4. Prop. XXIV: le maree

**Il quadro.** I Cor. 19 e 20 della Prop. LXVI danno due rigonfiamenti opposti, e quindi due alte maree per giorno lunare. L’alta marea non cade al passaggio della Luna al meridiano, ma circa tre ore dopo, perché la forza «impressa» si accumula finché la marea non smette di crescere: è un argomento d’inerzia, che Motte amplia (§ A.14). Le maree vive (sizigie) e morte (quadrature) nascono dalla somma e dalla differenza degli effetti di Sole e Luna; l’effetto lunare maggiore sposta il massimo verso la terza ora lunare.

**Il rapporto triplicato dei diametri apparenti.** L’effetto di marea di un corpo di massa *M* a distanza *D* è come *M*/*D*³. Se la massa è come la densità per il cubo del raggio, *M*/*D*³ è come la densità per il cubo del diametro apparente: è il Cor. 14 della Prop. LXVI, applicato qui senza citarlo. Il Sole è al perigeo d’inverno (per l’emisfero boreale), e per questo le maree massime e minime cadono più spesso prima dell’equinozio di primavera e dopo quello d’autunno: il perielio cade oggi all’inizio di gennaio (non verificato sulle fonti allegate).

**Lo sferoide.** La figura del mare è uno sferoide allungato con l’asse maggiore diretto verso il punto H che aveva la Luna allo zenit tre ore prima. Un luogo F fuori dell’equatore, nella rotazione diurna, percorre il parallelo Ff, che taglia lo sferoide in punti a distanza diversa dal centro: per questo le due alte maree del giorno sono disuguali (CF ≠ Cf). È la **disuguaglianza diurna**, che si annulla all’equatore e quando la Luna è nell’equatore.

**Batsham.** L’ipotesi di Newton si controlla con un modello minimo: ogni marea oceanica è la somma di una componente semidiurna e di una diurna (Luna declinante), con il massimo maggiore alla terza ora; la seconda marea giunge sei ore dopo. Sommando le due, le componenti semidiurne, sfasate di mezzo periodo, si annullano; le diurne, sfasate di un quarto di periodo, sopravvivono. Lo script dà il massimo **alla sesta ora** e il minimo alla diciottesima; con la Luna nell’equatore (componente diurna nulla) l’acqua resta ferma. È esattamente quanto dice il testo («una volta sola», «alla sesta ora»; la «trentesima» è la sesta del giorno successivo). La marea diurna del golfo del Tonchino è un fenomeno reale, e l’articolo di Halley è del 1684 nelle *Philosophical Transactions* (non verificato sulle fonti allegate); la spiegazione moderna è legata alla risonanza del golfo, non a due canali (non verificato sulle fonti allegate). Newton stesso lascia la questione alle osservazioni.

**La «forza di reciprocazione».** È la tendenza dell’acqua mossa a continuare il moto (Motte la chiama *vis insita*): spiega perché le maree massime a Plymouth e a Bristol sono le terze dopo le sizigie. Oggi si parla di «età della marea» (non verificato sulle fonti allegate).

### N5. Prop. XXV: le forze del Sole

**Costruzione.** SK = ST; SL : SK = SK² : SP², cioè SL è la gravità verso il Sole alla distanza SP, se SK = ST rappresenta quella alla distanza ST. SL si scompone in SM (parallela a ST) e LM (parallela a PT); poiché la Terra è attratta con ST, la parte che perturba il moto relativo è TM (lungo ST) insieme a LM (lungo PT). In termini moderni è la **forza di marea** del Sole sulla Luna, ∝ distanza Terra–Luna e ∝ 1/ST³.

**I numeri.** (365g 6h 9m : 27g 7h 43m)² = 178,72502, cioè 1000 : 178725 = 1 : 178 29/40. Il rapporto 60 ½ : 60 corregge la distanza, il fattore 60 × 60 porta dalla Luna alla superficie terrestre (legge dell’inverso del quadrato, Prop. IV). Risultato: 60³ × 178,725 : 60,5 = **638092,56**; Newton scrive 638092,6. Torna.

### N6. Prop. XXVI: l’incremento orario dell’area

**Geometria.** Con SP ∥ ST e l’angolo θ = CTP contato dalla quadratura: PK = TP sin θ (distanza della Luna dalla linea delle quadrature, verso il Sole), TK = TP cos θ, TM = 3PK. La forza TL si scompone in TE (radiale) ed EL (trasversale), con EL = 3PK × TK/TP = 1,5 TP sin 2θ: massima negli ottanti, 1,5 TP, cioè 3/2 di ML (= TP). Lo script conferma per θ = 10°, 30°, 45°, 60°: EL = 3Kd; Pd = PK²/TP; trapezio FKCG : triangolo TCG = PK² : TP².

**Il numero 11915.** EL massima : forza centripeta lunare = 1,5 : 178,725 = 100 : 11915. Per il Cor. 9 della Prop. IV del Libro I, la forza centripeta genera nel tempo CT (il tempo in cui la Luna percorre un arco uguale al raggio) proprio la velocità della Luna; dunque EL massima genera in quel tempo 100/11915 della velocità. Nel tempo di un quadrante (CA/CT = π/2) la forza massima genererebbe π/2 volte tanto; ma la forza reale è variabile, e la media di sin 2θ sul quadrante è 2/π. I due fattori si compensano: la velocità totale generata in un quadrante è ancora 100/11915. L’integrazione numerica dà 100/11915,0. È il ragionamento di Newton con area KCGF e triangolo TCG.

**Momenti.** Se il momento medio è 11915, l’oscillazione è di ±50: 11965 nelle sizigie, 11865 nelle quadrature. La correzione per il moto del Sole moltiplica l’incremento per il rapporto fra mese sinodico e periodico, 1,080853 (ricalcolato: 1,0808530). Allora 11915 : 1,080853 = **11023,7**: Newton scrive 11023 (troncamento; con l’arrotondamento si avrebbe 11024). Ne seguono 10973 e 11073. La formula finale: il momento in P è come 10973 + Pd, con Pd = 100 sin²θ = 50(1 − cos 2θ); dividendo per 50 si ha 219,46 + seno verso di 2θ. Lo script conferma i valori agli estremi e negli ottanti (10973, 11023, 11073).

**Il limite del metodo.** Newton tratta l’incremento di velocità trasversale come incremento del momento dell’area, su un’orbita circolare e con il tempo uniforme: è un calcolo al primo ordine nella forza perturbatrice. La correzione «in rapporto del tempo» (periodo sinodico invece che siderale) è giustificata perché il ciclo della forza perturbatrice dipende dalla posizione rispetto al Sole.

### N7. Prop. XXVII: la distanza dal moto orario

L’area descritta in un tempo piccolo è ½ *r*² ω (ω moto orario): «come il moto orario e il quadrato della distanza considerati congiuntamente». Di qui *r* ∝ √(momento dell’area) / √ω. Con il momento dato dalla Prop. XXVI e il moto orario osservato si ottiene la distanza, e quindi (Cor. 1) il diametro apparente, inversamente proporzionale alla distanza.

### N8. Prop. XXVIII: l’orbita della variazione

**Curvatura.** Per un corpo attratto perpendicolarmente alla traiettoria, la curvatura è *F*/*v*² (in termini moderni κ = *a*ₙ/*v*²). Nelle sizigie la forza verso la Terra è la gravità meno 2PK, nelle quadrature la gravità più KT; le velocità stanno come 11073CT : 10973AT (momento dell’area diviso per la distanza). Lo script conferma 10973² = 120406729, 11073² = 122611329 e le riduzioni 2151969, 24081, 2191371, 12261.

**I cinque rapporti.** Newton confronta la figura Cpa, descritta nel piano fisso, con l’ellisse DBCA, che ruota con il Sole. Se in una curva polare si moltiplicano gli angoli per *m* lasciando invariate le distanze, nei vertici (dove *r*′ = 0) la curvatura vale 1/*r* − *r*″/(*m*²*r*²): la differenza fra la curvatura della curva e quella del cerchio per il vertice si divide per *m*². È esattamente la regola «in rapporto duplicato dell’angolo CTP all’angolo CTp». Con l’ellisse di semiassi TC (quadrature) e TA (sizigie), curvatura TA/TC² in A e TC/TA² in C, si ottiene

curvatura in a : curvatura in C = AT(AT² + μCT²) : CT(CT² + μAT²), con μ = *m*² − 1.

È la formula di Newton **con il segno «+»** (latino). Con μ = (29g 12h 44′ : 27g 7h 43′)² − 1 = 0,168243 si ritrova 16824/100000.

**L’equazione.** Eguagliando i due rapporti di curvatura e moltiplicando estremi e medi, lo script ottiene i coefficienti 2062,79; 2151969; 368676,26; 36342,00; 362047,26; 2191371; 4051,39: sono quelli di Newton (a meno di un segno comune a tutti i termini). Con N = 1, CT = 1 + *x*, AT = 1 − *x*, la radice è **x = 0,0071900**: torna con lo 0,00719 di Newton. Se si adotta invece il «−» di Motte 1846 (SVG 1036), i segni di tre termini cambiano e l’equazione **non ha radici** fra 0 e 0,05: il segno di Motte 1846 è un errore della sua edizione (§ A.13). 1,00719 : 0,99281 = 1,014484, e (70 1/24) : (69 1/24) = 1,014484: torna.

**Un’approssimazione di Newton.** Nell’espressione della forza nelle sizigie il termine solare è 2000/(CT × N), mentre la forza perturbatrice cresce come la distanza (2000 × AT/N², con N = 1). Al primo ordine in *x* le due espressioni coincidono (1985,72 contro 1985,62 per *x* = 0,00719); Newton lo dichiara con *quam proxime*.

**Confronto moderno** (non verificato sulle fonti allegate): nella teoria moderna la variazione modifica la distanza Terra–Luna di circa lo 0,8% (termine di parallasse di circa 28″ su 3423″), con la Luna più vicina nelle sizigie; il valore di Newton, 0,72%, è dello stesso ordine e ha il segno giusto.

### N9. Prop. XXIX: la variazione

**Prima approssimazione.** In un’ellisse centrata in T, se l’area contata dall’asse maggiore cresce uniformemente, l’angolo «medio» è l’anomalia eccentrica *u* e tan θ = (TA/TC) tan *u*: lo script lo conferma (69/70 per *u* = 20°, 45°, 70°). L’accelerazione dell’area nelle sizigie (11073 : 10973) restringe ancora l’angolo; Newton la rappresenta diminuendo la tangente nel rapporto subduplicato, 69 √(10973/11073) = 68,68772. Negli ottanti arctan(68,6877/70) = **44° 27′ 28″**, e la differenza dal moto medio è **32′ 32″**; il massimo della differenza in tutto il quadrante cade a 45,27° ed è ancora 32′ 32″.

**Dilatazione sinodica.** Tutti gli angoli si dilatano nel rapporto 1,080853: 32′ 32″ × 1,080853 = 35′ 9,9″ = **35′ 10″**. Torna.

**Apogeo e perigeo del Sole.** Con *e* = 16 15/16 : 1000 = 0,016938, la variazione va come (*T*_sinodico)² / *D*³. Se si tiene conto che il mese sinodico si accorcia all’apogeo del Sole (moto apparente del Sole più lento, inversamente come *D*²) e si allunga al perigeo, lo script dà **33′ 16″** e **37′ 13″**; con il solo fattore 1/*D*³ si avrebbero 33′ 26″ e 37′ 01″. I valori di Newton, 33′ 14″ e 37′ 11″, sono vicini al primo calcolo: scarto di 2″, compatibile con un arrotondamento diverso dei dati. L’eccentricità moderna dell’orbita terrestre è circa 0,0167 (non verificato sulle fonti allegate).

**Confronto moderno** (non verificato sulle fonti allegate): l’ampiezza della variazione è di circa 39′ 30″. Il valore teorico di Newton (35′ 10″) è basso di circa l’11%; Newton stesso avverte che trascura la curvatura dell’orbe magno e la maggiore azione del Sole sulla Luna nuova, e lascia agli astronomi l’effetto dell’eccentricità.


---

## Controllo della copertura

Pagine 1726 dai marcatori ‹n› della trascrizione (la Prop. XXI comincia a p. 422, prima del marcatore ‹423›). Motte: estratto senza marcatori di pagina, «sezione corrispondente».

| Identificatori | Incipit latino | Contenuto | 1726 | Motte 1846 |
|---|---|---|---|---|
| III.G5.01–III.G5.02 | *Puncta æquinoctialia regredi* | Prop. XXI, enunciato e dimostrazione | p. 422 | Prop. XXI |
| III.G5.03–III.G5.04 | *Motus omnes lunares* … *Planetas majores* | Prop. XXII, enunciato e primo capoverso | p. 422 | Prop. XXII |
| III.G5.05 | *Sunt etiam aliæ quædam* | Prop. XXII, disuguaglianze non osservate | p. 423 | Prop. XXII |
| III.G5.06–III.G5.07 | *Motus inæquales satellitum jovis* | Prop. XXIII | pp. 423–424 | Prop. XXIII |
| III.G5.08–III.G5.09 | *Fluxum & refluxum maris* … *Mare singulis diebus* | Prop. XXIV, enunciato; le due maree e la terza ora | p. 424 | Prop. XXIV |
| III.G5.10 | *Motus autem bini* | maree vive e morte; ottanti; foci dei fiumi | pp. 424–425 | Prop. XXIV |
| III.G5.11 | *Pendent autem effectus luminarium ex eorum distantiis* | distanze dei luminari | p. 425 | Prop. XXIV |
| III.G5.12 | *Pendet etiam effectus utriusque luminaris ex ipsius declinatione* | declinazione | p. 425 | Prop. XXIV |
| III.G5.13 | *Pendent etiam effectus luminarium ex locorum latitudine* | figura dello sferoide | pp. 425–426 | Prop. XXIV |
| III.G5.14 | *Hinc in revolutione diurna* | maree diurne alterne; Plymouth e Bristol | pp. 426–427 | Prop. XXIV |
| III.G5.15 | *Motus autem hactenus descripti* | forza di reciprocazione | p. 427 | Prop. XXIV |
| III.G5.16 | *Porro fieri potest* | maree composte; Batsham | pp. 427–428 | Prop. XXIV |
| III.G5.17 | *Hactenus causas motuum lunæ & marium* | transizione | p. 428 | Prop. XXIV (fine) |
| III.G5.18–III.G5.19 | *Invenire vires solis* … *Designet S solem* | Prop. XXV | pp. 428–429 | Prop. XXV |
| III.G5.20–III.G5.21 | *Invenire incrementum horarium* … *Diximus aream* | Prop. XXVI, enunciato; costruzione | pp. 429–431 | Prop. XXVI |
| III.G5.22 | *Vis qua luna circa terram quiescentem* | Prop. XXVI, numeri 11915, 11965, 11865 | p. 431 | Prop. XXVI |
| III.G5.23 | *Hæc omnia ita se habent* | correzione sinodica: 11023, 10973, 11073 | p. 432 | Prop. XXVI |
| III.G5.24 | *Area igitur, quam luna* | regola 219,46 + seno verso | p. 432 | Prop. XXVI |
| III.G5.25–III.G5.28 | *Ex motu horario lunæ* … *Corol. 2.* | Prop. XXVII e Cor. 1–2 | p. 432 | Prop. XXVII, Cor. 1–2 |
| III.G5.29–III.G5.30 | *Invenire diametros orbis* … *Curvatura trajectoriæ* | Prop. XXVIII, curvature dalle forze | p. 433 | Prop. XXVIII |
| III.G5.31 | *Quoniam figura orbis lunaris ignoratur* | figura Cpa e curvature geometriche | pp. 433–435 | Prop. XXVIII |
| III.G5.32 | *Igitur cum a designet* | equazione e soluzione 69 : 70 | p. 435 | Prop. XXVIII |
| III.G5.33–III.G5.34 | *Invenire variationem lunæ* … *Oritur hæc inæqualitas* | Prop. XXIX, 32′ 32″ e 35′ 10″ | pp. 435–436 | Prop. XXIX |
| III.G5.35 | *Hæc est ejus magnitudo* | apogeo e perigeo del Sole | p. 436 | Prop. XXIX |
| III.G5.36 | *Hactenus variationem investigavimus* | orbita eccentrica | pp. 436–437 | Prop. XXIX (fine) |

**Controlli eseguiti.**

1. **Copertura frase per frase.** Ho riletto in sequenza ogni periodo della trascrizione, da *Puncta æquinoctialia regredi* a *ab astronomis per phænomena determinandum relinquo* (righe 12–102), contro la traduzione: nessuna frase manca. Il testo tradotto è generato da un unico elenco di frasi allineate al latino (`tmp/24a/testo.py`), lo stesso che produce i passi della Parte B: per le unità con passi la corrispondenza frase latina ↔ frase italiana è quindi uno a uno; per le altre (Propp. XXI, XXII, XXIV fuori dal capoverso della figura) l’ho controllata a vista. I 36 identificatori sono consecutivi e unici (controllo automatico).
2. **Parte B.** `check.py` sul file finale: JSON valido; 9 unità, 86 passi; tutte le stringhe `la` (enunciati e passi) sono sottostringhe esatte della trascrizione; tutte le stringhe `en` sono sottostringhe esatte di Motte (nessun avviso); ogni identificatore di `copertura` è presente nel testo. Ultima riga: «OK».
3. **Matematica** (`verifica.py`): Prop. XXIII (8° 22′ 45″ contro 8° 24′; 5,20″ contro 5″ 12‴); Prop. XXIV (composizione delle maree di Batsham: massimo alla sesta ora); Prop. XXV (178,72502; 638092,56); Prop. XXVI (relazioni geometriche, integrale del quadrante, 11915, 1,0808530, 11023,7, 219,46); Prop. XXVIII (μ = 0,168243; prodotti; coefficienti dell’equazione; radice 0,0071900; segno del primo termine); Prop. XXIX (tangenti; 44° 27′ 28″; 32′ 32″; 35′ 10″; 33′ 16″ e 37′ 13″ contro 33′ 14″ e 37′ 11″). **Cifre che non tornano esattamente**, non corrette nel testo: 11023 (calcolo 11023,7); 8° 24′ (calcolo 8° 22′ 45″, con dati forse diversi da quelli di Newton); 33′ 14″ e 37′ 11″ (calcolo 33′ 16″ e 37′ 13″).
4. **Tabelle numeriche:** il fascicolo non contiene tabelle; i numeri dei calcoli sono raccolti nei campi `dati` della Parte B.
5. **Motte e SVG.** Confronto di tutta la parte corrispondente (righe 7–641 dell’estratto); divergenze nel § A.14. 21 formule SVG controllate sul LaTeX, una non torna (SVG 1036, § A.13).
6. **Rimandi.** 20 citazioni ai Libri I e II verificate sui Fascicoli 3, 4, 5 e 10; una non torna (Cor. 2 per i nodi, da leggere Cor. 11). Rimandi al Libro III (Prop. IV; figura di p. 428) verificati sul latino.
7. **Separazione fra testo e commento.** Il testo tradotto non contiene formule moderne; le espressioni algebriche della Prop. XXVIII sono di Newton.

**Non ho potuto verificare:**

- **la stampa del 1726**: i punti del § A.11 restano «probabili»; in particolare il «Cor. 2» per i nodi e il «sol» per «luna» nella Prop. XXIV;
- **le figure originali** delle Propp. XXIV, XXV, XXVI, XXVIII e XXIX: la disposizione dei punti è ricostruita dal testo; il punto Q della Prop. XXIV non è definito nel testo;
- **Motte 1729**, per stabilire se il «−» di SVG 1036 è già nella prima edizione inglese o solo nella ristampa del 1846;
- **la paginazione di Motte**: l’estratto non ha marcatori di pagina;
- il **rimando a Euclide, *Elementi* V, 9**, e i dati moderni delle note (precessione e nutazione, ampiezza della variazione, termine di parallasse, eccentricità terrestre, articolo di Halley), che vengono da conoscenza generale;
- i **valori esatti usati da Newton** per i nodi lunari e per i periodi nella Prop. XXIII, da cui dipende lo scarto di 1,25′ su 8° 24′.

---

## Registro del lavoro successivo

| Unità | Stato |
|---|---|
| Libro III, Propp. XXI–XXIX | **Fascicolo 24a, presente documento, prima versione** |
| Propp. XXX–XXXIII, Scolio (Machin), Scolio finale | Fascicolo 24b (altro traduttore); identificatori da rinumerare in serie dopo III.G5.36 |
| Refusi e letture del § A.11 | Da verificare sulla stampa del 1726 (scansione ECCO) |
| Rimando *corol. 2.* per i nodi (Prop. XXII) | Da decidere dopo la verifica: nel testo è «Cor. [11]» |
| SVG 1036 di Motte (segno) | Da controllare su Motte 1729; nella pagina interattiva il testo a fronte di Motte va corretto con una nota («Motte 1846: −; latino 1726: +») |
| *digitus* «pollice» (Prop. XXIV) contro «dito» del Fascicolo 3 | Da armonizzare (A.0) |
| *affluxus / defluxus* «afflusso / deflusso», *fluctus* «flutto», *reciprocatio* «reciprocazione» | Termini nuovi, da armonizzare con il Fascicolo 25a–25b se vi ricorrono |
| Pagine interattive | Parte B: Propp. XXV–XXIX (catena di calcolo della variazione), Prop. XXIV (sferoide di marea), Prop. XXIII; candidati: un riquadro «che cosa torna» con i ricalcoli di N6, N8, N9 e l’equazione della Prop. XXVIII risolta in diretta |
| Figure NATP00303 | Da consultare per confermare le ricostruzioni di `figura_base` e il punto Q |
| Revisione filologica e scientifica indipendente | Da eseguire |

Il presente testo è una nuova traduzione assistita da IA. Non riproduce traduzioni italiane o inglesi moderne. **Licenza prevista** (decisione del curatore, Fascicolo 3): testi e traduzioni CC BY-SA 4.0, codice MIT. La trascrizione latina è © The Newton Project; i testi di Motte sono di pubblico dominio.


---

## Parte B — Dati per le pagine interattive

Unità incluse: una per proposizione, **L3-P21 … L3-P29**. Con passi (uno per frase latina): **L3-P23** (calcolo dei satelliti, 7 passi), **L3-P24** (solo il capoverso con la figura dello sferoide, III.G5.13–III.G5.14, 10 passi: vedi la `nota` dell’unità), **L3-P25** (9), **L3-P26** (26), **L3-P27** (1), **L3-P28** (20), **L3-P29** (13). Senza passi: **L3-P21** e **L3-P22**, la cui dimostrazione consiste in rimandi al Libro I. I Cor. 1–2 della Prop. XXVII non hanno dimostrazione propria e non entrano come unità.

Convenzioni:

- `la`: testo latino esatto della trascrizione, refusi, marcatori di pagina e [FIG] compresi; le formule appiattite restano come sono (letture nel § A.10 e nelle `nota`);
- `it`: la traduzione di questo fascicolo, identica al testo;
- `en`: Motte 1846, allineato per senso, con i marcatori `[SVG n]` della fonte; dove Motte unisce due frasi latine con un punto e virgola, il taglio cade sul punto e virgola;
- `dipende_da`: soltanto i rimandi citati nella frase latina;
- `figura.mostra`: elementi da rendere visibili, cumulativi; `figura.evidenzia`: relazioni da mettere in risalto;
- `dati`: valori numerici e risultati dei ricalcoli (`verifica.py`).


```json
{
 "fascicolo": "24a-L3-P21-29",
 "versione": "0.1",
 "data": "2026-11-08",
 "convenzioni": {
  "dipende_da": "solo rimandi citati esplicitamente nella frase latina",
  "en": "Motte 1846, allineato per senso; i marcatori [SVG n] sono lasciati come nella fonte (il LaTeX è in svg_tex.tsv)",
  "figura.mostra": "elementi da rendere visibili al passo, cumulativi salvo indicazione",
  "la": ""
 },
 "unita": [
  {
   "id": "L3-P21",
   "tipo": "Propositio/Theorema",
   "titolo": "Prop. XXI — precessione degli equinozi e nutazione",
   "copertura": [
    "III.G5.01",
    "III.G5.02"
   ],
   "fonti": {
    "la": "",
    "en": "Motte 1846, sezione corrispondente (Book III, Prop. XXI)"
   },
   "enunciato": {
    "la": "",
    "it": "I punti equinoziali retrocedono, e l’asse della Terra, con un moto di nutazione, a ogni rivoluzione annua si inclina due volte verso l’eclittica e due volte ritorna alla posizione di prima.",
    "en": "That the equinoctial points go backward, and that the axis of the earth, by a nutation in every annual revolution, twice vibrates towards the ecliptic, and as often returns to its former position."
   },
   "nota": "La dimostrazione si riduce a un rimando (Cor. 20 della Prop. LXVI del Libro I, verificato sul Fascicolo 10, S11.59) e a una stima qualitativa: unità senza passi.",
   "passi": []
  },
  {
   "id": "L3-P22",
   "tipo": "Propositio/Theorema",
   "titolo": "Prop. XXII — tutti i moti della Luna seguono dai principi",
   "copertura": [
    "III.G5.03",
    "III.G5.04",
    "III.G5.05"
   ],
   "fonti": {
    "la": "",
    "en": "Motte 1846, sezione corrispondente (Book III, Prop. XXII)"
   },
   "enunciato": {
    "la": "",
    "it": "Tutti i moti della Luna, e tutte le disuguaglianze dei suoi moti, seguono dai principi esposti.",
    "en": "That all the motions of the moon, and all the inequalities of those motions, follow from the principles which we have laid down."
   },
   "nota": "Argomento per rimandi, senza costruzione né calcolo: unità senza passi. Rimandi verificati sul Fascicolo 10: Prop. LXV; Prop. LXVI, Cor. 2, 3, 4, 5, 6, 7, 8, 9, 10, 14, 16; Lemma X, Cor. 1–2 (Fascicolo 4). Per i nodi la trascrizione ha «corol. 2.», Motte «Cor. 11»: è il Cor. 11 che tratta dei nodi (refuso probabile, da verificare sulla stampa).",
   "passi": []
  },
  {
   "id": "L3-P23",
   "tipo": "Propositio/Problema",
   "titolo": "Prop. XXIII — i moti dei satelliti di Giove dedotti da quelli della Luna",
   "copertura": [
    "III.G5.06",
    "III.G5.07"
   ],
   "fonti": {
    "la": "",
    "en": "Motte 1846, sezione corrispondente (Book III, Prop. XXIII)"
   },
   "enunciato": {
    "la": "",
    "it": "Derivare dai moti lunari i moti disuguali dei satelliti di Giove e di Saturno.",
    "en": "To derive the unequal motions of the satellites of Jupiter and Saturn from the motions of our moon."
   },
   "dati": {
    "periodi_giorni": {
     "Terra": 365.2565,
     "Giove": 4332.514,
     "satellite_IV": 16.689,
     "Luna_periodico": 27.32153
    },
    "fonte_periodi": "Fenomeni I e IV (latino L3-Regole-Fenomeni); mese periodico 27g 7h 43m (Prop. XXV)",
    "moto_nodi_lunari_annuo": "19° 18′ 1″ 23‴ (Prop. XXXII, latino L3-P21-33)",
    "verifiche": {
     "nodi_satellite_IV_100_anni": {
      "Newton": "8° 24′",
      "ricalcolo": "8° 22′ 45″"
     },
     "variazione_satellite_IV": {
      "Newton": "5″ 12‴",
      "ricalcolo": "5,20″ (periodo sinodico 16,7535 g)"
     }
    }
   },
   "passi": [
    {
     "id": "L3-P23-p1",
     "la": "",
     "it": "Dai moti della nostra Luna si derivano così i moti analoghi delle lune, ossia dei satelliti, di Giove.",
     "en": "From the motions of our moon we deduce the corresponding motions of the moons or satellites of Jupiter in this manner, by Cor. 16, Prop. LXVI, Book I.",
     "dipende_da": [],
     "figura": {
      "mostra": [],
      "evidenzia": []
     },
     "nota": "Passo introduttivo. Motte inserisce qui il rimando al Cor. 16 della Prop. LXVI, che nel latino è nella frase seguente."
    },
    {
     "id": "L3-P23-p2",
     "la": "",
     "it": "Il moto medio dei nodi del satellite più esterno di Giove sta al moto medio dei nodi della nostra Luna nel rapporto composto dal rapporto duplicato del tempo periodico della Terra attorno al Sole al tempo periodico di Giove attorno al Sole e dal rapporto semplice del tempo periodico del satellite attorno a Giove al tempo periodico della Luna attorno alla Terra (per il Cor. 16 della Prop. LXVI del Libro I); e perciò in cento anni quel nodo compie 8° 24′ in antecedenza.",
     "en": "The mean motion of the nodes of the outmost satellite of Jupiter is to the mean motion of the nodes of our moon in a proportion compounded of the duplicate proportion of the periodic times of the earth about the sun to the periodic times of Jupiter about the sun, and the simple proportion of the periodic time of the satellite about Jupiter to the periodic time of our moon about the earth; and, therefore, those nodes, in the space of a hundred years, are carried 8° 24' backward, or in antecedentia.",
     "dipende_da": [
      "Libro I, Prop. LXVI, Cor. 16"
     ],
     "figura": {
      "mostra": [
       "tempo periodico della Terra",
       "tempo periodico di Giove",
       "tempo periodico del satellite più esterno",
       "tempo periodico della Luna"
      ],
      "evidenzia": [
       "nodi del satellite : nodi lunari = (T Terra : T Giove)² × (T satellite : T Luna)",
       "8° 24′ in cento anni"
      ]
     },
     "nota": "Ricalcolo con i dati delle fonti: 8° 22′ 45″ (nota N3)."
    },
    {
     "id": "L3-P23-p3",
     "la": "",
     "it": "I moti medi dei nodi dei satelliti interni stanno al moto di questo come i loro tempi periodici stanno al tempo periodico di questo (per lo stesso corollario), e di qui sono dati.",
     "en": "The mean motions of the nodes of the inner satellites are to the mean motion of the nodes of the outmost as their periodic times to the periodic time of the former, by the same Corollary, and are thence given.",
     "dipende_da": [
      "Libro I, Prop. LXVI, Cor. 16 (per idem corollarium)"
     ],
     "figura": {
      "mostra": [
       "satelliti interni"
      ],
      "evidenzia": [
       "moti dei nodi come i tempi periodici"
      ]
     }
    },
    {
     "id": "L3-P23-p4",
     "la": "",
     "it": "Il moto dell’auge di ciascun satellite in conseguenza sta poi al moto dei suoi nodi in antecedenza come il moto dell’apogeo della nostra Luna sta al moto dei suoi nodi (per lo stesso corollario), e di qui è dato.",
     "en": "And the motion of the apsis of every satellite in consequentia is to the motion of its nodes in antecedentia as the motion of the apogee of our moon to the motion of its nodes (by the same Corollary), and is thence given.",
     "dipende_da": [
      "Libro I, Prop. LXVI, Cor. 16 (per idem corollarium)"
     ],
     "figura": {
      "mostra": [],
      "evidenzia": [
       "auge del satellite : suoi nodi = apogeo lunare : nodi lunari"
      ]
     },
     "nota": "Motte rende *augis* con «apsis»."
    },
    {
     "id": "L3-P23-p5",
     "la": "",
     "it": "Il moto dell’auge così trovato deve però essere diminuito nel rapporto di 5 a 9, o di circa 1 a 2, per una causa che qui non ho modo di esporre.",
     "en": "But the motions of the apsides thus found must be diminished in the proportion of 5 to 9, or of about 1 to 2, on account of a cause which I cannot here descend to explain.",
     "dipende_da": [],
     "figura": {
      "mostra": [],
      "evidenzia": [
       "diminuzione nel rapporto 5 : 9, o circa 1 : 2"
      ]
     },
     "nota": "La causa non è esposta nel testo."
    },
    {
     "id": "L3-P23-p6",
     "la": "",
     "it": "Le equazioni massime dei nodi e dell’auge di ciascun satellite stanno all’incirca alle equazioni massime dei nodi e dell’auge della Luna, rispettivamente, come i moti dei nodi e dell’auge dei satelliti nel tempo di una rivoluzione delle prime equazioni stanno ai moti dei nodi e dell’apogeo della Luna nel tempo di una rivoluzione delle seconde.",
     "en": "The greatest equations of the nodes, and of the apsis of every satellite, are to the greatest equations of the nodes, and apogee of our moon respectively, as the motions of the nodes and apsides of the satellites, in the time of one revolution of the former equations, to the motions of the nodes and apogee of our moon, in the time of one revolution of the latter equations.",
     "dipende_da": [],
     "figura": {
      "mostra": [],
      "evidenzia": [
       "equazioni massime come i moti dei nodi e dell’auge in una rivoluzione delle equazioni"
      ]
     }
    },
    {
     "id": "L3-P23-p7",
     "la": "",
     "it": "La variazione di un satellite visto da Giove sta alla variazione della Luna come stanno fra loro i moti totali dei nodi nei tempi in cui il satellite e la Luna ritornano al Sole, per lo stesso corollario; e perciò nel satellite più esterno non supera 5″ 12‴.",
     "en": "The variation of a satellite seen from Jupiter is to the variation of our moon in the same proportion as the whole motions of their nodes respectively during the times in which the satellite and our moon (after parting from) are revolved (again) to the sun, by the same Corollary; and therefore in the outmost satellite the variation does not exceed 5'' 12'''.",
     "dipende_da": [
      "Libro I, Prop. LXVI, Cor. 16 (per idem corollarium)"
     ],
     "figura": {
      "mostra": [
       "periodo sinodico del satellite",
       "mese sinodico"
      ],
      "evidenzia": [
       "5″ 12‴"
      ]
     },
     "nota": "Ricalcolo: 5,20″ (nota N3). Motte aggiunge «(after parting from)» e «(again)»."
    }
   ]
  },
  {
   "id": "L3-P24",
   "tipo": "Propositio/Theorema",
   "titolo": "Prop. XXIV — le maree",
   "copertura": [
    "III.G5.08",
    "III.G5.09",
    "III.G5.10",
    "III.G5.11",
    "III.G5.12",
    "III.G5.13",
    "III.G5.14",
    "III.G5.15",
    "III.G5.16",
    "III.G5.17"
   ],
   "fonti": {
    "la": "",
    "en": "Motte 1846, sezione corrispondente (Book III, Prop. XXIV)"
   },
   "enunciato": {
    "la": "",
    "it": "Il flusso e il riflusso del mare nascono dalle azioni del Sole e della Luna.",
    "en": "That the flux and reflux of the sea arise from the actions of the sun and moon."
   },
   "nota": "Proposizione lunga e in gran parte descrittiva. I passi coprono soltanto il capoverso con la figura (III.G5.13–III.G5.14: sferoide di marea, latitudine dei luoghi, maree diurne alterne), che è la parte che una pagina interattiva può mostrare; gli altri capoversi sono coperti dall’unità ma senza passi.",
   "figura_base": {
    "punti": [
     "A",
     "p",
     "E",
     "P",
     "C",
     "F",
     "f",
     "D",
     "d",
     "L",
     "H",
     "h",
     "K",
     "k",
     "N",
     "M",
     "R",
     "S",
     "T",
     "Q"
    ],
    "vincoli": [
     "ApEP sezione meridiana della Terra, C centro, P e p poli, AE equatore",
     "Ff parallelo del luogo F; Dd parallelo simmetrico rispetto all’equatore",
     "H sotto la Luna (posizione di tre ore prima, L), h opposto; K, k a 90° da H",
     "ellisse di assi Hh (maggiore) e Kk; sferoide HPKhpk per rotazione attorno a Hh",
     "N descrive il cerchio NM nella rotazione; R, T su Ff, Dd; S su AE",
     "Q: punto della figura non definito nel testo (minima altezza sul parallelo)"
    ]
   },
   "passi": [
    {
     "id": "L3-P24-p1",
     "la": "",
     "it": "Gli effetti dei luminari dipendono anche dalla latitudine dei luoghi.",
     "en": "Moreover, the effects of the luminaries depend upon the latitudes of places.",
     "dipende_da": [],
     "figura": {
      "mostra": [
       "Terra ApEP"
      ],
      "evidenzia": []
     }
    },
    {
     "id": "L3-P24-p2",
     "la": "",
     "it": "Rappresenti ApEP la Terra coperta da ogni parte di acque profonde; C il suo centro; P, p i poli; AE l’equatore; F un luogo qualsiasi fuori dell’equatore; Ff il parallelo del luogo; Dd il parallelo corrispondente dall’altra parte dell’equatore; L il luogo che la Luna occupava tre ore prima; H il luogo della Terra che le sta perpendicolarmente sotto; h il luogo opposto a questo; K, k i luoghi distanti di lì 90 gradi; CH, Ch le altezze massime del mare misurate dal centro della Terra; e CK, Ck le altezze minime: se con gli assi Hh, Kk si descrive un’ellisse, e poi con la rivoluzione di questa ellisse attorno all’asse maggiore Hh si descrive lo sferoide HPKhpk, questo rappresenterà con ottima approssimazione la figura del mare, e CF, Cf, CD, Cd saranno le altezze del mare nei luoghi F, f, D, d.",
     "en": "Let ApEP represent the earth covered with deep waters; C its centre; P, p its poles; AE the equator; F any place without the equator; Ff the parallel of the place; Dd the correspondent parallel on the other side of the equator; L the place of the moon three hours before; H the place of the earth directly under it; h the opposite place; K, k the places at 90 degrees distance; CH, Ch, the greatest heights of the sea from the centre of the earth; and CK, Ck, its least heights: and if with the axes Hh, Kk, an ellipsis is described, and by the revolution of that ellipsis about its longer axis Hh a spheroid HPKhpk is formed, this spheroid will nearly represent the figure of the sea; and CF, Cf, CD, Cd, will represent the heights of the sea in the places Ff, Dd.",
     "dipende_da": [],
     "figura": {
      "mostra": [
       "C",
       "P, p",
       "AE",
       "F",
       "Ff",
       "Dd",
       "L",
       "H",
       "h",
       "K, k",
       "ellisse di assi Hh, Kk",
       "sferoide HPKhpk"
      ],
      "evidenzia": [
       "CH, Ch altezze massime",
       "CK, Ck altezze minime",
       "CF, Cf, CD, Cd altezze nei luoghi F, f, D, d"
      ]
     },
     "nota": "Motte: «in the places Ff, Dd» per *in locis F, f, D, d*."
    },
    {
     "id": "L3-P24-p3",
     "la": "",
     "it": "Inoltre, se nella suddetta rivoluzione dell’ellisse un punto qualsiasi N descrive il cerchio NM, che taglia i paralleli Ff, Dd in luoghi qualsiasi R, T, e l’equatore AE in S, CN sarà l’altezza del mare in tutti i luoghi R, S, T situati su questo cerchio.",
     "en": "But farther; in the said revolution of the ellipsis any point N describes the circle NM cutting the parallels Ff, Dd, in any places RT, and the equator AE in S; CN will represent the height of the sea in all those places R, S, T, situated in this circle.",
     "dipende_da": [],
     "figura": {
      "mostra": [
       "N",
       "cerchio NM",
       "R, T",
       "S"
      ],
      "evidenzia": [
       "CN = altezza del mare in R, S, T"
      ]
     },
     "nota": "Motte: «in any places RT» per *in locis quibusvis R, T*."
    },
    {
     "id": "L3-P24-p4",
     "la": "",
     "it": "Di qui, nella rivoluzione diurna di un luogo qualsiasi F, l’afflusso sarà massimo in F, alla terza ora dopo l’arrivo della Luna al meridiano sopra l’orizzonte; poi il deflusso massimo in Q, alla terza ora dopo il tramonto della Luna; quindi l’afflusso massimo in f, alla terza ora dopo l’arrivo della Luna al meridiano sotto l’orizzonte; infine il deflusso massimo in Q, alla terza ora dopo il sorgere della Luna; e l’afflusso successivo in f sarà minore dell’afflusso precedente in F.",
     "en": "Wherefore, in the diurnal revolution of any place F, the greatest flood will be in F, at the third hour after the appulse of the moon to the meridian above the horizon; and afterwards the greatest ebb in Q, at the third hour after the setting of the moon; and then the greatest flood in f, at the third hour after the appulse of the moon to the meridian under the horizon; and, lastly, the greatest ebb in Q, at the third hour after the rising of the moon; and the latter flood in f will be less than the preceding flood in F.",
     "dipende_da": [],
     "figura": {
      "mostra": [
       "rotazione diurna di F",
       "f",
       "Q"
      ],
      "evidenzia": [
       "afflusso massimo in F",
       "deflusso massimo in Q",
       "afflusso in f minore di quello in F"
      ]
     },
     "nota": "Q non è definito nel testo: compare solo nella figura, non disponibile."
    },
    {
     "id": "L3-P24-p5",
     "la": "",
     "it": "Tutto il mare, infatti, si divide in due soli flutti emisferici, uno nell’emisfero KHk, rivolto verso borea, l’altro nell’emisfero opposto Khk; li si può dunque chiamare flutto boreale e flutto australe.",
     "en": "For the whole sea is divided into two hemispherical floods, one in the hemisphere KHk on the north side, the other in the opposite hemisphere Khk, which we may therefore call the northern and the southern floods.",
     "dipende_da": [],
     "figura": {
      "mostra": [
       "emisfero KHk",
       "emisfero Khk"
      ],
      "evidenzia": [
       "flutto boreale",
       "flutto australe"
      ]
     },
     "nota": "La trascrizione ha «hæmisphærio» accanto a «hemisphærio»: refuso probabile."
    },
    {
     "id": "L3-P24-p6",
     "la": "",
     "it": "Questi flutti, sempre opposti l’uno all’altro, giungono a turno ai meridiani dei singoli luoghi, a un intervallo di dodici ore lunari.",
     "en": "These floods, being always opposite the one to the other, come by turns to the meridians of all places, after an interval of 12 lunar hours.",
     "dipende_da": [],
     "figura": {
      "mostra": [],
      "evidenzia": [
       "intervallo di dodici ore lunari"
      ]
     }
    },
    {
     "id": "L3-P24-p7",
     "la": "",
     "it": "E poiché le regioni boreali partecipano di più del flutto boreale, e le australi dell’australe, ne nascono maree alternativamente maggiori e minori in tutti i luoghi fuori dell’equatore nei quali i luminari sorgono e tramontano.",
     "en": "And seeing the northern countries partake more of the northern flood, and the southern countries more of the southern flood, thence arise tides, alternately greater and less in all places without the equator, in which the luminaries rise and set.",
     "dipende_da": [],
     "figura": {
      "mostra": [],
      "evidenzia": [
       "maree alterne fuori dell’equatore"
      ]
     }
    },
    {
     "id": "L3-P24-p8",
     "la": "",
     "it": "La marea maggiore, quando la Luna declina verso lo zenit del luogo, cadrà circa alla terza ora dopo l’arrivo della Luna al meridiano sopra l’orizzonte, e quando la Luna cambia declinazione si volgerà in minore.",
     "en": "But the greatest tide will happen when the moon declines towards the vertex of the place, about the third hour after the appulse of the moon to the meridian above the horizon; and when the moon changes its declination to the other side of the equator, that which was the greater tide will be changed into a lesser.",
     "dipende_da": [],
     "figura": {
      "mostra": [
       "Luna declinante verso lo zenit del luogo"
      ],
      "evidenzia": [
       "marea maggiore alla terza ora dopo il passaggio superiore"
      ]
     }
    },
    {
     "id": "L3-P24-p9",
     "la": "",
     "it": "E la differenza massima dei flussi cadrà nei tempi dei solstizi, soprattutto se il nodo ascendente della Luna si trova al principio dell’Ariete.",
     "en": "And the greatest difference of the floods will fall out about the times of the solstices; especially if the ascending node of the moon is about the first of Aries.",
     "dipende_da": [],
     "figura": {
      "mostra": [],
      "evidenzia": [
       "differenza massima ai solstizi",
       "nodo ascendente al principio dell’Ariete"
      ]
     }
    },
    {
     "id": "L3-P24-p10",
     "la": "",
     "it": "Così si è trovato per esperienza che le maree del mattino nel tempo invernale superano quelle della sera, e quelle della sera nel tempo estivo quelle del mattino: a Plymouth di un’altezza di quasi un piede, a Bristol di un’altezza di quindici pollici, secondo le osservazioni di Colepress e di Sturmy.",
     "en": "So it is found by experience that the morning tides in winter exceed those of the evening, and the evening tides in summer exceed those of the morning; at Plymouth by the height of one foot, but at Bristol by the height of 15 inches, according to the observations of Colepress and Sturmy.",
     "dipende_da": [],
     "figura": {
      "mostra": [],
      "evidenzia": [
       "Plymouth: quasi un piede",
       "Bristol: quindici pollici"
      ]
     },
     "nota": "Motte: «inches» per *digitorum*."
    }
   ]
  },
  {
   "id": "L3-P25",
   "tipo": "Propositio/Problema",
   "titolo": "Prop. XXV — le forze del Sole che perturbano i moti della Luna",
   "copertura": [
    "III.G5.18",
    "III.G5.19"
   ],
   "fonti": {
    "la": "",
    "en": "Motte 1846, sezione corrispondente (Book III, Prop. XXV)"
   },
   "enunciato": {
    "la": "",
    "it": "Trovare le forze del Sole che perturbano i moti della Luna.",
    "en": "To find the forces with which the sun disturbs the motions of the moon."
   },
   "figura_base": {
    "punti": [
     "S",
     "T",
     "P",
     "C",
     "A",
     "D",
     "B",
     "K",
     "L",
     "M"
    ],
    "vincoli": [
     "CADB orbita della Luna attorno a T",
     "K su SP con SK = ST",
     "L su SP con SL : SK = SK² : SP²",
     "M su ST con LM ∥ PT"
    ]
   },
   "dati": {
    "ML_su_forza_lunare": "1 : 178,725 (ricalcolo 178,72502)",
    "ML_su_gravita": "1 : 638092,6 (ricalcolo 638092,56)"
   },
   "passi": [
    {
     "id": "L3-P25-p1",
     "la": "",
     "it": "Rappresenti S il Sole, T la Terra, P la Luna, CADB l’orbita della Luna.",
     "en": "Let S represent the sun, T the earth, P the moon, CADB the moon's orbit.",
     "dipende_da": [],
     "figura": {
      "mostra": [
       "S",
       "T",
       "P",
       "orbita CADB"
      ],
      "evidenzia": []
     }
    },
    {
     "id": "L3-P25-p2",
     "la": "",
     "it": "Su SP si prenda SK uguale a ST; SL stia a SK in rapporto duplicato di SK a SP; e si conduca LM parallela a PT: se la gravità acceleratrice della Terra verso il Sole è rappresentata dalla distanza ST o SK, SL sarà la gravità acceleratrice della Luna verso il Sole.",
     "en": "In SP take SK equal to ST; and let SL be to SK in the duplicate proportion of SK to SP: draw LM parallel to PT; and if ST or SK is supposed to represent the accelerated force of gravity of the earth towards the sun, SL will represent the accelerative force of gravity of the moon towards the sun.",
     "dipende_da": [],
     "figura": {
      "mostra": [
       "SP",
       "K (SK = ST)",
       "L (SL : SK = SK² : SP²)",
       "LM ∥ PT"
      ],
      "evidenzia": [
       "ST = gravità acceleratrice della Terra verso il Sole",
       "SL = gravità acceleratrice della Luna verso il Sole"
      ]
     },
     "nota": "Motte: «accelerated force of gravity» per la Terra, «accelerative» per la Luna."
    },
    {
     "id": "L3-P25-p3",
     "la": "",
     "it": "Essa si compone delle parti SM, LM, delle quali LM e la parte TM di SM perturbano il moto della Luna, come si è esposto nella Prop. LXVI del Libro I e nei suoi corollari.",
     "en": "But that force is compounded of the parts SM and LM, of which the force LM, and that part of SM which is represented by TM, disturb the motion of the moon, as we have shewn in Prop. LXVI, Book I, and its Corollaries.",
     "dipende_da": [
      "Libro I, Prop. LXVI e corollari"
     ],
     "figura": {
      "mostra": [
       "SM",
       "LM",
       "TM"
      ],
      "evidenzia": [
       "LM e TM forze perturbatrici"
      ]
     }
    },
    {
     "id": "L3-P25-p4",
     "la": "",
     "it": "In quanto la Terra e la Luna ruotano attorno al centro comune di gravità, anche il moto della Terra attorno a quel centro sarà perturbato da forze del tutto simili; ma si possono riferire alla Luna le somme sia delle forze sia dei moti, e rappresentare le somme delle forze con le linee TM e ML, che sono loro analoghe.",
     "en": "Forasmuch as the earth and moon are revolved about their common centre of gravity, the motion of the earth about that centre will be also disturbed by the like forces; but we may consider the sums both of the forces and of the motions as in the moon, and represent the sum of the forces by the lines TM and ML, which are analogous to them both.",
     "dipende_da": [],
     "figura": {
      "mostra": [
       "centro comune di gravità di T e P"
      ],
      "evidenzia": [
       "somme delle forze riferite alla Luna"
      ]
     }
    },
    {
     "id": "L3-P25-p5",
     "la": "",
     "it": "La forza ML, nella sua quantità media, sta alla forza centripeta con cui la Luna potrebbe ruotare nella sua orbita attorno alla Terra in quiete, alla distanza PT, in rapporto duplicato dei tempi periodici della Luna attorno alla Terra e della Terra attorno al Sole (per il Cor. 17 della Prop. LXVI del Libro I), cioè in rapporto duplicato di 27 giorni 7 ore 43 minuti a 365 giorni 6 ore 9 minuti, ossia come 1000 a 178725, o come 1 a 178 29/40.",
     "en": "The force ML (in its mean quantity) is to the centripetal force by which the moon may be retained in its orbit revolving about the earth at rest, at the distance PT, in the duplicate proportion of the periodic time of the moon about the earth to the periodic time of the earth about the sun (by Cor. 17, Prop. LXVI, Book I); that is, in the duplicate proportion of 27d. 7h. 43' to 365d. 6h. 9'; or as 1000 to 178725; or as 1 to [SVG 963] .",
     "dipende_da": [
      "Libro I, Prop. LXVI, Cor. 17"
     ],
     "figura": {
      "mostra": [],
      "evidenzia": [
       "ML : forza centripeta lunare = 1000 : 178725"
      ]
     },
     "nota": "Ricalcolo: (365g 6h 9m : 27g 7h 43m)² = 178,72502."
    },
    {
     "id": "L3-P25-p6",
     "la": "",
     "it": "Abbiamo poi trovato nella Prop. IV che, se la Terra e la Luna ruotano attorno al centro comune di gravità, la loro distanza media l’una dall’altra sarà di 60 ½ semidiametri medi della Terra, con ottima approssimazione.",
     "en": "But in the 4th Prop. of this Book we found, that, if both earth and moon were revolved about their common centre of gravity, the mean distance of the one from the other would be nearly [SVG 968] mean semi-diameters of the earth;",
     "dipende_da": [
      "Libro III, Prop. IV"
     ],
     "figura": {
      "mostra": [],
      "evidenzia": [
       "distanza media 60 ½ semidiametri terrestri"
      ]
     },
     "nota": "Verificato sul latino della Prop. IV (L3-P01-14): «60⁤12 semidiametrorum terrestrium»."
    },
    {
     "id": "L3-P25-p7",
     "la": "",
     "it": "E la forza con cui la Luna potrebbe ruotare in un’orbita attorno alla Terra in quiete, alla distanza PT di 60 ½ semidiametri terrestri, sta alla forza con cui potrebbe ruotare nello stesso tempo alla distanza di 60 semidiametri come 60 ½ sta a 60; e questa forza sta alla forza di gravità presso di noi come 1 a 60 × 60, con ottima approssimazione.",
     "en": "and the force by which the moon may be kept revolving in its orbit about the earth in rest at the distance PT of [SVG 968] semi-diameters of the earth, is to the force by which it may be revolved in the same time, at the distance of 60 semi-diameters, as [SVG 968] to 60: and this force is to the force of gravity with us very nearly as 1 to 60 × 60.",
     "dipende_da": [],
     "figura": {
      "mostra": [],
      "evidenzia": [
       "60 ½ : 60",
       "1 : 60 × 60"
      ]
     }
    },
    {
     "id": "L3-P25-p8",
     "la": "",
     "it": "Perciò la forza media ML sta alla forza di gravità sulla superficie della Terra come 1 × 60 ½ sta a 60 × 60 × 60 × 178 29/40, ossia come 1 a 638092,6.",
     "en": "Therefore the mean force ML is to the force of gravity on the surface of our earth as [SVG 1023] to [SVG 1024] , or as 1 to 638092,6;",
     "dipende_da": [],
     "figura": {
      "mostra": [],
      "evidenzia": [
       "ML : gravità = 1 : 638092,6"
      ]
     },
     "nota": "Ricalcolo: 638092,56."
    },
    {
     "id": "L3-P25-p9",
     "la": "",
     "it": "Da ciò, e dalla proporzione delle linee TM, ML, è data anche la forza TM: e queste sono le forze del Sole da cui sono perturbati i moti della Luna. C.V.T.",
     "en": "whence by the proportion of the lines TM, ML, the force TM is also given; and these are the forces with which the sun disturbs the motions of the moon. Q.E.I.",
     "dipende_da": [],
     "figura": {
      "mostra": [
       "TM"
      ],
      "evidenzia": []
     }
    }
   ]
  },
  {
   "id": "L3-P26",
   "tipo": "Propositio/Problema",
   "titolo": "Prop. XXVI — l’incremento orario dell’area",
   "copertura": [
    "III.G5.20",
    "III.G5.21",
    "III.G5.22",
    "III.G5.23",
    "III.G5.24"
   ],
   "fonti": {
    "la": "",
    "en": "Motte 1846, sezione corrispondente (Book III, Prop. XXVI)"
   },
   "enunciato": {
    "la": "",
    "it": "Trovare l’incremento orario dell’area che la Luna, con un raggio condotto alla Terra, descrive in un’orbita circolare.",
    "en": "To find the horary increment of the area which the moon, by a radius drawn to the earth, describes in a circular orbit."
   },
   "figura_base": {
    "punti": [
     "S",
     "T",
     "P",
     "C",
     "A",
     "D",
     "B",
     "K",
     "L",
     "M",
     "E",
     "G",
     "F",
     "p",
     "k",
     "f",
     "d"
    ],
    "vincoli": [
     "orbita circolare CADB di centro T, C quadratura, A congiunzione",
     "SP ∥ ST (Sole a distanza infinita)",
     "K su CT con PK ⊥ CT; k analogo per p",
     "LM = TP, TM = 3PK; LE ⊥ TP",
     "CG ⊥ CT con CG = CT; TG incontra KP, kp prolungate in F, f",
     "Kd ⊥ TP, d su TP"
    ]
   },
   "dati": {
    "momenti_moto_fisso": [
     11965,
     11915,
     11865
    ],
    "momenti_corretti": [
     11073,
     11023,
     10973
    ],
    "rapporto_sinodico": 1.080853,
    "costante_area": 219.46
   },
   "passi": [
    {
     "id": "L3-P26-p1",
     "la": "",
     "it": "Abbiamo detto che l’area che la Luna descrive con un raggio condotto alla Terra è proporzionale al tempo, se non in quanto il moto lunare è turbato dall’azione del Sole.",
     "en": "We have above shown that the area which the moon describes by a radius drawn to the earth is proportional to the time of description, excepting in so far as the moon's motion is disturbed by the action of the sun;",
     "dipende_da": [],
     "figura": {
      "mostra": [],
      "evidenzia": []
     }
    },
    {
     "id": "L3-P26-p2",
     "la": "",
     "it": "Ci proponiamo di indagare qui la disuguaglianza del momento, ossia dell’incremento orario.",
     "en": "and here we propose to investigate the inequality of the moment, or horary increment of that area or motion so disturbed.",
     "dipende_da": [],
     "figura": {
      "mostra": [],
      "evidenzia": []
     }
    },
    {
     "id": "L3-P26-p3",
     "la": "",
     "it": "Per rendere più facile il calcolo, supponiamo che l’orbita della Luna sia circolare, e trascuriamo tutte le disuguaglianze, eccetto soltanto quella di cui qui si tratta.",
     "en": "To render the calculus more easy, we shall suppose the orbit of the moon to be circular, and neglect all inequalities but that only which is now under consideration;",
     "dipende_da": [],
     "figura": {
      "mostra": [
       "orbita circolare CADB"
      ],
      "evidenzia": []
     }
    },
    {
     "id": "L3-P26-p4",
     "la": "",
     "it": "Per l’enorme distanza del Sole, poniamo anche che le linee SP, ST siano parallele fra loro.",
     "en": "and, because of the immense distance of the sun, we shall farther suppose that the lines SP and ST are parallel.",
     "dipende_da": [],
     "figura": {
      "mostra": [
       "SP ∥ ST"
      ],
      "evidenzia": []
     }
    },
    {
     "id": "L3-P26-p5",
     "la": "",
     "it": "In questo modo la forza LM si ridurrà sempre alla sua quantità media TP, come pure la forza TM alla sua quantità media 3PK.",
     "en": "By this means, the force LM will be always reduced to its mean quantity TP, as well as the force TM to its mean quantity 3PK.",
     "dipende_da": [],
     "figura": {
      "mostra": [
       "LM = TP",
       "TM = 3PK"
      ],
      "evidenzia": []
     }
    },
    {
     "id": "L3-P26-p6",
     "la": "",
     "it": "Queste forze (per il Cor. II delle leggi) compongono la forza TL; e questa forza, se sul raggio TP si abbassa la perpendicolare LE, si scompone nelle forze TE, EL; di queste, TE, agendo sempre lungo il raggio TP, non accelera né ritarda la descrizione dell’area TPC fatta da quel raggio TP; ed EL, agendo lungo la perpendicolare, la accelera o la ritarda quanto accelera o ritarda la Luna.",
     "en": "These forces (by Cor. 2 of the Laws of Motion) compose the force TL; and this force, by letting fall the perpendicular LE upon the radius TP, is resolved into the forces TE, EL; of which the force TE, acting constantly in the direction of the radius TP, neither accelerates nor retards the description of the area TPC made by that radius TP; but EL, acting on the radius TP in a perpendicular direction, accelerates or retards the description of the area in proportion as it accelerates or retards the moon.",
     "dipende_da": [
      "Leggi, Cor. II"
     ],
     "figura": {
      "mostra": [
       "TL",
       "LE ⊥ TP",
       "TE",
       "EL"
      ],
      "evidenzia": [
       "TE radiale: non cambia la descrizione dell’area",
       "EL trasversale: la accelera o la ritarda"
      ]
     }
    },
    {
     "id": "L3-P26-p7",
     "la": "",
     "it": "Quell’accelerazione della Luna, fatta nei singoli momenti di tempo nel suo passaggio dalla quadratura C alla congiunzione A, è come la stessa forza che accelera, EL, cioè come 3PK × TK/TP.",
     "en": "That acceleration of the moon, in its passage from the quadrature C to the conjunction A, is in every moment of time as the generating accelerative force EL, that is, as [SVG 1025] .",
     "dipende_da": [],
     "figura": {
      "mostra": [
       "C",
       "A"
      ],
      "evidenzia": [
       "EL = 3PK × TK/TP"
      ]
     },
     "nota": "Formula appiattita nella trascrizione («3⁢PK×TKTP»), letta 3PK × TK/TP come in Motte (SVG 1025)."
    },
    {
     "id": "L3-P26-p8",
     "la": "",
     "it": "Si rappresenti il tempo con il moto medio lunare, oppure (il che torna quasi allo stesso) con l’angolo CTP, o anche con l’arco CP.",
     "en": "Let the time be represented by the mean motion of the moon, or (which comes to the same thing) by the angle CTP, or even by the arc CP.",
     "dipende_da": [],
     "figura": {
      "mostra": [
       "angolo CTP",
       "arco CP"
      ],
      "evidenzia": [
       "tempo rappresentato dall’arco CP"
      ]
     }
    },
    {
     "id": "L3-P26-p9",
     "la": "",
     "it": "Su CT si innalzi la normale CG, uguale a CT.",
     "en": "At right angles upon CT erect CG equal to CT;",
     "dipende_da": [],
     "figura": {
      "mostra": [
       "CG ⊥ CT, CG = CT"
      ],
      "evidenzia": []
     }
    },
    {
     "id": "L3-P26-p10",
     "la": "",
     "it": "E, diviso l’arco quadrantale AC in innumerevoli particelle uguali Pp ecc., con le quali si possono rappresentare altrettante particelle uguali di tempo, e condotta pk perpendicolare a CT, si congiunga TG, che incontri KP, kp prolungate in F e f: FK sarà uguale a TK, e Kk starà a PK come Pp sta a Tp, cioè in un rapporto dato; e perciò FK × Kk, ossia l’area FKkf, sarà come 3PK × TK/TP, cioè come EL; e, componendo, l’area totale GCKF sarà come la somma di tutte le forze EL impresse sulla Luna nel tempo totale CP, e quindi anche come la velocità generata da questa somma, cioè come l’accelerazione della descrizione dell’area CTP, ossia come l’incremento del momento.",
     "en": "and, supposing the quadrantal arc AC to be divided into an infinite number of equal parts Pp, &c., these parts may represent the like infinite number of the equal parts of time. Let fall pk perpendicular on CT, and draw TG meeting with KP, kp produced in F and f; then will FK be equal to TK, and Kk be to PK as Pp to Tp, that is, in a given proportion; and therefore FK × Kk, or the area FKkf, will be as [SVG 1025] , that is, as EL; and compounding, the whole area GCKF will be as the sum of all the forces EL impressed upon the moon in the whole time CP; and therefore also as the velocity generated by that sum, that is, as the acceleration of the description of the area CTP, or as the increment of the moment thereof.",
     "dipende_da": [],
     "figura": {
      "mostra": [
       "particelle Pp",
       "pk ⊥ CT",
       "TG",
       "F, f"
      ],
      "evidenzia": [
       "FK = TK",
       "Kk : PK = Pp : Tp",
       "area FKkf come EL",
       "area GCKF come l’incremento del momento"
      ]
     },
     "nota": "La trascrizione ha «æuales» per «æquales»: refuso probabile."
    },
    {
     "id": "L3-P26-p11",
     "la": "",
     "it": "La forza con cui la Luna potrebbe ruotare attorno alla Terra in quiete alla distanza TP, nel suo tempo periodico CADB di 27 giorni 7 ore 43 minuti, farebbe sì che un corpo, cadendo nel tempo CT, descrivesse la lunghezza ½ CT e acquistasse nello stesso tempo una velocità uguale alla velocità con cui la Luna si muove nella sua orbita.",
     "en": "The force by which the moon may in its periodic time CADB of 27d. 7h. 43' be retained revolving about the earth in rest at the distance TP, would cause a body falling in the time CT to describe the length [SVG 1026] , and at the same time to acquire a velocity equal to that with which the moon is moved in its orbit.",
     "dipende_da": [],
     "figura": {
      "mostra": [],
      "evidenzia": [
       "caduta ½ CT nel tempo CT",
       "velocità acquistata = velocità della Luna"
      ]
     },
     "nota": "Lettura «12⁢CT» = ½ CT (SVG 1026)."
    },
    {
     "id": "L3-P26-p12",
     "la": "",
     "it": "Ciò risulta dal Cor. 9 della Prop. IV del Libro I.",
     "en": "This appears from Cor. 9, Prop. IV., Book I.",
     "dipende_da": [
      "Libro I, Prop. IV, Cor. 9"
     ],
     "figura": {
      "mostra": [],
      "evidenzia": []
     }
    },
    {
     "id": "L3-P26-p13",
     "la": "",
     "it": "Poiché poi la perpendicolare Kd abbassata su TP è la terza parte di EL, e negli ottanti è la metà di TP, ossia di ML, la forza EL negli ottanti, dove è massima, supererà la forza ML nel rapporto di 3 a 2; e perciò starà alla forza con cui la Luna, nel suo tempo periodico, potrebbe ruotare attorno alla Terra in quiete come 100 sta a 2/3 × 17872 ½, ossia a 11915; e nel tempo CT dovrebbe generare una velocità che sarebbe i 100/11915 della velocità lunare, mentre nel tempo CPA genererebbe una velocità maggiore nel rapporto di CA a CT, ossia a TP.",
     "en": "But since Kd, drawn perpendicular on TP, is but a third part of EL, and equal to the half of TP, or ML, in the octants, the force EL in the octants, where it is greatest, will exceed the force ML in the proportion of 3 to 2; and therefore will be to that force by which the moon in its periodic time may be retained revolving about the earth at rest as 100 to [SVG 1027] , or 11915; and in the time CT will generate a velocity equal to [SVG 1028] parts of the velocity of the moon; but in the time CPA will generate a greater velocity in the proportion of CA to CT or TP.",
     "dipende_da": [],
     "figura": {
      "mostra": [
       "Kd ⊥ TP"
      ],
      "evidenzia": [
       "Kd = EL/3",
       "Kd = TP/2 negli ottanti",
       "EL massima : ML = 3 : 2",
       "100 : 11915"
      ]
     },
     "nota": "Letture: «23×17872⁤12» = 2/3 × 17872 ½; «10011915» = 100/11915 (SVG 1027, 1028)."
    },
    {
     "id": "L3-P26-p14",
     "la": "",
     "it": "Si rappresenti la forza massima EL negli ottanti con l’area FK × Kk, uguale al rettangolo ½ TP × Pp.",
     "en": "Let the greatest force EL in the octants be represented by the area FK × Kk, or by the rectangle [SVG 1029] , which is equal thereto;",
     "dipende_da": [],
     "figura": {
      "mostra": [
       "rettangolo ½ TP × Pp"
      ],
      "evidenzia": []
     },
     "nota": "Lettura «12⁢TP×Pp» = ½ TP × Pp (SVG 1029)."
    },
    {
     "id": "L3-P26-p15",
     "la": "",
     "it": "E la velocità che la forza massima potrebbe generare in un tempo qualsiasi CP starà alla velocità che tutte le forze minori EL generano nello stesso tempo come il rettangolo ½ TP × CP sta all’area KCGF; nel tempo totale CPA, invece, le velocità generate staranno fra loro come il rettangolo ½ TP × CA e il triangolo TCG, ossia come l’arco quadrantale CA sta al raggio TP.",
     "en": "and the velocity which that greatest force can generate in any time CP will be to the velocity which any other lesser force EL can generate in the same time as the rectangle [SVG 1030] to the area KCGF; but the velocities generated in the whole time CPA will be one to the other as the rectangle [SVG 1031] to the triangle TCG, or as the quadrantal arc CA to the radius TP;",
     "dipende_da": [],
     "figura": {
      "mostra": [
       "area KCGF",
       "triangolo TCG"
      ],
      "evidenzia": [
       "½ TP × CP : KCGF",
       "½ TP × CA : TCG = CA : TP"
      ]
     }
    },
    {
     "id": "L3-P26-p16",
     "la": "",
     "it": "Perciò (per la Prop. IX del Libro V degli *Elementi*) quest’ultima velocità, generata nel tempo totale, sarà i 100/11915 della velocità della Luna.",
     "en": "and therefore the latter velocity generated in the whole time will be [SVG 1028] parts of the velocity of the moon.",
     "dipende_da": [
      "Euclide, Elementi, Libro V, Prop. IX"
     ],
     "figura": {
      "mostra": [],
      "evidenzia": [
       "velocità generata in CPA = 100/11915 della velocità lunare"
      ]
     },
     "nota": "Motte omette il rimando a Euclide. Ricalcolo per integrazione: 100/11915,0 (nota N6)."
    },
    {
     "id": "L3-P26-p17",
     "la": "",
     "it": "A questa velocità della Luna, che è analoga al momento medio dell’area, si aggiunga e si tolga la metà dell’altra velocità: se il momento medio si rappresenta con il numero 11915, la somma 11915 + 50, ossia 11965, darà il momento massimo dell’area nella sizigia A, e la differenza 11915 − 50, ossia 11865, il suo momento minimo nelle quadrature.",
     "en": "To this velocity of the moon, which is proportional to the mean moment of the area (supposing this mean moment to be represented by the number 11915), we add and subtract the half of the other velocity; the sum 11915 + 50, or 11965, will represent the greatest moment of the area in the syzygy A; and the difference 11915 - 50, or 11865, the least moment thereof in the quadratures.",
     "dipende_da": [],
     "figura": {
      "mostra": [
       "A"
      ],
      "evidenzia": [
       "11965 nella sizigia",
       "11865 nelle quadrature"
      ]
     }
    },
    {
     "id": "L3-P26-p18",
     "la": "",
     "it": "Le aree descritte in tempi uguali nelle sizigie e nelle quadrature stanno dunque fra loro come 11965 a 11865.",
     "en": "Therefore the areas which in equal times are described in the syzygies and quadratures are one to the other as 11965 to 11865.",
     "dipende_da": [],
     "figura": {
      "mostra": [],
      "evidenzia": [
       "11965 : 11865"
      ]
     }
    },
    {
     "id": "L3-P26-p19",
     "la": "",
     "it": "Al momento minimo 11865 si aggiunga un momento che stia alla differenza dei momenti, 100, come il trapezio FKCG sta al triangolo TCG (oppure, il che è lo stesso, come il quadrato del seno PK sta al quadrato del raggio TP, cioè come Pd sta a TP): la somma darà il momento dell’area quando la Luna si trova in un luogo intermedio qualsiasi P.",
     "en": "And if to the least moment 11865 we add a moment which shall be to 100, the difference of the two former moments, as the trapezium FKCG to the triangle TCG, or, which comes to the same thing, as the square of the sine PK to the square of the radius TP (that is, as Pd to TP), the sum will represent the moment of the area when the moon is in any intermediate place P.",
     "dipende_da": [],
     "figura": {
      "mostra": [
       "trapezio FKCG",
       "Pd"
      ],
      "evidenzia": [
       "FKCG : TCG = PK² : TP² = Pd : TP"
      ]
     }
    },
    {
     "id": "L3-P26-p20",
     "la": "",
     "it": "Tutto ciò vale nell’ipotesi che il Sole e la Terra siano in quiete e che la Luna compia la sua rivoluzione nel tempo sinodico di 27 giorni 7 ore 43 minuti.",
     "en": "But these things take place only in the hypothesis that the sun and the earth are at rest, and that the synodical revolution of the moon is finished in 27d. 7h. 43'.",
     "dipende_da": [],
     "figura": {
      "mostra": [],
      "evidenzia": []
     }
    },
    {
     "id": "L3-P26-p21",
     "la": "",
     "it": "Poiché però il periodo sinodico lunare è in realtà di 29 giorni 12 ore e 44 minuti, gli incrementi dei momenti devono essere aumentati nel rapporto del tempo, cioè nel rapporto di 1080853 a 1000000.",
     "en": "But since the moon's synodical period is really 29d. 12h. 44', the increments of the moments must be enlarged in the same proportion as the time is, that is, in the proportion of 1080853 to 1000000.",
     "dipende_da": [],
     "figura": {
      "mostra": [],
      "evidenzia": [
       "29g 12h 44m : 27g 7h 43m = 1080853 : 1000000"
      ]
     },
     "nota": "Ricalcolo: 1,0808530."
    },
    {
     "id": "L3-P26-p22",
     "la": "",
     "it": "In questo modo l’incremento totale, che era i 100/11915 del momento medio, diventerà ora i 100/11023 dello stesso.",
     "en": "Upon which account, the whole increment, which was [SVG 1028] parts of the mean moment, will now become [SVG 1032] parts thereof;",
     "dipende_da": [],
     "figura": {
      "mostra": [],
      "evidenzia": [
       "100/11023"
      ]
     },
     "nota": "Lettura «10011023» = 100/11023 (SVG 1032). 11915 : 1,080853 = 11023,7: Newton scrive 11023 (nota N6)."
    },
    {
     "id": "L3-P26-p23",
     "la": "",
     "it": "Perciò il momento dell’area nella quadratura della Luna starà al suo momento nella sizigia come 11023 − 50 sta a 11023 + 50, ossia come 10973 a 11073, e al suo momento quando la Luna si trova in un altro luogo intermedio qualsiasi P come 10973 sta a 10973 + Pd, posto naturalmente TP uguale a 100.",
     "en": "and therefore the moment of the area in the quadrature of the moon will be to the moment thereof in the syzygy as 11023 - 50 to 11023 + 50; or as 10973 to 11073; and to the moment thereof, when the moon is in any intermediate place P, as 10973 to 10973 + Pd; that is, supposing TP = 100.",
     "dipende_da": [],
     "figura": {
      "mostra": [],
      "evidenzia": [
       "10973 : 11073",
       "10973 : 10973 + Pd con TP = 100"
      ]
     }
    },
    {
     "id": "L3-P26-p24",
     "la": "",
     "it": "L’area, dunque, che la Luna descrive con un raggio condotto alla Terra in singole particelle di tempo uguali è, con ottima approssimazione, come la somma del numero 219,46 e del seno verso del doppio della distanza della Luna dalla quadratura più vicina, in un cerchio il cui raggio è l’unità.",
     "en": "The area, therefore, which the moon, by a radius drawn to the earth, describes in the several little equal parts of time, is nearly as the sum of the number 219,46, and the versed sine of the double distance of the moon from the nearest quadrature, considered in a circle which hath unity for its radius.",
     "dipende_da": [],
     "figura": {
      "mostra": [],
      "evidenzia": [
       "area come 219,46 + seno verso del doppio della distanza dalla quadratura"
      ]
     },
     "nota": "10973/50 = 219,46; 50 × seno verso (2θ) = 100 sin²θ = Pd (nota N6)."
    },
    {
     "id": "L3-P26-p25",
     "la": "",
     "it": "Così stanno le cose quando la variazione negli ottanti è di grandezza media.",
     "en": "Thus it is when the variation in the octants is in its mean quantity.",
     "dipende_da": [],
     "figura": {
      "mostra": [],
      "evidenzia": []
     }
    },
    {
     "id": "L3-P26-p26",
     "la": "",
     "it": "Se invece lì la variazione è maggiore o minore, quel seno verso deve essere aumentato o diminuito nello stesso rapporto.",
     "en": "But if the variation there is greater or less, that versed sine must be augmented or diminished in the same proportion.",
     "dipende_da": [],
     "figura": {
      "mostra": [],
      "evidenzia": []
     }
    }
   ]
  },
  {
   "id": "L3-P27",
   "tipo": "Propositio/Problema",
   "titolo": "Prop. XXVII — la distanza della Luna dal moto orario",
   "copertura": [
    "III.G5.25",
    "III.G5.26",
    "III.G5.27",
    "III.G5.28"
   ],
   "fonti": {
    "la": "",
    "en": "Motte 1846, sezione corrispondente (Book III, Prop. XXVII)"
   },
   "enunciato": {
    "la": "",
    "it": "Trovare dal moto orario della Luna la sua distanza dalla Terra.",
    "en": "From the horary motion of the moon to find its distance from the earth."
   },
   "nota": "Un solo passo (la soluzione). I Cor. 1 e 2 (III.G5.27–III.G5.28) non hanno dimostrazione propria e non entrano come passi.",
   "passi": [
    {
     "id": "L3-P27-p1",
     "la": "",
     "it": "L’area che la Luna descrive in singoli momenti di tempo con un raggio condotto alla Terra è come il moto orario della Luna e il quadrato della distanza della Luna dalla Terra considerati congiuntamente; e perciò la distanza della Luna dalla Terra sta nel rapporto composto dal rapporto subduplicato dell’area, direttamente, e dal rapporto subduplicato del moto orario, inversamente. C.V.T.",
     "en": "The area which the moon, by a radius drawn to the earth, describes in every moment of time, is as the horary motion of the moon and the square of the distance of the moon from the earth conjunctly. And therefore the distance of the moon from the earth is in a proportion compounded of the subduplicate proportion of the area directly, and the subduplicate proportion of the horary motion inversely. Q.E.I.",
     "dipende_da": [],
     "figura": {
      "mostra": [],
      "evidenzia": [
       "area ∝ moto orario × distanza²",
       "distanza ∝ √area : √moto orario"
      ]
     }
    }
   ]
  },
  {
   "id": "L3-P28",
   "tipo": "Propositio/Problema",
   "titolo": "Prop. XXVIII — i diametri dell’orbita lunare senza eccentricità",
   "copertura": [
    "III.G5.29",
    "III.G5.30",
    "III.G5.31",
    "III.G5.32"
   ],
   "fonti": {
    "la": "",
    "en": "Motte 1846, sezione corrispondente (Book III, Prop. XXVIII)"
   },
   "enunciato": {
    "la": "",
    "it": "Trovare i diametri dell’orbita in cui la Luna, senza eccentricità, dovrebbe muoversi.",
    "en": "To find the diameters of the orbit, in which, without eccentricity, the moon would move."
   },
   "figura_base": {
    "punti": [
     "D",
     "B",
     "C",
     "A",
     "T",
     "P",
     "p",
     "a"
    ],
    "vincoli": [
     "ellisse DBCA di centro T",
     "DC asse maggiore fra le quadrature, AB asse minore fra le sizigie",
     "p con Tp = TP e CTp : CTP = 29g 12h 44′ : 27g 7h 43′",
     "a con Ta = TA e CTa nello stesso rapporto all’angolo retto CTA",
     "per le forze: figura della Prop. XXV (p. 428)"
    ]
   },
   "dati": {
    "mu": 0.16824,
    "x": 0.00719,
    "CT": 1.00719,
    "AT": 0.99281,
    "verifica_x": 0.00719
   },
   "passi": [
    {
     "id": "L3-P28-p1",
     "la": "",
     "it": "La curvatura della traiettoria che un mobile descrive, se è attratto lungo la perpendicolare a quella traiettoria, è come l’attrazione direttamente e il quadrato della velocità inversamente.",
     "en": "The curvature of the orbit which a body describes, if attracted in lines perpendicular to the orbit, is as the force of attraction directly, and the square of the velocity inversely.",
     "dipende_da": [],
     "figura": {
      "mostra": [],
      "evidenzia": [
       "curvatura ∝ attrazione : velocità²"
      ]
     }
    },
    {
     "id": "L3-P28-p2",
     "la": "",
     "it": "Pongo che le curvature delle linee stiano fra loro nella proporzione ultima dei seni o delle tangenti degli angoli di contatto che appartengono a raggi uguali, quando quei raggi diminuiscono all’infinito.",
     "en": "I estimate the curvatures of lines compared one with another according to the evanescent proportion of the sines or tangents of their angles of contact to equal radii, supposing those radii to be infinitely diminished.",
     "dipende_da": [],
     "figura": {
      "mostra": [],
      "evidenzia": [
       "curvature come rapporto ultimo degli angoli di contatto"
      ]
     }
    },
    {
     "id": "L3-P28-p3",
     "la": "",
     "it": "L’attrazione della Luna verso la Terra nelle sizigie è poi l’eccesso della sua gravità verso la Terra sulla forza solare 2PK (vedi la figura di p. 428), cioè sulla quantità di cui la gravità acceleratrice della Luna verso il Sole supera la gravità acceleratrice della Terra verso il Sole, o ne è superata.",
     "en": "But the attraction of the moon towards the earth in the syzygies is the excess of its gravity towards the earth above the force of the sun 2PK (see Fig. Prop. XXV), by which force the accelerative gravity of the moon towards the sun exceeds the accelerative gravity of the earth towards the sun, or is exceeded by it.",
     "dipende_da": [
      "Prop. XXV (figura di p. 428)"
     ],
     "figura": {
      "mostra": [],
      "evidenzia": [
       "attrazione nelle sizigie = gravità − 2PK"
      ]
     },
     "nota": "Motte: «see Fig. Prop. XXV» per *vide fig. pag. 428*."
    },
    {
     "id": "L3-P28-p4",
     "la": "",
     "it": "Nelle quadrature, invece, quell’attrazione è la somma della gravità della Luna verso la Terra e della forza solare KT, con cui la Luna è tratta verso la Terra.",
     "en": "But in the quadratures that attraction is the sum of the gravity of the moon towards the earth, and the sun's force KT, by which the moon is attracted towards the earth.",
     "dipende_da": [],
     "figura": {
      "mostra": [],
      "evidenzia": [
       "attrazione nelle quadrature = gravità + KT"
      ]
     }
    },
    {
     "id": "L3-P28-p5",
     "la": "",
     "it": "E queste attrazioni, se (AT + CT)/2 si chiama N, sono con ottima approssimazione come 178725/AT² − 2000/(CT × N) e 178725/CT² + 1000/(AT × N); ossia come 178725N × CT² − 2000AT² × CT e 178725N × AT² + 1000CT² × AT.",
     "en": "And these attractions, putting N for [SVG 1033] , are nearly as [SVG 1034] and [SVG 1035] , or as 178725N × CT2 - 2000AT2 × CT, and 178725N × AT2 + 1000CT2 × AT.",
     "dipende_da": [],
     "figura": {
      "mostra": [],
      "evidenzia": [
       "N = (AT + CT)/2"
      ]
     },
     "nota": "Formule appiattite nella trascrizione: «AT+CT2» = (AT + CT)/2; «178725ATq-2000CT×N» = 178725/AT² − 2000/(CT × N), come in Motte (SVG 1033–1035). Le seconde forme si ottengono moltiplicando per AT² × CT² × N."
    },
    {
     "id": "L3-P28-p6",
     "la": "",
     "it": "Se infatti la gravità acceleratrice della Luna verso la Terra si rappresenta con il numero 178725, la forza media ML, che nelle quadrature è PT o TK e trae la Luna verso la Terra, sarà 1000, e la forza media TM nelle sizigie sarà 3000; e se da questa si sottrae la forza media ML, resterà la forza 2000, con cui la Luna nelle sizigie è allontanata dalla Terra, e che già sopra ho chiamato 2PK.",
     "en": "For if the accelerative gravity of the moon towards the earth be represented by the number 178725, the mean force ML, which in the quadratures is PT or TK, and draws the moon towards the earth, will be 1000, and the mean force TM in the syzygies will be 3000; from which, if we subtract the mean force ML, there will remain 2000, the force by which the moon in the syzygies is drawn from the earth, and which we above called 2PK.",
     "dipende_da": [],
     "figura": {
      "mostra": [],
      "evidenzia": [
       "178725 : 1000 : 3000 : 2000"
      ]
     }
    },
    {
     "id": "L3-P28-p7",
     "la": "",
     "it": "La velocità della Luna nelle sizigie A e B sta poi alla sua velocità nelle quadrature C e D come CT sta ad AT e il momento dell’area che la Luna descrive con un raggio condotto alla Terra nelle sizigie sta al momento della stessa area nelle quadrature, considerati congiuntamente; cioè come 11073CT sta a 10973AT.",
     "en": "But the velocity of the moon in the syzygies A and B is to its velocity in the quadratures C and D as CT to AT, and the moment of the area, which the moon by a radius drawn to the earth describes in the syzygies, to the moment of that area described in the quadratures conjunctly; that is, as 11073CT to 10973AT.",
     "dipende_da": [],
     "figura": {
      "mostra": [],
      "evidenzia": [
       "v sizigie : v quadrature = 11073CT : 10973AT"
      ]
     },
     "nota": "I momenti 11073 e 10973 vengono dalla Prop. XXVI, che qui non è citata."
    },
    {
     "id": "L3-P28-p8",
     "la": "",
     "it": "Si prenda questo rapporto due volte inversamente e il rapporto precedente una volta direttamente: la curvatura dell’orbita lunare nelle sizigie starà alla sua curvatura nelle quadrature come 120406729 × 178725AT² × CT² × N − 120406729 × 2000AT⁴ × CT sta a 122611329 × 178725AT² × CT² × N + 122611329 × 1000CT⁴ × AT, cioè come 2151969AT × CT × N − 24081AT³ sta a 2191371AT × CT × N + 12261CT³.",
     "en": "Take this ratio twice inversely, and the former ratio once directly, and the curvature of the orb of the moon in the syzygies will be to the curvature thereof in the quadratures as 120406729 × 178725AT2 × CT2 × N - 120406729 × 2000AT4 × CT to 122611329 × 178725AT2 × CT2 × N + 122611329 × 1000CT4 × AT, that is, as 2151969AT × CT × N - 24081AT3 to 2191371AT × CT × N + 12261CT3.",
     "dipende_da": [],
     "figura": {
      "mostra": [],
      "evidenzia": [
       "10973² = 120406729",
       "11073² = 122611329"
      ]
     },
     "nota": "Prodotti e riduzioni ricontrollati (nota N8)."
    },
    {
     "id": "L3-P28-p9",
     "la": "",
     "it": "Poiché la figura dell’orbita lunare è ignota, assumiamo al suo posto l’ellisse DBCA, nel cui centro T sia collocata la Terra, e il cui asse maggiore DC stia fra le quadrature, il minore AB fra le sizigie.",
     "en": "Because the figure of the moon's orbit is unknown, let us, in its stead, assume the ellipsis DBCA, in the centre of which we suppose the earth to be situated, and the greater axis DC to lie between the quadratures as the lesser AB between the syzygies.",
     "dipende_da": [],
     "figura": {
      "mostra": [
       "ellisse DBCA",
       "T al centro",
       "DC asse maggiore",
       "AB asse minore"
      ],
      "evidenzia": []
     }
    },
    {
     "id": "L3-P28-p10",
     "la": "",
     "it": "Poiché però il piano di questa ellisse ruota attorno alla Terra con moto angolare, e la traiettoria di cui consideriamo la curvatura deve essere descritta in un piano del tutto privo di ogni moto angolare, si dovrà considerare la figura che la Luna, ruotando in quell’ellisse, descrive in questo piano, cioè la figura Cpa, i cui singoli punti p si trovano prendendo un punto qualsiasi P sull’ellisse, che rappresenti il luogo della Luna, e conducendo Tp uguale a TP, con la condizione che l’angolo PTp sia uguale al moto apparente del Sole compiuto dal tempo della quadratura C; oppure (il che torna quasi allo stesso) che l’angolo CTp stia all’angolo CTP come il tempo della rivoluzione sinodica lunare sta al tempo della rivoluzione periodica, ossia come 29g 12h 44′ a 27g 7h 43′.",
     "en": "But since the plane of this ellipsis is revolved about the earth by an angular motion, and the orbit, whose curvature we now examine, should be described in a plane void of such motion we are to consider the figure which the moon, while it is revolved in that ellipsis, describes in this plane, that is to say, the figure Cpa, the several points p of which are found by assuming any point P in the ellipsis, which may represent the place of the moon, and drawing Tp equal to TP in such manner that the angle PTp may be equal to the apparent motion of the sun from the time of the last quadrature in C; or (which comes to the same thing) that the angle CTp may be to the angle CTP as the time of the synodic revolution of the moon to the time of the periodic revolution thereof, or as 29d. 12h. 44' to 27d. 7h. 43'.",
     "dipende_da": [],
     "figura": {
      "mostra": [
       "P sull’ellisse",
       "p con Tp = TP",
       "figura Cpa"
      ],
      "evidenzia": [
       "PTp = moto apparente del Sole",
       "CTp : CTP = 29g 12h 44′ : 27g 7h 43′"
      ]
     }
    },
    {
     "id": "L3-P28-p11",
     "la": "",
     "it": "Si prenda dunque l’angolo CTa nello stesso rapporto all’angolo retto CTA, e la lunghezza Ta sia uguale alla lunghezza TA: a sarà l’apside inferiore e C l’apside superiore di questa orbita Cpa.",
     "en": "If, therefore, in this proportion we take the angle CTa to the right angle CTA, and make Ta of equal length with TA, we shall have a the lower and C the upper apsis of this orbit Cpa.",
     "dipende_da": [],
     "figura": {
      "mostra": [
       "a con Ta = TA",
       "angolo CTa"
      ],
      "evidenzia": [
       "a apside inferiore",
       "C apside superiore"
      ]
     }
    },
    {
     "id": "L3-P28-p12",
     "la": "",
     "it": "Facendo i conti, poi, trovo che la differenza fra la curvatura dell’orbita Cpa nel vertice a e la curvatura del cerchio descritto con centro T e raggio TA sta alla differenza fra la curvatura dell’ellisse nel vertice A e la curvatura dello stesso cerchio in rapporto duplicato dell’angolo CTP all’angolo CTp; che la curvatura dell’ellisse in A sta alla curvatura di quel cerchio in rapporto duplicato di TA a TC; che la curvatura di quel cerchio sta alla curvatura del cerchio descritto con centro T e raggio TC come TC sta a TA; che la curvatura di quest’ultimo sta alla curvatura dell’ellisse in C in rapporto duplicato di TA a TC; e che la differenza fra la curvatura dell’ellisse nel vertice C e la curvatura dell’ultimo cerchio sta alla differenza fra la curvatura della figura [Cpa] nel vertice C e la curvatura dello stesso cerchio in rapporto duplicato dell’angolo CTp all’angolo CTP.",
     "en": "But, by computation, I find that the difference betwixt the curvature of this orbit Cpa at the vertex a, and the curvature of a circle described about the centre T with the interval TA, is to the difference between the curvature of the ellipsis at the vertex A, and the curvature of the same circle, in the duplicate proportion of the angle CTP to the angle CTp; and that the curvature of the ellipsis in A is to the curvature of that circle in the duplicate proportion of TA to TC; and the curvature of that circle to the curvature of a circle described about the centre T with the interval TC as TC to TA; but that the curvature of this last arch is to the curvature of the ellipsis in C in the duplicate proportion of TA to TC; and that the difference betwixt the curvature of the ellipsis in the vertex C, and the curvature of this last circle, is to the difference betwixt the curvature of the figure Cpa, at the vertex C, and the curvature of this same last circle, in the duplicate proportion of the angle CTp to the angle CTP;",
     "dipende_da": [],
     "figura": {
      "mostra": [
       "cerchio di centro T e raggio TA",
       "cerchio di centro T e raggio TC"
      ],
      "evidenzia": [
       "cinque rapporti fra curvature"
      ]
     },
     "nota": "La trascrizione ha «figuræ Tpa in vertice C»: refuso probabile per Cpa (Motte «figure Cpa»)."
    },
    {
     "id": "L3-P28-p13",
     "la": "",
     "it": "Questi rapporti si ricavano facilmente dai seni degli angoli di contatto e delle differenze degli angoli.",
     "en": "all which proportions are easily drawn from the sines of the angles of contact, and of the differences of those angles.",
     "dipende_da": [],
     "figura": {
      "mostra": [],
      "evidenzia": []
     }
    },
    {
     "id": "L3-P28-p14",
     "la": "",
     "it": "Confrontati poi questi rapporti fra loro, risulta che la curvatura della figura Cpa in a sta alla sua curvatura in C come AT³ + 16824/100000 CT² × AT sta a CT³ + 16824/100000 AT² × CT.",
     "en": "But, by comparing those proportions together, we find the curvature of the figure Cpa at a to be to its curvature at C as [SVG 1036] to [SVG 1037] ;",
     "dipende_da": [],
     "figura": {
      "mostra": [],
      "evidenzia": [
       "curv. in a : curv. in C = AT³ + 0,16824 CT² × AT : CT³ + 0,16824 AT² × CT"
      ]
     },
     "nota": "Il latino ha «+» nel primo termine, Motte 1846 (SVG 1036) «−». Il «+» è giusto: lo dà la derivazione dei cinque rapporti, e solo con il «+» l’equazione seguente ha la radice 0,00719 (nota N8)."
    },
    {
     "id": "L3-P28-p15",
     "la": "",
     "it": "Qui il numero 16824/100000 indica la differenza dei quadrati degli angoli CTP e CTp divisa per il quadrato dell’angolo minore CTP, ossia (il che è lo stesso) la differenza dei quadrati dei tempi 27g 7h 43′ e 29g 12h 44′ divisa per il quadrato del tempo 27g 7h 43′.",
     "en": "where the number [SVG 1038] represents the difference of the squares of the angles CTP and CTp, applied to the square of the lesser angle CTP; or (which is all one) the difference of the squares of the times 27d. 7h. 43', and 29d. 12h. 44', applied to the square of the time 27d. 7h. 43'.",
     "dipende_da": [],
     "figura": {
      "mostra": [],
      "evidenzia": [
       "16824/100000 = (CTp² − CTP²) : CTP²"
      ]
     },
     "nota": "Ricalcolo: 0,168243."
    },
    {
     "id": "L3-P28-p16",
     "la": "",
     "it": "Poiché dunque a indica la sizigia della Luna e C la sua quadratura, la proporzione ora trovata deve essere la stessa della proporzione, trovata sopra, fra la curvatura dell’orbita della Luna nelle sizigie e la sua curvatura nelle quadrature.",
     "en": "Since, therefore, a represents the syzygy of the moon, and C its quadrature, the proportion now found must be the same with that proportion of the curvature of the moon's orb in the syzygies to the curvature thereof in the quadratures, which we found above.",
     "dipende_da": [],
     "figura": {
      "mostra": [],
      "evidenzia": []
     }
    },
    {
     "id": "L3-P28-p17",
     "la": "",
     "it": "Perciò, per trovare la proporzione di CT ad AT, moltiplico fra loro gli estremi e i medi.",
     "en": "Therefore, in order to find the proportion of CT to AT, let us multiply the extremes and the means,",
     "dipende_da": [],
     "figura": {
      "mostra": [],
      "evidenzia": []
     }
    },
    {
     "id": "L3-P28-p18",
     "la": "",
     "it": "E i termini che ne risultano, divisi per AT × CT, diventano 2062,79CT⁴ − 2151969N × CT³ + 368676N × AT × CT² + 36342AT² × CT² − 362047N × AT² × CT + 2191371N × AT³ + 4051,4AT⁴ = 0.",
     "en": "and the terms which come out, applied to AT × CT, become 2062,79CT4 - 2151969N × CT3 + 368676N × AT × CT2 + 36342AT2 × CT2 - 362047N × AT2 × CT + 2191371N × AT3 + 4051,4AT4 = 0.",
     "dipende_da": [],
     "figura": {
      "mostra": [],
      "evidenzia": [
       "equazione di quarto grado in AT, CT, N"
      ]
     },
     "nota": "Coefficienti ricalcolati: coincidono con quelli di Newton a meno di un segno comune (nota N8)."
    },
    {
     "id": "L3-P28-p19",
     "la": "",
     "it": "Qui, al posto della semisomma N dei termini AT e CT scrivo 1, e ponendo x per la loro semidifferenza si ha CT = 1 + x e AT = 1 − x; sostituiti questi valori nell’equazione e risolta l’equazione che ne risulta, si ottiene x uguale a 0,00719; e di qui il semidiametro CT diventa 1,00719 e il semidiametro AT 0,99281, numeri che stanno con ottima approssimazione come 70 1/24 e 69 1/24.",
     "en": "Now if for the half sum N of the terms AT and CT we put 1, and x for their half difference, then CT will be = 1 + x, and AT = 1 - x. And substituting those values in the equation, after resolving thereof, we shall find x = 0,00719; and from thence the semi-diameter CT = 1,00719, and the semi-diameter AT = 0,99281, which numbers are nearly as [SVG 1039] , and [SVG 1040] .",
     "dipende_da": [],
     "figura": {
      "mostra": [],
      "evidenzia": [
       "x = 0,00719",
       "CT = 1,00719",
       "AT = 0,99281"
      ]
     },
     "nota": "Radice ricalcolata: 0,0071900."
    },
    {
     "id": "L3-P28-p20",
     "la": "",
     "it": "La distanza della Luna dalla Terra nelle sizigie sta dunque alla sua distanza nelle quadrature (messa da parte, s’intende, la considerazione dell’eccentricità) come 69 1/24 sta a 70 1/24, o, in numeri tondi, come 69 a 70.",
     "en": "Therefore the moon's distance from the earth in the syzygies is to its distance in the quadratures (setting aside the consideration of eccentricity) as [SVG 1040] to [SVG 1039] ; in round numbers, as 69 to 70.",
     "dipende_da": [],
     "figura": {
      "mostra": [],
      "evidenzia": [
       "AT : CT = 69 1/24 : 70 1/24, circa 69 : 70"
      ]
     }
    }
   ]
  },
  {
   "id": "L3-P29",
   "tipo": "Propositio/Problema",
   "titolo": "Prop. XXIX — la variazione della Luna",
   "copertura": [
    "III.G5.33",
    "III.G5.34",
    "III.G5.35",
    "III.G5.36"
   ],
   "fonti": {
    "la": "",
    "en": "Motte 1846, sezione corrispondente (Book III, Prop. XXIX)"
   },
   "enunciato": {
    "la": "",
    "it": "Trovare la variazione della Luna.",
    "en": "To find the variation of the moon."
   },
   "figura_base": {
    "punti": [
     "D",
     "B",
     "C",
     "A",
     "T",
     "P",
     "a"
    ],
    "vincoli": [
     "ellisse DBCA di centro T con CT : TA = 70 : 69",
     "C quadratura, A sizigia",
     "angolo CTa : angolo retto CTA = 29g 12h 44′ : 27g 7h 43′"
    ]
   },
   "dati": {
    "variazione_ottanti_moto_fisso": "32′ 32″",
    "variazione_media": "35′ 10″",
    "apogeo_sole": "33′ 14″ (ricalcolo 33′ 16″)",
    "perigeo_sole": "37′ 11″ (ricalcolo 37′ 13″)"
   },
   "passi": [
    {
     "id": "L3-P29-p1",
     "la": "",
     "it": "Questa disuguaglianza nasce in parte dalla forma ellittica dell’orbita lunare, in parte dalla disuguaglianza dei momenti dell’area che la Luna descrive con un raggio condotto alla Terra.",
     "en": "This inequality is owing partly to the elliptic figure of the moon's orbit, partly to the inequality of the moments of the area which the moon by a radius drawn to the earth describes.",
     "dipende_da": [],
     "figura": {
      "mostra": [],
      "evidenzia": []
     }
    },
    {
     "id": "L3-P29-p2",
     "la": "",
     "it": "Se la Luna P si muovesse nell’ellisse DBCA attorno alla Terra in quiete nel centro dell’ellisse, e con il raggio TP condotto alla Terra descrivesse l’area CTP proporzionale al tempo, e il semidiametro massimo CT dell’ellisse stesse al semidiametro minimo TA come 70 a 69, la tangente dell’angolo CTP starebbe alla tangente dell’angolo del moto medio, contato dalla quadratura C, come il semidiametro TA dell’ellisse sta al suo semidiametro TC, ossia come 69 a 70.",
     "en": "If the moon P revolved in the ellipsis DBCA about the earth quiescent in the centre of the ellipsis, and by the radius TP, drawn to the earth, described the area CTP, proportional to the time of description; and the greatest semi-diameter CT of the ellipsis was to the least TA as 70 to 69; the tangent of the angle CTP would be to the tangent of the angle of the mean motion, computed from the quadrature C, as the semi-diameter TA of the ellipsis to its semi-diameter TC, or as 69 to 70.",
     "dipende_da": [],
     "figura": {
      "mostra": [
       "ellisse DBCA",
       "T al centro",
       "P",
       "area CTP"
      ],
      "evidenzia": [
       "tan CTP : tan moto medio = TA : TC = 69 : 70"
      ]
     }
    },
    {
     "id": "L3-P29-p3",
     "la": "",
     "it": "La descrizione dell’area CTP, però, nel progresso della Luna dalla quadratura alla sizigia, deve essere accelerata in modo che il suo momento nella sizigia della Luna stia al suo momento nella quadratura come 11073 a 10973, e che l’eccesso del momento in un luogo intermedio qualsiasi P sul momento nella quadratura sia come il quadrato del seno dell’angolo CTP.",
     "en": "But the description of the area CTP, as the moon advances from the quadrature to the syzygy, ought to be in such manner accelerated, that the moment of the area in the moon's syzygy may be to the moment thereof in its quadrature as 11073 to 10973; and that the excess of the moment in any intermediate place P above the moment in the quadrature may be as the square of the sine of the angle CTP;",
     "dipende_da": [],
     "figura": {
      "mostra": [],
      "evidenzia": [
       "momento in sizigia : in quadratura = 11073 : 10973",
       "eccesso come sin² CTP"
      ]
     },
     "nota": "I valori vengono dalla Prop. XXVI, qui non citata."
    },
    {
     "id": "L3-P29-p4",
     "la": "",
     "it": "Ciò avverrà con sufficiente precisione se la tangente dell’angolo CTP si diminuisce nel rapporto subduplicato del numero 10973 al numero 11073, cioè nel rapporto del numero 68,6877 al numero 69.",
     "en": "which we may effect with accuracy enough, if we diminish the tangent of the angle CTP in the subduplicate proportion of the number 10973 to the number 11073, that is, in proportion of the number 68,6877 to the number 69.",
     "dipende_da": [],
     "figura": {
      "mostra": [],
      "evidenzia": [
       "69 × √(10973/11073) = 68,6877"
      ]
     },
     "nota": "Ricalcolo: 68,68772."
    },
    {
     "id": "L3-P29-p5",
     "la": "",
     "it": "In questo modo la tangente dell’angolo CTP starà ora alla tangente del moto medio come 68,6877 a 70, e l’angolo CTP negli ottanti, dove il moto medio è di 45°, risulterà di 44° 27′ 28″, che, sottratto dall’angolo del moto medio di 45°, lascia la variazione massima di 32′ 32″.",
     "en": "Upon which account the tangent of the angle CTP will now be to the tangent of the mean motion as 68,6877 to 70; and the angle CTP in the octants, where the mean motion is 45°, will be found 44° 27' 28'', which subtracted from 45°, the angle of the mean motion, leaves the greatest variation 32' 32''.",
     "dipende_da": [],
     "figura": {
      "mostra": [
       "ottante (moto medio 45°)"
      ],
      "evidenzia": [
       "CTP = 44° 27′ 28″",
       "variazione 32′ 32″"
      ]
     },
     "nota": "Ricalcolo: arctan(68,6877/70) = 44° 27′ 28″; il massimo della differenza (a 45,27°) è ancora 32′ 32″."
    },
    {
     "id": "L3-P29-p6",
     "la": "",
     "it": "Così sarebbero le cose se la Luna, procedendo dalla quadratura alla sizigia, descrivesse un angolo CTA di soli novanta gradi.",
     "en": "Thus it would be, if the moon, in passing from the quadrature to the syzygy, described an angle CTA of 90 degrees only.",
     "dipende_da": [],
     "figura": {
      "mostra": [
       "angolo CTA di 90°"
      ],
      "evidenzia": []
     }
    },
    {
     "id": "L3-P29-p7",
     "la": "",
     "it": "Ma per il moto della Terra, per cui il Sole è trasportato con moto apparente in conseguenza, la Luna, prima di raggiungere il Sole, descrive un angolo CTa maggiore dell’angolo retto nel rapporto del tempo della rivoluzione sinodica lunare al tempo della rivoluzione periodica, cioè nel rapporto di 29g 12h 44′ a 27g 7h 43′.",
     "en": "But because of the motion of the earth, by which the sun is apparently transferred in consequentia, the moon, before it overtakes the sun, describes an angle CTa, greater than a right angle, in the proportion of the time of the synodic revolution of the moon to the time of its periodic revolution, that is, in the proportion of 29d. 12h. 44' to 27d. 7h. 43'.",
     "dipende_da": [],
     "figura": {
      "mostra": [
       "angolo CTa"
      ],
      "evidenzia": [
       "CTa : CTA = 29g 12h 44′ : 27g 7h 43′"
      ]
     }
    },
    {
     "id": "L3-P29-p8",
     "la": "",
     "it": "E in questo modo tutti gli angoli attorno al centro T si dilatano nello stesso rapporto, e la variazione, che altrimenti sarebbe di 32′ 32″, ora, aumentata nello stesso rapporto, diventa di 35′ 10″.",
     "en": "Whence it comes to pass that all the angles about the centre T are dilated in the same proportion; and the greatest variation, which otherwise would be but 32' 32'', now augmented in the said proportion, becomes 35' 10''.",
     "dipende_da": [],
     "figura": {
      "mostra": [],
      "evidenzia": [
       "32′ 32″ × 1,080853 = 35′ 10″"
      ]
     },
     "nota": "Ricalcolo: 35′ 9,9″."
    },
    {
     "id": "L3-P29-p9",
     "la": "",
     "it": "Questa è la sua grandezza alla distanza media del Sole dalla Terra, trascurate le differenze che possono nascere dalla curvatura dell’orbe magno e dalla maggiore azione del Sole sulla Luna falcata e nuova che sulla Luna gibbosa e piena.",
     "en": "And this is its magnitude in the mean distance of the sun from the earth, neglecting the differences which may arise from the curvature of the orbis magnus, and the stronger action of the sun upon the moon when horned and new, than when gibbous and full.",
     "dipende_da": [],
     "figura": {
      "mostra": [],
      "evidenzia": []
     }
    },
    {
     "id": "L3-P29-p10",
     "la": "",
     "it": "Ad altre distanze del Sole dalla Terra, la variazione massima sta nel rapporto composto dal rapporto duplicato del tempo della rivoluzione sinodica lunare (dato il tempo dell’anno), direttamente, e dal rapporto triplicato della distanza del Sole dalla Terra, inversamente.",
     "en": "In other distances of the sun from the earth, the greatest variation is in a proportion compounded of the duplicate proportion of the time of the synodic revolution of the moon (the time of the year being given) directly, and the triplicate proportion of the distance of the sun from the earth inversely.",
     "dipende_da": [],
     "figura": {
      "mostra": [],
      "evidenzia": [
       "variazione ∝ (tempo sinodico)² : (distanza del Sole)³"
      ]
     }
    },
    {
     "id": "L3-P29-p11",
     "la": "",
     "it": "Perciò nell’apogeo del Sole la variazione massima è di 33′ 14″, e nel suo perigeo di 37′ 11″, purché l’eccentricità del Sole stia al semidiametro trasverso dell’orbe magno come 16 15/16 a 1000.",
     "en": "And, therefore, in the apogee of the sun, the greatest variation is 33' 14'', and in its perigee 37' 11'', if the eccentricity of the sun is to the transverse semi-diameter of the orbis magnus as [SVG 1041] to 1000.",
     "dipende_da": [],
     "figura": {
      "mostra": [],
      "evidenzia": [
       "33′ 14″ nell’apogeo",
       "37′ 11″ nel perigeo",
       "eccentricità 16 15/16 : 1000"
      ]
     },
     "nota": "Ricalcolo (nota N9): 33′ 16″ e 37′ 13″."
    },
    {
     "id": "L3-P29-p12",
     "la": "",
     "it": "Fin qui abbiamo indagato la variazione in un’orbita non eccentrica, nella quale cioè la Luna nei suoi ottanti è sempre alla sua distanza media dalla Terra.",
     "en": "Hitherto we have investigated the variation in an orb not eccentric, in which, to wit, the moon in its octants is always in its mean distance from the earth.",
     "dipende_da": [],
     "figura": {
      "mostra": [],
      "evidenzia": []
     }
    },
    {
     "id": "L3-P29-p13",
     "la": "",
     "it": "Se la Luna, per la sua eccentricità, dista dalla Terra più o meno che se fosse posta in questa orbita, la variazione può essere un po’ maggiore o un po’ minore di quanto comporti la regola qui data: ma lascio agli astronomi di determinarne l’eccesso o il difetto dai fenomeni.",
     "en": "If the moon, on account of its eccentricity, is more or less removed from the earth than if placed in this orb, the variation may be something greater, or something less, than according to this rule. But I leave the excess or defect to the determination of astronomers from the phænomena.",
     "dipende_da": [],
     "figura": {
      "mostra": [],
      "evidenzia": []
     },
     "nota": "Motte divide la frase in due."
    }
   ]
  }
 ]
}
```

**Fine del Fascicolo 24a.** Il seguito (Propp. XXX–XXXIII e Scolio) è nel Fascicolo 24b.
