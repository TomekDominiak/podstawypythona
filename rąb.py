
def piramida(n):
    for x, y in zip(range(-n, n+1), range(n*2, 2*-n-1, -2)):
        z=abs(y)-(n*2+1)
        print(" "*abs(x)+"x"*abs(z))

if __name__ == '__main__':
   piramida(5)


