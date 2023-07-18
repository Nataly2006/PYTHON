use twitter;

-- PARA ELIMINAR DATOS
SET SQL_SAFE_UPDATES = 0;

-- PARA MOSTRAR INFORMACIÒN
SELECT *
FROM users;

SELECT * 
FROM faves;

SELECT *  
FROM follows;

SELECT *
FROM tweets;

SELECT id,first_name,last_name,birthday 
FROM users;

SELECT *
FROM users
WHERE id = 4;

SELECT *
FROM users
WHERE id = 1 OR id = 4;

SELECT *
FROM users
WHERE id >= 3;

SELECT *
FROM users
WHERE id > 3;

SELECT birthday 
FROM users
WHERE first_name LIKE "%y";

SELECT * 
FROM users
WHERE first_name LIKE "K%";

SELECT * 
FROM users
WHERE first_name NOT LIKE "K%";

SELECT *
FROM users
ORDER BY birthday DESC;

SELECT *
FROM users
ORDER BY birthday ASC;

SELECT *
FROM users
WHERE first_name LIKE "%e"
ORDER BY birthday DESC;

SELECT *
FROM users
LIMIT 3;

SELECT *
FROM users;

-- PARA INSERTAR O AGREGAR INFORMACIÒN
INSERT INTO users (id,first_name,last_name,handle,birthday,created_at,updated_at)
VALUES(7,'Tamar','Epul','Itachi','2006-01-01',now(),now());

-- PARA ACTUALIZAR INFORMACIÒN
UPDATE users
SET first_name = 'Itachi', handle = 'Catito'
WHERE id=6;

-- PARA ELIMINAR INFORMACIÒN
DELETE FROM users 
WHERE id=6;

