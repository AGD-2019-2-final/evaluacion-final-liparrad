-- Pregunta
-- ===========================================================================
-- 
-- Obtenga los cinco (5) valores más pequeños de la 3ra columna.
-- Escriba el resultado a la carpeta `output` del directorio actual.
-- 
fs -rm -f -r output;
--
-- >>> Escriba su respuesta a partir de este punto <<<
--
datos = LOAD 'data.tsv' AS (letter:CHARARRAY,date:CHARARRAY,number:INT);

numeros = FOREACH datos GENERATE number;

ordenar_numeros = ORDER numeros BY number;

primeros_numeros = LIMIT ordenar_numeros 5;

STORE primeros_numeros INTO 'output';