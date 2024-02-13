# Diário para registros de evolução, descobertas e curiosidades alcançadas durante o curso. 

### Create and Use Virtual Environments
- To create a virtual environment, go to your project’s directory and run the following command. This will create a new virtual environment in a local folder named .venv:
  - python3 -m venv .venv
    - ao executarmos esse comando, será criada a pasta .venv no diretório do projeto e esta pasta terá todo o necessário para ter um ambiente separado da minha máquina e que fique rodando python 
  - Ativando o virtualenv
    - source .venv/bin/activate

### Pylint
- Pylint is a static code analyser for Python 2 or 3.
- install: pip3 install pylint

### snake_case
- São utilizados para Funções, variáveis e métodos

### PascalCase
- Utilizado para Classes

### Organização de código
- o pylint sempre vai exigir que seja realizado uma documentação de módulo, logo no início do documento
- e também documentação sobre a função criada em si.
<!-- 18 MINUTOS -->

### Criando um arquivo geral de configuração
- No terminal, digitar o seguinte comando dentro da pasta do projeto
  - pylint --generate-rcfile > .pylintrc

### Criando um arquivo de todas as dependências/instalações e suas respectivas versões, que estão presentes dentro do projeto
  - dentro do projeto realizar o seguinte comando:
    - .venv/bin/pip3/ freeze > requirements.txt