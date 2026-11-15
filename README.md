# CeylonGo - Travel & Service Marketplace Platform 🌴

**Klook.com** හි ආකෘතිය අනුව නිර්මාණය කරන ලද, ශ්‍රී ලංකාවේ සංචාරක සේවා සපයන්නන් සහ පාරිභෝගිකයන් අතරමැදියෙකු (Affiliate Agency) ලෙස සම්බන්ධ කර කොමිස් ලාභ උපයන සම්පූර්ණ වෙබ් පද්ධතිය.

---

## 🚀 පද්ධතිය ක්‍රියාත්මක වන ආකාරය (How It Works)

1. **පාරිභෝගිකයා (Customer):**
   - වෙබ් අඩවියට පිවිස ප්‍රධාන කාණ්ඩ 10 න් තමාට අවශ්‍ය සේවාව තෝරයි (උදා: Tours, Rooms, Cabs, Safaris...).
   - පැකේජයේ පින්තූර, විස්තර, මිල සහ **Package Code** එක (උදා: `TR-01`) බලයි.
   - **"Book via WhatsApp"** බොත්තම ක්ලික් කරයි.
   - ස්වයංක්‍රීයවම Code එක සහ Package නම සමඟ pre-filled පණිවිඩයක් ඔබගේ WhatsApp වෙත පැමිණේ.

2. **පරිපාලක ඔබ (Admin):**
   - ඔබට WhatsApp පණිවිඩය ලැබුණු සැණින්, **⚡ Quick Code Lookup** පිටුවට (`http://127.0.0.1:8000/lookup/`) පිවිස අදාළ Code එක (උදා: `TR-01`) search කරයි.
   - එහිදී:
     - සැබෑ **Vendor (සේවා සපයන්නාගේ නම, දුරකථන අංකය, 1-Click Direct WhatsApp link)** පෙනේ.
     - **Vendor Cost** (Wholesale මිල) සහ ඔබේ **Net Commission / Profit** (ලාභය) ගණනය වී පෙනේ.
     - රහසිගත සටහන් සහ Vendor ගේ බැංකු විස්තර පෙනේ.
   - ඔබ Vendor අමතා දිනය සහ වේලාව වෙන්කර, පාරිභෝගිකයාට WhatsApp මගින් තහවුරු කරයි.

---

## 💻 සර්වරය ආරම්භ කරන ආකාරය (How to Run)

පහසුම ක්‍රමය:
- ෆෝල්ඩරයේ ඇති **`run_server.bat`** ගොනුව double click කරන්න.

හෝ Terminal / PowerShell එකෙන්:
```bash
.\venv\Scripts\python manage.py runserver
```

---

## 🔗 ප්‍රධාන පිටු සහ සබැඳි (Key URLs)

- **පාරිභෝගික වෙබ් අඩවිය (Customer Frontend):** [http://127.0.0.1:8000/](http://127.0.0.1:8000/)
- **⚡ Admin Quick Vendor Lookup (රහසිගත පිටුව):** [http://127.0.0.1:8000/lookup/](http://127.0.0.1:8000/lookup/)
- **ප්‍රධාන Admin පාලක පුවරුව (Django Admin):** [http://127.0.0.1:8000/admin/](http://127.0.0.1:8000/admin/)

### පෙරනිමි Admin පිවිසුම් තොරතුරු (Default Login):
- **Username:** `admin`
- **Password:** `admin123`

---

## 📱 ඔබගේ WhatsApp අංකය වෙනස් කරන්නේ කෙසේද?
`config/settings.py` ගොනුවේ අග ඇති:
```python
ADMIN_WHATSAPP_NUMBER = '94770000000' # මෙහි ඔබේ අංකය country code එක සමඟ (+ නැතුව) යොදන්න
```

---

## 🗂️ පවතින ප්‍රධාන කාණ්ඩ (Customer's Curated Categories):
1. 🏔️ Ella Signature Experiences (ඇල්ල සුවිශේෂී අත්දැකීම්)
2. 🌿 Tea Trails & Mountain Discoveries (තේ වතු සහ කඳුකර ගවේෂණ)
3. 💦 Nature & Waterfall Escapes (දියඇලි සහ ස්වභාවික චාරිකා)
4. 🦌 Wildlife Encounters (වනජීවී සෆාරි අත්දැකීම්)
5. 🏛️ Heritage & Cultural Discoveries (ඓතිහාසික සහ සංස්කෘතික ගවේෂණ)
6. 🍽️ Scenic Dining Experiences (සුන්දර පරිසරයක භෝජන අත්දැකීම්)
7. 🧖‍♂️ Wellness & Soulful Escapes (සුවතා සහ ආයුර්වේද විවේකයන්)
8. ❤️ Romance & Special Moments (ආදරණීය සහ විශේෂ මොහොතවල්)
9. 🚐 Bespoke Private Journeys (සුවිශේෂී පෞද්ගලික ප්‍රවාහන සේවා)

