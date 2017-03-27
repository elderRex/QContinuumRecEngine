<%@taglib prefix="c" uri="http://java.sun.com/jsp/jstl/core"%>
<!DOCTYPE html>
<html lang="en">
  <head>
    <meta charset="utf-8">
    <meta http-equiv="X-UA-Compatible" content="IE=edge">
    <meta name="viewport" content="width=device-width, initial-scale=1">
    <!-- The above 3 meta tags *must* come first in the head; any other head content must come *after* these tags -->
    <title>My Friends Page</title>

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

    ul li{
        display: inline;
    }

    .container{
        background-color:white;
        width:90%;
        height:50px;
        border:2px black solid;
        margin-top:10px;
        margin-left:50px;
    }

    #toprow{
        text-align:center;
        font-size:200%;
        font-family: "Comic Sans MS", cursive, sans-serif;

    }

    .secondcontainer{
        background-color:white;
        width:90%;
        height:100%;
        border:2px black solid;
        margin-top:10px;
        margin-left:50px;
        overflow: hidden;
    }

    .friendlist{
        float: left;
        width: 25%;
        height: 500px;
        background-color: white;
        border:2px black solid;
        margin-left:15px;
        margin-right:15px;
        margin-bottom: 10px;
        line-height: 3em;
        overflow: auto;
    }

    .detail{
        overflow: hidden;
        width: 70%;
        height: 500px;
        background-color: white;
        border:2px black solid;
        margin-top:10px;
        margin-bottom: 10px;
        line-height: 3em;
        overflow: auto;
    }


    .bold{
        font-weight:bold;
    }

    .center{
        text-align:center;
    }

    .comic{
        font-size:150%;
        font-family: "Comic Sans MS", cursive, sans-serif;
    }

    .font{
        font-size:110%;
    }

    .ifont{
        font-size:100%;
    }

    .titlefont{
        font-size:150%;
    }

    .padding{
        padding-left: 20px;
    }


    .inputbox {
    border: 2.5px solid #456879;
    border-radius:10px;
    height: 22px;
    width: 230px;
}

    .topmargin{
        margin-top:20px;
    }

    .menumargin{
        margin-top:-6px;
    }

    .rightmargin{
        margin-right:10px;
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
            <form class="comic font menumargin">
            <ul style = "list-style-type: none;">
                <li class="padding bold font rightmargin "> My Account </li>
                <li class="padding bold font rightmargin "> My Friends </li>
                <li class="padding bold font "> My Comments </li>
    
            </ul>
            </form>

            </div>
            
        </div>
    </div>

    <div class = "secondcontainer">
        <h1 class="comic bold titlefont padding"> My Friends </h1>
        <div class = "col-md-4 col-md-offset-2 friendlist">
            <h1> test </h1>
            <h1> test </h1>
            <h1> test </h1>
            <h1> test </h1>
            <h1> test </h1>
            <h1> test </h1>
            <h1> test </h1>
            <h1> test </h1>
        </div>
        <div class="detail">
            <h2 class="padding comic bold font menumargin"> Details of Friends </h2>
        </div>
    </div>

        
    <!-- jQuery (necessary for Bootstrap's JavaScript plugins) -->
    <script src="https://ajax.googleapis.com/ajax/libs/jquery/1.12.4/jquery.min.js"></script>
    <!-- Include all compiled plugins (below), or include individual files as needed -->
    <script src="js/bootstrap.min.js"></script>
  </body>
</html>

