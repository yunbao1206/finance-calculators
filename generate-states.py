#!/usr/bin/env python3
"""Generate 50 state paycheck calculator pages for programmatic SEO."""
import os

STATES = {
    "alabama": {"abbr": "AL", "rate": 0.05, "avg": "5.0%"},
    "alaska": {"abbr": "AK", "rate": 0, "avg": "0%"},
    "arizona": {"abbr": "AZ", "rate": 0.025, "avg": "2.5%"},
    "arkansas": {"abbr": "AR", "rate": 0.047, "avg": "4.7%"},
    "california": {"abbr": "CA", "rate": 0.093, "avg": "9.3%"},
    "colorado": {"abbr": "CO", "rate": 0.044, "avg": "4.4%"},
    "connecticut": {"abbr": "CT", "rate": 0.0699, "avg": "6.99%"},
    "delaware": {"abbr": "DE", "rate": 0.066, "avg": "6.6%"},
    "florida": {"abbr": "FL", "rate": 0, "avg": "0%"},
    "georgia": {"abbr": "GA", "rate": 0.055, "avg": "5.5%"},
    "hawaii": {"abbr": "HI", "rate": 0.0825, "avg": "8.25%"},
    "idaho": {"abbr": "ID", "rate": 0.058, "avg": "5.8%"},
    "illinois": {"abbr": "IL", "rate": 0.0495, "avg": "4.95%"},
    "indiana": {"abbr": "IN", "rate": 0.0315, "avg": "3.15%"},
    "iowa": {"abbr": "IA", "rate": 0.06, "avg": "6.0%"},
    "kansas": {"abbr": "KS", "rate": 0.057, "avg": "5.7%"},
    "kentucky": {"abbr": "KY", "rate": 0.04, "avg": "4.0%"},
    "louisiana": {"abbr": "LA", "rate": 0.0425, "avg": "4.25%"},
    "maine": {"abbr": "ME", "rate": 0.0715, "avg": "7.15%"},
    "maryland": {"abbr": "MD", "rate": 0.0575, "avg": "5.75%"},
    "massachusetts": {"abbr": "MA", "rate": 0.05, "avg": "5.0%"},
    "michigan": {"abbr": "MI", "rate": 0.0425, "avg": "4.25%"},
    "minnesota": {"abbr": "MN", "rate": 0.0985, "avg": "9.85%"},
    "mississippi": {"abbr": "MS", "rate": 0.05, "avg": "5.0%"},
    "missouri": {"abbr": "MO", "rate": 0.048, "avg": "4.8%"},
    "montana": {"abbr": "MT", "rate": 0.059, "avg": "5.9%"},
    "nebraska": {"abbr": "NE", "rate": 0.0584, "avg": "5.84%"},
    "nevada": {"abbr": "NV", "rate": 0, "avg": "0%"},
    "new-hampshire": {"abbr": "NH", "rate": 0, "avg": "0%"},
    "new-jersey": {"abbr": "NJ", "rate": 0.1075, "avg": "10.75%"},
    "new-mexico": {"abbr": "NM", "rate": 0.059, "avg": "5.9%"},
    "new-york": {"abbr": "NY", "rate": 0.109, "avg": "10.9%"},
    "north-carolina": {"abbr": "NC", "rate": 0.045, "avg": "4.5%"},
    "north-dakota": {"abbr": "ND", "rate": 0.025, "avg": "2.5%"},
    "ohio": {"abbr": "OH", "rate": 0.035, "avg": "3.5%"},
    "oklahoma": {"abbr": "OK", "rate": 0.0475, "avg": "4.75%"},
    "oregon": {"abbr": "OR", "rate": 0.099, "avg": "9.9%"},
    "pennsylvania": {"abbr": "PA", "rate": 0.0307, "avg": "3.07%"},
    "rhode-island": {"abbr": "RI", "rate": 0.0599, "avg": "5.99%"},
    "south-carolina": {"abbr": "SC", "rate": 0.064, "avg": "6.4%"},
    "south-dakota": {"abbr": "SD", "rate": 0, "avg": "0%"},
    "tennessee": {"abbr": "TN", "rate": 0, "avg": "0%"},
    "texas": {"abbr": "TX", "rate": 0, "avg": "0%"},
    "utah": {"abbr": "UT", "rate": 0.0465, "avg": "4.65%"},
    "vermont": {"abbr": "VT", "rate": 0.0875, "avg": "8.75%"},
    "virginia": {"abbr": "VA", "rate": 0.0575, "avg": "5.75%"},
    "washington": {"abbr": "WA", "rate": 0, "avg": "0%"},
    "west-virginia": {"abbr": "WV", "rate": 0.055, "avg": "5.5%"},
    "wisconsin": {"abbr": "WI", "rate": 0.0765, "avg": "7.65%"},
    "wyoming": {"abbr": "WY", "rate": 0, "avg": "0%"},
}

