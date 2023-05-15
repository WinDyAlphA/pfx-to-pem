from OpenSSL import crypto

def pfx_to_pem(input_file, output_file, password):
    # Ouvre le fichier .pfx en mode binaire
    with open(input_file, 'rb') as pfx_file:
        pfx_data = pfx_file.read()

    # Charge le certificat PKCS12
    pfx = crypto.load_pkcs12(pfx_data, password)

    # Récupère la clé privée et le certificat
    private_key = crypto.dump_privatekey(crypto.FILETYPE_PEM, pfx.get_privatekey())
    certificate = crypto.dump_certificate(crypto.FILETYPE_PEM, pfx.get_certificate())

    # Écrit la clé privée et le certificat dans le fichier .pem
    with open(output_file, 'wb') as pem_file:
        pem_file.write(private_key)
        pem_file.write(certificate)

# Exemple d'utilisation du script
pfx_to_pem('GESCOM RQT.pfx', 'certificat.pem', str.encode('123456'))
