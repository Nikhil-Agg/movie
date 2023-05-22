
# MovieFy

MovieFy is used to search movies on the basis of directors, actors, and genre.


# Running MovieFy locally
- Create a virtual env using python2.7. Follow the below commands to do the same -
    `sudo apt install python2 virtualenv`

    `virtualenv --python=$(which python2) /path/to/newenv/folder/`
- Enable virtual environment with the help of the below command - 

    `source <venv folder>/bin/activate`
- After enabling install the dependencies from requirements.txt

    `pip install -r requirements.txt`
- Runserver using the below command - 

    `python service.py`

Head to http://127.0.0.1:8080 to view the website.