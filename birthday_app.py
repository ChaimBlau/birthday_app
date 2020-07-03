from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.gridlayout import GridLayout
from kivy.uix.button import Button
from kivy.properties import ObjectProperty

RED = [1, 0, 0, 1]
ROOMS = ['ramat gan', 'yeshiva', 'physics', 'family', 'abroad', 'art']

idx = 0


class BarcodeReader(BoxLayout):
    pass


class ScanScreen(GridLayout):
    idx = ObjectProperty(0)

    def __init__(self, **kwargs):
        super(ScanScreen, self).__init__(**kwargs)
        self.ids.reader.ids.zbarcam.bind(symbols=self.verify_code)

    def verify_code(self, instance, symbols):
        if symbols:
            data = symbols[0].data.decode('utf-8')
            if data == ROOMS[self.idx + 1]:
                print('GATE OPENED')
                self.idx += 1
            else:
                print('WRONG DOOR')


class BirthdayApp(App):
    def build(self):
        return ScanScreen()



BirthdayApp().run()
