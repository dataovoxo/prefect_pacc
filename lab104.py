import httpx
from prefect import flow, task, get_run_logger
from prefect.tasks import task_input_hash

@task
def fetch_cat_fact():
    return httpx.get("https://catfact.ninja/fact?max_length=140").json()["fact"]


@task
def formatting(fact: str):
    return fact.title()

@task
def write_fact(fact: str):
    with open("fact.txt", "w+") as f:
        f.write(fact)

    return "Success!!"

@flow
def pipe(name: str = "Ovo"):
    logger = get_run_logger()
    fact = fetch_cat_fact()
    formatted_fact = formatting(fact)
    msg = write_fact(formatted_fact)
    logger.info(f"printing name variable---{name}")
    print(msg)

if __name__ == "__main__":
    pipe()