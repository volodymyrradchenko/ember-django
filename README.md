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
  - [x] Prerequisites
  - [x] Creating our app
  - [x] Navigation
  - [x] Routes
  - [x] Model
  - [x] Posts
  - [x] Posts Delete
  - [ ] Posts New
  - [ ] Posts Edit


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
  - [Step 2.2 Creating app](#step-2-2)
  - [Step 2.3 Navigation](#step-2-3)
  - [Step 2.4 Routes](#step-2-4)
  - [Step 2.5 Model](#step-2-5)
  - [Step 2.6 Posts](#step-2-6)
  - [Step 2.7 Posts Delete](#step-2-7)
  - [Step 2.8 Posts New](#step-2-8)
  - [Step 2.9 Posts Edit](#step-2-9)



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
_**NOTE** mention "." character at the end of the line above._

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

And we want Django to pluralize and camelize types:
```python
JSON_API_PLURALIZE_TYPES = True
JSON_API_FORMAT_TYPES = 'camelize'
```

## <a name='step-1-3'></a>Step 1.3 Model

We're going to start by creating a simple `Post` model that will store our posts.
Add the following code to `posts/models.py`
```python
from django.db import models


class Post(models.Model):
	title = models.CharField(max_length=100, blank=True, default='')
	body = models.TextField(default='')
	url = models.URLField(default='')

	class Meta:
		ordering = ('id',)
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
        fields = ('id', 'title', 'body', 'url', )
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
_you can find more examples at DJAs [github page](https://github.com/django-json-api/django-rest-framework-json-api/blob/master/example/views.py)_

## <a name='step-1-6'></a>Step 1.6 Routes

Let's register appropriate view sets at `posts/urls.py`
```python
from django.conf.urls import include, url
from rest_framework import routers

from posts.views import PostViewSet

router = routers.DefaultRouter(trailing_slash=False)

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

you'll see an empty Posts List at [http://127.0.0.1:8000/posts/](http://127.0.0.1:8000/posts/)

_**NOTE** [JSON API conventions](http://jsonapi.org/recommendations/) suggest us to avoid using trailing slashes (trailing_slash=False). So pay attention if you're using trailing slashes in your browser or not.

If you'll scroll to the bottom of the page you'll notice an HTML form that allows us to `PUT` some information to the server. Try to add your first post.

Now, if you'll go to [http://127.0.0.1:8000/posts/](http://127.0.0.1:8000/posts/) you'll see a list of posts and if you'll go to [http://127.0.0.1:8000/posts/1/](http://127.0.0.1:8000/posts/1/) you'll see your first post.

# <a name='step-2'></a>Step 2 Frontend

We want our application to:
- display some information on the home page
- link to the list of posts, where we'll be able to:
  - create new post
  - view certain post
  - edit existing post
  - delete existing post

### Resources:
- [https://github.com/netguru/ember-styleguide](https://github.com/netguru/ember-styleguide)
- [https://www.emberjs.com/learn/](https://www.emberjs.com/learn/)
- [Install Node](https://yoember.com/nodejs/the-best-way-to-install-node-js/)
- DockYard's [Styleguide](https://github.com/DockYard/styleguides/blob/master/engineering/ember.md)
- [https://www.w3schools.com/](https://www.w3schools.com/)

## <a name='step-2-1'></a>Step 2.1 Prerequisites

Before starting our ember project we'll need to set up virtual environment and install Node.js. All you need to do is just to follow [zoltan-nz](https://yoember.com/nodejs/the-best-way-to-install-node-js/)'s recomendations.


## <a name='step-2-2'></a>Step 2.2 Creating app

After you installed node.js run the following command in your terminal. Make sure you're in our projects root directory. Add `--yarn` to the line following if you're using yarn as dependency manager.
```shell
ember new frontend
```

And to simplify our development process let's install ember-cli-sass. If you've used yarn in the previous step, then ember will automatically install addon using your preferred package manager.
```shell
ember install ember-cli-sass
```

Let's turn on some dev options and pods folder structure in `config/environment.js`. Just uncomment the following.
```js
ENV.APP.LOG_ACTIVE_GENERATION = true;
ENV.APP.LOG_TRANSITIONS = true;
ENV.APP.LOG_TRANSITIONS_INTERNAL = true;
ENV.APP.LOG_VIEW_LOOKUPS = true;
```
and add this line
```js
let ENV = {
  ...
  podModulePrefix: 'frontend/pods',
  ...
```

Now we can start our backend from `ember-django/backend` folder
```shell
python manage.py runserver
```

And proxy our ember server to `http://127.0.0.1:8000/` running the following from `ember-django/frontend` folder
```shell
ember s --proxy http://127.0.0.1:8000/
```

It's that easy!

## <a name='step-2-3'></a>Step 2.3 Navigation

Let's start with a simple navigation for the blog. We are going to create a 'main-header' component that will include 'nav-bar' and 'sub-menu' components. To not to get lost in that amount of directories and subdirectories we'll use ember pods structure.

```shell
ember g component main-header --pod
```
and 
```shell
ember g component main-header/nav-bar --pod
```

This will create a folder `pods` in our `app` directory. Each pod component will have `component.js` and template.hbs generated. Let's also make it possible to add scss files so we could style our components.

```shell
ember install ember-component-css
```

To make it work you must `app/styles/app.css` to `app/styles/app.scss` and add one single import. 
```scss
@import 'pod-styles';
```

Now we can style each component separately. Let's create a `styles.scss` file in `pods/components/main-header/nav-bar` folder, and add this styling to it.
```scss
& {
    ul {
        list-style-type: none;
        margin: 0;
        padding: 0;
        overflow: hidden;
        border: 1px solid #e7e7e7;
        background-color: #f3f3f3;

        li:last-child {
            float: right;
        }

        li {
            float: left;

            a {
                display: block;
                color: #666;
                text-align: center;
                padding: 14px 16px;
                text-decoration: none;
            }

            a:hover:not(.active) {
                background-color: #ddd;
            }

            a.active {
                color: white;
                background-color: #4CAF50;
            }
        }
    }
}
```

And a template with our `index` and funture `about` and `posts` link.
```
<ul>
  <li>{{#link-to 'index'}}Home{{/link-to}}</li>
  <li>{{#link-to 'posts'}}Posts{{/link-to}}</li>
  <li>{{#link-to 'about'}}About{{/link-to}}</li>
</ul>
```

Now we have to include nav-bar to the main-header component. Open `main-header/template.hbs` file and add the following.
```
{{yield (hash
  navBar=(component 'main-header/nav-bar')
  )
}}
```

And don't forget to add our main-header component to the `templates/application.hbs` file.
```
{{#main-header as |header|}}
  {{header.navBar}}
{{/main-header}}

{{outlet}}
```
Now you should be able to see a simple nav-bar and with one 'Home' button and an error in console saying that there's no such routes.

## <a name='step-2-4'></a>Step 2.4 Routes

Now let's add the missing about route!
```shell
ember g route about
```

And posts route in a separate folder.
```shell
ember g route posts/index
```
and
```shell
ember g route posts/new
```

Now if you start the server you should be able to navigate to Posts and About page.

## <a name='step-2-5'></a>Step 2.5 Model

Let's generate a model for our posts.
```shell
ember g model post title:string body:string url:string
```

And add the following to the `routes/posts/index.js`
```js
import Route from '@ember/routing/route';

export default Route.extend({
  model() {
    return this.store.findAll('post');
  }
});
```

## <a name='step-2-6'></a>Step 2.6 Posts

Now let's create post-container component that will include post-card component and be a wrapper for all postcards we'll have.
```shell
ember g component post-container --pod
```
and 
```shell
ember g component post-container/post-card --pod
```

Let's edit post-card component first. Add followinf to the `template.hbs`
```
<div class="card margin">
    <img src="{{url}}" style="width:100%">
    <div class="container">
      <h3><b>{{title}}</b></h3>
    </div>
    <div class="container">
      <p>{{body}}</p>
    </div>
</div>
```
Now let's style it - create file `styles.scss` and add
```scss
& {
  .card {
    box-shadow: 0 4px 10px 0 rgba(0,0,0,0.2), 0 4px 20px 0 rgba(0,0,0,0.19);
  }

  .margin{
    margin: 16px;
  }

  .container {
    padding: 0.01em 16px;
  }

  .opacity {
    opacity: 0.60;
  }
}
```

Now let's edit `post-container/template.hbs`
```
{{yield (hash 
  postCard=(component 'post-container/post-card' 
  url=url 
  body=body 
  title=title 
  created=created)
  )
}}
```
And add a grid too. Create `post-container/styles.scss`
```scss
& {
  display: grid;
  grid-template-columns: repeat(auto-fill, minmax(300px, 1fr));
  grid-gap: 20px;
  align-items: start;
}
```
We'll aslo need a submenu for our navigation to access the list of posts and to create a new post.

Let's generate new pod component.
```shell
ember g component main-header/sub-menu --pod
```

Add to `sub-menu/template.hbs`
```
<ul>
  <li>{{#link-to 'posts.index'}}List{{/link-to}}</li>
  <li>{{#link-to 'posts.new'}}New{{/link-to}}</li>
</ul>
```
And create `sub-menu/styles.scss` with the following code.
```scss
& {
    ul {
        list-style-type: none;
        margin: 10px 0px 20px 15px;
        padding: 0;
        overflow: hidden;

        li {
        border: 1px solid #e7e7e7;
        background-color: #f3f3f3;
            float: left;

            a {
                display: block;
                color: #666;
                text-align: center;
                padding: 14px 16px;
                text-decoration: none;
            }

            a:hover:not(.active) {
                background-color: #ddd;
            }

            a.active {
                color: white;
                background-color: #4CAF50;
            }
        }
    }
}
```
And of course don't forget to include it in the main-header components `template.hbs`. Now it should look like this:
```
{{yield (hash 
  navBar=(component 'main-header/nav-bar')
  subMenu=(component 'main-header/sub-menu')
  )
}}
```

The last thing to do is to add our pod component to the template. So open file `templates/posts/index.hbs` and add the code.
```
{{#post-container as |pc|}}
  {{#each model as |post|}}
    {{pc.postCard model=post url=post.url title=post.title body=post.body}}
  {{/each}}
{{/post-container}}

{{outlet}}
```

Congratulations! Now you should be able to see your posts list.

## <a name='step-2-7'></a>Step 2.7 Posts Delete

Let's add a delete button to our post-card pod component. I'll use ember-concurrency task for doing that.
First, let's install it.
```shell
ember install ember-concurrency
```

Then add a delete button to the `app/pods/components/post-container/post-card/template.hbs` file.
```
<div class="card margin">
    <img src="{{url}}" style="width:100%">
    <div class="container">
      <h3><b>{{title}}</b></h3>
    </div>
    <div class="container">
      <p>{{body}}</p>
    </div>
    <button type="button" onclick={{perform deletePost}}>Delete</button>
</div>
```

Now let's edit our `component.js` file.
```js
import Component from '@ember/component';
import { task } from 'ember-concurrency';

export default Component.extend({
  model: null,

  deletePost: task(function* () {
    yield this.model.destroyRecord();
  })
});
```

Now you should be able to delete posts from the server.

## <a name='step-2-8'></a>Step 2.8 Posts New


## <a name='step-2-9'></a>Step 2.9 Posts Edit
