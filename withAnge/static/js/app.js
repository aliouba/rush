var my_app = angular.module("newEstimate", [ "ngSanitize","ngResource", "ngRoute","ui.tinymce", "ngCookies" ,"ActivityServiceMock","MesDirectives"]);
my_app.config(function($httpProvider,$resourceProvider) {
    $httpProvider.defaults.headers.common['X-Requested-With'] = 'XMLHttpRequest';
});
 
my_app.controller("formHomeCtrl", function($scope, $location, $filter ,$http, $cookies,activitiesService ) {
	///Données///////////
	$scope.detailsCompany = activitiesService.getEntrDetails(1234567891).get();
	$scope.conf = activitiesService.getEntrConf(1234567891).get();
	$scope.allActivities = activitiesService.getActivities(1234567891).query();	

	//Par défaut , on montre que la page d'accueil
	$scope.showHome = true;
	$scope.showformPltsActs = false;
	$scope.showformPltsActsParam = false;
	//Aller -> la page d'acueil
	$scope.toShowHome = function(){
		$scope.showHome = true;
		$scope.showformPltsActsParam = false;
		$scope.showformPltsActs = false;
	};
	//Aller > Page de params
	$scope.toDevisParPlantsParams = function(){
		$scope.showHome = false;
		$scope.showformPltsActsParam = true;
		$scope.showformPltsActs = false;
	};
	//Aller -> Activities par plant
	$scope.toDevisParPlants = function(){
		$scope.showHome = false;
		$scope.showformPltsActsParam = false;
		$scope.showformPltsActs = true;
	};
});