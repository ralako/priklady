import os, sys
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from zadanie import *



# ODMOCNINY

class P51(Zadanie):     # zlomok simple
    def __init__(self):
        super().__init__()
        while True:
            A,B,C,D,E,F,G,H = super().zvolKoef(8, [[2,5,7,8],[3,4,7,8],[3,5,6,8],[1,3,5,7]])
            if H > 1:
                break
        A = abs(A)
        self.zadanie = super().prepis(r'\sqrt[A]{\left(\cfrac{x^{'+super().texRiesZlomCisla(B,C)[1:-1]+r'}\;x^{'+super().texRiesZlomCisla(D,E)[1:-1]+r'}}{x^{'+super().texRiesZlomCisla(F,G)[1:-1]+r'}}\right)^{H}}',[A,B,C,D,E,F,G,H])
        self.riesenie = r'$x^{'+super().texRiesZlomCisla((B*E*G+C*D*G-C*E*F)*H, C*E*G*A)[1:-1]+r'}$'
        self.neriesenie = r'$x^{'+super().texRiesZlomCisla((B*E*G-C*D*G-C*E*F)*H, C*E*G*A)[1:-1]+r'}$'



class P52(Zadanie):     # odmocnina simple
    def __init__(self):
        super().__init__(fontsize=r'\footnotesize')
        A,B,C = super().zvolKoef(3, [[]])
        A = 1 ; B = abs(B)
        self.zadanie = super().prepis(r'\big(A\sqrt{Bx+BCy}+\sqrt{Bx-BCy}\big)^2-\big(A\sqrt{Bx+BCy}-\sqrt{Bx-BCy}\big)^2',[A,B,C])
        Z = abs(B) ; Y = C**2 ; X = 4*A*Z
        self.riesenie = super().prepis(r'X\sqrt{x^2-Yy^2}',[X,Y],koefStr=['X','Y'])
        if C == Y and B == Z:
            X = 2*A*Z
        self.neriesenie = super().prepis(r'X\sqrt{x^2-Cy^2}',[X,C],koefStr=['X','C'])
        


# LIMITY


class P53(Zadanie):     # odmocnina "hard"
    def __init__(self):
        super().__init__(maxnum=5)
        while True:
            A,B = super().zvolKoef(2, [[]])
            if B > A and A > 1:
                break
        C = choice([A,B,A*B,A*A,B*B,-A,-B,-A*B,-A*A,-B*B])
        D = choice([A,B,A*B,A*A,B*B,-A,-B,-A*B,-A*A,-B*B])
        E = choice([A,B,A*B,A*A,B*B,-A,-B,-A*B,-A*A,-B*B])
        F = choice([A,B,A*B,A*A,B*B,-A,-B,-A*B,-A*A,-B*B])
        G = choice([2,1,0-1,-2])
        H = choice([2,1,0-1,-2])
        I = choice([2,1,0-1,-2])
        J = choice([2,1,0-1,-2])
        self.zadanie = super().prepis(r'\lim\limits_{n\to\infty}\cfrac{C\cdot A^{n+G}+D\cdot B^{n+H}}{E\cdot B^{n+I}+F\cdot A^{n+J}}',[A,B,C,D,E,F,G,H,I,J])
        rozdiel = H - I
        if rozdiel > 0:
            self.riesenie = super().texRiesZlomCisla(D*B**rozdiel, E)
            self.neriesenie = super().texRiesZlomCisla(D, E*B)
        elif rozdiel == 0:
            self.riesenie = super().texRiesZlomCisla(D, E)
            self.neriesenie = super().texRiesZlomCisla(D ,E*A)
        elif rozdiel < 0:
            self.riesenie = super().texRiesZlomCisla(D, E*B**(-rozdiel))
            self.neriesenie = super().texRiesZlomCisla(D*B, E)



class P54(Zadanie):     # logaritmus simple
    def __init__(self):
        super().__init__()
        while True:
            A,B,C,D,E,F,G,H = super().zvolKoef(8, [[]])
            if A > 1 and abs(B) != abs(F):
                break
        B = abs(B) ; F = abs(F)
        self.zadanie = r'$\lim\limits_{n\to\infty}'+str(A)+r'n\cfrac{\sqrt{'+super().texRiesPoly([D,C,B*B],premenna='n')[1:-1]+r'}-\sqrt{'+super().texRiesPoly([E,0,B*B],premenna='n')[1:-1]+r'}}{\sqrt{'+super().texRiesPoly([H,G,F*F],premenna='n')[1:-1]+r'}}$'
        self.riesenie = super().texRiesZlomCisla(A*C, 2*B*F)
        self.neriesenie = super().texRiesZlomCisla(A*C, B*F)
        





            


# GENERACIA

def prikladyLoad():
    return [P41(), P42(), P43(), P44(), blank(), blank()]

filewrite('odmoclim.tex','Odmocniny a limity', prikladyLoad,
          r'V \textbf{(a)} a \textbf{(b)} \textbf{uprav výrazy}, v \textbf{(c)} a \textbf{(d)} \textbf{vypočítaj limity}.\\Pokud se výsledky shodujú s tými za otazníky, tak napravo obarvi\\příslušející kroužek načerno. \textbf{Spolu odevzdejte výsledné slovo}.',
          prikladyFontsize=r'\normalsize', rieseniaFontsize=r'\footnotesize', tabulkyBraille=False, minimalistic=False)
