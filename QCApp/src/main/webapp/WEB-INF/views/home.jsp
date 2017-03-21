<!DOCTYPE html PUBLIC "-//W3C//DTD HTML 4.01 Transitional//EN" "http://www.w3.org/TR/html4/loose.dtd">
<%@ taglib uri="http://java.sun.com/jsp/jstl/core" prefix="c" %>
<%@ page session="false" %>
<jsp:include page="./partials/universal.jsp"/>
<html>
<head>

	<title>QContinuum</title>
	<jsp:include page="./partials/universal.jsp"/>

</head>
<body ng-app="home" ng-controller="homeController" ng-init="load()">
	<h1>{{data}}</h1>
	<jsp:include page="create_account.jsp"/>
	<hr/>
	<hr/>
	<jsp:include page="login.jsp"/>
	<hr/>
	<hr/>
	<jsp:include page="profile.jsp"/>
</body>
</html>