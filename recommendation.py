#!/usr/bin/env python
# coding: utf-8

# # Notebook Basics
# ---

# In[3]:


# Import Pandas
import pandas as pd


# This lesson assumes that the user has Jupyter [installed](https://jupyter.readthedocs.io/en/latest/install.html) and that the notebook server can be started by running:
# 
#     jupyter notebook
# 
# For more details on how to run the notebook server, see [Running the Notebook Server](Running%20the%20Notebook%20Server.ipynb).

# ## The Dashboard
# ---

# When the notebook server is first started, a browser will be opened to the notebook dashboard. The dashboard serves as a home page for the notebook. Its main purpose is to display the portion of the filesystem accessible by the user, and to provide an overview of the running kernels, terminals, and parallel clusters.

# ### Files Tab
# 
# The files tab provides an interactive view of the portion of the filesystem which is accessible by the user. This is typically rooted by the directory in which the notebook server was started.
# 
# The top of the files list displays clickable breadcrumbs of the current directory. It is possible to navigate the filesystem by clicking on these breadcrumbs or on the directories displayed in the notebook list.
# 
# A new notebook can be created by clicking on the **`New`** dropdown button at the top of the list, and selecting the desired language kernel.
# 
# Notebooks can also be uploaded to the current directory by dragging a notebook file onto the list or by clicking the **`Upload`** button at the top of the list.
# 
# <img src="images/dashboard_notebooks_tab_5_0.png" />

# ### Running Tab
# 
# The running tab displays the currently running notebooks which are known to the server. This view provides a convenient way to track notebooks that have been started during a long running notebook server session.
# 
# Each running notebook will have an orange **`Shutdown`** button which can be used to shutdown its associated kernel. Closing the notebook's page is not sufficient to shutdown a kernel.
# 
# Running terminals are also listed, provided that the notebook server is running on an operating system which supports PTY.
# 
# <img src="images/dashboard_running_tab_4_0.png" />

# ### Clusters Tab
# 
# The clusters tab provides a summary view of [IPython Parallel](https://ipyparallel.readthedocs.io/en/latest/) clusters. The IPython Parallel extension must be [installed](https://github.com/ipython/ipyparallel) in order to use this feature.
# 
# <img src="images/dashboard_clusters_tab_4_0.png" />

# ## The Notebook
# ---

# When a notebook is opened, a new browser tab will be created which presents the notebook user interface (UI). This UI allows for interactively editing and running the notebook document.
# 
# A new notebook can be created from the dashboard by clicking on the **`Files`** tab, followed by the **`New`** dropdown button, and then selecting the language of choice for the notebook.
# 
# An interactive tour of the notebook UI can be started by selecting **`Help -> User Interface Tour`** from the notebook menu bar.

# ### Header
# 
# At the top of the notebook document is a header which contains the notebook title, a menubar, and toolbar. This header remains fixed at the top of the screen, even as the body of the notebook is scrolled. The title can be edited in-place (which renames the notebook file), and the menubar and toolbar contain a variety of actions which control notebook navigation and document structure.
# 
# <img src="images/notebook_header_4_0.png" />

# ### Body
# 
# The body of a notebook is composed of cells. Each cell contains either markdown, code input, code output, or raw text. Cells can be included in any order and edited at-will, allowing for a large ammount of flexibility for constructing a narrative.
# 
# - **Markdown cells** - These are used to build a nicely formatted narrative around the code in the document. The majority of this lesson is composed of markdown cells.
# 
# - **Code cells** - These are used to define the computational code in the document. They come in two forms: the *input cell* where the user types the code to be executed, and the *output cell* which is the representation of the executed code. Depending on the code, this representation may be a simple scalar value, or something more complex like a plot or an interactive widget.
# 
# - **Raw cells** - These are used when text needs to be included in raw form, without execution or transformation.
# 
# <img src="images/notebook_body_4_0.png" />

# #### Modality
# 
# The notebook user interface is *modal*. This means that the keyboard behaves differently depending upon the current mode of the notebook. A notebook has two modes: **edit** and **command**.
# 
# **Edit mode** is indicated by a green cell border and a prompt showing in the editor area. When a cell is in edit mode, you can type into the cell, like a normal text editor.
# 
# <img src="images/edit_mode.png">
# 
# **Command mode** is indicated by a grey cell border. When in command mode, the structure of the notebook can be modified as a whole, but the text in individual cells cannot be changed. Most importantly, the keyboard is mapped to a set of shortcuts for efficiently performing notebook and cell actions. For example, pressing **`c`** when in command mode, will copy the current cell; no modifier is needed.
# 
# <img src="images/command_mode.png">
# 
# <br>
# <div class="alert alert-success">
# Enter edit mode by pressing `Enter` or using the mouse to click on a cell's editor area.
# </div>
# <div class="alert alert-success">
# Enter command mode by pressing `Esc` or using the mouse to click *outside* a cell's editor area.
# </div>
# <div class="alert alert-warning">
# Do not attempt to type into a cell when in command mode; unexpected things will happen!
# </div>

