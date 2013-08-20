print 'Content-Type: text/html; charset=UTF-8'
print ''

print '''

<html>

<head>

<style>

.tableStyle
{
	position: absolute;
	/* top: 50%; */
    left: 50%;
    width: 650px; /*              */
    height: 650px; /*              */
    /* margin-top: -325px; */ 
    margin-left: -325px; /*                                             ,                                                        */
}

.textStyle
{
	color: orange;
	font-family: 'Times New Roman', Times, serif; /*                  */ 
    font-size: 120%; /*                           */ 
}

.textareaStyle
{
	width: 100%;
	height: 100%;
 
	border-color: orange; /*              */ 
    border-style: solid; /*               */ 
 
	border-width: 1px;
}

.shadow
{
	/* http://htmlbook.ru/css/box-shadow */
	-moz-box-shadow:    0 0 10px rgba(0,0,0,0.5); /* Для Firefox */
	-webkit-box-shadow: 0 0 10px rgba(0,0,0,0.5); /* Для Safari и Chrome */
    box-shadow:         0 0 10px rgba(0,0,0,0.5); /* Параметры тени */
}

.langRow
{
	height: 6%;
}

.commentRow
{
	height: 6%;
}

.submitRow
{
	height: 6%;
}

.commentStyle
{
	width: 100%;
	height: 100%;
}

</style>

</head>

<body>

 <form action="submit" method="post">
 
  <table class="tableStyle">
 
  <tr class="langRow">
   <td>
    <select name="lang" class=shadow>
     <option>C++</option>
	 <option>Java</option>
	 <option>Python</option>
     <option>Other...</option>
    </select>
   </td>
  </tr>
 
  <tr class="commentRow">
   <td>
    <div class=textStyle>Comment:</div>
   </td>
  
   <td>
    <input class="textareaStyle shadow" type="text" name="comment"><br>
   </td>
  </tr>
 
  <tr>
   <td colspan="2">
    <textarea name="code" class="textareaStyle shadow"></textarea>
   </td>
  </tr>
  
  <tr class="submitRow">
   <td>
    <input type="submit" value="Submit">
   </td>
  </tr>
 
  </table>
 
  
 
 </form>
 
</body>

</html>

'''


