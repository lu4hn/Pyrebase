from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label
from kivy.uix.textinput import TextInput
from kivy.uix.button import Button
from kivy.core.window import Window
from kivy.uix.image import Image
from kivy.uix.screenmanager import ScreenManager, Screen
import requests
import json

class TelaLogin(BoxLayout):
    def __init__(self, **kwargs):
        super(TelaLogin, self).__init__(**kwargs)
        self.orientation = "vertical"
        self.padding = [50, 20]
        self.spacing = 10

        Window.icon = "Firebase.png"
        Window.size = (400, 696)
        Window.clearcolor = (1, 1, 1, 1)

        self.add_widget(Image(source='Firebase.png'))

        self.add_widget(Label(text='L O G I N', color=(0.25, 0.25, 0.25, 1), font_size=30, bold=True))

        self.username_input = TextInput(hint_text='Digite o usuário...', multiline=False, size_hint=(1, None),
                                        size=(400, 50), background_color=(0.15, 0.15, 0.15, 1), foreground_color=(1, 1, 1, 1))
        self.password_input = TextInput(hint_text='Digite a senha...', password=True, multiline=False,
                                        size_hint=(1, None), size=(400, 50), background_color=(0.15, 0.15, 0.15, 1), foreground_color=(1, 1, 1, 1))
        self.add_widget(self.username_input)
        self.add_widget(self.password_input)

        self.buttons_layout = BoxLayout(padding=[0, 10], spacing=5)
        self.login_button = Button(text='Entrar', color=(1, 1, 1, 1), size_hint=(1, None), size=(450, 50),
                                   background_color=(0.30, 0.30, 0.30, 1))
        self.login_button.bind(on_press=self.login)
        self.signup_button = Button(text='Cadastre-se', color=(1, 1, 1, 1), size_hint=(1, None), size=(450, 50),
                                    background_color=(0.30, 0.30, 0.30, 1))
        self.signup_button.bind(on_press=self.ir_para_segunda_tela)
        self.buttons_layout.add_widget(self.login_button)
        self.buttons_layout.add_widget(self.signup_button)
        self.add_widget(self.buttons_layout)

    def ir_para_segunda_tela(self, *kwargs):
        self.parent.parent.current = 'Cadastro'

    def login(self, instance):
        username = self.username_input.text
        password = self.password_input.text
        data = {
            'email': username,
            'senha': password
        }

        link = "https://cadastro-c609a-default-rtdb.firebaseio.com/"
        try:
            requisicao = requests.post(f'{link}/Login/.json', data=json.dumps(data))
            resposta = requisicao.json()

            if requisicao.status_code == 200 and resposta:
                print("Login bem-sucedido!")
                # Aqui você pode definir um estado de usuário logado, por exemplo:
                # self.parent.parent.current = 'Home'
            else:
                print("Falha no login!")
                # Aqui você pode mostrar uma mensagem de erro no aplicativo
                # como um pop-up ou uma label
        except requests.RequestException as e:
            print(f"Erro ao conectar ao servidor: {e}")

class TelaCadastro(BoxLayout):
    def __init__(self, **kwargs):
        super(TelaCadastro, self).__init__(**kwargs)
        self.orientation = "vertical"
        self.padding = [50, 20]
        self.spacing = 10

        Window.clearcolor = (1, 1, 1, 1)

        self.add_widget(Label(text='CADASTRO', color=(0.25, 0.25, 0.25, 1), font_size=30, bold=True))

        self.name_input = TextInput(hint_text='Digite seu nome...', multiline=False, size_hint=(1, None),
                                    size=(400, 50), background_color=(0.15, 0.15, 0.15, 1), foreground_color=(1, 1, 1, 1))
        self.email_input = TextInput(hint_text='Digite seu e-mail...', multiline=False, size_hint=(1, None),
                                     size=(400, 50), background_color=(0.15, 0.15, 0.15, 1), foreground_color=(1, 1, 1, 1))
        self.cellphone_input = TextInput(hint_text='Digite seu telefone...', multiline=False,
                                         size_hint=(1, None), size=(400, 50), background_color=(0.15, 0.15, 0.15, 1), foreground_color=(1, 1, 1, 1))
        self.password_input = TextInput(hint_text='Digite a senha...', password=True, multiline=False,
                                        size_hint=(1, None), size=(400, 50), background_color=(0.15, 0.15, 0.15, 1), foreground_color=(1, 1, 1, 1))
        self.add_widget(self.name_input)
        self.add_widget(self.email_input)
        self.add_widget(self.cellphone_input)
        self.add_widget(self.password_input)

        self.buttons_layout = BoxLayout(padding=[0, 10], spacing=5)
        self.back_button = Button(text='Voltar', color=(1, 1, 1, 1), size_hint=(1, None), size=(450, 50),
                                  background_color=(0.30, 0.30, 0.30, 1))
        self.back_button.bind(on_press=self.ir_para_primeira_tela)
        self.signup_button = Button(text='Cadastrar-se', color=(1, 1, 1, 1), size_hint=(1, None), size=(450, 50),
                                    background_color=(0.30, 0.30, 0.30, 1))
        self.signup_button.bind(on_press=self.cadastro)
        self.buttons_layout.add_widget(self.back_button)
        self.buttons_layout.add_widget(self.signup_button)
        self.add_widget(self.buttons_layout)

    def cadastro(self, instance):
        name = self.name_input.text
        email = self.email_input.text
        cellphone = self.cellphone_input.text
        password = self.password_input.text

        dados = {
            'email': email,
            'nome': name,
            'senha': password,
            'telefone': cellphone
        }

        link = "https://cadastro-c609a-default-rtdb.firebaseio.com/"
        requisicao = requests.post(f'{link}/Cadastro/.json', data=json.dumps(dados))

        if requisicao.status_code == 200:
            print("Dados enviados com sucesso!")
            self.ir_para_primeira_tela()  # Chama o redirecionamento para a tela de login
        else:
            print("Erro ao enviar dados")
            print(requisicao.status_code, requisicao.text)

    def ir_para_primeira_tela(self, *args):
        self.parent.parent.current = 'Login'

class MyApp(App):
    def build(self):
        sm = ScreenManager()
        tela_login = TelaLogin()
        tela_cadastro = TelaCadastro()

        screen_login = Screen(name='Login')
        screen_cadastro = Screen(name='Cadastro')

        screen_login.add_widget(tela_login)
        screen_cadastro.add_widget(tela_cadastro)

        sm.add_widget(screen_login)
        sm.add_widget(screen_cadastro)

        return sm

if __name__ == '__main__':
    MyApp().run()




