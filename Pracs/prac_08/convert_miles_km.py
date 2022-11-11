"""
CP1404 - Practicals - Convert miles
"""

from kivy.app import App
from kivy.lang import Builder
from kivy.core.window import Window


class ConvertMilesApp(App):
    """ConvertMilesApp is a Kivy App for converting miles to kms """

    def build(self):
        """Build the Kivy window"""
        Window.size = (400, 100)
        self.title = "Convert miles to kilometers"
        self.root = Builder.load_file("convert_miles_km.kv")
        return self.root


ConvertMilesApp().run()
