# MCP Server

A robust Python backend server for managing authentication, data, and APIs using modern best practices. Designed for extensibility, maintainability, and ease of development, MCP Server provides CRUD operations, service layers, schema validation, and database integration out of the box.

## Table of Contents

- [Project Overview](#project-overview)
- [Architecture Summary](#architecture-summary)
- [Installation Instructions](#installation-instructions)
- [Usage Guide](#usage-guide)
- [Configuration Details](#configuration-details)
- [API & Command Documentation](#api--command-documentation)
- [Contributing Guidelines](#contributing-guidelines)
- [License and Credits](#license-and-credits)

---

## Project Overview

**MCP Server** is a Python backend application structured for rapid API development and data management. It leverages modular code organization (APIs, services, CRUD, database models, and more) to streamline both small and large-scale backend projects. Main features include:

- RESTful API endpoints under `api/v1/` for authentication and MCP operations
- Service and CRUD layers for business/data logic
- Schema validation and serialization
- Database integration (migration-ready)
- Extensible utilities for common backend tasks

## Architecture Summary

```
mcp_server/
├── .gitignore
├── alembic.ini         # Database migration settings
├── autogen.py          # Automation/generation scripts
├── requirements.txt    # Python dependencies
├── main.py             # Application entry point
├── __init__.py         # Package marker
├── api/
│   └── v1/
│       ├── auth.py     # Authentication endpoints
│       └── mcp.py      # MCP-specific endpoints
├── core/               # Application core logic/configs
├── crud/               # CRUD operations (data access)
├── db/                 # Database setup and management
├── models/             # ORM or data models
├── schemas/            # Data schemas (validation, serialization)
├── services/           # Business logic/services
└── utils/              # Utility functions/helpers
```

**Directory Roles:**

- `api/v1/`: Defines versioned HTTP routes and request handlers (e.g., authentication, MCP).
- `core/`: Core settings, startup logic, and shared resources.
- `crud/`: Functions for create/read/update/delete database actions.
- `db/`: Database connection, migrations, and setup.
- `models/`: Data models (ORM classes, etc.).
- `schemas/`: Pydantic or marshmallow schemas for validation.
- `services/`: Encapsulates business logic separate from API/controllers.
- `utils/`: Helper utilities reused across the codebase.

## Installation Instructions

### Prerequisites

- Python 3.8+
- [pip](https://pip.pypa.io/en/stable/)

### Steps

1. **Clone the repository**
   ```bash
   git clone https://github.com/minasielemma/mcp_server.git
   cd mcp_server
   ```

2. **Create and activate a virtual environment**
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   ```

3. **Install dependencies**
   ```bash
   pip install -r requirements.txt
   ```

4. **Configure environment variables**
   - Copy `.env.example` to `.env` (if provided) and adjust settings.
   - Or set environment variables manually as described below.

5. **Run database migrations (optional)**
   ```bash
   alembic upgrade head
   ```

## Usage Guide

### Start the Application

```bash
python main.py
```

### Interacting with MCP Server

- Access API endpoints via browser or HTTP client (e.g., Postman, curl).
- Versioned endpoints are under `/api/v1/`.

### Example API Calls

```bash
curl -X POST http://localhost:8000/api/v1/auth/login -d '{"username":"user","password":"pass"}'
curl -X GET http://localhost:8000/api/v1/mcp/data
```

## Configuration Details

| Variable       | Description                           | Example Value       |
| -------------- | ------------------------------------- | ------------------ |
| `DATABASE_URL` | Database connection string            | `sqlite:///./test.db` |
| `SECRET_KEY`   | JWT/Session secret                    | `supersecretkey`   |
| `ENV`          | Environment (dev/prod/test)           | `development`      |

Edit `alembic.ini` for database migration settings as needed.

## API & Command Documentation

Endpoints are defined under `/api/v1/` and implemented in:

- [`api/v1/auth.py`](https://github.com/minasielemma/mcp_server/blob/main/api/v1/auth.py): Authentication endpoints (login, registration, token handling, etc.)
- [`api/v1/mcp.py`](https://github.com/minasielemma/mcp_server/blob/main/api/v1/mcp.py): MCP-specific data and logic endpoints

> **Note:** For a full list of endpoints, refer to the code in the respective files above.

**Typical Endpoints Example:**

| Method | Path                          | Description                  |
| ------ | ----------------------------- | ---------------------------- |
| POST   | `/api/v1/auth/login`          | User login                   |
| POST   | `/api/v1/auth/register`       | User registration            |
| GET    | `/api/v1/mcp/analyze`            | Get MCP data                 |
| POST   | `/api/v1/mcp/emails/since-yesterday`          | Perform MCP action           |

Request and response schemas are defined in the `schemas/` directory.

### Commands

- Run migrations: `alembic upgrade head`
- Generate schema: `python autogen.py`

## Contributing Guidelines

We welcome contributions! To contribute:

1. Fork the repository and create your branch (`git checkout -b feature/fooBar`).
2. Commit your changes (`git commit -am 'Add new feature'`).
3. Push to the branch (`git push origin feature/fooBar`).
4. Open a Pull Request.

**Standards:**

- Write clear commit messages.
- Follow Python style guides (PEP8).
- Add docstrings and comments.
- Update/extend tests for new features.

See [CONTRIBUTING.md](CONTRIBUTING.md) for detailed guidelines (create this file for more info).

## License and Credits

- **License:** _Not specified_ (add a LICENSE file to clarify terms)
- **Authors:** [minasielemma](https://github.com/minasielemma)
- Thanks to all contributors and open-source packages.

---

For more details, see individual files and folders, and raise issues or PRs for questions and improvements.
