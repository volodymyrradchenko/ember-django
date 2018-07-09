# WIP // TUTORIAL. Ember.js + Django REST framework


## To-dos: 
- [x] Django REST framework JSON API
  - [x] Prerequisites
  - [x] Configuration and requirements
  - [x] Model
  - [x] Serialization
  - [x] Views
  - [x] Routes
- [ ] Setting up frontend
  - [ ] node.js and nvm


## Building minimal Ember.js client and Django server

This is a minimal guide to setting up basic Django backend and making it work with Ember.js


## Contents
- [Step 1 Backend](#step-1)
  - [Step 1.1 Prerequisites](#step-1-1)
  - [Step 1.2 Configuration and requirements](#step-1-2)
  - [Step 1.3 Model](#step-1-3)
  - [Step 1.4 Serialization](#step-1-4)
  - [Step 1.5 Views](#step-1-5)
  - [Step 1.6 Routes](#step-1-6)
- [Step 2 Frontend](#step-2)
  - [Step 2.1 Prerequisites](#step-2-1)


# <a name='step-1'></a>Step 1 Backend

Some description on what we'll do and how we'll do that goes here.

### Resources:
- [http://www.django-rest-framework.org](http://www.django-rest-framework.org)
- [http://django-rest-framework-json-api.readthedocs.io](http://django-rest-framework-json-api.readthedocs.io)
- [https://github.com/django-json-api/django-rest-framework-json-api](https://github.com/django-json-api/django-rest-framework-json-api)

Install Python version manager, virtual environment manager and everything they need to work correctly:
- git is needed to install pyenv-installer
- pyenv lets you easily switch between multiple versions of Python
- pyenv-virtualenv lets you easily switch between multiple virtual environments
- pyenv-installer is needed to install pyenv and pyenv plugins for virtual environments control

## <a name='step-1-1'></a>Step 1.1 Prerequisites

Installing git:
 
 ```shell
 sudo apt-get install git 
 ```

Installing pyenv and plugins using pyenv-installer:
 
 ```shell
 curl -L https://github.com/pyenv/pyenv-installer/raw/master/bin/pyenv-installer | bash
```

Adding lines to the end of `~/.bashrc` file located in the root folder:
```bash
export PATH="/home/mint/.pyenv/bin:$PATH"
eval "$(pyenv init -)"
eval "$(pyenv virtualenv-init -)"
```

Installing requirements for using pyenv:
```shell
sudo apt-get install -y make build-essential libssl-dev zlib1g-dev libbz2-dev \
libreadline-dev libsqlite3-dev wget curl llvm libncurses5-dev libncursesw5-dev \
xz-utils tk-dev libffi-dev
```
## <a name='step-1-2'></a>Step 1.2 Configuration and requirements



According to current documentation the latest python version supported is 3.6

Type the following code to install Python:

```shell
pyenv install 3.6.6
```

Create and open our project directory:

```shell
mkdir ember-django && cd ember-django
```

Create and switch to our backend directory:
```shell
mkdir backend && cd backend
```

Let's create a virtual environment for the project and name it, say an `ember-django-3.6.6`:
```shell
pyenv virtualenv 3.6.6 ember-django-3.6.6
```

It would be nice to automatically switch virtual environment on opening current folder. Running command below will create `.python-version` file with the name of our virtualenv.
```shell
pyenv local ember-django-3.6.6
```
_if you wish `echo "ember-django-3.6.6" > .python-version` will also do the thing_

Let's install latest Django version:
```shell
pip install Django==2.0.7
```

Initialize project in the current directory:
```shell
django-admin.py startproject backend .
```
_Note "." character at the end of the line above._

Once we've done that let's create an app that we'll use to create Web API.
```shell
python manage.py startapp posts
```

Now we can install Django REST Framework: a "powerfull and flexible toolkit for building WEB APIs".

```shell
pip install djangorestframework
```

and additional package Django REST Framework JSON API:

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
Also, we'll need to add our new apps:
```python
INSTALLED_APPS = (
    ...
    'rest_framework',
    'posts',
)
```

## <a name='step-1-3'></a>Step 1.3 Model

We're going to start by creating a simple `Post` model that will store our posts.
Add the following code to `posts/models.py`:
```python
from django.db import models


class Post(models.Model):
	created = models.DateTimeField(auto_now_add=True)
	title = models.CharField(max_length=100, blank=True, default='')
	body = models.TextField(default='')
	url = models.URLField(default='')

	class Meta:
		ordering = ('created',)
```

We'll need to create a migration for posts model:
```shell
python manage.py makemigrations posts
```

and syncronize the database for the first time:
```shell
python manage.py migrate
```

## <a name='step-1-4'></a>Step 1.4 Serialization

First of all, let's create `posts/serializers.py` file.

We'll provide a way of serializing and deserializing our posts instances into JSON representation by creating `PostSerializer` class. Let's use base serializer class so kindly provided by `rest_framework_json_api`
```python
from rest_framework_json_api import serializers
from posts.models import Post


class PostSerializer(serializers.ModelSerializer):
    class Meta:
        model = Post
        fields = ('id', 'created', 'title', 'body', 'url', )
```

## <a name='step-1-5'></a>Step 1.5 Views

We'll start by adding classes for handling JSON API requests and responses. Add the code below to `posts/views.py`
```python
import rest_framework.parsers
import rest_framework.renderers
from rest_framework import exceptions

import rest_framework_json_api.parsers
import rest_framework_json_api.metadata
from rest_framework_json_api.utils import format_drf_errors
from rest_framework_json_api.views import ModelViewSet


from posts.models import Post
from posts.serializers import PostSerializer


HTTP_422_UNPROCESSABLE_ENTITY = 422

class JsonApiViewSet(ModelViewSet):
    """
    This is an example on how to configure DRF-jsonapi from
    within a class. It allows using DRF-jsonapi alongside
    vanilla DRF API views.
    """
    parser_classes = [
        rest_framework_json_api.parsers.JSONParser,
        rest_framework.parsers.FormParser,
        rest_framework.parsers.MultiPartParser,
    ]
    renderer_classes = [
        rest_framework_json_api.renderers.JSONRenderer,
        rest_framework.renderers.BrowsableAPIRenderer,
    ]
    metadata_class = rest_framework_json_api.metadata.JSONAPIMetadata

    def handle_exception(self, exc):
        if isinstance(exc, exceptions.ValidationError):
            # some require that validation errors return 422 status
            # for example ember-data (isInvalid method on adapter)
            exc.status_code = HTTP_422_UNPROCESSABLE_ENTITY
        # exception handler can't be set on class so you have to
        # override the error response in this method
        response = super(JsonApiViewSet, self).handle_exception(exc)
        context = self.get_exception_handler_context()
        return format_drf_errors(response, context, exc)


class PostViewSet(JsonApiViewSet):
    queryset = Post.objects.all()
    serializer_class = PostSerializer
```
_you can find more examples at DJA [github page](https://github.com/django-json-api/django-rest-framework-json-api/blob/master/example/views.py)_

## <a name='step-1-6'></a>Step 1.6 Routes

Let's register appropriate view sets at `posts/urls.py`
```python
from django.conf.urls import include, url
from rest_framework import routers

from posts.views import PostViewSet

router = routers.DefaultRouter()

router.register(r'posts', PostViewSet)


urlpatterns = [
    url(r'^', include(router.urls)),
]
```

and don't forget to make migrations:
```shell
python manage.py makemigrations
```

and:
```shell
python manage.py migrate
```

If you'll run django server:
```shell
python manage.py runserver
```

you'll see an empty Posts List at [http://127.0.0.1:8000/posts/](http://127.0.0.1:8000/posts/).

_Note, that [JSON API conventions](http://jsonapi.org/recommendations/)  suggest us to avoid using trailing slashes. So, when we'll set up Ember.js client we'll have change one of the lines in `urls.py` to `router = routers.DefaultRouter(trailing_slash=False)`_

If you'll scroll to the bottom of the page you'll notice a HTML form that allows us to `PUT` some information to the server. Try to add your first post.

Now, if you'll go to [http://127.0.0.1:8000/posts/](http://127.0.0.1:8000/posts/) you'll see a list of posts and if you'll go to [http://127.0.0.1:8000/posts/1/](http://127.0.0.1:8000/posts/1/) you'll see our first post

# <a name='step-2'></a>Step 2 Frontend

Some description on what we'll do and how we'll do that goes here

### Resources:
- [https://github.com/netguru/ember-styleguide](https://github.com/netguru/ember-styleguide)
- [https://www.emberjs.com/learn/](https://www.emberjs.com/learn/)
- [https://yoember.com/nodejs/the-best-way-to-install-node-js/](https://yoember.com/nodejs/the-best-way-to-install-node-js/)