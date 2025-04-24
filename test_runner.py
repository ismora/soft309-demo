# Ejecutar pruebas y generar reporte CSV
import os
import xml.etree.ElementTree as ET
import csv
import pytest
import reports.report_generator


def run_tests():
    """Ejecuta pytest y genera reporte XML"""
    os.makedirs("reports", exist_ok=True)
    ########################################## Código faltante

def generate_test_csv():
    """Genera CSV con los resultados desde el XML de pytest"""
    tree = ET.parse('reports/results.xml')
    root = tree.getroot()

    filePath = "reports/test_results.csv"
    with open(filePath, 'a', newline='') as csvfile:
        writer = csv.writer(csvfile)

        if not os.path.exists(filePath) or os.path.getsize(filePath) == 0:
            writer.writerow(['Test Class', 'Test Case', 'Resultado' , 'Tiempo (s)', 'Error'])
        
        for testcase in root.findall('.//testcase'):
            class_name = testcase.get('classname', 'NoClass')
            test_name = testcase.get('name')
            time = testcase.get('time')

            # Verificar tanto 'error' como 'failure'
            ########################################## Código faltante
            ########################################## Código faltante

            # Determinar resultado
            if error is not None or failure is not None:
                result = "FAIL"
                error_msg = error.get('message') if error is not None else failure.get('message')
            else:
                result = "PASS"
                error_msg = ""
            
            writer.writerow([class_name, test_name, result, time, error_msg])


if __name__ == "__main__":
    print("🏃 Ejecutando pruebas unitarias...")
    run_tests()
    
    print("💾 Generando CSV con resultados...")
    generate_test_csv()
    
    print("📊 Creando reporte visual interactivo...")
    reports.report_generator.generate_plotly_report()
    
    print("✅ Reportes generados:")
    print("- reportes/test_results.csv → Datos crudos de pruebas")
    print("- reportes/interactive_report.html → Reporte Plotly interactivo")

"""
Ejecución

- Instalar las bibliotecas: py -m pip install -r requirements.txt
- Ejecutar las pruebas y generar los resultados: python test_runner.py -v

Ejercicio: Crear otro script de pruebas que contenga al menos una prueba 
"""