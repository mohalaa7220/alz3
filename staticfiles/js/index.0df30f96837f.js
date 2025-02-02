const uploadUrl = "/process-image/";
const uploadBtn = document.getElementById("uploadBtn");
const fileInput = document.getElementById("fileInput");
const csrfToken = document.querySelector("[name=csrfmiddlewaretoken]").value;
const loader = document.getElementById("overlay");
const resultsDiv = document.getElementById("results");

// Function to show loader
function showLoader() {
  loader.style.display = "flex";
}

// Function to hide loader
function hideLoader() {
  loader.style.display = "none";
}

hideLoader();

uploadBtn.addEventListener("click", function () {
  fileInput.click();
});

fileInput.addEventListener("change", function (event) {
  const file = event.target.files[0];
  if (!file) return;

  let formData = new FormData();
  formData.append("image", file);

  // Show loading indicator
  showLoader();

  resultsDiv.innerHTML = ""; // Clear previous results

  // Send AJAX request to backend
  fetch(uploadUrl, {
    method: "POST",
    body: formData,
    headers: {
      "X-CSRFToken": csrfToken,
    },
  })
    .then((response) => response.json())
    .then((data) => {
      // Hide the loading indicator
      hideLoader();

      if (data.error) {
        resultsDiv.innerHTML = `<p style="color:red;">${data.error}</p>`;
      } else {
        resultsDiv.innerHTML = `
          <p><strong>Result:</strong> ${data.result}</p>
          <p><strong>Confidence Score:</strong> ${data.confidence_score.toFixed(
            2
          )}</p>
          <img src="${data.image_url}" width="200" alt="Processed Image">
        `;
      }
    })
    .catch((error) => {
      // Hide the loading indicator if there's an error
      hideLoader();

      console.log(error);
      resultsDiv.innerHTML = `<p style="color:red;">Error processing image.</p>`;
    });
});
