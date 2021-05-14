from random import random

from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.properties import ListProperty
from kivy.graphics.vertex_instructions import (Rectangle, Ellipse, Line)
from kivy.graphics.context_instructions import Color


class ScatterTextWidget(BoxLayout):

    text_colour = ListProperty([1, 0, 0, 1])

    def change_label_colour(self, *args):
        colour = [random() for i in range(3)] + [1]
        self.text_colour = colour


class TutorialApp(App):
    def build(self):
        return ScatterTextWidget()


if __name__ == "__main__":
    TutorialApp().run()
