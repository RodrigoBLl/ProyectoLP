import flet as ft

def main(page: ft.Page):
    page.title = "Gestión de Reportes"
    page.bgcolor = "black"
    page.vertical_alignment = ft.MainAxisAlignment.CENTER
    page.horizontal_alignment = ft.CrossAxisAlignment.CENTER

    # Función para redirigir a reportes.py
    def go_to_reportes(e):
        page.controls.clear()  # Limpiar la página actual
        from reportes import main as reportes_main  # Importar aquí para evitar circularidad
        reportes_main(page, go_to_oficial)  # Pasar la función de regreso
        page.update()

    # Función para regresar a oficial.py
    def go_to_oficial():
        page.controls.clear()
        main(page)  # Recargar la interfaz de oficial.py
        page.update()

    buttons = [
        ("Registrar nuevo delito", go_to_reportes),
        ("Descargar historial de reportes", lambda e: print("Descargar historial")),
        ("Editar reportes", lambda e: print("Editar reportes"))
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