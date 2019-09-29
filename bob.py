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
            linhas = [e.replace('A= ', self.SIMBOLO) for e in linhas]

            for i in range(len(linhas)):
                if linhas[i][0] == self.SIMBOLO:
                    self.A = int(linhas[i][1:])
                    break
        
        f = open(self.caminho_chave_privada, "a+")
        f.write("A= " + str(self.A) + "\n")
        f.close()

    def mostrar_chave_secreta(self):
        f = open(self.caminho_chave_privada, "a+")
        chave_secreta = (self.A**self.numero_secreto_b)%self.p
        f.write("A chave criptografada = " + str(chave_secreta) + "\n")
        f.close()
