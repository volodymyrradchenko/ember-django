# WIP // TUTORIAL. Ember.js + Django REST framework


## To-dos: 
- [ ] Setting up backend
  - [x] pyenv and virtualenv
- [ ] Setting up frontend
  - [ ] node.js and nvm


## Building minimal Ember.js client and Django server

This is a minimal guide to setting up basic Django backend and making it work with Ember.js


## Contents

- [Step 1. Setting up python environment](#step-1)
- [Step 2. Setting up node environment](#step-2)

## <a name='step-1'></a>Step 1

### Install Python version manager, virtual environment manager and everything they need to work correctly

- git is needed to install pyenv-installer
- pyenv lets you easily switch between multiple versions of Python
- pyenv-virtualenv lets you easily switch between multiple virtual environments
- pyenv-installer is needed to install pyenv and pyenv plugins for virtual environments control

## Prerequisites

Installing git
 
 ```bash
 sudo apt-get install git 
 ```

Installing pyenv and plugins using pyenv-installer
 
 ```bash
 curl -L https://github.com/pyenv/pyenv-installer/raw/master/bin/pyenv-installer | bash
```

Adding lines to the end of `~/.bashrc` file located in the root folder
```bash
export PATH="/home/mint/.pyenv/bin:$PATH"
eval "$(pyenv init -)"
eval "$(pyenv virtualenv-init -)"
```

Installing requirements for pyenv
```bash
sudo apt-get install -y make build-essential libssl-dev zlib1g-dev libbz2-dev \
libreadline-dev libsqlite3-dev wget curl llvm libncurses5-dev libncursesw5-dev \
xz-utils tk-dev libffi-dev
```

According to current Django REST and Django REST JSON API documentation the latest python version they support is 3.6.

Tipe the following code to install Python version 3.6.6

```bash
pyenv install 3.6.6
```

Create and open our project directory

```bash
mkdir ember-django && cd ember-django
```

Create and switch to our backend directory
```bash
mkdir backend && cd backend
```

Create a virtual environment for the project
```bash
pyenv virtualenv 3.6.6 ember-django-3.6.6
```
_ember-django-3.6.6 is the name of virtual env, you can give it any name_

Now we'll create a `.python-version` file with the name of our virtualenv so it would automatically switch to proper virtual environment every time we open backend folder
```bash
echo "ember-django-3.6.6" > .python-version
```

Let's install latest Django version
```bash
pip install Django==2.0.7
```

Django REST

```bash
pip install djangorestframework
```

and Django REST Framework JSON API

```bash
pip install djangorestframework-jsonapi
```

Let's initialize project in current directory
```bash
django-admin.py startproject backend .
```
_Note "." character at the end of line above._







## Welcome to GitHub Pages

You can use the [editor on GitHub](https://github.com/volodymyrradchenko/ember-django/edit/master/README.md) to maintain and preview the content for your website in Markdown files.

Whenever you commit to this repository, GitHub Pages will run [Jekyll](https://jekyllrb.com/) to rebuild the pages in your site, from the content in your Markdown files.

### Markdown

Markdown is a lightweight and easy-to-use syntax for styling your writing. It includes conventions for

```markdown
Syntax highlighted code block

# Header 1
## Header 2
### Header 3

- Bulleted
- List

1. Numbered
2. List

**Bold** and _Italic_ and `Code` text

[Link](url) and ![Image](src)
```

For more details see [GitHub Flavored Markdown](https://guides.github.com/features/mastering-markdown/).

### Jekyll Themes

Your Pages site will use the layout and styles from the Jekyll theme you have selected in your [repository settings](https://github.com/volodymyrradchenko/ember-django/settings). The name of this theme is saved in the Jekyll `_config.yml` configuration file.

### Support or Contact

Having trouble with Pages? Check out our [documentation](https://help.github.com/categories/github-pages-basics/) or [contact support](https://github.com/contact) and we’ll help you sort it out.
