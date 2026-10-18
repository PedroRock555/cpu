from ula import ula, limitar_8bits
class CPU:
  def __init__(self):
# Registradores gerais
    self.registradores = {
"R0": 0,

"R1": 0,
"R2": 0,
"R3": 0
}
# Memória com 16 posições
    self.memoria = [0] * 16
# Program Counter
    self.pc = 0
# Estado da CPU
    self.halted = False
# --------------------------------------------------
# EXECUÇÃO DE UMA INSTRUÇÃO
# --------------------------------------------------
  def executar_instrucao(self, instrucao):
# Permite instruções como:
# LOAD R0, 5
# ADD R0, R1

   partes = instrucao.replace(",", "").split()
   operacao = partes[0]
# ------------------------------------------------
# LOAD
# ------------------------------------------------
# LOAD R0, 5
#
# Coloca o valor 5 no registrador R0.
# ------------------------------------------------
   if operacao == "LOAD":
    registrador = partes[1]
    valor = int(partes[2])
    self.registradores[registrador] = limitar_8bits(valor)
    self.pc += 1
# ------------------------------------------------
# STORE
# ------------------------------------------------
# STORE R0, 15
#
# Ainda será implementado pelos alunos.
# ------------------------------------------------ 
   elif operacao == "STORE":
    registrador = partes[1]
    endereco = int(partes[2])

    self.memoria[endereco] = self.registradores[registrador]
    self.pc += 1
# IMPLEMENTAR
# ------------------------------------------------
# ADD
# ------------------------------------------------
# ADD R0, R1
# R0 = R0 + R1
# ------------------------------------------------
   elif operacao == "ADD":
    destino = partes[1]
    origem = partes[2]

    a = self.registradores[destino]
    b = self.registradores[origem]

    self.registradores[destino] = self.ula("ADD", a, b)
    self.pc += 1
# IMPLEMENTAR
# ------------------------------------------------
# SUB
# ------------------------------------------------
   elif operacao == "SUB":
    destino = partes[1]
    origem = partes[2]
    self.registradores[destino] = self.ula(
        "SUB",
        self.registradores[destino],
        self.registradores[origem]
    )
    self.pc += 1
# IMPLEMENTAR
# ------------------------------------------------

# AND
# ------------------------------------------------
   elif operacao == "AND":
    destino = partes[1]
    origem = partes[2]
    self.registradores[destino] = self.ula(
        "AND",
        self.registradores[destino],
        self.registradores[origem]
    )
    self.pc += 1
# IMPLEMENTAR
# ------------------------------------------------
# OR
# ------------------------------------------------
   elif operacao == "OR":
    destino = partes[1]
    origem = partes[2]
    self.registradores[destino] = self.ula(
        "OR",
        self.registradores[destino],
        self.registradores[origem]
    )
    self.pc += 1
# IMPLEMENTAR
# ------------------------------------------------
# XOR
# ------------------------------------------------
   elif operacao == "XOR":
    destino = partes[1]
    origem = partes[2]
    self.registradores[destino] = self.ula(
        "XOR",
        self.registradores[destino],
        self.registradores[origem]
    )
    self.pc += 1
# IMPLEMENTAR
# ------------------------------------------------
# JMP
# ------------------------------------------------
# JMP 8
#
# O PC passa a apontar para a posição 8.
# ------------------------------------------------
   elif operacao == "JMP":
    endereco = int(partes[1])
    self.pc = endereco
# ------------------------------------------------
# HALT
# ------------------------------------------------
   elif operacao == "HALT":
    self.halted = True
# IMPLEMENTAR
   else:
    raise ValueError(
f"Instrução desconhecida: {operacao}"
)
# --------------------------------------------------
# CICLO DA CPU

# --------------------------------------------------
  def ula(self, operacao, a, b):
    return ula(operacao, a, b)
  def ciclo(self):
# FETCH
    instrucao = self.memoria[self.pc]
    print()
    print("-----------------------------")
    print("PC:", self.pc)
    print("Instrução:", instrucao)
# DECODE + EXECUTE
    self.executar_instrucao(instrucao)
# Mostrar registradores
    self.mostrar_estado()
# --------------------------------------------------
# EXECUÇÃO COMPLETA
# --------------------------------------------------
  def executar(self):
    while not self.halted:
     self.ciclo()
# --------------------------------------------------
# MOSTRAR ESTADO
# --------------------------------------------------
  def mostrar_estado(self):
   print("Registradores:")
   for nome, valor in self.registradores.items():
    print(
f"{nome} = {valor:02X} "
f"({valor})"
)
