
// Redirect to another HTML page
function redirectTo(page) {
  window.location.href = page;
}

// Save user data to localStorage (after login/signup)
function saveUserToLocalStorage(userData) {
  logOut();
  localStorage.setItem('user', JSON.stringify(userData));
}

function getUser() {
  return JSON.parse(localStorage.getItem("user"));
}

// Check if user is logged in
function isAuthenticated() {
  return localStorage.getItem('user') !== null;
}



function isConfirmed(){
  if(getUser().isConfirmed == 0){
      return false
  }else{
      return true
  }
}

function logOut(){
  localStorage.removeItem("user");
}

  function logOut(){
    localStorage.clear();
    window.location.reload();
  }

const donationSectionToggler = (inAlgeria) => {
if(!inAlgeria){
  $("#donation-section-inalgeria").hide();
  $("#donation-section-outalgeria").show();
}else{
  $("#donation-section-inalgeria").show();
  $("#donation-section-outalgeria").hide();
}
}

