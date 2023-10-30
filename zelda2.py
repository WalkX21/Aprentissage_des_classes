

class Link():
    
    def __init__(self, name, health, armor, power , weapon):
        self.name = name
        self.health = health
        self.armor = armor
        self.power = power 
        self.weapon = weapon

    def print_info(self):
        print('', self.name)
        print('PV:', self.health)
        print('armor', self.armor)
        print('power', self.power)
        print('Weapon', self.weapon)
    
    def strike(self, enemy):
        print(
            '-> ATTAQUE!! ' + self.name + ' ATTAQUE ' + enemy.name + ' avec une force de ' + str(self.power) + ' avec un(e) ' + self.weapon + '\n')
        
        enemy.armor -= self.power
        if enemy.armor < 0:
            enemy.health += enemy.armor
            enemy.armor = 0
        if enemy.health < 0:
                enemy.health = 0

        print('Vos Pv sont à ' + str(self.health) + '\n' + 'Les Pv de ' + enemy.name + ' decendent à ' + str(enemy.health))
        
        print(
            enemy.name + 'est afaibli . \n La defence de ' + enemy.name + ' decend à '
            + str(enemy.armor) + ', et les PV de ' + enemy.name + ' decendent à ' +
            str(enemy.health) + '\n')


    def fight(self, enemy):
        print(
             self.name + ' decide de se battre contre ' + enemy.name 

        )
        
        
        while self.health and enemy.health > 0:
            self.strike(enemy)
            
           
                
        print(
            enemy.name + ' est mort \n' + 'Vos Pv decendent à ' + str(self.health) + ' et Votre defence à '+ str(self.armor) )
        # +'\n' + str(self.power)
        



            
            



        


