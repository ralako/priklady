import os, sys
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from zadanie import *

class P11(Zadanie):
    def __init__(self):
        super().__init__()
        A,B,C,D,E,F = super().zvolKoef(6, [[1,2],[1,3],[4,5],[4,6]])
        self.zadanie = super().check(r'$'+str(A)+'('+str(B)+'x+'+str(C)+')+'+str(D)+'('+str(E)+'+'+str(F)+r'x)$')
        self.absolutny = A*C + D*E
        self.linearny = A*B + D*F
        self.riesenie = super().texRiesPoly([self.absolutny, self.linearny])
        self.neriesenie = super().texRiesPoly([self.absolutny*choice([-1,0]), self.linearny])

class P12(Zadanie):
    def __init__(self):
        super().__init__()
        A,B,C,D,E,F,G,H = super().zvolKoef(8, [[1,2,4],[1,2,5],[1,3,4],[1,3,5],[6,7],[6,8]])
        self.zadanie = super().check(r'$'+str(A)+'('+str(B)+'+'+str(C)+'x)('+str(D)+'x+'+str(E)+')-'+str(F)+'('+str(G)+'+'+str(H)+r'x)$')
        self.absolutny = A*B*E - F*G
        self.linearny = A*B*D + A*C*E - F*H
        self.kvadraticky = A*C*D
        self.riesenie = super().texRiesPoly([self.absolutny, self.linearny, self.kvadraticky])
        if self.linearny == 0:
            self.neriesenie = super().texRiesPoly([self.absolutny*choice([-1,1,0]), self.linearny+2, self.kvadraticky])
        else:
            self.neriesenie = super().texRiesPoly([self.absolutny*choice([-1,1,0]), self.linearny*(-1), self.kvadraticky])

class P13(Zadanie):
    def __init__(self):
        super().__init__()
        A,B,C,D = super().zvolKoef(4, [[1,1,1],[1,1,2],[1,2,2],[2,2,2],[3,3],[3,4],[4,4]])
        self.zadanie = super().prepis(r'(Ax+B)^3-(Cx+D)^2',[A,B,C,D])
        self.absolutny = B*B*B - D*D
        self.linearny = 3*A*B*B - 2*C*D
        self.kvadraticky = 3*A*A*B - C*C
        self.kubicky = A*A*A
        self.riesenie = super().texRiesPoly([self.absolutny, self.linearny, self.kvadraticky, self.kubicky])
        self.neriesenie = super().texRiesPoly([self.absolutny, self.linearny*choice([1,0]), self.kvadraticky*choice([-1,1]), self.kubicky*(-1)])


class P14(Zadanie):
    def __init__(self):
        super().__init__()
        A,B,C,D,E,F,G = super().zvolKoef(7, [[1,7],[2,7],[3,4,5],[3,4,6]])
        self.zadanie = super().prepis(r'\cfrac{Ax+B}{C}+D\cfrac{E+Fx}{G}',[A,B,C,D,E,F,G])
        self.absolutnyCit = B*G + C*D*E
        self.linearnyCit = A*G + C*D*F
        self.absolutnyMen = C*G
        self.riesenie = super().texRiesZlom([self.absolutnyCit,self.linearnyCit],
                                            [self.absolutnyMen])
        self.neriesenie = super().texRiesZlom([self.absolutnyCit,self.linearnyCit*choice([-1,1,0])],
                                              [self.absolutnyMen*(-1)])


class P15(Zadanie):
    def __init__(self):
        super().__init__()
        while True:
            A,B,C,D,E,F = super().zvolKoef(6, [[1,4,6],[2,3,4,6],[2,4,5],[2,6]])
            if F + D*E != 0:
                break
        self.zadanie = super().prepis(r'\cfrac{\frac{A}{B}-\frac{C}{x}}{\frac{1}{D}+\frac{E}{F}}',[A,B,C,D,E,F])
        absoCit = (-1)*B*C*D*F ; lineCit = A*D*F
        absoMen = 0 ; lineMen = B * (F + D*E)
        self.riesenie = super().texRiesZlom([absoCit,lineCit],[absoMen,lineMen])
        drb1 = choice([-3,-2,-1,1,2,3]) ; drb2 = choice([-3,-2,-1,1,2,3])
        self.neriesenie = super().texRiesZlom([absoCit+drb1,lineCit+drb2],[absoMen,lineMen])


class P16(Zadanie):
    def __init__(self):
        super().__init__()
        A,B,C,D,E,F = super().zvolKoef(6, [[1,1],[1,2],[2,2],[4,6],[5,6]])
        self.zadanie = super().prepis(r'\cfrac{(A+Bx)^2+C}{(Dx+E)\cdot\frac{F}{x}}',[A,B,C,D,E,F])
        absoCit = 0 ; lineCit = A*A + C ; kvadCit = 2*A*B ; kubiCit = B*B
        absoMen = E*F ; lineMen = D*F
        self.riesenie = super().texRiesZlom([absoCit,lineCit,kvadCit,kubiCit],[absoMen,lineMen])
        self.neriesenie = super().texRiesZlom([absoCit,lineCit*(-1),kvadCit,kubiCit],[absoMen,lineMen*(-1)])




def prikladyLoad():
    return [P11(),P12(),P13(),P14(),P15(),P16()]

filewrite('zatvorky.tex','Závorky a zlomky',
          r'\textbf{Uprav výrazy (a) až (f)}. Pokud je výraz za otazníky roven výrazu pred otázniky, tak napravo obarvi príslušející kroužek. \textbf{Spolu odevzdejte výsledné slovo.}')
