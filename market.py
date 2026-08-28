import telebot
from telebot import types
import sqlite3
import random
import time

TOKEN = "8835272043:AAHYLBYhPVLJu2pgZYCrGwvgjI5KGcLLkqA"
bot = telebot.TeleBot(TOKEN)

ADMIN_IDS = [8630791464]

KANAL = "@TurxnMedia"
CHAT = "@KimsesizlerDogus"
BOT_USERNAME = "MissSanalMarketBot"

INSTAGRAM_STOK = 15420
KREDI_KARTI_STOK = 12850

INSTAGRAM_SETLERI = [
    f"1NST4GR4M H354P R3P0RT M3TH0D'U\n1: {random.randint(1,10)}x Şikayet Et\n2: {random.randint(1,10)}x Spam\n3: {random.randint(1,10)}x Zorbalık veya istenmeyen iletişim\n4: {random.randint(1,10)}x Şiddet, nefret veya sömürü\n5: {random.randint(1,10)}x Emniyete yönelik inandırıcı tehdit",
    f"1NST4GR4M H354P R3P0RT M3TH0D'U\n1: {random.randint(1,10)}x Şikayet Et\n2: {random.randint(1,10)}x Sahtekarlık veya dolandırıcılık\n3: {random.randint(1,10)}x Finans veya yatırım dolandırıcılığı\n4: {random.randint(1,10)}x Kimlik hırsızlığı\n5: {random.randint(1,10)}x Sahte ürün veya hizmet satışı\n6: {random.randint(1,10)}x Şüpheli bağlantılar",
    f"1NST4GR4M H354P R3P0RT M3TH0D'U\n1: {random.randint(1,10)}x Şikayet Et\n2: {random.randint(1,10)}x Çıplaklık veya cinsellik\n3: {random.randint(1,10)}x Çıplak görüntüleri paylaşmakla tehdit etme veya paylaşma\n4: {random.randint(1,10)}x Fuhuş gibi görünüyor\n5: {random.randint(1,10)}x Cinsel istismar gibi görünüyor",
    f"1NST4GR4M H354P R3P0RT M3TH0D'U\n1: {random.randint(1,10)}x Şikayet Et\n2: {random.randint(1,10)}x Kısıtlamaya tabi ürünlerin satışını veya tanıtımını yapma\n3: {random.randint(1,10)}x Uyuşturucular\n4: {random.randint(1,10)}x Silahlar\n5: {random.randint(1,10)}x Şans Oyunları\n6: {random.randint(1,10)}x Alkol",
    f"1NST4GR4M H354P R3P0RT M3TH0D'U\n1: {random.randint(1,10)}x Şikayet Et\n2: {random.randint(1,10)}x İntihar, kendine zarar verme veya yeme bozuklukları\n3: {random.randint(1,10)}x İntihar veya kendine zarar verme\n4: {random.randint(1,10)}x Yeme bozukluğu\n5: {random.randint(1,10)}x Yanlış Bilgi",
    f"1NST4GR4M H354P R3P0RT M3TH0D'U\n1: {random.randint(1,10)}x Şikayet Et\n2: {random.randint(1,10)}x Sadece bundan hoşlanmadım\n3: {random.randint(1,10)}x Fiziksel veya duygusal tehditler\n4: {random.randint(1,10)}x Terörizm ya da organize suç gibi görünüyor\n5: {random.randint(1,10)}x Nefret söylemi veya sembolleri\n6: {random.randint(1,10)}x Hayvan istismarı",
    f"1NST4GR4M H354P R3P0RT M3TH0D'U\n1: {random.randint(1,10)}x Şikayet Et\n2: {random.randint(1,10)}x Kısıtlamaya tabi ürünlerin satışını veya tanıtımını yapma\n3: {random.randint(1,10)}x Uyuşturucular\n4: {random.randint(1,10)}x Kokain, eroin veya fentanil gibi yüksek bağımlılık yapıcı uyuşturucular\n5: {random.randint(1,10)}x Reçeteli ilaçlar\n6: {random.randint(1,10)}x Diğer uyuşturucular\n7: {random.randint(1,10)}x Tütün",
    f"1NST4GR4M H354P R3P0RT M3TH0D'U\n1: {random.randint(1,10)}x Şikayet Et\n2: {random.randint(1,10)}x Şiddet, nefret veya sömürü\n3: {random.randint(1,10)}x Şiddet çağrısı yapma\n4: {random.randint(1,10)}x Şiddet, ölüm veya ciddi yaralama gösterme\n5: {random.randint(1,10)}x Hayvanlar\n6: {random.randint(1,10)}x Şüpheli veya istenmeyen iletişim",
    f"1NST4GR4M H354P R3P0RT M3TH0D'U\n1: {random.randint(1,10)}x Şikayet Et\n2: {random.randint(1,10)}x Sahtekarlık veya dolandırıcılık\n3: {random.randint(1,10)}x İstismar gibi görünüyor\n4: {random.randint(1,10)}x Şüpheli bağlantılar\n5: {random.randint(1,10)}x Bunun gibi daha az içerik görmek istiyorum",
    f"1NST4GR4M H354P R3P0RT M3TH0D'U\n1: {random.randint(1,10)}x Şikayet Et\n2: {random.randint(1,10)}x Spam\n3: {random.randint(1,10)}x Çıplaklık veya cinsellik\n4: {random.randint(1,10)}x Fuhuş gibi görünüyor\n5: {random.randint(1,10)}x Silahlar\n6: {random.randint(1,10)}x Yanlış Bilgi\n7: {random.randint(1,10)}x Kimlik hırsızlığı"
]

