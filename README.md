# Laboratorio de CI/CD - Módulo 4

Este repositorio contiene la implementación y evolución de los pipelines de Integración Continua (CI) y Despliegue Continuo (CD) para el proyecto del módulo.

## 🚀 Descripción del Proyecto

El objetivo de este proyecto es implementar flujos de trabajo automatizados utilizando **GitHub Actions**, integrando:
- Estrategias de branching profesional (`main` y ramas `feature/*`).
- Validación automática en Pull Requests.
- **Compilación y verificación de sintaxis** automática.
- **Ejecución de Pruebas Unitarias** con `pytest`.
- **Análisis de Cobertura de Código** con `pytest-cov`.
- **Publicación automática de Reportes como Artefactos** (`test-results.xml` y HTML de cobertura).
- **Quality Gate** que detiene el pipeline ante fallos en pruebas.
- Protección de ramas y políticas de calidad.

## 🌳 Estrategia de Branching

Se utiliza una estrategia basada en **Feature Branches** (Ramas de funcionalidad):

```text
main (Rama protegida / Producción)
  │
  └── feature/*  ──► [Pull Request + CI Checks (Build & Test)] ──► [Merge a main]
```

## ⚙️ Estructura del Pipeline CI

El pipeline configurado en `.github/workflows/pipeline.yml` se organiza en dos trabajos secuenciales:

```mermaid
flowchart LR
    A[Checkout] --> B[Setup Python]
    B --> C[Install Dependencies]
    C --> D[Build & Syntax Validation]
    D --> E[Unit Tests (pytest)]
    E --> F[Code Coverage Report]
    F --> G[Upload Artifacts]
```

### Etapas:
1. **Etapa 1: Build & Compile (`build`)**
   - Instala las dependencias del proyecto.
   - Compila y valida la sintaxis de todos los módulos Python (`python -m py_compile`).
2. **Etapa 2: Unit Tests & Quality Gate (`test`)**
   - Se ejecuta únicamente si la etapa de `build` concluye con éxito (`needs: build`).
   - Ejecuta las pruebas unitarias con `pytest`.
   - Genera reportes de resultados en formato JUnit XML y reporte de cobertura en HTML.
   - Publica los reportes como artefactos descargables en GitHub Actions.
   - Actúa como **Quality Gate**: ante cualquier aserción fallida, el pipeline se detiene inmediatamente.

---
*Autor: Jppm98*
