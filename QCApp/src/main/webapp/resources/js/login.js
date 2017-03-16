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
	
	$scope.logout_user = function()
	{
		window.location.href = pathingService.getCurrentPath("/logout");
	}
	
	// Register New User (Customer) (Just Email)
	$scope.register_user = function() {
		if ($scope.registration 
				&& ($scope.registration.selectedUsername)
				&& $scope.registration.firstname
				&& $scope.registration.lastname
				&& $scope.registration.email
				&& $scope.registration.password)
		{
			$http.post(pathingService.getCurrentPath('/new-user/register'), $scope.registration).then(function(data) {
					debugger;
				window.location.href = pathingService.getCurrentPath('setup');
			}, function errorCallback(response) {
				// TODO Error on callback
			  });
		}
		else
		{
			//$( "#warning-more-information" ).dialog( "open" );
		}
	}
	
}]);