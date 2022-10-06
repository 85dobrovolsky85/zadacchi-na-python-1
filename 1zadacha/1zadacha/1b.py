#задача 2. Напишите программу для. 
# проверки истинности утверждения ¬(X ⋁ Y ⋁ Z) = ¬X ⋀ ¬Y ⋀ ¬Z 
# для всех значений предикат.
from itertools import product
  
for x, y, z in product([0, 1], repeat=3): 
    print(not(x or y or z) , not x and not y and not z)