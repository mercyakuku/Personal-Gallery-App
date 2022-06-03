## Personal-Gallery-App

## By mercyakuku  
  
# Description  
This is a Django application of a personal gallery that displays photos for users to view, share images by copying the image link and view image details  by category, location and description.
  
##  Live Link  
  Click this link https://kushgallery.herokuapp.com/  to visit the site..
  
## Screenshots 
 ## Home page
  <img src="https://user-images.githubusercontent.com/100420952/171779725-b0cec5a9-51d8-4fa0-a755-0458bc3ac90d.png">
  
 ## Search results
 <img src="https://user-images.githubusercontent.com/100420952/171779580-69c96414-9d55-4548-bfb6-22ffc2831ac4.png">
 
 ## Image Details 
<img src="https://user-images.githubusercontent.com/100420952/171779811-7943a066-f72f-4ce7-b85b-1b02ecd20c74.png">
 
## User Story  
  
* View different photos that interest them. 
* Click a single image to expand it and view the details of that photo. 
* Search for different categories.  
* Copy a link to the photo to share with my friends.  
* View photos based on the location they were taken.  
  

  
## Setup and Installation  
To get the project .......  
  
##### Cloning the repository:  
 ```bash 
 https://github.com/mercyakuku/Personal-Gallery-App.git
```
##### Navigate into the folder and install requirements  
 ```bash 
cd Personal-Gallery-App pip install -r requirements.txt 
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
  
  
## Technologies used  
  
* [Python3.8](https://www.python.org/)  
* [Django 4.0](https://docs.djangoproject.com/en/2.2/)  
* [Heroku](https://heroku.com)  
  
  
## Known Bugs  
* There are no known bugs currently but pull requests are allowed incase you spot a bug. 
  
## Contact Information   
If you have any question or contributions, please email me at [mercyakuku24@gmail.com]  
  
## License 
MIT License

Copyright (c) 2022 mercyakuku

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.

Copyright &copy 2022 mercyakuku
