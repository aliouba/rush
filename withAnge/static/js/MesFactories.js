angular.module("ActivityServiceMock", [])
.factory("activitiesService", function($http) {
    //Recupération des infos de l'entreprise
    return {
        getEntrDetails: function (siret) {
            url = "/prestaviticoles/api/activities/" + siret + "/?format=json";
           return "jjjjjjjjjjjjjjjjj";
        }
    }
})  