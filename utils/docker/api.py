import docker

def list_running_containers():
    client = docker.from_env()
    containers = client.containers.list()
    return [(container.name, container.id) for container in containers]

def execute_command_in_container(container_name_or_id, command):
    client = docker.from_env()
    container = client.containers.get(container_name_or_id)
    exit_code, output = container.exec_run(command)
    return exit_code, output.decode('utf-8')

if __name__ == "__main__":
    # List all running containers
    containers = list_running_containers()
    print("Running Containers:")
    for name, container_id in containers:
        print(f"Name: {name}, ID: {container_id}")

    # Get container name or ID from user
    container_name_or_id = input("Enter the name or ID of the container you want to execute the command in: ")

   
