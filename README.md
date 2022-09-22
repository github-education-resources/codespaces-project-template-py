[![Open in GitHub Codespaces](https://github.com/codespaces/badge.svg)](https://github.com/codespaces/new?hide_repo_select=true&ref=main&repo=526682400)

# Python RESTful API for use with GitHub Codespaces

Here's a GitHub repository containing the following:

- A Python API built in [Fastapi](https://fastapi.tiangolo.com/) framework.
- A setup to run as a devcontainer via Codespaces.

It's also ready to be used with [Codespaces](https://github.com/features/codespaces) a developer environment running in the cloud.

<details>
   <summary><b>🎥 Watch the video tutorial to learn more about Codespaces</b></summary>

   [![Codespaces Tutorial](https://img.youtube.com/vi/ozuDPmcC1io/0.jpg)](https://aka.ms/CodespacesVideoTutorial "Codespaces Tutorial")
</details>

## For students

Thanks to Codespaces, you can work on your projects without having Visual Studio Code installed locally.

Using Codespaces you get Visual Studio code in the cloud, using a so called developer container. Like Visual Studio code installed locally, in this cloud version, you can install extensions, and use a terminal.

You can also configure your developer container to run a specific runtime and have it boot up with your favorite extensions.

## What's in it

- `/webapp` in this directory is your API, built in the Fastapi framework.
- `./devcontainer/devcontainer.json`, a devcontainer configuration file that decided things like runtime versions, installed extensions and Visual Studio Code settings and more.

## -1- Run it

To run what's in this repo, you need to first start a Codespaces instance.

1. Navigate to the main page of the newly created repository.
1. Under the repository name, use the Code drop-down menu, and in the Codespaces tab, select "Create codespace on main".
   ![Create codespace](https://docs.github.com/assets/cb-138303/images/help/codespaces/new-codespace-button.png)
1. Creating codespace

   ![Creating codespace](https://github.com/microsoft/codespaces-teaching-template-py/raw/main/images/Codespace_build.png)

Next, we will run our app.

## -2- Inspect your codespaces environment

What you have at this point is a pre-configured environment where all the runtimes and libraries you need are already installed - a 0 config experience.

> This environment will run the same regardless of whether your students are on Windows, macOS or Linux.

## -3- Run API
 
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

## Challenges

You can change your environment. Let us take you through two different challenges that you are likely to want to do.

### -1- Change Python runtime

Let's say you want to change what version of Python is installed. This is something you can control.

Open *.devcontainer/devcontainer.json* and replace the following section:

```json
"VARIANT": "3.8-bullseye"
```

with the following instruction:

```json
"VARIANT": "3.9-bullseye"
```

this change will use Python 3.9 instead of 3.8.

### -2- Add extension

Your environment comes with preinstalled extensions. You can change which extensions your codespaces environment starts with, here's how:

1. Open file *.devcontainer/devcontainer.json* and locate the following JSON element **extensions**:

   ```json
   "extensions": [
    "ms-python.python",
    "ms-python.vscode-pylance"
   ]
   ```

1. Add the following entry to **the extensions** list and add a comma on the previous extension:

   ```json
   "codespaces-Contrib.codeswing"
   ```
  
   What you did above was to add the unique identifier of an extension of the [CodeSwing extension](https://marketplace.visualstudio.com/items?itemName=codespaces-Contrib.codeswing). This will let Codespaces know that this extension should be pre-installed upon startup.

   Remainder: When you change any configuration on the json, a box will appear after saving.

   ![Recreating codespace](https://github.com/microsoft/codespaces-teaching-template-py/raw/main/images/Codespace_rebuild.png)

   Click on rebuild. Wait for your codespace to rebuild the VS Code environment.

To find the unique identifier of an extension:

- Navigate to the extension's web page, like so <https://marketplace.visualstudio.com/items?itemName=codespaces-Contrib.codeswing>
- Locate the *Unique Identifier* field under **More info** section on your right side.

## How to deploy

TODO

## Adding Ci/CD

TODO

## Resources

- [Fastapi](https://fastapi.tiangolo.com/)
- [Codespaces](https://github.com/features/codespaces)
