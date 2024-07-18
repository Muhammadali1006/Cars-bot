import asyncio
from aiogram import Dispatcher, Bot, filters, types, F
# from aiogram.fsm.context import FSMContext
# from aiogram.fsm.state import State, StatesGroup
from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton
from aiogram.types import ReplyKeyboardMarkup, KeyboardButton, ReplyKeyboardRemove

bot = Bot(token="7331395047:AAFAtgw3_P_pxdfr7NfWcyyd2EhYgLphBMw")
dp = Dispatcher(bot=bot)

main_button = ReplyKeyboardMarkup(keyboard=[
    [KeyboardButton(text="🚙 Cars"), KeyboardButton(text="🛒 Orders")],
    [KeyboardButton(text="💸 Balance"), KeyboardButton(text="📲 My_info")]
], resize_keyboard=True)

cars_button = InlineKeyboardMarkup(inline_keyboard=[
    [InlineKeyboardButton(text="Uzb cars", callback_data="uzb"),
     InlineKeyboardButton(text="Euro cars", callback_data="euro")],
])

uzb_car_button = InlineKeyboardMarkup(inline_keyboard=[
    [InlineKeyboardButton(text="Matiz", callback_data="matiz"),
     InlineKeyboardButton(text="Spark", callback_data="spark"),
     InlineKeyboardButton(text="Nexia", callback_data="nexia")],
    [InlineKeyboardButton(text="Malibu", callback_data="malibu"),
     InlineKeyboardButton(text="Cobalt", callback_data="cobalt"),
     InlineKeyboardButton(text="Jentra", callback_data="jentra")],
])

matiz_button = InlineKeyboardMarkup(inline_keyboard=[
    [InlineKeyboardButton(text="⬛️ Qora rangli Matiz", callback_data="qora_matiz"),
     InlineKeyboardButton(text="⬜️ Oq rangli Matiz", callback_data="oq_matiz")],
    [InlineKeyboardButton(text="🟥 Qizil rangli Matiz", callback_data="qizil_matiz"),
     InlineKeyboardButton(text="🟨 Sariq rangli Matiz", callback_data="sariq_matiz")],
    [InlineKeyboardButton(text="🟦 Moviy rangli Matiz", callback_data="moviy_matiz"),
     InlineKeyboardButton(text="🟩 Yashil rangli Matiz", callback_data="yashil_matiz")],
])

matiz_btn = InlineKeyboardMarkup(inline_keyboard=[
    [InlineKeyboardButton(text="🛒 Savatga solish", callback_data="savat_solish_mz"),
     InlineKeyboardButton(text="🛒 Savatdan olish", callback_data="savat_olish_mz")],
    [InlineKeyboardButton(text="💸 Sotib olish", callback_data="sotib_ol"),
     InlineKeyboardButton(text="🔍 Menu", callback_data="menu")],
])

spark_button = InlineKeyboardMarkup(inline_keyboard=[
    [InlineKeyboardButton(text="⬛️ Qora rangli Spark", callback_data="qora_spark"),
     InlineKeyboardButton(text="⬜️ Oq rangli Spark", callback_data="oq_spark"),
     InlineKeyboardButton(text="🟥 Qizil rangli Matiz", callback_data="qizil_spark")],
    [InlineKeyboardButton(text="🟨 Sariq rangli Spark", callback_data="sariq_spark"),
     InlineKeyboardButton(text="🟦 Moviy rangli Spark", callback_data="moviy_spark"),
     InlineKeyboardButton(text="🟩 Yashil rangli Matiz", callback_data="yashil_spark")],
])

spark_btn = InlineKeyboardMarkup(inline_keyboard=[
    [InlineKeyboardButton(text="🛒 Savatga solish", callback_data="savat_solish_sk"),
     InlineKeyboardButton(text="🛒 Savatdan olish", callback_data="savat_olish_sk")],
    [InlineKeyboardButton(text="💸 Sotib olish", callback_data="sotib_ol"),
     InlineKeyboardButton(text="🔍 Menu", callback_data="menu")],
])

euro_car_button = InlineKeyboardMarkup(inline_keyboard=[
    [InlineKeyboardButton(text="BMW", callback_data="bmw"),
     InlineKeyboardButton(text="Porsche", callback_data="porsche"),
     InlineKeyboardButton(text="Tesla", callback_data="tesla")],
    [InlineKeyboardButton(text="Mersadez-Benz", callback_data="mers"),
     InlineKeyboardButton(text="Lamborghini", callback_data="lambo"),
     InlineKeyboardButton(text="Mustang", callback_data="ford")],
])

bmw_button = InlineKeyboardMarkup(inline_keyboard=[
    [InlineKeyboardButton(text="⬛️ Qora rangli BMW", callback_data="qora_bmw"),
     InlineKeyboardButton(text="⬜️ Oq rangli BMW", callback_data="oq_bmw"),
     InlineKeyboardButton(text="🟥 Qizil rangli BMW", callback_data="qizil_bmw")],
    [InlineKeyboardButton(text="🟨 Sariq rangli BMW", callback_data="sariq_bmw"),
     InlineKeyboardButton(text="🟦 Moviy rangli BMW", callback_data="moviy_bmw"),
     InlineKeyboardButton(text="🟩 Binafsha rangli BMW", callback_data="binafsha_bmw")],
])

bmw_btn = InlineKeyboardMarkup(inline_keyboard=[
    [InlineKeyboardButton(text="🛒 Savatga solish", callback_data="savat_solish_b"),
     InlineKeyboardButton(text="🛒 Savatdan olish", callback_data="savat_olish_b")],
    [InlineKeyboardButton(text="💸 Sotib olish", callback_data="sotib_ol"),
     InlineKeyboardButton(text="🔍 Menu", callback_data="menu")],
])

porsh_button = InlineKeyboardMarkup(inline_keyboard=[
    [InlineKeyboardButton(text="⬛️ Qora rangli Porsche", callback_data="qora_porsh"),
     InlineKeyboardButton(text="⬜️ Oq rangli Porsche", callback_data="oq_porsh"),
     InlineKeyboardButton(text="🟥 Qizil rangli Porsche", callback_data="qizil_porsh")],
    [InlineKeyboardButton(text="🟨 Sariq rangli Porsche", callback_data="sariq_porsh"),
     InlineKeyboardButton(text="🟦 Moviy rangli Porsche", callback_data="moviy_porsh"),
     InlineKeyboardButton(text="🟩 Yashil rangli Porsche", callback_data="yashil_porsh")],
])

