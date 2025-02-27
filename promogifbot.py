import telegram
import time
import schedule

TOKEN = "8149516402:AAHGCMnnEqDVhJ77eBhuQ7LXpJULSIxSWro"
GROUP_CHAT_ID = "-1002480179650"
YOUR_CHAT_ID = "5999695924"

CAPTIONS = [
    "https://onlyfans.com/spicyberry Only $3!!!!!",
    "https://t.me/m/E-uCLNIeODFh $15 to join my nude private",
    "https://www.instagram.com/m00novermyhammyy?igsh=MTg4bHh1MDN2d3E3eA== Follow my IG!!",
    "Wyd 👀 text me https://t.me/LLm00nJ",
    "https://t.me/+DyzmUodPmO9hNWU5 Add my other group!!! Free nude video posted for every 100 new people that join!!!"
]

bot = telegram.Bot(token=TOKEN)

GIF_MESSAGE_IDS = [5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 41, 42, 43, 44, 45, 46, 47, 48, 49, 50, 51, 52, 53, 54, 55, 56, 57, 58, 59, 60, 61, 62, 63, 64, 65, 66, 67, 68, 69, 70, 71, 72, 73, 74, 75, 76, 77, 78, 79, 80, 81, 82, 83, 84, 85, 86, 87, 88, 89, 90, 91, 92, 93, 94, 95, 96, 97, 98, 99, 100, 101, 102, 103, 104, 105, 106, 107, 108, 109, 110, 111, 112, 113, 114, 115, 116, 117, 118, 119, 120, 121, 122, 123, 124, 125, 126, 127, 128, 129, 130, 131, 132, 133, 134, 135, 136, 137, 138, 275, 276, 277, 278, 279, 280, 281, 282, 283, 284, 285, 286, 287, 288, 289, 290, 291, 292, 293, 294, 295, 296, 297, 298, 299, 300, 301, 302, 303, 304, 305, 306, 307, 308, 309, 310, 311, 312, 313, 314, 315, 316, 317, 318, 319, 320, 321, 322, 323, 324, 325, 326, 327, 328, 329, 330, 331, 332, 333, 334, 335, 336, 337, 338, 339, 340, 341, 342, 343, 344, 345, 346, 347, 348, 349, 350, 351, 352, 353, 354, 355, 356, 357, 358, 359, 360, 361, 362, 363, 364, 365, 366, 367, 368, 369, 370, 371, 372, 373, 374, 392, 393, 394, 395, 396, 397, 398, 399, 400, 401, 402, 403, 404, 405, 406, 407, 408, 409, 410, 411, 412, 414, 415, 416, 417, 418, 419, 420, 421, 422, 423, 424, 425, 426]
gif_index = 0
caption_index = 0

def get_saved_gifs():
    if not GIF_MESSAGE_IDS:
        bot.send_message(YOUR_CHAT_ID, "No GIFs loaded yet! Forward some GIFs to me to add them.")
    return GIF_MESSAGE_IDS

def post_gif():
    global gif_index, caption_index
    gif_ids = get_saved_gifs()
    if not gif_ids:
        return
    current_gif_id = gif_ids[gif_index]
    current_caption = CAPTIONS[caption_index]
    try:
        bot.forward_message(
            chat_id=GROUP_CHAT_ID,
            from_chat_id=YOUR_CHAT_ID,
            message_id=current_gif_id
        )
        bot.send_message(chat_id=GROUP_CHAT_ID, text=current_caption)
        print(f"Posted GIF {current_gif_id} with caption {caption_index + 1} at {time.ctime()}")
        gif_index = (gif_index + 1) % len(gif_ids)
        caption_index = (caption_index + 1) % len(CAPTIONS)
    except Exception as e:
        print(f"Error posting GIF: {str(e)}")
        bot.send_message(YOUR_CHAT_ID, f"Failed to post GIF: {str(e)}")

schedule.every(1).hours.do(post_gif)

print("PromoGIFBot is running...")
while True:
    schedule.run_pending()
    time.sleep(60)
