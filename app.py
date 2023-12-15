import flet as ft
from metodos import register

class MyApp:

    def __init__(self):
        self.register=register()
        pass


    def main(self, page: ft.page):
        page.bgcolor = ft.colors.WHITE
        page.vertical_alignment = "center"
        page.horizontal_alignment = "center"
        page.add(ft.Container(
            ft.Column([
                ft.Container(
                    ft.Text(
                        "Registro Biométrico",
                        width=320,
                        height=30,
                        text_align="center",
                        weight="w900",
                        color=ft.colors.BLACK
                    ),
                    padding=ft.padding.only(10, 10)
                    ),
                ft.Container(
                    ft.TextField(
                        width=280,
                        height=40,
                        hint_text="Ingrese su cédula de ciudadanía",
                        border="underline",
                        prefix_icon=ft.icons.CREDIT_CARD,
                    
                    ),
                    padding=ft.padding.only(10)
                ),
                ft.Container(
                    ft.TextField(
                        width=280,
                        height=40,
                        hint_text="Ingrese su nombre",
                        border="underline",
                        prefix_icon=ft.icons.VERIFIED_USER,
                        color=ft.colors.BLACK
                    ),
                    padding=ft.padding.only(10)
                ),
                ft.Container(
                    ft.TextField(
                        width=280,
                        height=40,
                        hint_text="Ingrese su apellido",
                        border="underline",
                        prefix_icon=ft.icons.VERIFIED_USER,
                        color=ft.colors.BLACK
                    ),
                    padding=ft.padding.only(10)
                ),
                ft.Container(
                    ft.TextField(
                        width=280,
                        height=40,
                        hint_text="Ingrese su género",
                        border="underline",
                        prefix_icon=ft.icons.VERIFIED_USER
                    ),
                    padding=ft.padding.only(10)
                ),
                ft.Container(
                    ft.ElevatedButton(
                        text="inicio biometrico",
                        width=280,
                        bgcolor="black",

                    ),
                    padding=ft.padding.only(10,10)
                ),
                
            ],
            alignment=ft.MainAxisAlignment.CENTER,
            spacing=5  # Ajusta el espaciado entre elementos
            ),
            border_radius=20,
            width=300,
            height=450,  # Ajusta la altura para dejar espacio para el botón
            gradient=ft.LinearGradient([
                ft.colors.GREEN,
                # Agrega aquí los colores adicionales según sea necesario
            ])
            )
        )
    
    def iniciar_biometrico(self, page: ft.page):
        # Obtén la información del usuario desde la interfaz Flet
        document_number = page.get_value_of("Ingrese su cédula de ciudadanía")
        names = page.get_value_of("Ingrese su nombre")
        last_names = page.get_value_of("Ingrese su apellido")
        gender = page.get_value_of("Ingrese su género")

        # Crea una instancia de la clase Register y llama al método create_register_user
        register_instance = register()
        register_instance.regitro_usuarios(document_number, names, last_names, gender)

if __name__ == '__main__':
    app = MyApp()
    app.main(ft.app(target=app.main))