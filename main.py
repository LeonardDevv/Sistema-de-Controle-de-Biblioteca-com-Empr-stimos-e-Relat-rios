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
        id = max(livro['livro_id'] for livro in livros) + 1 

    titulo_livro = input("Informe o título do livro: ")
    autor_livro = input("Informe o nome do autor do livro: ")
    ano_publi_livro = int(input("Informe o ano de publicação do livro: "))
    quantidade_disp_estoque = int(input("Informe a quantidade disponível em estoque do livro: "))

    livro = {
        "livro_id": id,
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
        print(f"Erro ao salvar os dados: {e}")


def cadastrar_usuario():
    global usuarios

    if len(usuarios) == 0:
        id = 1
    else:
        id = max(usuario['usuario_id'] for usuario in usuarios) + 1 

    nome_usuario = input("Informe o nome do usuario: ")
    email_usuario = input("Informe o email do autor do usuario: ")

    usuario = {
        "usuario_id": id,
        "nome_usuario": nome_usuario,
        "email_usuario": email_usuario,
        "livros_emprestados": []
    }

    usuarios.append(usuario)

    try:
        with open('usuarios.json', 'w', encoding='utf8') as f:
            json.dump(usuarios, f, ensure_ascii=False, indent=4)
    except Exception as e:
        print(f"Erro ao salvar os dados: {e}")
    

def pegar_livro_emprestado():
    global livros
    global usuarios
    

    
    
def iniciar():
    while True:
        inicio = int(input("\n\nEscolha uma opção: \n[ 1 ] - Cadastrar novo livro \n[ 2 ] - Cadastrar novo usuario\n[ 3 ] - Pegar livro emprestado \n[ 4 ] - Sair do sistema\n"))

        if inicio == 1:
            cadastrar_livro()
        elif inicio == 2:
            cadastrar_usuario()
        elif inicio == 3:
            pegar_livro_emprestado()
        elif inicio == 4:
            print("Sistema encerrado...")
            break
        elif inicio != 1 and inicio != 2 and inicio != 3 and inicio != 4:
            print("Opção inválida, tente novamente.")
    
    
iniciar()
