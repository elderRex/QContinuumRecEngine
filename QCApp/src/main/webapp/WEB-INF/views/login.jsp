<%@taglib prefix="c" uri="http://java.sun.com/jsp/jstl/core"%>
<html>
<head>
</head>
<body>
	<form method="post" action="<c:url value='/j_spring_security_check' />">
		<div >
			<div >
	  			<div >
	    				Email: <input type="email" name="email" placeholder="Enter email">
	  			</div>
	  			<div>
	    				<input type="password" name="password" id="inputPassword" placeholder="Password">
	  			</div>
	  		</div>
  			<div>
  				<button type="submit"  value="Login">Sign In</button>
  			</div>
  			<div >
	    			<label>
	      			<a ng-href="{{pathingService.getCurrentPath('/accounts/forgot-password/')}}">Forgot Password?</a>
	    			</label>
	    			<span >
	  			${messageIncorrectPassword}
	  			</span>
    			</div>
  		</div>
</form>
</body>
</html>