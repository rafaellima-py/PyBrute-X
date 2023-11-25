import itertools


nome =  'Rafael'#input("Digite o nome: ").lower()
sobrenome = 'Lima'#input("Digite o sobrenome: ").lower()
apelido = 'bi'#input("Digite o apelido: ").lower()
nome_mae = 'valeria' #input("Digite o nome da mãe: ").lower()
nome_pai = 'jorge'#input("Digite o nome do pai: ").lower()
nome_pet = 'frederico'#input("Digite o nome do pet: ").lower()
data_nascimento ='12072000' #input("Digite a data de nascimento (DDMMYYYY): ")
ano_nascimento = '2000'#input("Digite o ano de nascimento: ")
nome_minusculo = nome.lower()
nome_maiusculo = nome.upper()
nome_capitalizado = nome.capitalize()
sobrenome_minusculo = sobrenome.lower()
sobrenome_maiusculo = sobrenome.upper()
sobrenome_capitalizado = sobrenome.capitalize()

    

  # Gera padrões de senhas combinando as informações fornecidas
padroes_senha = [
        [nome + sobrenome],
        [nome + ano_nascimento],
        [nome_pet],
        [apelido,],
        [apelido + ano_nascimento],
        [nome_minusculo + sobrenome_minusculo],
        [nome_maiusculo + sobrenome_maiusculo],
        [nome_capitalizado + sobrenome_capitalizado],
        [nome_minusculo + sobrenome_capitalizado],
        [nome_maiusculo + sobrenome_minusculo],
        [nome_capitalizado + sobrenome_maiusculo],
        [nome_capitalizado + ano_nascimento],
        [nome_minusculo + ano_nascimento],
        [nome_maiusculo + ano_nascimento],
        [nome_capitalizado + nome_pet],
        [nome_mae + nome],
        [nome_pai + nome],
        [nome_mae + sobrenome],
        [nome_pai + sobrenome],
        [nome_mae + ano_nascimento],
        [nome_pai + ano_nascimento],
        [nome_mae + nome_pet],
        [nome_pai + nome_pet],
        # Adicione mais padrões conforme necessário
    ]

print(padroes_senha)
