<%@taglib prefix="c" uri="http://java.sun.com/jsp/jstl/core"%>
<html>
<head>
</head>
<body>
	<form method="post" class="form-inline" style="margin-bottom: 0px" action="<c:url value='/j_spring_security_check' />">
		<div class="container text-right">
			<div class="col-xs-8">
	  			<div class="col-xs-9">
	    				Email: <input type="email" class="form-control" name="email" placeholder="Enter email" style="width: 125px; height: 25px">
	  			</div>
	  			<div class="col-xs-3">
	    				<input type="password" name="password" class="form-control" id="exampleInputPassword3" placeholder="Password" style="width: 87px; height: 25px">
	  			</div>
	  		</div>
  			<div class="col-xs-1">
  				<button type="submit" class="btn background-olive-green" value="Login" style="height: 25px; width: 50px; padding: 1px; font-size: 12px;">Sign In</button>
  			</div>
  			<div class="col-xs-3">
	    			<label>
	      			<a style="color: #63AB62" ng-href="{{pathingService.getCurrentPath('/accounts/forgot-password/')}}">Forgot Password?</a>
	    			</label>
	    			<span class="fnt-red lft-twenty">
	  			${messageIncorrectPassword}
	  			</span>
    			</div>
  		</div>
</form>
</body>
</html>