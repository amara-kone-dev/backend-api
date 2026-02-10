# Backend API

API REST pour les projets internes de TechShield Solutions CI.

## Stack

- Python 3.10+
- Flask + Flask-RESTful
- PostgreSQL
- JWT Authentication

## Installation

```bash
pip install -r requirements.txt
cp .env.example .env
# Modifier les variables dans .env
python app.py
```

## Endpoints

| Méthode | Route | Description |
|---------|-------|-------------|
| POST | `/api/auth/login` | Connexion |
| GET | `/api/users` | Liste des utilisateurs |
| GET | `/api/projects` | Liste des projets |

## TODO

- [ ] Ajouter la pagination
- [ ] Implémenter le rate limiting
- [ ] Écrire les tests unitaires
