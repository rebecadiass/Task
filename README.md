Projeto de criação de website para organização de tarefas (Cadastro, visualização, exclusão e conclusão)

  REQUISITOS
  dj-database-url==2.0.0
  Django==4.2.1
  python-decouple==3.8
  crispy-bootstrap5==0.7
  usar para todas: ```pip install (nomes acima)```
  
Pré passos
  1. Criar uma página na sua máquina
  2. No VS Code, abrir a pasta criada
  3. Abrir o terminal

Configurações iniciais para a criação do ambiente virtual no VS Code
  1. No terminal, digitar:
     ```python -m venv .venv```
  2. Para ativar o ambiente virtual, digitar:
     ```.venv\Scripts\activate```
  3. O comando exibirá um erro, para resolve-lo, digitar:
     ```Set-ExecutionPolicy -Scope Process -ExecutionPolicy Bypass```
  4. Executar novamente:
     ```.venv\Scripts\activate```

instalação pacote Django
  1. instalar o pacote Django, digitar:
     ```pip install django```

Testaando localhost no navegador
  1. Digitar:
     ```python manage.py runserver```
  3. Inserir na barra de pesquisa superior:
     ```localhost:8000```

Aplicação de migrações
  1. Executar migrações, digitar:
     ```python manage.py migrate```

Criar arquivo ```.env``` no projeto (clicar com botão direito no nome do projeto e adcionar arquivo)
  1. Em .env, digitar: ```SECRET_KEY=django-insecure-g4q@5m+*16xg3pmn&wm#iu4ow&#njdabn-!d6%cay#cc!ucvba```
```DEBUG=True```
```ALLOWED_HOSTS=*```









