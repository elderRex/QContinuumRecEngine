<%@taglib prefix="c" uri="http://java.sun.com/jsp/jstl/core"%>
<!DOCTYPE html>
<html lang="en">
  <head>
    <meta charset="utf-8">
    <meta http-equiv="X-UA-Compatible" content="IE=edge">
    <meta name="viewport" content="width=device-width, initial-scale=1">
    <!-- The above 3 meta tags *must* come first in the head; any other head content must come *after* these tags -->
    <title>Topic Selection</title>

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

    #note{
        text-align:center;
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

    .menumargin{
        margin-top:5px;
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

    .selection{
        -webkit-appearance: button;
        -webkit-border-radius: 2px;
        -webkit-box-shadow: 0px 1px 3px rgba(0, 0, 0, 0.1);
        -webkit-padding-end: 20px;
        -webkit-padding-start: 2px;
        -webkit-user-select: none;
        background-image: url(http://i62.tinypic.com/15xvbd5.png), -webkit-linear-gradient(#FAFAFA, #F4F4F4 40%, #E5E5E5);
        background-position: 97% center;
        background-repeat: no-repeat;
        border: 1px solid #AAA;
        color: #555;
        font-size: inherit;
        margin: 20px;
        overflow: hidden;
        padding: 5px 10px;
        text-overflow: ellipsis;
        white-space: nowrap;
        width: 300px;

    }


    </style>
    </head>

  <body>
    <div class = "container">
        <div class = "row">
            <div class = "col-md-4 col-md-offset-2">
            <h1 id="toprow"> Second step -- Please choose you topic of Interest! </h1>
            <h3 id="note"> Note: You will be asked about roughly 20 question for each topic you choose </h3>

        </div>
            
    </div>

    <form class="center topmargin">
        <select class="selection rightmargin">
            <option> Select an topic </option>option>
            <option> 1 </option>
            <option> 2 </option>
            <option> 3 </option>
            <option> 4 </option>
            <option> 5 </option>
            <option> 6 </option>
        </select>

        <select class="selection">
            <option> Select an topic </option>option>
            <option> 1 </option>
            <option> 2 </option>
            <option> 3 </option>
            <option> 4 </option>
            <option> 5 </option>
            <option> 6 </option>
        </select>
    </form>

     <form class="center menumargin">
        <select class="selection rightmargin">
            <option> Select an topic </option>option>
            <option> 1 </option>
            <option> 2 </option>
            <option> 3 </option>
            <option> 4 </option>
            <option> 5 </option>
            <option> 6 </option>
        </select>

        <select class="selection">
            <option> Select an topic </option>option>
            <option> 1 </option>
            <option> 2 </option>
            <option> 3 </option>
            <option> 4 </option>
            <option> 5 </option>
            <option> 6 </option>
        </select>
    </form>

     <form class="center menumargin">
        <select class="selection rightmargin">
            <option> Select an topic </option>option>
            <option> 1 </option>
            <option> 2 </option>
            <option> 3 </option>
            <option> 4 </option>
            <option> 5 </option>
            <option> 6 </option>
        </select>

        <select class="selection">
            <option> Select an topic </option>option>
            <option> 1 </option>
            <option> 2 </option>
            <option> 3 </option>
            <option> 4 </option>
            <option> 5 </option>
            <option> 6 </option>
        </select>
    </form>

    <form class="center">
                <input type="submit" value="Done" class = "fsSubmit topmargin"/> 
    </form> 

    <!-- jQuery (necessary for Bootstrap's JavaScript plugins) -->
    <script src="https://ajax.googleapis.com/ajax/libs/jquery/1.12.4/jquery.min.js"></script>
    <!-- Include all compiled plugins (below), or include individual files as needed -->
    <script src="js/bootstrap.min.js"></script>
  </body>
</html>

