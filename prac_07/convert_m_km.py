from kivy.app import App
from kivy.lang import Builder
from kivy.core.window import Window

MILES_TO_KM = 1.60934


class MilesConverterApp(App):
    def build(self):
        Window.size = (600, 300)
        self.title = "Convert Miles to Kilometers"
        self.root = Builder.load_file('convert_m_km.kv')
        return self.root

    def calculate(self):
        """Calculates miles to kilometers"""
        value = self.get_valid_miles()
        result = value * MILES_TO_KM
        self.root.ids.kilometres.text = str(result)

    def increment(self, change):
        value = self.get_valid_miles() + change
        self.root.ids.miles.text = str(value)
        self.calculate()

    def get_valid_miles(self):
        try:
            value = float(self.root.ids.miles.text)
            return value
        except ValueError:
            return 0


MilesConverterApp().run()
