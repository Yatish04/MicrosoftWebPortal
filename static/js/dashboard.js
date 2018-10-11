function crop(){
    var dom=document.getElementById("crop");
    dom.style.display="block";
    var dom2= document.getElementById("land");
    dom2.style.display="none";
    var dom3 = document.getElementById("cards")
    dom3.style.display="none";
}


function land(){
    var dom=document.getElementById("land");
    dom.style.display="block";
    var dom2= document.getElementById("crop");
    dom2.style.display="none";
    var dom3 = document.getElementById("cards")
    dom3.style.display="none";
}

function Get(yourUrl){
    var Httpreq = new XMLHttpRequest(); // a new request
    Httpreq.open("GET",yourUrl,false);
    Httpreq.send(null);
    return Httpreq.responseText;          
}

window.onload = function(){
	//var json_obj = JSON.parse(Get("https://rvngo.azurewebsites.net/ngo/resources"));
	var json_obj = JSON.parse(Get("http://127.0.0.1:8080/ngo/resources"));
	console.log("this is the author name: "+json_obj.data);
	var doms = this.document.getElementById("replace").innerHTML = json_obj.data
}

function dashboard()
{
    var dom=document.getElementById("land");
    dom.style.display="none";
    var dom2= document.getElementById("crop");
    dom2.style.display="none";
    var dom3 = document.getElementById("cards")
    dom3.style.display="block";
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
