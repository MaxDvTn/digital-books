> **Copia pubblica.** In questa versione i campi `"la"` della Parte B sono vuoti: le frasi latine vengono dalla trascrizione del Newton Project, che non si ridistribuisce. Il latino del 1726 si legge su newtonproject.ox.ac.uk.

# Isaac Newton
# Principi matematici della filosofia naturale

## Fascicolo 23 — Libro III: tempi periodici, figura della Terra e gravità alle diverse latitudini

**Nuova traduzione italiana di lavoro dal latino del 1726, confrontata con l’inglese di Andrew Motte nell’edizione del 1846.**

Versione 0.1 — 8 novembre 2026. Preparata con Claude (Anthropic) per Massimo Bosetti.

### Stato e perimetro

Questo fascicolo prosegue il Fascicolo 22 (Libro III, Propp. I–XIV) e traduce integralmente le **Proposizioni XV–XX** del Libro III, *De mundi systemate*: la Prop. XV (diametri principali delle orbite), la Prop. XVI (eccentricità e afeli), la Prop. XVII (moti diurni uniformi e librazione della Luna), la Prop. XVIII (gli assi dei pianeti più corti dei diametri equatoriali), la **Prop. XIX** (il rapporto 230 a 229 fra il diametro equatoriale e l’asse della Terra, l’applicazione a Giove e la tabella delle misure di Pound) e la **Prop. XX** (i pesi dei corpi alle diverse latitudini, la tabella delle lunghezze del pendolo e dei gradi di meridiano, le osservazioni dei pendoli fatte da Richer, Halley, Varin e Des Hayes, Couplet e Feuillée, e la discussione sulla dilatazione termica delle verghe). Il perimetro si chiude prima di «PROPOSITIO XXI.», che apre il Fascicolo 24a. È una traduzione di lavoro, non un’edizione critica validata.

Gli identificatori **III.G3.01–III.G3.20** (Propp. XV–XIX, gruppo G3) e **III.G4.01–III.G4.14** (Prop. XX, gruppo G4) e i titoli tematici tra parentesi sono aggiunte editoriali. Servono a orientare la lettura e a controllare la completezza. I numeri romani delle proposizioni, dei teoremi e dei problemi appartengono al testo originale. Le integrazioni del curatore sono tra parentesi quadre. Le note poste dopo la traduzione non fanno parte del testo di Newton.

In coda al fascicolo c’è la **Parte B**, con i dati strutturati per le pagine interattive: tutte e sei le proposizioni, con un passo per ogni frase latina; la parte osservativa della Prop. XX è un’unità a sé (`L3-P20-Obs`). Le due tabelle (Pound; pendoli e gradi) e i controlli numerici sono nel campo `dati`.

### Fonti effettivamente consultate

1. **Latino di riferimento.** Isaac Newton, *Philosophiæ Naturalis Principia Mathematica*, terza edizione, Londra, 1726, Libro III, **pp. 411–421** (la Prop. XV comincia a p. 411, prima del marcatore ‹412›; la Prop. XX comincia a p. 417 e finisce a p. 421, prima del marcatore ‹422›). Trascrizione normalizzata del Newton Project, documento **NATP00303**, estratta in testo semplice senza correzioni: `fonti/latino-1726/latino-1726-L3-P15-19.md` e `fonti/latino-1726/latino-1726-L3-P20.md`. Una sola figura, segnalata come [FIG] nella Prop. XIX (il canale ACQqca), non disponibile. Per i rimandi interni ho letto anche `latino-1726-L3-P01-14.md` (Propp. IV e VIII).
2. **Inglese di confronto.** *Newton’s Principia*, traduzione di Andrew Motte, New York, Daniel Adee, 1846, Libro III, Propp. XV–XX (Project Gutenberg n. 76404), estratti `fonti/motte-1846/motte-1846-L3-P15-19.md` e `fonti/motte-1846/motte-1846-L3-P20.md`. Gli estratti non hanno marcatori di pagina: le pagine Motte sono indicate come «sezione corrispondente». Le formule stampate come immagini (48 SVG diversi, 59 occorrenze) sono state lette sul LaTeX di `fonti/motte-1846/svg_tex.tsv`.
3. **Istruzioni:** brief comune, addendum del Libro II, istruzioni del Libro III; **modelli:** Fascicoli 3, 5 e 20; **rimandi:** Fascicoli 3, 6, 10, 11 e 12 (Leggi; Libro I, Sezioni III–IV, XI, XII, XIII).

Non ho consultato né riprodotto traduzioni moderne. Non ho potuto vedere la stampa del 1726, né Motte 1729, né la figura originale: la geometria del canale è ricostruita dalle lettere del testo.

### Criteri di traduzione

- Il testo guida è il latino; l’inglese di Motte serve a controllare le interpretazioni ed è annotato quando aggiunge, omette o si discosta.
- Si applicano il **glossario comune**, quello del **Libro II** e quello del **Libro III**: *tempus periodicum* «tempo periodico», *aphelium* «afelio», *excentricitas* «eccentricità», *umbilicus* «fuoco», *sinus versus* «seno verso», *ratio duplicata* «rapporto duplicato», *reciproce* «inversamente», *conjunctim* «considerate congiuntamente», *vis centrifuga* «forza centrifuga», *gravitas* «gravità», *pondus* «peso», *densitas* «densità», *canalis* «canale», *aqua* «acqua», *pes Parisiensis / Londinensis* «piede parigino / londinese», *linea* «linea», *minutum secundum* «secondo», *pendulum* «pendolo», *oscillatio* «oscillazione», *hexapeda* «tesa», *milliare* «miglio», *pendulum ad minuta secunda oscillans* «pendolo che batte i secondi», *sphærois* «sferoide», *figura terræ* «figura della Terra», *axis* «asse», *æquator* «equatore», *poli* «poli», *meridianus* «meridiano», *gradus* «grado», *latitudo* «latitudine», *dies sidereus* «giorno siderale», *diameter apparens* «diametro apparente», *telescopium* «telescopio», *micrometrum* «micrometro», *stellæ fixæ* «stelle fisse», *maculæ* «macchie», *ecliptica* «eclittica», *satelles* «satellite», *phænomenon* «fenomeno», *hypothesis* «ipotesi»; nomi dei corpi celesti con la maiuscola (Sole, Luna, Terra, Giove, Saturno, Marte, Venere).
- Le estensioni del glossario proprie di questo fascicolo sono nel § A.0.
- Gli enunciati latini all’infinito (Propp. XVII e XVIII) sono resi con l’indicativo; quelli dei problemi con l’infinito italiano («Trovare…»).
- **Numeri.** Le cifre restano come nel testo, con la virgola decimale. Le frazioni appiattite dalla trascrizione («25⁤12», «1⁤79», «4505») sono lette come 25½, 1 7/9, 4/505 e così via (§ A.7). Nel testo uso i caratteri ½ ⅓ ⅔ ¼ ¾ ⅙ ⅚ quando esistono, e la barra negli altri casi (1 7/9, 5/9, 4/505, 1/229, 5 7/12). Gli angoli e gli intervalli brevi restano con i segni ° ′ ″ ‴; le durate in ore e minuti sono scritte a parole («9 ore e 56 minuti»), salvo dove Newton le ripete come numeri accanto ad altri numeri.
- **Nomi.** Gli astronomi hanno il nome nella forma corrente (Picard, Cassini, Richer, Halley, Pound, Feuillée); *D.* (*Dominus*) «il signor», *P.* (*Pater*) «il padre». I luoghi hanno il nome italiano corrente quando c’è (Parigi, Londra, York, Lisbona, Caienna, Sant’Elena, Guadalupa, Martinica, Dunkerque) e altrimenti quello locale (Amiens, Malvoisine, Collioure, Gorée, Paraíba, Portobelo); le identificazioni seguono Motte.
- Nessuna formula moderna entra nel testo tradotto; le tabelle sono riprodotte per intero, senza correggere le cifre.

---

## Traduzione italiana

### Proposizione XV. Problema I (diametri principali delle orbite)

**[III.G3.01]** **Trovare i diametri principali delle orbite.**

**[III.G3.02]** Questi vanno presi nel rapporto subsesquiplicato dei tempi periodici, per la Prop. XV del Libro I; poi vanno aumentati uno per uno nel rapporto della somma delle masse del Sole e di ciascun pianeta che ruota, alla prima di due medie proporzionali fra quella somma e il Sole, per la Prop. LX del Libro I.

### Proposizione XVI. Problema II (eccentricità e afeli delle orbite)

**[III.G3.03]** **Trovare le eccentricità e gli afeli delle orbite.**

**[III.G3.04]** Il problema si risolve per la Prop. XVIII del Libro I.

### Proposizione XVII. Teorema XV (moti diurni uniformi e librazione della Luna)

**[III.G3.05]** **I moti diurni dei pianeti sono uniformi, e la librazione della Luna nasce dal suo moto diurno.**

**[III.G3.06]** È evidente per la Legge I del moto e per il Cor. 22 della Prop. LXVI del Libro I. Giove, infatti, rispetto alle stelle fisse ruota in 9 ore e 56 minuti, Marte in 24 ore e 39 minuti, Venere in circa 23 ore, la Terra in 23 ore e 56 minuti, il Sole in 25½ giorni e la Luna in 27 giorni, 7 ore e 43 minuti. Che le cose stiano così è manifesto dai fenomeni. Le macchie sul corpo del Sole ritornano alla stessa posizione sul disco del Sole in circa 27½ giorni rispetto alla Terra; e perciò rispetto alle stelle fisse il Sole ruota in circa 25½ giorni. Poiché poi il giorno della Luna, che ruota uniformemente attorno al proprio asse, è mensile, la stessa sua faccia guarderà sempre, con ottima approssimazione, il fuoco più lontano della sua orbita, e perciò, secondo la posizione di quel fuoco, devierà di qua e di là dalla Terra. Questa è la librazione della Luna in longitudine. La librazione in latitudine, infatti, nasce dalla latitudine della Luna e dall’inclinazione del suo asse sul piano dell’eclittica. Questa teoria della librazione lunare l’ha esposta più ampiamente, sulla base di mie lettere, il signor N. Mercator nella sua *Astronomia*, pubblicata all’inizio dell’anno 1676. Con un moto simile sembra ruotare attorno al proprio asse il satellite più esterno di Saturno, che guarda Saturno sempre con la stessa faccia. Infatti, ruotando attorno a Saturno, ogni volta che si avvicina alla parte orientale della sua orbita si vede a stento, e per lo più cessa di essere visibile: cosa che può avvenire per certe macchie in quella parte del corpo che allora è rivolta verso la Terra, come ha notato Cassini. Con un moto simile sembra ruotare attorno al proprio asse anche il satellite più esterno di Giove, poiché nella parte del corpo opposta a Giove ha una macchia che si vede come se fosse sul corpo di Giove ogni volta che il satellite passa fra Giove e i nostri occhi.

### Proposizione XVIII. Teorema XVI (gli assi dei pianeti sono minori dei diametri equatoriali)

**[III.G3.07]** **Gli assi dei pianeti sono minori dei diametri condotti perpendicolarmente a quegli stessi assi.**

**[III.G3.08]** I pianeti, tolto ogni moto circolare diurno, dovrebbero assumere una figura sferica, per l’uguale gravità delle parti da ogni lato. Per quel moto circolare avviene che le parti che si allontanano dall’asse tendano a salire presso l’equatore. Perciò la materia, se è fluida, salendo verso l’equatore aumenterà i diametri, e scendendo verso i poli diminuirà l’asse. Così il diametro di Giove (secondo le osservazioni concordi degli astronomi) risulta più breve fra i poli che da oriente a occidente. Con lo stesso argomento, se la nostra Terra non fosse un poco più alta sotto l’equatore che ai poli, i mari si abbasserebbero ai poli e, salendo presso l’equatore, vi inonderebbero ogni cosa.

### Proposizione XIX. Problema III (il rapporto dell’asse ai diametri: la figura della Terra)

**[III.G3.09]** **Trovare la proporzione dell’asse di un pianeta ai diametri a esso perpendicolari.**

**[III.G3.10]** Il nostro Norwood, verso l’anno 1635, misurando una distanza di 905751 piedi londinesi fra Londra e York e osservando una differenza di latitudine di 2 gradi e 28 primi, ricavò che la misura di un grado è di 367196 piedi londinesi, cioè di 57300 tese parigine.

**[III.G3.11]** Picard, misurando un arco di un grado e 22′ 55″ sul meridiano fra Amiens e Malvoisine, trovò che l’arco di un grado è di 57060 tese parigine. Cassini padre misurò la distanza sul meridiano dalla cittadina di Collioure, nel Roussillon, all’Osservatorio di Parigi; e suo figlio aggiunse la distanza dall’Osservatorio alla torre della città di Dunkerque. La distanza totale era di 486156½ tese, e la differenza di latitudine fra la cittadina di Collioure e la città di Dunkerque era di otto gradi e 31′ 11⅚″. Di qui l’arco di un grado risulta di 57061 tese parigine. E da queste misure si ricava che la circonferenza della Terra è di 123249600 piedi parigini, e il suo semidiametro di 19615800 piedi, nell’ipotesi che la Terra sia sferica.

**[III.G3.12]** Alla latitudine di Parigi un corpo grave, cadendo nel tempo di un secondo, descrive 15 piedi parigini, 1 pollice e 1 7/9 linee, come sopra [Prop. IV di questo Libro], cioè 2173 7/9 linee. Il peso del corpo è diminuito dal peso dell’aria circostante. Poniamo che il peso perduto sia l’undicimillesima parte del peso totale: quel corpo grave, cadendo nel vuoto, descriverà nel tempo di un secondo un’altezza di 2174 linee.

**[III.G3.13]** Un corpo che, alla distanza di 19615800 piedi dal centro, ruota uniformemente su un cerchio in ciascun giorno siderale di 23 ore, 56 minuti e 4 secondi, nel tempo di un secondo descriverà un arco di 1433,46 piedi, il cui seno verso è di 0,0523656 piedi, ossia di 7,54064 linee. Perciò la forza con cui i gravi scendono alla latitudine di Parigi sta alla forza centrifuga dei corpi all’equatore, originata dal moto diurno della Terra, come 2174 sta a 7,54064.

**[III.G3.14]** La forza centrifuga dei corpi all’equatore della Terra sta alla forza centrifuga con cui i corpi tendono direttamente ad allontanarsi dalla Terra alla latitudine di Parigi, di 48° 50′ 10″, nel rapporto duplicato del raggio al seno del complemento di quella latitudine, cioè come 7,54064 sta a 3,267. Si aggiunga questa forza alla forza con cui i gravi scendono a quella latitudine di Parigi, e un corpo, a quella latitudine, cadendo con tutta la forza di gravità, nel tempo di un secondo descriverà 2177,267 linee, ossia 15 piedi parigini, 1 pollice e 5,267 linee. E la forza totale di gravità a quella latitudine starà alla forza centrifuga dei corpi all’equatore della Terra come 2177,267 sta a 7,54064, ossia come 289 sta a 1.

**[III.G3.15]** Di qui, se APBQ rappresenta la figura della Terra, ormai non più sferica, ma generata dalla rivoluzione di un’ellisse attorno all’asse minore PQ, e ACQqca è un canale pieno d’acqua che va dal polo Qq al centro Cc e di là prosegue fino all’equatore Aa, il peso dell’acqua nel braccio ACca del canale dovrà stare al peso dell’acqua nell’altro braccio QCcq come 289 sta a 288, per il fatto che la forza centrifuga originata dal moto circolare sosterrà e sottrarrà una delle 289 parti del peso, e il peso 288 nell’altro braccio sosterrà le restanti. Inoltre, impostando il calcolo (in base al Cor. 2 della Prop. XCI del Libro I), trovo che, se la Terra fosse costituita di materia uniforme, fosse privata di ogni moto, e il suo asse PQ stesse al diametro AB come 100 sta a 101, la gravità nel luogo Q verso la Terra starebbe alla gravità nello stesso luogo Q verso una sfera descritta con centro C e raggio PC o QC come 126 sta a 125. E con lo stesso argomento la gravità nel luogo A verso lo sferoide descritto dalla rotazione dell’ellisse APBQ attorno all’asse AB sta alla gravità nello stesso luogo A verso la sfera descritta con centro C e raggio AC come 125 sta a 126. Ora, la gravità nel luogo A verso la Terra è media proporzionale fra le gravità verso il detto sferoide e verso la sfera: perché la sfera, diminuendo il diametro PQ nel rapporto di 101 a 100, si muta nella figura della Terra; e questa figura, diminuendo nello stesso rapporto il terzo diametro, che è perpendicolare ai due diametri AB, PQ, si muta nel detto sferoide; e la gravità in A, nell’uno e nell’altro caso, diminuisce con ottima approssimazione nello stesso rapporto. La gravità in A verso la sfera descritta con centro C e raggio AC sta dunque alla gravità in A verso la Terra come 126 sta a 125½; e la gravità nel luogo Q verso la sfera descritta con centro C e raggio QC sta alla gravità nel luogo A verso la sfera descritta con centro C e raggio AC nel rapporto dei diametri (per la Prop. LXXII del Libro I), cioè come 100 sta a 101. Si compongano ora questi tre rapporti, 126 a 125, 126 a 125½ e 100 a 101: e la gravità nel luogo Q verso la Terra starà alla gravità nel luogo A verso la Terra come 126 × 126 × 100 sta a 125 × 125½ × 101, ossia come 501 sta a 500.

**[III.G3.16]** Ora, poiché (per il Cor. 3 della Prop. XCI del Libro I) la gravità nell’uno o nell’altro braccio del canale, ACca o QCcq, è come la distanza dei luoghi dal centro della Terra, se quei bracci si dividono con superfici trasversali ed equidistanti in parti proporzionali ai bracci interi, i pesi delle singole parti nel braccio ACca staranno ai pesi di altrettante parti nell’altro braccio come le grandezze e le gravità acceleratrici considerate congiuntamente; cioè come 101 sta a 100 e 500 sta a 501, vale a dire come 505 sta a 501. E perciò, se la forza centrifuga di ciascuna parte nel braccio ACca, originata dal moto diurno, fosse stata al peso della stessa parte come 4 sta a 505, così da sottrarre dal peso di ciascuna parte, diviso in 505 parti, quattro parti, i pesi nell’uno e nell’altro braccio resterebbero uguali, e perciò il fluido starebbe in equilibrio. Ma la forza centrifuga di ciascuna parte sta al peso della stessa come 1 sta a 289; cioè la forza centrifuga, che dovrebbe essere i 4/505 del peso, ne è soltanto 1/289. E perciò dico, secondo la regola aurea, che, se la forza centrifuga 4/505 fa sì che l’altezza dell’acqua nel braccio ACca superi l’altezza dell’acqua nel braccio QCcq di un centesimo dell’altezza totale, la forza centrifuga 1/289 farà sì che l’eccesso di altezza nel braccio ACca sia soltanto 1/229 dell’altezza nell’altro braccio QCcq. Il diametro della Terra secondo l’equatore sta dunque al suo diametro per i poli come 230 sta a 229. E perciò, poiché il semidiametro medio della Terra, secondo la misura di Picard, è di 19615800 piedi parigini, ossia di 3923,16 miglia (posto che il miglio sia una misura di 5000 piedi), la Terra sarà più alta all’equatore che ai poli di un eccesso di 85472 piedi, ossia di 17 1/10 miglia. E la sua altezza all’equatore sarà di circa 19658600 piedi, e ai poli di 19573000 piedi.

**[III.G3.17]** Se un pianeta è maggiore o minore della Terra, restando la sua densità e il tempo periodico della rivoluzione diurna, resterà la proporzione della forza centrifuga alla gravità, e perciò resterà anche la proporzione del diametro fra i poli al diametro secondo l’equatore. Ma se il moto diurno si accelera o si ritarda in un rapporto qualsiasi, la forza centrifuga aumenterà o diminuirà in quel rapporto duplicato, e perciò la differenza dei diametri aumenterà o diminuirà nello stesso rapporto duplicato, con ottima approssimazione. E se la densità del pianeta aumenta o diminuisce in un rapporto qualsiasi, anche la gravità che tende verso di esso aumenterà o diminuirà nello stesso rapporto, e la differenza dei diametri, viceversa, diminuirà nel rapporto della gravità aumentata o aumenterà nel rapporto della gravità diminuita. Di qui, poiché la Terra rispetto alle stelle fisse ruota in 23 ore e 56 minuti, Giove invece in 9 ore e 56 minuti, e i quadrati dei tempi stanno come 29 a 5, e le densità dei due corpi rotanti come 400 a 94½, la differenza dei diametri di Giove starà al suo diametro minore come 29/5 × 400/94½ × 1/229 sta a 1, ossia come 1 sta a 9⅓, con ottima approssimazione. Il diametro di Giove condotto da oriente a occidente sta dunque al suo diametro fra i poli come 10⅓ sta a 9⅓, con ottima approssimazione. Di qui, poiché il suo diametro maggiore è di 37″, il suo diametro minore, che sta fra i poli, sarà di 33″ 25‴. Per la luce erratica si aggiungano circa 3″, e i diametri apparenti di questo pianeta diventeranno 40″ e 36″ 25‴, che stanno fra loro come 11⅙ sta a 10⅙, con ottima approssimazione. Così stanno le cose nell’ipotesi che il corpo di Giove sia uniformemente denso. Ma se il suo corpo è più denso verso il piano dell’equatore che verso i poli, i suoi diametri possono stare fra loro come 12 a 11, o 13 a 12, o forse 14 a 13. E Cassini, appunto, nell’anno 1691 osservò che il diametro di Giove disteso da oriente a occidente superava l’altro diametro di circa la quindicesima parte di sé. Il nostro Pound, poi, con un telescopio lungo 123 piedi e un ottimo micrometro, misurò nell’anno 1719 i diametri di Giove come segue.

**[III.G3.18]** *[Tabella delle misure di Pound, 1719.]*

| Tempi | giorno | ora | Diam. max. (parti) | Diam. min. (parti) | Diametri fra loro |
|---|---|---|---|---|---|
| gennaio | 28 | 6 | 13,40 | 12,28 | come 12 a 11 |
| marzo | 6 | 7 | 13,12 | 12,20 | 13¾ a 12¾ |
| marzo | 9 | 7 | 13,12 | 12,08 | 12⅔ a 14⅔ [*sic*: atteso 11⅔; nota N6] |
| aprile | 9 | 9 | 12,32 | 11,48 | 14½ a 13½ |

**[III.G3.19]** La teoria concorda dunque con i fenomeni. Infatti i pianeti si riscaldano di più alla luce del Sole verso i loro equatori, e perciò lì si cuociono un poco di più che verso i poli.

**[III.G3.20]** Che poi la gravità diminuisca sotto l’equatore per la rotazione diurna della nostra Terra, e che perciò la Terra lì si innalzi più che ai poli (se la sua materia è uniformemente densa), risulterà dagli esperimenti dei pendoli che sono riferiti nella proposizione seguente.

### Proposizione XX. Problema IV (i pesi dei corpi nelle diverse regioni della Terra)

**[III.G4.01]** **Trovare e confrontare fra loro i pesi dei corpi nelle diverse regioni di questa Terra.**

**[III.G4.02]** Poiché i pesi dei bracci disuguali del canale d’acqua ACQqca sono uguali, e i pesi delle parti proporzionali ai bracci interi e situate in modo simile negli interi stanno fra loro come i pesi degli interi, e perciò sono anche uguali fra loro, i pesi di parti uguali e situate in modo simile nei bracci saranno inversamente come i bracci, cioè inversamente come 230 a 229. E lo stesso vale per corpi qualsiasi omogenei e uguali, situati in modo simile nei bracci del canale. I loro pesi sono inversamente come i bracci, cioè inversamente come le distanze dei corpi dal centro della Terra. Perciò, se i corpi stanno nelle parti più alte dei canali, ossia sulla superficie della Terra, i loro pesi staranno fra loro inversamente come le loro distanze dal centro. E con lo stesso argomento i pesi, in qualsiasi altra regione su tutta la superficie della Terra, sono inversamente come le distanze dei luoghi dal centro; e perciò, nell’ipotesi che la Terra sia uno sferoide, sono dati in proporzione.

