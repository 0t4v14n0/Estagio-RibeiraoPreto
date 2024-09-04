#3) Observe o trecho de código abaixo: int INDICE = 12, SOMA = 0, K = 1;
#  enquanto K < INDICE faça { K = K + 1; SOMA = SOMA + K; } imprimir(SOMA);
#Ao final do processamento, qual será o valor da variável SOMA?

def calc(INDICE, SOMA, K):

    while(K < INDICE):
        K=K+1
        SOMA = SOMA+K
    return SOMA

INDICE = 12
SOMA = 0
K = 1

print(calc(INDICE,SOMA,K))