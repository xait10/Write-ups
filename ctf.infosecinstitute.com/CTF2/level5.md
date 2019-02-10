If look into the code may find this string

`<a class="btn btn-sm btn-info" disabled="" href="login.html">login</a>`

if try activate button

`<a class="btn btn-sm btn-info" enabled="" href="login.html">login</a>`

it will gives no result. So, try to referrer from login page

> curl --header "Referer: http://ctf.infosecinstitute.com/ctf2/exercises/login.html" http://ctf.infosecinstitute.com/ctf2/exercises/ex5.php
