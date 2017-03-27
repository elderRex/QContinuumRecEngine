<%@taglib prefix="c" uri="http://java.sun.com/jsp/jstl/core"%>

<html>
<body ng-app="account" ng-controller="accountController" ng-init="load()">
	<jsp:include page="./partials/header.jsp"/>
	<div id="pic">
		<img src="{{profile_pic}}">
		<p>My Interests</p>
		<button>Recommend GO!</button>
	</div>
	<div>
		<p>Past Activities</p>
		<div ng-repeat='x in history'>{{x}}</div>
	</div>
</body>
</html>