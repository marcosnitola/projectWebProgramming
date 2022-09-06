function initMaps() {
	let mapsContainer = document.getElementById('maps');
	let mapProp = {
		center: new google.maps.LatLng(7.1192899,-73.1679977),
		zoom: 13
	};
	let map = new google.maps.Map(mapsContainer, mapProp);

  let varMarkers = [
    {coordenadas:{x: 7.131997096497364, y:  -73.12951026387405}},
    {coordenadas:{x: 7.100485, y: -73.110294 }},
    {coordenadas:{x: 7.095799, y: -73.1070867}},
    {coordenadas:{x: 7.104620, y: -73.113765 }},
    {coordenadas:{x: 7.096950, y: -73.118161 }},
    {coordenadas:{x: 7.085965, y: -73.113150 }},
    {coordenadas:{x: 7.077885, y: -73.109574 }},
    {coordenadas:{x: 7.073563, y: -73.112921 }},
    {coordenadas:{x: 7.071689, y: -73.103394 }},
    {coordenadas:{x: 7.067191, y: -73.105799 }},
    {coordenadas:{x: 7.063859, y: -73.100209 }}
  ];
	// let marker = new google.maps.Marker({position: new google.maps.LatLng(7.131997096497364, -73.12951026387405)});
	// marker.setMap(map);
  for (let i = 0; i < varMarkers.length; i++){
    marker = new google.maps.Marker({
      position: new google.maps.LatLng(varMarkers[i].coordenadas.x, varMarkers[i].coordenadas.y)
    });
    marker.setMap(map);
  }
}
