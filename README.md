[SWAGGER DOCUMENTATION](https://britanncaflask.pythonanywhere.com/)

# BOOKS

### GET ALL BOOKS (GET)

                https://britanncaflask.pythonanywhere.com/api/books

### GET SPECIFIC BOOK (GET)
                https://britanncaflask.pythonanywhere.com/api/books/{id}


### CREATE NEW BOOK (POST)
                https://britanncaflask.pythonanywhere.com/api/books


*payload (Example Value)*
```js
{
  "title": "string",
  "user_id": 0,
  "locccn": 0
}
```

### UPDATE A BOOK (PUT)
                https://britanncaflask.pythonanywhere.com/api/books/{id}

*payload (Example value)*
```js
{
  "title": "string",
  "user_id": 0,
  "locccn": 0
}
```
### DELETE A BOOK
                https://britanncaflask.pythonanywhere.com/api/books/{id}

# USERS
### GET ALL USERS (GET)
                https://britanncaflask.pythonanywhere.com/api/users

### GET SPECIFIC USER (GET)
                https://britanncaflask.pythonanywhere.com/api/users{id}

### CREATE NEW USER (POST)
                https://britanncaflask.pythonanywhere.com/api/users


*payload (Example Value)*
```js
{
  "username": "string"
}
```

### UPDATE A USER (PUT)
            https://britanncaflask.pythonanywhere.com/api/users/{id}

*payload (Example value)*
```js
{
  "username": "string"
}
```

### DELETE A USER (DELETE)
                https://britanncaflask.pythonanywhere.com/api/users/{id}
