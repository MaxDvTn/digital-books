# Brief comune — Traduzione del Libro I dei *Principia* (fascicoli 4–12)

Leggi tutto questo brief prima di cominciare. Vale per ogni traduttore. Lavori in parallelo con altri traduttori su Sezioni diverse: la coerenza tra fascicoli dipende dal rispetto puntuale di queste regole.

## Ruolo

Agisci come redattore di un'edizione scientifica, con la competenza di un latinista, di uno storico della scienza e di un fisico. Il progetto è un'edizione didattica e interattiva in italiano dei *Principia* di Newton, per il liceo scientifico. Curatore: Massimo Bosetti.

## Modello da seguire

Il modello di formato, tono e livello di dettaglio è il **Fascicolo 3**: `/home/claude/work/Newton_Principia_IT_03_Leggi.md`. Leggilo per intero prima di scrivere. Il tuo fascicolo deve avere la stessa struttura:

1. intestazione: titolo, sottotitolo, «Versione 0.1 — 8 novembre 2026. Preparata con Claude (Anthropic) per Massimo Bosetti.»;
2. **Stato e perimetro**;
3. **Fonti effettivamente consultate** (latino 1726 con pagine; Motte 1846 con pagine dai marcatori, se le trovi, altrimenti «sezione corrispondente»);
4. **Criteri di traduzione** (richiama il glossario comune; elenca le estensioni proprie);
5. **Traduzione italiana**, con identificatori in grassetto `**[S5.01]**` (S + numero arabo della Sezione + punto + numero progressivo a due cifre, un identificatore per enunciato, per paragrafo di dimostrazione, per corollario, per scolio o per caso). Ogni lemma e proposizione ha un titolo `### Lemma XII` / `### Proposizione XIV. Teorema VI` con un breve titolo tematico tra parentesi;
6. **Apparato**: § A.0 estensioni del glossario; poi, per ogni lemma e proposizione, enunciato latino e inglese esatti e le scelte motivate; refusi della trascrizione; un riepilogo in tabella di **dove Motte aggiunge, omette o sbaglia**;
7. **Note editoriali e fisiche** numerate (N1, N2, …), separate dal testo di Newton, con le corrispondenze moderne e i controlli numerici;
8. **Controllo della copertura**: tabella identificatori → incipit latino → contenuto → pagine 1726 → pagine Motte; controlli eseguiti; «Non ho potuto verificare»;
9. **Registro del lavoro successivo**;
10. **Parte B — Dati per le pagine interattive** in un blocco ```json``` (vedi sotto).

## Fonti (solo queste; niente a memoria)

- Latino 1726, trascrizione del Newton Project: `/home/claude/libro1/fonti/latino-1726-L1-Sxx.md`. **È il testo guida.**
- Inglese di Motte, ed. New York 1846: `/home/claude/libro1/fonti/motte-1846-L1-Sxx.md`. Serve per il confronto. Le formule stampate come immagini compaiono come `[SVG n]`: quando una formula conta, rendila con `rsvg-convert -h 120 -b white /home/claude/src_epub/OEBPS/3191938728343764116_n.svg -o /tmp/f.png` e guardala con lo strumento Read.
- Nota tecnica: l'ultima frase della Sezione VII di Motte («…rectangle 2PD × DL to the area DLme.») è finita all'inizio del file della Sezione VIII.
- Non usare e non riprodurre traduzioni moderne (Cajori 1934, Cohen–Whitman, Pala, Giudice). Non ricostruire nulla a memoria: se una lettura è incerta, segnalala nell'apparato e non indovinarla.
- La trascrizione del Newton Project contiene refusi. Esempi già accertati sulla stampa del 1726: *invenit* omesso, *horizentem* per *horizontem*, *insimo* per *infimo*, *Qoud* per *Quod*. Quando una forma è chiaramente un refuso, traduci secondo il senso e annota «refuso probabile della trascrizione, da verificare sulla stampa». Non correggere in silenzio.
- Le formule della trascrizione possono comparire duplicate o con frazioni appiattite. Esempi: «15+115+1» vale «15+1»; «PE cub.SPq» vale PE³/SP². Ricostruiscile dal contesto e dichiara come le hai lette.
- Le figure originali non sono disponibili: ricostruisci le relazioni geometriche solo dalle lettere citate nel testo.

