// card animation about us
AOS.init({
  duration: 1000,
  once: true
});

// animation about us photo
const observer = new IntersectionObserver(entries => {
  entries.forEach(entry => {
    if (entry.isIntersecting) entry.target.classList.add('visible');
  });
});
document.querySelectorAll('.animate-on-scroll').forEach(el => observer.observe(el));


// donation toggle logic for both “in” and “out”
function initDonationGroup(suffix) {
  const btnClass     = `.donation-type-btn-${suffix}`;    // .donation-type-btn-in / -out
  const sectionClass = `.donation-section-${suffix}`;     // .donation-section-in / -out

  const $buttons  = $(btnClass);
  const $sections = $(sectionClass);

  $sections.hide();
  $buttons.on('click', function() {
    const type     = $(this).data('type');               // monthly / directed / general
    const targetId = `#${type}-${suffix}`;
    const $target  = $(targetId);

    $buttons.removeClass('active');
    $(this).addClass('active');

    $sections.hide();
    if (!$target.length) return;

    $target.show();
    $('html, body').animate({ scrollTop: $target.offset().top }, 400);
  });
}


// delegate payment-method changes
$(document).on('change', 'select.payment-method', function() {
  const $form = $(this).closest('form');
  $form.find('.payment-info').hide();

  const v = this.value.toLowerCase();
  if (v === 'paypal') {
    $form.find('.paypal-info').show();
  } else if (v === 'ccp') {
    $form.find('.ccp-info').show();
  } else if (v === 'bank' || v === 'bank transfer' || v === 'bank card') {
    $form.find('.bank-info').show();
  }
});

// delegate amount-button clicks
$(document).on('click', '.amount-btn', function(e) {
  e.preventDefault();
  const amount = $(this).data('amount');
  const $form = $(this).closest('form');
  $form.find('.custom-amount-input').val(amount);
  $form.find('.amount-btn').removeClass('selected');
  $(this).addClass('selected');
});


// PDF generation on form submit
$(function() {
  const { jsPDF } = window.jspdf;

    $('form[id^="form-"]').on('submit', function(e) {
      e.preventDefault();
      
      // determine in/out from form ID
      const formId = this.id; // e.g. "form-general-in" or "form-directed-out"
      const isIn    = formId.endsWith('-in');
      const region  = isIn ? 'In Algeria' : 'Out Algeria';
      
      // grab only non‐empty fields
      const entries = $(this).serializeArray()
        .filter(({ value }) => value.trim() !== '');

      const doc = new jsPDF();
      // big title: region + “Donation Receipt”
      doc.setFontSize(18);
      doc.text(`${region} Donation Receipt`, 20, 20);

      // now list the fields
      doc.setFontSize(12);
      let y = 30;
      entries.forEach(({ name, value }) => {
        doc.text(`${name}: ${value}`, 20, y);
        y += 8;
        if (y > 280) {
          doc.addPage();
          y = 20;
        }
      });

      doc.save(`donation_receipt_${region.replace(' ','_').toLowerCase()}_${Date.now()}.pdf`);
    });



  // wire up the in/out groups after DOM ready
  initDonationGroup('in');
  initDonationGroup('out');
});
