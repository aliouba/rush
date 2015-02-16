var my_app = angular.module("newEstimate", [ "ngSanitize", "ui.tinymce", "ngCookies"]);
my_app.config(function($httpProvider) {
    $httpProvider.defaults.headers.common['X-Requested-With'] = 'XMLHttpRequest';
});
 
my_app.controller("formHomeCtrl", function($scope, $location, $filter ,$http, $cookies ) {
	//Par défaut , on montre que la page d'accueil
	$scope.showHome = true;
	$scope.showformPltsActs = false;
	$scope.showformPltsActsParam = false;


	//Recupération des infos de l'entreprise
    $http.get('/prestaviticoles/api/company/1234567891/?format=json').success(function(out_data) {
          	$scope.entr = out_data ;
          	console.log($scope.entr);
    });
    //Recupération des infos de configuration
    $scope.btParPlts = false;
    $scope.btParHa = false;
    $http.get('/prestaviticoles/api/conf/1234567891/?format=json').success(function(out_data) {
	    $scope.conf = out_data ;
	    console.log($scope.conf);
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
    //Recupération des activités
    $http.get('/prestaviticoles/api/activities/1234567891/?format=json').success(function(out_data) {
        $scope.allActivities = out_data ;
        console.log($scope.allActivities);
    });
    ///////////////////Functions//////////////////
	//Aller -> la page d'acueil
	$scope.toShowHome = function(){
		$scope.showHome = true;
		$scope.showformPltsActsParam = false;
		$scope.showformPltsActs = false;
	};
	$scope.toDevisParPlantsParams = function(){
		$scope.showHome = false;
		$scope.showformPltsActsParam = true;
		$scope.showformPltsActs = false;
	};
    //Aller ->  Activities par plant
	$scope.toDevisParPlants = function(){
		$scope.showHome = false;
		$scope.showformPltsActsParam = false;
		$scope.showformPltsActs = true;
	};
});