from random import choices

def sonderzeichen_ersetzen(wort):
    wort = wort.replace(':u', 'ü')
    wort = wort.replace(':a', 'ä')
    wort = wort.replace(':o', 'ö')
    wort = wort.replace(':U', 'Ü')
    wort = wort.replace(':A', 'Ä')
    wort = wort.replace(':O', 'Ö')
    wort = wort.replace('sz', 'ß')
    return wort

def exercise_from_word(word, percentage, start_end_random='random'):
    """wortzumanzeigen = exercise_from_word(word='Situation', percentage=50, start_end_random='random')
print(wortzumanzeigen)
wortzumanzeigen = exercise_from_word(word='Situation', percentage=50, start_end_random='end')
print(wortzumanzeigen)
wortzumanzeigen = exercise_from_word(word='Situation', percentage=50, start_end_random='start')
print(wortzumanzeigen)"""
    anzeigen = []

    laengewort = len(word)
    wortalsliste = [x for x in word]
    wortalsliste = [(y, x) for y, x in enumerate(wortalsliste)]
    if start_end_random == 'start':
        wegmachen = int(laengewort / (100 / percentage))
        for indi, w in enumerate(wortalsliste):
            if indi < wegmachen:
                anzeigen.append('_')
                continue
            anzeigen.append(w[1])

    if start_end_random == 'end':
        wegmachen = int(laengewort / (100 / percentage))
        for indi, w in enumerate(wortalsliste):
            if indi < wegmachen:
                anzeigen.append(w[1])
                continue
            anzeigen.append('_')

    if start_end_random == 'random':
        rausmachen = choices(wortalsliste, weights=[1] * laengewort,
                             k=int(laengewort / (100 / percentage)))
        for w in wortalsliste:
            if w in rausmachen:
                anzeigen.append('_')
                continue
            anzeigen.append(w[1])
    wortzumanzeigen = ''.join(anzeigen)
    return wortzumanzeigen