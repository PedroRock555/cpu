from cpu import CPU
from programas import programa_grupo
cpu = CPU()

cpu.memoria[0] = "LOAD R0, 5"
cpu.memoria[1] = "LOAD R1, 8"
cpu.memoria[2] = "ADD R0, R1"
cpu.memoria[3] = "STORE R0, 15"
cpu.memoria[4] = "HALT"

print("================================")
print(" CPU SIMULADA - 8 BITS")
print("================================")

cpu.executar()

print()
print("Memória[15]:", cpu.memoria[15])
# --------------------------------------------------
# PROGRAMA PRÓPRIO DO GRUPO
# --------------------------------------------------
print("\n================================")
print(" PROGRAMA DO GRUPO")
print("================================")

cpu = CPU()

for i, instrucao in enumerate(programa_grupo):
    cpu.memoria[i] = instrucao

cpu.executar()

print("\nResultados do programa do grupo:")
print("R0:", cpu.registradores["R0"])
print("R1:", cpu.registradores["R1"])
print("R2:", cpu.registradores["R2"])
print("Memória[15]:", cpu.memoria[15])
print("Memória[14]:", cpu.memoria[14])
