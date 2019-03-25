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
		print (self.listaAtributos)
		print (self.listaEjemplos)

def leerArchivo(archivo):
	archivo = open(archivo)
	lista = archivo.read()
	lista = lista.splitlines()
	return lista

def main():
	id3 = ID3()
	print("lista de Ejemplos:"'\n')
	print(id3)

if __name__ == '__main__':
	main()