**[III.G4.03]** Di qui si ottiene questo teorema: l’incremento del peso, procedendo dall’equatore verso i poli, è con ottima approssimazione come il seno verso del doppio della latitudine, o, ciò che è lo stesso, come il quadrato del seno retto della latitudine. E all’incirca nello stesso rapporto crescono gli archi dei gradi di latitudine sul meridiano. E perciò, poiché la latitudine di Parigi è di 48° 50′, quella dei luoghi sotto l’equatore di 00° 00′ e quella dei luoghi ai poli di 90°, e i seni versi dei loro doppi sono 11334, 00000 e 20000, essendo il raggio 10000, e la gravità al polo sta alla gravità sotto l’equatore come 230 a 229, e l’eccesso della gravità al polo sulla gravità sotto l’equatore come 1 a 229, l’eccesso della gravità alla latitudine di Parigi starà alla gravità sotto l’equatore come 1 × 11334/20000 sta a 229, ossia come 5667 a 2290000. E perciò le gravità totali in questi luoghi staranno fra loro come 2295667 a 2290000. Quindi, poiché le lunghezze dei pendoli che oscillano in tempi uguali sono come le gravità, e alla latitudine di Parigi la lunghezza del pendolo che batte i secondi è di tre piedi parigini e 8½ linee, o piuttosto, per il peso dell’aria, 8 5/9, la lunghezza del pendolo sotto l’equatore sarà superata dalla lunghezza del pendolo sincrono di Parigi di un eccesso di una linea e 87 millesimi di linea. E con un calcolo simile si ottiene la tabella seguente.

**[III.G4.04]** *[Tabella delle lunghezze del pendolo e dei gradi di meridiano.]*

| Latitudine del luogo (gradi) | Lunghezza del pendolo: piedi | linee | Misura di un grado sul meridiano (tese) |
|---|---|---|---|
| 0 | 3 | 7,468 | 56637 |
| 5 | 3 | 7,482 | 56642 |
| 10 | 3 | 7,526 | 56659 |
| 15 | 3 | 7,596 | 56687 |
| 20 | 3 | 7,692 | 56724 |
| 25 | 3 | 7,812 | 56769 |
| 30 | 3 | 7,948 | 56823 |
| 35 | 3 | 8,099 | 56882 |
| 40 | 3 | 8,261 | 56945 |
| 41 | 3 | 8,294 | 56958 |
| 42 | 3 | 8,327 | 56971 |
| 43 | 3 | 8,361 | 56984 |
| 44 | 3 | 8,394 | 56997 |
| 45 | 3 | 8,428 | 57010 |
| 46 | 3 | 8,461 | 57022 |
| 47 | 3 | 8,494 | 57035 |
| 48 | 3 | 8,528 | 57048 |
| 49 | 3 | 8,561 | 57061 |
| 50 | 3 | 8,594 | 57074 |
| 55 | 3 | 8,756 | 57137 |
| 60 | 3 | 8,907 | 57196 |
| 65 | 3 | 9,044 | 57250 |
| 70 | 3 | 9,162 | 57295 |
| 75 | 3 | 9,258 | 57332 |
| 80 | 3 | 9,329 | 57360 |
| 85 | 3 | 9,372 | 57377 |
| 90 | 3 | 9,387 | 57382 |

Nella stampa le righe 41–44 e 46–49 portano soltanto l’ultima cifra della latitudine (1, 2, 3, 4; 6, 7, 8, 9); qui sono scritte per intero (§ A.6).

**[III.G4.05]** Risulta poi da questa tabella che la disuguaglianza dei gradi è così piccola che nelle questioni geografiche la figura della Terra si può considerare sferica: soprattutto se la Terra è un poco più densa verso il piano dell’equatore che verso i poli.

**[III.G4.06]** Ora, alcuni astronomi, mandati in regioni lontane per fare osservazioni astronomiche, hanno osservato che gli orologi a pendolo si muovevano più lentamente vicino all’equatore che nelle nostre regioni. E per primo il signor Richer lo osservò nell’anno 1672 nell’isola di Caienna. Infatti, mentre nel mese di agosto osservava il passaggio delle stelle fisse al meridiano, trovò che il suo orologio si muoveva più lentamente di quanto richiedesse il moto medio del Sole, con una differenza di 2 minuti e 28 secondi ogni giorno. Poi, facendo oscillare un pendolo semplice una volta per ogni secondo misurato con un ottimo orologio, annotò la lunghezza del pendolo semplice; e lo fece più volte ogni settimana per dieci mesi. Poi, tornato in Francia, confrontò la lunghezza di questo pendolo con la lunghezza del pendolo di Parigi (che era di tre piedi parigini e otto linee e tre quinti di linea) e la trovò più breve, con una differenza di una linea e un quarto.

**[III.G4.07]** In seguito il nostro Halley, navigando verso l’isola di Sant’Elena verso l’anno 1677, trovò che il suo orologio a pendolo lì si muoveva più lentamente che a Londra, ma non annotò la differenza. Rese però il pendolo più breve di più di un ottavo di pollice, ossia di una linea e mezza. E per ottenere questo, poiché la lunghezza della vite nella parte inferiore del pendolo non bastava, interpose un anello di legno fra la chiocciola della vite e il peso del pendolo.

**[III.G4.08]** Poi, nell’anno 1682, i signori Varin e Des Hayes trovarono che la lunghezza del pendolo che batte i secondi nell’Osservatorio reale di Parigi era di 3 piedi e 8 5/9 linee. E nell’isola di Gorée, con lo stesso metodo, trovarono che la lunghezza del pendolo sincrono era di 3 piedi e 6 5/9 linee, con una differenza fra le lunghezze di 2 linee. E nello stesso anno, navigando verso le isole di Guadalupa e Martinica, trovarono che la lunghezza del pendolo sincrono in queste isole era di 3 piedi e 6½ linee.

**[III.G4.09]** Dopo di ciò il signor Couplet figlio, nel mese di luglio dell’anno 1697, regolò il suo orologio a pendolo sul moto medio del Sole nell’Osservatorio reale di Parigi, in modo che per un tempo abbastanza lungo l’orologio concordasse con il moto del Sole. Poi, navigando verso Lisbona, trovò che nel successivo mese di novembre l’orologio andava più lentamente di prima, con una differenza di 2 minuti e 13 secondi in 24 ore. E nel marzo seguente, navigando verso Paraíba, trovò che lì il suo orologio andava più lentamente che a Parigi, con una differenza di 4 minuti e 12 secondi in 24 ore. E afferma che il pendolo che batte i secondi era più breve che a Parigi di 2½ linee a Lisbona e di 3⅔ linee a Paraíba. Più correttamente avrebbe posto le differenze uguali a 1⅓ e a 2 5/9 linee. Queste differenze, infatti, corrispondono alle differenze di tempo di 2′ 13″ e 4′ 12″. Alle osservazioni di costui, piuttosto grossolane, si deve prestare meno fede.

**[III.G4.10]** Negli anni seguenti (1699 e 1700) il signor Des Hayes, navigando di nuovo verso l’America, determinò che nelle isole di Caienna e di Grenada la lunghezza del pendolo che batte i secondi era poco minore di 3 piedi e 6½ linee, che nell’isola di San Cristoforo quella lunghezza era di 3 piedi e 6¾ linee, e che nell’isola di San Domingo la stessa era di 3 piedi e 7 linee.

**[III.G4.11]** E nell’anno 1704 il padre Feuillée trovò a Portobelo, in America, che la lunghezza del pendolo che batte i secondi era di tre piedi parigini e soltanto 5 7/12 linee, cioè quasi tre linee più breve che a Parigi; ma l’osservazione era sbagliata. Infatti, navigando poi verso l’isola di Martinica, trovò che la lunghezza del pendolo isocrono era soltanto di tre piedi parigini e 5 10/12 linee.

**[III.G4.12]** Ora, la latitudine di Paraíba è di 6° 38′ australe, e quella di Portobelo di 9° 33′ boreale; e le latitudini delle isole di Caienna, Gorée, Guadalupa, Martinica, Grenada, San Cristoforo e San Domingo sono rispettivamente di 4° 55′, 14° 40′, 14° 00′, 14° 44′, 12° 6′, 17° 19′ e 19° 48′ boreali. E gli eccessi della lunghezza del pendolo di Parigi sulle lunghezze dei pendoli isocroni osservate a queste latitudini sono un poco maggiori di quelli della tabella delle lunghezze del pendolo calcolata sopra. E perciò la Terra è alquanto più alta sotto l’equatore di quanto dia il calcolo precedente, e più densa al centro che nelle miniere vicine alla superficie, a meno che forse i calori della zona torrida non abbiano un poco aumentato la lunghezza dei pendoli.

**[III.G4.13]** Il signor Picard, infatti, osservò che una verga di ferro, che d’inverno, quando gelava, era lunga un piede, scaldata al fuoco divenne di un piede e un quarto di linea. Poi il signor de la Hire osservò che una verga di ferro che, in un analogo periodo invernale, era lunga sei piedi, esposta al sole estivo divenne lunga sei piedi e due terzi di linea. Nel primo caso il calore fu maggiore che nel secondo; in questo, però, fu maggiore del calore delle parti esterne del corpo umano. I metalli, infatti, al sole estivo si riscaldano molto. Ma la verga del pendolo in un orologio a pendolo non suole mai essere esposta al calore del sole estivo, e non acquista mai un calore uguale al calore della superficie esterna del corpo umano. E perciò la verga del pendolo in un orologio, lunga tre piedi, sarà sì un poco più lunga d’estate che d’inverno, ma di un eccesso che supera appena la quarta parte di una linea. Perciò la differenza totale di lunghezza dei pendoli che in diverse regioni sono isocroni non può essere attribuita al diverso calore. Ma neppure agli errori degli astronomi mandati dalla Francia si deve attribuire questa differenza. Infatti, sebbene le loro osservazioni non concordino perfettamente fra loro, gli errori sono tuttavia così piccoli che si possono trascurare. E in questo concordano tutti: che i pendoli isocroni sono più brevi sotto l’equatore che nell’Osservatorio reale di Parigi, con una differenza non minore di una linea e un quarto e non maggiore di 2⅔ linee. Secondo le osservazioni del signor Richer fatte a Caienna la differenza fu di una linea e un quarto. Secondo quelle del signor Des Hayes quella differenza, corretta, risultò di una linea e mezza o di una linea e tre quarti. Secondo quelle di altri, meno accurate, la stessa risultò di circa due linee. E questa discrepanza poté nascere in parte dagli errori delle osservazioni, in parte dalla dissomiglianza delle parti interne della Terra e dall’altezza dei monti, e in parte dai diversi calori dell’aria.

**[III.G4.14]** Una verga di ferro lunga tre piedi, d’inverno in Inghilterra, è più breve che d’estate di un sesto di linea, per quanto ne giudico. Per i calori sotto l’equatore si tolga questa quantità dalla differenza di una linea e un quarto osservata da Richer, e resterà 1 1/12 di linea, che concorda bene con 1 87/1000 di linea, ricavata poco prima dalla teoria. Richer, poi, ripeté ogni settimana per dieci mesi le osservazioni fatte a Caienna, e confrontò le lunghezze del pendolo lì segnate sulla verga di ferro con le sue lunghezze segnate in modo simile in Francia. Questa diligenza e questa cautela sembrano essere mancate agli altri osservatori. Se si deve prestar fede alle sue osservazioni, la Terra sarà più alta all’equatore che ai poli di un eccesso di circa diciassette miglia, come è risultato sopra dalla teoria.

---

## Apparato

### A.0 Estensioni del glossario

I termini seguenti non comparivano nei glossari comuni né nelle liste del coordinatore. Ognuno è reso in modo costante in tutto il fascicolo.

| Latino | Italiano | Motivazione |
|---|---|---|
| *ratio subsesquiplicata* | «rapporto subsesquiplicato» | Prop. XV: l’inverso del sesquiplicato, cioè la potenza 2/3 (nota N1). Calco coerente con «subduplicato» del glossario comune; Motte «sub-sesquiplicate». |
| *media proportionalis*; *duæ medie proportionales* | «media proporzionale»; «due medie proporzionali» | Prop. XV, come nel Fascicolo 10 (Prop. LX); Prop. XIX. |
| *massa* | «massa» | Prop. XV (*summa massarum*). |
| *libratio* (*in longitudinem / in latitudinem*) | «librazione» (in longitudine / in latitudine) | Prop. XVII; termine astronomico corrente. |
| *dies menstruus* | «giorno mensile» | Prop. XVII: il giorno della Luna (una rotazione) dura un mese. Motte «menstrual», con una glossa aggiunta. |
| *umbilicus ulterior* | «il fuoco più lontano» | Prop. XVII: il fuoco dell’orbita lunare che non è occupato dalla Terra. Motte «upper focus». *Umbilicus* «fuoco» (glossario). |
| *discus* | «disco» | Prop. XVII (*in disco solis*). |
| *satelles extimus* | «il satellite più esterno» | Prop. XVII; *jovialis* «di Giove». |
| *crus* (*canalis*) | «braccio» (del canale) | Propp. XIX–XX. «Gamba» è il senso letterale; «braccio» è l’uso italiano per i tubi a U e i vasi comunicanti. Motte «leg». |
| *gravitas acceleratrix* | «gravità acceleratrice» | Prop. XIX; per analogia con *vis acceleratrix* «forza acceleratrice» (glossario comune). |
| *magnitudo* (delle parti) | «grandezza» | Prop. XIX: il volume (e quindi la massa) delle parti del canale. |
| *regula aurea* | «regola aurea» | Prop. XIX: è la regola del tre (proporzione semplice); nota N4. Motte «rule of proportion». |
| *sinus complementi* | «seno del complemento» | Prop. XIX: il coseno della latitudine. Motte «cosine». Si conserva la forma storica. |
| *sinus rectus* | «seno retto» | Prop. XX: il seno ordinario, contrapposto al seno verso. |
| *vis tota gravitatis* | «forza totale di gravità» | Propp. XIX–XX (*gravitates totæ* «gravità totali»). |
| *ambitus terræ* | «circonferenza della Terra» | Prop. XIX. |
| *semidiameter mediocris* | «semidiametro medio» | Prop. XIX; coerente con *mediocris distantia* «distanza media» (glossario). |
| *villa*; *urbs*; *turris* | «cittadina»; «città»; «torre» | Prop. XIX (Collioure, Dunkerque). Motte «town», «Citadel» (§ A.9). |
| *digitus* (misura) | «pollice» | Prop. XIX (*dig.*), Prop. XX (*octava parte digiti*). Il glossario del Libro III fissa «dito» per il *digitus* delle eclissi; qui è l’unità di lunghezza (1/12 di piede), e vale il glossario del Libro II («pollice»). **Dubbio segnalato:** due rese per lo stesso termine, distinte per senso. |
| *lux erratica* | «luce erratica» | Prop. XIX, Giove: la luce diffusa che allarga il disco apparente. Motte «irregular refraction of light». Nota N5. |
| *decoqui* | «cuocersi» | Prop. XIX, ultimo capoverso: i pianeti si «cuociono», cioè si addensano, di più all’equatore. Motte «condensed». Si conserva l’immagine del latino. |
| *tertia* (‴) | «terzi» | Prop. XIX (33″ 25‴): sessantesimi di secondo d’arco; nel testo resta il segno ‴. |
| *horologium oscillatorium* | «orologio a pendolo» | Prop. XX; Motte «pendulum clock». |
| *pendulum simplex*; *pendulum synchronum / isochronum* | «pendolo semplice»; «pendolo sincrono / isocrono» | Prop. XX. I due aggettivi latini sono distinti anche in italiano, benché equivalenti nel senso (stesso periodo). |
| *cochlea*; *theca cochleæ* | «vite»; «chiocciola della vite» | Prop. XX, Halley: la vite di regolazione in fondo all’asta e la sua madrevite. Motte «screw», «nut». |
| *annulus ligneus* | «anello di legno» | Prop. XX; *annulus* «anello» (glossario). |
| *virga ferrea*; *virga penduli* | «verga di ferro»; «verga del pendolo» | Prop. XX; Motte «rod». |
| *fodinæ* | «miniere» | Prop. XX. |
| *zona torrida* | «zona torrida» | Prop. XX. |
| *observatorium regium Parisiense* | «Osservatorio reale di Parigi» | Prop. XX; Motte «Royal Observatory of Paris». |
| *ad austrum / ad boream* | «australe / boreale» | Prop. XX, latitudini; estensione di *lat. bor. / austr.* del glossario. |
| *D.*; *P.* | «il signor»; «il padre» | Titoli premessi ai nomi (*Dominus*, *Pater*). Motte «M.», «P.». |
| *quamproxime*, *quam proxime* | «con ottima approssimazione» | Come nei Fascicoli 5 e 20. |
| *partes millesimæ* | «millesimi» | Prop. XX (*87 partium millesimarum lineæ*). |
| *superficies transversæ & æquidistantes* | «superfici trasversali ed equidistanti» | Prop. XIX. |
| *Lutetia Parisiorum*; *Eboracum*; *Ambianum*; *Ulyssippo* | «Parigi»; «York»; «Amiens»; «Lisbona» | Identificazioni di Motte. |

*Hexapeda* «tesa» (glossario del coordinatore) compare la prima volta in III.G3.10: è la tesa di Parigi, di 6 piedi parigini (nota N11). *Milliare* «miglio» compare in III.G3.16, dove Newton stesso lo fissa a 5000 piedi parigini. *Pendulum ad minuta secunda oscillans* e *penduli singulis minutis secundis oscillantis* sono resi entrambi «pendolo che batte i secondi» (glossario), salvo III.G4.06, dove *faciendo ut pendulum simplex ad minuta singula secunda … oscillaret* descrive l’operazione («facendo oscillare un pendolo semplice una volta per ogni secondo»).

### A.1 Propp. XV e XVI

**Prop. XV — Latino:** *Invenire orbium principales diametros.* **Inglese:** “To find the principal diameters of the orbits of the planets.”

**Prop. XVI — Latino:** *Invenire orbium eccentricitates & aphelia.* **Inglese:** “To find the eccentricities and aphelions of the planets.”

**Scelte.**

- *orbium* «delle orbite» (glossario: *orbis* = orbita). Motte aggiunge in entrambi gli enunciati «of the planets».
- *Capiendæ sunt hæ* «Questi vanno presi»: il soggetto sono i *diametri* (femminile latino *diametros*); in italiano il maschile.
- *planetæ cujusque revolventis* «di ciascun pianeta che ruota»: il participio dice che il pianeta gira attorno al Sole.
- *ad primam duarum medie proportionalium inter summam illam & solem* «alla prima di due medie proporzionali fra quella somma e il Sole»: si conserva la formula della Prop. LX del Libro I (Fascicolo 10, S11.13). Motte esplicita «the quantity of matter in the sun».
- *Problema confit* «Il problema si risolve». Motte «is resolved».

### A.2 Prop. XVII

**Latino:** *Planetarum motus diurnos uniformes esse, & librationem lunæ ex ipsius motu diurno oriri.* **Inglese:** “That the diurnal motions of the planets are uniform, and that the libration of the moon arises from its diurnal motion.”

**Scelte.**

- *Patet* «È evidente».
- *Jupiter utique* «Giove, infatti»: *utique* introduce la conferma dai fenomeni.
- *respectu fixarum* «rispetto alle stelle fisse»; *respectu terræ* «rispetto alla Terra».
- *diebus 25⁤12* «25½ giorni»; *27⁤12* «27½».
- *Quoniam vero lunæ circa axem suum uniformiter revolventis dies menstruus est* «Poiché poi il giorno della Luna, che ruota uniformemente attorno al proprio asse, è mensile». Motte aggiunge la glossa «that is, equal to the time of its periodic revolution in its orb».
- *ulteriorem umbilicum orbis ejus* «il fuoco più lontano della sua orbita» (A.0). Motte aggiunge «a little» e «in the lower focus» (la Terra).
- *orta est* «nasce»: il perfetto latino ha valore di stato.
- *ex literis meis* «sulla base di mie lettere». Motte «out of the letters I sent him».
- *in astronomia sua* «nella sua *Astronomia*»: titolo dell’opera di Mercator, in corsivo.
- *ægerrime videtur* «si vede a stento»; *videri cessat* «cessa di essere visibile».
- *jovi aversa* «opposta a Giove»; *tanquam in corpore jovis cernitur* «si vede come se fosse sul corpo di Giove».

### A.3 Prop. XVIII

**Latino:** *Axes planetarum diametris quæ ad eosdem axes normaliter ducuntur minores esse.* **Inglese:** “That the axes of the planets are less than the diameters drawn perpendicular to the axes.”

**Scelte.**

- *sublato omni motu circulari diurno* «tolto ogni moto circolare diurno»; Motte capovolge la costruzione («if it was not for their diurnal revolution»).
- *affectare* «assumere» (tendere a una figura).
- *partes ab axe recedentes* «le parti che si allontanano dall’asse»; *ascendere conentur* «tendano a salire».
- *deprehenditur* «risulta» (si trova all’osservazione).
- *paulo altior* «un poco più alta»: Motte omette *paulo*.
- *subsiderent* «si abbasserebbero»; *inundarent* «inonderebbero».

### A.4 Prop. XIX

**Latino:** *Invenire proportionem axis planetæ ad diametros eidem perpendiculares.* **Inglese:** “To find the proportion of the axis of a planet to the diameters perpendicular thereto.”

**Scelte.**

- *Norwoodus noster* «il nostro Norwood»; Motte «Our countryman».
- *2 gr. 28′* «2 gradi e 28 primi» (minuti d’arco: glossario «primo»).
- *Cassinus senior … filius ejus* «Cassini padre … suo figlio».
- *ad turrem urbis Dunkirk* «alla torre della città di Dunkerque»; Motte «Citadel».
- *ut supra* «come sopra [Prop. IV di questo Libro]»: il valore 15 piedi, 1 pollice, 1 7/9 linee è dato nella Prop. IV (verificato sul latino `L3-P01-14`, § A.8).
- *Ponamus pondus amissum esse partem undecimam millesimam* «Poniamo che il peso perduto sia l’undicimillesima parte»: 1/11000 (SVG 990 di Motte).
- *vis centrifuga … qua corpora directe tendunt a terra* «la forza centrifuga con cui i corpi tendono direttamente ad allontanarsi dalla Terra»: è la componente della forza centrifuga lungo la verticale (nota N4).
- *in duplicata ratione radii ad sinum complementi latitudinis* «nel rapporto duplicato del raggio al seno del complemento della latitudine» (A.0).
- *via tota gravitatis* (trascrizione) è letto *vi tota gravitatis* «con tutta la forza di gravità» (§ A.7).
- *figuram terræ … jam non amplius sphæricam* «la figura della Terra, ormai non più sferica».
- *a polo Qq ad centrum Cc, & inde ad æquatorem Aa pergens* «che va dal polo Qq al centro Cc e di là prosegue fino all’equatore Aa»: le coppie di lettere (Qq, Cc, Aa) indicano le due pareti del canale in ciascun punto.
- *sustinebit ac detrahet* «sosterrà e sottrarrà».
- *computationem ineundo* «impostando il calcolo».
- *convolutione ellipseos APBQ circa axem AB* «dalla rotazione dell’ellisse APBQ attorno all’asse AB»: lo sferoide allungato ausiliario (nota N4).
- *vertitur in* «si muta in».
- *Conjungantur … rationes* «Si compongano … i rapporti».
- *ut magnitudines & gravitates acceleratrices conjunctim* «come le grandezze e le gravità acceleratrici considerate congiuntamente» (glossario: *conjunctim*).
- *secundum regulam auream* «secondo la regola aurea» (A.0).
- *parte centesima totius altitudinis* «di un centesimo dell’altezza totale»: viene dall’ipotesi di prova 100 a 101.
- *luce erratica* «luce erratica» (A.0, N5).
- *Poundus autem noster* «Il nostro Pound, poi».
- *decoquuntur* «si cuociono» (A.0).
- *æuatores* della trascrizione è letto *æquatores* (§ A.7).

