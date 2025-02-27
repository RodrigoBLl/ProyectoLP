import flet as ft

def map_screen(page: ft.Page):
    page.title = "Mapa de Actividades Económicas"
    page.bgcolor = "#181818"
    page.controls.clear()
    
    colonias = [
        ("cat1", "Ignacio Martínez", "blue", ["Asalto a mano armada", "Homicidio", "Robo de vehículo"]),
        ("cat2", "Himno Nacional", "red", ["Asalto a mano armada", "Homicidio", "Robo de vehículo"]),
        ("cat3", "Simón Diaz", "green", ["Asalto a mano armada", "Homicidio", "Robo de vehículo"]),
        ("cat4", "Tierra Blanca", "purple", ["Asalto a mano armada", "Homicidio", "Robo de vehículo"])
    ]

    def actualizar_mapa(event):
        delitos_seleccionados = [cb.label for cb in checkboxes if cb.value]
        mapa.content = ft.Text(
            f"Delitos seleccionados: {', '.join(delitos_seleccionados) if delitos_seleccionados else 'Ninguno'}",
            color="white",
            size=16,
            weight=ft.FontWeight.BOLD
        )
        page.update()

    def cerrar_sesion(event):
        from login import login_screen  
        page.controls.clear()
        login_screen(page)
        page.update()

    checkboxes = []

    sidebar = ft.Container(
        bgcolor="#f4f4f4",
        padding=20,
        width=300,
        height=page.height,  # Fija la altura al tamaño de la página
        content=ft.Column(
            [
                ft.Text("Colonias", size=18, weight=ft.FontWeight.BOLD, color="black"),
                ft.ListView(  # Permite el scroll cuando hay mucho contenido
                    expand=True,
                    controls=[
                        ft.ExpansionTile(
                            title=ft.Text(nombre, color="black", size=14, weight=ft.FontWeight.BOLD),
                            controls=[ 
                                ft.Column(
                                    [
                                        ft.Checkbox(
                                            label=delito,
                                            value=False,
                                            label_style=ft.TextStyle(color="black"),
                                            on_change=actualizar_mapa
                                        )
                                        for delito in delitos
                                    ],
                                    spacing=5
                                )
                            ]
                        )
                        for _, nombre, color, delitos in colonias
                    ],
                ),
                ft.ElevatedButton("Cerrar sesión", on_click=cerrar_sesion, bgcolor="red", color="white")
            ],
            spacing=20
        )
    )

    mapa = ft.Container(
        bgcolor="gray",
        expand=True,
        content=ft.Text("Aquí va el mapa interactivo", color="white", size=16, weight=ft.FontWeight.BOLD),
        alignment=ft.alignment.center
    )

    layout = ft.Row([sidebar, mapa], expand=True)

    page.add(layout)
    page.update()
