# MaestriaSwBI
Proyecto BI-Análisis de Sentimientos
PROYECTO 
DISEÑO E IMPLEMENTACION DE UN SISTEMA CLASIFICADOR DE SENTIMIENTOS
Daniel Viera, Geovanna Chela, Edwin Patiño
===============================================================================================================

PROCESO:
1. Archivo inicial de comentarios para entrenamiento y pruebas.

2. Análisis y obtención de atributos que describan el comportamiento del problema
-	Sustantivos (sust)
-	Adjetivos (adjet)
-	Verbos (verb)
-	Total palabras (total_pal)
-	Polaridad Oración (pol_ora): Tarea que pretende clasificar fragmentos de texto, en positivo o negativo dependiendo de su significado emocional
-	Calificación Adjetivo (calif_adj)
-	Calificación (calif)

3. Proceso de limpieza de archivo (eliminación de palabras de la lista negra, eliminación de palabras menores a tres caracteres y eliminación de instancias vacías)

4. Una vez limpio el data set de etrenamiento dividimos en:
-       75% de datos para entrenamiento
-       25% de datos para pruebas

5. Se procede a generar el diccionario de palabras (adjetivos), con su respectiva polaridad.

6. Se procede a generar de data set de entrenamiento considerando el data set, atributos (con sus respectivos pesos) y diccionario.

7. Entrenamos nuestro data set en Weca para diferente número de instancias


PREGUNTAS:
1. Cuando se alcanza la mejor precisión?
Se alcanza la mejor precisión cuando se definen los atributos más relevantes, aquellos que encierran la solución del problema, además cuando se dispone de un dataset de entrenamiento con el mayor de número de instancias posibles, siempre y cuando dicho dataset sea limpio y en lo posible no provoque ruido ni overfitted.

2. ¿Es importante el número de atributos (features) en el clasificador?  
La cantidad de atributos en el clasificador no define la precisión  de un sistema de aprendizaje, lo que es importante es saber que atributos hay que considerar para que describan de una forma global el problema, es decir, al incluir en el conjunto de entrenamiento atributos irrelevantes para el problema, atributos que no tendrá ninguna relación con las categorías y que únicamente aportarán ruido al aprendizaje.
En segundo lugar, cuando el número de atributos es muy elevado, los recursos necesarios (de tiempo y memoria) pueden hacer inviable el proceso de aprendizaje. Esta situación suele darse a menudo en casos prácticos donde se dispone de gran cantidad de información no organizada de la que se quiere extraer conocimiento.

3. Es importante el número de Instancias?
Es mucho mejor cuando se dispone de un dataset de entrenamiento con el mayor de número de instancias posibles, siempre y cuando dicho conjunto de datos sea limpio, considera la mayor variedad de posibilidades en cuanto al objetivo del proyecto y en lo posible no provoque ruido, ya que de esta manera nuestro sistema de aprendizaje tendrá un mayor número de posibilidades  y así podrá dar un mejor grado de precisión a la hora de clasificar un archivo.

4. ¿Es importante considerar diferentes pesos para cada atributo? ¿por qué?
Si es importante considerar diferentes pesos para diferentes atributos, ya que el mismo puede ayudar a mejorar el grado de precisión, sin embargo hay que tener en cuenta la amplia gama de intensificadores dentro de una misma subcategoría, siendo que no todos los cuantificadores intensifican o disminuyen de la misma manera. Por ejemplo, extraordinariamente es un amplificador mucho más fuerte que bastante o no sería lo mismo “realmente fantástico” que “realmente bien”. La intensificación debe depender también del término que se intensifica.

5. ¿Está su modelo sobreajustado “overfitted”? 
Nuestro sistema queda sobreajustado a las características específicas de los datos de entrenamiento por tal razón el modelo no es tan generalizado.

6. ¿Los atributos continuos son mejores o peores en el clasificador Naive Bayes? 
Hay que considerar que cuando los atributos son continuos y se utiliza el clasificador de Bayes, es necesario discretizar (dividir cada una de las zonas en N y M intervalos respectivamente, e ir analizando la función en esos puntos concretos) dichos datos.
El método de discretización tiende a ser mejor si hay una gran cantidad de datos de entrenamiento, ya que va a aprender para adaptarse a la distribución de los datos, sin embargo el proceso de discretizar puede afectar el rendimiento del clasificador

