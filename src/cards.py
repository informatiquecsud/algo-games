from random import choice

import justpy as jp

class CardState:
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
            self.cards = []
            
        self.card_container = jp.Div(a=self, classes="q-ma-md")
        
        for i, value in enumerate(self.values):
            card = Card(a=self.card_container, value=value, index=i, 
                onclick=self.clicked,
                max_clicks=1,
                classes="primary q-ma-xs q-pa-sm", style=f"width: {max_value_length}em")
            self.cards.append(card)
                        
        number_to_find = choice(self.values)
        self.number_to_find.text = "Nombre à trouver: " + str(number_to_find)
        
        CardState.nb_clicked = 0
        
                
    def clicked(self, index, value):
        card_clicked = self.cards[index]            
        card_clicked.turn()
        CardState.nb_clicked += 1
        
    def reset_clicked(self, e):
        self.reset()
        
        
    def react(self, data):
        self.nb_clicked.text = f"Nombre d'essais: {CardState.nb_clicked}"
        
