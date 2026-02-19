#!/usr/bin/env python3
"""
Verifica que los VALORES de respuesta especificados en los archivos de solución
coincidan con los resultados reales de ejecutar las queries.
"""

import sqlite3
import re
from pathlib import Path

# Colores para la terminal
class Colors:
    GREEN = '\033[92m'
    RED = '\033[91m'
    YELLOW = '\033[93m'
    BLUE = '\033[94m'
    BOLD = '\033[1m'
    END = '\033[0m'

def extract_questions_queries_answers(md_file):
    """Extrae preguntas, queries SQL y respuestas esperadas de un archivo markdown."""
    with open(md_file, 'r', encoding='utf-8') as f:
        content = f.read()
    
    # Dividir por preguntas
    pattern = r'## Pregunta (\d+)\n\*\*(.*?)\*\*\n\n```sql\n(.*?)\n```(?:\n\n\*\*Respuesta:\*\* (.*?)(?:\n|$))?'
    matches = re.findall(pattern, content, re.DOTALL)
    
    result = []
    for match in matches:
        num, question, query, answer = match
        result.append({
            'num': int(num),
            'question': question.strip(),
            'query': query.strip(),
            'expected_answer': answer.strip() if answer else None
        })
    
    return result

def execute_query(db_path, query):
    """Ejecuta una query y devuelve los resultados."""
    try:
        conn = sqlite3.connect(db_path)
        cursor = conn.cursor()
        cursor.execute(query)
        results = cursor.fetchall()
        conn.close()
        return results
    except Exception as e:
        return f"ERROR: {e}"

def format_result(results):
    """Formatea los resultados de una query para comparación."""
    if isinstance(results, str):  # Es un error
        return results
    
    if not results:
        return "Sin resultados"
    
    # Si es un solo valor
    if len(results) == 1 and len(results[0]) == 1:
        value = results[0][0]
        if isinstance(value, float):
            return f"{value:.2f}"
        return str(value)
    
    # Si es una fila con múltiples valores
    if len(results) == 1:
        formatted = []
        for val in results[0]:
            if isinstance(val, float):
                formatted.append(f"{val:.2f}")
            else:
                formatted.append(str(val))
        return ", ".join(formatted)
    
    # Si son múltiples filas
    return f"{len(results)} filas"

def normalize_answer(answer):
    """Normaliza una respuesta para comparación."""
    if not answer:
        return None
    
    # Extraer números de la respuesta esperada
    # Ejemplos: "129", "41.16", "47 miembros, edad promedio: 57.17 años"
    numbers = re.findall(r'\d+\.?\d*', answer)
    
    if not numbers:
        return answer.lower().strip()
    
    return numbers

