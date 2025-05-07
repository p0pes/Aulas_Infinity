import flet as ft

def main(page: ft.Page) :
    ola = ft.Text(value= "Ola mundo!", size = 30)
    page.controls.append(ola)
    page.update()

ft.app(target=main)

#“Page” (Página):
#Função: Representa a janela
#principal ou a tela do aplicativo
#onde todos os componentes
#(widgets) são adicionados.

#Tipos Comuns de Widgets:
#“Text”: Exibe texto na interface.
#“ElevatedBut ton”: Um botão elevado com ações configuráveis.
#“TextField”: Campo de entrada de texto.