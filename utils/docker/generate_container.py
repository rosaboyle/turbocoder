import docker


def list_all_images():
    client = docker.from_env()
    images = client.images.list()
    
    for image in images:
        print(f"Image ID: {image.id} Tags: {image.tags}")


def run_container(image_name):
    client = docker.from_env()
    
    # Check if the container with the given image name is already running
    containers = client.containers.list(filters={"ancestor": image_name})
    
    if containers:
        print(f"Container(s) with image {image_name} is/are already running.")
        for container in containers:
            print(f" - ID: {container.id}, Name: {container.name}, Status: {container.status}")
        
        choice = input("Do you want to create a new container? (Y/n): ").strip().lower()
        
        if choice == "n" or choice == "N":
            container_id = input("Enter the ID of the container you want to use: ").strip()
            return container_id
    # Run a new container with the dummy command to keep it running indefinitely
    container = client.containers.run(
        image=image_name,
        command="tail -f /dev/null",
        detach=True,  # Run in detached mode
        restart_policy={"Name": "always"}  # Restart always policy
    )
    print(f"Started container with ID {container.id} using image {image_name}.")

if __name__ == "__main__":
    list_all_images()
    image_name = input("Enter the Docker image name you want to keep running: ")
    run_container(image_name)
