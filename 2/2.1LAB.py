# Создание класса томатов
class Tomato:
    states = {1: 'Отсутствует(-ют)', 2:'Цветёт(-ут)', 3: 'Зеленый(-ые)', 4: 'Красный(-ые)'}      # статическое свойсво

    def __init__(self, index):      # создание томатов
        self._index = index
        self._state = 1

    def grow(self):     # переводит на след стадию
        if self._state < 4:
            self._state += 1
            self._print_state()

    def is_ripe(self):      # проверка на зрелость
        if self._state == 4:
            return True
        else:
            return False
    
    def _print_state(self): # Информация для меня, потому что я рукожоп
        print(f'Помидор(-ы) {self._index} сейчас {Tomato.states[self._state]}')


# создание томатного куста
class TomatoBush:
    def __init__(self, num):        # количество томатов на кусте
        self.tomatoes = [Tomato(index) for index in range(1, num+1)]

    def grow_all(self):     # томаты зреют
        for tomato in self.tomatoes:
            tomato.grow()

    def all_are_ripe(self):     # проверка все ли томаты созрели
        return all([tomato.is_ripe() for tomato in self.tomatoes])

    def give_away_all(self):        # сбор урожая
        self.tomatoes = []
        print("Собираем урожай!")


class Gardener:
    def __init__(self, name, plant):
        self.name = name
        self._plant = plant

    def work(self):     # садовник работает
        print(self.name + " работает...")
        self._plant.grow_all()
        print(self.name + " закончил работать")

    def harvest(self):      # проверка плодов на зрелость и сбор урожая
        print(self.name + " собирает урожай")
        if self._plant.all_are_ripe():
            self._plant.give_away_all()
            print("Урожай Собран!")
            return True
        else:
            print("!!!Не все томаты созрели!!!")
            return False


    @staticmethod
    def knowlenge_base():
        print("Справка по садоводству: ")
        print("За томатами нужно ухаживать: поливать, удобрять, а также своевременно собирать урожай")


# Тесты
if __name__ == '__main__':

    # 1
    Gardener.knowlenge_base()

    # 2
    bush = TomatoBush(2)
    gardener = Gardener("Иван", bush)

    # 3
    gardener.work()

    # 4
    gardener.harvest()
    
    # 5, 6
    print('Цирк цикловой:')
    while not gardener.harvest():
        gardener.work()
