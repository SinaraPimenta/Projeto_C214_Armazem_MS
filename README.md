# Projeto_C214_Armazem_MS

<p align="center">
<img src="https://github.com/SinaraPimenta/Projeto_C214_Armazem_MS/blob/main/static/images/logo.PNG" height="300" width="300" >
</p>
<p align="center">Figura 1 - Logo do projeto (Fonte: Refactoring Guru)</p>


☕  Um parágrafo da descrição do projeto vai aqui

### 🚀 Começando
Essas instruções permitirão que você obtenha uma cópia do projeto em operação na sua máquina local para fins de desenvolvimento e teste.
Consulte Implantação para saber como implantar o projeto.

### 📋 Pré-requisitos
De que coisas você precisa para instalar o software e como instalá-lo?
Dar exemplos

### 🔧 Instalação
Uma série de exemplos passo-a-passo que informam o que você deve executar para ter um ambiente de desenvolvimento em execução.

Diga como essa etapa será:

Dar exemplos
E repita:

Até finalizar
Termine com um exemplo de como obter dados do sistema ou como usá-los para uma pequena demonstração.

### ⚙️ Executando os testes
A implementação dos testes de unidade  foi feita utilizando o framework de teste para Python chamado Unittest e foram implementadas os seguintes casos de teste: AdministradorTest, CafeicultorTest e  WebScrappingTest.

**Para execução dos testes via uma IDE, basta executar o arquivo que contém os testes.**

**Para execução dos testes via terminal:**

**1°)** Garanta que o terminal esteja aberto na pasta do projeto;

**2°)** Execute o comando a seguir especificando o caminho até o arquivo contendo os testes: python -m unittest path/../../nomeArquivo.py

Exemplo: 
  ```
  python -m unittest src/unittest/model/testAdministrador.py
  ```
  
### Lista de testes implementados com seus respectivos objetivos:

**Na classe AdministradorTest**:

- **test_buscarCafeicultorBdVazio**: verifica o retorno do método buscarCafeicultores quando não há nenhum cafeicultor registrado no sistema. No caso o retorno esperado é uma string contendo o html de uma tabela vazia.

- **test_buscarCafeicultor**: também verifica o retorno do método buscarCafeicultores, porém quando há um cafeicultor cadastrado no banco de dados. No caso o retorno esperado é uma string contendo o html de uma tabela cuja primeira linha contém os dados do cafeicultor cadastrado.

- **test_cadastrarCafeicultor**: verifica se o método cadastrarCafeicultor adiciona corretamente o objeto cafeicultor no array de cafeicultores e, consequentemente, cadastra o usuário no banco de Dados. Para tal, o método de cadastro é invocado e as comparações são feitas entre o retorno do método get  e os parâmetros informados no cadastro.

- **test_editarCafeicultor**: verifica se o método editarCafeicultor modifica corretamente os atributos do objeto cafeicultor. A análise é feita de modo semelhante ao teste anterior.

- **test_excluirCafeicultor**: verifica se o método excluirCafeicultor consegue apagar o cafeicultor do sistema. Para tal, o método de remoção é invocado e analisa-se a ocorrência de uma exceção do tipo IndexError ao utilizar o método get.

**Na classe CafeicultorTest**:

- **test_buscarCafeBdVazio**: verifica o retorno do método buscarCafe quando não há nenhuma saca cadastrada. No caso o retorno esperado é uma string contendo o html de uma tabela vazia.

- **test_buscarCafe**: também verifica o retorno do método buscarCafe, porém quando há uma saca de café cadastrada no banco de dados. No caso o retorno esperado é uma string contendo o html de uma tabela cuja primeira linha contém os dados da saca registrada.

- **test_cadastrarCafe**: verifica se o método cadastrarCafe adiciona corretamente o objeto SacaCafe no array e no banco de Dados. Para tal, o método de cadastro é invocado e as comparações são feitas entre o retorno do método get e os parâmetros informados no cadastro.

- **test_editarCafe**: verifica se o método editarCafe modifica corretamente os atributos do objeto saca de café. A análise é feita de modo semelhante ao teste anterior.

- **test_excluirCafe**: verifica se o método excluirCafe consegue apagar o item do sistema. Para tal, o método de remoção é invocado e analisa-se a ocorrência de uma exceção do tipo IndexError ao utilizar o método get.


**Na classe WebScrappingTest**: (Nela foi utilizado um objeto Mock, que foi implementado por meio do unittest.mock)

