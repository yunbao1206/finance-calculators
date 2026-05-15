#!/usr/bin/env python3
"""Generate complete sitemap.xml with all calculator and state pages."""
import os

STATES = ["alabama","alaska","arizona","arkansas","california","colorado","connecticut","delaware","florida","georgia","hawaii","idaho","illinois","indiana","iowa","kansas","kentucky","louisiana","maine","maryland","massachusetts","michigan","minnesota","mississippi","missouri","montana","nebraska","nevada","new-hampshire","new-jersey","new-mexico","new-york","north-carolina","north-dakota","ohio","oklahoma","oregon","pennsylvania","rhode-island","south-carolina","south-dakota","tennessee","texas","utah","vermont","virginia","washington","west-virginia","wisconsin","wyoming"]

BASE = "https://calc.wiseclick.site"

urls = []
urls.append(f'  <url><loc>{BASE}/</loc><priority>1.0</priority></url>')

calculators = [
    "mortgage-calculator","loan-calculator","compound-interest-calculator",
    "credit-card-payoff-calculator","auto-loan-calculator","retirement-calculator",
    "401k-calculator","tax-calculator","annuity-calculator","savings-calculator",
    "paycheck-calculator"
]
for c in calculators:
    urls.append(f'  <url><loc>{BASE}/{c}/</loc><priority>0.9</priority></url>')

for s in STATES:
    urls.append(f'  <url><loc>{BASE}/paycheck-calculator/{s}/</loc><priority>0.8</priority></url>')

for p in ["about","privacy","terms"]:
    urls.append(f'  <url><loc>{BASE}/{p}/</loc><priority>0.3</priority></url>')

xml = '<?xml version="1.0" encoding="UTF-8"?>\n<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">\n' + '\n'.join(urls) + '\n</urlset>'

with open(os.path.join(os.path.dirname(__file__), "sitemap.xml"), "w") as f:
    f.write(xml)

print(f"Generated sitemap with {len(urls)} URLs")
