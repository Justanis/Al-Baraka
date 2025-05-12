    
    const loginlink = document.querySelector('.login-link');
    const registerlink = document.querySelector('.register-link');
    registerlink.addEventListener('click', () =>{
        registerlink.classList.add('active');
    });
    loginlink.addEventListener('click', () =>{
        loginlink.classList.remove('active');
    });

    