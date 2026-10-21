# CPU SIMULADA - 8 BITS 
Trabalho prático desenvolvido para disciplina de **Arquitetura e Organização de Computadores** da **Universidade Federal do Ceará (UFC) - Campus Sobral**. O projeto consiste na implementação de um modelo executável de uma CPU didática de 8 bits em Python, simulando seu ciclo de execução, registradores, memória e operações da ULA.

## FUNCIONALIDADES
- Execução de instruções de uma CPU simulada;
- Utilização de registradores para armazenar valores;
- Leitura e escrita de dados na memória;
- Operações aritméticas, como adição e subtração;
- Operações lógicas, com AND, OR E XOR;
- Controle do fluxo de execução;
- Encerramento do programa por meio da instrução HALT;
- Execução de programas de exemplo e testes;

## ORGANIZAÇÃO DOS ARQUIVOS
- `cpu.py`: implementa a estrutura da CPU e suas instruções;
- `ula.py`: realiza as operações aritméticas e lógicas;
- `programas.py`: contém o programa de exemplo e o programa desenvolvido pela dupla;
- `testes.py`: contém testes para verificar o funcionamento das operações e instruções;
- `main.py`: integra os componentes e executa a simulação;

## EXEMPLO DE EXECUÇÃO
1. Carrega o valor 5 no registrador RO;
2. Carrega o valor 8 no registrador R1;
3. Soma os valores armazenados nos registradores;
4. Armazena o resultado na posição 15 da memória;
5. Encerra a execução;

O resultado da soma é 13.

## COMO EXECUTAR

É necessário ter o Python instalado no computador
1. Baixe ou clone este repositório;
2. Abra o terminal na pasta do projeto;
3. Execute o arquivo principal com o comando:
```bash
python main.py
```

Se o seu sistema utilizar o comando `python3`, execute:

```bash
python3 main.py
```
A saída exibirá as instruções executadas, o valor do PC, o conteúdo dos registradores e os resultados armazenados na memória.

## TECNOLOGIAS UTILIZADAS
- Python;
- Git e Github

