# WIP // TUTORIAL. Ember.js + Django REST framework


## To-dos: 
- [ ] ### Setting up backend
  - [ ] pyenv and virtualenv
- [ ] ### Setting up frontend
  - [ ] node.js and nvm


## Building minimal Ember.js client and Django server

This is a minimal guide to setting up basic Django backend and making it work with Ember.js


## Contents

- [Step 1. Setting up python environment](#step-1)
- [Step 2. Setting up node environment](#step-2)

## <a name='step-1'></a>Step 1

### Install Simple Python Version Management: pyenv

pyenv lets you easily switch between multiple versions of Python.

 Installing git
 
 ```bash
 apt-get install git 
 ```
 Installing pyenv and plugins using pyenv-installer
 
 ```bash
 curl -L https://github.com/pyenv/pyenv-installer/raw/master/bin/pyenv-installer | bash
```
add lines to the end of ~/.bashrc 

```bash
export PATH="/home/mint/.pyenv/bin:$PATH"
eval "$(pyenv init -)"
eval "$(pyenv virtualenv-init -)"
```
requirements for pyenv 

```bash
sudo apt-get install -y make build-essential libssl-dev zlib1g-dev libbz2-dev \
libreadline-dev libsqlite3-dev wget curl llvm libncurses5-dev libncursesw5-dev \
xz-utils tk-dev libffi-dev
```

According to current Django REST and Django REST JSON API documentation the latest python version they support is 3.6,  
so let's install python 3.6.6:

```bash
pyenv install 3.6.6
```

lets create and open directory for our project

```bash
mkdir ember-django $$ cd ember-django
```
and a backend directory
```bash
mkdir backend $$ cd backend
```
create a virtual environment for the project

```bash
pyenv virtualenv 3.6.6 ember-django-3.6.6
```
now we will create a .python-version file with the name of our virtualenv so it would automatically switch to proper version after opening backend folder
```bash
echo "ember-django-3.6.6" > .python-version
```

now let's install latest Django version

```bash
pip install Django==2.0.7
```

install Django REST

```bash
pip install djangorestframework
```

and Django REST Framework JSON API

```bash
pip install djangorestframework-jsonapi
```
let's initialize project at the current directory
```bash
django-admin.py startproject backend .
```
Note "." character at the end of line above.







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
