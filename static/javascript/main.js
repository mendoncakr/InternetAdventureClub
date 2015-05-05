$(document).ready(function(){

  $('#map').ready(function(e){
    cartodb.createVis('map', 'https://mendoncakr.cartodb.com/api/v2/viz/6f745cd2-f2a5-11e4-a632-0e4fddd5de28/viz.json', {https: true});
  });

});

  // Assign a new mission
  // $('form[name="register"]').on("submit", function(e){
    // e.preventDefault();
    // var register_form = $(this).serialize()

    // $.ajax({
    //   url: '/mission/new/',
    //   type: "POST",
    //   data: register_form,
    //   success : function(json) {
    //     console.log("SUCCESS!!");
    //     console.log(json);
    //   },
    //   error :  function(json)  {
    //     console.log("ERROR");
    //     console.log(json);
    //   }
    // });
  // });

