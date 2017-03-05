<%@taglib prefix="c" uri="http://java.sun.com/jsp/jstl/core"%>
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
			    		<input type="text" name="firstname" id="inputFirst" class="form-control" ng-model="registration.firstname" placeholder="First name" required autofocus />
		    		</div>
			    	<div >	
			    		<label for="inputEmail">Last name</label>
			    		<input type="text" name="lastname" id="inputLast" class="form-control" ng-model="registration.lastname" placeholder="Last name" required autofocus />
			    	</div>
	    		</div>
	    <div >
		    	<label for="inputEmail" class="sr-only">Email address</label>
		    	<input type="email" id="inputEmail" name="email" class="form-control" ng-model="registration.email" placeholder="Email address" required autofocus>
	    </div>
	    <div >
		    	<label for="inputPassword" class="sr-only">Password</label>
		    	<input type="password" id="inputPassword" name="password" ng-model="registration.password" class="form-control" placeholder="Password" required>
	    </div>
	    	<button class="orange form-control" ng-click="register_user()">Get Started</button>
	</form>