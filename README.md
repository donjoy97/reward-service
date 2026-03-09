# Reward Decision Service 

FastAPI microservice that returns deterministic reward decisions for transactions.

## Features

- FastAPI REST API
- Request validation using Pydantic
- Global error handling
- Idempotent request handling
- Redis cache with in‑memory fallback
- Persona based rewards
- Daily CAC cap enforcement
- Unit tests
- Load testing

---

## Architecture

```mermaid
flowchart LR

Client --> API[FastAPI Controller]

API --> VALIDATION[Request Validation]
API --> IDEMPOTENCY[Idempotency Service]

IDEMPOTENCY --> CACHE[Cache Layer]

API --> REWARD[Reward Service]

REWARD --> POLICY[Policy Loader]
REWARD --> PERSONA[Persona Service]
REWARD --> CAC[CAC Service]

CACHE --> REDIS[(Redis)]
CACHE --> MEMORY[(In Memory Cache)]

REWARD --> RESPONSE[Reward Response]

RESPONSE --> Client
```