porsh_btn = InlineKeyboardMarkup(inline_keyboard=[
    [InlineKeyboardButton(text="🛒 Savatga solish", callback_data="savat_solish_p"),
     InlineKeyboardButton(text="🛒 Savatdan olish", callback_data="savat_olish_p")],
    [InlineKeyboardButton(text="💸 Sotib olish", callback_data="sotib_ol"),
     InlineKeyboardButton(text="🔍 Menu", callback_data="menu")],
])

tesla_button = InlineKeyboardMarkup(inline_keyboard=[
    [InlineKeyboardButton(text="⬛️ Qora rangli Tesla", callback_data="qora_tesla"),
     InlineKeyboardButton(text="⬜️ Oq rangli Tesla", callback_data="oq_tesla"),
     InlineKeyboardButton(text="🟥 Qizil rangli Tesla", callback_data="qizil_tesla")],
    [InlineKeyboardButton(text="🟨 Sariq rangli Tesla", callback_data="sariq_tesla"),
     InlineKeyboardButton(text="🟦 Moviy rangli Tesla", callback_data="moviy_tesla"),
     InlineKeyboardButton(text="🔸 Tilla rangli Tesla", callback_data="tilla_tesla")],
])

tesla_btn = InlineKeyboardMarkup(inline_keyboard=[
    [InlineKeyboardButton(text="🛒 Savatga solish", callback_data="savat_solish_t"),
     InlineKeyboardButton(text="🛒 Savatdan olish", callback_data="savat_olish_t")],
    [InlineKeyboardButton(text="💸 Sotib olish", callback_data="sotib_ol"),
     InlineKeyboardButton(text="🔍 Menu", callback_data="menu")],
])

mers_button = InlineKeyboardMarkup(inline_keyboard=[
    [InlineKeyboardButton(text="⬛️ Qora rangli Mers", callback_data="qora_mers"),
     InlineKeyboardButton(text="⬜️ Oq rangli Mers", callback_data="oq_mers"),
     InlineKeyboardButton(text="🟥 Qizil rangli Mers", callback_data="qizil_mers")],
    [InlineKeyboardButton(text="🟨 Sariq rangli Mers", callback_data="sariq_mers"),
     InlineKeyboardButton(text="🟦 Moviy rangli Mers", callback_data="moviy_mers"),
     InlineKeyboardButton(text="🟩 Yashil rangli Mers", callback_data="yashil_mers")],
])

mers_btn = InlineKeyboardMarkup(inline_keyboard=[
    [InlineKeyboardButton(text="🛒 Savatga solish", callback_data="savat_solish_m"),
     InlineKeyboardButton(text="🛒 Savatdan olish", callback_data="savat_olish_m")],
    [InlineKeyboardButton(text="💸 Sotib olish", callback_data="sotib_ol"),
     InlineKeyboardButton(text="🔍 Menu", callback_data="menu")],
])

lambo_button = InlineKeyboardMarkup(inline_keyboard=[
    [InlineKeyboardButton(text="⬛️ Qora rangli Lamborghini", callback_data="qora_lambo"),
     InlineKeyboardButton(text="⬜️ Oq rangli Lamborghini", callback_data="oq_lambo"),
     InlineKeyboardButton(text="🟥 Qizil rangli Lamborghini", callback_data="qizil_lambo")],
    [InlineKeyboardButton(text="🟨 Sariq rangli Lamborghini", callback_data="sariq_lambo"),
     InlineKeyboardButton(text="🟦 Moviy rangli Lamborghini", callback_data="moviy_lambo"),
     InlineKeyboardButton(text="🟩 Yashil rangli Lamborghini", callback_data="yashil_lambo")],
])

lambo_btn = InlineKeyboardMarkup(inline_keyboard=[
    [InlineKeyboardButton(text="🛒 Savatga solish", callback_data="savat_solish_l"),
     InlineKeyboardButton(text="🛒 Savatdan olish", callback_data="savat_olish_l")],
    [InlineKeyboardButton(text="💸 Sotib olish", callback_data="sotib_ol"),
     InlineKeyboardButton(text="🔍 Menu", callback_data="menu")],
])

ford_button = InlineKeyboardMarkup(inline_keyboard=[
    [InlineKeyboardButton(text="⬛️ Qora rangli Mustang", callback_data="qora_ford"),
     InlineKeyboardButton(text="⬜️ Oq rangli Mustang", callback_data="oq_ford"),
     InlineKeyboardButton(text="🟥 Qizil rangli Mustang", callback_data="qizil_ford")],
    [InlineKeyboardButton(text="🟨 Sariq rangli Mustang", callback_data="sariq_ford"),
     InlineKeyboardButton(text="🟦 Moviy rangli Mustang", callback_data="moviy_ford"),
     InlineKeyboardButton(text="🟩 Yashil rangli Mustang", callback_data="yashil_ford")],
])

ford_btn = InlineKeyboardMarkup(inline_keyboard=[
    [InlineKeyboardButton(text="🛒 Savatga solish", callback_data="savat_solish_f"),
     InlineKeyboardButton(text="🛒 Savatdan olish", callback_data="savat_olish_f")],
    [InlineKeyboardButton(text="💸 Sotib olish", callback_data="sotib_ol"),
     InlineKeyboardButton(text="🔍 Menu", callback_data="menu")],
])

kart_button = InlineKeyboardMarkup(inline_keyboard=[
    [InlineKeyboardButton(text="💳 Uzcard", callback_data="uzcard"),
     InlineKeyboardButton(text="💳 Humo", callback_data="humo")],
    [InlineKeyboardButton(text="🔍 Menu", callback_data="menu")]
])

balance = 500000
orders = []


@dp.message(filters.Command("start"))
async def start(message: types.Message):
    await message.answer(f"Xush kelibsiz {message.from_user.full_name}, sizga mashinalar yoqadimi ?",
                         reply_markup=main_button)


@dp.message(F.text == "🚙 Cars")
async def cars_function(message: types.Message):
    await message.answer("Xush kelibsiz !!!", reply_markup=ReplyKeyboardRemove())
    await message.answer("Qaysi turdagi moshinani tanlisiz?", reply_markup=cars_button)


@dp.message(F.text == "📲 My_info")
async def info_function(message: types.Message):
    await message.answer(
        f"\n \n Sizning ismingiz {message.from_user.full_name} \n Sizning user name {message.from_user.username} \n Sizning id ingiz {message.from_user.id} \n \n",
        reply_markup=main_button)


@dp.callback_query(F.data == "menu")
async def menu_function(call: types.CallbackQuery):
    await call.message.answer("Siz Menu bo'limiga o'tdingiz", reply_markup=main_button)


