# Getting started with Jupyter notebooks

## Overview

Jupyter notebooks are documents that take coding in Python (and potentially other languages) to a whole new level. They are technically just fancy JSON files with a `.ipynb` extension, but with a Jupyter notebook and a compatible IDE, you can:

1. Write, run and re-run code in a block-by-block basis, while keeping all variables in an active and *interactive* kernel space. Those blocks are called "cells."
2. Combine executable code, rich text, HTML, and even images in a single document, going way beyond standard Python comments and inserting HTML- or Markdown-formatted documentation inline with code in a way that never interferes with the operation of your code.
3. Rearrange code and Markdown cells aribitrarily for verification, experimentation, or pure curiosity.
4. Much more, if you are willing to learn!

Jupyter notebooks are a product of Project Jupyter, a nonprofit organization dedicated to open standards and interactive computing. Read more on [their official website](https://jupyter.org/).

In relation to the Meraki Python SDK, we will focus on using notebooks to write and document Python, of course! To get started, there's a few things you should know.

## Prerequisites

Jupyter notebooks (hereafter referred to as simply "notebooks") can be a great way to learn and experiment with Python code, and in fact are often used in scenarios where the users running and maintaining the code have minimal coding and/or Python experience. As a result, you will find that coding in a notebook offers certain advantages you might not have in a traditional IDE.

That said, to open and create a notebook, you will need a compatible editor. There are several free options.

* Project Jupyter offers [JupyterLab](https://jupyter.org/install.html), a web-based IDE with a local installer for running on a host machine (installation required)
* Microsoft offers [Visual Studio Code](https://code.visualstudio.com/), a powerful, multi-language IDE which has native support for notebooks and Python (installation required)
* Google offers [Colaboratory](https://colab.research.google.com/), a completely web-based notebook IDE which requires no download whatsoever. Google calls their notebooks "Colab notebooks," but they work in much the same way. To learn more, see [Overview of Colab](https://colab.research.google.com/notebooks/basic_features_overview.ipynb).

Regardless of how you choose to create them, notebooks are stored as `.ipnyb` files to distinguish them from standard `.py` Python scripts. In this guide, we will focus on using Google Colaboratory since it requires no download, but in some cases we will offer relevant instructions for other IDEs. In any case, if you prefer VS Code or JupyterLab, you can open the same notebook files covered in either IDE.

## Setting up your environment variables

Any use of the API requires the use of an _API key_ (also called _API token_) for authentication. Technically, you could include your API key in plaintext in your notebooks or Python scripts, but that would be like storing your password in plaintext, and make it risky to share or publish your work. A more secure approach is to store your API key in your local environment variables. The Meraki SDK will automatically check your `env` for the appropriate variable and use it if it exists.

### Using Colab

To simulate environment variables in Colab, we'll use the `colab-env` package. To set it up, you'll need a (free) Google account. `colab-env` creates a file called `vars.env` in your Google Drive to store the variables, and we'll use Python to add variables to it.

1. Open [Colaboratory](https://colab.research.google.com/) in your browser.
2. Sign in with a Google account if prompted.
3. By default, Colab opens the "Welcome to Colaboratory" notebook.
4. At the top, create a new code cell and paste in the following code, then run the cell. It will give you a link to log into your Google account:

    ```python
    %pip install colab-env -qU
    import colab_env
    import os
    ```

5. Click the link, complete the authentication, and copy the long code it gives you. 
6. Paste the code into the form field provided by the code cell, then hit `Enter` or `Return`.
7. You will then get one of the following outputs, depending on whether you've used the module with your Google account before:

    | ![Colab import colab_env output with new vars.env](/.github/images/colab-notebook-colab_env-import-new-instance_Annotation_2020-08-05_163942.png) | ![Colab import colab_env output with existing vars.env](/.github/images/colab-notebook-colab_env-import-Annotation_2020-08-05_163815.png) |
    |:--:|:--:|
    | *First time* | *When `vars.env` exists* |

8. In a new cell, paste in the following code block, and replace `YOUR_API_KEY_HERE` with your actual API key:

    ```python
    colab_env.envvar_handler.add_env(envname="MERAKI_DASHBOARD_API_KEY",envval="YOUR_API_KEY_HERE")
    print(os.getenv('MERAKI_DASHBOARD_API_KEY'))
    ```

9. Run the cell. You should see your API key printed in the output. If you do, that means your environment is configured!

### Using VS Code on Windows

1. Click `Start` > `This PC` (type it if necessary) > Right-click on `This PC` > `Manage`
2. Near top left, `Advanced system settings` > `Environment Variables...`
3. Under the box labeled `User variables for YOUR_USERNAME`, `New...`. _NB: Avoid using the second, lower `New...` button under `System variables`. Others have access to that information._
4. For `Variable name:`, type MERAKI_DASHBOARD_API_KEY
5. For `Variable value:`, paste in your actual API key
6. `OK`
7. Reboot your computer. This ensures the value is available to any program that calls it.

### Using VS Code on Mac

Depending on your version of macOS, your default shell is either bash or zsh. User variables are stored in `~/.bash_profile` or `~/.zsh_profile` respectively. To find out which shell you're using, open Terminal, then run `echo $SHELL`.

1. If `~/.bash_profile` or `~/.zsh_profile` doesn't already exist, create the one relevant to your shell, e.g. if you have zsh, then run `touch ~/.zsh_profile` in Terminal.
2. Add this line to it, replacing the placeholder with your own API key: `export MERAKI_DASHBOARD_API_KEY=YOUR_API_KEY_HERE`
3. Save the file.
4. Reboot your computer. This ensures the value is available to any program that calls it.

## Create your first notebook

### Using Colab

When using Colab, the steps are as follows:

1. Open [Colaboratory](https://colab.research.google.com/) in your browser.
2. Sign in with a Google account if prompted.
3. You're done! By default, Colab opens the "Welcome to Colaboratory" notebook.

### Using VS Code

When using VS Code, the steps are as follows:

1. Install [Python 3.x locally](https://www.python.org/). As of the time of this writing, Python 3.8.5 is current.
2. Install [VS Code locally](https://code.visualstudio.com/#alt-downloads).
3. Install [VS Code's Python extension](https://marketplace.visualstudio.com/items?itemName=ms-python.python).
4. __File__ > __New File__, then save the file with extension `.ipynb`.

For a more detailed overview, please read [Microsoft's guide](https://code.visualstudio.com/docs/python/jupyter-support#:~:text=You%20can%20create%20a%20Jupyter,edit%20and%20run%20code%20cells.).

## Open an existing notebook

### Using Colab

Click __File__ > __Open notebook__

You can manually upload notebooks you've saved locally, or you can clone a notebook from a public GitHub repository. In this case, let's clone a notebook from the Meraki GitHub.

Click GitHub, then type `meraki` in the search field, then click in the deadspace to leave the field. Colab automatically lists Meraki's GitHub repos. Choose `dashboard-api-python`. Then choose the desired notebook from the list.

![Colab notebook selection screenshot](/.github/images/colab-notebook-selection-Annotation_2020-08-05_120229.png)

Colab will open the notebook and you can get started!

### Using VS Code

1. Download the notebook(s) you'd like to use locally. When working with VS Code, it's helpful to create a "workspace" folder free of any other files.
2. Click __File__ > __Open Folder__
3. Choose the folder where your notebook files are located, confirm the prompt, then select the notebook you'd like to use from the Explorer pane.

## Installing dependencies

### Using Colab

Unlike local Python environments, Colab environments are not persistent. Therefore, whenever we expect to use a third-party package in Colab, we need to install it first using `pip`. The syntax is as follows:

```python
%pip install PACKAGE_NAME
```

For example, to install the Meraki SDK:

```python
%pip install meraki
```

If necessary, create a new code cell at the top of the notebook, paste in that code, and run it before working with the rest of your notebook.

### Using VS Code

At a terminal, run:

```shell
pip install meraki
```

Other packages can be installed the same way using the relevant package name. Try it with `tablib`!

## Creating new cells in a notebook

### Using Colab

Depending on whether you'd like a new cell for code or text, click `+ Code` or `+ Text` at top left.

![Colab notebook new cell screenshot](/.github/images/colab-notebook-new-cell-Annotation_2020-08-05_123920.png)

## Writing code in a notebook

### Using Colab or VS Code

After you have either created a new code cell, or clicked into an existing one, you can write Python like you normally would. You can put as much or as little into a cell, but for our purposes we've segmented the code into logical blocks for ease of consumption.

## Running code in a notebook

### Using Colab GUI

Press the Run button at the top left of the code cell you'd like to run.

![Colab notebook run button](/.github/images/colab-notebook-run-cell-Annotation_2020-08-05_143202.png)

### Using Colab or VS Code hotkeys

Notebook IDEs typically offer the hotkey `Shift + Enter` to run the current selected cell. This applies to both Colab and VS Code.

### Colab authorship warning

If you receive a warning, review the warning, then click `Run Anyway`:

![Colab notebook authorship warning](/.github/images/colab-notebook-warning-run-cell-Annotation_2020-08-05_143410.png)

## Toggling a cell's mode between code and text

### Using Colab

#### Convert code to text

Select the cell, then hold `Ctrl` or `⌘` and type `MM`.

#### Convert text to code

Select the cell, then hold `Ctrl` or `⌘` and type `MY`.

### Using VS Code

Select the cell, then at the top of the cell click either `M` to convert to text, or `{}` to convert to code.