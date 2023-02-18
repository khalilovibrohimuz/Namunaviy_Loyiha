class Versiya:
    def __init__(self,
                 Versiya_raqami,
                 Versiya_nomi,
                 Muallif,
                 Vaqt,
                 Izoh,
                 Havolalar
            ):
        self.Versiya_raqami = Versiya_raqami + 1
        self.Versiya_nomi = Versiya_nomi
        self.Muallif = Muallif
        self.Vaqt = Vaqt
        self.Izoh = Izoh
        self.Havolalar = Havolalar

    def versiya_haqida(self):
        print(f"\nVersiya raqami - {self.Versiya_raqami}")
        print(f"Versiya nomi - \"{self.Versiya_nomi}\"")
        print(f"Muallifi - \"{self.Muallif}\"")
        if self.Versiya_nomi == 1:
            print(f"Yaratilgan vaqti - \"{self.Vaqt}\"")
        else:
            print(f"O'zgartirilgan vaqti - \"{self.Vaqt}\"\n")
        print(f"Izoh:\n/**\n{self.Izoh}\n**/\n")
        for key in self.Havolalar.keys():
            if len(key) > 7:
                print(f"{key}\t - {self.Havolalar.get(key)}")
            else:
                print(f"{key}\t\t - {self.Havolalar.get(key)}")
        print()
