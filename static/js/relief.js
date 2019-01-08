function Get(yourUrl){
    var Httpreq = new XMLHttpRequest(); // a new request
    Httpreq.open("GET",yourUrl,false);
    Httpreq.send(null);
    return Httpreq.responseText;          
}

function faceanalytics(){
    document.getElementById('forms').style.display="none";
    document.getElementById('faces').style.display="";
    document.getElementById('messages').style.display="none";
    document.getElementById('thread').style.display="none";
}



function alertnew(){
    document.getElementById('forms').style.display="block";
    document.getElementById('faces').style.display="none";
    document.getElementById('messages').style.display="none";
    document.getElementById('thread').style.display="none";

}


function dashmessages(){
	var ob = document.getElementById("faces").style.display="none";
	var ob1 = document.getElementById("forms").style.display="none";
	
	var json_obj = JSON.parse(Get("https://rvngo.azurewebsites.net/message/pipeline/gettopic"));
	
	
	var doms = document.getElementById("message-replacer").innerHTML = json_obj.data
	// console.log(json_obj.data);
	var ob1 = document.getElementById("messages").style.display="block";

	var ob1 = document.getElementById("thread").style.display="none";
}

function reply(){

	var text=document.getElementById("reply").value;
	var js1={"message":text.toString(),"user":"Relief1"};
	var mid=document.getElementById("indices").innerHTML;
	document.getElementById("reply").value="";

	console.log(mid);
	var request=new XMLHttpRequest();

	request.onreadystatechange=function(){
        if(request.readyState===XMLHttpRequest.DONE){
            if(request.status===200)
            {
                alert('Updated Successfully');
            }
            else{
                alert('Network Error');
            }
            
    }
    };
    request.open("POST",'https://rvngo.azurewebsites.net/messages/pipeline/'+mid+'/updatethread',true);
    request.setRequestHeader('Content-Type','application/json');
request.send(JSON.stringify(js1));


}

function showthread(ele){
	console.log(ele);
	var ob = document.getElementById("faces").style.display="none";
	var ob1 = document.getElementById("forms").style.display="none";
	var ob1 = document.getElementById("messages").style.display="none";

	var json_obj = JSON.parse(Get("https://rvngo.azurewebsites.net/messages/pipeline/getthread/"+ele.toString()));
	
	
	var doms = document.getElementById("threadinfo").innerHTML = json_obj.data
	var doms = document.getElementById("topicname").innerHTML = json_obj.topic
	var doms = document.getElementById("indices").innerHTML = json_obj.mid


	var ob1 = document.getElementById("thread").style.display="block";
}

function goback(){
	var ob1 = document.getElementById("messages").style.display="block";
	var ob1 = document.getElementById("thread").style.display="none";
}

(function(document) {
	'use strict';

	var LightTableFilter = (function(Arr) {

		var _input;

		function _onInputEvent(e) {
			_input = e.target;
			var tables = document.getElementsByClassName(_input.getAttribute('data-table'));
			Arr.forEach.call(tables, function(table) {
				Arr.forEach.call(table.tBodies, function(tbody) {
					Arr.forEach.call(tbody.rows, _filter);
				});
			});
		}

		function _filter(row) {
			var text = row.textContent.toLowerCase(), val = _input.value.toLowerCase();
			row.style.display = text.indexOf(val) === -1 ? 'none' : 'table-row';
		}

		return {
			init: function() {
				var inputs = document.getElementsByClassName('light-table-filter');
				Arr.forEach.call(inputs, function(input) {
					input.oninput = _onInputEvent;
				});
			}
		};
	})(Array.prototype);

	document.addEventListener('readystatechange', function() {
		if (document.readyState === 'complete') {
			LightTableFilter.init();
		}
	});

})(document);
