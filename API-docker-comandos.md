## para comunicacao local usamos o docker.sock que nada mais é que um documento de refencia de um endpoint espicifico

* Nesse caso como vamos trabalhar localmente vamos usar o curl para as comunicacoes e chamadas

### pegar o docker version atraves da api do docker no linux
        curl --unix-socket /var/run/docker.sock http://localhost/version

* Para formatar a saída no formato json
        curl --unix-socket /var/run/docker.sock http://localhost/version | jq .

    * para instalar o jq no ubuntu
        sudo apt-get update && sudo apt install jq -y

### para exibir a info do docker
        curl --unix-socket /var/run/docker.sock http://localhost/info | jq .

### para executar um container usando a api do docker temos que primeiramente fazer o pull da imagem (que na api é no mesmo endpoint do images/create)
        curl --unix-socket /var/run/docker.sock -X POST http://localhost/images/create?fromImage=nginx:latest

* nao precisa usar o parametro -d para passar um body porque passamos as info da iamge como query parameter (?fromImage=<image>:<tag>)
* o parametro -X define o verbo da requisicao (nesse caso um POST)

#### apos a requisicao para fazer o pull da imagem, entao sim criamos o container
        curl --unix-socket /var/rum/docker.sock -X POST -d '{"image":"nginx"}' - H "Content-Type: application/json" http://localhost/containers/create

* onde o parametro -d é o body da requisicao (onde passamos informacao como qual imagem e etc)
* o parametro -H é o header da requisicao (onde passamos informacao como qual formato da requisicao, nesse caso json)

    * para expor a porta via api, podemos criar um arquivo.json com as informacoes e passar na chamar
            {
                "image": "nginx",
                "HostConfig": {
                    "PortBindings": {
                        "80/tcp": [
                            {
                                "HostIp": "0.0.0.0",
                                "HostPort": "8080"
                            }
                        ]
                    }
                }
            }

#### chamada de criacao expondo a porta
        curl --unix-socket /var/run/docker.sock -d @chamada.json -H "Content-Type: application/json" http>//localhost/containers/create

* O @ passa um arquivo

#### apos a criacao entao startamos o container
        curl --unix-socket /var/run/docker.sock -X POST http://localhost/containers/<id>/start
        curl --unix-socket /var/run/docker.sock -X POST http://localhost/containers/<id>/stop

* aqui nao precisamo do -d para o body e nem do -H para definir um formato para o body


### para listar um container
    curl --unix-socket /var/run/docker.sock -X GET http://localhost/containers/json | jq .
    curl --unix-socket /var/run/docker.sock -X GET http://localhost/containers/json?all=true | jq .

* o -X GET pra pegar info e o | jq . para formatar como json no terminal


### para deletar um container
    curl --unix-socket /var/run/docker.sock -X DELETE http://localhost/containers/<id>
    curl --unix-socket /var/run/docker.sock -X DELETE http://localhost/containers/<id>?force=true

* basicamente muda so verbo -X DELETE
