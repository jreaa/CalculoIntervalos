from math import *
import os
import pandas as pd
import matplotlib.pyplot as plot
import seaborn as sb

class tableIntervalos():

    arrayData = []
    def __init__(self,arrayData):
        self.arrayData = arrayData

    def sortingTable(self):
        return sorted(self.arrayData)

    def maxTable(self):
        arrayTable = self.sortingTable()
        return max(arrayTable)

    def minTable(self):
        arrayTable = self.sortingTable()
        return min(arrayTable)
    
    def nTable(self):
        return len(self.arrayData)

    def rango(self):
        maxValue = self.maxTable()
        minValue = self.minTable()

        r = (float("{0:.2f}".format(maxValue - minValue)))
        return r
    
    def sturgues(self):
        nIntervalos = self.nTable()
        mSturgues = round(float("{0:.2f}".format(1+3.3 * log(nIntervalos,10))))

        return mSturgues
    
    def amplitud(self):
        r = self.rango()
        m = self.sturgues()

        a = (float("{0:.2f}".format(r/m)))

        return a
    
    def amplitudEntero(self):
        r = self.rango()
        m = self.sturgues()

        a = round(float("{0:.2f}".format(r/m)))

        return a

class calculoIntervalo():
    #data
    tableIntervalo = []
    a = 0
    r = 0
    m = 0

    #valores
    intervalos = []
    intervalosHistograma = []
    fi = []
    xi = []

    #endvalores

    x1 = []
    i = 0
    calXi = 0
    hi = []
    f2i = []
    h2i = []

    p = 0


    tablesort = 0

    def __init__(self, tablaIntervalo, amplitud,radio,moda):
        self.tableIntervalo = tablaIntervalo
        self.a = amplitud
        self.r = radio
        self.m = moda
        self.x1 = tablaIntervalo[0]

        self.calculoIntervalos()

    def calculoIntervalos(self):
        for x in range(self.m):
            c = float("{0:.2f}".format(self.x1 + self.a))  
            value = (f'[{self.x1} - {c})')
            calXi = float("{0:.2f}".format((self.x1+c)/2))
            self.intervalos.append(value)
            
            if(self.i == 0):
                self.intervalosHistograma.append(self.x1)
                self.intervalosHistograma.append(c)
            else:
                self.intervalosHistograma.append(c)
            
            self.xi.append(calXi)
            
            count = 0
            for table in self.tableIntervalo:
                if(c == self.tableIntervalo[len(self.tableIntervalo)-1]):
                    if(table >= self.x1 and table <= c):
                        count = count + 1
                else:
                    if(table >= self.x1 and table < c):
                        count = count + 1
            self.fi.append(count)
            self.hi.append((count/len(self.tableIntervalo))*100)
                
            self.x1 = float("{0:.2f}".format(self.x1 + a))

            self.i = self.i + 1

        for x in self.fi:
            self.p = self.p + x
            self.f2i.append(self.p)

            self.h2i.append(  float("{0:.2f}".format((self.p/len(self.tableIntervalo) * 100))) )

    def obtenerTable(self):
        dataFrame = pd.DataFrame({'Intervalos': self.intervalos, 'fi': self.fi, 'xi' : self.xi, 'hi': self.hi, 'Fi' : self.f2i, 'Hi': self.h2i})
        return dataFrame

    def obtenerHistograma(self):
        #intervalos = range(min(self.intervalosHistograma), max(self.intervalosHistograma) + 2)

        dataFrame = self.obtenerTable()
        
        sb.barplot(x = 'Intervalos', y = 'fi', data=dataFrame)
        
        #sb.histplot(data = dataFrame, x = 'Intervalos', y = 'fi', color='#F2AB6D') #creamos el gráfico en Seaborn

        #configuramos en Matplotlib
        plot.ylabel('Frecuencia')
        plot.xlabel('Intervalos')
        plot.title('Barras - code by -  Jose Era')

        plot.show()

    

if __name__ == '__main__':
######################## Data General ########################################
    tabla = [1.56, 1.59, 1.63, 1.62, 1.47, 1.57, 1.60, 1.54, 1.56, 1.65,
    1.61, 1.59, 1.51, 1.62, 1.50, 1.62, 1.59, 1.62, 1.54, 1.62,
    1.53, 1.49, 1.57, 1.54, 1.68, 1.52, 1.62, 1.59, 1.49, 1.53,
    1.59,1.58, 1.57, 1.47, 1.65, 1.53, 1.59, 1.56, 1.54, 1.64,
    1.55, 1.59, 1.53 ,1.56 ,1.58 ,1.52 ,1.63 ,1.56 ,1.62 ,1.53]


    tabla2 = [119, 125, 126,128,132,135,135,135,136,138,138,140,140,142,142,144,144,145,145,146,
              146,147,147,148,149,150,150,152,153,154,156,157,158,161,163,164,165,168,173,176]


    tabla3 = [36.2,38.1,38.4,38.4,40.1,40.4,40.5,42.1,42.2,42.2,42.3,42.3,45.0,
              45.1,45.1,45.2,45.4,45.5,46.0,50.1,50.4,50.6,50.6,52.0,52.0,52.1,52.3,55.2,55.2,58.7]
######################## Calculo de datos necesarios ########################################

    tableIntervalo = tableIntervalos(tabla2)
    a = tableIntervalo.amplitudEntero()
    r = tableIntervalo.rango()
    m = tableIntervalo.sturgues()

    tablesort = tableIntervalo.sortingTable()
    
########################## Calculo de table Intervalos ######################################

    calculoIntervalo = calculoIntervalo(tablesort, a, r, m)
    print(calculoIntervalo.obtenerTable())

    calculoIntervalo.obtenerHistograma()

########################## Histograma #######################################################

        
    os.system('pause')

