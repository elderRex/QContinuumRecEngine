<%@taglib prefix="c" uri="http://java.sun.com/jsp/jstl/core"%>
<!DOCTYPE html>
<html lang="en">
  <head>
    <meta charset="utf-8">
    <meta http-equiv="X-UA-Compatible" content="IE=edge">
    <meta name="viewport" content="width=device-width, initial-scale=1">
    <!-- The above 3 meta tags *must* come first in the head; any other head content must come *after* these tags -->
    <title>Welcome Page</title>

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
    }

    .titlebox{
        background-color:white;
        text-align: center;
        width:98%;
        height:70px;
        border:2px black solid;
        margin-left:3px;
    
    }

    .title {
        font-size:300%;
        font-weight:bold;
        color:black;
        font-family: "Comic Sans MS", cursive, sans-serif;
        margin-top:-2px;

    }

    .picture{
        background-color:white;
        border:2px black solid;
        width:50%;
        height:400px;
        margin: 0 auto;
    }

    .buttonbox{
        background-color:white;
        width:90%;
        height:100%;
        border:2px black solid;
        margin-top:10px;
        margin-left:50px;
    }

    #toprow{
        text-align:center;
        font-family: "Comic Sans MS", cursive, sans-serif;

    }
    .bold{
        font-weight:bold;
    }

    .center{
        text-align:center;
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
        margin-bottom:5px;
    }   

    #signup{
        margin-top: 400px;
        margin-left: 220px;
    }

    #login{
        margin-left: 60px;
    }

    #facebook{
        margin-top:10px;
        margin-left:230px;
        margin-bottom:10px;
    }

    .margin{
        margin-top:10px;
        margin-bottom:10px;
    }




    </style>
    </head>

  <body>
    <div class="titlebox" class="col-md-6">
        <h1 class="title"> Next-Gen Reccomendation :D </h1>
    </div>

    <div class = "buttonbox" >
        <div class = "row">
            <div class = "col-md-6 col-md-offset-3">
            <h1 id="toprow"> Welcome to our fantastic recommendation search engine! </h1>

            <div class="picture center">
            </div>

            <div class= "col-md-6 col-md-offset-3 margin">
            <form class="center">

                <input type="submit" value="    Login   " class = "fsSubmit"/> 

                <input type="submit" value="Facebook Login" class = "fsSubmit"/> 

            </form> 

            <h3 class="bold center"> Not a member yet? Click the Sign up bottom for now!</h3>

            <form class="center">

                <input type="submit" value=" Sign up " class = "fsSubmit"/> 

            </form>  
            </div>


        </div>
            
    </div>

    <!-- jQuery (necessary for Bootstrap's JavaScript plugins) -->
    <script src="https://ajax.googleapis.com/ajax/libs/jquery/1.12.4/jquery.min.js"></script>
    <!-- Include all compiled plugins (below), or include individual files as needed -->
    <script src="js/bootstrap.min.js"></script>

    <script>

    //$(".buttonbox").css("height",$(window).height());

    </script>
  </body>
</html>

