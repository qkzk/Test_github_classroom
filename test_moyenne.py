'''
titre:  teste la moyenne
auteur: qkzk
date: 2020/10/28
'''

import moyenne


def test_moyenne():
    '''teste la fonction moyenne'''

    # pas d'égalité entre les flottants
    assert abs(moyenne.moyenne([1, 2, 3]) - 2) < 1e-6
    assert abs(moyenne.moyenne([0]) - 0) < 1e-6
    assert abs(moyenne.moyenne([-1, 2, 3]) - 4 / 3) < 1e-6
