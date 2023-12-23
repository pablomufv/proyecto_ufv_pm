#Práctica Final - proyecto_ufv_pm - Por Pablo Morán

En este servicio de interfaz gráfica tratamos de representar un conjunto de datos y sus diferentes métricas,
     sobre salarios de trabajadores de diferentes empresas a lo largo del mundo, cuya ocupación tiene que ver con 
     la ciencia de datos. Sobre esta misma página, encontrará una barra lateral con diferentes pestañas clicables.

DATOS UTILIZADOS

work_year - El año durante el cual se pagó el salario. Hay dos tipos de valores de año de trabajo:
2020 (Año con un importe definitivo del pasado)
2021e (Año con un importe estimado (por ejemplo, el año en curso))

experience_level - Nivel de experiencia en el puesto durante el año con los siguientes valores posibles:
ES (Entry-level / Junior)
MI (Nivel medio / Intermedio)
SE (Senior / Experto)
EX (Ejecutivo / Director)

employment_type - Tipo de empleo para la función:
PT (A tiempo parcial)
FT (A tiempo completo)
CT (Contrato)
FL (Autónomo)

job_title - Función desempeñada durante el año.

salary - El importe bruto total del salario pagado

salary_currency - La moneda del salario pagado como código de moneda ISO 4217

salary_in_usd - El salario en USD (tipo de cambio dividido por el tipo de cambio medio en USD para el año correspondiente a través de fxdata.foorilla.com)

employee_residence - País de residencia principal del empleado durante el año laboral como código de país ISO 3166

remote_ratio - La cantidad total de trabajo realizado a distancia, los valores posibles son los siguientes:
0 (Sin trabajo a distancia (menos del 20%))
50 (Parcialmente a distancia)
100 (Totalmente a distancia (más del 80%))

company_location - El país de la oficina principal del empleador o de la sucursal contratante como código de país ISO 3166

company_size - Número medio de personas que trabajaron para la empresa durante el año:
S (menos de 50 empleados (pequeña))
M (de 50 a 250 empleados (mediana))
L (más de 250 empleados (grande))

ORIGEN DE LOS DATOS

Estos datos poseen la licencia de CC0:Public Domain y proceden de la página [kaggle](https://www.kaggle.com/datasets/saurabhshahane/data-science-jobs-salaries/data)
