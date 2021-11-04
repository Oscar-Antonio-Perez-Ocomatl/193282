from imgurpython import ImgurClient
import threading
from concurrent.futures import ThreadPoolExecutor
from multiprocessing import Pool
import os
import urllib.request
import timeit

urls_list = [] #Lista de las url
secreto_cliente = "5f8c3cce299db5e26a2eb96b0b7809a82805c9ad"
id_cliente = "bfa0e227a1c5643"

cliente = ImgurClient(id_cliente, secreto_cliente)


def descarga_url_img(link):
    #print(link)
    nombre_img = link.split("/")[3]
    formato_img = nombre_img.split(".")[1]
    nombre_img = nombre_img.split(".")[0]
    print(nombre_img, formato_img)
    url_local = "D:\\SEPTIMO_CUATRI\\ProgramacionConcurrente\\SegundoCorte\\Actividades\\act_c2\\img\\{}.{}"
    urllib.request.urlretrieve(link, url_local.format(nombre_img, formato_img))

def multiprocesamiento():
    print('\nMultiprocesamiento')
    id_album = "bUaCfoz"
    imagenes = cliente.get_album_images(id_album)
    for imagen in imagenes:
        # descarga_url_img(imagen.link)
        urls_list.append(imagen.link)
    pool = Pool(len(urls_list))
    pool.map(descarga_url_img, urls_list)

# def subprocesoMultiples():
#     print('\n Subprocesos')
#     with ThreadPoolExecutor(max_workers=len(urls_list)) as executer:
#         executer.map(descarga_url_img, urls_list)

# def main():
#     id_album = "bUaCfoz"
#     imagenes = cliente.get_album_images(id_album)
#     for imagen in imagenes:
#         descarga_url_img(imagen.link)
#         urls_list.append(imagen.link)

if __name__ == "__main__":
    # print(f'Tiempo sincrono: {timeit.Timer(main).timeit(number=1)}')
    # print(f'Tiempo subprocesos multiples: {timeit.Timer(subprocesoMultiples).timeit(number=1)}')
    print(f'Tiempo multiprocesamiento: {timeit.Timer(multiprocesamiento).timeit(number=1)}')