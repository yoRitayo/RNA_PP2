# RNA_PP2
Repositório destinado à publicação das atividades do 2° Projeto Prático de Redes Neurais Artificiais 2025.1  
**Data de criação:** 05/03/2025
**Última atualização:** 07/04/2025 
[ENG BELLOW]

Este projeto tem por objetivo a execução de um treinamento mediante Aprendizado Supervisionado do neurônio Perceptron de Rosenblatt para problemas de classificação. Nesse contexto, tal prática é dividida em três partes:

1. Desenvolvimento de um algoritmo fundamentado na orientação a objetos para o neurônio Perceptron de Rosenblatt para um problema linearmente separável;
2. Execução do algoritmo com variadas configurações, bem como análise de eficiência;
3. Análise da aplicação do algoritmo para um problema não-linearmente separável.

## Tecnologias Utilizadas
- **Anaconda:** Gerenciamento de ambientes virtuais;
- **Python:** Execução do algoritmo, utilizando as seguintes bibliotecas:
  - **Pandas:** Manipulação de dados;
  - **Numpy:** Processos matriciais otimizados;
  - **Random:** Geração de números pseudo-aleatórios;
  - **Sci-kit learn:** Métricas de treinamentos do neurônio;
  - **Matplotlib:** Plotagem de gráficos;
  - **Pretty-table:** Organização e plotagem de dados tabulares.

## Estrutura do Projeto
```plaintext
RNA_PP2/
├── .gitignore                  # Manipulação de git para evitar conflitos de output na branch main
├── atividade.ipynb             # Jupyter Notebook contendo a execução da proposta de projeto
├── data1.txt                   # Dataset utilizado para a segunda parte do projeto
├── dataAll.txt                 # Dataset utilizado para a primeira parte do projeto
├── dataHouldout.txt            # Dataset utilizado para a terceira parte do projeto
├── environment.yml             # Armazenamento das variáveis de ambiente virtual
└── README.md                   # Documentação do projeto
```

## Como Executar
* Certifique-se de que o Git e o Anaconda estão devidamente instalados em sua máquina.
* Abra o terminal no diretório onde o código será executado.

1. Clone este repositório:
   ```bash
   git clone https://github.com/yoRitayo/RNA_PP2.git
   ```
2. Entre no diretório referente ao repositório:
   ```bash
   cd RNA_PP2
   ```

3. Instale o ambiente virtual do projeto:
   ```bash
   conda env create -f environment.yml
   ```
4. Ative o ambiente virtual:
   ```bash
   conda env activate env_rnapp2 
   ```
5. Abra o arquivo da atividade através do Jupyter Notebook:
   ```bash
   jupyter notebook
   ```

## Contribuições
Contribuições são bem-vindas! Para sugerir melhorias ou reportar problemas, abra uma [issue](https://github.com/yoRitayo/RNA_PP2/issues) ou envie um [pull request](https://github.com/yoRitayo/RNA_PP2/pulls).

## Autores
- Elloá B. Guedes (orientadora);
- Davi Aguiar Moreira;
- Ian Garrido Reis;
- Luiz Fernando Borges Brito;
- Pedro Vitor Barros Maranhão;
- Rita De Cassia Brasil Alves.

---

# RNA_PP2 [ENG]
Repository for the publication of activities related to the 2nd Practical Project in Artificial Neural Networks – 2025.1  
**Creation date:** 2025-03-05  
**Last update:** 2025-04-07 

This project aims to carry out a training process using Supervised Learning for Rosenblatt’s Perceptron neuron in classification problems. In this context, the project is divided into three parts:

1. Development of an object-oriented algorithm for Rosenblatt’s Perceptron, applied to a linearly separable problem;
2. Execution of the algorithm with different configurations, as well as an efficiency analysis;
3. Evaluation of the algorithm's application to a non-linearly separable problem.

## Technologies Used
- **Anaconda:** Virtual environment management;
- **Python:** Algorithm implementation using the following libraries:
  - **Pandas:** Data manipulation;
  - **Numpy:** Optimized matrix processing;
  - **Random:** Pseudo-random number generation;
  - **Scikit-learn:** Neuron training metrics;
  - **Matplotlib:** Plotting of graphs;
  - **PrettyTable:** Organization and visualization of tabular data.

## Project Structure
```plaintext
RNA_PP2/
├── .gitignore                  # Git handling to avoid output conflicts on the main branch
├── atividade.ipynb             # Jupyter Notebook containing the project implementation
├── data1.txt                   # Dataset used in the second part of the project
├── dataAll.txt                 # Dataset used in the first part of the project
├── dataHoldout.txt             # Dataset used in the third part of the project
├── environment.yml             # Virtual environment configuration file
└── README.md                   # Project documentation
```

## How to Run
* Make sure Git and Anaconda are properly installed on your machine.
* Open the directory where the code will be executed in the terminal.

1. Clone this repository:
   ```bash
   git clone https://github.com/yoRitayo/RNA_PP2.git
   ```
2. Access the directory related to the repository:
   ```bash
   cd RNA_PP2
   ```

3. Install the virtual environment on your machine:
   ```bash
   conda env create -f environment.yml
   ```
4. Activate the virtual environment:
   ```bash
   conda env activate env_rnapp2 
   ```
5. Open the activity file using Jupyter Notebook:
   ```bash
   jupyter notebook
   ```

## Contributions
Contributions are welcome! If you have suggestions for improvements or want to report issues, feel free to open an [issue](https://github.com/yoRitayo/RNA_PP2/issues) or submit a [pull request](https://github.com/yoRitayo/RNA_PP2/pulls)

## Authors
- Elloá B. Guedes (advisor);
- Davi Aguiar Moreira;
- Ian Garrido Reis;
- Luiz Fernando Borges Brito;
- Pedro Vitor Barros Maranhão;
- Rita De Cassia Brasil Alves.
