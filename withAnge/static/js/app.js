var my_app = angular.module("newEstimate", [ "ngSanitize", "ui.tinymce", "ngCookies"]);
my_app.config(function($httpProvider) {
    $httpProvider.defaults.headers.common['X-Requested-With'] = 'XMLHttpRequest';
});
my_app.controller("formHomeCtrl", function($scope, $location, $filter ,$http, $cookies ) {
	//Par défaut , on montre que la page d'accueil
	$scope.showHome = true;
	//ou si on retourne à la page d'acueil
	$scope.toShowHome = function(){
		$scope.showHome = true;
		$scope.showformPltsActs = false;
	};

	
	$scope.entr = null;
    $http.get('/prestaviticoles/api/company/1234567891/?format=json')
    .success(function(out_data) {
          	$scope.entr = out_data ;
          	console.log($scope.entr);
    });
	$scope.conf = null;
    $http.get('/prestaviticoles/api/conf/1234567891/?format=json')
    .success(function(out_data) {
	    $scope.conf = out_data ;
		//bouton ParPlants ou ParHa
		$scope.btParPlts = false;
		if($scope.conf.plant == true){
			$scope.btParPlts = true;
		}
		$scope.btParHa = false;
		if($scope.conf.superficie == true){
			$scope.btParHa = true;
		}
    });

	$scope.allActivities = [];
    $http.get('/prestaviticoles/api/activities/1234567891/?format=json')
    .success(function(out_data) {
        $scope.allActivities = out_data ;
    });

	$scope.showformPltsActs = false;
	$scope.allActivities = [];
	$scope.toDevisParPlants = function(){
		$scope.showHome = false;
		$scope.showformPltsActs = true;
	};
    $http.get('/prestaviticoles/api/activities/1234567891/?format=json')
    .success(function(out_data) {
        $scope.allActivities = out_data ;
    });
});