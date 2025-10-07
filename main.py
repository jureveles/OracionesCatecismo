# -*- coding: utf-8 -*-
"""
Created on Wed Feb 22 19:51:51 2023

@author: jreveles
"""

from kivy.app import App
from kivy.lang import Builder
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.properties import StringProperty

from kivy.config import Config
Config.set('graphics', 'width', '360')
Config.set('graphics', 'height', '640')

default_font = Config.get('kivy', 'default_font')
print(default_font)

fonts = [
    'OpenSans', 'fonts/OpenSans-Regular.ttf',
    'fonts/OpenSans-Italic.ttf',
    'fonts/OpenSans-Bold.ttf'
]
Config.set('kivy', 'default_font', fonts)
default_font = Config.get('kivy', 'default_font')
print(default_font)

# Define our different screens
class MainScreen(Screen):
    pass
class ScreenOne(Screen):
    pass
class ScreenTwo(Screen):
    pass
class ScreenThree(Screen):
    pass
class ScreenFour(Screen):
    pass
class ScreenFive(Screen):
    pass
class ScreenSix(Screen):
    pass
class ScreenSeven(Screen):
    pass
class ScreenEight(Screen):
    pass
class MainScreenE(Screen):
    pass
class ScreenOneE(Screen):
    pass
class ScreenTwoE(Screen):
    pass
class ScreenThreeE(Screen):
    pass
class ScreenFourE(Screen):
    pass
class ScreenFiveE(Screen):
    pass
class ScreenSixE(Screen):
    pass
class ScreenSevenE(Screen):
    pass
class ScreenEightE(Screen):
    pass


class WindowManager(ScreenManager):
    factor = StringProperty('00')
    from my_sounds import stop_sounds_reset, on_button_play
    from my_sounds import on_button_release, on_button_stop
    
    def __init__(self,**kwargs):
        super().__init__()
    
            
# .kv design file with the screens and prayers
kv = Builder.load_file('new_windows.kv')

# The main class of the application
class OracionesCatecismo(App):
    def build(self):
        return kv
    
if __name__ == '__main__':
    OracionesCatecismo().run()
    