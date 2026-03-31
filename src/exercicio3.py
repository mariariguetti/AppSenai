import asyncio
import flet
from flet import ThemeMode, Text, TextField, OutlinedButton, Column, CrossAxisAlignment, Container, Colors, FontWeight, \
    View, AppBar, Icon, Icons, Row


def main(page: flet.Page):
    page.title = "Primeiro APP"
    page.theme_mode = ThemeMode.DARK
    page.window.width = 400
    page.window.height = 700

    def navegar(route):
        asyncio.create_task(
            page.push_route(route)
        )

    def salvar_dados():
        text_nome.value = input_nome.value
        text_tipo.value = input_tipo.value
        text_cor.value = input_cor.value
        text_tamanho.value = input_tamanho.value
        text_bateria.value = input_bateria.value

        tem_erro = False

        if input_nome.value:
            input_nome.error = None
        else:
            tem_erro = True
            input_nome.error = "Campo obrigatório"

        if input_tipo.value:
            input_tipo.error = None
        else:
            tem_erro = True
            input_tipo.error = "Campo obrigatório"

        if input_cor.value:
            input_cor.error = None
        else:
            tem_erro = True
            input_cor.error = "Campo obrigatório"

        if input_tamanho.value:
            input_tamanho.error = None
        else:
            tem_erro = True
            input_tamanho.error = "Campo obrigatório"

        if input_bateria.value:
            input_bateria.error = None
        else:
            tem_erro = True
            input_bateria.error = "Campo obrigatório"

        if not tem_erro:
            input_nome.value = ""
            input_tipo.value = ""
            input_cor.value = ""
            input_tamanho.value = ""
            input_bateria.value = ""
            navegar("/segunda_tela")

            # Gerenciar as telas (routes)

    def route_change():
        page.views.clear()
        page.views.append(
            View(
                route="/",
                controls=[
                    AppBar(
                        title="Drone",
                        bgcolor=Colors.BLUE_900
                    ),
                    Text("Digite o nome do drone:"),
                    input_nome,

                    Text("Digite seu tipo:"),
                    input_tipo,

                    Text("Digite sua cor:"),
                    input_cor,

                    Text("Digite seu tamanho:"),
                    input_tamanho,

                    Text("Digite sua bateria:"),
                    input_bateria,
                    OutlinedButton("Salvar", on_click=salvar_dados)
                ]
            )
        )
        if page.route == "/segunda_tela":
            page.views.append(
                View(
                    route="/segunda_tela",
                    controls=[
                        AppBar(
                            title="Drone",
                            bgcolor=Colors.BLUE_900
                        ),
                        Container(
                            Column([
                                Text(f"{text_nome.value}", weight=FontWeight.BOLD, size=30),

                                Row([
                                    Icon(Icons.AIRPLANEMODE_ON_SHARP, color=Colors.WHITE, size=30),
                                    text_tipo
                                ]),
                                Row([
                                    Icon(Icons.COLOR_LENS, color=Colors.WHITE, size=30),
                                    text_cor
                                ]),
                                Row([
                                    Icon(Icons.CONFIRMATION_NUMBER, color=Colors.WHITE, size=30),
                                    text_tamanho
                                ]),
                                Row([
                                    Icon(Icons.BATTERY_6_BAR_ROUNDED, color=Colors.WHITE, size=30),
                                    text_bateria
                                ]),
                            ],
                                horizontal_alignment=CrossAxisAlignment.CENTER
                            )
                        ),
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

    text = Text()
    input_nome = TextField(label="Nome")
    input_tipo = TextField(label="Tipo")
    input_cor = TextField(label="Cor")
    input_tamanho = TextField(label="Tamanho")
    input_bateria = TextField(label="Bateria")
    text_nome = Text()
    text_tipo = Text()
    text_cor = Text()
    text_tamanho = Text()
    text_bateria = Text()

    # Eventos
    page.on_route_change = route_change
    page.on_view_pop = view_pop

    route_change()


flet.run(main)
