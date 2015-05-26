angular.module("Admin", [])
.controller("AdminController", [
        "$scope",
        "$http",
        function($scope, $http) {
            $scope.ang_posts = [];
            $scope.ang_departamento = null;
            $scope.ang_tipo_cenedu = 'Colegio';
            $scope.ang_nombre_cenedu = null;
            $scope.ang_centros_edu = null;
            $scope.ang_n_centros_edu = 0;
            $http.get("/administrador/departamentos/")
                .success(
                    function(data){
                        console.log(data);
                        $scope.ang_posts = data;
                    }
                )
                .error(
                    function(err){
                    }
                );
            $scope.busca_cen_edu = function(departamento, tipo){
                if (departamento != null) {
                    console.log("/administrador/centro_educativo/" + departamento + "/" + tipo);
                    $http.get("/administrador/centro_educativo/" + departamento + "/" + tipo)
                        .success(
                        function (data) {
                            $scope.ang_n_centros_edu = data.length;
                            $scope.ang_centros_edu = data;
                            console.log($scope.ang_centros_edu);
                        }
                    )
                        .error(
                        function (err) {
                        }
                    );
                }
            };
        }
    ]
);