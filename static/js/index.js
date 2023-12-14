var temp = 'metric';
if (!localStorage.getItem('unit')) {
    localStorage.setItem('unit', 'metric')
}

function changeData(objIn = undefined) {

    if (!objIn)
        objIn = document
    var allTempDataElems = objIn.querySelectorAll('.temp-data')
    var allSpeedDataElems = objIn.querySelectorAll('.speed-data')
    var allTempSymbolElems = objIn.querySelectorAll('.temp-symbol')
    var allSpeedSymbolElems = objIn.querySelectorAll('.speed-symbol')

    if (objIn != document && temp == 'imperial') {
        toImperial()
        return
    }
    else if (objIn != document)
        return

    switch (temp) {
        case 'imperial':
            toMetric();
            temp = 'metric';
            break;
        case 'metric':
            toImperial();
            temp = 'imperial';
            break;
    }
    return

    function toImperial () {
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
    }
    function toMetric() {
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
    }
}