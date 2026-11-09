> **Copia pubblica.** In questa versione i campi `"la"` della Parte B sono vuoti: le frasi latine vengono dalla trascrizione del Newton Project, che non si ridistribuisce. Il latino del 1726 si legge su newtonproject.ox.ac.uk.

# Isaac Newton
# Principi matematici della filosofia naturale

## Fascicolo 9 — Libro I, Sezioni IX e X

**Nuova traduzione italiana di lavoro dal latino del 1726, confrontata con l’inglese di Andrew Motte nell’edizione del 1846. Sezione IX: *De motu corporum in orbibus mobilibus, deque motu apsidum*. Sezione X: *De motu corporum in superficiebus datis, deque funipendulorum motu reciproco*.**

Versione 0.1 — 8 novembre 2026. Preparata con Claude (Anthropic) per Massimo Bosetti.

### Stato e perimetro

Questo fascicolo traduce integralmente le Sezioni IX e X del Libro I (*De motu corporum*): le Proposizioni XLIII–XLV con i loro corollari ed esempi, il capoverso di passaggio *Hactenus de motu corporum* che chiude la Sezione IX, e le Proposizioni XLVI–LVI con i corollari e lo scolio. È una traduzione di lavoro, non un’edizione critica validata.

Gli identificatori **S9.01–S9.25** e **S10.01–S10.38** e i titoli tematici tra parentesi sono aggiunte editoriali. Servono a orientare la lettura e a controllare la completezza. I numeri romani delle proposizioni e dei problemi o teoremi appartengono al testo originale. Le integrazioni del curatore sono tra parentesi quadre. Le note poste dopo la traduzione non fanno parte del testo di Newton.

Le due sezioni hanno un carattere diverso:

- la **Sezione IX** contiene il teorema delle orbite rotanti (Prop. XLIV) e il metodo per calcolare il moto delle apsidi nelle orbite quasi circolari (Prop. XLV), con il celebre valore per la Luna. Gli esempi della Prop. XLV sono stati ricontrollati cifra per cifra e verificati con un’integrazione numerica delle orbite (note N5–N8);
- la **Sezione X** tratta il moto su piani e superfici che non passano per il centro delle forze, la rettificazione della cicloide dentro e fuori di un globo, il pendolo cicloidale isocrono in un campo di forza proporzionale alla distanza e, in generale, le forze che rendono isocrone le oscillazioni. Le proposizioni geometriche principali (XLVIII–LII) sono state verificate numericamente su figure di prova (note N12–N15).

In coda al fascicolo, la **Parte B** contiene i dati strutturati per le pagine interattive di 14 unità (12 proposizioni e 2 corollari con dimostrazione e figura).

### Fonti effettivamente consultate

1. **Latino di riferimento.** Isaac Newton, *Philosophiæ Naturalis Principia Mathematica*, terza edizione, Londra, 1726, Libro I, Sezione IX, pp. 129–142, e Sezione X, pp. 142–160. Trascrizione normalizzata del Newton Project, documento **NATP00087**, nelle copie di lavoro `fonti/latino-1726-L1-S09.md` e `fonti/latino-1726-L1-S10.md` (pagine secondo i marcatori <n> della trascrizione; figure citate come NATP00087-100…119, non disponibili).
2. **Inglese di confronto.** *Newton’s Principia. The Mathematical Principles of Natural Philosophy*, traduzione di Andrew Motte, New York, Daniel Adee, 1846, Sezione IX, pp. 172–182, e Sezione X, pp. 182–194, secondo i marcatori di pagina dell’EPUB (Project Gutenberg n. 76404), nelle copie `fonti/motte-1846-L1-S09.md` e `-S10.md`. Le formule stampate come immagine (SVG 157–255) sono state rese in PNG e lette una per una.
3. **Fascicolo 3** e brief comune del Libro I, per il formato, i criteri e il glossario.

Non ho consultato né riprodotto traduzioni moderne (Cajori, Cohen–Whitman, Pala, Giudice). Le figure originali non erano disponibili: le relazioni geometriche sono ricostruite soltanto dalle lettere citate nel testo.

### Criteri di traduzione

- Il testo guida è il latino; l’inglese serve a controllare le interpretazioni ed è annotato quando aggiunge, omette o sbaglia.
- Si applica il **glossario comune** del brief (fascicoli 1–3 e termini tecnici del Libro I): in particolare «forza centripeta», «forza acceleratrice», «forza assoluta», «rapporto duplicato / triplicato / subduplicato», «rapporto primo / ultimo», «quantità nascenti / evanescenti», «seno verso», «lato retto», «fuoco», «dato di posizione / di forma / di grandezza», «apside, apsidi», «in conseguenza / in antecedenza», «pendolo a filo», «Cor.», C.V.D., C.V.T., C.V.F.
- Le estensioni del glossario proprie di questo fascicolo sono elencate e motivate nel § A.0 (fra le altre: *altitudo* «altezza», *apsis summa / ima* «apside superiore / inferiore», *lineola* «lineetta», *vicissim* «permutando», *dignitas* «potenza», *vestigium* «traccia», *vis extranea* «forza estranea»).
- Gli enunciati latini all’infinito sono resi con l’indicativo; i problemi all’infinito (*Facere ut…*, *Definire…*, *invenire…*) con l’infinito italiano.
- **Formule.** Nel testo tradotto restano i rapporti di Newton. Le quantità sono scritte come AB², A³, GG − FF; le frazioni con la barra; le radici con √, per esempio √3, √((b + c)/(mb + nc)). Gli esponenti letterali usano apici Unicode (Aⁿ⁻³, Tᵐ⁻¹); gli **esponenti frazionari o composti** si scrivono con l’accento circonflesso e la parentesi, per esempio A^(11/4), A^(nn/mm − 3); il numero misto «2 4/243» della stampa è scritto A^(2 + 4/243). I prodotti di linee sono scritti mk × ms.
- **Formule appiattite.** La trascrizione perde sistematicamente i segni di radice e le linee di frazione (§ A.15). Le ho ricostruite dal contesto, dalla matematica e dalle formule-immagine di Motte, e ogni lettura è dichiarata nell’apparato. Dove la trascrizione omette un termine necessario (Es. 1 della Prop. XLV), l’integrazione è tra parentesi quadre.
- I numeri decimali sono scritti con la virgola (357,45; 180,7623); gradi, primi e secondi con i simboli ° ′ ″.
- Rimandi interni nella forma del brief: «per il Cor. 2 della Prop. X», «per il Cor. II delle Leggi», «per la Prop. XXXVIII».

---

## Traduzione italiana

### Sezione IX

*Il moto dei corpi in orbite mobili, e il moto delle apsidi*

### Proposizione XLIII. Problema XXX (corpo in un’orbita che ruota)

**[S9.01]** **Si deve fare in modo che un corpo possa muoversi in una traiettoria qualsiasi, che ruota intorno al centro delle forze, esattamente come un altro corpo nella stessa traiettoria in quiete.**

**[S9.02]** Nell’orbita VPK, data di posizione, ruoti il corpo P procedendo da V verso K. Dal centro C si conduca in ogni istante Cp, uguale a CP, che formi l’angolo VCp proporzionale all’angolo VCP; l’area che la linea Cp descrive starà all’area VCP, che la linea CP descrive nello stesso tempo, come la velocità della linea Cp che descrive sta alla velocità della linea CP che descrive, cioè come l’angolo VCp sta all’angolo VCP: dunque in un rapporto dato, e perciò sarà proporzionale al tempo. Poiché l’area che la linea Cp descrive nel piano immobile è proporzionale al tempo, è manifesto che un corpo, sotto l’azione di una forza centripeta di giusta quantità, può ruotare insieme con il punto p lungo quella linea curva che lo stesso punto p, nel modo ora esposto, descrive nel piano immobile. Si faccia l’angolo VCu uguale all’angolo PCp, la linea Cu uguale alla linea CV e la figura uCp uguale alla figura VCP: il corpo, trovandosi sempre in p, si muoverà sul perimetro della figura rotante uCp, e ne descriverà l’arco up nello stesso tempo in cui l’altro corpo P può descrivere l’arco VP, simile e uguale a esso, nella figura in quiete VPK. Si cerchi dunque, per il Cor. 5 della Prop. VI, la forza centripeta con cui un corpo può ruotare lungo quella linea curva che il punto p descrive nel piano immobile, e il problema sarà risolto. C.V.F.

### Proposizione XLIV. Teorema XIV (la differenza delle forze va come l’inverso del cubo)

**[S9.03]** **La differenza delle forze per effetto delle quali un corpo in un’orbita in quiete e un altro corpo nella stessa orbita rotante possono muoversi allo stesso modo è inversamente in rapporto triplicato dell’altezza comune.**

**[S9.04]** Alle parti VP, PK dell’orbita in quiete siano simili e uguali le parti up, pk dell’orbita rotante; e si intenda che la distanza dei punti P, K sia minima. Dal punto k abbassa sulla retta pC la perpendicolare kr e prolungala fino a m, in modo che mr stia a kr come l’angolo VCp sta all’angolo VCP. Poiché le altezze dei corpi, PC e pC, KC e kC, sono sempre uguali, è manifesto che gli incrementi o i decrementi delle linee PC e pC sono sempre uguali; e perciò, se i singoli moti dei corpi che si trovano nei luoghi P e p si scompongono (per il Cor. II delle Leggi) in due, dei quali i primi siano diretti verso il centro, cioè lungo le linee PC, pC, e gli altri siano trasversali ai primi e abbiano direzione lungo linee perpendicolari a PC, pC, i moti verso il centro saranno uguali, e il moto trasversale del corpo p starà al moto trasversale del corpo P come il moto angolare della linea pC sta al moto angolare della linea PC, cioè come l’angolo VCp sta all’angolo VCP. Dunque, nello stesso tempo in cui il corpo P, con l’uno e l’altro dei suoi moti, giunge al punto K, il corpo p, con un moto uguale verso il centro, si muoverà di altrettanto da p verso C; e perciò, trascorso quel tempo, si troverà in qualche punto della linea mkr, che passa per il punto k ed è perpendicolare alla linea pC; e con il moto trasversale acquisterà dalla linea pC una distanza che starà alla distanza che l’altro corpo P acquista dalla linea PC come il moto trasversale del corpo p sta al moto trasversale dell’altro corpo P. Perciò, poiché kr è uguale alla distanza che il corpo P acquista dalla linea PC, e mr sta a kr come l’angolo VCp sta all’angolo VCP, cioè come il moto trasversale del corpo p sta al moto trasversale del corpo P, è manifesto che il corpo p, trascorso quel tempo, si troverà nel luogo m.

**[S9.05]** Così andranno le cose quando i corpi p e P si muovono allo stesso modo lungo le linee pC e PC, e sono perciò sollecitati lungo quelle linee da forze uguali. Si prenda poi l’angolo pCn che stia all’angolo pCk come l’angolo VCp sta all’angolo VCP, e sia nC uguale a kC: il corpo p, trascorso quel tempo, si troverà in realtà in n; e perciò è sollecitato da una forza maggiore di quella del corpo P, se l’angolo nCp è maggiore dell’angolo kCp, cioè se l’orbita upk si muove in conseguenza, oppure si muove in antecedenza con una celerità maggiore del doppio di quella con cui la linea CP è portata in conseguenza; e da una forza minore, se l’orbita si muove in antecedenza più lentamente. E la differenza delle forze è come la distanza mn fra i due luoghi, attraverso la quale il corpo p deve essere trasportato per azione di essa nel dato intervallo di tempo.

**[S9.06]** Con centro C e raggio Cn o Ck si intenda descritto un cerchio che tagli in s e t le linee mr, mn prolungate: il rettangolo mn × mt sarà uguale al rettangolo mk × ms, e perciò mn sarà uguale a (mk × ms)/mt. Ma poiché i triangoli pCk, pCn, in un tempo dato, sono dati di grandezza, kr e mr, e la loro differenza mk e la loro somma ms, sono inversamente come l’altezza pC; e perciò il rettangolo mk × ms è inversamente come il quadrato dell’altezza pC. Inoltre mt è direttamente come ½mt, cioè come l’altezza pC. Questi sono i rapporti primi delle linee nascenti; e di qui (mk × ms)/mt, cioè la lineetta nascente mn, e la differenza delle forze, che le è proporzionale, risultano inversamente come il cubo dell’altezza pC. C.V.D.

**[S9.07]** *Cor. 1.* Di qui la differenza delle forze nei luoghi P e p, o K e k, sta alla forza con cui un corpo potrebbe ruotare di moto circolare da R a K nello stesso tempo in cui il corpo P nell’orbita immobile descrive l’arco PK, come la lineetta nascente mn sta al seno verso dell’arco nascente RK, cioè come (mk × ms)/mt sta a rk²/(2kC), o come mk × ms sta al quadrato di rk; cioè, se si prendono due quantità date F, G che stiano fra loro nel rapporto che ha l’angolo VCP all’angolo VCp, come GG − FF sta a FF. E perciò, se con centro C e con un raggio qualsiasi CP o Cp si descrive un settore circolare uguale all’intera area VPC che il corpo P, ruotando nell’orbita immobile, ha descritto in un tempo qualsiasi con il raggio condotto al centro, la differenza delle forze con cui ruotano il corpo P nell’orbita immobile e il corpo p nell’orbita mobile starà alla forza centripeta con cui un corpo, con il raggio condotto al centro, avrebbe potuto descrivere uniformemente quel settore nello stesso tempo in cui è stata descritta l’area VPC, come GG − FF sta a FF. Infatti quel settore e l’area pCk stanno fra loro come i tempi in cui sono descritti.

**[S9.08]** *Cor. 2.* Se l’orbita VPK è un’ellisse che ha il fuoco in C e l’apside superiore in V, e le si pone simile e uguale l’ellisse upk, in modo che pC sia sempre uguale a PC e l’angolo VCp stia all’angolo VCP nel rapporto dato di G a F; e se per l’altezza PC o pC si scrive A e per il lato retto dell’ellisse si pone 2R, la forza con cui un corpo può ruotare nell’ellisse mobile sarà come FF/AA + (RGG − RFF)/A³, e viceversa. Si rappresenti infatti con la quantità FF/AA la forza con cui un corpo ruota nell’ellisse immobile: la forza in V sarà FF/CV². La forza con cui un corpo potrebbe ruotare in un cerchio, alla distanza CV, con la velocità che il corpo che ruota nell’ellisse ha in V, sta alla forza da cui il corpo che ruota nell’ellisse è sollecitato nell’apside V come la metà del lato retto dell’ellisse sta al semidiametro CV del cerchio, e perciò vale RFF/CV³; e la forza che sta a questa come GG − FF sta a FF vale (RGG − RFF)/CV³; e questa forza (per il Cor. 1 di questa proposizione) è la differenza delle forze in V con cui ruotano il corpo P nell’ellisse immobile VPK e il corpo p nell’ellisse mobile upk. Poiché dunque (per questa proposizione) quella differenza, in qualsiasi altra altezza A, sta a sé stessa nell’altezza CV come 1/A³ sta a 1/CV³, la stessa differenza in ogni altezza A varrà (RGG − RFF)/A³. Alla forza FF/AA, con cui un corpo può ruotare nell’ellisse immobile VPK, si aggiunga dunque l’eccesso (RGG − RFF)/A³: si comporrà la forza totale FF/AA + (RGG − RFF)/A³, con cui un corpo potrebbe ruotare negli stessi tempi nell’ellisse mobile upk.

**[S9.09]** *Cor. 3.* Allo stesso modo si ricaverà che, se l’orbita immobile VPK è un’ellisse che ha il centro nel centro delle forze C, e le si pone simile, uguale e concentrica l’ellisse mobile upk; se 2R è il lato retto principale di questa ellisse e 2T il lato trasverso, ossia l’asse maggiore, e l’angolo VCp sta sempre all’angolo VCP come G sta a F, le forze con cui i corpi possono ruotare in tempi uguali nell’ellisse immobile e in quella mobile saranno rispettivamente come FFA/T³ e FFA/T³ + (RGG − RFF)/A³.

**[S9.10]** *Cor. 4.* E in generale, se l’altezza massima CV del corpo si chiama T, il raggio di curvatura che l’orbita VPK ha in V, cioè il raggio del cerchio ugualmente curvo, si chiama R, e la forza centripeta con cui un corpo può ruotare in una traiettoria immobile qualsiasi VPK si chiama VFF/TT nel luogo V, e indeterminatamente X negli altri luoghi P, chiamata A l’altezza CP; e se si prende G a F nel rapporto dato dell’angolo VCp all’angolo VCP, la forza centripeta con cui lo stesso corpo può compiere gli stessi moti, negli stessi tempi, nella stessa traiettoria upk mossa di moto circolare, sarà come la somma delle forze X + (VRGG − VRFF)/A³.

**[S9.11]** *Cor. 5.* Dato dunque il moto di un corpo in un’orbita immobile qualsiasi, il suo moto angolare intorno al centro delle forze può essere accresciuto o diminuito in un rapporto dato, e di qui si possono trovare nuove orbite immobili nelle quali i corpi girino per effetto di nuove forze centripete.

**[S9.12]** *Cor. 6.* Dunque, se sulla retta CV, data di posizione, si innalza la perpendicolare VP di lunghezza indeterminata, si congiunge CP e si conduce Cp uguale a essa, che formi l’angolo VCp in un rapporto dato con l’angolo VCP, la forza con cui un corpo può girare lungo quella curva Vpk che il punto p tocca di continuo sarà inversamente come il cubo dell’altezza Cp. Infatti il corpo P, per la forza d’inerzia, senza che nessun’altra forza lo solleciti, può avanzare uniformemente lungo la retta VP. Si aggiunga una forza verso il centro C, inversamente proporzionale al cubo dell’altezza CP o Cp, e (per quanto ora dimostrato) quel moto rettilineo sarà piegato nella linea curva Vpk. E questa curva Vpk è la stessa curva VPQ trovata nel Cor. 3 della Prop. XLI, lungo la quale, come lì abbiamo detto, salgono obliquamente i corpi attratti da forze di questo tipo.

### Proposizione XLV. Problema XXXI (moto delle apsidi nelle orbite quasi circolari)

**[S9.13]** **Si cercano i moti delle apsidi delle orbite che sono vicinissime ai cerchi.**

**[S9.14]** Il problema si risolve aritmeticamente facendo in modo che l’orbita che un corpo, ruotando in un’ellisse mobile (come nel Cor. 2 o 3 della proposizione precedente), descrive nel piano immobile si avvicini alla forma dell’orbita di cui si cercano le apsidi, e cercando le apsidi dell’orbita che quel corpo descrive nel piano immobile. Le orbite, poi, acquisteranno la stessa forma se le forze centripete con cui sono descritte, confrontate fra loro, si rendono proporzionali ad altezze uguali. Sia il punto V l’apside superiore, e si scriva T per l’altezza massima CV, A per qualsiasi altra altezza CP o Cp, e X per la differenza delle altezze CV − CP: la forza con cui si muove un corpo che ruota in un’ellisse rotante intorno al proprio fuoco C (come nel Cor. 2), e che nel Cor. 2 era come FF/AA + (RGG − RFF)/A³, cioè come (FFA + RGG − RFF)/A³, sostituendo T − X al posto di A sarà come (RGG − RFF + TFF − FFX)/A³. In modo simile si deve ridurre qualsiasi altra forza centripeta a una frazione il cui denominatore sia A³, e i numeratori, confrontati i termini omologhi, si devono porre in proporzione. La cosa sarà chiara con degli esempi.

**[S9.15]** *Es. 1.* Supponiamo che la forza centripeta sia uniforme, e perciò come A³/A³, ossia (scrivendo T − X al posto di A nel numeratore) come (T³ − 3TTX + 3TXX − X³)/A³; e, confrontati i termini corrispondenti dei numeratori, cioè quelli dati con quelli dati e quelli non dati con quelli non dati, si avrà: RGG − RFF + TFF sta a T³ come −FF[X] sta a −3TTX + 3TXX − X³, ossia come −FF sta a −3TT + 3TX − XX. Ora, poiché si suppone che l’orbita sia vicinissima a un cerchio, l’orbita coincida con il cerchio; e, rese uguali R e T e diminuita X all’infinito, i rapporti ultimi saranno: RGG sta a T³ come −FF sta a −3TT, ossia GG sta a TT come FF sta a 3TT; e, permutando, GG sta a FF come TT sta a 3TT, cioè come 1 sta a 3; e perciò G sta a F, cioè l’angolo VCp sta all’angolo VCP, come 1 sta a √3.

**[S9.16]** Dunque, poiché un corpo nell’ellisse immobile, scendendo dall’apside superiore all’apside inferiore, compie un angolo VCP (per così dire) di 180 gradi, l’altro corpo nell’ellisse mobile, e quindi nell’orbita immobile di cui trattiamo, scendendo dall’apside superiore all’apside inferiore compirà un angolo VCp di 180/√3 gradi; e ciò a causa della similitudine fra quest’orbita, che il corpo descrive sotto l’azione di una forza centripeta uniforme, e l’orbita che descrive nel piano in quiete il corpo che compie i suoi giri nell’ellisse rotante. Con il precedente confronto dei termini queste orbite sono rese simili, non in generale, ma quando si avvicinano il più possibile alla forma circolare. Un corpo che ruota con una forza centripeta uniforme in un’orbita quasi circolare compirà dunque sempre, fra l’apside superiore e l’apside inferiore, un angolo al centro di 180/√3 gradi, ossia di 103° 55′ 23″: giungerà dall’apside superiore all’apside inferiore quando avrà compiuto una volta questo angolo, e di lì tornerà all’apside superiore quando avrà compiuto di nuovo lo stesso angolo; e così di seguito all’infinito.

**[S9.17]** *Es. 2.* Supponiamo che la forza centripeta sia come una potenza qualsiasi dell’altezza A, Aⁿ⁻³, ossia Aⁿ/A³, dove n − 3 e n indicano indici di potenze qualsiasi, interi o fratti, razionali o irrazionali, positivi o negativi. Quel numeratore Aⁿ, ossia (T − X)ⁿ, ridotto in una serie indeterminata con il nostro metodo delle serie convergenti, diventa Tⁿ − nXTⁿ⁻¹ + ((nn − n)/2)XXTⁿ⁻² ecc. E, confrontati i suoi termini con i termini dell’altro numeratore RGG − RFF + TFF − FFX, si ha: RGG − RFF + TFF sta a Tⁿ come −FF sta a −nTⁿ⁻¹ + ((nn − n)/2)XTⁿ⁻² ecc. E, prendendo i rapporti ultimi quando le orbite si avvicinano alla forma circolare, si ha: RGG sta a Tⁿ come −FF sta a −nTⁿ⁻¹, ossia GG sta a Tⁿ⁻¹ come FF sta a nTⁿ⁻¹; e, permutando, GG sta a FF come Tⁿ⁻¹ sta a nTⁿ⁻¹, cioè come 1 sta a n; e perciò G sta a F, cioè l’angolo VCp sta all’angolo VCP, come 1 sta a √n. Perciò, poiché l’angolo VCP compiuto nell’ellisse nella discesa del corpo dall’apside superiore all’apside inferiore è di 180 gradi, l’angolo VCp compiuto nella discesa del corpo dall’apside superiore all’apside inferiore, nell’orbita quasi circolare che un corpo qualsiasi descrive per effetto di una forza centripeta proporzionale alla potenza Aⁿ⁻³, sarà uguale a un angolo di 180/√n gradi; e, ripetuto questo angolo, il corpo tornerà dall’apside inferiore all’apside superiore, e così di seguito all’infinito.

**[S9.18]** Così, se la forza centripeta è come la distanza del corpo dal centro, cioè come A, ossia A⁴/A³, sarà n uguale a 4 e √n uguale a 2; e perciò l’angolo fra l’apside superiore e l’apside inferiore sarà uguale a 180/2 gradi, ossia a 90 gradi. Compiuta dunque la quarta parte di una rivoluzione, il corpo giungerà all’apside inferiore, e compiuta un’altra quarta parte all’apside superiore, e così di seguito, alternativamente, all’infinito. Ciò è manifesto anche dalla Prop. X. Infatti un corpo sollecitato da questa forza centripeta ruoterà in un’ellisse immobile, il cui centro è nel centro delle forze. Se invece la forza centripeta è inversamente come la distanza, cioè direttamente come 1/A, ossia A²/A³, sarà n uguale a 2, e perciò l’angolo fra l’apside superiore e l’inferiore sarà di 180/√2 gradi, ossia di 127° 16′ 45″; e perciò un corpo che ruota con una tale forza, ripetendo continuamente questo angolo, giungerà alternativamente dall’apside superiore all’inferiore e dall’inferiore alla superiore, in eterno. Inoltre, se la forza centripeta è inversamente come la radice quarta dell’undicesima potenza dell’altezza, cioè inversamente come A^(11/4), e perciò direttamente come 1/A^(11/4), ossia come A^(1/4)/A³, sarà n uguale a 1/4, e 180/√n gradi uguale a 360 gradi; e perciò il corpo, partendo dall’apside superiore e quindi scendendo continuamente, giungerà all’apside inferiore quando avrà compiuto una rivoluzione intera; poi, compiendo con una salita continua un’altra rivoluzione intera, tornerà all’apside superiore; e così alternativamente in eterno.

**[S9.19]** *Es. 3.* Assumendo m e n come indici qualsiasi di potenze dell’altezza, e b, c come numeri dati qualsiasi, supponiamo che la forza centripeta sia come (bAᵐ + cAⁿ)/A³, cioè come (b(T − X)ᵐ + c(T − X)ⁿ)/A³, ossia (con lo stesso nostro metodo delle serie convergenti) come (bTᵐ + cTⁿ − mbXTᵐ⁻¹ − ncXTⁿ⁻¹ + ((mm − m)/2)bXXTᵐ⁻² + ((nn − n)/2)cXXTⁿ⁻² ecc.)/A³; e, confrontati i termini dei numeratori, si avrà: RGG − RFF + TFF sta a bTᵐ + cTⁿ come −FF sta a −mbTᵐ⁻¹ − ncTⁿ⁻¹ + ((mm − m)/2)bXTᵐ⁻² + ((nn − n)/2)cXTⁿ⁻² ecc. E, prendendo i rapporti ultimi che risultano quando le orbite si avvicinano alla forma circolare, si ha: GG sta a bTᵐ⁻¹ + cTⁿ⁻¹ come FF sta a mbTᵐ⁻¹ + ncTⁿ⁻¹; e, permutando, GG sta a FF come bTᵐ⁻¹ + cTⁿ⁻¹ sta a mbTᵐ⁻¹ + ncTⁿ⁻¹. Questa proporzione, rappresentando aritmeticamente con l’unità l’altezza massima CV, ossia T, diventa: GG sta a FF come b + c sta a mb + nc, e perciò come 1 sta a (mb + nc)/(b + c). Di qui G sta a F, cioè l’angolo VCp sta all’angolo VCP, come 1 sta a √((mb + nc)/(b + c)). E perciò, poiché l’angolo VCP fra l’apside superiore e l’apside inferiore nell’ellisse immobile è di 180 gradi, l’angolo VCp fra le stesse apsidi, nell’orbita che un corpo descrive per effetto di una forza centripeta proporzionale alla quantità (bAᵐ + cAⁿ)/A³, sarà uguale a un angolo di 180√((b + c)/(mb + nc)) gradi. E con lo stesso argomento, se la forza centripeta è come (bAᵐ − cAⁿ)/A³, l’angolo fra le apsidi risulterà di 180√((b − c)/(mb − nc)) gradi.

**[S9.20]** Né diversamente si risolverà il problema nei casi più difficili. La quantità a cui la forza centripeta è proporzionale deve sempre essere sciolta in serie convergenti che abbiano per denominatore A³. Poi la parte data del numeratore che risulta da quell’operazione, rispetto all’altra parte, non data, dello stesso numeratore, e la parte data di questo numeratore RGG − RFF + TFF − FFX, rispetto all’altra sua parte, non data, si devono porre nello stesso rapporto; e, cancellando le quantità superflue e scrivendo l’unità al posto di T, si otterrà la proporzione di G a F.

**[S9.21]** *Cor. 1.* Di qui, se la forza centripeta è come una potenza dell’altezza, quella potenza si può trovare dal moto delle apsidi; e viceversa. Cioè, se il moto angolare totale con cui il corpo torna alla stessa apside sta al moto angolare di una rivoluzione, ossia di 360 gradi, come un numero m sta a un altro numero n, e l’altezza si chiama A, la forza sarà come la potenza A^(nn/mm − 3) dell’altezza, il cui indice è nn/mm − 3. Ciò è manifesto per il secondo esempio. Di qui è chiaro che quella forza, allontanandosi dal centro, non può decrescere in un rapporto maggiore del triplicato dell’altezza. Un corpo che ruota con una tale forza e parte da un’apside, se comincia a scendere, non giungerà mai all’apside inferiore, cioè all’altezza minima, ma scenderà fino al centro, descrivendo quella linea curva di cui abbiamo trattato nel Cor. 3 della Prop. XLI. Se invece, partendo dall’apside, comincia a salire anche di pochissimo, salirà all’infinito e non giungerà mai all’apside superiore: descriverà infatti quella linea curva di cui si è trattato nello stesso corollario e nel Cor. 6 della Prop. XLIV.

