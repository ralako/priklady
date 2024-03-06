from random import choices, choice, shuffle
from itertools import chain
import os, sys
from brailleSlovnik import *


class Zadanie:
    
    def __init__(self, maxnum=10):
        self.maxnum = maxnum
        self.vyber = []
        self.spravne = None
        for i in range(1,self.maxnum):
            self.vyber += [i]*(self.maxnum+1-i)
            self.vyber += [-i]*(self.maxnum+1-i)

    def zvolKoef(self,pocet,problemy,limit=100,menovatel=1):
        hladaj = True
        while hladaj == True:
            koeficienty = choices(self.vyber, k=pocet)
            #print(koeficienty)
            hladaj = False
            for problem in problemy:
                sucin = 1
                for p in problem:
                    #print(sucin,p)
                    sucin *= abs(koeficienty[p-1])
                if sucin > limit:
                    #print("ech")
                    hladaj = True
        return koeficienty


    def check(self,string):
        if string[0] == '+':
            string = string[1:]
        cisloStr = ''
        odstran = []
        odstranenePocet = 0
        
        for i in range(len(string)):
            try:
                cifra = int(string[i])
                cisloStr += string[i]
            except:
                if string[i] in ['x','y','z']:
                    if cisloStr != '':
                        if int(cisloStr) == 1:
                            odstran.append(i-1-odstranenePocet)
                            odstranenePocet += 1
                cisloStr = ''
                
        for i in range(len(string)):
            if i in odstran:
                string = string[:i] + string[i+1:]
                
        return string.replace(r'+-',r'-').replace(r'{+',r'{').replace(r'--',r'+').replace(r'-+',r'-').replace(r'++',r'+')


    def prepis(self,string,koef):
        koefStr = []
        for i in range(len(koef)):
            koefStr.append(abeceda[i])
        
        sucinKoefStr = ''
        sucinKoef = 1
        nahradzujStr = []
        nahradeneKoef = []

        for prvok in string:
            jetupismenko = False
            for i in range(len(koefStr)):
                if prvok == koefStr[i]:
                    sucinKoefStr += prvok
                    sucinKoef *= koef[i]
                    jetupismenko = True

            if jetupismenko == False:
                if sucinKoefStr != '':
                    nahradzujStr.append(sucinKoefStr)
                    nahradeneKoef.append(sucinKoef)
                    sucinKoefStr = ''
                    sucinKoef = 1
                    
        for i in range(len(nahradzujStr)):
            string = string.replace(nahradzujStr[i],str(nahradeneKoef[i]),1)
            
        return r'$' + self.check(string) + r'$'
    
    
    
    def texRiesPoly(self,cleny):    # cleny v poradi od absolutneho po najväèšiu mocninu
        riesenie = ''
        for i in reversed(range(1,len(cleny))):
            koef = cleny[i]
            if koef != 0:
                if koef > 0:
                    riesenie += '+'+str(cleny[i])+'x'
                else:
                    riesenie += str(cleny[i])+'x'
                if i >= 2:
                    riesenie += '^'+str(i)
        if cleny[0] != 0:
            riesenie += r'+'+str(cleny[0])
        if riesenie == '':
            riesenie = '0'
        return r'$' + self.check(riesenie) + r'$'


    def texRiesZlom(self,citatel,menovatel):
        riesenieCit = self.texRiesPoly(citatel)[1:-1]
        riesenieMen = self.texRiesPoly(menovatel)[1:-1]
        return r'$\cfrac{' + self.check(riesenieCit) + r'}{' + self.check(riesenieMen) + r'}$'


    def texRiesZlomCisla(self,citatel,menovatel):
        if menovatel == 0:
            return 'nedefinováno'
        elif citatel == 0:
            return '0'
        else:
            if menovatel < 0:
                citatel = -citatel
                menovatel = -menovatel
            # krátenie
            kratenie = True
            while kratenie == True:
                kratenie = False
                for prvocislo in prvocisla:
                    if citatel % prvocislo == 0 and menovatel % prvocislo == 0:
                        citatel //= prvocislo ; menovatel //= prvocislo
                        kratenie = True
            if menovatel == 1:
                return r'$'+ str(citatel) + r'$'
            else:
                return r'$\nicefrac{' + str(citatel) + r'}{' + str(menovatel) + r'}$'


    def texRiesVypis(self,cleny):
        vypis = ''
        oddelovac = r' , '
        for clen in cleny:
            if type(clen) == str:
                if clen[0] == r'$':
                    clen = clen[1:-1]
            vypis += str(clen) + oddelovac
        return r'$' + vypis[:-len(oddelovac)] + r'$'


    def texInterval(self,intervaly,uzavretia):
        uzavSymZac = [r'(',r'\langle']
        uzavSymKon = [r')',r'\rangle']
        string = '$x\in'
        for i in range(len(intervaly)):
            zaciatok = intervaly[i][0]
            koniec = intervaly[i][1]
            uzavZac = uzavretia[i][0]
            uzavKon = uzavretia[i][1]
            if zaciatok in ['inf','infty','INF','INFTY','infinity','INFINITY']:
                zaciatok = '\infty'
            if zaciatok in ['-inf','-infty','-INF','-INFTY','-infinity','-INFINITY']:
                zaciatok = '-\infty'
            if koniec in ['inf','infty','INF','INFTY','infinity','INFINITY']:
                koniec = '\infty'
            if koniec in ['-inf','-infty','-INF','-INFTY','-infinity','-INFINITY']:
                koniec = '-\infty'
            string += uzavSymZac[uzavZac] + str(zaciatok) + r' , ' + str(koniec) + uzavSymKon[uzavKon]
            if i != len(intervaly)-1:
                string += r'\cup'
        return string + r'$'


    def texIntervalR(self,body):
        string = r'$\mathbb{R}'
        if len(body) > 0:
            string += r'\smallsetminus\{'
            for bod in body:
                bodTu = str(bod)
                if bodTu[0] == r'$':
                    bodTu = bodTu[1:-1]
                string += bodTu+r','
            string = string[:-1]
        string += r'\}$'
        return string




