
from app.data.modelo.equipo import Equipo

class EquipoDao:

    def select_all(self,db) -> list[Equipo]:
        cursor = db.cursor()
        cursor.execute('SELECT * FROM equipos')
        equipos_en_db = cursor.fetchall()
        equipos : list[Equipo]= list()
        for equipo_en_db in equipos_en_db:
            equipos.append(Equipo(equipo_en_db[0], equipo_en_db[1], equipo_en_db[2]))

        cursor.close()
        return equipos
    
    def insert (self,db,nombre,pais):
        cursor = db.cursor()
        sql = ("INSERT INTO equipos (nombre,pais) values (%s,%s) ")
        data = (nombre,pais)
        cursor.execute(sql, data)
        db.commit()
        
    def delete (self,db,id):
        cursor = db.cursor()
        sql = ("delete FROM equipos WHERE id= %s ")
        data = [id]
        cursor.execute(sql,data)
        db.commit()
    
    def update (self,db,id,nombre,pais):
        cursor = db.cursor()
        sql = ("update equipos SET nombre = %s, pais = %s WHERE id = %s ")
        data = [nombre,pais,id]
        cursor.execute(sql, data)
        db.commit()
    
    def updateNombre (self,db,id,nombre):
        cursor = db.cursor()
        sql = ("update equipos set nombre = %s WHERE id = %s ")
        data = [nombre,id]
        cursor.execute(sql,data)
        db.commit()