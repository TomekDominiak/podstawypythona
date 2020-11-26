def piramida(n):
    for x, y in zip(range(1,n+1), range(1, 2*n, 2)):
        print(" "*(n-x)+"x"*y)

if __name__ == '__main__':
    piramida(5)
