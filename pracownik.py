class pracownik:
    podniesc_wyplate = 1.04

    def __init__(self,first,last,pay):
        self.first = first
        self.last = last
        self.pay = float(pay)
        self.email = f"{first},{last}@.com"
    def podwyzka(self):
        self.pay *= self.podniesc_wyplate
    def podtek(self, prug_dochodowy=85000):
        self.roczna_pensja = self.pay * 12
        if self.roczna_pensja < prug_dochodowy:
            print(f'Twoj podatek dochodowy to {self.roczna_pensja * 0.17}')
        else:
            print(f'Twoj podatek dochodowy to {self.roczna_pensja * 0.32}')
    @classmethod
    def ustaw_roczna_podwyzke(cls,nowa_podwyzka):
        cls.podniesc_wyplate = nowa_podwyzka
    @staticmethod
    def wyswietl_informace_podatkowe(kwota):
        print("pierwszy prug 17%")
        print(f"drugi powyzej {kwota} jest pnjety drogim")
        print("pierwszy prug 32%")

tomek = pracownik("tomek","dominiak", 10000)
pawlinska=pracownik("aga","pawlinska", 10000)

print(tomek.podniesc_wyplate)
print(pawlinska.podniesc_wyplate)

pracownik.ustaw_roczna_podwyzke(1.2)

print(tomek.podniesc_wyplate)
print(pawlinska.podniesc_wyplate)

tomek.wyswietl_informace_podatkowe(8500)

class developer(pracownik):
    podniesc_wyplate = 1.10
    def __init__(self,first,last,pay,jezyk_programowania):
        super().__init__(first,last,pay)
        self.jezyk_programowania = jezyk_programowania


tomek2=pracownik("tomek","dom",10000)
tomek3=developer("tomasz","domi",10000,"phthon")

print(tomek2.podniesc_wyplate)
print(tomek3.podniesc_wyplate)

print(tomek3.jezyk_programowania)


tomek.podtek()
tomek.podtek(200000)