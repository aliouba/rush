var my_app = angular.module("CreerCompany", [ "ngSanitize", "ui.tinymce", "ngCookies"]);
my_app.config(function($httpProvider) {
    $httpProvider.defaults.headers.common['X-Requested-With'] = 'XMLHttpRequest';
});
my_app.controller("creerCompanyCtrl", function($scope, $location, $filter ,$http, $cookies ) {
	//Les différentes parties (Home , Entreprise et Configuration)
	$scope.showConf = false;
	$scope.showEntr = false;
	$scope.showHome = true;

	$scope.suivHome = function(){
		$scope.showHome = false;
		$scope.showEntr = true;
		$scope.showConf = false;
	};
	$scope.suivEntr = function(){
		$scope.showHome = false;
		$scope.showEntr = false;
		$scope.showConf = true;
	};
	$scope.precEntr = function(){
		$scope.showHome = true;
		$scope.showEntr = false;		
		$scope.showConf = false;
	};
	$scope.suivConf = function(){
		$scope.showHome = false;
		$scope.showEntr = false;		
		$scope.showConf = false;		
	};
	$scope.precConf = function(){
		$scope.showHome = false;
		$scope.showEntr = true;		
		$scope.showConf = false;		
	};

	$scope.unetreprise = [];
        $http.get('/prestaviticoles/api/nouveauentr/1/?format=json')
          .success(function(out_data) {
          	$scope.unetreprise.entr = out_data ;
          	console.log($scope.unetreprise.entr); 
        });

    $scope.createEntrViticole = function (newEntreprise) {
        // On prépare l'envoie des données.
        var in_data = jQuery.param({'name': $scope.newEntreprise.entr.name, 'siret': $scope.newEntreprise.entr.siret,
        	'adesse': $scope.newEntreprise.entr.adesse});
        $http.post('/prestaviticoles/api/nouveauentr/1/?format=json', in_data)
          .success(function(out_data) {
          	$scope.newEntreprise = angular.copy({});
        });
    }

});
