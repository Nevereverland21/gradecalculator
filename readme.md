# GradeCalculator – Sistema de Cálculo de Notas

Proyecto desarrollado en Python con arquitectura orientada a objetos.  
Permite calcular la nota final de un estudiante considerando evaluaciones, asistencia mínima y puntos extra asignados por docentes.  
Incluye pruebas unitarias y soporte para análisis estático con SonarQube.

---

## 📘 Características Principales

- Registro de evaluaciones con **nota** y **peso porcentual**.
- Validación estricta de:
  - Máximo **10 evaluaciones** (RNF01)
  - La suma de pesos debe ser exactamente **1.0**
  - Notas solo entre **0 y 20**
- Reglas de asistencia mínima:
  - Si **no cumple asistencia**, la nota final es **0** (RF02)
- Asignación de puntos extra por docentes (True/False)
- Cálculo final determinista:
  - Nota base
  - Nota tras asistencia
  - Puntos extra sumados
  - Tope máximo de **20** (RF05)
- Arquitectura limpia, modular y mantenible.
- CLI interactivo desde terminal.
- Suite completa de pruebas unitarias (`pytest`).
- Integración con SonarQube para análisis de calidad.

---

## 📂 Estructura del Proyecto
gradecalculator/
│── evaluation.py
│── evaluation_list.py
│── attendance_policy.py
│── extra_points_policy.py
│── grade_calculator.py
│── dto.py
│── main.py
│── tests/
│ ├── test_evaluation.py
│ ├── test_evaluation_list.py
│ ├── test_attendance_policy.py
│ ├── test_extra_points_policy.py
│ └── test_grade_calculator.py
│── sonar-project.properties

---

## 🧠 Arquitectura Orientada a Objetos

### **Clases Principales**

| Clase                 | Responsabilidad |
|----------------------|-----------------|
| `Evaluation`         | Representa una evaluación individual (nota + peso). |
| `EvaluationList`     | Colección validada de evaluaciones y cálculo de nota base. |
| `AttendancePolicy`   | Aplica reglas de asistencia mínima (RF02). |
| `ExtraPointsPolicy`  | Cálculo de puntos extra otorgados por docentes (RF03, RF04). |
| `GradeCalculator`    | Lógica final del cálculo de nota (RF05). |
| `GradeResult`        | DTO con campos estructurados del resultado. |
| `main.py`            | Interfaz CLI interactiva. |

---

## ▶️ Cómo Ejecutar el Proyecto

### 1. Crear entorno virtual (opcional)
```bash
python3 -m venv venv
source venv/bin/activate

