angular.module("ActivityServiceMock", [])
.factory("activitiesService", function($http) {
    //Recupération des infos de l'entreprise
    return {
        getEntrDetails: function(siret) {
            var api = "/prestaviticoles/api/activities/";
            var format = "/?format=json";
            var url = api.concat(siret,format);
            return $http.get("/prestaviticoles/api/activities/" + siret + "/?format=json").then(function(result) {
               return result.data;
            });
        }
    }
})