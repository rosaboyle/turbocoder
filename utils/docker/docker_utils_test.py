import unittest
import docker

# Assuming the provided code is in a file named 'docker_utils.py'
from docker_utils import list_running_containers, execute_command_in_container, handle_exit_code

class TestDockerUtils(unittest.TestCase):

    def setUp(self):
        # This method will be called before each test
        self.client = docker.from_env()

    def test_list_running_containers(self):
        containers = list_running_containers()
        self.assertIsInstance(containers, list)
        for container in containers:
            self.assertIsInstance(container, tuple)
            self.assertEqual(len(container), 2)

    def test_execute_command_in_container(self):
        # For this test, we assume there's a running container.
        # Ideally, you'd set up a test container for this purpose.
        containers = list_running_containers()
        if containers:
            name, container_id = containers[0]
            exit_code, output = execute_command_in_container(container_id, "echo 'Hello'")
            self.assertEqual(exit_code, 0)
            self.assertEqual(output.strip(), "Hello")

    def test_handle_exit_code(self):
        # This test checks if the function prints the expected output.
        # It's a bit tricky since handle_exit_code prints to stdout.
        # We'll redirect stdout temporarily to capture the print statements.
        import io
        from contextlib import redirect_stdout

        f = io.StringIO()
        with redirect_stdout(f):
            handle_exit_code(0, "Hello")
        s = f.getvalue()
        self.assertIn("Command executed successfully!", s)
        self.assertIn("Hello", s)

        # You can add more tests for other exit codes as needed.

if __name__ == "__main__":
    unittest.main()
