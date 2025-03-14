import flet as ft
import requests
from post_login import main as post_login_main

import KEY
API_KEY = KEY.key_firebase

def main(page: ft.Page):
    snack_bar = ft.SnackBar(content=ft.Text(""), open=False)

    def btn_login(e):
        try:
            url = f"https://identitytoolkit.googleapis.com/v1/accounts:signInWithPassword?key={API_KEY}"
            payload = {
                "email": textfield_email.value,
                "password": textfield_password.value,
                "returnSecureToken": True
            }
            response = requests.post(url, json=payload)
            response.raise_for_status()
            
            data = response.json()
            if "idToken" in data:
                page.clean()
                post_login_main(page)
                snack_bar.content = ft.Text("Logado com sucesso!", weight=ft.FontWeight.BOLD)
                snack_bar.bgcolor = ft.Colors.GREEN_400
                snack_bar.action = "OK"
                snack_bar.action_color = ft.Colors.BLACK87
                snack_bar.duration = 3000
                snack_bar.open = True
                page.update()
            else:
                raise Exception("Falha na autenticação")

        except Exception as e:
            error_message = "Erro ao fazer login. Verifique suas credenciais."
            if isinstance(e, requests.RequestException) and e.response is not None:
                error_message = e.response.json().get("error", {}).get("message", error_message)
            snack_bar.content = ft.Text("Email ou senha incorreta", weight=ft.FontWeight.BOLD)
            snack_bar.bgcolor = ft.Colors.RED_400
            snack_bar.action = "OK"
            snack_bar.action_color = ft.Colors.BLACK87
            snack_bar.duration = 3000
            snack_bar.open = True
            page.update()
            
            textfield_email.value = ""
            textfield_password.value = ""
            page.update()

    login_text = ft.Text("Login", size=26)
    textfield_email = ft.TextField(label="Email", width=300)
    textfield_password = ft.TextField(label="Password", password=True, width=300)
    confirm_button = ft.ElevatedButton(text="Login", width=100, height=40, on_click=btn_login)

    main_page = ft.Container(
        expand=False,
        content=ft.Column(
            controls=[
                login_text,
                ft.Container(margin=ft.Margin(left=0, top=30, right=0, bottom=0)),  # Corrigido
                textfield_email,
                textfield_password,
                ft.Container(margin=ft.Margin(left=0, top=5, right=0, bottom=0)),   # Corrigido
                confirm_button,
            ],
            alignment=ft.MainAxisAlignment.CENTER,
            horizontal_alignment=ft.CrossAxisAlignment.CENTER,
        ),
        padding=20,
    )
    page.overlay.append(snack_bar)
    page.add(main_page)