TITLE_CASE = {k: k.replace("-", " ").title() for k in STATES}

def generate_page(slug, data):
    name = TITLE_CASE[slug]
    abbr = data["abbr"]
    rate = data["rate"]
    rate_str = f"{rate * 100}"

    no_tax = rate == 0
    tax_sentence = f"{name} has no state income tax." if no_tax else f"{name} has an effective state income tax rate of approximately {data['avg']}."

    example_salary = 75000
    state_tax_annual = example_salary * rate
    fed_tax_est = 8200
    fica_est = example_salary * 0.0765
    total_deductions = fed_tax_est + state_tax_annual + fica_est
    takehome = example_salary - total_deductions
    biweekly = takehome / 26

    return f'''<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>{name} Paycheck Calculator - Take-Home Pay After Tax in {name}</title>
  <meta name="description" content="Free {name} paycheck calculator. Estimate your take-home pay in {abbr} after federal and state income taxes. {tax_sentence}">
  <meta name="keywords" content="{name} paycheck calculator, {abbr} take home pay, {name} income tax calculator, {name} salary after tax, {name} tax calculator">
  <link rel="canonical" href="https://calc.wiseclick.site/paycheck-calculator/{slug}/">
  <link rel="stylesheet" href="../../css/style.css">
  <script type="application/ld+json">
  {{"@context":"https://schema.org","@type":"WebApplication","name":"{name} Paycheck Calculator","description":"Free paycheck calculator for {name} residents","applicationCategory":"FinanceApplication","operatingSystem":"Any","offers":{{"@type":"Offer","price":"0","priceCurrency":"USD"}}}}
  </script>
</head>
<body>
  <header class="site-header"><div class="header-inner">
    <a href="/" class="site-logo"><svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><rect x="4" y="2" width="16" height="20" rx="2"/><line x1="8" y1="6" x2="16" y2="6"/><line x1="8" y1="10" x2="16" y2="10"/><line x1="8" y1="14" x2="12" y2="14"/></svg>FinanceToolHub</a>
    <button class="nav-toggle" onclick="document.querySelector('.nav-links').classList.toggle('open')" aria-label="Menu"><svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><line x1="3" y1="6" x2="21" y2="6"/><line x1="3" y1="12" x2="21" y2="12"/><line x1="3" y1="18" x2="21" y2="18"/></svg></button>
    <ul class="nav-links"><li><a href="/">Home</a></li><li><a href="/mortgage-calculator/">Mortgage</a></li><li><a href="/tax-calculator/">Tax</a></li><li><a href="/paycheck-calculator/" class="active">Paycheck</a></li></ul>
  </div></header>

  <main>
    <nav class="breadcrumb"><a href="/">Home</a> / <a href="/paycheck-calculator/">Paycheck Calculator</a> / <span>{name}</span></nav>
    <div class="calc-page">
      <h1>{name} Paycheck Calculator</h1>
      <p class="subtitle">Calculate your take-home pay in {name} ({abbr}) after federal and state taxes.</p>

      <div class="calc-tool">
        <form class="calc-form" onsubmit="return false;">
          <div class="form-group"><label for="salary">Annual Salary ($)</label><input type="number" id="salary" value="75000" min="0" step="1000"></div>
          <div class="form-group"><label for="pay-freq">Pay Frequency</label>
            <select id="pay-freq"><option value="26" selected>Bi-weekly</option><option value="24">Semi-monthly</option><option value="52">Weekly</option><option value="12">Monthly</option></select>
          </div>
          <div class="form-group"><label for="filing">Filing Status</label>
            <select id="filing"><option value="single">Single</option><option value="married">Married</option></select>
          </div>
          <div class="form-group"><label for="pretax">Pre-tax Deductions ($/yr)</label><input type="number" id="pretax" value="5000" min="0" step="500"></div>
          <button type="button" class="btn-calculate" onclick="calc()">Calculate</button>
        </form>
        <div class="calc-results" id="results">
          <div class="result-highlight"><div class="label">Take-Home Pay Per Paycheck</div><div class="value" id="takehome">$0</div></div>
          <div class="result-details">
            <div class="result-item"><div class="label">Gross Per Paycheck</div><div class="value" id="gross">$0</div></div>
            <div class="result-item"><div class="label">Federal Tax</div><div class="value" id="fed">$0</div></div>
            <div class="result-item"><div class="label">{name} State Tax</div><div class="value" id="stax">$0</div></div>
            <div class="result-item"><div class="label">Social Security + Medicare</div><div class="value" id="fica">$0</div></div>
          </div>
        </div>
      </div>

      <div class="seo-content">
        <div class="seo-block">
          <h2>{name} Income Tax Overview</h2>
          <p>{tax_sentence}</p>
          <h3>Example: $75,000 Salary in {name}</h3>
          <ul>
            <li>Federal tax: ~${fed_tax_est:,}</li>
            <li>{name} state tax: ~${state_tax_annual:,.0f}</li>
            <li>FICA (SS + Medicare): ~${fica_est:,.0f}</li>
            <li><strong>Annual take-home: ~${takehome:,.0f}</strong></li>
            <li><strong>Bi-weekly paycheck: ~${biweekly:,.0f}</strong></li>
          </ul>
        </div>
        <div class="seo-block">
          <h2>Living and Working in {name}</h2>
          <p>{name} residents should consider the overall tax burden including federal income tax, state income tax{' (which is 0% in ' + name if no_tax else ''}, property taxes, and sales taxes when evaluating their take-home pay.</p>
          <h3>Tips for {name} Residents</h3>
          <ul>
            <li><strong>Maximize pre-tax deductions</strong> — 401(k) and HSA contributions reduce your taxable income.</li>
            <li><strong>Check your withholding</strong> — Use the IRS W-4 calculator to avoid overpaying or underpaying.</li>
            <li><strong>Consider local taxes</strong> — Some cities and counties add additional income taxes.</li>
          </ul>
        </div>
        <div class="seo-block full-width">
          <h2>Frequently Asked Questions</h2>
          <h3>What is the state income tax rate in {name}?</h3>
          <p>{tax_sentence} This is on top of the federal income tax which ranges from 10% to 37%.</p>
          <h3>How much will I take home in {name}?</h3>
          <p>On a $75,000 salary in {name}, your approximate bi-weekly take-home pay is <strong>${biweekly:,.0f}</strong> after all taxes and deductions. Use the calculator above for your exact situation.</p>
          <h3>Are there local taxes in {name}?</h3>
          <p>Some cities and counties impose additional income taxes. Check with your local tax authority for details specific to your area within {name}.</p>
        </div>
      </div>
    </div>
  </main>

  <footer class="site-footer"><div class="footer-inner">
    <ul class="footer-links"><li><a href="/about/">About</a></li><li><a href="/privacy/">Privacy Policy</a></li><li><a href="/terms/">Terms of Service</a></li></ul>
    <p class="footer-copy">&copy; 2026 FinanceToolHub. All rights reserved.</p>
  </div></footer>

  <script>
  const STATE_RATE = {rate};
  function calcFed(taxable, status) {{
    const brackets = status === 'married'
      ? [[23850,.10],[96950,.12],[206700,.22],[394600,.24],[500000,.32],[751600,.35],[Infinity,.37]]
      : [[11925,.10],[48475,.12],[103350,.22],[197300,.24],[250525,.32],[626350,.35],[Infinity,.37]];
    let tax=0, rem=taxable, prev=0;
    for (const [lim,rate] of brackets) {{
      const chunk = Math.min(rem, lim - prev);
      tax += chunk * rate; rem -= chunk;
      if (rem <= 0) break; prev = lim;
    }}
    return tax;
  }}
  function calc() {{
    const salary = +document.getElementById('salary').value || 0;
    const periods = +document.getElementById('pay-freq').value;
    const filing = document.getElementById('filing').value;
    const pretax = +document.getElementById('pretax').value || 0;
    const grossP = salary / periods;
    const taxable = Math.max(0, salary - pretax - (filing === 'married' ? 30000 : 15000));
    const fedAnnual = calcFed(taxable, filing);
    const stateAnnual = salary * STATE_RATE;
    const ss = Math.min(salary, 176100) * 0.062;
    const mc = salary * 0.0145 + Math.max(0, salary - 200000) * 0.009;
    const annualTakeHome = salary - fedAnnual - stateAnnual - ss - mc - pretax;
    const fmt = v => '$' + v.toLocaleString('en-US', {{minimumFractionDigits: 2, maximumFractionDigits: 2}});
    document.getElementById('takehome').textContent = fmt(annualTakeHome / periods);
    document.getElementById('gross').textContent = fmt(grossP);
    document.getElementById('fed').textContent = fmt(fedAnnual / periods);
    document.getElementById('stax').textContent = fmt(stateAnnual / periods);
    document.getElementById('fica').textContent = fmt((ss + mc) / periods);
    document.getElementById('results').classList.add('visible');
  }}
  calc();
  </script>
</body>
</html>'''

base = "/home/coder/workspace/Website/001-finance-calculators/paycheck-calculator"
for slug, data in STATES.items():
    dir_path = os.path.join(base, slug)
    os.makedirs(dir_path, exist_ok=True)
    with open(os.path.join(dir_path, "index.html"), "w") as f:
        f.write(generate_page(slug, data))

print(f"Generated {len(STATES)} state pages")