**[S9.22]** Così anche, quando la forza, allontanandosi dal centro, decresce in un rapporto maggiore del triplicato dell’altezza, il corpo che parte da un’apside, secondo che cominci a scendere o a salire, o scenderà fino al centro o salirà all’infinito. Ma se la forza, allontanandosi dal centro, o decresce in un rapporto minore del triplicato dell’altezza, o cresce in un rapporto qualsiasi dell’altezza, il corpo non scenderà mai fino al centro, ma prima o poi giungerà all’apside inferiore; e viceversa, se il corpo, scendendo e salendo alternativamente da un’apside all’altra, non approda mai al centro, la forza, allontanandosi dal centro, o aumenterà, o decrescerà in un rapporto minore del triplicato dell’altezza; e quanto più presto il corpo sarà tornato da un’apside all’altra, tanto più il rapporto delle forze si allontanerà da quel rapporto triplicato.

**[S9.23]** Così, se il corpo, con discesa e salita alternate, torna dall’apside superiore all’apside superiore in 8, o 4, o 2, o 1½ rivoluzioni, cioè se m sta a n come 8, o 4, o 2, o 1½ sta a 1, e perciò nn/mm − 3 vale 1/64 − 3, o 1/16 − 3, o 1/4 − 3, o 4/9 − 3, la forza sarà come A^(1/64 − 3), o A^(1/16 − 3), o A^(1/4 − 3), o A^(4/9 − 3), cioè inversamente come A^(3 − 1/64), o A^(3 − 1/16), o A^(3 − 1/4), o A^(3 − 4/9). Se il corpo a ogni rivoluzione torna alla stessa apside immobile, sarà m a n come 1 a 1, e perciò A^(nn/mm − 3) uguale ad A⁻², ossia 1/AA; e perciò il decremento delle forze è in rapporto duplicato dell’altezza, come si è dimostrato in precedenza. Se il corpo torna alla stessa apside in tre quarti, o due terzi, o un terzo, o un quarto di una rivoluzione, sarà m a n come 3/4, o 2/3, o 1/3, o 1/4 a 1, e perciò A^(nn/mm − 3) uguale ad A^(16/9 − 3), o A^(9/4 − 3), o A^(9 − 3), o A^(16 − 3); e perciò la forza sarà o inversamente come A^(11/9) o A^(3/4), o direttamente come A⁶ o A¹³. Infine, se il corpo, procedendo dall’apside superiore all’apside superiore, compie una rivoluzione intera e in più tre gradi, e perciò quell’apside, a ogni rivoluzione del corpo, avanza di tre gradi in conseguenza, sarà m a n come 363 gradi a 360 gradi, ossia come 121 a 120, e perciò A^(nn/mm − 3) sarà uguale ad A^(−29523/14641); e perciò la forza centripeta sarà inversamente come A^(29523/14641), ossia, con buona approssimazione, inversamente come A^(2 + 4/243). La forza centripeta decresce dunque in un rapporto poco maggiore del duplicato, ma che si avvicina al duplicato 59¾ volte più che al triplicato.

**[S9.24]** *Cor. 2.* Di qui anche, se un corpo, per effetto di una forza centripeta inversamente proporzionale al quadrato dell’altezza, ruota in un’ellisse che ha il fuoco nel centro delle forze, e a questa forza centripeta si aggiunge o si toglie un’altra forza estranea qualsiasi, si può conoscere (per il terzo esempio) il moto delle apsidi che nascerà da quella forza estranea; e viceversa. Così, se la forza con cui il corpo ruota nell’ellisse è come 1/AA e la forza estranea tolta è come cA, e perciò la forza residua è come (A − cA⁴)/A³, sarà (nel terzo esempio) b uguale a 1, m uguale a 1 e n uguale a 4, e perciò l’angolo di rivoluzione fra le apsidi sarà uguale a un angolo di 180√((1 − c)/(1 − 4c)) gradi. Supponiamo che quella forza estranea sia 357,45 volte minore dell’altra forza con cui il corpo ruota nell’ellisse, cioè che c sia 100/35745, essendo A o T uguale a 1: 180√((1 − c)/(1 − 4c)) diventerà 180√(35645/35345), ossia 180,7623, cioè 180° 45′ 44″. Dunque il corpo, partendo dall’apside superiore, giungerà all’apside inferiore con un moto angolare di 180° 45′ 44″, e con il doppio di questo moto tornerà all’apside superiore; e perciò l’apside superiore, a ogni rivoluzione, avanzando compirà 1° 31′ 28″. L’apside della Luna è circa due volte più veloce.

### Passaggio alla Sezione X (piani eccentrici)

**[S9.25]** Fin qui il moto dei corpi in orbite i cui piani passano per il centro delle forze. Resta da determinare anche i moti in piani eccentrici. Infatti gli autori che trattano del moto dei gravi sogliono considerare le salite e le discese dei pesi, tanto oblique, su piani dati qualsiasi, quanto perpendicolari; e con pari diritto si deve considerare qui il moto dei corpi che tendono verso centri per effetto di forze qualsiasi e che poggiano su piani eccentrici. Supponiamo poi che i piani siano levigatissimi e assolutamente lisci, perché non ritardino i corpi. Anzi, in queste dimostrazioni, al posto dei piani sui quali i corpi poggiano e che, poggiandovi, toccano, usiamo piani paralleli a essi, nei quali si muovono i centri dei corpi e, muovendosi, descrivono orbite. E con la stessa regola determiniamo in seguito i moti dei corpi compiuti su superfici curve.

### Sezione X

*Il moto dei corpi su superfici date, e il moto alterno dei pendoli a filo*

### Proposizione XLVI. Problema XXXII (moto in un piano che non passa per il centro)

**[S10.01]** **Posta una forza centripeta di qualsiasi genere, dati sia il centro delle forze sia un piano qualsiasi nel quale il corpo ruota, e ammesse le quadrature delle figure curvilinee, si cerca il moto di un corpo che parte da un luogo dato, con una velocità data, lungo una retta data in quel piano.**

**[S10.02]** Sia S il centro delle forze, SC la distanza minima di questo centro dal piano dato, P il corpo che parte dal luogo P lungo la retta PZ, Q lo stesso corpo che ruota nella sua traiettoria, e PQR quella traiettoria, descritta nel piano dato, che bisogna trovare. Si congiungano CQ, QS; e se su QS si prende SV proporzionale alla forza centripeta con cui il corpo è tirato verso il centro S, e si conduce VT parallela a CQ, che incontri SC in T: la forza SV si scomporrà (per il Cor. II delle Leggi) nelle forze ST, TV; di queste, ST, tirando il corpo lungo una linea perpendicolare al piano, non muta in nulla il suo moto in questo piano. L’altra forza, TV, agendo secondo la posizione del piano, tira il corpo direttamente verso il punto C dato nel piano, e perciò fa sì che il corpo si muova in questo piano esattamente come se la forza ST fosse tolta e il corpo ruotasse intorno al centro C nello spazio libero per effetto della sola forza TV. Ma, data la forza centripeta TV con cui il corpo Q ruota nello spazio libero intorno al centro dato C, sono dati (per la Prop. XLII) sia la traiettoria PQR che il corpo descrive, sia il luogo Q in cui il corpo si troverà in un tempo dato qualsiasi, sia infine la velocità del corpo in quel luogo Q; e viceversa. C.V.T.

### Proposizione XLVII. Teorema XV (forza proporzionale alla distanza: tempi uguali in ogni piano)

**[S10.03]** **Posto che la forza centripeta sia proporzionale alla distanza del corpo dal centro, tutti i corpi che ruotano in piani qualsiasi descriveranno ellissi e compiranno le rivoluzioni in tempi uguali; e quelli che si muovono lungo linee rette, correndo avanti e indietro, compiranno nei medesimi tempi i singoli periodi di andata e di ritorno.**

**[S10.04]** Infatti, ferme restando le cose della proposizione precedente, la forza SV, con cui il corpo Q che ruota in un piano qualsiasi PQR è tirato verso il centro S, è come la distanza SQ; e perciò, essendo proporzionali SV e SQ, TV e CQ, la forza TV, con cui il corpo è tirato verso il punto C dato nel piano dell’orbita, è come la distanza CQ. Le forze con cui i corpi che si trovano nel piano PQR sono tirati verso il punto C sono dunque, in proporzione alle distanze, uguali alle forze con cui i corpi sono tirati da ogni parte verso il centro S; e perciò i corpi si muoveranno negli stessi tempi e nelle stesse figure in un piano qualsiasi PQR intorno al punto C e negli spazi liberi intorno al centro S; e perciò (per il Cor. 2 della Prop. X e il Cor. 2 della Prop. XXXVIII), in tempi sempre uguali, o descriveranno ellissi in quel piano intorno al centro C, o compiranno i periodi del moto avanti e indietro lungo linee rette condotte in quel piano per il centro C. C.V.D.

### Scolio (superfici di rivoluzione)

**[S10.05]** Affini a questi sono le salite e le discese dei corpi su superfici curve. Immagina che si descrivano linee curve in un piano, che poi esse ruotino intorno ad assi dati qualsiasi passanti per il centro delle forze e con questa rotazione descrivano superfici curve; e che i corpi si muovano in modo che i loro centri si trovino sempre su queste superfici. Se quei corpi, salendo e scendendo obliquamente, corrono avanti e indietro, i loro moti si compiranno in piani passanti per l’asse, e quindi lungo le linee curve dalla cui rotazione sono state generate quelle superfici curve. In questi casi, dunque, basta considerare il moto lungo queste linee curve.

### Proposizione XLVIII. Teorema XVI (cicloide fuori del globo)

**[S10.06]** **Se una ruota poggia ad angoli retti sulla superficie esterna di un globo e, girando come fanno le ruote, avanza lungo un cerchio massimo, la lunghezza del cammino curvilineo che un punto qualsiasi dato sul perimetro della ruota ha percorso da quando ha toccato il globo (e che si può chiamare cicloide o epicicloide) starà al doppio del seno verso della metà dell’arco che da quel momento, nel suo andare, ha toccato il globo, come la somma dei diametri del globo e della ruota sta al semidiametro del globo.**

### Proposizione XLIX. Teorema XVII (cicloide dentro il globo)

**[S10.07]** **Se una ruota poggia ad angoli retti sulla superficie interna di un globo concavo e, girando, avanza lungo un cerchio massimo, la lunghezza del cammino curvilineo che un punto qualsiasi dato sul perimetro della ruota ha percorso da quando ha toccato il globo starà al doppio del seno verso della metà dell’arco che per tutto questo tempo, nel suo andare, ha toccato il globo, come la differenza dei diametri del globo e della ruota sta al semidiametro del globo.**

**[S10.08]** Sia ABL il globo, C il suo centro, BPV la ruota che poggia su di esso, E il centro della ruota, B il punto di contatto e P il punto dato sul perimetro della ruota. Immagina che questa ruota proceda lungo il cerchio massimo ABL da A, per B, verso L, e che nel suo andare giri in modo che gli archi AB, PB siano sempre uguali fra loro, e che il punto P dato sul perimetro della ruota descriva intanto il cammino curvilineo AP. Sia AP l’intero cammino curvilineo descritto da quando la ruota ha toccato il globo in A: la lunghezza AP di questo cammino starà al doppio del seno verso dell’arco ½PB come 2CE sta a CB. Infatti la retta CE (prolungata, se occorre) incontri la ruota in V; si congiungano CP, BP, EP, VP, e sul prolungamento di CP si abbassi la normale VF. PH e VH, che si incontrano in H, tocchino il cerchio in P e in V; PH tagli VF in G, e su VP si abbassino le normali GI, HK. Ancora, con centro C e raggio qualsiasi si descriva il cerchio nom, che tagli la retta CP in n, il perimetro BP della ruota in o e il cammino curvilineo AP in m; e con centro V e raggio Vo si descriva un cerchio che tagli in q il prolungamento di VP.

**[S10.09]** Poiché la ruota, nel suo andare, gira sempre intorno al punto di contatto B, è manifesto che la retta BP è perpendicolare alla linea curva AP che il punto P della ruota descrive, e quindi che la retta VP toccherà questa curva nel punto P. Il raggio del cerchio nom, accresciuto o diminuito a poco a poco, diventi infine uguale alla distanza CP; e, per la similitudine della figura evanescente Pnomq e della figura PFGVI, il rapporto ultimo delle lineette evanescenti Pm, Pn, Po, Pq, cioè il rapporto dei cambiamenti momentanei della curva AP, della retta CP, dell’arco circolare BP e della retta VP, sarà lo stesso di quello delle linee PV, PF, PG, PI rispettivamente. Ma poiché VF è perpendicolare a CF e VH a CV, e perciò gli angoli HVG, VCF sono uguali, e l’angolo VHG (poiché gli angoli del quadrilatero HVEP in V e in P sono retti) è uguale all’angolo CEP, i triangoli VHG, CEP saranno simili; e di qui risulterà: come EP sta a CE, così HG sta a HV, o HP, e così KI sta a KP; e, componendo o dividendo, come CB sta a CE così PI sta a PK; e, raddoppiando i conseguenti, come CB sta a 2CE così PI sta a PV, e così Pq sta a Pm. Il decremento della linea VP, cioè l’incremento della linea BV − VP, sta dunque all’incremento della linea curva AP nel rapporto dato di CB a 2CE; e perciò (per il corollario del Lemma IV) le lunghezze BV − VP e AP, generate da quegli incrementi, sono nello stesso rapporto. Ma, se BV è il raggio, VP è il coseno dell’angolo BVP, ossia ½BEP, e perciò BV − VP è il seno verso dello stesso angolo; e perciò in questa ruota, il cui raggio è ½BV, BV − VP sarà il doppio del seno verso dell’arco ½BP. Dunque AP sta al doppio del seno verso dell’arco ½PB come 2CE sta a CB. C.V.D.

**[S10.10]** Per distinguerle, chiameremo la linea AP della prima proposizione cicloide fuori del globo, e l’altra, della seconda, cicloide dentro il globo.

**[S10.11]** *Cor. 1.* Di qui, se si descrive l’intera cicloide ASL e la si divide a metà in S, la lunghezza della parte PS starà alla lunghezza VP (che è il doppio del seno dell’angolo VBP, se EB è il raggio) come 2CE sta a CB, e perciò in un rapporto dato.

**[S10.12]** *Cor. 2.* E la lunghezza del semiperimetro AS della cicloide sarà uguale alla linea retta che sta al diametro BV della ruota come 2CE sta a CB.

### Proposizione L. Problema XXXIII (pendolo che oscilla in una cicloide data)

**[S10.13]** **Fare in modo che un corpo pendolo oscilli in una cicloide data.**

**[S10.14]** Dentro il globo QVS, descritto con centro C, sia data la cicloide QRS, divisa a metà in R, che con i suoi punti estremi Q e S incontra da una parte e dall’altra la superficie del globo. Si conduca CR, che divida a metà l’arco QS in O, e la si prolunghi fino ad A, in modo che CA stia a CO come CO sta a CR. Con centro C e raggio CA si descriva il globo esterno DAF, e dentro questo globo, per mezzo di una ruota il cui diametro sia AO, si descrivano due semicicloidi AQ, AS, che tocchino il globo interno in Q e in S e incontrino il globo esterno in A. Da quel punto A penda il corpo T a un filo APT uguale in lunghezza ad AR, e oscilli fra le semicicloidi AQ, AS in modo che, ogni volta che il pendolo si allontana dalla perpendicolare AR, il filo si adagi con la sua parte superiore AP sulla semicicloide APS verso la quale si compie il moto e si pieghi intorno a essa come intorno a un ostacolo, mentre la parte restante PT, alla quale la semicicloide non si oppone ancora, si stenda in linea retta: il peso T oscillerà nella cicloide data QRS. C.V.F.

**[S10.15]** Il filo PT incontri infatti la cicloide QRS in T e il cerchio QOS in V, e si conduca CV; e sulla parte rettilinea PT del filo, dai suoi estremi P e T, si innalzino le perpendicolari BP, TW, che incontrino la retta CV in B e W. Dalla costruzione e dalla generazione delle figure simili AS, SR è chiaro che quelle perpendicolari PB, TW staccano da CV le lunghezze VB, VW, uguali ai diametri OA, OR delle ruote. TP sta dunque a VP (doppio del seno dell’angolo VBP, se ½BV è il raggio) come BW sta a BV, ossia come AO + OR sta ad AO, cioè (poiché CA a CO, CO a CR e, dividendo, AO a OR sono proporzionali) come CA + CO sta a CA, o, se si divide a metà BV in E, come 2CE sta a CB. Di conseguenza (per il Cor. 1 della Prop. XLIX) la lunghezza della parte rettilinea PT del filo è sempre uguale all’arco PS della cicloide, e il filo intero APT è sempre uguale alla metà APS della cicloide, cioè (per il Cor. 2 della Prop. XLIX) alla lunghezza AR. E perciò, viceversa, se il filo resta sempre uguale alla lunghezza AR, il punto T si muoverà nella cicloide data QRS. C.V.D.

**[S10.16]** *Cor.* Il filo AR è uguale alla semicicloide AS, e perciò ha con il semidiametro AC del globo esterno lo stesso rapporto che la semicicloide SR, simile a essa, ha con il semidiametro CO del globo interno.

### Proposizione LI. Teorema XVIII (isocronismo del pendolo cicloidale)

**[S10.17]** **Se la forza centripeta che tende da ogni parte al centro C di un globo è, nei singoli luoghi, come la distanza di ciascun luogo dal centro, e per l’azione di questa sola forza il corpo T oscilla (nel modo ora descritto) sul perimetro della cicloide QRS, dico che i tempi delle oscillazioni, per quanto disuguali, saranno uguali.**

**[S10.18]** Infatti sulla tangente TW della cicloide, prolungata all’infinito, cada la perpendicolare CX, e si congiunga CT. Poiché la forza centripeta con cui il corpo T è spinto verso C è come la distanza CT, e questa (per il Cor. II delle Leggi) si scompone nelle parti CX, TX, delle quali CX, spingendo il corpo direttamente via da P, tende il filo PT e, per la resistenza di questo, si annulla del tutto senza produrre alcun altro effetto, mentre l’altra parte, TX, sollecitando il corpo trasversalmente, cioè verso X, accelera direttamente il suo moto nella cicloide, è manifesto che l’accelerazione del corpo, proporzionale a questa forza acceleratrice, è in ogni istante come la lunghezza TX, cioè, essendo date CV, WV, e proporzionali a esse TX, TW, come la lunghezza TW, cioè (per il Cor. 1 della Prop. XLIX) come la lunghezza dell’arco TR della cicloide. Se dunque due pendoli APT, Apt vengono allontanati in misura disuguale dalla perpendicolare AR e lasciati andare insieme, le loro accelerazioni saranno sempre come gli archi da descrivere TR, tR. Ma le parti descritte all’inizio sono come le accelerazioni, cioè come gli archi interi da descrivere all’inizio; e perciò le parti che restano da descrivere, e le accelerazioni successive, proporzionali a queste parti, sono anch’esse come gli interi; e così di seguito. Le accelerazioni, dunque, e quindi le velocità generate, le parti descritte con queste velocità e le parti da descrivere sono sempre come gli interi; e perciò le parti da descrivere, conservando fra loro un rapporto dato, svaniranno insieme, cioè i due corpi oscillanti giungeranno insieme alla perpendicolare AR. E poiché, a loro volta, le salite dei pendoli dal luogo più basso R, compiute con moto retrogrado lungo gli stessi archi cicloidali, sono ritardate nei singoli luoghi dalle stesse forze dalle quali erano accelerate le discese, è chiaro che le velocità delle salite e delle discese compiute lungo gli stessi archi sono uguali, e che perciò esse avvengono in tempi uguali; e perciò, essendo simili e uguali le due parti RS e RQ della cicloide, che giacciono dall’una e dall’altra parte della perpendicolare, i due pendoli compiranno sempre negli stessi tempi le loro oscillazioni, sia intere sia dimezzate. C.V.D.

**[S10.19]** *Cor.* La forza con cui il corpo T, in un luogo qualsiasi T, è accelerato o ritardato nella cicloide sta al peso totale dello stesso corpo nel luogo più alto S o Q come l’arco TR della cicloide sta al suo arco SR o QR.

### Proposizione LII. Problema XXXIV (velocità e tempi del pendolo cicloidale)

**[S10.20]** **Determinare sia le velocità dei pendoli nei singoli luoghi, sia i tempi in cui si compiono tanto le oscillazioni intere quanto le singole parti delle oscillazioni.**

**[S10.21]** Con centro in un punto qualsiasi G e raggio GH uguale all’arco RS della cicloide, descrivi il semicerchio HKM, diviso a metà dal semidiametro GK. E se una forza centripeta proporzionale alle distanze dei luoghi dal centro tende al centro G ed è, sul perimetro HIK, uguale alla forza centripeta che, sul perimetro del globo QOS, tende al centro di questo; e se, nello stesso tempo in cui il pendolo T viene lasciato andare dal luogo più alto S, un corpo L cade da H verso G: poiché le forze da cui i corpi sono sollecitati sono uguali all’inizio e sempre proporzionali agli spazi da descrivere TR, LG, e perciò, se TR e LG sono uguali, sono uguali nei luoghi T e L, è chiaro che quei corpi descrivono all’inizio spazi uguali ST, HL, e quindi continuano in seguito a essere sollecitati in egual misura e a descrivere spazi uguali. Perciò (per la Prop. XXXVIII) il tempo in cui il corpo descrive l’arco ST sta al tempo di una oscillazione come l’arco HI, tempo in cui il corpo H giungerà in L, sta alla semicirconferenza HKM, tempo in cui il corpo H giungerà in M. E la velocità del corpo pendolo nel luogo T sta alla sua velocità nel luogo più basso R (cioè la velocità del corpo H nel luogo L sta alla sua velocità nel luogo G, ossia l’incremento momentaneo della linea HL sta all’incremento momentaneo della linea HG, mentre gli archi HI, HK crescono con flusso uniforme) come l’ordinata LI sta al raggio GK, ossia come √(SR² − TR²) sta a SR. Di qui, poiché nelle oscillazioni disuguali si descrivono in tempi uguali archi proporzionali agli archi interi delle oscillazioni, dai tempi dati si hanno sia le velocità sia gli archi descritti in tutte le oscillazioni. Erano queste le prime cose da trovare.

**[S10.22]** Oscillino ora corpi appesi a fili in cicloidi diverse descritte dentro globi diversi, le cui forze assolute sono anch’esse diverse; e, se la forza assoluta di un globo qualsiasi QOS si chiama V, la forza acceleratrice da cui il pendolo è sollecitato sulla circonferenza di questo globo, quando comincia a muoversi direttamente verso il suo centro, sarà come la distanza del corpo pendolo da quel centro e la forza assoluta del globo considerate congiuntamente, cioè come CO × V. Perciò la lineetta HY, che sia come questa forza acceleratrice CO × V, sarà descritta in un tempo dato; e, se si innalza la normale YZ, che incontri la circonferenza in Z, l’arco nascente HZ rappresenterà quel tempo dato. Ma questo arco nascente HZ è in rapporto subduplicato del rettangolo GHY, e perciò come √(GH × CO × V). Di qui il tempo di un’oscillazione intera nella cicloide QRS (poiché è direttamente come la semicirconferenza HKM, che rappresenta quell’oscillazione intera, e inversamente come l’arco HZ, che rappresenta similmente il tempo dato) risulterà direttamente come GH e inversamente come √(GH × CO × V), cioè, essendo uguali GH e SR, come √(SR/(CO × V)), ossia (per il corollario della Prop. L) come √(AR/(AC × V)). Perciò le oscillazioni compiute in tutti i globi e in tutte le cicloidi, con forze assolute qualsiasi, sono nel rapporto composto dal rapporto subduplicato della lunghezza del filo, direttamente, dal rapporto subduplicato della distanza fra il punto di sospensione e il centro del globo, inversamente, e dal rapporto subduplicato della forza assoluta del globo, anch’esso inversamente. C.V.T.

**[S10.23]** *Cor. 1.* Di qui si possono anche confrontare fra loro i tempi dei corpi che oscillano, che cadono e che ruotano. Infatti, se il diametro della ruota con cui si descrive la cicloide dentro il globo si pone uguale al semidiametro del globo, la cicloide diventerà una linea retta passante per il centro del globo, e l’oscillazione sarà ormai una discesa e una successiva salita lungo questa retta. Di qui è dato sia il tempo della discesa da un luogo qualsiasi fino al centro, sia il tempo, uguale a questo, in cui un corpo, ruotando uniformemente intorno al centro del globo a una distanza qualsiasi, descrive un arco di un quarto di cerchio. Questo tempo infatti (per il secondo caso) sta al tempo di una mezza oscillazione in una cicloide qualsiasi QRS come 1 sta a √(AR/AC).

**[S10.24]** *Cor. 2.* Di qui seguono anche i risultati che Wren e Huygens hanno trovato sulla cicloide comune. Infatti, se il diametro del globo si accresce all’infinito, la sua superficie sferica si muterà in un piano, la forza centripeta agirà uniformemente lungo linee perpendicolari a questo piano, e la nostra cicloide si trasformerà nella cicloide comune. In questo caso, poi, la lunghezza dell’arco di cicloide fra quel piano e il punto che descrive diventerà uguale al quadruplo del seno verso della metà dell’arco della ruota fra lo stesso piano e il punto che descrive, come trovò Wren; e un pendolo posto fra due cicloidi di questo tipo oscillerà in tempi uguali in una cicloide simile e uguale, come dimostrò Huygens. Ma anche la discesa dei gravi nel tempo di una oscillazione sarà quella che Huygens indicò.

**[S10.25]** Le proposizioni da noi dimostrate si adattano poi alla vera costituzione della Terra, in quanto le ruote, procedendo lungo i suoi cerchi massimi, descrivono con il moto dei chiodi infissi nei loro perimetri cicloidi fuori del globo; e i pendoli sospesi più in basso, nelle miniere e nelle caverne della Terra, devono oscillare in cicloidi dentro i globi, perché tutte le oscillazioni riescano isocrone. Infatti la gravità (come si insegnerà nel Libro III) decresce allontanandosi dalla superficie della Terra: verso l’alto in rapporto duplicato delle distanze dal suo centro, verso il basso in rapporto semplice.

### Proposizione LIII. Problema XXXV (forze che rendono isocrone le oscillazioni su una curva data)

**[S10.26]** **Ammesse le quadrature delle figure curvilinee, trovare le forze per effetto delle quali i corpi compiranno in linee curve date oscillazioni sempre isocrone.**

**[S10.27]** Oscilli il corpo T in una linea curva qualsiasi STRQ, il cui asse AR passi per il centro delle forze C. Si conduca TX, che tocchi quella curva in un luogo qualsiasi T del corpo, e su questa tangente TX si prenda TY uguale all’arco TR. La lunghezza di quell’arco, infatti, si conosce dalle quadrature delle figure con i metodi comuni. Dal punto Y si conduca la retta YZ perpendicolare alla tangente. Si conduca CT, che incontri quella perpendicolare in Z: la forza centripeta sarà proporzionale alla retta TZ. C.V.T.

**[S10.28]** Infatti, se la forza con cui il corpo è tirato da T verso C si rappresenta con la retta TZ, presa proporzionale a essa, questa si scomporrà nelle forze TY, YZ; di queste, YZ, tirando il corpo secondo la lunghezza del filo PT, non muta in nulla il suo moto, mentre l’altra forza, TY, accelera o ritarda direttamente il suo moto nella curva STRQ. Di conseguenza, poiché questa forza è come il cammino da descrivere TR, le accelerazioni o i ritardi del corpo, nel descrivere parti proporzionali di due oscillazioni (una maggiore e una minore), saranno sempre come quelle parti, e perciò faranno sì che quelle parti siano descritte insieme. Ma i corpi che descrivono insieme parti sempre proporzionali agli interi descriveranno insieme gli interi. C.V.D.

**[S10.29]** *Cor. 1.* Di qui, se il corpo T, appeso con un filo rettilineo AT al centro A, descrive l’arco circolare STRQ, e intanto è sollecitato verso il basso, lungo linee parallele, da una forza che stia alla forza uniforme della gravità come l’arco TR sta al suo seno TN, i tempi delle singole oscillazioni saranno uguali. Infatti, essendo parallele TZ e AR, i triangoli ATN, ZTY saranno simili; e perciò TZ starà ad AT come TY sta a TN; cioè, se la forza uniforme della gravità si rappresenta con la lunghezza data AT, la forza TZ, per effetto della quale le oscillazioni riusciranno isocrone, starà alla forza di gravità AT come l’arco TR, uguale a TY, sta al seno TN di quell’arco.

