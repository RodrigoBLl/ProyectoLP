import flet as ft

def main(page: ft.Page, go_back_func):
    page.title = "Editar Reportes"
    page.bgcolor = "black"
    page.vertical_alignment = ft.MainAxisAlignment.CENTER
    page.horizontal_alignment = ft.CrossAxisAlignment.CENTER
    
    # Función para regresar a oficial.py
    def go_back(e):
        go_back_func()  # Usar la función pasada como argumento
        
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
        on_click=go_back
    )
    
    # Título
    title = ft.Container(
        content=ft.Text("Editar reportes", size=20, weight=ft.FontWeight.BOLD, color="black"),
        bgcolor="white",
        padding=15,
        border_radius=20
    )
    
    # Lista de fechas de reportes
    report_dates = [
        "2024-11-10 14:23:45", "2024-02-05 08:12:30", "2023-12-22 19:45:10", "2023-09-15 22:34:55",
        "2023-07-03 06:20:18", "2023-05-28 12:58:33", "2023-05-13 15:30:22", "2023-04-10 09:42:42"
    ]
    
    # Función para crear cada fila con fecha e ícono de edición
    def create_row(date):
        return ft.Row(
            controls=[
                ft.Text(date, color="black", size=14, expand=1),
                ft.IconButton(ft.icons.EDIT, icon_color="black", bgcolor="white", icon_size=18)
            ],
            alignment=ft.MainAxisAlignment.SPACE_BETWEEN
        )
    
    # Lista de elementos
    report_list = ft.Column(
        controls=[create_row(date) for date in report_dates],
        spacing=5,
        alignment=ft.MainAxisAlignment.CENTER
    )
    
    # Contenedor principal
    main_container = ft.Container(
        content=report_list,
        bgcolor="white",
        padding=20,
        border_radius=10,
        width=500
    )
    
    # Agregar elementos a la página
    page.add(
        ft.Column(
            controls=[back_button, title, main_container],
            spacing=20,
            alignment=ft.MainAxisAlignment.CENTER,
            horizontal_alignment=ft.CrossAxisAlignment.CENTER
        )
    )