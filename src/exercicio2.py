import asyncio
import flet
from flet import ThemeMode, Text, TextField, OutlinedButton, Column, CrossAxisAlignment, Container, Colors, FontWeight, \
    View, AppBar


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

    def salvar_funcionario():
        text_nome.value = input_nome.value
        text_cpf.value = input_cpf.value
        text_email.value = input_email.value
        text_salario.value = input_salario.value

        tem_erro = False

        if input_nome.value:
            input_nome.error = None
        else:
            tem_erro = True
            input_nome.error = "Campo obrigatório"

        if input_cpf.value:
            input_cpf.error = None
        else:
            tem_erro = True
            input_cpf.error = "Campo obrigatório"

        if input_email.value:
            input_email.error = None
        else:
            tem_erro = True
            input_email.error = "Campo obrigatório"

        if input_salario.value:
            input_salario.error = None
        else:
            tem_erro = True
            input_salario.error = "Campo obrigatório"

        if not tem_erro:
            input_nome.value = ""
            input_cpf.value = ""
            input_email.value = ""
            input_salario.value = ""
            navegar("/segunda_tela")

    # Gerenciar as telas (routes)
    def route_change():
        page.views.clear()
        page.views.append(
            View(
                route="/",
                controls=[
                    AppBar(
                        title="Funcionário",
                        bgcolor=Colors.BLUE_900
                    ),
                    Text("Digite seu nome:"),
                    input_nome,

                    Text("Digite seu CPF:"),
                    input_cpf,

                    Text("Digite seu Email:"),
                    input_email,

                    Text("Digite seu salário:"),
                    input_salario,
                    OutlinedButton("Salvar", on_click=salvar_funcionario)
                ]
            )
        )
        if page.route == "/segunda_tela":
            page.views.append(
                View(
                    route="/segunda_tela",
                    controls=[
                        AppBar(
                            title="Funcionários",
                            bgcolor=Colors.BLUE_900
                        ),
                        text_nome,
                        text_cpf,
                        text_email,
                        text_salario,
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
    input_cpf = TextField(label="CPF")
    input_email = TextField(label="Email")
    input_salario = TextField(label="Salario")
    text_nome = Text()
    text_cpf = Text()
    text_email = Text()
    text_salario = Text()

    # Eventos
    page.on_route_change = route_change
    page.on_view_pop = view_pop

    route_change()


flet.run(main)
