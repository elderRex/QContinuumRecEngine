<%@taglib prefix="c" uri="http://java.sun.com/jsp/jstl/core"%>
<!DOCTYPE html>
<html lang="en">
  <head>
    <meta charset="utf-8">
    <meta http-equiv="X-UA-Compatible" content="IE=edge">
    <meta name="viewport" content="width=device-width, initial-scale=1">
    <!-- The above 3 meta tags *must* come first in the head; any other head content must come *after* these tags -->
    <title>Recommendation Detail Page</title>

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
        height:100%;
        border:2px black solid;
        margin-top:10px;
        margin-left:50px;
    }

    .reviewcontent{
        background-color:#6699CC;
        width: 99%;
        height: 100%;
        border:2px black solid;
        margin-top:5px;
        margin-left:3px;
        margin-bottom:2px;
    }

    #toprow{
        text-align:left;
        padding-left:10px;
        font-size:200%;
        font-family: "Comic Sans MS", cursive, sans-serif;
    }

    .secondcontainer{
        background-color:#6699CC;
        width:99%;
        height:140px;
        border:2px black solid;
        margin-top:10px;
        margin-left:3px;
        margin-bottom:3px;

    }

    .photo{
        background-color:white;
        width:15%;
        height:120px;
        border:2px black solid;
        margin-top:10px;
        margin-left:90px;
        margin-bottom:3px;

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



    .content{
        margin-left:50px;
        background-color:#6699CC;
        width:30%;
        height:120px;
        margin-top:10px;
        margin-right:10px;
        overflow: auto;
    }

    .scontent{
        background-color:white;
        width:98%;
        height:140px;
        border:2px black solid;
        margin-top:10px;
        margin-left:10px;
        margin-right:10px;

    }

    .aphoto{
        background-color:white;
        width: 15%;
        height:120px;
        border:2px black solid;
        margin-top:10px;
        margin-left:10px;

    }

    .rating{
        width:15%;
        height:140px;
        margin-left:10px;
        margin-right:45px;
    }

    .topmargin{
        margin-top:20px;
    }

    .menumargin{
        margin-top:-6px;
    }

    .rightmargin{
        margin-right:100px;
    }

    .leftmargin{
        margin-left:100px;
    }

    .floatl{
        float:left;
    }

    .floatr{
        float:right;
    }

    #buttonmargin{
        margin-top:30px;
        margin-right:25px;
    }

    #comment{
        margin-left:50px;
        margin-top:50px;
    }

    .scomment{
        margin-left:50px;
        background-color:white;
        width:63%;
        height:120px;
        margin-top:10px;
        margin-right:10px;
        overflow: auto;
    }

    .check{
        background-color: white;
        border: 2px solid black;
        -ms-transform: scale(4); /* IE */
        -moz-transform: scale(4); /* FF */
        -webkit-transform: scale(4); /* Safari and Chrome */
        -o-transform: scale(4); /* Opera */
        padding: 10px;
        margin-left:60px;
        margin-top:60px;
        margin-right:20px;
        float:left;

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

    .rating-bar{
        background:black;
        padding:3px;
    }

    .rating-bar span{
        display:block;
        height:15px;
    }
    .rating-bar, .rating-bar span {
        border-radius:4px; 
    }

    .rate-8{ width:80%; }

    .animate{
        animation: progress 2s linear;
        -moz-animation: progress 2s linear;
        -webkit-animation: progress 2s linear;
        -ms-animation: progress 2s linear;
        -o-animation: progress 2s linear;
    }

    .blue{
        background:#4169e1;
    }



    </style>
    </head>

  <body>
  <div>
  <form class="topmargin center">
        <input type="submit" value=" <     Home  " class = "fsSubmit rightmargin"/> 

        <select class="selection rightmargin">
            <option> Looking for {topic} </option>
            <option> 1 </option>
            <option> 2 </option>
            <option> 3 </option>
            <option> 4 </option>
            <option> 5 </option>
            <option> 6 </option>
        </select>

        <input type="submit" value="       Hit me !      " class = "fsSubmit leftmargin"/> 
    </form>
    </div>

    <div class = "container">
        <div class = "row">
            <div class = "col-md-4 col-md-offset-2">
            <h1 id="toprow"> Display Result of Recommendation </h1>
            </div>

            <div class = "col-md-4 col-md-offset-2 secondcontainer">
                <form>
                <input type="checkbox" class="check"/>
                </form>
                <div class= "col-md-4 col-md-offset-2 photo floatl">
                </div>

                <div class="col-md-4 col-md-offset-2 content floatl">
                    <h2 class="comic ifont"> a short description: </h2>
                    <h3> test</h3>
                    <h3> test</h3>
                    <h3> test</h3>
                    <h3> test</h3>
                </div>
                <div class="rating floatl">
                    <h4 class="comic ifont">Rating: </h4>
                    <div class="rating-bar">
                    <div class="rate-8">
                    <span class="animate blue"></span>
                    </div>
                    </div>
                </div>

                <div class="floatr">
                    <form id="buttonmargin">
                    <input type="submit" value="  Expand  " class = "fsSubmit topmargin"/> 
                    </form>
                </div>
            </div>

            <div class = "col-md-4 col-md-offset-2 reviewcontent">
            <h1 class="comic font padding"> Find out what others think! </h1>
                <div class= "col-md-4 col-md-offset-2 scontent">
                    <div class= "col-md-4 col-md-offset-2 aphoto floatl" >
                    </div>
                    <h2 class="comic titlefont floatl topmargin" id="comment"> Comments: </h2>
                    <div class="col-md-4 col-md-offset-2 scomment floatl">
                    <h3> test</h3>
                    <h3> test</h3>
                    <h3> test</h3>
                    <h3> test</h3>
                    </div>
                </div>

                <div class= "col-md-4 col-md-offset-2 scontent">
                    <div class= "col-md-4 col-md-offset-2 aphoto floatl" >
                    </div>
                    <h2 class="comic titlefont floatl topmargin" id="comment"> Comments: </h2>
                    <div class="col-md-4 col-md-offset-2 scomment floatl">
                    <h3> test</h3>
                    <h3> test</h3>
                    <h3> test</h3>
                    <h3> test</h3>
                    </div>
                </div>

                <div class= "col-md-4 col-md-offset-2 scontent">
                    <div class= "col-md-4 col-md-offset-2 aphoto floatl" >
                    </div>
                    <h2 class="comic titlefont floatl topmargin" id="comment"> Comments: </h2>
                    <div class="col-md-4 col-md-offset-2 scomment floatl">
                    <h3> test</h3>
                    <h3> test</h3>
                    <h3> test</h3>
                    <h3> test</h3>
                    </div>
                </div>
            </div>


        

        
    
    </div>
    </div>

    

        
    <!-- jQuery (necessary for Bootstrap's JavaScript plugins) -->
    <script src="https://ajax.googleapis.com/ajax/libs/jquery/1.12.4/jquery.min.js"></script>
    <!-- Include all compiled plugins (below), or include individual files as needed -->
    <script src="js/bootstrap.min.js"></script>
  </body>
</html>
