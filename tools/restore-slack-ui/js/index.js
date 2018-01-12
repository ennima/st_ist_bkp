 
 var user_name = "Javier Hernández"
 var it_name = "Enrique Nieto"
 
 var user_first_name = user_name.split(" ")[0]
 var it_first_name = it_name.split(" ")[0]
 var current_message_index = -1
 var prev_message_index = -1
 
 $('[data-toggle="tooltip"]').tooltip()
 //$("#pedir_btn").tooltip()
 
 function getRandomInt(min, max) {
    return Math.floor(Math.random() * (max - min + 1)) + min;
	}
 
 function formatDate(date) {
  let hours = date.getHours();
  let minutes = date.getMinutes();
  let hours_24 = date.getHours();
  let ampm = hours >= 12 ? 'pm' : 'am';
  
  hours = hours % 12;
  hours = hours ? hours : 12; // the hour '0' should be '12'
  minutes = minutes < 10 ? '0'+minutes : minutes;
  let strTime = hours + ':' + minutes + ' ' + ampm;
  let strTime24 = hours_24 + ':' + minutes + ' ';
  return  date.getDate()+ "-" + date.getMonth()+1 + "-" + date.getFullYear() + " " + strTime24;
}
 
 function add_item(){
 	
 	let clip_name = $("#clip_name").val()
  let clip_path = $("#clip_path").val()
  
  //Validation
  if(clip_name == ""){
  	console.log("¿Cómo se llama el clip?")
    $("#clip_name").tooltip('show')
  }else if(clip_path == ""){
  	console.log("¿Dónde está el clip?")
    $("#clip_path").tooltip('show')
  }else{
  
      let d = new Date();
      let now_fotmat = formatDate(d);

      let render_item = `<div id="peticion_item">
              <i class="fa fa-fw logo" aria-hidden="true"></i>
              <p id="nombre_peticion">${clip_name}</p>
              <p id="fecha_peticion">${now_fotmat}</p>
          </div>`
      let item_list = render_item + $("#peticion_area").html()

      //console.log(render_item)

      $("#peticion_area").html(item_list)
  
  
  }  
 }
 
 function print_peace_message(text){
 	let render_message = `<div class="alert alert-info" role="alert">
            ${text}
          </div>`
 	$("#log").html(render_message)
 }
 
 function first_message(){
 	let pace_messages = [
  										`${user_first_name}, en breve alguien de IT se pondrá en contacto contigo.`
                      ,`Estamos trabajando en tu clip. :)`
                      ,`${it_first_name} se encuentra resolviendo otro caso, en un momento se comunica contigo.`
                      ,`Recibimos tu petición, pronto será recuperado tu clip.`
                      ,`De momento todos en IT estamos resolviendo otros casos, en unos minutos alguno de nosotros se comunica contigo.`
                      ,`En un momento lo tienes. :D`
                      ,`Recuperando...`
                      ,`Hoy es un día con muchas recuperaciones, en un momento tienes tu clip. :D`
                      ,`¿Hay más clips por recuperar?`
                      ,`Hola ${user_first_name}, dame unos minutos para recuperar tu clip, te aviso cuando esté recuperado.`
                      ,`Dentro de unos minutos revisa en Vbackup o Recup Data, para verificar que lo tienes.`
                   
                      ]
                      
                      
	let message_index = getRandomInt(0,pace_messages.length-1)
  console.log(`message_index: ${message_index} current_message_index: ${current_message_index}`)
  if(current_message_index > -1){
  	if(message_index == current_message_index){
    	console.log("repetido...")
    	let nex_index = message_index + 1
      let prev_index = message_index - 1
      if(nex_index >= pace_messages.length){
      	current_message_index = prev_index
        message_index = prev_index
      }else{
      	current_message_index = nex_index
        message_index = nex_index
      }
    }
  }else{
  	current_message_index = message_index
  }
  console.log(pace_messages[message_index])
  console.log(pace_messages.length)
  print_peace_message(pace_messages[message_index])
  current_message_index = message_index
  
 }
 
 $("#pedir_btn").click(function(){
 	$(this).tooltip('hide')
 	add_item()
  first_message()
 })
 
 
 $('#clip_name').on('input',function(e){
 // Code here
 	$(this).tooltip('hide')
});

 $('#clip_path').on('input',function(e){
 // Code here
 	$(this).tooltip('hide')
});
















	




var substringMatcher = function(strs) {
  return function findMatches(q, cb) {
    var matches, substringRegex;
		console.log('TYPYYYYYYYNG');
    // an array that will be populated with substring matches
    matches = [];

    // regex used to determine if a string contains the substring `q`
    substrRegex = new RegExp(q, 'i');

    // iterate through the pool of strings and for any string that
    // contains the substring `q`, add it to the `matches` array
    $.each(strs, function(i, str) {
      if (substrRegex.test(str)) {
        matches.push(str);
      }
    });

    cb(matches);
  };
};

var states = ['Alabama', 'Alaska', 'Arizona', 'Arkansas', 'California',
  'Colorado', 'Connecticut', 'Delaware', 'Florida', 'Georgia', 'Hawaii',
  'Idaho', 'Illinois', 'Indiana', 'Iowa', 'Kansas', 'Kentucky', 'Louisiana',
  'Maine', 'Maryland', 'Massachusetts', 'Michigan', 'Minnesota',
  'Mississippi', 'Missouri', 'Montana', 'Nebraska', 'Nevada', 'New Hampshire',
  'New Jersey', 'New Mexico', 'New York', 'North Carolina', 'North Dakota',
  'Ohio', 'Oklahoma', 'Oregon', 'Pennsylvania', 'Rhode Island',
  'South Carolina', 'South Dakota', 'Tennessee', 'Texas', 'Utah', 'Vermont',
  'Virginia', 'Washington', 'West Virginia', 'Wisconsin', 'Wyoming'
];

var carpetas = ["Noticias", "GV NOT", "SKY", "Hey", "Programas HD Viernes", "FromMac", "FIELD_EDIT", "Redactores", "Operadores", "Ingesta Noticias", "TRUCOS", "RECUP DATA", "Estados", "Papelera", "From Archive", "GV Play", "LiveU", "EDIUS_LOCK", "ConformTempStore", "Camarografos", "PlayToAir", "Estudio", "Aldo", "Internacionales", "Ivette", "Cortinillas Noticias", "Paloma", "RMI", "Recycle Bin", "Fly", "Cepropie", "TEMPORAL", "TEST", "La Aficion", "Especiales Noticias", "default", "Productores", "Reporteros", "Comercial", "Media Manager", "REUTERS", "GXF", "IMPORTS", "Pogramas HD", "MXF", "Monterrey"]


$('#clip_path').typeahead({
  hint: true,
  highlight: true,
  minLength: 1
},
{
  name: 'carpetas',
  source: substringMatcher(carpetas)
});