for _ in range(1000):
    pass

KREDI_KARTLARI = [
    f"Kart Numarası\n`{random.choice([4111, 5432, 5555, 6227])} {random.randint(1000,9999)} {random.randint(1000,9999)} {random.randint(1000,9999)}`\n\nGeçerli\n`{random.randint(1,12):02d}/203{random.randint(6,9)}`\n\nCVV\n`{random.randint(100,999)}`"
    for _ in range(1000)
]

db = sqlite3.connect("market.db", check_same_thread=False)
cursor = db.cursor()

cursor.execute("""
CREATE TABLE IF NOT EXISTS users (
    user_id INTEGER PRIMARY KEY,
    username TEXT
)
""")
db.commit()

eklenecek_sutunlar = [
    ("referans_puani", "INTEGER DEFAULT 0"),
    ("kazandirdigi_uye", "INTEGER DEFAULT 0"),
    ("referans_sahibi", "INTEGER DEFAULT NULL"),
    ("ban_durumu", "INTEGER DEFAULT 0"),
    ("ban_bitis", "INTEGER DEFAULT 0"),
    ("ban_sebebi", "TEXT DEFAULT ''")
]

for sutun_adi, sutun_tipi in eklenecek_sutunlar:
    try:
        cursor.execute(f"ALTER TABLE users ADD COLUMN {sutun_adi} {sutun_tipi}")
        db.commit()
    except sqlite3.OperationalError:
        pass

def admin_mi(user_id):
    return user_id in ADMIN_IDS

def kullanici_kaydet(user):
    try:
        cursor.execute("INSERT OR IGNORE INTO users (user_id, username) VALUES (?, ?)", (user.id, user.username))
        cursor.execute("UPDATE users SET username = ? WHERE user_id = ?", (user.username, user.id))
        db.commit()
    except Exception as e:
        print(f"Kullanıcı kaydedilirken hata: {e}")

def ban_kontrol(user_id):
    try:
        cursor.execute("SELECT ban_durumu, ban_bitis FROM users WHERE user_id = ?", (user_id,))
        sonuc = cursor.fetchone()
        if not sonuc:
            return False

        ban_durumu, ban_bitis = sonuc
        if ban_durumu == 1:
            if ban_bitis > 0 and time.time() > ban_bitis:
                cursor.execute("UPDATE users SET ban_durumu = 0, ban_bitis = 0, ban_sebebi = '' WHERE user_id = ?", (user_id,))
                db.commit()
                return False
            return True
    except Exception as e:
        print(f"Ban kontrol hatası: {e}")
    return False