### A.5 Prop. XX

**Latino:** *Invenire & inter se comparare pondera corporum in terræ hujus regionibus diversis.* **Inglese:** “To find and compare together the weights of bodies in the different regions of our earth.”

**Scelte.**

- *canalis aqueæ ACQqca* «del canale d’acqua ACQqca» (lo stesso della Prop. XIX).
- *similiter in totis sitarum* «situate in modo simile negli interi».
- *Et par est ratio* «E lo stesso vale».
- *dantur proportione* «sono dati in proporzione».
- *Unde tale confit theorema* «Di qui si ottiene questo teorema».
- *sinus versus latitudinis duplicatæ* «il seno verso del doppio della latitudine»; *quadratum sinus recti latitudinis* «il quadrato del seno retto della latitudine».
- *11334, 00000 & 20000* «11334, 00000 e 20000»: la virgola separa i tre valori (Parigi, equatore, polo); la trascrizione scrive lo zero dell’equatore come «00000», e Motte lo fonde con il primo numero («11334,00000»).
- *vel potius ob pondus aëris 8⁤59* «o piuttosto, per il peso dell’aria, 8 5/9».
- *superabitur a longitudine synchroni penduli Parisiensis, excessu lineæ unius & 87 partium millesimarum lineæ* «sarà superata dalla lunghezza del pendolo sincrono di Parigi di un eccesso di una linea e 87 millesimi di linea»; Motte «shorter by 1,087 lines».
- *Et simuli computo* (trascrizione) è letto *simili computo* «con un calcolo simile» (§ A.7).
- *pro medio motu solis* «di quanto richiedesse il moto medio del Sole».
- *sæpius singulis septimanis* «più volte ogni settimana».
- *thecæ cochleæ & ponderi pendulo* «fra la chiocciola della vite e il peso del pendolo» (A.0).
- *Rectius posuisset* «Più correttamente avrebbe posto».
- *Crassioribus hujus observationibus minus fidendum est* «Alle osservazioni di costui, piuttosto grossolane, si deve prestare meno fede». Motte rafforza: «so gross, that we cannot confide in them».
- *sed errante observatione* «ma l’osservazione era sbagliata».
- *quantum sentio* «per quanto ne giudico».
- *probe congruit* «concorda bene».

### A.6 Le due tabelle

- **Tabella di Pound (III.G3.18).** La trascrizione dà le celle una per riga (tempi, diametri, rapporto in due celle «ut 12» / «ad 11»). Le colonne sono state allineate sul latino e controllate su Motte, che ha le stesse cifre salvo la riga del 9 marzo (sotto). Le intestazioni *dies*, *hor.*, *part.* sono rese «giorno», «ora», «parti» (parti della scala del micrometro).
- **Riga del 9 marzo.** La trascrizione dà «12⁤23 / 14⁤23», cioè 12⅔ a 14⅔: un rapporto **minore di 1**, impossibile per diametro massimo e minimo. Motte (SVG 1005–1006) ha 12⅔ a 11⅔, che torna con le misure (13,12/12,08 = 1,0861; 12⅔/11⅔ = 1,0857). La traduzione conserva 14⅔ con «[*sic*]» (nota N6; § A.7).
- **Tabella dei pendoli e dei gradi (III.G4.04).** La trascrizione dà 27 righe di quattro celle (latitudine, piedi, linee, tese). Le righe 41–44 e 46–49 portano la sola ultima cifra della latitudine, come in Motte: è certamente la convenzione tipografica della stampa (le altre colonne crescono con continuità fra 40 e 45 e fra 45 e 50), e qui sono scritte per intero. Motte ha una riga in meno (§ A.9).

### A.7 Refusi e anomalie della trascrizione

| Luogo | Trascrizione | Lettura | Tipo |
|---|---|---|---|
| III.G3.02 | *per. prop. lx.* | *per prop. lx.* | punto superfluo |
| III.G3.06 | *mars horis 24. 39′. venus* | *24. 39′, venus* | punteggiatura |
| III.G3.06 | *ad planum elipticæ* | *eclipticæ* | refuso probabile |
| III.G3.11 | *Picartus mensurado arcum* | *mensurando* | refuso probabile |
| III.G3.11 | *in Roussilion* | *Roussillon* (Motte) | grafia; da controllare |
| III.G3.12 | *corpus illud grave cedendo in vacuo* | *cadendo* | refuso probabile |
| III.G3.14 | *via tota gravitatis cadendo* | *vi tota gravitatis* | refuso probabile |
| III.G3.06, G3.11, G3.12, G3.15–17, G4.03–14 | *25⁤12*, *11⁤56″*, *1⁤79*, *125⁤12*, *4505*, *1289*, *1229*, *17⁤110*, *295×40094⁤12×1229*, *1×1133420000*, *8⁤59*, *5⁤712*, *1⁤871000* … | 25½, 11⅚″, 1 7/9, 125½, 4/505, 1/289, 1/229, 17 1/10, 29/5 × 400/94½ × 1/229, 1 × 11334/20000, 8 5/9, 5 7/12, 1 87/1000 | frazioni appiattite (artefatto della pagina web); lette con il contesto e con gli SVG di Motte |
| III.G3.18 | *12⁤23 … 14⁤23* (9 marzo) | 12⅔ a 11⅔ (Motte) | cifra errata, della trascrizione o della stampa; lasciata nel testo con [*sic*] |
| III.G3.19 | *versus æuatores suos* | *æquatores* | refuso probabile |
| III.G4.03 | *Et simuli computo* | *simili* | refuso probabile |
| III.G4.04 | righe *1, 2, 3, 4* e *6, 7, 8, 9* | 41–44, 46–49 | abbreviazione tipografica |
| III.G4.07 | *Sanctæ Hellenæ* | *Helenæ* | grafia; da controllare |
| III.G4.10 | *quam ped 3. lin.* | *ped. 3.* | punto mancante |
| III.G4.11 | *P. Feuelleus* | (Motte «Feuillé») | grafia; da controllare |
| III.G4.12 | *Guadaloupæ … 14gr. 00′* | Motte 15° 00′ | divergenza; da controllare |
| III.G4.13 | *in deversis regionibus* | *diversis* | refuso probabile |
| III.G4.13 | *partim ad erroribus* | *ab erroribus* | refuso probabile |
| III.G4.14 | *excessu milliarum septendecim* | *milliarium* | refuso probabile |

Nessuno di questi punti è stato verificato sulla stampa del 1726. La traduzione segue il senso; la Parte B riporta il latino esatto della trascrizione.

**Punti da controllare sulla stampa ECCO.**

| Pagina 1726 | Trascrizione | Lettura attesa | Motivo |
|---|---|---|---|
| p. 411 | *per. prop. lx.* | *per prop. lx.* | punto fuori posto |
| p. 412 | *elipticæ* | *eclipticæ* | c mancante |
| p. 413 | *mensurado* | *mensurando* | n mancante |
| p. 413 | *Roussilion* | *Roussillon* | grafia del toponimo |
| p. 413 | *cedendo in vacuo* | *cadendo* | il verbo è *cadere* (cfr. *cadendo describit* poco prima) |
| p. 413 | *via tota gravitatis* | *vi tota gravitatis* | *via* non dà senso; Motte «by its whole … force of gravity» |
| p. 416 | tabella di Pound, 9 marzo: *12⅔ ad 14⅔* | *12⅔ ad 11⅔* | il rapporto deve essere maggiore di 1; Motte ha 11⅔ |
| p. 416 | *æuatores* | *æquatores* | q mancante |
| p. 417 | *11334, 00000 & 20000* | idem | verificare se lo zero è stampato «00000» |
| p. 417 | *simuli computo* | *simili* | vocale errata |
| p. 418 | righe *1, 2, 3, 4*; *6, 7, 8, 9* | 41–44; 46–49 | verificare l’abbreviazione nella stampa |
| p. 418 | riga 75: *9,258 / 57332* | idem | Motte ha la riga 75 con i valori della riga 80; verificare che la stampa 1726 abbia 27 righe |
| p. 419 | *Hellenæ* | *Helenæ* | grafia |
| p. 420 | *ped 3.* | *ped. 3.* | punto mancante |
| p. 420 | *Feuelleus* | ? | grafia del nome (Motte «Feuillé») |
| p. 420 | *Guadaloupæ … 14gr. 00′* | 14° o 15°? | Motte 15° 00′ |
| p. 421 | *deversis* | *diversis* | vocale errata |
| p. 421 | *ad erroribus* | *ab erroribus* | preposizione |
| p. 421 | *milliarum* | *milliarium* | sillaba mancante |

### A.8 Rimandi

**Rimandi ai Libri I e II** (verificati sui fascicoli in `traduzione/`):

| Luogo | Latino | Resa | Verifica |
|---|---|---|---|
| III.G3.02 | *per prop. xv. lib. i.* | «per la Prop. XV del Libro I» | Fasc. 6, S3.27: tempi periodici nel rapporto sesquiplicato degli assi maggiori. Regge (inverso: assi nel subsesquiplicato dei tempi). |
| III.G3.02 | *per. prop. lx. lib. i.* | «per la Prop. LX del Libro I» | Fasc. 10, S11.13: asse dell’orbita attorno al centro comune di gravità sta all’asse attorno al corpo in quiete come S + P alla prima di due medie proporzionali fra S + P e S. Regge alla lettera. |
| III.G3.04 | *per prop. xviii. lib. i.* | «per la Prop. XVIII del Libro I» | Fasc. 6, S4.03: dati il fuoco e gli assi principali, descrivere ellissi per punti dati. Regge: il fuoco è il Sole, l’asse viene dalla Prop. XV, i punti sono luoghi osservati; la costruzione dà eccentricità e afelio. |
| III.G3.06 | *per motus legem 1* | «per la Legge I del moto» | Fasc. 3, Legge I (anche: le trottole non cessano di ruotare). Regge. |
| III.G3.06 | *corol. 22. prop. lxvi. lib. i.* | «il Cor. 22 della Prop. LXVI del Libro I» | Fasc. 10, S11.61: un globo omogeneo ruota con moto semplice e uniforme attorno a un asse d’inclinazione invariabile; la forza centripeta non muta inclinazione né velocità di rotazione. Regge. |
| III.G3.15 | *ex propositionis xci. corol. 2. lib. i.* | «in base al Cor. 2 della Prop. XCI del Libro I» | Fasc. 12, S13.25: forza di uno sferoide su un corpo posto fuori, sull’asse, confrontata con quella della sfera. Regge (Q e A sono estremi d’asse, al limite sulla superficie). |
| III.G3.15 | *per prop. lxxii. lib. i.* | «per la Prop. LXXII del Libro I» | Fasc. 11, S12.05: in punti simili di sfere simili e ugualmente dense la forza è proporzionale al semidiametro. Regge. |
| III.G3.16 | *per corol. 3. prop. xci. lib. i.* | «per il Cor. 3 della Prop. XCI del Libro I» | Fasc. 12, S13.26: dentro lo sferoide, sull’asse «o su un qualsiasi altro diametro dato», l’attrazione è come la distanza dal centro. Regge per entrambi i bracci. |

Otto rimandi (sette al Libro I e la Legge I); **nessuno che non torni**. Nessun rimando al Libro II.

**Rimandi interni al Libro III.**

| Luogo | Latino | Verifica |
|---|---|---|
| III.G3.12 | *pedes Parisienses 15 dig. 1 lin. 1⁤79 ut supra* | Prop. IV (latino `L3-P01-14`): *ideoque est pedum Parisiensium 15. dig. 1. lin. 1⁤79*. Torna. Nella traduzione: «come sopra [Prop. IV di questo Libro]». |
| III.G3.17 | *revolventium densitates ut 400 ad 94⁤12* | Non citato esplicitamente; i valori sono nella Prop. VIII, Cor. 3 (*densitates sunt ut 100, 94⁤12, 67, 400*: Sole, Giove, Saturno, Terra). Torna. |
| III.G3.20 | *in propositione sequente* | Prop. XX, osservazioni dei pendoli (III.G4.06–III.G4.14). Torna. |
| III.G4.03 | *longitudo penduli … pedum trium Parisiensium & linearum 8⁤12* | È il valore di Huygens nella Prop. IV (*linearum 8⁤12, ut observavit Hugenius*). Torna (non citato). |
| III.G4.12 | *pro tabula … superius computata*; *pro superiore calculo* | Tabella III.G4.04 e calcolo III.G4.03. Tornano (nota N8). |
| III.G4.14 | *per theoriam jam ante collecta* | 1 87/1000 di linea, III.G4.03. Torna. |
| III.G4.14 | *ut supra per theoriam prodiit* | Prop. XIX, III.G3.16: 17 1/10 miglia. Torna. |

### A.9 Riepilogo: dove Motte aggiunge, omette o sbaglia

| Luogo | Latino | Motte 1846 | Tipo |
|---|---|---|---|
| III.G3.01, G3.03 | *orbium* | «of the orbits of the planets», «of the planets» | aggiunta |
| III.G3.02 | *& solem* | «and the quantity of matter in the sun» | esplicitazione |
| III.G3.06 | *dies menstruus est* | «is menstrual, that is, equal to the time of its periodic revolution in its orb» | glossa aggiunta |
| III.G3.06 | *deviabit hinc inde a terra* | «will deviate a little … from the earth in the lower focus» | aggiunte |
| III.G3.06 | *Simili motu* | «with a motion like this of the moon» | esplicitazione |
| III.G3.08 | *paulo altior* | «higher» | omissione di *paulo* |
| III.G3.11 | *ad turrem urbis Dunkirk* | «to the Citadel of Dunkirk» | termine diverso |
| III.G3.12 | *dig. 1* | «1 inch» | (corretto: pollice) |
| III.G3.13 | *pedum 0,0523656* | «0,05236561 feet» | **cifra aggiunta** |
| III.G3.14 | *vis qua gravia descendunt* | «by their weight» | aggiunta |
| III.G3.14 | *vi(a) tota gravitatis* | «by its whole undiminished force of gravity» | aggiunta di «undiminished» |
| III.G3.15 | *partem unam … sustinebit* | «(in the one leg)» | aggiunta |
| III.G3.16 | *superficiebus transversis & æquidistantibus* | «transverse, parallel, and equidistant surfaces» | aggiunta di «parallel» |
| III.G3.16 | *si vis centrifuga 4505 faciat* | «if the centrifugal force make» | **omissione della frazione 4/505** |
| III.G3.16 | *pars tantum 1229* (= 1/229) | «only [SVG 995] part» (SVG 995 = 1/289) | **frazione errata** |
| III.G3.16 | *secundum regulam auream* | «by the rule of proportion» | resa per senso |
| III.G3.17 | *augebitur vel minuetur vis centrifuga in duplicata illa ratione* | «nearly in the same duplicate proportion» | aggiunta di «nearly» |
| III.G3.17 | *Pro luce erratica* | «for the irregular refraction of light» | interpretazione (N5) |
| III.G3.17 | *Et Cassinus quidem …* | nuovo capoverso | divisione diversa |
| III.G3.18 | 9 marzo *12⅔ ad 14⅔* | 12⅔ to 11⅔ | Motte torna con l’aritmetica; la trascrizione no |
| III.G3.19 | *decoquuntur* | «condensed by that heat» | interpretazione |
| III.G4.03 | *11334, 00000 & 20000* | «11334,00000 and 20000» | i primi due valori fusi in uno |
| III.G4.04 | riga 75 (*9,258 / 57332*) e riga 80 (*9,329 / 57360*) | una sola riga «75 / 9,329 / 57360» | **riga omessa** (manca la 75 vera, o la 80 ha l’etichetta sbagliata) |
| III.G4.06 | *tardius moverentur* | «do accordingly move slower» | aggiunta di «accordingly» |
| III.G4.06 | *Deinde faciendo* | «Therefore, fitting up» | connettivo diverso |
| III.G4.07 | *Halleius noster* | «our friend Dr. Halley» | aggiunta |
| III.G4.07 | *Pendulum vero brevius reddidit* | «he shortened the rod of his clock» | esplicitazione |
| III.G4.08 | *ped. 3. lin. 6⁤59* (Gorée) | «3 feet and [SVG 878] lines» (SVG 878 = 5/9) | **manca il 6** |
| III.G4.09 | *minus fidendum est* | «we cannot confide in them» | rafforzamento |
| III.G4.12 | *Guadaloupæ … 14gr. 00′* | «15° 00'» | **cifra diversa** |
| III.G4.12 | *densior ad centrum* | «a little denser» | aggiunta di «a little» |

### A.10 Formule SVG di Motte

Ho controllato tutte le **48 formule SVG** degli estratti (59 occorrenze) sul LaTeX di `svg_tex.tsv`, confrontandole con il latino. Tornano tutte salvo queste:

| n | LaTeX | Lettura attesa dal latino | Commento |
|---|---|---|---|
| 995 (terza occorrenza, III.G3.16) | `\tfrac{1}{289}` | 1/229 (*pars tantum 1229*) | Motte ripete 1/289 dove deve stare 1/229; l’inglese diventa contraddittorio con il rapporto 230 : 229 che segue. |
| 878 (III.G4.08, Gorée) | `\tfrac{5}{9}` | 6 5/9 (*lin. 6⁤59*) | Nel testo di Motte manca la parte intera 6 («3 feet and 5/9 lines»), mentre subito dopo dice «differing from the former by two lines». |
| 1005–1006 (III.G3.18) | `12\tfrac{2}{3}`, `11\tfrac{2}{3}` | la trascrizione ha 12⅔ a 14⅔ | Qui è Motte a tornare con l’aritmetica; la cifra dubbia è della trascrizione latina (§ A.7). |

Inoltre Motte omette la formula attesa 4/505 in «if the centrifugal force [4/505] make…» (III.G3.16): non c’è alcun SVG.

---

## Note editoriali e fisiche

Queste note sono aggiunte del presente fascicolo, non affermazioni tradotte da Newton. Le verifiche numeriche sono state eseguite con uno script Python (`tmp/23/verifica.py`). Ciò che proviene da conoscenza generale e non dalle fonti allegate è marcato «(non verificato sulle fonti allegate)».

### N1. Propp. XV–XVI: le orbite dei pianeti

