# Primeiro Projeto real - Cliente Imobiliaria - Consiste em um sistema que EMITE O RECIBO de forma automática na impressora que tiver conectado no pc.

# instalar bibilioteca PDF para chamar impressora = pip install fpdf2
from fpdf import FPDF
# Instalar biblioteca TK   personalizada = pip install customtkinter
import tkinter as tk
from turtle import title

# Gerenciador de banco de Dados
import sqlite3

# Bibliotecas para manipular dados
import pandas as pd


# #Abrindo a conexao com o banco, senão não salva nada:
conexao = sqlite3.connect('clientes.db')

# # Criando o cursor obrigatorio para haver conexao banco:
c = conexao.cursor()
#######################################################################################################
# TELA LOGIN
import customtkinter as ctk

# Inicializar a aplicação e definir a cor do tema
#ctk.set_appearance_mode("System")  # Modes: "System" (standard), "Dark", "Light"
#ctk.set_default_color_theme("green")  # Themes: "blue" (standard), "green", "dark-blue"   


# Inicializar a aplicação e definir o tema
ctk.set_appearance_mode("System")
ctk.set_default_color_theme("green")

import customtkinter as ctk
# Criar a janela principal
Login = ctk.CTk()
Login.geometry("300x200")
Login.title("Sistema Recibo - V2024")
Login.resizable(False, False)

# Criar os campos de entrada
username_entry = ctk.CTkEntry(master=Login, placeholder_text="Nome de usuário")
password_entry = ctk.CTkEntry(master=Login, placeholder_text="Senha", show="*")

# Criar o botão de login
def login():
    username = username_entry.get()
    password = password_entry.get()

    # Simulação de verificação de credenciais
    if username == "1" and password == "1":
        # Destruir a janela de login
        Login.destroy()

        # Criar uma nova janela (tela principal)
        ########################################################################################################################################
        import customtkinter
        customtkinter.set_appearance_mode("Light")
        customtkinter.set_default_color_theme("dark-blue")

        App = customtkinter.CTk()
        App.title("GERADOR DE RECIBOS IMOBILIARIA - V1_2024")
        App.geometry("400x560")
        App.resizable(False, False)
        App.iconbitmap("icon.ico")

        # Adicionar elementos à nova janela
        
        def gerar_pdf():

            nome_empresa = "IMOBILIARIA LIDER"
            cpf_cnpj = "11574840000184"

            label_nome = "JOAO DA SILVA"
            label_cnpj = "89748239004"

            label_valor = 2350.50
            label_formaPag = "EM DINHEIRO"
            referente = "AO ALUGUEL DO MES VIGENTE"

            texto_recibo = f"Pelo presente recibo, eu {nome_empresa}, inscrito no {cpf_cnpj}, declaro que RECEBI na data de Hoje, o valor de {label_valor}, por meio de pagamento em {label_formaPag}\
    , de {label_nome}, inscrito no cpf {label_cnpj}, referente a {referente}."
            print(texto_recibo)
    
            pdf = FPDF()
            pdf.add_page()
            pdf.image('logo1.png', 90, 8, 33)
            pdf.ln(40)
            pdf.set_font("times", "B", 20)
            pdf.cell(40, 10, "RECIBO")

            pdf.ln(10)

            pdf.multi_cell(200, 10, texto_recibo)
          
    
            pdf.output("impressao_recibo.pdf")

# FUNÇAO PARA CADASTRAR OS DADOS DO RECIBO DOS CLIENTES NO BANCO DE DADOS(FUNCIONANDO(OK)

        def cadastrar_cliente():
            conexao = sqlite3.connect('clientes.db')
            c = conexao.cursor()

    #Inserir dados no Banco de Dados (CLIENTES):
            c.execute("INSERT INTO clientes VALUES (:nome,:cnpj,:valor,:telefone,:formaPag,:dataEmissao,:referente,:observacao)",
              {
                  'nome': entry_nome.get(),
                  'cnpj': entry_cnpj.get(),
                  'valor': entry_valor.get(),
                  'telefone': entry_telefone.get(),
                  'formaPag': entry_formaPag.get(),
                  'dataEmissao': entry_dataEmissao.get(),
                  'referente': entry_referente.get(),
                  'observacao': entry_observacao.get()

              })


    # Commit as mudanças:
            conexao.commit()

    # Fechar o banco de dados:
            conexao.close()

    # # Limpa os valores das caixas de entrada apos cliclar no botão SALVAR Cliente(OK)
            entry_nome.delete(0,"end")
            entry_cnpj.delete(0,"end")
            entry_valor.delete(0,"end")
            entry_telefone.delete(0,"end")
            entry_formaPag.delete(0,"end")
            entry_dataEmissao.delete(0,"end")
            entry_referente.delete(0,"end")
            entry_observacao.delete(0,"end")

