import flet as ft
from login import login_screen  

def main(page: ft.Page):
    login_screen(page) 

ft.app(target=main)
