from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button
from kivy.uix.label import Label
from kivy.clock import Clock
from kivy.utils import platform

if platform == 'android':
    from jnius import autoclass
    PythonActivity = autoclass('org.kivy.android.PythonActivity')
    TextToSpeech = autoclass('android.speech.tts.TextToSpeech')
    Locale = autoclass('java.util.Locale')


class JarvisApp(App):
    tts = None

    def build(self):
        self.title = 'J.A.R.V.I.S.'
        root = BoxLayout(orientation='vertical', padding=20, spacing=15)

        root.add_widget(Label(
            text='J.A.R.V.I.S.',
            font_size='32sp',
            color=(0.5, 0.87, 1, 1),
            size_hint=(1, 0.3)
        ))

        self.log = Label(
            text='Система запущена',
            font_size='16sp',
            color=(0.7, 0.9, 1, 1),
            size_hint=(1, 0.4),
            halign='center',
            valign='middle'
        )
        self.log.bind(size=self.log.setter('text_size'))
        root.add_widget(self.log)

        btn = Button(
            text='ГОВОРИТЬ',
            font_size='20sp',
            size_hint=(1, 0.2),
            background_color=(0.12, 0.56, 1, 1)
        )
        btn.bind(on_release=self.say_hello)
        root.add_widget(btn)

        Clock.schedule_once(self.init_tts, 1)
        return root

    def init_tts(self, dt):
        if platform != 'android':
            self.log.text = 'Режим ПК (TTS недоступен)'
            return
        try:
            activity = PythonActivity.mActivity
            self.tts = TextToSpeech(activity, None)
            self.tts.setLanguage(Locale('ru', 'RU'))
            self.say('Джарвис к вашим услугам')
        except Exception as e:
            self.log.text = f'TTS ошибка: {e}'

    def say(self, text):
        self.log.text = f'🤖 {text}'
        if self.tts and platform == 'android':
            self.tts.speak(text, TextToSpeech.QUEUE_FLUSH, None, 'id1')

    def say_hello(self, *args):
        self.say('Приветствую, сэр')


if __name__ == '__main__':
    JarvisApp().run()
