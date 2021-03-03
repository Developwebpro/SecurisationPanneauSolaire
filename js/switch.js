document.addEventListener('DOMContentLoaded', function () {
  var checkbox = document.querySelector('input[type="checkbox"]');

  checkbox.addEventListener('change', function () {
    if (checkbox.checked) {
      // do this
      console.log('Sécurisé');
        document.getElementById("etatSwitch").innerHTML = "Sécurisé";
        document.getElementById("txtSitu").style.display = "none";
        document.getElementById("manuel").style.display = "none";
        document.getElementById("automatique").style.display = "none";
    } else {
      // do that
      console.log('Non sécurisé');
        document.getElementById("etatSwitch").innerHTML = "Non sécurisé";
        document.getElementById("txtSitu").style.display = "initial";
        document.getElementById("manuel").style.display = "initial";
        document.getElementById("automatique").style.display = "initial";        
    }
  });
});