def uyelik_kontrol(user_id):
    try:
        kanal = bot.get_chat_member(KANAL, user_id)
        grup = bot.get_chat_member(CHAT, user_id)
        return kanal.status in ["member", "administrator", "creator"] and grup.status in ["member", "administrator", "creator"]
    except Exception:
        return False

def kanal_mesaji(chat_id):
    keyboard = types.InlineKeyboardMarkup()
    keyboard.add(types.InlineKeyboardButton("📢 KANALA KATIL", url="https://t.me/TurxnMedia"))
    keyboard.add(types.InlineKeyboardButton("👥 GRUBA KATIL", url="https://t.me/KimsesizlerDogus"))
    keyboard.add(types.InlineKeyboardButton("✅ KONTROL ET", callback_data="kanal_kontrol"))
    try:
        bot.send_message(chat_id, "📢 Devam etmek için kanal ve gruba katıl:", reply_markup=keyboard)
    except Exception as e:
        print(f"Kanal mesajı gönderilemedi: {e}")

def stoklari_kontrol_et_ve_yenile():
    global INSTAGRAM_STOK, KREDI_KARTI_STOK
    if INSTAGRAM_STOK <= 0:
        INSTAGRAM_STOK = 15420
    if KREDI_KARTI_STOK <= 0:
        KREDI_KARTI_STOK = 12850

@bot.message_handler(commands=["start"])
def start(message):
    user_id = message.from_user.id
    kullanici_kaydet(message.from_user)

    if ban_kontrol(user_id):
        cursor.execute("SELECT ban_sebebi, ban_bitis FROM users WHERE user_id = ?", (user_id,))
        b_bilgi = cursor.fetchone()
        sebep = b_bilgi[0] if b_bilgi and b_bilgi[0] else "Belirtilmemiş"
        try:
            bot.reply_to(message, f"❌ Bot tarafından yasaklandınız.\n ⛔ Yönetici erişiminizi açana kadar bot size cevap veremez.\n📝 Sebep: {sebep}")
        except Exception:
            pass
        return

    args = message.text.split()
    if len(args) > 1:
        ref = args[1]
        if ref.startswith("ref_"):
            try:
                ref_id = int(ref.replace("ref_", ""))
                if ref_id != user_id:
                    cursor.execute("SELECT referans_sahibi FROM users WHERE user_id = ?", (user_id,))
                    sonuc = cursor.fetchone()
                    if sonuc and sonuc[0] is None:
                        cursor.execute("UPDATE users SET referans_sahibi = ? WHERE user_id = ?", (ref_id, user_id))
                        cursor.execute("UPDATE users SET referans_puani = referans_puani + 2, kazandirdigi_uye = kazandirdigi_uye + 1 WHERE user_id = ?", (ref_id,))
                        db.commit()
            except Exception:
                pass

    kanal_mesaji(message.chat.id)

@bot.message_handler(func=lambda message: ban_kontrol(message.from_user.id))
def banli_engeli(message):
    cursor.execute("SELECT ban_sebebi FROM users WHERE user_id = ?", (message.from_user.id,))
    b_bilgi = cursor.fetchone()
    sebep = b_bilgi[0] if b_bilgi and b_bilgi[0] else "Belirtilmemiş"
    try:
        bot.reply_to(message, f"❌ Bot tarafından yasaklandınız. Yönetici erişiminizi açana kadar bot size cevap veremez.\n📝 Sebep: {sebep}")
    except Exception:
        pass

