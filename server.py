# -*- coding: utf-8 -*-

from flask import Flask, render_template, redirect, url_for, send_from_directory
import json

app = Flask(__name__)

app.debug = True

@app.route("/")
def intro():
  return render_template("intro.html")

@app.route("/ancient-greek")
def ancient_greek():
    return render_template("main.html", alphabet="anc-greek")
  
@app.route("/russian")
def russian():
  return render_template("main.html", alphabet="russian")

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
        ("j", "ʒ", "")
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
        ("z", "ð", ""),
    ]
    if alphabet == "anc-greek":
        return json.dumps(ancgreek)
    elif alphabet == "turkish":
        return json.dumps(turkish)