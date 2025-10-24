
// Client-side validation and 'redirect' logic for the contact form.
document.addEventListener('DOMContentLoaded', () => {
  const form = document.getElementById('contactForm');
  if (!form) return;

  const showErr = (id, msg) => {
    const small = form.querySelector(`small[data-for="${id}"]`);
    if (small) small.textContent = msg || '';
  };

  const clearErrors = () => {
    ['firstName','lastName','email','password','confirmPassword'].forEach(id => showErr(id,''));
  };

  form.addEventListener('submit', (e) => {
    e.preventDefault();
    clearErrors();
    let ok = true;

    const firstName = form.firstName.value.trim();
    const lastName = form.lastName.value.trim();
    const email = form.email.value.trim();
    const password = form.password.value;
    const confirmPassword = form.confirmPassword.value;

    if (firstName.length < 2) { showErr('firstName','Please enter your first name (2+ characters).'); ok = false; }
    if (lastName.length < 2) { showErr('lastName','Please enter your last name (2+ characters).'); ok = false; }

    const emailOk = form.email.checkValidity();
    if (!emailOk) { showErr('email','Please enter a valid email address.'); ok = false; }

    if (password.length < 8) { showErr('password','Password must be at least 8 characters.'); ok = false; }
    else if (!/(?=.*\d)/.test(password)) { showErr('password','Include at least one number.'); ok = false; }

    if (confirmPassword !== password) { showErr('confirmPassword','Passwords must match.'); ok = false; }

    if (ok) {
      const payload = new URLSearchParams({ firstName, lastName, email });
      window.location.href = `thankyou.html?${payload.toString()}`;
    }
  });
});
