var tracerApp = angular.module('tracer',[]);

tracerApp.config(function($interpolateProvider) {
    $interpolateProvider.startSymbol('{$');
    $interpolateProvider.endSymbol('$}');
});

/*----- controller FILTRO-----*/
tracerApp.controller('filtroCtrl',function cadenaCtrl($scope, $http){
	$scope.cadenas={};
	var url='/ws/marca/76/cadenas';
	$http.get(url).success(function (data){
		$scope.cadenas=data.cadenas.item; //Get Element items in datos
	});

	
	/*
	$http.get('/ws/tienda/').success(function (data){
		$scope.tiendas=data.tiendas.item; //Get Element items in datos
	});
	$http.get('/ws/estado/').success(function (data){
		$scope.estados=data.datos.item; //Get Element items in datos
	});
	$http.get('/ws/responsable/').success(function (data){
		$scope.responsables=data.promotores.item; //Get Element items in datos
	});*/
});
/*----- controller Lista visitas-----*/
/*tracerApp.controller('listVistCtrl',function listCtrl($scope, $http){
	$scope.visitas={};
	var url='/ws/visita/filtro/division/1/inicio/20131101/fin/20131127/cadena//tienda//estado//responsable//';
	$http.get(url).success(function (data){
		$scope.visitas=data.visitas.item; //Get Element items in datos
		
	});*/

	$scope.visitDetails = function (param) {
		alert(param);
		
		//console.log("Get data visit ID: "+data);
		//Hacer todas las peticiones sobre demanda (Fotos, Precios, Comentarios, Participacion, Detalles)
	}
});