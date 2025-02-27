import flet as ft
from mapa import map_screen  # Importamos la pantalla del mapa

def login_screen(page: ft.Page):
    page.title = "Login"
    page.bgcolor = "#181818"  # Fondo oscuro
    page.horizontal_alignment = ft.CrossAxisAlignment.CENTER
    page.vertical_alignment = ft.MainAxisAlignment.CENTER
    page.controls.clear()  # Limpia la pantalla
    
    
    def on_login(e):
        map_screen(page)  # Cambia a la pantalla del mapa cuando se presiona el botón
    
    login_container = ft.Container(
        content=ft.Column(
            [
                ft.Text("Bienvenido", size=20, weight=ft.FontWeight.BOLD, color="black"),
                ft.TextField(label="Usuario", border_radius=10, bgcolor="#f0f0f0", color="black"),
                ft.TextField(label="Contraseña", password=True, border_radius=10, bgcolor="#f0f0f0", color="black"),
                
                # Botón con efecto hover
                ft.ElevatedButton(
                    text="Iniciar Sesión",
                    on_click=on_login,
                    style=ft.ButtonStyle(
                        shape=ft.RoundedRectangleBorder(radius=10),
                        bgcolor={"": "white", "hovered": "black"},
                        color={"": "black", "hovered": "white"},
                        padding=15,
                        text_style=ft.TextStyle(size=18, weight=ft.FontWeight.BOLD),
                    ),
                )
            ],
            alignment=ft.MainAxisAlignment.CENTER,
            horizontal_alignment=ft.CrossAxisAlignment.CENTER,
            spacing=15,
        ),
        width=300,
        height=250,
        bgcolor="white",
        border_radius=20,
        shadow=ft.BoxShadow(blur_radius=10, color=ft.colors.BLACK12),
        padding=20,
        alignment=ft.alignment.center,
    )
    
    page.add(login_container)
    page.update()
