import kivy
from kivy.lang.builder import Builder, BuilderBase, BuilderException 
from kivy.uix.floatlayout import FloatLayout
from kivy.uix.gridlayout import GridLayout 
from kivy.uix.scrollview import ScrollView 
from kivymd.uix.scrollview import MDScrollView
from kivy.uix.label import Label
from kivy.properties import ObjectProperty
from kivy.core.window import Window 
from kivy.core.text import LabelBase 
import kivy, os, sys, operator, time 
from kivy.app import App, runTouchApp
from kivymd.app import MDApp 
from pathlib import Path
import struct, threading, pickle 
from kivy.factory import Factory 
from kivy.uix.popup import Popup 
from kivy.uix.screenmanager import NoTransition
from kivy.properties import StringProperty, ObjectProperty
from kivy.uix.filechooser import FileChooser, FileChooserListView, FileChooserIconView
from kivymd.uix.widget import MDWidget
from kivy.uix.relativelayout import RelativeLayout
from kivy.uix.widget import Widget 
from kivymd.uix.screenmanager import MDScreenManager
from kivymd.uix.screen import MDScreen 
from kivymd.uix.label import MDLabel 
from kivy.uix.stacklayout import StackLayout 
from kivy.core.text import LabelBase 
from kivy.utils import get_color_from_hex
from kivymd.uix.button import MDFlatButton, MDRaisedButton, MDRoundFlatButton, MDTextButton 
from kivy.lang import builder, Builder, BuilderBase, BuilderException
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.uix.label import Label
from kivy.core.window import Window
from kivy.uix.scrollview import ScrollView
from kivy.effects.dampedscroll import DampedScrollEffect
from kivy.uix.slider import Slider
from kivy.uix.gridlayout import GridLayout
from kivymd.uix.gridlayout import MDGridLayout
from kivy.uix.textinput import TextInput
from kivy.core.audio import SoundLoader
from kivy.uix.button import Button 
from kivy.uix.boxlayout import BoxLayout
from kivy.animation import Animation, AnimationTransition, CompoundAnimation 
from datetime import datetime
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.uix.widget import Widget 
import datetime 
from kivymd.uix.button import MDRaisedButton 
from kivy.uix.image import Image
import openai

import random

randomval = random.randint(0,9)
randomval2 = random.randint(0,9)
# devBio.update({"newKey": newValue})
randomval3 = random.randint(10,99)
randomval4 = random.randint(10,99)

####add/sub single digits
def kindergarten(greater, lesser):
    x = int
    y = []
    if greater > lesser:
        x = greater - lesser
        print(greater, "-", lesser)
        y.append(x)
        y.append(39)
        y.append(14)
        y.append(15)
        return x
    else:
        x = greater + lesser
        print(greater, "+", lesser)
        y.append(10)
        y.append(x)
        y.append(29)
        y.append(30)
        return x


def doubledigit(greater, lesser):
    one = 1
    two = 2
    x = int
    y = []
    z = random.randint(1, 2)
    if z == 1:
        x = greater + lesser
        print(greater, "+", lesser)
        y.append(4)
        y.append(x)
        y.append(10)
        y.append(12)
        return x
    else:
        x = greater - lesser
        print(greater, "-", lesser)
        y.append(x)
        y.append(17)
        y.append(29)
        y.append(18)
        return x

def multiplication(greater, lesser):
    x = greater * lesser
    y = []
    print(greater, "+", lesser)
    y.append(2)
    y.append(4)
    y.append(1)
    y.append(x)
    return x

def division(greater, lesser):
    x = greater/lesser
    y = []
    print(greater, "/", lesser)
    y.append(28)
    y.append(4)
    y.append(x)
    y.append(3)
    return x


doubledigit(randomval3, randomval4)
multiplication(randomval, randomval2)

#Register Fonts
LabelBase.register(name='LoResWideBold', fn_regular='//Users//Liyat//Downloads//HackTJ//LoRes9OTWide-Bold.ttf')
LabelBase.register(name='LoResReg', fn_regular='//Users//Liyat//Downloads//HackTJ//LoRes9MinusOTWide-Regular.ttf')
LabelBase.register(name='LoResBold', fn_regular='//Users//Liyat//Downloads//HackTJ//LoRes15OT-Bold.ttf')
LabelBase.register(name='LoResSerifReg', fn_regular='//Users//Liyat//Downloads//HackTJ//LoRes21OTSerif-Regular.ttf')
LabelBase.register(name='LoResOakBold', fn_regular='//Users/Liyat//Downloads//HackTJ//LoRes22OTOakland-Bold.ttf')

