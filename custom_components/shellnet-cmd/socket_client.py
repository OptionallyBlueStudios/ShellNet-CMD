import socket

def send_command(host: str, port: int, command: str) -> str:
    """Send a command string over TCP to the specified host and port."""
    try:
        with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
            s.connect((host, port))
            # Send raw string (add "\n" manually in the command if your server expects it)
            s.sendall(command.encode())
        return f"Command '{command}' sent successfully to {host}:{port}"
    except Exception as e:
        return f"Failed to send command to {host}:{port} - {e}"
