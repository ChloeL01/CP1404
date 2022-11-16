"""Cp1404 Kivy Demo"""
from kivy.app import App
from kivy.lang import Builder


class BoxLayoutDemo(App):
    """Box Layout Demo"""

    def build(self):
        """Build the kivy app from for the program"""
        self.title = "Box Layout Demo"
        self.root = Builder.load_file('box_layout.kv')
        return self.root

    def handle_greet(self):
        """Handle the greet message"""
        # print("test")
        self.root.ids.output_label.text = f"Hello {self.root.ids.input_name.text}"

    def handle_reset(self):
        """Handle the rest button"""
        self.root.ids.output_label.text = "Enter your name"
        self.root.ids.input_name.text = ""


BoxLayoutDemo().run()
