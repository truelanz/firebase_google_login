import flet as ft
from login_page import main as login_main

def main(page: ft.Page):
    page.vertical_alignment = ft.MainAxisAlignment.CENTER
    page.horizontal_alignment = ft.CrossAxisAlignment.CENTER
    page.window.max_height = 480
    page.window.max_width = 480
    page.window.min_height = 480
    page.window.min_width = 480
    
    login_main(page)  # Inicia com a página de login
    page.update()

ft.app(target=main)