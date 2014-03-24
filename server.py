# -*- coding: utf-8 -*-

from flask import Flask, render_template, redirect, url_for, send_from_directory
import json

app = Flask(__name__)

app.Debug = True

@app.route("/")
def intro():
  return render_template("intro.html")

@app.route("/ancient-greek")
def ancient_greek():
    return render_template("main.html", alphabet="anc-greek")
  

@app.route("/biblical-hebrew")
def biblical_hebrew():
    return render_template("main.html", alphabet="bib-hebrew")
  
@app.route("/modern-hebrew")
def modern_hebrew():
    return render_template("main.html", alphabet="mod-hebrew")
  
@app.route("/russian")
def russian():
  return render_template("main.html", alphabet="russian")

@app.route("/icelandic")
def icelandic():
  return render_template("main.html", alphabet="icelandic")

@app.route("/vietnamese")
def vietnamese():
  return render_template("main.html", alphabet="vietnamese")

@app.route("/turkish")
def turkish():
  return render_template("main.html", alphabet="turkish")

@app.route("/data/<alphabet>")
def data(alphabet):
    ancgreek = [
        ("Α α", "a", "alpha"),
        ("B β", "b", "beta"),
        ("Γ γ", "g", "gamma"),
        ("Δ δ", "d", "delta"),
        ("E ε", "e", "epsilon"),
        ("Z ζ", "z", "zeta"),
        ("H η", "ɛ", "eta"),
        ("Θ θ", "t", "theta"),
        ("Ι ι", "i", "iota"),
        ("K κ", "k", "kappa"),
        ("Λ λ", "l", "lambda"),
        ("M μ", "m", "mu"),
        ("N ν", "n", "nu"),
        ("Ξ ξ", "ks", "xi"),
        ("O o", "o", "omicron"),
        ("Π π", "p", "pi"),
        ("P ρ", "r", "rho"),
        ("Σ σ", "s", "sigma"),
        ("T t", "t", "tau"),
        ("Y υ", "y", "upsilon"),
        ("Φ φ", "p", "phi"),
        ("Χ χ", "k", "chi"),
        ("Ψ ψ", "ps", "psi"),
        ("Ω ω", "ɔ", "omega")
    ]
    bib_hebrew = [
        ("א", "ʔ", "aleph"),
        ("ב", "b", "bet"),
        ("ג", "ɡ", "gimel"),
        ("ד", "d", "dalet"),
        ("ה", "h", "he"),
        ("ו", "w", "vav"),
        ("ז", "z", "zayin"),
        ("ח", "ħ", "het"),
        ("ט", "t", "tet"),
        ("י", "j", "yod"),
        ("כ ך", "k", "kaf"),
        ("ל", "l", "lamed"),
        ("מ ם", "m", "mem"),
        ("נ ן", "n", "nun"),
        ("ס", "s", "semkh"),
        ("ע", "ʕ", "ayin"),
        ("פ ף", "p", "pe"),
        ("צ  ץ", "s", "tsadi"),
        ("ק", "k", "qof"),
        ("ר", "ɾ", "resh"),
        ("ש", "ɬ", "shin"),
        ("ת", "t", "tav")]
    mod_hebrew = [
        ("א", "ʔ", "aleph"),
        ("ב", "b", "bet"),
        ("ג", "ɡ", "gimel"),
        ("ד", "d", "dalet"),
        ("ה", "h", "he"),
        ("ו", "v", "vav"),
        ("ז", "z", "zayin"),
        ("ז׳", "ʒ", ""),
        ("ח", "ħ", "het"),
        ("ט", "t", "tet"),
        ("י", "j", "yod"),
        ("כ ך", "χ", "kaf"),
        ("ל", "l", "lamed"),
        ("מ ם", "m", "mem"),
        ("נ ן", "n", "nun"),
        ("ס", "s", "semkh"),
        ("ע", "ʕ", "ayin"),
        ("פ ף", "p", "pe"),
        ("צ  ץ", "ts", "tsadi"),
        ("ק", "k", "qof"),
        ("ר", "ʁ", "resh"),
        ("ש", "s", "shin"),
        ("ת", "t", "tav")]
    polish = [
        ("A a", "ä", "a"),
        #("Ą ą", "ɔ̃ ", "ą"),
        ("B b", "b", "be"),
        ("C c", "t̪͡s̪", "ce"),
        ("Ć ć", "t͡ɕ", "cie"),
        ("D d", "d̪", "de"),
        ("E e", "ɛ", "e"),
        #("Ę ę", "ɛ̃ ", "ę"),
        ("F f", "f", "ef"),
        ("G g", "ɡ", "gie"),
        ("H h", "x", "ha"),
        ("I i", "i", "i"),
        ("J j", "j", "jot"),
        ("K k", "k", "ka"),
        ("L l", "l", "el"),
        ("Ł ł", "w", "eł"),
        ("M m", "m", "em"),
        ("N n", "n", "en"),
        ("Ń ń", "ɲ", "eɲ"),
        ("O o", "ɔ", "o"),
        ("Ó ó", "u", "ó"),
        ("P p", "p", "pe"),
        ("R r", "r", "er"),
        ("S s", "s", "es"),
        ("Ś ś", "ɕ", "eś"),
        ("T t", "t", "te"),
        ("U u", "u", "u"),
        ("W w", "v", "vu"),
        ("Y y", "ɘ", "igrek"),
        ("Z z", "z", "zet"),
        ("Ź ź", "ʐ", "ziet"),
        ("Ż ż", "ʐ", "żet")
    ]
    turkish = [
        ("a", "a", ""),
        ("a", "ɑ", ""),
        ("b", "b", ""),
        ("c", "dʒ", ""),
        ("ç", "tʃ", ""),
        ("d", "d", ""),
        ("e", "æ", ""),
        ("e", "e", ""),
        ("f", "f", ""),
        ("g", "g", ""),
        ("g", "ɟ", ""),
        ("ğ", "ɰ", "yumuşak ge"),
        ("h", "h", ""),
        ("i", "i", ""),
        ("ı", "ɯ", ""),
        ("j", "ʒ", ""),
        ("k", "k", ""),
        ("l", "l", ""),
        ("m", "m", ""),
        ("n", "n", ""),
        ("o", "o", ""),
        ("ö", "ø", ""),
        ("p", "p", ""),
        ("r", "ɾ", ""),
        ("s", "s", ""),
        ("s", "θ", ""),
        ("ş", "ʃ", ""),
        ("t", "t", ""),
        ("u", "u", ""),
        ("ü", "y", ""),
        ("y", "j", ""),
        ("v", "v", ""),
        ("z", "z", ""),
        ("z", "ð", "")
    ]
    if alphabet == "anc-greek":
        return json.dumps(ancgreek)
    elif alphabet == "turkish":
        return json.dumps(turkish)
    elif alphabet == "bib-hebrew":
        return json.dumps(bib_hebrew)
    elif alphabet == "mod-hebrew":
        return json.dumps(mod_hebrew)
    elif alphabet == "polish":
        return json.dumps(polish)
    else:
        return "Error"