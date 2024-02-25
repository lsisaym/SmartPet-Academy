import kivy 
from kivy.app import App
from kivy.lang import Builder
from kivy.uix.widget import Widget
from kivy.uix.boxlayout import BoxLayout 

Builder.load_string(
"""
<MyLayout>:
    BoxLayout:
        orientation: 'vertical'
        size: root.width, root.height

        padding: 50
        spacing: 20

        Image:
            source: "SP-Logo.png"
            size_hint: 1, 1


        Label:
            id: my_label
            text: "Welcome"
            font_size: 58

        Button:
            text: "Press Me!"
            font_size: 32
            size_hint: .75, .75
            pos_hint: {"center_x": 0.5}

"""
)

class MyLayout(Widget):
    pass

class AwesomeApp(App):
    def build(self):
        return MyLayout()
    
if __name__ == "__main__":
    AwesomeApp().run()




def math_add_prob():
        response1 = openai.ChatCompletion.create(
            model="gpt-3.5-turbo",
            messages=[{"role": "assistant", "content": "Write me a creative first grade word problem"}])
        question = response1['choices'][0]['message']['content']

        response2 = openai.ChatCompletion.create(
            model="gpt-3.5-turbo",
            messages=[{"role": "assistant", "content": "Write me the answer to this question: " + question + " in the form of an integer, no extra characters."}])
        answer = response2['choices'][0]['message']['content']

        question_text = StringProperty()
        answer_text = StringProperty()