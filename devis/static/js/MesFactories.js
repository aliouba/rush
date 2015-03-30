angular.module("ActivityServiceMock", [])
.factory("activitiesService", function($http, $resource, $location) {
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
     getSiretInPath: function(){
      newPath = $location.absUrl();
      var tabPath = newPath.split("/");
      for (var i = 0; i < tabPath.length ; i++) {
        if(tabPath[i] == "make_estimate"){
          return  tabPath[i+1];
        }
      };          
    },
    makeDeis: function (groups) {
      console.log(groups);
      var res = $http.post('/prestaviticoles/make_estimate/1234567891/', groups);
      res.success(function(data, status, headers, config) {
        console.log(data);
      });
      res.error(function(data, status, headers, config) {
        alert( "failure message: " + JSON.stringify({data: data}));
      });
    }
  }
})  