## Glossario comune (obbligatorio)

### Già fissato nei fascicoli 1–3

- *vis insita*: «forza insita»; *vis impressa*: «forza impressa»; *vis motrix*: «forza motrice»; *vis acceleratrix*: «forza acceleratrice»; *vis absoluta*: «forza assoluta»; *vis centripeta*: «forza centripeta»; *vis centrifuga*: «forza centrifuga».
- *quantitas motus*, e *motus* quando indica la grandezza: «quantità di moto»; *mutatio motus*: «cambiamento della quantità di moto».
- *impetus*: «impeto»; *impulsus*: «spinta», oppure «impulso» dove indica un'azione istantanea che cambia la quantità di moto. Nella Prop. I *impulsu unico sed magno* si rende «con un impulso unico ma grande». *ictus*: «urto».
- *ratio prima / ultima*: «rapporto primo / ultimo»; *quantitates evanescentes / nascentes*: «quantità evanescenti / nascenti»; *ultimo* (avverbio): «alla fine».
- *in directum*: «in linea retta»; *conjunctim*: «considerate congiuntamente».
- *constanter* (Lemma I, *constanter tendunt*): «senza interruzione».
- *determinatio*: «direzione» («verso» solo quando si contrappongono i due versi di un moto).
- *nisi quatenus*: «se non in quanto».
- *ratio duplicata / triplicata / subduplicata / sesquiplicata*: «rapporto duplicato / triplicato / subduplicato / sesquiplicato» (= quadrato / cubo / radice quadrata / potenza 3/2). Nelle note si può dare l'equivalente moderno.
- *reciproce*: «inversamente»; *directe*: «direttamente».
- *conatus*: «tendenza»; *pollere, æquipollere*: «avere la stessa efficacia»; *ducere in*: «moltiplicare per».
- *reflexio*: «riflessione»; *concursus / congressus*: «incontro / scontro».
- Q.E.D.: C.V.D.; Q.E.I.: C.V.T.; Q.E.F.: «C.V.F.» (come volevasi fare); Q.E.O.: «C.V.M.» (come volevasi mostrare).

### Termini tecnici del Libro I (fissati ora, valgono per tutti)

- *sagitta*: «saetta» (la freccia dell'arco; alla prima occorrenza nel fascicolo spiega in nota che è la freccia dell'arco).
- *sinus versus*: «seno verso»; *sinus*: «seno»; *subtensa*: «sottesa»; *chorda*: «corda»; *angulus contactus*: «angolo di contatto».
- *latus rectum*: «lato retto»; *umbilicus*: «fuoco»; *vertex principalis*: «vertice principale»; *axis principalis / transversus*: «asse principale / trasverso»; *diametri conjugatæ*: «diametri coniugati»; *ordinatim applicata*: «ordinata»; *abscissa*: «ascissa»; *sectio conica / coni sectio*: «sezione conica»; *trajectoria*: «traiettoria»; *orbis, orbita*: «orbita».
- *positione datus*: «dato di posizione»; *specie datus*: «dato di forma»; *magnitudine datus*: «dato di grandezza».
- *tempus periodicum*: «tempo periodico»; *apsis, apsides*: «apside, apsidi»; *in consequentia / in antecedentia*: «in conseguenza / in antecedenza», con una nota alla prima occorrenza che spieghi il senso (nel verso del moto / contro il verso del moto).
- *funependulum*: «pendolo a filo»; *corpus funependulum*: «corpo appeso a un filo».
- *attractio*: «attrazione»; *particula*: «particella»; *globus*: «globo»; *superficies sphærica*: «superficie sferica».
- *Cas.*: «Caso»; *Corol.*: «Cor.»; *Schol.*: «Scolio»; *Theorema / Problema*: «Teorema / Problema».
- Le lettere delle figure restano come nel latino, comprese le minuscole corsive.
- Se ti serve un termine nuovo, scegli la resa, motivala nel § A.0 e usala in modo costante.

## Criteri di traduzione

