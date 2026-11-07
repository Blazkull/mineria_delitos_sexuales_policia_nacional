Vamos a utilizar el dataset que tenemos en este proyecto en docs/data_set el cual debemos procesar y filtrar por el departamento del atlantico para procesar limpiar datos asi como hicimos en E:\KOOMPATECH\sistema_humedad_capacitiva utilizando strimlit como interfaz de esos datos ya procesado con pandas como se hizo aca E:\IA-UNIVERSIDAD\mineria_delitos_sexuales_policia_nacional\docs\ref\MINERIA_DE_DATOS_Nacidos_Vivos_en_Municipio_de_Bucaramanga.ipynb aca se proceso la informacion y se hizo un dashboard de esos datos en este

como usaremos streamlit ahi se mostraria la informacion toda esa informacion procesada por el backend del aplicativo lo estaremos conectando con una base de datos en supabase donde debemos crear tabla con sus columnas y la informacion
creo que seria una unica tabla con las columnas que tienes el csv y asi montariamos la informacion ya procesada debemos clarificar la fecha en que se realizo la descarga que fue hoy
debemos crear endpoint en supabase para que desde powerse pueda consultar los datos y generar los graficos que se requieran, se mostraria la informacion en diferentes graficos como tablas y graficos de barras y circulares como se hizo en E:\KOOMPATECH\sistema_humedad_capacitiva\dashboard_humedad.pybyi con el fin de poder destacar las graficas y datos para generar un documento investigativo citando las cifras del proyecto
diagram de flujo de los datos E:\IA-UNIVERSIDAD\mineria_delitos_sexuales_policia_nacional\docs\idea\diagrama de como se envia los datos.png

hay unos no negociables que son los siguientes:
Filtrar contenido por la región o departamento que se escogió no se debe borrar ninguna linea

el csv no se procesa se toma de base de dato inicial para procesar la informacion despues con base a eso se exporta el csv ya limpio y ordenado y ahi es donde se subiria la informacion a supabase en la base de datos
