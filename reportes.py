import flet as ft

def main(page: ft.Page, go_back_func):
    page.title = "Alta de Reportes"
    page.bgcolor = "black"
    page.vertical_alignment = ft.MainAxisAlignment.CENTER
    page.horizontal_alignment = ft.CrossAxisAlignment.CENTER

    # Función para regresar a oficial.py
    def go_back(e):
        go_back_func()  # Usar la función pasada como argumento

    # Efecto hover para los botones
    def hover_effect(e):
        e.control.bgcolor = "black" if e.data == "true" else "white"
        e.control.color = "white" if e.data == "true" else "black"
        e.control.border = ft.border.all(2, "white") if e.data == "true" else ft.border.all(2, "black")
        e.control.update()

    # Botón para regresar
    back_button = ft.ElevatedButton(
        "⬅ Regresar",
        bgcolor="white",
        color="black",
        height=40,
        width=150,
        style=ft.ButtonStyle(
            shape=ft.RoundedRectangleBorder(radius=10),
            side={"": ft.BorderSide(color="white", width=2)}
        ),
        on_hover=hover_effect,
        on_click=go_back  # Asignar la función de clic
    )

    # Título
    title = ft.Container(
        content=ft.Text("Alta de reportes", size=20, weight=ft.FontWeight.BOLD, color="black"),
        bgcolor="white",
        padding=15,
        border_radius=20
    )

    # Campos de entrada
    inputs = [
        ft.TextField(label="Tipo de delito", border_color="black", color="black"),
        ft.TextField(label="Ubicación", border_color="black", color="black"),
        ft.TextField(label="Fecha y hora", border_color="black", color="black"),
        ft.TextField(label="Descripción", border_color="black", multiline=True, min_lines=3, color="black")
    ]

    # Botón de subir reporte (centrado)
    submit_button = ft.Row(
        [
            ft.ElevatedButton(
                "Subir reporte",
                bgcolor="white",
                color="black",
                height=40,
                width=150,
                style=ft.ButtonStyle(
                    shape=ft.RoundedRectangleBorder(radius=10),
                    side={"": ft.BorderSide(color="black", width=2)}
                ),
                on_hover=hover_effect
            )
        ],
        alignment=ft.MainAxisAlignment.CENTER  # Centrar el botón
    )

    # Contenedor principal con fondo blanco
    form_container = ft.Container(
        content=ft.Column(
            controls=inputs + [submit_button],  # Agregar el botón centrado
            spacing=15,
            alignment=ft.MainAxisAlignment.CENTER
        ),
        bgcolor="white",
        padding=30,
        border_radius=40,
        width=500
    )

    # Agregar elementos a la página
    page.add(
        ft.Column(
            controls=[back_button, title, form_container],
            spacing=20,
            alignment=ft.MainAxisAlignment.CENTER,
            horizontal_alignment=ft.CrossAxisAlignment.CENTER
        )
    )
