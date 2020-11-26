
# def choinka(h,n):
#     for x,y in list(zip(range(1,(n+1)),range(1,n*2,2))):
#         print(" "* (n-x) + "*"* y)
#
# choinka(1,2)
#
# def rysujChoinke(warstw):
#   max = warstw * 2 + 1
#   for i in range(1, warstw + 1):
#     for j in range(i + 1):
#       znakow = 2 * j + 1
#       print(' ' * ((max - znakow) // 2) + ('*' * znakow))
#   print(' ' * (max // 2) + "*")
#
# rysujChoinke(3)

# def rysowanie_choinki2(wysokosc,liczba_segmentow):
# #     drewno=int(0.1*wysokosc*liczba_segmentow)+1
# #     for i in range(1,liczba_segmentow+1):
# #         for j in range(1,wysokosc+1):
# #             print(f' '*(wysokosc-j)+'+'*(2*j-1)+' '*(wysokosc-j))
# #     for k in range(1,drewno+1):
# #         print(f' '*(wysokosc-1)+'+')
# #
# # rysowanie_choinki2(3,2)

# def choinka(n):
#     if n%2==0:
#         n=n+1
#         for a, b in zip(range(n,4,-1), range(0,2*n,2)):
#             print(' '*a+'*'*(b+1))
#         for a, b in zip(range(n,4,-1), range(n//2,2*n,2)):
#             print(' '*(a-3)+'*'*(b+1))
#         for a, b in zip(range(n,0,-1), range(n,2*n,2)):
#             print(' '*(a-5)+'*'*(b+1))
#         for a in range(0,n//4):
#             print(' '*n+'*'*(n//4)+' '*2)
#     else:
#         for a, b in zip(range(n,4,-1), range(0,2*n,2)):
#             print(' '*a+'*'*(b+1))
#         for a, b in zip(range(n,4,-1), range(n//2,2*n,2)):
#             print(' '*(a-3)+'*'*(b+1))
#         for a, b in zip(range(n,0,-1), range(n,2*n,2)):
#             print(' '*(a-5)+'*'*(b+1))
#         for a in range(0,n//4):
#             print(' '*n+'*'*(n//4)+' '*2)
#
#
# if __name__=='__main__':
#     choinka(10)

#(i = ilość pięter, s = szerokość pnia)
def multiple_triangle(i,s):
    p = 1
    t = (i * 2 - 1)
    n = 0
    b = i
    lista = []
    while n < b:
        for e in range(1, i + 1):
            print(' ' * (t - e) + '*' * p)
            p += 2
        n += 1
        lista.append(p)
        p = 1
        i += 1
    p = 0
    while p < 2:
        print(' ' * (int((max(lista)-1)/2)-2) + '*' * s)
        p += 1

multiple_triangle(4,3)