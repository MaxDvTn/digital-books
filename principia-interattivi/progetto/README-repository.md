# Principia interattivi

Edizione didattica e interattiva dei *Philosophiæ Naturalis Principia Mathematica* di Isaac Newton, per il liceo scientifico. Ogni dimostrazione è tradotta in italiano frase per frase, e una figura si costruisce passo dopo passo insieme al testo. Le figure si possono manipolare: si trascinano i punti, e un cursore porta le grandezze al limite.

Stato: **bozza di lavoro (pilota)**. Repository privato.

## Contenuto del pilota

| Vista | Testo | Stato |
|---|---|---|
| `#leggi` | Leggi I–III, Corollario I | verificata |
| `#lemma-1` | Libro I, Lemma I (rapporti ultimi) | verificata |
| `#prop-1` | Libro I, Prop. I (legge delle aree) | verificata |
| `#prop-11` | Libro I, Prop. XI (forza verso il fuoco dell'ellisse) | verificata |

## Struttura

```
site/            pagina pubblicata (index.html autosufficiente)
sorgenti/        template.html + build.py, che incorpora immagini e CSS; p11_* sono le parti della Prop. XI
traduzione/      fascicoli della traduzione dal latino (01 Definizioni, 02 Scolio, 03 Leggi)
fonti/           testo inglese di Motte (ed. 1846, Project Gutenberg #76404) estratto in testo semplice
verifiche/       script Python delle verifiche numeriche indipendenti, una cartella per proposizione
strumenti/       estrazione dall'EPUB (x2t.py) e test con Chrome headless (shot*.py)
```

Il latino del 1726 (trascrizione del Newton Project) si usa per lavorare ma **non va incluso nel repository pubblico** finché non se ne chiariscono le condizioni d'uso.

## Come rigenerare la pagina

```bash
python3 sorgenti/build.py        # crea principia.html dal template
```

I percorsi in `build.py` vanno adattati alla propria macchina. Le librerie (JSXGraph 1.10.1 e MathJax 3.2.2 in versione SVG) si caricano da jsDelivr.

## Metodo di lavoro

1. Il testo si estrae dalla fonte. Non si lavora mai a memoria.
2. Traduzione frase per frase, con un glossario fisso: *vis insita* → «forza insita», *motus* → «quantità di moto» dove serve, *in directum* → «in linea retta», ecc.
3. Ogni passo della dimostrazione diventa un passo della costruzione geometrica.
4. Verifica **indipendente**: un revisore che non ha prodotto il lavoro controlla fedeltà, matematica e numeri con script propri.
5. Approvazione del docente prima della pubblicazione.

## Note testuali emerse

- Prop. XI, seconda dimostrazione: l'edizione Motte 1846 stampa PE²/SP². Il latino 1726 (*PE cub./SPq*) e Motte 1729 hanno **PE³/SP²**, coerente con il Cor. 3 della Prop. VII. Il refuso è dell'edizione 1846; nelle pagine si segnala in nota.
- Assiomi, Scolio: la trascrizione del Newton Project omette *invenit* («Galilæus invenit»), presente nella stampa del 1726. Altri refusi della trascrizione sono elencati nel Fascicolo 3, § A.

## Fonti e diritti

- Newton, *Principia*, trad. A. Motte, Londra 1729 e New York, D. Adee, 1846: pubblico dominio (Project Gutenberg #76404; Internet Archive).
- Latino 1726: trascrizione © The Newton Project (per i fascicoli di traduzione); controlli sulla stampa tramite la scansione ECCO su Internet Archive.

## Licenza

- Testi, traduzione italiana, note e apparati: **CC BY-SA 4.0**.
- Codice (pagine interattive, script di costruzione e di verifica): **MIT**.
- Lavoro originale con assistenza di IA (Claude, ChatGPT).

Curatore: Massimo Bosetti, Liceo Scientifico «Leonardo da Vinci», Trento.
