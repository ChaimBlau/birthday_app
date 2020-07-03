from datetime import datetime
from kivy.app import App
from kivy.uix.button import Button
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label
from kivy.clock import Clock

BIRTHDAY = datetime(2020, 7, 23)


class ToBirthday(Label):
    def update(self, dt):
        delta = BIRTHDAY - datetime.now()
        self.text = str(delta).split('.')[0] + '\n To Birthday'


class MainApp(App):
    def build(self):
        self.layout = BoxLayout(padding=30)
        button = Button(text='Try me',
                        size_hint=(.5, .5),
                        pos_hint={'center_x': .5, 'center_y': .5})
        button.bind(on_press=self.on_press_button)
        self.layout.add_widget(button)

        return self.layout

    def on_press_button(self, instance):
        self.layout.clear_widgets()
        to_birthday = ToBirthday()
        Clock.schedule_interval(to_birthday.update, 1)
        self.layout.add_widget(to_birthday)


if __name__ == '__main__':
    app = MainApp()
    app.run()
