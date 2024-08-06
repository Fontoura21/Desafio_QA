#Teste Automatizado de Cadastro de Usuário

Este repositório contém um script de teste automatizado para verificar a funcionalidade de cadastro de usuários em um site específico. O script utiliza o Selenium WebDriver para interagir com o navegador e realizar testes funcionais. 

##Estrutura do Projeto

O projeto está estruturado da seguinte forma:

- `tests/`: Diretório que contém o script de teste.
- `tests/site/testes_cadastro.csv`: Arquivo CSV contendo os dados de teste utilizados para o cadastro.

##Requisitos

Para executar os testes automatizados, os seguintes requisitos devem ser atendidos:

- Python 3.7 ou superior
- Bibliotecas Python:
  - `selenium`
  - `pandas`
  - `numpy`
  - `logging`

##Instalação

1. Clone o repositório para sua máquina local:

   ```bash
   git clone git@github.com:Fontoura21/Desafio_QA.git

2. Crie e ative um ambiente virtual (recomendado):

    ```bash
    python -m venv venv
    source venv/bin/activate  # No Windows, use: venv\Scripts\activate

3. Instale as dependências do projeto:

    ```bash 
    pip install -r requirements.txt

##Descrição do Script de Teste

O script de teste (test_cadastro.py) realiza as seguintes operações:

 - Inicialização: Configura o Selenium WebDriver, abre o navegador e navega até a página de cadastro do site alvo.
 - Execução dos Testes: Lê os dados de teste a partir do arquivo testes_cadastro.csv e preenche o formulário de cadastro para cada conjunto de dados. Verifica se o cadastro foi realizado com sucesso.
 - Finalização: Fecha o navegador e gera um relatório de resultados com logs detalhados.

##Logs

O sistema de logs captura informações detalhadas sobre cada passo do teste, incluindo:

  - Informações de Execução: Hora de início, tempo de execução e status final de cada teste.
  - Erros e Exceções: Mensagens de erro detalhadas caso algum teste falhe, auxiliando na identificação de problemas.
  - Logs de Debug: Informações adicionais úteis para desenvolvedores durante o processo de desenvolvimento e teste.

Os logs são gravados em um arquivo de log especificado no script, permitindo fácil acesso e análise posterior.

