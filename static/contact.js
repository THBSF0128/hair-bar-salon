document.getElementById("contact-form").addEventListener("submit", function(e) {
  e.preventDefault();
  document.getElementById("submit-contact").setAttribute("disabled", "disabled");
  submitForm();
});

function submitForm() {
  fetch("https://script.google.com/macros/s/AKfycbwRQDDRNiDrMeZ6NkQ2z_yFGHmC1peRInqFtLX6aL_BGG_XHYdhxTDz40YS5qdT9zcyuw/exec", {
    method: 'POST',
    body: new FormData(document.getElementById("contact-form")),
    mode: 'no-cors'
  })
  .then(response => {
    if (response.status == 0) {
      document.getElementById("form-message").innerHTML = "Form submitted successfully!";
    } else {
      document.getElementById("form-message").innerHTML = "Error submitting form!";
      document.getElementById("submit-contact").removeAttribute("disabled");
    }
  })
  .catch(error => {
    console.error(error);  // Log errors to console for debugging
    document.getElementById("form-message").innerHTML = "An error occurred!";
    document.getElementById("submit-contact").removeAttribute("disabled");
  });
}