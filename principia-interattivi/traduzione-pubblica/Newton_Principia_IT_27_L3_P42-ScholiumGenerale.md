> **Copia pubblica.** In questa versione i campi `"la"` della Parte B sono vuoti: le frasi latine vengono dalla trascrizione del Newton Project, che non si ridistribuisce. Il latino del 1726 si legge su newtonproject.ox.ac.uk.

# Isaac Newton
# Principi matematici della filosofia naturale

## Fascicolo 27 — Libro III: correzione delle orbite delle comete e Scolio generale

**Nuova traduzione italiana di lavoro dal latino del 1726, confrontata con l’inglese di Andrew Motte nell’edizione del 1846.**

Versione 0.1 — 8 novembre 2026. Preparata con Claude (Anthropic) per Massimo Bosetti.

### Stato e perimetro

Questo fascicolo prosegue i Fascicoli 26a e 26b (Prop. XLI del Libro III) e chiude l’opera. Traduce integralmente:

- la **Proposizione XLII** del Libro III, *Inventam cometæ trajectoriam corrigere* (gruppo G8): le tre operazioni e la soluzione; il confronto fra comete; la cometa del 1664–1665 con la tabella di Halley e le riduzioni delle osservazioni di febbraio e marzo 1665; le comete del 1683, del 1682 e del 1723 con le loro tabelle; la cometa del 1607 e il ritorno dopo 75 anni; le perturbazioni reciproche delle comete, la caduta delle comete nel Sole, le stelle nuove del 1572 e del 1604, le stelle variabili e i vapori;
- lo **Scolio generale** (gruppo G9), con le tre note a piè di pagina di Newton, fino a *FINIS*.

È una traduzione di lavoro, non un’edizione critica validata.

Gli identificatori **III.G8.01–III.G8.28** e **III.G9.01–III.G9.15** e i titoli tematici tra parentesi sono aggiunte editoriali. Servono a orientare la lettura e a controllare la completezza. I numeri romani della proposizione e del problema, e i numeri delle operazioni, appartengono al testo originale. Le integrazioni del curatore sono tra parentesi quadre. Le note poste dopo la traduzione non fanno parte del testo di Newton. Le tre note di Newton allo Scolio generale sono tradotte in fondo allo Scolio con i loro numeri [1]–[3].

La Prop. XLII cita «la proposizione precedente» (*propositionem superiorem*) e il confronto «fatto sopra» con la cometa del 1680: entrambi i rimandi vanno alla Prop. XLI, tradotta nei Fascicoli 26a e 26b. Per questi rimandi ho letto il latino del gruppo G7 (`latino-1726-L3-P41.md`).

In coda al fascicolo c’è la **Parte B**, con i dati per le pagine interattive: la Prop. XLII (le operazioni e la soluzione, un passo per frase); le riduzioni delle osservazioni del 7 febbraio 1665 (un calcolo di trigonometria sferica che una pagina può mostrare); le quattro tabelle con i valori numerici e l’esito dei controlli; il calcolo della cometa del 1607/1682; lo Scolio generale, con un passo per frase dei primi due capoversi.

### Fonti effettivamente consultate

1. **Latino di riferimento.** Isaac Newton, *Philosophiæ Naturalis Principia Mathematica*, terza edizione, Londra, 1726, Libro III: Prop. XLII, **pp. 518–526** (la proposizione comincia a p. 518, prima del marcatore ‹519›, e finisce a p. 526); Scolio generale, **pp. 526–530** (comincia a p. 526, prima del marcatore ‹527›). Trascrizione normalizzata del Newton Project, documento **NATP00303**, estratta in testo semplice senza correzioni: `fonti/latino-1726/latino-1726-L3-P42.md` e `fonti/latino-1726/latino-1726-L3-ScholiumGenerale.md`. Nella trascrizione le tabelle sono spezzate in una cella per riga; le ho ricostruite allineandole sulle colonne del latino. La Prop. XLII non ha figure.
2. **Inglese di confronto.** *Newton’s Principia*, traduzione di Andrew Motte, New York, Daniel Adee, 1846 (Project Gutenberg n. 76404), estratti `fonti/motte-1846/motte-1846-L3-P42.md` e `fonti/motte-1846/motte-1846-L3-ScholiumGenerale.md`. Gli estratti non hanno marcatori di pagina: le pagine Motte sono indicate come «sezione corrispondente». Il LaTeX delle formule stampate come immagini viene da `fonti/motte-1846/svg_tex.tsv`.
3. **Per i rimandi e i controlli:** il latino del gruppo G7 (Prop. XLI, `latino-1726-L3-P41.md`: distanza perielia della cometa del 1680), del gruppo G1 (Regole e Fenomeni I–II: numero dei satelliti di Giove e di Saturno), del gruppo G2 (Propp. VI e XIV), del gruppo G6 (diametro apparente medio del Sole); i Fascicoli 6 (Libro I, Propp. XV, XVI, XXI) e 20 (Libro II, Sezione IX, vortici).
4. **Brief comune**, **addendum del Libro II**, **istruzioni del Libro III** e i modelli: Fascicoli 3, 5 e 20.

Non ho consultato né riprodotto traduzioni moderne. Non ho potuto vedere la stampa del 1726 né l’edizione di Motte del 1729.

### Criteri di traduzione

- Il testo guida è il latino; l’inglese di Motte serve a controllare le interpretazioni ed è annotato quando aggiunge, omette o si discosta.
- Si applicano il **glossario comune** del brief, il **glossario del Libro II** e il **glossario del Libro III** con i termini fissati dal coordinatore. In questo fascicolo ricorrono in particolare: *cometa* «cometa»; *cauda* «coda»; *trajectoria* «traiettoria»; *orbis* (orbita) «orbita»; *orbis magnus* «orbe magno»; *aphelium / perihelium* «afelio / perielio»; *perigæum* «perigeo»; *nodus ascendens* «nodo ascendente»; *inclinatio* «inclinazione»; *longitudo / latitudo* «longitudine / latitudine» (*lat. bor. / aust.* «latitudine boreale / australe»); *latus rectum* «lato retto»; *latus transversum* «lato trasverso» (§ A.0); *tempus periodicum* «tempo periodico»; *mediocris distantia* «distanza media»; *parallaxis annua* «parallasse annua»; *st. vet.* «secondo il calendario giuliano (stile vecchio)»; *gradus*, *minutum*, *secundum* «grado», «primo» (per i tempi «minuto»), «secondo»; *stellæ fixæ* «stelle fisse»; *atmosphæra* «atmosfera»; *vapor* «vapore»; *vortex* «vortice»; *ratio duplicata / sesquiplicata* «rapporto duplicato / sesquiplicato»; *specie & positione datus* «dato di forma e di posizione»; *hypothesis* «ipotesi», *hypotheses non fingo* «non invento ipotesi»; *Deus* «Dio»; *Dominus* «Signore»; *Pantocrator* in greco traslitterato; *substantia* «sostanza»; *philosophia experimentalis* «filosofia sperimentale»; *inductio* «induzione»; *qualitates occultæ* «qualità occulte»; *spiritus subtilissimus* «spirito sottilissimo»; *impetus* «impeto»; Q.E.I. «C.V.T.».
- Nomi dei pianeti e dei corpi celesti con la maiuscola anche dove il latino ha la minuscola (Sole, Luna, Terra, Venere, Giove, Saturno, Marte); *deus* è sempre minuscolo nella trascrizione: lo scrivo «Dio» quando indica il Dio di cui Newton parla, «dio» e «dèi» nei casi generici (*deus sine dominio*, *deus deorum*, *dii*), come fa Motte («God», «a god», «gods»).
- I segni zodiacali restano come simboli; la nota N1 ne dà la lettura.
- Le estensioni del glossario proprie di questo fascicolo sono elencate e motivate nel § A.0.
- Le date, le ore e le coordinate restano come nel testo (calendario giuliano; ore contate da mezzogiorno, come nell’uso astronomico). Nelle tabelle i valori sessagesimali sono scritti come nel latino, con i punti fra gradi, primi e secondi.
- Le formule algebriche della soluzione della Prop. XLII sono di Newton e restano nel testo, scritte in forma lineare; le frazioni appiattite della trascrizione («1L») sono rese con la barra (1/L). Nessuna formula moderna entra nel testo tradotto.
- Le cifre che non tornano nei calcoli e nelle tabelle **non sono corrette** nel testo: sono segnalate nell’apparato (§ A.6) e nelle note.

---

## Traduzione italiana

### Proposizione XLII. Problema XXII (correggere l’orbita trovata di una cometa)

**[III.G8.01]** **Correggere la traiettoria trovata di una cometa.**

**[III.G8.02]** *Operazione 1.* Si assuma la posizione del piano della traiettoria trovata per la proposizione precedente; e si scelgano tre luoghi della cometa determinati con osservazioni accuratissime e il più possibile distanti fra loro; e sia A il tempo fra la prima e la seconda, e B il tempo fra la seconda e la terza. Conviene poi che in uno di essi la cometa si trovi nel perigeo, o almeno non ne sia lontana. Da questi luoghi apparenti si trovino, con operazioni trigonometriche, i tre luoghi veri della cometa in quel piano assunto della traiettoria. Poi per quei luoghi trovati, intorno al centro del Sole come fuoco, si descriva una sezione conica con operazioni aritmetiche condotte per mezzo della Prop. XXI del Libro I; e le sue aree, delimitate dai raggi condotti dal Sole ai luoghi trovati, siano D ed E: cioè D l’area fra la prima e la seconda osservazione, ed E l’area fra la seconda e la terza. E sia T il tempo totale in cui l’area totale D + E deve essere descritta con la velocità della cometa trovata per la Prop. XVI del Libro I.

**[III.G8.03]** *Operazione 2.* Si aumenti la longitudine dei nodi del piano della traiettoria, aggiungendo a quella longitudine 20′ o 30′, che si chiamino P; e si mantenga l’inclinazione di quel piano sul piano dell’eclittica. Poi, dai tre luoghi osservati della cometa già detti, si trovino in questo nuovo piano tre luoghi veri, come sopra; poi anche l’orbita che passa per quei luoghi, e le due aree della medesima descritte fra le osservazioni, che siano d ed e, e anche il tempo totale t in cui l’area totale d + e dovrebbe essere descritta.

**[III.G8.04]** *Operazione 3.* Si mantenga la longitudine dei nodi dell’operazione prima, e si aumenti l’inclinazione del piano della traiettoria sul piano dell’eclittica, aggiungendo a quella inclinazione 20′ o 30′, che si chiamino Q. Poi, dai tre luoghi apparenti della cometa osservati già detti, si trovino in questo nuovo piano tre luoghi veri, e l’orbita che passa per quei luoghi, come pure le due aree della medesima descritte fra le osservazioni, che siano δ ed ε, e il tempo totale τ in cui l’area totale δ + ε dovrebbe essere descritta.

**[III.G8.05]** Ora sia C a 1 come A sta a B, e G a 1 come D sta a E, e g a 1 come d sta a e, e γ a 1 come δ sta a ε; e sia S il tempo vero fra la prima e la terza osservazione; e, badando bene ai segni + e −, si cerchino i numeri m e n con questa legge: che sia 2G − 2C = mG − mg + nG − nγ, e 2T − 2S uguale a mT − mt + nT − nτ. E se nell’operazione prima I indica l’inclinazione del piano della traiettoria sul piano dell’eclittica, e K la longitudine dell’uno o dell’altro nodo, I + nQ sarà la vera inclinazione del piano della traiettoria sul piano dell’eclittica, e K + mP la vera longitudine del nodo. E infine, se nell’operazione prima, seconda e terza le quantità R, r e ρ indicano i lati retti della traiettoria, e le quantità 1/L, 1/l, 1/λ i suoi lati trasversi, rispettivamente, R + mr − mR + nρ − nR sarà il vero lato retto, e 1/(L + ml − mL + nλ − nL) il vero lato trasverso della traiettoria che la cometa descrive. Dato poi il lato trasverso, è dato anche il tempo periodico della cometa. C.V.T.

#### Il confronto fra comete; la cometa del 1664–1665

**[III.G8.06]** Del resto, i tempi periodici delle comete che ritornano e i lati trasversi delle loro orbite non si determineranno con sufficiente accuratezza se non confrontando fra loro comete che appaiono in tempi diversi. Se si troverà che più comete, dopo intervalli di tempo uguali, hanno descritto la stessa orbita, si dovrà concludere che tutte queste sono una sola e medesima cometa, che ruota nella medesima orbita. E soltanto allora dai tempi delle rivoluzioni saranno dati i lati trasversi delle orbite, e da questi lati si determineranno le orbite ellittiche.

**[III.G8.07]** A questo fine si devono dunque calcolare le traiettorie di più comete, nell’ipotesi che siano paraboliche. Traiettorie di questo genere, infatti, concorderanno sempre con i fenomeni con ottima approssimazione. Ciò risulta chiaro non soltanto dalla traiettoria parabolica della cometa dell’anno 1680, che ho confrontato sopra con le osservazioni, ma anche da quella della cometa insigne che apparve negli anni 1664 e 1665 e fu osservata da Hevelius. Egli dalle sue osservazioni calcolò le longitudini e le latitudini di questa cometa, ma con minore accuratezza. Dalle stesse osservazioni il nostro Halley calcolò di nuovo i luoghi di questa cometa, e soltanto allora, dai luoghi così trovati, determinò la traiettoria della cometa. Trovò dunque il suo nodo ascendente in ♊ 21° 13′ 55″; l’inclinazione dell’orbita sul piano dell’eclittica 21° 18′ 40″; la distanza del perielio dal nodo, misurata nell’orbita, 49° 27′ 30″; il perielio in ♌ 8° 40′ 30″, con latitudine eliocentrica australe 16° 1′ 45″; la cometa nel perielio il 24 novembre alle 11h 52′ pomeridiane, in tempo uguagliato, a Londra, ossia alle 13h 8′ a Danzica, secondo il calendario giuliano; e il lato retto della parabola 410286, essendo la distanza media della Terra dal Sole 100000. Quanto bene i luoghi della cometa calcolati in questa orbita concordino con le osservazioni, risulterà dalla tabella seguente, calcolata da Halley.

**[III.G8.08]** *Tabella della cometa del 1664–1665.*

| Tempo apparente a Danzica, st. vet. (d, h, ′) | Distanze osservate della cometa | (° ′ ″) | Luoghi osservati | (° ′ ″) | Luoghi calcolati nell’orbita (° ′ ″) |
|---|---|---|---|---|---|
| Dic. 3d 18h 29½′ | dal Cuore del Leone | 46.24.20 | Long. ♎ | 7.1.0 | ♎ 7.1.29 |
| | dalla Spiga della Vergine | 22.52.10 | Lat. austr. | 21.39.0 | 21.38.50 |
| 4d 18h 1½′ | dal Cuore del Leone | 46.2.45 | Long. ♎ | 6.15.0 | ♎ 6.16.5 |
| | dalla Spiga della Vergine | 23.52.40 | Lat. austr. | 22.24.0 | 22.24.0 |
| 7d 17h 48½′ | dal Cuore del Leone | 44.48.0 | Long. ♎ | 3.6.0 | ♎ 3.7.33 |
| | dalla Spiga della Vergine | 27.56.40 | Lat. austr. | 25.22.0 | 25.21.40 |
| 17d 14h 43½′ | dal Cuore del Leone | 53.15.15 | Long. ♌ | 2.56.0 | ♌ 2.56.0 |
| | dalla spalla destra di Orione | 45.43.30 | Lat. austr. | 49.25.0 | 49.25.0 |
| 19d 9h 25½′ | da Procione | 35.13.50 | Long. ♊ | 28.40.30 | ♊ 28.43.0 |
| | dalla lucida della mascella della Balena | 52.56.0 | Lat. austr. | 45.48.0 | 45.46.0 |
| 20d 9h 53½′ | da Procione | 40.49.0 | Long. ♊ | 13.3.0 | ♊ 13.5.0 |
| | dalla lucida della mascella della Balena | 40.4.0 | Lat. austr. | 39.54.0 | 39.53.0 |
| 21d 9h 9½′ | dalla spalla destra di Orione | 26.21.25 | Long. ♊ | 2.16.0 | ♊ 2.18.30 |
| | dalla lucida della mascella della Balena | 29.28.0 | Lat. austr. | 33.41.0 | 33.39.40 |
| 22d 9h 0½′ | dalla spalla destra di Orione | 29.47.0 | Long. ♉ | 24.24.0 | ♉ 24.27.0 |
| | dalla lucida della mascella della Balena | 20.29.30 | Lat. austr. | 27.45.0 | 27.46.0 |
| 26d 7h 58½′ | dalla lucida dell’Ariete | 23.20.0 | Long. ♉ | 9.0.0 | ♉ 9.2.28 |
| | da Aldebaran | 26.44.0 | Lat. austr. | 12.36.0 | 12.34.13 |
| 27d 6h 45′ [trascr. «45⁤01′»] | dalla lucida dell’Ariete | 20.45.0 | Long. ♉ | 7.5.40 | ♉ 7.8.54 |
| | da Aldebaran | 28.10.0 | Lat. austr. | 10.23.0 | 10.23.13 |
| 28d 7h 39½′ | dalla lucida dell’Ariete | 18.29.0 | Long. ♉ | 5.24.45 | ♉ 5.27.52 |
| | dal Palilicio | 29.37.0 | Lat. austr. | 8.22.50 | 8.23.37 |
| 31d 6h 45½′ | dalla cintura di Andromeda | 30.48.10 | Long. ♉ | 2.7.40 | ♉ 2.8.20 |
| | dal Palilicio | 32.53.30 | Lat. austr. | 4.13.0 | 4.16.25 |
| Gen. 1665, 7d 7h 37½′ | dalla cintura di Andromeda | 25.11.0 | Long. ♈ | 28.24.47 | ♈ 28.24.0 |
| | dal Palilicio | 37.12.25 | Lat. bor. | 0.54.0 | 0.53.0 |
| 13d 7h 0½′ | dalla testa di Andromeda | 28.7.10 | Long. ♈ | 27.6.54 | ♈ 27.6.39 |
| | dal Palilicio | 38.55.20 | Lat. bor. | 3.6.50 | 3.7.40 |
| 24d 7h 29½′ | dalla cintura di Andromeda | 20.32.15 | Long. ♈ | 26.29.15 | ♈ 26.28.50 |
| | dal Palilicio | 40.5.0 | Lat. bor. | 5.25.50 | 5.26.0 |
| Feb. 7d 8h 37½′ |  |  | Long. ♈ | 27.4.46 | ♈ 27.24.55 |
| |  |  | Lat. bor. | 7.3.25 | 7.3.15 |
| 22d 8h 46½′ |  |  | Long. ♈ | 28.29.46 | ♈ 28.29.58 |
| |  |  | Lat. bor. | 8.12.36 | 8.10.25 |
| Mar. 1d 8h 16½′ |  |  | Long. ♈ | 29.18.15 | ♈ 29.18.20 |
| |  |  | Lat. bor. | 8.36.26 | 8.36.12 |
| 7d 8h 37½′ |  |  | Long. ♉ | 0.2.48 | ♉ 0.2.42 |
| |  |  | Lat. bor. | 8.56.30 | 8.56.56 |

**[III.G8.09]** Nel mese di febbraio dell’anno 1665 appena cominciato, la prima stella dell’Ariete, che nel seguito chiamerò γ, era in ♈ 28° 30′ 15″ con latitudine boreale 7° 8′ 58″. La seconda dell’Ariete era in ♈ 29° 17′ 18″ con latitudine boreale 8° 28′ 16″. E un’altra stella di settima grandezza, che chiamerò A, era in ♈ 28° 24′ 45″ con latitudine boreale 8° 28′ 33″. La cometa poi, il 7 febbraio alle 7h 30′ a Parigi (cioè il 7 febbraio alle 8h 37′ a Danzica), secondo il calendario giuliano, formava con quelle stelle γ e A un triangolo rettangolo in γ. E la distanza della cometa dalla stella γ era uguale alla distanza delle stelle γ e A, cioè 1° 19′ 46″ su un cerchio massimo, e perciò era 1° 20′ 26″ nel parallelo della latitudine della stella γ. Perciò, se dalla longitudine della stella γ si sottrae la longitudine 1° 20′ 26″, resterà la longitudine della cometa ♈ 27° 9′ 49″. Auzout, da questa sua osservazione, pose la cometa in ♈ 27° 0′ circa. E secondo lo schema con cui Hooke ne disegnò il moto, essa era allora in ♈ 26° 59′ 24″. Prendendo un valore medio, io l’ho posta in ♈ 27° 4′ 46″. Dalla stessa osservazione Auzout pose la latitudine della cometa a 7° e 4′ o 5′ verso nord. Più correttamente l’avrebbe posta a 7° 3′ 29″, essendo cioè la differenza delle latitudini della cometa e della stella γ uguale alla differenza delle longitudini delle stelle γ e A.

**[III.G8.10]** Il 22 febbraio alle 7h 30′ a Londra, cioè il 22 febbraio alle 8h 46′ a Danzica, la distanza della cometa dalla stella A, secondo l’osservazione di Hooke disegnata da lui stesso in uno schema, come pure secondo le osservazioni di Auzout disegnate in uno schema da Petit, era la quinta parte della distanza fra la stella A e la prima dell’Ariete, ossia 15′ 57″. E la distanza della cometa dalla linea che congiunge la stella A e la prima dell’Ariete era la quarta parte di quella stessa quinta parte, cioè 4′. Perciò la cometa era in ♈ 28° 29′ 46″, con latitudine boreale 8° 12′ 36″.

**[III.G8.11]** Il 1° marzo alle 7h 0′ a Londra, cioè il 1° marzo alle 8h 16′ a Danzica, la cometa fu osservata vicino alla seconda dell’Ariete; e la distanza fra le due stava alla distanza fra la prima e la seconda dell’Ariete, cioè a 1° 33′, come 4 a 45 secondo Hooke, o come 2 a 23 secondo Gottignies. Di qui la distanza della cometa dalla seconda dell’Ariete era 8′ 16″ secondo Hooke, o 8′ 5″ secondo Gottignies, o, prendendo un valore medio, 8′ 10″. Secondo Gottignies, poi, la cometa aveva appena oltrepassato la seconda dell’Ariete di circa la quarta o la quinta parte del cammino compiuto in un giorno, cioè di circa 1′ 35″ (e con lui concorda abbastanza Auzout), o di poco meno secondo Hooke, diciamo 1′. Perciò, se alla longitudine della prima dell’Ariete si aggiunge 1′, e alla sua latitudine 8′ 10″, si avrà la longitudine della cometa ♈ 29° 18′ e la latitudine boreale 8° 36′ 26″.

**[III.G8.12]** Il 7 marzo alle 7h 30′ a Parigi (cioè il 7 marzo alle 8h 37′ a Danzica), dalle osservazioni di Auzout, la distanza della cometa dalla seconda dell’Ariete era uguale alla distanza della seconda dell’Ariete dalla stella A, cioè 52′ 29″. E la differenza delle longitudini della cometa e della seconda dell’Ariete era 45′ o 46′, o, prendendo un valore medio, 45′ 30″. Perciò la cometa era in ♉ 0° 2′ 48″. Dallo schema delle osservazioni di Auzout costruito da Petit, Hevelius dedusse la latitudine della cometa 8° 54′. Ma l’incisore incurvò irregolarmente il cammino della cometa verso la fine del suo moto, e Hevelius, nello schema delle osservazioni di Auzout costruito da lui stesso, corresse la curvatura irregolare, e così fece la latitudine della cometa di 8° 55′ 30″. E correggendo un poco di più l’irregolarità, la latitudine può risultare di 8° 56′ o di 8° 57′.

**[III.G8.13]** Questa cometa fu vista anche il 9 marzo, e allora doveva trovarsi in ♉ 0° 18′, con latitudine boreale di 9° 3½′ circa.

**[III.G8.14]** Questa cometa apparve per tre mesi, percorse quasi sei segni, e in un giorno compì quasi venti gradi. Il suo corso deviò moltissimo da un cerchio massimo, incurvato verso nord; e il suo moto, verso la fine, da retrogrado divenne diretto. E nonostante un corso così insolito, la teoria dal principio alla fine concorda con le osservazioni non meno accuratamente di quanto le teorie dei pianeti sogliono concordare con le loro osservazioni, come risulterà a chi guardi la tabella. Si devono però sottrarre circa due primi dove la cometa fu velocissima; il che si otterrà togliendo dodici secondi dall’angolo fra il nodo ascendente e il perielio, ossia ponendo quell’angolo di 49° 27′ 18″. La parallasse annua di entrambe le comete (sia di questa sia della precedente) fu notevole, e di qui si dimostra il moto annuo della Terra nell’orbe magno.