#Set Screen 
Window.size = (325, 530)
sm = ScreenManager()

#Build Screens
class Opening(MDScreen):
    pass 

class GradeLevel(MDScreen):
    pass

class MinigameTots(MDScreen):
    pass 

class SubjectOpt(MDScreen):
    pass 

class EnglishK(MDScreen):
    pass 

class MathK(MDScreen):
    pass 

class Pets(MDScreen):
    pass 

class Duck(MDScreen):
    pass 

class Cat(MDScreen):
    pass

class Tiger(MDScreen):
    pass 

class Panda(MDScreen):
    pass 

class SiQuiz(MDScreen):
    pass 

class ThKaQuiz(MDScreen):
    pass 

class ReBlQuiz(MDScreen):
    pass 

class SiQuest1(MDScreen):
    pass 

class SiQuest2(MDScreen):
    pass 

class SiQuest3(MDScreen):
    pass 

class SiQuest4(MDScreen):
    pass 

class SiQuest5(MDScreen):
    pass 

class SiQuest6(MDScreen):
    pass 

class SiQuest7(MDScreen):
    pass 

class SiQuest8(MDScreen):
    pass 

class SiQuest9(MDScreen):
    pass 

class SiQuest10(MDScreen):
    pass 

class SiQuest11(MDScreen):
    pass 

class SiQuest12(MDScreen):
    pass 

class SiQuest13(MDScreen):
    pass 

class SiQuest14(MDScreen):
    pass 

class SiQuest15(MDScreen):
    pass 

class SiQuest16(MDScreen):
    pass 

class SiQuest17(MDScreen):
    pass 

class SiQuest18(MDScreen):
    pass 

class SiQuest19(MDScreen):
    pass 

class SiQuest20(MDScreen):
    pass 

class Eval(MDScreen):
    pass 

#OpenAI
API_KEY = "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"
openai.api_key = API_KEY

class SiQuest1(MDScreen):
    def get_question():
        response1 = openai.ChatCompletion.create(
            model="gpt-3.5-turbo",
            messages=[{"role": "assistant", "content": "Give me a very simple mathematical expression for kindergartners for them to solve"}])
        global question
        question = response1['choices'][0]['message']['content']
        return response1['choices'][0]['message']['content']
    def get_answer():
        response2 = openai.ChatCompletion.create(
            model="gpt-3.5-turbo",
            messages=[{"role": "assistant", "content": "Write me the answer to this question: " + question + " in the form of an integer, no extra characters."}])
        return response2['choices'][0]['message']['content']

    question_text = StringProperty(get_question())
    answer_text = StringProperty(get_answer())

class SiQuest2(MDScreen):
    def get_question():
        return "Which one is an even number?"
    def get_answer():
        return str(6)

    question_text = StringProperty(get_question())
    answer_text = StringProperty(get_answer())

class SiQuest3(MDScreen):
    def get_question():
        return "5, 10, 15, __?"
    def get_answer():
        return str(20)

    question_text = StringProperty(get_question())
    answer_text = StringProperty(get_answer())

class SiQuest4(MDScreen):
    def get_question():
        return "If Amy has 5 apples and she buys 3 from the store. How many apples does she have in total?"
    def get_answer():
        return str(8)

    question_text = StringProperty(get_question())
    answer_text = StringProperty(get_answer())

class SiQuest5(MDScreen):
    def get_question():
        return "6 - 4 = __"
    def get_answer():
        return str(2)

    question_text = StringProperty(get_question())
    answer_text = StringProperty(get_answer())


class SmartPet(MDApp):
    def build(self):
        sm.add_widget(Opening(name='opening'))
        sm.add_widget(GradeLevel(name='gradelevel'))
        sm.add_widget(MinigameTots(name='minigame-tots'))
        sm.add_widget(SubjectOpt(name='subjopt'))
        sm.add_widget(EnglishK(name='englishk'))
        sm.add_widget(Pets(name='pets'))
        sm.add_widget(Tiger(name='tiger'))
        sm.add_widget(Cat(name='cat'))
        sm.add_widget(Panda(name='panda'))
        sm.add_widget(Duck(name='duck'))
        sm.add_widget(SiQuiz(name='siquiz'))
        sm.add_widget(SiQuest1(name='siquest1'))
        sm.add_widget(SiQuest2(name='siquest2'))
        sm.add_widget(SiQuest3(name='siquest3'))
        sm.add_widget(SiQuest4(name='siquest4'))
        sm.add_widget(SiQuest5(name='siquest5'))
        sm.add_widget(Eval(name='eval'))


        sm.current = 'opening'
        return sm
    
