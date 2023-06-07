var formulario = document.getElementById('formulario');

addEventListener('input', formatInput)

function formatInput() {
    var tel = document.getElementById('numero');
    var valor = tel.value;

    valor = valor.replace(/\D/g, '');
    valor = valor.replace(/^(\d{2})(\d{4})(\d{1,4}).*/, '($1) $2-$3');

    tel.value = valor;

    var senha = document.getElementById('password');
    var conSenha = document.getElementById('confirmPassword');

    if (senha.value != conSenha.value || senha.value == '' || conSenha.value == '') {
        senha.style.border = '2px solid red';
        conSenha.style.border = '2px solid red';
    }else {
        senha.style.border = '2px solid green';
        conSenha.style.border = '2px solid green';
    }
}

function visu(input) {
    var input = document.getElementById(input);
    if (input.type == 'password') {
        input.type = 'text';
    }else {
        input.type = 'password';
    }

} 