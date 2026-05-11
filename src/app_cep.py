import asyncio
from cProfile import label

import flet
from flet import ThemeMode, View, Colors, ListView, Icons, ListTile, Image, Column, Text, \
    Pagelet, NavigationBar, NavigationBarDestination, ScrollMode, FontWeight, TextOverflow, Container, Row, \
    CrossAxisAlignment, Alignment, Button, OutlinedButton, control, TextField
from flet.controls import page
from flet.controls.core import list_view, pagelet

from src.app_endpoints_cep import get_cep





def main(page: flet.Page):
    # Configurações
    page.title = "CEP API"
    page.theme_mode = ThemeMode.LIGHT  # ou ThemeMode.Light
    page.window.width = 400
    page.window.height = 700

    # Funções
    # Navegar
    def navegar(route):
        asyncio.create_task(
            page.push_route(route)
        )

    def cadastrar_cep():
        cep = input_cep.value
        num_c1 = input_nc.value

        tem_erro = False
        if cep:
            input_cep.error = None
        else:
            tem_erro = True
            input_cep.error = "Campo obrigatório"

        if not tem_erro:
            end1 = get_cep(cep)
            text_localidade.value = end1["localidade"]
            text_uf.value = end1["uf"]
            text_logra.value = end1["logradouro"]
            text_bairro.value = end1["bairro"]



    def route_change():
        page.views.clear()
        page.views.append(
            View(
                route="/",
                controls=[
                    flet.AppBar(
                        title="CEP",
                        bgcolor=Colors.PINK_600,
                    ),
                    input_cep,
                    input_nc,
                    text_localidade,
                    text_uf,
                    text_logra,
                    text_bairro,
                    btn_salvar,

                ]
            )
        )


#COMPONENTES

    input_cep = TextField(label="Digite o CEP", on_submit=lambda: cadastrar_cep())
    input_nc = TextField(label="Digite o número da casa")
    btn_salvar = Button("Buscar", width=400, bgcolor=Colors.WHITE_70, on_click=lambda: cadastrar_cep())
    text_localidade = TextField(label="Cidade", read_only=True, bgcolor=Colors.PINK_100)
    text_uf = TextField(label="UF", read_only=True, bgcolor=Colors.PINK_100)
    text_logra = TextField(label="Logradouro", read_only=True, bgcolor=Colors.PINK_100)
    text_bairro = TextField(label="Bairro", read_only=True, bgcolor=Colors.PINK_100)


    route_change()
flet.run(main)