@bot.callback_query_handler(func=lambda call: call.data == "kanal_kontrol")
def kontrol_et(call):
    user_id = call.from_user.id
    if ban_kontrol(user_id):
        try:
            bot.answer_callback_query(call.id, "❌ Yasaklısınız!", show_alert=True)
        except Exception:
            pass
        return

    if admin_mi(user_id) or uyelik_kontrol(user_id):
        ana_menu(call, yeni_mesaj=False)
        try:
            bot.answer_callback_query(call.id, "✅ Doğrulandı!")
        except Exception:
            pass
    else:
        try:
            bot.answer_callback_query(call.id, "❌ Önce kanal ve gruba katılmalısın.", show_alert=True)
        except Exception:
            pass

def ana_menu(call, yeni_mesaj=False):
    keyboard = types.InlineKeyboardMarkup()
    keyboard.row(
        types.InlineKeyboardButton("🛍 ÜRÜNLER", callback_data="urunler"),
        types.InlineKeyboardButton("⚡ REFERANS", callback_data="referans")
    )
    metin = "𝐙𝐀𝐘𝐑𝐄XZ 𝐌𝐀𝐑𝐊Ե𝐓\n\n🤖 Hoş geldin! İşlem seç:"
    try:
        if yeni_mesaj:
            bot.send_message(call.message.chat.id, metin, reply_markup=keyboard)
        else:
            bot.edit_message_text(metin, call.message.chat.id, call.message.message_id, reply_markup=keyboard)
    except Exception as e:
        print(f"Ana menü gönderilirken hata: {e}")

@bot.callback_query_handler(func=lambda call: call.data == "ana_menu")
def ana_menu_callback(call):
    ana_menu(call, yeni_mesaj=False)
    try:
        bot.answer_callback_query(call.id)
    except Exception:
        pass

@bot.callback_query_handler(func=lambda call: call.data == "urunler")
def urunler(call):
    user_id = call.from_user.id
    if ban_kontrol(user_id):
        try:
            bot.answer_callback_query(call.id, "❌ Yasaklısınız!", show_alert=True)
        except Exception:
            pass
        return

    cursor.execute("SELECT referans_puani FROM users WHERE user_id = ?", (user_id,))
    puan_sonuc = cursor.fetchone()
    puan = puan_sonuc[0] if puan_sonuc else 0

    keyboard = types.InlineKeyboardMarkup()
    keyboard.add(types.InlineKeyboardButton(f"🔥 İNSTAGRAM METHOD (Stok: {INSTAGRAM_STOK}) (30 Puan)", callback_data="insta_method_cek"))
    keyboard.add(types.InlineKeyboardButton(f"💳 KREDİ KARTI (Stok: {KREDI_KARTI_STOK}) (40 Puan)", callback_data="kredi_karti_cek"))
    keyboard.add(types.InlineKeyboardButton("🔙 GERİ", callback_data="ana_menu"))

    try:
        bot.edit_message_text(
            f"🛍 ÜRÜNLER\n\n📊 Puanın: {puan} ⭐",
            call.message.chat.id, call.message.message_id, reply_markup=keyboard
        )
        bot.answer_callback_query(call.id)
    except Exception as e:
        print(f"Ürünler menüsü hatası: {e}")

@bot.callback_query_handler(func=lambda call: call.data == "insta_method_cek")
def insta_method_cek(call):
    global INSTAGRAM_STOK
    user_id = call.from_user.id
    if ban_kontrol(user_id): return

    cursor.execute("SELECT referans_puani FROM users WHERE user_id = ?", (user_id,))
    puan = cursor.fetchone()[0]

    if not admin_mi(user_id) and puan < 30:
        try:
            bot.answer_callback_query(call.id, "❌ Yetersiz puan! (30 Puan gerekli)", show_alert=True)
        except Exception:
            pass
        return

    if not admin_mi(user_id):
        cursor.execute("UPDATE users SET referans_puani = referans_puani - 30 WHERE user_id = ?", (user_id,))
        db.commit()

    if INSTAGRAM_STOK > 0: INSTAGRAM_STOK -= 1
    stoklari_kontrol_et_ve_yenile()

    secilen_set = random.choice(INSTAGRAM_SETLERI)
    cursor.execute("SELECT referans_puani FROM users WHERE user_id = ?", (user_id,))
    kalan_puan = cursor.fetchone()[0]

    keyboard = types.InlineKeyboardMarkup()
    keyboard.add(types.InlineKeyboardButton("🔄 YENISINI ÇEK (30 Puan)", callback_data="insta_method_cek"))
    keyboard.add(types.InlineKeyboardButton("🔙 ÜRÜNLERE DÖN", callback_data="urunler"))

    try:
        bot.edit_message_text(f"`{secilen_set}`\n\n⭐ Kalan Puan: {kalan_puan}", call.message.chat.id, call.message.message_id, reply_markup=keyboard, parse_mode="Markdown")
        bot.answer_callback_query(call.id, "✅ Getirildi!")
    except Exception as e:
        print(f"Instagram method çekme hatası: {e}")

