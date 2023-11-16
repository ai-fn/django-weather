if (!localStorage.getItem('unit'))
    localStorage.setItem('unit', 'metric')

function loadMap(){
    var map = new Microsoft.Maps.Map('#map', {
        credentials: 'AsOdC9M6GAxnToMiAe68sKys6SgTPhStjJVg0qMtlK_NNX3ympcK9Wix_WnqZn5j'
    });

    map.setView({
        center: new Microsoft.Maps.Location({{cw.location.lat}}, {{cw.location.lon}}),
        zoom: 12
    });
}

function changeData() {
    var allTempDataElems = document.querySelectorAll('.temp-data')
    var allSpeedDataElems = document.querySelectorAll('.speed-data')
    var allTempSymbolElems = document.querySelectorAll('.temp-symbol')
    var allSpeedSymbolElems = document.querySelectorAll('.speed-symbol')
    if (localStorage.getItem('unit') == 'metric') {
        allTempDataElems.forEach(el => {
            el.textContent = (parseFloat(el.textContent) * 1.8 + 32).toFixed(1)
        })
        allTempSymbolElems.forEach(el => {
            el.textContent = "°F";
        })
        allSpeedDataElems.forEach(el => {
            el.textContent = (parseFloat(el.textContent) * 2.237).toFixed(1)
        })
        allSpeedSymbolElems.forEach(el => {
            el.textContent = 'm/h'
        })
        localStorage.unit = 'imperial';
    }
    else {
        allTempDataElems.forEach(el => {
            el.textContent = ((parseFloat(el.textContent) - 32) / 1.8).toFixed(1)
        })
        allTempSymbolElems.forEach(el => {
            el.textContent = "°C";
        })
        allSpeedSymbolElems.forEach(el => {
            el.textContent = 'm/s'
        })
        allSpeedDataElems.forEach(el => {
            el.textContent = (parseFloat(el.textContent) * 0.447).toFixed(1)
        })
        localStorage.unit = 'metric';
    }
}