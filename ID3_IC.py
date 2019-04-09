# coding: utf-8
import math

class ID3(object):

	def __init__(self,ejemplos = "Juego.txt", atributos = "AtributosJuego.txt"):
		self.listaEjemplosIni = []
		self.listaAtributosIni = []
		self.listaEjemplosIni = leerArchivo(ejemplos)
		self.listaAtributosIni = leerArchivo(atributos)
		for i in range(0,len(self.listaEjemplosIni)):
			if self.listaEjemplosIni[i] == "":
				del self.listaEjemplosIni[i]
			else:
				self.listaEjemplosIni[i] = self.listaEjemplosIni[i].split(",")
		self.listaAtributosIni = self.listaAtributosIni[0].split(",")
		self.arbol(self.listaAtributosIni,self.listaEjemplosIni)

	def arbol(self,listaAtributos,listaEjemplos):
		print ("Atributos:",listaAtributos,'\n')
		print ("Ejemplos:",listaEjemplos,'\n')
		#Si lista-ejemplos está vacía, "regresar"; en caso contrario, seguir.
		if esta_vacia(listaEjemplos) == True:
			print("No hay datos disponibles para analizar")
			return
		# Si todos los ejemplos en lista-ejemplos son +, devolver "+"; de otro modo seguir
		# Si todos los ejemplos en lista-ejemplos son -, devolver "-"; de otro modo seguir
		N = len(listaAtributos)
		Ins = len(listaEjemplos)
		positivos = 0
		negativos = 0
		for j in range(0,Ins):
			if listaEjemplos[j][N-1] == "si":
				positivos += 1
			elif listaEjemplos[j][N-1] == "no":
				negativos += 1
			else:
				print(evaluar)
		if positivos == 0:
			print("devuelve no",'\n')
			return ("no")
		if negativos == 0:
			print("devuelve si",'\n')
			return ("si")
		# Si lista-atributos está vacía, devolver "error";
		if esta_vacia(listaAtributos) == True:
			print("error")
			return
		#En caso contrario:
		#Encontrar el mérito de cada clase
		meritos = []
		for x in range(0,N-1):
			merito = self.hallar_merito(listaEjemplos,N,x)
			meritos.append(merito)
		print("Méritos:",meritos,'\n')
		#escogerAtributo
		mejor = min(meritos)
		#llamar mejor al elemento a de lista-atributos que minimice mérito
		posicionMejor = 0
		posicionMejor = meritos.index(mejor)
		print("El mejor atributo es",listaAtributos[posicionMejor],"con mérito",mejor,'\n')
		#iniciar un árbol cuya raíz sea mejor:
		#para cada valor vi de mejor
		ejemplos_restantes = []
		atributos_restantes = []
		lista_mejor = []
		for x in range(0,Ins):
			if listaEjemplos[x][posicionMejor] in lista_mejor:
				pass
			else:
				lista_mejor.append(listaEjemplos[x][posicionMejor])
		print("Valores del atributo seleccionado:",lista_mejor,'\n')
		#incluir en ejemplos-restantes los elementos de lista-ejemplos
		#que tengan valor vi del atributo mejor
		for x in range(0,len(lista_mejor)):
			ejemplos_re = []
			ejemplos_re = self.ordenar_lista(Ins,listaEjemplos,posicionMejor,N,lista_mejor[x])
			ejemplos_restantes.append(ejemplos_re)
		for z in range(0,N):
			if z == posicionMejor:
				pass
			else:
				atributos_restantes.append(listaAtributos[z])
		for total in range(0,len(ejemplos_restantes)):
			print("Para el valor",lista_mejor[total],"del atributo",listaAtributos[posicionMejor],":")
			self.arbol(atributos_restantes,ejemplos_restantes[total])

	def hallar_merito(self,listaEjemplos,N,clase):
		Instancias = len(listaEjemplos)
		claves = []
		valores = []
		for x in range(0,Instancias):
			claves.append(listaEjemplos[x][clase])
			valores.append(listaEjemplos[x][N-1])
			frecuencia = {}
			for word in claves:
				count = frecuencia.get(word,0)
				frecuencia[word] = count + 1	
		l = len(frecuencia)
		claves2 = []
		ax = []
		for clave, valor in frecuencia.items():
			claves2.append(clave)
			ax.append(valor)
		px = [0]*len(ax)
		nx = [0]*len(ax)
		rx = [0]*len(ax)
		for j in range(0,l):
			for i in range(0,len(claves)):
				if claves[i]== claves2[j]:
					if valores[i] == "si":
						px[j] += 1
					elif valores[i] == "no":
						nx[j] += 1
					else:
						print(evaluar)
				rx[j] = ax[j]/Instancias
		merito = calcular_merito(ax,px,nx,rx,l)
		return merito

	def ordenar_lista(self,Ins,listaEjemplos,posicionMejor,N,valor):
		ejemplosRestantes = []
		for p in range(0,Ins):
			ej = []
			if listaEjemplos[p][posicionMejor] == valor:
				for y in range(0,N):
					if y == posicionMejor:
						pass
					else:
						ej.append(listaEjemplos[p][y])
				ejemplosRestantes.append(ej)
			else:
				pass
		return ejemplosRestantes

def leerArchivo(archivo):
	archivo = open(archivo)
	lista = archivo.read()
	lista = lista.splitlines()
	return lista

def esta_vacia(estructura):
	if estructura:
		return False
	else:
		return True

def calcular_merito(a ,p ,n ,r ,clases):
	meritoClase = 0.00
	for i in range(0,clases):
		if p[i] == 0 or n[i] == 0:
			meritoClase = meritoClase
		else:
			meritoClase = meritoClase+(r[i]*(-(p[i]/a[i])*math.log((p[i]/a[i]),2)-(n[i]/a[i])*math.log((n[i]/a[i]),2)))
	return meritoClase

def main():
	id3 = ID3()

if __name__ == '__main__':
	main()