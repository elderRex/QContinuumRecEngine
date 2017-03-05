<!DOCTYPE html PUBLIC "-//W3C//DTD HTML 4.01 Transitional//EN" "http://www.w3.org/TR/html4/loose.dtd">
<%@ taglib uri="http://java.sun.com/jsp/jstl/core" prefix="c" %>
<%@ page session="false" %>
<html>
<head>

	<title>QContinuum</title>
	<script src="https://ajax.googleapis.com/ajax/libs/angularjs/1.4.8/angular.min.js"></script>
		<script type="text/javascript" src="<c:url value="/resources/js/pathing.js" />"> </script>
	<script type="text/javascript" src="<c:url value="/resources/js/login.js" />"> </script>

</head>
<body ng-app="home" ng-controller="homeController" ng-init="load()">
	<h1>{{data}}</h1>
 ACCOUNT SETUP
</body>
</html>