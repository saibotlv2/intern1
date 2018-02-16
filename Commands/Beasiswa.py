import json

from linebot.models import (
    MessageEvent, TextMessage, TextSendMessage
)

def bea_info(line_api, event):
    result = "Buat para pemburu beasiswa, ni ada link bagus buat dilihat2 :\n\n"\
             "1. Australia Award  Scholarship (http://australiaawardsindo.or.id)\n"\
             "2. LPDP Scholarsh hip (http://www.beasiswalpdp.org/index.html)\n"\
             "3. DIKTI Scholarship a. Dalam Negeri (http://www.beasiswa.dikti.go.id/dn/) b. Luar Negeri (http://beasiswa.dikti.go.id/ln/)\n"\
             "4. Turkey Government Scholarship (http://www.turkiyeburslari.gov.tr/index.php/en)\n"\
             "5. General Cultural Scholarship India (http://www.iccrindia.net/gereralscheme.html)\n"\
             "6. USA Government Scholarship a. (http://www.aminef.or.id/index.php)b. (http://www.iief.or.id)\n"\
             "7. Netherland Government Scholarship (http://www.nesoindonesia.or.id/beasiswa)\n"\
             "8. Korean Government Scholarship (http://www.niied.go.kr/eng/contents.do…)\n"
            #  "9. Belgium Government Scholarship (http://www.vliruos.be/4273.aspx)\n"\
            #  "10. Macquaire University Australia (http://www.mq.edu.au/…/macquarie_university_international_…/ \n"\
            #  "11. Sciences Po France (http://formation.sciences-po.fr/…/the-emile-boutmy-scholars…)\n"\
            #  "12. Utrecht University Netherland (http://www.uu.nl/…/grantsandscholarships/Pages/utrechtexcel…)\n"\
            #  "13. Prasetya Mulya Business School Indonesia (http://www.pmbs.ac.id/s2/scholarship.php?lang=ENG)\n"\
            #  "14. Brunei Darussalam Government Scholarship (http://www.mofat.gov.bn/index.php/announcement)\n"\
            #  "15. Monbugakusho Scholarship Japan (http://www.id.emb-japan.go.jp/sch.html)\n"\
            #  "16. Paramadin ba University Master Fellowship Indonesia (https://gradschool.paramadina.ac.id/…/paramadina-medco-fell…)\n"\
            #  "17. PPM School of Management Indonesia (http://ppm-manajemen.ac.id/beasiswa-penuh-s2-mm-reguler/)\n"\
            #  "18. University of Twente Netherland (http://www.utwente.nl/internationa…/scholarshipsandgrants/…/)\n"\
            #  "19. Sweden Government Scholarship (http://www.studyinsweden.se/Scholarships/)\n"\
            #  "20. Chinese Government Scholarship (http://www.csc.edu.cn/laihua/scholarshipdetailen.aspx…)\n"\
            #  "21. Taiwan Government Scholarship (http://www.studyintaiwan.org/taiwan_scholarships.html)\n"\
            #  "22. United Kingdom Government SCholarship (http://www.chevening.org/indonesia/)\n"\
            #  "23. Panasonic Scholarship Japan (http://panasonic.net/citizensh…/scholarships/…/requirements/)\n"\
            #  "24. Ancora Foundation Scholarship (http://ancorafoundation.com)\n"\
            #  "25. Asian Public Intellectuals Fellowship Japan (http://www.api-fellowships.org/body/)\n"\
            #  "26. AUN/SEED-Net Scholarship (http://www.seed-net.org/index.php)\n"\
            #  "27. Art Asia Major Scholarship Korea National University of Arts (http://eng.karts.ac.kr:81/karts/board/list.jsp…)\n"\
            #  "28. Ritsumeikan Asia Pacific University Japan (http://www.apu.ac.jp/home/life/index.php?content_id=30)\n"\
            #  "29. Seoul National University Korea (http://en.snu.ac.kr/…/gradu…/scholarships/before-application)\n"\
            #  "30. DIKTIS Overseas Scholarship (http://www.pendis.kemenag.go.id/beasiswaln/)\n"\
            #  "31. Honjo International Scholarship Foundation Japan (http://hisf.or.jp/english/sch-f/)\n"\
            #  "32. IDB Merit Scholarship Programme for High Technology (http://www.isdb.org/irj/portal/anonymous…)\n"\
            #  "33. International HIV & Drug Use Fellowship USA (http://www.iasociety.org/fellowship.aspx)\n"\
            #  "34. Nitori International Scholarship Foundation Japan (http://www.nitori-shougakuzaidan.com/en/)\n"\
            #  "35. School of Government and Public Policy Indonesia (http://sgpp.ac.id/pages/financial-conditions)\n"\
            #  "36. Inpex Scholarship Foundation Japan \n"\
            #  "37. Asia University Taiwan (http://ciae.asia.edu.tw/AdmissionsScholarship.html)\n"
    line_api.reply_message(
        event.reply_token, TextSendMessage(text=result)
    )
