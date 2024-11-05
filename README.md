# Recibo Imobiliaria, usado para gravar em banco de dados mysql as informaçoes do cliente e seu recibo.
Utiliza os seguintes requisitos

1- Gerenciador de banco de Dados = DB Browser for SQLite Version 3.13.1
2- Banco de dados - SQlite
import sqlite3

3- Instalar as Bibliotecas Abaixo:
# instalar bibilioteca PDF para chamar impressora = 
pip install fpdf2
from fpdf import FPDF

# Instalar biblioteca TK personalizada  Customtkinter = 
pip install customtkinter
import customtkinter as ctk
import tkinter as tk

# Bibliotecas para manipular Dados e Planilhas
import pandas as pd

# Importar Biblioteca para data e hora
import datetime

4- Utilizei o auto-py-to-exe para tornar o codigo executável
pip install auto-p

5- Tema e cores usados do Customtkinter
customtkinter.set_appearance_mode("Light")
customtkinter.set_default_color_theme("dark-blue")
