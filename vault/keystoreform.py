from wtforms import Form, TextField, IntegerField, \
            PasswordField, SelectField, SubmitField, validators


class KeyStoreForm(Form):
    alias = TextField(
        "KeyStore Alias", [validators.length(max=10)],
        id='alias', default='vault'
    )
    storetype = SelectField(
        "StoreType",
        choices=[('jceks', 'jceks'), ('pkcs12', 'pkcs12')]
    )
    keyalg = TextField('KeyStore Algorithm', id="keyalg", default="AES")
    keysize = IntegerField(
        'KeyStore Size', [validators.number_range(min=128)],
        id="keysize", default='128'
    )
    storepass = PasswordField('Store Password', [validators.length(min=8)])
    keypass = PasswordField('Key Password', [validators.length(min=8)])
    validity = IntegerField(
        'validity Time', [validators.number_range(min=360)],
        id='validity', default='730'
    )
    keystore = TextField(
        'KeyStore File name', id='keystore',
        default='vault.keystore'
    )
    createks = SubmitField('Create KeyStore')
