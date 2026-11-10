import numpy as np
import pandas as pd
from scipy import stats

# ==============================================================================
# 1. GENERACIÓN / CARGA DE DATOS REALISTAS DE LA MUESTRA (n = 127)
# ==============================================================================
# Ajustado a los datos del ITVER:
# Estrato 1 (Primeros semestres 1°-4°): n1 = 70
# Estrato 2 (Últimos semestres 5°-9°): n2 = 57

np.random.seed(42)  # Semilla para reproducibilidad de resultados

# Simulación de respuestas (1: Satisfecho con el sistema, 0: Insatisfecho)
# Supuesto realista: Mayor satisfacción en primeros semestres que en últimos
respuestas_e1 = np.random.choice([1, 0], size=70, p=[0.72, 0.28])
respuestas_e2 = np.random.choice([1, 0], size=57, p=[0.48, 0.52])

# Crear DataFrame estructurado
df_e1 = pd.DataFrame({'estrato': 'Primeros Semestres (1°-4°)', 'satisfecho': respuestas_e1})
df_e2 = pd.DataFrame({'estrato': 'Últimos Semestres (5°-9°)', 'satisfecho': respuestas_e2})
df_muestra = pd.concat([df_e1, df_e2], ignore_index=True)

# Exportar dataset de la muestra a CSV (Requisito de entregable)
df_muestra.to_csv('muestra_satisfaccion_itver.csv', index=False)

# ==============================================================================
# 2. ESTADÍSTICA DESCRIPTIVA MEDIANTE NUMPY (Integrante 2)
# ==============================================================================
# Filtrado de arreglos NumPy
e1_data = df_muestra[df_muestra['estrato'] == 'Primeros Semestres (1°-4°)']['satisfecho'].to_numpy()
e2_data = df_muestra[df_muestra['estrato'] == 'Últimos Semestres (5°-9°)']['satisfecho'].to_numpy()

# Conteos y tamaños muestrales
n1 = len(e1_data)
n2 = len(e2_data)
n_total = n1 + n2

x1 = np.sum(e1_data)  # Éxitos en Estrato 1
x2 = np.sum(e2_data)  # Éxitos en Estrato 2

# Estimaciones puntuales de la proporción (p_hat)
p1_hat = x1 / n1
p2_hat = x2 / n2
p_global_hat = np.sum(df_muestra['satisfecho']) / n_total

print("==================================================================")
print("1. RESUMEN DE ESTADÍSTICA DESCRIPTIVA (MUESTRA ISC - ITVER)")
print("==================================================================")
print(f"Población total estimada (N): 800 estudiantes")
print(f"Tamaño total de la muestra (n): {n_total} estudiantes")
print(f"• Estrato 1 (Primeros semestres): n1 = {n1} | Satisfechos (x1) = {x1} | p1_hat = {p1_hat:.4f} ({p1_hat*100:.2f}%)")
print(f"• Estrato 2 (Últimos semestres):  n2 = {n2} | Satisfechos (x2) = {x2} | p2_hat = {p2_hat:.4f} ({p2_hat*100:.2f}%)")
print(f"• Proporción muestral global (p_hat): {p_global_hat:.4f} ({p_global_hat*100:.2f}%)\n")

# ==============================================================================
# 3. ESTIMACIÓN PUNTUAL Y POR INTERVALO DE CONFIANZA (p1 - p2)
# ==============================================================================
def calcular_ic_diferencia_proporciones(p1, n1, p2, n2, nivel_confianza=0.95):
    """
    Calcula el Intervalo de Confianza para la diferencia de proporciones p1 - p2
    desglosando paso a paso las fórmulas estadísticas.
    """
    # Estimación puntual de la diferencia
    diff_puntual = p1 - p2
    
    # Nivel de significancia (alpha) y valor crítico Z
    alpha = 1 - nivel_confianza
    z_critico = stats.norm.ppf(1 - alpha / 2)
    
    # Error Estándar (SE) de la diferencia de proporciones independientes
    varianza_p1 = (p1 * (1 - p1)) / n1
    varianza_p2 = (p2 * (1 - p2)) / n2
    error_estandar = np.sqrt(varianza_p1 + varianza_p2)
    
    # Margen de Error (ME)
    margen_error = z_critico * error_estandar
    
    # Límites del intervalo
    limite_inferior = diff_puntual - margen_error
    limite_superior = diff_puntual + margen_error
    
    return {
        'nivel_confianza': nivel_confianza,
        'diff_puntual': diff_puntual,
        'z_critico': z_critico,
        'error_estandar': error_estandar,
        'margen_error': margen_error,
        'ic': (limite_inferior, limite_superior)
    }

# Cálculo del Intervalo al 95% de confianza (Estándar)
res_95 = calcular_ic_diferencia_proporciones(p1_hat, n1, p2_hat, n2, nivel_confianza=0.95)

# Cálculo del Intervalo al 99% de confianza (Para responder Decisiones Metodológicas)
res_99 = calcular_ic_diferencia_proporciones(p1_hat, n1, p2_hat, n2, nivel_confianza=0.99)

print("==================================================================")
print("2. RESULTADOS DE INFERENCIA ESTADÍSTICA (p1 - p2)")
print("==================================================================")
print(f"Estimación puntual de la diferencia (p1_hat - p2_hat): {res_95['diff_puntual']:.4f}")
print("\n--- INTERVALO DE CONFIANZA DEL 95% ---")
print(f"Valor crítico Z (alpha/2 = 0.025): {res_95['z_critico']:.4f}")
print(f"Error estándar (SE): {res_95['error_estandar']:.4f}")
print(f"Margen de error (ME): {res_95['margen_error']:.4f}")
print(f"IC 95%: ({res_95['ic'][0]:.4f}, {res_95['ic'][1]:.4f})")
print(f"En porcentaje: ({res_95['ic'][0]*100:.2f}%, {res_95['ic'][1]*100:.2f}%)")

print("\n--- INTERVALO DE CONFIANZA DEL 99% (COMPARATIVA) ---")
print(f"Valor crítico Z (alpha/2 = 0.005): {res_99['z_critico']:.4f}")
print(f"Margen de error (ME): {res_99['margen_error']:.4f}")
print(f"IC 99%: ({res_99['ic'][0]:.4f}, {res_99['ic'][1]:.4f})")
print("==================================================================")