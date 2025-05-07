import flet as ft

def main(page: ft.Page) :
    page.title = "Minha aplicação Flet"
    
    layout = ft.Column(
        controls = [
            ft.Text("Janela principal!", size=20, weight=ft.FontWeight.BOLD),
            ft.ElevatedButton("Botão 1"),
            ft.ElevatedButton("Botão 2"),
            ft.ElevatedButton("Botão 3"),
        ]
    )
    page.add(layout)
    
ft.app(target=main)