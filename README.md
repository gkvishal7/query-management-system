
# QUERY MANAGEMENT SYSTEM
Users can register themselves for sending queries. 
Users can raise a particular query to Management. 
The Admin from the management has access to all the queries raised by differnet users.An acknowledgment mail is sent when admin accepts the query.

This application being open source can be forked and built upon for various applications.

## Authors

- [@Vishwanath](https://github.com/vishwanath-29)
- [@Karthickeyan](https://github.com/karthickeyan03)
- [@Vishal](https://github.com/gkvishal7)


## Installation

Clone the repository 
```bash
  git clone https://github.com/vishwanath-29/query-management-system
```

Go into the directory and install the requirements
```bash
  cd query-management-system
  pip install -r requirements.txt
```
Edit the query_management_system/setting.py with your preferred Database and migrate
```bash
  python3 manage.py makemigrations
  python3 manage.py migrate
```
Run the development server for testing
```bash
  python3 manage.py runserver
```
To create a superuser 
```bash
  python3 manage.py createsuperuser
```
## License

[MIT](https://choosealicense.com/licenses/mit/)


## Features

- Send Acknowledgement Mail
- Managing Queries
- See query history
- Create staff from Django Admin Page


## Deployment

To deploy this project, clone this repository and make changes in the settings.py file

Our Deployment - https://querymanagementsystem.azurewebsites.net/ (Not yet Fully Depolyed)

For reference - https://docs.djangoproject.com/en/4.1/howto/deployment/ 



## Open Source Technologies Used

- Bootstrap : https://getbootstrap.com/docs/5.2/getting-started/introduction/
- Django : https://docs.djangoproject.com/en/4.1/
- PostgreSql : https://www.postgresql.org/docs/current/index.html


## Github Student Developer Tools
- Mailgun : Send Email through their powerful ecosystem
- Pycharm : For easier python development
- Name.com : To get free Domain
- Microsoft Azure : For Database-as-a-service and Platform-as-as-service for applicaion deployment

## Feedback

If you have any feedback, please reach out to us at 
- vishwanathnarayanan29@gmail.com
- karthiksithan007@gmail.com
- gkvishal7@gmail.com


## Screenshots

![App Screenshot](https://via.placeholder.com/468x300?text=App+Screenshot+Here)

