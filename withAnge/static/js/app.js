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
	$scope.showformPltsActsParam = false
});