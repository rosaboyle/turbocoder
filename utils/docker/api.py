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


def handle_exit_code(exit_code, output):
    if exit_code == 0:
        print("Command executed successfully!")
        print(output)
    elif exit_code == 125:
        print("Docker runtime error.")
    elif exit_code == 126:
        print("Contained command cannot be invoked.")
    elif exit_code == 127:
        print("Command not found inside the container.")
    elif 128 <= exit_code <= 255:
        print(f"Container process terminated by signal {exit_code - 128}.")
    else:
        print(f"Application-specific error with exit code: {exit_code}.")
        print(output)


if __name__ == "__main__":
    # List all running containers
    containers = list_running_containers()
    print("Running Containers:")
    for name, container_id in containers:
        print(f"Name: {name}, ID: {container_id}")

    # Get container name or ID from user
    #container_name_or_id = input("Enter the name or ID of the container you want to execute the command in: ")

   
    container_id = input("Enter the ID of the Docker container: ")
    command_to_execute = input("Enter the command you want to execute in the container: ")
    
    exit_code, output = execute_command_in_container(container_id, command_to_execute)
    handle_exit_code(exit_code, output)
