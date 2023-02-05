#!/usr/bin/env python3
import feedparser
import pandas as pd
import sys
import datetime
import dateutil.parser

# Fecha actual
today = datetime.datetime.now()
formatted_today_date = today.strftime("%Y%m%d_%H%M%S")

# Keyword a buscar entre todos los feed y asi formar el dataframe filtrado

keyword = str(sys.argv[1])

# Lista de url de feed rss

rss_url = ["https://www.bleepingcomputer.com/feed/",
"https://blog.rapid7.com/rss/",
"https://www.curatedintel.org/feeds/posts/default",
"https://www.proofpoint.com/us/threat-insight-blog.xml",
"https://blog.gigamon.com/feed/",
"http://blog.crowdstrike.com/feed",
"https://bushidotoken.blogspot.com/feeds/posts/default",
"http://blogs.cisco.com/rss/security/",
"https://www.coveware.com/blog?format=RSS",
"http://www.symantec.com/connect/item-feeds/blog/2261/feed/all/en/all",
"https://www.huntress.com/blog/rss.xml",
"https://www.cybereason.com/blog/rss.xml",
"http://www.securelist.com/en/rss/allupdates",
"https://techcrunch.com/author/zack-whittaker/feed/",
"https://ciberseguridad.blog/rss/",
"http://blog.jpcert.or.jp/atom.xml",
"https://bellingcat.com/feed/",
"http://feeds.trendmicro.com/Anti-MalwareBlog/",
"http://researchcenter.paloaltonetworks.com/unit42/feed/",
"https://www.proofpoint.com/rss.xml",
"https://www.ciberseguridadlatam.com/feed/",
"http://www.darkreading.com/rss/all.xml",
"http://feeds.feedblitz.com/alienvault-security-essentials",
"http://feeds.feedburner.com/AlienVaultLabs",
"http://feeds.trendmicro.com/TrendMicroResearch",
"http://iscxml.sans.org/rssfeed.xml",
"http://feeds.feedblitz.com/alienvault-blogs&amp;x=1",
"https://thedfirreport.com/feed/",
"http://www.seguridadyfirewall.cl/feeds/posts/default",
"https://expel.io/feed/",
"https://www.recordedfuture.com/feed/",
"https://blog.google/threat-analysis-group/rss",
"http://cyberseguridad.net/index.php?format=feed&amp;type=rss",
"https://labs.sentinelone.com/feed/",
"https://dragos.com/feed/",
"https://stairwell.com/feed/atom/",
"http://threatpost.com/en_us/rss.xml",
"http://www.volexity.com/blog/?feed=rss2",
"http://labs.bitdefender.com/feed/",
"https://www.us-cert.gov/ncas/analysis-reports.xml",
"https://www.secureworks.com/rss?feed=blog",
"https://forensicitguy.github.io/feed.xml",
"http://threatpost.com/feed",
"http://blog.morphisec.com/rss.xml",
"http://vrt-sourcefire.blogspot.com/feeds/posts/default",
"https://www.redcanary.com/blog/feed/",
"https://www.nccgroup.trust/uk/about-us/newsroom-and-events/blogs/uk-sc-rss-feed/",
"http://www.novetta.com/feed/",
"http://blogs.technet.com/msrc/rss.xml",
"https://www.maltego.com/index.xml",
"http://researchcenter.paloaltonetworks.com/feed/",
"https://www.ciberseguridadpyme.es/feed/",
"https://community.rapid7.com/community/infosec/blog/feeds/posts",
"http://feeds.feedburner.com/SansInstituteNewsbites",
"http://www.us-cert.gov/current/index.rdf",
"https://citizenlab.org/category/lab-news/feed/",
"https://posts.specterops.io/feed",
"https://www.brighttalk.com/channel/7451/feed/rss",
"https://www.greynoise.io/blog/rss.xml",
"http://cybersecuritynews.es/feed/",
"http://www.intezer.com/feed/",
"http://blog.emsisoft.com/feed/",
"http://blog.eset.com/feed",
"https://exchange.xforce.ibmcloud.com/rss/collection?tag=advisory",
"http://feeds.arstechnica.com/arstechnica/security",
"http://blogs.technet.com/mmpc/rss.xml",
"https://team-cymru.com/feed/"]


def obtain_rss_feed(rss_url):
    feeds = []
    for url in rss_url:
        print(url)
        try:
            feed = feedparser.parse(url)
            for entry in feed.entries:

                title = entry.title
                #description = entry.description
                link = entry.link
                date = entry.published
                formatted_date = dateutil.parser.parse(date,ignoretz=True).date()

                feeds.append({"title": title, "link": link, "date": formatted_date})
        except:
            continue
    return feeds


# Obtener arreglo de todos los feed
print("### Obteniendo feeds ###")
total_feeds = obtain_rss_feed(rss_url)

# Convertir arreglo de todos los feed a pandas dataframe
print("### Convertir a pandas dataframe ###")
df = pd.DataFrame(total_feeds)

# Remover caracteres no ASCII
print("### Remover caracteres no ASCII ###")
df = df.applymap(lambda x: x.encode('ascii', 'ignore').decode() if isinstance(x, str) else x)
#print(df.head(20))

# Filtrar por keywords
try:
    print("### Filtrar por keyword ###")
    df_filtrado = df[(df["title"].str.contains(keyword, case=False))]
    # Es necesario copiar el df para evitar errornes de chained index
    df_filtrado_copy = df_filtrado.copy()
    # Ordenar por fecha en orden descendente
    df_filtrado_copy['date'] = pd.to_datetime(df_filtrado['date'])
    df_ordenado_fecha = df_filtrado_copy.sort_values(by='date', ascending= False)
    # Exportar a CSV y agregar fecha actual a filename
    print("### Exportar a CSV ###")
    df_ordenado_fecha.to_csv('%s_informe_cti_rss_feed.csv' %formatted_today_date, sep =";")
    # Imprimir por pantalla primeras 20 lineas de DF
    print("### Imprimir muestra de dataframe ###")
    print(df_ordenado_fecha.head(20))
except:
    print("Keyword no encontrada")
    pass
