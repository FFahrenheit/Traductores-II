const mainContent = document.getElementById('main');

const validators = [
    {
        'id': 'telefono',
        'label': 'Teléfono de 10 dígitos',
        'regex': /abc/,
        'shortName': 'Teléfono',
        'icon': 'fa fa-phone'
    },
    {
        'id': 'correo',
        'label': 'Teléfono electrónico',
        'regex': /abc/,
        'shortName': 'Correo',
        'icon': 'fa fa-envelope-o'
    },
    {
        'id': 'curp',
        'label': 'CURP',
        'regex': /abc/,
        'shortName': 'CURP',
        'icon': 'fa fa-user'
    },
    {
        'id': 'rfc',
        'label': 'RFC',
        'regex': /abc/,
        'shortName': 'RFC',
        'icon': 'fa fa-building'
    },
    {
        'id': 'ip',
        'label': 'Dirección IPv4',
        'regex': /abc/,
        'shortName': 'Dirección IPv4',
        'icon': 'fa fa-laptop'
    },
    {
        'id': 'birthday',
        'label': 'Cumpleaños formato DD/MM/AA',
        'regex': /abc/,
        'shortName': 'Cumpleaños',
        'icon': 'fa fa-birthday-cake'
    }
];

(() => {
    let output = '<div class="row">';
    
    validators.forEach((validator, index) => {
        output += `
        <div class="col-md-4 mb-3">
            <label for="${validator.id}">${validator.label}</label>
            <div class="input-group">
                <div class="input-group-prepend">
                    <span class="input-group-text" id="inputGroupPrepend">
                        <i class="${validator.icon}" aria-hidden="true"></i>
                    </span>
                </div>
                <input
                    type="text"
                    class="form-control"
                    id="${validator.id}"
                    placeholder="${validator.label}"
                    aria-describedby="inputGroupPrepend"
                    required
                >
                <div class="valid-feedback">
                    ${validator.shortName} válido
                </div>
                <div class="invalid-feedback">
                    ${validator.shortName} inválido
                </div>
            </div>
        </div>
        `;
    });
    output += '</div>';
    mainContent.innerHTML = output;

    validators.forEach(validator => {
        const currentControl = document.getElementById(validator.id);

        currentControl.addEventListener('keyup', e => {
            const value = e.target.value;

            console.log(value);

            if (validator.regex.test(value)) {
                currentControl.classList.add('is-valid');
                currentControl.classList.remove('is-invalid');
            } else {
                currentControl.classList.add('is-invalid');
                currentControl.classList.remove('is-valid');
            }
        });
    });
})();