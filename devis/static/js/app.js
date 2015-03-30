var my_app = angular.module("newEstimate", [ "ngSanitize","ngResource", "ngRoute","ui.tinymce", "ngCookies" ,"ActivityServiceMock","MesDirectives"]);
my_app.config(function($httpProvider,$resourceProvider,$routeProvider) {
		$httpProvider.defaults.headers.post['Content-Type'] = 'application/x-www-form-urlencoded';
});

my_app.controller("formMakedevisCtrl", function($scope,$routeParams, $location, $filter ,$http, $cookies,activitiesService ) {

	/////////////////////////////////////////Get Siret///////////////
	$scope.siret = activitiesService.getSiretInPath();
	///Données///////////
	$scope.detailsCompany = activitiesService.getEntrDetails($scope.siret).get();
	$scope.conf = activitiesService.getEntrConf($scope.siret).get();
	$scope.groups = activitiesService.getGroups($scope.siret).query();
	//Par défaut , on montre que la page d'accueil
	$scope.showHome = true;
	$scope.showformPltsActs = false;
	$scope.showformPltsActsParam = false;
	///Superficie ou plant/////
	$scope.parPlant = false;
	$scope.parSuperficie = false;	
	$scope.typePlOuSup = null;
	////params////////
	$scope.allParams = {
		nombrePlants: 0
	};
});