# Comandos para Interação com a API Docker

Este guia tem como objetivo ensinar como usar comandos do `curl` para se comunicar com a API Docker localmente, utilizando o socket Unix (`docker.sock`). Isso é útil para interagir diretamente com o daemon Docker e obter informações sobre o estado e a configuração do Docker.

---

## O que é o `docker.sock`?
O `docker.sock` é um arquivo que funciona como um **endpoint** para comunicação local com o Docker. Ele permite que você envie comandos diretamente para o daemon Docker, como se estivesse utilizando o cliente Docker (`docker CLI`).

### Importante:
- Este método é geralmente usado em sistemas Linux. No Windows, o Docker utiliza **Named Pipes (npipe)** ou API REST HTTP.
- É necessário ter permissões adequadas para acessar o arquivo `docker.sock`.

---

## Comandos Disponíveis

### **1. Obter a Versão do Docker**
Este comando retorna as informações da versão do Docker instalado no sistema.

**Comando:**
```bash
curl --unix-socket /var/run/docker.sock http://localhost/version