var butn = document.getElementById('Go');
var Arry = [0, 1, 2, 5, 8, 7, 6, 3];
var Box = document.getElementsByTagName('li');
var Current = 7;
var Times;


butn.onclick = function(){
	butn.disabled = true;
	Times = Math.floor(Math.random() * 16) + 16;
	var Timer = setInterval (function(){
			if (Times == 0){
				butn.disabled = false;
				clearInterval(Timer);
			}
			Box[Arry[Current]].className = '';
			Current++;
			if (Current == 8){
				Current = 0;
			}
			Box[Arry[Current]].className = 'Chosen';
			Times--;
	}, 200);

	};
