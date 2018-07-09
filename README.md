# WIP // TUTORIAL. Ember.js + Django REST framework


## To-dos: 
- [ ] Django REST framework JSON API
  - [x] Prerequisites
  - [ ] Configuration and requirements
  - [ ] Serialization
  - [ ] Model
  - [ ] Views
  - [ ] Routes
- [ ] Setting up frontend
  - [ ] node.js and nvm


## Building minimal Ember.js client and Django server

This is a minimal guide to setting up basic Django backend and making it work with Ember.js


## Contents

- [Step 1. Prerequisites](#step-1)
- [Step 2. Configuration and requirements](#step-2)
- [Step 3. Serialization](#step-3)
- [Step 4. Model](#step-4)
- [Step 5. Views](#step-5)
- [Step 6. Routes](#step-6)

## <a name='step-1'></a>Step 1. Prerequisites

### Install Python version manager, virtual environment manager and everything they need to work correctly

- git is needed to install pyenv-installer
- pyenv lets you easily switch between multiple versions of Python
- pyenv-virtualenv lets you easily switch between multiple virtual environments
- pyenv-installer is needed to install pyenv and pyenv plugins for virtual environments control

## Prerequisites

Installing git
 
 ```shell
 sudo apt-get install git 
 ```

Installing pyenv and plugins using pyenv-installer
 
 ```shell
 curl -L https://github.com/pyenv/pyenv-installer/raw/master/bin/pyenv-installer | bash
```

Adding lines to the end of `~/.bashrc` file located in the root folder
```bash
export PATH="/home/mint/.pyenv/bin:$PATH"
eval "$(pyenv init -)"
eval "$(pyenv virtualenv-init -)"
```

Installing requirements for using pyenv
```shell
sudo apt-get install -y make build-essential libssl-dev zlib1g-dev libbz2-dev \
libreadline-dev libsqlite3-dev wget curl llvm libncurses5-dev libncursesw5-dev \
xz-utils tk-dev libffi-dev
```
## <a name='step-2'></a>Step 2. Configuration and requirements

According to the current Django REST and Django REST JSON API documentation the latest python version supported is 3.6

Type the following code to install Python version 3.6.6

```shell
pyenv install 3.6.6
```

Create and open our project directory

```shell
mkdir ember-django && cd ember-django
```

Create and switch to our backend directory
```shell
mkdir backend && cd backend
```

Create a virtual environment for the project and name it `ember-django-3.6.6`
```shell
pyenv virtualenv 3.6.6 ember-django-3.6.6
```

Now we'll create a `.python-version` file with the name of our virtualenv so it would automatically switch to proper virtual environment every time we open backend folder
```shell
pyenv local ember-django-3.6.6
```

Let's install latest Django version
```shell
pip install Django==2.0.7
```

Initialize project in the current directory
```shell
django-admin.py startproject backend .
```
_Note "." character at the end of the line above._

Once we've done that let's create an app that we'll use to create a Web API
```shell
python manage.py startapp posts
```

Now we can install Django REST Framework: a powerfull and flexible toolkit for building WEB APIs 

```shell
pip install djangorestframework
```

and additional package Django REST Framework JSON API

```shell
pip install djangorestframework-jsonapi
```
As suggested by DJA (Django REST Framework JSON API) let's add some code to `backend/settings.py`
```python
REST_FRAMEWORK = {
    'PAGE_SIZE': 10,
    'EXCEPTION_HANDLER': 'rest_framework_json_api.exceptions.exception_handler',
    'DEFAULT_PAGINATION_CLASS':
        'rest_framework_json_api.pagination.PageNumberPagination',
    'DEFAULT_PARSER_CLASSES': (
        'rest_framework_json_api.parsers.JSONParser',
        'rest_framework.parsers.FormParser',
        'rest_framework.parsers.MultiPartParser'
    ),
    'DEFAULT_RENDERER_CLASSES': (
        'rest_framework_json_api.renderers.JSONRenderer',
        # If you're performance testing, you will want to use the browseable API
        # without forms, as the forms can generate their own queries.
        # If performance testing, enable:
        # 'example.utils.BrowsableAPIRendererWithoutForms',
        # Otherwise, to play around with the browseable API, enable:
        'rest_framework.renderers.BrowsableAPIRenderer'
    ),
    'DEFAULT_METADATA_CLASS': 'rest_framework_json_api.metadata.JSONAPIMetadata',
}
```
Also, we'll need to add our new apps to the same file
```python
INSTALLED_APPS = (
    ...
    'rest_framework',
    'posts',
)
```

## <a name='step-3'></a>Step 3. Serialization


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