- **test_cotacaoCafe**: verifica se o método cotacaoCafe() é chamado uma vez.

- **test_exception_webScrapping**: testa o lançamento de uma exceção durante a requisição de acesso a página web.



### 📦 Desenvolvimento
  O projeto foi criado com o PyBuilder, com o comando:
  ```
  pyb --start-project
  ```
  A estrutura de pastas foi modificada para atender ao modelo MVC (Model, View e Controller). Porém, com o uso do Flask para o desenvolvimeto de uma interface web, a estrutura da interface foi colocada na raiz do projeto de modo a atender o formato esperado por essa ferramenta (arquivos estáticos na pasta Static e arquivos html em Templates).
  Abaixo segue um esboço da estrutura usada:
  
  📂ArmazemMS/
  
      server.py
      📂src/
          📂main/
              📂controller/
                  bancoDeDados.py
                  mediador.py
                  webScrapping.py
              📂model/
                  administrador.py
                  cafeicultor.py
                  sacaCafe.py
                  usuario.py
          📂unittest/
              📂controller/
                  testWebScrapping.py
              📂model/
                  testAdministrador.py
                  testCafeicultor.py
      📂static/
          📂bootstrap/
              arquivos diversos
          📂css/
              arquivos.css
          📂images/
              imagens
          📂js/
              arquivos.js
      📂templates/
          arquivos.html
  
  O front-end da aplicação foi feito em Html, utilizando do Bootstrap e CSS para estilização e do Javascript para implementação de algumas funcionalidades. O back-end foi desenvolvido em Python, sendo aplicado o [design pattern Mediator](https://refactoring.guru/pt-br/design-patterns/mediator). Este foi aplicado para diminuir o acoplamento das classes, permitindo também evitar o problema de importação circular.
  
  O Mediator é um padrão de projeto comportamental que traz a ideia de utilizar um objeto mediador para reduzir o acoplamento entre classes, facilitar as modificações de código, reutilização e extensão. A imagem a seguir ilustra a ideia desse padrão:
  
  <p align="center">
  <img src="https://refactoring.guru/images/patterns/diagrams/mediator/structure.png" height="500">
  </p>
	 <p align="center">Figura 2 - Lógicad do Mediator (Fonte: Refactoring Guru)</p>

  Por fim, os testes de unidade foram desenvolvidos para o back-end apenas.


### 🛠️ Construído com

**IDE**: [Visual Studio Code](https://code.visualstudio.com/)

**Linguagens**: [Python](https://www.python.org/), [Html, CSS e Javascript](https://www.devmedia.com.br/primeiros-passos-no-html5-javascript-e-css3/25647)

**Automatização da Build / Gerenciamento de dependências**: [PyBuilder](https://pybuilder.io/)

**Controle de versões**: [GitHub](https://github.com/)

**Framework de teste**: [Unittest](https://docs.python.org/3/library/unittest.html)

**Integração Contínua**: [Travis](https://travis-ci.org/)

**Armazenamento de dados**: [MongoDB Atlas](https://www.mongodb.com/)

**Interface Gráfica**: [Bootstrap](https://getbootstrap.com/)

**Principais bibliotecas utilizadas**: 

- para uso do MongoDB: [pymongo](https://pypi.org/project/pymongo/) e [bson](https://pypi.org/project/bson/)

- para uso do WebScrapping: [bs4](https://pypi.org/project/beautifulsoup4/) e [requests](https://pypi.org/project/requests/)

- para uso do Servidor: [flask](https://pypi.org/project/Flask/)

- para Testes: [unittest](https://pypi.org/project/unittest/), [unittest.mock](https://pypi.org/project/unittest/) e [nose.tools](https://pypi.org/project/nose/)


### 📌 Versão
O GitHub foi usado para controle de versão. Para as versões disponíveis, observe as [tags neste repositório](https://github.com/SinaraPimenta/Projeto_C214_Armazem_MS/tags).

## ✒️ Autores

* **Mariana Helena Inês Moreira** - [Mariana](https://github.com/Mariana-Helena)
* **Sinara Pimenta Medeiros** - [Sinara](https://github.com/SinaraPimenta)

### 📄 Licença
Este projeto está sob a licença MIT - veja o arquivo [LICENSE.txt](https://github.com/SinaraPimenta/Projeto_C214_Armazem_MS/blob/main/LICENSE.txt) para detalhes.

⌨️ com ❤️ por Mariana e Sinara 😊
