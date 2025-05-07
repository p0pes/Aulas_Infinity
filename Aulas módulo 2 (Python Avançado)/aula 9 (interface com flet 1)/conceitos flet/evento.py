import flet as ft

def main(page: ft.Page):
    page.title = "Estudando Python"
    page.add(
        ft.Text("Seja bem-vindo"),
        ft.ElevatedButton("Clique aqui", on_click=lambda _: page.add(ft.Text("Botão clicado")))
    )

ft.app(target=main)
