# loan-shark-service-python

## Migrations
```
pip install psycopg2-binary
pip install alembic

alembic init alembic
```
- update url database em alembic.ini, and execute:
```
alembic revision --autogenerate -m "First migration"
```
- generate file configuration script sql
```
alembic revision -m "create table"
```
- modify revision, include script modify em upgrade e rollback em downgrade
```
alembic upgrade head #create table 
#or
alembic downgrade -1
```
- lembrando que o alembic precisa dos metadados no arquivo alembic/env.py
```
from domain.loan import Base

target_metadata = Base.metadata
```