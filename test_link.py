import ctypes
import os

# 1. ENCONTRAR A BIBLIOTECA
# Precisamos do caminho absoluto para o Windows não se perder
dll_path = os.path.abspath("src/c_core/risk_engine.dll")
print(f"🔌 A carregar biblioteca C de: {dll_path}")

try:
    # Carregar a DLL para a memória do Python
    risk_lib = ctypes.CDLL(dll_path)
    print("✅ Biblioteca carregada com sucesso!")
except OSError as e:
    print(f"❌ Erro ao carregar DLL: {e}")
    exit()

# 2. DEFINIR AS REGRAS (Tipos de Dados)
# O C é burro. Temos de lhe dizer exatamente o que vai receber.
# A função é: double calculate_mean(double* returns, int size)

# Argumentos: [Ponteiro para Doubles, Inteiro]
risk_lib.calculate_mean.argtypes = [ctypes.POINTER(ctypes.c_double), ctypes.c_int]

# Retorno: Um Double
risk_lib.calculate_mean.restype = ctypes.c_double

# 3. CRIAR DADOS NO PYTHON
print("\n🐍 Python: A criar array de dados...")
valores_python = [10.0, 20.0, 30.0, 40.0, 50.0] # Média deve ser 30.0

# Converter lista Python para Array C
# (c_double * 5) cria um tipo de array de tamanho 5
array_c_type = (ctypes.c_double * len(valores_python))
input_c = array_c_type(*valores_python)

# 4. EXECUTAR (A MAGIA)
print("🚀 Python: A enviar dados para o Kernel C...")
resultado = risk_lib.calculate_mean(input_c, len(valores_python))

# 5. RESULTADO
print(f"\n🏁 Resultado recebido do C: {resultado}")

if resultado == 30.0:
    print("🏆 SUCESSO ABSOLUTO: O Python e o C estão ligados!")
else:
    print("⚠️ Algo correu mal na matemática.")