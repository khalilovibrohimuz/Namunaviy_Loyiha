from Manba.qiymat import sozlama
from Manba.qiymat import uslub
from Manba.qiymat import raqam
from Manba.qiymat import ibora
from Manba.qiymat import rang
from Ilova.versiya import *
from pygame import *
init()

VERSIYA = 0
for key in Versiyalar.keys():
    if VERSIYA == 0:
        VERSIYA = Versiyalar.get(key)
    if Versiyalar.get(key).Versiya_raqami >= VERSIYA.Versiya_raqami:
        VERSIYA = Versiyalar.get(key)

if sozlama.MAVZU == "yorqin":
    MAVZU = uslub.YorqinMavzu
elif sozlama.MAVZU == "tungi":
    MAVZU = uslub.TungiMavzu

DISPLEY_ULCHAMINI_OL = display.get_desktop_sizes()[0]
DISPLEY_ULCHAMI = (DISPLEY_ULCHAMINI_OL[0] * raqam.MASSHTAB // 100, DISPLEY_ULCHAMINI_OL[1] * raqam.MASSHTAB // 100)
DISPLEY_TURI = FULLSCREEN | SCALED
KENGLIK = DISPLEY_ULCHAMI[0]
BALANDLIK = DISPLEY_ULCHAMI[1]
YARIM_KENGLIK = KENGLIK // 2
YARIM_BALANDLIK = BALANDLIK // 2
DISPLEY = display.set_mode(DISPLEY_ULCHAMI, DISPLEY_TURI)
SOAT = time.Clock()
