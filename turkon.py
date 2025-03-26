from seleniumbase import SB

trackingNumber = "TRKU4445381"

inputElement = 'body > app-root > app-layout > div > div > div > app-tracking > div > div.col-12 > div > div > div.field.col-12.md\:col-6.mt-3 > span > input'
submitBtnElement = 'body > app-root > app-layout > div > div > div > app-tracking > div > div.col-12 > div > div > div.field.col-12.md\:col-2.mt-3 > button'

with SB(uc=True, test=True, headless=True) as sb:
    url = 'https://myturkonline.turkon.com/tracking'

    sb.activate_cdp_mode(url)
    sb.sleep(2)

    # input assertion
    sb.assert_element(inputElement)
    sb.highlight(inputElement)

    sb.sleep(2)

    # submit btn assertion
    sb.assert_element(submitBtnElement)
    sb.highlight(submitBtnElement)

    sb.type(inputElement, trackingNumber)
    sb.sleep(1)
    sb.click(submitBtnElement)

    sb.assert_text("Yükleme Bilgileri")

    sb.save_page_source('result.html')

    print("tamamlandi")

