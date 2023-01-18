[![Open in GitHub Codespaces](https://github.com/codespaces/badge.svg)](https://github.com/codespaces/new?hide_repo_select=true&ref=main&repo=526682400)

# Python HTTP API  com codespaces GitHub

_Execute uma API com Python neste repositório pronto para uso em minutos_

Ao abrir este template no Codespaces, você pode rapidamente obter hands-on com um aplicativo web Python que serve uma API HTTP usando a estrutura do [FastAPI](https://fastapi.tiangolo.com/). Você poderá se concentrar em trabalhar com o projeto em vez de configurar tudo.

🤔 Curioso? Veja o vídeo para mais detalhes:

[![Python development environment with Codespaces](https://img.youtube.com/vi/_i9Pywj3rSg/0.jpg)](https://youtu.be/_i9Pywj3rSg "Python Development environment with Codespaces")


<details>
   <summary><strong>Aprenda mais sobre APIs</strong></summary>

   Uma API (Application Programming Interface) descreve uma maneira de dois computadores interagirem.
   Uma API HTTP permite que um computador conectado à Internet envie uma solicitação HTTP para outro computador conectado à Internet
    e receber uma resposta. Por exemplo, meu computador poderia enviar uma solicitação para
   'http://a-weather-website-api.com/api/city=Los+Angeles' e receber de volta dados como '{"high": 72, "low": 66}'.
   
   APIs HTTP provem dados ou funcionalidade que é unico a um serviço, como o exemplo API para o site meteorológico. Um site meteorológico poderia fornecer pontos finais adicionais da API para outras funcionalidades relacionadas ao clima, como previsões futuras ou dados históricos. Qualquer site pode decidir oferecer uma API se achar que tem funcionalidade útil para compartilhar
   com outros computadores. Neste projeto, você vai executar uma API HTTP que gera um token randomico.
</details>

Este modelo também está pronto para ser usado com [Codespaces](https://github.com/features/codespaces), um ambiente de desenvolvedor em execução na nuvem com [Visual Studio Code](https://visualstudio.microsoft.com/?WT.mc_id=academic-77460-alfredodeza).
<details>
   <summary><b>🎥 Veja esse tutorial para aprender mais sobre codespaces (Em Inglês)</b></summary>

   [![Codespaces Tutorial](https://img.youtube.com/vi/ozuDPmcC1io/0.jpg)](https://aka.ms/CodespacesVideoTutorial "Codespaces Tutorial")
</details>

## Para estudantes e desenvolvedores

Utilizando Codespaces, você consegue uma instância do [Visual Studio Code](https://visualstudio.microsoft.com/?WT.mc_id=academic-77460-alfredodeza) na nuvem, utilizando um ["container de desenvolvimento"](https://containers.dev/). Como na versão normal do [Visual Studio Code](https://visualstudio.microsoft.com/?WT.mc_id=academic-77460-alfredodeza), a versão em cloud permite você instalar extensões e usar um terminal.

Você também pode configurar seu container de desenvolvimento para executar para executar a specific runtime and have it boot up with your favorite extensions.

Aqui estão os arquivos chaves e as pastas necessárias para tudo funcionar:

- [webapp/](./.webapp): O código da API HTTP, feita com o framework FastAPI.
- [.devcontainer/Dockerfile](./.devcontainer/Dockerfile): Arquivo de configuração utilizada pelo Codespaces para determinar o sistema operacional e outras variáveis.
- [.devcontainer/devcontainer.json](./.devcontainer/devcontainer.json), Um arquivo de configuração para o Codespaces configurando o [Visual Studio Code](https://visualstudio.microsoft.com/?WT.mc_id=academic-77460-alfredodeza), como habilitar extensões! 

## 🧐 Experimente

Experimente este template utilizando codespaces seguindo esses passos:

1. Crie um repositório a partir deste template. Use este [link para gerar um repositório](https://github.com/microsoft/codespaces-project-template-py/generate). Você pode tornar o repositório privado ou público, até você.
1. Navegue até a página principal do repositório recém-criado.
1. No nome do repositório, use o menu dropdwon em code e, na guia Codespaces, selecione "Create Codespace on main".
   ![Create Codespace](https://docs.github.com/assets/cb-138303/images/help/codespaces/new-codespace-button.png)
1. Aguarde enquanto Github inicializa o codespace:
   ![Creating Codespace](https://github.com/microsoft/codespaces-teaching-template-py/raw/main/images/Codespace_build.png)

### Inspecione seu ambiente do Codespaces

O que você tem neste momento é um ambiente pré-configurado onde todos os tempos de execução e bibliotecas que você precisa já estão instalados - uma experiência de configuração zero.

## Executando o Aplicativo

Este aplicativo Python está usando o FastAPI, uma poderosa framework  Web que auto-documenta seus pontos finais de API. A API tem apenas um ponto final que gera uma sequência pseudoaleatória única que pode ser usada como um token.


![Executando FastAPI](./images/api-running.png)


<details>
<summary><b>Executando FastAPI dentro do Codespace</b></summary>

A API incluída neste repositório de modelos tem um único ponto final que gera um token. Colocá-lo em funcionamento usando as seguintes etapas:

1. Abra uma janela de terminal abrindo a paleta de comando (Ctrl-Shift-P ou Cmd-Shift-P) e selecione o comando "Open new Terminal".
1. Execute 'uvicorn' no console para iniciar seu aplicativo de API:
  
    ```console
    uvicorn --host 0.0.0.0 webapp.main:app --reload
    ```

    Seu output deve ser similar à:

    ```output
    INFO:     Uvicorn running on http://127.0.0.1:8000 (Press CTRL+C to quit)
    INFO:     Started reloader process [28720]
    INFO:     Started server process [28722]
    INFO:     Waiting for application startup.
    INFO:     Application startup complete.
    ```

    Você terá um pop-up que diz que seu aplicativo está disponível na porta 8000. Clique no botão para abri-lo no navegador.
1. Quando o site carregar, clique no _Try it Out_ ou adicione `/docs` na URL. A documentação de API gerada automaticamente deve carregar e ficar assim:

   ![OpenAPI docs](./images/fast-api.png)

1. Finalmente, tente interagir com a API enviando uma solicitação usando a página auto-documentada. Clique no _POST_ e depois no _Try it Out_:

   ![Experimente um POST](./images/try-it-out.png)

🔒 Você vê o cadeado ao lado da URL do site no navegador? Isso indica que o site está sendo servido sobre uma conexão HTTPS segura que criptografa as respostas HTTP. Isso é muito importante sempre que uma API pode receber dados confidenciais ou responder com dados confidenciais (como uma senha).

</details>

## Customise o Codespace

Você pode alterar seu ambiente e o editor de texto para que, da próxima vez que você criar (ou reconstruir) o ambiente, tudo seja definido automaticamente. Vamos passar por dois desafios diferentes que você provavelmente quer fazer:

1. Mudar a versão do Python
1. Adicionar ou modificar extensões no Codespaces


<details>

### Step 1: Mudar a versão do Python

Digamos que você queira alterar qual versão do Python está instalada. Isso é algo que você pode controlar.

Abra [.devcontainer/devcontainer.json](./.devcontainer/devcontainer.json) e mude a seguinte seção:

```json
"VARIANT": "3.8-bullseye"
```

com a seguinte instrução:

```json
"VARIANT": "3.9-bullseye"
```

Essa mudança configura o Codespaces para usar o Python 3.9 invés do 3.8.

Se você mudar algo no `devcontainer.json`, uma janela vai aparecer após salvar.

![Recriando Codespace](https://github.com/microsoft/codespaces-teaching-template-py/raw/main/images/Codespace_rebuild.png)

Clique em rebuild. Espere seu Codespace reconstruir o ambiente do VS Code.

### Step 2: Adicione uma extensão

Seu ambiente vem com extensões pré-instaladas. Você pode alterar quais extensões o ambiente codespaces começa. Veja como:

1. Abra o arquivo [.devcontainer/devcontainer.json](./.devcontainer/devcontainer.json) e localize a seção **extensions**:

   ```json
   "extensions": [
    "ms-python.python",
    "ms-python.vscode-pylance"
   ]
   ```

1. Adiciona _"ms-python.black-formatter"_ para a lista de extensões. Deve parecer o seguinte:

   ```json
   "extensions": [
    "ms-python.python",
    "ms-python.vscode-pylance",
    "ms-python.black-formatter"
   ]
   ```

   Essa string é o identificador de [Black Formatter](https://marketplace.visualstudio.com/items?itemName=ms-python.black-formatter&WT.mc_id=academic-77460-alfredodeza), uma extensão popular para formatação de código Python de acordo com as melhores práticas. Adicionando _"ms-python.black-formatter"_ na lista deia o Codespaces saber que essa extensão deve ser pré instalada ao iniciar.

   Lembrete: Quando você muda algo no arquivo JSON, uma janela vai aparecer após salvar.

   ![Recriando Codespace](https://github.com/microsoft/codespaces-teaching-template-py/raw/main/images/Codespace_rebuild.png)

   Clique em rebuild. Espere seu Codespace reconstruir seu ambiente.

Ache o identificador único de uma extensão:

- Navegue até a página da extensão, por exemplo [https://marketplace.visualstudio.com/items?itemName=ms-python.black-formatter](https://marketplace.visualstudio.com/items?itemName=ms-python.black-formatter&WT.mc_id=academic-77460-alfredodeza)
- Localize o campo *Unique Identifier* em **More info** no lado direito.

</details>

## 🚀 Próximos passos

Leve este aplicativo de API para o próximo nível e implante-o na nuvem! Para este desafio, você usará uma opção de deploy gratuita com Azure e GitHub Actions para a automação.

Antes de continuar, certifique-se de ter uma conta do Azure pronta. Selecione qualquer um dos seguintes:

- [Faça login em sua conta do Azure](https://azure.microsoft.com/en-US/?WT.mc_id=academic-77460-alfredodeza)
- [Crie (sem Cartão) uma conta Azure For Students](https://azure.microsoft.com/free/students/?WT.mc_id=academic-77460-alfredodeza)
- [Crie uma conta Azure](https://azure.microsoft.com/en-US/?WT.mc_id=academic-77460-alfredodeza)

Há alguns passos envolvidos, então certifique-se de tudo!

<details>
<summary><b>Crie um Azure App Service</b></summary>

Agora, você vai configurar o deploy automático do aplicativo usando o Azure mais GitHub Actions! No entanto, primeiro você precisa configurar alguns serviços do Azure.

1. Abra o [Azure Cloud Shell](https://shell.azure.com/?WT.mc_id=academic-77460-alfredodeza).
1. Use o shell Bash (não PowerShell!) para esses passos.
1. Se mostra "You have no storage mounted", selecione a inscrição em sua conta e clique "Create storage". O shell da Cloud usa o recurso de armazenamento para armazenar os dados gerados durante a seção da shell.
1. Cria uma *Resource Group* que agrupará os diferentes recursos do Azure usados para o aplicativo:
```
az group create --name demo-fastapi --location "East US"
```
1. Você verá uma resposta JSON com detalhes sobre o recurso recém-criado, para este comando e todos os comandos que se seguem.
1. Crie um *App Service Plan* sem custo:
```
az appservice plan create --name "demo-fastapi" --resource-group demo-fastapi --is-linux --sku FREE
```
1. Crie um identificador aleatório para um nome de webapp unico:
```
let "randomIdentifier=$RANDOM*$RANDOM"
```
1. Crie *Web App Service* com um recipiente de espaço reservado usando a variável `randomIdentifier`:
```
az webapp create --name "demo-fastapi-$randomIdentifier" --resource-group demo-fastapi --plan demo-fastapi --runtime "PYTHON:3.9"
```
1. Vá ao Azure portal [App Services list](https://portal.azure.com/#view/HubsExtension/BrowseResource/resourceType/Microsoft.Web%2Fsites) e confirme que seu novo serviço foi criado e listado.

</details>


<details>
<summary><b>Crie um Azure Service Principal</b></summary>

Em seguida, crie um Azure Service Principal, que é um tipo especial de conta que tem permissões necessárias para autenticar do GitHub para o Azure:
  
1. Encontre a ID de sua Assinatura Azure [no portal do Azure](https://portal.azure.com/#view/Microsoft_Azure_Billing/SubscriptionsBlade?WT.mc_id=academic-77460-alfredodeza) ou [ao seguir esse guia](https://learn.microsoft.com/azure/azure-portal/get-subscription-tenant-id?WT.mc_id=academic-77460-alfredodeza).
1. Crie um Service Principal com o cargo de "contributor" que é permitido fazer mudanças em recusos nessa inscrições. Substitua $AZURE_SUBSCRIPTION_ID com o ID que você acho no passo 1:

```
az ad sp create-for-rbac  --sdk-auth --name "github-deployer" --role contributor --scopes /subscriptions/$AZURE_SUBSCRIPTION_ID
```

1. Pegue o output e coloque como [segredo de repositório do GitHub](/../../settings/secrets/actions/new) com o nome `AZURE_CREDENTIALS`. (_Se esse link não funcionar, certifique-se de que você está lendo isso em sua própria cópia do repo, não no modelo original._)

</details>

<details>

<summary><b>Configure GitHub Actions</b></summary>

Agora que você tem todos os recursos do Azure criados, você precisa atualizar o arquivo de workflow do GitHub Action com o nome do seu webapp.

1. Ache o nome do seu arquivo. Deve parecer com `demo-fastapi-97709018` com um numero randômico na frente, você pode encontrar no portal Azure e comando de Cloud Shell.
2. Abra o arquivo [.github/workflows/web_app.yml](/../../edit/main/.github/workflows/web_app.yml) e mude o valor `AZURE_WEBAPP_NAME` para o nome do seu aplicativo.
3. Commite e push as mudanças do repositório do Github:

```
git add .github/workflows/web_app.yml
git commit -m "Updating workflow file"
git push
```

</details>

<details>
<summary><b>🏃 Dê deploy no app!</b></summary>

Antes de continuar, cheque o seguinte:

1. Foi criado um Azure Service Principal e salvou um [segredo de repositório](/../../settings/secrets/) como `AZURE_CREDENTIALS`.
1. Foi criado um [App Service](https://portal.azure.com/#view/HubsExtension/BrowseResource/resourceType/Microsoft.Web%2Fsites) com um nome válido e o site está disponível com um conteúdo estático.

Para deploy:

1. Navegue até as [ações de repositório](/../../actions/workflows/web_app.yml). (_Se esse link não abrir o workflow "Build and deploy Python app", certifique-se de que você está lendo isso em sua própria cópia do repo._)
1. Selecione _Run workflow_ e selecione o botão verde dentro da janela para rodar o workflow.

**O deploy pode demorar brevemente**. Certifique-se de transmitir os logs no Azure Cloud Shell para verificar o progresso:

```
az webapp log tail --name $AZURE_WEBAPP_NAME --resource-group $AZURE_RESOURCE_GROUP
```

4. Depois rodar, visite seu website numa URL como `http://demo-fastapi-97709018.azurewebsites.net/`, onde o número aleatório é o seu número aleatório único. Você pode encontrar a URL do site no portal do Azure ou nos registros de implantação se você esqueceu o número.
5. 🎉 Celebre um deploy bem sucedido! Agora você tem uma URL que você pode compartilhar com colegas de classe, amigos e familiares.
  
### Destrua seus recursos quando completo

Você provavelmente não quer manter este site em particular funcionando para sempre na nuvem, então você deve limpar seus recursos do Azure destruindo o grupo de recursos. Você pode fazê-lo no Azure Cloud Shell fazendo referência ao nome de grupo que você criou inicialmente ('demo-fastapi' nos exemplos):

```
az group delete --name demo-fastapi
```

### Troubleshooting

No Deploy, você pode encontrar erros ou problemas, seja na parte de automação dele (GitHub Actions) ou algo no deploy (Azure Web Apps).

Você pode verificar os registros do workflow do Github Actions selecionando o fluxo de trabalho mais recente da guia _Actions_. Encontre o primeiro passo que tem um ícone quebrado ao lado dele, e expanda esse passo para ver o que deu errado nele.

Se houver problemas com o deploy do Azure, verifique os registros no portal ou use o seguinte com o Azure CLI:
  
```
az webapp log tail --name $AZURE_WEBAPP_NAME --resource-group $AZURE_RESOURCE_GROUP
```

Atualize ambas as variáveis para combinar com seu ambiente.

</details>

## Other Resources

- [FastAPI](https://fastapi.tiangolo.com/)
- [Codespaces](https://github.com/features/codespaces)
- [Use Dev containers localmente](https://github.com/Microsoft/vscode-remote-try-python)

### 🔎 Achou um porblema ou tem sugestões? 
Nos ajude a fazer esse template melhor por [deixar nós sabermos e abirir uma issue!](/../../issues/new).
