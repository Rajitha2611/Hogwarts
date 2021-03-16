console.log("This is for testing");
   
var $x= "http://jsonplaceholder.typicode.com/todos";
$.ajax({
    type:'GET',
    url: $x,
    success: function(data){
        $.each(data,function(i,d){
            $("#Students").append("<tr><td>"+d.userID+"</td><td>"+d.title+"</td><td>"+d.completed+"</td></tr>");
        });
        
    }
});



  $("#loginbutton").click(function(){
    $.post("http://127.0.0.1:5000/Students",{
        email: $("#exampleInputEmail1"),
        password: $("#exampleInputPassword1")
      }, function(data, status){
        console.log(data)
        alert("Data: " + data + "\nStatus: " + status);
    });
  });
 