import socket

HOST = '127.0.0.1'
PORT = 65432

def run_server():
    try:
        with socket . socket (socket.AF_INET,socket.SOCK_STREAM) as s:
            s.bind((HOST , PORT))
            s.listen()
            print(f"Server listening on {HOST}: {PORT}")
            conn,addr = s.accept()
            with conn:
                print(f"connected by {addr}")
                message = "hello from server!"
                conn.sendall(message.encode('utf-8'))
                print("message sent to client")

        except sockect error as e: 
           print(f"server error : {e}")
    except Exception as e:
         print(f"an unexpected server error occured:{e}")

         if_name_=='_main_':
         run_server()