#### Le comete del 1683, del 1682 e del 1723

**[III.G8.15]** La teoria è confermata anche dal moto della cometa che apparve nell’anno 1683. Questa fu retrograda in un’orbita il cui piano formava con il piano dell’eclittica un angolo quasi retto. Il suo nodo ascendente (secondo il calcolo di Halley) era in ♍ 23° 23′; l’inclinazione dell’orbita sull’eclittica 83° 11′; il perielio in ♊ 25° 29′ 30″; la distanza perielia dal Sole 56020, essendo il raggio dell’orbe magno 100000; e il tempo del perielio il 2 luglio, 3h 50′. I luoghi della cometa calcolati da Halley in questa orbita e confrontati con i luoghi osservati da Flamsteed sono esposti nella tabella seguente.

**[III.G8.16]** *Tabella della cometa del 1683.*

| 1683, tempo uguagliato (d, h, ′) | Luogo del Sole (° ′ ″) | Long. della cometa calcolata (° ′ ″) | Lat. bor. calcolata (° ′ ″) | Long. della cometa osservata (° ′ ″) | Lat. bor. osservata (° ′ ″) | Diff. long. (′ ″) | Diff. lat. (′ ″) |
|---|---|---|---|---|---|---|---|
| Lug. 13.12.55 | ♌ 1.2.30 | ♋ 13.5.42 | 29.28.13 | ♋ 13.6.42 | 29.28.20 | +1.0 | +0.7 |
| 15.11.15 | 2.53.12 | 11.37.48 | 29.34.0 | 11.39.43 | 29.34.50 | +1.55 | +0.50 |
| 17.10.20 | 4.45.45 | 10.7.6 | 29.33.30 | 10.8.40 | 29.34.0 | +1.34 | +0.30 |
| 23.13.40 | 10.38.21 | 5.10.27 | 28.51.42 | 5.11.30 | 28.50.28 | +1.3 | −1.14 |
| 25.14.5 | 12.35.28 | 3.27.53 | 24.24.47 | 3.27.0 | 28.23.40 | −0.53 | −1.7 |
| 31.9.42 | 18.9.22 | ♊ 27.55.3 | 26.22.52 | ♊ 27.54.24 | 26.22.25 | −0.39 | −0.27 |
| 31.14.55 | 18.21.53 | 27.41.7 | 26.16.57 | 27.41.8 | 26.14.50 | +0.1 | −2.7 |
| Ago. 2.14.56 | 20.17.16 | 25.29.32 | 25.16.19 | 25.28.46 | 25.17.28 | −0.46 | +1.9 |
| 4.10.49 | 22.2.50 | 23.18.20 | 24.10.49 | 23.16.55 | 24.12.19 | −1.25 | +1.30 |
| 6.10.9 | 23.56.45 | 20.42.23 | 22.47.5 | 20.40.32 | 22.49.5 | −1.51 | +2.0 |
| 9.10.26 | 26.50.52 | 16.7.57 | 20.6.37 | 16.5.55 | 20.6.10 | −2.2 | −0.27 |
| 15.14.1 | ♍ 2.47.13 | 3.30.48 | 11.37.33 | 3.26.18 | 11.32.1 | −4.30 | −5.32 |
| 16.15.10 | 3.48.2 | 0.43.7 | 9.34.16 | 0.41.55 | 9.34.13 | −1.12 | −0.3 |
| 18.15.44 | 5.45.33 | ♉ 24.52.53 | 5.11.15 | ♉ 24.49.5 | 5.9.11 | −3.48 | −2.4 |
|  |  |  | *austr.* |  | *austr.* |  |  |
| 22.14.44 | 9.35.49 | 11.7.14 | 5.16.53 | 11.7.12 | 5.16.50 | −0.2 | −0.3 |
| 23.15.52 | 10.36.48 | 7.2.18 | 8.17.9 | 7.1.17 | 8.16.41 | −1.1 | −0.28 |
| 26.16.2 | 13.31.10 | ♈ 24.45.31 | 16.38.0 | ♈ 24.44.0 | 16.38.20 | −1.31 | +0.20 |

**[III.G8.17]** La teoria è confermata anche dal moto della cometa retrograda che apparve nell’anno 1682. Il suo nodo ascendente (secondo il calcolo di Halley) era in ♉ 21° 16′ 30″. L’inclinazione dell’orbita sul piano dell’eclittica 17° 56′ 0″. Il perielio in ♒ 2° 52′ 50″. La distanza perielia dal Sole 58328, essendo il raggio dell’orbe magno 100000. E il tempo uguagliato del perielio il 4 settembre, 7h 39′. I luoghi calcolati dalle osservazioni di Flamsteed e confrontati con i luoghi calcolati con la teoria sono esposti nella tabella seguente.

**[III.G8.18]** *Tabella della cometa del 1682.*

| 1682, tempo apparente (d, h, ′) | Luogo del Sole (° ′ ″) | Long. della cometa calcolata (° ′ ″) | Lat. bor. calcolata (° ′ ″) | Long. della cometa osservata (° ′ ″) | Lat. bor. osservata (° ′ ″) | Diff. long. (′ ″) | Diff. lat. (′ ″) |
|---|---|---|---|---|---|---|---|
| Ago. 19.16.38 | ♍ 7.0.7 | ♌ 18.14.28 | 25.50.7 | ♌ 18.14.40 | 25.49.55 | −0.12 | +0.12 |
| 20.15.38 | 7.55.52 | 24.46.23 | 26.14.42 | 24.46.22 | 26.12.52 | +0.1 | +1.50 |
| 21.8.21 | 8.36.14 | 29.37.15 | 26.20.3 | 29.38.2 | 26.17.37 | −0.47 | +2.26 |
| 22.8.8 | 9.33.55 | ♍ 6.29.53 | 26.8.42 | ♍ 6.30.3 | 26.7.12 | −0.10 | +1.30 |
| 29.8.20 | 16.22.40 | ♎ 12.37.54 | 18.37.47 | ♎ 12.37.49 | 18.34.5 | +0.5 | +3.42 |
| 30.7.45 | 17.19.41 | 15.36.1 | 17.26.43 | 15.35.18 | 17.27.17 | +0.43 | −0.34 |
| Set. 1.7.33 | 19.16.9 | 20.30.53 | 15.13.0 | 20.27.4 | 15.9.49 | +3.49 | +3.11 |
| 4.7.22 | 22.11.28 | 25.42.0 | 12.23.48 | 25.40.58 | 12.22.0 | +1.2 | +1.48 |
| 5.7.32 | 23.10.29 | 27.0.46 | 11.33.8 | 26.59.24 | 11.33.51 | +1.22 | −0.43 |
| 8.7.16 | 26.5.58 | 29.58.44 | 9.26.46 | 29.58.45 | 9.26.43 | −0.1 | +0.3 |
| 9.7.26 | 27.5.9 | ♏ 0.44.10 | 8.49.10 | ♏ 0.44.4 | 8.48.25 | +0.6 | +0.45 |

**[III.G8.19]** La teoria è confermata anche dal moto retrogrado della cometa che apparve nell’anno 1723. Il suo nodo ascendente (secondo il calcolo del signor Bradley, professore saviliano di astronomia a Oxford) era in ♈ 14° 16′. L’inclinazione dell’orbita sul piano dell’eclittica 49° 59′. Il perielio in ♉ 12° 15′ 20″. La distanza perielia dal Sole 998651, essendo il raggio dell’orbe magno 1000000; e il tempo uguagliato del perielio il 16 settembre, 16h 10′. I luoghi della cometa calcolati da Bradley in questa orbita e confrontati con i luoghi osservati da lui stesso, da suo zio, il signor Pound, e dal signor Halley sono esposti nella tabella seguente.

**[III.G8.20]** *Tabella della cometa del 1723.*

| 1723, tempo uguagliato (d, h, ′) | Long. della cometa osservata (° ′ ″) | Lat. bor. osservata (° ′ ″) | Long. della cometa calcolata (° ′ ″) | Lat. bor. calcolata (° ′ ″) | Diff. long. (″) | Diff. lat. (″) |
|---|---|---|---|---|---|---|
| Ott. 9.8.5 | ♒ 7.22.15 | 5.2.0 | ♒ 7.21.26 | 5.2.47 | +49 | −47 |
| 10.6.21 | 6.41.12 | 7.44.13 | 6.41.42 | 7.43.18 | −50 | +55 |
| 12.7.22 | 5.39.58 | 11.55.0 | 5.40.19 | 11.54.55 | −21 | +5 |
| 14.8.57 | 4.59.49 | 14.43.50 | 5.0.37 | 14.44.1 | −48 | −11 |
| 15.6.35 | 4.47.41 | 15.40.51 | 4.47.45 | 15.40.55 | −4 | −4 |
| 21.6.22 | 4.2.32 | 19.41.49 | 4.2.21 | 19.42.3 | +11 | −14 |
| 22.6.24 | 3.59.2 | 20.8.12 | 3.59.10 | 20.8.17 | −8 | −5 |
| 24.8.2 | 3.55.29 | 20.55.18 | 3.55.11 | 20.55.9 | +18 | +9 |
| 29.8.56 | 3.56.17 | 22.20.27 | 3.56.42 | 22.20.10 | −25 | +17 |
| 30.6.20 | 3.58.9 | 22.32.28 | 3.58.17 | 22.32.12 | −8 | +16 |
| Nov. 5.5.53 | 4.16.30 | 23.38.33 | 4.16.23 | 23.38.7 | +7 | +26 |
| 8.7.6 | 4.29.36 | 24.4.30 | 4.29.34 | 24.4.40 | −18 | −10 |
| 14.6.20 | 5.2.16 | 24.48.46 | 5.2.21 | 24.48.16 | −35 | +30 |
| 20.7.45 | 5.42.20 | 25.24.45 | 5.43.13 | 25.25.17 | −53 | −32 |
| Dic. 7.6.45 | 8.4.13 | 26.54.18 | 8.3.55 | 26.53.42 | +18 | +36 |

#### Che cosa insegnano gli esempi; la cometa del 1607 e il ritorno dopo 75 anni

**[III.G8.21]** Da questi esempi è manifesto, più che a sufficienza, che i moti delle comete sono rappresentati dalla teoria da noi esposta non meno accuratamente di quanto i moti dei pianeti lo siano di solito dalle loro teorie. E perciò con questa teoria si possono enumerare le orbite delle comete, e si può infine conoscere il tempo periodico di una cometa che ruota in un’orbita qualsiasi; e soltanto allora si conosceranno i lati trasversi delle orbite ellittiche e le altezze degli afeli.

**[III.G8.22]** La cometa retrograda che apparve nell’anno 1607 descrisse un’orbita il cui nodo ascendente (secondo il calcolo di Halley) era in ♉ 20° 21′; l’inclinazione del piano dell’orbita sul piano dell’eclittica era 17° 2′; il perielio era in ♒ 2° 16′; e la distanza perielia dal Sole era 58680, essendo il raggio dell’orbe magno 100000. E la cometa era nel perielio il 16 ottobre, 3h 50′. Questa orbita concorda con ottima approssimazione con l’orbita della cometa che apparve nell’anno 1682. Se queste due comete sono state una sola e medesima, questa cometa ruoterà nello spazio di 75 anni, e l’asse maggiore della sua orbita starà all’asse maggiore dell’orbe magno come la radice cubica di 75 × 75 sta a 1, ossia circa come 1778 a 100. E la distanza afelia di questa cometa dal Sole starà alla distanza media della Terra dal Sole circa come 35 a 1. Conosciute queste cose, non sarà difficile determinare l’orbita ellittica di questa cometa. E così staranno le cose se la cometa, nello spazio di settantacinque anni, ritornerà in seguito in questa orbita. Le altre comete sembrano ruotare in un tempo maggiore e salire più in alto.

#### Perturbazioni reciproche; perché le comete non stanno nello zodiaco

**[III.G8.23]** Del resto le comete, per il loro grande numero, per la grande distanza degli afeli dal Sole e per la lunga permanenza negli afeli, devono essere alquanto perturbate dalle gravità reciproche, e le loro eccentricità e i tempi delle rivoluzioni devono ora aumentare un poco, ora diminuire. Perciò non ci si deve aspettare che la stessa cometa ritorni esattamente nella stessa orbita e con gli stessi tempi periodici. Basta che non si presentino cambiamenti maggiori di quelli che nascono dalle cause dette.

**[III.G8.24]** E di qui si rende ragione del perché le comete non siano comprese nello zodiaco alla maniera dei pianeti, ma ne escano e siano portate con moti vari in tutte le regioni dei cieli: cioè a questo fine, che nei loro afeli, dove si muovono lentissimamente, distino il più possibile l’una dall’altra e si attraggano a vicenda il meno possibile. Per questa causa le comete che scendono più in basso, e perciò si muovono lentissimamente negli afeli, devono salire più in alto.

#### Comete che cadono nel Sole; stelle nuove e stelle variabili; i vapori

**[III.G8.25]** La cometa che apparve nell’anno 1680 distava dal Sole, nel suo perielio, meno della sesta parte del diametro del Sole; e per la grandissima velocità in quella vicinanza e per una certa densità dell’atmosfera del Sole, dovette sentire una qualche resistenza, ed essere un poco ritardata, e avvicinarsi di più al Sole; e, avvicinandosi al Sole a ogni rivoluzione, cadrà infine nel corpo del Sole. Ma anche nell’afelio, dove si muove lentissimamente, può talvolta essere ritardata dall’attrazione di altre comete, e quindi cadere nel Sole. Così anche le stelle fisse, che a poco a poco si consumano in luce e vapori, possono essere ristorate dalle comete che cadono in esse e, accese da nuovo alimento, essere prese per stelle nuove. Di questo genere sono le stelle fisse che appaiono all’improvviso, al principio splendono moltissimo e poi a poco a poco svaniscono.

**[III.G8.26]** Tale fu la stella nella sedia di Cassiopea che Cornelius Gemma, l’8 novembre 1572, esplorando quella parte del cielo in una notte serena, non vide affatto; ma la notte seguente (9 novembre) la vide più splendente di tutte le fisse, e per luce poco inferiore a Venere. Tycho Brahe la vide l’11 dello stesso mese, quando splendeva al massimo; e da quel tempo la osservò decrescere a poco a poco e svanire nello spazio di sedici mesi. Nel mese di novembre, quando apparve per la prima volta, uguagliava Venere per luce. Nel mese di dicembre, un poco diminuita, sembrava uguagliare Giove. Nell’anno 1573, nel mese di gennaio, era minore di Giove e maggiore di Sirio, al quale divenne uguale alla fine di febbraio e al principio di marzo. Nei mesi di aprile e maggio sembrava uguale alle stelle di seconda grandezza; in giugno, luglio e agosto alle stelle di terza grandezza; in settembre, ottobre e novembre alle stelle di quarta; in dicembre e nel gennaio dell’anno 1574 alle stelle di quinta; e nel mese di febbraio alle stelle di sesta grandezza; e nel mese di marzo scomparve alla vista. Il suo colore fu al principio chiaro, biancheggiante e splendente, poi giallo, e nel mese di marzo dell’anno 1573 rosseggiante come Marte o la stella Aldebaran; in maggio poi assunse una bianchezza un po’ livida, quale vediamo in Saturno, e conservò quel colore fino alla fine, divenendo però sempre più oscura.

**[III.G8.27]** Tale fu anche la stella nel piede destro del Serpentario, che i discepoli di Keplero osservarono cominciare ad apparire il 30 settembre 1604, secondo il calendario giuliano, e superare per luce la stella di Giove, mentre la notte precedente non era apparsa affatto. Da quel tempo poi decrebbe a poco a poco, e nello spazio di quindici o sedici mesi scomparve alla vista. Si dice che da una tale stella nuova, splendente oltre misura, Ipparco sia stato spinto a osservare le fisse e a registrarle in un catalogo.

**[III.G8.28]** Ma le fisse che appaiono e svaniscono alternativamente, che crescono a poco a poco e per luce non superano quasi mai le fisse di terza grandezza, sembrano essere di un altro genere e, ruotando, mostrare alternativamente una parte luminosa e una parte oscura. I vapori, poi, che nascono dal Sole, dalle stelle fisse e dalle code delle comete possono cadere per la loro gravità nelle atmosfere dei pianeti, e lì condensarsi e convertirsi in acqua e in spiriti umidi, e poi, per un calore lento, passare a poco a poco in sali, zolfi, tinture, limo, fango, argilla, sabbia, pietre, coralli e altre sostanze terrestri.

### Scolio generale

#### 1. Contro i vortici

**[III.G9.01]** L’ipotesi dei vortici è gravata da molte difficoltà. Perché ogni pianeta, con il raggio condotto al Sole, descriva aree proporzionali al tempo, i tempi periodici delle parti del vortice dovrebbero essere in rapporto duplicato delle distanze dal Sole. Perché i tempi periodici dei pianeti siano nella proporzione sesquiplicata delle distanze dal Sole, i tempi periodici delle parti del vortice dovrebbero essere nella proporzione sesquiplicata delle distanze. Perché i vortici minori fatti girare attorno a Saturno, a Giove e agli altri pianeti si conservino e nuotino tranquillamente nel vortice del Sole, i tempi periodici delle parti del vortice solare dovrebbero essere uguali. Le rivoluzioni del Sole e dei pianeti attorno ai propri assi, che dovrebbero accordarsi con i moti dei vortici, si discostano da tutte queste proporzioni. I moti delle comete sono sommamente regolari, osservano le stesse leggi dei moti dei pianeti, e non possono essere spiegati per mezzo dei vortici. Le comete sono portate con moti molto eccentrici in tutte le parti dei cieli, il che non può avvenire se non si tolgono i vortici.

#### 2. I moti negli spazi liberi

**[III.G9.02]** I proiettili, nella nostra aria, sentono soltanto la resistenza dell’aria. Tolta l’aria, come avviene nel vuoto di Boyle, la resistenza cessa, poiché una piuma sottile e dell’oro massiccio cadono in questo vuoto con velocità uguale. E lo stesso ragionamento vale per gli spazi celesti, che sono al di sopra dell’atmosfera della Terra. Tutti i corpi devono muoversi in questi spazi con la massima libertà; e perciò i pianeti e le comete devono ruotare perpetuamente in orbite date di forma e di posizione secondo le leggi esposte sopra. Persevereranno certo nelle loro orbite per le leggi della gravità, ma la posizione regolare delle orbite non poterono affatto acquistarla in origine per queste leggi.

#### 3. L’ordine del sistema e l’ente intelligente

**[III.G9.03]** I sei pianeti principali ruotano attorno al Sole in cerchi concentrici al Sole, con la stessa direzione del moto, con ottima approssimazione nello stesso piano. Dieci lune ruotano attorno alla Terra, a Giove e a Saturno in cerchi concentrici, con la stessa direzione del moto, con ottima approssimazione nei piani delle orbite dei pianeti. E tutti questi moti regolari non hanno origine da cause meccaniche, poiché le comete sono portate liberamente in orbite molto eccentriche e in tutte le parti dei cieli. Con questo genere di moto le comete attraversano le orbite dei pianeti con grandissima velocità e grandissima facilità, e nei loro afeli, dove sono più lente e si trattengono più a lungo, distano il più possibile l’una dall’altra, così da attrarsi a vicenda il meno possibile. Questa elegantissima compagine del Sole, dei pianeti e delle comete non poté nascere se non dal disegno e dal dominio di un ente intelligente e potente. E se le stelle fisse sono centri di sistemi simili, tutti questi, costruiti secondo un simile disegno, saranno soggetti al dominio di Uno solo: tanto più che la luce delle fisse è della stessa natura della luce del Sole, e tutti i sistemi mandano luce gli uni negli altri. E perché i sistemi delle fisse non cadano gli uni sugli altri per la loro gravità, egli li ha posti a un’immensa distanza l’uno dall’altro.

#### 4. Dio e il suo dominio

**[III.G9.04]** Egli governa tutte le cose non come anima del mondo, ma come Signore dell’universo. E per il suo dominio suole essere chiamato Signore Dio *Pantocrator* (Παντοκράτωρ)[1]. Infatti «Dio» è una parola relativa e si riferisce ai servi; e la deità è la dominazione di Dio non su un corpo proprio, come pensano coloro per i quali Dio è l’anima del mondo, ma sui servi. Il Dio sommo è un ente eterno, infinito, assolutamente perfetto; ma un ente, per quanto perfetto, senza dominio non è Signore Dio. Diciamo infatti «Dio mio», «Dio vostro», «Dio d’Israele», «Dio degli dèi» e «Signore dei signori»; ma non diciamo «Eterno mio», «Eterno vostro», «Eterno d’Israele», «Eterno degli dèi»; non diciamo «Infinito mio» o «Perfetto mio». Queste denominazioni non hanno relazione con i servi.

**[III.G9.05]** La parola «Dio» significa comunemente[2] «signore»; ma non ogni signore è Dio. È la dominazione di un ente spirituale che costituisce Dio: una dominazione vera un Dio vero, una somma un Dio sommo, una finta un Dio finto. E dalla dominazione vera segue che il vero Dio è vivente, intelligente e potente; dalle altre perfezioni, che è sommo, ossia sommamente perfetto.

#### 5. Eternità, onnipresenza, durata e spazio

**[III.G9.06]** È eterno e infinito, onnipotente e onnisciente, cioè dura dall’eternità all’eternità ed è presente dall’infinito all’infinito: governa tutte le cose, e conosce tutte le cose che avvengono o possono avvenire. Non è l’eternità e l’infinità, ma è eterno e infinito; non è la durata e lo spazio, ma dura ed è presente. Dura sempre ed è presente ovunque, ed esistendo sempre e ovunque costituisce la durata e lo spazio. Poiché ogni particella dello spazio è sempre, e ogni momento indivisibile della durata è ovunque, certamente del fabbricatore e signore di tutte le cose non si potrà dire che non è mai e che non è in nessun luogo. Ogni anima che sente, in tempi diversi e in diversi organi dei sensi e dei moti, è la stessa persona indivisibile. Si danno parti successive nella durata e coesistenti nello spazio, ma né le une né le altre nella persona dell’uomo, ossia nel suo principio pensante; e molto meno nella sostanza pensante di Dio. Ogni uomo, in quanto cosa che sente, è uno e il medesimo uomo durante la sua vita, in tutti e in ciascuno degli organi dei sensi. Dio è uno e il medesimo Dio sempre e ovunque.

**[III.G9.07]** È onnipresente non per sola virtù, ma anche per sostanza: la virtù, infatti, non può sussistere senza sostanza. In lui[3] sono contenute e si muovono tutte le cose, ma senza che l’uno patisca dall’altro. Dio non patisce nulla dai moti dei corpi; questi non sentono alcuna resistenza dall’onnipresenza di Dio. Che il Dio sommo esista necessariamente è ammesso da tutti; e con la stessa necessità è sempre e ovunque. Di qui anche è tutto simile a sé, tutto occhio, tutto orecchio, tutto cervello, tutto braccio, tutto forza di sentire, di intendere e di agire, ma in un modo per nulla umano, in un modo per nulla corporeo, in un modo a noi del tutto sconosciuto.

#### 6. Che cosa possiamo conoscere di Dio

**[III.G9.08]** Come un cieco non ha idea dei colori, così noi non abbiamo idea dei modi in cui il sapientissimo Dio sente e intende tutte le cose. È del tutto privo di ogni corpo e di ogni figura corporea, e perciò non può essere visto, né udito, né toccato, né deve essere adorato sotto l’aspetto di qualche cosa corporea. Abbiamo idee dei suoi attributi, ma che cosa sia la sostanza di una cosa qualsiasi non lo conosciamo affatto. Vediamo soltanto le figure e i colori dei corpi, udiamo soltanto i suoni, tocchiamo soltanto le superfici esterne, odoriamo soltanto gli odori e gustiamo i sapori; le sostanze intime non le conosciamo con nessun senso, con nessun atto riflesso; e molto meno abbiamo idea della sostanza di Dio.

**[III.G9.09]** Lo conosciamo soltanto per le sue proprietà e i suoi attributi, e per le sapientissime e ottime strutture delle cose e per le cause finali; e lo ammiriamo per le perfezioni, ma lo veneriamo e lo adoriamo per il dominio. Lo adoriamo infatti come servi; e un dio senza dominio, provvidenza e cause finali non è altro che fato e natura. Da una cieca necessità metafisica, che è certamente la stessa sempre e ovunque, non nasce alcuna variazione delle cose. Tutta la diversità delle cose create secondo i luoghi e i tempi non poté nascere se non dalle idee e dalla volontà di un ente che esiste necessariamente. Per allegoria, poi, si dice che Dio vede, ode, parla, ride, ama, odia, desidera, dà, riceve, gode, si adira, combatte, fabbrica, fonda, costruisce. Ogni discorso su Dio, infatti, è tratto dalle cose umane per una certa somiglianza, non perfetta certo, ma tuttavia una somiglianza di qualche genere. E questo basti su Dio; del quale discorrere a partire dai fenomeni appartiene certamente alla filosofia naturale.

