function initMaps() {
	let mapsContainer = document.getElementById('maps');
	let mapProp = {
		center: new google.maps.LatLng(7.1192899,-73.1679977),
		zoom: 13
	};
	let map = new google.maps.Map(mapsContainer, mapProp);
}
