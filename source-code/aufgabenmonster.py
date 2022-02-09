import os
import subprocess
import sys
from satzmetzger.satzmetzger import Satzmetzger
from maximize_console import maximize_console
from add_color_print_reg import *
import bs4
import regex
import pickle
from menudownload import *
from exercise_from_word import *
from deep_translator import GoogleTranslator
import sprache_auswaehlen
metzgerle = Satzmetzger()
drucker=Farbprinter()
cfg = {}

def read_pkl(filename):
    with open(filename, 'rb') as f:
        data_pickle = pickle.load(f)
    return data_pickle

def get_file_path(datei):
    pfad = sys.path
    pfad = [x.replace('/', '\\') + '\\' + datei for x in pfad]
    exists = []
    for p in pfad:
        if os.path.exists(p):
            exists.append(p)
    return list(dict.fromkeys(exists))


def txtdateien_lesen(text):
    try:
        dateiohnehtml = (
            b"""<!DOCTYPE html><html><body><p>""" + text + b"""</p></body></html>"""
        )
        soup = bs4.BeautifulSoup(dateiohnehtml, "html.parser")
        soup = soup.text
        return soup.strip()
    except Exception as Fehler:
        print(Fehler)

def niveau_checken(textzusammen, pkldatei):
    suchen = read_pkl(pkldatei)
    gefundenewoerter =suchen.findall(textzusammen)
    gefundenewoerter = list(dict.fromkeys([wort for wort in gefundenewoerter if len(wort) > 1]))
    return len(gefundenewoerter)


