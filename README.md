# SolarApp

Base inicial do **SolarApp** para deploy barato em lab usando:
- **Supabase** (Postgres)
- **Render** (Web Service com Docker)
- **GitHub Secrets** (segredos)

## Estrutura

- `src/main.py`: API FastAPI mínima
- `requirements.txt`: dependências Python
- `Dockerfile`: build do container
- `render.yaml`: blueprint opcional do Render
- `.env.example`: variáveis de ambiente esperadas
- `.gitignore`: arquivos locais ignorados

## Rodar local

```bash
python -m venv .venv
# Windows
.venv\Scripts\activate
# Linux/macOS
# source .venv/bin/activate

pip install -r requirements.txt
uvicorn src.main:app --host 0.0.0.0 --port 8000 --reload
```

Abra:
- `http://localhost:8000/`
- `http://localhost:8000/health`

## Variáveis de ambiente

Copie `.env.example` para `.env` e ajuste:

- `DATABASE_URL`: string do Supabase com `sslmode=require`
- `APP_ENV`: `lab` ou `prod`
- `PORT`: porta (Render injeta automaticamente)

## Deploy no Render (sem CI/CD)

1. Crie um **Web Service** conectando este repositório.
2. Defina **Environment Variables** (manual ou via automação/chat):
   - `DATABASE_URL`
   - `APP_ENV=lab`
3. Build Command: *(vazio, usa Dockerfile)*
4. Start Command: *(vazio, usa CMD do Dockerfile)*
5. Health Check Path: `/health`

## Segredos via GitHub

Armazene no GitHub Secrets:
- `DATABASE_URL`

Depois, sincronize para Render (manual ou automação por chat/MCP).

## Próximos passos

- Adicionar camada de acesso a banco (`SQLAlchemy`) com endpoint de teste de conexão.
- Adicionar módulos de domínio do SolarApp.
- Opcional: Terraform/OpenTofu para provisionamento idempotente.
