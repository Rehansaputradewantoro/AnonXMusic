from pyrogram.errors.exceptions.bad_request_400 import UserNotParticipant
from pyrogram.enums import ChatMemberStatus
from config import OWNER_ID, FORCE_SUB_CHANNEL

async def is_subscribed(filter, client, update):
    user_id = update.from_user.id
    if user_id in OWNER_ID:
        return True
    
    if not FORCE_SUB_CHANNEL:
        return False
    
    try:
        member1 = await client.get_chat_member(chat_id=FORCE_SUB_CHANNEL, user_id=user_id)
        
        if member1.status in [ChatMemberStatus.OWNER, ChatMemberStatus.ADMINISTRATOR, ChatMemberStatus.MEMBER]:
            return True
    except UserNotParticipant:
        pass
    
    return False