@bot.callback_query_handler(func=lambda call: call.data == "kredi_karti_cek")
def kredi_karti_cek(call):
    global KREDI_KARTI_STOK
    user_id = call.from_user.id
    if ban_kontrol(user_id): return

    cursor.execute("SELECT referans_puani FROM users WHERE user_id = ?", (user_id,))
    puan = cursor.fetchone()[0]

    if not admin_mi(user_id) and puan < 40:
        try:
            bot.answer_callback_query(call.id, "❌ Yetersiz puan! (40 Puan gerekli)", show_alert=True)
        except Exception:
            pass
        return

    if not admin_mi(user_id):
        cursor.execute("UPDATE users SET referans_puani = referans_puani - 40 WHERE user_id = ?", (user_id,))
        db.commit()

    if KREDI_KARTI_STOK > 0: KREDI_KARTI_STOK -= 1
    stoklari_kontrol_et_ve_yenile()

    secilen_kart = random.choice(KREDI_KARTLARI)
    cursor.execute("SELECT referans_puani FROM users WHERE user_id = ?", (user_id,))
    kalan_puan = cursor.fetchone()[0]

    keyboard = types.InlineKeyboardMarkup()
    keyboard.add(types.InlineKeyboardButton("🔄 YENISINI ÇEK (40 Puan)", callback_data="kredi_karti_cek"))
    keyboard.add(types.InlineKeyboardButton("🔙 ÜRÜNLERE DÖN", callback_data="urunler"))

    try:
        bot.edit_message_text(f"💳 **KREDİ KARTI**\n\n{secilen_kart}\n\n⭐ Kalan Puan: {kalan_puan}", call.message.chat.id, call.message.message_id, reply_markup=keyboard, parse_mode="Markdown")
        bot.answer_callback_query(call.id, "✅ Getirildi!")
    except Exception as e:
        print(f"Kredi kartı çekme hatası: {e}")

@bot.callback_query_handler(func=lambda call: call.data == "referans")
def referans_menu(call):
    user_id = call.from_user.id
    if ban_kontrol(user_id):
        try:
            bot.answer_callback_query(call.id, "❌ Yasaklısınız!", show_alert=True)
        except Exception:
            pass
        return

    cursor.execute("SELECT referans_puani FROM users WHERE user_id = ?", (user_id,))
    mevcut_referans = cursor.fetchone()[0]
    referans_linki = f"https://t.me/{BOT_USERNAME}?start=ref_{user_id}"

    mesaj = f"⚡ Referans Puanın: {mevcut_referans}\n\n🔗 Linkin:\n{referans_linki}"
    markup = types.InlineKeyboardMarkup()
    markup.add(types.InlineKeyboardButton("📤 GÖNDER", url=f"https://t.me/share/url?url={referans_linki}&text=Gelin!"))
    markup.add(types.InlineKeyboardButton("🔙 GERİ", callback_data="ana_menu"))

    try:
        bot.answer_callback_query(call.id)
        bot.edit_message_text(mesaj, call.message.chat.id, call.message.message_id, reply_markup=markup)
    except Exception as e:
        print(f"Referans menüsü hatası: {e}")

