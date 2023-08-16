from prefect.deployments import run_deployment

def main():
    response = run_deployment(name="lab105.py:animal_facts/lab5_deployment")
    print(response)

if __name__ == "__main__":
    main()