@dp.callback_query(F.data == "euro")
async def cars_function(call: types.CallbackQuery):
    await call.message.answer_photo(
        photo="https://hips.hearstapps.com/hmg-prod/amv-prod-cad-assets/images/media/671589/2017-10best-cars-the-best-cars-for-sale-in-america-today-feature-car-and-driver-photo-672522-s-original.jpg?resize=640:*",
        caption="Siz Euro mashinalar bo'limini tanladingiz !!!", reply_markup=euro_car_button)


@dp.callback_query(F.data == "uzb")
async def cars_function(call: types.CallbackQuery):
    await call.message.answer_photo(photo="https://daryo.uz/cache/2018/07/gm-680x453.jpg",
                                    caption="Siz Uzbek mashinalar bo'limini tanladingiz !!!",
                                    reply_markup=uzb_car_button)


@dp.callback_query(F.data == "bmw")
async def bmw_function(call: types.CallbackQuery):
    await call.message.answer_photo(photo="https://www.carsome.my/news/wp-content/uploads/2023/07/BMW-M-Cars.jpg",
                                    caption="Siz BMW bo'limini tanladingiz. \n Bu yerdan siz o'zizga yoqqan ranglisini tanlay olasiz !!!",
                                    reply_markup=bmw_button)


@dp.callback_query(F.data == "qora_bmw")
async def bmw_function(call: types.CallbackQuery):
    await call.message.answer_photo(photo="https://cdn.kodixauto.ru/media/image/6100204caf109ce030c18fe6",
                                    caption="Siz qora rangli BMWni tanladingiz. \n Mahsulot nomi: BMW \n Narxi: 40000 \n Rangi: qora \n Yili: 2024 \n Mahsulot sifati: A'lo \n \n",
                                    reply_markup=bmw_btn)


@dp.callback_query(F.data == "oq_bmw")
async def bmw_function(call: types.CallbackQuery):
    await call.message.answer_photo(
        photo="https://quto.ru/imgs/2021/12/01/14/5067227/301b8c6e781b4dee30c4b9fd58ddb870abe7ca3a.jpeg",
        caption="Siz oq rangli BMWni tanladingiz. \n Mahsulot nomi: BMW \n Narxi: 40000 \n Rangi: oq \n Yili: 2024 \n Mahsulot sifati: A'lo \n \n",
        reply_markup=bmw_btn)


@dp.callback_query(F.data == "qizil_bmw")
async def bmw_function(call: types.CallbackQuery):
    await call.message.answer_photo(
        photo="https://avatars.mds.yandex.net/get-verba/1030388/2a0000018da1f30251e347a41305d485f160/cattouchretcr",
        caption="Siz qizil rangli BMWni tanladingiz. \n Mahsulot nomi: BMW \n Narxi: 40000 \n Rangi: qizil \n Yili: 2024 \n Mahsulot sifati: A'lo \n \n",
        reply_markup=bmw_btn)


@dp.callback_query(F.data == "sariq_bmw")
async def bmw_function(call: types.CallbackQuery):
    await call.message.answer_photo(photo="https://cdn.motor1.com/images/mgl/mr32B/s3/bmw-m4.jpg",
                                    caption="Siz sariq rangli BMWni tanladingiz. \n Mahsulot nomi: BMW \n Narxi: 40000 \n Rangi: sariq \n Yili: 2024 \n Mahsulot sifati: A'lo \n \n",
                                    reply_markup=bmw_btn)


@dp.callback_query(F.data == "moviy_bmw")
async def bmw_function(call: types.CallbackQuery):
    await call.message.answer_photo(
        photo="https://www.bmw-kz.com/content/dam/bmw/common/all-models/m-series/series-overview/bmw-m-series-seo-overview-ms-08.jpg",
        caption="Siz movif rangli BMWni tanladingiz. \n Mahsulot nomi: BMW \n Narxi: 40000 \n Rangi: moviy \n Yili: 2024 \n Mahsulot sifati: A'lo \n \n",
        reply_markup=bmw_btn)


@dp.callback_query(F.data == "binafsha_bmw")
async def bmw_function(call: types.CallbackQuery):
    await call.message.answer_photo(photo="https://carsdo.ru/job/CarsDo/photo/model/bmw-2-coupe-2-model.jpg",
                                    caption="Siz binafsha rangli BMWni tanladingiz. \n Mahsulot nomi: BMW \n Narxi: 40000 \n Rangi: Binafsha \n Yili: 2024 \n Mahsulot sifati: A'lo \n \n",
                                    reply_markup=bmw_btn)


@dp.callback_query(F.data == "savat_solish_b")
async def savat_function(call: types.CallbackQuery):
    global balance
    balance = balance - 40000
    orders.append(" BMW narxi: 40000$")
    await call.message.answer("Siz BMWni savat soldingiz", reply_markup=main_button)


@dp.callback_query(F.data == "savat_olish_b")
async def savat_function(call: types.CallbackQuery):
    global balance
    balance = balance + 40000
    orders.remove(" BMW narxi: 40000$")
    await call.message.answer("Siz BMWni savat oldingiz", reply_markup=main_button)


@dp.callback_query(F.data == "porsche")
async def bmw_function(call: types.CallbackQuery):
    await call.message.answer_photo(
        photo="https://newsroom.porsche.com/.imaging/mte/porsche-templating-theme/image_1290x726/dam/pnr/2021/Company/Porsche-achieves-robust-level-of-deliveries-in-2020-/Porsche-achieves-robust-level-of-deliveries-in-2020.jpeg0/jcr:content/Porsche%20achieves%20robust%20level%20of%20deliveries%20in%202020.jpeg",
        caption="Siz Porsche bo'limini tanladingiz. \n Bu yerdan siz o'zizga yoqqan ranglisini tanlay olasiz !!!",
        reply_markup=porsh_button)


@dp.callback_query(F.data == "qora_porsh")
async def bmw_function(call: types.CallbackQuery):
    await call.message.answer_photo(photo="https://storage.googleapis.com/pod_public/750/183511.jpg",
                                    caption="Siz qora rangli Porscheni tanladingiz. \n Mahsulot nomi: Porsche \n Narxi: 38000 \n Rangi: qora \n Yili: 2024 \n Mahsulot sifati: A'lo \n \n",
                                    reply_markup=porsh_btn)


