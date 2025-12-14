import numpy as np
from models import ParametricVar # <--- IMPORTANTE: O teu ficheiro chama-se models.py?

# 1. GERAR DADOS FALSOS (SIMULAÇÃO)
# Vamos simular 1000 dias de trading
# Média (loc) = 0 (o mercado não mexe em média)
# Desvio (scale) = 0.01 (1% de volatilidade diária)
print("🎲 A gerar dados de mercado simulados...")
fake_returns = np.random.normal(loc=0, scale=0.01, size=1000)

# Ver o que gerámos (só os primeiros 5)
print(f"Exemplo de retornos: {fake_returns[:5]}")

# 2. INICIALIZAR O MOTOR
# Vamos criar dois perfis para comparar
print("\n⚙️ A inicializar modelos de risco...")
horizon = [1, 10, 100]
print("\n--- RESULTADOS ---")
print(f"\nSe tiveres 1.000.000€ investidos:")
for h in horizon:
    modelo_normal = ParametricVar(confidence=0.95, horizon=h)

    # 3. EXECUTAR
    
    var_95 = modelo_normal.calculate_risk(fake_returns)

    # 4. ANÁLISE (O que um Quant faria)
    
    print(f"Risco Normal ({h} dia): {var_95 * 1000000:.2f} €")