# vsnquery
Querying a Car VSN db: python/django


Assumptions:

1) Instructions for compile and run documented at the moment only for Mac OS

2) DB back-end chosen as sqlite3 for simplicity of prototyping for this exercise

3) Make of vehicles does not exceed 3 characters

4) Models of vehicles does not exceed 200 characters 

5) Trim Name of vehicles is under 20 characters 

6) Python 2.7

7) Django 1.8.3 

8) Use of simple css here in exercise to showcase knowledge/usage, without getting too extensive in interests of time

9) Lower case or upper case queries for VSN should work; along with pre- and post- blank space characters

10) Primary key not yet used in db (scope for improvement later with speed up=> see limitations/scope section)

11) Unit tests not yet done in interest of time but can follow : https://docs.djangoproject.com/en/1.8/topics/testing/overview/. Manual testing done for now.

12) Advanced django forms, or having advanced get/post etc was not done, since sometimes simple solutions are preferred for simple problems

13) We assume the input VSNs to the form do not have wildcards but are full VSN numbers. The wildcard '*' are only in the csv/db

14) In case of multiple equal matches, we just return the first match. We can easily improve the solution to return all matches if required/requested. For now, we assume the earliest db entry is preferred. 

Dependencies (packages/modules):


1) python 'csv': to read csv file 

2) python 're': for regexp string pattern finds/searches

3) python 'template' module with multiple libraries such as RequesContext, loader, etc

4) django models for sqlite db

5) django http: for HTTP response send

6) gunicorn: production server deployment for multi-threaded master-worker process architecture for server deployment for scaling (later nginx f/e can be used with local proxy for further scaling)




Installation Requirements (tested and listed only on MAC OSX Yosemite):

Note: Use 'sudo' with some of below instructions in case of issues with permissions to root related paths, assuming you have sudo access. Other platforms with VMs/Docker installation steps are to be done, TBD.


1) Open up a mac terminal (OSX 10.10.4)

2) Clone the git repo: 'git clone https://github.com/vivekv77/vsnquery.git'

3) Set up basic environment: https://docs.djangoproject.com/en/1.8/topics/install/ 

a) python

b) pip : use the file 'get-pip.py' in top folder to do: 'python get-pip.py'

c) django: 'pip install Django==1.8.3'


4) Install gunicorn: 'pip install gunicorn'

5) Validate that django is installed: 'python -c "import django; print(django.get_version())"'

6) Delete any existing migration folders under vsnquery/vsnQuery/importVsns and delete db.sqlite3 file under vsnquery/vsnQuery

7) go to folder containing manage.py

8) To create the db: 'python manage.py makemigrations importVsns' followed by 'python manage.py migrate'

9) To import csv to db: 'python manage.py shell < ./importVsns/importCsvToDb.py'



To run Web Server:


1) Development mode (while coding/testing/iterating):

'python manage.py runserver'

2) Production mode (deployment):

'gunicorn vsnQuery.wsgi'

Go on your local web browser to http://127.0.0.1:8000.


Limitations and Scope for Improvement:

1) Admin and Input Data

Admin page to enter new db entries is not done. This is TBD. Also we assume the csv input db is "clean" and do not account for or check for "holes" or "gaps" in the input file (error handling)


2) Scalability

We have a direct browser to django interface, albeit scaling with gunicorn across multiple threads. We need nginx or apache f/e to scale better and use multiple localhost ports to local proxy.

3) F/E Responsiveness

Mobile responsiveness : untested. Mobile scaling once we add more fancies to f/e needs to be a key design consideration.


4) Error Handling


In general, the failure cases could be handled better, such as csv data with "holes" (incomplete), handling unsupported views (what if user goes to http://localhost:8000/foobar - gets random 404 error), paths within code need better error handling etc.


We also do not log errors to a log file (leads to devOps) in this exercise.


5) Cross-platform compilation and support

Instructions only for Mac today, no linux or windows or other OS, and also bugs, performance testing, etc not done. 


6) Auto-start

Today, we have to manually start using gunicorn or runserver the actual server. In production server deployment, one must start the server app upon bootup of the OS after initial uboot, etc done. We need conf to be set and/or watchdog process to kick server app back up if it crashes, etc.



7) Performance Improvements

Faster search, avoid db bloat, allow for scalability.

a) Indexed searches through elasticsearch and Haystack
b) Speed up db searches using primary/other keys for searching, as well as pre-sorting, divide and conquer (dictionary type approaches) and/or using graph (neo4j) or other back-ends
c) Use lower latency faster b/e such as nodejs async with cassandra NoSQL db for better scaling/perf
d) Instead of http GET requests for searching the server db, we can use websockets which are more lightweight and scale better, ex: socket.io


8) Testing

a) Unit tests need to be added 
b) Failure tests (bad input cases, etc) need to be added
c) Stress tests to pump 100k-100 mill requests per second using a dummy "client" need to be added to test load based performance/latency/resource loading


9) Hosting server on AWS/Heroku with auto-scaling not illustrated here in this exercise

10) DevOps/CI hook ups to say CircleCI or Jenkins are not done here

11) Faster iterative dev framework: expressJS or Meteor



