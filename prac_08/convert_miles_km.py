from kivy.app import App
from kivy.lang import Builder
from kivy.core.window import Window


class ConvertMilesKm(App):
    def build(self):
        Window.size = (500, 200)
        self.title = "Convert Miles to Kilometers"
        self.root = Builder.load_file('convert_miles_km.kv')
        return self.root

    def handle_add(self, number):
        try:
            current_state = int(self.root.ids.textbox_input_number.text)
            new_state = current_state + int(number)
        except:
            print("invalid number input")

        if new_state >= 0:
            self.root.ids.textbox_input_number.text = str(new_state)
        else:
            print("cant go below 1")

    def update_miles(self):
        try:
            input = float(self.root.ids.textbox_input_number.text)
            output = str(input * 1.609)
            self.root.ids.label_output.text = output
        except:
            print("unable to process input")
            former_input = int(float(self.root.ids.label_output.text) / 1.609)
            self.root.ids.textbox_input_number.text = str(former_input)


ConvertMilesKm().run()
