# Instrucciones para Compilar el Artículo

## 📄 Sobre el Artículo

**Título:** Desarrollo de un sistema de software basado en patrones de diseño y buenas prácticas de programación

**Autores:**  July Ramos

**Institución:** SENA - Servicio Nacional de Aprendizaje, Colombia

## 🚀 Compilación Rápida

### Opción 1: Con Docker (Recomendado)

```bash
# 1. Compilar todos los formatos (IEEE, ACM, APA7)
.\compile.bat

# O manualmente:
docker compose run --rm latex
```

Los PDFs generados estarán en la carpeta `build/`:
- `build/main_ieee.pdf` - Formato IEEE
- `build/main_acm.pdf` - Formato ACM
- `build/main_apa7.pdf` - Formato APA7

### Opción 2: Sin Docker (si tienes LaTeX instalado)

```bash
# Para IEEE
latexmk -pdfxe -shell-escape -outdir=build main_ieee.tex

# Para ACM
latexmk -pdfxe -shell-escape -outdir=build main_acm.tex

# Para APA7
latexmk -pdfxe -shell-escape -outdir=build main_apa7.tex
```

## 📊 Generar Gráficas

Las gráficas ya están generadas, pero si necesitas regenerarlas:

```bash
cd code
python generate_figures.py
```

Esto creará/actualizará:
- Archivos PDF en `graphics/` (para LaTeX)
- Archivos PNG en `graphics/` (para previsualización)

Gráficas generadas:
1. ✅ `arquitectura_capas.pdf` - Diagrama de arquitectura en capas
2. ✅ `tiempos_respuesta.pdf` - Comparación de tiempos antes/después
3. ✅ `metricas_codigo.pdf` - Métricas de calidad del código
4. ✅ `evolucion_proyecto.pdf` - Línea temporal del proyecto
5. ✅ `distribucion_modulos.pdf` - Distribución por módulos
6. ✅ `comparacion_codigo.pdf` - Comparación de organización del código

## 📁 Estructura del Proyecto

```
articulo-aplicada/
├── sections/              # Secciones del artículo
│   ├── 00_abstract.tex
│   ├── 01_introduccion.tex
│   ├── 02_relacionados.tex
│   ├── 03_metodologia.tex
│   ├── 04_implementacion.tex
│   ├── 05_resultados.tex
│   ├── 06_discusion.tex
│   └── 07_conclusiones.tex
│
├── graphics/              # Gráficas (PDF y PNG)
│   ├── arquitectura_capas.pdf
│   ├── tiempos_respuesta.pdf
│   └── ...
│
├── code/                  # Scripts para generar gráficas
│   └── generate_figures.py
│
├── bibliography/          # Referencias bibliográficas
│   └── references.bib
│
├── includes/              # Preámbulos LaTeX
├── build/                 # PDFs compilados (generado)
│
├── main_ieee.tex          # Documento principal (IEEE)
├── main_acm.tex           # Documento principal (ACM)
├── main_apa7.tex          # Documento principal (APA7)
│
└── compile.bat            # Script de compilación
```

## 📝 Editar el Contenido

### Modificar Secciones

Edita los archivos en `sections/`:
- `00_abstract.tex` - Resumen
- `01_introduccion.tex` - Introducción, problema, objetivos
- `02_relacionados.tex` - Trabajos relacionados
- `03_metodologia.tex` - Metodología, arquitectura, tecnologías
- `04_implementacion.tex` - Implementación, ejemplos de código
- `05_resultados.tex` - Resultados, métricas, gráficas
- `06_discusion.tex` - Discusión, análisis
- `07_conclusiones.tex` - Conclusiones, trabajos futuros

### Modificar Referencias

Edita `bibliography/references.bib` y agrega nuevas referencias en formato BibTeX.

Referencias actuales:
- 📚 Piñero González et al. (2021) - Buenas prácticas
- 📚 Mercado & Zapata (2019) - Gestión de calidad ágil
- 📚 Espinosa & Eraso (2024) - Gestión de tecnología
- 📚 Martin (2008) - Clean Code
- 📚 Beck (2003) - Test-Driven Development
- 📚 Fowler (2006) - Continuous Integration
- 📚 Forsgren et al. (2018) - Accelerate

### Cambiar Autores

Edita `main_ieee.tex`, `main_acm.tex` o `main_apa7.tex`:

```latex
\author{
\IEEEauthorblockN{Tu Nombre\IEEEauthorrefmark{1}}
\IEEEauthorblockA{\IEEEauthorrefmark{1}Tu Institución — \texttt{tu@email.com}}
}
```

## 🔧 Solución de Problemas

### Error: Gráfica no se muestra

Asegúrate de que el archivo existe en `graphics/`:
```bash
ls graphics/
```

Regenera las gráficas:
```bash
cd code
python generate_figures.py
```

### Error: Referencias no aparecen

Compila dos veces para que las referencias se actualicen:
```bash
docker compose run --rm latex
docker compose run --rm latex
```

### Error: Docker no funciona

Verifica que Docker Desktop esté corriendo:
```bash
docker --version
docker compose --version
```

Si no tienes Docker, usa LaTeX local (ver Opción 2 arriba).

## 📊 Vista Previa de Gráficas

Para ver las gráficas antes de compilar, abre los archivos PNG en `graphics/`:
- `arquitectura_capas.png`
- `tiempos_respuesta.png`
- `metricas_codigo.png`
- etc.

## 🎓 Información Académica

Este artículo documenta el desarrollo del **Sistema de AutoGestión SENA**, enfocándose en:
- Transformación de código caótico a código limpio
- Implementación de patrones de diseño (Repository, DTO, Service Layer)
- Aplicación de buenas prácticas de programación
- Mejoras medibles en rendimiento y mantenibilidad

## 📧 Contacto

Para preguntas sobre el proyecto:
- Jesus Ariel
- July Ramos
- SENA - Servicio Nacional de Aprendizaje

---

**¡Éxito con tu artículo!** 🚀