**[S10.30]** *Cor. 2.* E perciò negli orologi, se le forze impresse dal meccanismo sul pendolo per conservarne il moto possono comporsi con la forza di gravità in modo che la forza totale verso il basso sia sempre come la linea che si ottiene applicando al seno TN il rettangolo formato dall’arco TR e dal raggio AR, tutte le oscillazioni saranno isocrone.

### Proposizione LIV. Problema XXXVI (tempi di discesa e di salita lungo curve date)

**[S10.31]** **Ammesse le quadrature delle figure curvilinee, trovare i tempi in cui i corpi, per effetto di una forza centripeta qualsiasi, scenderanno e saliranno lungo linee curve qualsiasi descritte in un piano passante per il centro delle forze.**

**[S10.32]** Scenda il corpo da un luogo qualsiasi S lungo una linea curva qualsiasi STtR, data in un piano passante per il centro delle forze C. Si congiunga CS e la si divida in innumerevoli parti uguali, e sia Dd una di queste parti. Con centro C e raggi CD, Cd si descrivano i cerchi DT, dt, che incontrino la linea curva STtR in T e t. E, data sia la legge della forza centripeta sia l’altezza CS da cui il corpo è caduto, sarà data (per la Prop. XXXIX) la velocità del corpo in qualsiasi altra altezza CT. Il tempo in cui il corpo descrive la lineetta Tt è poi come la lunghezza di questa lineetta, cioè come la secante dell’angolo tTC, direttamente, e come la velocità, inversamente. Sia proporzionale a questo tempo l’ordinata DN, perpendicolare alla retta CS nel punto D; ed essendo data Dd, il rettangolo Dd × DN, cioè l’area DNnd, sarà proporzionale allo stesso tempo. Dunque, se PNn è la linea curva che il punto N tocca di continuo, e il suo asintoto è la retta SQ, perpendicolare alla retta CS, l’area SQPND sarà proporzionale al tempo in cui il corpo, scendendo, ha descritto la linea ST; e perciò, trovata quell’area, sarà dato il tempo. C.V.T.

### Proposizione LV. Teorema XIX (legge delle aree per la traccia del moto su una superficie)

**[S10.33]** **Se un corpo si muove su una superficie curva qualsiasi il cui asse passa per il centro delle forze, e dal corpo si abbassa sull’asse una perpendicolare, e da un punto qualsiasi dell’asse si conduce una retta parallela e uguale a essa, dico che quella parallela descriverà un’area proporzionale al tempo.**

**[S10.34]** Sia BKL la superficie curva, T il corpo che ruota su di essa, STR la traiettoria che il corpo descrive su di essa, S l’inizio della traiettoria, OMK l’asse della superficie curva, TN la retta condotta dal corpo perpendicolarmente all’asse, OP la retta parallela e uguale a questa condotta dal punto O dato sull’asse; AP la traccia della traiettoria descritta dal punto P nel piano AOP della linea rotante OP; A l’inizio della traccia, corrispondente al punto S; TC la retta condotta dal corpo al centro; TG la sua parte proporzionale alla forza centripeta con cui il corpo è sollecitato verso il centro C; TM la retta perpendicolare alla superficie curva; TI la sua parte proporzionale alla forza di pressione con cui il corpo preme la superficie e, a sua volta, è premuto dalla superficie verso M; PTF la retta parallela all’asse passante per il corpo, e GF, IH le rette abbassate perpendicolarmente dai punti G e I su quella parallela PHTF.

**[S10.35]** Dico ora che l’area AOP, descritta dal raggio OP dall’inizio del moto, è proporzionale al tempo. Infatti la forza TG (per il Cor. II delle Leggi) si scompone nelle forze TF, FG, e la forza TI nelle forze TH, HI; ma le forze TF, TH, agendo lungo la linea PF perpendicolare al piano AOP, mutano soltanto il moto del corpo in quanto è perpendicolare a questo piano. E perciò il suo moto in quanto si compie secondo la posizione del piano, cioè il moto del punto P con cui la traccia AP della traiettoria è descritta in questo piano, è lo stesso che si avrebbe se le forze TF, TH fossero tolte e il corpo fosse mosso dalle sole forze FG, HI; cioè lo stesso che si avrebbe se il corpo descrivesse la curva AP nel piano AOP per effetto di una forza centripeta che tende al centro O ed è uguale alla somma delle forze FG e HI. Ma per effetto di una tale forza l’area AOP sarà descritta (per la Prop. I) proporzionale al tempo. C.V.D.

**[S10.36]** *Cor.* Con lo stesso argomento, se un corpo, mosso da forze che tendono a due o più centri posti in una stessa retta data qualsiasi CO, descrivesse nello spazio libero una linea curva qualsiasi ST, l’area AOP sarebbe sempre proporzionale al tempo.

### Proposizione LVI. Problema XXXVII (traiettoria su una superficie di rivoluzione)

**[S10.37]** **Ammesse le quadrature delle figure curvilinee, e date sia la legge della forza centripeta che tende a un centro dato, sia la superficie curva il cui asse passa per quel centro, si deve trovare la traiettoria che un corpo descriverà su quella superficie partendo da un luogo dato, con una velocità data, verso una direzione data su quella superficie.**

**[S10.38]** Ferme restando le costruzioni della proposizione precedente, il corpo T parta dal luogo dato S, lungo una retta data di posizione, nella traiettoria da trovare STR, la cui traccia nel piano BLO sia AP. E dalla velocità data del corpo all’altezza SC sarà data la sua velocità a qualsiasi altra altezza TC. Con quella velocità, in un tempo dato piccolissimo, il corpo descriva la particella Tt della sua traiettoria, e sia Pp la sua traccia descritta nel piano AOP. Si congiunga Op, e la traccia nel piano AOP del cerchietto descritto sulla superficie curva con centro T e raggio Tt sia l’ellisse pQ. Ed essendo dato di grandezza il cerchietto Tt, e data la sua distanza TN, o PO, dall’asse CO, quell’ellisse PQ sarà data di forma e di grandezza, e anche di posizione rispetto alla retta PO. E poiché l’area POp è proporzionale al tempo, e perciò è data dal tempo dato, sarà dato l’angolo POp. E di qui sarà data l’intersezione comune p dell’ellisse e della retta, insieme con l’angolo OPp sotto cui la traccia APp della traiettoria taglia la linea OP. Di qui, poi (confrontando la Prop. XLI con il suo Cor. 2), appare facilmente il modo di determinare la curva APp. Poi, innalzando dai singoli punti P della traccia le perpendicolari PT al piano AOP, che incontrino la superficie curva in T, saranno dati i singoli punti T della traiettoria. C.V.T.

---

## Apparato

### A.0 Estensioni del glossario

I termini seguenti non comparivano nel glossario comune. Ognuno è reso in modo costante in tutto il fascicolo.

| Latino | Italiano | Motivazione |
|---|---|---|
| *altitudo* | «altezza» | In queste sezioni è la distanza del corpo dal centro delle forze, non un’altezza verticale. Si conserva il termine di Newton (Motte: *altitude*) e lo si spiega in nota N2. |
| *apsis summa / ima* | «apside superiore / inferiore» | Il glossario fissa «apside, apsidi»; in italiano il termine è femminile («l’apside», «le apsidi»). *Summa* e *ima* indicano il punto di massima e di minima distanza dal centro; «superiore / inferiore» corrisponde all’uso astronomico italiano e a Motte (*upper / lower apsis*). |
| *orbis revolvens / quiescens / mobilis / immobilis* | «orbita rotante / in quiete / mobile / immobile» | *Orbis* è «orbita» secondo il glossario; gli aggettivi sono resi alla lettera, perché Newton li alterna senza differenza di senso. |
| *motus angularis*; *motus transversus* | «moto angolare»; «moto trasversale» | Termini tecnici della Prop. XLIV; il moto trasversale è la componente perpendicolare al raggio. |
| *lineola* | «lineetta» | Diminutivo di *linea*, usato per segmenti nascenti o evanescenti. «Lineetta» conserva il diminutivo senza introdurre «infinitesimo». |
| *vicissim* (nelle proporzioni) | «permutando» | Termine euclideo: da A : B = C : D si passa ad A : C = B : D (Prop. XLV, Es. 1–3). Fuori dalle proporzioni (*& propterea vicissim*, Prop. L) è reso «viceversa». |
| *composite vel divisim*; *divisim* | «componendo o dividendo»; «dividendo» | Termini euclidei delle proporzioni (Prop. XLIX, L). |
| *dignitas*; *index dignitatis* | «potenza»; «indice della potenza» | *Dignitas* è il termine del Seicento per la potenza algebrica; l’indice è l’esponente (nota N5). |
| *latus quadrato-quadratum* | «radice quarta» | Alla lettera «lato del quadrato-quadrato»: il lato di cui il numero è la quarta potenza. Motte: *biquadrate root*. |
| *series convergentes*; *methodus nostra serierum* | «serie convergenti»; «il nostro metodo delle serie» | Newton rimanda al proprio sviluppo binomiale. |
| *vis extranea* | «forza estranea» | Forza aggiunta o tolta alla forza principale (Prop. XLV, Cor. 2); Motte *foreign force*. |
| *vis inertiæ* | «forza d’inerzia» | Coerente con la Def. III (*vis insita … sive vis inertiæ*). |
| *rectangulum* (di due linee) | «rettangolo» | È il prodotto di due segmenti; si scrive mk × ms. |
| *applicare rectangulum ad lineam* | «applicare il rettangolo alla linea» | Termine classico per la divisione di un’area per un segmento (Prop. LIII, Cor. 2); spiegato in nota N16. |
| *cyclois*, *epicyclois*, *semicyclois* | «cicloide», «epicicloide», «semicicloide» | Termini tecnici; per la Sez. X Newton chiama «cicloide fuori / dentro il globo» le curve oggi dette epicicloide e ipocicloide (nota N12). |
| *rota*; *globus*; *circulus maximus* | «ruota»; «globo»; «cerchio massimo» | Alla lettera; *globus* è nel glossario. |
| *corpus pendulum*; *funipendula corpora*; *perpendiculum* | «corpo pendolo»; «corpi appesi a fili»; «perpendicolare» | *Funependulum* e *corpus funependulum* seguono il glossario. *Perpendiculum AR* è la retta verticale (il «filo a piombo») per il punto di sospensione: si rende «perpendicolare AR», perché la forza qui è centrale e non uniforme. In *ascensus perpendiculorum* (Prop. LI) *perpendicula* sono i pendoli stessi, e così è tradotto. |
| *motus reciprocus* (titolo della Sez. X) | «moto alterno» | Moto di andata e ritorno; Motte *reciprocal motion*. |
| *ultro citroque* | «avanti e indietro» | Locuzione avverbiale. |
| *isochronus* | «isocrono» | Termine tecnico (Prop. LIII). |
| *vestigium* | «traccia» | Nelle Prop. LV–LVI è la proiezione ortogonale della traiettoria sul piano AOP, perpendicolare all’asse. «Traccia» conserva l’immagine del latino; Motte interpreta (*orthographic projection*). |
| *linea volubilis* | «linea rotante» | La retta OP, che ruota intorno all’asse. |
| *vis pressionis* | «forza di pressione» | Reazione della superficie (Prop. LV). |
| *circellus* | «cerchietto» | Diminutivo (Prop. LVI). |
| *secans* | «secante» | La funzione trigonometrica (Prop. LIV). |
| *plaga* (Prop. LVI, *versus plagam datam*) | «direzione» | Il Fascicolo 3 rende *plaga* con «verso / parte» in contesti di versi contrapposti; qui indica la direzione iniziale del moto sulla superficie. |
| *concessis figurarum curvilinearum quadraturis* | «ammesse le quadrature delle figure curvilinee» | Formula ricorrente (Prop. XLVI, LIII, LIV, LVI): si suppone di saper calcolare le aree, cioè gli integrali. |
| *specie & magnitudine datus* | «dato di forma e di grandezza» | Applicazione del glossario. |

### A.1 Titoli delle sezioni

**Sezione IX.** *De motu corporum in orbibus mobilibus, deque motu apsidum.* — Motte: “Of the motion of bodies in moveable orbits; and of the motion of the apsides.” Resa: «Il moto dei corpi in orbite mobili, e il moto delle apsidi».

**Sezione X.** *De motu corporum in superficiebus datis, deque funipendulorum motu reciproco.* — Motte: “Of the motion of bodies in given superficies, and of the reciprocal motion of funependulous bodies.” Resa: «Il moto dei corpi su superfici date, e il moto alterno dei pendoli a filo». La trascrizione ha la grafia *funipendulorum* (così anche nella Prop. LII, *funipendula corpora*); il brief cita *funependulorum*. Le due grafie si equivalgono e la traduzione non cambia; la forma della stampa del 1726 resta da verificare.

### A.2 Proposizione XLIII

**Latino:** *Efficiendum est ut corpus in trajectoria quacunque circa centrum virium revolvente perinde moveri possit, atque corpus aliud in eadem trajectoria quiescente.*

**Inglese:** “It is required to make a body move in a trajectory that revolves about the centre of force in the same manner as another body in the same trajectory at rest.”

**Scelte.**

- *perinde … atque* è reso «esattamente come»: Newton vuole lo stesso moto relativo all’orbita, non un moto simile.
- *cogente justæ quantitatis vi centripeta* è reso «sotto l’azione di una forza centripeta di giusta quantità», cioè di intensità opportuna.
- *velocitas lineæ describentis Cp* è reso «la velocità della linea Cp che descrive»: è la velocità angolare del raggio vettore.
- *per corollarium quintum propositionis vi*: «per il Cor. 5 della Prop. VI» (la forza dalla curva e dalla legge delle aree).
- **Motte:** «may be made to describe an immovable plane» omette «in» (*in plano immobili*); «its (revolving) arc up» aggiunge «revolving» tra parentesi.

### A.3 Proposizione XLIV e corollari

**Latino:** *Differentia virium, quibus corpus in orbe quiescente, & corpus aliud in eodem orbe revolvente æqualiter moveri possunt, est in triplicata ratione communis altitudinis inverse.*

**Inglese:** “The difference of the forces, by which two bodies may be made to move equally, one in a quiescent, the other in the same orbit revolving, is in a triplicate ratio of their common altitudes inversely.”

**Scelte.**

- *æqualiter moveri* è reso «muoversi allo stesso modo», come nella Prop. XLIII (*perinde moveri*).
- *est in triplicata ratione … inverse*: «è inversamente in rapporto triplicato», cioè come 1/A³ (nota N2).
- La lunga dimostrazione è un unico capoverso nel latino; nella traduzione è divisa in tre capoversi (S9.04–S9.06) senza omettere frasi.
- *Capiatur autem angulum pCn*: l’accusativo con il passivo *capiatur* è un **refuso probabile della trascrizione** per *angulus*; tradotto secondo il senso, da verificare sulla stampa.
- *ipsius actione* (S9.05) è riferito alla differenza delle forze: «per azione di essa».
- *in consequentia / in antecedentia* compaiono qui per la prima volta nel fascicolo: «in conseguenza / in antecedenza», spiegati in nota N1.
- *Est & mt directe ut ½mt* (trascrizione «12mt»): l’affermazione sembra tautologica, ma serve a dire che mt, quasi un diametro del cerchio di raggio Ck, è come l’altezza pC. Motte ha la stessa lettura (SVG 158).
- **Cor. 1.** Il punto **R** non è definito nel testo: dal contesto è il punto della retta CP alla distanza CK da C, cioè l’origine dell’arco circolare nascente RK di centro C, il cui seno verso è rk²/(2kC). Lettura da controllare sulla figura NATP00087-102.
- **Cor. 1.** *si capiantur datæ quantitates F, G in ea ratione … quam habet angulus VCP ad angulum VCp*: F sta a G come l’angolo VCP sta all’angolo VCp, quindi G/F è il rapporto delle velocità angolari dell’orbita mobile e di quella immobile.
- **Cor. 2.** La trascrizione dà le formule appiattite: «FFAA+RGG−RFFA cub.» = FF/AA + (RGG − RFF)/A³; «FFCV quad.» = FF/CV²; «RFFCV cub.» = RFF/CV³; «1A cub. ad 1CV cub.» = 1/A³ : 1/CV³. Motte le stampa come SVG 160–168, in accordo.
- **Cor. 3.** La trascrizione ha «FFAT cub. & **FAA**T cub.+RGG−RFFA cub.». La seconda forza deve contenere la prima più il termine aggiunto, quindi va letta FFA/T³ + (RGG − RFF)/A³; così Motte (SVG 170). «FAA» è un **refuso probabile** della trascrizione, da verificare.
- **Cor. 4.** «VFFTT» = VFF/TT; «X+VRGG−VRFFA cub.» = X + (VRGG − VRFF)/A³ (Motte, SVG 171–172).
- **Cor. 6.** *quam punctum p perpetuo tangit* è reso «che il punto p tocca di continuo», cioè lungo la quale si trova sempre; Motte rende con «is continually describing». La stessa formula ricorre nella Prop. LIV.

### A.4 Proposizione XLV: enunciato ed esempi

**Latino:** *Orbium qui sunt circulis maxime finitimi requiruntur motus apsidum.*

**Inglese:** “To find the motion of the apsides in orbits approaching very near to circles.”

**Scelte.**

- *circulis maxime finitimi* è reso «vicinissime ai cerchi»; più avanti *propemodum circularis* «quasi circolare».
- *Problema solvitur arithmetice*: «si risolve aritmeticamente», cioè per confronto di espressioni algebriche e non con una costruzione geometrica. Per questo la proposizione non ha figura e non entra nella Parte B.
- *numeratores … statuendi sunt analogi*: «i numeratori … si devono porre in proporzione». *Analogus* qui significa «in analogia», cioè proporzionale.
- *conficere angulum*: «compiere un angolo», cioè percorrere un angolo al centro.
- **Es. 1, termine mancante.** La trascrizione ha «RGG−RFF+TFF ad T cub. ut **−FF** ad −3TTX+3TXX−X cub. sive ut −FF ad −3TT+3TX−XX». Il confronto dei termini non dati richiede −FFX (il numeratore dell’orbita mobile è RGG − RFF + TFF − FFX), e il passaggio successivo, «sive ut −FF ad −3TT…», è la divisione per X. Motte ha «−FFX». Ho tradotto «−FF[X]», con l’integrazione tra parentesi quadre. Da verificare sulla stampa se la X manca già nel 1726.
- **Es. 1–3, radici perdute.** La trascrizione scrive «ut 1 ad 3», «graduum 1803», «n æqualis 2», «180n», «ut 1 ad mb+ncb+c» (seconda occorrenza), «180b+cmb+nc», «180b−cmb−nc»: in tutti questi luoghi manca il segno di radice. Il controllo è aritmetico: 180/3 = 60°, non 103° 55′ 23″, mentre 180/√3 = 103,923° = 103° 55′ 23″. Motte stampa le radici (SVG 177, 178, 187, 188, 192, 202, 203, 205). Tradotto con √ (§ A.15).
- **Es. 1.** *ut ita dicam* («per così dire») accompagna «un angolo di 180 gradi»: Newton si scusa di chiamare angolo un mezzo giro.
- **Es. 2.** *integros vel fractos, rationales vel irrationales, affirmativos vel negativos*: «interi o fratti, razionali o irrazionali, positivi o negativi».
- **Es. 2.** «T−X¯n» è la notazione del vincolo (la linea sopra T − X) per la potenza (T − X)ⁿ; Motte SVG 181.
- **Es. 2.** *latus quadrato-quadratum undecimæ dignitatis*: «la radice quarta dell’undicesima potenza», cioè A^(11/4). La trascrizione ha «A114» (= A^(11/4)), «1A114», «A14A3» (= A^(1/4)/A³) e «n æqualis 14» (= 1/4).
- **Es. 3.** La trascrizione ha «effe» per *esse* (**refuso probabile**, s lunga letta f) e «b in T−X¯+c in T−X¯n», dove manca l’esponente m sul primo vincolo (appiattimento). Tradotto (b(T − X)ᵐ + c(T − X)ⁿ)/A³.
- **Es. 3.** «ponendaæ» per *ponendæ*: **refuso della trascrizione**.
- **Es. 3.** *exponendo altitudinem maximam … arithmetice per unitatem*: «rappresentando aritmeticamente con l’unità», cioè ponendo T = 1.

### A.5 Proposizione XLV: corollari; capoverso *Hactenus*

**Cor. 1.**

- La trascrizione appiattisce tutti gli esponenti: «Annmm−3» = A^(nn/mm − 3); «112» = 1½; «164−3, 116−3, 14−3, 49−3» = 1/64 − 3, 1/16 − 3, 1/4 − 3, 4/9 − 3; «A3−164» = A^(3 − 1/64); «34, 23, 13, 14» = 3/4, 2/3, 1/3, 1/4; «A169−3, A94−3» = A^(16/9 − 3), A^(9/4 − 3); «A119, A34» = A^(11/9), A^(3/4); «A−2952314641» = A^(−29523/14641); «A24243» = A^(2 + 4/243); «5934» = 59¾. Tutte le letture sono confermate dal calcolo (nota N6) e, tranne una, da Motte (SVG 206–241).
- *per exempla secunda*: «per il secondo esempio» (il plurale latino indica il gruppo di casi dell’Es. 2).
- *Sin cœperit, illud de apside discedens, vel minimum ascendere*: «se invece, partendo dall’apside, comincia a salire anche di pochissimo». Motte aggiunge «from the **lower** apsis»: l’aggiunta è coerente (un corpo che sale partendo da un’apside parte da un minimo), ma non è nel latino.
- *nunquam appellat ad centrum*: «non approda mai al centro».
- *proxime* è reso «con buona approssimazione».

**Cor. 2.**

- *vim illam extraneam esse 357.45 partibus minorem quam vis altera*: alla lettera «minore di 357,45 parti rispetto all’altra». Il senso, confermato da *c esse 100/35745*, è che la forza estranea sta all’altra come 1 a 357,45. Ho tradotto «357,45 volte minore».
- La trascrizione appiattisce «1801−c1−4c» = 180√((1 − c)/(1 − 4c)) e «1803564535345» = 180√(35645/35345). Motte SVG 243–246, in accordo.
- *ideoque apsis summa singulis revolutionibus progrediendo conficiet 1gr. 31m. 28sec.*: «a ogni rivoluzione, avanzando compirà 1° 31′ 28″».
- *Apsis lunæ est duplo velocior circiter*: «L’apside della Luna è circa due volte più veloce». Vedi nota N7.

**Capoverso *Hactenus de motu corporum*** (S9.25). Nella trascrizione e in Motte chiude la Sezione IX, prima del titolo della Sezione X; così anche qui.

- *plana … politissima & absolute lubrica*: «levigatissimi e assolutamente lisci».
- *vice planorum quibus corpora incumbunt quæque tangunt incumbendo*: «al posto dei piani sui quali i corpi poggiano e che, poggiandovi, toccano». Motte amplia: «upon which those bodies roll or slide, and which are therefore tangent planes to the bodies».
- *perpendiculares* (dei moti dei gravi) è reso «perpendicolari», cioè verticali.

### A.6 Proposizione XLVI

**Latino:** *Posita cujuscunque generis vi centripeta, datoque tum virium centro tum plano quocunque in quo corpus revolvitur, & concessis figurarum curvilinearum quadraturis: requiritur motus corporis de loco dato, data cum velocitate, secundum rectam in plano illo datam egressi.*

**Inglese:** “Any kind of centripetal force being supposed, and the centre of force, and any plane whatsoever in which the body revolves, being given, and the quadratures of curvilinear figures being allowed; it is required to determine the motion of a body going off from a given place, with a given velocity, in the direction of a given right line in that plane.”

**Scelte.**

- *secundum positionem plani*: «secondo la posizione del piano», cioè parallelamente al piano. Motte: «coinciding with the position of the plane itself».
- La frase S10.02 che termina con i due punti («… che incontri SC in T:») è seguita nel latino da *Vis SV resolvetur*; in italiano la frase successiva comincia con la minuscola.

### A.7 Proposizione XLVII e scolio

**Latino:** *Posito quod vis centripeta proportionalis sit distantiæ corporis a centro; corpora omnia in planis quibuscunque revolventia describent ellipses, & revolutiones temporibus æqualibus peragent; quæque moventur in lineis rectis, ultro citroque discurrendo, singulas eundi & redeundi periodos iisdem temporibus absolvent.*

**Inglese:** “Supposing the centripetal force to be proportional to the distance of the body from the centre; all bodies revolving in any planes whatsoever will describe ellipses, and complete their revolutions in equal times; and those which move in right lines, running backwards and forwards alternately, will complete their several periods of going and returning in the same times.”

**Scelte.**

- *pro ratione distantiarum æquales*: «in proporzione alle distanze, uguali».
- *undiquaque*: «da ogni parte».
- **Motte** aggiunge in fondo alla dimostrazione «completing the same periods of time in all cases», che riassume ma non traduce.
- **Scolio.** La trascrizione ha *Si corpora illa oblique ascendendo & descendendo* ***ocurrant*** *ultro citroque*. La forma non esiste. Il senso richiesto da *ultro citroque* è «corrono avanti e indietro» (Motte: «reciprocate to and fro»): leggo *currant*. Non escludo *occurrant* («si vanno incontro»), meno adatto al contesto. **Refuso probabile della trascrizione, da verificare sulla stampa.**

### A.8 Proposizioni XLVIII e XLIX e corollari

**Prop. XLVIII. Latino:** *Si rota globo extrinsecus ad angulos rectos insistat, & more rotarum revolvendo progrediatur in circulo maximo; longitudo itineris curvilinei, quod punctum quodvis in rotæ perimetro datum, ex quo globum tetigit, confecit, (quodque cycloidem vel epicycloidem nominare licet) erit ad duplicatum sinum versum arcus dimidii qui globum ex eo tempore inter eundem tetigit, ut summa diametrorum globi & rotæ ad semidiametrum globi.*

**Inglese:** “If a wheel stands upon the outside of a globe at right angles thereto, and revolving about its own axis goes forward in a great circle, the length of the curvilinear path which any point, given in the perimeter of the wheel, hath described since the time that it touched the globe (which curvilinear path we may call the cycloid or epicycloid), will be to double the versed sine of half the arc which since that time has touched the globe in passing over it, as the sum of the diameters of the globe and the wheel to the semi-diameter of the globe.”

**Prop. XLIX. Latino:** *Si rota globo concavo ad rectos angulos intrinsecus insistat & revolvendo progrediatur in circulo maximo; longitudo itineris curvilinei quod punctum quodvis in rotæ perimetro datum, ex quo globum tetigit, confecit, erit ad duplicatum sinum versum arcus dimidii qui globum toto hoc tempore inter eundum tetigit, ut differentia diametrorum globi & rotæ ad semidiametrum globi.*

**Inglese:** “If a wheel stand upon the inside of a concave globe at right angles thereto, and revolving about its own axis go forward in one of the great circles of the globe, the length of the curvilinear path which any point, given in the perimeter of the wheel, hath described since it touched the globe, will be to the double of the versed sine of half the arc which in all that time has touched the globe in passing over it, as the difference of the diameters of the globe and the wheel to the semi-diameter of the globe.”

**Scelte e divergenze.**

- La Prop. XLVIII non ha dimostrazione propria: la dimostrazione che segue la Prop. XLIX vale per entrambe (lo dice il capoverso S10.10, *in propositione priore … in posteriore*). Per questo la Parte B la include nell’unità della Prop. XLIX.
- **Prop. XLVIII:** la trascrizione ha *inter* ***eundem*** *tetigit*, mentre la Prop. XLIX ha *inter* ***eundum***. *Eundem* non dà senso; il gerundio *eundum* («nel suo andare») sì. **Refuso probabile della trascrizione.**
- *more rotarum revolvendo*: «girando come fanno le ruote». Motte: «revolving about its own axis», parafrasi; nella Prop. XLIX Motte aggiunge di nuovo «about its own axis» e scrive «in one of the great circles of the globe».
- *duplicatum sinum versum*: qui *duplicatus* significa «doppio» (non «duplicato» nel senso dei rapporti); la dimostrazione dice infatti *duplum sinum versum*. Tradotto «il doppio del seno verso».
- La trascrizione ha «12PB», «12BEP», «12BV» per ½PB, ½BEP, ½BV (Motte SVG 247–249). Nella frase S10.09 Newton scrive *arcus ½BP*, altrove ½PB: si conserva.
- *composite vel divisim*: «componendo o dividendo»; *duplicatis consequentibus*: «raddoppiando i conseguenti».
- *per corol. lem. iv.*: «per il corollario del Lemma IV».
- **Cor. 1.** *quæ duplus est sinus anguli VBP, existente EB radio*: «che è il doppio del seno dell’angolo VBP, se EB è il raggio».

### A.9 Proposizione L

**Latino:** *Facere ut corpus pendulum oscilletur in cycloide data.*

