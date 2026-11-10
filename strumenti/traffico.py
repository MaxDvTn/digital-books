#!/usr/bin/env python3
"""Salva il traffico del repository GitHub, che GitHub conserva solo per 14 giorni.

Lo lancia ogni giorno la GitHub Action .github/workflows/traffico.yml e aggiorna, nella cartella data:
  visite.csv        data, visite, visitatori unici (pagine del repository su github.com)
  clonazioni.csv    data, clonazioni, cloni unici
  provenienze.csv   data del rilevamento, sito di provenienza, visite e unici negli ultimi 14 giorni
  pagine.csv        data del rilevamento, percorso, visite e unici negli ultimi 14 giorni

Le righe giornaliere si aggiornano (l'ultimo giorno è parziale), le altre si aggiungono.
Variabili d'ambiente: GH_TOKEN (token con permesso di lettura su Administration), REPO (owner/nome), CARTELLA.
"""
import csv, datetime, json, os, sys, urllib.request

REPO = os.environ.get("REPO", "MaxDvTn/digital-books")
TOKEN = os.environ.get("GH_TOKEN", "")
CARTELLA = os.environ.get("CARTELLA", "statistiche")


def api(percorso):
    req = urllib.request.Request("https://api.github.com/repos/%s/traffic/%s" % (REPO, percorso), headers={
        "Authorization": "Bearer " + TOKEN, "Accept": "application/vnd.github+json", "X-GitHub-Api-Version": "2022-11-28"})
    with urllib.request.urlopen(req, timeout=30) as r:
        return json.load(r)


def giornaliero(nome, chiave, dati, intest):
    f = os.path.join(CARTELLA, nome)
    righe = {}
    if os.path.exists(f):
        with open(f, newline="", encoding="utf-8") as fh:
            for r in csv.reader(fh):
                if r and r[0] != "data":
                    righe[r[0]] = r
    for x in dati.get(chiave, []):
        g = x["timestamp"][:10]
        righe[g] = [g, str(x["count"]), str(x["uniques"])]
    with open(f, "w", newline="", encoding="utf-8") as fh:
        w = csv.writer(fh)
        w.writerow(intest)
        for g in sorted(righe):
            w.writerow(righe[g])


def istantanea(nome, dati, campo, intest, oggi):
    f = os.path.join(CARTELLA, nome)
    nuovo = not os.path.exists(f)
    righe = []
    if not nuovo:
        with open(f, newline="", encoding="utf-8") as fh:
            righe = [r for r in csv.reader(fh) if r and r[0] != "data" and r[0] != oggi]
    with open(f, "w", newline="", encoding="utf-8") as fh:
        w = csv.writer(fh)
        w.writerow(intest)
        w.writerows(righe)
        for x in dati:
            w.writerow([oggi, x[campo], x["count"], x["uniques"]])


def main():
    if not TOKEN:
        sys.exit("manca GH_TOKEN")
    os.makedirs(CARTELLA, exist_ok=True)
    oggi = datetime.date.today().isoformat()
    giornaliero("visite.csv", "views", api("views"), ["data", "visite", "visitatori_unici"])
    giornaliero("clonazioni.csv", "clones", api("clones"), ["data", "clonazioni", "cloni_unici"])
    istantanea("provenienze.csv", api("popular/referrers"), "referrer", ["data", "provenienza", "visite_14g", "unici_14g"], oggi)
    istantanea("pagine.csv", api("popular/paths"), "path", ["data", "percorso", "visite_14g", "unici_14g"], oggi)
    print("traffico salvato in", CARTELLA)


if __name__ == "__main__":
    main()
