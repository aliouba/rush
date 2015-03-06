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
                templateUrl: '/static/directivesHTML/paramsDevis.html',
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
                templateUrl: '/static/directivesHTML/devis.html',
                scope: {
                	groups: "=",
                	selectparam: "&",
                        activities: "="
                },
                controller: function($scope) {
                        $scope.selectOption = function(groupID,activityID){
                                alert(groupID +"ffffffffffff" + activityID);
                        };
                }
	}
})