# Rapporto di verifica: «Principia interattivi — Libro I», v0.4

Artefatto: slug 0d8bdaa9-e9f3-4571-8549-cdb0f0855ab9, versione 1794128769-6469. HTML ricostruito in `/home/claude/verifica/index.html` (1198 righe, documento completo letto in un solo blocco dal tool). L'artefatto non è stato modificato.

## Verdetto

**APPROVATO CON CORREZIONI**, cioè **pubblicabile con riserve** nella scala della skill.

Le cinque modifiche della v0.4 sono fedeli al latino e coincidono con il Fascicolo 3 e con le decisioni del curatore. Nella pagina non restano formulazioni vecchie («tendono continuamente», «grande impulso», «due forze» nell'enunciato, «ABCD» nel testo italiano, Leggi nella vecchia forma). L'avviso di degenerazione funziona, non genera cicli di aggiornamento e si legge a 375 px. Le riserve sono tutte minori: due riguardano il testo dell'avviso e il momento in cui compare, le altre sono rifiniture.

## Problemi, in ordine di gravità

### 1. (Minore, codice e didattica) L'avviso compare anche al passo 1, quando C e il parallelogramma non sono ancora mostrati
Posizione: riga 735, gestore `b.on("update", …)`. La condizione non tiene conto del passo. In Chrome headless, al passo 1 (indice 0) con B portato in (0.35, 1.4) sulla retta AC (C è nascosto), l'avviso risulta visibile (`vis: true`). Lo studente legge così di «retta AC» e di «parallelogramma» prima che compaiano.
Correzione: nel gestore, `const deg = VIEWS["leggi"].step>=2 && …` (oppure `>=1`), e alla fine di `onStep` della vista Leggi aggiungere `this.board.update()`, che già c'è, così l'avviso si ricalcola al cambio di passo.

### 2. (Minore, testo dell'avviso) Il messaggio è troppo assoluto e non copre tutti i casi
Posizione: riga 734. Testo attuale:
`"⚠ B è sulla retta AC: il parallelogramma degenera"`
- La soglia (seno < 0,06, cioè meno di 3,44°) scatta anche quando B è solo *quasi* sulla retta.
- Scatta anche quando B coincide con A, o C con A. In quei casi `nn = 0 → 1` e il prodotto vettoriale è 0: l'ho verificato, `deg = true`. Lì però «retta AC» non ha senso o è fuorviante.
- Si possono trascinare sia B sia C.
Testo proposto: `"⚠ A, B e C sono (quasi) allineati: il parallelogramma degenera"`.

### 3. (Minore, accessibilità) L'avviso non arriva ai lettori di schermo
Il testo è disegnato dentro la tavola JSXGraph, un `div` con `role="img"` e `aria-label` uguale all'alt del passo, quindi i lettori di schermo non lo leggono. Correzione: nel gestore, quando `deg` cambia, scrivere anche in `#live`, per esempio `$("#live").textContent = deg ? "Attenzione: A, B e C sono allineati, il parallelogramma degenera." : "";`.

### 4. (Minore, leggibilità) L'avviso è sovrapposto alla figura
Lo screenshot a 375 px (`leggi_mobile_degenere.png`) mostra che, con B sulla retta AC, la diagonale AD attraversa la scritta, che resta comunque leggibile. Il box del testo misura 286 × 16 px, da x = 20 a 306 su 375, quindi è interamente visibile. Le misure sono prese con il font di riserva, perché Google Fonts non era raggiungibile. Suggerimento: aggiungere `cssStyle:"background:rgba(255,253,248,.9);padding:1px 4px;border-radius:4px"` oppure spostare l'avviso in HTML sotto la tavola, nel `div.controls` di Leggi.

### 5. (Minore, nota testuale Prop. XI) La nota afferma più di quanto la fonte consultata dimostri
Posizione: riga 529. Testo attuale: «… il refuso è dell'edizione americana del 1846.»
Il riscontro sul 1846 è stato fatto sul file Gutenberg (SVG n. 96, che ho controllato: si legge PE²/SP²), non su una scansione della stampa. Il Fascicolo 3, § F3, è infatti più prudente: «dell'edizione americana del 1846 (o della sua trascrizione Gutenberg)».
Sostituire con: «il refuso è dell'edizione americana del 1846 o della sua trascrizione Gutenberg, non di Motte.»
Il resto della nota è corretto: il latino 1726 ha *PE cub./SPq* a p. 56 (riga 24 di S03, dopo il segno `<56>`), e lo stesso vale per la Prop. XII. Il controllo numerico al punto C conferma PE³.

### 6. (Minore, Lemma I, nota di traduzione) La frase sul ruolo di *constanter* è un po' vaga
Posizione: riga 428. Testo attuale: «La dimostrazione funziona se l'avvicinamento non si interrompe, cioè se la differenza non torna mai a crescere.»
Matematicamente l'ipotesi «più vicine di qualsiasi differenza data» basta già a dare liminf = 0. A *constanter* (differenza che non torna a crescere) serve che la «differenza ultima» **esista**, ed è proprio ciò che la «Lettura moderna» dice che Newton dà per scontato.
Proposta: «L'avvicinamento senza interruzione, cioè una differenza che non torna mai a crescere, garantisce che una differenza ultima esista; la dimostrazione per assurdo mostra poi che essa non può essere diversa da zero.»

### 7. (Minore, fedeltà Prop. I, fuori dalle modifiche v0.4) Tre calchi da Motte non presenti nel latino
- Passo 1 (riga 603): «**Infatti**, si supponga…» → il latino *Dividatur tempus…* non ha *Nam*; «For» è di Motte. Proposta: «Si supponga il tempo diviso in parti uguali…».
- Passo 1: «per la **sua** forza insita» → latino *vi insita*; il Fascicolo 3, § F2, scrive «per la forza insita». Proposta: «per la forza insita».
- Passo 3 (riga 609): «e, deviandolo dalla retta Bc, lo costringa a continuare il suo moto lungo la retta BC» ricalca Motte («turning aside… compels it afterwards to continue its motion»). Il latino ha *efficiatque ut corpus de recta Bc declinet & pergat in recta BC*. Proposta: «e faccia sì che il corpo devii dalla retta Bc e prosegua lungo la retta BC.»
La parte nuova, «agisca con un impulso unico ma grande», è conforme alla decisione del curatore e al latino *impulsu unico sed magno*.

### 8. (Suggerimento, note di traduzione) Le scelte nuove non sono spiegate nella pagina
Con il testo inglese attivo, lo studente vede «two forces», «unless» e «at once with a great impulse» accanto a un italiano diverso, ma le note della pagina non lo spiegano. Suggerisco di aggiungere:
- nelle note di Leggi (riga ~398): «*nisi quatenus* è reso "se non in quanto": il corpo persevera eccetto che nella misura in cui le forze lo costringono a cambiare (Motte: "unless"). Nell'enunciato del Corollario I il latino *viribus conjunctis* non dice "due": "two" è un'aggiunta di Motte.»
- nelle note della Prop. I (riga 486): «*impulsu unico sed magno*: "con un impulso unico ma grande"; Motte ("at once with a great impulse") perde l'opposizione *unico sed magno*.»

### 9. (Cosmetico) Apostrofi
La pagina usa l'apostrofo dritto ('), il Fascicolo quello tipografico (’). Normalizzando gli apostrofi i testi coincidono carattere per carattere. Uniformare se si vuole la coerenza tipografica.

