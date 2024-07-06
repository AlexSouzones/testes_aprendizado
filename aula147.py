class Ponto:
  def __init__(self, x: int, y: int):
    self.x = x
    self.y = y
    
  def __repr__(self) -> str:
    return f"{self.__class__.__name__}(x={self.x}, y={self.y})"
  

p1 = Ponto(1, 2)
p2 = Ponto(231, 342)

print(p1)
print(p2)

nome = "Alex"
print(nome.__subclasshook__)