# Exportando  dados na tabela(Clientes) para o Excel:
        def exporta_clientes():
            conexao = sqlite3.connect('clientes.db')
            c = conexao.cursor()

            c.execute("SELECT * FROM clientes")
            clientes_cadastrados = c.fetchall()
            print(clientes_cadastrados)
            clientes_cadastrados=pd.DataFrame(clientes_cadastrados, columns=['nome','cnpj','valor','telefone','formaPag','dataEmissao','referente','observacao'])
            clientes_cadastrados.to_excel('Recibos_Clientes.xlsx')

    # Commit as mudanças:
            conexao.commit()

    # Fechar o banco de dados:
            conexao.close()
# Listar em um  GRID, outra Janela os dados dos Recibos dos Clientes(TESTAR PARA APARECER OS DADOS)
        def consulta_clientes():
            janela = tk.Toplevel()
            janela.title("CONSULTA DE RECIBOS CLIENTES - V1_2024")
            janela.geometry("1000x850")
            janela.resizable(False, False)
            janela.iconbitmap("icon.ico")

    
    # DESCRIÇAO DAS GRIDS Entradas - TELA mostrando clientes:
            label_nome = tk.Label(janela, text='NOME CLIENTE DO RECIBO')
            label_nome.grid(row=0,column=1, padx=85, pady=10)

            label_cnpj = tk.Label(janela, text='CNPJ/CPF')
            label_cnpj.grid(row=0,column=2, padx=10, pady=10)

            label_valor = tk.Label(janela, text='VALOR PAGO')
            label_valor.grid(row=0,column=3, padx=10, pady=10)

            label_formaPag = tk.Label(janela, text='FORMA PAGAMENTO')
            label_formaPag.grid(row=0,column=4, padx=10, pady=10)

            label_telefone = tk.Label(janela, text='Telefone')
            label_telefone.grid(row=0,column=5, padx=10, pady=10)

            label_dataEmissao = tk.Label(janela, text='Data')
            label_dataEmissao.grid(row=0,column=6, padx=10, pady=10)

            label_referente = tk.Label(janela, text='Referente')
            label_referente.grid(row=0,column=7, padx=10, pady=10)

            label_observacao = tk.Label(janela, text='Obs')
            label_observacao.grid(row=0,column=8, padx=30, pady=10)

# Mostrar os clientes CADASTRADOS no BANCO DADOS

   # como mostrar dados na tela  
###########################################################################
            conexao = sqlite3.connect('clientes.db')
            c = conexao.cursor()
##########################################################################
    # Inserir dados na tabela:
            c.execute("SELECT * FROM clientes")
            clientes_cadastrados = c.fetchall()
            App(len(consulta_clientes))
            print(clientes_cadastrados)
            clientes_cadastrados=pd.DataFrame(clientes_cadastrados, columns=['nome','cnpj','valor','telefone','formaPag','dataEmissao','referente','observacao'])
            clientes_cadastrados.to_excel('Recibos_Clientes.xlsx')

    # Commit as mudanças:
            conexao.commit()

    # Fechar o banco de dados:
            conexao.close()
###########################################################################

###########################################################################    
# DESCRIÇAO DAS GRIDS Entradas tela PRINCIPAL
        label_nome = tk.Label(App, text='Nome do CLIENTE')
        label_nome.grid(row=1, column=0, padx=10, pady=10)

        label_cnpj = tk.Label(App, text='CPFCNPJ CLIENTE')
        label_cnpj.grid(row=2, column=0, padx=10, pady=10)

        label_valor = tk.Label(App, text='VLR_PAGO')
        label_valor.grid(row=3, column=0, padx=10, pady=10)

        label_telefone = tk.Label(App, text='Telefone')
        label_telefone.grid(row=4, column=0, padx=10, pady=10)

        label_formaPag = tk.Label(App, text='Forma Pagamento')
        label_formaPag.grid(row=5, column=0, padx=10, pady=10)

        # label_dataEmissao = tk.Label(App, text='DATA')
        # label_dataEmissao.grid(row=6, column=0, padx=10, pady=10)

        label_referente = tk.Label(App, text='Referente')
        label_referente.grid(row=7, column=0, padx=10, pady=10)

        label_observacao = tk.Label(App, text='OBS')
        label_observacao.grid(row=8, column=0, padx=10, pady=10)