## Controlli secondo la skill

### A. Fedeltà al testo: SUPERATO (con le riserve 5–8)
- Legge I, II, III, enunciato del Cor. I e concatenazione dei 5 passi del Cor. I: **identici** al Fascicolo 3 (L01, L03, L05, L08, L09). Metodo: script `script/confronta.py`, confronto esatto dopo la normalizzazione di spazi e apostrofi; risultato True su tutte e cinque le voci.
- Confronto con il latino (`fonte_la.md` r. 38–40): ogni frase di *Si corpus dato tempore… per legem I* ha il suo passo; nessun passo inventa contenuto. «se non in quanto», «in linea retta» e il Cor. I senza «due» sono conformi alle decisioni.
- Nota «[sic …]» nel passo 3 (en): corretta. Motte 1846 (`fonte_en.md` r. 79) ha «ABCD»; il latino ha *ABDC*. Anche la figura 1846 incorporata nella pagina, che ho estratto e guardato, ha i vertici A, B in alto e C, D in basso, con la diagonale AD: è il parallelogramma ABDC.
- Lemma I: enunciato e passo 1 con «tendono senza interruzione» conformi a § F1 e al latino *constanter tendunt* (S01 r. 24). Passi 3–4 conformi a *Si negas… contra hypothesin*.
- Prop. I, passo 3: «impulso unico ma grande» conforme a § F2.
- Prop. XI, «La stessa cosa altrimenti»: traduzione conforme al latino S03 r. 24; PE³/SP² corretto.
- Ricerca dei residui (`continuamente`, `grande impulso`, `due forze`, `ABCD`, `costantemente`, `a meno che`) su tutto l'HTML. Restano solo usi legittimi:
  - «Le due forze» nella Lettura moderna del Cor. I, riferito a M e N della dimostrazione;
  - «richiama continuamente», che traduce *perpetuo* nel passo 8 della Prop. I;
  - «ABCDEF» nella Prop. I;
  - «ABCD» dentro la nota [sic].
  Nessuna sostituzione obbligatoria.
