import os, sys
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from zadanie import *



# TECNY

class P71(Zadanie):     # sklon z bodu, zlomok
    def __init__(self):
        super().__init__()
        while True:
            A,B,C,D,E = super().zvolKoef(5, [[3,3,5,5],[3,4,5],[1,3,5,5],[2,3,5]])
            if C*E != -D:
                break
        self.zadanie = r'$f(x)=' + super().texRiesZlom([B,A], [D,C])[1:-1] + r'\enspace , \enspace x_0='+str(E)+r'$'
        self.riesenie = super().check(r'$y = ' + super().texRiesZlomCisla(A*D-C*B, (C*E+D)**2, nicefrac=False, popZnamienko=True)[1:-1] + r'x+' + super().texRiesZlomCisla(A*C*E*E + 2*B*C*E + B*D, (C*E+D)**2, nicefrac=False, popZnamienko=True)[1:])
        self.neriesenie = super().check(r'$y = ' + super().texRiesZlomCisla(A*D-C*B, (C*E+D)**2, nicefrac=False, popZnamienko=True)[1:-1] + r'x+' + super().texRiesZlomCisla(A*C*E*E - 2*B*C*E + B*D, (C*E+D)**2, nicefrac=False, popZnamienko=True)[1:])



class P72(Zadanie):     # sklon z bodu, odmocnina
    def __init__(self):
        super().__init__()    
        A,B,C,D = super().zvolKoef(4, [[1,2,4]])
        D = abs(D)
        E = super().texRiesZlomCisla(D*D-C, B, nicefrac=False, popZnamienko=True)
        self.zadanie = r'$f(x)=' + super().prepis(r'A\sqrt{Bx+C}', [A,B,C])[1:-1] + r'\enspace , \enspace x_0='+str(E)[1:]
        self.riesenie = super().check(r'$y = ' + super().texRiesZlomCisla(A*B, 2*D, nicefrac=False, popZnamienko=True)[1:-1] + r'x+' + super().texRiesZlomCisla(A*(D*D+C), 2*D, nicefrac=False, popZnamienko=True)[1:])
        self.neriesenie = super().check(r'$y = ' + super().texRiesZlomCisla(A*B, 2*D, nicefrac=False, popZnamienko=True)[1:-1] + r'x+' + super().texRiesZlomCisla(A*(D*D+C), D, nicefrac=False, popZnamienko=True)[1:])



class P73(Zadanie):     # bod zo sklonu, kvadra
    def __init__(self):
        super().__init__()
        A,B,C,D = super().zvolKoef(4, [[]])
        self.zadanie = r'$f(x)=' + super().texRiesPoly([C,B,A])[1:-1] + r'\enspace , \enspace k='+str(D)+r'$'
        self.riesenie = super().texRiesZlomCisla(D*D-B*B+4*A*C, 4*A, nicefrac=False, popZnamienko=True)
        self.neriesenie = super().texRiesZlomCisla(D*D-B*B-4*A*C, 4*A, nicefrac=False, popZnamienko=True)
        


class P74(Zadanie):     # bod zo sklonu, kubic  # PROBLEM
    def __init__(self):
        super().__init__(maxnum=6)
        while True:
            A,B,C,D,E,F,G,H = super().zvolKoef(8, [[6,2,2,2],[6,7,2,2],[6,7,7,7],[6,7,7,2]],limit=40)
            if F > 0 and G-B > 0 and 2*G-B != 0 and A*B*C+H != 0:
                break
        A = 3*F
        C = 2*G-B
        D = A*B*C+H
        self.zadanie = r'$f(x)=' + super().texRiesPoly([E,D,-A*G,F])[1:-1] + r'\enspace , \enspace k='+str(H)+r'$'
        self.riesenie = r'$' + str(F*B*B*B - A*G*B*B + D*B + E) + r' , ' + str(F*C*C*C - A*G*C*C + D*C + E) + r'$'
        self.neriesenie = r'$' + str(F*B*B*B - A*G*B*B + D*B + E) + r' , ' + str(F*C*C*C - A*G*C*C - D*C + E) + r'$'
        





            


# GENERACIA

def prikladyLoad():
    return [P71(), P72(), P73(), P74(), blank(), blank()]

filewrite('dotycnica.tex','Tečna funkce', prikladyLoad,
          r'V \textbf{(a)} a \textbf{(b)} urči \text{rovnicu tečny} $y = kx + q$ ku funkci $f(x)$ v bode $x_0$.\\V \textbf{(c)} a \textbf{(d)} urči ypsilonové souřadnice bodů, ve kterých je sklon $f(x)$ rovný $k$.\\Pokud se výsledky shodujú s těmi za otazníky, tak napravo obarvi\\příslušející kroužek načerno. \textbf{Spolu odevzdejte výsledné slovo}.',
          prikladyFontsize=r'\small', rieseniaFontsize=r'\small', tabulkyBraille=False, minimalistic=False, nicefracSolution=True)
