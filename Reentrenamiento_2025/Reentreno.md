# Reentrenamiento de modelos (Poner nombre más atractivo) 

## 1. Introducción

- Una vez que diseñamos y ponemos en producción cierto modelo de machine learning, ¿podemos despreocuparnos y asumir que obtendremos buenos resultados siempre?
- ¿Es posible que nuestro modelo se degrade con el tiempo y sea necesario un reentrenamiento?

Si alguna vez habéis creado y puesto en producción un modelo de machine learning, las preguntas anteriores os sonarán. Todos sabemos que los modelos se degradan en el tiempo y que no podemos poner un modelo en producción y despreocuparnos. El objetivo del siguiente estudio es:
1. Demostrar la necesidad de monitorear las métricas de un modelo para ver la degradación.
2. Demostrar la necesidad de este reentrenamiento.
3. Cuantificar la degradación de un modelo tras un determiando paso de tiempo.

Hace poco se cumplirán 4 años desde que presenté mi TFM. El objetivo era la predicción del precio de la luz en España a nivel horario. En el presente estudio, evidenciaré la necesidad de reentrenamiento de modelos, el concepto de data drift y cómo varían las correlaciones de las variables explicativas con la variable objetivo con el tiempo

Para realizar este análisis, se van a realizar una serie de comparaciones.
1. Modelo de predicción del precio de la luz en los dos primeros meses de 2021
2. Usando el modelo anterior, predicción del precio de la luz en los dos primeros meses de 2025
3. Reentrenamiendo del modelo

## 2. Modelo predicción 2021

El objetivo del TFM fue el de la predicción del precio de la luz a nivel horario en España. Para realizar la comparación, nos quedamos con los dos primeros meses del año para que la comparación sea directa. Tras una serie de pruebas, se obtuvo un modelo de XGBoost. Las métricas arrojadas por este modelo en los dos primeros meses de 2021 fueron de un WAPE del 19.52%. Visualmente, se puede ver en el siguiente gráfico.

(Señalar el 19.52%)

![alt text](https://github.com/caralosal/TFM-Big-Data-Business-Analytics/blob/master/Reentrenamiento_2025/grafico_2021.png?raw=true)


## 3. Predicciones 2025 con modelo de 2021

¿Cómo se hubiera comportado este modelo en la actualidad?
En esta sección, guardamos el modelo de la sección anterior y realizamos predicciones con los datos de enero y febrero de 2025. ¿Qué resultados cabría esperar?
El modelo anterior hubiese arrojado un 46.78% de WAPE. Esto es igual a decir, que el modelo es, aproximadamente, **2.5 veces peor que en 2021**. Visualmente, se puede ver en el siguiente gráfico.

(Señalar el 46.78%)

![alt text](https://github.com/caralosal/TFM-Big-Data-Business-Analytics/blob/master/Reentrenamiento_2025/grafico_2025_sin_reentrenamiento.png?raw=true)


## 4. Predicciones 2025 con modelo 2025

Si realizamos entrenamiento, ¿cómo se hubiera comportado este modelo entrenando con los últimos datos disponibles?
En esta sección, obtenemos los últimos datos disponibles, entrenamos con ellos y realizamos las predicciones sobre los dos primeros meses de enero y febrero de 2025. ¿Qué resultados cabría esperar?
Con un reentrenamiento del modelo, volvemos a recuperar las métricas obtenidas del mejor modelo de 2021, un WAPE del 19.50%

(Señalar el 19.50%)

![alt text](https://github.com/caralosal/TFM-Big-Data-Business-Analytics/blob/master/Reentrenamiento_2025/grafico_2025_reentrenamiento.png?raw=true)

## 5. Data Drift

El objetivo de esta sección es darle sentido a los resultados anteriores. Los resultados del modelo han empeorado sin el reentrenamiento pero, tras el reentrenamiento, han vuelto prácticamente al mismo valor de error que cuando se diseñó (un 19.5%). ¿Cómo ha ocurrido esto?
Para entenderlo, hay que introducir los siguientes conceptos.

(Hablar concepto data drift y correlaciones)

El modelo entrenó con unos determinados datos en 2021, en el que las variables tenían determinadas relaciones, estas relaciones se han modificado ligeramente, además de que los modelos no son perfectos.

(Hacer gráfico más bonito para visualizar la variación de correlaciones entre 2025 y 2021)

(Concepto de data drift.)

Para visualizarlo, puedes observar los siguientes gráficos:

En primer lugar, analizamos la propia variable objetivo. Aquí encontramos la primera diferencia clave. La media de la variable objetivo ha pasado de 45€/MWh en enero de 2021 a 120€/MWh en enero de 2025. Otra diferencia es la volatilidad, mientras que en 2021 había poca desviación (casi todos los precioes estaban concentrados en su media) en 2025, hay un amplio abanico de precios a lo largo de todo el mes, aumentando mucho la volatilidad 

![alt text](https://github.com/caralosal/TFM-Big-Data-Business-Analytics/blob/master/Reentrenamiento_2025/target.png?raw=true)

Como hemos visto en gráficos de correlaciones anteriores, el precio del gas es una variable muy correlada positiva con la variable objetivo, esto es, cuanto más caro esté el gas, más caro será el precio de la luz. Analizando el siguiente gráfico, se observa una diferencia muy notable en las distribuciones. Las distribuciones están perfectamente separadas de 2021 a 2025, el precio del gas se ha triplicado

![alt text](https://github.com/caralosal/TFM-Big-Data-Business-Analytics/blob/master/Reentrenamiento_2025/gas.png?raw=true)

Otra variable interesante que ha modificado mucho su valor respecto 2021 es el spread del precio. Esta variable representa la diferencia del precio de la luz de una hora a otra, es decir, es una especie de la medida de la volatilidad, ya que recoge la diferencia de precio de una hora y otra. Como vemos, en 2025 hay mucha más volatilidad en estos precios, también relacionado con que los precios son más altos, la variación de precios también está siendo más alto

![alt text](https://github.com/caralosal/TFM-Big-Data-Business-Analytics/blob/master/Reentrenamiento_2025/spread_precio.png?raw=true)

## 6. Conclusiones

La siguiente tabla resume los resultados obtenidos en este estudio:
| Modelo | Datos  | WAPE (%) |
|-----:|-----------|
|   2021  |  2021|19.52|
|     2021| 2025 |46.78    |
|     2025| 2025 |19.50       |

Como cabría esperar, el reentrenamiento del modelo y el monitoreo tanto de las variables como de las métricas de performance es algo crítico a la hora de diseñar y mantener un modelo, en el presente estudio se ha demostrado el impacto que puede llegar a tener y se ha cuantificado.

- Destacar cómo se ha vuelto a obtener las mismas métricas de error con el reentrenamiento que había inicialmente
- Demostración visual y cuantitativa del efecto de reentreno
- El data drift es algo que hay que monitorear y tener en cuenta en el mantenimiento de los modelos