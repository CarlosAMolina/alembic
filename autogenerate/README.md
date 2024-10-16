## Introduction

Folder to analyze how to work with the autogenerate option.

## How it works

- Create the alembic project and update the required files as described in the main README file of this project.
- If not exists, create the `alembic/versions` folder.
- Run docker: `make docker-run`.
- Create migration: `alembic revision --autogenerate -m "add customers model"`.
- Execute migration: `make alembic-run-migration`.
