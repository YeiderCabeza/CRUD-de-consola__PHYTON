import mysql.connector
from mysql.connector import Error

# create table contacto(
#     cont_id int PRIMARY key AUTO_INCREMENT,
#     cont_nombre varchar(50) not null,
#     cont_apellido varchar(50) not null,
#     cont_telefono int NOT null,
#     cont_correo varchar(50) not null
# );

class ConectarBD():
    
    def __init__(self):
        try:
            self.conexion = mysql.connector.connect(
                host='localhost',
                port=3309,
                user='root',
                password='',
                db='bd_contactos'
            )
        except Error as ex:
            print("error al conectar en la base de datos: {0}".format(ex))

    def listarContactos(self):
        if self.conexion.is_connected():
            try:
                cursor = self.conexion.cursor()
                cursor.execute("SELECT * FROM contacto ORDER BY cont_nombres ASC")
                resultados = cursor.fetchall()
                return resultados
            except Error as ex:
                print("error al conectar en la base de datos: {0}".format(ex))

    def crearContactos(self,contactos):
        if self.conexion.is_connected():
            try:
                cursor = self.conexion.cursor()
                sql = "INSERT INTO `contacto`(cont_nombres,cont_apellidos,cont_telefono,cont_correo) VALUES ( '{0}','{1}','{2}','{3}')"
                cursor.execute(sql.format(contactos[0],contactos[1],contactos[2],contactos[3]))
                self.conexion.commit()
                print("Conctato creado")
            except Error as ex:
                print("error al conectar en la base de datos: {0}".format(ex))
    
    def eliminar(self,id): 
         if self.conexion.is_connected():
            try:
                cursor = self.conexion.cursor()
                sql = "DELETE FROM contacto WHERE cont_id ='{0}' "
                cursor.execute(sql.format(id))
                self.conexion.commit()
                print("xxxx Conctato Eliminado xxxx")
            except Error as ex:
                print("error al conectar en la base de datos: {0}".format(ex))
                
    def editar(self,contactos): 
         if self.conexion.is_connected():
            try:
                cursor = self.conexion.cursor()
                sql = "UPDATE `contacto` SET `cont_nombres`='{0}',`cont_apellidos`='{1}',`cont_telefono`={2},`cont_correo`='{3}' WHERE cont_id ={4} "
                cursor.execute(sql.format(contactos[1],contactos[2],contactos[3],contactos[4],contactos[0]))
                self.conexion.commit()
                print("¡¡¡¡ Conctato Actualizado !!!!")
            except Error as ex:
                print("error al conectar en la base de datos: {0}".format(ex))
    
    
    
