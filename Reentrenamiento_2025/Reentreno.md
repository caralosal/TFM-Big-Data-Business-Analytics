# Tu modelo de IA también envejece: La importancia del reentrenamiento de modelos

## 1. Introducción

- ¿Cómo podemos saber si un modelo de machine learning sigue siendo fiable con el paso del tiempo?
- Una vez que ponemos en producción un modelo, ¿podemos confiar en que seguirá ofreciendo buenos resultados sin intervención?
- Si los datos cambian constantemente, ¿por qué esperar que un modelo siga funcionando igual?

Si alguna vez has trabajado con modelos en producción, seguro que estas preguntas te resultan familiares. **La realidad es que los modelos de machine learning no son estáticos**: con el tiempo, los datos evolucionan y su rendimiento puede degradarse debido a fenómenos como el data drift y el concept drift.

El **objetivo** de este estudio es:

+ Demostrar la **importancia de monitorear las métricas** de un modelo para detectar su degradación.
+ Evidenciar la **necesidad de reentrenamiento** para mantener su precisión.
+ **Cuantificar el impacto** del paso del tiempo en la calidad de las predicciones.

Para ello, analizaré un **caso concreto: un modelo de predicción del precio de la luz en España** que desarrollé en 2021. Compararé su desempeño en dos momentos clave:

+ Predicción del precio de la luz con datos de 2021, que compone el **modelo original**.
+ Uso del mismo modelo para predecir el precio en 2025, **sin reentrenamiento**.
+ **Reentrenamiento** del modelo con datos actualizados para evaluar la mejora.

A través de este análisis, veremos cómo las correlaciones entre variables y las distribuciones de las mismas han cambiado con el tiempo y por qué es fundamental actualizar los modelos para mantener su precisión.

## 2. Modelo original - Predicciones en 2021

**El objetivo del modelo original fue el de la predicción del precio de la luz a nivel horario en España en 2021**. Para realizar la comparación, nos quedamos con el mes de enero de 2021 para que la comparación sea directa. Tras una serie de pruebas, se obtuvo un modelo de XGBoost. Las métricas arrojadas por este modelo en el primer mes de 2021 fueron de un **WAPE del 19.52%**. Visualmente, se puede ver en el siguiente gráfico.

