var app = angular.module('app_demo',[]);

app.config(function($interpolateProvider) {
	$interpolateProvider.startSymbol('{$');
	$interpolateProvider.endSymbol('$}');
});

function homeCtrl($scope) {
  $scope.holaMundo ='Hola mundo - Angular';
}