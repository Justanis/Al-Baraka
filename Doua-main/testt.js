const loginBox = document.querySelector('.login-box');
const registerBox = document.querySelector('.register-box');
const switchToRegister = document.querySelector('.switch-to-register');
const switchToLogin = document.querySelector('.switch-to-login');

switchToRegister.addEventListener('click', () => {
    loginBox.classList.remove('active');
    registerBox.classList.add('active');
});

switchToLogin.addEventListener('click', () => {
    registerBox.classList.remove('active');
    loginBox.classList.add('active');
});
