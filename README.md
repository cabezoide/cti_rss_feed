# cti_rss_feed
Script en Python que busca en feed rss de paginas de noticias de ciberseguridad, buscando por una palabra en especifico. 

El usuario ingresa un keyword especifico para buscar en las fuentes de RSS de ciberseguridad. El script lee las fuentes de RSS, busca el keyword especifico y entrega un reporte de los resultados obtenidos en .csv. El reporte incluye información como el título, la fecha de publicación y el enlace de la fuente de RSS. 

Requiere librerias feedparser y pandas. Funciona tanto en windows como linux. La idea es poder buscar rápidamente por palabras clave, como jira, ransomware, critical, vmware y asi. Ejemplode uso: python cti_rss_feed.py vmware
