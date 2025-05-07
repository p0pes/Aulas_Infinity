import flet as ft

def main(page: ft.Page):
    page.title = "Tela de cadastro"
    
    layout = ft.Column(
        controls=[ft.TextField(label="Nome", autofocus=True),
        ft.TextField(label="Sobrenome", autofocus=True),
        ft.TextField(label="e-mail", autofocus=True),
        ft.ElevatedButton("Cadastrar")]
    )
 
    page.add(layout)
    page.update()
    
ft.app(target=main)