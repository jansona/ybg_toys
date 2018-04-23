/*
var myHeading = document.querySelector('h1');
myHeading.innerHTML = 'Hello world';
*/

var myImage = document.querySelector('img');

myImage.onclick = function(){
	var mySrc = myImage.getAttribute('src');
	if(mySrc === 'images/violet_evergarden.jpg'){
		myImage.setAttribute('src', 'images/violet_evergarden2.png');
	}
	else{
		myImage.setAttribute('src', 'images/violet_evergarden.jpg');
	}
}

var myButton = document.querySelector('button');
var myHeading = document.querySelector('h1');

myButton.onclick = function(){
	setUserName();
}

function setUserName(){
	var myName = prompt('please enter your name:');
	localStorage.setItem('master', myName);
	myHeading.innerHTML = myName + ' loves violet violet_evergarden';
}

if(!localStorage.getItem('master')){
	setUserName();
}
else{
	myHeading.innerHTML = localStorage.getItem('master') + ' loves violet evergarden';
}