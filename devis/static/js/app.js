var my_app = angular.module("newEstimate", [ "ngSanitize","ngResource", "ngRoute","ui.tinymce", "ngCookies" ,"ActivityServiceMock","MesDirectives"]);
my_app.config(function($httpProvider,$resourceProvider,$routeProvider) {
	$httpProvider.defaults.headers.common['X-CSRFToken'] = '{{ csrf_token|escapejs }}';
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
	//////Nb Plant/////////////
	$scope.nbPlants = 0;
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
			console.log($scope.params);
			if($scope.params.optionssuperficie || $scope.params.optionsdistceps || $scope.params.optionsdistrangs){
				$scope.nbPlants = $scope.params.optionssuperficie / ( $scope.params.optionsdistceps * $scope.params.optionsdistrangs) ;
				console.log($scope.nbPlants);
				$scope.showHome = false;
				$scope.showformPltsActsParam = false;
				$scope.showformPltsActs = true;
			}
			else{
				console.log("error");
			}

		}
		else{
			$scope.showHome = false;
			$scope.showformPltsActsParam = false;
			$scope.showformPltsActs = true;
		}
	};
	
});