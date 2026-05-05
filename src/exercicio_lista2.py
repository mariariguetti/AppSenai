import asyncio
from cProfile import label


import flet
from flet import ThemeMode, Text, TextField, OutlinedButton, Column, CrossAxisAlignment, Container, Colors, FontWeight, \
    View, AppBar, FloatingActionButton, Button, ListView, Card, Row, Icon, ListTile, PopupMenuButton, PopupMenuItem, \
    Dropdown, DropdownOption
from flet.controls import page
from flet.controls.border_radius import horizontal
from flet.controls.material.icons import Icons


class Drone:
    def __init__(self, nome, tipo, cor, tamanho, bateria):
        self.nome = nome
        self.tipo = tipo
        self.cor = cor
        self.tamanho = tamanho
        self.bateria = bateria


def main(page: flet.Page):
    page.title = "Exemplo de listas"
    page.theme_mode = ThemeMode.DARK
    page.window.width = 400
    page.window.height = 700

    lista_dados = []

    # Navegar
    def navegar(route):
        asyncio.create_task(
            page.push_route(route)
        )


    def montar_lista_padrao():
        list_view.controls.clear()

        for item in lista_dados:
            list_view.controls.append(
                ListTile(
                    leading=Icon(Icons.CIRCLE),
                    title=item.nome,
                    subtitle=item.tipo,
                    trailing=PopupMenuButton(
                        icon=Icons.MORE_VERT,
                        items=[
                            PopupMenuItem("Ver detalhes", icon=Icons.REMOVE_RED_EYE, on_click=lambda _, drone=item: ver_detalhes(drone)),
                            PopupMenuItem("Excluir", icon=Icons.DELETE, on_click=lambda: excluir(item))
                        ],
                    ),
                ),
            )

    def ver_detalhes(drone):
        text_nome.value = drone.nome
        text_tipo.value = drone.tipo
        text_cor.value = drone.cor
        text_tamanho.value = drone.tipo
        text_bateria.value = drone.tipo

        navegar("/form_detalhes")

    def excluir(item):
        lista_dados.remove(item)
        montar_lista_padrao()

    def salvar_dados():
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
            drone = Drone(
                nome=input_nome.value,
                tipo=input_tipo.value,
                cor=input_cor.value,
                tamanho=input_tamanho.value,
                bateria=input_bateria.value,
            )

            lista_dados.append(drone)

            input_nome.value = ""
            input_tipo.value = ""
            input_cor.value = ""
            input_tamanho.value = ""
            input_bateria.value = ""

        montar_lista_padrao()

    # Gerenciar as telas (routes)
    def route_change():
        page.views.clear()
        page.views.append(
            View(
                route="/lista_padrao",
                controls=[
                    AppBar(
                        title="Drones",
                    ),
                    list_view
                ],
                floating_action_button=FloatingActionButton(
                    icon=Icons.ADD,
                    on_click=lambda: navegar("/form_cadastro"),
                )
            )
        )

        if page.route == "/form_cadastro":
            page.views.append(
                View(
                    route="/form_cadastro",
                    controls=[
                        AppBar(
                            title="Cadastro",
                        ),
                        input_nome,
                        input_tipo,
                        input_cor,
                        input_tamanho,
                        input_bateria,
                        btn_salvar
                    ]
                )
            )

        elif page.route == "/form_detalhes":
            page.views.append(
                View(
                    route="/form_detalhes",
                    controls=[
                        AppBar(
                            title="Detalhes",
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
    input_nome = TextField(label="Nome", hint_text="Digite o nome")
    input_tipo = TextField(label="Tipo", hint_text="EX: Agrário")
    input_cor = Dropdown(
        label="Cor",
        editable=True,
        options=[
            DropdownOption("Preto"),
            DropdownOption("Branco"),
            DropdownOption("Cinza"),
            DropdownOption("Azul"),
            DropdownOption("Verde"),
        ],
        width=400,
    )
    input_tamanho = TextField(label="Tamanho", hint_text="EX: 1000 M")
    input_bateria = TextField(label="Bateria", hint_text="EX: 100%")


    btn_salvar = Button("Salvar", width=400, on_click=lambda: salvar_dados())

    list_view = ListView(height=500)

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