![alt text](https://github.com/caralosal/TFM-Big-Data-Business-Analytics/blob/master/Reentrenamiento_2025/grafico_2021.png?raw=true)


## 3. Modelo original sin reentrenamiento - Predicciones en 2025

¿Cómo habría funcionado este modelo en la actualidad?
En esta sección, utilizamos el modelo entrenado con datos de 2021 para realizar predicciones sobre los datos de enero de 2025. ¿Qué resultados podríamos esperar?

El modelo original obtiene un **WAPE del 46.78%** sobre el conjunto de datos de 2025, lo que significa que su precisión se ha reducido significativamente. En otras palabras, **su error es aproximadamente 2.5 veces mayor que en 2021**. Este deterioro en el rendimiento se puede observar claramente en el siguiente gráfico.

![alt text](https://github.com/caralosal/TFM-Big-Data-Business-Analytics/blob/master/Reentrenamiento_2025/grafico_2025_sin_reentrenamiento.png?raw=true)


## 4. Modelo reentrenado - Predicciones en 2025

¿Qué pasaría si reentrenamos el modelo con los datos más recientes? En esta sección, utilizamos los datos más recientes para reentrenar el modelo y evaluar su desempeño en el mes de enero de 2025. ¿Cuál sería el resultado?

**Gracias al reentrenamiento, el modelo logra recuperar el nivel de precisión que tenía en 2021**, alcanzando un **WAPE del 19.50%**, prácticamente igual al obtenido con el mejor modelo original. Este resultado refuerza la importancia de actualizar los modelos periódicamente para evitar la degradación de su rendimiento.

![alt text](https://github.com/caralosal/TFM-Big-Data-Business-Analytics/blob/master/Reentrenamiento_2025/grafico_2025_reentrenamiento.png?raw=true)

## 5. Data Drift y Concept Drift

El objetivo de esta sección es darle sentido a los resultados anteriores. Los resultados del modelo han empeorado sin el reentrenamiento pero, tras el reentrenamiento, han vuelto prácticamente al mismo valor de error que cuando se diseñó (un 19.5%). **¿Cómo ha ocurrido esto?** Para entenderlo, hay que introducir los siguientes conceptos.

### 5.1. Data Drift

Se produce **data drift** cuando se dan **cambios en la distribución de las variables de entrada del modelo de Machine Learning a lo largo del tiempo**. Puede darse por determinados motivos
+ Que los datos hayan sido recopilados en diferentes periodos de tiempo 
+ Que haya datos que provengan de distintas fuentes
+ Que el proceso de recopilación de los datos sea diferente y genere ciertas inconsistencias.

En este caso, estamos comparando 2021 con 2025, así que el data drift se produce por la **recopilación de datos en diferentes periodos de tiempo**.

Para visualizar el **data drift**, puedes observar los siguientes tres gráficos, en los que vamos a comparar las distribuciones en 2021 y 2025 del precio de la luz, el precio del gas y el spread del precio (calcula la diferencia entre el precio máximo y mínimo en el precio de la luz en un mismo día)

#### 5.1.1. Data drift en el precio de la luz

En primer lugar, analizamos la propia variable objetivo. Aquí encontramos la primera diferencia clave. La media de la variable objetivo ha pasado de 45€/MWh en enero de 2021 a 120€/MWh en enero de 2025. Otra diferencia es la volatilidad, mientras que en 2021 había poca desviación (casi todos los precios estaban concentrados en su media) en 2025, hay un amplio abanico de precios a lo largo de todo el mes, aumentando mucho la volatilidad.

![alt text](https://github.com/caralosal/TFM-Big-Data-Business-Analytics/blob/master/Reentrenamiento_2025/target.png?raw=true)

#### 5.1.2. Data drift en el precio del gas

El precio del gas es una variable muy correlada positiva con la variable objetivo, esto es, cuanto más caro esté el gas, más caro será el precio de la luz. Analizando el siguiente gráfico, se observa una diferencia muy notable en las distribuciones. Las distribuciones están perfectamente separadas de 2021 a 2025, el precio del gas se ha triplicado

![alt text](https://github.com/caralosal/TFM-Big-Data-Business-Analytics/blob/master/Reentrenamiento_2025/gas.png?raw=true)

#### 5.1.3. Data drift en el spread del precio

Otra variable interesante que ha modificado mucho su valor respecto 2021 es el spread del precio. Esta variable representa la diferencia del precio de la luz de una hora a otra, es decir, es una especie de la medida de la volatilidad, ya que recoge la diferencia de precio de una hora y otra. Como vemos, en 2025 hay mucha más volatilidad en estos precios, también relacionado con que los precios son más altos, la variación de precios también está siendo más alto

![alt text](https://github.com/caralosal/TFM-Big-Data-Business-Analytics/blob/master/Reentrenamiento_2025/spread_precio.png?raw=true)

### 5.2. Concept drift
Por otra parte, existe el **concept drift**. En él, nos estamos refiriendo a **cambios en la relación entre las variables de entrada y la variable objetivo**. Aquí, incluso si la distribución de las variables de entrada no se ve alterada, sí lo hacen las reglas que definen el comportamiento global del sistema con el paso del tiempo. El modelo entrenó con unos determinados datos en 2021, en el que las variables tenían determinadas relaciones, estas relaciones se han modificado ligeramente en 2025, incurriendo en el **concept drift**.

Para visualizar el **concept drift**, puedes observar los siguientes gráficos comparando las correlaciones existentes en 2021 y en 2025:

![alt text](https://github.com/caralosal/TFM-Big-Data-Business-Analytics/blob/master/Reentrenamiento_2025/cambio_correlaciones_1.png?raw=true)

![alt text](https://github.com/caralosal/TFM-Big-Data-Business-Analytics/blob/master/Reentrenamiento_2025/cambio_correlaciones_2.png?raw=true)

Como vemos, hay variaciones bastante notables entre las correlaciones de las variables explicativas y la variable objetivo. Entre ellas, destacamos:
- MIBGAS (precio del gas): ha evolucionado de 0.50 en 2021 a 0.32 en 2025
- Previsión de generación eólica y fotovoltaica: ha fluctuado de -0.32 en 2021 a -0.67 en 2025
- Previsión de la demanda de energía: ha tenido una desviación de 0.58 a 0.39
- Precio de la luz de la semana anterior: se ha modificado de 0.58 a 0.35

## 6. Conclusiones

Los resultados de este estudio confirman la importancia del reentrenamiento y monitoreo continuo en modelos de machine learning en producción. Como se observa en la siguiente tabla, el modelo entrenado en 2021 experimentó una degradación significativa cuando se aplicó a datos de 2025, aumentando su error de un WAPE del 19.52% a un 46.78%. Sin embargo, al actualizarlo con datos recientes, el modelo recuperó su precisión original, reduciendo nuevamente el error al 19.50%.

<div align="center">

| Modelo | Datos  | WAPE (%) |
|:------:|:------:|:--------:|
|  2021  |  2021  |  19.52   |
|  2021  |  2025  |  46.78   |
|  2025  |  2025  |  19.50   |

</div>

A partir de estos resultados, se pueden extraer las siguientes conclusiones clave:

✅ **El reentrenamiento es fundamental**: Hemos demostrado que un modelo antiguo puede volverse ineficaz con el tiempo, pero al actualizarlo con datos recientes, recupera su rendimiento original.

✅ **Evidencia cuantitativa y visual del impacto del reentrenamiento**: Los resultados muestran no solo numéricamente sino también de manera gráfica cómo el modelo se degrada sin mantenimiento y cómo se recupera tras el reentrenamiento.

✅ **El data drift es un factor crítico a monitorear**: A lo largo del tiempo, la relación entre las variables explicativas y la variable objetivo cambia, lo que afecta la precisión del modelo. Por ello, es crucial implementar sistemas de monitoreo que alerten sobre estos cambios y permitan la actualización del modelo de manera proactiva.

✅ **No podemos asumir que un modelo funcionará indefinidamente**: Incluso un modelo que fue altamente preciso en su momento puede volverse obsoleto si no se revisa periódicamente. El mantenimiento activo es clave para garantizar su eficacia a largo plazo.

## 7. Fuentes de datos
- https://www.esios.ree.es/es/analisis/600?vis=1&start_date=01-01-2021T00%3A00&end_date=30-11-2021T23%3A00&compare_start_date=31-12-2020T00%3A00&groupby=hour&geoids=3
- https://www.mibgas.es/es/file-access
- https://www.esios.ree.es/es/analisis/1775?vis=1&start_date=06-10-2016T00%3A00&end_date=31-12-2021T23%3A50&compare_start_date=05-10-2016T00%3A00&groupby=hour
- https://www.esios.ree.es/es/analisis/10358?vis=1&start_date=01-10-2015T00%3A00&end_date=31-12-2021T23%3A50&compare_start_date=30-09-2015T00%3A00&groupby=hour
- https://datos.madrid.es/portal/site/egob/menuitem.c05c1f754a33a9fbe4b2e4b284f1a5a0/?vgnextoid=fa8357cec5efa610VgnVCM1000001d4a900aRCRD&vgnextchannel=374512b9ace9f310VgnVCM100000171f5a0aRCRD&vgnextfmt=default

