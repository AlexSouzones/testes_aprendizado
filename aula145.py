class MeuError(Exception):
    ...



def levantar():
    exception_ = MeuError("A", "B", "C")
    exception_.add_note("Está errado")
    raise exception_


try:
  levantar()
except MeuError as error:
   print(error)
   raise
