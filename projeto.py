def cadastrar(usuarios) -> None:
    qtn_usuario = int(input('Quantidade: '))
    for i in range(qtn_usuario):
      usur = input('Usuario: ')
      paswd = input('Senha: ')
      usuarios.append(usur)
      senhas.append(paswd)

def login(usuarios, senhas) -> None:
    login = input('Usuario: ')
    senha = input('Senha: ')
    if login in usuarios:
        i = usuarios.index(login)
        if senha == senhas[i]:
            print('entrou')
        else:
            print('usuario ou senha errado')
    else:
        print('usuario ou senha errado')

def listar(usuarios) -> None:
    if usuarios != []:
        print('-'*20)
        for i in usuarios:
            print(i)
    else:
        print('Nenhum usuario cadastrado')

usuarios = []
senhas = []

while True:
  e = input('''
Ben vindo ao carona unimar!
[1] cadastrar usuario
[2] entrar
[3] listar
[0] sair

opção: ''')
  if e == '1':
    cadastrar(usuarios)
  elif e == '2':
    login(usuarios, senhas)
  elif e == '3':
    listar(usuarios)
  elif e == '0':
    break