# Backend Concurrency Test

Este projeto demonstra como o Django se comporta com funções assíncronas e síncronas ao mesmo tempo. Ele executa um loop com espera síncrona em uma view e uma função assíncrona em outra, permitindo comparar o comportamento de cada abordagem.

## Como Executar

Siga os passos abaixo para executar o projeto localmente:

1. Clone o repositório do GitHub para o seu ambiente local:
    ```bash
    git clone https://github.com/seu_usuario/backend_concurrency.git
    ```

2. Navegue até o diretório do projeto:
    ```bash
    cd backend_concurrency
    ```

3. Crie e ative um ambiente virtual:
    ```bash
    python -m venv env
    source env/Scripts/activate  # Para usuários do Windows
    ```
4. Certifique-se de ter o Uvicorn instalado. Se não estiver instalado, você pode instalá-lo com o seguinte comando:
    ```bash
    pip install uvicorn
    ```

5. Inicie o servidor Uvicorn para executar a aplicação Django:
    ```bash
    uvicorn --reload asyncviews.asgi:application
    ```

6. Uma vez que o servidor esteja em execução, você poderá acessar os seguintes endpoints:
    - [http://localhost:8000/api/](http://localhost:8000/api/): Aguarda 5 segundos antes de retornar uma resposta JSON com a mensagem "Hello World".
    - [http://localhost:8000/sync/](http://localhost:8000/sync/): Executa um loop com espera síncrona por 10 segundos e, em seguida, retorna "Blocking HTTP request".
    - [http://localhost:8000/async/](http://localhost:8000/async/): Executa uma função assíncrona que aguarda 5 segundos e, em seguida, retorna "Non-blocking HTTP request".

Certifique-se de que o Uvicorn está instalado e em execução para testar corretamente os endpoints fornecidos.

## Autor

Este projeto foi desenvolvido por Cristiano Tobias, com auxílio da EBAC - Escola de Tecnologia.

Sinta-se à vontade para contribuir ou relatar problemas criando uma issue ou enviando um pull request.
