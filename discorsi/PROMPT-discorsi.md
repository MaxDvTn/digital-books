# Prompt — Galileo, *Discorsi e dimostrazioni matematiche intorno a due nuove scienze* (1638), libro interattivo

Da incollare in una **nuova chat del progetto «Digital Book»**, aperta dall'app desktop sul Mac (serve la cartella locale).

---

Ciao. Sono Max, insegno fisica e matematica al Liceo scientifico «Leonardo da Vinci» di Trento. Stiamo trasformando classici scientifici in libri web interattivi per i miei studenti. Il primo libro di Galileo, il *Sidereus Nuncius*, è fatto. Ora passiamo al secondo: i **Discorsi e dimostrazioni matematiche intorno a due nuove scienze** (Leida, 1638).

## 1. Prima di tutto
1. Leggi nel progetto:
   - `claude/galileo-stato-del-progetto.md`: stato, decisioni, convenzioni;
   - `claude/stato-del-progetto.md`: le decisioni prese per Newton, solo come riferimento.
2. Carica le skill:
   - `editore-libri-scientifici-interattivi`, che è la guida principale;
   - `verifica-dimostrazioni-interattive`;
   - `osservazioni-storiche-come-dati`, solo per le schede in cui confronti dati di Galileo con un modello (tavole dei proietti, pendoli).
3. Chiedi l'accesso alla cartella `~/Projects/digital_books` sul mio Mac. Lavori in `discorsi/`.
4. Guarda come è fatto il Sidereus e **riusa il suo codice**, non ripartire da zero. Tutto è in `sidereus_nuncius/interattivo/`:
   - `build.py` e `template.html`: generazione della pagina;
   - `libro.js` e `libro.css`: libro sfogliabile, con le schede aperte a tutto schermo e la «tavola interattiva»;
   - `fasi.js`: simulazione three.js in stile incisione e fotogrammi in loop per il libro;
   - `astro.js` + `verifica_conteggi.py`: un solo modello per la pagina e per i test.

   Il risultato pubblicato è un'anteprima privata: https://claude.ai/artifact/AjdnjrvcCTaMaQBnkQCY6e

## 2. La fonte
- **Sorgente**: `discorsi/discorsi.tex`, con 97 figure in `discorsi/images/` e il PDF di confronto `discorsi/discorsi.pdf`.
- **Struttura**, con le righe del .tex (verificale):
  - Nota storica e filologica: 95
  - Dedica e Avviso: 119
  - Giornata Prima: 141
  - Giornata Seconda: 730
  - Giornata Terza, *Del moto locale*: 1174
    - «Del moto equabile»: 1182
    - «Del moto naturalmente accelerato»: 1214
    - esperimento del piano inclinato: circa 1320 e 1336
  - Giornata Quarta, *Del moto dei proietti*: 1651 («Del moto dei proietti» a 1657)
  - Appendice sul centro di gravità: 2058
  - una tabella intorno a 1959
- **È un dialogo.** Ci sono 390 battute `\speaker{...}`: Salviati 180, Sagredo 117, Simplicio 92. Le parti di trattato contengono definizioni, assiomi, teoremi, problemi e corollari.
- **Importazione**: usa `strumenti/importa_latex.py`. Gestisce già `\speaker` (blocchi «battuta»). Va esteso per tre cose:
  - le macro `\theoremheader` e `\propbox` (definite alle righe 53–60);
  - le intestazioni `\textbf{TEOREMA 1. PROPOSIZIONE 1}\\`;
  - circa 250 `\textcolor{rubric}{\textit{NN…}}`. Sembrano numeri di pagina o rimandi in margine: capisci che cosa sono **prima** di decidere come mostrarli.

  L'importatore segnala i comandi che non gestisce: non cancellarli a mano, aggiungili allo script. Ogni enunciato deve diventare un blocco strutturato, con tipo, numero e testo, perché poi ci si aggancia la scheda.
- **Attenzione: nel 1638 le parti di trattato delle Giornate Terza e Quarta erano in latino**, mentre qui sono in italiano. Controlla nella nota del .tex e sulla fonte da quale traduzione vengono.

## 3. Licenza (prima di pubblicare)
L'e-book di Liber Liber dichiara «diritti d'autore: no» ed è tratto da *Opere di Galileo Galilei*, UTET 1980 (a cura di F. Brunetti). Verifica:
- la licenza indicata oggi dalla pagina di Liber Liber dei *Discorsi*;
- chi ha tradotto le parti latine.

Scrivi nelle note della pagina fonte, licenza e attribuzione. Il codice resta MIT. Se la licenza è diversa da quella del Sidereus (CC BY-NC-SA), dimmelo prima.

