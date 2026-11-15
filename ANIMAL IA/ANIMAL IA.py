
import os
import sys
import cv2

print("===== ANIMAL VISION AI =====")

BASE = os.path.dirname(os.path.abspath(__file__))

# Buscar imagen
nombre = input("\nEscribe el nombre de la imagen: ").strip()
nombre = os.path.splitext(nombre)[0].lower()

ruta = None

for raiz, carpetas, archivos in os.walk(BASE):
    for archivo in archivos:
        nombre_archivo = os.path.splitext(archivo)[0].lower()

        if nombre_archivo == nombre:
            ruta = os.path.join(raiz, archivo)
            break

    if ruta:
        break

# Comprobar imagen
if ruta is None:
    print("\nNo se encontro la imagen.")
    input("Presiona ENTER para salir...")
    sys.exit()

imagen = cv2.imread(ruta)

if imagen is None:
    print("No se pudo abrir la imagen.")
    input("Presiona ENTER para salir...")
    sys.exit()

print("\nImagen encontrada:", ruta)

# Convertir a escala de grises
gris = cv2.cvtColor(imagen, cv2.COLOR_BGR2GRAY)

# Extraer caracteristicas con SIFT
sift = cv2.SIFT_create()
puntos, descriptores = sift.detectAndCompute(gris, None)

# Clasificar segun el nombre del archivo
if "gato" in nombre:
    animal = "GATO"
elif "perro" in nombre:
    animal = "PERRO"
else:
    animal = "ANIMAL NO IDENTIFICADO"

# Mostrar resultados
print("\n===== RESULTADOS =====")
print("Animal:", animal)
print("Puntos detectados:", len(puntos))

# Dibujar puntos detectados
resultado = cv2.drawKeypoints(
    imagen,
    puntos,
    None,
    flags=cv2.DRAW_MATCHES_FLAGS_DRAW_RICH_KEYPOINTS
)

cv2.putText(
    resultado,
    animal,
    (20, 40),
    cv2.FONT_HERSHEY_SIMPLEX,
    1,
    (0, 255, 0),
    2
)

cv2.imshow("ANIMAL VISION AI", resultado)

print("\nPresiona una tecla para cerrar.")
cv2.waitKey(0)
cv2.destroyAllWindows()

print("Analisis terminado.")
