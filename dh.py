from ada import Ada
from bob import Bob



# O "canal" representa o ambiente inseguro onde haverá a comunicação entre Bob e Ada
canal = "canal.txt"

# O caminho_chave_privada serve para provar que seus números secretos podem ser diferentes e que resultam na mesma chave privada
# NÃO É UTILIZADO EM UM SISTEMA DH REAL
caminho_chave_privada_ada = "chave_privada_ada.txt"
caminho_chave_privada_bob = "chave_privada_bob.txt"

# Limpa os arquivos onde serão armazenadas as chaves privadas e os resultados trocados
open(caminho_chave_privada_ada, "w").close()
open(caminho_chave_privada_bob, "w").close()

ada = Ada(canal, caminho_chave_privada_ada)
bob = Bob(canal, caminho_chave_privada_bob)

# Ada e Bob vão armazenar localmente as variáveis g e p que eles escolheram pelo público
ada.ler_g_p()
bob.ler_g_p()

# Ada e Bob vão enviar publicamente seus respectivos resultados de g^num_secreto(mod p)
ada.gravar_A()
bob.gravar_B()
input()

# Ada e Bob vão ler os resultados um do outro que foram passados pelo rede pública
ada.ler_B()
bob.ler_A()

# Os números secretos são salvos para provar que podem ser diferentes e mesmo assim a chave privada é identica
ada.gravar_num_secreto()
bob.gravar_num_secreto()

# Ada e Bob vão gravar localmente sua chave privada, que será usada para descriptografar as mensagens
ada.calcula_chave_secreta()
bob.calcula_chave_secreta()