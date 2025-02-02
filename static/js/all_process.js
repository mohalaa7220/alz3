const results = document.getElementById("data_display");
const loader = document.getElementById("loader");

// Function to show loader
function showLoader() {
  loader.style.display = "block";
}

// Function to hide loader
function hideLoader() {
  loader.style.display = "none";
}

// Show loader initially
showLoader();

axios
  .get("https://alz-texg.onrender.com/api/all_process_image/")
  .then((response) => {
    const imageData = response.data;

    hideLoader();

    imageData.forEach((item) => {
      results.innerHTML += `
        <div class="col-4">
          <div class="card card-product">
            <!-- top-card -->
            <div class="top-card">
              <img src="${item.image_url}" class="card-img-top" alt="1" />
            </div>
            <div class="card-body">
              <h5 class="card-title">result: ${item.result}</h5>
              <h5 class="card-title"> confidence score: ${item.confidence_score}</h5>
            </div>
          </div>
        </div>
      `;
    });
  })
  .catch((error) => {
    console.error("Error:", error);
    hideLoader();
  });
