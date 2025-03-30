import os, sys
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from zadanie import *



# DERIVÁCIE

class P61(Zadanie):     # polynóm
    def __init__(self):
        super().__init__()
        A,B,C,D,E = super().zvolKoef(5, [[]])
        self.zadanie = super().texRiesPoly([E,D,C,B,A])
        self.riesenie = super().texRiesPoly([D,2*C,3*B,4*A])
        self.neriesenie = super().texRiesPoly([D,C,B,A])



class P62(Zadanie):     # zlomok (kvadraticka/linearna)
    def __init__(self):
        super().__init__(maxnum=7)
        A,B,C,D,E = super().zvolKoef(5, [[]])
        self.zadanie = super().texRiesZlom([C,B,A],[E,D])
        self.riesenie = super().texRiesZlom([B*E-C*D, 2*A*E, A*D], [E*E, 2*D*E, D*D])
        self.neriesenie = super().texRiesZlom([B*E-C*D, -2*A*E, A*D], [E*E, 2*D*E, D*D])



class P63(Zadanie):     # sucin 1/x a odmocniny z linearnej
    def __init__(self):
        super().__init__()
        A,B,C = super().zvolKoef(3, [[]])
        self.zadanie = super().prepis(r'\frac{A}{x}\sqrt{Bx+C}', [A,B,C])
        self.riesenie = super().prepis(r'\frac{'+str(-A*B)+r'x-'+str(2*A*C)+r'}{2x^2 \sqrt{\smash[b]{Bx+C}}}', [A,B,C])
        self.neriesenie = super().prepis(r'\frac{'+str(-A*B)+r'x-'+str(2*A*C)+r'}{x^2 \sqrt{\smash[b]{Bx+C}}}', [A,B,C])
        


class P64(Zadanie):     # exponenciala
    def __init__(self):
        super().__init__()
        A,B,C = super().zvolKoef(3, [[]])
        self.zadanie = super().prepis(r'e^{Ax^2+Bx+C}', [A,B,C])
        self.riesenie = super().prepis(r'('+str(2*A)+r'x+B)e^{Ax^2+Bx+C}', [A,B,C])
        self.neriesenie = super().prepis(r'e^{Ax^2+Bx+C}', [A,B,C])



class P65(Zadanie):     # logaritmus zo zlomku linearna/linearna
    def __init__(self):
        super().__init__()
        A,B,C,D = super().zvolKoef(4, [[]])
        self.zadanie = super().prepis(r'\ln{\left(\frac{Ax+B}{Cx+D}\right)}', [A,B,C,D])
        self.riesenie = super().prepis(r'\frac{A}{Ax+B}-\frac{C}{Cx+D}', [A,B,C,D])
        self.neriesenie = super().prepis(r'\frac{A}{Ax+B}+\frac{C}{Cx+D}', [A,B,C,D])



class P66(Zadanie):     # exponenciala/linearna
    def __init__(self):
        super().__init__()
        A,B,C,D = super().zvolKoef(4, [[]])
        self.zadanie = super().prepis(r'\frac{e^{Ax+B}}{Cx+D}', [A,B,C,D])
        self.riesenie = super().prepis(r'\frac{ACx+'+str(A*D-C)+r'}{(Cx+D)^2}e^{Ax+B}', [A,B,C,D])
        self.neriesenie = super().prepis(r'\frac{-ACx+'+str(A*D-C)+r'}{(Cx+D)^2}e^{Ax+B}', [A,B,C,D])



            


# GENERACIA

def prikladyLoad():
    return [P61(), P62(), P63(), P64(), P65(), P66()]

filewrite('derivacie.tex','Derivácie', prikladyLoad,
          r'\textbf{Vypočítej derivace.} Pokud se výsledky shodují s těmi za otazníky,\\tak napravo obarvi příslušející kroužek načerno. \textbf{Spolu odevzdejte výsledné slovo}.',
          prikladyFontsize=r'\normalsize', rieseniaFontsize=r'\tiny', tabulkyBraille=False, minimalistic=False, nicefracSolution=False, tightLayoutRies=3)
