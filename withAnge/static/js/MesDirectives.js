angular.module("MesDirectives", [])
.directive("contenuHomeDevis", function() {
	return {
		restrict: "E",
        templateUrl: '/static/directivesHTML/homedevis.html',
        scope: {
        	email: "="
        }
	}
})