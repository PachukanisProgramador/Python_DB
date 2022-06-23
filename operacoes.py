import mysql.connector
import conexaoBD # Classe que faz a conexão com o Banco de Dados

db_connection = conexaoBD.conectar()
con = db_connection.cursor()


def inserir(nome, telefone, endereco, data_nascimento):
    try:
        texto_codigo = f"INSERT INTO pessoa(id, nome, telefone, endereco, dataNascimento) VALUES('','{nome}','{telefone}','{endereco}','{tratar_data(data_nascimento)}')"
        con.execute(texto_codigo)
        db_connection.commit()

        return print(f'{con.rowcount} linha(s) afetada(s).')

    except Exception as error:
        return print(f'Erro no comando inserir.\n{error.msg}')


def cosultar_tudo():
    try:
        texto_codigo = 'SELECT * FROM pessoa'
        con.execute(texto_codigo)

        for(codigo, nome, telefone, endereco, dataNascimento) in con:
            print(f'Código: {codigo}\nNome: {nome}\nTelefone: {telefone}\nEndereço: {endereco}\nData de nascimento: {dataNascimento}\n')

    except Exception as error:
        print(error)


def consultar(id):
    try:
        texto_codigo = f"SELECT * FROM pessoa where id = '{id}'"
        con.execute(texto_codigo)

        for (codigo, nome, telefone, endereco, dataNascimento) in con:
            print(
                f'Código: {codigo}\nNome: {nome}\nTelefone: {telefone}\nEndereço: {endereco}\nData de nascimento: {dataNascimento}\n')

    except Exception as error:
        print(error)


def atualizar(codigo, campo, dado_novo):
    try:
        texto_codigo = f"UPDATE pessoa SET {campo} = '{dado_novo}' WHERE id = '{codigo}'"
        con.execute(texto_codigo)
        db_connection.commit()

        print(f'{con.rowcount} linha(s) afetada(s)')

    except Exception as error:
        print(error)


def excluir_pessoa(codigo):
    try:
        texto_codigo = f"DELETE FROM pessoa WHERE id = '{codigo}'"
        con.execute(texto_codigo)
        db_connection.commit()

        print(f'{con.rowcount} linha(s) afetada(s)')

    except Exception as error:
        print(error)


def tratar_data(texto):
    separado = texto.split('/')
    dia = separado[0]
    mes = separado[1]
    ano = separado[2]

    return f'{ano}-{mes}-{dia}'
