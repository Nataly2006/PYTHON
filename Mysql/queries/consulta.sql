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
-- Tu consulta debe ordenar el resultado por porcentaje de habla del idioma en orden descendente.

-- CONSULTA  si funciona
SELECT name,language,percentage
FROM countries,languages
WHERE language LIKE "Slovene%"
ORDER BY percentage DESC;

-- ------------------------------------------------------------------------------------------------------------------------------------
-- 2. ¿Qué consulta ejecutarías para mostrar el número total de ciudades de cada país?  Tu consulta debe devolver el nombre del país,
-- el idioma y el número total de ciudades. Tu consulta debe ordenar el resultado por el número de ciudades en orden descendente.

-- CONSULTA no funciona
SELECT countries.name AS nombre_pais, languages.language AS idioma, COUNT(cities.id) AS numero_ciudades
FROM countries
JOIN languages ON countries.code = languages.code
JOIN cities ON countries.code = cities.country_code
GROUP BY countries.name, languages.language
ORDER BY numero_ciudades DESC;

-- -------------------------------------------------------------------------------------------------------------------------------------
-- 3. ¿Qué consulta ejecutarías para obtener todos ciudades de México con una población mayor a 500,000? Tu consulta 
-- debe ordenar el resultado por población en orden descendente.

-- CONSULTA si funciona
SELECT name AS nombre_ciudad, population AS poblacion
FROM cities
WHERE country_code = 'MEX' AND population > 500000
ORDER BY population DESC;

-- --------------------------------------------------------------------------------------------------------------------------------------
-- 4. ¿Qué consulta ejecutarías para obtener todos los idiomas en cada país con un porcentaje de habla mayor a 89%?
-- Tu consulta debe ordenar el resultado por porcentaje de habla en orden descendente.

-- CONSULTA no funciona
SELECT countries.name AS nombre_pais, languages.language AS idioma, languages.percentage AS porcentaje_habla
FROM countries
JOIN languages ON countries.code = languages.code
WHERE languages.percentage > 89
ORDER BY languages.percentage DESC;

-- -------------------------------------------------------------------------------------------------------------------------------------
-- 5. ¿Qué consulta ejecutarías para obtener todos los países con un área de superficie menor a 501 y población mayor a 100,000?

-- CONSULTA si funciona
SELECT name AS nombre_pais, surface_area AS area_superficie, population AS poblacion
FROM countries
WHERE surface_area < 501 AND population > 100000;

-- -------------------------------------------------------------------------------------------------------------------------------------
-- 6. ¿Qué consulta ejecutarías para obtener países solo con monarquía constitucional, un capital superior a 200 
-- y una esperanza de vida mayor a 75 años?

-- CONSULTA si funciona
SELECT name AS nombre_pais, government_form AS tipo_gobierno, capital AS capital, life_expectancy AS esperanza_vida
FROM countries
WHERE government_form = 'Constitutional Monarchy' AND capital > 200 AND life_expectancy > 75;

-- -------------------------------------------------------------------------------------------------------------------------------------
-- 7. ¿Qué consulta ejecutarías para obtener todas las ciudades de Argentina dentro del distrito de Buenos Aires con una población mayor
-- a 500,000 habitantes?  La consulta debe devolver el nombre del país, el nombre de la ciudad, el distrito y la población.

-- CONSULTA no funciona
SELECT countries.name AS nombre_pais, cities.name AS nombre_ciudad, districts.name AS distrito, cities.population AS poblacion
FROM countries
JOIN cities ON countries.code = cities.country_code
JOIN districts ON cities.district = districts.name
WHERE countries.code = 'ARG' AND districts.name = 'Buenos Aires' AND cities.population > 500000;

-- -------------------------------------------------------------------------------------------------------------------------------------
-- 8. ¿Qué consulta ejecutarías para resumir el número de países en cada región? Tu consulta debe mostrar el nombre de la región y 
-- el número de países. Además, debe ordenar el resultado por el número de países en orden descendente.

-- CONSULTA si funciona
SELECT region AS nombre_region, COUNT(name) AS numero_paises
FROM countries
GROUP BY region
ORDER BY numero_paises DESC;