**Inglese:** “To cause a pendulous body to oscillate in a given cycloid.”

**Scelte.**

- *a perpendiculo AR*: «dalla perpendicolare AR» (§ A.0).
- *ceu obstaculum*: «come intorno a un ostacolo». Motte aggiunge «solid»: «as if it were some solid obstacle».
- *cum sint CA ad CO, CO ad CR & divisim AO ad OR proportionales*: tradotto alla lettera, «poiché CA a CO, CO a CR e, dividendo, AO a OR sono proporzionali». Il passaggio *divisim* dà AO : OR = CA : CO (nota N13).
- *cycloidis arcui dimidio APS*: «alla metà APS della cicloide».
- Parole spezzate dal cambio di pagina nella trascrizione: «inter vallo» (p. 147/148).

### A.10 Proposizione LI

**Latino:** *Si vis centripeta tendens undique ad globi centrum C sit in locis singulis ut distantia loci cujusque a centro, & hac sola vi agente corpus T oscilletur (modo jam descripto) in perimetro cycloidis QRS: dico quod oscillationum utcunque inæqualium æqualia erunt tempora.*

**Inglese:** “If a centripetal force tending on all sides to the centre C of a globe, be in all places as the distance of the place from the centre, and by this force alone acting upon it, the body T oscillate (in the manner above described) in the perimeter of the cycloid QRS; I say, that all the oscillations, how unequal soever in themselves, will be performed in equal times.”

**Scelte.**

- *directe a P*: «direttamente via da P».
- *ob datas CV, WV iisque proportionales TX, TW*: «essendo date CV, WV, e proporzionali a esse TX, TW». Il rapporto TX : TW = CV : WV è ricostruito senza figura in nota N14.
- *totæ*: «gli interi», cioè gli archi interi da descrivere.
- *oscillationes … tam totas quam dimidias*: «sia intere sia dimezzate».
- Parola spezzata dal cambio di pagina: «cor pus» (p. 149/150).

### A.11 Proposizione LII, corollari e capoverso sulla Terra

**Latino:** *Definire & velocitates pendulorum in locis singulis, & tempora quibus tum oscillationes totæ, tum singulæ oscillationum partes peraguntur.*

**Inglese:** “To define the velocities of the pendulums in the several places, and the times in which both the entire oscillations, and the several parts of them are performed.”

**Scelte e problemi del testo.**

- *si æquantur TR ad LG*: costrutto anomalo (*æquari ad*); inteso «se TR e LG sono uguali», come fa Motte. Forse refuso per *TR & LG*; da verificare.
- *arcus HI, tempus quo corpus H perveniet ad L*: apposizione conservata: l’arco HI «è» il tempo, perché nel moto armonico ausiliario l’arco del semicerchio cresce uniformemente.
- **Radici perdute:** «SR q.−TR q.» = √(SR² − TR²); «GH×CO×V» = √(GH × CO × V) (due volte); «SRCO×V» = √(SR/(CO × V)); «ARAC×V» = √(AR/(AC × V)); Cor. 1: «ARAC» = √(AR/AC). Motte SVG 250–255, in accordo.
- *directæ* (S10.22) per *directe*: **refuso probabile della trascrizione**.
- *Itaque oscillationes … sunt in ratione*: Newton intende i tempi delle oscillazioni; si traduce alla lettera, «le oscillazioni … sono nel rapporto».
- **Cor. 1.** *per casum secundum*: «per il secondo caso», cioè per la seconda parte della proposizione (S10.22). *arcum quadrantalem*: «un arco di un quarto di cerchio».
- **Cor. 2.** *Wrennus & Hugenius*: «Wren e Huygens», nella forma moderna. Motte aggiunge i titoli «Sir Christopher Wren», «M. Huygens». *cycloidem vulgi* / *vulgarem*: «cicloide comune». *quadruplicato sinui verso*: «al quadruplo del seno verso».
- **Capoverso *Aptantur*** (S10.25): *motu clavorum, perimetris suis infixorum*: «con il moto dei chiodi infissi nei loro perimetri». *in fodinis & cavernis*: «nelle miniere e nelle caverne». *decrescit … deorsum vero in ratione simplici*: «verso il basso in rapporto semplice» (nota N15).

### A.12 Proposizione LIII e corollari

**Latino:** *Concessis figurarum curvilinearum quadraturis, invenire vires quibus corpora in datis curvis lineis oscillationes semper isochronas peragent.*

**Inglese:** “Granting the quadratures of curvilinear figures, it is required to find the forces with which bodies moving in given curve lines may always perform their oscillations in equal times.”

**Scelte.**

- *per methodos vulgares*: «con i metodi comuni».
- *fili PT*: il filo PT non è definito in questa proposizione; Newton pensa a un corpo vincolato alla curva come nella Prop. L. Si traduce senza integrare.
- **Cor. 1.** La trascrizione ha *æqualia* ***erun*** per *erunt*: **refuso probabile della trascrizione**. *filo rectilineo AT a centro A pendens*: «appeso con un filo rettilineo AT al centro A».
- **Cor. 2.** *vires a machina … impressæ*: «le forze impresse dal meccanismo» (dell’orologio). *applicando rectangulum sub arcu TR & radio AR ad sinum TN*: «applicando al seno TN il rettangolo formato dall’arco TR e dal raggio AR», cioè (TR × AR)/TN.

### A.13 Proposizione LIV

**Latino:** *Concessis figurarum curvilinearum quadraturis, invenire tempora, quibus corpora vi qualibet centripeta in lineis quibuscunque curvis, in plano per centrum virium transeunte descriptis, descendent & ascendent.*

**Inglese:** “Granting the quadratures of curvilinear figures, it is required to find the times in which bodies by means of any centripetal force will descend or ascend in any curve lines described in a plane passing through the centre of force.”

**Scelte e problemi del testo.**

- Motte rende *descendent & ascendent* con «descend **or** ascend».
- La trascrizione ha «… altitudine CT, (per prop. xxxix.) Tempus autem …»: il punto fermo dopo la parentesi manca. Ho diviso il periodo in due frasi, come richiede il senso.
- La trascrizione ha «id est, ut secans anguli tTC) directe»: parentesi chiusa senza apertura. Probabilmente l’originale era «(ut secans anguli tTC)». Il senso non cambia.
- *ordinatim applicata DN ad rectam CS per punctum D perpendicularis*: «l’ordinata DN, perpendicolare alla retta CS nel punto D». Parole spezzate: «per pendicularis» (p. 156/157).
- *quam punctum N perpetuo tangit*: come nel Cor. 6 della Prop. XLIV, «che il punto N tocca di continuo».

### A.14 Proposizioni LV e LVI

**Prop. LV. Latino:** *Si corpus movetur in superficie quacunque curva, cujus axis per centrum virium transit, & a corpore in axem demittatur perpendicularis, eique parallela & æqualis ab axis puncto quovis ducatur: dico quod parallela illa aream tempori proportionalem describet.*

**Inglese:** “If a body move in any curve superficies, whose axis passes through the centre of force, and from the body a perpendicular be let fall upon the axis; and a line parallel and equal thereto be drawn from any given point of the axis; I say, that this parallel line will describe an area proportional to the time.”

**Prop. LVI. Latino:** *Concessis figurarum curvilinearum quadraturis, datisque tum lege vis centripetæ ad centrum datum tendentis, tum superficie curva cujus axis per centrum illud transit; invenienda est trajectoria quam corpus in eadem superficie describet, de loco dato, data cum velocitate, versus plagam in superficie illa datam egressum.*

**Inglese:** “Granting the quadratures of curvilinear figures, and supposing that there are given both the law of centripetal force tending to a given centre, and the curve superficies whose axis passes through that centre; it is required to find the trajectory which a body will describe in that superficies, when going off from a given place with a given velocity, and in a given direction in that superficies.”

**Scelte e divergenze.**

- *vestigium*: «traccia» (§ A.0). Motte: «orthographic projection», che esplicita correttamente la costruzione ma non traduce.
- *in lineæ volubilis OP plano AOP*: «nel piano AOP della linea rotante OP». Motte: «in the plane AOP in which the revolving line OP is found».
- *motus … quatenus huic plano perpendicularem*: «il moto del corpo in quanto è perpendicolare a questo piano», cioè la sua componente perpendicolare.
- **Prop. LV, Cor.** *a viribus agitatum ad centra duo vel plura in eadem quavis recta CO data tendentibus*: «mosso da forze che tendono a due o più centri posti in una stessa retta data qualsiasi CO».
- **Prop. LVI:** il latino ha *in plano* ***BLO***, Motte *in the plane* ***BDO***. La lettera D non compare altrove nelle Prop. LV–LVI; L compare in BKL (la superficie). Senza la figura NATP00087-119 non si può decidere; il piano della traccia è comunque il piano AOP. **Da verificare sulla figura.**
- **Prop. LVI:** la trascrizione ha prima *ellipsis pQ*, poi *ellipsis illa PQ*. È la stessa ellisse; probabile oscillazione tipografica fra p minuscola e P maiuscola. Motte ha «pQ» entrambe le volte. Si conserva la lettera del latino in ciascun luogo, con questa avvertenza.
- *confe rendo* è spezzato dal cambio di pagina (p. 159/160).

### A.15 Refusi e formule appiattite della trascrizione

**Refusi probabili della trascrizione** (tradotti secondo il senso; da verificare sulla stampa del 1726):

| Luogo | Trascrizione | Lettura | Nota |
|---|---|---|---|
| S9.05 | *Capiatur autem angulum pCn* | *angulus* | accusativo con passivo |
| S9.09 | *FAAT cub.* | FFA/T³ | Motte SVG 170 |
| S9.15 | *−FF ad −3TTX…* | −FF[X] | integrazione; Motte «−FFX» |
| S9.19 | *effe* | *esse* | s lunga letta f |
| S9.20 | *ponendaæ* | *ponendæ* | |
| S10.05 | *ocurrant* | *currant* (?) | forma inesistente |
| S10.06 | *inter eundem* | *inter eundum* | cfr. Prop. XLIX |
| S10.21 | *si æquantur TR ad LG* | «se TR e LG sono uguali» | costrutto anomalo |
| S10.22 | *directæ* | *directe* | |
| S10.29 | *erun* | *erunt* | |
| S10.32 | *(per prop. xxxix.) Tempus*; *tTC)* | punto mancante; parentesi spaiata | punteggiatura |
| S10.38 | *ellipsis illa PQ* | pQ | maiuscola oscillante |

**Formule appiattite** (lette come segue; tutte coerenti con Motte, salvo dove indicato nel § A.16):

- **Frazioni:** «mk×msmt» = (mk × ms)/mt; «rkq2kC» = rk²/(2kC); «FFAA» = FF/AA; «A cub.A cub.» = A³/A³; «AnA3» = Aⁿ/A³; «bAm+cAnA cub.» = (bAᵐ + cAⁿ)/A³; «nn−n2» = (nn − n)/2; «100 35745» = 100/35745.
- **Metà:** «12mt», «12PB», «12BEP», «12BV», «12BP» = ½mt, ½PB, ½BEP, ½BV, ½BP.
- **Radici perdute:** Prop. XLV, Es. 1: «1 ad 3», «1803»; Es. 2: «n æqualis 2» (= √n), «1 ad n», «180n», «1802» (= 180/√2; nel caso «1802gr. seu 90gr.» è invece 180/2, cioè 180/√4); Es. 3: «1 ad mb+ncb+c» (seconda occorrenza), «180b+cmb+nc», «180b−cmb−nc»; Cor. 2: «1801−c1−4c», «1803564535345»; Prop. LII: «SR q.−TR q.», «GH×CO×V», «SRCO×V», «ARAC×V», Cor. 1 «ARAC».
- **Esponenti:** «An−3» = Aⁿ⁻³; «T−X¯n» = (T − X)ⁿ; «A114» = A^(11/4); «A14A3» = A^(1/4)/A³; «n æqualis 14» = 1/4; «180ngr.» = 180/√n; tutti gli esponenti del Cor. 1 della Prop. XLV (§ A.5).
- **Esponente perso:** «b in T−X¯+c in T−X¯n» = b(T − X)ᵐ + c(T − X)ⁿ.
- **Numeri misti:** «112» = 1½; «5934» = 59¾; «A24243» = A^(2 + 4/243).

**Parole spezzate dal cambio di pagina** (la trascrizione inserisce il marcatore di pagina dentro la parola; nella Parte B resta lo spazio): *re perietur* (p. 131/132), *inter vallo* (147/148), *cor pus* (149/150), *per pendicularis* (156/157), *perpendi culares* (153/154), *confe rendo* (159/160).

### A.16 Riepilogo: dove Motte aggiunge, omette o sbaglia

| Luogo | Latino | Motte 1846 | Tipo |
|---|---|---|---|
| S9.02 | *in plano immobili describit* | «describe an immovable plane» | omissione di «in» |
| S9.02 | *arcum ejus up* | «its (revolving) arc up» | aggiunta |
| S9.05 | *transferri debet* | «would be carried» | modo verbale |
| S9.15 | −FF[X] : −3TTX + 3TXX − X³ | «−FFX to 3TTX + 3TXX − X3» | segno mancante davanti a 3TTX |
| S9.15 | *RGG ad T cub.* | «RGG to T2» | **errore**: T² per T³ |
| S9.18 | *ut A seu A⁴/A³* | «as or [SVG 180]» | omissione di A |
| S9.18 | *A^(11/4)* | SVG 193: A^(11/14) | **errore** di esponente |
| S9.18 | *A^(1/4)/A³* | SVG 195: A^(3/4)/A³ | **errore** di esponente |
| S9.18 | *de apside summa discedens* | «parting from [SVG 187] the upper apsis» | formula √n fuori posto |
| S9.19 | serie di (b(T − X)ᵐ + c(T − X)ⁿ)/A³ | SVG 199: «−mbXTⁿ⁻¹», manca «−ncXTⁿ⁻¹», «(mm − n)/2 bXXTⁿ⁻²» | **tre errori** nella serie |
| S9.19 | *mbTᵐ⁻¹ + ncTⁿ⁻¹* (dopo *vicissim*) | «mbTn − 1 + ncTn − 1» | **errore** di indice |
| S9.21 | *de apside discedens* | «from the lower apsis» | aggiunta |
| S9.23 | *A^(2 + 4/243)* | SVG 240: A^(2 + 49/253) | **errore** numerico |
| S9.24 | 357.45; 180.7623 | «357,45»; «180,7623» | virgola decimale (non è un errore) |
| S9.25 | *quibus corpora incumbunt quæque tangunt* | «roll or slide, and which are therefore tangent planes» | ampliamento |
| Tit. X | *funipendulorum* | «funependulous bodies» | grafia |
| S10.04 | — | «completing the same periods of time in all cases» | aggiunta |
| S10.06–07 | *more rotarum revolvendo*; *revolvendo* | «revolving about its own axis» | parafrasi |
| S10.14 | *ceu obstaculum* | «as if it were some solid obstacle» | aggiunta |
| S10.22 | *vis acceleratrix* | «this accelerated force» | termine non equivalente |
| S10.24 | *Wrennus & Hugenius* | «Sir Christopher Wren and M. Huygens» | titoli aggiunti |
| S10.31 | *descendent & ascendent* | «descend or ascend» | congiunzione |
| S10.34 | *vestigium* | «orthographic projection» | interpretazione |
| S10.38 | *in plano BLO* | «in the plane BDO» | lettera diversa (da verificare sulla figura) |
| S10.38 | *ellipsis illa PQ* | «the ellipsis pQ» | Motte uniforma |

Le formule-immagine di Motte sono per il resto corrette: tutte le altre (SVG 157–192, 196–198, 200–239, 241–255) coincidono con la lettura ricostruita della trascrizione. Gli errori di SVG 193, 195, 199 e 240 potrebbero essere dell’edizione 1846 o della sua conversione digitale; il confronto con Motte 1729 non è stato eseguito.

---

## Note editoriali e fisiche

Queste note sono aggiunte del presente fascicolo, non affermazioni tradotte da Newton. I controlli numerici sono stati eseguiti con script Python (NumPy, SciPy) scritti per questo fascicolo.

### N1. «In conseguenza» e «in antecedenza»

*In consequentia* significa «nel verso del moto», cioè nel verso in cui procede il corpo (e, in astronomia, nel verso dell’ordine dei segni dello zodiaco); *in antecedentia*, «contro il verso del moto». Nella Prop. XLIV l’orbita upk che ruota **in conseguenza** ruota nello stesso verso del corpo; quella che ruota **in antecedenza** ruota in verso opposto. Nel Cor. 1 della Prop. XLV l’apside che «avanza di tre gradi in conseguenza» si sposta nel verso del moto del corpo: è il moto progressivo dell’apside, come quello dell’apogeo lunare.

### N2. Prop. XLIII–XLIV: il teorema delle orbite rotanti

*Altitudo* è la distanza dal centro delle forze, oggi *r*. Se un corpo descrive un’orbita *r*(θ) sotto la forza centrale *f*(*r*), il corpo che descrive la stessa orbita mentre questa ruota, cioè con *r* uguale e angolo θ′ = *k*θ con *k* = G/F, ha momento angolare *L*′ = *kL* e richiede la forza

*f*′(*r*) = *f*(*r*) + (*L*′² − *L*²)/*r*³ = *f*(*r*) + *L*²(*k*² − 1)/*r*³.

È l’enunciato della Prop. XLIV: la differenza va come 1/*r*³. La condizione di Newton per una forza maggiore («se l’orbita si muove in conseguenza, oppure in antecedenza con una celerità maggiore del doppio di quella di CP») equivale a *k*² > 1, cioè *k* > 1 oppure *k* < −1: un’orbita che ruota all’indietro con velocità angolare maggiore del doppio di quella del raggio dà θ′ = *k*θ con *k* < −1.

**Verifica numerica.** Ellisse di Keplero con forza 1/*r*² (F = 1), semiasse 1, eccentricità 0,5, partenza dall’apside superiore; *k* = 1,3. Ho integrato separatamente l’orbita fissa e quella con forza 1/*r*² + R(*k*² − 1)/*r*³ (R semilato retto) e momento angolare *k* volte maggiore, per 20 unità di tempo. Risultato: |*r*₂ − *r*₁| < 4·10⁻¹², |θ₂ − *k*θ₁| < 3·10⁻¹¹. L’orbita rotante è esattamente l’ellisse che ruota come prevede il teorema.

### N3. Prop. XLIV, Cor. 1–5

- **Cor. 1.** Nella stessa prova (N2): la forza circolare alla distanza CV con la velocità che il corpo ha in V sta alla forza ellittica in V come R : CV (0,5 = 0,5), e la differenza delle forze in V sta alla forza circolare come GG − FF : FF (0,69 = 0,69). Il rapporto (GG − FF)/FF dipende soltanto dal rapporto delle velocità angolari.
- **Cor. 2.** In forma moderna, con μ = FF e *L*² = μR: *f*′ = FF/A² + (RGG − RFF)/A³. È la formula usata nella Prop. XLV.
- **Cor. 3.** Ellisse con il centro nel centro delle forze (forza ∝ A, Prop. X): ho ripetuto la verifica di N2 per *x* = 2 cos *t*, *y* = sin *t* (T = 2, R = b²/a = 1/2) con *k* = 1,3. Errori < 3·10⁻¹²; l’identità RFF = *L*² vale con FF = ω²T³.
- **Cor. 4–5.** Il Cor. 4 generalizza a qualsiasi orbita usando il raggio di curvatura nell’apside; il Cor. 5 è il principio del metodo: da un’orbita nota se ne ottengono infinite altre aggiungendo forze come 1/A³.

### N4. Prop. XLIV, Cor. 6: la spirale della retta ruotata

Una retta percorsa uniformemente in assenza di forza ha, in coordinate polari, *u* = 1/*r* = cos θ / *d*. Ruotandola con θ′ = *k*θ si ottiene *u* = cos(θ′/*k*)/*d*, che soddisfa *u*″ + *u* = *u*(1 − 1/*k*²): per la formula di Binet la forza è proporzionale a *u*³, cioè all’inverso del cubo della distanza, come afferma Newton. Le curve ottenute sono le spirali che oggi si dicono «di Cotes» (del tipo 1/*r* = cos(θ/*k*)/*d*); Newton le collega alla curva del Cor. 3 della Prop. XLI.

### N5. Prop. XLV: il metodo e gli esempi 1–3

**Il metodo in termini moderni.** Per un’orbita quasi circolare di raggio *r*₀ sotto la forza *f*(*r*), la piccola oscillazione radiale ha pulsazione Ω con Ω² = ω²(3 + *r f*′/*f*) calcolata in *r*₀, dove ω è la velocità angolare. L’angolo fra apside superiore e inferiore è quindi ψ = π/√(3 + *r f*′/*f*). Per *f* ∝ *r*ⁿ⁻³ si ha *r f*′/*f* = *n* − 3 e ψ = 180°/√*n*: è l’Es. 2. Per *f* ∝ (b*r*ᵐ + c*r*ⁿ)/*r*³ con *r*₀ = 1 si ottiene ψ = 180°·√((b + c)/(mb + nc)): è l’Es. 3. Il confronto dei «termini dati» e «non dati» del numeratore è un’espansione al primo ordine in X = T − A, cioè una linearizzazione.

**Verifica delle cifre di Newton.**

| Esempio | Forza | Formula | Valore esatto | Newton | Esito |
|---|---|---|---|---|---|
| Es. 1 | uniforme (n = 3) | 180/√3 | 103,92305° = 103° 55′ 22,97″ | 103° 55′ 23″ | corretto |
| Es. 2 | ∝ A (n = 4) | 180/√4 | 90° | 90° | corretto |
| Es. 2 | ∝ 1/A (n = 2) | 180/√2 | 127,27922° = 127° 16′ 45,19″ | 127° 16′ 45″ | corretto |
| Es. 2 | ∝ 1/A^(11/4) (n = 1/4) | 180/√(1/4) | 360° | 360° | corretto |

**Verifica per integrazione numerica.** Ho integrato le equazioni del moto per ciascuna legge di forza, partendo da un’apside a distanza 1 con velocità ridotta di una frazione ε rispetto a quella circolare, e ho misurato l’angolo percorso fino all’apside successiva. Con ε = 10⁻⁴: forza uniforme 103,923048° (teoria 103,923048°); forza ∝ A 90,000000°; forza ∝ 1/A 127,279221°; forza ∝ A^(−11/4) 360,00003°; forza ∝ 1/A² 180,000000°. Per l’Es. 3 con b = 1, c = 1/2, m = 1, n = 4, cioè forza 1/A² + A/2, la teoria dà 127,279°; l’integrazione dà 127,921° con ε = 10⁻², 127,343° con ε = 10⁻³, 127,286° con ε = 10⁻⁴, 127,2799° con ε = 10⁻⁵: converge al valore di Newton quando l’orbita tende al cerchio. Ciò conferma la clausola di Newton: le orbite sono rese simili «non in generale, ma quando si avvicinano il più possibile alla forma circolare».

### N6. Prop. XLV, Cor. 1: esponenti dal moto delle apsidi

Se l’apside ritorna dopo un angolo 360°·m/n, allora 2·180°/√N = 360°·m/n, quindi √N = n/m e la forza va come A^(nn/mm − 3). Ho ricalcolato con frazioni esatte tutti i casi:

| m : n | nn/mm − 3 | Newton |
|---|---|---|
| 8, 4, 2, 1½ : 1 | −191/64, −47/16, −11/4, −23/9 | A^(1/64 − 3), A^(1/16 − 3), A^(1/4 − 3), A^(4/9 − 3): corretti |
| 1 : 1 | −2 | A⁻² = 1/AA: corretto |
| 3/4, 2/3, 1/3, 1/4 : 1 | −11/9, −3/4, 6, 13 | inversamente A^(11/9), A^(3/4); direttamente A⁶, A¹³: corretti |
| 363 : 360 = 121 : 120 | −29523/14641 = −2,0164606 | A^(−29523/14641): corretto |

- 2 + 4/243 = 2,0164609: l’approssimazione di Newton differisce dal valore esatto di 3·10⁻⁷, «con buona approssimazione».
- Rapporto di vicinanza: (3 − 2,0164606)/(2,0164606 − 2) = 59,751; con 2 + 4/243 si ha esattamente (1 − 4/243)/(4/243) = 239/4 = 59¾. Corretto.
- Integrazione numerica con forza ∝ A^(−29523/14641): il semiangolo fra le apsidi risulta 181,500000°, cioè un ritorno all’apside dopo 363,000000°, come previsto.
- **Errore di Motte 1846:** SVG 240 stampa A^(2 + 49/253) = A^2,194, valore che corrisponderebbe a un moto delle apsidi molto più rapido. È un errore dell’edizione inglese o della sua conversione digitale, non di Newton.
- La conclusione fisica è importante: se la forza decrescesse più rapidamente dell’inverso del cubo, non esisterebbero orbite quasi circolari stabili (il corpo cade al centro o fugge all’infinito). In termini moderni: 3 + *r f*′/*f* deve essere positivo.

### N7. Prop. XLV, Cor. 2: il moto dell’apside della Luna

Con *f* = 1/A² − cA (forza estranea sottratta, proporzionale alla distanza), l’Es. 3 con b = 1, m = 1, n = 4 e −c al posto di c dà ψ = 180°·√((1 − c)/(1 − 4c)).

- c = 100/35745 = 1/357,45 = 0,0027976: corretto.
- (1 − c)/(1 − 4c) = (35745 − 100)/(35745 − 400) = 35645/35345: corretto.
- 180·√(35645/35345) = 180,762285° = 180° 45′ 44,2″. Newton: 180,7623 = 180° 45′ 44″. **Corretto.**
- Avanzamento dell’apside per rivoluzione: 2 × 0,762285° = 1,524569° = 1° 31′ 28,4″. Newton: 1° 31′ 28″. **Corretto.**
- Integrazione numerica dell’orbita con questa forza: 180,7618° con ε = 10⁻⁴ e 180,76224° con ε = 10⁻⁵, convergente al valore teorico.

**Confronto con la Luna (valori moderni, non ricavati dalle fonti del fascicolo).** Dal mese anomalistico (27,5546 giorni) e dal mese siderale (27,3217 giorni) l’apside lunare avanza di circa 3,04°–3,07° per rivoluzione, cioè circa 2,0 volte il valore calcolato (1,52°). La frase di Newton, «l’apside della Luna è circa due volte più veloce», è quindi esatta come confronto. Il rapporto 1 : 357,45 non è giustificato in questa sezione: corrisponde alla parte media della forza perturbatrice del Sole sulla Luna, che Newton tratta nel Libro III (da riscontrare nel fascicolo relativo). Notizia storica, esterna alle fonti: la discrepanza di un fattore 2 fra il calcolo al primo ordine e l’osservazione fu risolta da Clairaut nel 1749, tenendo conto dei termini di ordine superiore della perturbazione.

### N8. Il passaggio ai piani eccentrici

Il capoverso *Hactenus* (S9.25) annuncia il programma della Sezione X: dopo i moti in piani che passano per il centro delle forze, i moti vincolati a piani che non vi passano e poi a superfici curve. Il richiamo agli «autori che trattano del moto dei gravi» rimanda alla tradizione di Galileo sui piani inclinati. I piani sono supposti senza attrito, e Newton considera il moto del centro del corpo, in piani paralleli a quelli fisici.

### N9. Prop. XLVI–XLVII: forza centrale e piano vincolato

La forza centrale SV si scompone in una parte perpendicolare al piano, annullata dalla reazione del vincolo, e in una parte TV nel piano, diretta verso il piede C della perpendicolare da S. Se la forza è proporzionale alla distanza (Prop. XLVII), TV = k·CQ: la forza efficace nel piano è ancora proporzionale alla distanza da C, con la stessa costante. Il moto nel piano è quindi un oscillatore armonico isotropo con lo stesso periodo 2π/√k in ogni piano e per ogni ampiezza: ellissi di centro C oppure oscillazioni rettilinee per C. In forma moderna, l’equazione **r**̈ = −k**r** si proietta su ogni piano senza cambiare la costante.

### N10. Lo scolio sulle superfici di rivoluzione

Se la superficie è generata dalla rotazione di una curva intorno a un asse che passa per il centro delle forze, e il corpo si muove in un piano che contiene l’asse (senza componente di rotazione intorno all’asse), il moto resta in quel piano per simmetria: basta studiare il moto lungo la curva generatrice. È il caso del pendolo che oscilla in un piano. Il caso generale, con rotazione intorno all’asse, è trattato nelle Prop. LV–LVI.

### N11. Seno verso e cicloidi

Il **seno verso** di un arco di angolo φ in un cerchio di raggio *r* è *r*(1 − cos φ). Il «doppio seno verso dell’arco ½PB» è quindi 2*r*(1 − cos(φ/2)), dove φ è l’angolo BEP di cui la ruota ha girato rispetto al raggio EB.

### N12. Prop. XLVIII–XLIX: lunghezza della cicloide fuori e dentro il globo

Le curve di Newton sono l’**epicicloide** (ruota fuori del globo) e l’**ipocicloide** (ruota dentro). Con a raggio del globo (CB) e *r* raggio della ruota, CE = a ± *r* e la tesi è

AP = (2CE/CB) · 2*r*(1 − cos(φ/2)), con φ = a*t*/*r*,

