class Critter(object):
    """Виртуальный питомец"""

    total = 0

    def __init__(self, name, mood):
        self.name = name
        self.__mood = mood
        print(f'Появилась на свет новая зверушка! По имени {self.name}')
        Critter.total = Critter.total + 1
      
    # def talk(self, name):
    #     print(f'Привет {name}. Я зверушка - экземпляр класса Critter.')

    def __str__(self) -> str:
        return self.name

    @staticmethod
    def status():
        print(f'Статический метод {Critter.total}')

    def talk(self):
        print(f'Привет. Я зверушка - экземпляр класса Critter.{self.__mood} По имени {self.name}')

print(Critter.total)
#Critter.total = Critter.total + 1
Critter.status()

crit1 = Critter('лапа', 'hello')
crit2 = Critter("шлёпа", 'oppss')

print(crit1.name)
print(crit1._Critter__mood) #доступ к закрытым отребутам класса

crit1.talk()
crit2.talk()
print(crit1.total)
print(crit2.total)

Critter.status()