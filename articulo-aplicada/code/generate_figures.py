#!/usr/bin/env python3
"""
Script para generar todas las figuras del artículo sobre patrones de diseño
y buenas prácticas en el desarrollo del sistema AutoGestión SENA.

Genera gráficas en formato PDF (para LaTeX) y PNG (para previsualización).
"""

import matplotlib.pyplot as plt
import matplotlib.patches as patches
import numpy as np
from pathlib import Path

# Configuración de estilo
plt.style.use('seaborn-v0_8-darkgrid')
plt.rcParams['font.family'] = 'DejaVu Sans'
plt.rcParams['font.size'] = 10
plt.rcParams['axes.labelsize'] = 11
plt.rcParams['axes.titlesize'] = 12
plt.rcParams['xtick.labelsize'] = 9
plt.rcParams['ytick.labelsize'] = 9
plt.rcParams['legend.fontsize'] = 9
plt.rcParams['figure.titlesize'] = 13

# Crear directorios si no existen
GRAPHICS_DIR = Path('../graphics')
GRAPHICS_DIR.mkdir(exist_ok=True)

# Colores del tema
COLOR_ANTES = '#e74c3c'  # Rojo
COLOR_DESPUES = '#27ae60'  # Verde
COLOR_NEUTRO = '#3498db'  # Azul
COLOR_ACENTO = '#f39c12'  # Naranja


def save_figure(fig, filename):
    """Guarda la figura en PDF y PNG."""
    pdf_path = GRAPHICS_DIR / f'{filename}.pdf'
    png_path = GRAPHICS_DIR / f'{filename}.png'
    
    fig.savefig(pdf_path, format='pdf', bbox_inches='tight', dpi=300)
    fig.savefig(png_path, format='png', bbox_inches='tight', dpi=150)
    print(f'✓ Generada: {filename}')


def figura_arquitectura_capas():
    """Genera diagrama de arquitectura en capas."""
    fig, ax = plt.subplots(figsize=(8, 6))
    
    capas = [
        'ViewSet\n(Capa de Vista)',
        'Service\n(Capa de Negocio)',
        'Repository\n(Capa de Datos)',
        'Serializer\n(Transferencia/DTO)',
        'Model\n(Estructura BD)'
    ]
    
    colors = ['#3498db', '#e74c3c', '#f39c12', '#9b59b6', '#1abc9c']
    y_positions = np.arange(len(capas), 0, -1)
    
    for i, (capa, color, y) in enumerate(zip(capas, colors, y_positions)):
        rect = patches.FancyBboxPatch(
            (0.1, y - 0.4), 0.8, 0.8,
            boxstyle="round,pad=0.05",
            linewidth=2,
            edgecolor='black',
            facecolor=color,
            alpha=0.7
        )
        ax.add_patch(rect)
        ax.text(0.5, y, capa, ha='center', va='center', 
                fontsize=11, fontweight='bold', color='white')
        
        # Flechas entre capas
        if i < len(capas) - 1:
            ax.arrow(0.5, y - 0.5, 0, -0.3, 
                    head_width=0.08, head_length=0.08,
                    fc='gray', ec='gray', linewidth=2)
    
    ax.set_xlim(0, 1)
    ax.set_ylim(0, len(capas) + 0.5)
    ax.axis('off')
    ax.set_title('Arquitectura en Capas del Sistema AutoGestión SENA', 
                 fontsize=13, fontweight='bold', pad=20)
    
    save_figure(fig, 'arquitectura_capas')
    plt.close()


