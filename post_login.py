import flet as ft

def texto(page: ft.Page):
    page.add(
            ft.Text(
                "Hello Another World!",
                size=20,
                weight=ft.FontWeight.BOLD,
                text_align=ft.TextAlign.CENTER
            )
        )
    page.update()