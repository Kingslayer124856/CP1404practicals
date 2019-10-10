from kivy.app import App
from kivy.lang import Builder


class BoxLayoutDemo(App):
    def build(self):
        self.title = "Box Layout Demo"
        self.root = Builder.load_file('box_layout_demo.kv')
        return self.root

    def handle_greet(self):
        print("test")
        self.root.ids.output_label.text = "Hello "

    def handle_clear(self):
        """Clears the text box to an empty box"""
        print("Testing")
        self.root.ids.input_name.text = " "


# add a clear button
BoxLayoutDemo().run()
