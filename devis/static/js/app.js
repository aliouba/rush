var my_app = angular.module("newEstimate", [ "ngSanitize","ngResource", "ngRoute","ui.tinymce", "ngCookies" ,"ActivityServiceMock","MesDirectives"]);
my_app.config(function($httpProvider,$resourceProvider) {
	$httpProvider.defaults.headers.common['X-Requested-With'] = 'XMLHttpRequest';
});

my_app.controller("formMakedevisCtrl", function($scope, $location, $filter ,$http, $cookies,activitiesService ) {
	///Données///////////
	$scope.detailsCompany = activitiesService.getEntrDetails(1234567891).get();
	$scope.conf = activitiesService.getEntrConf(1234567891).get();
	$scope.groups = activitiesService.getGroups(1234567891).query();
	/////////////////////////////////////////
	///////////////////////////////////////////


	//Par défaut , on montre que la page d'accueil
	$scope.showHome = true;
	$scope.showformPltsActs = false;
	$scope.showformPltsActsParam = false;
	///Superficie ou plant/////
	$scope.parPlant = false;
	$scope.parSuperficie = false;	
	$scope.typePlOuSup = null;
	//Nombre de plants
	$scope.nbPlants= 0;
	//Aller -> la page d'acueil
	$scope.toShowHome = function(){
		$scope.showHome = true;
		$scope.showformPltsActsParam = false;
		$scope.showformPltsActs = false;
	};
	//Aller > Page de params
	$scope.toDevisParams = function(typeDevis){
		if(typeDevis == "plant"){
			$scope.parPlant = true;
			$scope.parSuperficie = false;	
			$scope.typePlOuSup = "plant";
		}
		else{
			$scope.parSuperficie = true;
			$scope.parPlant = false;
			$scope.typePlOuSup = "Superficie";
		}
		$scope.showHome = false;
		$scope.showformPltsActsParam = true;
		$scope.showformPltsActs = false;
	};
	//Aller -> Activities par plant
	$scope.toDevis = function(){
		if($scope.parSuperficie == true){
			console.log($scope.option);
			if($scope.option.optionssuperficie || $scope.option.optionsdistceps || $scope.option.optionsdistrangs){
				$scope.nbPlants = $scope.option.optionssuperficie / ( $scope.option.optionsdistceps * $scope.option.optionsdistrangs) ;
				$scope.showHome = false;
				$scope.showformPltsActsParam = false;
				$scope.showformPltsActs = true;
			}
			else{

			}

		}
		else{
			$scope.showHome = false;
			$scope.showformPltsActsParam = false;
			$scope.showformPltsActs = true;
		}
	};

});