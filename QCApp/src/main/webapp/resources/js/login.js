var app = angular.module('home', ['pathing_controller']);

app.controller('homeController', ['$scope', '$http','$location','pathingService', function($scope, $http, $location,pathingService) {	

	$scope.data = {};

	$scope.load = function()
	{
		var url = pathingService.getCurrentPath("/get_all_user_data");
		$http.get(url).then(function(response){
			
			$scope.data = response;
		});
	}
	
}]);