"""
Faça um jogo para o usuário adivinhar qual a palavra secreta.
- Você vai propor uma palavra secreta qualquer e vai dar a possibilidade para
o usuário digitar apenas uma letra.
- Quando o usuário digitar uma letra, você vai conferir se a letra digitada está
na palavra secreta.
    - Se a letra digitada estiver na palavra secreta, exiba a letra;
    - Se a letra digitada não estiver na palavra secreta, exiba *.
Faça a contagem de tentativas do seu usuário.
"""
import sys 
from getpass import getpass

palavra_secreta = getpass('Digite a palavra secreta: ').lower()
lista_palavra_secreta = list(palavra_secreta)

print('Tudo pronto para iniciar o jogo!')

palavra_formada = []
for l in range(len(lista_palavra_secreta)):
    palavra_formada.append('*')
print(palavra_formada)

tentativa = 0

def entrada_usuario():
    
    entrada = input('Digite uma letra ou SAIR: ').lower()
    #tentativa += 1
    
    # Validação da entrada do usuário:
    if entrada == 'sair':
        print('Até logo!')
        sys.exit()
    elif entrada.isalpha() :
        if len(entrada) == 1 :
            print('Letra recebida: ', entrada)
            confere_letra(entrada)
            confere_palavras()
            entrada_usuario()
        else:
            print('Digite somente uma letra')
            entrada_usuario()
    else: 
        print('Entrada inválida; O caractere digitado não é uma letra.')
        entrada_usuario()
             
def confere_letra(entrada):
      
    for i, letra in enumerate(lista_palavra_secreta, start =0):
        if entrada == letra:
            #tentativa -= 1
            palavra_formada[i] = entrada
        #else:
    
    #print(tentativa)
    
    print(palavra_formada)
    
def confere_palavras():
    str_palavra_formada = ''.join(palavra_formada)
    if str_palavra_formada == palavra_secreta:
        print('A palavra secreta é ', str_palavra_formada)
        sys.exit()
    else:
        entrada_usuario()
    
entrada_usuario()
print()
    