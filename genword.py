from itertools import product

nome =  'Rafael'#input("Digite o nome: ").lower()
sobrenome = 'Lima'#input("Digite o sobrenome: ").lower()
apelido = 'bi'#input("Digite o apelido: ").lower()
nome_mae = 'valeria' #input("Digite o nome da mãe: ").lower()
nome_pai = ''#input("Digite o nome do pai: ").lower()
nome_pet = ''#input("Digite o nome do pet: ").lower()
data_nascimento ='1207200' #input("Digite a data de nascimento (DDMMYYYY): ")
ano_nascimento = '2000'#input("Digite o ano de nascimento: ")
telefone = '998840910'#input("Digite o telefone: ")
telefone2 = '988840910'#input("Digite o telefone 2: ")
nome_minusculo = nome.lower()
nome_maiusculo = nome.upper()
nome_capitalizado = nome.capitalize()
sobrenome_minusculo = sobrenome.lower()
sobrenome_maiusculo = sobrenome.upper()
sobrenome_capitalizado = sobrenome.capitalize()



# Numeros
um_digito = [''.join(map(str, combo)) for combo in product(range(10), repeat=1 )]
dois_digitos = [''.join(map(str, combo)) for combo in product(range(10), repeat=2 )]
tres_digitos = [''.join(map(str, combo)) for combo in product(range(10), repeat=3 )]
quatro_digitos = [''.join(map(str, combo)) for combo in product(range(10), repeat=4 )]
cinco_digitos = [''.join(map(str, combo)) for combo in product(range(10), repeat=5 )]
seis_digitos = [''.join(map(str, combo)) for combo in product(range(10), repeat=6 )]
#sete_digitos = [''.join(map(str, combo)) for combo in product(range(10), repeat=7 )]
#oito_digitos = [''.join(map(str, combo)) for combo in product(range(10), repeat=8 )]


    

  # Gera padrões de senhas combinando as informações fornecidas
padroes_senha = [
        nome + sobrenome,
        nome_minusculo + sobrenome,
        nome_maiusculo + sobrenome,
        nome_capitalizado + sobrenome,
        nome_minusculo + sobrenome_minusculo,
        nome_maiusculo + sobrenome_maiusculo,
        nome_capitalizado + sobrenome_capitalizado,
        nome + sobrenome + ano_nascimento,
        nome_minusculo + sobrenome + ano_nascimento,
        nome_maiusculo + sobrenome + ano_nascimento,
        nome_capitalizado + sobrenome + ano_nascimento,
        nome + sobrenome_maiusculo + ano_nascimento,
        nome_minusculo + sobrenome_maiusculo + ano_nascimento,
        nome_maiusculo + sobrenome_maiusculo + ano_nascimento,
        nome_capitalizado + sobrenome_maiusculo + ano_nascimento,
        nome_pet,
        nome_pet + telefone,
        nome_pet + telefone2,
        nome_pet + ano_nascimento,
        nome_pet + sobrenome,
        nome_pet + sobrenome + ano_nascimento,
        nome_pet + sobrenome_maiusculo,
        nome_pet + sobrenome_maiusculo + ano_nascimento,
        nome_pet + sobrenome_capitalizado,
        nome_pet + sobrenome_capitalizado + ano_nascimento,
        nome + telefone,
        sobrenome + telefone,
        nome + telefone2,
        sobrenome + telefone2,
        nome + sobrenome + telefone,
        nome + sobrenome + telefone2,
        nome+telefone,
        sobrenome + telefone,
        nome + telefone2,
        sobrenome + telefone2,
        nome + sobrenome + telefone,
        nome + sobrenome + telefone2,
        nome + sobrenome + ano_nascimento,
        nome + sobrenome + nome_pet,
        nome + sobrenome + apelido,
        nome + sobrenome + apelido + ano_nascimento,
        nome + sobrenome + nome_pet + apelido,
        nome + ano_nascimento,
        nome + ano_nascimento,
        nome_pet,
        apelido,
        apelido + ano_nascimento,
        nome_minusculo + sobrenome_minusculo,
        nome_maiusculo + sobrenome_maiusculo,
        nome_capitalizado + sobrenome_capitalizado,
        nome_minusculo + sobrenome_capitalizado,
        nome_maiusculo + sobrenome_minusculo,
        nome_capitalizado + sobrenome_maiusculo,
        nome_capitalizado + ano_nascimento,
        nome_minusculo + ano_nascimento,
        nome_maiusculo + ano_nascimento,
        nome_capitalizado + nome_pet,
        nome_mae + nome,
        nome_pai + nome,
        nome_mae + sobrenome,
        nome_pai + sobrenome,
        nome_mae + ano_nascimento,
        nome_pai + ano_nascimento,
        nome_mae + nome_pet,
        nome_pai + nome_pet,
        # Padroes com digito
    ] + [digito+nome for digito in um_digito
    ] + [nome+digito for digito in um_digito
    ] + [nome_capitalizado+digito for digito in um_digito
    ] + [nome_minusculo+digito for digito in um_digito
    ] + [nome_maiusculo+digito for digito in um_digito
    ] + [digito+nome_capitalizado for digito in um_digito
    ] + [digito+nome_minusculo for digito in um_digito
    ] + [digito+nome_maiusculo for digito in um_digito
    ] + [digito+nome_capitalizado for digito in um_digito
    ] + [digito+nome_minusculo for digito in um_digito
    ] + [digito+nome_minusculo for digito in um_digito
         
              
    ] + [digito+nome for digito in um_digito
    ] + [digito+nome for digito in um_digito
    ] + [digito+nome for digito in um_digito]
    
     

print(padroes_senha)
