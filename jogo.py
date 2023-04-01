
def jogar():
	letras_usadas = set() #Criamos um Conjunto pois não queremos que as letras repetidas sejam exibidas
	palavra_secreta = input("Digite a palavra para ser descoberta: ")
	print("\n" * 100) #limpamos a tela para que o jogador não leia a palavra
	print('*********************************')
	print('***Bem vindo ao jogo da Forca!***')
	print('*********************************')
	letras_acertadas = [] #Criamos uma lista, que será alimentada com a quantidade de letras da palavra secreta
	for x in range(1,len(palavra_secreta)+1): #usando o loop for, identificaremos com o range o tamanho da minha palavra secreta
		letras_acertadas.append("_") #em seguida, acrescentaremos um "_" para que o jogador saiba quantas letras a palavra possui
		x+1 #a cada letra analisada, o contador é incrementado
	enforcou = False #adicionamos o valor boleano para enforcou e acertou, para determinar quando o jogo termina
	acertou = False
	erros = 0 #definimos o valor de erro para 0
	print(' '.join(letras_acertadas)) #removemos as aspas e ","... DE: ['_','_'] PARA: _ _
	while not enforcou and not acertou: #enquanto não enforcou e não acertou, o jogo continua
		chute = input("Digite uma letra: ") # o jogador pode digitar mais uma letra
		if chute.upper() in palavra_secreta.upper(): #para letras maiúscula e minúsculas serão aceitas, usamos o método .upper()
			posicao = 0
			for letra in palavra_secreta.upper(): #cada vez que a letra for encontrada, o "_" na posição é substituído.
				if chute.upper() == letra.upper():
					letras_acertadas[posicao] = letra
				posicao = posicao + 1
		else:
			erros += 1 #se a letra estiver incorreta, o contador de erro é incrementado
		enforcou = erros == 6 # após 6 erros, o jogo termina
		acertou = '_' not in letras_acertadas
		print(' '.join(letras_acertadas))
		letras_usadas.add(chute.upper()) #as letras usadas são adicionadas e exibidas
		print("Letras Usadas: {}".format(letras_usadas))
	if acertou:
		print('Você ganhou!!')
	else:
		print('Você perdeu!!')
	print('Fim do jogo')

jogar()
