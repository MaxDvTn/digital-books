#!/usr/bin/env python3
"""Pagina di copertina comune ai libri interattivi (Galileo, Newton).

Uso dentro un build.py:
    sys.path.insert(0, os.path.join(<digital_books>, "strumenti"))
    import copertina
    html = copertina.html(json.load(open("copertina.json")), cartella_del_json)
    css  = copertina.CSS
e nel template: %%COPERTINA_CSS%% dentro <style>, %%COPERTINA%% in <main> prima di #testo.

La copertina sta FUORI da #testo: il libro sfogliabile non la impagina, ma ne riusa
il frontespizio antico (CONF.frontespizioDa = "#copertina .cop-fac img").
Controlli: il facsimile deve esistere; ogni tavola deve puntare a un id che esiste nella pagina
(lo verifica controlla_ancore, da chiamare sul testo HTML finale).
"""
import base64, html as H, json, os, re, sys

CSS = r"""
/* ---------------- copertina (strumenti/copertina.py) ---------------- */
.copertina{min-height:calc(100svh - 60px);display:flex;align-items:center;justify-content:center;padding:1.2rem 0 1.6rem;
  width:min(980px,calc(100vw - 2.4rem));margin-left:calc(50% - min(490px,50vw - 1.2rem))}
.cop-cornice{width:100%;border:3px double var(--rubrica);outline:1px solid var(--linea);outline-offset:5px;background:var(--carta);
  padding:1.6rem 1.4rem 1.3rem;display:grid;grid-template-columns:minmax(0,1fr);grid-template-areas:"alto" "fac" "basso";gap:1rem 1.8rem}
.cop-alto{grid-area:alto;text-align:center;min-width:0}
.cop-basso{grid-area:basso;text-align:center;min-width:0}
.cop-fac{grid-area:fac;margin:0;text-align:center}
.cop-fac img{width:min(100%,300px);height:auto;mix-blend-mode:multiply;filter:sepia(.25) contrast(1.05);border:1px solid var(--linea);box-shadow:0 6px 18px rgba(60,40,20,.12);background:#fff}
.cop-fac figcaption{font:.72rem/1.4 Inter,system-ui,sans-serif;color:var(--dato);margin-top:.35rem}
.cop-autore{font-variant:small-caps;letter-spacing:.18em;font-size:1.05rem;margin:0 0 .5rem}
.cop-titolo{font-weight:400;font-variant:small-caps;color:var(--rubrica);font-size:clamp(1.6rem,7vw,3.1rem);line-height:1.05;letter-spacing:.04em;overflow-wrap:break-word;margin:.2rem 0 .3rem;text-align:center}
.cop-titolo2{font-variant:small-caps;letter-spacing:.12em;font-size:1.15rem;margin:0 0 .6rem}
.cop-sotto{font-style:italic;color:var(--dato);font-size:.98rem;line-height:1.45;margin:0 auto .5rem;max-width:30em}
.cop-fregio{display:block;margin:.6rem auto;width:180px;height:18px}
.cop-luogo{font-variant:small-caps;letter-spacing:.14em;margin:.2rem 0 0}
.cop-edizione{font:600 .74rem Inter,system-ui,sans-serif;text-transform:uppercase;letter-spacing:.12em;color:var(--rubrica);margin:.2rem 0 .3rem}
.cop-crediti{font-size:.9rem;color:var(--dato);margin:0 0 .8rem;line-height:1.45}
.cop-tavole{display:block;overflow:visible;text-align:left;margin:.4rem auto .9rem;max-width:26rem}
.cop-tavole .cop-et{font:600 .68rem Inter,system-ui,sans-serif;text-transform:uppercase;letter-spacing:.1em;color:var(--dato);margin:0 0 .25rem;text-align:center}
.cop-tavole ol{list-style:none;margin:0;padding:0;border-top:1px solid var(--linea)}
.cop-tavole li{border-bottom:1px solid var(--linea)}
.cop-tavole a,.cop-tavole span.prossima{font-family:"EB Garamond",Georgia,serif;white-space:normal;border:0;border-radius:0;display:flex;align-items:center;gap:.6rem;min-height:44px;padding:.2rem .3rem;line-height:1.3;color:var(--inchiostro);text-decoration:none;font-size:1rem}
.cop-tavole a:hover,.cop-tavole a:focus{background:var(--pannello)}
.cop-tavole .n{font-variant:small-caps;color:var(--rubrica);min-width:3.4em;flex:none;white-space:nowrap;font-size:.9rem;letter-spacing:.05em}
.cop-tavole .dove{margin-left:auto;flex:none;padding-left:.4rem;font:.7rem Inter,system-ui,sans-serif;color:var(--dato);white-space:nowrap}
.cop-tavole span.prossima{color:var(--dato)}
.cop-azioni{display:flex;flex-wrap:wrap;justify-content:center;gap:.6rem;margin:.4rem 0 .9rem}
.cop-azioni .b{font-family:Inter,system-ui,sans-serif;text-decoration:none;display:inline-flex;align-items:center;font-size:.9rem;padding:.55rem 1rem;min-height:44px}
.cop-azioni .b.primo{background:var(--rubrica);color:#fff;border-color:var(--rubrica)}
.cop-piede{font:.7rem/1.5 Inter,system-ui,sans-serif;color:var(--dato);margin:0}
@media(min-width:860px){
  .cop-cornice{grid-template-columns:minmax(0,1.15fr) minmax(0,.85fr);grid-template-areas:"alto fac" "basso fac";padding:2.2rem 2.2rem 1.6rem;align-items:center}
  .cop-fac img{width:100%;max-width:340px}
  .cop-basso{align-self:start}
}
@media(max-width:767px){.copertina{min-height:0;padding-top:.6rem;width:auto;margin-left:0}.cop-cornice{padding:1.2rem .9rem 1rem}.cop-fac img{width:min(70%,260px)}}
"""

