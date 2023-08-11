use world;

select*
FROM cities;

select*
FROM countries;

select*
FROM languages;

-- ------------------------------------------------------------------------------------------------------------------------------------
-- 1. ¿Qué consulta ejecutarías para obtener todos los países que hablan esloveno?
-- Tu consulta debe devolver el nombre del país, el idioma y el porcentaje de habla del idioma.  
-- Tu consulta debe ordenar el resultado por porcentaje de habla del idioma en orden descendente. (1)

-- CONSULTA 
SELECT name,language,percentage
FROM countries,languages
WHERE language LIKE "Slovene%"
ORDER BY percentage DESC;
-- ------------------------------------------------------------------------------------------------------------------------------------
-- 2. ¿Qué consulta ejecutarías para mostrar el número total de ciudades de cada país?  Tu consulta debe devolver el nombre del país,
-- el idioma y el número total de ciudades. Tu consulta debe ordenar el resultado por el número de ciudades en orden descendente. (3)

-- -------------------------------------------------------------------------------------------------------------------------------------
-- 3. ¿Qué consulta ejecutarías para obtener todos ciudades de México con una población mayor a 500,000? Tu consulta 
-- debe ordenar el resultado por población en orden descendente. (1)
-- --------------------------------------------------------------------------------------------------------------------------------------
-- 4. ¿Qué consulta ejecutarías para obtener todos los idiomas en cada país con un porcentaje de habla mayor a 89%?
-- Tu consulta debe ordenar el resultado por porcentaje de habla en orden descendente. (1)
-- -------------------------------------------------------------------------------------------------------------------------------------
-- 5. ¿Qué consulta ejecutarías para obtener todos los países con un área de superficie menor a 501 y población mayor a 100,000? (2)
-- -------------------------------------------------------------------------------------------------------------------------------------
-- 6. ¿Qué consulta ejecutarías para obtener países solo con monarquía constitucional, un capital superior a 200 
-- y una esperanza de vida mayor a 75 años?  (1)
-- -------------------------------------------------------------------------------------------------------------------------------------
-- 7. ¿Qué consulta ejecutarías para obtener todas las ciudades de Argentina dentro del distrito de Buenos Aires con una población mayor
-- a 500,000 habitantes?  La consulta debe devolver el nombre del país, el nombre de la ciudad, el distrito y la población.  (2)
-- -------------------------------------------------------------------------------------------------------------------------------------
-- 8. ¿Qué consulta ejecutarías para resumir el número de países en cada región? Tu consulta debe mostrar el nombre de la región y 
-- el número de países. Además, debe ordenar el resultado por el número de países en orden descendente. (2)