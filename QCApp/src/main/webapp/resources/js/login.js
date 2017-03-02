var app = angular.module("home", []);

app.controller("homeController", function($scope, $http){
	$scope.load = function(){
		$http.get("/").then(function(response){
			$scope.welcome = response.data;
		})
	}
})