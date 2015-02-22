angular.module("ActivityServiceMock", [])
.factory("activitiesService", function($http, $resource) {
    //Recupération des infos de l'entreprise
    return {
        getEntrDetails: function (siret) {
           return $resource('/prestaviticoles/api/company/:siret/?format=json',{siret:siret});
        },
        getEntrConf: function (siret) {
           return $resource('/prestaviticoles/api/conf/:siret/?format=json',{siret:siret});
        },
        getActivities: function (siret) {
           return $resource('/prestaviticoles/api/activities/:siret/?format=json',{siret:siret});
        },
        getGroups: function (siret) {
           return $resource('/prestaviticoles/api/group_activities/:siret/?format=json',{siret:siret});
        }
    }
})  