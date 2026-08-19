# Laboratorio de CI/CD - Módulo 4

Este repositorio contiene la implementación y evolución de los pipelines de Integración Continua (CI) y Despliegue Continuo (CD) para el proyecto del módulo.

## 🚀 Descripción del Proyecto

El objetivo de este proyecto es implementar flujos de trabajo automatizados utilizando **GitHub Actions**, integrando:
- Estrategias de branching profesional (`main` y ramas `feature/*`).
- Validación automática en Pull Requests.
- Verificaciones del entorno y dependencias.
- Protección de ramas y Quality Gates.

## 🌳 Estrategia de Branching

Se utiliza una estrategia basada en **Feature Branches** (Ramas de funcionalidad):

```text
main (Rama protegida / Producción)
  │
  └── feature/update-readme  ──► [Pull Request + CI Check] ──► [Merge a main]
```

- **`main`**: Rama principal estable y protegida contra pushes directos.
- **`feature/*`**: Ramas dedicadas al desarrollo de nuevas características o documentación.
- **Pull Requests**: Mecanismo formal de revisión de código y validación obligatoria por CI antes de la integración.

## ⚙️ Estructura del Pipeline

El pipeline configurado en `.github/workflows/pipeline.yml` se ejecuta ante:
- Pushes a la rama `main` y ramas `feature/**`.
- Creación y actualización de `Pull Requests` dirigidos a `main`.

### Etapas actuales:
1. **Checkout del repositorio**: Descarga del código fuente.
2. **Información del entorno**: Identifica repositorio, rama activa y commit SHA.
3. **Fecha y Hora**: Registra la marca de tiempo de la ejecución.
4. **Versión de Git**: Valida el entorno de ejecución en el runner.
5. **Confirmación de finalización**: Cierre exitoso del pipeline.

---
*Autor: Jppm98*
