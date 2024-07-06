from contextlib import contextmanager


@contextmanager
def my_open(caminho_arquivo, modo):
  try:
    print("Abrindo arquivo")
    arquivo = open(caminho_arquivo, modo, encoding="utf8")
    yield arquivo
  
  finally:
    print("fechando arquivo")
    arquivo.close()


with my_open('aula149.txt', 'w') as arquivo:
  arquivo.write("Linha 1\n")
  arquivo.write("Linha 2\n")
  arquivo.write("Linha 3\n")
  print(arquivo)
