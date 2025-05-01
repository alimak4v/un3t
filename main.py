#---------------------------------------------------------------------------------------------#
#|///////////////////////////////////////////////////////////////////////////////////////////|#
#|///////000//////00-//////000000000///00------00/////000000///////000000/////000000000//////|#
#|//////00-00/////00--/////00------/////00----00////00------00///00------00///------00///////|#
#|/////00---00////00--/////00-----///////00--00////00--++++--00/00--++++--00//-----00////////|#
#|/////00---00////00---////000000000//////0000/////00-++--++-00/00-++--++-00//----00/////////|#
#|////00-----00///00---////00-----///////00--00////00-++--++-00/00-++--++-00//---00//////////|#
#|///0000000000///00----///00----///////00----00///00--++++--00/00--++++--00//--00///////////|#
#|//00---------00/00-----//00---///////00------00///00------00///00------00///-00////////////|#
#|//00---------00/00000000/000000000//00--------00////000000///////000000/////00/////////////|#
#|///////////////////////////////////////////////////////////////////////////////////////////|#
#---------------------------------------------------------------------------------------------#

from logging import basicConfig, INFO
from aiogram import Bot, Dispatcher, executor, types


API_TOKEN = 'YOUR_TG_API'
basicConfig(level=INFO)
bot = Bot(token=API_TOKEN)
dp = Dispatcher(bot)

was_id_before = []
names_clients = []
pub = []
pub_id_admin = []
pub_id_users = [[]]

can_use = "QWERTYUIOPASDFGHJKLZXCVBNMqwertyuiopasdfghjklzxcvbnm1234567890"


@dp.message_handler(commands=['start', 'help'])
async def starting(message: types.Message):
	await message.answer("Чтобы изменить ник или использовать другие команды напиши следующие команды в одну строчку", parse_mode="HTML")
	await message.answer("Чтобы зарегетрироваться в UNet напиши /id <b>Ваш ник</b>", parse_mode="HTML")
	await message.answer("Чтобы изменить имя /change <b>Ваш новый ник</b>", parse_mode="HTML")
	await message.answer("Чтобы создать собственный паблик/канал /new_pub <b>Уникальное имя паблика</b>", parse_mode="HTML")
	await message.answer("Чтобы создать новую запись в собственный паблик/канал /new_post <b>Текст поста</b>", parse_mode="HTML")
	await message.answer("Чтобы войти в существующий паблик /meet_pub <b>Имя паблика</b>", parse_mode="HTML")
	await message.delete()


@dp.message_handler(commands='update')
async def starting(message: types.Message):
	for i in range(0, len(was_id_before)):
		print(was_id_before[i], end=', ')
	print('\n')
	for i in range(0, len(names_clients)):
		print('"' + names_clients[i] + '"', end=', ')
	print('\n')
	await message.delete()


@dp.message_handler(commands=['new_pub'])
async def starting(message: types.Message):
	names_room = message.text[9:]
	pub.append(names_room)
	pub_id_admin.append(message.from_user.id)
	pub_id_users.append([1142177034])
	await message.answer("Новый паблик зарегестрирован", parse_mode="HTML")

	for i in range(0, len(was_id_before)):
		await bot.send_message(was_id_before[i], f"Зарегестрирован новый паблик <b>{names_room}</b>", parse_mode="HTML")

	await message.delete()


@dp.message_handler(commands=['new_post'])
async def starting(message: types.Message):
	post_text = message.text[10:]
	index = -1

	for i in range(0, len(pub_id_admin)):
		if pub_id_admin[i] == message.from_user.id:
			index = i
			break

	if index == -1:
		await message.answer("У тебя нет паблика : (")
		await message.delete()
		return

	for i in range(0, len(pub_id_users[index])):
		await bot.send_message(pub_id_users[index][i], f"<b>{pub[index]}</b>\n{post_text}", parse_mode="HTML")

	await message.delete()


@dp.message_handler(commands=['meet_pub'])
async def starting(message: types.Message):
	names_room = message.text[10:]
	index = -1
	for i in range(0, len(pub)):
		if pub[i] == names_room:
			index = i
			break

	if index == -1:
		await message.answer("Такого паблика не существует : (")
		await message.delete()
		return

	await message.answer("Вы вступили в новый паблик", parse_mode="HTML")

	pub_id_users[index].append(message.from_user.id)
	await message.delete()


