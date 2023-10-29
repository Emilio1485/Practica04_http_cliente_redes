import socket
import sys

user_agents = [
    "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.36",
    "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Firefox/52.0 Safari/537.36",
    "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Edge/16.16299 Safari/537.36"
]

def http_client(host, http_method, url, user_agent_choice, encoding, connection):
    port = 80

    client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    try:
        client_socket.connect((host, port))

        request = f"{http_method} {url} HTTP/1.1\r\n"
        request += f"Host: {host}\r\n"
        request += f"User-Agent: {user_agents[user_agent_choice - 1]}\r\n"
        request += "Accept: */*\r\n"
        request += "Accept-Charset: utf-8\r\n"
        request += f"Accept-Encoding: {encoding}\r\n"
        request += "Accept-Language: en-US\r\n"
        request += f"Connection: {connection}\r\n\r\n"

        client_socket.sendall(request.encode())

        response = b""
        while True:
            data = client_socket.recv(1024)
            if not data:
                break
            response += data

        print(response.decode())

    except socket.error as e:
        print(f"Error de conexión: {e}")

    finally:
        client_socket.close()

if __name__ == "__main__":
    if len(sys.argv) != 7:
        print("Uso: python clientHTTP.py <host> <http_method> <url> <user_agent_choice> <encoding> <connection>")
        sys.exit(1)

    host = sys.argv[1]
    http_method = sys.argv[2]
    url = sys.argv[3]
    user_agent_choice = int(sys.argv[4])
    encoding = sys.argv[5]
    connection = sys.argv[6]

    http_client(host, http_method, url, user_agent_choice, encoding, connection)