def figura_tiempos_respuesta():
    """Genera gráfica comparativa de tiempos de respuesta."""
    fig, ax = plt.subplots(figsize=(10, 6))
    
    operaciones = ['Listar\nInstructores', 'Crear\nAsignación', 
                   'Filtrar\nSolicitudes', 'Dashboard\nAprendiz']
    antes = [850, 1200, 950, 1800]
    despues = [320, 680, 410, 750]
    
    x = np.arange(len(operaciones))
    width = 0.35
    
    bars1 = ax.bar(x - width/2, antes, width, label='Antes', 
                   color=COLOR_ANTES, alpha=0.8)
    bars2 = ax.bar(x + width/2, despues, width, label='Después', 
                   color=COLOR_DESPUES, alpha=0.8)
    
    # Agregar valores sobre las barras
    for bars in [bars1, bars2]:
        for bar in bars:
            height = bar.get_height()
            ax.text(bar.get_x() + bar.get_width()/2., height,
                   f'{int(height)}ms',
                   ha='center', va='bottom', fontsize=9)
    
    ax.set_ylabel('Tiempo de Respuesta (ms)', fontweight='bold')
    ax.set_title('Comparación de Tiempos de Respuesta\nAntes vs Después de Aplicar Patrones',
                fontweight='bold')
    ax.set_xticks(x)
    ax.set_xticklabels(operaciones)
    ax.legend()
    ax.grid(axis='y', alpha=0.3)
    
    save_figure(fig, 'tiempos_respuesta')
    plt.close()


def figura_metricas_codigo():
    """Genera gráfica de métricas de complejidad del código."""
    fig, ax = plt.subplots(figsize=(10, 6))
    
    metricas = ['Líneas por\nFunción', 'Archivos\n>500 líneas', 
                'Código\nDuplicado (%)', 'Cobertura\nTests (%)']
    antes = [85, 12, 35, 0]
    despues = [28, 2, 8, 45]
    
    x = np.arange(len(metricas))
    width = 0.35
    
    bars1 = ax.bar(x - width/2, antes, width, label='Antes', 
                   color=COLOR_ANTES, alpha=0.8)
    bars2 = ax.bar(x + width/2, despues, width, label='Después', 
                   color=COLOR_DESPUES, alpha=0.8)
    
    # Valores sobre barras
    for bars in [bars1, bars2]:
        for bar in bars:
            height = bar.get_height()
            ax.text(bar.get_x() + bar.get_width()/2., height,
                   f'{int(height)}',
                   ha='center', va='bottom', fontsize=9)
    
    ax.set_ylabel('Valor de la Métrica', fontweight='bold')
    ax.set_title('Métricas de Calidad del Código\nAntes vs Después',
                fontweight='bold')
    ax.set_xticks(x)
    ax.set_xticklabels(metricas)
    ax.legend()
    ax.grid(axis='y', alpha=0.3)
    
    save_figure(fig, 'metricas_codigo')
    plt.close()


def figura_evolucion_proyecto():
    """Genera línea temporal de evolución del proyecto."""
    fig, ax = plt.subplots(figsize=(12, 5))
    
    etapas = ['Caos\nInicial', 'Descubrimiento', 'Implementación\nPatrones', 'Refinamiento']
    duracion = [2.5, 4, 10, 6]  # semanas
    calidad = [20, 35, 70, 90]  # calidad estimada (%)
    
    x_pos = np.cumsum([0] + duracion[:-1])
    colors_etapas = ['#e74c3c', '#f39c12', '#3498db', '#27ae60']
    
    for i, (etapa, dur, x, color) in enumerate(zip(etapas, duracion, x_pos, colors_etapas)):
        rect = patches.FancyBboxPatch(
            (x, 10), dur, 80,
            boxstyle="round,pad=0.3",
            linewidth=2,
            edgecolor='black',
            facecolor=color,
            alpha=0.6
        )
        ax.add_patch(rect)
        ax.text(x + dur/2, 50, etapa, ha='center', va='center',
               fontsize=10, fontweight='bold', color='white')
        ax.text(x + dur/2, 95, f'{dur:.1f} sem', ha='center', va='bottom',
               fontsize=8)
    
    # Línea de calidad
    x_calidad = [x + d/2 for x, d in zip(x_pos, duracion)]
    ax.plot(x_calidad, calidad, 'ko-', linewidth=2, markersize=8, 
            label='Calidad del Código', zorder=10)
    
    for x, q in zip(x_calidad, calidad):
        ax.text(x, q + 5, f'{q}%', ha='center', fontsize=9, fontweight='bold')
    
    ax.set_xlim(-1, sum(duracion) + 1)
    ax.set_ylim(0, 105)
    ax.set_xlabel('Tiempo (semanas)', fontweight='bold')
    ax.set_ylabel('Calidad del Código (%)', fontweight='bold')
    ax.set_title('Evolución del Proyecto: De Caos a Código Limpio', 
                fontweight='bold', fontsize=13)
    ax.legend(loc='lower right')
    ax.grid(axis='y', alpha=0.3)
    
    save_figure(fig, 'evolucion_proyecto')
    plt.close()


