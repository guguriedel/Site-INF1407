# 🎬 CineApp - Sua Biblioteca de Filmes Pessoal

> Um projeto web desenvolvido com Django para gerenciar uma coleção pessoal de filmes, incluindo funcionalidades completas de CRUD (Criar, Ler, Atualizar, Deletar) e um sistema robusto de autenticação de usuários.

## 🚀 Escopo do Projeto (Funcionalidades)

Este projeto foi desenvolvido como uma aplicação web completa para a organização de filmes, onde cada usuário possui sua própria coleção privada. As principais funcionalidades implementadas são:

* **Autenticação Completa de Usuários:**
    * **Cadastro (Registro):** Permite que novos usuários criem uma conta no sistema.
    * **Login e Logout:** Sistema de login seguro baseado em sessões para autenticação dos usuários.
    * **Alteração de Senha:** Usuários logados podem alterar suas próprias senhas.
    * **Recuperação de Senha:** Funcionalidade de "Esqueci minha senha" que envia instruções para o e-mail do usuário (renderizado no console para fins de desenvolvimento).

* **Gerenciamento de Filmes (CRUD):**
    * **Criar:** Adicionar novos filmes à coleção pessoal do usuário. Cada filme fica associado ao usuário que o cadastrou.
    * **Ler (Listar):** Visualizar todos os filmes cadastrados pelo usuário logado, com opções de busca e ordenação.
    * **Atualizar (Editar):** Editar as informações de um filme já existente na coleção.
    * **Deletar:** Remover um filme da coleção após uma etapa de confirmação.

* **Busca e Filtragem Avançada:**
    * Sistema de busca na página de listagem que permite filtrar filmes por **nome**, **gênero** ou **nota mínima**.
    * Opções para **ordenar** os resultados por data de lançamento (mais recentes), nome (A-Z ou Z-A), nota (maior ou menor) e duração.

* **Segurança e Autorização:**
    * As páginas de gerenciamento de filmes (listar, criar, editar, deletar) são protegidas e acessíveis **apenas para usuários autenticados**.
    * Um usuário não pode ver, editar ou deletar filmes que foram cadastrados por outro usuário.

## 🛠️ Tecnologias Utilizadas

* **Backend:** Python 3, Django Framework
* **Frontend:** HTML5, Bootstrap 4
* **Banco de Dados:** SQLite3 (padrão do Django)

## ⚙️ Configuração do Ambiente (Como Instalar)

Para executar este projeto em uma máquina local, siga os passos abaixo:

1.  **Clonar o Repositório:**
    ```bash
    git clone <url-do-seu-repositorio>
    cd nome-do-repositorio
    ```

2.  **Criar e Ativar o Ambiente Virtual (`venv`):**
    ```bash
    # Criar o ambiente
    python3 -m venv venv

    # Ativar no Mac/Linux
    source venv/bin/activate

    # Ativar no Windows
    venv\Scripts\activate
    ```

3.  **Instalar as Dependências:**
    Todas as bibliotecas necessárias estão listadas no arquivo `requirements.txt`.
    ```bash
    pip install -r requirements.txt
    ```

4.  **Aplicar as Migrações do Banco de Dados:**
    Este comando cria o arquivo de banco de dados e todas as tabelas necessárias.
    ```bash
    python manage.py migrate
    ```

5.  **Criar um Superusuário:**
    Para acessar a área de administração do Django, crie um superusuário.
    ```bash
    python manage.py createsuperuser
    ```

## ▶️ Como Executar o Projeto

Com o ambiente configurado, execute o servidor de desenvolvimento do Django:

1.  Certifique-se de que seu ambiente virtual (`venv`) esteja ativado.
2.  Execute o comando:
    ```bash
    python manage.py runserver
    ```
3.  Acesse o site no seu navegador em: `http://127.0.0.1:8000`

## 📖 Manual do Usuário (Como Usar o Site)

### 1. Criando uma Conta e Fazendo Login
* Na barra de navegação, clique em **"Registrar"**. Preencha o formulário para criar sua conta. Após o sucesso, você será redirecionado para a página de login.
* Clique em **"Login"** e insira seu nome de usuário e senha.

### 2. Navegando pela Coleção
* Após o login, você será redirecionado para a página **"Minha Coleção"**, onde todos os seus filmes serão listados.
* Utilize o formulário no topo da página para **filtrar** os filmes por nome, gênero ou nota.
* Use o campo **"Ordenar por"** para reorganizar a lista de acordo com sua preferência.

### 3. Adicionando um Novo Filme
* Na página "Minha Coleção", clique no botão **"Adicionar Novo Filme"**.
* Preencha o formulário com as informações do filme (título, nota, duração, etc.) e clique em "Salvar". Você será redirecionado de volta para a sua coleção, agora com o novo filme adicionado.

### 4. Editando e Deletando um Filme
* Na lista de filmes, cada filme possui os botões **"Editar"** e **"Deletar"**.
* Ao clicar em **"Editar"**, você será levado a um formulário pré-preenchido com os dados do filme para fazer as alterações desejadas.
* Ao clicar em **"Deletar"**, você será levado a uma página de confirmação para evitar a exclusão acidental do filme.

### 6. Gerenciando sua Conta
* Quando logado, seu nome de usuário aparecerá no canto superior direito.
* Clicando no seu nome, um menu dropdown aparecerá com as opções:
    * **"Alterar Senha"**: Permite que você defina uma nova senha, desde que saiba a senha atual.
    * **"Logout"**: Encerra sua sessão de forma segura e te redireciona para a página inicial.