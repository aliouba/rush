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
                todevis: "&",
                paramsuperficie: "=",
                params: "=",
                nbplants: "=",
                showhome: "=",
                showformpltsactsparam: "=",
                showformpltsacts: "="

        },
        controller: function($scope) {
                    $scope.toDevis = function(){
                        console.log($scope.params);
                        if($scope.parSuperficie == true){
                            if($scope.params.optionssuperficie || $scope.params.optionsdistceps || $scope.params.optionsdistrangs){
                                console.log($scope.params.optionssuperficie);
                                $scope.nbPlants = $scope.params.optionssuperficie / ( $scope.params.optionsdistceps * $scope.params.optionsdistrangs) ;
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
                    devisparsup: "=",
                    devisparplant: "=",
                    activities: "="
                },
                controller: function($scope) {
                        $scope.nbplants = 0;
                        $scope.benefits = [];
                        $scope.selectBenefit = function(groupID,activityID,nbPlants){
                                $scope.benefitsStatus = false;
                                for (var i = 0; i < $scope.benefits.length  ; i++) {
                                        if( $scope.benefits[i].group ==  groupID){
                                            $scope.benefits[i].activity = activityID;
                                            $scope.benefits[i].plants = nbPlants;
                                            $scope.benefitsStatus = true;
                                        }
                                };
                                if($scope.benefitsStatus == false){
                                        $scope.oneBenefit = {group:groupID,activity:activityID,plants:nbPlants};
                                        $scope.benefits.push($scope.oneBenefit);
                                }
                        };
                        $scope.updateNbPlants = function(groupID,nbPlants){
                                $scope.benefitsStatus = false;
                                for (var i = 0; i < $scope.benefits.length  ; i++) {
                                        if( $scope.benefits[i].group ==  groupID){
                                            $scope.benefits[i].plants = nbPlants;
                                            $scope.benefitsStatus = true;
                                        }
                                };
                                if($scope.benefitsStatus == false){
                                        $scope.oneBenefit = {group:groupID,activity:"",plants:nbPlants};
                                        $scope.benefits.push($scope.oneBenefit);
                                }
                        };
                }
	}
})