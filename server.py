# -*- coding: utf-8 -*-

from flask import Flask, render_template, redirect, url_for, send_from_directory
import json

app = Flask(__name__)

@app.route("/")
def intro():
  return render_template("intro.html")

@app.route("/ancient-greek")
def ancient_greek():
    return render_template("main.html", alphabet="anc-greek")
  
@app.route("/russian")
def russian():
  return render_template("main.html", alphabet="russian")

@app.route("/data/<alphabet>")
def data(alphabet):
    ancgreek = {
        "Α α": ("a", "alpha"),
        "B β": ("b", "beta"),
        "Γ γ": ("g", "gamma"),
        "Δ δ": ("d", "delta"),
        "E ε": ("e", "epsilon"),
        "Z ζ": ("z", "zeta"),
        "H η": ("u025b", "eta"),
        "Θ θ": ("th", "theta"),
        "Ι ι": ("i", "iota"),
        "K κ": ("k", "kappa"),
        "Λ λ": ("l", "lambda"),
        "M μ": ("m", "mu"),
        "N ν": ("n", "nu"),
        "Ξ ξ": ("ks", "xi"),
        "O o": ("o", "omicron"),
        "Π π": ("p", "pi"),
        "P ρ": ("r", "rho"),
        "Σ σ": ("s", "sigma"),
        "T t": ("t", "tau"),
        "Y υ": ("y", "upsilon"),
        "Φ φ": ("p", "phi"),
        "Χ χ": ("k", "chi"),
        "Ψ ψ": ("ps", "psi"),
        "Ω ω": ("u0254", "omega")
    }
    cyrillic = {
        "A a": ("u00E4", "a"),
        "Б б": ("b", "бэ"),
        "В в": ("v", "вэ"),
        "Г г": ("g", "гэ"),
        "Д д": ("d", "дэ"),
        "E e": ("je", "е"),
        "Ё ё": ("jo", "ё"),
        "Ж ж": ("u0290", "жэ"),
        "З з": ("z", "зэ"),
        "И и": ("i", "и"),
        "Й й": ("j", "и краткое"),
        "К к": ("k", "ка"),
        "Л л": ("l", "эл"),
        "М м": ("m", "эм"),
        "Н н": ("n", "эн"),
        "О о": ("o", "o"),
        "П п": ("p", "пэ"),
        "Р р": ("r", "эр"),
        "С с": ("s", "эс"),
        "Т т": ("t", "тэ"),
        "У у": ("u", "y"),
        "Ф ф": ("f", "эф"),
        "Х х": ("х", "хa"),
        "Ц ц": ("ts", "це"),
        "Ч ч": ("tch", "че"),
        "Ш ш": ("s?", "ша"),
        "Щ щ": ("chch", "ща"),
        "Ы ы": ("u0268", "ы"),
        "Э э": ("u025B", "э"),
        "Ю ю": ("ju", "ю"),
        "Я я": ("ja", "я")
    }
    if alphabet == "anc-greek":
        return json.dumps(ancgreek)
    elif alphabet == "russian":
        return json.dumps(cyrillic)