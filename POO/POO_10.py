"""Definir la clase Automovil, que puede subclasificarse en AutoMediano o Camion.
Los autos medianos son capaces de estar habilitados luego de la adquisición de
un permiso en una fecha dada. Los camiones también podrán estar habilitados
luego de la adquisición de un permiso, pero éste sólo podrá expedirse con la
debida autorización previa de la concesionaria donde fue adquirido. Las
concesionarias de camiones verifican ciertas características del camión para
poder registrar al mismo. Este dato también es registrado dentro de la misma
concesionaria."""

class Automovil:
    def __init__(self):
        self.habilitado = False
        pass

    def esta_habilitado(self):
        return self.habilitado
    

class AutoMediano (Automovil):
    def __init__(self):
        super().__init__()
        self.fecha_permiso = None

    def adquirir_permiso(self, fecha):
        self.fecha_permiso = fecha
        self.habilitado = True

class Concesionaria:
    def __init__(self, nombre):
        self.nombre= nombre
        self.camiones = []


    def verificar_camion(self,camion):
        print(f'El camion{camion} ha sido verificado')
        return True

    def registrar_camion(self, camion):
        if self.verificar_camion(camion):
            self.camiones.append(camion)
            return True
        return False

class Camion(Automovil):
    def __init__(self,concesionaria: Concesionaria):
        super().__init__()
        self.autorizado =False
        self.concesionaria = concesionaria

    def adquirir_permiso_autorizacion(self):
        if self.concesionaria.registrar_camion(self):
            self.habilitado = True
        else: 
            return False
        

# Crear concesionaria
concesionaria = Concesionaria("Camiones XYZ")

# Crear un auto mediano y habilitarlo
auto_mediano = AutoMediano()
auto_mediano.adquirir_permiso("2024-08-15")
print(f"AutoMediano habilitado: {auto_mediano.esta_habilitado()}")

# Crear un camión y tratar de habilitarlo
camion = Camion(concesionaria)
camion.adquirir_permiso_autorizacion()
print(f"Camión habilitado: {camion.esta_habilitado()}")
