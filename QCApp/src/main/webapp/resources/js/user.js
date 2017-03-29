var app = angular.module('user', ['pathing_controller']);

app.controller('userController', ['$scope', '$http','$location','pathingService', function($scope, $http, $location,pathingService) {	

	$scope.user_answers = {};
	
	// Submit Comment Responses
	$scope.submit_questions = function() {

		
	}
	
	
	
}]);