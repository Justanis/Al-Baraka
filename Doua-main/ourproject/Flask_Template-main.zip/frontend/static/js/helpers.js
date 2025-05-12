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

  function logOut(){
    localStorage.removeItem("user");
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
  