document.addEventListener("DOMContentLoaded", function () {
    // Inicializar el mapa con una ubicación y zoom predeterminado
    var map = L.map('map').setView([19.4326, -99.1332], 13); // CDMX como ejemplo

    // Agregar capa base del mapa (si esta línea falla, el mapa no se verá)
    L.tileLayer('https://{s}.tile.openstreetmap.org/{z}/{x}/{y}.png', {
        attribution: '&copy; OpenStreetMap contributors'
    }).addTo(map);
});

// Simulación de puntos en distintas categorías
const puntos = [
    { lat: 19.4326, lng: -99.1332, categoria: "cat1" }, // Comercio
    { lat: 19.4285, lng: -99.1276, categoria: "cat2" }, // Industria
    { lat: 19.4253, lng: -99.1400, categoria: "cat3" }, // Salud
    { lat: 19.4382, lng: -99.1455, categoria: "cat4" }  // Educación
];

// Diccionario de colores según la categoría
const colores = {
    "cat1": "blue",
    "cat2": "red",
    "cat3": "green",
    "cat4": "purple"
};

// Mapa de marcadores
let marcadores = [];

// Manejo de selección de categorías
document.querySelectorAll("#categorias input").forEach(input => {
    input.addEventListener("change", () => {
        actualizarPuntos();
    });
});

// Función para actualizar los puntos en el mapa según los checkboxes seleccionados
function actualizarPuntos() {
    // Eliminar todos los marcadores actuales
    marcadores.forEach(marcador => map.removeLayer(marcador));
    marcadores = [];

    // Obtener las categorías seleccionadas
    let seleccionadas = [...document.querySelectorAll("#categorias input:checked")]
        .map(input => input.id);

    // Filtrar puntos según la selección y agregarlos al mapa
    puntos.forEach(punto => {
        if (seleccionadas.includes(punto.categoria)) {
            let marcador = L.circleMarker([punto.lat, punto.lng], {
                color: colores[punto.categoria],
                radius: 8
            }).addTo(map);
            marcadores.push(marcador);
        }
    });
}
