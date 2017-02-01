angular.module('sql-sandbox', [])
  .controller('home', function($scope, $http) {
    $http.get('/greet').then(function(data) {
        $scope.greeting = data.data;
    });
});