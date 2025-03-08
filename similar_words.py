def count_words(array, pivot): # função que conta a quantidade de strings da lista array similares à string pivot
    amount = array.count(pivot) # verifica a quantidade de strings iguais a pivot
    for i in array:
        if len(i) == len(pivot) and sum(1 for j in range(len(pivot)) if i[j] != pivot[j]) == 1: # verifica se a string i de array se torna pivot trocando um de seus caracteres
            amount += 1
        elif len(i) + 1 == len(pivot) and any(pivot[:j] + pivot[j+1:] == i for j in range(len(pivot))): # verifica se pivot se torna a string i de array removendo um caractere de pivot
            amount += 1
        elif len(i) - 1 == len(pivot) and any(i[:j] + i[j+1:] == pivot for j in range(len(i))): # verifica se a string i de array se torna pivot removendo um caractere de i
            amount += 1

    return amount

num = int(input()) # recebe número inteiro N
word = input() # recebe palavra especial
words = [input() for _ in range(num)] # recebe N strings

amount = count_words(words,word) # conta a quantidade de palavras similares

print(amount)