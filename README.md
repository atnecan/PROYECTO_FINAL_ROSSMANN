# 📊 Proyecto Final – Análisis de Ventas (Rossmann) con Power BI

Dashboard interactivo y análisis exploratorio de ventas, ticket medio y efecto de promociones según el tipo de tienda.

---

## 🎯 Objetivo

Construir un panel de control profesional con Power BI que permita:

- Analizar la evolución mensual de ventas.
- Comparar Ventas Totales y Ticket Promedio por tipo de tienda.
- Medir el impacto de las promociones (`uplift`) en el comportamiento de compra.
- Extraer insights claros para la toma de decisiones.

---

## 🗂️ Estructura del repositorio

PROYECTO_FINAL_ROSSMANN/
├── data/
│ ├── rossmann_final.csv # Dataset principal procesado
│ ├── store.csv # Datos tienda
│ └── tienda.csv # Datos adicionales
├── panel/
│ └── proyecto_final_rossmann.pbix # Dashboard Power BI
├── docs/
│ └── Informe_proyecto_final.docx # Informe final
├── ProyectoFinal.ipynb # Cuaderno con resumen y pasos
├── *.py # Scripts Python para carga, limpieza y merge
└── README.md # Este archivo

---

## 🧰 Requisitos y herramientas

- Power BI Desktop (versión actualizada)
- Git + GitHub
- Datasets: `rossmann_final.csv`, `store.csv`, `tienda.csv`

---

## 🧭 Cómo abrir el panel en Power BI

1. Clona o descarga este repositorio.
2. Asegúrate de que los archivos `.csv` estén en la carpeta `data/`.
3. Abre `proyecto_final_rossmann.pbix` con Power BI Desktop.
4. Si es necesario, actualiza las rutas en Power Query.
5. Refresca los datos y ¡explora el dashboard!

---

## 📌 Contenido del dashboard

### **Página 1 – Resumen general**
- Ventas totales
- Ticket medio
- Evolución mensual de ventas

### **Página 2 – Análisis por tienda**
- Top 10 tiendas por ventas
- Ventas y ticket por tipo de tienda

### **Página 3 – Efecto promociones**
- Comparativa ventas con/sin promoción
- Uplift en ticket medio por tipo de tienda
- Visuales combinadas de impacto

---

## 🧪 Datos utilizados

- `rossmann_final.csv`: datos integrados y preprocesados (~66 MB)
- `store.csv`, `tienda.csv`: datos auxiliares (metadatos tiendas)
- Todos los archivos están incluidos para facilitar la reproducción del análisis.

---

## 📄 Informe

Incluido en [`/docs/Informe_proyecto_final.docx`](docs/Informe_proyecto_final.docx):

- Lógica de medidas y diseño
- Decisiones visuales
- Conclusiones de negocio

---

## 🔄 Próximos pasos

- Publicar el panel en Power BI Service
- Añadir un mapa geográfico si se dispone de coordenadas
- Realizar pruebas adicionales con promociones específicas

---

## ✒️ Autor

**Marc Nacenta (atnecan)**  
Proyecto final del máster **Data Analytics & IA Developer – ThePower Business School**  
Año: 2025

---

## 🧑‍🏫 Licencia

Este proyecto es de uso **educativo** y forma parte del Trabajo Final del máster.
