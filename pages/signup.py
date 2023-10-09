from flet import *
from utils.colors import *
from utils.validation import Validator

class Signup(Container):
    def __init__(self, page: Page):
        super().__init__()
        self.alignment = alignment.center
        self.validator = Validator()
        self.expand = True
        self.bgcolor = blue

        self.error_border = border.all(width=1,color='red')
        self.name_box = Container(
            content= TextField(
                border=InputBorder.NONE,
                content_padding=padding.only(
                    top=0, bottom=0, right=0,left=0
                ), hint_style=TextStyle(
                    size=12, color='#858796'
                ),
                hint_text='Seu nome completo',
                text_style=TextStyle(
                    size=14,
                    color='black'
                ),
            ),
            border=border.all(width=1, color='#bdcbf4'),
            border_radius=30
        )
        self.email_box = Container(
            content= TextField(
                border=InputBorder.NONE,
                content_padding=padding.only(
                    top=0, bottom=0, right=0,left=0
                ), hint_style=TextStyle(
                    size=12, color='#858796'
                ),
                hint_text='Entre com seu email...',
                text_style=TextStyle(
                    size=14,
                    color='black'
                ),
            ),
            border=border.all(width=1, color='#bdcbf4'),
            border_radius=30
        )

        self.password_box = Container(
            content=TextField(
                border=InputBorder.NONE,
                content_padding=padding.only(
                    top=0, bottom=0, right=0, left=0
                ), hint_style=TextStyle(
                    size=12, color='#858796'
                ),
                hint_text='Senha...',
                text_style=TextStyle(
                    size=14,
                    color='black'
                ),
                password=True
            ),
            border=border.all(width=1, color='#bdcbf4'),
            border_radius=30
        )

        Container(
            content=Text(
                value='Login'
            )
        )

        self.content = Column(
            alignment='center',
            horizontal_alignment='center',
            controls=[
                Container(
                    width=500,
                    padding=40,
                    bgcolor='white',
                    content=Column(
                        horizontal_alignment='center',
                        controls=[
                            Text(
                                value="Criar uma conta!",
                                size=16,
                                color='black',
                                text_align='center'
                            ),
                            Container(height=0),
                            self.name_box,
                            self.email_box,
                            self.password_box,
                            Container(height=0),

                            Container(
                                alignment=alignment.center,
                                bgcolor='#4e73df',
                                height=40,
                                border_radius=30,
                                content=Text(
                                    value='Criar a conta'
                                ),
                                on_click=self.signup
                            ),

                            Container(
                                content=Text(
                                    value='Esqueci a senha',
                                    color='#4e73df',
                                    size=12
                                ),
                                on_click=lambda _: self.page.go(
                                    '/forgotpassword'
                                )
                            ),                            Container(
                                content=Text(
                                    value='Já tem a conta? Fazer Login!',
                                    color='#4e73df',
                                    size=12
                                ),
                                on_click=lambda _: self.page.go(
                                    '/login'
                                )
                            ),



                        ]
                    )
                )
            ]
        )

    def signup(self,e):
        if not self.validator.is_correct_name(self.name_box.content.value):
            self.name_box.border = self.error_border
            self.name_box.update()
