"""
Após instalar o Selenium com:
- pip install selenium

Acessar a pagina do selenium em https://pypi.org/project/selenium/ para baixar
os drivers do navegador que será utilizado. Tem uma seção especifica com os
drivers dos navegadores suportados. (é importante baixar o driver especifico
para a versão do navegador utilizado)

Nos testes foi utilizado o Google Chrome V88.0.4324
"""
from selenium import webdriver
from time import sleep


class ChromeAuto:
    def __init__(self):
        self.driver_path = 'chromedriver.exe'   # Caminho do driver
        # Definindo o diretório/perfil onde o cache fica salvo. (opcional)
        self.options = webdriver.ChromeOptions()
        self.options.add_argument('user-data-dir=perfil')
        self.chrome = webdriver.Chrome(
            self.driver_path,
            options=self.options
        )

    def clica_sign_in(self):
        try:
            # Procurando por um elemento que contenha o texto "Sign in" na home do github
            btn_sign_in = self.chrome.find_element_by_link_text('Sign in')
            btn_sign_in.click()   # Clicando no elemento que contem o texto Sign in
        except Exception as e:
            print('Erro ao clicar em Sign in:', e)

    def faz_login(self):
        try:
            # o id pode ser encontrado ao inspecionar o elemento da pagina
            input_login = self.chrome.find_element_by_id('login_field')
            input_password = self.chrome.find_element_by_id('password')

            # Insere o conteúdo informado no parâmetro no campo de login
            input_login.send_keys('User')   # Inserir o usuário
            input_password.send_keys('Password')   # Inserir a senha
            sleep(0.5)   # Pausa pra visualização
            # Clicando no botão de login (nome dele no fonte é commit)
            btn_login = self.chrome.find_element_by_name('commit')
            btn_login.click()
        except Exception as e:
            print('Erro ao fazer login:', e)

    def clica_perfil(self):
        try:
            # Pegando o botão através do seletor css (Inspecionar elemento no
            # css + botão direito no cod. > Copy > Copy Selector )
            btn_perfil = self.chrome.find_element_by_css_selector(
                'body > div.position-relative.js-header-wrapper > header> '
                'div.Header-item.position-relative.mr-0.d-none.d-md-flex > details'
            )
            # Clicando no botão
            btn_perfil.click()
        except Exception as e:
            print('Erro ao clicar no perfil:', e)

    def faz_logout(self):
        sleep(0.5)   # Pausando o código por 1seg pra garantir que o menu já tenha sido aberto
        try:
            btn_logout = self.chrome.find_element_by_css_selector(
                'body > div.position-relative.js-header-wrapper > header > '
                'div.Header-item.position-relative.mr-0.d-none.d-md-flex > '
                'details > details-menu > form > button')
            # Clicando no botão
            btn_logout.click()
        except Exception as e:
            print('Erro ao fazer logout:', e)

    def verifica_usuario(self, usuario):
        """
        Verificando se o nome de usuário informado por parâmetro é o mesmo da
        pagina, caso não seja, levanta exceção.

        :param usuario: usuário do github
        """
        sleep(0.5)
        profile_link = self.chrome.find_element_by_class_name('user-profile-link')
        profile_link_html = profile_link.get_attribute('innerHTML')

        # Verificando se o nome de usuário consta no html, caso não exista
        # levanta exceção
        assert usuario in profile_link_html

    def acessa(self, site):
        self.chrome.get(site)

    def sair(self):
        self.chrome.quit()


if __name__ == '__main__':
    chrome = ChromeAuto()
    chrome.acessa('https://github.com/')

    chrome.clica_perfil()
    chrome.faz_logout()

    chrome.clica_sign_in()
    chrome.faz_login()

    chrome.clica_perfil()
    chrome.verifica_usuario('GitHub User Here')

    sleep(0.5)
    chrome.sair()
