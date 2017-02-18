(function () {

    angular.module('sql-sandbox', ['ngRoute']);

    angular
        .module('sql-sandbox')
        .controller('demoCtrl', demoCtrl);

    demoCtrl.$inject = ['$scope', '$http', 'sqlService'];
    function demoCtrl($scope, $http, sqlService) {
        console.log("demo running");
        $scope.users = [];
        $scope.exec = [];

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

        $scope.exec.push(function () {
            sqlService.insert().then(displayData);
        });

        $scope.exec.push(function () {
            displayData();
        });

        $scope.exec.push(function () {
            sqlService.select1().then(function(data){
                $scope.users = data.data;
                formatUsers();
            });
        });

        $scope.exec.push(function () {
            sqlService.select2().then(function(data){
                $scope.users = data.data;
                formatUsers();
            });
        });

        $scope.exec.push(function () {
            sqlService.select3().then(function(data){
                $scope.users = data.data;
                formatUsers();
            });
        });

        $scope.exec.push(function () {
            sqlService.select4().then(function(data){
                $scope.users = data.data;
                formatUsers();
            });
        })

        $scope.exec.push(function () {
            sqlService.update().then(displayData);
        });

        $scope.exec.push(function () {
            sqlService.del().then(displayData);
        });

        $scope.exec.push(function () {
            sqlService.select5().then(function(data){
                $scope.users = data.data;
                formatUsers();
            })
        });

        $scope.exec.push(function () {
            sqlService.select6().then(function(data){
                $scope.users = data.data;
                formatUsers();
            })
        });

        $scope.exec.push(function () {
            sqlService.select7().then(function(data){
                $scope.users = data.data;
                formatUsers();
            })
        });

        $scope.exec.push(function () {
            sqlService.select8().then(function(data){
                $scope.users = data.data;
                console.log(data)
                formatUsers();
            })
        });

        $scope.exec.push(function () {
            sqlService.select9().then(function(data){
                $scope.users = data.data;
                formatUsers();
            })
        });

        $scope.exec.push(function () {
            sqlService.select10().then(function(data){
                $scope.users = data.data;
                formatUsers();
            })
        });

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

         var del = function() {
            return $http.get('/delete/fail');
         }

        var select5 = function () {
            return $http.get('/select/like');
         }

        var select6 = function () {
           return $http.get('/select/top');
        }

        var select7 = function () {
            return $http.get('/select/order');
        }

        var select8 = function () {
           return $http.get('/select/group');
        }

        var select9 = function () {
             return $http.get('/select/distinct');
        }

        var select10 = function () {
           return $http.get('/select/sort');
        }

        return {
            insert : insert,
            display : display,
            select1 : select1,
            select2 : select2,
            select3 : select3,
            select4 : select4,
            update : update,
            del : del,
            select5 : select5,
            select6 : select6,
            select7 : select7,
            select8 : select8,
            select9 : select9,
            select10 : select10
        };
    }

})();