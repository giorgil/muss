Quick Start Guide
=================


Download Muss forum Project
----------------------------------------------

First, you need to download Muss from GitHub.

You can visit the repository webpage in |muss_github| and download it as a zip file.


.. |muss_github| raw:: html

    <a href="https://github.com/mapeveri/muss" target="_blank">Github</a>

You can also do the same using your terminal with::

    $ git clone git@github.com:mapeveri/muss.git


Install the requirements
------------------------

Next, located in the root directory project, install the packages dependencies inside your virtual environment::

    $ pip install -r requirements.txt


Go to the conf/ folder and rename **settings_local.py.txt** file  to **settings_local.py** file.

Secret Django Key
-----------------

Muss has the SECRET_KEY environment variable hidden.
You can the generate the SECRET_KEY and export environment variable of this way:


Generating the SECRET_KEY
~~~~~~~~~~~~~~~~~~~~~~~~~

Locate in the root directory and type::

    $ python script/django-secret-keygen.py

This will generate the characters combination value to **SECRET_KEY**


Defining the SECRET_KEY environment variable
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Copy this value and paste it instead of **your_secret_django_key** value::

    $ export SECRET_KEY="your_secret_django_key"

With this previous step will be include your new **Django SECRET_KEY** inside your project

Migrating and create super user
-------------------------------

We sync the changes to the database::

    $ python manage.py migrate
    $ python manage.py createsuperuser


Setup the admin
~~~~~~~~~~~~~~~

Execute::

    $ python manage.py config_admin



Internationalization and Localization
-------------------------------------


Settings
~~~~~~~~

The default language for this Project is **English**, and the internationalization is used to translate the text to
Spanish and Italian languages.

If you want to change the translation language, or include a new one, you just need to modify the **LANGUAGES** variable
in the file *settings/base.py*. The language codes that define each language can be found |codes_link|.

.. |codes_link| raw:: html

    <a href="http://msdn.microsoft.com/en-us/library/ms533052(v=vs.85).aspx" target="_blank">here</a>

For example, if you want to use German you should include::

    LANGUAGES = (
            ...
            'de', _("German"),
            ...
        )



Translation
~~~~~~~~~~~

Go to the terminal, inside the muss folder and create the files to translate with::

    $ python manage.py compilemessages


Now, Go to the folder */static/muss* and execute::

    $ npm install
    $ bower install

Make sure you have a |redis_installer_link|

.. |redis_installer_link| raw:: html

    <a href="https://redis.io/topics/quickstart" target="_blank">redis installer.</a>

Continue to the :doc:`dev`!

