angular.module("MesDirectives", [])
.directive("contenuHomeDevis", function() {
	return {
		restrict: "E",
        templateUrl: '/static/directivesHTML/homeDevis.html',
        scope: {
        	entr: "=",        	
        	conf: "=",
        	selectparam: "&"
        }
	}
})
.directive("contenuParamsPlants", function() {
	return {
		restrict: "E",
        templateUrl: '/static/directivesHTML/paramsPlantDevis.html',
        scope: {
        	conf: "="
        }
	}
})