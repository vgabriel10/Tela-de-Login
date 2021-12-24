
from PyQt5 import uic,QtWidgets
import sqlite3


def login():
    nome_usuario = primeiraTela.lineEdit.text()
    senha = primeiraTela.lineEdit_3.text()

    banco = sqlite3.connect("banco_usuarios.db",timeout=10)
    cursor = banco.cursor()
    try:
        cursor.execute(f"SELECT senha FROM usuarios WHERE login = '{nome_usuario}'")
        senhaBd = cursor.fetchall()

        if senha == senhaBd[0][0]:
            primeiraTela.close()
            segundaTela.show()
        else:
            primeiraTela.label_4.setText("Dados de Login Incorretos!")

    except:
        primeiraTela.label_4.setText("Usário Inexistente")


def sair():
    segundaTela.close()
    tela_cadastro.close()
    primeiraTela.show()
    primeiraTela.label_4.setText('')


def telaCadastro():
    primeiraTela.close()
    tela_cadastro.show()
    tela_cadastro.label_2.setText("")
    tela_cadastro.pushButton_2.clicked.connect(sair)
    tela_cadastro.pushButton.clicked.connect(cadastrar)


def cadastrar():
    nome = tela_cadastro.lineEdit.text()
    login = tela_cadastro.lineEdit_3.text()
    senha = tela_cadastro.lineEdit_2.text()

    if nome.strip() and login.strip() and senha.strip() != '':
        try:
            banco = sqlite3.connect("banco_usuarios.db",timeout=10)
            cursor = banco.cursor()
            cursor.execute("INSERT INTO usuarios VALUES ('"+nome+"','"+login+"','"+senha+"')")
            banco.commit()
            banco.close()

        except sqlite3.Error as erro:
            print(f'Erro: {erro}')

        else:
            tela_cadastro.label_2.setText("Usuário Cadastrado com Sucesso!")
    else:
        tela_cadastro.label_2.setText("Dados Inválidos!")


app = QtWidgets.QApplication([])
#Carregando Janelas
primeiraTela = uic.loadUi("primeira_tela.ui")
segundaTela = uic.loadUi("segunda_tela.ui")
tela_cadastro = uic.loadUi("tela_cadastro.ui")

primeiraTela.pushButton.clicked.connect(login)
segundaTela.pushButton.clicked.connect(sair)
primeiraTela.pushButton_2.clicked.connect(telaCadastro)

primeiraTela.lineEdit_3.setEchoMode(QtWidgets.QLineEdit.Password)

primeiraTela.show()
app.exec()
