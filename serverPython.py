# Importa todo do módulo de sockets
from socket import *

# Cria o endereço do meu servidor( host)
myHost = '127.0.0.1'

# Qual o porto utilizado
myPortNumber = 8000

# Cria um objeto socket, onde os parâmetros dizem que vai ser recebido um endereço de IP(AF_INET) e que o protocolo de transferência será TCP(SOCKET_STREAM)
# Combinação das configurações indica que será uma servidor TCP/IP
server = socket(AF_INET, SOCK_STREAM)

# Bincula o servidor ao número de porto
server.bind((myHost, myPortNumber))

#Número de Clientes que pode lida por vez
server.listen(1)

# Informações para o console
print("Servidor iniciado...")
print("Servidor na porta:", myPortNumber)
print("Servidor no endreço:", myHost)

while True:
    # O servidor vai aceitar a conecção, 
    connection, address = server.accept()
    print('Servidor conectado por', address)

    # Converte e armazena a requisiçãoe
    request = connection.recv(1024).decode('utf-8')

    # Aqui vamos pegar toda a mensagem de requisição http e pegar somente o parâmetro de url que determina o arquivo requisitado
    messageTemp = request.split('/')
    messageFile = messageTemp[1].split(' HTTP')
    
    try:

        urlFile = 'C:\\Users\italo\Desktop\www\\''' + messageFile[0]        
        file = open(urlFile, 'rb')# Abre o arquivo(APENAS HTML), r => read , b => byte format
        
        response = file.read()
        
        file.close()

        header = 'HTTP/1.1 200 OK\n'
        tipoarquivo = 'text/html'

        header += 'Content-Type: ' + str(tipoarquivo) + '\n\n'

    except Exception as e:
        header = 'HTTP/1.1 404 Not Found\n\n'
        response = '<html><meta charset= "utf-8"><body><center><h3>Erro 404: Arquivo não encontrado</h3>' \
                   '<p>Servidor Python</p></center></body></html>'.encode('utf-8')

    # Converte o header pra bytes.
    respostafinal = header.encode('utf-8')

    # Concatena a resposta com header.
    respostafinal += response                    

    # Envia a resposta final para o cliente.
    connection.send(respostafinal)                  

    connection.close()

        
    

