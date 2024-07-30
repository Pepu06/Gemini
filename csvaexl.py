import pandas as pd

# Ruta al archivo CSV de entrada y al archivo de Excel de salida
csv_file_path = 'resultados.csv'  # Reemplaza con la ruta correcta a tu archivo CSV
excel_file_path = 'output.xlsx'  # Reemplaza con la ruta donde quieres guardar el archivo de Excel

# Leer el archivo CSV con un delimitador '|'
with open(csv_file_path, 'r', encoding='utf-8') as file:
    lines = file.readlines()

# Procesar las líneas para crear un DataFrame
data = [line.strip().split('|', 1) for line in lines]
df = pd.DataFrame(data, columns=['Entrada', 'Salida'])

# Guardar el DataFrame como un archivo de Excel
df.to_excel(excel_file_path, index=False)

print("Proceso completado. El archivo de Excel se ha guardado en 'output.xlsx'.")
