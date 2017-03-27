<%@taglib prefix="c" uri="http://java.sun.com/jsp/jstl/core"%>>
<title>Registration</title>
	<form >
		    <div>
		    		<div>
			    		<span>
			    			<input type="text" name="firstname" id="inputFirst" ng-model="registration.selectedUsername" placeholder="Select your own username" autofocus />
			    		</span>
		    		</div>
		    </div>
		    <div>
	  			<div >
			    		<label for="inputEmail">First name</label>
			    		<input type="text" name="firstname" id="inputFirst" ng-model="registration.firstname" placeholder="First name" required autofocus />
		    		</div>
			    	<div >	
			    		<label for="inputEmail">Last name</label>
			    		<input type="text" name="lastname" id="inputLast" ng-model="registration.lastname" placeholder="Last name" required autofocus />
			    	</div>
	    		</div>
	    <div >
		    	<label for="inputEmail">Email address</label>
		    	<input type="email" id="inputEmail" name="email" ng-model="registration.email" placeholder="Email address" required autofocus>
	    </div>
	    <div >
		    	<label for="inputPassword" >Password</label>
		    	<input type="password" id="inputPassword" name="password" ng-model="registration.password" placeholder="Password" required>
	    </div>
	    	<button ng-click="register_user()">Get Started</button>
	</form>