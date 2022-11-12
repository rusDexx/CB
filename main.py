import random
from kivy.app import App
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.uix.button import Button
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.gridlayout import GridLayout
from kivy.uix.label import Label
from kivy.uix.textinput import TextInput

from bulls import get_dict_words
dict_words = get_dict_words()

class ScreenOne(Screen):


    def __init__(self,**kwargs):
        super().__init__(**kwargs)


        boxlayout = BoxLayout(orientation="vertical")      #упорядочить по вертикали

        self.insert_num_letter = TextInput(                     # ТЕКСТОВОе поле

        size_hint = (1, 0.2),
        multiline = False
        )

        button = Button(                                    # кнопка
            text="Введите количество букв в слове",
            font_size=24,
            size_hint=(1, 1),
            background_color=(1, 2, 3, 1),
            color=(1, 1, 1, 1),
            on_press=self.on_press_button

        )

        self.add_widget(boxlayout)
        boxlayout.add_widget(self.insert_num_letter)
        boxlayout.add_widget(button)


    def on_press_button(self,instance,*args):
        num = int(self.insert_num_letter.text)
        print(num)
        word = random.choice(dict_words[num])

        self.manager.screens[1].setWord(word)
        self.manager.transition.direction = 'left'
        self.manager.current = 'two'



class ScreenTwo(Screen):

    def __init__(self, **kwargs):
        super().__init__(**kwargs)


#########################Графическая оболочка##################################
        self.label_word = Label(                      ### текстовое поле
            text= "",
            font_size=48

        )
        self.label_cows = Label(                       ### текстовое поле
            text="",
            font_size=24

        )

        self.boxlayout = BoxLayout(orientation="vertical")      #упорядочить по вертикали
        self.insert_word = TextInput(                     # ТЕКСТОВОе поле

        size_hint = (1, 0.2),
        multiline = False
        )


        self.button = Button(                                    # кнопка
            text="Отгадайте слово !",
            size_hint=(1, 1),
            background_color=(1, 2, 3, 1),
            color=(1, 1, 1, 1),
            on_press=self.gaming_button

        )
#######################################################################################

        self.add_widget(self.boxlayout)
        self.boxlayout.add_widget(self.insert_word)
        self.boxlayout.add_widget(self.button)
        self.boxlayout.add_widget(self.label_word)
        self.boxlayout.add_widget(self.label_cows)

################### генерируем слово##########################################################

    def setWord(self, new_word):
        self.word = new_word
        self.label_word.text = '*' * len(self.word)
        print(self.word)

###################### функция игровой кнопки ввода слова пользователем ##############################

    def gaming_button(self,instance,*args):
        word_t = self.insert_word.text
        self.manager.screens[1].game_center(word_t)

############ Игровой процесс ###################################################################

    def game_center(self,insert):
        total = 0
        cows = []
        self.insert = insert

        word = self.word
        print(insert)
        print(word)
        slovo = list(('*' * len(word)))

        for index, letter in enumerate(word):
            total += 1
            if letter == insert[index]:
                slovo[index] = letter
            if letter in insert and letter not in slovo:
                cows.append(letter)
        if word == insert:
            self.label_cows.text = f"Угадал c {total} попытки!!! Поздравляю старина!"

        else:
            self.label_word.text = str(slovo)
            if len(cows) >= 1:
                self.label_cows.text = f"Так же вы нашли эти коровки - {cows}"











class Bulls(App):
    def build(self):
        sm = ScreenManager()
        sm.add_widget(ScreenOne(name='one'))
        sm.add_widget(ScreenTwo(name='two'))

        return sm


if __name__ == "__main__":
    Bulls().run()




