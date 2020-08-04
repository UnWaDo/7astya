from web import app
from flask import render_template
from web.forms import EncodeForm, DecodeForm
from web.encrypter.encoder import encode
from web.encrypter.decoder import decode

@app.route('/', methods=['GET', 'POST'])
def main():
	enc_form = EncodeForm()
	dec_form = DecodeForm()
	if enc_form.validate_on_submit():
		text = enc_form.text.data
		dec_form.encrypted.data = encode(text)
		return render_template('main.html', enc_form=enc_form, dec_form=dec_form, title='Нас7я')
	if dec_form.validate_on_submit():
		encr = dec_form.encrypted.data
		enc_form.text.data = decode(encr)
	return render_template('main.html', enc_form=enc_form, dec_form=dec_form, title='Нас7я')
