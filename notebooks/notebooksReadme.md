# Getting started with Jupyter notebooks

## Overview

Jupyter notebooks are documents that take coding in Python (and potentially other languages) to a whole new level. With a Jupyter notebook, you can:

1. Write, run and re-run code in a block-by-block basis, while keeping all variables in an active, interactive kernel space. Those blocks are called "cells."
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

## Create your first notebook

### Using Colab

When using Colab, the steps are as follows:

1. Open [Colaboratory](https://colab.research.google.com/) in your browser.
2. Sign in with a Google account if prompted.
3. You're done! By default, Colab opens the "Welcome to Colaboratory" notebook that demonstrates what's possible.

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

## Changing a cell's mode from code to text formatting (typically Markdown)

### Using Colab
