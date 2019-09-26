from random import randrange
from alice import Alice
from bob import Bob

def seleciona_primo():
    with open("primos.txt") as f:
        primos = f.readline().split()
        return int(primos[randrange(0,len(primos))])

def calcula_raiz_primitiva_e_primo():
    while True:
        p = seleciona_primo()
        for g in range(2,p):
            coprimos = set(range(1,p))
            for i in range(1, p):
                try:
                    coprimos.remove((g**i) % p)
                except:
                    break
            if len(coprimos) == 0:
                f = open("canal.txt", "w")
                f.write("O gerador = " + str(g))
                f.write("\nO primo = " + str(p) + "\n")
                f.close()
                return g,p
     
def limpa_canais(canal, cppa, cppb):
    open(canal, 'w').close()
    open(cppa, 'w').close()
    open(cppb, 'w').close()

# O "canal" representa o ambiente inseguro onde haverá a comunicação entre Bob e Alice
canal = "canal.txt"

# O caminho_chave_privada serve para provar que seus números secretos podem ser diferentes e que resultam na mesma chave privada
# NÃO É UTILIZADO EM UM SISTEMA DH REAL
caminho_chave_privada_alice = "chave_privada_alice.txt"
caminho_chave_privada_bob = "chave_privada_bob.txt"

# Limpa os arquivos privados e o canal público
limpa_canais(canal, caminho_chave_privada_alice, caminho_chave_privada_bob)

# É selecionado aleatoriamente um número primo positivo até 1000 e calculado sua menor raiz primitiva
(g, p) = calcula_raiz_primitiva_e_primo()

# São criados Alice e Bob recebendo o gerador e o número primo pelo canal público
alice = Alice(canal, caminho_chave_privada_alice, g, p)
bob = Bob(canal, caminho_chave_privada_bob, g, p)
input()

# Ada e Bob vão armazenar localmente as variáveis g e p que eles escolheram pelo público
alice.calcula_e_grava_A()
bob.calcula_e_grava_B()
input()

# Ada e Bob vão ler os resultados das chaves intermediárias um do outro que foram passados pela rede pública
alice.ler_B()
bob.ler_A()

# Os números secretos são salvos para provar que mesmo podendo ser diferentes, a chave privada é idêntica
# Ada e Bob vão gravar localmente sua chave privada, que será usada para descriptografar as mensagens
alice.gravar_num_e_chave_secretos()
bob.gravar_num_e_chave_secretos()


