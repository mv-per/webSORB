from invoke.tasks import task
from invoke.context import Context


@task
def start(c: Context) -> None:
    c.run("gunicorn -k uvicorn.workers.UvicornWorker main:app --reload")


@task
def freeze_requirements(c: Context) -> None:
    c.run("pip list --local --format=freeze > requirements.txt; ")


@task
def cloud_build(c: Context) -> None:
    freeze_requirements(c)
    c.run("gcloud builds submit --tag gcr.io/websorb/api")


@task
def hooks(c: Context) -> None:
    c.run("pre-commit install")
