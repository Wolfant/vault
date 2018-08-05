import subprocess
import logging
from flask import Flask, redirect, url_for, request, render_template
from vault.keystoreform import KeyStoreForm

app = Flask(__name__)


def excuteCommand(command):
    logging.info(command)
    print(command)
    p = subprocess.Popen([command], stdout=subprocess.PIPE, shell=True)
    return p.stdout.read().decode('utf-8').strip()


@app.route('/create-vaultform/<name>')
def vault(name):
    return 'KeyStore "%s" is created on this server, \
            please create the Vault ' % name


@app.route('/create-keystoreform', methods=['POST', 'GET'])
def keyStore():
    form = KeyStoreForm(request.form)
    if request.method == 'POST' and form.validate():
        alias = form.alias.data
        storetype = form.storetype.data
        keyalg = form.keyalg.data
        keysize = form.keysize.data
        storepass = form.storepass.data
        keypass = form.keypass.data
        validity = form.validity.data
        keystore = form.keystore.data
        command = "keytool -genseckey -alias {} -storetype {} ".format(
            alias,
            storetype) + \
            "-keyalg {} -keysize {} -storepass {} -keypass {} ".format(
                keyalg, keysize,
                storepass, keypass) + \
            " -validity {} -keystore {}".format(validity, keystore)
        execution = excuteCommand(command)
        if execution == '':
            return redirect(url_for('vault', name=alias))
        else:
            return redirect(url_for('keyStore', menssage=execution))
    else:
        menssage = request.args.get('menssage')
        if menssage:
            return render_template(
                'keystore.html',
                form=form, menssage=menssage)
        else:
            return render_template('keystore.html', form=form)


@app.route('/')
def index():
    return render_template('index.html')


if __name__ == '__main__':
    app.run(debug=True)
