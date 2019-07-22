var app = angular.module('myApp', ['ngRoute']);


app.controller('loginController',function($scope,$location,$window,$http,){
	var today = new Date();
  var minAge = 18;
  $scope.minAge = new Date(today.getFullYear() - minAge, today.getMonth(), today.getDate());
	$scope.Register=function(){

        console.log("Register");
     
        $http({
            
            method:"POST",
            url: "/signup/",
            data: {
                'name':$scope.name,
                'email': $scope.email,
                'dob': $scope.dob,
                'phone':$scope.phone,
                'password': $scope.pass,

                
         }
     }).then(
         function (success){
             console.log(success.data.status);
             $scope.loginsuccess=success.data.status;
             if($scope.loginsuccess=="0"){
                 alert("User already exists");
             if($scope.verifyotp==apiotp){
                 alert("successful");
                

             }else
             aler("incorrect otp");
             }else{
              $window.location.href = "/homehtml";
             }
             
         });
     
         
}

$scope.otp=function(){
    console.log("hello");
    console.log("phone",$scope.phone);
    $http({
        method:"POST",
        url:"/verifymobile/",
        data:{
            'phone':$scope.phone
        }
    }).then(function(success){
        console.log("apiotp",success.data.OTP);
        $scope.verifyotp=success.data.otp;
    })
}

// $scope.apiotp = otp.getData();
//     $scope.otp=function(){
//         console.log("$scope.sharedData",$scope.sharedData);
//         console.log("$scope.OTP",$scope.OTP);
//         if($scope.apiotp == $scope.otp){
//             $window.location.href = "";
//         }else{
//             alert("Incorrect otp");
//         }
//     }


 });   

