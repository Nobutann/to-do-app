# Lista de Tarefas com Django

Projeto de uma lista de tarefas feito com django que permite o usuário gerenciar uma lista de afazeres.

---

## Funcionalidades

- Adicionar novas tarefas
- Verificar se elas estão completas ou não
- Modificar as tarefas e alternar se elas estão ou não completas
- Excluir tarefas

--- 

## Tecnologias utilizadas

- Python
- Django
- HTML/CSS
- SQLite

---

## Como rodar

1. Clone o repositório:
    ```bash
    git@github.com:Nobutann/to-do-app.git
    ```
2. Crie um ambiente virtual:
    No Windows:
    ```bash
    python -m venv venv
    venv/Scripts/activate
    ```
    Outros:
    ```bash
    python -m venv venv
    source venv/bin/activate
    ```
3. Instale as dependências:
    ```bash
    pip install -r requirements.txt
    ```
4. Rode as migrações:
    ```bash
    python manage.py migrate
    ```
5. Inicie o servidor:
    ```bash
    python manage.py runserver
    ```

## Créditos

Feito por **Luiz Gonzaga**

- [GitHub](https://github.com/Nobutann)
- [LinkedIn](https://linkedin.com/in/gonzaga07/)