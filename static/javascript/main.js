$(document).ready(function(){
  $('#map').ready(function(e){
    cartodb.createVis('map', 'https://internetadventureclub.cartodb.com/api/v2/viz/617ba774-fd8c-11e4-9e57-0e4fddd5de28/viz.json', {https: true});
  });

  // Resizes Bottom Buttons
  $(window).resize(function(){
     var width = $(window).width();
     if(width <= 900){
         $('#mission_couch').removeClass('btn-group btn-group-justified').addClass('btn-group btn-group-vertical');
     }
     else{
         $('#mission_couch').removeClass('btn-group btn-group-vertical').addClass('btn-group btn-group-justified');
     }
  }).resize()

});
