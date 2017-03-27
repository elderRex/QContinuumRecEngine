var app = angular.module('account', ['pathing_controller']);

app.controller('accountController', ['$scope', '$http','$location','pathingService', function($scope, $http, $location,pathingService) {
	$scope.load = function()
	{
		var url = pathingService.getCurrentPath("/get_account_info");
		$http.get(url).then(function(response){
			$scope.profile_pic = response.data['profile_pic']
			$scope.history = response.data['history']
		});
	}
}]);