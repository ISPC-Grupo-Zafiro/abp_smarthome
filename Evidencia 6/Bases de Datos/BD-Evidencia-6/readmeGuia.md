# README - Ejecución de ConsultasDDL y DML.txt en un DBMS Online

- Este esta carpera se encuentra un archivo llamado ConsultasDDL y DML.txt:

## Requisitos

- No es necesario instalar software en tu computadora.  
- Se recomienda usar un **DBMS online**, como:

- [db-fiddle.com](https://db-fiddle.com/) (MySQL, PostgreSQL, SQL Server, SQLite, Oracle)
- [sqlfiddle.com](http://sqlfiddle.com/) (más limitado, pero simple)
- [OneCompiler](https://onecompiler.com/mysql) (rápido para MySQL)

## Ejecución Paso a Paso

1. **Abrir el DBMS online**  
-  Ingresa a [OneCompiler](https://onecompiler.com/mysql).

2. **Borra el siquiente texto que trae por defecto el compilador**  
   
-- create
CREATE TABLE EMPLOYEE (
  empId INTEGER PRIMARY KEY,
  name TEXT NOT NULL,
  dept TEXT NOT NULL
);
-- insert
INSERT INTO EMPLOYEE VALUES (0001, 'Clark', 'Sales');
INSERT INTO EMPLOYEE VALUES (0002, 'Dave', 'Accounting');
INSERT INTO EMPLOYEE VALUES (0003, 'Ava', 'Sales');
-- fetch 
SELECT * FROM EMPLOYEE WHERE dept = 'Sales';


3. **Abre el archivo ConsultasDDL y DML.txt**  
   El mismo se encuentra en las siguiente carpetas abp_smarthome\Evidencia 6\Bases de Datos\BD-Evidencia-6
   - Copia todo el contenido del archivo.
   - Pégalo en el editor de consultas del DBMS online.
   - Haz clic en **Run** para crear la estructura de la base de datos y que se ejecuten las consultas.


5. **Verificar resultados**  
   - Los datos insertados se mostrarán en la parte derecha de la página del DBMS online en formato de tablas con lineas de puntos.
   - Si hay errores, asegúrate de haber ejecutado y copiado todo el texto del archivo txt.


## Archivos del proyecto  
Los siguientes archivos detallados debajo tambien se encuentran en esta misma ubicacion los mismos son necesarios para crear la base de datos de la siguiente app. Usamos MySQL Workbench para ejecutarlos 

- `consultasDDL.sql` → Contiene las instrucciones para crear las tablas y estructuras de la base de datos.
- `consultasDML.sql` → Contiene las instrucciones para insertar, modificar, eliminar y consultar datos.

Espero que puedas entender las siguientes instrucciones desde ya muchas gracias 