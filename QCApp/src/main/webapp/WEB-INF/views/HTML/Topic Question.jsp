<%@taglib prefix="c" uri="http://java.sun.com/jsp/jstl/core"%>
<!DOCTYPE html>
<html lang="en">
  <head>
    <meta charset="utf-8">
    <meta http-equiv="X-UA-Compatible" content="IE=edge">
    <meta name="viewport" content="width=device-width, initial-scale=1">
    <!-- The above 3 meta tags *must* come first in the head; any other head content must come *after* these tags -->
    <title>Topic Question</title>

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
        height:120px;
        border:2px black solid;
        margin-top:10px;
        margin-left:50px;
    }

    #toprow{
        text-align:center;
        font-size:200%;
        font-family: "Comic Sans MS", cursive, sans-serif;

    }

    .qcontainer{
        background-color:#6699CC;
        width:90%;
        height:400px;
        border:2px black solid;
        margin-top:10px;
        margin-left:50px;

    }

    .smallcontainer{
        background-color:white;
        width:90%;
        height:250px;
        line-height: 3em;
        overflow: auto;
        padding:5px;
        border:2px black solid;
        margin-top:10px;
        margin-left:50px;
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
        font-size:100%;
    }

    .padding{
        padding-left: 30px;
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
        margin-top:-20px;
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
            <h1 id="toprow"> One More Step -- Please answer the following question so that we could recommend good stuff for you! </h1>
        </div>
            
    </div>

    <div class = "qcontainer">
        <div class = "row">
            <div class = "col-md-4 col-md-offset-2">
            <h1 class="comic padding"> Questions of Topic </h1>
            <div class = "smallcontainer">
                <form class="comic font">
                    <ul style = "list-style-type: none;">
                        <li> Q1: XXXXXXXXXXXXXXXXXXXXXXX </li>
                        <li class="menumargin center"> Rating: Dislike 
                        <input type = "radio" name= "one" /> 1 
                        <input type = "radio" name= "one" /> 2
                        <input type = "radio" name= "one" /> 3
                        <input type = "radio" name= "one" /> 4
                        <input type = "radio" name= "one" /> 5
                        Like
                        </li>

                        <li> Q2: XXXXXXXXXXXXXXXXXXXXXXX </li>
                        <li class="menumargin center"> Rating: Dislike 
                        <input type = "radio" name= "one" /> 1 
                        <input type = "radio" name= "one" /> 2
                        <input type = "radio" name= "one" /> 3
                        <input type = "radio" name= "one" /> 4
                        <input type = "radio" name= "one" /> 5
                        Like
                        </li>

                        <li> Q3: XXXXXXXXXXXXXXXXXXXXXXX </li>
                        <li class="menumargin center"> Rating: Dislike 
                        <input type = "radio" name= "one" /> 1 
                        <input type = "radio" name= "one" /> 2
                        <input type = "radio" name= "one" /> 3
                        <input type = "radio" name= "one" /> 4
                        <input type = "radio" name= "one" /> 5
                        Like
                        </li>

                        <li> Q4: XXXXXXXXXXXXXXXXXXXXXXX </li>
                        <li class="menumargin center"> Rating: Dislike 
                        <input type = "radio" name= "one" /> 1 
                        <input type = "radio" name= "one" /> 2
                        <input type = "radio" name= "one" /> 3
                        <input type = "radio" name= "one" /> 4
                        <input type = "radio" name= "one" /> 5
                        Like
                        </li>

                        <li> Q5: XXXXXXXXXXXXXXXXXXXXXXX </li>
                        <li class="menumargin center"> Rating: Dislike 
                        <input type = "radio" name= "one" /> 1 
                        <input type = "radio" name= "one" /> 2
                        <input type = "radio" name= "one" /> 3
                        <input type = "radio" name= "one" /> 4
                        <input type = "radio" name= "one" /> 5
                        Like
                        </li>

                    </ul>
                </form>

            </div>
        </div>
            
    </div>

    

    <form class="center">
                <input type="submit" value="Done" class = "fsSubmit topmargin"/> 
    </form> 

    <!-- jQuery (necessary for Bootstrap's JavaScript plugins) -->
    <script src="https://ajax.googleapis.com/ajax/libs/jquery/1.12.4/jquery.min.js"></script>
    <!-- Include all compiled plugins (below), or include individual files as needed -->
    <script src="js/bootstrap.min.js"></script>
  </body>
</html>