- Dipendenze: la vista Leggi ha Legge I e Legge II, come cita il testo (*per legem II*, *per legem I*).

### B. Correttezza matematica: SUPERATO
- Corollario I: D = B + C − A (riga 721) realizza ABDC. Il punto «M e N» è pM + t·(C − A), quindi sta sulla parallela a BD per pM: arriva a BD nello stesso istante del corpo «solo M», come dicono il passo 4 e la domanda 2 per la classe.
- Avviso: la condizione |AB × AC| / (|AB|·|AC|) < 0,06 equivale a |sin BAC| < 0,06, cioè un angolo sotto 3,44° oppure sopra 176,56° (B dalla parte opposta). In entrambi i casi il parallelogramma è schiacciato, quindi la condizione è giusta. Con |AB| ≈ 4,2 (configurazione iniziale) la soglia corrisponde a un'altezza del parallelogramma di 0,25 unità, circa 20–25 px: una scelta ragionevole, che permette di vedere ancora la figura prima che l'avviso scatti. La configurazione iniziale ha un angolo di 80,4°, lontano dalla soglia.
- Ipotesi implicite del Cor. I: forze istantanee in A e indipendenza delle componenti, già nella nota N4 del Fascicolo. B ≠ A e C ≠ A sono coperti dall'avviso, ma con un testo improprio (problema 2).

### C. Controllo numerico: SUPERATO
- `script/degwarn.js` (Node): B esattamente sulla retta AC in 5 posizioni su 5 → avviso presente. Su 100 000 configurazioni casuali la formula coincide con sin(angolo) < 0,06 senza alcuna discordanza. Casi limite B = A e C = A → avviso (vedi problema 2).
- `script/numerico.js`, che usa le funzioni `construct`, `triArea`, `lineInter` e `footOn` estratte dal codice della pagina:
  - Prop. I, 1000 configurazioni casuali × 3 leggi di forza: scarto relativo massimo tra le aree 1,6·10⁻¹² (< 1e-9). Con impulso non centrale lo scarto è dell'ordine di 1, come deve essere.
  - Prop. XI, con dl = 1e-4 e 200 punti P per e = 0,2 / 0,7 / 0,9: QT²/(QR·L) è compreso in [0,9998; 1,0002]; la variazione relativa di forza × SP² è 4·10⁻⁵ / 2·10⁻⁴ / 4·10⁻⁴, sempre sotto 1e-3.
