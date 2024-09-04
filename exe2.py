def verificar_letra_a(texto):
    texto = texto.lower()
    
    if 'a' in texto:
        quantidade_a = texto.count('a')
        print(f"A letra 'a' aparece {quantidade_a} vezes na string.")
    else:
        print("A letra 'a' não foi encontrada na string.")

string_exemplo = input("Digite uma palavra ou frase")
verificar_letra_a(string_exemplo)