--
-- Pregunta
-- ===========================================================================
-- 
-- El archivo `truck_event_text_partition.csv` tiene la siguiente estructura:
-- 
--   driverId       INT
--   truckId        INT
--   eventTime      STRING
--   eventType      STRING
--   longitude      DOUBLE
--   latitude       DOUBLE
--   eventKey       STRING
--   correlationId  STRING
--   driverName     STRING
--   routeId        BIGINT
--   routeName      STRING
--   eventDate      STRING
-- 
-- Escriba un script en Pig que carge los datos y obtenga los primeros 10 
-- registros del archivo para las primeras tres columnas, y luego, ordenados 
-- por driverId, truckId, y eventTime. 
--
-- Escriba el resultado a la carpeta `output` del directorio actual.
-- 
fs -rm -f -r output;
-- 
--  >>> Escriba su respuesta a partir de este punto <<<
-- 
datos = LOAD 'truck_event_text_partition.csv' USING PigStorage(',') AS (driverId:INT,
   truckId:INT,
   eventTime:CHARARRAY,
   eventType:CHARARRAY,
   longitude:DOUBLE,
   latitude:DOUBLE,
   eventKey:CHARARRAY,
   correlationId:CHARARRAY,
   driverName:CHARARRAY,
   routeId:BIGINTEGER,
   routeName:CHARARRAY,
   eventDate:CHARARRAY);

datos = LIMIT datos 10;

datos = FOREACH datos GENERATE driverId,truckId,eventTime;

datos = ORDER datos BY driverId,truckId,eventTime;

STORE datos INTO 'output'  USING PigStorage(',');
