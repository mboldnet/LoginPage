"""

"""

from lib.mylib import *


_Token: bytearray = "mb".encode()


def email_clicked(e): ...


def pwd_clicked(e): ...


_Email: ft.TextField = ft.TextField(
    value="",
    text_size=12,
    icon=ft.icons.EMAIL,
    label="Your best email",
    border_radius=10,
    border_color=ft.colors.WHITE,
    border_width=1,
    on_submit=email_clicked,
)
_Password: ft.TextField = ft.TextField(
    value="",
    password=True,
    can_reveal_password=True,
    icon=ft.icons.PASSWORD,
    label="Your Password",
    tooltip="Pwd > 10 , UpperCase, LowerCase, Spec. char >= 1",
    text_size=12,
    border_color=ft.colors.WHITE,
    border_width=1,
    # color=ft.colors.WHITE,
    border_radius=10,
    on_submit=pwd_clicked,
)


"""
"""


def btn_submit_click(e): ...


def btn_cancel_click(e): ...


# Row with 2 buttons
submit = ft.Container(
    alignment=ft.alignment.center,
    padding=20,
    # bgcolor=ft.colors.YELLOW_300,
    # height=400,
    content=ft.Row(
        width=430,
        # expand=True,
        spacing=10,
        alignment=ft.MainAxisAlignment.CENTER,
        vertical_alignment=ft.CrossAxisAlignment.CENTER,
        controls=[
            ft.Text(width=10),
            ft.ElevatedButton(
                text="Cancel",
                icon=ft.icons.CANCEL,
                # icon_color=ft.colors.BLACK,
                on_click=btn_cancel_click,
            ),
            ft.Text(width=85),
            ft.ElevatedButton(
                text="Submit",
                icon=ft.icons.LOGIN,
                on_click=btn_submit_click,
            ),
        ],
    ),
)


def main(page: ft.Page):

    page.title = " Python login Page with flet"
    page.theme_mode = ft.ThemeMode.DARK

    layout = ft.Container(
        padding=20,
        width=450,
        alignment=ft.alignment.center,
        border=ft.border.all(width=2, color=ft.colors.CYAN),
        border_radius=20,
        content=ft.Column(
            horizontal_alignment=ft.CrossAxisAlignment.CENTER,
            alignment=ft.MainAxisAlignment.CENTER,
            controls=[
                ft.Text(
                    # width=410,
                    expand=True,
                    value="Login/Subscribe",
                    size=14,
                    color=ft.colors.WHITE,
                    text_align=ft.alignment.center,
                    # bgcolor=ft.colors.YELLOW_300,
                ),
                _Email,
                _Password,
                submit,
            ],
        ),
    )

    page.add(layout)


if __name__ == "__main__":
    ft.app(target=main, assets_dir="assets", port=7777, view=ft.AppView.FLET_APP_WEB)
