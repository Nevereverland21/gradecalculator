from evaluation import Evaluation
from evaluation_list import EvaluationList
from attendance_policy import AttendancePolicy
from extra_points_policy import ExtraPointsPolicy
from grade_calculator import GradeCalculator


def ask_float(prompt):
    while True:
        try:
            return float(input(prompt))
        except ValueError:
            print("Error: Debe ingresar un número válido.")


def ask_int(prompt):
    while True:
        try:
            return int(input(prompt))
        except ValueError:
            print("Error: Debe ingresar un número entero.")


def ask_bool(prompt):
    while True:
        val = input(prompt).strip().lower()
        if val in ("s", "si", "sí"):
            return True
        if val in ("n", "no"):
            return False
        print("Error: Ingrese 's' o 'n'.")


def main():
    print("\n=== Sistema de Cálculo de Notas ===")
    print("Responda la siguiente información:\n")

    # 1. Número de evaluaciones
    num_evals = ask_int("¿Cuántas evaluaciones tiene el estudiante? (1–10): ")

    if num_evals < 1 or num_evals > 10:
        print("Error: El número de evaluaciones debe estar entre 1 y 10.")
        return

    # 2. Cargar evaluaciones
    evaluations = []
    total_weight = 0.0

    for i in range(1, num_evals + 1):
        print(f"\n--- Evaluación {i} ---")
        score = ask_float("Ingrese la nota (0-20): ")
        weight = ask_float("Ingrese el peso (0.0–1.0): ")

        try:
            evaluations.append(Evaluation(score, weight))
            total_weight += weight
        except Exception as e:
            print(f"Error: {e}")
            return

    # Validación del peso total
    if abs(total_weight - 1.0) > 0.0001:
        print("\nError: La suma total de los pesos debe ser 1.0")
        print(f"Suma actual = {total_weight}")
        return

    try:
        evaluation_list = EvaluationList(evaluations)
    except Exception as e:
        print(f"Error: {e}")
        return

    # 3. Asistencia mínima
    has_min_attendance = ask_bool("\n¿Cumplió la asistencia mínima? (s/n): ")

    # 4. Docentes y puntos extra
    num_teachers = ask_int("\n¿Cuántos docentes pueden otorgar puntos extra?: ")

    teachers_flags = []
    for i in range(1, num_teachers + 1):
        flag = ask_bool(f"¿El docente {i} otorga punto extra? (s/n): ")
        teachers_flags.append(flag)

    try:
        extra_policy = ExtraPointsPolicy(teachers_flags)
    except Exception as e:
        print(f"Error: {e}")
        return

    # 5. Cálculo final
    attendance_policy = AttendancePolicy()
    calculator = GradeCalculator(attendance_policy, extra_policy)

    result = calculator.calculate(evaluation_list, has_min_attendance)

    # 6. Mostrar resultado
    print("\n=== RESULTADOS ===")
    print(f"Nota base:          {result.base_grade:.2f}")
    print(f"Tras asistencia:    {result.after_attendance:.2f}")
    print(f"Puntos extra:       {result.extra_points}")
    print(f"Nota final:         {result.final_grade:.2f}")


if __name__ == "__main__":
    main()

