
// Chargement des observateurs depuis le fichier JSON généré à partir d'Excel
let observateursMap = {};

function normaliserNumero(num) {
  if (!num) return "";
  let digits = String(num).replace(/[^0-9]/g, "");
  if (digits.length >= 9) {
    return digits.slice(-9); // conserve les 9 derniers chiffres
  }
  return digits;
}

document.addEventListener("DOMContentLoaded", () => {
  const checkBtn = document.getElementById('checkBtn');
  const phoneInput = document.getElementById('phone');
  const resultEl = document.getElementById('result');
  const notFoundEl = document.getElementById('notFound');
  const errorBox = document.getElementById('errorBox');
  const message = document.getElementById('message');

  // Charger la base JSON
  fetch('observateurs.json')
    .then(res => {
      if (!res.ok) throw new Error("Impossible de charger observateurs.json");
      return res.json();
    })
    .then(data => {
      observateursMap = data || {};
      console.log("Base observateurs chargée :", Object.keys(observateursMap).length, "numéros.");
    })
    .catch(err => {
      console.error(err);
      errorBox.style.display = 'block';
      errorBox.textContent = "Erreur lors du chargement de la base des observateurs : " + err.message;
    });

  function resetViews(){
    resultEl.style.display = 'none';
    notFoundEl.style.display = 'none';
    errorBox.style.display = 'none';
    message.textContent = '';
  }

  function renderSuccess(data){
    const photoPath = data.photo_filename ? ("images/" + data.photo_filename) : "https://via.placeholder.com/400x400?text=Photo";
    document.getElementById('photo').src = photoPath;
    document.getElementById('fullname').textContent = (data.nom || "") + " " + (data.prenom || "");
    document.getElementById('commune').textContent = data.commune || '-';
    document.getElementById('phoneOut').textContent = data.telephone_affiche || '-';
    document.getElementById('obsId').textContent = data.id || '-';

    const statusBox = document.getElementById('statusBox');
    const successText = document.getElementById('successText');

    statusBox.textContent = "Félicitations — Retenu";
    successText.textContent = "Félicitations, vous avez été retenu comme Observateur Domestique du CNOSCG pour la Commune de " + (data.commune || '') + ".";

    resultEl.style.display = 'flex';
    window.scrollTo({top: resultEl.offsetTop - 20, behavior:'smooth'});
  }

  function renderNotFound(){
    notFoundEl.style.display = 'block';
    window.scrollTo({top: notFoundEl.offsetTop - 20, behavior:'smooth'});
  }

  checkBtn.addEventListener('click', () => {
    resetViews();
    const rawPhone = phoneInput.value.trim();
    if(!rawPhone){
      message.textContent = 'Veuillez entrer un numéro de téléphone valide.';
      return;
    }
    const normalized = normaliserNumero(rawPhone);
    if(!normalized){
      message.textContent = 'Numéro invalide.';
      return;
    }

    message.textContent = 'Recherche en cours...';

    // recherche dans la base JSON
    const found = observateursMap[normalized];
    if(found){
      message.textContent = '';
      // ajouter le téléphone pour affichage
      found.telephone_affiche = rawPhone;
      renderSuccess(found);
    } else {
      message.textContent = '';
      renderNotFound();
    }
  });

  phoneInput.addEventListener('keyup', (e) => {
    if(e.key === 'Enter') checkBtn.click();
  });
});


// Défilement automatique du carrousel de l'équipe de coordination
setInterval(() => {
  const carousel = document.getElementById("teamCarousel");
  if (carousel) {
    const scrollAmount = 260;
    carousel.scrollBy({ left: scrollAmount, behavior: 'smooth' });

    if (carousel.scrollLeft + carousel.clientWidth >= carousel.scrollWidth - 5) {
      // retour au début
      setTimeout(() => {
        carousel.scrollTo({ left: 0, behavior: 'smooth' });
      }, 1000);
    }
  }
}, 3500);
