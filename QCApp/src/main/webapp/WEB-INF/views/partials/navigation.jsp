<%@taglib prefix="c" uri="http://java.sun.com/jsp/jstl/core"%>
<%@ taglib uri="http://www.springframework.org/security/tags" prefix="security" %>
<nav id="main-nav" class="navbar-fixed-top">
	<div>
		<div class="col-xs-1">
			QCApp
		</div>
		<div class="col-xs-1"></div>
		<div class="col-xs-8">
		</div>
		<div class="col-xs-2">
			<ul>
				<li>
					<security:authorize access="hasRole('ROLE_USER')">
		   				<a href="<c:url value="/logout" />" >
							Logout
						</a>
					</security:authorize>
				</li>
			</ul>
		</div>				
  	</div>
</nav>