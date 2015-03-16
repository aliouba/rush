angular.module("ActivityServiceMock", [])
.factory("activitiesService", function($http, $resource) {
    //Recupération des infos de l'entreprise
    return {
        getEntrDetails: function (siret) {
           return $resource('/prestaviticoles/api/company/:siret/',{siret:siret});
        },
        getEntrConf: function (siret) {
           return $resource('/prestaviticoles/api/conf/:siret/',{siret:siret});
        },
        getGroups: function (siret) {
           return $resource('/prestaviticoles/api/group_activities/:siret/',
              {siret:siret}
            );  
        },
        selectActivity: function(goupID,activityID){
          eltsEnvoyes.emails.forEach(function(email) {


            
          });

        }
    }
})  