#### 7. La causa della gravità: «non invento ipotesi»

**[III.G9.10]** Finora ho esposto i fenomeni dei cieli e del nostro mare per mezzo della forza di gravità, ma non ho ancora assegnato la causa della gravità. Certo questa forza nasce da una qualche causa che penetra fino ai centri del Sole e dei pianeti senza diminuzione della sua virtù; che agisce non secondo la quantità delle superfici delle particelle su cui agisce (come sogliono le cause meccaniche), ma secondo la quantità di materia solida; e la cui azione si estende da ogni parte a distanze immense, decrescendo sempre in rapporto duplicato delle distanze. La gravità verso il Sole si compone delle gravità verso le singole particelle del Sole, e allontanandosi dal Sole decresce esattamente in rapporto duplicato delle distanze fino all’orbita di Saturno, come è manifesto dalla quiete degli afeli dei pianeti, e fino agli ultimi afeli delle comete, se pure quegli afeli sono in quiete. Ma la ragione di queste proprietà della gravità non ho ancora potuto dedurla dai fenomeni, e non invento ipotesi. Tutto ciò che non si deduce dai fenomeni, infatti, va chiamato ipotesi; e le ipotesi, siano metafisiche o fisiche, siano di qualità occulte o meccaniche, non hanno posto nella filosofia sperimentale. In questa filosofia le proposizioni si deducono dai fenomeni e si rendono generali per induzione. Così si sono conosciute l’impenetrabilità, la mobilità e l’impeto dei corpi, e le leggi dei moti e della gravità. Ed è sufficiente che la gravità esista realmente, agisca secondo le leggi da noi esposte e basti a tutti i moti dei corpi celesti e del nostro mare.

#### 8. Lo spirito sottilissimo

**[III.G9.11]** Si potrebbe ora aggiungere qualcosa su un certo spirito sottilissimo che pervade i corpi grossolani e si nasconde in essi; per la cui forza e le cui azioni le particelle dei corpi si attraggono a vicenda a distanze minime e, divenute contigue, si tengono unite; e i corpi elettrici agiscono a distanze maggiori, tanto respingendo quanto attraendo i corpuscoli vicini; e la luce è emessa, riflessa, rifratta, inflessa, e riscalda i corpi; e ogni sensazione è eccitata, e le membra degli animali si muovono a volontà, cioè per le vibrazioni di questo spirito propagate attraverso i solidi filamenti dei nervi dagli organi esterni dei sensi al cervello, e dal cervello nei muscoli. Ma queste cose non si possono esporre in poche parole; né si dispone di una quantità sufficiente di esperimenti, con i quali si devono determinare e mostrare con accuratezza le leggi delle azioni di questo spirito.

**[III.G9.12]** FINE.

#### Note di Newton allo Scolio generale

**[III.G9.13]** [1] Cioè imperatore universale.

**[III.G9.14]** [2] Il nostro Pocock fa derivare la parola *deus* dalla parola araba *du* (e, nel caso obliquo, *di*), che significa «signore». E in questo senso i principi sono chiamati dèi, Salmo lxxxiv, 6, e Giovanni x, 45. E Mosè è detto dio del fratello Aronne e dio del re Faraone (Esodo iv, 16 e vii, 1). E nello stesso senso le anime dei principi morti erano un tempo chiamate dèi dai pagani, ma falsamente, per mancanza di dominio.

**[III.G9.15]** [3] Così pensavano gli antichi, come Pitagora presso Cicerone, *De natura deorum*, libro I; Talete; Anassagora; Virgilio, *Georgiche*, libro IV, v. 220, ed *Eneide*, libro VI, v. 721; Filone, *Allegorie*, libro I, all’inizio; Arato nei *Fenomeni*, all’inizio. Così anche gli scrittori sacri, come Paolo negli Atti xvii, 27, 28; Giovanni nel Vangelo xiv, 2; Mosè nel Deuteronomio iv, 39 e x, 14; Davide nel Salmo cxxxix, 7, 8, 9; Salomone in 1 Re viii, 27; Giobbe xxii, 12, 13, 14; Geremia xxiii, 23, 24. Gli idolatri, invece, immaginavano che il Sole, la Luna e gli astri, le anime degli uomini e altre parti del mondo fossero parti del Dio sommo, e perciò da adorare; ma falsamente.

**Fine del Libro III e dell’opera. Nel testo originale segue *FINIS*; le tre note sono a piè di pagina.**

---

## Apparato

### A.0 Estensioni del glossario

I termini seguenti non comparivano nei glossari comuni né fra quelli fissati dal coordinatore. Ognuno è reso in modo costante in tutto il fascicolo.

| Latino | Italiano | Motivazione |
|---|---|---|
| *latus transversum* | «lato trasverso» | Prop. XLII. Il glossario fissa *axis transversus* «asse trasverso» e *latus rectum* «lato retto»; *latus transversum* è il termine di Apollonio per l’asse trasverso, e si conserva il calco parallelo a «lato retto». Motte «transverse diameter». Nota N3. |
| *operatio* | «operazione» | Prop. XLII (*Operatio 1*, *Oper. 2*, *Oper. 3*); *operationes trigonometricæ / arithmeticæ* «operazioni trigonometriche / aritmetiche». |
| *tempus æquatum* | «tempo uguagliato» | Il tempo corretto con l’equazione del tempo, cioè il tempo medio (Motte «equal time»). Si conserva il calco per coerenza con *æquatio* «equazione»; nota N1. |
| *tempus apparens* | «tempo apparente» | Il tempo dell’orologio solare. Intestazioni delle tabelle del 1664–65 e del 1682. |
| *distantia perihelia / aphelia* | «distanza perielia / afelia» | Aggettivi tecnici; Motte «perihelion distance», «aphelion distance». |
| *nodus ascendens* | «nodo ascendente» | Applicazione di *nodi* «nodi». |
| *retrogradus*; *directus* | «retrogrado»; «diretto» | Moto contro / secondo l’ordine dei segni. |
| *signa* (*signa fere sex descripsit*) | «segni» | I segni zodiacali di 30°; nota N1. |
| *schema* | «schema» | Il disegno su carta del cammino della cometa fra le stelle (Hooke, Petit, Hevelius). Motte «scheme». |
| *sculptor* | «incisore» | Chi incise la tavola dello schema di Petit. |
| *stella nova*; *stellæ quæ per vices apparent & evanescunt* | «stella nuova»; «stelle che appaiono e svaniscono alternativamente» | Senza termini moderni nel testo («supernova», «variabile» solo nelle note). |
| *magnitudo* (delle stelle) | «grandezza» | «Stelle di seconda grandezza». |
| *zodiacus* | «zodiaco» | |
| *cathedra Cassiopeiæ*; *pes dexter serpentarii* | «sedia di Cassiopea»; «piede destro del Serpentario» | Parti delle figure delle costellazioni. |
| Nomi delle stelle nella tabella del 1664–65 | *Cor Leonis* «Cuore del Leone»; *Spica Virginis* «Spiga della Vergine» (istruzione del coordinatore); *Humerus Orionis dexter* «spalla destra di Orione»; *Procyon* «Procione»; *Lucida Mandibulæ Ceti* «lucida della mascella della Balena»; *Lucida Arietis* «lucida dell’Ariete»; *Aldebaran*; *Palilicium* «Palilicio»; *Cingulum / Caput Andromedæ* «cintura / testa di Andromeda» | Rese italiane dei nomi latini; le identificazioni moderne sono nella nota N5 (non verificate sulle fonti allegate). *Stella prima / secunda arietis* «prima / seconda stella dell’Ariete», abbreviato «la prima / la seconda dell’Ariete» come nel latino. |
| *spiritus humidi*; *tincturæ*; *sulphura*; *limus*, *lutum*, *argilla* | «spiriti umidi»; «tinture»; «zolfi»; «limo», «fango», «argilla» | Lessico chimico del Seicento, conservato (Prop. XLII, ultima frase). |
| *anima mundi* | «anima del mondo» | Scolio generale. |
| *dominium*; *dominatio* | «dominio»; «dominazione» | Newton distingue il dominio che Dio ha (*propter dominium suum*) e la dominazione che costituisce la deità (*deitas est dominatio dei*; *dominatio entis spiritualis deum constituit*). Motte rende entrambi «dominion». Due termini latini, due italiani. |
| *dominus* | «Signore» (titolo di Dio, *dominus deus*, *universorum dominus*), «signore» (nome comune: *omnis dominus non est deus*, *dominus dominorum* nell’elenco) | Glossario: *Dominus* «Signore». Distinzione di maiuscola, non di termine. |
| *ens* | «ente» | *ens intelligens & potens*, *ens æternum*. |
| *consilium* | «disegno» | *consilio & dominio entis intelligentis*: il progetto intenzionale. Motte «counsel». |
| *compages* | «compagine» | *Elegantissima hæcce … compages*. Motte «system». |
| *virtus* | «virtù» | *non per virtutem solam, sed etiam per substantiam*; *sine virtutis diminutione*. È l’efficacia, la potenza attiva; «virtù» conserva il termine storico (come Motte, «virtually», «virtue»). |
| *passio*; *pati* | «patire» | *sine mutua passione*; *Deus nihil patitur*: subire un’azione. |
| *colere*; *venerari* | «adorare»; «venerare» | *nec … coli debet*; *veneramur autem & colimus*. |
| *causæ finales* | «cause finali» | |
| *fatum & natura* | «fato e natura» | Minuscole; Motte «Fate and Nature». |
| *fingere* | «inventare» (*hypotheses non fingo*); «finto» (*ficta fictum*); «immaginare» (*fingebant idololatræ*) | Il glossario fissa «non invento ipotesi». Lo stesso verbo ricorre due altre volte nello Scolio: è segnalato nella nota N12. |
| *corpora crassa* | «corpi grossolani» | Come *crassus* nel Fascicolo 20. |
| *capillamenta nervorum* | «filamenti dei nervi» | Motte «filaments». |
| *corpora electrica* | «corpi elettrici» | I corpi che, strofinati, attraggono. |

**Dubbi sul glossario fissato.**

- *Pantocrator*: il glossario chiede il greco traslitterato con nota. Nel testo scrivo *Pantocrator* seguito dal greco Παντοκράτωρ fra parentesi, perché la trascrizione ha il solo greco; la nota di Newton (III.G9.13) dà la glossa latina.
- *sensorium* «sensorio»: il termine era previsto nel glossario del coordinatore ma **non compare** nello Scolio generale del 1726 secondo la trascrizione allegata, né in Motte. Vedi la nota N14.
- *hypothesis* «ipotesi»: nella Prop. XLII *ex hypothesi quod sint parabolicæ* (III.G8.07) è un’assunzione di calcolo, resa «nell’ipotesi che»; nello Scolio generale (*hypothesis vorticum*, *hypotheses non fingo*) è la congettura che Newton respinge. Stesso termine, due usi; nota N12.

### A.1 Proposizione XLII

**Latino:** *Inventam cometæ trajectoriam corrigere.*

**Inglese:** “To correct a comet's trajectory found as above.”

**Scelte.**

- Enunciato all’infinito, reso con l’infinito italiano come gli altri problemi («Correggere la traiettoria trovata di una cometa»). Motte aggiunge «as above», cioè per la Prop. XLI: è implicito in *inventam*.
- *Operatio 1.*, *Oper. 2.*, *Oper. 3.* → «Operazione 1, 2, 3».
- *propositionem superiorem* → «la proposizione precedente» (la Prop. XLI).
- *in eorum aliquo in perigæo versari*: *eorum* è neutro plurale e può riferirsi ai *loca* (i tre luoghi) o ai *tempora* A e B; Motte sceglie «in one of those times». Ho reso «in uno di essi», conservando l’ambiguità. *Perigæum* è reso «perigeo» secondo il glossario (Motte «perigeon»): per una cometa il punto più vicino alla Terra. Non è chiaro se Newton intenda il perigeo in senso stretto o, per estensione, il punto della traiettoria più vicino al Sole; la parola latina è *perigæum* in entrambe le occorrenze. Lettura da discutere.
- *circa centrum solis ceu umbilicum* → «intorno al centro del Sole come fuoco».
- *per operationes arithmeticas, ope prop. xxi. Lib. i. institutas* → «con operazioni aritmetiche condotte per mezzo della Prop. XXI del Libro I»: la Prop. XXI è una costruzione geometrica; qui va eseguita con il calcolo.
- *velocitate cometæ per prop. xvi. lib. i. inventa* → «con la velocità della cometa trovata per la Prop. XVI del Libro I».
- **Ordine delle istruzioni nell’Operazione 2.** Il latino dice prima di aumentare la longitudine dei nodi, poi di mantenere l’inclinazione; Motte inverte l’ordine. Nell’Operazione 2 Motte scrive «20 or 30 minutes» a parole, nell’Operazione 3 «20' or 30'».
- *signis + & − probe observatis* → «badando bene ai segni + e −».
- *ea lege, ut sit* → «con questa legge: che sia».
- Le formule della soluzione sono scritte come nel latino, con la barra per le frazioni appiattite («1L» = 1/L; «1L+m⁢l-m⁢L+n⁢λ-n⁢L» = 1/(L + ml − mL + nλ − nL)). La lettura è confermata dalle formule SVG 1275–1279 di Motte.
- **Il fattore 2.** Le due equazioni per m e n hanno a sinistra 2G − 2C e 2T − 2S, sia nel latino sia in Motte (SVG 1272, 1273). Con le correzioni K + mP e I + nQ della frase seguente, la coerenza lineare richiederebbe G − C e T − S. Lo segnalo senza correggere: nota N2.
- *Q.E.I.* → «C.V.T.».

### A.2 Il confronto fra comete e la cometa del 1664–1665 (III.G8.06–III.G8.14)

- *Cæterum* → «Del resto». Motte non apre un nuovo capoverso e continua dopo «Q.E.I.».
- *revolventium* → «che ritornano»: sono le comete che percorrono orbite chiuse.
- *ex hypothesi quod sint parabolicæ* → «nell’ipotesi che siano paraboliche» (A.0).
- *quam cum observationibus supra contuli* → «che ho confrontato sopra con le osservazioni»: la Prop. XLI (gruppo G7), dove la tabella della cometa del 1680 confronta osservazioni e calcoli.
- **Nomi.** *Hevelius* (Johannes Hevelius, astronomo di Danzica); *Halleius noster* «il nostro Halley» (Edmond Halley); *Auzoutius* (Adrien Auzout); *Hookius* (Robert Hooke); *Petitus* (Pierre Petit); *Gottignies* (Gilles-François de Gottignies); *Flamstedius* (John Flamsteed); *D. Bradleus* «il signor Bradley» (James Bradley); *D. Poundius* «il signor Pound» (James Pound); *Cornelius Gemma*; *Tycho Brahæus* «Tycho Brahe»; *Keplerus* «Keplero»; *Hipparchus* «Ipparco»; *Pocockus* «Pocock» (Edward Pocock). Le forme moderne dei nomi e i nomi propri non presenti nel latino (Johannes, Adrien, Pierre ecc.) vengono da conoscenza generale (non verificato sulle fonti allegate). *Gedanum* è Danzica.
- *tempore æquato Londini* → «in tempo uguagliato, a Londra» (A.0). *p. m.* → «pomeridiane».
- *existente mediocri terræ a sole distantia 100000* → «essendo la distanza media della Terra dal Sole 100000».
- *Mense Februario anni ineuntis 1665* → «Nel mese di febbraio dell’anno 1665 appena cominciato»: per il calendario giuliano inglese l’anno civile cominciava il 25 marzo, ma Newton intende qui l’anno astronomico (non verificato sulle fonti allegate). Motte «the beginning of the year 1665».
- **Le ore del 7 febbraio.** La trascrizione scrive *Feb. 7d. 7′. 30″ Parisiis (id est Feb. 7d 8′. 37″ Gedani)*, con i segni dei primi e dei secondi al posto di ore e minuti. Motte ha «7h. 30'» e «8h. 37'», come richiedono la differenza di longitudine Parigi–Danzica (1h 7′, la stessa del 7 marzo) e la tabella (8h 37½′). Traduco «7h 30′», «8h 37′».
- *in circulo magno* → «su un cerchio massimo»; *in paralello latitudinis* (refuso della trascrizione per *parallelo*) → «nel parallelo della latitudine».
- *Ratione mediocri posui* → «Prendendo un valore medio, io l’ho posta». Motte esplicita «taking the middle between the two extremes», che il latino non dice. Il conto non torna esattamente: nota N4.
- **«primæ arietis» (III.G8.11).** Il testo dice di aggiungere 1′ alla longitudine e 8′ 10″ alla latitudine della **prima** dell’Ariete; i numeri risultanti (♈ 29° 18′, 8° 36′ 26″) si ottengono invece dalla **seconda** (♈ 29° 17′ 18″ + 1′ = 29° 18′ 18″; 8° 28′ 16″ + 8′ 10″ = 8° 36′ 26″). Dalla prima si avrebbe ♈ 28° 31′ 15″ e 7° 17′ 8″. La lezione è la stessa in Motte («the first star in Aries»): svista dell’originale, non corretta nel testo (§ A.6; nota N4).
- *quasi spatio quartæ vel quintæ partis itineris uno die confecti* → «di circa la quarta o la quinta parte del cammino compiuto in un giorno».
- *jam módo prætergressus fuerat*: *módo* con l’accento è un refuso della trascrizione (atteso *modo*).
- *secunduum Hookium*: refuso della trascrizione per *secundum*.
- *sculptor viam cometæ … irregulariter incurvavit* → «l’incisore incurvò irregolarmente il cammino della cometa». Motte attenua: «did not rightly trace the curvature».
- *9gr. 3′⁤12* → «9° 3½′» (frazione appiattita della trascrizione; Motte SVG 1254 = 3½′).
- *signaque fere sex descripsit* → «percorse quasi sei segni» (180° circa di longitudine).
- *ex retrogrado factus est directus* → «da retrogrado divenne diretto».
- *Subducenda tamen sunt minuta duo prima circiter, ubi cometa velocissimus fuit* → «Si devono però sottrarre circa due primi dove la cometa fu velocissima». Motte «we are to subduct about 2'».
- *in orbe magno* → «nell’orbe magno» (glossario; Motte lascia il latino *orbis magnus*).

### A.3 Le comete del 1683, 1682, 1723 e 1607; perturbazioni, stelle nuove, vapori (III.G8.15–III.G8.28)

