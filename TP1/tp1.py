from doctest import testmod
from data import L_ETUDIANTS


def pour_tous(l):
    '''
    >>> pour_tous([])
    True
    >>> pour_tous((True, True, True))
    True
    >>> pour_tous((True, False, True))
    False
    '''
    i = 0
    while i < len(l) and l[i]:
        i += 1
    return i == len(l)


def il_existe(l):
    '''
    >>> il_existe([])
    False
    >>> il_existe((False, True, False))
    True
    >>> il_existe((False, False))
    False
    '''
    i = 0
    while i < len(l) and not l[i]:
        i += 1
    return i < len(l)


cList = L_ETUDIANTS[:10]


def est_liste_etu(x):
    '''
    >>> est_liste_etu(cList)
    True
    >>> est_liste_etu('Timoleon')
    False
    >>> est_liste_etu([('12345678', 'Calbuth', 'Raymond', 'Danse', '12')])
    False
    '''
    def est_etu(d):
        '''
        >>> est_etu({'nip': '49284201','nom': 'Remy','prenom': 'Anne','formation': 'SESI','groupe': '14'})
        True
        '''
        return type(d) == dict and [(k, type(d[k])) for k in d] == [('nip', str), ('nom', str), ('prenom', str), ('formation', str), ('groupe', str)]
    return all([est_etu(e) for e in x])


len_L_ETUDIANTS = len(L_ETUDIANTS)
nip = 42211346
v = len_L_ETUDIANTS % nip  # v=583 car len < nip


def liste_des_formations(l):
    '''
    >>> sorted(liste_des_formations(cList)) == ['LICAM', 'MASS', 'PEIP', 'SESI']
    True
    >>> sorted(liste_des_formations(cList[0:2])) == ['PEIP', 'SESI']
    True
    '''
    l2 = []
    for e in l:
        l2.append(e['formation'])
    return set(l2)


def compter_occurrences_prenoms(liste):
    """
    Compter le nombre d'étudiants ayant le même prénom dans la liste d'étudiants passée en paramètre.
    :param liste: liste des étudiants, chacun étant représenté par un dictionnaire contenant les clés 'prenom'
    :return: dictionnaire contenant les prénoms en clé et le nombre d'occurrences en valeur

    >>> compter_occurrences_prenoms([{'prenom': 'Alexandre'}, {'prenom': 'Camille'}, {'prenom': 'Alexandre'}])
    {'Alexandre': 2, 'Camille': 1}
    >>> compter_occurrences_prenoms([{'prenom': 'Camille'}, {'prenom': 'Camille'}])
    {'Camille': 2}
    """
    res = {}
    for etud in liste:
        prenom = etud['prenom']
        if prenom in res:
            res[prenom] = res[prenom] + 1
        else:
            res[prenom] = 1
    return res


def nombre_prenoms_differents(l):
    '''
    Cette fonction prend en paramètre une liste d'étudiants et renvoie le nombre de prénoms différents parmi tous les étudiants.

    Exemples :
    >>> nombre_prenoms_differents(cList)
    9
    >>> nombre_prenoms_differents(L_ETUDIANTS)
    199
    '''
    prenoms = compter_occurrences_prenoms(l)
    return len(prenoms)
    # prenoms = set()
    # for e in l:
    #     prenoms.add(e['prenom'])
    # return len(prenoms)


def prenom_le_plus_frequent(liste):
    '''
    >>> prenom_le_plus_frequent(cList)
    ['David']
    '''
    # Fonctionne en modfiant le fichier data, retournera les deux prénoms ex aequo
    prenoms = compter_occurrences_prenoms(liste)
    max_occurence = max(prenoms.values())
    max_prenoms = [p for p in prenoms if prenoms[p] == max_occurence]
    return max_prenoms


def verifier_nip_distincts(liste):
    nips = {}
    i = 0
    while i < len(liste):
        nip = liste[i]['nip']
        if nip in nips:
            # print("Identifiant en double : ", nip)
            return False
        else:
            nips[nip] = 1
        i += 1
    return True


def compter_occurrences_formations(liste_etudiants):
    '''
    >>> compter_occurrences_formations(cList)
    {'SESI': 6, 'PEIP': 1, 'MASS': 2, 'LICAM': 1}
    '''
    formations = {}
    for etudiant in liste_etudiants:
        formation = etudiant["formation"]
        if formation not in formations:
            formations[formation] = 1
        else:
            formations[formation] += 1
    return formations


testmod(verbose=False)
