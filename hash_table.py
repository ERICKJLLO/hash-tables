from linked_lists import SinglyLinkedList

class TablaHash:
    def __init__(self, tamaño=10):
        
        self.tamaño = tamaño
        self.tabla = [SinglyLinkedList() for _ in range(self.tamaño)]

    def _hash_knuth(self, clave):
        
        constante_aurea = 0.6180339887
        return int(self.tamaño * ((hash(clave) * constante_aurea) % 1))
    
    def _hash_xor(self, clave):
        
        valor_hash = 0
        
        for caracter in str(clave):
            
            valor_hash ^= (valor_hash << 5) + (valor_hash >> 2) + ord(caracter)
            
        return valor_hash % self.tamaño
    
    def _hash_personalizada(self, clave):
        
        valor_hash = 0
        
        for caracter in str(clave):
            valor_hash += ord(caracter)
        return (valor_hash * 31) % self.tamaño
    
    def _hash(self, clave, metodo):
        
        if metodo == "knuth":
            return self._hash_knuth(clave)
        
        elif metodo == "xor":
            return self._hash_xor(clave)
        
        elif metodo == "personalizada":
            return self._hash_personalizada(clave)

    def insert(self, clave, valor, metodo="knuth"):
        
        indice = self._hash(clave, metodo)
        
        for nodo in self.tabla[indice]:
            if nodo[0] == clave:
                nodo[1] = valor
                return
            
        self.tabla[indice].insert([clave, valor])

    def search(self, clave, metodo="knuth"):
        
        indice = self._hash(clave, metodo)
        
        for nodo in self.tabla[indice]:
            if nodo[0] == clave:
                return nodo[1]
        return None

    def delete(self, clave, metodo="knuth"):
        
        indice = self._hash(clave, metodo)
        
        for nodo in self.tabla[indice]:
            
            if nodo[0] == clave:
                self.tabla[indice].delete(nodo)
                return
            
        raise KeyError(f"La clave '{clave}' no fue encontrada")

    def __str__(self):
        return str([list(cubeta) for cubeta in self.tabla])

def encontrar_duplicados(lista):
    
    tabla_hash = TablaHash()
    duplicados = []
    
    for elemento in lista:
        
        if tabla_hash.search(elemento) is not None:
            if elemento not in duplicados:
                duplicados.append(elemento)
    
        else:
            tabla_hash.insert(elemento, True)
            
    return duplicados

def contar_elementos(lista):
    
    tabla_hash = TablaHash()
    
    for elemento in lista:
        
        frecuencia = tabla_hash.search(elemento)
        
        if frecuencia is None:
            tabla_hash.insert(elemento, 1)
            
        else:
            tabla_hash.insert(elemento, frecuencia + 1)
    resultado = {}
    
    for lista_enlazada in tabla_hash.tabla:
        
        for clave, valor in lista_enlazada:
            resultado[clave] = valor
            
    return resultado

if __name__ == "__main__":
    
    lista_duplicados = ["a", "b", "c", "a", "b", "d"]   
    print("Duplicados en la lista:", encontrar_duplicados(lista_duplicados))
    
    lista_frecuencia = ["a", "b", "c", "a", "b", "d"]
    print("Frecuencia de elementos:", contar_elementos(lista_frecuencia))
