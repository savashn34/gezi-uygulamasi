function dizinBelirt(goster, element) {
    if (goster) {
        element.classList.add("tr-hover");
    } else {
        element.classList.remove("tr-hover");
    }
}

document.addEventListener("DOMContentLoaded", function() {
    var radios = document.querySelectorAll('input[type="radio"]');
    
    radios.forEach(function(radio) {
      radio.addEventListener("change", function() {
        radios.forEach(function(otherRadio) {
          if (otherRadio.name !== radio.name) {
            otherRadio.checked = false;
          }
        });
      });
    });
});
  
function openNav() {
    document.getElementById("sidebarNav").style.width = "250px";
    document.getElementById("main").style.marginRight = "250px"; // BURASI DOLAŞIM AÇILDIĞINDA MAIN ALANINDAKİ İÇERİĞİ SAĞA KAYDIRIR
    document.body.style.background = "rgba(0,0,0,0.4)";
}
  
function closeNav() {
    document.getElementById("sidebarNav").style.width = "0";
    document.getElementById("main").style.marginRight = "0"; // BURASI KAYDIRILAN ANA İÇERİĞİ DOLAŞIM GERİ KAPATILDIĞINDA GERİ ESKİ YERİNE GETİRİR.
    document.body.style.background = "";
}