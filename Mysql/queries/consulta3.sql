use lead_gen_business;

-- ---------------------------------------------------------------------------------------------------------
-- 1. ¿Qué consulta ejecutarías para obtener los ingresos totales de marzo de 2012?

-- CONSULTA no funciona
SELECT SUM(ingresos) AS ingresos_totales
FROM tabla_ingresos
WHERE fecha >= '2012-03-01' AND fecha <= '2012-03-31';

-- ---------------------------------------------------------------------------------------------------------
-- 2. ¿Qué consulta ejecutarías para obtener los ingresos totales recaudados del cliente con id de 2?

-- CONSULTA no funciona
SELECT SUM(ingresos) AS ingresos_totales_cliente
FROM tabla_ingresos
WHERE cliente_id = 2;

-- ---------------------------------------------------------------------------------------------------------
-- 3. ¿Qué consulta ejecutarías para obtener todos los sitios que posee el cliente con id de 10?

-- CONSULTA
SELECT sitios
FROM tabla_sitios
WHERE cliente_id = 10;

-- ---------------------------------------------------------------------------------------------------------
-- 4. ¿Qué consulta ejecutarías para obtener el número total de sitios creados por mes por año para el 
-- cliente con id de 1? ¿Qué pasa con el cliente con id de 20?

-- CONSULTA no funciona
SELECT YEAR(fecha) AS anio, MONTH(fecha) AS mes, COUNT(sitio_id) AS total_sitios_creados
FROM tabla_sitios
WHERE cliente_id = 1
GROUP BY anio, mes;

-- ---------------------------------------------------------------------------------------------------------
-- 5. ¿Qué consulta ejecutarías para obtener el número total de clientes potenciales generados para cada uno
-- de los sitios entre el 1 de enero de 2011 y el 15 de febrero de 2011?

-- CONSULTA
SELECT sitio_id, COUNT(cliente_potencial_id) AS total_clientes_potenciales
FROM tabla_clientes_potenciales
WHERE fecha >= '2011-01-01' AND fecha <= '2011-02-15'
GROUP BY sitio_id;

-- ---------------------------------------------------------------------------------------------------------
-- 6. ¿Qué consulta ejecutarías para obtener el número total de clientes potenciales que hemos generado para
-- cada uno de nuestros clientes entre el 1 de enero de 2011 y el 31 de diciembre de 2011?

-- CONSULTA no funciona
SELECT cliente_id, COUNT(cliente_potencial_id) AS total_clientes_potenciales
FROM tabla_clientes_potenciales
WHERE fecha >= '2011-01-01' AND fecha <= '2011-12-31'
GROUP BY cliente_id;

-- ---------------------------------------------------------------------------------------------------------
-- 7. ¿Qué consulta ejecutarías para obtener una lista de nombres de clientes y el número total de clientes
-- potenciales que hemos generado para cada cliente, cada mes, entre los meses 1 y 6 del año 2011?

-- CONSULTA no funciona
SELECT cliente_id, nombre_cliente, MONTH(fecha) AS mes, COUNT(cliente_potencial_id) AS total_clientes_potenciales
FROM tabla_clientes_potenciales
JOIN tabla_clientes ON tabla_clientes_potenciales.cliente_id = tabla_clientes.cliente_id
WHERE YEAR(fecha) = 2011 AND MONTH(fecha) BETWEEN 1 AND 6
GROUP BY cliente_id, mes;

-- ---------------------------------------------------------------------------------------------------------
-- 8. ¿Qué consulta ejecutarías para obtener una lista de nombres de clientes y el número total de clientes 
-- potenciales que hemos generado para cada uno de los sitios de nuestros clientes entre el 1 de enero de 2011
-- y el 31 de diciembre de 2011? Solicita esta consulta por id de cliente. Realiza una segunda consulta que 
-- muestre todos los clientes, los nombres del o los sitios y el número total de clientes potenciales generados 
-- en cada sitio para todos los tiempos.   

-- CONSULTA no funciona
SELECT tabla_clientes.cliente_id, nombre_cliente, GROUP_CONCAT(sitio_nombre) AS sitios, COUNT(cliente_potencial_id) AS total_clientes_potenciales
FROM tabla_clientes
LEFT JOIN tabla_sitios ON tabla_clientes.cliente_id = tabla_sitios.cliente_id
LEFT JOIN tabla_clientes_potenciales ON tabla_sitios.sitio_id = tabla_clientes_potenciales.sitio_id
WHERE fecha >= '2011-01-01' AND fecha <= '2011-12-31'
GROUP BY tabla_clientes.cliente_id, nombre_cliente;

-- ---------------------------------------------------------------------------------------------------------
-- 9. Escribe una única consulta que recupere los ingresos totales recaudados por cada cliente durante cada
-- mes del año. Haz la consulta por id de cliente. Primero intenta esto con el número del mes, luego con el
-- nombre del mes.   Se necesitará una subconsulta SELECT para el segundo desafío.   Mira aquí para ver una pista.     

-- CONSULTA
SELECT cliente_id, nombre_cliente, YEAR(fecha) AS anio, MONTH(fecha) AS mes, SUM(ingresos) AS ingresos_totales
FROM tabla_ingresos
JOIN tabla_clientes ON tabla_ingresos.cliente_id = tabla_clientes.cliente_id
GROUP BY cliente_id, anio, mes;

-- ---------------------------------------------------------------------------------------------------------
-- 10. Escribe una única consulta que recupere todos los sitios que posee cada cliente.  Agrupa los resultados 
-- para que todos los sitios de cada cliente se muestren en un solo campo. Se volverá más claro cuando agregues 
-- un nuevo campo llamado “sitios” que tiene todos los sitios que posee el cliente. (PISTA: usa GROUP_CONCAT)

-- CONSULTA no funciona
SELECT cliente_id, nombre_cliente, GROUP_CONCAT(sitio_nombre) AS sitios
FROM tabla_clientes
LEFT JOIN tabla_sitios ON tabla_clientes.cliente_id = tabla_sitios.cliente_id
GROUP BY cliente_id, nombre_cliente;
