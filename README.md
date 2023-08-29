Docs can be accessed at https://britanncaflask.pythonanywhere.com/

                        BOOKS
GET ALL BOOKS (GET)
--------------
                https://britanncaflask.pythonanywhere.com/api/books

GET SPECIFIC BOOK (GET)
------------------
                https://britanncaflask.pythonanywhere.com/api/books/{id}


CREATE NEW BOOK (POST)
---------------
                https://britanncaflask.pythonanywhere.com/api/books


payload (Example Value)

{
  "title": "string",
  "user_id": 0,
  "locccn": 0
}
----------------------

UPDATE A BOOK
-------------
HTTP METHOD--> PUT
ENDPOINT--
https://britanncaflask.pythonanywhere.com/api/books/{id}
---------------------------------------------------------

payload (Example value)

{
  "title": "string",
  "user_id": 0,
  "locccn": 0
}
--------------------

DELETE A BOOK
-------------
                https://britanncaflask.pythonanywhere.com/api/books/{id}

                        USERS
                    -------------
GET ALL USERS (GET)
--------------
                https://britanncaflask.pythonanywhere.com/api/users

GET SPECIFIC USER (GET)
-----------------
                https://britanncaflask.pythonanywhere.com/api/users{id}

CREATE NEW USER (POST)
---------------
                https://britanncaflask.pythonanywhere.com/api/users

payload (Example Value)

{
  "username": "string"
}
---------------------

UPDATE A USER
-------------
HTTP METHOD--> PUT
ENDPOINT--
https://britanncaflask.pythonanywhere.com/api/users/{id}
---------------------------------------------------------

payload (Example value)

{
  "username": "string"
}
----------------------

DELETE A USER (DELETE)
-------------
                https://britanncaflask.pythonanywhere.com/api/users/{id}