@bot.callback_query_handler(func=lambda call: call.data.startswith("unban_btn_"))
def unban_buton_ile(call):
    if not admin_mi(call.from_user.id): return
    hedef_id = int(call.data.replace("unban_btn_", ""))

    cursor.execute("UPDATE users SET ban_durumu = 0, ban_bitis = 0, ban_sebebi = '' WHERE user_id = ?", (hedef_id,))
    db.commit()

    try:
        bot.answer_callback_query(call.id, "✅ Kullanıcının yasağı kaldırıldı!")
        bot.edit_message_text(f"✅ ID: {hedef_id} olan kullanıcının yasağı başarıyla kaldırıldı.", call.message.chat.id, call.message.message_id)
    except Exception:
        pass

    try:
        bot.send_message(hedef_id, "🎉 Yasağınız kaldırıldı!")
    except Exception:
        pass

@bot.message_handler(commands=["uye"])
def uye_sayisi(message):
    if not admin_mi(message.from_user.id): return
    cursor.execute("SELECT COUNT(*) FROM users")
    toplam = cursor.fetchone()[0]
    try:
        bot.reply_to(message, f"📊 Botu kullanan toplam kişi sayısı: {toplam}")
    except Exception:
        pass

@bot.message_handler(commands=["genel"])
def genel_liste(message):
    if not admin_mi(message.from_user.id): return
    cursor.execute("SELECT username, user_id, referans_puani, kazandirdigi_uye FROM users")
    kullanicilar = cursor.fetchall()

    if not kullanicilar:
        try:
            bot.reply_to(message, "❌ Kayıtlı kullanıcı bulunmuyor.")
        except Exception:
            pass
        return

    metin = ""
    for row in kullanicilar:
        u_adi = f"@{row[0]}" if row[0] else "Kullanıcı adı yok"
        u_id = row[1]
        u_puan = row[2]
        u_kazanan = row[3]

        parca = f"______________\n{u_adi}\n{u_id}\nReferans puanı: {u_puan}\nKazandırdığı üye: {u_kazanan}\n______________\n\n"
        if len(metin + parca) > 3500:
            try:
                bot.send_message(message.chat.id, metin)
            except Exception:
                pass
            metin = ""
        metin += parca
    if metin:
        try:
            bot.send_message(message.chat.id, metin)
        except Exception:
            pass

@bot.message_handler(commands=["admin"])
def admin_yardim(message):
    if not admin_mi(message.from_user.id): return

    yardim_metni = (
        "👑 **ADMİN KOMUT PANELİ VE AÇIKLAMALARI**\n\n"
        "🔹 `/uye`\n"
        "   ➜ Botu kullanan toplam kişi sayısını gösterir.\n\n"
        "🔹 `/genel`\n"
        "   ➜ Tüm kullanıcıları kullanıcı adı, İD, puan ve kazandırdığı üye olarak listeler.\n\n"
        "🔹 `/ban <kullanici> <süre_opsiyonel> <sebep>`\n"
        "   ➜ Kullanıcıyı kalıcı veya süreli banlar.\n\n"
        "🔹 `/unban <kullanici> <mesaj>`\n"
        "   ➜ Kullanıcının banını kaldırır ve belirttiğiniz mesajı iletir.\n\n"
        "🔹 `/yasak`\n"
        "   ➜ Yasaklı/sesi kapalı olan kullanıcıları listeler.\n\n"
        "🔹 `/ref <kullanici> <puan>`\n"
        "   ➜ Kullanıcıya referans puanı ekler.\n\n"
        "🔹 `/duyuru <mesaj>`\n"
        "   ➜ Tüm kullanıcılara duyuru gönderir."
    )
    try:
        bot.reply_to(message, yardim_metni, parse_mode="Markdown")
    except Exception:
        pass

