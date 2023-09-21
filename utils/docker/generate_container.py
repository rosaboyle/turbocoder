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
        print(f"Container with image {image_name} is already running.")
        return

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
