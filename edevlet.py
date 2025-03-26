from seleniumbase import SB

TCKN = ''
PASS = ''

with SB(uc=True, test=True, headless=True) as sb:
    url = 'https://giris.turkiye.gov.tr/Giris/gir'

    sb.activate_cdp_mode(url)
    sb.sleep(2)

    # TCKN input assertion
    sb.assert_element('input[name="tridField"]')
    sb.highlight('input[name="tridField"]')

    # Pass input assertion
    sb.assert_element('input[name="egpField"]')
    sb.highlight('input[name="egpField"]')

    # Submit Button Assertion
    sb.assert_element('button[name="submitButton"]')

    # FILL CREDENTIALS
    sb.type('input[name="tridField"]', TCKN)
    sb.type('input[name="egpField"]', PASS)

    #CLICK
    sb.click('button[name="submitButton"]')

    sb.wait_for_element('input[name="aranan"]', timeout=60)
    sb.highlight("body")
    sb.post_message("E-DEVLETE GİRİŞ YAPILDI")