@dp.callback_query(F.data == "oq_porsh")
async def bmw_function(call: types.CallbackQuery):
    await call.message.answer_photo(
        photo="https://hips.hearstapps.com/hmg-prod/images/2025-porsche-taycan-118-660b044a263dd.jpg?crop=0.807xw:0.603xh;0.0732xw,0.324xh&resize=640:*",
        caption="Siz oq rangli Porscheni tanladingiz. \n Mahsulot nomi: Porsche \n Narxi: 38000 \n Rangi: oq \n Yili: 2024 \n Mahsulot sifati: A'lo \n \n",
        reply_markup=porsh_btn)


@dp.callback_query(F.data == "qizil_porsh")
async def bmw_function(call: types.CallbackQuery):
    await call.message.answer_photo(
        photo="https://newsroom.porsche.com/.imaging/mte/porsche-templating-theme/image_1290x726/dam/pnr/2022/Company/Porsche-deliveries-2021/The-all-electric-Porsche-Taycan-saw-an-outstanding-increase-with-41,296-units.jpeg/jcr:content/The%20all-electric%20Porsche%20Taycan%20saw%20an%20outstanding%20increase%20with%2041,296%20units.jpeg",
        caption="Siz qizil rangli Porscheni tanladingiz. \n Mahsulot nomi: Porsche \n Narxi: 38000 \n Rangi: qizil \n Yili: 2024 \n Mahsulot sifati: A'lo \n \n",
        reply_markup=porsh_btn)


@dp.callback_query(F.data == "sariq_porsh")
async def bmw_function(call: types.CallbackQuery):
    await call.message.answer_photo(
        photo="https://newsroom.porsche.com/.imaging/mte/porsche-templating-theme/image_1290x726/dam/AU_local/2022/Products_AU/911-GTS--Product-Highlights/911-GTS-Australian-images---exterior-static/PORSCHE_TAYCANGTS_911GTS_DKIMG_0920.jpg/jcr:content/PORSCHE_TAYCANGTS_911GTS_DKIMG_0920.jpg",
        caption="Siz sariq rangli Porscheni tanladingiz. \n Mahsulot nomi: Porsche \n Narxi: 38000 \n Rangi: sariq \n Yili: 2024 \n Mahsulot sifati: A'lo \n \n",
        reply_markup=porsh_btn)


@dp.callback_query(F.data == "moviy_porsh")
async def bmw_function(call: types.CallbackQuery):
    await call.message.answer_photo(
        photo="https://editorial.pxcrush.net/carsales/general/editorial/2023-porsche-718-boxster-style-edition-08.jpg",
        caption="Siz movif rangli Porscheni tanladingiz. \n Mahsulot nomi: Porsche \n Narxi: 38000 \n Rangi: moviy \n Yili: 2024 \n Mahsulot sifati: A'lo \n \n",
        reply_markup=porsh_btn)


@dp.callback_query(F.data == "yashil_porsh")
async def bmw_function(call: types.CallbackQuery):
    await call.message.answer_photo(photo="https://static.autox.com/uploads/2024/03/Porsche-911-Carrera-T.jpg",
                                    caption="Siz yashil rangli Porscheni tanladingiz. \n Mahsulot nomi: Porsche \n Narxi: 38000 \n Rangi: Yashil \n Yili: 2024 \n Mahsulot sifati: A'lo \n \n",
                                    reply_markup=porsh_btn)


@dp.callback_query(F.data == "savat_solish_p")
async def savat_function(call: types.CallbackQuery):
    global balance
    balance = balance - 38000
    orders.append(" Porsche narxi: 38000$")
    await call.message.answer("Siz Porscheni savat soldingiz", reply_markup=main_button)


@dp.callback_query(F.data == "savat_olish_p")
async def savat_function(call: types.CallbackQuery):
    global balance
    balance = balance + 38000
    orders.remove(" Porsche narxi: 38000$")
    await call.message.answer("Siz Porscheni savat oldingiz", reply_markup=main_button)


@dp.callback_query(F.data == "tesla")
async def bmw_function(call: types.CallbackQuery):
    await call.message.answer_photo(
        photo="https://electrek.co/wp-content/uploads/sites/3/2021/05/Tesla-Logo-Hero.jpg?quality=82&strip=all&w=1024",
        caption="Siz Tesla bo'limini tanladingiz. \n Bu yerdan siz o'zizga yoqqan ranglisini tanlay olasiz !!!",
        reply_markup=tesla_button)


@dp.callback_query(F.data == "qora_tesla")
async def bmw_function(call: types.CallbackQuery):
    await call.message.answer_photo(
        photo="https://kapital.uz/wp-content/uploads/2021/08/5ea6dd8dec05c41134000004_large.jpg",
        caption="Siz qora rangli Teslani tanladingiz. \n Mahsulot nomi: Tesla \n Narxi: 32000 \n Rangi: qora \n Yili: 2024 \n Mahsulot sifati: A'lo \n \n",
        reply_markup=tesla_btn)


@dp.callback_query(F.data == "oq_tesla")
async def bmw_function(call: types.CallbackQuery):
    await call.message.answer_photo(
        photo="https://media.cnn.com/api/v1/images/stellar/prod/gettyimages-2113300644.jpg?c=16x9&q=h_833,w_1480,c_fill",
        caption="Siz oq rangli Teslani tanladingiz. \n Mahsulot nomi: Tesla \n Narxi: 32000 \n Rangi: oq \n Yili: 2024 \n Mahsulot sifati: A'lo \n \n",
        reply_markup=tesla_btn)


@dp.callback_query(F.data == "qizil_tesla")
async def bmw_function(call: types.CallbackQuery):
    await call.message.answer_photo(photo="https://car-images.bauersecure.com/wp-images/3033/021_tesla_model_3.jpg",
                                    caption="Siz qizil rangli Teslani tanladingiz. \n Mahsulot nomi: Tesla \n Narxi: 32000 \n Rangi: qizil \n Yili: 2024 \n Mahsulot sifati: A'lo \n \n",
                                    reply_markup=tesla_btn)


@dp.callback_query(F.data == "sariq_tesla")
async def bmw_function(call: types.CallbackQuery):
    await call.message.answer_photo(
        photo="https://s1.cdn.autoevolution.com/images/news/nyc-yellow-cab-fleet-now-includes-tesla-model-3-138684-7.jpg",
        caption="Siz sariq rangli Teslani tanladingiz. \n Mahsulot nomi: Tesla \n Narxi: 32000 \n Rangi: sariq \n Yili: 2024 \n Mahsulot sifati: A'lo \n \n",
        reply_markup=tesla_btn)


