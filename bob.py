import random

class Bob:
    def __init__(self, tf, ccp, g, p):
        self.SIMBOLO = "-"
        self.g = g
        self.p = p

        self.A = None
        self.B = None

        self.tf = tf
        self.caminho_chave_privada = ccp

        self.numero_secreto_b = random.randrange(0, p - 1)

        f = open(ccp, "a+")
        f.write("Meu gerador = " + str(self.g) + "\n")
        f.write("Meu numero primo = " + str(self.p) + "\n")
        f.write("Meu numero secreto b = " + str(self.numero_secreto_b) + "\n")
        f.close()

    def calcula_e_grava_B(self):
        self.B = (self.g**self.numero_secreto_b)%self.p

        f = open(self.tf, "a+")
        f.write("B= " + str(self.B) + "\n")
        f.close()

        f = open(self.caminho_chave_privada, "a+")
        f.write("B= " + str(self.B) + "\n")
        f.close()

    def ler_A(self):
        with open(self.tf) as f:
            linhas = f.readlines()

            lista_invertida = [linhas[i] for i in range(len(linhas) - 1, -1, -1)]
            lista_invertida = [e.replace('\n', '') for e in lista_invertida]
            lista_invertida = [e.replace('A= ', self.SIMBOLO) for e in lista_invertida]

            for i in range(len(lista_invertida)):
                if lista_invertida[i][0] == self.SIMBOLO:
                    self.A = int(lista_invertida[i][1:])
                    break
        
        f = open(self.caminho_chave_privada, "a+")
        f.write("A= " + str(self.A) + "\n")
        f.close()

    def gravar_num_e_chave_secretos(self):
        f = open(self.caminho_chave_privada, "a+")
        chave_secreta = (self.A**self.numero_secreto_b)%self.p
        f.write("A chave criptografada = " + str(chave_secreta) + "\n")
        f.close()
