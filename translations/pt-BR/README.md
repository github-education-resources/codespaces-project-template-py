
[![Abrir no GitHub Codespaces](https://github.com/codespaces/badge.svg)](https://github.com/codespaces/new?hide_repo_select=true&ref=main&repo=526682400)

# API HTTP Python com GitHub Codespaces e Copilot

_Execute uma API Python neste repositório pronto para uso em minutos_

Ao abrir este modelo de repositório no Codespaces, você poderá, rapidamente, desenvolver um aplicativo da web Python que serve uma API HTTP. Você poderá se concentrar no trabalho com o projeto em vez de configuração e instalação. Em seguida, você fará alterações no código usando o [GitHub Copilot](https://copilot.github.com/), uma nova ferramenta de conclusão de código alimentada por IA que ajuda você a escrever código mais rapidamente.

## 🚀 Início rápido
1. [Siga as etapas](#--try-it-out) para configurar seu Codespace e executar o aplicativo.
2. [Faça alterações no aplicativo](#faça-alterações-usando-o-Copilot) usando o [GitHub Copilot](https://copilot.github.com/) para modificar o código.
3. Aceite o desafio e publique seu aplicativo no Azure.

🤔 Curioso? Assista ao seguinte vídeo onde explicamos todos os detalhes:

[![Ambiente de desenvolvimento Python com Codespaces](https://img.youtube.com/vi/_i9Pywj3rSg/0.jpg)](https://youtu.be/_i9Pywj3rSg "Ambiente de desenvolvimento Python com Codespaces")

<details>
   <summary><strong>Saiba mais sobre APIs</strong></summary>

   Uma API (Interface de Programação de Aplicativos) descreve uma maneira para dois computadores interagirem. Uma API HTTP permite que um computador conectado à Internet envie uma solicitação HTTP para outro computador conectado à Internet e receba uma resposta. Por exemplo, meu computador pode enviar uma solicitação para `http://um-site-de-previsao-do-tempo.com/api/cidade=Los+Angeles` e receber dados de volta, como `{"alta": 72, "baixa": 66}`.

   APIs HTTP frequentemente fornecem dados ou funcionalidades exclusivas de um serviço, como o exemplo da API do site de previsão do tempo. Um site de previsão do tempo pode fornecer endpoints de API adicionais para outras funcionalidades relacionadas ao clima, como previsões futuras ou dados históricos. Qualquer site pode optar por oferecer uma API se acreditar que possui funcionalidades úteis para compartilhar com outros computadores. Neste projeto, você executará uma API HTTP que gera um token aleatório.
</details>

Este modelo também está pronto para ser usado com o [Codespaces](https://github.com/features/codespaces), um ambiente de desenvolvimento executado na nuvem com o [Visual Studio Code](https://visualstudio.microsoft.com/?WT.mc_id=academic-77460-alfredodeza).

<details>
   <summary><b>🎥 Assista ao tutorial em vídeo para aprender mais sobre Codespaces</b></summary>

   [![Tutorial do Codespaces](https://img.youtube.com/vi/ozuDPmcC1io/0.jpg)](https://aka.ms/CodespacesVideoTutorial "Tutorial do Codespaces")
</details>

## Para estudantes e desenvolvedores

Usando o Codespaces, você obtém o [Visual Studio Code](https://visualstudio.microsoft.com/?WT.mc_id=academic-77460-alfredodeza) na nuvem, usando um ["container de desenvolvimento"](https://containers.dev/). Assim como a versão local do [Visual Studio Code](https://visualstudio.microsoft.com/?WT.mc_id=academic-77460-alfredodeza), a versão na nuvem também permite que você instale extensões e use um terminal.

Você também pode configurar o seu container de desenvolvimento para executar um tempo de execução específico e inicializá-lo com as suas extensões favoritas.

Aqui estão os arquivos e pastas principais que tornam isso possível:

- [webapp/](/webapp): O código da API HTTP, construído com o framework FastAPI.
- [.devcontainer/Dockerfile](/.devcontainer/Dockerfile): Arquivo de configuração usado pelo Codespaces para determinar o sistema operacional e outros detalhes.
- [.devcontainer/devcontainer.json](/.devcontainer/devcontainer.json): Um arquivo de configuração usado pelo Codespaces para configurar as configurações do [Visual Studio Code](https://visualstudio.microsoft.com/?WT.mc_id=academic-77460-alfredodeza), como a ativação de extensões adicionais.

## 🧐 Usando o Codespaces

Experimente este modelo de repositório usando o Codespaces seguindo estes passos:

1. Crie um repositório a partir deste modelo. Use este [link de criação do repositório](https://github.com/microsoft/codespaces-project-template-py/generate). Você pode tornar o repositório privado ou público, conforme sua preferência.
2. Antes de criar o codespace, habilite o GitHub Copilot para a sua conta! Se não estiver habilitado, dê uma olhada em [Faça alterações usando o Copilot](#make-changes-using-copilot).
3. Acesse a página principal do repositório recém-criado.
4. Abaixo do nome do repositório, use o menu suspenso Code e, na guia Codespaces, selecione "Criar Codespace em main".
   ![Criar Codespace](https://docs.github.com/assets/cb-138303/images/help/codespaces/new-codespace-button.png)
5. Aguarde enquanto o GitHub inicializa o codespace:
   ![Criando Codespace](https://github.com/microsoft/codespaces-teaching-template-py/raw/main/images/Codespace_build.png)

### Inspecionando o ambiente do Codespaces

Neste ponto, você tem um ambiente pré-configurado no qual todos os tempos de execução e bibliotecas de que você precisa já estão instalados - uma experiência de configuração zero.

## Executando o aplicativo

Este aplicativo Python está usando o FastAPI, um poderoso framework da web que documenta automaticamente seus endpoints de API. A API tem apenas um endpoint que gera uma sequência pseudoaleatória única que pode ser usada como um token.


![Executando o FastAPI](https://github.com/Corttezz/codespaces-project-template-py/assets/106662629/87b84e79-51c7-4d73-9c21-ff6403e64e35)

<details>
<summary> <b>O que é um ponto de extremidade?</b></summary>

Um ponto de extremidade é uma URL estável e durável que representa um recurso específico em uma API. Ele fornece uma maneira de interagir com esse recurso, enviar solicitações e receber respostas. Em termos simples, um ponto de extremidade é um "ponto de entrada" para uma API.

Características de um ponto de extremidade:

- **URL estável e durável**: Um ponto de extremidade é acessado por meio de uma URL específica, que permanece consistente ao longo do tempo. Por exemplo, uma URL estável e durável (como endpoint-name.region.inference.ml.azure.com).

- **Mecanismo de autenticação e autorização**: Para garantir a segurança e controlar o acesso ao recurso, os pontos de extremidade podem exigir autenticação e autorização. Isso pode envolver o uso de tokens, chaves de API ou outros métodos de autenticação.

- **Implantação e roteamento**: Um ponto de extremidade pode ter várias implantações, que são responsáveis por executar a lógica do recurso e fornecer as respostas adequadas. Essas implantações podem estar localizadas em servidores diferentes, dependendo dos requisitos de recursos e escalabilidade. O mecanismo de roteamento direciona as solicitações recebidas para as implantações corretas.

Portanto, um ponto de extremidade é um componente fundamental em uma API. Ele representa um recurso específico e define a maneira como os clientes podem interagir com ele, fornecendo uma URL estável, um mecanismo de autenticação e autorização, e encaminhando as solicitações para as implantações corretas.

</details>
<details>
<summary><b>Executando o FastAPI dentro do Codespace</b></summary>

A API incluída neste modelo de repositório possui um único ponto de extremidade (endpoint) que gera um token. Coloque-a em funcionamento seguindo as etapas a seguir:

1. Abra um terminal, abrindo o painel de comandos (Ctrl-Shift-P ou Cmd-Shift-P) e selecione o comando "Abrir novo terminal".
2. Execute `uvicorn` no console para iniciar o aplicativo da API:

    ```console
    uvicorn --host 0.0.0.0 webapp.main:app --reload
    ```

    Você verá uma saída semelhante a esta:

    ```output
    INFO:     Uvicorn running on http://127.0.0.1:8000 (Press CTRL+C to quit)
    INFO:     Started reloader process [28720]
    INFO:     Started server process [28722]
    INFO:     Waiting for application startup.
    INFO:     Application startup complete.
    ```

    Você verá uma janela pop-up informando que o seu aplicativo está disponível na porta 8000. Clique no botão para abri-lo no navegador.
3. Assim que o site for carregado, clique no botão _Try it Out_ ou adicione `/docs` à URL na barra de endereços. A documentação da API gerada automaticamente deve ser carregada e parecer assim:

 ![Documentação OpenAPI](https://github.com/Corttezz/codespaces-project-template-py/assets/106662629/ca251db8-30dc-46bb-b91e-4012b18bafaf)


4. Por fim, tente interagir com a API enviando uma solicitação usando a página auto documentada. Clique no botão _POST_ e depois no botão _Try it Out_:

   ![Experimente uma solicitação POST](https://github.com/Corttezz/codespaces-project-template-py/assets/106662629/730e7edc-9669-4c16-9819-466a8b29669b)


🔒 Você vê o cadeado ao lado da URL do site no navegador? Isso indica que o site está sendo servido por meio de uma conexão HTTPS segura, que criptografa as respostas HTTP. Isso é muito importante sempre que uma API pode receber dados sensíveis ou responder com dados sensíveis (como uma senha).

</details>

## Personalize o Codespace

Você pode alterar o seu ambiente e o editor de texto para que, da próxima vez que você criar (ou reconstruir) o ambiente, tudo seja configurado automaticamente. Vamos abordar dois desafios diferentes e que você provavelmente deseja fazer:

1. Alterar a versão do Python instalada
2. Adicionar ou modificar uma extensão do editor pré-instalada

<details>

### Passo 1:  Alterar a versão do Python instalada

Digamos que você queira alterar a versão do Python que está instalada. Isso é algo que você pode controlar.

Abra o arquivo [.devcontainer/devcontainer.json](/.devcontainer/devcontainer.json) e substitua a seguinte seção:

```json
"VARIANT": "3.8-bullseye"
```

pela seguinte instrução:

```json
"VARIANT": "3.9-bullseye"
```

Essa alteração instrui o Codespaces a usar o Python 3.9 em vez do 3.8.

Se você fizer qualquer alteração de configuração no `devcontainer.json`, uma caixa aparecerá após salvar.

![Recriando Codespace](https://github.com/microsoft/codespaces-teaching-template-py/raw/main/images/Codespace_rebuild.png)

Clique em Rebuild (em português, "Reconstruir"). Aguarde o seu Codespace reconstruir o ambiente do VS Code.

### Passo 2: Adicionar ou modificar uma extensão do editor pré-instalada

Seu ambiente vem com extensões pré-instaladas. Você pode alterar quais extensões o ambiente do Codespaces inicia. Veja como fazer:

1. Abra o arquivo [.devcontainer/devcontainer.json](/.devcontainer/devcontainer.json) e localize o seguinte elemento JSON **extensions**:

   ```json
   "extensions": [
    "ms-python.python",
    "ms-python.vscode-pylance"
   ]
   ```

2. Adicione _"ms-python.black-formatter"_ à lista de extensões. Deve ficar assim:

   ```json
   "extensions": [
    "ms-python.python",
    "ms-python.vscode-pylance",
    "ms-python.black-formatter"
   ]
   ```

   Essa sequência é o identificador único do [Black Formatter](https://marketplace.visualstudio.com/items?itemName=ms-python.black-formatter&WT.mc_id=academic-77460-alfredodeza), uma extensão popular para formatar o código Python de acordo com as melhores práticas. Adicionar o identificador _"ms-python.black-formatter"_ à lista informa ao Codespaces que essa extensão deve ser pré-instalada ao iniciar.

   Lembrete: Quando você alterar qualquer configuração no arquivo JSON, uma caixa aparecerá após salvar.

   ![Recriando Codespace](https://github.com/microsoft/codespaces-teaching-template-py/raw/main/images/Codespace_rebuild.png)

   Clique em Rebuild (em português, "Reconstruir"). Aguarde o seu Codespace reconstruir o ambiente do VS Code.

Para encontrar o identificador único de uma extensão:

- Acesse a página da extensão, por exemplo [https://marketplace.visualstudio.com/items?itemName=ms-python.black-formatter](https://marketplace.visualstudio.com/items?itemName=ms-python.black-formatter&WT.mc_id=academic-77460-alfredodeza)
- Localize o campo *Identificador Único* na seção **Mais informações** no lado direito.



</details>

## Faça alterações usando o Copilot

Vamos seguir algumas etapas para fazer alterações no código usando o Copilot. Essa é uma ótima maneira de aprender a usar o Copilot e obter sugestões úteis para um desenvolvimento mais rápido. Observe que essas são soluções sugeridas, e aconselhamos que você as revise para garantir que sejam aplicáveis ao seu código.

Este repositório do Codespaces já tem a extensão Copilot habilitada. Verifique se sua conta tem acesso a ela. Se você não tiver acesso, pode [solicitar](https://github.com/login?return_to=%2fgithub-copilot%2fsignup) e, em seguida, instale a extensão [aqui](https://aka.ms/get-copilot). Se você for estudante, pode obter o Copilot gratuitamente [seguindo estas instruções](https://techcommunity.microsoft.com/t5/desenvolvedores-br/como-obter-github-copilot-gratuito-para-estudantes-e-professores/ba-p/3828780?WT.mc_id=academic-97170-cyzanon).

Para garantir que o Copilot esteja funcionando corretamente, siga estas etapas:

1. Verifique se o Copilot está ativado navegando na guia de extensões em seu Codespace e verificando o status.
2. Se o status estiver inativo, reconstrua o Codespace e habilite a extensão para garantir que ela seja ativada.

🤔 Curioso? Assista ao seguinte vídeo em que explicamos todos os detalhes:

[![Assisted AI Coding with GitHub Copilot](https://img.youtube.com/vi/9c7SSHbzD80/0.jpg)](https://youtu.be/9c7SSHbzD80 "Assisted AI Coding with GitHub Copilot")

<details>
<summary><b>Utilizando o Copilot</b></summary>

### Passo 1: Alterar o HTML para torná-lo interativo

Abra o arquivo [index.html](./webapp/static/index.html) e exclua a seguinte linha:

```html
<button onclick="window.location.href='/docs'" type="button" class="btn btn-info">Try it out</button>
```

Agora, adicione um comentário para que o Copilot possa gerar código para você:

```html
<!-- criar um formulário interativo com entrada de texto e botão, e adicionar um ouvinte de evento ao botão para enviar uma solicitação POST para o endpoint /generate e exibir a resposta em uma div com id "result" -->
```

Isso deve ser suficiente para o Copilot gerar código para você depois de pressionar `Enter` (ou `Return`). 
Se não for o caso, use `Ctrl+Enter` para obter várias sugestões e escolha aquela que se encaixa melhor no código abaixo.
Lembre-se de que é possível que o Copilot não gere o trecho exato! Nesse caso, digite ou substitua a sugestão para o código abaixo.
O código gerado deve ser semelhante a este:

```html
              <form id="form">
                <input type="text" id="input" placeholder="Digite o texto aqui">
                <button type="button" id="button" class="btn btn-info">Gerar</button>
              </form>
              <div id="result"></div>
              <script>
               

 const button = document.getElementById('button');
                const form = document.getElementById('form');
                button.addEventListener('click', async (event) => {
                  event.preventDefault();
                  const input = document.getElementById('input').value;
                  const response = await fetch('/generate', {
                    method: 'POST',
                    headers: {
                      'Content-Type': 'application/json'
                    },
                    body: JSON.stringify({ text: input })
                  });
                  const data = await response.json();
                  const result = document.getElementById('result');
                  result.innerHTML = data.result;
                });
              </script>
```

Execute a aplicação e verifique se o formulário aparece.

### Passo 2: Atualizar o HTML para corrigir um bug

O código gerado introduziu alguns problemas. Primeiro, o botão não está funcionando. Segundo, o formulário não está usando a chave JSON correta ao enviar o texto para o endpoint da API. Vamos corrigir isso.

Altere o corpo da solicitação para usar a chave `length` em vez de `text`:

```javascript
body: JSON.stringify({ length: input })
```

Agora, vamos alterar o `innerHTML` para usar a chave `token` em vez de `result`:

```javascript
result.innerHTML = data.token;
```

Execute a aplicação e verifique se o formulário está funcionando agora.

### Passo 3: Alterar o formulário para usar um menu suspenso

Atualmente, o formulário aceita qualquer texto como entrada. Vamos alterá-lo para usar um menu suspenso. Adicione um comentário para que o Copilot possa gerar código para você. Exclua a seguinte linha:

```html
<input type="text" id="input" placeholder="Digite o texto aqui">
```

E adicione o seguinte comentário para que o Copilot possa gerar código para você:

```html
<!-- criar uma entrada com um menu suspenso para selecionar entre os seguintes valores: 5, 10, 15, 20 -->
```

O código gerado agora deve ficar assim:

```html
<select id="input">
   <option value="5">5</option>
   <option value="10">10</option>
   <option value="15">15</option>
   <option value="20">20</option>
</select>
```

Execute a aplicação novamente para verificar se o menu suspenso está funcionando corretamente.
   
### Passo 4: Adicionar um novo ponto de extremidade (endpoint) à API

Agora vamos adicionar uma nova funcionalidade à API. Adicione um novo ponto de extremidade (endpoint) à API que aceite um texto e retorne uma lista de tokens. Adicione o seguinte comentário para que o Copilot possa gerar um modelo Pydantic para você:

```python
# Crie um modelo Pydantic que aceita um corpo JSON com um único campo chamado "text", que é uma string
```

O modelo gerado deve ficar assim:

```python
class Text(BaseModel):
    text: str
```

Em seguida, adicione o seguinte comentário para que o Copilot possa adicionar um novo endpoint:

```python
# Crie um endpoint FastAPI que aceita uma solicitação POST com um corpo JSON contendo um único campo chamado "text" e retorna um checksum do texto
```

O código gerado deve ficar assim:

```python
@app.post('/checksum')
def checksum(body: Text):
    """
    Gere um checksum do texto. Exemplo de corpo de solicitação POST:

    {
        "text": "Olá mundo!"
    }
    """
    checksum = base64.b64encode(os.urandom(64))[:20].decode('utf-8')
    return {'checksum': checksum}
```

O código gerado fará com que a aplicação falhe. Isso ocorre porque os módulos `base64` e `os` não estão sendo importados. Adicione as seguintes linhas no início do arquivo:

```python
import base64
import os
```

Por fim, verifique se o novo ponto de extremidade (endpoint) está funcionando acessando a página `/docs` e testando o novo endpoint.

Parabéns! Você usou o Copilot não apenas para gerar código, mas também para fazer isso de forma interativa e divertida. Agora você pode usar o Copilot para gerar código em qualquer um de seus projetos, incluindo escrever documentação, gerar modelos e muito mais! Até mesmo partes deste README foram geradas usando sugestões do Copilot 🧐
   
   </details>

## 🚀 Próximos passos

Leve essa aplicação da API para o próximo nível e faça a sua publicação na nuvem! Para este desafio de aprendizado, você usará uma opção para publicar GRATUITAMENTE no Azure e o GitHub Actions para a automação.

Antes de continuar, certifique-se de ter uma conta no Azure pronta. Selecione uma das opções a seguir:

- [Faça login na sua conta do Azure](https://azure.microsoft.com/en-US/?WT.mc_id=academic-77460-alfredodeza)
- [Crie uma conta no Azure For Students (sem necessidade de cartão de crédito)](https://azure.microsoft.com/free/students/?WT.mc_id=academic-77460-alfredodeza)
- [Crie uma nova conta no Azure](https://azure.microsoft.com/en-US/?WT.mc_id=academic-77460-alfredodeza)

Há algumas etapas envolvidas, então certifique-se de fazer tudo corretamente!

<details>
<summary><b>Criar um Serviço de Aplicativo do Azure</b></summary>

Agora você irá configurar a publicação automática da aplicação usando o Azure e o GitHub Actions! No entanto, primeiro você precisa configurar alguns serviços do Azure.

1. Abra o [Azure Cloud Shell](https://shell.azure.com/?WT.mc_id=academic-77460-alfredodeza).
2. Use o Bash Shell (não o PowerShell!) para executar estas etapas.
3. Se aparecer a mensagem "You have no storage mounted", selecione uma assinatura em sua conta e clique em "Create storage". O Cloud Shell usará esse recurso de armazenamento para armazenar os dados gerados durante suas sessões no shell.
4. Crie um *Grupo de Recursos* que agrupará os diferentes recursos do Azure usados pela aplicação:
```
az group create --name demo-fastapi --location "East US"
```
5. Você verá uma resposta em JSON com detalhes sobre o novo recurso criado, para este comando e todos os comandos que seguem.
6. Crie o *Plano de Serviço de Aplicativo* **GRATUITO**:
```
az appservice plan create --name "demo-fastapi" --resource-group demo-fastapi --is-linux --sku FREE
```
7. Crie um identificador aleatório para um nome exclusivo do web app:
```
let "randomIdentifier=$RANDOM*$RANDOM"
```
8. Crie o *Serviço de Aplicativo da Web* com um contêiner reservado usando a variável `randomIdentifier` criada anteriormente:
```
az webapp create --name "demo-fastapi-$randomIdentifier" --resource-group demo-fastapi --plan demo-fastapi --runtime "PYTHON:3.9"
```
9. Acesse a lista de [Serviços de Aplicativos](https://portal.azure.com/#view/HubsExtension/BrowseResource/resourceType/Microsoft.Web%2Fsites) no portal do Azure e verifique se o serviço recém-criado está listado.

</details>


<details>
<summary><b>Criando um Azure Service Principal</b></summary>

A seguir, crie um Azure Service Principal, que é um tipo especial de conta que possui as permissões necessárias para autenticação do GitHub no Azure:

1. Encontre o ID de sua assinatura do Azure

 [no portal do Azure](https://portal.azure.com/#view/Microsoft_Azure_Billing/SubscriptionsBlade?WT.mc_id=academic-77460-alfredodeza) ou [seguindo este guia](https://learn.microsoft.com/azure/azure-portal/get-subscription-tenant-id?WT.mc_id=academic-77460-alfredodeza).
2. Crie um Azure Service Principal com a função "contributor" que está autorizada a fazer alterações em todos os recursos dessa assinatura. Substitua $AZURE_SUBSCRIPTION_ID pelo ID encontrado no passo 1 e execute o seguinte comando:

```
az ad sp create-for-rbac  --sdk-auth --name "github-deployer" --role contributor --scopes /subscriptions/$AZURE_SUBSCRIPTION_ID
```

3. Copie a saída e adicione-a como um [segredo do repositório do GitHub](/../../settings/secrets/actions/new) com o nome `AZURE_CREDENTIALS`. (_Se esse link não funcionar, certifique-se de que você está lendo isso em sua própria cópia do repositório, não no modelo original._)

</details>

<details>

<summary><b>Configurar o GitHub Actions</b></summary>

Agora que você criou todos os recursos do Azure, precisa atualizar o arquivo de fluxo de trabalho do GitHub Actions com o nome do seu web app.

1. Encontre o nome do seu aplicativo. Deve ser algo como `demo-fastapi-97709018`, mas com um número aleatório diferente no final, e você pode encontrá-lo no portal do Azure ou nos comandos do Cloud Shell.
2. Abra o arquivo [.github/workflows/web_app.yml](/../../edit/main/.github/workflows/web_app.yml) e atualize o valor de `AZURE_WEBAPP_NAME` com o nome do seu aplicativo.
3. Faça o commit e envie as alterações para o repositório do GitHub:

```
git add .github/workflows/web_app.yml
git commit -m "Atualizando arquivo de fluxo de trabalho"
git push
```

</details>

<details>
<summary><b>🏃 Implante a sua aplicação!</b></summary>

Antes de continuar, verifique o seguinte:

1. Você criou um Azure Service Principal e o salvou como um [segredo do repositório](/../../settings/secrets/) chamado `AZURE_CREDENTIALS`.
2. Você criou um [Serviço de Aplicativo](https://portal.azure.com/#view/HubsExtension/BrowseResource/resourceType/Microsoft.Web%2Fsites) com um nome válido e o site já está disponível com o conteúdo estático padrão.

Para implantar:

1. Acesse [Actions do repositório](/../../actions/workflows/web_app.yml). (_Se esse link não abrir o fluxo de trabalho "Build and deploy Python app", certifique-se de que você está lendo isso em sua própria cópia do repositório._)
2. Selecione _Run workflow_ e clique no botão verde dentro da janela pop-up para executar o fluxo de trabalho.

**A implantação pode levar alguns minutos**. Certifique-se de transmitir os logs no Azure Cloud Shell para verificar o progresso:

```
az webapp log tail --name $AZURE_WEBAPP_NAME --resource-group $AZURE_RESOURCE_GROUP
```

3. Após a conclusão da implantação, acesse seu site em uma URL

 como `http://demo-fastapi-97709018.azurewebsites.net/`, em que o número aleatório é o seu número aleatório exclusivo. Você pode encontrar a URL do site no portal do Azure ou nos logs de implantação, caso tenha esquecido o número.
4. 🎉 Celebre um implantação bem-sucedida! Agora você tem uma URL que pode compartilhar com colegas, amigos e familiares.

### Removendo os recursos quando concluído

Provavelmente você não deseja manter esse site específico em execução na nuvem para sempre, então você deve limpar seus recursos do Azure excluindo o grupo de recursos. Você pode fazer isso no Azure Cloud Shell referenciando o nome do grupo que você criou inicialmente (`demo-fastapi` nos exemplos):

```
az group delete --name demo-fastapi
```

### Solução de problemas de implantação

Ao fazer a implantação, você pode encontrar erros ou problemas, seja na automação (GitHub Actions) ou no destino de implantação (Azure Web Apps).

Você pode verificar os logs do fluxo de trabalho do GitHub Actions selecionando o fluxo de trabalho mais recente na guia _Actions_. Localize a primeira etapa que tem um ícone quebrado ao lado e expanda essa etapa para ver o que deu errado.

Se você tiver problemas com a implantação no Azure, verifique os logs no portal ou use o seguinte comando com o Azure CLI:

```
az webapp log tail --name $AZURE_WEBAPP_NAME --resource-group $AZURE_RESOURCE_GROUP
```

Atualize ambas as variáveis para corresponder ao seu ambiente.

</details>

## Outros Recursos

- [FastAPI](https://fastapi.tiangolo.com/)
- [Codespaces](https://github.com/features/codespaces)
- [Use containers de desenvolvimento localmente](https://github.com/Microsoft/vscode-remote-try-python)

### 🔎 Encontrou algum problema ou tem uma ideia de melhoria?
Ajude-nos a melhorar este repositório de modelo [nos informando e abrindo uma issue!](https://github.com/education/codespaces-project-template-py/issues/new).
