document.addEventListener("DOMContentLoaded", function () {
  // Mapping form fields to preview elements
  const fields = {
    recipient_name: ["preview_recipient_name", "preview_recipient_name_alt"],
    your_name: ["preview_name", "preview_name_alt"],
    your_address: "preview_address",
    city_state_zip: "preview_city_state_zip",
    phone_number: "preview_phone",
    email_address: "preview_email",
    website: "preview_website",
    date: "preview_date",
    recipient_title: "preview_recipient_title",
    company_name: "preview_company_name",
    company_address: "preview_company_address",
    company_city_state_zip: "preview_company_city_state_zip", // Corrected preview element ID
    your_title: "preview_your_title",
  };

  // Update preview based on input
  Object.keys(fields).forEach(function (fieldId) {
    const field = document.getElementById(fieldId);
    const previewElementIds = fields[fieldId];

    if (!field) {
      console.error(`Field with ID '${fieldId}' not found.`);
      return;
    }

    field.addEventListener("input", function () {
      const value = field.value || field.getAttribute("placeholder");
      console.log(`Updating previews for '${fieldId}' with value: ${value}`);

      if (Array.isArray(previewElementIds)) {
        previewElementIds.forEach(function (previewElementId) {
          const previewElement = document.getElementById(previewElementId);
          if (previewElement) {
            previewElement.textContent = value;
          } else {
            console.error(
              `Preview element with ID '${previewElementId}' not found.`
            );
          }
        });
      } else {
        const previewElement = document.getElementById(previewElementIds);
        if (previewElement) {
          previewElement.textContent = value;
        } else {
          console.error(
            `Preview element with ID '${previewElementIds}' not found.`
          );
        }
      }
    });

    // Initial update of previews
    const initialValue = field.value || field.getAttribute("placeholder");
    console.log(`Initial value for '${fieldId}': ${initialValue}`);
    if (Array.isArray(previewElementIds)) {
      previewElementIds.forEach(function (previewElementId) {
        const previewElement = document.getElementById(previewElementId);
        if (previewElement) {
          previewElement.textContent = initialValue;
        }
      });
    } else {
      const previewElement = document.getElementById(previewElementIds);
      if (previewElement) {
        previewElement.textContent = initialValue;
      }
    }
  });
});

 // data using ajax
// document.addEventListener("DOMContentLoaded", function () {
//   const form = document.getElementById("coverLetterForm");

//   if (form) {
//     form.addEventListener("submit", function (event) {
//       event.preventDefault(); // Prevent the default form submission

//       const formData = new FormData(form);
//       fetch("/core/save_form_data/", {
//         method: "POST",
//         body: formData,
//         headers: {
//           "X-CSRFToken": document.querySelector("[name=csrfmiddlewaretoken]")
//             .value,
//         },
//       })
//         .then((response) => response.json())
//         .then((data) => {
//           if (data.status === "success") {
            // Log a success message
//             console.log("Form data saved successfully");

            // Open the PDF in a new tab
//             window.open("/core/download_pdf/", "_blank");
//           } else {
//             console.error("Failed to save form data");
//           }
//         })
//         .catch((error) => console.error("Error:", error));
//     });
//   } else {
//     console.error("Form with ID 'coverLetterForm' not found.");
//   }
// });


// userprofile page
function toggleEdit() {
    const form = document.getElementById('profile-form');
    const editButton = document.getElementById('edit-button');
    form.classList.toggle('hidden');
    editButton.classList.toggle('hidden');
}


    document.addEventListener("DOMContentLoaded", function () {
        const deleteForms = document.querySelectorAll('form[action*="delete_template"]');

        deleteForms.forEach(form => {
            form.addEventListener('submit', function (event) {
                if (!confirm('Are you sure you want to delete this template?')) {
                    event.preventDefault();
                }
            });
        });
    });

    // <!-- JavaScript to handle visibility -->
    
    document.addEventListener('DOMContentLoaded', function() {
        var seeAllBtn = document.getElementById('see-all-btn');
        var allTemplatesDiv = document.getElementById('all-templates');

        seeAllBtn.addEventListener('click', function() {
            allTemplatesDiv.classList.toggle('hidden');
            seeAllBtn.textContent = allTemplatesDiv.classList.contains('hidden') ? 'See All Templates' : 'Hide All Templates';
        });
    });