document.addEventListener('DOMContentLoaded', function() {
    const accordionHeaders = document.querySelectorAll('.accordion-header');

    accordionHeaders.forEach((header) => {
        header.addEventListener('click', () => {
            const accordionContent = header.nextElementSibling;
            const arrow = header.querySelector('.arrow');
            
            accordionHeaders.forEach((otherHeader) => {
                if (otherHeader !== header) {
                    otherHeader.nextElementSibling.classList.remove('show');
                    otherHeader.classList.remove('active');
                }
            });

            accordionContent.classList.toggle('show');
            header.classList.toggle('active');
            arrow.classList.toggle('active');
        });
    });
});



// Mengambil data dari API
fetch('https://eb00-103-129-95-233.ngrok-free.app/api/profiles/') // Ganti dengan URL ngrok Anda
    .then(response => response.json())
    .then(data => {
        console.log(data); // Tampilkan data di konsol
    })
    .catch(error => {
        console.error('Error:', error);
    });

// Mengirim data ke API
const newUserProfile = {
    username: 'new_user',
    score: 100,
    // Tambahkan field lain sesuai model
};

fetch('https://eb00-103-129-95-233.ngrok-free.app/api/profiles/', { // Ganti dengan URL ngrok Anda
    method: 'POST',
    headers: {
        'Content-Type': 'application/json',
        // Sertakan token CSRF jika diperlukan
    },
    body: JSON.stringify(newUserProfile)
})
.then(response => response.json())
.then(data => {
    console.log('Success:', data);
})
.catch(error => {
    console.error('Error:', error);
});