def verify_exam(exam_name, solution_file, db_file):
    """Verifica que los valores de respuesta coincidan con los resultados reales."""
    print(f"\n{Colors.BOLD}{Colors.BLUE}{'='*70}")
    print(f"Verificando respuestas: {exam_name.upper()}")
    print(f"{'='*70}{Colors.END}\n")
    
    questions = extract_questions_queries_answers(solution_file)
    
    if len(questions) != 12:
        print(f"{Colors.YELLOW}⚠️  Se encontraron {len(questions)} preguntas (se esperaban 12){Colors.END}\n")
    
    all_correct = True
    no_answer_specified = []
    
    for q in questions:
        result = execute_query(db_file, q['query'])
        
        if isinstance(result, str):  # Error
            print(f"{Colors.RED}❌ P{q['num']:2d}: ERROR AL EJECUTAR QUERY")
            print(f"     {result}{Colors.END}")
            all_correct = False
            continue
        
        formatted_result = format_result(result)
        
        # Si no hay respuesta esperada especificada
        if not q['expected_answer']:
            no_answer_specified.append(q['num'])
            print(f"{Colors.YELLOW}⚠️  P{q['num']:2d}: Sin valor de respuesta especificado")
            print(f"     Resultado actual: {formatted_result}{Colors.END}")
            continue
        
        # Verificar si coincide
        expected_numbers = normalize_answer(q['expected_answer'])
        
        # Comparar
        match = False
        if expected_numbers:
            # Extraer números del resultado
            if isinstance(result, list) and len(result) == 1 and len(result[0]) == 1:
                # Un solo valor
                actual_value = result[0][0]
                if isinstance(actual_value, float):
                    # Comparar con tolerancia
                    expected_float = float(expected_numbers[0])
                    match = abs(actual_value - expected_float) < 0.01
                else:
                    match = str(actual_value) == expected_numbers[0]
            elif isinstance(result, list) and len(result) == 1:
                # Una fila con múltiples valores
                result_numbers = []
                for val in result[0]:
                    if isinstance(val, float):
                        result_numbers.append(f"{val:.2f}")
                    else:
                        result_numbers.append(str(val))
                
                # Verificar si todos los números esperados están en el resultado
                match = all(num in result_numbers or 
                          any(abs(float(num) - float(rn)) < 0.1 for rn in result_numbers if rn.replace('.','').isdigit())
                          for num in expected_numbers)
            elif isinstance(result, list):
                # Múltiples filas - verificar el count
                if expected_numbers[0].isdigit():
                    match = len(result) == int(expected_numbers[0])
        
        if match:
            print(f"{Colors.GREEN}✅ P{q['num']:2d}: Valor correcto")
            print(f"     Esperado: {q['expected_answer']}")
            print(f"     Obtenido: {formatted_result}{Colors.END}")
        else:
            print(f"{Colors.RED}❌ P{q['num']:2d}: VALOR NO COINCIDE")
            print(f"     Esperado: {Colors.YELLOW}{q['expected_answer']}{Colors.END}")
            print(f"     Obtenido: {Colors.RED}{formatted_result}{Colors.END}")
            
            # Mostrar la query para debug
            print(f"{Colors.BLUE}     Query: {q['query'][:80]}...{Colors.END}")
            all_correct = False
    
    # Resumen
    print(f"\n{Colors.BOLD}Resumen:{Colors.END}")
    if no_answer_specified:
        print(f"  {Colors.YELLOW}⚠️  Preguntas sin valor de respuesta: {len(no_answer_specified)} - P{', P'.join(map(str, no_answer_specified))}{Colors.END}")
    
    return all_correct

def main():
    """Función principal."""
    base_dir = Path(__file__).parent
    
    exams = [
        ('gimnasio', 'soluciones/solucion_gimnasio.md', 'data/gimnasio.db'),
        ('hospital', 'soluciones/solucion_hospital.md', 'data/hospital.db'),
        ('banco', 'soluciones/solucion_banco.md', 'data/banco.db'),
        ('bar', 'soluciones/solucion_bar.md', 'data/bar.db'),
        ('restaurante', 'soluciones/solucion_restaurante.md', 'data/restaurante.db'),
    ]
    
    print(f"\n{Colors.BOLD}{Colors.BLUE}{'='*70}")
    print("VERIFICACIÓN DE VALORES DE RESPUESTA EN SOLUCIONARIOS")
    print(f"{'='*70}{Colors.END}")
    
    all_correct = True
    
    for exam_name, solution_file, db_file in exams:
        solution_path = base_dir / solution_file
        db_path = base_dir / db_file
        
        if not solution_path.exists() or not db_path.exists():
            print(f"{Colors.RED}❌ Archivos no encontrados para {exam_name}{Colors.END}")
            all_correct = False
            continue
        
        exam_result = verify_exam(exam_name, solution_path, db_path)
        all_correct = all_correct and exam_result
    
    # Resumen final
    print(f"\n{Colors.BOLD}{Colors.BLUE}{'='*70}")
    print("RESUMEN FINAL")
    print(f"{'='*70}{Colors.END}\n")
    
    if all_correct:
        print(f"{Colors.GREEN}{Colors.BOLD}🎉 ¡TODOS LOS VALORES DE RESPUESTA SON CORRECTOS!{Colors.END}")
        print(f"{Colors.GREEN}Los resultados de las queries coinciden con las respuestas especificadas.{Colors.END}")
    else:
        print(f"{Colors.RED}{Colors.BOLD}❌ SE ENCONTRARON DISCREPANCIAS EN LOS VALORES{Colors.END}")
        print(f"{Colors.RED}Por favor revisa los errores indicados arriba.{Colors.END}")
    
    print()
    return 0 if all_correct else 1

if __name__ == '__main__':
    exit(main())