@dp.callback_query(F.data == "moviy_tesla")
async def bmw_function(call: types.CallbackQuery):
    await call.message.answer_photo(
        photo="https://d2hucwwplm5rxi.cloudfront.net/wp-content/uploads/2021/12/09084606/tesla-2020-129020210149.jpg",
        caption="Siz movif rangli Teslani tanladingiz. \n Mahsulot nomi: Tesla \n Narxi: 32000 \n Rangi: moviy \n Yili: 2024 \n Mahsulot sifati: A'lo \n \n",
        reply_markup=tesla_btn)


@dp.callback_query(F.data == "tilla_tesla")
async def bmw_function(call: types.CallbackQuery):
    await call.message.answer_photo(
        photo="https://masterpiecer-images.s3.yandex.net/95afff9999dd11eea07a5ece24738c58:upscaled",
        caption="Siz tilla rangli Teslani tanladingiz. \n Mahsulot nomi: Tesla \n Narxi: 32000 \n Rangi: Tilla \n Yili: 2024 \n Mahsulot sifati: A'lo \n \n",
        reply_markup=tesla_btn)


@dp.callback_query(F.data == "savat_solish_t")
async def savat_function(call: types.CallbackQuery):
    global balance
    balance = balance - 32000
    orders.append(" Tesla narxi: 32000$")
    await call.message.answer("Siz Teslani savat soldingiz", reply_markup=main_button)


@dp.callback_query(F.data == "savat_olish_t")
async def savat_function(call: types.CallbackQuery):
    global balance
    balance = balance + 32000
    orders.remove(" Tesla narxi: 32000$")
    await call.message.answer("Siz Teslani savat oldingiz", reply_markup=main_button)


@dp.callback_query(F.data == "mers")
async def bmw_function(call: types.CallbackQuery):
    await call.message.answer_photo(
        photo="https://gorliniya.ru/wp-content/uploads/2020/02/Avtosalon-Mersedes-Bents-.jpg",
        caption="Siz Mers bo'limini tanladingiz. \n Bu yerdan siz o'zizga yoqqan ranglisini tanlay olasiz !!!",
        reply_markup=mers_button)


@dp.callback_query(F.data == "qora_mers")
async def bmw_function(call: types.CallbackQuery):
    await call.message.answer_photo(photo="https://repost.uz/storage/uploads/370-1656401821-avto-post-material.jpeg",
                                    caption="Siz qora rangli Mersni tanladingiz. \n Mahsulot nomi: Tesla \n Narxi: 42000 \n Rangi: qora \n Yili: 2024 \n Mahsulot sifati: A'lo \n \n",
                                    reply_markup=mers_btn)


@dp.callback_query(F.data == "oq_mers")
async def bmw_function(call: types.CallbackQuery):
    await call.message.answer_photo(
        photo="https://sales.mercedes-sheremetevo.ru/images/news/news_card_collage/crop_6277654.jpg",
        caption="Siz oq rangli Mersni tanladingiz. \n Mahsulot nomi: Tesla \n Narxi: 42000 \n Rangi: oq \n Yili: 2024 \n Mahsulot sifati: A'lo \n \n",
        reply_markup=mers_btn)


@dp.callback_query(F.data == "qizil_mers")
async def bmw_function(call: types.CallbackQuery):
    await call.message.answer_photo(photo="https://journalauto.com/wp-content/uploads/2023/12/Classe-E.jpg",
                                    caption="Siz qizil rangli Mersni tanladingiz. \n Mahsulot nomi: Tesla \n Narxi: 42000 \n Rangi: qizil \n Yili: 2024 \n Mahsulot sifati: A'lo \n \n",
                                    reply_markup=mers_btn)


@dp.callback_query(F.data == "sariq_mers")
async def bmw_function(call: types.CallbackQuery):
    await call.message.answer_photo(
        photo="https://carsdo.ru/job/CarsDo/photo/model/mercedes-benz-a-class-new-1-model.jpg",
        caption="Siz sariq rangli Mersni tanladingiz. \n Mahsulot nomi: Tesla \n Narxi: 42000 \n Rangi: sariq \n Yili: 2024 \n Mahsulot sifati: A'lo \n \n",
        reply_markup=mers_btn)


@dp.callback_query(F.data == "moviy_mers")
async def bmw_function(call: types.CallbackQuery):
    await call.message.answer_photo(
        photo="https://mercedes-benz-uzbekistan.uz/wp-content/uploads/2022/02/image.mq6_.12.20211027111239.webp",
        caption="Siz movif rangli Mersni tanladingiz. \n Mahsulot nomi: Tesla \n Narxi: 42000 \n Rangi: moviy \n Yili: 2024 \n Mahsulot sifati: A'lo \n \n",
        reply_markup=mers_btn)


@dp.callback_query(F.data == "yashil_mers")
async def bmw_function(call: types.CallbackQuery):
    await call.message.answer_photo(
        photo="https://cdn-1.motorsport.com/images/amp/6xEgEAr0/s1000/mercedes-amg-sl63-s-e-performa.jpg",
        caption="Siz yashil rangli Mersni tanladingiz. \n Mahsulot nomi: Tesla \n Narxi: 42000 \n Rangi: Yashil \n Yili: 2024 \n Mahsulot sifati: A'lo \n \n",
        reply_markup=mers_btn)


@dp.callback_query(F.data == "savat_solish_m")
async def savat_function(call: types.CallbackQuery):
    global balance
    balance = balance - 42000
    orders.append(" Mers narxi: 42000$")
    await call.message.answer("Siz Mersni savat soldingiz", reply_markup=main_button)


@dp.callback_query(F.data == "savat_olish_m")
async def savat_function(call: types.CallbackQuery):
    global balance
    balance = balance + 42000
    orders.remove(" Mers narxi: 42000$")
    await call.message.answer("Siz Mersni savat oldingiz", reply_markup=main_button)


@dp.callback_query(F.data == "lambo")
async def bmw_function(call: types.CallbackQuery):
    await call.message.answer_photo(photo="https://hips.hearstapps.com/hmg-prod/images/limitedlambos2-1618325640.jpg",
                                    caption="Siz Lamborghini bo'limini tanladingiz. \n Bu yerdan siz o'zizga yoqqan ranglisini tanlay olasiz !!!",
                                    reply_markup=lambo_button)


