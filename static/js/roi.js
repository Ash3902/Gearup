
function compute(){
    var monthVisit =  document.getElementById('monthly-visitors').value
    var monthLeads = document.getElementById('monthly-leads').value
    var monthQual = document.getElementById('qualified-leads').value
    var monthClose =  document.getElementById('closed-leads').value
    var monthTot =  document.getElementById('customer-val').value
    var monthlyLeads =  document.getElementById('monthly-leads').value
    var monthlyVisitors =  document.getElementById('monthly-visitors').value
    if(monthVisit == "" || monthLeads == "" || monthQual == "" || monthClose == "" || monthTot == "") {
            alert('Some fields are empty');
          } else {
            
              console.log(monthVisit);
              //     Store conversion rate
              var conversionRate = ((monthlyLeads/monthlyVisitors)*100).toFixed(2);
              
              //     Store qualified leads / month
              var qualifiedLeads = ((monthLeads*monthQual)/100).toFixed(2);
              
              //     Store avg new customers / month
              var newCustomers = ((qualifiedLeads * monthClose)/100).toFixed(2);
              
              //     Store total revenue
              var totRevenue = newCustomers * monthTot;
              
              var v1 = Math.floor(totRevenue / conversionRate); 
              // var v1 = Math.ceil(totRevenue * 0.0125);
              var v2 = Math.ceil(totRevenue * 0.3);
              var v3 = v1 + v2;
              v1 = v1.toFixed(2);    
              v2 = v2.toFixed(2);
              v3 = v3.toFixed(2);
              
              //     Display conversion rate
              document.querySelector('.conv-rate').innerHTML =  (conversionRate);
              
              //     Store qualified leads / month
              document.querySelector('.q-leads').innerHTML =  (qualifiedLeads);
              
              //     Store avg new customers / month
              document.querySelector('.new-customer').innerHTML =  (newCustomers);
              
              //     Store total revenue
              document.querySelector('.t-rev').innerHTML =  (totRevenue);
              
              document.querySelector('.v1').innerHTML =  (v1);
              document.querySelector('.v2').innerHTML =  (v2);
              document.querySelector('.v3').innerHTML =  (v3);
              
              document.querySelector('.month-traffic').innerHTML =  (monthVisit);
              document.querySelector('.month-leads').innerHTML =  (monthLeads);
              document.querySelector('.month-qualified').innerHTML =  (monthQual);
              document.querySelector('.month-close').innerHTML =  (monthClose);
              document.querySelector('.month-tot').innerHTML =  (monthTot);
              
            }
            
        }
            
 
//   $('#dwnld-btn').click(function () {
//   var pdf = new jsPDF();
//   var specialElementHandlers = {
//     '#editor': function (element, renderer) {
//         return true;
//     }
//   };
//   var $temp = $('.okk');
//   pdf.fromHTML($temp.html(), 15, 15, {
//         'width': 170,
//         'elementHandlers':specialElementHandlers
// 	    }
//   );
//   if ($('#email-address').value) !== '') {
//   pdf.save('sample-file.pdf');
//   	$('.email-container').hide();
//   	$('.form-overlay').hide();
//     $('body').removeClass('scroll-hidden');
//   } else {
//     alert("Please fill the email address!");
//   }
// });


// $('#popup-btn').on('click', function() {
//   if($('#monthly-visitors').value == "" || $('#monthly-leads').value == "" || $('#qualified-leads').value == "" || $('#closed-leads').value == "" || $('#customer-val'){
//     alert('Some fields are empty');
//   } else {
//     $('.email-container').show();
//     $('.form-overlay').show();
//     $('body').addClass('scroll-hidden');
//   }
// })



//   $('.form-overlay').on('click', function() {
//   	$('.email-container').hide();
//   	$('.form-overlay').hide();
//     $('body').removeClass('scroll-hidden');
//   })

// 	document.onkeydown = function(evt) {
// 	    evt = evt || window.event;
// 	    if (evt.keyCode == 27) {
// 		  	$('.email-container').hide();
// 		  	$('.form-overlay').hide();
//     $('body').removeClass('scroll-hidden');
// 	    }
// 	};
  
  
