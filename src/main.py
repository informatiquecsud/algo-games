from random import randint


import justpy as jp

from utils import generate_random_numbers
from cards import Card, CardList

app = jp.app
    
MAX_CARDS_NUM = 5000

def html_consigne():
    return f'''
        <q-banner class="bg-primary text-white">
            <div class="text-h6">Recherche dichotomique</div>
            <div class="text-subtitle2">Trouver un nombre parmi les cartes triées dans l'ordre croissant</div>
        </q-banner>
        '''


def not_found_404(request):
    wp = jp.QuasarPage()
    
    banner = jp.parse_html('''
        <q-banner class="bg-warning text-white">
            <div class="text-h6">Impossible de trouver la page</div>
            <div class="text-subtitle2">Erreur 404 : la page demandée n'existe pas</div>
        </q-banner>
    ''', a=wp)
    
    return wp
    

@jp.SetRoute('/binarysearch')
def binary_search(request):
    wp = jp.QuasarPage()
    
    
    size = int(request.query_params.get('size', 50))
    
    consigne = jp.parse_html(html_consigne(), a=wp)
    container = jp.Div(classes="container q-ma-md", a=wp)

    if size > MAX_CARDS_NUM:
        error_msg = f"Indiquez un nombre de cartes inférieur à {MAX_CARDS_NUM}"
        error_message = jp.QBanner(a=wp, text=error_msg, classes="bg-red-4 text-white")
        return wp
        
        
    a = randint(0, 3000)
    nb_groups = randint(5, 10)
    distribution = [randint(0, 800) for _ in range(nb_groups)]
    # distribution = [5, 30, 60, 4, 15, 70]
    values = generate_random_numbers(a, size, distribution)
    CardList(values=values, a=wp, classes="q-ma-xs q-pa-sm")

    return wp

jp.justpy(not_found_404)