@dp.message_handler(commands=['id', 'ID', 'Id'])
async def registration_nick(message: types.Message):
	name = message.text[4:]

	if ("admin" in name.lower() or "adm1n" in name.lower()) and message.from_user.id != 1142177034:
		await message.answer("В твоем нике не может содержаться слово admin")
		await message.delete()
		return

	if len(name) < 2:
		await message.answer("Твой ник должен быть больше 2 символов английского алфавита и цифр")
		await message.delete()
		return

	for i in range(0, len(name)):
		if name[i] not in can_use:
			await message.answer("Твой ник должен быть больше 2 символов английского алфавита и цифр")
			await message.delete()
			return

	for i in range(0, len(was_id_before)):
		if message.from_user.id == was_id_before[i] or name == names_clients[i]:
			await message.answer("Ты был зарегестрирован ранее:)")
			await message.delete()
			return

	was_id_before.append(message.from_user.id)

	for i in range(0, len(was_id_before)):
		await bot.send_message(was_id_before[i], f"<b>{name}</b> --> UNet", parse_mode="HTML")

	names_clients.append(name)
	await message.delete()


@dp.message_handler(commands=['change', 'Change'])
async def changing_nick(message: types.Message):
	name = message.text[8:]

	if "admin" in name.lower() or "adm1n" in name.lower():
		await message.answer("В твоем нике не может содержаться слово admin")
		await message.delete()
		return

	if len(name) < 2:
		await message.answer("Твой ник должен быть больше 2 символов английского алфавита и цифр")
		await message.delete()
		return

	for i in range(0, len(name)):
		if name[i] not in can_use:
			await message.answer("Твой ник должен быть больше 2 символов английского алфавита и цифр")
			await message.delete()
			return

	you_was = 0
	index = 0

	for i in range(0, len(was_id_before)):
		if name.lower == names_clients[i].lower():
			await message.answer("Используй именно свой ник")
			await message.delete()
			return
		if message.from_user.id == was_id_before[i]:
			you_was = 1
			index = i
			break

	if you_was == 0:
		await message.answer("Ты не был зарегистрирован")
		await message.delete()
		return

	for i in range(0, len(was_id_before)):
		await bot.send_message(was_id_before[i], f"<b>{names_clients[index]}</b> ---> {name}", parse_mode="HTML")

	names_clients[index] = name
	await message.delete()


@dp.message_handler(commands=['exit'])
async def update_messages(message: types.Message):
	index = -1
	for i in range(0, len(was_id_before)):
		if was_id_before[i] == message.from_user.id:
			index = i
			break

	if index == -1:
		await message.delete()
		return

	was_id_before.remove(was_id_before[index])
	names_clients.remove(names_clients[index])
	await message.delete()


@dp.message_handler(content_types="text")
async def sending_messages(message: types.Message):
	name = "NONE"

	for i in range(0, len(names_clients)):
		if message.from_user.id == was_id_before[i]:
			name = names_clients[i]
			break

	if name == "NONE":
		await message.answer("Ты не был зарегистрирован")
		await message.delete()
		return

	for i in range(0, len(names_clients)):
		await bot.send_message(was_id_before[i], f"<b>{name}</b>\n{message.text}", parse_mode="HTML")

	await message.delete()


@dp.message_handler(content_types=types.ContentType.STICKER)
async def sending_messages(message: types.Message):
	name = "NONE"

	for i in range(0, len(names_clients)):
		if message.from_user.id == was_id_before[i]:
			name = names_clients[i]
			break

	if name == "NONE":
		await message.answer("Ты не был зарегистрирован")
		await message.delete()
		return

	for i in range(0, len(names_clients)):
		await bot.send_message(was_id_before[i], f"<b>{name}</b>", parse_mode="HTML")
		await bot.send_sticker(was_id_before[i], message.sticker.file_id)

	await message.delete()


if __name__ == "__main__":
	executor.start_polling(dp, skip_updates=True)
