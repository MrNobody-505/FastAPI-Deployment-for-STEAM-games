# Proyecto - STEAM

Hola, soy César Forero!
Este es mi proyecto que he realizado como parte de mi primer proyecto individual para el programa de estudios de HENRY.

## Descripción preliminar
La base del proyecto radica en la implementación de una API con el objetivo de que los usuarios puedan consultar información relevante acerca de la plataforma Steam y los servicios que ofrece, la cual fue desarrollada por Valve corporation, empresa del sector de la tecnología y enfocada principalmente en el nicho de la distribución digital de videojuegos.

## Descripción del trabajo desarrollado
1. Inicialmente se tuvo que realizar la ingesta de los datos a mi entorno de trabajo y preparar las librerías que utilizaría para poder manejar los archivos entregados por la compañía. dichas librerías son pandas, ast y json.
2. Posteriormente se realiza un Análisis Exploratorio de Datos o EDA (Exploratory Data Analysis) con el objetivo de poder visualizar de la manera más práctica posible la información recogida de los archivos JSON que nos otorgaba la compañía.
3. Se realiza entonces un tratamiento de datos con el fin de limpiar datos que entorpecían el análisis (duplicados, NaN, outliers y vacíos).
4. una vez tenemos una clara idea de la información relevante, se procede a limpiar los datasets y dejar unicamente lo estrictamente necesario, haciendo "drops" de columnas para reducir el tamaño de los archivos.
5. Se realizan joins/merges de algunos datasets con el objetivo de establecer relaciones para llegar a conclusiones.
6. Se implementa un modelo de ML ya establecido conocido como "sentiment_analysis".
7. Se ejecuta con una muestra aleatoria del dataset debido a su excesivo poder de cómputo que se necesita y con base en esto poder realizar las recomendaciones a los usuarios.
8. Posteriormente se desarrollan algunas funciones como PlayTimeGenre, UserForGenre, UsersRecommend, UsersNotRecommend y sentiment_analysis; las cuales nos otorgan información relevante del negocio la cual es facilmente accesible desde un endpoint.
9. Finalmente se implementa una API gracias al framework FastAPI y se disponibiliza públicamente a través de [Render.com](https://api-steam-henry-proyecto1.onrender.com/)

## Resultados
Se puede acceder a la siguiente dirección con el fin de acceder a los resultados de lo mencionado anteriomente:
 - https://api-steam-henry-proyecto1.onrender.com/
 - https://api-steam-henry-proyecto1.onrender.com/docs#/default/index__get
 - https://github.com/MrNobody-505/Proyecto1
