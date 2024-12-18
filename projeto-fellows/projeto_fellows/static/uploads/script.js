document.addEventListener('DOMContentLoaded', function () {
    const registerForm = document.getElementById('registerForm');

    registerForm.addEventListener('submit', function (event) {
        event.preventDefault();

        const userType = document.querySelector('input[name="type"]:checked').value;

        if (userType === 'fisica') {
            document.querySelector('.modal').classList.remove('hidden');
            document.body.classList.add('modal-active');
        } else if (userType === 'juridica') {
            window.location.href = 'cadastro-juridica.html';
        }
    });

    document.querySelector('.btn-back').addEventListener('click', function () {
        document.querySelector('.modal').classList.add('hidden');
        document.body.classList.remove('modal-active');
    });
});