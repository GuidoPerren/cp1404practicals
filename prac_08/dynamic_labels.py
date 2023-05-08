from kivy.app import App
from kivy.lang import Builder
from kivy.uix.button import Label

class DynamicLabels(App):
    def __init__(self,**kwargs):
        super().__init__(**kwargs)
        self.label_list = ["This", "could", "almost", "be", "fun"]

    def build(self):
        self.title = "Dynamic Labels"
        self.root = Builder.load_file('dynamic_labels.kv')
        self.create_labels()
        return self.root

    def create_labels(self):
        for label_text in self.label_list:
            label_to_add = Label(text=label_text)
            self.root.ids.main.add_widget(label_to_add)

DynamicLabels().run()