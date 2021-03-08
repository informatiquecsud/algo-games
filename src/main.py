from random import randint, choice, random

import justpy as jp

class State:
    nb_clicked = 0
        

class Card(jp.Button):
    
    def __init__(self, index, value, onclick, max_clicks=-1, **kwargs):
        self.value = value
        self.index = index
        self.show_value = False
        self.onclick = onclick
        self.max_clicks = max_clicks
        self.nb_clicks = 0
        super().__init__(**kwargs)
        
        self.on('click', self.clicked)
        
    def clicked(self, e):
        if self.max_clicks < 0 or self.nb_clicks < self.max_clicks:
            self.onclick(index=self.index, value=self.value)
            self.nb_clicks += 1
        
    def hightlight(self):
        pass
    
    def turn(self, highlight="bg-red-4"):
        self.show_value = not self.show_value        
        if highlight in self.classes:
            # remove the hightlight class from the classes
            self.classes = "".join(self.classes.split(highlight))
        else:
            self.classes += " bg-red-4"
        
    def react(self, data):
        if self.show_value:
            self.text = str(self.value)
        else:
            self.text = str(self.index)
        
class CardList(jp.Div):
    
    def __init__(self, values, **kwargs):
        self.values = values
        super().__init__(**kwargs)
        self.cards = []
        
        self.stats = jp.Div(a=self, classes="q-pa-sm bg-grey-3")
        self.number_to_find = jp.Div(a=self.stats, classes="q-ml-sm q-mb-sm")
        self.nb_clicked = jp.Div(a=self.stats, classes="q-ml-sm ")
        self.btn_reset = jp.Button(a=self.stats, 
            classes="bg-primary q-pa-sm q-ma-md text-white",
            text="Réinitialiser")
        self.btn_reset.on("click", self.reset_clicked)
        self.card_container = None
        
        self.reset()
        
    def reset(self):        
        max_value_length = max([len(str(x)) for x in self.values])
                    
        if self.card_container:
            self.card_container.delete()
            
        self.card_container = jp.Div(a=self, classes="q-ma-md")
        
        for i, value in enumerate(self.values):
            card = Card(a=self.card_container, value=value, index=i, 
                onclick=self.clicked,
                max_clicks=1,
                classes="primary q-ma-xs q-pa-sm", style=f"width: {max_value_length}em")
            self.cards.append(card)
                        
        number_to_find = choice(self.values)
        self.number_to_find.text = "Nombre à trouver: " + str(number_to_find)
        
        State.nb_clicked = 0
        
                
    def clicked(self, index, value):
        card_clicked = self.cards[index]            
        card_clicked.turn()
        State.nb_clicked += 1
        
    def reset_clicked(self, e):
        self.reset()
        
        
    def react(self, data):
        self.nb_clicked.text = f"Nombre d'essais: {State.nb_clicked}"
        
        
        
        
    

def html_consigne(number_to_find, binary_search_comparisons):
    return f'''
        <q-banner class="bg-primary text-white">
            <div class="text-h6">Recherche dichotomique</div>
            <div class="text-subtitle2">Trouver un nombre parmi les cartes triées dans l'ordre croissant</div>
        </q-banner>
        '''

def generate_random_numbers(a, size, distribution):
    values = []
    number_min = a
    count = 0
    for i, interval in enumerate(distribution):
        if i == len(distribution) - 1:
            numbers_to_generate = size - count
        else:
            numbers_to_generate = int(size / len(distribution))
            
        for _ in range(numbers_to_generate):
            number = randint(number_min, number_min + interval)
            values.append(number)
            number_min = number + 1
            count += 1
            
                        
    print("values generated", values)

    return values
    

def quasar_example():
    wp = jp.QuasarPage()
    
    size = 50
    number_min = 10
    interval = 30
    
    consigne = jp.parse_html(html_consigne(number_to_find=50, binary_search_comparisons=5), a=wp)
    container = jp.Div(classes="container q-ma-md", a=wp)
        
    a = int(size * 0.01)
    distribution = [5, 30, 60, 4, 15, 70]
    values = generate_random_numbers(a, size, distribution)
    CardList(values=values, a=wp, classes="q-ma-xs q-pa-sm")

    return wp

jp.justpy(quasar_example)