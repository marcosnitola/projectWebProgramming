const menuURL = 'rsc/menu.json';

const request = new XMLHttpRequest();
request.open('GET', menuURL);
request.responseType = 'json';
request.send();
request.onload  = function () {
	const menuDB = request.response;
	console.log('Funcionó?'+menuDB);
}
