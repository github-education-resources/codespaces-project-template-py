[![Open in GitHub Codespaces](https://github.com/codespaces/badge.svg)](https://github.com/codespaces/new?hide_repo_select=true&ref=main&repo=526682400)

# Python RESTful API for use with GitHub Codespaces

_Run a Python API in this ready-to-use-repository in minutes_

With this template respository you can quickly get hands-on a Python project for running an HTTP API using the [Fastapi](https://fastapi.tiangolo.com/) framework. It will let you focus in working with the project instead of setting and configuring anything.

![Running FastAPI](./images/api-running.png)

It's also ready to be used with [Codespaces](https://github.com/features/codespaces) a developer environment running in the cloud with [Visual Studio Code](https://visualstudio.microsoft.com/?WT.mc_id=academic-77460-alfredodeza)

<details>
   <summary><b>🎥 Watch the video tutorial to learn more about Codespaces</b></summary>

   [![Codespaces Tutorial](https://img.youtube.com/vi/ozuDPmcC1io/0.jpg)](https://aka.ms/CodespacesVideoTutorial "Codespaces Tutorial")
</details>

## For students and developers

Thanks to Codespaces, you can work on your projects without having [Visual Studio Code](https://visualstudio.microsoft.com/?WT.mc_id=academic-77460-alfredodeza) installed locally.

Using Codespaces you get [Visual Studio Code](https://visualstudio.microsoft.com/?WT.mc_id=academic-77460-alfredodeza) in the cloud, using a so called developer container. Like [Visual Studio Code](https://visualstudio.microsoft.com/?WT.mc_id=academic-77460-alfredodeza) installed locally, in this cloud version, you can install extensions, and use a terminal.

You can also configure your developer container to run a specific runtime and have it boot up with your favorite extensions.

- [webapp/](./.webapp) in this directory is your API, built with the Fastapi framework.
- [.devcontainer/Dockerfile](./.devcontainer/Dockerfile), So that you can configure what operating system the Codespace will use and how should the container be built.
- [.devcontainer/devcontainer.json](./.devcontainer/devcontainer.json), A configuration file used by Codespaces to configure [Visual Studio Code](https://visualstudio.microsoft.com/?WT.mc_id=academic-77460-alfredodeza), for example to add and enable an extension.

### 🔎 Found an issue or have an idea for improvement?
Help us make this template repository better by [letting us know and opening an issue!](/../../issues/new).

## 🧐 Try it out

Try out this template repository using Codespaces following these steps:

1. Create a repo from this template. Use this [create repo link](https://github.com/microsoft/codespaces-project-template-py/generate)
1. Navigate to the main page of the newly created repository.
1. Under the repository name, use the Code drop-down menu, and in the Codespaces tab, select "Create Codespace on main".
   ![Create Codespace](https://docs.github.com/assets/cb-138303/images/help/codespaces/new-codespace-button.png)
1. Creating Codespace

   ![Creating Codespace](https://github.com/microsoft/codespaces-teaching-template-py/raw/main/images/Codespace_build.png)

### Inspect your Codespaces environment

What you have at this point is a pre-configured environment where all the runtimes and libraries you need are already installed - a zero config experience.

> This environment will run the same regardless of whether your students are on Windows, macOS or Linux.


## Running our app!

This Python application is using FastAPI, a powerful web framework that self-documents its API endpoints. The API has only one endpoint that generates a unique pseudo-random string that can be used as a token.

<details>

<summary><b>Run FastAPI inside the Codespace</b></summary>

The API included in this template repository has a single endpoint that generates a token. Get it up and running using the following steps:

1. Open up a terminal window by opening up the command palette (Ctrl-Shift-P or Cmd-Shift-P) and then select "Open new Terminal" command.
1. Run `uvicorn` in the console, it will start up your API:

    ```console
    uvicorn --host 0.0.0.0 webapp.main:app --reload
    ```

    You should see output similar to:

    ```output
    INFO:     Uvicorn running on http://127.0.0.1:8000 (Press CTRL+C to quit)
    INFO:     Started reloader process [28720]
    INFO:     Started server process [28722]
    INFO:     Waiting for application startup.
    INFO:     Application startup complete.
    ```

    You'll get a pop-up that says your application is available at port 8000. Click the button to open it in the browser.
1. Once the site loads, click on the _Try it Out_ button or append the following url part: `/docs` in the address bar. The self-documented API should load and look like this:

   ![OpenAPI docs](./images/fast-api.png)
1. Finally, try to interact with the API by sending a request using the self-documented page. Click on the _POST_ button and then on the _Try it Out_ button:

   ![Try a POST request](./images/try-it-out.png)

</details>



## Customize the Codespace

You can change your environment and the text editor so that the next time you create (or rebuild) the environment, everything will be set automatically. Let's go through two different challenges that you are likely to want to do:

1. Changing the Python version
1. Adding or modifying a pre-installed editor extension


<details>

### Step 1: Change the Python environment

Let's say you want to change what version of Python is installed. This is something you can control.

Open [.devcontainer/devcontainer.json](./.devcontainer/devcontainer.json) and replace the following section:

```json
"VARIANT": "3.8-bullseye"
```

with the following instruction:

```json
"VARIANT": "3.9-bullseye"
```

this change will use Python 3.9 instead of 3.8.

### Step 2: Add an extension

Your environment comes with preinstalled extensions. You can change which extensions your Codespaces environment starts with, here's how:

1. Open file [.devcontainer/devcontainer.json](./.devcontainer/devcontainer.json) and locate the following JSON element **extensions**:

   ```json
   "extensions": [
    "ms-python.python",
    "ms-python.vscode-pylance"
   ]
   ```

1. Add _"ms-python.black-formatter"_ to the list of extensions. It should end up looking like the following:

   ```json
   "extensions": [
    "ms-python.python",
    "ms-python.vscode-pylance",
    "ms-python.black-formatter"
   ]
   ```

   What you did above was to add the unique identifier of an extension of the Python [Black Formatter extension](https://marketplace.visualstudio.com/items?itemName=ms-python.black-formatter&WT.mc_id=academic-77460-alfredodeza). This will let Codespaces know that this extension should be pre-installed upon startup.

   Remainder: When you change any configuration on the json, a box will appear after saving.

   ![Recreating Codespace](https://github.com/microsoft/codespaces-teaching-template-py/raw/main/images/Codespace_rebuild.png)


   Click on rebuild. Wait for your Codespace to rebuild the VS Code environment.

To find the unique identifier of an extension:

- Navigate to the extension's web page, for example [https://marketplace.visualstudio.com/items?itemName=ms-python.black-formatter](https://marketplace.visualstudio.com/items?itemName=ms-python.black-formatter&WT.mc_id=academic-77460-alfredodeza)
- Locate the *Unique Identifier* field under **More info** section on your right side.

</details>


## 🚀 Next steps

Take this API application to the next level and deploy it to the cloud! For this learning challenge you'll use a FREE deployment option for Azure and GitHub Actions for the automation.

Before continuing, make sure you have an Azure account ready. Select any of the following:

- [Sign in to your account](https://azure.microsoft.com/en-US/?WT.mc_id=academic-77460-alfredodeza)
- [Create a (no Credit Card required) Azure For Students account](https://azure.microsoft.com/free/students/?WT.mc_id=academic-77460-alfredodeza)
- [Create a new Azure account](https://azure.microsoft.com/en-US/?WT.mc_id=academic-77460-alfredodeza)

There are a few steps involved, so make sure you get everything right!

<details>
<summary><b>Create an Azure App Service</b></summary>

Now, we are going to deploy our application using Azure and GitHub actions to do this autmomatically! However, we need to configure our services.

Start by creating the Azure resources.

1. Open an [Azure Cloud Shell](https://shell.azure.com/?WT.mc_id=academic-77460-alfredodeza) to use the `az` cli.
1. Use the Bash shell (not PowerShell!) for this guide to generate your unique identifier quickly.
1. Create a *Resource Group*:
```
az group create --name demo-fastapi --location "East US"
```
1. Create the **FREE** App Service Plan:
```
az appservice plan create --name "demo-fastapi" --resource-group demo-fastapi --is-linux --sku FREE
```
1. Create a random identifier for a unique webapp name:
```
let "randomIdentifier=$RANDOM*$RANDOM"
```
1. Create the web app with a placeholder container using the `randomIdentifier` from before
```
az webapp create --name "demo-fastapi-$randomIdentifier" --resource-group demo-fastapi --plan demo-fastapi --runtime "PYTHON:3.9"
```
1. Head to the [App Service](https://portal.azure.com/#view/HubsExtension/BrowseResource/resourceType/Microsoft.Web%2Fsites) and confirm that your service is up and running
</details>

<details>
<summary><b>Create an Azure Service Principal</b></summary>

Next, create an Azure Service Principal, which is a special type of account that has permissions necessary to authenticate from GitHub to Azure:

1. The Azure subscription ID [find it here](https://portal.azure.com/#view/Microsoft_Azure_Billing/SubscriptionsBlade?WT.mc_id=academic-77460-alfredodeza) or [follow this guide](https://learn.microsoft.com/azure/azure-portal/get-subscription-tenant-id?WT.mc_id=academic-77460-alfredodeza)
1. A Service Principal with the following details the AppID, password, and tenant information. Set the proper role access using the following command (use a real subscription id and replace it):

```
az ad sp create-for-rbac --name "CICD" --role contributor --scopes /subscriptions/$AZURE_SUBSCRIPTION_ID --sdk-auth
```

Capture the output and add it as a [repository secret](/../../settings/secrets/actions/new) with the name `AZURE_CREDENTIALS`
</details>

<details>

<summary><b>Setup GitHub Actions</b></summary>

Now that you have everything created, we need to update the GitHub Action workflow file with the name for our webapp.

- Check the result of `randomIdentifier` in your bash shell in az, use that to change in our webapp
- Update the [.github/workflows/web_app.yml](/../../edit/main/.github/workflows/web_app.yml) file
- Update this: `AZURE_WEBAPP_NAME`: demo-fastapi-(randomIdentifier-result-here)

</details>

<details>
<summary><b>🏃 Deploy your app!</b></summary>

Before continuing, check the following:

1. You've created an Azure Service Principal and saved it as a [repository secret](/../../settings/secrets/) as `AZURE_CREDENTIALS`
1. You've created an [App Service](https://portal.azure.com/#view/HubsExtension/BrowseResource/resourceType/Microsoft.Web%2Fsites) with a valid name and the site is already available with the default static content

To deploy:

1. Go to [repository actions](/../../actions/workflows/web_app.yml) and click on _Run workflow_ and then the green button to run it.

**Deploying can take a couple of minutes**. Make sure you tail the logs in the Azure cloud shell to check the progress:

```
az webapp log tail --name $AZURE_WEBAPP_NAME --resource-group $AZURE_RESOURCE_GROUP
```

### Destroy resources when complete

After deploying, make sure you cleanup your resources by destroying the resource group. You can do it by re-using the group name you created initially (`demo-fastapi` in the examples):

```
az group delete --name demo-fastapi
```

### Deployment Troubleshooting

When deploying, you might encounter errors or problems, either on the autonatiom part of it (GitHub Actions) or on the deployment destination (Azure WebApps).

If running into trouble, check logs in the portal or use the following with the Azure CLI:

```
az webapp log tail --name $AZURE_WEBAPP_NAME --resource-group $AZURE_RESOURCE_GROUP
```

Update both variables to match your environment

</details>


## Other Resources

- [Fastapi](https://fastapi.tiangolo.com/)
- [Codespaces](https://github.com/features/codespaces)
- [Use Dev containers locally](https://github.com/Microsoft/vscode-remote-try-python)
