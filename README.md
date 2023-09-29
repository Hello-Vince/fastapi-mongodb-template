# fastapi-mongodb-template

## Install pip-tools in venv

pip install pip-tools

## use pip-tools

pip-compile requirements/requirements.in\
pip install -r requirements/requirements.txt

## setup the MongoDB docker

Docker build —tag ‘tag_name’ .\
Docker run -d ‘image_name’
