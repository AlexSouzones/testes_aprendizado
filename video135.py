#lambda teste

# def executa_function(function, *args):
#   return function(*args)


# print(executa_function(
#   lambda a, b: 
#   a + b,
#   1, 4
# ))

def args(*args, **kwargs):
  print(kwargs)


args("ok", nome="ola")