Hello everyone
I completed this odoo quickstart . Here is the breakdown of what I did:
installed python from deadsnakes on my ubuntu 22
python --version
Python 3.8.18
odoo --version
16
install requirements.txt
wget http://archive.ubuntu.com/ubuntu/pool/main/o/openssl/libssl1.1_1.1.0g-2ubuntu4_amd64.deb
sudo dpkg -i libssl1.1_1.1.0g-2ubuntu4_amd64.deb 
sudo apt-get install xfonts-base
sudo apt-get install xfonts-75dpi
sudo apt-get install xfonts-base
sudo apt-get install -y git  postgresql nano virtualenv xz-utils wget fontconfig libfreetype6 libx11-6 libxext6 libxrender1 node-less node-clean-css xfonts-75dpi
sudo apt install -f
sudo apt-get update
sudo apt-get upgrade
sudo apt install postgresql postgresql-client 
sudo -u postgres createuser -s hadiya
sudo apt install python3.8-distutils
pip install psycopg2-binary
sudo apt-get install libsasl2-dev python-dev libldap2-dev libssl-dev
sudo apt-get install libsasl2-dev python-dev-is-python3 libldap2-dev libssl-dev
pip install python-ldap
sudo apt-get install python3.8-dev
sudo apt install build-essential wget git python3-pip python3-dev python3-venv python3-wheel libfreetype6-dev libxml2-dev libzip-dev libsasl2-dev python3-setuptools libjpeg-dev zlib1g-dev libpq-dev libxslt1-dev libldap2-dev libtiff5-dev libopenjp2-7-dev

Create a pycharm project and add the run configuration

Create the following folder structure
-addons
  -estate
      -model
         __init__.py
         __manifest__.py
      -data
      -security
      -views
      __init__.py
      __manifest__.py
      
  -estate_account
      -models
Create 5 models and their corresponding views;
estate_property, property_tag, estate_property_offer, estate_property_type, inherited_model
## Estate property model
This model is based on property and it's given attributes.
## Property Tag
This model is based on tags a property can have. It has many to many relationship with estate property model.
A tag can have multiple properties and A properties can have multiple tags
## estate_property_offer
This model is based on the offers received on a property. It is used to track the offers received, refused, or accepted on a property.
## estate_property_type
This model is based on the type attribute of a property. A property can have only one type but a type can can be associated with many properties.
## inherited_model
This model is inherited from res.users to add listed properties  to the users form with the help of property_id key.
# Access rights
Add access rights to the created models
## Views
Views are used to display records to the user.
## Actions
Actions are used for user interaction with the web.
## Menus 
Menus are used to navigate to different models and views.
Add menus for property type, tags, and properties
## SQL constrains
Constraints are used to specify data for the table.
Add sql constrains for checking if price is strictly positive and tag names are unique
## Model Relations
Build relation between models , A property and tag has many2many relation, A property type and property has many2one relationship. A offer and property has one2many relation
## Computed Fields
Compute the deadline and validity using python code
Write onchange function for garden availability
Add buttons for cancel and sold properties, accept and refuse offer.
Inherit from res.users to add a page in users notebook to view all the properties their
Add link to estate_account module for accounting.