dove *t* è l’angolo al centro C percorso dal punto di contatto. In forma moderna, s = (8*r*(a ± *r*)/a)·sin²(φ/4).

**Verifica numerica.** Ho parametrizzato le due curve (rotolamento senza strisciamento: arco AB = arco PB), controllato che |PE| = *r* e che l’angolo BEP sia φ (errori < 10⁻¹²), e calcolato la lunghezza d’arco per quadratura.

| Caso | a | *r* | *t* | AP/(2·sinvers) | 2CE/CB |
|---|---|---|---|---|---|
| esterno (XLVIII) | 3 | 1 | 0,5 | 2,6666666666 | 2,6666666667 |
| esterno | 5 | 1,2 | 0,9 | 2,4800000000 | 2,4800000000 |
| esterno | 2 | 0,7 | 1,1 | 2,7000000000 | 2,7000000000 |
| interno (XLIX) | 3 | 1 | 0,5 | 1,3333333333 | 1,3333333333 |
| interno | 5 | 1,2 | 0,9 | 1,5200000000 | 1,5200000000 |
| interno | 2 | 0,7 | 1,1 | 1,3000000000 | 1,3000000000 |

Il rapporto 2CE/CB = (somma dei diametri)/(semidiametro del globo) per la XLVIII e (differenza dei diametri)/(semidiametro) per la XLIX, come negli enunciati. Il Cor. 2 (semiperimetro AS) segue con φ = π: il doppio seno verso diventa 2*r* = BV, e quindi AS = (2CE/CB)·BV, come afferma Newton (verificato nella prova di N13: AS = 1,0666667 = (2CE/CB)·BV con a = 5/3, BV = 2/3).

### N13. Prop. L: l’evoluta della cicloide dentro il globo

La Prop. L afferma, in termini moderni, che l’**evoluta** di un’ipocicloide è un’ipocicloide simile, generata nel globo di raggio CA = CO²/CR da una ruota di diametro AO, con la cuspide in A sulla retta CR. Il filo che si avvolge sull’evoluta descrive l’ipocicloide data (come nel pendolo di Huygens per la cicloide comune).

**Verifica numerica** su un’ipocicloide con CO = 1 e ruota di raggio 0,2 (CR = 0,6):

- CA = CO²/CR = 1,666667; AO = 0,666667.
- Il centro di curvatura nel vertice R coincide con A (scarto 8·10⁻¹⁶).
- I centri di curvatura di 40 punti dell’arco RS stanno sull’ipocicloide di raggio CA generata dalla ruota di diametro AO, con cuspide in A: distanza massima 1,3·10⁻¹¹.
- Lunghezza del filo: per tre posizioni di T, PT + arco AP = 1,06666667 = AR, e PT = arco PS dell’evoluta (Cor. 1 della Prop. XLIX).
- Cor. della Prop. L: AR/AC = 0,64000000 e arco SR/CO = 0,64000000.

Il passaggio *divisim* è corretto: da CA : CO = CO : CR segue (CA − CO) : CO = (CO − CR) : CR, e quindi AO : OR = CO : CR = CA : CO; da qui (AO + OR) : AO = (CA + CO) : CA.

### N14. Prop. LI e corollario: isocronismo

Se la forza è V·CT verso C, la sua componente lungo la tangente in T alla cicloide è proporzionale all’arco TR: la cicloide dentro il globo è la **tautocrona** per la forza proporzionale alla distanza. Il moto lungo l’arco *s* obbedisce allora a *s*̈ = −κ*s*, con κ = V·CO/SR, ed è armonico: il tempo non dipende dall’ampiezza.

**Verifica numerica** (stessa figura di N13, V = 2,5): il rapporto fra la componente tangenziale della forza e l’arco TR vale 3,90625000 in quattro punti diversi dell’arco, uguale a V·CO/SR = 2,5/0,64 = 3,90625. Il corollario (forza in T : peso in S = arco TR : arco SR) è la stessa proporzionalità.

La frase *ob datas CV, WV iisque proportionales TX, TW* va intesa così. Il punto T sta sul cerchio di diametro VW (la ruota generatrice, nella posizione in cui tocca il globo interno in V; per la Prop. L, VW = OR): l’angolo VTW è quindi retto, VT è la direzione del filo e TW la tangente. CX e VT, entrambe perpendicolari a TW, sono parallele; i triangoli WTV e WXC sono simili e danno TX : TW = CV : WV, rapporto costante. La ricostruzione è mia, fatta senza la figura NATP00087-109, ed è confermata dalla verifica numerica qui sopra.

### N15. Prop. LII e corollari; la gravità dentro la Terra

- Il cerchio ausiliario HKM è il modo geometrico di rappresentare il **moto armonico**: il corpo L, attratto verso G con forza proporzionale alla distanza, è la proiezione di un punto che percorre il semicerchio con velocità uniforme. Quindi il tempo è come l’arco HI e la velocità in L è come l’ordinata LI = √(GH² − GL²), cioè v(T) : v(R) = √(SR² − TR²) : SR.
- **Tempo di oscillazione.** Da κ = V·CO/SR (N14), il tempo di un’oscillazione semplice è π√(SR/(CO·V)) = π√(AR/(AC·V)), perché SR/CO = AR/AC (Cor. della Prop. L, verificato in N13). È la legge composta enunciata da Newton: direttamente come la radice della lunghezza del filo AR, inversamente come la radice della distanza AC del punto di sospensione dal centro e della forza assoluta V.
- **Cor. 1.** Se il diametro della ruota è uguale al raggio del globo, l’ipocicloide degenera in un diametro (*r* = a/2: le equazioni danno *x* = a cos *t*, *y* = 0). Il moto lungo il diametro e il moto circolare uniforme a qualsiasi distanza hanno, con forza V·*r*, lo stesso periodo 2π/√V: il quarto di giro dura quanto la caduta fino al centro. Il rapporto con la mezza oscillazione in una cicloide qualsiasi è 1 : √(AR/AC), coerente con la formula precedente.
- **Cor. 2.** Per raggio del globo infinito la forza diventa uniforme e parallela, e si ritrovano la rettificazione della cicloide di Wren (arco = 4 volte il seno verso della metà dell’arco della ruota, cioè s = 4*r*(1 − cos(φ/2)), caso limite della formula di N12 con a → ∞) e il pendolo cicloidale isocrono di Huygens.
- **La Terra** (S10.25). Newton afferma che la gravità, sotto la superficie, decresce in proporzione alla distanza dal centro. Ciò vale per una Terra di densità uniforme, che è l’ipotesi del Libro III. **Nota fisica moderna:** poiché la densità della Terra cresce verso il centro, la gravità reale nella crosta e nel mantello superiore non diminuisce scendendo, anzi aumenta leggermente fino al confine con il nucleo. L’osservazione non tocca la matematica della proposizione.

### N16. Prop. LIII: forze per l’isocronismo su una curva qualsiasi

La costruzione dà una forza centrale TZ la cui componente tangenziale TY è uguale all’arco TR: in forma moderna, la componente tangenziale della forza è proporzionale all’arco *s* misurato dal punto più basso, quindi *s*̈ = −κ*s* e le oscillazioni sono isocrone.

- **Cor. 1.** Per il pendolo circolare di lunghezza ℓ, la componente tangenziale di una forza verticale F è F sin θ, e l’arco è ℓθ. Per l’isocronismo serve F sin θ ∝ θ, cioè F : g = θ : sin θ = arco TR : seno TN, come scrive Newton.
- **Cor. 2.** *Applicare il rettangolo TR × AR al seno TN* significa dividere: la forza totale deve essere come (TR × AR)/TN. È un progetto di correzione dell’orologio a pendolo semplice, non cicloidale.

### N17. Prop. LIV: il tempo come area

