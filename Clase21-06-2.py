from Clase21 import Cargo
class Empleado:
    codigo=0
    def __init__(self,nom,ced,sue,Clase21):
        self.codigo=self.generarCodigo()
        self.nombre=nom
        self.cedula=ced
        self.sueldo=sue
        self.cargo=Clase21

    def mostrar(self):
        print("codigo: {} nombre: {} cargo:{}-{}".format(self.codigo,self.nombre, self.cargo.codigo, self.cargo.descripcion))

    def generarCodigo(self):
        Empleado.codigo= Empleado.codigo+1
        return Empleado.codigo

# x=5
# nom="Ana"
cargo1=Cargo("Docente")
emp1=Empleado("Ashley","0953156049",500,cargo1)
emp1.mostrar()
cargo2=Cargo("Analista")
emp2=Empleado("Carol","09531",500,cargo2)
emp2.mostrar()
