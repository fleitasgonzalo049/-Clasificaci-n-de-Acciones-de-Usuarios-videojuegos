# Observaciones del estudiante

En esta actividad se utilizaron reglas simples de tipo "si-entonces" para clasificar las acciones de los usuarios de una plataforma de videojuegos.

## ¿Qué reglas funcionaron mejor?

Las reglas que combinan el tipo de acción con el resultado permiten obtener una clasificación más precisa. Por ejemplo, si la acción es "Combate" y el resultado es "Victoria", se clasifica como "Combate exitoso". Si la acción es "Exploración" y el resultado es "Descubrimiento", se clasifica como "Exploración exitosa".

## ¿Qué limitaciones tiene este enfoque?

Las reglas fueron creadas manualmente a partir de un conjunto de datos pequeño. Si aparecen nuevos tipos de acciones o resultados, habría que modificar el programa. Además, las reglas no aprenden automáticamente de nuevos datos.

## ¿Cómo se podría mejorar utilizando machine learning?

Se podría utilizar un modelo de aprendizaje supervisado entrenado con una cantidad mayor de ejemplos previamente clasificados. Algunas alternativas son árboles de decisión, regresión logística, K-Nearest Neighbors (KNN) o Random Forest.

El modelo podría aprender automáticamente relaciones entre características como tipo de acción, duración y resultado, y utilizarlas para clasificar nuevos registros.

## Conclusión

Las reglas simples son útiles cuando el problema es pequeño y las categorías están claramente definidas. Para una plataforma real de videojuegos, con muchos usuarios y comportamientos diferentes, sería más conveniente utilizar un modelo de machine learning entrenado con un conjunto de datos más grande.
