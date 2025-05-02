import docker

client = docker.from_env()

# Criacao de container
# client.containers.run("nginx", detach=True, ports={"80/tcp": ("0.0.0.0", 8080)})

#listar todos os containers
# lista_container = client.containers.list(all=True)
# for item in lista_container:
#     print(f'{item.id} - {item.status} - {item.name}')
    
# #pegar info de um container    
container = client.containers.get("b1577d33763b944d936207deeca8342aefea6b395768f0c9b49295d29e5eae81")
# print(f'{container.id} - {container.status} - {container.name}')
# #printar os logs de um container 
# print(container.logs())

#deleter um container
container.remove(force=True)
#print pra mostra os se deletou
lista_container = client.containers.list(all=True)
for item in lista_container:
    print(f'{item.id} - {item.status} - {item.name}')