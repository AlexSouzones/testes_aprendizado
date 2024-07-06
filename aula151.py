
# def my_repr(class_):
#   class_name = class_.__class__.__name__
#   class_dict = class_.__dict__
#   return f"{class_name}{class_dict}"

# class MyReprMixin:

#   def __repr__(self) -> str:
#     class_name = self.__class__.__name__
#     class_dict = self.__dict__
#     return f"{class_name}{class_dict}"


# class Time:
#   def __init__(self, nome) -> None:
#     self.nome = nome


# class Planeta:
#   def __init__(self, nome) -> None:
#     self.nome = nome
    


# brasil = Time("Brasil")
# portugal = Time("Portugal")

# terra = Planeta("Terra")
# jupiter = Planeta("Jupiter")

# print(brasil)
# print(portugal)

# print(terra)
# print(jupiter)
def meu_repr(self):
    class_name = self.__class__.__name__
    class_dict = self.__dict__
    class_repr = f'{class_name}({class_dict})'
    return class_repr


def adiciona_repr(cls):
    cls.__repr__ = meu_repr
    return cls


@adiciona_repr
class Time:
    def __init__(self, nome):
        self.nome = nome


@adiciona_repr
class Planeta:
    def __init__(self, nome):
        self.nome = nome


brasil = Time('Brasil')
portugal = Time('Portugal')

terra = Planeta('Terra')
marte = Planeta('Marte')

print(brasil)
print(portugal)

print(terra)
print(marte)