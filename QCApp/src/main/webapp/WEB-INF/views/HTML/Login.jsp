<%@taglib prefix="c" uri="http://java.sun.com/jsp/jstl/core"%>
<!DOCTYPE html>
<html lang="en">
  <head>
    <meta charset="utf-8">
    <meta http-equiv="X-UA-Compatible" content="IE=edge">
    <meta name="viewport" content="width=device-width, initial-scale=1">
    <!-- The above 3 meta tags *must* come first in the head; any other head content must come *after* these tags -->
    <title>Login</title>

    <script type = "text/javascript" src="http://code.jquery.com/jquery-latest.min.js"> </script>


    <!-- Bootstrap -->
    <link href="css/bootstrap.min.css" rel="stylesheet">

    <!-- HTML5 shim and Respond.js for IE8 support of HTML5 elements and media queries -->
    <!-- WARNING: Respond.js doesn't work if you view the page via file:// -->
    <!--[if lt IE 9]>
      <script src="https://oss.maxcdn.com/html5shiv/3.7.3/html5shiv.min.js"></script>
      <script src="https://oss.maxcdn.com/respond/1.4.2/respond.min.js"></script>
    <![endif]-->

    <style type ="text/css">
    body {
        background-color:#6495ED;
        height: 100%;
        width:100%;
    }

    .container{
        background-color:white;
        width:90%;
        height:500px;
        border:2px black solid;
        margin-top:10px;
        margin-left:50px;
    }

    #toprow{
        text-align:center;
        font-size:200%;
        font-family: "Comic Sans MS", cursive, sans-serif;

    }
    .bold{
        font-weight:bold;
    }

    .center{
        text-align:center;
    }

    .comic{
        font-size:100%;
        font-family: "Comic Sans MS", cursive, sans-serif;
    }

    .inputbox {
    border: 2.5px solid #456879;
    border-radius:10px;
    height: 22px;
    width: 230px;
}

    .topmargin{
        margin-top:50px;
    }



    .fsSubmit{
        padding: 10px 15px 11px !important;
        font-size: 18px !important;
        background-color: #9EB9D4;
        font-weight: bold;
        text-shadow: 1px 1px #9EB9D4    ;
        color: #ffffff;
        border-radius: 5px;
        border: 1px solid #9EB9D4;
        cursor: pointer;
        box-shadow: 0 1px 0 rgba(255, 255, 255, 0.5) inset;
    }   


    </style>
    </head>

  <body>
    <div class = "container">
        <div class = "row">
            <div class = "col-md-4 col-md-offset-2">
            <h1 id="toprow"> Welcome back! Please log in :D </h1>

            <form class="center">
            <ul style="list-style-type: none;">
            

                <li class="topmargin comic">Username : <input type="text" placeholder= "Username / Email..." class="inputbox"/> </li>
                <li class="topmargin comic">Password :  <input type="password" placeholder= "Password...   " class="inputbox"/> </li>
            </ul>
                <input type="submit" value=" Continue" class = "fsSubmit topmargin"/> 
            </form> 
 


        </div>
            
    </div>

    <!-- jQuery (necessary for Bootstrap's JavaScript plugins) -->
    <script src="https://ajax.googleapis.com/ajax/libs/jquery/1.12.4/jquery.min.js"></script>
    <!-- Include all compiled plugins (below), or include individual files as needed -->
    <script src="js/bootstrap.min.js"></script>
  </body>
</html>