class blank(Zadanie):
    def __init__(self):
        super().__init__()
        self.zadanie = ''
        self.riesenie = 'vybarvi'
        self.neriesenie = 'nebarvi'



# TEXOVANIE

def t(prikaz):
    global file
    file.write(prikaz)
    file.write('\n')


def stranawrite(skupina,slovo,nazov,prikladyLoad,text,N,prikladyFontsize='\small'):
    #global braille
    tabularsep = [r'&', r'\\ \hdashline', r'&', r'%']
    t(r'\thispagestyle{empty}')
    t(r'\begin{tabular}{c:c}')
    prikladyRiesALL = []
    # stvrtina
    for j in range(N):
        t(r'\begin{minipage}[c][99mm][t]{0.49\linewidth}')
        t(r'\begin{center}')
        t(r'\vspace{7mm}')
        t(r'{\huge '+nazov+r', skupina \textit{'+skupina+r' $'+'\\'+skupina.lower()+r'$} -\romannumeral'+str(j+1)+r'}\\[4.5mm]')
        t(r'\textit{Meno:}\phantom{xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx}\\[3.5mm]')
        t(text+r'\\[3mm]')
        t(r'\begin{minipage}{0.77\linewidth}')
        t(r'\begin{center}')
        # priklady
        t(r'\begin{varwidth}{\textwidth}')
        t(r'\begin{enumerate}')
        t(prikladyFontsize)
        priklady = prikladyLoad()    # load prikladov
        prikladyRies = []
        for i in range(6):
            priklad = priklady[i]
            if braille[slovo[j]][i] == 1:
                zaotaznikom = priklad.riesenie
                priklad.spravne = 1
            else:
                zaotaznikom = priklad.neriesenie
                priklad.spravne = 0
            t(r'\item ' + priklad.zadanie + r'\quad \dotfill\; ???\;\dotfill \quad ' + zaotaznikom)
            prikladyRies.append([priklad.riesenie,priklad.spravne])
        prikladyRiesALL.append(prikladyRies)
        t(r'\end{enumerate}')
        t(r'\end{varwidth}')
        t(r'\end{center}')
        t(r'\end{minipage}')
        # braille
        t(r'\begin{minipage}{0.20\linewidth}')
        t(r'\begin{center}')
        t(r'{\Huge\bfseries '+str(j+1)+r'.} \\[2mm]')
        t(r'\includegraphics[height=40mm]{../images/braille.png}')
        t(r'{\small Písmeno Braillovej abecedy}')
        t(r'\end{center}')
        t(r'\end{minipage}')
        t(r'\end{center}')
        t(r'\end{minipage}')
        t(tabularsep[j])
    t(r'\end{tabular}')
    t(r'\begin{tikzpicture}[remember picture,overlay]\node[xshift=7mm,yshift=-100.6mm,anchor=north west] at (current page.north west){\ding{33}};\end{tikzpicture}')
    t(r'\begin{tikzpicture}[remember picture,overlay]\node[xshift=151.2mm,yshift=-7mm,anchor=north west,rotate=270] at (current page.north west){\ding{33}};\end{tikzpicture}')
    return prikladyRiesALL


