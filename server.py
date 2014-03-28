# -*- coding: utf-8 -*-

from flask import Flask, render_template, redirect, url_for, send_from_directory
import json

app = Flask(__name__)

app.Debug = True

@app.route("/")
@app.route("/home")
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

@app.route("/elder-futhark")
def elder_futhark():
  return render_template("main.html", alphabet="elder-futhark")

@app.route("/polish")
def polish():
  return render_template("main.html", alphabet="polish")

@app.route("/armenian")
def armenian():
  return render_template("main.html", alphabet="armenian")

@app.route("/turkish")
def turkish():
  return render_template("main.html", alphabet="turkish")

@app.route("/data/<alphabet>")
def data(alphabet):
    ancgreek = [
        ("Α α", "a", "alpha"),
        ("B β", "b", "beta"),
        ("Γ γ", "ɡ", "gamma"),
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
    elder_futhark = [
        ("ᚠ", "f", "fehu"),
        ("ᚢ", "u", "uruz"),
        ("ᚦ", "θ", "þurisaz"),
        ("ᚦ", "ð", "þurisaz"),
        ("ᚨ", "a", "ansuz"),
        ("ᚱ", "r", "raido"),
        ("ᚲ", "k", "kaunan"),
        ("ᚷ", "ɡ", "gebo"),
        ("ᚹ", "w", "wunjo"),
        ("ᚺ ᚻ", "h", "hagalaz"),
        ("ᚾ", "n", "naudiz"),
        ("ᛁ", "i", "isaz"),
        ("ᛃ", "j", "jera"),
        ("ᛇ", "æ", "ihwaz"),
        ("ᛈ", "p", "perþ"),
        ("ᛉ", "z", "algiz"),
        ("ᛊ", "s", "sowilo"),
        ("ᛏ", "t", "tiwaz"),
        ("ᛒ", "b", "berkanan"),
        ("ᛖ", "e", "ehwaz"),
        ("ᛗ", "m", "mannaz"),
        ("ᛚ", "l", "laguz"),
        ("ᛜ ᛝ", "ŋ", "ingwaz"),
        ("ᛟ", "o", "oþila"),
        ("ᛞ", "d", "dagaz")
    ]
    russian = [
        ("A a", "ä", "a"),
        ("Б б", "b", "b"),
        ("В в", "v", "вэ"),
        ("Г г", "ɡ", "гэ"),
        ("Д д", "d", "дэ"),
        ("Е е", "je", "e"),
        ("Ё ё", "jo", "ё"),
        ("Ж ж", "ʐ", "ж"),
        ("З з", "z", "зэ"),
        ("И и", "i", "и"),
        ("Й й", "j", "й"),
        ("К к", "k", "ка"),
        ("Л л", "l", "эл"),
        ("М м", "m", "эм"),
        ("Н н", "n", "эн"),
        ("О о", "o", "o"),
        ("П п", "p", "пэ"),
        ("Р р", "r", "эр"),
        ("С с", "s", "эс"),
        ("T т", "t", "тэ"),
        ("У у", "u", "y"),
        ("Ф ф", "f", "эф"),
        ("Х х", "x", "xa"),
        ("Ц ц", "ts", "це"),
        ("Ч ч", "tɕ", "че"),
        ("Ш ш", "ʂ", "ша"),
        ("Щ щ", "ɕ", "ща"),
        ("Ъъ"),
        ("Ы ы", "ɨ", "ы"),
        ("Ьь"),
        ("Ээ", "ɛ", "э"),
        ("Ю ю", "ju", "ю"),
        ("Я я", "ja", "я")

    ]
    polish = [
        ("A a", "ä", "a"),
        ("Ą ą", "ɔ̃", "ą"),
        ("B b", "b", "be"),
        ("C c", "ts", "ce"),
        ("Ć ć", "tɕ", "cie"),
        ("D d", "d", "de"),
        ("E e", "ɛ", "e"),
        ("Ę ę", "ɛ̃ ", "ę"),
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
    armenian = [
        ("Ա ա", "ɑ", "ayb"),
        ("Բ բ", "b", "ben"),
        ("Գ գ", "ɡ", "gim"),
        ("Դ դ", "d", "da"),
        ("Ե ե", "ɛ", "yeč"),
        ("Զ զ", "z", "za"),
        ("Է է", "ɛ", "ē"),
        ("Ը ը", "ə", "ët"),
        ("Թ թ", "t", "to"),
        ("Ժ ժ", "ʒ", "zhe"),
        ("Ի ի", "i", "ini"),
        ("Լ լ", "l", "lyown"),
        ("Խ խ", "χ", "xe"),
        ("Ծ ծ", "ts", "ça"),
        ("Կ կ", "k", "ken"),
        ("Հ հ", "h", "ho"),
        ("Ձ ձ", "z", "tsa"),
        ("Ղ ղ", "ɫ", "gat"),
        ("Ճ ճ ", "tʃ", "č̣e"),
        ("Մ մ", "m", "men"),
        ("Յ յ", "j", "yi"),
        ("Ն ն", "n", "now"),
        ("Շ շ", "ʃ", "ša"),
        ("Ո ո", "o", "vo"),
        ("Չ չ", "tʃ", "ča"),
        ("Պ պ", "p", "pe"),
        ("Ջ ջ", "dʒ", "je"),
        ("Ռ ռ", "r", "ra"),
        ("Ս ս", "s", "se"),
        ("Վ վ", "v", "vev"),
        ("Տ տ", "t", "tyown"),
        ("Ր ր", "ɹ", "re"),
        ("Ց ց", "s", "c'o"),
        ("ՈՒ Ու", "u", "u"),
        ("Փ փ", "p", "pywor"),
        ("Ք ք", "k", "ke"),
        ("Օ օ", "o", "o"),
        ("Ֆ ֆ", "f", "fe")
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
        ("g", "ɡ", ""),
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
    elif alphabet == "russian":
        return json.dumps(russian)
    elif alphabet == "turkish":
        return json.dumps(turkish)
    elif alphabet == "bib-hebrew":
        return json.dumps(bib_hebrew)
    elif alphabet == "mod-hebrew":
        return json.dumps(mod_hebrew)
    elif alphabet == "elder-futhark":
        return json.dumps(elder_futhark)
    elif alphabet == "polish":
        return json.dumps(polish)
    elif alphabet == "armenian":
        return json.dumps(armenian)
    else:
        return "Error"