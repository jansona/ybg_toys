var app = angular.module("myApp", [])

app.controller("showAll", function($scope, $http){
    $scope.all = function(){
        $http.get("http://localhost:8080/user")
            .then(function(response){$scope.persons = response.data;})
    }
});

app.controller("queryAll", function($scope, $http){
    $scope.methods = ["id", "name", "email"]
    $scope.query = function(){
        var data = { keyword: $scope.keyword, method: $scope.selectedItem };
        $http.post("http://localhost:8080/user/", data)
            .then(function(response){$scope.persons = response.data;});
    };
    $scope.delete = function(id) {
        $http.post("http://localhost:8080/user/remove/", {ID: id, keyword: $scope.keyword, method: $scope.selectedItem})
            .then(function (response) {
                $scope.persons = response.data;
            });
    };
    $scope.update = function(id){
        $('#updateModal').modal('toggle')
        $scope.id = id;
    };
    $scope.submit = function(){
        alert($scope.newName + " " + $scope.newEmail);
        $http.post("http://localhost:8080/user/update/", {id: $scope.id, name: $scope.newName, email: $scope.newEmail})
            .then(function(response){
                alert(response.data);
            });
    };
});

app.controller("create", function($scope, $http){
    $scope.add = function(){
        $http.post("http://localhost:8080/user/add/", {name: $scope.name, email: $scope.email})
            .then(function(reponse){
                $scope.name = "";
                $scope.email = "";
                $scope.result = "添加成功";
            })
    }
});

