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
    ancgreek = [
        ("Α α", "a", "alpha"),
        ("B β", "b", "beta"),
        ("Γ γ", "g", "gamma"),
        ("Δ δ", "d", "delta"),
        ("E ε", "e", "epsilon"),
        ("Z ζ", "z", "zeta"),
        ("H η", "ɛ", "eta"),
        ("Θ θ", "th", "theta"),
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
    if alphabet == "anc-greek":
        return json.dumps(ancgreek)