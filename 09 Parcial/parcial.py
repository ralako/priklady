import os, sys
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from zadanie import *
from random import choice, randint



# VOLNY EXTREM, PARCIALNE DERIVACIE


class P9(Zadanie):
    def __init__(self):
        super().__init__(maxnum=8)
        while True:
            A,B,C,D,E,F,G,H,I = super().zvolKoef(9, [[5,7,7,7],[5,7,7,2],[5,7,2,2],[5,2,2,2],[6,8,8,8],[6,8,8,4],[6,8,4,4],[6,4,4,4]], limit=50)
            if E < 5 and F < 6 and 2*G-B != 0 and 2*H-D != 0 and 2*G-B != B and 2*H-D != D:
                break
        self.konstanty = [A,B,C,D,E,F,G,H,I]
        self.riesenia = [[2*G-B,2*H-D],[2*G-B,D],[B,2*H-D],[B,D]]
    def funkcia(self,xy):
        x = xy[0] ; y = xy[1]
        A,B,C,D,E,F,G,H,I = self.konstanty
        xcast = E*x*x*x - 3*E*G*x*x + 3*E*(2*G-B)*B*x
        ycast = F*y*y*y - 3*F*H*y*y + 3*F*(2*H-D)*D*y
        return (xcast + ycast + I)
    def fstring(self):
        A,B,C,D,E,F,G,H,I = self.konstanty
        xcastString = super().prepis(r'Ex^3-'+str(3*E*G)+r'x^2+'+str(3*E*(2*G-B)*B)+r'x', self.konstanty)
        ycastString = super().prepis(str(3*F*(2*H-D)*D)+r'y-'+str(3*F*H)+r'y^2+Fy^3', self.konstanty)
        string = super().check(xcastString[:-1] + r'+' + str(I) + r'+' + ycastString[1:])
        #print(string)
        #print(self.riesenia)
        return string
    def dfdx(self):
        A,B,C,D,E,F,G,H,I = self.konstanty
        string = super().texRiesPoly([3*E*(2*G-B)*B, -3*E*2*G, 3*E], premenna='x')
        return string
    def dfdxChyba(self):
        A,B,C,D,E,F,G,H,I = self.konstanty
        string = super().texRiesPoly([3*E*(2*G-B)*B, -3*E*G, 3*E], premenna='x')
        return string
    def dfdy(self):
        A,B,C,D,E,F,G,H,I = self.konstanty
        string = super().texRiesPoly([3*F*(2*H-D)*D, -3*F*2*H, 3*F], premenna='y')
        return string
    def dfdyChyba(self):
        A,B,C,D,E,F,G,H,I = self.konstanty
        string = super().texRiesPoly([3*F*(H-D)*D, -3*F*2*H, 3*F], premenna='y')
        return string
        
    

    
class P91(Zadanie):     # Je v bode rastuca
    def __init__(self):
        super().__init__()
        global prikl
        prikl = P9()
        self.zadanie = r'$f(x,y)='+prikl.fstring()[1:-1]+r'$'
        self.riesenie = 'vybarvi'
        self.neriesenie = 'nebarvi'



class P92(Zadanie):
    def __init__(self):
        super().__init__()
        global prikl
        self.zadanie = r'Najdi parciální derivaci podle $x$, $\pdv{f}{x}=$'
        self.riesenie = prikl.dfdx()
        self.neriesenie = prikl.dfdxChyba()
        #print(self.riesenie)

class P93(Zadanie):
    def __init__(self):
        super().__init__()
        global prikl
        self.zadanie = r'Najdi stacionární body v $x$'
        self.riesenie = r'$x_1+x_2='+str(prikl.riesenia[0][0]+prikl.riesenia[2][0])+r'$'
        self.neriesenie = r'$x_1+x_2='+str(prikl.riesenia[0][0]+prikl.riesenia[2][0]+1)+r'$'
        #print(self.riesenie)



class P94(Zadanie):
    def __init__(self):
        super().__init__()
        global prikl
        self.zadanie = r'Najdi parciální derivaci podle $y$, $\pdv{f}{y}=$'
        self.riesenie = prikl.dfdy()
        self.neriesenie = prikl.dfdyChyba()
        #print(self.riesenie)

class P95(Zadanie):
    def __init__(self):
        super().__init__()
        global prikl
        self.zadanie = r'Najdi stacionární body v $y$'
        self.riesenie = r'$y_1+y_2='+str(prikl.riesenia[0][1]+prikl.riesenia[1][1])+r'$'
        self.neriesenie = r'$y_1+y_2='+str(prikl.riesenia[0][1]+prikl.riesenia[1][1]+1)+r'$'
        #print(self.riesenie)



class P96(Zadanie):
    def __init__(self):
        super().__init__()
        global prikl
        self.zadanie = r'Najdi funkční hodnoty vo všech stacionárních bodech \\ \phantom{xxxxxx} a vyber tu najvětší. $f_{\text{max}}(x,y)=$'
        stac1 = prikl.funkcia(prikl.riesenia[0])
        stac2 = prikl.funkcia(prikl.riesenia[1])
        stac3 = prikl.funkcia(prikl.riesenia[2])
        stac4 = prikl.funkcia(prikl.riesenia[3])
        stac = [stac1,stac2,stac3,stac4]
        maxstac = -10000
        maxindex = 0
        for i in range(4):
            if stac[i] > maxstac:
                maxstac = stac[i]
                maxindex = i
        chybneMaxstac = stac[(maxindex+1)%4]
        if chybneMaxstac == maxstac:
            chybneMaxstac = stac[(maxindex+2)%4]
            if chybneMaxstac == maxstac:
                chybneMaxstac = stac[(maxindex+3)%4]
                if chybneMaxstac == maxstac:
                    while True:
                        chybneMaxstac = randint(-100,100)
                        if chybneMaxstac != maxtac:
                            break
        self.riesenie = r'$'+str(maxstac)+r'$'
        self.neriesenie = r'$'+str(chybneMaxstac)+r'$'




            
# GENERACIA


def prikladyLoad():
    return [P91(), P92(), P93(), P94(), P95(), P96()]



filewrite('parcial.tex','Volné extrémy', prikladyLoad,
          r'Cílem je najít \textbf{volné extrémy} funkce $f(x,y)$ zadané v \textbf{(a)}.\\Postupuj podle krokú v \textbf{(b)} až \textbf{(f)}. Pokud se medzivýsledky shodujú s těmi za otazníky,\\tak napravo obarvi příslušející kroužek načerno. \textbf{Spolu odevzdejte výsledné slovo}.',
          prikladyFontsize=r'\normalsize', rieseniaFontsize=r'\footnotesize', tabulkyBraille=False, minimalistic=False, nicefracSolution=False, tightLayout=False)