if __name__ == '__main__':
    print(1000 * "\n")
    maximize_console(lines=30000)
    add_color_print_to_regedit()
    colorfunctionslogo = [drucker.f.black.red.normal, drucker.f.black.brightyellow.normal]
    drucker.p_ascii_front_on_flag_with_border(
        text="Aufgabenmonster",
        colorfunctions=colorfunctionslogo,
        bordercolorfunction=drucker.f.brightgreen.black.italic,
        font="slant",
        width=1000,
        offset_from_left_side=5,
        offset_from_text=15,
    )
    colorfunctionspage = [
        drucker.f.black.brightwhite.normal,
        drucker.f.black.brightgreen.normal,
    ]
    drucker.p_ascii_front_on_flag_with_border(
        text="www . queroestudaralemao . com . br",
        colorfunctions=colorfunctionspage,
        bordercolorfunction=drucker.f.brightgreen.black.negative,
        font="slant",
        width=1000,
        offset_from_left_side=1,
        offset_from_text=1,
    )
    updates_quero_estudar_alemao()
    p = subprocess.run(get_file_path(r"Everything2TXT.exe")[0], capture_output=True)
    ganzertext2 = txtdateien_lesen(p.stdout)
    ganzertext = ganzertext2
    textalsliste = metzgerle.zerhack_den_text(ganzertext)
    einzelnewoerter = regex.findall(r'\b[a-zA-ZäöüßÄÖÜ-]+\b', ganzertext)
    einzelnewoerter = list(dict.fromkeys([wort for wort in einzelnewoerter if len(wort) > 1]))
    allewoerterimtext = len(einzelnewoerter)
    textzusammen = ' '.join(einzelnewoerter)
    a1=niveau_checken(textzusammen, 'a1vokabelliste_suchen.qea')
    a2=niveau_checken(textzusammen, 'a2vokabelliste_suchen.qea')
    b1=niveau_checken(textzusammen, 'b1vokabelliste_suchen.qea')
    b2=niveau_checken(textzusammen, 'b2vokabelliste_suchen.qea')
    print(drucker.f.black.brightyellow.bold('\nIm Text sind insgesamt ') + drucker.f.brightyellow.black.normal(f'   {allewoerterimtext}  ') + drucker.f.black.brightyellow.bold('verschiedene Wörter.\n'), end=' ' )
    print(drucker.f.black.brightgreen.bold('\nDavon lernt man ') + drucker.f.brightgreen.black.normal(f'   {a1}  ') + drucker.f.black.brightgreen.bold(' Wörter in Stufe A1\n'), end=' ' )
    print(drucker.f.black.brightmagenta.bold('\nDavon lernt man ') + drucker.f.brightmagenta.black.normal(f'   {a2}  ') + drucker.f.black.brightmagenta.bold(' Wörter in Stufe A2\n'), end=' ' )
    print(drucker.f.black.brightcyan.bold('\nDavon lernt man ') + drucker.f.brightcyan.black.normal(f'   {b1}  ') + drucker.f.black.brightcyan.bold(' Wörter in Stufe B1\n'), end=' ' )
    print(drucker.f.black.brightblue.bold('\nDavon lernt man ') + drucker.f.brightblue.black.normal(f'   {b2}  ') + drucker.f.black.brightblue.bold(' Wörter in Stufe B2\n'), end=' ')




    return_choice = drucker.f.black.brightcyan.italic(
        " <-- Gib diese Nummer ein, sobald du alles korrigiert hast!\n"
    )
    prompt = drucker.f.black.magenta.bold(
        """\nDeine Eingabe: \n"""
    )

    gewaehltes = auswahlmenu_erstellen(optionen=['A1', 'A2', 'B1', 'B2'], uberschrift='Welches Niveau?', color='brightcyan', unterdemtext='\nBitte Niveau eingeben: \n')

    if gewaehltes == '1':
        regexsuche = read_pkl('a1vokabelliste_suchen.qea')
    if gewaehltes == '2':
        regexsuche = read_pkl('a2vokabelliste_suchen.qea')

    if gewaehltes == '3':
        regexsuche = read_pkl('b1vokabelliste_suchen.qea')

    if gewaehltes == '4':
        regexsuche = read_pkl('b2vokabelliste_suchen.qea')

    prozentwegmachen = ''
    while not isinstance(prozentwegmachen, int):
        try:
            prozentwegmachen = input(drucker.f.black.brightblue.italic('\nWie viel Prozent von den Wörtern wegschneiden?\n'))
            prozentwegmachen = int(prozentwegmachen)
            if prozentwegmachen >100:
                prozentwegmachen=''
        except:
            print(drucker.f.black.brightred.normal('\nFalsche Eingabe!\n'))

            continue
    gueltigeauswahl_liste  = ['1', '2', '3']
    gueltigeauswahl = '0'
    start_end_random = 'beginning'
    while not gueltigeauswahl in gueltigeauswahl_liste:
        try:
            gueltigeauswahl = input(drucker.f.black.brightblue.italic('\nArt der Aufgabe:\n1) Zufällig: Situation -> Si__a__o_ \n2) Anfang: Situation -> ____ation \n3) Ende: Situation -> Situa____ \n'))
            gueltigeauswahl = str(gueltigeauswahl).strip()
            print(gueltigeauswahl)
        except:
            print(drucker.f.black.brightred.normal('\nFalsche Eingabe!\n'))

            continue
    if gueltigeauswahl == '1':
        start_end_random = 'random'

    if gueltigeauswahl == '2':
        start_end_random = 'start'

    if gueltigeauswahl == '3':
        start_end_random = 'end'

    spracheubersetzen = sprache_auswaehlen.get_sprache('\nAuf welche Sprache sollen die Sätze übersetzt werden\n')[1]


    for satzdruckeneditiert in textalsliste:
        ganzersatz_split = regex.split(r"[^a-zA-ZäöüßÄÖÜ-]+", satzdruckeneditiert)
        ganzersatz_split = [x for x in ganzersatz_split if len(x) > 0]
        erstellteaufgabe = []
        korrekteantwort = []
        for wort in ganzersatz_split:
            korrekteantwort.append(wort)
            if any(regexsuche.findall(wort)):
                erstellteaufgabe.append(exercise_from_word(wort, percentage=50, start_end_random=start_end_random))
                continue
            erstellteaufgabe.append(wort)
        try:
            uebersetzter_text = GoogleTranslator(source='de', target=spracheubersetzen).translate(satzdruckeneditiert)
        except:
            uebersetzter_text = ''
            print(drucker.f.black.brightred.normal('\nFalsche Eingabe!\n'))

        cfg = {str(key + 1): x for key, x in enumerate(erstellteaufgabe)}
        kurzbeschreibung_aufgabe = drucker.f.black.brightyellow.italic(
            f"\nVervollständige den Satz!\n{uebersetzter_text}\n"
        )
        cfg = m.config_menu(
            kurzbeschreibung_aufgabe,
            cfg.copy(),
            return_choice=return_choice,
            prompt=prompt,
    )
        gegebeneantworten = [item for key,item in cfg.items()]
        matches =[]
        notmatches=[]
        for gegebenantwort, richtigantwort in zip(gegebeneantworten,korrekteantwort):
            if gegebenantwort.strip() == richtigantwort.strip():
                matches.append(richtigantwort)
            elif gegebenantwort.strip() != richtigantwort.strip():
                notmatches.append(richtigantwort)

        moeglichepunkte = len(korrekteantwort)
        print(f'\n{drucker.f.black.brightgreen.negative("Korrekte Antworten")}\n', end='')
        for rr in matches:
            richtigea=drucker.f.black.brightgreen.italic(f"\n{rr}\n")
            print(richtigea, end='')

        print(f'\n{drucker.f.black.brightred.negative("Falsche Antworten")}\n', end='')
        for rr in notmatches:
            falschea = drucker.f.black.brightred.italic(f"\n{rr}\n")
            print(f'{falschea}', end='')
        print(drucker.f.black.brightyellow.italic(f'\n{len(matches)} richtige Antworten / {len(notmatches)} falsche Antworten\n'))

