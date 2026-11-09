# Digital Books — classici della scienza interattivi

Edizioni didattiche e interattive di testi fondativi della fisica, per il liceo scientifico. Le dimostrazioni prendono vita: le figure si costruiscono passo dopo passo insieme al testo e si possono manipolare.

**Sito:** https://maxdvtn.github.io/digital-books/

| Libro | Cartella | Stato |
|---|---|---|
| Newton, *Principia* (traduzione italiana dal latino del 1726) | `principia-interattivi/` | traduzione completa v0.1 (27 fascicoli), pagina pilota interattiva v0.4.1 |
| Galileo, *Sidereus Nuncius* (trad. L. Lanzillotta; inglese di E. S. Carlos, 1880) | `sidereus_nuncius/` | libro interattivo v0.3 in italiano e inglese, PDF |
| Galileo, *Discorsi e dimostrazioni matematiche* (inglese di H. Crew e A. de Salvio, 1914) | `discorsi/` | libro interattivo v0.2 in italiano e inglese, PDF |
| Galileo, *Dialogo sopra i due massimi sistemi* | `dialogo_massimi_sistemi/` | edizione LaTeX/PDF |
| Galileo, *Il Saggiatore* | `il_saggiatore/` | edizione LaTeX/PDF |

`strumenti/` contiene gli script comuni (importazione da LaTeX, copertine, motore del libro sfogliabile, `lingue.py` per le pagine in più lingue).

## Lingue

Ogni libro interattivo ha una pagina per lingua (`index.html` in italiano, `index.en.html` in inglese), generate dallo stesso `build.py`. Il menu in alto passa da una lingua all'altra restando allo stesso paragrafo e ricorda la scelta.

- Il testo inglese del libro sta in `blocchi_en.json`, con gli stessi id dei paragrafi italiani; lo produce `allinea_en.py` a partire dalla traduzione storica in `fonti_en/`.
- I testi dell'interfaccia (schede, pulsanti, note) stanno in `i18n/en.json`: coppie italiano → inglese; `"="` vuol dire «lascia com'è». Il build segnala ogni testo senza traduzione.
- Per aggiungere una lingua: una voce in `LINGUE` in `strumenti/lingue.py`, un `blocchi_xx.json` e un `i18n/xx.json` (si genera con `python3 build.py xx --scheletro`).

## Metodo di lavoro

1. Il testo si estrae dalla fonte, mai a memoria.
2. Traduzione frase per frase con un glossario fisso.
3. Ogni passo della dimostrazione diventa un passo della costruzione geometrica.
4. Verifica indipendente di fedeltà, matematica e numeri, con script propri (cartelle `verifiche/`).
5. Approvazione del curatore prima della pubblicazione.

Dettagli sui *Principia*: `principia-interattivi/progetto/README-repository.md` e `principia-interattivi/progetto/stato-del-progetto.md`.

## Fonti e diritti

- **Newton.** Latino 1726: la trascrizione del Newton Project si usa per lavorare ma **non è inclusa** nel repository; i fascicoli pubblicati (`traduzione-pubblica/`) hanno i campi latini della Parte B vuoti e si rigenerano con `strumenti/pubblica_fascicoli.py`. Motte 1729/1846 (Project Gutenberg #76404): pubblico dominio.
- **Galileo.** Testi dall'Edizione Nazionale (Favaro) tramite le edizioni elettroniche di Liber Liber / Progetto Manuzio; *Sidereus Nuncius* nella traduzione di Luisa Lanzillotta (Ricciardi, 1953), distribuita da Liber Liber.
- **Galileo in inglese.** *The Sidereal Messenger*, trad. E. S. Carlos (1880), Project Gutenberg #46036, pubblico dominio. *Dialogues Concerning Two New Sciences*, trad. H. Crew e A. de Salvio (1914), pubblico dominio, nella trascrizione della Online Library of Liberty (Liberty Fund).

## Licenze

- *Principia*: testi, traduzione italiana, note e apparati **CC BY-SA 4.0**.
- Libri di Galileo: testi e apparati **CC BY-NC-SA 4.0**, come le edizioni Liber Liber da cui derivano.
- Codice (pagine interattive, script di costruzione e di verifica): **MIT** (`LICENSE`).

Lavoro originale con assistenza di IA (Claude, ChatGPT).

Curatore: Massimo Bosetti, Liceo Scientifico «Leonardo da Vinci», Trento.