Il tempo per percorrere l’elemento Tt è *ds*/*v*. Con *ds* = Dd/cos(angolo tTC) = Dd · sec(tTC) e *v* data dalla Prop. XXXIX (conservazione dell’energia in linguaggio moderno), il tempo totale è ∫ sec(tTC)/*v* d*r*. Newton costruisce la curva PNn con ordinata DN proporzionale all’integrando: l’area sotto la curva è il tempo. La retta SQ è un asintoto perché in S la velocità iniziale è nulla e l’integrando diverge (in modo integrabile).

### N18. Prop. LV–LVI: la legge delle aree su una superficie di rivoluzione

In termini moderni la Prop. LV afferma che si conserva la **componente del momento angolare lungo l’asse**. La forza centrale passa per C, che è sull’asse, e la reazione normale di una superficie di rivoluzione giace nel piano che contiene l’asse e il corpo: nessuna delle due ha momento rispetto all’asse. La proiezione del moto sul piano perpendicolare all’asse (la «traccia» AP) obbedisce quindi alla legge delle aree rispetto al punto O, come per una forza centrale (Prop. I). Il corollario estende il risultato a forze dirette verso più centri allineati sull’asse, per lo stesso motivo. La Prop. LVI usa questa legge delle aree, insieme alla velocità nota a ogni altezza, per costruire la traccia punto per punto e poi risalire alla traiettoria sulla superficie: è l’analogo, su una superficie, del metodo della Prop. XLI.

---

## Controllo della copertura

I gruppi seguono l’ordine del testo latino. Le pagine sono quelle dell’edizione 1726, segnate nella trascrizione con i numeri tra parentesi angolari; per Motte valgono i marcatori di pagina dell’EPUB.

| Identificatori | Incipit latino | Contenuto | 1726 | Motte 1846 |
|---|---|---|---|---|
| S9.01–S9.02 | *Efficiendum est ut corpus* | Prop. XLIII | pp. 129–130 | pp. 172–173 |
| S9.03–S9.06 | *Differentia virium, quibus corpus* | Prop. XLIV, dimostrazione | pp. 130–133 | pp. 173–174 |
| S9.07–S9.08 | *Hinc differentia virium in locis P & p* | Cor. 1–2 | pp. 133–134 | pp. 174–176 |
| S9.09–S9.12 | *Ad eundem modum colligetur* | Cor. 3–6 | pp. 134–135 | p. 176 |
| S9.13–S9.14 | *Orbium qui sunt circulis maxime finitimi* | Prop. XLV, metodo | p. 136 | p. 177 |
| S9.15–S9.16 | *Ponamus vim centripetam uniformem* | Es. 1 | pp. 136–137 | pp. 177–178 |
| S9.17–S9.18 | *Ponamus vim centripetam esse ut altitudinis* | Es. 2 | pp. 137–138 | pp. 178–179 |
| S9.19–S9.20 | *Assumentes m & n* | Es. 3 e regola generale | pp. 138–139 | pp. 179–180 |
| S9.21–S9.23 | *Hinc si vis centripeta sit ut aliqua* | Cor. 1 | pp. 139–141 | pp. 180–181 |
| S9.24 | *Hinc etiam si corpus, vi centripeta* | Cor. 2, Luna | p. 141 | pp. 181–182 |
| S9.25 | *Hactenus de motu corporum* | passaggio ai piani eccentrici | pp. 141–142 | p. 182 |
| S10.01–S10.02 | *Posita cujuscunque generis vi centripeta* | Prop. XLVI | pp. 142–143 | pp. 182–183 |
| S10.03–S10.04 | *Posito quod vis centripeta proportionalis* | Prop. XLVII | pp. 143–144 | pp. 183–184 |
| S10.05 | *His affines sunt ascensus* | Scolio | p. 144 | p. 184 |
| S10.06 | *Si rota globo extrinsecus* | Prop. XLVIII | p. 145 | p. 184 |
| S10.07–S10.10 | *Si rota globo concavo* | Prop. XLIX e denominazione | pp. 145–147 | pp. 184–186 |
| S10.11–S10.12 | *Hinc si describatur cyclois integra* | Cor. 1–2 | p. 147 | p. 186 |
| S10.13–S10.16 | *Facere ut corpus pendulum* | Prop. L e corollario | pp. 147–149 | pp. 186–187 |
| S10.17–S10.19 | *Si vis centripeta tendens undique* | Prop. LI e corollario | pp. 149–151 | pp. 187–188 |
| S10.20–S10.22 | *Definire & velocitates pendulorum* | Prop. LII | pp. 151–153 | pp. 188–190 |
| S10.23–S10.25 | *Hinc etiam oscillantium* | Cor. 1–2; la Terra | pp. 153–154 | p. 190 |
| S10.26–S10.30 | *Concessis … invenire vires* | Prop. LIII e corollari | pp. 154–156 | pp. 190–191 |
| S10.31–S10.32 | *Concessis … invenire tempora* | Prop. LIV | pp. 156–157 | pp. 191–192 |
| S10.33–S10.36 | *Si corpus movetur in superficie* | Prop. LV e corollario | pp. 157–158 | pp. 192–193 |
| S10.37–S10.38 | *Concessis … datisque tum lege* | Prop. LVI | pp. 159–160 | pp. 193–194 |

**Controlli eseguiti.**

1. **Rilettura frase per frase contro il latino.** Ho confrontato in sequenza ogni periodo della trascrizione, da *Efficiendum est ut corpus* (p. 129) a *dabuntur singula trajectoriæ puncta T. Q.E.I.* (p. 160), con la traduzione. Nessuna frase manca. I periodi lunghi sono stati divisi in più frasi italiane senza omettere membri; le dimostrazioni delle Prop. XLIV, XLIX, L, LII, LIII e LV sono divise in più capoversi identificati. Le 94 frasi latine della Parte B sono state estratte automaticamente dalla trascrizione e allineate una per una alla traduzione: il testo italiano delle dimostrazioni e i campi `it` della Parte B sono generati dalla stessa fonte e coincidono.
2. **check.py.** `check.py` sul fascicolo con le due fonti latine e le due di Motte: 14 unità, 94 passi, 63 identificatori, nessun errore e nessun avviso. Tutte le stringhe `la` ed `en` (enunciati e passi) sono sottostringhe esatte delle fonti.
3. **Matematica.** Tutti gli esempi numerici della Prop. XLV (Es. 1–2, Cor. 1, Cor. 2 con il valore lunare) sono stati ricalcolati con frazioni esatte e confermati per integrazione numerica delle orbite (N5–N7); tutte le cifre di Newton sono corrette. Verifiche numeriche su figure di prova per le Prop. XLIV e Cor. 1, 3 (N2–N3), XLVIII–XLIX (N12), L e corollario (N13), LI (N14), LII (N15).
4. **Confronto con Motte.** Tutta la sezione corrispondente, pp. 172–194, comprese le 99 formule-immagine SVG 157–255, rese in PNG e lette. Le divergenze sono nel § A.16.
5. **Separazione fra testo e commento.** Il testo tradotto non contiene formule moderne; le notazioni √, ^( ) e × trascrivono le formule di Newton (§ Criteri). L’unica integrazione nel testo è «[X]» in S9.15.

**Non ho potuto verificare:**

- **la stampa del 1726**: i refusi probabili del § A.15 (*angulum*, *FAA*, −FF senza X, *effe*, *ponendaæ*, *ocurrant*, *eundem*, *æquantur … ad*, *directæ*, *erun*, la punteggiatura della Prop. LIV, *PQ*) e la grafia *funipendulorum* non sono stati controllati sulla stampa;
- **le figure NATP00087-100…119**: in particolare il punto R del Cor. 1 della Prop. XLIV, la lettera *BLO / BDO* della Prop. LVI e la posizione di X e W nella Prop. LI sono ricostruiti dal testo;
- **Motte 1729**: non so se gli errori delle formule SVG 193, 195, 199 e 240 siano già nella prima edizione inglese o soltanto nell’edizione 1846 o nella sua conversione;
- **la corrispondenza esatta della numerazione di pagina di Motte**, che deriva dai marcatori dell’EPUB Gutenberg;
- **il valore 357,45 nel Libro III**: il collegamento con la forza perturbatrice del Sole (N7) è da riscontrare nel fascicolo del Libro III.

---

## Registro del lavoro successivo

| Unità | Stato |
|---|---|
| Libro I, Sezioni IX e X | **Fascicolo 9, presente documento, prima versione** |
| Dati per le pagine interattive (14 unità) | Parte B di questo fascicolo |
| Prop. XLV (senza figura) | Candidata a una pagina interattiva di tipo diverso: calcolatore dell’angolo apsidale per forze ∝ Aⁿ⁻³ e per 1/A² − cA, con il caso lunare; non inclusa nella Parte B perché il brief richiede figura e costruzione |
| Riscontro sulla stampa del 1726 | Da eseguire per i punti del § A.15 |
| Riscontro sulle figure NATP00087-100…119 | Da eseguire (punto R, BLO/BDO, figura della Prop. LI) |
| Motte 1729 | Controllare SVG 193, 195, 199, 240 sulla prima edizione |
| Coerenza con i fascicoli vicini | Verificare la resa di *altitudo*, *lineola*, *vicissim*, *apsis summa / ima*, *vestigium* con i traduttori delle Sezioni VIII e XI |
| Libro III | Riscontrare il valore 357,45 e la legge della gravità dentro la Terra |
| Revisione filologica e scientifica indipendente | Da eseguire, come previsto dalla skill di verifica |

Il presente testo è una nuova traduzione assistita da IA. Non riproduce le traduzioni italiane moderne. **Licenza prevista** (decisione del curatore, Fascicolo 3): testi e traduzioni CC BY-SA 4.0, codice MIT. La trascrizione latina è © The Newton Project e non va ridistribuita finché non se ne chiariscono le condizioni d’uso; il testo di Motte 1846 è di pubblico dominio.

---

## Parte B — Dati per le pagine interattive

Unità incluse: le proposizioni con dimostrazione e figura (XLIII, XLIV, XLVI, XLVII, XLIX con la XLVIII, L, LI, LII, LIII, LIV, LV, LVI) e i due corollari con dimostrazione propria e figura (Prop. XLIV, Cor. 6; Prop. LIII, Cor. 1). Escluse:

- **Prop. XLV**: è risolta *arithmetice*, senza figura né costruzione; è candidata a una pagina di calcolo (Registro);
- **Prop. XLVIII**: non ha dimostrazione propria; il suo enunciato è coperto dall’unità della Prop. XLIX (S10.06);
- **Prop. XLIV, Cor. 1–5**: il Cor. 3 ha una figura (NATP00087-103) ma non una dimostrazione propria (*Ad eundem modum colligetur*); i Cor. 1, 2, 4, 5 non hanno figura propria;
- **i corollari brevi** delle Prop. XLIX, L, LI, LII e LV, lo Scolio che segue la Prop. XLVII e il Cor. 2 della Prop. LIII: senza dimostrazione propria con figura.

Convenzioni:

- `la`: frase latina esatta della trascrizione, compresi i refusi (annotati in `nota`); sono tolti soltanto i marcatori di figura e di pagina;
- `it`: la traduzione di questo fascicolo; le frasi coincidono con il testo delle dimostrazioni;
- `en`: Motte 1846, allineato per senso; `[SVG n]` indica una formula stampata come immagine;
- `dipende_da`: soltanto i rimandi citati nella frase («per legum corol. 2.» → "Leggi, Cor. II");
- `figura.mostra`: elementi da rendere visibili al passo; `figura.evidenzia`: relazioni da mettere in risalto.

```json
{
 "fascicolo": "09-L1-S9-10",
 "versione": "0.1",
 "data": "2026-11-08",
 "convenzioni": {
  "dipende_da": "solo rimandi citati esplicitamente nella frase latina",
  "en": "Motte 1846, allineato per senso; i segnaposto [SVG n] sono formule stampate come immagine nell’EPUB",
  "la": "",
  "figura.mostra": "elementi da rendere visibili al passo, cumulativi salvo indicazione"
 },
 "unita": [
  {
   "id": "L1-P43",
   "tipo": "Propositio/Problema",
   "titolo": "Prop. XLIII — corpo in un’orbita che ruota",
   "copertura": [
    "S9.01",
    "S9.02"
   ],
   "fonti": {
    "la": "",
    "en": "Motte 1846, pp. 172–173"
   },
   "enunciato": {
    "la": "",
    "it": "Si deve fare in modo che un corpo possa muoversi in una traiettoria qualsiasi, che ruota intorno al centro delle forze, esattamente come un altro corpo nella stessa traiettoria in quiete.",
    "en": "It is required to make a body move in a trajectory that revolves about the centre of force in the same manner as another body in the same trajectory at rest."
   },
   "figura_base": {
    "punti": [
     "C",
     "V",
     "P",
     "K",
     "p",
     "u"
    ],
    "vincoli": [
     "VPK orbita data di posizione, C centro delle forze",
     "Cp = CP",
     "angolo VCp : angolo VCP = rapporto dato",
     "angolo VCu = angolo PCp; Cu = CV; figura uCp uguale alla figura VCP"
    ]
   },
   "passi": [
    {
     "id": "L1-P43-p1",
     "la": "",
     "it": "Nell’orbita VPK, data di posizione, ruoti il corpo P procedendo da V verso K.",
     "en": "In the orbit VPK, given by position, let the body P revolve, proceeding from V towards K.",
     "dipende_da": [],
     "figura": {
      "mostra": [
       "orbita VPK",
       "C",
       "V",
       "corpo P"
      ],
      "evidenzia": [
       "moto di P da V verso K"
      ]
     }
    },
    {
     "id": "L1-P43-p2",
     "la": "",
     "it": "Dal centro C si conduca in ogni istante Cp, uguale a CP, che formi l’angolo VCp proporzionale all’angolo VCP; l’area che la linea Cp descrive starà all’area VCP, che la linea CP descrive nello stesso tempo, come la velocità della linea Cp che descrive sta alla velocità della linea CP che descrive, cioè come l’angolo VCp sta all’angolo VCP: dunque in un rapporto dato, e perciò sarà proporzionale al tempo.",
     "en": "From the centre C let there be continually drawn Cp, equal to CP, making the angle VCp proportional to the angle VCP; and the area which the line Cp describes will be to the area VCP, which the line CP describes at the same time, as the velocity of the describing line Cp to the velocity of the describing line CP; that is, as the angle VCp to the angle VCP, therefore in a given ratio, and therefore proportional to the time.",
     "dipende_da": [],
     "figura": {
      "mostra": [
       "segmento CP",
       "segmento Cp = CP",
       "angoli VCP, VCp",
       "aree VCP e VCp"
      ],
      "evidenzia": [
       "angolo VCp : angolo VCP costante",
       "area descritta da Cp ∝ tempo"
      ]
     }
    },
    {
     "id": "L1-P43-p3",
     "la": "",
     "it": "Poiché l’area che la linea Cp descrive nel piano immobile è proporzionale al tempo, è manifesto che un corpo, sotto l’azione di una forza centripeta di giusta quantità, può ruotare insieme con il punto p lungo quella linea curva che lo stesso punto p, nel modo ora esposto, descrive nel piano immobile.",
     "en": "Since, then, the area described by the line Cp in an immovable plane is proportional to the time, it is manifest that a body, being acted upon by a just quantity of centripetal force may revolve with the point p in the curve line which the same point p, by the method just now explained, may be made to describe an immovable plane.",
     "dipende_da": [],
     "figura": {
      "mostra": [
       "curva descritta da p nel piano immobile"
      ],
      "evidenzia": [
       "legge delle aree per p"
      ]
     },
     "nota": "Motte omette «in» davanti a «an immovable plane»."
    },
    {
     "id": "L1-P43-p4",
     "la": "",
     "it": "Si faccia l’angolo VCu uguale all’angolo PCp, la linea Cu uguale alla linea CV e la figura uCp uguale alla figura VCP: il corpo, trovandosi sempre in p, si muoverà sul perimetro della figura rotante uCp, e ne descriverà l’arco up nello stesso tempo in cui l’altro corpo P può descrivere l’arco VP, simile e uguale a esso, nella figura in quiete VPK.",
     "en": "Make the angle VCu equal to the angle PCp, and the line Cu equal to CV, and the figure uCp equal to the figure VCP, and the body being always in the point p, will move in the perimeter of the revolving figure uCp, and will describe its (revolving) arc up in the same time that the other body P describes the similar and equal arc VP in the quiescent figure VPK.",
     "dipende_da": [],
     "figura": {
      "mostra": [
       "u",
       "figura rotante uCp",
       "arco up"
      ],
      "evidenzia": [
       "arco up uguale e simile all’arco VP"
      ]
     },
     "nota": "Motte aggiunge «(revolving)»."
    },
    {
     "id": "L1-P43-p5",
     "la": "",
     "it": "Si cerchi dunque, per il Cor. 5 della Prop. VI, la forza centripeta con cui un corpo può ruotare lungo quella linea curva che il punto p descrive nel piano immobile, e il problema sarà risolto. C.V.F.",
     "en": "Find, then, by Cor. 5, Prop. VI., the centripetal force by which the body may be made to revolve in the curve line which the point p describes in an immovable plane, and the Problem will be solved. Q.E.F.",
     "dipende_da": [
      "Prop. VI, Cor. 5"
     ],
     "figura": {
      "mostra": [
       "forza centripeta verso C sulla curva di p"
      ],
      "evidenzia": []
     }
    }
   ]
  },
  {
   "id": "L1-P44",
   "tipo": "Propositio/Theorema",
   "titolo": "Prop. XLIV — la differenza delle forze va come l’inverso del cubo",
   "copertura": [
    "S9.03",
    "S9.04",
    "S9.05",
    "S9.06"
   ],
   "fonti": {
    "la": "",
    "en": "Motte 1846, pp. 173–174"
   },
   "enunciato": {
    "la": "",
    "it": "La differenza delle forze per effetto delle quali un corpo in un’orbita in quiete e un altro corpo nella stessa orbita rotante possono muoversi allo stesso modo è inversamente in rapporto triplicato dell’altezza comune.",
    "en": "The difference of the forces, by which two bodies may be made to move equally, one in a quiescent, the other in the same orbit revolving, is in a triplicate ratio of their common altitudes inversely."
   },
   "figura_base": {
    "punti": [
     "C",
     "V",
     "P",
     "K",
     "u",
     "p",
     "k",
     "r",
     "m",
     "n",
     "s",
     "t"
    ],
    "vincoli": [
     "up, pk simili e uguali a VP, PK; PK nascente",
     "pC = PC, kC = KC",
     "kr ⊥ pC, r su pC; m sul prolungamento di kr con mr : kr = angolo VCp : angolo VCP",
     "angolo pCn : angolo pCk = angolo VCp : angolo VCP; nC = kC",
     "cerchio di centro C e raggio Ck taglia mr, mn prolungate in s, t"
    ]
   },
   "passi": [
    {
     "id": "L1-P44-p1",
     "la": "",
     "it": "Alle parti VP, PK dell’orbita in quiete siano simili e uguali le parti up, pk dell’orbita rotante; e si intenda che la distanza dei punti P, K sia minima.",
     "en": "Let the parts of the quiescent orbit VP, PK be similar and equal to the parts of the revolving orbit up, pk; and let the distance of the points P and K be supposed of the utmost smallness.",
     "dipende_da": [],
     "figura": {
      "mostra": [
       "orbita in quiete VPK",
       "orbita rotante upk",
       "archi VP, PK, up, pk"
      ],
      "evidenzia": [
       "PK nascente"
      ]
     }
    },
    {
     "id": "L1-P44-p2",
     "la": "",
     "it": "Dal punto k abbassa sulla retta pC la perpendicolare kr e prolungala fino a m, in modo che mr stia a kr come l’angolo VCp sta all’angolo VCP.",
     "en": "Let fall a perpendicular kr from the point k to the right line pC, and produce it to m, so that mr may be to kr as the angle VCp to the angle VCP.",
     "dipende_da": [],
     "figura": {
      "mostra": [
       "kr ⊥ pC",
       "m sul prolungamento di kr"
      ],
      "evidenzia": [
       "mr : kr = VCp : VCP"
      ]
     }
    },
    {
     "id": "L1-P44-p3",
     "la": "",
     "it": "Poiché le altezze dei corpi, PC e pC, KC e kC, sono sempre uguali, è manifesto che gli incrementi o i decrementi delle linee PC e pC sono sempre uguali; e perciò, se i singoli moti dei corpi che si trovano nei luoghi P e p si scompongono (per il Cor. II delle Leggi) in due, dei quali i primi siano diretti verso il centro, cioè lungo le linee PC, pC, e gli altri siano trasversali ai primi e abbiano direzione lungo linee perpendicolari a PC, pC, i moti verso il centro saranno uguali, e il moto trasversale del corpo p starà al moto trasversale del corpo P come il moto angolare della linea pC sta al moto angolare della linea PC, cioè come l’angolo VCp sta all’angolo VCP.",
     "en": "Because the altitudes of the bodies PC and pC, KC and kC, are always equal, it is manifest that the increments or decrements of the lines PC and pC are always equal; and therefore if each of the several motions of the bodies in the places P and p be resolved into two (by Cor. 2 of the Laws of Motion), one of which is directed towards the centre, or according to the lines PC, pC, and the other, transverse to the former, hath a direction perpendicular to the lines PC and pC; the motions towards the centre will be equal, and the transverse motion of the body p will be to the transverse motion of the body P as the angular motion of the line pC to the angular motion of the line PC; that is, as the angle VCp to the angle VCP.",
     "dipende_da": [
      "Leggi, Cor. II"
     ],
     "figura": {
      "mostra": [
       "componenti radiali e trasversali dei moti in P e p"
      ],
      "evidenzia": [
       "moti radiali uguali",
       "moto trasversale ∝ moto angolare"
      ]
     }
    },
    {
     "id": "L1-P44-p4",
     "la": "",
     "it": "Dunque, nello stesso tempo in cui il corpo P, con l’uno e l’altro dei suoi moti, giunge al punto K, il corpo p, con un moto uguale verso il centro, si muoverà di altrettanto da p verso C; e perciò, trascorso quel tempo, si troverà in qualche punto della linea mkr, che passa per il punto k ed è perpendicolare alla linea pC; e con il moto trasversale acquisterà dalla linea pC una distanza che starà alla distanza che l’altro corpo P acquista dalla linea PC come il moto trasversale del corpo p sta al moto trasversale dell’altro corpo P.",
     "en": "Therefore, at the same time that the body P, by both its motions, comes to the point K, the body p, having an equal motion towards the centre, will be equally moved from p towards C; and therefore that time being expired, it will be found somewhere in the line mkr, which, passing through the point k, is perpendicular to the line pC; and by its transverse motion will acquire a distance from the line pC, that will be to the distance which the other body P acquires from the line PC as the transverse motion of the body p to the transverse motion of the other body P.",
     "dipende_da": [],
     "figura": {
      "mostra": [
       "retta mkr"
      ],
      "evidenzia": [
       "p si trova sulla retta mkr"
      ]
     }
    },
    {
     "id": "L1-P44-p5",
     "la": "",
     "it": "Perciò, poiché kr è uguale alla distanza che il corpo P acquista dalla linea PC, e mr sta a kr come l’angolo VCp sta all’angolo VCP, cioè come il moto trasversale del corpo p sta al moto trasversale del corpo P, è manifesto che il corpo p, trascorso quel tempo, si troverà nel luogo m.",
     "en": "Therefore since kr is equal to the distance which the body P acquires from the line PC, and mr is to kr as the angle VCp to the angle VCP, that is, as the transverse motion of the body p to the transverse motion of the body P, it is manifest that the body p, at the expiration of that time, will be found in the place m.",
     "dipende_da": [],
     "figura": {
      "mostra": [
       "punto m"
      ],
      "evidenzia": [
       "con forze uguali p arriva in m"
      ]
     }
    },
    {
     "id": "L1-P44-p6",
     "la": "",
     "it": "Così andranno le cose quando i corpi p e P si muovono allo stesso modo lungo le linee pC e PC, e sono perciò sollecitati lungo quelle linee da forze uguali.",
     "en": "These things will be so, if the bodies p and P are equally moved in the directions of the lines pC and PC, and are therefore urged with equal forces in those directions,",
     "dipende_da": [],
     "figura": {
      "mostra": [],
      "evidenzia": [
       "caso di forze uguali"
      ]
     }
    },
    {
     "id": "L1-P44-p7",
     "la": "",
     "it": "Si prenda poi l’angolo pCn che stia all’angolo pCk come l’angolo VCp sta all’angolo VCP, e sia nC uguale a kC: il corpo p, trascorso quel tempo, si troverà in realtà in n; e perciò è sollecitato da una forza maggiore di quella del corpo P, se l’angolo nCp è maggiore dell’angolo kCp, cioè se l’orbita upk si muove in conseguenza, oppure si muove in antecedenza con una celerità maggiore del doppio di quella con cui la linea CP è portata in conseguenza; e da una forza minore, se l’orbita si muove in antecedenza più lentamente.",
     "en": "But if we take an angle pCn that is to the angle pCk as the angle VCp to the angle VCP, and nC be equal to kC, in that case the body p at the expiration of the time will really be in n; and is therefore urged with a greater force than the body P, if the angle nCp is greater than the angle kCp, that is, if the orbit upk, move either in consequentia or in antecedentia, with a celerity greater than the double of that with which the line CP moves in consequentia; and with a less force if the orbit moves slower in antecedentia.",
     "dipende_da": [],
     "figura": {
      "mostra": [
       "punto n con nC = kC",
       "angoli pCn, pCk"
      ],
      "evidenzia": [
       "n invece di m: forza maggiore se angolo nCp > angolo kCp"
      ]
     },
     "nota": "Il latino ha «Capiatur autem angulum pCn»: accusativo con passivo, refuso probabile della trascrizione per «angulus»."
    },
    {
     "id": "L1-P44-p8",
     "la": "",
     "it": "E la differenza delle forze è come la distanza mn fra i due luoghi, attraverso la quale il corpo p deve essere trasportato per azione di essa nel dato intervallo di tempo.",
     "en": "And the difference of the forces will be as the interval mn of the places through which the body would be carried by the action of that difference in that given space of time.",
     "dipende_da": [],
     "figura": {
      "mostra": [
       "segmento mn"
      ],
      "evidenzia": [
       "differenza delle forze ∝ mn"
      ]
     },
     "nota": "Motte «would be carried» per «transferri debet»."
    },
    {
     "id": "L1-P44-p9",
     "la": "",
     "it": "Con centro C e raggio Cn o Ck si intenda descritto un cerchio che tagli in s e t le linee mr, mn prolungate: il rettangolo mn × mt sarà uguale al rettangolo mk × ms, e perciò mn sarà uguale a (mk × ms)/mt.",
     "en": "About the centre C with the interval Cn or Ck suppose a circle described cutting the lines mr, mn produced in s and t, and the rectangle mn × mt will be equal to the rectangle mk × ms, and therefore mn will be equal to [SVG 157].",
     "dipende_da": [],
     "figura": {
      "mostra": [
       "cerchio di centro C e raggio Ck",
       "punti s, t"
      ],
      "evidenzia": [
       "mn × mt = mk × ms"
      ]
     },
     "nota": "Formula appiattita nella trascrizione: «mk×msmt» = (mk × ms)/mt (Motte, SVG 157)."
    },
    {
     "id": "L1-P44-p10",
     "la": "",
     "it": "Ma poiché i triangoli pCk, pCn, in un tempo dato, sono dati di grandezza, kr e mr, e la loro differenza mk e la loro somma ms, sono inversamente come l’altezza pC; e perciò il rettangolo mk × ms è inversamente come il quadrato dell’altezza pC.",
     "en": "But since the triangles pCk, pCn, in a given time, are of a given magnitude, kr and mr, and their difference mk, and their sum ms, are reciprocally as the altitude pC, and therefore the rectangle mk × ms is reciprocally as the square of the altitude pC.",
     "dipende_da": [],
     "figura": {
      "mostra": [
       "triangoli pCk, pCn"
      ],
      "evidenzia": [
       "kr, mr, mk, ms ∝ 1/pC",
       "mk × ms ∝ 1/pC²"
      ]
     }
    },
    {
     "id": "L1-P44-p11",
     "la": "",
     "it": "Inoltre mt è direttamente come ½mt, cioè come l’altezza pC.",
     "en": "But, moreover, mt is directly as [SVG 158], that is, as the altitude pC.",
     "dipende_da": [],
     "figura": {
      "mostra": [
       "segmento mt"
      ],
      "evidenzia": [
       "mt ≈ 2·pC"
      ]
     },
     "nota": "«12mt» = ½mt (Motte, SVG 158)."
    },
    {
     "id": "L1-P44-p12",
     "la": "",
     "it": "Questi sono i rapporti primi delle linee nascenti; e di qui (mk × ms)/mt, cioè la lineetta nascente mn, e la differenza delle forze, che le è proporzionale, risultano inversamente come il cubo dell’altezza pC. C.V.D.",
     "en": "These are the first ratios of the nascent lines; and hence [SVG 157], hat is, the nascent lineola mn, and the difference of the forces proportional thereto, are reciprocally as the cube of the altitude pC. Q.E.D.",
     "dipende_da": [],
     "figura": {
      "mostra": [],
      "evidenzia": [
       "mn ∝ 1/pC³"
      ]
     }
    }
   ]
  },
  {
   "id": "L1-P44-Cor6",
   "tipo": "Corollarium",
   "titolo": "Prop. XLIV, Cor. 6 — retta che ruota e forza come l’inverso del cubo",
   "copertura": [
    "S9.12"
   ],
   "fonti": {
    "la": "",
    "en": "Motte 1846, p. 176"
   },
   "enunciato": {
    "la": "",
    "it": "Dunque, se sulla retta CV, data di posizione, si innalza la perpendicolare VP di lunghezza indeterminata, si congiunge CP e si conduce Cp uguale a essa, che formi l’angolo VCp in un rapporto dato con l’angolo VCP, la forza con cui un corpo può girare lungo quella curva Vpk che il punto p tocca di continuo sarà inversamente come il cubo dell’altezza Cp.",
    "en": "Therefore if there be erected the line VP of an indeterminate length, perpendicular to the line CV given by position, and CP be drawn, and Cp equal to it, making the angle VCp having a given ratio to the angle VCP, the force with which a body may revolve in the curve line Vpk, which the point p is continually describing, will be reciprocally as the cube of the altitude Cp."
   },
   "figura_base": {
    "punti": [
     "C",
     "V",
     "P",
     "p",
     "k"
    ],
    "vincoli": [
     "VP ⊥ CV, di lunghezza indeterminata",
     "Cp = CP",
     "angolo VCp : angolo VCP = rapporto dato"
    ]
   },
   "passi": [
    {
     "id": "L1-P44-Cor6-p1",
     "la": "",
     "it": "Infatti il corpo P, per la forza d’inerzia, senza che nessun’altra forza lo solleciti, può avanzare uniformemente lungo la retta VP.",
     "en": "For the body P, by its vis inertiæ alone, no other force impelling it, will proceed uniformly in the right line VP.",
     "dipende_da": [],
     "figura": {
      "mostra": [
       "retta VP",
       "corpo P in moto uniforme"
      ],
      "evidenzia": [
       "moto senza forza"
      ]
     }
    },
    {
     "id": "L1-P44-Cor6-p2",
     "la": "",
     "it": "Si aggiunga una forza verso il centro C, inversamente proporzionale al cubo dell’altezza CP o Cp, e (per quanto ora dimostrato) quel moto rettilineo sarà piegato nella linea curva Vpk.",
     "en": "Add, then, a force tending to the centre C reciprocally as the cube of the altitude CP or Cp, and (by what was just demonstrated) the body will deflect from the rectilinear motion into the curve line Vpk.",
     "dipende_da": [
      "Prop. XLIV"
     ],
     "figura": {
      "mostra": [
       "curva Vpk",
       "forza verso C ∝ 1/Cp³"
      ],
      "evidenzia": [
       "la retta «ruotata» diventa la curva Vpk"
      ]
     },
     "nota": "Il rimando è «per jam demonstrata», cioè la Prop. XLIV stessa."
    },
    {
     "id": "L1-P44-Cor6-p3",
     "la": "",
     "it": "E questa curva Vpk è la stessa curva VPQ trovata nel Cor. 3 della Prop. XLI, lungo la quale, come lì abbiamo detto, salgono obliquamente i corpi attratti da forze di questo tipo.",
     "en": "But this curve Vpk is the same with the curve VPQ found in Cor. 3, Prop. XLI, in which, I said, bodies attracted with such forces would ascend obliquely.",
     "dipende_da": [
      "Prop. XLI, Cor. 3"
     ],
     "figura": {
      "mostra": [],
      "evidenzia": [
       "identità con la curva del Cor. 3 della Prop. XLI"
      ]
     }
    }
   ]
  },
  {
   "id": "L1-P46",
   "tipo": "Propositio/Problema",
   "titolo": "Prop. XLVI — moto in un piano che non passa per il centro",
   "copertura": [
    "S10.01",
    "S10.02"
   ],
   "fonti": {
    "la": "",
    "en": "Motte 1846, pp. 182–183"
   },
   "enunciato": {
    "la": "",
    "it": "Posta una forza centripeta di qualsiasi genere, dati sia il centro delle forze sia un piano qualsiasi nel quale il corpo ruota, e ammesse le quadrature delle figure curvilinee, si cerca il moto di un corpo che parte da un luogo dato, con una velocità data, lungo una retta data in quel piano.",
    "en": "Any kind of centripetal force being supposed, and the centre of force, and any plane whatsoever in which the body revolves, being given, and the quadratures of curvilinear figures being allowed; it is required to determine the motion of a body going off from a given place, with a given velocity, in the direction of a given right line in that plane."
   },
   "figura_base": {
    "punti": [
     "S",
     "C",
     "P",
     "Z",
     "Q",
     "R",
     "V",
     "T"
    ],
    "vincoli": [
     "SC ⊥ piano dato, C nel piano",
     "PZ retta di partenza nel piano",
     "SV su QS proporzionale alla forza centripeta",
     "VT ∥ CQ, T su SC"
    ]
   },
   "passi": [
    {
     "id": "L1-P46-p1",
     "la": "",
     "it": "Sia S il centro delle forze, SC la distanza minima di questo centro dal piano dato, P il corpo che parte dal luogo P lungo la retta PZ, Q lo stesso corpo che ruota nella sua traiettoria, e PQR quella traiettoria, descritta nel piano dato, che bisogna trovare.",
     "en": "Let S be the centre of force, SC the least distance of that centre from the given plane, P a body issuing from the place P in the direction of the right line PZ, Q the same body revolving in its trajectory, and PQR the trajectory itself which is required to be found, described in that given plane.",
     "dipende_da": [],
     "figura": {
      "mostra": [
       "piano dato",
       "S",
       "C",
       "SC",
       "P",
       "PZ",
       "traiettoria PQR",
       "Q"
      ],
      "evidenzia": [
       "SC distanza minima dal piano"
      ]
     }
    },
    {
     "id": "L1-P46-p2",
     "la": "",
     "it": "Si congiungano CQ, QS; e se su QS si prende SV proporzionale alla forza centripeta con cui il corpo è tirato verso il centro S, e si conduce VT parallela a CQ, che incontri SC in T:",
     "en": "Join CQ, QS, and if in QS we take SV proportional to the centripetal force with which the body is attracted towards the centre S, and draw VT parallel to CQ, and meeting SC in T;",
     "dipende_da": [],
     "figura": {
      "mostra": [
       "CQ",
       "QS",
       "V su QS",
       "VT ∥ CQ",
       "T su SC"
      ],
      "evidenzia": [
       "SV ∝ forza centripeta"
      ]
     }
    },
    {
     "id": "L1-P46-p3",
     "la": "",
     "it": "la forza SV si scomporrà (per il Cor. II delle Leggi) nelle forze ST, TV; di queste, ST, tirando il corpo lungo una linea perpendicolare al piano, non muta in nulla il suo moto in questo piano.",
     "en": "then will the force SV be resolved into two (by Cor. 2, of the Laws of Motion), the force ST, and the force TV; of which ST attracting the body in the direction of a line perpendicular to that plane, does not at all change its motion in that plane.",
     "dipende_da": [
      "Leggi, Cor. II"
     ],
     "figura": {
      "mostra": [
       "ST",
       "TV"
      ],
      "evidenzia": [
       "ST ⊥ piano: non agisce nel piano"
      ]
     }
    },
    {
     "id": "L1-P46-p4",
     "la": "",
     "it": "L’altra forza, TV, agendo secondo la posizione del piano, tira il corpo direttamente verso il punto C dato nel piano, e perciò fa sì che il corpo si muova in questo piano esattamente come se la forza ST fosse tolta e il corpo ruotasse intorno al centro C nello spazio libero per effetto della sola forza TV.",
     "en": "But the action of the other force TV, coinciding with the position of the plane itself, attracts the body directly towards the given point C in that plane; and therefore causes the body to move in this plane in the same manner as if the force ST were taken away, and the body were to revolve in free space about the centre C by means of the force TV alone.",
     "dipende_da": [],
     "figura": {
      "mostra": [],
      "evidenzia": [
       "TV diretta verso C nel piano"
      ]
     }
    },
    {
     "id": "L1-P46-p5",
     "la": "",
     "it": "Ma, data la forza centripeta TV con cui il corpo Q ruota nello spazio libero intorno al centro dato C, sono dati (per la Prop. XLII) sia la traiettoria PQR che il corpo descrive, sia il luogo Q in cui il corpo si troverà in un tempo dato qualsiasi, sia infine la velocità del corpo in quel luogo Q; e viceversa. C.V.T.",
     "en": "But there being given the centripetal force TV with which the body Q revolves in free space about the given centre C, there is given (by Prop. XLII) the trajectory PQR which the body describes; the place Q, in which the body will be found at any given time; and, lastly, the velocity of the body in that place Q. And so è contra. Q.E.I.",
     "dipende_da": [
      "Prop. XLII"
     ],
     "figura": {
      "mostra": [],
      "evidenzia": [
       "problema ricondotto alla Prop. XLII con centro C"
      ]
     }
    }
   ]
  },
  {
   "id": "L1-P47",
   "tipo": "Propositio/Theorema",
   "titolo": "Prop. XLVII — forza proporzionale alla distanza: tempi uguali in ogni piano",
   "copertura": [
    "S10.03",
    "S10.04"
   ],
   "fonti": {
    "la": "",
    "en": "Motte 1846, pp. 183–184"
   },
   "enunciato": {
    "la": "",
    "it": "Posto che la forza centripeta sia proporzionale alla distanza del corpo dal centro, tutti i corpi che ruotano in piani qualsiasi descriveranno ellissi e compiranno le rivoluzioni in tempi uguali; e quelli che si muovono lungo linee rette, correndo avanti e indietro, compiranno nei medesimi tempi i singoli periodi di andata e di ritorno.",
    "en": "Supposing the centripetal force to be proportional to the distance of the body from the centre; all bodies revolving in any planes whatsoever will describe ellipses, and complete their revolutions in equal times; and those which move in right lines, running backwards and forwards alternately, will complete their several periods of going and returning in the same times."
   },
   "figura_base": {
    "punti": [
     "S",
     "C",
     "P",
     "Q",
     "R",
     "V",
     "T"
    ],
    "vincoli": [
     "come nella Prop. XLVI",
     "SV ∝ SQ"
    ]
   },
   "passi": [
    {
     "id": "L1-P47-p1",
     "la": "",
     "it": "Infatti, ferme restando le cose della proposizione precedente, la forza SV, con cui il corpo Q che ruota in un piano qualsiasi PQR è tirato verso il centro S, è come la distanza SQ; e perciò, essendo proporzionali SV e SQ, TV e CQ, la forza TV, con cui il corpo è tirato verso il punto C dato nel piano dell’orbita, è come la distanza CQ.",
     "en": "For letting all things stand as in the foregoing Proposition, the force SV, with which the body Q revolving in any plane PQR is attracted towards the centre S, is as the distance SQ; and therefore because SV and SQ, TV and CQ are proportional, the force TV with which the body is attracted towards the given point C in the plane of the orbit is as the distance CQ.",
     "dipende_da": [],
     "figura": {
      "mostra": [
       "triangoli SVT e SQC"
      ],
      "evidenzia": [
       "TV ∝ CQ"
      ]
     }
    },
    {
     "id": "L1-P47-p2",
     "la": "",
     "it": "Le forze con cui i corpi che si trovano nel piano PQR sono tirati verso il punto C sono dunque, in proporzione alle distanze, uguali alle forze con cui i corpi sono tirati da ogni parte verso il centro S; e perciò i corpi si muoveranno negli stessi tempi e nelle stesse figure in un piano qualsiasi PQR intorno al punto C e negli spazi liberi intorno al centro S; e perciò (per il Cor. 2 della Prop. X e il Cor. 2 della Prop. XXXVIII), in tempi sempre uguali, o descriveranno ellissi in quel piano intorno al centro C, o compiranno i periodi del moto avanti e indietro lungo linee rette condotte in quel piano per il centro C. C.V.D.",
     "en": "Therefore the forces with which bodies found in the plane PQR are attracted towards the point C, are in proportion to the distances equal to the forces with which the same bodies are attracted every way towards the centre S; and therefore the bodies will move in the same times, and in the same figures, in any plane PQR about the point C, as they would do in free spaces about the centre S; and therefore (by Cor. 2, Prop. X, and Cor. 2, Prop. XXXVIII.) they will in equal times either describe ellipses in that plane about the centre C, or move to and fro in right lines passing through the centre C in that plane; completing the same periods of time in all cases. Q.E.D.",
     "dipende_da": [
      "Prop. X, Cor. 2",
      "Prop. XXXVIII, Cor. 2"
     ],
     "figura": {
      "mostra": [
       "ellisse di centro C nel piano"
      ],
      "evidenzia": [
       "periodo indipendente dal piano"
      ]
     },
     "nota": "Motte aggiunge «completing the same periods of time in all cases»."
    }
   ]
  },
  {
   "id": "L1-P49",
   "tipo": "Propositio/Theorema",
   "titolo": "Prop. XLIX (e XLVIII) — lunghezza della cicloide dentro e fuori del globo",
   "copertura": [
    "S10.06",
    "S10.07",
    "S10.08",
    "S10.09"
   ],
   "fonti": {
    "la": "",
    "en": "Motte 1846, pp. 184–186"
   },
   "enunciato": {
    "la": "",
    "it": "Se una ruota poggia ad angoli retti sulla superficie interna di un globo concavo e, girando, avanza lungo un cerchio massimo, la lunghezza del cammino curvilineo che un punto qualsiasi dato sul perimetro della ruota ha percorso da quando ha toccato il globo starà al doppio del seno verso della metà dell’arco che per tutto questo tempo, nel suo andare, ha toccato il globo, come la differenza dei diametri del globo e della ruota sta al semidiametro del globo.",
    "en": "If a wheel stand upon the inside of a concave globe at right angles thereto, and revolving about its own axis go forward in one of the great circles of the globe, the length of the curvilinear path which any point, given in the perimeter of the wheel, hath described since it touched the globe, will be to the double of the versed sine of half the arc which in all that time has touched the globe in passing over it, as the difference of the diameters of the globe and the wheel to the semi-diameter of the globe."
   },
   "figura_base": {
    "punti": [
     "A",
     "B",
     "L",
     "C",
     "E",
     "P",
     "V",
     "F",
     "H",
     "G",
     "I",
     "K",
     "n",
     "o",
     "m",
     "q"
    ],
    "vincoli": [
     "ABL cerchio massimo del globo di centro C; ruota BPV di centro E tangente in B",
     "arco AB = arco PB (rotolamento)",
     "V sulla retta CE, sulla ruota; VF ⊥ CP prolungata",
     "PH, VH tangenti alla ruota in P e V; G = PH ∩ VF; GI, HK ⊥ VP",
     "cerchio nom di centro C; cerchio di centro V e raggio Vo taglia VP prolungata in q"
    ]
   },
   "passi": [
    {
     "id": "L1-P49-p1",
     "la": "",
     "it": "Sia ABL il globo, C il suo centro, BPV la ruota che poggia su di esso, E il centro della ruota, B il punto di contatto e P il punto dato sul perimetro della ruota.",
     "en": "Let ABL be the globe, C its centre, BPV the wheel insisting thereon, E the centre of the wheel, B the point of contact, and P the given point in the perimeter of the wheel.",
     "dipende_da": [],
     "figura": {
      "mostra": [
       "globo ABL",
       "C",
       "ruota BPV",
       "E",
       "B",
       "P"
      ],
      "evidenzia": []
     }
    },
    {
     "id": "L1-P49-p2",
     "la": "",
     "it": "Immagina che questa ruota proceda lungo il cerchio massimo ABL da A, per B, verso L, e che nel suo andare giri in modo che gli archi AB, PB siano sempre uguali fra loro, e che il punto P dato sul perimetro della ruota descriva intanto il cammino curvilineo AP.",
     "en": "Imagine this wheel to proceed in the great circle ABL from A through B towards L, and in its progress to revolve in such a manner that the arcs AB, PB may be always equal one to the other, and the given point P in the perimeter of the wheel may describe in the mean time the curvilinear path AP.",
     "dipende_da": [],
     "figura": {
      "mostra": [
       "A",
       "L",
       "cammino AP"
      ],
      "evidenzia": [
       "arco AB = arco PB"
      ]
     }
    },
    {
     "id": "L1-P49-p3",
     "la": "",
     "it": "Sia AP l’intero cammino curvilineo descritto da quando la ruota ha toccato il globo in A: la lunghezza AP di questo cammino starà al doppio del seno verso dell’arco ½PB come 2CE sta a CB.",
     "en": "Let AP be the whole curvilinear path described since the wheel touched the globe in A, and the length of this path AP will be to twice the versed sine of the arc [SVG 247] as 2CE to CB.",
     "dipende_da": [],
     "figura": {
      "mostra": [],
      "evidenzia": [
       "AP : 2·sinvers(½PB) = 2CE : CB"
      ]
     },
     "nota": "«12PB» = ½PB (Motte, SVG 247)."
    },
    {
     "id": "L1-P49-p4",
     "la": "",
     "it": "Infatti la retta CE (prolungata, se occorre) incontri la ruota in V; si congiungano CP, BP, EP, VP, e sul prolungamento di CP si abbassi la normale VF.",
     "en": "For let the right line CE (produced if need be) meet the wheel in V, and join CP, BP, EP, VP; produce CP, and let fall thereon the perpendicular VF.",
     "dipende_da": [],
     "figura": {
      "mostra": [
       "V",
       "CP",
       "BP",
       "EP",
       "VP",
       "VF ⊥ CP prolungata"
      ],
      "evidenzia": []
     }
    },
    {
     "id": "L1-P49-p5",
     "la": "",
     "it": "PH e VH, che si incontrano in H, tocchino il cerchio in P e in V; PH tagli VF in G, e su VP si abbassino le normali GI, HK.",
     "en": "Let PH, VH, meeting in H, touch the circle in P and V, and let PH cut VF in G, and to VP let fall the perpendiculars GI, HK.",
     "dipende_da": [],
     "figura": {
      "mostra": [
       "tangenti PH, VH",
       "H",
       "G",
       "GI",
       "HK"
      ],
      "evidenzia": []
     }
    },
    {
     "id": "L1-P49-p6",
     "la": "",
     "it": "Ancora, con centro C e raggio qualsiasi si descriva il cerchio nom, che tagli la retta CP in n, il perimetro BP della ruota in o e il cammino curvilineo AP in m; e con centro V e raggio Vo si descriva un cerchio che tagli in q il prolungamento di VP.",
     "en": "From the centre C with any interval let there be described the circle nom, cutting the right line CP in n, the perimeter of the wheel BP in o, and the curvilinear path AP in m; and from the centre V with the interval Vo let there be described a circle cutting VP produced in q.",
     "dipende_da": [],
     "figura": {
      "mostra": [
       "cerchio nom",
       "n",
       "o",
       "m",
       "cerchio di centro V e raggio Vo",
       "q"
      ],
      "evidenzia": []
     }
    },
    {
     "id": "L1-P49-p7",
     "la": "",
     "it": "Poiché la ruota, nel suo andare, gira sempre intorno al punto di contatto B, è manifesto che la retta BP è perpendicolare alla linea curva AP che il punto P della ruota descrive, e quindi che la retta VP toccherà questa curva nel punto P.",
     "en": "Because the wheel in its progress always revolves about the point of contact B, it is manifest that the right line BP is perpendicular to that curve line AP which the point P of the wheel describes, and therefore that the right line VP will touch this curve in the point P.",
     "dipende_da": [],
     "figura": {
      "mostra": [],
      "evidenzia": [
       "BP normale alla curva AP",
       "VP tangente in P"
      ]
     }
    },
    {
     "id": "L1-P49-p8",
     "la": "",
     "it": "Il raggio del cerchio nom, accresciuto o diminuito a poco a poco, diventi infine uguale alla distanza CP; e, per la similitudine della figura evanescente Pnomq e della figura PFGVI, il rapporto ultimo delle lineette evanescenti Pm, Pn, Po, Pq, cioè il rapporto dei cambiamenti momentanei della curva AP, della retta CP, dell’arco circolare BP e della retta VP, sarà lo stesso di quello delle linee PV, PF, PG, PI rispettivamente.",
     "en": "Let the radius of the circle nom be gradually increased or diminished so that at last it become equal to the distance CP; and by reason of the similitude of the evanescent figure Pnomq, and the figure PFGVI, the ultimate ratio of the evanescent lineolæ Pm, Pn, Po, Pq, that is, the ratio of the momentary mutations of the curve AP, the right line CP, the circular arc BP, and the right line VP, will be the same as of the lines PV, PF, PG, PI, respectively.",
     "dipende_da": [],
     "figura": {
      "mostra": [
       "figura evanescente Pnomq",
       "figura PFGVI"
      ],
      "evidenzia": [
       "Pm : Pn : Po : Pq = PV : PF : PG : PI"
      ]
     }
    },
    {
     "id": "L1-P49-p9",
     "la": "",
     "it": "Ma poiché VF è perpendicolare a CF e VH a CV, e perciò gli angoli HVG, VCF sono uguali, e l’angolo VHG (poiché gli angoli del quadrilatero HVEP in V e in P sono retti) è uguale all’angolo CEP, i triangoli VHG, CEP saranno simili; e di qui risulterà: come EP sta a CE, così HG sta a HV, o HP, e così KI sta a KP; e, componendo o dividendo, come CB sta a CE così PI sta a PK; e, raddoppiando i conseguenti, come CB sta a 2CE così PI sta a PV, e così Pq sta a Pm.",
     "en": "But since VF is perpendicular to CF, and VH to CV, and therefore the angles HVG, VCF equal; and the angle VHG (because the angles of the quadrilateral figure HVEP are right in V and P) is equal to the angle CEP, the triangles VHG, CEP will be similar; and thence it will come to pass that as EP is to CE so is HG to HV or HP, and so KI to KP, and by composition or division as CB to CE so is PI to PK, and doubling the consequents as CB to 2CE so PI to PV, and so is Pq to Pm.",
     "dipende_da": [],
     "figura": {
      "mostra": [
       "triangoli VHG, CEP"
      ],
      "evidenzia": [
       "CB : 2CE = PI : PV = Pq : Pm"
      ]
     }
    },
    {
     "id": "L1-P49-p10",
     "la": "",
     "it": "Il decremento della linea VP, cioè l’incremento della linea BV − VP, sta dunque all’incremento della linea curva AP nel rapporto dato di CB a 2CE; e perciò (per il corollario del Lemma IV) le lunghezze BV − VP e AP, generate da quegli incrementi, sono nello stesso rapporto.",
     "en": "Therefore the decrement of the line VP, that is, the increment of the line BV - VP to the increment of the curve line AP is in a given ratio of CB to 2CE, and therefore (by Cor. Lem. IV) the lengths BV - VP and AP, generated by those increments, are in the same ratio.",
     "dipende_da": [
      "Lemma IV, Cor."
     ],
     "figura": {
      "mostra": [
       "BV − VP"
      ],
      "evidenzia": [
       "incrementi in rapporto dato ⇒ lunghezze in rapporto dato"
      ]
     }
    },
    {
     "id": "L1-P49-p11",
     "la": "",
     "it": "Ma, se BV è il raggio, VP è il coseno dell’angolo BVP, ossia ½BEP, e perciò BV − VP è il seno verso dello stesso angolo; e perciò in questa ruota, il cui raggio è ½BV, BV − VP sarà il doppio del seno verso dell’arco ½BP.",
     "en": "But if BV be radius, VP is the cosine of the angle BVP or [SVG 248], and therefore BV - VP is the versed sine of the same angle, and therefore in this wheel, whose radius is [SVG 249], BV - VP will be double the versed sine of the arc [SVG 247].",
     "dipende_da": [],
     "figura": {
      "mostra": [
       "angolo BVP = ½BEP"
      ],
      "evidenzia": [
       "BV − VP = 2·sinvers(½BP)"
      ]
     },
     "nota": "Il latino ha qui «arcus 12BP», cioè ½BP, mentre altrove ½PB."
    },
    {
     "id": "L1-P49-p12",
     "la": "",
     "it": "Dunque AP sta al doppio del seno verso dell’arco ½PB come 2CE sta a CB. C.V.D.",
     "en": "Therefore AP is to double the versed sine of the arc [SVG 247] as 2CE to CB. Q.E.D.",
     "dipende_da": [],
     "figura": {
      "mostra": [],
      "evidenzia": [
       "AP : 2·sinvers(½PB) = 2CE : CB"
      ]
     }
    }
   ]
  },
  {
   "id": "L1-P50",
   "tipo": "Propositio/Problema",
   "titolo": "Prop. L — pendolo che oscilla in una cicloide data",
   "copertura": [
    "S10.13",
    "S10.14",
    "S10.15"
   ],
   "fonti": {
    "la": "",
    "en": "Motte 1846, pp. 186–187"
   },
   "enunciato": {
    "la": "",
    "it": "Fare in modo che un corpo pendolo oscilli in una cicloide data.",
    "en": "To cause a pendulous body to oscillate in a given cycloid."
   },
   "figura_base": {
    "punti": [
     "C",
     "Q",
     "R",
     "S",
     "O",
     "A",
     "D",
     "F",
     "P",
     "T",
     "V",
     "B",
     "W",
     "E"
    ],
    "vincoli": [
     "QRS cicloide dentro il globo QOS (centro C), cuspidi Q, S, vertice R",
     "O sull’arco QS, su CR prolungata; CA : CO = CO : CR",
     "semicicloidi AQ, AS descritte dalla ruota di diametro AO dentro il globo DAF di raggio CA",
     "filo APT = AR; AP aderisce alla semicicloide, PT rettilineo",
     "BP, TW ⊥ PT, B e W su CV"
    ]
   },
   "passi": [
    {
     "id": "L1-P50-p1",
     "la": "",
     "it": "Dentro il globo QVS, descritto con centro C, sia data la cicloide QRS, divisa a metà in R, che con i suoi punti estremi Q e S incontra da una parte e dall’altra la superficie del globo.",
     "en": "Let there be given within the globe QVS described with the centre C, the cycloid QRS, bisected in R, and meeting the superficies of the globe with its extreme points Q and S on either hand.",
     "dipende_da": [],
     "figura": {
      "mostra": [
       "globo QVS di centro C",
       "cicloide QRS",
       "R"
      ],
      "evidenzia": []
     }
    },
    {
     "id": "L1-P50-p2",
     "la": "",
     "it": "Si conduca CR, che divida a metà l’arco QS in O, e la si prolunghi fino ad A, in modo che CA stia a CO come CO sta a CR.",
     "en": "Let there be drawn CR bisecting the arc QS in O, and let it be produced to A in such sort that CA may be to CO as CO to CR.",
     "dipende_da": [],
     "figura": {
      "mostra": [
       "CR",
       "O",
       "A"
      ],
      "evidenzia": [
       "CA : CO = CO : CR"
      ]
     }
    },
    {
     "id": "L1-P50-p3",
     "la": "",
     "it": "Con centro C e raggio CA si descriva il globo esterno DAF, e dentro questo globo, per mezzo di una ruota il cui diametro sia AO, si descrivano due semicicloidi AQ, AS, che tocchino il globo interno in Q e in S e incontrino il globo esterno in A.",
     "en": "About the centre C, with the interval CA, let there be described an exterior globe DAF; and within this globe, by a wheel whose diameter is AO, let there be described two semi-cycloids AQ, AS, touching the interior globe in Q and S, and meeting the exterior globe in A.",
     "dipende_da": [],
     "figura": {
      "mostra": [
       "globo esterno DAF",
       "semicicloidi AQ, AS"
      ],
      "evidenzia": [
       "ruota di diametro AO"
      ]
     }
    },
    {
     "id": "L1-P50-p4",
     "la": "",
     "it": "Da quel punto A penda il corpo T a un filo APT uguale in lunghezza ad AR, e oscilli fra le semicicloidi AQ, AS in modo che, ogni volta che il pendolo si allontana dalla perpendicolare AR, il filo si adagi con la sua parte superiore AP sulla semicicloide APS verso la quale si compie il moto e si pieghi intorno a essa come intorno a un ostacolo, mentre la parte restante PT, alla quale la semicicloide non si oppone ancora, si stenda in linea retta: il peso T oscillerà nella cicloide data QRS. C.V.F.",
     "en": "From that point A, with a thread APT in length equal to the line AR, let the body T depend, and oscillate in such manner between the two semi-cycloids AQ, AS, that, as often as the pendulum parts from the perpendicular AR, the upper part of the thread AP may be applied to that semi-cycloid APS towards which the motion tends, and fold itself round that curve line, as if it were some solid obstacle, the remaining part of the same thread PT which has not yet touched the semi-cycloid continuing straight. Then will the weight T oscillate in the given cycloid QRS. Q.E.F.",
     "dipende_da": [],
     "figura": {
      "mostra": [
       "filo APT",
       "P",
       "T"
      ],
      "evidenzia": [
       "AP avvolto sulla semicicloide, PT rettilineo"
      ]
     },
     "nota": "Motte aggiunge «solid» («as if it were some solid obstacle»)."
    },
    {
     "id": "L1-P50-p5",
     "la": "",
     "it": "Il filo PT incontri infatti la cicloide QRS in T e il cerchio QOS in V, e si conduca CV; e sulla parte rettilinea PT del filo, dai suoi estremi P e T, si innalzino le perpendicolari BP, TW, che incontrino la retta CV in B e W.",
     "en": "For let the thread PT meet the cycloid QRS in T, and the circle QOS in V, and let CV be drawn; and to the rectilinear part of the thread PT from the extreme points P and T let there be erected the perpendiculars BP, TW, meeting the right line CV in B and W.",
     "dipende_da": [],
     "figura": {
      "mostra": [
       "V",
       "CV",
       "BP ⊥ PT",
       "TW ⊥ PT",
       "B",
       "W"
      ],
      "evidenzia": []
     }
    },
    {
     "id": "L1-P50-p6",
     "la": "",
     "it": "Dalla costruzione e dalla generazione delle figure simili AS, SR è chiaro che quelle perpendicolari PB, TW staccano da CV le lunghezze VB, VW, uguali ai diametri OA, OR delle ruote.",
     "en": "It is evident, from the construction and generation of the similar figures AS, SR, that those perpendiculars PB, TW, cut off from CV the lengths VB, VW equal the diameters of the wheels OA, OR.",
     "dipende_da": [],
     "figura": {
      "mostra": [],
      "evidenzia": [
       "VB = OA",
       "VW = OR"
      ]
     }
    },
    {
     "id": "L1-P50-p7",
     "la": "",
     "it": "TP sta dunque a VP (doppio del seno dell’angolo VBP, se ½BV è il raggio) come BW sta a BV, ossia come AO + OR sta ad AO, cioè (poiché CA a CO, CO a CR e, dividendo, AO a OR sono proporzionali) come CA + CO sta a CA, o, se si divide a metà BV in E, come 2CE sta a CB.",
     "en": "Therefore TP is to VP (which is double the sine of the angle VBP when [SVG 249] is radius) as BW to BV, or AO + OR to AO, that is (since CA and CO, CO and CR, and by division AO and OR are proportional), as CA + CO to CA, or, if BV be bisected in E, as 2CE to CB.",
     "dipende_da": [],
     "figura": {
      "mostra": [
       "E punto medio di BV"
      ],
      "evidenzia": [
       "TP : VP = 2CE : CB"
      ]
     },
     "nota": "«12BV» = ½BV (Motte, SVG 249)."
    },
    {
     "id": "L1-P50-p8",
     "la": "",
     "it": "Di conseguenza (per il Cor. 1 della Prop. XLIX) la lunghezza della parte rettilinea PT del filo è sempre uguale all’arco PS della cicloide, e il filo intero APT è sempre uguale alla metà APS della cicloide, cioè (per il Cor. 2 della Prop. XLIX) alla lunghezza AR.",
     "en": "Therefore (by Cor. 1, Prop. XLIX), the length of the rectilinear part of the thread PT is always equal to the arc of the cycloid PS, and the whole thread APT is always equal to the half of the cycloid APS, that is (by Cor. 2, Prop. XLIX), to the length AR.",
     "dipende_da": [
      "Prop. XLIX, Cor. 1",
      "Prop. XLIX, Cor. 2"
     ],
     "figura": {
      "mostra": [
       "arco PS",
       "semicicloide APS"
      ],
      "evidenzia": [
       "PT = arco PS",
       "APT = APS = AR"
      ]
     }
    },
    {
     "id": "L1-P50-p9",
     "la": "",
     "it": "E perciò, viceversa, se il filo resta sempre uguale alla lunghezza AR, il punto T si muoverà nella cicloide data QRS. C.V.D.",
     "en": "And therefore contrariwise, if the string remain always equal to the length AR, the point T will always move in the given cycloid QRS. Q.E.D.",
     "dipende_da": [],
     "figura": {
      "mostra": [],
      "evidenzia": [
       "T descrive la cicloide QRS"
      ]
     }
    }
   ]
  },
  {
   "id": "L1-P51",
   "tipo": "Propositio/Theorema",
   "titolo": "Prop. LI — isocronismo del pendolo cicloidale",
   "copertura": [
    "S10.17",
    "S10.18"
   ],
   "fonti": {
    "la": "",
    "en": "Motte 1846, pp. 187–188"
   },
   "enunciato": {
    "la": "",
    "it": "Se la forza centripeta che tende da ogni parte al centro C di un globo è, nei singoli luoghi, come la distanza di ciascun luogo dal centro, e per l’azione di questa sola forza il corpo T oscilla (nel modo ora descritto) sul perimetro della cicloide QRS, dico che i tempi delle oscillazioni, per quanto disuguali, saranno uguali.",
    "en": "If a centripetal force tending on all sides to the centre C of a globe, be in all places as the distance of the place from the centre, and by this force alone acting upon it, the body T oscillate (in the manner above described) in the perimeter of the cycloid QRS; I say, that all the oscillations, how unequal soever in themselves, will be performed in equal times."
   },
   "figura_base": {
    "punti": [
     "C",
     "A",
     "P",
     "T",
     "W",
     "X",
     "V",
     "R",
     "t",
     "S",
     "Q"
    ],
    "vincoli": [
     "come nella Prop. L",
     "TW tangente alla cicloide in T (perpendicolare al filo PT)",
     "CX ⊥ TW, X su TW"
    ]
   },
   "passi": [
    {
     "id": "L1-P51-p1",
     "la": "",
     "it": "Infatti sulla tangente TW della cicloide, prolungata all’infinito, cada la perpendicolare CX, e si congiunga CT.",
     "en": "For upon the tangent TW infinitely produced let fall the perpendicular CX, and join CT.",
     "dipende_da": [],
     "figura": {
      "mostra": [
       "tangente TW prolungata",
       "CX ⊥ TW",
       "CT"
      ],
      "evidenzia": []
     }
    },
    {
     "id": "L1-P51-p2",
     "la": "",
     "it": "Poiché la forza centripeta con cui il corpo T è spinto verso C è come la distanza CT, e questa (per il Cor. II delle Leggi) si scompone nelle parti CX, TX, delle quali CX, spingendo il corpo direttamente via da P, tende il filo PT e, per la resistenza di questo, si annulla del tutto senza produrre alcun altro effetto, mentre l’altra parte, TX, sollecitando il corpo trasversalmente, cioè verso X, accelera direttamente il suo moto nella cicloide, è manifesto che l’accelerazione del corpo, proporzionale a questa forza acceleratrice, è in ogni istante come la lunghezza TX, cioè, essendo date CV, WV, e proporzionali a esse TX, TW, come la lunghezza TW, cioè (per il Cor. 1 della Prop. XLIX) come la lunghezza dell’arco TR della cicloide.",
     "en": "Because the centripetal force with which the body T is impelled towards C is as the distance CT, let this (by Cor. 2, of the Laws) be resolved into the parts CX, TX, of which CX impelling the body directly from P stretches the thread PT, and by the resistance the thread makes to it is totally employed, producing no other effect; but the other part TX, impelling the body transversely or towards X, directly accelerates the motion in the cycloid. Then it is plain that the acceleration of the body, proportional to this accelerating force, will be every moment as the length TX, that is (because CV, WV, and TX, TW proportional to them are given), as the length TW, that is (by Cor. 1, Prop. XLIX) as the length of the arc of the cycloid TR.",
     "dipende_da": [
      "Leggi, Cor. II",
      "Prop. XLIX, Cor. 1"
     ],
     "figura": {
      "mostra": [
       "componenti CX e TX della forza CT"
      ],
      "evidenzia": [
       "accelerazione ∝ TX ∝ TW ∝ arco TR"
      ]
     }
    },
    {
     "id": "L1-P51-p3",
     "la": "",
     "it": "Se dunque due pendoli APT, Apt vengono allontanati in misura disuguale dalla perpendicolare AR e lasciati andare insieme, le loro accelerazioni saranno sempre come gli archi da descrivere TR, tR.",
     "en": "If therefore two pendulums APT, Apt, be unequally drawn aside from the perpendicular AR, and let fall together, their accelerations will be always as the arcs to be described TR, tR.",
     "dipende_da": [],
     "figura": {
      "mostra": [
       "secondo pendolo Apt",
       "t"
      ],
      "evidenzia": [
       "accelerazioni ∝ TR, tR"
      ]
     }
    },
    {
     "id": "L1-P51-p4",
     "la": "",
     "it": "Ma le parti descritte all’inizio sono come le accelerazioni, cioè come gli archi interi da descrivere all’inizio; e perciò le parti che restano da descrivere, e le accelerazioni successive, proporzionali a queste parti, sono anch’esse come gli interi; e così di seguito.",
     "en": "But the parts described at the beginning of the motion are as the accelerations, that is, as the wholes that are to be described at the beginning, and therefore the parts which remain to be described, and the subsequent accelerations proportional to those parts, are also as the wholes, and so on.",
     "dipende_da": [],
     "figura": {
      "mostra": [],
      "evidenzia": [
       "parti proporzionali agli interi"
      ]
     }
    },
    {
     "id": "L1-P51-p5",
     "la": "",
     "it": "Le accelerazioni, dunque, e quindi le velocità generate, le parti descritte con queste velocità e le parti da descrivere sono sempre come gli interi; e perciò le parti da descrivere, conservando fra loro un rapporto dato, svaniranno insieme, cioè i due corpi oscillanti giungeranno insieme alla perpendicolare AR.",
     "en": "Therefore the accelerations, and consequently the velocities generated, and the parts described with those velocities, and the parts to be described, are always as the wholes; and therefore the parts to be described preserving a given ratio to each other will vanish together, that is, the two bodies oscillating will arrive together at the perpendicular AR.",
     "dipende_da": [],
     "figura": {
      "mostra": [],
      "evidenzia": [
       "arrivo simultaneo in R"
      ]
     }
    },
    {
     "id": "L1-P51-p6",
     "la": "",
     "it": "E poiché, a loro volta, le salite dei pendoli dal luogo più basso R, compiute con moto retrogrado lungo gli stessi archi cicloidali, sono ritardate nei singoli luoghi dalle stesse forze dalle quali erano accelerate le discese, è chiaro che le velocità delle salite e delle discese compiute lungo gli stessi archi sono uguali, e che perciò esse avvengono in tempi uguali; e perciò, essendo simili e uguali le due parti RS e RQ della cicloide, che giacciono dall’una e dall’altra parte della perpendicolare, i due pendoli compiranno sempre negli stessi tempi le loro oscillazioni, sia intere sia dimezzate. C.V.D.",
     "en": "And since on the other hand the ascent of the pendulums from the lowest place R through the same cycloidal arcs with a retrograde motion, is retarded in the several places they pass through by the same forces by which their descent was accelerated; it is plain that the velocities of their ascent and descent through the same arcs are equal, and consequently performed in equal times; and, therefore, since the two parts of the cycloid RS and RQ lying on either side of the perpendicular are similar and equal, the two pendulums will perform as well the wholes as the halves of their oscillations in the same times. Q.E.D.",
     "dipende_da": [],
     "figura": {
      "mostra": [
       "archi RS, RQ"
      ],
      "evidenzia": [
       "simmetria di salita e discesa"
      ]
     },
     "nota": "Il latino ha «ascensus perpendiculorum»: qui *perpendicula* sono i pendoli (Motte «pendulums»)."
    }
   ]
  },
  {
   "id": "L1-P52",
   "tipo": "Propositio/Problema",
   "titolo": "Prop. LII — velocità e tempi del pendolo cicloidale",
   "copertura": [
    "S10.20",
    "S10.21",
    "S10.22"
   ],
   "fonti": {
    "la": "",
    "en": "Motte 1846, pp. 188–190"
   },
   "enunciato": {
    "la": "",
    "it": "Determinare sia le velocità dei pendoli nei singoli luoghi, sia i tempi in cui si compiono tanto le oscillazioni intere quanto le singole parti delle oscillazioni.",
    "en": "To define the velocities of the pendulums in the several places, and the times in which both the entire oscillations, and the several parts of them are performed."
   },
   "figura_base": {
    "punti": [
     "G",
     "H",
     "K",
     "M",
     "I",
     "L",
     "Y",
     "Z",
     "S",
     "T",
     "R"
    ],
    "vincoli": [
     "semicerchio HKM di centro G e raggio GH = arco RS",
     "GK ⊥ HM",
     "L su HG con LG = TR; I sul semicerchio con LI ⊥ HG",
     "HY nascente su HG; YZ ⊥ HG, Z sul semicerchio"
    ]
   },
   "passi": [
    {
     "id": "L1-P52-p1",
     "la": "",
     "it": "Con centro in un punto qualsiasi G e raggio GH uguale all’arco RS della cicloide, descrivi il semicerchio HKM, diviso a metà dal semidiametro GK.",
     "en": "About any centre G, with the interval GH equal to the arc of the cycloid RS, describe a semi-circle HKM bisected by the semi-diameter GK.",
     "dipende_da": [],
     "figura": {
      "mostra": [
       "semicerchio HKM",
       "G",
       "GK"
      ],
      "evidenzia": [
       "GH = arco RS"
      ]
     }
    },
    {
     "id": "L1-P52-p2",
     "la": "",
     "it": "E se una forza centripeta proporzionale alle distanze dei luoghi dal centro tende al centro G ed è, sul perimetro HIK, uguale alla forza centripeta che, sul perimetro del globo QOS, tende al centro di questo; e se, nello stesso tempo in cui il pendolo T viene lasciato andare dal luogo più alto S, un corpo L cade da H verso G: poiché le forze da cui i corpi sono sollecitati sono uguali all’inizio e sempre proporzionali agli spazi da descrivere TR, LG, e perciò, se TR e LG sono uguali, sono uguali nei luoghi T e L, è chiaro che quei corpi descrivono all’inizio spazi uguali ST, HL, e quindi continuano in seguito a essere sollecitati in egual misura e a descrivere spazi uguali.",
     "en": "And if a centripetal force proportional to the distance of the places from the centre tend to the centre G, and it be in the perimeter HIK equal to the centripetal force in the perimeter of the globe QOS tending towards its centre, and at the same time that the pendulum T is let fall from the highest place S, a body, as L, is let fall from H to G; then because the forces which act upon the bodies are equal at the beginning, and always proportional to the spaces to be described TR, LG, and therefore if TR and LG are equal, are also equal in the places T and L, it is plain that those bodies describe at the beginning equal spaces ST, HL, and therefore are still acted upon equally, and continue to describe equal spaces.",
     "dipende_da": [],
     "figura": {
      "mostra": [
       "corpo L su HG"
      ],
      "evidenzia": [
       "TR = LG ⇒ forze uguali",
       "ST = HL"
      ]
     },
     "nota": "Latino «si æquantur TR ad LG»: costrutto anomalo, inteso come «se TR e LG sono uguali» (così anche Motte)."
    },
    {
     "id": "L1-P52-p3",
     "la": "",
     "it": "Perciò (per la Prop. XXXVIII) il tempo in cui il corpo descrive l’arco ST sta al tempo di una oscillazione come l’arco HI, tempo in cui il corpo H giungerà in L, sta alla semicirconferenza HKM, tempo in cui il corpo H giungerà in M.",
     "en": "Therefore by Prop. XXXVIII, the time in which the body describes the arc ST is to the time of one oscillation, as the arc HI the time in which the body H arrives at L, to the semi-periphery HKM, the time in which the body H will come to M.",
     "dipende_da": [
      "Prop. XXXVIII"
     ],
     "figura": {
      "mostra": [
       "I",
       "arco HI"
      ],
      "evidenzia": [
       "tempo ∝ arco HI"
      ]
     }
    },
    {
     "id": "L1-P52-p4",
     "la": "",
     "it": "E la velocità del corpo pendolo nel luogo T sta alla sua velocità nel luogo più basso R (cioè la velocità del corpo H nel luogo L sta alla sua velocità nel luogo G, ossia l’incremento momentaneo della linea HL sta all’incremento momentaneo della linea HG, mentre gli archi HI, HK crescono con flusso uniforme) come l’ordinata LI sta al raggio GK, ossia come √(SR² − TR²) sta a SR.",
     "en": "And the velocity of the pendulous body in the place T is to its velocity in the lowest place R, that is, the velocity of the body H in the place L to its velocity in the place G, or the momentary increment of the line HL to the momentary increment of the line HG (the arcs HI, HK increasing with an equable flux) as the ordinate LI to the radius GK, or as [SVG 250] to SR.",
     "dipende_da": [],
     "figura": {
      "mostra": [
       "ordinata LI"
      ],
      "evidenzia": [
       "v(T) : v(R) = LI : GK = √(SR² − TR²) : SR"
      ]
     },
     "nota": "Radice persa nella trascrizione: «SR q.−TR q.» va letto √(SR² − TR²) (Motte, SVG 250)."
    },
    {
     "id": "L1-P52-p5",
     "la": "",
     "it": "Di qui, poiché nelle oscillazioni disuguali si descrivono in tempi uguali archi proporzionali agli archi interi delle oscillazioni, dai tempi dati si hanno sia le velocità sia gli archi descritti in tutte le oscillazioni. Erano queste le prime cose da trovare.",
     "en": "Hence, since in unequal oscillations there are described in equal time arcs proportional to the entire arcs of the oscillations, there are obtained from the times given, both the velocities and the arcs described in all the oscillations universally. Which was first required.",
     "dipende_da": [],
     "figura": {
      "mostra": [],
      "evidenzia": [
       "archi descritti in tempi uguali ∝ archi interi"
      ]
     }
    },
    {
     "id": "L1-P52-p6",
     "la": "",
     "it": "Oscillino ora corpi appesi a fili in cicloidi diverse descritte dentro globi diversi, le cui forze assolute sono anch’esse diverse; e, se la forza assoluta di un globo qualsiasi QOS si chiama V, la forza acceleratrice da cui il pendolo è sollecitato sulla circonferenza di questo globo, quando comincia a muoversi direttamente verso il suo centro, sarà come la distanza del corpo pendolo da quel centro e la forza assoluta del globo considerate congiuntamente, cioè come CO × V.",
     "en": "Let now any pendulous bodies oscillate in different cycloids described within different globes, whose absolute forces are also different; and if the absolute force of any globe QOS be called V, the accelerative force with which the pendulum is acted on in the circumference of this globe, when it begins to move directly towards its centre, will be as the distance of the pendulous body from that centre and the absolute force of the globe conjunctly, that is, as CO × V.",
     "dipende_da": [],
     "figura": {
      "mostra": [],
      "evidenzia": [
       "forza acceleratrice iniziale ∝ CO × V"
      ]
     }
    },
    {
     "id": "L1-P52-p7",
     "la": "",
     "it": "Perciò la lineetta HY, che sia come questa forza acceleratrice CO × V, sarà descritta in un tempo dato; e, se si innalza la normale YZ, che incontri la circonferenza in Z, l’arco nascente HZ rappresenterà quel tempo dato.",
     "en": "Therefore the lineola HY, which is as this accelerated force CO × V, will be described in a given time; and if there be erected the perpendicular YZ meeting the circumference in Z, the nascent arc HZ will denote that given time.",
     "dipende_da": [],
     "figura": {
      "mostra": [
       "HY",
       "YZ",
       "Z",
       "arco HZ"
      ],
      "evidenzia": [
       "arco HZ rappresenta il tempo dato"
      ]
     }
    },
    {
     "id": "L1-P52-p8",
     "la": "",
     "it": "Ma questo arco nascente HZ è in rapporto subduplicato del rettangolo GHY, e perciò come √(GH × CO × V).",
     "en": "But that nascent arc HZ is in the subduplicate ratio of the rectangle GHY, and therefore as [SVG 251].",
     "dipende_da": [],
     "figura": {
      "mostra": [],
      "evidenzia": [
       "HZ ∝ √(GH × CO × V)"
      ]
     },
     "nota": "Radice persa nella trascrizione: «GH×CO×V» = √(GH × CO × V)."
    },
    {
     "id": "L1-P52-p9",
     "la": "",
     "it": "Di qui il tempo di un’oscillazione intera nella cicloide QRS (poiché è direttamente come la semicirconferenza HKM, che rappresenta quell’oscillazione intera, e inversamente come l’arco HZ, che rappresenta similmente il tempo dato) risulterà direttamente come GH e inversamente come √(GH × CO × V), cioè, essendo uguali GH e SR, come √(SR/(CO × V)), ossia (per il corollario della Prop. L) come √(AR/(AC × V)).",
     "en": "Whence the time of an entire oscillation in the cycloid QRS (it being as the semi-periphery HKM, which denotes that entire oscillation, directly; and as the arc HZ which in like manner denotes a given time inversely) will be as GH directly and [SVG 252] inversely; that is, because GH and SR are equal, as [SVG 253], or (by Cor. Prop. L.) as [SVG 254].",
     "dipende_da": [
      "Prop. L, Cor."
     ],
     "figura": {
      "mostra": [],
      "evidenzia": [
       "T ∝ √(SR/(CO·V)) = √(AR/(AC·V))"
      ]
     },
     "nota": "Nella trascrizione «directæ» per «directe» (refuso probabile) e radici perse in «SRCO×V», «ARAC×V»."
    },
    {
     "id": "L1-P52-p10",
     "la": "",
     "it": "Perciò le oscillazioni compiute in tutti i globi e in tutte le cicloidi, con forze assolute qualsiasi, sono nel rapporto composto dal rapporto subduplicato della lunghezza del filo, direttamente, dal rapporto subduplicato della distanza fra il punto di sospensione e il centro del globo, inversamente, e dal rapporto subduplicato della forza assoluta del globo, anch’esso inversamente. C.V.T.",
     "en": "Therefore the oscillations in all globes and cycloids, performed with what absolute forces soever, are in a ratio compounded of the subduplicate ratio of the length of the string directly, and the subduplicate ratio of the distance between the point of suspension and the centre of the globe inversely, and the subduplicate ratio of the absolute force of the globe inversely also. Q.E.I.",
     "dipende_da": [],
     "figura": {
      "mostra": [],
      "evidenzia": [
       "legge composta dei tempi"
      ]
     }
    }
   ]
  },
  {
   "id": "L1-P53",
   "tipo": "Propositio/Problema",
   "titolo": "Prop. LIII — forze che rendono isocrone le oscillazioni su una curva data",
   "copertura": [
    "S10.26",
    "S10.27",
    "S10.28"
   ],
   "fonti": {
    "la": "",
    "en": "Motte 1846, pp. 190–191"
   },
   "enunciato": {
    "la": "",
    "it": "Ammesse le quadrature delle figure curvilinee, trovare le forze per effetto delle quali i corpi compiranno in linee curve date oscillazioni sempre isocrone.",
    "en": "Granting the quadratures of curvilinear figures, it is required to find the forces with which bodies moving in given curve lines may always perform their oscillations in equal times."
   },
   "figura_base": {
    "punti": [
     "S",
     "T",
     "R",
     "Q",
     "A",
     "C",
     "X",
     "Y",
     "Z",
     "P"
    ],
    "vincoli": [
     "STRQ curva data, asse AR per il centro C",
     "TX tangente in T; TY = arco TR",
     "YZ ⊥ TX; Z su CT"
    ]
   },
   "passi": [
    {
     "id": "L1-P53-p1",
     "la": "",
     "it": "Oscilli il corpo T in una linea curva qualsiasi STRQ, il cui asse AR passi per il centro delle forze C.",
     "en": "Let the body T oscillate in any curve line STRQ, whose axis is AR passing through the centre of force C.",
     "dipende_da": [],
     "figura": {
      "mostra": [
       "curva STRQ",
       "asse AR",
       "C",
       "T"
      ],
      "evidenzia": []
     }
    },
    {
     "id": "L1-P53-p2",
     "la": "",
     "it": "Si conduca TX, che tocchi quella curva in un luogo qualsiasi T del corpo, e su questa tangente TX si prenda TY uguale all’arco TR.",
     "en": "Draw TX touching that curve in any place of the body T, and in that tangent TX take TY equal to the arc TR.",
     "dipende_da": [],
     "figura": {
      "mostra": [
       "tangente TX",
       "Y"
      ],
      "evidenzia": [
       "TY = arco TR"
      ]
     }
    },
    {
     "id": "L1-P53-p3",
     "la": "",
     "it": "La lunghezza di quell’arco, infatti, si conosce dalle quadrature delle figure con i metodi comuni.",
     "en": "The length of that arc is known from the common methods used for the quadratures of figures.",
     "dipende_da": [],
     "figura": {
      "mostra": [],
      "evidenzia": []
     }
    },
    {
     "id": "L1-P53-p4",
     "la": "",
     "it": "Dal punto Y si conduca la retta YZ perpendicolare alla tangente.",
     "en": "From the point Y draw the right line YZ perpendicular to the tangent.",
     "dipende_da": [],
     "figura": {
      "mostra": [
       "YZ ⊥ TX"
      ],
      "evidenzia": []
     }
    },
    {
     "id": "L1-P53-p5",
     "la": "",
     "it": "Si conduca CT, che incontri quella perpendicolare in Z: la forza centripeta sarà proporzionale alla retta TZ. C.V.T.",
     "en": "Draw CT meeting that perpendicular in Z, and the centripetal force will be proportional to the right line TZ. Q.E.I.",
     "dipende_da": [],
     "figura": {
      "mostra": [
       "CT",
       "Z"
      ],
      "evidenzia": [
       "forza ∝ TZ"
      ]
     }
    },
    {
     "id": "L1-P53-p6",
     "la": "",
     "it": "Infatti, se la forza con cui il corpo è tirato da T verso C si rappresenta con la retta TZ, presa proporzionale a essa, questa si scomporrà nelle forze TY, YZ; di queste, YZ, tirando il corpo secondo la lunghezza del filo PT, non muta in nulla il suo moto, mentre l’altra forza, TY, accelera o ritarda direttamente il suo moto nella curva STRQ.",
     "en": "For if the force with which the body is attracted from T towards C be expressed by the right line TZ taken proportional to it, that force will be resolved into two forces TY, YZ, of which YZ drawing the body in the direction of the length of the thread PT, does not at all change its motion; whereas the other force TY directly accelerates or retards its motion in the curve STRQ.",
     "dipende_da": [],
     "figura": {
      "mostra": [
       "componenti TY e YZ"
      ],
      "evidenzia": [
       "solo TY agisce lungo la curva"
      ]
     },
     "nota": "Il «filo PT» non è definito in questa proposizione: viene dalla costruzione della Prop. L."
    },
    {
     "id": "L1-P53-p7",
     "la": "",
     "it": "Di conseguenza, poiché questa forza è come il cammino da descrivere TR, le accelerazioni o i ritardi del corpo, nel descrivere parti proporzionali di due oscillazioni (una maggiore e una minore), saranno sempre come quelle parti, e perciò faranno sì che quelle parti siano descritte insieme.",
     "en": "Wherefore since that force is as the space to be described TR, the accelerations or retardations of the body in describing two proportional parts (a greater and a less) of two oscillations, will be always as those parts, and therefore will cause those parts to be described together.",
     "dipende_da": [],
     "figura": {
      "mostra": [],
      "evidenzia": [
       "forza tangenziale ∝ arco da descrivere"
      ]
     }
    },
    {
     "id": "L1-P53-p8",
     "la": "",
     "it": "Ma i corpi che descrivono insieme parti sempre proporzionali agli interi descriveranno insieme gli interi. C.V.D.",
     "en": "But bodies which continually describe together parts proportional to the wholes, will describe the wholes together also. Q.E.D.",
     "dipende_da": [],
     "figura": {
      "mostra": [],
      "evidenzia": [
       "isocronismo"
      ]
     }
    }
   ]
  },
  {
   "id": "L1-P53-Cor1",
   "tipo": "Corollarium",
   "titolo": "Prop. LIII, Cor. 1 — pendolo circolare reso isocrono",
   "copertura": [
    "S10.29"
   ],
   "fonti": {
    "la": "",
    "en": "Motte 1846, p. 191"
   },
   "enunciato": {
    "la": "",
    "it": "Di qui, se il corpo T, appeso con un filo rettilineo AT al centro A, descrive l’arco circolare STRQ, e intanto è sollecitato verso il basso, lungo linee parallele, da una forza che stia alla forza uniforme della gravità come l’arco TR sta al suo seno TN, i tempi delle singole oscillazioni saranno uguali.",
    "en": "Hence if the body T, hanging by a rectilinear thread AT from the centre A, describe the circular arc STRQ, and in the mean time be acted on by any force tending downwards with parallel directions, which is to the uniform force of gravity as the arc TR to its sine TN, the times of the several oscillations will be equal."
   },
   "figura_base": {
    "punti": [
     "A",
     "T",
     "S",
     "R",
     "Q",
     "N",
     "Y",
     "Z"
    ],
    "vincoli": [
     "arco circolare STRQ di centro A, raggio AT; AR verticale",
     "TN seno dell’arco TR (TN ⊥ AR)",
     "TY = arco TR sulla tangente; TZ ∥ AR"
    ]
   },
   "passi": [
    {
     "id": "L1-P53-Cor1-p1",
     "la": "",
     "it": "Infatti, essendo parallele TZ e AR, i triangoli ATN, ZTY saranno simili; e perciò TZ starà ad AT come TY sta a TN; cioè, se la forza uniforme della gravità si rappresenta con la lunghezza data AT, la forza TZ, per effetto della quale le oscillazioni riusciranno isocrone, starà alla forza di gravità AT come l’arco TR, uguale a TY, sta al seno TN di quell’arco.",
     "en": "For because TZ, AR are parallel, the triangles ATN, ZTY are similar; and therefore TZ will be to AT as TY to TN; that is, if the uniform force of gravity be expressed by the given length AT, the force TZ, by which the oscillations become isochronous, will be to the force of gravity AT, as the arc TR equal to TY is to TN the sine of that arc.",
     "dipende_da": [],
     "figura": {
      "mostra": [
       "triangoli ATN, ZTY"
      ],
      "evidenzia": [
       "TZ : AT = arco TR : TN"
      ]
     },
     "nota": "Nell’enunciato la trascrizione ha «erun» per «erunt» (refuso probabile)."
    }
   ]
  },
  {
   "id": "L1-P54",
   "tipo": "Propositio/Problema",
   "titolo": "Prop. LIV — tempi di discesa lungo curve date",
   "copertura": [
    "S10.31",
    "S10.32"
   ],
   "fonti": {
    "la": "",
    "en": "Motte 1846, pp. 191–192"
   },
   "enunciato": {
    "la": "",
    "it": "Ammesse le quadrature delle figure curvilinee, trovare i tempi in cui i corpi, per effetto di una forza centripeta qualsiasi, scenderanno e saliranno lungo linee curve qualsiasi descritte in un piano passante per il centro delle forze.",
    "en": "Granting the quadratures of curvilinear figures, it is required to find the times in which bodies by means of any centripetal force will descend or ascend in any curve lines described in a plane passing through the centre of force."
   },
   "figura_base": {
    "punti": [
     "S",
     "T",
     "t",
     "R",
     "C",
     "D",
     "d",
     "N",
     "n",
     "P",
     "Q"
    ],
    "vincoli": [
     "STtR curva nel piano per C",
     "D, d su CS con Dd nascente; cerchi DT, dt di centro C",
     "DN ⊥ CS proporzionale al tempo lungo Tt",
     "SQ ⊥ CS asintoto della curva PNn"
    ]
   },
   "passi": [
    {
     "id": "L1-P54-p1",
     "la": "",
     "it": "Scenda il corpo da un luogo qualsiasi S lungo una linea curva qualsiasi STtR, data in un piano passante per il centro delle forze C.",
     "en": "Let the body descend from any place S, and move in any curve STtR given in a plane passing through the centre of force C.",
     "dipende_da": [],
     "figura": {
      "mostra": [
       "curva STtR",
       "C",
       "S"
      ],
      "evidenzia": []
     }
    },
    {
     "id": "L1-P54-p2",
     "la": "",
     "it": "Si congiunga CS e la si divida in innumerevoli parti uguali, e sia Dd una di queste parti.",
     "en": "Join CS, and let it be divided into innumerable equal parts, and let Dd be one of those parts.",
     "dipende_da": [],
     "figura": {
      "mostra": [
       "CS",
       "Dd"
      ],
      "evidenzia": []
     }
    },
    {
     "id": "L1-P54-p3",
     "la": "",
     "it": "Con centro C e raggi CD, Cd si descrivano i cerchi DT, dt, che incontrino la linea curva STtR in T e t.",
     "en": "From the centre C, with the intervals CD, Cd, let the circles DT, dt be described, meeting the curve line STtR in T and t.",
     "dipende_da": [],
     "figura": {
      "mostra": [
       "cerchi DT, dt",
       "T",
       "t"
      ],
      "evidenzia": []
     }
    },
    {
     "id": "L1-P54-p4",
     "la": "",
     "it": "E, data sia la legge della forza centripeta sia l’altezza CS da cui il corpo è caduto, sarà data (per la Prop. XXXIX) la velocità del corpo in qualsiasi altra altezza CT.",
     "en": "And because the law of centripetal force is given, and also the altitude CS from which the body at first fell, there will be given the velocity of the body in any other altitude CT (by Prop. XXXIX).",
     "dipende_da": [
      "Prop. XXXIX"
     ],
     "figura": {
      "mostra": [],
      "evidenzia": [
       "velocità a ogni altezza CT"
      ]
     },
     "nota": "Nella trascrizione la parentesi «(per prop. xxxix.)» chiude la frase senza punto finale."
    },
    {
     "id": "L1-P54-p5",
     "la": "",
     "it": "Il tempo in cui il corpo descrive la lineetta Tt è poi come la lunghezza di questa lineetta, cioè come la secante dell’angolo tTC, direttamente, e come la velocità, inversamente.",
     "en": "But the time in which the body describes the lineola Tt is as the length of that lineola, that is, as the secant of the angle tTC directly, and the velocity inversely.",
     "dipende_da": [],
     "figura": {
      "mostra": [
       "angolo tTC"
      ],
      "evidenzia": [
       "tempo ∝ secante(tTC)/velocità"
      ]
     },
     "nota": "Nella trascrizione c’è una parentesi chiusa in eccesso dopo «tTC»."
    },
    {
     "id": "L1-P54-p6",
     "la": "",
     "it": "Sia proporzionale a questo tempo l’ordinata DN, perpendicolare alla retta CS nel punto D; ed essendo data Dd, il rettangolo Dd × DN, cioè l’area DNnd, sarà proporzionale allo stesso tempo.",
     "en": "Let the ordinate DN, proportional to this time, be made perpendicular to the right line CS at the point D, and because Dd is given, the rectangle Dd × DN, that is, the area DNnd, will be proportional to the same time.",
     "dipende_da": [],
     "figura": {
      "mostra": [
       "DN",
       "area DNnd"
      ],
      "evidenzia": [
       "area DNnd ∝ tempo"
      ]
     }
    },
    {
     "id": "L1-P54-p7",
     "la": "",
     "it": "Dunque, se PNn è la linea curva che il punto N tocca di continuo, e il suo asintoto è la retta SQ, perpendicolare alla retta CS, l’area SQPND sarà proporzionale al tempo in cui il corpo, scendendo, ha descritto la linea ST; e perciò, trovata quell’area, sarà dato il tempo. C.V.T.",
     "en": "Therefore if PNn be a curve line in which the point N is perpetually found, and its asymptote be the right line SQ standing upon the line CS at right angles, the area SQPND will be proportional to the time in which the body in its descent hath described the line ST; and therefore that area being found, the time is also given. Q.E.I.",
     "dipende_da": [],
     "figura": {
      "mostra": [
       "curva PNn",
       "asintoto SQ",
       "area SQPND"
      ],
      "evidenzia": [
       "area ∝ tempo di discesa"
      ]
     }
    }
   ]
  },
  {
   "id": "L1-P55",
   "tipo": "Propositio/Theorema",
   "titolo": "Prop. LV — legge delle aree per la traccia su una superficie di rivoluzione",
   "copertura": [
    "S10.33",
    "S10.34",
    "S10.35"
   ],
   "fonti": {
    "la": "",
    "en": "Motte 1846, pp. 192–193"
   },
   "enunciato": {
    "la": "",
    "it": "Se un corpo si muove su una superficie curva qualsiasi il cui asse passa per il centro delle forze, e dal corpo si abbassa sull’asse una perpendicolare, e da un punto qualsiasi dell’asse si conduce una retta parallela e uguale a essa, dico che quella parallela descriverà un’area proporzionale al tempo.",
    "en": "If a body move in any curve superficies, whose axis passes through the centre of force, and from the body a perpendicular be let fall upon the axis; and a line parallel and equal thereto be drawn from any given point of the axis; I say, that this parallel line will describe an area proportional to the time."
   },
   "figura_base": {
    "punti": [
     "B",
     "K",
     "L",
     "T",
     "S",
     "R",
     "O",
     "M",
     "N",
     "P",
     "A",
     "C",
     "G",
     "I",
     "F",
     "H"
    ],
    "vincoli": [
     "BKL superficie curva con asse OMK passante per C",
     "TN ⊥ asse; OP ∥ TN e OP = TN, nel piano AOP ⊥ asse",
     "AP traccia della traiettoria nel piano AOP",
     "TG su TC ∝ forza centripeta; TI su TM (normale) ∝ pressione",
     "PTF ∥ asse; GF, IH ⊥ PF"
    ]
   },
   "passi": [
    {
     "id": "L1-P55-p1",
     "la": "",
     "it": "Sia BKL la superficie curva, T il corpo che ruota su di essa, STR la traiettoria che il corpo descrive su di essa, S l’inizio della traiettoria, OMK l’asse della superficie curva, TN la retta condotta dal corpo perpendicolarmente all’asse, OP la retta parallela e uguale a questa condotta dal punto O dato sull’asse; AP la traccia della traiettoria descritta dal punto P nel piano AOP della linea rotante OP; A l’inizio della traccia, corrispondente al punto S; TC la retta condotta dal corpo al centro; TG la sua parte proporzionale alla forza centripeta con cui il corpo è sollecitato verso il centro C; TM la retta perpendicolare alla superficie curva; TI la sua parte proporzionale alla forza di pressione con cui il corpo preme la superficie e, a sua volta, è premuto dalla superficie verso M; PTF la retta parallela all’asse passante per il corpo, e GF, IH le rette abbassate perpendicolarmente dai punti G e I su quella parallela PHTF.",
     "en": "Let BKL be a curve superficies, T a body revolving in it, STR a trajectory which the body describes in the same, S the beginning of the trajectory, OMK the axis of the curve superficies, TN a right line let fall perpendicularly from the body to the axis; OP a line parallel and equal thereto drawn from the given point O in the axis; AP the orthographic projection of the trajectory described by the point P in the plane AOP in which the revolving line OP is found; A the beginning of that projection, answering to the point S; TC a right line drawn from the body to the centre; TG a part thereof proportional to the centripetal force with which the body tends towards the centre C; TM a right line perpendicular to the curve superficies; TI a part thereof proportional to the force of pressure with which the body urges the superficies, and therefore with which it is again repelled by the superficies towards M; PTF a right line parallel to the axis and passing through the body, and GF, IH right lines let fall perpendicularly from the points G and I upon that parallel PHTF.",
     "dipende_da": [],
     "figura": {
      "mostra": [
       "superficie BKL",
       "asse OMK",
       "T",
       "traiettoria STR",
       "TN",
       "OP",
       "traccia AP",
       "TC, TG",
       "TM, TI",
       "PTF",
       "GF, IH"
      ],
      "evidenzia": [
       "OP ∥ TN, OP = TN"
      ]
     },
     "nota": "*Vestigium* è reso «traccia»; Motte «orthographic projection»."
    },
    {
     "id": "L1-P55-p2",
     "la": "",
     "it": "Dico ora che l’area AOP, descritta dal raggio OP dall’inizio del moto, è proporzionale al tempo.",
     "en": "I say, now, that the area AOP, described by the radius OP from the beginning of the motion, is proportional to the time.",
     "dipende_da": [],
     "figura": {
      "mostra": [
       "area AOP"
      ],
      "evidenzia": [
       "tesi"
      ]
     }
    },
    {
     "id": "L1-P55-p3",
     "la": "",
     "it": "Infatti la forza TG (per il Cor. II delle Leggi) si scompone nelle forze TF, FG, e la forza TI nelle forze TH, HI; ma le forze TF, TH, agendo lungo la linea PF perpendicolare al piano AOP, mutano soltanto il moto del corpo in quanto è perpendicolare a questo piano.",
     "en": "For the force TG (by Cor. 2, of the Laws of Motion) is resolved into the forces TF, FG; and the force TI into the forces TH, HI; but the forces TF, TH, acting in the direction of the line PF perpendicular to the plane AOP, introduce no change in the motion of the body but in a direction perpendicular to that plane.",
     "dipende_da": [
      "Leggi, Cor. II"
     ],
     "figura": {
      "mostra": [
       "TF, FG",
       "TH, HI"
      ],
      "evidenzia": [
       "TF, TH ⊥ piano AOP"
      ]
     }
    },
    {
     "id": "L1-P55-p4",
     "la": "",
     "it": "E perciò il suo moto in quanto si compie secondo la posizione del piano, cioè il moto del punto P con cui la traccia AP della traiettoria è descritta in questo piano, è lo stesso che si avrebbe se le forze TF, TH fossero tolte e il corpo fosse mosso dalle sole forze FG, HI; cioè lo stesso che si avrebbe se il corpo descrivesse la curva AP nel piano AOP per effetto di una forza centripeta che tende al centro O ed è uguale alla somma delle forze FG e HI.",
     "en": "Therefore its motion, so far as it has the same direction with the position of the plane, that is, the motion of the point P, by which the projection AP of the trajectory is described in that plane, is the same as if the forces TF, TH were taken away, and the body were acted on by the forces FG, HI alone; that is, the same as if the body were to describe in the plane AOP the curve AP by means of a centripetal force tending to the centre O, and equal to the sum of the forces FG and HI.",
     "dipende_da": [],
     "figura": {
      "mostra": [],
      "evidenzia": [
       "FG + HI diretta verso O nel piano AOP"
      ]
     }
    },
    {
     "id": "L1-P55-p5",
     "la": "",
     "it": "Ma per effetto di una tale forza l’area AOP sarà descritta (per la Prop. I) proporzionale al tempo. C.V.D.",
     "en": "But with such a force as that (by Prop. 1) the area AOP will be described proportional to the time. Q.E.D.",
     "dipende_da": [
      "Prop. I"
     ],
     "figura": {
      "mostra": [],
      "evidenzia": [
       "legge delle aree per P"
      ]
     }
    }
   ]
  },
  {
   "id": "L1-P56",
   "tipo": "Propositio/Problema",
   "titolo": "Prop. LVI — traiettoria su una superficie di rivoluzione",
   "copertura": [
    "S10.37",
    "S10.38"
   ],
   "fonti": {
    "la": "",
    "en": "Motte 1846, pp. 193–194"
   },
   "enunciato": {
    "la": "",
    "it": "Ammesse le quadrature delle figure curvilinee, e date sia la legge della forza centripeta che tende a un centro dato, sia la superficie curva il cui asse passa per quel centro, si deve trovare la traiettoria che un corpo descriverà su quella superficie partendo da un luogo dato, con una velocità data, verso una direzione data su quella superficie.",
    "en": "Granting the quadratures of curvilinear figures, and supposing that there are given both the law of centripetal force tending to a given centre, and the curve superficies whose axis passes through that centre; it is required to find the trajectory which a body will describe in that superficies, when going off from a given place with a given velocity, and in a given direction in that superficies."
   },
   "figura_base": {
    "punti": [
     "T",
     "S",
     "R",
     "A",
     "P",
     "O",
     "t",
     "p",
     "Q",
     "N",
     "C"
    ],
    "vincoli": [
     "costruzione della Prop. LV",
     "Tt particella nascente della traiettoria; Pp sua traccia",
     "ellisse pQ traccia del cerchietto di centro T e raggio Tt"
    ]
   },
   "passi": [
    {
     "id": "L1-P56-p1",
     "la": "",
     "it": "Ferme restando le costruzioni della proposizione precedente, il corpo T parta dal luogo dato S, lungo una retta data di posizione, nella traiettoria da trovare STR, la cui traccia nel piano BLO sia AP.",
     "en": "The last construction remaining, let the body T go from the given place S, in the direction of a line given by position, and turn into the trajectory sought STR, whose orthographic projection in the plane BDO is AP.",
     "dipende_da": [],
     "figura": {
      "mostra": [
       "S",
       "traiettoria STR",
       "traccia AP"
      ],
      "evidenzia": []
     },
     "nota": "Il latino ha «in plano BLO», Motte «BDO»: lettura da verificare sulla figura."
    },
    {
     "id": "L1-P56-p2",
     "la": "",
     "it": "E dalla velocità data del corpo all’altezza SC sarà data la sua velocità a qualsiasi altra altezza TC.",
     "en": "And from the given velocity of the body in the altitude SC, its velocity in any other altitude TC will be also given.",
     "dipende_da": [],
     "figura": {
      "mostra": [
       "SC",
       "TC"
      ],
      "evidenzia": [
       "velocità a ogni altezza"
      ]
     }
    },
    {
     "id": "L1-P56-p3",
     "la": "",
     "it": "Con quella velocità, in un tempo dato piccolissimo, il corpo descriva la particella Tt della sua traiettoria, e sia Pp la sua traccia descritta nel piano AOP.",
     "en": "With that velocity, in a given moment of time, let the body describe the particle Tt of its trajectory, and let Pp be the projection of that particle described in the plane AOP.",
     "dipende_da": [],
     "figura": {
      "mostra": [
       "Tt",
       "Pp"
      ],
      "evidenzia": []
     }
    },
    {
     "id": "L1-P56-p4",
     "la": "",
     "it": "Si congiunga Op, e la traccia nel piano AOP del cerchietto descritto sulla superficie curva con centro T e raggio Tt sia l’ellisse pQ.",
     "en": "Join Op, and a little circle being described upon the curve superficies about the centre T with the interval Tt let the projection of that little circle in the plane AOP be the ellipsis pQ.",
     "dipende_da": [],
     "figura": {
      "mostra": [
       "Op",
       "cerchietto di raggio Tt",
       "ellisse pQ"
      ],
      "evidenzia": []
     }
    },
    {
     "id": "L1-P56-p5",
     "la": "",
     "it": "Ed essendo dato di grandezza il cerchietto Tt, e data la sua distanza TN, o PO, dall’asse CO, quell’ellisse PQ sarà data di forma e di grandezza, e anche di posizione rispetto alla retta PO.",
     "en": "And because the magnitude of that little circle Tt, and TN or PO its distance from the axis CO is also given, the ellipsis pQ will be given both in kind and magnitude, as also its position to the right line PO.",
     "dipende_da": [],
     "figura": {
      "mostra": [],
      "evidenzia": [
       "ellisse data di forma, grandezza e posizione"
      ]
     },
     "nota": "Il latino ha qui «ellipsis illa PQ» (maiuscola), sopra «pQ»; Motte ha «pQ»."
    },
    {
     "id": "L1-P56-p6",
     "la": "",
     "it": "E poiché l’area POp è proporzionale al tempo, e perciò è data dal tempo dato, sarà dato l’angolo POp.",
     "en": "And since the area POp is proportional to the time, and therefore given because the time is given, the angle POp will be given.",
     "dipende_da": [],
     "figura": {
      "mostra": [
       "area POp",
       "angolo POp"
      ],
      "evidenzia": [
       "area ∝ tempo (Prop. LV)"
      ]
     }
    },
    {
     "id": "L1-P56-p7",
     "la": "",
     "it": "E di qui sarà data l’intersezione comune p dell’ellisse e della retta, insieme con l’angolo OPp sotto cui la traccia APp della traiettoria taglia la linea OP.",
     "en": "And thence will be given p the common intersection of the ellipsis and the right line Op, together with the angle OPp, in which the projection APp of the trajectory cuts the line OP.",
     "dipende_da": [],
     "figura": {
      "mostra": [
       "p",
       "angolo OPp"
      ],
      "evidenzia": []
     }
    },
    {
     "id": "L1-P56-p8",
     "la": "",
     "it": "Di qui, poi (confrontando la Prop. XLI con il suo Cor. 2), appare facilmente il modo di determinare la curva APp.",
     "en": "But from thence (by conferring Prop. XLI, with its 2d Cor.) the manner of determining the curve APp easily appears.",
     "dipende_da": [
      "Prop. XLI",
      "Prop. XLI, Cor. 2"
     ],
     "figura": {
      "mostra": [
       "curva APp"
      ],
      "evidenzia": []
     }
    },
    {
     "id": "L1-P56-p9",
     "la": "",
     "it": "Poi, innalzando dai singoli punti P della traccia le perpendicolari PT al piano AOP, che incontrino la superficie curva in T, saranno dati i singoli punti T della traiettoria. C.V.T.",
     "en": "Then from the several points P of that projection erecting to the plane AOP, the perpendiculars PT meeting the curve superficies in T, there will be given the several points T of the trajectory. Q.E.I.",
     "dipende_da": [],
     "figura": {
      "mostra": [
       "perpendicolari PT",
       "punti T"
      ],
      "evidenzia": [
       "ricostruzione della traiettoria sulla superficie"
      ]
     }
    }
   ]
  }
 ]
}
```
