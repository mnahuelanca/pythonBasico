import subprocess

nombre_wifi = "Privada de Produccion"

resultado = subprocess.run([
    "netsh", "wlan", "show", "profile", nombre_wifi, "key=clear"], stdout=subprocess.PIPE
)

salida = resultado.stdout.decode("latin1")

for linea in salida.split ("\n"):
    if "Key content" in linea or "Contenido de la clave" in linea:
        print("la contraseña de la red es: ", linea.split(":")[1].strip())
    else:
        print("no se pudo ejecutar")