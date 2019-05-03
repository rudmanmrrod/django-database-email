function loadFields(pk){
  $.ajax({
    type: 'GET',
    data:{
      'pk':pk
    },
    url: URL_GET,
    success: function(response) {
      var select = document.getElementById('id_fields')
      select.innerHTML = ''
      if(response){
        for(let item of response.fields){
          let op = document.createElement('option')
          op.id = item
          op.text = item
          select.append(op)
        }
      }
    },
  });
}