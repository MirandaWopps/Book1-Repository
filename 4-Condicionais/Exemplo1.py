#A variavel livros armazena a quantidade de livros.
livros = 2
#1
if livros: # <- Essa é uma estrutura condicional. Começam com 'if', 'else', 'else if'.
    #   Os 4 espaços antes desse comentário fazem qualquer código pertencer a estrutura.
    # Quando o código volta a ser escrito antes dos 4 espaços significa que a estrutura
    # terminou.
    #   A estrutura condicional é ativada se a condição for verdadeira. A estrutura será 
    # "ativada" porque livros = 2. Isso significa que livros existe, portanto, a condição é 
    # True. Se livros fosse "0" ou "False" essa estrutura não aconteceria.  
    print("Print 1: Existem livros!\n") # \n  significa 'pula linha' para o compilador
    
#2 O código voltou a ser escrito antes dos 4 espaços, então, é outra estrutura.        
if livros > 1:# Lemos: "o primeiro valor é maior que 1 ?"
    #note os 4 espaços antes do próximo comando.
    print("Print 2: Existe mais de 1 livro")
  
#3    
if livros == 2:# Lemos: <primeiro valor> é igual a 2 ?" Usamos "==" porque é uma comparação !
    print("Print 3: Existem 2 livros")
    
#4
if livros < 1:#Lemos: "o primeiro valor é menor que 1 ?"
    print("Print4: O primeiro valor é menor que 1.") # NAO EXECUTA porque é a condição falsa.
    
#5
if livros != 0:#Lemos: "livros é diferente de 0 ?" 
    print("Print 5: a quantidade de livros é diferente de 0.")

#6 Estrutura condicional com "else". Essa estrutura significa que se a primeira condição
# for falsa(False), então, outro caminho é tomado. Esse caminho está no "else".
if livros ==1: #Livros não é 1 ! FALSE
    print("Print 6: o livro é maior que 1 !") #Não executa essa parte.
else: #Então, execute essa parte.
    print("Print 6: O livro é maior que 2 !")

#7 Estrutura condicional "elif".
if livros ==0: #Livros é 0 ? Não ! FALSE 
    print("A quantidade de livos é igual a 0.")
elif livros ==1: #Livros é 1 ? Não ! FALSE ! Podes escrever vários "else if" se quiser.
    print("A quantidade de livros é 1.")
else: #Então, como nada acima é verdade, o conteúdo no else é executado.
    print("Print 7: O livro é maior que 2 !")

#8 Estrutura condicional dentro de estrutura condicional.
if livros == 2:
    if livros % 2 == 0:
        print("Print 8: livros é par !")
    else:
        print("Livros é ímpar !")

#9 Estrutura com operador condicional 'and'. Se tudo que está na esquerda e na direita do
#operador 'and' for verdade, então a condição é TRUE. Se 1 for FALSE não executará.
if livros > 1 and livros >= 3: # >= Significa que será verdade(TRUE) se livros for maior
# ou igual a 3.
    print("Print 9: livros é maior que 1 e maior ou igual a 3.")


#10 Estrutura com operador condicional 'or'. Se pelo menos 1 condição que está na esquerda e # na direita do operador 'and' for verdade, então a condição é TRUE. Se os 2 forem falses
# a execução não ocorre.
if livros > 1 or livros >= 3:
    print("Print 10: livros é maior que 1 e maior ou igual a 3.")
