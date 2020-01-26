-- 
-- Pregunta
-- ===========================================================================
-- 
-- Para el archivo `data.tsv` Calcule la cantidad de registros por clave de la 
-- columna 3. En otras palabras, cuántos registros hay que tengan la clave 
-- `aaa`?
-- 
-- Escriba el resultado a la carpeta `output` del directorio actual.
-- 
fs -rm -f -r output;
--
-- >>> Escriba su respuesta a partir de este punto <<<
--
datos = LOAD 'data.tsv' AS (upper_case:CHARARRAY, lower_case:BAG{tup:TUPLE(letter:CHARARRAY)},obs:MAP[]);

datos = FOREACH datos GENERATE FLATTEN(obs) AS obs;

agrupacion = GROUP datos BY obs;

cuenta_letras = FOREACH agrupacion GENERATE group, COUNT($1);

STORE cuenta_letras INTO 'output' USING PigStorage(',');
