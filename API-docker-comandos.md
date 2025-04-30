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