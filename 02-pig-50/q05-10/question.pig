-- 
-- Pregunta
-- ===========================================================================
-- 
-- Para el archivo `data.tsv` compute Calcule la cantidad de registros en que 
-- aparece cada letra minúscula en la columna 2.
-- 
-- Escriba el resultado a la carpeta `output` del directorio actual.
-- 
fs -rm -f -r output;
--
-- >>> Escriba su respuesta a partir de este punto <<<
--

datos = LOAD 'data.tsv' AS (upper_case:CHARARRAY, lower_case:BAG{tup:TUPLE(letter:CHARARRAY)},obs:CHARARRAY);

datos1 = FOREACH datos GENERATE FLATTEN(lower_case) AS letter;

agrupar = GROUP datos1 BY letter;

conteo_letras = FOREACH agrupar GENERATE group, COUNT($1);

STORE conteo_letras INTO 'output';