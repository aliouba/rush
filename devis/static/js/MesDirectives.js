angular.module("MesDirectives", ["ActivityServiceMock"])
.directive("contenuHomeDevis", function() {
	return {
		restrict: "E",
        templateUrl: '/static/directivesHTML/homeDevis.html',
        scope: {
         entr: "=",        	
         conf: "=",
         showhome: "=",
         showparams: "=",
         showdevis: "=",
         parplant: "=",
         parsuperficie: "=",
         typeplousup: "="                                                   
     },
     controller: function($scope) {
            //Aller > Page de params
            $scope.todevisparams = function(typeDevis){
                if(typeDevis == "plant"){
                    $scope.parplant = true;
                    $scope.parsuperficie = false;   
                    $scope.typeplousup = "plant";
                }
                else{
                    $scope.parsuperficie = true;
                    $scope.parplant = false;
                    $scope.typeplousup = "Superficie";
                }
                $scope.showhome = false;
                $scope.showparams = true;
                $scope.showdevis = false;
            };        
        }
    }
})
.directive("contenuParams", function() {
	return {
		restrict: "E",
        templateUrl: '/static/directivesHTML/paramsDevis.html',
        scope: {
            conf: "=",
            params: "=",
            showhome: "=",
            showparams: "=",
            showdevis: "=",
            parplant: "=",
            parsuperficie: "=",
            typeplousup: "="    
        },
        controller: function($scope) {
            //Aller -> la page d'acueil
            $scope.toshowhome = function(){
                $scope.showhome = true;
                $scope.showparams = false;
                $scope.showdevis = false;
            };
            //Aller -> Activities par plant
            $scope.toestimate = function(){
                if($scope.parsuperficie == true){             
                    if($scope.params.optionssuperficie || $scope.params.optionsdistceps || $scope.params.optionsdistrangs){
                        $scope.params.nombrePlants = $scope.params.optionssuperficie / ( $scope.params.optionsdistceps * $scope.params.optionsdistrangs) ;
                        if($scope.params.nombrePlants > 100){
                            $scope.showhome = false;
                            $scope.showparams = false;
                            $scope.showdevis = true;
                        }
                    }
                }
                else{
                    if($scope.parplant == true && $scope.params.nombrePlants > 100){
                        $scope.showhome = false;
                        $scope.showparams = false;
                        $scope.showdevis = true;
                    }
                }
            };
        }
    }
})
.directive("contenuDevis", function(activitiesService) {
	return {
		restrict: "E",
                templateUrl: '/static/directivesHTML/devis.html',
                scope: {
                	groups: "=",
                    params: "=",
                    showhome: "=",
                    showparams: "=",
                    showdevis: "=",
                    parplant: "=",
                    parsuperficie: "=",
                    typeplousup: "="    
                },
                controller: function($scope) {
                        //Aller > Page de params
                        $scope.todevisparams = function(){
                            $scope.showhome = false;
                            $scope.showparams = true;
                            $scope.showdevis = false;
                        }; 
                        $scope.createestimate = function(){
                            console.log($scope.benefits);
                        };     
                        $scope.benefits = [];
                        $scope.selectBenefit = function(groupID,activityID){
                                $scope.benefitsStatus = false;
                                for (var i = 0; i < $scope.benefits.length  ; i++) {
                                        if( $scope.benefits[i].group ==  groupID){
                                            $scope.benefits[i].activity = activityID;
                                            $scope.benefits[i].plants = $scope.params.nombrePlants;
                                            $scope.benefitsStatus = true;
                                        }
                                };
                                if($scope.benefitsStatus == false){
                                        $scope.oneBenefit = {group:groupID,activity:activityID,plants:$scope.params.nombrePlants};
                                        $scope.benefits.push($scope.oneBenefit);
                                }
                        };
                }
	}
})