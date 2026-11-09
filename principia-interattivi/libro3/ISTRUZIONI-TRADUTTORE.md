# Istruzioni per il traduttore — Libro III dei *Principia*, *De mundi systemate* (coordinatore: Claude, curatore: Massimo Bosetti)

Lavori in parallelo con altri 9 traduttori, ognuno su un fascicolo diverso del Libro III. Esegui il lavoro direttamente, senza delegare ad altri agenti.

## Da leggere prima di scrivere

1. `/home/claude/libro3/strumenti/BRIEF.md` — il brief comune del Libro I. **Vale integralmente**, con queste sostituzioni di percorso:
   - modelli di formato: `/home/claude/libro3/traduzione/Newton_Principia_IT_03_Leggi.md` (leggilo per intero), `/home/claude/libro3/traduzione/Newton_Principia_IT_05_L1_S02.md` (fascicolo di Sezione: leggi almeno intestazione, criteri, le prime due proposizioni, apparato, controllo della copertura e l'inizio della Parte B) e `/home/claude/libro3/traduzione/Newton_Principia_IT_20_L2_S09.md` (il modello più vicino per titoli, identificatori con prefisso di libro, apparato e Parte B);
   - fonti: `/home/claude/libro3/fonti/latino-1726/latino-1726-L3-*.md` e `/home/claude/libro3/fonti/motte-1846/motte-1846-L3-*.md` (stessi gruppi);
   - LaTeX delle formule SVG di Motte: `/home/claude/libro3/fonti/motte-1846/svg_tex.tsv` (righe «n<TAB>latex»);
   - check: `python3 /home/claude/libro3/check.py <fascicolo> <latino…> --en <motte…>`;
   - consegna: `/home/claude/libro3/out/`;
   - fascicoli già tradotti (per i rimandi): `/home/claude/libro3/traduzione/` (01–03 Definizioni, Scolio, Leggi; 04–12 Libro I; 13–20 Libro II).
2. `/home/claude/libro3/libro2/ISTRUZIONI-TRADUTTORE.md` — l'addendum del Libro II: il suo glossario e i «termini fissati dal coordinatore» **valgono anche per il Libro III**.
3. Questo file, che prevale su entrambi dove diverge.

## Ripartizione e perimetro (rispetta esattamente i confini)

| Fasc. | File da produrre in `out/` | Perimetro | Latino / Motte | Gruppo | `"fascicolo"` |
|---|---|---|---|---|---|
| 21 | `Newton_Principia_IT_21_L3_Regole-Fenomeni.md` | Titolo e introduzione del Libro III, *Regulæ philosophandi* I–IV, *Phænomena* I–VI, fino a «PROPOSITIONES.» compreso | `L3-Regole-Fenomeni` | G1 | `"21-L3-Regole-Fenomeni"` |
| 22 | `Newton_Principia_IT_22_L3_P01-14.md` | Propp. I–XIV con scolî e Ipotesi I | `L3-P01-14` | G2 | `"22-L3-P01-14"` |
| 23 | `Newton_Principia_IT_23_L3_P15-20.md` | Propp. XV–XIX (G3) e Prop. XX (G4) | `L3-P15-19` + `L3-P20` | G3, G4 | `"23-L3-P15-20"` |
| 24a | `Newton_Principia_IT_24a_L3_P21-29.md` | Propp. XXI–XXIX (fino a prima di «PROPOSITIO XXX.») | `L3-P21-33` | G5 | `"24a-L3-P21-29"` |
| 24b | `Newton_Principia_IT_24b_L3_P30-33.md` | Propp. XXX–XXXIII, Scolio con le Propp. I–II (Machin) e lo Scolio finale | `L3-P21-33` | G5 | `"24b-L3-P30-33"` |
| 25a | `Newton_Principia_IT_25a_L3_P34-37.md` | Propp. XXXIV–XXXVII con lo Scolio della Prop. XXXV (fino a prima di «PROPOSITIO XXXVIII.») | `L3-P34-40` | G6 | `"25a-L3-P34-37"` |
| 25b | `Newton_Principia_IT_25b_L3_P38-40.md` | Prop. XXXVIII, Lemmi I–III, Ipotesi II, Prop. XXXIX, Lemma IV, Prop. XL, Lemmi V–XI con scolio | `L3-P34-40` | G6 | `"25b-L3-P38-40"` |
| 26a | `Newton_Principia_IT_26a_L3_P41.md` | Prop. XLI: costruzione, dimostrazione, *Exemplum* della cometa del 1680 con tutte le tabelle e le osservazioni, fino al paragrafo «Congruunt igitur hæ observationes…» compreso | `L3-P41` | G7 | `"26a-L3-P41"` |
| 26b | `Newton_Principia_IT_26b_L3_P41.md` | Prop. XLI, seconda parte: da «Cæterum trajectoriam quam cometa descripsit…» (Motte: «And, thinking it would not be improper…») alla fine (code e atmosfere delle comete) | `L3-P41` | G7 | `"26b-L3-P41"` |
| 27 | `Newton_Principia_IT_27_L3_P42-ScholiumGenerale.md` | Prop. XLII (G8) e *Scholium generale* (G9) fino alla fine dell'opera | `L3-P42` + `L3-ScholiumGenerale` | G8, G9 | `"27-L3-P42-SchGen"` |

Titoli dei fascicoli (riga `## Fascicolo NN — Libro III, …`): scegli un titolo breve sul modello del Fascicolo 20 (per esempio «Fascicolo 21 — Libro III: regole del filosofare e fenomeni»).

Per le parti divise, la parte «a» deve dire in «Stato e perimetro» che il seguito è nella parte «b», e viceversa. Usa il file latino e il file Motte **interi** per check.py (le stringhe devono essere sottostringhe del file intero).

## Identificatori

- Forma: `**[III.G5.01]**` — libro III, gruppo, numero a due cifre, senza buchi né doppioni, uno per enunciato, paragrafo di dimostrazione, corollario, scolio, caso, esempio, tabella.
- Gruppi: G1 Regole e Fenomeni; G2 Propp. I–XIV; G3 Propp. XV–XIX; G4 Prop. XX; G5 Propp. XXI–XXXIII; G6 Propp. XXXIV–XL; G7 Prop. XLI; G8 Prop. XLII; G9 Scolio generale.
- **Parti «b» (24b, 25b, 26b): numera provvisoriamente da 101** (`III.G5.101`, `III.G5.102`, …). Il coordinatore rinumererà alla fine con uno script, in modo che la serie continui quella della parte «a». Scrivi i rimandi a serie sempre per esteso con il prefisso completo (`III.G5.104–III.G5.107`, non «104–107»), così lo script li sposta correttamente.
- Le parti «a» e i fascicoli interi partono da 01.
- Nella Parte B, `copertura` usa la stessa forma (`"III.G5.01"`).

## Parte B

- `id` delle unità: `L3-Reg1`, `L3-Phaen5`, `L3-Hyp1`, `L3-P10`, `L3-P10-Cor2`, `L3-Lem4`; le due proposizioni dello scolio dopo la Prop. XXXIII: `L3-Machin-P1`, `L3-Machin-P2`; lo Scolio generale: `L3-SchGen`. Passi: `L3-P10-p1`, … Gli `id` devono essere unici in tutto il Libro III: nelle parti divise di una stessa proposizione (26a/26b) usa suffissi distinti (`L3-P41-Constr`, `L3-P41-Ex`, `L3-P41-Caudae`).
- Includi ogni lemma e proposizione con dimostrazione geometrica o con un calcolo che una pagina interattiva potrebbe mostrare (un passo per frase latina della dimostrazione). Le Regole, i Fenomeni, le Ipotesi e le proposizioni senza dimostrazione entrano come unità con `enunciato` e `copertura` e `"passi": []`. Per i Fenomeni e le tabelle aggiungi, se utile, un campo `"dati"` con i valori numerici della tabella (come numeri) e i risultati dei tuoi controlli.
- Lo Scolio generale (Fasc. 27) entra come unità `L3-SchGen` con un passo per ogni frase dei primi due paragrafi (argomento contro i vortici e sulle comete) e `"passi"` vuoti per il resto; nel campo `nota` spiega la scelta.
- `la` ed `en` esatti come nel brief; check.py deve chiudere con «OK». Gli avvisi su `en` sono ammessi solo se spiegati in `nota`.

## Glossario del Libro III (vincolante)

Deciso nel prompt del curatore:

| Latino | Italiano |
|---|---|
| *regulæ philosophandi* | «regole del filosofare» |
| *phænomenon* | «fenomeno» (titoli: «Fenomeno I») |
| *hypothesis* | «ipotesi» (titoli: «Ipotesi I»); *hypotheses non fingo* «non invento ipotesi», con nota |
| *systema mundi* | «sistema del mondo» |
| *planeta primarius / secundarius* | «pianeta primario / secondario» (= satellite, in nota alla prima occorrenza) |
| *satelles*, *comites* (di Giove e Saturno) | «satellite», con nota alla prima occorrenza di *comites* |
| *aphelium / perihelium* | «afelio / perielio» |
| *nodi*; *linea nodorum* | «nodi»; «linea dei nodi» |
| *præcessio æquinoctiorum* | «precessione degli equinozi» |
| *æstus maris*; *fluxus / refluxus* | «maree» (al singolare «marea»); «flusso / riflusso» |
| *cometa*; *cauda* | «cometa»; «coda» |
| *parallaxis* | «parallasse» |
| *variatio* (della Luna) | «variazione» |
| *æquatio* | «equazione» (correzione astronomica), con nota alla prima occorrenza |
| *Sol, Luna, Tellus / Terra* | «Sole, Luna, Terra» (maiuscola per i corpi celesti) |
| *gravitas universalis* | «gravità universale» |
| *æther*; *spiritus subtilissimus* | «etere»; «spirito sottilissimo» |

Fissati ora dal coordinatore (usali anche se ti sembrano meno adatti; motiva il dubbio nel § A.0):

- Nomi dei pianeti e dei corpi celesti con la maiuscola anche dove il latino ha la minuscola: Mercurio, Venere, Terra, Marte, Giove, Saturno, Sole, Luna; le costellazioni e le stelle con il nome latino in corsivo dove è un nome proprio (*spica Virginis* → «la Spiga della Vergine»). I segni zodiacali (♈ ♉ … ♓) restano come simboli, con nota alla prima occorrenza («♑ = Capricorno; la longitudine si conta in gradi dentro il segno»).
- *orbis magnus* «orbe magno» (l'orbita annua della Terra, con nota); *orbis* (orbita) «orbita»; *orbis* (strato) «guscio».
- *syzygiæ* «sizigie»; *quadraturæ* «quadrature»; *octantes* «ottanti»; *apogæum / perigæum* «apogeo / perigeo»; *conjunctio / oppositio* «congiunzione / opposizione»; *eclipsis* «eclissi».
- *motus medius* «moto medio»; *locus medius / verus* «luogo medio / vero»; *æquatio centri* «equazione del centro»; *æquatio annua* «equazione annua»; *anomalia* «anomalia»; *excentricitas* «eccentricità»; *inclinatio* «inclinazione»; *limites* «limiti».
- *longitudo / latitudo* «longitudine / latitudine» (eclittiche o geografiche secondo il contesto; *lat. bor. / austr.* «latitudine boreale / australe»); *declinatio* «declinazione»; *meridianus* «meridiano»; *gradus* «grado»; *minutum (primum) / secundum* «primo / secondo» (per i tempi: «minuto / secondo»); *horizon* «orizzonte»; *zenith* «zenit».
- *dies sidereus / solaris* «giorno siderale / solare»; *annus sidereus / tropicus* «anno siderale / tropico»; *st. vet.* «secondo il calendario giuliano (stile vecchio)», con nota alla prima occorrenza; le date restano come nel testo.
- *diameter apparens* «diametro apparente»; *semidiameter* «semidiametro»; *digitus* (eclissi) «dito», con nota (non è il pollice); *telescopium* «telescopio»; *micrometrum* «micrometro».
- *sphærois / figura sphæroidica* «sferoide / figura sferoidale»; *figura terræ* «figura della Terra»; *axis* «asse»; *æquator* «equatore»; *poli* «poli»; *annulus* «anello».
- *pendulum ad minuta secunda oscillans* «pendolo che batte i secondi»; *hexapeda* «tesa» (la tesa di Parigi, = 6 piedi parigini, con nota); *milliare* «miglio»; *linea* (misura) «linea»; *pes Parisiensis / Londinensis* «piede parigino / londinese».
- *vis solis ad perturbandos motus lunæ* e simili: «forza del Sole che perturba i moti della Luna»; *vis addititia / ablatitia* «forza aggiunta / sottratta».
- Comete: *caput* «testa»; *coma* «chioma»; *nucleus* «nucleo»; *atmosphæra* «atmosfera»; *vapor* «vapore»; *jubar* «splendore», con nota; *cometæ comati / caudati* «comete chiomate / caudate».
- *stellæ fixæ* «stelle fisse»; *maculæ* (solari) «macchie»; *planetæ* «pianeti»; *materia cœlestis* «materia celeste»; *vortex* «vortice».
- *ecliptica* «eclittica»; *mediocris distantia* «distanza media»; *ratio sesquialtera / sesquiplicata* «rapporto sesquialtero / sesquiplicato»; *divisim* «separando».
- Scolio generale: *Deus* «Dio»; *Dominus* «Signore»; *Pantocrator* resta in greco traslitterato con nota; *sensorium* «sensorio»; *substantia* «sostanza»; *experimentalis philosophia* «filosofia sperimentale»; *inductio* «induzione»; *qualitates occultæ* «qualità occulte».
- *inductio* (Regola IV) «induzione»; *qualitates corporum* (Regola III) «qualità dei corpi»; *intendi & remitti* «aumentare e diminuire».

Ogni altro termine nuovo va fissato nel tuo § A.0 e **segnalato nel messaggio di ritorno** (riga «Termini nuovi: …»).

## Regole specifiche del Libro III

- **Tabelle numeriche.** Le tabelle della trascrizione latina sono spezzate in una cella per riga; quelle di Motte hanno «|» tra le celle. Ricostruiscile come tabelle Markdown complete nel testo tradotto, allineando le colonne sul latino e controllando le righe su Motte. Controlla l'aritmetica con uno script Python tuo (per esempio la terza legge di Keplero nei *Phænomena*, i rapporti di distanze e periodi, le differenze «osservato − calcolato» nelle tabelle delle comete, le conversioni sessagesimali) e riporta il risultato nelle note. Segnala ogni cifra che non torna **senza correggerla nel testo**. Date e coordinate restano come nel testo (calendario giuliano, ore e minuti come in Newton).
- **Formule di Motte `[SVG n]`.** Hai il LaTeX di tutte le formule in `svg_tex.tsv`: per ogni formula rilevante cerca `n` e confrontala con il latino. Nell'apparato metti una tabella «SVG di Motte che non tornano con il latino» (n, LaTeX, lettura attesa). Non serve elencare quelle che tornano: basta dire quante ne hai controllate.
- **Stampa 1726 e Motte 1729.** Non provare a raggiungerle dal web. Elenca i punti dubbi in «Punti da controllare sulla stampa ECCO» (pagina 1726, lettura della trascrizione, lettura attesa, motivo).
- **Rimandi ai Libri I e II** («per prop. lxvi. lib. i.», «per corol. 22»): verifica sui fascicoli in `/home/claude/libro3/traduzione/` che l'enunciato citato regga l'uso che ne fa Newton. Scrivi «per la Prop. LXVI del Libro I» (e il corollario). I rimandi interni al Libro III si scrivono «per la Prop. XXV» (o «di questo Libro»). Elenca in apparato i rimandi verificati e quelli che non tornano. I rimandi a parti del Libro III che non sono nel tuo fascicolo puoi controllarli sul latino degli altri gruppi.
- **Note storiche e astronomiche.** Solo da ciò che risulta dalle fonti allegate; ciò che aggiungi da conoscenza generale (valori moderni, identificazione di osservatori e strumenti, date) va marcato «(non verificato sulle fonti allegate)». I confronti con i valori moderni sono utili per il liceo: mettili nelle note, marcati così.
- **Scolio generale (Fasc. 27).** Traduci con cura particolare. Annota le differenze rispetto alle edizioni precedenti **solo se risultano dalle fonti allegate** (per esempio dove Motte, che traduce il 1726, diverge dal latino); altrimenti non annotarle.
- **Lunghezza.** Scrivi per parti in `/home/claude/libro3/tmp/<tuo-fascicolo>/` e concatenale. Non creare in `out/` altro che il tuo fascicolo. Se il lavoro si interrompe, al riavvio riparti dai file in `tmp/`.

## Messaggio di ritorno (massimo 25 righe)

Nome del file e dimensioni; identificatori (primo–ultimo, numero); unità della Parte B e passi; esito dei controlli (copertura frase per frase, check.py con l'ultima riga dell'output, verifiche numeriche e tabelle); riga «Termini nuovi: …»; riga «Rimandi ai Libri I e II: …» (quanti, quali non tornano); 3–8 punti principali per il curatore (cifre che non tornano, refusi, errori di Motte, letture incerte); numero di SVG controllati e di SVG che non tornano; cosa non hai potuto verificare. Non incollare il fascicolo.
