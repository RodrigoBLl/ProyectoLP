import flet as ft

def main(page: ft.Page):
    page.title = "Gestión de Reportes"
    page.bgcolor = "black"
    page.vertical_alignment = ft.MainAxisAlignment.CENTER
    page.horizontal_alignment = ft.CrossAxisAlignment.CENTER

    buttons = [
        "Registrar nuevo delito",
        "Descargar Historial de reportes",
        "Editar reportes"
    ]

    button_widgets = [
        ft.ElevatedButton(
            text,
            height=60,
            width=250,
            style=ft.ButtonStyle(
                bgcolor={"": "white", "hovered": "black"},  # Blanco normal, negro en hover
                color={"": "black", "hovered": "white"},  # Negro normal, blanco en hover
                shape=ft.RoundedRectangleBorder(radius=20),
                side={"": ft.BorderSide(color="black", width=2), 
                      "hovered": ft.BorderSide(color="white", width=2)}  # Borde negro normal, blanco en hover
            )
        )
        for text in buttons
    ]

    container = ft.Row(
        button_widgets,
        alignment=ft.MainAxisAlignment.SPACE_EVENLY
    )

    page.add(container)
    page.update()

ft.app(target=main)
