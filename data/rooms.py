class Room:  
    def __init__(self, name, exits, items, enemies):
        self.name = name
        self.exits = exits
        self.items = items
        self.enemies = enemies
    
    def get_items(self):
        res = "<пусто>"
        if self.items:
            res = " ".join(str(item) for item in self.items)
        return res

    def get_enemies(self):
        res = "<пусто>"
        if self.items:
            res = " ".join(str(enemie) for enemie in self.enemies)
        return res
        
    def __str__(self):
        return ('\n' + \
'######################################\n\t' 
+f'Вы попали в {self.name}\n'
+'######################################\n'
+'Выходы есть только:\n\t'
+f'{self.exits}\n'
+'В комнате лежит:\n\t'
+f'{self.get_items()}\n'
+'В комнате находятся:\n\t'
+f'{self.get_enemies()}\n')
