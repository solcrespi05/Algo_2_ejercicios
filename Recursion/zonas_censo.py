from abc import ABC, abstractmethod
from typing import List
class Zona(ABC): 
    def __init__(self):
        self.subzonas: List['Zona'] = []
        
    @abstractmethod
    def censar(self)-> int:
        pass

class Vivienda(Zona): 
    def __init__(self, habitantes: int):
        super().__init__()
        self.habitantes= habitantes

    def censar(self) -> int:
        return self.habitantes

class Barrio(Zona):
    def __init__(self):
        super().__init__()
    
    def censar(self) -> int:
        total_habitantes = 0
        for subzona in self.subzonas:
            total_habitantes += subzona.censar()
        return total_habitantes


class Municipio(Zona):
    def __init__(self):
        super().__init__()
    def censar(self) -> int:
        total_habitantes = 0
        for subzona in self.subzonas:
            total_habitantes += subzona.censar()
        return total_habitantes

class Provincia(Zona):
    def __init__(self):
        super().__init__()
    def censar(self) -> int:
        total_habitantes = 0
        for subzona in self.subzonas:
            total_habitantes += subzona.censar()
        return total_habitantes


class Pais(Zona):
    def __init__(self) -> None:
        super().__init__()

    def censar(self) -> int:
        total_habitantes = 0
        for subzona in self.subzonas:
            total_habitantes += subzona.censar()
        return total_habitantes
    
# Ejemplo de uso
def main():
    # Crear algunas viviendas
    vivienda1 = Vivienda(habitantes=4)
    vivienda2 = Vivienda(habitantes=3)
    
    # Crear un barrio con las viviendas
    barrio = Barrio()
    barrio.subzonas.append(vivienda1)
    barrio.subzonas.append(vivienda2)
    
    # Crear un municipio con el barrio
    municipio = Municipio()
    municipio.subzonas.append(barrio)
    
    # Crear una provincia con el municipio
    provincia = Provincia()
    provincia.subzonas.append(municipio)
    
    # Crear un país con la provincia
    pais = Pais()
    pais.subzonas.append(provincia)
    
    # Censar el país
    print(f"Total de habitantes en el país: {pais.censar()}")

if __name__ == "__main__":
    main()
