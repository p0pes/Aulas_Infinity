import flet as ft

def main(page: ft.Page) :
    page.controls.append(ft.Text(value= "Ola mundo!", size = 30))
    page.controls.append(ft.ElevatedButton("Sou um botão!"))
    page.update()

ft.app(target=main)