@dp.callback_query(F.data == "qora_lambo")
async def bmw_function(call: types.CallbackQuery):
    await call.message.answer_photo(
        photo="https://media.cnn.com/api/v1/images/stellar/prod/191104152639-14-lamborghini-special.jpg?q=w_3077,h_1994,x_0,y_0,c_fill",
        caption="Siz qora rangli Lamborghinini tanladingiz. \n Mahsulot nomi: TLamborghini \n Narxi: 40000 \n Rangi: qora \n Yili: 2024 \n Mahsulot sifati: A'lo \n \n",
        reply_markup=lambo_btn)


@dp.callback_query(F.data == "oq_lambo")
async def bmw_function(call: types.CallbackQuery):
    await call.message.answer_photo(
        photo="https://cdn.motor1.com/images/mgl/OozxwY/0:1003:8000:5993/2024-lamborghini-aventador-successor-rendering.webp",
        caption="Siz oq rangli Lamborghinini tanladingiz. \n Mahsulot nomi: TLamborghini \n Narxi: 40000 \n Rangi: oq \n Yili: 2024 \n Mahsulot sifati: A'lo \n \n",
        reply_markup=lambo_btn)


@dp.callback_query(F.data == "qizil_lambo")
async def bmw_function(call: types.CallbackQuery):
    await call.message.answer_photo(photo="https://repost.uz/storage/uploads/0-1679466294-avto11-post-material.png",
                                    caption="Siz qizil rangli Lamborghinini tanladingiz. \n Mahsulot nomi: TLamborghini \n Narxi: 40000 \n Rangi: qizil \n Yili: 2024 \n Mahsulot sifati: A'lo \n \n",
                                    reply_markup=lambo_btn)


@dp.callback_query(F.data == "sariq_lambo")
async def bmw_function(call: types.CallbackQuery):
    await call.message.answer_photo(
        photo="https://hips.hearstapps.com/hmg-prod/images/2023-lamborghini-huracan-sterrato127-6467c8f12dcce.jpg?crop=0.595xw:0.445xh;0.174xw,0.447xh&resize=1200:*",
        caption="Siz sariq rangliLamborghinisni tanladingiz. \n Mahsulot nomi: TLamborghini \n Narxi: 40000 \n Rangi: sariq \n Yili: 2024 \n Mahsulot sifati: A'lo \n \n",
        reply_markup=lambo_btn)


@dp.callback_query(F.data == "moviy_lambo")
async def bmw_function(call: types.CallbackQuery):
    await call.message.answer_photo(
        photo="https://s3-prod-europe.autonews.com/s3fs-public/styles/1200x630/public/Lamborghini%20Huracan%20STO%20web.jpg",
        caption="Siz movif rangli Lamborghinini tanladingiz. \n Mahsulot nomi: TLamborghini \n Narxi: 40000 \n Rangi: moviy \n Yili: 2024 \n Mahsulot sifati: A'lo \n \n",
        reply_markup=lambo_btn)


@dp.callback_query(F.data == "yashil_lambo")
async def bmw_function(call: types.CallbackQuery):
    await call.message.answer_photo(photo="https://repost.uz/storage/uploads/0-1649788058-avto-post-material.jpeg",
                                    caption="Siz yashil rangli Lamborghinini tanladingiz. \n Mahsulot nomi: TLamborghini \n Narxi: 40000 \n Rangi: Yashil \n Yili: 2024 \n Mahsulot sifati: A'lo \n \n",
                                    reply_markup=lambo_btn)


@dp.callback_query(F.data == "savat_solish_l")
async def savat_function(call: types.CallbackQuery):
    global balance
    balance = balance - 40000
    orders.append(" Lamborghini narxi: 40000$")
    await call.message.answer("Siz Lamborghinini savat soldingiz", reply_markup=main_button)


@dp.callback_query(F.data == "savat_olish_l")
async def savat_function(call: types.CallbackQuery):
    global balance
    balance = balance + 40000
    orders.remove(" Lamborghini narxi: 40000$")
    await call.message.answer("Siz Lamborghinini savat oldingiz", reply_markup=main_button)


@dp.callback_query(F.data == "ford")
async def bmw_function(call: types.CallbackQuery):
    await call.message.answer_photo(
        photo="https://avatars.mds.yandex.net/get-vertis-journal/4080458/4.jpg_1649844806431/orig",
        caption="Siz Mustang bo'limini tanladingiz. \n Bu yerdan siz o'zizga yoqqan ranglisini tanlay olasiz !!!",
        reply_markup=ford_button)


@dp.callback_query(F.data == "qora_ford")
async def bmw_function(call: types.CallbackQuery):
    await call.message.answer_photo(
        photo="https://cdn.dealeraccelerate.com/rkm/1/7040/447761/790x1024/1967-ford-mustang-eleanor-tribute",
        caption="Siz qora rangli Mustangni tanladingiz. \n Mahsulot nomi: Mustang \n Narxi: 41000 \n Rangi: qora \n Yili: 2024 \n Mahsulot sifati: A'lo \n \n",
        reply_markup=ford_btn)


@dp.callback_query(F.data == "oq_ford")
async def bmw_function(call: types.CallbackQuery):
    await call.message.answer_photo(
        photo="https://www.telegraph.co.uk/cars/images/2017/05/05/TELEMMGLPICT000127811726_1_trans_NvBQzQNjv4BqpVlberWd9EgFPZtcLiMQfyf2A9a6I9YchsjMeADBa08.jpeg?imwidth=680",
        caption="Siz oq rangli Mustangni tanladingiz. \n Mahsulot nomi: Mustang \n Narxi: 41000 \n Rangi: oq \n Yili: 2024 \n Mahsulot sifati: A'lo \n \n",
        reply_markup=ford_btn)


@dp.callback_query(F.data == "qizil_ford")
async def bmw_function(call: types.CallbackQuery):
    await call.message.answer_photo(
        photo="https://www.autobild.es/sites/navi.axelspringer.es/public/media/image/2019/04/roush-mustang-stage-3-2019.jpg",
        caption="Siz qizil rangli Mustangni tanladingiz. \n Mahsulot nomi: Mustang \n Narxi: 41000 \n Rangi: qizil \n Yili: 2024 \n Mahsulot sifati: A'lo \n \n",
        reply_markup=ford_btn)


@dp.callback_query(F.data == "sariq_ford")
async def bmw_function(call: types.CallbackQuery):
    await call.message.answer_photo(
        photo="https://mediacloud.carbuyer.co.uk/image/private/s--X-WVjvBW--/f_auto,t_content-image-full-desktop@1/v1646649059/carbuyer/2022/03/Ford%20Mustang%20California%20Special%20convertible-2.jpg",
        caption="Siz sariq rangli Mustangni tanladingiz. \n Mahsulot nomi: Mustang \n Narxi: 41000 \n Rangi: sariq \n Yili: 2024 \n Mahsulot sifati: A'lo \n \n",
        reply_markup=ford_btn)


