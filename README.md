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

\n
payload (Example Value)

{
  "title": "string",
  "user_id": 0,
  "locccn": 0
}

UPDATE A BOOK (PUT)
-------------
                https://britanncaflask.pythonanywhere.com/api/books/{id}
\n
payload (Example value)

{
  "title": "string",
  "user_id": 0,
  "locccn": 0
}

DELETE A BOOK
-------------
                https://britanncaflask.pythonanywhere.com/api/books/{id}

                        \nUSERS
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

\n
payload (Example Value)

{
  "username": "string"
}

UPDATE A USER (PUT)
-------------
            https://britanncaflask.pythonanywhere.com/api/users/{id}
\n
payload (Example value)

{
  "username": "string"
}

DELETE A USER (DELETE)
-------------
                https://britanncaflask.pythonanywhere.com/api/users/{id}
