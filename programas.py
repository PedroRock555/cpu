
# --------------------------------------------------
# PROGRAMAS UTILIZADOS NA CPU SIMULADA
# --------------------------------------------------

# Programa de exemplo utilizado nos testes
programa_exemplo = [
    "LOAD R0, 5",
    "LOAD R1, 8",
    "ADD R0, R1",
    "STORE R0, 15",
    "HALT"
]

# Programa próprio do grupo
# Utiliza 8 instruções, LOAD, STORE e duas operações da ULA
programa_grupo = [
    "LOAD R0, 5",
    "LOAD R1, 8",
    "ADD R0, R1",
    "STORE R0, 15",
    "LOAD R2, 3",
    "XOR R0, R2",
    "STORE R0, 14",
    "HALT"
]