def filewrite(filename,nazov,prikladyLoad,text,prikladyFontsize='\small',rieseniaFontsize='\scriptsize',tabulkyBraille=False,minimalistic=False):
    global file
    file = open(filename, 'w', encoding="utf-8")
    # hlavicka
    t(r'\documentclass[10pt]{report}')
    t(r'\usepackage{graphicx}')
    t(r'\usepackage{varwidth}')
    t(r'\usepackage{enumitem}')
    t(r'\usepackage{amsmath}')
    t(r'\usepackage{amssymb}')
    t(r'\usepackage{pifont}')
    t(r'\usepackage{arydshln}')
    t(r'\usepackage{tikz}')
    t(r'\usepackage{lscape}')
    t(r'\usepackage{bm}')
    t(r'\usepackage{nicefrac}')
    t(r'\usepackage[landscape]{geometry}')
    t(r'\geometry{a4paper, total={282mm,200mm}, left=0mm, top=5mm}')
    t(r'\renewcommand{\labelenumi}{\bfseries(\alph{enumi})\phantom{x}}')
    #t(r'\renewcommand{\tabcolsep}{1pt}')
    t(r'\newcommand\omicron{o}')
    t(r'\hfuzz=50pt')
    t(r'\setlist[enumerate]{leftmargin=0pt,itemindent=12pt}')
    t(r'\pagenumbering{gobble}')
    # dokument
    t(r'\begin{document}')
    global zadaniaRiesALL
    zadaniaRiesALL = []
    for strana in range(24):
        zadaniaRiesALL.append(stranawrite(skupiny[strana],slova[strana],nazov,prikladyLoad,text,4,prikladyFontsize=prikladyFontsize))
        t(r'\newpage')
        if minimalistic:
            break     
        
    #print(zadaniaRiesALL)
    # riesenia
    t(r'\begin{landscape}')
    t(r'\newgeometry{total={194mm,285mm}, left=8mm, top=9mm}')
    t(r'\begin{center}')
    t(r'{\huge '+str(nazov)+r' (riešenia)}\\[4mm]')
    t(r'\begin{varwidth}{\linewidth}')
    t(r'\begin{center}')
    t(rieseniaFontsize)
    t(r'\rule[1mm]{\linewidth}{0.5pt}')
    for i in range(24):
        if i == 12:
            t(r'\end{center}\end{varwidth}\end{center}\clearpage\begin{center}{\huge '+str(nazov)+r' (riešenia)}\\[4mm]\begin{varwidth}{\linewidth}\begin{center}')
            t(rieseniaFontsize)
            t(r'\rule[1mm]{\linewidth}{0.5pt}')
        t(r'$\boxed{\bm{'+'\\'+skupiny[i].lower()+r'}} \quad \begin{aligned}')
        for j in range(4):
            t(r'\romannumeral'+str(j+1)+r' : \; &\textbf{'+slova[i][j].upper()+r'} ')
            for k in range(6):
                podzadanie = ['a','b','c','d','e','f'][k]
                t(r' &&\mathrm{\textbf{('+podzadanie+r') }} '+zadaniaRiesALL[i][j][k][0].replace('cfrac','nicefrac').replace(r'$','').replace(r'\enspace',' ')+[r'\,\text{\ding{55}}',r'\,\text{\ding{51}}'][zadaniaRiesALL[i][j][k][1]])
            if j != 3:
                t(r'\\[-0.4mm]')
        t(r'\end{aligned} $')
        if i != 23:
            t(r'\\[2mm]')
            t(r'\rule[1mm]{\linewidth}{0.5pt}')
        if minimalistic:
            break
        
    t(r'\\[1mm]')
    t(r'\rule[-1mm]{\linewidth}{0.5pt}')
    t(r'\end{center}')
    t(r'\end{varwidth}')
    t(r'\end{center}')
    t(r'\end{landscape}')
    
    if tabulkyBraille == True:
        for i in range(6):
            t(r'\clearpage')
            t(r'\setlength{\tabcolsep}{4mm}')
            t(r'\begin{tabular}{c c}')
            for koncovka in [r'&',r'\\',r'&','']:
                t(r'\begin{minipage}{0.49\textwidth}')
                t(r'\begin{center}')
                t(r'\phantom{x}\\[10mm]')
                t(r'{\Large Abeceda v Braillovom písmen na dekódování slov}\\[1mm]')
                t(r'\includegraphics[width=\textwidth]{../images/brailleSkratene.png}')
                t(r'\end{center}')
                t(r'\end{minipage}')
                t(koncovka)
            t(r'\end{tabular}')

    t(r'\end{document}')

    file.close()

    os.system("pdflatex "+str(filename))






