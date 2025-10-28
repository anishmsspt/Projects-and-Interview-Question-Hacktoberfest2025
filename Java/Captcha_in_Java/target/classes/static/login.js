document.addEventListener("DOMContentLoaded", function () {
  fetch("api/captcha/generate")
    .then((response) => response.json())
    .then((data) => {
      document.getElementById("captchaImage").src = data.image;
    });
  // fetch("/auth/checkAttempts")
  //     .then(response => response.json())
  //     .then(data => {
  //         if (data.attempts >= 3) {
  //             document.getElementById("captchaDiv").style.display = "block";
  //             document.getElementById("captchaImage").src = "/captcha";
  //         }
  //     });

  document
    .getElementById("loginForm")
    .addEventListener("submit", function (event) {
      event.preventDefault();

      let username = document.getElementById("username").value;
      let password = document.getElementById("password").value;
      let captcha = document.getElementById("captchaInput").value;

      let formData = new URLSearchParams();
      formData.append("username", username);
      formData.append("password", password);
      formData.append("captcha", captcha);

      fetch("api/captcha/validate", {
        method: "POST",
        body: formData,
        headers: { "Content-Type": "application/x-www-form-urlencoded" },
      })
        .then((response) => response.json())
        .then((data) => {
          document.getElementById("message").textContent = data.status;

          if (data.status === "fail") {
            fetch("api/captcha/generate")
              .then((response) => response.json())
              .then((data) => {
                document.getElementById("captchaImage").src = data.image;
              });
          }
        });
    });
});