@dp.callback_query(F.data == "moviy_ford")
async def bmw_function(call: types.CallbackQuery):
    await call.message.answer_photo(
        photo="https://claveyscorner.com/wp-content/uploads/2019/08/2019-Ford-Mustang-EcoBoost-Convertible-Three-Quarter-Front.jpg",
        caption="Siz movif rangli Mustangni tanladingiz. \n Mahsulot nomi: Mustang \n Narxi: 41000 \n Rangi: moviy \n Yili: 2024 \n Mahsulot sifati: A'lo \n \n",
        reply_markup=ford_btn)


@dp.callback_query(F.data == "yashil_ford")
async def bmw_function(call: types.CallbackQuery):
    await call.message.answer_photo(
        photo="https://assets-eu-01.kc-usercontent.com/3b3d460e-c5ae-0195-6b86-3ac7fb9d52db/0d0e8029-5c51-4dab-bd7c-df1932d90e4f/Ford%20Mustang%20%285%29.jpg?width=1750&fm=jpg&auto=format",
        caption="Siz yashil rangli Mustangni tanladingiz. \n Mahsulot nomi: Mustang \n Narxi: 41000 \n Rangi: Yashil \n Yili: 2024 \n Mahsulot sifati: A'lo \n \n",
        reply_markup=ford_btn)


@dp.callback_query(F.data == "savat_solish_f")
async def savat_function(call: types.CallbackQuery):
    global balance
    balance = balance - 41000
    orders.append(" Mustang narxi: 41000$")
    await call.message.answer("Siz Mustangni savat soldingiz", reply_markup=main_button)


@dp.callback_query(F.data == "savat_olish_f")
async def savat_function(call: types.CallbackQuery):
    global balance
    balance = balance + 41000
    orders.remove(" Mustang narxi: 41000$")
    await call.message.answer("Siz Mustangni savat oldingiz", reply_markup=main_button)


# @dp.callback_query(F.data == "sotib_ol")
# async def sotib_function(call: types.CallbackQuery):
#     await call.message.answer("Siz sotib olish bo'limiga o'tdingiz. \n Siz to'lovni 2 usulda amalga oshira olasiz. \n 1-usul Uzcard kartasi orqali \n 2-usul Humo kartasi orqali", reply_markup=kart_button)


@dp.callback_query(F.data == "matiz")
async def bmw_function(call: types.CallbackQuery):
    await call.message.answer_photo(
        photo="https://masterpiecer-images.s3.yandex.net/e7c5d0a0854011ee9e561ad242dc1d78:upscaled",
        caption="Siz Matiz bo'limini tanladingiz. \n Bu yerdan siz o'zizga yoqqan ranglisini tanlay olasiz !!!",
        reply_markup=matiz_button)


@dp.callback_query(F.data == "qora_matiz")
async def bmw_function(call: types.CallbackQuery):
    await call.message.answer_photo(photo="https://avangard29.com/media/posts/80/daewoo-matiz-2012-0001.jpg",
                                    caption="Siz qora rangli Matizni tanladingiz. \n Mahsulot nomi: Matiz \n Narxi: 6000 \n Rangi: qora \n Yili: 2024 \n Mahsulot sifati: A'lo \n \n",
                                    reply_markup=matiz_btn)


@dp.callback_query(F.data == "oq_matiz")
async def bmw_function(call: types.CallbackQuery):
    await call.message.answer_photo(
        photo="https://frankfurt.apollo.olxcdn.com/v1/files/mh2extxrmal42-UZ/image;s=1632x1088",
        caption="Siz oq rangli Matizni tanladingiz. \n Mahsulot nomi: Matiz \n Narxi: 6000 \n Rangi: oq \n Yili: 2024 \n Mahsulot sifati: A'lo \n \n",
        reply_markup=matiz_btn)


@dp.callback_query(F.data == "qizil_matiz")
async def bmw_function(call: types.CallbackQuery):
    await call.message.answer_photo(
        photo="https://upload.wikimedia.org/wikipedia/commons/thumb/e/e8/Daewoo_Matiz_front_20090920.jpg/1200px-Daewoo_Matiz_front_20090920.jpg",
        caption="Siz qizil rangli Matizni tanladingiz. \n Mahsulot nomi: Matiz \n Narxi: 6000 \n Rangi: qizil \n Yili: 2024 \n Mahsulot sifati: A'lo \n \n",
        reply_markup=matiz_btn)


@dp.callback_query(F.data == "sariq_matiz")
async def bmw_function(call: types.CallbackQuery):
    await call.message.answer_photo(
        photo="https://avatars.mds.yandex.net/get-verba/787013/2a000001609bd8dcc792cd4ee02367a24886/cattouch",
        caption="Siz sariq rangli Matizni tanladingiz. \n Mahsulot nomi: Matiz \n Narxi: 6000 \n Rangi: sariq \n Yili: 2024 \n Mahsulot sifati: A'lo \n \n",
        reply_markup=matiz_btn)


@dp.callback_query(F.data == "moviy_matiz")
async def bmw_function(call: types.CallbackQuery):
    await call.message.answer_photo(
        photo="https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcQUbHwsMNtZBvHMdgtb6OUKD_4iU0EqC4K1uGFSpIKRjtGbfWQZTfU2qfepV2GYVTE40nY&usqp=CAU",
        caption="Siz movif rangli Matizni tanladingiz. \n Mahsulot nomi: Matiz \n Narxi: 6000 \n Rangi: moviy \n Yili: 2024 \n Mahsulot sifati: A'lo \n \n",
        reply_markup=matiz_btn)


@dp.callback_query(F.data == "yashil_matiz")
async def bmw_function(call: types.CallbackQuery):
    await call.message.answer_photo(photo="https://storage.kun.uz/source/3/NvRMxGaa2aXAcIY-o87DDl9NUHrgGLp3.jpg",
                                    caption="Siz yashil rangli Matizni tanladingiz. \n Mahsulot nomi: Matiz \n Narxi: 6000 \n Rangi: Yashil \n Yili: 2024 \n Mahsulot sifati: A'lo \n \n",
                                    reply_markup=matiz_btn)


@dp.callback_query(F.data == "savat_solish_mz")
async def savat_function(call: types.CallbackQuery):
    global balance
    balance = balance - 6000
    orders.append(" Matiz narxi: 6000$")
    await call.message.answer("Siz Matizni savat soldingiz", reply_markup=main_button)


