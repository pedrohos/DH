import random

class Bob:
    def __init__(self, tf, ccp):
        self.g = None
        self.p = None

        self.A = None
        self.B = None

        self.tf = tf
        self.caminho_chave_privada = ccp

        self.numero_secreto_b = random.randrange(1, 10)


    def ler_g_p(self):
        with open(self.tf) as f:
            linhas = f.readlines()

            for linha in linhas:
                linha = linha.replace("\n", "")

            g = int(linhas[0].split()[1])
            p = int(linhas[1].split()[1]) 

        self.g = g
        self.p = p

        self.B = (self.g**self.numero_secreto_b)%self.p

    def gravar_B(self):
        f = open(self.tf, "a+")
        f.write("B= " + str(self.B) + "\n")
        f.close()

    def ler_A(self):
        with open(self.tf) as f:
            linhas = f.readlines()

            lista_invertida = [linhas[i] for i in range(len(linhas) - 1, -1, -1)]
            lista_invertida = [e.replace('\n', '') for e in lista_invertida]
            lista_invertida = [e.replace('A= ', '-') for e in lista_invertida]

            for i in range(len(lista_invertida)):
                if lista_invertida[i][0] == "-":
                    self.A = int(lista_invertida[i][1:])
                    break

    def gravar_num_secreto(self):
        f = open(self.caminho_chave_privada, "a+")
        f.write("Meu numero secreto eh " + str(self.numero_secreto_b) + "\n")
        f.close()

    def calcula_chave_secreta(self):
        f = open(self.caminho_chave_privada, "a+")

        chave_secreta = (self.A**self.numero_secreto_b)%self.p
        f.write("A chave criptografada eh " + str(chave_secreta))

        f.close()
