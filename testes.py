
import unittest
from cpu import CPU
from ula import ula, limitar_8bits


class TestesULA(unittest.TestCase):

    def test_add(self):
        self.assertEqual(ula("ADD", 5, 3), 8)

    def test_sub(self):
        self.assertEqual(ula("SUB", 8, 3), 5)

    def test_and(self):
        self.assertEqual(ula("AND", 12, 10), 8)

    def test_or(self):
        self.assertEqual(ula("OR", 12, 10), 14)

    def test_xor(self):
        self.assertEqual(ula("XOR", 12, 10), 6)

    def test_limitar_8bits(self):
        self.assertEqual(limitar_8bits(260), 4)


class TestesCPU(unittest.TestCase):

    def test_load(self):
        cpu = CPU()
        cpu.executar_instrucao("LOAD R0, 10")

        self.assertEqual(cpu.registradores["R0"], 10)
        self.assertEqual(cpu.pc, 1)

    def test_store(self):
        cpu = CPU()
        cpu.registradores["R0"] = 25

        cpu.executar_instrucao("STORE R0, 15")

        self.assertEqual(cpu.memoria[15], 25)
        self.assertEqual(cpu.pc, 1)

    def test_add_registradores(self):
        cpu = CPU()
        cpu.registradores["R0"] = 5
        cpu.registradores["R1"] = 7

        cpu.executar_instrucao("ADD R0, R1")

        self.assertEqual(cpu.registradores["R0"], 12)

    def test_jmp(self):
        cpu = CPU()
        cpu.executar_instrucao("JMP 5")

        self.assertEqual(cpu.pc, 5)

    def test_halt(self):
        cpu = CPU()
        cpu.executar_instrucao("HALT")

        self.assertTrue(cpu.halted)
    
    def test_halt_interrompe_execucao(self):
        cpu = CPU()
        cpu.memoria[0] = "HALT"
        cpu.memoria[1] = "LOAD R0, 10"

        cpu.executar()

        self.assertTrue(cpu.halted)
        self.assertEqual(cpu.registradores["R0"], 0)

    def test_programa_exemplo(self):
        cpu = CPU()
        cpu.memoria[0] = "LOAD R0, 5"
        cpu.memoria[1] = "LOAD R1, 8"
        cpu.memoria[2] = "ADD R0, R1"
        cpu.memoria[3] = "STORE R0, 15"
        cpu.memoria[4] = "HALT"

        cpu.executar()

        self.assertEqual(cpu.registradores["R0"], 13)
        self.assertEqual(cpu.memoria[15], 13)
        self.assertTrue(cpu.halted)



if __name__ == "__main__":
    unittest.main()
