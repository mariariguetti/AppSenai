import asyncio

import flet
from flet import ThemeMode, Text, TextField, OutlinedButton, Column, CrossAxisAlignment, Container, Colors, FontWeight, \
    View, AppBar
from flet.controls import page
from flet.controls.border_radius import horizontal


def main(page: flet.Page):

    page.title = "Primeiro APP"
    page.theme_mode = ThemeMode.DARK
    page.window.width = 400
    page.window.height = 700

    # Navegar
    def navegar(route):
        asyncio.create_task(
            page.push_route(route)
        )


    # Gerenciar as telas (routes)
    def route_change():
        page.views.clear()
        page.views.append(
            View(
                route="/",
                controls=[
                    AppBar(
                        title="Primeira página",
                        bgcolor=Colors.BLUE_900
                    ),
                    OutlinedButton("Ir para segunda tela", on_click=lambda: navegar("/segunda_tela"))
                ]
            )
        )
        if page.route == "/segunda_tela":
            page.views.append(
                View(
                    route="/segunda_tela",
                    controls=[
                        AppBar(
                            title="Segunda página",
                        )
                    ]
                )
            )


    # Voltar
    async def view_pop(e):
        if e.view is not None:
            page.views.remove(e.view)
            top_view = page.views[-1]
            await page.push_route(top_view.route)

    # Componentes


    # Eventos
    page.on_route_change = route_change
    page.on_view_pop= view_pop

    route_change()

flet.run(main)



