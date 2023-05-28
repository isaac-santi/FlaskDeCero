from flask import Flask, Blueprint, render_template, request,redirect,url_for

from app import db
from app.data.equipo_dao import EquipoDao
from app.data.jugador_dao import JugadorDao

import random   

rutas_usuarios = Blueprint("routes", __name__)


@rutas_usuarios.route('/')
def index():
    return render_template('index.html')

@rutas_usuarios.route('/test')
def test():
    return render_template('test.html')

@rutas_usuarios.route('/verEquipos')
def verEquipos():
    equipo_dao = EquipoDao()

    equipos = equipo_dao.select_all(db)

    return render_template('test.html',equipos=equipos)

@rutas_usuarios.route('/verJugadores')
def verJugadores():
    jugador_dao = JugadorDao()

    jugadores = jugador_dao.select_all(db)

    return render_template('jugadores.html',jugadores=jugadores)

@rutas_usuarios.route('/addEquipo', methods=['POST'])
def addEquipo():

    equipo_dao = EquipoDao()

    nombre = request.form['nombre']
    pais = request.form['pais']

    if (nombre == "" or pais == ""):
        return redirect(url_for('routes.verEquipos'))
    
    equipo_dao.insert(db,nombre,pais)

    return redirect(url_for('routes.verEquipos'))

@rutas_usuarios.route('/addJugador', methods=['POST'])
def addJugador():

    jugador_dao = JugadorDao()

    nombre = request.form['nombre']
    id_equipo = request.form['id_equipo']

    if (nombre == "" or id_equipo == ""):
        return redirect(url_for('routes.verJugadores'))
    
    jugador_dao.insert(db,nombre,id_equipo)

    return redirect(url_for('routes.verJugadores'))

@rutas_usuarios.route('/deleteEquipo', methods=['POST'])
def deleteEquipo():
    
    equipo_dao = EquipoDao()
    
    id = request.form['id']
    
    equipo_dao.delete (db,id)

    return redirect(url_for('routes.verEquipos'))

@rutas_usuarios.route('/deleteJugador', methods=['POST'])
def deleteJugador():
    jugador_dao = JugadorDao()

    idjugador = request.form['id']

    jugador_dao.delete(db, idjugador)

    return redirect(url_for('routes.verJugadores'))


@rutas_usuarios.route('/updateEquipo', methods=['POST'])
def updateEquipo():
        
    equipo_dao = EquipoDao()
        
    id = request.form['id']
    nombre = request.form['nombre']
    pais = request.form['pais']

    if (pais == ""):
        equipo_dao.updateNombre (db,id,nombre)
    else:
        equipo_dao.update (db,id,nombre,pais)
        
    return redirect(url_for('routes.verEquipos'))

@rutas_usuarios.route('/updateJugador', methods=['POST'])
def updateJugador():

    jugador_dao = JugadorDao()
        
    idjugador = request.form['idjugador']
    nombre = request.form['nombre']
    id_equipo = request.form['id_equipo']

    if (id_equipo == ""):
        jugador_dao.updateNombre (db,idjugador,nombre)
    else:
        jugador_dao.update (db,idjugador,nombre,id_equipo)
        
    return redirect(url_for('routes.verJugadores'))