use sakila;

select*
from category;

-- --------------------------------------------------------------------------------------------------------------
-- 1. ¿Qué consulta ejecutarías para obtener todos los clientes dentro de ciudad_id = 312? 
-- Tu consulta debe devolver el nombre, apellido, correo electrónico y dirección del cliente.

-- CONSULTA no funciona
SELECT nombre, apellido, correo_electronico, direccion
FROM clientes
WHERE ciudad_id = 312;

-- --------------------------------------------------------------------------------------------------------------
-- 2. ¿Qué consulta ejecutarías para obtener todas las películas de comedias? Tu consulta debe
-- devolver el título de la película, la descripción, el año de lanzamiento, la clasificación, 
-- las características especiales y el género (categoría).

-- CONSULTA no funciona
SELECT titulo, descripcion, anio_lanzamiento, clasificacion, caracteristicas_especiales, categoria
FROM peliculas
WHERE categoria = 'Comedy%';

-- --------------------------------------------------------------------------------------------------------------
-- 3. ¿Qué consulta ejecutarías para obtener todas las películas por actor_id=5? Tu consulta debe 
-- devolver el id del actor, el nombre del actor, el título de la película, la descripción y el año de lanzamiento.

-- CONSULTA no funciona
SELECT actores.actor_id, actores.nombre AS nombre_actor, peliculas.titulo, peliculas.descripcion, peliculas.anio_lanzamiento
FROM actores
JOIN peliculas_actores ON actores.actor_id = peliculas_actores.actor_id
JOIN peliculas ON peliculas_actores.pelicula_id = peliculas.pelicula_id
WHERE actores.actor_id = 5;

-- --------------------------------------------------------------------------------------------------------------
-- 4. ¿Qué consulta ejecutarías para obtener todos los clientes en store_id=1 y dentro de estas ciudades 
-- (1, 42, 312 y 459)? Tu consulta debe devolver el nombre, apellido, correo electrónico y dirección del cliente.

-- CONSULTA no funciona
SELECT nombre, apellido, correo_electronico, direccion
FROM clientes
WHERE ciudad_id IN (1, 42, 312, 459) AND store_id = 1;

-- ---------------------------------------------------------------------------------------------------------------
-- 5. ¿Qué consulta ejecutarías para obtener todas las películas con una "calificación = G" y una "característica
-- especial = detrás de escena", unidas por actor_id = 15?  Tu consulta debe devolver el título de la película, 
-- la descripción, el año de lanzamiento, la clasificación y la característica especial. Sugerencia: puede usar 
-- la función LIKE para obtener la parte “detrás de escena”.

-- CONSULTA no funciona
SELECT peliculas.titulo, peliculas.descripcion, peliculas.anio_lanzamiento, peliculas.clasificacion, peliculas.caracteristicas_especiales
FROM peliculas
JOIN peliculas_actores ON peliculas.pelicula_id = peliculas_actores.pelicula_id
JOIN actores ON peliculas_actores.actor_id = actores.actor_id
WHERE peliculas.clasificacion = 'G' AND peliculas.caracteristicas_especiales LIKE '%detrás de escena%' AND actores.actor_id = 15;
-- ---------------------------------------------------------------------------------------------------------------
-- 6. ¿Qué consulta ejecutarías para obtener todos los actores que se unieron al film_id = 369? Tu consulta debe 
-- devolver film_id, título, actor_id y actor_name.

-- CONSULTA no funciona
SELECT peliculas_actores.pelicula_id AS film_id, peliculas.titulo, actores.actor_id, actores.nombre AS actor_name
FROM peliculas_actores
JOIN actores ON peliculas_actores.actor_id = actores.actor_id
JOIN peliculas ON peliculas_actores.pelicula_id = peliculas.pelicula_id
WHERE peliculas_actores.pelicula_id = 369;

-- ----------------------------------------------------------------------------------------------------------------
-- 7. ¿Qué consulta ejecutarías para obtener todas las películas de drama con una tarifa de arriendo de 2,99? Tu 
-- consulta debe devolver el título de la película, la descripción, el año de lanzamiento, la clasificación, las
-- características especiales y el género (categoría).

-- CONSULTA no funciona
SELECT peliculas.titulo, peliculas.descripcion, peliculas.anio_lanzamiento, peliculas.clasificacion, peliculas.caracteristicas_especiales, peliculas.categoria
FROM peliculas
JOIN inventario ON peliculas.pelicula_id = inventario.pelicula_id
WHERE peliculas.categoria = 'Drama' AND inventario.tarifa_arriendo = 2.99;

-- ----------------------------------------------------------------------------------------------------------------
-- 8. ¿Qué consulta ejecutarías para obtener todas las películas de acción que estén unidas por SANDRA KILMER? Tu
-- consulta debe devolver el título de la película, la descripción, el año de lanzamiento, la clasificación, las 
-- características especiales, el género (categoría) y el nombre y apellido del actor.

-- CONSULTA
SELECT peliculas.titulo, peliculas.descripcion, peliculas.anio_lanzamiento, peliculas.clasificacion, peliculas.caracteristicas_especiales, peliculas.categoria, actores.nombre AS nombre_actor, actores.apellido AS apellido_actor
FROM peliculas
JOIN peliculas_actores ON peliculas.pelicula_id = peliculas_actores.pelicula_id
JOIN actores ON peliculas_actores.actor_id = actores.actor_id
WHERE peliculas.categoria = 'Acción' AND (actores.nombre = 'SANDRA' AND actores.apellido = 'KILMER');