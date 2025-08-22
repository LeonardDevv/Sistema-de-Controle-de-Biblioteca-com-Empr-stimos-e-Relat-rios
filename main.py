import json
import os

livros = []
usuarios = []

if os.path.exists("livros.json"):
    try:
        with open('livros.json', 'r', encoding='utf8') as f:
            livros = json.load(f)
    except Exception as e:
        print(f"Erro ao carregar dados {e}")


if os.path.exists("usuarios.json"):
    try:
        with open('usuarios.json', 'r', encoding='utf8') as f:
            usuarios = json.load(f)
    except Exception as e:
        print(f"Erro ao carregar dados {e}")

def cadastrar_livro():
    global livros

    if len(livros) == 0:
        id = 1
    else:
        id = max(livro['id'] for livro in livros) + 1 

    titulo_livro = input("Informe o título do livro: ")
    autor_livro = input("Informe o nome do autor do livro: ")
    ano_publi_livro = int(input("Informe o ano de publicação do livro: "))
    quantidade_disp_estoque = int(input("Informe a quantidade disponível em estoque do livro: "))

    livro = {
        "id": id,
        "titulo_livro": titulo_livro,
        "autor_livro": autor_livro,
        "ano_publi_livro": ano_publi_livro,
        "quantidade_disp_estoque": quantidade_disp_estoque
    }

    livros.append(livro)

    try:
        with open('livros.json', 'w', encoding='utf8') as f:
            json.dump(livros, f, ensure_ascii=False, indent=4)
    except Exception as e:
        print("Erro ao salvar os dados: {e}")






def cadastrar_usuario():
    global usuarios

    if len(usuarios) == 0:
        id = 1
    else:
        id = max(usuario['id'] for usuario in usuarios) + 1 

    nome_usuario = input("Informe o nome do usuario: ")
    email_usuario = input("Informe o email do autor do usuario: ")

    usuario = {
        "id": id,
        "nome_usuario": nome_usuario,
        "email_usuario": email_usuario,
    }

    usuarios.append(usuario)

    try:
        with open('usuarios.json', 'w', encoding='utf8') as f:
            json.dump(usuarios, f, ensure_ascii=False, indent=4)
    except Exception as e:
        print("Erro ao salvar os dados: {e}")


def iniciar():
    while True:
        inicio = int(input("Escolha uma opção: \n[ 1 ] - Cadastrar novo livro \n[ 2 ] - Cadastrar usuario\n"))

        if inicio == 1:
            cadastrar_livro()
        elif inicio == 2:
            cadastrar_usuario()

iniciar()