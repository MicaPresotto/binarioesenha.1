import random 

print('Sua senha: ') #mostrando a senha na qual foi impressa.

senha1 = random.randint(1,9) #dando numeros aleatorios para uma senha.
senha2 = random.randint(1,9)
senha3 = random.randint(1,9)
senha4 = random.randint(1,9)
senha5 = random.randint(1,9)
senha = str(senha1) + str(senha2) +  str(senha3) +  str(senha4) +  str(senha5)
#transforma as senhas em string
print (senha) 
x = 1
j = 1
while j == 1:
    
    while x == 1:
        palavra = input('Digite os numeros: ')

        if palavra[0] == str(senha1) :
            print ('+1')
            #se o primeiro numero da senha estar certo com o que o usuario digitou,irá printar isso.
        else:
            print ( '-1')
            #se nao,printa isso.
        
        if palavra[1] == str(senha2)  :
            print ('+1' )
            #se o segundo numero da senha estar certo com o que o usuario digitou,irá printar isso.

        else:
            print ('-1')
            
        if palavra[2] == str(senha3)  :
            
            print ('+1')
            #se o terceiro numero da senha estar certo com o que o usuario digitou,irá printar isso.

        else:
            print ('-1')
            
        if palavra[3] == str(senha4)  :
            print ('+1' )
            #se o quarto numero da senha estar certo com o que o usuario digitou,irá printar isso.

        else:
            print ('-1')
            
        if palavra[4] == str(senha5):
            print ('+1' )
            #se o quinto numero da senha estar certo com o que o usuario digitou,irá printar isso.

        else:
            print ('-1')


        if palavra == senha:
            print ('Você ganhou')
            break
    if input('Quer continuar jogando?(Y/N): ').upper() == 'N':
        #pediu para o user se ele irá querer continuar jogando
        print('Obrigado por jogar!!')
        # se ele digitou 'n',aparece isso.
        x = 0
        j = 0
    else:
        senha1 = random.randint(1,9)
        senha2 = random.randint(1,9)
        senha3 = random.randint(1,9)
        senha4 = random.randint(1,9)
        senha5 = random.randint(1,9)
        x = 1
        j = 1
        senha = str(senha1) + str(senha2) +  str(senha3) +  str(senha4) +  str(senha5)
        print (senha)

        
