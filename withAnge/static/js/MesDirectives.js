angular.module("MesDirectives", [])
.directive("contenuHomeDevis", function() {
	return {
		restrict: "E",
        templateUrl: '/static/directivesHTML/homeDevis.html',
        scope: {
        	entr: "=",        	
        	conf: "="
        },
        controller: function($scope) {
			//Aller > Page de params
			$scope.toDevisParPlantsParams = function(){
				$scope.showHome = false;
				$scope.showformPltsActsParam = true;
				$scope.showformPltsActs = false;
			};
        }
	}
})
.directive("contenuParamsPlants", function() {
	return {
		restrict: "E",
        templateUrl: '/static/directivesHTML/paramsPlantDevis.html',
        scope: {
        }
	}
})