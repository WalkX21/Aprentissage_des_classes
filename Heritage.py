from time import sleep

class Hero():
    #class constructor
    def __init__(self, name, health, armor):
        self.name = name
        self.health = health #number
        self.armor = armor #string
    #print character parameters
    def print_info(self):
        print('Health level:', self.health)
        print('Armor class:', self.armor, '\n')

#then program the derived classes of the Hero superclass

class Warrior(Hero):

    def hello(self):
        print("NEW HERO. A brave warrior appears riding a horse who is named ", self.name)
        self.print_info()


    def attack(self,evil):


        print(
            'HIT! A brave warrior ',self.name ,'is attacking ' ,evil.name ,' by sword!')

        if evil.armor < 0:
            evil.health = evil.health + evil.armor
            evil.armor = 0

        print(
            'A terrible blow fell upon the enemy.',
            "\n Now it's armor:" ,str(evil.armor), "\n health level: ", str(evil.health )
        
        )
            
class Magician(Hero):

    def hello(self):
        print("NEW HERO. A brave magician appears riding a horse who is named ", self.name)
        self.print_info()


    def attack(self,evil):


        print(
            'HIT! A brave magician ',self.name ,'is attacking ' ,evil.name ,' by sword!')

        if evil.armor < 0:
            evil.health = evil.health + evil.armor
            evil.armor = 0

        print(
            'A terrible blow fell upon the enemy.',
            "\n Now it's armor:" ,str(evil.armor), "\n health level: ", str(evil.health )
        
        )


Warior1 = Warrior('abdoul', 100, 100)
Warior1.hello()

magicianred = Magician("stand_of_abdul",200,400)
magicianred.hello()

Warior1.attack(magicianred)
magicianred.attack(Warior1)


    