@bot.message_handler(commands=["ban"])
def banla(message):
    if not admin_mi(message.from_user.id): return
    args = message.text.split(maxsplit=3)
    if len(args) < 2:
        try:
            bot.reply_to(message, "❌ Kullanım: /ban @kullanici [süre örn: 1 gün] [sebep mesajı]")
        except Exception:
            pass
        return

    hedef = args[1].replace("@", "")
    kalan_metin = args[2] if len(args) > 2 else ""

    saniye_ekle = 0
    sebep = kalan_metin

    if "gün" in kalan_metin.lower() or "saat" in kalan_metin.lower() or "dakika" in kalan_metin.lower():
        parcalar = kalan_metin.split(maxsplit=2)
        try:
            sayi = int(parcalar[0])
            birim = parcalar[1].lower()
            if "gün" in birim:
                saniye_ekle = sayi * 86400
            elif "saat" in birim:
                saniye_ekle = sayi * 3600
            elif "dakika" in birim:
                saniye_ekle = sayi * 60

            sebep = parcalar[2] if len(parcalar) > 2 else "Belirtilmemiş"
        except Exception:
            sebep = kalan_metin

    if hedef.isdigit():
        cursor.execute("SELECT user_id, username FROM users WHERE user_id = ?", (int(hedef),))
    else:
        cursor.execute("SELECT user_id, username FROM users WHERE username = ?", (hedef,))

    sonuc = cursor.fetchone()
    if not sonuc:
        try:
            bot.reply_to(message, "❌ Kullanıcı veritabanında bulunamadı!")
        except Exception:
            pass
        return

    hedef_id = sonuc[0]
    ban_bitis_zamani = int(time.time() + saniye_ekle) if saniye_ekle > 0 else 0

    cursor.execute("UPDATE users SET ban_durumu = 1, ban_bitis = ?, ban_sebebi = ? WHERE user_id = ?", (ban_bitis_zamani, sebep, hedef_id))
    db.commit()

    sure_str = f"Süreli ({kalan_metin})" if saniye_ekle > 0 else "Kalıcı"
    try:
        bot.reply_to(message, f"✅ Kullanıcı banlandı!\n🔒 Tür: {sure_str}\n📝 Sebep: {sebep}")
    except Exception:
        pass

    try:
        bot.send_message(hedef_id, f"❌ Bot tarafından yasaklandınız.\n📝 Sebep: {sebep}")
    except Exception:
        pass

@bot.message_handler(commands=["unban"])
def unbanla(message):
    if not admin_mi(message.from_user.id): return
    args = message.text.split(maxsplit=2)
    if len(args) < 2:
        try:
            bot.reply_to(message, "❌ Kullanım: /unban @kullaniciadi veya ID <mesajınız>")
        except Exception:
            pass
        return

    hedef = args[1].replace("@", "")
    unban_mesaji = args[2] if len(args) > 2 else "Yasağınız kaldırıldı."

    if hedef.isdigit():
        cursor.execute("SELECT user_id FROM users WHERE user_id = ?", (int(hedef),))
    else:
        cursor.execute("SELECT user_id FROM users WHERE username = ?", (hedef,))

    sonuc = cursor.fetchone()
    if not sonuc:
        try:
            bot.reply_to(message, "❌ Kullanıcı veritabanında bulunamadı!")
        except Exception:
            pass
        return

    hedef_id = sonuc[0]
    cursor.execute("UPDATE users SET ban_durumu = 0, ban_bitis = 0, ban_sebebi = '' WHERE user_id = ?", (hedef_id,))
    db.commit()

    try:
        bot.reply_to(message, f"✅ Kullanıcının yasağı kaldırıldı ve mesajı iletildi.")
    except Exception:
        pass

    try:
        bot.send_message(hedef_id, f"🎉 Yasağınız kaldırıldı.\n💬 Adminin size bıraktığı mesaj: {unban_mesaji}")
    except Exception:
        pass

