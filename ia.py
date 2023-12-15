import random
def ia(board, signe):
    cases_vides = [i for i, cell in enumerate(board) if cell == '']
    if cases_vides:
        choix_ia = random.choice(cases_vides)
        print(f"L'IA choisit la case {choix_ia}")
        return choix_ia
    else:
        return -1