def figura_distribucion_modulos():
    """Genera gráfica de distribución por módulos."""
    fig, ax = plt.subplots(figsize=(8, 8))
    
    modulos = ['Seguridad\n(35%)', 'Asignaciones\n(40%)', 'General\n(25%)']
    sizes = [35, 40, 25]
    colors = ['#3498db', '#e74c3c', '#27ae60']
    explode = (0.05, 0.1, 0.05)
    
    wedges, texts, autotexts = ax.pie(
        sizes, 
        explode=explode,
        labels=modulos,
        colors=colors,
        autopct='%1.0f%%',
        shadow=True,
        startangle=90,
        textprops={'fontsize': 11, 'fontweight': 'bold'}
    )
    
    for autotext in autotexts:
        autotext.set_color('white')
        autotext.set_fontsize(12)
        autotext.set_fontweight('bold')
    
    ax.set_title('Distribución de Funcionalidades por Módulo', 
                fontweight='bold', fontsize=13, pad=20)
    
    save_figure(fig, 'distribucion_modulos')
    plt.close()


def figura_comparacion_codigo():
    """Genera gráfica comparando complejidad del código."""
    fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(12, 5))
    
    # Antes: muchas líneas y alta complejidad
    categorias_antes = ['Lógica\nNegocio', 'Consultas\nBD', 'Validación', 
                        'Respuesta\nHTTP', 'Otros']
    valores_antes = [35, 25, 15, 15, 10]
    
    ax1.pie(valores_antes, labels=categorias_antes, autopct='%1.0f%%',
           colors=['#e74c3c', '#c0392b', '#e67e22', '#d35400', '#95a5a6'],
           startangle=90, textprops={'fontsize': 9})
    ax1.set_title('ANTES: Todo Mezclado\n(~200 líneas/archivo)', 
                 fontweight='bold', color=COLOR_ANTES)
    
    # Después: separación clara
    categorias_despues = ['ViewSet', 'Service', 'Repository', 
                          'Serializer', 'Model']
    valores_despues = [15, 30, 25, 20, 10]
    
    ax2.pie(valores_despues, labels=categorias_despues, autopct='%1.0f%%',
           colors=['#3498db', '#27ae60', '#f39c12', '#9b59b6', '#1abc9c'],
           startangle=90, textprops={'fontsize': 9})
    ax2.set_title('DESPUÉS: Separación en Capas\n(~50 líneas/archivo)', 
                 fontweight='bold', color=COLOR_DESPUES)
    
    fig.suptitle('Comparación de Organización del Código', 
                fontweight='bold', fontsize=14, y=1.02)
    
    save_figure(fig, 'comparacion_codigo')
    plt.close()


def main():
    """Genera todas las figuras."""
    print('\n🎨 Generando figuras para el artículo...\n')
    
    figura_arquitectura_capas()
    figura_tiempos_respuesta()
    figura_metricas_codigo()
    figura_evolucion_proyecto()
    figura_distribucion_modulos()
    figura_comparacion_codigo()
    
    print(f'\n✅ Todas las figuras generadas en: {GRAPHICS_DIR.absolute()}')
    print('   - Archivos PDF para LaTeX')
    print('   - Archivos PNG para previsualización\n')


if __name__ == '__main__':
    main()
