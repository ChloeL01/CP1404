"""
CP1404 - Practicals - Convert miles
"""

from kivy.app import App
from kivy.lang import Builder
from kivy.core.window import Window
from kivy.properties import StringProperty

CONVERSION = 1.60934


class ConvertMilesApp(App):
    """ConvertMilesApp is a Kivy App for converting miles to kms."""
    message = StringProperty()

    def build(self):
        """Build the Kivy window."""
        Window.size = (400, 100)
        self.title = "Convert miles to kilometers"
        self.root = Builder.load_file("convert_miles_km.kv")
        self.message = "Enter miles to be converted to kilometers"
        return self.root

    def convert_miles_to_km(self, value):
        """Convert miles to kilometers."""
        try:
            result = float(value) * CONVERSION
            self.message = str(result)
        except ValueError:
            self.root.ids.user_input.text = str(0.0)
            self.message = str(0.0)

    def handle_increment(self, increment):
        """Add the increment to the current value."""
        try:
            if self.root.ids.user_input.text == "":
                self.root.ids.user_input.text = str(0)
            value = float(self.root.ids.user_input.text) + increment
            self.root.ids.user_input.text = str(value)
        except ValueError:
            pass


ConvertMilesApp().run()
