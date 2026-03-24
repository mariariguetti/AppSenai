from datetime import datetime

import flet
from flet import ThemeMode, Text, TextField, OutlinedButton, Column, CrossAxisAlignment
from flet.controls import page
from flet.controls.border_radius import horizontal


def main(page: flet.Page):
    # Configurações
    page.title = "Primeiro APP"
    page.theme_mode = ThemeMode.DARK
    page.window.width = 400
    page.window.height = 700

    # Funções

    def salvar_nome(nome):
        text.value = f"Bom dia {input_nome.value} {input_sobrenome.value}"
        page.update()

    def par_impar():
        if int(input_par_impar.value) % 2 == 0:
            numero.value = f'O número {input_par_impar.value} é par!'
        else:
            numero.value = f'O número {input_par_impar.value} é ímpar!'
        page.update()

    def data_nascimento(data_atual):
        data_convertida = datetime.strptime(input_data.value, '%d/%m/%Y').date()
        idade_da_pessoa = datetime.now().year - data_convertida.year
        if data_convertida.month > datetime.now().month:
            idade_da_pessoa -= 1
        if idade_da_pessoa < 18:
            data.value = f'A sua idade é: {idade_da_pessoa}, você é menor de idade'
        else:
            data.value = f'A sua idade é: {idade_da_pessoa}, você é maior de idade'


    # Componentes
    text = Text()
    input_nome = TextField(label="Nome")
    input_sobrenome = TextField(label="Sobrenome")
    btn_salvar = OutlinedButton("Salvar", on_click=salvar_nome)

    text_numero = Text()
    input_par_impar = TextField(label="Par ou Ímpar")
    btn_verificar = OutlinedButton("Verificar", on_click=par_impar)

    text_data = Text()
    input_data = TextField(label="Data de Nascimento")
    btn_data = OutlinedButton("Verificar", on_click=data_nascimento)


# Construções da tela
    page.add(
        Column(
            [
                input_nome,
                input_sobrenome,
                btn_salvar,
                text,
                input_par_impar,
                btn_verificar,
                text_numero,
                input_data,
                btn_data,
                text_data
            ],
            width=400,
            horizontal_alignment=CrossAxisAlignment.CENTER
        )
    )

flet.app(main)
