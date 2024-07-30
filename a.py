import pandas as pd
import re

# Cargar el archivo CSV
file_path = 'mati.csv'  # Reemplaza con la ruta correcta a tu archivo
data = pd.read_csv(file_path, delimiter="|")

# Función para eliminar emojis
def eliminar_emojis(texto):
    emoji_pattern = re.compile(
        "["
        u"\U0001F600-\U0001F64F"  # emoticons
        u"\U0001F300-\U0001F5FF"  # symbols & pictographs
        u"\U0001F680-\U0001F6FF"  # transport & map symbols
        u"\U0001F1E0-\U0001F1FF"  # flags (iOS)
        u"\U00002700-\U000027BF"  # Dingbats
        u"\U000024C2-\U0001F251" 
        "]+", flags=re.UNICODE)
    return emoji_pattern.sub(r'', texto)

# Crear una función para generar las divisiones de oraciones
def generar_divisiones(oracion):
    oracion_sin_emojis = eliminar_emojis(oracion)
    palabras = oracion_sin_emojis.split()
    divisiones = []
    for i in range(1, len(palabras) + 1):
        entrada = ' '.join(palabras[:i])
        salida = ' '.join(palabras[i:])
        divisiones.append(f"{entrada}|{salida}")
    return divisiones

# Aplicar la función a cada oración en la columna 'text'
resultados = []
for oracion in data['text']:
    divisiones = generar_divisiones(oracion)
    resultados.extend(divisiones)

# Convertir los resultados en un DataFrame
resultados_df = pd.DataFrame(resultados, columns=['Entrada|Salida'])

# Guardar los resultados en un nuevo archivo CSV
resultados_df.to_csv('resultados.csv', index=False)  # Reemplaza con la ruta donde quieres guardar el archivo

print("Proceso completado. Los resultados se han guardado en 'resultados.csv'.")
