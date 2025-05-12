//card animation about us
AOS.init({
    duration: 1000,
    once: true
   });
   //card animation about us end
   
   //animation about us photo
      
       const observer = new IntersectionObserver((entries) => {
          entries.forEach(entry => {
            if (entry.isIntersecting) {
               entry.target.classList.add('visible');
            }
           });
       });
       document.querySelectorAll('.animate-on-scroll').forEach(el => observer.observe(el));
   //animation about us photo end

   // donate-script.js
   
   const donationButtons = document.querySelectorAll('.donation-type-btn');
   const donationSections = document.querySelectorAll('.donation-section');
   
   // Function to toggle donation sections
   function toggleDonationSection(type) {
     donationButtons.forEach(btn => btn.classList.remove('active'));
     donationSections.forEach(sec => sec.style.display = 'none');
   
     const targetSection = document.getElementById(type);
     if (targetSection) {
       targetSection.style.display = 'block';
     }
   }
   
   // Function to handle cloning and modification of the form
   function handleFormClone(type) {
     const monthlyForm = document.querySelector('#monthly .donation-form-content').cloneNode(true);
   
     const targetSection = document.getElementById(type);
     targetSection.innerHTML = '';
     targetSection.appendChild(monthlyForm);
   
     if (type === 'general') {
       const purposeField = targetSection.querySelector('.purpose-field');
       if (purposeField) purposeField.remove();
     }
   
     handlePaymentToggle(targetSection);
     handleAmountSelection(targetSection);
   }
   
   // Handle Payment Method Toggle
   function handlePaymentToggle(section) {
     const methodSelect = section.querySelector('.payment-method');
     const paypalInfo = section.querySelector('.paypal-info');
     const ccpInfo = section.querySelector('.ccp-info');
     const bankInfo = section.querySelector('.bank-info');
   
     paypalInfo.style.display = 'none';
     ccpInfo.style.display = 'none';
     bankInfo.style.display = 'none';
   
     methodSelect.addEventListener('change', function () {
       paypalInfo.style.display = 'none';
       ccpInfo.style.display = 'none';
       bankInfo.style.display = 'none';
   
       if (this.value === 'paypal') {
         paypalInfo.style.display = 'block';
       } else if (this.value === 'ccp') {
         ccpInfo.style.display = 'block';
       } else if (this.value === 'bank') {
         bankInfo.style.display = 'block';
       }
     });
   }
   
   // Handle Amount Selection
   function handleAmountSelection(section) {
     const amountButtons = section.querySelectorAll('.amount-btn');
     const customInput = section.querySelector('.custom-amount-input');
   
     amountButtons.forEach(button => {
       button.addEventListener('click', () => {
         const amount = button.getAttribute('data-amount');
         customInput.value = amount;
         amountButtons.forEach(b => b.classList.remove('selected'));
         button.classList.add('selected');
       });
     });
   }
   
   // Event Listener for Donation Buttons
   
   donationButtons.forEach(btn => {
     btn.addEventListener('click', () => {
       const type = btn.dataset.type;
   
       btn.classList.add('active');
       toggleDonationSection(type);
       handleFormClone(type);
     });
   });
   // Initialize Monthly Section
   // Remove all sections initially
     donationSections.forEach(sec => sec.style.display = 'none');






//donation in algeria//
     document.addEventListener("DOMContentLoaded", () => {
  const donationButtons = document.querySelectorAll(".donation-type-btn");
  const donationSections = document.querySelectorAll(".donation-section");

  function toggleDonationSection(type) {
    donationSections.forEach(section => (section.style.display = "none"));
    const targetSection = document.getElementById(type);
    if (targetSection) targetSection.style.display = "block";
  }

  function handlePaymentToggle(section) {
    const methodSelect = section.querySelector("#payment-method");
    const ccpInfo = section.querySelector("#ccp-info");
    const bankInfo = section.querySelector("#bank-info");
    if (methodSelect) {
      ccpInfo && (ccpInfo.style.display = "none");
      bankInfo && (bankInfo.style.display = "none");
      methodSelect.addEventListener("change", () => {
        ccpInfo && (ccpInfo.style.display = "none");
        bankInfo && (bankInfo.style.display = "none");
        if (methodSelect.value === "ccp") ccpInfo.style.display = "block";
        else if (methodSelect.value === "bank") bankInfo.style.display = "block";
      });
    }
  }

  function handleAmountSelection(section) {
    const amountButtons = section.querySelectorAll(".amount-btn");
    const customInput = section.querySelector(".custom-amount-input");
    if (amountButtons && customInput) {
      amountButtons.forEach(button => {
        button.addEventListener("click", () => {
          customInput.value = button.dataset.amount;
          amountButtons.forEach(b => b.classList.remove("selected"));
          button.classList.add("selected");
        });
      });
    }
  }

  donationButtons.forEach(button => {
    button.addEventListener("click", () => {
      const type = button.dataset.type;
      donationButtons.forEach(btn => btn.classList.remove("active"));
      button.classList.add("active");
      toggleDonationSection(type);
      const section = document.getElementById(type);
      if (section) {
        handlePaymentToggle(section);
        handleAmountSelection(section);
      }
    });
  });

  donationSections.forEach(section => (section.style.display = "none"));
});