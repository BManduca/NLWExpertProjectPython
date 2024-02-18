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

### Pre-commit: A framework for managing and maintaining multi-language pre-commit hooks.
  - install: pip install pre-commit

### Flask: A simple framework for building complex web applications.
  - install: pip3 install Flask

### Python-barcode: Create standard barcodes with Python
  - install: pip3 install python-barcode
  - doc: https://python-barcode.readthedocs.io/en/stable/

### Pillow: Python Imaging Library (Fork)
  - install: pip3 install pillow

### Inicializando servidor Flask
  ```
    from flask import Flask

    app = Flask(__name__)

    # para rodar servidores em Flask, é preciso definir a função main
    if __name__ == '__main__':
        app.run(host='0.0.0.0', port=3000)
  ```  

  ### Criando decoradores para inicializar rotas
    - devemos usar o seguinte:
      - @apps.route('')

  ### Codificação para gerar o QRCode, através da biblioteca barcode
    - Code128 -> codificação para geracao de tag

  ### Modularização da aplicação
    - Isto pode ser feito através das Blueprints
      - Blueprints ajudam você a estruturar seu aplicativo organizando a lógica em subdiretórios. Além disso, você pode armazenar seus modelos e arquivos estáticos junto com a lógica no mesmo subdiretório.

  ### PyCache
    - São arquivos que o python cria, para criar um tipo de otimização quando for rodar os projetos 
    - É basicamente como se fosse compilar parte do código e fosse criando esses arquivos .pyc

  ### Views
    - Local para tratar o HTTP

  - ### Http types
    - É onde iremos criar todas as tipagens que iremos ter para o protocolo HTTP

  <!-- Stop 37:22 -->