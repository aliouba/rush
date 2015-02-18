var my_app = angular.module("newEstimate", [ "ngSanitize", "ui.tinymce", "ngCookies" ,"ActivityServiceMock","MesDirectives"]);
my_app.config(function($httpProvider) {
    $httpProvider.defaults.headers.common['X-Requested-With'] = 'XMLHttpRequest';
});
 
my_app.controller("formHomeCtrl", function($scope, $location, $filter ,$http, $cookies,activitiesService ) {
	console.log("aaaaaaaaaaaaaaaaaa");
});