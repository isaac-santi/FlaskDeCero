from app.data.modelo.jugador import Jugador

class JugadorDao:

    def select_all(self,db) -> list[Jugador]:
        cursor = db.cursor()
        cursor.execute('select jugadores.*, equipos.nombre  from jugadores inner join equipos on jugadores.id_equipo = equipos.id;')
        jugadores_en_db = cursor.fetchall()
        jugadores : list[Jugador]= list()
        for jugador_en_db in jugadores_en_db:
            jugadores.append(Jugador(jugador_en_db[0], jugador_en_db[1], jugador_en_db[2], jugador_en_db[3]))

        cursor.close()
        return jugadores
    

    def insert (self,db,nombre,id_equipo):
        cursor = db.cursor()
        sql = ("INSERT INTO jugadores (nombre,id_equipo) values (%s,%s) ")
        data = (nombre,id_equipo)
        cursor.execute(sql, data)
        db.commit()

    def delete (self,db,idjugador):
        cursor = db.cursor()
        sql = ("delete FROM jugadores WHERE idjugador = %s ")
        data = [idjugador]
        cursor.execute(sql,data)
        db.commit()

    def update (self,db,idjugador,nombre,id_equipo):
        cursor = db.cursor()
        sql = ("update jugadores SET nombre = %s, id_equipo = %s WHERE idjugador = %s ")
        data = [nombre,id_equipo,idjugador]
        cursor.execute(sql, data)
        db.commit()

    def updateNombre (self,db,idjugador,nombre):
        cursor = db.cursor()
        sql = ("update jugadores set nombre = %s WHERE idjugador = %s ")
        data = [nombre,idjugador]
        cursor.execute(sql,data)
        db.commit()