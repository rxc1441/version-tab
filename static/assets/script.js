document.addEventListener('DOMContentLoaded', () => {
    const textPromptInput = document.getElementById('textPrompt');
    const imageUploadInput = document.getElementById('imageUpload');
    const submitButton = document.getElementById('submitBtn');
    const responseOutput = document.getElementById('responseOutput');

    submitButton.addEventListener('click', async () => {
        const text = textPromptInput.value.trim();
        const imageFile = imageUploadInput.files[0];

        if (!text && !imageFile) {
            responseOutput.textContent = "Please enter some text or upload an image.";
            responseOutput.classList.add('error');
            return;
        }

        responseOutput.textContent = 'Thinking...';
        responseOutput.classList.remove('error');

        try {
            let apiUrl = '';
            let formData = new FormData();

            if (imageFile) {
                // Multimodal request (text + image)
                apiUrl = '/generate_multimodal/'; // Relative path, FastAPI serves on same host/port
                formData.append('prompt', text);
                formData.append('image', imageFile);
            } else {
                // Text-only request
                apiUrl = '/generate_text/'; // Relative path
                formData.append('text', text); // For JSON body
            }

            const fetchOptions = {
                method: 'POST',
            };

            if (imageFile) {
                // For multimodal, FormData automatically sets 'Content-Type': 'multipart/form-data'
                fetchOptions.body = formData;
            } else {
                // For text-only, send JSON
                fetchOptions.headers = {
                    'Content-Type': 'application/json'
                };
                fetchOptions.body = JSON.stringify({ text: text });
            }

            const response = await fetch(apiUrl, fetchOptions);

            if (!response.ok) {
                const errorData = await response.json();
                throw new Error(errorData.detail || `HTTP error! Status: ${response.status}`);
            }

            const data = await response.json();
            responseOutput.textContent = data.response;

        } catch (error) {
            console.error('Error:', error);
            responseOutput.textContent = `Error: ${error.message}`;
            responseOutput.classList.add('error');
        }
    });
});