# #### Mouse navigation
# 
# The first concept to understand in mouse-based navigation is that **cells can be selected by clicking on them.** The currently selected cell is indicated with a grey or green border depending on whether the notebook is in edit or command mode. Clicking inside a cell's editor area will enter edit mode. Clicking on the prompt or the output area of a cell will enter command mode.
# 
# The second concept to understand in mouse-based navigation is that **cell actions usually apply to the currently selected cell**. For example, to run the code in a cell, select it and then click the <button class='btn btn-default btn-xs'><i class="fa fa-play icon-play"></i></button> button in the toolbar or the **`Cell -> Run`** menu item. Similarly, to copy a cell, select it and then click the <button class='btn btn-default btn-xs'><i class="fa fa-copy icon-copy"></i></button> button in the toolbar or the **`Edit -> Copy`** menu item. With this simple pattern, it should be possible to perform nearly every action with the mouse.
# 
# Markdown cells have one other state which can be modified with the mouse. These cells can either be rendered or unrendered. When they are rendered, a nice formatted representation of the cell's contents will be presented. When they are unrendered, the raw text source of the cell will be presented. To render the selected cell with the mouse, click the <button class='btn btn-default btn-xs'><i class="fa fa-play icon-play"></i></button> button in the toolbar or the **`Cell -> Run`** menu item. To unrender the selected cell, double click on the cell.

# #### Keyboard Navigation
# 
# The modal user interface of the IPython Notebook has been optimized for efficient keyboard usage. This is made possible by having two different sets of keyboard shortcuts: one set that is active in edit mode and another in command mode.
# 
# The most important keyboard shortcuts are **`Enter`**, which enters edit mode, and **`Esc`**, which enters command mode.
# 
# In edit mode, most of the keyboard is dedicated to typing into the cell's editor. Thus, in edit mode there are relatively few shortcuts. In command mode, the entire keyboard is available for shortcuts, so there are many more possibilities.
# 
# The following images give an overview of the available keyboard shortcuts. These can viewed in the notebook at any time via the **`Help -> Keyboard Shortcuts`** menu item.
# 
# <img src="images/notebook_shortcuts_4_0.png">
# 
# The following shortcuts have been found to be the most useful in day-to-day tasks:
# 
# - Basic navigation: **`enter`**, **`shift-enter`**, **`up/k`**, **`down/j`**
# - Saving the notebook: **`s`**
# - Cell types: **`y`**, **`m`**, **`1-6`**, **`r`**
# - Cell creation: **`a`**, **`b`**
# - Cell editing: **`x`**, **`c`**, **`v`**, **`d`**, **`z`**, **`ctrl+shift+-`**
# - Kernel operations: **`i`**, **`.`**

# ## The Text Editor
# ---

# The notebook application has the ability to edit more than just notebook files and code cells. Any plain text file can be edited using the built-in text editor.
# 
# The text editor will be opened in a new browser tab whenever a non-notebook text file is accessed from the dashboard. A new text file can also be created from the dashboard by clicking on the **`Files`** tab, followed by the **`New`** dropdown button, and then selecting **`Text File`**.
# 
# The text editor has a header which is similar to that of the notebook's, and includes the document title and a menubar. The syntax highlighting for the text file is determined automatically by the file extension. It can also be set manually via the **`Language`** option in the menubar.
# 
# <img src="images/text_editor_4_0.png">

# ## The Terminal
# ---

# If the notebook server is run on an operating system which supports [PTY](https://en.wikipedia.org/wiki/Pseudoterminal) (Linux/Mac), then the notebook application will be able to spawn interactive terminal instances. If the operating system does not support PTY (Windows), the terminal feature will not be enabled.
# 
# A new terminal can be spawned from the dashboard by clicking on the **`Files`** tab, followed by the **`New`** dropdown button, and then selecting **`Terminal`**.
# 
# The terminal supports all applications which would otherwise run in a PTY, this includes classical terminal applications like Vim, Nano, and Bash.
# 
# <img src="images/terminal_4_0.png">
