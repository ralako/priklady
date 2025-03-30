import os, sys
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from zadanie import *




class kubic(Zadanie):  # kubická rovnica
    def __init__(self):
        super().__init__()
        while True:
            A,B,C,D,E,F,G = super().zvolKoef(7, [[1,2,4,7],[1,2,5,7],[1,3,4,7],[1,3,5,7]], limit=60)
            F = 1
            B = 1 ; D = 1       
            if (B*D*G + B*E*F + C*D*F != 0) or (B*E*G + C*D*G + C*E*F != 0):
                break
        self.koeficienty = [A*C*E*G, A*B*E*G + A*C*D*G + A*C*E*F, A*B*D*G + A*B*E*F + A*C*D*F, A*B*D*F]
        self.riesenie = set([-C,-E,-G])
        self.neriesenie = set([-C,-E+choice([-2,-1,1,2]),G])




# DEFINICNE OBORY

class P41(Zadanie):     # zlomok simple
    def __init__(self):
        super().__init__()
        A,B,C,D = super().zvolKoef(4, [[]])
        self.zadanie = r'$f(x)='+super().texRiesZlom([B,A],[D,C])[1:]
        self.riesenie = super().texIntervalR([super().texRiesZlomCisla(-D,C)])
        self.neriesenie = super().texIntervalR([super().texRiesZlomCisla(D,C)])


class P42(Zadanie):     # zlomok kubic
    def __init__(self):
        super().__init__()
        menovatel = kubic()
        self.zadanie = r'$f(x)='+super().texRiesZlom([1],menovatel.koeficienty)[1:]
        self.riesenie = super().texIntervalR(menovatel.riesenie)
        self.neriesenie = super().texIntervalR(menovatel.neriesenie)


class P43(Zadanie):     # odmocnina simple
    def __init__(self):
        super().__init__()
        A,B,C = super().zvolKoef(3, [[]])
        self.zadanie = r'$f(x)='+super().prepis(r'A\sqrt{Bx+C}',[A,B,C])[1:]
        if B > 0:
            self.riesenie = r'$x\geq'+super().texRiesZlomCisla(-C,B)[1:]
            if choice([True,False]):            
                self.neriesenie = r'$x\leq'+super().texRiesZlomCisla(-C,B)[1:]
            else:
                self.neriesenie = r'$x\geq'+super().texRiesZlomCisla(C,B)[1:]
        else:
            self.riesenie = r'$x\leq'+super().texRiesZlomCisla(-C,B)[1:]
            if choice([True,False]):
                self.neriesenie = r'$x\geq'+super().texRiesZlomCisla(-C,B)[1:]
            else:
                self.neriesenie = r'$x\leq'+super().texRiesZlomCisla(C,B)[1:]



class P44(Zadanie):     # odmocnina "hard"
    def __init__(self):
        super().__init__()
        A, = super().zvolKoef(1, [[]])
        self.zadanie = r'$f(x)='+super().prepis(r'\sqrt{-x^2-Ax}',[A])[1:]
        if A > 0:
            self.riesenie = super().texInterval([[-A,0]],[[True,True]])
            if choice([True,False]):            
                self.neriesenie = super().texInterval([[0,A]],[[True,True]])
            else:
                self.neriesenie = super().texInterval([[-A,0]],[[False,False]])
        else:
            self.riesenie = super().texInterval([[0,-A]],[[True,True]])
            if choice([True,False]):            
                self.neriesenie = super().texInterval([[A,0]],[[True,True]])
            else:
                self.neriesenie = super().texInterval([[0,-A]],[[False,False]])



class P45(Zadanie):     # logaritmus simple
    def __init__(self):
        super().__init__()
        A,B,C = super().zvolKoef(3,[[]])
        self.zadanie = r'$f(x)='+super().prepis(r'A\ln{(Bx+C)}',[A,B,C])[1:]
        if B > 0:
            self.riesenie = r'$x>'+super().texRiesZlomCisla(-C,B)[1:]
            if choice([True,False]):            
                self.neriesenie = r'$x<'+super().texRiesZlomCisla(-C,B)[1:]
            else:
                self.neriesenie = r'$x>'+super().texRiesZlomCisla(C,B)[1:]
        else:
            self.riesenie = r'$x<'+super().texRiesZlomCisla(-C,B)[1:]
            if choice([True,False]):
                self.neriesenie = r'$x>'+super().texRiesZlomCisla(-C,B)[1:]
            else:
                self.neriesenie = r'$x<'+super().texRiesZlomCisla(C,B)[1:]



class P46(Zadanie):     # logaritmus "hard"
    def __init__(self):
        super().__init__()
        A,B = super().zvolKoef(2,[[]])
        self.zadanie = r'$f(x)=\ln{(' + super().texRiesPoly([A*B,-(A+B),1])[1:-1] + r')}$'
        if A > B:
            self.riesenie = super().texInterval([['-inf',B],[A,'inf']],[[False,False],[False,False]])
            self.neriesenie = super().texInterval([[B,A]],[[False,False]])
        else:
            self.riesenie = super().texInterval([['-inf',A],[B,'inf']],[[False,False],[False,False]])
            self.neriesenie = super().texInterval([[A,B]],[[False,False]])


            


# GENERACIA

def prikladyLoad():
    return [P41(), P42(), P43(), P44(), P45(), P46()]

filewrite('definic.tex','Definiční obor', prikladyLoad,
          r'\textbf{Zjisti definiční obor} zadaných funkcí. Pokud se shoduje s tím za otazníky,\\tak napravo obarvi příslušející kroužek načerno. \textbf{Spolu odevzdejte výsledné slovo}.',
          prikladyFontsize=r'\normalsizerrr', rieseniaFontsize=r'\footnotesize', tabulkyBraille=False,minimalistic=False,tightLayoutRies=-1)
