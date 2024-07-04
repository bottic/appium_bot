from functional import check_phone_numbers_ru, Phone
from config import URL, PATH_TO_APK, FILE_NAME


if __name__ == '__main__':
    with open(FILE_NAME) as file:
        tnumbers = file.readlines()
    list_udid = []
    list_pnumbers = []
    phones = []
    for number in tnumbers:
        list_udid.append(number.split(' ')[0].strip())
        list_pnumbers.append(number.split(' ')[1].strip())

    if check_phone_numbers_ru(list_pnumbers):
        for i, udid in enumerate(list_udid):
            country_code = list_pnumbers[i][:1]
            phone_number = list_pnumbers[i][1:]
            phones.append(Phone(country_code, phone_number, 1080, 1920, udid, URL))

    for phone in phones:
        phone.test_click()
        # phone.install_open_tg(PATH_TO_APK)