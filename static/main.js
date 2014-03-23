ipa = {
    "b": "http://upload.wikimedia.org/wikipedia/commons/a/a8/Voiced_bilabial_stop.ogg",
    "a": "http://upload.wikimedia.org/wikipedia/commons/6/65/Open_front_unrounded_vowel.ogg",
    "g": "http://upload.wikimedia.org/wikipedia/commons/transcoded/5/58/Voiced_velar_stop.ogg/Voiced_velar_stop.ogg.ogg",
    "e": "http://upload.wikimedia.org/wikipedia/commons/6/6c/Close-mid_front_unrounded_vowel.ogg",
    "d": "http://upload.wikimedia.org/wikipedia/commons/f/f3/Voiced_alveolar_stop.ogg",
    "k": "http://upload.wikimedia.org/wikipedia/commons/e/e3/Voiceless_velar_plosive.ogg",
    "i": "http://upload.wikimedia.org/wikipedia/commons/9/91/Close_front_unrounded_vowel.ogg",
    "o": "http://upload.wikimedia.org/wikipedia/commons/8/84/Close-mid_back_rounded_vowel.ogg",
    "n": "http://upload.wikimedia.org/wikipedia/commons/2/29/Alveolar_nasal.ogg",
    "m": "http://upload.wikimedia.org/wikipedia/commons/a/a9/Bilabial_nasal.ogg",
    "l": "http://upload.wikimedia.org/wikipedia/commons/b/bc/Alveolar_lateral_approximant.ogg",
    "s": "http://upload.wikimedia.org/wikipedia/commons/a/ac/Voiceless_alveolar_sibilant.ogg",
    "r": "http://upload.wikimedia.org/wikipedia/commons/c/ce/Alveolar_trill.ogg",
    "p": "http://upload.wikimedia.org/wikipedia/commons/3/35/Voiceless_bilabial_stop.ogg",
    "t": "http://upload.wikimedia.org/wikipedia/commons/e/e0/Voiceless_alveolar_stop.ogg",
    "p\\u02b0": "https://dl.dropboxusercontent.com/s/e2qzl1mm4zpfkoj/ph.ogg?token_hash=AAEbU-1NoTTvUPLp2bt9oxE73o2SVv9xI9iISUWWalosag",
    "y": "http://upload.wikimedia.org/wikipedia/commons/e/ea/Close_front_rounded_vowel.ogg",
    "k\\u02b0": "https://dl.dropboxusercontent.com/s/guqbo5xwhj5f7ib/kh.ogg?token_hash=AAHZEW_RsBrHz33CCt8SD24GdQfaj2DNbq3MugMthIhkHQ",
    "dz": "http://upload.wikimedia.org/wikipedia/commons/d/d8/Voiced_alveolar_sibilant_affricate.oga",
    "ps": "https://dl.dropboxusercontent.com/s/3w1ywt5rhd8y59e/ps.ogg?token_hash=AAGQGPHwAUvhV5laBfGErNUyWmP1gZRxNqI3kjc2HiCPuw",
    "t\\u02b0": "http://upload.wikimedia.org/wikipedia/commons/e/e0/Voiceless_alveolar_stop.ogg",
    "\\u0254": "http://upload.wikimedia.org/wikipedia/commons/0/02/Open-mid_back_rounded_vowel.ogg",
    "\\u025b": "http://upload.wikimedia.org/wikipedia/commons/7/71/Open-mid_front_unrounded_vowel.ogg",
    "ks": "https://dl.dropboxusercontent.com/s/fwegk0q7uamqbe7/ks.ogg?token_hash=AAFfY--szpKho5xE-OYQiybQjf8NOmKxrDzgmdpTmXsFZw"
}

setAudio = function(url) {
  $("#audio").attr("src", url);
  $("#audio").get(0).play();
}

getAlphabet = function (alphabet) {
    $.getJSON(("http://harlaw-96324.use1-2.nitrousbox.com:5000/data/" + alphabet), function (data) {
        $.each(data, function (key, value) {
            $(".table").append("<tr id=\'" + key[0] + "\'><td>" + key + "</td><td>" +  value[1] +"</tr>");
            var ipavalue = ipa[value[0]];
            $("#" + key[0]).on("click", function() {
                setAudio(ipavalue);
            })            
        })
    })
}