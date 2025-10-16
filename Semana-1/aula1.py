#a.x² +b.x +c"
"""
Raiz de Equação Quadrática 
"""
import math
    
def zeros(a,b,c):
# se a for igual 0 a solução -c/b   
    if a == 0:
        if b == 0:
            raise ValueError("A equação não possui solução")
        else:
            return -c/b

    delta = b**2 - (4*a*c) 
    if delta < 0:
        return None
    elif delta == 0:
        x = -b/(2*a)
        return[x,x]
    else:
        x1 = (-b + math.sqrt(delta))/(2*a)
        x2 = (-b - delta**0.5)/(2*a)
        return[x1,x2]

def main():
    x= zeros(1,-5,6)
    print(x)
if __name__ =="__main__":
    main()

   


    

    
    