#Builder string
kv = Builder.load_string(
"""
<Opening>:
    MDFloatLayout:
        md_bg_color: (198/255, 213/255, 225/255, 1)
        Image:
            source: "rabbit.gif"
            pos_hint: {"center_x": .5, "center_y": .6}
            size_hint: .8, .8
        MDLabel:
            text: "SmartPets Academy"
            pos_hint: {"center_x": 0.6, "center_y": 0.448}
            font_size: "23sp"
            font_name: "LoResReg"
            text_color: (255/255, 255/255, 255/255, 1)
        MDRaisedButton:
            md_bg_color: (93/255, 113/255, 168/255, 1)
            text: '>'
            font_name: "LoResReg"
            font_size: "17sp"
            on_press: root.manager.current = "pets"
            pos_hint: {"center_x": .52, "center_y": 0.26}
            size_hint: .52, .067
<Pets>:
    MDFloatLayout:
        md_bg_color: (198/255, 213/255, 225/255, 1)
        MDLabel:
            text: "Choose your avatar!"
            font_name: "LoResSerifReg"
            font_size: 30
            text_color: (255/255, 255/255, 255/255, 1)
            pos_hint: {"center_x": 0.725, "center_y": 0.9}
        MDRaisedButton:
            md_bg_color: (93/255, 113/255, 168/255, 1)
            pos_hint: {"center_x": .725, "center_y": .3}
            size_hint: .3, .3
            on_press:
                root.manager.current = 'tiger'
            Image:
                source: "tiger.png"
                text_color: (0/255, 0/255, 0/255, 1)
        MDRaisedButton:
            md_bg_color: (93/255, 113/255, 168/255, 1)
            pos_hint: {"center_x": .275, "center_y": .3}
            size_hint: .3, .3
            on_press:
                root.manager.current='cat'
            Image:
                source: "cat.png"
                text_color: (0/255, 0/255, 0/255, 1)
        MDRaisedButton:
            md_bg_color: (93/255, 113/255, 168/255, 1)
            pos_hint: {"center_x": .725, "center_y": .65}
            size_hint: .3, .3
            on_press:
                root.manager.current = 'duck'
            Image:
                source: "duck.png"
                text_color: (0/255, 0/255, 0/255, 1)
        MDRaisedButton:
            md_bg_color: (93/255, 113/255, 168/255, 1)
            pos_hint: {"center_x": .275, "center_y": .65}
            size_hint: .3, .3
            on_press:
                root.manager.current = 'panda'
            Image:
                source: "panda.png"
                text_color: (0/255, 0/255, 0/255, 1)
            
<Tiger>:
    MDFloatLayout:
        md_bg_color: (93/255, 113/255, 168/255, 1)
        Label:
            text: "TADA! You've chosen Rocky."
            pos_hint: {"center_x": 0.5, "center_y": 0.9}
            font_name: "LoResReg"
            font_size: "15sp"
        MDLabel:
            text: "Rocky likes to run around and play with his brothers."
            pos_hint: {"center_x": 0.5, "center_y": 0.8}
            multiline: True
            text_color: (255/255, 255/255, 255/255, 1)
            font_name: "LoResReg"
            font_size: "12sp"
            padding: "40sp"
        Image:
            source: "tiger.png"
            valign: "center"
            halign: "center"
        MDRaisedButton:
            text: 'Next'
            pos_hint: {"center_x": 0.5, "center_y": 0.2}
            on_press:
                root.manager.current = 'gradelevel'
            md_bg_color: (255/255, 255/255, 255/255, 1)
            text_color: (93/255, 113/255, 168/255, 1)
            font_name: 'LoResBold'                       
<Panda>:
    MDFloatLayout:
        md_bg_color: (93/255, 113/255, 168/255, 1)
        Label:
            text: "TADA! You've chosen Blue."
            pos_hint: {"center_x": 0.5, "center_y": 0.9}
            font_name: "LoResReg"
            font_size: "15sp"
        MDLabel:
            text: "Blue likes eating bamboo on tall trees during sunset."
            pos_hint: {"center_x": 0.5, "center_y": 0.8}
            text_color: (255/255, 255/255, 255/255, 1)
            multiline: True
            font_name: "LoResReg"
            font_size: "12sp"
            padding: "40sp"
        Image:
            source: "panda.png"
            valign: "center"
            halign: "center"
        MDRaisedButton:
            text: 'Next'
            pos_hint: {"center_x": 0.5, "center_y": 0.2}
            on_press:
                root.manager.current = 'gradelevel'
            md_bg_color: (255/255, 255/255, 255/255, 1)
            text_color: (93/255, 113/255, 168/255, 1)
            font_name: 'LoResBold'                       
<Cat>:
    MDFloatLayout:
        md_bg_color: (93/255, 113/255, 168/255, 1)
        Label:
            text: "TADA! You've chosen Sam."
            pos_hint: {"center_x": 0.5, "center_y": 0.9}
            font_name: "LoResReg"
            font_size: "15sp"
        MDLabel:
            text: "Sam likes to spend time outdoors and chase squirrels."
            pos_hint: {"center_x": 0.5, "center_y": 0.8}
            multiline: True
            text_color: (255/255, 255/255, 255/255, 1)
            font_name: "LoResReg"
            font_size: "12sp"
            padding: "40sp"
        Image:
            source: "cat.png"
            valign: "center"
            halign: "center"
        MDRaisedButton:
            text: 'Next'
            pos_hint: {"center_x": 0.5, "center_y": 0.2}
            on_press:
                root.manager.current = 'gradelevel'
            md_bg_color: (255/255, 255/255, 255/255, 1)
            text_color: (93/255, 113/255, 168/255, 1)
            font_name: 'LoResBold'                       
<Duck>:
    MDFloatLayout:
        md_bg_color: (93/255, 113/255, 168/255, 1)
        Label:
            text: "TADA! You've chosen Frankie."
            pos_hint: {"center_x": 0.5, "center_y": 0.9}
            font_name: "LoResReg"
            font_size: "15sp"
        MDLabel:
            text: "Frankie likes to swim and jump on lily pads."
            multiline: True
            text_color: (255/255, 255/255, 255/255, 1)
            pos_hint: {"center_x": 0.5, "center_y": 0.8}
            font_name: "LoResReg"
            font_size: "12sp"
            padding: "40sp"
        Image:
            source: "duck.png"
            valign: "center"
            halign: "center"
        MDRaisedButton:
            text: 'Next'
            pos_hint: {"center_x": 0.5, "center_y": 0.2}
            on_press:
                root.manager.current = 'gradelevel'
            md_bg_color: (255/255, 255/255, 255/255, 1)
            text_color: (93/255, 113/255, 168/255, 1)
            font_name: 'LoResBold'                                                                                                                         
<GradeLevel>:
    md_bg_color: (198/255, 213/255, 225/255, 1)
    Label:
        text: 'What grade level are you in?'
        font_size: '32'
        font_name: 'LoResBold'
        valign: "top"
        pos_hint: {"center_x": 0.5, "center_y": 0.9}
    MDRaisedButton:
        text: "Pre-K - Kindergarden"
        font_size: "15sp"
        font_name: "LoResReg"
        size_hint: .2, .15
        pos_hint: {"center_x": 0.5, "center_y": 0.7}
        md_bg_color: (93/255, 113/255, 168/255, 1)
        on_press: root.manager.current = 'siquiz'
    MDRaisedButton:
        text: "1st - 2nd"
        font_size: "15sp"
        font_name: "LoResReg"
        size_hint: .7, .15
        pos_hint: {"center_x": 0.5, "center_y": 0.5}
        md_bg_color: (93/255, 113/255, 168/255, 1)
    MDRaisedButton:
        text: "3rd - 5th"
        font_size: "15sp"
        font_name: "LoResReg"
        size_hint: .7, .15
        pos_hint: {"center_x": 0.5, "center_y": 0.3}
        md_bg_color: (93/255, 113/255, 168/255, 1)
<SiQuiz>:
    MDFloatLayout:
        md_bg_color: (98/255, 113/255, 225/255, 1)
        MDRaisedButton:
            md_bg_color: (93/255, 113/255, 168/255, 1)
            text: 'Test your math skills now!'
            pos_hint: {"center_x": 0.5, "center_y": 0.5}
            size: 0.8, 0.8
            font_name: 'LoResBold'
            on_press: root.manager.current = 'siquest1'
<SiQuest1>:
    MDFloatLayout:
        md_bg_color: (198/255, 213/255, 225/255, 1)
        MDLabel:
            id: question_label
            text: root.question_text
            text_color: (255/255, 255/255, 255/255, 1)
            pos_hint: {"center_x": 0.5, "center_y": 0.85}
            font_name: "LoResBold"
            font_size: "25sp"
        MDRaisedButton:
            id: answer_label
            text: root.answer_text
            on_press: root.manager.current = 'siquest2'
            md_bg_color: (93/255, 113/255, 168/255, 1)
            text_color: (255/255, 255/255, 255/255, 1)
            pos_hint: {"center_x": 0.5, "center_y": 0.3}
            size: 0.9, 0.8
        MDRaisedButton:
            text: '13'
            on_press: root.manager.current = 'siquest2'
            md_bg_color: (93/255, 113/255, 168/255, 1)
            text_color: (255/255, 255/255, 255/255, 1)
            pos_hint: {"center_x": 0.5, "center_y": 0.6}
            size: 0.9, 0.8
        MDRaisedButton:
            text: '11'
            on_press: root.manager.current = 'siquest2'
            md_bg_color: (93/255, 113/255, 168/255, 1)
            text_color: (255/255, 255/255, 255/255, 1)
            pos_hint: {"center_x": 0.5, "center_y": 0.4}
            size: 0.9, 0.8
        MDRaisedButton:
            text: '19'
            on_press: root.manager.current = 'siquest2'
            md_bg_color: (93/255, 113/255, 168/255, 1)
            text_color: (255/255, 255/255, 255/255, 1)
            pos_hint: {"center_x": 0.5, "center_y": 0.5}
            size: 0.9, 0.8
<SiQuest2>:
    MDFloatLayout:
        md_bg_color: (198/255, 213/255, 225/255, 1)
        MDLabel:
            id: question_label
            text: root.question_text
            text_color: (255/255, 255/255, 255/255, 1)
            pos_hint: {"center_x": 0.5, "center_y": 0.85}
            font_name: "LoResBold"
            font_size: "25sp"
        MDRaisedButton:
            id: answer_label
            text: root.answer_text
            md_bg_color: (93/255, 113/255, 168/255, 1)
            text_color: (255/255, 255/255, 255/255, 1)
            on_press: root.manager.current = 'siquest3'
            pos_hint: {"center_x": 0.5, "center_y": 0.3}
            size: 0.9, 0.8
        MDRaisedButton:
            text: '3'
            md_bg_color: (93/255, 113/255, 168/255, 1)
            text_color: (255/255, 255/255, 255/255, 1)
            on_press: root.manager.current = 'siquest3'
            pos_hint: {"center_x": 0.5, "center_y": 0.6}
            size: 0.9, 0.8
        MDRaisedButton:
            text: '11'
            md_bg_color: (93/255, 113/255, 168/255, 1)
            text_color: (255/255, 255/255, 255/255, 1)
            pos_hint: {"center_x": 0.5, "center_y": 0.4}
            on_press: root.manager.current = 'siquest3'
            size: 0.9, 0.8
        MDRaisedButton:
            text: '9'
            md_bg_color: (93/255, 113/255, 168/255, 1)
            on_press: root.manager.current = 'siquest3'
            text_color: (255/255, 255/255, 255/255, 1)
            pos_hint: {"center_x": 0.5, "center_y": 0.5}
            size: 0.9, 0.8
<SiQuest3>:
    MDFloatLayout:
        md_bg_color: (198/255, 213/255, 225/255, 1)
        MDLabel:
            id: question_label
            text: root.question_text
            text_color: (255/255, 255/255, 255/255, 1)
            pos_hint: {"center_x": 0.5, "center_y": 0.85}
            font_name: "LoResBold"
            font_size: "25sp"
        MDRaisedButton:
            id: answer_label
            text: root.answer_text
            md_bg_color: (93/255, 113/255, 168/255, 1)
            on_press: root.manager.current = 'siquest4'
            text_color: (255/255, 255/255, 255/255, 1)
            pos_hint: {"center_x": 0.5, "center_y": 0.3}
            size: 0.9, 0.8
        MDRaisedButton:
            text: '3'
            md_bg_color: (93/255, 113/255, 168/255, 1)
            text_color: (255/255, 255/255, 255/255, 1)
            pos_hint: {"center_x": 0.5, "center_y": 0.6}
            on_press: root.manager.current = 'siquest4'
            size: 0.9, 0.8
        MDRaisedButton:
            text: '11'
            md_bg_color: (93/255, 113/255, 168/255, 1)
            text_color: (255/255, 255/255, 255/255, 1)
            on_press: root.manager.current = 'siquest4'
            pos_hint: {"center_x": 0.5, "center_y": 0.4}
            size: 0.9, 0.8
        MDRaisedButton:
            text: '0'
            md_bg_color: (93/255, 113/255, 168/255, 1)
            text_color: (255/255, 255/255, 255/255, 1)
            pos_hint: {"center_x": 0.5, "center_y": 0.5}
            on_press: root.manager.current = 'siquest4'
            size: 0.9, 0.8
<SiQuest4>:
    MDFloatLayout:
        md_bg_color: (198/255, 213/255, 225/255, 1)
        MDLabel:
            id: question_label
            text: root.question_text
            text_color: (255/255, 255/255, 255/255, 1)
            pos_hint: {"center_x": 0.5, "center_y": 0.85}
            font_name: "LoResBold"
            font_size: "19sp"
        MDRaisedButton:
            text: '7'
            on_press: root.manager.current = 'siquest5'
            md_bg_color: (93/255, 113/255, 168/255, 1)
            text_color: (255/255, 255/255, 255/255, 1)
            pos_hint: {"center_x": 0.5, "center_y": 0.3}
            size: 0.9, 0.8
        MDRaisedButton:
            text: '5'
            md_bg_color: (93/255, 113/255, 168/255, 1)
            text_color: (255/255, 255/255, 255/255, 1)
            pos_hint: {"center_x": 0.5, "center_y": 0.6}
            on_press: root.manager.current = 'siquest5'
            size: 0.9, 0.8
        MDRaisedButton:
            id: answer_label
            text: root.answer_text
            md_bg_color: (93/255, 113/255, 168/255, 1)
            text_color: (255/255, 255/255, 255/255, 1)
            pos_hint: {"center_x": 0.5, "center_y": 0.4}
            on_press: root.manager.current = 'siquest5'
            size: 0.9, 0.8
        MDRaisedButton:
            text: '2'
            md_bg_color: (93/255, 113/255, 168/255, 1)
            text_color: (255/255, 255/255, 255/255, 1)
            pos_hint: {"center_x": 0.5, "center_y": 0.5}
            on_press: root.manager.current = 'siquest5'
            size: 0.9, 0.8
<SiQuest5>:
    MDFloatLayout:
        md_bg_color: (198/255, 213/255, 225/255, 1)
        MDLabel:
            id: question_label
            text: root.question_text
            text_color: (255/255, 255/255, 255/255, 1)
            pos_hint: {"center_x": 0.5, "center_y": 0.85}
            font_name: "LoResBold"
            font_size: "25sp"
        MDRaisedButton:
            text: '8'
            md_bg_color: (93/255, 113/255, 168/255, 1)
            text_color: (255/255, 255/255, 255/255, 1)
            pos_hint: {"center_x": 0.5, "center_y": 0.3}
            size: 0.9, 0.8
        MDRaisedButton:
            text: '10'
            md_bg_color: (93/255, 113/255, 168/255, 1)
            text_color: (255/255, 255/255, 255/255, 1)
            pos_hint: {"center_x": 0.5, "center_y": 0.6}
            size: 0.9, 0.8
        MDRaisedButton:
            id: answer_label
            text: root.answer_text
            on_press: root.current.manager = "eval"
            md_bg_color: (93/255, 113/255, 168/255, 1)
            text_color: (255/255, 255/255, 255/255, 1)
            pos_hint: {"center_x": 0.5, "center_y": 0.4}
            size: 0.9, 0.8
        MDRaisedButton:
            text: '3'
            md_bg_color: (93/255, 113/255, 168/255, 1)
            text_color: (255/255, 255/255, 255/255, 1)
            pos_hint: {"center_x": 0.5, "center_y": 0.5}
            size: 0.9, 0.8
<Eval>:
    MDFloatLayout:
        md_bg_color: (198/255, 213/255, 225/255, 1)
        MDLabel:
            text: "Nice work! You got 4 out of 5 questions correct. Try again next time!"
            pos_hint: {"center_x": 0.5, "center_y": 0.5}
            font_name: "LoResBold"
            font_size: "18sp"
            font_color: (255/255, 255/255, 255/255, 1)
            multiline: True
""")

#Run The Application
if __name__ == '__main__':
    SmartPet().run()