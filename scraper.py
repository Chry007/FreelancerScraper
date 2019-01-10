from lxml import html, etree
import requests

siteIndicator = 0
i = 1

page = requests.get('https://www.freelance.de/Projekte/K/IT-Entwicklung-Projekte/')
tree = html.fromstring(page.content)

while "Es wurden leider keine Projekte für Ihre Suchanfrage gefunden." not in page.content.decode("utf-8"):

    panels = tree.xpath("//div[contains(@class, 'panel-body single-profile clearfix')]")

    print("Page: " + str(i))

    for panel in panels:
        panelstring = etree.tostring(panel)
        panelElement = html.fromstring(panelstring)
        timeelement = panelElement.xpath("//i[contains(@class, 'fa fa-clock-o')]")
        if len(timeelement) > 0 and "April" in timeelement[0].tail or "Mai" in timeelement[0].tail or "Juni" in timeelement[0].tail or "Juli" in timeelement[0].tail:
            linkelement = panelElement.xpath("//a[contains(@id, 'project_link_')]")
            print(linkelement[0].text, "https://www.freelance.de" + linkelement[0].attrib['href'], timeelement[0].tail)

    siteIndicator += 20
    i += 1
    page = requests.get('https://www.freelance.de/Projekte/K/IT-Entwicklung-Projekte/' + str(siteIndicator) + '-2')
    tree = html.fromstring(page.content)



