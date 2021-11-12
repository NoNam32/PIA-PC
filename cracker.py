import hashlib
def cracker(args):
    encontrada = 0
    try:
        pass_file = open(args.y, 'r',)
    except:
        print("Error:"+args.y+"no ha sido encontrada")

    for palabra in pass_file:
        palabra_cifrada = palabra.encode('utf-8')
        palabra_hasheada = hashlib.md5(palabra_cifrada.strip())
        digest = palabra_hasheada.hexdigest()

        if digest == args.x:
            print ("Contraseña encontrada: "+palabra)
            encontrada = 1
            break
        
    if not encontrada:
        print("contraseña no encontrada en el archivo "+ args.y)