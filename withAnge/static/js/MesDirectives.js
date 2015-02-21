angular.module("MesDirectives", [])
.directive("contenuHomeDevis", function() {
	return {
		restrict: "E",
                templateUrl: '/static/directivesHTML/homeDevis.html',
                scope: {
                	entr: "=",        	
                	conf: "=",
                	selectparamplant: "&",
                        selectparamsuperficie: "&"
                }
	}
})
.directive("contenuParams", function() {
	return {
		restrict: "E",
                templateUrl: '/static/directivesHTML/paramsPlantDevis.html',
                scope: {
                	conf: "=",
                	selecthome: "&",
                	selectdevis: "&",
                        paramsuperficie: "="

                },
                controller: function($scope) {
                        $scope.params = {};
                }
	}
})
.directive("contenuPlants", function() {
	return {
		restrict: "E",
                templateUrl: '/static/directivesHTML/PlantsDevis.html',
                scope: {
                	activities: "=",
                	selectparam: "&"
                }
	}
})