document.addEventListener('DOMContentLoaded', function() {
		var elems = document.querySelectorAll('.fixed-action-btn');
		var instances = M.FloatingActionButton.init(elems, {
		hoverEnabled: false
	});
  });
  

		  
		  
    document.addEventListener('DOMContentLoaded', function() {
		var elems = document.querySelectorAll('.fixed-action-btn');
		var instances = M.FloatingActionButton.init(elems, {
		hoverEnabled: false
	});
  });
  
  
	$(document).ready(function(){
      $('#venue').hide();
		$('#red-btn').click(function(){;
		 $('#newuser').hide();
		$('#venue').toggle(500);
		});
	});
	
	$(document).ready(function(){
   $('#newuser').hide();
   $('#yellow-btn').click(function(){;
		$('#venue').hide();
		$('#newuser').toggle(500);
		});
	});	
	
$(document).ready(function(){
      $('#id03').hide();
		$('#addevent').click(function(){;
		 $('#id03').show();
		
		});
	});
	
$('#navigation a').on('click', function (e) {
  e.preventDefault()
  $(this).tab('show')
})

// Get the modal
var modal = document.getElementById('id03');

// When the user clicks anywhere outside of the modal, close it
window.onclick = function(event) {
  if (event.target == modal) {
    modal.style.display = "none";
  }
}

$(function() {
            $( ".pickdate" ).datepicker({minDate: 0, dateFormat: 'yy-mm-dd'});
         });
		 
		 $(document).ready(function(){
		 $(".enable").prop("disabled", true);
        $("#availability").click(function(){
            if($(this).prop("checked") == true){
                $(".enable").prop("disabled", false);
            }
            else if($(this).prop("checked") == false){
                $(".enable").prop("disabled", true);
            }
        });
    });