

# may  need to -pip install kivy in your terminal
# command: pip install kivy
from kivy.app import App

import math

# from kivy.uix.gridlayout import GridLayout

from kivy.uix.boxlayout import BoxLayout

from kivy.uix.label import Label

from kivy.uix.textinput import TextInput

from kivy.uix.button import Button


class circle(App):
    def build(self):  # helps build the function itself
        root_widget = BoxLayout(orientation='vertical')

        root_widget.add_widget(Label(text="What is your radius?(Please input a number) "))
        self.radius = TextInput(multiline=True)

        # b1 = Button(text="go", size=(10, 10), pos=(20, 20))

        output_label = Label(size_hint_y=1)

        output_label_2 = Label(size_hint_y=1)

        output_label_3 = Label(size_hint_y=1)

        def evaluate_result(instance):
            x = float(self.radius.text)
            area = x * math.pi * x
            output_label.text = "Area: " + str(area)

        def evaluate_result_2(instance):
            x = float(self.radius.text)
            perimeter = x * math.pi * 2
            output_label_2.text = "Perimeter: " + str(perimeter)

        def evaluate_result_3(instance):
            x = float(self.radius.text)
            Volume = x * x * x * math.pi * (4 / 3)
            output_label_3.text = "Volume: " + str(Volume)
            
        b1 = Button(text="Calculate Area")
        b2 = Button(text="Calcuate perimter")
        b3 = Button(text="Calculate Volume")
        b1.bind(on_press=evaluate_result)
        b2.bind(on_press=evaluate_result_2)
        b3.bind(on_press=evaluate_result_3)

        root_widget.add_widget(self.radius)
        root_widget.add_widget(output_label)
        root_widget.add_widget(output_label_2)
        root_widget.add_widget(output_label_3)
        root_widget.add_widget(b1)
        root_widget.add_widget(b2)
        root_widget.add_widget(b3)

        return root_widget


if "__main__" == __name__:
    circle().run()
