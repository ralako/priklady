import os, sys
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from zadanie import *



# TECNY

class P81(Zadanie):     # Je v bode rastuca
    def __init__(self):
        super().__init__()
        while True:
            A,B,C,D,E,F = super().zvolKoef(6, [[1,4,6,6],[1,5,6]])
            if D*F != -E:
                break
        self.zadanie = r'$f(x)=' + super().texRiesZlom([C,B,A], [E,D])[1:-1] + r'\enspace , \enspace x_0='+str(F)+r'$'
        citatelDer = A*D*F*F + 2*A*E*F + B*E - C*D
        #print(self.zadanie, citatelDer)
        if citatelDer > 0:
            self.riesenie = r'\text{ano}'
            self.neriesenie = r'\text{ne}'
        else:
            self.riesenie = r'\text{ne}'
            self.neriesenie = r'\text{ano}'



class P82(Zadanie):     # Je v bode konvexná
    def __init__(self):
        super().__init__()
        A,B,C,D,E,F = super().zvolKoef(6, [[1,6,6,6],[2,6,6]])
        self.zadanie = r'$f(x)=' + super().texRiesPoly([E,D,C,B,A])[1:-1] + r'\enspace , \enspace x_0='+str(F)+r'$'
        Der = 12*A*F*F + 6*B*F + 2*C
        if Der > 0:
            self.riesenie = r'\text{ano}'
            self.neriesenie = r'\text{ne}'
        else:
            self.riesenie = r'\text{ne}'
            self.neriesenie = r'\text{ano}'


class P83(Zadanie):     # Sucet stac a inflex
    def __init__(self):
        super().__init__()
        A,B = super().zvolKoef(2, [[]])
        self.zadanie = r'$f(x)=' + super().prepis(r'Axe^{Bx}',[A,B])[1:]
        self.riesenie = super().texRiesZlomCisla(-3,B)
        self.neriesenie = super().texRiesZlomCisla(1,B)
        


class P84(Zadanie):     # stac max min
    def __init__(self):
        super().__init__(maxnum=6)
        while True:
            A,B,C = super().zvolKoef(3, [[]])
            if A > 0 and (B*B - 4*A*C) < 0:
                break
        self.zadanie = r'$f(x)=' + super().prepis(r'\sqrt{Ax^2+Bx+C}',[A,B,C])[1:]
        DDerCit = 4*A*C - B*B
        if DDerCit < 0:
            self.riesenie = super().texRiesZlomCisla(-B,2*A)[:-1] + r'\enspace , \enspace \mathrm{lomax}$'
            self.neriesenie = super().texRiesZlomCisla(-B,2*A)[:-1] + r'\enspace , \enspace '+choice([r'\mathrm{lomin}$',r'\mathrm{lomin}$',r'\mathrm{lomin}$',r'\mathrm{lomin}$',r'\mathrm{lomin}$',r'\mathrm{inflex}$'])
        elif DDerCit > 0:
            self.riesenie = super().texRiesZlomCisla(-B,2*A)[:-1] + r'\enspace , \enspace \mathrm{lomin}$'
            self.neriesenie = super().texRiesZlomCisla(-B,2*A)[:-1] + r'\enspace , \enspace'+choice([r'\mathrm{lomax}$',r'\mathrm{lomax}$',r'\mathrm{lomax}$',r'\mathrm{lomax}$',r'\mathrm{lomax}$',r'\mathrm{inflex}$'])
        else:
            self.riesenie = super().texRiesZlomCisla(-B,2*A)[:-1] + r'\enspace , \enspace \mathrm{sedlo}$'
            self.neriesenie = super().texRiesZlomCisla(-B,2*A)[:-1] + r'\enspace , \enspace'+choice(['\mathrm{lomax}$',r'\mathrm{inflex}$'])





            
# GENERACIA

def prikladyLoad():
    return [P81(), P82(), P83(), P84(), blank(), blank()]

filewrite('stacinflex.tex','Stacionární body', prikladyLoad,
          r'{\small V \textbf{(a)} zjisti jestli $f(x)$ \textbf{roste} v bode $x_0$. V \textbf{(b)} zjisti jestli je $f(x)$ v bode $x_0$ \textbf{ryze konvexní}.\\V \textbf{(c)} spočti \textbf{součet} x-ových souřadnic stacionárního a inflexního bodu. V \textbf{(d)} najdi x-ovou souřadnici stacionárního bodu a rozhodli jestli to je \textbf{lomax, lomin či inflex}.\\Pokud se výsledky shodujú s těmi za otazníky, tak napravo obarvi příslušející kroužek načerno.\\\textbf{Spolu odevzdejte výsledné slovo}}.',
          prikladyFontsize=r'\normalsize', rieseniaFontsize=r'\small', tabulkyBraille=False, minimalistic=False, nicefracSolution=False, tightLayout=False)
