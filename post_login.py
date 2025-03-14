import locale
import flet as ft

locale.setlocale(locale.LC_ALL, 'pt_BR.UTF-8')

def main(page: ft.Page):
    products = ["Zebra", "Água", "Maçã", "Café", "Uva", "Água",
                "Maçã", "Café", "Uva", "Água", "Maçã", "Café",
                "Uva", "Água", "Maçã", "Café", "Uva", "Água",
                "Maçã", "Café", "Uva", "Água", "Maçã", "Café", "Uva"]
    sorted_products = [ft.dropdown.Option(product) for product in sorted(products, key=locale.strxfrm)]
    
    dropdown = ft.DropdownM2(  # Corrigido de DropdownM2 para Dropdown
        label="Produto",
        hint_text="Selecione",
        options=sorted_products,
        value=None,
        width=200,
        border_color=ft.Colors.GREY_400,
    )
    
    txt = ft.Text("Supposedly returned the page", size=20, weight="bold")
    
    def back_home(e):
        page.clean()
        page.add(txt)
        page.update()
        
    btn_return_home = ft.Container(
        content = ft.Icon(
            name=ft.Icons.ARROW_BACK,
        ),
        on_click=back_home
    )

    def selection_confirm(e):
        if dropdown.value:
            print(f"Produto selecionado: {dropdown.value}")
            dropdown.value = None
            page.update()

    btn_confirm = ft.ElevatedButton(
        text="Confirmar",
        on_click=selection_confirm,
    )
    
    page.add(
        ft.Column([
            btn_return_home,
            dropdown,
            btn_confirm
        ])
    )