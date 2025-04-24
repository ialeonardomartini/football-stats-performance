# 📊 Brasileirão Stats Scraper

Scraper de dados históricos e atuais da Série A do Campeonato Brasileiro direto do site [FBref](https://fbref.com/pt/). O projeto coleta os dados dos jogos e armazena em um banco SQLite local utilizando SQLAlchemy e Pydantic para estrutura e validação.

---

## 🏗️ Estrutura do Projeto

```
football-stats-performance/
│
├── app/
│   ├── db/
│   │   ├── database.py         # Configuração do banco SQLite
│   │   ├── models.py           # Modelos SQLAlchemy (JogoHistorico, JogoAtual)
│   │   ├── crud.py             # Funções de inserção no banco
│   └── schemas/
│       ├── jogo_historico.py   # Schema Pydantic para dados históricos
│       ├── jogo_atual.py       # Schema Pydantic para dados da temporada atual
│
├── data/
│   └── brasileirao.db          # Banco de dados SQLite gerado
│
├── scrape_jogos_historicos.py     # Raspagem de 2014 a 2024
├── scrape_temporada_atual.py      # Raspagem da temporada atual (link fixo)
└── README.md
```

---

## 🔎 Funcionalidades

- 🕰️ Coleta de dados históricos (2014–2024)
- 📆 Raspagem da temporada atual com jogos realizados e futuros
- 🧱 Armazenamento via SQLite
- 🛠️ Estrutura modular com SQLAlchemy + Pydantic

---

## 🐍 Como executar

### 1. Clonar o repositório

```bash
git clone https://github.com/ialeonardomartini/football-stats-performance.git
cd football-stats-performance
```

### 2. Criar ambiente virtual

```bash
python -m venv venv
source venv/bin/activate  # ou venv\Scripts\activate no Windows
```

### 3. Instalar dependências

```bash
pip install -r requirements.txt
```

### 4. Rodar os scrapers

- **Histórico (uma vez):**

```bash
python scrape_jogos_historicos.py
```

- **Temporada atual:**

```bash
python scrape_temporada_atual.py
```

---

## 📂 Banco de Dados

O banco de dados SQLite será salvo em:  
```
./data/brasileirao.db
```

Com as seguintes tabelas:
- `jogos_resultados` – temporadas de 2014 a 2024
- `jogos_temporada_atual` – temporada atual (dados com placar ou futuros)

---

## ✍️ Autor

Desenvolvido por [Leonardo R. Martini](https://www.linkedin.com/in/leonardormartini/)  
GitHub: [@ialeonardomartini](https://github.com/ialeonardomartini)

---

## 📜 Licença

MIT License