- `script/pe3.js`, controllo della Nota testuale. Ho calcolato la forza verso un punto S qualsiasi interno all'ellisse, divisa per la forza verso C, e confrontata con PE^k/(SP²·CP). Con k = 3 il rapporto è costante (variazione relativa ≤ 2·10⁻⁴); con k = 2 varia del 40 % per S diverso dal fuoco. PE³ è quindi corretto; nel fuoco le due forme coincidono perché PE = AC.
- Coerenza con il codice JSXGraph: ho usato le stesse funzioni della pagina, e i chip ✓ visualizzati in Chrome coincidono, per esempio EP = AC = 4,2000 ed ES = EI = 2,0483.

### D. Interfaccia e didattica: DUBBIO, per i problemi 1–4
- Cicli di aggiornamento: **nessuno**. In JSXGraph 1.10.1 (`src/base/board.js`, r. 5948–5994) gli handler `update` vengono chiamati con `inUpdate = true`, quindi un eventuale `board.update()` annidato ritornerebbe subito. In più, `setAttribute({visible})` (`element.js` r. 1432–1447) chiama solo `setDisplayRendNode` e non `board.update()`. Il controllo `visProp.visible !== deg` evita chiamate ripetute. Misura in Chrome: 2 `moveTo` più 2 `update()` producono esattamente 4 eventi `update`, uno per aggiornamento.
- Test in Chrome headless (Playwright, `/usr/bin/google-chrome`, a 1280×900 e 375×740 touch), script `script/browser.py`, risultati in `risultati_browser.json`:
  - B trascinato col mouse da (4,2; 3,2) a un punto della retta AC: avviso visibile (`display:block`). Se B torna alla posizione iniziale, l'avviso sparisce.
  - B ruotato oltre la retta AC di arcsin 0,05: avviso presente. Di arcsin 0,07: assente. La soglia è rispettata.
  - Alt-text: per tutti e 5 i passi di Leggi `aria-label` della tavola coincide con `STEPS.leggi[i].alt`. I testi alt sono coerenti con il testo italiano e con gli oggetti mostrati da `onStep`.
  - #lemma-1 (4 passi), #prop-1 (8 passi, chip delle aree tutti ✓, SADS:SAFS = 0,6000) e #prop-11 (9 passi, chip ✓ esatti, → al limite): nessun errore JavaScript e nessun `pageerror`. L'unico messaggio in console è `Failed to load resource: net::ERR_FAILED`, dovuto ai Google Fonts bloccati di proposito nel test (vedi sotto).
- `node --check` sui 4 script inline estratti (`script/inline0–3.js`): nessun errore di sintassi.
- Vincoli di pubblicazione: MathJax `tex-svg` ✓; CSS di JSXGraph e della pagina incorporati ✓ (resta esterno solo il foglio dei Google Fonts, già presente nella v0.3); hash semplici `#leggi`, `#lemma-1`, `#prop-1`, `#prop-11` ✓; nessun `alert(` ✓.

## Cosa non ho potuto verificare
- **Rete:** jsDelivr e Google Fonts sono bloccati dal proxy del contenitore (403). Ho installato JSXGraph 1.10.1 e MathJax 3.2.2 con `npm pack`, le stesse versioni dei CDN, e li ho serviti alla pagina intercettando le richieste. Google Fonts non era disponibile, quindi i test usano il font di riserva (Georgia/Times): la larghezza dell'avviso con EB Garamond può differire di qualche pixel.
- **Motte 1729 (vol. I, p. 80) e la stampa del 1846:** non li ho visti. Il dato sul 1729 viene dal Fascicolo 3, § F3; per il 1846 ho visto solo la resa Gutenberg (SVG n. 96).
- **Dispositivi reali:** nessun test su un dispositivo touch reale né con un lettore di schermo reale. La valutazione di accessibilità del punto 3 viene dall'analisi della struttura ARIA.

## File prodotti
- `/home/claude/verifica/index.html`: HTML ricostruito
- `/home/claude/verifica/script/`: `confronta.py`, `degwarn.js`, `numerico.js`, `pe3.js`, `browser.py`, `inline0–3.js`
- `/home/claude/verifica/risultati_browser.json`
- Screenshot: `leggi_desktop_degenere.png`, `leggi_mobile_degenere.png`, `lemma-1_*.png`, `prop-1_*.png`, `prop-11_*.png`
