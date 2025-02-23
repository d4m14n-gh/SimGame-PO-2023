import tkinter as tk
from tkinter.ttk import OptionMenu

from antylopa import Antylopa
from barszcz_sosnowskiego import BarszczSosnowskiego
from cyber_owca import CyberOwca
from czlowiek import Czlowiek
from guarana import Guarana
from lis import Lis
from mlecz import Mlecz
from owca import Owca
from punkt import Punkt
from organizm import Organizm
from math import sin, cos, sqrt

from trawa import Trawa
from wilcze_jagody import WilczeJagody
from wilk import Wilk
from zolw import Zolw


class Okno:
    def __init__(self, swiat):
        self.c = None
        self.okno = None
        self.swiat = None
        self.a = 60
        self.b = 1
        self.kolory = {}
        self.zwierze = None
        padx = 10
        pady = 10
        self.okno = tk.Tk()
        self.okno.resizable(True, False)
        self.okno.protocol("WM_DELETE_WINDOW", lambda: exit(0))
        self.okno.title("PO projekt python")
        self.okno.geometry("800x450")
        self.okno.configure(bg="#313336")
        self.swiat = swiat
        ramka = tk.Frame(self.okno, bg="#313336")
        ramka.pack(pady=0, padx=0)
        if swiat.is_hex():
            r = int(self.a / sqrt(3))
            m = int((3 * self.a) / (sqrt(3) * 2))
            w = self.a * swiat.get_szerokosc() + self.a // 2 + 2 * self.b
            h = m * swiat.get_wysokosc() + r // 2 + 2 * self.b
            self.okno.geometry(f"{w + padx * 2 + 300}x{h + pady * 2 + 50}")
            self.c = tk.Canvas(ramka, bg="#313336", width=w, height=h, highlightthickness=0)
        else:
            w = self.a * swiat.get_szerokosc() + 2 * self.b
            h = self.a * swiat.get_wysokosc() + 2 * self.b
            self.okno.geometry(f"{w + 2 * padx + 300}x{h + 2 * pady + 50}")
            self.c = tk.Canvas(ramka, bg="#3C3F41", width=w, height=h, highlightthickness=0)
        self.c.bind("<Button-1>", self.mouse_click)
        self.c.pack(pady=pady, padx=padx, side=tk.LEFT, anchor=tk.NW)
        self.konsola = SkrolowanaKonsola(ramka, h, highlightthickness=0)
        self.konsola.pack(pady=pady, padx=padx, anchor=tk.NW)

        def nt():
            self.swiat.wykonaj_ture()
            self.rysuj_swiat()

        def wczytaj():
            self.swiat.wczytaj(options.index(so.get()))
            self.rysuj_swiat()

        def zapisz():
            self.swiat.zapisz(options.index(so.get()))
        b1 = tk.Button(self.okno, text="NASTEPNA TURA", command=nt)
        b1.configure(relief="flat", bd=0, padx=20, pady=8)
        b1.pack(side=tk.LEFT, padx=padx, anchor=tk.NW)
        b2 = tk.Button(self.okno, text="ZAPISZ", command=zapisz)
        b2.configure(relief="flat", bg="#7a1a1a", fg="#DADADA", bd=0, padx=20, pady=8)
        b2.pack(side=tk.LEFT, padx=0, anchor=tk.NW)
        b3 = tk.Button(self.okno, text="WCZYTAJ", command=wczytaj)
        b3.configure(relief="flat", bd=0, padx=20, pady=8)
        b3.pack(side=tk.LEFT, padx=padx, anchor=tk.NW)

        options = [""]
        for i in range(5):
            options.append(f"Slot {i+1}")
        # style = Style()
        # style.configure('TCombobox', foreground='blue', background='red', relief="flat")
        so = tk.StringVar()
        s = OptionMenu(self.okno, so, *options)
        s.configure(padding=12, width=8)
        s.pack(side=tk.LEFT, padx=0, anchor=tk.NW)
        so.set(options[1])

        def on_select(*args):
            index = options3.index(so2.get())
            self.zwierze = options2[index]
        options2 = ["", None, Czlowiek(), Wilk(), Owca(), Lis(), Zolw(), Antylopa(), CyberOwca()]
        options2.extend([Trawa(), Mlecz(), Guarana(), WilczeJagody(), BarszczSosnowskiego()])
        options3 = []
        for opt in options2:
            options3.append(str(opt))
        options3[1] = "Usun"
        so2 = tk.StringVar()
        so2.trace('w', on_select)
        a = OptionMenu(self.okno, so2, *options3)
        a.configure(padding=12, width=23)
        a.pack(side=tk.LEFT, padx=padx, anchor=tk.NW)
        so2.set(options3[1])

        def on_key_press(event):
            key = event.keysym
            if key == "c":
                self.mouse_click(event)
                return
            elif key == "f":
                if self.swiat.get_czlowiek():
                    self.swiat.get_czlowiek().aktywuj_umiejetnosc()
                    self.rysuj_swiat()
                return
            elif key == "n":
                swiat.wczytaj(0)
                self.rysuj_swiat()
                return
            if self.swiat.get_czlowiek():
                p = self.swiat.get_czlowiek().pozycja.y % 2 - 1
                if self.swiat.is_hex():
                    if key == "w":
                        self.swiat.get_czlowiek().set_kierunek(Punkt(p, 1))
                    elif key == "e":
                        self.swiat.get_czlowiek().set_kierunek(Punkt(p + 1, 1))
                    elif key == "z":
                        self.swiat.get_czlowiek().set_kierunek(Punkt(p, -1))
                    elif key == "x":
                        self.swiat.get_czlowiek().set_kierunek(Punkt(p + 1, -1))
                    elif key == "d":
                        self.swiat.get_czlowiek().set_kierunek(Punkt(1, 0))
                    elif key == "a":
                        self.swiat.get_czlowiek().set_kierunek(Punkt(-1, 0))
                    elif key == "space":
                        self.swiat.get_czlowiek().set_kierunek(Punkt(0, 0))
                    else:
                        return
                else:
                    if key == "Up":
                        self.swiat.get_czlowiek().set_kierunek(Punkt(0, 1))
                    elif key == "Down":
                        self.swiat.get_czlowiek().set_kierunek(Punkt(0, -1))
                    elif key == "Right":
                        self.swiat.get_czlowiek().set_kierunek(Punkt(1, 0))
                    elif key == "Left":
                        self.swiat.get_czlowiek().set_kierunek(Punkt(-1, 0))
                    elif key == "space":
                        self.swiat.get_czlowiek().set_kierunek(Punkt(0, 0))
                    else:
                        return
                self.swiat.wykonaj_ture()
                self.rysuj_swiat()
            elif key == "space":
                self.swiat.wykonaj_ture()
                self.rysuj_swiat()
        self.okno.bind("<KeyPress>", on_key_press)

    def mouse_click(self, event):
        if self.swiat.is_hex():
            self.mouse_click_hex(event)
            return
        x = (event.x-2*self.b)//self.a
        y = (event.y-2*self.b)//self.a
        y = self.swiat.get_wysokosc()-1-y
        if not self.zwierze:
            self.swiat.usun_organizm(Punkt(x, y), True)
        else:
            self.swiat.dodaj_organizm(self.zwierze.stworz_nowy(), Punkt(x, y), True)
        self.rysuj_swiat()

    def mouse_click_hex(self, event):
        r = int(self.a / sqrt(3))
        h = self.a//2
        y = int((2 * event.y - 2 * self.b - r / 2) / (3 * r))
        y = self.swiat.get_wysokosc()-1-y
        if y % 2 == 0:
            x = (event.x - self.b) // (h * 2)
        else:
            x = (event.x - self.b - h) // (h * 2)
            if (event.x - self.b - h) < 0:
                return
        # x = (event.x - self.b) // (ht * 2)
        if not self.swiat.na_mapie(Punkt(x, y)):
            return
        if not self.zwierze:
            self.swiat.usun_organizm(Punkt(x, y), True)
        else:
            self.swiat.dodaj_organizm(self.zwierze.stworz_nowy(), Punkt(x, y), True)
        self.rysuj_swiat_hex()

    def wypisz(self, text: str):
        self.konsola.wypisz_linie(text)

    def rysuj_swiat(self):
        if self.swiat.is_hex():
            self.rysuj_swiat_hex()
            return
        c = self.c
        swiat = self.swiat
        for x in range(swiat.get_szerokosc()):
            for y in range(swiat.get_wysokosc()):
                color = "#3C3F41"
                letter = "."
                fill = "#262626"
                punkt = Punkt(x, swiat.get_wysokosc()-1-y)
                if punkt in swiat.get_organizmy():
                    color = swiat.get_organizmy()[punkt].get_kolor()
                    letter = swiat.get_organizmy()[punkt].get_symbol()
                    if Organizm.avg_color(color) < 90:
                        fill = "#DADADA"
                if punkt in self.kolory and self.kolory[punkt] == color:
                    continue
                else:
                    self.kolory[punkt] = color
                x1 = x * self.a + self.b
                y1 = y * self.a + self.b
                x2 = x1 + self.a
                y2 = y1 + self.a
                c.create_rectangle(x1, y1, x2, y2, fill=color, outline="#2B2B2C", width=self.b*2)
                text_x = (x1 + x2) / 2
                text_y = (y1 + y2) / 2
                c.create_text(text_x, text_y, text=letter, fill=fill)

    def rysuj_swiat_hex(self):
        c = self.c
        swiat = self.swiat
        for x in range(swiat.get_szerokosc()):
            for y in range(swiat.get_wysokosc()):
                color = "#3C3F41"
                letter = "."
                fill = "#262626"
                punkt = Punkt(x, swiat.get_wysokosc() - 1 - y)
                if punkt in swiat.get_organizmy():
                    color = swiat.get_organizmy()[punkt].get_kolor()
                    letter = swiat.get_organizmy()[punkt].get_symbol()
                    if Organizm.avg_color(color) < 90:
                        fill = "#DADADA"
                if punkt in self.kolory and self.kolory[punkt] == color:
                    continue
                else:
                    self.kolory[punkt] = color
                r = int(self.a/sqrt(3))
                m = int((3*self.a)/(sqrt(3)*2))
                h = self.a//2
                x1 = x * self.a + self.b + h
                if (self.swiat.get_wysokosc()-y) % 2 == 0:
                    x1 += h
                y1 = y * m + self.b + r
                self.draw_hexagon(x1, y1, r, color)
                text_x = x1
                text_y = y1
                c.create_text(text_x, text_y, text=letter, fill=fill)

    def draw_hexagon(self, x: int, y: int, promien: int, kolor):
        kat = 2 * 3.14159 / 6
        punkty = []
        for i in range(6):
            x_i = x + promien * sin(i * kat)
            y_i = y + promien * cos(i * kat)
            punkty.append((x_i, y_i))
        self.c.create_polygon(punkty, outline='#2B2B2C', fill=kolor, width=self.b*2)


class SkrolowanaKonsola(tk.Frame):
    def __init__(self, master, h, *args, **kwargs):
        super().__init__(master, *args, **kwargs)
        self.text_box = tk.Text(self, wrap="word", state="disabled")
        self.text_box.configure(background="#313336", foreground="#DADADA", relief="flat", bd=2)
        self.scrollbar = tk.Scrollbar(self, command=self.text_box.yview)
        self.text_box.configure(yscrollcommand=self.scrollbar.set)
        self.text_box.configure(height=h//21)
        self.text_box.pack(side="left", fill="both", expand=True)
        self.scrollbar.pack(side="right", fill="y")

    def wypisz_linie(self, tekst):
        self.text_box.configure(state="normal")
        self.text_box.insert("end", "\n" + tekst)
        self.text_box.configure(state="disabled")
        self.text_box.see("end")
