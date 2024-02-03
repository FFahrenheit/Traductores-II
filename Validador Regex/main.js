const mainContent = document.getElementById('main');

const validators = [
    {
        'id': 'telefono',
        'label': 'Teléfono de 10 dígitos',
        'regex': /^[0-9]{10}$/,
        'shortName': 'Teléfono',
        'icon': 'fa fa-phone'
    },
    {
        'id': 'correo',
        'label': 'Correo electrónico',
        'regex': /^\w+([\.-]?\w+)*@\w+([\.-]?\w+)*(\.\w{2,3})+$/,
        'shortName': 'Correo',
        'icon': 'fa fa-envelope-o'
    },
    {
        'id': 'curp',
        'label': 'CURP',
        'regex': /^[A-Z][AEIOU][A-Z]{2}\d{2}(0[1-9]|1[0-2])(0[1-9]|[12][0-9]|3[0-1])[HM](AS|BC|BS|CC|CS|CH|CL|CM|DF|DG|GT|GR|HG|JC|MC|MN|MS|NT|NL|OC|PL|QT|QR|SP|SL|SR|TC|TS|TL|VZ|YN|ZS|NE)[B-DF-HJ-NP-TV-Z]{3}[0-9A-Z]\d$/,
        'shortName': 'CURP',
        'icon': 'fa fa-user'
    },
    {
        'id': 'rfc',
        'label': 'RFC',
        'regex': /^([A-ZÑ\x26]{3,4}([0-9]{2})(0[1-9]|1[0-2])(0[1-9]|[1-2][0-9]|3[0-1]))([A-Z\d]{3})?$/,
        'shortName': 'RFC',
        'icon': 'fa fa-building'
    },
    {
        'id': 'ip',
        'label': 'Dirección IPv4',
        'regex': /^((25[0-5]|(2[0-4]|1\d|[1-9]|)\d)\.?\b){4}$/,
        'shortName': 'Dirección IPv4',
        'icon': 'fa fa-laptop'
    },
    {
        'id': 'birthday',
        'label': 'Cumpleaños formato DD/MM/AA',
        'regex': /^(0[1-9]|[12][0-9]|3[01])\/(0[1-9]|1[012])\/\d{2}$/,
        'shortName': 'Cumpleaños',
        'icon': 'fa fa-birthday-cake'
    }
];

(() => {
    let output = '<div class="row">';
    
    validators.forEach(validator => {
        output += `
        <div class="col-md-6 mb-3 px-5">
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
            const isValid = validator.regex.test(value);

            console.table([
                {
                    'Campo': validator.shortName,
                    'Valor': value,
                    'Regex': validator.regex, 
                    'Válido': isValid
                }
            ]);

            if (isValid) {
                currentControl.classList.add('is-valid');
                currentControl.classList.remove('is-invalid');
            } else {
                currentControl.classList.add('is-invalid');
                currentControl.classList.remove('is-valid');
            }
        });
    });
})();