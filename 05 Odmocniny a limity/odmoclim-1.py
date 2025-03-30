import os, sys
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from zadanie import *





# LIMITY


class P5a1(Zadanie):   
    def __init__(self):
        super().__init__()
        A,B,C,D = super().zvolKoef(4, [[]])
        self.zadanie = super().prepis(r'\lim\limits_{n\to\infty}\cfrac{A+Bn}{C+Dn}',[A,B,C,D])
        self.riesenie = super().texRiesZlomCisla(B,D)
        neriesenia = [r'$\infty$',r'$0$']
        if super().texRiesZlomCisla(A,C) != super().texRiesZlomCisla(B,D):
            neriesenia.append(super().texRiesZlomCisla(A,C))
        self.neriesenie = choice(neriesenia)


class P5a2(Zadanie):   
    def __init__(self):
        super().__init__()
        A,B,C,D,E = super().zvolKoef(5, [[]])
        self.zadanie = super().prepis(r'\lim\limits_{n\to\infty}\cfrac{A(B+Cn)}{(Dn+E)^2}',[A,B,C,D,E])
        self.riesenie = r'$0$'
        neriesenia = [r'$\infty$',r'$-\infty$',super().texRiesZlomCisla(C,D), super().texRiesZlomCisla(C,2*D*E), str(A)]
        self.neriesenie = choice(neriesenia)


class P5a3(Zadanie):
    def __init__(self):
        super().__init__()
        A,B,C,D = super().zvolKoef(4, [[]])
        self.zadanie = super().prepis(r'\lim\limits_{n\to\infty}\cfrac{(A+Bn)^2}{n^2+Cn+D}',[A,B,C,D])
        self.riesenie = r'$'+str(B*B)+r'$'
        neriesenia = [r'$\infty$',r'$-\infty$',r'$0$',super().texRiesZlomCisla(B,C)]
        if A != D*B*B:
            neriesenia.append(super().texRiesZlomCisla(A,D))
        self.neriesenie = choice(neriesenia)




class P5a4(Zadanie):
    def __init__(self):
        super().__init__(maxnum=5)
        while True:
            A,B,C = super().zvolKoef(3, [[]])
            if A > 1 and abs(C-B) < 5:
                break
        self.zadanie = super().prepis(r'\lim\limits_{n\to\infty}\cfrac{A^{n+B}}{A^{n+C}}', [A,B,C])
        if B > C:
            self.riesenie = r'$'+str(A**(B-C))+r'$'
            neriesenia = [r'$\infty$',r'$-\infty$',r'$0$',super().texRiesZlomCisla(1,A**(B-C)),r'$'+str(A**(B))+r'$']
        elif B < C:
            self.riesenie = super().texRiesZlomCisla(1,A**(C-B))
            neriesenia = [r'$\infty$',r'$-\infty$',r'$0$',r'$'+str(A**(C-B))+r'$',r'$'+str(A**(B))+r'$']
        else:
            self.riesenie = r'$1$'
            neriesenia = [r'$\infty$',r'$-\infty$',r'$0$',r'$'+str(A**(B))+r'$']
        self.neriesenie = choice(neriesenia)


class P5a5(Zadanie):
    def __init__(self):
        super().__init__(maxnum=5)
        while True:
            A,B,C,D,E,F = super().zvolKoef(6, [[]])
            if A > 0 and B > 1 and A != B and abs(E) > 1 and abs(F) > 1:
                break
        self.zadanie = super().prepis(r'\lim\limits_{n\to\infty}\cfrac{\left(\frac{A}{B}\right)^n +C}{Dn^{EF}}', [A,B,C,D,E,F])
        if A > B:
            if D > 0:
                self.riesenie = r'$\infty$'
                neriesenia = [r'$-\infty$',r'$0$',super().texRiesZlomCisla(C,D),r'$'+str(E*F)+r'$']
            else:
                self.riesenie = r'$-\infty$'
                neriesenia = [r'$\infty$',r'$0$',super().texRiesZlomCisla(C,D),r'$'+str(E*F)+r'$']
        else:
            if E*F > 0:
                self.riesenie = r'$0$'
                neriesenia = [r'$-\infty$',super().texRiesZlomCisla(C,D),r'$'+str(E*F)+r'$']
            else:
                if C*D > 0:
                    self.riesenie = r'$\infty$'
                    neriesenia = [r'$-\infty$',r'$0$',super().texRiesZlomCisla(C,D),r'$'+str(E*F)+r'$']
                else:
                    self.riesenie = r'$-\infty$'
                    neriesenia = [r'$\infty$',r'$0$',super().texRiesZlomCisla(C,D),r'$'+str(E*F)+r'$']
                
        self.neriesenie = choice(neriesenia)

    

class P5a6(Zadanie):   
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






# GENERACIA

def prikladyLoad():
    return [P5a1(), P5a2(), P5a3(), P5a4(), P5a5(), P5a6()]

filewrite('odmoclim-1.tex','Limity', prikladyLoad,
          r'\textbf{Vypočti limity}. Pokud se výsledky shodujú s tými za otazníky, tak napravo\\obarvi příslušející kroužek načerno. \textbf{Spolu odevzdejte výsledné slovo}.',
          prikladyFontsize=r'\normalsize', rieseniaFontsize=r'\small', tabulkyBraille=False, minimalistic=False)
