#!/usr/bin/env python3
"""
Verifica que todas las soluciones SQL en los archivos de solucion/ 
sean correctas y ejecutables contra las bases de datos.
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

def extract_sql_queries(md_file):
    """Extrae las queries SQL de un archivo markdown de soluciones."""
    with open(md_file, 'r', encoding='utf-8') as f:
        content = f.read()
    
    # Encontrar todas las queries SQL (código entre ```sql y ```)
    pattern = r'```sql\n(.*?)\n```'
    queries = re.findall(pattern, content, re.DOTALL)
    
    return queries

def extract_questions(md_file):
    """Extrae los títulos de las preguntas de un archivo markdown."""
    with open(md_file, 'r', encoding='utf-8') as f:
        content = f.read()
    
    # Encontrar todos los títulos de pregunta
    pattern = r'## Pregunta \d+\n\*\*(.*?)\*\*'
    questions = re.findall(pattern, content, re.DOTALL)
    
    return questions

def verify_query(db_path, query, question_num):
    """Ejecuta una query y verifica que sea correcta."""
    try:
        conn = sqlite3.connect(db_path)
        cursor = conn.cursor()
        cursor.execute(query)
        results = cursor.fetchall()
        conn.close()
        
        num_rows = len(results)
        num_cols = len(results[0]) if results else 0
        
        return {
            'status': 'OK',
            'num_rows': num_rows,
            'num_cols': num_cols,
            'sample': results[:3] if results else []
        }
    except Exception as e:
        return {
            'status': 'ERROR',
            'error': str(e)
        }

def verify_exam(exam_name, solution_file, exam_file, db_file):
    """Verifica todas las queries de un examen."""
    print(f"\n{Colors.BOLD}{Colors.BLUE}{'='*70}")
    print(f"Verificando: {exam_name.upper()}")
    print(f"{'='*70}{Colors.END}\n")
    
    # Extraer queries y preguntas
    queries = extract_sql_queries(solution_file)
    questions = extract_questions(solution_file)
    
    if len(queries) != 12:
        print(f"{Colors.RED}⚠️  ALERTA: Se encontraron {len(queries)} queries (se esperaban 12){Colors.END}")
    
    if len(questions) != 12:
        print(f"{Colors.RED}⚠️  ALERTA: Se encontraron {len(questions)} preguntas (se esperaban 12){Colors.END}")
    
    errors = []
    warnings = []
    success = []
    
    for i, query in enumerate(queries, 1):
        question_text = questions[i-1] if i <= len(questions) else "Sin título"
        # Truncar el texto de la pregunta si es muy largo
        if len(question_text) > 60:
            question_text = question_text[:57] + "..."
        
        result = verify_query(db_file, query, i)
        
        if result['status'] == 'ERROR':
            errors.append((i, question_text, result['error']))
            print(f"{Colors.RED}❌ P{i:2d}: ERROR - {question_text}")
            print(f"     {result['error']}{Colors.END}")
        else:
            success.append((i, question_text, result))
            
            # Determinar el indicador según el número de filas
            if result['num_rows'] == 0:
                indicator = f"{Colors.YELLOW}⚠️{Colors.END} "
                warnings.append((i, question_text, "No devuelve resultados"))
            elif result['num_rows'] > 20:
                indicator = f"{Colors.YELLOW}📊{Colors.END}"
            else:
                indicator = f"{Colors.GREEN}✅{Colors.END}"
            
            print(f"{indicator} P{i:2d}: OK - {result['num_rows']} fila(s), {result['num_cols']} columna(s)")
            print(f"     {Colors.BLUE}{question_text}{Colors.END}")
    
    # Resumen
    print(f"\n{Colors.BOLD}Resumen:{Colors.END}")
    print(f"  {Colors.GREEN}✅ Correctas: {len(success)}{Colors.END}")
    if warnings:
        print(f"  {Colors.YELLOW}⚠️  Advertencias: {len(warnings)}{Colors.END}")
        for w in warnings:
            print(f"     P{w[0]}: {w[2]}")
    if errors:
        print(f"  {Colors.RED}❌ Errores: {len(errors)}{Colors.END}")
        for e in errors:
            print(f"     P{e[0]}: {e[2]}")
    
    return len(errors) == 0, len(warnings), len(success)

def main():
    """Función principal."""
    base_dir = Path(__file__).parent
    
    exams = [
        ('gimnasio', 'soluciones/solucion_gimnasio.md', 'examenes/examen_gimnasio.md', 'data/gimnasio.db'),
        ('hospital', 'soluciones/solucion_hospital.md', 'examenes/examen_hospital.md', 'data/hospital.db'),
        ('banco', 'soluciones/solucion_banco.md', 'examenes/examen_banco.md', 'data/banco.db'),
        ('bar', 'soluciones/solucion_bar.md', 'examenes/examen_bar.md', 'data/bar.db'),
        ('restaurante', 'soluciones/solucion_restaurante.md', 'examenes/examen_restaurante.md', 'data/restaurante.db'),
    ]
    
    print(f"\n{Colors.BOLD}{Colors.BLUE}{'='*70}")
    print("VERIFICACIÓN DEL SOLUCIONARIO OFICIAL")
    print(f"{'='*70}{Colors.END}")
    
    all_ok = True
    total_warnings = 0
    total_success = 0
    total_exams = len(exams)
    
    for exam_name, solution_file, exam_file, db_file in exams:
        solution_path = base_dir / solution_file
        exam_path = base_dir / exam_file
        db_path = base_dir / db_file
        
        # Verificar que los archivos existan
        if not solution_path.exists():
            print(f"{Colors.RED}❌ No se encontró: {solution_file}{Colors.END}")
            all_ok = False
            continue
        
        if not db_path.exists():
            print(f"{Colors.RED}❌ No se encontró: {db_file}{Colors.END}")
            all_ok = False
            continue
        
        ok, warnings, success = verify_exam(exam_name, solution_path, exam_path, db_path)
        all_ok = all_ok and ok
        total_warnings += warnings
        total_success += success
    
    # Resumen final
    print(f"\n{Colors.BOLD}{Colors.BLUE}{'='*70}")
    print("RESUMEN FINAL")
    print(f"{'='*70}{Colors.END}\n")
    
    print(f"Total de exámenes: {total_exams}")
    print(f"Total de preguntas verificadas: {total_success}/{total_exams * 12}")
    
    if total_warnings > 0:
        print(f"{Colors.YELLOW}Advertencias totales: {total_warnings}{Colors.END}")
    
    if all_ok:
        print(f"\n{Colors.GREEN}{Colors.BOLD}🎉 ¡TODOS LOS SOLUCIONARIOS SON CORRECTOS!{Colors.END}")
        print(f"{Colors.GREEN}Todas las queries se ejecutaron sin errores.{Colors.END}")
    else:
        print(f"\n{Colors.RED}{Colors.BOLD}❌ SE ENCONTRARON ERRORES EN LOS SOLUCIONARIOS{Colors.END}")
        print(f"{Colors.RED}Por favor revisa los errores indicados arriba.{Colors.END}")
    
    print()
    return 0 if all_ok else 1

if __name__ == '__main__':
    exit(main())
