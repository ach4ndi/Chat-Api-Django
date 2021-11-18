Before running this test application, should know what stack and tools is being used :

- Python 3.7.12 x64 windows
- Django 3.2.6
- Django Rest Framework 3.12.4
- Django Knox 4.1.0
- VSCodium/VSCode
- Notepad
- Markdown Monster
- SourceTree

## Prepare 

1. Python (and Pip Python package installer) is already installed on your system. Make sure python version is on around 3.7.x for avoid compatibility.
2. Create virtual environment, you can see <a href="https://virtualenvwrapper.readthedocs.io/en/latest/install.html#basic-installation" target="_blank">[on here]</a> for detail about installation and how to use. 
    a. After virtual environment for your OS is already installed, you can create one VE for this application to operate :

        ```bash
            mkvirtualenv test-rakamin
        ```

    b. then you can active VE :
        
        ```bash
            workon test-rakamin
        ```

3. After prepare virtual enviroment, install some python module using pip for application to run :
    ```bash
        pip install -r requirements.txt
    ```

4. If you want using new database file, you can remove sqlite database is already on repository, and execute :
    ```bash
    python manage.py migrate
    ```
5. You can create super user account on django commandline for access admin web panel django provide, but you can also create user via register endpoint.
    ```bash
    python manage.py createsuperuser --email admin@example.com --username admin
    ```
6. After that you can running the application server.
     ```bash
    python manage.py runserver
     ```
    * url for access :
        ```bash
        http://127.0.0.1:8000/admin
        ```
        you can see all endpoint on postman collection file.

## Application

Simple chat api app for recruitment process.

1. user can send a message to another user.
2. user can list all message in a conversation between them and another user.
3. user can reply to a conversation they are involved.
4. user can list all their conversations (if user A has been chatting with user C & D, the list for A it will shows A-C and A-D)

## API Usage

You can test some api endpoint on postman collection, you can found them on repository.

#### Register / Login User:

1. Users can register their account using endpoint:
    ```bash
    /api/register
    ```
2. After got respond about user profile and token, place token on authentication header with format "Token {token}".
3. After registration you can use that account on login api endpoint to get token for accessing other restricted endpoint. login endpoint:
    ```bash
    /api/login
    ```
4. you can access user profile `/api/user` and all user `app/users`

#### Send Message to User

1. Before send conservation to other user, you should create room between them. you can use this endpoint to create chat room first :
    ```bash
    /api/room/create
    ```
2. After chat room is created, you can send message using :
    ```bash
    /api/message/create
    ```
3. You can list all message on selected chat room, using :
    ```bash
    /api/message/list
    ```
4. You also can see all chat room is found on current user login :
    ```bash
    /api/room/
    ```

other information can be found on postman collection file.