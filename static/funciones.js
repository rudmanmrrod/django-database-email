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

function addToHtml(){
  var model = document.getElementById('id_models').value
  var val = document.getElementById('id_fields').value
  var html_content = $('#id_mail').trumbowyg('html');
  console.log(html_content)
  var content = "{{"+val+"}}"
  $('#id_mail').trumbowyg('html',html_content+" "+content);
}