import flet as ft

def main(page: ft.Page):
    page.title = "Gestión de Reportes"
    page.bgcolor = "black"
    page.vertical_alignment = ft.MainAxisAlignment.CENTER
    page.horizontal_alignment = ft.CrossAxisAlignment.CENTER


    buttons = [
        ("Gestión de usuario", lambda e: print("Gestión de usuario")),
        ("Gestión de reportes", lambda e: print("Gestión de reportes")),
        ("Editar reportes", lambda e: print("Editar reportes"))  # Asignar la función de redirección
    ]

    button_widgets = [
        ft.ElevatedButton(
            text,
            height=60,
            width=250,
            style=ft.ButtonStyle(
                bgcolor={"": "white", "hovered": "black"},
                color={"": "black", "hovered": "white"},
                shape=ft.RoundedRectangleBorder(radius=20),
                side={"": ft.BorderSide(color="black", width=2), 
                      "hovered": ft.BorderSide(color="white", width=2)}
            ),
            on_click=on_click  # Asignar la función de clic
        )
        for text, on_click in buttons
    ]

    container = ft.Row(
        button_widgets,
        alignment=ft.MainAxisAlignment.SPACE_EVENLY
    )

    page.add(container)
    page.update()

ft.app(target=main)