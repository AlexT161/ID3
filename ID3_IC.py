# coding: utf-8

class ID3(object):

	def __init__(self,ejemplos = "Juego.txt", atributos = "AtributosJuego.txt"):
		self.listaEjemplos = []
		self.listaAtributos = []
		self.listaEjemplos = leerArchivo(ejemplos)
		self.listaAtributos = leerArchivo(atributos)
		for i in range(0,len(self.listaEjemplos)):
			if self.listaEjemplos[i] == "":
				del self.listaEjemplos[i]
			else:
				self.listaEjemplos[i] = self.listaEjemplos[i].split(",")
		self.listaAtributos = self.listaAtributos[0].split(",")
		self.arbol(self.listaAtributos,self.listaEjemplos)

	def arbol(self,listaAtributos,listaEjemplos):
		#Si lista-ejemplos está vacía, "regresar"; en caso contrario, seguir.
		if (listaEjemplos == 0):
			return
		# Si todos los ejemplos en lista-ejemplos son +, devolver "+"; de otro modo seguir
		# Si todos los ejemplos en lista-ejemplos son -, devolver "-"; de otro modo seguir
		N = len(listaAtributos)
		positivos = 0
		negativos = 0
		for j in range(0,len(listaEjemplos)):
			if listaEjemplos[j][N-1] == "si":
				positivos += 1
			elif listaEjemplos[j][N-1] == "no":
				negativos += 1
			else:
				print(evaluar)
		if positivos == 0:
			return ("no")
		if negativos == 0:
			return ("si")
		print(positivos)
		print(negativos)
		##hallarMerito
		##escogerAtributo
		print (listaAtributos)
		print (listaEjemplos)

def leerArchivo(archivo):
	archivo = open(archivo)
	lista = archivo.read()
	lista = lista.splitlines()
	return lista

def main():
	id3 = ID3()

if __name__ == '__main__':
	main()