## 4. Come lavoriamo
- **Una cosa alla volta.** Faccio vedere una scheda, guardo, ti correggo, poi passiamo alla successiva. Dopo ogni scheda aspetta il mio parere.
- **Il libro resta intero.** Come per il Sidereus, il volume ha sempre due modi di lettura:
  - la pagina continua;
  - il **libro sfogliabile**, dove le schede sono «tavole interattive» che si aprono a tutto schermo, e le animazioni in loop stanno dentro la pagina quando servono.
- **Stile.** Lo stesso del Sidereus:
  - EB Garamond, carta `#fbf8f2`, rubrica `#871919`;
  - le simulazioni grafiche in **stile incisione**: inchiostro su carta, tratteggio, nessun colore fotografico;
  - nei dialoghi il nome dell'interlocutore in maiuscoletto rubricato.
- **Didattica.** L'interattività deve far vedere il ragionamento di Galileo, non sostituirlo:
  - Galileo ragiona con le **proporzioni euclidee**, senza algebra. Ogni scheda mostra prima la sua proporzione e poi, in una «lettura moderna» separata, la formula (es. s ∝ t², v ∝ t);
  - ogni scheda ha le domande «Per la classe» con risposte nascoste e una sezione «Come è fatta» che dichiara le semplificazioni.
- **Figure.** Ogni figura geometrica diventa SVG ricostruito con le lettere di Galileo, accanto all'incisione originale. Nei riquadri ingranditi usa sempre la **scala vera** (mai un asse solo esagerato). I cursori devono andare nel verso intuitivo: a destra la grandezza cresce.
- **Telefono.** Prova tutto a 375, 768 e 1280 px. Aree di tocco almeno 44 px. Riquadri secondari sotto la figura sul telefono.

## 5. Primo lotto: Giornata Terza
In quest'ordine, una scheda per volta:
1. **Moto equabile**: definizione, assiomi e Teorema I (tempi come spazi a velocità costante). Due mobili, cursori, la proporzione che si legge sulla figura.
2. **Moto naturalmente accelerato**:
   - la definizione (velocità che cresce in proporzione al tempo);
   - il **Teorema I** (teorema della velocità media): il triangolo delle velocità e il rettangolo di uguale area;
   - il **Teorema II** con il **Corollario I**: spazi come quadrati dei tempi, e la regola dei numeri dispari 1, 3, 5, 7, con una caduta animata a intervalli uguali.
3. **Esperimento del piano inclinato**, alle righe ~1320–1336: il regolo di 12 braccia, la palla di bronzo, il canale con la cartapecora, l'orologio ad acqua.
   - La simulazione permette di cambiare l'inclinazione e di «pesare l'acqua».
   - Produce una tabella di misure con un errore realistico e dichiarato.
   - Lo studente verifica la proporzione come faceva Galileo («replicate ben cento volte»).
   - Distingui bene che cosa dice il testo da che cosa è simulato.

Dopo il lotto:
- **Giornata Quarta**: parabola come composizione di moto equabile e accelerato (Prop. I); le tavole delle gittate, da confrontare con la formula moderna secondo la skill delle osservazioni;
- **Giornata Prima**: pendolo e isocronismo, caduta nel vuoto e nei mezzi, la trave a sbalzo.

## 6. Verifica e consegna
- **Verifica.** Ogni scheda passa da un **revisore indipendente**, un agente che non l'ha costruita, prima che la consideri finita. Applica la skill di verifica: fedeltà al testo, matematica, controllo numerico, interfaccia a 375, 768 e 1280 px.
- **Test.** Il container non raggiunge le CDN: installa `three@0.128.0` con npm e prova una copia con gli script locali in Chrome headless (swiftshader). Nel libro sfogliabile controlla che nessuna pagina debordi.
- **Pubblicazione.** Prima come **artefatto privato**. Se una pagina è già condivisa pubblicamente, aggiornala solo dopo un mio esplicito «aggiorna la pagina pubblica».
- **Salvataggio.** Salva tutto in `~/Projects/digital_books/discorsi/interattivo/`: `build.py`, `template.html`, dati, script di verifica, `index.html`. Deve rigenerarsi sul Mac con `python3 build.py`.
- **Stato.** Aggiorna `claude/galileo-stato-del-progetto.md` (sezione Discorsi).
- **Skill.** Quando impari qualcosa di generale (es. come rendere un dialogo, come trattare le proporzioni), proponimi l'aggiornamento delle skill con lo strumento delle proposte, non con file a parte.

Rispondimi sempre in italiano. Comincia leggendo stato e skill, aprendo il .tex e dicendomi in poche righe:
- che cosa sono i numeri in rubrica;
- da dove viene la traduzione delle parti latine;
- come pensi di impaginare dialogo e enunciati.

Poi parti con la scheda 1.
