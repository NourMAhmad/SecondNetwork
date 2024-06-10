import socket
def main():
    client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    client.connect(('127.0.0.1', 5555))
    # Authentication
    response = client.recv(1024).decode()
    print(response, end='', flush=True)
    username = input()
    client.send(username.encode())
    response = client.recv(1024).decode()
    print(response, end='', flush=True)
    password = input()
    client.send(password.encode())
    response = client.recv(1024).decode()
    print(response, flush=True)
    while True:
        print("Options:")
        print("1. Check Balance 2. Deposit 3. Withdraw 4. Exit")
        choice = input("Enter your choice: ")
        if choice == '1':
            client.send("check_balance".encode())
            balance = client.recv(1024).decode()
            print(balance, flush=True)
        elif choice == '2':
            amount = float(input("Enter amount to deposit: "))
            client.send(f"deposit {amount}".encode())
            response = client.recv(1024).decode()
            print(response, flush=True)
        elif choice == '3':
            amount = float(input("Enter amount to withdraw: "))
            client.send(f"withdraw {amount}".encode())
            response = client.recv(1024).decode()
            print(response, flush=True)
        elif choice == '4':
            client.send("exit".encode())
            print("Exiting.", flush=True)
            break
        else:
            print("Invalid choice.", flush=True)
    client.close()
if __name__ == "__main__":
    main()
