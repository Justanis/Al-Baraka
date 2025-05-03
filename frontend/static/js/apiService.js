// apiService.js

// Namespace to encapsulate all API calls
var ApiService = (function () {
  // Base URL of your Flask app
  var baseUrl = 'http://localhost:5000/';

  // Utility function to handle AJAX requests
  function sendRequest(method, endpoint, data, onSuccess, onError) {
    $.ajax({
      url: baseUrl + endpoint,
      type: method,
      data: JSON.stringify(data),
      contentType: 'application/json',
      dataType: 'json',
      success: onSuccess,
      error: onError
    });
  }

  // Public methods
  return {
    // Signup API call
    signup: function (userData, onSuccess, onError) {
      sendRequest('POST', '/users', userData, onSuccess, onError);
    },
    // Login API call
    login: function (userData, onSuccess, onError) {
      sendRequest('POST', '/login', userData, onSuccess, onError);
    },
    // You can add more API methods here if needed
    // For example, fetching user profile or logging out
    confirmEmail : function (userData, onSuccess, onError){
      sendRequest('POST', '/users/confirm', userData, onSuccess, onError)
    }
  };
})();
