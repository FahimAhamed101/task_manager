# task_manager
if you go to
* http://127.0.0.1:8000/api/
By default, Django REST framework will produce a response like:

.. code:: JSON

    {
        "id": 9,
        "user": "fb1b0360-9872-4180-b745-9503500ae5b3",
        "title": "hhhhhhhh",
        "images": [
            {
                "id": 21,
                "image": "/media/images/notification.png",
                "tasks": 9
            },
            {
                "id": 22,
                "image": "/media/images/more.png",
                "tasks": 9
            }
        ]
    },


However, for an ``identity`` model in JSON:API format the response should look
like the following:

.. code:: JSON

    {
        "id": 9,
        "user": "fb1b0360-9872-4180-b745-9503500ae5b3",
        "title": "hhhhhhhh",
        "images": [
            {
                "id": 21,
                "image": "/media/images/notification.png",
                "tasks": 9
            },
            {
                "id": 22,
                "image": "/media/images/more.png",
                "tasks": 9
            }
        ]
    },


-----
Goals
-----

As a Django REST framework JSON:API (short DJA) we are trying to address following goals:

1. Support the `JSON:API`_ spec to compliance

2. Be as compatible with `Django REST framework`_ as possible

   e.g. issues in Django REST framework should be fixed upstream and not worked around in DJA

3. Have same defaults to be as easy to pick up as possible

4. Be solid and tested with good coverage

5. Be performant

.. _JSON:API: https://jsonapi.org
.. _Django REST framework: https://www.django-rest-framework.org/

------------
Requirements
------------

1. Python (3.8, 3.9, 3.10, 3.11)
2. Django (3.2, 4.1, 4.2)
3. Django REST framework (3.13, 3.14)

I **highly** recommend and only officially support the latest patch release of each Python, Django and REST framework series.

Generally Python and Django series are supported till the official end of life. For Django REST framework the last two series are supported.

For optional dependencies such as Django Filter only the latest release is officially supported even though lower versions should work as well.

------------
Installation
------------
#go to root rename .env.example to .env and setup your enviroment variables

Install using ``pip``...

.. code:: sh

    $ python -m venv env
    $ source env/Scripts/activate
    $ pip install -r requirements.txt
    $ python manage.py makemigrations
    $ python manage.py migrate
    $ python manage.py runserver
    $ python manage.py createsuperuser

or from source...

.. code:: sh

    $ git clone https://github.com/FahimAhamed101/task_manager.git
    $ cd task_manager
    $ pip install -r requirements.txt .




Running the example app
^^^^^^^^^^^^^^^^^^^^^^^

It is recommended to create a virtualenv for testing.



Browse to

* http://127.0.0.1:8000/api/ for the list of available collections (in a non-JSON:API format!),
* http://127.0.0.1:8000/api/create/ for a creating task in POSTman interface to create Task or
* http://127.0.0.1:8000/api/update/`{id}` for updating tasks and making put or patch request.
* http://127.0.0.1:8000/api/delete/`{id}` for deleting a single task request.

-----
Usage
-----


``rest_framework_json_api`` assumes you are using class-based views in Django
REST framework.

