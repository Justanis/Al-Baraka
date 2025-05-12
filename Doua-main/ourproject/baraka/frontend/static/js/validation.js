// helpers.js

function isValidEmail(email) {
  const regex = /^[^\s@]+@[^\s@]+\.[^\s@]+$/;
  return regex.test(email);
}

function isValidUsername(userName) {
  return typeof userName === 'string' && userName.trim().length >= 3;
}

function isValidPassword(password) {
  return typeof password === 'string' && password.length >= 6;
}

// Flexible validator
function validateUserData(userData) {
  const errors = [];

  if ('userName' in userData) {
    if (!isValidUsername(userData.userName)) {
      errors.push("Invalid username: must be at least 3 characters long.");
    }
  }

  if ('email' in userData) {
    if (!isValidEmail(userData.email)) {
      errors.push("Invalid email address.");
    }
  }

  if ('password' in userData) {
    if (!isValidPassword(userData.password)) {
      errors.push("Invalid password: must be at least 6 characters long.");
    }
  }

  return {
    isValid: errors.length === 0,
    errors: errors
  };
}
