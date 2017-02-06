(function () {

    angular.module('sql-sandbox', ['ngRoute']);

    angular
        .module('sql-sandbox')
        .controller('demoCtrl', demoCtrl);

    demoCtrl.$inject = ['$scope', '$http', 'sqlService'];
    function demoCtrl($scope, $http, sqlService) {
        console.log("demo running");
        $scope.users = [];
        sqlService.display().then(function(data) {
                $scope.users = data.data;
            });
    }

    // Service creation
     angular
        .module('sql-sandbox')
        .service('sqlService', sqlService);

    sqlService.$inject = ['$http'];
    function sqlService ($http) {

        var greet = function () {
            return $http.get('/greet');
        };

         var display = function () {
            return $http.get('/select/all');
        }

        return {
            greet : greet,
            display : display
        };
    }

})();