Il «rapporto subsesquiplicato» è l’inverso del sesquiplicato: se i tempi stanno come *T*₁ : *T*₂, i diametri stanno come *T*₁^2/3 : *T*₂^2/3. È la terza legge di Keplero letta al contrario (Prop. XV del Libro I). La correzione della Prop. LX del Libro I tiene conto del fatto che Sole e pianeta ruotano attorno al centro comune di gravità: la «prima di due medie proporzionali» fra *S* + *P* e *S* è (*S* + *P*)^2/3 · *S*^1/3, e il fattore di correzione è [(*S* + *P*)/*S*]^1/3. In termini moderni è la terza legge nella forma *a*³ = *G*(*S* + *P*)*T*²/4π² (non verificato sulle fonti allegate). La Prop. XVI rimanda a una costruzione geometrica (Prop. XVIII del Libro I): noto l’asse maggiore e il fuoco, bastano luoghi osservati del pianeta per tracciare l’ellisse.

### N2. Prop. XVII: rotazioni e librazione

**I periodi di rotazione.** Valori moderni, per confronto (non verificati sulle fonti allegate): Giove 9 h 55 min 30 s (Newton 9 h 56′); Marte 24 h 37 min (24 h 39′); Terra 23 h 56 min 4 s (23 h 56′); Sole circa 25,4 giorni all’equatore (25½); Luna 27,32 giorni = 27 g 7 h 43 min (esatto). Venere ruota in realtà in circa 243 giorni, in verso retrogrado: le «23 ore circa» vengono da osservazioni del Seicento di macchie mal interpretate (non verificato sulle fonti allegate).

**Sole: 27½ e 25½ giorni.** Le macchie tornano nella stessa posizione rispetto alla Terra in 27½ giorni (periodo sinodico); poiché nel frattempo la Terra avanza sulla sua orbita, il periodo rispetto alle stelle fisse è più breve: 1/25,57 = 1/27,5 + 1/365,25. Il valore di Newton, 25½, torna.

**La librazione in longitudine.** La Luna ruota uniformemente su sé stessa, ma percorre l’orbita ellittica con velocità variabile; il moto angolare visto dal fuoco vuoto è all’incirca uniforme, e per questo la faccia rivolta verso il «fuoco più lontano» si sposta di qua e di là rispetto alla Terra, che è nell’altro fuoco. La librazione in latitudine nasce dall’inclinazione dell’asse lunare e dell’orbita. L’attribuzione della teoria a Mercator (*Astronomia*, 1676) è nel testo.

**I satelliti.** Il satellite più esterno di Saturno allora noto è Giapeto, che ha davvero un emisfero scuro e uno chiaro e rotazione sincrona; il satellite più esterno di Giove allora noto è Callisto (non verificato sulle fonti allegate).

### N3. Prop. XVIII: perché i pianeti si schiacciano

L’argomento è qualitativo: la forza centrifuga, massima all’equatore, fa salire la materia fluida verso l’equatore e la fa scendere ai poli. La frase finale è un ragionamento per assurdo: se la Terra fosse sferica, il mare, che obbedisce alla stessa forza, si accumulerebbe all’equatore e lascerebbe scoperti i poli. La Terra solida deve quindi avere la stessa figura dell’oceano.

### N4. Prop. XIX: i conti, uno per uno

**Misure del grado.**

| Dato | Testo | Ricalcolo | Esito |
|---|---|---|---|
| Norwood: 905751 piedi su 2° 28′ | 367196 piedi londinesi | 905751 / 2,4667 = 367196,35 | torna |
| Norwood in tese | 57300 | rapporto implicito piede parigino/londinese = 367196 / (6 × 57300) = 1,0681 | coerente (N11) |
| Cassini: 486156½ tese su 8° 31′ 11⅚″ | 57061 | 486156,5 / 8,519954 = 57060,93 | torna |
| Circonferenza | 123249600 piedi | 57060 × 360 × 6 = 123249600 esatto | usa il grado di **Picard** (con 57061 si avrebbe 123251760) |
| Semidiametro | 19615800 piedi | 123249600 / 2π = 19615783 | torna (arrotondato) |

**Caduta in un secondo.** 15 piedi, 1 pollice, 1 7/9 linee = 2160 + 12 + 1,778 = 2173,778 linee = 2173 7/9 (torna). Con la correzione 1/11000 per la spinta dell’aria: 2173,975, arrotondato a **2174** (torna).

**Forza centrifuga all’equatore.** Qui c’è una cifra che non torna. Un punto a 19615800 piedi dal centro, con il giorno siderale di 23 h 56′ 4″ = 86164 s, percorre in un secondo 2π × 19615800 / 86164 = **1430,41 piedi**, non 1433,46. Il seno verso di 1430,41 piedi è 0,052154 piedi = 7,5101 linee; quello dell’arco di Newton (1433,46²/2*R*) è 0,052376 piedi = 7,5422 linee; il testo dà 0,0523656 piedi = 7,54064 linee, che corrisponde a un arco di 1433,31. Né l’arco né il seno verso seguono esattamente dai dati del capoverso; lo scarto è dello 0,2 % sull’arco e dello 0,4 % sul seno verso. Con il valore ricalcolato il rapporto finale sarebbe circa 290 invece di 289 (2177,25 / 7,5101 = 289,9). Il testo non è stato corretto. Motte stampa 0,05236561, con una cifra in più.

**A Parigi.** 7,54064 × cos²(48° 50′ 10″) = 3,26696, cioè **3,267** (torna). La forza centrifuga a latitudine φ è ω²*R* cos φ, diretta perpendicolarmente all’asse; la sua componente lungo la verticale è ω²*R* cos²φ: è questo il «rapporto duplicato del raggio al seno del complemento». 2174 + 3,267 = 2177,267 = 15 piedi, 1 pollice, 5,267 linee (torna); 2177,267 / 7,54064 = 288,74, arrotondato a **289** (torna).

**Il canale e le attrazioni.** Le tre attrazioni di Newton per uno sferoide omogeneo di assi 100 : 101 si controllano con le formule moderne di Maclaurin per l’ellissoide omogeneo (*g*ᵢ = 2π*G*ρ*A*ᵢ*x*ᵢ; non verificato sulle fonti allegate per le formule) e, per lo sferoide allungato, con un’integrazione numerica a dischi:

| Rapporto | Newton | Calcolo | Esito |
|---|---|---|---|
| gravità in Q: Terra / sfera di raggio QC | 126/125 = 1,00800 | 1,00797 | torna |
| gravità in A: sferoide allungato / sfera di raggio AC | 125/126 = 0,99206 | 0,99205 | torna |
| gravità in A: sfera / Terra (media proporzionale) | 126/125½ = 1,00398 | 1,00400 | torna |
| gravità in Q / gravità in A (Terra) | 501/500 = 1,00200 | 1,00199 | torna |

L’aritmetica del testo: 126 × 126 × 100 / (125 × 125½ × 101) = 1,001996 ≈ 501/500 (torna); 101/100 × 500/501 = 505/501 esatto (torna).

**La regola aurea.** Se la forza centrifuga 4/505 produce un eccesso d’altezza di 1/100, la forza 1/289 produce (1/289) / (4/505) × 1/100 = 505/115600 = **1/228,9**, arrotondato a 1/229 (torna). Di qui 230 : 229.

**Le dimensioni.** Con semidiametro medio 19615800 piedi e rapporto 230 : 229: semiassi 19658536 e 19573064 piedi, differenza 85471,9 (testo 19658600, 19573000, 85472: tornano, i primi due arrotondati alle centinaia); 19615800/5000 = 3923,16 miglia, 85472/5000 = 17,09 = 17 1/10 miglia (torna).

**Confronto moderno** (non verificato sulle fonti allegate). Per un fluido omogeneo in rotazione lenta lo schiacciamento è *f* = 5*m*/4, con *m* = ω²*a*/*g*: con *m* = 1/289 si ha *f* = 1/231,2, molto vicino all’1/230 di Newton (è lo sferoide di Maclaurin). Lo schiacciamento reale della Terra è circa 1/298, perché la Terra è più densa al centro: Newton stesso lo sospetta in III.G4.12. La differenza fra i semiassi reali è circa 21,4 km; 85472 piedi parigini sono circa 27,8 km.

**Giove.** (23 h 56′ / 9 h 56′)² = (1436/596)² = 5,805 ≈ 29/5 (torna). 29/5 × 400/94½ × 1/229 = 0,10721 = 1/9,328 ≈ 1/9⅓ (torna). 37″ × 9⅓ / 10⅓ = 33,419″ = 33″ 25,2‴ (torna). 40 / 36″ 25‴ = 1,09840 e 11⅙ / 10⅙ = 1,09836 (torna). La regola usata («a parità di dimensioni, la differenza dei diametri va come il quadrato della velocità di rotazione e inversamente come la densità») equivale a *m* ∝ ω²/ρ, indipendente dal raggio: è corretta. Lo schiacciamento reale di Giove è circa 1/15,4 (non verificato sulle fonti allegate): più vicino all’1/15 di Cassini e ai rapporti 13 : 12 o 14 : 13 per un Giove più denso al centro (Newton dice «verso il piano dell’equatore») che al valore omogeneo 1/10⅓.

### N5. «Luce erratica»

Newton aggiunge 3″ a entrambi i diametri apparenti di Giove per tenere conto della luce che si diffonde attorno al disco nel telescopio (ciò che oggi si chiama irradiazione o allargamento dell’immagine; non verificato sulle fonti allegate). Motte la intende come «rifrazione irregolare». Il contributo è additivo, non proporzionale: per questo il rapporto dei diametri scende da 10⅓ : 9⅓ a 11⅙ : 10⅙.

### N6. La tabella di Pound

| Data | Max | Min | Max/min | Rapporto del testo | Valore |
|---|---|---|---|---|---|
| 28 gennaio | 13,40 | 12,28 | 1,0912 | 12 : 11 | 1,0909 |
| 6 marzo | 13,12 | 12,20 | 1,0754 | 13¾ : 12¾ | 1,0784 |
| 9 marzo | 13,12 | 12,08 | 1,0861 | 12⅔ : 14⅔ (trascrizione) / 12⅔ : 11⅔ (Motte) | 0,8636 / 1,0857 |
| 9 aprile | 12,32 | 11,48 | 1,0732 | 14½ : 13½ | 1,0741 |

Tutti i rapporti di Newton tornano con le misure (scarto massimo 0,003), salvo il «14⅔» della trascrizione, che dà un rapporto minore di 1: va letto 11⅔ come in Motte. Le misure di Pound indicano uno schiacciamento fra 1/12 e 1/14 circa, minore dell’1/10⅓ del Giove omogeneo: di qui la conclusione di Newton che Giove sia più denso verso il piano dell’equatore.

### N7. Prop. XX: il teorema del seno al quadrato

Il ragionamento: i pesi di corpi uguali alla superficie sono inversamente come le distanze dal centro (per l’equilibrio del canale della Prop. XIX). Su uno sferoide poco schiacciato la distanza dal centro alla latitudine φ è all’incirca *a*(1 − *f* sen²φ), quindi il peso cresce come 1 + *f* sen²φ: l’incremento è proporzionale a sen²φ, cioè al seno verso del doppio della latitudine (1 − cos 2φ = 2 sen²φ). Controlli: il seno verso di 2 × 48° 50′ = 97° 40′, con raggio 10000, è 11334,1 (testo 11334, torna); quello di 180° è 20000 (torna). 1 × 11334/20000 / 229 = 5667/2290000 (esatto). Il pendolo all’equatore: (432 + 8 5/9) × 2290000/2295667 = 439,468 linee = **3 piedi 7,468 linee**, e la differenza con Parigi è 1,0875 linee (testo **1,087**, torna).

In termini moderni (non verificato sulle fonti allegate): il rapporto *g*(polo)/*g*(equatore) reale è circa 1,0053, contro 230/229 = 1,0044 di Newton; il pendolo che batte i secondi a Parigi è lungo circa 994 mm, e 440 5/9 linee parigine, con la linea di 2,256 mm, fanno 993,8 mm.

### N8. La tabella dei pendoli e dei gradi, riga per riga

Ho ricostruito le due colonne con la legge che Newton dichiara: lunghezza del pendolo = 439,468 × (1 + sen²φ/229) linee; grado di meridiano = 56637 + (57382 − 56637) sen²φ tese.

| Lat. | Pendolo (testo) | Calcolo | Scarto (millesimi di linea) | Grado (testo) | Calcolo | Scarto (tese) |
|---|---|---|---|---|---|---|
| 0 | 7,468 | 7,468 | 0,0 | 56637 | 56637,0 | 0,0 |
| 5 | 7,482 | 7,483 | −0,6 | 56642 | 56642,7 | −0,7 |
| 10 | 7,526 | 7,526 | +0,1 | 56659 | 56659,5 | −0,5 |
| 15 | 7,596 | 7,597 | −0,6 | 56687 | 56686,9 | +0,1 |
| 20 | 7,692 | 7,693 | −0,5 | 56724 | 56724,1 | −0,1 |
| 25 | 7,812 | 7,811 | +1,2 | 56769 | 56770,1 | −1,1 |
| 30 | 7,948 | 7,948 | +0,2 | 56823 | 56823,2 | −0,2 |
| 35 | 8,099 | 8,099 | −0,4 | 56882 | 56882,1 | −0,1 |
| 40 | 8,261 | 8,261 | +0,1 | 56945 | 56944,8 | +0,2 |
| 41 | 8,294 | 8,294 | 0,0 | 56958 | 56957,7 | +0,3 |
| 42 | 8,327 | 8,327 | −0,3 | 56971 | 56970,6 | +0,4 |
| 43 | 8,361 | 8,361 | +0,4 | 56984 | 56983,5 | +0,5 |
| 44 | 8,394 | 8,394 | −0,1 | 56997 | 56996,5 | +0,5 |
| 45 | 8,428 | 8,428 | +0,4 | 57010 | 57009,5 | +0,5 |
| 46 | 8,461 | 8,461 | 0,0 | 57022 | 57022,5 | −0,5 |
| 47 | 8,494 | 8,494 | −0,5 | 57035 | 57035,5 | −0,5 |
| 48 | 8,528 | 8,528 | +0,1 | 57048 | 57048,4 | −0,4 |
| 49 | 8,561 | 8,561 | −0,1 | 57061 | 57061,3 | −0,3 |
| 50 | 8,594 | 8,594 | −0,2 | 57074 | 57074,2 | −0,2 |
| 55 | 8,756 | 8,756 | +0,3 | 57137 | 57136,9 | +0,1 |
| 60 | 8,907 | 8,907 | −0,3 | 57196 | 57195,8 | +0,2 |
| 65 | 9,044 | 9,044 | −0,3 | 57250 | 57248,9 | +1,1 |
| 70 | 9,162 | 9,163 | −0,6 | 57295 | 57294,9 | +0,1 |
| 75 | 9,258 | 9,259 | −0,5 | 57332 | 57332,1 | −0,1 |
| 80 | 9,329 | 9,329 | −0,2 | 57360 | 57359,5 | +0,5 |
| 85 | 9,372 | 9,373 | −0,5 | 57377 | 57376,3 | +0,7 |
| 90 | 9,387 | 9,387 | −0,1 | 57382 | 57382,0 | 0,0 |

**Esito: tutte le 27 righe tornano** entro 1,2 millesimi di linea e 1,1 tese, cioè entro l’arrotondamento (gli scarti massimi, alle righe 25 e 65, sono di una unità dell’ultima cifra). Osservazioni:

- il polo e l’equatore stanno come 230 : 229 per il pendolo (439,468 × 230/229 = 441,387 = 3 piedi 9,387 linee) e come 57382/56637 = 1,013154 per il grado, cioè (230/229)³ = 1,013158: Newton ha preso per il grado il rapporto dei raggi di curvatura del meridiano al polo e all’equatore, *a*²/*c* : *c*²/*a* = (*a*/*c*)³ (interpretazione mia, coerente con le cifre);
- la colonna dei gradi è ancorata in modo che a 49° si abbia **57061**, la misura di Cassini (56637 × (1 + 0,013158 × sen²49°) = 57061,3): anche questo risulta dal calcolo, il testo non lo dice;
- alla latitudine di Parigi (48° 50′) la legge dà 8,5556 linee = 8 5/9, il valore dichiarato in III.G4.03.

### N9. Le osservazioni dei pendoli

**Ritardo dell’orologio e lunghezza del pendolo.** Il periodo va come la radice della lunghezza, quindi un ritardo di Δ*t* secondi al giorno corrisponde a un accorciamento relativo 2Δ*t*/86400. Con il pendolo di Parigi di 440 5/9 linee: 2′ 13″ (Lisbona) → 1,356 linee (Newton 1⅓, torna); 4′ 12″ (Paraíba) → 2,570 linee (Newton 2 5/9 = 2,556, torna). Le correzioni di Newton a Couplet sono dunque giuste. Con la stessa regola, i 2′ 28″ al giorno di Richer darebbero 1,509 linee, non la linea e un quarto che Richer misurò direttamente sul pendolo semplice; Newton non commenta lo scarto (che può dipendere dalla regolazione dell’orologio a Parigi).

**Osservato e calcolato.** Differenza fra il pendolo di Parigi (8 5/9 linee) e quello osservato, confrontata con la legge della tabella alla latitudine indicata da Newton:

| Luogo, osservatore | Latitudine (testo) | Differenza osservata (linee) | Differenza dalla tabella | Eccesso |
|---|---|---|---|---|
| Caienna, Richer 1672 | 4° 55′ bor. | 1,250 | 1,073 | +0,18 |
| Gorée, Varin e Des Hayes 1682 | 14° 40′ bor. | 2,000 | 0,965 | +1,04 |
| Guadalupa, 1682 | 14° 00′ bor. | 2,056 | 0,975 | +1,08 |
| Martinica, 1682 | 14° 44′ bor. | 2,056 | 0,963 | +1,09 |
| Grenada, Des Hayes 1699–1700 | 12° 6′ bor. | poco più di 2,056 | 1,003 | > +1,05 |
| San Cristoforo, Des Hayes | 17° 19′ bor. | 1,806 | 0,918 | +0,89 |
| San Domingo, Des Hayes | 19° 48′ bor. | 1,556 | 0,867 | +0,69 |
| Paraíba, Couplet (corretto) | 6° 38′ austr. | 2,556 | 1,062 | +1,49 |
| Portobelo, Feuillée 1704 | 9° 33′ bor. | 2,972 | 1,035 | +1,94 |
| Martinica, Feuillée | 14° 44′ bor. | 2,722 | 0,963 | +1,76 |

Tutte le differenze osservate superano quelle della tabella, come dice Newton (III.G4.12); l’eccesso va da 0,18 linee (Richer) a circa una linea per le misure del 1682 e di Des Hayes, e a quasi due per Feuillée, che Newton stesso dichiara sbagliato. Il «non minore di una linea e un quarto, non maggiore di 2⅔» di III.G4.13 abbraccia tutte le misure tranne quelle di Feuillée.

**Latitudini** (confronto moderno, non verificato sulle fonti allegate): Caienna 4° 56′, Gorée 14° 40′, Martinica 14° 36′, Grenada 12° 3′, Saint Kitts 17° 18′, Portobelo 9° 33′ tornano bene; Guadalupa è a circa 16°, quindi né il 14° del latino né il 15° di Motte sono esatti; Paraíba (João Pessoa) è a 7° 7′ sud.

### N10. La dilatazione delle verghe

Picard: un piede di ferro si allunga di ¼ di linea al fuoco, cioè di 1/576 = 0,0017; de la Hire: sei piedi si allungano di ⅔ di linea al sole estivo, cioè di 0,00077. Per tre piedi la proporzione di de la Hire darebbe ⅓ di linea; Newton assume che la verga di un orologio, mai esposta al sole, si allunghi meno, «appena più di un quarto di linea», e per l’Inghilterra fra inverno ed estate un sesto di linea. 1¼ − 1/6 = 1 1/12 = 1,083 linee, contro 1,087 della teoria: «concorda bene» (torna). Con il coefficiente moderno del ferro, circa 1,2 × 10⁻⁵ per grado, gli allungamenti di Picard e de la Hire corrispondono a riscaldamenti di circa 145 e 65 gradi, e il sesto di linea su tre piedi a circa 32 gradi (non verificato sulle fonti allegate).

### N11. Unità di misura

Piede parigino = 12 pollici = 144 linee; tesa di Parigi = 6 piedi parigini; miglio = 5000 piedi parigini (definito da Newton in III.G3.16). Dalla misura di Norwood risulta implicitamente che Newton prende il piede parigino uguale a 1,068 piedi londinesi; con i valori moderni (piede parigino 0,3248 m, londinese 0,3048 m) il rapporto è 1,066 (non verificato sulle fonti allegate). Il grado di Picard, 57060 tese, vale circa 111,2 km, molto vicino al valore moderno alla latitudine di Parigi (non verificato sulle fonti allegate).

---

## Controllo della copertura

Pagine 1726 dai marcatori ‹n› della trascrizione. Motte: estratti senza marcatori di pagina, «sezione corrispondente».

