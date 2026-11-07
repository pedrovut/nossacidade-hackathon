# Nossa cidade - HACKATHON 2026

## Tema
    
### Cidades inteligentes
    A cidade Nova Esperança passa por diversos problemas de administração, como bairros ao norte da cidade sem luz, bairros da regiao central com buracos nas ruas, outras regiões com descarte irregular de lixo, etc. E mesmo com a prefeitura tendo seus canais de comunicação para receber solicitações, parte da populaçao relatam problemas para identificar o processo e acompanhar se as demandas estão sendo feitas.

## Resolução dos problemas
    Para resolver o problema pensamos em um site que compartilhe os relatos da comunidade e acompanhe os problemas para demonstrar o processo da prefeitura na manutenção, as solicitações aparecem na tela inicial acompanhada de uma categoria, descrição e engajamento. Em geral, a ideia é informar a comunidade sobre problemas urbanos no municipio, afim de informar o processo de admnistração da prefeitura sobre os problemas.

## Lista de membros
    - NOME: Daniel Próspero     RGM: 114.070
    - NOME: Gabriel Augusto     RGM: 114.062
    - NOME: Pedro Pereira       RGM: 114.047

## Diretórios das pastas
    Nossa Cidade/
    ├── .venv/
    ├── accounts/  
    │   ├── migrations/
    │   │   └── __init__.py
    │   ├── templates/
    │   │   └── accounts/
    │   │       ├── user_form_create.html
    │   │       └── user_login.html
    │   ├── __init__.py
    │   ├── admin.py
    │   ├── apps.py
    │   ├── forms.py
    │   ├── models.py
    │   ├── tests.py
    │   ├── url.py
    │   └── views.py
    ├── app/
    │   ├── __init__.py
    │   ├── asgi.py
    │   ├── settings.py
    │   ├──urls.py
    │   └── wsgi.py
    ├── nossacidade/  
    │   ├── migrations/
    │   │   └── __init__.py
    │   ├── static/
    │   │   └──nossacidade
    │   │      ├── css
    │   │      │  └──nossacidade.css
    │   │      ├── img
    │   │      │  └── logo.png
    │   │      └── js
    │   │         └── home.js
    │   ├── templates/
    │   │   └── nossacidade/
    │   │       ├── _card.html
    │   │       ├── _form_relato.html
    │   │       ├── base.html
    │   │       ├── inicio.html
    │   │       ├── perfil.html
    │   │       ├── reclamacao_create.html
    │   │       ├── reclamacao_delete.html
    │   │       ├── reclamacao_detail.html
    │   │       ├── reclamacao_list.html
    │   │       └── reclamacao_update.html
    │   ├── __init__.py
    │   ├── admin.py
    │   ├── apps.py
    │   ├── models.py
    │   ├── prioridades.py
    │   ├── tests.py
    │   ├── url.py
    │   └── views.py
    ├── manage.py
    ├── .gitignore
    ├── db.sqlite3
    ├── README.md
    └── requirements.txt

## Como rodar

    1. Abra o terminal e digite o comando:
    python -m venv .venv

    2. Ative o ambiente virtual
    .venv\Scripts\Activate.ps1
    .venv\Scripts\activate

    3. Instale as bibliotecas necessarias do requirements.txt
    python.exe -m pip install --upgrade pip
    pip install django
    pip install pillow

    4. Rode o servidor:
    python manage.py runserver
    e acesse http://127.0.0.1:8000 no navegador

## TECNOLOGIAS UTILIZADAS

- Utilizamos o framework Django unido a ferramentas de IA como Claude e Gemini para auxiliar no desenvolvimento do prototipo, backend e frontend.