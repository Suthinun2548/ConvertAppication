from kivymd.app import MDApp
from kivymd.uix.screen import MDScreen
from kivy.uix.image import  Image
from kivymd.uix.button import MDFillRoundFlatButton
from kivymd.uix.textfield import MDTextField
from kivymd.uix.label import MDLabel
from kivymd.uix.toolbar import MDTopAppBar
from kivy.lang import Builder
from kivy.core.window import Window

Window.size = (500,300)


class ConvertApp(MDApp):

    def flip(self):
        if self.state == 0:
            self.state = 1
            self.theme_cls.primary_palette = 'DeepOrange'
            self.TopAppBar.title = 'Decimal to Binary'
            self.input.text = '0'
            self.converted.text = ''
            self.label.text = ""
        else:
            self.state = 0
            self.TopAppBar.title = 'Binary to Decimal'
            self.input.text = ''
            self.converted.text = ""
            self.label.text = ""

    def convert(self, args):
        if self.state == 0:
            val = int(self.input.text, 2)
            self.converted.text = str(val)
            self.label.text = 'in Decimal is :'
        else:
            val = bin(int(self.input.text))[2:]
            self.converted.text = val
            self.label.text = 'in Binary is :'

    def build(self):
        self.state = 0
        screen = MDScreen()

        # Header text
        self.TopAppBar = MDTopAppBar(title='Binary to Decimal')
        self.TopAppBar.pos_hint = {'top': 1}
        self.TopAppBar.right_action_items = [["rotate-3d-variant", lambda x: self.flip()]]
        screen.add_widget(self.TopAppBar)

        # Logo
        screen.add_widget(Image(source='logo.png.jpg', pos_hint={'center_x':0.5, 'center_y':0.7}))

        # User input
        self.input = MDTextField(
            text="Input your binary number",
            helper_text_mode = 'persistent',
            halign='center',
            size_hint=(0.8, 1),
            pos_hint={'center_x':0.5, 'center_y':0.25},
            font_size = 22
        )
        screen.add_widget(self.input)

        # Labels
        self.label = MDLabel(
            text="In Decimal is :",
            halign='center',
            pos_hint={'center_x':0.5, 'center_y':0.2},
            theme_text_color='Secondary'
        )
        self.converted = MDLabel(
            text="00000",
            halign='center',
            pos_hint={'center_x': 0.5, 'center_y': 0.1},
            theme_text_color='Primary',
            font_style='H5'
        )

        screen.add_widget(self.label)
        screen.add_widget(self.converted)

        # Convert button
        screen.add_widget(MDFillRoundFlatButton(
            text="CONVERT",
            pos_hint={'center_x': 0.2, 'center_y': 0.5},
            font_size=17,
            on_press=self.convert
        ))

        return screen

ConvertApp().run()
