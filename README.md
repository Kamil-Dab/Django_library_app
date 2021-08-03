# Django_library_app
How to run app: 
* Click in this link: https://djalib.herokuapp.com/
##Django_library_app has:
* home page
* books tab - contain table with every book in database, this view allows searching books by title, author , from/ to date ora language. Table is read-only.
* add books tab - allows adding, deleting or editing books. Table is the same as in previous view, but here each of records have edit and delete button. When edit button is hitted, you will be directed to the form which allows you to insert new data about chosen book.
* import books tab - allows importing books from https://developers.google.com/books/docs/v1/using#WorkingVolumes. You have to insert keyword and click import button. You will see messages about imported books (if they were imported correctly or if there were some problems).
* REST Api tab - this is list in json with every book and allows searching/filtering books by query sting. That view does not have front end view. If you want to filter books by querystring, you have to add querystring to url in browser search window. If querystring is valid, you will see list of books in json filtered by given criteria.

Edit form has validation rules - if user will pass invalid data, there will be message shown which field is invalid.
