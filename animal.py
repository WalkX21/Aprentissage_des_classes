class Animal():
    def __init__(self, look, voice):
        self.look = look 
        self.voice = voice

    def make_voice(self):
        print ( 
            str(self.voice) + (" ") + str(self.voice) )
        
    def print_info(self):

        print("I'm a robot-" + str(self.look) + '. I know the voice command: ')
        


lapin = Animal("dog","waff" )
lapin.print_info()
lapin.make_voice()