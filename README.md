Docs can be accessed at https://britanncaflask.pythonanywhere.com/

                    BOOKS
                -------------
GET ALL BOOKS
--------------
HTTP METHOD--> GET
ENDPOINT--
https://britanncaflask.pythonanywhere.com/api/books
---------------------------------------------------

CREATE NEW BOOK
---------------
HTTP METHOD--> POST
ENDPOINT--
https://britanncaflask.pythonanywhere.com/api/books
---------------------------------------------------

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
HTTP METHOD--> DELETE 
ENDPOINT--
https://britanncaflask.pythonanywhere.com/api/books/{id}
--------------------------------------------------------

                    USERS
                -------------
GET ALL USERS
--------------
HTTP METHOD--> GET
ENDPOINT--
                https://britanncaflask.pythonanywhere.com/api/users
---------------------------------------------------

GET SPECIFIC USER
-----------------
HTTP METHOD--> GET
ENDPOINT--
https://britanncaflask.pythonanywhere.com/api/users{id}
-------------------------------------------------------

CREATE NEW USER
---------------
HTTP METHOD--> POST
ENDPOINT--
https://britanncaflask.pythonanywhere.com/api/users
---------------------------------------------------        

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

DELETE A USER
-------------
HTTP METHOD--> DELETE 
ENDPOINT--
https://britanncaflask.pythonanywhere.com/api/users/{id}
--------------------------------------------------------
