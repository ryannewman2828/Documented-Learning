(function () {

    angular.module('sql-sandbox', ['ngRoute']);

    angular
        .module('sql-sandbox')
        .controller('demoCtrl', demoCtrl);

    demoCtrl.$inject = ['$scope', '$http', 'sqlService'];
    function demoCtrl($scope, $http, sqlService) {
        console.log("demo running");
        $scope.users = [];

        var formatUsers = function () {
            if ($scope.users.length > 0) {
                var fields = $scope.users[0].fields.split(';');
            }
            $scope.users.map(function(user) {
                var u = {}
                for (var field in fields) {
                    u[fields[field].toLowerCase()] = user[fields[field].toLowerCase()];
                }
                return u;
            });
        }

        var displayData = function () {
            sqlService.display().then(function(data) {
                $scope.users = data.data;
            });
            formatUsers();
        }
        displayData();

        $scope.exec1 = function () {
            sqlService.insert().then(displayData);
        }

        $scope.exec2 = function () {
            displayData();
        }

        $scope.exec3 = function () {
            sqlService.select1().then(function(data){
                $scope.users = data.data;
                formatUsers();
            });
        }

        $scope.exec4 = function () {
            sqlService.select2().then(function(data){
                $scope.users = data.data;
                formatUsers();
            });
        }

        $scope.exec5 = function () {
            sqlService.select3().then(function(data){
                $scope.users = data.data;
                formatUsers();
            });
        }

        $scope.exec6 = function () {
            sqlService.select4().then(function(data){
                $scope.users = data.data;
                formatUsers();
            });
        }

        $scope.exec7 = function () {
            sqlService.update().then(displayData);
        }
    }

    // Service creation
     angular
        .module('sql-sandbox')
        .service('sqlService', sqlService);

    sqlService.$inject = ['$http'];
    function sqlService ($http) {

        var insert = function () {
            return $http.get('/create');
        }

         var display = function () {
            return $http.get('/select/all');
         }

         var select1 = function () {
            return $http.get('/select/selected');
         }

         var select2 = function () {
            return $http.get('/select/pass');
         }

         var select3 = function () {
             return $http.get('/select/salary');
         }

         var select4 = function () {
            return $http.get('/select/fail-salary');
         }

         var update = function() {
            return $http.get('/update/pass');
         }

        return {
            insert : insert,
            display : display,
            select1 : select1,
            select2 : select2,
            select3 : select3,
            select4 : select4,
            update : update
        };
    }

})();