def next_number():
  yield 1
  yield 2
  yield 3


finidade = next_number()

print(next(finidade))
print(next(finidade))
print(next(finidade))

