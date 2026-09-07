import sys
import math
import requests
from urllib.parse import urlparse

def calculate_entropy(domain):
    if not domain: return 0
    probabilities = [float(domain.count(c)) / len(domain) for c in set(domain)]
    return -sum(p * math.log(p, 2) for p in probabilities)

def detect_homograph(domain):
    try:
        domain.encode('ascii')
        return False
    except UnicodeEncodeError:
        return True

def trace_redirects(url):
    try:
        response = requests.get(url, allow_redirects=True, timeout=5, headers={"User-Agent": "Mozilla/5.0"})
        return [r.url for r in response.history] + [response.url]
    except Exception as e:
        return [f"Error connecting: {e}"]

def analyze_url(url):
    print(f"\n🔍 Analyzing URL: {url}")
    parsed = urlparse(url)
    domain = parsed.netloc
    
    is_homograph = detect_homograph(domain)
    punycode = domain.encode('idna').decode('ascii') if is_homograph else domain
    entropy = calculate_entropy(domain)
    
    print("[*] Tracking redirect hops...")
    redirect_chain = trace_redirects(url)
    
    score = 0
    reasons = []
    
    if is_homograph:
        score += 50
        reasons.append(f"IDN Homograph Attack Detected! Disguised Punycode: {punycode}")
    if entropy > 4.2:
        score += 25
        reasons.append(f"High Domain Entropy ({entropy:.2f}) -> Suspiciously random domain layout")
    if len(redirect_chain) > 2:
        score += 25
        reasons.append(f"Deep Redirect Chain ({len(redirect_chain)-1} hops) -> Trying to mask target destination")
        
    print(f"\n📊 RESULTS:")
    print(f"[-] Final Destination: {redirect_chain[-1]}")
    print(f"[-] Threat Level Score: {min(score, 100)}%")
    if reasons:
        for r in reasons: print(f"    ⚠️ {r}")
    else:
        print("    ✅ No advanced anomalies detected.")

if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Usage: python3 advanced_phish_detect.py <URL>")
    else:
        analyze_url(sys.argv[1])
