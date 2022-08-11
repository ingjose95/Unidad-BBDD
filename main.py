import sqlite3

miConexion = sqlite3.connect('Alumnos.db')

miCursor = miConexion.cursor()

miCursor.execute('''


    create table ALUMNOS (
    
    ID integer primary key autoincrement,

    NOMBRE_ALUMNO varchar(50),

    APELLIDO_ALUMNO varchar(50))
    
    
    ''')


listaAlumnos = [


    ('JOSÉ', 'MELÉNDEZ'),
    ('MARÍA', 'PÉREZ'),
    ('JUAN', 'SOTO'),
    ('LUIS', 'RAMÍREZ'),
    ('ROMINA', 'GEBEL'),
    ('SALVADOR', 'PÉREZ'),
    ('PATRICIA', 'CASTRO'),
    ('CLAUDIA', 'VARGAS')

    ]

miCursor.executemany('insert into ALUMNOS values (null, ?, ?)', listaAlumnos)

miCursor.execute('select * from ALUMNOS')

verAlumnos = miCursor.fetchall()

for alum in verAlumnos:

    print(f'Nombre de alumno: {alum[1]}')

miConexion.commit()

miConexion.close()