7.Comparar los diferentes algoritmos con su conjunto de datos y determinar cuál de ellos es el que mejor
Naives 99.2625 %
J48    99.41   % 
LMT    98.8201 %

El valor más alto es J48, sin embargo, no es posible determinar cual es mejor sin conocer más profundamente la teoría que implica cada uno de los algoritmos utilizados.

8. ¿Es mejor utilizar validación cruzada (cross-validation) o un test dataset para realizar la evaluación del clasificador? ¿Por qué? 
El método entrenamiento/test tiene el problema de tener una alta variabilidad si el tamaño del conjunto es pequeño, por lo que se recomienda el uso de la validación cruzada que es una especie de entrenamiento/test repetido en el que las particiones de test nunca solapan. De hecho, todos los datos figuran como entrenamiento o test en alguno de los ciclos de validación cruzada. Las particiones de test de los distintos ciclos son independientes (no solapan)
=======================================================================================================================================

DISCUSIÓN DE PRUEBAS
1. De 678 instancias se dispone 177 positivos,  87 negativos y 414 neutros por tal razón los datos considerados en nuestro training set contiene datos neutrales en su mayor porcentaje por tal razón puede verse sesgado el análisis con un nuevo test set.
2. Se dispone de un 99.2625 % con Naives siendo el atributo con mayor peso los atribuos de polaridad los cuales disminuyen a  66.0767 %.
3. Se disponde de 10 en cross validation de un total de 678 instancias que no se ven afectadas al ser modificadas (overfitting).
4. Se obtiene 5 instancias incorrectas.

=======================================================================================================================================

CONCLUSIONES

1. El modelo al no estar generalizado no tiene un alto grado de predicción ante un conjunto nuevo, por lo que se podría aplicar a futuro otros ámbitos de análisis de sentimentos como tweeter que nos puede dar un rango más exacto de precisión.
2. Los atributos seleccionados fueron considerados en base a teoría y se requiere un alto grado de conocimiento y estudios matemáticos que permitan definir de mejor manera dichas características.
3. El modelo no considera en la oración el análisis de negatividad por tal razón afectó la clasificación de estas oraciones.
4. Al no efectuarse un test de nuestro modelo queda sesgada el análisis en datos reales. Sólo se obtiene el % de entrenamiento utilizando el cross-validation.


=======================================================================================================================================

INSTALACION

Para el correcto funcionamiento de nuestra aplicación se debe seguir las siguientes instrucciones:
1.Crear el archivo de entrenamiento con el nombre: texto_proy.txt
2.Desde Python, ejecutar el archivo limpieza_datos.py el mismo que nos permitirá limpiar dicho archivo (eliminación de palabras de la lista negra, eliminación de palabras menores a tres caracteres y eliminación de instancias vacías), dicha función nos generará un nuevo archivo que se denomina Archivo_limpio.txt
3.Ejecutando el archivo generar_diccionario.py el mismo que genera el diccionario de palabras (adjetivos), con su respectiva polaridad (para esta fusión internamente considerará el archivo limpio generado) (dic_adjfinal.txt). Dicho archivo generado es necesario aumentar al inicio del texto los caracteres  { “ y al final eliminar los caracteres , " y aumenta el carácter } 
4.Ejecutar el archivo generador_data_set_entrenamiento.py el mismo que en su implementación considera:
	-Toma las palabras de las diferentes instancias, comparándolas con el diccionario de datos creado previamente, generando así una calificación a la instancia de acuerdo a la polaridad de los adjetivos encontrados.
	-A estos resultados obtenidos se suma los valores de los diferentes atributos.
	-Para la clasificación se toma los valores obtenidos previamente, de la siguiente manera: si la suma es mayor que cero  la clase será positiva; si la suma es igual a cero la clase será neutro; si la sumatoria da un valor menor a cero la clasificación será negativa.

=========================================================================================================================================