FREGIO = ('<svg class="cop-fregio" viewBox="0 0 180 18" aria-hidden="true">'
          '<line x1="4" y1="9" x2="72" y2="9" stroke="currentColor" stroke-width="1"/>'
          '<line x1="108" y1="9" x2="176" y2="9" stroke="currentColor" stroke-width="1"/>'
          '<path d="M90 2 L98 9 L90 16 L82 9 Z" fill="none" stroke="currentColor" stroke-width="1.2"/>'
          '<circle cx="90" cy="9" r="2" fill="currentColor"/><circle cx="76" cy="9" r="1.6" fill="currentColor"/>'
          '<circle cx="104" cy="9" r="1.6" fill="currentColor"/></svg>')

ROMANI = ["I", "II", "III", "IV", "V", "VI", "VII", "VIII", "IX", "X", "XI", "XII"]


def _uri(percorso):
    ext = percorso.rsplit(".", 1)[1].lower()
    mime = "jpeg" if ext in ("jpg", "jpeg") else "png"
    return "data:image/%s;base64,%s" % (mime, base64.b64encode(open(percorso, "rb").read()).decode())


def _dim_png(percorso):
    with open(percorso, "rb") as f:
        t = f.read(24)
    return int.from_bytes(t[16:20], "big"), int.from_bytes(t[20:24], "big")


def html(c, base):
    """c: dizionario letto da copertina.json; base: cartella da cui risolvere i percorsi del json."""
    e = lambda s: H.escape(s, quote=True)
    fac = c["facsimile"]
    f = os.path.join(base, fac["file"])
    if not os.path.exists(f):
        sys.exit("copertina: facsimile mancante: " + f)
    w, h = _dim_png(f)
    tav = []
    for i, t in enumerate(c.get("tavole", [])):
        n = '<span class="n">Tav. %s</span>' % ROMANI[i]
        dove = '<span class="dove">%s</span>' % e(t["dove"]) if t.get("dove") else ""
        if t.get("id"):
            tav.append('<li><a href="#%s">%s<span>%s</span>%s</a></li>' % (t["id"], n, e(t["titolo"]), dove))
        else:
            tav.append('<li><span class="prossima">%s<span>%s</span><span class="dove">in preparazione</span></span></li>' % (n, e(t["titolo"])))
    tavole = ('<nav class="cop-tavole" aria-label="Tavole interattive"><p class="cop-et">Tavole interattive</p><ol>%s</ol></nav>' % "".join(tav)) if tav else ""
    crediti = "<br>".join(c.get("crediti", []))   # possono contenere <i>: html fidato, scritto dai curatori
    return f"""<section id="copertina" class="copertina" aria-labelledby="copTitolo">
<div class="cop-cornice">
<div class="cop-alto">
<p class="cop-autore">{e(c["autore"])}</p>
<h1 id="copTitolo" class="cop-titolo">{c["titolo"]}</h1>
{('<p class="cop-titolo2">%s</p>' % c["titolo2"]) if c.get("titolo2") else ""}
<p class="cop-sotto">{c["sottotitolo"]}</p>
{FREGIO}
<p class="cop-luogo">{c["luogo"]}</p>
</div>
<figure class="cop-fac"><img src="{_uri(f)}" width="{w}" height="{h}" alt="{e(fac["alt"])}"><figcaption>{fac["didascalia"]}</figcaption></figure>
<div class="cop-basso">
<p class="cop-edizione">{e(c["edizione"])}</p>
<p class="cop-crediti">{crediti}</p>
{tavole}
<div class="cop-azioni"><a class="b primo" href="#testo">Comincia a leggere ↓</a><button class="b" type="button" id="copLibro">📖 Sfoglia il libro</button></div>
<p class="cop-piede">{c["piede"]}</p>
</div>
</div>
<script>(function(){{var b=document.getElementById("copLibro"),l=document.getElementById("btnLibro");if(b&&l)b.addEventListener("click",function(){{l.click();}});else if(b)b.hidden=true;}})();</script>
</section>"""


def controlla_ancore(c, pagina):
    """Ogni tavola con id deve puntare a un elemento che esiste nella pagina finale."""
    mancanti = [t["id"] for t in c.get("tavole", []) if t.get("id") and ('id="%s"' % t["id"]) not in pagina]
    if mancanti:
        sys.exit("copertina: tavole senza destinazione nella pagina: %s" % mancanti)


if __name__ == "__main__":   # anteprima: python3 copertina.py copertina.json > anteprima.html
    p = sys.argv[1]
    c = json.load(open(p, encoding="utf-8"))
    print("<!DOCTYPE html><html lang=it><meta charset=utf-8><meta name=viewport content='width=device-width,initial-scale=1'>"
          "<style>:root{--carta:#fbf8f2;--inchiostro:#22201c;--rubrica:#871919;--dato:#6b6458;--linea:#d9d1c3;--pannello:#f3eee4}"
          "body{margin:0 auto;max-width:880px;padding:0 1rem;background:var(--carta);font:19px/1.6 'EB Garamond',Georgia,serif;color:var(--inchiostro)}"
          ".b{border:1px solid var(--linea);border-radius:8px;background:#fff;color:inherit;font-family:Inter,sans-serif}" + CSS + "</style>"
          + html(c, os.path.dirname(os.path.abspath(p))))
