import os
import papermill

def ejecutar_notebook(output_path='output.ipynb', output_folder='C:/Users/piece/Documents/ironhack/projects/ih_datamadpt0923_project_m1/data'):
    try:
        # Ejecutar el notebook y guardar en la carpeta de salida
        papermill.execute_notebook(
            'importing_exporting_dfs.ipynb',
            output_path,
            parameters=dict(output_folder=output_folder)
        )
        print(f"El notebook se ejecutó correctamente. Los archivos CSV se guardaron en: {output_folder}")
    except Exception as e:
        print(f"Hubo un error al ejecutar el notebook: {str(e)}")

if __name__ == "__main__":
    # Puedes proporcionar la ruta deseada para la carpeta de salida al llamar a la función
    ejecutar_notebook(output_path='../data/nombre_output.ipynb', output_folder='mi_carpeta_de_salida')