- Il latino è il testo guida. Traduci frase per frase, senza omettere frasi.
- Italiano contemporaneo, ma conserva la struttura argomentativa e il lessico storico: i rapporti restano rapporti, nel testo non entrano formule moderne. Le formule moderne vanno solo nelle note.
- Gli enunciati latini all'infinito (accusativo e infinito) si rendono con l'indicativo.
- Le espressioni come «AB quad.», «SPq», «PE cub.» si scrivono in testo come AB², SP², PE³ (apice Unicode), e i rapporti come «A sta a B come C sta a D». Le frazioni si scrivono con la barra (QT²/QR) o a parole, mai in LaTeX nel testo tradotto.
- Rimandi interni: «per il Cor. 2 del Lemma VII», «per la Prop. VI», «per la Legge II».

## Controlli obbligatori prima di consegnare

1. **Copertura:** rileggi il latino frase per frase contro la traduzione e dichiara l'esito.
2. **Matematica:** per ogni esempio numerico o rapporto verificabile, ricontrolla l'aritmetica. Per le proposizioni geometriche importanti fai una verifica numerica con uno script tuo (Python o Node) su una figura di prova, come nel Fascicolo 3 (F3), e riportala nelle note.
3. **Divergenze di Motte:** confronta tutta la sezione corrispondente. Formule sbagliate, lettere diverse, aggiunte e omissioni vanno nella tabella dell'apparato.
4. **Parte B:** valida il JSON con `python3 /home/claude/libro1/brief/check.py <tuo_file.md> <file_latino> [<file_latino2>…] --en <file_motte> [<file_motte2>…]`. Lo script controlla che il JSON sia valido e che ogni stringa `la` ed `en` dei passi sia una sottostringa esatta delle fonti (spazi normalizzati). Correggi finché non passa.

## Parte B — specifica

Un oggetto JSON con questa forma:

```json
{"fascicolo":"05-L1-S2","versione":"0.1","data":"2026-11-08",
 "convenzioni":{"dipende_da":"solo rimandi citati esplicitamente nella frase","en":"Motte 1846, allineato per senso","figura.mostra":"elementi da rendere visibili al passo, cumulativi salvo indicazione"},
 "unita":[{"id":"L1-P1","tipo":"Propositio/Theorema","titolo":"Prop. I — legge delle aree","copertura":["S2.01","S2.02"],
   "fonti":{"la":"1726, pp. 38–39","en":"Motte 1846, p. …"},
   "enunciato":{"la":"…","it":"…","en":"…"},
   "figura_base":{"punti":["S","A","B","c","C"],"vincoli":["…"]},
   "passi":[{"id":"L1-P1-p1","la":"…","it":"…","en":"…","dipende_da":["Legge I"],"figura":{"mostra":["…"],"evidenzia":["…"]},"nota":"…"}]}]}
```

- Includi **ogni lemma e proposizione che ha una dimostrazione con figura** (cioè con [FIG n] nel latino o con costruzione geometrica). I corollari entrano solo se hanno una dimostrazione propria con figura.
- Un passo per ogni frase latina della dimostrazione principale. `la` deve essere la frase latina **esatta** della trascrizione, refusi compresi.
- `en` è la frase corrispondente di Motte, esatta. Quando non c'è corrispondenza esatta, metti la porzione più vicina e spiegalo in `nota`.
- In `dipende_da` vanno soltanto i rimandi citati davvero nella frase («per leg. i.» → "Legge I"; «per corol. 4 lem. iii.» → "Lemma III, Cor. 4").
- Gli `id` delle unità seguono lo schema `L1-Lem1`, `L1-P14`, `L1-P14-Cor2`.

## Consegna

- Scrivi il fascicolo in `/home/claude/libro1/out/` con il nome che ti è stato assegnato. Se il file è lungo, scrivilo per parti e poi concatenale.
- Alla fine il messaggio di ritorno deve essere breve, al massimo 25 righe: nome del file e dimensioni, numero di unità tradotte, esito dei controlli (copertura, check.py, verifiche numeriche), i 3–8 punti più importanti per il curatore (refusi, errori di Motte, letture incerte) e cosa non hai potuto verificare. Non incollare il fascicolo nel messaggio.
