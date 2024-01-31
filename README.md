Flask
=====

Flask is a lightweight `WSGI`_ web application framework. It is designed
to make getting started quick and easy, with the ability to scale up to
complex applications. It began as a simple wrapper around `Werkzeug`_
and `Jinja`_ and has become one of the most popular Python web
application frameworks.

Flask offers suggestions, but doesn't enforce any dependencies or
project layout. It is up to the developer to choose the tools and
libraries they want to use. There are many extensions provided by the
community that make adding new functionality easy.

.. _WSGI: https://wsgi.readthedocs.io/
.. _Werkzeug: https://werkzeug.palletsprojects.com/
.. _Jinja: https://jinja.palletsprojects.com/


Installing
----------

Install and update using `pip`_:

.. code-block:: text

    $ git clone <Repo Name>

.. _pip: https://pip.pypa.io/en/stable/getting-started/

### Setting up Virtual Environment

.. code-block:: text

    # Create a virtual environment (Python 3)
    python3 -m venv venv
    
    # Activate the virtual environment (Linux/Mac)
    source venv/bin/activate
    
    # Activate the virtual environment (Windows)
    venv\Scripts\activate

# Install required dependencies

.. code-block:: python

    pip install -r requirements.txt

Docker
------

To run the Flask application using Docker, you can follow these steps:

### Build Docker Image

```bash

    # Build the Docker image
    docker build -t yourflaskapp .
    
    # Run the Docker Container
    docker run -p 5000:5000 yourflaskapp

```