# CAMPOS PARA PREENCHER Entradas:
        entry_nome = tk.Entry(App , width =35)
        entry_nome.grid(row=1,column=1, padx=10, pady=10)

        entry_cnpj = tk.Entry(App, width =18)
        entry_cnpj.grid(row=2, column=1, padx=10, pady=10)

        entry_valor = tk.Entry(App, width =12)
        entry_valor.grid(row=3, column=1 , padx=10, pady=10)

        entry_telefone = tk.Entry(App, width =35)
        entry_telefone.grid(row=4, column=1, padx=10, pady=10)

        entry_formaPag = tk.Entry(App, width =35)
        entry_formaPag.grid(row=5, column=1, padx=10, pady=10)

        import datetime
        today = datetime.date.today().strftime("%d/%m/%Y")
        entry_dataEmissao = tk.Entry(width =35)
        entry_dataEmissao.insert(0, today)

        # entry_dataEmissao = tk.Entry(App, width =35)
        # entry_dataEmissao.grid(row=6, column=1, padx=10, pady=10)

        entry_referente = tk.Entry(App, width =35)
        entry_referente.grid(row=7, column=1, padx=10, pady=10)

        entry_observacao = tk.Entry(App, width =35)
        entry_observacao.grid(row=8, column=1, padx=10, pady=10)
#############################################################################################
# Botão de Cadastrar OS RECIBOS CLIENTES
        botao_cadastrar = customtkinter.CTkButton(App, text='SALVAR Cliente', command=cadastrar_cliente)
        botao_cadastrar.grid(row=9, column=0, columnspan=2, padx=10, pady=10 , ipadx = 50)

# Botão de GERAR - COMANDO PARA GERAR O RECIBO
        botao_gerar = customtkinter.CTkButton(App, text='IMPRIMIR o RECIBO', command=gerar_pdf)
        botao_gerar.grid(row=10, column=0, columnspan=2, padx=10, pady=10 , ipadx = 50)

# Botão de Exportar - COMANDO PARA EXPORTAR EXCEL

        botao_exportar = tk.Button(text='RELATORIO no Excel', command=exporta_clientes)
        botao_exportar.grid(row=11, column=0, columnspan=2, padx=10, pady=10 , ipadx = 50)

# Botão de CONSULTA - COMANDO PARA VER DADOS NA TELA
        botao_consulta = tk.Button(text='MOSTRAR RECIBOS TELA', command=consulta_clientes)
        botao_consulta.grid(row=12, column=0, columnspan=2, padx=10, pady=10 , ipadx = 50)

        botao_fechar = customtkinter.CTkButton(App, text='FECHAR', command=App.destroy)
        botao_fechar.grid(row=14, column=0, columnspan=2, padx=10, pady=10 , ipadx = 50)



#############################################################################################
# Deixar essa funçao para alguma outra coisa que precisar
#def funcao():
   
        def manual():
            customtkinter.set_appearance_mode("Light")
            customtkinter.set_default_color_theme("dark-blue")
    
            janela1 = tk.Toplevel()
            janela1.geometry("1250x250")
            janela1.title("Recibo Manual - V1_2024")
            janela1.iconbitmap("icon.ico")

            entry_observacao = tk.Entry(janela1, width =150)
            entry_observacao.grid(row=1, column=1, padx=10, pady=10)

            entry_observacao1 = tk.Entry(janela1, width = 150)
            entry_observacao1.grid(row=2, column=1, padx=10, pady=10)
    
            entry_observacao2 = tk.Entry(janela1, width = 150)
            entry_observacao2.grid(row=3, column=1, padx=10, pady=10)

            entry_observacao3 = tk.Entry(janela1, width = 150)
            entry_observacao3.grid(row=4, column=1, padx=10, pady=10)

            label_observacao = tk.Label(janela1, text='DIGITE DADOS RECIBO')
            label_observacao.grid(row=2, column=0, padx=10, pady=10)
###############################################################################
# funçao dentro da ultima janela
            botao_gerar = customtkinter.CTkButton(janela1, text='imprimir', command=gerar_pdf)
            botao_gerar.grid(row=5, column=0,columnspan=2, padx=10, pady=30 , ipadx = 50)

            botao_fechar = customtkinter.CTkButton(janela1, text='FECHAR', command=janela1.destroy)
            botao_fechar.grid(row=5, column=2,columnspan=1, padx=10, pady=10 , ipadx = 5)
   
        botao_alterar = tk.Button(text='RECIBO MANUAL', command=manual)
        botao_alterar.grid(row=13, column=0,columnspan=2, padx=10, pady=10 , ipadx = 50)
        App.mainloop()

########################################################
                    
               
    else:
        label.configure(text="Nome de Usuário ou Senha incorretos!!")

button = ctk.CTkButton(master=Login, text="Login", command=login, fg_color="red")

# Criar um rótulo para exibir mensagens
label = ctk.CTkLabel(master=Login, text="")

# Empacotar os elementos na janela
username_entry.pack(pady=12, padx=10)
password_entry.pack(pady=12, padx=10)
button.pack(pady=12, padx=10)
label.pack(pady=12, padx=10)

Login.mainloop()