@dp.callback_query(F.data == "savat_olish_mz")
async def savat_function(call: types.CallbackQuery):
    global balance
    balance = balance + 6000
    orders.remove(" Matiz narxi: 6000$")
    await call.message.answer("Siz Matizni savat oldingiz", reply_markup=main_button)


@dp.callback_query(F.data == "spark")
async def bmw_function(call: types.CallbackQuery):
    await call.message.answer_photo(
        photo="https://www.autostrada.uz/wp-content/uploads/2018/09/Chevrolet-Spark-Tashkent.jpg",
        caption="Siz Spark bo'limini tanladingiz. \n Bu yerdan siz o'zizga yoqqan ranglisini tanlay olasiz !!!",
        reply_markup=spark_button)


@dp.callback_query(F.data == "qora_spark")
async def bmw_function(call: types.CallbackQuery):
    await call.message.answer_photo(
        photo="https://car24.uz/wp-content/uploads/2024/01/4c78fd8c-654e-41b8-9c1a-5868d6af06c34-1.jpg",
        caption="Siz qora rangli Sparkni tanladingiz. \n Mahsulot nomi: Spark \n Narxi: 8000 \n Rangi: qora \n Yili: 2021 \n Mahsulot sifati: A'lo \n \n",
        reply_markup=spark_btn)


@dp.callback_query(F.data == "oq_spark")
async def bmw_function(call: types.CallbackQuery):
    await call.message.answer_photo(
        photo="https://files.glotr.uz/company/000/013/254/products/2021/01/12/2021-01-12-20-38-08-737413-35b85a161b36adca0f6308234ffae3ab.jpg?_=ozbol",
        caption="Siz oq rangli Sparkni tanladingiz. \n Mahsulot nomi: Spark \n Narxi: 6000 \n Rangi: oq \n Yili: 2021 \n Mahsulot sifati: A'lo \n \n",
        reply_markup=spark_btn)


@dp.callback_query(F.data == "qizil_spark")
async def bmw_function(call: types.CallbackQuery):
    await call.message.answer_photo(photo="https://lionmotors.uz/wp-content/uploads/2020/11/spark3.jpg",
                                    caption="Siz qizil rangli Sparkni tanladingiz. \n Mahsulot nomi: Spark \n Narxi: 6000 \n Rangi: qizil \n Yili: 2021 \n Mahsulot sifati: A'lo \n \n",
                                    reply_markup=spark_btn)


@dp.callback_query(F.data == "sariq_spark")
async def bmw_function(call: types.CallbackQuery):
    await call.message.answer_photo(photo="https://www.kochamyauta.pl/wp-content/uploads/2013/10/sparky2-1.jpg",
                                    caption="Siz sariq rangli Sparkni tanladingiz. \n Mahsulot nomi: Spark \n Narxi: 8000 \n Rangi: sariq \n Yili: 2021 \n Mahsulot sifati: A'lo \n \n",
                                    reply_markup=spark_btn)


@dp.callback_query(F.data == "moviy_spark")
async def bmw_function(call: types.CallbackQuery):
    await call.message.answer_photo(
        photo="https://files.glotr.uz/company/000/013/254/products/2021/01/12/2021-01-12-21-15-07-756714-81ffe7aeff28ef1c35b5fa281a817333.jpg?_=ozbol",
        caption="Siz movif rangli Sparkni tanladingiz. \n Mahsulot nomi: Spark \n Narxi: 8000 \n Rangi: moviy \n Yili: 2021 \n Mahsulot sifati: A'lo \n \n",
        reply_markup=spark_btn)


@dp.callback_query(F.data == "yashil_spark")
async def bmw_function(call: types.CallbackQuery):
    await call.message.answer_photo(photo="https://www.gazeta.uz/media/img/2010/05/1379_m.jpg",
                                    caption="Siz yashil rangli Sparkni tanladingiz. \n Mahsulot nomi: Spark \n Narxi: 8000 \n Rangi: Yashil \n Yili: 2024 \n Mahsulot sifati: A'lo \n \n",
                                    reply_markup=spark_btn)


@dp.callback_query(F.data == "savat_solish_sk")
async def savat_function(call: types.CallbackQuery):
    global balance
    balance = balance - 8000
    orders.append(" Spark narxi: 6000$")
    await call.message.answer("Siz Sparkni savat soldingiz", reply_markup=main_button)


@dp.callback_query(F.data == "savat_olish_sk")
async def savat_function(call: types.CallbackQuery):
    global balance
    balance = balance + 8000
    orders.remove(" Spark narxi: 6000$")
    await call.message.answer("Siz Sparkni savat oldingiz", reply_markup=main_button)


@dp.callback_query(F.data == "sotib_ol")
async def sotib_function(call: types.CallbackQuery):
    await call.message.answer(
        "Siz sotib olish bo'limiga o'tdingiz. \n Siz to'lovni 2 usulda amalga oshira olasiz. \n 1-usul Uzcard kartasi orqali \n 2-usul Humo kartasi orqali",
        reply_markup=kart_button)


@dp.callback_query(F.data == "uzcard")
async def uzcard_function(call: types.CallbackQuery):
    await call.message.answer(
        "Siz to'lovni Uzcard kartasi orqali amalga oshirdingiz. \n To'lovingiz uchun rahmat \n Mahsulot yoqqan bo'lsa biz hursandmiz \n Yana bizdan foydalanishni unutmang. \n Boshiga qaytmoqchi bo'lsangiz Menu bo'limiga o'ting",
        reply_markup=main_button)


@dp.callback_query(F.data == "humo")
async def humo_function(call: types.CallbackQuery):
    await call.message.answer(
        "Siz to'lovni Humo kartasi orqali amalga oshirdingiz. \n To'lovingiz uchun rahmat \n Mahsulot yoqqan bo'lsa biz hursandmiz \n Yana bizdan foydalanishni unutmang. \n Boshiga qaytmoqchi bo'lsangiz Menu bo'limiga o'ting",
        reply_markup=main_button)


@dp.message(F.text == "🛒 Orders")
async def orders_function(message: types.Message):
    await message.answer(f"Siz bor narsalar ro'yxati !!!")
    for i in orders:
        await message.answer(f"Moshina nomi: {i}", reply_markup=main_button)


@dp.message(F.text == "💸 Balance")
async def balance_function(message: types.Message):
    await message.answer(f"Sizning qolgan mablag'ingiz: {balance}", reply_markup=main_button)


async def main():
    await dp.start_polling(bot)


if __name__ == '__main__':
    asyncio.run(main())
