class Multiplicar:
  def __init__(self, func) -> None:
    self.func = func


  def __call__(self, *args, **kwargs):
    print(args, kwargs)
    return self.func(*args, **kwargs)


@Multiplicar
def soma(x, y):
  return x + y


c1 = soma(2, 4)
