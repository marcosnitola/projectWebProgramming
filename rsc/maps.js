function initMaps() {
	let mapsContainer = document.getElementById('maps');
	let mapProp = {
		center: new google.maps.LatLng(7.1192899,-73.1679977),
		zoom: 13
	};
	let map = new google.maps.Map(mapsContainer, mapProp);

	let marker = new google.maps.Marker({position: new google.maps.LatLng(7.131997096497364, -73.12951026387405)});
	marker.setMap(map);
}