- *Confirmatur etiam theoria* → «La teoria è confermata anche», ripetuto tre volte come nel latino.
- *Hic fuit retrogradus in orbe* → «Questa fu retrograda in un’orbita». Motte riorganizza la frase in un periodo unico.
- *computante Halleio* → «secondo il calcolo di Halley». Nella cometa del 1682 la trascrizione apre la parentesi e non la chiude: *(computante Halleio erat in ♉ …*; Motte la chiude. Traduco con la parentesi chiusa.
- *Loca vero ex observationibus Flamstedii computata, & cum locis per theoriam computatis collata* (1682) → «I luoghi calcolati dalle osservazioni di Flamsteed e confrontati con i luoghi calcolati con la teoria». Motte «collected from Mr. Flamsted's observations … computed from our theory»: aggiunge «our».
- *D. Bradleo, astronomiæ apud Oxonienses professore Saviliano* → «il signor Bradley, professore saviliano di astronomia a Oxford». *patruo suo D. Poundio* → «suo zio, il signor Pound» (*patruus* è propriamente lo zio paterno; Motte «his uncle»).
- *distantia perihelia a sole 998651, existente radio orbis magni 1000000* (1723): unità diverse (un milione invece di centomila), come nel latino e in Motte.
- *His exemplis abunde satis manifestum est* → «Da questi esempi è manifesto, più che a sufficienza».
- *orbes cometarum … enumerari possunt* → «si possono enumerare le orbite delle comete»; *apheliorum altitudines* → «le altezze degli afeli». Motte «aphelion distances».
- *ut √c: 75×75 ad 1* → «come la radice cubica di 75 × 75 sta a 1» (trascrizione di ∛(75 × 75); Motte SVG 1280).
- *Si cometæ hi duo fuerint unus & idem* → «Se queste due comete sono state una sola e medesima»; Motte «If these were not two different comets, but one and the same».
- *Atque hæc ita se habebunt si cometa, spatio annorum septuaginta quinque, in hoc orbe posthac redierit* → «E così staranno le cose se la cometa, nello spazio di settantacinque anni, ritornerà in seguito in questa orbita». Il futuro anteriore *redierit* esprime una condizione da verificare: Newton non afferma il ritorno, lo propone come prova.
- *eorumm* (III.G8.23): refuso della trascrizione per *eorum*.
- *per gravitates in se mutuo* → «dalle gravità reciproche».
- *non comprehendantur zodiaco more planetarum* → «non siano comprese nello zodiaco alla maniera dei pianeti».
- *Qua de causa cometæ, qui altius descendunt …, debent altius ascendere* → «Per questa causa le comete che scendono più in basso … devono salire più in alto». Motte «descend the lowest … ascend the highest» (superlativi per comparativi).
- *minus distabat a sole in perihelio suo quam parte sexta diametri solis* → «distava dal Sole, nel suo perielio, meno della sesta parte del diametro del Sole»: la distanza è dalla superficie del Sole (nota N8).
- *stellæ fixæ, quæ paulatim expirant in lucem & vapores* → «le stelle fisse, che a poco a poco si consumano in luce e vapori». Motte «that have been gradually wasted by the light and vapours emitted from them for a long time»: aggiunge «for a long time».
- *refici*; *novo alimento accensæ* → «essere ristorate»; «accese da nuovo alimento». Motte «recruited»; «from this fresh supply of new fuel».
- *stella in cathedra Cassiopeiæ* → «la stella nella sedia di Cassiopea».
- *luce sua vix cedentem veneri* → «per luce poco inferiore a Venere».
- *ex oculis evanuit* → «scomparve alla vista».
- *Color illi ab initio clarus, albicans ac splendidus, postea flavus, … rutilans instar martis aut stellæ aldebaran; … albitudinem sublividam induxit* → «Il suo colore fu al principio chiaro, biancheggiante e splendente, poi giallo, … rosseggiante come Marte o la stella Aldebaran; … assunse una bianchezza un po’ livida». Motte «afterwards it turned a little yellow» aggiunge «a little»; «a kind of dusky whiteness».
- *stella in dextro pede serpentarii* → «la stella nel piede destro del Serpentario»; *stellam jovis* → «la stella di Giove», cioè il pianeta.
- *Hipparchus … excitatus fuisse dicitur* → «Si dice che … Ipparco sia stato spinto».
- *revolvendo partem lucidam & partem obscuram per vices ostendere* → «ruotando, mostrare alternativamente una parte luminosa e una parte oscura». Motte aggiunge «about their axes».
- *atmospheæras* (III.G8.28): refuso della trascrizione per *atmosphæras*.
- *limum, & lutum, & argillam* → «limo, fango, argilla»; Motte «mud, and clay» rende due termini con due e ne omette uno.

### A.4 Scolio generale

**Latino (incipit):** *Hypothesis vorticum multis premitur difficultatibus.*

**Inglese (incipit):** “The hypothesis of vortices is pressed with many difficulties.”

Lo Scolio è il testo più citato dei *Principia*. Ho tradotto frase per frase, conservando le ripetizioni volute (*semper & ubique*, *more minime humano, more minime corporeo*), le enumerazioni complete e la sintassi argomentativa. Scelte e divergenze, capoverso per capoverso:

- **III.G9.01, vortici.** *multis premitur difficultatibus* → «è gravata da molte difficoltà». *Ut … deberent* è una serie di tre finali parallele («Perché … dovrebbero»), conservata. *Revolutiones solis & planetarum circum axes suos* → «Le rivoluzioni del Sole e dei pianeti attorno ai propri assi» (Motte «rotation»). Motte unisce le frasi a coppie con «but» e chiude con una parafrasi: «with a freedom that is incompatible with the notion of a vortex» per *quod fieri non potest, nisi vortices tollantur*.
- **III.G9.02, spazi liberi.** *in vacuo Boyliano* → «nel vuoto di Boyle» (Motte «Mr. Boyle's vacuum»). *pluma tenuis & aurum solidum* → «una piuma sottile e dell’oro massiccio». *Et par est ratio* → «E lo stesso ragionamento vale». *in orbibus specie & positione datis* → «in orbite date di forma e di posizione» (glossario: *specie datus*). Motte aggiunge «where there is no air to resist their motions».
- **III.G9.03, ordine del sistema.** *Planetæ sex principales* → «I sei pianeti principali» (Motte «primary»). *Lunæ decem* → «Dieci lune», minuscolo: è il nome comune dei satelliti (nota N11). *Et hi omnes motus regulares originem non habent ex causis mechanicis* è un’affermazione; Motte la attenua in «it is not to be conceived that mere mechanical causes could give birth». *consilio & dominio entis intelligentis & potentis* → «dal disegno e dal dominio di un ente intelligente e potente». *Unius dominio* → «al dominio di Uno solo», con la maiuscola come nel latino. **Ultima frase:** la trascrizione ha *hic eadem immensam ab invicem distantiam posuerit*, costruzione anomala (*hic* per *is*? *eadem* senza un sostantivo chiaro); traduco secondo il senso, che Motte conferma («he hath placed those systems at immense distances one from another»), e la segnalo nel § A.7.
- **III.G9.04–III.G9.05, dominio.** *non ut anima mundi, sed ut universorum dominus* → «non come anima del mondo, ma come Signore dell’universo». *dominus deus Παντοκράτωρ* → «Signore Dio *Pantocrator* (Παντοκράτωρ)»; Motte porta la glossa della nota di Newton nel testo («παντοκράτωρ, or Universal Ruler») e omette la nota (nota N13). *deus est vox relativa & ad servos refertur* → «“Dio” è una parola relativa e si riferisce ai servi». *Dominatio entis spiritualis deum constituit, vera verum, summa summum, ficta fictum* → «È la dominazione di un ente spirituale che costituisce Dio: una dominazione vera un Dio vero, una somma un Dio sommo, una finta un Dio finto»; Motte «a true, supreme, or imaginary dominion makes a true, supreme, or imaginary God». *Vox deus passim significat dominum* → «La parola “Dio” significa comunemente “signore”».
- **III.G9.06, eternità e spazio.** *durat ab æterno in æternum, & adest ab in infinitum*: la trascrizione ha *ab in infinitum*, dove manca *infinito*; Motte «from infinity to infinity». Traduco «è presente dall’infinito all’infinito» (§ A.7). *Non est æternitas & infinitas, sed æternus & infinitus; non est duratio & spatium, sed durat & adest* → conservo l’opposizione fra sostantivi astratti e predicati. *certe rerum omnium fabricator ac dominus non erit nunquam, nusquam*: alla lettera «non sarà mai, in nessun luogo», cioè «non potrà essere un ente che non è in nessun tempo e in nessun luogo»; la doppia negazione latina non si regge in italiano, perciò la sciolgo: «del fabbricatore e signore di tutte le cose non si potrà dire che non è mai e che non è in nessun luogo». Motte «cannot be never and no where». *neutræ* → «né le une né le altre». *principio ejus cogitante* → «nel suo principio pensante».
- **III.G9.07, onnipresenza.** *non per virtutem solam, sed etiam per substantiam* → «non per sola virtù, ma anche per sostanza» (A.0; Motte «not virtually only, but also substantially»). *sine mutua passione* → «senza che l’uno patisca dall’altro»; Motte «yet neither affects the other». *omnispræsentia*: refuso della trascrizione per *omnipræsentia*. *in confesso est* → «è ammesso da tutti» (Motte «It is allowed by all»). *totus est sui similis* → «è tutto simile a sé». *totus vis sentiendi* → «tutto forza di sentire».
- **III.G9.08–III.G9.09, conoscenza di Dio.** *nec sub specie rei alicujus corporei coli debet* → «né deve essere adorato sotto l’aspetto di qualche cosa corporea». *nulla actione reflexa* → «con nessun atto riflesso» (Motte «by any reflex act of our minds», aggiunge «of our minds»). **Omissione di Motte:** *Hunc cognoscimus solummodo per proprietates ejus & attributa, & per sapientissimas …* diventa «We know him only by his most wise and excellent contrivances of things»: cade *per proprietates ejus & attributa*. *Tota rerum conditarum … diversitas* → «Tutta la diversità delle cose create»; Motte «natural things which we find suited to», parafrasi. **Omissione di Motte nell’elenco:** *videre, audire, loqui* → Motte «to see, to speak»: cade *audire*. *aliqualem tamen* → «ma tuttavia una somiglianza di qualche genere». *Et hæc de deo* → «E questo basti su Dio». *ex phænomenis disserere* → «discorrere a partire dai fenomeni»; Motte «from the appearances of things».
- **III.G9.10, causa della gravità.** *Hactenus … exposui … nondum assignavi* → «Finora ho esposto … non ho ancora assegnato», alla prima persona singolare; Motte passa al plurale («we have explained … have not yet assigned») e torna al singolare per «I have not been able … I frame no hypotheses». *Oritur utique hæc vis a causa aliqua* → «Certo questa forza nasce da una qualche causa»; Motte «This is certain, that it must proceed». *sine virtutis diminutione* → «senza diminuzione della sua virtù». *pro quantitate materiæ solidæ* → «secondo la quantità di materia solida». *ex quiete apheliorum planetarum* → «dalla quiete degli afeli dei pianeti» (la Prop. XIV di questo Libro, non citata). *hypotheses non fingo* → «non invento ipotesi» (glossario; nota N12). *seu metaphysicæ, seu physicæ, seu qualitatum occultarum, seu mechanicæ* → «siano metafisiche o fisiche, siano di qualità occulte o meccaniche». *propositiones deducuntur ex phænomenis, & redduntur generales per inductionem* → «le proposizioni si deducono dai fenomeni e si rendono generali per induzione»; **Motte aggiunge** «particular propositions … and afterwards rendered general», due parole che non sono nel latino. *impetus corporum* → «l’impeto dei corpi» (glossario; Motte «the impulsive force»).
- **III.G9.11, spirito.** *spiritu quodam subtilissimo* → «un certo spirito sottilissimo» (glossario); *corpora crassa pervadente, & in iisdem latente* → «che pervade i corpi grossolani e si nasconde in essi». *ad minimas distantias* → «a distanze minime» (Motte «at near distances»). *contiguæ factæ cohærent* → «divenute contigue, si tengono unite». *inflectitur* → «inflessa» (la diffrazione dei bordi, nota N15). *ad voluntatem moventur* → «si muovono a volontà». *per solida nervorum capillamenta* → «attraverso i solidi filamenti dei nervi»; Motte «mutually propagated along», aggiunge «mutually». **Aggiunta di Motte:** nell’ultima frase *leges actionum hujus spiritus* diventa «the laws by which this electric and elastic Spirit operates»: «electric and elastic» non è nel latino del 1726 (nota N15).
- **FINIS** → «FINE». Motte «END OF THE MATHEMATICAL PRINCIPLES».
- **Note di Newton.** La trascrizione ha tre note: [1] *Id est Imperator universalis*; [2] Pocock; [3] *Ita sentiebant veteres*. Motte ne ha due: la [1] è assorbita nel testo, e le altre due sono numerate [1] e [2]. Nella nota [2] la trascrizione ha *Psalm. lxxxiv. 6* e *Joan. x. 45*; Motte «Psal. lxxxii. ver. 6» e «John x. ver. 35» (§ A.7). Nella nota [3] *Philo Allegor. lib. 1. sub initio* → «Filone, *Allegorie*, libro I, all’inizio»; *Fingebant autem idololatræ* → «Gli idolatri, invece, immaginavano» (nota N12). Nella nota [3] il latino ha *Johannes in Evang. xiv. 2*, Motte «St. John's Gosp. chap. xiv. ver. 2»: coincidono.

**Differenze rispetto alle edizioni precedenti.** Le fonti allegate (latino 1726 e Motte 1846, che traduce la terza edizione) non documentano varianti fra le edizioni dei *Principia*; perciò non ne annoto. L’unica divergenza di contenuto fra il latino e Motte è l’aggiunta «electric and elastic» (nota N15). Che lo Scolio generale manchi nella prima edizione (1687) e compaia dalla seconda (1713) è di conoscenza generale (non verificato sulle fonti allegate).

### A.5 Rimandi

**Rimandi al Libro I (2), verificati sul Fascicolo 6.**

| Luogo | Latino | Resa | Enunciato citato (Fascicolo 6) | Esito |
|---|---|---|---|---|
| III.G8.02 | *ope prop. xxi. Lib. i.* | «per mezzo della Prop. XXI del Libro I» | S4.24: «Descrivere intorno a un fuoco dato una traiettoria che passi per punti dati e tocchi rette date di posizione.» | Regge: per tre punti, con il Sole nel fuoco, si descrive la conica. Newton chiede di eseguire per via aritmetica la costruzione geometrica. |
| III.G8.02 | *velocitate cometæ per prop. xvi. lib. i. inventa* | «con la velocità della cometa trovata per la Prop. XVI del Libro I» | S3.30: le velocità nelle coniche stanno in rapporto composto dal rapporto inverso delle perpendicolari sulle tangenti e dal rapporto subduplicato dei lati retti. | Regge: dalla velocità e dalla perpendicolare dal fuoco si ha l’area descritta nell’unità di tempo, quindi il tempo T per l’area D + E. |

Non citata ma usata: il passo «dato il lato trasverso è dato il tempo periodico» (III.G8.05) e il calcolo dei 75 anni (III.G8.22) usano la Prop. XV del Libro I (tempi periodici in rapporto sesquiplicato degli assi maggiori, Fascicolo 6). Nessun rimando che non torni.

**Rimandi al Libro II.** Nessuno esplicito. Lo Scolio generale (III.G9.01) riprende l’argomento contro i vortici della Sezione IX del Libro II (Fascicolo 20, II.S9.27 e II.S9.32), senza citarla.

**Rimandi interni al Libro III (verificati sul latino degli altri gruppi).**

| Luogo | Latino | Resa | Esito |
|---|---|---|---|
| III.G8.02 | *per propositionem superiorem* | «per la proposizione precedente» | Prop. XLI (G7), che trova la traiettoria parabolica da tre osservazioni: regge. |
| III.G8.07 | *quam cum observationibus supra contuli* | «che ho confrontato sopra con le osservazioni» | Prop. XLI, *Exemplum* della cometa del 1680 con le tabelle: regge. |
| III.G8.25 | *minus distabat … quam parte sexta diametri solis* | — | Non è un rimando, ma il dato si controlla con la Prop. XLI (distanza perielia «come 6 a 1000 circa») e con il diametro apparente medio del Sole (32′ 12″, gruppo G6): nota N8. |
| III.G9.02 | *pluma tenuis & aurum solidum* | — | Esperimento descritto anche nella Prop. VI (G2), non citata. |
| III.G9.02 | *secundum leges supra expositas* | «secondo le leggi esposte sopra» | Generico (Libri I e III). |
| III.G9.10 | *ex quiete apheliorum planetarum* | «dalla quiete degli afeli dei pianeti» | Prop. XIV (G2): *Orbium aphelia & nodi quiescunt*; non citata. |

### A.6 Tabelle: ricostruzione e cifre che non tornano

Le quattro tabelle sono ricostruite dalla trascrizione, che le spezza in una cella per riga, allineando le colonne sul latino e controllando le righe su Motte. Le differenze «osservato − calcolato» sono state ricalcolate con lo script `tmp/27/verifica.py` (nota N5). **Nessuna cifra è corretta nel testo.**

| Tabella | Riga | Trascrizione | Che cosa non torna | Motte | Lettura probabile |
|---|---|---|---|---|---|
| 1664–65 | Feb. 7, long. calcolata | ♈ 27.24.55 | scarto di 20′ 9″ dall’osservato (♈ 27.4.46), contro scarti di pochi primi nelle righe vicine | uguale | ♈ 27.4.55 (scarto 9″); refuso della stampa o della fonte di Halley |
| 1664–65 | Feb. 7, lat. osservata | 7.3.25 | il testo (III.G8.09) dà 7° 3′ 29″ | 7.3.29 | 7.3.29 |
| 1664–65 | Dic. 27, ora | 06h.45⁤01′ | forma anomala; le altre righe hanno «½» | 6.45 | da leggere sulla stampa |
| 1664–65 | Dic. 27, long. calcolata | ♉ 7.8.54 | non controllabile (non c’è colonna delle differenze) | 7.8.45 | da leggere sulla stampa |
| 1683 | Lug. 25, lat. calcolata | 24.24.47 | con la differenza −1′ 7″ l’osservato 28.23.40 richiede 28.24.47 | uguale | 28.24.47 |
| 1683 | Ago. 22, latitudini | 5.16.53 / 5.16.50 | tornano con −0.3 | 5.16.58 / 5.16.58 | il latino è coerente; Motte sbaglia |
| 1723 | Ott. 10, diff. long. | −50 | osservato 6.41.12 − calcolato 6.41.42 = −30″ | uguale | una delle due longitudini o la differenza (da leggere sulla stampa) |
| 1723 | Nov. 8, long. calcolata | 4.29.34 | con la differenza −18″ ci vuole 4.29.54 | 4.29.54 | 4.29.54 (Motte coerente) |
| 1723 | Nov. 14, long. calcolata | 5.2.21 | con la differenza −35″ ci vuole 5.2.51 | 5.2.51 | 5.2.51 (Motte coerente) |

**Convenzioni dei segni.** Nella tabella del 1683 le differenze sono osservato − calcolato (per le latitudini australi, |osservato| − |calcolato|); nella tabella del 1682 sono calcolato − osservato; in quella del 1723 osservato − calcolato. Con queste convenzioni, che il testo non dichiara, tutte le altre righe tornano al secondo.

**Calcoli del testo che non tornano esattamente** (nota N4): il «valore medio» 27° 4′ 46″ (la media degli estremi è 27° 4′ 36,5″); la distanza fra la prima e la seconda dell’Ariete, 1° 33′ nel testo, 1° 32′ dalle coordinate date; la distanza fra la seconda dell’Ariete e la stella A, 52′ 29″ nel testo, 51′ 59″ su cerchio massimo dalle coordinate date (52′ 33″ è la sola differenza di longitudine); *primæ arietis* per *secundæ* (§ A.2).

### A.7 Refusi e anomalie della trascrizione

| Luogo | Trascrizione | Lettura | Tipo |
|---|---|---|---|
| III.G8.02 | *trajectoriaeæ* | *trajectoriæ* | doppia codifica del dittongo |
| III.G8.05 | *2⁢G-2⁢C=m⁢G…*, *1L*, *1L+m⁢l-m⁢L+n⁢λ-n⁢L* | 2G − 2C = mG …; 1/L; 1/(L + ml − mL + nλ − nL) | segno invisibile U+2062 fra i fattori; frazioni appiattite |
| III.G8.08 | *29′⁤12*, *01⁤12* ecc. | 29½′, 1½′ | frazioni appiattite |
| III.G8.08 | *06h.45⁤01′* (Dic. 27) | ? | forma anomala |
| III.G8.08 | *Lat. aust* (Dic. 20) | *Lat. aust.* | punto mancante |
| III.G8.09 | *Feb. 7d. 7′. 30″ … Feb. 7d 8′. 37″* | 7d. 7h. 30′ … 7d. 8h. 37′ | segni di primi e secondi per ore e minuti |
| III.G8.09 | *paralello* | *parallelo* | refuso probabile |
| III.G8.11 | *secunduum*; *módo* | *secundum*; *modo* | refusi probabili |
| III.G8.11 | *ad longitudinem primæ arietis* | (*secundæ*) | svista dell’originale (anche in Motte) |
| III.G8.16 | *2.5{3}.12* (Lug. 15) | 2.53.12 | artefatto della pagina web |
| III.G8.17 | *(computante Halleio erat* | *(computante Halleio) erat* | parentesi non chiusa |
| III.G8.18 | *gr.18.* (intestazione della colonna) | *gr.* | artefatto |
| III.G8.23 | *eorumm* | *eorum* | refuso probabile |
| III.G8.28 | *atmospheæras* | *atmosphæras* | doppia codifica |
| III.G9.03 | *hic eadem immensam ab invicem distantiam posuerit* | senso: «egli li ha posti a immensa distanza l’uno dall’altro» | costruzione anomala |
| III.G9.04 | *deourum* | *deorum* | refuso probabile |
| III.G9.06 | *adest ab in infinitum* | *adest ab infinito in infinitum* | parola caduta |
| III.G9.07 | *omnispræsentia* | *omnipræsentia* | refuso probabile |
| III.G9.14 | *Psalm. lxxxiv. 6*; *Joan. x. 45* | Motte: *lxxxii. 6*; *x. 35* | numeri da controllare |

**Punti da controllare sulla stampa ECCO.**

| Pagina 1726 | Trascrizione | Lettura attesa | Motivo |
|---|---|---|---|
| p. 519 | *2⁢G-2⁢C=…*, *2⁢T-2⁢S …* | G − C, T − S? | il fattore 2 non è coerente con K + mP, I + nQ (nota N2); verificare se è nella stampa |
| p. 520 | Dic. 27, *06h.45⁤01′*; long. calcolata *7.8.54* | 6h 45½′?; 7.8.54 o 7.8.45 | forma anomala; Motte 7.8.45 |
| p. 520 | Feb. 7, lat. osservata *7.3.25* | 7.3.29 | il testo e Motte hanno 29″ |
| p. 520 | Feb. 7, long. calcolata *♈ 27.24.55* | ♈ 27.4.55? | scarto di 20′ (anche in Motte: forse nell’originale) |
| p. 521 | *Feb. 7d. 7′. 30″ Parisiis (id est Feb. 7d 8′. 37″ Gedani)* | 7h. 30′; 8h. 37′ | segni anomali |
| p. 521 | *paralello*; *secunduum*; *módo* | *parallelo*; *secundum*; *modo* | refusi |
| pp. 521–522 | *ad longitudinem primæ arietis* | *secundæ*? | i numeri sono quelli della seconda; verificare se la svista è nella stampa |
| p. 522 | *(computante Halleio erat* | parentesi chiusa | punteggiatura |
| p. 523 | 1683, Lug. 25, lat. calcolata *24.24.47* | 28.24.47 | la differenza −1′ 7″ lo richiede (anche in Motte) |
| p. 523 | 1682, intestazione *gr.18.* | *gr.* | artefatto |
| p. 524 | 1723, Ott. 10, *6.41.12 / 6.41.42 / −50* | — | −30″ dai valori; uno dei tre numeri |
| p. 524 | 1723, Nov. 8 e 14, long. calcolate *4.29.34*, *5.2.21* | 4.29.54, 5.2.51 | le differenze e Motte le richiedono |
| p. 525 | *eorumm* | *eorum* | refuso |
| p. 526 | *atmospheæras* | *atmosphæras* | refuso |
| p. 527 | *hic eadem immensam ab invicem distantiam posuerit* | ? | costruzione anomala |
| p. 528 | *deourum*; *adest ab in infinitum* | *deorum*; *ab infinito in infinitum* | refuso; parola caduta |
| p. 529 | *omnispræsentia* | *omnipræsentia* | refuso |
| p. 528, nota | *Psalm. lxxxiv. 6*; *Joan. x. 45* | lxxxii. 6; x. 35 (Motte) | numeri dei versetti |

### A.8 Formule SVG di Motte

Ho controllato con `svg_tex.tsv` tutte le **17** formule SVG distinte degli estratti di Motte del fascicolo (1149, 925, 1166, 1271, 927, 1272, 1273, 1274, 1275, 1276, 1277, 1278, 1279, 643, 1169, 1254, 1280); lo Scolio generale non ne ha. Tornano con il latino: δ, ε, τ, δ + ε, γ, ρ, 1/L, 1/l, 1/λ, R + mr − mR + nρ − nR, 1/(L + ml − mL + nλ − nL), ½, 3½′, ∛(75 × 75), e le due equazioni 1272–1273 (con il fattore 2 del latino).

**SVG di Motte che non tornano con il latino.**

| n | LaTeX | Lettura attesa | Commento |
|---|---|---|---|
| 1169 | `\lambda` | γ | «the first star of Aries, which I shall hereafter call [SVG 1169]»: il latino ha γ, e Motte stesso usa poi γ (SVG 927). |
| 1272 | `2\mathrm G - 2 \mathrm C, = m\mathrm G - mg + n\mathrm G - n \gamma` | 2G − 2C = mG − mg + nG − nγ | virgola spuria prima di «=»; il contenuto torna con il latino. |
| 643 | `\tfrac{1}{2}` | — | La formula torna, ma Motte la mette soltanto in cinque righe della tabella del 1664–65 (Dic. 3, 4, 20, 21; Gen. 7), mentre il latino ha «½» in diciotto righe su diciannove (tutte tranne Dic. 27). |

### A.9 Riepilogo: dove Motte aggiunge, omette o sbaglia

| Luogo | Latino | Motte 1846 | Tipo |
|---|---|---|---|
| III.G8.01 | *Inventam … corrigere* | «found as above» | esplicitazione |
| III.G8.02 | *in eorum aliquo* | «in one of those times» | interpretazione |
| III.G8.03 | aumento del nodo, poi inclinazione mantenuta | ordine invertito | riordino |
| III.G8.08 | intestazione *Temp. Appar. Gedani, st. vet.* | «Appar. Time» | omissione di Danzica e dello stile |
| III.G8.08 | Dic. 19 e Gen. 7: segni ♊, ♈ | segno mancante | omissione |
| III.G8.08 | Dic. 26 calc. ♉ 9.2.28 | «♉. . 2.28» | cifra mancante |
| III.G8.08 | Dic. 27 calc. 7.8.54 | 7.8.45 | cifre diverse (da controllare) |
| III.G8.08 | Feb. 7 lat. oss. 7.3.25 | 7.3.29 | Motte coerente con il testo |
| III.G8.08 | Mar. 1, 8h 16½′ | «1.18.16» | **ora errata** |
| III.G8.08 | Mar. 7, long. ♉ 0.2.48 / ♉ 0.2.42 | ♈ in entrambe | **segno errato** |
| III.G8.08 | «½» in diciotto ore su diciannove | solo in cinque righe | omissione |
| III.G8.09 | γ | [SVG 1169] = λ | lettera errata |
| III.G8.09 | *Ratione mediocri* | «taking the middle between the two extremes» | aggiunta interpretativa |
| III.G8.12 | *sculptor … irregulariter incurvavit* | «did not rightly trace» | attenuazione |
| III.G8.14 | *in orbe magno* | «in the orbis magnus» | latino conservato |
| III.G8.16 | 1683, Ago. 22 lat. 5.16.53 / 5.16.50 | 5.16.58 / 5.16.58 | **cifre errate** (non tornano con −0.3) |
| III.G8.17 | *per theoriam* | «from our theory» | aggiunta |
| III.G8.20 | 1723, Nov. 8 e 14 calc. 4.29.34, 5.2.21 | 4.29.54, 5.2.51 | Motte coerente con le differenze |
| III.G8.21 | *apheliorum altitudines* | «aphelion distances» | resa libera |
| III.G8.24 | *altius descendunt … altius ascendere* | «the lowest … the highest» | superlativi |
| III.G8.25 | *expirant in lucem & vapores* | «… for a long time» | aggiunta |
| III.G8.26 | *postea flavus* | «turned a little yellow» | aggiunta |
| III.G8.28 | *revolvendo* | «revolve about their axes» | aggiunta |
| III.G8.28 | *limum, & lutum, & argillam* | «mud, and clay» | omissione di un termine |
| III.G9.01 | *nisi vortices tollantur* | «with a freedom that is incompatible with the notion of a vortex» | parafrasi |
| III.G9.02 | — | «where there is no air to resist their motions» | aggiunta |
| III.G9.03 | *originem non habent ex causis mechanicis* | «it is not to be conceived that mere mechanical causes could give birth» | attenuazione |
| III.G9.04 | nota [1] *Imperator universalis* | «or Universal Ruler» nel testo; nota omessa | spostamento |
| III.G9.04–05 | *dominium*, *dominatio* | «dominion» per entrambi | distinzione persa |
| III.G9.09 | *per proprietates ejus & attributa* | — | **omissione** |
| III.G9.09 | *videre, audire, loqui* | «to see, to speak» | **omissione** di *audire* |
| III.G9.09 | *rerum conditarum* | «natural things which we find suited to» | parafrasi |
| III.G9.10 | *exposui … assignavi* | «we have explained … have not yet assigned» | persona cambiata |
| III.G9.10 | *propositiones … redduntur generales* | «particular propositions … afterwards rendered general» | **aggiunta** |
| III.G9.10 | *impetus corporum* | «the impulsive force of bodies» | termine non equivalente (*impetus*) |
| III.G9.11 | *ad minimas distantias* | «at near distances» | attenuazione |
| III.G9.11 | *propagatis* | «mutually propagated» | aggiunta |
| III.G9.11 | *hujus spiritus* | «this electric and elastic Spirit» | **aggiunta di contenuto** |
| III.G9.14 | *Psalm. lxxxiv. 6*; *Joan. x. 45* | «Psal. lxxxii. ver. 6»; «John x. ver. 35» | numeri diversi (Motte probabilmente corretto) |

---

## Note editoriali e fisiche

Queste note sono aggiunte del presente fascicolo, non affermazioni tradotte da Newton. Le verifiche numeriche sono state eseguite con lo script `tmp/27/verifica.py` (trigonometria sferica sulle coordinate eclittiche date nel testo, ricalcolo delle differenze delle tabelle, controllo del metodo della Prop. XLII su un modello lineare di prova). Ciò che proviene da conoscenza generale e non dalle fonti allegate è marcato «(non verificato sulle fonti allegate)».

### N1. Segni zodiacali, coordinate, ore e calendario

I simboli sono i dodici segni dello zodiaco, ciascuno di 30° di longitudine eclittica contata dall’equinozio di primavera: ♈ Ariete (0°–30°), ♉ Toro, ♊ Gemelli, ♋ Cancro, ♌ Leone, ♍ Vergine, ♎ Bilancia, ♏ Scorpione, ♐ Sagittario, ♑ Capricorno, ♒ Acquario, ♓ Pesci (330°–360°). La longitudine si conta in gradi dentro il segno: «♌ 8° 40′ 30″» vale 128° 40′ 30″. La latitudine è la distanza angolare dall’eclittica, boreale o australe. Le ore sono contate da mezzogiorno, secondo l’uso astronomico: «Dic. 3d 18h 29½′» è la mattina del 4 dicembre, alle 6h 29½′ del tempo civile (non verificato sulle fonti allegate). Il «tempo apparente» è quello della meridiana; il «tempo uguagliato» (*tempus æquatum*) è il tempo apparente corretto con l’equazione del tempo, cioè il tempo medio. Le date sono secondo il calendario giuliano (*stylo veteri*, «stile vecchio»), dieci giorni indietro rispetto al gregoriano nel Seicento e undici nel 1723 (non verificato sulle fonti allegate).

Le differenze d’ora del testo sono coerenti fra loro: Londra → Danzica +1h 16′ (22 febbraio, 1° marzo, perielio di novembre: 11h 52′ → 13h 8′); Parigi → Danzica +1h 7′ (7 febbraio, 7 marzo); dunque Londra → Parigi 9′. I valori moderni sono 1h 14,6′ e 9,3′ (non verificato sulle fonti allegate).

### N2. Il metodo della Prop. XLII e il fattore 2

La Prop. XLII è un metodo di **correzione differenziale**: si parte dal piano dell’orbita trovato con la Prop. XLI (nodo K, inclinazione I), si calcolano due varianti spostando di poco il nodo (di P) e l’inclinazione (di Q), e si interpola linearmente. Le condizioni che il piano vero deve soddisfare sono due:

1. il rapporto delle aree descritte fra le osservazioni deve uguagliare il rapporto dei tempi (legge delle aree): G = C;
2. il tempo calcolato per l’area totale deve uguagliare il tempo vero: T = S.

Se G, g, γ sono i valori del rapporto delle aree nei tre piani, l’approssimazione lineare dà per il piano (K + mP, I + nQ) il valore G + m(g − G) + n(γ − G). Imporre che sia uguale a C dà

G − C = mG − mg + nG − nγ,

e allo stesso modo T − S = mT − mt + nT − nτ. Le correzioni del lato retto, R + m(r − R) + n(ρ − R), e dell’inverso del lato trasverso, L + m(l − L) + n(λ − L), hanno esattamente questa forma.

Il testo (latino e Motte, SVG 1272–1273) ha invece **2G − 2C** e **2T − 2S** a sinistra. Con queste equazioni i numeri m e n risultano doppi e le correzioni K + mP, I + nQ annullano gli scarti soltanto se si prende la metà di m e n. Lo script lo mostra su un modello lineare di prova: con il fattore 1 gli scarti finali sono 0 e 0; con il fattore 2 restano −0,05 su G − C e −1,0 su T − S, cioè gli scarti iniziali cambiati di segno. È un punto per il curatore: non correggo il testo; va verificato sulla stampa del 1726 (§ A.7) e, se possibile, sulle edizioni precedenti. Non posso dire, dalle fonti allegate, se il fattore 2 abbia una giustificazione nell’uso di Newton.

### N3. Lato retto, lato trasverso e periodo

Il **lato retto** è il parametro della conica (per la parabola, quattro volte la distanza perielia: per la cometa del 1664, 410286/4 = 102572, cioè 1,026 volte la distanza media della Terra dal Sole). Il **lato trasverso** è l’asse maggiore. Newton interpola non il lato trasverso ma il suo inverso (1/L, 1/l, 1/λ): una scelta felice, perché per orbite quasi paraboliche l’asse maggiore è enorme e mal determinato, mentre il suo inverso è piccolo e varia con regolarità (passa da valori positivi a zero quando l’ellisse diventa parabola). In termini moderni 1/*a* è proporzionale all’energia dell’orbita (non verificato sulle fonti allegate). Dato l’asse maggiore, il periodo segue dal rapporto sesquiplicato (Libro I, Prop. XV): è il calcolo usato per la cometa del 1607/1682 (nota N7).

### N4. Le riduzioni delle osservazioni di febbraio e marzo 1665

Ho ricalcolato con la trigonometria sferica tutti i passaggi numerici di III.G8.09–III.G8.12, partendo dalle coordinate delle stelle date nel testo.

| Passo | Testo | Ricalcolo | Esito |
|---|---|---|---|
| distanza γ–A su cerchio massimo | 1° 19′ 46″ | 1° 19′ 46,2″ | torna |
| la stessa nel parallelo di γ (divisa per cos 7° 9′) | 1° 20′ 26″ | 1° 20′ 23,7″ | scarto 2″ |
| longitudine della cometa 28° 30′ 15″ − 1° 20′ 26″ | ♈ 27° 9′ 49″ | 27° 9′ 49″ | torna |
| «valore medio» | ♈ 27° 4′ 46″ | media di 27° 9′ 49″ e 26° 59′ 24″ (gli estremi): 27° 4′ 36,5″; di 27° 9′ 49″ e 27° 0′: 27° 4′ 54,5″; dei tre valori: 27° 3′ 4″ | **non torna** con nessuna media semplice (scarto minimo 10″) |
| latitudine corretta 7° 8′ 58″ − (28° 30′ 15″ − 28° 24′ 45″) | 7° 3′ 29″ | 7° 3′ 28″ (7° 3′ 31″ riducendo i 5′ 30″ al parallelo) | torna |
| 22 febbraio: un quinto di γA; un quarto del quinto | 15′ 57″; 4′ | 15′ 57,2″; 3′ 59,3″ | torna |
| 22 febbraio: posizione della cometa | ♈ 28° 29′ 46″, 8° 12′ 36″ | ♈ 28° 29′ 52″, 8° 12′ 54″ (punto a un quinto da A verso γ, spostato di 4′ perpendicolarmente verso est) | accordo entro circa 20″ |
| 1° marzo: distanza fra la prima e la seconda dell’Ariete | 1° 33′ | 1° 31′ 59″ | scarto di 1′ |
| 1° marzo: 4/45 e 2/23 di 1° 33′; media | 8′ 16″; 8′ 5″; 8′ 10″ | 8′ 16,0″; 8′ 5,2″; 8′ 10,5″ | torna |
| 1° marzo: posizione della cometa | ♈ 29° 18′, 8° 36′ 26″ | dalla **seconda** dell’Ariete: 29° 18′ 18″, 8° 36′ 26″; dalla prima (come dice il testo): 28° 31′ 15″, 7° 17′ 8″ | torna solo con la seconda (§ A.2) |
| 7 marzo: distanza fra la seconda dell’Ariete e A | 52′ 29″ | 51′ 59″ su cerchio massimo; 52′ 33″ la sola differenza di longitudine | scarto di 30″ |
| 7 marzo: seconda dell’Ariete + 45′ 30″ | ♉ 0° 2′ 48″ | ♉ 0° 2′ 48″ | torna |

Gli scarti sono dell’ordine di quelli che si hanno lavorando su schemi disegnati (Newton parla espressamente di schemi di Hooke, Petit e Hevelius). L’unico errore vero è *primæ* per *secundæ* nel 1° marzo.

### N5. Le tabelle: controllo aritmetico e identificazioni

**Cometa del 1664–1665.** La tabella non ha la colonna delle differenze. Ho calcolato «calcolato − osservato» per tutte le diciannove righe. In longitudine gli scarti sono di +0,5′ … +1,6′ in dicembre fino al 7, poi crescono a +2′ … +3,2′ fra il 19 e il 28 dicembre, quando la cometa era più veloce (quasi 20° in un giorno), e scendono sotto 1′ da gennaio a marzo. È esattamente ciò che dice Newton in III.G8.14: «Si devono però sottrarre circa due primi dove la cometa fu velocissima». Fa eccezione la riga del 7 febbraio, con uno scarto di **20′ 9″**: il calcolato ♈ 27.24.55 è quasi certamente un errore per ♈ 27.4.55 (§ A.6). In latitudine gli scarti stanno entro 2′, salvo il 31 dicembre (+3′ 25″) e il 22 febbraio (−2′ 11″).

**Cometa del 1683.** Tutte le differenze tornano al secondo con la convenzione osservato − calcolato, salvo la latitudine del 25 luglio, dove il calcolato 24.24.47 va letto 28.24.47 (§ A.6). Per le tre righe con latitudine australe la differenza è |osservato| − |calcolato|.

**Cometa del 1682.** Tutte le undici righe tornano al secondo, con la convenzione opposta: calcolato − osservato.

**Cometa del 1723.** Dodici righe su quindici tornano al secondo (osservato − calcolato). Non tornano: 10 ottobre (−30″ dai valori, −50″ nella tabella; anche in Motte), 8 e 14 novembre (le longitudini calcolate della trascrizione, 4.29.34 e 5.2.21, danno +2″ e −5″; quelle di Motte, 4.29.54 e 5.2.51, danno esattamente −18″ e −35″ come la tabella). Gli scarti di questa tabella non superano 55″: l’orbita di Bradley rappresenta le osservazioni entro un primo.

**Le stelle di riferimento** (identificazioni moderne, non verificate sulle fonti allegate): Cuore del Leone = Regolo (α Leonis); Spiga della Vergine = Spica (α Virginis); spalla destra di Orione = Betelgeuse (α Orionis); Procione = α Canis Minoris; lucida della mascella della Balena = Menkar (α Ceti); lucida dell’Ariete = Hamal (α Arietis); Aldebaran = α Tauri; il Palilicio è, nei cataloghi antichi, un altro nome di Aldebaran, ma nella tabella compaiono entrambi i nomi in righe diverse, quindi l’identificazione resta incerta; cintura di Andromeda = Mirach (β Andromedae); testa di Andromeda = Alpheratz (α Andromedae); prima e seconda dell’Ariete = γ e β Arietis.

### N6. Gli elementi di Halley per la cometa del 1664

Dal nodo ascendente (♊ 21° 13′ 55″), dall’inclinazione (21° 18′ 40″) e dalla distanza del perielio dal nodo misurata nell’orbita (49° 27′ 30″), la trigonometria sferica dà la longitudine del perielio sull’eclittica ♌ 8° 40′ 35″ (Halley ♌ 8° 40′ 30″) e la latitudine 16° 1′ 57″ (Halley 16° 1′ 45″). Gli elementi sono coerenti entro una decina di secondi. La correzione proposta da Newton (49° 27′ 18″ invece di 49° 27′ 30″) sposta la longitudine del perielio di circa 11″.

### N7. La cometa del 1607 e del 1682

Se il periodo è di 75 anni, l’asse maggiore sta all’asse maggiore dell’orbe magno come ∛(75²) = 17,784 sta a 1: «1778 a 100» torna. La distanza afelia è l’asse maggiore meno la distanza perielia: 35,57 − 0,587 = 34,98, cioè «35 a 1 circa», con l’uno o l’altro dei due valori della distanza perielia (0,58680 per il 1607, 0,58328 per il 1682). Le differenze fra gli elementi del 1607 e del 1682 sono 55′ nel nodo, 54′ nell’inclinazione, 37′ nel perielio e 0,0035 nella distanza perielia: piccole, e Newton subito dopo spiega che le perturbazioni reciproche delle comete possono produrne (III.G8.23).

È la cometa che oggi porta il nome di Halley. Il suo ritorno, previsto per la fine del 1758, fu osservato a partire dal dicembre 1758 e passò al perielio nel marzo 1759; il periodo medio è di circa 76 anni (non verificato sulle fonti allegate). Il testo di Newton è prudente: «se la cometa … ritornerà».

### N8. La cometa del 1680 e la caduta nel Sole

Il dato «meno della sesta parte del diametro del Sole» si controlla con due dati del Libro III. Nella Prop. XLI la distanza della cometa dal centro del Sole al perielio sta alla distanza della Terra dal Sole «come 6 a 1000 circa»; nel gruppo G6 il diametro apparente medio del Sole è 32′ 12″, cioè un semidiametro di 0,00468 volte la distanza Terra–Sole. La cometa passò dunque a 0,0060 − 0,0047 = 0,0013 dalla superficie del Sole, mentre un sesto del diametro vale 0,0016: il testo torna se la distanza è contata dalla superficie. L’argomento della caduta per resistenza dell’atmosfera solare è un’ipotesi fisica di Newton; non ha un calcolo.

### N9. Le stelle nuove del 1572 e del 1604 e le stelle variabili

La «stella nuova» di Cassiopea del 1572 e quella del Serpentario del 1604 sono oggi identificate come due supernove della nostra Galassia (la «stella di Tycho» e la «stella di Keplero»); la spiegazione di Newton, una stella ravvivata da comete che vi cadono, non è quella moderna (non verificato sulle fonti allegate). La sequenza di luminosità che Newton riporta (Venere, Giove, Sirio, poi dalla seconda alla sesta grandezza in circa sedici mesi) è una curva di luce descritta a occhio nudo. Le stelle «che appaiono e svaniscono alternativamente … e non superano quasi mai la terza grandezza» sono le variabili periodiche, come Mira Ceti; la spiegazione per rotazione di un corpo con una faccia chiara e una scura è un’ipotesi del Seicento (non verificato sulle fonti allegate).

### N10. Scolio generale: perché i vortici non funzionano

Il primo capoverso mette in fila tre richieste incompatibili per il moto delle parti del vortice:

1. **legge delle aree** per ogni pianeta: un raggio che spazza aree uguali in tempi uguali in un’orbita quasi circolare ha velocità angolare inversamente proporzionale al quadrato della distanza, quindi periodi delle parti del vortice **proporzionali al quadrato della distanza** («rapporto duplicato»);
2. **terza legge di Keplero** per i pianeti: periodi proporzionali alla potenza 3/2 della distanza («proporzione sesquiplicata»);
3. **stabilità dei vortici minori** di Giove e Saturno trasportati nel vortice solare: periodi **uguali** a tutte le distanze (rotazione rigida).

Tre esponenti diversi (2, 3/2, 0) per la stessa funzione: le richieste si escludono a vicenda. La prima e la seconda erano già confrontate nello Scolio della Prop. LII del Libro II (Fascicolo 20, II.S9.27), dove Newton trova che un vortice viscoso dà proprio il rapporto duplicato. A queste si aggiungono le rotazioni del Sole e dei pianeti, che non seguono nessuna delle tre leggi, e le comete, che attraversano il sistema in tutte le direzioni.

### N11. «Sei pianeti principali» e «dieci lune»

I sei pianeti sono Mercurio, Venere, Terra, Marte, Giove e Saturno. Le dieci lune sono la Luna, i quattro satelliti di Giove e i cinque di Saturno: lo conferma il Libro III stesso, che nel Fenomeno I dà i tempi periodici di quattro satelliti di Giove e nel Fenomeno II di cinque satelliti di Saturno (gruppo G1). La parola *lunæ* per i satelliti è un uso di Newton; il glossario usa «satellite» per *satelles* e *comites*. Qui la conservo, minuscola, perché il latino ha *lunæ*.

### N12. *Hypotheses non fingo*: «non invento ipotesi»

La resa è fissata dal glossario. Il verbo *fingere* significa «plasmare, foggiare» e quindi «immaginare, inventare, fingere». «Non invento ipotesi» rende la sfumatura dell’invenzione arbitraria; «non formulo ipotesi» sarebbe troppo debole e contraddirebbe l’uso di Newton, che di ipotesi ne formula (lo Scolio stesso propone lo «spirito sottilissimo», e la Prop. XLII lavora «nell’ipotesi che siano paraboliche»). Motte traduce «I frame no hypotheses».

Il senso preciso è dato dalla frase che segue: «Tutto ciò che non si deduce dai fenomeni deve essere chiamato ipotesi». Newton non rinuncia a congetturare; rifiuta di dare per dimostrata una causa della gravità che non sia dedotta dai fenomeni. Nel fascicolo e nelle fonti allegate *fingere* e i suoi derivati compaiono in punti che illuminano la scelta:

- *ficta fictum* (III.G9.05): «una dominazione finta, un Dio finto»;
- *Fingebant autem idololatræ* (nota [3], III.G9.15): gli idolatri «immaginavano» che il Sole e gli astri fossero parti di Dio, «ma falsamente»;
- nella Regola III del Libro III (gruppo G1): *contra experimentorum tenorem somnia temere confingenda non sunt*, «non si devono inventare temerariamente sogni contro il tenore degli esperimenti»;
- nella Regola IV (gruppo G1): le proposizioni raccolte dai fenomeni per induzione valgono *non obstantibus contrariis hypothesibus*, «nonostante le ipotesi contrarie».

In tutti questi luoghi *fingere* indica il costruire qualcosa che non ha fondamento nei fenomeni. Per la didattica conviene leggere insieme la Regola IV e questa frase dello Scolio.

### N13. *Pantocrator*

Παντοκράτωρ è una parola greca composta da «tutto» e «dominare»: «colui che domina su tutto». La nota di Newton (III.G9.13) la rende in latino *Imperator universalis*, «imperatore universale». Motte porta la glossa nel testo («or Universal Ruler») e omette la nota. Il termine è il titolo con cui la traduzione greca della Bibbia (la *Settanta*) e il Nuovo Testamento rendono l’«Onnipotente» o il «Signore degli eserciti» (non verificato sulle fonti allegate). Per Newton conta che sia un titolo di **dominio**, non di natura: tutto l’argomento del capoverso (III.G9.04–III.G9.05) è che «Dio» è una parola relativa, come «signore», e si dice in rapporto ai servi. La nota [2] su Pocock sostiene la stessa tesi con l’etimologia (*deus* da un arabo *du*, «signore»), che va presa come documento delle idee del tempo (non verificato sulle fonti allegate).

### N14. *Sensorium*: un termine che qui non c’è

Il glossario del Libro III (preparato dal coordinatore) fissava *sensorium* «sensorio» per lo Scolio generale. Ma **nella trascrizione allegata dello Scolio generale del 1726 la parola *sensorium* non compare**, e neppure in Motte (ho cercato la stringa in tutte le fonti allegate: nessuna occorrenza). Il passo più vicino è III.G9.07: Dio è «tutto occhio, tutto orecchio, tutto cervello, tutto braccio, tutto forza di sentire, di intendere e di agire, ma in un modo per nulla umano, in un modo per nulla corporeo», e III.G9.08: «non abbiamo idea dei modi in cui il sapientissimo Dio sente e intende tutte le cose». Newton qui esclude proprio che Dio abbia organi di senso.

L’immagine dello spazio come «sensorio» di Dio è delle Questioni finali dell’*Ottica* (nell’edizione latina del 1706 e, con altra numerazione, nelle Questioni 28 e 31 dell’edizione inglese del 1717), e fu al centro della polemica fra Leibniz e Clarke (1715–1716) (non verificato sulle fonti allegate). Nel testo tradotto non ho introdotto la parola. Se il curatore vuole un riquadro didattico sul *sensorium*, va costruito su quelle fonti, che non sono nel pacchetto.

### N15. Lo spirito sottilissimo

L’ultimo capoverso elenca i fenomeni che Newton attribuisce, in via di congettura dichiarata («Si potrebbe ora aggiungere …»; «queste cose non si possono esporre in poche parole»), a uno spirito che pervade i corpi: la coesione a piccolissima distanza, l’attrazione e repulsione elettrica, l’emissione, riflessione, rifrazione e **inflessione** della luce (cioè la sua deviazione presso i bordi dei corpi, che oggi chiamiamo diffrazione: non verificato sulle fonti allegate), il riscaldamento, la sensazione e il moto volontario per vibrazioni lungo i nervi. Il capoverso si chiude con un argomento metodologico coerente con «non invento ipotesi»: mancano gli esperimenti per determinarne le leggi.

**L’aggiunta di Motte.** Nell’ultima frase Motte scrive «this **electric and elastic** Spirit»; il latino del 1726 della trascrizione allegata ha soltanto *hujus spiritus*. È l’unica aggiunta di contenuto di Motte nello Scolio. Che derivi da annotazioni di Newton nel suo esemplare dell’edizione del 1713, è di conoscenza generale (non verificato sulle fonti allegate); dalle fonti allegate risulta soltanto la divergenza. Nella pagina interattiva il testo a fronte di Motte va accompagnato da una nota.

### N16. Il metodo dello Scolio e la gravità

III.G9.10 riassume il metodo dei *Principia*: si sa **come** agisce la gravità (sulle masse e non sulle superfici, in proporzione inversa al quadrato della distanza, fino all’orbita di Saturno e agli afeli delle comete), non **perché**. La prova della legge dell’inverso del quadrato «fino all’orbita di Saturno» è la quiete degli afeli (Prop. XIV del Libro III): un esponente diverso da 2 farebbe ruotare le apsidi (Libro I, Sezione IX; non citata qui). La condizione «se pure quegli afeli sono in quiete» per le comete è un esempio di prudenza: per le comete il dato osservativo manca.

---

## Controllo della copertura

Pagine 1726 dai marcatori ‹n› della trascrizione (la Prop. XLII comincia a p. 518, prima del marcatore ‹519›). Motte: estratti senza marcatori di pagina, «sezione corrispondente».

| Identificatori | Incipit latino | Contenuto | 1726 | Motte 1846 |
|---|---|---|---|---|
| III.G8.01 | *Inventam cometæ trajectoriam corrigere* | Prop. XLII, enunciato | p. 518 | Prop. XLII |
| III.G8.02–III.G8.04 | *Operatio 1.* … *Oper. 3.* | le tre operazioni | pp. 518–519 | Operation 1–3 |
| III.G8.05 | *Jam sit C ad 1 ut A ad B* | soluzione, C.V.T. | p. 519 | «Then taking C to 1» |
| III.G8.06 | *Cæterum cometarum revolventium* | confronto fra comete | p. 519 | «But the periodic times» |
| III.G8.07 | *In hunc finem computandæ sunt* | cometa del 1664–65, elementi di Halley | pp. 519–520 | «To this purpose» |
| III.G8.08 | *Temp. Appar. Gedani, st. vet.* | tabella 1664–65 (19 righe doppie) | p. 520 | tabella |
| III.G8.09 | *Mense Februario anni ineuntis 1665* | riduzione del 7 febbraio | p. 521 | «In February» (due capoversi) |
| III.G8.10 | *Feb. 22d. 7h. 30′ Londini* | 22 febbraio | p. 521 | «February 22d.» |
| III.G8.11 | *Mart. 1d. 7h. 0′ Londini* | 1° marzo | pp. 521–522 | «March 1» |
| III.G8.12 | *Mart. 7d. 7h. 30′ Parisiis* | 7 marzo | p. 522 | «March 7» |
| III.G8.13 | *Visus etiam fuit hic cometa Martii die 9* | 9 marzo | p. 522 | «This comet was also seen» |
| III.G8.14 | *Apparuit hic cometa menses tres* | bilancio; parallasse annua | p. 522 | «This comet appeared three months» |
| III.G8.15–III.G8.16 | *Confirmatur etiam theoria per motum cometæ, qui apparuit anno 1683* | cometa del 1683 e tabella (17 righe) | pp. 522–523 | «This theory is likewise confirmed» |
| III.G8.17–III.G8.18 | *… qui apparuit anno 1682* | cometa del 1682 e tabella (11 righe) | p. 523 | «This theory is yet farther confirmed» |
| III.G8.19–III.G8.20 | *… qui apparuit anno 1723* | cometa del 1723 e tabella (15 righe) | pp. 523–524 | «This theory is also confirmed» |
| III.G8.21 | *His exemplis abunde satis manifestum est* | conclusione sugli esempi | p. 524 | «From these examples» |
| III.G8.22 | *Cometa retrogradus qui apparuit anno 1607* | cometa del 1607; 75 anni | pp. 524–525 | «That retrograde comet» |
| III.G8.23 | *Cæterum cometæ, ob magnum eorum numerum* | perturbazioni reciproche | p. 525 | «But, because of the great number» |
| III.G8.24 | *Et hinc ratio redditur* | comete fuori dallo zodiaco | p. 525 | «And hence a reason» |
| III.G8.25 | *Cometa, qui anno 1680 apparuit* | caduta nel Sole; stelle ravvivate | p. 525 | «The comet which appeared in the year 1680» |
| III.G8.26 | *Talis fuit stella in cathedra Cassiopeiæ* | stella del 1572 | pp. 525–526 | «Such was that star» |
| III.G8.27 | *Talis etiam fuit stella in dextro pede serpentarii* | stella del 1604; Ipparco | p. 526 | «Such also was the star» |
| III.G8.28 | *Sed fixæ, quæ per vices apparent* | stelle variabili; vapori | p. 526 | «As to those fixed stars» |
| III.G9.01 | *Hypothesis vorticum multis premitur difficultatibus* | Scolio generale: contro i vortici | pp. 526–527 | General Scholium |
| III.G9.02 | *Projectilia, in aëre nostro* | spazi liberi | p. 527 | «Bodies projected» |
| III.G9.03 | *Planetæ sex principales* | ordine del sistema; ente intelligente | p. 527 | «The six primary planets» |
| III.G9.04–III.G9.09 | *Hic omnia regit* … *ad philosophiam naturalem pertinet* | Dio, dominio, eternità, onnipresenza, conoscenza di Dio | pp. 528–529 | «This Being governs» |
| III.G9.10 | *Hactenus phænomena cælorum & maris nostri* | causa della gravità; *hypotheses non fingo* | p. 530 | «Hitherto we have explained» |
| III.G9.11 | *Adjicere jam liceret* | spirito sottilissimo | p. 530 | «And now we might add» |
| III.G9.12 | *FINIS.* | fine | p. 530 | «END OF THE MATHEMATICAL PRINCIPLES» |
| III.G9.13–III.G9.15 | *Id est Imperator universalis* … *Ita sentiebant veteres* | note [1]–[3] di Newton | pp. 528–529 | Footnotes [1]–[2] |

**Controlli eseguiti.**

1. **Copertura frase per frase.** Ho riletto in sequenza ogni periodo della trascrizione, da *Inventam cometæ trajectoriam corrigere* a *& substantias alias terrestres paulatim migrare* (Prop. XLII) e da *Hypothesis vorticum* a *FINIS* e alle tre note (Scolio generale), contro la traduzione: nessuna frase manca. Le tabelle sono riprodotte per intero: 19 righe doppie (1664–65), 17 righe più la riga «austr.» (1683), 11 (1682), 15 (1723), confrontate cella per cella con il latino e riga per riga con Motte. I 43 identificatori (III.G8.01–III.G8.28, III.G9.01–III.G9.15) sono consecutivi e unici (controllo automatico).
2. **Parte B.** `check.py` sul file finale con i due file latini e i due di Motte: JSON valido; tutte le stringhe `la` (enunciati e passi) sono sottostringhe esatte della trascrizione; tutte le stringhe `en` sono sottostringhe esatte di Motte; ogni identificatore di `copertura` è presente nel testo; ultima riga «OK».
3. **Matematica e tabelle** (`tmp/27/verifica.py`): riduzioni del febbraio–marzo 1665 (N4); elementi di Halley del 1664 (N6); differenze delle tabelle 1683, 1682, 1723 e scarti della tabella 1664–65 (N5); cometa del 1607/1682 (N7); metodo della Prop. XLII su un modello lineare (N2); cometa del 1680 e diametro del Sole (N8); orari Londra–Parigi–Danzica (N1). Le cifre che non tornano sono elencate nel § A.6 e non sono corrette nel testo.
4. **Motte.** Confronto di tutta la sezione corrispondente; divergenze nel § A.9; formule SVG nel § A.8 (17 controllate, 2 che non tornano più un’omissione).
5. **Separazione fra testo e commento.** Il testo tradotto non contiene formule moderne; le formule della Prop. XLII sono quelle di Newton, in forma lineare.

**Non ho potuto verificare:**

- **la stampa del 1726**: tutti i punti del § A.7, in particolare il fattore 2 della Prop. XLII, la riga del 7 febbraio nella tabella del 1664–65, le longitudini calcolate dell’8 e del 14 novembre 1723 e la frase *hic eadem immensam … posuerit*;
- **Motte 1729**: non so se le divergenze di Motte 1846 nelle tabelle (ora del 1° marzo, segno del 7 marzo, latitudini del 22 agosto 1683) siano già nella prima edizione inglese;
- **la paginazione di Motte**: gli estratti non hanno marcatori di pagina;
- **le identificazioni moderne** delle stelle, dei personaggi, della cometa di Halley e delle supernove (N5, N7, N9) e le notizie su *sensorium*, *Ottica* e polemica Leibniz–Clarke (N14), che vengono da conoscenza generale;
- **le varianti fra le edizioni** dello Scolio generale (1713, 1726): le fonti allegate non le documentano.

---

## Registro del lavoro successivo

| Unità | Stato |
|---|---|
| Libro III, Prop. XLII e Scolio generale | **Fascicolo 27, presente documento, prima versione** |
| Fattore 2 nelle equazioni di m e n (Prop. XLII) | Da verificare sulla stampa del 1726 e sulle edizioni precedenti; decidere se annotarlo nella pagina interattiva (N2) |
| Cifre delle tabelle che non tornano (§ A.6) | Da verificare sulla stampa del 1726 (scansione ECCO) e su Motte 1729 |
| *primæ arietis* per *secundæ* (III.G8.11) | Da verificare sulla stampa; nella pagina interattiva, nota a margine |
| *sensorium* | Il termine non compare nelle fonti allegate: decidere se togliere la voce dal glossario dello Scolio generale o costruire un riquadro con le fonti dell’*Ottica* (N14) |
| *dominium* / *dominatio* «dominio» / «dominazione» | Da confermare (A.0) |
| *latus transversum* «lato trasverso» | Da armonizzare con gli altri fascicoli del Libro III (A.0) |
| Pagine interattive | Parte B: Prop. XLII (metodo di correzione, con il modello lineare di N2 come simulazione); riduzione del 7 febbraio 1665 (triangolo sferico); quattro tabelle con il grafico degli scarti; ritorno della cometa del 1682; Scolio generale (primi due capoversi, con il confronto dei tre esponenti di N10) |
| Revisione filologica e scientifica indipendente | Da eseguire, con particolare attenzione allo Scolio generale |

Il presente testo è una nuova traduzione assistita da IA. Non riproduce traduzioni italiane o inglesi moderne. **Licenza prevista** (decisione del curatore, Fascicolo 3): testi e traduzioni CC BY-SA 4.0, codice MIT. La trascrizione latina è © The Newton Project; i testi di Motte sono di pubblico dominio.

---

## Parte B — Dati per le pagine interattive

Unità incluse:

- **L3-P42**: la Prop. XLII, con un passo per ogni frase latina delle tre operazioni e della soluzione (13 passi). Non ha figura: la pagina può mostrarla come simulazione numerica (nota N2).
- **L3-P42-Red1665**: la riduzione dell’osservazione del 7 febbraio 1665 (11 passi), un calcolo di trigonometria sferica con i controlli in `dati`.
- **L3-P42-Tab1665**, **L3-P42-Tab1683**, **L3-P42-Tab1682**, **L3-P42-Tab1723**: le quattro tabelle, con `passi` vuoti, i valori numerici in `dati` e l’esito dei controlli.
- **L3-P42-Cometa1607**: il calcolo del ritorno dopo 75 anni, con `passi` vuoti e i dati.
- **L3-SchGen**: lo Scolio generale, con un passo per frase dei primi due capoversi (12 passi) e nessun passo per il resto; la scelta è spiegata nel campo `nota`.

Escluse: le riduzioni del 22 febbraio, del 1° marzo e del 7 marzo (stesso tipo di calcolo del 7 febbraio; i controlli sono nella nota N4) e i capoversi descrittivi su perturbazioni, stelle nuove e vapori (III.G8.23–III.G8.28), che non hanno calcoli.

Convenzioni:

- `la`: testo latino esatto della trascrizione, refusi e segni invisibili U+2062 compresi, con gli spazi normalizzati;
- `it`: la traduzione di questo fascicolo;
- `en`: Motte 1846, allineato per senso; dove Motte unisce più frasi latine, `en` è la porzione corrispondente del suo periodo; i marcatori `[SVG n]` sono conservati;
- `dipende_da`: soltanto i rimandi citati nella frase latina;
- `figura.mostra`: elementi da rendere visibili, cumulativi; `figura.evidenzia`: relazioni da mettere in risalto;
- `dati`: valori sessagesimali come liste [segno, gradi, primi, secondi]; differenze in secondi con la convenzione di ciascuna tabella (§ A.6).

```json
{
 "fascicolo": "27-L3-P42-SchGen",
 "versione": "0.1",
 "data": "2026-11-08",
 "convenzioni": {
  "dipende_da": "solo rimandi citati esplicitamente nella frase latina",
  "en": "Motte 1846, allineato per senso; i marcatori [SVG n] sono conservati",
  "figura.mostra": "elementi da rendere visibili al passo, cumulativi salvo indicazione",
  "la": "",
  "dati": "valori sessagesimali come liste [segno zodiacale, gradi, primi, secondi]; differenze in secondi"
 },
 "unita": [
  {
   "id": "L3-P42",
   "tipo": "Propositio/Problema",
   "titolo": "Prop. XLII — correggere l’orbita trovata di una cometa (correzione differenziale)",
   "copertura": [
    "III.G8.01",
    "III.G8.02",
    "III.G8.03",
    "III.G8.04",
    "III.G8.05"
   ],
   "fonti": {
    "la": "",
    "en": "Motte 1846, sezione corrispondente (Book III, Prop. XLII)"
   },
   "enunciato": {
    "la": "",
    "it": "Correggere la traiettoria trovata di una cometa.",
    "en": "To correct a comet's trajectory found as above."
   },
   "figura_base": {
    "punti": [
     "Sole (fuoco)",
     "Terra nelle tre osservazioni",
     "luoghi veri 1, 2, 3 della cometa"
    ],
    "vincoli": [
     "tre piani di prova: (K, I), (K + P, I), (K, I + Q), con P, Q di 20′ o 30′",
     "in ciascun piano una conica con fuoco nel Sole per i tre luoghi veri (Libro I, Prop. XXI)",
     "aree D, E (d, e; δ, ε) fra le osservazioni; tempi T (t, τ) per l’area totale",
     "condizioni: rapporto delle aree = rapporto dei tempi (G = C); tempo calcolato = tempo vero (T = S)"
    ]
   },
   "passi": [
    {
     "id": "L3-P42-p1",
     "la": "",
     "it": "Operazione 1. Si assuma la posizione del piano della traiettoria trovata per la proposizione precedente; e si scelgano tre luoghi della cometa determinati con osservazioni accuratissime e il più possibile distanti fra loro; e sia A il tempo fra la prima e la seconda, e B il tempo fra la seconda e la terza.",
     "en": "OPERATION 1. Assume that position of the plane of the trajectory which was determined according to the preceding proposition; and select three places of the comet, deduced from very accurate observations, and at great distances one from the other. Then suppose A to represent the time between the first observation and the second, and B the time between the second and the third",
     "dipende_da": [
      "Prop. XLI di questo Libro"
     ],
     "figura": {
      "mostra": [
       "piano della traiettoria (posizione di prova: nodo K, inclinazione I)",
       "tre luoghi osservati 1, 2, 3",
       "intervalli A (1→2) e B (2→3)"
      ],
      "evidenzia": [
       "piano assunto"
      ]
     },
     "nota": "propositionem superiorem = la Prop. XLI. Motte divide il periodo latino in più frasi; en arriva fino alla definizione di B."
    },
    {
     "id": "L3-P42-p2",
     "la": "",
     "it": "Conviene poi che in uno di essi la cometa si trovi nel perigeo, o almeno non ne sia lontana.",
     "en": "but it will be convenient that in one of those times the comet be in its perigeon, or at least not far from it.",
     "dipende_da": [],
     "figura": {
      "mostra": [
       "posizione della Terra",
       "luogo osservato vicino al perigeo"
      ],
      "evidenzia": []
     },
     "nota": "eorum: i luoghi (o i tempi, come intende Motte: «in one of those times»). perigæum: Motte «perigeon»; vedi apparato A.1."
    },
    {
     "id": "L3-P42-p3",
     "la": "",
     "it": "Da questi luoghi apparenti si trovino, con operazioni trigonometriche, i tre luoghi veri della cometa in quel piano assunto della traiettoria.",
     "en": "From those apparent places find, by trigonometric operations, the three true places of the comet in that assumed plane of the trajectory;",
     "dipende_da": [],
     "figura": {
      "mostra": [
       "raggi visuali Terra→cometa nelle tre osservazioni",
       "intersezioni con il piano assunto: tre luoghi veri"
      ],
      "evidenzia": [
       "luoghi veri"
      ]
     }
    },
    {
     "id": "L3-P42-p4",
     "la": "",
     "it": "Poi per quei luoghi trovati, intorno al centro del Sole come fuoco, si descriva una sezione conica con operazioni aritmetiche condotte per mezzo della Prop. XXI del Libro I; e le sue aree, delimitate dai raggi condotti dal Sole ai luoghi trovati, siano D ed E: cioè D l’area fra la prima e la seconda osservazione, ed E l’area fra la seconda e la terza.",
     "en": "then through the places found, and about the centre of the sun as the focus, describe a conic section by arithmetical operations, according to Prop. XXI., Book I. Let the areas of this figure which are terminated by radii drawn from the sun to the places found be D and E; to wit, D the area between the first observation and the second, and E the area between the second and third;",
     "dipende_da": [
      "Libro I, Prop. XXI"
     ],
     "figura": {
      "mostra": [
       "Sole nel fuoco",
       "conica per i tre luoghi veri",
       "settori D (1→2) ed E (2→3)"
      ],
      "evidenzia": [
       "D",
       "E"
      ]
     }
    },
    {
     "id": "L3-P42-p5",
     "la": "",
     "it": "E sia T il tempo totale in cui l’area totale D + E deve essere descritta con la velocità della cometa trovata per la Prop. XVI del Libro I.",
     "en": "and let T represent the whole time in which the whole area D + E should be described with the velocity of the comet found by Prop. XVI., Book I.",
     "dipende_da": [
      "Libro I, Prop. XVI"
     ],
     "figura": {
      "mostra": [
       "tempo T calcolato per l’area D + E"
      ],
      "evidenzia": [
       "T"
      ]
     }
    },
    {
     "id": "L3-P42-p6",
     "la": "",
     "it": "Operazione 2. Si aumenti la longitudine dei nodi del piano della traiettoria, aggiungendo a quella longitudine 20′ o 30′, che si chiamino P; e si mantenga l’inclinazione di quel piano sul piano dell’eclittica.",
     "en": "OPER. 2. Retaining the inclination of the plane of the trajectory to the plane of the ecliptic, let the longitude of the nodes of the plane of the trajectory be increased by the addition of 20 or 30 minutes, which call P.",
     "dipende_da": [],
     "figura": {
      "mostra": [
       "secondo piano: nodo K + P, inclinazione I"
      ],
      "evidenzia": [
       "P"
      ]
     },
     "nota": "Motte inverte l’ordine delle due istruzioni (prima l’inclinazione mantenuta, poi l’aumento del nodo)."
    },
    {
     "id": "L3-P42-p7",
     "la": "",
     "it": "Poi, dai tre luoghi osservati della cometa già detti, si trovino in questo nuovo piano tre luoghi veri, come sopra; poi anche l’orbita che passa per quei luoghi, e le due aree della medesima descritte fra le osservazioni, che siano d ed e, e anche il tempo totale t in cui l’area totale d + e dovrebbe essere descritta.",
     "en": "Then from the aforesaid three observed places of the comet let the three true places be found (as before) in this new plane; as also the orbit passing through those places, and the two areas of the same described between the two observations, which call d and e; and let t be the whole time in which the whole area d + e should be described.",
     "dipende_da": [],
     "figura": {
      "mostra": [
       "nuovi luoghi veri",
       "nuova conica",
       "aree d, e",
       "tempo t"
      ],
      "evidenzia": [
       "d",
       "e",
       "t"
      ]
     }
    },
    {
     "id": "L3-P42-p8",
     "la": "",
     "it": "Operazione 3. Si mantenga la longitudine dei nodi dell’operazione prima, e si aumenti l’inclinazione del piano della traiettoria sul piano dell’eclittica, aggiungendo a quella inclinazione 20′ o 30′, che si chiamino Q.",
     "en": "OPER. 3. Retaining the longitude of the nodes in the first operation, let the inclination of the plane of the trajectory to the plane of the ecliptic be increased by adding thereto 20' or 30', which call Q.",
     "dipende_da": [],
     "figura": {
      "mostra": [
       "terzo piano: nodo K, inclinazione I + Q"
      ],
      "evidenzia": [
       "Q"
      ]
     }
    },
    {
     "id": "L3-P42-p9",
     "la": "",
     "it": "Poi, dai tre luoghi apparenti della cometa osservati già detti, si trovino in questo nuovo piano tre luoghi veri, e l’orbita che passa per quei luoghi, come pure le due aree della medesima descritte fra le osservazioni, che siano δ ed ε, e il tempo totale τ in cui l’area totale δ + ε dovrebbe essere descritta.",
     "en": "Then from the aforesaid three observed apparent places of the comet let the three true places be found in this new plane, as well as the orbit passing through them, and the two areas of the same described between the observation, which call [SVG 1149] and [SVG 925] ; and let [SVG 1166] be the whole time in which the whole area [SVG 1271] should be described.",
     "dipende_da": [],
     "figura": {
      "mostra": [
       "luoghi veri nel terzo piano",
       "conica",
       "aree δ, ε",
       "tempo τ"
      ],
      "evidenzia": [
       "δ",
       "ε",
       "τ"
      ]
     },
     "nota": "In Motte δ, ε, τ e δ + ε sono le formule SVG 1149, 925, 1166, 1271 (tornano con il latino)."
    },
    {
     "id": "L3-P42-p10",
     "la": "",
     "it": "Ora sia C a 1 come A sta a B, e G a 1 come D sta a E, e g a 1 come d sta a e, e γ a 1 come δ sta a ε; e sia S il tempo vero fra la prima e la terza osservazione; e, badando bene ai segni + e −, si cerchino i numeri m e n con questa legge: che sia 2G − 2C = mG − mg + nG − nγ, e 2T − 2S uguale a mT − mt + nT − nτ.",
     "en": "Then taking C to 1 as A to B; and G to 1 as D to E; and g to 1 as d to e; and [SVG 927] to 1 as [SVG 1149] to [SVG 925] ; let S be the true time between the first observation and the third; and, observing well the signs + and -, let such numbers m and n be found out as will make [SVG 1272] ; and [SVG 1273] .",
     "dipende_da": [],
     "figura": {
      "mostra": [
       "rapporti C = A/B, G = D/E, g = d/e, γ = δ/ε",
       "tempi S, T, t, τ",
       "sistema lineare in m, n"
      ],
      "evidenzia": [
       "condizioni da soddisfare: G = C e T = S"
      ]
     },
     "nota": "Il latino ha le formule con il segno invisibile U+2062 fra i fattori. Il fattore 2 a sinistra non è coerente con le correzioni K + mP e I + nQ della frase seguente: vedi nota N2 e la verifica numerica."
    },
    {
     "id": "L3-P42-p11",
     "la": "",
     "it": "E se nell’operazione prima I indica l’inclinazione del piano della traiettoria sul piano dell’eclittica, e K la longitudine dell’uno o dell’altro nodo, I + nQ sarà la vera inclinazione del piano della traiettoria sul piano dell’eclittica, e K + mP la vera longitudine del nodo.",
     "en": "And if, in the first operation, I represents the inclination of the plane of the trajectory to the plane of the ecliptic, and K the longitude of either node, then I + nQ will be the true inclination of the plane of the trajectory to the plane of the ecliptic, and K + mP the true longitude of the node.",
     "dipende_da": [],
     "figura": {
      "mostra": [
       "piano corretto: nodo K + mP, inclinazione I + nQ"
      ],
      "evidenzia": [
       "piano corretto"
      ]
     }
    },
    {
     "id": "L3-P42-p12",
     "la": "",
     "it": "E infine, se nell’operazione prima, seconda e terza le quantità R, r e ρ indicano i lati retti della traiettoria, e le quantità 1/L, 1/l, 1/λ i suoi lati trasversi, rispettivamente, R + mr − mR + nρ − nR sarà il vero lato retto, e 1/(L + ml − mL + nλ − nL) il vero lato trasverso della traiettoria che la cometa descrive.",
     "en": "And, lastly, if in the first, second, and third operations, the quantities R, r, and [SVG 1274] , represent the parameters of the trajectory, and the quantities [SVG 1275] , [SVG 1276] , [SVG 1277] , the transverse diameters of the same, then [SVG 1278] will be the true parameter, and [SVG 1279] will be the true transverse diameter of the trajectory which the comet describes;",
     "dipende_da": [],
     "figura": {
      "mostra": [
       "lati retti R, r, ρ",
       "inversi dei lati trasversi L, l, λ",
       "valori corretti"
      ],
      "evidenzia": [
       "lato retto e lato trasverso corretti"
      ]
     },
     "nota": "La trascrizione appiattisce le frazioni: «1L» = 1/L e «1L+m⁢l-m⁢L+n⁢λ-n⁢L» = 1/(L + ml − mL + nλ − nL), come confermano le formule SVG 1275–1279 di Motte."
    },
    {
     "id": "L3-P42-p13",
     "la": "",
     "it": "Dato poi il lato trasverso, è dato anche il tempo periodico della cometa. C.V.T.",
     "en": "and from the transverse diameter given the periodic time of the comet is also given. Q.E.I.",
     "dipende_da": [],
     "figura": {
      "mostra": [
       "periodo dal lato trasverso (rapporto sesquiplicato)"
      ],
      "evidenzia": []
     },
     "nota": "Il passo dal lato trasverso al periodo usa implicitamente la Prop. XV del Libro I, non citata."
    }
   ],
   "nota": "La proposizione non ha figura; la pagina interattiva può mostrarla come simulazione numerica: tre piani di prova, due condizioni, interpolazione lineare (nota N2). Il fattore 2 delle equazioni di m e n (passo p10) non è coerente con K + mP e I + nQ (p11): segnalato, non corretto."
  },
  {
   "id": "L3-P42-Red1665",
   "tipo": "Calcolo (riduzione di un’osservazione)",
   "titolo": "Cometa del 1665: la posizione del 7 febbraio dalle stelle γ e A",
   "copertura": [
    "III.G8.09"
   ],
   "fonti": {
    "la": "",
    "en": "Motte 1846, sezione corrispondente (due capoversi «In February…» e «From the same observations…»)"
   },
   "figura_base": {
    "punti": [
     "γ (prima dell’Ariete)",
     "A (stella di settima grandezza)",
     "seconda dell’Ariete",
     "cometa"
    ],
    "vincoli": [
     "coordinate eclittiche delle stelle dal testo",
     "triangolo cometa–γ–A rettangolo in γ",
     "cometa–γ = γ–A"
    ]
   },
   "passi": [
    {
     "id": "L3-P42-Red1665-p1",
     "la": "",
     "it": "Nel mese di febbraio dell’anno 1665 appena cominciato, la prima stella dell’Ariete, che nel seguito chiamerò γ, era in ♈ 28° 30′ 15″ con latitudine boreale 7° 8′ 58″.",
     "en": "In February, the beginning of the year 1665, the first star of Aries, which I shall hereafter call [SVG 1169] , was in ♈ 28° 30' 15'', with 7° 8' 58'' north lat.;",
     "dipende_da": [],
     "figura": {
      "mostra": [
       "stella γ (prima dell’Ariete)"
      ],
      "evidenzia": []
     },
     "nota": "Motte chiama la stella [SVG 1169], il cui LaTeX è λ: non torna con il latino (γ), e nel seguito Motte usa γ (SVG 927)."
    },
    {
     "id": "L3-P42-Red1665-p2",
     "la": "",
     "it": "La seconda dell’Ariete era in ♈ 29° 17′ 18″ con latitudine boreale 8° 28′ 16″.",
     "en": "the second star of Aries was in ♈ 29° 17' 18'', with 8° 28' 16'' north lat.;",
     "dipende_da": [],
     "figura": {
      "mostra": [
       "seconda stella dell’Ariete"
      ],
      "evidenzia": []
     }
    },
    {
     "id": "L3-P42-Red1665-p3",
     "la": "",
     "it": "E un’altra stella di settima grandezza, che chiamerò A, era in ♈ 28° 24′ 45″ con latitudine boreale 8° 28′ 33″.",
     "en": "and another star of the seventh magnitude, which I call A, was in ♈ 28° 24' 45'', with 8° 28' 33'' north lat.",
     "dipende_da": [],
     "figura": {
      "mostra": [
       "stella A"
      ],
      "evidenzia": []
     }
    },
    {
     "id": "L3-P42-Red1665-p4",
     "la": "",
     "it": "La cometa poi, il 7 febbraio alle 7h 30′ a Parigi (cioè il 7 febbraio alle 8h 37′ a Danzica), secondo il calendario giuliano, formava con quelle stelle γ e A un triangolo rettangolo in γ.",
     "en": "The comet Feb. 7d. 7h. 30' at Paris (that is, Feb. 7d. 8h. 37' at Dantzick) O. S. made a triangle with those stars [SVG 927] and A, which was right-angled in [SVG 927] ;",
     "dipende_da": [],
     "figura": {
      "mostra": [
       "triangolo cometa–γ–A",
       "angolo retto in γ"
      ],
      "evidenzia": [
       "angolo retto in γ"
      ]
     },
     "nota": "La trascrizione scrive le ore con i segni dei minuti e dei secondi («7d. 7′. 30″», «7d 8′. 37″»); Motte ha 7h. 30' e 8h. 37'."
    },
    {
     "id": "L3-P42-Red1665-p5",
     "la": "",
     "it": "E la distanza della cometa dalla stella γ era uguale alla distanza delle stelle γ e A, cioè 1° 19′ 46″ su un cerchio massimo, e perciò era 1° 20′ 26″ nel parallelo della latitudine della stella γ.",
     "en": "and the distance of the comet from the star [SVG 927] was equal to the distance of the stars [SVG 927] and A, that is, 1° 19' 46'' of a great circle; and therefore in the parallel of the latitude of the star [SVG 927] it was 1° 20' 26''.",
     "dipende_da": [],
     "figura": {
      "mostra": [
       "cerchio massimo γA",
       "parallelo di latitudine di γ"
      ],
      "evidenzia": [
       "cometa–γ = γ–A"
      ]
     },
     "nota": "Verifica: distanza γA su cerchio massimo 1° 19′ 46,2″; nel parallelo di γ 1° 20′ 23,7″ (Newton 1° 20′ 26″). paralello: refuso della trascrizione."
    },
    {
     "id": "L3-P42-Red1665-p6",
     "la": "",
     "it": "Perciò, se dalla longitudine della stella γ si sottrae la longitudine 1° 20′ 26″, resterà la longitudine della cometa ♈ 27° 9′ 49″.",
     "en": "Therefore if from the longitude of the star [SVG 927] there be subducted the longitude 1° 20' 26'', there will remain the longitude of the comet ♈ 27° 9' 49''.",
     "dipende_da": [],
     "figura": {
      "mostra": [
       "longitudine della cometa"
      ],
      "evidenzia": []
     },
     "nota": "28° 30′ 15″ − 1° 20′ 26″ = 27° 9′ 49″: torna."
    },
    {
     "id": "L3-P42-Red1665-p7",
     "la": "",
     "it": "Auzout, da questa sua osservazione, pose la cometa in ♈ 27° 0′ circa.",
     "en": "M. Auzout, from this observation of his, placed the comet in ♈ 27° 0', nearly;",
     "dipende_da": [],
     "figura": {
      "mostra": [],
      "evidenzia": []
     }
    },
    {
     "id": "L3-P42-Red1665-p8",
     "la": "",
     "it": "E secondo lo schema con cui Hooke ne disegnò il moto, essa era allora in ♈ 26° 59′ 24″.",
     "en": "and, by the scheme in which Dr. Hooke delineated its motion, it was then in ♈ 26° 59' 24''.",
     "dipende_da": [],
     "figura": {
      "mostra": [],
      "evidenzia": []
     }
    },
    {
     "id": "L3-P42-Red1665-p9",
     "la": "",
     "it": "Prendendo un valore medio, io l’ho posta in ♈ 27° 4′ 46″.",
     "en": "I place it in ♈ 27° 4' 46'', taking the middle between the two extremes.",
     "dipende_da": [],
     "figura": {
      "mostra": [],
      "evidenzia": [
       "valore medio"
      ]
     },
     "nota": "Motte esplicita «taking the middle between the two extremes». La media degli estremi 27° 9′ 49″ e 26° 59′ 24″ è 27° 4′ 36,5″, non 27° 4′ 46″ (scarto di circa 10″): vedi nota N4."
    },
    {
     "id": "L3-P42-Red1665-p10",
     "la": "",
     "it": "Dalla stessa osservazione Auzout pose la latitudine della cometa a 7° e 4′ o 5′ verso nord.",
     "en": "From the same observations, M. Auzout made the latitude of the comet at that time 7° and 4' or 5' to the north;",
     "dipende_da": [],
     "figura": {
      "mostra": [],
      "evidenzia": []
     },
     "nota": "Motte apre qui un nuovo capoverso."
    },
    {
     "id": "L3-P42-Red1665-p11",
     "la": "",
     "it": "Più correttamente l’avrebbe posta a 7° 3′ 29″, essendo cioè la differenza delle latitudini della cometa e della stella γ uguale alla differenza delle longitudini delle stelle γ e A.",
     "en": "but he had done better to have made it 7° 3' 29'', the difference of the latitudes of the comet and the star [SVG 927] being equal to the difference of the longitude of the stars [SVG 927] and A.",
     "dipende_da": [],
     "figura": {
      "mostra": [
       "differenza di latitudine cometa–γ = differenza di longitudine γ–A"
      ],
      "evidenzia": []
     },
     "nota": "7° 8′ 58″ − 5′ 30″ = 7° 3′ 28″ (Newton 7° 3′ 29″). Nella tabella la trascrizione ha 7.3.25, Motte 7.3.29."
    }
   ],
   "dati": {
    "stelle": {
     "gamma": {
      "long": [
       "♈",
       28,
       30,
       15
      ],
      "lat_bor": [
       7,
       8,
       58
      ]
     },
     "seconda_arietis": {
      "long": [
       "♈",
       29,
       17,
       18
      ],
      "lat_bor": [
       8,
       28,
       16
      ]
     },
     "A": {
      "long": [
       "♈",
       28,
       24,
       45
      ],
      "lat_bor": [
       8,
       28,
       33
      ]
     }
    },
    "verifiche": {
     "gammaA_cerchio_massimo": {
      "testo": [
       1,
       19,
       46
      ],
      "ricalcolo_sec": 4786.2
     },
     "gammaA_parallelo": {
      "testo": [
       1,
       20,
       26
      ],
      "ricalcolo_sec": 4823.7
     },
     "longitudine_cometa": {
      "testo": [
       "♈",
       27,
       9,
       49
      ],
      "ricalcolo": [
       "♈",
       27,
       9,
       49
      ]
     },
     "valore_medio": {
      "testo": [
       "♈",
       27,
       4,
       46
      ],
      "media_estremi": [
       "♈",
       27,
       4,
       36.5
      ],
      "esito": "non torna (10″)"
     },
     "latitudine_corretta": {
      "testo": [
       7,
       3,
       29
      ],
      "ricalcolo": [
       7,
       3,
       28
      ]
     }
    }
   },
   "nota": "Calcolo di trigonometria sferica che una pagina può mostrare sul globo celeste. Motte divide il periodo in due capoversi; per il passo p1 la sua lettera [SVG 1169] è λ, non γ."
  },
  {
   "id": "L3-P42-Tab1665",
   "tipo": "Tabella",
   "titolo": "Cometa del 1664–1665: luoghi osservati e calcolati da Halley",
   "copertura": [
    "III.G8.07",
    "III.G8.08",
    "III.G8.14"
   ],
   "fonti": {
    "la": "",
    "en": "Motte 1846, sezione corrispondente"
   },
   "enunciato": {
    "la": "",
    "it": "Quanto bene i luoghi della cometa calcolati in questa orbita concordino con le osservazioni, risulterà dalla tabella seguente, calcolata da Halley.",
    "en": "And how nearly the places of the comet computed in this orbit agree with the observations, will appear from the annexed table, calculated by Dr. Halley."
   },
   "passi": [],
   "dati": {
    "colonne": [
     "data",
     "ora (h.′, ½ = mezzo minuto)",
     "long. osservata [segno, °, ′, ″]",
     "lat. osservata [°, ′, ″]",
     "long. calcolata",
     "lat. calcolata"
    ],
    "righe": [
     {
      "data": "Dic. 3",
      "ora": "18.29½",
      "long_oss": [
       "♎",
       7,
       1,
       0
      ],
      "lat": "austr.",
      "lat_oss": [
       21,
       39,
       0
      ],
      "long_calc": [
       "♎",
       7,
       1,
       29
      ],
      "lat_calc": [
       21,
       38,
       50
      ]
     },
     {
      "data": "4",
      "ora": "18.1½",
      "long_oss": [
       "♎",
       6,
       15,
       0
      ],
      "lat": "austr.",
      "lat_oss": [
       22,
       24,
       0
      ],
      "long_calc": [
       "♎",
       6,
       16,
       5
      ],
      "lat_calc": [
       22,
       24,
       0
      ]
     },
     {
      "data": "7",
      "ora": "17.48½",
      "long_oss": [
       "♎",
       3,
       6,
       0
      ],
      "lat": "austr.",
      "lat_oss": [
       25,
       22,
       0
      ],
      "long_calc": [
       "♎",
       3,
       7,
       33
      ],
      "lat_calc": [
       25,
       21,
       40
      ]
     },
     {
      "data": "17",
      "ora": "14.43½",
      "long_oss": [
       "♌",
       2,
       56,
       0
      ],
      "lat": "austr.",
      "lat_oss": [
       49,
       25,
       0
      ],
      "long_calc": [
       "♌",
       2,
       56,
       0
      ],
      "lat_calc": [
       49,
       25,
       0
      ]
     },
     {
      "data": "19",
      "ora": "9.25½",
      "long_oss": [
       "♊",
       28,
       40,
       30
      ],
      "lat": "austr.",
      "lat_oss": [
       45,
       48,
       0
      ],
      "long_calc": [
       "♊",
       28,
       43,
       0
      ],
      "lat_calc": [
       45,
       46,
       0
      ]
     },
     {
      "data": "20",
      "ora": "9.53½",
      "long_oss": [
       "♊",
       13,
       3,
       0
      ],
      "lat": "austr.",
      "lat_oss": [
       39,
       54,
       0
      ],
      "long_calc": [
       "♊",
       13,
       5,
       0
      ],
      "lat_calc": [
       39,
       53,
       0
      ]
     },
     {
      "data": "21",
      "ora": "9.9½",
      "long_oss": [
       "♊",
       2,
       16,
       0
      ],
      "lat": "austr.",
      "lat_oss": [
       33,
       41,
       0
      ],
      "long_calc": [
       "♊",
       2,
       18,
       30
      ],
      "lat_calc": [
       33,
       39,
       40
      ]
     },
     {
      "data": "22",
      "ora": "9.0½",
      "long_oss": [
       "♉",
       24,
       24,
       0
      ],
      "lat": "austr.",
      "lat_oss": [
       27,
       45,
       0
      ],
      "long_calc": [
       "♉",
       24,
       27,
       0
      ],
      "lat_calc": [
       27,
       46,
       0
      ]
     },
     {
      "data": "26",
      "ora": "7.58½",
      "long_oss": [
       "♉",
       9,
       0,
       0
      ],
      "lat": "austr.",
      "lat_oss": [
       12,
       36,
       0
      ],
      "long_calc": [
       "♉",
       9,
       2,
       28
      ],
      "lat_calc": [
       12,
       34,
       13
      ]
     },
     {
      "data": "27",
      "ora": "6.45 [01′]",
      "long_oss": [
       "♉",
       7,
       5,
       40
      ],
      "lat": "austr.",
      "lat_oss": [
       10,
       23,
       0
      ],
      "long_calc": [
       "♉",
       7,
       8,
       54
      ],
      "lat_calc": [
       10,
       23,
       13
      ]
     },
     {
      "data": "28",
      "ora": "7.39½",
      "long_oss": [
       "♉",
       5,
       24,
       45
      ],
      "lat": "austr.",
      "lat_oss": [
       8,
       22,
       50
      ],
      "long_calc": [
       "♉",
       5,
       27,
       52
      ],
      "lat_calc": [
       8,
       23,
       37
      ]
     },
     {
      "data": "31",
      "ora": "6.45½",
      "long_oss": [
       "♉",
       2,
       7,
       40
      ],
      "lat": "austr.",
      "lat_oss": [
       4,
       13,
       0
      ],
      "long_calc": [
       "♉",
       2,
       8,
       20
      ],
      "lat_calc": [
       4,
       16,
       25
      ]
     },
     {
      "data": "Gen. 1665, 7",
      "ora": "7.37½",
      "long_oss": [
       "♈",
       28,
       24,
       47
      ],
      "lat": "bor.",
      "lat_oss": [
       0,
       54,
       0
      ],
      "long_calc": [
       "♈",
       28,
       24,
       0
      ],
      "lat_calc": [
       0,
       53,
       0
      ]
     },
     {
      "data": "13",
      "ora": "7.0½",
      "long_oss": [
       "♈",
       27,
       6,
       54
      ],
      "lat": "bor.",
      "lat_oss": [
       3,
       6,
       50
      ],
      "long_calc": [
       "♈",
       27,
       6,
       39
      ],
      "lat_calc": [
       3,
       7,
       40
      ]
     },
     {
      "data": "24",
      "ora": "7.29½",
      "long_oss": [
       "♈",
       26,
       29,
       15
      ],
      "lat": "bor.",
      "lat_oss": [
       5,
       25,
       50
      ],
      "long_calc": [
       "♈",
       26,
       28,
       50
      ],
      "lat_calc": [
       5,
       26,
       0
      ]
     },
     {
      "data": "Feb. 7",
      "ora": "8.37½",
      "long_oss": [
       "♈",
       27,
       4,
       46
      ],
      "lat": "bor.",
      "lat_oss": [
       7,
       3,
       25
      ],
      "long_calc": [
       "♈",
       27,
       24,
       55
      ],
      "lat_calc": [
       7,
       3,
       15
      ]
     },
     {
      "data": "22",
      "ora": "8.46½",
      "long_oss": [
       "♈",
       28,
       29,
       46
      ],
      "lat": "bor.",
      "lat_oss": [
       8,
       12,
       36
      ],
      "long_calc": [
       "♈",
       28,
       29,
       58
      ],
      "lat_calc": [
       8,
       10,
       25
      ]
     },
     {
      "data": "Mar. 1",
      "ora": "8.16½",
      "long_oss": [
       "♈",
       29,
       18,
       15
      ],
      "lat": "bor.",
      "lat_oss": [
       8,
       36,
       26
      ],
      "long_calc": [
       "♈",
       29,
       18,
       20
      ],
      "lat_calc": [
       8,
       36,
       12
      ]
     },
     {
      "data": "7",
      "ora": "8.37½",
      "long_oss": [
       "♉",
       0,
       2,
       48
      ],
      "lat": "bor.",
      "lat_oss": [
       8,
       56,
       30
      ],
      "long_calc": [
       "♉",
       0,
       2,
       42
      ],
      "lat_calc": [
       8,
       56,
       56
      ]
     }
    ],
    "elementi_Halley": {
     "nodo_asc": [
      "♊",
      21,
      13,
      55
     ],
     "inclinazione": [
      21,
      18,
      40
     ],
     "perielio_dal_nodo": [
      49,
      27,
      30
     ],
     "perielio": [
      "♌",
      8,
      40,
      30
     ],
     "lat_perielio_austr": [
      16,
      1,
      45
     ],
     "latus_rectum": 410286,
     "unita": 100000
    },
    "controlli": {
     "scarti_long_calc_meno_oss_primi": {
      "Dic3": 0.48,
      "Dic4": 1.08,
      "Dic7": 1.55,
      "Dic17": 0.0,
      "Dic19": 2.5,
      "Dic20": 2.0,
      "Dic21": 2.5,
      "Dic22": 3.0,
      "Dic26": 2.47,
      "Dic27": 3.23,
      "Dic28": 3.12,
      "Dic31": 0.67,
      "Gen7": -0.78,
      "Gen13": -0.25,
      "Gen24": -0.42,
      "Feb7": 20.15,
      "Feb22": 0.2,
      "Mar1": 0.08,
      "Mar7": -0.1
     },
     "anomalie": [
      "Feb. 7 long. calcolata 27.24.55: scarto 20′ (probabile 27.4.55)",
      "Feb. 7 lat. osservata 7.3.25 (testo e Motte 7.3.29)",
      "Dic. 27 ora 06h.45⁤01′"
     ],
     "perielio_ricalcolato": {
      "long": [
       "♌",
       8,
       40,
       35
      ],
      "lat": [
       16,
       1,
       57
      ]
     }
    }
   },
   "nota": "La tabella non ha la colonna delle differenze; gli scarti sono ricalcolati (nota N5). Nella trascrizione le celle sono spezzate una per riga."
  },
  {
   "id": "L3-P42-Tab1683",
   "tipo": "Tabella",
   "titolo": "Cometa del 1683: luoghi calcolati da Halley e osservati da Flamsteed",
   "copertura": [
    "III.G8.15",
    "III.G8.16"
   ],
   "fonti": {
    "la": "",
    "en": "Motte 1846, sezione corrispondente"
   },
   "enunciato": {
    "la": "",
    "it": "I luoghi della cometa calcolati da Halley in questa orbita e confrontati con i luoghi osservati da Flamsteed sono esposti nella tabella seguente.",
    "en": "And the places thereof, computed by Dr. Halley in this orbit, are compared with the places of the same observed by Mr. Flamsted, in the following table:—"
   },
   "passi": [],
   "dati": {
    "nota": "[segno, °, ′, ″] dove il segno zodiacale è scritto nella tabella; altrimenti vale quello della riga precedente; dalla riga Ago. 22 le latitudini sono australi; differenze in secondi, osservato − calcolato (per le latitudini australi |oss| − |calc|)",
    "righe": [
     {
      "data": "Lug. 13.12.55",
      "sole": [
       "♌",
       1,
       2,
       30
      ],
      "long_calc": [
       "♋",
       13,
       5,
       42
      ],
      "lat_calc": [
       29,
       28,
       13
      ],
      "long_oss": [
       "♋",
       13,
       6,
       42
      ],
      "lat_oss": [
       29,
       28,
       20
      ],
      "diff_long_sec": 60,
      "diff_lat_sec": 7
     },
     {
      "data": "15.11.15",
      "sole": [
       2,
       53,
       12
      ],
      "long_calc": [
       11,
       37,
       48
      ],
      "lat_calc": [
       29,
       34,
       0
      ],
      "long_oss": [
       11,
       39,
       43
      ],
      "lat_oss": [
       29,
       34,
       50
      ],
      "diff_long_sec": 115,
      "diff_lat_sec": 50
     },
     {
      "data": "17.10.20",
      "sole": [
       4,
       45,
       45
      ],
      "long_calc": [
       10,
       7,
       6
      ],
      "lat_calc": [
       29,
       33,
       30
      ],
      "long_oss": [
       10,
       8,
       40
      ],
      "lat_oss": [
       29,
       34,
       0
      ],
      "diff_long_sec": 94,
      "diff_lat_sec": 30
     },
     {
      "data": "23.13.40",
      "sole": [
       10,
       38,
       21
      ],
      "long_calc": [
       5,
       10,
       27
      ],
      "lat_calc": [
       28,
       51,
       42
      ],
      "long_oss": [
       5,
       11,
       30
      ],
      "lat_oss": [
       28,
       50,
       28
      ],
      "diff_long_sec": 63,
      "diff_lat_sec": -74
     },
     {
      "data": "25.14.5",
      "sole": [
       12,
       35,
       28
      ],
      "long_calc": [
       3,
       27,
       53
      ],
      "lat_calc": [
       24,
       24,
       47
      ],
      "long_oss": [
       3,
       27,
       0
      ],
      "lat_oss": [
       28,
       23,
       40
      ],
      "diff_long_sec": -53,
      "diff_lat_sec": -67
     },
     {
      "data": "31.9.42",
      "sole": [
       18,
       9,
       22
      ],
      "long_calc": [
       "♊",
       27,
       55,
       3
      ],
      "lat_calc": [
       26,
       22,
       52
      ],
      "long_oss": [
       "♊",
       27,
       54,
       24
      ],
      "lat_oss": [
       26,
       22,
       25
      ],
      "diff_long_sec": -39,
      "diff_lat_sec": -27
     },
     {
      "data": "31.14.55",
      "sole": [
       18,
       21,
       53
      ],
      "long_calc": [
       27,
       41,
       7
      ],
      "lat_calc": [
       26,
       16,
       57
      ],
      "long_oss": [
       27,
       41,
       8
      ],
      "lat_oss": [
       26,
       14,
       50
      ],
      "diff_long_sec": 1,
      "diff_lat_sec": -127
     },
     {
      "data": "Ago. 2.14.56",
      "sole": [
       20,
       17,
       16
      ],
      "long_calc": [
       25,
       29,
       32
      ],
      "lat_calc": [
       25,
       16,
       19
      ],
      "long_oss": [
       25,
       28,
       46
      ],
      "lat_oss": [
       25,
       17,
       28
      ],
      "diff_long_sec": -46,
      "diff_lat_sec": 69
     },
     {
      "data": "4.10.49",
      "sole": [
       22,
       2,
       50
      ],
      "long_calc": [
       23,
       18,
       20
      ],
      "lat_calc": [
       24,
       10,
       49
      ],
      "long_oss": [
       23,
       16,
       55
      ],
      "lat_oss": [
       24,
       12,
       19
      ],
      "diff_long_sec": -85,
      "diff_lat_sec": 90
     },
     {
      "data": "6.10.9",
      "sole": [
       23,
       56,
       45
      ],
      "long_calc": [
       20,
       42,
       23
      ],
      "lat_calc": [
       22,
       47,
       5
      ],
      "long_oss": [
       20,
       40,
       32
      ],
      "lat_oss": [
       22,
       49,
       5
      ],
      "diff_long_sec": -111,
      "diff_lat_sec": 120
     },
     {
      "data": "9.10.26",
      "sole": [
       26,
       50,
       52
      ],
      "long_calc": [
       16,
       7,
       57
      ],
      "lat_calc": [
       20,
       6,
       37
      ],
      "long_oss": [
       16,
       5,
       55
      ],
      "lat_oss": [
       20,
       6,
       10
      ],
      "diff_long_sec": -122,
      "diff_lat_sec": -27
     },
     {
      "data": "15.14.1",
      "sole": [
       "♍",
       2,
       47,
       13
      ],
      "long_calc": [
       3,
       30,
       48
      ],
      "lat_calc": [
       11,
       37,
       33
      ],
      "long_oss": [
       3,
       26,
       18
      ],
      "lat_oss": [
       11,
       32,
       1
      ],
      "diff_long_sec": -270,
      "diff_lat_sec": -332
     },
     {
      "data": "16.15.10",
      "sole": [
       3,
       48,
       2
      ],
      "long_calc": [
       0,
       43,
       7
      ],
      "lat_calc": [
       9,
       34,
       16
      ],
      "long_oss": [
       0,
       41,
       55
      ],
      "lat_oss": [
       9,
       34,
       13
      ],
      "diff_long_sec": -72,
      "diff_lat_sec": -3
     },
     {
      "data": "18.15.44",
      "sole": [
       5,
       45,
       33
      ],
      "long_calc": [
       "♉",
       24,
       52,
       53
      ],
      "lat_calc": [
       5,
       11,
       15
      ],
      "long_oss": [
       "♉",
       24,
       49,
       5
      ],
      "lat_oss": [
       5,
       9,
       11
      ],
      "diff_long_sec": -228,
      "diff_lat_sec": -124
     },
     {
      "data": "22.14.44",
      "sole": [
       9,
       35,
       49
      ],
      "long_calc": [
       11,
       7,
       14
      ],
      "lat_calc": [
       5,
       16,
       53
      ],
      "long_oss": [
       11,
       7,
       12
      ],
      "lat_oss": [
       5,
       16,
       50
      ],
      "diff_long_sec": -2,
      "diff_lat_sec": -3
     },
     {
      "data": "23.15.52",
      "sole": [
       10,
       36,
       48
      ],
      "long_calc": [
       7,
       2,
       18
      ],
      "lat_calc": [
       8,
       17,
       9
      ],
      "long_oss": [
       7,
       1,
       17
      ],
      "lat_oss": [
       8,
       16,
       41
      ],
      "diff_long_sec": -61,
      "diff_lat_sec": -28
     },
     {
      "data": "26.16.2",
      "sole": [
       13,
       31,
       10
      ],
      "long_calc": [
       "♈",
       24,
       45,
       31
      ],
      "lat_calc": [
       16,
       38,
       0
      ],
      "long_oss": [
       "♈",
       24,
       44,
       0
      ],
      "lat_oss": [
       16,
       38,
       20
      ],
      "diff_long_sec": -91,
      "diff_lat_sec": 20
     }
    ],
    "elementi": {
     "nodo_asc": [
      "♍",
      23,
      23
     ],
     "inclinazione": [
      83,
      11
     ],
     "perielio": [
      "♊",
      25,
      29,
      30
     ],
     "q": 56020,
     "unita": 100000,
     "perielio_tempo": "Lug. 2d 3h 50′"
    },
    "controlli": {
     "righe_che_tornano": 16,
     "righe": 17,
     "anomalia": "Lug. 25 lat. calcolata 24.24.47 (richiesta 28.24.47)"
    }
   }
  },
  {
   "id": "L3-P42-Tab1682",
   "tipo": "Tabella",
   "titolo": "Cometa del 1682: luoghi dalle osservazioni di Flamsteed e dalla teoria",
   "copertura": [
    "III.G8.17",
    "III.G8.18"
   ],
   "fonti": {
    "la": "",
    "en": "Motte 1846, sezione corrispondente"
   },
   "enunciato": {
    "la": "",
    "it": "I luoghi calcolati dalle osservazioni di Flamsteed e confrontati con i luoghi calcolati con la teoria sono esposti nella tabella seguente.",
    "en": "And its places, collected from Mr. Flamsted's observations, are compared with its places computed from our theory in the following table:—"
   },
   "passi": [],
   "dati": {
    "nota": "differenze in secondi, calcolato − osservato",
    "righe": [
     {
      "data": "Ago. 19.16.38",
      "sole": [
       "♍",
       7,
       0,
       7
      ],
      "long_calc": [
       "♌",
       18,
       14,
       28
      ],
      "lat_calc": [
       25,
       50,
       7
      ],
      "long_oss": [
       "♌",
       18,
       14,
       40
      ],
      "lat_oss": [
       25,
       49,
       55
      ],
      "diff_long_sec": -12,
      "diff_lat_sec": 12
     },
     {
      "data": "20.15.38",
      "sole": [
       7,
       55,
       52
      ],
      "long_calc": [
       24,
       46,
       23
      ],
      "lat_calc": [
       26,
       14,
       42
      ],
      "long_oss": [
       24,
       46,
       22
      ],
      "lat_oss": [
       26,
       12,
       52
      ],
      "diff_long_sec": 1,
      "diff_lat_sec": 110
     },
     {
      "data": "21.8.21",
      "sole": [
       8,
       36,
       14
      ],
      "long_calc": [
       29,
       37,
       15
      ],
      "lat_calc": [
       26,
       20,
       3
      ],
      "long_oss": [
       29,
       38,
       2
      ],
      "lat_oss": [
       26,
       17,
       37
      ],
      "diff_long_sec": -47,
      "diff_lat_sec": 146
     },
     {
      "data": "22.8.8",
      "sole": [
       9,
       33,
       55
      ],
      "long_calc": [
       "♍",
       6,
       29,
       53
      ],
      "lat_calc": [
       26,
       8,
       42
      ],
      "long_oss": [
       "♍",
       6,
       30,
       3
      ],
      "lat_oss": [
       26,
       7,
       12
      ],
      "diff_long_sec": -10,
      "diff_lat_sec": 90
     },
     {
      "data": "29.8.20",
      "sole": [
       16,
       22,
       40
      ],
      "long_calc": [
       "♎",
       12,
       37,
       54
      ],
      "lat_calc": [
       18,
       37,
       47
      ],
      "long_oss": [
       "♎",
       12,
       37,
       49
      ],
      "lat_oss": [
       18,
       34,
       5
      ],
      "diff_long_sec": 5,
      "diff_lat_sec": 222
     },
     {
      "data": "30.7.45",
      "sole": [
       17,
       19,
       41
      ],
      "long_calc": [
       15,
       36,
       1
      ],
      "lat_calc": [
       17,
       26,
       43
      ],
      "long_oss": [
       15,
       35,
       18
      ],
      "lat_oss": [
       17,
       27,
       17
      ],
      "diff_long_sec": 43,
      "diff_lat_sec": -34
     },
     {
      "data": "Set. 1.7.33",
      "sole": [
       19,
       16,
       9
      ],
      "long_calc": [
       20,
       30,
       53
      ],
      "lat_calc": [
       15,
       13,
       0
      ],
      "long_oss": [
       20,
       27,
       4
      ],
      "lat_oss": [
       15,
       9,
       49
      ],
      "diff_long_sec": 229,
      "diff_lat_sec": 191
     },
     {
      "data": "4.7.22",
      "sole": [
       22,
       11,
       28
      ],
      "long_calc": [
       25,
       42,
       0
      ],
      "lat_calc": [
       12,
       23,
       48
      ],
      "long_oss": [
       25,
       40,
       58
      ],
      "lat_oss": [
       12,
       22,
       0
      ],
      "diff_long_sec": 62,
      "diff_lat_sec": 108
     },
     {
      "data": "5.7.32",
      "sole": [
       23,
       10,
       29
      ],
      "long_calc": [
       27,
       0,
       46
      ],
      "lat_calc": [
       11,
       33,
       8
      ],
      "long_oss": [
       26,
       59,
       24
      ],
      "lat_oss": [
       11,
       33,
       51
      ],
      "diff_long_sec": 82,
      "diff_lat_sec": -43
     },
     {
      "data": "8.7.16",
      "sole": [
       26,
       5,
       58
      ],
      "long_calc": [
       29,
       58,
       44
      ],
      "lat_calc": [
       9,
       26,
       46
      ],
      "long_oss": [
       29,
       58,
       45
      ],
      "lat_oss": [
       9,
       26,
       43
      ],
      "diff_long_sec": -1,
      "diff_lat_sec": 3
     },
     {
      "data": "9.7.26",
      "sole": [
       27,
       5,
       9
      ],
      "long_calc": [
       "♏",
       0,
       44,
       10
      ],
      "lat_calc": [
       8,
       49,
       10
      ],
      "long_oss": [
       "♏",
       0,
       44,
       4
      ],
      "lat_oss": [
       8,
       48,
       25
      ],
      "diff_long_sec": 6,
      "diff_lat_sec": 45
     }
    ],
    "elementi": {
     "nodo_asc": [
      "♉",
      21,
      16,
      30
     ],
     "inclinazione": [
      17,
      56,
      0
     ],
     "perielio": [
      "♒",
      2,
      52,
      50
     ],
     "q": 58328,
     "unita": 100000,
     "perielio_tempo": "Set. 4d 7h 39′"
    },
    "controlli": {
     "righe_che_tornano": 11,
     "righe": 11
    }
   }
  },
  {
   "id": "L3-P42-Tab1723",
   "tipo": "Tabella",
   "titolo": "Cometa del 1723: luoghi osservati e calcolati da Bradley",
   "copertura": [
    "III.G8.19",
    "III.G8.20"
   ],
   "fonti": {
    "la": "",
    "en": "Motte 1846, sezione corrispondente"
   },
   "enunciato": {
    "la": "",
    "it": "I luoghi della cometa calcolati da Bradley in questa orbita e confrontati con i luoghi osservati da lui stesso, da suo zio, il signor Pound, e dal signor Halley sono esposti nella tabella seguente.",
    "en": "The places of this comet computed in this orbit by Mr. Bradley, and compared with the places observed by himself, his uncle Mr. Pound, and Dr. Halley, may be seen in the following table."
   },
   "passi": [],
   "dati": {
    "righe": [
     {
      "data": "Ott. 9.8.5",
      "long_oss": [
       "♒",
       7,
       22,
       15
      ],
      "lat_oss": [
       5,
       2,
       0
      ],
      "long_calc": [
       "♒",
       7,
       21,
       26
      ],
      "lat_calc": [
       5,
       2,
       47
      ],
      "diff_long_sec": 49,
      "diff_lat_sec": -47
     },
     {
      "data": "10.6.21",
      "long_oss": [
       6,
       41,
       12
      ],
      "lat_oss": [
       7,
       44,
       13
      ],
      "long_calc": [
       6,
       41,
       42
      ],
      "lat_calc": [
       7,
       43,
       18
      ],
      "diff_long_sec": -50,
      "diff_lat_sec": 55
     },
     {
      "data": "12.7.22",
      "long_oss": [
       5,
       39,
       58
      ],
      "lat_oss": [
       11,
       55,
       0
      ],
      "long_calc": [
       5,
       40,
       19
      ],
      "lat_calc": [
       11,
       54,
       55
      ],
      "diff_long_sec": -21,
      "diff_lat_sec": 5
     },
     {
      "data": "14.8.57",
      "long_oss": [
       4,
       59,
       49
      ],
      "lat_oss": [
       14,
       43,
       50
      ],
      "long_calc": [
       5,
       0,
       37
      ],
      "lat_calc": [
       14,
       44,
       1
      ],
      "diff_long_sec": -48,
      "diff_lat_sec": -11
     },
     {
      "data": "15.6.35",
      "long_oss": [
       4,
       47,
       41
      ],
      "lat_oss": [
       15,
       40,
       51
      ],
      "long_calc": [
       4,
       47,
       45
      ],
      "lat_calc": [
       15,
       40,
       55
      ],
      "diff_long_sec": -4,
      "diff_lat_sec": -4
     },
     {
      "data": "21.6.22",
      "long_oss": [
       4,
       2,
       32
      ],
      "lat_oss": [
       19,
       41,
       49
      ],
      "long_calc": [
       4,
       2,
       21
      ],
      "lat_calc": [
       19,
       42,
       3
      ],
      "diff_long_sec": 11,
      "diff_lat_sec": -14
     },
     {
      "data": "22.6.24",
      "long_oss": [
       3,
       59,
       2
      ],
      "lat_oss": [
       20,
       8,
       12
      ],
      "long_calc": [
       3,
       59,
       10
      ],
      "lat_calc": [
       20,
       8,
       17
      ],
      "diff_long_sec": -8,
      "diff_lat_sec": -5
     },
     {
      "data": "24.8.2",
      "long_oss": [
       3,
       55,
       29
      ],
      "lat_oss": [
       20,
       55,
       18
      ],
      "long_calc": [
       3,
       55,
       11
      ],
      "lat_calc": [
       20,
       55,
       9
      ],
      "diff_long_sec": 18,
      "diff_lat_sec": 9
     },
     {
      "data": "29.8.56",
      "long_oss": [
       3,
       56,
       17
      ],
      "lat_oss": [
       22,
       20,
       27
      ],
      "long_calc": [
       3,
       56,
       42
      ],
      "lat_calc": [
       22,
       20,
       10
      ],
      "diff_long_sec": -25,
      "diff_lat_sec": 17
     },
     {
      "data": "30.6.20",
      "long_oss": [
       3,
       58,
       9
      ],
      "lat_oss": [
       22,
       32,
       28
      ],
      "long_calc": [
       3,
       58,
       17
      ],
      "lat_calc": [
       22,
       32,
       12
      ],
      "diff_long_sec": -8,
      "diff_lat_sec": 16
     },
     {
      "data": "Nov. 5.5.53",
      "long_oss": [
       4,
       16,
       30
      ],
      "lat_oss": [
       23,
       38,
       33
      ],
      "long_calc": [
       4,
       16,
       23
      ],
      "lat_calc": [
       23,
       38,
       7
      ],
      "diff_long_sec": 7,
      "diff_lat_sec": 26
     },
     {
      "data": "8.7.6",
      "long_oss": [
       4,
       29,
       36
      ],
      "lat_oss": [
       24,
       4,
       30
      ],
      "long_calc": [
       4,
       29,
       34
      ],
      "lat_calc": [
       24,
       4,
       40
      ],
      "diff_long_sec": -18,
      "diff_lat_sec": -10
     },
     {
      "data": "14.6.20",
      "long_oss": [
       5,
       2,
       16
      ],
      "lat_oss": [
       24,
       48,
       46
      ],
      "long_calc": [
       5,
       2,
       21
      ],
      "lat_calc": [
       24,
       48,
       16
      ],
      "diff_long_sec": -35,
      "diff_lat_sec": 30
     },
     {
      "data": "20.7.45",
      "long_oss": [
       5,
       42,
       20
      ],
      "lat_oss": [
       25,
       24,
       45
      ],
      "long_calc": [
       5,
       43,
       13
      ],
      "lat_calc": [
       25,
       25,
       17
      ],
      "diff_long_sec": -53,
      "diff_lat_sec": -32
     },
     {
      "data": "Dic. 7.6.45",
      "long_oss": [
       8,
       4,
       13
      ],
      "lat_oss": [
       26,
       54,
       18
      ],
      "long_calc": [
       8,
       3,
       55
      ],
      "lat_calc": [
       26,
       53,
       42
      ],
      "diff_long_sec": 18,
      "diff_lat_sec": 36
     }
    ],
    "elementi": {
     "nodo_asc": [
      "♈",
      14,
      16
     ],
     "inclinazione": [
      49,
      59
     ],
     "perielio": [
      "♉",
      12,
      15,
      20
     ],
     "q": 998651,
     "unita": 1000000,
     "perielio_tempo": "Set. 16d 16h 10′"
    },
    "controlli": {
     "righe_che_tornano": 12,
     "righe": 15,
     "anomalie": [
      "Ott. 10: −30″ dai valori, −50″ in tabella",
      "Nov. 8: long. calcolata 4.29.34 (Motte 4.29.54, coerente con −18″)",
      "Nov. 14: long. calcolata 5.2.21 (Motte 5.2.51, coerente con −35″)"
     ]
    }
   }
  },
  {
   "id": "L3-P42-Cometa1607",
   "tipo": "Calcolo",
   "titolo": "La cometa del 1607 e del 1682: periodo di 75 anni, asse maggiore, distanza afelia",
   "copertura": [
    "III.G8.22"
   ],
   "fonti": {
    "la": "",
    "en": "Motte 1846, sezione corrispondente"
   },
   "enunciato": {
    "la": "",
    "it": "Questa orbita concorda con ottima approssimazione con l’orbita della cometa che apparve nell’anno 1682.",
    "en": "which orbit agrees very nearly with the orbit of the comet which was seen in 1682."
   },
   "passi": [],
   "dati": {
    "elementi_1607": {
     "nodo_asc": [
      "♉",
      20,
      21
     ],
     "inclinazione": [
      17,
      2
     ],
     "perielio": [
      "♒",
      2,
      16
     ],
     "q": 58680,
     "unita": 100000,
     "perielio_tempo": "Ott. 16d 3h 50′"
    },
    "elementi_1682": {
     "nodo_asc": [
      "♉",
      21,
      16,
      30
     ],
     "inclinazione": [
      17,
      56,
      0
     ],
     "perielio": [
      "♒",
      2,
      52,
      50
     ],
     "q": 58328,
     "unita": 100000
    },
    "periodo_anni": 75,
    "asse_maggiore_testo": [
     1778,
     100
    ],
    "asse_maggiore_ricalcolo": 17.784,
    "afelio_testo": 35,
    "afelio_ricalcolo": 34.98
   },
   "nota": "Il calcolo usa il rapporto sesquiplicato (Libro I, Prop. XV), non citato (nota N7)."
  },
  {
   "id": "L3-SchGen",
   "tipo": "Scholium",
   "titolo": "Scolio generale",
   "copertura": [
    "III.G9.01",
    "III.G9.02",
    "III.G9.03",
    "III.G9.04",
    "III.G9.05",
    "III.G9.06",
    "III.G9.07",
    "III.G9.08",
    "III.G9.09",
    "III.G9.10",
    "III.G9.11",
    "III.G9.12",
    "III.G9.13",
    "III.G9.14",
    "III.G9.15"
   ],
   "fonti": {
    "la": "",
    "en": "Motte 1846, sezione corrispondente (General Scholium)"
   },
   "passi": [
    {
     "id": "L3-SchGen-p1",
     "la": "",
     "it": "L’ipotesi dei vortici è gravata da molte difficoltà.",
     "en": "The hypothesis of vortices is pressed with many difficulties.",
     "dipende_da": [],
     "figura": {
      "mostra": [
       "Sole",
       "vortice"
      ],
      "evidenzia": []
     }
    },
    {
     "id": "L3-SchGen-p2",
     "la": "",
     "it": "Perché ogni pianeta, con il raggio condotto al Sole, descriva aree proporzionali al tempo, i tempi periodici delle parti del vortice dovrebbero essere in rapporto duplicato delle distanze dal Sole.",
     "en": "That every planet by a radius drawn to the sun may describe areas proportional to the times of description, the periodic times of the several parts of the vortices should observe the duplicate proportion of their distances from the sun;",
     "dipende_da": [],
     "figura": {
      "mostra": [
       "strati del vortice a distanze diverse",
       "legge delle aree"
      ],
      "evidenzia": [
       "periodi ∝ distanza²"
      ]
     },
     "nota": "Libro I, Prop. I e II (legge delle aree) e Libro II, Sez. IX non sono citati. Verifica: velocità areale costante ⇒ periodo ∝ r²."
    },
    {
     "id": "L3-SchGen-p3",
     "la": "",
     "it": "Perché i tempi periodici dei pianeti siano nella proporzione sesquiplicata delle distanze dal Sole, i tempi periodici delle parti del vortice dovrebbero essere nella proporzione sesquiplicata delle distanze.",
     "en": "but that the periodic times of the planets may obtain the sesquiplicate proportion of their distances from the sun, the periodic times of the parts of the vortex ought to be in the sesquiplicate proportion of their distances.",
     "dipende_da": [],
     "figura": {
      "mostra": [
       "periodi dei pianeti"
      ],
      "evidenzia": [
       "periodi ∝ distanza^(3/2)",
       "contraddizione con il passo precedente"
      ]
     },
     "nota": "Il latino include il marcatore di pagina <527>; Motte unisce questa frase alla precedente con «but»."
    },
    {
     "id": "L3-SchGen-p4",
     "la": "",
     "it": "Perché i vortici minori fatti girare attorno a Saturno, a Giove e agli altri pianeti si conservino e nuotino tranquillamente nel vortice del Sole, i tempi periodici delle parti del vortice solare dovrebbero essere uguali.",
     "en": "That the smaller vortices may maintain their lesser revolutions about Saturn, Jupiter, and other planets, and swim quietly and undisturbed in the greater vortex of the sun, the periodic times of the parts of the sun's vortex should be equal;",
     "dipende_da": [],
     "figura": {
      "mostra": [
       "vortici minori di Giove e Saturno dentro il vortice solare"
      ],
      "evidenzia": [
       "periodi uguali: terza richiesta incompatibile"
      ]
     }
    },
    {
     "id": "L3-SchGen-p5",
     "la": "",
     "it": "Le rivoluzioni del Sole e dei pianeti attorno ai propri assi, che dovrebbero accordarsi con i moti dei vortici, si discostano da tutte queste proporzioni.",
     "en": "but the rotation of the sun and planets about their axes, which ought to correspond with the motions of their vortices, recede far from all these proportions.",
     "dipende_da": [],
     "figura": {
      "mostra": [
       "rotazioni del Sole e dei pianeti"
      ],
      "evidenzia": []
     },
     "nota": "Motte «rotation», al singolare; aggiunge «far»."
    },
    {
     "id": "L3-SchGen-p6",
     "la": "",
     "it": "I moti delle comete sono sommamente regolari, osservano le stesse leggi dei moti dei pianeti, e non possono essere spiegati per mezzo dei vortici.",
     "en": "The motions of the comets are exceedingly regular, are governed by the same laws with the motions of the planets, and can by no means be accounted for by the hypothesis of vortices;",
     "dipende_da": [],
     "figura": {
      "mostra": [
       "orbita di una cometa"
      ],
      "evidenzia": []
     },
     "nota": "Motte aggiunge «by no means» e «the hypothesis of»."
    },
    {
     "id": "L3-SchGen-p7",
     "la": "",
     "it": "Le comete sono portate con moti molto eccentrici in tutte le parti dei cieli, il che non può avvenire se non si tolgono i vortici.",
     "en": "for comets are carried with very eccentric motions through all parts of the heavens indifferently, with a freedom that is incompatible with the notion of a vortex.",
     "dipende_da": [],
     "figura": {
      "mostra": [
       "orbite cometarie inclinate in tutte le direzioni"
      ],
      "evidenzia": []
     },
     "nota": "Motte parafrasa: «indifferently, with a freedom that is incompatible with the notion of a vortex»."
    },
    {
     "id": "L3-SchGen-p8",
     "la": "",
     "it": "I proiettili, nella nostra aria, sentono soltanto la resistenza dell’aria.",
     "en": "Bodies projected in our air suffer no resistance but from the air.",
     "dipende_da": [],
     "figura": {
      "mostra": [
       "proiettile nell’aria"
      ],
      "evidenzia": []
     }
    },
    {
     "id": "L3-SchGen-p9",
     "la": "",
     "it": "Tolta l’aria, come avviene nel vuoto di Boyle, la resistenza cessa, poiché una piuma sottile e dell’oro massiccio cadono in questo vuoto con velocità uguale.",
     "en": "Withdraw the air, as is done in Mr. Boyle's vacuum, and the resistance ceases; for in this void a bit of fine down and a piece of solid gold descend with equal velocity.",
     "dipende_da": [],
     "figura": {
      "mostra": [
       "piuma e oro che cadono nel vuoto"
      ],
      "evidenzia": [
       "velocità uguali"
      ]
     },
     "nota": "Lo stesso esperimento è descritto nella Prop. VI di questo Libro (non citata)."
    },
    {
     "id": "L3-SchGen-p10",
     "la": "",
     "it": "E lo stesso ragionamento vale per gli spazi celesti, che sono al di sopra dell’atmosfera della Terra.",
     "en": "And the parity of reason must take place in the celestial spaces above the earth's atmosphere;",
     "dipende_da": [],
     "figura": {
      "mostra": [
       "atmosfera terrestre",
       "spazi celesti"
      ],
      "evidenzia": []
     }
    },
    {
     "id": "L3-SchGen-p11",
     "la": "",
     "it": "Tutti i corpi devono muoversi in questi spazi con la massima libertà; e perciò i pianeti e le comete devono ruotare perpetuamente in orbite date di forma e di posizione secondo le leggi esposte sopra.",
     "en": "in which spaces, where there is no air to resist their motions, all bodies will move with the greatest freedom; and the planets and comets will constantly pursue their revolutions in orbits given in kind and position, according to the laws above explained;",
     "dipende_da": [
      "leggi esposte sopra (Libri I e III)"
     ],
     "figura": {
      "mostra": [
       "orbite dei pianeti e delle comete"
      ],
      "evidenzia": []
     },
     "nota": "Motte aggiunge «where there is no air to resist their motions»."
    },
    {
     "id": "L3-SchGen-p12",
     "la": "",
     "it": "Persevereranno certo nelle loro orbite per le leggi della gravità, ma la posizione regolare delle orbite non poterono affatto acquistarla in origine per queste leggi.",
     "en": "but though these bodies may, indeed, persevere in their orbits by the mere laws of gravity, yet they could by no means have at first derived the regular position of the orbits themselves from those laws.",
     "dipende_da": [],
     "figura": {
      "mostra": [],
      "evidenzia": [
       "leggi della gravità: conservano le orbite, non ne spiegano la disposizione"
      ]
     }
    }
   ],
   "nota": "Come da istruzioni, un passo per frase dei primi due capoversi (contro i vortici; i moti negli spazi liberi), che hanno un argomento fisico che una pagina può mostrare (i tre esponenti incompatibili per i periodi delle parti del vortice, nota N10). I capoversi teologici e metodologici (III.G9.03–III.G9.15) non hanno passi: sono testo da leggere, non un calcolo. Motte unisce più frasi latine con «but» e «for»: ogni en è la porzione corrispondente del suo periodo."
  }
 ]
}
```
