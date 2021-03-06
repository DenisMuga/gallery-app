# Muga_Gallery 
## Author  
  
>[DenisMuga](https://github.com/DenisMuga)  
  
# Description  
Muga_Gallery a Django application for personal gallery that allows a user to upload images for other to see and be able to to share by coping the image link.
  
##  Live Link  
 Click [View Site](https://mugasgallery.herokuapp.com/)  to visit the site
 
## User Story  
* View categories of photos they like. 
* Click a single image to expand it and view the details of that photo  
* Copy a link to the photo to share with my friends. 
* Search and filter based on categories 
* View photos based on the location they were taken.
  
## Setup and Installation  
To get the project .......  
  
##### Cloning the repository:  
 ```bash 
 https://github.com/DenisMuga/gallery-app.git
```
##### Navigate into the folder and install requirements  
 ```bash 
cd muga_gallery cd mygallery pip install -r requirements.txt 
```
##### Install and activate Virtual  
 ```bash 
- python3 -m venv virtual - source virtual/bin/activate  
```  
##### Install Dependencies  
 ```bash 
 pip install -r requirements.txt 
```  
 ##### Setup Database  
  SetUp your database User,Password, Host then make migrate  
 ```bash 
python manage.py makemigrations pictures 
 ``` 
 Now Migrate  
 ```bash 
 python manage.py migrate 
```
##### Run the application  
 ```bash 
 python manage.py runserver 
``` 
##### Running the application  
 ```bash 
 python manage.py server 
```
##### Testing the application  
 ```bash 
 python manage.py test 
```
Open the application on your browser `127.0.0.1:8000`.  
  
  
## Technology used  
  
* [Python3.8](https://www.python.org/)  
* [Django 3.2](https://docs.djangoproject.com/en/2.2/)  
* [Heroku](https://heroku.com)  
  
  
## Known Bugs  
* There are no known bugs currently but pull requests are allowed incase you spot a bug  
  
## Contact Information   
If you have any question or contributions, please email me at [mugah2011@gmail.com]  
  
## License 

MIT License

* Copyright (c) 2022 **Denis Muga**