import flet as ft
import oficial
import reportes

def route_change(route, page: ft.Page):
    page.controls.clear()
    if route in oficial.app_routes:
        oficial.app_routes[route](page)
    elif route in reportes.app_routes:
        reportes.app_routes[route](page)
    page.update()

def main(page: ft.Page):
    page.on_route_change = lambda e: route_change(page.route, page)
    page.go("/")  # Empieza en la página principal

ft.app(target=main)
