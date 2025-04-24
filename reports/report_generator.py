# Crear reporte con los resultados
from reportlab.lib.pagesizes import letter
from reportlab.platypus import SimpleDocTemplate, Paragraph, Image
from reportlab.lib.styles import getSampleStyleSheet
import plotly.express as px
import pandas as pd

def generate_plotly_report():
    """Crea un reporte interactivo con Plotly desde el CSV"""
    df = pd.read_csv('reports/test_results.csv')
    
    # Crear gráfico Sunburst interactivo
    fig = px.sunburst(
        df,
        path=['Test Class', 'Test Case', 'Resultado'],
        color='Resultado',
        color_discrete_map={'PASS': '#4CAF50', 'FAIL': '#FF5722'},
        hover_data=['Tiempo (s)', 'Error'],
        title='Reporte de Resultados de Pruebas'
    )
    
    # Personalizar layout
    fig.update_layout(
        margin=dict(t=40, l=0, r=0, b=0),
        hoverlabel=dict(
            bgcolor="white",
            font_size=12,
            font_family="Arial"
        )
    )
    
    # Añadir tabla resumen
    summary = df.groupby('Resultado').size().reset_index(name='Count')
    fig.add_annotation(
        x=1.1,
        y=0.5,
        xref='paper',
        yref='paper',
        text=f"<b>Resumen:<br>{summary.to_string(index=False)}</b>",
        showarrow=False,
        align='left',
        bordercolor='black',
        borderwidth=1
    )
    
    # Guardar como HTML interactivo
    fig.write_html("informeInteractivo/interactive_report.html")