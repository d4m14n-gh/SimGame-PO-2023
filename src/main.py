import time

from swiat import Swiat
from swiat_hex import SwiatHex
from punkt import Punkt
from zwierze import Zwierze
from owca import Owca
from zolw import Zolw
from lis import Lis
from trawa import Trawa
from wilcze_jagody import WilczeJagody
from wilk import Wilk
from antylopa import Antylopa
from okno import Okno
from mlecz import Mlecz
from barszcz_sosnowskiego import BarszczSosnowskiego
from cyber_owca import CyberOwca
from guarana import Guarana
from czlowiek import Czlowiek
from ctypes import windll
windll.shcore.SetProcessDpiAwareness(1)

swiat = SwiatHex(20, 10)
organizmy = [Czlowiek(), Wilk(), Owca(), Lis(), Zolw(), Antylopa(), CyberOwca()]
organizmy.extend([Trawa(), Mlecz(), Guarana(), WilczeJagody(), BarszczSosnowskiego()])

swiat.dodaj_organizm(Owca(), Punkt(1, 3))
swiat.dodaj_organizm(Czlowiek(), Punkt(2, 3))
swiat.dodaj_organizm(Zolw(), Punkt(1, 6))
swiat.dodaj_organizm(Owca(), Punkt(11, 4))
swiat.dodaj_organizm(Lis(), Punkt(9, 4))
swiat.dodaj_organizm(Lis(), Punkt(15, 4))
swiat.dodaj_organizm(Trawa(), Punkt(11, 7))
swiat.dodaj_organizm(Trawa(), Punkt(12, 3))
swiat.dodaj_organizm(Trawa(), Punkt(15, 5))
swiat.dodaj_organizm(WilczeJagody(), Punkt(19, 8))
swiat.dodaj_organizm(Wilk(), Punkt(11, 4))
swiat.dodaj_organizm(Antylopa(), Punkt(13, 1))
swiat.dodaj_organizm(Mlecz(), Punkt(19, 0))
swiat.dodaj_organizm(BarszczSosnowskiego(), Punkt(18, 0))
swiat.dodaj_organizm(CyberOwca(), Punkt(15, 4))
swiat.dodaj_organizm(Guarana(), Punkt(1, 1))

swiat.zapisz(0)
ok = Okno(swiat)
swiat.set_konsola(ok.wypisz)
ok.wypisz(f'{swiat.__class__.__name__} wymiary {swiat.get_szerokosc()}x{swiat.get_wysokosc()}\n')
for o in organizmy:
    ok.wypisz(o.get_symbol()+"-"+str(o))

ok.rysuj_swiat()
ok.okno.mainloop()
swiat.wykonaj_ture()
