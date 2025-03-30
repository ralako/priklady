import os, sys
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from zadanie import *
from random import choice, randint



# VOLNY EXTREM, PARCIALNE DERIVACIE

pytagoras = [[3,4,5],[5,12,13],[6,8,10],[10,24,26]]
counter = 0

class P10(Zadanie):
    def __init__(self):
        super().__init__(maxnum=8)
        global counter
        D,E = super().zvolKoef(2, [[]])
        A = pytagoras[counter%4][0]*choice([1,-1])
        B = pytagoras[counter%4][1]*choice([1,-1])
        C = pytagoras[counter%4][2]
        self.konstanty = [A,B,C,D]
        self.riesenia = [[-A,-B],[A,B]]
    def funkcia(self,xy):
        x = xy[0] ; y = xy[1]
        A,B,C,D = self.konstanty
        #print(x,y,A,B,D)
        return A*x + B*y + D
    def fstring(self):
        A,B,C,D = self.konstanty
        string = super().prepis(r'Ax+By+D ', [A,B,C,D])
        #print(string)
        #print(self.riesenia)
        return string
    def vstring(self):  # vazba
        A,B,C,D = self.konstanty
        string = super().prepis(r'x^2+y^2='+str(C*C), [A,B,C,D])
        return string
    def dLdx(self):
        A,B,C,D = self.konstanty
        string = super().prepis(r'A+2\lambda x', [A,B,C,D])
        return string
    def dLdxChyba(self):
        A,B,C,D = self.konstanty
        string = super().prepis(r'A+\lambda x', [A,B,C,D])
        return string
    def dLdy(self):
        A,B,C,D = self.konstanty
        string = super().prepis(r'B+2\lambda y', [A,B,C,D])
        return string
    def dLdyChyba(self):
        A,B,C,D = self.konstanty
        string = super().prepis(r'-B+2\lambda y', [A,B,C,D])
        return string
        
    

    
class P101(Zadanie):     # Je v bode rastuca
    def __init__(self):
        super().__init__()
        global prikl
        prikl = P10()
        self.zadanie = r'$f(x,y)='+prikl.fstring()[1:-1]+r'\enspace , \enspace \mathrm{vazba:} \enspace '+prikl.vstring()[1:]
        self.riesenie = 'vybarvi'
        self.neriesenie = 'nebarvi'
        global counter
        counter += 1



class P102(Zadanie):
    def __init__(self):
        super().__init__()
        global prikl
        self.zadanie = r'Sestav $L(\lambda,x,y)$ a spočti $\pdv{L}{x}=$'
        self.riesenie = prikl.dLdx()
        self.neriesenie = prikl.dLdxChyba()
        #print(self.riesenie)

class P103(Zadanie):
    def __init__(self):
        super().__init__()
        global prikl
        self.zadanie = r'Takisto spočti $\pdv{L}{y}=$'
        self.riesenie = prikl.dLdy()
        self.neriesenie = prikl.dLdyChyba()
        #print(self.riesenie)
        


class P104(Zadanie):
    def __init__(self):
        super().__init__()
        global prikl
        self.zadanie = r'Z podmínek $\pdv{L}{x}=0 , \pdv{L}{y}=0$ vyjádři $x,y$ v závislosti na $\lambda$.\\ \phantom{xxxxxx}Následne $x,y$ dosaď do vazbové rovnice\\ \phantom{xxxxxx}a vypočti dva výsledky pro $\lambda$.'
        self.riesenie = r'$\lambda_1+\lambda_2=0$'
        self.neriesenie = r'$\lambda_1+\lambda_2='+str(choice([-2,-1,1,2]))+r'$'
        #print(self.riesenie)

class P105(Zadanie):
    def __init__(self):
        super().__init__()
        global prikl
        self.zadanie = r'Pomocou $\lambda$ urč dvě dvojice pro $x,y$.'
        self.riesenie = r'$x_1 x_2 y_1 y_2='+str(prikl.riesenia[0][0]*prikl.riesenia[0][1]*prikl.riesenia[1][0]*prikl.riesenia[1][1])+r'$'
        self.neriesenie = r'$x_1 x_2 y_1 y_2='+str(-prikl.riesenia[0][0]*prikl.riesenia[1][0]*prikl.riesenia[1][1])+r'$'
        #print(self.riesenie)



class P106(Zadanie):
    def __init__(self):
        super().__init__()
        global prikl
        self.zadanie = r'Najdi funkční hodnoty pro oba vázané stacionární body\\ \phantom{xxxxxx}a vyber tu najvětší. $f_{\text{max}}(x,y)=$'
        stac1 = prikl.funkcia(prikl.riesenia[0])
        stac2 = prikl.funkcia(prikl.riesenia[1])
        #stac3 = prikl.funkcia(prikl.riesenia[2])
        #stac4 = prikl.funkcia(prikl.riesenia[3])
        stac = [stac1,stac2]
        maxstac = -10000
        maxindex = 0
        N = len(stac)
        for i in range(N):
            if stac[i] > maxstac:
                maxstac = stac[i]
                maxindex = i
        chybneMaxstac = maxstac - 1
        self.riesenie = r'$'+str(maxstac)+r'$'
        self.neriesenie = r'$'+str(chybneMaxstac)+r'$'




            
# GENERACIA


def prikladyLoad():
    return [P101(), P102(), P103(), P104(), P105(), P106()]



filewrite('vazba.tex','Viazané extrémy', prikladyLoad,
          r'Cílem je najít \textbf{vázané extrémy} funkce $f(x,y)$ zadané v \textbf{(a)} spolu s vazbou (podmínkou). Postupuj podle krokú v \textbf{(b)} až \textbf{(f)}. Pokud se medzivýsledky shodujú s těmi za otazníky,\\tak napravo obarvi příslušející kroužek načerno. \textbf{Spolu odevzdejte výsledné slovo}.',
          prikladyFontsize=r'\normalsize', rieseniaFontsize=r'\footnotesize', tabulkyBraille=False, minimalistic=False, nicefracSolution=False, tightLayout=False)
