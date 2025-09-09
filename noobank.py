import flet as ft
from datetime import datetime

class NooBank:
    """
    Classe principal do aplicativo NooBank
    """

    def __init__(self):
        # Inicializa o aplicativo Flet apontando para o método main
        self.app = ft.app(target=self.main)

    def main(self, page: ft.Page):
        """
        Método principal que configura a página inicial do aplicativo
        """
        # Configurações básicas da janela/página
        page.title = "NooBank"
        page.theme_mode = ft.ThemeMode.DARK # Tema escuro
        page.padding = 0 # Remove padding padrão
        page.window_width = 400 # Largura da janela (formato mobile)
        page.window_height = 800 # Altura da janela (formato mobile)
        page.bgcolor = "#8a05be" # Cor de fundo roxa

        # Armazena referência da página para uso em outros métodos
        self.page = page
        # Nome padrão do usuário
        self.user_name = "Cliente"
        # Controla se os valores financeiros estão visíveis ou ocultos
        self.show_values = False

        # Lista de movimentações bancárias fictícias
        # type: 1 = entrada (receita), 0 = saída (despesa)
        self.movements = [
            {"id": 1, "label": "Depósito Bancário", "value": "4.395,90", "date": "03/02/2025",
            "type": 1},
            {"id": 2, "label": "Conta de Luz", "value": "300,90", "date": "09/02/2025", "type":
            0},
            {"id": 3, "label": "Salário", "value": "7.350,00", "date": "05/03/2025", "type": 1},
            {"id": 4, "label": "Supermercado", "value": "2.350,00", "date": "05/04/2025", "type":
            0}
        ]

        # Adiciona a tela de login com primeira tela
        self.page.add(self.build_login_view())

    def handle_name_change(self, e):
        """
        Manipula mudanças no campo de nome do usuário
        """
        # Atualiza o nome do usuário ou mantém "Cliente" se vazio
        self.user_name = e.control.value if e.control.value else "Cliente"

    def toggle_values(self, e):
        """
        Altera entre mostrar e ocultar valores financeiros
        """
        # Inverte o estado de visibilidade
        self.show_values = not self.show_values

        # Atualiza o texto do saldo principal
        self.saldo_text.value = "R$ 9.295,90" if self.show_values else "R$ ****,**"

        # Atualiza o ícone do botão (olho aberto/fechado)
        self.toggle_saldo_btn.icon = ft.Icons.VISIBILITY_OFF if self.show_values else ft.Icons.VISIBILITY

    # Atualiza todos os valores das movimentações
    for item in self.movement_texts:
        item["item"].value = f"R$ {item['date']['value']}" if self.show_values else "R$****,**"

        # Atualiza a interface
        self.page.update()

    def build_login_view(self):
        """
        Constrói a tela de login/boas-vindas
        """
        # Campo de entrada para o nome do usuário
        input_name = ft.TextField(
            border=ft.InputBorder.UNDERLINE, # Borda apenas embaixo
            hint_text="Digite seu nome aqui...",
            on_change=self.handle_name_change, # Chama função quando texto muda
            hint_style=ft.TextStyle(color="#9e9e9e"), # Cor do placeholder
            text_style=ft.TextStyle(color="white"), # Cor do texto digitado
            cursor_color="white", # Cor do cursor
        )

        def handle_login(e):
            """
            Função interna para lidar com o clique no botão entrar
            """
            # Limpa a tela atual e mostra a tela principal
            self.page.controls.clear()
            self.page.add(self.build_login_view())
            self.page.update()

        # Retorna container com layout da tela de login
        return ft.Container(
            bgcolor="#8a05be", # Mesma cor de fundo roxa
            alignment=ft.alignment.top_center, # Alinhamento no topo e centro
            expand=True, # Expande para ocupar espaço disponível
            padding=ft.padding.only(left=16, right=16, top=40), # Espaçamento interno
            content=ft.Column(
                alignment=ft.MaxAxisAlignment.START, # Alinha elementos no início
                controls=[
                    # Título de boas-vindas
                    ft.Text("Bem-vindo(a) ao NooBank!", size=25, weight=ft.FontWeight.NORMAL,
                        color="white"),
                        # Campo de entrada do nome
                        input_name,
                        # Botão para entrar no app
                        ft.ElevatedButton(
                            "ENTRAR"
                            bgcolor="#a126d7", # Cor de fundo roxa mais clara
                            color="white", # Cor do texto
                            on_click=handle_login, # Função chamada no clique
                            style=ft.ButtonStyle(
                                shape=ft.RoundedRectangleBorder(radius=8), # Bordas arredondadas
                            ),
                            width=200,
                            height=50,
                        )
                ]
            )
        )
    
    def build_home_view(self):