| Identificatori | Incipit latino | Contenuto | 1726 | Motte 1846 |
|---|---|---|---|---|
| III.G3.01–III.G3.02 | *Invenire orbium principales diametros* | Prop. XV | p. 411 | Prop. XV |
| III.G3.03–III.G3.04 | *Invenire orbium eccentricitates* | Prop. XVI | p. 411 | Prop. XVI |
| III.G3.05–III.G3.06 | *Planetarum motus diurnos* | Prop. XVII | pp. 411–412 | Prop. XVII |
| III.G3.07–III.G3.08 | *Axes planetarum diametris* | Prop. XVIII | p. 412 | Prop. XVIII |
| III.G3.09–III.G3.10 | *Invenire proportionem axis* … *Norwoodus noster* | Prop. XIX, enunciato; Norwood | pp. 412–413 | Prop. XIX |
| III.G3.11–III.G3.13 | *Picartus mensurado* … *Corpus in circulo* | misure del grado; caduta; forza centrifuga | p. 413 | idem |
| III.G3.14 | *Vis centrifuga corporum in æquatore* | a Parigi: 289 a 1 | pp. 413–414 | idem |
| III.G3.15 | *Unde si APBQ figuram terræ* | canale; 501 a 500 | p. 414 | idem |
| III.G3.16 | *Jam cum (per corol. 3.* | 505 a 501; 230 a 229; dimensioni | p. 415 | idem |
| III.G3.17 | *Si planeta vel major sit* | Giove | pp. 415–416 | idem |
| III.G3.18 | *Tempora. Diam. max.* | tabella di Pound | p. 416 | tabella |
| III.G3.19–III.G3.20 | *Congruit igitur theoria* … *Quinetiam gravitatem* | conclusione; rinvio alla Prop. XX | p. 416 | idem |
| III.G4.01–III.G4.03 | *Invenire & inter se comparare* … *Unde tale confit theorema* | Prop. XX, enunciato, teorema, pendolo all’equatore | p. 417 | Prop. XX |
| III.G4.04–III.G4.05 | *Latitudo loci.* … *Constat autem* | tabella; commento | p. 418 | tabella |
| III.G4.06 | *Jam vero astronomi aliqui* | Richer | pp. 418–419 | idem |
| III.G4.07–III.G4.09 | *Postea Halleius* … *Posthac D. Couplet* | Halley; Varin e Des Hayes; Couplet | p. 419 | idem |
| III.G4.10–III.G4.12 | *Annis proximis* … *Latitudo autem Paraibæ* | Des Hayes; Feuillée; latitudini | p. 420 | idem |
| III.G4.13 | *Observavit utique D. Picartus* | verghe; accordo delle osservazioni | pp. 420–421 | idem |
| III.G4.14 | *Virga ferrea pedes tres longa* | correzione termica; conclusione | p. 421 | idem |

**Controlli eseguiti.**

1. **Copertura frase per frase.** Ogni frase latina è stata estratta per inizio e fine dalla trascrizione (script `tmp/23/build.py`) e associata alla sua traduzione; tolte tutte le frasi tradotte, nel latino restano soltanto i titoli delle proposizioni e le celle delle due tabelle, che sono rese per intero in III.G3.18 e III.G4.04 (script `tmp/23/copertura.py`). Lo stesso controllo su Motte lascia soltanto titoli e tabelle. Nessuna frase manca. I 34 identificatori (20 + 14) sono consecutivi e unici.
2. **Parte B.** `check.py` sul file finale, con i due file latini e i due file di Motte: JSON valido; tutte le stringhe `la` sono sottostringhe esatte della trascrizione; tutte le stringhe `en` sono sottostringhe esatte di Motte; ogni identificatore di `copertura` è presente nel testo. Ultima riga: «OK».
3. **Matematica** (`verifica.py`): tutti i numeri delle Propp. XVII, XIX e XX (N2, N4, N6–N10). Non tornano: l’arco 1433,46 piedi e il seno verso 0,0523656 (N4); il 14⅔ della tabella di Pound (N6). Tutto il resto torna entro l’arrotondamento, comprese le tre attrazioni dello sferoide e tutte le 27 righe della tabella dei pendoli e dei gradi.
4. **Motte.** Confronto di tutta la sezione corrispondente; divergenze nel § A.9; 48 SVG controllati, 2 che non tornano con il latino più uno che non torna con la trascrizione ma con l’aritmetica (§ A.10).
5. **Rimandi.** Otto rimandi ai Libri I e II verificati, nessuno che non torni; sette rimandi interni al Libro III verificati sul latino delle Propp. IV e VIII (§ A.8).
6. **Separazione fra testo e commento.** Il testo tradotto non contiene formule moderne; le frazioni sono quelle di Newton.

**Non ho potuto verificare:**

- **la stampa del 1726**: i diciannove punti del § A.7, in particolare il 14⅔ di Pound, la latitudine di Guadalupa e le righe abbreviate della tabella;
- **la figura originale** della Prop. XIX: la disposizione del canale ACQqca è ricostruita dal testo;
- **Motte 1729**: se la riga mancante della tabella (75° / 80°), lo 0,05236561 e l’1/289 al posto dell’1/229 siano già nella prima edizione o nascano nella ristampa del 1846 o nell’EPUB;
- **la paginazione di Motte**: gli estratti non hanno marcatori di pagina;
- i **valori moderni** citati nelle note N2, N4, N7, N9–N11, che vengono da conoscenza generale;
- l’origine dello scarto **1433,46 / 1430,41** (N4): potrebbe dipendere da un valore intermedio che Newton non riporta.

---

## Registro del lavoro successivo

| Unità | Stato |
|---|---|
| Libro III, Propp. XV–XX | **Fascicolo 23, presente documento, prima versione** |
| Refusi e punti dubbi (§ A.7) | Da verificare sulla stampa del 1726 (scansione ECCO) |
| Tabella di Pound, 9 marzo (14⅔ / 11⅔) | Da verificare sulla stampa; nel testo resta [*sic*] |
| Arco 1433,46 e seno verso 0,0523656 (N4) | Da discutere con il curatore; il testo non è corretto |
| *digitus* «pollice» (misura) e «dito» (eclissi) | Da armonizzare nel glossario del Libro III (A.0) |
| *crus* «braccio», *regula aurea* «regola aurea», *lux erratica* «luce erratica», *decoqui* «cuocersi» | Termini nuovi da armonizzare |
| Motte: riga 75°/80°, Guadalupa 15°, SVG 878 e 995 | Da controllare su Motte 1729 |
| Pagine interattive | Parte B: candidate in particolare la Prop. XIX (canale e catena dei rapporti 289 → 501/500 → 505/501 → 230/229) e la tabella della Prop. XX (curva del pendolo e dei gradi con i punti osservati di N9) |
| Figura NATP00303 della Prop. XIX | Da consultare per confermare `figura_base` |
| Revisione filologica e scientifica indipendente | Da eseguire |

Il presente testo è una nuova traduzione assistita da IA. Non riproduce traduzioni italiane o inglesi moderne. **Licenza prevista** (decisione del curatore, Fascicolo 3): testi e traduzioni CC BY-SA 4.0, codice MIT. La trascrizione latina è © The Newton Project; i testi di Motte sono di pubblico dominio.

---

## Parte B — Dati per le pagine interattive

Unità incluse: **Propp. XV–XX**, con un passo per ogni frase latina; la parte osservativa della Prop. XX è l’unità `L3-P20-Obs` (senza enunciato). Le Propp. XV e XVI hanno un solo passo (la regola e il rimando); le Propp. XVII e XVIII sono argomenti senza figura, inclusi perché contengono dati e calcoli controllabili. Le tabelle e i controlli numerici sono nel campo `dati` delle unità `L3-P19`, `L3-P20` e `L3-P20-Obs`.

Convenzioni:

- `la`: testo latino esatto della trascrizione, refusi e frazioni appiattite compresi, senza marcatori di pagina e senza [FIG];
- `it`: la traduzione di questo fascicolo;
- `en`: Motte 1846, allineato per senso, con i marcatori `[SVG n]`; dove la frase di Motte non coincide con quella latina il campo `nota` lo dice;
- `dipende_da`: soltanto i rimandi citati nella frase latina;
- `identificatore`: il paragrafo del testo tradotto a cui appartiene il passo;
- `figura.mostra`: elementi da rendere visibili, cumulativi; `figura.evidenzia`: relazioni da mettere in risalto.

```json
{
 "fascicolo": "23-L3-P15-20",
 "versione": "0.1",
 "data": "2026-11-08",
 "convenzioni": {
  "dipende_da": "solo rimandi citati esplicitamente nella frase latina",
  "en": "Motte 1846, allineato per senso; [SVG n] = formula stampata come immagine (LaTeX in svg_tex.tsv)",
  "figura.mostra": "elementi da rendere visibili al passo, cumulativi salvo indicazione",
  "la": "",
  "identificatore": "paragrafo del testo tradotto a cui appartiene il passo"
 },
 "unita": [
  {
   "id": "L3-P15",
   "tipo": "Propositio/Problema",
   "titolo": "Prop. XV — diametri principali delle orbite",
   "copertura": [
    "III.G3.01",
    "III.G3.02"
   ],
   "fonti": {
    "la": "",
    "en": "Motte 1846, sezione corrispondente (Book III)"
   },
   "enunciato": {
    "la": "",
    "it": "Trovare i diametri principali delle orbite.",
    "en": "To find the principal diameters of the orbits of the planets."
   },
   "passi": [
    {
     "id": "L3-P15-p1",
     "la": "",
     "it": "Questi vanno presi nel rapporto subsesquiplicato dei tempi periodici, per la Prop. XV del Libro I; poi vanno aumentati uno per uno nel rapporto della somma delle masse del Sole e di ciascun pianeta che ruota, alla prima di due medie proporzionali fra quella somma e il Sole, per la Prop. LX del Libro I.",
     "en": "They are to be taken in the sub-sesquiplicate proportion of the periodic times, by Prop. XV, Book I, and then to be severally augmented in the proportion of the sum of the masses of matter in the sun and each planet to the first of two mean proportionals betwixt that sum and the quantity of matter in the sun, by Prop. LX, Book I.",
     "dipende_da": [
      "Libro I, Prop. XV",
      "Libro I, Prop. LX"
     ],
     "figura": {
      "mostra": [],
      "evidenzia": []
     },
     "nota": "«per. prop. lx.»: punto superfluo della trascrizione.",
     "identificatore": "III.G3.02"
    }
   ]
  },
  {
   "id": "L3-P16",
   "tipo": "Propositio/Problema",
   "titolo": "Prop. XVI — eccentricità e afeli",
   "copertura": [
    "III.G3.03",
    "III.G3.04"
   ],
   "fonti": {
    "la": "",
    "en": "Motte 1846, sezione corrispondente (Book III)"
   },
   "enunciato": {
    "la": "",
    "it": "Trovare le eccentricità e gli afeli delle orbite.",
    "en": "To find the eccentricities and aphelions of the planets."
   },
   "passi": [
    {
     "id": "L3-P16-p1",
     "la": "",
     "it": "Il problema si risolve per la Prop. XVIII del Libro I.",
     "en": "This Problem is resolved by Prop. XVIII, Book I.",
     "dipende_da": [
      "Libro I, Prop. XVIII"
     ],
     "figura": {
      "mostra": [],
      "evidenzia": []
     },
     "identificatore": "III.G3.04"
    }
   ]
  },
  {
   "id": "L3-P17",
   "tipo": "Propositio/Theorema",
   "titolo": "Prop. XVII — moti diurni uniformi; librazione della Luna",
   "copertura": [
    "III.G3.05",
    "III.G3.06"
   ],
   "fonti": {
    "la": "",
    "en": "Motte 1846, sezione corrispondente (Book III)"
   },
   "enunciato": {
    "la": "",
    "it": "I moti diurni dei pianeti sono uniformi, e la librazione della Luna nasce dal suo moto diurno.",
    "en": "That the diurnal motions of the planets are uniform, and that the libration of the moon arises from its diurnal motion."
   },
   "passi": [
    {
     "id": "L3-P17-p1",
     "la": "",
     "it": "È evidente per la Legge I del moto e per il Cor. 22 della Prop. LXVI del Libro I.",
     "en": "The Proposition is proved from the first Law of Motion, and Cor. 22, Prop. LXVI, Book I.",
     "dipende_da": [
      "Legge I",
      "Libro I, Prop. LXVI, Cor. 22"
     ],
     "figura": {
      "mostra": [],
      "evidenzia": []
     },
     "identificatore": "III.G3.06"
    },
    {
     "id": "L3-P17-p2",
     "la": "",
     "it": "Giove, infatti, rispetto alle stelle fisse ruota in 9 ore e 56 minuti, Marte in 24 ore e 39 minuti, Venere in circa 23 ore, la Terra in 23 ore e 56 minuti, il Sole in 25½ giorni e la Luna in 27 giorni, 7 ore e 43 minuti.",
     "en": "Jupiter, with respect to the fixed stars, revolves in 9h. 56'; Mars in 24h. 39'; Venus in about 23h.; the Earth in 23h. 56'; the Sun in [SVG 985] days, and the moon in 27 days, 7 hours, 43'.",
     "dipende_da": [],
     "figura": {
      "mostra": [],
      "evidenzia": []
     },
     "nota": "Il punto dopo «24. 39′» è della trascrizione; la frase prosegue.",
     "identificatore": "III.G3.06"
    },
    {
     "id": "L3-P17-p3",
     "la": "",
     "it": "Che le cose stiano così è manifesto dai fenomeni.",
     "en": "These things appear by the Phænomena.",
     "dipende_da": [],
     "figura": {
      "mostra": [],
      "evidenzia": []
     },
     "identificatore": "III.G3.06"
    },
    {
     "id": "L3-P17-p4",
     "la": "",
     "it": "Le macchie sul corpo del Sole ritornano alla stessa posizione sul disco del Sole in circa 27½ giorni rispetto alla Terra; e perciò rispetto alle stelle fisse il Sole ruota in circa 25½ giorni.",
     "en": "The spots in the sun's body return to the same situation on the sun's disk, with respect to the earth, in [SVG 986] days; and therefore with respect to the fixed stars the sun revolves in about [SVG 985] days.",
     "dipende_da": [],
     "figura": {
      "mostra": [],
      "evidenzia": []
     },
     "identificatore": "III.G3.06"
    },
    {
     "id": "L3-P17-p5",
     "la": "",
     "it": "Poiché poi il giorno della Luna, che ruota uniformemente attorno al proprio asse, è mensile, la stessa sua faccia guarderà sempre, con ottima approssimazione, il fuoco più lontano della sua orbita, e perciò, secondo la posizione di quel fuoco, devierà di qua e di là dalla Terra.",
     "en": "But because the lunar day, arising from its uniform revolution about its axis, is menstrual, that is, equal to the time of its periodic revolution in its orb, therefore the same face of the moon will be always nearly turned to the upper focus of its orb; but, as the situation of that focus requires, will deviate a little to one side and to the other from the earth in the lower focus;",
     "dipende_da": [],
     "figura": {
      "mostra": [],
      "evidenzia": []
     },
     "nota": "Motte aggiunge «that is, equal to the time of its periodic revolution in its orb» e «in the lower focus»; la frase inglese continua con la librazione in longitudine.",
     "identificatore": "III.G3.06"
    },
    {
     "id": "L3-P17-p6",
     "la": "",
     "it": "Questa è la librazione della Luna in longitudine.",
     "en": "and this is the libration in longitude;",
     "dipende_da": [],
     "figura": {
      "mostra": [],
      "evidenzia": []
     },
     "nota": "In Motte è un membro della frase precedente.",
     "identificatore": "III.G3.06"
    },
    {
     "id": "L3-P17-p7",
     "la": "",
     "it": "La librazione in latitudine, infatti, nasce dalla latitudine della Luna e dall’inclinazione del suo asse sul piano dell’eclittica.",
     "en": "for the libration in latitude arises from the moon's latitude, and the inclination of its axis to the plane of the ecliptic.",
     "dipende_da": [],
     "figura": {
      "mostra": [],
      "evidenzia": []
     },
     "nota": "«elipticæ»: refuso probabile della trascrizione per «eclipticæ».",
     "identificatore": "III.G3.06"
    },
    {
     "id": "L3-P17-p8",
     "la": "",
     "it": "Questa teoria della librazione lunare l’ha esposta più ampiamente, sulla base di mie lettere, il signor N. Mercator nella sua *Astronomia*, pubblicata all’inizio dell’anno 1676.",
     "en": "This theory of the libration of the moon, Mr. N. Mercator in his Astronomy, published at the beginning of the year 1676, explained more fully out of the letters I sent him.",
     "dipende_da": [],
     "figura": {
      "mostra": [],
      "evidenzia": []
     },
     "identificatore": "III.G3.06"
    },
    {
     "id": "L3-P17-p9",
     "la": "",
     "it": "Con un moto simile sembra ruotare attorno al proprio asse il satellite più esterno di Saturno, che guarda Saturno sempre con la stessa faccia.",
     "en": "The utmost satellite of Saturn seems to revolve about its axis with a motion like this of the moon, respecting Saturn continually with the same face;",
     "dipende_da": [],
     "figura": {
      "mostra": [],
      "evidenzia": []
     },
     "identificatore": "III.G3.06"
    },
    {
     "id": "L3-P17-p10",
     "la": "",
     "it": "Infatti, ruotando attorno a Saturno, ogni volta che si avvicina alla parte orientale della sua orbita si vede a stento, e per lo più cessa di essere visibile: cosa che può avvenire per certe macchie in quella parte del corpo che allora è rivolta verso la Terra, come ha notato Cassini.",
     "en": "for in its revolution round Saturn, as often as it comes to the eastern part of its orbit, it is scarcely visible, and generally quite disappears; which is like to be occasioned by some spots in that part of its body, which is then turned towards the earth, as M. Cassini has observed.",
     "dipende_da": [],
     "figura": {
      "mostra": [],
      "evidenzia": []
     },
     "identificatore": "III.G3.06"
    },
    {
     "id": "L3-P17-p11",
     "la": "",
     "it": "Con un moto simile sembra ruotare attorno al proprio asse anche il satellite più esterno di Giove, poiché nella parte del corpo opposta a Giove ha una macchia che si vede come se fosse sul corpo di Giove ogni volta che il satellite passa fra Giove e i nostri occhi.",
     "en": "So also the utmost satellite of Jupiter seems to revolve about its axis with a like motion, because in that part of its body which is turned from Jupiter it has a spot, which always appears as if it were in Jupiter's own body, whenever the satellite passes between Jupiter and our eye.",
     "dipende_da": [],
     "figura": {
      "mostra": [],
      "evidenzia": []
     },
     "identificatore": "III.G3.06"
    }
   ]
  },
  {
   "id": "L3-P18",
   "tipo": "Propositio/Theorema",
   "titolo": "Prop. XVIII — gli assi dei pianeti sono minori dei diametri equatoriali",
   "copertura": [
    "III.G3.07",
    "III.G3.08"
   ],
   "fonti": {
    "la": "",
    "en": "Motte 1846, sezione corrispondente (Book III)"
   },
   "enunciato": {
    "la": "",
    "it": "Gli assi dei pianeti sono minori dei diametri condotti perpendicolarmente a quegli stessi assi.",
    "en": "That the axes of the planets are less than the diameters drawn perpendicular to the axes."
   },
   "passi": [
    {
     "id": "L3-P18-p1",
     "la": "",
     "it": "I pianeti, tolto ogni moto circolare diurno, dovrebbero assumere una figura sferica, per l’uguale gravità delle parti da ogni lato.",
     "en": "The equal gravitation of the parts on all sides would give a spherical figure to the planets, if it was not for their diurnal revolution in a circle.",
     "dipende_da": [],
     "figura": {
      "mostra": [],
      "evidenzia": []
     },
     "identificatore": "III.G3.08"
    },
    {
     "id": "L3-P18-p2",
     "la": "",
     "it": "Per quel moto circolare avviene che le parti che si allontanano dall’asse tendano a salire presso l’equatore.",
     "en": "By that circular motion it comes to pass that the parts receding from the axis endeavour to ascend about the equator;",
     "dipende_da": [],
     "figura": {
      "mostra": [],
      "evidenzia": []
     },
     "identificatore": "III.G3.08"
    },
    {
     "id": "L3-P18-p3",
     "la": "",
     "it": "Perciò la materia, se è fluida, salendo verso l’equatore aumenterà i diametri, e scendendo verso i poli diminuirà l’asse.",
     "en": "and therefore if the matter is in a fluid state, by its ascent towards the equator it will enlarge the diameters there, and by its descent towards the poles it will shorten the axis.",
     "dipende_da": [],
     "figura": {
      "mostra": [],
      "evidenzia": []
     },
     "identificatore": "III.G3.08"
    },
    {
     "id": "L3-P18-p4",
     "la": "",
     "it": "Così il diametro di Giove (secondo le osservazioni concordi degli astronomi) risulta più breve fra i poli che da oriente a occidente.",
     "en": "So the diameter of Jupiter (by the concurring observations of astronomers) is found shorter betwixt pole and pole than from east to west.",
     "dipende_da": [],
     "figura": {
      "mostra": [],
      "evidenzia": []
     },
     "identificatore": "III.G3.08"
    },
    {
     "id": "L3-P18-p5",
     "la": "",
     "it": "Con lo stesso argomento, se la nostra Terra non fosse un poco più alta sotto l’equatore che ai poli, i mari si abbasserebbero ai poli e, salendo presso l’equatore, vi inonderebbero ogni cosa.",
     "en": "And, by the same argument, if our earth was not higher about the equator than at the poles, the seas would subside about the poles, and, rising towards the equator, would lay all things there under water.",
     "dipende_da": [],
     "figura": {
      "mostra": [],
      "evidenzia": []
     },
     "nota": "Motte omette «paulo» (un poco).",
     "identificatore": "III.G3.08"
    }
   ]
  },
  {
   "id": "L3-P19",
   "tipo": "Propositio/Problema",
   "titolo": "Prop. XIX — figura della Terra: 230 a 229; Giove",
   "copertura": [
    "III.G3.09",
    "III.G3.10",
    "III.G3.11",
    "III.G3.12",
    "III.G3.13",
    "III.G3.14",
    "III.G3.15",
    "III.G3.16",
    "III.G3.17",
    "III.G3.18",
    "III.G3.19",
    "III.G3.20"
   ],
   "fonti": {
    "la": "",
    "en": "Motte 1846, sezione corrispondente (Book III)"
   },
   "enunciato": {
    "la": "",
    "it": "Trovare la proporzione dell’asse di un pianeta ai diametri a esso perpendicolari.",
    "en": "To find the proportion of the axis of a planet to the diameters perpendicular thereto."
   },
   "figura_base": {
    "punti": [
     "A",
     "P",
     "B",
     "Q",
     "C",
     "a",
     "c",
     "q"
    ],
    "vincoli": [
     "APBQ ellisse; PQ asse minore (asse di rotazione), AB diametro equatoriale; C centro",
     "il solido è generato dalla rivoluzione dell’ellisse attorno a PQ",
     "canale ACQqca: dal polo Qq al centro Cc e di qui all’equatore Aa; Cc, Qq, Aa indicano le due pareti del canale",
     "nel calcolo di prova PQ : AB = 100 : 101; nel risultato AB : PQ = 230 : 229"
    ]
   },
   "passi": [
    {
     "id": "L3-P19-p1",
     "la": "",
     "it": "Il nostro Norwood, verso l’anno 1635, misurando una distanza di 905751 piedi londinesi fra Londra e York e osservando una differenza di latitudine di 2 gradi e 28 primi, ricavò che la misura di un grado è di 367196 piedi londinesi, cioè di 57300 tese parigine.",
     "en": "Our countryman, Mr. Norwood, measuring a distance of 905751 feet of London measure between London and York, in 1635, and observing the difference of latitudes to be 2° 28', determined the measure of one degree to be 367196 feet of London measure, that is 57300 Paris toises.",
     "dipende_da": [],
     "figura": {
      "mostra": [],
      "evidenzia": []
     },
     "identificatore": "III.G3.10"
    },
    {
     "id": "L3-P19-p2",
     "la": "",
     "it": "Picard, misurando un arco di un grado e 22′ 55″ sul meridiano fra Amiens e Malvoisine, trovò che l’arco di un grado è di 57060 tese parigine.",
     "en": "M. Picart, measuring an arc of one degree, and 22' 55'' of the meridian between Amiens and Malvoisine, found an arc of one degree to be 57060 Paris toises.",
     "dipende_da": [],
     "figura": {
      "mostra": [],
      "evidenzia": []
     },
     "nota": "«mensurado»: refuso probabile della trascrizione per «mensurando».",
     "identificatore": "III.G3.11"
    },
    {
     "id": "L3-P19-p3",
     "la": "",
     "it": "Cassini padre misurò la distanza sul meridiano dalla cittadina di Collioure, nel Roussillon, all’Osservatorio di Parigi; e suo figlio aggiunse la distanza dall’Osservatorio alla torre della città di Dunkerque.",
     "en": "M. Cassini, the father, measured the distance upon the meridian from the town of Collioure in Roussillon to the Observatory of Paris; and his son added the distance from the Observatory to the Citadel of Dunkirk.",
     "dipende_da": [],
     "figura": {
      "mostra": [],
      "evidenzia": []
     },
     "nota": "Motte «Citadel» per «turrem» (torre).",
     "identificatore": "III.G3.11"
    },
    {
     "id": "L3-P19-p4",
     "la": "",
     "it": "La distanza totale era di 486156½ tese, e la differenza di latitudine fra la cittadina di Collioure e la città di Dunkerque era di otto gradi e 31′ 11⅚″.",
     "en": "The whole distance was [SVG 987] toises and the difference of the latitudes of Collioure and Dunkirk was 8 degrees, and 31' [SVG 988] .",
     "dipende_da": [],
     "figura": {
      "mostra": [],
      "evidenzia": []
     },
     "identificatore": "III.G3.11"
    },
    {
     "id": "L3-P19-p5",
     "la": "",
     "it": "Di qui l’arco di un grado risulta di 57061 tese parigine.",
     "en": "Hence an arc of one degree appears to be 57061 Paris toises.",
     "dipende_da": [],
     "figura": {
      "mostra": [],
      "evidenzia": []
     },
     "identificatore": "III.G3.11"
    },
    {
     "id": "L3-P19-p6",
     "la": "",
     "it": "E da queste misure si ricava che la circonferenza della Terra è di 123249600 piedi parigini, e il suo semidiametro di 19615800 piedi, nell’ipotesi che la Terra sia sferica.",
     "en": "And from these measures we conclude that the circumference of the earth is 123249600, and its semi-diameter 19615800 Paris feet, upon the supposition that the earth is of a spherical figure.",
     "dipende_da": [],
     "figura": {
      "mostra": [],
      "evidenzia": []
     },
     "identificatore": "III.G3.11"
    },
    {
     "id": "L3-P19-p7",
     "la": "",
     "it": "Alla latitudine di Parigi un corpo grave, cadendo nel tempo di un secondo, descrive 15 piedi parigini, 1 pollice e 1 7/9 linee, come sopra [Prop. IV di questo Libro], cioè 2173 7/9 linee.",
     "en": "In the latitude of Paris a heavy body falling in a second of time describes 15 Paris feet, 1 inch, [SVG 989] line, as above, that is, 2173 lines [SVG 972] .",
     "dipende_da": [
      "Libro III, Prop. IV (ut supra)"
     ],
     "figura": {
      "mostra": [],
      "evidenzia": []
     },
     "identificatore": "III.G3.12"
    },
    {
     "id": "L3-P19-p8",
     "la": "",
     "it": "Il peso del corpo è diminuito dal peso dell’aria circostante.",
     "en": "The weight of the body is diminished by the weight of the ambient air.",
     "dipende_da": [],
     "figura": {
      "mostra": [],
      "evidenzia": []
     },
     "identificatore": "III.G3.12"
    },
    {
     "id": "L3-P19-p9",
     "la": "",
     "it": "Poniamo che il peso perduto sia l’undicimillesima parte del peso totale: quel corpo grave, cadendo nel vuoto, descriverà nel tempo di un secondo un’altezza di 2174 linee.",
     "en": "Let us suppose the weight lost thereby to be [SVG 990] part of the whole weight; then that heavy body falling in vacuo will describe a height of 2174 lines in one second of time.",
     "dipende_da": [],
     "figura": {
      "mostra": [],
      "evidenzia": []
     },
     "nota": "«cedendo»: refuso probabile della trascrizione per «cadendo».",
     "identificatore": "III.G3.12"
    },
    {
     "id": "L3-P19-p10",
     "la": "",
     "it": "Un corpo che, alla distanza di 19615800 piedi dal centro, ruota uniformemente su un cerchio in ciascun giorno siderale di 23 ore, 56 minuti e 4 secondi, nel tempo di un secondo descriverà un arco di 1433,46 piedi, il cui seno verso è di 0,0523656 piedi, ossia di 7,54064 linee.",
     "en": "A body in every sidereal day of 23h. 56' 4'' uniformly revolving in a circle at the distance of 19615800 feet from the centre, in one second of time describes an arc of 1433,46 feet; the versed sine of which is 0,05236561 feet, or 7,54064 lines.",
     "dipende_da": [],
     "figura": {
      "mostra": [
       "cerchio di raggio 19615800 piedi",
       "arco descritto in 1 s e suo seno verso"
      ],
      "evidenzia": [
       "seno verso = 7,54064 linee"
      ]
     },
     "nota": "Motte stampa 0,05236561 (una cifra in più). L’arco 1433,46 non segue dal semidiametro 19615800 e dal giorno siderale (si ottiene 1430,41): nota N4.",
     "identificatore": "III.G3.13"
    },
    {
     "id": "L3-P19-p11",
     "la": "",
     "it": "Perciò la forza con cui i gravi scendono alla latitudine di Parigi sta alla forza centrifuga dei corpi all’equatore, originata dal moto diurno della Terra, come 2174 sta a 7,54064.",
     "en": "And therefore the force with which bodies descend in the latitude of Paris is to the centrifugal force of bodies in the equator arising from the diurnal motion of the earth as 2174 to 7,54064.",
     "dipende_da": [],
     "figura": {
      "mostra": [],
      "evidenzia": []
     },
     "identificatore": "III.G3.13"
    },
    {
     "id": "L3-P19-p12",
     "la": "",
     "it": "La forza centrifuga dei corpi all’equatore della Terra sta alla forza centrifuga con cui i corpi tendono direttamente ad allontanarsi dalla Terra alla latitudine di Parigi, di 48° 50′ 10″, nel rapporto duplicato del raggio al seno del complemento di quella latitudine, cioè come 7,54064 sta a 3,267.",
     "en": "The centrifugal force of bodies in the equator is to the centrifugal force with which bodies recede directly from the earth in the latitude of Paris 48° 50' 10'' in the duplicate proportion of the radius to the cosine of the latitude, that is, as 7,54064 to 3,267.",
     "dipende_da": [],
     "figura": {
      "mostra": [
       "latitudine di Parigi 48° 50′ 10″",
       "componente della forza centrifuga lungo la verticale"
      ],
      "evidenzia": [
       "riduzione nel rapporto del quadrato del coseno"
      ]
     },
     "identificatore": "III.G3.14"
    },
    {
     "id": "L3-P19-p13",
     "la": "",
     "it": "Si aggiunga questa forza alla forza con cui i gravi scendono a quella latitudine di Parigi, e un corpo, a quella latitudine, cadendo con tutta la forza di gravità, nel tempo di un secondo descriverà 2177,267 linee, ossia 15 piedi parigini, 1 pollice e 5,267 linee.",
     "en": "Add this force to the force with which bodies descend by their weight in the latitude of Paris, and a body, in the latitude of Paris, falling by its whole undiminished force of gravity, in the time of one second, will describe 2177·267 lines, or 15 Paris feet, 1 inch, and 5,267 lines.",
     "dipende_da": [],
     "figura": {
      "mostra": [],
      "evidenzia": []
     },
     "nota": "«via tota gravitatis»: refuso probabile per «vi tota gravitatis». Motte aggiunge «undiminished».",
     "identificatore": "III.G3.14"
    },
    {
     "id": "L3-P19-p14",
     "la": "",
     "it": "E la forza totale di gravità a quella latitudine starà alla forza centrifuga dei corpi all’equatore della Terra come 2177,267 sta a 7,54064, ossia come 289 sta a 1.",
     "en": "And the total force of gravity in that latitude will be to the centrifugal force of bodies in the equator of the earth as 2177,267 to 7,54064, or as 289 to 1.",
     "dipende_da": [],
     "figura": {
      "mostra": [],
      "evidenzia": []
     },
     "identificatore": "III.G3.14"
    },
    {
     "id": "L3-P19-p15",
     "la": "",
     "it": "Di qui, se APBQ rappresenta la figura della Terra, ormai non più sferica, ma generata dalla rivoluzione di un’ellisse attorno all’asse minore PQ, e ACQqca è un canale pieno d’acqua che va dal polo Qq al centro Cc e di là prosegue fino all’equatore Aa, il peso dell’acqua nel braccio ACca del canale dovrà stare al peso dell’acqua nell’altro braccio QCcq come 289 sta a 288, per il fatto che la forza centrifuga originata dal moto circolare sosterrà e sottrarrà una delle 289 parti del peso, e il peso 288 nell’altro braccio sosterrà le restanti.",
     "en": "Wherefore if APBQ represent the figure of the earth, now no longer spherical, but generated by the rotation of an ellipsis about its lesser axis PQ; and ACQqca a canal full of water, reaching from the pole Qq to the centre Cc, and thence rising to the equator Aa; the weight of the water in the leg of the canal ACca will be to the weight of water in the other leg QCcq as 289 to 288, because the centrifugal force arising from the circular motion sustains and takes off one of the 289 parts of the weight (in the one leg), and the weight of 288 in the other sustains the rest.",
     "dipende_da": [],
     "figura": {
      "mostra": [
       "ellisse APBQ, asse minore PQ, centro C",
       "canale ACQqca: braccio polare QCcq e braccio equatoriale ACca"
      ],
      "evidenzia": [
       "pesi dei due bracci come 289 a 288"
      ]
     },
     "nota": "Nella trascrizione il segno [FIG] cade fra «altero» e «crure».",
     "identificatore": "III.G3.15"
    },
    {
     "id": "L3-P19-p16",
     "la": "",
     "it": "Inoltre, impostando il calcolo (in base al Cor. 2 della Prop. XCI del Libro I), trovo che, se la Terra fosse costituita di materia uniforme, fosse privata di ogni moto, e il suo asse PQ stesse al diametro AB come 100 sta a 101, la gravità nel luogo Q verso la Terra starebbe alla gravità nello stesso luogo Q verso una sfera descritta con centro C e raggio PC o QC come 126 sta a 125.",
     "en": "But by computation (from Cor. 2, Prop. XCI, Book I) I find, that, if the matter of the earth was all uniform, and without any motion, and its axis PQ were to the diameter AB as 100 to 101, the force of gravity in the place Q towards the earth would be to the force of gravity in the same place Q towards a sphere described about the centre C with the radius PC, or QC, as 126 to 125.",
     "dipende_da": [
      "Libro I, Prop. XCI, Cor. 2"
     ],
     "figura": {
      "mostra": [
       "sfera di centro C e raggio QC"
      ],
      "evidenzia": [
       "gravità in Q: Terra : sfera = 126 : 125"
      ]
     },
     "identificatore": "III.G3.15"
    },
    {
     "id": "L3-P19-p17",
     "la": "",
     "it": "E con lo stesso argomento la gravità nel luogo A verso lo sferoide descritto dalla rotazione dell’ellisse APBQ attorno all’asse AB sta alla gravità nello stesso luogo A verso la sfera descritta con centro C e raggio AC come 125 sta a 126.",
     "en": "And, by the same argument, the force of gravity in the place A towards the spheroid generated by the rotation of the ellipsis APBQ about the axis AB is to the force of gravity in the same place A, towards the sphere described about the centre C with the radius AC, as 125 to 126.",
     "dipende_da": [],
     "figura": {
      "mostra": [
       "sferoide ottenuto ruotando APBQ attorno ad AB",
       "sfera di raggio AC"
      ],
      "evidenzia": [
       "gravità in A: sferoide : sfera = 125 : 126"
      ]
     },
     "identificatore": "III.G3.15"
    },
    {
     "id": "L3-P19-p18",
     "la": "",
     "it": "Ora, la gravità nel luogo A verso la Terra è media proporzionale fra le gravità verso il detto sferoide e verso la sfera: perché la sfera, diminuendo il diametro PQ nel rapporto di 101 a 100, si muta nella figura della Terra; e questa figura, diminuendo nello stesso rapporto il terzo diametro, che è perpendicolare ai due diametri AB, PQ, si muta nel detto sferoide; e la gravità in A, nell’uno e nell’altro caso, diminuisce con ottima approssimazione nello stesso rapporto.",
     "en": "But the force of gravity in the place A towards the earth is a mean proportional betwixt the forces of gravity towards the spheroid and this sphere; because the sphere, by having its diameter PQ diminished in the proportion of 101 to 100, is transformed into the figure of the earth; and this figure, by having a third diameter perpendicular to the two diameters AB and PQ diminished in the same proportion, is converted into the said spheroid; and the force of gravity in A, in either case, is diminished nearly in the same proportion.",
     "dipende_da": [],
     "figura": {
      "mostra": [
       "sfera → Terra (PQ ridotto 101 : 100) → sferoide (terzo diametro ridotto)"
      ],
      "evidenzia": [
       "gravità in A sulla Terra media proporzionale"
      ]
     },
     "identificatore": "III.G3.15"
    },
    {
     "id": "L3-P19-p19",
     "la": "",
     "it": "La gravità in A verso la sfera descritta con centro C e raggio AC sta dunque alla gravità in A verso la Terra come 126 sta a 125½; e la gravità nel luogo Q verso la sfera descritta con centro C e raggio QC sta alla gravità nel luogo A verso la sfera descritta con centro C e raggio AC nel rapporto dei diametri (per la Prop. LXXII del Libro I), cioè come 100 sta a 101.",
     "en": "Therefore the force of gravity in A towards the sphere described about the centre C with the radius AC, is to the force of gravity in A towards the earth as 126 to [SVG 991] . And the force of gravity in the place Q towards the sphere described about the centre C with the radius QC, is to the force of gravity in the place A towards the sphere described about the centre C, with the radius AC, in the proportion of the diameters (by Prop. LXXII, Book I), that is, as 100 to 101.",
     "dipende_da": [
      "Libro I, Prop. LXXII"
     ],
     "figura": {
      "mostra": [
       "sfere di raggi QC e AC"
      ],
      "evidenzia": [
       "126 : 125½",
       "100 : 101"
      ]
     },
     "nota": "Motte divide in due frasi; «en» le comprende entrambe.",
     "identificatore": "III.G3.15"
    },
    {
     "id": "L3-P19-p20",
     "la": "",
     "it": "Si compongano ora questi tre rapporti, 126 a 125, 126 a 125½ e 100 a 101: e la gravità nel luogo Q verso la Terra starà alla gravità nel luogo A verso la Terra come 126 × 126 × 100 sta a 125 × 125½ × 101, ossia come 501 sta a 500.",
     "en": "If, therefore, we compound those three proportions 126 to 125, 126 to [SVG 991] . and 100 to 101, into one, the force of gravity in the place Q towards the earth will be to the force of gravity in the place A towards the earth as [SVG 992] to [SVG 993] ; or as 501 to 500.",
     "dipende_da": [],
     "figura": {
      "mostra": [],
      "evidenzia": [
       "gravità in Q : gravità in A = 501 : 500"
      ]
     },
     "identificatore": "III.G3.15"
    },
    {
     "id": "L3-P19-p21",
     "la": "",
     "it": "Ora, poiché (per il Cor. 3 della Prop. XCI del Libro I) la gravità nell’uno o nell’altro braccio del canale, ACca o QCcq, è come la distanza dei luoghi dal centro della Terra, se quei bracci si dividono con superfici trasversali ed equidistanti in parti proporzionali ai bracci interi, i pesi delle singole parti nel braccio ACca staranno ai pesi di altrettante parti nell’altro braccio come le grandezze e le gravità acceleratrici considerate congiuntamente; cioè come 101 sta a 100 e 500 sta a 501, vale a dire come 505 sta a 501.",
     "en": "Now since (by Cor. 3, Prop. XCI, Book I) the force of gravity in either leg of the canal ACca, or QCcq, is as the distance of the places from the centre of the earth, if those legs are conceived to be divided by transverse, parallel, and equidistant surfaces, into parts proportional to the wholes, the weights of any number of parts in the one leg ACca will be to the weights of the same number of parts in the other leg as their magnitudes and the accelerative forces of their gravity conjunctly, that is, as 101 to 100, and 500 to 501, or as 505 to 501.",
     "dipende_da": [
      "Libro I, Prop. XCI, Cor. 3"
     ],
     "figura": {
      "mostra": [
       "bracci ACca e QCcq divisi da superfici trasversali in parti proporzionali"
      ],
      "evidenzia": [
       "pesi delle parti come 505 a 501"
      ]
     },
     "identificatore": "III.G3.16"
    },
    {
     "id": "L3-P19-p22",
     "la": "",
     "it": "E perciò, se la forza centrifuga di ciascuna parte nel braccio ACca, originata dal moto diurno, fosse stata al peso della stessa parte come 4 sta a 505, così da sottrarre dal peso di ciascuna parte, diviso in 505 parti, quattro parti, i pesi nell’uno e nell’altro braccio resterebbero uguali, e perciò il fluido starebbe in equilibrio.",
     "en": "And therefore if the centrifugal force of every part in the leg ACca, arising from the diurnal motion, was to the weight of the same part as 4 to 505, so that from the weight of every part, conceived to be divided into 505 parts, the centrifugal force might take off four of those parts, the weights would remain equal in each leg, and therefore the fluid would rest in an equilibrium.",
     "dipende_da": [],
     "figura": {
      "mostra": [],
      "evidenzia": [
       "forza centrifuga di equilibrio 4/505"
      ]
     },
     "identificatore": "III.G3.16"
    },
    {
     "id": "L3-P19-p23",
     "la": "",
     "it": "Ma la forza centrifuga di ciascuna parte sta al peso della stessa come 1 sta a 289; cioè la forza centrifuga, che dovrebbe essere i 4/505 del peso, ne è soltanto 1/289.",
     "en": "But the centrifugal force of every part is to the weight of the same part as 1 to 289; that is, the centrifugal force, which should be [SVG 994] parts of the weight, is only [SVG 995] part thereof.",
     "dipende_da": [],
     "figura": {
      "mostra": [],
      "evidenzia": []
     },
     "nota": "«4505» e «1289» della trascrizione valgono 4/505 e 1/289 (frazioni appiattite).",
     "identificatore": "III.G3.16"
    },
    {
     "id": "L3-P19-p24",
     "la": "",
     "it": "E perciò dico, secondo la regola aurea, che, se la forza centrifuga 4/505 fa sì che l’altezza dell’acqua nel braccio ACca superi l’altezza dell’acqua nel braccio QCcq di un centesimo dell’altezza totale, la forza centrifuga 1/289 farà sì che l’eccesso di altezza nel braccio ACca sia soltanto 1/229 dell’altezza nell’altro braccio QCcq.",
     "en": "And, therefore, I say, by the rule of proportion, that if the centrifugal force make the height of the water in the leg ACca to exceed the height of the water in the leg QCcq by one [SVG 996] part of its whole height, the centrifugal force [SVG 995] will make the excess of the height in the leg ACca only [SVG 995] part of the height of the water in the other leg QCcq;",
     "dipende_da": [
      "regola aurea (regola del tre)"
     ],
     "figura": {
      "mostra": [
       "eccesso d’altezza del braccio ACca"
      ],
      "evidenzia": [
       "1/100 con 4/505 → 1/229 con 1/289"
      ]
     },
     "nota": "Motte omette la frazione 4/505 dopo «if the centrifugal force» e stampa [SVG 995] = 1/289 dove il latino ha 1/229 («1229»). La frase inglese prosegue con il rapporto 230 : 229 (passo seguente).",
     "identificatore": "III.G3.16"
    },
    {
     "id": "L3-P19-p25",
     "la": "",
     "it": "Il diametro della Terra secondo l’equatore sta dunque al suo diametro per i poli come 230 sta a 229.",
     "en": "and therefore the diameter of the earth at the equator, is to its diameter from pole to pole as 230 to 229.",
     "dipende_da": [],
     "figura": {
      "mostra": [
       "AB : PQ"
      ],
      "evidenzia": [
       "230 : 229"
      ]
     },
     "nota": "In Motte è il membro finale della frase precedente.",
     "identificatore": "III.G3.16"
    },
    {
     "id": "L3-P19-p26",
     "la": "",
     "it": "E perciò, poiché il semidiametro medio della Terra, secondo la misura di Picard, è di 19615800 piedi parigini, ossia di 3923,16 miglia (posto che il miglio sia una misura di 5000 piedi), la Terra sarà più alta all’equatore che ai poli di un eccesso di 85472 piedi, ossia di 17 1/10 miglia.",
     "en": "And since the mean semi-diameter of the earth, according to Picart's mensuration, is 19615800 Paris feet, or 3923,16 miles (reckoning 5000 feet to a mile), the earth will be higher at the equator than at the poles by 85472 feet, or [SVG 997] miles.",
     "dipende_da": [
      "misura di Picard (III.G3.11)"
     ],
     "figura": {
      "mostra": [],
      "evidenzia": []
     },
     "identificatore": "III.G3.16"
    },
    {
     "id": "L3-P19-p27",
     "la": "",
     "it": "E la sua altezza all’equatore sarà di circa 19658600 piedi, e ai poli di 19573000 piedi.",
     "en": "And its height at the equator will be about 19658600 feet, and at the poles 19573000 feet.",
     "dipende_da": [],
     "figura": {
      "mostra": [],
      "evidenzia": []
     },
     "identificatore": "III.G3.16"
    },
    {
     "id": "L3-P19-p28",
     "la": "",
     "it": "Se un pianeta è maggiore o minore della Terra, restando la sua densità e il tempo periodico della rivoluzione diurna, resterà la proporzione della forza centrifuga alla gravità, e perciò resterà anche la proporzione del diametro fra i poli al diametro secondo l’equatore.",
     "en": "If, the density and periodic time of the diurnal revolution remaining the same, the planet was greater or less than the earth, the proportion of the centrifugal force to that of gravity, and therefore also of the diameter betwixt the poles to the diameter at the equator, would likewise remain the same.",
     "dipende_da": [],
     "figura": {
      "mostra": [],
      "evidenzia": []
     },
     "identificatore": "III.G3.17"
    },
    {
     "id": "L3-P19-p29",
     "la": "",
     "it": "Ma se il moto diurno si accelera o si ritarda in un rapporto qualsiasi, la forza centrifuga aumenterà o diminuirà in quel rapporto duplicato, e perciò la differenza dei diametri aumenterà o diminuirà nello stesso rapporto duplicato, con ottima approssimazione.",
     "en": "But if the diurnal motion was accelerated or retarded in any proportion, the centrifugal force would be augmented or diminished nearly in the same duplicate proportion; and therefore the difference of the diameters will be increased or diminished in the same duplicate ratio very nearly.",
     "dipende_da": [],
     "figura": {
      "mostra": [],
      "evidenzia": []
     },
     "nota": "Motte aggiunge «nearly» anche al primo membro (forza centrifuga).",
     "identificatore": "III.G3.17"
    },
    {
     "id": "L3-P19-p30",
     "la": "",
     "it": "E se la densità del pianeta aumenta o diminuisce in un rapporto qualsiasi, anche la gravità che tende verso di esso aumenterà o diminuirà nello stesso rapporto, e la differenza dei diametri, viceversa, diminuirà nel rapporto della gravità aumentata o aumenterà nel rapporto della gravità diminuita.",
     "en": "And if the density of the planet was augmented or diminished in any proportion, the force of gravity tending towards it would also be augmented or diminished in the same proportion: and the difference of the diameters contrariwise would be diminished in proportion as the force of gravity is augmented, and augmented in proportion as the force of gravity is diminished.",
     "dipende_da": [],
     "figura": {
      "mostra": [],
      "evidenzia": []
     },
     "identificatore": "III.G3.17"
    },
    {
     "id": "L3-P19-p31",
     "la": "",
     "it": "Di qui, poiché la Terra rispetto alle stelle fisse ruota in 23 ore e 56 minuti, Giove invece in 9 ore e 56 minuti, e i quadrati dei tempi stanno come 29 a 5, e le densità dei due corpi rotanti come 400 a 94½, la differenza dei diametri di Giove starà al suo diametro minore come 29/5 × 400/94½ × 1/229 sta a 1, ossia come 1 sta a 9⅓, con ottima approssimazione.",
     "en": "Wherefore, since the earth, in respect of the fixed stars, revolves in 23h. 56', but Jupiter in 9h. 56', and the squares of their periodic times are as 29 to 5, and their densities as 400 to [SVG 982] , the difference of the diameters of Jupiter will be to its lesser diameter as [SVG 998] to 1, or as 1 to [SVG 999] , nearly.",
     "dipende_da": [],
     "figura": {
      "mostra": [],
      "evidenzia": []
     },
     "nota": "«295×40094⁤12×1229» della trascrizione vale 29/5 × 400/94½ × 1/229 (SVG 998 di Motte).",
     "identificatore": "III.G3.17"
    },
    {
     "id": "L3-P19-p32",
     "la": "",
     "it": "Il diametro di Giove condotto da oriente a occidente sta dunque al suo diametro fra i poli come 10⅓ sta a 9⅓, con ottima approssimazione.",
     "en": "Therefore the diameter of Jupiter from east to west is to its diameter from pole to pole nearly as [SVG 1000] to [SVG 999] .",
     "dipende_da": [],
     "figura": {
      "mostra": [],
      "evidenzia": []
     },
     "identificatore": "III.G3.17"
    },
    {
     "id": "L3-P19-p33",
     "la": "",
     "it": "Di qui, poiché il suo diametro maggiore è di 37″, il suo diametro minore, che sta fra i poli, sarà di 33″ 25‴.",
     "en": "Therefore since its greatest diameter is 37'', its lesser diameter lying between the poles will be 33'' 25'''.",
     "dipende_da": [],
     "figura": {
      "mostra": [],
      "evidenzia": []
     },
     "identificatore": "III.G3.17"
    },
    {
     "id": "L3-P19-p34",
     "la": "",
     "it": "Per la luce erratica si aggiungano circa 3″, e i diametri apparenti di questo pianeta diventeranno 40″ e 36″ 25‴, che stanno fra loro come 11⅙ sta a 10⅙, con ottima approssimazione.",
     "en": "Add thereto about 3'' for the irregular refraction of light, and the apparent diameters of this planet will become 40'' and 36'' 25'''; which are to each other as [SVG 1001] to [SVG 1002] , very nearly.",
     "dipende_da": [],
     "figura": {
      "mostra": [],
      "evidenzia": []
     },
     "nota": "Motte «for the irregular refraction of light» per «pro luce erratica» (nota N5).",
     "identificatore": "III.G3.17"
    },
    {
     "id": "L3-P19-p35",
     "la": "",
     "it": "Così stanno le cose nell’ipotesi che il corpo di Giove sia uniformemente denso.",
     "en": "These things are so upon the supposition that the body of Jupiter is uniformly dense.",
     "dipende_da": [],
     "figura": {
      "mostra": [],
      "evidenzia": []
     },
     "identificatore": "III.G3.17"
    },
    {
     "id": "L3-P19-p36",
     "la": "",
     "it": "Ma se il suo corpo è più denso verso il piano dell’equatore che verso i poli, i suoi diametri possono stare fra loro come 12 a 11, o 13 a 12, o forse 14 a 13.",
     "en": "But now if its body be denser towards the plane of the equator than towards the poles, its diameters may be to each other as 12 to 11, or 13 to 12, or perhaps as 14 to 13.",
     "dipende_da": [],
     "figura": {
      "mostra": [],
      "evidenzia": []
     },
     "identificatore": "III.G3.17"
    },
    {
     "id": "L3-P19-p37",
     "la": "",
     "it": "E Cassini, appunto, nell’anno 1691 osservò che il diametro di Giove disteso da oriente a occidente superava l’altro diametro di circa la quindicesima parte di sé.",
     "en": "And Cassini observed in the year 1691, that the diameter of Jupiter reaching from east to west is greater by about a fifteenth part than the other diameter.",
     "dipende_da": [],
     "figura": {
      "mostra": [],
      "evidenzia": []
     },
     "identificatore": "III.G3.17"
    },
    {
     "id": "L3-P19-p38",
     "la": "",
     "it": "Il nostro Pound, poi, con un telescopio lungo 123 piedi e un ottimo micrometro, misurò nell’anno 1719 i diametri di Giove come segue.",
     "en": "Mr. Pound with his 123 feet telescope, and an excellent micrometer, measured the diameters of Jupiter in the year 1719, and found them as follow.",
     "dipende_da": [],
     "figura": {
      "mostra": [],
      "evidenzia": []
     },
     "identificatore": "III.G3.17"
    },
    {
     "id": "L3-P19-p39",
     "la": "",
     "it": "La teoria concorda dunque con i fenomeni.",
     "en": "So that the theory agrees with the phænomena;",
     "dipende_da": [],
     "figura": {
      "mostra": [],
      "evidenzia": []
     },
     "nota": "In Motte è il primo membro di una frase unica.",
     "identificatore": "III.G3.19"
    },
    {
     "id": "L3-P19-p40",
     "la": "",
     "it": "Infatti i pianeti si riscaldano di più alla luce del Sole verso i loro equatori, e perciò lì si cuociono un poco di più che verso i poli.",
     "en": "for the planets are more heated by the sun's rays towards their equators, and therefore are a little more condensed by that heat than towards their poles.",
     "dipende_da": [],
     "figura": {
      "mostra": [],
      "evidenzia": []
     },
     "nota": "«æuatores»: refuso probabile della trascrizione per «æquatores». Motte «condensed» per «decoquuntur».",
     "identificatore": "III.G3.19"
    },
    {
     "id": "L3-P19-p41",
     "la": "",
     "it": "Che poi la gravità diminuisca sotto l’equatore per la rotazione diurna della nostra Terra, e che perciò la Terra lì si innalzi più che ai poli (se la sua materia è uniformemente densa), risulterà dagli esperimenti dei pendoli che sono riferiti nella proposizione seguente.",
     "en": "Moreover, that there is a diminution of gravity occasioned by the diurnal rotation of the earth, and therefore the earth rises higher there than it does at the poles (supposing that its matter is uniformly dense), will appear by the experiments of pendulums related under the following Proposition.",
     "dipende_da": [
      "Libro III, Prop. XX"
     ],
     "figura": {
      "mostra": [],
      "evidenzia": []
     },
     "identificatore": "III.G3.20"
    }
   ],
   "dati": {
    "misure": {
     "Norwood_piedi_lond": 905751,
     "Norwood_diff_lat": "2° 28′",
     "Norwood_grado_calc": 367196.35,
     "Picard_grado_tese": 57060,
     "Cassini_distanza_tese": 486156.5,
     "Cassini_diff_lat": "8° 31′ 11 5/6″",
     "Cassini_grado_calc": 57060.93,
     "circonferenza_piedi": 123249600,
     "circonferenza_da_57060": 123249600,
     "semidiametro_calc": 19615783
    },
    "caduta": {
     "linee_aria": 2173.7778,
     "linee_vuoto_calc": 2173.975,
     "testo": 2174
    },
    "forza_centrifuga": {
     "arco_testo": 1433.46,
     "arco_calc_da_R_e_T": 1430.41,
     "seno_verso_testo_linee": 7.54064,
     "seno_verso_da_arco_testo": 7.5422,
     "seno_verso_da_arco_calc": 7.5101,
     "a_Parigi_testo": 3.267,
     "a_Parigi_calc": 3.26696,
     "rapporto_testo": 289,
     "rapporto_calc": 288.74
    },
    "canale": {
     "126x126x100_su_125x125.5x101": 1.001996,
     "501_su_500": 1.002,
     "505_su_501": "101/100 × 500/501 = 505/501 esatto",
     "eccesso_calc": "1/228,91",
     "testo": "1/229"
    },
    "dimensioni": {
     "semiasse_eq_calc": 19658536,
     "semiasse_pol_calc": 19573064,
     "differenza_calc": 85471.9,
     "testo": [
      19658600,
      19573000,
      85472
     ],
     "miglia_calc": 17.094
    },
    "Giove": {
     "quadrati_tempi_calc": 5.805,
     "testo": "29/5",
     "eccesso_calc": "1/9,328",
     "testo_eccesso": "1/9⅓",
     "diam_min_calc": "33″ 25,2‴",
     "rapporto_40_36_25": 1.0984,
     "rapporto_11_1_6": 1.09836
    },
    "Pound": [
     {
      "data": "28 gen. 6 h",
      "max": 13.4,
      "min": 12.28,
      "rapporto_misure": 1.0912,
      "testo": "12 : 11",
      "rapporto_testo": 1.0909
     },
     {
      "data": "6 mar. 7 h",
      "max": 13.12,
      "min": 12.2,
      "rapporto_misure": 1.0754,
      "testo": "13¾ : 12¾",
      "rapporto_testo": 1.0784
     },
     {
      "data": "9 mar. 7 h",
      "max": 13.12,
      "min": 12.08,
      "rapporto_misure": 1.0861,
      "testo": "12⅔ : 14⅔ (trascrizione); Motte 12⅔ : 11⅔",
      "rapporto_testo_Motte": 1.0857
     },
     {
      "data": "9 apr. 9 h",
      "max": 12.32,
      "min": 11.48,
      "rapporto_misure": 1.0732,
      "testo": "14½ : 13½",
      "rapporto_testo": 1.0741
     }
    ]
   }
  },
  {
   "id": "L3-P20",
   "tipo": "Propositio/Problema",
   "titolo": "Prop. XX — pesi alle diverse latitudini; tabella dei pendoli e dei gradi",
   "copertura": [
    "III.G4.01",
    "III.G4.02",
    "III.G4.03",
    "III.G4.04",
    "III.G4.05"
   ],
   "fonti": {
    "la": "",
    "en": "Motte 1846, sezione corrispondente (Book III)"
   },
   "enunciato": {
    "la": "",
    "it": "Trovare e confrontare fra loro i pesi dei corpi nelle diverse regioni di questa Terra.",
    "en": "To find and compare together the weights of bodies in the different regions of our earth."
   },
   "figura_base": {
    "punti": [
     "A",
     "C",
     "Q",
     "a",
     "c",
     "q"
    ],
    "vincoli": [
     "lo stesso canale ACQqca della Prop. XIX",
     "bracci CA : CQ = 230 : 229"
    ]
   },
   "passi": [
    {
     "id": "L3-P20-p1",
     "la": "",
     "it": "Poiché i pesi dei bracci disuguali del canale d’acqua ACQqca sono uguali, e i pesi delle parti proporzionali ai bracci interi e situate in modo simile negli interi stanno fra loro come i pesi degli interi, e perciò sono anche uguali fra loro, i pesi di parti uguali e situate in modo simile nei bracci saranno inversamente come i bracci, cioè inversamente come 230 a 229.",
     "en": "Because the weights of the unequal legs of the canal of water ACQqca are equal; and the weights of the parts proportional to the whole legs, and alike situated in them, are one to another as the weights of the wholes, and therefore equal betwixt themselves; the weights of equal parts, and alike situated in the legs, will be reciprocally as the legs, that is, reciprocally as 230 to 229.",
     "dipende_da": [],
     "figura": {
      "mostra": [],
      "evidenzia": []
     },
     "identificatore": "III.G4.02"
    },
    {
     "id": "L3-P20-p2",
     "la": "",
     "it": "E lo stesso vale per corpi qualsiasi omogenei e uguali, situati in modo simile nei bracci del canale.",
     "en": "And the case is the same in all homogeneous equal bodies alike situated in the legs of the canal.",
     "dipende_da": [],
     "figura": {
      "mostra": [],
      "evidenzia": []
     },
     "identificatore": "III.G4.02"
    },
    {
     "id": "L3-P20-p3",
     "la": "",
     "it": "I loro pesi sono inversamente come i bracci, cioè inversamente come le distanze dei corpi dal centro della Terra.",
     "en": "Their weights are reciprocally as the legs, that is, reciprocally as the distances of the bodies from the centre of the earth.",
     "dipende_da": [],
     "figura": {
      "mostra": [],
      "evidenzia": []
     },
     "identificatore": "III.G4.02"
    },
    {
     "id": "L3-P20-p4",
     "la": "",
     "it": "Perciò, se i corpi stanno nelle parti più alte dei canali, ossia sulla superficie della Terra, i loro pesi staranno fra loro inversamente come le loro distanze dal centro.",
     "en": "Therefore if the bodies are situated in the uppermost parts of the canals, or on the surface of the earth, their weights will be one to another reciprocally as their distances from the centre.",
     "dipende_da": [],
     "figura": {
      "mostra": [],
      "evidenzia": []
     },
     "identificatore": "III.G4.02"
    },
    {
     "id": "L3-P20-p5",
     "la": "",
     "it": "E con lo stesso argomento i pesi, in qualsiasi altra regione su tutta la superficie della Terra, sono inversamente come le distanze dei luoghi dal centro; e perciò, nell’ipotesi che la Terra sia uno sferoide, sono dati in proporzione.",
     "en": "And, by the same argument, the weights in all other places round the whole surface of the earth are reciprocally as the distances of the places from the centre; and, therefore, in the hypothesis of the earth's being a spheroid are given in proportion.",
     "dipende_da": [],
     "figura": {
      "mostra": [],
      "evidenzia": []
     },
     "identificatore": "III.G4.02"
    },
    {
     "id": "L3-P20-p6",
     "la": "",
     "it": "Di qui si ottiene questo teorema: l’incremento del peso, procedendo dall’equatore verso i poli, è con ottima approssimazione come il seno verso del doppio della latitudine, o, ciò che è lo stesso, come il quadrato del seno retto della latitudine.",
     "en": "Whence arises this Theorem, that the increase of weight in passing from the equator to the poles is nearly as the versed sine of double the latitude; or, which comes to the same thing, as the square of the right sine of the latitude;",
     "dipende_da": [],
     "figura": {
      "mostra": [],
      "evidenzia": []
     },
     "nota": "La frase inglese continua con il passo seguente.",
     "identificatore": "III.G4.03"
    },
    {
     "id": "L3-P20-p7",
     "la": "",
     "it": "E all’incirca nello stesso rapporto crescono gli archi dei gradi di latitudine sul meridiano.",
     "en": "and the arcs of the degrees of latitude in the meridian increase nearly in the same proportion.",
     "dipende_da": [],
     "figura": {
      "mostra": [],
      "evidenzia": []
     },
     "identificatore": "III.G4.03"
    },
    {
     "id": "L3-P20-p8",
     "la": "",
     "it": "E perciò, poiché la latitudine di Parigi è di 48° 50′, quella dei luoghi sotto l’equatore di 00° 00′ e quella dei luoghi ai poli di 90°, e i seni versi dei loro doppi sono 11334, 00000 e 20000, essendo il raggio 10000, e la gravità al polo sta alla gravità sotto l’equatore come 230 a 229, e l’eccesso della gravità al polo sulla gravità sotto l’equatore come 1 a 229, l’eccesso della gravità alla latitudine di Parigi starà alla gravità sotto l’equatore come 1 × 11334/20000 sta a 229, ossia come 5667 a 2290000.",
     "en": "And, therefore, since the latitude of Paris is 48° 50', that of places under the equator 00° 00', and that of places under the poles 90°; and the versed sines of double those arcs are 11334,00000 and 20000, the radius being 10000; and the force of gravity at the pole is to the force of gravity at the equator as 230 to 229; and the excess of the force of gravity at the pole to the force of gravity at the equator as 1 to 229; the excess of the force of gravity in the latitude of Paris will be to the force of gravity at the equator as [SVG 1009] to 229, or as 5667 to 2290000.",
     "dipende_da": [],
     "figura": {
      "mostra": [],
      "evidenzia": []
     },
     "nota": "«1×1133420000» vale 1 × 11334/20000 (SVG 1009 di Motte).",
     "identificatore": "III.G4.03"
    },
    {
     "id": "L3-P20-p9",
     "la": "",
     "it": "E perciò le gravità totali in questi luoghi staranno fra loro come 2295667 a 2290000.",
     "en": "And therefore the whole forces of gravity in those places will be one to the other as 2295667 to 2290000.",
     "dipende_da": [],
     "figura": {
      "mostra": [],
      "evidenzia": []
     },
     "identificatore": "III.G4.03"
    },
    {
     "id": "L3-P20-p10",
     "la": "",
     "it": "Quindi, poiché le lunghezze dei pendoli che oscillano in tempi uguali sono come le gravità, e alla latitudine di Parigi la lunghezza del pendolo che batte i secondi è di tre piedi parigini e 8½ linee, o piuttosto, per il peso dell’aria, 8 5/9, la lunghezza del pendolo sotto l’equatore sarà superata dalla lunghezza del pendolo sincrono di Parigi di un eccesso di una linea e 87 millesimi di linea.",
     "en": "Wherefore since the lengths of pendulums vibrating in equal times are as the forces of gravity, and in the latitude of Paris, the length of a pendulum vibrating seconds is 3 Paris feet, and [SVG 1010] lines, or rather because of the weight of the air, [SVG 1011] lines, the length of a pendulum vibrating in the same time under the equator will be shorter by 1,087 lines.",
     "dipende_da": [],
     "figura": {
      "mostra": [],
      "evidenzia": []
     },
     "identificatore": "III.G4.03"
    },
    {
     "id": "L3-P20-p11",
     "la": "",
     "it": "E con un calcolo simile si ottiene la tabella seguente.",
     "en": "And by a like calculus the following table is made.",
     "dipende_da": [],
     "figura": {
      "mostra": [],
      "evidenzia": []
     },
     "nota": "«simuli»: refuso probabile della trascrizione per «simili».",
     "identificatore": "III.G4.03"
    },
    {
     "id": "L3-P20-p12",
     "la": "",
     "it": "Risulta poi da questa tabella che la disuguaglianza dei gradi è così piccola che nelle questioni geografiche la figura della Terra si può considerare sferica: soprattutto se la Terra è un poco più densa verso il piano dell’equatore che verso i poli.",
     "en": "By this table, therefore, it appears that the inequality of degrees is so small, that the figure of the earth, in geographical matters, may be considered as spherical; especially if the earth be a little denser towards the plane of the equator than towards the poles.",
     "dipende_da": [],
     "figura": {
      "mostra": [],
      "evidenzia": []
     },
     "identificatore": "III.G4.05"
    }
   ],
   "dati": {
    "legge": "pendolo(φ) = 439,468 linee × (1 + sen²φ/229); grado(φ) = 56637 + 745 sen²φ tese",
    "pendolo_equatore_calc_linee": 439.468,
    "eccesso_Parigi_calc": 1.0875,
    "testo": 1.087,
    "rapporto_gradi_polo_equatore": 1.013154,
    "(230/229)^3": 1.013158,
    "tabella": [
     {
      "lat": 0,
      "pendolo_piedi": 3,
      "pendolo_linee": 7.468,
      "grado_tese": 56637,
      "pendolo_calc": 7.468,
      "grado_calc": 56637.0,
      "scarto_pendolo_millesimi": -0.0,
      "scarto_grado_tese": 0.0
     },
     {
      "lat": 5,
      "pendolo_piedi": 3,
      "pendolo_linee": 7.482,
      "grado_tese": 56642,
      "pendolo_calc": 7.483,
      "grado_calc": 56642.7,
      "scarto_pendolo_millesimi": -0.6,
      "scarto_grado_tese": -0.7
     },
     {
      "lat": 10,
      "pendolo_piedi": 3,
      "pendolo_linee": 7.526,
      "grado_tese": 56659,
      "pendolo_calc": 7.526,
      "grado_calc": 56659.5,
      "scarto_pendolo_millesimi": 0.1,
      "scarto_grado_tese": -0.5
     },
     {
      "lat": 15,
      "pendolo_piedi": 3,
      "pendolo_linee": 7.596,
      "grado_tese": 56687,
      "pendolo_calc": 7.597,
      "grado_calc": 56686.9,
      "scarto_pendolo_millesimi": -0.6,
      "scarto_grado_tese": 0.1
     },
     {
      "lat": 20,
      "pendolo_piedi": 3,
      "pendolo_linee": 7.692,
      "grado_tese": 56724,
      "pendolo_calc": 7.693,
      "grado_calc": 56724.1,
      "scarto_pendolo_millesimi": -0.5,
      "scarto_grado_tese": -0.1
     },
     {
      "lat": 25,
      "pendolo_piedi": 3,
      "pendolo_linee": 7.812,
      "grado_tese": 56769,
      "pendolo_calc": 7.811,
      "grado_calc": 56770.1,
      "scarto_pendolo_millesimi": 1.2,
      "scarto_grado_tese": -1.1
     },
     {
      "lat": 30,
      "pendolo_piedi": 3,
      "pendolo_linee": 7.948,
      "grado_tese": 56823,
      "pendolo_calc": 7.948,
      "grado_calc": 56823.2,
      "scarto_pendolo_millesimi": 0.2,
      "scarto_grado_tese": -0.2
     },
     {
      "lat": 35,
      "pendolo_piedi": 3,
      "pendolo_linee": 8.099,
      "grado_tese": 56882,
      "pendolo_calc": 8.099,
      "grado_calc": 56882.1,
      "scarto_pendolo_millesimi": -0.4,
      "scarto_grado_tese": -0.1
     },
     {
      "lat": 40,
      "pendolo_piedi": 3,
      "pendolo_linee": 8.261,
      "grado_tese": 56945,
      "pendolo_calc": 8.261,
      "grado_calc": 56944.8,
      "scarto_pendolo_millesimi": 0.1,
      "scarto_grado_tese": 0.2
     },
     {
      "lat": 41,
      "pendolo_piedi": 3,
      "pendolo_linee": 8.294,
      "grado_tese": 56958,
      "pendolo_calc": 8.294,
      "grado_calc": 56957.7,
      "scarto_pendolo_millesimi": -0.0,
      "scarto_grado_tese": 0.3
     },
     {
      "lat": 42,
      "pendolo_piedi": 3,
      "pendolo_linee": 8.327,
      "grado_tese": 56971,
      "pendolo_calc": 8.327,
      "grado_calc": 56970.6,
      "scarto_pendolo_millesimi": -0.3,
      "scarto_grado_tese": 0.4
     },
     {
      "lat": 43,
      "pendolo_piedi": 3,
      "pendolo_linee": 8.361,
      "grado_tese": 56984,
      "pendolo_calc": 8.361,
      "grado_calc": 56983.5,
      "scarto_pendolo_millesimi": 0.4,
      "scarto_grado_tese": 0.5
     },
     {
      "lat": 44,
      "pendolo_piedi": 3,
      "pendolo_linee": 8.394,
      "grado_tese": 56997,
      "pendolo_calc": 8.394,
      "grado_calc": 56996.5,
      "scarto_pendolo_millesimi": -0.1,
      "scarto_grado_tese": 0.5
     },
     {
      "lat": 45,
      "pendolo_piedi": 3,
      "pendolo_linee": 8.428,
      "grado_tese": 57010,
      "pendolo_calc": 8.428,
      "grado_calc": 57009.5,
      "scarto_pendolo_millesimi": 0.4,
      "scarto_grado_tese": 0.5
     },
     {
      "lat": 46,
      "pendolo_piedi": 3,
      "pendolo_linee": 8.461,
      "grado_tese": 57022,
      "pendolo_calc": 8.461,
      "grado_calc": 57022.5,
      "scarto_pendolo_millesimi": -0.0,
      "scarto_grado_tese": -0.5
     },
     {
      "lat": 47,
      "pendolo_piedi": 3,
      "pendolo_linee": 8.494,
      "grado_tese": 57035,
      "pendolo_calc": 8.494,
      "grado_calc": 57035.5,
      "scarto_pendolo_millesimi": -0.5,
      "scarto_grado_tese": -0.5
     },
     {
      "lat": 48,
      "pendolo_piedi": 3,
      "pendolo_linee": 8.528,
      "grado_tese": 57048,
      "pendolo_calc": 8.528,
      "grado_calc": 57048.4,
      "scarto_pendolo_millesimi": 0.1,
      "scarto_grado_tese": -0.4
     },
     {
      "lat": 49,
      "pendolo_piedi": 3,
      "pendolo_linee": 8.561,
      "grado_tese": 57061,
      "pendolo_calc": 8.561,
      "grado_calc": 57061.3,
      "scarto_pendolo_millesimi": -0.1,
      "scarto_grado_tese": -0.3
     },
     {
      "lat": 50,
      "pendolo_piedi": 3,
      "pendolo_linee": 8.594,
      "grado_tese": 57074,
      "pendolo_calc": 8.594,
      "grado_calc": 57074.2,
      "scarto_pendolo_millesimi": -0.2,
      "scarto_grado_tese": -0.2
     },
     {
      "lat": 55,
      "pendolo_piedi": 3,
      "pendolo_linee": 8.756,
      "grado_tese": 57137,
      "pendolo_calc": 8.756,
      "grado_calc": 57136.9,
      "scarto_pendolo_millesimi": 0.3,
      "scarto_grado_tese": 0.1
     },
     {
      "lat": 60,
      "pendolo_piedi": 3,
      "pendolo_linee": 8.907,
      "grado_tese": 57196,
      "pendolo_calc": 8.907,
      "grado_calc": 57195.8,
      "scarto_pendolo_millesimi": -0.3,
      "scarto_grado_tese": 0.2
     },
     {
      "lat": 65,
      "pendolo_piedi": 3,
      "pendolo_linee": 9.044,
      "grado_tese": 57250,
      "pendolo_calc": 9.044,
      "grado_calc": 57248.9,
      "scarto_pendolo_millesimi": -0.3,
      "scarto_grado_tese": 1.1
     },
     {
      "lat": 70,
      "pendolo_piedi": 3,
      "pendolo_linee": 9.162,
      "grado_tese": 57295,
      "pendolo_calc": 9.163,
      "grado_calc": 57294.9,
      "scarto_pendolo_millesimi": -0.6,
      "scarto_grado_tese": 0.1
     },
     {
      "lat": 75,
      "pendolo_piedi": 3,
      "pendolo_linee": 9.258,
      "grado_tese": 57332,
      "pendolo_calc": 9.259,
      "grado_calc": 57332.1,
      "scarto_pendolo_millesimi": -0.5,
      "scarto_grado_tese": -0.1
     },
     {
      "lat": 80,
      "pendolo_piedi": 3,
      "pendolo_linee": 9.329,
      "grado_tese": 57360,
      "pendolo_calc": 9.329,
      "grado_calc": 57359.5,
      "scarto_pendolo_millesimi": -0.2,
      "scarto_grado_tese": 0.5
     },
     {
      "lat": 85,
      "pendolo_piedi": 3,
      "pendolo_linee": 9.372,
      "grado_tese": 57377,
      "pendolo_calc": 9.373,
      "grado_calc": 57376.3,
      "scarto_pendolo_millesimi": -0.5,
      "scarto_grado_tese": 0.7
     },
     {
      "lat": 90,
      "pendolo_piedi": 3,
      "pendolo_linee": 9.387,
      "grado_tese": 57382,
      "pendolo_calc": 9.387,
      "grado_calc": 57382.0,
      "scarto_pendolo_millesimi": -0.1,
      "scarto_grado_tese": 0.0
     }
    ],
    "esito": "tutte le 27 righe tornano entro 1,2 millesimi di linea e 1,1 tese"
   }
  },
  {
   "id": "L3-P20-Obs",
   "tipo": "Observationes (Prop. XX)",
   "titolo": "Prop. XX — osservazioni dei pendoli (Richer, Halley, Varin e Des Hayes, Couplet, Feuillée) e dilatazione termica",
   "copertura": [
    "III.G4.06",
    "III.G4.07",
    "III.G4.08",
    "III.G4.09",
    "III.G4.10",
    "III.G4.11",
    "III.G4.12",
    "III.G4.13",
    "III.G4.14"
   ],
   "fonti": {
    "la": "",
    "en": "Motte 1846, sezione corrispondente (Book III)"
   },
   "passi": [
    {
     "id": "L3-P20-Obs-p1",
     "la": "",
     "it": "Ora, alcuni astronomi, mandati in regioni lontane per fare osservazioni astronomiche, hanno osservato che gli orologi a pendolo si muovevano più lentamente vicino all’equatore che nelle nostre regioni.",
     "en": "Now several astronomers, sent into remote countries to make astronomical observations, have found that pendulum clocks do accordingly move slower near the equator than in our climates.",
     "dipende_da": [],
     "figura": {
      "mostra": [],
      "evidenzia": []
     },
     "identificatore": "III.G4.06"
    },
    {
     "id": "L3-P20-Obs-p2",
     "la": "",
     "it": "E per primo il signor Richer lo osservò nell’anno 1672 nell’isola di Caienna.",
     "en": "And, first of all, in the year 1672, M. Richer took notice of it in the island of Cayenne;",
     "dipende_da": [],
     "figura": {
      "mostra": [],
      "evidenzia": []
     },
     "identificatore": "III.G4.06"
    },
    {
     "id": "L3-P20-Obs-p3",
     "la": "",
     "it": "Infatti, mentre nel mese di agosto osservava il passaggio delle stelle fisse al meridiano, trovò che il suo orologio si muoveva più lentamente di quanto richiedesse il moto medio del Sole, con una differenza di 2 minuti e 28 secondi ogni giorno.",
     "en": "for when, in the month of August, he was observing the transits of the fixed stars over the meridian, he found his clock to go slower than it ought in respect of the mean motion of the sun at the rate of 2' 28'' a day.",
     "dipende_da": [],
     "figura": {
      "mostra": [],
      "evidenzia": []
     },
     "identificatore": "III.G4.06"
    },
    {
     "id": "L3-P20-Obs-p4",
     "la": "",
     "it": "Poi, facendo oscillare un pendolo semplice una volta per ogni secondo misurato con un ottimo orologio, annotò la lunghezza del pendolo semplice; e lo fece più volte ogni settimana per dieci mesi.",
     "en": "Therefore, fitting up a simple pendulum to vibrate in seconds, which were measured by an excellent clock, he observed the length of that simple pendulum; and this he did over and over every week for ten months together.",
     "dipende_da": [],
     "figura": {
      "mostra": [],
      "evidenzia": []
     },
     "identificatore": "III.G4.06"
    },
    {
     "id": "L3-P20-Obs-p5",
     "la": "",
     "it": "Poi, tornato in Francia, confrontò la lunghezza di questo pendolo con la lunghezza del pendolo di Parigi (che era di tre piedi parigini e otto linee e tre quinti di linea) e la trovò più breve, con una differenza di una linea e un quarto.",
     "en": "And upon his return to France, comparing the length of that pendulum with the length of the pendulum at Paris (which was 3 Paris feet and [SVG 1012] lines), he found it shorter by [SVG 1013] line.",
     "dipende_da": [],
     "figura": {
      "mostra": [],
      "evidenzia": []
     },
     "identificatore": "III.G4.06"
    },
    {
     "id": "L3-P20-Obs-p6",
     "la": "",
     "it": "In seguito il nostro Halley, navigando verso l’isola di Sant’Elena verso l’anno 1677, trovò che il suo orologio a pendolo lì si muoveva più lentamente che a Londra, ma non annotò la differenza.",
     "en": "Afterwards, our friend Dr. Halley, about the year 1677, arriving at the island of St. Helena, found his pendulum clock to go slower there than at London without marking the difference.",
     "dipende_da": [],
     "figura": {
      "mostra": [],
      "evidenzia": []
     },
     "identificatore": "III.G4.07"
    },
    {
     "id": "L3-P20-Obs-p7",
     "la": "",
     "it": "Rese però il pendolo più breve di più di un ottavo di pollice, ossia di una linea e mezza.",
     "en": "But he shortened the rod of his clock by more than the [SVG 637] of an inch, or [SVG 208] line;",
     "dipende_da": [],
     "figura": {
      "mostra": [],
      "evidenzia": []
     },
     "identificatore": "III.G4.07"
    },
    {
     "id": "L3-P20-Obs-p8",
     "la": "",
     "it": "E per ottenere questo, poiché la lunghezza della vite nella parte inferiore del pendolo non bastava, interpose un anello di legno fra la chiocciola della vite e il peso del pendolo.",
     "en": "and to effect this, because the length of the screw at the lower end of the rod was not sufficient, he interposed a wooden ring betwixt the nut and the ball.",
     "dipende_da": [],
     "figura": {
      "mostra": [],
      "evidenzia": []
     },
     "identificatore": "III.G4.07"
    },
    {
     "id": "L3-P20-Obs-p9",
     "la": "",
     "it": "Poi, nell’anno 1682, i signori Varin e Des Hayes trovarono che la lunghezza del pendolo che batte i secondi nell’Osservatorio reale di Parigi era di 3 piedi e 8 5/9 linee.",
     "en": "Then, in the year 1682, M. Varin and M. des Hayes found the length of a simple pendulum vibrating in seconds at the Royal Observatory of Paris to be 3 feet and [SVG 1011] lines.",
     "dipende_da": [],
     "figura": {
      "mostra": [],
      "evidenzia": []
     },
     "identificatore": "III.G4.08"
    },
    {
     "id": "L3-P20-Obs-p10",
     "la": "",
     "it": "E nell’isola di Gorée, con lo stesso metodo, trovarono che la lunghezza del pendolo sincrono era di 3 piedi e 6 5/9 linee, con una differenza fra le lunghezze di 2 linee.",
     "en": "And by the same method in the island of Goree, they found the length of an isochronal pendulum to be 3 feet and [SVG 878] lines, differing from the former by two lines.",
     "dipende_da": [],
     "figura": {
      "mostra": [],
      "evidenzia": []
     },
     "nota": "Motte «3 feet and [SVG 878] lines» con SVG 878 = 5/9: manca il 6 (atteso 6 5/9).",
     "identificatore": "III.G4.08"
    },
    {
     "id": "L3-P20-Obs-p11",
     "la": "",
     "it": "E nello stesso anno, navigando verso le isole di Guadalupa e Martinica, trovarono che la lunghezza del pendolo sincrono in queste isole era di 3 piedi e 6½ linee.",
     "en": "And in the same year, going to the islands of Guadeloupe and Martinico, they found that the length of an isochronal pendulum in those islands was 3 feet and [SVG 727] lines.",
     "dipende_da": [],
     "figura": {
      "mostra": [],
      "evidenzia": []
     },
     "identificatore": "III.G4.08"
    },
    {
     "id": "L3-P20-Obs-p12",
     "la": "",
     "it": "Dopo di ciò il signor Couplet figlio, nel mese di luglio dell’anno 1697, regolò il suo orologio a pendolo sul moto medio del Sole nell’Osservatorio reale di Parigi, in modo che per un tempo abbastanza lungo l’orologio concordasse con il moto del Sole.",
     "en": "After this, M. Couplet, the son, in the month of July 1697, at the Royal Observatory of Paris, so fitted his pendulum clock to the mean motion of the sun, that for a considerable time together the clock agreed with the motion of the sun.",
     "dipende_da": [],
     "figura": {
      "mostra": [],
      "evidenzia": []
     },
     "identificatore": "III.G4.09"
    },
    {
     "id": "L3-P20-Obs-p13",
     "la": "",
     "it": "Poi, navigando verso Lisbona, trovò che nel successivo mese di novembre l’orologio andava più lentamente di prima, con una differenza di 2 minuti e 13 secondi in 24 ore.",
     "en": "In November following, upon his arrival at Lisbon, he found his clock to go slower than before at the rate of 2' 13'' in 24 hours.",
     "dipende_da": [],
     "figura": {
      "mostra": [],
      "evidenzia": []
     },
     "identificatore": "III.G4.09"
    },
    {
     "id": "L3-P20-Obs-p14",
     "la": "",
     "it": "E nel marzo seguente, navigando verso Paraíba, trovò che lì il suo orologio andava più lentamente che a Parigi, con una differenza di 4 minuti e 12 secondi in 24 ore.",
     "en": "And next March coming to Paraiba, he found his clock to go slower than at Paris, and at the rate 4' 12'' in 24 hours;",
     "dipende_da": [],
     "figura": {
      "mostra": [],
      "evidenzia": []
     },
     "identificatore": "III.G4.09"
    },
    {
     "id": "L3-P20-Obs-p15",
     "la": "",
     "it": "E afferma che il pendolo che batte i secondi era più breve che a Parigi di 2½ linee a Lisbona e di 3⅔ linee a Paraíba.",
     "en": "and he affirms, that the pendulum vibrating in seconds was shorter at Lisbon by [SVG 959] lines, and at Paraiba by [SVG 1014] lines, than at Paris.",
     "dipende_da": [],
     "figura": {
      "mostra": [],
      "evidenzia": []
     },
     "identificatore": "III.G4.09"
    },
    {
     "id": "L3-P20-Obs-p16",
     "la": "",
     "it": "Più correttamente avrebbe posto le differenze uguali a 1⅓ e a 2 5/9 linee.",
     "en": "He had done better to have reckoned those differences [SVG 1015] and [SVG 1016] :",
     "dipende_da": [],
     "figura": {
      "mostra": [],
      "evidenzia": []
     },
     "identificatore": "III.G4.09"
    },
    {
     "id": "L3-P20-Obs-p17",
     "la": "",
     "it": "Queste differenze, infatti, corrispondono alle differenze di tempo di 2′ 13″ e 4′ 12″.",
     "en": "for these differences correspond to the differences of the times 2' 13'' and 4' 12''.",
     "dipende_da": [],
     "figura": {
      "mostra": [],
      "evidenzia": []
     },
     "identificatore": "III.G4.09"
    },
    {
     "id": "L3-P20-Obs-p18",
     "la": "",
     "it": "Alle osservazioni di costui, piuttosto grossolane, si deve prestare meno fede.",
     "en": "But this gentleman's observations are so gross, that we cannot confide in them.",
     "dipende_da": [],
     "figura": {
      "mostra": [],
      "evidenzia": []
     },
     "identificatore": "III.G4.09"
    },
    {
     "id": "L3-P20-Obs-p19",
     "la": "",
     "it": "Negli anni seguenti (1699 e 1700) il signor Des Hayes, navigando di nuovo verso l’America, determinò che nelle isole di Caienna e di Grenada la lunghezza del pendolo che batte i secondi era poco minore di 3 piedi e 6½ linee, che nell’isola di San Cristoforo quella lunghezza era di 3 piedi e 6¾ linee, e che nell’isola di San Domingo la stessa era di 3 piedi e 7 linee.",
     "en": "In the following years, 1699, and 1700, M. des Hayes, making another voyage to America, determined that in the island of Cayenne and Granada the length of the pendulum vibrating in seconds was a small matter less than 3 feet and [SVG 727] lines; that in the island of St. Christophers it was 3 feet and [SVG 1017] lines; and in the island of St. Domingo 3 feet and 7 lines.",
     "dipende_da": [],
     "figura": {
      "mostra": [],
      "evidenzia": []
     },
     "nota": "«ped 3.»: punto mancante nella trascrizione.",
     "identificatore": "III.G4.10"
    },
    {
     "id": "L3-P20-Obs-p20",
     "la": "",
     "it": "E nell’anno 1704 il padre Feuillée trovò a Portobelo, in America, che la lunghezza del pendolo che batte i secondi era di tre piedi parigini e soltanto 5 7/12 linee, cioè quasi tre linee più breve che a Parigi; ma l’osservazione era sbagliata.",
     "en": "And in the year 1704, P. Feuillé, at Puerto Bello in America, found that the length of the pendulum vibrating in seconds was 3 Paris feet, and only [SVG 1018] lines, that is, almost 3 lines shorter than at Paris; but the observation was faulty.",
     "dipende_da": [],
     "figura": {
      "mostra": [],
      "evidenzia": []
     },
     "nota": "«Feuelleus»: grafia della trascrizione; Motte «Feuillé».",
     "identificatore": "III.G4.11"
    },
    {
     "id": "L3-P20-Obs-p21",
     "la": "",
     "it": "Infatti, navigando poi verso l’isola di Martinica, trovò che la lunghezza del pendolo isocrono era soltanto di tre piedi parigini e 5 10/12 linee.",
     "en": "For afterward, going to the island of Martinico, he found the length of the isochronal pendulum there 3 Paris feet and [SVG 1019] lines.",
     "dipende_da": [],
     "figura": {
      "mostra": [],
      "evidenzia": []
     },
     "identificatore": "III.G4.11"
    },
    {
     "id": "L3-P20-Obs-p22",
     "la": "",
     "it": "Ora, la latitudine di Paraíba è di 6° 38′ australe, e quella di Portobelo di 9° 33′ boreale; e le latitudini delle isole di Caienna, Gorée, Guadalupa, Martinica, Grenada, San Cristoforo e San Domingo sono rispettivamente di 4° 55′, 14° 40′, 14° 00′, 14° 44′, 12° 6′, 17° 19′ e 19° 48′ boreali.",
     "en": "Now the latitude of Paraiba is 6° 38' south; that of Puerto Bello 9° 33' north; and the latitudes of the islands Cayenne, Goree, Guadeloupe, Martinico, Granada, St. Christophers, and St. Domingo, are respectively 4° 55', 14° 40', 15° 00', 14° 44', 12° 06', 17° 19', and 19° 48', north.",
     "dipende_da": [],
     "figura": {
      "mostra": [],
      "evidenzia": []
     },
     "nota": "Motte stampa 15° 00′ per Guadalupa, dove il latino ha 14gr. 00′.",
     "identificatore": "III.G4.12"
    },
    {
     "id": "L3-P20-Obs-p23",
     "la": "",
     "it": "E gli eccessi della lunghezza del pendolo di Parigi sulle lunghezze dei pendoli isocroni osservate a queste latitudini sono un poco maggiori di quelli della tabella delle lunghezze del pendolo calcolata sopra.",
     "en": "And the excesses of the length of the pendulum at Paris above the lengths of the isochronal pendulums observed in those latitudes are a little greater than by the table of the lengths of the pendulum before computed.",
     "dipende_da": [
      "tabella III.G4.04"
     ],
     "figura": {
      "mostra": [],
      "evidenzia": []
     },
     "identificatore": "III.G4.12"
    },
    {
     "id": "L3-P20-Obs-p24",
     "la": "",
     "it": "E perciò la Terra è alquanto più alta sotto l’equatore di quanto dia il calcolo precedente, e più densa al centro che nelle miniere vicine alla superficie, a meno che forse i calori della zona torrida non abbiano un poco aumentato la lunghezza dei pendoli.",
     "en": "And therefore the earth is a little higher under the equator than by the preceding calculus, and a little denser at the centre than in mines near the surface, unless, perhaps, the heats of the torrid zone have a little extended the length of the pendulums.",
     "dipende_da": [
      "calcolo precedente (III.G4.03)"
     ],
     "figura": {
      "mostra": [],
      "evidenzia": []
     },
     "identificatore": "III.G4.12"
    },
    {
     "id": "L3-P20-Obs-p25",
     "la": "",
     "it": "Il signor Picard, infatti, osservò che una verga di ferro, che d’inverno, quando gelava, era lunga un piede, scaldata al fuoco divenne di un piede e un quarto di linea.",
     "en": "For M. Picart has observed, that a rod of iron, which in frosty weather in the winter season was one foot long, when heated by fire, was lengthened into one foot and [SVG 228] line.",
     "dipende_da": [],
     "figura": {
      "mostra": [],
      "evidenzia": []
     },
     "identificatore": "III.G4.13"
    },
    {
     "id": "L3-P20-Obs-p26",
     "la": "",
     "it": "Poi il signor de la Hire osservò che una verga di ferro che, in un analogo periodo invernale, era lunga sei piedi, esposta al sole estivo divenne lunga sei piedi e due terzi di linea.",
     "en": "Afterward M. de la Hire found that a rod of iron, which in the like winter season was 6 feet long, when exposed to the heat of the summer sun, was extended into 6 feet and [SVG 226] line.",
     "dipende_da": [],
     "figura": {
      "mostra": [],
      "evidenzia": []
     },
     "identificatore": "III.G4.13"
    },
    {
     "id": "L3-P20-Obs-p27",
     "la": "",
     "it": "Nel primo caso il calore fu maggiore che nel secondo; in questo, però, fu maggiore del calore delle parti esterne del corpo umano.",
     "en": "In the former case the heat was greater than in the latter; but in the latter it was greater than the heat of the external parts of a human body;",
     "dipende_da": [],
     "figura": {
      "mostra": [],
      "evidenzia": []
     },
     "nota": "In Motte è il primo membro di una lunga frase che arriva fino a «may be neglected; and in this they all agree…».",
     "identificatore": "III.G4.13"
    },
    {
     "id": "L3-P20-Obs-p28",
     "la": "",
     "it": "I metalli, infatti, al sole estivo si riscaldano molto.",
     "en": "for metals exposed to the summer sun acquire a very considerable degree of heat.",
     "dipende_da": [],
     "figura": {
      "mostra": [],
      "evidenzia": []
     },
     "identificatore": "III.G4.13"
    },
    {
     "id": "L3-P20-Obs-p29",
     "la": "",
     "it": "Ma la verga del pendolo in un orologio a pendolo non suole mai essere esposta al calore del sole estivo, e non acquista mai un calore uguale al calore della superficie esterna del corpo umano.",
     "en": "But the rod of a pendulum clock is never exposed to the heat of the summer sun, nor ever acquires a heat equal to that of the external parts of a human body;",
     "dipende_da": [],
     "figura": {
      "mostra": [],
      "evidenzia": []
     },
     "identificatore": "III.G4.13"
    },
    {
     "id": "L3-P20-Obs-p30",
     "la": "",
     "it": "E perciò la verga del pendolo in un orologio, lunga tre piedi, sarà sì un poco più lunga d’estate che d’inverno, ma di un eccesso che supera appena la quarta parte di una linea.",
     "en": "and, therefore, though the 3 feet rod of a pendulum clock will indeed be a little longer in the summer than in the winter season, yet the difference will scarcely amount to [SVG 228] line.",
     "dipende_da": [],
     "figura": {
      "mostra": [],
      "evidenzia": []
     },
     "identificatore": "III.G4.13"
    },
    {
     "id": "L3-P20-Obs-p31",
     "la": "",
     "it": "Perciò la differenza totale di lunghezza dei pendoli che in diverse regioni sono isocroni non può essere attribuita al diverso calore.",
     "en": "Therefore the total difference of the lengths of isochronal pendulums in different climates cannot be ascribed to the difference of heat;",
     "dipende_da": [],
     "figura": {
      "mostra": [],
      "evidenzia": []
     },
     "nota": "«deversis»: refuso probabile della trascrizione per «diversis».",
     "identificatore": "III.G4.13"
    },
    {
     "id": "L3-P20-Obs-p32",
     "la": "",
     "it": "Ma neppure agli errori degli astronomi mandati dalla Francia si deve attribuire questa differenza.",
     "en": "nor indeed to the mistakes of the French astronomers.",
     "dipende_da": [],
     "figura": {
      "mostra": [],
      "evidenzia": []
     },
     "identificatore": "III.G4.13"
    },
    {
     "id": "L3-P20-Obs-p33",
     "la": "",
     "it": "Infatti, sebbene le loro osservazioni non concordino perfettamente fra loro, gli errori sono tuttavia così piccoli che si possono trascurare.",
     "en": "For although there is not a perfect agreement betwixt their observations, yet the errors are so small that they may be neglected;",
     "dipende_da": [],
     "figura": {
      "mostra": [],
      "evidenzia": []
     },
     "identificatore": "III.G4.13"
    },
    {
     "id": "L3-P20-Obs-p34",
     "la": "",
     "it": "E in questo concordano tutti: che i pendoli isocroni sono più brevi sotto l’equatore che nell’Osservatorio reale di Parigi, con una differenza non minore di una linea e un quarto e non maggiore di 2⅔ linee.",
     "en": "and in this they all agree, that isochronal pendulums are shorter under the equator than at the Royal Observatory of Paris, by a difference not less than [SVG 1013] line, nor greater than [SVG 1020] lines.",
     "dipende_da": [],
     "figura": {
      "mostra": [],
      "evidenzia": []
     },
     "identificatore": "III.G4.13"
    },
    {
     "id": "L3-P20-Obs-p35",
     "la": "",
     "it": "Secondo le osservazioni del signor Richer fatte a Caienna la differenza fu di una linea e un quarto.",
     "en": "By the observations of M. Richer, in the island of Cayenne, the difference was [SVG 1013] line.",
     "dipende_da": [],
     "figura": {
      "mostra": [],
      "evidenzia": []
     },
     "identificatore": "III.G4.13"
    },
    {
     "id": "L3-P20-Obs-p36",
     "la": "",
     "it": "Secondo quelle del signor Des Hayes quella differenza, corretta, risultò di una linea e mezza o di una linea e tre quarti.",
     "en": "That difference being corrected by those of M. des Hayes, becomes [SVG 208] line or [SVG 638] line.",
     "dipende_da": [],
     "figura": {
      "mostra": [],
      "evidenzia": []
     },
     "identificatore": "III.G4.13"
    },
    {
     "id": "L3-P20-Obs-p37",
     "la": "",
     "it": "Secondo quelle di altri, meno accurate, la stessa risultò di circa due linee.",
     "en": "By the less accurate observations of others, the same was made about two lines.",
     "dipende_da": [],
     "figura": {
      "mostra": [],
      "evidenzia": []
     },
     "identificatore": "III.G4.13"
    },
    {
     "id": "L3-P20-Obs-p38",
     "la": "",
     "it": "E questa discrepanza poté nascere in parte dagli errori delle osservazioni, in parte dalla dissomiglianza delle parti interne della Terra e dall’altezza dei monti, e in parte dai diversi calori dell’aria.",
     "en": "And this disagreement might arise partly from the errors of the observations, partly from the dissimilitude of the internal parts of the earth, and the height of mountains; partly from the different heats of the air.",
     "dipende_da": [],
     "figura": {
      "mostra": [],
      "evidenzia": []
     },
     "nota": "«ad erroribus»: refuso probabile della trascrizione per «ab erroribus».",
     "identificatore": "III.G4.13"
    },
    {
     "id": "L3-P20-Obs-p39",
     "la": "",
     "it": "Una verga di ferro lunga tre piedi, d’inverno in Inghilterra, è più breve che d’estate di un sesto di linea, per quanto ne giudico.",
     "en": "I take an iron rod of 3 feet long to be shorter by a sixth part of one line in winter time with us here in England than in the summer.",
     "dipende_da": [],
     "figura": {
      "mostra": [],
      "evidenzia": []
     },
     "identificatore": "III.G4.14"
    },
    {
     "id": "L3-P20-Obs-p40",
     "la": "",
     "it": "Per i calori sotto l’equatore si tolga questa quantità dalla differenza di una linea e un quarto osservata da Richer, e resterà 1 1/12 di linea, che concorda bene con 1 87/1000 di linea, ricavata poco prima dalla teoria.",
     "en": "Because of the great heats under the equator, subduct this quantity from the difference of one line and a quarter observed by M. Richer, and there will remain one line [SVG 1021] , which agrees very well with [SVG 1022] line collected, by the theory a little before.",
     "dipende_da": [
      "teoria (III.G4.03)"
     ],
     "figura": {
      "mostra": [],
      "evidenzia": []
     },
     "identificatore": "III.G4.14"
    },
    {
     "id": "L3-P20-Obs-p41",
     "la": "",
     "it": "Richer, poi, ripeté ogni settimana per dieci mesi le osservazioni fatte a Caienna, e confrontò le lunghezze del pendolo lì segnate sulla verga di ferro con le sue lunghezze segnate in modo simile in Francia.",
     "en": "M. Richer repeated his observations, made in the island of Cayenne, every week for ten months together, and compared the lengths of the pendulum which he had there noted in the iron rods with the lengths thereof which he observed in France.",
     "dipende_da": [],
     "figura": {
      "mostra": [],
      "evidenzia": []
     },
     "identificatore": "III.G4.14"
    },
    {
     "id": "L3-P20-Obs-p42",
     "la": "",
     "it": "Questa diligenza e questa cautela sembrano essere mancate agli altri osservatori.",
     "en": "This diligence and care seems to have been wanting to the other observers.",
     "dipende_da": [],
     "figura": {
      "mostra": [],
      "evidenzia": []
     },
     "identificatore": "III.G4.14"
    },
    {
     "id": "L3-P20-Obs-p43",
     "la": "",
     "it": "Se si deve prestar fede alle sue osservazioni, la Terra sarà più alta all’equatore che ai poli di un eccesso di circa diciassette miglia, come è risultato sopra dalla teoria.",
     "en": "If this gentleman's observations are to be depended on, the earth is higher under the equator than at the poles, and that by an excess of about 17 miles; as appeared above by the theory.",
     "dipende_da": [
      "Libro III, Prop. XIX (III.G3.16)"
     ],
     "figura": {
      "mostra": [],
      "evidenzia": []
     },
     "nota": "«milliarum»: refuso probabile della trascrizione per «milliarium».",
     "identificatore": "III.G4.14"
    }
   ],
   "dati": {
    "Parigi_linee": 8.5556,
    "osservazioni": [
     {
      "luogo": "Caienna (Richer 1672)",
      "lat": "4° 55′ N",
      "diff_oss": 1.25,
      "diff_teoria": 1.073
     },
     {
      "luogo": "Gorée (1682)",
      "lat": "14° 40′ N",
      "diff_oss": 2.0,
      "diff_teoria": 0.965
     },
     {
      "luogo": "Guadalupa (1682)",
      "lat": "14° 00′ N",
      "diff_oss": 2.056,
      "diff_teoria": 0.975
     },
     {
      "luogo": "Martinica (1682)",
      "lat": "14° 44′ N",
      "diff_oss": 2.056,
      "diff_teoria": 0.963
     },
     {
      "luogo": "Grenada (Des Hayes 1699–1700, poco meno di 6½)",
      "lat": "12° 6′ N",
      "diff_oss": ">2.056",
      "diff_teoria": 1.003
     },
     {
      "luogo": "S. Cristoforo",
      "lat": "17° 19′ N",
      "diff_oss": 1.806,
      "diff_teoria": 0.918
     },
     {
      "luogo": "S. Domingo",
      "lat": "19° 48′ N",
      "diff_oss": 1.556,
      "diff_teoria": 0.867
     },
     {
      "luogo": "Paraíba (Couplet, corretta da Newton)",
      "lat": "6° 38′ S",
      "diff_oss": 2.556,
      "diff_teoria": 1.062
     },
     {
      "luogo": "Portobelo (Feuillée 1704)",
      "lat": "9° 33′ N",
      "diff_oss": 2.972,
      "diff_teoria": 1.035
     },
     {
      "luogo": "Martinica (Feuillée)",
      "lat": "14° 44′ N",
      "diff_oss": 2.722,
      "diff_teoria": 0.963
     }
    ],
    "ritardo_orologio": {
     "regola": "ΔL/L = 2Δt/86400",
     "Couplet_2m13s_calc": 1.356,
     "Newton": "1⅓",
     "Couplet_4m12s_calc": 2.57,
     "Newton_2": "2 5/9",
     "Richer_2m28s_calc": 1.509,
     "Richer_misura_diretta": 1.25
    },
    "correzione_termica": {
     "1¼ − 1/6": "1 1/12 = 1,083",
     "teoria": 1.087
    }
   },
   "nota": "Unità senza enunciato: è la parte osservativa della Prop. XX (III.G4.06–III.G4.14), separata per comodità delle pagine interattive."
  }
 ]
}
```
