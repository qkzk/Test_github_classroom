'''
titre:  Implémente le calcul de la moyenne d'une liste de nombres
auteur: qkzk
date:   2020/10/28
'''


def moyenne(nombres: list) -> int:
    somme = 0
    longueur = 0
    for nombre in nombres:
        somme += nombre
        longueur += 1
    moyenne = somme / longueur
