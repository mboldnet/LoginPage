"""
    Functions and definitions used in loginpage.py
    MNegreiros - 20240412
"""

import io
import sys
import os
import base64
import cryptography
from cryptography.fernet import Fernet
from cryptography.hazmat.primitives import hashes
from cryptography.hazmat.primitives.kdf.pbkdf2 import PBKDF2HMAC

import flet as ft


def getStyle(ctrl: str):
    """
    Returns a default style for the type of control passed ("button","Text",etc)
    MNegreiros - 20231228
    """

    mystyle = ""

    match ctrl.lower:

        case "button":

            mystyle = (
                ft.ButtonStyle(
                    shape=ft.RoundedRectangleBorder(radius=10),
                    bgcolor=ft.colors.CYAN,
                    color=ft.colors.BLACK,
                    side=ft.BorderSide(width=1),
                    shadow_color=ft.colors.ORANGE,
                ),
            )
    return mystyle