@bot.message_handler(commands=["yasak"])
def yasakli_listesi(message):
    if not admin_mi(message.from_user.id): return

    cursor.execute("SELECT user_id, username, ban_sebebi FROM users WHERE ban_durumu = 1")
    yasaklilar = cursor.fetchall()

    if not yasaklilar:
        try:
            bot.reply_to(message, "🟢 Şu anda yasaklı/sesi kapalı hiçbir kullanıcı bulunmuyor.")
        except Exception:
            pass
        return

    try:
        bot.reply_to(message, "🚫 **YASAKLI / SESİ KAPALI KULLANICILAR:**")
    except Exception:
        pass
    
    for row in yasaklilar:
        u_id = row[0]
        u_adi = f"@{row[1]}" if row[1] else "Kullanıcı adı yok"
        sebep = row[2] if row[2] else "Sebep belirtilmemiş"

        markup = types.InlineKeyboardMarkup()
        markup.add(types.InlineKeyboardButton("🔓 SESİ AÇ (UNBAN)", callback_data=f"unban_btn_{u_id}"))

        try:
            bot.send_message(message.chat.id, f"👤 {u_adi}\n🆔 ID: `{u_id}`\n📝 Sebep: {sebep}", reply_markup=markup, parse_mode="Markdown")
        except Exception:
            pass

@bot.message_handler(commands=["ref"])
def admin_puan_ver(message):
    if not admin_mi(message.from_user.id): return
    args = message.text.split()
    if len(args) < 3:
        try:
            bot.reply_to(message, "❌ Kullanım: /ref @kullaniciadi veya ID <puan>")
        except Exception:
            pass
        return

    hedef = args[1].replace("@", "")
    try:
        eklenecek_puan = int(args[2])
    except ValueError:
        try:
            bot.reply_to(message, "❌ Puan kısmı sayı olmalıdır!")
        except Exception:
            pass
        return

    if hedef.isdigit():
        cursor.execute("SELECT user_id, referans_puani FROM users WHERE user_id = ?", (int(hedef),))
    else:
        cursor.execute("SELECT user_id, referans_puani FROM users WHERE username = ?", (hedef,))

    sonuc = cursor.fetchone()
    if not sonuc:
        try:
            bot.reply_to(message, "❌ Kullanıcı veritabanında bulunamadı!")
        except Exception:
            pass
        return

    hedef_id = sonuc[0]
    mevcut_puan = sonuc[1] + eklenecek_puan

    cursor.execute("UPDATE users SET referans_puani = ? WHERE user_id = ?", (mevcut_puan, hedef_id))
    db.commit()

    try:
        bot.reply_to(message, f"✅ Başarıyla {hedef} adlı kullanıcıya {eklenecek_puan} puan eklendi.")
    except Exception:
        pass
        
    try:
        bot.send_message(hedef_id, f"🎉 Admin tarafından **{eklenecek_puan}** referans kazandınız!\n⭐ Mevcut Puanınız: {mevcut_puan}", parse_mode="Markdown")
    except Exception:
        pass

@bot.message_handler(commands=["duyuru"])
def duyuru_gonder(message):
    if not admin_mi(message.from_user.id): return
    args = message.text.split(maxsplit=1)
    if len(args) < 2:
        try:
            bot.reply_to(message, "❌ Kullanım: /duyuru <Mesajınız>")
        except Exception:
            pass
        return

    duyuru_metni = args[1]
    cursor.execute("SELECT user_id FROM users")
    kullanicilar = cursor.fetchall()

    basarili = 0
    basarisiz = 0
    for row in kullanicilar:
        u_id = row[0]
        try:
            bot.send_message(u_id, f"📢 **DUYURU**\n\n{duyuru_metni}", parse_mode="Markdown")
            basarili += 1
        except Exception:
            basarisiz += 1

    try:
        bot.reply_to(message, f"✅ Duyuru gönderildi!\nİletilen: {basarili}\nİletilemeyen: {basarisiz}")
    except Exception:
        pass

print("Bot çalışıyor...")
while True:
    try:
        bot.infinity_polling(timeout=60, long_polling_timeout=30)
    except Exception as e:
        print(f"Bağlantı hatası oluştu: {e}. 5 saniye sonra yeniden başlatılıyor...")
        time.sleep(5)
